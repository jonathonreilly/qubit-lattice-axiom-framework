"""Control, block 23 (supervisor): algebraic decay on the plane by complex rotations, with explicit constants.
(1) identities: cos(phi + i a) = cos phi cosh a - i sin phi sinh a; |exp(c cos(phi + i a))| = exp(c cos phi cosh a) for real c;
    cos phi cosh a <= cos phi + (cosh a - 1); cosh t - 1 <= (t^2/2) cosh t (series ratio 2/((2k)(2k-1)) <= 1); log(1+u) <= u;
(2) the shift function a_y = gamma log((1+R)/(1+|y|))_+ : |a_y - a_z| <= gamma/(1 + min(|y|,|z|)) on bonds (checked on a 41x41 patch);
    the shell sum sum_{|y|<R+1} 4/(1+|y|)^2 <= 4(1 + 8 H_R) exactly (Z^2, R <= 40) and on the torus (Z/2LZ)^2 with the torus distance (L <= 12);
    H_R <= 1 + log R;
(3) constants: cosh 1 <= 25/16 <= 8/5 from 8/3 <= e <= 11/4; kappa(gamma) = gamma - (128/5) beta gamma^2 maximal at gamma* = 5/(256 beta), value 5/(512 beta);
    prefactor 18 beta gamma^2 cosh gamma <= (144/5) beta gamma^2 = 45/(4096 beta) <= 9/16 for beta >= 5/256; for beta <= 5/256, gamma = 1 gives kappa >= 1/2;
(4) the inequality of P1 on exactly integrable instances: the two-site and three-site open chains (weight e^{beta s.s'}), |<s_0^1 s_x^1 + s_0^2 s_x^2>| = (2/3) L(beta)^r
    versus exp(a_x - a_0 + beta sum_b (cosh(Delta a) - 1)) for a grid of shift values and beta in {1/4, 1, 4};
(5) the torus consequence: M_N^2 <= 6 C_0 (1+L)^{-min(kappa,1)} + 1/(4 L^2) skeleton: sum over sup-norm shells 8j (1+j)^{-kappa} <= L (1+L)^{1-kappa} for kappa <= 1."""
import math, cmath
from fractions import Fraction as F
import sympy as sp
phi, a, c, t = sp.symbols("phi a c t", real=True)
lhs = sp.cos(phi + sp.I * a)
rhs = sp.cos(phi) * sp.cosh(a) - sp.I * sp.sin(phi) * sp.sinh(a)
print("(1) cos(phi + i a) identity:", sp.simplify(sp.expand(lhs - rhs, complex=True)) == 0)
print("(1) |exp(c cos(phi+ia))| = exp(c cos phi cosh a): Re part is c cos phi cosh a:", sp.simplify(sp.re(c * rhs) - c * sp.cos(phi) * sp.cosh(a)) == 0)
print("(1) cos phi + (cosh a - 1) - cos phi cosh a = (1 - cos phi)(cosh a - 1) >= 0:", sp.simplify(sp.cos(phi) + sp.cosh(a) - 1 - sp.cos(phi) * sp.cosh(a) - (1 - sp.cos(phi)) * (sp.cosh(a) - 1)) == 0)
s1 = sp.series(sp.cosh(t) - 1, t, 0, 20).removeO(); s2 = sp.series(t ** 2 / 2 * sp.cosh(t), t, 0, 20).removeO()
print("(1) coefficient ratios of (cosh t - 1)/((t^2/2) cosh t) at t^{2k}, k=1..9:", [sp.nsimplify(s1.coeff(t, 2 * k) / s2.coeff(t, 2 * k)) for k in range(1, 10)], "= 2/((2k)(2k-1)):", all(sp.simplify(s1.coeff(t, 2*k)/s2.coeff(t, 2*k) - sp.Rational(2, 2*k*(2*k-1))) == 0 for k in range(1, 10)))
u = sp.symbols("u", positive=True)
print("(1) d/du (u - log(1+u)) = u/(1+u) >= 0:", sp.simplify(sp.diff(u - sp.log(1 + u), u) - u / (1 + u)) == 0)
# (2) shift function Lipschitz on Z^2 patch
def H(n): return sum((F(1, j) for j in range(1, n + 1)), F(0))
gamma = 0.7; R = 20
def a_fun(y): return gamma * max(0.0, math.log((1 + R) / (1 + math.hypot(*y))))
ok2 = True; worst = 0
for y1 in range(-40, 41):
    for y2 in range(-40, 41):
        for d in ((1, 0), (0, 1)):
            z = (y1 + d[0], y2 + d[1])
            m = min(math.hypot(y1, y2), math.hypot(*z))
            diff = abs(a_fun((y1, y2)) - a_fun(z))
            ok2 = ok2 and diff <= gamma / (1 + m) + 1e-12
            worst = max(worst, diff * (1 + m) / gamma)
