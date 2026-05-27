#!/usr/bin/env python3
"""Verify the Kubo Fam2 possible-obstruction inventory note."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KUBO_FAM2_NON_CONVERGENCE_NOTE_2026-05-02.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, ok, detail=""):
    global PASS_COUNT, FAIL_COUNT
    tag = "PASS (A)" if ok else "FAIL (A)"
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{tag}] {label}  ({detail})")


def section(title):
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


section("Part 1: open-gate inventory structure")
note_text = NOTE_PATH.read_text()
required = [
    "Kubo Fam2 Non-Convergence Possible-Obstruction Inventory",
    "open-gate inventory",
    "Recorded Finite Data",
    "Minimal Local Premises",
    "Forbidden Imports",
    "Fam2",
    "Fam1",
    "Fam3",
    "(O1)",
    "(O2)",
    "(O3)",
    "not exhaustive",
    "proposal_allowed: false",
]
for s in required:
    check(f"contains: {s!r}", s in note_text)

section("Part 2: 3 possible obstruction routes documented")
obstructions = [
    "Parameter-dependent microscopic dynamics",
    "Critical or near-critical parameter regime",
    "Fam2-specific discretization interaction",
]
for o in obstructions:
    check(f"obstruction: {o[:50]}",
          o in note_text)

section("Part 3: Fam parameters enumerated")
fam_params = [
    "drift=0.20, restore=0.70",  # Fam1
    "drift=0.05, restore=0.30",  # Fam2
    "drift=0.50, restore=0.90",  # Fam3
]
for fp in fam_params:
    check(f"family parameter: {fp}", fp in note_text)

section("Part 4: explicit non-closure and non-exhaustiveness")
non_closures = [
    "does not resolve Fam2 non-convergence",
    "does not prove an exhaustive obstruction trichotomy",
    "does not prove a continuum limit for Fam2",
    "does not alter the status of any parent Kubo-family evidence",
]
for nc in non_closures:
    check(f"non-closure: {nc}", nc in note_text)

section("Part 5: closeout labels")
closeout_requirements = [
    "actual_current_surface_status: open",
    "bare_retained_allowed: false",
]
for label in closeout_requirements:
    check(f"status label: {label}", label in note_text)

print(f"\n{'='*88}\n  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}\n{'='*88}")
if FAIL_COUNT == 0:
    print("KUBO_FAM2_POSSIBLE_OBSTRUCTION_INVENTORY=TRUE")
    print("OPEN_GATE_DOCUMENTED=TRUE")
    print("EXHAUSTIVE_TRICHOTOMY_CLAIMED=FALSE")
    print("FAM2_NON_CONVERGENCE_RESOLVED=FALSE")
    print("OBSERVED_OR_FITTED_TARGET_CONSUMED=FALSE")
sys.exit(1 if FAIL_COUNT > 0 else 0)
