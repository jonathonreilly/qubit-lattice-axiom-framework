"""(1') U-vertex simultaneous zero with corners A=G(1.0), C2=Zz(1.0,0.35,0.47,0.03), C=Zz(1.0,0.35,0.43,0.03);
(3') clean hopping tails (law built on nf=2^20, samples on exact grid points, no interpolation); (4') gentle-valley I(B), resolved B range."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz
from simul2 import A, C, law, F, newton, NF
T0 = time.time()
C2 = Zz(1.0, 0.35, 0.47, 0.03)
for vtx in ['U', 'M']:
    for m in [0.1, 0.03, 0.01]:
        best = None
        for u in np.arange(0, 1.0001, 0.05):
            for v in np.arange(0, 1.0001 - u, 0.05):
                r = F(np.array([u, v]), m, vtx, [A, C2, C], nn=1 << 12, nu=500); s = np.abs(r).sum()
                if best is None or s < best[0]: best = (s, u, v)
        p, r = newton(np.array([best[1], best[2]]), m, vtx, [A, C2, C])
        L = law(p, [A, C2, C]); g, f = L.samples(1 << 16); X = xi_all(g, f, m, nu=4000, umin=-22)
        print('%s zero, corners A,C2,C, m=%.2f: (u,v)=(%.6f,%.6f) in-simplex=%s | %s | mu_E %+.3e | v_max %.6f max|s\'| %.9f min edge g %.4f'
              % (vtx, m, p[0], p[1], bool(p.min() >= 0 and p.sum() <= 1), ' '.join('%s %+.2e' % kv for kv in X.items()), mu_E(g, f, m, nu=3000), L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= 1.0]**2).min()), flush=True)
# (3') clean tails
def tails_clean(vals, bks, wt, m=0.3, n=1 << 14, nf=1 << 20):
    L = ZLaw(vals, bks, wt, nf=nf)
    kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi; j = np.rint(np.abs(kk)/np.pi*nf).astype(int)
    assert np.allclose(L.k[j], np.abs(kk))
    e = np.sqrt(m*m + L.sig[j]**2); c = np.abs(np.fft.fft(e))/n
    return [c[r] for r in [16, 32, 64, 128, 256, 512, 1024]]
for nm, args in [('Z1(wt=0.06)', ([1, -1, 1, -1, 1, -1, 0], [1.0, 1.4, 1.8, 2.2, 2.6, 3.0], 0.06)),
                 ('C=Zz(1.0,0.35,0.43,wt=0.03)', (C.vals, C.bks, 0.03)),
                 ('G(1.0)', ([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0))]:
    print('clean tails |eps_r| (m=0.3; raw Fourier coefficient, nothing subtracted) %s: ' % nm + ' '.join('r=%d:%.1e' % (r, v) for r, v in zip([16, 32, 64, 128, 256, 512, 1024], tails_clean(*args))), flush=True)
# (4') gentle valley
Lg = ZLaw([1.0, -0.44, 0.44, -0.44, 0.0], [1.0, 1.8, 2.4, 2.8], 0.06, 'gentle', nf=1 << 18)
g, f = Lg.samples(1 << 18); Bs = np.logspace(-3, 2, 26); I = Icurve(g, f, Bs)
print('gentle-valley law: valleys %s; max|sigma\'| on k>1.03: %.3f; I(B) for B in [1e-3,1e2]: max %+.4e, all negative: %s; I(1e-3)=%+.4f'
      % (Lg.info()['valleys'], np.abs(Lg.sp[Lg.k > 1.03]).max(), I.max(), bool((I < 0).all()), I[0]))
for m in [1.0, 0.3, 0.1, 0.01]:
    X = xi_all(*Lg.samples(1 << 15), m); print('   gentle m=%.2f: %s' % (m, ' '.join('%s %+.3e' % kv for kv in X.items())))
print('runtime %.1fs' % (time.time()-T0))
