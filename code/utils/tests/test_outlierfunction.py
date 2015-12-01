"""
Test outlierfunction

Run with::

    nosetests test_outlierfunction.py
"""
# Python 3 compatibility
from __future__ import print_function, division

import numpy as np

from numpy.testing import assert_allclose

import os

import sys

# Set path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load function

from outlierfunction import outlier

def test_outlierfunction():
    # Test outlierfunction
    # Test data 
    x = np.random.normal(size=(1000))
    expected = np.where(x>2)[0]
    actual = np.ravel(outlier(x, 2))
    # Did you forget to return the value?
    if actual is None:
        raise RuntimeError("function returned None")
    assert_allclose(expected, actual)
