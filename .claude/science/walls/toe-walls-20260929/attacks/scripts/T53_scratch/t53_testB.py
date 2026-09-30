"""T53 Test B: is the repo's 'upper-octant chamber law' a property of the chamber, or of the label sigma=(2,1,0)?"""
import numpy as np, math, json
from scipy.optimize import fsolve, brentq
from chart import obs, SQ, preimage
PIN = (0.657061342210, 0.933806343759, 0.715042329587)

def pin3(s12, s13, s23, perm, gamma=0.5, x0=PIN):
    def f(x):
        o = obs(x[0], x[1], x[2], gamma, perm)
        return [o['s12'] - s12, o['s13'] - s13, o['s23'] - s23]
    best = None
    for st in [x0, (0.5, 1.0, 0.8), (0.8, 0.9, 0.65), (1.1, 0.85, 0.5), (0.68, 0.928, 0.70)]:
        x, info, ier, msg = fsolve(f, list(st), xtol=1e-14, full_output=True)
        r = max(abs(v) for v in f(x))
        if r < 1e-10:
            return x, r
    return None, None

res = {}
for perm in [(2, 1, 0), (2, 0, 1)]:
    for s23 in [0.545, 0.455, 0.530, 0.470, 0.541, 0.459]:
        x, r = pin3(0.307, 0.0218, s23, perm)
        if x is None:
            print(perm, s23, 'no root found'); res[f'{perm}/{s23}'] = None; continue
        ch = x[2] + x[1] - SQ
        print(perm, 'target s23^2=%.3f' % s23, 'root (m,d,q)=(%.5f,%.5f,%.5f)' % tuple(x), 'q+d-sqrt(8/3)=%+.5f' % ch, 'chamber-interior' if ch >= 0 else 'OUTSIDE chamber')
        res[f'{perm}/{s23}'] = dict(root=[float(v) for v in x], margin=float(ch))

# threshold under each labelling via bisection in the target s23^2 on the chamber boundary
def threshold(perm, s12, s13, lo, hi):
    def g(t):
        x, r = pin3(s12, s13, t, perm)
        return None if x is None else x[2] + x[1] - SQ
    return brentq(lambda t: g(t), lo, hi, xtol=1e-12)

t210 = threshold((2, 1, 0), 0.307, 0.0218, 0.50, 0.56)
t201 = threshold((2, 0, 1), 0.307, 0.0218, 0.40, 0.50)
print('\nthreshold sigma=(2,1,0): s23^2 >= %.9f ; sigma=(2,0,1): s23^2 <= %.9f ; sum = %.12f' % (t210, t201, t210 + t201))
res['threshold_210'] = t210; res['threshold_201'] = t201
# the same chamber boundary point: (m,d,q) of the two thresholds
print('\nThe excluded band around maximal mixing, same in both labellings: (%.6f, %.6f)' % (t201, t210))
json.dump(res, open('testB_result.json', 'w'), indent=1)
