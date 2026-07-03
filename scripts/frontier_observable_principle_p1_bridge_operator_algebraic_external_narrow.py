#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge operator-algebraic
external bounded note.

This runner verifies the operator-algebraic primitives (Hilbert tensor
product factorization, Grassmann determinant block factorization,
trace-state factorization on tensor product) at exact ``Fraction`` /
``sympy`` precision, plus exhibits the explicit ``F_p = r^p`` counter-
example family witnessing that operator-algebraic factorization is
compatible with non-additive scalar functionals on ``|Z|``. Plus a live-
ledger check that the cluster-decomposition and Reeh-Schlieder rows are
not currently retained-grade primitives for closing P1, while the mass-gap
bridge is retained-grade but supplies only temporal-decay context.

All numerical checks use exact ``fractions.Fraction`` arithmetic or
SymPy symbolic verification.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_OPERATOR_ALGEBRAIC_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md"
)
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

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


# ----------------------------------------------------------------------
# T1: Hilbert tensor product factorization on independent subsystems
# ----------------------------------------------------------------------


def test_T1_hilbert_tensor_product_dim() -> None:
    section("T1: Hilbert tensor product dim factorization on independent subsystems")
    # On a per-site Cl(3) Fock module of dim 2, with |Lambda_A| = m_A sites
    # and |Lambda_B| = m_B sites, dim(H_A) = 2^m_A and dim(H_B) = 2^m_B.
    # Independent subsystem factorization gives
    # dim(H_A (x) H_B) = dim(H_A) * dim(H_B) = 2^(m_A + m_B) = dim(H_{A u B}).
    ok = True
    cases = []
    for m_A, m_B in [(1, 1), (1, 2), (2, 2), (1, 3), (2, 3), (3, 3)]:
        dim_A = 2**m_A
        dim_B = 2**m_B
        dim_AuB = 2 ** (m_A + m_B)
        if dim_A * dim_B != dim_AuB:
            ok = False
        cases.append((m_A, m_B, dim_A * dim_B, dim_AuB))
    check(
        "dim(H_A) * dim(H_B) = dim(H_{AuB}) on per-site Cl(3) Fock with dim_C V = 2",
        ok,
        f"cases={cases}",
    )


# ----------------------------------------------------------------------
# T2: Grassmann determinant block factorization (O2/P1)
# ----------------------------------------------------------------------


def test_T2_grassmann_determinant_factorization() -> None:
    section("T2: Grassmann determinant block factorization (O2/P1) — symbolic")
    # Take symbolic D_A and D_B as 2x2 real anti-Hermitian (anti-symmetric on
    # real entries) plus symbolic real symmetric J_A and J_B. Block diagonal
    # D = D_A (+) D_B; J = J_A (+) J_B.
    a, b, jaa, jab, jbb = sp.symbols("a b jaa jab jbb", real=True)
    c, d, kcc, kcd, kdd = sp.symbols("c d kcc kcd kdd", real=True)
    # D_A real anti-symmetric:
    D_A = sp.Matrix([[0, a], [-a, 0]])
    # D_B real anti-symmetric:
    D_B = sp.Matrix([[0, c], [-c, 0]])
    # J_A real symmetric:
    J_A = sp.Matrix([[jaa, jab], [jab, jbb]])
    # J_B real symmetric:
    J_B = sp.Matrix([[kcc, kcd], [kcd, kdd]])
    # Block diagonal D and J:
    D = sp.diag(D_A, D_B)
    J = sp.diag(J_A, J_B)
    lhs = sp.expand((D + J).det())
    rhs = sp.expand((D_A + J_A).det() * (D_B + J_B).det())
    diff = sp.simplify(lhs - rhs)
    check(
        "det(D_A (+) D_B + J_A (+) J_B) = det(D_A+J_A) det(D_B+J_B) symbolically",
        diff == 0,
        f"sympy.simplify(lhs - rhs) = {diff}",
    )
    # Sanity: numerical instance with rational entries
    subs = {a: Fraction(2, 3), c: Fraction(1, 5), jaa: Fraction(1, 2),
            jab: Fraction(1, 7), jbb: Fraction(1, 3), kcc: Fraction(2, 11),
            kcd: Fraction(1, 9), kdd: Fraction(3, 5)}
    lhs_n = sp.Rational(lhs.subs(subs))
    rhs_n = sp.Rational(rhs.subs(subs))
    check(
        "Numerical rational instance: det factorization holds",
        lhs_n == rhs_n,
        f"lhs={lhs_n}, rhs={rhs_n}",
    )


