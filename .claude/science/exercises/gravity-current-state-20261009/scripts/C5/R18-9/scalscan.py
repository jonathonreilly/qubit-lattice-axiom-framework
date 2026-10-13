"""R18-9: scalar G_w(b_s, fr*(pi-b_s)) under U at m: per real scalar (Xi_T2g, Xi_Eg, mu_E); grid saved."""
import sys, time, numpy as np, lib9 as L
m = float(sys.argv[1]); t0 = time.time(); out = []
for bs in np.r_[0.2:3.0:0.2, 3.0, 3.05, 3.1, 3.12]:
    for fr in (0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0):
        s = L.scal(bs, fr, m); out.append([bs, fr, *s[:3]])
np.save('scalscan_m%g.npy' % m, np.array(out)); A = np.array(out)
for row in A: print('G_w(%.2f, fr=%.2f): T %+.4e E %+.4e muE %+.4e' % tuple(row))
print('max muE %.4e; range T [%.3e, %.3e] E [%.3e, %.3e]; elapsed %.0fs' % (A[:,4].max(), A[:,2].min(), A[:,2].max(), A[:,3].min(), A[:,3].max(), time.time()-t0))
