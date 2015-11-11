"""
Test graph_function module the following functions:
    loadtxt_dict
    loadnib_dict
    vol_mean

Run with::

    nosetests test_graph_functions.py
"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import os
import sys
from numpy.testing import assert_almost_equal, assert_array_equal

# Set path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load graph_functions:
from graph_functions import loadtxt_dict, loadnib_dict, vol_mean

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
    assert all(mydict.values()[0] == truedict.values()[0])
    assert_array_equal(mydict.keys(), truedict.keys())

def test_vol_mean():
    mymean = vol_mean(x2)
    truemean = np.array([30., 31 ,32 ,33])
    assert_array_equal(mymean, truemean)    
