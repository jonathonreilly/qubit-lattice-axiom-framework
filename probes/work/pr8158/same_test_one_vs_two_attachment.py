#!/usr/bin/env python3
"""J:attack-b:PR8158 — same constancy test on one- vs two-attachment factors.

Do not re-find the known Q4(a) triangle HIT.

Q2 vs Q3: one-attachment F_C is constant; two-attachment is not (unless p=q=r).
Apply the identical test: is F invariant under the covariance group / equal
for all boundary values? Exact six-axis product at (3,1,2) and (1,1,1).

HIT if the same test does not separate one-attachment from two-attachment
at a nonconstant rule, or separates them at p=q=r.
"""
from __future__ import annotations

from itertools import product
from fractions import Fraction


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def F_pendant(vb, p, q, r):
    return sum(phi(vb, u, p, q, r) for u in AXES)


def F_bridge(vx, vy, p, q, r):
    return sum(phi(vx, u, p, q, r) * phi(u, vy, p, q, r) for u in AXES)


def is_constant(vals):
    return len(set(vals)) == 1


def main():
    hits = []
    for pqr in ((3, 1, 2), (5, 2, 4), (1, 1, 1), (2, 2, 2)):
        p, q, r = (Fraction(x) for x in pqr)
        pend = [F_pendant(vb, p, q, r) for vb in AXES]
        bridge = [F_bridge(vx, vy, p, q, r) for vx, vy in product(AXES, repeat=2)]
        pc, bc = is_constant(pend), is_constant(bridge)
        print(
            f"{pqr}: pendant constant={pc} value={pend[0] if pc else set(pend)}; "
            f"bridge constant={bc} nvals={len(set(bridge))}"
        )
        nonconst_rule = not (p == q == r)
        if nonconst_rule:
            if pc == bc:
                hits.append(
                    f"HIT: same constancy test does not separate one- vs two-attachment at {pqr}: "
                    f"pendant={pc} bridge={bc}"
                )
                print(hits[-1])
            if not pc:
                hits.append(f"HIT: pendant (one-attachment) is not constant at {pqr}")
                print(hits[-1])
            if bc:
                hits.append(f"HIT: bridge (two-attachment) is constant at nonconstant {pqr}")
                print(hits[-1])
        else:
            if not pc or not bc:
                hits.append(
                    f"HIT: at p=q=r={pqr} a factor is nonconstant: pendant={pc} bridge={bc}"
                )
                print(hits[-1])
    if hits:
        print("SUMMARY: one- vs two-attachment constancy test fails to separate as stated")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known Q4(a) triangle "
        "HIT — the same constancy test on F_C separates one-attachment (constant at "
        "every triple) from two-attachment (nonconstant iff not p=q=r) at (3,1,2), "
        "(5,2,4) and the constant rule"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
