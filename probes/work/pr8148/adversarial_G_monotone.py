#!/usr/bin/env python3
"""J:attack-e:PR8148 — pattern (e) SAMPLED EVIDENCE.

Not the known R3 uniform-distance HIT (1/216, 56059/3369600).

R4: no covariant rate law reaches the static law on a plaquette, because
G(p,d)=(1-p)d/6 + p d^2/36 is strictly increasing in d>0 for every p in [0,1].
The note executes four explicit laws rather than sampling p. Adversarial
grid over p in [0,1] and extra (p,q,r) with (p-q)^2>0, looking for
G(p,d_anti)-G(p,d_same)<=0. HIT if a clock parameter in range flattens G.
"""
from __future__ import annotations

from fractions import Fraction as Fr

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def N2(a_kind: str, p, q, r):
    if a_kind == "same":
        return p * p + q * q + 4 * r * r
    if a_kind == "anti":
        return 2 * p * q + 4 * r * r
    return 2 * r * (p + q + r)


def d_of(kind, p, q, r):
    z1 = p + q + 4 * r
    return Fr(z1 * z1, N2(kind, p, q, r))


def G(pv, d):
    return (1 - pv) * d / 6 + pv * (d * d) / 36


def main() -> int:
    triples = [
        (3, 1, 2),
        (5, 2, 4),
        (10, 1, 2),
        (4, 1, 1),
        (7, 3, 5),
        (Fr(5, 2), Fr(1, 3), Fr(7, 4)),
    ]
    pgrid = [Fr(i, 20) for i in range(21)]  # 0, 1/20, ..., 1
    ncheck = 0
    for p, q, r in triples:
        if (p - q) ** 2 == 0:
            continue
        ds, da = d_of("same", p, q, r), d_of("anti", p, q, r)
        print(f"(p,q,r)=({p},{q},{r}) d_same={ds} d_anti={da} da>ds {da > ds}")
        if not (da > ds):
            hit(f"d_anti<=d_same at ({p},{q},{r})")
            continue
        for pv in pgrid:
            gap = G(pv, da) - G(pv, ds)
            ncheck += 1
            if gap <= 0:
                hit(f"G not increasing at clock p={pv} triple=({p},{q},{r}) gap={gap}")
                break
        else:
            # endpoints and a midpoint already in the grid
            print(f"  G(·,d_anti)-G(·,d_same)>0 on {len(pgrid)} values of p including 0 and 1")
    print(f"checked {ncheck} (clock p, triple) pairs")

    # algebraic: bracket (1-p)/6 + p(d1+d2)/36 > 0 for p in [0,1], d>0
    psym = Fr(1, 2)
    d1, d2 = Fr(72, 13), Fr(72, 11)
    br = (1 - psym) / 6 + psym * (d1 + d2) / 36
    print(f"bracket at p=1/2, (3,1,2) d's: {br} >0 {br > 0}")
    if br <= 0:
        hit("bracket nonpositive at p=1/2")

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - adversarial grid of "
        "clock p in [0,1] (21 values) at extra (p,q,r) never flattens "
        "G(p,d_anti)-G(p,d_same); R4's 'no rate law reaches static' is not a "
        "sampled never; not the known R3 uniform-distance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
