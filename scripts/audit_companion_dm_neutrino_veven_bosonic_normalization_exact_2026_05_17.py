#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`DM_NEUTRINO_VEVEN_BOSONIC_NORMALIZATION_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is purely finite-dimensional
real matrix algebra on C^3 and C^2:

  (G)  Frobenius-orthogonality of the active basis
       {A_op, b_op, c_op, d_op, T_delta, T_rho}.
  (D1) Tr(H · F1) = E1(H) on generic real coefficients.
  (D2) Tr(H · F2) = E2(H) on generic real coefficients.
  (S1) spec(F1) = {-sqrt(3/8), 0, +sqrt(3/8)}.
  (S2) spec(F2) = {-3/sqrt(8), 0, +3/sqrt(8)}.
  (S3) spec(sqrt(3/8) Z_row) = {-sqrt(3/8), +sqrt(3/8)}.
  (S4) spec((3/sqrt(8)) Z_row) = {-3/sqrt(8), +3/sqrt(8)}.
  (W1) Equal-baseline-subtracted response match for F1 vs sqrt(3/8) Z_row.
  (W2) Equal-baseline-subtracted response match for F2 vs (3/sqrt(8)) Z_row.

Counterfactual: a non-scalar baseline D = diag(m_1, m_2, m_3) with
m_1 != m_2 != m_3 breaks the equal-baseline-subtracted match,
confirming that the scalar baseline D = m I is load-bearing on the
algebraic identity.

