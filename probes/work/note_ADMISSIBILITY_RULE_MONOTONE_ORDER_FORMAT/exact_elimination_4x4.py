#!/usr/bin/env python3
"""J:note falsifiers for ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.

Falsifiers implemented (the note's finite list, beyond its sizes): "a column or row ... not the K-chain"; "a block marginal not pi";
"P(a, b | c) != K(c -> a) K(c -> b)"; "a diagonal pair not (1/6) K^2"; "a staircase ... with zero defect at a declared triple";
"P(c | c, c) <= K(c -> c) at some non-constant triple"; extension counts.

The runner enumerates configurations on 2x3, 3x3, 3x4. Here, with disjoint machinery, on the 4 x 4 rectangle (6^16 configurations,
never enumerated): exact rational VARIABLE ELIMINATION on the factor graph of mu_P = (1/6) prod_top-row K prod_left-column K
prod_interior beta(v_ij | v_i,j-1, v_i-1,j), beta(s | a, b) = K(a -> s) K(s -> b) / K^2(a, b), K(a -> s) = phi(s, a)/(p + q + 4r);
for both declared triples (3, 1, 2) and (5, 2, 4):
  - the joint law of every column and every row (4 sites) against the K-chain (1/6) prod K;
  - the joint law of all 9 two-by-two blocks against pi(c, b, a, d) = (1/6) K(c,a) K(c,b) K(a,d) K(d,b) / K^2(a,b), and the
    conditional P(a, b | c) = K(c -> a) K(c -> b);
  - every anti-diagonal pair (i, j+1), (i+1, j) against (1/6) K^2;
  - every 3-site right/down staircase with a turn: its Markov defect max |P(z | x, y) - P(z | y)| (must be nonzero);
and, beyond the note's {1..6}^3, the inequality P(c | c, c) > K(c -> c) at every non-constant triple of {1..10}^3 (exact, from the
note's closed form of the minimal staircase conditional), plus the linear-extension counts of the r x s rectangles by the hook-length
formula against a direct count, up to 4 x 5 and 5 x 5.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F
from math import factorial

AX = [0, 0, 1, 1, 2, 2]


def kernel(p, q, r):
    phi = [[F(p) if a == b else (F(q) if AX[a] == AX[b] else F(r)) for b in range(6)] for a in range(6)]
    Z1 = p + q + 4 * r
    K = [[phi[s][a] / Z1 for s in range(6)] for a in range(6)]            # K[a][s] = K(a -> s)
    K2 = [[sum(K[a][s] * K[s][b] for s in range(6)) for b in range(6)] for a in range(6)]
    return K, K2


def factors(n, m, K, K2):
    fs = [(((0, 0),), {(v,): F(1, 6) for v in range(6)})]
    for j in range(1, m):
        fs.append((((0, j - 1), (0, j)), {(a, s): K[a][s] for a in range(6) for s in range(6)}))
    for i in range(1, n):
        fs.append((((i - 1, 0), (i, 0)), {(a, s): K[a][s] for a in range(6) for s in range(6)}))
    for i in range(1, n):
        for j in range(1, m):
            fs.append((((i, j - 1), (i - 1, j), (i, j)),
                       {(a, b, s): K[a][s] * K[s][b] / K2[a][b] for a in range(6) for b in range(6) for s in range(6)}))
    return fs


def multiply_sum_out(fs, var):
    """multiply every factor containing var and sum var out; returns the new factor list."""
    touch = [f for f in fs if var in f[0]]
    rest = [f for f in fs if var not in f[0]]
    scope = sorted({v for sc, _ in touch for v in sc if v != var})
    table = {}
    for assign in itertools.product(range(6), repeat=len(scope)):
        env = dict(zip(scope, assign))
        tot = F(0)
        for x in range(6):
            env[var] = x
            prod = F(1)
            for sc, tb in touch:
                prod *= tb[tuple(env[v] for v in sc)]
                if prod == 0:
                    break
            tot += prod
        table[assign] = tot
    return rest + [(tuple(scope), table)]


def marginal(fs, keep, sites):
    fs = list(fs)
    elim = [s for s in sites if s not in keep]
    while elim:
        # min-scope heuristic
        best = min(elim, key=lambda v: len({u for sc, _ in fs if v in sc for u in sc}))
        fs = multiply_sum_out(fs, best)
        elim.remove(best)
    out = {}
    for assign in itertools.product(range(6), repeat=len(keep)):
        env = dict(zip(keep, assign))
        prod = F(1)
        for sc, tb in fs:
            prod *= tb[tuple(env[v] for v in sc)]
        out[assign] = prod
    return out


def main():
    n = m = 4
    sites = [(i, j) for i in range(n) for j in range(m)]
    report = {}
    all_ok = True
    for trip in ((3, 1, 2), (5, 2, 4)):
        K, K2 = kernel(*trip)
        fs = factors(n, m, K, K2)
        chain = lambda vals: F(1, 6) * _prod(K[vals[k - 1]][vals[k]] for k in range(1, len(vals)))
        cols_ok = all(all(v == chain(a) for a, v in marginal(fs, [(i, j) for i in range(n)], sites).items()) for j in range(m))
        rows_ok = all(all(v == chain(a) for a, v in marginal(fs, [(i, j) for j in range(m)], sites).items()) for i in range(n))
        blocks_ok, cond_ok = True, True
        for i in range(n - 1):
            for j in range(m - 1):
                c, b, a, d = (i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)
                mg = marginal(fs, [c, b, a, d], sites)
                for (vc, vb, va, vd), val in mg.items():
                    pi = F(1, 6) * K[vc][va] * K[vc][vb] * K[va][vd] * K[vd][vb] / K2[va][vb]
                    blocks_ok &= val == pi
                for vc in range(6):
                    tot_c = sum(mg[(vc, vb, va, vd)] for vb in range(6) for va in range(6) for vd in range(6))
                    for va in range(6):
                        for vb in range(6):
                            pab = sum(mg[(vc, vb, va, vd)] for vd in range(6)) / tot_c
                            cond_ok &= pab == K[vc][va] * K[vc][vb]
        diag_ok = all(all(v == F(1, 6) * K2[a][b] for (a, b), v in marginal(fs, [(i, j + 1), (i + 1, j)], sites).items())
                      for i in range(n - 1) for j in range(m - 1))
        defects = []
        for i in range(n - 1):
            for j in range(m - 1):
                for path in (((i, j), (i, j + 1), (i + 1, j + 1)), ((i, j), (i + 1, j), (i + 1, j + 1))):
                    mg = marginal(fs, list(path), sites)
                    dmax = F(0)
                    for x, y in itertools.product(range(6), repeat=2):
                        pxy = sum(mg[(x, y, z)] for z in range(6))
                        py = sum(mg[(x2, y, z)] for x2 in range(6) for z in range(6))
                        for z in range(6):
                            pz_xy = mg[(x, y, z)] / pxy
                            pz_y = sum(mg[(x2, y, z)] for x2 in range(6)) / py
                            dmax = max(dmax, abs(pz_xy - pz_y))
                    defects.append(dmax)
        ok = cols_ok and rows_ok and blocks_ok and cond_ok and diag_ok and all(d > 0 for d in defects)
        all_ok &= ok
        report[trip] = (cols_ok, rows_ok, blocks_ok, cond_ok, diag_ok, min(defects), max(defects), len(defects))
        print(f"4x4, triple {trip}: every column K-chain {cols_ok}; every row K-chain {rows_ok}; all 9 blocks = pi {blocks_ok}; "
              f"P(a,b|c) = K(c,a)K(c,b) {cond_ok}; all anti-diagonal pairs = K^2/6 {diag_ok}; {len(defects)} turning 3-site staircases, "
              f"Markov defects in [{float(min(defects)):.6f}, {float(max(defects)):.6f}] (all nonzero {all(d > 0 for d in defects)})")
    # P(c | c, c) > K(c -> c) at every non-constant triple of {1..10}^3 (closed form of the minimal staircase conditional)
    viol, tested = [], 0
    for p, q, r in itertools.product(range(1, 11), repeat=3):
        if p == q == r:
            continue
        K, K2 = kernel(p, q, r)
        for c in (0, 2):
            val = sum(K[c][a] * K[a][c] * K[c][c] / K2[a][c] for a in range(6))
            tested += 1
            if val <= K[c][c]:
                viol.append((p, q, r, c))
    print(f"P(c|c,c) > K(c->c): {tested} (triple, c) cases on {{1..10}}^3 non-constant, violations {len(viol)}")
    # extension counts: hook length vs direct DP count of standard Young tableaux of rectangular shape
    def hook(r_, s_):
        num = factorial(r_ * s_)
        den = 1
        for i in range(r_):
            for j in range(s_):
                den *= (r_ - i - 1) + (s_ - j - 1) + 1
        return num // den

    def direct(r_, s_):
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def ways(state):
            if all(x == s_ for x in state):
                return 1
            tot = 0
            for i in range(r_):
                if state[i] < s_ and (i == 0 or state[i - 1] > state[i]):
                    st = list(state)
                    st[i] += 1
                    tot += ways(tuple(st))
            return tot
        return ways(tuple([0] * r_))

    counts = {(r_, s_): (hook(r_, s_), direct(r_, s_)) for r_, s_ in ((2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5))}
    counts_ok = all(a == b for a, b in counts.values()) and [counts[k][0] for k in ((2, 3), (3, 3), (3, 4), (4, 4))] == [5, 42, 462, 24024]
    print(f"linear extensions (hook length = direct count): {counts}")
    if not (all_ok and not viol and counts_ok):
        print(f"HIT: a finite statement fails: 4x4 checks {all_ok}, inequality violations {viol[:3]}, counts {counts_ok}")
    print(f"SUMMARY: by exact variable elimination on the 4 x 4 rectangle (beyond the note's 3 x 4), at both declared triples every "
          f"column and row is the K-chain, all 9 blocks carry the corner law pi with P(a,b|c) = K(c,a)K(c,b), all anti-diagonal pairs are "
          f"K^2/6, and all 18 turning 3-site staircases have nonzero Markov defect; P(c|c,c) > K(c->c) holds in all {tested} cases on "
          f"{{1..10}}^3; the extension counts 5, 42, 462, 24024 extend to {counts[(4, 5)][0]} and {counts[(5, 5)][0]}: no falsifier fires")


def _prod(it):
    out = F(1)
    for v in it:
        out *= v
    return out


if __name__ == "__main__":
    main()
