import numpy as np
from outlierfunction import outlier
import json

dvars_out = {}
fd_out = {}

for i in range(1,10):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        # common boundary for dvars is 0.3 - 0.5
        # paper used 0.5
        dvars_outlier = outlier(dvarsfile, 0.5)
        dvars_out['sub'+`i`+'run'+`j`] = dvars_outlier[0].tolist()
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        # common boundary for fd is 0.2 - 0.5
        # paper used 0.5
        fd_outlier = outlier(fdfile, 0.5)
        fd_out['sub'+`i`+'run'+`j`] = fd_outlier[0].tolist()

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        # common boundary for dvars is 0.3 - 0.5
        # paper used 0.5
        dvars_outlier = outlier(dvarsfile, 0.5)
        dvars_out['sub'+`i`+'run'+`j`] = dvars_outlier[0].tolist()
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        # common boundary for fd is 0.2 - 0.5
        # paper used 0.5
        fd_outlier = outlier(fdfile, 0.5)
        fd_out['sub'+`i`+'run'+`j`] = fd_outlier[0].tolist()

json.dump(dvars_out, open("../../data/ds005/dvarsOutliers.txt",'w'))
json.dump(fd_out, open("../../data/ds005/fdOutliers.txt",'w'))

