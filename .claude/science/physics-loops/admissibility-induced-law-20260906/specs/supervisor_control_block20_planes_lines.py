"""Control, block 20 (supervisor): no long-range order for the unsoldered sphere static law on planes and lines — the lattice sums
and the algebra behind the bound.  Exact (Fractions / sympy) throughout.
(1) plane torus (Z/2LZ)^2: wavevectors k = (pi/L) n with n in {-L+1..L}^2; the sup-norm shell |n|_inf = j has 8j points for j <= L-1
    and 4L-1 points for j = L; every point of shell j has |n|^2 <= 2 j^2; hence sum_{n != 0} 1/|n|^2 >= 4 H_{L-1} (checked exactly, L = 2..12);
    the dyadic bound H_{2^m} >= 1 + m/2 (exact, m <= 12);
(2) E(k) = sum 2(1 - cos k_i) <= |k|^2: the identity 2(1 - cos u) = 4 sin^2(u/2) and |sin x| <= |x|; sample points;
(3) 4/(3N) = |k_min|^2/(3 pi^2) at N = 4L^2 (|k_min| = pi/L), so beta E(k) + 4/(3N) <= (beta + 1/(3 pi^2)) |k|^2 for k != 0;
(4) the simplification chain of the zero-field lower bound: (2M^2/3)^2/[sqrt(a) + sqrt(a + 4M^2/(3N))]^2 >= (M^2/3)^2/(a + 4M^2/(3N))
    >= (M^2/3)^2/(a + 4/(3N)) for 0 < M^2 <= 1;
(5) the final algebra: (M^2/3)^2 (N/pi^2) H/(beta + 1/(3 pi^2)) <= N/3  <=>  M^4 <= (3 pi^2 beta + 1)/H;
(6) isotropy: the sphere average of (s^1)^2 is 1/3; Parseval on the 4x4 torus with symbolic site values (roots of unity +-1, +-i);
(7) the line torus (Z/2LZ): N = 2L, 4/(3N) = 2/(3L); for 1 <= |n| <= m = floor(sqrt L): beta (pi n/L)^2 + 2/(3L) <= (beta pi^2 + 2/3)/L;
    2m points; 4 m^2 >= L for L = 1..400 (so m >= sqrt(L)/2); hence M^4 <= (6 beta pi^2 + 4)/sqrt(L);
(8) the bond identity behind the d-independence of the lower bound: |1 - e^{-i theta}|^2 = 2(1 - cos theta); bonds per direction = N on the 4x4 and 8-tori."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import sympy as sp

def H(n):
    return sum((F(1, j) for j in range(1, n + 1)), F(0))

ok1 = True
for L in range(2, 13):
    rng = range(-L + 1, L + 1)
    pts = [(a, b) for a in rng for b in rng if (a, b) != (0, 0)]
    shells = {}
    for a, b in pts:
        shells.setdefault(max(abs(a), abs(b)), []).append(a * a + b * b)
    counts_ok = all(len(shells[j]) == 8 * j for j in range(1, L)) and len(shells[L]) == 4 * L - 1
    norms_ok = all(max(shells[j]) <= 2 * j * j for j in range(1, L + 1))
    s = sum((F(1, q) for j in shells for q in shells[j]), F(0))
    ok1 = ok1 and counts_ok and norms_ok and s >= 4 * H(L - 1)
    if L in (2, 3, 12):
        print(f"(1) L={L}: shell counts ok={counts_ok}, |n|^2 <= 2j^2 ok={norms_ok}, sum 1/|n|^2 = {s} >= 4 H_(L-1) = {4*H(L-1)}: {s >= 4*H(L-1)}")
print("(1) plane: 8j / (4L-1) shell counts, the norm bound and sum >= 4 H_{L-1} for L = 2..12:", ok1)
print("(1) dyadic: H_{2^m} >= 1 + m/2 for m <= 12:", all(H(2 ** m) >= 1 + F(m, 2) for m in range(13)))
u = sp.symbols("u", real=True)
ident = sp.simplify(2 * (1 - sp.cos(u)) - 4 * sp.sin(u / 2) ** 2) == 0
samples = all(sp.simplify(x ** 2 - 2 * (1 - sp.cos(x))) >= 0 for x in [sp.Rational(i, 10) * sp.pi for i in range(-10, 11)])
print("(2) 2(1 - cos u) = 4 sin^2(u/2):", ident, "; u^2 - 2(1 - cos u) >= 0 at 21 sample points:", samples)
L, beta, a, M, N = sp.symbols("L beta a M N", positive=True)
print("(3) 4/(3 N) = (pi/L)^2/(3 pi^2) at N = 4 L^2:", sp.simplify(sp.Rational(4, 3) / (4 * L ** 2) - (sp.pi / L) ** 2 / (3 * sp.pi ** 2)) == 0)
b = sp.sqrt(a + 4 * M ** 2 / (3 * N))
full = (2 * M ** 2 / 3) ** 2 / (sp.sqrt(a) + b) ** 2
simp = (M ** 2 / 3) ** 2 / (a + 4 * M ** 2 / (3 * N))
# full >= simp  <=>  4 b^2 >= (sqrt a + b)^2  <=>  (b - sqrt a)(3 b + sqrt a) >= 0
print("(4) 4 b^2 - (sqrt a + b)^2 = (b - sqrt a)(3b + sqrt a):", sp.simplify(4 * b ** 2 - (sp.sqrt(a) + b) ** 2 - (b - sp.sqrt(a)) * (3 * b + sp.sqrt(a))) == 0,
      "; b >= sqrt a since 4M^2/(3N) >= 0; then (M^2/3)^2/(a + 4M^2/(3N)) >= (M^2/3)^2/(a + 4/(3N)) iff M^2 <= 1")
Hs = sp.symbols("H", positive=True)
lhs_bound = sp.pi ** 2 * (beta + 1 / (3 * sp.pi ** 2)) / (3 * Hs)   # (M^2/3)^2 <= this
print("(5) 9 * pi^2 (beta + 1/(3 pi^2))/(3 H) = (3 pi^2 beta + 1)/H:", sp.simplify(9 * lhs_bound - (3 * sp.pi ** 2 * beta + 1) / Hs) == 0)
th, ph = sp.symbols("theta phi", real=True)
avg = sp.integrate(sp.integrate((sp.sin(th) * sp.cos(ph)) ** 2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
print("(6) sphere average of (s^1)^2 =", avg)
Lt = 4
sites = list(product(range(Lt), repeat=2))
sym = {x: sp.Symbol(f"s_{x[0]}{x[1]}", real=True) for x in sites}
tot = 0
for n in product(range(Lt), repeat=2):
    hat = sum(sp.I ** ((n[0] * x[0] + n[1] * x[1]) % 4) * sym[x] for x in sites) / sp.Integer(4)  # N^{-1/2} = 1/4
    tot += sp.expand(hat * sp.conjugate(hat))
print("(6) Parseval on the 4x4 torus (symbolic site values): sum_k |s^(k)|^2 - sum_x s_x^2 =", sp.simplify(sp.expand(tot) - sum(v ** 2 for v in sym.values())))
ok7 = True
for Lv in range(1, 401):
    m = isqrt(Lv)
    ok7 = ok7 and 4 * m * m >= Lv
print("(7) line: 4 floor(sqrt L)^2 >= L for L = 1..400:", ok7)
n = sp.symbols("n", positive=True)
print("(7) line: 4/(3N) at N = 2L is 2/(3L):", sp.simplify(sp.Rational(4, 3) / (2 * L) - 2 / (3 * L)) == 0,
      "; for n^2 <= L: beta pi^2 n^2/L^2 + 2/(3L) <= (beta pi^2 + 2/3)/L  [n^2/L^2 <= 1/L]")
m_ = sp.symbols("m", positive=True)
# (M^2/3)^2 * m/(beta pi^2 + 2/3) <= 1/3  =>  M^4 <= 3 (beta pi^2 + 2/3)/m ; with m >= sqrt(L)/2: <= 6 (beta pi^2 + 2/3)/sqrt(L) = (6 beta pi^2 + 4)/sqrt(L)
print("(7) 9 * (beta pi^2 + 2/3)/(3 m) = 3 (beta pi^2 + 2/3)/m; at m = sqrt(L)/2 this is (6 beta pi^2 + 4)/sqrt(L):",
      sp.simplify(3 * (beta * sp.pi ** 2 + sp.Rational(2, 3)) / (sp.sqrt(L) / 2) - (6 * beta * sp.pi ** 2 + 4) / sp.sqrt(L)) == 0)
print("(8) |1 - e^{-i theta}|^2 = 2(1 - cos theta):", sp.simplify(sp.expand((1 - sp.exp(-sp.I * th)) * (1 - sp.exp(sp.I * th)), complex=True) - 2 * (1 - sp.cos(th))) == 0)
bonds2 = {tuple(sorted((x, ((x[0] + d[0]) % 4, (x[1] + d[1]) % 4)))) for x in sites for d in ((1, 0), (0, 1))}
bonds1 = {tuple(sorted((x, (x + 1) % 8))) for x in range(8)}
print("(8) bonds: 4x4 torus", len(bonds2), "= 2N; 8-torus", len(bonds1), "= N")
