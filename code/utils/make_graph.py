"""
Script that plots framewise displacement(fd),  RMS signal derivative (DVARS), 
and meanSignal per subject per run and indicates potential outliers (motion-
induced artifacts) based on commonly used threshold of 0.2-0.5mm for FD and 
0.3-0.5% for DVARS. 0.5 was used for DVARS and 0.4 was used for FD.
"""
import graph_functions as gf
pathtodata = '../../data'
# need to create two loops, one for 1-9 and one for 10-16
# because of folder naming difference.

for i in range(1,10):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath= pathtodata+'ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=txtpath+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars_dict = gf.loadtxt_dict(dvarsfile, dvarsfigname)
        gf.plot_dvars(dvars_dict, saveit=True)
        # fd path and name, call function
        fdfile=txtpath+'fd.txt'
        fdfigname=txtpath+'fd_sub'+`i`+'run'+`j`+'.png'
        fd_dict = gf.loadtxt_dict(fdfile, fdfigname)
        gf.plot_fd(fd_dict, saveit=True)
        # mean path and name, call function
        niipath=pathtodata+'ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii.gz'
        meanfigname=txtpath+'mean_sub'+`i`+'run'+`j`+'.png'
        data_dict = gf.loadnib_dict(meandata, meanfigname)
        gf.meanSig(data_dict)

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath=pathtodata+'ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=txtpath+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars_dict = gf.loadtxt_dict(dvarsfile, dvarsfigname)
        gf.plot_dvars(dvars_dict, saveit=True)
        # fd path and name, call function
        fdfile=txtpath+'fd.txt'
        fdfigname=txtpath+'fd_sub'+`i`+'run'+`j`+'.png'
        fd_dict = gf.loadtxt_dict(fdfile, fdfigname)
        gf.plot_fd(fd_dict, saveit=True)
        # mean path and name, call function
        niipath=pathtodata+'ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii'
        meanfigname=txtpath+'mean_sub'+`i`+'run'+`j`+'.png'
        data_dict = gf.loadnib_dict(meandata, meanfigname)
        gf.meanSig(data_dict)

