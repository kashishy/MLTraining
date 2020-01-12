import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    # Number of observations/points
    n = np.size(x)

    # Mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # Calculating cross-deviation and deviation about x
    SS_xy = np.sum(x * y) - n * m_x * m_y
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # Calculation regression coefficients
    m = SS_xy/SS_xx
    c = m_y-m*m_x
    return[m, c]
