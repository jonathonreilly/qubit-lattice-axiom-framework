import numpy as np, sys, time
from lib import *
from tiles import patch
n,b=patch((4,4))
for ferm in (True,False):
    for N in (6,7,8,9):
        t=time.time()
        H,_=build_sector(n,b,N,N//2,ferm)
        w=sla.eigsh(H,k=2,which='SA',tol=1e-11)[0]
        print("open4x4","F" if ferm else "B",N,H.shape[0],np.sort(w),round(time.time()-t,1),flush=True)
