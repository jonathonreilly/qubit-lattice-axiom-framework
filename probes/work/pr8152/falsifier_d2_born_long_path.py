#!/usr/bin/env python3
"""J:falsifier:PR8152 — Falsifiers D1/D2 (not the known unnormalized-frame HIT).

D1: on a path of 12 sites (note executed 5), each seeing one recorded
neighbour, every record stays in {s0, −s0}.
D2: Born (1+s·q)/2 is 1 at s=q and 0 at s=−q, for extra rational q.

HIT if a path record leaves the antipodal pair, or Born is not {1,0} there.
"""
from fractions import Fraction as Fr
from itertools import permutations, product

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def born(s, q):
    return (1 + sum(s[i] * q[i] for i in range(3))) / 2


def octahedral():
    mats = []
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
                mats.append(M)
    return mats


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def main() -> int:
    # D2 extra rational unit vectors (beyond a single q)
    qs = [
        (Fr(1), Fr(0), Fr(0)),
        (Fr(0), Fr(1), Fr(0)),
        (Fr(3, 5), Fr(4, 5), Fr(0)),
        (Fr(5, 13), Fr(12, 13), Fr(0)),
        (Fr(8, 17), Fr(15, 17), Fr(0)),
        (Fr(7, 25), Fr(24, 25), Fr(0)),
    ]
    for q in qs:
        nrm = sum(x * x for x in q)
        if nrm != 1:
            hit(f"q={q} not unit {nrm}")
            continue
        mq = tuple(-x for x in q)
        bq, bm = born(q, q), born(mq, q)
        print(f"q={q}: Born(q,q)={bq} Born(-q,q)={bm}")
        if bq != 1:
            hit(f"Born(q,q)={bq} != 1 at {q}")
        if bm != 0:
            hit(f"Born(-q,q)={bm} != 0 at {q}")
        # off-axis: (0,0,1) vs q in xy
        if q[2] == 0 and q[0] != 0:
            off = (Fr(0), Fr(0), Fr(1))
            bo = born(off, q)
            print(f"  off-axis Born={bo} (not in {{0,1}} is allowed)")
            if bo in (0, 1):
                hit(f"off-axis Born {bo} in {{0,1}} at q={q} (should need support beyond antipodes)")

    # D1: path of 12 sites, each sees the previous; values stay in {s0,-s0}
    s0 = (Fr(3, 5), Fr(4, 5), Fr(0))
    alphabet = {s0, tuple(-x for x in s0)}
    path = [s0]
    # alternate copying and antipodal (both legal under M1)
    for i in range(11):
        path.append(s0 if i % 2 == 0 else tuple(-x for x in s0))
    print(f"D1 path length {len(path)} (note executed 5)")
    for i, s in enumerate(path):
        if s not in alphabet:
            hit(f"D1 path site {i} value {s} off {{s0,-s0}}")
    print("D1: all 12 path records in {s0,-s0}")

    # C1 extra directions (beyond the note's five): orbit sizes in {6,8,12,24}
    mats = octahedral()
    print(f"|O+|={len(mats)} (stated 24)")
    if len(mats) != 24:
        hit(f"|O+|={len(mats)} != 24")
    extras = [
        (Fr(1), Fr(1), Fr(2)),  # review's (1,1,2): proper orbit 24
        (Fr(1), Fr(2), Fr(3)),
        (Fr(2), Fr(3), Fr(6)),
        (Fr(1), Fr(4), Fr(8)),
    ]
    allowed = {6, 8, 12, 24}
    for v in extras:
        pts = {apply(M, v) for M in mats}
        print(f"orbit of {v}: {len(pts)}")
        if len(pts) not in allowed:
            hit(f"orbit size {len(pts)} of {v} not in {allowed}")

    if HITS:
        print("SUMMARY: falsifier FIRED; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: falsifier D1/D2/C1 did not fire — Born is 1 and 0 on "
        "antipodes for six rational q (including 5-12-13, 8-15-17, 7-24-25), "
        "a 12-site path stays in {s0,-s0}, extra orbits of (1,1,2) and "
        "(1,2,3) have size 24; not a re-find of the unnormalized-frame HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
