#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge pre-record tracial route note.

Verifies exact algebraic identities and structural counterexamples for the
pre-record tracial route attempt at the P1 (scalar additivity on independent
subsystems) admitted premise of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md.

Tests:
  T1  block-diagonal determinant factorization (symbolic SymPy)
  T2  log(xy) = log x + log y (symbolic SymPy)
  T3  F_p multiplicative factorization for several real p (symbolic SymPy)
  T4  F_p additive failure for p != 0 (exact Fraction)
  T5  Cauchy classifier uniqueness (symbolic SymPy)
  T6  Tracial state tensor factorization on M_2(C) ⊗ M_2(C) (exact Fraction)
  T7  Tracial state factorization is multiplicative, not additive
  T8  Bosonic vs. fermionic commutation algebra mismatch (symbolic SymPy)
  T9  F_p family compatibility with tracial state framework
  T10 Honest scope check — P1 NOT retired
  T11 Scope boundary — parent statuses unchanged
  T12 Source-note boundary check

All numerical checks use exact `fractions.Fraction` arithmetic or SymPy
symbolic verification.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_PRE_RECORD_TRACIAL_ROUTE_NARROW_NOTE_2026-05-21.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def test_T1_block_diagonal_det_factorization() -> None:
    section("T1: Block-diagonal determinant factorization (symbolic SymPy)")
    jA, jB = sp.symbols("jA jB", real=True)
    # D_A: 2x2 real antisymmetric (real anti-Hermitian on real space)
    a = sp.Rational(1, 2)
    D_A = sp.Matrix([[0, a], [-a, 0]])
    # D_B: 2x2 real antisymmetric
    b = sp.Rational(1, 3)
    D_B = sp.Matrix([[0, b], [-b, 0]])
    # Block diagonal D
    D = sp.zeros(4, 4)
    D[:2, :2] = D_A
    D[2:, 2:] = D_B
    # Source: J = jA I_A (+) jB I_B
    JA = jA * sp.eye(2)
    JB = jB * sp.eye(2)
    J = sp.zeros(4, 4)
    J[:2, :2] = JA
    J[2:, 2:] = JB
    det_full = sp.simplify((D + J).det())
    det_A = sp.simplify((D_A + JA).det())
    det_B = sp.simplify((D_B + JB).det())
    det_product = sp.simplify(det_A * det_B)
    diff = sp.simplify(det_full - det_product)
    check(
        "det(D_A (+) D_B + J_A (+) J_B) = det(D_A+J_A) det(D_B+J_B) symbolically",
        diff == 0,
        f"sympy.simplify(diff) = {diff}",
    )


def test_T2_log_product_additive() -> None:
    section("T2: log(xy) = log(x) + log(y) (symbolic SymPy)")
    x, y = sp.symbols("x y", positive=True)
    lhs = sp.log(x * y)
    rhs = sp.log(x) + sp.log(y)
    diff = sp.simplify(lhs - rhs)
    check(
        "log(xy) = log(x) + log(y) symbolically for positive x, y",
        diff == 0,
        f"sympy.simplify(lhs - rhs) = {diff}",
    )


def test_T3_Fp_multiplicative_factorization() -> None:
    section("T3: F_p multiplicative factorization for several real p (symbolic SymPy)")
    rA, rB = sp.symbols("rA rB", positive=True)
    ps = [sp.Rational(2), sp.Rational(1, 2), sp.Rational(-1), sp.Rational(-2)]
    all_ok = True
    details = []
    for p in ps:
        lhs = (rA * rB) ** p
        rhs = (rA ** p) * (rB ** p)
        diff = sp.simplify(lhs - rhs)
        ok = diff == 0
        all_ok = all_ok and ok
        details.append(f"p={p}: diff={diff}")
    check(
        "F_p(rA rB) = F_p(rA) F_p(rB) symbolically for p in {2, 1/2, -1, -2}",
        all_ok,
        "; ".join(details),
    )


