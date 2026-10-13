"""R19-35 totals: separable bands from lnn_laplace (converged), Dirac from GL(4,10) (lnn_dirac_GL410.out values), R19-29's
vertex bubbles G(0)/4 at N=128 (root_N128_128_128.out) for the seagull split.  Units: R19-29's lam_nn (= its G(0)/4)."""
import numpy as np
s_h, s_tau, s_e0, p_h, p_tau, p_e0, s_bSF, p_bSF = np.load('sep_lap.npy')
d_h, d_tau, d_e0, d_bphys = 2.164325e-02, -3.042161e-01, -3.205194e+00, -7.363235e-02     # GL(4,10); GL(3,8): 2.164363e-02
G0 = {'s': -2.012298e-01/4, 'd': -1.178118e+00/4*0.25, 'p': -1.537569e+00/4}             # R19-29 vertex bubbles, lam units
W = {'s': 4.0, 'd': 22.5, 'p': 12.0}; H = {'s': s_h, 'd': d_h, 'p': p_h}
lam = sum(W[k]*H[k] for k in W); bub = sum(W[k]*G0[k] for k in W)
e0 = 4*s_e0 + 22.5*d_e0 + 12*p_e0; tau = 4*s_tau + 22.5*d_tau + 12*p_tau
print('per species Hess(nn) (SF): scalar %+.7e  Dirac %+.7e  vector %+.7e' % (s_h, d_h, p_h))
print('per species vertex bubble (R19-29 G(0)/4): scalar %+.7e  Dirac %+.7e  vector %+.7e' % (G0['s'], G0['d'], G0['p']))
print('per species implied seagull (Hess - vertex bubble): scalar %+.7e  Dirac %+.7e  vector %+.7e' % tuple(H[k] - G0[k] for k in 'sdp'))
print('band-level SF bubble (=3 Hess): scalar %+.7e  vector %+.7e ; Dirac interband %+.7e' % (s_bSF, p_bSF, d_bphys))
for k, nm in zip('sdp', ('scalars', 'Dirac', 'vectors')):
    print('  totals %-8s Hess %+.6f  bubble %+.6f  seagull %+.6f' % (nm, W[k]*H[k], W[k]*G0[k], W[k]*(H[k] - G0[k])))
print('TOTAL bubble %+.6f (4x = %+.5f; R19-29: -25.88266)  seagull %+.6f  LAM_NN(bare SF) %+.6f  ratio |lam|/|bubble| = %.4f'
      % (bub, 4*bub, lam - bub, lam, abs(lam/bub)))
print('one-point totals: e0 %+.6f  tau %+.6f  (p = 2 tau = %+.6f, W = e0 + p = %+.6f)' % (e0, tau, 2*tau, e0 + 2*tau))
for nm, v in (('A: one-point counterterms exactly linear in h_SF (bare SF value)', lam),
              ('B: (S) as -e0 sqrt(g), exponential map; P-Tad linear in h_SF', lam - e0/4),
              ('C: one-point counterterms linear in h_lin (g_ij = delta + h)', lam + tau),
              ('D: (S) as -e0 sqrt(g) in h_lin; P-Tad linear in h_lin', lam + tau + e0/4)):
    print('  %-66s lam_nn = %+.5f   |lam|/|bubble| = %.3f' % (nm, v, abs(v/bub)))
c4p8X = -2.926278 + 8*0.1754159
print('crossover (Theorem Q denominator 4 lam + (c4+8X) s^2, c4+8X = %+.4f): ' % c4p8X +
      '  '.join('%s s*^2 = %s' % (nm, ('%.3f' % (-4*v/c4p8X)) if -4*v/c4p8X > 0 else 'none') for nm, v in (('A', lam), ('B', lam - e0/4), ('C', lam + tau), ('D', lam + tau + e0/4))))
