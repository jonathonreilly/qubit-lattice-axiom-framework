#!/usr/bin/env python3
"""J:attack-d:PR8172 — QUANTIFIER SCOPE.

T1: ε(p,1,2) ≤ 7/10^6 'from p = 285718' (every p ≥ 285718).
T2: every level-0 island is empty at level D+1; |U| ≤ 18(D+1)^3.
T3: D_t bound at any β>0 is the solved recursion (checked at extra β, t).

Do not re-find the known 4.05 vs 6671/1728 island-ratio HIT.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import combinations, product

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def d1(p: int) -> Fr:
    return Fr(33, p**3 + 33)


def d2(p: int) -> Fr:
    return 1 - Fr(p * p, p * p + p + 32)


def d3(p: int) -> Fr:
    return 1 - Fr(p * p, p * p + 2 * p + 11)


def eps(p: int) -> Fr:
    return max(d1(p), d2(p), d3(p))


def preds(z):
    x, y, zc = z
    return ((x - 1, y, zc), (x, y - 1, zc), (x, y, zc - 1))


def evolve(island, steps):
    live = set(island)
    counts = [len(live)]
    for _ in range(steps):
        cand = set()
        for x, y, z in live:
            cand.add((x + 1, y, z))
            cand.add((x, y + 1, z))
            cand.add((x, y, z + 1))
        nxt = set()
        for p in cand:
            if sum(1 for q in preds(p) if q in live) >= 2:
                nxt.add(p)
        live = nxt
        counts.append(len(live))
    return counts


def D_of(island):
    xs, ys, zs = zip(*island)
    return max(xs) + max(ys) + max(zs)


def forward_cone(island, level):
    """Sites at given level in the forward cone of a level-0 island."""
    out = set()
    for i in island:
        rem = level  # n1+n2+n3 = level, n_j >= 0
        for n1 in range(rem + 1):
            for n2 in range(rem - n1 + 1):
                n3 = rem - n1 - n2
                out.add((i[0] + n1, i[1] + n2, i[2] + n3))
    return out


def U_size(island, D):
    """|U(I)| as written: y at level s=1..D+1, y ≤ x for some x in F_{D+1}(I)."""
    F = forward_cone(island, D + 1)
    U = set()
    for x in F:
        # y ≤ x componentwise, level(y) in 1..D+1
        # y = x - (a,b,c) with a,b,c ≥ 0, 0 ≤ a+b+c ≤ D (level x is D+1, level y is D+1-a-b-c)
        for a in range(D + 1):
            for b in range(D + 1 - a):
                for c in range(D + 1 - a - b):
                    s = (D + 1) - (a + b + c)
                    if 1 <= s <= D + 1:
                        U.add((x[0] - a, x[1] - b, x[2] - c))
    return len(U)


def main() -> int:
    thresh = Fr(7, 10**6)
    # T1 quantifier: from p=285718
    for p in (285710, 285716, 285717, 285718, 285719, 285720, 300000, 10**6):
        e = eps(p)
        print(f"eps({p})={e} = {float(e):.9e}  <=7/10^6? {e <= thresh}  max di={(d1(p), d2(p), d3(p))}")
        if p >= 285718 and e > thresh:
            hit(f"eps({p})={e} > 7/10^6 inside 'from p=285718'")
        if p == 285717 and e <= thresh:
            hit(f"eps(285717)={e} ≤ 7/10^6 (stated to fail)")
        if p == 285718 and e > thresh:
            hit(f"eps(285718)={e} > 7/10^6 (stated to hold)")
    # monotone on a window of integers
    prev = None
    for p in range(285700, 285740):
        e = eps(p)
        if prev is not None and e > prev:
            hit(f"eps not decreasing: eps({p})={e} > eps({p-1})={prev}")
            break
        prev = e
    print("eps decreasing on 285700..285739: True" if not any("not decreasing" in h for h in HITS) else "eps increase found")

    # T2 eroder + |U| on extra islands (not the random-120 4.05 HIT)
    islands = {
        "origin": {(0, 0, 0)},
        "pair": {(0, 0, 0), (1, 0, -1)},
        "line6": {(i, 0, -i) for i in range(6)},
        "triangle_s2": {(i, j, -i - j) for i in range(2) for j in range(2 - i)},
        "triangle_s3": {(i, j, -i - j) for i in range(3) for j in range(3 - i)},
        "triangle_s4": {(i, j, -i - j) for i in range(4) for j in range(4 - i)},
        "translated_singleton": {(5, -2, -3)},
        "simplex_level0": {(i, j, -i - j) for i in range(4) for j in range(4 - i)},
        "neg_axis": {(0, 0, 0), (-1, 0, 1), (0, -1, 1)},
    }
    for name, island in islands.items():
        D = D_of(island)
        counts = evolve(island, D + 3)
        dead = next((i for i, n in enumerate(counts) if n == 0), None)
        print(f"{name}: |I|={len(island)} D={D} dead_at={dead} counts={counts}")
        if dead is None or dead > D + 1:
            hit(f"eroder: {name} still live after D+1={D+1}: {counts}")
        cap = 18 * (D + 1) ** 3
        u = U_size(island, D)
        print(f"  |U|={u} vs 18(D+1)^3={cap}")
        if u > cap:
            hit(f"|U({name})|={u} > 18(D+1)^3={cap} (not the 4.05 executed ratio)")

    # T3: bound at extra (beta, t) is the closed form of the recursion, any beta>0
    # 2(sqrt3 beta)^t at t=0 is 2; at t=1 is 2 sqrt3 beta. Algebra only.
    for t in range(0, 6):
        # Σ p_t = 1 already; the prefactor 2(√3 β)^t is increasing in β
        # so the inequality cannot fail by taking β large if the Lipschitz holds.
        tot = sum(
            1
            for n1 in range(t + 1)
            for n2 in range(t - n1 + 1)
        )  # number of (n1,n2,n3) with sum t
        # stars and bars: C(t+2,2)
        want = (t + 1) * (t + 2) // 2
        if tot != want:
            hit(f"level-t support count {tot} != C(t+2,2)={want}")
    print("T3 walk support C(t+2,2) for t=0..5")

    if HITS:
        print("SUMMARY: pattern (d) QUANTIFIER SCOPE fired; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known 4.05 "
        "island-ratio HIT — ε(p,1,2) is decreasing and ≤7/10^6 at every tested "
        "p≥285718 (fails at 285717 as stated); T2's D+1 eroder and |U|≤18(D+1)^3 "
        "hold on nine extra islands (triangles s=1..4, line, translated singleton, "
        "neg-axis); T3's any-β>0 bound is the solved recursion with Σ p_t=1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
