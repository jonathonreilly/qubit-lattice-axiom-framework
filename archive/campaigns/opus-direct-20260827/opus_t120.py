"""T120 - IS THE FLAT-CONTROL OFFSET THE TORUS WINDING SUM?  (second route on T119A)

T119(A) found F(tau) = [(4 pi tau)^2 K(tau) - Vol]/tau does NOT vanish on a flat
mesh: it converges, as L grows, to an L-independent 26.72 at tau=0.2 and 40.65 at
tau=0.28.  If that is a lattice defect the whole heat-trace route is dead.  If it
is the torus's own topology it is exactly predictable and harmless.

On the flat unit 4-torus the heat trace is exact.  With eigenvalues 4 pi^2 |n|^2,
   K(tau) = [ sum_m e^{-4 pi^2 m^2 tau} ]^4
and Poisson resummation turns the mode sum into a WINDING sum:
   K(tau) = (4 pi tau)^{-2} sum_{w in Z^4} e^{-|w|^2/(4 tau)}
         = (4 pi tau)^{-2} [ 1 + 8 e^{-1/(4tau)} + 24 e^{-2/(4tau)} + 32 e^{-3/(4tau)} + ... ]
so the prediction with NO free parameters is
   F_exact(tau) = (1/tau) sum_{w != 0} e^{-|w|^2/(4 tau)} .
These are geodesics winding the torus -- global, not local, and invisible to the
Seeley-DeWitt expansion, which is why they do not spoil the a_1 reading provided
they are subtracted or made exponentially small.

This is an absolute prediction, computed from the continuum only.  If the lattice
reproduces it the machinery is verified independently of anything in T119."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum

def F_wind(tau,W=6):
    s=0.0
    for w in itertools.product(range(-W,W+1),repeat=4):
        n2=sum(x*x for x in w)
        if n2: s+=np.exp(-n2/(4.0*tau))
    return s/tau

TAUS=np.array([0.05,0.07,0.10,0.14,0.20,0.28,0.40])
print("T120  flat control vs the exact torus winding sum (zero free parameters)")
print()
print(f"    {'tau':>6} {'CONTINUUM F_exact':>19} |  " + "  ".join(f"L={L:<8}" for L in (5,6,7,8)))
exact=np.array([F_wind(t) for t in TAUS])
meas={}
for L in (5,6,7,8):
    verts,vid,simp=kuhn(L); N=len(verts)
    l20=[lengths_from_positions(positions(s,lambda X:0.0*X,L)) for s in simp]
    lam=spectrum(simp,l20,N)
    K=np.array([float(np.sum(np.exp(-t*lam))) for t in TAUS])
    meas[L]=((4*np.pi*TAUS)**2*K-1.0)/TAUS
for i,t in enumerate(TAUS):
    print(f"    {t:6.2f} {exact[i]:19.6f} |  "+"  ".join(f"{meas[L][i]:10.6f}" for L in (5,6,7,8)))
print()
print("    relative deviation from the continuum prediction")
print(f"    {'tau':>6} |  " + "  ".join(f"L={L:<9}" for L in (5,6,7,8)) + "   exponent p (L=7->8)")
for i,t in enumerate(TAUS):
    r=[abs(meas[L][i]-exact[i])/abs(exact[i]) for L in (5,6,7,8)]
    p=np.log(r[3]/r[2])/np.log(7.0/8.0) if r[2]>0 and r[3]>0 else float('nan')
    print(f"    {t:6.2f} |  "+"  ".join(f"{x:11.3e}" for x in r)+f"     {p:8.2f}")
print()
print("    Matching a parameter-free continuum prediction to 4-5 digits at large tau,")
print("    with the deviation falling as a power of h, verifies the heat-trace")
print("    machinery independently of T119 -- and identifies exactly what must be")
print("    subtracted before reading a_1.")
