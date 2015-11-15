import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import smooth_gaussian

#possibly put in os function to specify path later

#this file was more of a test, but since can easily adapt it into a more useful
#script i left it in utils


img = nib.load("../../data/ds005/sub001/BOLD/task001_run001/bold.nii.gz")
data = img.get_data()

#just plot a random slice to see if works
spatial2 = smooth_gaussian.smooth_spatial(data,time = 50, fwhm = 5)[:, :, 16]
spatial3 = smooth_gaussian.smooth_spatial(data,time = 50, fwhm = 4)[:, :, 16]
spatial4 = smooth_gaussian.smooth_spatial(data,time = 50, fwhm = 3)[:, :, 16]


f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex = True, sharey = True)
ax1.imshow(data[:, :, 16, 50], cmap = 'gray')
ax1.set_title('Original')
ax2.imshow(spatial2, cmap = 'gray')
ax2.set_title('fwhm = 5 mm')
ax3.imshow(spatial3, cmap = 'gray')
ax3.set_title('fwhm = 4 mm')
ax4.imshow(spatial4, cmap = 'gray')
ax4.set_title('fwhm = 3mm')


plt.savefig("smoothed_images.png")
plt.close()





