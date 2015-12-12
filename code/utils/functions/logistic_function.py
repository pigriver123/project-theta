import numpy as np
import matplotlib.pyplot as plt

def create_confusion(logreg_proba, y, thrs_inc=0.01):
    """
        Creates the confusion matrix based on various levels of discriminate
        probability thresholds
        
        Parameters
        ----------
        y: Actual responses, 1-d array with values 0 or 1
        logreg_proba: Fitted probabilities, 2-d array with values between 0 and 1 in second column
        thrs_inc: increment of threshold probability (default 0.05)
        
        Returns
        -------
        Confusion Matrix : Array of dim (X, 5) where X is the number of different
        thresholds
        Column 1: Threshold value between 0, 1
        Columns 2-5 show counts for:
        Column 2: True postive
        Column 3: True negative
        Column 4: False postive
        Column 5: False negative
        """
    thrs_array = np.linspace(0, 1, 1/thrs_inc +1)
    confusion = np.ones((len(thrs_array), 5))
    confusion[:,0] = thrs_array
    for i in range(int(1/thrs_inc +1)):
        t = thrs_array[i]
        # Classifier / label agree and disagreements for current threshold.
        TP_t = np.logical_and( logreg_proba[:,1] > t, y==1 ).sum()
        TN_t = np.logical_and( logreg_proba[:,1] <=t, y==0 ).sum()
        FP_t = np.logical_and( logreg_proba[:,1] > t, y==0 ).sum()
        FN_t = np.logical_and( logreg_proba[:,1] <=t, y==1 ).sum()
        confusion[i, 1:5] = [TP_t, TN_t, FP_t, FN_t]
    return confusion


def getMin_thrs(confusion):
    """
        Returns the threshold with the smallest number of wrong predictions
        
        Parameters:
        -----------
        Confustion matrix: 2-d array with 5 columns
        
        Returns:
        --------
        thrs: min threshold that gives minimum wrong predictions: columns 3 +
        column 4
        false_pos: number of incorrect trues
        false_neg: number of incorrect falses
        """
    thrs_min = np.min(confusion[:,3]+ confusion[:,4])
    col_out = confusion[thrs_min, :]
    thrs = col_out[0]
    false_pos = col_out[3]
    false_neg = col_out[4]
    return thrs, false_pos, false_neg


def plot_roc(confusion, fig):
    """
        function to plot the ROC (receiver operating characteristic) curve and
        calculate the corresponding AUC (Area Under Curve).
        
        Parameters:
        -----------
        Confustion matrix: 2-d array with 5 columns
        
        Returns:
        --------
        fig: The ROC curve
        AUC: Correspong AUC value
        """
    ROC = np.zeros((confusion.shape[0],2))
    for i in range(confusion.shape[0]):
        # Compute false positive rate for current threshold.
        FPR_t = confusion[i, 3] / float(confusion[i, 3] + confusion[i, 2])
        ROC[i,0] = FPR_t
        
        # Compute true  positive rate for current threshold.
        TPR_t = confusion[i, 1] / float(confusion[i, 1] + confusion[i, 4])
        ROC[i,1] = TPR_t

    AUC = 0.
    for i in range(confusion.shape[0]-1):
        AUC += (ROC[i+1,0]-ROC[i,0]) * (ROC[i+1,1]+ROC[i,1])
    AUC *= -0.5
    
    return fig, ROC,  AUC
