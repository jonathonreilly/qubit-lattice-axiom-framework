"""Lane RG probe G2, part 4: Chebyshev stopband filter f_r(k) = T_r(2cos k + 1)/T_r(3)
(degree r; minimal sup on the stopband [pi/2, pi] given f(0)=1, by the Chebyshev extremal property).
Predicted 2<->2 umklapp sup: T_r(3)^-2, i.e. rate 2 arccosh(3) = 3.5255 per degree,
versus the binomial ((1+cos k)/2)^r: 16^-r, rate 4 ln 2 = 2.7726.  Also compares passband widths."""
import numpy as np
from numpy.polynomial import chebyshev as C
from g2_filters import eps_sup, f_binom

def f_cheb(r):
    cr = np.zeros(r + 1); cr[-1] = 1
    T3 = C.chebval(3.0, cr)
    return lambda k: C.chebval(2 * np.cos(k) + 1, cr) / T3, T3

print(" r   eps_sup(cheb)   T_r(3)^-2      ratio   -ln(eps)/r | eps_sup(binom)=16^-r | k_1/2 cheb  k_1/2 binom (f=1/2 point)")
for r in [1, 2, 4, 8, 12, 16, 24, 32]:
    f, T3 = f_cheb(r)
    e = eps_sup(f, ngrid=2001)
    kk = np.linspace(0, np.pi / 2, 200001)
    kc = kk[np.argmin(np.abs(f(kk) - 0.5))]; kb = kk[np.argmin(np.abs(f_binom(r)(kk) - 0.5))]
    print(f"{r:3d}  {e:.4e}  {T3**-2.0:.4e}  {e*T3**2:.4f}   {-np.log(e)/r:.4f}  | {16.0**-r:.4e} | {kc:.4f}  {kb:.4f}")
print("2 arccosh 3 =", 2 * np.arccosh(3.0), " 4 ln 2 =", 4 * np.log(2))
