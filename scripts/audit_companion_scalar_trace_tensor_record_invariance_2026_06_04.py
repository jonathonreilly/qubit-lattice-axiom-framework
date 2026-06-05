#!/usr/bin/env python3
"""Scalar-trace tensor record-invariance hygiene.

Meta evidence only. The runner checks that the parent scalar-trace witness is
unchanged by the Record axiom adoption and keeps the parent helper-dependency
boundary explicit.
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
PARENT_NOTE = REPO_ROOT / "docs" / "SCALAR_TRACE_TENSOR_NO_GO_NOTE.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_scalar_trace_tensor_nogo.py"
COMPANION_NOTE = REPO_ROOT / "docs" / "SCALAR_TRACE_TENSOR_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "scalar_trace_tensor_no_go_note"
EXPECTED_NOTE_HASH = "da00887dcb2d49196ada4b8049f15aa2aade2028fdf94ef77045789303ed148f"
EXPECTED_RUNNER_HASH = "5ce8dce53260e73bdaf23731c97381ef219d62319484ed0953224e0ce72427f9"
EXPECTED_RUNNER_PATH = "scripts/frontier_scalar_trace_tensor_nogo.py"
EXPECTED_CLAIM_TYPE = "bounded_theorem"
EXPECTED_CRITICALITY = "medium"
EXPECTED_LOAD = 7.172
EXPECTED_DEPS = {
    "tensorial_einstein_regge_completion_probe_helper_note_2026-04-14",
    "one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13",
    "coarse_grained_exterior_law_helper_note_2026-04-14",
}
EXPECTED_HELPER = {"scripts/_frontier_loader.py"}
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


def parent_tally(stdout: str) -> tuple[int, int, int] | None:
    match = re.search(r"PASS=(\d+)\s+FAIL=(\d+)\s+TOTAL=(\d+)", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


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
    lines = []
    for line in stdout.splitlines():
        if line.startswith("Elapsed"):
            continue
        lines.append(line)
    return "\n".join(lines)


def main() -> int:
    print("=" * 72)
    print("Scalar-trace tensor record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/SCALAR_TRACE_TENSOR_NO_GO_NOTE.md")
    print("Parent runner: scripts/frontier_scalar_trace_tensor_nogo.py")
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
    record("parent_helper_loader_declared", set(row.get("helper_runner_paths", [])) == EXPECTED_HELPER)
    record("parent_current_row_unresolved", row.get(STATUS_FIELD) == PENDING_STATUS)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    start = parent_text.find("## Purpose")
    end = parent_text.find("## Imported authorities", start)
    load_bearing = parent_text[start:end]
    load_bearing_words = " ".join(load_bearing.split())
    record("parent_load_bearing_block_present", len(load_bearing) > 1000)
    for idx, phrase in enumerate(
        (
            "scalar shell trace / Schur data",
            "shift-vector mode",
            "traceless spatial shear mode",
            "tensorial Einstein channels",
            "genuinely tensor-valued",
        )
    ):
        record(f"parent_load_bearing_contains_witness_phrase_{idx}", phrase in load_bearing_words)
    record_terms = ("record axiom", "record" + "-axiom", "recorded information")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    parent_false = run_parent(record_asserted=False)
    parent_true = run_parent(record_asserted=True)
    tally = parent_tally(parent_false.stdout)
    record("parent_runner_exit_zero", parent_false.returncode == 0, f"returncode={parent_false.returncode}")
    record("parent_runner_tally_present", tally is not None)
    if tally:
        record("parent_runner_pass_count_six", tally[0] == 6, f"pass_count={tally[0]}")
        record("parent_runner_fail_count_zero", tally[1] == 0, f"fail_count={tally[1]}")
        record("parent_runner_total_count_six", tally[2] == 6, f"total={tally[2]}")
    else:
        record("parent_runner_pass_count_six", False)
        record("parent_runner_fail_count_zero", False)
        record("parent_runner_total_count_six", False)
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
    record("companion_keeps_helper_boundary", "does not discharge the parent helper-dependency boundary" in companion_text)
    record("companion_marks_axioms_not_support", "not verdict-grade support" in companion_words)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