No upstream-ledger authority is load-bearing on this runner. The
companion verifies the finite-dimensional algebra at exact sympy
precision.
"""

from __future__ import annotations

import sys

try:
    import sympy
    from sympy import (
        Matrix,
        Rational,
        Symbol,
        diag,
        eye,
        log,
        sqrt,
        symbols,
        zeros,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


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


def matrix_eq(A: Matrix, B: Matrix) -> bool:
    """Exact sympy matrix equality via sympy.simplify on every entry."""
    if A.shape != B.shape:
        return False
    diff = A - B
    for i in range(diff.rows):
        for j in range(diff.cols):
            if sympy.simplify(diff[i, j]) != 0:
                return False
    return True


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("DM_NEUTRINO_VEVEN_BOSONIC_NORMALIZATION_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy verification of the finite-dimensional algebraic identities")
    print("      (G), (D1)-(D2), (S1)-(S4), (W1)-(W2) at exact precision")
    print("=" * 88)

    # =========================================================================
    section("Part 0: explicit 3x3 active basis and 2x2 source row-contrast")
    # =========================================================================

    A_op = Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    b_op = Matrix([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    c_op = Matrix([[0, 0, 0], [0, 1, 0], [0, 0, 1]])
    d_op = Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    T_delta = Matrix([[0, 0, 0], [0, 1, 0], [0, 0, -1]])
    T_rho = Matrix([[0, 1, -1], [1, 0, 0], [-1, 0, 0]])

    basis = [A_op, b_op, c_op, d_op, T_delta, T_rho]
    basis_names = ["A_op", "b_op", "c_op", "d_op", "T_delta", "T_rho"]

    Z_row = Matrix([[1, 0], [0, -1]])

    # =========================================================================
    section("Part 1: (G) Frobenius-orthogonality of the active basis")
    # =========================================================================

    gram = Matrix(
        6, 6, lambda i, j: (basis[i].T * basis[j]).trace()
    )
    expected_diag = [1, 4, 2, 2, 2, 4]
    diag_match = all(sympy.simplify(gram[k, k] - expected_diag[k]) == 0 for k in range(6))
    offdiag_zero = all(
        sympy.simplify(gram[i, j]) == 0
        for i in range(6)
        for j in range(6)
        if i != j
    )
    check(
        "(G) Frobenius-orthogonality: diagonal magnitudes (1, 4, 2, 2, 2, 4) match",
        diag_match,
        detail=f"diag(Gram) = {[gram[k, k] for k in range(6)]}",
    )
    check(
        "(G) Frobenius-orthogonality: off-diagonal entries all zero",
        offdiag_zero,
    )

    # =========================================================================
    section("Part 2: (F1), (F2) Frobenius-dual generators and trace pairings (D1), (D2)")
    # =========================================================================

    F1 = Rational(1, 2) * T_delta + Rational(1, 4) * T_rho
    F2 = A_op + Rational(1, 4) * b_op - Rational(1, 2) * c_op - Rational(1, 2) * d_op

    alpha, beta_, gamma_, delta_, eps_, zeta_ = symbols("alpha beta gamma delta eps zeta", real=True)
    H_generic = alpha * A_op + beta_ * b_op + gamma_ * c_op + delta_ * d_op + eps_ * T_delta + zeta_ * T_rho

    E1_expected = eps_ + zeta_
    E2_expected = alpha + beta_ - gamma_ - delta_

    pairing_F1 = sympy.simplify((H_generic.T * F1).trace())
    pairing_F2 = sympy.simplify((H_generic.T * F2).trace())

    check(
        "(D1) Tr(H · F1) = ε + ζ = E1(H) on generic real coefficients",
        sympy.simplify(pairing_F1 - E1_expected) == 0,
        detail=f"Tr(H·F1) = {pairing_F1}",
    )
    check(
        "(D2) Tr(H · F2) = α + β - γ - δ = E2(H) on generic real coefficients",
        sympy.simplify(pairing_F2 - E2_expected) == 0,
        detail=f"Tr(H·F2) = {pairing_F2}",
    )

    # =========================================================================
    section("Part 3: (S1)-(S4) spectra of F1, F2, scaled Z_row")
    # =========================================================================

    lam = Symbol("lam")

    # F1: characteristic polynomial
    char_F1 = sympy.simplify((F1 - lam * eye(3)).det())
    char_F1_target = -lam ** 3 + Rational(3, 8) * lam
    check(
        "(C1) char poly of F1 is -λ^3 + (3/8) λ",
        sympy.simplify(char_F1 - char_F1_target) == 0,
        detail=f"char F1 = {char_F1}",
    )
    # Roots: 0, ±sqrt(3/8)
    eigs_F1 = F1.eigenvals()
    F1_target_eigs = {
        sympy.Integer(0): 1,
        sqrt(Rational(3, 8)): 1,
        -sqrt(Rational(3, 8)): 1,
    }
    # Normalize sympy keys (may appear as -sqrt(3)/(2*sqrt(2)) etc.)
    check(
        "(S1) spec(F1) = {-sqrt(3/8), 0, +sqrt(3/8)} (multiplicities (1,1,1))",
        sympy.simplify(sum(k * v for k, v in eigs_F1.items())) == 0
        and sympy.simplify(sum(k ** 2 * v for k, v in eigs_F1.items()) - Rational(3, 4)) == 0
        and sum(eigs_F1.values()) == 3,
        detail=f"eigs F1 = {eigs_F1}",
    )

    # F2: characteristic polynomial
    char_F2 = sympy.simplify((F2 - lam * eye(3)).det())
    char_F2_target = -lam ** 3 + Rational(9, 8) * lam
    check(
        "(C2) char poly of F2 is -λ^3 + (9/8) λ",
        sympy.simplify(char_F2 - char_F2_target) == 0,
        detail=f"char F2 = {char_F2}",
    )
    eigs_F2 = F2.eigenvals()
    # Roots: 0, ±3/sqrt(8)
    check(
        "(S2) spec(F2) = {-3/sqrt(8), 0, +3/sqrt(8)} (multiplicities (1,1,1))",
        sympy.simplify(sum(k * v for k, v in eigs_F2.items())) == 0
        and sympy.simplify(sum(k ** 2 * v for k, v in eigs_F2.items()) - Rational(9, 4)) == 0
        and sum(eigs_F2.values()) == 3,
        detail=f"eigs F2 = {eigs_F2}",
    )

    # Z_row scaled
    a1 = sqrt(Rational(3, 8))
    a2 = 3 / sqrt(8)
    S1 = a1 * Z_row
    S2 = a2 * Z_row
    eigs_S1 = S1.eigenvals()
    eigs_S2 = S2.eigenvals()

    check(
        "(S3) spec(sqrt(3/8) Z_row) = {-sqrt(3/8), +sqrt(3/8)} (multiplicities (1,1))",
        sympy.simplify(sum(k * v for k, v in eigs_S1.items())) == 0
        and sympy.simplify(sum(k ** 2 * v for k, v in eigs_S1.items()) - Rational(3, 4)) == 0
        and sum(eigs_S1.values()) == 2,
        detail=f"eigs sqrt(3/8) Z = {eigs_S1}",
    )
    check(
        "(S4) spec((3/sqrt(8)) Z_row) = {-3/sqrt(8), +3/sqrt(8)} (multiplicities (1,1))",
        sympy.simplify(sum(k * v for k, v in eigs_S2.items())) == 0
        and sympy.simplify(sum(k ** 2 * v for k, v in eigs_S2.items()) - Rational(9, 4)) == 0
        and sum(eigs_S2.values()) == 2,
        detail=f"eigs (3/sqrt(8)) Z = {eigs_S2}",
    )

    # =========================================================================
    section("Part 4: (DG1), (DS1), (DG2), (DS2) determinant identities at exact symbolic (m, j)")
    # =========================================================================

    m_sym = Symbol("m", real=True, nonzero=True)
    j_sym = Symbol("j", real=True)

    # det(m I_3 + j F1) = m^3 (1 - (3/8) j^2/m^2) = m (m^2 - (3/8) j^2)
    det_F1 = sympy.simplify((m_sym * eye(3) + j_sym * F1).det())
    target_F1 = m_sym ** 3 - Rational(3, 8) * m_sym * j_sym ** 2
    check(
        "(DG1) det(m I_3 + j F1) = m^3 - (3/8) m j^2 = m^3 (1 - (3/8) j^2/m^2)",
        sympy.simplify(det_F1 - target_F1) == 0,
        detail=f"det = {det_F1}",
    )

    # det(m I_2 + j sqrt(3/8) Z_row) = m^2 - (3/8) j^2
    det_S1 = sympy.simplify((m_sym * eye(2) + j_sym * S1).det())
    target_S1 = m_sym ** 2 - Rational(3, 8) * j_sym ** 2
    check(
        "(DS1) det(m I_2 + j sqrt(3/8) Z_row) = m^2 - (3/8) j^2",
        sympy.simplify(det_S1 - target_S1) == 0,
        detail=f"det = {det_S1}",
    )

    # det(m I_3 + j F2) = m^3 - (9/8) m j^2
    det_F2 = sympy.simplify((m_sym * eye(3) + j_sym * F2).det())
    target_F2 = m_sym ** 3 - Rational(9, 8) * m_sym * j_sym ** 2
    check(
        "(DG2) det(m I_3 + j F2) = m^3 - (9/8) m j^2 = m^3 (1 - (9/8) j^2/m^2)",
        sympy.simplify(det_F2 - target_F2) == 0,
        detail=f"det = {det_F2}",
    )

    # det(m I_2 + j (3/sqrt(8)) Z_row) = m^2 - (9/8) j^2
    det_S2 = sympy.simplify((m_sym * eye(2) + j_sym * S2).det())
    target_S2 = m_sym ** 2 - Rational(9, 8) * j_sym ** 2
    check(
        "(DS2) det(m I_2 + j (3/sqrt(8)) Z_row) = m^2 - (9/8) j^2",
        sympy.simplify(det_S2 - target_S2) == 0,
        detail=f"det = {det_S2}",
    )

    # =========================================================================
    section("Part 5: (W1), (W2) equal-baseline-subtracted response identity at exact rationals")
    # =========================================================================

    # W[j M] := log|det(m I + j M)| - log|det(m I)|
    # For F1 vs sqrt(3/8) Z_row, both should equal log|1 - (3/8) j^2/m^2|.

    rationals_mj = [(Rational(1, 1), Rational(1, 5)), (Rational(2, 1), Rational(3, 10)), (Rational(3, 1), Rational(7, 10))]

    for m_val, j_val in rationals_mj:
        W_F1 = sympy.simplify(
            log(sympy.Abs(det_F1.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 3))
        )
        W_S1 = sympy.simplify(
            log(sympy.Abs(det_S1.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 2))
        )
        target_W = sympy.simplify(log(sympy.Abs(1 - Rational(3, 8) * j_val ** 2 / m_val ** 2)))
        check(
            f"(W1) F1 and sqrt(3/8) Z_row have identical response at (m,j) = ({m_val}, {j_val})",
            sympy.simplify(W_F1 - W_S1) == 0
            and sympy.simplify(W_F1 - target_W) == 0,
            detail=f"W_F1 = {W_F1}, W_S1 = {W_S1}, target = {target_W}",
        )

    for m_val, j_val in rationals_mj:
        W_F2 = sympy.simplify(
            log(sympy.Abs(det_F2.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 3))
        )
        W_S2 = sympy.simplify(
            log(sympy.Abs(det_S2.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 2))
        )
        target_W = sympy.simplify(log(sympy.Abs(1 - Rational(9, 8) * j_val ** 2 / m_val ** 2)))
        check(
            f"(W2) F2 and (3/sqrt(8)) Z_row have identical response at (m,j) = ({m_val}, {j_val})",
            sympy.simplify(W_F2 - W_S2) == 0
            and sympy.simplify(W_F2 - target_W) == 0,
            detail=f"W_F2 = {W_F2}, W_S2 = {W_S2}, target = {target_W}",
        )

    # =========================================================================
    section("Part 6: exact-symbolic determinant polynomial match for (W1), (W2)")
    # =========================================================================

    # The strongest form: the equal-baseline-subtracted response is a function
    # of (j/m) alone, and the two sides match identically as functions of
    # (m, j). Verify by showing det_F1 / m^3 = det_S1 / m^2 (after baseline
    # subtraction) symbolically.

    ratio_F1 = sympy.simplify(det_F1 / m_sym ** 3)
    ratio_S1 = sympy.simplify(det_S1 / m_sym ** 2)
    check(
        "(W1.symb) det(m I_3 + j F1)/m^3 = det(m I_2 + j sqrt(3/8) Z_row)/m^2 = 1 - (3/8) j^2/m^2",
        sympy.simplify(ratio_F1 - ratio_S1) == 0
        and sympy.simplify(ratio_F1 - (1 - Rational(3, 8) * j_sym ** 2 / m_sym ** 2)) == 0,
        detail=f"ratio_F1 = {ratio_F1}, ratio_S1 = {ratio_S1}",
    )

    ratio_F2 = sympy.simplify(det_F2 / m_sym ** 3)
    ratio_S2 = sympy.simplify(det_S2 / m_sym ** 2)
    check(
        "(W2.symb) det(m I_3 + j F2)/m^3 = det(m I_2 + j (3/sqrt(8)) Z_row)/m^2 = 1 - (9/8) j^2/m^2",
        sympy.simplify(ratio_F2 - ratio_S2) == 0
        and sympy.simplify(ratio_F2 - (1 - Rational(9, 8) * j_sym ** 2 / m_sym ** 2)) == 0,
        detail=f"ratio_F2 = {ratio_F2}, ratio_S2 = {ratio_S2}",
    )

    # =========================================================================
    section("Part 7: counterfactual — non-scalar baseline D = diag(m_1, m_2, m_3) breaks (W1)/(W2)")
    # =========================================================================

    # Take m_1 = 2, m_2 = 3, m_3 = 5 on C^3 and m_1' = 2, m_2' = 3 on C^2.
    # The baseline-subtracted response for F1 vs sqrt(3/8) Z_row should
    # differ.

    m1, m2, m3 = Rational(2), Rational(3), Rational(5)
    j_cf = Rational(1, 4)
    D3 = diag(m1, m2, m3)
    D2 = diag(m1, m2)
    det_F1_cf = sympy.simplify((D3 + j_cf * F1).det())
    det_S1_cf = sympy.simplify((D2 + j_cf * S1).det())
    W_F1_cf = sympy.simplify(log(sympy.Abs(det_F1_cf)) - log(sympy.Abs(D3.det())))
    W_S1_cf = sympy.simplify(log(sympy.Abs(det_S1_cf)) - log(sympy.Abs(D2.det())))
    check(
        "(cf) non-scalar baseline D = diag(2,3,5) vs diag(2,3) breaks the (W1) match for F1",
        sympy.simplify(W_F1_cf - W_S1_cf) != 0,
        detail=f"W_F1 = {W_F1_cf}, W_S1 = {W_S1_cf}, difference = {sympy.simplify(W_F1_cf - W_S1_cf)}",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print("  Verified at exact sympy precision on C^3 and C^2:")
    print("    (G)  Frobenius-orthogonality of the active basis")
    print("    (D1) Tr(H · F1) = E1(H) = ε + ζ on generic real coefficients")
    print("    (D2) Tr(H · F2) = E2(H) = α + β - γ - δ on generic real coefficients")
    print("    (S1) spec(F1) = {-sqrt(3/8), 0, +sqrt(3/8)}")
    print("    (S2) spec(F2) = {-3/sqrt(8), 0, +3/sqrt(8)}")
    print("    (S3) spec(sqrt(3/8) Z_row) = {-sqrt(3/8), +sqrt(3/8)}")
    print("    (S4) spec((3/sqrt(8)) Z_row) = {-3/sqrt(8), +3/sqrt(8)}")
    print("    (W1) F1 ↔ sqrt(3/8) Z_row identical exact bosonic response on m I baseline")
    print("    (W2) F2 ↔ (3/sqrt(8)) Z_row identical exact bosonic response on m I baseline")
    print("    Counterfactual: non-scalar baseline D = diag(2,3,5) vs diag(2,3) breaks (W1)")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
