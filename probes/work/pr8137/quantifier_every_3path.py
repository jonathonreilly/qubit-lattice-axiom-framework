#!/usr/bin/env python3
"""J:attack-d:PR8137 — QUANTIFIER SCOPE.

A collinear 3-site NN path exists along every axis; two sequential orders
(ends-first vs chain). Check all three axes and both orders.
"""
from itertools import permutations

HITS = []
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def main():
    for e in E:
        path = [(0, 0, 0), e, (2 * e[0], 2 * e[1], 2 * e[2])]
        for i in range(2):
            a, b = path[i], path[i + 1]
            d = sum(abs(a[j] - b[j]) for j in range(3))
            if d != 1:
                HITS.append(f"path {path} edge {i} l1={d}")
        print(f"axis {e}: path {path}")
    orders = list(permutations(range(3)))
    print(f"3-site orders {len(orders)}")
    if len(orders) != 6:
        HITS.append(f"3!={len(orders)}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - a collinear 3-site NN "
        "path exists on every axis and 3!=6 sequential orders exist"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
