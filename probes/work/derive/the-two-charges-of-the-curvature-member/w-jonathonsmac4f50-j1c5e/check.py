#!/usr/bin/env python3
"""check.py for J:derive:the-two-charges-of-the-curvature-member:a2 (worker w-jonathonsmac4f50-j1c5e, claude-opus-5-5).

Exact arithmetic (sympy, Fraction) for every finite claim of ATTEMPT.md.  One section (C4) is floating-point evidence and is labelled so.
Sections:
  A  the turn at every order by the orbit integral expanded directly, and its closed form by Lagrange inversion;
  B  capture by the discriminant of the turning-point cubic;
  C  the radius of the turn series in 1/b;
  D  exact box examples for T2(a)-(e) and the wall hypothesis.
"""
import sys, time, math
from fractions import Fraction as Fr
from itertools import product
import sympy as sp

PASS, FAIL = [], []
def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail else "") + "  [%.0f s]" % (time.time() - t_start), flush=True)

t_start = time.time()
u, w, v, t = sp.symbols("u w v t")
a, p, M, rho = sp.symbols("a p M rho", positive=True)
e = sp.Symbol("epsilon", positive=True)          # 1/b

def m(k):
    """m_k = 2 int_0^1 y^k dy / sqrt(1 - y^2) = sqrt(pi) Gamma((k+1)/2) / Gamma(k/2 + 1)"""
    return sp.simplify(sp.sqrt(sp.pi) * sp.gamma(sp.Rational(k + 1, 2)) / sp.gamma(sp.Rational(k, 2) + 1))

# ================================================================ A: the orbit integral expanded directly
# chi + pi = 2 int_0^{u0} du / sqrt(n(u)^2/b^2 - u^2) (u = 1/r; u0 the first root).  Scale u = eps x, x = x0 v, x0 the exact turning point:
# N2(eps x0 v) - x0^2 v^2 = (1 - v) x0^2 [(1 + v) - T(v)],  T(v) = sum_{k>=1} c_k eps^k x0^(k-2) (1 + v + ... + v^(k-1)),  N2 = n^2 = sum c_k u^k,
# so chi + pi = 2 int_0^1 dv / sqrt(1 - v^2) (1 - T/(1+v))^(-1/2), expanded in eps; the integrals int_0^1 v^m (1+v)^(-j) dv / sqrt(1-v^2)
# become, with t = tan(theta/2), v = cos theta, int_0^1 2^(1-j) (1 - t^2)^m (1 + t^2)^(j-m-1) dt: rational functions of t, exact.
KA = 5
nus = sp.symbols("nu1:%d" % (KA + 1))
n_gen = 1 + sum(nus[k] * u ** (k + 1) for k in range(KA))
N2 = sp.expand(sp.series(n_gen ** 2, u, 0, KA + 1).removeO())
c = [sp.expand(N2.coeff(u, k)) for k in range(KA + 1)]
x0 = sp.Integer(1)
for _ in range(KA + 1):
    x0 = sp.expand(sp.series(sp.sqrt(sum(c[k] * (e * x0) ** k for k in range(KA + 1))), e, 0, KA + 1).removeO())
T = sp.expand(sp.series(sum(c[k] * e ** k * x0 ** (k - 2) * sum(v ** i for i in range(k)) for k in range(1, KA + 1)), e, 0, KA + 1).removeO())
cache = {}
def Ivj(mm, j):
    if (mm, j) not in cache:
        cache[(mm, j)] = sp.integrate(sp.Integer(2) ** (1 - j) * (1 - t ** 2) ** mm * (1 + t ** 2) ** (j - mm - 1), (t, 0, 1))
    return cache[(mm, j)]
tot, Tj = sp.Integer(0), sp.Integer(1)
for j in range(KA + 1):
    if j: Tj = sp.expand(sp.series(Tj * T, e, 0, KA + 1).removeO())
    for (mm,), cm in sp.Poly(Tj, v).terms():
        tot += sp.binomial(2 * j, j) / sp.Integer(4) ** j * cm * Ivj(mm, j)
