from __future__ import division
from statsmodels.regression.mixed_linear_model import MixedLM
import pandas as pd
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from behavtask_tr import events2neural_extend, merge_cond
from regression_functions import hrf, getRegressor, calcBeta, calcMRSS, deleteOutliers
import os
from scipy.stats import gamma
import math
import numpy.linalg as npl
import json

def calcBetaLme(data_full, gain_full, loss_full, run_group, thrshd):
    """ 
    function to calculate beta parameters.
    Input: data from bold file, two list of gain, loss regressor values
        dummy variable indicating the groups,
        a threshold to idenfity the voxels inside the brain
    Output: beta coefficient, the corresponding p-values, the convergence information
    """
    T = data_full.shape[-1]
    time_by_vox = np.reshape(data_full, (-1, T)).T
    beta = np.empty([time_by_vox.shape[1],5])
    fml = "bold ~ gain + loss"
    for k in np.arange(0,time_by_vox.shape[1]):
        ## set a threshold to idenfity the voxels inside the brain
        if (np.mean(time_by_vox[:,k]) <= 400):
            beta[k, :] = [0, 0, 0, 0, 0]
        else:
            dt = pd.DataFrame({'gain':gain_full,'loss':loss_full,'run_group':run_group, 'bold':time_by_vox[:,k]})
            mod_lme = MixedLM.from_formula(fml, dt, groups=dt["run_group"])
            lme_result = mod_lme.fit()
            beta[k, :] = [lme_result.fe_params["gain"], lme_result.pvalues["gain"], 
                      lme_result.fe_params["loss"], lme_result.pvalues["loss"], lme_result.converged]
    return beta


def calcSigProp(beta, sig_level):
    """ 
    function to calculate the proportion of significant beta for each subject.
    Input: the betas and its corresponding p-values for loss and gain seperately
           the significance level
    Output: the proportion of significant beta loss and beta gain 
    """
    nzbeta = np.reshape(beta[beta != 0], (-1,5))
    count_nzbeta = nzbeta.shape[0]
    sig_gain = np.sum(nzbeta[:,1] <= sig_level)
    sig_loss = np.sum(nzbeta[:,3] <= sig_level)
    sig_gain_prop = sig_gain / count_nzbeta
    sig_loss_prop = sig_loss / count_nzbeta
    return sig_gain_prop, sig_loss_prop
