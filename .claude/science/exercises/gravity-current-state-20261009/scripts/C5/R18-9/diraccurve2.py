"""R18-9: fine D1 mu_T2 = 0 curve near its subluminal end (r* -> 1/sqrt3), UD rows; plus the end point b_end(m)."""
import sys, time, numpy as np, lib9 as L
from scipy.optimize import brentq
m = float(sys.argv[1]); t0 = time.time(); out = []
bend = brentq(lambda b: L.muT2(b, 1/np.sqrt(3), m), 0.85, 1.0, xtol=1e-10)
print('m=%g: curve end (r = 1/sqrt3) at b_end = %.8f' % (m, bend))
for b in list(np.linspace(0.70, bend, 12)):
    r = L.rstar(b, m, lo=0.3, hi=1/np.sqrt(3)+1e-12)
    if r is None: print('b=%.4f no root' % b); continue
    F = L.dirac(b, r, m=m); out.append([b, r, *F])
    print('m=%g b=%.5f r*=%.6f UD (T %+.5e E %+.5e muE %+.5e muT2 %+.1e) x22.5 [%+.4f %+.4f %+.4f]' % (m, b, r, *F, *(22.5*F[:3])), flush=True)
np.save('diraccurve2_m%g.npy' % m, np.array(out)); print('elapsed %.0fs' % (time.time()-t0))
