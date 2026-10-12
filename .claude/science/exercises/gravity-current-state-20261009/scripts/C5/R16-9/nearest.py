"""R16-9 (c): the explicit nearest-approach laws (graviton-cone zero on one vertex, smallest mu_E found) from opt3.py,
re-evaluated at high resolution, with whole-zone v_max and raw Fourier tails |eps_r| of eps_1D = sqrt(0.09 + g) (nothing subtracted)."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *
def law(b, N, wt, v, nf=1 << 17):
    edges = np.linspace(b, np.pi - 0.08, N + 1); return ZLaw([1.0] + list(v) + [0.0], list(edges), wt, 'P', nf=nf)
cands = {'M-best (opt3 M N16 b0.6)': (0.6, 16, 0.03, [-1.0, -0.661253, -1.0, 0.968462, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 0.061961, 0.026244]),
         'U-best (opt3 U N16 b0.6)': (0.6, 16, 0.03, [0.045227, -0.04252, -0.161799, -0.272918, -0.393618, -0.864482, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0])}
for name, (b, N, wt, v) in cands.items():
    L = law(b, N, wt, v)
    for m in (0.1, 0.03):
        g, f = L.samples(1 << 15); X = xi_all(g, f, m, nu=2500, umin=-20); mu = mu_E(g, f, m, nu=2500, umin=-20)
        print('%s m=%.2f: M Eg %+.3e T2g %+.3e | U Eg %+.3e T2g %+.3e | mu_E %+.4e | vmax %.6f' % (name, m, X['M,Eg'], X['M,T2g'], X['U,Eg'], X['U,T2g'], mu, L.vmax(m)))
    n = 1 << 20; g, f = L.samples(n); e1 = np.sqrt(0.09 + g); c = np.abs(np.fft.rfft(e1))/n
    print('   max|sp| %.9f  min edge g %.4f  tails |eps_r| r=128 %.2e r=256 %.2e r=512 %.2e' % (np.abs(L.sp).max(), (L.sig[L.k >= b]**2).min(), c[128], c[256], c[512]))
