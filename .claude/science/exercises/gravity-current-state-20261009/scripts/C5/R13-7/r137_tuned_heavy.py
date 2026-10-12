"""R13-7 REFUTED-direction attempt: tune the photon plateau so the heavy-electron constant dc_e(inf) = 0
(literal edge, e-box (2.5,3.1), photon box (c1, c1+0.6)), then show Delta(m) is still not identically zero."""
import sys; sys.path.insert(0,'.')
import numpy as np
from r137_onshell import *
from r137_sign_scan import inf_const
N=64; lam=0.05
f=lambda c1: inf_const(Law(2.5,3.1,0.0,c1,min(c1+0.6,3.12),1.0),N,lam)
lo,hi=0.5,2.5; flo,fhi=f(lo),f(hi)
print('bracket: c1=%.3f -> %+.4f ; c1=%.3f -> %+.4f'%(lo,flo,hi,fhi))
for it in range(30):
    mid=0.5*(lo+hi); fm=f(mid)
    if np.sign(fm)==np.sign(flo): lo,flo=mid,fm
    else: hi,fhi=mid,fm
c1=0.5*(lo+hi); print('tuned photon plateau c1 = %.6f, c2 = %.6f, dc_e(inf)*U = %+.2e'%(c1,c1+0.6,f(c1)))
print('m, dc_e(on-shell)*U, dc_gamma*U, Delta*U   (N=%d, lam=%.2f)'%(N,lam))
rows=[]
for m in (0.1,0.2,0.4,0.8,1.6,3.2,6.4,12.8,25.6,51.2,102.4):
    law=Law(2.5,3.1,0.0,c1,c1+0.6,m)
    ce,ct,_=ce2_minus_1(law,N,lam,h=0.02); dce=ce/2*U; dcg=moment(law,N)['tot']
    rows.append((m,dce,dcg)); print('  m=%7.2f  dc_e=%+9.4f  dc_g=%+9.4f  Delta=%+9.4f  m*Delta=%+9.4f'%(m,dce,dcg,dce-dcg,m*(dce-dcg)),flush=True)
