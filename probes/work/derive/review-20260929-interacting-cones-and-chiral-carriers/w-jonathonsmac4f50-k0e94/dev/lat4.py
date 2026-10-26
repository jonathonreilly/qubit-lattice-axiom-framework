from lat3 import *
for P in [0.05,0.025,0.0125]:
    for N in [400,700,1000]:
        t0=time.time(); v=dE(P,0.0,N)/np.sin(P); print(P,N,v,round(time.time()-t0,1),flush=True)
