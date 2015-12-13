"""
Test regression_function module the following functions:
    create_confusion
    getmin_thrs
    plot_roc

Run with::
    **Run from project-theta or code directory with 'make test'

"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import os
import sys
from numpy.testing import assert_allclose

# Set path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Load graph_functions:
from logistic_function import create_confusion, getMin_thrs, plot_roc

def test_create_confusion():
    # Sample data
    actual = np.array([0,1,1,0,0,1])
    fittedin = np.array([[0,0,0,0,0,0],[0.2, 0.6, 0.7, 0.1, 0.3, 0.9]])
    fitted = np.array([0.2, 0.6, 0.7, 0.1, 0.3, 0.9])
    # thrs_inc = 0.2
    thrs_array = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    t_confusion = np.ones((len(thrs_array), 5))
    t_confusion[:,0] = thrs_array
    # thrs_inc = 0.2
    for index, item in enumerate(thrs_array):
        a = sum((actual == 1) & (fitted > item))
        b = sum((actual == 0) & (fitted <= item))
        c = sum((actual == 0) & (fitted > item))
        d = sum((actual == 1) & (fitted <= item))
        t_confusion[index, 1:5] = [a, b, c, d]
    # my function
    my_confusion = create_confusion(fittedin.T, actual, thrs_inc = 0.2)

    # Assert
    assert_allclose(t_confusion, my_confusion)

def test_getMin_thrs():
    # Test data
    t_data = np.array([[0, 1, 2, 2, 3], [0.25, 1, 5, 1, 1], 
                       [0.3, 3, 3, 1, 1], [0.5, 2, 3, 1, 3], 
                       [1, 4, 1, 2, 1]])
    # Should return the row with the lowest sum of 4th and 5th column values
    # the 2nd row
    t_result = t_data[2, :]
    t_result = np.array([t_result[0], t_result[3], t_result[4]])
    
    my_thrs, my_fp, my_fn = getMin_thrs(t_data)
    my_result = np.array([my_thrs, my_fp, my_fn])
    
    # Assert
    assert_allclose(t_result, my_result)

def test_plot_roc():
    # test data
    t_data = np.array([[0, 1, 2, 2, 3], [0.25, 1, 5, 1, 1], 
                       [0.5, 2, 3, 1, 3],[1, 4, 1, 2, 1]])
    fig = 111
    # Calculating by hand: the roc matrix
    # first column: 4th entry of each row / (4th + 3rd entries)
    # second column: 2nd entry of each row / (2nd + 5th entries)
    t_roc = np.array([[2/4, 1/4], [1/6, 1/2], [1/4, 2/5], [2/3, 4/5]])
    dif1 = np.array([t_roc.T[0][i+1] - t_roc.T[0][i] for i in range(len(t_roc.T[0])-1)])
    dif2 = np.array([t_roc.T[1][i+1] + t_roc.T[1][i] for i in range(len(t_roc.T[1])-1)])
    t_AUC = sum(dif1*dif2)* (-0.5)

    # my function
    my_fig, my_ROC, my_AUC = plot_roc(t_data, fig)

    # assert
    assert (t_AUC == my_AUC)
    assert (fig == my_fig)
    assert_allclose(t_roc, my_ROC)
