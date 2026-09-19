#!/usr/bin/env python3
"""ordering-threshold-down, attempt a4 (w-jonathonsmac4f50-jc31e): the checks behind ATTEMPT.md.

Objects: block 30 (PR #8174) two-level automaton eta', deviations d1, d2, d3 on (p, 1, 2): d1 = 33/(p^3 + 33), d2 = (p + 32)/(p^2 + p + 32),
d3 = (2p + 11)/(p^2 + 2p + 11) (closed forms as used by the round-1 attempts); the round-1 refinement-history grammar G (attempt
beyond-the-union-bound a3): per refinement a move pattern d in {1,2,3}^3, bad pairs b(d) = #{k : d_k = k}, histories weighted by the
physical cylinder weight eps1^{F+1} eps2^B and realizable only when R <= F + B (the potential).

 D1  on (p, 1, 2): d2 - d1 has the sign of p^2 (p - 1)(p + 33) and d3 - d1 that of p^2 (2p^2 + 11p - 33): d1 <= max(d2, d3) for every p >= 1
     (block 30's T1(a), false for general weights, holds on this line)
 D2  eps2 = max(d2, d3): d2 = d3 exactly at p = 21 (d2 - d3 has the sign of p^2 (21 - p)); eps2 < 1/27 iff p >= 58; the table of eps2
 G1  per refinement sum_{d in {1,2,3}^3} r^{b(d)} = (2 + r)^3 (27 at r = 1): the pattern counts 8, 12, 6, 1 by b = 0..3
 G2  the block count M_m = #{m-refinement move sequences with, for each charge k, as many moves 1 as moves 2, and exactly m bad pairs}
     (exact for m <= 60) and the bound M_m >= multinomial(m; m/3, m/3, m/3)^3 >= 27^m/(m + 1)^6 (m in 3Z)
 G3  pole separation: a move changes l = X1 - X2 by -1, +1, 0 (d = 1, 2, 3); a block with, per charge, equal numbers of moves 1 and 2
     returns every pole's l to its start, and within it the l-gaps move by at most 2 per step
 G4  the weighted chain sum: along concatenated blocks, sum eps2^B >= (27 eps2 (m + 1)^{-6/m})^R -> infinity whenever 27 eps2 > (m+1)^{6/m};
     at the p = 57 value eps2 = 125/3374 (27 eps2 = 3375/3374) the smallest such m in 3Z is found exactly
"""
import math
import sys
import time
from fractions import Fraction as F
from itertools import product

import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


def d1(p):
    return F(33, p ** 3 + 33)


def d2(p):
    return F(p + 32, p * p + p + 32)


def d3(p):
    return F(2 * p + 11, p * p + 2 * p + 11)


def section_D():
    print("=" * 110)
    print("D  the deviations on (p, 1, 2)")
    p = sp.Symbol("p", positive=True)
    D1 = sp.Rational(33) / (p ** 3 + 33)
    D2 = (p + 32) / (p ** 2 + p + 32)
    D3 = (2 * p + 11) / (p ** 2 + 2 * p + 11)
    n21 = sp.factor(sp.numer(sp.together(D2 - D1)))
    n31 = sp.factor(sp.numer(sp.together(D3 - D1)))
    ok = sp.simplify(n21 - p ** 2 * (p - 1) * (p + 33)) == 0 and sp.simplify(n31 - p ** 2 * (2 * p ** 2 + 11 * p - 33)) == 0
    ok &= all(sp.denom(sp.together(x)) != 0 for x in (D2 - D1, D3 - D1))
    ok &= all(max(d2(q), d3(q)) >= d1(q) for q in range(1, 400))
    check("D1", ok, f"numerators: d2 - d1 -> {n21}, d3 - d1 -> {n31} (denominators positive): d1 <= d2 for p >= 1, d1 <= d3 for "
          f"p >= (-11 + sqrt 385)/4 = 2.155; so d1 <= max(d2, d3) on (p, 1, 2) for every p >= 1 (exact also at p = 1..399)")
    n23 = sp.factor(sp.numer(sp.together(D2 - D3)))
    ok2 = sp.simplify(n23 - p ** 2 * (21 - p)) == 0
    ok2 &= d3(57) > F(1, 27) >= d3(58) and d2(58) < d3(58) and d2(57) < d3(57)
    ok2 &= all(max(d2(q), d3(q)) >= F(1, 27) for q in range(1, 58)) and all(max(d2(q), d3(q)) < F(1, 27) for q in range(58, 400))
    tab = ", ".join(f"eps2({q}) = {float(max(d2(q), d3(q))):.4f}" for q in (11, 13, 14, 21, 30, 40, 57, 58, 84))
    check("D2", ok2, f"d2 - d3 has numerator {n23}: d2 > d3 below p = 21, d3 > d2 above; eps2 = max(d2, d3) < 1/27 exactly for p >= 58 "
          f"(d3(57) = {d3(57)} > 1/27 >= d3(58) = {d3(58)}); {tab}")


