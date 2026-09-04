"""T30 - Richardson in the lattice spacing at FIXED PHYSICS.
r(s) depends on the lattice through a^2/s and a^2 k^2; the physical variable is
s k^2.  (L=32, s) and (L=64, 4s) have the SAME s k^2 and half the effective
spacing, so the residual error falls like 1/L^2 and r_cont = (4 r64 - r32)/3."""
import numpy as np
z32=np.load("struct_L32_a0.06_nk1_14.npz"); z64=np.load("spec_L64_a0.06_nk1.npz")
def mk(z,pre,post,imp=True):
    lf=z['flat'+post]; Vf,Rf=z['flat'+pre]; muf=lf+lf*lf/24.0 if imp else lf
    def r(t,s):
        lp=z[t+post]; Vp,Rp=z[t+pre]; mu=lp+lp*lp/24.0 if imp else lp
        P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
        return ((P-(Vp-Vf))/s)/((Rp-Rf)/3)
    return r
for imp in (True,False):
    r32=mk(z32,'VR','lam',imp); r64=mk(z64,'_VR','_lam',imp)
    print(f"\nT30 {'improved' if imp else 'plain'}:  r_cont = (4 r64 - r32)/3 at matched s k^2")
    print(f"  {'s(32)':>6} {'s(64)':>6} {'s k^2':>7} | {'TT r32':>8}{'TT r64':>8}{'TT cont':>9} | "
          f"{'cf r32':>8}{'cf r64':>8}{'cf cont':>9}")
    for s in (3,4,5,6,8,10,12,16,20):
        k2=(2*np.pi/32)**2
        a=r32('(0, 1, -1, 0)',s); b=r64('TT',4*s)
        c=r32('(1, 1, 1, 1)',s); d=r64('conf',4*s)
        print(f"  {s:6.1f} {4*s:6.1f} {s*k2:7.3f} | {a:8.4f}{b:8.4f}{(4*b-a)/3:9.4f} | "
              f"{c:8.4f}{d:8.4f}{(4*d-c)/3:9.4f}")