chi_direct = sp.expand(sp.series(sp.expand(2 * tot - sp.pi), e, 0, KA + 1).removeO())
ok = chi_direct.coeff(e, 0) == 0
lag = {}
for k in range(1, KA + 1):
    lag[k] = sp.expand(m(k) * sp.series(n_gen ** k, u, 0, k + 1).removeO().coeff(u, k))
    ok = ok and sp.simplify(chi_direct.coeff(e, k) - lag[k]) == 0
check("A1 direct expansion of the orbit integral to order (1/b)^5 for n = 1 + nu1/r + ... + nu5/r^5: the (1/b)^k coefficient is m_k [u^k] n(u)^k, k = 1..5", ok,
      "k=4: %s" % sp.factor(chi_direct.coeff(e, 4)))
note_T4 = [2 * nus[0], sp.pi * (nus[1] + nus[0] ** 2 / 2), sp.Rational(4, 3) * (nus[0] ** 3 + 6 * nus[0] * nus[1] + 3 * nus[2])]
check("A2 orders 1-3 agree with block 110 T4's 2nu1, pi(nu2 + nu1^2/2), (4/3)(nu1^3 + 6nu1nu2 + 3nu3)",
      all(sp.simplify(chi_direct.coeff(e, k + 1) - note_T4[k]) == 0 for k in range(3)))
check("A3 m_k = 2, pi/2, 4/3, 3pi/8, 16/15, 5pi/16 for k = 1..6 (m_k = sqrt(pi) Gamma((k+1)/2)/Gamma(k/2+1))",
      [m(k) for k in range(1, 7)] == [2, sp.pi / 2, sp.Rational(4, 3), 3 * sp.pi / 8, sp.Rational(16, 15), 5 * sp.pi / 16])
# Lagrange-Buermann at the scope used: with u(w) the root of u = w n(u), u(0) = 0, [w^k] log n(u(w)) = (1/k) [u^k] n(u)^k
# exact power series (lists of Fractions, truncated at order KL)
KL = 12
def mul(A, B):
    C = [Fr(0)] * (KL + 1)
    for i, x_ in enumerate(A):
        if x_:
            for j in range(KL + 1 - i):
                C[i + j] += x_ * B[j]
    return C
def compose(nc, U):                       # n(U) for n = sum nc[k] u^k, U = O(w)
    out, P = [Fr(0)] * (KL + 1), [Fr(1)] + [Fr(0)] * KL
    for k in range(KL + 1):
        out = [o + nc[k] * q for o, q in zip(out, P)]
        P = mul(P, U)
    return out
def logser(X):                            # log(1 + X), X = O(w)
    out, P = [Fr(0)] * (KL + 1), [Fr(1)] + [Fr(0)] * KL
    for j in range(1, KL + 1):
        P = mul(P, X); out = [o + Fr((-1) ** (j + 1), j) * q for o, q in zip(out, P)]
    return out
def powcoef(nc, k):                       # [u^k] n^k
    P = [Fr(1)] + [Fr(0)] * KL
    for _ in range(k): P = mul(P, nc)
    return P[k]
import random
random.seed(1)
indices = [[Fr(1)] + [Fr(random.randint(-9, 9), random.randint(1, 9)) for _ in range(KL)] for _ in range(5)]
Am, Pm = Fr(2, 7), Fr(3, 5)               # the member at a = 2/7, p = 3/5: coefficients of (1 + a u)^3 / (1 - p u)
memc = [sum(Fr(math.comb(3, i)) * Am ** i * Pm ** (k - i) for i in range(0, min(3, k) + 1)) for k in range(KL + 1)]
indices.append(memc)
ok = True
for nc in indices:
    U = [Fr(0), Fr(1)] + [Fr(0)] * (KL - 1)            # u = w n(u): iterate
    for _ in range(KL + 1):
        U = [Fr(0)] + compose(nc, U)[:KL]
    g = logser([x_ - (1 if i == 0 else 0) for i, x_ in enumerate(compose(nc, U))])
    ok = ok and all(g[k] == powcoef(nc, k) / k for k in range(1, KL + 1))
