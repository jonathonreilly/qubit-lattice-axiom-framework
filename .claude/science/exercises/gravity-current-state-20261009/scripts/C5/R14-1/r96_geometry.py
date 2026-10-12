"""R9-6, script 5: geometry of the legs.  (i) Q_max such that every leg of (P, q), |P| < Pi1, |q| < Q lies in the open
ball |k| < B (the invariant domain D2 of the d = 3 algebra; S-, W-, F-, X_NW-invariant); (ii) the direction-dependent
|P| at which some leg of (P, q), |q| <= kappa, first touches the face of the exact cube |k_a| < B (axis / face / body
diagonal) and the inscribed ball |k| < B; (iii) boost budgets at rest, cube vs ball."""
import numpy as np
m, KAP = 0.5, 0.8
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
def legs(P, q):
    w = np.sqrt(m*m + (q**2).sum(-1)); M0 = 2*w; H0 = np.sqrt(M0**2 + (P**2).sum(-1)); Pq = (P*q).sum(-1)
    k1 = q + P*(Pq/(M0*(H0 + M0)) + w/M0)[..., None]
    return k1, P - k1
rng = np.random.default_rng(5)
dirs = rng.normal(size=(20000, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
def maxleg(P, Q, norm):
    q = Q*dirs; k1, k2 = legs(np.broadcast_to(P, q.shape), q)
    f = (lambda k: np.abs(k).max(-1)) if norm == 'cube' else (lambda k: np.linalg.norm(k, axis=-1))
    return max(f(k1).max(), f(k2).max())
B = 2.6; PI1 = 0.6
Pdirs = rng.normal(size=(200, 3)); Pdirs /= np.linalg.norm(Pdirs, axis=1)[:, None]
lo, hi = 0.0, 2.6
for _ in range(40):
    Q = 0.5*(lo + hi)
    if max(maxleg(PI1*d, Q, 'ball') for d in Pdirs[:60]) < B: lo = Q
    else: hi = Q
pr('(i) B = %.2f, Pi1 = %.2f: legs stay in the open ball |k| < B for all |P| < Pi1, |q| < Q iff Q <~ %.4f (sampled); kappa = %.2f' % (B, PI1, lo, KAP))
pr('    max |leg| over |q| <= kappa, |P| <= 1.2 (where c > 0): %.4f  (inside the inscribed ball, B = 2.6)'
   % max(maxleg(1.2*d, KAP, 'ball') for d in Pdirs))
for Bc in [1.6]:
    for lab, n in [('axis', [1, 0, 0]), ('face diagonal', [1, 1, 0]), ('body diagonal', [1, 1, 1])]:
        n = np.array(n, float)/np.linalg.norm(n)
        Ps = np.linspace(0.5, 2.6, 2101)
        for Pn in Ps:
            if maxleg(Pn*n, KAP, 'cube') >= Bc:
                pr('(ii) B = %.2f, %-14s: some leg with |q| <= kappa first touches the cube face at |P| = %.3f' % (Bc, lab, Pn)); break
    for Pn in np.linspace(0.5, 2.6, 2101):
        if maxleg(Pn*np.array([1.0, 0, 0]), KAP, 'ball') >= Bc:
            pr('(ii) B = %.2f, ball |k| < B: first touched at |P| = %.3f (every direction)' % (Bc, Pn)); break
for Bc, mm in [(2.6, 0.5), (2.6, 0.85)]:
    for lab, n in [('axis', [1, 0, 0]), ('face diagonal', [1, 1, 0]), ('body diagonal', [1, 1, 1])]:
        n = np.array(n, float)/np.linalg.norm(n)
        pr('(iii) boost budget at rest, mass %.2f, cube B = %.1f, %-14s: eta* = asinh(B/(m max|n_a|)) = %.4f' % (mm, Bc, lab, np.arcsinh(Bc/(mm*np.abs(n).max()))))
    pr('(iii) boost budget at rest, mass %.2f, ball B = %.1f, every direction: eta* = %.4f' % (mm, Bc, np.arcsinh(Bc/mm)))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
