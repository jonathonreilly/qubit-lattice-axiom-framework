#!/usr/bin/env python3
"""J:attack-a:PR8156 — closed cubic-walk witnesses on Z^3, n<=3.

V1: P_{2n}(0,0)=6^{-2n} C(2n,n) sum_a C(n,a)^2 C(2(n-a), n-a) is the return
probability of simple random walk on Z^3. Executed by enumeration for n<=3.
Z^3 is 6-regular and bipartite (no odd closed walks, no triangles).

HIT if the enumerated return count disagrees with the formula, a triangle
exists, or an odd-length return to the origin exists.
"""
from __future__ import annotations

from itertools import combinations, product
from math import comb


STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def P_formula(n):
    s = sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))
    return comb(2 * n, n) * s, 6 ** (2 * n)


def count_returns(n):
    """number of walks of length 2n from 0 to 0 on Z^3."""
    # DFS with length 2n is 6^{2n}; for n=3, 6^6=46656
    L = 2 * n
    tot = 0

    def rec(x, y, z, left):
        nonlocal tot
        if left == 0:
            if x == y == z == 0:
                tot += 1
            return
        rec(x + 1, y, z, left - 1)
        rec(x - 1, y, z, left - 1)
        rec(x, y + 1, z, left - 1)
        rec(x, y - 1, z, left - 1)
        rec(x, y, z + 1, left - 1)
        rec(x, y, z - 1, left - 1)

    rec(0, 0, 0, L)
    return tot


def main():
    hits = []
    for n in range(0, 4):
        num, den = P_formula(n)
        cnt = count_returns(n)
        print(f"n={n}: formula {num}/{den}, enumerated returns {cnt}, 6^{2*n}={den}")
        if cnt != num:
            hits.append(f"HIT: return count n={n}: enumerated {cnt} != formula numerator {num}")
            print(hits[-1])
        if n >= 1:
            # odd length 2n-1 cannot return (bipartite)
            pass

    # no triangles, no odd returns of length 1 or 3
    odd1 = count_returns_odd = None
    # length 1: 0 returns
    def returns_len(L):
        tot = 0

        def rec(x, y, z, left):
            nonlocal tot
            if left == 0:
                if x == y == z == 0:
                    tot += 1
                return
            rec(x + 1, y, z, left - 1)
            rec(x - 1, y, z, left - 1)
            rec(x, y + 1, z, left - 1)
            rec(x, y - 1, z, left - 1)
            rec(x, y, z + 1, left - 1)
            rec(x, y, z - 1, left - 1)

        rec(0, 0, 0, L)
        return tot

    r1, r3 = returns_len(1), returns_len(3)
    print(f"odd-length returns len1={r1} len3={r3}")
    if r1 or r3:
        hits.append(f"HIT: odd closed walks exist on Z^3: 1->{r1} 3->{r3}")
        print(hits[-1])

    pts = list(product(range(-1, 2), repeat=3))

    def nn(a, b):
        return sum(abs(x - y) for x, y in zip(a, b)) == 1

    tris = [
        (a, b, c)
        for a, b, c in combinations(pts, 3)
        if nn(a, b) and nn(b, c) and nn(c, a)
    ]
    print(f"triangles in [-1,1]^3: {len(tris)}")
    if tris:
        hits.append(f"HIT: Z^3 has a triangle {tris[0]}")
        print(hits[-1])

    if hits:
        print("SUMMARY: cubic-walk witnesses fail on Z^3")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — closed-walk counts on Z^3 "
        "match V1's formula for n=0,1,2,3, there are no odd-length returns of "
        "length 1 or 3, and the cubic lattice has no triangles"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
