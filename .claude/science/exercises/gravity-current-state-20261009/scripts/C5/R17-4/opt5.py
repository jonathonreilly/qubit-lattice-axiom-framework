"""R17-4 (b): direct least-squares search for U-vertex Xi_Eg = Xi_T2g = Xi_face1 = 0 in the free-segment family P(N)
(as opt4.py), from structured starts (zigzags with flats at the turns) and random ternary starts.
Usage: python3 opt5.py m N b wt nstarts seed"""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw
from fastU import rowsU
from scipy.optimize import least_squares
m = float(sys.argv[1]); N = int(sys.argv[2]); b = float(sys.argv[3]); wt = float(sys.argv[4]); NS = int(sys.argv[5]); seed = int(sys.argv[6])
e = 0.08; smin = 0.15; NF = 1 << 14; NN = 1 << 12; NU = 400
edges = np.linspace(b, np.pi - e, N + 1)
def law(v, nf=NF): return ZLaw([1.0] + list(v) + [0.0], list(edges), wt, 'P', nf=nf)
cache = {}
def get(v, nn=NN, nu=NU, nf=NF):
    key = (tuple(np.round(v, 13)), nn, nu, nf)
    if key not in cache:
        L = law(v, nf); g, f = L.samples(nn); R = rowsU(g, f, m, nu=nu, shear=True)
        cache[key] = (np.array([R['Eg'], R['T2g'], R['face1']]), R, L)
    return cache[key]
def floor(v): L = get(v)[2]; return np.minimum((L.sig[L.k >= b] - smin)[::128], 0)
def res(v): return np.concatenate([1e4*get(v)[0], 1e2*floor(v)])
pats = [[-1, 0, 1, 0], [-1, 0, 0, 1, 0, 0], [-1, -1, 0, 1, 1, 0], [-1, 0, 0, 0, 1, 0, 0, 0], [-1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, 0]]
rng = np.random.default_rng(seed); T0 = time.time(); best = None
for s in range(NS):
    if s < len(pats): v0 = np.array([pats[s][j % len(pats[s])] for j in range(N)], float)
    else: v0 = rng.choice([-1.0, 0.0, 1.0], N, p=[0.35, 0.35, 0.3])
    for it in range(60):
        if (floor(v0) >= 0).all(): break
        v0 = np.clip(v0 + 0.15, -1, 1)
    X0 = get(v0)[0]
    r = least_squares(res, v0, bounds=(-1, 1), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=300, diff_step=1e-6)
    v = r.x; X, R, L = get(v)
    print('start %d: start rows %s -> Eg %+.3e T2g %+.3e face1 %+.3e (K6row %+.3e mu_E %+.3e) floor-viol %.1e cost %.2e nfev %d (%.0fs) v=%s'
          % (s, np.array2string(X0, precision=2), *X, R['K6row'], R['mu_E'], -floor(v).min() if len(floor(v)) else 0, r.cost, r.nfev, time.time()-T0, np.round(v, 3).tolist()), flush=True)
    if best is None or r.cost < best[0]: best = (r.cost, v.copy())
c, v = best; X, R, L = get(v, nn=1 << 15, nu=2000, nf=1 << 17)
print('BEST (refined nf=2^17, nn=2^15, nu=2000): Eg %+.3e T2g %+.3e face1 %+.3e K6row %+.3e mu_E %+.4e vmax %.6f max|sp| %.9f min edge g %.4f v=%s'
      % (*X, R['K6row'], R['mu_E'], L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= b]**2).min(), np.round(v, 6).tolist()))
np.save('opt5_best_m%g_N%d_b%g.npy' % (m, N, b), v)
print('runtime %.0fs' % (time.time()-T0))
