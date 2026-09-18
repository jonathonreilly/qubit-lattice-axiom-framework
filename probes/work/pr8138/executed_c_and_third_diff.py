#!/usr/bin/env python3
"""J:attack:PR8138 - block 08, attack pattern (c) EXECUTED NUMBERS.

Recompute (i) the eight-corner third difference of log K_3 at the stated
witness, (ii) c_k = max TV of k-neighbor kernels differing in one entry,
c = max(c_1,c_2,c_3), and 3c, at the eight table triples. Exact rationals.

HIT if a stated ratio or c-table entry disagrees.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {"+x": "-x", "-x": "+x", "+y": "-y", "-y": "+y", "+z": "-z", "-z": "+z"}

TABLE = {
    (3, 1, 2): (F(1, 6), F(30, 143), F(27, 110), F(27, 110), F(81, 110), F(27, 56)),
    (5, 2, 4): (F(3, 23), F(65, 434), F(10650, 63407), F(10650, 63407), F(31950, 63407), F(10650, 42107)),
    (7, 3, 5): (F(2, 15), F(910, 5609), F(5782, 30885), F(5782, 30885), F(5782, 10295), F(5782, 19321)),
    (2, 1, 2): (F(1, 11), F(1, 10), F(1, 9), F(1, 9), F(1, 3), F(1, 7)),
    (3, 2, 2): (F(1, 13), F(39, 406), F(234, 2077), F(234, 2077), F(702, 2077), F(234, 1609)),
    (5, 4, 4): (F(1, 25), F(25, 546), F(500, 9701), F(500, 9701), F(1500, 9701), F(500, 8701)),
    (11, 10, 10): (F(1, 61), F(671, 38502), F(73810, 3994861), F(73810, 3994861), F(221430, 3994861), F(73810, 3847241)),
    (2, 2, 2): (F(0), F(0), F(0), F(0), F(0), F(0)),
}
THIRD = {(3, 1, 2): F(2160, 2197), (5, 2, 4): F(686196, 704969), (2, 2, 2): F(1)}
WIT = ("+x", "+y", "+x", "+y", "+x", "+z")  # a0,a1; b0,b1; c0,c1


def K(pqr, s, t):
    p, q, r = pqr
    if s == t:
        return p
    if OPP[s] == t:
        return q
    return r


def K3(pqr, a, b, c):
    tot = 0
    for s in VALS:
        tot += K(pqr, a, s) * K(pqr, b, s) * K(pqr, c, s)
    return tot


def rcond(pqr, rec, s):
    if not rec:
        return F(1, 6)
    num = 1
    for a in rec:
        num *= K(pqr, a, s)
    den = 0
    for t in VALS:
        pr = 1
        for a in rec:
            pr *= K(pqr, a, t)
        den += pr
    return F(num, den)


def tv(p, q):
    return sum(abs(p[s] - q[s]) for s in VALS) / 2


def ck(pqr, k):
    best = F(0)
    for A in product(VALS, repeat=k):
        for i in range(k):
            for alt in VALS:
                if alt == A[i]:
                    continue
                Ap = list(A)
                Ap[i] = alt
                p = {s: rcond(pqr, A, s) for s in VALS}
                q = {s: rcond(pqr, tuple(Ap), s) for s in VALS}
                t = tv(p, q)
                if t > best:
                    best = t
    return best


def third_diff(pqr, wit=WIT):
    a0, a1, b0, b1, c0, c1 = wit
    num = (
        K3(pqr, a0, b0, c0)
        * K3(pqr, a1, b1, c0)
        * K3(pqr, a1, b0, c1)
        * K3(pqr, a0, b1, c1)
    )
    den = (
        K3(pqr, a1, b0, c0)
        * K3(pqr, a0, b1, c0)
        * K3(pqr, a0, b0, c1)
        * K3(pqr, a1, b1, c1)
    )
    return F(num, den)


def main() -> None:
    hits = []
    for pqr, stated in THIRD.items():
        got = third_diff(pqr)
        print(f"third-diff {pqr}: {got} (stated {stated})")
        if got != stated:
            hits.append(f"third-diff {pqr} {got} != {stated}")

    for pqr, (c1, c2, c3, c, c3x, th) in TABLE.items():
        g1, g2, g3 = ck(pqr, 1), ck(pqr, 2), ck(pqr, 3)
        gc = max(g1, g2, g3)
        g3c = 3 * gc
        gth = gc / (1 - 2 * gc) if 2 * gc < 1 else None
        print(f"{pqr}: c1={g1} c2={g2} c3={g3} c={gc} 3c={g3c} theta={gth}")
        for name, got, want in (
            ("c1", g1, c1),
            ("c2", g2, c2),
            ("c3", g3, c3),
            ("c", gc, c),
            ("3c", g3c, c3x),
        ):
            if got != want:
                hits.append(f"{pqr} {name} {got} != {want}")
        if gth != th:
            hits.append(f"{pqr} theta {gth} != {th}")
        if pqr != (2, 1, 2) and g3c >= 1:
            hits.append(f"{pqr} 3c={g3c} not < 1")
        if pqr == (2, 1, 2) and g3c != F(1, 3):
            hits.append(f"(2,1,2) 3c={g3c} != 1/3")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; third-difference 2160/2197 and 686196/704969 "
            "and the eight-row (c1,c2,c3,c,3c,theta) table all match exact kernel TV"
        )


if __name__ == "__main__":
    main()
