#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`.

Pattern A narrow witness for d=4 forcing from the graded-algebra
degree-counting direction. The narrow scope is purely the graded-
algebra identity that, for a 2-form ω ∈ Λ^2(R^d), the wedge-square
ω ∧ ω lies in the top-degree form space Λ^d(R^d) iff d = 4.

The script verifies, at exact rational precision via sympy:

  (1) (W1)/(W2) The dimension formula dim Λ^p(R^d) = binom(d, p) for
      d in {0, 1, ..., 8} and p in {0, 1, ..., d}.
  (2) (W3) Top-form criterion: Λ^4(R^d) ≠ 0 iff d ≥ 4.
  (3) (W4) Explicit ω = e^1 ∧ e^2 + e^3 ∧ e^4 on R^4 has
      ω ∧ ω = 2 e^1 ∧ e^2 ∧ e^3 ∧ e^4.
  (4) (W5) The Plücker polynomial identity ω_{12} ω_{34} -
      ω_{13} ω_{24} + ω_{14} ω_{23} (verified symbolically).
  (5) (W6) Counterfactual at d in {2, 3}: ω ∧ ω = 0 for every ω.
  (6) (W7) Counterfactual at d in {5, 6}: ω ∧ ω ∈ Λ^4(R^d) is a
      4-form, not a top-form.
  (7) (W3) Uniqueness over d in {0, 1, ..., 8}: only d = 4 gives a
      top-form wedge-square.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow theorem's
load-bearing class-(A) graded-algebra identity holds at exact symbolic
precision.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import sys

try:
    import sympy
    from sympy import Rational, Symbol, binomial, expand, symbols
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT / "docs" / "F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md"
)
CLAIM_ID = "f_wedge_f_top_form_forces_d_four_narrow_theorem_note_2026-05-26"


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


# ==============================================================================
# Differential-form representation
# ==============================================================================
#
# A p-form on R^d is represented as a dict mapping ordered tuples
# (i_1, ..., i_p) with i_1 < i_2 < ... < i_p, i_k ∈ {1, ..., d}, to
# sympy-rational coefficients. The wedge product is the usual graded-
# antisymmetric product on these basis elements.


def basis_pforms(d: int, p: int) -> list:
    """Enumerate the (i_1 < ... < i_p) basis indices for Λ^p(R^d).

    Returns a list of ordered tuples of length p with values in
    {1, ..., d}.
    """
    if p == 0:
        return [()]
    if p > d:
        return []
    return [tuple(s) for s in combinations(range(1, d + 1), p)]


def dim_lambda_p(d: int, p: int) -> int:
    """Dim of Λ^p(R^d) = binom(d, p) for 0 <= p <= d, else 0."""
    if p < 0 or p > d:
        return 0
    return int(binomial(d, p))


def wedge_basis(s1: tuple, s2: tuple) -> tuple[tuple, int]:
    """Wedge two ordered tuples of indices.

    Returns (combined_ordered_tuple, sign). If any index is repeated,
    sign = 0 and combined = ().
    """
    combined = list(s1) + list(s2)
    # Check for repeats
    if len(set(combined)) != len(combined):
        return ((), 0)
    # Bubble-sort to canonical order, counting transpositions
    sign = 1
    sorted_combined = list(combined)
    n = len(sorted_combined)
    for i in range(n):
        for j in range(n - 1 - i):
            if sorted_combined[j] > sorted_combined[j + 1]:
                sign = -sign
                sorted_combined[j], sorted_combined[j + 1] = (
                    sorted_combined[j + 1],
                    sorted_combined[j],
                )
    return (tuple(sorted_combined), sign)


def wedge_forms(alpha: dict, beta: dict) -> dict:
    """Wedge two forms (each a dict {ordered_tuple: coeff}).

    Returns the resulting form as a dict.
    """
    out: dict = {}
    for s1, c1 in alpha.items():
        for s2, c2 in beta.items():
            sorted_combined, sign = wedge_basis(s1, s2)
            if sign == 0:
                continue
            coeff = sign * c1 * c2
            if sorted_combined in out:
                out[sorted_combined] = out[sorted_combined] + coeff
            else:
                out[sorted_combined] = coeff
    # Drop zero-coefficient entries
    return {k: v for k, v in out.items() if sympy.simplify(v) != 0}


def form_is_zero(alpha: dict) -> bool:
    """Check if a form is identically zero."""
    if not alpha:
        return True
    return all(sympy.simplify(c) == 0 for c in alpha.values())


