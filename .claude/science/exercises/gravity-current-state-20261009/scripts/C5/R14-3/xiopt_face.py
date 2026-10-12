"""(b), strict 'face-gapped' sub-class: |sigma'| <= 1 AND sigma >= b on the whole edge (every edge state above the
box-face energy sqrt(m^2+b^2), R8-2's ceiling), but with an interior valley of g.  Maximize Xi_{M,Eg} and Xi_{U,Eg}
(and T2g) at m = 0.1 by random search + Nelder-Mead with a hard constraint."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
from scipy.optimize import minimize
T0 = time.time()
rng = np.random.default_rng(143)
def make(b, c, name='node', nfine=40001):
    K = len(c); a = np.linspace(b, np.pi, K+2)[:-1]; w = a[1]-a[0]
    vals = [1.0] + list(c) + [0.0]; starts = list(a); widths = [w]*(K+1); widths[-1] = np.pi - a[-1]
    return Law(vals, starts, widths, name, nfine=nfine)
def val(b, c, v, m=0.1, fine=False):
    law = make(b, c)
    if law.sig_minmax_edge(20001)[0] < b - 1e-9: return -1.0, law
    mu, X = evaluate(law, m, n=(1 << 15) if fine else (1 << 13), nu=2500 if fine else 700)
    return X[v], law
for b in [1.0, 1.4]:
    for v in ['M,Eg', 'U,Eg', 'M,T2g']:
        K = 8; best = (-1e9, None)
        for trial in range(60):
            c = rng.uniform(-1, 1, K)
            x = val(b, c, v)[0]
            if x > best[0]: best = (x, c)
        obj = lambda z: -val(b, np.tanh(z), v)[0]*1e3
        r = minimize(obj, np.arctanh(np.clip(best[1], -0.999, 0.999)), method='Nelder-Mead', options={'maxfev': 300})
        c = np.tanh(r.x); x, law = val(b, c, v, fine=True)
        lo, hi = law.sig_minmax_edge()
        kk = np.linspace(b, np.pi, 20001); s = law._s(kk); g = s*s
        nmin = int(np.sum((g[1:-1] < g[:-2]) & (g[1:-1] <= g[2:])))
        print('b=%.1f %-6s face-gapped: random %+.4e -> NM %+.4e (fine %+.5e) | sigma_edge [%.4f, %.3f], #edge local minima of g = %d, v_max(m=0.1)=%.4f c=%s (%.0fs)'
              % (b, v, best[0], -r.fun/1e3, x, lo, hi, nmin, law.vmax(0.1), np.array2string(c, precision=3), time.time()-T0), flush=True)
