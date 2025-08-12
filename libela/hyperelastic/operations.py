"""
operations.py
=============

Symbolic stress utilities built on SymPy + NumPy.

A material model class (e.g. :class:`~libela.hyperelastic.hyperelastic.neohookean`) should inherit from
:class:`operations` and override :meth:`energy` to supply its strain-energy
function *W(I₁, I₂, J,…)*.  The mix-in then provides:

* :py:meth:`operations.stress` - convert principal stretches → stress array
* deformation-gradient builders for common test protocols
* tiny numerical plotting helper

.. note::
   See :doc:`/theory/material_models` for mathematical background and :doc:`/user_guide/hyperelastic/overview` for usage examples.

Dependencies
------------
* sympy >= 1.12
* numpy >= 1.24
* matplotlib (for optional plotting)
"""

from __future__ import annotations
import sympy as sp
import numpy as np
# Define the symbols for invariants to share across all materials.
(I1_sym, I2_sym, J_sym) = sp.symbols('I1 I2 J')

class operations:
    """
    Mix-in for symbolic stress and fitting utilities.

    Subclasses must implement an `energy` method that returns a symbolic
    expression in terms of the invariants I1, I2 (and optionally J),
    and must define a `param_symbols_list` attribute in their __init__.

    Provides
    --------
    stress : Compute stress response for a given loading protocol.
    fit : Parameter fitting (placeholder).

    Examples
    --------
    >>> class MyModel(operations):
    ...     def __init__(self):
    ...         self.param_symbols_list = [...]
    ...     def energy(self):
    ...         return ...
    >>> model = MyModel()
    >>> sigma = model.stress(strain, params)
    """
    param_symbols_list = []
    def stress(self, 
               strain: np.ndarray | float, 
               params: list[float],  
               *,
               protocol: str | None = None, 
               stress_type: str | None = None, 
               strain_type: str | None = None,
               plot: bool = False):
        """
        Compute stress response for a given loading protocol.

        Parameters
        ----------
        strain : array_like or float
            Principal stretch (uniaxial/shear) or array for biaxial tests.
        params : list of float
            Material parameters in the same order as the symbols in `energy`.
        protocol : {'uniaxial', 'simple_shear', 'biaxial'}, optional
            Deformation protocol to use. Default is 'uniaxial'.
        stress_type : {'cauchy', 'piola', '2nd-piola'}, optional
            Stress measure to return. Default is 'cauchy'.
        strain_type : {'stretch', 'engineering'}, optional
            Input strain type. Default is 'stretch'.
        plot : bool, optional
            If True, show a quick Matplotlib plot.

        Returns
        -------
        np.ndarray or tuple of np.ndarray
            Stress values for the specified protocol.
        """
        compressible_flag = getattr(self, "compressible", False)
        if compressible_flag and len(params) < 2:
            raise ValueError("Compressible model needs [K, MU] parameters.")
        
        model_param_syms = self.param_symbols_list
        
        strain = strain_converter(strain, strain_type or "stretch")
        stress_type = stress_type or 'cauchy'
        strain_type = strain_type or 'stretch'
        protocol = protocol or 'uniaxial'
        
        #deformation gradient & tensors
        F = deformation_gradient_matrix(protocol, compressible=compressible_flag)
        self.F = F
        J_expr = F.det()  # symbolic determinant of F
        
        # Invariant symbols
        P = sp.symbols('P')
        
        #Invariants from F
        F_inverse = F.inv()
        F_inverse_transpose = sp.transpose(F_inverse)
        b = F * sp.transpose(F)
        b_inverse = b.inv()
        b2 = b * b 
        
        I1 = b.trace()
        I2 = 1 / 2 * (b.trace()**2 - b2.trace())
        
        # Strain-energy expression 
        energy_expr = self.energy() # call energy function without passing J_sym.
        
        #First derivatives, *then* substitute I1, I2, J
        invariant_subs = {I1_sym: I1, I2_sym: I2, J_sym: J_expr}
        diff1_W = sp.diff(energy_expr, I1_sym).subs(invariant_subs)
        diff2_W = sp.diff(energy_expr, I2_sym).subs(invariant_subs)
        
        #Isochoric part
        sigma_expression = 2 * (diff1_W * b) - 2 * (diff2_W * b_inverse)
        
        if compressible_flag:
            dW_dJ = sp.diff(energy_expr, J_sym ).subs(invariant_subs)
            sigma_expression += J_expr * dW_dJ * sp.eye(3)  # volumetric part
        
        # add Lagrange multiplier for incompressible model
        else:
            sigma_expression -= P * sp.eye(3)  # incompressible part
        
        #choose stress measure
        
        if stress_type == 'piola':
            sigma_cauchy_incompressible = sigma_expression - P * sp.eye(3)
            sigma_piola_incompressible = sigma_cauchy_incompressible * F_inverse_transpose
            sigma_tensor = sigma_piola_incompressible
        elif stress_type == '2nd-piola':
            sigma_cauchy_incompressible = sigma_expression - P * sp.eye(3)
            sigma_piola_incompressible = sigma_cauchy_incompressible * F_inverse_transpose
            sigma_2nd_piola_incompressible = F_inverse * sigma_piola_incompressible
            sigma_tensor = sigma_2nd_piola_incompressible
        else:
            sigma_tensor = sigma_expression
        
        #protocol specific stress solver
            
        if protocol == 'uniaxial':
            stress_component_expr = sigma_tensor[0, 0]  # Uniaxial stress component
            lam_s = sp.symbols('lamda')
            
            if compressible_flag:
                lambdify_args = [lam_s] + model_param_syms
                stress_fn = sp.lambdify(lambdify_args, stress_component_expr, 'numpy')
            
            else:
                stress_fn = uniaxial_solver(sigma_tensor, P, model_param_syms)
            
            stress_values = stress_fn(strain, *params)

        elif protocol == 'simple_shear':
            stress_12_function = simple_shear_solver(sigma_tensor)
            stress_values = stress_12_function(strain, *params)
            #return stress_12_function(strain, *params)

        elif protocol == 'biaxial':
            stress_11_function, stress_22_function = biaxial_solver(sigma_tensor)
            stress_11_values = stress_11_function(strain[0, :], strain[1, :], *params)
            stress_22_values = stress_22_function(strain[0, :], strain[1, :], *params)
            stress_values = (stress_11_values, stress_22_values)
            #return (stress_11_function(strain[0, :], strain[1, :], *params), stress_22_function(strain[0, :], strain[1, :], *params))
        else:
            raise ValueError(f"Unknown protocol: {protocol}")
        
        model_name = self.__class__.__name__
        
        if plot:
            _plot_stress_strain(strain, stress_values, 
                        protocol, 
                        stress_type,  
                        strain_type or "stretch",
                        self.__class__.__name__)
            
        return stress_values
    
    def fit(self):
        """
        Placeholder for parameter-fitting routine.

        Returns
        -------
        sympy.Expr
            Example symbolic derivative.
        """
        x = sp.Symbol('x')
        return sp.diff(x**2, x)

