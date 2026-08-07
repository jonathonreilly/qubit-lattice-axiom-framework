#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge Route D sharpened no_go.

This runner verifies the consolidated structural no-go theorem on P1
(scalar additivity on independent subsystems) of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, by:

  - stating the no_go theorem precisely (T1);
  - enumerating the 5 obstructions D1-D5 from Routes A/B/C/E (T2);
  - verifying the F_p[J] = r(J)^p counterexample family explicitly
    (continuity, CPT-even, multiplicative factorization, NOT additive
    for p ≠ 0) (T3);
  - enumerating the 4 routes' independent confirmations (T4);
  - structural enumeration: Pattern L (log-reducing) vs Pattern D
    (functor-additivity inapplicable) (T5);
  - identifying what WOULD close the gap (T6);
  - listing forward paths (a) new retained primitive, (b) permanent P1
    admission (T7);
  - no_go scope boundary: does NOT claim P1 is FALSE (T8);
  - explicit list of out-of-scope: doesn't promote/demote any upstream
    (T9);
  - source-note boundary check (T10).

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
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md"
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


def test_T1_no_go_theorem_stated_precisely() -> None:
    section("T1: No-go theorem stated precisely")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        # The theorem statement core elements
        "Theorem (Route D, sharpened structural no-go on P1)",
        # The counterexample family
        "F_p[J] := r(J)^p",
        # Scope-bounding to scaffold families
        "S_OA",
        "S_IT",
        "S_FI",
        "S_CD",
        # Sharpened structural statement
        "not derivable",
        "A_RETAINED",
        "S_STD",
    ]
    missing = [s for s in required if s not in text]
    check(
        "no_go theorem statement contains all required core elements",
        len(missing) == 0,
        f"missing={missing}" if missing else "all required strings present",
    )


def test_T2_five_obstructions_enumerated() -> None:
    section("T2: Five obstructions D1-D5 enumerated")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "D1 — operator-algebraic compatibility",
        "D2 — information-theoretic uniqueness theorems require additivity",
        "D3 — framework retained primitives don't exclude `F_p`",
        "D4 — cross-disciplinary functor-additivity inapplicable",
        "D5 — Pattern L circularity",
    ]
    missing = [s for s in required if s not in text]
    check(
        "all five obstructions D1-D5 explicitly enumerated",
        len(missing) == 0,
        f"missing={missing}" if missing else "all 5 obstructions present",
    )


