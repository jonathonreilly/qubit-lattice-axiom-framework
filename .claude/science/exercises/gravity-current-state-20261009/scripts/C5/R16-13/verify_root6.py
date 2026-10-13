"""R16-13: verify the content-6 root (2 G(b1) + 2 G_w(b2,w2) real scalars + 1 D1(bf, r) Dirac): higher resolution, m-transfer,
v_max of every edge, Jacobian rank (3x5) and a 3-knob re-solve with (b1, w2) frozen."""
import numpy as np, time, dfam
from content3 import ferm, D1q
from content4 import scalw
from zz import ZLaw
from scipy.optimize import fsolve
t0 = time.time()
n1, n2, ND, m, b1, b2, fr2, bf, r = np.load('root6_2_2_1.npy')
def tot(z, mm=m, n=1 << 14, nu=1500, q=(3, 8)):
    b1, b2, fr2, bf, r = z
    return n1*scalw(b1, 1.0, mm, n=n, nu=nu)[0] + n2*scalw(b2, fr2, mm, n=n, nu=nu)[0] + ND*ferm(bf, r, mm, q=q)[0]
z = np.array([b1, b2, fr2, bf, r])
print('root knobs', z)
print('base resolution  totals:', tot(z))
print('high resolution  totals (scalar n=2^16, nu=4000; fermion GL (4,10)):', tot(z, n=1 << 16, nu=4000, q=(4, 10)))
for mm in (0.03, 0.003, 0.001):
    print('m-transfer m=%.3f totals:' % mm, tot(z, mm))
J = np.zeros((3, 5)); h = 1e-5
for i in range(5):
    dz = np.zeros(5); dz[i] = h
    J[:, i] = (tot(z + dz)[:3] - tot(z - dz)[:3])/(2*h)
print('Jacobian (rows Xi_T2g, Xi_Eg, mu_E; cols b1, b2, w2frac, bf, r):\n', J)
print('singular values:', np.linalg.svd(J, compute_uv=False))
sub = J[:, [1, 3, 4]]; print('det of (b2, bf, r) block: %.3e' % np.linalg.det(sub))
g = lambda y: tot(np.array([b1, y[0], fr2, y[1], y[2]]))[:3]*1e3
y = fsolve(g, [b2 + 0.01, bf - 0.01, r - 0.003], xtol=1e-13)
print('3-knob re-solve (b1, w2 frozen) from a perturbed start: b2=%.10f bf=%.10f r=%.10f  residual' % tuple(y), g(y)/1e3)
for name, L in (('G(b1)', ZLaw([1.0, 0.0], [b1 + (np.pi-b1)/2], np.pi-b1)), ('G_w(b2,w2)', ZLaw([1.0, 0.0], [b2 + fr2*(np.pi-b2)/2], fr2*(np.pi-b2)))):
    inf = L.info(); print('%s: max|sigma\'| %.9f valleys %s v_max(m=0.01) %.6f' % (name, inf['maxabs'], inf['valleys'], L.vmax(0.01)))
law = D1q(bf, r); print('D1(bf, r): W_pi %.4f sampled v_max (121^3) %.6f; Lemma V1 bound 1 (r < 1/sqrt3)' % (law.Wpi, dfam.vmax_sample(law, 0.01, 121)))
print('elapsed %.1fs' % (time.time()-t0))
