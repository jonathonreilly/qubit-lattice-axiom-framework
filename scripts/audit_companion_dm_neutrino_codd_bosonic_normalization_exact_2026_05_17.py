#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`DM_NEUTRINO_CODD_BOSONIC_NORMALIZATION_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem's load-bearing content is purely finite-dimensional
matrix algebra on C^4, C^3, and C^2:

  (S1)   spec(S_cls)    = {+1, -1, 0, 0}.
  (S2)   spec(T_gamma)  = {+1, -1, 0}.
  (S3)   spec(Z_odd)    = {+1, -1}.
  (E1)   S_cls^3   = S_cls   (cubic involution on C^4).
  (E2)   T_gamma^3 = T_gamma (cubic involution on C^3).
  (E3)   Z_odd^3   = Z_odd   (cubic involution on C^2).
  (Herm) S_cls = S_cls^H, T_gamma = T_gamma^H, Z_odd = Z_odd^H.
  (Trace) Tr S_cls = 0, Tr T_gamma = 0, Tr Z_odd = 0.
  (DG4)  det(m I_4 + j S_cls)   = m^2 (m^2 - j^2) = m^4 (1 - j^2/m^2).
  (DG3)  det(m I_3 + j T_gamma) = m (m^2 - j^2)   = m^3 (1 - j^2/m^2).
  (DG2)  det(m I_2 + j Z_odd)   = m^2 - j^2       = m^2 (1 - j^2/m^2).
  (W)    Equal-baseline-subtracted response triple match for
         S_cls / T_gamma / Z_odd on scalar baseline D = m I.
  (R1)   Small-source curvature ∂^2 W / ∂j^2 |_{j=0} = -2/m^2 matches
         across all three generators.

