import numpy as np, time
from ice_flux_mc import run_replicas
t=time.time()
for q,exact in ((0,8.0),(1,188/29)):
    qs=np.full(10,q,dtype=np.int64)
    out,diag=run_replicas(2,qs,10,200,20000,2,12345)
    m=out.mean(axis=1)
    print("q",q,"mean",m.mean(),"+/-",m.std(ddof=1)/np.sqrt(len(m)),"exact",exact,"z",(m.mean()-exact)/(m.std(ddof=1)/np.sqrt(len(m))))
    print(" diag bad,W:",diag.max(axis=0),diag.min(axis=0))
print(time.time()-t)
