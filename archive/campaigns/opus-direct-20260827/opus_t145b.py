"""T145b - the same independent check, inside a window that actually exists.

T145 was inconclusive and the reason is one the campaign already established:
at L=5-6 with s = 0.05-0.25 on the unit torus, s/a^2 = s L^2 = 1.8 to 9, which is
deep inside the lattice-error region (plain-operator UV floor s ~ 25 a^2, R78).
There is no window at that size -- which is exactly why the bridge lane needed
L = 32/64.  My check did not test their claim; it re-derived their obstruction.

Retry with the COVARIANT SYMANZIK operator, whose 1% floor is s ~ 2.7 a^2 (R78,
c = 1/24 verified by hand).  In unit-torus units lambda_unit = lambda_lat L^2, so
the improvement reads  lambda -> lambda + lambda^2/(24 L^2).  At L=8 the window is
then roughly s/a^2 in [3, 10], i.e. s in [0.047, 0.16], with the winding fraction
8 exp(-1/(4s)) still small at the bottom of it.  Narrow, but it exists."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t145 import run

print("T145b  same relation, improved operator, inside the window")
print("       (4 pi s)^2 dK - dVol  ==  s dS_Regge/3,  with lambda -> lambda + lambda^2/(24 L^2)")
print()
for L in (6,8):
    lam0,lamp,V0,Vp,S0,Sp=run(L,0.10)
    dV=Vp-V0; dS=Sp-S0
    i0=lam0+lam0**2/(24.0*L*L); ip=lamp+lamp**2/(24.0*L*L)
    print(f"   L={L}:  dVol = {dV:+.5e}  dS_Regge = {dS:+.5e}  predicted slope dS/3 = {dS/3:+.5e}")
    print(f"      {'s':>7} {'s/a^2':>7} {'wind frac':>10} | {'PLAIN ratio':>12} {'IMPROVED ratio':>15}")
    for s in (0.05,0.07,0.09,0.11,0.14,0.18):
        wf=8*np.exp(-1.0/(4*s))
        def ratio(a,b):
            dK=float(np.sum(np.exp(-s*b))-np.sum(np.exp(-s*a)))
            return (((4*np.pi*s)**2*dK)-dV)/s/(dS/3)
        print(f"      {s:7.3f} {s*L*L:7.2f} {wf:10.2e} | {ratio(lam0,lamp):12.4f} {ratio(i0,ip):15.4f}")
    print()
print("   The improved column approaching 1 where the plain one does not is the check:")
print("   it would confirm the bridge lane's relation independently, and confirm that")
print("   the failure in T145 was the UV floor rather than the physics.")