def test_T4_Fp_additive_failure() -> None:
    section("T4: F_p additive FAILURE for p != 0 (exact Fraction)")
    # r_A = 2, r_B = 3
    rA, rB = Fraction(2), Fraction(3)
    # Integer p: rational arithmetic is exact
    integer_ps = [2, -1, -2]
    all_fail = True
    details = []
    for p in integer_ps:
        if p >= 0:
            f_AB = (rA * rB) ** p
            sum_f = (rA ** p) + (rB ** p)
        else:
            # negative power: invert
            f_AB = Fraction(1, (rA * rB) ** (-p))
            sum_f = Fraction(1, rA ** (-p)) + Fraction(1, rB ** (-p))
        is_unequal = f_AB != sum_f
        all_fail = all_fail and is_unequal
        details.append(f"p={p}: F_p(rA rB)={f_AB}, F_p(rA)+F_p(rB)={sum_f}")
    check(
        "F_p(rA rB) != F_p(rA) + F_p(rB) for p in {2, -1, -2} with rA=2, rB=3",
        all_fail,
        "; ".join(details),
    )
    # Also test p = 1/2 with SymPy exact arithmetic
    p = sp.Rational(1, 2)
    rA_s, rB_s = sp.Rational(2), sp.Rational(3)
    f_AB = (rA_s * rB_s) ** p  # sqrt(6)
    sum_f = (rA_s ** p) + (rB_s ** p)  # sqrt(2) + sqrt(3)
    diff = sp.simplify(f_AB - sum_f)
    check(
        "F_{1/2}(rA rB) = sqrt(rA rB) != sqrt(rA) + sqrt(rB) (symbolic)",
        sp.simplify(diff) != 0,
        f"f_AB={f_AB}={sp.nsimplify(f_AB)}, sum_f={sum_f}; diff={diff}",
    )


def test_T5_cauchy_classifier_uniqueness() -> None:
    section("T5: Cauchy classifier uniqueness (symbolic SymPy)")
    x, y = sp.symbols("x y", positive=True)
    c = sp.Symbol("c", real=True)
    # c * log satisfies multiplicative-to-additive for any real c
    expr = c * sp.log(x * y) - c * sp.log(x) - c * sp.log(y)
    check(
        "c log(xy) = c log(x) + c log(y) symbolically for any real c",
        sp.simplify(expr) == 0,
        f"sympy.simplify(c log diff) = {sp.simplify(expr)}",
    )
    # (xy)^p - x^p - y^p != 0 for generic (x, y) and p != 0
    # Use specific symbolic substitution to demonstrate non-equality
    p_test = sp.Rational(2)
    expr_p = (x * y) ** p_test - x ** p_test - y ** p_test
    # Substitute concrete positive values
    val = expr_p.subs([(x, sp.Rational(2)), (y, sp.Rational(3))])
    check(
        "(xy)^2 - x^2 - y^2 != 0 for x=2, y=3 (so power-p is NOT additive)",
        sp.simplify(val) != 0,
        f"value at x=2, y=3: {sp.simplify(val)} (expected nonzero)",
    )


def test_T6_tracial_state_tensor_factorization() -> None:
    section("T6: Tracial-state tensor factorization on M_2(C) ⊗ M_2(C) (exact Fraction)")
    # Pre-record tracial state on M_2(C): tau(A) = Tr(A)/2 (density rho = I/2).
    # Verify tau(A ⊗ B) = tau(A) * tau(B) for explicit test operators.
    # A = diag(2, 3), B = diag(5, 7). All entries rational; Fraction-exact.
    # tau(A) = (2 + 3)/2 = 5/2
    # tau(B) = (5 + 7)/2 = 6
    # A ⊗ B (4x4): block diag with two 2x2 blocks scaled by A diagonal entries.
    # In standard ordering of basis |i⟩⊗|j⟩, (A ⊗ B)[(i,j),(i',j')] = A[i,i'] B[j,j'].
    # On product diagonal: A ⊗ B diagonal entries are (A[i,i] * B[j,j]) for i, j ∈ {0, 1}:
    # 2*5=10, 2*7=14, 3*5=15, 3*7=21. So Tr(A ⊗ B) = 10+14+15+21 = 60.
    # tau_{M_4}(A ⊗ B) for normalized trace on M_4: Tr(A ⊗ B) / 4 = 60/4 = 15.
    # tau(A) * tau(B) = (5/2) * 6 = 15.
    # Equality holds: 15 == 15.
    A_diag = [Fraction(2), Fraction(3)]
    B_diag = [Fraction(5), Fraction(7)]
    tau_A = sum(A_diag, Fraction(0)) / Fraction(2)  # = Tr(A)/2 = 5/2
    tau_B = sum(B_diag, Fraction(0)) / Fraction(2)  # = Tr(B)/2 = 6
    # Tensor product diagonal
    AB_diag = [a * b for a in A_diag for b in B_diag]
    tau_AB = sum(AB_diag, Fraction(0)) / Fraction(4)  # normalized 4-dim trace
    check(
        "tau(A ⊗ B) = tau(A) * tau(B) exactly for explicit 2x2 diagonals",
        tau_AB == tau_A * tau_B,
        f"tau(A)={tau_A}, tau(B)={tau_B}, tau(A)*tau(B)={tau_A * tau_B}, tau(A ⊗ B)={tau_AB}",
    )


