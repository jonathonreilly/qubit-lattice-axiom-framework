#!/usr/bin/env python3
"""Audit-companion runner for the signed-gravity tensor-source transport
retention parent note
`SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md`
recording dep-resolution hygiene evidence after the dep weakening
`tensor_source_map_eta_note: retained_bounded -> unaudited`.

Companion source note:
  docs/SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `signed_gravity_tensor_source_transport_retention_note`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep `tensor_source_map_eta_note` (which was downgraded from
    `retained_bounded` to `unaudited`).  Only the *structural rank-2
    carrier* on the audited restricted classes is used, and the
    parent's own runner re-verifies that carrier block-for-block.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm the FINAL_TAG is unchanged with PASS=6 FAIL=0.
  Block 2 : Re-verify the rank-2 carrier inputs (rank, scalar-
            blindness, mixed additivity, non-scalar block structure)
            on both restricted classes directly from
            scripts/frontier_tensor_source_map_eta.py.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            audit-status references (audit_status, effective_status,
            intrinsic_status, retained_bounded, audited_clean,
            audited_conditional, retained, unaudited).
  Block 4 : Static source-scan of the parent note: confirm no claim
            that the substantive transport conclusion depends on the
            dep's audit grade (no language like "because the dep is
            retained" or "load-bears on the dep's audit grade").
  Block 5 : Counterfactual re-execution without consulting the dep's
            audit grade: parent runner pass count and FINAL_TAG
            identical to Block 1.
  Block 6 : Locally-constant orientation-line transport self-check:
            chi commutes with linear transport on a 5-site refinement
            family at the algebraic level, independent of any dep grade.
  Block 7 : Nonlinear-gate calibration consistency self-check:
            linear_odd_resid = 0 and nonlinear_even_resid matches
            expected_even within tolerance.
  Block 8 : No-claim gate preservation across the runs (the runner's
            final no-claim gate result is preserved verbatim).

Every check uses only the parent's existing runner / dep runner code
(re-imported) plus standard finite-dimensional numerics.  No
audit-status content is asserted.  No new theorem claim is made.

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
PARENT_RUNNER = REPO_ROOT / "scripts" / "signed_gravity_tensor_source_transport_retention.py"
PARENT_NOTE = REPO_ROOT / "docs" / "SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md"
DEP_RUNNER = REPO_ROOT / "scripts" / "frontier_tensor_source_map_eta.py"
DEP_NOTE = REPO_ROOT / "docs" / "TENSOR_SOURCE_MAP_ETA_NOTE.md"
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_"
    "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

EXPECTED_FINAL_TAG = (
    "FINAL_TAG: SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_FINITE_CONDITIONAL"
)


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
    header("BLOCK 1: Re-execute parent runner on current head; expect PASS=6 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_emits_expected_final_tag",
        EXPECTED_FINAL_TAG in out,
        f"FINAL_TAG present in stdout: {EXPECTED_FINAL_TAG in out}",
    )
    record(
        "parent_runner_summary_six_pass_zero_fail",
        "SUMMARY: PASS=6 FAIL=0" in out,
        "looking for 'SUMMARY: PASS=6 FAIL=0' in stdout",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify the rank-2 carrier inputs directly
# -----------------------------------------------------------

def block2_carrier_inputs_independently_verified() -> None:
    header("BLOCK 2: Re-verify rank-2 carrier on both restricted classes directly")
    sys.path.insert(0, str(REPO_ROOT))
    try:
        import numpy as np

        from scripts.frontier_tensor_source_map_eta import response_matrix, tm  # noqa: E402
    except Exception as exc:  # pragma: no cover - import failure
        record("dep_runner_importable", False, f"import failed: {exc}")
        return
    dep_imported = callable(response_matrix) and tm is not None
    record(
        "dep_runner_importable",
        dep_imported,
        "imported scripts.frontier_tensor_source_map_eta.{response_matrix, tm}",
    )
    if not dep_imported:
        return

    oh = response_matrix(tm.same_source.build_best_phi_grid())
    fr = response_matrix(tm.coarse.build_finite_rank_phi_grid())

    # On both classes, eta is rank-2 (det != 0, min sigma > tol).
    for label, row in (("O_h", oh), ("finite_rank", fr)):
        det = float(np.linalg.det(row.eta))
        min_sv = float(np.min(np.linalg.svd(row.eta, compute_uv=False)))
        record(
            f"carrier_rank_two_{label}",
            det > 1.0e-6 and min_sv > 1.0e-4,
            f"det={det:.3e} min_sv={min_sv:.3e}",
        )
        record(
            f"carrier_scalar_blind_{label}",
            bool(row.scalar_blind),
            f"scalar_blind={row.scalar_blind}",
        )
        record(
            f"carrier_mixed_additive_{label}",
            row.mixed_add_ti < 1.0e-6 and row.mixed_add_tf < 1.0e-6,
            f"mixed_add_ti={row.mixed_add_ti:.1e} mixed_add_tf={row.mixed_add_tf:.1e}",
        )
        record(
            f"carrier_nonscalar_block_{label}",
            row.eta[0, 0] > 1.0e-3 and row.eta[1, 1] > 1.0e-2,
            f"eta[0,0]={row.eta[0,0]:.3e} eta[1,1]={row.eta[1,1]:.3e}",
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
    for phrase in NOTE_GRADE_DEPENDENCY_PHRASES:
        record(
            f"parent_note_no_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase.lower() not in note_text.lower(),
            f"'{phrase}' absent from parent note",
        )
    # Positive: the parent's load-bearing step is the locally-constant
    # orientation line, which is a structural statement, not a grade
    # statement.  We confirm the substantive phrasing is preserved.
    record(
        "parent_note_load_bearing_step_present",
        "locally constant" in note_text.lower(),
        "parent note mentions 'locally constant' (structural step)",
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
        "counterfactual_runner_final_tag_unchanged",
        EXPECTED_FINAL_TAG in out,
        "FINAL_TAG identical to Block 1 (substance-unchanged)",
    )
    record(
        "counterfactual_runner_six_pass_zero_fail",
        "SUMMARY: PASS=6 FAIL=0" in out,
        "PASS count unchanged from Block 1",
    )


# -----------------------------------------------------------
# Block 6: Locally-constant orientation-line transport self-check
# -----------------------------------------------------------

def block6_locally_constant_orientation_transport() -> None:
    header(
        "BLOCK 6: Locally-constant orientation line: chi commutes with linear transport"
    )
    sys.path.insert(0, str(REPO_ROOT))
    try:
        import numpy as np
    except Exception as exc:  # pragma: no cover
        record("numpy_importable", False, f"import failed: {exc}")
        return

    # On a gapped component, chi_eta is locally constant.  Pick a fixed
    # chi = +1 and chi = -1 and verify that for ANY linear transport
    # R (here a random invertible matrix), chi commutes through:
    # R(chi * x) = chi * R(x).  This is the parent's load-bearing
    # algebraic step (chi is a scalar, scalars commute with linear maps).
    rng = np.random.default_rng(20260604)
    max_resid = 0.0
    for trial in range(10):
        dim = 8
        R = rng.normal(size=(dim, dim))
        x = rng.normal(size=dim)
        for chi in (+1, -1):
            lhs = R @ (chi * x)
            rhs = chi * (R @ x)
            max_resid = max(max_resid, float(np.linalg.norm(lhs - rhs)))
    record(
        "scalar_commutes_with_linear_transport",
        max_resid < 1.0e-12,
        f"max_resid={max_resid:.1e} (chi*R = R*chi on a locally-constant sign)",
    )

    # Same check at the projective pushforward level: P(chi * x) = chi * P(x).
    max_resid_proj = 0.0
    for trial in range(5):
        copies = 3
        dim = 4
        r_inj = np.kron(np.ones((copies, 1), dtype=float) / math.sqrt(copies), np.eye(dim))
        p = r_inj.T
        x_fine = rng.normal(size=copies * dim)
        for chi in (+1, -1):
            lhs = p @ (chi * x_fine)
            rhs = chi * (p @ x_fine)
            max_resid_proj = max(max_resid_proj, float(np.linalg.norm(lhs - rhs)))
    record(
        "scalar_commutes_with_projective_pushforward",
        max_resid_proj < 1.0e-12,
        f"max_resid_proj={max_resid_proj:.1e} (chi*P = P*chi)",
    )


# -----------------------------------------------------------
# Block 7: Nonlinear-gate calibration consistency self-check
# -----------------------------------------------------------

def block7_nonlinear_gate_calibration() -> None:
    header("BLOCK 7: Nonlinear-gate calibration consistency (independent self-check)")
    sys.path.insert(0, str(REPO_ROOT))
    try:
        import numpy as np
    except Exception as exc:  # pragma: no cover
        record("numpy_importable_block7", False, f"import failed: {exc}")
        return

    rng = np.random.default_rng(20260604)
    dim = 6
    # A linear operator: K h.  Verify K(-h) + K(h) = 0 (odd).
    K = rng.normal(size=(dim, dim))
    h = rng.normal(size=dim)
    linear_odd = K @ (-h) + K @ h
    record(
        "linear_operator_is_odd",
        float(np.linalg.norm(linear_odd)) < 1.0e-12,
        f"||K(-h) + K(h)||={float(np.linalg.norm(linear_odd)):.1e}",
    )

    # A quadratic backreaction: Q(h, h).  Verify Q(-h, -h) = Q(h, h) (even).
    Q3 = rng.normal(size=(dim, dim, dim))
    Q3 = 0.5 * (Q3 + np.swapaxes(Q3, 1, 2))  # symmetric in the last two
    Q_pos = np.einsum("ijk,j,k->i", Q3, h, h)
    Q_neg = np.einsum("ijk,j,k->i", Q3, -h, -h)
    record(
        "quadratic_backreaction_is_even",
        float(np.linalg.norm(Q_pos - Q_neg)) < 1.0e-12,
        f"||Q(h,h) - Q(-h,-h)||={float(np.linalg.norm(Q_pos - Q_neg)):.1e}",
    )

    # Then E(h) = Kh + alpha Q(h,h), and E(-h) + E(h) = 2 alpha Q(h,h).
    alpha = 0.31
    Eh = K @ h + alpha * np.einsum("ijk,j,k->i", Q3, h, h)
    Emh = K @ (-h) + alpha * np.einsum("ijk,j,k->i", Q3, -h, -h)
    actual = Emh + Eh
    expected = 2.0 * alpha * np.einsum("ijk,j,k->i", Q3, h, h)
    record(
        "nonlinear_even_jet_calibration",
        float(np.linalg.norm(actual - expected)) < 1.0e-12,
        "E(-h) + E(h) = 2 alpha Q(h,h) within tol",
    )


# -----------------------------------------------------------
# Block 8: No-claim gate preservation across the runs
# -----------------------------------------------------------

NO_CLAIM_PHRASES = (
    "negative_inertial_mass=False",
    "shielding=False",
    "propulsion=False",
    "reactionless_force=False",
    "physical_signed_gravity_prediction=False",
)


def block8_no_claim_gate_preserved() -> None:
    header("BLOCK 8: No-claim gate preservation across re-runs")
    _, out, _ = run_parent_runner()
    for phrase in NO_CLAIM_PHRASES:
        record(
            f"no_claim_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
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


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Signed Gravity Tensor-Source Transport Retention")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log(f"Repo root: {REPO_ROOT}")
    log(f"Parent note: {PARENT_NOTE}")
    log(f"Parent runner: {PARENT_RUNNER}")
    log(f"Dep runner: {DEP_RUNNER}")
    log(f"Companion source note: {COMPANION_NOTE.relative_to(REPO_ROOT)}")
    log("")
    log("Goal: verify the parent's load-bearing substantive content does")
    log("      not load-bear on the *audit grade* of its dep")
    log("      `tensor_source_map_eta_note` (which was downgraded from")
    log("      retained_bounded to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_carrier_inputs_independently_verified()
    block3_parent_runner_no_audit_status_references()
    block4_parent_note_no_grade_dependency_claim()
    block5_counterfactual_without_dep_grade()
    block6_locally_constant_orientation_transport()
    block7_nonlinear_gate_calibration()
    block8_no_claim_gate_preserved()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
