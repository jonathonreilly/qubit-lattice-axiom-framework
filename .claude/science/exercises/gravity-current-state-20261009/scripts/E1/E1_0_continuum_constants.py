"""E1 step 0: continuum constants for the Benincasa-Dowker (BD) operators.

Operators (verified against Sorkin gr-qc/0703099 eqs (1),(7),(7a) and
Belenchia-Benincasa-Liberati arXiv:1411.6513 eq (5.22)):

 2D local : B phi(x) = (4/l^2)[-1/2 phi(x) + (S_L1 - 2 S_L2 + S_L3) phi]
 2D smeared: B_eps phi(x) = (4 eps/l^2)[-1/2 phi(x) + eps sum_{y<x} f2(n,eps) phi(y)]
   f2(n,e) = (1-e)^n [1 - 2 e n/(1-e) + e^2 n(n-1)/(2(1-e)^2)]
 4D local : B phi(x) = (4/(sqrt6 l^2))[-phi(x) + (S_L1 - 9 S_L2 + 16 S_L3 - 8 S_L4) phi]
 4D smeared: B_eps phi(x) = (4 sqrt(eps)/(sqrt6 l^2))[-phi(x) + eps sum f4(n,eps) phi(y)]
   f4(n,e) = (1-e)^n [1 - 9 e n/(1-e) + 8 e^2 n(n-1)/(1-e)^2 - (4/3) e^3 n(n-1)(n-2)/(1-e)^3]
 rho = l^-d, rho_k = eps rho = l_k^-d.  Mean kernel: g_d(s) e^{-s} poly, s = rho_k V.

This script computes (units rho_k = 1):
 * mean of eps*sum f over a past diamond of height T (must -> 1/2 in 2D, 1 in 4D)
 * shell integral S(T) = int_{past diamond} g(rho_k V)^2 dV  (variance driver), its
   asymptotic form, and the 'white-noise gain' coefficient c' in A^2 = eps*rho_k*S.
"""
import numpy as np
from scipy import integrate
from math import pi, sqrt, log

g2 = lambda s: np.exp(-s) * (1 - 2*s + s*s/2)
g4 = lambda s: np.exp(-s) * (1 - 9*s + 8*s*s - (4/3)*s**3)

print("== 2D (u,v light-cone coords, dt dx = du dv, V = du*dv) ==")
# past diamond of x with sides U (in u and v): int_0^U int_0^U g(uv) du dv
for U in [2, 4, 8, 16, 32]:
    m, _ = integrate.dblquad(lambda v, u: g2(u*v), 0, U, 0, U, epsabs=1e-11)
    S, _ = integrate.dblquad(lambda v, u: g2(u*v)**2, 0, U, 0, U, epsabs=1e-11)
    print(f"U={U:4d}  mean(eps sum f)={m:.8f} (target 0.5)  S={S:.5f}  "
          f"S/log(U^2)={S/log(U*U):.5f}")
H2, _ = integrate.quad(lambda s: g2(s)**2, 0, np.inf)
print(f"int g2^2 ds = {H2:.6f} (exact 3/16 = 0.1875): S(U) ~ 0.1875*log(U^2) + c")

print("\n== 4D (tau, rapidity eta), V = (pi/24) tau^4 ==")
# past diamond of height T: y = x - tau(cosh eta, sinh eta n); y in diamond iff tau e^eta < T
def diamond_int(fun, T):
    def inner(tau):
        a = log(T/tau)
        hyp = (np.sinh(2*a)/4 - a/2)  # int_0^a sinh^2
        return 4*pi * tau**3 * hyp * fun(pi/24 * tau**4)
    val, err = integrate.quad(inner, 1e-12, T, limit=400, epsabs=1e-12)
    return val
for T in [2, 3, 4, 6, 8, 12, 16, 32]:
    m = diamond_int(g4, T)
    S = diamond_int(lambda s: g4(s)**2, T)
    print(f"T={T:4d}  mean(eps sum f)={m:.8f} (target 1)  S={S:10.4f}  S/T^2={S/T**2:.5f}")
# asymptotic: S ~ (pi/2) T^2 int tau g^2 dtau  (from hyp ~ (T/tau)^2/8)
Ia, _ = integrate.quad(lambda tau: tau * g4(pi/24*tau**4)**2, 0, 20, limit=400)
print(f"asymptotic S/T^2 -> (pi/2)*int tau g4^2 dtau = {pi/2*Ia:.5f}")
# moment condition that kills light-cone (IR) contribution of the mean
from math import gamma
mc = sum(c*gamma(k+0.5) for k, c in enumerate([1, -9, 8, -4/3]))
print(f"moment int g4(s) s^-1/2 ds = {mc:.3e} (0 => light-cone tail cancels in mean)")
print("\nWhite-noise gain A^2 = eps^2 * rho * S = eps * S (rho_k=1):")
cp = pi/2*Ia
print(f"  4D: A^2 ~ c' eps (T/l_k)^2 with c' = {cp:.5f}")
print(f"  2D: A^2 ~ eps*(0.1875*log(rho_k U^2)+c)")
