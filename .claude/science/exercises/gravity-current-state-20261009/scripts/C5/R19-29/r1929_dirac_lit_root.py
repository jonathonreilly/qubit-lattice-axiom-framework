"""R19-29 bracket at the root Dirac edge (m = 0.01): literal-R19-5 model. y := Im Pi(e1, g0)/s^3 per Dirac field (e:e = 2),
raw face1 shift, and the g0-channel Schur term in R18-13 totals: (5.625 y)^2/(8 X_tot), X_tot from root_N128_128_128.out."""
import sys, numpy as np
sys.argv = ['x', '0.909103708', '0.555604226', '0.01', sys.argv[1]]
src = open('r1929_dirac_lit.py').read().split("t4 = np.array")[0]
exec(src)
t4 = np.array([1., 0, 0, 0]); nx = np.r_[0., n3]
for s in (0.04, 0.02):
    q = s*n3
    P = block(q, s, [E1F, gauge(t4, s, q)], 1)
    print('s=%.2f  Pi(e1,g0) = %+.4e%+.4ei  -> y = Im/s^3 = %+.6e' % (s, P[0, 1].real, P[0, 1].imag, P[0, 1].imag/s**3))
y = P[0, 1].imag/s**3
v = []
for s in (0.02, 0.01):
    d = (block(s*n3, s, [E1F], 1)[0, 0] - block(s*n3, s, [E1F], 0)[0, 0]).real/s**2/4; v.append(d)
print('raw face1 shift literal - rows (dface units, per field): %+.6e, %+.6e -> %+.6e' % (v[0], v[1], (4*v[1] - v[0])/3))
Xt = 1.754159e-01
print('g0-channel Schur term in R18-13 totals (lam_nn != 0): (5.625 y)^2/(8 X_tot) = %+.4e ; raw-row shift x 22.5 = %+.4e' % ((5.625*y)**2/(8*Xt), 22.5*(4*v[1] - v[0])/3))
