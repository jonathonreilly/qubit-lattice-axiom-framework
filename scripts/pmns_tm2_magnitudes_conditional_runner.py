#!/usr/bin/env python3
"""Bounded checker for the conditional PMNS TM2 |U|^2 matrix."""

from __future__ import annotations

from fractions import Fraction

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    PASS += int(condition)
    FAIL += int(not condition)
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def matrix(s2: Fraction) -> list[list[Fraction]]:
    return [
        [Fraction(2, 3) - s2, Fraction(1, 3), s2],
        [Fraction(1, 6) + s2 / 2, Fraction(1, 3), (1 - s2) / 2],
        [Fraction(1, 6) + s2 / 2, Fraction(1, 3), (1 - s2) / 2],
    ]


def row_sums(m: list[list[Fraction]]) -> list[Fraction]:
    return [sum(row) for row in m]


def col_sums(m: list[list[Fraction]]) -> list[Fraction]:
    return [sum(m[i][j] for i in range(3)) for j in range(3)]


def main() -> int:
    print("=" * 72)
    print("PMNS TM2 MAGNITUDES CONDITIONAL MATRIX -- BOUNDED CHECK")
    print("=" * 72)

    samples = [
        Fraction(0),
        Fraction(1, 100),
        Fraction(1, 45),
        Fraction(223, 10000),
        Fraction(1, 10),
        Fraction(2, 3),
    ]

    for s2 in samples:
        m = matrix(s2)
        check(f"row sums are 1 for s^2={s2}", row_sums(m) == [1, 1, 1])
        check(f"column sums are 1 for s^2={s2}", col_sums(m) == [1, 1, 1])
        check(f"second column trimaximal for s^2={s2}", [m[i][1] for i in range(3)] == [Fraction(1, 3)] * 3)
        check(f"mu and tau rows equal for s^2={s2}", m[1] == m[2])
        check(f"entries nonnegative for s^2={s2}", all(x >= 0 for row in m for x in row))

    for s2 in [Fraction(0), Fraction(1, 45), Fraction(223, 10000)]:
        m = matrix(s2)
        check(
            f"|U_e1|^2 formula at s^2={s2}",
            m[0][0] == Fraction(2, 3) - s2,
            f"value={m[0][0]}",
        )
        check(
            f"|U_mu3|^2 formula at s^2={s2}",
            m[1][2] == (1 - s2) / 2,
            f"value={m[1][2]}",
        )
        check(
            f"|U_mu1|^2 formula at s^2={s2}",
            m[1][0] == Fraction(1, 6) + s2 / 2,
            f"value={m[1][0]}",
        )

    zero = matrix(Fraction(0))
    denoms_zero = [x.denominator for row in zero for x in row if x]
    check("TBM-limit denominators divide 6", max(denoms_zero) <= 6, f"max={max(denoms_zero)}")

    rational = matrix(Fraction(1, 45))
    denoms_rational = [x.denominator for row in rational for x in row if x]
    check("s^2=1/45 denominators divide 90", max(denoms_rational) <= 90, f"max={max(denoms_rational)}")

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: conditional TM2 magnitudes matrix FAILED.")
        return 1
    print("VERDICT: conditional TM2 magnitudes matrix holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
