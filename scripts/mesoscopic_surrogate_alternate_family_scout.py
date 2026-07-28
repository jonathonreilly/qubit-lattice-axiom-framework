#!/usr/bin/env python3
"""Alternate-family planning scout for the mesoscopic surrogate lane.

This is intentionally not a heavy numerical sweep. It reads the already frozen
notes for the mesoscopic-surrogate lane and records one narrow planning context:

    Which already-bounded non-Gate-B family remains a non-load-bearing
    planning candidate for a more localized source object?

The scout is looking for a family where localization might matter more than on
the retained 3D h=0.5 family, without re-running a large parameter sweep. The
2D threshold fixture contributes only its explicitly listed finite-row result,
not a family-level negative conclusion.

The answer is a planning recommendation, not an objective ranking theorem or a
new physics claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AUDIT_INPUT_PATHS = (
    "docs/MESOSCOPIC_SURROGATE_LOCALIZATION_FRONTIER_NOTE.md",
    "docs/MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md",
    "docs/MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE.md",
    "docs/SAME_FAMILY_3D_CLOSURE_NOTE.md",
    "docs/VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md",
    "docs/PERSISTENT_INERTIAL_RESPONSE_READINESS_NOTE.md",
    "docs/MESOSCOPIC_SURROGATE_ALTERNATE_FAMILY_SCOUT_NOTE.md",
)
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class FamilyRead:
    name: str
    status: str
    why: str
    next_step: str


def read_text(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def has_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle in text for needle in needles)


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def main() -> None:
    frontier = read_text("docs/MESOSCOPIC_SURROGATE_LOCALIZATION_FRONTIER_NOTE.md").lower()
    sweep_3d = read_text("docs/MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md").lower()
    threshold_2d = read_text("docs/MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE.md").lower()
    same_family_3d = read_text("docs/SAME_FAMILY_3D_CLOSURE_NOTE.md").lower()
    asymptotic = read_text("docs/VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md").lower()
    readiness = read_text("docs/PERSISTENT_INERTIAL_RESPONSE_READINESS_NOTE.md").lower()

    families = [
        FamilyRead(
            name="3D ordered-lattice h=0.5 localization frontier",
            status="closed",
            why="The frozen frontier note says the only winners are degenerate point-like cases, and topN remains the least-bad mesoscopic control once the family is meaningfully localized.",
            next_step="Do not keep sweeping this family for a sharp localization win.",
        ),
        FamilyRead(
            name="Fixed 2D support-list computation",
            status="finite_rows_pass",
            why=(
                "The threshold note reports that all 19 requested topN rows pass "
                "two programmed gates for one source-identity-pinned implementation."
            ),
            next_step=(
                "Do not extrapolate this finite fixture to a retained family or "
                "to unlisted support values."
            ),
        ),
        FamilyRead(
            name="Retained 3D h=0.25 ordered-lattice family",
            status="planning_candidate",
            why=(
                "The same-family 3D closure and asymptotic bridge are already frozen at h=0.25, "
                "with stronger near-Newtonian behavior and a cleaner retained continuum read than h=0.5."
            ),
            next_step=(
                "If we try a more localized source object at all, this bounded family remains a planning "
                "candidate: use non-degenerate shapes with an explicit support/capture floor."
            ),
        ),
    ]

    print("=" * 92)
    print("MESOSCOPIC SURROGATE ALTERNATE-FAMILY SCOUT")
    print("  Purpose: verify frozen scope/evidence markers and record the")
    print("           non-load-bearing planning candidate for any later localized")
    print("           source-object attempt.")
    print("=" * 92)
    print()
    print("Frozen evidence check")
    print(f"  h=0.5 frontier closed? {'yes' if 'degenerate point-like localizations' in sweep_3d else 'no'}")
    threshold_finite_marker = (
        "all 19 rows satisfy both stability gates" in threshold_2d
        and "implementation-specific finite claim" in threshold_2d
    )
    print(f"  2D finite-row result present? {'yes' if threshold_finite_marker else 'no'}")
    print(f"  3D h=0.25 same-family closure present? {'yes' if 'h=0.25, w=10, l=12' in same_family_3d else 'no'}")
    print(f"  3D h=0.25 asymptotic bridge present? {'yes' if 'z>=5: -1.00' in asymptotic else 'no'}")
    print(f"  Persistent-mass readiness still open? {'yes' if 'not yet' in readiness else 'no'}")
    print()
    print("Planning ordering (non-load-bearing)")
    for idx, fam in enumerate(families, 1):
        print(f"{idx}. {fam.name} [{fam.status}]")
        print(f"   why: {fam.why}")
        print(f"   next: {fam.next_step}")
    print()
    print("Planning recommendation")
    print(
        "  The already-bounded family worth one more planning attempt is the retained 3D h=0.25 "
        "ordered-lattice family. The retained 3D h=0.5 family is already closed as a "
        "degenerate-point-source frontier. The fixed 2D computation supplies no family-level "
        "threshold conclusion."
    )
    print(
        "  If we do proceed, the next attempt should use only non-degenerate localized shapes "
        "(annular windows, tapered ellipsoids, or compact Gaussians) with a minimum support/capture floor."
    )
    print(
        "  If that family still cannot beat the broad topN control, the localization lane is probably "
        "done and should be frozen as a bounded negative result."
    )
    print()
    print("Useful frozen context")
    print(
        "  - 3D h=0.5 localization frontier: only degenerate point-like winners; topN remains least-bad."
    )
    print(
        "  - Fixed 2D computation: all 19 requested topN rows pass its two programmed gates."
    )
    print(
        "  - 3D h=0.25 ordered-lattice family: already has same-family closure and the strongest retained asymptotic bridge."
    )
    print()
    print("Scope scorecard")
    note = read_text("docs/MESOSCOPIC_SURROGATE_ALTERNATE_FAMILY_SCOUT_NOTE.md")
    note_flat = " ".join(note.lower().split())
    report("source note is a meta/support planning index", "meta/support planning index" in note)
    report("source note says no theorem-grade target selection", "must not be used as theorem-grade target-selection authority" in note_flat)
    report("source note marks priority as editorial judgment", "editorial judgment" in note)
    report("source note marks planning input as non-load-bearing", "non-load-bearing planning input" in note)
    report(
        "source note preserves the 2D finite-only boundary",
        "2d fixture does not close a 2d family-level threshold question" in note_flat,
    )
    report(
        "runner output has non-load-bearing planning label",
        threshold_finite_marker
        and any(fam.status == "planning_candidate" for fam in families)
        and "non-load-bearing planning input" in note,
    )
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