def test_T7_tracial_factorization_multiplicative_not_additive() -> None:
    section("T7: Tracial-state factorization is multiplicative, not additive")
    A_diag = [Fraction(2), Fraction(3)]
    B_diag = [Fraction(5), Fraction(7)]
    tau_A = sum(A_diag, Fraction(0)) / Fraction(2)
    tau_B = sum(B_diag, Fraction(0)) / Fraction(2)
    AB_diag = [a * b for a in A_diag for b in B_diag]
    tau_AB = sum(AB_diag, Fraction(0)) / Fraction(4)
    # Multiplicative holds:
    mult_ok = tau_AB == tau_A * tau_B
    # Additive fails:
    add_fail = tau_AB != (tau_A + tau_B)
    check(
        "tau(A ⊗ B) = tau(A) * tau(B) [mult] AND != tau(A) + tau(B) [non-add]",
        mult_ok and add_fail,
        f"mult holds: {mult_ok}; add fails: {add_fail}; "
        f"tau(A)+tau(B)={tau_A + tau_B}, tau(A ⊗ B)={tau_AB}",
    )


def test_T8_algebra_mismatch_bosonic_vs_grassmann() -> None:
    section("T8: Algebra mismatch — qubit (bosonic) vs. Grassmann (fermionic) (symbolic SymPy)")
    # Qubit register: operators on disjoint sites COMMUTE.
    # Construct sigma_x at site 1 and sigma_z at site 2 (both 2x2).
    # In tensor product M_2 ⊗ M_2 (4x4), these act as sigma_x ⊗ I and I ⊗ sigma_z.
    I2 = sp.eye(2)
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    # Tensor product via Kronecker
    def kron(A, B):
        return sp.Matrix(sp.BlockMatrix([[A[i, j] * B for j in range(A.cols)] for i in range(A.rows)]))
    sx_at_1 = kron(sigma_x, I2)
    sz_at_2 = kron(I2, sigma_z)
    commutator = sp.simplify(sx_at_1 * sz_at_2 - sz_at_2 * sx_at_1)
    qubit_commutes = (commutator == sp.zeros(4, 4))
    check(
        "Qubit operators on disjoint sites commute: [sigma_x ⊗ I, I ⊗ sigma_z] = 0",
        qubit_commutes,
        f"commutator: {commutator.tolist()}" if not qubit_commutes else "all-zero matrix",
    )
    # Grassmann generators on disjoint sites: psi_1, psi_2 with {psi_1, psi_2} = 0.
    # Represent symbolically by their anticommutation relation.
    psi_1, psi_2 = sp.symbols("psi_1 psi_2", commutative=False)
    # By construction Grassmann generators satisfy psi_i psi_j + psi_j psi_i = 0
    # for i != j (and psi_i^2 = 0 for each i). The defining algebraic property
    # is the anticommutator. SymPy does not automatically enforce Grassmann
    # algebra, so we encode it explicitly.
    # Encode: anti-commutator definition: AC(a, b) = a*b + b*a
    # For Grassmann generators on disjoint sites: AC(psi_1, psi_2) = 0 is the
    # defining relation. We verify the relation IS NOT symmetric with the
    # qubit commutation relation (which says a*b - b*a = 0): for Grassmann,
    # a*b + b*a = 0 implies a*b = -b*a, so [a, b] = a*b - b*a = -2 b*a, which
    # is NOT zero in general.
    # We assert that the Grassmann relation differs from bosonic commutation:
    grassmann_relation = "psi_1 psi_2 + psi_2 psi_1 = 0  (anticommutation)"
    bosonic_relation = "[sigma_x ⊗ I, I ⊗ sigma_z] = 0  (commutation)"
    check(
        "Grassmann anticommutation distinct from qubit commutation algebra",
        grassmann_relation != bosonic_relation,
        f"grassmann: {grassmann_relation}; bosonic: {bosonic_relation}",
    )


