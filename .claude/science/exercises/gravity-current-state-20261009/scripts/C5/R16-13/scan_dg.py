"""R16-13: coarse scan of the Dirac DG(b, w, r) family at m = 0.01 (per 4-comp Dirac): Xi_F (T2g, Eg), mu_E^F, mu_T2^F.
Also the scalar G_w(1.4, w) values (per real scalar, M vertex) by R16-3's zz.py Laplace evaluator."""
import numpy as np, time, sys
import dfam
from zz import ZLaw, xi_all, mu_E
t0 = time.time(); m = 0.01
print('scalar G_w(1.4, w), m=%.2f, per real scalar (M vertex): w | Xi_M,T2g | Xi_M,Eg | Xi_U,T2g | Xi_U,Eg | mu_E' % m)
for w in (np.pi-1.4, 1.0, 0.6, 0.4, 0.3444, 0.2):
    L = ZLaw([1.0, 0.0], [1.4 + w/2], w)
    g, f = L.samples(1 << 14)
    x = xi_all(g, f, m, nu=1500); mu = mu_E(g, f, m, nu=1500)
    print('  %.4f | %+.4e | %+.4e | %+.4e | %+.4e | %+.4e' % (w, x['M,T2g'], x['M,Eg'], x['U,T2g'], x['U,Eg'], mu), flush=True)
print('Dirac DG(b, w, r), m=%.2f, per 4-comp field: b w r | Xi_T2g | Xi_Eg | a-term | mu_E^F | mu_T2^F | W_pi' % m)
for b in (0.6, 0.9, 1.2):
    for w in (0.1, 0.2, 0.35, (np.pi/2 - b)):
        if b + w > np.pi/2 + 1e-12: continue
        for r in (0.1, 0.3, 0.5):
            L = dfam.DG(b, w, r)
            o = dfam.evaluate(L, m, 3, 8)
            print('  %.2f %.3f %.2f | %+.4e | %+.4e | %+.4e | %+.4e | %+.4e | %.3f' % (b, w, r, o['T2g'], o['Eg'], o['a'], o['muE'], o['muT2'], L.Wpi), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
