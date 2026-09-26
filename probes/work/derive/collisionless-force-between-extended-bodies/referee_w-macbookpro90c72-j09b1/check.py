#!/usr/bin/env python3
"""Independent check of the collisionless single-site remainder.

Does not import the author's script. The body averages and the Dirichlet
quadrature of Phi were not rebuilt. The remainder coefficients are the
delta-method expansion, evaluated exactly.
"""
from fractions import Fraction as Fr
from itertools import product
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


# Dirichlet moments: E[prod W_i^{e_i}] = prod (a_i)_{e_i} / (A)_E
def rising(a, e):
    out = 1
    for t in range(e):
        out *= a + t
    return out


def moment(alpha, powers):
    return Fr(rising(alpha[0], powers[0]) * rising(alpha[1], powers[1]) * rising(alpha[2], powers[2]),
              rising(sum(alpha), sum(powers)))


# a few exact values, including the mean (x+1)/(n+3)
ok_mom = (
    moment((2, 3, 4), (0, 0, 0)) == 1
    and moment((2, 3, 4), (1, 0, 0)) == Fr(2, 9)
    and moment((5, 1, 1), (1, 1, 0)) == Fr(5 * 1, 7 * 8)
    and moment((3, 3, 3), (2, 0, 0)) == Fr(3 * 4, 9 * 10)
)
check("M moments", ok_mom, "Dirichlet moments match the rising-factorial formula")

y = sp.Matrix(sp.symbols("y1:4", positive=True))
radius = sp.sqrt(sum(component**2 for component in y))
phi = y / radius**5


def remainder(direction):
    point = {y[i]: direction[i] for i in range(3)}
    value = phi.subs(point)
    grad = phi.jacobian(y)
    shift = (grad * sp.Matrix([1 - 3 * component for component in y])).subs(point)
    cov = sp.diag(*y) - y * y.T
    second = sp.Matrix([
        sum(cov[i, j] * sp.diff(phi[k], y[i], y[j]) for i in range(3) for j in range(3))
        for k in range(3)
    ]).subs(point) / 2
    norm = sp.sqrt((value.T * value)[0])
    unit = value / norm
    return sp.simplify(-3 + ((unit.T * (shift + second))[0]) / norm)


c111 = remainder([sp.Rational(1, 3)] * 3)
c122 = remainder([sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5)])
c2811 = remainder([sp.Rational(28, 30), sp.Rational(1, 30), sp.Rational(1, 30)])
check(
    "R coefficients",
    c111 == -8 and c122 == sp.Rational(-481, 81) and c2811 == sp.Rational(167603, 34322),
    "c = -8 on the diagonal, -481/81 toward (1,2,2), 167603/34322 toward (28,1,1)",
)

# on the diagonal the mean shift vanishes and the covariance piece is -5
diag = [sp.Rational(1, 3)] * 3
point = {y[i]: diag[i] for i in range(3)}
value = phi.subs(point)
cov = (sp.diag(*y) - y * y.T).subs(point)
second = sp.Matrix([
    sum(cov[i, j] * sp.diff(phi[k], y[i], y[j]) for i in range(3) for j in range(3))
    for k in range(3)
]).subs(point) / 2
norm = sp.sqrt((value.T * value)[0])
unit = value / norm
cov_piece = sp.simplify(((unit.T * second)[0]) / norm)
check(
    "R diagonal split",
    cov_piece == -5,
    "on (1,1,1) the mean equals y-hat, the covariance piece is -5, and -3 + -5 = -8",
)

# lead magnitude m |x|_1^2 / |x|^4, with m = 2^{number of zero coordinates}
def lead_mag(vec):
    zeros = sum(component == 0 for component in vec)
    n1 = sum(abs(component) for component in vec)
    r2 = sum(component**2 for component in vec)
    return Fr((1 << zeros) * n1 * n1, r2 * r2)


def point_factor(vec):
    return lead_mag(vec) * sum(component**2 for component in vec)


check(
    "L lead",
    point_factor((3, 0, 0)) == 4 and point_factor((2, 2, 0)) == 4 and point_factor((1, 1, 1)) == 3
    and lead_mag((1, 2, 2)) == Fr(25, 81) and point_factor((1, 2, 2)) == Fr(25, 9),
    "times r^2 the point-pair factors are 4, 4 and 3; the (1,2,2) force magnitude is 25/81",
)

ball = [p for p in product(range(-6, 7), repeat=3) if p[0]**2 + p[1]**2 + p[2]**2 <= 36]
# integer autocorrelation sums to |ball|^2
offsets = {}
for a in ball:
    for b in ball:
        delta = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
        offsets[delta] = offsets.get(delta, 0) + 1
check(
    "S pairs",
    len(ball) == 925 and sum(offsets.values()) == 925**2,
    "a radius-6 ball has 925 sites, and the pair-offset counts sum to 925^2",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL the single-site law's relative remainder is c/|x|_1 + O(|x|_1^-2), with "
        "c = -8 on the diagonal, -481/81 toward (1,2,2) and 167603/34322 toward (28,1,1). "
        "Those are not -24, -16 and +5.6. The radius-6 ball has 925 sites. "
        "The 20-site body averages were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - the Dirichlet law's 1/n remainder coefficients are -8, -481/81 and 167603/34322 "
        "on (1,1,1), (1,2,2) and (28,1,1), not the -24, -16 and +5.6 quoted as established.",
        flush=True,
    )
