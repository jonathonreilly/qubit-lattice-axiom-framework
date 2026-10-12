"""E3 (a5): pair-potential level (R3's necessity-lemma setting), EXACT direct sums, no eigenproblem.
E_pair per point = 1/2 sum_{j != i} V(d_g(i,j)^2), V(s) = (1 - s/Rk^2)_+^4.  Shear second derivative at t = 0 per point:
  1/2 sum_j [ V''(s) (D.h.D)^2 + V'(s) (D.h^2.D) ],  averaged over interior points and the channel's directions.
Substrates at density 1: icosahedral model set (spherical window, 3 generic offsets), Z^3 crystal, Poisson (control),
hard-core RSA d0 = 0.8 (glass).  Scan of the kernel range Rk.  R3's lemma: shear-blind for EVERY V iff rho2 = a + b/r^3;
so a quasicrystal zero at one Rk would be accidental (a tuned range), not protected."""
import numpy as np
from scipy.spatial import cKDTree
import E3_a_core as q, e23_core as c
rng = np.random.default_rng(77)
RK = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.6, 3.0]
Rp, Rmax = 16.0, 3.0

def pair_hessian(X, interior):
    tr = cKDTree(X); P = tr.query_pairs(Rmax, output_type='ndarray')
    P = P[interior[P[:, 0]] | interior[P[:, 1]]]
    D = X[P[:, 1]] - X[P[:, 0]]; s = np.einsum('pk,pk->p', D, D)
    wt = interior[P[:, 0]].astype(float) + interior[P[:, 1]].astype(float)   # each interior endpoint gets 1/2 of the pair
    res = {}
    for Rk in RK:
        u = s / Rk**2; ok = u < 1
        V1 = np.where(ok, -4 * (1 - u)**3 / Rk**2, 0); V2 = np.where(ok, 12 * (1 - u)**2 / Rk**4, 0)
        out = []
        for h in c.DIRS:
            sp = np.einsum('pi,ij,pj->p', D, h, D); spp = np.einsum('pi,ij,pj->p', D, h @ h, D)
            out.append(0.5 * np.sum(wt * (V2 * sp**2 + V1 * spp)) / interior.sum())
        out = np.array(out); res[Rk] = (out[c.CH['E_g']].mean(), out[c.CH['T_2g']].mean(), out.std())
    return res

def report(name, X):
    interior = np.linalg.norm(X, axis=1) < Rp - Rmax - 0.5
    r = pair_hessian(X, interior)
    print(f"{name:18s} n_int={interior.sum():6d} " + " ".join(f"R{Rk}:{v[0]:+.4f}/{v[1]:+.4f}" for Rk, v in r.items()), flush=True)
    return r

for k in range(3):
    while True:
        gam = rng.uniform(-0.6, 0.6, 3)
        if np.linalg.norm(gam) < 0.6: break
    X, _ = q.ico_patch(Rp, gam); report(f"quasicrystal {k}", X)
r = np.arange(-17, 18); g = np.stack(np.meshgrid(r, r, r, indexing='ij'), -1).reshape(-1, 3).astype(float) + 0.31
report("Z3 crystal", g[np.linalg.norm(g, axis=1) < Rp])
for k in range(2):
    X = rng.uniform(-Rp, Rp, (int((2 * Rp)**3), 3)); report(f"Poisson {k}", X[np.linalg.norm(X, axis=1) < Rp])
print("(entries: E_g/T_2g pair-level second derivative per point; Poisson rows show the sampling noise level)")
