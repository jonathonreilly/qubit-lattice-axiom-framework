import numpy as np, time
from common import *
L=24
ring=Ring(L)
m=Bell2(L,0.0,np.pi/4,ring)
P0=m.P(0.0)
print('P0 sum',P0.sum(), 'min', P0.min())
t0=time.time()
te=np.arange(0,9.0)
rho=m.evolve(P0,te)
print('time',time.time()-t0)
for i,t in enumerate(te):
    Pt=m.P(t)
    print(t, np.abs(rho[i]-Pt).max(), rho[i].sum())
