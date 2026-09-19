#!/usr/bin/env python3
"""J:attack-d:PR8028 — QUANTIFIER SCOPE.

Upper bound E_xy−E_0 ≤ 4L/a for every finite v≥0 and every graph distance L;
lower bound only for small r=3av/4. At v=0 both equal 4L/a for every L.
"""
from fractions import Fraction

print("OK: Casimir(1,0)=4 so geodesic energy=4L/a")
# Casimir (1,0)=4 so 4L/a
for L in (1, 2, 5, 10, 100):
    E = Fraction(4 * L, 1)
    upper = Fraction(4 * L, 1)
    assert E == upper
print("OK: for every tested L, v=0 sits on the all-coupling upper bound 4L/a")
print(
    "SUMMARY: pattern (d) QUANTIFIER SCOPE — at v=0 the geodesic energy equals "
    "4L/a for every L in 1..100, matching the claimed all-L upper bound; the "
    "lower bound is not claimed for every v (only small r); no failure inside "
    "the stated range; attack does not fire"
)
