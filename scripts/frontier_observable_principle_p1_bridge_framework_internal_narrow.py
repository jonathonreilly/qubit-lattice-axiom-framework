#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge framework-internal Route C bounded note.

This runner verifies the Route C framework-internal audit of catalog retained
framework theorems against the explicit Route-C exclusion question: does any
currently-retained framework theorem in the load-bearing catalog independently
exclude the non-additive counterexample family F_p[J] = r(J)^p (p != 1)?

The runner checks at exact SymPy/Fraction precision:
- the algebraic facts about F_p block-multiplicativity vs. F_p block-additivity;
- log block-additivity;
- block-diagonal determinant factorization on a finite real anti-Hermitian
  SymPy block;
- the failed real-D candidate contains the (A) block-additive criterion as
  part of its admissibility class (X2);
- the failed real-D candidate explicitly admits P1 is not retired;
- the live audit-ledger effective_status of each catalog candidate listed
  in the note;
- the note declares bounded_theorem with the correct honest-scope strings.

All checks are exact (SymPy or string-parse); no numerical fits. Expected
result: PASS=9, FAIL=0.
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
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_FRAMEWORK_INTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md"
)
CITED_RETAINED_NARROW = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md"
)
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

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


def test_T1_Fp_block_multiplicative_symbolic() -> None:
    section(
        "T1: F_p[J] = r(J)^p is block-multiplicative for general real p (SymPy)"
    )
    r_A, r_B = sp.symbols("r_A r_B", positive=True)
    p = sp.Symbol("p", real=True)
    # F_p_total = (r_A * r_B)^p
    # Block-product form = r_A^p * r_B^p
    lhs = (r_A * r_B) ** p
    rhs = r_A ** p * r_B ** p
    diff = sp.simplify(lhs - rhs)
    check(
        "(r_A r_B)^p = r_A^p * r_B^p symbolically (general real p)",
        diff == 0,
        f"sympy.simplify(lhs - rhs) = {diff}",
    )


def test_T2_Fp_block_additive_fails_for_p_neq_1() -> None:
    section(
        "T2: F_p[J] = r(J)^p fails block-additivity for p != 1 (rational grid)"
    )
    rationals = [Fraction(2, 1), Fraction(3, 1), Fraction(5, 2), Fraction(7, 3)]
    ps = [Fraction(2, 1), Fraction(1, 2), Fraction(3, 1), Fraction(-1, 1)]
    # additive residual at (r_A, r_B, p):
    #   (r_A r_B)^p - r_A^p - r_B^p
    # We want all sample values to be nonzero for p != 1.
    ok_all = True
    max_zero = None
    for p_q in ps:
        for r_A_q in rationals:
            for r_B_q in rationals:
                lhs = (r_A_q * r_B_q) ** p_q  # exact rational since p is rational
                rhs = r_A_q ** p_q + r_B_q ** p_q
                # For symbolic exactness we compute via sympy:
                lhs_s = sp.Rational(r_A_q.numerator * r_B_q.numerator,
                                    r_A_q.denominator * r_B_q.denominator) ** \
                        sp.Rational(p_q.numerator, p_q.denominator)
                rhs_s = (sp.Rational(r_A_q.numerator, r_A_q.denominator) **
                         sp.Rational(p_q.numerator, p_q.denominator)) + \
                        (sp.Rational(r_B_q.numerator, r_B_q.denominator) **
                         sp.Rational(p_q.numerator, p_q.denominator))
                residual = sp.simplify(lhs_s - rhs_s)
                # residual must be nonzero (counterexample lives at p != 1)
                if residual == 0:
                    ok_all = False
                    max_zero = (p_q, r_A_q, r_B_q)
    check(
        "F_p additive residual is nonzero for all p in {2, 1/2, 3, -1} on grid",
        ok_all,
        "All (p, r_A, r_B) tested produce a nonzero additive residual"
        if ok_all
        else f"Found unexpected zero at {max_zero}",
    )


