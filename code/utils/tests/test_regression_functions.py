"""
Test regression_function module the following functions:
    hrf
    getRegressor
    deleteOutliers
    calcBeta
    calcMRSS

Run with::
    **Run from project-theta directory with 'make test'

"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import os
import sys
from sklearn import linear_model
from scipy.stats import gamma
from numpy.testing import assert_almost_equal, assert_allclose


# Set path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Path to the first subject, first run, this is used as the test data for 
# getGainLoss:
pathtotest = 'code/utils/tests/' 

# Load graph_functions:
from regression_functions import hrf, getRegressor, calcBeta, calcMRSS, deleteOutliers
from behavtask_tr import merge_cond, events2neural_extend

def test_hrf():
    # create test array of times
    hrf_times = np.arange(0,20,0.2)
    # Gamma pdf for the peak
    peak_values = gamma.pdf(hrf_times, 6)
    # Gamma pdf for the undershoot
    undershoot_values = gamma.pdf(hrf_times, 12)
    # Combine them
    test_values = peak_values - 0.35 * undershoot_values
    # Scale max to 0.6
    test_values = test_values/np.max(test_values)*0.6
    # my values from function
    my_values = hrf(hrf_times)
    # assert
    assert_almost_equal(test_values, my_values)

def test_getRegressor():
    # Set up and load in subject 1 run 1
    # This is the convolution method described, in detail on:
    # http://practical-neuroimaging.github.io/on_convolution.html
    TR = 2
    n_vols = 240
    tr_times = np.arange(0, 30, TR)
    hrf_signal = hrf(tr_times)
    behav_cond = pathtotest + 'test_behavdata.txt'
    task_cond1 = pathtotest + 'test_cond001.txt'
    task_cond2 = pathtotest + 'test_cond002.txt'
    task_cond3 = pathtotest + 'test_cond003.txt'
    task_cond4 = pathtotest + 'test_cond004.txt'
    parameters = merge_cond(behav_cond, task_cond1, task_cond2, task_cond3, task_cond4)
    # get neural_signal
    neural_signal = events2neural_extend(parameters,TR, n_vols)
    # get gain signal
    gain_signal = neural_signal[:,1]
    # get loss signal 
    loss_signal = neural_signal[:,2]
    # Len of neural signal 
    N = neural_signal.shape[0]
    # Length of hrf_signal
    M = len(hrf_signal)
    # create the convolved bold signal gain/loss 
    convolved_gain = np.zeros(N + M - 1)  # adding the tail
    convolved_loss = np.zeros(N + M - 1)  # adding the tail
    for i in range(N):
        input_value_g = gain_signal[i]
        input_value_l = loss_signal[i]
        # Adding the shifted, scaled HRF
        convolved_gain[i : i + M] += hrf_signal * input_value_g
        convolved_loss[i : i + M] += hrf_signal * input_value_l
    # Remove the extra_times
    n_to_remove = M-1
    convolved_gain = convolved_gain[:-n_to_remove]
    convolved_loss = convolved_loss[:-n_to_remove]
    lin_dr = np.linspace(-1, 1, n_vols)
    quad_dr = lin_dr ** 2
    quad_dr -= np.mean(quad_dr)
     
    #--------------------------------------------------------------------------#
    # my function 
    myconv_gain, myconv_loss, my_lin, my_quad = getRegressor(TR, n_vols, hrf_signal, neural_signal)
    myconv_gain1, myconv_loss1, my_lin1, my_quad1 = getRegressor(TR, n_vols, hrf_signal, neural_signal, standard = True)

    #--------------------------------------------------------------------------#
    # assert checks
    assert (max(abs(convolved_gain-myconv_gain) < .0001))
    assert (max(abs(convolved_loss-myconv_loss) < .0001))
    assert (max(abs(quad_dr-my_quad) < .0001))
    assert (max(abs(lin_dr-my_lin) < .0001))
    # Check standard template
    assert_allclose(myconv_gain, myconv_gain1)
    assert_allclose(myconv_loss, myconv_loss1)
    assert (my_lin1 is None)
    assert (my_quad1 is None)

def test_deleteOutliers():
    # Create some test arrays/dictionaries
    t_data = np.arange(8).reshape((1,1,1,8))
    t_gain = np.arange(8)+2
    t_loss = np.arange(8)+4
    t_lin = np.linspace(-1,1, 8)
    t_quad = t_lin ** 2
    t_quad -= np.mean(t_quad)
    dvars_out= {'sub1run1': [2,3],'sub2run2':[1,2]}
    fd_out= {'sub1run1': [1,2,3], 'sub2run2':[4,5,6]}
    # sub 1 run 1
    sub1 = 1
    run1 = 1
    # t_outliers = [2,3]
    t_nonoutliers1 = [0,4,5,6,7]
    t_data1= t_data[:,:,:,t_nonoutliers1]
    t_gain1 = t_gain[t_nonoutliers1]
    t_loss1 = t_loss[t_nonoutliers1]
    t_lin1 = t_lin[t_nonoutliers1]
    t_quad1 = t_quad[t_nonoutliers1]
    #--------------------------------------------------------------------------#
    # my function
    # Raw
    my_data1, my_gain1, my_loss1, my_lin1, my_quad1 = deleteOutliers(t_data, t_gain, t_loss, sub1, run1, dvars_out, fd_out, t_lin, t_quad)
    # Standard
    my_data1s, my_gain1s, my_loss1s, my_lin1s, my_quad1s = deleteOutliers(t_data, t_gain, t_loss, sub1, run1, dvars_out, fd_out)

    #--------------------------------------------------------------------------#
    # assert 1
    assert_allclose(my_data1, t_data1)
    assert_allclose(my_gain1, t_gain1)
    assert_allclose(my_loss1, t_loss1)
    assert_allclose(my_lin1, t_lin1)
    assert_allclose(my_quad1, t_quad1)
    # standard
    assert (my_lin1s is None)
    assert (my_quad1s is None)
    assert_allclose(my_data1, my_data1s)
    assert_allclose(my_gain1, my_gain1s)
    assert_allclose(my_loss1, my_loss1s)


    #--------------------------------------------------------------------------#
    # sub 2 run 2
    sub2 = 2
    run2 = 2
    # t_outliers = [1,2,4,5,6]
    t_nonoutliers2 = [0,3,7]
    t_data2= t_data[:,:,:,t_nonoutliers2]
    t_gain2 = t_gain[t_nonoutliers2]
    t_loss2 = t_loss[t_nonoutliers2]
    t_lin2 = t_lin[t_nonoutliers2] 
    t_quad2 = t_quad[t_nonoutliers2]
    #--------------------------------------------------------------------------#
    # my function
    my_data2, my_gain2, my_loss2 , my_lin2, my_quad2 = deleteOutliers(t_data, t_gain, t_loss, sub2, run2, dvars_out, fd_out, t_lin, t_quad)
    my_data2s, my_gain2s, my_loss2s , my_lin2s, my_quad2s = deleteOutliers(t_data, t_gain, t_loss, sub2, run2, dvars_out, fd_out)

    
    #--------------------------------------------------------------------------#
    # assert 2
    assert_allclose(my_data2, t_data2)
    assert_allclose(my_gain2, t_gain2)
    assert_allclose(my_loss2, t_loss2)
    assert_allclose(my_lin2, t_lin2)
    assert_allclose(my_quad2, t_quad2)
    # standard
    assert (my_lin2s is None)
    assert (my_quad2s is None)
    assert_allclose(my_data2, my_data2s)
    assert_allclose(my_gain2, my_gain2s)
    assert_allclose(my_loss2, my_loss2s)



def test_calcBeta():
    # X, Y are constructed like the way in calcBeta(data, gain, loss).
    # Create a simple linear model based on Y = 2X1 + 5X2 + e
    X = np.ones((6, 4))
    X[:, 0] = np.array([1,2,3,4,5,6])
    X[:, 1] = np.array([2,4,6,8,10,12])
    X[:, 2] = np.linspace(-1,1,6)
    t_quad = X[:,2] ** 2
    t_quad -= np.mean(t_quad)
    X[:, 3] = t_quad
    Y = X[:,0] + X[:,1]*2 + X[:,2] + X[:,3] + 1
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    test_beta = np.append(regr.coef_ , regr.intercept_)
    #--------------------------------------------------------------------------#
    # my function
    design, t_by_v, my_beta = calcBeta(Y, X[:,0], X[:,1], X[:,2], X[:,3])
    #--------------------------------------------------------------------------#
    # assert betas: the threshold here is a bit high since 2 methods of 
    # implementation for a small sample size gives some variation in betas
    assert all(my_beta.ravel()-test_beta < 0.1)
    # assert time_by_voxel (predictions)
    assert_allclose(t_by_v.ravel(), regr.predict(X))
    # assert design
    assert_allclose(X, design[:,:4])
    
    #--------------------------------------------------------------------------#
    Y = X[:,0] + X[:,1]*2 + X[:,2] + X[:,3] + 1
    # myfunction when thrs != None
    design1, t_by_v1, my_beta1 = calcBeta(Y, X[:,0], X[:,1], X[:,2], X[:,3], 1)

    # assert the threshold values are produce different betas and tbyv
    assert (t_by_v.ravel() != t_by_v1.ravel()).any()
    assert (my_beta.ravel() != my_beta1.ravel()).all()
    # assert design still the same
    assert_allclose(X, design1[:,:4])

    #--------------------------------------------------------------------------#
    # Standard Template test
    X_s = np.ones((6, 2))
    X_s[:, 0] = np.array([1,2,3,4,5,6])
    X_s[:, 1] = np.array([2,4,6,8,10,12])
    Y_s = X_s[:,0] + X_s[:,1]*2  + 1
    # Create linear regression object
    regr_s = linear_model.LinearRegression()
    # Train the model using the training sets
    regr_s.fit(X_s, Y_s)

    # my function standard 
    design_s, t_by_v_s, my_beta_s = calcBeta(Y_s, X_s[:,0], X_s[:,1])

    # assert the threshold values are produce different betas and tbyv
    assert_allclose(t_by_v_s.ravel(), regr_s.predict(X_s))
    # assert design
    assert_allclose(X_s, design_s[:,:2])


def test_calcMRSS():
    # Like above, create a test matrix of regressors
    X = np.ones((6, 4))
    X[:, 0] = np.array([1,2,3,4,5,6])
    X[:, 1] = np.array([2,4,6,9,10,12])
    X[:, 2] = np.linspace(-1,1,6)
    X[:, 3] = X[:,2]**2
    Y = np.array([10,12,14,15,17,20])
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    pred = regr.predict(X)
    test_MRSS = np.mean(np.sum((pred - Y)**2/(Y.shape[-1]-4)))
    #--------------------------------------------------------------------------#
    # my function
    my_MRSS = calcMRSS(Y, X[:,0], X[:,1], X[:,2], X[:,3])
    #--------------------------------------------------------------------------#
    # assert
    assert (abs(test_MRSS-my_MRSS) < .0001) 
    #--------------------------------------------------------------------------#
    # standard
    X_s = np.ones((6, 2))
    X_s[:, 0] = np.array([1,2,3,4,5,6])
    X_s[:, 1] = np.array([2.5,4.1,6.3,9.7,10.1,12.3])
    Y_s = np.array([10,12,14,15,17,20])
    # Create linear regression object
    regr_s = linear_model.LinearRegression()
    # Train the model using the training sets
    regr_s.fit(X_s, Y_s)
    pred_s = regr_s.predict(X_s)
    test_MRSS_s = np.mean(np.sum((pred_s - Y_s)**2/(Y_s.shape[-1]-3)))

    # my function
    my_MRSS_s = calcMRSS(Y_s, X_s[:,0], X_s[:,1])
    #--------------------------------------------------------------------------#
    # assert
    assert (abs(test_MRSS_s-my_MRSS_s) < .0001) 


