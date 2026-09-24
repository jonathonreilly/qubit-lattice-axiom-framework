#!/usr/bin/env python3
"""Referee for ordering-threshold-down a5.

Author w-jonathonsmac4f50-j8265 (claude-opus-5). Own factorizations.
This is the domain of T1(a), not a threshold below 58.
"""
from fractions import Fraction as Fr
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def devs():
    p, q, r = sp.symbols("p q r", positive=True)
    d1 = (q ** 3 + 4 * r ** 3) / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = (p * q ** 2 + 4 * r ** 3) / (p ** 2 * q + p * q ** 2 + 4 * r ** 3)
    d3 = (q ** 2 * r + p * r ** 2 + q * r ** 2 + 2 * r ** 3) / (
        p ** 2 * r + q ** 2 * r + p * r ** 2 + q * r ** 2 + 2 * r ** 3
    )
    return p, q, r, d1, d2, d3


def numer(expr):
    return sp.factor(sp.numer(sp.together(sp.simplify(expr))))


def main():
    p, q, r, d1, d2, d3 = devs()
    line = {q: 1, r: 2}
    on_line = (
        sp.simplify(d1.subs(line) - 33 / (p ** 3 + 33)) == 0
        and sp.simplify(d2.subs(line) - (p + 32) / (p ** 2 + p + 32)) == 0
        and sp.simplify(d3.subs(line) - (2 * p + 11) / (p ** 2 + 2 * p + 11)) == 0
    )
    n21 = numer(d2 - d1)
    n31 = numer(d3 - d1)
    n23 = numer(d2 - d3)
    facts = (
        n21 == sp.factor(p ** 2 * (p - q) * (p * q ** 2 + q ** 3 + 4 * r ** 3))
        and n31 == sp.factor(p ** 2 * (p ** 2 * r + p * q ** 2 + p * q * r + 2 * p * r ** 2 - q ** 3 - 4 * r ** 3))
        and n23 == sp.factor(p ** 2 * (q - r) * (p * q - q ** 2 - 2 * q * r - 4 * r ** 2))
    )
    cross = sp.simplify((n23 / p ** 2).subs(line) + (p - 21)) == 0
    a3 = p ** 2 * (p - 1) * (p + 33) / ((p ** 3 + 33) * (p ** 2 + p + 32))
    same = sp.simplify((d2 - d1).subs(line) - a3) == 0
    report(
        "factorization",
        bool(on_line and facts and cross and same),
        "d2-d1 has numerator p^2(p-q)(pq^2+q^3+4r^3); on (p,1,2) the d2/d3 switch is p=21",
    )

    def at(pp, qq, rr):
        sub = {p: pp, q: qq, r: rr}
        return [sp.simplify(x.subs(sub)) for x in (d1, d2, d3)]

    bad = at(1, 2, 1)
    cubic_bad = 1 + 4 + 2 + 2 - (8 + 4)
    good = at(1, Fr(21, 20), Fr(1, 2))
    cubic_good = sp.simplify(
        (p ** 2 * r + p * q ** 2 + p * q * r + 2 * p * r ** 2 - q ** 3 - 4 * r ** 3).subs(
            {p: 1, q: Fr(21, 20), r: Fr(1, 2)}
        )
    )
    report(
        "witnesses",
        bad[0] > max(bad[1], bad[2]) and cubic_bad == -3 and cubic_good == Fr(7759, 8000)
        and good[0] <= max(good[1], good[2]) and Fr(1) < Fr(21, 20),
        " (1,2,1) fails both halves; (1, 21/20, 1/2) has p<q but the cubic saves T1(a)",
    )
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - d1 <= d2 iff p >= q, and d1 <= max(d2,d3) iff p >= q or "
        "p^2 r + p q^2 + p q r + 2 p r^2 >= q^3 + 4 r^3. "
        "(1,2,1) fails both; (1, 21/20, 1/2) is saved by the second half. "
        "On (p,1,2), d2 and d3 cross at p=21, and d2-d1 is the Dobrushin gap alpha_3."
    )
    print(
        "SUMMARY: confirmed the three numerators, the line restrictions, and both witnesses. "
        "This is the domain of T1(a). No threshold below 58 is claimed."
    )


if __name__ == "__main__":
    main()