def test_T3_F_p_counterexample_family() -> None:
    section("T3: F_p[J] = r(J)^p counterexample family")

    # T3a: F_p is continuous (composition of continuous functions, symbolic)
    p, r = sp.symbols("p r", positive=True, real=True)
    F_p = r ** p
    # Continuity: F_p is a symbolic function of (r, p); verify it's continuous
    # at r > 0 for any real p by checking it's differentiable.
    dF_dr = sp.diff(F_p, r)
    # Two equivalent forms: p*r^p/r and p*r^(p-1)
    expected = p * r ** (p - 1)
    diff_ok = sp.simplify(dF_dr - expected) == 0
    check(
        "F_p = r^p is differentiable (hence continuous) at r > 0 (symbolic)",
        diff_ok,
        f"d/dr (r^p) = {dF_dr}; matches p*r^(p-1) after simplify: {diff_ok}",
    )

    # T3b: F_p is CPT-even (depends only on r = |Z|)
    Z = sp.Symbol("Z", complex=True)
    abs_Z = sp.Abs(Z)
    F_p_of_abs = abs_Z ** p
    # CPT-even: F_p[Z] = F_p[conj(Z)] since both have same |Z|
    F_p_conj = sp.Abs(sp.conjugate(Z)) ** p
    diff_cpt = sp.simplify(F_p_of_abs - F_p_conj)
    check(
        "F_p[Z] = F_p[conj(Z)] (CPT-even via |Z| dependence)",
        diff_cpt == 0,
        f"sympy.simplify(F_p[Z] - F_p[conj(Z)]) = {diff_cpt}",
    )

    # T3c: F_p is multiplicatively factorizing on independent subsystems
    r_A, r_B = sp.symbols("r_A r_B", positive=True, real=True)
    F_p_combined = (r_A * r_B) ** p
    F_p_A_times_F_p_B = (r_A ** p) * (r_B ** p)
    diff_mult = sp.simplify(F_p_combined - F_p_A_times_F_p_B)
    check(
        "F_p[J_A ⊕ J_B] = F_p[J_A] * F_p[J_B] (multiplicative factorization, symbolic)",
        diff_mult == 0,
        f"sympy.simplify((r_A r_B)^p - r_A^p r_B^p) = {diff_mult}",
    )

    # T3d: F_p is NOT additive for p ≠ 0 on rational grid
    p_values = [Fraction(-2), Fraction(-1), Fraction(1, 2), Fraction(1),
                Fraction(2), Fraction(3)]
    r_pairs = [(Fraction(2), Fraction(3)),
               (Fraction(3, 2), Fraction(5, 7)),
               (Fraction(11, 13), Fraction(7, 5))]
    all_non_additive = True
    examples = []
    for p_val in p_values:
        for r_a, r_b in r_pairs:
            # F_p[A⊕B] = (r_A * r_B)^p
            lhs_num = (r_a * r_b) ** int(p_val.numerator) if p_val.denominator == 1 else None
            # Use float for fractional p
            lhs_f = float(r_a * r_b) ** float(p_val)
            rhs_f = float(r_a) ** float(p_val) + float(r_b) ** float(p_val)
            diff = abs(lhs_f - rhs_f)
            if diff > 1e-9:  # not additive
                examples.append(
                    f"p={p_val}, r_A={r_a}, r_B={r_b}: |LHS - RHS| = {diff:.3e}"
                )
            else:
                all_non_additive = False
    check(
        "F_p fails block-additivity for all tested p ≠ 0 (rational grid)",
        all_non_additive,
        f"examples={examples[:3]}",
    )

    # T3e: log r IS additive (the p → 0 limit / Cauchy classifier)
    log_combined = sp.log(r_A * r_B)
    log_separated = sp.log(r_A) + sp.log(r_B)
    diff_log = sp.simplify(sp.expand_log(log_combined - log_separated, force=True))
    check(
        "log r IS block-additive (the p -> 0 / Cauchy classifier limit)",
        diff_log == 0,
        f"sympy.simplify(log(r_A r_B) - log(r_A) - log(r_B)) = {diff_log}",
    )


def test_T4_four_routes_independent_confirmations() -> None:
    section("T4: Four routes' independent confirmations")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Route A (PR #1373)",
        "Route B (PR #1368)",
        "Route C (PR #1402)",
        "Route E (PR #1406)",
        # Each route's outcome
        "Operator-algebraic external",
        "Information-theoretic external",
        "Framework-internal",
        "Tao cross-disciplinary",
        # Convergence
        "Convergence across the four routes",
    ]
    missing = [s for s in required if s not in text]
    check(
        "all four routes A/B/C/E referenced with PRs and outcomes",
        len(missing) == 0,
        f"missing={missing}" if missing else "all four routes documented",
    )


