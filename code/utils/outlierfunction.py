
# find outliers based on DVARS and FD

def outlier(data, bound):
    '''
    Input:
        data: array of values
        bound: threshold for outliers
    
    Output:
        indices of outliers
    '''
    outlier = []
    # set nonoutlier values to 0, outliers to nonzero
    for i in data:
        if i <= bound:
            outlier.append(0)
        else:
            outlier.append(i)
    # find outlier indices
    outlier_indices = np.nonzero(outlier)
    return outlier_indices
