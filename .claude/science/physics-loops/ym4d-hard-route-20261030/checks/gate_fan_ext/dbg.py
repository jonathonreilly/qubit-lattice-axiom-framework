import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
import t2_opt_extension as t
L=8
n,a,om,E,par=t.build(L,"flat")
N=n**3;d=3;w0,w1=a**d,a**(d-2)
A=(w0*sp.identity(N)+w1*t.lap(N,E)).tocsr()
both=om[E[:,0]]&om[E[:,1]]
G=(w0*sp.diags(om.astype(float))+w1*t.lap(N,E,both)).tocsr()
print("edges",len(E),"both",both.sum())
# reflection test on random zero parent mean u
rng=np.random.default_rng(1)
idx=np.arange(N).reshape(n,n,n)
refl=idx[:,:,::-1].ravel()
u=np.zeros(N); iO=np.where(om)[0]; u[iO]=rng.standard_normal(len(iO))
for p in np.unique(par[iO]):
    m=(par==p); u[m]-=u[m].mean()
w=u+u[refl]
print("om symmetric?",np.all(om[refl]==~om))
print("E(w)/E_Om(u)",w@(A@w)/(u@(G@u)))
# check the top row of idx layout: which axis is z
print("z axis check", om.reshape(n,n,n)[0,0,:n].astype(int)[:n//2+2], om.reshape(n,n,n)[:,0,0].astype(int)[:4])
print("par layout", par.reshape(n,n,n)[0,0,[0,7,8,15]], par.reshape(n,n,n)[[0,7,8,15],0,0])