# ----------------------------------------------------------------------
# T3: Trace-state factorization on finite-dim matrix tensor product (O3)
# ----------------------------------------------------------------------


def test_T3_trace_state_tensor_product() -> None:
    section("T3: Trace-state factorization Tr(A (x) B) = Tr(A) Tr(B)")
    # Take small rational matrices A and B and verify Tr(A (x) B) = Tr(A) Tr(B).
    # This is the finite-dim incarnation of the type II_1 trace-state
    # multiplicative factorization (O3).
    cases = [
        (sp.Matrix([[Fraction(1, 2), Fraction(2, 3)], [Fraction(3, 4), Fraction(5, 6)]]),
         sp.Matrix([[Fraction(1, 5), Fraction(2, 7)], [Fraction(3, 8), Fraction(1, 9)]])),
        (sp.Matrix([[Fraction(7, 3), -Fraction(1, 2)], [Fraction(11, 8), Fraction(2, 3)]]),
         sp.Matrix([[-Fraction(5, 4), Fraction(2, 9)], [Fraction(3, 7), Fraction(13, 6)]])),
    ]
    ok = True
    details = []
    for A, B in cases:
        tr_A = sum(A[i, i] for i in range(A.shape[0]))
        tr_B = sum(B[i, i] for i in range(B.shape[0]))
        kron = sp.tensorproduct(A, B)  # 4-index tensor; we'll compute trace via Kronecker
        # Build the Kronecker product as a 4x4 matrix:
        n, m = A.shape[0], B.shape[0]
        K = sp.zeros(n * m, n * m)
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    for l in range(m):
                        K[i * m + k, j * m + l] = A[i, j] * B[k, l]
        tr_kron = sum(K[r, r] for r in range(n * m))
        lhs = sp.Rational(tr_kron)
        rhs = sp.Rational(tr_A * tr_B)
        details.append((lhs, rhs))
        if lhs != rhs:
            ok = False
    check("Tr(A (x) B) = Tr(A) Tr(B) on rational test pairs", ok, f"cases={details}")


# ----------------------------------------------------------------------
# T4: Sub-route (a)/(b)/(c) discrimination
# ----------------------------------------------------------------------


def test_T4_sub_route_discrimination() -> None:
    section("T4: Sub-route (a)/(b)/(c) — multiplicative does not imply additive")
    # All three sub-routes (a) GNS / Reeh-Schlieder, (b) cluster decomposition,
    # (c) operator-algebraic trace, deliver multiplicative factorization on
    # r(J) := |det(D+J)| / |det D|. The step to additive W = log r is the
    # additivity admissibility criterion. Demonstrate this gap explicitly.
    r_A, r_B = sp.symbols("r_A r_B", positive=True)
    mult = sp.simplify(r_A * r_B - r_A * r_B)
    add_log = sp.simplify(sp.log(r_A * r_B) - sp.log(r_A) - sp.log(r_B))
    add_r = sp.simplify((r_A * r_B) - (r_A + r_B))
    check(
        "Multiplicative on r holds identically",
        mult == 0,
        "(r_A * r_B) - (r_A * r_B) = 0",
    )
    check(
        "log r is additive: log(r_A r_B) - log r_A - log r_B = 0",
        add_log == 0,
        "Cauchy classifier on the additive class",
    )
    check(
        "r itself is NOT additive: r_A r_B - r_A - r_B != 0 generically",
        add_r != 0,
        f"sympy.simplify(r_A r_B - r_A - r_B) = {add_r} (nonzero for r_A != 1 or r_B != 1)",
    )
    # Numerical witness: r_A = 2, r_B = 3 -> r_A r_B = 6, r_A + r_B = 5, diff = 1
    diff_val = sp.Rational(add_r.subs({r_A: 2, r_B: 3}))
    check(
        "Numerical witness: r_A=2, r_B=3 -> r_A r_B - r_A - r_B = 1",
        diff_val == 1,
        f"diff={diff_val}",
    )


