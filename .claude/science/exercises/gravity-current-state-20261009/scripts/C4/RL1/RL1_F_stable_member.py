"""RL1 (F): a STABLE 6-layer local operator from the RL1_E scan (exact coefficients recomputed here), then:
 1. stability re-check on a larger contour and a near-axis strip (argument principle);
 2. exact finite-density mean of its realization inverse (Volterra, as RL1_B): Hbar -> 0 (no tail) and W -> cone target?
 3. variance growth: diagonal-ladder rate z* for the unsmeared operator, and for the eps-smeared operator
    N_eps(n) = eps sum_j C_j binom(n,j) eps^j (1-eps)^(n-j)  (mean kernel eps f_C(eps m): same symbol at rho_k = eps rho),
    rung r_eps = E[N_eps(n)^2], n ~ Poisson(m) summed exactly; small-eps law z* ~ eps^{3/4} sqrt(4 pi I1), I1 = int u f_C(u)^2 du.
"""
import numpy as np, sys
from scipy.special import kv, gammaln
from scipy.optimize import brentq
from scipy.stats import poisson
exec(open("RL1_E_layer_family_scan.py").read().split('if __name__ == "__main__":')[0])
L = 6; Fb = basis(L)
A_ = np.array([[np.exp(gammaln(n+(k+1)/2) - gammaln(n+1)) for n in range(L)] for k in range(3)])
null = np.linalg.svd(A_)[2][3:]
path = contour(); Tc = trans(Fb, path); Tsmall = trans(Fb, np.array([1e-3]))[0]; Tz01 = trans(Fb, np.array([1e-2]))[0]
best = None
for t in np.linspace(0, np.pi, 91):
    for p in np.linspace(0, 2*np.pi, 181)[:-1]:
        q = np.array([np.cos(t), np.sin(t)*np.cos(p), np.sin(t)*np.sin(p)])
        res = analyse(q @ null, Fb, Tc, path, Tsmall)
        if res is None or res[0] != 0 or res[1] <= 0: continue
        if best is None or res[2] < best[2]: best = res
nz, c2, zs, C = best
print("stable member C =", np.array2string(C, precision=6), " c2 = %.4f  ladder var rate z* = %.3f" % (c2, zs))
print("moment check (k=0,1,2):", A_ @ C)
def Sfun(z): return trans(Fb, np.atleast_1d(z)) @ C - 1.0
for (x0, x1, y) in [(1e-3, 20.0, 40.0), (1e-4, 0.03, 40.0), (0.03, 8.0, 12.0)]:
    pth = contour(x0, x1, y, 6000); v = Sfun(pth); ph = np.unwrap(np.angle(v))
    print("  zeros in [%g,%g]x[-%g,%g]: %.3f" % (x0, x1, y, y, -(ph[-1]-ph[0])/(2*np.pi)))
# Volterra mean
exec(open("RL1_B_bd_mean_volterra.py").read().split('if __name__ == "__main__":')[0].replace('def fc(s):', 'def fc_old(s):'))
def fstab(s):
    m = np.pi*np.asarray(s, float)**2/24
    return np.exp(-m)*sum(C[n]*m**n/np.exp(gammaln(n+1)) for n in range(L))
taus, H = solve(fstab, 30.0, 0.02, 0.04)
sig = taus**2; Wc = np.concatenate([[0], np.cumsum(0.5*(H[1:]+H[:-1])*np.diff(sig))])
print("\nmean inverse of the stable member (Volterra):  tau | Hbar | W = int Hbar dsigma;  continuum target W -> 1/(2 pi c2) = %.5f" % (1/(2*np.pi*c2)))
for T in [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30]:
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
for eps in [1.0, 0.3, 0.1, 0.03, 0.01, 0.003]:
    z = rate_eps(eps); print("  eps=%-6g  ladder var rate z* = %.4e /ell   law eps^{3/4} sqrt(4 pi I1) = %.4e   ratio %.3f" % (eps, z, eps**0.75*np.sqrt(4*np.pi*I1), z/(eps**0.75*np.sqrt(4*np.pi*I1))))
    sys.stdout.flush()
