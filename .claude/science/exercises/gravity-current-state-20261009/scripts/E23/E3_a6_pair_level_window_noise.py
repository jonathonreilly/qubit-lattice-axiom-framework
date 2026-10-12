"""E3 (a6): S(0) of the pair-level stiffness density on very large patches (EXACT direct sums).
f_i = 1/2 sum_j [V''(s)(D.h.D)^2 + V'(s)(D.h^2.D)], V = (1 - s/Rk^2)_+^4, 5 TT directions, per point i.
Window sums W(r) = sum_{|x_i - c| < r} (f_i - fbar) over balls with random centres; Var(W)/<n(r)> vs r.
White noise (S(0) > 0): flat.  Hyperuniform (S(0) = 0): decays (class I: ~1/r).
Substrates (density 1): icosahedral model set (spherical window), Poisson, Gaussian-perturbed Z^3 (s = 0.3), stealthy is
periodic-box only (not here).  Kernel ranges Rk = 1.8 and 2.2."""
import numpy as np
from scipy.spatial import cKDTree
import E3_a_core as q, e23_core as c
rng = np.random.default_rng(11)
Rp, Rmax = 22.0, 2.2

def density(X, Rk):
    P = cKDTree(X).query_pairs(Rk, output_type='ndarray')
    D = X[P[:, 1]] - X[P[:, 0]]; s = np.einsum('pk,pk->p', D, D); u = s / Rk**2
    V1 = -4 * (1 - u)**3 / Rk**2; V2 = 12 * (1 - u)**2 / Rk**4
    F = np.zeros((len(X), 5))
    for d, h in enumerate(c.DIRS):
        sp = np.einsum('pi,ij,pj->p', D, h, D); spp = np.einsum('pi,ij,pj->p', D, h @ h, D)
        v = 0.5 * (V2 * sp**2 + V1 * spp)
        np.add.at(F[:, d], P[:, 0], v); np.add.at(F[:, d], P[:, 1], v)
    return F

def window_var(X, F, Ri):
    m = np.linalg.norm(X, axis=1) < Ri; Xi, Fi = X[m], F[m] - F[m].mean(0)
    tr = cKDTree(Xi); out = []
    for r in [1, 2, 3, 4, 6, 8, 10]:
        cs = rng.uniform(-(Ri - r), Ri - r, (4000, 3)); cs = cs[np.linalg.norm(cs, axis=1) < Ri - r][:1500]
        idx = tr.query_ball_point(cs, r)
        W = np.array([Fi[i].sum(0) for i in idx]); n = np.array([len(i) for i in idx])
        out.append((r, n.mean(), (W**2).mean() / n.mean()))
    return out, np.mean(Fi**2)

if __name__ == "__main__":
  subs = {}
  gam = np.array([0.21, -0.17, 0.33])
  subs['quasicrystal'] = q.ico_patch_fast(Rp, gam)[0]
  X = rng.uniform(-Rp, Rp, (int((2 * Rp)**3), 3)); subs['Poisson'] = X[np.linalg.norm(X, axis=1) < Rp]
  r = np.arange(-23, 24); g = np.stack(np.meshgrid(r, r, r, indexing='ij'), -1).reshape(-1, 3).astype(float)
  Y = g + 0.3 * rng.standard_normal(g.shape); subs['perturbed Z3 s=0.3'] = Y[np.linalg.norm(Y, axis=1) < Rp]
  for Rk in [1.8, 2.2]:
      print(f"== kernel range Rk = {Rk}: Var(W)/<n> for window radii r (per-point variance in brackets)")
      for name, X in subs.items():
          F = density(X, Rk); out, pv = window_var(X, F, Rp - Rk - 0.5)
          print(f"  {name:20s} mean {F[np.linalg.norm(X,axis=1) < Rp-Rk-0.5].mean():+.5f} [{pv:.2e}] " +
                " ".join(f"r={o[0]}:{o[2]:.2e}" for o in out), flush=True)
