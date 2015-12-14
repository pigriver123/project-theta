"""
This scipt mainly does two things.One thing is to plot significant p values of behavial loss aversion
against neural loss aversion of all the voxels.The second thing is to plot the actual linear regression
of begavial loss aversion against neural loss aversion of a single voxel
"""


from scipy import stats
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
import nibabel as nib
sys.path.append('../utils/functions')
from sig_region import stat_region
sys.path.append('../utils/graphing')
from neural_behavior import plot_neur_beh


pgain = np.loadtxt("../../results/texts/pgain.txt")
slopegain = np.loadtxt("../../results/texts/slopegain.txt")
ploss = np.loadtxt("../../results/texts/ploss.txt")
slopeloss = np.loadtxt("../../results/texts/slopeloss.txt")

"""
The following part of script will plot the significant gain p values of the linear regression
between behavial loss aversion and neural loss averision on standard brain.The slices is by z
axis.And we use 31-60 slices.
"""
p = pgain
slope = slopegain
siglevel = 0.001
sig_inx = p <= siglevel
mask = p != 1
base = nib.load('../../data/templates/mni_standard.nii')
base = base.get_data()
p_plot = np.zeros(slope.shape)
p_plot[p > siglevel] = np.nan
p_plot[p <= siglevel] = slope[p <= siglevel]
p_plot = p_plot.reshape(91, 109, 91)
plot_number=1
fig = plt.figure(figsize = (60, 80))

for subject in range(31, 61):
    axis = fig.add_subplot(6, 5, plot_number)
    plt.imshow(base[:, :, subject], cmap = plt.get_cmap('gray'), alpha = 0.3)
    img = axis.imshow(p_plot[:, :, subject], cmap=plt.get_cmap('rainbow'), alpha = 1, 
                      interpolation = 'nearest', vmin = -0.03, vmax = 0.03)
    plt.colorbar(img, ax=axis, fraction=0.023, pad=0.02)
    
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)
    axis.set_title('Z axis Slice ' + str(subject), fontsize = 26)
    plot_number += 1

fig.savefig("../../results/figures/sig_cor_z_gain.png")

"""
The following part of script will plot the significant loss p values of the linear regression
between behavial loss aversion and neural loss averision on standard brain.The slices are by z
axis.And we use 31-60 slices.
"""
p = ploss
slope = slopeloss
siglevel = 0.001
sig_inx = p <= siglevel
mask = p != 1
base = nib.load('../../data/templates/mni_standard.nii')
base = base.get_data()
p_plot = np.zeros(slope.shape)
p_plot[p > siglevel] = np.nan
p_plot[p <= siglevel] = slope[p <= siglevel]
p_plot = p_plot.reshape(91, 109, 91)
plot_number=1
fig = plt.figure(figsize = (60, 80))

for subject in range(31, 61):
    axis = fig.add_subplot(6, 5, plot_number)
    plt.imshow(base[:, :, subject], cmap = plt.get_cmap('gray'), alpha = 0.3)
    img = axis.imshow(p_plot[:, :, subject], cmap=plt.get_cmap('rainbow'), alpha = 1, 
                      interpolation = 'nearest', vmin = -0.03, vmax = 0.03)
    plt.colorbar(img, ax=axis, fraction=0.023, pad=0.02)
    
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)
    axis.set_title('Z axis Slice ' + str(subject), fontsize = 26)
    plot_number += 1

fig.savefig("../../results/figures/sig_cor_z_loss.png")

"""
The following part of script will plot the significant difference p values of the linear regression
between behavial loss aversion and neural loss averision on standard brain.The slices are by z
axis.And we use 31-60 slices.
"""
p = pgainloss
slope = slopegainloss
siglevel = 0.001
sig_inx = p <= siglevel
mask = p != 1
base = nib.load('../../data/templates/mni_standard.nii')
base = base.get_data()
p_plot = np.zeros(slope.shape)
p_plot[p > siglevel] = np.nan
p_plot[p <= siglevel] = slope[p <= siglevel]
p_plot = p_plot.reshape(91, 109, 91)
plot_number=1
fig = plt.figure(figsize = (60, 80))

for subject in range(31, 61):
    axis = fig.add_subplot(6, 5, plot_number)
    plt.imshow(base[:, :, subject], cmap = plt.get_cmap('gray'), alpha = 0.3)
    img = axis.imshow(p_plot[:, :, subject], cmap=plt.get_cmap('rainbow'), alpha = 1, 
                      interpolation = 'nearest', vmin = -0.03, vmax = 0.03)
    plt.colorbar(img, ax=axis, fraction=0.023, pad=0.02)
    
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)
    axis.set_title('Z axis Slice ' + str(subject), fontsize = 26)
    plot_number += 1

fig.savefig("../../results/figures/sig_cor_z_gainloss.png")

"""
The following part of script will plot the significant difference p values of the linear regression
between behavial loss aversion and neural loss averision on standard brain.The slices are by y
axis.And we use 31-60 slices.
"""
plot_number=1
fig = plt.figure(figsize = (60, 80))

for subject in range(31, 61):
    axis = fig.add_subplot(6, 5, plot_number)
    plt.imshow(base[:, subject, :], cmap = plt.get_cmap('gray'), alpha = 0.3)
    plt.imshow(p_plot[:, subject, :], cmap=plt.cm.RdBu, alpha = 1)
    
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)
    axis.set_title('Y axis: Slice ' + str(subject), fontsize=18)
    plot_number += 1

fig.savefig("../../results/figures/sig_cor_y_neural_aversion.png")

"""
The following part of script will plot the linear regression plot of three voxels of behavial loss aversion
and neural loss aversion.The coordinates of three voxels in standard brain are (22,81,44),(71,59,56)
and (46,44,68)
"""
betagains = np.empty([902629, 16])
betalosses = np.empty([902629, 16])

for i in np.arange(1, 17):
    betas = np.loadtxt("../../results/texts/beta"+str(i)+".txt")
    betas = betas.transpose()
    betagains[:, i-1] = betas[:,0]
    betalosses[:, i-1] = betas[:,1]

betagains = np.empty([902629, 16])
betalosses = np.empty([902629, 16])
for i in np.arange(1, 17):
    betas = np.loadtxt("../../results/texts/beta"+str(i)+".txt")
    betas = betas.transpose()
    betagains[:, i-1] = betas[:,0]
    betalosses[:, i-1] = betas[:,1]

betagains = betagains.reshape(91, 109, 91, 16)
betalosses = betalosses.reshape(91, 109, 91, 16)


Y = np.loadtxt("../../results/texts/lambda.txt")
plot_neur_beh(22, 81, 44, betagains, betalosses, Y)
fig.savefig("../../results/figures/linearreg_22_81_44.png")
plot_neur_beh(71, 59, 56, betagains, betalosses, Y)
fig.savefig("../../results/figures/linearreg_71_59_56.png")
plot_neur_beh(46, 44, 68, betagains, betalosses, Y)
fig.savefig("../../results/figures/linearreg_46_44_48.png.png")



