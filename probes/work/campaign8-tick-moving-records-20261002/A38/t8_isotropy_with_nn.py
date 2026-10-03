"""A38 t8 (isotropy with NN hops held nonzero; sublattice decoupling at the NN-free optimum): (i) NN hops in the record-calm subfamily; (ii) can any calm star-local law make the zone-corner
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
# NN hop functional over the calm family (rank 1): the hop 0 -> e_x
def nn_of(wv):
    c = N @ wv
    return sum(ci * amp for ci, tlb in zip(c, per) for a, b, d, amp, Si, Sj in tlb
               if a == 0 and tuple(int(v) for v in d) == (1, 0, 0))
nu = np.array([nn_of(N[:, j] * 0 + np.eye(N.shape[1])[j]) if False else nn_of(np.eye(N.shape[1])[j]) for j in range(N.shape[1])])
print("NN hop 0->e_x over the 24 calm directions: |max| =", round(float(np.max(np.abs(nu))), 4), "; phase of nonzero entries/pi:",
      sorted(set(np.round(np.angle(nu[np.abs(nu) > 1e-9]) / np.pi % 1, 6))))
nuP = nu @ P0                                    # NN hop on the corner-level-0 family
def resid2(u, target):
    w = P0 @ u
    V = np.tensordot(w, Vj, axes=(0, 0))
    s = slopes(V)
    scale = np.sqrt(np.mean(s ** 2)) + 1e-12
    return np.r_[((s - s.mean(axis=0)) / scale).ravel(), 10 * (abs(nuP @ u) / scale - target)]
for target in (0.25, 0.5, 1.0):
    best = None
    for trial in range(8):
        u0 = rng.normal(size=P0.shape[1]); u0 /= np.linalg.norm(u0)
        r = least_squares(resid2, u0, args=(target,), max_nfev=300)
        val = np.linalg.norm(r.fun[:-1]) / np.sqrt(40 * 8)
        if best is None or val < best[0]:
            best = (val, r.x, r.fun[-1])
        if time.time() - t0 > 15 + 12 * (target > 0.3) + 12 * (target > 0.6):
            break
    print(f"corner level 0, NN hop / rms slope fixed at {target}: smallest relative slope spread {best[0]:.3e} (constraint residual {best[2]:.1e})")
# decoupling at the isotropic optimum (NN = 0): even/odd sites
w = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "t6_best_w.npy"))
c = N @ w
tl = [(a, b, d, ci * amp, Si, Sj) for ci, tlb in zip(c, per) if abs(ci) > 1e-14 for a, b, d, amp, Si, Sj in tlb]
par = np.array([sum(x) % 2 for x in CELL])
cross = max([abs(amp) for a, b, d, amp, _, _ in tl if par[a] != par[b]] + [0])
print(f"isotropic optimum: largest hop between even and odd sites {cross:.2e} (decoupled into two fcc sublattices)")
for p in (0, 1):
    idx = np.where(par == p)[0]
    sl = []
    for q in dirs[:10]:
        h1 = bloch_batch(tl, (kR + 1e-4 * q)[None, :])[0][np.ix_(idx, idx)]
        sl.append(np.round(np.linalg.eigvalsh(h1) / 1e-4, 3))
    print(f"  sublattice parity {p}: slopes of its 4 modes at the corner (10 directions): {np.unique(np.array(sl), axis=0).tolist()}")
print(f"time {time.time() - t0:.1f} s")
