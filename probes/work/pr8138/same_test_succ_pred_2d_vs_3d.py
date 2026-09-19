#!/usr/bin/env python3
"""J:attack-b:PR8138 — same successor/predecessor-triple test in 2D vs 3D.

Q2: in 2D the two successors of a plaquette's first corner are the two
predecessors of its last corner; in 3D a successor triple is never a
predecessor triple. Same test: exists x,y with sorted(succ(x))=sorted(pred(y)).

HIT if 3D has a match or 2D has none.
"""
from __future__ import annotations

from itertools import product


def pred(x, d):
    return tuple(sorted(tuple(x[j] - (1 if j == i else 0) for j in range(d)) for i in range(d)))


def succ(x, d):
    return tuple(sorted(tuple(x[j] + (1 if j == i else 0) for j in range(d)) for i in range(d)))


def matches(d, box=range(-1, 4)):
    sites = list(product(*([box] * d)))
    P, S = {}, {}
    for y in sites:
        P.setdefault(pred(y, d), []).append(y)
        S.setdefault(succ(y, d), []).append(y)
    keys = set(P) & set(S)
    return [(S[k], P[k], k) for k in keys]


def main():
    hits = []
    m2 = matches(2)
    m3 = matches(3)
    print(f"2D matches {len(m2)} example {m2[:1]}")
    print(f"3D matches {len(m3)} example {m3[:1]}")
    if not m2:
        hits.append("HIT: 2D has no successor=predecessor pair (the plaquette identity fails)")
        print(hits[-1])
    if m3:
        hits.append(f"HIT: 3D has successor=predecessor triples {m3[:2]}")
        print(hits[-1])
    if hits:
        print("SUMMARY: 2D vs 3D successor/predecessor test fails to separate as stated")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the same successor=predecessor "
        "set test has matches on Z^2 (plaquette telescoping) and none on Z^3, as Q2 states"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
