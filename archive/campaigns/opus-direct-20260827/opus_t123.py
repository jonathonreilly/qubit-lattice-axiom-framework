"""T123 - CLOSING R67 ON S^2 x T^2, WHERE THE 4D CURVATURE IS O(1) AND EXACT.

R67 named the escape from the closed 4D window: stop perturbing a torus, use a
product manifold whose curvature is O(1) with no small parameter.  S^2 x T^2 has
   int R sqrt(g) = (int_{S^2} R dA) * Area(T^2) = 8 pi * Area(T^2)   exactly,
by Gauss-Bonnet on the sphere factor.

The escape is better than it looked, because the Laplacian on a product SPLITS,
   Delta_{X x Y} = Delta_X (x) 1 + 1 (x) Delta_Y   =>   K_{XxY}(tau) = K_X(tau) K_Y(tau),
so the 4D heat trace is the PRODUCT of two 2D ones, exactly, with no 4D mesh and
no eigendecomposition of a 4D operator at all.

AND -- this is the part that makes it a real 4D test rather than a restatement --
the singular set of S^2 x T^2 is (cone points of the icosphere) x T^2, which is
genuinely TWO-DIMENSIONAL.  That is exactly the codimension-2 hinge structure of
a 4D Regge geometry: curvature on 2D hinges, not on points.  So this probes the
object the framework actually has.

What it does NOT test: how hinges meet.  Hinge intersections are codimension 4
and enter at a_2, not a_1, so they cannot affect the coefficient being read.
That limitation is stated, not hidden.

Prediction, zero free parameters:
   (4 pi tau)^2 K(tau) - Vol  ->  (tau/6) int R sqrt(g) = (tau/6) 8 pi A_T
with Vol = Area(S^2_poly) * A_T.  Slope = 8 pi/6 = 4.18879 per unit A_T."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t121 import icosphere, spec2d

def K_torus_exact(tau,A=1.0,W=8):
    """flat T^2 of area A=1 (unit square): exact, via the winding sum."""
    s=0.0
    for w in itertools.product(range(-W,W+1),repeat=2):
        s+=np.exp(-(w[0]**2+w[1]**2)/(4.0*tau))
    return s/(4*np.pi*tau)

print("T123  S^2 x T^2 : the induced Einstein-Hilbert coefficient in 4D")
print(f"      exact target  int R sqrt(g) = 8 pi A_T = {8*np.pi:.6f}   (A_T = 1)")
print(f"      so            [(4 pi tau)^2 K - Vol]/tau  ->  8 pi/6 = {8*np.pi/6:.6f}")
print()
TAUS=np.array([0.004,0.008,0.015,0.025,0.04,0.06,0.09])
for k in (3,4,5):
    P,Fc=icosphere(k); lam,area,ang=spec2d(P,Fc)
    Ks=np.array([float(np.sum(np.exp(-t*lam))) for t in TAUS])
    Kt=np.array([K_torus_exact(t) for t in TAUS])
    K4=Ks*Kt
    Vol=area*1.0
    F=((4*np.pi*TAUS)**2*K4-Vol)/TAUS
    print(f"   icosphere k={k}: {len(P)} vertices, Area_poly = {area:.6f}, Vol = {Vol:.6f}")
    print(f"      {'tau':>8} " + " ".join(f"{t:9.4g}" for t in TAUS))
    print(f"      {'F(tau)':>8} " + " ".join(f"{x:9.5f}" for x in F))
    print(f"      {'err %':>8} " + " ".join(f"{100*(x-8*np.pi/6)/(8*np.pi/6):9.2f}" for x in F),flush=True)
    print()
print("   For reference, the SAME quantity with the exact smooth sphere substituted")
print("   for the polyhedron (isolates mesh error from method error):")
def K_sph_exact(tau,LMAX=600):
    l=np.arange(LMAX+1); return float(np.sum((2*l+1)*np.exp(-tau*l*(l+1))))
Ke=np.array([K_sph_exact(t)*K_torus_exact(t) for t in TAUS])
Fe=((4*np.pi*TAUS)**2*Ke-4*np.pi)/TAUS
print(f"      {'tau':>8} " + " ".join(f"{t:9.4g}" for t in TAUS))
print(f"      {'F_exact':>8} " + " ".join(f"{x:9.5f}" for x in Fe))
print(f"      {'err %':>8} " + " ".join(f"{100*(x-8*np.pi/6)/(8*np.pi/6):9.2f}" for x in Fe))
print()
print(f"   A plateau at {8*np.pi/6:.5f} is the induced Einstein-Hilbert term of a")
print("   4D piecewise-flat geometry with 2D hinges, read with no free parameters.")
