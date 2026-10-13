"""R19-12: complete the six gravity rows at the direct S1 root (b_g = 2.936996; Sigma = -0.00044 there), by R18-13's route:
scalar off-axis rows (R17-4 offaxis.py via the E1/U evaluator), Dirac UD off-axis rows (R18-13 dface.py, GL(4,10)),
photon VWa-geo off-axis rows at N = 160 (R18-13 vwface.py), then solve the two own-direction weights (w_d, w_o) of the 12
vectors for face1_tot = face2_tot = 0 and re-evaluate DIRECTLY.  Same logic as R18-13's photface_hi.py (whose root
constants are hard-coded), with S1's edges and stencil.  All imported modules unmodified from ../arch/."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(HERE, '..', 'arch')
sys.path.insert(0, os.path.join(A, 'R18-13')); sys.path.insert(1, os.path.join(A, 'arch18')); sys.path.insert(2, os.path.join(A, 'arch17_4'))
t0 = time.time()
z = np.load(os.path.join(HERE, 'root4k_S1.npy')); bs, bf, r, a, fr, bg, fw, m = z
print('S1 root (b_s, b_f, r, a, fr, b_g, fw, m) =', z, flush=True)
from zz import ZLaw
import offaxis as O
wA = fr*(np.pi - bs); SC, mom = O.xi_off(ZLaw([1.0, 0.0], [bs + wA/2], wA), m, 'U')
print('scalar per real:', {k: '%+.6e' % v for k, v in SC.items()}, '(%.0fs)' % (time.time()-t0), flush=True)
import dface
from content3 import D1q
DI = dface.xi_dirac(D1q(bf, r), m, npan=4, ngl=10)
print('Dirac per field:', {k: '%+.8e' % v for k, v in DI.items()}, '(%.0fs)' % (time.time()-t0), flush=True)
import vwface as V
from photon import photonGw
NS, ND, NV = 4.0, 22.5, 12.0; N = int(sys.argv[1]) if len(sys.argv) > 1 else 160; shifts = (1, 2)
law = photonGw(bg, fw*(np.pi - bg))
sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
F1 = V.xi_geo(law, N, 'face1', a, sets, shifts); F2 = V.xi_geo(law, N, 'face2', a, sets, shifts)
oth = {k: NS*SC[k] + ND*DI[k] for k in ('face1', 'face2', 'body', 'T2g', 'Eg')}
tot1, tot2 = oth['face1'] + NV*F1[0], oth['face2'] + NV*F2[0]
J = NV*np.array([[F1[1]-F1[0], F1[2]-F1[0]], [F2[1]-F2[0], F2[2]-F2[0]]]); w = np.linalg.solve(J, -np.array([tot1, tot2]))
print('N=%d photon per vector at (0,0): face1 %+.6e face2 %+.6e ; totals at (0,0): face1 %+.4e face2 %+.4e ; J det %+.4e ; solved (w_d, w_o) = (%+.6f, %+.6f) (%.0fs)'
      % (N, F1[0], F2[0], tot1, tot2, np.linalg.det(J), *w, time.time()-t0), flush=True)
sol = ((w[0], w[1]),)
G1 = V.xi_geo(law, N, 'face1', a, sol, shifts)[0]; G2 = V.xi_geo(law, N, 'face2', a, sol, shifts)[0]
T = V.xi_geo(law, N, 'T2g', a, sol, shifts)[0]; E = V.xi_geo(law, N, 'Eg', a, sol, shifts)[0]
print('DIRECT at solved (w_d, w_o): per vector T2g %+.9e Eg %+.9e face1 %+.9e face2 %+.9e' % (T, E, G1, G2))
print('TOTALS: face1 %+.3e face2 %+.3e | axial T2g %+.3e Eg %+.3e at this photon N (the S1 axial root used the exact-quadratic photon at N=160)'
      % (oth['face1'] + NV*G1, oth['face2'] + NV*G2, oth['T2g'] + NV*T, oth['Eg'] + NV*E))
print('time %.0fs' % (time.time() - t0))
