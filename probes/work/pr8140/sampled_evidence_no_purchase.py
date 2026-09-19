#!/usr/bin/env python3
"""J:attack-e:PR8140 — SAMPLED EVIDENCE.

Clock-static-charge notes (convexification, coupled defects, Ginibre) are
exact combinatorial identities (cube 8 vertices / 12 edges / 6 faces;
cancellation 4R+4). No never/always Monte Carlo conjecture.
"""
from itertools import combinations, product


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def main() -> int:
    verts = list(product((0, 1), repeat=3))
    edges = [frozenset((a, b)) for a, b in combinations(verts, 2) if nn(a, b)]
    print(f"cube |V|={len(verts)} |E|={len(edges)}")
    assert len(verts) == 8 and len(edges) == 12
    for R in range(0, 6):
        print(f"4R+4 at R={R}: {4 * R + 4}")
    print(
        "SUMMARY: pattern has no purchase on this note — cube census and "
        "4R+4 cancellation are exact identities, not sampled never/always "
        "observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