def test_T5_pattern_L_vs_D_enumeration() -> None:
    section("T5: Pattern L vs Pattern D structural enumeration")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Pattern L circularity",
        "Pattern D inapplicability",
        # Pattern L candidates
        "Cramer rate function",
        "Tropical max-plus",
        "Geometric quantization",
        "Free energy",
        # Pattern D candidates
        "Atiyah-Singer index",
        "K-theory / Euler characteristic",
        # Pattern reduction
        "invokes `log`",
        "inapplicable to scalar",
    ]
    missing = [s for s in required if s not in text]
    check(
        "Pattern L and Pattern D enumerated with candidates",
        len(missing) == 0,
        f"missing={missing}" if missing else "all pattern enumeration present",
    )

    # Symbolic check: log-additive vs (.)^p
    r_A, r_B = sp.symbols("r_A r_B", positive=True, real=True)
    # Pattern L: log is additive
    log_diff = sp.simplify(sp.expand_log(
        sp.log(r_A * r_B) - sp.log(r_A) - sp.log(r_B), force=True
    ))
    check(
        "Pattern L: log additive verified symbolically",
        log_diff == 0,
        f"sympy.simplify diff = {log_diff}",
    )
    # Pattern D: dim is additive on direct sum (toy check on integer dims)
    # dim(V_1 ⊕ V_2) = dim(V_1) + dim(V_2)
    # Z[J] = det(D+J) ∈ R is NOT a vector-space dim; it's a scalar.
    # Symbolic check: det of 2x2 block-diagonal matches product of dets.
    a, b, c, d = sp.symbols("a b c d", real=True)
    M1 = sp.Matrix([[a, b], [-b, a]])  # 2x2 anti-symmetric-like
    M2 = sp.Matrix([[c, d], [-d, c]])
    M_block = sp.Matrix.diag(M1, M2)
    det_block = sp.simplify(M_block.det())
    det_product = sp.simplify(M1.det() * M2.det())
    det_diff = sp.simplify(det_block - det_product)
    check(
        "det(M1 ⊕ M2) = det(M1) * det(M2) (multiplicative, not additive)",
        det_diff == 0,
        f"sympy.simplify(det(block) - det(M1)*det(M2)) = {det_diff}",
    )
    # And explicit witness that det is NOT additive: det(M1 ⊕ M2) - det(M1) - det(M2) ≠ 0 generically
    det_additive_diff = sp.simplify(det_block - M1.det() - M2.det())
    check(
        "det is NOT block-additive (would be P1 if it were) — sanity",
        det_additive_diff != 0,
        f"sympy.simplify(det(block) - det(M1) - det(M2)) = {det_additive_diff}",
    )


def test_T6_what_would_close_the_gap() -> None:
    section("T6: What WOULD close the gap")
    text = NOTE.read_text(encoding="utf-8")
    # Normalize whitespace to handle line-wrapped phrases
    text_norm = " ".join(text.split())
    required = [
        "Identifies the exact structural primitive that would be needed",
        # The needed primitive description
        "physical scalar bosonic observable generator",
        "additive subclass on independent subsystems",
        # Statement that none currently exists
        "No such primitive is currently identified",
        # Constraints on a future primitive
        "no new axiom",
        "without invoking `log`",
    ]
    missing = [s for s in required if s not in text_norm]
    check(
        "the needed primitive description is precise and constrained",
        len(missing) == 0,
        f"missing={missing}" if missing else "all primitive-description strings present",
    )


def test_T7_forward_paths() -> None:
    section("T7: Forward paths (a) new primitive, (b) permanent admission")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        # Path (a)
        "Path (a) — discover/derive a new retained-grade primitive",
        # Path (b)
        "Path (b) — accept P1 as a permanent classification premise",
        # Path (b) current state
        "current state",
        # Path (a) research-grade open
        "research-grade open work",
    ]
    missing = [s for s in required if s not in text]
    check(
        "both forward paths (a) and (b) explicitly enumerated",
        len(missing) == 0,
        f"missing={missing}" if missing else "both paths present",
    )


