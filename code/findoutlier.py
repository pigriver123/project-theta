import numpy as np
from outlierfunction import outlier

for i in range(1,10):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        dvarssave=txtpath+'dvars_outlier_sub'+`i`+'run'+`j`+'.txt'
        # common boundary for dvars is 0.3 - 0.5
        # paper used 0.5
        dvars_outlier = outlier(dvarsfile,dvarssave, 0.5)
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        fdsave=txtpath+'fd_outlier_sub'+`i`+'run'+`j`+'.txt'
        # common boundary for fd is 0.2 - 0.5
        # paper used 0.5
        fd_outlier = outlier(fdfile, fdsave, 0.5)

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        dvarssave=txtpath+'dvars_outlier_sub'+`i`+'run'+`j`+'.txt'
        # common boundary for dvars is 0.3 - 0.5
        # paper used 0.5
        dvars_outlier = outlier(dvarsfile,dvarssave, 0.5)
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        fdsave=txtpath+'fd_outlier_sub'+`i`+'run'+`j`+'.txt'
        # common boundary for fd is 0.2 - 0.5
        # paper used 0.5
        fd_outlier = outlier(fdfile, fdsave, 0.5)
