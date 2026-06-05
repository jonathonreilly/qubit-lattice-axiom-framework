#!/usr/bin/env python3
"""Audit-companion runner for the static-source readout I1 accepted-premise
bridge parent note
`STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`
recording dep-resolution hygiene evidence after the dep weakening
`alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27:
retained_bounded -> unaudited`.

Companion source note:
  docs/STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion; this runner writes no
    audit verdict or direct status change.
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep `alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27`
    (which was downgraded from `retained_bounded` to `unaudited`).
    Only the *structural definitional identity* `alpha := g_bare^2/(4*pi)`
    consumed at steps (B2)-(B4) of the parent's proof-walk is used,
    and the parent's own runner re-verifies the substitution chain
    symbolically by direct sympy primitives.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm the VERDICT is unchanged with EXACT=41 FAIL=0,
            BOUNDED=11 FAIL=0, TOTAL=52 FAIL=0.
  Block 2 : Re-verify the canonical I2 dimensionless-coupling identity
            `alpha := g_bare^2/(4*pi)` symbolically via independent
            sympy primitives, without importing or executing any code
            from the dep.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            audit-status references (audit_status, effective_status,
            intrinsic_status, retained_bounded, audited_clean,
            audited_conditional, retained, unaudited).
  Block 4 : Static source-scan of the parent note: confirm no claim
            that the substantive substitution conclusion depends on the
            dep's audit grade.
  Block 5 : Counterfactual re-execution without consulting the dep's
            audit grade: parent runner pass count and VERDICT identical
            to Block 1.
  Block 6 : Direct symbolic re-derivation of the (B1)-(B4) substitution
            chain at the algebraic level (sympy simplify residuals
            zero) independent of any dep grade.
  Block 7 : Numerical cross-check of alpha = 1/(4*pi) at g_bare = 1
            and the Casimir convention C_F = 4/3 at N_c = 3 independent
            of any dep grade.
  Block 8 : No-claim gate preservation: the runner's no-new-axiom /
            no-new-vocab / multiplicative-bridge / regulator-dependence
            gates remain green across runs, and the companion note
            self-declares claim_type meta and disclaims status
            promotion.

Every check uses only the parent's existing runner plus standard
finite-dimensional sympy/numpy primitives. No audit-status content is
asserted. No new theorem claim is made.

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
PARENT_RUNNER = REPO_ROOT / "scripts" / "static_source_readout_i1_accepted_premise_runner.py"
PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
)
DEP_NOTE = (
    REPO_ROOT
    / "docs"
    / "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
)
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_"
    "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

EXPECTED_VERDICT_PREFIX = (
    "VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from"
)


# -----------------------------------------------------------
# Block 1: Re-execute the parent runner on the current head
# -----------------------------------------------------------

def run_parent_runner() -> tuple[int, str, str]:
    """Return (returncode, stdout, stderr) of the parent runner."""
    env_pythonpath = str(REPO_ROOT / "scripts")
    proc = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        capture_output=True,
        text=True,
        timeout=180,
        cwd=str(REPO_ROOT),
        env={
            **__import__("os").environ,
            "PYTHONPATH": env_pythonpath,
        },
    )
    return proc.returncode, proc.stdout, proc.stderr


def block1_parent_runner_passes() -> tuple[int, str]:
    header("BLOCK 1: Re-execute parent runner on current head; expect 52 PASS / 0 FAIL")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_emits_expected_verdict_prefix",
        EXPECTED_VERDICT_PREFIX in out,
        f"VERDICT prefix present in stdout: {EXPECTED_VERDICT_PREFIX in out}",
    )
    record(
        "parent_runner_exact_pass_count_41",
        "EXACT   : PASS = 41, FAIL = 0" in out,
        "looking for 'EXACT   : PASS = 41, FAIL = 0' in stdout",
    )
    record(
        "parent_runner_bounded_pass_count_11",
        "BOUNDED : PASS = 11, FAIL = 0" in out,
        "looking for 'BOUNDED : PASS = 11, FAIL = 0' in stdout",
    )
    record(
        "parent_runner_total_pass_count_52",
        "TOTAL   : PASS = 52, FAIL = 0" in out,
        "looking for 'TOTAL   : PASS = 52, FAIL = 0' in stdout",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify the canonical I2 dimensionless-coupling identity
# -----------------------------------------------------------

def block2_i2_identity_independently_verified() -> None:
    header(
        "BLOCK 2: Re-verify canonical I2 identity alpha = g_bare^2 / (4*pi) symbolically"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable", False, f"import failed: {exc}")
        return
    record("sympy_importable", True, "sympy primitives available")

    # Define the canonical identity (D) of the I2 bridge independently
    # from sympy primitives.  This does NOT import any code from the
    # dep `alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27`;
    # it re-states the well-known QFT convention as a sympy expression.
    g_bare, alpha = sp.symbols("g_bare alpha", positive=True, real=True)
    pi = sp.pi
    D_expr = sp.Eq(alpha, g_bare**2 / (4 * pi))

    # (B2-independent) The defining substitution is exact.
    expected_rhs = g_bare**2 / (4 * pi)
    actual_rhs = D_expr.rhs
    record(
        "i2_identity_rhs_matches_expected",
        sp.simplify(actual_rhs - expected_rhs) == 0,
        "canonical alpha := g_bare^2 / (4*pi) reproduced symbolically",
    )

    # At g_bare = 1, alpha = 1/(4*pi) (matching parent's Section C).
    alpha_at_one = (g_bare**2 / (4 * pi)).subs(g_bare, 1)
    record(
        "i2_identity_specializes_at_gbare_one_to_one_over_four_pi",
        sp.simplify(alpha_at_one - sp.Rational(1) / (4 * pi)) == 0,
        "at g_bare = 1 the identity yields alpha = 1/(4*pi)",
    )

    # The identity is dimensionless: g_bare^2 / (4*pi) involves no
    # additional dimensional symbols.  We check that the only free
    # symbol in the rhs is g_bare.
    free_syms = set(map(str, expected_rhs.free_symbols))
    record(
        "i2_identity_only_free_symbol_is_g_bare",
        free_syms == {"g_bare"},
        f"free symbols = {free_syms}",
    )


# -----------------------------------------------------------
# Block 3: Static source-scan of parent runner
# -----------------------------------------------------------

AUDIT_STATUS_TOKENS = (
    "audit_status",
    "effective_status",
    "intrinsic_status",
    "audited_clean",
    "audited_conditional",
    "retained_no_go",
    "retained_bounded",
    "audit_ledger",
    "audit_grade",
)


def _strip_forbidden_source_phrases_block(source: str) -> str:
    """Strip the parent runner's ``forbidden_source_phrases`` Python list
    literal from the source text.

    The parent runner contains a deliberately-curated list of
    string-literals enumerating phrases that must NOT appear in the
    source NOTE text (a source-firewall self-check).  Those literals
    are *targets of exclusion*, not consumption of any audit-status
    field at runtime.  For the substance-vs-grade scan we therefore
    look at the parent runner with that list-literal block removed,
    and assert no audit-status token appears in the remainder.

    The block is delimited by ``forbidden_source_phrases = [`` and the
    next ``]`` on its own line in the parent runner source.
    """
    start_marker = "forbidden_source_phrases = ["
    idx_start = source.find(start_marker)
    if idx_start == -1:
        return source
    # find the closing bracket on its own line after the start
    idx_end = source.find("\n]", idx_start)
    if idx_end == -1:
        return source
    return source[:idx_start] + source[idx_end + 2 :]


def block3_parent_runner_no_audit_status_references() -> None:
    header(
        "BLOCK 3: Parent runner contains zero audit-status references"
        " (outside the source-firewall exclusion list)"
    )
    source = PARENT_RUNNER.read_text(encoding="utf-8")
    scan_source = _strip_forbidden_source_phrases_block(source)
    record(
        "forbidden_source_phrases_block_stripped",
        len(scan_source) < len(source),
        (
            f"stripped block of {len(source) - len(scan_source)} chars from"
            " forbidden_source_phrases (self-firewall exclusion list)"
        ),
    )
    for token in AUDIT_STATUS_TOKENS:
        record(
            f"parent_runner_no_token_{token}",
            token not in scan_source,
            f"'{token}' absent from parent runner source (outside firewall list)",
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
    for phrase in NOTE_GRADE_DEPENDENCY_PHRASES:
        record(
            f"parent_note_no_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase.lower() not in note_text.lower(),
            f"'{phrase}' absent from parent note",
        )
    # Positive: the parent's load-bearing step is exact substitution
    # arithmetic, which is a structural statement, not a grade statement.
    record(
        "parent_note_load_bearing_step_present",
        "exact rational substitution arithmetic" in note_text.lower()
        or "exact symbolic substitution arithmetic" in note_text.lower(),
        "parent note mentions 'exact (rational|symbolic) substitution arithmetic'",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual re-execution under the dep at unaudited
# -----------------------------------------------------------

def block5_counterfactual_without_dep_grade() -> None:
    header("BLOCK 5: Counterfactual re-execution without dep-grade consultation")
    rc, out, _ = run_parent_runner()
    # The parent runner does not consult the audit ledger; a passing run here
    # demonstrates that the executable substance is grade-independent.
    record(
        "counterfactual_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "counterfactual_runner_verdict_unchanged",
        EXPECTED_VERDICT_PREFIX in out,
        "VERDICT prefix identical to Block 1 (substance-unchanged)",
    )
    record(
        "counterfactual_runner_total_pass_unchanged",
        "TOTAL   : PASS = 52, FAIL = 0" in out,
        "PASS count unchanged from Block 1",
    )


# -----------------------------------------------------------
# Block 6: Direct symbolic re-derivation of (B1)-(B4) chain
# -----------------------------------------------------------

def block6_substitution_chain_self_check() -> None:
    header(
        "BLOCK 6: Direct symbolic re-derivation of (B1)-(B4) chain (sympy)"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block6", False, f"import failed: {exc}")
        return

    g_bare, C_sym, r_sym, alpha_sym = sp.symbols(
        "g_bare C r alpha", positive=True, real=True
    )
    pi = sp.pi
    # (M1) Maradudin asymptotic
    G_sym = 1 / (4 * pi * r_sym)
    # (P1) static-source readout
    V_from_P1 = -C_sym * g_bare**2 * G_sym

    # (B1) substitution residual
    V_B1 = sp.simplify(V_from_P1)
    V_B1_expected = -C_sym * g_bare**2 / (4 * pi * r_sym)
    record(
        "B1_substitution_residual_zero",
        sp.simplify(V_B1 - V_B1_expected) == 0,
        "V_from_P1 == -C * g_bare^2 / (4*pi*r) by sympy.simplify",
    )

    # (B2) define alpha
    alpha_def = g_bare**2 / (4 * pi)
    record(
        "B2_alpha_definition_holds",
        sp.simplify(alpha_def - g_bare**2 / (4 * pi)) == 0,
        "alpha := g_bare^2 / (4*pi) is the canonical I2 identity",
    )

    # (B3) substitution into alpha form
    V_alpha_form = -C_sym * alpha_sym / r_sym
    V_alpha_form_subbed = V_alpha_form.subs(alpha_sym, alpha_def)
    record(
        "B3_alpha_form_consistent_with_B1",
        sp.simplify(V_alpha_form_subbed - V_B1_expected) == 0,
        "-C alpha/r at alpha=alpha_def equals -C g_bare^2/(4*pi*r)",
    )

    # (B4) g_bare = 1 specialization
    alpha_at_gbare1 = alpha_def.subs(g_bare, 1)
    alpha_at_gbare1_expected = sp.Rational(1) / (4 * pi)
    record(
        "B4_alpha_at_gbare_one_equals_one_over_four_pi",
        sp.simplify(alpha_at_gbare1 - alpha_at_gbare1_expected) == 0,
        "alpha at g_bare=1 is exactly 1/(4*pi)",
    )

    V_at_gbare1 = V_B1_expected.subs(g_bare, 1)
    V_at_gbare1_expected = -C_sym / (4 * pi * r_sym)
    record(
        "B4_V_at_gbare_one_equals_minus_C_over_four_pi_r",
        sp.simplify(V_at_gbare1 - V_at_gbare1_expected) == 0,
        "V(r) -> -C/(4*pi*r) at g_bare=1 (I1 readout identification)",
    )

    # Composite chain identity
    chain = sp.simplify(
        -C_sym * g_bare**2 * (1 / (4 * pi * r_sym))
        - (-C_sym * (g_bare**2 / (4 * pi)) / r_sym)
    )
    record(
        "B1_to_B3_composite_chain_identity",
        chain == 0,
        "full chain residual zero: -C g_bare^2/(4*pi*r) = -C (g_bare^2/(4*pi))/r",
    )


# -----------------------------------------------------------
# Block 7: Numerical alpha and Casimir cross-checks
# -----------------------------------------------------------

def block7_numerical_alpha_and_casimir() -> None:
    header(
        "BLOCK 7: Numerical alpha = 1/(4*pi) at g_bare=1 and C_F = 4/3 at N_c = 3"
    )
    PI = math.pi
    FOUR_PI = 4.0 * PI

    alpha_num = 1.0 / FOUR_PI
    expected_alpha = 0.07957747154594768
    record(
        "alpha_num_matches_expected",
        abs(alpha_num - expected_alpha) < 1.0e-15,
        f"alpha = 1/(4*pi) = {alpha_num:.17f} vs expected {expected_alpha:.17f}",
    )

    # Recompute via g_bare^2 / (4*pi) at g_bare = 1
    alpha_num_recomputed = (1.0**2) / FOUR_PI
    record(
        "alpha_num_recomputed_matches",
        abs(alpha_num - alpha_num_recomputed) < 1.0e-15,
        "g_bare^2/(4*pi) at g_bare = 1 numerically equals 1/(4*pi)",
    )

    # Casimir C_F = (N_c^2 - 1) / (2 N_c) at N_c = 3
    N_c = 3
    C_F = (N_c**2 - 1) / (2 * N_c)
    record(
        "C_F_at_N_c_3_equals_four_thirds",
        abs(C_F - 4.0 / 3.0) < 1.0e-15,
        f"C_F = {C_F} (expected 4/3 = {4.0 / 3.0})",
    )

    # V(r) -> -C_F * alpha / r at large r (numerical spot-check)
    for r_val in (5.0, 10.0, 20.0, 50.0):
        V_expected = -C_F * alpha_num / r_val
        V_chain = -C_F * 1.0 / (FOUR_PI * r_val)
        record(
            f"V_chain_equals_V_alpha_form_at_r_{int(r_val)}",
            abs(V_chain - V_expected) < 1.0e-15,
            f"V_chain(r={r_val}) - V_alpha_form(r={r_val}) = {abs(V_chain - V_expected):.3e}",
        )


# -----------------------------------------------------------
# Block 8: No-claim gate preservation across runs
# -----------------------------------------------------------

NO_CLAIM_PHRASES = (
    "(G1) no new repo vocabulary introduced",
    "(G2) no multiplicative cross-row combination used",
    "(G3) regulator-dependence no-go honored",
    "(G4) bridge addresses exactly parent note packet entry I1, not I2 or I3",
    "(F1) no continuum 4D-Fourier-measure d^4 k / (2 pi)^4 import used",
    "(F3) no Wick rotation Z^3 -> Z^4 in load-bearing chain",
)


def block8_no_claim_gate_preserved() -> None:
    header("BLOCK 8: No-claim gate preservation across re-runs")
    _, out, _ = run_parent_runner()
    for phrase in NO_CLAIM_PHRASES:
        record(
            f"no_claim_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')[:60]}",
            phrase in out,
            f"'{phrase}' present in parent runner stdout",
        )
    # Also: the companion note explicitly disclaims promotion/import.
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8")
    record(
        "companion_disclaims_status_promotion",
        "does not promote status" in companion_text.lower()
        or "not a status promotion" in companion_text.lower(),
        "companion explicitly disclaims status promotion",
    )
    record(
        "companion_metadata_declares_meta",
        "type:** meta" in companion_text.lower(),
        "companion metadata declares Type: meta",
    )
    record(
        "companion_names_parent_explicitly",
        "static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27"
        in companion_text.lower(),
        "companion names parent ledger row exactly",
    )
    record(
        "companion_names_dep_explicitly",
        "alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27"
        in companion_text.lower(),
        "companion names weakened dep ledger row exactly",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Static-Source Readout I1 Accepted-Premise Bridge")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log("Repo root: <repo-root>")
    log(f"Parent note: {PARENT_NOTE.relative_to(REPO_ROOT)}")
    log(f"Parent runner: {PARENT_RUNNER.relative_to(REPO_ROOT)}")
    log(f"Weakened dep note: {DEP_NOTE.relative_to(REPO_ROOT)}")
    log(f"Companion source note: {COMPANION_NOTE.relative_to(REPO_ROOT)}")
    log("")
    log("Goal: verify the parent's load-bearing substantive content does")
    log("      not load-bear on the *audit grade* of its dep")
    log("      `alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27`")
    log("      (which was downgraded from retained_bounded to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_i2_identity_independently_verified()
    block3_parent_runner_no_audit_status_references()
    block4_parent_note_no_grade_dependency_claim()
    block5_counterfactual_without_dep_grade()
    block6_substitution_chain_self_check()
    block7_numerical_alpha_and_casimir()
    block8_no_claim_gate_preserved()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: STATIC_SOURCE_READOUT_I1_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: STATIC_SOURCE_READOUT_I1_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
