"""R17-13 curve2: the mu_T2^F = 0 curve as r*(b) on D1 (m = 0.01), and Dirac rows along it."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import lib13 as L
from content3 import ferm
from scipy.optimize import brentq
m = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01
for b in (0.15, 0.2, 0.25, 0.3, 0.35, 0.385, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95):
    f = lambda r: L.muT2(L.D1law(b, r), m, 4, 12)
    rr = np.linspace(0.02, 1/np.sqrt(3), 30); v = [f(r) for r in rr]
    roots = [brentq(f, rr[i], rr[i+1], xtol=1e-13) for i in range(len(rr)-1) if v[i]*v[i+1] < 0]
    for r in roots:
        x = ferm(b, r, m)[0]
        print('m=%g b=%.3f r*=%.8f: Dirac per field T2g %+.4e Eg %+.4e muE %+.4e (arch muT2 %+.1e) | x22.5 %s' % (m, b, r, *x, np.array2string(22.5*x[:3], precision=4)), flush=True)
    if not roots: print('b=%.3f: no r-root in (0.02, 1/sqrt3]' % b)
