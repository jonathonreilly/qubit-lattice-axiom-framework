#!/usr/bin/env python3
"""Exact-rational checks for the D-form and spin-boundary identities."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/boundary_form_verifier.py',)
from fractions import Fraction
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "D_RESIDUE_POLYNOMIALS.json").read_text())
rows = data["rows"]
remainders = data["weighted_laplacian_remainder"]

def coeff(row, name):
    return tuple(Fraction(x) for x in row[name]["quadratic_k2_k_const"])

weights = []
for r, row in enumerate(rows):
    A, B, C0 = coeff(row, "right")
    assert A == 9 and abs(B) <= 21
    f = lambda k: (A - 1) * k * k + B * k + C0
    assert f(-3) >= 0 and f(3) >= 0
    # f(k+1)-f(k) is positive for k>=3; f(k-1)-f(k) is
    # positive for k<=-3. Thus these endpoint checks cover both tails.
    assert 2 * (A - 1) * 3 + (A - 1) + B > 0
    assert 2 * (A - 1) * 3 - (A - 1) - B > 0
    # The exact quadratic has its minimum at the rational vertex. Check
    # the nearest integers around that vertex for global nonnegativity.
    vertex = -B / (2 * A)
    base = vertex.numerator // vertex.denominator
    assert min(A*k*k + B*k + C0 for k in (base-1, base, base+1, base+2)) >= 0
    weights.append((A, B, C0))

alpha = [Fraction(x["remainder_alpha_k_plus_beta"][0]) for x in remainders]
beta = [Fraction(x["remainder_alpha_k_plus_beta"][1]) for x in remainders]
assert sum(alpha) == 0 and sum(beta) == 3
assert max(map(abs, alpha)) <= 3 and max(map(abs, beta)) <= 3

# P_15 path gap lambda=2(1-cos(pi/15)) > 1/25 follows from
# 2(1-cos x) >= x^2 - x^4/12, 3.14 < pi, and pi/15 < 1/4.
assert Fraction(157, 750)**2 - Fraction(1, 4**4 * 12) > Fraction(1, 25)
# For |k|>=200, k^2/25 - 3(|k|+1) >= k^2/50.
def g(k):
    return Fraction(k*k, 50) - 3*(k+1)
assert g(200) > 0 and 200 > 75  # g is increasing for k>=200.
# Young's inequality leaves at most 13500(1+1/k)^2 <= 13650 times |u|^2.
assert 13500 * Fraction(201, 200)**2 < 13650

# Boundary d_(5S-4)=S^2 in each residue class, checked over many spins;
# the three closed forms below are exactly the relevant table rows.
def right_value(n):
    r, k = n % 15, n // 15
    A, B, C0 = weights[r]
    return A*k*k + B*k + C0

for S in range(1, 10001):
    n = 5*S - 4
    assert right_value(n) == S*S, (S, n, right_value(n))
    m, s = divmod(S, 3)
    if s == 0:
        assert n % 15 == 11 and n // 15 == m - 1
    elif s == 1:
        assert n % 15 == 1 and n // 15 == m
    else:
        assert n % 15 == 6 and n // 15 == m

print("PASS exact rational residue, form-bound inputs, and boundary identities; S=1..10000")
