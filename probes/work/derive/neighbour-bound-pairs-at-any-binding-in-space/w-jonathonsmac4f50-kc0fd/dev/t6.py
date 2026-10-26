from dev_engine import *
import time
for dl in (0.5,0.1,0.03):
    E=EC+dl
    prev=None
    for N in (24,48,72,96,144):
        t=time.time()
        res=free_G(E,(0,0,0),N,axes=(0,),order=1)
        S=G1_series(res,0)
        G1=S[0]; 
        d0=np.abs(G1-prev).max() if prev is not None else float('nan')
        d2=np.abs(S[2]-prevS2).max() if prev is not None else float('nan')
        prev=G1; prevS2=S[2]
        print(dl,N,round(time.time()-t,2),'change G1',d0,'change d2',d2,flush=True)
