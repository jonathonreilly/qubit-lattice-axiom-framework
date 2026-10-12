"""R13-7: the 1/m coefficient of the heavy-electron expansion, dc_e(m) = dc_inf + e1/m + O(1/m^2) (literal edge),
estimated as e1 ~ m (dc_e(m) - dc_inf) at m = 51.2 and 102.4 (Richardson-combined), over the literal shape scan."""
import sys; sys.path.insert(0,'.')
import numpy as np
from r137_onshell import *
from r137_sign_scan import inf_const
N=64; lam=0.05
print('e-box, photon-box, dc_inf*U, e1*U (from m=51.2,102.4), photon dc_g*U at m=0.1')
res=[]
for b1,b2 in [(0.5,1.5),(1.0,2.0),(1.5,2.5),(2.0,3.0),(2.5,3.1),(1.0,3.0),(2.0,2.5),(2.8,3.1),(0.3,0.6)]:
    for c in [(None,None),(0.5,1.0),(b1,b2),(2.5,3.1),(2.8,3.12)]:
        dinf=inf_const(Law(b1,b2,0.0,c[0],c[1],1.0),N,lam)
        e=[]
        for m in (51.2,102.4):
            ce,_,_=ce2_minus_1(Law(b1,b2,0.0,c[0],c[1],m),N,lam,h=0.02); e.append(m*(ce/2*U-dinf))
        e1=2*e[1]-e[0]
        res.append((b1,b2,c,dinf,e1))
        print('  (%.1f,%.2f) %-12s dc_inf=%+9.4f  e1=%+9.3f   [m e-estimates %+.3f %+.3f]'%(b1,b2,str(c),dinf,e1,e[0],e[1]),flush=True)
print('e1 range over scan: [%+.3f, %+.3f]; shapes with dc_inf>0: %d'%(min(r[4] for r in res),max(r[4] for r in res),sum(r[3]>0 for r in res)))
