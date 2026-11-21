# Check of row 1081 Corollary N2-SMALL (L116-L118): n = 2, one sheet, t = 0.
# Bessel I by its power series (independent of the row's scripts).
import numpy as np
from math import exp, factorial
from math import lgamma, log
def I(nu, x, K=200):
    t = exp(nu*log(x/2) - lgamma(nu+1)); s = 0.0
    for k in range(K):
        s += t; t *= (x/2)**2/((k+1)*(k+1+nu))
    return s
def n0_and_bound(beta, nmax=40):
    ns = np.arange(1, nmax+1)
    a = np.array([I(n, beta)/I(1, beta) for n in ns])
    k = np.array([[I(abs(n-m), beta) - I(n+m, beta) for m in ns] for n in ns])
    A = np.diag(a)@k@np.diag(a)
    w, V = np.linalg.eigh(A); phi0 = V[:,-1]; lam0 = w[-1]
    c = (ns**2-1)/2.
    n0 = float(c@(phi0**2))
    exact_bound = exp(beta)*max(c*a**2)/lam0           # e^beta sup(c a^2)/lambda_0
    hand_bound = (3*beta**2/32)*exp(beta)/(1+beta**2/8) # the row's closed form
    return n0, lam0, 2*I(1,beta)/beta, exact_bound, hand_bound
print("beta n0(0) lambda0 A(1,1) exactbound handbound")
for beta in [0.5, 1.0, 1.25, 1.5]:
    print(beta, *["%.6f" % v for v in n0_and_bound(beta)])
print("hand arithmetic at 3/2:", (3*2.25/32)*exp(1.5)/1.28125)
