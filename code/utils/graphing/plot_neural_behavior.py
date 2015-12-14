import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
"""
Function to plot the linear regression picture of behavial loss aversion
and neural loss aversion(-betagain-betaloss) at a single coordinate of standard brain
"""
def plot_neur_beh(x, y, z, betagains, betalosses, neural):
    """ 
     plot the linear regression picture of behavial loss aversion
     and neural loss aversion(-betagain-betaloss) of a single voxel's 
     coordinates of standard brain
     Parameters: 
     ----------- 
     x: the x coordinate of the voxel in standard brain
     y: the y coordinate of the voxel in standard brain 
     z: the z coordinate of the voxel in standard brain
     betagains: beta gain estimates from OLS regression of a single voxel,  
     4-d array (91*109*91*16)
     betalosses:beta loss estimates from OLS regression of a single voxel,  
     4-d array (91*109*91*16)
     neural: behavial loss aversion
      
     Returns: 
     -------- 
     A linear regression plot, the x axis is Neural loss aversion.
     The y axis is the Behavial loss aversion.The title is the coordinate of 
     the voxel in standrd brain.The plot is with the p value and r value of the
     linear regression.
     """ 

    X = -betagains[x, y, z, :] - betalosses[x, y, z, :]
    slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
    plt.scatter(X,Y)
    X_plot = np.linspace(-75,130,100)
    plt.plot(X_plot, X_plot*slope + intercept)
    plt.xlabel(r'Neural loss aversion ($-\beta loss-\beta{gain}$)' , fontsize=12)
    plt.ylabel(r'Behavoiral aversion (In$\lambda$)', fontsize=12)
    plt.text(-80, 2.2, r'r = %.4f'%r_value +', p = %.4f'%p_value, fontsize=12)
    plt.title('('+str(x)+',  '+str(y)+',  '+str(z)+')', fontsize=18)
    
