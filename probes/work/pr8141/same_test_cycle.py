#!/usr/bin/env python3
"""J:attack-b:PR8141 — pattern (b) SAME TEST, BOTH SIDES.

Same test: is the window a 4-cycle? Plaquette yes; 6-star no.
"""
from __future__ import annotations

HITS = []


def nn(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3)) == 1


def is_4cycle(sites):
    if len(sites) != 4:
        return False
    deg = [sum(nn(sites[i], sites[j]) for j in range(4) if j != i) for i in range(4)]
    return deg == [2, 2, 2, 2]


def main():
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    star = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    p4 = is_4cycle(plaq)
    s4 = is_4cycle(star)
    print(f"4-cycle test: plaquette={p4} star={s4}")
    if p4 == s4:
        HITS.append("4-cycle test does not separate plaquette from star")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same 4-cycle test "
        "holds for the plaquette and fails for the star"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
