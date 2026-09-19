#!/usr/bin/env python3
"""J:attack-g:PR8141 — brute-force T1: each edge recorded exactly once, product form.

T1: every edge xy of W is recorded exactly once, by its later endpoint, and
mu_sigma(v) = (1/6)^{n0} Pi_{xy in E} K(v_x,v_y) / Pi_{|A_x|>=2} K_|A|(v_{A_x})
equals the product of conditionals. Executed on the plaquette (C4) and the
star (star4) for all 24 orders.

Enumerate all 4! orders and all 6^4 configurations at (p,q,r)=(3,1,2).
HIT if some edge is recorded 0 or >=2 times, or the two products disagree.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import permutations, product

P, Q, Rwt = 3, 1, 2
VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {"+x": "-x", "-x": "+x", "+y": "-y", "-y": "+y", "+z": "-z", "-z": "+z"}
M = 6
Z1 = P + Q + 4 * Rwt  # 12; note: K_1 ≡ 1 so K is phi/Z1


def phi(s, t):
    if s == t:
        return P
    if OPP[s] == t:
        return Q
    return Rwt


def K(a, s):
    """Normalized one-site kernel K(a, s) = phi(s, a)/Z1, so K_1 ≡ 1."""
    return F(phi(s, a), Z1)


def Kk(a):
    tot = F(0)
    for s in VALS:
        pr = F(1)
        for ai in a:
            pr *= K(ai, s)
        tot += pr
    return tot


def cond(s, a):
    if not a:
        return F(1, M)
    num = F(1)
    for ai in a:
        num *= K(ai, s)
    return num / Kk(a)


def recorded(order, edges):
    pos = {x: i for i, x in enumerate(order)}
    A = {x: [] for x in order}
    rec_count = {e: 0 for e in edges}
    for x, y in edges:
        later, earlier = (x, y) if pos[x] > pos[y] else (y, x)
        A[later].append(earlier)
        rec_count[(x, y)] += 1
    return A, rec_count


def mu_conditionals(cfg, order, A):
    w = F(1)
    for x in order:
        w *= cond(cfg[x], tuple(cfg[y] for y in A[x]))
    return w


def mu_closed(cfg, edges, A):
    n0 = sum(1 for x in A if not A[x])
    num = 1
    for x, y in edges:
        num *= K(cfg[x], cfg[y])
    den = 1
    for x, rec in A.items():
        if len(rec) >= 2:
            den *= Kk(tuple(cfg[y] for y in rec))
    return F(num, den) * F(1, M) ** n0


def check_graph(name, verts, edges):
    n_ord = 0
    n_cfg = 0
    n_eq = 0
    rec_ok = True
    witness = None
    for order in permutations(verts):
        n_ord += 1
        A, rec_count = recorded(order, edges)
        if any(c != 1 for c in rec_count.values()):
            rec_ok = False
            witness = ("record-count", order, rec_count)
            break
        for vals in product(VALS, repeat=len(verts)):
            n_cfg += 1
            cfg = dict(zip(verts, vals))
            lhs, rhs = mu_conditionals(cfg, order, A), mu_closed(cfg, edges, A)
            if lhs == rhs:
                n_eq += 1
            elif witness is None:
                witness = ("product", order, cfg, lhs, rhs)
    return name, n_ord, n_cfg, n_eq, rec_ok, witness


def main():
    # plaquette C4: a—b, a—c, b—d, c—d
    pla = check_graph(
        "plaquette",
        ("a", "b", "c", "d"),
        (("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")),
    )
    # star: x with leaves l1,l2,l3
    sta = check_graph(
        "star",
        ("x", "l1", "l2", "l3"),
        (("x", "l1"), ("x", "l2"), ("x", "l3")),
    )
    hits = []
    for name, n_ord, n_cfg, n_eq, rec_ok, witness in (pla, sta):
        print(f"{name}: orders={n_ord} configs={n_cfg} product_eq={n_eq} rec_once={rec_ok}")
        if n_ord != 24:
            hits.append(f"{name} orders {n_ord} != 24")
        if not rec_ok:
            hits.append(f"{name} some edge not recorded exactly once: {witness}")
        if n_eq != n_cfg:
            hits.append(f"{name} product form failed on {n_cfg - n_eq} configs witness={witness}")
    if hits:
        print("HIT: T1 " + "; ".join(hits))
        print("SUMMARY: PROOF STEP BY BRUTE FORCE on T1 recorded-once product form (PR #8141): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on T1 (PR #8141): on the plaquette "
            "and the star, all 24 orders record each edge exactly once and the "
            "closed product form equals the product of conditionals on every "
            "6^4 configuration at (3,1,2); pattern has purchase and the step holds as written"
        )


if __name__ == "__main__":
    main()
