"""R17-13 dgman: the mu_T2^F = 0 manifold of R16-13's DG(b, w, r) family (lib13 DGlaw root in r, GL 3x10), with the other
Dirac rows (V0+SF) from the archived dfam.evaluate (3,8) at the root; m = 0.01.  Saved to dgman.npy: [b, w, r*, T2g, Eg, muE, muT2(arch)]."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import lib13 as L, dfam
from scipy.optimize import brentq
m = 0.01; t0 = time.time(); out = []
for b in (0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3):
    for w in (0.03, 0.05, 0.1, 0.2, 0.3, 0.5):
        if b + w > np.pi/2: continue
        f = lambda r: L.muT2(L.DGlaw(b, w, r), m, 3, 10)
        rr = np.array([0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 1/np.sqrt(3)]); v = [f(r) for r in rr]
        for i in range(len(rr)-1):
            if v[i]*v[i+1] < 0:
                r = brentq(f, rr[i], rr[i+1], xtol=1e-12)
                o = dfam.evaluate(dfam.DG(b, w, r, nf=40001), m, 3, 8)
                out.append([b, w, r, o['T2g'], o['Eg'], o['muE'], o['muT2']])
                print('DG(%.2f,%.2f) r*=%.6f W_pi=%.4f: T2g %+.4e Eg %+.4e muE %+.4e (arch muT2 %+.1e) [%.0fs]' % (b, w, r, L.DGlaw(b, w, r).Wpi, *out[-1][3:], time.time()-t0), flush=True)
np.save('dgman.npy', np.array(out)); print('saved %d, %.0fs' % (len(out), time.time()-t0))
