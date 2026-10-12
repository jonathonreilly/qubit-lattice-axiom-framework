"""(b) outside class U0: try to make Xi >= 0 with |sigma'| <= 1 (subluminal for every m) laws that have
gapped edge valleys (local minima of g with g > 0).  sigma' on [b, pi] = smooth (sstep) interpolation of node
values c_j in [-1, 1], last node 0 (even g needs sigma sigma'(pi) = 0).  Maximize each Xi_v at m = 0.1 by random
search + Nelder-Mead in the node values (tanh-bounded).  Laplace evaluator (lap.py), coarse; best re-evaluated fine."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
from scipy.optimize import minimize
T0 = time.time()
rng = np.random.default_rng(14)
def make(b, c, name='node'):
    K = len(c); a = np.linspace(b, np.pi, K+2)[:-1]; w = a[1]-a[0]
    vals = [1.0] + list(c) + [0.0]
    starts = [a[j] for j in range(K+1)]; widths = [w]*(K+1)
    starts[-1] = a[-1]; widths[-1] = np.pi - a[-1]
    return Law(vals, starts, widths, name, nfine=40001)
def xi(b, c, v, m=0.1, fine=False):
    law = make(b, c)
    mu, X = evaluate(law, m, n=(1 << 15) if fine else (1 << 13), nu=2500 if fine else 700)
    return X[v], mu, law
for b in [0.8, 1.4]:
    for v in ['M,T2g', 'M,Eg', 'U,T2g', 'U,Eg']:
        K = 8
        best = (-1e9, None)
        for trial in range(40):
            c = rng.uniform(-1, 1, K)
            x = xi(b, c, v)[0]
            if x > best[0]: best = (x, c)
        obj = lambda z: -xi(b, np.tanh(z), v)[0]*1e3
        z0 = np.arctanh(np.clip(best[1], -0.999, 0.999))
        r = minimize(obj, z0, method='Nelder-Mead', options={'maxfev': 250, 'xatol': 1e-3, 'fatol': 1e-6})
        c = np.tanh(r.x); x, mu, law = xi(b, c, v, fine=True)
        lo, hi = law.sig_minmax_edge()
        print('b=%.1f %-6s random best %+.4e -> NM %+.4e (fine %+.5e) | v_max(d=3,m=0.1)=%.4f sigma_edge [%.3f, %.3f] c=%s  (%.0fs)'
              % (b, v, best[0], -r.fun/1e3, x, law.vmax(0.1), lo, hi, np.array2string(c, precision=3), time.time()-T0), flush=True)
print('runtime %.1fs' % (time.time()-T0))
