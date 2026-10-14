"""NF-1 (a): position-space check of the second protecting symmetry P_stag: chi(x) -> eps(x) chi(-x) (inversion times eps), with
A_j(x) -> -A_j(-x) (bond (z, z+e_j) -> bond (-z, -z-e_j)), on the SF-strained staggered law (L = 8 torus, straight axial Wilson lines,
random U(1) links), plus the Theta condition {eps, h[U]} = 0 and the k = 0 consequence: a matrix that both commutes (P_stag) and
anticommutes (Theta) with eps vanishes."""
import numpy as np
from nf1_poslib import pos_space
L = 8
for t, lk in ((0.0, None), (0.3, None), (0.3, True)):
    H, X, sym, th = pos_space(L, t, lk, seed=7)
    eps = (-1.0)**X.sum(1)
    V = L**3
    Xm = (-X) % L
    Pm = np.zeros((V, V)); Pm[np.arange(V), np.ravel_multi_index(Xm.T, (L, L, L))] = eps      # (P chi)(x) = eps(x) chi(-x)
    if lk:
        thP = np.zeros_like(th)
        for j in range(3):
            Z = (-X).copy(); Z[:, j] -= 1; Z %= L                                              # -z - e_j
            thP[j][X[:, 0], X[:, 1], X[:, 2]] = -th[j][Z[:, 0], Z[:, 1], Z[:, 2]]
        HP, _, _, _ = pos_space(L, t, thP)
    else:
        HP = H
    print('L=%d t=%+.1f links=%s: |P h[A] P^-1 - h[A^P]| = %.1e ; |{eps, h}| = %.1e' %
          (L, t, bool(lk), np.abs(Pm @ H @ Pm.T - HP).max(), np.abs(eps[:, None]*H*eps[None, :] + H).max()))
