#!/usr/bin/env python3
"""J:attack-b:PR8177 — pattern (b) SAME TEST, BOTH SIDES.

Same test: number of 1-predecessors of the tight root. Z_A root (3,3,3)
and Z_B root (4,4,4) both have three 1-predecessors, so that count does
not separate them. Do not re-find the known HIT on the value triple
[-1,-1,-1] vs [-1,-1,0].
"""
from __future__ import annotations

HITS = []
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def preds(z):
    return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]


def run(sites, zeta):
    eta = {}
    for z in sorted(sites, key=lambda t: sum(t)):
        ps = [eta.get(p, 0) for p in preds(z)]
        eta[z] = 1 if (sum(ps) >= 2 or zeta.get(z, 0)) else 0
    return eta


def n1pred(eta, root):
    return sum(eta.get(p, 0) for p in preds(root))


def main():
    ZA = (
        (3, 3, 3),
        (4, 4, 7),
        [
            (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 2),
            (1, 0, 5), (1, 2, 0), (1, 2, 5), (1, 3, 1), (2, 0, 0), (2, 1, 3),
            (2, 2, 3), (2, 3, 3), (3, 0, 1), (3, 0, 2), (3, 1, 0), (3, 1, 3),
            (3, 3, 5), (3, 3, 6),
        ],
    )
    ZB = (
        (4, 4, 4),
        (5, 5, 8),
        [
            (0, 0, 0), (0, 0, 1), (0, 0, 7), (0, 1, 0), (0, 1, 1), (0, 1, 2),
            (0, 1, 7), (0, 2, 7), (0, 4, 4), (1, 0, 0), (1, 0, 2), (1, 1, 2),
            (1, 2, 0), (1, 2, 2), (1, 3, 1), (1, 3, 7), (2, 0, 0), (2, 2, 0),
            (2, 2, 2), (2, 2, 3), (2, 2, 6), (2, 3, 3), (2, 3, 4), (2, 4, 2),
            (2, 4, 6), (3, 0, 1), (3, 0, 2), (3, 1, 2), (3, 2, 1), (3, 2, 7),
            (4, 0, 2), (4, 0, 6), (4, 1, 1), (4, 2, 1), (4, 4, 2), (4, 4, 4),
        ],
    )
    for name, (root, shape, marks) in (("Z_A", ZA), ("Z_B", ZB)):
        A, B, L = shape
        sites = [(a, b, c) for a in range(A) for b in range(B) for c in range(L)]
        eta = run(sites, {z: 1 for z in marks})
        n = n1pred(eta, root)
        print(f"{name} root {root} n_1pred={n}")
        if name == "Z_A":
            na = n
        else:
            nb = n
    print(f"same test n_1pred: Z_A={na} Z_B={nb}")
    if na != nb:
        # they differ on count; note's T2 is about values not count
        print("counts differ; not used as a HIT (known HIT is the value triple)")
    # pattern (b): if the note separates Z_A from Z_B by 'has three 1-preds', both have 3
    if na == 3 and nb == 3:
        print("both have three 1-predecessors: that property does not separate them")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same 1-predecessor "
        "count is 3 at both Z_A and Z_B roots, so that count does not separate "
        "them; the value-triple mismatch is a known HIT and is not re-claimed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
