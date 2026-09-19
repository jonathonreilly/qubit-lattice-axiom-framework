#!/usr/bin/env python3
"""J:attack-g:PR8172 — brute-force T1 brackets, T2's polynomial, T3's kernel.

Do NOT recompute the known T2 island-ratio HIT (6671/1728 vs note 4.05).

T1: c = max TV of three-predecessor kernels over 216 triples and five
one-predecessor alternatives; 3c(37/10)=406962630/413162167<1,
3c(19/5)=871815/862244>1; ε=max(d1,d2,d3) with block-25 closed forms
holds at p=285718 and fails at 285717 vs 7/10^6.

T2 count (the proof's box, not the executed 4.05): |U| ≤ (D+1)(6D+5)(6D+4)/2
≤ 18(D+1)^3 with difference (D+1)(9D+8).

T3: 2(β/√3)^t 3^t = 2(√3 β)^t; p_t(n1,n2,n3)= t!/(n1!n2!n3! 3^t) sums to 1.

HIT if a stated exact identity fails. Exact Fraction / integer / sympy.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import factorial

import sympy as sp


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def neg(a):
    return (-a[0], -a[1], -a[2])


def phi(s, a, p, q, r):
    if s == a:
        return p
    if s == neg(a):
        return q
    return r


def rcond(s, pred, p, q, r):
    def w(ss):
        acc = 1
        for a in pred:
            acc *= phi(ss, a, p, q, r)
        return acc

    Z = sum(w(ss) for ss in AXES)
    return Fraction(w(s), Z)


def tv(P, Q):
    return sum(abs(P[s] - Q[s]) for s in AXES) / 2


def c_of(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    best = Fraction(0)
    for pred in product(AXES, repeat=3):
        P = {s: rcond(s, pred, p, q, r) for s in AXES}
        for i in range(3):
            for a2 in AXES:
                if a2 == pred[i]:
                    continue
                pred2 = list(pred)
                pred2[i] = a2
                Q = {s: rcond(s, tuple(pred2), p, q, r) for s in AXES}
                t = tv(P, Q)
                if t > best:
                    best = t
    return best


def eps(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = (q ** 3 + 4 * r ** 3) / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return max(d1, d2, d3), d1, d2, d3


def main():
    hits = []

    c37 = c_of(Fraction(37, 10), 1, 2)
    three_c37 = 3 * c37
    want37 = Fraction(406962630, 413162167)
    print(f"3c(37/10)={three_c37}")
    if three_c37 != want37:
        hits.append(f"HIT: 3c(37/10)={three_c37} != {want37}")
        print(hits[-1])
    if not (three_c37 < 1):
        hits.append(f"HIT: 3c(37/10) is not <1: {three_c37}")
        print(hits[-1])

    c19 = c_of(Fraction(19, 5), 1, 2)
    three_c19 = 3 * c19
    want19 = Fraction(871815, 862244)
    print(f"3c(19/5)={three_c19}")
    if three_c19 != want19:
        hits.append(f"HIT: 3c(19/5)={three_c19} != {want19}")
        print(hits[-1])
    if not (three_c19 > 1):
        hits.append(f"HIT: 3c(19/5) is not >1: {three_c19}")
        print(hits[-1])

    thresh = Fraction(7, 10 ** 6)
    e_ok, *ds_ok = eps(285718, 1, 2)
    e_fail, *ds_fail = eps(285717, 1, 2)
    print(f"eps(285718)={e_ok} vs 7/10^6={thresh} <= {e_ok <= thresh}")
    print(f"eps(285717)={e_fail} vs 7/10^6={thresh} <= {e_fail <= thresh}")
    print(f"d's at 285718: {ds_ok}")
    if not (e_ok <= thresh):
        hits.append(f"HIT: eps(285718)={e_ok} > 7/10^6")
        print(hits[-1])
    if e_fail <= thresh:
        hits.append(f"HIT: eps(285717)={e_fail} <= 7/10^6 (stated to fail)")
        print(hits[-1])

    # T2 polynomial identity
    D = sp.symbols("D", integer=True, nonnegative=True)
    box = (D + 1) * (6 * D + 5) * (6 * D + 4) / 2
    eighteen = 18 * (D + 1) ** 3
    diff = sp.simplify(eighteen - box)
    want_diff = (D + 1) * (9 * D + 8)
    print(f"18(D+1)^3 - (D+1)(6D+5)(6D+4)/2 = {diff}")
    if sp.expand(diff - want_diff) != 0:
        hits.append(f"HIT: T2 polynomial difference {diff} != (D+1)(9D+8)")
        print(hits[-1])
    for d in range(0, 40):
        b = (d + 1) * (6 * d + 5) * (6 * d + 4) // 2
        e18 = 18 * (d + 1) ** 3
        dd = (d + 1) * (9 * d + 8)
        if e18 - b != dd or b > e18:
            hits.append(f"HIT: T2 poly at D={d}: box={b} 18={e18} diff={e18-b} want {dd}")
            print(hits[-1])
            break
    print("T2 polynomial D=0..39: box <= 18(D+1)^3 with difference (D+1)(9D+8)")

    # T3 kernel identity
    b, t = sp.symbols("beta t", positive=True)
    left = 2 * (b / sp.sqrt(3)) ** t * 3 ** t
    right = 2 * (sp.sqrt(3) * b) ** t
    if sp.simplify(left - right) != 0:
        hits.append(f"HIT: T3 2(beta/sqrt3)^t 3^t != 2(sqrt3 beta)^t")
        print(hits[-1])
    else:
        print("T3: 2(β/√3)^t 3^t = 2(√3 β)^t")
    for tt in range(0, 8):
        tot = 0
        for n1 in range(tt + 1):
            for n2 in range(tt - n1 + 1):
                n3 = tt - n1 - n2
                tot += factorial(tt) // (factorial(n1) * factorial(n2) * factorial(n3))
        if tot != 3 ** tt:
            hits.append(f"HIT: level-walk multinomials at t={tt} sum {tot} != 3^{tt}")
            print(hits[-1])
    print("p_t multinomials sum to 1 for t=0..7")

    if hits:
        print("SUMMARY: T1 brackets, T2 polynomial or T3 kernel identity fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known island-ratio HIT "
        "— T1 3c(37/10)=406962630/413162167<1 and 3c(19/5)=871815/862244>1 by exact TV "
        "over 216×5 kernels, ε(285718,1,2)<=7/10^6<ε(285717), T2's box identity "
        "(D+1)(6D+5)(6D+4)/2 + (D+1)(9D+8) = 18(D+1)^3, and T3's "
        "2(β/√3)^t 3^t=2(√3 β)^t with p_t summing to 1, all hold literally"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
