"""Bracket the coexistence vapour density: slab jam + gas started EMPTY (from below) or SEEDED at 2e^{-zg/2} (from above).
usage: python3 toy3_slab2.py D g1,... T ; prints gas-core density averaged over 5 time windows for both starts,
plus monomer fraction of gas records (records with no recorded neighbour) and slab-core hole density."""
import sys, time, numpy as np
from t1lib import move_phase, neighbour_count
D=int(sys.argv[1]); gs=[float(v) for v in sys.argv[2].split(",")]; T=int(sys.argv[3])
shape=(64,64) if D==2 else (32,20,20); L0=shape[0]; z=2*D; lo,hi=L0//4,3*L0//4
x=np.arange(L0); gas=(x<lo-6)|(x>=hi+6); core=(x>=lo+6)&(x<hi-6)
ax=tuple(range(1,D))
for g in gs:
    res={}
    for start in ("empty","seeded"):
        rng=np.random.default_rng(int(100*g)+(0 if start=="empty" else 1)); guess=np.exp(-z*g/2)
        occ=np.zeros(shape,bool) if start=="empty" else rng.random(shape)<min(0.3,2*guess)
        sl=[slice(None)]*D; sl[0]=slice(lo,hi); occ[tuple(sl)]=True
        expg=np.exp(g*np.arange(z+1)); w=T//5; win=[[] for _ in range(5)]; mono=[]; hl=[]
        for t in range(1,T+1):
            occ,mv,arr,ww=move_phase(occ,g,rng,expg)
            if t%10==0:
                col=occ.mean(axis=ax); win[min((t-1)//w,4)].append(col[gas].mean())
                if t>T//2:
                    nr=neighbour_count(occ); gm=occ.copy(); gm[~gas]=False
                    mono.append((gm&(nr==0)).sum()/max(gm.sum(),1)); hl.append(1-col[core].mean())
        res[start]=([np.mean(v) for v in win],np.mean(mono),np.mean(hl))
    e,s=res["empty"],res["seeded"]
    print(f"D={D} g={g:4.2f} e^(-zg/2)={np.exp(-z*g/2):.5f} e^(-(z-1)g)={np.exp(-(z-1)*g):.5f} | from below: "+" ".join(f"{v:.5f}" for v in e[0])+
          " | from above: "+" ".join(f"{v:.5f}" for v in s[0])+f" | monomer frac {e[1]:.2f}/{s[1]:.2f} | slab holes {e[2]:.5f}/{s[2]:.5f}",flush=True)
