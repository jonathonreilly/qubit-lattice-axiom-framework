#!/usr/bin/env python3
"""r55b_num.py -- REVIEW55_BFTB (reviewer claude-opus-5-5). Criteria: checks/r55b_num_criteria.md (written first).
Exact rational arithmetic only (fractions.Fraction, ints). No floats in any verdict."""
from fractions import Fraction as F

res = []
def rec(tag, ok, note):
    res.append(ok); print(f"{tag}: {'PASS' if ok else 'FAIL'}  {note}")

# N1: x = 3^{-9/4}; x^4 = 3^{-9}. Bracket x by rationals a <= x <= b  <=>  a^4 <= 3^{-9} <= b^4.
t = F(1, 3 ** 9)
def in_bracket(a, b):
    return a ** 4 <= t <= b ** 4
a, b = F(8442, 100000), F(8443, 100000)
br = in_bracket(a, b)
Kf_lo, Kf_hi = 8 / (1 - a), 8 / (1 - b)       # K_f = 8/(1-x) increasing in x
ok1 = br and F(8737, 1000) <= Kf_lo and Kf_hi <= F(874, 100)
printed = F(8434, 100000)
printed_in = (F(8433, 100000) ** 4 <= t <= F(8435, 100000) ** 4)
rec("N1", ok1, f"x=3^(-9/4) in [0.08442,0.08443]: {br}; K_f in [{float(Kf_lo):.6f},{float(Kf_hi):.6f}] (display only); "
             f"8.737 <= K_f <= 8.74: {ok1}. Printed intermediate 0.08434 within [0.08433,0.08435] of x: {printed_in} (recorded)")

# N2: 1 + 8*(27/26) = 121/13 <= 9.31
v = 1 + 8 * F(27, 26)
rec("N2", v == F(121, 13) and v <= F(931, 100), f"1 + 8*27/26 = {v} = {float(v):.6f} <= 9.31")

# N3: 2M_n/n = 4(4n+1)/n <= 20 for n = 3^k; 1D Green identity on Z_M
ok3 = all(F(4 * (4 * 3 ** k + 1), 3 ** k) <= 20 for k in range(1, 13))
ok3b = True
for M in (4, 6, 8, 10, 12, 50):
    g = lambda s: F((s - F(M, 2)) ** 2, 2 * M)
    gp = lambda s: g(s % M)
    for s in range(M):
        lap = -(gp(s + 1) - 2 * gp(s) + gp(s - 1))
        target = (1 if s == 0 else 0) - F(1, M)
        ok3b = ok3b and (lap == target)
    ok3b = ok3b and (2 * (g(0) - g(F(M, 2))) == F(M, 4))
rec("N3", ok3 and ok3b, f"2M_n/n <= 20 for n=3^k, k=1..12: {ok3}; -Lap g = delta_0 - 1/M and 2(g(0)-g(M/2)) = M/4: {ok3b}")
print("VERDICT r55b_num:", "ALL PASS" if all(res) else "NOT ALL PASS")
