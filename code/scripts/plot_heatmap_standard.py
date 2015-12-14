"""
This script will plot the heatmap for the beta_gain,beta_loss,t_gain and t_loss
for all the subjects for standard brain data.
"""
import numpy as np
import matplotlib.pyplot as plt

base = nib.load('../../data/templates/mni_standard.nii')
base = base.get_data()
for i in range(1,17):    
    beta = np.loadtxt('../../results/texts/sub0'+str(i).zfill(2)+'standard_beta.txt')
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
        plt.imshow(base[:, :, subject], cmap = plt.get_cmap('gray'), alpha = 0.3)
        img=axis.imshow(beta_gain[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=betagainmin, vmax=betagainmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('../../results/figures/beta_gain_sub'+str(i)+'.png', dpi=40) 
    plt.close()
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        plt.imshow(base[:, :, subject], cmap = plt.get_cmap('gray'), alpha = 0.3)
        img=axis.imshow(beta_loss[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=betalossmin, vmax=betalossmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('../../results/figures/beta_loss_sub'+str(i)+'.png', dpi=40) 
    plt.close()



for i in range(1,17):
    t_val = np.loadtxt('../../results/texts/sub0'+str(i).zfill(2)+'_tvals.txt')
    #reshape t
    t1=np.asarray(t_val[0])
    t2=np.asarray(t_val[1])
    t1=np.reshape(t1,(91, 109, 91))
    t2=np.reshape(t2,(91, 109, 91))
    t1=t1[:,:,31:65]
    t2=t2[:,:,31:65]
    t1[t1==0]=float('nan')
    t2[t2==0]=float('nan')
    t1max=np.max(t1[np.isnan(t1)==False])
    t2max=np.max(t2[np.isnan(t2)==False])
    t1min=np.min(t1[np.isnan(t1)==False])
    t2min=np.min(t2[np.isnan(t2)==False])
    a=np.asarray((t1max,abs(t1min)))
    b=np.asarray((t2max,abs(t2min)))
    t1max=np.max(a)
    t1min=-np.max(a)
    t2max=np.max(b)
    t2min=-np.max(b)
    plot_number=1
    plot_number2=1
    t_gain=t1
    t_loss=t2
    t_gain[abs(t_gain)<=2.3]=np.nan
    t_loss[abs(t_loss)<=2.3]=np.nan
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        plt.imshow(base[:, :, subject], cmap = plt.get_cmap('gray'), alpha = 0.3)
        img=axis.imshow(t_gain[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=t_gainmin, vmax=t_gainmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('../../results/figures/t_gain_sub'+str(i)+'.png', dpi=40) 
    plt.close()
    
    fig = plt.figure(figsize = (54.2, 28.4))
    for plot_number in range(2, 32):
        axis = fig.add_subplot(5, 6, plot_number-1)
        img=axis.imshow(t_loss[:, :, plot_number], cmap=plt.get_cmap('rainbow'), alpha=0.5,interpolation='nearest',vmin=tlossmin, vmax=tlossmax)
        plt.colorbar(img, ax=axis)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title('Slice ' + str(plot_number))
    plt.savefig('../../results/figures/t_loss_sub'+str(i)+'.png', dpi=40) 
    plt.close()


