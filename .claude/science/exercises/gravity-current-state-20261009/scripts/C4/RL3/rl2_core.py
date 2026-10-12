"""RL2 core: the three distinct stable L=6 layer operators (RL1_F4b rows 0,1,2; rows 3-5 are antipodal duplicates),
renormalised so the 4D symbol has ftilde(0) = 1 EXACTLY (massless), plus their s-Laplace transforms fhat(p).
Conventions (rho = 1, l = 1): f(s) = sum_n C_n e^{-m} m^n/n!,  m = pi s^2/24,  s = tau^2.
  4D symbol  ftilde(z) = 2 pi int s f(s) K1(z sqrt s)/(z sqrt s) ds ;  ftilde(0) = (pi/2) int s ln s f(s) ds (moments 0,1,2 vanish).
  s-Laplace  fhat(p) = int_0^inf e^{-p s} f(s) ds = -M3 p^3/6 + ...  (M_n = int s^n f ds).
"""
import numpy as np
from scipy.special import gammaln, kv
from scipy.interpolate import CubicSpline
import os
HERE = os.path.dirname(os.path.abspath(__file__))
RL1 = os.path.join(os.path.dirname(HERE), "RL1")
L = 6
_raw = np.load(os.path.join(RL1, "RL1_F4b_stable_L6.npy"))[:3]
xs, ws = np.polynomial.legendre.leggauss(3000)
S = 11.0*(xs+1); WS = 11.0*ws          # s in [0,22]: m(22) = 63
def fvals(C, s):
    m = np.pi*np.asarray(s, float)**2/24
    return np.exp(-m)*sum(C[n]*m**n/np.exp(gammaln(n+1)) for n in range(len(C)))
def moments(C, nmax=24):
    f = fvals(C, S); return np.array([np.sum(WS*S**n*f) for n in range(nmax+1)])
def ft0(C):
    f = fvals(C, S); return (np.pi/2)*np.sum(WS*S*np.log(S)*f)
def ftilde(C, z):
    f = fvals(C, S); z = np.atleast_1d(np.asarray(z, complex)); y = z[:, None]*np.sqrt(S)[None, :]
    return 2*np.pi*((kv(1, y)/y) @ (WS*S*f))
OPS = []
for C in _raw:
    C = C/ft0(C)                      # exact massless normalisation
    OPS.append(C)
def c2_of(C):
    """S(z) = ftilde(z) - 1 = -c2 z^2 + O(z^4 ln z), c2 = -(pi/16) int s^2 ln s f ds (K1 expansion; M0=M1=M2=0)."""
    f = fvals(C, S); return -(np.pi/16)*np.sum(WS*S**2*np.log(S)*f)
def fhat_factory(C):
    """returns fhat(p) vectorised for p > 0 via spline of phi(p) = fhat(p) (1+p)^4 / p^3 in log p."""
    Mn = moments(C)
    lp = np.linspace(np.log(1e-6), np.log(1e8), 3001); P = np.exp(lp)
    out = np.empty_like(P)
    xg, wg = np.polynomial.legendre.leggauss(600)
    for i, p in enumerate(P):
        if p < 0.03:
            n = np.arange(3, 25); out[i] = np.sum((-p)**n*Mn[3:25]/np.exp(gammaln(n+1)))
        else:
            smax = min(22.0, 80.0/p); s = 0.5*smax*(xg+1); w = 0.5*smax*wg
            out[i] = np.sum(w*np.exp(-p*s)*fvals(C, s))
    phi = out*(1+P)**4/P**3
    sp = CubicSpline(lp, phi)
    def fhat(p):
        p = np.asarray(p, float); pc = np.clip(p, 1e-6, 1e8)
        val = sp(np.log(pc))*pc**3/(1+pc)**4
        return np.where(p > 1e8, Mn[0]*0 + fvals(C, 0.0)/np.maximum(p, 1e-300), val)
    return fhat, Mn
if __name__ == "__main__":
    BD = np.array([1., -9., 16., -8.])
    print("BD check: ftilde(0) = %.6f (BD is normalised by beta, value 1 expected) ; c2 = %.6f (expected sqrt6/4 = %.6f)" % (ft0(BD), c2_of(BD), np.sqrt(6)/4))
    zt = np.array([0.05, 0.1]); print("   direct S(z)/z^2 at z=0.05,0.1:", (ftilde(BD, zt).real-1)/zt**2)
    for k, C in enumerate(OPS):
        Mn = moments(C)
        print("op %d: C = %s" % (k, np.array2string(C, precision=6)))
        print("   renorm factor vs RL1 row: %.8f ; moments M0..M3 = %s" % (C[0]/_raw[k][0], np.array2string(Mn[:4], precision=3)))
        print("   ftilde(0) = %.10f ; ftilde(1e-3) = %.10f ; c2 = %.6f ; W_target = 1/(2 pi c2) = %.6f" %
              (ft0(C), ftilde(C, 1e-3)[0].real, c2_of(C), 1/(2*np.pi*c2_of(C))))
        fh, _ = fhat_factory(C)
        pp = np.array([1e-3, 0.03, 0.0300001, 1.0, 10.0, 1e3])
        print("   fhat(p) at", pp, "=", fh(pp), " ; check (pi/2) int fhat/x^2 dx =", end=" ")
        x = np.exp(np.linspace(np.log(1e-6), np.log(1e8), 400001)); print("%.6f" % ((np.pi/2)*np.trapezoid(fh(x)/x**2*x, np.log(x))))
