#!/usr/bin/env python3
"""J:falsifier:PR8172 — independent check of the T2 healing polynomial.

Falsifier: a negative coefficient in 18(D+1)^3 − (D+1)(6D+5)(6D+4)/2,
or the polynomial negative for some integer D≥0.
"""
import sympy as sp

D = sp.symbols("D", integer=True, nonnegative=True)
expr = 18 * (D + 1) ** 3 - (D + 1) * (6 * D + 5) * (6 * D + 4) / 2
poly = sp.Poly(sp.expand(expr), D)
coeffs = poly.all_coeffs()
print("polynomial:", sp.expand(expr))
print("coeffs (high to low):", coeffs)
hits = []
for i, c in enumerate(coeffs):
    if c < 0:
        hits.append(f"negative coefficient {c} at degree {poly.degree()-i}")
for n in range(0, 40):
    val = expr.subs(D, n)
    if val < 0:
        hits.append(f"poly({n})={val} < 0")
        break
# also 18(D+1)^3 bound positivity for D>=0
if hits:
    for h in hits:
        print("HIT:", h)
    print("SUMMARY: healing-polynomial falsifier FIRED:", "; ".join(hits))
else:
    print(
        "SUMMARY: healing-polynomial falsifier did not fire: "
        f"{sp.expand(expr)} has all nonnegative coefficients and is "
        "nonnegative at D=0..39"
    )
