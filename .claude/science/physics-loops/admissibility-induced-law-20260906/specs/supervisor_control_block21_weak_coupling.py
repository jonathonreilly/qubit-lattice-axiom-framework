"""Controls, block 21 (supervisor): two passes run in sequence. Pass a: the crude route TV <= tanh(osc/4) (threshold artanh(1/6)), the sphere TV sweep,
the Langevin constants. Pass b: the exact antipodal value, the covariance eigenvalues and series ratios, the mean-absolute-deviation sweep, the walk bound on a 7^3 box.
The contract was written on the variance route after pass b. Original docstrings follow."""
# ---- pass a ----
# """Control, block 21 (supervisor): the weak-coupling side of the unsoldered sphere static law on Z^3.
# (1) TV lemma: for densities p ∝ e^f, q ∝ e^g against a common measure with osc(f - g) = R: TV(p, q) <= tanh(R/4).
#     Numeric sweep on finite spaces (random f, g) and the extremal two-point example (equality).
# (2) Sphere one-site law P_h ∝ e^{beta s.h}: partition function Z(h) = 4 pi sinh(beta|h|)/(beta|h|); TV(P_h, P_h') numerically for
#     h, h' differing by a unit-vector change of one neighbour (|h - h'| <= 2): compare with tanh(beta |h-h'|/2) <= tanh(beta); worst case sweep.
# (3) Threshold: 6 tanh(beta) < 1  <=>  beta < artanh(1/6) = (1/2) log(7/5) = 0.16824...; also the exact worst-case TV at that beta.
# (4) Alternative (Wasserstein) constant: W1 contraction K(beta) = sup_h |d/dh E_h[s]| ... the mean m(h) = L(beta|h|) h/|h| with Langevin L(x) = coth x - 1/x;
#     the Lipschitz constant of h -> m(h) is <= beta sup L'(x)/(beta)... compute sup over x of L(x)/x and L'(x): both <= 1/3; so W1(P_h, P_h') <= ? (not a full bound; noted).
# (5) Exponential decay: with row sum alpha = 6 tanh beta < 1, the influence at graph distance n is <= alpha^n; at beta = 1/10: alpha = 0.5987."""
import math, random
import numpy as np
random.seed(21)
def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())
ok1 = True
worst = 0.0
for trial in range(4000):
    n = random.randint(2, 7)
    f = np.random.uniform(-2, 2, n); g = np.random.uniform(-2, 2, n)
    mu = np.random.uniform(0.1, 1, n); mu /= mu.sum()
    p = np.exp(f) * mu; p /= p.sum(); q = np.exp(g) * mu; q /= q.sum()
    R = (f - g).max() - (f - g).min()
    ratio = tv(p, q) / math.tanh(R / 4) if R > 0 else 0
    worst = max(worst, ratio)
    ok1 = ok1 and tv(p, q) <= math.tanh(R / 4) + 1e-12
d = 1.3
p = np.array([math.exp(d / 2), math.exp(-d / 2)]); p /= p.sum(); q = p[::-1]
print(f"(1) TV <= tanh(osc/4) on 4000 random finite instances: {ok1}; worst ratio {worst:.4f}; two-point extremal: TV={tv(p,q):.6f} tanh(2d/4)={math.tanh(d/2):.6f}")
# (2) sphere: quadrature on the sphere (Gauss-Legendre in cos theta, uniform in phi)
nodes, weights = np.polynomial.legendre.leggauss(80)
phis = np.linspace(0, 2 * math.pi, 160, endpoint=False)
ct = np.repeat(nodes, len(phis)); st = np.sqrt(1 - ct ** 2); ph = np.tile(phis, len(nodes))
S = np.stack([st * np.cos(ph), st * np.sin(ph), ct], axis=1)
W = np.repeat(weights, len(phis)) * (2 * math.pi / len(phis))   # integrates to 4 pi
def dens(beta, h):
    e = np.exp(beta * (S @ h)); return e * W / (e * W).sum()
def Z_exact(beta, h):
    x = beta * np.linalg.norm(h)
    return 4 * math.pi * (math.sinh(x) / x if x > 0 else 1.0)
