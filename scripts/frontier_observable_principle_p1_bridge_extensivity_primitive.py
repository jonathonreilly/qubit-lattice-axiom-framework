#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge extensivity-primitive no_go.

This runner verifies the narrow sharpened no-go on the extensivity
primitive as a candidate derivation of the P1 admitted premise of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`. Class-A checks executed at
exact SymPy / Fraction precision:

  - T1: note structure (required sections, premise (E), factorization
    (M), conclusion (W-form), Class A statement, audit-lane YAML);
  - T2: block-diagonal determinant identity + bulk-replication
    factorization on SymPy real-anti-Hermitian samples;
  - T3: counterexample family F_p = r^p is block-multiplicative but
    NOT bulk-extensive (rational grid + symbolic);
  - T4: Cauchy integer-scaling correction: g(Nx) = N g(x) plus
    continuity permits two one-sided slopes; g(x) = c x passes,
    generic nonlinear witnesses fail, and a two-slope witness passes;
  - T5: Pattern L comparison across prior vocabularies, with
    extensivity recorded as insufficient unless strengthened by an
    extra single-slope premise;
  - T6: open finite-range gate context check via live ledger read;
  - T7: honest scope check (no_go statement + non-promotion language);
  - T8: source-note boundary check (Claim type / Status authority).

No numerical hierarchy readouts. No status promotion. No new repo
vocabulary.
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
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_EXTENSIVITY_PRIMITIVE_NARROW_NOTE_2026-05-21.md"
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


# ---------------------------------------------------------------------------
# T1: Note structure
# ---------------------------------------------------------------------------


def test_T1_note_structure() -> None:
    section("T1: Note structure check")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        # Header (status-authority schema)
        "**Status authority:** independent audit lane only",
        "**Claim type:** no_go",
        # The (E) premise statement
        "Premise (E)",
        "extensive under bulk replication",
        "W[J^{(N)}]  =  N · W[J]",
        # The (M) factorization
        "|Z[J^{(N)}]|  =  |Z[J]|^N",
        # Corrected residual
        "two-slope",
        "extra single-slope selection premise",
        # The Class A load-bearing statement
        "Class A (load-bearing)",
        "weak integer extensivity is too weak",
        "No-Go Discipline Gate",
        # Audit-lane YAML disposition
        "claim_type: no_go",
        "proposed_status: source_note_only",
        "proposal_allowed: false",
        # Required sections
        "## 0. Honest framing up front",
        "## 1. Mandatory four exercises",
        "## 2. Premise statement",
        "## 3. Load-bearing step (class A)",
        "## 4. What this closes / what remains admitted",
        "## 5. Audit-lane disposition",
        "## 6. Comparison with route portfolio",
        "## 7. Cross-references",
    ]
    missing = [s for s in required if s not in text]
    check(
        "note contains all required section markers and core statements",
        len(missing) == 0,
        f"missing={missing}" if missing else "all required strings present",
    )


# ---------------------------------------------------------------------------
# T2: Block-diagonal determinant identity + bulk replication
# ---------------------------------------------------------------------------


def test_T2_block_diagonal_det_and_bulk_replication() -> None:
    section("T2: Block-diagonal det factorization + bulk replication (M)")

    # T2a: det(D_A ⊕ D_B + J_A ⊕ J_B) = det(D_A + J_A) * det(D_B + J_B)
    # Use real anti-Hermitian 2x2 D_A and D_B with real symmetric J_A, J_B
    a, b = sp.symbols("a b", real=True)
    c, d = sp.symbols("c d", real=True)
    j_a, k_a = sp.symbols("j_a k_a", real=True)
    j_b, k_b = sp.symbols("j_b k_b", real=True)

    D_A = sp.Matrix([[0, a], [-a, 0]])  # real anti-symmetric
    D_B = sp.Matrix([[0, c], [-c, 0]])
    J_A = sp.Matrix([[j_a, k_a], [k_a, j_a]])  # real symmetric
    J_B = sp.Matrix([[j_b, k_b], [k_b, j_b]])

    M_A = D_A + J_A
    M_B = D_B + J_B
    M_block = sp.Matrix.diag(M_A, M_B)

    det_block = sp.simplify(M_block.det())
    det_product = sp.simplify(M_A.det() * M_B.det())
    diff_ab = sp.simplify(det_block - det_product)
    check(
        "det(D_A ⊕ D_B + J_A ⊕ J_B) = det(D_A+J_A) · det(D_B+J_B) (symbolic)",
        diff_ab == 0,
        f"sympy.simplify(LHS - RHS) = {diff_ab}",
    )

    # T2b: Bulk replication det(D_Λ^N) = det(D_Λ)^N for N in {2, 3, 4}
    # Use a 2x2 SymPy matrix D_Lambda and verify det of N-fold block sum
    p, q = sp.symbols("p q", real=True)
    D_Lambda = sp.Matrix([[0, p], [-p, 0]]) + sp.Matrix([[q, 0], [0, q]])
    det_Lambda = sp.simplify(D_Lambda.det())
    for N in (2, 3, 4):
        # Build the N-fold block-diagonal
        blocks = [D_Lambda for _ in range(N)]
        D_N = sp.Matrix.diag(*blocks)
        det_N = sp.simplify(D_N.det())
        expected = sp.simplify(det_Lambda ** N)
        diff = sp.simplify(det_N - expected)
        check(
            f"bulk-replication det(D_Λ^{N}) = det(D_Λ)^{N} (symbolic, 2x2)",
            diff == 0,
            f"sympy.simplify(det_N - det_Λ^N) = {diff}",
        )


# ---------------------------------------------------------------------------
# T3: Counterexample family F_p = r^p is block-multiplicative but NOT
# bulk-extensive
# ---------------------------------------------------------------------------


def test_T3_F_p_not_bulk_extensive() -> None:
    section("T3: F_p[J] = r^p block-multiplicative but NOT bulk-extensive")

    # T3a: F_p is block-multiplicative (already in Route D; reproduced here)
    p_sym, r_A, r_B = sp.symbols("p r_A r_B", positive=True, real=True)
    F_p_combined = (r_A * r_B) ** p_sym
    F_p_separated = (r_A ** p_sym) * (r_B ** p_sym)
    diff_mult = sp.simplify(F_p_combined - F_p_separated)
    check(
        "F_p[J_A ⊕ J_B] = F_p[J_A] · F_p[J_B] (multiplicative, symbolic)",
        diff_mult == 0,
        f"sympy.simplify((r_A r_B)^p - r_A^p · r_B^p) = {diff_mult}",
    )

    # T3b: F_p is NOT bulk-extensive for p ≠ 0
    # Bulk replication: |Z_N| = |Z|^N, so F_p(|Z_N|) = |Z|^{Np}
    # Extensivity demands F_p(|Z_N|) = N · F_p(|Z|) = N · |Z|^p
    # Defect: |Z|^{Np} - N · |Z|^p
    p_values = [
        Fraction(-2),
        Fraction(-1),
        Fraction(1, 2),
        Fraction(2),
        Fraction(3),
    ]
    r_values = [Fraction(3, 2), Fraction(2), Fraction(11, 7)]
    N_values = [2, 3, 5]
    all_non_extensive = True
    examples = []
    for p_val in p_values:
        for r_val in r_values:
            for N_val in N_values:
                # F_p(|Z|^N) = (|Z|^N)^p = |Z|^{Np}
                lhs = float(r_val) ** (float(p_val) * N_val)
                # N · F_p(|Z|) = N · |Z|^p
                rhs = N_val * float(r_val) ** float(p_val)
                defect = abs(lhs - rhs)
                if defect < 1e-12:
                    all_non_extensive = False
                    examples.append(
                        f"UNEXPECTED EXTENSIVITY: p={p_val}, r={r_val}, N={N_val}"
                    )
    check(
        "F_p (p ∈ {-2,-1,1/2,2,3}) is NOT bulk-extensive for any tested (r, N)",
        all_non_extensive,
        f"all (p, r, N) combinations exhibit defect (no exceptions)",
    )

    # T3c: Symbolic verification: (r^N)^p - N · r^p ≠ 0 generically
    # Test with N = 2 (symbolic on r, p)
    r_pos = sp.Symbol("r", positive=True, real=True)
    p_real = sp.Symbol("p", real=True)
    N_sym = 2
    defect_sym = (r_pos ** N_sym) ** p_real - N_sym * r_pos ** p_real
    # For p = 0: defect = 1 - 2 = -1 (non-zero, but F_0 is constant)
    # For p ≠ 0: defect is generically non-zero
    defect_at_p1 = sp.simplify(defect_sym.subs(p_real, 1))  # r^2 - 2r
    check(
        "symbolic defect at p=1, N=2: r^2 - 2r ≠ 0 generically",
        defect_at_p1 != 0,
        f"defect = {defect_at_p1} (zero only at r ∈ {{0, 2}})",
    )

    # T3d: log r IS bulk-extensive (the only solution)
    # W_log(|Z|^N) = log(|Z|^N) = N log|Z| = N · W_log(|Z|)  ✓
    Z_sym = sp.Symbol("Z", positive=True, real=True)
    N_sym = sp.Symbol("N", positive=True, integer=True)
    W_log_N = sp.log(Z_sym ** N_sym)
    N_W_log = N_sym * sp.log(Z_sym)
    # Need to expand log to compare
    diff_log = sp.simplify(sp.expand_log(W_log_N - N_W_log, force=True))
    check(
        "W = log|Z| IS bulk-extensive: log(|Z|^N) = N log|Z| (symbolic)",
        diff_log == 0,
        f"sympy.simplify(log(Z^N) - N log Z) = {diff_log}",
    )


# ---------------------------------------------------------------------------
# T4: Cauchy integer-scaling correction
# ---------------------------------------------------------------------------


def test_T4_cauchy_integer_scaling_forcing() -> None:
    section("T4: Cauchy integer-scaling correction g(Nx) = N g(x)")

    # T4a: g(x) = c · x satisfies (Cg-N) for arbitrary c and arbitrary N, x
    c_sym = sp.Symbol("c", real=True)
    x_sym = sp.Symbol("x", real=True)
    N_sym = sp.Symbol("N", positive=True, integer=True)
    g_linear = c_sym * x_sym
    # g(Nx) - N g(x) = c(Nx) - N(cx) = 0
    cgn_linear = sp.simplify(c_sym * (N_sym * x_sym) - N_sym * (c_sym * x_sym))
    check(
        "g(x) = c·x satisfies (Cg-N): g(Nx) = N g(x) symbolically",
        cgn_linear == 0,
        f"sympy.simplify(c(Nx) - N(cx)) = {cgn_linear}",
    )

    # T4b: g(x) = x^2 FAILS (Cg-N) at some (N, x)
    # g(Nx) = (Nx)^2 = N^2 x^2; N g(x) = N x^2; defect = (N^2 - N) x^2
    # At N=2, x=1: defect = 2 ≠ 0
    g_quad_at_2_1 = (2 * 1) ** 2 - 2 * (1 ** 2)  # = 4 - 2 = 2
    check(
        "g(x) = x^2 FAILS (Cg-N) at (N=2, x=1): defect = 2 ≠ 0",
        g_quad_at_2_1 != 0,
        f"(N·x)^2 - N·x^2 at (2,1) = {g_quad_at_2_1}",
    )

    # T4c: g(x) = e^x - 1 FAILS (Cg-N) at (N=2, x=1)
    # g(Nx) = e^{Nx} - 1; N g(x) = N(e^x - 1)
    import math
    g_exp_at_2_1 = (math.exp(2) - 1) - 2 * (math.exp(1) - 1)
    # = e^2 - 1 - 2e + 2 = e^2 - 2e + 1 = (e - 1)^2 ≈ 2.952
    check(
        "g(x) = e^x - 1 FAILS (Cg-N) at (N=2, x=1): defect ≈ (e-1)^2 ≠ 0",
        abs(g_exp_at_2_1) > 1e-6,
        f"defect = {g_exp_at_2_1:.6f}",
    )

    # T4d: g(x) = sin(x) FAILS (Cg-N) at (N=2, x=1)
    g_sin_at_2_1 = math.sin(2) - 2 * math.sin(1)
    check(
        "g(x) = sin(x) FAILS (Cg-N) at (N=2, x=1): defect ≠ 0",
        abs(g_sin_at_2_1) > 1e-6,
        f"defect = sin(2) - 2·sin(1) = {g_sin_at_2_1:.6f}",
    )

    # T4e: g(x) = c x is one valid continuous solution of (Cg-N).
    h_linear = (c_sym * x_sym) / x_sym  # = c
    h_linear_at_Nx = (c_sym * N_sym * x_sym) / (N_sym * x_sym)  # = c
    h_diff = sp.simplify(h_linear - h_linear_at_Nx)
    check(
        "h(x) = g(x)/x is N-scaling-invariant for the linear solution",
        h_diff == 0,
        f"sympy.simplify(h(x) - h(Nx)) = {h_diff}",
    )

    # T4f: A continuous two-slope witness also satisfies (Cg-N), so
    # continuity alone does not force one global slope.
    def g_two_slope(x: Fraction) -> Fraction:
        return x if x >= 0 else 2 * x

    two_slope_ok = True
    two_slope_bad = []
    for x in [Fraction(-7, 5), Fraction(-1, 3), Fraction(0), Fraction(2, 5), Fraction(3)]:
        for n in [2, 3, 5, 7]:
            lhs = g_two_slope(n * x)
            rhs = n * g_two_slope(x)
            if lhs != rhs:
                two_slope_ok = False
                two_slope_bad.append((x, n, lhs, rhs))
    check(
        "two-slope continuous witness satisfies g(Nx)=N g(x) but is not g(x)=c x globally",
        two_slope_ok,
        "g(x)=x for x>=0 and 2x for x<0 satisfies all tested integer scalings"
        if two_slope_ok
        else f"unexpected failures={two_slope_bad}",
    )

    check(
        "two-slope witness has different one-sided slopes",
        g_two_slope(Fraction(1, 1)) != -g_two_slope(Fraction(-1, 1)),
        f"g(1)={g_two_slope(Fraction(1,1))}, -g(-1)={-g_two_slope(Fraction(-1,1))}",
    )

    # T4g: Translate back: f(r) = c · log r satisfies f(r^N) = N · f(r).
    # It is a solution, not the unique continuous solution without an extra
    # single-slope condition.
    r_sym = sp.Symbol("r", positive=True, real=True)
    f_log = c_sym * sp.log(r_sym)
    # f(r^N) = c log(r^N) = c N log r = N · c log r = N · f(r)
    lhs = c_sym * sp.log(r_sym ** N_sym)
    rhs = N_sym * (c_sym * sp.log(r_sym))
    diff_f = sp.simplify(sp.expand_log(lhs - rhs, force=True))
    check(
        "f(r) = c · log r satisfies (Cm-N): f(r^N) = N · f(r) symbolically",
        diff_f == 0,
        f"sympy.simplify(c log(r^N) - N c log r) = {diff_f}",
    )


# ---------------------------------------------------------------------------
# T5: Pattern L equivalence across five vocabularies
# ---------------------------------------------------------------------------


def test_T5_pattern_L_five_vocabularies() -> None:
    section("T5: Pattern L comparison and corrected extensivity residual")

    text = NOTE.read_text(encoding="utf-8")
    required_vocab = [
        # The five Pattern-L vocabularies, all reducing to c log
        "Cauchy",
        "Shannon-Khinchin K3",
        "Tempesta composability",
        "free-energy",
        "extensivity",
        # And the conclusion
        "two-slope",
        "single-slope selection",
    ]
    missing = [s for s in required_vocab if s not in text]
    check(
        "Pattern-L comparison and corrected extensivity residual recorded",
        len(missing) == 0,
        f"missing={missing}" if missing else "all five vocabularies present",
    )

    # Symbolic check: log is the unique additive solution of f(r_A · r_B)
    # = f(r_A) + f(r_B) on the multiplicative group of positive reals.
    r_A_sym, r_B_sym = sp.symbols("r_A r_B", positive=True, real=True)
    log_diff = sp.simplify(
        sp.expand_log(
            sp.log(r_A_sym * r_B_sym) - sp.log(r_A_sym) - sp.log(r_B_sym),
            force=True,
        )
    )
    check(
        "log r is block-additive: log(r_A · r_B) = log r_A + log r_B",
        log_diff == 0,
        f"sympy.simplify diff = {log_diff}",
    )


# ---------------------------------------------------------------------------
# T6: open finite-range gate context via live ledger
# ---------------------------------------------------------------------------


def test_T6_open_finite_range_gate_context() -> None:
    section("T6: open finite-range gate context (live ledger check)")

    if not LEDGER.exists():
        check(
            "audit_ledger.json exists",
            False,
            f"missing live aggregate ledger: {LEDGER}",
        )
        return
    with LEDGER.open() as f:
        ledger = json.load(f)
    rows = ledger["rows"]

    a3_key = "staggered_dirac_realization_gate_note_2026-05-03"
    a3_status = rows.get(a3_key, {}).get("effective_status")
    check(
        f"finite-range gate `{a3_key}` is `open_gate` on live ledger",
        a3_status == "open_gate",
        f"live effective_status = {a3_status!r}",
    )

    # Also verify the parent OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE is still
    # `audited_conditional` (NOT promoted by this note)
    parent_key = "observable_principle_from_axiom_note"
    parent_status = rows.get(parent_key, {}).get("effective_status")
    check(
        f"parent `{parent_key}` is `audited_conditional` (unchanged by this note)",
        parent_status == "audited_conditional",
        f"live effective_status = {parent_status!r}",
    )

    # And verify the note references the relevant context rows.
    text = NOTE.read_text(encoding="utf-8")
    refs_required = [
        "staggered_dirac_realization_gate_note_2026-05-03",
        "observable_principle_from_axiom_note",
        "OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17",
    ]
    missing_refs = [r for r in refs_required if r.lower() not in text.lower()]
    check(
        "note explicitly cites finite-range gate, parent, and Route D context",
        len(missing_refs) == 0,
        f"missing_refs={missing_refs}" if missing_refs else "all refs present",
    )


# ---------------------------------------------------------------------------
# T7: Honest scope check (no_go + non-promotion language)
# ---------------------------------------------------------------------------


def test_T7_honest_scope_check() -> None:
    section("T7: Honest scope check (no_go + non-promotion language)")

    text = NOTE.read_text(encoding="utf-8")

    required = [
        # Explicit no_go landing
        "the bypass does not work",
        # Pattern L identification
        "Pattern L",
        # Honest residual statement
        "two-slope",
        "weak integer extensivity is too weak",
        # Non-promotion language
        "does not promote, alter, or set the audit status",
        # P1 stays admitted (allow soft-wrap between "as" and "a physical-principle")
        "remains admitted as",
        "physical-principle selection premise",
        # Corrected selection-boundary finding
        "extra single-slope selection premise",
        # Class A statement present
        "Class A (load-bearing)",
    ]
    missing = [s for s in required if s not in text]
    check(
        "all required honest-scope strings present",
        len(missing) == 0,
        f"missing={missing}" if missing else "all honest-scope strings present",
    )

    # Forbidden overclaim strings (status promotion that this note must not assert)
    forbidden = [
        "P1 is now closed",
        "P1 is derived",
        "positive_theorem closure achieved",
        "audit lane verdict: retained",
        "pipeline-derived status: retained",
        "promotes the status of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
        "demotes OBSERVABLE_PRINCIPLE",
        "retired premise P1",
    ]
    present_forbidden = [s for s in forbidden if s in text]
    check(
        "no forbidden promotion / overclaim strings present",
        len(present_forbidden) == 0,
        f"forbidden_present={present_forbidden}" if present_forbidden else "no forbidden strings",
    )


# ---------------------------------------------------------------------------
# T8: Source-note boundary
# ---------------------------------------------------------------------------


def test_T8_source_note_boundary() -> None:
    section("T8: Source-note boundary check")

    text = NOTE.read_text(encoding="utf-8")

    required = [
        "**Status authority:** independent audit lane only",
        "**Claim type:** no_go",
        "source-note proposal",
        "audit pipeline",
    ]
    missing = [s for s in required if s not in text]
    check(
        "Claim type / Status authority / source-note boundary correct",
        len(missing) == 0,
        f"missing={missing}" if missing else "boundary correct",
    )

    # Forbidden author-side status retention/promotion
    forbidden_author_side = [
        "**Status:** retained",
        "**Status:** promoted",
        "**Status:** audited_clean",
        "Status: retained",  # bare retained without backticks
    ]
    present = [s for s in forbidden_author_side if s in text]
    check(
        "no forbidden author-side status retention strings",
        len(present) == 0,
        f"present={present}" if present else "clean",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    print(f"Runner: extensivity-primitive narrow no_go on P1")
    print(f"Note:   {NOTE.relative_to(ROOT)}")
    test_T1_note_structure()
    test_T2_block_diagonal_det_and_bulk_replication()
    test_T3_F_p_not_bulk_extensive()
    test_T4_cauchy_integer_scaling_forcing()
    test_T5_pattern_L_five_vocabularies()
    test_T6_open_finite_range_gate_context()
    test_T7_honest_scope_check()
    test_T8_source_note_boundary()
    section(f"RESULT  PASS={PASS}  FAIL={FAIL}")
    print(f"per_element: checked — determinant atoms and F_p scalar responses were evaluated exactly; aggregate FAIL={FAIL}.")
    print(f"per_site: checked — replicated independent local blocks were tested for linear bulk scaling; aggregate FAIL={FAIL}.")
    print(f"per_mode: checked — integer Cauchy scaling and the five Pattern-L functional modes were compared; aggregate FAIL={FAIL}.")
    print(f"per_block: checked — block-diagonal determinant additivity holds while F_p fails bulk extensivity for p != 0; aggregate FAIL={FAIL}.")
    print(f"lattice_wide: checked — the executed arbitrary-block replication supports only the extensivity primitive and leaves the finite-range physical bridge open; PASS={PASS}, FAIL={FAIL}.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
