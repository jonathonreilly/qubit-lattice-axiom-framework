"""Check of the fast-only rewriting (|sigma'| = 1 a.e., f^2 = g): with Phi0 = E0, a(t) = -2t Phi0'/Phi0, omega = t^{-1/2} e^{-tm^2} Phi0^3,
  Xi_T2g = C_X int omega a^2 (a-1) dt,  Xi_Eg = C_X int omega (a - t a')(a-1) dt,  mu_E = C_mu int omega a (5a - 1 + 2 m^2 t)/(4t) dt,
C_X = 1/(32 Gamma(5/2)), C_mu = 1/(12 Gamma(3/2)). Compared with the moment forms of zz.py on a box + fast-atom measure."""
import numpy as np
from math import gamma
m = 0.1; b = 1.0
xg, wg = np.polynomial.legendre.leggauss(400); k = 0.5*b*(xg+1); w = 0.5*b*wg
atoms = [(0.5, 1.0), (0.3, np.pi - b - 1.0)]
u = np.linspace(-16, np.log(80/m**2)+2, 20000); t = np.exp(u); du = u[1]-u[0]
def mom(p):   # zone mean of g^p e^{-tg} (fast-only: f^2 = g)
    s = (np.exp(-np.outer(t, k*k))@(w*k**(2*p)))
    for lv, ms in atoms: s = s + ms*lv**(2*p)*np.exp(-t*lv*lv)
    return s/np.pi
E0, G1, G2 = mom(0), mom(1), mom(2); F2, F4 = G1, G2
J = 2*t*F2 - E0; cX = 1/(32*gamma(2.5)); cM = 1/(12*gamma(1.5))
XT = cX*np.sum(t*du*t**1.5*np.exp(-t*m*m)*4*G1**2*J); XE = cX*np.sum(t*du*t**1.5*np.exp(-t*m*m)*2*(G2*E0-G1**2)*J)
MU = cM*np.sum(t*du*t**0.5*np.exp(-t*m*m)*E0*(3*F2**2-F4*E0))
a = 2*t*G1/E0; om = t**-0.5*np.exp(-t*m*m)*E0**3
ap = np.gradient(a, u)/t      # da/dt
XT2 = cX*np.sum(t*du*om*a*a*(a-1)); XE2 = cX*np.sum(t*du*om*(a - t*ap)*(a-1)); MU2 = cM*np.sum(t*du*om*a*(5*a-1+2*m*m*t)/(4*t))
print('moment forms: Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % (XT, XE, MU))
print('a-forms     : Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % (XT2, XE2, MU2))
print('a(t) range: min %.4f max %.4f; a < 1/5 for t < %.3g' % (a.min(), a.max(), t[np.argmax(a > 0.2)]))
