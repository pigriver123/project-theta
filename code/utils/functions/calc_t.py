"""
    Function to calculated t statistics of a single voxel from regression data, design, and beta gain/loss
"""

import numpy.linalg as npl
import numpy as np

def significant(X,Y,beta):
    """
    Calculates t statistic for the first two entries of given beta estimates. 
    Particularly, this is a function to calculate t values for beta gain and 
    beta loss for a single voxel.

    Parameters:
    -----------
    X: Design matrix
    Y: Data matrix for a single voxel
    beta: beta gain/loss estimates from OLS regression of a single voxel, 
    1-d array of length = 2 
    
    Returns:
    --------
    t1, t2: t value for beta gain, t value for beta loss, type: double

    Example use for ith voxel: significant(X, Y[:,i], beta[:,i]) 
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
