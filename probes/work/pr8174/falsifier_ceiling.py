#!/usr/bin/env python3
"""J:falsifier:PR8174 — independent exact check of T5 (E1–E2).

Recomputes max (v-1)/v^3 = 4/27, max t^2(4/27-t) = 256/531441, and
d_3(p,1,2) vs that bound at p=4150 and 4165.
"""
from fractions import Fraction


def d3_p12(p: int) -> Fraction:
    return Fraction(2 * p + 11, p * p + 2 * p + 11)


def main() -> None:
    hits = []
    v = Fraction(3, 2)
    m = (v - 1) / v**3
    if m != Fraction(4, 27):
        hits.append(f"(v-1)/v^3 at 3/2 = {m} != 4/27")
    for vv in (Fraction(1), Fraction(5, 4), Fraction(2), Fraction(5, 2), Fraction(4, 3)):
        val = (vv - 1) / vv**3
        if val > m:
            hits.append(f"v={vv} gives {val} > 4/27")
    t = Fraction(8, 81)
    g = t**2 * (Fraction(4, 27) - t)
    if g != Fraction(256, 531441):
        hits.append(f"t^2(4/27-t) at 8/81 = {g} != 256/531441")
    for tt in (Fraction(1, 27), Fraction(2, 27), Fraction(4, 27) / 3, Fraction(1, 10)):
        val = tt**2 * (Fraction(4, 27) - tt)
        if val > g:
            hits.append(f"t={tt} gives {val} > 256/531441")
    d_lo, d_hi = d3_p12(4150), d3_p12(4165)
    print(f"d3(4150,1,2) = {d_lo}")
    print(f"d3(4165,1,2) = {d_hi}")
    print(f"256/531441   = {Fraction(256, 531441)}")
    if d_lo != Fraction(8311, 17230811):
        hits.append(f"d3(4150) = {d_lo} != 8311/17230811")
    if d_hi != Fraction(8341, 17355566):
        hits.append(f"d3(4165) = {d_hi} != 8341/17355566")
    bound = Fraction(256, 531441)
    if not (d_lo > bound > d_hi):
        hits.append(f"ceiling crossing not 4150 > 256/531441 > 4165: {d_lo} vs {bound} vs {d_hi}")
    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: ceiling falsifier FIRED:", "; ".join(hits))
    else:
        print(
            "SUMMARY: ceiling falsifier did not fire: max (v-1)/v^3=4/27, "
            "max t^2(4/27-t)=256/531441, d3(4150)=8311/17230811 > bound > "
            "d3(4165)=8341/17355566"
        )


if __name__ == "__main__":
    main()
