
def dvars(file_name, fig_name):
    data = np.loadtxt(file_name)
    bound = np.array([0.5]*(240))
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(111)
    plt.xlim(0,240)
    # plt.ylim(-0.05, 1.0)
    ax.plot(data)
    ax.plot(bound, 'g--')
    plt.ylabel('DVARS')
    plt.xlabel('timepoints')
    plt.title('DVARS (RMS Signal Derivative over brain mask)')
    plt.savefig(fig_name)

def fd(file_name, fig_name):
    data = np.loadtxt(file_name)
    bound = np.array([0.4]*(240))
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(111)
    plt.xlim(0,240)    
    plt.ylim(0, 0.6)
    ax.plot(data)
    ax.plot(bound, 'g--')
    plt.ylabel('FD')
    plt.xlabel('timepoints')
    plt.title('Framewise Displacement')
    plt.savefig(fig_name)

def mean(data):
    shape = data.shape
    mean_list = []
    for i in range(shape[3]):
        mean = np.mean(data[...,i])
        mean_list.append(mean)
    return np.asarray(mean_list)
	
def meanSig(file_name, fig_name):
    img = nib.load(file_name)
    data = img.get_data()
    x=list(range(240))
    y=mean(data)
    coefficients = np.polyfit(x, y, 2)
    polynomial = np.poly1d(coefficients)
    xs = np.arange(1, 240, 1)
    ys = polynomial(xs)
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(111)
    plt.xlim(0,240)
    # plt.ylim(300,400)
    ax.plot(x, y)
    ax.plot(xs, ys)
    plt.ylabel('Mean MR signal')
    plt.xlabel('timepoints')
    plt.title('Mean signal (unfiltered)')
    plt.savefig(fig_name)


