"""(b) Crossing map. Family: sigma'_t = (1-t) sigma'_{G(b)} + t sigma'_{Zz(b,V,P=b,wt)}  (convex, |sigma'| <= 1).
For each endpoint, bisect t_E (Xi_Eg = 0) and t_T (Xi_T2g = 0) along t in [0,1]; report D = t_T - t_E.
A sign change of D across endpoints => simultaneous zero (IVT on the continuous 2-parameter family)."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz
T0 = time.time()
n = 1 << 13
def root_t(GL, ZL, m, key, nb=30):
    def val(t):
        L = Mix([GL, ZL], [1-t, t]); g, f = L.samples(n); return xi_all(g, f, m, nu=700)[key]
    a, b_ = 0.0, 1.0; fa, fb = val(a), val(b_)
    if fa*fb > 0: return np.nan
    for _ in range(nb):
        c = 0.5*(a+b_); fc = val(c)
        if fa*fc <= 0: b_, fb = c, fc
        else: a, fa = c, fc
    return 0.5*(a+b_)
for vtx in ['M', 'U']:
    for m in [0.3, 0.1]:
        for b in [0.6, 0.8, 1.0]:
            GL = ZLaw([1.0, 0.0], [b + (np.pi-b)/2], np.pi-b, nf=1 << 16)
            row = []
            for V in np.arange(0.2, b - 0.09, 0.1):
                ZL = Zz(b, V, b, 0.06)
                if ZL is None: continue
                tE = root_t(GL, ZL, m, vtx+',Eg'); tT = root_t(GL, ZL, m, vtx+',T2g')
                row.append('V=%.1f tE=%.4f tT=%.4f D=%+.4f' % (V, tE, tT, tT - tE))
            print('%s m=%.1f b=%.1f: ' % (vtx, m, b) + ' | '.join(row), flush=True)
print('runtime %.1fs' % (time.time()-T0))