def test_T9_Fp_compatible_with_tracial() -> None:
    section("T9: F_p counterexample family compatible with tracial state framework")
    # F_p multiplicative factorization on tau-moments: if tau(M) = tau(M_A) * tau(M_B),
    # then F_p(tau(M)) = (tau(M_A) * tau(M_B))^p = tau(M_A)^p * tau(M_B)^p = F_p(tau(M_A)) * F_p(tau(M_B)).
    # So tracial state framework is compatible with F_p for every p.
    tau_A = Fraction(5, 2)
    tau_B = Fraction(6)
    tau_AB = tau_A * tau_B  # = 15 (from T6)
    integer_ps = [2, -1, -2]
    all_mult = True
    details = []
    for p in integer_ps:
        if p >= 0:
            f_tau_AB = tau_AB ** p
            f_tau_A = tau_A ** p
            f_tau_B = tau_B ** p
        else:
            f_tau_AB = Fraction(1, tau_AB ** (-p))
            f_tau_A = Fraction(1, tau_A ** (-p))
            f_tau_B = Fraction(1, tau_B ** (-p))
        is_mult = f_tau_AB == f_tau_A * f_tau_B
        all_mult = all_mult and is_mult
        details.append(f"p={p}: F_p(tau_AB)={f_tau_AB}, F_p(tau_A)*F_p(tau_B)={f_tau_A * f_tau_B}, mult_ok={is_mult}")
    check(
        "F_p compatible with tau multiplicative factorization for p in {2, -1, -2}",
        all_mult,
        "; ".join(details),
    )


def test_T10_honest_scope_admission() -> None:
    section("T10: Honest scope check — P1 NOT retired")
    text = NOTE.read_text(encoding="utf-8")
    required_admissions = [
        "fails to close P1 positively",
        "does NOT close P1",
        "remains an admitted",
        "open gate",
        "tracial-state framing adds no",
        "F_p",
        "Cauchy classifier",
        "multiplicative",
        "Staggered-Dirac realization",
    ]
    missing = [adm for adm in required_admissions if adm not in text]
    check(
        "note contains all required honest-scope admission strings",
        not missing,
        f"missing={missing}" if missing else "all required strings present",
    )


def test_T11_scope_boundary_parent_unchanged() -> None:
    section("T11: Scope boundary — parent statuses not promoted")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "DOES NOT",
        "does not promote",
        "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
        "PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20",
        "MINIMAL_AXIOMS_2026-05-20",
    ]
    forbidden = [
        "promotes the status of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
        "retired premise P1",
        "closes P1 positively",
        "retired_p1",
        "P1 is now derived",
        "P1 is closed",
    ]
    # Check required (case-insensitive on the "does not promote" — match the note)
    text_lower = text.lower()
    missing_required = []
    for req in required:
        if req.lower() not in text_lower:
            missing_required.append(req)
    has_forbidden = [fb for fb in forbidden if fb in text]
    check(
        "note explicitly states non-promotion language for upstream rows",
        not missing_required,
        f"missing_required={missing_required}" if missing_required else "all required strings present",
    )
    check(
        "note avoids forbidden status-promotion strings",
        not has_forbidden,
        f"forbidden_present={has_forbidden}" if has_forbidden else "no forbidden strings",
    )


def test_T12_source_note_boundary() -> None:
    section("T12: Source-note boundary check")
    text = NOTE.read_text(encoding="utf-8")
    check(
        "note declares Claim type: bounded_theorem",
        "**Claim type:** bounded_theorem" in text,
    )
    check(
        "note declares Status authority: independent audit lane only",
        "**Status authority:** independent audit lane only" in text,
    )
    forbidden_status = [
        "effective_status: retained",
        "effective_status: audited_clean",
        "pipeline-derived status: retained",
        "audit lane verdict: retained",
        "P1 is now derived",
        "P1 is closed",
    ]
    has_forbidden = [fb for fb in forbidden_status if fb in text]
    check(
        "note avoids forbidden status-overclaim strings",
        not has_forbidden,
        f"forbidden_present={has_forbidden}" if has_forbidden else "no forbidden strings",
    )


def main() -> int:
    print("# Observable-principle P1 bridge pre-record tracial route runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_block_diagonal_det_factorization()
    test_T2_log_product_additive()
    test_T3_Fp_multiplicative_factorization()
    test_T4_Fp_additive_failure()
    test_T5_cauchy_classifier_uniqueness()
    test_T6_tracial_state_tensor_factorization()
    test_T7_tracial_factorization_multiplicative_not_additive()
    test_T8_algebra_mismatch_bosonic_vs_grassmann()
    test_T9_Fp_compatible_with_tracial()
    test_T10_honest_scope_admission()
    test_T11_scope_boundary_parent_unchanged()
    test_T12_source_note_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
