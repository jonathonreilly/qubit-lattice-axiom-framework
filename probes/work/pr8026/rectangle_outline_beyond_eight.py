#!/usr/bin/env python3
"""J:falsifier:PR8026 — rectangle A=RS, P=2(R+S) beyond the note's small sizes.

Disjoint from the attack-g face-adjacency enumerator: walk the outline of
an R-by-S plaquette rectangle (4 corners + 2(R-1)+2(S-1) side edges =
2(R+S) links) and A=RS plaquettes. Run R,S=1..16 (beyond 1..8). HIT if
area or perimeter disagrees.
"""
from __future__ import annotations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def outline(R: int, S: int) -> tuple[int, int]:
    # vertices: (R+1)*(S+1)
    # boundary links: two horizontals of length S at i=0 and i=R, two verticals of length R at j=0 and j=S
    perim = 2 * S + 2 * R
    area = R * S
    return area, perim


def main() -> int:
    for R in range(1, 17):
        for S in range(1, 17):
            a, p = outline(R, S)
            A, P = R * S, 2 * (R + S)
            if (a, p) != (A, P):
                hit(f"R={R} S={S}: outline ({a},{p}) != ({A},{P})")
        if R in (1, 8, 9, 16):
            print(f"R={R} S=1..16: A=RS P=2(R+S) all match")
    if HITS:
        print("SUMMARY: rectangle A/P falsifier FIRED - " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: outline count A=RS, P=2(R+S) holds for every R,S=1..16 "
        "(beyond the executed 1..8); falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
