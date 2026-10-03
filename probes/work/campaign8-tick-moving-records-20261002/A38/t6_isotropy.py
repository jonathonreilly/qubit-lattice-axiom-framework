"""A38 t6: (i) NN hops in the record-calm subfamily; (ii) can any calm star-local law make the zone-corner
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
best = None
for trial in range(12):
    u0 = rng.normal(size=P0.shape[1]); u0 /= np.linalg.norm(u0)
    r = least_squares(resid, u0, max_nfev=300)
    val = np.linalg.norm(r.fun[:-1]) / np.sqrt(40 * 8)
    if best is None or val < best[0]:
        best = (val, r.x)
    if time.time() - t0 > 40:
        break
w = P0 @ best[1]
V = np.tensordot(w, Vj, axes=(0, 0)); s = slopes(V)
print(f"(ii) calm family, corner level 0: smallest rms direction-spread of the 8 corner slopes = {best[0]:.3e} (relative)")
print(f"     slopes of the 8 modes at the optimum, min/max over 40 directions: "
      f"{[(round(s[:, i].min(), 3), round(s[:, i].max(), 3)) for i in range(8)]}")
# KS control: pi-flux NN hopping, 8 bands, Dirac point at (pi/2,pi/2,pi/2) in the same reduced-zone convention
eta = lambda x, d: [1, (-1) ** x[0], (-1) ** (x[0] + x[1])][d]
tlKS = []
for i, x in enumerate(CELL):
    for d in range(3):
        for s_ in (1, -1):
            y = np.array(x) + s_ * np.eye(3, dtype=int)[d]
            sgn = eta(x if s_ == 1 else tuple(y), d)
            tlKS.append((i, CELL.index(tuple(int(v) % 2 for v in y)), y - np.array(x), -1.0 * sgn, None, None))
hK, VK = VR(tlKS, np.zeros(3))
eK = np.linalg.eigvalsh(hK)
sK = slopes(VK)
print(f"     KS control (pi flux): levels at k=0 of this cell convention {np.round(eK, 3).tolist()}; "
      f"slope spread over directions {np.max(sK.max(axis=0) - sK.min(axis=0)):.2e}; slopes {np.round(sK[0], 3).tolist()}")
# (i) record-calm subfamily's NN hops: recompute quickly from t5's construction
print(f"time {time.time() - t0:.1f} s")
