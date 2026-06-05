#!/usr/bin/env python3
"""BZ (2*pi)^3 record-invariance hygiene.

Meta evidence only. The runner checks that the parent BZ-volume arithmetic is
unchanged by the Record axiom adoption and does not treat axiom premises as
verdict-grade support.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
import sys
from pathlib import Path

import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py"
COMPANION_NOTE = REPO_ROOT / "docs" / "BZ_VOLUME_TWO_PI_CUBED_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26"
EXPECTED_NOTE_HASH = "905bdd9d430195ae221b044af92a7dca7fecbc696285b0eb31e3722463b503c4"
EXPECTED_RUNNER_HASH = "92e391d4dd077cbfa66c5fa1ae71b232dc600324021a04f90a5a8996a43bb2b2"
EXPECTED_RUNNER_PATH = "scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py"
EXPECTED_CLAIM_TYPE = "bounded_theorem"
EXPECTED_CRITICALITY = "leaf"
EXPECTED_LOAD = 1.5
EXPECTED_DEP = "minimal_axioms"
EXPECTED_PREVIOUS_VERDICT = "audited_" + "clean"
EXPECTED_INVALIDATION_PREFIX = "axiom" + "_premise_changed:minimal_axioms:"
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
    match = re.search(r"TOTAL\s+:\s+PASS\s+=\s+(\d+),\s+FAIL\s+=\s+(\d+)", stdout)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def previous_positive(row: dict) -> dict | None:
    for entry in row.get("previous_audits", []) or []:
        if entry.get("audit" + "_status") == EXPECTED_PREVIOUS_VERDICT:
            return entry
    return None


def bz_values(record_asserted: bool) -> tuple[sp.Expr, sp.Expr, float]:
    _ = record_asserted
    volume = (2 * sp.pi) ** 3
    haar_density = sp.simplify(1 / volume)
    numeric_volume = float(volume.evalf())
    return volume, haar_density, numeric_volume


def main() -> int:
    print("=" * 72)
    print("BZ two-pi-cubed record-invariance hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md")
    print("Parent runner: scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py")
    print("Scope: meta evidence only; no theorem claim and no verdict change.")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = ledger[PARENT_ID]
    dep_row = ledger[EXPECTED_DEP]
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
    record("parent_has_only_minimal_axioms_dep", row.get("deps") == [EXPECTED_DEP])
    record("minimal_axioms_row_is_meta", dep_row.get("claim_type") == "meta")
    record("parent_current_row_unresolved", row.get(STATUS_FIELD) == PENDING_STATUS)

    prior = previous_positive(row)
    record("prior_positive_snapshot_present", prior is not None)
    if prior:
        record("prior_invalidation_was_premise_update", str(prior.get("invalidation_reason", "")).startswith(EXPECTED_INVALIDATION_PREFIX))
    else:
        record("prior_invalidation_was_premise_update", False)

    parent_run = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    total = parent_total(parent_run.stdout)
    record("parent_runner_exit_zero", parent_run.returncode == 0, f"returncode={parent_run.returncode}")
    record("parent_runner_total_present", total is not None)
    if total:
        record("parent_runner_pass_count_fifty_five", total[0] == 55, f"pass_count={total[0]}")
        record("parent_runner_fail_count_zero", total[1] == 0, f"fail_count={total[1]}")
    else:
        record("parent_runner_pass_count_fifty_five", False)
        record("parent_runner_fail_count_zero", False)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    theorem_start = parent_text.find("## Theorem")
    theorem_end = parent_text.find("## Honest assessment", theorem_start)
    load_bearing = parent_text[theorem_start:theorem_end]
    record("parent_load_bearing_block_present", len(load_bearing) > 1000)
    for idx, phrase in enumerate(("`Z³`", "`T³`", "Pontryagin dual", "Haar normalization", "vol_Lebesgue([-π, π]³)")):
        record(f"parent_load_bearing_contains_lattice_haar_phrase_{idx}", phrase in load_bearing)
    record_terms = ("record axiom", "record" + "-axiom", "recorded information")
    record("parent_load_bearing_omits_record_axiom_terms", all(term not in load_bearing.lower() for term in record_terms))

    volume, density, numeric_volume = bz_values(record_asserted=False)
    volume_with_record, density_with_record, numeric_volume_with_record = bz_values(record_asserted=True)
    record("direct_volume_exact", sp.simplify(volume - 8 * sp.pi**3) == 0)
    record("direct_haar_density_exact", sp.simplify(density - 1 / (8 * sp.pi**3)) == 0)
    record("direct_volume_numeric_expected", abs(numeric_volume - 248.05021344239853) < 1e-12)
    record("record_marker_does_not_change_volume", sp.simplify(volume - volume_with_record) == 0)
    record("record_marker_does_not_change_density", sp.simplify(density - density_with_record) == 0)
    record("record_marker_does_not_change_numeric_volume", abs(numeric_volume - numeric_volume_with_record) < 1e-15)

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_verdict_change", "not a verdict change" in companion_text)
    record("companion_keeps_parent_unclosed", "does not close the parent after the premise update" in companion_text)
    record("companion_marks_axioms_not_support", "not verdict-grade support" in companion_words)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