check("A4 Lagrange-Buermann at the scope used, exactly to order 12 on five random rational indices and the member (a, p) = (2/7, 3/5): [w^k] log n(u(w)) = (1/k)[u^k] n(u)^k for u = w n(u)", ok)
# the member: n = (1 + a u)^3 / (1 - p u);  [u^k] n^k = sum_j C(3k, k-j) C(k+j-1, j) a^(k-j) p^j
def member_coef(k, aa=a, pp=p):
    return sum(sp.binomial(3 * k, k - j) * sp.binomial(k + j - 1, j) * aa ** (k - j) * pp ** j for j in range(k + 1))
n_mem = (1 + a * u) ** 3 / (1 - p * u)
ok = all(sp.expand(member_coef(k) - sp.series(n_mem ** k, u, 0, k + 1).removeO().coeff(u, k)) == 0 for k in range(1, 9))
check("A5 member: [u^k] ((1+au)^3/(1-pu))^k = sum_j C(3k,k-j) C(k+j-1,j) a^(k-j) p^j, k = 1..8", ok)
note_mem = [2 * (3 * a + p), sp.Rational(3, 2) * sp.pi * (5 * a ** 2 + 4 * a * p + p ** 2),
            sp.Rational(8, 3) * (42 * a ** 3 + 54 * a ** 2 * p + 27 * a * p ** 2 + 5 * p ** 3),
            sp.Rational(15, 8) * sp.pi * (99 * a ** 4 + 176 * a ** 3 * p + 132 * a ** 2 * p ** 2 + 48 * a * p ** 3 + 7 * p ** 4)]
check("A6 the member's turn coefficients m_k [u^k] n^k equal block 110 T4's four listed coefficients",
      all(sp.expand(m(k + 1) * member_coef(k + 1) - note_mem[k]) == 0 for k in range(4)))
comp = [sp.nsimplify(m(k) * member_coef(k, M / 2, M / 2) / M ** k) for k in range(1, 7)]
check("A7 at a = p = M/2 the series is 4, 15pi/4, 128/3, 3465pi/64, 3584/5, 255255pi/256 (M/b)^k, k = 1..6",
      comp == [4, 15 * sp.pi / 4, sp.Rational(128, 3), 3465 * sp.pi / 64, sp.Rational(3584, 5), 255255 * sp.pi / 256], str(comp))
kap = sp.Symbol("kappa", positive=True)
ok = all(sp.simplify(m(k) * sp.series(sp.exp(kap * u) ** k, u, 0, k + 1).removeO().coeff(u, k)
                     - sp.sqrt(sp.pi) * k ** k * sp.gamma(sp.Rational(k + 1, 2)) / (sp.factorial(k) * sp.gamma(sp.Rational(k, 2) + 1)) * kap ** k) == 0 for k in range(1, 9))
check("A8 for n = e^(kappa u) the formula gives block 110 T5's c_n = sqrt(pi) n^n Gamma((n+1)/2)/(n! Gamma(n/2+1)) kappa^n, n = 1..8", ok)
aa = 2 * M / (3 + rho)
sec = sp.simplify(m(2) * member_coef(2, aa, rho * aa) / M ** 2)
check("A9 at a fixed first-order turn (3a + p = 2M, p = rho a) the second-order term is 6pi(5 + 4rho + rho^2)/(3 + rho)^2 (M/b)^2",
      sp.simplify(sec - 6 * sp.pi * (5 + 4 * rho + rho ** 2) / (3 + rho) ** 2) == 0)
third = sp.factor(sp.simplify(m(3) * member_coef(3, aa, rho * aa) / M ** 3))
check("A10 (new) at a fixed first-order turn the third-order term is (64/3)(42 + 54rho + 27rho^2 + 5rho^3)/(3 + rho)^3 (M/b)^3: 896/27 at rho = 0, 128/3 at rho = 1",
      sp.simplify(third - sp.Rational(64, 3) * (42 + 54 * rho + 27 * rho ** 2 + 5 * rho ** 3) / (3 + rho) ** 3) == 0
      and third.subs(rho, 1) == sp.Rational(128, 3) and third.subs(rho, 0) == sp.Rational(896, 27), str(third))

