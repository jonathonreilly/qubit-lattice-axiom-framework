"""(1) U-vertex simultaneous zero with corners A=G(1.0), B'=Z1(wt=0.25), C; (2) 3D-grid check of the M zero (m=0.03);
(3) hopping-kernel tails |eps_r| (raw Fourier coefficients of the 1D dispersion eps(k)=sqrt(m^2+g), m=0.3; no subtraction);
(4) Theorem B' sanity: gentle-valley law (|sigma'| <= 1/sqrt5 after the first peak) has I(B) < 0."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz; from grid3d import xi3d
from simul2 import A, B, C, law, F, newton, NF
T0 = time.time()
Bp = ZLaw([1, -1, 1, -1, 1, -1, 0], [1.0, 1.4, 1.8, 2.2, 2.6, 3.0], 0.25, 'Z1(0.25)', nf=NF)
for m in [0.1, 0.03, 0.01]:
    best = None
    for u in np.arange(0, 1.0001, 0.05):
        for v in np.arange(0, 1.0001 - u, 0.05):
            r = F(np.array([u, v]), m, 'U', [A, Bp, C], nn=1 << 12, nu=500); s = np.abs(r).sum()
            if best is None or s < best[0]: best = (s, u, v)
    p, r = newton(np.array([best[1], best[2]]), m, 'U', [A, Bp, C])
    L = law(p, [A, Bp, C]); g, f = L.samples(1 << 16); X = xi_all(g, f, m, nu=4000, umin=-22)
    print('U zero, corners A,Z1(0.25),C, m=%.2f: (u,v)=(%.6f,%.6f) in-simplex=%s | %s | mu_E %+.3e | v_max %.6f max|s\'| %.9f min edge g %.4f'
          % (m, p[0], p[1], p.min() >= 0 and p.sum() <= 1, ' '.join('%s %+.2e' % kv for kv in X.items()), mu_E(g, f, m, nu=3000), L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= 1.0]**2).min()), flush=True)
# (2) M zero at m = 0.03 (corners A,B,C), 3D grid
best = None
for u in np.arange(0, 0.2001, 0.02):
    for v in np.arange(0.8, 1.0001 - u, 0.02):
        r = F(np.array([u, v]), 0.03, 'M', [A, B, C], nn=1 << 12, nu=500); s = np.abs(r).sum()
        if best is None or s < best[0]: best = (s, u, v)
p, r = newton(np.array([best[1], best[2]]), 0.03, 'M', [A, B, C]); Lz = law(p, [A, B, C])
g, f = Lz.samples(1 << 16); X = xi_all(g, f, 0.03, nu=4000, umin=-22)
print('M zero m=0.03 (u,v)=(%.6f,%.6f): Laplace %s' % (p[0], p[1], ' '.join('%s %+.3e' % kv for kv in X.items())), flush=True)
for N in [480, 720, 960]:
    Xg = xi3d(Lz, 0.03, N)
    print('   3D grid N=%d: ' % N + ' '.join('%s A %+.3e / IBP %+.3e' % (v, x[0], x[1]) for v, x in Xg.items()), flush=True)
# scale for comparison: corner values at m=0.03
for nm, Lc in [('A=G(1.0)', A), ('B=Z1', B), ('C', C)]:
    g, f = Lc.samples(1 << 15); X = xi_all(g, f, 0.03)
    print('   corner %s m=0.03: %s mu_E %+.3e' % (nm, ' '.join('%s %+.3e' % kv for kv in X.items()), mu_E(g, f, 0.03)), flush=True)
# (3) tails
def tails(Lc, m=0.3, n=1 << 16):
    g, f = Lc.samples(n); e = np.sqrt(m*m + g); c = np.abs(np.fft.fft(e))/n
    kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
    # samples are on midpoints; |coefficient| unaffected by the half-cell phase
    return [c[r] for r in [16, 32, 64, 128, 256, 512]]
for nm, Lc in [('Z1(0.06)', B), ('C=Zz(1.0,0.35,0.43,0.03)', C), ('M-zero law (m=0.03)', Lz), ('G(1.0)', A), ('Z1(0.25)', Bp)]:
    print('tails |eps_r| (m=0.3, no subtraction) %s: ' % nm + ' '.join('r=%d:%.1e' % (r, v) for r, v in zip([16, 32, 64, 128, 256, 512], tails(Lc))), flush=True)
# (4) gentle-valley law: sigma'=1 on [0,1.0], then -0.44 for 0.8, +0.44 for 0.6, -0.44 for 0.4, then 0
Lg = ZLaw([1.0, -0.44, 0.44, -0.44, 0.0], [1.0, 1.8, 2.4, 2.8], 0.06, 'gentle', nf=NF)
g, f = Lg.samples(1 << 15); inf = Lg.info()
Bs = np.logspace(-6, 2, 41); I = Icurve(g, f, Bs)
print('gentle-valley law: valleys %s; max|s\'| after first peak %.3f; max_B I(B) over [1e-6,1e2] = %+.4e (all negative: %s)'
      % (inf['valleys'], np.abs(Lg.sp[Lg.k > 1.03]).max(), I.max(), bool((I < 0).all())))
print('runtime %.1fs' % (time.time()-T0))
