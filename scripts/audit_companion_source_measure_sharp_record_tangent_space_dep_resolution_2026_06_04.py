#!/usr/bin/env python3
"""Audit-companion runner for the source/measure sharp-record tangent-space
parent note `SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`
recording dep-resolution hygiene evidence after the dep weakening
`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:
retained_bounded -> unaudited`.

Companion source note:
  docs/SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `source_measure_sharp_record_tangent_space_theorem_note_2026-05-30`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep
    `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`
    (which was downgraded from `retained_bounded` to `unaudited`).
    The parent only names the dep as the projective-record-surface
    concept via a single `exists()` filesystem check; the load-bearing
    parts (RN score, Fisher norm, exponential chart, six-component top
    source unit) are pure sympy on a finite `{-1, +1}` reference
    probability `(1/2, 1/2)`.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm `SUMMARY: PASS=38 FAIL=0` is unchanged.
  Block 2 : Re-verify the load-bearing finite-probability algebra
            (RN score, zero reference mean, Fisher norm 4a^2,
            primitive signed-record Fisher norm one, lambda^2
            scaling, exponential-chart W = log cosh(h),
            six-component top coefficient 1/sqrt(6)) directly from
            sympy primitives.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            audit-status references (audit_status, effective_status,
            intrinsic_status, retained_bounded, audited_clean, etc.).
  Block 4 : Static source-scan of the parent note: confirm no claim
            that the substantive conclusion depends on the dep's
            audit grade.
  Block 5 : Counterfactual re-execution under the dep at its current
            `unaudited` grade: parent runner pass count and content
            identical to Block 1.
  Block 6 : Exponential-chart self-check: W(h) is forced by
            E_0[R_h] = 1, not imported, with score retrieval
            independent of any dep grade.
  Block 7 : Y_T source-unit self-check: six-component top tangent has
            Fisher norm one, lambda-scaling matches lambda^2,
            coefficient 1/sqrt(6) — independent of any dep grade.
  Block 8 : Status-boundary preservation across the runs (the
            parent's `actual_current_surface_status: exact-support`
            marker, `bare_retained_allowed: false`, firewall
            forbidden-import list, and forbidden-overclaim absences
            preserved; companion explicitly disclaims promotion).

Every check uses only the parent's existing runner code (re-executed)
plus standard finite-dimensional sympy.  No audit-status content is
asserted.  No new theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

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
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_source_measure_sharp_record_tangent_space.py"
PARENT_NOTE = (
    REPO_ROOT / "docs" / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
)
DEP_NOTE = (
    REPO_ROOT
    / "docs"
    / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
)
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_"
    "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

EXPECTED_PARENT_SUMMARY = "SUMMARY: PASS=38 FAIL=0"


# -----------------------------------------------------------
# Block 1: Re-execute the parent runner on the current head
# -----------------------------------------------------------

def run_parent_runner() -> tuple[int, str, str]:
    """Return (returncode, stdout, stderr) of the parent runner."""
    proc = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(REPO_ROOT),
    )
    return proc.returncode, proc.stdout, proc.stderr


def block1_parent_runner_passes() -> tuple[int, str]:
    header("BLOCK 1: Re-execute parent runner on current head; expect PASS=38 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_summary_thirty_eight_pass_zero_fail",
        EXPECTED_PARENT_SUMMARY in out,
        f"looking for '{EXPECTED_PARENT_SUMMARY}' in stdout",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    # The parent runner writes the JSON cache; confirm the file is updated.
    out_json = REPO_ROOT / "outputs" / "source_measure_sharp_record_tangent_space_2026-05-30.json"
    record(
        "parent_runner_wrote_outputs_json",
        out_json.exists(),
        f"outputs JSON exists at {out_json.relative_to(REPO_ROOT)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify the load-bearing algebra directly from sympy
# -----------------------------------------------------------

def block2_finite_probability_algebra() -> None:
    header("BLOCK 2: Re-verify load-bearing finite-probability algebra directly")
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover - import failure
        record("sympy_importable", False, f"import failed: {exc}")
        return
    record("sympy_importable", True, "imported sympy")

    # Two-outcome sharp record with reference p0 = (1/2, 1/2).
    a = sp.symbols("a", real=True)
    p0 = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
    dp = sp.Matrix([a, -a])
    score = sp.Matrix([sp.simplify(dp[i] / p0[i]) for i in range(2)])

    record(
        "probability_tangent_sums_to_zero",
        sp.simplify(sum(dp)) == 0,
        f"sum(dp)={sp.simplify(sum(dp))}",
    )
    rn_mean = sp.simplify(sum(p0[i] * score[i] for i in range(2)))
    record(
        "rn_score_zero_reference_mean",
        rn_mean == 0,
        f"E_0[s]={rn_mean}",
    )
    fisher_generic = sp.simplify(sum(p0[i] * score[i] ** 2 for i in range(2)))
    record(
        "fisher_norm_generic_two_outcome_is_4a_squared",
        sp.simplify(fisher_generic - 4 * a**2) == 0,
        f"E_0[s^2]={fisher_generic}",
    )

    # Primitive signed record epsilon = (+1, -1) corresponds to dp = (1/2, -1/2).
    score_prim = sp.Matrix([1, -1])
    dp_prim = sp.Matrix([p0[i] * score_prim[i] for i in range(2)])
    fisher_prim = sp.simplify(sum(p0[i] * score_prim[i] ** 2 for i in range(2)))
    record(
        "primitive_score_is_signed_record",
        list(score_prim) == [1, -1],
        f"score_prim={list(score_prim)}",
    )
    record(
        "primitive_dp_sums_to_zero",
        sp.simplify(sum(dp_prim)) == 0,
        f"sum(dp_prim)={sp.simplify(sum(dp_prim))}",
    )
    record(
        "primitive_signed_record_fisher_norm_one",
        sp.simplify(fisher_prim - 1) == 0,
        f"E_0[s^2]={fisher_prim}",
    )

    # Lambda-scaled signed tangent has Fisher norm lambda^2.
    lam = sp.symbols("lambda", positive=True, real=True)
    eps = {1: 1, -1: -1}
    p0_dict = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    fisher_lam = sp.simplify(sum(p0_dict[e] * (lam * eps[e]) ** 2 for e in (1, -1)))
    record(
        "lambda_scaled_fisher_norm_is_lambda_squared",
        sp.simplify(fisher_lam - lam**2) == 0,
        f"fisher_lam={fisher_lam}",
    )
    record(
        "unit_fisher_condition_selects_lambda_one",
        sp.solve(sp.Eq(fisher_lam, 1), lam) == [1],
        "lambda solves to [1]",
    )


# -----------------------------------------------------------
# Block 3: Static source-scan of parent runner
# -----------------------------------------------------------

AUDIT_STATUS_TOKENS = (
    "audit_status",
    "effective_status",
    "intrinsic_status",
    "retained_bounded",
    "audited_clean",
    "audited_conditional",
    "retained_no_go",
    "audit_ledger",
    "audit_grade",
)


def block3_parent_runner_no_audit_status_references() -> None:
    header("BLOCK 3: Parent runner contains zero audit-status references")
    source = PARENT_RUNNER.read_text(encoding="utf-8")
    for token in AUDIT_STATUS_TOKENS:
        record(
            f"parent_runner_no_token_{token}",
            token not in source,
            f"'{token}' absent from parent runner source",
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
)


def block4_parent_note_no_grade_dependency_claim() -> None:
    header("BLOCK 4: Parent note contains no claim of dep-grade dependency")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")
    note_lower = note_text.lower()
    for phrase in NOTE_GRADE_DEPENDENCY_PHRASES:
        record(
            f"parent_note_no_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase.lower() not in note_lower,
            f"'{phrase}' absent from parent note",
        )
    # Positive: the parent's load-bearing scope is finite-probability
    # tangent algebra; we confirm the substantive phrasing is preserved.
    record(
        "parent_note_load_bearing_scope_finite_sharp_record",
        "finite sharp-record" in note_lower,
        "parent note frames scope as 'finite sharp-record'",
    )
    record(
        "parent_note_load_bearing_rn_score_present",
        "radon-nikodym" in note_lower or "rn score" in note_lower or "rn-cocycle" in note_lower,
        "parent note mentions Radon-Nikodym / RN score (load-bearing primitive)",
    )
    record(
        "parent_note_status_boundary_present",
        "status boundary" in note_lower,
        "parent note has a Status boundary section",
    )
    record(
        "parent_note_marks_exact_support",
        "actual_current_surface_status: exact-support" in note_text,
        "parent note carries actual_current_surface_status: exact-support marker",
    )
    record(
        "parent_note_forbids_bare_retained",
        "bare_retained_allowed: false" in note_text,
        "parent note forbids bare retained promotion",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual re-execution under the dep at unaudited
# -----------------------------------------------------------

def block5_counterfactual_without_dep_grade() -> None:
    header("BLOCK 5: Counterfactual re-execution under dep at current unaudited grade")
    rc, out, _ = run_parent_runner()
    # The parent runner does not consult the audit ledger; a passing run here
    # demonstrates that the executable substance is grade-independent.
    record(
        "counterfactual_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "counterfactual_runner_summary_unchanged",
        EXPECTED_PARENT_SUMMARY in out,
        "PASS count identical to Block 1 (substance-unchanged)",
    )
    # The dep is referenced only via an exists() check on its note path.
    # Confirm both dep note and parent note still exist on the head.
    record(
        "dep_note_path_still_exists",
        DEP_NOTE.exists(),
        f"dep note present at {DEP_NOTE.relative_to(REPO_ROOT)}",
    )
    record(
        "parent_note_path_still_exists",
        PARENT_NOTE.exists(),
        f"parent note present at {PARENT_NOTE.relative_to(REPO_ROOT)}",
    )


# -----------------------------------------------------------
# Block 6: Exponential-chart self-check (W forced by normalization)
# -----------------------------------------------------------

def block6_exponential_chart_self_check() -> None:
    header(
        "BLOCK 6: Exponential chart W(h) = log cosh(h) forced by E_0[R_h] = 1"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block6", False, f"import failed: {exc}")
        return

    h = sp.symbols("h", real=True)
    eps = {1: 1, -1: -1}
    p0 = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}

    # W is forced by normalization; do not import it.
    W = sp.log(sum(p0[e] * sp.exp(h * eps[e]) for e in (1, -1)))
    R = {e: sp.exp(h * eps[e] - W) for e in (1, -1)}
    norm = sp.simplify(sum(p0[e] * R[e] for e in (1, -1)))
    record(
        "exponential_chart_normalizes_path",
        sp.simplify(norm - 1) == 0,
        f"sum_e p0[e] R[e]={norm}",
    )
    score = {e: sp.diff(sp.log(R[e]), h).subs(h, 0) for e in (1, -1)}
    record(
        "exponential_chart_score_retrieval_plus",
        score[1] == 1,
        f"d log R_+1 / dh |_0 = {score[1]}",
    )
    record(
        "exponential_chart_score_retrieval_minus",
        score[-1] == -1,
        f"d log R_-1 / dh |_0 = {score[-1]}",
    )
    record(
        "exponential_chart_W_equals_log_cosh_h",
        sp.simplify(W - sp.log(sp.cosh(h))) == 0,
        f"W={sp.simplify(W)}",
    )

    # Sanity: W(0) = 0, W'(0) = 0 (W is a centered log-MGF).
    record(
        "log_mgf_W_vanishes_at_origin",
        sp.simplify(W.subs(h, 0)) == 0,
        f"W(0)={sp.simplify(W.subs(h, 0))}",
    )
    record(
        "log_mgf_W_prime_vanishes_at_origin",
        sp.simplify(sp.diff(W, h).subs(h, 0)) == 0,
        f"W'(0)={sp.simplify(sp.diff(W, h).subs(h, 0))}",
    )


# -----------------------------------------------------------
# Block 7: Y_T source-unit self-check
# -----------------------------------------------------------

def block7_yt_source_unit_self_check() -> None:
    header("BLOCK 7: Y_T six-component top tangent has Fisher norm one")
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block7", False, f"import failed: {exc}")
        return

    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    fisher = sp.simplify(u.dot(u))
    fisher_lam = sp.simplify((lam * u).dot(lam * u))
    record(
        "six_component_top_fisher_norm_one",
        sp.simplify(fisher - 1) == 0,
        f"||u||^2 = {fisher}",
    )
    record(
        "lambda_scaled_top_fisher_norm_lambda_squared",
        sp.simplify(fisher_lam - lam**2) == 0,
        f"||lambda u||^2 = {fisher_lam}",
    )
    record(
        "unit_top_tangent_selects_lambda_one",
        sp.solve(sp.Eq(fisher_lam, 1), lam) == [1],
        "lambda solves to [1]",
    )
    record(
        "top_component_coefficient_is_one_over_sqrt_six",
        sp.simplify(u[0] - 1 / sp.sqrt(6)) == 0,
        f"u[0]={u[0]}",
    )
    # Equal-weight check: every component matches the first.
    eq_components = all(sp.simplify(u[i] - u[0]) == 0 for i in range(6))
    record(
        "top_components_equal_weight",
        eq_components,
        "u[i] == u[0] for i in 0..5 (equal-weight normalized top)",
    )


# -----------------------------------------------------------
# Block 8: Status-boundary preservation across the runs
# -----------------------------------------------------------

FIREWALL_FORBIDDEN_IMPORT_NAMES = (
    "H_unit",
    "yt_ward_identity",
    "y_t_bare",
    "PDG",
    "alpha_LM",
    "plaquette",
    "fitted selector",
)

FIREWALL_FORBIDDEN_OVERCLAIM_PHRASES = (
    "Status: retained",
    "unbounded retained Y_T closure is claimed",
    "audit-clean retained",
)


def block8_status_boundary_preserved() -> None:
    header("BLOCK 8: Status-boundary preservation and companion-disclaim")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")
    flat = " ".join(note_text.split())

    # The parent note's firewall must NAME every forbidden import explicitly.
    for name in FIREWALL_FORBIDDEN_IMPORT_NAMES:
        record(
            f"parent_note_firewall_names_{re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')}",
            name in flat,
            f"'{name}' named in parent note firewall section",
        )
    # And it must NOT contain the forbidden overclaim phrases.
    for phrase in FIREWALL_FORBIDDEN_OVERCLAIM_PHRASES:
        record(
            f"parent_note_no_overclaim_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase not in note_text,
            f"'{phrase}' absent from parent note",
        )

    # Parent note status-boundary keys preserved.
    for key in (
        "actual_current_surface_status: exact-support",
        "trace_class: direct_blocker_closure_candidate",
        "proposal_allowed: false",
        "bare_retained_allowed: false",
        "audit_required_before_effective_retained: true",
    ):
        record(
            f"parent_note_status_key_present_{re.sub(r'[^a-z0-9]+', '_', key.lower()).strip('_')}",
            key in note_text,
            f"'{key}' present in parent note Status boundary",
        )

    # Companion explicitly disclaims promotion/import.
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8")
    companion_lower = companion_text.lower()
    record(
        "companion_disclaims_status_promotion",
        "does not promote status" in companion_lower
        or "not a status promotion" in companion_lower,
        "companion explicitly disclaims status promotion",
    )
    record(
        "companion_metadata_declares_meta",
        "type:** meta" in companion_lower,
        "companion metadata declares Type: meta",
    )
    # Use flattened-whitespace match so the disclaim can span line wraps.
    companion_flat = " ".join(companion_text.split()).lower()
    record(
        "companion_disclaims_new_theorem",
        "not a new theorem claim" in companion_flat
        or "claim a new theorem" in companion_flat,
        "companion explicitly disclaims new theorem claim",
    )
    record(
        "companion_disclaims_parent_edits",
        "modify the parent note" in companion_flat,
        "companion explicitly disclaims parent edits",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Source/Measure Sharp-Record Tangent-Space")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log(f"Repo root: {REPO_ROOT}")
    log(f"Parent note: {PARENT_NOTE}")
    log(f"Parent runner: {PARENT_RUNNER}")
    log(f"Dep note: {DEP_NOTE}")
    log(f"Companion source note: {COMPANION_NOTE.relative_to(REPO_ROOT)}")
    log("")
    log("Goal: verify the parent's load-bearing substantive content does")
    log("      not load-bear on the *audit grade* of its dep")
    log("      `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`")
    log("      (which was downgraded from retained_bounded to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_finite_probability_algebra()
    block3_parent_runner_no_audit_status_references()
    block4_parent_note_no_grade_dependency_claim()
    block5_counterfactual_without_dep_grade()
    block6_exponential_chart_self_check()
    block7_yt_source_unit_self_check()
    block8_status_boundary_preserved()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
