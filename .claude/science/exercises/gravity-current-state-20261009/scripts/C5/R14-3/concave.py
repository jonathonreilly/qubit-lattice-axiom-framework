"""Delineation test for (a): concave edges (sigma' nonincreasing from 1 to 0 on [b, pi], even g; G-type) --
is mu_E > 0 throughout?  Random nonincreasing node values, b in {0.4, 0.6, 1.0, 1.4, 2.0, 2.6}, m in {0.1, 1}."""
import numpy as np, sys, time
sys.path.insert(0, '.')
from prof import *; from lap import *
T0 = time.time()
rng = np.random.default_rng(7)
def make(b, c, nfine=40001):
    K = len(c); a = np.linspace(b, np.pi, K+2)[:-1]; w = a[1]-a[0]
    vals = [1.0] + list(c) + [0.0]; starts = list(a); widths = [w]*(K+1); widths[-1] = np.pi - a[-1]
    return Law(vals, starts, widths, 'concave', nfine=nfine)
mins = {}
for b in [0.4, 0.6, 1.0, 1.4, 2.0, 2.6]:
    worst = (1e9, None)
    for trial in range(30):
        K = rng.integers(2, 9)
        c = np.sort(rng.uniform(0, 1, K))[::-1]
        if trial % 3 == 0: c = np.sort(rng.uniform(0, 1, K)**4)[::-1]       # fast drops
        if trial % 3 == 1: c = np.sort(1 - rng.uniform(0, 1, K)**4)[::-1]   # late drops
        law = make(b, c)
        for m in [0.1, 1.0]:
            mu = evaluate(law, m, n=1 << 13, nu=700)[0]
            if mu < worst[0]: worst = (mu, m, np.round(c, 3))
    print('b=%.1f: min mu_E over 30 concave edges x m in {0.1,1}: %+.4e at m=%.1f c=%s' % (b, worst[0], worst[1], worst[2]), flush=True)
print('runtime %.1fs' % (time.time()-T0))
