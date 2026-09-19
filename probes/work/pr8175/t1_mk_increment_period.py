#!/usr/bin/env python3
"""J:attack-g:PR8175 — brute-force T1.1 M_k increment and T1.3 period arithmetic.

T1.1: M_k(z)=z_k-τ(z)/3; amplified v with direction j satisfies
M_k(v-e_j)-M_k(v)=1/3-δ_{jk}; processed Excuse_k(v) (winning-pair member
with index ≠ k) always gives +1/3. Enumerated on a box × all directions
and all winning pairs.

T1.3: fork-free (b,a,e)=(0,0,3) has r=1; (2,2,1) has r=-1; sum (r,e,a)=(0,4,2)
and (e-3r)/a=2. W1 log as written sums to E=16, |A|=10, F=0 with two periods.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def tau(z):
    return z[0] + z[1] + z[2]


def M(k, z):
    return Fr(z[k]) - Fr(tau(z), 3)


def sub(z, e):
    return (z[0] - e[0], z[1] - e[1], z[2] - e[2])


def main() -> int:
    box = range(-2, 5)
    for v in itertools.product(box, box, box):
        if sum(M(k, v) for k in range(3)) != 0:
            return hits(f"sum_k M_k({v}) != 0")
        for j in range(3):
            w = sub(v, E[j])
            for k in range(3):
                dlt = Fr(1, 3) - (1 if j == k else 0)
                got = M(k, w) - M(k, v)
                if got != dlt:
                    return hits(
                        f"amplified increment at v={v} j={j} k={k}: {got} != {dlt}"
                    )
        # processed: every 2-subset of predecessors is a possible winning pair
        for pair in itertools.combinations(range(3), 2):
            for k in range(3):
                if k not in pair:
                    idx = min(pair)  # "the smaller if both" (neither is k)
                else:
                    idx = pair[0] if pair[1] == k else pair[1]
                if idx == k:
                    return hits(f"Excuse_k used direction k at pair={pair} k={k}")
                w = sub(v, E[idx])
                got = M(k, w) - M(k, v)
                if got != Fr(1, 3):
                    return hits(
                        f"processed increment at v={v} pair={pair} k={k}: {got} != 1/3"
                    )
    print("T1.1 M_k increments on box [-2,5)^3 × directions/pairs: True")

    def rise(b):
        return 1 - b  # T1.2 fork-free

    r1, e1, a1, b1 = rise(0), 3, 0, 0
    r2, e2, a2, b2 = rise(2), 1, 2, 2
    if (r1, e1, a1, b1) != (1, 3, 0, 0):
        return hits("three-processed fork-free tuple is not (r,e,a,b)=(1,3,0,0)")
    if (r2, e2, a2, b2) != (-1, 1, 2, 2):
        return hits("two-bad fork-free tuple is not (r,e,a,b)=(-1,1,2,2)")
    r, e, a = r1 + r2, e1 + e2, a1 + a2
    print(f"period sum (r,e,a)=({r},{e},{a})")
    if (r, e, a) != (0, 4, 2):
        return hits(f"period sum {(r, e, a)} != (0,4,2)")
    ratio = Fr(e - 3 * r, a)
    print(f"(e-3r)/a = {ratio}")
    if ratio != 2:
        return hits(f"period ratio {ratio} != 2")

    # equality cases of e <= 3r+2a at fork-free integer (b,a,e)
    eq = []
    sharper_fail = []
    for b, aa, ee in itertools.product(range(0, 4), range(0, 4), range(0, 4)):
        if b > aa or ee + aa > 3:
            continue
        rr = 1 - b
        if ee > 3 * rr + 2 * aa:
            return hits(f"e <= 3r+2a fails at (b,a,e)={(b, aa, ee)}")
        if ee == 3 * rr + 2 * aa:
            eq.append((b, aa, ee))
        if ee > 3 * rr + aa:
            sharper_fail.append((b, aa, ee))
    stated = {(1, 1, 2), (2, 2, 1), (3, 3, 0)}
    print(f"e=3r+2a equality cases: {eq}")
    print(f"sharper e<=3r+a failures: {sharper_fail}")
    if not stated.issubset(set(eq)):
        return hits(f"stated equality cases missing from e=3r+2a census {eq}")
    if not stated.issubset(set(sharper_fail)):
        return hits(f"stated triples are not all sharper failures: {sharper_fail}")

    # W1 log (b, kept, a, e) as written
    log = [
        (0, 1, 0, 1),
        (1, 2, 1, 1),
        (0, 2, 0, 2),
        (1, 3, 1, 2),
        (0, 3, 0, 3),
        (2, 3, 2, 1),
        (0, 3, 0, 3),
        (2, 3, 2, 1),
        (1, 3, 1, 2),
        (3, 3, 3, 0),
    ]
    sr = se = sa = sb = 0
    nperiod = 0
    for i, (b, kept, aa, ee) in enumerate(log):
        if aa + ee > 3 or b > aa or kept > 3:
            return hits(f"W1 log row {i} violates e+a<=3 or b<=a: {(b, kept, aa, ee)}")
        sr += 1 - b
        se += ee
        sa += aa
        sb += b
        if i + 1 < len(log):
            if (b, aa, ee) == (0, 0, 3) and log[i + 1][0] == 2 and log[i + 1][2:] == (2, 1):
                nperiod += 1
    print(f"W1 log sums r={sr} E={se} |A|={sa} b={sb} periods={nperiod}")
    if (sr, se, sa, sb, nperiod) != (0, 16, 10, 10, 2):
        return hits("W1 log does not sum to (r,E,|A|,b,periods)=(0,16,10,10,2)")
    # ratios as stated
    for name, E_, A_, S_, claimed in (
        ("W1", 16, 10, 1, Fr(8, 5)),
        ("W2", 20, 12, 1, Fr(5, 3)),
        ("W3", 23, 12, 2, Fr(5, 3)),
    ):
        rat = Fr(E_ - 3 * (S_ - 1), A_)
        b30 = E_ <= 3 * (S_ - 1) + 2 * A_
        sharp = E_ <= 3 * (S_ - 1) + A_
        print(f"{name} ratio {rat} block30={b30} sharper={sharp}")
        if rat != claimed:
            return hits(f"{name} ratio {rat} != {claimed}")
        if not b30 or sharp:
            return hits(f"{name} does not sit inside block 30 and outside the sharper budget")

    print(
        "SUMMARY: pattern has no purchase on this note: T1.1 M_k increments hold "
        "on the enumerated box, T1.3 period sums to (0,4,2) with ratio 2, the "
        "three stated (b,a,e) triples are e=3r+2a equalities and sharper failures, "
        "and the stated W1 log / witness ratios match"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
