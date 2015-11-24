"""
Test regression_function module the following functions:
    hrf
    getGainLoss
    deleteOutliers
    calcBeta
    calcMRSS

Run with::
    nosetests test_regression_functions.py
    Note: Run from project-theta directory with 'make test'

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
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Path to the first subject, first run, this is used as the test data for some 
# functions below
pathtofirst = 'data/ds005/'

# Load graph_functions:
from regression_functions import hrf, getGainLoss, calcBeta, calcMRSS, deleteOutliers
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

def test_getGainLoss():
    # Set up and load in subject 1 run 1
    # This is the convolution method described, in detail on:
    # http://practical-neuroimaging.github.io/on_convolution.html
    TR = 2
    n_vols = 240
    tr_times = np.arange(0, 30, TR)
    hrf_signal = hrf(tr_times)
    behav_cond = pathtofirst + 'sub001/behav/task001_run001/behavdata.txt'
    task_cond1 = pathtofirst+ 'sub001/model/model001/onsets/task001_run001/cond001.txt'
    task_cond2 = pathtofirst+ 'sub001/model/model001/onsets/task001_run001/cond002.txt'
    task_cond3 = pathtofirst+ 'sub001/model/model001/onsets/task001_run001/cond003.txt'
    task_cond4 = pathtofirst+ 'sub001/model/model001/onsets/task001_run001/cond004.txt'
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
    
    #--------------------------------------------------------------------------#
    # my function 
    myconv_gain, myconv_loss = getGainLoss(TR, n_vols, hrf_signal, neural_signal)
    #--------------------------------------------------------------------------#
    # assert checks
    assert (max(abs(convolved_gain-myconv_gain) < .0001))
    assert (max(abs(convolved_loss-myconv_loss) < .0001))

def test_deleteOutliers():
    # Create some test arrays/dictionaries
    t_data = np.arange(8).reshape((1,1,1,8))
    t_gain = np.arange(8)+2
    t_loss = np.arange(8)+4
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
    #--------------------------------------------------------------------------#
    # my function
    my_data1, my_gain1, my_loss1 = deleteOutliers(t_data, t_gain, t_loss, sub1, run1, dvars_out, fd_out)
    #--------------------------------------------------------------------------#
    # asssert 1
    assert_allclose(my_data1, t_data1)
    assert_allclose(my_gain1, t_gain1)
    assert_allclose(my_loss1, t_loss1)
    
    #--------------------------------------------------------------------------#
    # sub 2 run 2
    sub2 = 2
    run2 = 2
    # t_outliers = [1,2,4,5,6]
    t_nonoutliers2 = [0,3,7]
    t_data2= t_data[:,:,:,t_nonoutliers2]
    t_gain2 = t_gain[t_nonoutliers2]
    t_loss2 = t_loss[t_nonoutliers2]
    #--------------------------------------------------------------------------#
    # my function
    my_data2, my_gain2, my_loss2 = deleteOutliers(t_data, t_gain, t_loss, sub2, run2, dvars_out, fd_out)
    #--------------------------------------------------------------------------#
    # assert 2
    assert_allclose(my_data2, t_data2)
    assert_allclose(my_gain2, t_gain2)
    assert_allclose(my_loss2, t_loss2)

def test_calcBeta():
    # X, Y are constructed like the way in calcBeta(data, gain, loss).
    # Create a simple linear model based on Y = 2X1 + 5X2 + e
    X = np.ones((5, 2))
    X[:, 0] = np.array([1,2,3,4,5])
    X[:, 1] = np.array([2,4,6,8,10])
    Y = X[:,0]*2 + X[:,1]*5 + 1
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    test_beta = np.append(regr.coef_ , regr.intercept_)
    #--------------------------------------------------------------------------#
    # my function
    design, t_by_v, my_beta = calcBeta(Y, X[:,0], X[:,1])
    #--------------------------------------------------------------------------#
    # assert betas
    assert_allclose(my_beta.ravel(), test_beta)
    # assert time_by_voxel (predictions)
    assert_allclose(t_by_v.ravel(), regr.predict(X))
    # assert design
    assert_allclose(X, design[:,:2])

def test_calcMRSS():
    # Like above, create a test matrix of regressors
    X = np.ones((5, 2))
    X[:, 0] = np.array([1,2,3,4,5])
    X[:, 1] = np.array([2,4,6,8,10])
    Y = np.array([10,12,14,15,17])
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    pred = regr.predict(X)
    test_MRSS = np.mean(np.sum((pred - Y)**2/(Y.shape[-1]-2)))
    #--------------------------------------------------------------------------#
    # my function
    my_MRSS = calcMRSS(Y, X[:,0], X[:,1])
    #--------------------------------------------------------------------------#
    # assert
    assert (abs(test_MRSS-my_MRSS) < .0001 )

    
   
