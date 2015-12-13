"""
    Function to calculated t statistics from regression data, design, adn beta
results from regression
"""

import numpy.linalg as npl
import numpy as np

def significant(X,Y,beta):
    """
    Calculates t statistic for the first two entries of given beta estimates
    
    Parameters:
    -----------
    X: Design matrix
    Y: Data matrix
    beta: beta estimates from OLS regression, 1-d array of length at least 2
    
    Returns:
    --------
    t-statistics: t1 (for beta1) and t2 (for beta2), each of type double
    """

    y_hat = X.dot(beta)
    residuals = Y - y_hat
    RSS = np.sum(residuals ** 2)
    df = X.shape[0] - npl.matrix_rank(X)
    MRSS = RSS / df
    s2 = MRSS
    v_cov = s2 * npl.inv(X.T.dot(X))
    numerator1 = beta[0]
    denominator1 = np.sqrt(v_cov[0, 0])
    t1= numerator1 / denominator1
    numerator2 = beta[1]
    denominator2 = np.sqrt(v_cov[1, 1])
    t2= numerator2 / denominator2
    return t1,t2
