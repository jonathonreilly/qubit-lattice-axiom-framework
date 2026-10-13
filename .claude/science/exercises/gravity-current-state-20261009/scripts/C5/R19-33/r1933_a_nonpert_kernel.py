"""R19-33 (a) non-perturbative control: at fixed slice-0 data, site RP <=> the cross kernel
X(b, a) = exp(lam * Bcross(b, a)) is a positive-semidefinite kernel in the slice-1 variable
a = phi_1 - phi_0 (b = Theta a); the one-sided factors are a positive diagonal rescaling (Markov).
A kernel is PSD iff every finite Gram matrix is, so a negative eigenvalue of X on a finite grid of
a-values proves a site-RP violation at that lam (bump test functions around the grid points).
Spatial torus 2^3 (8 sites), a_x in {-1, 0, 1}: a random subset of 1500 of the 3^8 grid points (dense eigvalsh); screened K (muK = 0.3).
"""
import numpy as np, itertools, importlib.util, sys
from scipy.sparse.linalg import eigsh
src = open(__file__.replace("_nonpert_kernel", "_site_rp")).read().split("rng = np.random.default_rng(5)")[0]
s = {}; exec(src, s)
L, m, muK = 2, 0.5, 0.3
R, C1, Lap, idx = s['half_chain'](L, m); N = L ** 3
K = np.linalg.inv(Lap + muK ** 2 * np.eye(N))
grid = np.array(list(itertools.product([-1.0, 0.0, 1.0], repeat=N)))
grid = grid[np.random.default_rng(1).choice(len(grid), 1500, replace=False)]   # random finite subset (still a valid Gram test)
G2 = grid ** 2
P = np.einsum('ix,iy->ixy', grid, grid).reshape(len(grid), -1)
Q = grid * (G2 @ K.T)            # Q_x = a_x sum_y K_xy a_y^2
def B(disc, br, w):
    if disc == 'D2':
        return (0.625 if br == 'GR' else 0.125) * G2 @ K @ G2.T
    T = 0.25 * (P * K.ravel()[None, :]) @ P.T + (grid * w[None, :]) @ grid.T
    if br == 'GR':
        T += -0.5 * (grid @ Q.T + Q @ grid.T)
    return T
rng = np.random.default_rng(3)
for phi0_kind in ('zero', 'random'):
    phi0 = np.zeros(N) if phi0_kind == 'zero' else 0.5 * rng.normal(size=N)
    u, A_s = s['slice_quantities'](phi0, L, m, idx)
    print("== phi_0 = %s ==" % phi0_kind)
    for disc in ('K2', 'D2'):
        for br in ('Newton', 'GR'):
            w = K @ (u + A_s) if br == 'GR' else K @ u
            Bm = B(disc, br, w)
            for sign, lab in ((1, 'attractive'), (-1, 'repulsive')):
                if br == 'GR' and sign < 0: continue
                row = []
                for lam in (0.01, 0.1, 1.0):
                    E_ = sign * lam * Bm; X = np.exp(E_ - E_.max())   # positive rescaling: PSD-ness unchanged
                    ev = np.linalg.eigvalsh(X); lo, hi = ev[0], ev[-1]
                    row.append("lam=%.2f min/max=%+.2e" % (lam, lo / hi))
                print("  %s-%s (%s): " % (disc, br, lab) + " | ".join(row))
            sys.stdout.flush()
