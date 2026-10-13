"""R18-9: D1 mu_T2 = 0 curve r*(b) at m (argv), with UD rows per Dirac field (Xi_T2g, Xi_Eg, mu_E) and V0 for comparison."""
import sys, time, numpy as np, lib9 as L
m = float(sys.argv[1]); t0 = time.time(); out = []
for b in (0.06, 0.08, 0.10, 0.12, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.94):
    r = L.rstar(b, m, lo=0.05)
    if r is None: print('b=%.3f no root' % b); continue
    F = L.dirac(b, r, m=m); F0 = L.dirac(b, r, m=m, vtx='V0')
    out.append([b, r, *F])
    print('m=%g b=%.3f r*=%.6f UD (T %+.4e E %+.4e muE %+.4e muT2 %+.1e) | V0 (T %+.4e E %+.4e) | x22.5 UD [%+.4f %+.4f %+.4f]' % (m, b, r, *F, F0[0], F0[1], *(22.5*F[:3])), flush=True)
np.save('diraccurve_m%g.npy' % m, np.array(out)); print('elapsed %.0fs' % (time.time()-t0))