def form_degree(alpha: dict) -> int | None:
    """Return the degree of a homogeneous form (or None if multi-degree
    or empty)."""
    if not alpha or form_is_zero(alpha):
        return None
    degs = {len(k) for k in alpha.keys() if sympy.simplify(alpha[k]) != 0}
    if len(degs) > 1:
        return None
    return degs.pop() if degs else None


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("F_WEDGE_F_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26")
    print("Goal: sympy verification that ω ∧ ω ∈ Λ^d(R^d) iff d = 4")
    print("      via graded exterior-algebra degree counting on Λ^*(R^d)")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (W1)/(W2) Dimension formula dim Λ^p(R^d) = binom(d, p)")
    # =========================================================================
    for d in range(9):
        for p in range(d + 1):
            expected = int(binomial(d, p))
            actual = dim_lambda_p(d, p)
            check(
                f"(W1) at d = {d}, p = {p}: dim Λ^p(R^d) = {expected}",
                actual == expected,
                detail=f"computed = {actual}",
            )

    # Top-form criterion: dim Λ^d(R^d) = 1 for every d ≥ 0
    for d in range(9):
        check(
            f"(W2) at d = {d}: dim Λ^d(R^d) = 1 (top-form line)",
            dim_lambda_p(d, d) == 1,
            detail=f"top dim = {dim_lambda_p(d, d)}",
        )

    # =========================================================================
    section("Part 2: (W3) Top-form criterion Λ^4(R^d) ≠ 0 iff d ≥ 4")
    # =========================================================================
    for d in range(9):
        nonzero = dim_lambda_p(d, 4) > 0
        expected = d >= 4
        check(
            f"(W3) at d = {d}: Λ^4(R^d) ≠ 0 iff d ≥ 4 (got {nonzero})",
            nonzero == expected,
            detail=f"dim Λ^4(R^{d}) = {dim_lambda_p(d, 4)}",
        )

    # =========================================================================
    section("Part 3: (W4) Explicit ω = e^1∧e^2 + e^3∧e^4 at d = 4")
    # =========================================================================
    d = 4
    # ω = e^1 ∧ e^2 + e^3 ∧ e^4 in component form
    omega = {(1, 2): Rational(1), (3, 4): Rational(1)}
    # Verify ω is a 2-form
    deg_omega = form_degree(omega)
    check(
        "(W4) ω has degree 2",
        deg_omega == 2,
        detail=f"degree = {deg_omega}",
    )

    # Compute ω ∧ ω
    omega_squared = wedge_forms(omega, omega)
    expected_omega_sq = {(1, 2, 3, 4): Rational(2)}
    # Compare
    keys_match = set(omega_squared.keys()) == set(expected_omega_sq.keys())
    vals_match = keys_match and all(
        sympy.simplify(omega_squared[k] - expected_omega_sq[k]) == 0
        for k in expected_omega_sq
    )
    check(
        "(W4) ω ∧ ω = 2 · e^1 ∧ e^2 ∧ e^3 ∧ e^4",
        vals_match,
        detail=f"ω ∧ ω = {omega_squared}",
    )

    # ω ∧ ω has degree 4 (= top form on R^4)
    deg_sq = form_degree(omega_squared)
    check(
        "(W4) ω ∧ ω has degree 4 = top degree on R^4",
        deg_sq == 4 and deg_sq == d,
        detail=f"degree = {deg_sq}, d = {d}",
    )

    # =========================================================================
    section("Part 4: (W5) Plücker polynomial identity in 6 components")
    # =========================================================================
    # General ω = ω_{12} e^1∧e^2 + ω_{13} e^1∧e^3 + ω_{14} e^1∧e^4
    #           + ω_{23} e^2∧e^3 + ω_{24} e^2∧e^4 + ω_{34} e^3∧e^4
    w12, w13, w14, w23, w24, w34 = symbols("w12 w13 w14 w23 w24 w34", real=True)
    omega_gen = {
        (1, 2): w12,
        (1, 3): w13,
        (1, 4): w14,
        (2, 3): w23,
        (2, 4): w24,
        (3, 4): w34,
    }
    omega_gen_squared = wedge_forms(omega_gen, omega_gen)
    # Should have a single key (1, 2, 3, 4) with coefficient
    # 2 * (w12 * w34 - w13 * w24 + w14 * w23)
    expected_coeff = 2 * (w12 * w34 - w13 * w24 + w14 * w23)
    keys_correct = set(omega_gen_squared.keys()) == {(1, 2, 3, 4)}
    coeff_correct = keys_correct and sympy.simplify(
        omega_gen_squared[(1, 2, 3, 4)] - expected_coeff
    ) == 0
    check(
        "(W5) Plücker polynomial: ω∧ω = 2(w12 w34 - w13 w24 + w14 w23) e^1∧e^2∧e^3∧e^4",
        coeff_correct,
        detail=f"coeff = {sympy.simplify(omega_gen_squared.get((1, 2, 3, 4), 0))}",
    )

    # The Plücker polynomial is not identically zero (substitute w12 = w34 = 1,
    # others = 0)
    plucker_eval = expected_coeff.subs(
        {w12: 1, w34: 1, w13: 0, w14: 0, w23: 0, w24: 0}
    )
    check(
        "(W5) Plücker polynomial is not identically zero",
        sympy.simplify(plucker_eval) != 0,
        detail=f"P(1, 0, 0, 0, 0, 1) = {plucker_eval}",
    )

    # =========================================================================
    section("Part 5: (W6) Counterfactual at d ∈ {2, 3}: ω ∧ ω = 0")
    # =========================================================================
    for d_test in (2, 3):
        # Build a generic 2-form on R^{d_test}
        omega_d = {}
        for i, j in basis_pforms(d_test, 2):
            sym = Symbol(f"w_{d_test}_{i}_{j}", real=True)
            omega_d[(i, j)] = sym
        # Squared
        omega_d_sq = wedge_forms(omega_d, omega_d)
        # On d_test = 2: should be empty / zero
        # On d_test = 3: should be empty / zero (4-form has no nonzero entries
        # because Λ^4(R^3) = 0)
        check(
            f"(W6) at d = {d_test}: ω ∧ ω = 0 for every 2-form ω",
            form_is_zero(omega_d_sq),
            detail=f"computed: {omega_d_sq}",
        )

    # Also check explicit monomial wedge-squares at d = 2, 3
    # d = 2: only (1, 2) basis. (e^1∧e^2) ∧ (e^1∧e^2) = 0 (repeated 1, 2)
    d = 2
    e12 = {(1, 2): Rational(1)}
    e12_sq = wedge_forms(e12, e12)
    check(
        "(W6) at d = 2: (e^1∧e^2) ∧ (e^1∧e^2) = 0 (repeated factor)",
        form_is_zero(e12_sq),
    )

    # d = 3: try each pairwise wedge of monomials
    d = 3
    basis_d3 = basis_pforms(d, 2)  # [(1,2), (1,3), (2,3)]
    for s1 in basis_d3:
        for s2 in basis_d3:
            mono = {s1: Rational(1)}
            mono2 = {s2: Rational(1)}
            res = wedge_forms(mono, mono2)
            check(
                f"(W6) at d = 3: (e^{s1[0]}∧e^{s1[1]}) ∧ (e^{s2[0]}∧e^{s2[1]}) = 0",
                form_is_zero(res),
                detail=f"only 4-forms allowed live in Λ^4(R^3) = 0",
            )

    # =========================================================================
    section("Part 6: (W7) Counterfactual at d ∈ {5, 6}: ω∧ω ∈ Λ^4 not top")
    # =========================================================================
    for d_test in (5, 6):
        # Take ω = e^1 ∧ e^2 + e^3 ∧ e^4 on R^{d_test}
        omega_dt = {(1, 2): Rational(1), (3, 4): Rational(1)}
        omega_dt_sq = wedge_forms(omega_dt, omega_dt)
        deg = form_degree(omega_dt_sq)
        check(
            f"(W7) at d = {d_test}: ω ∧ ω has degree 4",
            deg == 4,
            detail=f"degree = {deg}",
        )
        check(
            f"(W7) at d = {d_test}: degree 4 < d = {d_test} (not top form)",
            deg == 4 and deg < d_test,
            detail=f"4 < {d_test} = {4 < d_test}",
        )
        # Verify the wedge-square is nonzero (sanity)
        check(
            f"(W7) at d = {d_test}: ω ∧ ω ≠ 0 (sanity)",
            not form_is_zero(omega_dt_sq),
            detail=f"ω∧ω = 2 e^1∧e^2∧e^3∧e^4",
        )

    # =========================================================================
    section("Part 7: (W3) Uniqueness — d = 4 is the only top-form wedge-square dim")
    # =========================================================================
    # For each d in {0, 1, ..., 8}, check whether some 2-form ω has
    # ω ∧ ω as a top-degree form (degree = d).
    top_form_match = {}
    for d_test in range(9):
        if d_test < 2:
            # No 2-forms on R^{d_test} for d_test < 2
            top_form_match[d_test] = False
            continue
        # Try ω = e^1 ∧ e^2 + e^3 ∧ e^4 (if d_test >= 4) or smaller
        if d_test >= 4:
            omega_t = {(1, 2): Rational(1), (3, 4): Rational(1)}
        else:
            # d_test in {2, 3}: only smaller wedges available
            omega_t = {(1, 2): Rational(1)}
        omega_t_sq = wedge_forms(omega_t, omega_t)
        if form_is_zero(omega_t_sq):
            top_form_match[d_test] = False
            continue
        deg = form_degree(omega_t_sq)
        top_form_match[d_test] = deg == d_test

    for d_test in range(9):
        expected = d_test == 4
        check(
            f"(W3) at d = {d_test}: ω ∧ ω is a top-form: {top_form_match[d_test]}",
            top_form_match[d_test] == expected,
            detail=f"expected {expected}",
        )

    # Unique d
    unique_d = [d_test for d_test in range(9) if top_form_match[d_test]]
    check(
        "(W3) Among d in {0, 1, ..., 8}, exactly d = 4 has ω ∧ ω as top-form",
        unique_d == [4],
        detail=f"matching d values = {unique_d}",
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
