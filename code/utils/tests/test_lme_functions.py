"""
Test lme_function module the following functions:
    calcAnov
    calcBetaLme
    calcSigProp
    anovStat

Run with::
    **Run from project-theta directory or code directory  with 'make test'

"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import sys, os
from scipy import stats
from sklearn import linear_model
from numpy.testing import assert_almost_equal, assert_allclose


# Append function path
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))

# Path to the first subject, first run, this is used as the test data for 
# getGainLoss:
pathtotest = 'code/utils/tests/' 

# Load graph_functions:
from lme_functions import calcBetaLme, calcSigProp, calcAnov, anovStat

def test_calcBetaLme():
    # Test data with large n = 1500
    X = np.ones((2000, 4))
    X[:, 0] = np.random.normal(0, 1, 2000)
    X[:, 1] = np.random.normal(2, 2, 2000)
    X[:, 2] = np.linspace(-1,1,2000)
    X[:, 3] = X[:,2]**2
    Y = np.random.normal(3,1,2000)
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    test_betas = regr.coef_
    # My function, should produce same results if groups are all the same:
    lme = calcBetaLme(Y, X[:,0], X[:,1], X[:,2], X[:,3], np.repeat(1,2000))
    lme_thrs = calcBetaLme(Y, X[:,0], X[:,1], X[:,2], X[:,3], np.repeat(1,2000), -40000)
    lme_thrs1 = calcBetaLme(Y, X[:,0], X[:,1], X[:,2], X[:,3], np.repeat(1,2000), 0)
    # Compare betas
    my_betas = lme.ravel()[[0,2]]
    my_betas_thrs = lme_thrs.ravel()[[0,2]]
    my_betas_thrs1 = lme_thrs1.ravel()[[0,2]]
    assert max(abs(my_betas - test_betas[:2])) < 0.005
    assert max(abs(my_betas_thrs - test_betas[:2])) < 0.005
    assert (test_betas != my_betas_thrs1)

    
def test_calcSigProp():
    # Set up test betas
    t_beta = np.array([[0, 0, 0, 0, 0], [0.4, 0.03, 0.1, 1, 0.17], [2, 0.1, 0.09, 0.2, 0.88], [1, 1.2, 0.9, 0.4, 0.51], [0.31, 0.22, 0.16, 0.05, 0.02]])
    sig_level = 0.1
    # Get significant level of 2nd column after reshaping to (5,5)
    # 0, 0.03, 0.1, 1.2, 0.22
    notzero_beta = t_beta[t_beta !=0].reshape(-1,5)
    t_psig_gain = sum(notzero_beta[:,1]<=sig_level)/len(notzero_beta[:,1])
    # Get significant level of 4th column 
    # 0, 1, 0.2, 0.4, 0.05
    t_psig_loss = sum(notzero_beta[:,3]<=sig_level)/len(notzero_beta[:,3]) 
 
   # My function
    my_psig_gain, my_psig_loss = calcSigProp(t_beta, sig_level)
    
    # Assert
    assert_almost_equal(my_psig_gain, t_psig_gain)
    assert_almost_equal(my_psig_loss, t_psig_loss)

def test_calcAnova():
    # Test dataset
    t_data = np.reshape(np.random.normal(0,1,8), (1,1,1,8))
    run_group = np.array([1, 2, 1, 3, 3, 2, 2, 1])
    # split into runs
    d1 = np.reshape(t_data, (-1, 8)).T[:,0][run_group == 1]
    d2 = np.reshape(t_data, (-1, 8)).T[:,0][run_group == 2]
    d3 = np.reshape(t_data, (-1, 8)).T[:,0][run_group == 3]
    groups = np.array([d1,d2,d3])
    def ANOVA(G):
        # variation within groups
        SSD_W = 0
        for g in G:
            SSD_W += np.sum([(i-np.mean(g))**2 for i in g])
        # a bit awkward, just flattening the list of lists
        # to get the mean and N
        T = list()
        for g in G:
            T.extend(g)
        m = np.mean(T)
    
        # variation between groups (X for 'cross')
        SSD_X = 0
        for g in G:
            SSD_X += len(g)*(np.mean(g)-m)**2
        N = len(T)  
        k = len(G)  
        MS_W = SSD_W*1.0/(N-k)
        MS_X = SSD_X*1.0/(k-1)
        F_stat = MS_X/MS_W
        pval = 1-stats.f.cdf(F_stat, k-1, N-k)
        return np.array([F_stat, pval])
    
    test_anova = ANOVA(groups)
    # My function
    my_anova = calcAnov(t_data, run_group).ravel()
    my_anova_thrs = calcAnov(t_data, run_group, -40000).ravel()
    my_anova_thrs1 = calcAnov(t_data, run_group, 0).ravel()
    # Assert
    assert_allclose(test_anova, my_anova)
    assert_allclose(test_anova, my_anova_thrs)
    assert (test_anova != my_anova_thrs1).any()


def test_anovStat():
    # create a test dataset
    t_data = np.reshape(np.array([2, 0.1, 3, 0.04, 2.1, 0.01, 0, 0, 1.2, 0.05, 2.2, 2]), (-1, 2))
    # Significance level chosen to be 0.05, 0.05/5 = 0.01 after bonferroni correction
    # Should give: 0.01 significant out of 0.1, 0.04, 0.01, 0.05, 2
    test_prop = 1/5
    # my function
    my_prop = anovStat(t_data)
    # Assert
    assert_allclose(test_prop, my_prop)
