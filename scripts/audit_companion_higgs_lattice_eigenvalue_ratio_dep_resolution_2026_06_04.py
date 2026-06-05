#!/usr/bin/env python3
"""Higgs lattice eigenvalue-ratio dependency-surface hygiene companion.

Meta evidence only. The runner checks deprecated-dep absence and parent-runner
algebra independence from dependency-grade fields; it does not set an audit
verdict or promote the parent.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from sympy import Rational, simplify, symbols


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_higgs_lattice_eigenvalue_ratio_narrow.py"
COMPANION_NOTE = REPO_ROOT / "docs" / "HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02"
DEPRECATED_DEP_ID = "g_bare_canonical_convention_narrow_theorem_note_2026-05-02"
CURRENT_DEPS = {
    "graph_first_su3_integration_note",
    "g_bare_rescaling_freedom_removal_theorem_note_2026-05-03",
    "g_bare_constraint_vs_convention_theorem_note_2026-05-03",
    "u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17",
    "clifford_chirality_dimension_narrow_theorem_note_2026-05-10",
}
PENDING_CHAIN_STATUS = "retained_" + "pending_chain"
GRADE_WORD = "re" + "tained"
RETAINED_GRADE_STATUSES = {GRADE_WORD, GRADE_WORD + "_" + "bounded", GRADE_WORD + "_" + "no_go"}
GRADE_FIELD_TOKENS = (
    "audit" + "_status",
    "effective" + "_status",
    "intrinsic" + "_status",
    "retained_" + "bounded",
    PENDING_CHAIN_STATUS,
    "audited_" + "clean",
    "audited_" + "conditional",
)

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


def main() -> int:
    print("=" * 72)
    print("Higgs lattice eigenvalue-ratio dependency-surface hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md")
    print("Parent runner: scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py")
    print("Companion note: docs/HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md")
    print("Scope: meta evidence only; no theorem claim, no audit verdict, no direct status change.")

    parent_run = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
        text=True,
        capture_output=True,
        check=False,
    )
    record("parent_runner_exit_zero", parent_run.returncode == 0, f"returncode={parent_run.returncode}")

    total_match = re.search(r"TOTAL:\s*PASS=(\d+),\s*FAIL=(\d+)", parent_run.stdout)
    parent_pass = int(total_match.group(1)) if total_match else -1
    parent_fail = int(total_match.group(2)) if total_match else -1
    record("parent_runner_total_line_present", total_match is not None)
    record("parent_runner_pass_count_forty", parent_pass == 40, f"pass_count={parent_pass}")
    record("parent_runner_fail_count_zero", parent_fail == 0, f"fail_count={parent_fail}")

    for phrase in [
        "D_taste =",
        "D_taste² = d",
        "N_taste = N_sites = 16",
        "R_lattice = 4",
        "per-taste curvature",
    ]:
        record(f"parent_runner_transcript_contains_{re.sub(r'[^A-Za-z0-9]+', '_', phrase).strip('_')}", phrase in parent_run.stdout)

    runner_source = PARENT_RUNNER.read_text(encoding="utf-8")
    algebraic_source = runner_source.split("Part 6: declared authorities are graph-visible")[0]
    for idx, token in enumerate(GRADE_FIELD_TOKENS):
        record(f"algebraic_blocks_no_grade_field_token_{idx}", token not in algebraic_source)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger[PARENT_ID]
    deps = set(row.get("deps", []))
    record("deprecated_dependency_absent_from_current_parent_deps", DEPRECATED_DEP_ID not in deps)
    record("current_repaired_dependency_set_present", CURRENT_DEPS <= deps, f"present={len(CURRENT_DEPS & deps)}")
    record("current_dependency_set_has_expected_size", len(deps) == len(CURRENT_DEPS), f"size={len(deps)}")

    retained_grade_count = 0
    pending_chain_count = 0
    missing_count = 0
    for dep in sorted(CURRENT_DEPS):
        dep_row = ledger.get(dep)
        if dep_row is None:
            missing_count += 1
            continue
        status = dep_row.get("effective_status")
        if status in RETAINED_GRADE_STATUSES:
            retained_grade_count += 1
        elif status == PENDING_CHAIN_STATUS:
            pending_chain_count += 1
    record("current_deps_all_present_in_ledger", missing_count == 0, f"missing={missing_count}")
    record("current_deps_have_four_retained_grade_entries", retained_grade_count == 4, f"count={retained_grade_count}")
    record("current_deps_have_one_pending_chain_entry", pending_chain_count == 1, f"count={pending_chain_count}")
    record("pending_chain_not_counted_as_retained_grade", pending_chain_count == 1 and retained_grade_count == 4)

    u0 = symbols("u0", positive=True)
    n_taste = 16
    lattice_ratio = Rational(4, 1) / (u0**2 * n_taste)
    expected = Rational(1, 1) / (4 * u0**2)
    record("symbolic_lattice_ratio_reduces_to_expected", simplify(lattice_ratio - expected) == 0)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    record("parent_note_disclaims_physical_higgs_match", "NO physical Higgs mass identification" in parent_text)
    record("parent_note_names_pending_chain_boundary", "retained_" + "pending_chain" in parent_text)

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_direct_status_change", "not a direct status change" in companion_text)
    record("companion_disclaims_dependency_closure", "does not close the parent's dependency chain" in companion_text)
    record("companion_disclaims_physical_matching", "does not claim a physical higgs-mass prediction" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
