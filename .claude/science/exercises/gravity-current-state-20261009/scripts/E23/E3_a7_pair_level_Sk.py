"""E3 (a7): S(0) of the pair-level stiffness density, big patches (Rp = 36, ~195k points), two estimators:
 (1) Var(W)/<n> for windows r = 2..16 with centres on a grid (spacing r, non-overlapping) inside the interior;
 (2) tapered structure factor S_F(k) = |sum_i (f_i - fbar) phi_i e^{ik.x_i}|^2 / sum phi_i^2, Gaussian taper w = 9,
     |k| = 0.15 .. 2.0, 300 random directions per shell; 5 TT directions averaged.  White: S_F(k->0) = const > 0.
Substrates: icosahedral model set, Poisson, perturbed Z^3 (s = 0.3).  Kernel Rk = 2.2 (and 1.8)."""
import numpy as np
from scipy.spatial import cKDTree
import E3_a_core as q, e23_core as c
from E3_a6_pair_level_window_noise import density
rng = np.random.default_rng(12)
Rp = 36.0
subs = {'quasicrystal': q.ico_patch_fast(Rp, np.array([0.21, -0.17, 0.33]))[0]}
X = rng.uniform(-Rp, Rp, (int((2 * Rp)**3), 3)); subs['Poisson'] = X[np.linalg.norm(X, axis=1) < Rp]
r = np.arange(-37, 38); g = np.stack(np.meshgrid(r, r, r, indexing='ij'), -1).reshape(-1, 3).astype(float)
Y = g + 0.3 * rng.standard_normal(g.shape); subs['perturbed Z3 s=0.3'] = Y[np.linalg.norm(Y, axis=1) < Rp]
dirs = rng.standard_normal((300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
for Rk in [2.2, 1.8]:
    print(f"== Rk = {Rk}")
    for name, X in subs.items():
        F = density(X, Rk); Ri = Rp - Rk - 0.5; m = np.linalg.norm(X, axis=1) < Ri
        Xi, Fi = X[m], F[m] - F[m].mean(0); tr = cKDTree(Xi)
        row = []
        for rr in [2, 4, 8, 12, 16]:
            gg = np.arange(-Ri, Ri + 1e-9, 2 * rr); cs = np.stack(np.meshgrid(gg, gg, gg, indexing='ij'), -1).reshape(-1, 3)
            cs = cs[np.linalg.norm(cs, axis=1) < Ri - rr]
            idx = tr.query_ball_point(cs, rr); W = np.array([Fi[i].sum(0) for i in idx]); n = np.array([len(i) for i in idx])
            row.append(f"r={rr}({len(cs)}):{(W**2).mean()/n.mean():.2e}")
        w = 9.0; phi = np.exp(-np.einsum('ij,ij->i', Xi, Xi) / (2 * w**2)); sel = phi > 1e-8
        Xs, Fs, ph = Xi[sel], Fi[sel], phi[sel]
        sk = []
        for k in [0.15, 0.3, 0.5, 1.0, 2.0]:
            E = np.exp(1j * k * Xs @ dirs.T) * ph[:, None]              # n x 300
            A = Fs.T @ E                                                # 5 x 300
            sk.append(f"k={k}:{np.mean(np.abs(A)**2)/np.sum(ph**2):.2e}")
        print(f"  {name:20s} N={len(X)} mean {F[m].mean():+.5f} per-pt var {np.mean(Fi**2):.2e} | " + " ".join(row) + " | S_F: " + " ".join(sk), flush=True)
