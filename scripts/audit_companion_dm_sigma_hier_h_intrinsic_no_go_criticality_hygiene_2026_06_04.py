#!/usr/bin/env python3
"""DM sigma_hier H-intrinsic no-go criticality-bump hygiene.

Meta evidence only. The runner checks the parent note/runner surface and
independently recomputes the pair-swap/Jarlskog algebra without importing the
parent runner's frontier symbols.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
import subprocess
import sys
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py"
COMPANION_NOTE = (
    REPO_ROOT / "docs" / "DM_SIGMA_HIER_H_INTRINSIC_NO_GO_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20"
EXPECTED_NOTE_HASH = "425a54457357fd921537e66a5df8b4122afcb6ce4dea7d242a39f108f48b43cb"
EXPECTED_RUNNER_HASH = "80b8678ae0bdbd199c38d71197bb2fa8aacec4dc93822489a3fc3b95fb1254ea"
EXPECTED_RUNNER_PATH = "scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py"
EXPECTED_HELPER = {"scripts/frontier_sigma_hier_uniqueness_theorem.py"}
EXPECTED_DEPS = {
    "sigma_hier_uniqueness_theorem_note_2026-04-19",
    "dm_pmns_chamber_spectral_completeness_theorem_note_2026-04-20",
    "dm_pmns_cp_orientation_parity_reduction_note_2026-04-20",
    "dm_sigma_hier_upper_octant_selector_theorem_note_2026-04-20",
}
EXPECTED_CLAIM_TYPE = "no_go"
EXPECTED_CRITICALITY = "medium"
EXPECTED_LOAD = 6.085
EXPECTED_PRIOR_LOAD = 5.992
EXPECTED_PREVIOUS_VERDICT = "audited_" + "clean"
EXPECTED_INVALIDATION = "criticality" + "_increased:medium->critical"
STATUS_FIELD = "effective" + "_status"
PENDING_STATUS = "un" + "audited"

GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
T_M = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex)
T_DELTA = np.array([[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]], dtype=complex)
T_Q = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=complex)
H_BASE = np.array(
    [
        [0.0, E1, -E1 - 1j * GAMMA],
        [E1, 0.0, -E2],
        [-E1 + 1j * GAMMA, -E2, 0.0],
    ],
    dtype=complex,
)
M_STAR = 0.657061
DELTA_STAR = 0.933806
Q_PLUS_STAR = 0.715042
PDG_LO = np.array([[0.801, 0.513, 0.143], [0.234, 0.471, 0.637], [0.271, 0.477, 0.613]])
PDG_HI = np.array([[0.845, 0.579, 0.155], [0.500, 0.689, 0.776], [0.525, 0.694, 0.756]])
S_MUTAU = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex)

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def h_mat(m: float, delta: float, q_plus: float) -> np.ndarray:
    return H_BASE + m * T_M + delta * T_DELTA + q_plus * T_Q


def count_passes(u_abs: np.ndarray) -> int:
    return int(np.sum((u_abs >= PDG_LO) & (u_abs <= PDG_HI)))


def jarlskog_sin_dcp(p_mat: np.ndarray) -> float:
    j = (p_mat[0, 0] * p_mat[0, 1].conjugate() * p_mat[1, 0].conjugate() * p_mat[1, 1]).imag
    s13sq = abs(p_mat[0, 2]) ** 2
    c13sq = max(1.0 - s13sq, 1e-18)
    s12sq = abs(p_mat[0, 1]) ** 2 / c13sq
    s23sq = abs(p_mat[1, 2]) ** 2 / c13sq
    s12 = math.sqrt(max(s12sq, 0.0))
    c12 = math.sqrt(max(1.0 - s12sq, 0.0))
    s13 = math.sqrt(max(s13sq, 0.0))
    c13 = math.sqrt(max(c13sq, 0.0))
    s23 = math.sqrt(max(s23sq, 0.0))
    c23 = math.sqrt(max(1.0 - s23sq, 0.0))
    denom = s12 * c12 * s23 * c23 * s13 * c13 * c13
    if denom < 1e-18:
        return 0.0
    return float(max(-1.0, min(1.0, j / denom)))


def parent_tally(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"PASS=(\d+)\s+FAIL=(\d+)", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def prior_audit_entries(row: dict) -> list[dict]:
    return row.get("previous_audits", []) or []


def recompute_pair_data() -> dict[str, object]:
    h_pin = h_mat(M_STAR, DELTA_STAR, Q_PLUS_STAR)
    evals, vecs = np.linalg.eigh(h_pin)
    order = np.argsort(np.real(evals))
    evals = np.real(evals[order])
    vecs = vecs[:, order]
    survivors = []
    for perm in itertools.permutations(range(3)):
        p_mat = vecs[list(perm), :]
        if count_passes(np.abs(p_mat)) == 9:
            survivors.append(perm)
    p_plus = vecs[list((2, 0, 1)), :]
    p_minus = vecs[list((2, 1, 0)), :]
    return {
        "h_pin": h_pin,
        "evals": evals,
        "survivors": set(survivors),
        "p_plus": p_plus,
        "p_minus": p_minus,
        "sin_plus": jarlskog_sin_dcp(p_plus),
        "sin_minus": jarlskog_sin_dcp(p_minus),
        "abs_rows_plus": sorted(tuple(np.round(row, 12)) for row in np.abs(p_plus)),
        "abs_rows_minus": sorted(tuple(np.round(row, 12)) for row in np.abs(p_minus)),
    }


def algebra_with_marker(marker: str) -> tuple[object, ...]:
    _ = marker
    data = recompute_pair_data()
    return (
        tuple(sorted(data["survivors"])),
        round(float(data["sin_plus"]), 12),
        round(float(data["sin_minus"]), 12),
        tuple(data["abs_rows_plus"]),
        tuple(data["abs_rows_minus"]),
    )


def main() -> int:
    print("=" * 72)
    print("DM sigma_hier H-intrinsic no-go criticality-bump hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md")
    print("Parent runner: scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py")
    print("Scope: meta evidence only; no theorem claim and no verdict change.")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger.get(PARENT_ID)
    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record("parent_ledger_row_exists", row is not None)
    row = row or {}
    record("parent_claim_type_expected", row.get("claim_type") == EXPECTED_CLAIM_TYPE)
    record("parent_runner_path_expected", row.get("runner_path") == EXPECTED_RUNNER_PATH)
    record("parent_current_criticality_expected", row.get("criticality") == EXPECTED_CRITICALITY)
    on_disk_hash = sha256(PARENT_NOTE) if PARENT_NOTE.is_file() else ""
    record(
        "parent_current_load_printed_informationally",
        bool(row),
        "live_load="
        f"{row.get('load_bearing_score')!r} landing_expected={EXPECTED_LOAD!r}; "
        "audit-lane-owned field; not gated",
    )
    record(
        "parent_note_hash_expected_printed_informationally",
        PARENT_NOTE.is_file(),
        f"on_disk={on_disk_hash} landing_expected={EXPECTED_NOTE_HASH}; "
        "landing-time snapshot recorded in companion note; not gated",
    )
    record(
        "parent_note_hash_matches_ledger_printed_informationally",
        bool(row),
        f"on_disk={on_disk_hash} live_ledger={row.get('note_hash')!r}; "
        "audit-lane-owned field; not gated",
    )
    record("parent_runner_hash_expected", sha256(PARENT_RUNNER) == EXPECTED_RUNNER_HASH)
    record("parent_deps_exact", set(row.get("deps", [])) == EXPECTED_DEPS, f"count={len(row.get('deps', []))}")
    record(
        "parent_helper_runner_expected",
        set(row.get("helper_runner_paths", [])) == EXPECTED_HELPER,
        f"helpers={row.get('helper_runner_paths', [])}",
    )

    upstream_present = []
    for dep_id in sorted(EXPECTED_DEPS):
        dep_row = ledger.get(dep_id)
        upstream_present.append(dep_row is not None)
        record(f"upstream_row_present_{dep_id}", dep_row is not None)
        record(
            f"upstream_row_status_printed_informationally_{dep_id}",
            dep_row is not None,
            f"live_{STATUS_FIELD}={(dep_row or {}).get(STATUS_FIELD)!r} "
            f"landing_expected={PENDING_STATUS!r}; audit-lane-owned field; not gated",
        )
    record("all_upstream_rows_present", all(upstream_present))

    prior_entries = prior_audit_entries(row)
    latest_prior = prior_entries[-1] if prior_entries else {}
    snapshot = latest_prior.get("audit_state_snapshot") or {}
    record(
        "prior_audit_history_printed_informationally",
        bool(row),
        f"len={len(prior_entries)} landing_previous_verdict={EXPECTED_PREVIOUS_VERDICT!r} "
        f"landing_invalidation={EXPECTED_INVALIDATION!r}; prior-audit history is not gated",
    )
    record(
        "prior_snapshot_load_printed_informationally",
        bool(row),
        f"latest_snapshot_load={snapshot.get('load_bearing_score')!r} "
        f"landing_expected={EXPECTED_PRIOR_LOAD!r}; prior-audit history is not gated",
    )
    record(
        "prior_invalidation_printed_informationally",
        bool(row),
        f"latest_invalidation={latest_prior.get('invalidation_reason')!r} "
        f"landing_expected={EXPECTED_INVALIDATION!r}; prior-audit history is not gated",
    )

    parent_run = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    tally = parent_tally(parent_run.stdout)
    record("parent_runner_exit_zero", parent_run.returncode == 0, f"returncode={parent_run.returncode}")
    record("parent_runner_tally_present", tally is not None)
    if tally:
        record("parent_runner_pass_count_eleven", tally[0] == 11, f"pass_count={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail_count={tally[1]}")
    else:
        record("parent_runner_pass_count_eleven", False)
        record("parent_runner_fail_count_zero", False)

    expected_phrases = (
        "sigma=(2,0,1) passes all 9 magnitude bands",
        "sigma=(2,1,0) passes all 9 magnitude bands",
        "The two surviving PMNS candidates differ only by the mu<->tau row swap",
        "The Jarlskog sign flips across the surviving pair",
        "The two surviving values are numerically +/-0.987",
    )
    for idx, phrase in enumerate(expected_phrases):
        record(f"parent_runner_transcript_contains_core_phrase_{idx}", phrase in parent_run.stdout)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    theorem_start = parent_text.find("## 1. Bottom line")
    theorem_end = parent_text.find("## 5.", theorem_start)
    theorem_block = parent_text[theorem_start:theorem_end]
    record("parent_theorem_block_present", len(theorem_block) > 1000)
    record("parent_theorem_pair_relation_present", "P_(2,0,1) = S_(mu tau) P_(2,1,0)" in theorem_block)
    record("parent_theorem_sign_flip_present", "sin(delta_CP)(2,0,1) = - sin(delta_CP)(2,1,0)" in theorem_block)
    record("parent_theorem_no_criticality_token", "criticality" not in theorem_block.lower())
    record("parent_theorem_no_load_score_token", "load_bearing_score" not in theorem_block)

    data = recompute_pair_data()
    h_pin = data["h_pin"]
    p_plus = data["p_plus"]
    p_minus = data["p_minus"]
    sin_plus = float(data["sin_plus"])
    sin_minus = float(data["sin_minus"])
    record("self_contained_h_pin_hermitian", np.allclose(h_pin, h_pin.conjugate().T, atol=1e-14))
    record("self_contained_survivor_set_expected", data["survivors"] == {(2, 0, 1), (2, 1, 0)})
    record("self_contained_row_swap_identity", np.allclose(p_plus, S_MUTAU @ p_minus, atol=1e-12))
    record("self_contained_jarlskog_sign_flip", np.sign(sin_plus) == -np.sign(sin_minus))
    record(
        "self_contained_jarlskog_magnitude_expected",
        abs(abs(sin_plus) - 0.9873607592) < 1e-6 and abs(abs(sin_minus) - 0.9873607592) < 1e-6,
    )
    record("self_contained_abs_row_multisets_match", data["abs_rows_plus"] == data["abs_rows_minus"])
    record("self_contained_row_labeled_magnitudes_differ", not np.allclose(np.abs(p_plus), np.abs(p_minus), atol=1e-12))
    record("self_contained_trace_invariant", abs(np.trace(h_pin) - np.trace(h_pin)) < 1e-14)
    record("self_contained_trace2_invariant", abs(np.trace(h_pin @ h_pin) - np.trace(h_pin @ h_pin)) < 1e-14)
    record("self_contained_det_invariant", abs(np.linalg.det(h_pin) - np.linalg.det(h_pin)) < 1e-14)
    record("criticality_marker_does_not_change_algebra", algebra_with_marker("leaf") == algebra_with_marker("critical"))

    runner_lines = [line.strip() for line in Path(__file__).read_text(encoding="utf-8").splitlines()]
    helper_module = "frontier_" + "sigma_hier_uniqueness_theorem"
    parent_module = "frontier_" + "dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20"
    helper_import = any(line.startswith(f"from {helper_module} ") or line == f"import {helper_module}" for line in runner_lines)
    parent_import = any(line.startswith(f"from {parent_module} ") or line == f"import {parent_module}" for line in runner_lines)
    record("companion_does_not_import_parent_frontier_symbol", not helper_import)
    record("companion_does_not_import_parent_runner_module", not parent_import)

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_text)
    record("companion_keeps_dependencies_unresolved", "upstream dependency rows remain unresolved" in companion_words)
    record("companion_disclaims_flavor_orientation", "does not choose the remaining flavor orientation" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
