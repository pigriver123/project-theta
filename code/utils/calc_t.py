import matplotlib.pyplot as plt 
import nibabel as nib
import numpy as np
import os
from stimuli import events2neural
from scipy.stats import gamma
import math
import numpy.linalg as npl
from scipy.stats import mstats
from scipy.stats import t

def significant(a,b,c):
    df=len(b)-2
    y_hat = a.dot(c)
    residuals = b - y_hat
    ma=npl.pinv(a.transpose().dot(a))
    RSS = np.sum(residuals ** 2)
    df = a.shape[0] - npl.matrix_rank(a)
    MRSS = RSS / df
    s2 = MRSS
    v_cov = s2 * npl.inv(a.T.dot(a))
    numerator1 = c[0]
    denominator1 = np.sqrt(v_cov[0, 0])
    t1= numerator1 / denominator1
    numerator2 = c[1]
    denominator2 = np.sqrt(v_cov[1, 1])
    t2= numerator2 / denominator2
    return t1,t2

