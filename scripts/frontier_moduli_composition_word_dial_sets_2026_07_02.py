#!/usr/bin/env python3
"""Exact checks for Block12 composition-word dial sets."""

from __future__ import annotations

from fractions import Fraction
import sys

import sympy as sp


r = sp.Symbol("r")


def exponent_for_word(word: tuple[str, ...]) -> int:
    k = len(word)
    return sum(2 ** (k - i - 1) for i, letter in enumerate(word) if letter == "f")


def expression_for_word(word: tuple[str, ...]) -> sp.Expr:
    expr = r
    for letter in word:
        if letter == "f":
            expr = 2 * expr**2
        elif letter == "g":
            expr = expr**2
        else:
            raise ValueError(f"unknown letter: {letter}")
    return sp.expand(expr)


def power_string(e: int, denom: int) -> str:
    if e == 0:
        return "2^0"
    if e == denom:
        return "2^-1"
    return f"2^(-{e}/{denom})"


def dial_set_string(k: int) -> str:
    denom = 2**k - 1
    values = ["0"] + [power_string(e, denom) for e in range(0, 2**k)]
    return "{" + ", ".join(values) + "}"


def all_words(k: int) -> list[tuple[str, ...]]:
    words: list[tuple[str, ...]] = [()]
    for _ in range(k):
        words = [word + (letter,) for word in words for letter in ("g", "f")]
    return words


checks: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    checks.append((name, bool(condition), detail))


def run_induction_exhaustive_checks() -> None:
    for k in range(1, 7):
        for word in all_words(k):
            expr = r
            prefix_e = 0
            for prefix_len, letter in enumerate(word, start=1):
                if letter == "f":
                    expr = 2 * expr**2
                    prefix_e = 2 * prefix_e + 1
                else:
                    expr = expr**2
                    prefix_e = 2 * prefix_e
                expected_prefix = 2**prefix_e * r ** (2**prefix_len)
                check(
                    f"induction_prefix_k{k}_{''.join(word)}_{prefix_len}",
                    sp.simplify(expr - expected_prefix) == 0,
                    str(word),
                )
            e = exponent_for_word(word)
            expected = 2**e * r ** (2**k)
            check(
                f"closed_form_k{k}_{''.join(word)}",
                sp.simplify(expression_for_word(word) - expected) == 0,
                str(word),
            )


def run_bijection_and_dial_checks() -> None:
    for k in range(1, 5):
        exponents = sorted(exponent_for_word(word) for word in all_words(k))
        expected = list(range(0, 2**k))
        check(f"bijection_k{k}", exponents == expected, str(exponents))
        denom = 2**k - 1
        dial_exponents = [Fraction(e, denom) for e in exponents]
        expected_exponents = [Fraction(e, denom) for e in range(0, 2**k)]
        check(f"dial_exponents_k{k}", dial_exponents == expected_exponents)


def run_spacing_checks() -> None:
    for k in range(1, 9):
        denom = 2**k - 1
        grid = [Fraction(e, denom) for e in range(0, 2**k)]
        spacings = [b - a for a, b in zip(grid, grid[1:])]
        check(f"spacing_k{k}", all(delta == Fraction(1, denom) for delta in spacings))
        check(f"endpoints_k{k}", grid[0] == 0 and grid[-1] == 1)


def run_boundary_checks() -> None:
    for k in range(1, 17):
        denom = 2**k - 1
        all_g = tuple("g" for _ in range(k))
        all_f = tuple("f" for _ in range(k))
        check(f"all_g_endpoint_k{k}", Fraction(exponent_for_word(all_g), denom) == 0)
        check(f"all_f_endpoint_k{k}", Fraction(exponent_for_word(all_f), denom) == 1)
    for k in range(1, 11):
        denom = 2**k - 1
        for word in all_words(k):
            x = Fraction(exponent_for_word(word), denom)
            check(f"boundary_k{k}_{''.join(word)}", Fraction(0) <= x <= Fraction(1))


def run_block07_match_checks() -> None:
    cases = [
        ("f", ("f",), 1, "2^-1"),
        ("g", ("g",), 0, "2^0"),
        ("f_after_f", ("f", "f"), 3, "2^-1"),
        ("f_after_g", ("g", "f"), 1, "2^(-1/3)"),
        ("g_after_f", ("f", "g"), 2, "2^(-2/3)"),
        ("g_after_g", ("g", "g"), 0, "2^0"),
    ]
    for name, word, expected_e, expected_power in cases:
        k = len(word)
        denom = 2**k - 1
        e = exponent_for_word(word)
        check(f"block07_e_{name}", e == expected_e, str(e))
        check(f"block07_power_{name}", power_string(e, denom) == expected_power)


def main() -> int:
    run_induction_exhaustive_checks()
    run_bijection_and_dial_checks()
    run_spacing_checks()
    run_boundary_checks()
    run_block07_match_checks()

    failures = [item for item in checks if not item[1]]
    status = "PASS" if not failures else "FAIL"
    print(f"STATUS {status} FAIL={len(failures)} TOTAL={len(checks)}")
    print(
        "VERIFIED exact induction all words k<=6; exponent bijections k=1..4; "
        "uniform spacing; endpoints; exhaustive r*>=1/2 boundary k<=10; Block07 matches; "
        f"D_1={dial_set_string(1)}; D_2={dial_set_string(2)}"
    )
    print(f"D_3={dial_set_string(3)}; D_4={dial_set_string(4)}")
    if failures:
        for name, _, detail in failures[:10]:
            print(f"FAIL_DETAIL {name} {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
