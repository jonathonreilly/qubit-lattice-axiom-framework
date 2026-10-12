"""E3 (a0) validation of the local stiffness density on open patches: Z^3 ball (exact bulk value known:
E_g +0.0473827, T_2g +0.0140046 for m2 = 1) and a Poisson ball (ensemble mean 0)."""
import numpy as np, time
import E3_a_core as q, e23_core as c
rng = np.random.default_rng(5)
Rp = 8.0
r = np.arange(-9, 10)
g = np.stack(np.meshgrid(r, r, r, indexing='ij'), -1).reshape(-1, 3).astype(float)
Z = g[np.linalg.norm(g, axis=1) < Rp] + 1e-9
t0 = time.time(); e1, e2 = q.local_stiffness(Z); print(f"Z3 ball N={len(Z)} [{time.time()-t0:.0f}s]")
rad = np.linalg.norm(Z, axis=1)
for buf in [2, 3, 4, 5]:
    m = rad < Rp - buf
    print(f"  buffer {buf}: n_int={m.sum():4d}  E_g {e2[m][:, c.CH['E_g']].mean():+.7f}  T_2g {e2[m][:, c.CH['T_2g']].mean():+.7f}"
          f"  max site deviation {np.abs(e2[m][:, 0] - 0.0473827).max():.1e}")
print("  total E''/N over whole ball (boundary-contaminated):", e2[:, c.CH['E_g']].sum(0).mean() / len(Z))
X = rng.uniform(-Rp, Rp, (int(2 * (2 * Rp)**3), 3)); X = X[np.linalg.norm(X, axis=1) < Rp]
t0 = time.time(); p1, p2 = q.local_stiffness(X); print(f"Poisson ball N={len(X)} [{time.time()-t0:.0f}s]")
rad = np.linalg.norm(X, axis=1)
for buf in [3, 4]:
    m = rad < Rp - buf
    print(f"  buffer {buf}: n_int={m.sum():4d}  E_g {p2[m][:, c.CH['E_g']].mean():+.5f}  T_2g {p2[m][:, c.CH['T_2g']].mean():+.5f}"
          f"  per-site sd {p2[m].std():.4f}")
np.savez("E3_a0_validate.npz", Z=Z, e2=e2, X=X, p2=p2)
