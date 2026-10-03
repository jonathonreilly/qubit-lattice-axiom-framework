"""A41 d4: (i) pi flux, theta = pi/2: are the E = 0 zeros the lines {k_a in {0, pi}, k_b = +-pi/2, k_c free}? min|E|
along those 24 lines and off them; (ii) zero flux, theta = pi/16 and pi/4: census of the lower-pair touchings
(70 Nelder-Mead starts from the smallest-gap grid points), their energies and slope ranges; the upper-pair
touchings are their images under k -> k + (pi,pi,pi), E -> -E (checked)."""
import os, signal, itertools
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from scipy.optimize import minimize
from common import *
rng = np.random.default_rng(5)
def wrap(k): return (k + np.pi) % (2 * np.pi) - np.pi
# (i)
M = M_family(np.pi / 2); s = np.linspace(-np.pi, np.pi, 61)
worst = 0.0; kern = set()
for a, b in itertools.permutations(range(3), 2):
    c = 3 - a - b
    for ka, kb in itertools.product((0.0, np.pi), (np.pi / 2, -np.pi / 2)):
        K = np.zeros((61, 3)); K[:, a] = ka; K[:, b] = kb; K[:, c] = s
        e = np.linalg.eigvalsh(H6(K, M)); worst = max(worst, np.sort(np.abs(e), 1)[:, 1].max())
        kern |= set(np.sum(np.abs(e) < 1e-9, 1).tolist())
print(f"(i) pi flux theta=pi/2: on the 24 lines k_a in {{0,pi}}, k_b = +-pi/2 (61 points each): 2nd smallest |E(H6)| max "
      f"{worst:.1e}; zero-mode counts of H6 seen {sorted(kern)}")
# all zeros found by random-start minimization lie on those lines?
f = lambda k: np.abs(np.linalg.eigvalsh(H6(k, M))).min()
dist = []
for _ in range(40):
    r = minimize(f, rng.uniform(-np.pi, np.pi, 3), method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-15, maxiter=1500))
    if r.fun < 1e-9:
        k = wrap(r.x); d = np.inf
        for a, b in itertools.permutations(range(3), 2):
            for ka, kb in itertools.product((0.0, np.pi), (np.pi / 2, -np.pi / 2)):
                d = min(d, np.hypot(wrap(k[a] - ka), wrap(k[b] - kb)))
        dist.append(d)
print(f"    40 random-start minimizations: {len(dist)} reached |E| < 1e-9; max distance of those zeros from the line set "
      f"{max(dist) if dist else float('nan'):.1e}")
# (ii)
for th in (np.pi / 16, np.pi / 4):
    M = M_family(th); G = grid(22)
    E = np.linalg.eigvalsh(H0(G, M)); gap = E[:, 1] - E[:, 0]
    g = lambda k: np.diff(np.linalg.eigvalsh(H0(k, M)))[0]
    pts = []
    for i in np.argsort(gap)[:70]:
        r = minimize(g, G[i], method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-15, maxiter=1500))
        if r.fun < 1e-9:
            k = wrap(r.x)
            if all(np.linalg.norm(wrap(k - q)) > 1e-4 for q in pts): pts.append(k)
    Es = np.array([np.linalg.eigvalsh(H0(k, M))[0] for k in pts])
    vals, cnt = np.unique(np.round(Es, 5), return_counts=True)
    img = max(abs(np.linalg.eigvalsh(H0(k + np.pi, M))[2] - np.linalg.eigvalsh(H0(k + np.pi, M))[1]) for k in pts)
    print(f"(ii) zero flux theta={th/np.pi:.4f} pi: {len(pts)} distinct lower-pair touchings; energies (count): "
          f"{', '.join(f'{v:+.5f} ({c})' for v, c in zip(vals, cnt))}; upper pair touches at k+(pi,pi,pi): max gap {img:.1e}")
    dirs = rng.normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    for v in vals:
        k = pts[int(np.argmin(np.abs(Es - v)))]; e0 = np.linalg.eigvalsh(H0(k, M))[0]
        sl = np.array([np.linalg.eigvalsh(H0(k + 1e-5 * u, M))[:2] - e0 for u in dirs]) / 1e-5
        sp = np.abs(sl[:, 1] - sl[:, 0])
        print(f"    E={v:+.5f} e.g. k/pi={np.round(k/np.pi,4)}: slopes band0 {sl[:,0].min():.3f}..{sl[:,0].max():.3f}, "
              f"band1 {sl[:,1].min():.3f}..{sl[:,1].max():.3f}; splitting/q min {sp.min():.3f} max {sp.max():.3f}")
