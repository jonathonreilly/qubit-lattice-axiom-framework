"""R18-1 s5: summary table over all runs (direct d_*, PT pt_*, long direct d_*_long, post-selected post_*).
Per (bU, L): E/edge, r(qmin) = S_V/S_TT at the smallest axis k, xi^2(q) = (1/r-1)/q^2 at the two smallest axis q,
xi(qmin)/L, S_gamma/q^2 at qmin; plus the pinch comparison S_xz,xz(k z) vs S_xz,xz(k y) at qmin (same component, two directions)."""
import numpy as np, glob, pickle, re, os
from analyze import channels
from mc import cvec
D = "../data/"
files = sorted(glob.glob(D + "d_L*_b*.pkl") + glob.glob(D + "pt_L*_b*.pkl"))
rows = []
for f in files:
    if "test" in f: continue
    res = pickle.load(open(f, "rb")); L = res['L']; bU = res['bU']
    tab = channels(res)
    q2 = [tab[("axis", m)][0] for m in (1, 2)]; d1 = tab[("axis", 1)][1]; d2 = tab[("axis", 2)][1]
    r1, er1 = d1['r']; r2 = d2['r'][0]
    # same component xz at k||z (vector) and k||y (tensor): from Mb directly
    eps = np.zeros((3, 3)); eps[0, 2] = eps[2, 0] = 1/np.sqrt(2); c = cvec(eps)
    kl = res['klist']; Mb = res['Mb']
    iz = [i for i, (n, m, v) in enumerate(kl) if n == "axis" and m == 1 and v[2] != 0][0]
    iy = [i for i, (n, m, v) in enumerate(kl) if n == "axis" and m == 1 and v[1] != 0][0]
    Sz = np.array([np.real(c @ Mb[b, iz] @ c) for b in range(Mb.shape[0])]); Sy = np.array([np.real(c @ Mb[b, iy] @ c) for b in range(Mb.shape[0])])
    rows.append((bU, L, os.path.basename(f), res['Eb'].mean(), r1, er1, (1/r1 - 1)/q2[0], (1/r2 - 1)/q2[1], q2[0],
                 d1['gam'][0]/q2[0], Sz.mean(), Sz.std()/np.sqrt(len(Sz)), Sy.mean(), Sy.std()/np.sqrt(len(Sy))))
rows.sort()
print("%-5s %-3s %-22s %-8s %-15s %-8s %-8s %-6s %-7s %-7s %-17s %-17s" % ("bU", "L", "run", "E/edge", "r(qmin)", "xi2(q1)", "xi2(q2)", "q1^2", "xi/L", "Sg/q2", "S_xz,xz(k z)", "S_xz,xz(k y)"))
for (bU, L, f, E, r1, er1, x1, x2, q1, gq, Sz, eSz, Sy, eSy) in rows:
    print("%-5.2f %-3d %-22s %-8.5f %.4f+-%.4f %-8.3f %-8.3f %-6.3f %-7.3f %-7.4f %.4f+-%.4f  %.4f+-%.4f" %
          (bU, L, f, E, r1, er1, x1, x2, q1, np.sqrt(max(x1, 0))/L, gq, Sz, eSz, Sy, eSy))
for f in sorted(glob.glob(D + "*_post.pkl")):
    res = pickle.load(open(f, "rb"))
    print("post-selected gamma=0 (bU = infinity) %s: samples %d, distinct configurations %d" % (os.path.basename(f), res['npost'], res['ndistinct']))