# --------------------------------------------------------------------------
# helper functions 
# --------------------------------------------------------------------------

def strain_converter(strain, strain_type):
    """
    Convert input strain into principal stretches (λ) based on the specified strain type.

    Parameters
    ----------
    strain : array_like or float
        The input strain array. Can be engineering strain (ε) or direct stretch (λ).
    strain_type : {'engineering', 'stretch'}
        Type of input strain:
        - 'engineering': Interprets input as ε, returns λ = 1 + ε.
        - 'stretch': Returns the input as-is.

    Returns
    -------
    np.ndarray
        Normalized array of stretches λ.

    Raises
    ------
    ValueError
        If an invalid strain type is provided.
        
    
    """
    strain = np.asarray(strain)
    
    if strain_type == 'engineering':
        return 1 + strain
    elif strain_type == 'stretch':
        return strain
    else:
        raise ValueError("Invalid strain type. Use 'engineering' or 'stretch'")
    
def deformation_gradient_matrix(protocol: str = 'uniaxial', *, compressible: bool = False):
    """
    Return the symbolic deformation gradient tensor F for a given loading protocol.

    Parameters
    ----------
    protocol : {'uniaxial', 'simple_shear', 'biaxial'}
        Type of deformation protocol.
    compressible : bool, optional
        If True, no lateral contraction is enforced (J ≠ 1 in uniaxial).

    Returns
    -------
    sympy.Matrix
        A 3x3 symbolic deformation gradient matrix F.

    Examples
    --------
    >>> F = deformation_gradient_matrix('uniaxial')
    """
    lamda, lamda1, lamda2 = sp.symbols('lamda lamda1 lamda2')

    if protocol == 'uniaxial':
        if compressible: #if specified as compressible, no lateral contraction is enforced
            return sp.Matrix([[lamda, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]])
        return sp.Matrix([[lamda, 0, 0],
                          [0, 1/sp.sqrt(lamda), 0],
                          [0, 0, 1/sp.sqrt(lamda)]])
    elif protocol == 'simple_shear':
        return sp.Matrix([[1, lamda, 0],
                          [0, 1, 0],
                          [0, 0, 1]])
    elif protocol == 'biaxial':
        if compressible: #added compressibility flag for biaxial protocol
            return sp.Matrix([[lamda1, 0, 0],
                              [0, lamda2, 0],
                              [0, 0, 1]])
        return sp.Matrix([[lamda1, 0, 0],
                          [0, lamda2, 0],
                          [0, 0, 1/(lamda1*lamda2)]])
    else:
        raise ValueError(f"Unknown protocol: {protocol}. Supported protocols are 'uniaxial', 'simple_shear', 'biaxial'.")

