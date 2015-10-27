# Compatibility with Python 3
from __future__ import print_function, division

# Interactive graphs for matplotlib at the IPython prompt
# %matplotlib

# Standard imports of libraries
import numpy as np
import matplotlib.pyplot as plt

# Load img processing nibabel function
import nibabel as nib
# Load the neural time course using pre-packaged function
from stimuli import events2neural

# Load data
img = nib.load('/home/benjamin/Documents/ds005/sub001/BOLD/task001_run001/bold.nii.gz')
data = img.get_data()
# check shape
shape = data.shape
data.shape
neural = events2neural('', TR, n_trs)
