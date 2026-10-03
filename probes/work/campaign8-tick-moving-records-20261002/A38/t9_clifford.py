"""A38 t9 (can the corner point be a full 8-mode Dirac cone?): (i) NN hops in the record-calm subfamily; (ii) can any calm star-local law make the zone-corner
8-fold point a light-like (isotropic, linear) cone at zero cost?  Velocity matrices V_a = dH/dk_a at the
corner are linear in the law; minimise the direction-spread of the 8 slopes (sorted eigenvalues of q.V)
over the calm family with corner level 0; KS (A34 c7 / A31 c4) as the positive control."""
import os, sys, signal, itertools, time, functools
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import least_squares
from lib38 import *
print = functools.partial(print, flush=True)
t0 = time.time()
H8 = {r: np.array([(-1) ** r[0], (-1) ** r[1], (-1) ** r[2]], float) / np.sqrt(3) for r in CELL}
shapes = [[(0, 0, 0), (1, 0, 0)], [(1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (1, 0, 0)],
          [(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
          [(1, 0, 0), (0, 1, 0), (0, 0, 1)], [(-1, 0, 0), (0, 1, 0), (1, 0, 0)]]
basis = []
for sh in shapes:
    basis += covariant_basis(sh)
basis[0:3] = [pair_law(1, 0, 0), pair_law(0, 1, 0), pair_law(0, 0, 1)]
M, _ = calm_matrix(H8, basis)
N, S = null_space(M, tol=1e-9)
per = [onefl_terms(H8, t) for t in basis]
kR = np.array([np.pi / 2] * 3)
def VR(tl, k=kR):
    """H(k) and V_a(k) = dH/dk_a (8x8) from aggregated terms"""
    H = np.zeros((8, 8), complex); V = np.zeros((3, 8, 8), complex)
    for a, b, d, amp, _, _ in tl:
        ph = amp * np.exp(1j * np.dot(k, d))
        H[b, a] += ph
        for c in range(3):
            V[c, b, a] += 1j * d[c] * ph
    return H, V
Hj, Vj = [], []
for j in range(N.shape[1]):
    tl = [(a, b, d, cj * amp, Si, Sj) for cj, tlb in zip(N[:, j], per) if abs(cj) > 1e-14 for a, b, d, amp, Si, Sj in tlb]
    h, v = VR(tl); Hj.append(h); Vj.append(v)
Hj = np.array(Hj); Vj = np.array(Vj)
trR = np.array([np.trace(h).real / 8 for h in Hj])
P0, _ = null_space(trR[None, :], tol=1e-12)
rng = np.random.default_rng(2)
dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
def slopes(V):
    return np.array([np.linalg.eigvalsh(np.tensordot(q, V, axes=(0, 0))) for q in dirs])   # 40 x 8
def resid(u):
    w = P0 @ u
    V = np.tensordot(w, Vj, axes=(0, 0))
    s = slopes(V)
    scale = np.sqrt(np.mean(s ** 2)) + 1e-12
    return np.r_[((s - s.mean(axis=0)) / scale).ravel(), (np.linalg.norm(u) - 1.0)]
# Dirac-type (all 8 modes light-like) test: Clifford residual {V_a,V_b} - 2 delta_ab v^2 I over the corner-level-0 family
def resid3(u):
    w = P0 @ u
    V = np.tensordot(w, Vj, axes=(0, 0))
    v2 = np.real(sum(np.trace(V[a] @ V[a]) for a in range(3))) / 24 + 1e-12
    out = []
    for a in range(3):
        for b in range(a, 3):
            Aab = V[a] @ V[b] + V[b] @ V[a] - (2 * v2 if a == b else 0) * np.eye(8)
            out += list((Aab / v2).real.ravel()) + list((Aab / v2).imag.ravel())
    return np.r_[out, np.linalg.norm(u) - 1]
best = None
for trial in range(12):
    u0 = rng.normal(size=P0.shape[1]); u0 /= np.linalg.norm(u0)
    r = least_squares(resid3, u0, max_nfev=400)
    val = np.linalg.norm(r.fun[:-1]) / np.sqrt(6 * 64)
    if best is None or val < best[0]:
        best = (val, r.x)
    if time.time() - t0 > 40:
        break
w = P0 @ best[1]; V = np.tensordot(w, Vj, axes=(0, 0)); s = slopes(V)
print(f"Clifford (all-8-modes Dirac cone at the corner) residual, best of {trial+1} starts: {best[0]:.3e}")
print("slopes at that point (min/max over 40 directions):", [(round(s[:, i].min(), 3), round(s[:, i].max(), 3)) for i in range(8)])
# also: count light-like (nonzero, direction-independent) modes at the isotropic optimum of t6
w6 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "t6_best_w.npy"))
V6 = np.tensordot(w6, Vj, axes=(0, 0))
print("t6 optimum: Clifford residual", round(float(np.linalg.norm(resid3(np.linalg.lstsq(P0, w6, rcond=None)[0])[:-1]) / np.sqrt(6 * 64)), 4))
print(f"time {time.time() - t0:.1f} s")
