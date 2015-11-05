from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

def merge_cond(behav_cond, task_cond):
    """
    Input: 
    behav_cond: txt file
    task_cond: txt file
    
    Output: array 2d
    Merged behav_task_cond
    An array of dim 2, merging the behav condition text file with the task 
    conditions

    """
    # Load the two text files
    behav = np.loadtxt(behav_cond, skiprows = 1)
    task = np.loadtxt(task_cond)
    # merge the two txt files
    behav_task = np.insert(behav, [1],  task[:,1:], axis = 1)
    return behav_task

def events2neural_extend(behav_task, tr, n_trs):
    """ Return predicted neural time course from event file `task_fname`

    Parameters
    ----------
    behav_task : array 
        Combined behav_task condition
    tr : float
        TR in seconds
    n_trs : int
        Number of TRs in functional run

    Returns
    -------
    time_course : array shape (n_trs, K)
        Predicted neural time course, one value per TR
    1. The TR
    2. For which tr there is a signal (0 or 1)
    3. If there is a signal, whether that signal is due to the behavior
    to accept or the behavior to reject. (0 for no signal, 1 for accept, 2 
    for reject)
    """
    # Check that the file is plausibly a task file
    if behav_task.ndim != 2 or behav_task.shape[1] != 9:
        raise ValueError("Is {0} really a task file?", behav_task)
    # Convert onset, duration seconds to TRs
    behav_task[:, :2] = behav_task[:, :2] / tr
    # Neural time course from onset, duration, amplitude, gain, loss, PTval, 
    # respnum,respcat, RT for each event
    time_course = np.zeros((n_trs, 7))
    for on, dur, amp, gain, loss, PTval, respnum,respcat, RT in behav_task:
        time_course[on:on + dur,0] = amp
        time_course[on:on + dur,1] = gain
        time_course[on:on + dur,2] = loss
        time_course[on:on + dur,3] = PTval
        time_course[on:on + dur,4] = respnum
        time_course[on:on + dur,5] = respcat
        time_course[on:on + dur,6] = RT
    return time_course

def plot_time_course(time_course):
    """
    Simple function to plot time_course, an array from return of 
    events2neural_extend
    """
    plt.plot(time_course[:,0])    
    plt.show()
