import numpy as np, time
from scipy.special import j0
from e1p_core import sprinkle2d_diamond, chain_sums_2d
from E1p_4_massive2d import exact_W
rng=np.random.default_rng(3)
U=30.0; tau=np.sqrt(2)*U
mT=np.array([0.,1,2,4,8,16]); m=mT/tau
Ks=[]
t0=time.time()
for r in range(400):
    u,v=sprinkle2d_diamond(U,rng)
    K,KJ=chain_sums_2d(u,v,U,np.zeros(len(u)),np.full(len(m),0.5),-m**2)
    Ks.append(K)
Ks=np.array(Ks); print("time",time.time()-t0)
for k in range(len(m)):
    mu=Ks[:,k].mean(); sd=Ks[:,k].std(ddof=1)
    if m[k]>0:
        taus,S,W,it=exact_W(m[k],1.0,tau*1.0001,ntau=300,nq=60)
        V=np.interp(tau,taus,W-S)
    else: V=0
    print(f"mT={mT[k]:5.1f} mean={mu:.5f} cont={0.5*j0(mT[k]):.5f} (se {sd/20:.5f})  sd={sd:.5f}  exact sd={np.sqrt(V):.5f}")
