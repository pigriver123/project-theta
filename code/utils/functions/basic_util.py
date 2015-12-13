"""
A collection of basic utility functions for use in outlier detection/graphing
of fd, dvars, and meanSignal, see graphoutlier_functions.py
"""

import numpy as np
import nibabel as nib


def loadtxt_dict(file_name, fig_name):
    """
    Input: 
        Txt file specified by file_name
        Name of figure file wish to output
    
    Output:
        Dictonary that attached to file_name the np array after loading 
    file_name
    """
    data = np.loadtxt(file_name)
    dict_out = {fig_name: data}
    return dict_out

def loadnib_dict(file_name, fig_name):
    """
    Input: 
        Bold file (bold.nii, bold.nii.gz) specified by file_name 
        Name of figure file wish to output
    
    Output:
    Dictonary that attached to file_name the np array after loading file_name
    """
    img = nib.load(file_name)
    data = img.get_data()
    dict_out = {fig_name: data}
    return dict_out


# Calculate mean
def vol_mean(data):
    """ Return mean across voxels for $D `data`
    
    Input:
        np array of data
    Output: np array of dim (T,)
        mean of data across all but the last dimension
    """
    mean_list = []
    # Loop over the each volume and outputs the mean of each dimension
    for i in range(data.shape[-1]):
        mean = np.mean(data[...,i])
        mean_list.append(mean)
    return np.asarray(mean_list)
