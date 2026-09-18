#!/usr/bin/env python3
"""J:falsifier:PR8176 — independent exact check of T4.2 floor (E2).

Recomputes d_3(p,1,2) from the six-axis one-site kernel and the claimed
one-variable maximum 4/729. A HIT fires if the crossing is not between
p=367 and p=368, or if max_t t(4/27-t) is not 4/729.
Machinery: fractions only; no import of the note's runner.
"""
from fractions import Fraction

# Six-axis menu: φ = p (equal), q (antipodal), r (orthogonal).
# K(a|a,a,b) for b ⊥ a, q=1, r=2:
#   Z = p²r + q²r + r²p + r²q + 2 r³
#   K = p² r / Z
#   d_3 = 1-K = (2p+11)/(p²+2p+11) at (p,1,2).


def d3_p12(p: int) -> Fraction:
    return Fraction(2 * p + 11, p * p + 2 * p + 11)


def main() -> None:
    hits = []
    # max of f(t)=t(4/27-t) on (0,4/27): vertex at t=2/27, value 4/729.
    t_star = Fraction(2, 27)
    f_star = t_star * (Fraction(4, 27) - t_star)
    if f_star != Fraction(4, 729):
        hits.append(f"max t(4/27-t) = {f_star} != 4/729")
    # sample a few other t to confirm not larger
    for t in (Fraction(1, 27), Fraction(3, 27), Fraction(1, 10), Fraction(4, 27) / 2):
        val = t * (Fraction(4, 27) - t)
        if val > f_star:
            hits.append(f"t={t} gives {val} > 4/729")
    lo, hi = d3_p12(367), d3_p12(368)
    bound = Fraction(4, 729)
    print(f"d3(367,1,2) = {lo} = {float(lo):.12f}")
    print(f"d3(368,1,2) = {hi} = {float(hi):.12f}")
    print(f"4/729         = {bound} = {float(bound):.12f}")
    print(f"745/135434 vs cache: {lo == Fraction(745, 135434)}")
    print(f"747/136171 vs cache: {hi == Fraction(747, 136171)}")
    if not (lo > bound > hi):
        hits.append(f"crossing not 367>4/729>368: {lo} vs {bound} vs {hi}")
    if lo != Fraction(745, 135434) or hi != Fraction(747, 136171):
        hits.append("closed-form d3 disagrees with the note's displayed fractions")
    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: floor falsifier FIRED:", "; ".join(hits))
    else:
        print(
            "SUMMARY: floor falsifier did not fire: max t(4/27-t)=4/729 exactly, "
            "d3(367)=745/135434 > 4/729 > d3(368)=747/136171"
        )


if __name__ == "__main__":
    main()
