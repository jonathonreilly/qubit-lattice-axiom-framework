from sim import *
from sim2 import windows
import time
q0=np.array([0.9,-0.6])
for N,m,T0,T,nt in [(96,(10,6),28.0,56.0,113),(160,(17,10),48.0,96.0,193)]:
    t=time.time()
    ts,Jt,wt,nrm,v,r0,K,el=run(N,m,q0,T0,6.0,T,0,nt=nt)
    pk,wb,wa,W,avgb,avga=windows(ts,Jt,wt,1e-2)
    print(f"N={N} K={np.round(K,4)} r0={np.round(r0,1)} peak t={pk:.1f} before {wb} after {wa} W={W:.1f} avgb={avgb:.6f} avga={avga:.6f} diff={avga-avgb:.6f} bound={W*abs(avga-avgb)/4:.4f} [{time.time()-t:.1f}s]")
