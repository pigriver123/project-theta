"""
Script that plots framewise displacement(fd),  RMS signal derivative (DVARS), 
and meanSignal per subject per run and indicates potential outliers (motion-
induced artifacts) based on commonly used threshold of 0.2-0.5mm for FD and 
0.3-0.5% for DVARS. 0.5 was used for DVARS and 0.5 was used for FD.
"""
import sys
import json
# Paths
pathtodata = '../../data/'
pathtofig = '../../paper/figures/'
pathtofunction = '../utils'
# Append fuction path
sys.path.append(pathtofunction)
# Import function
from graphoutlier_functions import loadnib_dict, loadtxt_dict, plot_dvars, plot_fd, plot_meanSig


# load outlier files
dvars_out = json.load(open(pathtodata+"ds005/dvarsOutliers.txt"))
fd_out = json.load(open(pathtodata+"ds005/fdOutliers.txt"))

# need to create two loops, one for 1-9 and one for 10-16
# because of folder naming difference.

for i in range(1,10):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath= pathtodata+'ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=pathtofig+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars_dict = loadtxt_dict(dvarsfile, dvarsfigname)
        dvars_outliers = dvars_out['sub'+`i`+'run'+`j`]
        plot_dvars(dvars_dict, dvars_outliers, saveit=True)
        # fd path and name, call function
        fdfile=txtpath+'fd.txt'
        fdfigname=pathtofig+'fd_sub'+`i`+'run'+`j`+'.png'
        fd_dict = loadtxt_dict(fdfile, fdfigname)
        fd_outliers = fd_out['sub'+`i`+'run'+`j`]
        plot_fd(fd_dict, fd_outliers, saveit=True)
        # mean path and name, call function
        niipath=pathtodata+'ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii.gz'
        meanfigname=pathtofig+'mean_sub'+`i`+'run'+`j`+'.png'
        data_dict = loadnib_dict(meandata, meanfigname)
        plot_meanSig(data_dict, saveit=True)

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath=pathtodata+'ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=pathtofig+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars_dict = loadtxt_dict(dvarsfile, dvarsfigname)
        dvars_outliers = dvars_out['sub'+`i`+'run'+`j`]
        plot_dvars(dvars_dict, dvars_outliers, saveit=True)
        # fd path and name, call function
        fdfile=txtpath+'fd.txt'
        fdfigname=pathtofig+'fd_sub'+`i`+'run'+`j`+'.png'
        fd_dict = loadtxt_dict(fdfile, fdfigname)
        fd_outliers = fd_out['sub'+`i`+'run'+`j`]
        plot_fd(fd_dict, fd_outliers, saveit=True)
        # mean path and name, call function
        niipath=pathtodata+'ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii.gz'
        meanfigname=pathtofig+'mean_sub'+`i`+'run'+`j`+'.png'
        data_dict = loadnib_dict(meandata, meanfigname)
        plot_meanSig(data_dict, saveit=True)

