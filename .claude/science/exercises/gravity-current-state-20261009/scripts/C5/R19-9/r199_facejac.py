"""R19-9 (c), part 1: Jacobian of the two off-axis totals (face1, face2) in the four AXIAL knobs (b_s, b_f, r_D, a), at the
vR18-9 retuned root (arch18_13/root_refR18-9.npy), with R18-13's off-axis evaluators UNMODIFIED:
  scalars: R17-4 offaxis.xi_off (U, E1) via ZLaw as in R18-9's scal_offaxis.py;  Dirac: R18-13 dface.xi_dirac (UD, GL(3,8));
  photon: R18-13 vwface.xi_geo at N (argv), own-direction data (w_d, w_o) at R18-13's N = 224 solve.
Counts as R18-9: 4 real scalars, 22.5 Dirac, 12 vectors. Central differences."""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'arch17_4'))
import offaxis as O
from zz import ZLaw
sys.path.insert(0, os.path.join(HERE, 'arch18_13')); sys.path.insert(0, os.path.join(HERE, 'arch18'))
import dface as DF, vwface as V
from content3 import D1q
t0 = time.time()
z = np.load(os.path.join(HERE, 'arch18_13', 'root_refR18-9.npy')); bs, bf, rD, a, fr, bg, fw, m = z
NPH = int(sys.argv[1]) if len(sys.argv) > 1 else 96
WD, WO = -1.17155412, -0.19541845
NS, ND, NV = 4, 22.5, 12
def scal(bs_):
    wA = fr*(np.pi - bs_); law = ZLaw([1.0, 0.0], [bs_ + wA/2], wA)
    X, _ = O.xi_off(law, m, 'U'); return np.array([X['face1'], X['face2']])
def dirac(bf_, r_):
    X = DF.xi_dirac(D1q(bf_, r_), m, rows=('face1', 'face2'), npan=3, ngl=8); return np.array([X['face1'], X['face2']])
law = V.photonGw(bg, fw*(np.pi - bg))
def phot(a_):
    return np.array([V.xi_geo(law, NPH, row, a_, settings=((WD, WO),))[0] for row in ('face1', 'face2')])
print(f'root (b_s, b_f, r_D, a) = ({bs:.9f}, {bf:.9f}, {rD:.9f}, {a:.9f}), m = {m}; photon N = {NPH}', flush=True)
s0 = scal(bs); print(f'scalar per field face1/face2 {s0} [{time.time()-t0:.0f}s]', flush=True)
J = np.zeros((2, 4))
h = 1e-4
J[:, 0] = NS*(scal(bs + h) - scal(bs - h))/(2*h); print(f'd/db_s {J[:,0]} [{time.time()-t0:.0f}s]', flush=True)
J[:, 1] = ND*(dirac(bf + h, rD) - dirac(bf - h, rD))/(2*h); print(f'd/db_f {J[:,1]} [{time.time()-t0:.0f}s]', flush=True)
J[:, 2] = ND*(dirac(bf, rD + h) - dirac(bf, rD - h))/(2*h); print(f'd/dr_D {J[:,2]} [{time.time()-t0:.0f}s]', flush=True)
ha = 1e-3
J[:, 3] = NV*(phot(a + ha) - phot(a - ha))/(2*ha); print(f'd/da {J[:,3]} [{time.time()-t0:.0f}s]', flush=True)
np.save('facejac.npy', J)
print('J_face,axial (rows face1, face2; cols b_s, b_f, r_D, a) =\n', J)
print(f'time {time.time()-t0:.0f} s')
