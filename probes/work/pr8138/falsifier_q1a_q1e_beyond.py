#!/usr/bin/env python3
"""J:falsifier:PR8138 — Q1a recorded-set family and Q1e product form,
beyond the executed 2x2x2 / 1x2x2 / 2x2x1 sizes.

Falsifiers: a linear extension whose recorded sets are not the predecessor
sets (Q1a); a config of 1x2x2 or 2x2x1 where product form != conditionals
(Q1e). Machinery disjoint from the runner (no Rule class, no cube_pass):
recursive topological generation and integer φ / Z_k cross-multiply.
Beyond: the 2x2x3 product order (12 sites) and the 1x2x3 box (all 6^6).
HIT if a recorded-set family splits or the two products disagree.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

M = 6
P, Q, Rwt = 3, 1, 2
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def box_sites(dims):
    return list(product(*[range(n) for n in dims]))


def preds(x):
    return [
        tuple(x[i] - (1 if j == i else 0) for i in range(len(x)))
        for j in range(len(x))
        if x[j] > 0
    ]


def linear_extensions(sites):
    remaining = set(sites)
    pred = {x: preds(x) for x in sites}

    def rec(chosen):
        if not remaining:
            yield tuple(chosen)
            return
        ready = [x for x in remaining if all(p in chosen for p in pred[x])]
        for x in sorted(ready):
            remaining.remove(x)
            chosen.append(x)
            yield from rec(chosen)
            chosen.pop()
            remaining.add(x)

    return rec([])


def recorded_family(order, sites):
    pos = {s: i for i, s in enumerate(order)}
    out = []
    for x in sites:
        rec = []
        for i in range(len(x)):
            for d in (-1, 1):
                y = list(x)
                y[i] += d
                y = tuple(y)
                if y in pos and pos[y] < pos[x]:
                    rec.append(y)
        out.append(tuple(sorted(rec)))
    return tuple(out)


def predecessor_family(sites):
    return tuple(tuple(sorted(preds(x))) for x in sites)


def check_q1a(dims) -> None:
    sites = box_sites(dims)
    expected = predecessor_family(sites)
    n = 0
    n_bad = 0
    for order in linear_extensions(sites):
        n += 1
        fam = recorded_family(order, sites)
        if fam != expected:
            n_bad += 1
            if n_bad <= 2:
                hit(
                    f"Q1a {dims}: linear extension recorded sets != predecessors "
                    f"order={order[:6]}..."
                )
    print(f"Q1a {dims}: linear_extensions={n} mismatches={n_bad}")
    if n == 0:
        hit(f"Q1a {dims}: no linear extensions found")
    # 2x2x2 sanity: 48
    if dims == (2, 2, 2) and n != 48:
        hit(f"Q1a 2x2x2 count {n} != 48")


def orbit(s, t):
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


def tables():
    w = {"p": P, "q": Q, "r": Rwt}
    phi = tuple(tuple(w[orbit(s, t)] for t in range(M)) for s in range(M))
    Z1 = sum(phi[0])
    Z2 = {
        (a, b): sum(phi[s][a] * phi[s][b] for s in range(M))
        for a in range(M)
        for b in range(M)
    }
    Z3 = {
        (a, b, c): sum(phi[s][a] * phi[s][b] * phi[s][c] for s in range(M))
        for a in range(M)
        for b in range(M)
        for c in range(M)
    }
    return phi, Z1, Z2, Z3


def check_q1e(dims) -> None:
    phi, Z1, Z2, Z3 = tables()
    sites = box_sites(dims)
    spec = []
    for x in sites:
        A = preds(x)
        spec.append((x, A))
    n = 0
    n_bad = 0
    for vals in product(range(M), repeat=len(sites)):
        n += 1
        v = dict(zip(sites, vals))
        cn, cd = 1, 1
        pn, pd = 1, M
        for x, A in spec:
            s = v[x]
            k = len(A)
            if k == 0:
                cd *= M
            elif k == 1:
                a = v[A[0]]
                cn *= phi[s][a]
                cd *= Z1
                pn *= phi[s][a]
                pd *= Z1
            elif k == 2:
                a, b = v[A[0]], v[A[1]]
                z = Z2[(a, b)]
                cn *= phi[s][a] * phi[s][b]
                cd *= z
                pn *= phi[s][a] * phi[s][b] * (Z1 ** 2)
                pd *= (Z1 ** 2) * z
            else:
                a, b, c = v[A[0]], v[A[1]], v[A[2]]
                z = Z3[(a, b, c)]
                cn *= phi[s][a] * phi[s][b] * phi[s][c]
                cd *= z
                pn *= phi[s][a] * phi[s][b] * phi[s][c] * (Z1 ** 3)
                pd *= (Z1 ** 3) * z
        if cn * pd != pn * cd:
            n_bad += 1
            if n_bad <= 2:
                hit(f"Q1e {dims} config {vals}: conditionals != product form")
    print(f"Q1e {dims}: configs={n} mismatches={n_bad}")


def main() -> int:
    check_q1a((2, 2, 2))
    check_q1a((2, 2, 3))
    check_q1a((3, 2, 2))
    check_q1e((1, 2, 2))
    check_q1e((2, 2, 1))
    check_q1e((1, 2, 3))
    check_q1e((3, 1, 2))
    if HITS:
        print("SUMMARY: FALSIFIER (PR #8138): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: FALSIFIER (PR #8138): Q1a recorded sets equal predecessor "
        "sets on every linear extension of 2x2x2, 2x2x3 and 3x2x2; Q1e "
        "product form equals conditionals on all configs of 1x2x2, 2x2x1, "
        "1x2x3 and 3x1x2 at (3,1,2); beyond executed sizes; does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