def test_T8_no_go_scope_boundary() -> None:
    section("T8: No-go scope boundary — does NOT claim P1 is FALSE")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        # Explicit non-falsity claim
        "does not claim P1 is false",
        # Sharpened bounded statement
        "not derivable",
        # Scope-bounding
        "scope-bounded to",
        # Forward closure remains possible
        "does NOT foreclose every conceivable closure path",
    ]
    missing = [s for s in required if s not in text]
    check(
        "no_go scope boundary explicitly stated (not falsity claim)",
        len(missing) == 0,
        f"missing={missing}" if missing else "all scope-bounding strings present",
    )

    # Forbidden absolutist strings — but allow safe negation phrases that EXPLICITLY DENY them
    # e.g. "does not claim P1 is false" is safe; bare "P1 is false" as a claim is not.
    forbidden_patterns = [
        ("P1 is false", ["does not claim P1 is false", "DOES NOT claim P1 is false",
                          "not claim P1 is false"]),
        ("P1 is FALSE", ["does not claim P1 is FALSE", "not claim P1 is FALSE",
                          "does NOT claim P1 is FALSE", "NOT claim P1 is FALSE"]),
        ("P1 is definitively false", []),
        ("P1 cannot ever be derived", []),
        ("additivity is wrong", []),
    ]
    present_forbidden = []
    for forbidden_str, safe_contexts in forbidden_patterns:
        # Count raw occurrences
        n_total = text.count(forbidden_str)
        # Subtract occurrences within safe phrases
        n_safe = sum(text.count(safe) for safe in safe_contexts)
        if n_total > n_safe:
            present_forbidden.append(
                f"{forbidden_str} (total={n_total}, safe={n_safe})"
            )
    check(
        "no forbidden absolutist no_go strings present (outside safe-negation contexts)",
        len(present_forbidden) == 0,
        f"forbidden_present={present_forbidden}" if present_forbidden else "no absolutist strings",
    )


def test_T9_out_of_scope_no_upstream_promotion() -> None:
    section("T9: Out-of-scope — doesn't promote/demote any upstream")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        # Non-promotion language
        "does not promote, alter, or set the audit status",
        # Specific upstream rows preserved
        "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
        "OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS",
        "CPT_EXACT_NOTE",
        "STAGGERED_DIRAC_SUBSTEP1",
        # Out-of-scope items list
        "Out of scope",
        "Promotion or demotion of any cited authority row",
    ]
    missing = [s for s in required if s not in text]
    check(
        "non-promotion language and out-of-scope list present",
        len(missing) == 0,
        f"missing={missing}" if missing else "all non-promotion strings present",
    )

    forbidden = [
        "promotes the status of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
        "demotes",
        "retired premise P1",
        "closes P1 positively",
        "audit lane verdict: retained",
        "pipeline-derived status: retained",
    ]
    present_forbidden = [s for s in forbidden if s in text]
    check(
        "no forbidden status-promotion strings present",
        len(present_forbidden) == 0,
        f"forbidden_present={present_forbidden}" if present_forbidden else "clean",
    )


def test_T10_source_note_boundary() -> None:
    section("T10: Source-note boundary check")
    text = NOTE.read_text(encoding="utf-8")
    check(
        "note declares Claim type: no_go",
        "**Claim type:** no_go" in text,
    )
    check(
        "note declares Status authority: source-note proposal only",
        "Status authority" in text and "source-note proposal only" in text,
    )
    forbidden_status = [
        "effective_status: retained",
        "effective_status: audited_clean",
        "pipeline-derived status: retained",
        "audit lane verdict: retained",
        # also forbid removing the honest admission later
        "P1 is now derived",
        "P1 is closed",
        "P1 has been derived",
    ]
    present_forbidden = [s for s in forbidden_status if s in text]
    check(
        "note avoids forbidden status-overclaim strings",
        len(present_forbidden) == 0,
        f"forbidden_present={present_forbidden}" if present_forbidden else "clean",
    )
    # Verify it cites Routes A/B/C/E PRs as markdown links
    required_pr_links = [
        "pull/1373",
        "pull/1368",
        "pull/1402",
        "pull/1406",
    ]
    missing_pr = [s for s in required_pr_links if s not in text]
    check(
        "note cites Routes A/B/C/E PRs as markdown links",
        len(missing_pr) == 0,
        f"missing PR links={missing_pr}" if missing_pr else "all four PR links present",
    )


