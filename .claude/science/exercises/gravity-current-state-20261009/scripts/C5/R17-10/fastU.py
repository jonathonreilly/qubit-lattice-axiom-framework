"""R17-4: U-vertex rows from five 3D moments (derived by IBP in the report, valid for f periodic, f(pi)=0):
  a6=<fx^6/e^7>, a42=<fx^4 fy^2/e^7>, a222=<fx^2 fy^2 fz^2/e^7>, b4=<fx^4/e^5>, b22=<fx^2 fy^2/e^5>
  Eg    = (5/16)(a42 - a222) - (1/16)(b4 - b22)
  T2g   = (5/8) a222 - (1/8) b22            (= face2, identity)
  face1 = -(1/128) a6 + (45/128) a42 - (5/16) a222 - (3/64) b4 + (1/64) b22
  at Eg = T2g = 0: face1 = -(1/128) <K6/e^7>, K6 = sixth cumulant combination (a6 - 15 a42 + 30 a222)."""
import numpy as np
from math import gamma
def rowsU(g, f, m, nu=1500, umin=-16.0, chunk=200, shear=True):
    umax = np.log(80.0/min(m*m, 1.0)) + 2
    u = np.linspace(umin, umax, nu); t = np.exp(u); du = u[1]-u[0]
    f2 = f*f; Ms = {k: np.empty(nu) for k in ['E0', 'F2', 'F4', 'F6']}
    for i0 in range(0, nu, chunk):
        W = np.exp(-np.outer(t[i0:i0+chunk], g))
        Ms['E0'][i0:i0+chunk] = W.mean(1); Ms['F2'][i0:i0+chunk] = W @ f2/len(g)
        Ms['F4'][i0:i0+chunk] = W @ (f2*f2)/len(g); Ms['F6'][i0:i0+chunk] = W @ (f2**3)/len(g)
    E0, F2, F4, F6 = Ms['E0'], Ms['F2'], Ms['F4'], Ms['F6']
    w7 = t*du*t**2.5*np.exp(-t*m*m)/gamma(3.5); w5 = t*du*t**1.5*np.exp(-t*m*m)/gamma(2.5)
    a6 = np.sum(w7*F6*E0*E0); a42 = np.sum(w7*F4*F2*E0); a222 = np.sum(w7*F2**3)
    b4 = np.sum(w5*F4*E0*E0); b22 = np.sum(w5*F2*F2*E0)
    out = dict(Eg=(5/16)*(a42-a222) - (b4-b22)/16, T2g=(5/8)*a222 - b22/8,
               face1=-a6/128 + 45*a42/128 - 5*a222/16 - 3*b4/64 + b22/64, K6row=-(a6 - 15*a42 + 30*a222)/128)
    if shear:
        w3 = t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5))
        out['mu_E'] = float(np.sum(w3*E0*(3*F2**2 - F4*E0)))
    return out
