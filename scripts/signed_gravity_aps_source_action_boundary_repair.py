#!/usr/bin/env python3
"""Boundary repair checker for the APS-locked source-action proposal.

The repair does not derive the cross term. It verifies that the source row is
framed as an unadmitted open-gate proposed-extension boundary and that the
original algebra harness still only proves conditional consequences after the
premise is inserted.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
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


def has_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.split()) in " ".join(text.split())


def main() -> int:
    print("Signed gravity APS source-action boundary repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")

    print()
    print("A. Boundary wording")
    print("-" * 72)
    check("note declares open_gate type", "**Type:** open_gate" in note)
    check("note declares open_gate claim type", "**Claim type:** open_gate" in note)
    check("note has no source-side status authority", "Status authority" not in note)
    check(
        "note states unadmitted proposed-extension boundary",
        has_phrase(note, "`open_gate` proposed-extension boundary")
        and has_phrase(note, "not as an admitted axiom")
        and has_phrase(note, "not as a retained theorem"),
    )
    check(
        "note says cross term is not derived",
        "not supplied by the current retained inventory" in note
        and has_phrase(note, "not derived by source-unit normalization"),
    )
    check("note says no physical signed-gravity claim", "not a negative-mass" in note and "physical signed-gravity claim" in note)
    check("note does not admit a new axiom", "not an admitted axiom" in note and "No new axiom" in note)

    print()
    print("B. Original algebra harness")
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
    check(
        "note displayed Born/norm controls match current harness",
        "Born I3, chi=+ sector: +1.794e-43" in note
        and "Born I3, chi=- sector: +1.794e-43" in note
        and "max norm drift: 2.887e-15" in note
        and "I3=+1.794e-43" in output
        and "max drift=2.887e-15" in output,
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: APS source-action row is an unadmitted open_gate proposed-extension boundary.")
        return 0
    print("VERDICT: APS source-action boundary repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