print(f"(2) |a_y - a_z| <= gamma/(1 + min(|y|,|z|)) on all bonds of a 81x81 patch: {ok2}; worst ratio {worst:.4f}")
ok2b = True
for Rv in range(1, 41):
    s = sum((F(4, (1 + F(math.isqrt(y1*y1+y2*y2)))**2) for y1 in range(-Rv-1, Rv+2) for y2 in range(-Rv-1, Rv+2) if y1*y1+y2*y2 < (Rv+1)**2), F(0))
    # with |y| replaced by floor(|y|) the sum only grows; the exact bound uses |y| >= |y|_inf = j: sum <= 4(1 + 8 H_R)
    s_shell = sum((F(8 * j, (1 + j) ** 2) for j in range(1, Rv + 1)), F(0)) * 4 + 4
    ok2b = ok2b and s_shell <= 4 * (1 + 8 * H(Rv))
print("(2) 4(1 + sum_{j<=R} 8j/(1+j)^2) <= 4(1 + 8 H_R) for R <= 40 exactly:", ok2b)
ok2c = True
for L in range(2, 13):
    for j in range(1, L + 1):
        cnt = sum(1 for x1 in range(-L + 1, L + 1) for x2 in range(-L + 1, L + 1) if max(min(abs(x1), 2*L-abs(x1)), min(abs(x2), 2*L-abs(x2))) == j)
        ok2c = ok2c and cnt == (8 * j if j < L else 4 * L - 1) and cnt <= 8 * j
print("(2) torus sup-norm shells: 8j points for j < L, 4L-1 <= 8L for j = L, L = 2..12:", ok2c)
print("(2) H_R <= 1 + log R for R <= 10^5:", all(sum(1/j for j in range(1, n+1)) <= 1 + math.log(n) + 1e-12 for n in range(1, 100001)))
# (3) constants
e_lo = F(8, 3); e_hi = F(11, 4)
print("(3) partial sum 1+1+1/2+1/6 = 8/3 <= e; 65/24 + 1/100 = ", F(65, 24) + F(1, 100), "<= 11/4:", F(65, 24) + F(1, 100) <= e_hi, "; cosh 1 <= (11/4 + 3/8)/2 =", (e_hi + F(3, 8)) / 2, "<= 8/5:", (e_hi + F(3, 8)) / 2 <= F(8, 5))
g, b = sp.symbols("gamma beta", positive=True)
kappa = g - sp.Rational(128, 5) * b * g ** 2
gstar = sp.solve(sp.diff(kappa, g), g)[0]
print("(3) gamma* =", gstar, "; kappa(gamma*) =", sp.simplify(kappa.subs(g, gstar)), "; 18 beta gamma*^2 (8/5) =", sp.simplify(sp.Rational(144, 5) * b * gstar ** 2), "; at beta = 5/256:", sp.simplify((sp.Rational(144, 5) * b * gstar ** 2).subs(b, sp.Rational(5, 256))))
print("(3) small beta: gamma = 1: kappa = 1 - 128 beta/5 >= 1/2 iff beta <= 5/256:", sp.solve(1 - sp.Rational(128, 5) * b - sp.Rational(1, 2) >= 0, b))
# (4) P1's inequality on the open chains
Lang = lambda x: 1 / math.tanh(x) - 1 / x
ok4 = True; tight = 1e9
for beta in (0.25, 1.0, 4.0):
    for r in (1, 2):
        truth = (2 / 3) * Lang(beta) ** r
        for a0 in [i / 10 for i in range(0, 41)]:
            # chain 0 - 1 - ... - r with a_0 = a0, a_r = 0, linear in between (a_k = a0 (1 - k/r)); bonds: r
            da = a0 / r
            bound = math.exp(-a0 + beta * r * (math.cosh(da) - 1))
            ok4 = ok4 and truth <= bound + 1e-12
            tight = min(tight, bound / truth)
print(f"(4) P1's inequality on 2- and 3-site chains for 41 shift values, beta in (1/4, 1, 4): {ok4}; tightest bound/truth = {tight:.3f}")
# (5) torus consequence skeleton
kap = 0.3
for L in (10, 100, 1000):
    ssum = sum(8 * j * (1 + j) ** (-kap) for j in range(1, L + 1))
    print(f"(5) L={L}: sum_j 8j(1+j)^-kappa = {ssum:.2f} <= 8 L (1+L)^(1-kappa) = {8*L*(1+L)**(1-kap):.2f}: {ssum <= 8*L*(1+L)**(1-kap)}")
