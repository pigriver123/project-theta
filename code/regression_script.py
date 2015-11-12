import nibabel as nib
import numpy as np
from behavtask_tr.py import events2neural_extend, merge_cond
from regression_functions import hrf, getGainLoss, calcBeta, calcMRSS
import os
from scipy.stats import gamma
import math
import numpy.linalg as npl

n_vols=240
TR=2
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)


for i in range(1,10):
    for j in range(1,4):
        direct='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/'
        boldname = direct+'bold.nii'
        img=nib.load(boldname)
        data=img.get_data()
        gain, loss = getGainLoss(run, TR, n_vols)
        mea=calcMRSS(gain, loss)
        X, Y, beta=calcBeta(gain, loss)
        write='ds005/sub00'+`i`+'/model/model001/onsets/task001_run00'+`j`+'.txt'
        np.savetxt(write, beta)

for i in range(10,17):
    for j in range(1,4):
        direct='ds0051/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/'
        boldname = direct+'bold.nii'
        img=nib.load(boldname)
        data=img.get_data()
        gain, loss = getGainLoss(run, TR, n_vols)
        mea=calcMRSS(gain, loss)
        X, Y, beta=calcBeta(gain, loss)
        write='ds005/sub0'+`i`+'/model/model001/onsets/task001_run00'+`j`+'.txt'
        np.savetxt(write, beta)

