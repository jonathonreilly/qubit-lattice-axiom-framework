#!/usr/bin/env python3
"""Axiom-first lattice Noether record-invariance hygiene.

Meta evidence only. The runner checks that the parent finite
staggered-carrier Noether surface is unchanged by the Record axiom adoption.
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
PARENT_NOTE = REPO_ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "axiom_first_lattice_noether_check.py"
COMPANION_NOTE = REPO_ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "axiom_first_lattice_noether_theorem_note_2026-04-29"
EXPECTED_RUNNER_PATH = "scripts/axiom_first_lattice_noether_check.py"
REQUIRED_DEPS = {
    "minimal_axioms",
    "staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16",
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


def parent_summary(stdout: str) -> tuple[int, int] | None:
    match = re.search(r"PASSED:\s+(\d+)/(\d+)", stdout)
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
    print("Axiom-first lattice Noether record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md")
    print("Parent runner: scripts/axiom_first_lattice_noether_check.py")
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
    start = parent_text.find("## Statement")
    end = parent_text.find("## Hypothesis-set summary", start)
    load_bearing = parent_text[start:end]
    load_bearing_words = " ".join(load_bearing.split())
    record("parent_load_bearing_block_present", len(load_bearing) > 4000)
    for idx, phrase in enumerate(
        (
            "`(2Z)^3` sublattice two-step Ward identity",
            "Fermion-number current",
            "Symmetry condition",
            "commutes with `M_KS`",
            "bilateral form (5)",
            "on shell",
            "central two-step generator",
            "localized Ward identity",
            "one-site shifts are not pure translations",
            "support-only",
        )
    ):
        record(f"parent_load_bearing_contains_noether_phrase_{idx}", phrase in load_bearing_words)
    record_terms = ("record axiom", "record" + "-axiom", "scalar record", "record functional")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    parent_false = run_parent(record_asserted=False)
    parent_true = run_parent(record_asserted=True)
    summary = parent_summary(parent_false.stdout)
    record("parent_runner_exit_zero", parent_false.returncode == 0, f"returncode={parent_false.returncode}")
    record("parent_runner_summary_present", summary is not None)
    if summary:
        record(
            "parent_runner_passed_all_live_exhibits",
            summary[0] == summary[1] and summary[1] >= 7,
            f"passed={summary[0]}/{summary[1]}",
        )
    else:
        record("parent_runner_passed_all_live_exhibits", False)
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
