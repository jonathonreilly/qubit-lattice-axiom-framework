"""R19-12 probe (help or hurt): F_1/2(0+) on the ROOT Dirac edge and F_0(0+) on the ROOT scalar edge as the photon symbol moves.
Subluminal gammaG_w photons (d' in [0,1]): Gph(c) for c from 1.0 to 3.13 (fw = 1), R18-5's photon gammaG_w(1.271203, 0.259986);
R16-2's R8-5 box photon R85(1, 2, G = 1) (v_max 1); and the R16-10 stiffened photon R85(1, 2, G): bisection for the Dirac zero
G* on the root D1, with its whole-zone photon v_max = max d'.  Also dF/db_g across the window [2.9361, 2.9469]."""
import time, numpy as np
from r1912_lib import *
t0 = time.time(); R = ROOT; N = 96
def vmax(d):
    q = np.linspace(1e-6, np.pi - 1e-6, 200001); dd = np.gradient(d(q), q); return dd.max(), dd.min()
rows = [('Gph', c) for c in (1.0, 1.5, 2.0, 2.6, 2.9, 2.9361, 2.9435, 2.9469, 3.0, 3.1, 3.13)] + [('Gw185',), ('R85', 1.0, 2.0, 1.0)]
for ph in rows:
    if ph[0] == 'Gw185':
        d, pr = photon_Gw(1.271203, 0.259986); cb = 1.271203; lab = 'gammaG_w(1.271203,0.259986) [R18-5]'
    elif ph[0] == 'Gph':
        d, pr = photon_Gw(ph[1], np.pi - ph[1]); cb = ph[1]; lab = 'gammaG_w(%.4f, fw=1)' % ph[1]
    else:
        d = photon(*ph); cb = ph[1]; lab = 'R85(1,2,G=1) [R16-2 box photon]'
    vx, vn = vmax(d)
    Fd = F_dirac(R['bf'], R['r'], d, cb, N)[0]; Fs = F_scalar(R['bs'], d, cb, N)[0]
    print('%-40s v_max %.4f min d\' %+.1e | F_1/2(0+) %+.5f | F_0(0+) %+.5f  (%.0fs)' % (lab, vx, vn, Fd, Fs, time.time()-t0), flush=True)
print('-- stiffened R85(1,2,G) on the root D1 (R16-10 route), N=64 bisection:')
f = lambda G: F_dirac(R['bf'], R['r'], photon('R85', 1.0, 2.0, G), 1.0, 64)[0]
a, b = 2.0, 4.5; fa = f(a); fb = f(b); print('  F(G=%.2f) = %+.4f, F(G=%.2f) = %+.4f' % (a, fa, b, fb), flush=True)
if fa*fb < 0:
    for it in range(16):
        c = 0.5*(a + b); fc = f(c)
        if np.sign(fc) == np.sign(fa): a, fa = c, fc
        else: b = c
    Gs = 0.5*(a + b); vx, vn = vmax(photon('R85', 1.0, 2.0, Gs))
    print('  G* = %.4f (N=64); F at G* (N=96) = %+.5f ; photon whole-zone v_max = %.3f' % (Gs, F_dirac(R['bf'], R['r'], photon('R85', 1.0, 2.0, Gs), 1.0, 96)[0], vx), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
