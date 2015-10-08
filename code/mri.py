import numpy as np
import matplotlib.pyplot as plt
# %matplotlib
import nibabel as nib
img = nib.load('bold.nii')
data = img.get_data()
data = data[..., 1:]
data.shape
vol0 = data[..., 0]
vol0.shape
mean_data = np.mean(data, axis=-1)
mean_data[42, 32, 19] = np.max(mean_data)
plt.imshow(mean_data[:, :, 19], cmap='gray', interpolation='nearest')
voxel_time_course = data[42, 32, 19]
plt.plot(voxel_time_course)
img.shape
from stimuli import events2neural
TR = 2  # time between volumes
n_trs = img.shape[-1]  # The original number of TRs
neural = events2neural('cond002.txt', TR, n_trs)
plt.plot(neural)
neural = neural[1:]
plt.plot(neural, voxel_time_course, 'o')
np.corrcoef(neural, voxel_time_course)
