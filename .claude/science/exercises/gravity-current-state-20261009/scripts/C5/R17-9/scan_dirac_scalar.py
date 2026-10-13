"""R17-9: ranges per field over the stated families at m = 0.01 (and 0.001 spot):
 Dirac D1(b_f, r) [V0 vertex, SF], R16-13's evaluator (rechecked); real scalars on G_w(b, w) incl. G(b) [U vertex (Lemma M), SF]."""
import numpy as np, time
from content3 import ferm
from content4 import scalw
t0 = time.time(); m = 0.01
rows = []
for bf in (0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.45, 1.55):
    for r in (0.02, 0.15, 0.3, 0.45, 0.5773):
        v = ferm(bf, r, m)[0]; rows.append((bf, r, *v))
        print('D1(%.2f,%.4f): Xi_T2g %+.4e Xi_Eg %+.4e mu_E %+.4e mu_T2 %+.3e  biref %+.3e' % (bf, r, *v, v[0]-v[1]), flush=True)
A = np.array(rows)
print('D1 family min Xi_T2g %+.4e, min Xi_Eg %+.4e, max mu_E %+.4e, min (T2g-Eg) %+.4e' % (A[:, 2].min(), A[:, 3].min(), A[:, 4].max(), (A[:, 2]-A[:, 3]).min()))
srows = []
for b in (0.3, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6, 2.9):
    for fr in (0.1, 0.25, 0.5, 0.75, 1.0):
        try:
            v = scalw(b, fr, m, vert='U')[0]
        except Exception as ex:
            print('skip', b, fr, ex); continue
        srows.append((b, fr, *v[:3]))
        print('G_w(%.2f, w=%.3f) U: Xi_T2g %+.4e Xi_Eg %+.4e mu_E %+.4e' % (b, fr*(np.pi-b), *v[:3]), flush=True)
B = np.array(srows)
print('scalar U family min Xi_T2g %+.4e, min Xi_Eg %+.4e, max mu_E %+.4e' % (B[:, 2].min(), B[:, 3].min(), B[:, 4].max()))
np.save('scan_D1.npy', A); np.save('scan_GwU.npy', B)
print('elapsed %.1fs' % (time.time()-t0))
