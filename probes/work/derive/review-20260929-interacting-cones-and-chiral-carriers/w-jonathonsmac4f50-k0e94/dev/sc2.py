from sc1 import AmB
import time
for r,Ns in [(0.1,[512,1024]),(0.05,[512,1024,1536]),(0.025,[1024,1536])]:
    for N in Ns:
        t0=time.time(); print(r,N,AmB(r,N),round(time.time()-t0,1),flush=True)
