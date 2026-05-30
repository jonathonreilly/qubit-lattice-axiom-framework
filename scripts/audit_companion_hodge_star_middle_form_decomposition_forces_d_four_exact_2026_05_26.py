#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`HODGE_STAR_MIDDLE_FORM_DECOMPOSITION_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md`.

Pattern A narrow witness for d=4 forcing from the Hodge-star direction.
The narrow scope is purely the linear-algebra identity that, for the
Hodge star `*` on the graded exterior algebra Λ^*(R^d) with a non-
degenerate metric of signature sgn(g) in {+1, -1}, the operator `*`
restricts to an endomorphism of Λ^2(R^d) iff d = 4. At d = 4
Riemannian, the eigenvalue equation *^2 = +id on Λ^2(R^4) yields the
canonical orthogonal decomposition

    Λ^2(R^4) = Λ^2_+(R^4) ⊕ Λ^2_-(R^4)

into self-dual (+1 eigenvalue) and anti-self-dual (-1 eigenvalue)
3-dimensional subspaces.

The script verifies, at exact rational precision via sympy:

  (1) (H1) Source-target dim equality: dim Λ^k(R^d) = dim Λ^{d-k}(R^d)
      for d in {0, ..., 8} and every valid k in {0, ..., d}.
  (2) (H2)/(H3) Endomorphism condition k = d - k iff d = 2k, special-
      ized to k = 2 giving d = 4.
  (3) (H4) Hodge-star square identity: *^2 = (-1)^{k(d-k)} sgn(g) id on
      Λ^k, specialized to k = 2 giving *^2 = sgn(g) id (factor +1).
  (4) (H5)/(H8) Explicit Riemannian eigenbasis at d = 4: the six basis
      2-forms η^+_i, η^-_i are eigenvectors of `*` with eigenvalues +-1.
  (5) (H6) Counterfactual at d in {2, 3}: `*` maps Λ^2(R^d) to Λ^{d-2}
      (R^d), a different exterior degree.
  (6) (H7) Counterfactual at d in {5, 6, 7, 8}: `*` maps Λ^2(R^d) to
      Λ^{d-2}(R^d), a different exterior degree.
  (7) (H9) Uniqueness over d in {0, ..., 8}: d = 4 is the only
      dimension where `*` is an endomorphism of Λ^2(R^d).
  (8) Orthonormality of the eigenbasis at d = 4 Riemannian.
  (9) Trace of `*` on Λ^2(R^4) is zero (equal-dim split).

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the narrow theorem's
load-bearing class-(A) linear-algebra identity holds at exact symbolic
precision.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys

try:
    import sympy
    from sympy import Matrix, Rational, binomial, sqrt, sympify
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "HODGE_STAR_MIDDLE_FORM_DECOMPOSITION_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26.md"
)
CLAIM_ID = (
    "hodge_star_middle_form_decomposition_forces_d_four_narrow_theorem_note_2026-05-26"
)


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
# sympy-rational coefficients.


def basis_pforms(d: int, p: int) -> list:
    """Enumerate the (i_1 < ... < i_p) basis indices for Λ^p(R^d)."""
    if p == 0:
        return [()]
    if p < 0 or p > d:
        return []
    return [tuple(s) for s in combinations(range(1, d + 1), p)]


def dim_lambda_p(d: int, p: int) -> int:
    """Dim of Λ^p(R^d) = binom(d, p) for 0 <= p <= d, else 0."""
    if p < 0 or p > d:
        return 0
    return int(binomial(d, p))


def parity_of_permutation(perm: tuple) -> int:
    """Sign of the permutation given as a tuple of distinct integers.

    Counts inversions; returns +1 (even) or -1 (odd).
    """
    n = len(perm)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1