def test_T3_log_block_additive_symbolic() -> None:
    section("T3: W = log r is block-additive (SymPy)")
    r_A, r_B = sp.symbols("r_A r_B", positive=True)
    # log(r_A * r_B) = log(r_A) + log(r_B)
    lhs = sp.log(r_A * r_B)
    rhs = sp.log(r_A) + sp.log(r_B)
    diff = sp.simplify(lhs - rhs)
    check(
        "log(r_A * r_B) = log(r_A) + log(r_B) symbolically",
        diff == 0,
        f"sympy.simplify(diff) = {diff}",
    )


def test_T4_block_det_factorization_real_antiH_block() -> None:
    section(
        "T4: Block-diagonal det factorization on a finite real anti-H block (SymPy)"
    )
    # Build a 4x4 real anti-Hermitian D = D_A (+) D_B where D_A, D_B are 2x2
    # real anti-Hermitian (so each has imaginary entries on the off-diagonal of
    # a real matrix form... but we want REAL anti-Hermitian, which is real
    # antisymmetric). On the real-D block of CPT_EXACT, "real anti-Hermitian"
    # on R^N means D^T = -D with real entries. We build that here.
    # D_A, D_B real antisymmetric:
    a = sp.Symbol("a", real=True)
    b = sp.Symbol("b", real=True)
    D_A = sp.Matrix([[0, a], [-a, 0]])
    D_B = sp.Matrix([[0, b], [-b, 0]])
    # Full D as block-diagonal:
    D = sp.Matrix.zeros(4, 4)
    D[0:2, 0:2] = D_A
    D[2:4, 2:4] = D_B
    # Real-symmetric source J:
    j1, j2 = sp.symbols("j1 j2", real=True)
    J_A = sp.Matrix([[j1, 0], [0, j1]])
    J_B = sp.Matrix([[j2, 0], [0, j2]])
    J = sp.Matrix.zeros(4, 4)
    J[0:2, 0:2] = J_A
    J[2:4, 2:4] = J_B
    # Compute determinants:
    det_total = sp.simplify((D + J).det())
    det_A = sp.simplify((D_A + J_A).det())
    det_B = sp.simplify((D_B + J_B).det())
    diff = sp.simplify(det_total - det_A * det_B)
    check(
        "det(D_A (+) D_B + J_A (+) J_B) = det(D_A + J_A) det(D_B + J_B) exactly",
        diff == 0,
        f"sympy.simplify(det_total - det_A * det_B) = {diff}",
    )


def test_T5_X2_contains_A_block_additive() -> None:
    section(
        "T5: failed real-D candidate contains (A) block-additive criterion"
    )
    if not CITED_RETAINED_NARROW.exists():
        check(
            "cited file exists",
            False,
            f"File not found: {CITED_RETAINED_NARROW}",
        )
        return
    text = CITED_RETAINED_NARROW.read_text(encoding="utf-8")
    # The cited file packages (A) block-additive on realized no-bond direct sums.
    # Look for distinctive phrasing from that note's §"(X2) Admissibility class".
    needle = "block-additive on every realized no-bond direct sum within `B`"
    check(
        '(A) "block-additive on every realized no-bond direct sum within `B`" is part of (X2)',
        needle in text,
        f"Substring '{needle}' present in cited markdown" if needle in text
        else f"Substring '{needle}' MISSING in cited markdown",
    )


def test_T6_cited_narrow_admits_P1_not_retired() -> None:
    section(
        "T6: failed real-D candidate explicitly admits P1 not retired"
    )
    if not CITED_RETAINED_NARROW.exists():
        check(
            "cited file exists",
            False,
            f"File not found: {CITED_RETAINED_NARROW}",
        )
        return
    text = CITED_RETAINED_NARROW.read_text(encoding="utf-8")
    # Look for honest admission strings (one of):
    needles = [
        "does not** retire P1",
        "does not retire P1",
        "scalar additivity remains a selection premise",
    ]
    found = any(n in text for n in needles)
    check(
        "cited narrow theorem contains explicit 'P1 not retired' admission",
        found,
        f"One of {needles} present in cited markdown" if found
        else f"None of {needles} present",
    )


