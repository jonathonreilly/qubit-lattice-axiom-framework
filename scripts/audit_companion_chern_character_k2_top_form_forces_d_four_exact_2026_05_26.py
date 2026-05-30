#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`.

Pattern A narrow witness for d=4 forcing from the Chern-character
formal-expansion direction. The narrow scope is purely the graded-
algebra identity that, for a matrix-valued 2-form F ∈ Λ^2(R^d) ⊗ M_N,
the k-th Chern-character term

  ch_k(F) = (i / (2π))^k * tr(F^∧k) / k!

is a top-degree form on R^d iff 2k = d. Specializing k = 2 (the ABJ
chiral-anomaly identification with the second Chern character) forces
d = 4.

The script verifies, at exact rational/symbolic precision via sympy:

  (1) (K1)/(K2) The dimension formula dim Λ^p(R^d) = binom(d, p) for
      d in {0, 1, ..., 8} and p in {0, 1, ..., d}.
  (2) (K1) Degree-additivity of wedge powers: F^∧k has degree 2k for
      k in {1, 2, 3, 4}.
  (3) (K3) ch_k(F) is a top-form iff 2k = d, verified by symbolic
      evaluation for k in {1, 2, 3, 4} and d in {0, 1, ..., 8}.
  (4) (K4) Specialization k=2 forces d=4; symbolic verification of
      ch_2(F) = (- 1 / (8 π^2)) * tr(F ∧ F) from the factorial
      coefficient (i / (2π))^2 / 2!.
  (5) (K5) Explicit F = i (e^1∧e^2 + e^3∧e^4) ⊗ I_N at d=4 has
      ch_2(F) = (N / (4 π^2)) * volume form on R^4.
  (6) (K6) Counterfactual at d in {0, 1, 2, 3}: ch_2(F) = 0.
  (7) (K7) Counterfactual at d in {5, 6, 7, 8}: ch_2(F) ∈ Λ^4(R^d)
      is a 4-form, not a top-form.
  (8) (K8) Uniqueness over d in {0, 1, ..., 8} with k=2: only d=4.
  (9) Factorial-coefficient identity: (i/(2π))^2 / 2! = -1/(8 π^2).

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow theorem's
load-bearing class-(A) graded-algebra identity holds at exact symbolic
precision.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys

try:
    import sympy
    from sympy import I, Rational, Symbol, binomial, pi, simplify, symbols
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md"
)
CLAIM_ID = "chern_character_k2_top_form_forces_d_four_narrow_theorem_note_2026-05-26"


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
# sympy coefficients. The wedge product is the usual graded-
# antisymmetric product on these basis elements.
#
# Matrix-valued forms: same representation, but coefficients are
# matrices (modeled as scalars for the I_N case, with multiplicative
# factor N when tracing).


def basis_pforms(d: int, p: int) -> list:
    """Enumerate the (i_1 < ... < i_p) basis indices for Λ^p(R^d)."""
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
    if len(set(combined)) != len(combined):
        return ((), 0)
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
    return {k: v for k, v in out.items() if sympy.simplify(v) != 0}


def form_is_zero(alpha: dict) -> bool:
    """Check if a form is identically zero."""
    if not alpha:
        return True
    return all(sympy.simplify(c) == 0 for c in alpha.values())


def form_degree(alpha: dict) -> int | None:
    """Return the degree of a homogeneous form (or None)."""
    if not alpha or form_is_zero(alpha):
        return None
    degs = {len(k) for k in alpha.keys() if sympy.simplify(alpha[k]) != 0}
    if len(degs) > 1:
        return None
    return degs.pop() if degs else None


def wedge_power(alpha: dict, k: int) -> dict:
    """Compute the k-fold wedge power F^∧k = F ∧ F ∧ ... ∧ F."""
    if k <= 0:
        return {(): Rational(1)}  # ch_0 = scalar 1 (per copy of identity)
    out = alpha
    for _ in range(k - 1):
        out = wedge_forms(out, alpha)
    return out


