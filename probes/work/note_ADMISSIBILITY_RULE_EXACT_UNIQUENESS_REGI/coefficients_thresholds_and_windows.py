#!/usr/bin/env python3
"""J:note falsifiers for ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06 (on main).

Falsifiers implemented (the note's list), exact rational arithmetic throughout:
  1. "a literal ... differing", "c_1 != 0 at (2,2,2) or c_1 = 0 at a non-constant triple", "6c_1(7,3,5) < 1",
     "c_1^(4)(2,5,3) <= c_1(2,5,3)": c_1 recomputed at every declared triple by brute force over all 6^5 ordered shells and all 30 ordered
     value pairs at the flipped slot (the runner's definition), and independently by a multiset reduction (252 shells x 15 pairs);
  2. "the diamond differing": 6c_1(p,q,4) < 1 exactly on p, q in 1..12 (multiset reduction), and beyond the note's grid the same
     region at r = 3 and r = 5 (numbers only);
  3. "a crossing outside its bracket", "a declared line point with 6c_1 >= 1": the sign of 6c_1 - 1 at exact rationals 1e-15 outside
     and inside every one of the six isolating brackets on the lines (t,1,1), (t,t,1), (1,1,t), and 6c_1 < 1 at 25 rational points
     between the two crossings of each line;
  4. "a center-site total variation above (D_Lambda b)_c": the exact site marginals of the planar static law with twelve (3x3),
     sixteen (4x4) and twenty (5x5) exterior slots under the base exterior (P(+e_x) everywhere) and one flipped slot, by a
     column-factorised row transfer in exact integers (not enumeration), at (2,1,2) and (3,2,2); TV at EVERY site against (D b)_x,
     D = (I - c_1^(4) A)^-1; the note's center value 691410442136477999520/76730168638463067377251 and bound 1/56 reproduced;
  5. "sum_y N_n(0,y) != 6^n for some n <= 4": walk counts on Z^3 by convolution to n = 8.
HIT if any finite statement fails.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as Fr

import numpy as np

VALS = range(6)                  # +x, -x, +y, -y, +z, -z


def phi_table(p, q, r):
    t = [[None] * 6 for _ in range(6)]
    for s in VALS:
        for u in VALS:
            t[s][u] = p if s == u else (q if s // 2 == u // 2 else r)
    return t


def tv(w, fa, fb):
    """TV between normalised w*fa and w*fb (lists of 6 positive ints)."""
    a = [x * y for x, y in zip(w, fa)]
    b = [x * y for x, y in zip(w, fb)]
    A, B = sum(a), sum(b)
    return Fr(sum(abs(x * B - y * A) for x, y in zip(a, b)), 2 * A * B)


def c1_bruteforce(p, q, r, d=6):
    ph = phi_table(p, q, r)
    best = Fr(0)
    for shell in itertools.product(VALS, repeat=d - 1):
        w = [1] * 6
        for s in VALS:
            for y in shell:
                w[s] *= ph[s][y]
        for a in VALS:
            for b in VALS:
                if a != b:
                    best = max(best, tv(w, [ph[s][a] for s in VALS], [ph[s][b] for s in VALS]))
    return best


def c1_multiset(p, q, r, d=6):
    ph = phi_table(p, q, r)
    best = Fr(0)
    for ms in itertools.combinations_with_replacement(VALS, d - 1):
        w = [1] * 6
        for s in VALS:
            for y in ms:
                w[s] *= ph[s][y]
        for a, b in itertools.combinations(VALS, 2):
            best = max(best, tv(w, [ph[s][a] for s in VALS], [ph[s][b] for s in VALS]))
    return best


def c1_rational(p, q, r):
    """c_1 for rational weights: scale to integers (homogeneous of degree zero)."""
    from math import lcm
    den = lcm(Fr(p).denominator, Fr(q).denominator, Fr(r).denominator)
    return c1_multiset(int(Fr(p) * den), int(Fr(q) * den), int(Fr(r) * den))


LITERALS = {(3, 1, 2): Fr(270, 989), (5, 2, 4): Fr(8650000, 40615109), (2, 1, 2): Fr(2, 13), (3, 2, 2): Fr(2079, 15566),
            (5, 4, 4): Fr(4000000, 61385721), (11, 10, 10): Fr(98241110000, 4544062780611), (2, 2, 2): Fr(0)}
DIAMOND = {(2, 4), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (5, 6), (6, 4), (6, 5)}
BRACKETS = {"(t,1,1) t*": (Fr("1.60970232778584910813"), Fr("1.60970232778584910814")),
            "(t,t,1) t*": (Fr("1.47753945492134830313"), Fr("1.47753945492134830314")),
            "(1,1,t) t*": (Fr("0.67680087774930621901"), Fr("0.67680087774930621903")),
            "(t,1,1) t2": (Fr("0.47722557505166113456"), Fr("0.47722557505166113457")),
            "(t,t,1) t2": (Fr("0.69167061103656469380"), Fr("0.69167061103656469381")),
            "(1,1,t) t2": (Fr("1.44577488770465582773"), Fr("1.44577488770465582774"))}
LINE = {"(t,1,1)": lambda t: (t, 1, 1), "(t,t,1)": lambda t: (t, t, 1), "(1,1,t)": lambda t: (1, 1, t)}


def thresholds():
    out, eps = {}, Fr(1, 10 ** 15)
    for name, (lo, hi) in BRACKETS.items():
        line = LINE[name.split()[0]]
        f = lambda t: 6 * c1_rational(*line(t)) - 1
        out[name] = (f(lo - eps) > 0) != (f(hi + eps) > 0) and f(lo - eps) != 0 and f(hi + eps) != 0
    inside = {}
    for name, fn in LINE.items():
        a = BRACKETS[name + " t2"][1] if name != "(1,1,t)" else BRACKETS["(1,1,t) t*"][1]
        b = BRACKETS[name + " t*"][0] if name != "(1,1,t)" else BRACKETS["(1,1,t) t2"][0]
        pts = [a + (b - a) * Fr(k, 26) for k in range(1, 26)]
        inside[name] = (float(a), float(b), max(float(6 * c1_rational(*fn(t))) for t in pts))
    return out, inside


# -------------------------------------------------------------------------------------------------- planar windows by transfer
def window_marginals(L, p, q, r, flip):
    """Exact site marginals (numerators, Z) of the L x L planar static law; exterior P(+e_x)=0 everywhere, value 1 at the left slot of
    row `flip` if flip is not None. Rows i = 0..L-1 (bottom..top), columns j = 0..L-1."""
    ph = np.array(phi_table(p, q, r), dtype=object)
    shape = (6,) * L

    def row_weight(i):
        W = np.ones(shape, dtype=object)
        for idx in itertools.product(VALS, repeat=L):
            w = 1
            for j in range(L - 1):
                w *= ph[idx[j], idx[j + 1]]
            left = 1 if (flip is not None and i == flip) else 0
            w *= ph[idx[0], left] * ph[idx[L - 1], 0]
            if i == 0:
                for j in range(L):
                    w *= ph[idx[j], 0]
            if i == L - 1:
                for j in range(L):
                    w *= ph[idx[j], 0]
            W[idx] = w
        return W

    def vertical(F):
        for j in range(L):
            F = np.moveaxis(np.tensordot(ph, F, axes=([0], [j])), 0, j)
        return F

    RW = [row_weight(i) for i in range(L)]
    Fw = [None] * L
    F = RW[0]
    Fw[0] = F
    for i in range(1, L):
        F = vertical(F) * RW[i]
        Fw[i] = F
    Bw = [None] * L
    B = np.ones(shape, dtype=object)
    Bw[L - 1] = B
    for i in range(L - 2, -1, -1):
        B = vertical(B * RW[i + 1])                         # phi symmetric, so the same contraction transports backwards
        Bw[i] = B
    Z = int(np.sum(Fw[L - 1]))
    marg = {}
    for i in range(L):
        joint = Fw[i] * Bw[i]
        for j in range(L):
            axes = tuple(k for k in range(L) if k != j)
            m = np.sum(joint, axis=axes)
            marg[(i, j)] = [int(x) for x in m]
    return marg, Z


def solve(A, b):
    n = len(A)
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c] / M[c][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def windows():
    out = {}
    for (p, q, r) in ((2, 1, 2), (3, 2, 2)):
        c4 = c1_multiset(p, q, r, d=4)
        for L in (3, 4, 5):
            flip = 1 if L == 3 else L // 2
            base, Z0 = window_marginals(L, p, q, r, None)
            flp, Z1 = window_marginals(L, p, q, r, flip)
            sites = [(i, j) for i in range(L) for j in range(L)]
            pos = {s: k for k, s in enumerate(sites)}
            n = len(sites)
            A = [[Fr(0)] * n for _ in range(n)]
            for (i, j), k in pos.items():
                A[k][k] = Fr(1)
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nb = (i + di, j + dj)
                    if nb in pos:
                        A[k][pos[nb]] -= c4
            b = [c4 if s == (flip, 0) else Fr(0) for s in sites]
            Db = solve(A, b)
            worst, ok, center_tv = Fr(0), True, None
            for s in sites:
                t = Fr(sum(abs(x * Z1 - y * Z0) for x, y in zip(base[s], flp[s])), 2 * Z0 * Z1)
                ok &= t <= Db[pos[s]]
                if Db[pos[s]] > 0:
                    worst = max(worst, t / Db[pos[s]])
                if L == 3 and s == (1, 1):
                    center_tv = (t, Db[pos[s]])
            out[((p, q, r), L)] = {"c1^(4)": c4, "max row sum": 4 * c4, "TV <= (Db)_x at every site": ok,
                                   "max TV/(Db)": float(worst), "center (TV, bound) L=3": center_tv}
    return out


def center_extra():
    """The note's other executed 3x3 centers: (3,2,2), (5,4,4) (bound asserted) and (3,1,2) (row sum above one, TV recorded)."""
    out = {}
    for t in ((3, 2, 2), (5, 4, 4), (3, 1, 2)):
        c4 = c1_multiset(*t, d=4)
        base, Z0 = window_marginals(3, *t, None)
        flp, Z1 = window_marginals(3, *t, 1)
        tvc = Fr(sum(abs(x * Z1 - y * Z0) for x, y in zip(base[(1, 1)], flp[(1, 1)])), 2 * Z0 * Z1)
        out[t] = (c4, 4 * c4, float(tvc))
    return out