# ================================================================ B: capture by the discriminant
b = sp.Symbol("b", positive=True)
cub = sp.expand((1 + a * u) ** 3 - b * u * (1 - p * u))    # turning points: n(u)/b = u, i.e. (1+au)^3 = b u (1 - pu), 0 < u < 1/p
D = sp.factor(sp.discriminant(cub, u))
print("   B: Disc_u[(1+au)^3 - b u (1 - p u)] =", D)
s = sp.Symbol("s", positive=True)                          # s = sqrt(rho^2 + rho + 1)
bc_note = 2 * M * (rho + s + 2) ** 3 / ((rho + 3) * (s + 1) * (rho + s + 1))
Dr = sp.together(D.subs({a: aa, p: rho * aa, b: bc_note}))
num = sp.numer(Dr)
red = sp.rem(sp.Poly(sp.expand(num), s), sp.Poly(s ** 2 - rho ** 2 - rho - 1, s))
check("B1 block 110 T3's closed form b_c/M = 2(rho + s + 2)^3/((rho+3)(s+1)(rho+s+1)) is a root of the discriminant (reduced with s^2 = rho^2 + rho + 1)",
      sp.expand(red.as_expr()) == 0)
# the double root: at b = b_c the cubic has the double root u* = 1/r*, r* = a + p + sqrt(a^2 + ap + p^2)
S = sp.sqrt(a ** 2 + a * p + p ** 2)
rs = a + p + S; us = 1 / rs; bcs = (rs + a) ** 3 / (rs * (rs - p))
ok = sp.simplify(cub.subs({u: us, b: bcs})) == 0 and sp.simplify(sp.diff(cub, u).subs({u: us, b: bcs})) == 0
check("B2 at b = b_c the cubic has the double root u* = 1/(a + p + sqrt(a^2 + ap + p^2)) (the circular ray), and 0 < u* < 1/p", ok and sp.simplify(1 / p - us).is_positive is not False)
vals = {}
for rv in (0, sp.Rational(1, 2), 1, 3):
    sv = sp.sqrt(rv ** 2 + rv + 1)
    vals[rv] = sp.nsimplify(sp.radsimp(sp.simplify((bc_note / M).subs({rho: rv, s: sv}))))
check("B3 b_c/M = 9/2, 4 sqrt7 - 40/7, 3 sqrt3, (70 + 26 sqrt13)/27 at rho = 0, 1/2, 1, 3",
      [sp.simplify(vals[0] - sp.Rational(9, 2)), sp.simplify(vals[sp.Rational(1, 2)] - (4 * sp.sqrt(7) - sp.Rational(40, 7))),
       sp.simplify(vals[1] - 3 * sp.sqrt(3)), sp.simplify(vals[3] - (70 + 26 * sp.sqrt(13)) / 27)] == [0, 0, 0, 0], str(vals))
lim = sp.limit((bc_note / M).subs(s, sp.sqrt(rho ** 2 + rho + 1)), rho, sp.oo)
check("B4 b_c/M -> 8 as rho -> oo", lim == 8)
# monotonicity by the envelope of w(u) = u(1 - p u)/(1 + a u)^3 (b_c = 1/max w): d(1/b_c)/drho = d w/drho at fixed u = u*
x = sp.Symbol("x", positive=True)
W = x * (1 - rho * aa / M * x) / (1 + aa / M * x) ** 3          # M = 1 units, x = M u
xs = (1 / (rs / M)).subs({a: aa, p: rho * aa})
dW = sp.simplify(sp.diff(W, rho).subs(x, xs))
okm = all(sp.N(dW.subs(rho, rv)) < 0 for rv in [sp.Rational(k, 4) for k in range(0, 41)] + [20, 100, 1000])
check("B5 d(max_u w)/drho < 0 on a grid of 44 rho in [0, 1000] (evaluated from the exact expression): b_c rises with rho", okm)