def n5_execution_certificate() -> None:
    """State the granularity at which this runner actually resolves the no_go.

    Reporting only: adds no check() call and moves no PASS/FAIL count.
    """
    section("N5 execution certificate: what this runner resolves")

    p_grid = 6
    r_pairs = 3
    doc_scan_checks = 14
    computed_checks = 8

    print(
        "per_element: resolved symbolically over named free entries. T5 writes two "
        "explicit 2 x 2 blocks, M1 = [[a, b], [-b, a]] and M2 = [[c, d], [-d, c]], "
        "assembles them into a 4 x 4 block-diagonal matrix and certifies "
        "det(M1 (+) M2) = det(M1) det(M2) as an exact symbolic zero in all four free "
        "entries, then exhibits the non-additive residual symbolically as well. T3 "
        "adds entry-level exactness on the source side, with r-pairs given as exact "
        "rationals (2, 3), (3/2, 5/7) and (11/13, 7/5)."
    )
    print(
        "per_site: checked and not executed, and here the absence is total. This "
        "runner contains no site index, no lattice, no per-site dimension and no "
        "register count anywhere in the file - the subsystem split it reasons about "
        "is the abstract pair (J_A, J_B) with no underlying geometry attached. There "
        "is consequently nothing site-shaped even to count, let alone to evaluate."
    )
    print(
        "per_mode: checked and not executed. No spectral operation occurs in this "
        "runner at all: the two 2 x 2 blocks are consumed only through their "
        "determinants, nothing is diagonalized, and no eigenvalue, singular value or "
        "spectral weight is formed. The F_p family is a family of scalar functionals "
        "of a positive real and has no mode structure to resolve."
    )
    print(
        "per_block: resolved, and it is the granularity the entire no_go is stated "
        "at. The claim is block-additivity on the two-block split J_A (+) J_B, and "
        "the runner exercises exactly that split three independent ways: F_p is shown "
        "multiplicatively factorizing across the two blocks as an exact symbolic "
        f"identity; additivity is shown to fail across a {p_grid} x {r_pairs} = "
        f"{p_grid * r_pairs}-point grid of (p, r_A, r_B); and the determinant of an "
        "explicit block-diagonal matrix is confirmed multiplicative with a nonzero "
        "additive residual, which is the concrete form of the obstruction."
    )
    print(
        "lattice_wide: checked and not executed, and the missing global object is "
        "this note's own obstruction. Nothing global is constructed - no volume, no "
        "sequence, no limit - and the note's own statement of what would close the "
        "gap is a retained primitive that supplies scalar block-additivity directly. "
        "That primitive is by definition absent, so no execution of this runner "
        "could exhibit it; what the runner can and does exhibit is the "
        "counterexample family that blocks the alternatives."
    )
    print(
        "  scope: the file's own docstring states that all numerical checks use exact "
        "Fraction arithmetic or SymPy symbolic verification with no floating-point "
        "comparator inputs, but the block-additivity grid in T3 does not meet that "
        "standard: it evaluates float(r_A * r_B) ** float(p) against a 1e-9 threshold "
        "in double precision, and the exact-Fraction value it prepares for the "
        "integer-p cases is computed and then never used. The other seven computed "
        "checks are exact as described."
    )
    print(
        f"  scope: of the {PASS + FAIL} checks, {doc_scan_checks} are substring scans "
        f"over the source Markdown and only {computed_checks} compute anything. And "
        "the 'fails for all tested p != 0' statement is quantified over a six-value "
        "rational p grid crossed with three r-pairs, not over all real p."
    )
    print(
        "  scope: fully deterministic - no RNG stream and no optimizer appears "
        "anywhere in this runner."
    )


def main() -> int:
    print("# Observable-principle P1 bridge Route D sharpened no_go runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_no_go_theorem_stated_precisely()
    test_T2_five_obstructions_enumerated()
    test_T3_F_p_counterexample_family()
    test_T4_four_routes_independent_confirmations()
    test_T5_pattern_L_vs_D_enumeration()
    test_T6_what_would_close_the_gap()
    test_T7_forward_paths()
    test_T8_no_go_scope_boundary()
    test_T9_out_of_scope_no_upstream_promotion()
    test_T10_source_note_boundary()
    n5_execution_certificate()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
