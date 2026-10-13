"""R19-35: separable bands (scalar, photon) by exact 1D-moment Laplace forms (no derivatives, no 3D grid):
<u^4/E^3> = G(3/2)^-1 int t^{1/2} e^{-tm^2}[F4 E0^2/2 + 3 F2^2 E0/2];  tau = (1/4) G(1/2)^-1 int t^{-1/2} e^{-tm^2} F2 E0^2;
<E> = -(2 sqrt pi)^-1 int t^{-3/2}(e^{-tm^2}E0^3 - 1).  Hess(nn) = 2w(-1/24)<u^4/E^3>, bubble_SF = 3 Hess(nn).  Dirac from lnn_fast (GL)."""
import os, sys, numpy as np
from math import gamma, sqrt, pi
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18')); sys.path.insert(0, HERE)
from zz import ZLaw, mu_E, moments_from
from photon import photonGw
BS, BF, RR, AST, FR, BG, FW, M0 = np.load(os.path.join(HERE, 'root_refR18-9.npy'))
def lap(g, f, m, w, nu=4000, umin=-20.0):
    umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(umin, umax, nu); t = np.exp(u); dt = t*(u[1] - u[0])
    E0 = np.empty(nu); F2 = np.empty(nu); F4 = np.empty(nu)
    for i in range(0, nu, 200):
        mm = moments_from(g, f, t[i:i+200]); E0[i:i+200] = mm['E0']; F2[i:i+200] = mm['F2']; F4[i:i+200] = mm['F4']
    em = np.exp(-t*m*m)
    u4 = np.sum(dt*t**0.5*em*(0.5*F4*E0**2 + 1.5*F2**2*E0))/gamma(1.5)
    tau = 2*w*0.25*np.sum(dt*t**-0.5*em*F2*E0**2)/gamma(0.5)
    Em = -np.sum(dt*t**-1.5*(em*E0**3 - 1))/(2*sqrt(pi))
    return dict(hnn=2*w*(-u4/24), bubSF=2*w*(-u4/8), seagSF=2*w*(u4/12), tau=tau, e0=w*Em, muE=2*w*mu_E(g, f, m))
wA = FR*(np.pi - BS); Ls = ZLaw([1.0, 0.0], [BS + wA/2], wA); Lp = photonGw(BG, FW*(np.pi - BG))
for n in (1 << 14, 1 << 16):
    gs, fs = Ls.samples(n); gp, fp = Lp.samples(n)
    s = lap(gs, fs, M0, 0.5); out = ['n=2^%d scalar: ' % np.log2(n) + '  '.join('%s %+.7e' % kv for kv in s.items())]
    for mr in (1e-3, 1e-4):
        p = lap(gp, fp, mr, 1.0); out.append('        photon reg %.0e: ' % mr + '  '.join('%s %+.7e' % kv for kv in p.items()))
    print('\n'.join(out), flush=True)
np.save(os.path.join(HERE, 'sep_lap.npy'), np.array([s['hnn'], s['tau'], s['e0'], p['hnn'], p['tau'], p['e0'], s['bubSF'], p['bubSF']]))
