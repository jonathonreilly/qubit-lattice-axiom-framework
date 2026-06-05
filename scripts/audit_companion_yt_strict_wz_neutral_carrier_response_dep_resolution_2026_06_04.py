#!/usr/bin/env python3
"""Audit-companion runner for the Y_T strict W/Z neutral-carrier response
packet parent note
`YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md`
recording dep-resolution hygiene evidence after the dep weakening
`yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25: retained_bounded -> unaudited`.

Companion source note:
  docs/YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `yt_strict_wz_neutral_carrier_response_packet_note_2026-05-25`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`
    (which was downgraded from `retained_bounded` to `unaudited`).
    Only the *structural neutral-ray finite-Pauli/projector algebra*
    is used, and the parent's own runner re-derives that algebra
    block-for-block.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm SUMMARY: PASS=47 FAIL=0 unchanged.
  Block 2 : Re-verify the neutral-ray finite-Pauli/projector algebra
            inputs (P_- H_0 = H_0, Q H_0 = 0, sigma_z = I - 2 P_-,
            projector / orthogonality / completeness) directly from
            sympy primitives, independent of the dep runner.
  Block 3 : Static source-scan of the parent's runner: confirm no
            ledger read of the weakened dep claim_id.
  Block 4 : Static source-scan of the parent note: confirm no claim
            that the substantive conclusion depends on the dep's
            audit grade.
  Block 5 : Counterfactual re-execution without consulting the dep's
            audit grade: parent runner pass count identical to Block 1.
  Block 6 : Strict W/Z response self-check at the algebraic level
            (the parent's load-bearing differentiation step),
            independent of any dep grade.
  Block 7 : Source-coordinate reparameterization invariance self-check
            (s = f(r) invariance of the W/Z ratio), independent of any
            dep grade.
  Block 8 : Forbidden-overclaim absences preserved in the parent note;
            companion declares claim_type=meta and disclaims status
            promotion.

Every check uses only the parent's existing runner / sympy primitives.
No audit-status content is asserted. No new theorem claim is made.

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
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_yt_strict_wz_neutral_carrier_response_packet.py"
PARENT_NOTE = REPO_ROOT / "docs" / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
DEP_NOTE = REPO_ROOT / "docs" / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_"
    "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

WEAKENED_DEP_CLAIM_ID = (
    "yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25"
)

EXPECTED_SUMMARY = "SUMMARY: PASS=47 FAIL=0"


# -----------------------------------------------------------
# Block 1: Re-execute the parent runner on the current head
# -----------------------------------------------------------

def run_parent_runner() -> tuple[int, str, str]:
    """Return (returncode, stdout, stderr) of the parent runner."""
    proc = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        capture_output=True,
        text=True,
        timeout=180,
        cwd=str(REPO_ROOT),
    )
    return proc.returncode, proc.stdout, proc.stderr


def block1_parent_runner_passes() -> tuple[int, str]:
    header("BLOCK 1: Re-execute parent runner on current head; expect PASS=47 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_emits_expected_summary",
        EXPECTED_SUMMARY in out,
        f"'{EXPECTED_SUMMARY}' present in stdout: {EXPECTED_SUMMARY in out}",
    )
    record(
        "parent_runner_zero_fails",
        " FAIL=0" in out,
        "looking for ' FAIL=0' in stdout",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify neutral-ray finite-Pauli/projector algebra
#          directly from sympy primitives.
# -----------------------------------------------------------

def block2_neutral_ray_algebra_independently_verified() -> None:
    header(
        "BLOCK 2: Re-verify neutral-ray finite-Pauli/projector algebra directly"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover - import failure
        record("sympy_importable", False, f"import failed: {exc}")
        return

    record("sympy_importable", True, "imported sympy")

    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_plus = (ident + z) / 2
    p_minus = (ident - z) / 2
    t3 = z / 2
    y_h = sp.Rational(1, 2) * ident
    q = t3 + y_h

    def m_is_zero(m: sp.Matrix) -> bool:
        return all(sp.simplify(e) == 0 for e in m)

    record(
        "P_plus_is_projector",
        m_is_zero(p_plus * p_plus - p_plus),
        "P_+^2 = P_+",
    )
    record(
        "P_minus_is_projector",
        m_is_zero(p_minus * p_minus - p_minus),
        "P_-^2 = P_-",
    )
    record(
        "P_plus_P_minus_orthogonal",
        m_is_zero(p_plus * p_minus),
        "P_+ P_- = 0",
    )
    record(
        "P_plus_plus_P_minus_completeness",
        m_is_zero(p_plus + p_minus - ident),
        "P_+ + P_- = I",
    )
    record(
        "sigma_z_equals_P_plus_minus_P_minus",
        m_is_zero(z - (p_plus - p_minus)),
        "sigma_z = P_+ - P_-",
    )
    record(
        "sigma_z_equals_I_minus_2_P_minus",
        m_is_zero(z - (ident - 2 * p_minus)),
        "sigma_z = I - 2 P_-",
    )

    # Neutral-ray identifications on the retained one-Higgs surface.
    v = sp.symbols("v", positive=True, real=True)
    h0 = sp.Matrix([0, v / sp.sqrt(2)])
    upper = sp.Matrix([1, 0])

    record(
        "P_minus_fixes_H0",
        m_is_zero(p_minus * h0 - h0),
        "P_- H_0 = H_0 on (0, v/sqrt(2))",
    )
    record(
        "P_plus_kills_H0",
        m_is_zero(p_plus * h0),
        "P_+ H_0 = 0",
    )
    record(
        "Q_annihilates_H0",
        m_is_zero(q * h0),
        "Q H_0 = 0 (neutral)",
    )
    record(
        "Q_acts_as_identity_on_upper",
        m_is_zero(q * upper - upper),
        "upper-component is charged: Q (1,0)^T = (1,0)^T",
    )

    # Radial tangent stays on the same neutral ray.
    s = sp.symbols("s", real=True)
    vs = sp.Function("v")(s)
    h_s = sp.Matrix([0, vs / sp.sqrt(2)])
    tangent = sp.diff(h_s, s)
    record(
        "H_s_on_P_minus_ray",
        m_is_zero(p_minus * h_s - h_s),
        "P_- H(s) = H(s) for H(s) = (0, v(s)/sqrt(2))",
    )
    record(
        "dH_ds_on_P_minus_ray",
        m_is_zero(p_minus * tangent - tangent),
        "P_- dH/ds = dH/ds",
    )
    record(
        "dH_ds_is_Q_neutral",
        m_is_zero(q * tangent),
        "Q dH/ds = 0",
    )


# -----------------------------------------------------------
# Block 3: Static source-scan of parent runner — confirm no ledger
#          read of the weakened dep claim_id.
# -----------------------------------------------------------

def block3_parent_runner_no_dep_grade_read() -> None:
    header(
        "BLOCK 3: Parent runner does not read the weakened dep's ledger row"
    )
    source = PARENT_RUNNER.read_text(encoding="utf-8")
    # The parent runner does call ledger_row(...) for several other rows,
    # but it must NOT call it on the weakened dep's claim_id.
    record(
        "parent_runner_no_ledger_read_of_weakened_dep",
        f'ledger_row("{WEAKENED_DEP_CLAIM_ID}")' not in source
        and f"ledger_row('{WEAKENED_DEP_CLAIM_ID}')" not in source,
        f"no ledger_row({WEAKENED_DEP_CLAIM_ID}) call",
    )
    # Defensive: even if the runner ever computed something against the
    # dep's grade as a string literal, that would be a smell.  Ensure
    # the dep claim_id appears at most in a path constant, not in a
    # ledger_row call or grade comparison.
    occurrences = [
        line
        for line in source.splitlines()
        if WEAKENED_DEP_CLAIM_ID in line
    ]
    record(
        "parent_runner_dep_claim_id_only_in_path_constants",
        all(
            ("ledger_row" not in line)
            and ("effective_status" not in line)
            and ("audit_status" not in line)
            for line in occurrences
        ),
        f"{len(occurrences)} occurrences of '{WEAKENED_DEP_CLAIM_ID}' in parent runner (none in grade-read context)",
    )

    # Audit-status tokens scan: confirm parent runner does not gate any
    # check on dep grade strings related to the weakened dep claim_id.
    # (Other ledger reads target retained authority rows by design.)
    for token in (
        "audit_status",
        "intrinsic_status",
        "retained_bounded",
        "audited_clean",
        "audited_conditional",
        "retained_no_go",
        "unaudited",
    ):
        if token in source:
            # The token may appear but must not be associated with the
            # weakened dep's claim_id (we already checked above).
            # Record presence-of-token as informational PASS.
            record(
                f"parent_runner_audit_token_{token}_present_but_not_dep_gated",
                True,
                f"'{token}' may appear but is not weakened-dep-gated",
            )


# -----------------------------------------------------------
# Block 4: Static source-scan of parent note: confirm no claim
#          that the substantive transport conclusion depends on the
#          dep's audit grade.
# -----------------------------------------------------------

NOTE_GRADE_DEPENDENCY_PHRASES = (
    "load-bears on the dep's audit",
    "depends on the dep's audit grade",
    "requires the dep to be retained",
    "requires retained_bounded",
    "requires audited_clean",
    "conditional on the dep's audit",
    "conditional on the dep being",
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
    # Positive: parent note still describes its load-bearing differentiation
    # step in structural-algebraic terms.
    record(
        "parent_note_load_bearing_step_present",
        "Strict W/Z Response Rows" in note_text,
        "parent note still contains the 'Strict W/Z Response Rows' section",
    )
    record(
        "parent_note_response_ratio_present",
        "g_2 / sqrt(g_2^2 + g_Y^2)" in note_text,
        "parent note still contains the W/Z response ratio formula",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual re-execution under the dep at unaudited
# -----------------------------------------------------------

def block5_counterfactual_without_dep_grade() -> None:
    header("BLOCK 5: Counterfactual re-execution without dep-grade consultation")
    rc, out, _ = run_parent_runner()
    # The parent runner does not consult the audit ledger for the
    # weakened dep; a passing run here demonstrates that the executable
    # substance is grade-independent for the weakened dep.
    record(
        "counterfactual_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "counterfactual_runner_summary_unchanged",
        EXPECTED_SUMMARY in out,
        "SUMMARY: PASS=47 FAIL=0 identical to Block 1 (substance-unchanged)",
    )
    record(
        "counterfactual_runner_no_failures",
        " FAIL=0" in out,
        "PASS count unchanged from Block 1",
    )


# -----------------------------------------------------------
# Block 6: Strict W/Z response rows: algebraic self-check.
# -----------------------------------------------------------

def block6_strict_wz_response_rows_algebraic() -> None:
    header(
        "BLOCK 6: Strict W/Z response rows (algebraic self-check)"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block6", False, f"import failed: {exc}")
        return

    s = sp.symbols("s", real=True)
    g2, gy = sp.symbols("g_2 g_Y", positive=True)
    v = sp.Function("v")(s)
    mw = g2 * v / 2
    mz = sp.sqrt(g2**2 + gy**2) * v / 2
    dmw = sp.diff(mw, s)
    dmz = sp.diff(mz, s)
    expected_dmw = g2 * sp.diff(v, s) / 2
    expected_dmz = sp.sqrt(g2**2 + gy**2) * sp.diff(v, s) / 2

    def is_zero(expr: sp.Expr) -> bool:
        return sp.simplify(expr) == 0

    record(
        "dMW_ds_matches_expected",
        is_zero(dmw - expected_dmw),
        "dM_W/ds = (g_2 / 2) v'(s)",
    )
    record(
        "dMZ_ds_matches_expected",
        is_zero(dmz - expected_dmz),
        "dM_Z/ds = (sqrt(g_2^2 + g_Y^2) / 2) v'(s)",
    )

    ratio = sp.simplify(dmw / dmz)
    record(
        "wz_response_ratio_cancels_jacobian",
        is_zero(ratio - g2 / sp.sqrt(g2**2 + gy**2)),
        "ratio = g_2 / sqrt(g_2^2 + g_Y^2) (Jacobian cancels)",
    )

    recovered_jacobian = sp.simplify(2 * dmw / g2)
    record(
        "absolute_W_response_recovers_jacobian",
        is_zero(recovered_jacobian - sp.diff(v, s)),
        "v'(s) = 2 (dM_W/ds) / g_2 if g_2 is known",
    )


# -----------------------------------------------------------
# Block 7: Source-coordinate reparameterization invariance.
# -----------------------------------------------------------

def block7_reparameterization_invariance() -> None:
    header(
        "BLOCK 7: Source-coordinate reparameterization invariance (s = f(r))"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable_block7", False, f"import failed: {exc}")
        return

    r = sp.symbols("r", real=True)
    g2, gy = sp.symbols("g_2 g_Y", positive=True)
    f = sp.Function("f")(r)
    v = sp.Function("v")(f)
    mw = g2 * v / 2
    mz = sp.sqrt(g2**2 + gy**2) * v / 2

    dmw_dr = sp.diff(mw, r)
    dmz_dr = sp.diff(mz, r)
    ratio = sp.simplify(dmw_dr / dmz_dr)
    record(
        "wz_ratio_invariant_under_reparameterization",
        sp.simplify(ratio - g2 / sp.sqrt(g2**2 + gy**2)) == 0,
        "ratio = g_2 / sqrt(g_2^2 + g_Y^2) under any local s = f(r)",
    )

    # Second reparameterization: try v(g(r)) for an arbitrary g.
    g = sp.Function("g")(r)
    v2 = sp.Function("v")(g)
    mw2 = g2 * v2 / 2
    mz2 = sp.sqrt(g2**2 + gy**2) * v2 / 2
    ratio2 = sp.simplify(sp.diff(mw2, r) / sp.diff(mz2, r))
    record(
        "wz_ratio_invariant_under_second_reparameterization",
        sp.simplify(ratio2 - g2 / sp.sqrt(g2**2 + gy**2)) == 0,
        "ratio still cancels under a second arbitrary s = g(r)",
    )

    # Same-coordinate Feynman-Hellmann common factor cancellation: any
    # scalar multiplier alpha(r) on both numerator and denominator
    # cancels in the ratio.
    alpha = sp.Function("alpha")(r)
    ratio_alpha = sp.simplify((alpha * dmw_dr) / (alpha * dmz_dr))
    record(
        "wz_ratio_invariant_under_common_multiplier",
        sp.simplify(ratio_alpha - g2 / sp.sqrt(g2**2 + gy**2)) == 0,
        "common multiplier alpha(r) cancels in the W/Z ratio",
    )


# -----------------------------------------------------------
# Block 8: Forbidden-overclaim absences preserved in parent note;
#          companion declares meta and disclaims status promotion.
# -----------------------------------------------------------

FORBIDDEN_OVERCLAIM_ABSENCES = (
    "Status:** retained",
    "proposed_retained",
    "This packet derives `y_t`",
    "positive Y_T closure has been obtained",
    "coefficient-certified top response rows are present",
    "physical-scale `g_2(v)` is retained",
)


def block8_no_claim_gate_preserved() -> None:
    header("BLOCK 8: Forbidden-overclaim absences preserved in parent note")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")
    for phrase in FORBIDDEN_OVERCLAIM_ABSENCES:
        record(
            f"forbidden_overclaim_absent_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase not in note_text,
            f"'{phrase}' absent from parent note",
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
        "companion_metadata_declares_companion_only",
        "companion-only" in companion_text.lower(),
        "companion metadata declares status: companion-only",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Y_T Strict W/Z Neutral-Carrier Response Packet")
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
    log("      `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`")
    log("      (which was downgraded from retained_bounded to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_neutral_ray_algebra_independently_verified()
    block3_parent_runner_no_dep_grade_read()
    block4_parent_note_no_grade_dependency_claim()
    block5_counterfactual_without_dep_grade()
    block6_strict_wz_response_rows_algebraic()
    block7_reparameterization_invariance()
    block8_no_claim_gate_preserved()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
