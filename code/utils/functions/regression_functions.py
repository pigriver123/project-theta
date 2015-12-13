from __future__ import division
import numpy as np
from scipy.stats import gamma
import numpy.linalg as npl


def hrf(times):
    """ 
    Return values for HRF at given times 
    Used to get the convolved parameters
    """
    peak_values=gamma.pdf(times,6)
    undershoot_values=gamma.pdf(times,12)
    values=peak_values-0.35*undershoot_values
    return values/np.max(values)*0.6


def getRegressor(TR, n_vols, hrf_at_trs, neural_prediction, standard = False):
    """ 
    function to get all regressors for model.
    Regressors include  convolved gain and loss, linear and quadratic drift
    Input: number of run, TR, v_vols, hrf_at_trs (created with hrf function)
           neural_prediction is the combined behavior and task condition data
    Output: gain, loss, linear drift quadratic drift
    """
    convolved_gain = np.convolve(neural_prediction[:,1], hrf_at_trs)
    convolved_loss = np.convolve(neural_prediction[:,2], hrf_at_trs)
    n_to_remove = len(hrf_at_trs) - 1
    convolved_gain = convolved_gain[:-n_to_remove]
    convolved_loss = convolved_loss[:-n_to_remove]
    if standard: 
        linear_dr = None
        quadratic_dr = None
    else:
        linear_dr = np.linspace(-1, 1, n_vols)
        quadratic_dr = linear_dr ** 2
        quadratic_dr -= np.mean(quadratic_dr)
    return convolved_gain, convolved_loss, linear_dr, quadratic_dr

def deleteOutliers(data, gain, loss, sub, run, dvars_out, fd_out, linear_dr=None, quad_dr=None):
    """
    function that deleter outliers in each run and merge 3 run into one dataset
    Input: data, gain, loss (got from the getGainLoss function), optional linear
    and quadratic terms,  sub and run number, dictionary of dvars and fd 
    outliers
    output: data from bold, gain, loss variable, optional lin/quad drifts 
            (all without outliers and merged together for each sub)
    """
    dvars_outliers = dvars_out['sub'+ str(sub) +'run'+ str(run)]
    fd_outliers = fd_out['sub'+ str(sub) +'run'+ str(run)]
    outliers = list(set(dvars_outliers+fd_outliers))
    nonoutliers = [out for out in range(data.shape[3]) if out not in outliers]
    data = data[:,:,:, nonoutliers]
    gain = gain[nonoutliers]
    loss = loss[nonoutliers]
    if (linear_dr is not None) & (quad_dr is not None):
        linear_dr = linear_dr[nonoutliers]
        quad_dr = quad_dr[nonoutliers]
    return data, gain, loss, linear_dr, quad_dr

def calcBeta(data, gain, loss, linear_dr=None, quad_dr=None, threshold=None):
    """ 
    function to calculate beta parameters.
    Input: data from bold file, two list of gain, loss regressor values
    Output: X, Y, coefficient
    """

    if (linear_dr is not None) & (quad_dr is not None):
        design = np.ones((len(gain), 5))
        design[:, 2] = linear_dr
        design[:, 3] = quad_dr
    else:
        design = np.ones((len(gain), 3))
    design[:, 0] = gain
    design[:, 1] = loss
    designp = npl.pinv(design)
    if threshold!=None:
        mask = np.mean(data, axis=-1) > threshold
        data[~mask]=0
    T = data.shape[-1]
    time_by_vox = np.reshape(data, (-1, T)).T
    beta_hats = designp.dot(time_by_vox)
    return design, time_by_vox, beta_hats

def calcMRSS(data, gain, loss, linear_dr=None, quad_dr=None, threshold=None):
    """ 
    function to calculate MRSS.
    Input: data from bold file, two list of gain, loss regressor values
        Optional lin and quad drift terms, and threshold masking
    Output: X, Y, coefficient
    """
    design, time_by_vox, beta_hats = calcBeta(data, gain, loss, linear_dr, quad_dr, threshold)
    T = data.shape[-1]
    residuals = time_by_vox - design.dot(beta_hats)
    df = T - npl.matrix_rank(design)
    mrss = np.sum(residuals ** 2, axis=0) / df
    return np.mean(mrss)


