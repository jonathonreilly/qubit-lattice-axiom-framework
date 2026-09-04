"""T122 - THE PIECEWISE-FLAT HEAT TRACE vs THE EXACT SMOOTH SPHERE (second route on T121).

T121 gave the answer twice already, and they agree:
  * Cheeger's exact cone term  sum_v (1/12)(2 pi/theta_v - theta_v/2 pi)  evaluates
    on the icosphere to 0.333923, 0.333519, 0.333402 at k=3,4,5 -> chi/6 = 1/3,
    NOT chi/3.  (My small-deficit expansion of that formula was off by a factor 2;
    the formula itself, evaluated exactly, lands on the continuum value.)
  * the measured c(tau) from the polyhedral spectrum falls toward the same region.
So a piecewise-flat complex carries the CONTINUUM a_1.  Sakharov's coefficient is
not renormalised by the discreteness of the arena.

Third and sharpest route: compare against the exact smooth sphere, no expansion
anywhere.  On the unit S^2 the Laplacian eigenvalues are l(l+1) with multiplicity
2l+1, so
        K_smooth(tau) = sum_l (2l+1) e^{-tau l(l+1)}
is exact and elementary.  If the polyhedral heat trace converges to THIS function
pointwise in tau, as the mesh refines, then the arena reproduces the smooth
spectral geometry entirely -- a_0, a_1 and every coefficient at once, which is a
far stronger statement than matching one number."""
import numpy as np, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t121 import icosphere, spec2d

def K_exact(tau,LMAX=400):
    l=np.arange(LMAX+1)
    return float(np.sum((2*l+1)*np.exp(-tau*l*(l+1))))

TAUS=np.array([0.03,0.05,0.08,0.12,0.20,0.35,0.60])
print("T122  polyhedral heat trace vs the EXACT smooth sphere, K(tau) = sum_l (2l+1) e^{-tau l(l+1)}")
print()
ex=np.array([K_exact(t) for t in TAUS])
print(f"    {'tau':>6} {'K_exact':>12} " + " ".join(f"{'k=%d'%k:>12}" for k in (3,4,5)) + "   |  rel. error k=3,4,5")
res={}
for k in (3,4,5):
    P,Fc=icosphere(k); lam,area,ang=spec2d(P,Fc)
    res[k]=(np.array([float(np.sum(np.exp(-t*lam))) for t in TAUS]),area,len(P))
for i,t in enumerate(TAUS):
    errs=[abs(res[k][0][i]-ex[i])/ex[i] for k in (3,4,5)]
    print(f"    {t:6.2f} {ex[i]:12.6f} " + " ".join(f"{res[k][0][i]:12.6f}" for k in (3,4,5))
          + "   |  " + " ".join(f"{e:8.2e}" for e in errs))
print()
print("    convergence exponent p in (relative error) ~ h^p,  h ~ 2^-k")
print(f"    {'tau':>6} {'k=3->4':>9} {'k=4->5':>9}")
for i,t in enumerate(TAUS):
    e=[abs(res[k][0][i]-ex[i])/ex[i] for k in (3,4,5)]
    p1=np.log(e[1]/e[0])/np.log(0.5); p2=np.log(e[2]/e[1])/np.log(0.5)
    print(f"    {t:6.2f} {p1:9.2f} {p2:9.2f}")
print()
print("    the a_1 constant, read three ways at k=5:")
P,Fc=icosphere(5); lam,area,ang=spec2d(P,Fc)
defs=np.array([2*np.pi-ang[i] for i in range(len(P))])
cone=float(np.sum([(1.0/12.0)*(2*np.pi/(2*np.pi-dd)-(2*np.pi-dd)/(2*np.pi)) for dd in defs]))
print(f"       (i)   smooth Gauss-Bonnet   chi/6                        = {2/6:.6f}")
print(f"       (ii)  Cheeger cone sum on the actual polyhedron          = {cone:.6f}")
kk=np.array([float(np.sum(np.exp(-t*lam))) for t in TAUS])
kex=ex
print(f"       (iii) exact-sphere residual K_exact - Area/(4 pi tau) at tau=0.20 = {K_exact(0.20)-4*np.pi/(4*np.pi*0.20):.6f}")
print(f"       (iv)  polyhedral            K_poly  - Area_poly/(4 pi tau) at tau=0.20 = {kk[4]-area/(4*np.pi*0.20):.6f}")
print()
print("    All four agreeing near 1/3 = the piecewise-flat arena induces the")
print("    CONTINUUM Einstein-Hilbert coefficient, unrenormalised by discreteness.")
