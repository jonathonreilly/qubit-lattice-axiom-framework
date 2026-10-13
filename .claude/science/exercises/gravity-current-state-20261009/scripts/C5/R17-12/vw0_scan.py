"""R17-12 (c): VW0 photon scan against R17-9's two sampled necessary inequalities (C5_R17-9_report.md:226-227):
  Xi_g,T2g <= 6.0e-4  and  Xi_g,Eg - Xi_g,T2g >= 4.46e-3   (per vector; from R17-9's sampled matter ranges)."""
import numpy as np, time
from r1712_lib import *
t0 = time.time(); N = 48; ok = []
for b in (0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.7, 1.0):
    for w in (0.25, 0.5, 1.0, 1.5, 2.0):
        if b + w > np.pi: continue
        law = photonGw(b, w)
        T = xi(law, N, 'T2g', 'VW0')[0]; E = xi(law, N, 'Eg', 'VW0')[0]
        flag = (T <= 6.0e-4) and (E - T >= 4.46e-3)
        if flag: ok.append((b, w))
        print('%-24s VW0 Xi_T2g %+.4e Xi_Eg %+.4e diff %+.4e  T2g<=6e-4:%s diff>=4.46e-3:%s' % (law.name, T, E, E - T, T <= 6e-4, E - T >= 4.46e-3), flush=True)
print('laws meeting both:', ok); print('elapsed %.1fs' % (time.time() - t0))
