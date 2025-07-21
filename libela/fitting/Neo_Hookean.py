import sympy as sp
import numpy as np
# from strain_measure import strain_to_stretch
from deformation_gradient import deformation_function
from deformation_gradient import deformation_gradient_properties
from energy_functions import energy_function

# Define symbols
mu, I1_sym, lamda, P = sp.symbols('mu I1 lamda P')

# Define strain energy function for Neo-Hookean material
W = mu/2*(I1_sym-3)

# Compute derivatives
diff1_W = sp.diff(W,I1_sym)

def stress(mu1, strain, energy_ ='neo_hookean',deformation_type = 'uniaxial', stress_type = 'Cauchy', strain_type = 'stretch'):
    
    lambda1 = strain_to_stretch(strain, strain_type)
    F = deformation_function(deformation_type)
    props = deformation_gradient_properties(F) 

    # Access properties using the dictionary
    F_inverse = props['F_inverse']
    F_inverse_transpose = props['F_inverse_transpose']
    b = props['b']
    I1 = props['I1']
    I3 = props['I3']   

    if energy_ == 'neo_hookean':
        energy_props = energy_function(energy_)
        diff1_W = energy_props['diff1_W']
        Sigma = 2 * (1/I3) * (diff1_W*b)

    elif energy_type == 'mooney_rivlin':
        energy_props = energy_function(energy_)
        diff1_W = energy_props['diff1_W']    
        diff2_W = energy_props['diff2_W'] 
        Sigma = 2 * (1/I3) * (diff1_W*b)


    # Define the Raw stress tensor
    
    Sigma_Cauchy = Sigma - P * sp.eye(3)
    # Define the Piola stress tensor
    Sigma_Piola = I3 * Sigma_Cauchy * F_inverse_transpose
    # Define the Second Piola stress tensor
    Sigma_S = F_inverse * Sigma_Piola 

    if deformation_type == 'uniaxial':
        # Solve for hydrostatic pressure P to satisfy stress equilibrium
        Eq_Cauchy = sp.Eq(Sigma_Cauchy[1,1],0)
        P_Cauchy = sp.solve(Eq_Cauchy,P)[0]    

        # Substitute P into the stress tensor and extract S1
        S1_Cauchy = Sigma_Cauchy[0,0].subs(P, P_Cauchy)
        S1_Piola = Sigma_Piola[0,0].subs(P, P_Cauchy)
        S1_S = Sigma_S[0,0].subs(P, P_Cauchy)

        # Generate a numerical function for stress using lambdify
        S1_Cauchy_function = sp.lambdify((mu, lamda), S1_Cauchy, 'numpy')
        S1_Piola_function = sp.lambdify((mu, lamda), S1_Piola, 'numpy')
        S1_S_function = sp.lambdify((mu, lamda), S1_S, 'numpy')

    elif deformation_type == 'simple_shear':             
        S1_Cauchy = Sigma_Cauchy[0,1]
        S1_Piola = Sigma_Piola[0,1]
        S1_S = Sigma_S[0,1]

        # Generate a numerical function for stress using lambdify
        S1_Cauchy_function = sp.lambdify((mu, lamda), S1_Cauchy, 'numpy')
        S1_Piola_function = sp.lambdify((mu, lamda), S1_Piola, 'numpy')
        S1_S_function = sp.lambdify((mu, lamda), S1_S, 'numpy')
    else:
        raise ValueError("Invalid deformation type. Use 'uniaxial', 'biaxial', 'pure_shear', or 'simple_shear'.")


    
    if stress_type == 'Cauchy':
        return S1_Cauchy_function(mu1,lambda1)
    elif stress_type == 'Piola':
        return S1_Piola_function(mu1, lambda1)
    elif stress_type == 'S':
        return S1_S_function(mu1, lambda1)
    else:
        raise ValueError("Invalid stress function type. Use 'Cauchy' or 'Piola'.")


print(stress(1, 2, energy_ = 'neo_hookean', deformation_type='uniaxial', stress_type='Cauchy', strain_type='stretch'))

