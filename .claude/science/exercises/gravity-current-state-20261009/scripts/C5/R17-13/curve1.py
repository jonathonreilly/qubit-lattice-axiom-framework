"""R17-13 curve1: Dirac rows (Xi_T2g, Xi_Eg, mu_E; archived dfam V0+SF evaluator) along the mu_T2^F = 0 curve b*(r) of D1, m = 0.01,
compared with the R17-9 VM root's Dirac point D1(0.38483, 0.55963)."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import lib13 as L
from content3 import ferm
from scipy.optimize import brentq
m = 0.01
def bstar(r, m=0.01, lo=0.3, hi=1.5):
    return brentq(lambda b: L.muT2(L.D1law(b, r), m, 4, 12), lo, hi, xtol=1e-13)
v = ferm(0.38483254, 0.55962727, m)[0]
print('VM root Dirac D1(0.38483,0.55963) per field: T2g %+.4e Eg %+.4e muE %+.4e muT2 %+.4e ; x22.5: %s' % (*v, np.array2string(22.5*v[:3], precision=4)))
for r in (0.42, 0.45, 0.48, 0.5, 0.53, 0.56, 0.5773):
    try:
        b = bstar(r)
    except ValueError:
        print('r=%.4f: no sign change on [0.3,1.5]' % r); continue
    v = ferm(b, r, m)[0]
    print('r=%.4f b*=%.6f: per field T2g %+.4e Eg %+.4e muE %+.4e muT2(arch) %+.2e | biref T2g-Eg %+.4e | x22.5 %s' % (r, b, *v, v[0]-v[1], np.array2string(22.5*v[:3], precision=4)), flush=True)
