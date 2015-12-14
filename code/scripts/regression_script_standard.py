import nibabel as nib
import numpy as np
import os
import json
import sys

# Path to function
pathtofunction = '../utils/functions'
# Append path to sys
sys.path.append(pathtofunction)

from behavtask_tr import events2neural_extend, merge_cond
from regression_functions import hrf, getRegressor, calcBeta, calcMRSS, deleteOutliers
from smooth_gaussian import fwhm2sigma, smooth_spatial
from calc_t import significant

n_vols=240
TR=2
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)

os.chdir("../../data")

dvars_out = json.load(open("../results/dvarsOutliers.txt"))
fd_out = json.load(open("../results/fdOutliers.txt"))

# Threshold cutoff from histogram observation
threshold = 7500

for i in range(1,17):
    # first three dimension for data shape is 91, 109, 91.
    # create array to store the combined dataset of three runs
    data_full = np.empty([91, 109, 91, 0])
    gain_full = np.empty([0,])
    loss_full = np.empty([0,])
    for j in range(1,4):
        boldname='ds005_mnifunc/sub0'+str(i).zfill(2)+'/model/model001/task001_run00'+`j`+'.feat/filtered_func_data_mni.nii.gz'
        img=nib.load(boldname)
        data=img.get_data()
        data=smooth_spatial(data)
        run = j
        behav_cond = 'ds005/sub0'+str(i).zfill(2)+'/behav/task001_run00'+`j`+'/behavdata.txt'
        task_cond1 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond001.txt'
        task_cond2 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond002.txt'
        task_cond3 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond003.txt'
        task_cond4 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond004.txt'
        parameters = merge_cond(behav_cond, task_cond1, task_cond2, task_cond3, task_cond4)
        neural_prediction = events2neural_extend(parameters,TR, n_vols)
        gain, loss, linear_dr, quad_dr = getRegressor(TR, n_vols, hrf_at_trs, neural_prediction, standard = True)
        data, gain, loss, linear_dr, quad_dr = deleteOutliers(data, gain, loss, i, run, dvars_out, fd_out)
        data_full = np.concatenate((data_full,data),axis=3)
        gain_full = np.concatenate((gain_full,gain),axis=0)
        loss_full = np.concatenate((loss_full,loss),axis=0)
    # mea=calcMRSS(data_full, gain_full, loss_full, None, None, threshold)
    X, Y, beta=calcBeta(data_full, gain_full, loss_full, None, None, threshold)
    # calculate t values
    t_val=np.zeros((2,139264))
    for k in range(Y.shape[1]):
        t_val[:,k] = significant(X,Y[:,k], beta[:,k])
    # file names for beta and t
    beta_file='../results/sub0'+str(i).zfill(2)+'_standard_beta.txt'
    t_file='../results/sub0'+str(i).zfill(2)+'_standard_tvals.txt'
    # save beta and t values to file
    np.savetxt(beta_file, beta)
    np.savetxt(t_file, t_val)

