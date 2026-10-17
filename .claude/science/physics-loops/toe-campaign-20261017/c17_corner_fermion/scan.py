import numpy as np, itertools
from bloch import *
from scipy.optimize import minimize
N=16
ks=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,N,endpoint=False),repeat=3)))
G0=np.zeros(3); RR=np.array([np.pi]*3)
def lowest(u,k,p): return np.linalg.eigvalsh(bloch(u,k,*p,TRI))
res=[]
for tri,tube in itertools.product((0,1),(0,1)):
    F=dict(square=1,triangle=tri,plaquette=1,tube=tube); u=solve(F)
    for t1 in (1,-1):
        for t2 in np.linspace(-1.5,1.5,7):
            for lam in np.linspace(-1,1,9):
                p=(t1,t2,lam)
                e=np.array([lowest(u,k,p)[0] for k in ks])
                i=np.argmin(e); k0=ks[i]
                r=minimize(lambda k: lowest(u,k,p)[0], k0, method='Nelder-Mead',options=dict(xatol=1e-6,fatol=1e-10,maxiter=4000))
                emin=r.fun
                best=None
                for name,kk in (('Gamma',G0),('R',RR)):
                    ev=lowest(u,kk,p)
                    if abs(ev[0]-emin)<1e-6:
                        deg=int(np.sum(np.abs(ev-ev[0])<1e-7)); best=(name,deg,ev[deg]-ev[0])
                res.append((tri,tube,t1,round(t2,2),round(lam,2),best, round(emin,4)))
good=[r for r in res if r[5] is not None and r[5][1]==2]
print(len(res),'parameter points;', len(good),'with band minimum at Gamma or R and 2-fold')
for r in good[:40]: print(r)
