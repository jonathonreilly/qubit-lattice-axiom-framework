#!/usr/bin/env python3
"""Independent referee for ordering-threshold-down a4.

The deviation line on (p, 1, 2) and the fork-free chain sum that diverges
for every p <= 57. Does not import the attempt.
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def d1(p: int) -> F:
    return F(33, p**3 + 33)


def d2(p: int) -> F:
    return F(p + 32, p * p + p + 32)


def d3(p: int) -> F:
    return F(2 * p + 11, p * p + 2 * p + 11)


p = sp.symbols("p", positive=True)
D1 = sp.Rational(33) / (p**3 + 33)
D2 = (p + 32) / (p**2 + p + 32)
D3 = (2 * p + 11) / (p**2 + 2 * p + 11)
n21 = sp.factor(sp.numer(sp.together(D2 - D1)))
n31 = sp.factor(sp.numer(sp.together(D3 - D1)))
n23 = sp.factor(sp.numer(sp.together(D2 - D3)))
den_ok = all(sp.denom(sp.together(expr)) > 0 for expr in (D2 - D1, D3 - D1, D2 - D3))
# 2p^2+11p-33 > 0 for every integer p >= 3: its positive root is below 3.
quad = 2 * 3**2 + 11 * 3 - 33
small_ok = all(d1(q) <= max(d2(q), d3(q)) for q in (1, 2))
check(
    "D1 domination",
    den_ok and n21 == p**2 * (p - 1) * (p + 33) and n31 == p**2 * (2 * p**2 + 11 * p - 33)
    and quad > 0 and small_ok,
    "d2-d1 and d3-d1 have nonnegative numerators for integer p >= 1, so d1 <= max(d2, d3)",
)
threshold = all(max(d2(q), d3(q)) >= F(1, 27) for q in range(1, 58)) and all(
    max(d2(q), d3(q)) < F(1, 27) for q in range(58, 200)
)
# For p >= 21, eps2 = d3, and d3 < 1/27 iff p^2 - 52p - 286 > 0.
# That quadratic is positive at p = 58 and increasing thereafter.
disc_gap = 58**2 - 52 * 58 - 286
check(
    "D2 threshold",
    sp.simplify(n23 - p**2 * (21 - p)) == 0 and d2(21) == d3(21)
    and d3(57) == F(125, 3374) and d3(58) == F(127, 3491)
    and d3(57) > F(1, 27) >= d3(58) and d2(57) < d3(57) and d2(58) < d3(58)
    and threshold and disc_gap > 0 and (59**2 - 52 * 59 - 286) > disc_gap,
    "eps2 = max(d2, d3) drops through 1/27 between p = 57 and p = 58, and stays below afterwards",
)

patterns = list(itertools.product((1, 2, 3), repeat=3))
counts = [sum(1 for d in patterns if sum(d[k] == k + 1 for k in range(3)) == b) for b in range(4)]
r = sp.symbols("r")
total = sum(r ** sum(d[k] == k + 1 for k in range(3)) for d in patterns)
check(
    "G1 pattern weights",
    counts == [8, 12, 6, 1] and sp.expand(total - (2 + r) ** 3) == 0,
    "the 27 patterns split 8,12,6,1 by bad-pair count, and the generating function is (2+r)^3",
)


def block_count(m: int) -> int:
    return sum((math.factorial(m) // (math.factorial(a) ** 2 * math.factorial(m - 2 * a))) ** 3 for a in range(m // 2 + 1))


def brute_blocks(m: int) -> int:
    found = 0
    for seq in itertools.product(range(27), repeat=m):
        tally = [[0, 0, 0] for _ in range(3)]
        for code in seq:
            move = (code // 9 + 1, (code // 3) % 3 + 1, code % 3 + 1)
            for k in range(3):
                tally[k][move[k] - 1] += 1
        if all(tally[k][0] == tally[k][1] == tally[0][0] for k in range(3)):
            found += 1
    return found


small_blocks = all(block_count(m) == brute_blocks(m) for m in (1, 2, 3))
bound_ok = True
for m in (3, 6, 9, 12, 30):
    a = m // 3
    central = math.factorial(m) // math.factorial(a) ** 3
    # (a,a,a) is the unique maximal trinomial coefficient, and there are C(m+2,2) of them.
    compositions = (m + 1) * (m + 2) // 2
    bound_ok = bound_ok and central * compositions >= 3**m
    bound_ok = bound_ok and 8 * (m + 1) ** 3 >= (m + 2) ** 3
    bound_ok = bound_ok and block_count(m) >= central**3
    bound_ok = bound_ok and central**3 >= 27**m // (m + 1) ** 6
check(
    "G2 blocks",
    small_blocks and bound_ok,
    "block counts match brute force at m=1,2,3, and the balanced term is at least 27^m/(m+1)^6",
)

moves = {1: (-1, 0), 2: (0, -1), 3: (0, 0)}
dl = {d: moves[d][0] - moves[d][1] for d in moves}
check(
    "G3 separation",
    dl == {1: -1, 2: 1, 3: 0},
    "each move changes ell = X1-X2 by -1, +1 or 0, so a balanced block returns every pole's ell",
)

# p = 57: 27 eps2 = 3375/3374. Find the least m in 3Z with (3375/3374)^m > (m+1)^6.
lhs = 27 * d3(57)
found = None
guess = 3
log_ratio = math.log(float(lhs))
while guess < 1_000_000:
    if 6 * math.log(guess + 1) < guess * log_ratio * (1 - 1e-12):
        found = guess
        break
    guess += 3
exact = found is not None and lhs.numerator**found > lhs.denominator**found * (found + 1) ** 6
# The float start can be early. Step back while the exact inequality still holds, then check the previous multiple fails.
if exact:
    while found > 3 and lhs.numerator ** (found - 3) > lhs.denominator ** (found - 3) * (found - 2) ** 6:
        found -= 3
    previous_fails = lhs.numerator ** (found - 3) <= lhs.denominator ** (found - 3) * (found - 2) ** 6
else:
    previous_fails = False
check(
    "G4 divergence",
    lhs == F(3375, 3374) and exact and previous_fails and found == 251802,
    "at p=57, 27 eps2 = 3375/3374 and m=%s is the least multiple of 3 with 3375^m > 3374^m (m+1)^6" % found,
)

# Explicit prefix: two coincident-pole refinements, then n=6 gap steps. Poles stay distinct and the gaps reach 7.
def sub(v, move):
    basis = {1: (1, 0, 0), 2: (0, 1, 0), 3: (0, 0, 1)}
    e = basis[move]
    return tuple(v[i] - e[i] for i in range(3))


poles = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
poles = [sub(poles[k], (2, 1, 1)[k]) for k in range(3)]
poles = [sub(poles[k], (3, 3, 2)[k]) for k in range(3)]
distinct = len(set(poles)) == 3
for _ in range(6):
    poles = [sub(poles[k], (2, 1, 3)[k]) for k in range(3)]
    distinct = distinct and len(set(poles)) == 3
ells = sorted(v[0] - v[1] for v in poles)
# One balanced block, a=1, m=3: each charge takes moves 1,2,3 in that order. Relative positions return.
origin = [tuple(poles[k][i] - poles[2][i] for i in range(3)) for k in range(3)]
for move in ((1, 1, 1), (2, 2, 2), (3, 3, 3)):
    poles = [sub(poles[k], move[k]) for k in range(3)]
    distinct = distinct and len(set(poles)) == 3
restored = [tuple(poles[k][i] - poles[2][i] for i in range(3)) for k in range(3)] == origin
# Budget of the glued chain: prefix R=2+n, B=n; blocks and the 2n-step suffix have B=R; the seed step has B-R=2.
n = 6
prefix_R, prefix_B = 2 + n, n
suffix_B = 2 * n
seed_extra = 2
budget = prefix_B + suffix_B + seed_extra == prefix_R + suffix_B
check(
    "G5 prefix",
    distinct and ells[1] - ells[0] >= 7 and ells[2] - ells[1] >= 7 and restored and budget,
    "the separating prefix opens ell-gaps of at least 7, a balanced block restores them, and the chain budget has B=R",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed no-go. On (p, 1, 2), eps2 = max(d2, d3) is at least 1/27 for every p <= 57 and drops below it at p = 58. "
    "Any history sum that still contains the fork-free separated-pole chains is then infinite, because those chains grow like 27^R "
    "up to a (m+1)^{6/m} factor that can be brought below 27 eps2. No threshold below 58 is obtained from this grammar. "
    "Whether the chains are realized by configurations is not decided.",
    flush=True,
)
print(
    "HIT: confirmed - the refinement-history route cannot prove a threshold below 58, because its fork-free chains diverge for every p <= 57",
    flush=True,
)