def section_G():
    print("=" * 110)
    print("G  the refinement-history grammar along fork-free chains with separated poles")
    r = sp.Symbol("r")
    tot = sum(r ** sum(1 for k in range(3) if d[k] == k + 1) for d in product((1, 2, 3), repeat=3))
    counts = [sum(1 for d in product((1, 2, 3), repeat=3) if sum(1 for k in range(3) if d[k] == k + 1) == b) for b in range(4)]
    ok1 = sp.expand(tot - (2 + r) ** 3) == 0 and counts == [8, 12, 6, 1]
    check("G1", ok1, f"sum over the 27 move patterns of r^b = (2 + r)^3; patterns with b = 0, 1, 2, 3 bad pairs: {counts} (tilted at sigma = eps2 "
          "every pattern has weight eps2 and b has mean exactly 1)")

    # G2: exact block counts: per charge a moves 1, a moves 2, m - 2a moves 3, the same a for the three charges (then B = a + a + (m - 2a) = m)
    def M(m):
        return sum((math.factorial(m) // (math.factorial(a) ** 2 * math.factorial(m - 2 * a))) ** 3 for a in range(m // 2 + 1))

    def brute(m):
        n = 0
        for seq in product(range(27), repeat=m):
            c = [[0, 0, 0] for _ in range(3)]
            bad = 0
            for sq in seq:
                d = (sq // 9 + 1, (sq // 3) % 3 + 1, sq % 3 + 1)
                for k in range(3):
                    c[k][d[k] - 1] += 1
                    bad += (d[k] == k + 1)
            if all(c[k][0] == c[k][1] == c[0][0] for k in range(3)):
                n += 1
                assert bad == m
        return n
    ok2 = all(M(m) == brute(m) for m in (1, 2, 3))
    rows = []
    for m in (3, 6, 9, 12, 30, 60):
        Mm = M(m)
        bal = (math.factorial(m) // math.factorial(m // 3) ** 3) ** 3
        lb = F(27 ** m, (m + 1) ** 6)
        ok2 &= Mm >= bal >= lb
        rows.append(f"m = {m}: M_m = {Mm if m <= 6 else f'{Mm:.4e}'}, (1/m) log M_m = {math.log(Mm) / m:.4f}")
    mm = sp.Symbol("m", positive=True, integer=True)
    check("G2", ok2, "the exact block count (formula = brute force at m = 1, 2, 3) dominates the balanced term multinomial(m; m/3, m/3, m/3)^3 "
          f">= 27^m/(m+1)^6: " + "; ".join(rows) + f" (log 27 = {math.log(27):.4f})")
    # G3: pole separation
    moves = {1: (-1, 0), 2: (0, -1), 3: (0, 0)}           # in-plane change of (X1, X2) for the predecessor step X -> X - e_d
    dl = {d: moves[d][0] - moves[d][1] for d in moves}
    ok3 = dl == {1: -1, 2: 1, 3: 0}
    check("G3", ok3, "the predecessor step X -> X - e_d changes the in-plane coordinates (X1, X2) by (-1, 0), (0, -1), (0, 0), so l = X1 - X2 changes by "
          "-1, +1, 0: in a block with, per charge, as many moves 1 as moves 2 every pole's l returns to its start, and pairwise l-gaps move by at "
          "most 2 per step; poles whose l-gaps start >= 2m + 1 stay pairwise distinct through the block")
    # G4: divergence of the physical-weight chain sum for eps2 > 1/27
    e57 = max(d2(57), d3(57))
    lhs = 27 * e57
    m_found = None
    m = 3
    # find the smallest m in 3Z with (m + 1)^6 < (27 eps2)^m, i.e. 6 log(m+1) < m log(27 eps2) (checked exactly by integer powers at the found m)
    lg = math.log(float(lhs))
    while True:
        if 6 * math.log(m + 1) < m * lg * (1 - 1e-9):
            m_found = m
            break
        m += 3
    exact_ok = lhs.numerator ** m_found > lhs.denominator ** m_found * (m_found + 1) ** 6     # exact integers (about 890000 digits)
    check("G4", bool(exact_ok) and lhs > 1, f"along chains built from such blocks (B = R exactly, F = 0, poles pairwise distinct), sum eps2^B >= "
          f"C (27 eps2)^R (m + 1)^(-6R/m), infinite as soon as 27 eps2 > (m + 1)^(6/m); at p = 57, 27 eps2 = {lhs} and m = {m_found} suffices "
          f"(checked with exact integers: 3375^m > 3374^m (m + 1)^6); for every eps2 > 1/27 some m does, since (m + 1)^(6/m) -> 1")


def section_chain():
    print("=" * 110)
    print("G5  an explicit chain of the family: root -> separation -> gaps -> blocks -> merge -> seed (m = 3, five random blocks)")
    import random
    rng = random.Random(8174)
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def sub(v, d):
        return tuple(v[i] - E[d - 1][i] for i in range(3))
    m = 3
    n = 2 * m
    poles = [(0, 0, 0)] * 3
    log = []

    def step(mv):
        nonlocal poles
        b = sum(1 for k in range(3) if mv[k] == k + 1)
        log.append((tuple(poles), tuple(mv), b))
        poles = [sub(poles[k], mv[k]) for k in range(3)]
    ok = True
    # ref 1: the root's coincident pole x, processed with winning pair {1, 2}: excuses (x - e2, x - e1, x - e1)
    step((2, 1, 1))
    # ref 2: charge 1 alone at x - e2 (move 3); charges 2, 3 coincident at x - e1, processed with winning pair {2, 3}: moves (3, 2)
    ok &= poles[1] == poles[2] and poles[0] != poles[1]
    step((3, 3, 2))
    ok &= len(set(poles)) == 3
    ell = lambda v: v[0] - v[1]
    # the gap-making prefix (2, 1, 3)^n: one bad pair per refinement
    for _ in range(n):
        step((2, 1, 3))
        ok &= len(set(poles)) == 3
    ls = sorted(ell(v) for v in poles)
    gaps_ok = ls[1] - ls[0] >= 2 * m + 1 and ls[2] - ls[1] >= 2 * m + 1
    rel0 = [tuple(poles[k][i] - poles[2][i] for i in range(3)) for k in range(3)]
    # middle: blocks with, per charge, a moves 1, a moves 2, m - 2a moves 3 (the same a for all charges), random order
    for _ in range(5):
        a = rng.randrange(0, m // 2 + 1)
        cols = []
        for k in range(3):
            c = [1] * a + [2] * a + [3] * (m - 2 * a)
            rng.shuffle(c)
            cols.append(c)
        for i in range(m):
            step((cols[0][i], cols[1][i], cols[2][i]))
            ok &= len(set(poles)) == 3
        rel = [tuple(poles[k][i] - poles[2][i] for i in range(3)) for k in range(3)]
        ok &= rel == rel0
    # merge: DFS for a suffix taking the poles to (u + e1, u + e2, u + e3), pairwise distinct on the way
    base = poles[2]
    tgt_in = [(-n, -1 - n), (-1 - n, -n), (-1 - n, -1 - n)]          # in-plane targets relative to the start of the merge (see ATTEMPT.md)
    rel_in = [(poles[k][0] - base[0], poles[k][1] - base[1]) for k in range(3)]
    shift_in = (rel_in[2][0] + 1, rel_in[2][1] + 1)                   # P3 sits at (-1, -1) in the prefix frame
    tgt = [(t[0] - (-1) + rel_in[2][0] - 0 + 0, t[1] - (-1) + rel_in[2][1]) for t in tgt_in]
    tgt = [(t[0] + base[0], t[1] + base[1]) for t in tgt]
    S = 2 * n
    moves_in = {1: (-1, 0), 2: (0, -1), 3: (0, 0)}
    start = [(v[0], v[1]) for v in poles]
    sol = []

    def feasible(pos, rem):
        for k in range(3):
            dx, dy = pos[k][0] - tgt[k][0], pos[k][1] - tgt[k][1]
            if dx < 0 or dy < 0 or dx + dy > rem:
                return False
        return True

    def dfs(pos, rem):
        if rem == 0:
            return pos == tgt
        for mv in product((1, 2, 3), repeat=3):
            new = [(pos[k][0] + moves_in[mv[k]][0], pos[k][1] + moves_in[mv[k]][1]) for k in range(3)]
            if len(set(new)) < 3 or not feasible(new, rem - 1):
                continue
            sol.append(mv)
            if dfs(new, rem - 1):
                return True
            sol.pop()
        return False
    found = feasible(start, S) and dfs(start, S)
    ok &= found
    for mv in sol:
        step(mv)
        ok &= len(set(poles)) == 3
    # the final refinement: poles at u + e1, u + e2, u + e3, moves (1, 2, 3), every terminal equal to u
    u = sub(poles[0], 1)
    ok &= sub(poles[1], 2) == u and sub(poles[2], 3) == u
    step((1, 2, 3))
    ok &= poles[0] == poles[1] == poles[2] == u
    R = len(log)
    B = sum(b for _, _, b in log)
    check("G5", ok and gaps_ok and B == R, f"explicit chain (m = 3, gaps {ls[1] - ls[0]}, {ls[2] - ls[1]} >= 7 after the prefix, five random blocks, a {len(sol)}-step "
          f"merge found by search): the root's coincident pole makes the processed pattern (2, 1, 1), the coincident charges 2, 3 the processed pattern "
          f"(3, 2), poles pairwise distinct from the second refinement to the last, relative positions restored after every block, the last "
          f"refinement (1, 2, 3) sends all three terminals to one site u (the seed), R = {R} refinements, B = {B} bad pairs (R <= F + B with F = 0)")


def main():
    section_D()
    section_G()
    section_chain()
    print("=" * 110)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} (check failures: {FAILS})")
        return 0
    core = ("no threshold below 58 is proved; route (ii) and every re-summation of the refinement-history count fail at eps2 = 1/27: the "
            "grammar contains, for every R, the fork-free chains of R refinements with pairwise distinct poles and exactly R bad pairs "
            "(concatenated blocks in which each charge makes as many moves 1 as moves 2), at least 27^R (m+1)^(-6R/m) of them, each of physical "
            "weight eps1 eps2^R and satisfying the potential constraint R <= F + B; so the physical-weight sum over any family containing them "
            "diverges whenever 27 eps2 > 1, i.e. for every p <= 57 on (p, 1, 2); any thinning that acts only on forks or on coincident poles "
            "(the diamond-free lift, pole-configuration typing) keeps these chains. Also: d1 <= max(d2, d3) on (p, 1, 2) for every p >= 1 "
            "(numerators p^2 (p-1)(p+33), p^2 (2p^2 + 11p - 33)); d2 = d3 exactly at p = 21")
    print("SUMMARY: ROUTE FAILS AT (ii) (every history grammar containing the fork-free separated-pole chains is capped at eps2 < 1/27); " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
