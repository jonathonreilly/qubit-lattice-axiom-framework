"""R19-9 (c) direct check of the two off-axis rows at the re-solved knobs for radius r (argv; from resolve_sols.npy):
photon face rows evaluated DIRECTLY with R18-13's vwface.xi_geo at N = 224 at the solved (a, w_d, w_o) (no linearization),
scalar/Dirac face rows (R17-4 offaxis; R18-13 dface GL(4,10)), plus the exact-vertex corner 12 C_e(a, w) r^4."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'arch17_4')); sys.path.insert(0, os.path.join(HERE, 'arch18_13')); sys.path.insert(0, os.path.join(HERE, 'arch18'))
import offaxis as O
from zz import ZLaw
import dface as DF, vwface as V
from content3 import D1q
import r199_corner_rows as CR
t0 = time.time(); r = float(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 224
z = np.load(os.path.join(HERE, 'arch18_13', 'root_refR18-9.npy')); fr, bg, fw, m = z[4], z[5], z[6], z[7]
S = np.load('resolve_sols.npy'); row = S[np.argmin(np.abs(S[:, 0] - r))]; x = row[1:7]
bs, bf, rD, a, wd, wo = x
print(f'r = {row[0]}: knobs {x}; model rows {row[7:]}', flush=True)
wA = fr*(np.pi - bs); Xs, _ = O.xi_off(ZLaw([1.0, 0.0], [bs + wA/2], wA), m, 'U')
Xd = DF.xi_dirac(D1q(bf, rD), m, rows=('face1', 'face2'), npan=4, ngl=10)
law = V.photonGw(bg, fw*(np.pi - bg))
ph = {rw: V.xi_geo(law, N, rw, a, settings=((wd, wo),))[0] for rw in ('face1', 'face2')}
C = CR.corner_coeffs(a, wd, wo)
for rw in ('face1', 'face2'):
    tot = 4*Xs[rw] + 22.5*Xd[rw] + 12*ph[rw] + (12*C[rw]*r**4 if r > 0 else 0.0)
    print(f'{rw}: scal {4*Xs[rw]:+.6e} dirac {22.5*Xd[rw]:+.6e} vec(N={N}, direct) {12*ph[rw]:+.9e} corner {12*C[rw]*r**4:+.3e} -> TOTAL {tot:+.3e}', flush=True)
print(f'time {time.time()-t0:.0f} s')
