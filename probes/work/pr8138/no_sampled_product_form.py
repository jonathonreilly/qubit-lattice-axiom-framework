#!/usr/bin/env python3
"""J:attack-e:PR8138 — SAMPLED EVIDENCE.

B5 executes the Q1e product-form identity on every config of the 1x2x2 and
2x2x1 boxes, but only on a 2000-draw LCG sample of the 2x2x2 cube (6^8 =
1679616). The identity is proved by regrouping; the sample is the only
'observed on random configs' check.

Instead of more samples: exhaustive integer comparison of
  (1/6) Π_edges K / Π K_2 / Π K_3
against the product of conditionals on every configuration of those boxes
and of the cube, at (3,1,2) and the constant rule (2,2,2). HIT if any
disagree. Not a never/always conjecture; a defect is a config where the
two expressions differ.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd

M = 6


def orbit_type(s: int, t: int) -> str:
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


def tables(tr):
    p, q, r = tr
    w = {"p": p, "q": q, "r": r}
    phi = tuple(tuple(w[orbit_type(s, t)] for t in range(M)) for s in range(M))
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


def box_sites(dims):
    return list(product(*[range(n) for n in dims]))


def preds(x):
    return [
        tuple(x[i] - (1 if j == i else 0) for i in range(len(x)))
        for j in range(len(x))
        if x[j] > 0
    ]


def both_frac(phi, Z1, Z2, Z3, sites, vals):
    v = dict(zip(sites, vals))
    # product of conditionals as Fraction
    cond = Fraction(1)
    for x in sites:
        A = preds(x)
        s = v[x]
        k = len(A)
        if k == 0:
            cond *= Fraction(1, M)
        elif k == 1:
            a = v[A[0]]
            cond *= Fraction(phi[s][a], Z1)
        elif k == 2:
            a, b = v[A[0]], v[A[1]]
            cond *= Fraction(phi[s][a] * phi[s][b], Z2[(a, b)])
        else:
            a, b, c = v[A[0]], v[A[1]], v[A[2]]
            cond *= Fraction(phi[s][a] * phi[s][b] * phi[s][c], Z3[(a, b, c)])
    # product form
    pf = Fraction(1, M)
    for x in sites:
        A = preds(x)
        s = v[x]
        for y in A:
            pf *= Fraction(phi[s][v[y]], Z1)
        if len(A) == 2:
            a, b = v[A[0]], v[A[1]]
            pf /= Fraction(Z2[(a, b)], Z1 ** 2)
        elif len(A) == 3:
            a, b, c = v[A[0]], v[A[1]], v[A[2]]
            pf /= Fraction(Z3[(a, b, c)], Z1 ** 3)
    return cond, pf


def exhaustive_small(tr, dims):
    phi, Z1, Z2, Z3 = tables(tr)
    sites = box_sites(dims)
    n = 0
    bad = None
    for vals in product(range(M), repeat=len(sites)):
        n += 1
        c, p = both_frac(phi, Z1, Z2, Z3, sites, vals)
        if c != p:
            bad = (vals, c, p)
            break
    return n, bad


def exhaustive_cube_int(tr):
    """All 6^8 cube configs; integer cross-multiply of the two expressions."""
    phi, Z1, Z2, Z3 = tables(tr)
    sites = box_sites((2, 2, 2))
    # precompute per-site predecessor index lists
    idx = {s: i for i, s in enumerate(sites)}
    spec = []
    for x in sites:
        A = preds(x)
        spec.append((idx[x], tuple(idx[y] for y in A)))
    n = 0
    bad = None
    for vals in product(range(M), repeat=8):
        n += 1
        # conditionals: num/den
        cn = 1
        cd = 1
        # product form: start 1/M, times phi/Z1 per edge, times Z1^k / Zk for k=2,3
        pn = 1
        pd = M
        for ix, A in spec:
            s = vals[ix]
            k = len(A)
            if k == 0:
                cd *= M
            elif k == 1:
                a = vals[A[0]]
                cn *= phi[s][a]
                cd *= Z1
                pn *= phi[s][a]
                pd *= Z1
            elif k == 2:
                a, b = vals[A[0]], vals[A[1]]
                z = Z2[(a, b)]
                cn *= phi[s][a] * phi[s][b]
                cd *= z
                pn *= phi[s][a] * phi[s][b] * (Z1 ** 2)
                pd *= (Z1 ** 2) * z
            else:
                a, b, c = vals[A[0]], vals[A[1]], vals[A[2]]
                z = Z3[(a, b, c)]
                cn *= phi[s][a] * phi[s][b] * phi[s][c]
                cd *= z
                pn *= phi[s][a] * phi[s][b] * phi[s][c] * (Z1 ** 3)
                pd *= (Z1 ** 3) * z
        # cn/cd == pn/pd  iff cn*pd == pn*cd
        if cn * pd != pn * cd:
            bad = vals
            break
        if n % 400000 == 0:
            print(f"  cube {tr} scanned {n}")
    return n, bad


def main() -> int:
    hits = []
    for tr in ((3, 1, 2), (2, 2, 2)):
        for dims in ((1, 2, 2), (2, 2, 1), (2, 1, 2)):
            n, bad = exhaustive_small(tr, dims)
            print(f"box {dims} at {tr}: {n} configs, mismatch={bad is not None}")
            if bad is not None:
                msg = f"product form != conditionals on {dims} at {tr} vals={bad[0]}"
                hits.append(msg)
                print("HIT:", msg)
        n, bad = exhaustive_cube_int(tr)
        print(f"cube 2x2x2 at {tr}: {n} configs, mismatch={bad is not None}")
        if bad is not None:
            msg = f"product form != conditionals on cube at {tr} vals={bad}"
            hits.append(msg)
            print("HIT:", msg)

    if hits:
        print("SUMMARY: SAMPLED EVIDENCE (PR #8138): " + "; ".join(hits[:3]))
        return 0
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8138): B5's 2000-draw cube sample is an "
        "executed check of a proved product-form identity; exhaustive integer "
        "comparison agrees on all 6^4 configs of 1x2x2, 2x2x1, 2x1x2 and all "
        "6^8 cube configs at (3,1,2) and (2,2,2); the load-bearing 'never' "
        "(successor triple vs predecessor triple) is proved not sampled; "
        "pattern has purchase and does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
