"""O2 check 1: tree-level soft-graviton Ward defect for nearest-neighbour KG on Z^3.

The soft gauge variation of an n-point amplitude is xi_nu * sum_i eta_i Q^nu(k_i) * M0,
with Q^i(k) the spatial Ward charge of the one-particle stress vertex.  For nn KG,
E^2 = m^2 + sum_j 2(1-cos k_j) and the energy current per particle is grad(E^2/2) = sin k,
which is also the nn lattice momentum.  We measure the non-additivity
   D = | sum_in sin k - sum_out sin k |
on exactly on-shell 2->2 collisions with sum k conserved (no umklapp) and sum E conserved,
at momentum scale kappa (lattice units), and fit D/kappa ~ kappa^p.
Then: umklapp collisions (sum k_in = sum k_out + 2 pi e_x) give O(1) defect for any
continuous vector charge that equals k near 0 (the folded linear charge jumps by 2 pi).
"""
import numpy as np
rng = np.random.default_rng(12345)

def E(k, m):
    return np.sqrt(m*m + np.sum(2.0*(1.0-np.cos(k)), axis=-1))

def solve_out(K, Etot, n, m, smax):
    # out momenta k3 = K/2 + s n, k4 = K/2 - s n ; find s in (0, smax) with E3+E4 = Etot
    f = lambda s: E(K/2 + s*n, m) + E(K/2 - s*n, m) - Etot
    lo, hi = 0.0, smax
    flo, fhi = f(lo), f(hi)
    if flo*fhi > 0:
        return None
    for _ in range(200):
        mid = 0.5*(lo+hi); fm = f(mid)
        if flo*fm <= 0: hi, fhi = mid, fm
        else: lo, flo = mid, fm
    return 0.5*(lo+hi)

def defect_at_scale(kappa, m, nsamp=400):
    out = []
    for _ in range(nsamp):
        k1 = rng.normal(size=3); k1 *= kappa/np.linalg.norm(k1)
        k2 = rng.normal(size=3); k2 *= kappa*rng.uniform(0.3,1.0)/np.linalg.norm(k2)
        K = k1+k2; Et = E(k1,m)+E(k2,m)
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        s = solve_out(K, Et, n, m, 3*kappa)
        if s is None: continue
        k3 = K/2 + s*n; k4 = K/2 - s*n
        D = np.linalg.norm(np.sin(k1)+np.sin(k2)-np.sin(k3)-np.sin(k4))
        out.append(D/kappa)
    out = np.array(out)
    return np.median(out), np.max(out), len(out)

print("nn KG on Z^3: soft Ward defect D/kappa on on-shell non-umklapp 2->2 collisions")
for m in (1.0, 0.0):
    ks, meds = [], []
    for kappa in (0.4, 0.2, 0.1, 0.05, 0.025, 0.0125):
        med, mx, n = defect_at_scale(kappa, m)
        ks.append(kappa); meds.append(med)
        print(f"  m={m:3.1f} kappa={kappa:7.4f}  median D/kappa={med:.3e}  max={mx:.3e}  (n={n})")
    p = np.polyfit(np.log(ks[2:]), np.log(meds[2:]), 1)[0]
    print(f"  m={m:3.1f} fitted exponent p (D/kappa ~ kappa^p, small kappa) = {p:.3f}")

# continuum-unit translation: kappa = p * a with a = Planck length (non-reduced convention, a^-1 = M_Pl c^2 = 1.22e19 GeV)
MPl = 1.22e19  # GeV
print("\nRelative tree-level defect ~ C kappa^2 with kappa = p/M_Pl (C from the m=1 fit at smallest kappa):")
med, mx, n = defect_at_scale(0.0125, 1.0)
C = med/0.0125**2
for label, pGeV in (("atom-scale 10 keV", 1e-5), ("nucleon Fermi 0.25 GeV", 0.25), ("LHC 1 TeV", 1e3), ("UHECR 1e11 GeV", 1e11)):
    kap = pGeV/MPl
    print(f"  {label:24s} kappa={kap:.2e}  D/kappa ~ {C*kap**2:.1e}")

# umklapp: high-energy collision with k1+k2 = k3+k4 + 2 pi e_x ; charge Q=sin k is periodic so 'sum k' additivity
# is meaningless; any continuous charge equal to k near 0 differs by O(1) somewhere on the umklapp shell.
print("\nUmklapp example (m=1): k1=k2=(2.5,0.3,-0.2); out pair with total K-2pi e_x, energy conserved")
k1 = np.array([2.5,0.3,-0.2]); k2 = np.array([2.5,-0.3,0.2]); m=1.0
K = k1+k2; Et = E(k1,m)+E(k2,m); Kf = K - np.array([2*np.pi,0,0])
best=None
for _ in range(2000):
    nn = rng.normal(size=3); nn/=np.linalg.norm(nn)
    s = solve_out(Kf, Et, nn, m, 4.0)
    if s is None: continue
    k3 = Kf/2+s*nn; k4 = Kf/2-s*nn
    lin_def = np.linalg.norm((k1+k2)-(k3+k4))   # linear (unfolded) charge defect = 2 pi
    sin_def = np.linalg.norm(np.sin(k1)+np.sin(k2)-np.sin(k3)-np.sin(k4))
    best = (lin_def, sin_def, k3, k4); break
print(f"  linear-charge defect |sum k_in - sum k_out| = {best[0]:.4f} (=2 pi); sin-charge defect = {best[1]:.4f}")
