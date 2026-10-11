"""RL2 (C): ladder growth rates for the three operators (all three, incl. op1 which RL1 F5 skipped as a duplicate pick).
 (i) bare shared-path ladder (RL1): rung eps^2 E[g_eps(n)^2], root of rtilde(z) = 1; small-eps law z* = eps^{3/4} sqrt(4 pi I1)/l
     with I1 = int u f_C(u)^2 du.  In l_k units: z* l_k = sqrt(4 pi I1 eps) (+ pre-asymptotic corrections).
 (ii) node-only renormalised ladder (chaos expansion, first-order-in-insertion amplitudes): rung rho Hbar^2 = eps rho_k h_k^2,
     small-eps law z_h* l_k = sqrt(4 pi I_h eps), I_h = int tau h_k(tau)^2 dtau (h_k = flat mean inverse, RL1 Volterra solver).
"""
import numpy as np, os, sys
from scipy.special import kv, gammaln
from scipy.optimize import brentq
from scipy.stats import poisson
from rl2_core import OPS, fvals
RL1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "RL1")
src = open(os.path.join(RL1, "RL1_B_bd_mean_volterra.py")).read().split('if __name__ == "__main__":')[0]
xg2, wg2 = np.polynomial.legendre.leggauss(400)
def rate_eps(C, eps):
    L = len(C); tmax = 9.0*eps**-0.25
    T2 = 0.5*tmax*(xg2+1); W2 = 0.5*tmax*wg2; m = np.pi*T2**4/24
    r = np.zeros_like(T2)
    for i, mi in enumerate(m):
        nmax = int(mi + 12*np.sqrt(mi+1) + 30); n = np.arange(nmax+1); pn = poisson.pmf(n, mi)
        if eps < 1:
            Ne = eps*sum(C[j]*np.exp(gammaln(n+1)-gammaln(j+1)-gammaln(np.maximum(n-j, 0)+1) + j*np.log(eps) + (n-j)*np.log1p(-eps))*(n >= j) for j in range(L))
        else:
            Ne = np.where(n < L, np.concatenate([C, np.zeros(max(0, nmax+1-L))])[:nmax+1], 0.0)
        r[i] = np.sum(pn*Ne**2)
    g = lambda z: 4*np.pi*np.sum(W2*T2**3*r*kv(1, z*T2)/(z*T2)) - 1.0
    return brentq(g, 1e-6, 50.0)
for o, C in enumerate(OPS):
    u = np.linspace(0, 12, 200001); I1 = np.trapezoid(u*fvals(C, u**2)**2, u)
    g = {}; exec(src, g)
    taus, H = g["solve"](lambda s: fvals(C, s), 16.0, 0.02, 0.05)
    Ih = np.trapezoid(taus*H**2, taus)
    print("op%d: I1 = %.5f  (bare small-eps law z* l_k = %.4f sqrt(eps)) ; I_h = int tau hbar^2 (tau<=16) = %.5f  (node ladder: z_h* l_k = %.4f sqrt(eps))"
          % (o, I1, np.sqrt(4*np.pi*I1), Ih, np.sqrt(4*np.pi*Ih)))
    for eps in [1.0, 0.5, 0.25, 0.125, 0.01]:
        z = rate_eps(C, eps)        # in units of 1/l ; convert to 1/l_k: z l_k = z * eps^{-1/4}
        print("   eps=%-6g bare-ladder variance rate: %.4f /l = %.4f /l_k  (law %.4f /l_k; ratio %.3f) -> predicted sd rate %.3f /l_k"
              % (eps, z, z*eps**-0.25, np.sqrt(4*np.pi*I1*eps), z*eps**-0.25/np.sqrt(4*np.pi*I1*eps), 0.5*z*eps**-0.25))
    sys.stdout.flush()
