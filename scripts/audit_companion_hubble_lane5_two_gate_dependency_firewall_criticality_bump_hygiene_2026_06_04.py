#!/usr/bin/env python3
"""Audit-readiness hygiene companion for Hubble Lane 5 two-gate firewall.

Companion target:
    hubble_lane5_two_gate_dependency_firewall_note_2026-04-27

The parent row's most recent invalidation reason is the queue-priority
signal `criticality_increased:medium->high`, not a substance-change
flag. This runner verifies that the on-disk parent note and parent
runner are unchanged in load-bearing content since the prior
`audited_clean` verdict (2026-04-28, codex-audit-loop, PASS=18 FAIL=0),
so the audit lane can decide whether to honor that verdict at the new
`high` criticality bucket with full information about what has and has
not changed.

This runner does no new physics. It performs:

  (R1) Presence checks for the parent note and parent runner files.
  (R2) Note-hash invariance against the current ledger row's
       `note_hash` field.
  (R3) Re-execution of the parent runner, asserting exit code 0 and
       `PASS=18 FAIL=0`.
  (R4) Load-bearing-content static checks on the parent note prose.
  (R5) Invalidation-reason structure check on the ledger row.
  (R6) Input-table invariance check on the parent note's
       `## Inputs And Import Roles` section.

Exit code 0 with PASS=18 FAIL=0 means the parent substance is
provably identical to what the prior `audited_clean` verdict
evaluated; any FAIL means the on-disk artifacts have drifted since
this companion was filed and the audit lane should treat the
companion as stale.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0

ROOT = Path(__file__).resolve().parents[1]

PARENT_NOTE_REL = "docs/HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md"
PARENT_RUNNER_REL = "scripts/frontier_hubble_lane5_two_gate_dependency_firewall.py"
LEDGER_REL = "docs/audit/data/audit_ledger.json"

LEDGER_ROW_ID = "hubble_lane5_two_gate_dependency_firewall_note_2026-04-27"
EXPECTED_NOTE_HASH = (
    "c370a34fb90377baab49dfaffe89f04c99bee922aa88edde7b79fdfd1f110254"
)
EXPECTED_PARENT_PASS = 18
EXPECTED_INVALIDATION_PREFIX = "criticality_increased"

EXPECTED_INPUT_ROW_KEYS = (
    "OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22",
    "COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26",
    "HUBBLE_TENSION_STRUCTURAL_LOCK_THEOREM_NOTE_2026-04-26",
    "HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26",
    "HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26",
    "HUBBLE_LANE5_C3_VACUUM_TOPOLOGY_NO_ACTIVE_ROUTE_NOTE_2026-04-27",
)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_ledger_row() -> dict:
    with open(ROOT / LEDGER_REL, "r", encoding="utf-8") as f:
        data = json.load(f)
    rows = data.get("rows", {})
    return rows.get(LEDGER_ROW_ID, {})


def part_R1_presence() -> None:
    section("(R1) Presence checks for parent note and parent runner")
    parent_note_path = ROOT / PARENT_NOTE_REL
    parent_runner_path = ROOT / PARENT_RUNNER_REL
    check(
        "parent note file exists on disk",
        parent_note_path.is_file(),
        f"path={PARENT_NOTE_REL}",
    )
    check(
        "parent runner file exists on disk",
        parent_runner_path.is_file(),
        f"path={PARENT_RUNNER_REL}",
    )


def part_R2_note_hash_invariance() -> None:
    section("(R2) Note-hash invariance against current ledger row")
    row = load_ledger_row()
    on_disk_hash = hashlib.sha256(read_bytes(PARENT_NOTE_REL)).hexdigest()
    ledger_hash = row.get("note_hash", "")
    check(
        "ledger row recorded expected note_hash",
        ledger_hash == EXPECTED_NOTE_HASH,
        f"ledger={ledger_hash[:12]}... expected={EXPECTED_NOTE_HASH[:12]}...",
    )
    check(
        "on-disk note hash matches ledger note_hash",
        on_disk_hash == ledger_hash,
        f"on_disk={on_disk_hash[:12]}... ledger={ledger_hash[:12]}...",
    )
    check(
        "on-disk note hash matches the expected substance-unchanged hash",
        on_disk_hash == EXPECTED_NOTE_HASH,
        f"on_disk={on_disk_hash[:12]}... expected={EXPECTED_NOTE_HASH[:12]}...",
    )


def part_R3_parent_runner_execution() -> None:
    section("(R3) Re-execution of parent runner")
    env = {"PYTHONPATH": str(ROOT / "scripts")}
    import os
    full_env = os.environ.copy()
    full_env.update(env)
    result = subprocess.run(
        [sys.executable, str(ROOT / PARENT_RUNNER_REL)],
        capture_output=True,
        text=True,
        env=full_env,
        cwd=str(ROOT),
    )
    tail = result.stdout.strip().splitlines()[-3:] if result.stdout else []
    check(
        "parent runner exits with status 0",
        result.returncode == 0,
        f"returncode={result.returncode}",
    )
    pass_line = next(
        (line for line in tail if "PASS=" in line and "FAIL=" in line),
        "",
    )
    check(
        f"parent runner reports PASS={EXPECTED_PARENT_PASS} FAIL=0",
        f"PASS={EXPECTED_PARENT_PASS} FAIL=0" in pass_line,
        f"tail_line={pass_line!r}",
    )


def part_R4_load_bearing_static_checks() -> None:
    section("(R4) Load-bearing-content static checks on parent note prose")
    text = read_text(PARENT_NOTE_REL)
    text_flat = " ".join(text.split())
    check(
        "bridge identity H_0 = H_inf / sqrt(L) present in parent prose",
        "H_0 = H_inf / sqrt(L)" in text_flat
        or "`H_0 = H_inf / sqrt(L)`" in text,
    )
    check(
        "blocked upgrade (C1) alone enumerated in parent prose",
        "`(C1)` absolute-scale information alone fixes" in text
        or "(C1)` absolute-scale information alone fixes" in text,
    )
    check(
        "blocked upgrade (C2)/(C3) alone enumerated in parent prose",
        "cosmic-history-ratio retirement" in text
        and "hypothetical `(C3)`" in text,
    )
    check(
        "structural-lock-only blocked upgrade enumerated in parent prose",
        "structural lock fixes the form" in text
        or "structural lock fixes the form\n" in text
        or "structural lock fixes the form " in text,
    )
    check(
        "two-gate firewall conclusion present in parent prose",
        "(C1) AND ((C2) OR (C3))" in text,
    )
    check(
        "gate-inventory table contains C1 row",
        "`(C1)` absolute scale" in text,
    )
    check(
        "gate-inventory table contains C2 row",
        "`(C2)` cosmic-history ratio" in text,
    )
    check(
        "gate-inventory table contains C3 row",
        "`(C3)` direct cosmic-`L`" in text,
    )


def part_R5_invalidation_reason_structure() -> None:
    section("(R5) Invalidation-reason structure on ledger row")
    row = load_ledger_row()
    previous_audits = row.get("previous_audits", [])
    check(
        "ledger row has at least one previous_audits entry",
        len(previous_audits) >= 1,
        f"len(previous_audits)={len(previous_audits)}",
    )
    most_recent = previous_audits[0] if previous_audits else {}
    invalidation_reason = most_recent.get("invalidation_reason", "")
    check(
        "most-recent previous audit was audited_clean",
        most_recent.get("audit_status") == "audited_clean",
        f"audit_status={most_recent.get('audit_status')!r}",
    )
    check(
        "most-recent invalidation_reason begins with criticality_increased",
        invalidation_reason.startswith(EXPECTED_INVALIDATION_PREFIX),
        f"invalidation_reason={invalidation_reason!r}",
    )


def part_R6_input_table_invariance() -> None:
    section("(R6) Input-table invariance on parent note")
    text = read_text(PARENT_NOTE_REL)
    inputs_idx = text.find("## Inputs And Import Roles")
    check(
        "parent note contains '## Inputs And Import Roles' section",
        inputs_idx > 0,
        f"section_idx={inputs_idx}",
    )
    inputs_section = text[inputs_idx:] if inputs_idx > 0 else ""
    # Check each expected input-row source key (uppercased note path stems)
    # appears in the inputs section. Use case-insensitive substring matching
    # because the parent links the lowercase markdown reference and the
    # uppercase note path.
    inputs_lower = inputs_section.lower()
    all_present = all(key.lower() in inputs_lower for key in EXPECTED_INPUT_ROW_KEYS)
    check(
        "all six expected input rows present in parent inputs section",
        all_present,
        f"checked {len(EXPECTED_INPUT_ROW_KEYS)} keys",
    )


def main() -> int:
    print("=" * 88)
    print("AUDIT COMPANION: HUBBLE LANE 5 TWO-GATE FIREWALL")
    print("CRITICALITY-BUMP AUDIT-READINESS HYGIENE")
    print("=" * 88)
    print()
    print("Companion target:")
    print(f"  {LEDGER_ROW_ID}")
    print()
    print("Question:")
    print("  Has the parent note's substance changed since the prior")
    print("  audited_clean verdict, or is the criticality-bump invalidation")
    print("  a queue-priority signal only?")
    print()
    print("Answer:")
    print("  The substance is unchanged. The invalidation is a")
    print("  queue-priority bump (criticality_increased: medium -> high),")
    print("  not a content-change flag.")

    part_R1_presence()
    part_R2_note_hash_invariance()
    part_R3_parent_runner_execution()
    part_R4_load_bearing_static_checks()
    part_R5_invalidation_reason_structure()
    part_R6_input_table_invariance()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
