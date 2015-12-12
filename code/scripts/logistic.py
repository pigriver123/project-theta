import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
import sys

# Path to function
pathtofunction = '../utils/functions'
# Append path to sys
sys.path.append(pathtofunction)

from logistic_function import create_confusion, getMin_thrs, plot_roc

pathtofolder = '../../data/'

nsub = 16
beh_lambda = np.array([])
beh_score = np.array([])
val_score = np.array([])
Min_thrs = np.array([])
AUC_smr = np.array([])
fig = plt.figure(figsize=(20,20))
for i in np.arange(1, nsub+1):
    run1 = np.loadtxt(pathtofolder + 'ds005/sub0'+ str(i).zfill(2)+
                      '/behav/task001_run001/behavdata.txt', skiprows = 1)
    run2 = np.loadtxt(pathtofolder + 'ds005/sub0'+ str(i).zfill(2)+
                      '/behav/task001_run002/behavdata.txt', skiprows = 1)
    run3 = np.loadtxt(pathtofolder + 'ds005/sub0'+ str(i).zfill(2)+
                      '/behav/task001_run003/behavdata.txt', skiprows = 1)
    behav = np.concatenate((run1, run2, run3), axis=0)
    behav = behav[np.logical_or.reduce([behav[:,5] == x for x in [0,1]])]
    X = zip(np.ones(len(behav)), behav[:, 1], behav[:, 2])
    y = behav[:, 5]
    logreg = LogisticRegression(C=1e5)
    # C=1e5 specifies a regularization strength
    logreg.fit(X, y)
    # calculate the lambdas, the behavioral loss aversion measure
    beh_sub_lambda = np.log(-logreg.coef_[0, 2] / logreg.coef_[0, 1])
    beh_lambda = np.append(beh_lambda, beh_sub_lambda)
    # check the accuracy on the training set
    # Returns the mean accuracy on the given test data and labels.
    beh_sub_score = logreg.score(X, y)
    beh_score = np.append(beh_score, beh_sub_score)
    # evaluate the model using 10-fold cross-validation
    scores = cross_val_score(LogisticRegression(), X, y, 
        scoring='accuracy', cv=10)
    val_score = np.append(val_score, scores.mean())
    # calculate the AUC and plot ROC curve for each subject
    logreg_proba = logreg.predict_proba(X)
    confusion = create_confusion(logreg_proba, y)
    addsub = fig.add_subplot(4, 4, i)
    addsub, ROC, AUC = plot_roc(confusion, addsub)
    # Plot the ROC curve.
    plt.plot(ROC[:,0], ROC[:,1], lw=2)
    plt.xlim(-0.1,1.1)
    plt.ylim(-0.1,1.1)
    plt.xlabel('$FPR(t)$')
    plt.ylabel('$TPR(t)$')
    plt.grid()
    plt.title('subject '+ str(i)+', AUC = %.4f'%AUC)
    #------------------------------------------------------------------------#
    Min_thrs = np.append(Min_thrs, getMin_thrs(confusion))
    AUC_smr = np.append(AUC_smr, AUC)

np.savetxt(pathtofolder + 'ds005/models/lambda.txt', beh_lambda)
np.savetxt(pathtofolder + 'ds005/models/reg_score.txt', beh_score)
np.savetxt(pathtofolder + 'ds005/models/cross_val_score.txt', val_score)
np.savetxt(pathtofolder + 'ds005/models/Min_thrs.txt', Min_thrs.reshape(16,3))
np.savetxt(pathtofolder + 'ds005/models/AUC_smr.txt', AUC_smr)
fig.savefig(pathtofolder + 'ds005/models/roc_curve')

