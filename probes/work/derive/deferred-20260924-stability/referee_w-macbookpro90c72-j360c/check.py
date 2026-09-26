#!/usr/bin/env python3
"""Independent cubic for the traceless anisotropy.

Does not import the author's script. Taylor coefficients are exact.
The window above threshold uses a monotone lower sum with outward
rounding. Dominated convergence, Taylor's remainder, and Jensen's
inequality are imports. The floating-point scans are not rebuilt.
"""
import math
from fractions import Fraction as Fr

import sympy as sp
from mpmath import iv, mp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


e = sp.symbols("epsilon", real=True)
a, b = sp.symbols("a b", positive=True)
u1, u2, u3 = sp.symbols("u1 u2 u3", nonnegative=True)
S = a + b
Q = (1 + 2 * e) ** 2 * a + (1 - e) ** 2 * b
series = sp.series(sp.sqrt(Q), e, 0, 4).removeO()
c1, c2, c3 = [sp.simplify(series.coeff(e, k)) for k in (1, 2, 3)]


def axis(expr):
    f = sp.Lambda((a, b), expr)
    return (f(u1, u2 + u3) + f(u2, u3 + u1) + f(u3, u1 + u2)) / 3


s1 = u1 + u2 + u3
s2 = u1 * u2 + u2 * u3 + u3 * u1
s3 = u1 * u2 * u3
gap_poly = u1 * (u2 - u3) ** 2 + u2 * (u3 - u1) ** 2 + u3 * (u1 - u2) ** 2
check(
    "S1 arithmetic cubic",
    sp.simplify(sp.diff(sp.sqrt(Q), e, 2) - 9 * a * b / Q ** sp.Rational(3, 2)) == 0
    and sp.simplify(axis(c1)) == 0
    and sp.simplify(2 * c2 - 9 * a * b / S ** sp.Rational(3, 2)) == 0
    and sp.simplify(c3 + sp.Rational(9, 2) * a * b * (2 * a - b) / S ** sp.Rational(5, 2)) == 0
    and sp.expand(sp.simplify(axis(c3) * s1 ** sp.Rational(5, 2)) + sp.Rational(3, 2) * (s1 * s2 - 9 * s3)) == 0
    and sp.expand(s1 * s2 - 9 * s3 - gap_poly) == 0,
    "second derivative 9ab/Q^(3/2); axis-averaged cubic -(3/2)(s1 s2-9 s3)/S^(5/2), and that numerator is a sum of squares",
)

Qg = sp.exp(4 * e) * a + sp.exp(-2 * e) * b
gser = sp.series(sp.sqrt(Qg), e, 0, 4).removeO()
g1, g2, g3 = [sp.simplify(gser.coeff(e, k)) for k in (1, 2, 3)]
log_cubic = sp.expand(sp.simplify(axis(g3) * s1 ** sp.Rational(5, 2)))
check(
    "S2 log cubic",
    sp.simplify(axis(g1)) == 0
    and sp.simplify(axis(2 * g2) - (axis(9 * a * b / S ** sp.Rational(3, 2)) + 2 * sp.sqrt(s1))) == 0
    and sp.expand(log_cubic - (s1**3 + sp.Rational(9, 2) * s1 * s2 + sp.Rational(81, 2) * s3) / 3) == 0,
    "log-rate first order cancels; second order is chi_a + 2<|s|>; the cubic numerator is a sum of nonnegative terms",
)

D2 = 4 * a + b
Qp = sp.diff(Q, e)
fourth = sp.diff(sp.sqrt(Q), e, 4)
check(
    "R1 fourth derivative",
    sp.simplify(fourth + sp.Rational(27, 2) * a * b * (2 * D2 * Q - sp.Rational(5, 2) * Qp**2) / Q ** sp.Rational(7, 2)) == 0,
    "d4 sqrt(Q)/de4 = -(27/2) ab (2 D2 Q - 5/2 Q'^2) / Q^(7/2)",
)

e0 = Fr(1, 100)
M0 = (1 + 2 * e0) ** 2
J_up = Fr(12248, 10000)
check("R1 Jensen", J_up * J_up >= Fr(3, 2), "12248/10000 >= sqrt(3/2) >= <|s|>")
K = Fr(162, 24) * M0 * J_up / (1 - 2 * e0) ** 7

iv.dps = 25
n = 24
scale = 10**18


def frac_floor(x):
    return Fr(int(mp.floor(mp.mpf(x) * scale)), scale)


def frac_ceil(x):
    return Fr(int(mp.ceil(mp.mpf(x) * scale)), scale)


boxes = []
for j in range(n):
    left = iv.sin(iv.pi * j / (2 * n)) ** 2
    right = iv.sin(iv.pi * (j + 1) / (2 * n)) ** 2
    boxes.append((frac_floor(left.a), frac_ceil(right.b)))


def separation(p, q):
    return max(Fr(0), p[0] - q[1], q[0] - p[1])


total = Fr(0)
for i1 in range(n):
    for i2 in range(i1, n):
        for i3 in range(i2, n):
            B = (boxes[i1], boxes[i2], boxes[i3])
            num = (B[0][0] * separation(B[1], B[2]) ** 2
                   + B[1][0] * separation(B[2], B[0]) ** 2
                   + B[2][0] * separation(B[0], B[1]) ** 2)
            if num == 0:
                continue
            S_hi = B[0][1] + B[1][1] + B[2][1]
            root = Fr(math.isqrt(math.ceil(S_hi * scale * scale)) + 1, scale)
            weight = 6 if i1 < i2 < i3 else 1 if i1 == i2 == i3 else 3
            total += weight * num / (S_hi * S_hi * root)
e3_lo = Fr(3, 2) * total / n**3
t = e3_lo / (2 * K)
eta = e3_lo ** 2 / (4 * K)
width = eta / 36
check(
    "R2 window",
    e3_lo > Fr(13, 100) and t <= e0 and width > Fr(1, 100000),
    f"e3 >= {float(e3_lo):.5f}, test point {-float(t):.5f}, window width {float(width):.3e} in beta",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL the traceless path is decided by its cubic. "
        "Arithmetic rates have e3 = (3/2)<sum u_i(u_j-u_k)^2/|s|^5> > 0, so at beta = chi_a/72 the path descends for epsilon < 0. "
        "Log rates have the opposite cubic sign, so they descend for epsilon > 0. "
        f"A certified window above the arithmetic threshold has width {float(width):.3e}. "
        "The global scan, the log quartic, and the chord inequality were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - at either quadratic threshold the uniform rates are not a local minimum along the traceless path: "
        "arithmetic rates descend toward a weaker special axis, and log rates descend toward a stronger one. "
        f"In linear rates the descent persists on a beta interval of width {float(width):.3e} above chi_a/72.",
        flush=True,
    )