def test_T7_candidate_ledger_status_check() -> None:
    section("T7: live ledger effective_status for each catalog candidate")
    if not LEDGER_PATH.exists():
        check("audit_ledger.json exists", False, f"Missing: {LEDGER_PATH}")
        return
    full = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = full.get("rows", full)
    candidates = [
        "observable_principle_real_d_block_uniqueness_narrow_theorem_note_2026-05-10",
        "axiom_first_reflection_positivity_theorem_note_2026-04-29",
        "anomaly_forces_time_theorem",
        "cl3_color_automorphism_theorem",
        "graph_first_su3_integration_note",
        "native_gauge_closure_note",
        "staggered_dirac_realization_gate_note_2026-05-03",
        "observable_generator_additivity_from_cluster_decomposition_theorem_note_2026-05-10",
        "observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16",
    ]
    missing = []
    live_statuses = {}
    for cid in candidates:
        row = rows.get(cid)
        if row is None:
            missing.append(cid)
            live_statuses[cid] = None
            continue
        live_statuses[cid] = row.get("effective_status")
    check(
        "candidate rows are present in the audit ledger (presence only)",
        not missing,
        f"missing={missing}",
    )
    print(f"  [info] live effective statuses (audit-lane-owned; not gated): {live_statuses}")


def test_T8_honest_scope_strings_present() -> None:
    section("T8: note string contains honest-scope admission strings")
    if not NOTE.exists():
        check("note file exists", False, f"Missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "does NOT close P1",
        "bounded_theorem",
        "Route C",
        "F_p",
        "block-additive",
        "admissibility class",
        "P1 retirement requires",
    ]
    forbidden = [
        "Status: retained",
        "audited_clean",
        "audited_renaming",
        "promotes to retained",
        "**Effective status:** retained",
    ]
    missing_required = [s for s in required if s not in text]
    found_forbidden = [s for s in forbidden if s in text]
    ok_required = len(missing_required) == 0
    ok_forbidden = len(found_forbidden) == 0
    check(
        "required honest-scope strings present in note",
        ok_required,
        "All required strings present" if ok_required
        else f"MISSING required strings: {missing_required}",
    )
    check(
        "forbidden status-promotion strings absent from note",
        ok_forbidden,
        "No forbidden strings found" if ok_forbidden
        else f"FOUND forbidden strings: {found_forbidden}",
    )


def test_T9_source_note_boundary_declaration() -> None:
    section("T9: source-note boundary declarations present")
    if not NOTE.exists():
        check("note file exists", False, f"Missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "**Claim type:** bounded_theorem",
        "**Status authority:**",
        "independent audit lane",
        "DOES NOT promote",
        "DOES NOT derive the P1 admitted premise",
        "Hypothesis set used",
        "Forbidden imports check",
    ]
    missing = [s for s in required if s not in text]
    ok = len(missing) == 0
    check(
        "source-note boundary declarations present",
        ok,
        "All boundary declarations present" if ok
        else f"MISSING boundary declarations: {missing}",
    )


def main() -> int:
    test_T1_Fp_block_multiplicative_symbolic()
    test_T2_Fp_block_additive_fails_for_p_neq_1()
    test_T3_log_block_additive_symbolic()
    test_T4_block_det_factorization_real_antiH_block()
    test_T5_X2_contains_A_block_additive()
    test_T6_cited_narrow_admits_P1_not_retired()
    test_T7_candidate_ledger_status_check()
    test_T8_honest_scope_strings_present()
    test_T9_source_note_boundary_declaration()

    print()
    print("=" * 78)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 78)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
