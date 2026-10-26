import numpy as np,time,sys
from sampler import *
def tau(D):
    Dc=D-D.mean(1,keepdims=True)
    n=D.shape[1]; f=np.fft.rfft(Dc,2*n,axis=1); ac=np.fft.irfft(np.abs(f)**2,axis=1)[:,:n].mean(0); rho=ac/ac[0]
    t=0.5
    for w in range(1,n):
        t=0.5+rho[1:w+1].sum()
        if w>=6*t: break
    return t,rho[:6]
for L,M,nk,b in [(4,1000,1000,100),(6,600,800,100)]:
    t0=time.time();r=run(L,M,nk,b,5);dt=time.time()-t0
    Kc=(2*r['N']+1)/(3*r['N']); D=Kc*(2*r['ser'][:,b:,1]-r['ser'][:,b:,0])
    cm=D.mean(1);tt,rho=tau(D)
    h=D.shape[1]//2
    print(L,M,"time",round(dt,1),"loops",M*(nk+b),"D",cm.mean(),"seedSE",cm.std(ddof=1)/np.sqrt(M),"naive",D.std()/np.sqrt(D.size),"tau",tt,rho.round(3),"first/second half",D[:,:h].mean(),D[:,h:].mean())
