#!/usr/bin/env python3
"""J:attack:PR8029 - infinite static source sector, attack pattern (c) EXECUTED NUMBERS.

Recompute the note's executed 15 exact controls (3 Stieltjes first-moment
rows, 2 local-resolvent modes, 3 Z3 projector identities plus the wrong
projector, resource N5 3+3+2+3+0) and the algebraic claims 9=3*3,
(4/a)(1-1/2)d=2d/a, shortest-path length d on Z^3, Casimir 4/a.

HIT if a stated executed number or identity disagrees.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def stieltjes(x: F):
    return (x / (x * x + 1), F(1) / (x * x + 1))


def shortest_len(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def geodesic(x, y):
    """One lattice shortest path from x to y (axis-aligned)."""
    cur = list(x)
    path = [tuple(cur)]
    for i in range(3):
        step = 1 if y[i] >= x[i] else -1
        while cur[i] != y[i]:
            cur[i] += step
            path.append(tuple(cur))
    return path


def main() -> None:
    hits = []
    n_ck = 0

    def ck(ok, msg):
        nonlocal n_ck
        n_ck += 1
        print(f"[{'ok' if ok else 'MISMATCH'}] {msg}")
        if not ok:
            hits.append(msg)

    # 3 first-moment / Stieltjes rows (per_element)
    for n in (2, 4, 8):
        p = F(1, n)
        mean = (1 - p) * 2 + p * (2 + n)
        ck((1 - p) + p == 1 and mean == 3, f"n={n} mixture weights and mean {mean}==3")
        z = tuple((1 - p) * a + p * b for a, b in zip(stieltjes(F(2)), stieltjes(F(2 + n))))
        diff = tuple(a - b for a, b in zip(z, stieltjes(F(2))))
        lip = sum(x * x for x in diff)
        ck(lip <= 4 * p * p, f"n={n} Stieltjes Lipschitz {lip} <= 4 p^2={4*p*p}")

    ck(F(2) < F(3), "2<3")

    # 2 local resolvent modes (per_mode): dim 4 and 6, first two diags are 1
    for dim in (4, 6):
        diag = [1] * (dim - 1) + [0]
        local = [stieltjes(F(x)) for x in diag[:2]]
        ck(local == [stieltjes(F(1))] * 2, f"dim={dim} local resolvent at 1,1")
        ck(min(diag) == 0 and min([1] * dim) == 1, f"dim={dim} finite bottom 0 vs all-1 bottom 1")

    # Z3 projector toy (per_site 3 labels + identities)
    P = [int((q + 1) % 3 == 0) for q in range(3)]
    ck(P == [0, 0, 1] and [p * p for p in P] == P, f"Z3 projector P={P} idempotent")
    ck(all(not p or (q + 1) % 3 == 0 for q, p in enumerate(P)), "P supported on q=2")
    v = [F(1), F(2), F(3)]
    proj = [p * x for p, x in zip(P, v)]
    ck(sum(x * x for x in proj) <= sum(x * x for x in v), "projector does not increase l2")
    wrong = [int(q % 3 == 0) for q in range(3)]
    ck(wrong != P and any(p and (q + 1) % 3 for q, p in enumerate(wrong)), f"wrong projector {wrong} != P")

    print(f"recomputed scientific checks: {n_ck} (stated 15)")
    if n_ck != 15:
        hits.append(f"check count {n_ck} vs stated 15")
        print("[MISMATCH] check count")

    if 3 * 3 != 9:
        hits.append("nine-dimensional E != 3 x 3-bar")
    print("[ok] nine-dimensional E = 3 x 3-bar")
    a, d, kappa = F(5, 2), F(7), F(1, 2)
    lo = (F(4) / a) * (1 - kappa) * d
    two = F(2) * d / a
    hi = F(4) * d / a
    ck(lo == two, f"(4/a)(1-1/2)d={lo} == 2d/a={two}")
    ck(lo <= hi, f"lower {lo} <= upper {hi}")

    x, y = (0, 0, 0), (2, 1, 0)
    dxy = shortest_len(x, y)
    g = geodesic(x, y)
    ck(len(g) - 1 == dxy == 3, f"shortest path {x}->{y} length {len(g)-1} (graph distance {dxy})")
    # Z^3 bipartite: odd cycle impossible; path of length 3 exists
    ck(dxy % 2 == sum(y) % 2, "bipartite distance parity")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; 15 exact Stieltjes/resolvent/Z3 controls, "
            "9=3*3, (4/a)(1-1/2)d=2d/a, and a length-d shortest path on Z^3 all match"
        )


if __name__ == "__main__":
    main()
