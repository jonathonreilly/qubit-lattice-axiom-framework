"""R16-10: targeted scalar scan, matter box b below a stiff photon's box c1 (photon continuum where matter is lattice).
Resolution checked (N = 48, 96). Matter Flat(b, w) (u'/2 <= q), photon R85(c1, c2, G) (nondecreasing; G >= pi/2)."""
import numpy as np, sys, time
from r1610_eval import *
from r1610_laws import *
from sublum import Phi, wrap
t0 = time.time()
def scal_flat(b, w):
    def h(k):
        a = np.abs(wrap(np.asarray(k, float))); x = np.clip((a - b)/w, 0, 1)
        return np.where(a <= b, a, b + w*(x - Phi(x)))
    return lambda k: h(k)**2
rows = []
for b in (0.8, 1.2, 1.6, 2.0):
    for w in (0.4, 0.8, np.pi - b):
        for (c1, c2) in [(b, min(b + 0.8, 3.1)), (min(b + 0.5, 2.6), min(b + 1.3, 3.12)), (min(b + 0.9, 2.7), 3.12)]:
            for G in (1.0, 3.0, 8.0):
                d = photon('R85', c1, c2, G)
                qq = np.linspace(0, np.pi, 4001); dd = np.gradient(d(qq), qq)
                if dd[1:-1].min() < -1e-6: continue
                box = min(b, c1); r1 = min(0.75*box, 0.9); r0 = 0.35*r1
                lp, sp = lattice_part(0, 48, 0.0, 0.0, scal_flat(b, w), d, r0, r1, 0.02)
                rows.append((K[0] + lp, b, w, c1, c2, G, sp, dd.max()))
                print('Flat(b=%.2f,w=%.2f) R85(%.2f,%.2f,G=%.1f) maxd\'=%5.2f N=48 | F(0+) %+8.4f [seagull %+8.4f]' % (b, w, c1, c2, G, dd.max(), K[0] + lp, sp), flush=True)
rows.sort()
print('--- top 5 rechecked at N=96')
for r in rows[-5:]:
    F, b, w, c1, c2, G, sp, vm = r
    box = min(b, c1); r1 = min(0.75*box, 0.9); r0 = 0.35*r1
    lp, sp2 = lattice_part(0, 96, 0.0, 0.0, scal_flat(b, w), photon('R85', c1, c2, G), r0, r1, 0.02)
    print('Flat(b=%.2f,w=%.2f) R85(%.2f,%.2f,G=%.1f) | N=48 %+8.4f  N=96 %+8.4f [seagull %+8.4f]' % (b, w, c1, c2, G, F, K[0] + lp, sp2), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
