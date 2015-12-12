"""
Test basic_util module the following functions:
    loadtxt_dict
    loadnib_dict
    vol_mean

Run with::
   `make test` from code or project directory
"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import sys, os
from numpy.testing import assert_array_equal
import nibabel as nib

# Set path
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))

# Load graph_functions:
from basic_util import loadtxt_dict, loadnib_dict, vol_mean


# Test txt:
np.savetxt('temp.txt', range(30))
# Test np array, dim = 4
# x1 = np.random.randn(100).reshape((2, 5, 2, 5))
x2 = np.arange(64).reshape((2, 4, 2, 4))
 
def test_loadtxt_dict():
    # Using loadtxt_dict
    mydict = loadtxt_dict('temp.txt', 'mytxt')
    # True dictionary
    truedict = {'mytxt': np.arange(30.)}
    assert_array_equal(list(mydict.values()), list(truedict.values()))
    assert_array_equal(mydict.keys(), truedict.keys())

def test_vol_mean():
    mymean = vol_mean(x2)
    truemean = np.array([30., 31 ,32 ,33])
    assert_array_equal(mymean, truemean)    

def test_loadnib_dict():
    # create test img
    t_data = np.array([1,2,3])
    t_dict = {'testnib': t_data}
    img = nib.Nifti1Image(t_data, np.eye(4))
    nib.save(img,'testnib.nii.gz')
    # my function
    my_dict = loadnib_dict('testnib.nii.gz', 'testnib')
    assert (t_dict.keys()[0] == my_dict.keys()[0])
    assert_array_equal(t_dict.values()[0], my_dict.values()[0])