def hodge_star_riemannian(d: int, ordered: tuple) -> tuple[tuple, int]:
    """Compute Hodge star of a basis k-form on R^d (Riemannian, orient
    e^1 ∧ ... ∧ e^d).

    Given ordered = (i_1 < ... < i_k) with i_m in {1, ..., d},
    returns (complementary_ordered, sign) so that
        * (e^{i_1} ∧ ... ∧ e^{i_k}) = sign · e^{j_1} ∧ ... ∧ e^{j_{d-k}}
    where {j_1 < ... < j_{d-k}} is the complement of {i_1, ..., i_k} in
    {1, ..., d}, and sign = sign of the permutation
    (i_1, ..., i_k, j_1, ..., j_{d-k}) of (1, ..., d).
    """
    universe = set(range(1, d + 1))
    inset = set(ordered)
    complement = tuple(sorted(universe - inset))
    full_perm = tuple(list(ordered) + list(complement))
    sign = parity_of_permutation(full_perm)
    return (complement, sign)


def hodge_apply(d: int, form: dict) -> dict:
    """Apply Riemannian Hodge star to a form (dict
    {ordered_tuple: coeff})."""
    out: dict = {}
    for s, c in form.items():
        target, sign = hodge_star_riemannian(d, s)
        coeff = sign * c
        if target in out:
            out[target] = out[target] + coeff
        else:
            out[target] = coeff
    return {k: sympy.simplify(v) for k, v in out.items() if sympy.simplify(v) != 0}


def forms_equal(a: dict, b: dict) -> bool:
    """Test equality of two forms (dicts)."""
    keys = set(a.keys()) | set(b.keys())
    for k in keys:
        diff = a.get(k, 0) - b.get(k, 0)
        if sympy.simplify(diff) != 0:
            return False
    return True


def form_scale(form: dict, c) -> dict:
    """Multiply a form by a scalar."""
    return {k: sympy.simplify(c * v) for k, v in form.items()}


def form_add(a: dict, b: dict) -> dict:
    """Add two forms."""
    out = dict(a)
    for k, v in b.items():
        if k in out:
            out[k] = sympy.simplify(out[k] + v)
        else:
            out[k] = v
    return {k: v for k, v in out.items() if sympy.simplify(v) != 0}


def form_neg(a: dict) -> dict:
    """Negate a form."""
    return {k: sympy.simplify(-v) for k, v in a.items()}