beta = 0.5; h = np.array([0.3, -1.2, 2.0])
print(f"(2) Z(h) quadrature {float((np.exp(beta*(S@h))*W).sum()):.6f} vs exact 4 pi sinh(beta|h|)/(beta|h|) = {Z_exact(beta,h):.6f}")
def worst_tv(beta, trials=300):
    w = 0.0; arg = None
    for _ in range(trials):
        # h = sum of up to 5 unit vectors (the other neighbours), change one neighbour u -> u'
        k = random.randint(0, 5)
        base = sum((np.random.normal(size=3) / np.linalg.norm(v) for v in [np.random.normal(size=3) for _ in range(k)]), np.zeros(3)) if k else np.zeros(3)
        u = np.random.normal(size=3); u /= np.linalg.norm(u)
        up = np.random.normal(size=3); up /= np.linalg.norm(up)
        for cand in (up, -u):
            t = tv(dens(beta, base + u), dens(beta, base + cand))
            bound = math.tanh(beta * np.linalg.norm(u - cand) / 2)
            if t / bound > w:
                w = t / bound; arg = (k, float(np.linalg.norm(base)), float(np.linalg.norm(u - cand)), t, bound)
    return w, arg
for beta in (0.1, 0.16824, 0.5, 1.0):
    w, arg = worst_tv(beta)
    print(f"(2) beta={beta}: worst TV/tanh(beta|dh|/2) ratio {w:.4f} at (k, |base|, |dh|, TV, bound) = {tuple(round(x,4) if isinstance(x,float) else x for x in arg)}; tanh(beta) = {math.tanh(beta):.4f}")
b0 = math.atanh(1 / 6)
print(f"(3) artanh(1/6) = {b0:.6f}; (1/2) log(7/5) = {0.5*math.log(7/5):.6f}; 6 tanh(b0) = {6*math.tanh(b0):.6f}")
# antipodal worst case at beta0 with base = 0: TV(P_u, P_-u)
t_anti = tv(dens(b0, np.array([0, 0, 1.0])), dens(b0, np.array([0, 0, -1.0])))
print(f"(3) at beta0, TV(P_e, P_-e) (base 0, antipodal change) = {t_anti:.6f} vs tanh(beta0) = {math.tanh(b0):.6f}; 6*TV = {6*t_anti:.4f}")
L = lambda x: 1 / math.tanh(x) - 1 / x if x > 1e-9 else x / 3
xs = np.linspace(1e-6, 20, 200001)
print(f"(4) sup_x L(x)/x = {max(L(x)/x for x in xs):.6f} (= 1/3 at 0); sup_x L'(x) = {max((L(x+1e-6)-L(x-1e-6))/2e-6 for x in xs[1:]):.6f} (= 1/3 at 0)")
print(f"(5) alpha = 6 tanh(beta) at beta = 1/10: {6*math.tanh(0.1):.4f}; at beta = 1/8: {6*math.tanh(0.125):.4f}")


# ---- pass b ----
# """Control b (block 21): (a) exact TV of the antipodal pair at zero field = tanh(beta/2); (b) covariance eigenvalues of s under P_h:
# longitudinal L'(x) = 1/x^2 - 1/sinh^2 x, transverse L(x)/x, both <= 1/3 (series with nonnegative coefficients: ratios 6/(n(2n-1)), 3/(2n+1));
# (c) MAD sweep: sup over (x, angle) of E_h|s.D - E_h[s.D]| for unit D (is it 1/2 at x = 0?); (d) the matrix bound sum_n (C^n)_{0x} <= alpha^{|x|_1}/(1-alpha)
# on a 7^3 box with uniform edge weights alpha/6 (exact Fractions), and the 3D geometric sum ((1+a)/(1-a))^3."""
import math
from fractions import Fraction as F
from itertools import product
import numpy as np
import sympy as sp
x, t, b = sp.symbols("x t beta", positive=True)
# (a)
Z = 4 * sp.pi * sp.sinh(b) / b
tv = (2 * sp.pi / Z) * sp.integrate(sp.exp(b * t) - sp.exp(-b * t), (t, 0, 1))
print("(a) TV(P_e, P_-e) =", sp.simplify(tv), "; equals tanh(beta/2):", sp.simplify(tv - sp.tanh(b / 2)) == 0)
# (b)
Lg = sp.coth(x) - 1 / x
E_par2 = sp.integrate(sp.exp(x * t) * t ** 2, (t, -1, 1)) / sp.integrate(sp.exp(x * t), (t, -1, 1))
print("(b) E_h[(s.h^)^2] = 1 - 2L/x:", sp.simplify(E_par2 - (1 - 2 * Lg / x)) == 0, "; Var = L'(x):", sp.simplify(E_par2 - Lg ** 2 - sp.diff(Lg, x)) == 0,
      "; L'(x) = 1/x^2 - 1/sinh^2 x:", sp.simplify(sp.diff(Lg, x) - (1 / x ** 2 - 1 / sp.sinh(x) ** 2)) == 0)
