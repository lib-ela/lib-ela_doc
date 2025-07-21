import sympy as sp
import numpy as np

def energy_function(energy_type):
     
    if energy_type == 'neo_hookean':
        # Define symbols
        mu, I1_sym, lamda, P = sp.symbols('mu I1 lamda P')
        # Define strain energy function for Neo-Hookean material
        W = mu/2*(I1_sym-3)
        # Compute derivatives
        diff1_W = sp.diff(W,I1_sym)
        return {
        'diff1_W': diff1_W,
    }
    elif energy_type == 'mooney_rivlin':
        # Define symbols
        c10, c01, I1_sym, I2_sym = sp.symbols('c10 c01 I1 I2')
        # Define strain energy function for mooney_rivlin material
        W = c10/2*(I1_sym-3) + c01/2*(I2_sym-3)
        # Compute derivatives
        diff1_W = sp.diff(W,I1_sym)
        # Compute derivatives
        diff2_W = sp.diff(W,I2_sym)

        return {
        'diff1_W': diff1_W,
        'diff2_W': diff2_W,
    }     
    else:
        raise ValueError("Invalid energy type. ")