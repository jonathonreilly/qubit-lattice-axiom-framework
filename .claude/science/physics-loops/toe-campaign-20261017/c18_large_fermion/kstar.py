import numpy as np, itertools
from bloch import *
from scipy.optimize import minimize
rng=np.random.default_rng(1)
for tri in (0,1):
  F=dict(square=1,triangle=tri,plaquette=1,tube=1); u=solve(F)
  t1=-1.0 if tri==0 else 1.0
  for t2,lam in ((0.1,-0.5),(-0.1,-0.5),(0.3,-0.5),(0.1,0.5)):
    p=(t1,t2,lam); ev=lambda k: np.linalg.eigvalsh(bloch(u,np.asarray(k,float),*p,TRI))
    # global search: dense grid + local refinements from the 10 best grid points
    N=20; ks=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,N,endpoint=False),repeat=3)))
    e=np.array([ev(k)[0] for k in ks]); best=ks[np.argsort(e)[:12]]
    res=[minimize(lambda k: ev(k)[0],k0,method='Nelder-Mead',options=dict(xatol=1e-9,fatol=1e-13,maxiter=8000)) for k0 in best]
    r=min(res,key=lambda r:r.fun); kmin=(r.x+np.pi)%(2*np.pi)-np.pi
    ks_=[np.array(s)*np.pi/2 for s in ((1,-1,1),(-1,1,-1))]
    eks=[ev(k) for k in ks_]
    which=int(np.argmin([x[0] for x in eks])); w=eks[which]
    deg=int(np.sum(np.abs(w-w[0])<1e-9))
    # Kramers: 2-fold degeneracy at random k
    kr=all(abs(ev(k)[0]-ev(k)[1])<1e-9 and abs(ev(k)[2]-ev(k)[3])<1e-9 for k in rng.uniform(-np.pi,np.pi,(20,3)))
    # Hessian of lowest band at k*
    k0=ks_[which]; h=1e-3; Hs=np.zeros((3,3))
    f=lambda k: ev(k)[0]
    for i in range(3):
        for j in range(3):
            ei=np.eye(3)[i]*h; ej=np.eye(3)[j]*h
            Hs[i,j]=(f(k0+ei+ej)-f(k0+ei-ej)-f(k0-ei+ej)+f(k0-ei-ej))/(4*h*h)
    hev=np.linalg.eigvalsh(Hs)
    # quartic anisotropy: compare E along [100] and [111] at |dk|=0.3
    dk=0.3; e100=f(k0+dk*np.array([1,0,0]))-w[0]; e111=f(k0+dk*np.ones(3)/np.sqrt(3))-w[0]
    print(f'tri={tri} t1={t1:+} t2={t2:+} chiral={lam:+}: global min E={r.fun:.6f} at k={np.round(kmin/(np.pi/2),4)}(pi/2);'
          f' E(k*)={w[0]:.6f} deg={deg} gap@k*={w[deg]-w[0]:.4f}; Kramers everywhere={kr};'
          f' Hessian eig={np.round(hev,4)}; E100/E111 at |dk|=0.3: {e100:.5f}/{e111:.5f}')
