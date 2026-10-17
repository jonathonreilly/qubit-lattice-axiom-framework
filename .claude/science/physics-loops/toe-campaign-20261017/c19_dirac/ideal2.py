import itertools, numpy as np
from diraclib import *
from scipy.optimize import minimize
exec(open('ideal.py').read().split("def excess")[0].replace("from diraclib import *","").replace("from scipy.optimize import minimize",""))
rngd=np.random.default_rng(9); DIRS3=rngd.normal(size=(4,3)); DIRS3/=np.linalg.norm(DIRS3,axis=1)[:,None]
def vel(t2,coef):
    vs=[]
    for d in DIRS3:
        e=np.linalg.eigvalsh(Hk_comb(kst+1e-4*d,t2,coef)); vs.append((e[1]-e[0])/2e-4)
    return np.mean(vs)
V0=0.05
def norm(p):
    t2=0.05+abs(p[0]); c=p[1:]; v=vel(t2,c)
    return t2, c*(V0/v) if v>1e-9 else c
def excess(p,g=grid):
    t2,c=norm(p)
    EN=np.linalg.eigvalsh(Hk_comb(kst,t2,c))[0]
    e=np.array([np.linalg.eigvalsh(Hk_comb(k,t2,c))[:2] for k in g])
    return max(0,e[:,0].max()-EN)+max(0,EN-e[:,1].min())
rng=np.random.default_rng(1); best=None
for trial in range(10):
    p0=np.concatenate([[rng.uniform(0,0.3)], rng.normal(size=len(Xb))])
    r=minimize(excess,p0,method='Nelder-Mead',options=dict(maxiter=800,xatol=1e-6,fatol=1e-8))
    t2,c=norm(r.x)
    print(trial,'excess %.6f t2 %.3f |coef| %.3f'%(r.fun,t2,np.linalg.norm(c)),flush=True)
    if best is None or r.fun<best.fun: best=r
t2,c=norm(best.x); np.save('ideal2_params.npy',np.concatenate([[t2],c]))
fine=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,24,endpoint=False),repeat=3)))
print('best: t2 %.4f, velocity %.4f, excess 10^3 grid %.6f, 24^3 grid %.6f'%(t2,vel(t2,c),best.fun,excess(best.x,fine)))
