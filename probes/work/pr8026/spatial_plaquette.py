#!/usr/bin/env python3
"""J:attack-a:PR8026 — pattern (a) WITNESS REALIZABILITY.

A spatial plaquette of area 1 exists in Z^3 (xy-plane 4-cycle). Z^3 NN
has no triangles.
"""
from __future__ import annotations

HITS = []


def nn(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3)) == 1


def main():
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    ok = all(nn(plaq[i], plaq[(i + 1) % 4]) for i in range(4))
    print(f"spatial plaquette {plaq} 4-cycle? {ok}")
    if not ok:
        HITS.append("plaquette")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - an area-1 spatial "
        "plaquette exists as a 4-cycle in a coordinate plane of Z^3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
