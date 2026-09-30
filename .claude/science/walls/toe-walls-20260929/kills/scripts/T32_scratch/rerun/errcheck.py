import numpy as np, sys
sys.path.insert(0,'.')
from analyze import jack
def sqrt_sigma(fn, lev, Tp, rmax_used=None, luscher=False):
    d=np.load(fn); Ws=d['Ws']; dims=d['dims']
    Rmax=Ws.shape[2]-1
    Rlist=list(range(1,min(Rmax,dims[0]//2)+1))
    if rmax_used: Rlist=[R for R in Rlist if R<=rmax_used]
    def f(m):
        V=np.array([np.log(m[R,Tp]/m[R,Tp+1]) for R in Rlist]); F=V[1:]-V[:-1]; r=np.array(Rlist[:-1])+0.5
        if luscher:
            s=F-(np.pi/12)/r**2
            return np.array([np.sqrt(abs(s[-1])), np.sqrt(abs(s[-2]))])
        A=np.vstack([np.ones_like(r),1/r**2]).T
        sol=np.linalg.lstsq(A,F,rcond=None)[0]
        return np.array([np.sqrt(abs(sol[0])),sol[0]])
    for nb in (6,10,20):
        v,e,_=jack(Ws[:,lev],f,nb)
        print("  %s lev%d T%d->%d Rmax=%s luscher=%s nb=%2d : %s +- %s" % (fn.split('/')[-1],lev,Tp,Tp+1,rmax_used,luscher,nb,np.round(v,4),np.round(e,4)))
for fn in ("runs/L10_b6.npz","runs/L8_b6.npz"):
    d=np.load(fn); T=d['Ws'].shape[3]-1
    for lev in (0,1):
        for Tp in range(2,T-0):
            if Tp+1>T: continue
            sqrt_sigma(fn,lev,Tp)
# plaquette autocorrelation
for fn in ("runs/L10_b6.npz","runs/L8_b6.npz"):
    p=np.load(fn)['plaq']; p=p-p.mean(); n=len(p)
    ac=[np.dot(p[:n-k],p[k:])/np.dot(p,p) for k in range(1,6)]
    print(fn,"plaq autocorr lags1-5:",np.round(ac,2),"n=",n)
print("Luscher-term (pi/12) fixed:")
sqrt_sigma("runs/L10_b6.npz",1,4,luscher=True)
sqrt_sigma("runs/L10_b6.npz",0,4,luscher=True)
print("Fit with R<=4 only (r<=3.5), 10^4:")
sqrt_sigma("runs/L10_b6.npz",1,4,rmax_used=4)