# ================================================================ C: the radius of the turn series in 1/b
wexpr = u * (1 - p * u) / (1 + a * u) ** 3
dw = sp.factor(sp.diff(wexpr, u))
check("C1 w(u) = u(1-pu)/(1+au)^3 = 1/(r n): w'(u) = (1 - 2(a+p)u + a p u^2)/(1 + a u)^4", sp.simplify(dw - (1 - 2 * (a + p) * u + a * p * u ** 2) / (1 + a * u) ** 4) == 0, str(dw))
um = 1 / (a + p - S)
wm = sp.simplify(wexpr.subs(u, um))
ok = sp.simplify(wexpr.subs(u, us) - 1 / bcs) == 0
test = [(sp.Rational(1, 3), sp.Rational(1, 7)), (1, 1), (2, 5), (sp.Rational(1, 10), 3)]
ok2 = all(sp.N(wm.subs({a: A_, p: P_})) < 0 and sp.N((1 / (a + p - S)).subs({a: A_, p: P_})) > sp.N((1 / p).subs({a: A_, p: P_})) for A_, P_ in test)
check("C2 the finite critical values of w are w* = 1/b_c (at u* in (0, 1/p)) and w- = w(1/(a+p-S)) < 0 with 1/(a+p-S) > 1/p (tested at 4 (a,p))", ok and ok2)
ok = all(sp.N((1 - 2 * (a + p) * u + a * p * u ** 2).subs({a: A_, p: P_, u: -sp.Rational(k, 10) / A_})) > 0 for A_, P_ in test for k in range(0, 10))
check("C3 on (-1/a, 0] the quadratic 1 - 2(a+p)u + apu^2 > 0 (all terms positive): the principal branch u(w) is increasing and analytic on (-oo, w*)", ok)
dn = sp.factor(sp.diff(sp.log(n_mem), u))
check("C4 d log n/du = (3a/(1+au) + p/(1-pu)) > 0 on [0, 1/p): log n(u(w)) has a square-root branch point at w*, not a removable one",
      sp.simplify(dn - (3 * a / (1 + a * u) + p / (1 - p * u))) == 0)
# floating-point evidence: ratio test on the exact coefficients [u^k] n^k
print("   C5 (floating-point evidence) ratio test on exact coefficients L_k = [u^k] n^k, radius estimate b by Richardson of L_{k+1}/L_k:")
import math
okc = True
for rv in (Fr(1, 2), Fr(1), Fr(3)):
    A_ = Fr(2) / (3 + rv); P_ = rv * A_
    L = []
    for k in range(1, 161):
        tot_ = Fr(0)
        for j in range(k + 1):
            tot_ += math.comb(3 * k, k - j) * math.comb(k + j - 1, j) * A_ ** (k - j) * P_ ** j if k + j - 1 >= 0 else 0
        L.append(tot_)
    rat = [float(L[k] / L[k - 1]) for k in range(1, len(L))]
    kk = len(rat)
    rich = (kk * rat[-1] - (kk - 20) * rat[-21]) / 20      # removes the 1/k term of the ratio
    sv = math.sqrt(float(rv) ** 2 + float(rv) + 1)
    bc_f = 2 * (float(rv) + sv + 2) ** 3 / ((float(rv) + 3) * (sv + 1) * (float(rv) + sv + 1))
    print("      rho = %s: ratio at k = 160: %.6f, Richardson %.6f, b_c/M = %.6f" % (rv, rat[-1], rich, bc_f))
    okc = okc and abs(rich - bc_f) < 2e-3 * bc_f
check("C5 (evidence) the growth rate of the exact coefficients matches b_c/M to 2e-3 at rho = 1/2, 1, 3", okc)

# ================================================================ D: exact box examples
K8 = Fr(1)            # 8K = 1 throughout (K = 1/8)
def box(L):
    inter = [(i, j, k) for i in range(1, L - 1) for j in range(1, L - 1) for k in range(1, L - 1)]
    idx = {z: n for n, z in enumerate(inter)}
    def nbrs(z):
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            yield (z[0] + d[0], z[1] + d[1], z[2] + d[2])
    return inter, idx, nbrs
