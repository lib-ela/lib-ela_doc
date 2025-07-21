#write the class here
import sympy as sp
import numpy as np
from libela.hyperelastic.deformation_gradient import protocol_type, deformation_gradient_properties

def strain_type(strain_input, strain):
    strain_input = np.asarray(strain_input)
    
    if strain == 'engineering':
        return  1 + strain_input
    elif strain  == 'true':
        return  np.exp(strain_input)
    elif strain  == 'green':
        return  np.sqrt(2 * strain_input + 1)
    # elif strain  == ('almansi'):
    #    return  0.5 * (1 - 1/(strain_input)**2)
    elif strain == 'stretch':
        return strain_input
    else:
        raise ValueError("Invalid strain type. Use 'engineering', 'true', 'green', 'almansi', or 'stretch'.")

def uniaxial_solver(Sigma_tensor):
    """
    Solves for the uniaxial protocol by setting stress in
    direction 22 (here we use this case) or 33 to zero.
    Note, regardless of the energy function, for uniaxial
    protocol of incompressible materials, the component 11
    is calculated as follows: 

    Parameters
    ----------
    Sigma_tensor : sympy.Matrix
        The stress tensor.
    
    Returns
    -------
    function
        a lambda function computing the uniaxial stress
        component in terms of the principal stretch.
    """
    P = sp.symbols('P')
    Eq = sp.Eq(Sigma_tensor[1,1], 0) # Enforcing component 22 of stress = 0
    P_val = sp.solve(Eq, P)[0] # Solving the symbolic expression for P 
    stress_tensor = Sigma_tensor[0,0].subs(P, P_val) # Substituting the expression of P into the component 11 of stress
    # This is used to make sure that input parameters are sorted and also lamda comes in the first place
    #stress_func = sp.lambdify(symbols, stress_tensor, 'numpy')
    #print(stress_tensor)
    symbols = sorted(
        stress_tensor.free_symbols, 
        key=lambda s: (s.name != 'lamda', s.name)
    )
    return sp.lambdify(symbols, stress_tensor, 'numpy')

def simple_shear_solver(Sigma_tensor):
    """
    Computes the shear stress component for a simple shear
    test. 

    Parameters
    ----------
    Sigma_tensor : sympy.Matrix
        The stress tensor.

    Returns
    -------
    function
        A lambda function computing the shear stress component. 
    """
    stress_tensor = Sigma_tensor[0,1] # Shear stress component
    symbols = sorted (
        stress_tensor.free_symbols,
        key = lambda s: (s.name != 'lamda', s.name)
    ) # This is used to make sure that input parameters are sorted and also lamda comes in the first place
    return sp.lambdify(symbols, stress_tensor, 'numpy')

def biaxial_solver(Sigma_tensor):
    """
    Solves for the biaxial stress protocol by setting the out-of-plane stress component to zero.

    Parameters
    ----------
    Sigma_tensor : sympy.Matrix
        The stress tensor.

    Returns
    -------
    tuple of functions
        Lambda functions computing the two in-plane stress components as function of the principal stresses.
    """
    P = sp.symbols('P')
    Eq = sp.Eq(Sigma_tensor[2,2], 0) # Enforcing out-of-plane stress = 0
    P_val = sp.solve(Eq, P)[0]
    stress_1 = Sigma_tensor[0,0].subs(P, P_val)
    stress_2 = Sigma_tensor[1,1].subs(P, P_val)
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

def deformation(protocol):
    F = protocol_type(protocol)
    props = deformation_gradient_properties(F)
    I1 = props['I1']
    I2 = props['I2']
    return I1, I2

def stress_calculation(protocol):
    F = protocol_type(protocol) 
    props = deformation_gradient_properties(F)
    F_inverse = props['F_inverse']
    F_inverse_transpose = props['F_inverse_transpose']
    b = props['b']
    b_inv = props['b_inv']
    I2 = props['I2']
    return F, props, F_inverse, F_inverse_transpose, b, b_inv, I2       

def neohookean():
    (mu_sym, 
     I1_sym
    ) = sp.symbols('a_mu I1')
    W_neohookean = mu_sym/2*(I1_sym-3)
    diff1_W = sp.diff(W_neohookean, I1_sym)
    diff2_W = 0
    return diff1_W, diff2_W

def mooneyrivlin():
    (c10_sym, c01_sym, 
     I1_sym, I2_sym
    ) = sp.symbols('a_c10 b_c01 I1 I2')
    W_mooneyrivlin = c10_sym*(I1_sym-3) + c01_sym*(I2_sym-3)
    diff1_W = sp.diff(W_mooneyrivlin,I1_sym)
    diff2_W = sp.diff(W_mooneyrivlin,I2_sym)
    return diff1_W, diff2_W 

def klosnersegal(protocol):
    (c11_sym, c21_sym, c22_sym, c23_sym, 
     I1_sym, I2_sym
    ) = sp.symbols('a_c11 b_c21 c_c22 d_c23 I1 I2')
    W_klosnersegal = (c11_sym*(I1_sym - 3) 
                      + c21_sym*(I2_sym - 3)
                      + c22_sym*(I2_sym - 3)**2
                      + c23_sym*(I2_sym - 3)**3
    )
    _ , I2 = deformation(protocol)
    diff1_W = sp.diff(W_klosnersegal,I1_sym)
    diff2_W_ = sp.diff(W_klosnersegal,I2_sym) 
    diff2_W = diff2_W_.subs(I2_sym, I2)
    return W_klosnersegal

