"""T31 - DOUBLE extrapolation.  Step 1: Richardson in the lattice spacing at fixed
s k^2 (L=32,s) vs (L=64,4s)  ->  r_cont(s k^2).  Step 2: linear extrapolation of
r_cont in s k^2 -> 0, which removes the a_2 (derivative-expansion) tail.
What survives is the coefficient of the Einstein term relative to the Regge/
heat-kernel prediction, with both lattice systematics projected out."""
import numpy as np
z32=np.load("struct_L32_a0.06_nk1_14.npz"); z64=np.load("spec_L64_a0.06_nk1.npz")
def mk(z,pre,post,imp):
    lf=z['flat'+post]; Vf,Rf=z['flat'+pre]; muf=lf+lf*lf/24.0 if imp else lf
    def r(t,s):
        lp=z[t+post]; Vp,Rp=z[t+pre]; mu=lp+lp*lp/24.0 if imp else lp
        P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
        return ((P-(Vp-Vf))/s)/((Rp-Rf)/3)
    return r
k2=(2*np.pi/32)**2
print("T31  r* = value after Richardson in a AND linear removal of the s k^2 tail")
print(f"{'op':>4} {'channel':>16} {'fit window in s(32)':>22} {'s k^2 range':>14} {'r*':>9} {'slope':>9}")
for imp in (True,False):
    r32=mk(z32,'VR','lam',imp); r64=mk(z64,'_VR','_lam',imp)
    for t32,t64,nm in (('(0, 1, -1, 0)','TT','TT  (0,1,-1,0)'),('(1, 1, 1, 1)','conf','conf(1,1,1,1)')):
        for w in ([5,6,8,10],[6,8,10,12],[8,10,12,16],[10,12,16,20],[6,8,10,12,16,20]):
            x=np.array([s*k2 for s in w]); y=np.array([(4*r64(t64,4*s)-r32(t32,s))/3 for s in w])
            A=np.stack([np.ones_like(x),x],1); c,*_=np.linalg.lstsq(A,y,rcond=None)
            print(f"{'imp' if imp else 'pln':>4} {nm:>16} {str(w):>22} "
                  f"{f'{x[0]:.3f}-{x[-1]:.3f}':>14} {c[0]:9.4f} {c[1]:9.4f}")
        print()
