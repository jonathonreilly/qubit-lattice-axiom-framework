#!/usr/bin/env python3
"""J:attack-g:PR8024 — brute-force whole-group vs individual plaquette counts and Casimir floor.

Note: Lambda0={0,e1,e2,e3}; whole-group retains the three-plaquette group at x
iff x+Lambda0 ⊂ Lambda={0,...,L-1}^3, hence 3(L-1)^3 plaquettes; individual
cell support retains 3L(L-1)^2; difference 3(L-1)^2; at L=2 the counts are 3
and 6. Casimir C(p,q)=(2/3)(p²+pq+q²+3p+3q) ≥ 4 for every nonzero label,
equality only at (1,0) and (0,1).

HIT if a count, the difference identity, or the Casimir floor fails.
Exact integers / Fraction. Do not redo the existing loop-witness script.
"""
from __future__ import annotations

from itertools import product
from fractions import Fraction


E = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def in_lambda(x, L):
    return all(0 <= c < L for c in x)


def whole_group_anchors(L):
    out = []
    for x in product(range(L), repeat=3):
        if all(in_lambda(add(x, d), L) for d in E):
            out.append(x)
    return out


def individual_plaquettes(L):
    # W_(x,ij) uses cells {x, x+ei, x+ej}
    dirs = ((0, 1), (0, 2), (1, 2))
    ei = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    out = []
    for x in product(range(L), repeat=3):
        for i, j in dirs:
            cells = (x, add(x, ei[i]), add(x, ei[j]))
            if all(in_lambda(c, L) for c in cells):
                out.append((x, i, j))
    return out


def C(p, q):
    return Fraction(2, 3) * (p * p + p * q + q * q + 3 * p + 3 * q)


def main():
    hits = []
    for L in range(1, 9):
        anchors = whole_group_anchors(L)
        n_wg = 3 * len(anchors)
        n_ind = len(individual_plaquettes(L))
        want_wg = 3 * (L - 1) ** 3
        want_ind = 3 * L * (L - 1) ** 2
        diff = n_ind - n_wg
        want_diff = 3 * (L - 1) ** 2
        print(f"L={L}: whole-group {n_wg} (want {want_wg}), individual {n_ind} (want {want_ind}), diff {diff} (want {want_diff})")
        if n_wg != want_wg:
            hits.append(f"HIT: whole-group count L={L}: {n_wg} != {want_wg}")
            print(hits[-1])
        if n_ind != want_ind:
            hits.append(f"HIT: individual count L={L}: {n_ind} != {want_ind}")
            print(hits[-1])
        if diff != want_diff:
            hits.append(f"HIT: difference L={L}: {diff} != {want_diff}")
            print(hits[-1])
        if L == 2 and (n_wg, n_ind) != (3, 6):
            hits.append(f"HIT: L=2 counts {n_wg},{n_ind} != 3,6")
            print(hits[-1])

    # "this polynomial is at least 4, equality only at (1,0),(0,1)"
    # C(p,q)=(2/3)(p²+pq+q²+3p+3q); the unscaled quadratic is E's numerator.
    quad = lambda p, q: p * p + p * q + q * q + 3 * p + 3 * q
    print(f"C(1,0)={C(1, 0)} C(0,1)={C(0, 1)} quad(1,0)={quad(1, 0)}")
    if C(1, 0) != 4:
        hits.append(
            f"HIT: stated C(p,q)=(2/3)(p^2+pq+q^2+3p+3q) 'at least 4 with equality "
            f"only at (1,0) and (0,1)' fails: C(1,0)={C(1, 0)} != 4 "
            f"(the unscaled quadratic equals 4; E=(quad)/a = 4/a)"
        )
        print(hits[-1])
    eq_q, below_q = [], []
    for pp, qq in product(range(0, 21), repeat=2):
        if (pp, qq) == (0, 0):
            continue
        val = quad(pp, qq)
        if val < 4:
            below_q.append(((pp, qq), val))
        if val == 4:
            eq_q.append((pp, qq))
    print(f"unscaled quadratic =4 at {eq_q}; <4 {below_q}")
    if set(eq_q) != {(1, 0), (0, 1)} or below_q:
        hits.append(f"HIT: unscaled quadratic floor fails eq={eq_q} below={below_q}")
        print(hits[-1])
    # strictly increasing under either increment
    inc_ok = True
    for p, q in product(range(0, 15), repeat=2):
        if C(p + 1, q) <= C(p, q) or C(p, q + 1) <= C(p, q):
            inc_ok = False
            hits.append(f"HIT: Casimir not strictly increasing at {(p, q)}")
            print(hits[-1])
            break
    print(f"Casimir strictly increasing in each coordinate: {inc_ok}")

    if hits:
        print(
            "SUMMARY: whole-group vs individual plaquette counts hold on L=1..8, but "
            "the stated Casimir floor C>=4 with equality at (1,0),(0,1) fails: "
            "C(1,0)=C(0,1)=8/3; the unscaled quadratic in E is 4 at those labels"
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — whole-group vs individual "
        "plaquette counts 3(L-1)^3 vs 3L(L-1)^2 (difference 3(L-1)^2; L=2 gives 3 vs 6) "
        "hold by enumeration on L=1..8, and the energy polynomial is >=4 for every "
        "nonzero label in {0..20}^2 with equality only at (1,0) and (0,1)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
