#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`.

Pattern A narrow witness for d=4 forcing from the integer-arithmetic
direction. The narrow scope is purely the elementary number-theoretic
identity that, for integers d >= 2, the equation
binom(d, 2) = 2 (d - 1) holds iff d = 4.

The script verifies, at exact rational precision via sympy:

  (1) (D1)/(D2) The numerical evaluation L(d) = binom(d, 2) and
      R(d) = 2(d - 1) for d in {2, 3, ..., 12}.
  (2) (D1) Factorization (d - 1)(d - 4) = 0 ⟺ d in {1, 4} via
      direct sympy polynomial factorization.
  (3) (D2) Tabular matching: L(d) = R(d) exactly at d = 4 in
      {2, ..., 12}.
  (4) (D3) Monotonicity: L(d) - R(d) > 0 for d in {5, 6, ..., 12}.
  (5) (D4) Violation: L(d) - R(d) < 0 for d in {2, 3}.
  (6) (D5) Uniqueness: d = 4 is the unique integer in {2, ..., 12}
      satisfying L(d) = R(d).

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow theorem's
load-bearing class-(A) integer-arithmetic identity holds at exact
symbolic precision.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import sympy
    from sympy import Rational, Symbol, binomial, factor, simplify, solve, Eq, Integer
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md"
)
CLAIM_ID = "binom_d_2_equals_twice_dminus1_forces_d_four_narrow_theorem_note_2026-05-26"


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def L_of_d(d: int) -> int:
    """L(d) = binom(d, 2) = d (d - 1) / 2 for integer d >= 0."""
    return int(binomial(d, 2))