def solve(Amat, rhs):
    n = len(rhs); Aa = [row[:] + [rhs[i]] for i, row in enumerate(Amat)]
    for col in range(n):
        piv = next(r for r in range(col, n) if Aa[r][col] != 0); Aa[col], Aa[piv] = Aa[piv], Aa[col]
        pv = Aa[col][col]
        Aa[col] = [x_ / pv for x_ in Aa[col]]
        for r in range(n):
            if r != col and Aa[r][col] != 0:
                f = Aa[r][col]; Aa[r] = [x_ - f * y_ for x_, y_ in zip(Aa[r], Aa[col])]
    return [Aa[i][n] for i in range(n)]
def configure(L, src, bonds):
    """src: interior site -> s > 0 (Lap chi = -s there); bonds: {(x, y): B} content bond energies (y may be a wall site).
       Returns chi, N (walls 1), e, tau, rest energies, and the member's F, the charges P, Q as wall fluxes."""
    inter, idx, nbrs = box(L); n = len(inter)
    wall = lambda z: z not in idx
    A = [[Fr(0)] * n for _ in range(n)]
    for z in inter:
        i = idx[z]
        for y in nbrs(z):
            A[i][i] -= 1
            if not wall(y): A[i][idx[y]] += 1
    # Lap chi = -s with chi = 1 on walls:  sum_y chi_y - 6 chi_z = -s  ->  A chi = -s - (#wall nbrs)
    rhs = [-src.get(z, Fr(0)) - sum(1 for y in nbrs(z) if wall(y)) for z in inter]
    chi = solve(A, rhs)
    tau = {z: Fr(0) for z in inter}
    for (x_, y_), B in bonds.items():
        if x_ in idx: tau[x_] += B / 2
        if y_ in idx: tau[y_] += B / 2
    # Lap N + N (Lap chi)/chi = 2 tau/(8K chi):   A N - diag(s/chi) N = 2 tau/(8K chi) - (#wall nbrs)
    A2 = [row[:] for row in A]
    for z in inter:
        i = idx[z]; A2[i][i] -= src.get(z, Fr(0)) / chi[i]
    rhs2 = [2 * tau[z] / (K8 * chi[idx[z]]) - sum(1 for y in nbrs(z) if wall(y)) for z in inter]
    N = solve(A2, rhs2)
    lap = lambda f, z: sum((f[idx[y]] if not wall(y) else Fr(1)) - f[idx[z]] for y in nbrs(z))
    e_ = {z: -K8 * N[idx[z]] * lap(chi, z) for z in inter}                   # e = -8K w chi Lap chi = -8K N Lap chi
    rest = {z: e_[z] - tau[z] for z in inter}
    # member field energy over bonds with an interior end, walls held at 1
    F = Fr(0); seen = set()
    for z in inter:
        for y in nbrs(z):
            key = tuple(sorted([z, y]))
            if key in seen: continue
            seen.add(key)
            Ny = N[idx[y]] if not wall(y) else Fr(1); cy = chi[idx[y]] if not wall(y) else Fr(1)
            F += -K8 * (Ny - N[idx[z]]) * (cy - chi[idx[z]])
    Q = -sum(lap(chi, z) for z in inter); P = sum(lap(N, z) for z in inter)
    return dict(inter=inter, idx=idx, chi=chi, N=N, e=e_, tau=tau, rest=rest, F=F, P=P, Q=Q, lap=lap, Hhop=sum(bonds.values()),
                Hrest=sum(rest.values()))