# ----------------------------------------------------------------------
# T5: (C5) counterexample family - F_p = r^p
# ----------------------------------------------------------------------


def test_T5_counterexample_family_F_p() -> None:
    section("T5: (C5) counterexample family F_p = r^p — multiplicative yes, additive no")
    # For F_p[J] := r(J)^p, multiplicative factorization (M5) holds for ANY p,
    # but additivity fails for p != 0.
    test_ps = [Fraction(-2), Fraction(-1), Fraction(1, 2), Fraction(1), Fraction(2),
               Fraction(3)]
    r_A_val = Fraction(2)
    r_B_val = Fraction(3)
    ok_mult_all = True
    ok_add_failure_all = True
    details = []
    for p in test_ps:
        # F_p[J_A (+) J_B] = (r_A * r_B)^p
        # F_p[J_A] * F_p[J_B] = r_A^p * r_B^p
        # These are equal for any p.
        # Use sympy for r^p to handle rational p exactly:
        p_sym = sp.Rational(p)
        r_A_s = sp.Rational(r_A_val)
        r_B_s = sp.Rational(r_B_val)
        F_total = (r_A_s * r_B_s) ** p_sym
        F_prod = (r_A_s**p_sym) * (r_B_s**p_sym)
        diff_mult = sp.simplify(F_total - F_prod)
        if diff_mult != 0:
            ok_mult_all = False
        # Additivity check: F_p[J_A (+) J_B] vs F_p[J_A] + F_p[J_B]
        F_sum = (r_A_s**p_sym) + (r_B_s**p_sym)
        diff_add = sp.simplify(F_total - F_sum)
        # For p != 0, expect diff_add != 0:
        if p != 0 and diff_add == 0:
            ok_add_failure_all = False
        details.append((float(p), str(diff_mult), str(diff_add)))
    check(
        "F_p multiplicative factorization holds for all test p (M5)",
        ok_mult_all,
        f"cases (p, mult_diff, add_diff): {details}",
    )
    check(
        "F_p additivity fails on the explicit witness (r_A=2, r_B=3) for tested p != 0 (P3) - existential non-additivity",
        ok_add_failure_all,
        "F_p[J_A (+) J_B] != F_p[J_A] + F_p[J_B] verified on the off-coincidence-curve witness (r_A=2, r_B=3) for the tested p != 0 values; suffices for the existential non-additivity conclusion. The universal 'for all r_A, r_B' version is not checked and is not claimed (the coincidence curve r_A^p r_B^p = r_A^p + r_B^p contains nontrivial points such as r_A^p = r_B^p = 2)",
    )


# ----------------------------------------------------------------------
# T6: Cluster decomposition retained-status check on live ledger
# ----------------------------------------------------------------------


def test_T6_cluster_decomposition_ledger_status() -> None:
    section("T6: Cluster decomposition retained-status check (live ledger)")
    if not LEDGER.exists():
        check("Audit ledger present", False, f"missing: {LEDGER}")
        return
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = data.get("rows", data)
    cid_cluster = "axiom_first_cluster_decomposition_theorem_note_2026-04-29"
    cid_reeh = "axiom_first_reeh_schlieder_theorem_note_2026-05-01"
    cid_bridge = "cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09"
    status_cluster = rows.get(cid_cluster, {}).get("effective_status", "?")
    status_reeh = rows.get(cid_reeh, {}).get("effective_status", "?")
    status_bridge = rows.get(cid_bridge, {}).get("effective_status", "?")
    positive_closure_grade = {"retained"}
    retained_or_bounded_grade = {"retained", "retained_bounded", "retained_no_go"}
    # The operator-algebraic attempt cannot consume cluster decomposition as a
    # positive retained primitive for closing P1 under the live ledger. A
    # bounded/conditional context row is expected and is part of the boundary.
    check(
        f"Cluster decomposition row is not positive-closure retained",
        status_cluster not in positive_closure_grade,
        f"{cid_cluster}.effective_status = {status_cluster}",
    )
    # Reeh-Schlieder is also not consumable as a retained primitive.
    check(
        f"Reeh-Schlieder row is not retained-grade",
        status_reeh not in retained_or_bounded_grade,
        f"{cid_reeh}.effective_status = {status_reeh}",
    )
    # The mass-gap bridge is retained-grade, but provides temporal decay,
    # not the additivity-of-generator step.
    check(
        f"Mass-gap bridge row is retained-grade (conditional temporal bridge only)",
        status_bridge in retained_or_bounded_grade,
        f"{cid_bridge}.effective_status = {status_bridge}",
    )


