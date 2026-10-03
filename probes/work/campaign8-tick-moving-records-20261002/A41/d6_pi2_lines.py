"""A41 d6: pi flux, theta = pi/2: the zeros of H6 (pairs, PHS C^2 = -1). For 20 zeros from random starts: singular
values of the first-order condition matrix D (3 x 4); for rank-2 zeros, |E|min along the null direction n of D
(E ~ delta^2 means the zero continues as a line, E ~ delta means it does not) and along the two other directions;
then track one line by predictor-corrector over 200 steps of 0.02 and report its closure/period."""
import os, signal
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from scipy.optimize import minimize
from common import *
rng = np.random.default_rng(23)
PAU = [np.eye(2), SIG[0], SIG[1], SIG[2]]
M = M_family(np.pi / 2)
f = lambda kk: np.abs(np.linalg.eigvalsh(H6(kk, M))).min()
def Dmat(k0):
    e, V = np.linalg.eigh(H6(k0, M)); P = V[:, np.argsort(np.abs(e))[:2]]
    A = [(P.conj().T @ ((H6(k0 + 1e-6 * E3[j], M) - H6(k0 - 1e-6 * E3[j], M)) / 2e-6) @ P) for j in range(3)]
    return np.array([[np.real(np.trace(Pm @ Aj)) / 2 for Pm in PAU] for Aj in A])
stats = []
for _ in range(30):
    r = minimize(f, rng.uniform(-np.pi, np.pi, 3), method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-16, maxiter=2500))
    if r.fun > 1e-10: continue
    k0 = r.x; D = Dmat(k0); U, sv, Vt = np.linalg.svd(D)
    n = U[:, 2] if sv[2] < 1e-3 * sv[0] else U[:, np.argmin(sv)]   # direction in k with the weakest first-order change
    along = [f(k0 + d * n) for d in (1e-3, 1e-2)]
    perp = [min(f(k0 + d * u) for u in (U[:, 0], U[:, 1])) for d in (1e-3, 1e-2)]
    stats.append((sv[0], sv[1], sv[2], along[0], along[1], perp[0], perp[1]))
st = np.array(stats); r2 = st[:, 2] < 1e-6; r3 = ~r2
print(f"{len(st)} zeros: {r2.sum()} with first-order rank 2 (s3 < 1e-6), {r3.sum()} with rank 3 (s3 {st[r3,2].min() if r3.any() else 0:.2f}..{st[r3,2].max() if r3.any() else 0:.2f})")
if r2.any():
    print(f"  rank-2 zeros: |E|min along the null direction at delta=1e-3, 1e-2: max {st[r2,3].max():.1e}, {st[r2,4].max():.1e}; "
          f"along the other two directions: min {st[r2,5].min():.1e}, {st[r2,6].min():.1e}")
if r3.any():
    print(f"  rank-3 zeros: |E|min along the weakest direction at delta=1e-3, 1e-2: min {st[r3,3].min():.1e}, {st[r3,4].min():.1e} (linear -> isolated point)")
# track a line from a rank-2 zero that is not a high-symmetry point
for attempt in range(30):
    r = minimize(f, rng.uniform(-np.pi, np.pi, 3), method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-16, maxiter=2500))
    if r.fun < 1e-10 and np.linalg.svd(Dmat(r.x), compute_uv=False)[2] < 1e-6: break
k = r.x.copy(); start = k.copy(); n = np.linalg.svd(Dmat(k))[0][:, 2]; path = [k.copy()]; worst = 0.0
for step in range(150):
    kp = k + 0.02 * n
    U = np.linalg.svd(Dmat(kp))[0]; nn = U[:, 2]; nn = nn if nn @ n > 0 else -nn
    g = lambda c: f(kp + c[0] * U[:, 0] + c[1] * U[:, 1])
    rr = minimize(g, np.zeros(2), method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-16, maxiter=600))
    k = kp + rr.x[0] * U[:, 0] + rr.x[1] * U[:, 1]; n = nn; worst = max(worst, rr.fun); path.append(k.copy())
path = np.array(path)
print(f"  tracked a line from a rank-2 zero at k/pi {np.round(start/np.pi,4)}: 150 steps of 0.02, max |E|min on it {worst:.1e}; "
      f"end k/pi {np.round(path[-1]/np.pi,4)}; extent /pi {np.round((path.max(0)-path.min(0))/np.pi,3)}")
