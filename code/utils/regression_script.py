import nibabel as nib
import numpy as np
from behavtask_tr import events2neural_extend, merge_cond
from regression_functions import hrf, getRegressor, calcBeta, calcMRSS, deleteOutliers
import os
from scipy.stats import gamma
import math
import numpy.linalg as npl
import json

n_vols=240
TR=2
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)

os.chdir("../../data")

dvars_out = json.load(open("dvarsOutliers.txt"))
fd_out = json.load(open("fdOutliers.txt"))

for i in range(1,17):
    # first three dimension for data shape is 64, 64, 34.
    # create array to store the combined dataset of three runs
    data_full = np.empty([64, 64, 34, 0])
    gain_full = np.empty([0,])
    loss_full = np.empty([0,])
    linear_full = np.empty([0,])
    quad_full = np.empty([0,])
    for j in range(1,4):
        direct='ds005/sub0'+str(i).zfill(2)+'/BOLD/task001_run00'+`j`+'/'
        boldname = direct+'bold.nii.gz'
        img=nib.load(boldname)
        data=img.get_data()
        run = j
        behav_cond = 'ds005/sub0'+str(i).zfill(2)+'/behav/task001_run00'+`j`+'/behavdata.txt'
        task_cond1 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond001.txt'
        task_cond2 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond002.txt'
        task_cond3 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond003.txt'
        task_cond4 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond004.txt'
        parameters = merge_cond(behav_cond, task_cond1, task_cond2, task_cond3, task_cond4)
        neural_prediction = events2neural_extend(parameters,TR, n_vols)
        gain, loss, linear_dr, quad_dr = getRegressor(TR, n_vols, hrf_at_trs, neural_prediction)
        data, gain, loss, linear_dr, quad_dr = deleteOutliers(data, gain, loss, linear_dr, quad_dr, i, run, dvars_out, fd_out)
        data_full = np.concatenate((data_full,data),axis=3)
        gain_full = np.concatenate((gain_full,gain),axis=0)
        loss_full = np.concatenate((loss_full,loss),axis=0)
        linear_full = np.concatenate((linear_full,linear_dr),axis=0)
        quad_full = np.concatenate((quad_full,quad_dr),axis=0)
    mea=calcMRSS(data_full, gain_full, loss_full, linear_full, quad_full)
    X, Y, beta=calcBeta(data_full, gain_full, loss_full, linear_full, quad_full)
    write='ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/sub'+`i`+'_beta.txt'
    np.savetxt(write, beta)