# ----------------------------------------------------------------------
# T7: Alternative scalar functionals r^p — only p -> 0 (log) is additive
# ----------------------------------------------------------------------


def test_T7_alternative_scalar_functionals() -> None:
    section("T7: Alternative scalar functionals r^p — only log representative additive")
    # Numerically scan p in {1/4, 1/2, 1, 2, 4}, check additivity defect is
    # bounded away from zero for each p != 0.
    test_ps = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)]
    r_A_val = sp.Rational(Fraction(7, 3))
    r_B_val = sp.Rational(Fraction(11, 5))
    threshold = sp.Rational(1, 1000)  # additivity defect >> 0
    ok_all = True
    defects = []
    for p in test_ps:
        p_s = sp.Rational(p)
        F_total = (r_A_val * r_B_val) ** p_s
        F_sum = r_A_val**p_s + r_B_val**p_s
        defect = sp.simplify(sp.Abs(F_total - F_sum))
        # Evaluate as a float to compare magnitude:
        defect_num = float(defect)
        defects.append((float(p), defect_num))
        if defect_num < float(threshold):
            ok_all = False
    check(
        "F_p additivity defect > 1e-3 for each p in {1/4, 1/2, 1, 2, 4}",
        ok_all,
        f"(p, |F_p[A (+) B] - F_p[A] - F_p[B]|): {defects}",
    )
    # Confirm that log r (the p -> 0 limit) IS additive:
    log_defect = sp.simplify(sp.log(r_A_val * r_B_val) - sp.log(r_A_val) - sp.log(r_B_val))
    check(
        "log r is additive (p -> 0 limit): log(r_A r_B) - log r_A - log r_B = 0",
        log_defect == 0,
        f"sympy.simplify(log_defect) = {log_defect}",
    )


# ----------------------------------------------------------------------
# T8: Numerical toy on independent staggered blocks
# ----------------------------------------------------------------------


def test_T8_numerical_toy_staggered_blocks() -> None:
    section("T8: Numerical toy on independent 2x2 + 2x2 staggered blocks")
    # Block A: D_A real anti-symmetric 2x2 with entry a = 2 (rational).
    # Block B: D_B real anti-symmetric 2x2 with entry c = 3 (rational).
    a = Fraction(2)
    c = Fraction(3)
    # Source: J = (j_A, j_B), small rational shifts.
    jA = Fraction(1, 2)
    jB = Fraction(1, 5)
    # det(D_A + j_A I): det([[j_A, a],[-a, j_A]]) = j_A^2 + a^2
    detA0 = a**2
    detAj = jA**2 + a**2
    detB0 = c**2
    detBj = jB**2 + c**2
    # r_A = |det(D_A + j_A)| / |det D_A|
    r_A_val = Fraction(detAj, detA0)
    r_B_val = Fraction(detBj, detB0)
    # Multiplicative on r:
    r_total = r_A_val * r_B_val
    detTotal0 = detA0 * detB0
    detTotalJ = detAj * detBj
    r_total_check = Fraction(detTotalJ, detTotal0)
    check(
        "Direct det factorization matches r product on independent 2x2 blocks",
        r_total == r_total_check,
        f"r_A * r_B = {r_total}, det_ratio = {r_total_check}",
    )
    # For p in {1, 2, 1/2}, multiplicative holds; only p = 0 (log) is additive.
    test_ps = [Fraction(1), Fraction(2), Fraction(1, 2)]
    ok_mult = True
    mult_details = []
    for p in test_ps:
        p_s = sp.Rational(p)
        F_total = (sp.Rational(r_total)) ** p_s
        F_prod = (sp.Rational(r_A_val) ** p_s) * (sp.Rational(r_B_val) ** p_s)
        diff = sp.simplify(F_total - F_prod)
        mult_details.append((float(p), str(diff)))
        if diff != 0:
            ok_mult = False
    check(
        "Multiplicative factorization F_p[A+B] = F_p[A] F_p[B] for p in {1, 2, 1/2}",
        ok_mult,
        f"(p, sympy.simplify(F_total - F_prod)): {mult_details}",
    )
    # Additivity check for p = 1 (raw r, not log): expect failure.
    p_s = sp.Rational(1)
    F_total = (sp.Rational(r_total)) ** p_s
    F_sum = (sp.Rational(r_A_val) ** p_s) + (sp.Rational(r_B_val) ** p_s)
    diff_add = sp.simplify(F_total - F_sum)
    check(
        "Additivity FAILS for F_1 = r on the independent block toy (P3 witness)",
        diff_add != 0,
        f"F_1[A+B] - F_1[A] - F_1[B] = {diff_add} (nonzero -> additivity fails)",
    )
    # Additivity check for log r (the p -> 0 limit / W representative).
    log_total = sp.log(sp.Rational(r_total))
    log_sum = sp.log(sp.Rational(r_A_val)) + sp.log(sp.Rational(r_B_val))
    diff_log = sp.simplify(log_total - log_sum)
    check(
        "Additivity HOLDS for log r on the independent block toy (W representative)",
        diff_log == 0,
        f"log(r_A r_B) - log r_A - log r_B = {diff_log}",
    )


