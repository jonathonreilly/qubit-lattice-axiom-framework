"""R10-1 check 4: (i) a tuned zero of the Dirac photon moment along R8-5's no-box Wilson family r in [0,1];
(ii) residual of the boson-fermion pairing under mass splitting (moment formulas, IR-safe), box curve b1=0.8,b2=1.6;
(iii) sign-definiteness: A_xx <= 0 on the zone for the Clifford-flat curves used (then Lemma N / sign theorem apply).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r85_box_qed_copy import Law
from r101_dirac_moment import moment
from r101_pairing import make_box_curve, wilson_curve

U = 16 * np.pi ** 2
t0 = time.time()
print('(i) no-box Wilson family (R8-5 control law at r = 1; F2 naive at r = 0), m = 0.025, N = 128: photon moment x16pi^2')
prev = None
for r in [0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
    mo = moment(Law(None, None, r, None, None, 0.025, naive_photon=True), 128)
    print('  r=%.2f  total %+8.4f  (a %+8.4f, A %+8.4f, mix %+8.4f)' % (r, mo['tot'], mo['a'], mo['A'], mo['mix']), flush=True)

def flat_moments(cur, m, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W, Sp, Wp = cur['S'](k), cur['W'](k), cur['Sp'](k), cur['Wp'](k)
    h = 1e-4
    v = S ** 2 + W ** 2
    vpp = ((cur['S'](k + h) ** 2 + cur['W'](k + h) ** 2) - 2 * v + (cur['S'](k - h) ** 2 + cur['W'](k - h) ** 2)) / h ** 2
    A = vpp / 2 - 1
    X = S * Sp + W * Wp                      # x.h for the y-axis curve
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    E = np.sqrt(m * m + v[IX] + v[IY] + v[IZ])
    XD = -np.mean(A[IX] * X[IY] ** 2 / (4 * E ** 5))
    XS = np.mean(A[IX] * X[IY] ** 2 / (8 * E ** 5))
    return XD, XS, A

print('(ii) pairing residual under mass splitting, moment formulas (IR-safe), N = 128, x16pi^2')
cv = make_box_curve(0.8, 1.6)
XD0, XS0, A = flat_moments(cv, 0.0, 128)
print('  box curve b1=0.8 b2=1.6: A_xx range on zone [%.3f, %.3f]; X_D(0) = %+.6f, X_S(0) = %+.6f, X_D + 2X_S = %+.1e'
      % (A.min(), A.max(), XD0 * U, XS0 * U, (XD0 + 2 * XS0) * U))
for ms in [0.3, 0.1, 0.03, 0.01]:
    _, XS, _ = flat_moments(cv, ms, 128)
    res = (XD0 + 2 * XS) * U
    print('  m_f = 0, m_s = %.2f: residual %+.3e   residual/m_s^2 = %+.4f' % (ms, res, res / ms ** 2), flush=True)
cw = wilson_curve()
XD0w, XS0w, Aw = flat_moments(cw, 0.0, 128)
print('  Wilson circle: A_xx range [%.3f, %.3f]; X_D(0) = %+.6f, X_S(0) = %+.6f' % (Aw.min(), Aw.max(), XD0w * U, XS0w * U))
print('elapsed %.1fs' % (time.time() - t0))
