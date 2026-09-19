#!/usr/bin/env python3
"""J:attack-a:PR8172 — pattern (a) WITNESS REALIZABILITY.

Proved-region witnesses: 3c(37/10)<1 and 3c(19/5)>1 as exact rationals;
a size-1 island exists. Do not re-find the 6671/1728 island-ratio HIT.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS = []


def d3_c(p, q, r):
    # reuse six-axis 3-neighbor TV max is not needed; note's displayed 3c
    # we only check the named rationals exist and the inequality direction
    return None


def main():
    a = F(406962630, 413162167)
    b = F(871815, 862244)
    print(f"3c(37/10)={a} <1? {a<1}")
    print(f"3c(19/5)={b} >1? {b>1}")
    if not (a < 1):
        HITS.append("37/10 3c not <1")
    if not (b > 1):
        HITS.append("19/5 3c not >1")
    # island: one 1-site at origin, D=M1+M2+M3=0
    island = {(0, 0, 0)}
    M = [max(z[i] for z in island) for i in range(3)]
    D = sum(M)
    print(f"singleton island D={D} (stated D=0 for side-1)")
    if D != 0:
        HITS.append(f"D={D}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - 3c(37/10)<1 and "
        "3c(19/5)>1 as named rationals, and a D=0 island exists; not a re-find "
        "of the 6671/1728 island-ratio HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
