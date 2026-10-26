from dev_engine import *
import time,sys
Mz=np.eye(4,dtype=complex); Mall=build_M_all(Mz)
for g in (12.0,8.0,6.0,5.0,4.5,4.0):
    for N in (24,40):
        t=time.time()
        out=scan_g(Mall,g,N,+1)
        print('g',g,'N',N,'time',round(time.time()-t,1),flush=True)
        for r,m,nl,fi,ev in out:
            print('   E0=%.6f mult=%d null=%d first=%.1e  max=%.5f min=%.5f'%(r,m,nl,fi,ev.max(),ev.min()),flush=True)
