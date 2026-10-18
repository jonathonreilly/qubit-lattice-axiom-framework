import itertools, numpy as np
from diraclib import *
from scipy.optimize import minimize
Xb2=np.load('Xbasis2.npy'); Rb2=np.load('Rbasis2.npy')
ops=[H0(-1.0,0.0), H0(0.0,1.0)]+list(Rb2)+list(Xb2)
nR=len(Rb2); nX=len(Xb2)
blks=[blocks_from(o) for o in ops]
def stack(ks):
    return np.array([[Hk(b,k) for b in blks] for k in ks])   # (nk, nops, 12,12)
g=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,8,endpoint=False),repeat=3)))+0.13
Tg=stack(g); Tk=stack([kst])[0]
dirs=np.random.default_rng(1).normal(size=(3,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
Td=stack([kst+1e-4*d for d in dirs])
def coeffs(p):   # p: [t2, a(nR), b(nX)]; t1 fixed to 1 (op 0)
    return np.concatenate([[1.0],p])
def J(p, verbose=False):
    c=coeffs(p)
    HK=np.tensordot(c,Tk,1); EN=np.linalg.eigvalsh(HK)[0]
    H=np.tensordot(Tg,c,axes=([1],[0])); e=np.linalg.eigvalsh(H)
    vs=[(np.linalg.eigvalsh(np.tensordot(c,T,1))[1]-np.linalg.eigvalsh(np.tensordot(c,T,1))[0])/2e-4 for T in Td]
    v=np.mean(vs)
    pen=np.sum(np.maximum(0,e[:,0]-EN+0.01)**2)+np.sum(np.maximum(0,EN+0.01-e[:,1])**2)
    pen+=np.sum(np.maximum(0,EN-e[:,2]+0.05)**2)          # keep the pair separated from higher bands
    pen+=10*max(0,0.03-v)**2 + 1e-3*np.sum(np.maximum(0,np.abs(p)-1.0)**2)
    if verbose: print('EN %.4f v %.4f max e0-EN %.4f min e1-EN %.4f min e2-EN %.4f'%(EN,v,(e[:,0]-EN).max(),(e[:,1]-EN).min(),(e[:,2]-EN).min()))
    return pen
rng=np.random.default_rng(7); best=None
for trial in range(6):
    p0=np.concatenate([[rng.uniform(0.05,0.3)], 0.05*rng.normal(size=nR), 0.1*rng.normal(size=nX)])
    r=minimize(J,p0,method='L-BFGS-B',options=dict(maxiter=300))
    print(trial,'J=%.3e'%r.fun,flush=True); J(r.x,True)
    if best is None or r.fun<best.fun: best=r
np.save('clean_params.npy',best.x)
