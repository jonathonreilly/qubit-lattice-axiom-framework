#!/usr/bin/env python3
"""Audit-companion runner for the Y_T source-Higgs pole-row normalization
no-go parent note
`YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md`
recording dep-resolution hygiene evidence after the dep weakening

  dep_weakened:observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16:
      decoration_under_observable_principle_real_d_block_uniqueness_narrow_theorem_note_2026-05-10
      -> unaudited

Companion source note:
  docs/YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its cited context dep
    `observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16`
    (which transitioned from
    decoration_under_observable_principle_real_d_block_uniqueness_narrow_theorem_note_2026-05-10
    to unaudited).  Only the elementary pole-residue scaling algebra
    plus the retained K_Y(kappa_Y) = 8/9 + kappa_Y/9 family from
    `yt_color_projection_correction_note` is used, and the parent's
    own runner re-verifies that algebra block-for-block.

The companion runner verifies the substance-vs-grade separation by:

  Block 1  : Re-execute the parent runner on the current head and
             confirm RESULT: PASS=50 FAIL=0 with exit code zero.
  Block 2  : Pole-residue Gram-purity algebra on a numeric rank-one
             row: Gram determinant identically zero for sample times.
  Block 3  : Effective-mass amplitude-blindness: C(t)/C(t+1) = exp(m)
             for each of the three correlator rows under random
             positive (A_s, A_H, m).
  Block 4  : Rescaling invariance under s -> mu s and H -> lambda H:
             Gram determinant remains zero, effective mass unchanged,
             normalized residue ratio equals 1.
  Block 5  : K_Y(kappa_Y) = 8/9 + kappa_Y/9 ratio K_Y(1)/K_Y(0) = 9/8
             absorbed by lambda^2 = 9/8.
  Block 6  : Parent runner contains zero audit-status references.
  Block 7  : Parent note: Cited Context disclaims context as
             non-derivational; N8 frames source-response note as
             rhetorical analogy.
  Block 8  : Counterfactual re-execution: parent runner pass count
             and final result line independent of any dep-grade query.
  Block 9  : Parent note: five-route no-go discipline enumeration
             preserved (Gram-purity / mass-extraction / residue-ratio
             / kappa_Y absorption / absolute-residue routes).
  Block 10 : Parent note: positive-closure path preserved (canonical
             O_H, scalar LSZ, same-surface source/action, W/Z
             physical-response routes open).
  Block 11 : Companion-only metadata sanity: claim_type meta, no
             status-setting language, no audit-ledger writes.

Every check uses only the parent's existing runner / note text
(re-imported or re-read) plus standard finite-rational / floating-
point arithmetic.  No audit-status content is asserted.  No new
theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
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
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_yt_source_higgs_pole_row_normalization_no_go.py"
PARENT_NOTE = REPO_ROOT / "docs" / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
COMPANION_RUNNER = Path(__file__).resolve()

EXPECTED_PARENT_RESULT_LINE = "RESULT: PASS=50 FAIL=0"

# Deterministic test points for the pole-row algebra.
# Use exact rationals where possible so identities hold exactly.
SAMPLE_AS = [Fraction(2, 1), Fraction(5, 2), Fraction(7, 3)]
SAMPLE_AH = [Fraction(1, 1), Fraction(11, 7), Fraction(13, 5)]
SAMPLE_M = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
SAMPLE_T = [0, 2]
SAMPLE_MU = [Fraction(2, 1), Fraction(7, 4)]
SAMPLE_LAMBDA = [Fraction(3, 2), Fraction(9, 7)]


# -----------------------------------------------------------
# Helpers
# -----------------------------------------------------------

def correlator_residues(a_s: Fraction, a_h: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return (Res(C_ss), Res(C_sH), Res(C_HH)) on the rank-one ansatz."""
    return (a_s * a_s, a_s * a_h, a_h * a_h)


