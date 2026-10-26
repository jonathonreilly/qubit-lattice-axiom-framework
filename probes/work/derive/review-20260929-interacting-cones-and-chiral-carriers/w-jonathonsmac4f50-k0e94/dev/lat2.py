from lat1 import *
import time
for mu_ in [0.25,0.125,0.0625,1/32,1/64,0.0]:
    for N in [60,120,200]:
        t0=time.time(); v=integrate(mu_,N)[0]; print(mu_,N,v,round(time.time()-t0,1),flush=True)
