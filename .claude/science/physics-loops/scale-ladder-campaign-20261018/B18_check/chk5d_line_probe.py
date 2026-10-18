#!/usr/bin/env python3
"""Probe: are the 'generic' E-touchings of S2.L202.S2.L020 at E = 0 nodal lines? Follow the zero-velocity direction."""
import sys
sys.argv = sys.argv[:1]
exec(open('chk5_s2_b1.py').read().split("# ---------------- (A) S^2 family")[0])
from scipy.optimize import minimize
W = word(fS2, const(onsite("L202")), fS2, const(onsite("L020"))); E = 0.0
def gap(k): return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)[0])) - E)))
rng = np.random.default_rng(1); found = None
for _ in range(400):
    r = minimize(gap, rng.uniform(0, np.pi, 3), method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-15, maxiter=3000))
    if r.fun < 1e-10:
        Wk, d = W(r.x); e, V = np.linalg.eig(Wk); idx = np.argsort(np.abs(wrap(np.angle(e) - E)))[:2]; Q, _ = np.linalg.qr(V[:, idx]); a, B = pt(W, r.x, Q)
        u, s, vh = np.linalg.svd(B)
        if s.min() < 1e-6: found = (r.x, u[:, -1], s); break
k0, dirn, s = found
print("node", np.round(k0 / np.pi, 6), "pi; speeds", np.round(s, 6), "zero-velocity direction", np.round(dirn, 4))
# follow the line: step along dirn, re-minimise in the transverse plane
path = [k0]; k = k0.copy(); t = dirn.copy()
for step in range(40):
    kp = k + 0.02 * t
    P = np.eye(3) - np.outer(t, t)
    r = minimize(lambda y: gap(kp + P @ y), np.zeros(3), method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-15, maxiter=3000))
    knew = kp + P @ r.x
    if r.fun > 1e-8: print("line lost at step", step, r.fun); break
    t = (knew - k) / np.linalg.norm(knew - k); k = knew; path.append(k)
print(f"followed {len(path)-1} steps of 0.02 with gap < 1e-8 along the line; end point {np.round(k/np.pi,4)} pi; max gap on path {max(gap(p) for p in path):.1e}")
print(f"[{'PASS' if len(path) > 30 else 'FAIL'}] S2.L202.S2.L020 has a nodal line at its k* node quasi-energy E = 0 (point census not applicable)")
