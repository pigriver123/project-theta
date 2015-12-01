"""
Some utility graphing functions for doing linear regression diagnostics:
Main goal is to check the assumptions of our model, namely:
1. Constant variance/linearity of our residuals: residual vs fitted
2. Normality of errors: qqplot

"""
import scipy.stats as stats
import matplotlib.pyplot as plt 

# Note savefig location/path assumes call from script directory

def qqplot(residuals, dist_type = 'norm', subplot_num = None, saveit = False):
    """
    Parameters
    ----------
    residuals: 1-d array
    subplot_num: location of subplot in 3 digits or a list of 3 numericals

    Returns:
    --------
    QQplot w.r. to indicated distribution
    Out: displays which subplot plotted
    
    NOTE: If plotting mutiple subplots and wish to save figure, only the last 
    subplot should include 'saveit=True' 

    """
    if subplot_num != None:
        out = str(subplot_num)
        if type(subplot_num) is list:
            plt.subplot(subplot_num[0],subplot_num[1],subplot_num[2])
            plotnum = str(subplot_num[2])
        else:
            plt.subplot(subplot_num)
            plotnum = str(subplot_num)[-1]
    else:
        out = 'Single Plot'
        plotnum = ''
    stats.probplot(residuals, dist = dist_type, plot = plt)
    plt.title(dist_type + "QQ Plot" + plotnum)
    if saveit:
        plt.savefig('../../paper/figures/qqplot.png')
        plt.close()
        savecond = 'saved'
    else: 
        savecond = 'not saved'
    return  out + ' plotted' + "," + savecond

def res_var(var_val, residuals, name, subplot_num = None, saveit = False):
    """
    Parameters
    ----------
    residuals: 1-d array
    var_val: variable values 1-d array
    subplot_num: location of subplot in 3 digits or a list of 3 numericals
    name: string, name of variable

    Returns:
    --------
    Residual vs Fitted Plot 
    Ouput: displays which subplot plotted
    
    NOTE: If plotting mutiple subplots and wish to save figure, only the last 
    subplot should include 'saveit=True' 

    """
 
    if subplot_num != None:
        if type(subplot_num) is list:
            plt.subplot(subplot_num[0],subplot_num[1],subplot_num[2])
            plotnum = str(subplot_num[2])
        else:
            plt.subplot(subplot_num)
            plotnum = str(subplot_num)[-1]
        out = str(subplot_num)
    else: 
        out = 'Single plot'
        plotnum = ''
    plt.plot(var_val, residuals, 'o')
    plt.axhline(y = 0)
    plt.title("Residual vs " + name + plotnum)
    plt.xlabel(name +" Values")
    plt.ylabel("Residual Values")
    if saveit:
        plt.savefig('../../paper/figures/res_' + name +'.png')
        plt.close()
        savecond = 'saved'
    else:
        savecond =  "not saved"
    return  out + ' plotted' + "," + savecond

