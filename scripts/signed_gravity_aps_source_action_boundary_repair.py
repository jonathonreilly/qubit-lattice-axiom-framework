#!/usr/bin/env python3
"""Boundary repair checker for the APS-locked source-action proposal.

The repair does not derive the cross term. It verifies that the source row is
permanently framed as an open-gate axiomatic-extension premise and that the
original algebra harness still only proves conditional consequences after the
premise is inserted.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
NOTE = DOCS / "SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md"
ORIGINAL = ROOT / "scripts" / "signed_gravity_aps_locked_source_action_proposal.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def main() -> int:
    print("Signed gravity APS source-action boundary repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger["rows"]

    print()
    print("A. Boundary wording")
    print("-" * 72)
    check("note declares open_gate type", "**Type:** open_gate" in note)
    check("note states permanent axiomatic-extension boundary", "permanently classified" in note and "axiomatic-extension premise" in note)
    check("note says cross term is not derived", "not derived from the retained stack" in note and "not derived\nby source-unit normalization" in note)
    check("note says no physical signed-gravity claim", "not a negative-mass" in note and "physical signed-gravity claim" in note)
    check("note does not ask audit to retain current theorem", "does not ask\naudit to retain" in note)

    print()
    print("B. Ledger authority")
    print("-" * 72)
    lane_status = rows["signed_gravity_response_lane_status_note_2026-04-26"]
    this_row = rows["signed_gravity_aps_locked_source_action_proposal_note"]
    check("lane status authority is retained_no_go", lane_status.get("effective_status") == "retained_no_go", str(lane_status.get("effective_status")))
    check("source-action row claim_type is open_gate before repair pipeline", this_row.get("claim_type") == "open_gate", str(this_row.get("claim_type")))
    check("source-action row is not retained before repair pipeline", this_row.get("effective_status") != "retained", str(this_row.get("effective_status")))

    print()
    print("C. Original algebra harness")
    print("-" * 72)
    result = subprocess.run(
        [sys.executable, str(ORIGINAL.relative_to(ROOT))],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout
    check("original harness exits cleanly", result.returncode == 0, f"returncode={result.returncode}")
    check("original harness remains conditional", "CONDITIONAL_CANDIDATE" in output)
    check("original harness states new source-action premise", "new source-action premise" in output)
    check("original harness does not derive origin", "derive this APS-locked source action" in output)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: APS source-action row is permanently open_gate / axiomatic-extension boundary.")
        return 0
    print("VERDICT: APS source-action boundary repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
