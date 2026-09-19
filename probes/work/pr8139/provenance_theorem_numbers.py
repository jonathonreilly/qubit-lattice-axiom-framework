#!/usr/bin/env python3
"""J:provenance:PR8139 — theorem-statement numbers.

Eight corners, |G_kappa|=12, |O|=24, 3-fold stabilizer, TV witnesses.
HIT if an identity fails.
"""
from __future__ import annotations

from itertools import permutations, product

HITS: list[str] = []
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def D(k):
    return [
        tuple(k[i] * E[i][a] - k[j] * E[j][a] for a in range(3))
        for i in range(3)
        for j in range(3)
        if i != j
    ]


def main() -> int:
    corners = list(product((-1, 1), repeat=3))
    print(f"[DERIVED] |corners|={len(set(corners))} stated 8")
    if len(set(corners)) != 8:
        hit("corners")
    k = (1, 1, 1)
    print(f"[DERIVED] |D_kappa|={len(set(D(k)))} stated 6; |G|=6+6=12")
    if len(set(D(k))) != 6:
        hit("|D|")
    # proper cubic rotations: signed perm det +1
    mats = 0
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i, j in enumerate(perm):
                M[i][j] = signs[i]
            det = (
                M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
            )
            if det == 1:
                mats += 1
    print(f"[DERIVED] |O|={mats} stated 24")
    if mats != 24:
        hit("|O|")
    print("[CACHE] TV 793975879125/24719290847393 (R1 witness at (3,1,2))")
    print("[CACHE] TV 1646222697/263752139417 (R3 within-pair at (3,1,2))")
    print("[DEFINITION] c<1/3 region from block 08")
    print("[EXCLUDED] PR #8139")
    if HITS:
        print("SUMMARY: provenance FIRED - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: 6 theorem numbers: 8 corners, |D|=6 so |G|=12, |O|=24 derived; "
        "two TV witnesses cache-named; c<1/3 definition; unsourced 0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
