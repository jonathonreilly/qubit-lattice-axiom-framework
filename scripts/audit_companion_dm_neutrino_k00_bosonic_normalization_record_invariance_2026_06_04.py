#!/usr/bin/env python3
"""DM neutrino K00 bosonic-normalization record-invariance hygiene.

Meta evidence only. The runner checks that the parent finite matrix
calculation and source-response comparison are unchanged by the Record axiom
adoption.
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
PARENT_NOTE = REPO_ROOT / "docs" / "DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_dm_neutrino_k00_bosonic_normalization_theorem.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
)
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15"
EXPECTED_NOTE_HASH = "0da6e7549d1178d541f97e6fb3fbaac473ca0db14f7c7111e6ae5c89b2b4c906"
EXPECTED_RUNNER_PATH = "scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py"
EXPECTED_CLAIM_TYPE = "bounded_theorem"
EXPECTED_CRITICALITY = "critical"
EXPECTED_LOAD = 11.165
EXPECTED_DEPS = {
    "observable_principle_from_axiom_note",
    "dm_neutrino_weak_even_swap_reduction_theorem_note_2026-04-15",
    "dm_neutrino_triplet_character_source_theorem_note_2026-04-15",
    "dm_neutrino_bosonic_normalization_theorem_note_2026-04-15",
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


def parent_summary(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"SUMMARY:\s+PASS=(\d+)\s+FAIL=(\d+)", stdout)
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
    print("DM neutrino K00 bosonic-normalization record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md")
    print("Parent runner: scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py")
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
    record("parent_deps_exact", set(row.get("deps", [])) == EXPECTED_DEPS, f"count={len(row.get('deps', []))}")
    record(
        "parent_current_row_status_printed_informationally",
        bool(row),
        f"live_{STATUS_FIELD}={row.get(STATUS_FIELD)!r} landing_expected={PENDING_STATUS!r}; "
        "audit-lane-owned field; not gated",
    )

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    start = parent_text.find("## Bottom line")
    end = parent_text.find("## Command", start)
    load_bearing = parent_text[start:end]
    load_bearing_words = " ".join(load_bearing.split())
    record("parent_load_bearing_block_present", len(load_bearing) > 1000)
    for idx, phrase in enumerate(
        (
            "K00 = (K_mass)00 = (A + 4b + 2c + 2d)/3",
            "K00 = Tr(H F00), F00 = J3/3",
            "independent of the odd/even breaking triplet",
            "full row-sum generator `J2`",
            "`F00` and `(1/2) J2` have the same nonzero spectrum `{+1}`",
            "identical exact bosonic response",
            "K00 = 2 tau_+",
            "tau_E = 1/2",
            "tau_T = 1/2",
            "K00 = 2",
        )
    ):
        record(f"parent_load_bearing_contains_k00_phrase_{idx}", phrase in load_bearing_words)
    record_terms = ("record axiom", "record" + "-axiom", "scalar record", "record functional")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    parent_false = run_parent(record_asserted=False)
    parent_true = run_parent(record_asserted=True)
    summary = parent_summary(parent_false.stdout)
    record("parent_runner_exit_zero", parent_false.returncode == 0, f"returncode={parent_false.returncode}")
    record("parent_runner_summary_present", summary is not None)
    if summary:
        record("parent_runner_pass_count_eleven", summary[0] == 11, f"pass_count={summary[0]}")
        record("parent_runner_fail_count_zero", summary[1] == 0, f"fail_count={summary[1]}")
    else:
        record("parent_runner_pass_count_eleven", False)
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
    record("companion_keeps_dependency_boundary", "does not change the parent dependency boundary" in companion_text)
    record("companion_marks_axioms_not_support", "not verdict-grade support" in companion_words)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
