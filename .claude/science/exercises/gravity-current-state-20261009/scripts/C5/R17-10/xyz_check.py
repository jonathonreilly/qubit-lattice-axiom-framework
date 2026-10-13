"""R17-10 (a): check the compact pointwise-in-t form of the U+E1 rows against R17-4's fastU (five-moment form).
With W = t f^2 under the 1D tilted measure e^{-tg}dk/E0: x = E[W], y = E[W^2], z = E[W^3], dlam = t^{-1/2} e^{-tm^2} E0^3 dt, c7 = 1/Gamma(7/2):
  Eg   = (5 c7/32) int dlam (2x-1)(y-x^2)
  T2g  = (5 c7/16) int dlam x^2 (2x-1)
  K    = <K6/e^7> = c7 int dlam (z - 15 x y + 30 x^3)        (face1 = (3Eg+T2g)/4 - K/128)
  mu_E = (1/(12 Gamma(3/2))) int t^{-3/2} e^{-tm^2} E0^3 (3x^2 - y) dt"""
import numpy as np, sys; sys.path.insert(0, '.')
from math import gamma
from zz import ZLaw, Mix
from floor_scan import Zz
from fastU import rowsU
NF = 1 << 16
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03)
def xyz_rows(g, f, m, nu=3000, umin=-16.0):
    umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(umin, umax, nu); t = np.exp(u); du = u[1]-u[0]
    W = np.exp(-np.outer(t, g)); E0 = W.mean(1); f2 = f*f
    x = t*(W@f2)/len(g)/E0; y = t**2*(W@(f2**2))/len(g)/E0; z = t**3*(W@(f2**3))/len(g)/E0
    dl = t*du*t**-0.5*np.exp(-t*m*m)*E0**3; c7 = 1/gamma(3.5)
    Eg = 5*c7/32*np.sum(dl*(2*x-1)*(y-x*x)); T2g = 5*c7/16*np.sum(dl*x*x*(2*x-1)); K = c7*np.sum(dl*(z-15*x*y+30*x**3))
    mu = np.sum(t*du*t**-1.5*np.exp(-t*m*m)*E0**3*(3*x*x-y))/(12*gamma(1.5))
    return dict(Eg=Eg, T2g=T2g, K6row=-K/128, face1=(3*Eg+T2g)/4-K/128, mu_E=mu)
for nm, L in [('G(1.0)', A), ('C2', C2), ('C', C), ('Uzero m=.1', Mix([A, C2, C], [1-0.964879-0.007410, 0.964879, 0.007410]))]:
    g, f = L.samples(1 << 13)
    for m in (0.1, 0.01):
        a = rowsU(g, f, m, nu=3000); b = xyz_rows(g, f, m)
        print('%-11s m=%.2f ' % (nm, m) + ' '.join('%s %+.6e/%+.6e' % (k, a[k], b[k]) for k in ['Eg', 'T2g', 'face1', 'K6row', 'mu_E']))
