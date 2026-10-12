"""Theorem B check: I(B) = int A (B+g)^{-5/2} dk (A-form) = int (5f^2-(B+g))(B+g)^{-7/2} dk (IBP form), against the
piecewise-monotone bound  I/2 <= sum_pieces [F(h_hi) - F(h_lo)],  F(x) = -x (B+x^2)^{-5/2}  (unimodal pieces => < 0)."""
import numpy as np, sys
sys.path.insert(0, '.')
from prof import *; from lap import *
exec(open('wit_b.py').read().split('for law in [W14, W08]:')[0].split('T0 = time.time()')[1])
exec(open('root.py').read().split('for law in [E1, E2]:')[0].split('T0 = time.time()')[1])
F = lambda x, B: -x*(B+x*x)**-2.5
def bound(law, B, n=400001):
    k = np.linspace(0, np.pi, n); h = np.abs(law._s(k))
    d = np.sign(np.diff(h)); d[d == 0] = 0
    # monotone pieces: sum over sign changes of h
    ext = [0] + [i for i in range(1, len(d)) if d[i] != 0 and d[i] != d[i-1] and d[i-1] != 0] + [n-1]
    # robust: accumulate F differences along the path
    tot = 0.0; hs = h[ext]
    for a, c in zip(hs[:-1], hs[1:]): tot += abs(F(c, B) - F(a, B)) * (1 if (c > a) == (F(c, B) > F(a, B)) else -1) if False else (F(max(a, c), B) - F(min(a, c), B))
    return 2*tot
laws = [S_law(1.4), G_law(1.4), Law([1.0, 0.0], [1.4], [0.344371], 'G_w*(1.4)'), E2, W14, W08]
for law in laws:
    rows = []
    for B in [0.0001, 0.01, 0.09, 0.3, 1.0, 3.0, 10.0]:
        Ia, Ii = IB(law, B, n=400001)
        rows.append('B=%g: %+.3e/%+.3e (bound %+.3e)' % (B, Ia, Ii, bound(law, B)))
    print('%s\n   ' % law.name + '\n   '.join(rows), flush=True)
