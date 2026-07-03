#!/usr/bin/env python3
"""Symbolic checks for the all-odd-N exact Q-gen Metzler obstruction."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


class Runner:
    def __init__(self) -> None:
        self.checks: list[Check] = []

    def add(self, name: str, passed: bool, detail: str) -> None:
        self.checks.append(Check(name, bool(passed), detail))
        status = "PASS" if passed else "FAIL"
        print(f"{status} {name}: {detail}")

    @property
    def passed(self) -> int:
        return sum(1 for check in self.checks if check.passed)

    @property
    def failed(self) -> int:
        return sum(1 for check in self.checks if not check.passed)

    @property
    def total(self) -> int:
        return len(self.checks)


def exact_zero(expr: sp.Expr) -> bool:
    simplified = sp.simplify(sp.trigsimp(expr))
    if simplified == 0:
        return True
    equality = simplified.equals(0)
    if equality is not None:
        return bool(equality)
    x = sp.Symbol("x")
    return sp.minpoly(simplified, x) == x


def odd_direct_sum(N: int, j: int) -> sp.Expr:
    M = (N - 1) // 2
    return sp.simplify(
        sum(
            n * n * sp.cos(sp.Rational(2) * sp.pi * n * j / N)
            for n in range(-M, M + 1)
        )
    )


def odd_closed_sum(N: int, j: int) -> sp.Expr:
    alpha = sp.pi * j / N
    return sp.simplify(
        sp.Rational(N, 2)
        * ((-1) ** j)
        * sp.cos(alpha)
        / sp.sin(alpha) ** 2
    )


def odd_generator_entry(N: int, j: int) -> sp.Expr:
    return sp.simplify(-odd_closed_sum(N, j) / N)


def even_direct_sum(N: int, j: int) -> sp.Expr:
    M = N // 2
    return sp.simplify(
        sum(
            n * n * sp.cos(sp.Rational(2) * sp.pi * n * j / N)
            for n in range(-M + 1, M + 1)
        )
    )


def even_closed_sum(N: int, j: int) -> sp.Expr:
    alpha = sp.pi * j / N
    return sp.simplify(sp.Rational(N, 2) * ((-1) ** j) / sp.sin(alpha) ** 2)


def even_generator_entry(N: int, j: int) -> sp.Expr:
    return sp.simplify(-even_closed_sum(N, j) / N)


def main() -> int:
    runner = Runner()

    odd_closed_verified: list[str] = []
    for N in (5, 7, 9, 11, 13):
        for j in range(1, N):
            direct = odd_direct_sum(N, j)
            closed = odd_closed_sum(N, j)
            ok = exact_zero(direct - closed)
            runner.add(
                f"odd_closed_form_N{N}_j{j}",
                ok,
                "direct-minus-closed=0"
                if ok
                else f"direct-minus-closed={sp.sstr(sp.simplify(direct - closed))}",
            )
        odd_closed_verified.append(str(N))

    odd_signs: list[str] = []
    for N in range(5, 42, 2):
        entry = odd_generator_entry(N, 2)
        runner.add(
            f"odd_j2_metzler_violation_N{N}",
            entry.is_negative is True,
            f"L_2={sp.sstr(entry)} < 0",
        )
        odd_signs.append(str(N))

    even_closed_verified: list[str] = []
    for N in (6, 8, 10, 12, 14):
        for j in range(1, N):
            direct = even_direct_sum(N, j)
            closed = even_closed_sum(N, j)
            ok = exact_zero(direct - closed)
            runner.add(
                f"even_closed_form_N{N}_j{j}",
                ok,
                "direct-minus-closed=0"
                if ok
                else f"direct-minus-closed={sp.sstr(sp.simplify(direct - closed))}",
            )
        even_closed_verified.append(str(N))

    even_signs: list[str] = []
    for N in (6, 8, 10, 12, 14):
        entry = even_generator_entry(N, 2)
        runner.add(
            f"even_j2_metzler_violation_N{N}",
            entry.is_negative is True,
            f"L_2={sp.sstr(entry)} < 0",
        )
        even_signs.append(str(N))

    print(f"SUMMARY PASS={runner.passed} FAIL={runner.failed} TOTAL={runner.total}")
    print(
        "SUMMARY ODD_CLOSED_FORM "
        f"verified_N={','.join(odd_closed_verified)} all_j; "
        f"odd_j2_negative_N={odd_signs[0]}..{odd_signs[-1]}"
    )
    print(
        "SUMMARY EVEN_SCOPE "
        "convention=residues_-N/2+1..N/2; "
        f"closed_form_verified_N={','.join(even_closed_verified)} all_j; "
        f"sampled_j2_negative_N={','.join(even_signs)}; "
        "theorem=even_N>=4_j2_negative_under_this_convention"
    )
    return 0 if runner.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
