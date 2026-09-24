#!/usr/bin/env python3
"""Referee for J:derive:causal-clauses:a3.

Three-parent kernels on the six axis values. Total variation is half the L1
distance. The author's script is not called.
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

FAILS = []
STATES = (0, 1, 2, 3, 4, 5)


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def anti(s):
    return s ^ 3


def kernel(parents, p, q, r):
    weights = []
    for a in STATES:
        w = Fr(1)
        for u in parents:
            if a == u:
                w *= p
            elif a == anti(u):
                w *= q
            else:
                w *= r
        weights.append(w)
    z = sum(weights)
    return [w / z for w in weights]


def tv(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / 2


def alpha3(p, q, r):
    best = Fr(0)
    for parents in itertools.product(STATES, repeat=3):
        base = kernel(parents, p, q, r)
        for slot in range(3):
            for new in STATES:
                if new == parents[slot]:
                    continue
                alt = parents[:slot] + (new,) + parents[slot + 1 :]
                best = max(best, tv(base, kernel(alt, p, q, r)))
    return best


def closed(p, q=1, r=2):
    """Three equal parents, one flipped to its antipode."""
    s = 0
    eq = kernel((s, s, s), p, q, r)
    fl = kernel((s, s, anti(s)), p, q, r)
    return tv(eq, fl)


# ---------- M1. the four campaign points ----------
points = {
    (3, 1, 2): (Fr(27, 110), Fr(81, 110)),
    (5, 2, 4): (Fr(10650, 63407), Fr(31950, 63407)),
    (2, 1, 2): (Fr(1, 9), Fr(1, 3)),
    (40, 1, 1): (Fr(130, 137), Fr(390, 137)),
}
m1 = True
rows = []
for (p, q, r), (a, triple) in points.items():
    got = alpha3(Fr(p), Fr(q), Fr(r))
    m1 &= got == a and 3 * got == triple
    rows.append(f"({p},{q},{r})->{got}")
ok("M1", m1, "largest single-parent total variation: " + ", ".join(rows))

# ---------- M2. closed form on the verified range, and not beyond ----------
x = sp.symbols("x", positive=True)
formula = x ** 2 * (x - 1) * (x + 33) / ((x ** 3 + 33) * (x ** 2 + x + 32))
range_ok = True
for p in (Fr(5, 2), Fr(3), Fr(7, 2), Fr(15, 4), Fr(4), Fr(5)):
    brute = alpha3(p, Fr(1), Fr(2))
    closed_v = closed(p)
    form = sp.Rational(formula.subs(x, sp.Rational(p)))
    range_ok &= brute == closed_v == Fr(form.p, form.q)
beyond = True
for p in (Fr(8), Fr(20)):
    beyond &= alpha3(p, Fr(1), Fr(2)) > closed(p)
ok("M2", range_ok and beyond,
   "on p=5/2..5 the maximizer is three equals with one antipodal flip and matches the closed form; at p=8 and 20 a different pair is larger")

# ---------- M3. the threshold is the smallest positive root of the quintic ----------
num, den = sp.fraction(sp.together(formula))
diff = sp.factor(sp.expand(3 * num - den))
quoted = x ** 5 - 2 * x ** 4 - 64 * x ** 3 + 132 * x ** 2 + 33 * x + 1056
roots = [r for r in sp.real_roots(quoted) if r > 0]
pstar = roots[0]
pstar_n = sp.N(pstar, 20)
below = alpha3(Fr(15, 4), Fr(1), Fr(2))
above = alpha3(Fr(94, 25), Fr(1), Fr(2))
crosses = below * 3 < 1 < above * 3
on_form = sp.simplify(quoted.subs(x, pstar)) == 0 and sp.simplify((3 * formula - 1).subs(x, pstar)) == 0
ok("M3", crosses and on_form and abs(pstar_n - sp.Float("3.756359818320370")) < sp.Float("1e-12"),
   f"3 alpha_3 crosses 1 between 15/4 ({3 * below}) and 94/25 ({3 * above}); p* = {pstar_n}")

# ---------- M4. the strong-coupling limit of the closed form, and the values ----------
# The antipodal-flip formula tends to 0. The true maximum tends to 1: one parent can
# change a nearly deterministic child, so 3 alpha_3 tends to 3 and no per-parent bound stays below 1.
limit_form = sp.limit(formula, x, sp.oo)
vals = {p: alpha3(Fr(p), Fr(1), Fr(2)) for p in (100, 4165, 10 ** 4)}
m4 = limit_form == 0 and abs(float(vals[100]) - 0.9771) < 5e-5
m4 = m4 and abs(float(vals[4165]) - 0.99952) < 5e-6 and abs(float(vals[10 ** 4]) - 0.99980) < 5e-6
m4 = m4 and 3 * vals[10 ** 4] > Fr(299, 100)
ok("M4", m4,
   f"closed form -> 0, but the true alpha is {float(vals[100]):.5f}, {float(vals[4165]):.5f}, {float(vals[10**4]):.5f} at p=100, 4165, 10^4, so 3 alpha -> 3")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - on (p,1,2) the single-parent influence crosses 1/3 at p* = 3.7563598183, and 3 alpha_3 tends to 3, so the Dobrushin bound cannot prove uniqueness at strong coupling.")
print("HIT: confirmed - alpha_3(p) = p^2(p-1)(p+33)/((p^3+33)(p^2+p+32)) on p in [5/2, 5], 3 alpha_3 = 1 at the smallest positive root p* = 3.7563598183 of x^5 - 2x^4 - 64x^3 + 132x^2 + 33x + 1056, and 3 alpha_3 -> 3, so no sharpening of this per-parent bound reaches the ordered phase.")