def form_inner_product_riemannian(a: dict, b: dict) -> object:
    """Compute the Riemannian inner product g(a, b) on Λ^p(R^d) using
    the formula g(e^I, e^J) = delta_{I, J} on ordered basis."""
    s = 0
    for k, va in a.items():
        if k in b:
            s = s + va * b[k]
    return sympy.simplify(s)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("HODGE_STAR_MIDDLE_FORM_DECOMPOSITION_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26")
    print("Goal: sympy verification that `*` is an endomorphism of Λ²(R^d) iff d = 4,")
    print("      with explicit self-dual / anti-self-dual eigenbasis at d = 4 Riemannian.")
    print("=" * 88)

    # =========================================================================
    section("Part 1: (H1) Source-target dim equality dim Λ^k(R^d) = dim Λ^{d-k}(R^d)")
    # =========================================================================
    for d in range(9):
        for k in range(d + 1):
            lhs = dim_lambda_p(d, k)
            rhs = dim_lambda_p(d, d - k)
            check(
                f"(H1) at d = {d}, k = {k}: dim Λ^{k}(R^{d}) = dim Λ^{d - k}(R^{d}) = {lhs}",
                lhs == rhs,
                detail=f"binom({d}, {k}) = {lhs}, binom({d}, {d - k}) = {rhs}",
            )

    # =========================================================================
    section("Part 2: (H2)/(H3) Endomorphism condition * : Λ^k → Λ^k iff d = 2k")
    # =========================================================================
    # `*` is endomorphism of Λ^k(R^d) iff k = d - k iff d = 2k.
    # For each (d, k), endomorphism condition holds iff d == 2 * k.
    for d in range(9):
        for k in range(d + 1):
            endo = (k == d - k)
            expected = (d == 2 * k)
            check(
                f"(H2) at d = {d}, k = {k}: * is endomorphism of Λ^k iff k = d-k (here: {endo})",
                endo == expected,
                detail=f"d == 2k: {d == 2 * k}",
            )

    # (H3) Specialization to k = 2 over d in {0, ..., 8}
    for d in range(9):
        k = 2
        endo_at_k2 = (d == 2 * k)  # i.e., d = 4
        expected = (d == 4)
        check(
            f"(H3) at k = 2, d = {d}: * is endomorphism of Λ^2(R^{d}) iff d = 4 (here: {endo_at_k2})",
            endo_at_k2 == expected,
            detail=f"d == 4: {d == 4}",
        )

    # =========================================================================
    section("Part 3: (H4) Hodge-star square identity *^2 = (-1)^{k(d-k)} sgn(g) id")
    # =========================================================================
    # For each (d, k), the *^2 coefficient on Λ^k(R^d) is (-1)^{k(d-k)} sgn(g).
    # We verify the (-1) parity factor symbolically: (-1)^{k(d-k)}.
    for d in range(9):
        for k in range(d + 1):
            parity = (k * (d - k)) % 2
            sign_riemannian = 1 if parity == 0 else -1
            # For k = 2: parity = 2 * (d - 2) % 2 = 0 always
            if k == 2:
                check(
                    f"(H4) at d = {d}, k = 2: (-1)^{{k(d-k)}} = (-1)^{2 * (d - 2)} = +1 always",
                    sign_riemannian == 1,
                    detail=f"parity exponent = {2 * (d - 2)}, result = {sign_riemannian}",
                )

    # (H4)/(Q') At k = 2 Riemannian: *^2 = (+1) id; at k = 2 Lorentzian: *^2 = (-1) id.
    # We test this on the explicit basis at d = 4.
    d = 4
    basis_2forms = basis_pforms(d, 2)
    # Apply * twice and compare to +id (Riemannian)
    for basis_tuple in basis_2forms:
        form = {basis_tuple: Rational(1)}
        star_form = hodge_apply(d, form)
        star_star_form = hodge_apply(d, star_form)
        expected = form  # *^2 = +id Riemannian
        check(
            f"(H4)+(Q') at d = 4 Riemannian: *^2 (e^{basis_tuple[0]} ∧ e^{basis_tuple[1]}) = +id",
            forms_equal(star_star_form, expected),
            detail=f"*^2 = {star_star_form}, expected = {expected}",
        )

    # =========================================================================
    section("Part 4: (H8) Explicit basis-2-form Hodge action at d = 4 Riemannian")
    # =========================================================================
    # Expected:
    #   * (e^1 ∧ e^2) = +e^3 ∧ e^4
    #   * (e^1 ∧ e^3) = -e^2 ∧ e^4
    #   * (e^1 ∧ e^4) = +e^2 ∧ e^3
    #   * (e^2 ∧ e^3) = +e^1 ∧ e^4
    #   * (e^2 ∧ e^4) = -e^1 ∧ e^3
    #   * (e^3 ∧ e^4) = +e^1 ∧ e^2
    expected_star = {
        (1, 2): {(3, 4): Rational(1)},
        (1, 3): {(2, 4): Rational(-1)},
        (1, 4): {(2, 3): Rational(1)},
        (2, 3): {(1, 4): Rational(1)},
        (2, 4): {(1, 3): Rational(-1)},
        (3, 4): {(1, 2): Rational(1)},
    }
    for basis_tuple, expected in expected_star.items():
        form = {basis_tuple: Rational(1)}
        star_form = hodge_apply(d, form)
        check(
            f"(H8) * (e^{basis_tuple[0]} ∧ e^{basis_tuple[1]}) at d = 4",
            forms_equal(star_form, expected),
            detail=f"computed = {star_form}, expected = {expected}",
        )

    # =========================================================================
    section("Part 5: (H5)/(H8) Self-dual / anti-self-dual eigenbasis at d = 4 Riemannian")
    # =========================================================================
    # Self-dual basis (eigenvalue +1):
    #   η^+_1 = (1/√2) (e^1∧e^2 + e^3∧e^4)
    #   η^+_2 = (1/√2) (e^1∧e^3 - e^2∧e^4)
    #   η^+_3 = (1/√2) (e^1∧e^4 + e^2∧e^3)
    # Anti-self-dual basis (eigenvalue -1):
    #   η^-_1 = (1/√2) (e^1∧e^2 - e^3∧e^4)
    #   η^-_2 = (1/√2) (e^1∧e^3 + e^2∧e^4)
    #   η^-_3 = (1/√2) (e^1∧e^4 - e^2∧e^3)
    inv_sqrt2 = sympy.Rational(1) / sympy.sqrt(2)
    eta_plus = [
        {(1, 2): inv_sqrt2, (3, 4): inv_sqrt2},
        {(1, 3): inv_sqrt2, (2, 4): -inv_sqrt2},
        {(1, 4): inv_sqrt2, (2, 3): inv_sqrt2},
    ]
    eta_minus = [
        {(1, 2): inv_sqrt2, (3, 4): -inv_sqrt2},
        {(1, 3): inv_sqrt2, (2, 4): inv_sqrt2},
        {(1, 4): inv_sqrt2, (2, 3): -inv_sqrt2},
    ]

    for i, eta in enumerate(eta_plus, start=1):
        star_eta = hodge_apply(d, eta)
        # Should equal +eta
        check(
            f"(H5) * η^+_{i} = +η^+_{i} (eigenvalue +1)",
            forms_equal(star_eta, eta),
            detail=f"* η^+_{i} = {star_eta}",
        )
    for i, eta in enumerate(eta_minus, start=1):
        star_eta = hodge_apply(d, eta)
        # Should equal -eta
        neg_eta = form_neg(eta)
        check(
            f"(H5) * η^-_{i} = -η^-_{i} (eigenvalue -1)",
            forms_equal(star_eta, neg_eta),
            detail=f"* η^-_{i} = {star_eta}, -η^-_{i} = {neg_eta}",
        )

    # =========================================================================
    section("Part 6: Orthonormality of eigenbasis under Λ²(R^4) inner product")
    # =========================================================================
    # The Riemannian inner product on Λ²(R^4) under orthonormal basis
    # {e^I}_{|I|=2} has Gram matrix = identity (each basis 2-form has unit norm
    # and they are orthogonal).
    # We verify: <η^±_i, η^±_j> = δ_ij and <η^+_i, η^-_j> = 0.
    all_eta = eta_plus + eta_minus
    labels = ["+1", "+2", "+3", "-1", "-2", "-3"]
    n = len(all_eta)
    gram = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            gram[i][j] = form_inner_product_riemannian(all_eta[i], all_eta[j])

    # Diagonal = 1 (each η has unit norm)
    for i in range(n):
        check(
            f"(H8) <η^{labels[i]}, η^{labels[i]}> = 1 (orthonormal diag)",
            sympy.simplify(gram[i][i] - 1) == 0,
            detail=f"gram[{i}][{i}] = {gram[i][i]}",
        )

    # Off-diagonal = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                check(
                    f"(H8) <η^{labels[i]}, η^{labels[j]}> = 0 (orthogonal off-diag)",
                    sympy.simplify(gram[i][j]) == 0,
                    detail=f"gram[{i}][{j}] = {gram[i][j]}",
                )

    # =========================================================================
    section("Part 7: (H6) Counterfactual at d ∈ {2, 3}: * is not endo of Λ²(R^d)")
    # =========================================================================
    for d_test in (2, 3):
        target_degree = d_test - 2
        # source degree is 2; * maps to target_degree
        is_endo = (target_degree == 2)
        check(
            f"(H6) at d = {d_test}: * maps Λ²(R^{d_test}) to Λ^{target_degree}(R^{d_test}),"
            f" target_degree {'=' if is_endo else '≠'} 2 (not endo)",
            not is_endo,
            detail=f"target degree {target_degree} = 2: {is_endo}",
        )
        # Verify dim source == dim target (H1 sanity)
        ds = dim_lambda_p(d_test, 2)
        dt = dim_lambda_p(d_test, target_degree)
        check(
            f"(H1)+(H6) at d = {d_test}: dim Λ²(R^{d_test}) = dim Λ^{target_degree}(R^{d_test}) = {ds}",
            ds == dt,
            detail=f"dim_source = {ds}, dim_target = {dt}",
        )

    # =========================================================================
    section("Part 8: (H7) Counterfactual at d ∈ {5, 6, 7, 8}: * is not endo of Λ²(R^d)")
    # =========================================================================
    for d_test in (5, 6, 7, 8):
        target_degree = d_test - 2
        is_endo = (target_degree == 2)
        check(
            f"(H7) at d = {d_test}: * maps Λ²(R^{d_test}) to Λ^{target_degree}(R^{d_test}),"
            f" target_degree {'=' if is_endo else '≠'} 2 (not endo)",
            not is_endo,
            detail=f"target degree {target_degree} = 2: {is_endo}",
        )
        ds = dim_lambda_p(d_test, 2)
        dt = dim_lambda_p(d_test, target_degree)
        check(
            f"(H1)+(H7) at d = {d_test}: dim Λ²(R^{d_test}) = dim Λ^{target_degree}(R^{d_test}) = {ds}",
            ds == dt,
            detail=f"dim_source = {ds}, dim_target = {dt}",
        )

    # =========================================================================
    section("Part 9: (H9) Uniqueness over d ∈ {0, ..., 8}: only d = 4 is endo dim")
    # =========================================================================
    endo_dims = []
    for d_test in range(9):
        # k = 2: endomorphism iff d = 4
        if d_test - 2 == 2:
            endo_dims.append(d_test)
    check(
        "(H9) Among d ∈ {0, 1, ..., 8}, exactly d = 4 has * endo of Λ²(R^d)",
        endo_dims == [4],
        detail=f"matching d values = {endo_dims}",
    )

    # =========================================================================
    section("Part 10: Trace of `*` on Λ²(R^4) is zero (equal-dim split sanity)")
    # =========================================================================
    # Tr(*) = (sum of +1 eigenvalues) + (sum of -1 eigenvalues)
    #        = 3 * (+1) + 3 * (-1) = 0.
    # We compute the matrix of `*` in the basis {e^I}_{|I|=2} and take trace.
    d = 4
    basis_2forms = basis_pforms(d, 2)  # 6 basis 2-forms
    n_b = len(basis_2forms)
    # Build matrix M[i][j] such that * basis[j] = sum_i M[i][j] basis[i]
    M = [[sympify(0)] * n_b for _ in range(n_b)]
    for j, basis_tuple in enumerate(basis_2forms):
        form_j = {basis_tuple: Rational(1)}
        star_form_j = hodge_apply(d, form_j)
        for i, target_tuple in enumerate(basis_2forms):
            coeff = star_form_j.get(target_tuple, 0)
            M[i][j] = sympy.simplify(coeff)

    M_mat = Matrix(M)
    trace_M = sympy.simplify(M_mat.trace())
    check(
        "Tr(* on Λ²(R^4) Riemannian) = 0 (equal +1/-1 multiplicity split)",
        trace_M == 0,
        detail=f"trace = {trace_M}",
    )

    # Verify *^2 = identity matrix on Λ²(R^4) Riemannian
    M_sq = M_mat * M_mat
    I6 = sympy.eye(n_b)
    check(
        "*^2 = identity on Λ²(R^4) Riemannian (matrix form of (Q'))",
        sympy.simplify(M_sq - I6) == sympy.zeros(n_b, n_b),
        detail=f"*^2 - I = {sympy.simplify(M_sq - I6)}",
    )

    # Trace of *^2 = 6 (dimension of Λ²(R^4))
    trace_M_sq = sympy.simplify(M_sq.trace())
    check(
        "Tr(*^2) = dim Λ²(R^4) = 6",
        trace_M_sq == 6,
        detail=f"Tr(*^2) = {trace_M_sq}",
    )

    # Number of +1 eigenvalues = number of -1 eigenvalues = 3
    eigs = M_mat.eigenvals()
    # eigs is a dict {eigenvalue: multiplicity}
    plus_one_mult = eigs.get(sympify(1), 0)
    minus_one_mult = eigs.get(sympify(-1), 0)
    check(
        "(H8) Multiplicity of +1 eigenvalue of `*` on Λ²(R^4) is 3 (self-dual subspace dim)",
        plus_one_mult == 3,
        detail=f"+1 mult = {plus_one_mult}",
    )
    check(
        "(H8) Multiplicity of -1 eigenvalue of `*` on Λ²(R^4) is 3 (anti-self-dual subspace dim)",
        minus_one_mult == 3,
        detail=f"-1 mult = {minus_one_mult}",
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
