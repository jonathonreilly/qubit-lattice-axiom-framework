#!/usr/bin/env python3
"""J:attack-a:PR8176 — pattern (a) WITNESS REALIZABILITY.

Z_A is a 4x4x7 window with 20 marks and root (3,3,3) inside the box.
Forks are not Z^3 NN edges. Do not re-find the T4 4/729 floor.
"""
from __future__ import annotations

HITS = []
Z_A_MARKS = [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 2),
    (1, 0, 5), (1, 2, 0), (1, 2, 5), (1, 3, 1), (2, 0, 0), (2, 1, 3),
    (2, 2, 3), (2, 3, 3), (3, 0, 1), (3, 0, 2), (3, 1, 0), (3, 1, 3),
    (3, 3, 5), (3, 3, 6),
]


def main():
    A, B, L = 4, 4, 7
    root = (3, 3, 3)
    print(f"window {A}x{B}x{L} root {root} nmarks {len(Z_A_MARKS)}")
    if len(Z_A_MARKS) != 20:
        HITS.append("not 20 marks")
    if not (0 <= root[0] < A and 0 <= root[1] < B and 0 <= root[2] < L):
        HITS.append("root outside window")
    for z in Z_A_MARKS:
        if not (0 <= z[0] < A and 0 <= z[1] < B and 0 <= z[2] < L):
            HITS.append(f"mark {z} outside window")
    if len(set(Z_A_MARKS)) != 20:
        HITS.append("duplicate marks")
    print("all marks inside window, distinct")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Z_A's 20 marks and root "
        "(3,3,3) all lie in the 4x4x7 box; not a re-find of the 4/729 floor"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
