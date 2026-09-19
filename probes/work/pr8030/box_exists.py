#!/usr/bin/env python3
"""J:attack-a:PR8030 — pattern (a) WITNESS REALIZABILITY.

A finite cubic box in Z^3 exists; NN graph is triangle-free.
"""
from __future__ import annotations

HITS = []


def main():
    L = 2
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    print(f"box [0,{L})^3 has {len(sites)} sites (stated 8 for L=2)")
    if len(sites) != L**3:
        HITS.append("box count")
    # no NN triangles
    nn = lambda a, b: sum(abs(a[i] - b[i]) for i in range(3)) == 1
    tri = False
    for i, a in enumerate(sites):
        for b in sites[i + 1 :]:
            if not nn(a, b):
                continue
            for c in sites:
                if c == a or c == b:
                    continue
                if nn(a, c) and nn(b, c):
                    tri = True
    print(f"NN triangle in box? {tri}")
    if tri:
        HITS.append("triangle")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - a finite cubic box "
        "exists in Z^3 and its NN graph is triangle-free"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
