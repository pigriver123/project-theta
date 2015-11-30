import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression

nsub = 16
beh_lambda = np.array([])
beh_score = np.array([])
val_score = np.array([])
for i in np.arange(1, nsub+1):
    run1 = np.loadtxt('ds005/sub0'+ str(i).zfill(2)+
                      '/behav/task001_run001/behavdata.txt', skiprows = 1)
    run2 = np.loadtxt('ds005/sub0'+ str(i).zfill(2)+
                      '/behav/task001_run002/behavdata.txt', skiprows = 1)
    run3 = np.loadtxt('ds005/sub0'+ str(i).zfill(2)+
                      '/behav/task001_run003/behavdata.txt', skiprows = 1)
    behav = np.concatenate((run1, run2, run3), axis=0)
    behav = behav[np.logical_or.reduce([behav[:,5] == x for x in [0,1]])]
    X = zip(np.ones(len(behav)), behav[:, 1],behav[:, 2])
    y = behav[:, 5]
    logreg = linear_model.LogisticRegression(C=1e5) 
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
    

np.savetxt('lambda.txt', beh_lambda)
np.savetxt('reg_score.txt', beh_score)
np.savetxt('cross_val_score.txt', val_score)