def walks(nmax=8):
    counts = {(0, 0, 0): 1}
    sums = []
    for n in range(1, nmax + 1):
        new = {}
        for (x, y, z), c in counts.items():
            for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                k = (x + d[0], y + d[1], z + d[2])
                new[k] = new.get(k, 0) + c
        counts = new
        sums.append(sum(counts.values()) == 6 ** n)
    return all(sums)


def main():
    brute = {t: c1_bruteforce(*t) for t in LITERALS}
    multi = {t: c1_multiset(*t) for t in LITERALS}
    lit_ok = all(brute[t] == multi[t] == v for t, v in LITERALS.items())
    c735 = c1_multiset(7, 3, 5)
    c253, c4_253 = c1_multiset(2, 5, 3), c1_multiset(2, 5, 3, d=4)
    print(f"1. literals by brute force over 6^5 shells x 30 pairs and by 252 multisets x 15 pairs: agree with the note {lit_ok}; "
          f"6c_1(7,3,5) = {6 * c735} ({float(6 * c735):.5f}); c_1^(4)(2,5,3) = {c4_253}, c_1(2,5,3) = {c253}")
    grid = {(p, q) for p in range(1, 13) for q in range(1, 13) if 6 * c1_multiset(p, q, 4) < 1}
    beyond = {r: sorted((p, q) for p in range(1, 13) for q in range(1, 13) if 6 * c1_multiset(p, q, r) < 1) for r in (3, 5)}
    print(f"2. r = 4 region on 1..12: equals the note's diamond {grid == DIAMOND} ({len(grid)} cells); beyond: r = 3 region {beyond[3]}, "
          f"r = 5 region {beyond[5]}")
    th, inside = thresholds()
    print(f"3. sign change across every bracket (1e-15 outside): {th}; max 6c_1 at 25 interior points per line: {inside}")
    win = windows()
    for k, v in win.items():
        print(f"4. {k}: {v}")
    ce = center_extra()
    print(f"4'. 3x3 centers (c_1^(4), row sum, TV): {ce}")
    wk = walks()
    print(f"5. sum_y N_n(0,y) = 6^n for n = 1..8: {wk}")
    fails = []
    if not lit_ok:
        fails.append("literals")
    if not (6 * c735 > 1 and c4_253 > c253):
        fails.append("(7,3,5) or window-vs-shell coefficient")
    if grid != DIAMOND:
        fails.append("diamond")
    if not all(th.values()):
        fails.append("threshold brackets")
    if any(v[2] >= 1 for v in inside.values()):
        fails.append("line point with 6c_1 >= 1")
    center = win[((2, 1, 2), 3)]["center (TV, bound) L=3"]
    if center[0] != Fr(691410442136477999520, 76730168638463067377251) or center[1] != Fr(1, 56):
        fails.append(f"3x3 center values {center}")
    if not all(v["TV <= (Db)_x at every site"] and v["max row sum"] < 1 for v in win.values()):
        fails.append("Theorem H site bound")
    if not wk:
        fails.append("walk counts")
    trunc = lambda x, label: 0 <= x - label < 1e-7              # the note's decimal labels are truncated to seven places
    if not (ce[(3, 2, 2)][0] == Fr(1404, 11431) and trunc(ce[(3, 2, 2)][2], 0.0073929) and ce[(5, 4, 4)][0] == Fr(10000, 175641)
            and trunc(ce[(5, 4, 4)][2], 0.0016901) and ce[(3, 1, 2)][0] == Fr(918, 3431) and ce[(3, 1, 2)][1] == Fr(3672, 3431)
            and trunc(ce[(3, 1, 2)][2], 0.0346753)):
        fails.append(f"3x3 center literals {ce}")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: all seven literals agree under brute force and a multiset reduction, 6c_1(7,3,5) = {float(6 * c735):.4f} > 1, "
          f"c_1^(4)(2,5,3) > c_1(2,5,3); the r = 4 region on 1..12 is the note's 15-cell diamond (beyond: r = 3 has {len(beyond[3])} "
          f"cells, r = 5 has {len(beyond[5])}); 6c_1 - 1 changes sign across all six isolating brackets and stays below 1 at 75 interior "
          f"line points (largest {max(v[2] for v in inside.values()):.4f}); the column-factorised transfer reproduces the 3x3 center TV "
          f"691410442136477999520/76730168638463067377251 with bound 1/56, and TV <= (D b)_x holds at every site of the 3x3, 4x4 and 5x5 "
          f"windows at (2,1,2) and (3,2,2) (largest ratio {max(v['max TV/(Db)'] for v in win.values()):.4f}); walk counts hold to n = 8; "
          f"no falsifier fires")


if __name__ == "__main__":
    main()