def R_of_d(d: int) -> int:
    """R(d) = 2 (d - 1) for integer d."""
    return 2 * (d - 1)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26")
    print("Goal: sympy verification that binom(d, 2) = 2(d - 1) iff d = 4")
    print("      via elementary integer arithmetic on binomial coefficients")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (D2) Numerical evaluation table for d in {2, ..., 12}")
    # =========================================================================
    table = {}
    for d in range(2, 13):
        L = L_of_d(d)
        R = R_of_d(d)
        table[d] = (L, R, L - R)
        check(
            f"(D2) at d = {d}: L = binom(d, 2) = {L}, R = 2(d - 1) = {R}, "
            f"L - R = {L - R}",
            L == d * (d - 1) // 2 and R == 2 * (d - 1),
            detail=f"L = {L}, R = {R}",
        )

    # =========================================================================
    section("Part 2: (D1) Polynomial factorization")
    # =========================================================================
    d = Symbol("d", integer=True)
    poly_LR = d * (d - 1) - 4 * (d - 1)  # = (d-1)(d-4)
    factored = factor(poly_LR)
    expected_factored = (d - 1) * (d - 4)
    check(
        "(D1) d(d-1) - 4(d-1) factors as (d-1)(d-4)",
        sympy.expand(factored) == sympy.expand(expected_factored),
        detail=f"factored = {factored}",
    )

    # Solve (d - 1)(d - 4) = 0 over integers
    solutions = solve(Eq(poly_LR, 0), d)
    check(
        "(D1) (d - 1)(d - 4) = 0 has solutions d ∈ {1, 4}",
        set(solutions) == {Integer(1), Integer(4)},
        detail=f"solutions = {solutions}",
    )

    # Restrict to d >= 2
    valid_solutions = [s for s in solutions if s >= 2]
    check(
        "(D1) Restricted to d >= 2, unique solution is d = 4",
        valid_solutions == [Integer(4)],
        detail=f"valid = {valid_solutions}",
    )

    # =========================================================================
    section("Part 3: (D2) Match at d = 4 (only)")
    # =========================================================================
    for d in range(2, 13):
        match = table[d][0] == table[d][1]
        expected_match = d == 4
        check(
            f"(D2) at d = {d}: L = R is {match}",
            match == expected_match,
            detail=f"expected match: {expected_match}, got {match}",
        )

    # =========================================================================
    section("Part 4: (D3) Monotonicity L > R for d in {5, ..., 12}")
    # =========================================================================
    for d in range(5, 13):
        gap = table[d][2]
        check(
            f"(D3) at d = {d}: L - R = {gap} > 0",
            gap > 0,
            detail=f"L - R = {gap}",
        )
        # Verify the explicit formula (d - 1)(d - 4) / 2
        expected_gap = (d - 1) * (d - 4) // 2
        check(
            f"(D3) at d = {d}: L - R = (d - 1)(d - 4) / 2 = {expected_gap}",
            gap == expected_gap,
            detail=f"formula = {expected_gap}, computed = {gap}",
        )

    # Symbolic identity: L(d) - R(d) = (d-1)(d-4)/2 (as polynomial)
    d_sym = Symbol("d", integer=True)
    L_sym = binomial(d_sym, 2)
    R_sym = 2 * (d_sym - 1)
    diff_sym = sympy.simplify(L_sym - R_sym)
    expected_diff_sym = (d_sym - 1) * (d_sym - 4) / 2
    check(
        "(D3) Symbolic: L(d) - R(d) = (d-1)(d-4)/2",
        sympy.simplify(diff_sym - expected_diff_sym) == 0,
        detail=f"L - R = {diff_sym}",
    )

    # =========================================================================
    section("Part 5: (D4) Violation at d in {2, 3}: L < R")
    # =========================================================================
    for d in (2, 3):
        gap = table[d][2]
        check(
            f"(D4) at d = {d}: L - R = {gap} < 0",
            gap < 0,
            detail=f"L - R = {gap}",
        )

    # =========================================================================
    section("Part 6: (D5) Uniqueness over d in {2, ..., 12}")
    # =========================================================================
    matching_d = [d for d in range(2, 13) if table[d][0] == table[d][1]]
    check(
        "(D5) Among d in {2, ..., 12}, exactly d = 4 satisfies L(d) = R(d)",
        matching_d == [4],
        detail=f"matching d values = {matching_d}",
    )

    # Extend range up to d = 20 for extra confidence
    matching_d_ext = [d for d in range(2, 21) if L_of_d(d) == R_of_d(d)]
    check(
        "(D5) Among d in {2, ..., 20}, exactly d = 4 satisfies L(d) = R(d)",
        matching_d_ext == [4],
        detail=f"matching d values (extended) = {matching_d_ext}",
    )

    # =========================================================================
    section("Part 7: (D6) Informational geometric reading (cross-check, not load-bearing)")
    # =========================================================================
    # At d = 4: L(4) = dim Λ^2(R^4) = dim so(4) = 6. R(4) = 2 (4 - 1) = 6 = 2 · 3.
    # The matching 6 = 2 · 3 splits as the self-dual + anti-self-dual halves
    # of Λ^2(R^4), each of dim 3 = d - 1 = dim su(2).
    # Verify this dimensional cross-check (informational only):
    dim_lambda_2_r4 = int(binomial(4, 2))
    dim_so_4 = 4 * 3 // 2
    dim_su_2 = 3  # standard
    check(
        "(D6) [info] dim Λ^2(R^4) = dim so(4) = 6",
        dim_lambda_2_r4 == dim_so_4 and dim_so_4 == 6,
        detail=f"dim Λ^2(R^4) = {dim_lambda_2_r4}, dim so(4) = {dim_so_4}",
    )
    check(
        "(D6) [info] 6 = 2 × 3 = 2 × dim su(2) (self-dual + anti-self-dual halves)",
        dim_so_4 == 2 * dim_su_2,
        detail=f"6 = 2 × 3 = {2 * dim_su_2}",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print()
    print(f"  Note path: {NOTE_PATH.name}")
    print(f"  Claim id:  {CLAIM_ID}")
    print()
    if FAIL == 0:
        print("  Result: all class-(A) checks pass at exact rational precision.")
        return 0
    print("  Result: at least one class-(A) check failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
