"""Simplest (a) refutation: R14-1's G-form with drop width w, G_w(b): sigma' = 1 - sstep((|k|-b)/w), b = 1.4.
0 <= sigma' <= 1 => subluminal for every m, d (R14-1 Sec.5(b) bound, refereed).  Root w*(m) of mu_E; 3D-grid check;
Xi at the root (Theorem B: must be < 0 for every vertex)."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
b = 1.4
def mu_w(w, m, fine=False):
    law = Law([1.0, 0.0], [b], [w], 'G_w(1.4, w=%.6f)' % w)
    return evaluate(law, m, n=(1 << 16) if fine else (1 << 14), nu=4000 if fine else 1200)[0], law
for m in [1.0, 0.3, 0.1, 0.01]:
    lo, hi = 0.2, 0.5
    flo, fhi = mu_w(lo, m)[0], mu_w(hi, m)[0]
    assert flo < 0 < fhi, (m, flo, fhi)
    for _ in range(32):
        c = 0.5*(lo+hi); fc = mu_w(c, m)[0]
        if fc < 0: lo = c
        else: hi = c
    w = 0.5*(lo+hi); mu, law = mu_w(w, m, fine=True)
    X = evaluate(law, m, n=1 << 16, nu=4000)[1]
    print('m=%.2f: w* = %.6f  mu_E(w*) = %+.2e (fine)  [mu_E(w=0.2) = %+.4e, mu_E(w=0.5) = %+.4e]  v_max(d=3) = %.6f  max sigma\' = %.6f  A in [%.2f, %.2f] | Xi '
          % (m, w, mu, flo, fhi, law.vmax(m), law.dsig(np.linspace(0, np.pi, 100001)).max(), *law.Amax()[::-1]) + ' '.join('%s %+.4e' % (v, x) for v, x in X.items()), flush=True)
    if m == 0.3:
        for N in [240, 400]:
            a_, b_ = mu_E(law, m, N)
            print('    3D grid N=%d at w*: mu_E IBP %+.3e, A-form %+.3e  (reference: R14-1 G(1.4) at m=0.3 = +4.252e-03)' % (N, b_, a_), flush=True)
        for w2 in [0.25, 0.35]:
            l2 = Law([1.0, 0.0], [b], [w2], 'x'); print('    w=%.2f: Laplace %+.5e, 3D grid N=400 IBP %+.5e' % (w2, evaluate(l2, m)[0], mu_E(l2, m, 400)[1]), flush=True)
print('runtime %.1fs' % (time.time()-T0))
