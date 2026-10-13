"""R19-29 lam_nn = 0 branch: the same re-solve with the Dirac kernel weighted uniformly (22.5 x E1F kernel instead of
R18-13's 22.5 x 1/4). Photon parts from the exactly linear fits of resolve_N128.out minus the R18-13-convention scalar+Dirac totals."""
import numpy as np
from scipy.optimize import brentq
wd0, J11 = -1.171554, 1.67645
s = np.array([1.434160e-04, -5.364369e-03, 9.589168e-04]); d = np.array([-4.630016e-03, -7.228331e-02, 1.729653e-02])
sd_conv = 4*s + 5.625*d; sd_uni = 4*s + 22.5*d
kg = lambda w: 2.24653706*w + 1.35124289 - sd_conv[0]
cg = lambda w: 2.28250037*w - 0.252201334 - sd_conv[1]
Xg = 1.754162e-01 - sd_conv[2]
for lab, sd in (('R18-13 convention', sd_conv), ('uniform Dirac weight', sd_uni)):
    kap = lambda w: kg(w) + sd[0]; den = lambda w: cg(w) + sd[1] + 8*(Xg + sd[2])
    f = lambda w: J11*(w - wd0) - kap(w)**2/den(w)
    wp = brentq(den, -10, 10)
    print('%s: Schur term at R18-13 solution %+.4f; gauge-block singular point w_d = %+.4f' % (lab, -kap(wd0)**2/den(wd0), wp))
    for lo, hi in ((-10, wp - 1e-6), (wp + 1e-6, 10)):
        g = np.linspace(lo, hi, 40001); fv = f(g)
        for i in range(len(g)-1):
            if fv[i]*fv[i+1] < 0:
                r = brentq(f, g[i], g[i+1]); h = 1e-6; dd = (f(r+h) - f(r-h))/(2*h)
                print('   root w_d = %+.5f (distance to singular point %+.4f), d face1/d w_d = %+.4f, face-block det %+.4f' % (r, r - wp, dd, dd*6.94286))
