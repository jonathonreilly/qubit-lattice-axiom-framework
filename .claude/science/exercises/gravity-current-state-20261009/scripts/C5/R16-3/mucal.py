import numpy as np, sys; sys.path.insert(0, '.')
from zz import *; from laws import *
n = 1 << 14; kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
g = 2-2*np.cos(kk); f = np.sin(kk)
for m in [1.0, 0.3]: print('NN mu_E m=%.1f: %+.8e' % (m, mu_E(g, f, m)))
L = G(1.4); g, f = L.samples(1 << 15); print('G(1.4) mu_E m=1: %+.8e (R14-3: +3.52543170e-3), m=0.3: %+.8e (+4.25201261e-3)' % (mu_E(g, f, 1.0), mu_E(g, f, 0.3)))
for L in [G(1.0), Z1(0.06), Z1(0.15), Z1(0.25)]:
    g, f = L.samples(1 << 15)
    print(L.name, ' '.join('m=%.2f mu_E %+.4e' % (m, mu_E(g, f, m)) for m in [1.0, 0.3, 0.1, 0.01]), '| Xi m=0.3', ' '.join('%s %+.3e' % kv for kv in xi_all(g, f, 0.3).items()))
