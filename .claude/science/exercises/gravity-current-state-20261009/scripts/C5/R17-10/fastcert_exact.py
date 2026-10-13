"""R17-10 Theorem F constants, exact/interval:
 (i) rational coefficients of P(x,s) for A = 67/500, B = -1/25 (exact Fractions);
 (ii) region 1 (s <= s* = 9/50): P <= c0 + s* k1 < 0 (exact);  region 2 (x >= x* = k1/k2): P <= q(x) <= c0 < 0 (exact, c1, c2 < 0);
 (iii) x_box(z) = (1 - R(z))/2, R(z) = 2 z e^{-z^2}/(sqrt(pi) erf z); for z >= z0 >= 1/sqrt2, R(z) <= R(z0) (2ze^{-z^2} decreasing, erf increasing):
      outward-rounded interval value of R(z0) and the check (1 - R(z0))/2 >= x*  (mpmath.iv).
 (iv) the resulting sufficient conditions: s_min >= m sqrt(x*/s*), b >= z0 m / sqrt(s*)."""
from fractions import Fraction as Fr
from mpmath import iv, mp
A, B = Fr(67, 500), Fr(-1, 25)
c2 = Fr(-635, 1280) + 3*A - 2*B; c1 = Fr(9875, 12800) - Fr(11, 2)*A + B; c0 = Fr(-2625, 12800) + Fr(3, 2)*A
k1 = Fr(20, 128) - A; k2 = Fr(255, 1280) - A; ss = Fr(9, 50); xs = k1/k2
print('c2 =', c2, float(c2), ' c1 =', c1, float(c1), ' c0 =', c0, float(c0))
print('k1 =', k1, float(k1), ' k2 =', k2, float(k2), ' x* = k1/k2 =', xs, float(xs))
print('region 1 bound c0 + s* k1 =', c0 + ss*k1, float(c0 + ss*k1), '< 0:', c0 + ss*k1 < 0, '| region 2: c0, c1, c2 < 0:', c0 < 0 and c1 < 0 and c2 < 0)
print('multipliers: alpha = 32A/5 =', 32*A/5, float(32*A/5), ' beta = 16B/5 =', 16*B/5, float(16*B/5))
iv.dps = 30
for z0s in ['1.25', '1.26', '1.27', '1.30']:
    z0 = iv.mpf(z0s); N = 4000
    # rigorous lower bound of int_0^z0 e^{-v^2} dv: right-endpoint Riemann sum of a decreasing function (interval arithmetic)
    Ilo = sum(iv.exp(-(z0*i/N)**2) for i in range(1, N+1))*(z0/N)
    R = 2*z0*iv.exp(-z0*z0)/(2*Ilo)          # = 2 z e^{-z^2}/(sqrt(pi) erf z) with sqrt(pi) erf z = 2 int_0^z e^{-v^2}; upper bound
    xb = (1 - R)/2
    ok = xb.a >= iv.mpf(xs.numerator)/xs.denominator
    print('z0 = %s: R(z0) <= [%s, %s] (upper enclosure); x_box lower %s; >= x*: %s' % (z0s, mp.nstr(R.a, 12), mp.nstr(R.b, 12), mp.nstr(xb.a, 12), ok))
z0 = iv.mpf('1.27'); sq = iv.sqrt(iv.mpf(ss.numerator)/ss.denominator)
print('sufficient: s_min/m >= sqrt(x*/s*) = %s ; b/m >= z0/sqrt(s*) = %s (z0 = 1.27)' % (mp.nstr(iv.sqrt((iv.mpf(xs.numerator)/xs.denominator)/(iv.mpf(ss.numerator)/ss.denominator)).b, 8), mp.nstr((z0/sq).b, 8)))
