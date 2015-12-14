import numpy as np
import json
import sys
pathtofunction = '../utils/functions'
# Append the sys path
sys.path.append(pathtofunction)
from outlierfunction import outlier

dvars_out = {}
fd_out = {}

for i in range(1,10):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='../../data/ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        dvars_data = np.loadtxt(dvarsfile)
        # common boundary for dvars is 0.3 - 0.5
        # paper used 0.5
        dvars_outlier = outlier(dvars_data, 0.5)
        dvars_out['sub'+`i`+'run'+`j`] = dvars_outlier[0].tolist()
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        fd_data = np.loadtxt(fdfile)
        # common boundary for fd is 0.2 - 0.5
        # paper used 0.5
        fd_outlier = outlier(fd_data, 0.5)
        fd_out['sub'+`i`+'run'+`j`] = fd_outlier[0].tolist()

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='../../data/ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function to get outliers
        dvarsfile=txtpath+'dvars.txt'
        dvars_data = np.loadtxt(dvarsfile)
        # common boundary for dvars is 0.3 - 0.5
        # paper used 0.5
        dvars_outlier = outlier(dvars_data, 0.5)
        dvars_out['sub'+`i`+'run'+`j`] = dvars_outlier[0].tolist()
        # fd path and name, call function to get outliers
        fdfile=txtpath+'fd.txt'
        fd_data = np.loadtxt(fdfile)
        # common boundary for fd is 0.2 - 0.5
        # paper used 0.5
        fd_outlier = outlier(fd_data, 0.5)
        fd_out['sub'+`i`+'run'+`j`] = fd_outlier[0].tolist()

json.dump(dvars_out, open("../../results/dvarsOutliers.txt",'w'))
json.dump(fd_out, open("../../results/fdOutliers.txt",'w'))

