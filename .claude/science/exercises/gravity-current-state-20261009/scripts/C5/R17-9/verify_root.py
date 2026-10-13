"""R17-9: verify an SM-count root: photon resolution N = 48 -> 96 -> 128, 3-knob re-solve at N = 96 (other knobs frozen),
Jacobian rank, m-transfer (scalar/Dirac m = 0.001 re-solve), mu_T2 total, whole-zone v_max per edge."""
import numpy as np, sys, time
import smsolve_lib as L
from scipy.optimize import fsolve
from zz import ZLaw
import dfam
from content3 import D1q
vert = sys.argv[1]; z = np.load(sys.argv[2]); knobs = [int(v) for v in sys.argv[3].split(',')]
L.vert = vert; t0 = time.time()
print('root', z)
for N in (48, 96, 128):
    print('N=%d totals:' % N, L.tot(z, N=N), '(%.0fs)' % (time.time()-t0), flush=True)
J = np.zeros((3, 6)); h = 1e-5
for i in range(6):
    dz = np.zeros(6); dz[i] = h; J[:, i] = (L.tot(z + dz, N=64)[:3] - L.tot(z - dz, N=64)[:3])/(2*h)
print('Jacobian (N=64) rows T2g,Eg,muE; cols b_g,fw_g,b_f,r,b_s,fr_s:\n', J); print('singular values', np.linalg.svd(J, compute_uv=False))
print('det of block', knobs, '%.3e' % np.linalg.det(J[:, knobs]), flush=True)
def g(y, N=96, m=0.01):
    zz = z.copy(); zz[knobs] = y; return L.tot(zz, N=N, m=m)[:3]*1e2
y = fsolve(g, z[knobs], xtol=1e-12); zz = z.copy(); zz[knobs] = y
print('3-knob re-solve at N=96:', zz, 'totals N=96', L.tot(zz, N=96), flush=True)
print('   totals N=128 at that point:', L.tot(zz, N=128), flush=True)
np.save('verified_%s.npy' % vert, zz)
y2 = fsolve(lambda y: g(y, N=96, m=0.001), y, xtol=1e-12); z2 = zz.copy(); z2[knobs] = y2
print('m=0.001 re-solve (N=96):', z2, 'totals', L.tot(z2, N=96, m=0.001), flush=True)
bg, fwg, bf, r, bs, frs = zz
Ls = ZLaw([1.0, 0.0], [bs + frs*(np.pi-bs)/2], frs*(np.pi-bs)); inf = Ls.info()
print('scalar G_w: max|sigma\'| %.9f valleys %s whole-zone v_max(m=0.01) %.6f' % (inf['maxabs'], inf['valleys'], Ls.vmax(0.01)))
law = D1q(bf, r); print('Dirac D1(%.6f, %.6f): r <= 1/sqrt3: %s (Lemma V1 => v_max <= 1); sampled v_max (81^3) %.6f' % (bf, r, r <= 1/np.sqrt(3), dfam.vmax_sample(law, 0.01, 81)))
ph = L.phot(bg, fwg, 48)[1]; print('photon %s: d\' in [%.4f, %.6f] => whole-zone v_max = max d\' = %.6f (attained in the box)' % (ph.name, ph.mindp, ph.maxdp, ph.maxdp))
print('elapsed %.0fs' % (time.time()-t0))
