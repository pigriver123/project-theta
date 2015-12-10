import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../utils/functions')
import smooth_gaussian
import os


os.chdir("../../data")
plot_number = 1

fig = plt.figure(figsize = (50, 70))
for subject in range(1, 17):
    for run in range(1, 4):
        path = 'ds005/sub0' + str(subject).zfill(2) + '/BOLD/task001_run00' + str(run) + '/bold.nii.gz' 
        img = nib.load(path)
        data = img.get_data()
        data = smooth_gaussian.smooth_spatial(data)
        mean_data = np.mean(data, axis = -1)
        axis = fig.add_subplot(16, 3, plot_number )
        axis.hist(np.ravel(mean_data), bins = 100)
        axis.set_title('Subject ' + str(subject) + ', Run ' + str(run))
        plot_number += 1

#fig.tight_layout()
fig.savefig('../paper/figures/mean_hists.png')


