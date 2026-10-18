import sys, numpy as np, random
sys.path.insert(0,'.')
from driver import Sim
import qmc
T=0.3
sim=Sim(2,0.0,T,seed=9,cap=64); sim.pr=np.array([0.,0.,0.,1.0])
lat=sim.lat
nbs=[set(lat.nbh[p,:lat.nnb[p]].tolist()) for p in range(lat.np)]
def flippable(s,p): return abs((s[lat.plinks[p]]*lat.psign).sum())==4
for trial in range(4):
    for i in range(50): sim.do_sweep()
    kinks=sorted((sim.kt[p,i],p) for p in range(lat.np) for i in range(sim.kc[p]))
    n0=len(kinks)
    # python exact probabilities of +1 / -1 for one move
    pplus=0; pminus=0
    for p in range(lat.np):
        first=[(t,q) for (t,q) in kinks if q in nbs[p]]
        tf=first[0][0] if first else T
        if flippable(sim.s0,p): pplus+=0.5*min(1,tf)/lat.np
        if first and first[0][1]==p:
            tf2=first[1][0] if len(first)>1 else T
            pminus+=0.5*min(1,1/tf2)/lat.np
    cp=cm=0; N=200000
    for i in range(N):
        s0=sim.s0.copy(); kt=sim.kt.copy(); kc=sim.kc.copy(); st=np.zeros(10,dtype=np.int64)
        qmc.sweep(s0,kt,kc,*sim.args,1.0,0.0,T,0,1,sim.buf,st,sim.pr)
        d=kc.sum()-n0
        cp+=d==1; cm+=d==-1
    print(f"n={n0}: P(+1) python {pplus:.4f} numba {cp/N:.4f} | P(-1) python {pminus:.4f} numba {cm/N:.4f}")
