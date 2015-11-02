import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

for i in range(1,10):
    for j in range(1,4):
        txtpath='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=txtpath+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars(dvarsfile, dvarsfigname)
        fdfile=txtpath+'fd.txt'
        fdfigname=txtpath+'fd_sub'+`i`+'run'+`j`+'.png'
        fd(fdfile, fdfigname)
        niipath='ds005/sub00'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii'
        meanfigname=txtpath+'mean_sub'+`i`+'run'+`j`+'.png'
        meanSig(meandata, meanfigname)

for i in range(10,17):
    for j in range(1,4):
        txtpath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`+'/QA/'
        dvarsfile=txtpath+'dvars.txt'
        dvarsfigname=txtpath+'dvars_sub'+`i`+'run'+`j`+'.png'
        dvars(dvarsfile, dvarsfigname)
        fdfile=txtpath+'fd.txt'
        fdfigname=txtpath+'fd_sub'+`i`+'run'+`j`+'.png'
        fd(fdfile, fdfigname)
        niipath='ds005/sub0'+`i`+'/BOLD/task001_run00'+`j`
        meandata=niipath+'/bold.nii'
        meanfigname=txtpath+'mean_sub'+`i`+'run'+`j`+'.png'
        meanSig(meandata, meanfigname)

