"""A41 d7: pi flux, theta = pi/2: the isolated (first-order rank 3) zeros of H6: positions, and the slopes of the 4 of
12 minimal-cell bands (spec H6 + spec(-H6)) that meet there, over 300 directions at q = 1e-5 and 1e-3."""
import os, signal
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from scipy.optimize import minimize
from common import *
rng = np.random.default_rng(29)
PAU = [np.eye(2), SIG[0], SIG[1], SIG[2]]
M = M_family(np.pi / 2)
f = lambda kk: np.abs(np.linalg.eigvalsh(H6(kk, M))).min()
def wrap(k): return (k + np.pi) % (2 * np.pi) - np.pi
def Dsv(k0):
    e, V = np.linalg.eigh(H6(k0, M)); P = V[:, np.argsort(np.abs(e))[:2]]
    A = [(P.conj().T @ ((H6(k0 + 1e-6 * E3[j], M) - H6(k0 - 1e-6 * E3[j], M)) / 2e-6) @ P) for j in range(3)]
    return np.linalg.svd(np.array([[np.real(np.trace(Pm @ Aj)) / 2 for Pm in PAU] for Aj in A]), compute_uv=False)
pts = []
for _ in range(60):
    r = minimize(f, rng.uniform(-np.pi, np.pi, 3), method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-16, maxiter=2500))
    if r.fun < 1e-10 and Dsv(r.x)[2] > 1e-3:
        k = wrap(r.x)
        if all(np.linalg.norm(wrap(k - q)) > 1e-5 for q in pts): pts.append(k)
print(f"isolated zeros found from 60 starts: {len(pts)} distinct; positions k/pi: {[list(np.round(p/np.pi,4)) for p in pts]}")
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
for k in pts[:4]:
    out = []
    for q in (1e-5, 1e-3):
        s = []
        for u in dirs:
            e6 = np.linalg.eigvalsh(H6(k + q * u, M)); e12 = np.sort(np.concatenate([e6, -e6])); s.append(e12[4:8] / q)
        out.append(np.array(s))
    sl = out[0]
    print(f"  k/pi {np.round(k/np.pi,4)}: 4 bands' slopes min..max: {'; '.join(f'{sl[:,j].min():.3f}..{sl[:,j].max():.3f}' for j in range(4))}; "
          f"|slope| ratio max/min of the upper pair {np.abs(sl[:,2:]).max()/np.abs(sl[:,2:]).min():.2f}; q=1e-3 vs 1e-5 max diff {np.abs(out[1]-out[0]).max():.1e}; "
          f"other bands |E| min {np.sort(np.abs(np.linalg.eigvalsh(H6(k, M))))[2]:.4f}")
