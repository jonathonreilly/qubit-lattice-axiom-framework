"""R18-1 s5b: primary pinch diagnostic (pre-registered direct comparison): the SAME readout component xz at k||z (vector
channel) and at k||y (tensor channel), rho(q) = S_xz,xz(k z)/S_xz,xz(k y) (white noise: 1; Coulomb pinch: -> 0 as q -> 0),
xi^2(q) = (1/rho - 1)/q^2 at the two smallest axis q, with bin errors; averaged over the cubic copies
(xz@z & xz@y, yz@x & yz@z, xy@y & xy@x). Gaussian control (s7): xi^2 = lam exactly at every q."""
import numpy as np, glob, pickle, os, sys
from mc import cvec
D = "../data/"
def comp(a, b):
    e = np.zeros((3, 3)); e[a, b] = e[b, a] = 1/np.sqrt(2); return cvec(e)
def rho(res, m):
    kl = res['klist']; Mb = res['Mb']; L = res['L']
    def ik(ax):
        return [i for i, (n, mm, v) in enumerate(kl) if n == "axis" and mm == m and v[ax] != 0][0]
    num = 0; den = 0
    for (a, b, along, perp) in [(0, 2, 2, 1), (1, 2, 2, 0), (0, 1, 1, 2), (0, 2, 0, 1), (1, 2, 1, 0), (0, 1, 0, 2)]:
        c = comp(a, b)   # component ab at k || 'along' (one of a,b -> vector) vs k || 'perp' (neither -> tensor)
        num = num + np.array([np.real(c @ Mb[bb, ik(along)] @ c) for bb in range(Mb.shape[0])])
        den = den + np.array([np.real(c @ Mb[bb, ik(perp)] @ c) for bb in range(Mb.shape[0])])
    r = num/den; q2 = 4*np.sin(np.pi*m/L)**2
    x2 = (1/r - 1)/q2
    return q2, r.mean(), r.std()/np.sqrt(len(r)), x2.mean(), x2.std()/np.sqrt(len(x2)), den.mean()/6
files = sys.argv[1:] if len(sys.argv) > 1 else sorted(f for f in glob.glob(D + "d_L*_b*.pkl") + glob.glob(D + "pt*_L*_b*.pkl") + glob.glob(D + "binf_L*.pkl") if "test" not in f)
rows = []
for f in files:
    res = pickle.load(open(f, "rb")); L = res['L']
    a = rho(res, 1); b = rho(res, 2)
    rows.append((res['bU'], L, os.path.basename(f), res['Eb'].mean(), a, b))
rows.sort(key=lambda r: (r[0], r[1], r[2]))
print("%-5s %-3s %-24s %-8s | q1^2   rho(q1)          xi^2(q1)         | q2^2   rho(q2)          xi^2(q2)        | S_T(q1) | xi(q1)/L" % ("bU", "L", "run", "E/edge"))
for bU, L, f, E, a, b in rows:
    xl = np.sqrt(max(a[3], 0))/L
    print("%-5.2f %-3d %-24s %-8.5f | %.3f  %.4f+-%.4f  %8.3f+-%6.3f | %.3f  %.4f+-%.4f  %8.3f+-%6.3f | %.3f   | %.3f" %
          (bU, L, f, E, a[0], a[1], a[2], a[3], a[4], b[0], b[1], b[2], b[3], b[4], a[5], xl))
