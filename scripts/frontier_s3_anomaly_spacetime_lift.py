#!/usr/bin/env python3
"""
Route 2 assessment: S^3 topology + anomaly-forced time spacetime lift.

This is not a full GR proof. It checks whether the current retained stack
already gives a clean kinematic background candidate and whether the atlas
contains an exact dynamics bridge for that candidate.
"""

from __future__ import annotations

from pathlib import Path
import sys


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    msg = f"  [{status}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_existing(paths: list[Path]) -> Path:
    for path in paths:
        if path.exists():
            return path
    raise FileNotFoundError("None of the candidate paths exist: " + ", ".join(str(p) for p in paths))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    atlas = first_existing([
        root / "docs" / "publication" / "ci3_z3" / "DERIVATION_ATLAS.md",
    ])
    s3_general_note = first_existing([
        docs / "S3_GENERAL_R_DERIVATION_NOTE.md",
    ])
    s3_boundary_note = first_existing([
        docs / "S3_BOUNDARY_LINK_THEOREM_NOTE.md",
    ])
    s3_cap_note = first_existing([
        docs / "S3_CAP_UNIQUENESS_NOTE.md",
    ])
    anomaly_note = first_existing([
        docs / "ANOMALY_FORCES_TIME_THEOREM.md",
    ])
    lift_note = first_existing([
        docs / "S3_ANOMALY_SPACETIME_LIFT_NOTE.md",
    ])

    atlas_text = read_text(atlas)
    s3_general_text = read_text(s3_general_note)
    s3_boundary_text = read_text(s3_boundary_note)
    s3_cap_text = read_text(s3_cap_note)
    anomaly_text = read_text(anomaly_note)
    lift_text = read_text(lift_note)

    print("Route 2: S^3 + anomaly-forced time spacetime lift")
    print("=" * 72)
    print("  Candidate background: PL S^3 x R")
    print()

    check(
        "S^3 compactification support is present with bounded/conditional scope",
        "retained_bounded" in lift_text
        and "audited_conditional" in lift_text
        and "No proof that the compactified lattice is `PL S^3`" in s3_general_text,
        "boundary-link is retained-bounded, cap uniqueness is conditional, and the general-R note does not overclaim PL S^3 closure",
    )
    check(
        "Anomaly-forced time theorem is present with admission-inherited bounded scope",
        "d_t = 1" in anomaly_text
        and "bounded_theorem" in anomaly_text
        and "admission" in lift_text,
        "the route consumes d_t = 1 as a bounded kinematic input and preserves upstream admission inheritance",
    )
    check(
        "Atlas contains both ingredients as reusable tools",
        "`S^3` cap uniqueness" in atlas_text and "Anomaly-forced time" in atlas_text,
        "the atlas exposes the required topology/time primitives",
    )
    check(
        "Combined kinematic background is documented at the inherited weaker tier",
        "PL S^3 x R" in lift_text and "kinematic background candidate" in lift_text,
        "PL S^3 x R is the documented route-2 background candidate, not a dynamics theorem",
    )
    check(
        "No exact dynamics bridge is present in the atlas (gap documented)",
        "no exact `S^3`-to-curvature law is present" in lift_text
        and "no exact anomaly-to-Einstein-field-equation derivation is present" in lift_text,
        "no exact S^3 -> curvature / anomaly -> Einstein-field theorem yet exists on main; gap is documented in the spacetime-lift note",
    )

    print()
    print("Summary:")
    print("  Kinematic lift: yes, at inherited bounded/conditional scope")
    print("  Dynamical lift / GR closure: blocked")
    print("  Missing theorem: exact dynamics bridge from PL S^3 x R to the metric law")
    print()
    print(f"PASS={PASS} FAIL={FAIL}")

    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
