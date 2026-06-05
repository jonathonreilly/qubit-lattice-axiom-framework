#!/usr/bin/env python3
"""N_F trace-space bounded obstruction record-invariance hygiene.

Meta evidence only. The runner checks that the parent trace-space obstruction
is unchanged by the Record axiom adoption and keeps the dependency boundary
explicit.
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
PARENT_NOTE = REPO_ROOT / "docs" / "N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "cl3_n_f_v3_trace_check_2026-05-07_w2binary.py"
COMPANION_NOTE = (
    REPO_ROOT / "docs" / "N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "n_f_trace_space_bounded_obstruction_note_2026-05-07_w2binary"
EXPECTED_NOTE_HASH = "a2e3edf03c32f29c61157ba7b6ea9de5c924154bb9679623dd845e41b03bb1ae"
EXPECTED_RUNNER_HASH = "b757a00d1fa7ca37c9dc145366a350fc52cf6875bf0793b3b529bd055cf446b7"
EXPECTED_RUNNER_PATH = "scripts/cl3_n_f_v3_trace_check_2026-05-07_w2binary.py"
EXPECTED_CLAIM_TYPE = "open_gate"
EXPECTED_CRITICALITY = "high"
EXPECTED_LOAD = 10.179
EXPECTED_DEPS = {
    "n_f_bounded_z2_reduction_theorem_note_2026-05-07_w2",
    "cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02",
    "cl3_color_automorphism_theorem",
    "g_bare_constraint_vs_convention_restatement_note_2026-05-07",
    "g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07",
    "su3_casimir_fundamental_theorem_note_2026-05-02",
    "g_bare_structural_normalization_theorem_note_2026-04-18",
}
STATUS_FIELD = "effective" + "_status"
PENDING_STATUS = "un" + "audited"
PENDING_CHAIN = "retained_" + "pending_chain"
EXPECTED_INVALIDATION_PREFIX = "dep_weakened:cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02:"

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
    match = re.search(r"TOTAL\s+:\s+PASS\s+=\s+(\d+),\s+FAIL\s+=\s+(\d+)", stdout)
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
    print("N_F trace-space bounded obstruction record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md")
    print("Parent runner: scripts/cl3_n_f_v3_trace_check_2026-05-07_w2binary.py")
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
    record("parent_current_row_unresolved", row.get(STATUS_FIELD) == PENDING_STATUS)

    previous = row.get("previous_audits", []) or []
    record("parent_has_previous_review_snapshot", bool(previous))
    if previous:
        reason = str(previous[0].get("invalidation_reason", ""))
        record("previous_invalidation_was_dependency_state_change", reason.startswith(EXPECTED_INVALIDATION_PREFIX))
    else:
        record("previous_invalidation_was_dependency_state_change", False)

    dep_states = [ledger[dep].get(STATUS_FIELD) for dep in sorted(EXPECTED_DEPS)]
    record("parent_dependency_surface_still_not_closed", any(state in {PENDING_STATUS, PENDING_CHAIN} for state in dep_states))

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    start = parent_text.find("## Claim")
    end = parent_text.find("## Honest scope", start)
    load_bearing = parent_text[start:end]
    load_bearing_words = " ".join(load_bearing.split())
    record("parent_load_bearing_block_present", len(load_bearing) > 1000)
    for idx, phrase in enumerate(
        (
            "binary admission",
            "Tr_V / Tr_{V_3} = 2",
            "dim(V_fiber)",
            "SU(2) sub of color-SU(3)",
            "per-site Cl(3) bivector SU(2)",
            "not derived from Cl(3) + Z^3 primitives",
        )
    ):
        record(f"parent_load_bearing_contains_obstruction_phrase_{idx}", phrase in load_bearing_words)
    record_terms = ("record axiom", "record" + "-axiom", "recorded information")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    parent_false = run_parent(record_asserted=False)
    parent_true = run_parent(record_asserted=True)
    total = parent_total(parent_false.stdout)
    record("parent_runner_exit_zero", parent_false.returncode == 0, f"returncode={parent_false.returncode}")
    record("parent_runner_total_present", total is not None)
    if total:
        record("parent_runner_pass_count_twenty_nine", total[0] == 29, f"pass_count={total[0]}")
        record("parent_runner_fail_count_zero", total[1] == 0, f"fail_count={total[1]}")
    else:
        record("parent_runner_pass_count_twenty_nine", False)
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
    record("companion_keeps_dependency_boundary", "does not resolve the parent dependency boundary" in companion_text)
    record("companion_marks_axioms_not_support", "not verdict-grade support" in companion_words)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
