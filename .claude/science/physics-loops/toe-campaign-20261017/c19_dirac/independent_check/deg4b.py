"""Complex combination of real and imaginary O-invariant staggered A1 terms at finite strength:
folded levels at k* split 2+2 (E1/2 and E5/2 sectors), each doublet stays a Weyl node (Berry flux)."""
import numpy as np
from core import *
from bases import get
rng = np.random.default_rng(4)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
def rnd(bs):
    c = rng.normal(size=len(bs)); m = addm(*bs, coeffs=list(c)); nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
Hb = addm(hop(-1.0, 0.2), rnd(get('X_r1')), coeffs=[1, 0.05])
S = addm(rnd(get('Q_r1_re_A1')), rnd(get('Q_r1_im_A1')))
for s in (0.05, 0.2):
    Ss = {a: s * b for a, b in S.items()}
    f = lambda k: fold(Hb, Ss, k)
    e = np.linalg.eigvalsh(f(KS)); print(f"strength {s}: lowest folded levels at k*: {np.round(e[:8], 5)}")
    def berry(band, r=0.01, n=20):
        th = np.linspace(0, np.pi, n + 1); ph = np.linspace(0, 2*np.pi, 2*n, endpoint=False)
        U = [[np.linalg.eigh(f(KS + r*np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])))[1][:, band] for p in ph] for t in th]
        tot = 0
        for i in range(n):
            for j in range(2*n):
                a, b, c, d = U[i][j], U[i+1][j], U[i+1][(j+1) % (2*n)], U[i][(j+1) % (2*n)]
                tot += np.angle(np.vdot(a, b)*np.vdot(b, c)*np.vdot(c, d)*np.vdot(d, a))
        return tot / (2*np.pi)
    print("   Berry flux of bands 0..3 around folded k*:", [round(berry(b), 4) for b in range(4)])
