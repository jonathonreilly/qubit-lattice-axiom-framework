#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is purely finite-dimensional
real matrix algebra on C^3 and C^2:

  (S1)    spec(F00) = {1, 0, 0}.
  (S2)    spec(F_row) = {1, 0}.
  (E1)    F00^2 = F00 (idempotency on C^3).
  (E2)    F_row^2 = F_row (idempotency on C^2).
  (Trace) Tr F00 = 1, Tr F_row = 1.
  (DG3)   det(m I_3 + j F00) = m^2 (m + j) = m^3 (1 + j/m).
  (DG2)   det(m I_2 + j F_row) = m (m + j) = m^2 (1 + j/m).
  (W)     Equal-baseline-subtracted response match for F00 vs F_row.
  (R1)    Tr(H_core · F00) = (A + 4 b + 2 c + 2 d)/3 on generic symbols.
  (R2)    Tr(B · F00) = 0 for the parent's antisymmetric breaking triplet
          B(δ, ρ, γ).

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
    print("DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy verification of the finite-dimensional algebraic identities")
    print("      (S1)-(S2), (E1)-(E2), (DG3)-(DG2), (W), (R1)-(R2) at exact precision")
    print("=" * 88)

    # =========================================================================
    section("Part 0: explicit F00 = J3/3 and F_row = J2/2")
    # =========================================================================

    J3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    J2 = Matrix([[1, 1], [1, 1]])
    F00 = J3 / 3
    F_row = J2 / 2

    # =========================================================================
    section("Part 1: (E1), (E2) idempotency; (Trace) traces")
    # =========================================================================

    check(
        "(E1) F00^2 = F00 on C^3",
        matrix_eq(F00 * F00, F00),
    )
    check(
        "(E2) F_row^2 = F_row on C^2",
        matrix_eq(F_row * F_row, F_row),
    )
    check(
        "(Trace) Tr F00 = 1",
        sympy.simplify(F00.trace() - 1) == 0,
        detail=f"Tr F00 = {F00.trace()}",
    )
    check(
        "(Trace) Tr F_row = 1",
        sympy.simplify(F_row.trace() - 1) == 0,
        detail=f"Tr F_row = {F_row.trace()}",
    )

    # All-ones-square identities J3^2 = 3 J3, J2^2 = 2 J2.
    check(
        "(aux) J3^2 = 3 J3 on C^3",
        matrix_eq(J3 * J3, 3 * J3),
    )
    check(
        "(aux) J2^2 = 2 J2 on C^2",
        matrix_eq(J2 * J2, 2 * J2),
    )

    # =========================================================================
    section("Part 2: (S1), (S2) spectra of F00, F_row")
    # =========================================================================

    eigs_F00 = F00.eigenvals()
    # Should be {1: 1, 0: 2}
    n_ones_F00 = eigs_F00.get(sympy.Integer(1), 0)
    n_zeros_F00 = eigs_F00.get(sympy.Integer(0), 0)
    check(
        "(S1) spec(F00) = {1, 0, 0} (multiplicities (1, 2))",
        n_ones_F00 == 1 and n_zeros_F00 == 2,
        detail=f"eigs F00 = {eigs_F00}",
    )

    eigs_F_row = F_row.eigenvals()
    n_ones_F_row = eigs_F_row.get(sympy.Integer(1), 0)
    n_zeros_F_row = eigs_F_row.get(sympy.Integer(0), 0)
    check(
        "(S2) spec(F_row) = {1, 0} (multiplicities (1, 1))",
        n_ones_F_row == 1 and n_zeros_F_row == 1,
        detail=f"eigs F_row = {eigs_F_row}",
    )

    # =========================================================================
    section("Part 3: (DG3), (DG2) determinant identities at exact symbolic (m, j)")
    # =========================================================================

    m_sym = Symbol("m", real=True, nonzero=True)
    j_sym = Symbol("j", real=True)

    # det(m I_3 + j F00) = (m + j) * m * m = m^2 (m + j)
    det_F00 = sympy.simplify((m_sym * eye(3) + j_sym * F00).det())
    target_F00 = m_sym ** 2 * (m_sym + j_sym)
    check(
        "(DG3) det(m I_3 + j F00) = m^2 (m + j) = m^3 (1 + j/m)",
        sympy.simplify(det_F00 - target_F00) == 0,
        detail=f"det = {det_F00}",
    )

    # det(m I_2 + j F_row) = (m + j) * m = m (m + j)
    det_F_row = sympy.simplify((m_sym * eye(2) + j_sym * F_row).det())
    target_F_row = m_sym * (m_sym + j_sym)
    check(
        "(DG2) det(m I_2 + j F_row) = m (m + j) = m^2 (1 + j/m)",
        sympy.simplify(det_F_row - target_F_row) == 0,
        detail=f"det = {det_F_row}",
    )

    # =========================================================================
    section("Part 4: (W) equal-baseline-subtracted response identity")
    # =========================================================================

    # ratio_3 := det(m I_3 + j F00) / m^3 = 1 + j/m
    # ratio_2 := det(m I_2 + j F_row) / m^2 = 1 + j/m
    ratio_F00 = sympy.simplify(det_F00 / m_sym ** 3)
    ratio_F_row = sympy.simplify(det_F_row / m_sym ** 2)
    check(
        "(W.symb) det(m I_3 + j F00)/m^3 = 1 + j/m at exact symbolic (m, j)",
        sympy.simplify(ratio_F00 - (1 + j_sym / m_sym)) == 0,
        detail=f"ratio_F00 = {ratio_F00}",
    )
    check(
        "(W.symb) det(m I_2 + j F_row)/m^2 = 1 + j/m at exact symbolic (m, j)",
        sympy.simplify(ratio_F_row - (1 + j_sym / m_sym)) == 0,
        detail=f"ratio_F_row = {ratio_F_row}",
    )
    check(
        "(W.symb) baselines match: det(m I_3 + j F00)/m^3 = det(m I_2 + j F_row)/m^2",
        sympy.simplify(ratio_F00 - ratio_F_row) == 0,
        detail="both ratios = 1 + j/m",
    )

    # Rational sanity at three (m, j) pairs
    rationals_mj = [(Rational(1), Rational(1, 5)), (Rational(2), Rational(3, 10)), (Rational(3), Rational(7, 10))]

    for m_val, j_val in rationals_mj:
        W_F00 = sympy.simplify(
            log(sympy.Abs(det_F00.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 3))
        )
        W_F_row = sympy.simplify(
            log(sympy.Abs(det_F_row.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 2))
        )
        target_W = sympy.simplify(log(sympy.Abs(1 + j_val / m_val)))
        check(
            f"(W) F00 and F_row have identical response at (m,j) = ({m_val}, {j_val})",
            sympy.simplify(W_F00 - W_F_row) == 0
            and sympy.simplify(W_F00 - target_W) == 0,
            detail=f"W_F00 = {W_F00}, W_F_row = {W_F_row}, target = {target_W}",
        )

    # =========================================================================
    section("Part 5: (R1) Tr(H_core · F00) = (A + 4 b + 2 c + 2 d)/3 on generic symbols")
    # =========================================================================

    A_, b_, c_, d_ = symbols("A b c d", real=True)
    H_core = Matrix([[A_, b_, b_], [b_, c_, d_], [b_, d_, c_]])
    pairing = sympy.simplify((H_core * F00).trace())
    target_R1 = (A_ + 4 * b_ + 2 * c_ + 2 * d_) / 3
    check(
        "(R1) Tr(H_core · F00) = (A + 4 b + 2 c + 2 d)/3 on generic real symbols",
        sympy.simplify(pairing - target_R1) == 0,
        detail=f"Tr(H_core · F00) = {pairing}",
    )

    # =========================================================================
    section("Part 6: (R2) (δ, ρ, γ)-independence — Tr(B · F00) = 0")
    # =========================================================================

    delta_, rho_, gamma_ = symbols("delta rho gamma", real=True)
    # B(δ, ρ, γ) per the parent k00 row:
    # B = [[0, ρ, -ρ - i γ], [ρ, δ, 0], [-ρ + i γ, 0, -δ]]
    # The runner takes the real part (the parent uses Hermitian H = H_core + Hermitian part of B);
    # but for the (δ, ρ, γ)-independence trace identity it suffices to compute
    # Tr(B · F00) symbolically and verify it vanishes when the diagonal sum
    # of (δ, -δ) entries cancel and the off-diagonal ρ contributions trace to 0.

    sym_I = sympy.I
    B = Matrix(
        [
            [0, rho_, -rho_ - sym_I * gamma_],
            [rho_, delta_, 0],
            [-rho_ + sym_I * gamma_, 0, -delta_],
        ]
    )
    tr_B_F00 = sympy.simplify((B * F00).trace())
    check(
        "(R2) Tr(B · F00) = 0 identically in (δ, ρ, γ) (breaking-triplet independence)",
        sympy.simplify(tr_B_F00) == 0,
        detail=f"Tr(B · F00) = {tr_B_F00}",
    )

    # =========================================================================
    section("Part 7: counterfactual — non-scalar baseline D = diag(m_1, m_2, m_3) breaks (W)")
    # =========================================================================

    # Take m_1 = 2, m_2 = 3, m_3 = 5 on C^3 and m_1' = 2, m_2' = 3 on C^2.

    m1, m2, m3 = Rational(2), Rational(3), Rational(5)
    j_cf = Rational(1, 4)
    D3 = diag(m1, m2, m3)
    D2 = diag(m1, m2)
    det_F00_cf = sympy.simplify((D3 + j_cf * F00).det())
    det_F_row_cf = sympy.simplify((D2 + j_cf * F_row).det())
    W_F00_cf = sympy.simplify(log(sympy.Abs(det_F00_cf)) - log(sympy.Abs(D3.det())))
    W_F_row_cf = sympy.simplify(log(sympy.Abs(det_F_row_cf)) - log(sympy.Abs(D2.det())))
    check(
        "(cf) non-scalar baseline D = diag(2,3,5) vs diag(2,3) breaks the (W) match for F00 vs F_row",
        sympy.simplify(W_F00_cf - W_F_row_cf) != 0,
        detail=f"W_F00 = {W_F00_cf}, W_F_row = {W_F_row_cf}, difference = {sympy.simplify(W_F00_cf - W_F_row_cf)}",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print("  Verified at exact sympy precision on C^3 and C^2:")
    print("    (E1) F00^2 = F00 (idempotency)")
    print("    (E2) F_row^2 = F_row (idempotency)")
    print("    (Tr) Tr F00 = Tr F_row = 1")
    print("    (S1) spec(F00) = {1, 0, 0}")
    print("    (S2) spec(F_row) = {1, 0}")
    print("    (DG3) det(m I_3 + j F00) = m^2 (m + j) = m^3 (1 + j/m)")
    print("    (DG2) det(m I_2 + j F_row) = m (m + j) = m^2 (1 + j/m)")
    print("    (W)  Equal-baseline-subtracted response identity: both = log|1 + j/m|")
    print("    (R1) Tr(H_core · F00) = (A + 4 b + 2 c + 2 d)/3 on generic real (A, b, c, d)")
    print("    (R2) Tr(B(δ, ρ, γ) · F00) = 0 identically")
    print("    Counterfactual: non-scalar baseline D = diag(2,3,5) vs diag(2,3) breaks (W)")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
