#!/usr/bin/env python3
"""J:attack:PR8141 - block 10, attack pattern (a) WITNESS REALIZABILITY.

T6's plaquette a—b, a—c, b—d, c—d and 3-star must exist as Z^3 windows
(cubic lattice is bipartite: co-recorded pairs are never lattice edges).
The stated canonical-potential ratios are recomputed from the formation law
by Möbius inversion of μ_σ, exact rationals, (p,q,r)=(3,1,2).

HIT if a witness graph is not realizable on Z^3, a co-recorded pair is a
lattice edge, or a stated T6 ratio disagrees with the formation-law potential.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product

P, Q, R = 3, 1, 2
VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {"+x": "-x", "-x": "+x", "+y": "-y", "-y": "+y", "+z": "-z", "-z": "+z"}
VAC = "+x"


def K(s, t):
    if s == t:
        return P
    if OPP[s] == t:
        return Q
    return R


def Kk(a):
    tot = 0
    for s in VALS:
        pr = 1
        for ai in a:
            pr *= K(ai, s)
        tot += pr
    return tot


Z1 = sum(K(VAC, s) for s in VALS)  # p+q+4r = 12


def mu_plaquette(v):
    """Formation law on the 4-cycle, order (a,b,c,d); d records {b,c}."""
    a, b, c, d = v
    ra = F(1, 6)
    rb = F(K(a, b), Z1)
    rc = F(K(a, c), Z1)
    rd = F(K(b, d) * K(c, d), Kk((b, c)))
    return ra * rb * rc * rd


def mu_star(v):
    """Star: leaves first (uniform), center last records the three leaves."""
    l1, l2, l3, x = v
    return F(1, 6) ** 3 * F(K(l1, x) * K(l2, x) * K(l3, x), Kk((l1, l2, l3)))


def exp_phi(mu_fn, sites, A, assign, vac=VAC):
    """exp Φ_A(assign) from vacuum-normalized Möbius of log μ; rest of W at vac."""
    A = tuple(A)
    k = len(A)
    num, den = F(1), F(1)
    idx = {s: i for i, s in enumerate(sites)}
    for r in range(k + 1):
        for S in combinations(range(k), r):
            cfg = [vac] * len(sites)
            for i in S:
                cfg[idx[A[i]]] = assign[i]
            val = mu_fn(tuple(cfg))
            if (k - r) % 2 == 0:
                num *= val
            else:
                den *= val
    return num / den


def lattice_edges(pts):
    e = set()
    for i, p in enumerate(pts):
        for j, q in enumerate(pts):
            if i < j and sum(abs(p[k] - q[k]) for k in range(3)) == 1:
                e.add((i, j))
    return e


def main() -> None:
    hits = []
    # --- Z^3: two neighbors of a site are never adjacent ---
    origin = (0, 0, 0)
    nbs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    adj = 0
    for i, p in enumerate(nbs):
        for q in nbs[i + 1 :]:
            if sum(abs(p[k] - q[k]) for k in range(3)) == 1:
                adj += 1
    print(f"Z^3 origin: 6 neighbors, adjacent neighbor-pairs {adj} (want 0; cubic is bipartite)")
    if adj:
        hits.append(f"neighbor pairs of the origin are lattice-adjacent ({adj}); Z^3 would have triangles")

    # --- plaquette embedding: unit square ---
    names = ("a", "b", "c", "d")
    pts = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]  # a,b,c,d
    E = lattice_edges(pts)
    print(f"plaquette embedding edges {sorted(E)} (want (0,1),(0,2),(1,3),(2,3) = a-b,a-c,b-d,c-d)")
    want = {(0, 1), (0, 2), (1, 3), (2, 3)}
    if E != want:
        hits.append(f"plaquette embedding edges {E} != {want}")
    if (1, 2) in E or (0, 3) in E:
        hits.append("co-recorded or other diagonal is a lattice edge")
    print("non-edges {b,c}={1,2} and {a,d}={0,3} are face diagonals, not NN")

    # 1296
    ncfg = 6 ** 4
    print(f"plaquette configs {ncfg} (stated 1296)")
    if ncfg != 1296:
        hits.append(f"6^4={ncfg} != 1296")

    wit = ("-x", "+y", "+z", "-y")
    phi_bc = exp_phi(mu_plaquette, names, ("b", "c"), (wit[1], wit[2]))
    phi_ad_w = exp_phi(mu_plaquette, names, ("a", "d"), (wit[0], wit[3]))
    phi_ab = exp_phi(mu_plaquette, names, ("a", "b"), (wit[0], wit[1]))
    phi_bd = exp_phi(mu_plaquette, names, ("b", "d"), (wit[1], wit[3]))
    phi_bcd = exp_phi(mu_plaquette, names, ("b", "c", "d"), (wit[1], wit[2], wit[3]))
    phi_abcd = exp_phi(mu_plaquette, names, ("a", "b", "c", "d"), wit)
    print(f"witness {wit}: exp Phi_bc={phi_bc} (12/13), Phi_ab={phi_ab} (3), Phi_bd={phi_bd} (3/4)")
    print(f"  Phi_ad={phi_ad_w}, Phi_bcd={phi_bcd}, Phi_abcd={phi_abcd} (stated 1,1,1)")
    stated = {
        "Phi_bc": (phi_bc, F(12, 13)),
        "Phi_ab": (phi_ab, F(3, 1)),
        "Phi_bd": (phi_bd, F(3, 4)),
        "Phi_bcd": (phi_bcd, F(1, 1)),
        "Phi_abcd": (phi_abcd, F(1, 1)),
    }
    for name, (got, wantv) in stated.items():
        if got != wantv:
            hits.append(f"{name} at witness {got} != {wantv}")

    bad_ad = 0
    for cfg in product(VALS, repeat=4):
        if exp_phi(mu_plaquette, names, ("a", "d"), (cfg[0], cfg[3])) != 1:
            bad_ad += 1
    print(f"exp Phi_ad != 1 on {bad_ad} of {ncfg} (stated 0)")
    if bad_ad:
        hits.append(f"exp Phi_ad != 1 on {bad_ad}/1296 configs")

    # --- star embedding ---
    spts = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]  # x, l1, l2, l3
    sE = lattice_edges(spts)
    print(f"star embedding edges {sorted(sE)} (want the three spokes from origin)")
    if sE != {(0, 1), (0, 2), (0, 3)}:
        hits.append(f"star embedding not a 3-star: {sE}")
    # no plaquette: no 4-cycle
    if len(sE) != 3:
        hits.append("star is not a tree")
    swit = ("-x", "-x", "+y", VAC)  # leaves then dummy center for printing
    phi_lll = exp_phi(mu_star, ("l1", "l2", "l3", "x"), ("l1", "l2", "l3"), ("-x", "-x", "+y"))
    print(f"star leaves (-x,-x,+y): exp Phi={phi_lll} (165/169)")
    if phi_lll != F(165, 169):
        hits.append(f"star three-body {phi_lll} != 165/169")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (a) WITNESS REALIZABILITY; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (a) WITNESS REALIZABILITY; plaquette and 3-star embed in Z^3 with "
            "co-recorded pairs non-adjacent; T6 ratios 12/13, 3, 3/4, 165/169 and Phi_ad=1 on 1296 "
            "all match the formation-law canonical potential"
        )


if __name__ == "__main__":
    main()
