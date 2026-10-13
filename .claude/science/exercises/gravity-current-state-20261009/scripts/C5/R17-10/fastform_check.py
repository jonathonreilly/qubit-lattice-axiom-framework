"""R17-10: fast-only (|sigma'| = 1 a.e., u = 1) form of face1 after two integrations by parts in t (derived in the report):
  face1 = (c7/128) int dlam [ -63.5 x^3 + 98.75 x^2 - 26.25 x + m^2 t (20 x - 25.5 x^2) - m^4 t^2 x ],
  x = -t Phi'/Phi, dlam = t^{-1/2} e^{-t m^2} Phi^3 dt, Phi = E0 (box + edge, all fast).  Compared with the five-moment form."""
import numpy as np
from math import gamma
L = 50; smin = 0.15; lev = np.linspace(smin, np.pi, L); b = 0.3; m = 0.01
x = np.load('relaxK6_ge_m0.01_b0.30_hi0.80.npy'); M = x[:L].copy()
NU = 6000; u = np.linspace(-16.0, np.log(80.0/(m*m)) + 2, NU); t = np.exp(u); du = u[1]-u[0]
xg, wg = np.polynomial.legendre.leggauss(400); kb = 0.5*b*(xg+1); wb = 0.5*b*wg
def mom(p):  # (1/pi) int over box + edge of h^p e^{-t h^2}, all fast (f^2 = g)
    return (np.exp(-np.outer(t, kb*kb))@(wb*kb**p) + np.exp(-np.outer(t, lev**2))@(M*lev**p))/np.pi
E0, F2, F4, F6 = mom(0), mom(2), mom(4), mom(6)
w7 = t*du*t**2.5*np.exp(-t*m*m)/gamma(3.5); w5 = t*du*t**1.5*np.exp(-t*m*m)/gamma(2.5)
a6 = w7@(F6*E0*E0); a42 = w7@(F4*F2*E0); a222 = w7@F2**3; b4 = w5@(F4*E0*E0); b22 = w5@(F2*F2*E0)
face1_mom = -a6/128 + 45*a42/128 - 5*a222/16 - 3*b4/64 + b22/64
X = t*F2/E0; dl = t*du*t**-0.5*np.exp(-t*m*m)*E0**3; c7 = 1/gamma(3.5)
face1_ibp = c7/128*np.sum(dl*(-63.5*X**3 + 98.75*X**2 - 26.25*X + m*m*t*(20*X - 25.5*X**2) - m**4*t*t*X))
print('all-fast measure (stored M at b=0.3, hi=0.8, m=0.01): face1 five-moment %+.8e | fast IBP form %+.8e | diff %.1e' % (face1_mom, face1_ibp, abs(face1_mom-face1_ibp)))
psi = lambda X: -63.5*X**3 + 98.75*X**2 - 26.25*X
print('m->0 integrand psi(x) roots:', np.roots([-63.5, 98.75, -26.25, 0]), ' psi(0.5) = %+.4f (positive: not sign-definite pointwise)' % psi(0.5))
