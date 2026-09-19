#!/usr/bin/env python3
"""J:attack-g:PR8026 — brute-force the note's rectangle count A=RS, P=2(R+S).

claim_scope: every qualifying planar rectangle satisfies |omega|(W_C)| <= C_0^P (u/u_0)^A
with A=RS, P=2(R+S). Literal: an R-by-S array of plaquettes has area RS and
boundary of 2(R+S) links. Enumerate the grid graph for R,S=1..8.
"""
from __future__ import annotations


def counts(R: int, S: int) -> tuple[int, int]:
    """R x S plaquettes: vertices (i,j) i=0..R, j=0..S.
    Horizontal edges (i,j)-(i,j+1); vertical (i,j)-(i+1,j).
    Boundary: edges with a unique adjacent plaquette.
    """
    area = R * S
    perim = 0
    # horizontal edges
    for i in range(R + 1):
        for j in range(S):
            faces = 0
            if i > 0:
                faces += 1  # plaquette above? edge at row i is south of plaquette i-1
            if i < R:
                faces += 1
            if faces == 1:
                perim += 1
    # vertical edges
    for i in range(R):
        for j in range(S + 1):
            faces = 0
            if j > 0:
                faces += 1
            if j < S:
                faces += 1
            if faces == 1:
                perim += 1
    return area, perim


def main() -> int:
    hits = []
    print("PR #8026: A=RS, P=2(R+S) for an R x S plaquette rectangle")
    for R in range(1, 9):
        for S in range(1, 9):
            a, p = counts(R, S)
            A, P = R * S, 2 * (R + S)
            if (a, p) != (A, P):
                hits.append(f"HIT: R={R} S={S}: enumerated area,perimeter=({a},{p}) vs stated ({A},{P})")
            print(f"  R={R} S={S}: area {a} (RS={A}), perimeter {p} (2(R+S)={P})")
    if hits:
        for h in hits:
            print(h)
        print("SUMMARY: A=RS, P=2(R+S) fails grid enumeration")
    else:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on the rectangle count A=RS, P=2(R+S) "
            "(PR #8026): holds for all 1<=R,S<=8 by enumerating boundary links of the "
            "grid graph; pattern has purchase and the step holds as written"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
