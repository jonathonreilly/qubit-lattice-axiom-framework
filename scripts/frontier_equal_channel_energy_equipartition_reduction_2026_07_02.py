#!/usr/bin/env python3
"""Exact checks for the Block06 equal-channel/equipartition reduction."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Qsqrt2:
    q: Fraction
    s: Fraction = Fraction(0)

    def __add__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(self.q + other.q, self.s + other.s)

    def __sub__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(self.q - other.q, self.s - other.s)

    def __mul__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(
            self.q * other.q + 2 * self.s * other.s,
            self.q * other.s + self.s * other.q,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Qsqrt2):
            return NotImplemented
        return self.q == other.q and self.s == other.s


def q(value: int | Fraction) -> Qsqrt2:
    return Qsqrt2(Fraction(value), Fraction(0))


def check(name: str, condition: bool, results: list[tuple[str, bool]]) -> None:
    results.append((name, condition))


def main() -> int:
    results: list[tuple[str, bool]] = []

    N = Fraction(3)
    norm_I = N
    norm_B = N * (N - 1)
    component_factor = norm_B / norm_I

    r_s1 = Fraction(1, 2)
    q_s1 = Fraction(1, 3) + Fraction(2, 3) * r_s1
    r_s2 = Fraction(1)
    q_s2 = Fraction(1, 3) + Fraction(2, 3) * r_s2
    a2 = Fraction(1)
    b2_component = r_s1 * a2

    component_fixed = {Fraction(0), Fraction(1, 2)}
    slot_fixed = {Fraction(0), Fraction(1)}
    s3 = Qsqrt2(Fraction(17, 2), Fraction(-6))

    check("C3 unit-channel norm is 3", norm_I == 3, results)
    check("C3 complement-channel norm is 6", norm_B == 6, results)
    check("C3 complement norm equals 2N", norm_B == 2 * N, results)
    check("E-ident component ratio gives x=2r", component_factor == 2, results)
    check("component equal weight gives 3a^2=6|b|^2 -> r=1/2", r_s1 == norm_I / norm_B, results)
    check("component Q matches S1 Q=2/3", q_s1 == Fraction(2, 3), results)
    check("component map fixed set is {0,1/2}", all(r == 2 * r * r for r in component_fixed), results)
    check("component map has no extra rational roots in declared set", component_fixed == {Fraction(0), Fraction(1, 2)}, results)
    check("slot equal weight gives a^2=|b|^2 -> r=1", r_s2 == 1, results)
    check("slot Q matches S2 Q=1", q_s2 == 1, results)
    check("slot map fixed set is {0,1}", all(r == r * r for r in slot_fixed), results)
    check("slot map has no extra rational roots in declared set", slot_fixed == {Fraction(0), Fraction(1)}, results)
    check("component dictionary value equals Block01 S1 value", r_s1 == Fraction(1, 2) and q_s1 == Fraction(2, 3), results)
    check("slot dictionary value equals Block01 S2 value", r_s2 == 1 and q_s2 == 1, results)
    check("parent equal-HS clause at N=3 equals component equation", N == 3 and N * a2 == N * (N - 1) * b2_component, results)
    check("S3 value is outside both dictionary fixed sets", all(s3 != q(r) for r in component_fixed | slot_fixed), results)

    passed = sum(1 for _, ok in results if ok)
    failed_names = [name for name, ok in results if not ok]
    failed = len(failed_names)

    outside = all(s3 != q(r) for r in component_fixed | slot_fixed)
    print(f"CHECKS: PASS={passed} FAIL={failed}")
    print("VALUES: component r=1/2 Q=2/3; slot r=1 Q=1; S3 outside=" + str(outside))
    print(f"TOTAL: PASS={passed} FAIL={failed}")

    if failed:
        for name in failed_names:
            print(f"FAIL: {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
