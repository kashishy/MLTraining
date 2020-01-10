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


def plot_regression_line(x,y,b):
    # Ploting actual points as scatter points
    plt.scatter(x, y, color='m', marker='o', s=30)

    # Predicted response vector
    y_pred = b[0] + b[1]*x;

    # Plotting the regression line
    plt.scatter(x, y_pred, color='g')
    plt.plot(x, y_pred, color='b')

    # Putting labels
    plt.xlabel('---x--->')
    plt.ylabel('---y--->')

    plt.show()


def startAIAlgorithm():
    # observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10,  12])

    print("Hello : ", np.sum(x))

    # estimating coefficient
    m, c = estimate_coef(x, y) # sender values
    print('Estimate Coefficient:\n')
    print('Slope m = ', m)
    print('y-intercept c = ', c)
    print('y = ', m, '* x +', c)

    # plotting regression line
    plot_regression_line(x, y, [c, m])

if __name__=="__main__":
    startAIAlgorithm()