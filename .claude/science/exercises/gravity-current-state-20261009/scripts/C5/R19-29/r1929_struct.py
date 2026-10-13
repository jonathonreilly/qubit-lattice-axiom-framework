"""R19-29 (a)/(b): structure of the A_1 face block for the root's scalar (U, E1, P1 time components, ultralocal seagull).
Checks:  (1) Ward-contact: e1.Pi(omega).g(xi, omega) is omega-independent (P1 = exact pair-channel W1); e1.Pi.g0 = 0;
         (2) Pi_{g0 g0} = -8 s^4 X, Pi_{g0 gn} = 8 omega s^3 X (X = <nrm^2 (n tau n)^2 / E^3>);
         (3) face1 row from Pi_11(s, s)/s^2 against R17-4's archived evaluator (normalization);
         (4) Schur(s)/s^2 for lam_b = 0 and lam_b != 0.
usage: python r1929_struct.py m N"""
import sys, time, numpy as np
from a1lib import *
t0 = time.time()
m = float(sys.argv[1]); N = int(sys.argv[2])
law, z = root_scalar_law()
sc = Scalar(law, m, N)
print('root scalar edge G_w(b_s=%.7f, fr=%g), m = %g, N = %d (midpoint)' % (z[0], z[4], m, N))
t4 = np.array([1., 0, 0, 0]); nx = np.r_[0., n3]

# (1) Ward-contact test
s = 0.05; q = s*n3
print('\n(1) Ward-contact test at s = %.3f (bubble only, no seagull)' % s)
for w in (0.0, 0.02, 0.05, 0.11, 0.3):
    P = sc.block(q, w, [E1F, gauge(t4, w, q), gauge(nx, w, q)])
    print('   omega=%.3f  e1.Pi.g0 = %+.3e   e1.Pi.gn = %+.10e   g0.Pi.g0 = %+.10e  g0.Pi.gn = %+.6e  gn.Pi.gn = %+.10e' % (w, P[0, 1], P[0, 2], P[1, 1], P[1, 2], P[2, 2]))
# (2) closed forms
ep, em = sc.amps(q); E = ep + em; nrm2 = 1/(8*ep*em); ntn = sc.tau(np.outer(n3, n3))
X = np.sum(sc.W*nrm2*ntn**2/E**3); w = s
print('(2) X = %.10e ; -8 s^4 X = %+.10e ; 8 w s^3 X (w = s) = %+.10e ; gn.Pi.gn closed form -8 s^2 <nrm^2 (ntn)^2/E> = %+.10e'
      % (X, -8*s**4*X, 8*w*s**3*X, -8*s**2*np.sum(sc.W*nrm2*ntn**2/E)))
e1t = sc.tau(E1F[1:, 1:])
print('    e1.Pi.gn closed form -4 s <nrm^2 (e1 tau)(n tau n)/E> = %+.10e' % (-4*s*np.sum(sc.W*nrm2*e1t*ntn/E)))

# (3) face1 row (bubble, degree-0 removed)
print('\n(3) face1 TT row: [Pi_11(s, s) - Pi_11(0, 0)]/s^2, Richardson in s')
vals = []
ss = (0.04, 0.02, 0.01)
for s in ss:
    q = s*n3
    P = sc.block(q, s, [E1F])[0, 0] - sc.block(0*q, 0.0, [E1F])[0, 0]
    vals.append(P/s**2); print('   s=%.3f  row(s) = %+.10e' % (s, vals[-1]))
r1 = [(4*vals[i+1] - vals[i])/3 for i in range(2)]; r2_ = (16*r1[1] - r1[0])/15
print('   Richardson: %+.10e  %+.10e  -> %+.10e' % (r1[0], r1[1], r2_))
try:
    import offaxis as O
    Xr, _ = O.xi_off(law, m, 'U', names=('Eg', 'T2g', 'face1', 'face2'))
    print('   R17-4 archived evaluator (U, E1): face1 = %+.10e  (Eg %+.6e, T2g %+.6e, face2 %+.6e)' % (Xr['face1'], Xr['Eg'], Xr['T2g'], Xr['face2']))
except Exception as ex:
    print('   R17-4 evaluator failed:', ex)

# (4) Schur complement on shell
print('\n(4) on-shell Schur correction Pi_1G Pi_GG^-1 Pi_G1 / s^2 (bubble + ultralocal seagull with total degree-0 block lam_b (tr h)^2)')
for lam in (0.0, 1e-3, 1e-2, 1e-1):
    S = ultralocal_seagull(sc, lam)
    line = []
    for s in (0.08, 0.04, 0.02, 0.01):
        q = s*n3; w = s
        pols = [E1F, gauge(t4, w, q), gauge(nx, w, q)]
        P = sc.block(q, w, pols, seagull=S)
        P1G = P[0, 1:]; PGG = P[1:, 1:]
        sch = P1G @ np.linalg.solve(PGG, P1G)
        line.append('s=%.2f: Pi_1g0=%+.1e Pi_1gn=%+.3e Schur/s^2=%+.4e' % (s, P[0, 1], P[0, 2], sch/s**2))
    print('  lam_b = %g:' % lam); [print('     ', l) for l in line]
print('runtime %.1f s' % (time.time() - t0))
