import numpy as np, time, sys
from lib import *
n,bonds=torus_bonds((4,4))
# free spinless pi-flux one-body
h1=np.zeros((16,16))
for a,b,j,t,c in bonds: h1[a,b]+=t; h1[b,a]+=t
ev1=np.linalg.eigvalsh(h1); print("one-body levels",np.round(ev1,6))
print("free spinless sea",ev1[ev1<-1e-12].sum(), " free (2 coins)",2*ev1[ev1<-1e-12].sum())
for N in range(1,16):
  for ferm in (True,False):
    Nup=N//2
    t0=time.time()
    H,codes=build_sector(n,bonds,N,Nup,ferm)
    dim=H.shape[0]
    if dim<2500:
        w=np.sort(np.linalg.eigvalsh(H.toarray()))[:6]
    else:
        w=np.sort(sla.eigsh(H,k=6,which='SA',tol=1e-10)[0])
    print(N,"F" if ferm else "B",dim,np.round(w[:4],8),round(time.time()-t0,1),flush=True)