def verify(cfg, label, away_from_walls=True):
    idx, chi, N, e_, tau = cfg["idx"], cfg["chi"], cfg["N"], cfg["e"], cfg["tau"]
    lap = cfg["lap"]
    ok_site = all(lap(chi, z) == -e_[z] / (K8 * (N[idx[z]] / chi[idx[z]]) * chi[idx[z]]) and
                  lap(N, z) == (e_[z] + 2 * tau[z]) / (K8 * chi[idx[z]]) for z in cfg["inter"])
    Qs = sum(e_[z] / (K8 * (N[idx[z]] / chi[idx[z]]) * chi[idx[z]]) for z in cfg["inter"])
    Ps = sum((e_[z] + 2 * tau[z]) / (K8 * chi[idx[z]]) for z in cfg["inter"])
    diff = sum((2 * tau[z] - e_[z] * (1 - N[idx[z]] / chi[idx[z]]) / (N[idx[z]] / chi[idx[z]])) / chi[idx[z]] for z in cfg["inter"]) / K8
    ok_ch = Qs == cfg["Q"] and Ps == cfg["P"] and cfg["P"] - cfg["Q"] == diff
    H = cfg["Hrest"] + cfg["Hhop"]
    g1 = K8 * cfg["Q"] - (H + cfg["F"]); g2 = K8 / 2 * (cfg["P"] + cfg["Q"]) - (cfg["Hrest"] + 2 * cfg["Hhop"])
    return ok_site, ok_ch, g1, g2
L = 7
c0 = (3, 3, 3); c1 = (3, 3, 4)
# D1 generic content: two sources, one content bond between them
cfg = configure(L, {c0: Fr(1, 2), c1: Fr(1, 3)}, {(c0, c1): Fr(1, 20)})
s1, s2, g1, g2 = verify(cfg, "generic")
wv = {z: cfg["N"][cfg["idx"][z]] / cfg["chi"][cfg["idx"][z]] for z in (c0, c1)}
check("D1 7x7x7 box (125 interior sites), sources 1/2, 1/3 on two neighbours, content bond energy 1/20, 8K = 1: site equations exact at all 125 sites, "
      "Q = sum e/(8Kw chi), P = sum (e+2tau)/(8K chi), P - Q = (1/8K) sum [2tau - e(1-w)/w]/chi, 8KQ = H + F and 4K(P+Q) = H_rest + 2 H_hop exactly",
      s1 and s2 and g1 == 0 and g2 == 0, "P = %.6f, Q = %s, clocks %.4f %.4f, rest parts %.4f %.4f" %
      (float(cfg["P"]), cfg["Q"], float(wv[c0]), float(wv[c1]), float(cfg["rest"][c0]), float(cfg["rest"][c1])))
# D2 a balanced configuration: the charge P is affine in the bond energy; solve P = Q exactly
cfgA = configure(L, {c0: Fr(1, 2), c1: Fr(1, 3)}, {(c0, c1): Fr(0)})
cfgB = configure(L, {c0: Fr(1, 2), c1: Fr(1, 3)}, {(c0, c1): Fr(1)})
lam = (cfgA["Q"] - cfgA["P"]) / (cfgB["P"] - cfgA["P"])
cfgC = configure(L, {c0: Fr(1, 2), c1: Fr(1, 3)}, {(c0, c1): lam})
s1, s2, g1, g2 = verify(cfgC, "balanced")
wC = [cfgC["N"][cfgC["idx"][z]] / cfgC["chi"][cfgC["idx"][z]] for z in (c0, c1)]
rC = [cfgC["rest"][z] for z in (c0, c1)]
check("D2 balanced content: bond energy B* = %s (exact rational) gives P = Q = 5/6 exactly with positive rest parts; clocks %.4f, %.4f; F = H_hop (T2(e)) exactly"
      % ("%d/%d digits" % (len(str(lam.numerator)), len(str(lam.denominator))), float(wC[0]), float(wC[1])),
      s1 and s2 and cfgC["P"] == cfgC["Q"] == Fr(5, 6) and min(rC) > 0 and g1 == 0 and g2 == 0 and cfgC["F"] == cfgC["Hhop"],
      "B* = %.6f, rest parts %.6f %.6f" % (float(lam), float(rC[0]), float(rC[1])))
