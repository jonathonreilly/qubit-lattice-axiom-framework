"""R16-13: whole-zone v_max at the closest approach (root3_4_1_M): scalar G(bA) (separable bisection, zz.py) and Dirac D1(bf, r) (sampled lower bound; Lemma V1 upper bound 1)."""
import numpy as np, dfam
from zz import ZLaw
from content3 import D1q
Ns, ND, m, bA, bf, r = np.load('root3_4_1_M.npy')
L = ZLaw([1.0, 0.0], [bA + (np.pi-bA)/2], np.pi-bA)
print('G(%.6f): max|sigma\'| %.9f valleys %s v_max(m=%.2f) %.6f' % (bA, L.info()['maxabs'], L.info()['valleys'], m, L.vmax(m)))
law = D1q(bf, r)
print('D1(%.6f, %.6f): W_pi %.4f  sampled v_max(m=%.2f, 81^3) %.6f, (121^3) %.6f; Lemma V1 bound 1' % (bf, r, law.Wpi, m, dfam.vmax_sample(law, m, 81), dfam.vmax_sample(law, m, 121)))
