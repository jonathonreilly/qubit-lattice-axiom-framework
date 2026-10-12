"""Scan 1: (i) heavy-mass loophole for R9-2's literal edge L (odd s, B=2, B2=3.1);
(ii) non-monotone even laws with an edge valley (|sigma'| <= 1, subluminal for every m);
(iii) monotone terrace laws (0 <= sigma' <= 1);  (iv) massive-slack laws (sigma' up to 1+delta)."""
import numpy as np, time, sys
sys.path.insert(0, '.')
from prof import *
T0 = time.time()
class LawF(Law):
    def __init__(self, fn, b, name):
        self.fn = fn; super().__init__([1.0], [b], [1.0], name)
    def dsig(self, k):
        return self.fn(np.asarray(k, float))
# R7-1/R8-2 literal edge: s = rho k + (1-rho) sin k, rho = sstep((B2-|k|)/(B2-B))
Bq, B2q = 2.0, 3.1
def dsL(k):
    h = 1e-6
    sL = lambda x: sstep((B2q-x)/(B2q-Bq))*x + (1-sstep((B2q-x)/(B2q-Bq)))*np.sin(x)
    return (sL(k+h) - sL(k-h))/(2*h)
L = LawF(dsL, Bq, 'L(2,3.1)')
def report(law, ms, N=160, xi=True):
    print('== %s: A range [%.3f, %.3f]; sigma on edge [%.3f, %.3f]; sigma(pi)=%.4f' % ((law.name,) + law.Amax()[::-1] + law.sig_minmax_edge() + (law.sig_pi,)), flush=True)
    for m in ms:
        v = law.vmax(m); a, b = mu_E(law, m, N)
        line = '   m=%.2f v_max(d=3)=%.4f mu_E=%+.5e (A-form %+.5e)' % (m, v, b, a)
        if xi:
            X = Xi(law, m, N)
            line += ' | Xi ' + ' '.join('%s %+.4e' % (vv, x[1]) for vv, x in X.items())
        print(line, flush=True)
print('--- (i) literal edge L at heavy mass ---')
report(L, [1.0, 2.0, 3.0, 4.0, 6.0])
print('--- (ii) edge-valley laws: sigma: 1 -> -1 at b (w1), -1 -> +1 at a2 (w2), +1 -> 0 at a3 (to pi) ---')
for (b, w1, a2, w2) in [(1.4, 0.3, 1.9, 0.15), (1.4, 0.3, 2.1, 0.15), (1.4, 0.3, 2.3, 0.1), (1.4, 0.2, 2.0, 0.05), (1.0, 0.3, 1.8, 0.1), (1.4, 0.4, 2.6, 0.1)]:
    a3 = a2 + w2 + 0.05; w3 = np.pi - a3
    law = Law([1.0, -1.0, 1.0, 0.0], [b, a2, a3], [w1, w2, w3], 'valley(b=%.1f,w1=%.2f,a2=%.2f,w2=%.2f)' % (b, w1, a2, w2))
    report(law, [0.1, 0.3, 1.0])
print('--- (iii) monotone terrace laws: sigma 1 -> 0 at b (w1), 0 -> 1 at a2 (w2), 1 -> 0 at a3 (to pi) ---')
for (b, w1, a2, w2, a3) in [(1.4, 0.2, 2.2, 0.1, 2.6), (1.0, 0.2, 1.8, 0.1, 2.6), (0.6, 0.2, 1.5, 0.1, 2.7), (1.4, 0.1, 2.6, 0.05, 2.9)]:
    w3 = np.pi - a3
    law = Law([1.0, 0.0, 1.0, 0.0], [b, a2, a3], [w1, w2, w3], 'terrace(b=%.1f,a2=%.1f,a3=%.1f)' % (b, a2, a3))
    report(law, [0.1, 0.3, 1.0])
print('runtime %.1fs' % (time.time()-T0))
