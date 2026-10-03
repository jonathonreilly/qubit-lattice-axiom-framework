"""Formation + crowd-tilted moves together (2D 128^2, 2000 ticks, rho0=0.1, p=0.01).
Reports h(t), fraction of records with all 4 neighbours recorded, event rate (moves+formations) per site,
and the event rate split by 8x8 block density (dense blocks >= 0.9 vs the rest), plus hole moves per hole."""
import sys, numpy as np
from t1lib import tick, neighbour_count
rule=sys.argv[1]; g=float(sys.argv[2]); L=128; T=2000; p=0.01
rng=np.random.default_rng(5); occ=rng.random((L,L))<0.1; expg=np.exp(g*np.arange(5))
for t in range(1,T+1):
    prev=occ
    occ,out,form=tick(occ,g,rule,rng,dict(p=p,k=1),moves=True,expg=expg)
    if t in (100,500,1000,2000):
        ev=(out.astype(int)+form.astype(int))
        blk=prev.reshape(16,8,16,8).mean(axis=(1,3)); dense=np.repeat(np.repeat(blk>=0.9,8,0),8,1)
        nr=neighbour_count(occ); full=(nr[occ]==4).mean()
        h=1-occ.mean()
        ed=ev[dense].mean() if dense.any() else np.nan; eo=ev[~dense].mean() if (~dense).any() else np.nan
        hd=(~prev)[dense].mean() if dense.any() else np.nan
        print(f"{rule} g={g} t={t}: h={h:.4f} full-surrounded recs={full:.3f} events/site={ev.mean():.4f} "
              f"| dense blocks: frac={dense.mean():.3f} holes={hd:.4f} events={ed:.4f} (events/hole={ed/max(hd,1e-9):.2f}) | other blocks events={eo:.4f}",flush=True)
