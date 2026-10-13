"""R19-12 probe (a): F_1/2(0+) on the root Dirac edge D1(b_f, r) and F_0(0+) on the root scalar edge G(b_s),
each with the root photon gammaG_w(2.9435, pi - 2.9435) (= Gph(2.9435)), by R16-10's Theorem-L split (m -> 0, lam = 0).
Convergence in N (48..160), split radii (two choices), and the Dirac mass slope F(m) - F(0+) at m in {0.0025..0.02}.
Then the photon moments G_1/2(m), G_0(m) on the same matter edges (N = 128, 192, 256), m -> 0."""
import time, numpy as np
from r1912_lib import *
t0 = time.time()
R = ROOT; d, pr = photon_Gw(R['bg'], np.pi - R['bg']); cb = R['bg']
print('root edges: D1(b_f=%.9f, r=%.9f), G(b_s=%.9f), photon gammaG_w(%.4f, %.6f): max d\' %.4f min d\' %.1e d(pi) %.4f'
      % (R['bf'], R['r'], R['bs'], R['bg'], np.pi - R['bg'], pr.maxdp, pr.mindp, pr.dpi), flush=True)
for N in (48, 64, 96, 128, 160):
    for ch in (0, 1):
        if N == 160 and ch == 1: continue
        Fd, Td = F_dirac(R['bf'], R['r'], d, cb, N, choice=ch)
        Fs, Ts = F_scalar(R['bs'], d, cb, N, choice=ch)
        print('N=%3d radii#%d | F_1/2(0+) = %+.5f [tadpole %+.5f] | F_0(0+) = %+.5f [seagull %+.5f]  (%.0fs)' % (N, ch, Fd, Td, Fs, Ts, time.time()-t0), flush=True)
print('-- Dirac mass dependence at N=128 (lam = 0; Theorem L path-independence):')
F0 = F_dirac(R['bf'], R['r'], d, cb, 128)[0]
for m in (0.0025, 0.005, 0.01, 0.02):
    Fm = F_dirac(R['bf'], R['r'], d, cb, 128, m=m)[0]
    print('  m=%.4f F=%+.5f F-F(0+)=%+.6f (F-F0)/m=%+.4f' % (m, Fm, Fm - F0, (Fm - F0)/m), flush=True)
print('-- scalar mass dependence at N=128:')
F0s = F_scalar(R['bs'], d, cb, 128)[0]
for m in (0.005, 0.01, 0.02):
    Fm = F_scalar(R['bs'], d, cb, 128, m=m)[0]
    print('  m=%.4f F0=%+.5f F-F(0+)=%+.6f (F-F0)/m^2=%+.3f' % (m, Fm, Fm - F0s, (Fm - F0s)/m**2), flush=True)
print('-- photon moments (Lemma Q: independent of the photon symbol and lam):')
for N in (128, 192, 256):
    row = []
    for m in (0.04, 0.02, 0.01, 0.005, 0.0025):
        row.append((m, G_dirac(R['bf'], R['r'], m, N), G_scalar(R['bs'], m, N)))
    print('  N=%3d ' % N + ' '.join('m=%.4f: G12 %+.6f G0 %+.6f |' % x for x in row) + ' (%.0fs)' % (time.time()-t0), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
