"""
T271 - extrapolate the 1/s lattice artifact and recover b1 in d=3.

T269 showed R_lat -> R_cont monotonically with a deviation ~ c/s.  Fit
R_lat(s) = A + B/s at fixed x over a window of L, and test A against the
exact continuum R_cont(x).  Then fit the slope of A(x) and compare to
b1 = (d-1)/(3d) = 2/9  (T270, symbolic; and 1/4 at d=4 matches MEASURED R132).

Controls: (i) two disjoint fit windows -- if A moves, the extrapolation is
unreliable; (ii) B must come out ~universal across x if it is a genuine
lattice artifact rather than a per-x fudge.
"""
import numpy as np, time
from opus_t269 import heat3
Rcont={0.10:1.02374, 0.20:1.05038, 0.35:1.09533, 0.50:1.14569}
xs=np.array(sorted(Rcont)); h=0.05
Ls=(32,40,56,72,96,120)
data={}
for L in Ls:
    t0=time.time(); kap=2*np.pi/L; s=xs/kap**2
    Ks={};Vs={}
    for e in (-2,-1,0,1,2): Ks[e],Vs[e]=heat3(L,e*h,s)
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    data[L]=((4*np.pi*s)**1.5*d2(Ks)/d2(Vs), s)
    print(f"  L={L:3d} done [{time.time()-t0:.0f}s]  R = "+" ".join(f"{r:.5f}" for r in data[L][0]))

def extrap(window):
    A=[];B=[]
    for i,x in enumerate(xs):
        sv=np.array([data[L][1][i] for L in window]); rv=np.array([data[L][0][i] for L in window])
        co=np.polyfit(1.0/sv, rv, 1)          # R = A + B*(1/s)
        A.append(co[1]); B.append(co[0])
    return np.array(A), np.array(B)

for window in ((40,56,72),(56,72,96),(72,96,120)):
    A,B=extrap(window)
    print(f"\n=== fit window L={window} ===")
    print("    x     R_extrap    R_cont     dev        B (artifact coeff)")
    for i,x in enumerate(xs):
        print(f"  {x:5.3f}  {A[i]:9.5f}  {Rcont[x]:9.5f}  {A[i]/Rcont[x]-1:+9.2e}   {B[i]:8.4f}")
    b1=np.polyfit(xs,A-1,1)[0]
    print(f"  slope of (R_extrap - 1) vs x : b1 = {b1:.5f}    2/9 = {2/9:.5f}   dev {b1/(2/9)-1:+.2%}")