# D3 the weighted bound: balanced content must have sum (e/chi)(1-3w)/w <= 0 when 0 <= tau <= e
wsum = sum(cfgC["e"][z] / cfgC["chi"][cfgC["idx"][z]] * (1 - 3 * wv_) / wv_ for z, wv_ in zip((c0, c1), wC))
check("D3 T2(d) on D2: 0 <= tau <= e at both content sites and sum (e/chi)(1 - 3w)/w = %.6f <= 0" % float(wsum),
      all(0 <= cfgC["tau"][z] <= cfgC["e"][z] for z in (c0, c1)) and wsum <= 0)
# D4 too compact: strong sources push clocks below 1/3; balance then needs a negative rest part
cfgA = configure(L, {c0: Fr(3), c1: Fr(3)}, {(c0, c1): Fr(0)})
cfgB = configure(L, {c0: Fr(3), c1: Fr(3)}, {(c0, c1): Fr(1)})
lam4 = (cfgA["Q"] - cfgA["P"]) / (cfgB["P"] - cfgA["P"])
cfgD = configure(L, {c0: Fr(3), c1: Fr(3)}, {(c0, c1): lam4})
wD = [cfgD["N"][cfgD["idx"][z]] / cfgD["chi"][cfgD["idx"][z]] for z in (c0, c1)]
s1, s2, g1, g2 = verify(cfgD, "compact")
check("D4 sources 3, 3: clocks %.4f, %.4f < 1/3 at P = Q, and balance forces rest parts %.4f, %.4f < 0 (T2(d)'s bound, exact)"
      % (float(wD[0]), float(wD[1]), float(cfgD["rest"][c0]), float(cfgD["rest"][c1])),
      s1 and s2 and cfgD["P"] == cfgD["Q"] and max(wD) < Fr(1, 3) and max(cfgD["rest"][z] for z in (c0, c1)) < 0)
# D5 content on a bond touching a held wall: site equations and charges still exact; the global identities fail
cw = (1, 3, 3); wallsite = (0, 3, 3)
cfgW = configure(L, {cw: Fr(1, 2)}, {(cw, wallsite): Fr(1, 10)})
s1, s2, g1, g2 = verify(cfgW, "wall")
check("D5 content bond from an interior site next to a wall into the wall (B = 1/10): site equations and charge formulas exact, but "
      "8KQ - (H + F) = %s and 4K(P + Q) - (H_rest + 2H_hop) = %s, both nonzero: T2(e) needs content away from the walls" % (g1, g2),
      s1 and s2 and g1 != 0 and g2 != 0)
# D6 one content site balances iff w = e/(e + 2 tau): check on a single source with content bond energy chosen to balance
cfgA = configure(L, {c0: Fr(1, 2)}, {})
check("D6 a single body at rest (tau = 0): P = w0 Q exactly (block 60), P = %.6f, Q = 1/2, w0 = %.6f" %
      (float(cfgA["P"]), float(cfgA["N"][cfgA["idx"][c0]] / cfgA["chi"][cfgA["idx"][c0]])),
      cfgA["P"] == cfgA["N"][cfgA["idx"][c0]] / cfgA["chi"][cfgA["idx"][c0]] * cfgA["Q"])

print("")
print("TOTAL: PASS=%d FAIL=%d (%.0f s)" % (len(PASS), len(FAIL), time.time() - t_start))
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("HIT: the turn of block 110's curvature-member exterior at every order in closed form, chi(b) = sum_k m_k [u^k] n(u)^k b^-k with "
          "m_k = sqrt(pi) Gamma((k+1)/2)/Gamma(k/2+1), for the member sum_j C(3k,k-j) C(k+j-1,j) a^(k-j) p^j (Lagrange inversion of w = u/n(u); "
          "block 110's T4 orders 1-4 and T5 reproduced), and the series in 1/b has radius exactly 1/b_c, the capture threshold, for every charge ratio")
    print("SUMMARY: PARTIAL all-orders turn formula (orbit integral expanded directly, Lagrange inversion), T3 re-derived by the discriminant, "
          "radius of the turn series = capture threshold at every rho, T2(a)-(e) and the wall hypothesis checked on exact 7^3 boxes (balanced, too-compact, wall)")
