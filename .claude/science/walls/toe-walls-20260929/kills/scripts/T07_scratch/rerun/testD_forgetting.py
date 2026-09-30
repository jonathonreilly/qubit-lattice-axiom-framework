"""Test D: does the law forget its start? Lower bound on the Dobrushin coefficient of K_{0->8}
from point-mass starts on a 5x5 grid of (xA, xB) around the packet, setting (0, pi/4)."""
import numpy as np, itertools, time
from common import *
L=24; ring=Ring(L); m=Bell2(L,0.0,np.pi/4,ring)
P0=m.P(0.0); P8=m.P(8.0)
pts=[(a,b) for a in (8,10,12,14,16) for b in (8,10,12,14,16)]
cols={}
t0=time.time()
for (a,b) in pts:
    r0=np.zeros((L,L)); r0[a,b]=1.0
    cols[(a,b)]=m.evolve(r0,np.array([0.,8.]))[-1]
print('time',time.time()-t0)
best=0; arg=None; tvs=[]
for p,q in itertools.combinations(pts,2):
    t=tv(cols[p],cols[q]); tvs.append(t)
    if t>best: best,arg=t,(p,q)
print('lower bound on Dobrushin delta(K_0->8): %.4f at %s'%(best,arg))
print('median pairwise TV of 25 point-mass starts: %.4f, min %.4f'%(np.median(tvs),min(tvs)))
# distance of each point-start's ensemble from equilibrium at t=8
print('TV(K(x,.),P_8): min %.3f median %.3f max %.3f'%(min(tv(c,P8) for c in cols.values()),np.median([tv(c,P8) for c in cols.values()]),max(tv(c,P8) for c in cols.values())))
# equilibrium-weighted forgetting: P0-weighted average over these points (renormalised) of TV(K(x,.),P8)
w=np.array([P0[p] for p in pts]); w/=w.sum()
print('P0-weighted mean TV(K(x,.),P_8) over the 25 points: %.3f'%(sum(wi*tv(cols[p],P8) for wi,p in zip(w,pts))))
