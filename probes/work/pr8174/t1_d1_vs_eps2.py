#!/usr/bin/env python3
"""J:attack-g:PR8174 — brute-force T1(a): d1 ≤ max(d2, d3) for all positive (p,q,r).

T1(a) states the three deviations have the closed forms of the front matter,
are strictly decreasing in p, and d1 ≤ max(d2, d3). The T1(b) coupling then
sets max(d1,d2,d3) = ε2 := max(d2,d3) when exactly one η'-predecessor is 1
(possible with all three formation-predecessors equal to a, because η' can
seed independently of ξ).

HIT if the closed forms disagree with the six-axis kernel, or if any positive
triple has d1 > max(d2,d3). Exact Fraction.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
A = AXES[0]
MA = AXES[1]
B = AXES[2]


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def K(s, pred, p, q, r):
    def w(ss):
        acc = 1
        for t in pred:
            acc *= phi(ss, t, p, q, r)
        return acc

    Z = sum(w(ss) for ss in AXES)
    return Fraction(w(s), Z)


def closed(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def from_kernel(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - K(A, (A, A, A), p, q, r)
    d2 = 1 - K(A, (A, A, MA), p, q, r)
    d3 = 1 - K(A, (A, A, B), p, q, r)
    return d1, d2, d3


def main():
    hits = []
    samples = [
        (3, 1, 2),
        (5, 2, 4),
        (4165, 1, 2),
        (2085, 1, 1),
        (8330, 2, 4),
        (6247, 1, 3),
        (1, 1, 1),
        (1, 2, 1),
        (1, 2, 2),
        (2, 5, 1),
        (10, 1, 2),
    ]
    for pqr in samples:
        c, k = closed(*pqr), from_kernel(*pqr)
        if c != k:
            hits.append(f"HIT: closed forms != kernel at {pqr}: {c} vs {k}")
            print(hits[-1])
        else:
            print(f"closed=kernel {pqr}: d1={c[0]} d2={c[1]} d3={c[2]} max23={max(c[1], c[2])}")
        if c[0] > max(c[1], c[2]):
            hits.append(
                f"HIT: T1(a) d1 <= max(d2,d3) fails at (p,q,r)={pqr}: "
                f"d1={c[0]} d2={c[1]} d3={c[2]} max(d2,d3)={max(c[1], c[2])}"
            )
            print(hits[-1])

    # exhaustive small positive integers
    n_fail = 0
    examples = []
    for p, q, r in product(range(1, 8), repeat=3):
        d1, d2, d3 = closed(p, q, r)
        if d1 > max(d2, d3):
            n_fail += 1
            if len(examples) < 6:
                examples.append(((p, q, r), d1, d2, d3))
    print(f"positive integer triples p,q,r in 1..7 with d1>max(d2,d3): {n_fail}")
    for ex in examples:
        print("  example", ex)

    # T2.2 increment identity (sanity; not the HIT)
    def M(k, z):
        return Fraction(z[k]) - Fraction(sum(z), 3)

    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    v = (4, 1, 2)
    inc_ok = True
    for j in range(3):
        w = (v[0] - e[j][0], v[1] - e[j][1], v[2] - e[j][2])
        for k in range(3):
            want = Fraction(1, 3) - (1 if j == k else 0)
            if M(k, w) - M(k, v) != want:
                inc_ok = False
                hits.append(f"HIT: amplified excuse increment at j={j} k={k}")
                print(hits[-1])
    print(f"T2.2 amplified increment 1/3-delta_jk: {inc_ok}")

    if hits:
        print(
            "SUMMARY: T1(a) 'd1 <= max(d2,d3)' fails at (1,2,1): d1=12/13 > 9/10=max(d2,d3) "
            f"(and at {n_fail} integer triples with coordinates 1..7); closed forms match "
            "the kernel; the T1(b) identification max(d1,d2,d3)=ε2=max(d2,d3) is therefore false "
            "for general positive weights"
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — T1 closed forms match the kernel "
        "and d1<=max(d2,d3) on the sampled triples"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
