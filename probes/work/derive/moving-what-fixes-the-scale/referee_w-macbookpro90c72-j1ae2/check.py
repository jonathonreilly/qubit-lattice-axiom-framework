#!/usr/bin/env python3
"""Referee for moving-what-fixes-the-scale a1.

Author w-jonathonsmac4f50-j882f (claude-opus-5). Own enumeration of the six axes.
The logged sums are (p**2+q**2+4*r**2)/6, (p*q+2*r**2)/3 and r*(p+q+r)/3.
"""
from fractions import Fraction as Fr
import sympy as sp

AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def kind(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return {1: "eq", -1: "op"}.get(dot, "or")


def omega(a, b, p, q, r):
    return {"eq": p, "op": q, "or": r}[kind(a, b)]


def readings():
    p, q, r = sp.symbols("p q r", positive=True)
    S = p + q + 4 * r
    c0 = 6 / S
    geo = (p * q * r ** 4) ** (-sp.Rational(1, 6))
    harm = (1 / p + 1 / q + 4 / r) / 6
    closed = sp.Integer(2) ** sp.Rational(1, 3) * sp.Integer(3) ** sp.Rational(5, 6) / 6
    sub = {p: 3, q: 1, r: 2}
    at = {
        "arith": sp.simplify(c0.subs(sub)),
        "geo": sp.simplify(geo.subs(sub)),
        "harm": sp.simplify(harm.subs(sub)),
        "same": sp.simplify((1 / p).subs(sub)),
    }
    row = all(sp.simplify(sum(omega(a, b, p, q, r) for a in AX) - S) == 0 for b in AX)
    sixth = {
        "arith": Fr(1, 2) ** 6,
        "geo": Fr(1, 48),
        "harm": Fr(5, 9) ** 6,
        "same": Fr(1, 3) ** 6,
    }
    ok = row and sp.simplify(geo.subs(sub) - closed) == 0
    ok &= at["arith"] == sp.Rational(1, 2) and at["harm"] == sp.Rational(5, 9) and at["same"] == sp.Rational(1, 3)
    ok &= len(set(sixth.values())) == 4
    report(
        "four readings",
        bool(ok),
        "at (3,1,2) the scales are 1/2, 2^(1/3)*3^(5/6)/6, 5/9 and 1/3; each sixth power differs",
    )


def branches():
    p, q, r = sp.symbols("p q r", positive=True)
    forms = {
        "eq": (p ** 2 + q ** 2 + 4 * r ** 2) / 6,
        "op": (p * q + 2 * r ** 2) / 3,
        "or": r * (p + q + r) / 3,
    }
    counts = {"eq": 0, "op": 0, "or": 0}
    match = True
    for s1 in AX:
        for s2 in AX:
            k = kind(s1, s2)
            counts[k] += 1
            got = sp.simplify(sum(omega(a, s1, p, q, r) * omega(a, s2, p, q, r) for a in AX) / 6)
            match &= sp.simplify(got - forms[k]) == 0
    gap_q = sp.factor(sp.together(forms["eq"] - forms["op"]))
    gap_r = sp.factor(sp.together(forms["eq"].subs(q, p) - forms["or"].subs(q, p)))
    sub = {p: 3, q: 1, r: 2}
    vals = [sp.simplify(forms[k].subs(sub)) for k in ("eq", "op", "or")]
    iso = all(sp.simplify(forms[k].subs({q: p, r: p}) - p ** 2) == 0 for k in forms)
    ok = match and counts == {"eq": 6, "op": 6, "or": 24}
    ok &= gap_q == (p - q) ** 2 / 6 and gap_r == (p - r) ** 2 / 3 and iso
    ok &= vals == [sp.Rational(13, 3), sp.Rational(11, 3), sp.Integer(4)]
    report(
        "two-neighbour branches",
        bool(ok),
        "36 pairs give 13/3, 11/3 and 4 at (3,1,2); the branches meet for every pair only at p=q=r, where each sum is p^2",
    )


def normalizer():
    p, q, r, c = sp.symbols("p q r c", positive=True)
    S = p + q + 4 * r
    c0 = 6 / S
    per = all(
        sp.simplify(sum(omega(a, s, p, q, r) for s in AX) - S) == 0 for a in AX
    )
    # k=2: average of sum_a c^2 omega(a,s1) omega(a,s2) over the 36 neighbour pairs
    acc = sum(
        sum(omega(a, s1, p, q, r) * omega(a, s2, p, q, r) for a in AX)
        for s1 in AX
        for s2 in AX
    )
    avg2 = sp.simplify(c ** 2 * acc / 36)
    claimed = sp.simplify(6 * (c * S / 6) ** 2)
    ratio = sp.simplify((avg2 / 6).subs(c, 2 * c0))
    # pointwise Z at c0 on (3,1,2), and the isotropic point where it is 6 for every pair
    sub = {p: 3, q: 1, r: 2}
    zvals = []
    for s2, tag in ((AX[0], "eq"), (AX[1], "op"), (AX[2], "or")):
        z = sp.simplify(
            sum(omega(a, AX[0], p, q, r) * omega(a, s2, p, q, r) for a in AX) * c0 ** 2
        )
        zvals.append(sp.simplify(z.subs(sub)))
    iso_z = sp.simplify(
        sum(omega(a, AX[0], p, p, p) * omega(a, AX[2], p, p, p) for a in AX) * (6 / (6 * p)) ** 2
    )
    ok = per and sp.simplify(avg2 - claimed) == 0 and ratio == 4
    ok &= zvals == [sp.Rational(13, 2), sp.Rational(11, 2), sp.Integer(6)]
    ok &= sp.simplify(iso_z - 6) == 0
    report(
        "average normalizer",
        bool(ok),
        "averaged Z_2 is 6(c/c0)^2, so c=2 c0 gives 4; at (3,1,2) the pointwise values are 13/2, 11/2 and 6; at p=q=r they are 6",
    )


def pendant():
    p, q, r, c = sp.symbols("p q r c", positive=True)
    one = c * (p + q + 4 * r) / 6
    sol = sp.solve(sp.Eq(one, 1), c)
    c0 = 6 / (p + q + 4 * r)
    report(
        "pendant",
        sol == [c0],
        "c(p+q+4r)/6 = 1 has the unique solution c = 6/(p+q+4r)",
    )


def main():
    readings()
    pendant()
    branches()
    normalizer()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the four readings at (3,1,2) are 1/2, 2^(1/3)*3^(5/6)/6, 5/9 and 1/3. "
        "A pendant site matches the vacancy only at c0. Two occupied neighbours give 13/3, 11/3 and 4, "
        "so no single c matches every pair there, and the averaged normalizer is 6(c/c0)^k. "
        "The three branches are the same function of the pair only when p=q=r, and then c0 makes the normalizer 6 for every neighbourhood."
    )
    print(
        "SUMMARY: confirmed the logged sums, the pendant uniqueness, and the average factorization. "
        "The markdown fractions 17/6 and 17/3 are not those sums. "
        "The blanket no-go fails on p=q=r, where c0 works pointwise. (d) and (e) were not attempted."
    )


if __name__ == "__main__":
    main()
