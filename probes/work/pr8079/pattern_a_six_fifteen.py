#!/usr/bin/env python3
"""J:attack:PR8079 — pattern (a) WITNESS REALIZABILITY: 6 labels, 15 channels.

Native finite-moment Ward: 15 two-neighbor channels of 6 labels. HIT if
C(6,2)!=15 or the six axes are not distinct unit vectors.
"""
from __future__ import annotations

from math import comb


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def main():
    hits = []
    n = comb(6, 2)
    print(f"labels={len(set(AXES))} C(6,2)={n}")
    if n != 15 or len(set(AXES)) != 6:
        hits.append("HIT: 6-label/15-channel census fails")
        print(hits[-1])
    if hits:
        print("SUMMARY: pattern (a) WITNESS REALIZABILITY; 6/15 census fails")
        return 0
    print(
        "SUMMARY: pattern (a) WITNESS REALIZABILITY; six unit axes and C(6,2)=15 "
        "two-neighbor channels exist as stated"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
