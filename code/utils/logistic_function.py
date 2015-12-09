import numpy as np
import matplotlib.pyplot as plt

def plot_roc(logreg_proba, y):
    
    thresholds = np.linspace(1,0,101)

    ROC = np.zeros((101,2))

    for i in range(101):
        t = thresholds[i]

        # Classifier / label agree and disagreements for current threshold.
        TP_t = np.logical_and( logreg_proba[:,1] > t, y==1 ).sum()
        TN_t = np.logical_and( logreg_proba[:,1] <=t, y==0 ).sum()
        FP_t = np.logical_and( logreg_proba[:,1] > t, y==0 ).sum()
        FN_t = np.logical_and( logreg_proba[:,1] <=t, y==1 ).sum()

        # Compute false positive rate for current threshold.
        FPR_t = FP_t / float(FP_t + TN_t)
        ROC[i,0] = FPR_t

        # Compute true  positive rate for current threshold.
        TPR_t = TP_t / float(TP_t + FN_t)
        ROC[i,1] = TPR_t

    # Plot the ROC curve.
    fig = plt.figure(figsize=(6,6))
    plt.plot(ROC[:,0], ROC[:,1], lw=2)
    plt.xlim(-0.1,1.1)
    plt.ylim(-0.1,1.1)
    plt.xlabel('$FPR(t)$')
    plt.ylabel('$TPR(t)$')
    plt.grid()

    AUC = 0.
    for i in range(100):
        AUC += (ROC[i+1,0]-ROC[i,0]) * (ROC[i+1,1]+ROC[i,1])
    AUC *= 0.5

    plt.title('ROC curve, AUC = %.4f'%AUC)
    return fig, AUC