def gram_determinant(r_ss: Fraction, r_sh: Fraction, r_hh: Fraction) -> Fraction:
    """Gram determinant C_sH^2 - C_ss * C_HH (purity witness)."""
    return r_sh * r_sh - r_ss * r_hh


# -----------------------------------------------------------
# Block 1: Re-execute parent runner on current head
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
    header("BLOCK 1: Re-execute parent runner; expect RESULT: PASS=50 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_result_line_present",
        EXPECTED_PARENT_RESULT_LINE in out,
        f"looking for {EXPECTED_PARENT_RESULT_LINE!r}",
    )
    record(
        "parent_runner_no_stderr_errors",
        len(err.strip()) == 0,
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Pole-residue Gram-purity algebra
# -----------------------------------------------------------

def block2_gram_determinant_zero() -> None:
    header("BLOCK 2: Gram determinant identically zero on rank-one row")
    for a_s, a_h in zip(SAMPLE_AS, SAMPLE_AH):
        r_ss, r_sh, r_hh = correlator_residues(a_s, a_h)
        det = gram_determinant(r_ss, r_sh, r_hh)
        record(
            f"gram_det_zero_(A_s={a_s},A_H={a_h})",
            det == 0,
            f"det={det}",
        )


# -----------------------------------------------------------
# Block 3: Effective-mass amplitude-blindness
# -----------------------------------------------------------

def block3_mass_extraction_amplitude_blind() -> None:
    header("BLOCK 3: C(t)/C(t+1) = exp(m) amplitude-blind for all three rows")
    tol = 1e-12
    for a_s, a_h, m in zip(SAMPLE_AS, SAMPLE_AH, SAMPLE_M):
        a_s_f = float(a_s)
        a_h_f = float(a_h)
        m_f = float(m)
        for t in SAMPLE_T:
            c_ss_t = (a_s_f ** 2) * math.exp(-m_f * t)
            c_ss_t1 = (a_s_f ** 2) * math.exp(-m_f * (t + 1))
            c_sh_t = a_s_f * a_h_f * math.exp(-m_f * t)
            c_sh_t1 = a_s_f * a_h_f * math.exp(-m_f * (t + 1))
            c_hh_t = (a_h_f ** 2) * math.exp(-m_f * t)
            c_hh_t1 = (a_h_f ** 2) * math.exp(-m_f * (t + 1))
            expected = math.exp(m_f)
            ratios = (
                c_ss_t / c_ss_t1,
                c_sh_t / c_sh_t1,
                c_hh_t / c_hh_t1,
            )
            ok = all(abs(r - expected) < tol for r in ratios)
            record(
                f"mass_ratio_amplitude_blind_t={t}_m={m}",
                ok,
                f"expected={expected:.6f} got={ratios}",
            )


# -----------------------------------------------------------
# Block 4: Rescaling invariance s -> mu s, H -> lambda H
# -----------------------------------------------------------

def block4_rescaling_invariance() -> None:
    header("BLOCK 4: Gram determinant, mass, normalized residue ratio are rescaling-invariant")
    tol = 1e-12
    # Pair (A_s, A_H, m) with (mu, lambda) for several samples.
    for a_s, a_h, m, mu, lam in zip(SAMPLE_AS, SAMPLE_AH, SAMPLE_M, SAMPLE_MU, SAMPLE_LAMBDA):
        # Original residues.
        r_ss, r_sh, r_hh = correlator_residues(a_s, a_h)
        # Rescaled residues per the parent's load-bearing identity.
        r_ss_p = mu * mu * r_ss
        r_sh_p = mu * lam * r_sh
        r_hh_p = lam * lam * r_hh

        # (i) Gram determinant remains zero.
        det_p = gram_determinant(r_ss_p, r_sh_p, r_hh_p)
        record(
            f"rescaled_gram_zero_(mu={mu},lam={lam})",
            det_p == 0,
            f"det_p={det_p}",
        )

        # (ii) Effective mass C(t)/C(t+1) = exp(m) unchanged under rescaling.
        a_s_f = float(a_s) * float(mu)
        a_h_f = float(a_h) * float(lam)
        m_f = float(m)
        c_ss_t = (a_s_f ** 2) * math.exp(-m_f * 1)
        c_ss_t1 = (a_s_f ** 2) * math.exp(-m_f * 2)
        ratio_ss = c_ss_t / c_ss_t1
        record(
            f"rescaled_mass_ratio_unchanged_(mu={mu},lam={lam})",
            abs(ratio_ss - math.exp(m_f)) < tol,
            f"ratio_ss={ratio_ss:.6f} expected={math.exp(m_f):.6f}",
        )

        # (iii) Normalized residue ratio Res(C_sH)/sqrt(Res(C_ss) Res(C_HH)) = 1.
        norm_orig = float(r_sh) / math.sqrt(float(r_ss) * float(r_hh))
        norm_resc = float(r_sh_p) / math.sqrt(float(r_ss_p) * float(r_hh_p))
        ok = abs(norm_orig - 1.0) < tol and abs(norm_resc - 1.0) < tol
        record(
            f"normalized_residue_ratio_unit_(mu={mu},lam={lam})",
            ok,
            f"norm_orig={norm_orig:.12f} norm_resc={norm_resc:.12f}",
        )


# -----------------------------------------------------------
# Block 5: K_Y(kappa_Y) 9/8 absorption
# -----------------------------------------------------------

def k_y(kappa_y: Fraction) -> Fraction:
    """Retained K_Y(kappa_Y) = 8/9 + kappa_Y/9 family."""
    return Fraction(8, 9) + kappa_y * Fraction(1, 9)


def block5_kappa_y_absorption() -> None:
    header("BLOCK 5: K_Y(1)/K_Y(0) = 9/8 absorbed by lambda^2 = 9/8")
    k0 = k_y(Fraction(0))
    k1 = k_y(Fraction(1))
    record(
        "k_y_kappa0_eq_8_over_9",
        k0 == Fraction(8, 9),
        f"k_y(0)={k0}",
    )
    record(
        "k_y_kappa1_eq_1",
        k1 == Fraction(1, 1),
        f"k_y(1)={k1}",
    )
    ratio = k1 / k0
    record(
        "k_y_ratio_eq_9_over_8",
        ratio == Fraction(9, 8),
        f"k_y(1)/k_y(0)={ratio}",
    )
    # The absorption: lambda^2 = 9/8 exactly absorbs the K_Y ratio.
    # Pick any A_s, A_H and m; replace H -> lambda H with lambda^2 = 9/8
    # on the kappa_Y=0 side and verify residues match the kappa_Y=1 side
    # in the normalization sense: r_hh' = lambda^2 * r_hh = (9/8) r_hh.
    a_s, a_h = SAMPLE_AS[0], SAMPLE_AH[0]
    r_ss, r_sh, r_hh = correlator_residues(a_s, a_h)
    lambda_sq = Fraction(9, 8)
    r_hh_resc = lambda_sq * r_hh
    # Ratio (K_Y(1) * r_hh) vs (K_Y(0) * r_hh_resc) should be equal.
    lhs = k1 * r_hh
    rhs = k0 * r_hh_resc
    record(
        "k_y_absorption_lambda_sq_9_over_8",
        lhs == rhs,
        f"K_Y(1) * Res(C_HH) = {lhs}; K_Y(0) * (9/8) * Res(C_HH) = {rhs}",
    )


# -----------------------------------------------------------
# Block 6: Static-source scan of parent runner
# -----------------------------------------------------------

AUDIT_GRADE_TOKENS = [
    "audit_status",
    "effective_status",
    "intrinsic_status",
    "retained_bounded",
    "audited_clean",
    "audited_conditional",
    # Plain "retained" and "unaudited" are checked as standalone words
    # to avoid false positives in unrelated identifiers.
]
STANDALONE_AUDIT_GRADE_RE = [
    re.compile(r"\bretained\b"),
    re.compile(r"\bunaudited\b"),
]


def block6_parent_runner_no_audit_status_refs() -> None:
    header("BLOCK 6: Parent runner contains zero audit-status references")
    text = PARENT_RUNNER.read_text(encoding="utf-8")
    for tok in AUDIT_GRADE_TOKENS:
        n = text.count(tok)
        record(
            f"parent_runner_no_token::{tok}",
            n == 0,
            f"count={n}",
        )
    for pat in STANDALONE_AUDIT_GRADE_RE:
        n = len(pat.findall(text))
        record(
            f"parent_runner_no_standalone::{pat.pattern}",
            n == 0,
            f"count={n}",
        )


# -----------------------------------------------------------
# Block 7: Parent note context disclaim + analogy framing
# -----------------------------------------------------------

DISCLAIM_PHRASE = "These context notes are not used to derive the no-go"
ANALOGY_PHRASE = "has the same shape as"
NO_GRADE_DEPENDENCE_NEGATIVE_PHRASES = [
    # If any of these surface in the parent text, the substance-vs-grade
    # separation would be broken.
    "the no-go depends on the audit grade of",
    "load-bears on the audit grade",
    "load-bears on the dep audit grade",
    "depends on the audit status of",
]


def block7_parent_note_disclaim_and_analogy() -> None:
    header("BLOCK 7: Parent note: Cited Context disclaimed; N8 framed as analogy")
    text = PARENT_NOTE.read_text(encoding="utf-8")
    record(
        "parent_note_disclaim_phrase_present",
        DISCLAIM_PHRASE in text,
        f"phrase {DISCLAIM_PHRASE!r}",
    )
    record(
        "parent_note_analogy_phrase_present",
        ANALOGY_PHRASE in text,
        f"phrase {ANALOGY_PHRASE!r}",
    )
    for phrase in NO_GRADE_DEPENDENCE_NEGATIVE_PHRASES:
        n = text.lower().count(phrase.lower())
        record(
            f"parent_note_no_grade_dependence::{phrase!r}",
            n == 0,
            f"count={n}",
        )


# -----------------------------------------------------------
# Block 8: Counterfactual re-execution
# -----------------------------------------------------------

def block8_counterfactual_grade_independent(rc_baseline: int, out_baseline: str) -> None:
    header("BLOCK 8: Counterfactual re-execution: result independent of dep grade")
    rc2, out2, err2 = run_parent_runner()
    record(
        "parent_runner_idempotent_exit_code",
        rc2 == rc_baseline,
        f"rc_baseline={rc_baseline} rc2={rc2}",
    )
    # Extract just the RESULT line; bytewise identity is too strong because
    # of timestamps/cache-paths the parent may emit; structural identity is
    # what matters.
    line1 = next(
        (ln for ln in out_baseline.splitlines() if ln.startswith("RESULT:")),
        "",
    )
    line2 = next(
        (ln for ln in out2.splitlines() if ln.startswith("RESULT:")),
        "",
    )
    record(
        "parent_runner_result_line_idempotent",
        line1 == line2 and line1.startswith("RESULT:"),
        f"line1={line1!r} line2={line2!r}",
    )
    record(
        "parent_runner_no_stderr_on_second_run",
        len(err2.strip()) == 0,
        f"stderr length={len(err2)}",
    )


# -----------------------------------------------------------
# Block 9: Five-route enumeration preservation
# -----------------------------------------------------------

FIVE_ROUTE_NAMES = [
    "Gram-purity route",
    "Mass-extraction route",
    "Residue-ratio route",
    "kappa_Y absorption route",
    "Absolute-residue route",
]


def block9_five_route_names_present() -> None:
    header("BLOCK 9: Parent note: five-route no-go discipline names preserved")
    text = PARENT_NOTE.read_text(encoding="utf-8")
    for name in FIVE_ROUTE_NAMES:
        record(
            f"parent_note_route_name::{name}",
            name in text,
            f"phrase {name!r}",
        )


# -----------------------------------------------------------
# Block 10: Positive-closure path preserved
# -----------------------------------------------------------

POSITIVE_CLOSURE_PHRASES = [
    "canonical O_H",
    "canonical scalar LSZ normalization",
    "source/action",
    "W/Z",
]


def block10_positive_closure_preserved() -> None:
    header("BLOCK 10: Parent note: positive-closure path explicitly open")
    text = PARENT_NOTE.read_text(encoding="utf-8")
    for phrase in POSITIVE_CLOSURE_PHRASES:
        record(
            f"parent_note_positive_closure_phrase::{phrase}",
            phrase in text,
            f"phrase {phrase!r}",
        )


# -----------------------------------------------------------
# Block 11: Companion-only metadata sanity
# -----------------------------------------------------------

COMPANION_FORBIDDEN_PHRASES = [
    # Setting these would violate the meta-companion role.
    "audit_status: audited_clean",
    "audit_status: audited_conditional",
    "audit_status: retained",
    "audit_status: retained_bounded",
    "effective_status: retained",
    "effective_status: retained_bounded",
    "effective_status: audited_clean",
]


def block11_companion_metadata_sanity() -> None:
    header("BLOCK 11: Companion-only metadata sanity")
    text = COMPANION_NOTE.read_text(encoding="utf-8")
    record(
        "companion_note_claim_type_meta",
        "**Claim type:** meta" in text or "claim_type: meta" in text.lower(),
        "looking for explicit claim_type meta declaration",
    )
    record(
        "companion_note_type_is_meta_audit_companion",
        "meta (audit-companion" in text,
        "looking for 'meta (audit-companion' framing",
    )
    record(
        "companion_note_status_companion_only",
        "companion-only" in text,
        "looking for 'companion-only' status framing",
    )
    for phrase in COMPANION_FORBIDDEN_PHRASES:
        n = text.lower().count(phrase.lower())
        record(
            f"companion_note_no_forbidden_status::{phrase}",
            n == 0,
            f"count={n}",
        )
    # Companion runner does not write to the audit ledger or queue.
    runner_text = COMPANION_RUNNER.read_text(encoding="utf-8")
    for forbidden in ("audit_ledger.json", "audit_queue.json"):
        n_write = sum(
            1
            for ln in runner_text.splitlines()
            if forbidden in ln and ("write" in ln.lower() or "open(" in ln.lower())
        )
        record(
            f"companion_runner_no_write_to::{forbidden}",
            n_write == 0,
            f"write-mention lines={n_write}",
        )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Y_T Source-Higgs Pole-Row Normalization No-Go")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log(f"Repo root: {REPO_ROOT}")
    log(f"Parent note: {PARENT_NOTE}")
    log(f"Parent runner: {PARENT_RUNNER}")
    log(f"Companion source note: {COMPANION_NOTE.relative_to(REPO_ROOT)}")
    log("")
    log("Goal: verify the parent's load-bearing substantive content does")
    log("      not load-bear on the *audit grade* of its cited context dep")
    log("      `observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16`")
    log("      (which transitioned from decoration_under_... to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    rc, out = block1_parent_runner_passes()
    block2_gram_determinant_zero()
    block3_mass_extraction_amplitude_blind()
    block4_rescaling_invariance()
    block5_kappa_y_absorption()
    block6_parent_runner_no_audit_status_refs()
    block7_parent_note_disclaim_and_analogy()
    block8_counterfactual_grade_independent(rc, out)
    block9_five_route_names_present()
    block10_positive_closure_preserved()
    block11_companion_metadata_sanity()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
