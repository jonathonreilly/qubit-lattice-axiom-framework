"""3D thinning check: rule 'needs >=1 empty neighbour' (kempty) and 'stirB', unbiased moves, 40^3 periodic, 1500 ticks."""
import sys, time
import numpy as np
from t1lib import tick
rule=sys.argv[1]; L=40; T=1500; p=0.05
rng=np.random.default_rng(7); occ=rng.random((L,L,L))<0.2
h=[1-occ.mean()]; E=[]; t0=time.time()
expg=np.ones(7)
last=np.full(occ.shape,-1,np.int32)
for t in range(T):
    occ,out,form=tick(occ,0.0,rule,rng,dict(p=p,k=1),moves=True,expg=expg)
    ev=out|form; last[ev]=t
    E.append((out.sum()+form.sum())/occ.size); h.append(1-occ.mean())
h=np.array(h); E=np.array(E)
tt=np.arange(len(h))
for a,b in [(100,400),(400,1500)]:
    s=np.polyfit(np.log(tt[a:b+1]),np.log(h[a:b+1]),1)[0]
    print(f"{rule} 3D: loglog slope of h over t in [{a},{b}] = {s:.3f}")
print(f"{rule} 3D: h(t) at 100,400,1000,1500 = {h[100]:.5f} {h[400]:.5f} {h[1000]:.5f} {h[1500]:.5f}; t*h(t) = {100*h[100]:.3f} {400*h[400]:.3f} {1000*h[1000]:.3f} {1500*h[1500]:.3f}")
print(f"{rule} 3D: E(t)/h(t) at 1500 = {E[-1]/h[-1]:.3f}; frac sites with an event in last 500 ticks = {(last>=T-500).mean():.3f}; time {time.time()-t0:.1f}s")
