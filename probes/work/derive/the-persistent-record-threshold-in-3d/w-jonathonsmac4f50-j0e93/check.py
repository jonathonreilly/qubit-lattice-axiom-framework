#!/usr/bin/env python3
"""The persistent-record threshold in 3D (block 96 T2): exact boundaries along the axes and the body diagonal.

M(k) = E(k) T,  E = diag(exp(-i k.d)) over d in {+-e1, +-e2, +-e3},  T = p I + ((1-p)/5)(J - I) = a I + q J,
a = (6p-1)/5, q = (1-p)/5.  Exact sympy arithmetic throughout (z = exp(-i kappa) kept as a symbol where needed).
"""
import sys
import sympy as sp

FAIL = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

lam, p, c, z, s, t, eps = sp.symbols('lambda p c z s t epsilon')
q = (1 - p) / 5; a = (6 * p - 1) / 5
check("0 T = a I + q J with a = (6p-1)/5, q = (1-p)/5; rows of T sum to 1 (a + 6q = 1)", sp.simplify(a + 6 * q - 1) == 0)
T = p * sp.eye(6) + q * (sp.ones(6, 6) - sp.eye(6))
check("0 T equals a I + q J", sp.simplify(T - (a * sp.eye(6) + q * sp.ones(6, 6))) == sp.zeros(6, 6))
def charpoly6(Ediag):
    M = sp.diag(*Ediag) * T
    return sp.together((lam * sp.eye(6) - M).det(method='berkowitz'))
D = lam ** 2 - 2 * a * lam * c + a ** 2            # = |lam e^{i kappa} - a|^2 for real lam, c = cos kappa
cz = (z + 1 / z) / 2

# ------------------------------------------------------------------ axis k = (kappa, 0, 0)
P = sp.expand((lam - a) * D - q * ((lam - a) * (2 * lam * c - 2 * a) + 4 * D))
full_axis = charpoly6([z, 1 / z, 1, 1, 1, 1])
check("A1 axis: det(lam - M) = (lam - a)^3 P(lam), P the cubic of the secular equation",
      sp.simplify(full_axis - (lam - a) ** 3 * P.subs(c, cz)) == 0)
coeffs = sp.Poly(P, lam).all_coeffs()
print("     P coefficients:", [sp.factor(x) for x in coeffs])
G = 4 / (lam - a) + 2 * (lam * c - a) / D
check("A2 P = (lam - a) D (1 - q G), G(lam) = 4/(lam-a) + 2 Re 1/(lam e^{i kappa} - a)", sp.simplify(P - (lam - a) * D * (1 - q * G)) == 0)
check("A2 D = (lam - a)^2 + 2 a lam (1 - c): so D >= (lam - a)^2 for lam > 0, a > 0", sp.expand(D - (lam - a) ** 2 - 2 * a * lam * (1 - c)) == 0)
# G'(lam) = -4/(lam-a)^2 - 2 (lam^2 c - 2 a lam + a^2 c)/D^2 and |lam^2 c - 2a lam + a^2 c| <= D
Gp = sp.diff(G, lam)
N2 = lam ** 2 * c - 2 * a * lam + a ** 2 * c
check("A3 G' = -4/(lam-a)^2 - 2 N/D^2 with N = lam^2 c - 2 a lam + a^2 c = Re[e^{-i kappa}(lam e^{i kappa} - a)^2]",
      sp.simplify(Gp - (-4 / (lam - a) ** 2 - 2 * N2 / D ** 2)) == 0)
# |N| <= D:  D^2 - N^2 = (1 - c^2)(lam^2 - a^2)^2 >= 0
check("A3 D^2 - N^2 = (1 - c^2)(lam^2 - a^2)^2 >= 0, so |N|/D^2 <= 1/D <= 1/(lam-a)^2 and G' <= -2/(lam-a)^2 < 0 on (a, oo)",
      sp.expand(D ** 2 - N2 ** 2 - (1 - c ** 2) * (lam ** 2 - a ** 2) ** 2) == 0)
check("A4 P(a) = -8 q a^2 (1 - c) < 0 for c < 1, p in (1/6, 1)", sp.expand(P.subs(lam, a) + 8 * q * a ** 2 * (1 - c)) == 0)
check("A4 the pair term of G at lam = a equals -1/a for c != 1 (finite): 2(ac - a)/D(a) = -1/a",
      sp.simplify((2 * (lam * c - a) / D).subs(lam, a) + 1 / a) == 0)
