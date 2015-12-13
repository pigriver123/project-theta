from __future__ import division
from statsmodels.regression.mixed_linear_model import MixedLM
from scipy import stats  
import pandas as pd
import numpy as np

def calcBetaLme(data_full, gain_full, loss_full, linear_full, quad_full, run_group, thrshd=None):
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
        if thrshd != None:
            if (np.mean(time_by_vox[:,k]) <= thrshd):
                beta[k, :] = [0, 0, 0, 0, 0]
            else:
                dt = pd.DataFrame({'gain':gain_full,'loss':loss_full,'run_group':run_group,
                              'ldrift':linear_full,'qdrift':quad_full,'bold':time_by_vox[:,k]})
                mod_lme = MixedLM.from_formula(fml, dt, groups=dt["run_group"])
                lme_result = mod_lme.fit()
                beta[k, :] = [lme_result.fe_params["gain"], lme_result.pvalues["gain"], 
                      lme_result.fe_params["loss"], lme_result.pvalues["loss"], lme_result.converged]
        else:
            dt = pd.DataFrame({'gain':gain_full,'loss':loss_full,'run_group':run_group,
                          'ldrift':linear_full,'qdrift':quad_full,'bold':time_by_vox[:,k]})
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


def calcAnov(data_full, run_group, thrshold = None):
    """ 
    function to do ANOVA test between runs
    Input: data from bold file, dummy variable indicating the groups
    Output: F test value and p value of anova test
    """
    T = data_full.shape[-1]
    time_by_vox = np.reshape(data_full, (-1, T)).T
    anov_test = np.empty([time_by_vox.shape[1],2])
    for k in np.arange(0,time_by_vox.shape[1]):
        ## set a threshold to idenfity the voxels inside the brain
        if thrshold != None:
            if (np.mean(time_by_vox[:,k]) <= thrshold):
                anov_test[k, :] = [0, 0]
            else:
                anov_test[k, :]  = stats.f_oneway(time_by_vox[:,k][run_group==1], 
                                                            time_by_vox[:,k][run_group==2],
                                                            time_by_vox[:,k][run_group==3])
        else:
            anov_test[k, :]  = stats.f_oneway(time_by_vox[:,k][run_group==1], 
                                                        time_by_vox[:,k][run_group==2],
                                                        time_by_vox[:,k][run_group==3])
            
    return anov_test


def anovStat(anov_test):
    """ 
    function to do check proportions of p-values not equal to 0 and significant

    Input: Result fo calcAnov: array of size (k,2) where k is number of voxels not equal 0
    Output: Proportions of p-values(voxels) significant (but not 0)
    """    
    mask = anov_test[:, 1] != 0
    nzcount = mask.sum()
    p_value = anov_test[mask, 1]
    prop_sig = np.sum(p_value <= 0.05/nzcount)/nzcount # Bonferroni correction
    return prop_sig
