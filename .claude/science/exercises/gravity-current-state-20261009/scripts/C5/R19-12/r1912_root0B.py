"""R19-12: the 4-row axial gravity root at m -> 0+ (scalar m_s = 1e-5, Dirac m_f = 0; R19-11's convention, its root0.py logic)
at a FIXED photon edge gammaG_w(b_g, fw = 1) whose VWa coefficients are computed here (R18-9 lib9.phot_quad, N = 160).
Then Sigma = 8 G_1/2(0+) at the root's Dirac edge (does the m -> 0+ gravity family carry Sigma = 0?).  Runners unmodified."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch', 'R18-9'))
import lib9 as L
from r1912_lib import G_dirac
bg = float(sys.argv[1]); x = np.array([float(v) for v in sys.argv[2].split(',')]); tag = sys.argv[3]
ms, mf, q, N = 1e-5, 0.0, (4, 10), 160
t0 = time.time(); P = L.phot_quad(bg, 1.0, N); T, E, Vmu = P['T2g'], P['Eg'], P['muE']
print('photon gGw(%.6f, fw=1) N=%d: T %s E %s muE %+.6e [%.0fs]' % (bg, N, T, E, Vmu, time.time()-t0), flush=True)
def rows(x):
    bs, bf, r, a = x
    S = L.scal(bs, 1.0, ms); F = L.dirac(bf, r, m=mf, q=q)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu])
    t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
h = np.array([1e-5, 1e-6, 1e-6, 1e-6])
for it in range(8):
    f = rows(x); J = np.empty((4, 4))
    for j in range(4):
        dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx) - rows(x - dx))/(2*h[j])
    print('it %d x=(%.9f, %.9f, %.9f, %.9f) |rows| %.2e detJ %.4e' % (it, *x, np.abs(f).max(), np.linalg.det(J)), flush=True)
    if np.abs(f).max() < 1e-12: break
    x = x - np.linalg.solve(J, f)
f = rows(x); bs, bf, r, a = x
g1, g2 = G_dirac(bf, r, 0.0025, 192), G_dirac(bf, r, 0.005, 192); G = 2*g1 - g2
print('ROOT0 b_g=%.6f: (b_s, b_f, r, a) = (%.10f, %.10f, %.10f, %.10f); rows %s; r<1/sqrt3 %s; detJ %.4e' % (bg, *x, f, r < 1/np.sqrt(3), np.linalg.det(J)))
print('  G_1/2(0+) = %+.6f ; Sigma_SM = 8 G = %+.5f ; u*Sigma = %+.3e  [%.0fs]' % (G, 8*G, 8*G*5.80705e-4, time.time()-t0))
np.save(os.path.join(HERE, 'root0B_%s.npy' % tag), np.r_[x, 1.0, bg, 1.0, mf, ms])