def yeoh(protocol):
    (c10_sym, c20_sym, c30_sym, 
     I1_sym
    ) = sp.symbols('a_c10 b_c20 c_c20 I1')
    W_yeoh = (c10_sym*(I1_sym - 3) 
            + c20_sym*(I1_sym - 3)**2
            + c30_sym*(I1_sym - 3)**3
    )
    I1 , _ = deformation(protocol)

    diff1_W_ = sp.diff(W_yeoh,I1_sym) 
    diff1_W = diff1_W_.subs(I1_sym, I1)
    diff2_W = 0
    return diff1_W, diff2_W

def polynomial(protocol):
    (c10_sym, c01_sym, c20_sym, c11_sym, c02_sym, c30_sym,
     c21_sym, c12_sym, c03_sym, 
     I1_sym, I2_sym ) = sp.symbols(
        '''a_c10 b_c01 c_c20 d_c11 e_c02 f_c30 
           g_c21 h_c12 i_c03 I1 I2'''
    )
    W_polynomial =(c10_sym*(I1_sym - 3)
                 + c01_sym*(I2_sym - 3)
                 + c20_sym*(I1_sym - 3)**2
                 + c11_sym*(I1_sym - 3)*(I2_sym - 3)
                 + c02_sym*(I2_sym - 3)**2
                 + c30_sym*(I1_sym - 3)**3
                 + c21_sym*(I1_sym - 3)**2 * (I2_sym - 3)
                 + c12_sym*(I1_sym - 3)*(I2_sym - 3)**2
                 + c03_sym*(I2_sym - 3)**3
    )
    I1 , I2 = deformation(protocol)
    diff1_W_ = sp.diff(W_polynomial,I1_sym)
    diff2_W_ = sp.diff(W_polynomial,I2_sym)

    subs_dict = {I1_sym: I1, I2_sym: I2}
    diff1_W = diff1_W_.subs(subs_dict)
    diff2_W = diff2_W_.subs(subs_dict)
    return diff1_W, diff2_W

def stress_calculator(model = None, 
                      protocol = None, 
                      stress = None, 
                      strain = None):

    model = model or 'neohookean'
    protocol = protocol or 'uniaxial'
    stress = stress or 'cauchy'
    strain = strain or 'stretch'  

    model_map = {
        'neohookean': neohookean,
        'mooneyrivlin': mooneyrivlin,
        'klosnersegal': lambda: klosnersegal(protocol),
        'yeoh': lambda: yeoh(protocol),
        'polynomial': lambda: polynomial(protocol)
    }  

    if model not in model_map:
        raise ValueError(f"Unknown hyperelastic model: {model}")

    (F, 
     props, 
     F_inverse,
     F_inverse_transpose,
     b,
     b_inv,
     I2
    ) = stress_calculation(protocol)
    

    diff1_W, diff2_W = model_map[model]()
    Sigma = 2 * (diff1_W * b) - 2 * (diff2_W * b_inv)

    Sigma
    P = sp.symbols('P')
    Sigma_Cauchy = Sigma - P * sp.eye(3)
    Sigma_Piola = Sigma_Cauchy * F_inverse_transpose if stress in ['piola', '2nd-piola'] else None

    sigma_dic = {
        'cauchy':Sigma_Cauchy,
        'piola':Sigma_Piola,
        '2nd-piola': F_inverse * Sigma_Piola if stress == '2nd-piola' else None
    }

    if protocol == 'uniaxial': 
        stress_func = uniaxial_solver(sigma_dic[stress])
        return stress_func
    
    elif protocol == 'simple_shear':  
         stress_func = simple_shear_solver(sigma_dic[stress])
         return stress_func
    
    elif protocol == 'biaxial':
        stress_func = biaxial_solver(sigma_dic[stress])
        stress1, stress2 = stress_func     
        return (stress1, stress2)
    return None

def hyperelastic(strain_input, params, 
                 model = None, 
                 protocol = None, 
                 stress = None, 
                 strain = None):
    model = model or 'neohookean'
    protocol = protocol or 'uniaxial'
    stress = stress or 'cauchy'
    strain = strain or 'stretch'    

    strain_input = strain_type(strain_input, strain)

    if protocol == 'uniaxial':
        stress_func = stress_calculator(model, protocol, stress, strain)
        return np.vectorize(stress_func)(strain_input, *params)
    
    elif protocol == 'simple_shear':  
         stress_func = stress_calculator(model, protocol, stress, strain)
         return np.vectorize(stress_func)(strain_input, *params)
    
    elif protocol == 'biaxial':
        stress_func = stress_calculator(model, protocol, stress, strain)
        stress1, stress2 = stress_func  

        return (np.vectorize(stress1)(strain_input[0, :], strain_input[1, :], *params),
                np.vectorize(stress2)(strain_input[0, :], strain_input[1, :], *params)
            )
    return None

print(hyperelastic(((2,3),(2,3)), [2,3], model = 'mooneyrivlin', protocol = 'biaxial', stress='cauchy'))

# print(hyperelastic((2,3), [2], model = 'neohookean', protocol = 'uniaxial', stress='cauchy'))
# print(hyperelastic((2,3), [2,3], model = 'mooneyrivlin', protocol = 'uniaxial', stress='cauchy'))
