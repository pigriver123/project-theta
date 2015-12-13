"""
Test calc_t module the following functions:
    significant

Run with::
    **Run from project-theta or code directory with 'make test'

"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import os
import sys
from scipy.stats import t as t_dist
import numpy.linalg as npl
from numpy.testing import assert_almost_equal


# Set path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Load graph_functions:
from calc_t import significant

def test_significant():
    # Some test data and test code taken from example at:
    # http://www.jarrodmillman.com/rcsds/lectures/glm_intro.html
    psychopathy = [11.416,   4.514,  12.204,  14.835,
                   8.416,   6.563,  17.343, 13.02,
                   15.19 ,  11.902,  22.721,  22.324]
    clammy = [0.389,  0.2  ,  0.241,  0.463,
              4.585,  1.097,  1.642,  4.972,
              7.957,  5.585,  5.527,  6.964]
    def t_stat(y, X, c):
        """ betas, t statistic and significance test given data, design matrix, contrast

        This is OLS estimation; we assume the errors to have independent
        and identical normal distributions around zero for each $i$ in
        $\e_i$ (i.i.d).
        """
        # Make sure y, X, c are all arrays
        y = np.asarray(y)
        X = np.asarray(X)
        c = np.atleast_2d(c).T  # As column vector
        # Calculate the parameters - b hat
        beta = npl.pinv(X).dot(y)
        # The fitted values - y hat
        fitted = X.dot(beta)
        # Residual error
        errors = y - fitted
        # Residual sum of squares
        RSS = (errors**2).sum(axis=0)
        # Degrees of freedom is the number of observations n minus the number
        # of independent regressors we have used.  If all the regressor
        # columns in X are independent then the (matrix rank of X) == p
        # (where p the number of columns in X). If there is one column that
        # can be expressed as a linear sum of the other columns then
        # (matrix rank of X) will be p - 1 - and so on.
        df = X.shape[0] - npl.matrix_rank(X)
        # Mean residual sum of squares
        MRSS = RSS / df
        # calculate bottom half of t statistic
        SE = np.sqrt(MRSS * c.T.dot(npl.pinv(X.T.dot(X)).dot(c)))
        t = c.T.dot(beta) / SE
        # Get p value for t value using cumulative density dunction
        # (CDF) of t distribution
        ltp = t_dist.cdf(t, df) # lower tail p
        p = 1 - ltp # upper tail p
        return beta, t, df, p
    X = np.column_stack((np.ones(12), clammy))    
    Y = np.asarray(psychopathy)
    B1, t1, df1, p1 = t_stat(Y, X, [1, 0])
    B2, t2, df2, p2 = t_stat(Y, X, [0, 1])
    #---------------------------------------------------------#

    # my function

    myt1, myt2 = significant(X, Y, B1) 
    # assert
    assert_almost_equal(t1.ravel(), myt1)
    assert_almost_equal(t2.ravel(), myt2)
