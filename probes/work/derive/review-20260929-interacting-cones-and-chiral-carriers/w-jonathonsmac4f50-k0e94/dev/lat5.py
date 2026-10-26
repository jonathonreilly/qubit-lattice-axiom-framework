from lat1 import *
import time
for mu_ in [1/128,1/256]:
    for N in [200,300]:
        t0=time.time(); v=integrate(mu_,N)[0]; print(mu_,N,repr(v),round(time.time()-t0,1),flush=True)