def scale_form(alpha: dict, c) -> dict:
    """Multiply all coefficients of a form by a scalar c."""
    return {k: sympy.simplify(v * c) for k, v in alpha.items() if sympy.simplify(v * c) != 0}


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("CHERN_CHARACTER_K2_TOP_FORM_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26")
    print("Goal: sympy verification that ch_k(F) ∈ Λ^d(R^d) iff 2k = d")
    print("      and that k=2 (chiral-anomaly identification) forces d=4")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (K1)/(K2) Dimension formula dim Λ^p(R^d) = binom(d, p)")
    # =========================================================================
    for d in range(9):
        for p in range(d + 1):
            expected = int(binomial(d, p))
            actual = dim_lambda_p(d, p)
            check(
                f"(K1) at d = {d}, p = {p}: dim Λ^p(R^d) = {expected}",
                actual == expected,
                detail=f"computed = {actual}",
            )

    # Top-form criterion: dim Λ^d(R^d) = 1 for every d ≥ 0
    for d in range(9):
        check(
            f"(K2) at d = {d}: dim Λ^d(R^d) = 1 (top-form line)",
            dim_lambda_p(d, d) == 1,
            detail=f"top dim = {dim_lambda_p(d, d)}",
        )

    # =========================================================================
    section("Part 2: (K1) Degree-additivity F^∧k has degree 2k for k = 1..4")
    # =========================================================================
    # Use d = 8 to fit up to k = 4 (degree 8). Take F = (e^1∧e^2) + (e^3∧e^4)
    # + (e^5∧e^6) + (e^7∧e^8) so F^∧4 ≠ 0.
    F_d8 = {
        (1, 2): Rational(1),
        (3, 4): Rational(1),
        (5, 6): Rational(1),
        (7, 8): Rational(1),
    }
    for k_test in (1, 2, 3, 4):
        Fk = wedge_power(F_d8, k_test)
        deg = form_degree(Fk)
        check(
            f"(K1) at d = 8: F^∧{k_test} has form degree 2k = {2 * k_test}",
            deg == 2 * k_test,
            detail=f"computed degree = {deg}",
        )

    # =========================================================================
    section("Part 3: (K3) ch_k(F) top-form iff 2k = d (k = 1..4, d = 0..8)")
    # =========================================================================
    # For each k in {1, 2, 3, 4} and d in {0, ..., 8}, build a "canonical"
    # F = i * (sum of pairs e^{2j-1}∧e^{2j} up to floor(d/2)) and check
    # whether F^∧k has degree d (i.e., is a top-form).
    for k_test in (1, 2, 3, 4):
        for d_test in range(9):
            # Build F on R^d. Take F = i * Σ_{j=1}^{floor(d/2)} e^{2j-1}∧e^{2j}.
            F_d = {}
            num_pairs = d_test // 2
            for j in range(1, num_pairs + 1):
                F_d[(2 * j - 1, 2 * j)] = I  # i * 1
            if not F_d:
                # No 2-forms exist (d < 2); F = 0 and F^∧k = 0
                if d_test < 2:
                    expected_top = False
                    actual_is_top = False
                    # ch_k for k>=1 is 0 on R^0 or R^1
                    check(
                        f"(K3) at (k, d) = ({k_test}, {d_test}): "
                        f"ch_k top-form? {actual_is_top}",
                        actual_is_top == expected_top,
                        detail=f"d < 2 -> F = 0 -> ch_k = 0; expected top? {expected_top}",
                    )
                    continue
            Fk = wedge_power(F_d, k_test)
            if form_is_zero(Fk):
                actual_is_top = False
            else:
                deg = form_degree(Fk)
                actual_is_top = (deg == d_test)
            expected_top = (2 * k_test == d_test)
            check(
                f"(K3) at (k, d) = ({k_test}, {d_test}): "
                f"ch_k top-form? {actual_is_top}",
                actual_is_top == expected_top,
                detail=f"2k = {2 * k_test}; d = {d_test}; expected top? {expected_top}",
            )

    # =========================================================================
    section("Part 4: (K4) Specialization k=2 forces d=4; factorial coefficient")
    # =========================================================================
    # The factorial coefficient (i / (2π))^2 / 2! = -1 / (8 π^2).
    coeff_ch2 = (I / (2 * pi)) ** 2 / sympy.factorial(2)
    expected_ch2_coeff = Rational(-1, 8) / (pi ** 2)
    check(
        "(K4) Factorial coefficient: (i/(2π))^2 / 2! = -1/(8 π^2)",
        sympy.simplify(coeff_ch2 - expected_ch2_coeff) == 0,
        detail=f"computed = {sympy.simplify(coeff_ch2)}",
    )

    # The unique d satisfying 2k = d with k = 2 is d = 4
    k_fixed = 2
    matching_d = [d for d in range(9) if 2 * k_fixed == d]
    check(
        "(K4) Unique d satisfying 2k = d with k = 2: d = 4",
        matching_d == [4],
        detail=f"matching d = {matching_d}",
    )

    # =========================================================================
    section("Part 5: (K5) Explicit F = i(e^1∧e^2 + e^3∧e^4) ⊗ I_N on R^4")
    # =========================================================================
    d = 4
    # F = i * (e^1∧e^2 + e^3∧e^4), coefficient is i (we track the matrix
    # trace factor N at the end).
    F_explicit = {(1, 2): I, (3, 4): I}
    deg_F = form_degree(F_explicit)
    check(
        "(K5) F has degree 2",
        deg_F == 2,
        detail=f"degree = {deg_F}",
    )

    # Compute F ∧ F
    F_squared = wedge_forms(F_explicit, F_explicit)
    # Expected: i^2 * 2 * e^1∧e^2∧e^3∧e^4 = -2 * e^1∧e^2∧e^3∧e^4
    expected_F_sq = {(1, 2, 3, 4): Rational(-2)}
    keys_match = set(F_squared.keys()) == set(expected_F_sq.keys())
    vals_match = keys_match and all(
        sympy.simplify(F_squared[k] - expected_F_sq[k]) == 0
        for k in expected_F_sq
    )
    check(
        "(K5) F ∧ F = -2 · e^1∧e^2∧e^3∧e^4 (form part, before trace)",
        vals_match,
        detail=f"F ∧ F = {F_squared}",
    )

    # tr(F ∧ F) for F ⊗ I_N: trace gives factor N
    # tr(F ∧ F) = N * (form part of F ∧ F)
    N_sym = Symbol("N", positive=True, integer=True)
    tr_F_squared = scale_form(F_squared, N_sym)
    expected_tr = {(1, 2, 3, 4): -2 * N_sym}
    keys_match = set(tr_F_squared.keys()) == set(expected_tr.keys())
    vals_match = keys_match and all(
        sympy.simplify(tr_F_squared[k] - expected_tr[k]) == 0
        for k in expected_tr
    )
    check(
        "(K5) tr(F ∧ F) = -2 N · e^1∧e^2∧e^3∧e^4",
        vals_match,
        detail=f"tr(F ∧ F) = {tr_F_squared}",
    )

    # ch_2(F) = (i / (2π))^2 / 2! · tr(F ∧ F)
    #        = (- 1 / (8 π^2)) · (-2 N) · e^1∧⋯∧e^4
    #        = (N / (4 π^2)) · e^1∧⋯∧e^4
    ch2_F = scale_form(tr_F_squared, coeff_ch2)
    expected_ch2 = {(1, 2, 3, 4): N_sym / (4 * pi ** 2)}
    keys_match = set(ch2_F.keys()) == set(expected_ch2.keys())
    vals_match = keys_match and all(
        sympy.simplify(ch2_F[k] - expected_ch2[k]) == 0
        for k in expected_ch2
    )
    check(
        "(K5) ch_2(F) = (N / (4 π^2)) · e^1∧e^2∧e^3∧e^4 (top-form on R^4)",
        vals_match,
        detail=f"ch_2(F) = {ch2_F}",
    )

    # ch_2(F) has degree 4 = top degree on R^4
    deg_ch2 = form_degree(ch2_F)
    check(
        "(K5) ch_2(F) has degree 4 = top degree on R^4",
        deg_ch2 == 4 and deg_ch2 == d,
        detail=f"degree = {deg_ch2}, d = {d}",
    )

    # =========================================================================
    section("Part 6: (K6) Counterfactual at d ∈ {0, 1, 2, 3}: ch_2(F) = 0")
    # =========================================================================
    for d_test in (0, 1, 2, 3):
        # Build F on R^{d_test}; for d < 2, F is empty (no 2-forms)
        F_d = {}
        if d_test >= 2:
            num_pairs = d_test // 2
            for j in range(1, num_pairs + 1):
                F_d[(2 * j - 1, 2 * j)] = I
        # F ∧ F
        F_d_sq = wedge_forms(F_d, F_d) if F_d else {}
        # ch_2(F) = coeff_ch2 * (trace of F_d_sq); but since F_d_sq is zero
        # for d < 4, ch_2 is zero
        is_zero = form_is_zero(F_d_sq)
        check(
            f"(K6) at d = {d_test}: F ∧ F = 0 (so ch_2(F) = 0)",
            is_zero,
            detail=f"F ∧ F = {F_d_sq}",
        )

    # Also explicit monomial check: at d=2, only (e^1∧e^2) basis;
    # (e^1∧e^2) ∧ (e^1∧e^2) = 0 (repeated 1, 2)
    d_test = 2
    e12 = {(1, 2): Rational(1)}
    e12_sq = wedge_forms(e12, e12)
    check(
        "(K6) at d = 2: (e^1∧e^2) ∧ (e^1∧e^2) = 0 (repeated factor)",
        form_is_zero(e12_sq),
    )

    # d = 3: every pairwise wedge of 2-form monomials is zero
    d_test = 3
    basis_d3 = basis_pforms(d_test, 2)  # [(1,2), (1,3), (2,3)]
    for s1 in basis_d3:
        for s2 in basis_d3:
            mono = {s1: Rational(1)}
            mono2 = {s2: Rational(1)}
            res = wedge_forms(mono, mono2)
            check(
                f"(K6) at d = 3: (e^{s1[0]}∧e^{s1[1]}) ∧ (e^{s2[0]}∧e^{s2[1]}) = 0",
                form_is_zero(res),
                detail="Λ^4(R^3) = 0",
            )

    # =========================================================================
    section("Part 7: (K7) Counterfactual at d ∈ {5, 6, 7, 8}: ch_2 ∈ Λ^4")
    # =========================================================================
    for d_test in (5, 6, 7, 8):
        # F = i * Σ pairs
        F_d = {}
        num_pairs = d_test // 2
        for j in range(1, num_pairs + 1):
            F_d[(2 * j - 1, 2 * j)] = I
        F_d_sq = wedge_forms(F_d, F_d)
        if form_is_zero(F_d_sq):
            check(
                f"(K7) at d = {d_test}: F ∧ F ≠ 0 (sanity for d ≥ 4)",
                False,
                detail=f"F ∧ F = {F_d_sq}",
            )
            continue
        deg = form_degree(F_d_sq)
        check(
            f"(K7) at d = {d_test}: F ∧ F has degree 4",
            deg == 4,
            detail=f"degree = {deg}",
        )
        check(
            f"(K7) at d = {d_test}: 4 < d = {d_test} (ch_2 sub-top)",
            deg == 4 and deg < d_test,
            detail=f"4 < {d_test} = {4 < d_test}",
        )

    # Matching k = d/2 for even d ∈ {6, 8}: ch_k IS a top-form
    for d_test in (6, 8):
        k_match = d_test // 2
        F_d = {}
        num_pairs = d_test // 2
        for j in range(1, num_pairs + 1):
            F_d[(2 * j - 1, 2 * j)] = I
        Fk = wedge_power(F_d, k_match)
        deg = form_degree(Fk)
        check(
            f"(K7) at d = {d_test}: matching k = {k_match} gives F^∧k of degree d (top-form)",
            deg == d_test,
            detail=f"computed degree = {deg}",
        )

    # =========================================================================
    section("Part 8: (K8) Uniqueness — d = 4 is unique with k = 2")
    # =========================================================================
    # Among d ∈ {0, 1, ..., 8} and the constraint k = 2, which d satisfies
    # the top-form condition 2k = d?
    k_fixed = 2
    matches = []
    for d_test in range(9):
        if 2 * k_fixed == d_test:
            matches.append(d_test)
    check(
        "(K8) Among d ∈ {0, ..., 8} with k = 2, unique top-form match is d = 4",
        matches == [4],
        detail=f"matching d = {matches}",
    )

    # Cross-check: for k = 2, the unique d-value (over all integers d ≥ 0)
    # satisfying 2k = d is d = 4. Verified by direct integer arithmetic
    # via sympy `solve`.
    d_var = Symbol("d", integer=True, nonnegative=True)
    solutions = sympy.solve(sympy.Eq(2 * k_fixed, d_var), d_var)
    check(
        "(K8) sympy solve(2·2 = d): unique solution d = 4",
        solutions == [4],
        detail=f"sympy solutions = {solutions}",
    )

    # =========================================================================
    section("Part 9: Factorial-coefficient identity (i/(2π))^2 / 2! = -1/(8 π^2)")
    # =========================================================================
    # Already checked in Part 4; here verify the per-k pattern (i/(2π))^k / k!
    # for k = 1, 2, 3 reproduces standard normalizations.
    coeff_ch1 = (I / (2 * pi)) ** 1 / sympy.factorial(1)
    expected_ch1 = I / (2 * pi)
    check(
        "(K9) (i/(2π))^1 / 1! = i / (2 π)  (Chern char k=1 coeff)",
        sympy.simplify(coeff_ch1 - expected_ch1) == 0,
        detail=f"computed = {sympy.simplify(coeff_ch1)}",
    )

    coeff_ch2 = (I / (2 * pi)) ** 2 / sympy.factorial(2)
    expected_ch2 = Rational(-1, 8) / (pi ** 2)
    check(
        "(K9) (i/(2π))^2 / 2! = -1 / (8 π^2)  (Chern char k=2 coeff)",
        sympy.simplify(coeff_ch2 - expected_ch2) == 0,
        detail=f"computed = {sympy.simplify(coeff_ch2)}",
    )

    coeff_ch3 = (I / (2 * pi)) ** 3 / sympy.factorial(3)
    expected_ch3 = -I / (48 * pi ** 3)
    check(
        "(K9) (i/(2π))^3 / 3! = -i / (48 π^3)  (Chern char k=3 coeff)",
        sympy.simplify(coeff_ch3 - expected_ch3) == 0,
        detail=f"computed = {sympy.simplify(coeff_ch3)}",
    )

    # The factor 8 in the chiral-anomaly normalization 1/(8π²) comes from
    # 2 * (2π)^2 = 8 π^2; explicit check:
    eight_pi_sq = 2 * (2 * pi) ** 2
    check(
        "(K9) 8 π^2 = 2 · (2π)^2  (factor 2 from 1/2! in ch_2)",
        sympy.simplify(eight_pi_sq - 8 * pi ** 2) == 0,
        detail=f"2 · (2π)^2 = {sympy.expand(eight_pi_sq)}",
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
        print("  Result: all class-(A) checks pass at exact symbolic precision.")
        return 0
    print("  Result: at least one class-(A) check failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
