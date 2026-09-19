#!/usr/bin/env python3
"""J:attack-f:PR8148 — pattern (f) NORMALIZATION.

Not the known R3 uniform-distance HIT (1/216, 56059/3369600).

R4 writes the plaquette sequential weight with Haar 1/6 on the first value,
1/36 = (1/6)^2 on a diagonal-first history, 1/4 over starting corners, and
G(p,d)=(1-p)d/6 + p d^2/36. Recompute at (3,1,2) by enumerating all 24
uniform-clock orders × 6^4 patterns. HIT if the 1/6 or 1/36 factor is off
(stated uniform ratios 152/169, 136/121, 1 at P1, P3, P4 would then fail).
"""
from __future__ import annotations

import itertools
from collections import defaultdict
from fractions import Fraction as Fr

M = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
P, Q, R = 3, 1, 2
Z1 = P + Q + 4 * R  # 12

# plaquette corners in cycle order
SITES = (0, 1, 2, 3)
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
DIAGS = ((0, 2), (1, 3))
NBR = {0: (1, 3), 1: (0, 2), 2: (1, 3), 3: (0, 2)}


def phi(i: int, j: int) -> int:
    d = M[i][0] * M[j][0] + M[i][1] * M[j][1] + M[i][2] * M[j][2]
    return P if d == 1 else (Q if d == -1 else R)


def Nk(vals: list[int]) -> int:
    if not vals:
        return 6
    acc = 0
    for v in range(6):
        w = 1
        for a in vals:
            w *= phi(v, a)
        acc += w
    return acc


def K(v: int, vals: list[int]) -> Fr:
    if not vals:
        return Fr(1, 6)
    num = 1
    for a in vals:
        num *= phi(v, a)
    return Fr(num, Nk(vals))


def Pi_phi(col: tuple[int, ...]) -> int:
    w = 1
    for a, b in EDGES:
        w *= phi(col[a], col[b])
    return w


def PiK(col: tuple[int, ...]) -> Fr:
    """Edge product of one-neighbour kernels φ/Z1, as in the note's ΠK."""
    return Fr(Pi_phi(col), Z1 ** 4)


def sequential(order: tuple[int, ...], col: tuple[int, ...]) -> Fr:
    formed = []
    pr = Fr(1)
    for x in order:
        rec = [col[y] for y in NBR[x] if y in formed]
        pr *= K(col[x], rec)
        formed.append(x)
    return pr


def d_of_pair(a: int, b: int) -> Fr:
    """Z1^2 / N_2(a,b) as in the note's d_same=72/13, d_anti=72/11, d_orth=6."""
    return Fr(Z1 * Z1, Nk([a, b]))


def G(p: Fr, d: Fr) -> Fr:
    return (1 - p) * d / 6 + p * (d * d) / 36


def main() -> int:
    hits: list[str] = []

    # stated d at (3,1,2)
    d_same = d_of_pair(0, 0)
    d_anti = d_of_pair(0, 1)
    d_orth = d_of_pair(0, 2)
    print(f"d_same={d_same} stated 72/13={Fr(72, 13)} eq={d_same == Fr(72, 13)}")
    print(f"d_anti={d_anti} stated 72/11={Fr(72, 11)} eq={d_anti == Fr(72, 11)}")
    print(f"d_orth={d_orth} stated 6 eq={d_orth == 6}")
    if d_same != Fr(72, 13) or d_anti != Fr(72, 11) or d_orth != 6:
        hits.append(f"d values {d_same, d_anti, d_orth}")

    # uniform clock: every order equally likely (1/24)
    orders = list(itertools.permutations(SITES))
    mass = defaultdict(lambda: Fr(0))
    for col in itertools.product(range(6), repeat=4):
        acc = Fr(0)
        for order in orders:
            acc += sequential(order, col)
        mass[col] = acc / 24

    tot = sum(mass.values())
    print(f"uniform plaquette mass sums to {tot}")
    if tot != 1:
        hits.append(f"uniform mass {tot} != 1")

    # P1 = (+x, -x, +x, -x) = (0,1,0,1)
    # P3 = (+x, +x, -x, -x) = (0,0,1,1)
    # P4 = (+x, -x, +y, +y) = (0,1,2,2)
    P1, P3, P4 = (0, 1, 0, 1), (0, 0, 1, 1), (0, 1, 2, 2)
    # static is proportional to PiK; ratio μ/PiK
    ratios = {}
    for name, pat in (("P1", P1), ("P3", P3), ("P4", P4)):
        pk = PiK(pat)
        ratios[name] = mass[pat] / pk
        print(f"{name} μ={mass[pat]} ΠK={pk} μ/ΠK={ratios[name]}")

    # uniform: p=1/3 at every fork, so μ/ΠK = G(1/3, d) for equal-diagonal patterns
    want = {
        "P1": G(Fr(1, 3), d_same),
        "P3": G(Fr(1, 3), d_anti),
        "P4": G(Fr(1, 3), d_orth),
    }
    stated = {"P1": Fr(152, 169), "P3": Fr(136, 121), "P4": Fr(1)}
    for name in ("P1", "P3", "P4"):
        print(f"{name}: brute {ratios[name]}  G(1/3,d)={want[name]}  stated {stated[name]}")
        if ratios[name] != want[name]:
            hits.append(f"{name} brute {ratios[name]} != G {want[name]}")
        if ratios[name] != stated[name]:
            hits.append(f"{name} brute {ratios[name]} != stated {stated[name]}")

    # factor audit: Haar 1/6 vs a wrong 1/4 (four corners) on first value
    # path history weight (1/6) ΠK d vs (1/4) ΠK d
    # pick one path order (0,1,2,3) on P1 and compare to the written formula
    path_order = (0, 1, 2, 3)
    pr_path = sequential(path_order, P1)
    written_path = Fr(1, 6) * PiK(P1) * d_same
    print(f"path order (0,1,2,3) on P1: sequential={pr_path} written (1/6)ΠK d={written_path}")
    if pr_path != written_path:
        hits.append(f"path 1/6 factor: seq {pr_path} != (1/6)ΠK d {written_path}")

    diag_order = (0, 2, 1, 3)  # start, opposite, then the other two
    pr_diag = sequential(diag_order, P1)
    written_diag = Fr(1, 36) * PiK(P1) * d_same * d_same
    print(f"diag-first (0,2,1,3) on P1: sequential={pr_diag} written (1/36)ΠK d^2={written_diag}")
    if pr_diag != written_diag:
        hits.append(f"diag 1/36 factor: seq {pr_diag} != (1/36)ΠK d^2 {written_diag}")

    # 1/4 over starts: for uniform, average of G
    g_avg = (
        G(Fr(1, 3), d_same)
        + G(Fr(1, 3), d_same)
        + G(Fr(1, 3), d_same)
        + G(Fr(1, 3), d_same)
    ) / 4
    print(f"(1/4)Σ G for P1 = {g_avg} vs brute μ/ΠK {ratios['P1']}")
    if g_avg != ratios["P1"]:
        hits.append(f"1/4 average {g_avg} != brute {ratios['P1']}")

    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - plaquette Haar 1/6, "
        "diagonal-first 1/36=(1/6)^2, start-average 1/4 and G=(1-p)d/6+p d^2/36 "
        "recompute exactly at (3,1,2) (uniform ratios 152/169, 136/121, 1); "
        "not the known R3 uniform-distance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
