import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

# need to create two loops, one for 1-9 and one for 10-16
# because of folder naming difference.

for i in range(1,10):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=txtpath+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars(dvarsfile, dvarsfigname)
        # fd path and name, call function
        fdfile=txtpath+'fd.txt'
        fdfigname=txtpath+'fd_sub'+`i`+'run'+`j`+'.png'
        fd(fdfile, fdfigname)
        # mean path and name, call function
        niipath='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii'
        meanfigname=txtpath+'mean_sub'+`i`+'run'+`j`+'.png'
        meanSig(meandata, meanfigname)

for i in range(10,17):
    for j in range(1,4):
        # set general path for reaching dvars and fd files
        # also path for saving files
        txtpath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        # dvars path and name, call function
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=txtpath+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars(dvarsfile, dvarsfigname)
        # fd path and name, call function
        fdfile=txtpath+'fd.txt'
        fdfigname=txtpath+'fd_sub'+`i`+'run'+`j`+'.png'
        fd(fdfile, fdfigname)
        # mean path and name, call function
        niipath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii'
        meanfigname=txtpath+'mean_sub'+`i`+'run'+`j`+'.png'
        meanSig(meandata, meanfigname)

