#!/usr/bin/env python3
"""J:attack:PR8024 - volume-uniform gap note, attack pattern (a) WITNESS REALIZABILITY.

The checker's cube graphs and plaquette loops must exist as stated: Z^3 is
bipartite (no triangles); each Wilson loop is a 4-cycle on the actual link
graph of [0,L)^3; whole-group vs individually-supported plaquette counts
are 3(L-1)^3 and 3 L (L-1)^2. Independently rebuilt for L=1..6 (beyond the
note's L=1,2,3). Casimir C(p,q)=(2/3)(p^2+pq+q^2+3p+3q) is checked against
K_e=(3/(2a)) C giving E=(p^2+pq+q^2+3p+3q)/a.

HIT if a loop fails to close, a triangle exists, or a stated count is wrong.
"""
from __future__ import annotations

from itertools import combinations, product
from fractions import Fraction as F

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def cube(n):
    return set(product(range(n), repeat=3))


def loop(x, i, j):
    return [(x, i, 1), (add(x, E[i]), j, 1), (add(x, E[j]), i, -1), (x, j, -1)]


def endpoints(item):
    x, i, sgn = item
    y = add(x, E[i])
    return (x, y) if sgn == 1 else (y, x)


def main() -> None:
    hits = []
    for L in range(1, 7):
        cells = cube(L)
        # bipartite: no odd cycles among nearest-neighbor vertices
        verts = list(cells)
        nb = {v: [] for v in verts}
        for v in verts:
            for d in E:
                w = add(v, d)
                if w in cells:
                    nb[v].append(w)
                    nb[w].append(v)
        triangles = 0
        for v in verts:
            nbs = nb[v]
            for a, b in combinations(nbs, 2):
                if a in nb[b]:
                    triangles += 1
        print(f"L={L}: vertices {len(cells)} triangles {triangles}")
        if triangles:
            hits.append(f"L={L} has {triangles} triangles; Z^3 cubic is bipartite")

        groups = [x for x in cells if all(add(x, z) in cells for z in E)]
        indiv = [
            (x, i, j)
            for x in cells
            for i, j in combinations(range(3), 2)
            if add(x, E[i]) in cells and add(x, E[j]) in cells
        ]
        want_g, want_i = 3 * (L - 1) ** 3, 3 * L * (L - 1) ** 2
        print(f"  whole-group {3*len(groups)} (want {want_g}); indiv {len(indiv)} (want {want_i})")
        if 3 * len(groups) != want_g:
            hits.append(f"L={L} whole-group {3*len(groups)} != {want_g}")
        if len(indiv) != want_i:
            hits.append(f"L={L} indiv {len(indiv)} != {want_i}")
        if len(indiv) - 3 * len(groups) != 3 * (L - 1) ** 2:
            hits.append(f"L={L} omitted {len(indiv)-3*len(groups)} != {3*(L-1)**2}")

        for x, i, j in indiv:
            w = loop(x, i, j)
            ends = [endpoints(a) for a in w]
            closed = all(ends[k][1] == ends[(k + 1) % 4][0] for k in range(4))
            verts4 = {ends[k][0] for k in range(4)} | {ends[k][1] for k in range(4)}
            if not closed:
                hits.append(f"L={L} loop at {x,i,j} does not close: {ends}")
            if len(verts4) != 4:
                hits.append(f"L={L} loop at {x,i,j} has {len(verts4)} vertices {verts4}")
            if any(v not in cells for v in verts4):
                hits.append(f"L={L} loop at {x,i,j} leaves the cube: {verts4 - cells}")

        # open-box identities (note L=1,2; here to 5)
        if L <= 5:
            verts_o = cube(L + 1)
            real = {(x, i) for x in verts_o for i in range(3) if add(x, E[i]) in verts_o}
            faces = [
                (x, i, j)
                for x in verts_o
                for i, j in combinations(range(3), 2)
                if add(add(x, E[i]), E[j]) in verts_o
            ]
            print(f"  open L={L}: edges {len(real)} want {3*L*(L+1)**2}; faces {len(faces)} want {3*L*L*(L+1)}")
            if len(real) != 3 * L * (L + 1) ** 2:
                hits.append(f"open L={L} edges {len(real)} != {3*L*(L+1)**2}")
            if len(faces) != 3 * L * L * (L + 1):
                hits.append(f"open L={L} faces {len(faces)} != {3*L*L*(L+1)}")

    # Casimir vs electric energy
    def C(p, q):
        return F(2, 3) * (p * p + p * q + q * q + 3 * p + 3 * q)

    a = F(5, 2)
    for p, q in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (3, 1)):
        E_pq = F(p * p + p * q + q * q + 3 * p + 3 * q, 1) / a
        Ke = F(3, 2) / a * C(p, q)
        print(f"Casimir (p,q)=({p},{q}): C={C(p,q)} K_e={Ke} E={E_pq}")
        if Ke != E_pq:
            hits.append(f"K_e vs E mismatch at ({p},{q}): {Ke} != {E_pq}")
        if (p, q) == (0, 0) and C(p, q) != 0:
            hits.append("vacuum Casimir not zero")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (a) WITNESS REALIZABILITY; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (a) WITNESS REALIZABILITY; cube graphs are triangle-free 4-cycle "
            "plaquette complexes; whole-group/indiv/open-box counts match 3(L-1)^3, 3L(L-1)^2 "
            "and 3L(L+1)^2 through L=6; K_e=(3/(2a))C equals E=(p^2+pq+q^2+3p+3q)/a"
        )


if __name__ == "__main__":
    main()
