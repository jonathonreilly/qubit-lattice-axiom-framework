#!/usr/bin/env python3
"""J:attack:PR8169 — pattern (c) executed/exact masses on the four-point menu.

claim_scope: at t=0 with e^{2β}=2 the copy mass is 1/3 and the flip mass is 1/6;
Born (1+s·q)/2 on {q,q',-q,-q'} takes 1, 1/2, 0, 1/2 and sums to 2.
Exact Fraction. HIT if those values fail.
"""
from fractions import Fraction
from math import isclose


def main() -> None:
    hits = []
    # e^{2β}=2 => e^β = sqrt(2), e^{-β}=1/sqrt(2). Use sqrt(2) symbolically via squares.
    # α = e^β / (2e^β + 2e^{-β}) = 1 / (2 + 2 e^{-2β}) = 1/(2+1)=1/3
    e2b = Fraction(2)
    alpha = 1 / (2 + 2 / e2b)
    gamma = 1 / (2 + 2 * e2b)
    print(f"copy α={alpha} stated 1/3; flip γ={gamma} stated 1/6; 2α+2γ={2*alpha+2*gamma}")
    if alpha != Fraction(1, 3) or gamma != Fraction(1, 6):
        hits.append(f"Gibbs masses α={alpha} γ={gamma}")
    if 2 * alpha + 2 * gamma != 1:
        hits.append("2α+2γ != 1")

    # Born values on the four-point set at t=0: s·q is 1, t, -1, -t = 1,0,-1,0
    born = [Fraction(1 + t, 2) for t in (1, 0, -1, 0)]
    print(f"Born values {born} sum {sum(born)}")
    if born != [1, Fraction(1, 2), 0, Fraction(1, 2)]:
        hits.append(f"Born values {born}")
    if sum(born) != 2:
        hits.append(f"Born sum {sum(born)} != 2")

    # distinctness: |q·q'|<1
    if not (abs(0) < 1):
        hits.append("t=0 should be distinct")

    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS on four-point masses - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS on four-point masses - "
            "α=1/3, γ=1/6, Born (1,1/2,0,1/2) sums to 2; does not fire"
        )


if __name__ == "__main__":
    main()
