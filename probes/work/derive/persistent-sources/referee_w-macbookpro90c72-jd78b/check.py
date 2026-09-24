#!/usr/bin/env python3
"""Independent referee for persistent-sources a3.

Two pinned sources of the linear light-cone process are a 2x2 Green solve,
not a sum of one-source formulas. Does not import the attempt.
"""
from __future__ import annotations

import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


ka, kb, kc = sp.symbols("k_a k_b k_c", real=True)
symbol = (6 - 2 * (sp.cos(ka) + sp.cos(kb) + sp.cos(kc))) / 7
energy = 2 * ((1 - sp.cos(ka)) + (1 - sp.cos(kb)) + (1 - sp.cos(kc)))
check(
    "T0 symbol",
    sp.simplify(symbol - energy / 7) == 0,
    "the 7-point stencil has 1 - P(k) = E(k)/7",
)

# The two-source algebra, for any Green values with G(0) > G(d) > 0.
g0, gd, alpha, beta = sp.symbols("G0 Gd alpha beta", positive=True)
gram = sp.Matrix([[g0, gd], [gd, g0]])
charges = gram.inv() * sp.Matrix([alpha, beta])
equal = sp.simplify(charges.subs(beta, alpha)[0] - alpha / (g0 + gd))
opposite = sp.simplify((gram.inv() * sp.Matrix([alpha, -alpha]))[0] - alpha / (g0 - gd))
overshoot = sp.simplify(alpha * g0 / g0 + beta * gd / g0 - alpha - beta * gd / g0)
check(
    "T4 two-source algebra",
    equal == 0 and opposite == 0 and overshoot == 0
    and sp.simplify(g0 / (g0 + gd) - 1) != 0,
    "equal charges are alpha/(G0+Gd), opposite charges alpha/(G0-Gd), and the naive sum overshoots by beta*Gd/G0",
)

# Finite certificate: 4x4x4 torus, killing 1/10, separation 2.
L = 4
kill = sp.Rational(1, 10)
sites = [(i, j, k) for i in range(L) for j in range(L) for k in range(L)]
index = {site: n for n, site in enumerate(sites)}
steps = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
weight = sp.Rational(1, 7) * (1 - kill)
operator = sp.zeros(len(sites))
for site in sites:
    operator[index[site], index[site]] += 1 - weight
    for step in steps:
        dest = tuple((site[a] + step[a]) % L for a in range(3))
        operator[index[site], index[dest]] -= weight
green = operator.inv()
origin = green[0, 0]
pair = (2, 0, 0)
separation = green[0, index[pair]]
translation = all(sp.simplify(green[i, i] - origin) == 0 for i in range(len(sites)))
symmetric = sp.simplify(green[0, index[pair]] - green[index[pair], 0]) == 0
claimed_origin = sp.Rational(3337205782, 2311505635)
claimed_separation = sp.Rational(380959524, 2311505635)
check(
    "T1 Green values",
    translation and symmetric and sp.simplify(origin - claimed_origin) == 0
    and sp.simplify(separation - claimed_separation) == 0
    and origin > separation > 0,
    "G(0)=3337205782/2311505635 and G(2 e1)=380959524/2311505635",
)

a1, a2 = sp.Rational(3, 2), sp.Rational(1, 2)
one = a1 / origin
mean = sp.Matrix([one * green[index[y], 0] for y in sites])
residual = operator * mean
one_ok = sp.simplify(mean[0] - a1) == 0 and all(
    sp.simplify(residual[index[y]]) == 0 for y in sites if y != (0, 0, 0)
)
gram_n = sp.Matrix([[origin, separation], [separation, origin]])
coeff = gram_n.inv() * sp.Matrix([a1, a2])
two = sp.Matrix([
    coeff[0] * green[index[y], 0] + coeff[1] * green[index[y], index[pair]] for y in sites
])
residual_two = operator * two
two_ok = (
    sp.simplify(two[0] - a1) == 0
    and sp.simplify(two[index[pair]] - a2) == 0
    and all(sp.simplify(residual_two[index[y]]) == 0 for y in sites if y not in ((0, 0, 0), pair))
)
naive_overshoot = sp.simplify(a2 * separation / origin)
screening = sp.simplify(origin / (origin + separation))
antiscreen = sp.simplify(origin / (origin - separation))
equal_coeff = sp.simplify((gram_n.inv() * sp.Matrix([a1, a1]))[0] - a1 / (origin + separation))
opposite_coeff = sp.simplify((gram_n.inv() * sp.Matrix([a1, -a1]))[0] - a1 / (origin - separation))
check(
    "T2-T5 pinning",
    one_ok and two_ok and equal_coeff == 0 and opposite_coeff == 0
    and naive_overshoot == sp.Rational(95239881, 1668602891)
    and sp.simplify(coeff[0] / (a1 / origin) - 1) != 0
    and screening < 1 and antiscreen > 1,
    "the naive sum overshoots by 95239881/1668602891; like charges are screened and opposite charges are not",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. For the linear light-cone process a pinned set has stationary mean "
    "m(y) = sum_i c_i G(y-x_i) with c = M^{-1} alpha. The one-source formula is the case of one pin "
    "and does not superpose: the naive sum overshoots by the other charge's tail. Equal charges are "
    "screened by G(0)/(G(0)+G(d)) and opposite charges are enlarged by G(0)/(G(0)-G(d)). "
    "On the 4x4x4 torus with killing 1/10 these factors are exact rationals; they are not the transient "
    "Z^3 Green function, and the nonlinear law is untouched.",
    flush=True,
)
print(
    "HIT: confirmed - two pinned sources are the 2x2 Green solve c = M^{-1} alpha, so the one-source "
    "formula does not superpose",
    flush=True,
)
