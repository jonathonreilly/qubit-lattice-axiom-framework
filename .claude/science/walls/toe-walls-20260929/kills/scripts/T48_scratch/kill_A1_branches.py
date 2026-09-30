"""Enumerate the exact sector-blind-seed solutions (A1) by multi-start, using the attacker's own dressed_U machinery
(so it is the same model), and report the full spread of |R23|/|R12|, |R13|/|R12| among exact solutions with all |R_ij|<=1.6."""
import numpy as np, sys, json
from scipy.optimize import least_squares
from common import *
from testA_lib import observables
rng=np.random.default_rng(21)
out={}
for sname in ("MZ","LOW"):
  for p in (1.0,0.5):
    tu=np.array(MASSES[sname]["u"])**p; td=np.array(MASSES[sname]["d"])**p
    def f(x):
        o=observables(seed(*x),tu,td)
        if o is None: return np.ones(4)*8
        return np.clip(np.array([np.log(o["Vus"]/OBS["Vus"]),np.log(o["Vcb"]/OBS["Vcb"]),np.log(o["Vub"]/OBS["Vub"]),np.log(max(o["J"],1e-30)/OBS["J"])]),-8,8)
    sols=[]
    for t in range(700):
        x0=[rng.uniform(0.02,1.4),rng.uniform(0.02,1.4),rng.uniform(0.0,1.4),rng.uniform(0,2*np.pi)]
        try: s=least_squares(f,x0,bounds=([0,0,0,-2*np.pi],[1.6,1.6,1.6,4*np.pi]),xtol=1e-13,ftol=1e-13,max_nfev=120)
        except Exception: continue
        if np.max(np.abs(s.fun))<1e-8:
            x=s.x; sols.append([x[0],x[1],x[2],x[3]%(2*np.pi)])
    sols=np.array(sols)
    if len(sols)==0: print(sname,p,"none"); continue
    # unique
    u=np.unique(np.round(sols[:,:3],4),axis=0)
    r23=u[:,1]/u[:,0]; r13=u[:,2]/u[:,0]
    inwin=[(a,b) for a,b in zip(r23,r13) if 0.75<=a<=1.33 and 0.75<=b<=1.33]
    print(f"{sname} p={p}: {len(sols)} converged, {len(u)} distinct exact seeds (|R|<=1.6). r23/r12 range [{r23.min():.3f},{r23.max():.3f}]; r13/r12 range [{r13.min():.3f},{r13.max():.3f}]; in circulant window [0.75,1.33]^2: {len(inwin)}",flush=True)
    # equal-magnitude test: max/min of (r12,r23,r13)
    spread=u.max(axis=1)/np.maximum(u.min(axis=1),1e-9)
    k=np.argmin(spread)
    print(f"     most circulant-like exact seed: |R|=({u[k,0]:.3f},{u[k,1]:.3f},{u[k,2]:.3f}) max/min={spread[k]:.2f}",flush=True)
    out[f"{sname}_p{p}"]=u.tolist()
json.dump(out,open("kill_A1_branches.json","w"))
