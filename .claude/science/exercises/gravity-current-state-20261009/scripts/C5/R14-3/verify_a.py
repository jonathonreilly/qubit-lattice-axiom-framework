"""Independent 3D-grid check (no Laplace rewriting) of the (a) witnesses, and the one-step flat-edge family
G_w(b): sigma' = 1 - sstep((k-b)/w)  (R14-1's G(b) is w = pi - b)."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
exec(open('root.py').read().split('for law in [E1, E2]:')[0].split('T0 = time.time()')[1])
for law, m in [(E2, 0.3), (Mix(0.892823), 0.3), (E1, 0.3)]:
    for N in [240, 400, 560]:
        a, b_ = mu_E(law, m, N)
        print('%s m=%.1f 3D grid N=%d: mu_E IBP form %+.6e  A-form %+.6e   (Laplace %+.6e)' % (law.name, m, N, b_, a, evaluate(law, m)[0]), flush=True)
print('--- one-step flat edges G_w(b) at m = 0.1 ---')
for b in [0.4, 0.6, 0.8, 1.0, 1.4]:
    row = []
    for w in [np.pi - b, 1.0, 0.5, 0.2, 0.1, 0.05]:
        if w > np.pi - b + 1e-12: continue
        law = Law([1.0, 0.0], [b], [w], 'G_w')
        row.append('w=%.2f %+.3e' % (w, evaluate(law, 0.1, n=1 << 15, nu=1500)[0]))
    print('b=%.1f: ' % b + ' | '.join(row), flush=True)
print('runtime %.1fs' % (time.time()-T0))
