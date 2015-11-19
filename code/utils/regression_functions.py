import matplotlib.pyplot as plt 
import nibabel as nib
import numpy as np
import os
from scipy.stats import gamma
import math
import numpy.linalg as npl
from behavtask_tr import events2neural_extend, merge_cond

def hrf(times):
    """ 
    Return values for HRF at given times 
    Used to get the convolved parameters
    """
    peak_values=gamma.pdf(times,6)
    undershoot_values=gamma.pdf(times,12)
    values=peak_values-0.35*undershoot_values
    return values/np.max(values)*0.6


def getGainLoss(run, TR, n_vols, hrf_at_trs):
    """ 
    function to get the convolved gain and loss values.
    the gain and loss values for every subject is the same for the same run.
    Input: number of run, TR, v_vols, hrf_at_trs (created with hrf function)
    Output: gain, loss values
    """
    behav_cond = 'ds005/sub001/behav/task001_run00'+`run`+'/behavdata.txt'
    task_cond = 'ds005/sub001/model/model001/onsets/task001_run00'+`run`+'/cond001.txt'
    parameters = merge_cond(behav_cond, task_cond)
    neural_prediction = events2neural_extend(parameters,TR, n_vols)
    convolved_gain = np.convolve(neural_prediction[:,1], hrf_at_trs)
    convolved_loss = np.convolve(neural_prediction[:,2], hrf_at_trs)
    n_to_remove = len(hrf_at_trs) - 1
    convolved_gain = convolved_gain[:-n_to_remove]
    convolved_loss = convolved_loss[:-n_to_remove]
    return convolved_gain, convolved_loss

def calcBeta(data, gain, loss):
    """ 
    function to calculate beta parameters.
    Input: data from bold file, two list of gain, loss regressor values
    Output: X, Y, coefficient
    """
    design = np.ones((len(gain), 3))
    design[:, 0] = gain
    design[:, 1] = loss
    designp = npl.pinv(design)
    T = data.shape[-1]
    time_by_vox = np.reshape(data, (-1, T)).T
    beta_hats = designp.dot(time_by_vox)
    return design, time_by_vox, beta_hats

def calcMRSS(data, gain, loss):
    """ 
    function to calculate MRSS.
    Input: data from bold file, two list of gain, loss regressor values
    Output: X, Y, coefficient
    """
    design = np.ones((len(gain), 3))
    design[:, 0] = gain
    design[:, 1] = loss
    designp = npl.pinv(design)
    T = data.shape[-1]
    time_by_vox = np.reshape(data, (-1, T)).T
    beta_hats = designp.dot(time_by_vox)
    residuals = time_by_vox - design.dot(beta_hats)
    df = T - npl.matrix_rank(design)
    mrss = np.sum(residuals ** 2, axis=0) / df
    return np.mean(mrss)


