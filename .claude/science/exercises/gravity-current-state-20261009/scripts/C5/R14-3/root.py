"""(a) REFUTATION witness and shear-cancelling subluminal edge.
E1 = terrace at b = 0.6; E2 = terrace at b = 1.4 (sharp).  Family sigma'_t = (1-t) sigma'_{G(1.4)} + t sigma'_{E2}:
0 <= sigma'_t <= 1, sigma'_t = 1 on [0, 1.4]  =>  subluminal for every m, every d (R14-1 G-form bound, refereed).
mu_E(t=0) > 0 > mu_E(t=1): intermediate-value root t*(m) = a subluminal law with mu_E = 0."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
E1 = Law([1.0, 0.0, 1.0, 0.0], [0.6, 1.5, 2.7], [0.2, 0.1, np.pi-2.7], 'E1=terrace(b=0.6;w1=0.2,a2=1.5,w2=0.1,a3=2.7)')
E2 = Law([1.0, 0.0, 1.0, 0.0], [1.4, 2.85, np.pi-0.05], [0.05, 0.05, 0.05], 'E2=terrace(b=1.4;w1=0.05,a2=2.85,w2=0.05,w3=0.05)')
G = G_law(1.4)
class Mix(Law):
    def __init__(self, t):
        self.t = t; super().__init__([1.0], [1.4], [1.0], 'mix(t=%.6f)' % t)
    def dsig(self, k):
        return (1-self.t)*G.dsig(k) + self.t*E2.dsig(k)
for law in [E1, E2]:
    print('== %s  sigma(pi)=%.4f  A in [%.2f, %.2f]  min sigma\' on [0,pi] = %.3e, max = %.6f' % (law.name, law.sig_pi, *law.Amax()[::-1], law.dsig(np.linspace(0, np.pi, 100001)).min(), law.dsig(np.linspace(0, np.pi, 100001)).max()), flush=True)
    for m in [1.0, 0.3, 0.1, 0.01]:
        mu, X = evaluate(law, m); mu2, _ = evaluate(law, m, n=1 << 17, nu=5000, umin=-22)
        print('   m=%.2f v_max(d=3)=%.5f mu_E=%+.6e (refined %+.6e) | Xi ' % (m, law.vmax(m), mu, mu2) + ' '.join('%s %+.4e' % (v, x) for v, x in X.items()), flush=True)
def mu_t(t, m):
    return evaluate(Mix(t), m, n=1 << 15, nu=1500)[0]
for m in [1.0, 0.3, 0.1, 0.01]:
    a, b_ = 0.0, 1.0; fa, fb = mu_t(a, m), mu_t(b_, m)
    for _ in range(30):
        c = 0.5*(a+b_); fc = mu_t(c, m)
        if np.sign(fc) == np.sign(fa): a, fa = c, fc
        else: b_, fb = c, fc
    ts = 0.5*(a+b_); law = Mix(ts)
    mu_ref, X = evaluate(law, m, n=1 << 17, nu=5000, umin=-22)
    print('root m=%.2f: t* = %.6f  mu_E(t*) refined = %+.2e  [mu_E(0) = %+.4e, mu_E(1) = %+.4e]  v_max(d=3) = %.5f  Xi: ' % (m, ts, mu_ref, mu_t(0, m), mu_t(1, m), law.vmax(m)) + ' '.join('%s %+.3e' % (v, x) for v, x in X.items()), flush=True)
print('runtime %.1fs' % (time.time()-T0))
