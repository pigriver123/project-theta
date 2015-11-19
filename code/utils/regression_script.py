import nibabel as nib
import numpy as np
from behavtask_tr import events2neural_extend, merge_cond
from regression_functions import hrf, getGainLoss, calcBeta, calcMRSS
import os
from scipy.stats import gamma
import math
import numpy.linalg as npl

n_vols=240
TR=2
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)

os.chdir("../../data")

for i in range(1,10):
    for j in range(1,4):
        direct='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/'
        boldname = direct+'bold.nii.gz'
        img=nib.load(boldname)
        data=img.get_data()
        run = j
        gain, loss = getGainLoss(run, TR, n_vols, hrf_at_trs)
        mea=calcMRSS(data, gain, loss)
        X, Y, beta=calcBeta(data, gain, loss)
        write='ds005/sub00'+`i`+'/model/model001/onsets/task001_run00'+`j`+'.txt'
        np.savetxt(write, beta)

for i in range(10,17):
    for j in range(1,4):
        direct='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/'
        boldname = direct+'bold.nii.gz'
        img=nib.load(boldname)
        data=img.get_data()
        run = j
        gain, loss = getGainLoss(run, TR, n_vols, hrt_at_trs)
        mea=calcMRSS(data, gain, loss)
        X, Y, beta=calcBeta(data, gain, loss)
        write='ds005/sub0'+`i`+'/model/model001/onsets/task001_run00'+`j`+'.txt'
        np.savetxt(write, beta)

