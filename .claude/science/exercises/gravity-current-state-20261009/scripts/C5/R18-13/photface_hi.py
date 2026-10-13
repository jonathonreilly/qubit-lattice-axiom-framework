"""R18-13 (b)-(c): photon (VWa-geo) off-axis rows at R18-9's root photon edge at grid N; totals with the root's scalar and
Dirac off-axis rows (fixed inputs below, from scal_offaxis_N224.out and dface_root_m0.01.out GL(6,16));
solve the two own-direction placement data (wd, wo) of the 12 vectors for face1_tot = face2_tot = 0 (axial totals are
zero at R18-9's root and own-direction data do not enter them), then re-evaluate DIRECTLY at the solved (wd, wo):
face1, face2, body per vector and totals."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import vwface as V
from photon import photonGw
NS, ND, NV = 4.0, 22.5, 12.0
SC = {'face1': -4.576501e-04, 'face2': -6.277560e-04, 'body': -5.650827e-04, 'Eg': -3.621603e-04, 'T2g': -6.277560e-04}
DI = {'face1': +1.12353499e-03, 'face2': +2.12323617e-03, 'body': +1.89831057e-03, 'Eg': +1.32143161e-04, 'T2g': +1.98456001e-03}
bg, fw, a = 2.9435, 1.0, -0.1760950036
N = int(sys.argv[1]); shifts = tuple(int(v) for v in sys.argv[2].split(',')) if len(sys.argv) > 2 else (1, 2)
law = photonGw(bg, fw*(np.pi - bg)); t0 = time.time()
sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
F1 = V.xi_geo(law, N, 'face1', a, sets, shifts); F2 = V.xi_geo(law, N, 'face2', a, sets, shifts)
print('N=%d shifts=%s per vector at (wd,wo)=(0,0): face1 %+.9e face2 %+.9e | d/dwd: %+.6e %+.6e | d/dwo: %+.6e %+.6e (%.0fs)'
      % (N, shifts, F1[0], F2[0], F1[1]-F1[0], F2[1]-F2[0], F1[2]-F1[0], F2[2]-F2[0], time.time()-t0), flush=True)
oth = {r: NS*SC[r] + ND*DI[r] for r in SC}
tot1, tot2 = oth['face1'] + NV*F1[0], oth['face2'] + NV*F2[0]
print('  totals at (0,0): face1 %+.6e [scal %+.4e dirac %+.4e vec %+.4e]  face2 %+.6e [scal %+.4e dirac %+.4e vec %+.4e]'
      % (tot1, NS*SC['face1'], ND*DI['face1'], NV*F1[0], tot2, NS*SC['face2'], ND*DI['face2'], NV*F2[0]), flush=True)
J = NV*np.array([[F1[1]-F1[0], F1[2]-F1[0]], [F2[1]-F2[0], F2[2]-F2[0]]])
w = np.linalg.solve(J, -np.array([tot1, tot2]))
print('  Jacobian (12 vectors) [[d f1/dwd, d f1/dwo],[d f2/dwd, d f2/dwo]] = %s det %+.4e ; solved (wd, wo) = (%+.8f, %+.8f)' % (J.tolist(), np.linalg.det(J), *w), flush=True)
sol = ((w[0], w[1]),)
G1 = V.xi_geo(law, N, 'face1', a, sol, shifts)[0]; G2 = V.xi_geo(law, N, 'face2', a, sol, shifts)[0]
B = V.xi_geo(law, N, 'body', a, sol, shifts)[0]; T = V.xi_geo(law, N, 'T2g', a, sol, shifts)[0]; E = V.xi_geo(law, N, 'Eg', a, sol, shifts)[0]
print('  DIRECT at solved (wd, wo): per vector T2g %+.9e Eg %+.9e face1 %+.9e face2 %+.9e body %+.9e | O_h resid %+.2e' % (T, E, G1, G2, B, B - (8*G1 + 4*G2 - 3*E)/9), flush=True)
print('  TOTALS at solved: face1 %+.3e face2 %+.3e body %+.3e (body via direct per-vector value) | axial T2g, Eg totals at this N: %+.3e %+.3e (R18-9 root zeroes them at N=224)'
      % (oth['face1'] + NV*G1, oth['face2'] + NV*G2, oth['body'] + NV*B, oth['T2g'] + NV*T, oth['Eg'] + NV*E), flush=True)
print('  time %.0fs' % (time.time() - t0))
