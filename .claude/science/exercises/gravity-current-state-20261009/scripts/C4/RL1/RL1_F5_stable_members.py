"""RL1 (F5): the same analysis as RL1_F (mean inverse by Volterra; ladder variance rate vs eps) for the members found STABLE by the
resolved re-scan RL1_F4b (contour [0.003,20]x[-12,12], 1500 nodes).  Coefficients loaded from RL1_F4b_stable_L6.npy (exact)."""
import numpy as np, sys
from scipy.special import kv, gammaln
from scipy.optimize import brentq
from scipy.stats import poisson
L = 6
allC = np.load("RL1_F4b_stable_L6.npy")
A_ = np.array([[np.exp(gammaln(n+(k+1)/2) - gammaln(n+1)) for n in range(L)] for k in range(3)])
for C in allC[[0, 3, 5]]:
  print("\n==== member C =", np.array2string(C, precision=5), " moments:", A_ @ C)
  if True:
    # Volterra mean
    exec(open("RL1_B_bd_mean_volterra.py").read().split('if __name__ == "__main__":')[0].replace('def fc(s):', 'def fc_old(s):'))
    def fstab(s):
        m = np.pi*np.asarray(s, float)**2/24
        return np.exp(-m)*sum(C[n]*m**n/np.exp(gammaln(n+1)) for n in range(L))
    taus, H = solve(fstab, 40.0, 0.02, 0.05)
    sig = taus**2; Wc = np.concatenate([[0], np.cumsum(0.5*(H[1:]+H[:-1])*np.diff(sig))])
    print("\nmean inverse of the stable member (Volterra):  tau | Hbar | W = int Hbar dsigma;  continuum target W -> 1/(2 pi sqrt6/4) [c2 not normalised here] = %.5f" % (1/(2*np.pi*(np.sqrt(6)/4))))
    for T in [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 35, 40]:
        i = np.argmin(abs(taus-T)); print("  %5.2f %+.5e  %+.5f" % (taus[i], H[i], Wc[i]))
    # ladder rates vs eps
    I1 = None
    u = np.linspace(0, 12, 200001); mu = np.pi*u**4/24
    fu = np.exp(-mu)*sum(C[n]*mu**n/np.exp(gammaln(n+1)) for n in range(L)); I1 = np.trapezoid(u*fu**2, u)
    print("\nI1 = int u f_C(u)^2 du = %.5f ;  small-eps law: z*_var = eps^{3/4} sqrt(4 pi I1) = eps^{3/4} * %.4f" % (I1, np.sqrt(4*np.pi*I1)))
    xg2, wg2 = np.polynomial.legendre.leggauss(400)
    def rate_eps(eps):
        tmax = 9.0*eps**-0.25
        T2 = 0.5*tmax*(xg2+1); W2 = 0.5*tmax*wg2; m = np.pi*T2**4/24
        r = np.zeros_like(T2)
        for i, mi in enumerate(m):
            nmax = int(mi + 12*np.sqrt(mi+1) + 30); n = np.arange(nmax+1)
            pn = poisson.pmf(n, mi)
            Ne = eps*sum(C[j]*np.exp(gammaln(n+1)-gammaln(j+1)-gammaln(np.maximum(n-j, 0)+1) + j*np.log(eps) + (n-j)*np.log1p(-eps))*(n >= j)
                         for j in range(L)) if eps < 1 else np.where(n < L, np.concatenate([C, np.zeros(max(0, nmax+1-L))])[:nmax+1], 0.0)
            r[i] = np.sum(pn*Ne**2)
        g = lambda z: 4*np.pi*np.sum(W2*T2**3*r*kv(1, z*T2)/(z*T2)) - 1.0
        return brentq(g, 1e-6, 50.0)
    for eps in [1.0, 0.1, 0.01]:
        z = rate_eps(eps); print("  eps=%-6g  ladder var rate z* = %.4e /ell   law eps^{3/4} sqrt(4 pi I1) = %.4e   ratio %.3f" % (eps, z, eps**0.75*np.sqrt(4*np.pi*I1), z/(eps**0.75*np.sqrt(4*np.pi*I1))))
        sys.stdout.flush()
