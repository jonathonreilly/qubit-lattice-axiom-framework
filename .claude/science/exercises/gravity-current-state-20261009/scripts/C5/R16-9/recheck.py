"""R16-9 recheck of archived R16-3 numbers (zz.py copied unmodified)."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz
T0 = time.time()
# 1. NN scalar at m=1: g = 4 sin^2(k/2), f = sin k. R9-9 table: M,T2g -1.903007e-3, M,Eg -8.301857e-4, U,T2g -2.289166e-4, U,Eg -6.883237e-5; V3 mu_E +1.97038864e-3
n = 1 << 14; kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
g = 4*np.sin(kk/2)**2; f = np.sin(kk)
X = xi_all(g, f, 1.0, nu=3000, umin=-20); print('NN m=1:', ' '.join('%s %+.6e' % kv for kv in X.items()), '| mu_E %+.8e' % mu_E(g, f, 1.0, nu=3000, umin=-20))
# 2. Z1 at m=0.3 (R16-3: M,T2g +3.904715e-4, U,T2g +2.810149e-4, M,Eg +4.117765e-4, U,Eg +4.053591e-4, mu_E +1.227e-2, vmax 0.984560)
from laws import Z1, G
L = Z1(0.06); g, f = L.samples(1 << 16); X = xi_all(g, f, 0.3, nu=4000, umin=-22)
print('Z1 m=0.3:', ' '.join('%s %+.6e' % kv for kv in X.items()), '| mu_E %+.4e | vmax %.6f' % (mu_E(g, f, 0.3, nu=3000), L.vmax(0.3)))
# 3. G(1.4) mu_E at m=1 (R14-3: +3.52543170e-3)
L = G(1.4); g, f = L.samples(1 << 16); print('G(1.4) mu_E(m=1) %+.8e' % mu_E(g, f, 1.0, nu=3000, umin=-20))
# 4. simultaneous zero, A,C2,C, M vertex m=0.1, (u,v)=(0.955978,0.024523): Xi ~ 0, mu_E +6.19e-3
NF = 1 << 16
A_ = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
C = Zz(1.0, 0.35, 0.43, 0.03); C2 = Zz(1.0, 0.35, 0.47, 0.03)
for (vtx, m, u, v) in [('M', 0.1, 0.955978, 0.024523), ('U', 0.1, 0.964879, 0.007410), ('M', 0.01, 0.943709, 0.038492)]:
    Lm = Mix([A_, C2, C], [1-u-v, u, v]); g, f = Lm.samples(1 << 16); X = xi_all(g, f, m, nu=4000, umin=-22)
    print('zero %s m=%.2f (u,v)=(%.6f,%.6f):' % (vtx, m, u, v), ' '.join('%s %+.3e' % kv for kv in X.items()), '| mu_E %+.4e | vmax %.6f | max|sp| %.9f' % (mu_E(g, f, m, nu=3000), Lm.vmax(m), np.abs(Lm.sp).max()))
print('runtime %.1fs' % (time.time()-T0))
