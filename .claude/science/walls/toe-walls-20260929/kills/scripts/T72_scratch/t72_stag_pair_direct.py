import numpy as np, scipy.linalg as la, sys, time
from t72_stag import *
from t72_stag_pairband import W_pair_band

def direct_pair(N, lam, beta, m, e0, timed, g=1e-3, Ecut=None):
    xs=np.arange(N); xc=(N-1)/2
    X=Xcm(N)
    Hfun=lambda gg: two_body(N,np.exp(gg*(xs-xc)),beta,m,e0,lam,timed)
    ev,V=la.eigh(Hfun(0.0).toarray())
    if Ecut is None: Ecut=2*e0+1.0*m
    Xd=X.diagonal().real
    cand=np.where(ev>Ecut)[0]
    idx=None
    for i in cand:
        p=V[:,i]; dens=np.abs(p)**2
        xm=np.sum(dens*Xd); xv=np.sum(dens*Xd**2)-xm**2
        if abs(xm-xc)<1.0 and xv>0.02*N*N:      # bulk n=1 COM standing wave (var ~ 0.033 N^2), not a wall-bound pair
            idx=i; break
    Wm=W_direct(Hfun,X,ev,V,idx,Ecut,g)
    return Wm, ev[idx], ev, V, idx

if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 40
    beta=1.0; m=1.0; e0=0.0
    print(f"# open chain N={N}, staggered walkers m=1, beta=1; pair with contact attraction; timed binding")
    print(" lam   E_stand   W_direct   W_band    ratio   |  UNTIMED binding: W_direct")
    for lam in (0.2,0.4,0.8,1.2):
        Wb=W_pair_band(60,lam,beta,m,e0)[0]
        Wd,E,*_ = direct_pair(N,lam,beta,m,e0,True)
        Wu,Eu,*_ = direct_pair(N,lam,beta,m,e0,False)
        print(f"{lam:4.1f}  {E:8.5f}  {Wd:8.5f}  {Wb:8.5f}  {Wd/Wb:7.4f}   | {Wu:8.5f}", flush=True)