check("A4 at kappa = 0 the root in (a, oo) is 1: P(1) = 0 at c = 1", sp.expand(P.subs({c: 1, lam: 1})) == 0)
# leading multiplier: P(t^2) with a = t^3
Pt = sp.expand(P.subs(p, (5 * t ** 3 + 1) / 6).subs(lam, t ** 2))
lin = sp.expand(t * (2 * c * p + 8 * c + 4 * p + 1) - (10 * c * p + 2 * p + 3)).subs(p, (5 * t ** 3 + 1) / 6)
check("A5 with a = t^3: P(t^2) = (t^4/5) [t(2cp + 8c + 4p + 1) - (10cp + 2p + 3)]", sp.simplify(Pt - t ** 4 / 5 * lin) == 0)
e1 = sp.factor(sp.expand(lin.subs(c, 1))); em1 = sp.factor(sp.expand(lin.subs(c, -1)))
print("     bracket at c = 1:", e1, "   at c = -1:", em1)
check("A5 bracket at c = +1 is 5(t-1)^3(t+1) and at c = -1 is (5/3)(t-1)(t+1)(t^2+4t+1): both < 0 for t in (0,1)",
      sp.expand(e1 - 5 * (t - 1) ** 3 * (t + 1)) == 0 and sp.expand(em1 - sp.Rational(5, 3) * (t - 1) * (t + 1) * (t ** 2 + 4 * t + 1)) == 0)
check("A5 the bracket is linear in c (so negative on all of [-1, 1])", sp.degree(sp.expand(lin), c) == 1)
check("A5 product of the three roots of P is a^2", sp.simplify(-coeffs[3] - a ** 2) == 0)
# block 96's executed statement at (pi/2, 0, 0), p = 9/10
P96 = P.subs({p: sp.Rational(9, 10), c: 0})
d96 = sp.discriminant(P96, lam)
check("A6 block 96 at (pi/2,0,0), p=9/10: P(9/10) < 0 < P(1) and discriminant < 0 (one real root, two non-real)",
      P96.subs(lam, sp.Rational(9, 10)) < 0 and P96.subs(lam, 1) > 0 and d96 < 0)
Qc = sp.factor(sp.discriminant(P, lam))
check("A7 at kappa = pi: disc = 64 (1-p)^2 (6p-1)^2 (p^2+28p-4)/15625 > 0 for p > 10 sqrt2 - 14: three real roots there (the pair near a has returned to the real line; the density root stays the only one above a)",
      sp.expand(Qc.subs(c, -1) - sp.Rational(64, 15625) * (1 - p) ** 2 * (6 * p - 1) ** 2 * (p ** 2 + 28 * p - 4)) == 0
      and (-14 + 10 * sp.sqrt(2)) in sp.solve(p ** 2 + 28 * p - 4, p))

# ------------------------------------------------------------------ body diagonal k = kappa (1,1,1)
Qd = sp.expand(lam ** 2 - 2 * lam * c * (a + 3 * q) + a * (a + 6 * q))
full_diag = charpoly6([z, 1 / z, z, 1 / z, z, 1 / z])
check("B1 diagonal: det(lam - M) = (lam - a z)^2 (lam - a/z)^2 Q(lam), Q = lam^2 - 2 lam c (3p+2)/5 + (6p-1)/5",
      sp.simplify(full_diag - (lam - a * z) ** 2 * (lam - a / z) ** 2 * Qd.subs(c, cz)) == 0
      and sp.simplify(Qd - (lam ** 2 - 2 * lam * c * (3 * p + 2) / 5 + (6 * p - 1) / 5)) == 0)
disc4 = sp.expand((c * (3 * p + 2) / 5) ** 2 - (6 * p - 1) / 5)
check("B2 quarter-discriminant = [9(1-p)^2 - s^2 (3p+2)^2]/25 with s^2 = 1 - c^2",
      sp.expand(disc4.subs(c ** 2, 1 - s ** 2) - (9 * (1 - p) ** 2 - s ** 2 * (3 * p + 2) ** 2) / 25) == 0)
