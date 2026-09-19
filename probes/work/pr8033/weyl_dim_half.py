#!/usr/bin/env python3
"""J:attack-f:PR8033 — NORMALIZATION of SU(3) Weyl dim (p+1)(q+1)(p+q+2)/2.

R=1 carrier sum dim^2 = 19 uses this 1/2. HIT if the 1/2 is the wrong
factorial (e.g. /1 or /3) relative to dim(1,0)=3, dim(1,1)=8, dim(2,0)=6.
"""
from __future__ import annotations


def dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def main():
    hits = []
    known = {(0, 0): 1, (1, 0): 3, (0, 1): 3, (1, 1): 8, (2, 0): 6, (2, 1): 15}
    for pq, d in known.items():
        got = dim(*pq)
        print(f"dim{pq}={got} expected {d}")
        if got != d:
            hits.append(f"dim{pq}={got}!={d}")
    dH = sum(dim(p, q) ** 2 for p in range(2) for q in range(2 - p))
    print(f"R=1 dimH={dH} stated 19")
    if dH != 19:
        hits.append(f"R=1 dimH={dH}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: NORMALIZATION (PR #8033): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: NORMALIZATION of Weyl dim (p+1)(q+1)(p+q+2)/2 (PR #8033): "
            "dim(1,0)=3, dim(1,1)=8, dim(2,0)=6 and R=1 carrier 19; the 1/2 holds"
        )


if __name__ == "__main__":
    main()
