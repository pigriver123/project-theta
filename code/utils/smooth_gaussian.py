#import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter, gaussian_filter1d

def fwhm2sigma(fwhm):
    """
    Converts FWHM (full width at half maximum) of Gaussian kernel to sigma
    (standard deviation) of the kernel, to be used as input in smoothing 
    functions

    Parameters
    ----------
    fwhm : Full width at half maximum, in millimeters. Ex: If expected signals
    of image is Gaussian with FWHM of 4 mm, fwhm = 4

    Returns
    -------
    sigma: value of sigma of the Gaussian curve
    """
    return fwhm/np.sqrt(8 * np.log(2))


def smooth_time_series(voxel_over_time, fwhm):
    #we might not need this function, and only need spatial smoothing. should
    #clarify next week
    """
    Returns smoothed time series of a voxel over time. 
    
    Parameters
    ----------
    voxel_over_time : time-series array of a voxel, e.g. data[32, 32, 16, :]
    fwhm : expected fwhm in millimeters of the Gaussian kernel
    
    Returns
    --------
    Smoothed time series array
    
    """
    sigma = fwhm2sigma(fwhm)
    return gaussian_filter1d(voxel_over_time, sigma)

def smooth_spatial(data, time, fwhm = 5):
    """
    Smooths a slice of the volume. Improves signal to noise ratio aka 
    sensitivity and makes error dist. more normal. However can reduce spatial 
    resolution and result in edge artifacts
    
    Parameters
    ---------
    data = BOLD signal data
    fwhm = expected fwhm in millimeters of Gaussian kernel. I believe the 
        supplement specifies a 5 mm fwhm on page 3
    time = Time aka which scan volume wanted 

    Returns
    -------
    Smoothed volume 
    """
    sigma = fwhm2sigma(fwhm)
    s = (gaussian_filter(data, [sigma, sigma, sigma, 0]))
    return(s[..., time])
    #return(gaussian_filter(data[..., time], sigma))



    
