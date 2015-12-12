"""
Test smooth_gaussian module the following functions:
    fwhm2sigma
    smooth_time_series
    smooth_spatial

Run with::
    **Run from project-theta directory or code directory  with 'make test'

"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import sys
from numpy.testing import assert_allclose

# Append function path
sys.path.append('..')

# Path to the first subject, first run, this is used as the test data for 
# getGainLoss:
pathtotest = 'code/utils/tests/' 

# Load graph_functions:
from smooth_gaussian import fwhm2sigma, smooth_spatial, smooth_time_series

def test_smooth():
    # Test data:
    t_data = np.reshape(np.random.normal(0,1,64), (2,2,4,4))
    # No smooth
    fwhm_0 = 0
    t_fwhm0 = fwhm2sigma(fwhm_0)
    my_no_ssmooth = smooth_spatial(t_data, t_fwhm0)
    my_no_tsmooth = smooth_time_series(t_data, t_fwhm0)
    # Assert the same of as original data
    assert_allclose(t_data, my_no_ssmooth)
    assert_allclose(t_data, my_no_tsmooth)
    
    # Now with smoothing
    fwhm_1 = 5
    t_fwhm1 = fwhm2sigma(fwhm_1)
    my_ssmooth = smooth_spatial(t_data, t_fwhm1)
    my_tsmooth = smooth_time_series(t_data, t_fwhm1)
    assert (t_data != my_ssmooth).all()
    assert (t_data !=  my_tsmooth).all()
    
