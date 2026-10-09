"""Supervisor check (E1): small-epsilon limit of the BD 4D noise gain A^2 = E[sum_y w_xy^2].

Units: l_k = 1, rho = 1/eps.  Weight of event y relative to -phi(x): w = eps*f4(n, eps),
n ~ Poisson(rho*V), V = pi*tau^4/24 (4D Alexandrov interval of proper time tau).
Past truncated at time T >> tau: measure rho*d^4y -> 2*pi*rho*T^2 * tau dtau (asymptotic).
=> A^2 = (pi/2)*sqrt(24*rho/pi) * T^2 * Int E_m[w^2] m^(-1/2) dm   (m = rho*V)
Small eps: E_m[w^2] -> eps^2 f_inf(eps m)^2  =>  A^2 -> C_inf * eps * T^2,
C_inf = (pi/2)*sqrt(24/pi) * Int_0^inf f_inf(u)^2 u^(-1/2) du,  f_inf = e^-u (1 - 9u + 8u^2 - 4/3 u^3).
Also evaluates the exact Poisson average at finite eps (0.2, 0.1, 0.05, 0.01, 1e-3).
"""
from mpmath import mp, mpf, quad, exp, sqrt, pi, inf
import math
mp.dps = 30

def f_inf(u):
    return exp(-u)*(1 - 9*u + 8*u**2 - mpf(4)/3*u**3)

I_inf = quad(lambda u: f_inf(u)**2/sqrt(u), [0, 1, 5, 20, inf])
C_inf = (pi/2)*sqrt(24/pi)*I_inf
print("Int f_inf^2 u^-1/2 du =", I_inf)
print("C_inf (A^2 / (eps T^2), eps->0) =", C_inf)

def f4(n, e):
    q = 1 - e
    return q**n*(1 - 9*e*n/q + 8*e**2*n*(n-1)/q**2 - mpf(4)/3*e**3*n*(n-1)*(n-2)/q**3)

def Ew2(m, e, nmax):
    # exact Poisson average of (e f4(n,e))^2, n ~ Poisson(m)
    s = mpf(0); p = exp(-m)
    for n in range(nmax):
        if n > 0: p *= m/n
        s += p*(e*f4(n, e))**2
    return s

for e in [0.2, 0.1, 0.05, 0.01, 0.001]:
    e = mpf(e); rho = 1/e
    # integrate over m with nmax adaptive
    def integrand(m):
        nmax = int(m + 12*math.sqrt(float(m)+1) + 40)
        return Ew2(m, e, nmax)/sqrt(m)
    mmax = 60/e
    pts = [0, 1, 5, 1/e, 3/e, 10/e, mmax]
    pts = sorted(set([mpf(x) for x in pts]))
    J = quad(integrand, pts, maxdegree=8)
    A2coef = (pi/2)*sqrt(24*rho/pi)*J      # A^2 / T^2
    print(f"eps={float(e):7.3g}  A^2/(eps T^2) = {float(A2coef/e):.6f}   ratio to C_inf = {float(A2coef/e/C_inf):.4f}")
