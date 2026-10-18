import itertools, numpy as np
exec(open('clean.py').read().split("rng=np.random.default_rng(7)")[0].replace("+0.13","+0.13"))
from scipy.optimize import minimize
grids=[np.array(list(itertools.product(np.linspace(-np.pi,np.pi,12,endpoint=False),repeat=3)))+off for off in (0.05,0.19)]
Tgs=[stack(g) for g in grids]
def J2(p, verbose=False):
    c=coeffs(p); HK=np.tensordot(c,Tk,1); EN=np.linalg.eigvalsh(HK)[0]
    vs=[(np.linalg.eigvalsh(np.tensordot(c,T,1))[1]-np.linalg.eigvalsh(np.tensordot(c,T,1))[0])/2e-4 for T in Td]; v=np.mean(vs)
    pen=0; stats=[]
    for T in Tgs:
        e=np.linalg.eigvalsh(np.tensordot(T,c,axes=([1],[0])))
        pen+=np.sum(np.maximum(0,e[:,0]-EN+0.02)**2)+np.sum(np.maximum(0,EN+0.02-e[:,1])**2)+np.sum(np.maximum(0,EN-e[:,2]+0.05)**2)
        stats.append(((e[:,0]-EN).max(),(e[:,1]-EN).min()))
    pen+=10*max(0,0.05-v)**2+1e-3*np.sum(np.maximum(0,np.abs(p)-1.0)**2)
    if verbose: print('v %.4f grid stats'%v, np.round(stats,4))
    return pen
p0=np.load('clean_params_v1.npy')
r=minimize(J2,p0,method='L-BFGS-B',options=dict(maxiter=200))
print('J2=%.3e'%r.fun); J2(r.x,True); np.save('clean_params.npy',r.x)
