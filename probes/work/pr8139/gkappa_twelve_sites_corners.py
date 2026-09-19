#!/usr/bin/env python3
"""J:attack-a:PR8139 — WITNESS REALIZABILITY of G_kappa and the eight corners.

Note: G_kappa(x) = {x ± e_i} ∪ D_kappa(x), twelve sites; D_kappa(x) =
{x + kappa_i e_i - kappa_j e_j : i != j}, six face-diagonal sites (l1=2,
not lattice edges; Z^3 bipartite). Eight corners kappa in {±1}^3; 24 proper
cubic rotations act transitively, stabilizer the 3-fold about the body diagonal.

HIT if some D_kappa collides with an axial neighbor, has size != 6, is a
lattice edge, or the rotation action is not as stated.
"""
from __future__ import annotations

from itertools import permutations, product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
AXIAL = tuple(tuple(s * e[i] for i in range(3)) for e in E for s in (1, -1))
CORNERS = tuple(product((-1, 1), repeat=3))


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def l1(v):
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def D(k):
    out = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            out.append(tuple(k[i] * E[i][a] - k[j] * E[j][a] for a in range(3)))
    return tuple(out)


def det3(P, signs):
    # permutation matrix with signs: rows i -> signs[i] * e_{P[i]}
    # det = sign(perm) * prod(signs)
    inv = 0
    P = list(P)
    for a in range(3):
        for b in range(a + 1, 3):
            if P[a] > P[b]:
                inv += 1
    s = 1 if inv % 2 == 0 else -1
    for t in signs:
        s *= t
    return s


def rotations():
    out = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if det3(perm, signs) != 1:
                continue
            def apply(v, perm=perm, signs=signs):
                w = [0, 0, 0]
                for i in range(3):
                    w[perm[i]] = signs[i] * v[i]
                return tuple(w)
            out.append(apply)
    return out


def main():
    hits = []
    for k in CORNERS:
        d = D(k)
        print(f"kappa={k} D={d}")
        if len(d) != 6:
            hits.append(f"{k} |D|={len(d)} != 6")
        if len(set(d)) != 6:
            hits.append(f"{k} D not distinct")
        for v in d:
            if l1(v) != 2:
                hits.append(f"{k} {v} l1={l1(v)} != 2 (would be a lattice edge if 1)")
            if v in AXIAL:
                hits.append(f"{k} D meets axial {v}")
            if v == (0, 0, 0):
                hits.append(f"{k} D contains 0")
        g = set(AXIAL) | set(d)
        if len(g) != 12:
            hits.append(f"{k} |G_kappa(0)|={len(g)} != 12")

    rots = rotations()
    print(f"proper cubic rotations: {len(rots)}")
    if len(rots) != 24:
        hits.append(f"|SO|={len(rots)} != 24")
    orbit = {rots[0]((1, 1, 1))}
    # act on (1,1,1)
    orb = set()
    for f in rots:
        orb.add(f((1, 1, 1)))
    print(f"orbit of (1,1,1): {sorted(orb)} size={len(orb)}")
    if orb != set(CORNERS):
        hits.append(f"orbit of +++ is {orb} not all 8 corners")
    stab = sum(1 for f in rots if f((1, 1, 1)) == (1, 1, 1))
    print(f"stabilizer of +++ : {stab}")
    if stab != 3:
        hits.append(f"stab={stab} != 3")

    # 2x2 rectangle embeds in Z^2 (no wrap): 4 sites, no +e=-e
    C2 = list(product((0, 1), repeat=2))
    def nb2(x):
        s = []
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            y = (x[0] + d[0], x[1] + d[1])
            if y in C2:
                s.append(y)
        return s
    degs = {x: len(nb2(x)) for x in C2}
    print(f"2x2 rectangle degrees {degs}")
    if any(len(nb2(x)) == 0 for x in C2):
        hits.append("2x2 rectangle isolated")

    if hits:
        print("HIT: " + hits[0])
        for h in hits[1:]:
            print("HIT: " + h)
        print("SUMMARY: WITNESS REALIZABILITY (PR #8139): " + "; ".join(hits[:3]))
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8139): all eight corners have "
            "|G_kappa(0)|=12 with six l1=2 face-diagonals disjoint from the axial "
            "neighbors; 24 proper cubic rotations act transitively with stabilizer 3; "
            "the 2x2 rectangle embeds in Z^2; pattern has purchase and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()
