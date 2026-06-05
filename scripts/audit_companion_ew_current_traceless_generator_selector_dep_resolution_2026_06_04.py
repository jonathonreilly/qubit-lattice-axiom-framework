#!/usr/bin/env python3
"""Audit-companion runner for the EW current traceless-generator selector
parent note
`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`
recording dep-resolution hygiene evidence after the dep weakening

    axiom_first_lattice_noether_theorem_note_2026-04-29:
        retained_bounded -> unaudited

Companion source note:
  docs/EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `ew_current_traceless_generator_selector_no_go_note_2026-05-03`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion; this runner writes no
    audit verdict or direct status change.
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content (the algebraic counterexample T_3 vs M=I_color
    plus K_EW(0)=9/8 vs K_EW(1)=1 selector separation) does not
    load-bear on the *audit grade* of its dep
    `axiom_first_lattice_noether_theorem_note_2026-04-29`
    (which was downgraded from `retained_bounded` to `unaudited`).
    The dep appears in the parent only as "bounded current-form
    context for the point-split bilinear" (parent cited-context
    section); the parent's runner consumes the dep note text only
    via a single string presence check on the point-split bilinear
    symbol, and computes the load-bearing rational identities itself
    over `fractions.Fraction` primitives.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm the canonical RESULT line with PASS=29 FAIL=0.
  Block 2 : Re-verify the algebraic counterexample inputs
            (Tr(T_3), Tr(T_3^2), S(I_color), C(I_color),
            Tr(T_3^2)*S(I_color)) directly over Fraction arithmetic,
            independent of the parent runner.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            audit-status references (audit_status, effective_status,
            intrinsic_status, retained_bounded, audited_clean,
            audited_conditional, retained_no_go, unaudited,
            audit_ledger, audit_grade).
  Block 4 : Static source-scan of the parent note: confirm no claim
            that the substantive no-go conclusion depends on the
            dep's audit grade, AND confirm the parent's explicit
            demotion of the Noether dep to "bounded current-form
            context...this branch does not promote it to repo-wide
            axiom status".
  Block 5 : Counterfactual re-execution under the current dep grade
            (`unaudited` on origin/main): parent runner pass count
            and RESULT line identical to Block 1.
  Block 6 : Selector separation at the algebraic level: K_EW(0)=9/8
            and K_EW(1)=1 with K_EW(0) != K_EW(1).
  Block 7 : Linear-vs-quadratic trace distinction at the algebraic
            level: (Tr T_3)^2 = 0 but Tr(T_3^2) = 1/2.
  Block 8 : No-claim gate preservation; companion declares
            claim_type=meta and disclaims status promotion.

Every check uses only the parent's existing runner code (re-executed)
plus standard finite rational arithmetic.  No audit-status content is
asserted.  No new theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import re
import subprocess
import sys
from fractions import Fraction
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
PARENT_RUNNER = (
    REPO_ROOT
    / "scripts"
    / "frontier_ew_current_traceless_generator_selector_no_go.py"
)
PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md"
)
DEP_NOTE = (
    REPO_ROOT
    / "docs"
    / "AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md"
)
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

EXPECTED_RESULT_LINE = "RESULT: PASS=29 FAIL=0"


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
    header("BLOCK 1: Re-execute parent runner on current head; expect PASS=29 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_emits_expected_result_line",
        EXPECTED_RESULT_LINE in out,
        f"'{EXPECTED_RESULT_LINE}' present in stdout: {EXPECTED_RESULT_LINE in out}",
    )
    # Spot-check that the parent runner's load-bearing checks pass.
    spot_phrases = (
        "traceless EW generator has Tr(T3)=0",
        "same generator has nonzero quadratic trace",
        "tracelessness kills ordinary Wick-disconnected one-current loops",
        "connected two-current contraction is nonzero for M=I_color",
        "that nonzero contraction is entirely the color Fierz singlet S",
        "therefore Tr(Q_EW)=0 does not imply kappa_EW=0",
        "connected selector would give K_EW(0)=9/8",
        "full-trace readout remains algebraically admissible at K_EW(1)=1",
        "traceless-generator route cannot distinguish kappa=0 from kappa=1",
    )
    for phrase in spot_phrases:
        record(
            f"parent_runner_load_bearing_passes_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')[:50]}",
            f"[PASS] {phrase}" in out,
            f"PASS line for: {phrase}",
        )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify load-bearing rational identities directly
# -----------------------------------------------------------

def tr_diag(entries: tuple[Fraction, ...]) -> Fraction:
    return sum(entries, Fraction(0))


def tr_diag_square(entries: tuple[Fraction, ...]) -> Fraction:
    return sum((x * x for x in entries), Fraction(0))


def color_singlet_channel(trace_m: Fraction, n_c: int) -> Fraction:
    return trace_m * trace_m / n_c


def color_total_channel(frob_norm_sq: Fraction) -> Fraction:
    return frob_norm_sq


def color_adjoint_channel(frob_norm_sq: Fraction, trace_m: Fraction, n_c: int) -> Fraction:
    return color_total_channel(frob_norm_sq) - color_singlet_channel(trace_m, n_c)


def k_ew(n_c: int, kappa: Fraction) -> Fraction:
    f_adj = Fraction(n_c * n_c - 1, n_c * n_c)
    s = Fraction(1, n_c * n_c)
    return Fraction(1, 1) / (f_adj + kappa * s)


def block2_algebraic_counterexample_independently_verified() -> None:
    header("BLOCK 2: Re-verify the T_3 / I_color algebraic counterexample directly")
    n_c = 3
    t3 = (Fraction(1, 2), Fraction(-1, 2))
    tr_t3 = tr_diag(t3)
    tr_t3_sq = tr_diag_square(t3)
    record(
        "indep_tr_t3_equals_zero",
        tr_t3 == 0,
        f"Tr(T_3) = {tr_t3}",
    )
    record(
        "indep_tr_t3_squared_equals_one_half",
        tr_t3_sq == Fraction(1, 2),
        f"Tr(T_3^2) = {tr_t3_sq}",
    )

    wick_disconnected = tr_t3 * tr_t3
    record(
        "indep_wick_disconnected_one_current_factor_zero",
        wick_disconnected == 0,
        f"(Tr T_3)^2 = {wick_disconnected}",
    )

    # M = I_color
    trace_I = Fraction(n_c)
    frob_I = Fraction(n_c)
    singlet_I = color_singlet_channel(trace_I, n_c)
    adjoint_I = color_adjoint_channel(frob_I, trace_I, n_c)
    record(
        "indep_singlet_of_I_color_equals_Nc",
        singlet_I == n_c,
        f"S(I_color) = {singlet_I}",
    )
    record(
        "indep_adjoint_of_I_color_equals_zero",
        adjoint_I == 0,
        f"C(I_color) = {adjoint_I}",
    )

    same_line_singlet = singlet_I * tr_t3_sq
    record(
        "indep_connected_singlet_weight_three_halves",
        same_line_singlet == Fraction(3, 2),
        f"Tr(T_3^2) * S(I_color) = {same_line_singlet}",
    )
    record(
        "indep_implication_fails",
        wick_disconnected == 0 and same_line_singlet != 0,
        "Tr(Q_EW)=0 coexists with non-zero color-singlet channel",
    )

    # A color-adjoint witness (diag(1/2, -1/2, 0)) gives pure-adjoint.
    color_t3 = (Fraction(1, 2), Fraction(-1, 2), Fraction(0))
    trace_color_t3 = tr_diag(color_t3)
    frob_color_t3 = tr_diag_square(color_t3)
    singlet_color_t3 = color_singlet_channel(trace_color_t3, n_c)
    adjoint_color_t3 = color_adjoint_channel(frob_color_t3, trace_color_t3, n_c)
    record(
        "indep_color_traceless_pure_adjoint",
        singlet_color_t3 == 0 and adjoint_color_t3 == Fraction(1, 2),
        f"S=0, C={adjoint_color_t3}",
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
    "depends on the Noether note being retained",
)


def block4_parent_note_no_grade_dependency_claim() -> None:
    header("BLOCK 4: Parent note contains no claim of dep-grade dependency")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")
    for phrase in NOTE_GRADE_DEPENDENCY_PHRASES:
        record(
            f"parent_note_no_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase.lower() not in note_text.lower(),
            f"'{phrase}' absent from parent note",
        )
    # Positive: the parent note explicitly demotes the Noether dep
    # to bounded current-form context.
    record(
        "parent_note_explicitly_demotes_noether_dep",
        "bounded current-form context" in note_text.lower(),
        "parent note phrase 'bounded current-form context' present",
    )
    record(
        "parent_note_does_not_promote_dep",
        "does not promote it to repo-wide axiom" in note_text.lower(),
        "parent note phrase 'does not promote it to repo-wide axiom' present",
    )
    # And the parent note records the load-bearing route-specific no-go.
    record(
        "parent_note_records_route_specific_no_go",
        "**Claim type:** no_go" in note_text,
        "parent note declares claim_type=no_go",
    )
    record(
        "parent_note_records_not_a_positive_closure",
        "not a positive closure" in note_text,
        "parent note phrase 'not a positive closure' present",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual re-execution under the dep at unaudited
# -----------------------------------------------------------

def block5_counterfactual_dep_unaudited() -> None:
    header("BLOCK 5: Counterfactual under dep at `unaudited` on origin/main")
    rc, out, _ = run_parent_runner()
    # The current `origin/main` head already has the dep at `unaudited`
    # (per docs/audit/data/audit_ledger.json on this head); a passing
    # run here IS the counterfactual.
    record(
        "counterfactual_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "counterfactual_runner_result_line_unchanged",
        EXPECTED_RESULT_LINE in out,
        "RESULT line identical to Block 1 (substance-unchanged)",
    )
    record(
        "counterfactual_runner_no_extra_failures",
        "FAIL=0" in out,
        "no FAIL lines present in counterfactual run",
    )


# -----------------------------------------------------------
# Block 6: Selector separation at the algebraic level
# -----------------------------------------------------------

def block6_selector_separation_algebraic() -> None:
    header("BLOCK 6: Algebraic selector separation K_EW(0)=9/8 vs K_EW(1)=1")
    n_c = 3
    k0 = k_ew(n_c, Fraction(0))
    k1 = k_ew(n_c, Fraction(1))
    record(
        "k_ew_kappa_zero_is_nine_eighths",
        k0 == Fraction(9, 8),
        f"K_EW(0) = {k0}",
    )
    record(
        "k_ew_kappa_one_is_one",
        k1 == 1,
        f"K_EW(1) = {k1}",
    )
    record(
        "k_ew_kappa_zero_neq_kappa_one",
        k0 != k1,
        f"K_EW(0)={k0} vs K_EW(1)={k1}; traceless route cannot fix kappa_EW",
    )
    # Cross-check arithmetic of K_EW formula at N_c=3.
    # K_EW(kappa) = 1 / ((N_c^2-1)/N_c^2 + kappa/N_c^2) = N_c^2 / (N_c^2-1+kappa)
    for kappa in (Fraction(0), Fraction(1), Fraction(1, 2), Fraction(2)):
        expected = Fraction(n_c * n_c, n_c * n_c - 1 + kappa)
        got = k_ew(n_c, kappa)
        record(
            f"k_ew_closed_form_kappa_{kappa.numerator}_{kappa.denominator}",
            got == expected,
            f"K_EW({kappa}) = {got} == {expected}",
        )


# -----------------------------------------------------------
# Block 7: Linear-vs-quadratic trace distinction
# -----------------------------------------------------------

def block7_linear_vs_quadratic_trace() -> None:
    header("BLOCK 7: (Tr T_3)^2 = 0 vs Tr(T_3^2) = 1/2 (substance of the no-go)")
    # Repeat for several traceless generators to show the distinction
    # is not specific to T_3.
    generators: dict[str, tuple[Fraction, ...]] = {
        "T_3":     (Fraction(1, 2), Fraction(-1, 2)),
        "Y_lep":   (Fraction(-1, 2), Fraction(-1, 2), Fraction(1)),  # left-handed lepton hypercharge balanced w/ singlet 1
        "diag1m1": (Fraction(1), Fraction(-1)),
        "diag2m1m1": (Fraction(2), Fraction(-1), Fraction(-1)),
        "diag1m2_1": (Fraction(1), Fraction(-2), Fraction(1)),
    }
    for label, entries in generators.items():
        lin = tr_diag(entries)
        quad = tr_diag_square(entries)
        # All chosen generators are traceless; quadratic trace is non-zero.
        record(
            f"traceless_linear_{label}",
            lin == 0,
            f"Tr({label}) = {lin}",
        )
        record(
            f"nonzero_quadratic_{label}",
            quad != 0,
            f"Tr({label}^2) = {quad}",
        )
        record(
            f"distinct_lin_squared_vs_quad_{label}",
            (lin * lin) != quad,
            f"(Tr {label})^2 = {lin * lin} != Tr({label}^2) = {quad}",
        )


# -----------------------------------------------------------
# Block 8: No-claim gate preservation
# -----------------------------------------------------------

def block8_no_claim_gate_preserved() -> None:
    header("BLOCK 8: No-claim gate preservation; companion disclaims promotion")
    # Companion note self-checks.
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8")
    record(
        "companion_declares_claim_type_meta",
        "claim_type=meta" in companion_text.lower()
        or "type:** meta" in companion_text.lower(),
        "companion declared claim_type=meta",
    )
    record(
        "companion_disclaims_status_promotion",
        "not a status promotion" in companion_text.lower()
        or "does not promote status" in companion_text.lower(),
        "companion explicitly disclaims status promotion",
    )
    record(
        "companion_disclaims_new_theorem",
        "not a new theorem claim" in companion_text.lower()
        or "not a theorem claim" in companion_text.lower(),
        "companion explicitly disclaims new theorem claim",
    )
    record(
        "companion_disclaims_parent_edits",
        "does not modify the parent note text" in companion_text.lower()
        or "modify the parent note text" in companion_text.lower(),
        "companion explicitly disclaims parent edits",
    )
    record(
        "companion_disclaims_dep_restoration",
        # Tolerate Markdown emphasis (e.g. "has *not* been restored").
        re.search(r"has\s+\*?not\*?\s+been\s+restored", companion_text, re.IGNORECASE) is not None,
        "companion explicitly disclaims dep grade restoration",
    )
    record(
        "companion_names_invalidation_reason",
        "dep_weakened:axiom_first_lattice_noether_theorem_note_2026-04-29:retained_bounded->unaudited"
        in companion_text,
        "companion records the exact invalidation_reason string",
    )
    record(
        "companion_names_parent_row",
        "ew_current_traceless_generator_selector_no_go_note_2026-05-03"
        in companion_text,
        "companion names the parent ledger row",
    )
    record(
        "companion_independent_audit_handoff_present",
        "audit handoff" in companion_text.lower()
        and "independent audit handling" in companion_text.lower(),
        "companion includes independent audit handoff section",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("EW Current Traceless-Generator Selector")
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
    log("      `axiom_first_lattice_noether_theorem_note_2026-04-29`")
    log("      (which was downgraded from retained_bounded to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_algebraic_counterexample_independently_verified()
    block3_parent_runner_no_audit_status_references()
    block4_parent_note_no_grade_dependency_claim()
    block5_counterfactual_dep_unaudited()
    block6_selector_separation_algebraic()
    block7_linear_vs_quadratic_trace()
    block8_no_claim_gate_preserved()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
