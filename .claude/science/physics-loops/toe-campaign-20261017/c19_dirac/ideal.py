import itertools, numpy as np
from diraclib import *
from scipy.optimize import minimize
blX=[blocks_from(x) for x in Xb]
grid=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,10,endpoint=False),repeat=3)))
blH1=blocks_from(H0(-1.0,0.0)); blH2=blocks_from(H0(0.0,1.0))
def Hk_comb(k,t2,coef):
    H=Hk(blH1,k)+t2*Hk(blH2,k)
    for c,b in zip(coef,blX): H=H+c*Hk(b,k)
    return H
def excess(p, g=grid):
    t2=p[0]; coef=p[1:]
    EN=np.linalg.eigvalsh(Hk_comb(kst,t2,coef))[0]
    e=np.array([np.linalg.eigvalsh(Hk_comb(k,t2,coef))[:2] for k in g])
    return max(0,e[:,0].max()-EN)+max(0,EN-e[:,1].min())
rng=np.random.default_rng(0)
best=None
for trial in range(12):
    p0=np.concatenate([[rng.uniform(0.05,0.4)], rng.normal(size=len(Xb))*0.08])
    r=minimize(excess,p0,method='Nelder-Mead',options=dict(maxiter=600,xatol=1e-5,fatol=1e-7))
    print(trial, 'excess %.5f'%r.fun, 't2 %.3f'%r.x[0])
    if best is None or r.fun<best.fun: best=r
np.save('ideal_params.npy',best.x)
fine=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,24,endpoint=False),repeat=3)))
print('best excess on a 10^3 grid %.6f; on a 24^3 grid %.6f'%(best.fun, excess(best.x,fine)))
