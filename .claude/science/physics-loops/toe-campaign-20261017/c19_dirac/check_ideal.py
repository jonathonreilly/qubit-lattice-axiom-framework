import itertools, numpy as np
from diraclib import *
exec(open('ideal.py').read().split("rng=np.random.default_rng(0)")[0].replace("from diraclib import *",""))
p=np.load('ideal_params.npy'); t2=p[0]; coef=p[1:]
print('t2 =',t2,' |coef| =',np.round(np.linalg.norm(coef),4))
f=lambda k: Hk_comb(k,t2,coef)
EN=np.linalg.eigvalsh(f(kst))[0]
rng=np.random.default_rng(2)
dirs=rng.normal(size=(6,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
v=[(np.linalg.eigvalsh(f(kst+1e-3*d))[1]-np.linalg.eigvalsh(f(kst+1e-3*d))[0])/2e-3 for d in dirs]
print('Weyl velocity along 6 random directions:',np.round(v,5))
fine=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,30,endpoint=False),repeat=3)))
e=np.array([np.linalg.eigvalsh(f(k))[:3] for k in fine])
print('node %.6f band0 max %.6f band1 min %.6f band2 min %.6f'%(EN,e[:,0].max(),e[:,1].min(),e[:,2].min()))
# overall bandwidth scale: how flat is the pair?
print('band0 width %.4f, band1 width %.4f'%(np.ptp(e[:,0]),np.ptp(e[:,1])))
