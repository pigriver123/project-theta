from scipy import stats
import numpy as np
""" 
    Scripts to do the linear regression between behavial loss aversion and neaural loss aversion.

    """


Ynew=np.loadtxt('../../results/texts/lambda.txt')

betagain=list()
betaloss=list()
for i in range(1,17):
    u=np.loadtxt('../../results/texts/sub0'+str(i).zfill(2)+'_standard_beta.txt')
    ugain=u[0]
    betagain.append(ugain)
    uloss=u[1]
    betaloss.append(uloss)
betgain=np.zeros((len(betagain[0]),len(betagain)))
betloss=np.zeros((len(betaloss[0]),len(betaloss)))
betagain=np.asarray(betagain)
betaloss=np.asarray(betaloss)
for j in range(len(betgain)):
    betgain[j,]=betagain[:,j]
    betloss[j,]=betaloss[:,j]

betgainloss=np.zeros((len(betagain[0]),len(betagain)))
for j in range(len(betgain)):
    betgainloss[j,]=-betgain[j,]-betloss[j,]

slopegain=list()
slopeloss=list()
slopegainloss=list()
for j in range(len(betgain)):
    slopegain.append(stats.linregress(betgain[j,:],Ynew)[0])
    slopeloss.append(stats.linregress(betloss[j,:],Ynew)[0])
    slopegainloss.append(stats.linregress(betgainloss[j,:],Ynew)[0])

constantgain=list()
constantloss=list()
constantgainloss=list()
for j in range(len(betgain)):
    constantgain.append(stats.linregress(betgain[j,:],Ynew)[1])
    constantloss.append(stats.linregress(betloss[j,:],Ynew)[1])
    constantgainloss.append(stats.linregress(betgainloss[j,:],Ynew)[1])

R2gain=list()
R2loss=list()
R2gainloss=list()
for j in range(len(betgain)):
    R2gain.append(stats.linregress(betgain[j,:],Ynew)[2]**2)
    R2loss.append(stats.linregress(betloss[j,:],Ynew)[2]**2)
    R2gainloss.append(stats.linregress(betgainloss[j,:],Ynew)[2]**2)

pgain=list()
ploss=list()
pgainloss=list()
for j in range(len(betgain)):
    pgain.append(stats.linregress(betgain[j,:],Ynew)[3])
    ploss.append(stats.linregress(betloss[j,:],Ynew)[3])
    pgainloss.append(stats.linregress(betgainloss[j,:],Ynew)[3])

np.savetxt('../../results/texts/slopegain.txt',slopegain)
np.savetxt('../../results/texts/slopeloss.txt',slopeloss)
np.savetxt('../../results/texts/slopegainloss.txt',slopegainloss)
np.savetxt('../../results/texts/constantgain.txt',constantgain)
np.savetxt('../../results/texts/constantloss.txt',constantloss)
np.savetxt('../../results/texts/constantgainloss.txt',constantgainloss)
np.savetxt('../../results/texts/R2gain.txt',R2gain)
np.savetxt('../../results/texts/R2loss.txt',R2loss)
np.savetxt('../../results/texts/R2gainloss.txt',R2gainloss)
np.savetxt('../../results/texts/pgain.txt',pgain)
np.savetxt('../../results/texts/ploss.txt',ploss)
np.savetxt('../../results/texts/pgainloss.txt',pgainloss)





