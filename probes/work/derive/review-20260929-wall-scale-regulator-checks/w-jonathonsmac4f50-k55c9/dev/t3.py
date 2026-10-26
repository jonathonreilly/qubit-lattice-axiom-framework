import numpy as np, time, sys
from engine import *
lat=Lat((4,4,4,4))
for nmd,tau in [(5,1.0),(8,1.0)]:
    h=HMC(lat,6.0,Ns=1,m=0.1,nmd=nmd,tau=tau,seed=3)
    t=time.time()
    for k in range(40): h.trajectory(thermal=True) if h.Ns==0 else None
    hq=HMC(lat,6.0,Ns=0,nmd=10,tau=1.0,seed=3)
    for k in range(60): hq.trajectory(thermal=True)
    h.U=hq.U.copy()
    t=time.time(); acc=0; dHs=[]
    for k in range(12):
        a,d=h.trajectory(); acc+=a; dHs.append(d)
    print(nmd,tau,'time/traj',(time.time()-t)/12,'acc',acc/12,'dH',np.round(dHs,2),'cg/traj',h.f.cg_iters/12,'P',h.g.plaq(h.U))
