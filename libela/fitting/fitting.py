import numpy as np
from scipy.optimize import minimize
#from sympy import symbols, lambdify

#from libela.hyperelastic.hyperelastic import hyperelastic

def func1(lamda, a_mu):
    return a_mu * lamda**2 - a_mu / lamda


def func2(lamda, a_c10, b_c01):
    return 2*a_c10*lamda**2 - 2*a_c10/lamda + 2*b_c01*lamda - 2*b_c01/lamda**2


def model(lamda, y, params, function_type):
    if function_type == 'func1':
        a_mu = params[0]
        y_pred = func1(lamda, a_mu)
    elif function_type == 'func2':
        a_c10, b_c01 = params[1]
        y_pred = func2(lamda, a_c10, b_c01)

    return np.sum((y-y_pred)**2)

def fit_model(lamda, y, initial_guess, function_type):
    result = minimize(model, initial_guess, args=(lamda, y, function_type), method = 'Nelder-Mead')
    return result

if __name__ == "__main__":
    lamda = np.array([2, 3, 4, 5])
    #y = np.array([7, 17.33, 31.5, 49.6])
    y = np.array([24.5, 52, 86.625, 128.96])
    initial_guess = [2, 3]
    function_type = 'func2'

    result = fit_model(lamda, y, initial_guess, function_type)

    print("Optimization results:", result)
    print("Optimized parameters:", result.x)


