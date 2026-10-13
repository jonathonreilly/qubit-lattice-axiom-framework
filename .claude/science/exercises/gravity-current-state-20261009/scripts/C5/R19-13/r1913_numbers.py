"""R19-13 bookkeeping numbers (Planck units, a = l_P; RECALLED: H0 = 67.4 km/s/Mpc, Omega_L = 0.685, l_P, t_P)."""
import numpy as np
from r1913_lib import chain_corr
H0 = 67.4/3.0857e19*5.391e-44; rhoL = 0.685*3*H0**2/(8*np.pi); lP = 1.616e-35; tP = 5.391e-44
print('H0 = %.4e /t_P ; rho_L = %.4e ; 1/H0 = %.3e t_P' % (H0, rhoL, 1/H0))
print('persistent threshold: 3 dE / a^3 per Hubble time < rho_L  <=>  dE < %.3e' % (rhoL/3))
print('registered threshold: 3 H dE tau / a^3 < rho_L  <=>  dE tau < %.3e' % (rhoL/(3*H0)))
# R = 0 with per-q optimal new-site state (new plane in its own 2D ground state = R19-10 "P-plane")
NQ = 400; t = (np.arange(NQ)+0.5)/NQ; q = np.pi*t
QY, QZ = np.meshgrid(q, q, indexing='ij'); S = 4*np.sin(QY/2)**2 + 4*np.sin(QZ/2)**2
for m in (0.0, 1.0):
    Ms = np.sqrt(m*m + S).ravel(); Mu = np.unique(np.round(Ms, 9))
    tab = {}
    for M in Mu:
        Gx, Gp, e0 = chain_corr(float(max(M, 1e-9)), 1)
        tab[M] = np.sqrt(M*M + 2)/2 + Gx[1] - e0
    v = np.mean([tab[x] for x in np.round(Ms, 9)])
    print('scalar m=%g: R=0 per-q optimum (new plane in its 2D GS) dE = %.6f per site [R19-10 P-plane Lp=16: %s]' % (m, v, {0.0: '0.040813', 1.0: '0.026126'}[m]))
for R, lab in ((1.66e23, 'scalar persistent, proved-inequality (asymptotic evaluation)'), (4.6e24, 'scalar persistent, central (fit)'),
               (7.9e13, 'scalar registered tau=R'), (1.43e11, 'scalar registered tau=1 t_P'), (1.71e18, 'scalar m a=1e-17 persistent')):
    print('  R = %.2e a = %.2e m ; light-crossing R/c = %.2e s = %.2e of 1/H0' % (R, R*lP, R*tP, R*H0))
print('ball (point) insertions: concurrent overlapping events per site = 4 pi H R^4 (tau = R): equals 1 at R = %.2e a' % ((4*np.pi*H0)**-0.25))
print('plane insertions: overlap count = 2 R^2 H (tau = R): equals 1 at R = %.2e a' % ((2*H0)**-0.5))
for R in (1e15, 1.66e23, 4.6e24):
    print('  R=%.2e: ball overlap %.2e ; plane overlap %.2e' % (R, 4*np.pi*H0*R**4, 2*H0*R**2))
