
import numpy as np
import matplotlib.pyplot as plt

for i in range(1,17):    
    beta = np.loadtxt('../../results/sub0'+str(i).zfill(2)+'_beta.txt')
    beta1 = np.reshape(beta.T,(64,64,34,-1))
    beta_gain = beta1[..., 0]
    beta_loss = beta1[..., 1]
    betagainmax=np.max(beta_gain)
    betalossmax=np.max(beta_loss)
    betagainmin=np.min(beta_gain)
    betalossmin=np.min(beta_loss)
    betagainmax=max(betagainmax,abs(betagainmin))
    betagainmin=-max(betagainmax,abs(betagainmin))
    betalossmax=max(betalossmax,abs(betalossmin))
    betalossmin=-max(betalossmax,abs(betalossmin))
    beta_gain[beta_gain==0] = np.nan
    beta_loss[beta_loss==0] = np.nan
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        img=axis.imshow(beta_gain[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=betagainmin, vmax=betagainmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('beta_gain_sub'+str(i)+'.png', dpi=40) 
    plt.close()
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        img=axis.imshow(beta_loss[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=betalossmin, vmax=betalossmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('beta_loss_sub'+str(i)+'.png', dpi=40) 
    plt.close()


for i in range(1,17):
    t_val = np.loadtxt('../../results/sub0'+str(i).zfill(2)+'_tvals.txt')
    #reshape t
    t_val1 = np.reshape(t_val.T,(64,64,34,-1))
    t_gain = t_val1[..., 0]
    t_loss = t_val1[..., 1]
    tgainmax=np.max(t_gain[~np.isnan(t_gain)])
    tgainmin=np.min(t_gain[~np.isnan(t_gain)])
    tlossmax=np.max(t_loss[~np.isnan(t_loss)])
    tlossmin=np.min(t_loss[~np.isnan(t_loss)])
    tgainmax=max(tgainmax,abs(tgainmin))
    tgainmin=-max(tgainmax,abs(tgainmin))
    tlossmax=max(tlossmax,abs(tlossmin))
    tlossmin=-max(tlossmax,abs(tlossmin))
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        img=axis.imshow(t_gain[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=tgainmin, vmax=tgainmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('t_gain_sub'+str(i)+'.png', dpi=40) 
    plt.close()
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        img=axis.imshow(t_loss[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=tlossmin, vmax=tlossmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('t_loss_sub'+str(i)+'.png', dpi=40) 
    plt.close()


