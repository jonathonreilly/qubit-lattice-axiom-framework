#!/usr/bin/env python3
"""J:falsifier:PR8175 — independent check of T1.3 two-level period and T3 floor.

HIT if the period pair does not sum to (r,e,a)=(0,4,2) with (e-3r)/a=2,
or if max t(4/27-t) is not 4/729, or if d3 does not cross 4/729 between 367 and 368.
"""
from fractions import Fraction

# T1.2: fork-free rise r = 1-b.
# three processed poles: b=0, r=1, e=3, a=0
# two bad amplified + one processed: b=2, r=-1, e=1, a=2


def d3_p12(p: int) -> Fraction:
    return Fraction(2 * p + 11, p * p + 2 * p + 11)


def main() -> None:
    hits = []
    r1, e1, a1, b1 = 1, 3, 0, 0
    r2, e2, a2, b2 = -1, 1, 2, 2
    if r1 != 1 - b1 or r2 != 1 - b2:
        hits.append("rise r != 1-b on a fork-free refinement")
    r, e, a = r1 + r2, e1 + e2, a1 + a2
    print(f"period sum (r,e,a)=({r},{e},{a})")
    if (r, e, a) != (0, 4, 2):
        hits.append(f"period sum {r,e,a} != (0,4,2)")
    ratio = Fraction(e - 3 * r, a)
    print(f"(e-3r)/a = {ratio}")
    if ratio != 2:
        hits.append(f"period ratio {ratio} != 2")
    # W1/W2/W3 claimed ratios
    w1 = Fraction(16 - 0, 10)  # E=16, |S|=1, |A|=10
    w2 = Fraction(20 - 0, 12)
    w3 = Fraction(23 - 3, 12)  # |S|=2 => 3(|S|-1)=3
    print(f"W1 ratio {w1} (claimed 8/5={Fraction(8,5)})")
    print(f"W2 ratio {w2} (claimed 5/3={Fraction(5,3)})")
    print(f"W3 ratio {w3} (claimed 5/3={Fraction(5,3)})")
    if w1 != Fraction(8, 5) or w2 != Fraction(5, 3) or w3 != Fraction(5, 3):
        hits.append("witness ratios from the stated (E,A,S) disagree with 8/5, 5/3, 5/3")
    # sharper budget vs block 30 budget on those counts
    for name, E, A, S in (("W1", 16, 10, 1), ("W2", 20, 12, 1), ("W3", 23, 12, 2)):
        sharp = 3 * (S - 1) + A
        proved = 3 * (S - 1) + 2 * A
        print(f"{name}: E={E} sharp {E}<={sharp} is {E <= sharp}; proved {E}<={proved} is {E <= proved}")
        if E <= sharp:
            hits.append(f"{name} satisfies the sharper budget (refutation fails)")
        if E > proved:
            hits.append(f"{name} exceeds block 30's proved budget")
    t_star = Fraction(2, 27)
    f_star = t_star * (Fraction(4, 27) - t_star)
    if f_star != Fraction(4, 729):
        hits.append(f"max t(4/27-t)={f_star} != 4/729")
    lo, hi = d3_p12(367), d3_p12(368)
    bound = Fraction(4, 729)
    if not (lo > bound > hi):
        hits.append(f"d3 crossing not 367/368: {lo} vs {bound} vs {hi}")
    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: PR8175 period/floor falsifier FIRED:", "; ".join(hits))
    else:
        print(
            "SUMMARY: PR8175 period/floor falsifier did not fire: "
            "period (r,e,a)=(0,4,2) ratio 2; W1/W2/W3 ratios 8/5,5/3,5/3 "
            "inside proved budget and outside sharper; d3 crosses 4/729 at 367/368"
        )


if __name__ == "__main__":
    main()
