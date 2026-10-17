import numpy as np, itertools
from bloch import *
from scipy.optimize import minimize
F=dict(square=1,triangle=0,plaquette=1,tube=1); u=solve(F)
pts={'Gamma':(0,0,0),'X':(np.pi,0,0),'M':(np.pi,np.pi,0),'R':(np.pi,np.pi,np.pi)}
N=12
ks=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,N,endpoint=False),repeat=3)))
for t2 in (0.1,-0.1,0.3,-0.3):
    p=(-1.0,t2,-0.5)
    ev=lambda k: np.linalg.eigvalsh(bloch(u,np.array(k),*p,TRI))
    hs={n:np.round(ev(k)[:3],4) for n,k in pts.items()}
    e=np.array([ev(k)[0] for k in ks]); k0=ks[np.argmin(e)]
    r=minimize(lambda k: ev(k)[0],k0,method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-12,maxiter=5000))
    kmin=np.mod(r.x+np.pi,2*np.pi)-np.pi
    w=ev(r.x)
    print(f't2={t2:+}: lowest 3 levels at', hs, '| band minimum E=%.5f at k=%s, deg=%d'%(r.fun,np.round(kmin,3),int(np.sum(np.abs(w-w[0])<1e-6))))
