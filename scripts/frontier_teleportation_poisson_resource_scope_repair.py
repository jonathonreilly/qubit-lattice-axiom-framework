#!/usr/bin/env python3
"""Scope-boundary repair checker for the Poisson/CHSH teleportation row.

The repair does not prove the native preparation/readout theorem. It verifies
that the row is framed as an open gate, that the old stale minimal-axiom link is
gone, and that the original bounded diagnostic still runs on the restricted
small surfaces.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"
ORIGINAL = ROOT / "scripts" / "frontier_teleportation_resource_from_poisson.py"

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
    print("Teleportation Poisson resource scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")

    print()
    print("A. Boundary wording")
    print("-" * 72)
    check("note declares open_gate type", "**Type:** open_gate" in note)
    check("note declares open_gate claim type", "**Claim type:** open_gate" in note)
    check("note has no branch-local status authority", "Status authority" not in note)
    check(
        "note says this is not a deterministic-resource theorem",
        has_phrase(note, "not as a deterministic-resource theorem"),
    )
    check(
        "note preserves small-surface diagnostic value",
        has_phrase(note, "small-surface Poisson/CHSH calculation is still useful")
        and has_phrase(note, "high ideal state-teleportation fidelity"),
    )
    check(
        "note leaves native carrier derivation open",
        "No sentence in this note asserts that the last taste bit has been derived" in note
        and "missing native preparation/readout theorem remains" in note,
    )
    check(
        "note does not claim matter or FTL teleportation",
        "does not claim matter teleportation" in note
        and "faster-than-light transport" in note,
    )

    print()
    print("B. Dependency hygiene")
    print("-" * 72)
    check(
        "stale minimal axiom link removed",
        "MINIMAL_AXIOMS_2026-05-03.md" not in note,
    )
    check(
        "current canonical axiom premise cited",
        "MINIMAL_AXIOMS_2026-05-20.md" in note,
    )
    check(
        "adjacent notes are source references, not status imports",
        "Ledger snapshot" not in note
        and "audited_clean" not in note
        and "retained_bounded" not in note,
    )

    print()
    print("C. Original bounded diagnostic")
    print("-" * 72)
    result = subprocess.run(
        [
            sys.executable,
            str(ORIGINAL.relative_to(ROOT)),
            "--trials",
            "16",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout
    check(
        "original runner exits cleanly",
        result.returncode == 0,
        f"returncode={result.returncode}",
    )
    check("original runner covers null control", "Case: 1d_null" in output)
    check("original runner covers 1d Poisson case", "Case: 1d_poisson_chsh" in output)
    check("original runner covers 2d Poisson case", "Case: 2d_poisson_chsh" in output)
    check(
        "original runner reports diagnostic-only postselection",
        "Postselected branches" in output and "diagnostics only" in output,
    )
    check(
        "original runner does not promote the result",
        "independent hardening before promotion" in output
        and "not by itself a teleportation resource derivation" in output,
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: row is ready for re-audit as an open_gate bounded diagnostic.")
        return 0
    print("VERDICT: teleportation Poisson scope repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
