"""V1: energy denominators of the O(lambda) (and O(lambda^2)) momentum-correction sectors, lattice KG on Z^3.
 0<->4 : D = sum of 4 w >= 4m                                  (trivial)
 1<->3 : D = w1+w2+w3 - w(k1+k2+k3)   PROVED >= sqrt(9m^2+X^2)-sqrt(m^2+X^2) > 0, X <= 6 sqrt3 (subadditivity of
         |sin| per axis + triangle + Minkowski); checked by minimisation here.
 1<->5 : same argument, gapped.
 2<->2 : D = w1+w2-w3-w(k1+k2-k3): elastic shell non-empty; numerator N = f1+f2-f3-f4 (f = sin k) on nontrivial points.
 2<->4 : D = sum_4 w - w1 - w2: shell non-empty iff 2 w_max > 4m (inelastic threshold) -- obstructed at O(lambda^2).
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(7)
def w(k, m): return np.sqrt(m**2 + np.sum(4*np.sin(k/2)**2, axis=-1))
def D13(x, m):
    k = x.reshape(3, 3); return w(k, m).sum() - w(k.sum(0), m)
def D15(x, m):
    k = x.reshape(5, 3); return w(k, m).sum() - w(k.sum(0), m)
for m in [0.1, 0.3, 1.0, 1.5]:
    best = np.inf; bx = None
    for _ in range(400):
        x0 = rng.uniform(-np.pi, np.pi, 9)
        r = minimize(D13, x0, args=(m,), method='L-BFGS-B')
        if r.fun < best: best, bx = r.fun, r.x
    bound = np.sqrt(9*m**2 + 108) - np.sqrt(m**2 + 108)
    best5 = np.inf
    for _ in range(150):
        r = minimize(D15, rng.uniform(-np.pi, np.pi, 15), args=(m,), method='L-BFGS-B')
        best5 = min(best5, r.fun)
    print(f'm={m:4.2f}: 1<->3 min D = {best:.5f} (proved lower bound {bound:.5f}; minimiser k = {np.round(bx.reshape(3,3)/np.pi,3).tolist()} pi) | 1<->5 min D = {best5:.5f}')
# 2<->2 nontrivial resonances and the numerator there (m = 1, 0.3)
from scipy.optimize import brentq
for m in [1.0, 0.3]:
    Ns = []; cnt = 0
    while cnt < 4000:
        k1, k2, k3 = rng.uniform(-np.pi, np.pi, (3, 3)); d = rng.normal(size=3); d /= np.linalg.norm(d)
        g = lambda s: w(k1, m) + w(k2, m) - w(k3 + s*d, m) - w(k1 + k2 - k3 - s*d, m)
        ss = np.linspace(-np.pi, np.pi, 61); gv = np.array([g(s) for s in ss])
        idx = np.where(np.sign(gv[:-1]) != np.sign(gv[1:]))[0]
        if len(idx) == 0: continue
        s0 = brentq(g, ss[idx[0]], ss[idx[0]+1]); q3 = k3 + s0*d; q4 = k1 + k2 - q3
        # skip near-trivial (permutation) resonances
        dist = min(np.linalg.norm(np.angle(np.exp(1j*(q3 - k1)))) + np.linalg.norm(np.angle(np.exp(1j*(q4 - k2)))),
                   np.linalg.norm(np.angle(np.exp(1j*(q3 - k2)))) + np.linalg.norm(np.angle(np.exp(1j*(q4 - k1)))))
        if dist < 0.3: continue
        N = np.sin(k1) + np.sin(k2) - np.sin(q3) - np.sin(q4)
        Ns.append(np.linalg.norm(N)); cnt += 1
    Ns = np.array(Ns)
    print(f'm={m}: 2<->2 nontrivial elastic resonances sampled {len(Ns)}: |sum f_in - sum f_out| median {np.median(Ns):.3f}, '
          f'10th pct {np.percentile(Ns,10):.3f}, min {Ns.min():.2e}  -> numerator nonzero on the shell where D=0')
    print(f'      2<->4 threshold: 2 w_max = {2*np.sqrt(m**2+12):.3f} vs 4m = {4*m:.3f} -> inelastic 2->4 shell '
          f'{"NON-EMPTY" if 2*np.sqrt(m**2+12) > 4*m else "empty"}; 3<->3 elastic shell always non-empty')