# ----------------------------------------------------------------------
# T9: Scope boundary — admission + non-promotion strings
# ----------------------------------------------------------------------


def test_T9_scope_boundary() -> None:
    section("T9: Scope boundary — admission and non-promotion language")
    text = NOTE.read_text(encoding="utf-8")
    required_admissions = [
        "P1 is NOT closed positively by the\noperator-algebraic attempt",
        "Operator-algebraic primitives do not retire P1",
        "they recast it",
        "the same structural",
        "(C5) counterexample",
    ]
    for s in required_admissions:
        check(
            f'note contains admission string: "{s}"',
            s in text,
            f"present={s in text}",
        )
    forbidden = [
        "P1 is now derived",
        "P1 is closed by this note",
        "P1 is retired by this note",
        "this note promotes the status",
        "audit lane verdict: retained",
        "effective_status: retained (this note)",
        "effective_status: audited_clean (this note)",
    ]
    hits = [f for f in forbidden if f in text]
    check(
        "note avoids forbidden status-promotion strings",
        len(hits) == 0,
        f"forbidden_hits={hits}",
    )


# ----------------------------------------------------------------------
# T10: Source-note boundary
# ----------------------------------------------------------------------


def test_T10_source_note_boundary() -> None:
    section("T10: Source-note boundary")
    text = NOTE.read_text(encoding="utf-8")
    check(
        "Claim type declared bounded_theorem",
        "**Claim type:** bounded_theorem" in text,
    )
    check(
        "Status authority declares independent audit lane only",
        "Status authority:** independent audit lane only" in text,
    )
    check(
        "Source-note proposal disclaimer present",
        "Source-note proposal disclaimer" in text,
    )
    forbidden_overclaim = [
        "**Claim type:** positive_theorem",
        "**Claim type:** retained",
        "audited_clean (this note)",
        "retained_bounded (this note)",
    ]
    hits = [s for s in forbidden_overclaim if s in text]
    check(
        "no forbidden overclaim strings present",
        len(hits) == 0,
        f"hits={hits}",
    )


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------


def main() -> int:
    print("# Observable-principle P1 bridge operator-algebraic runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_hilbert_tensor_product_dim()
    test_T2_grassmann_determinant_factorization()
    test_T3_trace_state_tensor_product()
    test_T4_sub_route_discrimination()
    test_T5_counterexample_family_F_p()
    test_T6_cluster_decomposition_ledger_status()
    test_T7_alternative_scalar_functionals()
    test_T8_numerical_toy_staggered_blocks()
    test_T9_scope_boundary()
    test_T10_source_note_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
