#!/usr/bin/env python3
"""Hadron Lane 1 confinement-to-mass firewall record-invariance hygiene.

Meta evidence only. The runner checks that the parent firewall arithmetic and
dependency-boundary structure are unchanged by the Record axiom adoption.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_hadron_lane1_confinement_to_mass_firewall.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "hadron_lane1_confinement_to_mass_firewall_note_2026-04-27"
EXPECTED_RUNNER_PATH = "scripts/frontier_hadron_lane1_confinement_to_mass_firewall.py"
REQUIRED_DEPS = {
    "g_bare_derivation_note",
    "staggered_dirac_realization_gate_note_2026-05-03",
    "quark_lane3_bounded_companion_retention_firewall_note_2026-04-27",
}
STATUS_FIELDS = ("effective" + "_status", "audit" + "_status")

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


def parent_total(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"PASS=(\d+)\s+FAIL=(\d+)", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def run_parent(record_asserted: bool) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO_ROOT / "scripts")
    env["CL3_RECORD_ASSERTED"] = "1" if record_asserted else "0"
    return subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        env=env,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )


def normalized_parent_output(stdout: str) -> str:
    return "\n".join(line for line in stdout.splitlines() if not line.startswith("Elapsed"))


def main() -> int:
    print("=" * 72)
    print("Hadron Lane 1 confinement-to-mass firewall record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md")
    print("Parent runner: scripts/frontier_hadron_lane1_confinement_to_mass_firewall.py")
    print("Scope: meta evidence only; no theorem claim and no verdict change.")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger.get(PARENT_ID, {})
    deps = row.get("deps", [])
    deps_set = set(deps) if isinstance(deps, list) else set()
    record("parent_note_exists", PARENT_NOTE.is_file())
    record("parent_runner_exists", PARENT_RUNNER.is_file())
    record("parent_ledger_row_exists", bool(row))
    record("parent_claim_type_field_present", bool(row.get("claim_type")), f"claim_type={row.get('claim_type')}")
    record("parent_runner_path_expected", row.get("runner_path") == EXPECTED_RUNNER_PATH)
    record(
        "parent_current_criticality_present",
        bool(row.get("criticality")),
        f"criticality={row.get('criticality')}",
    )
    try:
        load_value = float(row.get("load_bearing_score"))
        load_present = True
    except (TypeError, ValueError):
        load_value = row.get("load_bearing_score")
        load_present = False
    record("parent_current_load_present", load_present, f"load={load_value}")
    row_note_hash = row.get("note_hash")
    record("parent_note_hash_field_present", isinstance(row_note_hash, str) and len(row_note_hash) == 64)
    record("parent_note_hash_matches_ledger", sha256(PARENT_NOTE) == row.get("note_hash"))
    record("parent_deps_field_present", bool(deps_set), f"count={len(deps_set)}")
    record(
        "parent_deps_include_required_sources",
        REQUIRED_DEPS.issubset(deps_set),
        f"missing={sorted(REQUIRED_DEPS - deps_set)}",
    )
    record(
        "parent_deps_omit_record_specific_sources",
        all("record" not in dep.lower() for dep in deps_set),
        f"count={len(deps_set)}",
    )
    record(
        "parent_current_status_fields_present",
        all(bool(row.get(field)) for field in STATUS_FIELDS),
        ", ".join(f"{field}={row.get(field)}" for field in STATUS_FIELDS),
    )

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    start = parent_text.find("## Theorem")
    end = parent_text.find("## Hypothesis set", start)
    load_bearing = parent_text[start:end]
    load_bearing_words = " ".join(load_bearing.split())
    record("parent_load_bearing_block_present", len(load_bearing) > 1000)
    for idx, phrase in enumerate(
        (
            "m_H = c_H * sqrt(sigma)",
            "c_pi ~= 0.29",
            "c_p ~= 2.02",
            "GMOR",
            "hadronic-scale running/matching",
            "spectral coefficient",
            "standard lattice-QCD methodology exists",
            "Safe Wording",
        )
    ):
        record(f"parent_load_bearing_contains_firewall_phrase_{idx}", phrase in load_bearing_words)
    record_terms = ("record axiom", "record" + "-axiom", "scalar record")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    parent_false = run_parent(record_asserted=False)
    parent_true = run_parent(record_asserted=True)
    total = parent_total(parent_false.stdout)
    record("parent_runner_exit_zero", parent_false.returncode == 0, f"returncode={parent_false.returncode}")
    record("parent_runner_total_present", total is not None)
    if total:
        record("parent_runner_pass_count_at_least_original", total[0] >= 16, f"pass_count={total[0]}")
        record("parent_runner_fail_count_zero", total[1] == 0, f"fail_count={total[1]}")
    else:
        record("parent_runner_pass_count_at_least_original", False)
        record("parent_runner_fail_count_zero", False)
    record("record_marker_true_exit_zero", parent_true.returncode == 0, f"returncode={parent_true.returncode}")
    record(
        "record_marker_does_not_change_parent_output",
        normalized_parent_output(parent_false.stdout) == normalized_parent_output(parent_true.stdout),
    )

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_text)
    record("companion_keeps_dependency_boundary", "dependency-boundary surface" in companion_text)
    record("companion_marks_axioms_not_support", "not verdict-grade support" in companion_words)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
