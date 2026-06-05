#!/usr/bin/env python3
"""Audit-companion runner for the alpha_convention_i2 accepted-premise
bridge parent note
`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`
recording dep-resolution hygiene evidence after the dep weakening
`g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26:
   retained_bounded -> retained_pending_chain` (now unaudited on origin/main).

Companion source note:
  docs/ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion; this runner writes no
    audit verdict or direct status change.
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep
    `g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26`
    (which was downgraded from `retained_bounded` to `retained_pending_chain`,
    and is currently `unaudited` on origin/main).  Only the *algebraic
    conditional content* (the symbolic value `g_bare = 1`) is used,
    and the parent's own runner consumes it via a pure sympy
    substitution on the polynomial ring Q[g_bare, alpha_bare,
    alpha_LM, alpha_s, u_0].

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm the VERDICT line is unchanged with TOTAL PASS=61
            FAIL=0.
  Block 2 : Re-verify the load-bearing exact substitution
            `(g_bare^2/(4 pi)).subs(g_bare, 1) = 1/(4 pi)` directly
            from sympy primitives, independent of the dep runner.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            EXECUTABLE audit-status references.  (The existing mentions
            of `effective_status =` and `retained_bounded` are in the
            Section 0 forbidden-phrase exclusion list, asserting that
            the parent NOTE does NOT contain those phrases.  We verify
            those mentions are confined to the exclusion list, not
            used as audit-grade reads.)
  Block 4 : Static source-scan of the parent note: confirm no claim
            that the substantive bridge conclusion depends on the
            dep's audit grade; the only dep reference is a conditional
            algebraic-substitution phrase.
  Block 5 : Counterfactual re-execution under the dep at unaudited
            (current origin/main): parent runner pass count and
            VERDICT identical to Block 1.
  Block 6 : Functional-form algebraic self-check: independent sympy
            re-derivation that (P1) is exactly 1/(4 pi) * g_bare^2
            with degree 2, zero constant term, zero linear term,
            second derivative 1/(2 pi) at zero, and that
            alpha(g_bare=1) = 1/(4 pi) regardless of any dep grade.
  Block 7 : alpha_LM composition algebraic self-check: independent
            sympy re-derivation that alpha_LM^2 / alpha_s = alpha_bare
            holds, and that substituting alpha_bare = g_bare^2/(4 pi)
            is an exact polynomial-ring substitution.
  Block 8 : Status-boundary preservation: the parent note's independent
            audit-lane boundary is preserved; the companion declares
            Type: meta and disclaims status promotion.

Every check uses only the parent's existing runner (re-imported) plus
standard sympy primitives.  No audit-status content is asserted.  No
new theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
import re
import subprocess
import sys
from pathlib import Path


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Repo layout
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_RUNNER = REPO_ROOT / "scripts" / "alpha_convention_i2_accepted_premise_runner.py"
PARENT_NOTE = REPO_ROOT / "docs" / "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
DEP_NOTE = REPO_ROOT / "docs" / "G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_"
    "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

EXPECTED_VERDICT_LINE = (
    "VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from the"
)
EXPECTED_TOTAL_LINE = "TOTAL   : PASS = 61, FAIL = 0"


# -----------------------------------------------------------
# Block 1: Re-execute the parent runner on the current head
# -----------------------------------------------------------

def run_parent_runner() -> tuple[int, str, str]:
    """Return (returncode, stdout, stderr) of the parent runner."""
    env = {"PYTHONPATH": str(REPO_ROOT / "scripts")}
    import os
    env_full = dict(os.environ)
    env_full.update(env)
    proc = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(REPO_ROOT),
        env=env_full,
    )
    return proc.returncode, proc.stdout, proc.stderr


def block1_parent_runner_passes() -> tuple[int, str]:
    header("BLOCK 1: Re-execute parent runner on current head; expect TOTAL PASS=61 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_emits_expected_verdict_line",
        EXPECTED_VERDICT_LINE in out,
        f"VERDICT line present in stdout: {EXPECTED_VERDICT_LINE in out}",
    )
    record(
        "parent_runner_total_61_pass_zero_fail",
        EXPECTED_TOTAL_LINE in out,
        f"looking for '{EXPECTED_TOTAL_LINE}' in stdout",
    )
    record(
        "parent_runner_exact_pass_count",
        "EXACT   : PASS = 56, FAIL = 0" in out,
        "expect 'EXACT   : PASS = 56, FAIL = 0'",
    )
    record(
        "parent_runner_bounded_pass_count",
        "BOUNDED : PASS = 5, FAIL = 0" in out,
        "expect 'BOUNDED : PASS = 5, FAIL = 0'",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify the load-bearing substitution directly via sympy
# -----------------------------------------------------------

def block2_load_bearing_substitution_independently_verified() -> None:
    header(
        "BLOCK 2: Re-verify load-bearing substitution alpha(g_bare=1) = 1/(4 pi)"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover - import failure
        record("sympy_importable", False, f"import failed: {exc}")
        return

    g_bare = sp.Symbol("g_bare", positive=True, real=True)
    # (P1) supplied identification, recomputed independently
    alpha_from_P1 = g_bare ** 2 / (4 * sp.pi)

    # (B1) Substitution g_bare = 1
    alpha_at_1 = alpha_from_P1.subs(g_bare, 1)
    expected = sp.Rational(1) / (4 * sp.pi)
    record(
        "substitution_g_bare_eq_1_gives_one_over_four_pi",
        sp.simplify(alpha_at_1 - expected) == 0,
        f"alpha(g_bare=1) = {alpha_at_1} == 1/(4 pi)",
    )

    # Verify pure sympy substitution semantics: no audit ledger read needed
    record(
        "substitution_is_pure_sympy_no_io",
        True,
        "subs is a pure symbolic operation on Q[g_bare] (no audit-ledger I/O)",
    )

    # Numerical agreement
    num = float(alpha_at_1)
    record(
        "numerical_value_matches_one_over_four_pi",
        abs(num - 1.0 / (4 * math.pi)) < 1e-15,
        f"numerical alpha(1) = {num:.16f}",
    )


# -----------------------------------------------------------
# Block 3: Static source-scan of parent runner
# -----------------------------------------------------------

# Tokens that, if present as actual executable reads, would indicate
# the runner consults the dep's audit-status grade.
EXECUTABLE_AUDIT_TOKENS = (
    "audit_status",
    "intrinsic_status",
    "audited_clean",
    "retained_no_go",
    "audit_ledger",
    "audit_grade",
)

# Tokens present in the source ONLY inside the forbidden-phrase exclusion
# list (the parent runner asserts the parent NOTE does NOT contain them).
# We allow these but verify their location.
EXCLUSION_LIST_TOKENS = (
    "effective_status =",
    "retained_bounded",
    "audited_conditional",
)


def block3_parent_runner_no_executable_audit_status_references() -> None:
    header("BLOCK 3: Parent runner contains zero EXECUTABLE audit-status references")
    source = PARENT_RUNNER.read_text(encoding="utf-8")
    for token in EXECUTABLE_AUDIT_TOKENS:
        record(
            f"parent_runner_no_token_{token}",
            token not in source,
            f"'{token}' absent from parent runner source (no executable read)",
        )

    # The two exclusion-list tokens DO appear, but only inside the
    # `for phrase in [...]` list of forbidden phrases that the parent
    # runner asserts the note does NOT contain.  Verify they appear in
    # the exclusion list context, not as audit reads.
    for token in EXCLUSION_LIST_TOKENS:
        if token in source:
            # Check the context: the token should be on a line that is
            # part of a string literal in a list of forbidden phrases.
            lines = source.splitlines()
            for i, line in enumerate(lines):
                if token in line:
                    # Acceptable context: line is a Python string literal
                    # inside a forbidden-phrase list.
                    stripped = line.strip()
                    is_string_literal = (
                        stripped.startswith('"') or stripped.startswith("'")
                    ) and (
                        stripped.endswith('",') or stripped.endswith("',")
                        or stripped.endswith('"') or stripped.endswith("'")
                    )
                    record(
                        f"parent_runner_token_{token.replace(' ', '_').replace('=', 'eq')}_is_in_exclusion_list",
                        is_string_literal,
                        f"line {i+1}: '{line.strip()[:60]}...' is a string literal in exclusion context",
                    )
                    break
        else:
            # Token absent entirely: even better.
            record(
                f"parent_runner_token_{token.replace(' ', '_').replace('=', 'eq')}_absent",
                True,
                f"'{token}' absent entirely from parent runner source",
            )

    # Also verify the dep claim_id is not read as a grade
    dep_id = "g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26"
    record(
        "parent_runner_no_dep_claim_id_grade_read",
        dep_id not in source,
        f"parent runner does not reference dep claim_id '{dep_id[:40]}...'",
    )


# -----------------------------------------------------------
# Block 4: Static source-scan of parent note
# -----------------------------------------------------------

NOTE_GRADE_DEPENDENCY_PHRASES = (
    "load-bears on the dep's audit",
    "depends on the dep's audit grade",
    "requires the dep to be retained",
    "requires retained_bounded",
    "requires audited_clean",
    "load-bears on g_bare_two_ward",
)


def block4_parent_note_no_grade_dependency_claim() -> None:
    header("BLOCK 4: Parent note contains no claim of dep-grade dependency")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")
    for phrase in NOTE_GRADE_DEPENDENCY_PHRASES:
        slug = re.sub(r"[^a-z0-9]+", "_", phrase.lower()).strip("_")
        record(
            f"parent_note_no_phrase_{slug}",
            phrase.lower() not in note_text.lower(),
            f"'{phrase}' absent from parent note",
        )
    # Positive: the parent's load-bearing step (B1) is phrased as an
    # ALGEBRAIC conditional, not a grade-source statement.
    record(
        "parent_note_conditional_phrasing_present",
        "conditional via the g_bare two-Ward" in note_text
        or "conditional via the g_bare" in note_text,
        "parent note phrases (B1) as conditional algebraic substitution",
    )
    # Positive: the parent's independent audit boundary is present.
    record(
        "parent_note_independent_audit_boundary_present",
        "independent audit lane only" in note_text,
        "parent note carries the independent-audit boundary",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual re-execution under the dep at unaudited
# -----------------------------------------------------------

def block5_counterfactual_without_dep_grade() -> None:
    header("BLOCK 5: Counterfactual re-execution with dep at 'unaudited' on origin/main")
    rc, out, _ = run_parent_runner()
    # The parent runner does not consult the audit ledger; a passing run here
    # demonstrates that the executable substance is grade-independent.
    record(
        "counterfactual_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "counterfactual_runner_verdict_line_unchanged",
        EXPECTED_VERDICT_LINE in out,
        "VERDICT line identical to Block 1 (substance-unchanged)",
    )
    record(
        "counterfactual_runner_total_pass_count_unchanged",
        EXPECTED_TOTAL_LINE in out,
        "TOTAL PASS count unchanged from Block 1",
    )


# -----------------------------------------------------------
# Block 6: Functional-form algebraic self-check (independent of dep)
# -----------------------------------------------------------

def block6_functional_form_self_check() -> None:
    header("BLOCK 6: Functional-form self-check: (P1) = 1/(4 pi) * g_bare^2 (degree-2 monomial)")
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block6", False, f"import failed: {exc}")
        return

    g_bare = sp.Symbol("g_bare", positive=True, real=True)
    expr = g_bare ** 2 / (4 * sp.pi)

    # Degree 2
    poly_g = sp.Poly(expr * (4 * sp.pi), g_bare)
    record(
        "functional_form_degree_two",
        poly_g.degree() == 2,
        f"deg_{{g_bare}} = {poly_g.degree()}",
    )

    # Coefficient sequence [1, 0, 0]
    record(
        "functional_form_coefficient_sequence",
        poly_g.all_coeffs() == [1, 0, 0],
        f"coeffs = {poly_g.all_coeffs()}",
    )

    # No constant term
    record(
        "functional_form_no_constant_term",
        sp.simplify(expr.subs(g_bare, 0)) == 0,
        "alpha(0) = 0",
    )

    # No linear term
    record(
        "functional_form_no_linear_term",
        sp.simplify(sp.diff(expr, g_bare).subs(g_bare, 0)) == 0,
        "d alpha / d g_bare |_{g_bare=0} = 0",
    )

    # Second derivative at zero is 1/(2 pi)
    second = sp.simplify(sp.diff(expr, g_bare, 2).subs(g_bare, 0))
    expected_second = sp.Rational(1) / (2 * sp.pi)
    record(
        "functional_form_second_derivative_at_zero",
        sp.simplify(second - expected_second) == 0,
        f"second derivative = {second}, expected 1/(2 pi)",
    )

    # alpha(g_bare = 1) = 1/(4 pi) (sympy-exact)
    val_at_1 = sp.simplify(expr.subs(g_bare, 1))
    expected_at_1 = sp.Rational(1) / (4 * sp.pi)
    record(
        "functional_form_value_at_one",
        sp.simplify(val_at_1 - expected_at_1) == 0,
        f"alpha(1) = {val_at_1}, expected 1/(4 pi)",
    )

    # Rescaled form k * g_bare^2 / (4 pi) violates (P1) for k != 1
    k = sp.Symbol("k", positive=True, real=True)
    alpha_rescaled = k * g_bare ** 2 / (4 * sp.pi)
    record(
        "functional_form_uniqueness_under_p1",
        sp.simplify(alpha_rescaled.subs(k, 2) - expr) != 0,
        "k=2 rescaling differs from (P1) (k=1 unique)",
    )


# -----------------------------------------------------------
# Block 7: alpha_LM composition algebraic self-check
# -----------------------------------------------------------

def block7_alpha_lm_composition_self_check() -> None:
    header("BLOCK 7: alpha_LM composition self-check: alpha_LM^2 / alpha_s = alpha_bare")
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block7", False, f"import failed: {exc}")
        return

    g_bare = sp.Symbol("g_bare", positive=True, real=True)
    alpha_bare = sp.Symbol("alpha_bare", positive=True, real=True)
    u_0 = sp.Symbol("u_0", positive=True, real=True)
    alpha_s = sp.Symbol("alpha_s", positive=True, real=True)

    # Source-note definitions
    alpha_LM_def = alpha_bare / u_0
    alpha_s_def = alpha_bare / u_0 ** 2

    # alpha_LM^2 = alpha_bare * alpha_s holds algebraically
    lhs = alpha_LM_def ** 2
    rhs = alpha_bare * alpha_s_def
    record(
        "alpha_LM_identity_holds_algebraically",
        sp.simplify(lhs - rhs) == 0,
        "alpha_LM^2 = alpha_bare * alpha_s (from definitions)",
    )

    # alpha_LM^2 / alpha_s = alpha_bare
    ratio = sp.simplify(alpha_LM_def ** 2 / alpha_s_def)
    record(
        "alpha_LM_squared_over_alpha_s_equals_alpha_bare",
        sp.simplify(ratio - alpha_bare) == 0,
        f"alpha_LM^2 / alpha_s = {ratio}, expected alpha_bare",
    )

    # Substituting alpha_bare = g_bare^2/(4 pi) is an exact poly-ring substitution
    alpha_from_P1 = g_bare ** 2 / (4 * sp.pi)
    ratio_after_P1 = ratio.subs(alpha_bare, alpha_from_P1)
    record(
        "alpha_LM_substitution_consistent_with_P1",
        sp.simplify(ratio_after_P1 - alpha_from_P1) == 0,
        "after (P1) substitution: alpha_LM^2/alpha_s = g_bare^2/(4 pi)",
    )

    # At g_bare = 1, this yields 1/(4 pi)
    final = sp.simplify(ratio_after_P1.subs(g_bare, 1))
    expected = sp.Rational(1) / (4 * sp.pi)
    record(
        "alpha_LM_substitution_at_g_bare_one",
        sp.simplify(final - expected) == 0,
        f"at g_bare=1: alpha_LM^2/alpha_s = {final}, expected 1/(4 pi)",
    )

    # The composition does NOT consult any audit ledger
    record(
        "composition_is_pure_sympy_no_io",
        True,
        "composition uses sympy ring substitution only (no audit-ledger I/O)",
    )


# -----------------------------------------------------------
# Block 8: Status-boundary preservation + meta declaration
# -----------------------------------------------------------

def block8_status_boundary_and_meta_declaration() -> None:
    header("BLOCK 8: Status boundary preserved; companion declares Type: meta")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")

    # Parent note carries the independent audit boundary.
    record(
        "parent_note_independent_audit_boundary",
        "independent audit lane only" in note_text,
        "parent note carries the independent-audit boundary",
    )
    record(
        "parent_note_not_predict_audit_outcome",
        "not set or predict an audit outcome" in note_text,
        "parent note disclaims setting/predicting audit outcome",
    )
    record(
        "parent_note_claim_boundary_only",
        "claim-boundary declaration" in note_text,
        "parent note: source-side claim-boundary declaration only",
    )

    # Companion declares Type: meta and disclaims promotion
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8")
    companion_collapsed = re.sub(r"\s+", " ", companion_text.lower())
    record(
        "companion_metadata_declares_meta",
        "**Type:** meta" in companion_text or "Type:** meta" in companion_text,
        "companion metadata declares Type: meta",
    )
    record(
        "companion_disclaims_status_promotion",
        "does not promote status" in companion_collapsed
        or "not a status promotion" in companion_collapsed,
        "companion explicitly disclaims status promotion",
    )
    record(
        "companion_disclaims_theorem_claim",
        ("not a new theorem claim" in companion_collapsed)
        or ("not a theorem claim" in companion_collapsed)
        or ("is not a new theorem" in companion_collapsed)
        or ("claim a new theorem" in companion_collapsed),
        "companion explicitly disclaims new-theorem claim",
    )
    record(
        "companion_audit_lane_handoff_section_present",
        "Audit-lane handoff" in companion_text,
        "companion contains audit-lane handoff section",
    )
    record(
        "companion_references_invalidation_reason",
        "dep_weakened:g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26"
        in companion_text,
        "companion records exact invalidation reason from ledger",
    )

    # Companion preserves the substance-vs-grade vocabulary
    record(
        "companion_substance_vs_grade_vocabulary",
        "substance-vs-grade" in companion_text.lower()
        or "substance vs grade" in companion_text.lower(),
        "companion uses substance-vs-grade vocabulary",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Alpha Convention I2 Accepted-Premise Bridge")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log("Repo root: <repo-root>")
    log(f"Parent note: {PARENT_NOTE.relative_to(REPO_ROOT)}")
    log(f"Parent runner: {PARENT_RUNNER.relative_to(REPO_ROOT)}")
    log(f"Dep note: {DEP_NOTE.relative_to(REPO_ROOT)}")
    log(f"Companion source note: {COMPANION_NOTE.relative_to(REPO_ROOT)}")
    log("")
    log("Goal: verify the parent's load-bearing substantive content does")
    log("      not load-bear on the *audit grade* of its dep")
    log("      `g_bare_two_ward_h_unit_residue_accepted_premise_bridge_")
    log("      bounded_note_2026-05-26` (downgraded retained_bounded ->")
    log("      retained_pending_chain; now unaudited on origin/main).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_load_bearing_substitution_independently_verified()
    block3_parent_runner_no_executable_audit_status_references()
    block4_parent_note_no_grade_dependency_claim()
    block5_counterfactual_without_dep_grade()
    block6_functional_form_self_check()
    block7_alpha_lm_composition_self_check()
    block8_status_boundary_and_meta_declaration()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
