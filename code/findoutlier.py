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
        dvars_outlier = outlier(dvarsfile,dvarssave)
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        fdsave=txtpath+'fd_outlier_sub'+`i`+'run'+`j`+'.txt'
        fd_outlier = outlier(fdfile, fdsave)

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        dvarssave=txtpath+'dvars_outlier_sub'+`i`+'run'+`j`+'.txt'
        dvars_outlier = outlier(dvarsfile,dvarssave)
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        fdsave=txtpath+'fd_outlier_sub'+`i`+'run'+`j`+'.txt'
        fd_outlier = outlier(fdfile, fdsave)
