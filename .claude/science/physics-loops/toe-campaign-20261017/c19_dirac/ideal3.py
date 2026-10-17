import itertools, numpy as np
from diraclib import *
from scipy.optimize import minimize
exec(open('ideal2.py').read().split("rng=np.random.default_rng(1)")[0].replace("from diraclib import *","").replace("from scipy.optimize import minimize",""))
g14=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,14,endpoint=False),repeat=3)))
g24=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,24,endpoint=False),repeat=3)))
def obj(p):
    t2,c=norm(p)
    if np.linalg.norm(c)>3: return 1+np.linalg.norm(c)
    return excess(p,g14)
rng=np.random.default_rng(4); res=[]
for trial in range(8):
    p0=np.concatenate([[rng.uniform(0,0.3)], rng.normal(size=len(Xb))])
    r=minimize(obj,p0,method='Nelder-Mead',options=dict(maxiter=500,xatol=1e-6,fatol=1e-8))
    t2,c=norm(r.x); e24=excess(r.x,g24)
    print(trial,'excess14 %.5f excess24 %.5f t2 %.3f |coef| %.3f'%(r.fun,e24,t2,np.linalg.norm(c)),flush=True)
    res.append((e24,r.x))
res.sort(key=lambda x:x[0]); np.save('ideal3_params.npy',res[0][1]); print('best excess on 24^3 grid: %.5f'%res[0][0])