Counterfactual: a non-scalar baseline D = diag(m_1, m_2, m_3, m_4) on
C^4 and diag(m_1, m_2, m_3) on C^3 and diag(m_1, m_2) on C^2 with
distinct entries breaks the equal-baseline-subtracted match,
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
        I,
        Matrix,
        Rational,
        Symbol,
        diag,
        diff,
        eye,
        log,
        symbols,
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
    diff_M = A - B
    for i in range(diff_M.rows):
        for j in range(diff_M.cols):
            if sympy.simplify(diff_M[i, j]) != 0:
                return False
    return True


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("DM_NEUTRINO_CODD_BOSONIC_NORMALIZATION_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy verification of the finite-dimensional algebraic identities")
    print("      (S1)-(S3), (E1)-(E3), (Herm), (Trace), (DG4)-(DG2), (W), (R1)")
    print("      at exact precision")
    print("=" * 88)

    # =========================================================================
    section("Part 0: explicit generators S_cls (C^4), T_gamma (C^3), Z_odd (C^2)")
    # =========================================================================

    S_cls = Matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1],
        ]
    )
    T_gamma = Matrix(
        [
            [0, 0, -I],
            [0, 0, 0],
            [I, 0, 0],
        ]
    )
    Z_odd = Matrix(
        [
            [1, 0],
            [0, -1],
        ]
    )

    # =========================================================================
    section("Part 1: (Herm) Hermiticity and (Trace) traces")
    # =========================================================================

    check(
        "(Herm) S_cls = S_cls^H on C^4",
        matrix_eq(S_cls, S_cls.H),
    )
    check(
        "(Herm) T_gamma = T_gamma^H on C^3",
        matrix_eq(T_gamma, T_gamma.H),
    )
    check(
        "(Herm) Z_odd = Z_odd^H on C^2",
        matrix_eq(Z_odd, Z_odd.H),
    )
    check(
        "(Trace) Tr S_cls = 0",
        sympy.simplify(S_cls.trace()) == 0,
        detail=f"Tr S_cls = {S_cls.trace()}",
    )
    check(
        "(Trace) Tr T_gamma = 0",
        sympy.simplify(T_gamma.trace()) == 0,
        detail=f"Tr T_gamma = {T_gamma.trace()}",
    )
    check(
        "(Trace) Tr Z_odd = 0",
        sympy.simplify(Z_odd.trace()) == 0,
        detail=f"Tr Z_odd = {Z_odd.trace()}",
    )

    # =========================================================================
    section("Part 2: (S1)-(S3) spectra of the three generators")
    # =========================================================================

    eigs_S_cls = S_cls.eigenvals()
    n_pos_S = eigs_S_cls.get(sympy.Integer(1), 0)
    n_neg_S = eigs_S_cls.get(sympy.Integer(-1), 0)
    n_zero_S = eigs_S_cls.get(sympy.Integer(0), 0)
    check(
        "(S1) spec(S_cls) = {+1, -1, 0, 0} (multiplicities (1, 1, 2))",
        n_pos_S == 1 and n_neg_S == 1 and n_zero_S == 2,
        detail=f"eigs S_cls = {eigs_S_cls}",
    )

    eigs_T_gamma = T_gamma.eigenvals()
    n_pos_T = eigs_T_gamma.get(sympy.Integer(1), 0)
    n_neg_T = eigs_T_gamma.get(sympy.Integer(-1), 0)
    n_zero_T = eigs_T_gamma.get(sympy.Integer(0), 0)
    check(
        "(S2) spec(T_gamma) = {+1, -1, 0} (multiplicities (1, 1, 1))",
        n_pos_T == 1 and n_neg_T == 1 and n_zero_T == 1,
        detail=f"eigs T_gamma = {eigs_T_gamma}",
    )

    eigs_Z_odd = Z_odd.eigenvals()
    n_pos_Z = eigs_Z_odd.get(sympy.Integer(1), 0)
    n_neg_Z = eigs_Z_odd.get(sympy.Integer(-1), 0)
    check(
        "(S3) spec(Z_odd) = {+1, -1} (multiplicities (1, 1))",
        n_pos_Z == 1 and n_neg_Z == 1,
        detail=f"eigs Z_odd = {eigs_Z_odd}",
    )

    # Characteristic polynomial cross-checks
    lam = Symbol("lam")
    char_S = sympy.simplify((S_cls - lam * eye(4)).det())
    char_T = sympy.simplify((T_gamma - lam * eye(3)).det())
    char_Z = sympy.simplify((Z_odd - lam * eye(2)).det())
    char_S_target = lam ** 4 - lam ** 2
    char_T_target = -lam ** 3 + lam
    char_Z_target = lam ** 2 - 1
    check(
        "(C1) char poly S_cls = λ^4 - λ^2 = λ^2 (λ-1)(λ+1)",
        sympy.simplify(char_S - char_S_target) == 0,
        detail=f"char S_cls = {char_S}",
    )
    check(
        "(C2) char poly T_gamma = -λ^3 + λ = -λ (λ-1)(λ+1)",
        sympy.simplify(char_T - char_T_target) == 0,
        detail=f"char T_gamma = {char_T}",
    )
    check(
        "(C3) char poly Z_odd = λ^2 - 1 = (λ-1)(λ+1)",
        sympy.simplify(char_Z - char_Z_target) == 0,
        detail=f"char Z_odd = {char_Z}",
    )

    # =========================================================================
    section("Part 3: (E1)-(E3) cubic involution identities M^3 = M")
    # =========================================================================

    check(
        "(E1) S_cls^3 = S_cls on C^4",
        matrix_eq(S_cls ** 3, S_cls),
    )
    check(
        "(E2) T_gamma^3 = T_gamma on C^3",
        matrix_eq(T_gamma ** 3, T_gamma),
    )
    check(
        "(E3) Z_odd^3 = Z_odd on C^2",
        matrix_eq(Z_odd ** 3, Z_odd),
    )

    # Auxiliary intermediate identity: T_gamma^2 = diag(1, 0, 1)
    check(
        "(aux) T_gamma^2 = diag(1, 0, 1) on C^3",
        matrix_eq(T_gamma ** 2, diag(1, 0, 1)),
    )

    # =========================================================================
    section("Part 4: (DG4), (DG3), (DG2) determinant identities at exact symbolic (m, j)")
    # =========================================================================

    m_sym = Symbol("m", real=True, nonzero=True)
    j_sym = Symbol("j", real=True)

    det_S = sympy.simplify((m_sym * eye(4) + j_sym * S_cls).det())
    target_S = m_sym ** 2 * (m_sym ** 2 - j_sym ** 2)
    check(
        "(DG4) det(m I_4 + j S_cls) = m^2 (m^2 - j^2) = m^4 (1 - j^2/m^2)",
        sympy.simplify(det_S - target_S) == 0,
        detail=f"det = {det_S}",
    )

    det_T = sympy.simplify((m_sym * eye(3) + j_sym * T_gamma).det())
    target_T = m_sym * (m_sym ** 2 - j_sym ** 2)
    check(
        "(DG3) det(m I_3 + j T_gamma) = m (m^2 - j^2) = m^3 (1 - j^2/m^2)",
        sympy.simplify(det_T - target_T) == 0,
        detail=f"det = {det_T}",
    )

    det_Z = sympy.simplify((m_sym * eye(2) + j_sym * Z_odd).det())
    target_Z = m_sym ** 2 - j_sym ** 2
    check(
        "(DG2) det(m I_2 + j Z_odd) = m^2 - j^2 = m^2 (1 - j^2/m^2)",
        sympy.simplify(det_Z - target_Z) == 0,
        detail=f"det = {det_Z}",
    )

    # =========================================================================
    section("Part 5: (W) equal-baseline-subtracted triple-match response identity")
    # =========================================================================

    # ratio_S := det(m I_4 + j S_cls) / m^4
    # ratio_T := det(m I_3 + j T_gamma) / m^3
    # ratio_Z := det(m I_2 + j Z_odd) / m^2
    # All three should equal 1 - j^2/m^2.

    ratio_S = sympy.simplify(det_S / m_sym ** 4)
    ratio_T = sympy.simplify(det_T / m_sym ** 3)
    ratio_Z = sympy.simplify(det_Z / m_sym ** 2)
    target_ratio = 1 - j_sym ** 2 / m_sym ** 2
    check(
        "(W.symb) det(m I_4 + j S_cls)/m^4 = 1 - j^2/m^2 at exact symbolic (m, j)",
        sympy.simplify(ratio_S - target_ratio) == 0,
        detail=f"ratio_S = {ratio_S}",
    )
    check(
        "(W.symb) det(m I_3 + j T_gamma)/m^3 = 1 - j^2/m^2 at exact symbolic (m, j)",
        sympy.simplify(ratio_T - target_ratio) == 0,
        detail=f"ratio_T = {ratio_T}",
    )
    check(
        "(W.symb) det(m I_2 + j Z_odd)/m^2 = 1 - j^2/m^2 at exact symbolic (m, j)",
        sympy.simplify(ratio_Z - target_ratio) == 0,
        detail=f"ratio_Z = {ratio_Z}",
    )
    check(
        "(W.symb) triple baseline match: ratio_S = ratio_T = ratio_Z",
        sympy.simplify(ratio_S - ratio_T) == 0
        and sympy.simplify(ratio_T - ratio_Z) == 0,
        detail="all three ratios = 1 - j^2/m^2",
    )

    # Rational sanity at three (m, j) pairs (with |j| < m so the abs branch
    # is in the same regime for all three).

    rationals_mj = [
        (Rational(1), Rational(1, 5)),
        (Rational(2), Rational(3, 10)),
        (Rational(3), Rational(7, 10)),
    ]

    for m_val, j_val in rationals_mj:
        W_S = sympy.simplify(
            log(sympy.Abs(det_S.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 4))
        )
        W_T = sympy.simplify(
            log(sympy.Abs(det_T.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 3))
        )
        W_Z = sympy.simplify(
            log(sympy.Abs(det_Z.subs({m_sym: m_val, j_sym: j_val})))
            - log(sympy.Abs(m_val ** 2))
        )
        target_W = sympy.simplify(log(sympy.Abs(1 - j_val ** 2 / m_val ** 2)))
        check(
            f"(W) S_cls, T_gamma, Z_odd have identical response at (m,j) = ({m_val}, {j_val})",
            sympy.simplify(W_S - W_T) == 0
            and sympy.simplify(W_T - W_Z) == 0
            and sympy.simplify(W_S - target_W) == 0,
            detail=f"W_S = {W_S}, W_T = {W_T}, W_Z = {W_Z}, target = {target_W}",
        )

    # =========================================================================
    section("Part 6: (R1) small-source bosonic curvature ∂^2 W / ∂j^2 |_{j=0} = -2/m^2")
    # =========================================================================

    # On a scalar baseline D = m I, W = log(1 - j^2/m^2) (in the symbolic
    # branch where 1 - j^2/m^2 > 0). The leading bosonic curvature is
    # d^2 W / d j^2 |_{j=0} = -2/m^2 for all three generators.

    W_sym_S = log(ratio_S)  # since the ratio is positive in symbolic algebra
    W_sym_T = log(ratio_T)
    W_sym_Z = log(ratio_Z)

    curv_S = sympy.simplify(diff(W_sym_S, j_sym, 2).subs({j_sym: 0}))
    curv_T = sympy.simplify(diff(W_sym_T, j_sym, 2).subs({j_sym: 0}))
    curv_Z = sympy.simplify(diff(W_sym_Z, j_sym, 2).subs({j_sym: 0}))
    target_curv = -2 / m_sym ** 2

    check(
        "(R1) ∂^2 W / ∂j^2 |_{j=0} = -2/m^2 for S_cls on scalar baseline",
        sympy.simplify(curv_S - target_curv) == 0,
        detail=f"curv_S = {curv_S}",
    )
    check(
        "(R1) ∂^2 W / ∂j^2 |_{j=0} = -2/m^2 for T_gamma on scalar baseline",
        sympy.simplify(curv_T - target_curv) == 0,
        detail=f"curv_T = {curv_T}",
    )
    check(
        "(R1) ∂^2 W / ∂j^2 |_{j=0} = -2/m^2 for Z_odd on scalar baseline",
        sympy.simplify(curv_Z - target_curv) == 0,
        detail=f"curv_Z = {curv_Z}",
    )
    check(
        "(R1) curvatures match across the three odd generators on m I baseline",
        sympy.simplify(curv_S - curv_T) == 0
        and sympy.simplify(curv_T - curv_Z) == 0,
        detail="all three curvatures = -2/m^2",
    )

    # =========================================================================
    section("Part 7: counterfactual — non-scalar baseline breaks (W)")
    # =========================================================================

    # Take m_1 = 2, m_2 = 3, m_3 = 5, m_4 = 7 on C^4; m_1, m_2, m_3 on C^3;
    # m_1, m_2 on C^2.
    # The baseline-subtracted response should differ across the three.

    m1, m2, m3, m4 = Rational(2), Rational(3), Rational(5), Rational(7)
    j_cf = Rational(1, 4)
    D4 = diag(m1, m2, m3, m4)
    D3 = diag(m1, m2, m3)
    D2 = diag(m1, m2)

    det_S_cf = sympy.simplify((D4 + j_cf * S_cls).det())
    det_T_cf = sympy.simplify((D3 + j_cf * T_gamma).det())
    det_Z_cf = sympy.simplify((D2 + j_cf * Z_odd).det())

    W_S_cf = sympy.simplify(log(sympy.Abs(det_S_cf)) - log(sympy.Abs(D4.det())))
    W_T_cf = sympy.simplify(log(sympy.Abs(det_T_cf)) - log(sympy.Abs(D3.det())))
    W_Z_cf = sympy.simplify(log(sympy.Abs(det_Z_cf)) - log(sympy.Abs(D2.det())))

    diff_ST = sympy.simplify(W_S_cf - W_T_cf)
    diff_TZ = sympy.simplify(W_T_cf - W_Z_cf)

    check(
        "(cf) non-scalar baseline diag(2,3,5,7) vs diag(2,3,5) breaks (W) for S_cls vs T_gamma",
        diff_ST != 0,
        detail=f"W_S = {W_S_cf}, W_T = {W_T_cf}, diff = {diff_ST}",
    )
    check(
        "(cf) non-scalar baseline diag(2,3,5) vs diag(2,3) breaks (W) for T_gamma vs Z_odd",
        diff_TZ != 0,
        detail=f"W_T = {W_T_cf}, W_Z = {W_Z_cf}, diff = {diff_TZ}",
    )

    # =========================================================================
    section("Summary")
    # =========================================================================
    print("  Verified at exact sympy precision on C^4, C^3, and C^2:")
    print("    (Herm)  S_cls, T_gamma, Z_odd all Hermitian")
    print("    (Trace) Tr S_cls = Tr T_gamma = Tr Z_odd = 0")
    print("    (S1)    spec(S_cls)   = {+1, -1, 0, 0}")
    print("    (S2)    spec(T_gamma) = {+1, -1, 0}")
    print("    (S3)    spec(Z_odd)   = {+1, -1}")
    print("    (C1)    char poly S_cls   = λ^4 - λ^2")
    print("    (C2)    char poly T_gamma = -λ^3 + λ")
    print("    (C3)    char poly Z_odd   = λ^2 - 1")
    print("    (E1)    S_cls^3   = S_cls   (cubic involution)")
    print("    (E2)    T_gamma^3 = T_gamma (cubic involution)")
    print("    (E3)    Z_odd^3   = Z_odd   (cubic involution)")
    print("    (DG4)   det(m I_4 + j S_cls)   = m^2 (m^2 - j^2)")
    print("    (DG3)   det(m I_3 + j T_gamma) = m (m^2 - j^2)")
    print("    (DG2)   det(m I_2 + j Z_odd)   = m^2 - j^2")
    print("    (W)     Triple baseline match: log|...| - log|m^n| = log|1 - j^2/m^2|")
    print("    (R1)    Small-source curvature ∂^2 W / ∂j^2 |_{j=0} = -2/m^2 (all 3)")
    print("    Counterfactual: non-scalar baseline diag(2,3,5,7)/diag(2,3,5)/diag(2,3) breaks (W)")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
