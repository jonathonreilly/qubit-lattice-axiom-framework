#!/usr/bin/env python3
"""Verify the g_bare_derivation status-correction audit packet.

Verifies the post-2026-05-24 refresh of
docs/G_BARE_DERIVATION_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md:

  - audit-packet structure and required sections;
  - the originally-claimed "missing runner" finding is **superseded** and
    the runner scripts/frontier_g_bare_derivation.py is now present;
  - the constraint-vs-convention ambiguity discussion is retained and
    refreshed against the 2026-05-03 disambiguation theorem;
  - the A -> A/g rescaling-freedom analysis is retained and refreshed
    against the 2026-05-03 rescaling-freedom-removal theorem;
  - the two 2026-05-03 repair-candidate notes are declared dependencies
    of the present packet;
  - the seven retained-proposal certificate criteria section is refreshed
    against the 2026-05-24 state;
  - the G_BARE_* sister family enumeration is preserved.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "G_BARE_DERIVATION_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md"
PRIMARY_RUNNER_PARENT = ROOT / "scripts" / "frontier_g_bare_derivation.py"
RESCALING_NOTE = (
    ROOT / "docs" / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"
)
CONSTRAINT_NOTE = (
    ROOT / "docs" / "G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md"
)

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


section("Part 1: audit-packet structure")

note_text = NOTE_PATH.read_text()
required = [
    "g_bare Derivation Note — Status Correction Audit",
    "G_BARE_DERIVATION_NOTE.md",
    "constraint vs. convention",
    "A → A/g rescaling freedom",
    "frontier_g_bare_derivation.py",
    "status-correction packet",
    "proposal_allowed: false",
    "2026-05-24",
]
for s in required:
    check(f"audit packet contains: {s!r}", s in note_text)

section("Part 2: confirm primary runner now present (superseded missing-runner finding)")

check(
    "primary runner scripts/frontier_g_bare_derivation.py is present",
    PRIMARY_RUNNER_PARENT.exists(),
    detail=f"path = {PRIMARY_RUNNER_PARENT}",
)
check(
    "packet documents that the missing-runner finding is superseded",
    "superseded" in note_text,
    detail="2026-05-24 refresh language",
)

section("Part 3: constraint vs convention ambiguity discussion (refreshed)")

ambiguity_points = [
    "(a) Structural constraint",
    "(b) Convention choice",
    "upstream",
    "derived",
]
for ap in ambiguity_points:
    check(
        f"ambiguity point: {ap}",
        ap in note_text,
        detail="§3 refreshed ambiguity discussion",
    )

section("Part 4: A → A/g rescaling freedom analysis (refreshed)")

rescaling_points = [
    "S_gauge[A; g]",
    "1/4 g²",
    "rescaling-freedom-removal theorem",
    "Tr(T_a T_b) = δ_ab/2",
]
for rp in rescaling_points:
    check(
        f"rescaling analysis: {rp}",
        rp in note_text,
        detail="§4 refreshed rescaling discussion",
    )

section("Part 5: 2026-05-03 repair-candidate notes declared as dependencies")

check(
    "rescaling-freedom-removal theorem cited (markdown link)",
    "[`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`]"
    "(G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)" in note_text,
    detail="§2 declared deps table",
)
check(
    "constraint-vs-convention theorem cited (markdown link)",
    "[`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`]"
    "(G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md)" in note_text,
    detail="§2 declared deps table",
)
check(
    "rescaling-freedom-removal note exists in docs/",
    RESCALING_NOTE.exists(),
    detail=f"path = {RESCALING_NOTE}",
)
check(
    "constraint-vs-convention note exists in docs/",
    CONSTRAINT_NOTE.exists(),
    detail=f"path = {CONSTRAINT_NOTE}",
)

section("Part 6: 7 cert criteria refreshed assessment")

for i in range(1, 8):
    pattern = rf"\|\s*{i}\s*\|"
    check(
        f"audit packet explicitly assesses Criterion {i}",
        bool(re.search(pattern, note_text)),
    )
check(
    "criteria table includes 2026-05-24 refresh column",
    "2026-05-24 refresh" in note_text,
    detail="§5 refreshed table",
)

section("Part 7: G_BARE_* sister family enumerated")

g_bare_family = [
    "G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18",
    "G_BARE_RIGIDITY_THEOREM_NOTE",
    "G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18",
    "G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION_NOTE_2026-04-18",
    "G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02",
]
for gb in g_bare_family:
    check(
        f"G_BARE_* family member: {gb}",
        gb in note_text,
        detail="§9 cross-references",
    )

print(f"\n{'='*88}\n  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}\n{'='*88}")
sys.exit(1 if FAIL_COUNT > 0 else 0)
