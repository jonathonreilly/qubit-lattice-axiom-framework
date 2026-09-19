#!/usr/bin/env python3
"""J:attack-a:PR8137 — pattern (a) WITNESS REALIZABILITY.

A three-site NN path L—M—R exists in Z^3 (collinear or L-shape). Z^3 is
bipartite. Two-point menu {+,-} exists. Six-axis orbit of size 6 exists.
"""
from __future__ import annotations

HITS = []


def nn(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3)) == 1


def main():
    collinear = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    ell = [(0, 0, 0), (1, 0, 0), (1, 1, 0)]
    for name, p in (("collinear", collinear), ("L", ell)):
        ok = nn(p[0], p[1]) and nn(p[1], p[2]) and not nn(p[0], p[2])
        print(f"{name} path {p} NN-path-of-3? {ok}")
        if not ok:
            HITS.append(name)
    print("two-point menu {+,-}; six-axis orbit size 6")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - collinear and L-shaped "
        "three-site NN paths exist in Z^3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