# ---- protocol-specific solvers ---------------------------
def uniaxial_solver(sigma_tensor, P, model_param_symbols):
    """
    Generate a function to solve for uniaxial stress given a symbolic stress tensor.

    Parameters
    ----------
    sigma_tensor : sympy.Matrix
        Symbolic stress tensor.
    P : sympy.Symbol
        Lagrange multiplier for incompressibility.
    model_param_symbols : list
        List of model parameter symbols.

    Returns
    -------
    function
        Function that computes uniaxial stress for given stretches and parameters.
    """
    #P = sp.symbols('P')
    Eq = sp.Eq(sigma_tensor[1,1], 0) # Enforcing component 22 of stress = 0
    P_val = sp.solve(Eq, P)[0] # Solving the symbolic expression for P 
    P_sub_val = P_val
    
    stress_tensor = sigma_tensor[0,0].subs(P, P_sub_val) # Substituting the expression of P into the component 11 of stress
    
    lam_s = sp.symbols('lamda')
    lambdify_args = [lam_s] + model_param_symbols
    return sp.lambdify(lambdify_args, stress_tensor, 'numpy')

def simple_shear_solver(sigma_tensor):
    """
    Generate a function to solve for simple shear stress given a symbolic stress tensor.

    Parameters
    ----------
    sigma_tensor : sympy.Matrix
        Symbolic stress tensor.

    Returns
    -------
    function
        Function that computes shear stress for given strains and parameters.
    """
    stress_tensor = sigma_tensor[0,1] # Shear stress component
    symbols = sorted (
        stress_tensor.free_symbols,
        key = lambda s: (s.name != 'lamda', s.name)
        ) # This is used to make sure that input parameters are sorted and also lamda comes in the first place
    return sp.lambdify(symbols, stress_tensor, 'numpy')

def biaxial_solver(sigma_tensor):
    """
    Generate functions to solve for biaxial stress components given a symbolic stress tensor.

    Parameters
    ----------
    sigma_tensor : sympy.Matrix
        Symbolic stress tensor.

    Returns
    -------
    tuple of functions
        Functions that compute σ₁₁ and σ₂₂ for given stretches and parameters.
    """
    P = sp.symbols('P')
    Eq = sp.Eq(sigma_tensor[2,2], 0) # Enforcing out-of-plane stress = 0
    P_val = sp.solve(Eq, P)[0]
    stress_1 = sigma_tensor[0,0].subs(P, P_val)
    stress_2 = sigma_tensor[1,1].subs(P, P_val)
    symbols1 = sorted(
        stress_1.free_symbols, 
        key=lambda s: (s.name not in ['lamda1', 'lamda2'], s.name)
    ) # This is used to make sure that input parameters are sorted and also lamda1 and lamda2 comes in the first place
    symbols2 = sorted(
        stress_2.free_symbols, 
        key=lambda s: (s.name not in ['lamda1', 'lamda2'], s.name)
    ) # This is used to make sure that input parameters are sorted and also lamda1 and lamda2 comes in the first place
    return (
        sp.lambdify(symbols1, stress_1, 'numpy'),
        sp.lambdify(symbols2, stress_2, 'numpy')        
    )

# ---- plotting helper ------------------------------------------------------

def _plot_stress_strain(strain, stress_values, protocol, stress_type, strain_type, model_name):
    """
    Plot stress-strain response for a given protocol and model.

    Parameters
    ----------
    strain : array_like
        Input strain values.
    stress_values : array_like
        Computed stress values.
    protocol : str
        Deformation protocol used.
    stress_type : str
        Type of stress measure.
    strain_type : str
        Type of strain measure.
    model_name : str
        Name of the material model.
    """
  
    
    import matplotlib.pyplot as plt

    plt.figure(figsize=(7,5))

    if protocol in ["uniaxial", "shear"]:

        plt.plot(strain, stress_values, 'o-', label = 'stress')
    else:
        plt.plot(strain[0, :], stress_values[0], 'o-', label = 'stress 11')
        plt.plot(strain[1, :], stress_values[1], 's-', label = 'stress 22')
        
    plt.xlabel(strain_type)
    plt.ylabel(stress_type)
    plt.title(f"{model_name}: {protocol}")
    plt.grid(True)
    plt.legend()
    plt.show()
          
