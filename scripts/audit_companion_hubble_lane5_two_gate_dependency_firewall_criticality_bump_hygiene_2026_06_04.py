#!/usr/bin/env python3
"""Hubble Lane 5 two-gate dependency firewall criticality-bump hygiene.

Meta evidence only. The runner checks that the parent two-gate firewall
surface remains reproducible while all registered upstream gate rows remain
visible as dependencies. Audit-lane values are printed as live metadata only,
not used as gates.
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
EXPECTED_RUNNER_PATH = "scripts/frontier_hubble_lane5_two_gate_dependency_firewall.py"
REQUIRED_DEPS = {
    "omega_lambda_matter_bridge_theorem_note_2026-04-22",
    "cosmology_open_number_reduction_theorem_note_2026-04-26",
    "hubble_tension_structural_lock_theorem_note_2026-04-26",
    "hubble_lane5_planck_c1_gate_audit_note_2026-04-26",
    "hubble_lane5_eta_retirement_gate_audit_note_2026-04-26",
    "hubble_lane5_c3_vacuum_topology_no_active_route_note_2026-04-27",
}
STATUS_FIELD = "effective" + "_status"
AUDIT_STATUS_FIELD = "audit" + "_status"

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


def value_present(value: object) -> bool:
    return value is not None and str(value) != ""


def numeric_value_present(value: object) -> bool:
    try:
        float(value)
    except (TypeError, ValueError):
        return False
    return True


def parent_tally(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"PASS=(\d+)\s+FAIL=(\d+)", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def previous_audit_with_snapshot(row: dict) -> dict | None:
    for entry in row.get("previous_audits", []) or []:
        snapshot = entry.get("audit_state_snapshot", {})
        if isinstance(snapshot, dict) and snapshot:
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
    print("Audit-lane fields are informational metadata, not pass/fail targets.")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger.get(PARENT_ID, {})
    record("parent_ledger_row_present", PARENT_ID in ledger)
    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record(
        "parent_claim_type_field_present",
        value_present(row.get("claim_type")),
        f"claim_type={row.get('claim_type')}",
    )
    record("parent_runner_path_expected", row.get("runner_path") == EXPECTED_RUNNER_PATH)
    record(
        "parent_current_criticality_field_present",
        value_present(row.get("criticality")),
        f"criticality={row.get('criticality')}",
    )
    record(
        "parent_current_load_numeric",
        numeric_value_present(row.get("load_bearing_score")),
        f"load={row.get('load_bearing_score')}",
    )
    record(
        "parent_status_fields_present",
        STATUS_FIELD in row and AUDIT_STATUS_FIELD in row,
        f"{STATUS_FIELD}={row.get(STATUS_FIELD)} {AUDIT_STATUS_FIELD}={row.get(AUDIT_STATUS_FIELD)}",
    )
    parent_note_hash = sha256(PARENT_NOTE) if PARENT_NOTE.is_file() else ""
    parent_runner_hash = sha256(PARENT_RUNNER) if PARENT_RUNNER.is_file() else ""
    ledger_note_hash = row.get("note_hash")
    record("parent_note_hash_field_present", value_present(ledger_note_hash))
    record("parent_note_hash_matches_ledger", bool(ledger_note_hash) and parent_note_hash == ledger_note_hash)
    record("parent_runner_hash_computable", len(parent_runner_hash) == 64)
    row_deps = set(row.get("deps", []))
    record(
        "parent_deps_include_required_sources",
        REQUIRED_DEPS.issubset(row_deps),
        f"required={len(REQUIRED_DEPS)} row_deps={len(row_deps)}",
    )
    record(
        "parent_helper_runner_paths_field_present",
        "helper_runner_paths" in row,
        f"count={len(row.get('helper_runner_paths') or [])}",
    )

    dep_rows_present = []
    for dep_id in sorted(REQUIRED_DEPS):
        dep_row = ledger.get(dep_id)
        dep_rows_present.append(dep_row is not None)
        record(f"upstream_row_present_{dep_id}", dep_id in ledger)
        record(
            f"upstream_effective_status_field_present_{dep_id}",
            dep_row is not None and STATUS_FIELD in dep_row,
            f"value={dep_row.get(STATUS_FIELD) if dep_row else None}",
        )
        record(
            f"upstream_audit_status_field_present_{dep_id}",
            dep_row is not None and AUDIT_STATUS_FIELD in dep_row,
            f"value={dep_row.get(AUDIT_STATUS_FIELD) if dep_row else None}",
        )
    record("all_required_upstream_rows_present", all(dep_rows_present))

    prior = previous_audit_with_snapshot(row)
    record("previous_audit_history_present", bool(row.get("previous_audits")))
    record("prior_snapshot_present", prior is not None)
    if prior:
        snapshot = prior.get("audit_state_snapshot", {})
        record(
            "prior_snapshot_load_field_present",
            "load_bearing_score" in snapshot,
            f"load={snapshot.get('load_bearing_score')}",
        )
        record(
            "prior_snapshot_criticality_field_present",
            "criticality" in snapshot,
            f"criticality={snapshot.get('criticality')}",
        )
        record(
            "prior_invalidation_reason_field_present",
            "invalidation_reason" in prior,
            f"reason={prior.get('invalidation_reason')}",
        )
    else:
        record("prior_snapshot_load_field_present", False)
        record("prior_snapshot_criticality_field_present", False)
        record("prior_invalidation_reason_field_present", False)

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
        record("parent_runner_pass_count_at_least_eighteen", tally[0] >= 18, f"pass_count={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail_count={tally[1]}")
    else:
        record("parent_runner_pass_count_at_least_eighteen", False)
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
    for idx, dep_id in enumerate(sorted(REQUIRED_DEPS)):
        note_stub = dep_id.upper().replace("_NOTE_2026-04-", "_NOTE_2026-04-") + ".md"
        record(f"parent_import_section_names_dep_{idx}", note_stub in import_section)

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_text)
    record("companion_records_registered_dependencies", "registered upstream dependency rows" in companion_words)
    record(
        "companion_disclaims_dependency_resolution",
        "does not remove or resolve the upstream dependencies" in companion_words,
    )
    record(
        "companion_marks_audit_values_informational",
        "audit-lane values are informational" in companion_words,
    )
    record("companion_disclaims_h0_derivation", "does not derive a numerical `h_0`" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
