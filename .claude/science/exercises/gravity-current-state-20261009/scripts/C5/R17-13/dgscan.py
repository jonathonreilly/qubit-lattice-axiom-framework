"""R17-13 dgscan: other subluminal Wilson-Dirac families (R16-13's DG(b, w, r): s' with a flat plateau, W' = r sqrt(1-s'^2); Lemma V1 needs r <= 1/sqrt3).
For each (b, w): roots r* of mu_T2^F = 0 and the Dirac rows there (archived dfam.evaluate, GL (3,8)); m = 0.01."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1])
import dfam
from scipy.optimize import brentq
m = 0.01; t0 = time.time()
def ev(b, w, r): return dfam.evaluate(dfam.DG(b, w, r, nf=40001), m, 3, 8)
for b in (0.15, 0.3, 0.5, 0.7, 0.9, 1.1):
    for w in (0.1, 0.3, 0.5):
        if b + w > np.pi/2: continue
        f = lambda r: ev(b, w, r)['muT2']
        rr = np.linspace(0.03, 1/np.sqrt(3), 12); v = [f(r) for r in rr]
        roots = [brentq(f, rr[i], rr[i+1], xtol=1e-10) for i in range(len(rr)-1) if v[i]*v[i+1] < 0]
        sgn = ''.join('+' if x > 0 else '-' for x in v)
        if not roots: print('DG(%.2f,%.2f): signs over r %s, no root' % (b, w, sgn), flush=True)
        for r in roots:
            o = ev(b, w, r)
            print('DG(%.2f,%.2f) r*=%.6f: T2g %+.4e Eg %+.4e muE %+.4e muT2 %+.1e | x22.5 (%+.4f %+.4f %+.4f) [%.0fs]' % (b, w, r, o['T2g'], o['Eg'], o['muE'], o['muT2'], 22.5*o['T2g'], 22.5*o['Eg'], 22.5*o['muE'], time.time()-t0), flush=True)
