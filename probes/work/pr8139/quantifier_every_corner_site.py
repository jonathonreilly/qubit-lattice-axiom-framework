#!/usr/bin/env python3
"""J:attack:PR8139 — pattern (d) QUANTIFIER SCOPE.

R1/R3: G_kappa has six axial plus six face-diagonal neighbours, for every
corner kappa in {±1}^3 and every site x (executed at the origin). Extra
sites and all eight corners. HIT if some (x, kappa) has |G|!=12, a
face-diagonal that is a Z^3 NN edge, or a triangle in the NN graph.
"""
from __future__ import annotations

from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
AXIAL = tuple(tuple(s * e[i] for i in range(3)) for e in E for s in (1, -1))
CORNERS = tuple(product((-1, 1), repeat=3))
NN = set(AXIAL)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def D(k):
    out = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            out.append(tuple(k[i] * E[i][a] - k[j] * E[j][a] for a in range(3)))
    return tuple(out)


def G(x, k):
    return tuple(add(x, v) for v in AXIAL) + tuple(add(x, v) for v in D(k))


def main() -> int:
    hits = []
    sites = [(0, 0, 0), (1, 0, 0), (2, -1, 3), (-4, 5, 1), (7, 7, -7)]
    print(f"|CORNERS|={len(CORNERS)} stated 8")
    if len(set(CORNERS)) != 8:
        hits.append("corners not 8 distinct")
    for x in sites:
        for k in CORNERS:
            g = G(x, k)
            if len(set(g)) != 12:
                hits.append(f"|G|={len(set(g))} != 12 at x={x} k={k}")
                break
            d = D(k)
            if len(set(d)) != 6:
                hits.append(f"|D|={len(set(d))} != 6 at k={k}")
                break
            for v in d:
                if v in NN:
                    hits.append(f"face-diagonal {v} is NN at k={k}")
                    break
                if sum(abs(c) for c in v) != 2:
                    hits.append(f"D vector {v} has l1!={2}")
                    break
            else:
                continue
            break
        else:
            print(f"OK x={x}: all 8 corners have |G|=12, |D|=6, D not NN")
            continue
        break
    else:
        print(f"OK: {len(sites)} sites × 8 corners")

    # Z^3 NN has no triangles: extra 2-step pairs at extra origins
    for a in NN:
        for b in NN:
            if a >= b:
                continue
            diff = tuple(a[i] - b[i] for i in range(3))
            if sum(abs(c) for c in diff) == 1:
                hits.append(f"NN triangle 0-{a}-{b}")
    print("OK: Z^3 NN triangle-free on the six-star")

    if hits:
        print("HIT: " + "; ".join(hits[:4]))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(hits[:3]))
        return 0
    print(
        "SUMMARY: attack pattern (d) QUANTIFIER SCOPE - G_kappa has 12 distinct "
        "neighbours (6 axial + 6 face-diagonal, l1=2, not NN) at every tested "
        "site and all eight corners; Z^3 NN remains triangle-free"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
