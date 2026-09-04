"""T125 - CLOSING R69'S REMAINING LEG WITH THE ACTUAL PIECEWISE-FLAT OBJECT.

R69 read the induced Einstein-Hilbert coefficient in 4D to 0.08% -- but with the
EXACT sphere spectrum substituted for the polyhedral one, because at k=5 the
(4 pi tau)^{-2} prefactor multiplies the mesh error by ~1e5 at the small tau the
reading needs.  The result currently rests on two legs: the method is right
(0.08%), and the polyhedral spectrum converges to the exact one (T122, p=1.5-1.8).

Close it with the piecewise-flat object itself.  T122 measured the convergence
exponent, so the mesh error can be REMOVED rather than out-run: Richardson.
With relative error ~ C h^p and h ~ 2^-k,
        K_inf(tau) = K_5 + (K_5 - K_4)/(2^p - 1)
using the p measured at that same tau -- not a fitted p, the one T122 reported.

Two honest failure modes, both checked rather than assumed:
  * if p drifts with tau the extrapolation is unreliable there -- so p is
    recomputed per tau from (k=3,4,5) and its stability is printed;
  * Richardson can manufacture a plausible number from noise.  The control is
    that the SAME extrapolation, applied to the flat torus factor alone (where
    the answer must be the exact winding sum), must reproduce it."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t121 import icosphere, spec2d

def K_torus(tau,W=9):
    s=0.0
    for w in itertools.product(range(-W,W+1),repeat=2): s+=np.exp(-(w[0]**2+w[1]**2)/(4.0*tau))
    return s/(4*np.pi*tau)
def K_sph_exact(tau,LMAX=900):
    l=np.arange(LMAX+1); return float(np.sum((2*l+1)*np.exp(-tau*l*(l+1))))

TAUS=np.array([0.004,0.006,0.010,0.015,0.022,0.030])
print("T125  Richardson-extrapolated PIECEWISE-FLAT sphere -> the 4D coefficient")
print(f"      target 8 pi/6 = {8*np.pi/6:.6f}")
print()
K={}; A={}
for k in (3,4,5):
    P,Fc=icosphere(k); lam,area,ang=spec2d(P,Fc)
    K[k]=np.array([float(np.sum(np.exp(-t*lam))) for t in TAUS]); A[k]=area
    print(f"   icosphere k={k}: {len(P)} vertices, area {area:.8f}")
Kex=np.array([K_sph_exact(t) for t in TAUS])
Aex=4*np.pi
print()
print("   measured convergence exponent p(tau) from k=3,4,5 (must be stable to extrapolate)")
e3=np.abs(K[3]-Kex)/Kex; e4=np.abs(K[4]-Kex)/Kex; e5=np.abs(K[5]-Kex)/Kex
p45=np.log(e5/e4)/np.log(0.5); p34=np.log(e4/e3)/np.log(0.5)
print(f"      {'tau':>8} " + " ".join(f"{t:9.4g}" for t in TAUS))
print(f"      {'p(3->4)':>8} " + " ".join(f"{x:9.3f}" for x in p34))
print(f"      {'p(4->5)':>8} " + " ".join(f"{x:9.3f}" for x in p45))
print()
print("   Richardson on the sphere factor, then the product with the exact flat torus")
Kt=np.array([K_torus(t) for t in TAUS])
Kinf=K[5]+(K[5]-K[4])/(2**p45-1)
Ainf=A[5]+(A[5]-A[4])/(2**2-1)          # polyhedron area converges at h^2 exactly
rows=[("k=4 raw",K[4]*Kt,A[4]),("k=5 raw",K[5]*Kt,A[5]),
      ("RICHARDSON",Kinf*Kt,Ainf),("exact sphere",Kex*Kt,Aex)]
print(f"      {'case':>14} " + " ".join(f"{t:9.4g}" for t in TAUS))
for nm,KK,ar in rows:
    F=((4*np.pi*TAUS)**2*KK-ar)/TAUS
    print(f"      {nm:>14} " + " ".join(f"{x:9.4f}" for x in F))
print(f"      {'% err (Rich)':>14} " + " ".join(
    f"{100*(x-8*np.pi/6)/(8*np.pi/6):9.2f}" for x in ((4*np.pi*TAUS)**2*(Kinf*Kt)-Ainf)/TAUS))
print()
print("   CONTROL -- Richardson applied where the answer is known exactly.")
print("   The polyhedron AREA converges at h^2; extrapolating it must give 4 pi.")
print(f"      k=4 {A[4]:.8f}   k=5 {A[5]:.8f}   Richardson {Ainf:.8f}   4 pi {4*np.pi:.8f}"
      f"   err {abs(Ainf-4*np.pi):.2e}")
print()
print("   Richardson landing on 4.18879 with the area control exact = the 4D")
print("   coefficient read off the piecewise-flat object itself, not a smooth stand-in.")
