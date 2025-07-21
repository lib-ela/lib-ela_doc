"""
Hyperelastic material models
============================

Each class is a thin functional wrapper around :class:`operations`, providing a
symbolic strain-energy expression *W = W(I₁, I₂, J, …)* that can be fed back
into helper functions from :class:`operations` to compute stress, fit parameters,
etc.

.. note::
   See :doc:`/theory/material_models` for mathematical background and :doc:`/user_guide/hyperelastic/overview` for usage examples.

Public API
----------
neo_hookean      — incompressible or compressible Neo-Hookean
mooney_rivlin    — two-parameter Mooney-Rivlin
klosner_segal    — four-term Klosner-Segal
yeoh             — three-term Yeoh
polynomial       — full nine-term polynomial

Notes
-----
* All symbols are generated on the fly so they remain unique in SymPy's cache.
* Incompressibility is assumed (**J = 1**) unless 
  ``compressible=True`` and a bulk modulus *K* is supplied.
"""

from __future__ import annotations #allows annotations to be stored as strings

import sympy as sp
from .operations import operations, I1_sym, J_sym, I2_sym

class neohookean(operations):
    """
    Compressible or incompressible Neo-Hookean strain-energy model.

    Inherits from
    -------------
    operations

    Parameters
    ----------
    compressible : bool, optional
        If True, a bulk-modulus term ``K/2*(J - 1)**2`` is added.
        Defaults to False (incompressible, i.e. J = 1).

    Examples
    --------
    >>> model = neohookean(mu=1.0)
    >>> W = model.energy()
    """
    def __init__(self, *, compressible: bool = False):
        """
        Initialize a Neo-Hookean material model.

        Parameters
        ----------
        compressible : bool, optional
            If True, include a bulk modulus term for compressibility.
            Defaults to False.
        """
        self.compressible = compressible
        super().__init__()
        self.param_symbols_list = []
        if self.compressible:
            # K_sym is defined first for compressible to match params=[K, MU]
            self.K_sym = sp.symbols('a_K')
            self.param_symbols_list.append(self.K_sym)
        self.mu_sym = sp.symbols('a_mu')
        self.param_symbols_list.append(self.mu_sym)

    def energy(self):
        """
        Return the symbolic strain-energy function for the Neo-Hookean model.

        Returns
        -------
        sympy.Expr
            The strain-energy function :math:`W = \\frac{\\mu}{2}(I_1 - 3)` (plus volumetric term if compressible).
        """
        (mu_sym,) = sp.symbols('a_mu')
        W_neohookean = self.mu_sym/2 * (I1_sym - 3)
        if self.compressible:
            W_neohookean += self.K_sym/2 * (J_sym - 1)**2
        return W_neohookean

class mooneyrivlin(operations):
    """
    Two-parameter Mooney–Rivlin strain-energy model.

    Inherits from
    -------------
    operations

    Examples
    --------
    >>> model = mooneyrivlin()
    >>> W = model.energy()
    """
    def energy(self):
        """
        Return the symbolic strain-energy function for the Mooney–Rivlin model.

        Returns
        -------
        sympy.Expr
            The strain-energy function :math:`W = C_1(I_1-3) + C_2(I_2-3)`.
        """
        (c10_sym, c01_sym, I1_sym, I2_sym) = sp.symbols('a_c10 b_c01 I1 I2')
        W_mooneyrivlin = c10_sym*(I1_sym-3) + c01_sym*(I2_sym-3)
        return W_mooneyrivlin

class klosnersegal(operations):
    """
    Four-term Klosner–Segal strain-energy model.

    Inherits from
    -------------
    operations

    Examples
    --------
    >>> model = klosnersegal()
    >>> W = model.energy()
    """
    def energy(self):
        """
        Return the symbolic strain-energy function for the Klosner–Segal model.

        Returns
        -------
        sympy.Expr
            The strain-energy function.
        """
        (c11_sym, c21_sym, c22_sym, c23_sym, I1_sym, I2_sym) = sp.symbols('a_c11 b_c21 c_c22 d_c23 I1 I2')
        W_klosnersegal = (c11_sym*(I1_sym - 3) 
                        + c21_sym*(I2_sym - 3)
                        + c22_sym*(I2_sym - 3)**2
                        + c23_sym*(I2_sym - 3)**3)
        return W_klosnersegal

class yeoh(operations):
    """
    Three-term Yeoh strain-energy model (I1-based).

    Inherits from
    -------------
    operations

    Examples
    --------
    >>> model = yeoh()
    >>> W = model.energy()
    """
    def energy(self):
        """
        Return the symbolic strain-energy function for the Yeoh model.

        Returns
        -------
        sympy.Expr
            The strain-energy function.
        """
        (c10_sym, c20_sym, c30_sym, I1_sym) = sp.symbols('a_c10 b_c20 c_c20 I1')
        W_yeoh = (c10_sym*(I1_sym - 3) 
                + c20_sym*(I1_sym - 3)**2
                + c30_sym*(I1_sym - 3)**3)
        return W_yeoh

class polynomial(operations):
    """
    Nine-term polynomial hyperelastic model.

    Inherits from
    -------------
    operations

    Examples
    --------
    >>> model = polynomial()
    >>> W = model.energy()
    """
    def energy(self):
        """
        Return the symbolic strain-energy function for the polynomial model.

        Returns
        -------
        sympy.Expr
            The strain-energy function.
        """
        (c10_sym, c01_sym, c20_sym, c11_sym, c02_sym, c30_sym,
        c21_sym, c12_sym, c03_sym, I1_sym, I2_sym ) = sp.symbols(
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
                    + c03_sym*(I2_sym - 3)**3)
        return W_polynomial
    





