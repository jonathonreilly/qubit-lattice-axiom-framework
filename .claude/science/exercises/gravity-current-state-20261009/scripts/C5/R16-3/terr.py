"""Corner D for the shear condition: subluminal terrace / step laws with strongly negative mu_E, and zigzag+flat hybrids."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *
NF = 1 << 16; res = []
for b in [0.3, 0.5, 0.7, 1.0]:
    for k1 in [1.2, 1.6, 2.0, 2.4]:
        for L2 in [0.3, 0.6, 0.9]:
            k2 = k1 + L2
            if k2 > np.pi - 0.1: continue
            for wt in [0.03, 0.06]:
                L = ZLaw([1.0, 0.0, 1.0, 0.0], [b, k1, k2], wt, 'T(b=%.1f,k1=%.1f,k2=%.1f,wt=%.2f)' % (b, k1, k2, wt), nf=NF)
                g, f = L.samples(1 << 13)
                X = xi_all(g, f, 0.01, nu=600); mu = mu_E(g, f, 0.01, nu=600)
                res.append((mu, L.name, X))
            # zigzag + flat hybrid: down-up once then flat
            for amp in [0.2, 0.4]:
                L = ZLaw([1.0, 0.0, -1.0, 1.0, 0.0], [b, k1, k1 + amp, k1 + 2*amp], 0.03, 'H(b=%.1f,k1=%.1f,amp=%.1f)' % (b, k1, amp), nf=NF)
                g, f = L.samples(1 << 13)
                X = xi_all(g, f, 0.01, nu=600); mu = mu_E(g, f, 0.01, nu=600)
                res.append((mu, L.name, X))
res.sort(key=lambda r: r[0])
for r in res[:10]: print('mu_E(m=0.01) %+.3e %s :: %s' % (r[0], r[1], ' '.join('%s %+.2e' % kv for kv in r[2].items())))
