
# find outliers based on DVARS and FD

def outlier(file_name, bound):
    # load data
    data = np.loadtxt(file_name)
    outlier = []
    # set outlier values to 0
    for i in data:
        if i <= bound:
            outlier.append(0)
        else:
            outlier.append(i)
    # find outlier indices
    outlier_indices = np.nonzero(outlier)
    return outlier_indices
