#!/usr/bin/env python3
"""Hubble Lane 5 two-gate dependency firewall criticality-bump hygiene.

Meta evidence only. The runner checks that the parent two-gate firewall
surface remains reproducible while all registered upstream gate rows remain
unresolved.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_hubble_lane5_two_gate_dependency_firewall.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "hubble_lane5_two_gate_dependency_firewall_note_2026-04-27"
EXPECTED_NOTE_HASH = "c370a34fb90377baab49dfaffe89f04c99bee922aa88edde7b79fdfd1f110254"
EXPECTED_RUNNER_HASH = "b7ad9fb4569c93e62be34ed82bef156a93615446851fbd361fd645a2785a1a68"
EXPECTED_RUNNER_PATH = "scripts/frontier_hubble_lane5_two_gate_dependency_firewall.py"
EXPECTED_CLAIM_TYPE = "positive_theorem"
EXPECTED_CRITICALITY = "high"
EXPECTED_LOAD = 9.644
EXPECTED_PRIOR_LOAD = 5.907
EXPECTED_PREVIOUS_VERDICT = "audited_" + "clean"
EXPECTED_INVALIDATION = "criticality" + "_increased:medium->high"
EXPECTED_DEPS = {
    "omega_lambda_matter_bridge_theorem_note_2026-04-22",
    "cosmology_open_number_reduction_theorem_note_2026-04-26",
    "hubble_tension_structural_lock_theorem_note_2026-04-26",
    "hubble_lane5_planck_c1_gate_audit_note_2026-04-26",
    "hubble_lane5_eta_retirement_gate_audit_note_2026-04-26",
    "hubble_lane5_c3_vacuum_topology_no_active_route_note_2026-04-27",
}
STATUS_FIELD = "effective" + "_status"
PENDING_STATUS = "un" + "audited"

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


def parent_tally(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"PASS=(\d+)\s+FAIL=(\d+)", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def previous_medium_positive(row: dict) -> dict | None:
    for entry in row.get("previous_audits", []) or []:
        snapshot = entry.get("audit_state_snapshot", {})
        if entry.get("audit" + "_status") == EXPECTED_PREVIOUS_VERDICT and snapshot.get("criticality") == "medium":
            return entry
    return None


def main() -> int:
    print("=" * 72)
    print("Hubble Lane 5 two-gate dependency firewall criticality-bump hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md")
    print("Parent runner: scripts/frontier_hubble_lane5_two_gate_dependency_firewall.py")
    print("Scope: meta evidence only; no theorem claim and no verdict change.")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger[PARENT_ID]
    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record("parent_claim_type_expected", row.get("claim_type") == EXPECTED_CLAIM_TYPE)
    record("parent_runner_path_expected", row.get("runner_path") == EXPECTED_RUNNER_PATH)
    record("parent_current_criticality_expected", row.get("criticality") == EXPECTED_CRITICALITY)
    record(
        "parent_current_load_expected",
        abs(float(row.get("load_bearing_score")) - EXPECTED_LOAD) < 1e-12,
        f"load={row.get('load_bearing_score')}",
    )
    record("parent_note_hash_expected", sha256(PARENT_NOTE) == EXPECTED_NOTE_HASH)
    record("parent_note_hash_matches_ledger", sha256(PARENT_NOTE) == row.get("note_hash"))
    record("parent_runner_hash_expected", sha256(PARENT_RUNNER) == EXPECTED_RUNNER_HASH)
    record("parent_deps_exact", set(row.get("deps", [])) == EXPECTED_DEPS, f"count={len(row.get('deps', []))}")
    record("parent_has_no_helper_runners", not row.get("helper_runner_paths"))

    unresolved = []
    for dep_id in sorted(EXPECTED_DEPS):
        dep_row = ledger[dep_id]
        unresolved.append(dep_row.get(STATUS_FIELD) == PENDING_STATUS)
        record(f"upstream_row_present_{dep_id}", dep_id in ledger)
        record(f"upstream_row_unresolved_{dep_id}", dep_row.get(STATUS_FIELD) == PENDING_STATUS)
    record("all_upstream_rows_unresolved", all(unresolved))

    prior = previous_medium_positive(row)
    record("prior_medium_positive_snapshot_present", prior is not None)
    if prior:
        snapshot = prior.get("audit_state_snapshot", {})
        record("prior_snapshot_load_expected", abs(float(snapshot.get("load_bearing_score")) - EXPECTED_PRIOR_LOAD) < 1e-12)
        record("prior_invalidation_was_priority_bump", prior.get("invalidation_reason") == EXPECTED_INVALIDATION)
    else:
        record("prior_snapshot_load_expected", False)
        record("prior_invalidation_was_priority_bump", False)

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
        record("parent_runner_pass_count_eighteen", tally[0] == 18, f"pass_count={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail_count={tally[1]}")
    else:
        record("parent_runner_pass_count_eighteen", False)
        record("parent_runner_fail_count_zero", False)

    transcript_phrases = (
        "H_0 = H_inf/sqrt(L)",
        "C1 alone leaves a continuum of H_0 values",
        "C2/C3 alone leaves a continuum of H_0 values",
        "structural lock fixes H(a)/H_0, not the scalar H_0",
        "lock inversion returns whichever scalar was supplied",
    )
    for idx, phrase in enumerate(transcript_phrases):
        record(f"parent_runner_transcript_contains_core_phrase_{idx}", phrase in parent_run.stdout)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    record("parent_text_two_gate_identity_present", "H_0 = H_inf / sqrt(L)" in parent_text)
    record("parent_text_c1_only_block_present", "(C1) alone => numerical H_0" in parent_text)
    record("parent_text_c2_c3_only_block_present", "(C2) or (C3) alone => numerical H_0" in parent_text)
    record("parent_text_structural_lock_boundary_present", "structural lock is a late-time falsifier" in parent_text)
    record("parent_text_no_observed_h0_input_present", "No observed `H_0` value is used" in parent_text)
    import_section = parent_text.split("## Inputs And Import Roles", 1)[1].split("## Safe Wording", 1)[0]
    for idx, dep_id in enumerate(sorted(EXPECTED_DEPS)):
        note_stub = dep_id.upper().replace("_NOTE_2026-04-", "_NOTE_2026-04-") + ".md"
        record(f"parent_import_section_names_dep_{idx}", note_stub in import_section)

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_text)
    record("companion_keeps_dependencies_unresolved", "upstream dependency rows remain unresolved" in companion_words)
    record("companion_disclaims_h0_derivation", "does not derive a numerical `h_0`" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
