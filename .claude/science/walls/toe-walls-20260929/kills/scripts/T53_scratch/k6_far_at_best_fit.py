"""Kill-check T53: far chamber-interior root at the NuFIT-6.1 best-fit triple (0.307,0.0218,0.470): precise root, margin, I_src, and dCP on all four label sheets."""
import numpy as np
from scipy.optimize import fsolve
from chart import H, obs, SQ
def solve(perm,gamma,x0,t=(0.307,0.0218,0.470)):
    f=lambda x:[obs(*x,gamma,perm)['s12']-t[0],obs(*x,gamma,perm)['s13']-t[1],obs(*x,gamma,perm)['s23']-t[2]]
    x=fsolve(f,x0,xtol=1e-14); assert max(abs(v) for v in f(x))<1e-10; return x
for perm,x0 in [((2,0,1),(26.9,19.2,4.5)),((2,1,0),(22.25,13.83,2.52))]:
    x=solve(perm,0.5,x0)
    Hm=H(*x,0.5); I=(Hm[0,1]*Hm[1,2]*Hm[2,0]).imag
    print('root for sigma',perm,'gamma=+.5:',np.round(x,4),'margin=%+.3f'%(x[1]+x[2]-SQ),'I_src=%+.2f'%I)
    for g in (0.5,-0.5):
        for p in [(2,1,0),(2,0,1)]:
            o=obs(*x,g,p); print('     labels gamma=%+.1f sigma=%s -> s23^2=%.4f dCP=%.2f sin=%+.3f'%(g,p,o['s23'],o['dcp'],o['sind']))
