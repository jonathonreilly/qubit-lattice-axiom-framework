"""R16-10: (i) resolution recheck of the best scalar search candidates (N = 32 -> 64, 128);
(ii) the subluminal-photon Lemma T' constants: for d' in [0,1] (so d(q) <= q) and lam -> 0,
   Dirac tadpole <= -8 pi^2 <w(pi)> <= -8 pi^2 <1/(pi^2 sqrt(pi^2 + qy^2 + qz^2))>_perp ; scalar seagull <= half of that."""
import numpy as np, time
from r1610_eval import *
from r1610_laws import *
from sublum import Phi, wrap
t0 = time.time()
def scal_flat(b, w):
    def h(k):
        a = np.abs(wrap(np.asarray(k, float))); x = np.clip((a - b)/w, 0, 1)
        return np.where(a <= b, a, b + w*(x - Phi(x)))
    return lambda k: h(k)**2
cands = [(('Flat', 2.72, 0.126), ('Gph', 0.8425)), (('Flat', 2.718, 0.116), ('Gph', 2.808)),
         (('Flat', 1.8776, 0.0542), ('R85', 2.3837, 2.9846, 7.5712)), (('Flat', 2.983, 0.051), ('R85', 1.591, 2.168, 2.797))]
for mat, ph in cands:
    d = photon(*ph); u = scal_flat(mat[1], mat[2]); box = min(mat[1], ph[1]); r1 = min(0.75*box, 0.9); r0 = 0.35*r1
    for N in (32, 64, 128):
        lp, sp = lattice_part(0, N, 0.0, 0.0, u, d, r0, r1, 0.02)
        print('%s %s N=%3d | F_0(0+) %+8.4f [seagull %+8.4f]' % (mat, ph, N, K[0] + lp, sp), flush=True)
x, w = np.polynomial.legendre.leggauss(200)
X, Y = np.meshgrid(np.pi*x, np.pi*x); Wt = np.outer(w, w)*np.pi**2/(2*np.pi)**2
avg = np.sum(Wt/(np.pi**2*np.sqrt(np.pi**2 + X**2 + Y**2)))
print('subluminal photon bound: <w(pi)>_perp >= %.6f ; Dirac tadpole <= %+.4f ; scalar seagull <= %+.4f (x16pi^2 units, m,lam -> 0)' % (avg, -8*np.pi**2*avg, -4*np.pi**2*avg))
print('elapsed %.1fs' % (time.time() - t0))
