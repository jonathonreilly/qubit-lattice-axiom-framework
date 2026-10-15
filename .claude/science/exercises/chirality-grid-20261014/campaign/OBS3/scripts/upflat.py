"""OBS-3 R2b: minimum of the FIXED-row ratio restricted to 'up sector flat' (W_u = F P_g D_g, X_u = W_u: Hermitian
circulant up texture, corner-universal up data). Free: P_g (6), D_g (2 phases), X_d (U(3)), split, placement, carrier.
Objective per realisation = max over bracket (m0 x Delta, N = 96) of the fixed-row ratio (PREREG rule 4);
also the per-variant ('tuned') minimum at the primary point."""
import numpy as np, itertools, time, sys
from scipy.optimize import minimize
from scipy.linalg import expm
from obs3_core import *
P = print; t0 = time.time()
V = INPUTS['pdg24']['V']
TABS = {(m, D): get_tabs(96, m, D) for (m, D) in BRACKET}
def perm(p):
    M = np.zeros((3, 3)); M[np.arange(3), p] = 1; return M
GEN = []
for a in range(3):
    for b in range(3):
        H = np.zeros((3, 3), complex)
        if a == b: H[a, a] = 1
        elif a < b: H[a, b] = H[b, a] = 1
        else: H[a, b] = 1j; H[b, a] = -1j
        GEN.append(H)
def unitary(x):
    return expm(1j * sum(xi * G for xi, G in zip(x, GEN)))
def realisation(pg, x, car, var, split):
    Wu = F @ perm(pg) @ np.diag(np.exp(1j * np.array([0, x[0], x[1]])))
    Xd = unitary(x[2:11])
    return dict(Wu=Wu, Xu=Wu, Xd=Xd, carrier=car, var=var, y0mode=split)
def obj(x, pg, car, var, split, keys):
    real = realisation(pg, x, car, var, split)
    return max(fixed_ratio(evaluate(real, TABS[k]))[0] for k in keys)
def dfirst_flat_dev(pg, x):
    Wd = realisation(pg, x, 'M1', 'sym', 'trace')['Wu'] @ V
    return np.abs(np.abs(Wd[:, 0])**2 - 1 / 3).max()
# analytic bound check: min over D_g, P_g of the d-column non-flatness
mins = []
for pg in itertools.permutations(range(3)):
    for p1 in np.linspace(0, 2 * np.pi, 61):
        for p2 in np.linspace(0, 2 * np.pi, 61):
            mins.append(dfirst_flat_dev(pg, [p1, p2]))
P(f"up-flat: min over P_g, D_g of max_c ||W_d,c1|^2 - 1/3| = {min(mins):.4f} (proved bound >= 0.121 in REPORT)")
rng = np.random.default_rng(11)
prim = ('0.025', '0.5')
results = []
for car in ('M1', 'M2'):
    for split in ('trace', 'selective'):
        for var in ('sym', 'int', 'ext'):
            best_rb, best_tu = None, None
            for pg in itertools.permutations(range(3)):
                for start in range(2):
                    x0 = rng.uniform(-np.pi, np.pi, 11)
                    # tuned: primary variant only
                    r1 = minimize(obj, x0, args=(pg, car, var, split, [prim]), method='Powell', options=dict(maxiter=3000, xtol=1e-6, ftol=1e-12))
                    # bracket-robust: max over the six (m0, Delta) points, started from the tuned optimum
                    r2 = minimize(obj, r1.x, args=(pg, car, var, split, BRACKET), method='Powell', options=dict(maxiter=3000, xtol=1e-6, ftol=1e-12))
                    if best_tu is None or r1.fun < best_tu[0]: best_tu = (r1.fun, pg, r1.x)
                    if best_rb is None or r2.fun < best_rb[0]: best_rb = (r2.fun, pg, r2.x)
            results.append((car, split, var, best_tu, best_rb))
            P(f"{car} {split:9s} {var}: tuned (primary point) min ratio {best_tu[0]:.3e} [P_g {best_tu[1]}];  bracket-robust min ratio {best_rb[0]:.3e} [P_g {best_rb[1]}]  ({time.time()-t0:.0f}s)", flush=True)
np.save('upflat_results.npy', np.array([(r[0], r[1], r[2], r[3][0], r[4][0], list(r[4][1]), list(r[4][2])) for r in results], dtype=object), allow_pickle=True)