# series: 3 sinh^2 x - 3x^2 vs x^2 sinh^2 x  (L' <= 1/3  <=>  3 sinh^2 - 3 x^2 <= x^2 sinh^2)
s1 = sp.series(3 * sp.sinh(x) ** 2 - 3 * x ** 2, x, 0, 16).removeO()
s2 = sp.series(x ** 2 * sp.sinh(x) ** 2, x, 0, 16).removeO()
print("(b) coefficients of x^{2n}, n=2..7: left", [s1.coeff(x, 2 * n) for n in range(2, 8)], " right", [s2.coeff(x, 2 * n) for n in range(2, 8)],
      "; ratios", [sp.nsimplify(s1.coeff(x, 2 * n) / s2.coeff(x, 2 * n)) for n in range(2, 8)], "= 6/(n(2n-1)):", all(sp.simplify(s1.coeff(x, 2*n)/s2.coeff(x, 2*n) - sp.Rational(6, n*(2*n-1))) == 0 for n in range(2, 8)))
s3 = sp.series(x * sp.cosh(x) - sp.sinh(x), x, 0, 16).removeO()
s4 = sp.series(x ** 2 * sp.sinh(x) / 3, x, 0, 16).removeO()
print("(b) L/x <= 1/3 <=> x cosh x - sinh x <= (x^2/3) sinh x; coefficient ratios x^{2n+1}, n=1..6:", [sp.nsimplify(s3.coeff(x, 2*n+1)/s4.coeff(x, 2*n+1)) for n in range(1, 7)], "= 3/(2n+1):", all(sp.simplify(s3.coeff(x, 2*n+1)/s4.coeff(x, 2*n+1) - sp.Rational(3, 2*n+1)) == 0 for n in range(1, 7)))
# (c) MAD sweep numerically
nodes, weights = np.polynomial.legendre.leggauss(120)
phis = np.linspace(0, 2 * math.pi, 240, endpoint=False)
ct = np.repeat(nodes, len(phis)); st = np.sqrt(1 - ct ** 2); ph = np.tile(phis, len(nodes))
S = np.stack([st * np.cos(ph), st * np.sin(ph), ct], axis=1)
W = np.repeat(weights, len(phis)) * (2 * math.pi / len(phis))
best = (0, None)
for xv in np.linspace(0, 12, 121):
    for ang in np.linspace(0, math.pi / 2, 31):
        h = xv * np.array([0, 0, 1.0]); D = np.array([math.sin(ang), 0, math.cos(ang)])
        w = np.exp(S @ h) * W; w /= w.sum()
        X = S @ D; m = (w * X).sum(); mad = (w * np.abs(X - m)).sum()
        if mad > best[0]:
            best = (mad, (round(float(xv), 3), round(float(ang), 3)))
print(f"(c) sup over x in [0,12], angle in [0, pi/2] of MAD_h(s.D) = {best[0]:.6f} at (x, angle) = {best[1]} (1/2 at x = 0?)")
# (d) matrix bound on a 7^3 box
n = 7
sites = list(product(range(n), repeat=3))
idx = {s: i for i, s in enumerate(sites)}
alpha = F(9, 10)
c = alpha / 6
ok = True
o = idx[(3, 3, 3)]
# vector iteration: v_n = C^n e_o (C symmetric); accumulate sums
v = [F(0)] * len(sites); v[o] = F(1)
acc = [F(0)] * len(sites)
for step in range(1, 25):
    nv = [F(0)] * len(sites)
    for s in sites:
        i = idx[s]
        if v[i] == 0: continue
        for d in range(3):
            for e in (1, -1):
                y = list(s); y[d] += e
                if 0 <= y[d] < n:
                    nv[idx[tuple(y)]] += c * v[i]
    v = nv
    for i in range(len(sites)):
        acc[i] += v[i]
for s in sites:
    dist = sum(abs(s[d] - 3) for d in range(3))
    if dist >= 1:
        ok = ok and acc[idx[s]] <= alpha ** dist / (1 - alpha)
print("(d) sum_{n<=24} (C^n)_{0x} <= alpha^{|x|_1}/(1-alpha) on the 7^3 box at alpha = 9/10, all x != 0:", ok, "; e.g. |x|_1 = 3:", float(acc[idx[(4,4,4)]]), "<=", float(alpha**3/(1-alpha)))
a = sp.symbols("a", positive=True)
print("(d) sum_{n in Z} a^{|n|} = (1+a)/(1-a):", sp.simplify(sp.summation(a ** sp.Abs(sp.symbols('m', integer=True)), (sp.symbols('m', integer=True), -sp.oo, sp.oo)) - (1 + a) / (1 - a)) == 0 if False else "checked by hand: 1 + 2a/(1-a) = (1+a)/(1-a)", sp.simplify(1 + 2 * a / (1 - a) - (1 + a) / (1 - a)) == 0)