print("     => the density branch on the diagonal is non-real  iff  |sin kappa| > 3(1-p)/(3p+2)   (line: (1-p)/p)")
check("B2 at kappa = 0 the roots of Q are 1 and (6p-1)/5 (density branch = the root 1)",
      sp.expand(Qd.subs({c: 1, lam: 1})) == 0 and sp.expand(Qd.subs({c: 1, lam: a})) == 0)
check("B3 threshold below the zone edge iff 3(1-p) < 3p+2 iff p > 1/6", sp.solve(sp.Eq(3 * (1 - p), 3 * p + 2), p) == [sp.Rational(1, 6)])
check("B3 when non-real, the pair has modulus^2 = a = (6p-1)/5 > a^2 (the other four multipliers a e^{+-i kappa}): it is the leading pair",
      sp.expand(Qd.subs(lam, 0) - a) == 0)
print("     when real, the larger root >= sqrt(a) > a (product a): the leading multiplier is real; so the leading multiplier leaves the real line exactly at the threshold")
# (b) scaling
kstar = sp.asin(3 * eps / (5 - 3 * eps))
ser = sp.series(kstar, eps, 0, 4).removeO()
print("     kappa* = asin(3 eps/(5 - 3 eps)), eps = 1 - p:", ser)
check("B4 kappa* = 3 eps/5 + 9 eps^2/25 + O(eps^3): memory length 1/kappa* ~ 5/(3(1-p)) per coordinate, |k*| ~ 3 sqrt3 (1-p)/5",
      sp.expand(ser - (sp.Rational(3, 5) * eps + sp.Rational(9, 25) * eps ** 2)) .coeff(eps, 1) == 0
      and sp.expand(ser).coeff(eps, 2) == sp.Rational(9, 25))
check("B4 check of 3(1-p)/(3p+2) = 3 eps/(5 - 3 eps)", sp.simplify((3 * (1 - p) / (3 * p + 2)).subs(p, 1 - eps) - 3 * eps / (5 - 3 * eps)) == 0)
# consistency with block 96's executed 24^3 grid (diagonal points kappa = n pi/12)
def nonreal_diag(pv, kap):
    return sp.sin(kap) ** 2 > (3 * (1 - pv) / (3 * pv + 2)) ** 2
g1 = nonreal_diag(sp.Rational(9, 10), sp.pi / 12) and nonreal_diag(sp.Rational(99, 100), sp.pi / 12)
g2 = (not nonreal_diag(sp.Rational(1, 2), sp.pi / 12)) and nonreal_diag(sp.Rational(1, 2), sp.pi / 6)
check("B5 block 96 W2: at p = 9/10, 99/100 the first diagonal grid point (|k| = 0.453) is past the threshold; at p = 1/2 the first is real "
      "and the second (|k| = 0.907 > 0.8) is not", bool(g1) and bool(g2))
# line reference (block 96 T2.1)
mu = sp.Symbol('mu')
line = mu ** 2 - 2 * p * c * mu + (2 * p - 1)
check("C the line's quarter-discriminant p^2 c^2 - (2p-1) = (1-p)^2 - p^2 s^2 (block 96 T2.1: |sin k| > (1-p)/p)",
      sp.expand((p ** 2 * c ** 2 - (2 * p - 1)).subs(c ** 2, 1 - s ** 2) - ((1 - p) ** 2 - p ** 2 * s ** 2)) == 0)

print()
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + FAIL[0]); sys.exit(1)
print("SUMMARY: PROVED along the body diagonal k = kappa(1,1,1) the density branch, which is the leading multiplier, is non-real exactly "
      "when |sin kappa| > 3(1-p)/(3p+2) (p > 1/6; the line's (1-p)/p); along the axes it is real, simple and the unique root above "
      "(6p-1)/5 for every kappa in [0, pi] and p in (1/6, 1), and the leading multiplier is real there (no threshold on the axes); "
      "kappa* = 3(1-p)/5 + 9(1-p)^2/25 + O((1-p)^3)")
print("HIT: (a) exact: on the body diagonal the leading (density) multiplier leaves the real line exactly at |sin kappa| = 3(1-p)/(3p+2); "
      "on the axes it never does (secular function strictly decreasing above (6p-1)/5); (b) kappa* ~ 3(1-p)/5, memory length 5/(3(1-p))")
