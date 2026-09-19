#!/usr/bin/env python3
"""J:attack-a:PR8142 — six-axis menu and exceptional-point isolating intervals exist.

The note's objects: 6 Bloch axes, 216 triples, positive octant, t* in (4,5),
rho in (6,7), sextic roots in (1,2) and (6,7), declared triples (3,1,2) and
(5,2,4). HIT if the menu is not 6 distinct unit axes, 6^3!=216, a stated
isolating interval has no sign change, or a declared triple is not positive.
"""
from __future__ import annotations


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def ct(t):
    return t ** 3 - 3 * t ** 2 - 6 * t - 1


def cr(x):
    return x ** 3 - 3 * x ** 2 - 15 * x - 19


def s(x):
    return x ** 6 - 6 * x ** 5 - 3 * x ** 4 + 4 * x ** 3 - 3 * x ** 2 - 6 * x + 31


def main():
    hits = []
    if len(set(AXES)) != 6:
        hits.append("HIT: six-axis menu is not 6 distinct axes")
        print(hits[-1])
    if any(sum(a[i] ** 2 for i in range(3)) != 1 for a in AXES):
        hits.append("HIT: an axis is not a unit vector")
        print(hits[-1])
    if 6 ** 3 != 216:
        hits.append("HIT: 6^3 != 216")
        print(hits[-1])
    print(f"menu |A|={len(AXES)} triples={6 ** 3}")

    if not (ct(4) < 0 < ct(5)):
        hits.append(f"HIT: t* isolating interval (4,5) has no sign change ct(4)={ct(4)} ct(5)={ct(5)}")
        print(hits[-1])
    else:
        print(f"t* in (4,5): ct(4)={ct(4)} ct(5)={ct(5)}")
    if not (cr(6) < 0 < cr(7)):
        hits.append(f"HIT: rho isolating interval (6,7) has no sign change")
        print(hits[-1])
    else:
        print(f"rho in (6,7): cr(6)={cr(6)} cr(7)={cr(7)}")
    if not (s(1) > 0 and s(2) < 0):
        hits.append("HIT: sextic has no sign change on (1,2)")
        print(hits[-1])
    else:
        print(f"sextic (1,2): s(1)={s(1)} s(2)={s(2)}")
    if not (s(6) < 0 and s(7) > 0):
        hits.append("HIT: sextic has no sign change on (6,7)")
        print(hits[-1])
    else:
        print(f"sextic (6,7): s(6)={s(6)} s(7)={s(7)}")

    for pqr in ((3, 1, 2), (5, 2, 4)):
        if any(x <= 0 for x in pqr):
            hits.append(f"HIT: declared triple {pqr} is not positive")
            print(hits[-1])
        else:
            print(f"declared triple {pqr} is in the positive octant")

    if hits:
        print("SUMMARY: a stated menu object or isolating interval does not exist")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the six-axis menu has 6 "
        "unit axes and 216 triples, t* in (4,5), rho in (6,7), sextic roots in "
        "(1,2) and (6,7) by integer sign changes, and (3,1,2),(5,2,4) lie in the "
        "positive octant"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
