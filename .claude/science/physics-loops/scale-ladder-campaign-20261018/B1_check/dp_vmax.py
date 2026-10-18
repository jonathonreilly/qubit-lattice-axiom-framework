import numpy as np
from scipy.optimize import minimize
s3=np.sqrt(3)
def om(k):
    c,s=np.cos(k/s3),np.sin(k/s3); return np.arccos(np.clip(c.prod()-s.prod(),-1,1))
def g(k,h=1e-7): return np.array([(om(k+h*e)-om(k-h*e))/(2*h) for e in np.eye(3)])
rng=np.random.default_rng(1); best=(0,None)
for k0 in rng.uniform(-np.pi*s3,np.pi*s3,(400,3)):
    r=minimize(lambda k:-np.linalg.norm(g(k)),k0,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-12,maxiter=4000))
    if -r.fun>best[0] and np.isfinite(r.fun): best=(-r.fun,r.x)
print("sup |v| ~", best[0], "at k/sqrt3 =", best[1]/s3, " 1/sqrt2 =",1/np.sqrt(2), "v=",g(best[1]))
