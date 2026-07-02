#!/usr/bin/env python3
"""Route-2 assessment: S^3 topology plus anomaly-forced time.

The source note is an `open_gate` route survey, not a full GR proof. This
runner verifies the current honest boundary:

* the cited topology/time ingredients support a `PL S^3 x R` kinematic
  background candidate only at the weakest inherited tier;
* the source note preserves the upstream `S^3` non-overclaim and
  anomaly-admission inheritance; and
* no unique metric/tensor/Einstein-field dynamics theorem is claimed here.
"""

from __future__ import annotations

import sys
from pathlib import Path


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
    boundary_link_note = first_existing([
        docs / "S3_BOUNDARY_LINK_THEOREM_NOTE.md",
    ])
    cap_note = first_existing([
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
    boundary_link_text = read_text(boundary_link_note)
    cap_text = read_text(cap_note)
    anomaly_text = read_text(anomaly_note)
    lift_text = read_text(lift_note)
    lift_lower = lift_text.lower()

    print("Route 2: S^3 + anomaly-forced time spacetime lift")
    print("=" * 72)
    print("  Candidate background: PL S^3 x R")
    print("  Scope: kinematic open-gate route survey, not GR closure")
    print()

    check(
        "source note is explicitly scoped as an open route survey",
        "open route survey" in lift_lower
        and "full-gr closure" in lift_lower
        and "**Type:** open_gate" in lift_text,
        "the parent note preserves the open-gate boundary",
    )
    check(
        "S3 boundary-link and cap-uniqueness sources are present",
        "S^3 Boundary-Link" in boundary_link_text
        and "S^3 Cap" in cap_text
        and "S3_BOUNDARY_LINK_THEOREM_NOTE.md" in lift_text
        and "S3_CAP_UNIQUENESS_NOTE.md" in lift_text,
        "the topology side is cited as a two-source PL compactification family",
    )
    check(
        "S3 compactification tier and non-overclaim guard are preserved",
        "retained_bounded" in lift_text
        and "audited_conditional" in lift_text
        and "No proof that the compactified lattice" in s3_general_text
        and "`PL S^3`" in s3_general_text,
        "boundary-link is retained-bounded, cap uniqueness is conditional, and the general-R note still refuses PL S3 closure",
    )
    check(
        "Anomaly-forced time theorem is present with admission-inherited bounded scope",
        "d_t" in anomaly_text
        and "bounded_theorem" in anomaly_text
        and "ANOMALY_FORCES_TIME_THEOREM.md" in lift_text
        and "Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`" in lift_text,
        "the route consumes d_t = 1 as a bounded kinematic input and preserves upstream admission inheritance",
    )
    check(
        "atlas exposes the route as a kinematic spacetime lift, not a solved dynamics bridge",
        "Route 2 spacetime lift `PL S^3 x R`" in atlas_text
        and "remaining issue on that route is dynamics" in atlas_text,
        "publication atlas points to the same kinematic/dynamics split",
    )
    check(
        "combined PL S3 x R kinematic background is the route candidate",
        "PL S^3 x R" in lift_text and "kinematic background candidate" in lift_text,
        "composition of S3 topology and anomaly-forced time is the candidate background",
    )
    check(
        "no exact dynamics bridge is present in the source note",
        "no exact `S^3`-to-curvature law is present" in lift_text
        and "no exact anomaly-to-Einstein-field-equation derivation is present" in lift_text,
        "no exact S3 -> curvature / anomaly -> Einstein-field theorem is claimed",
    )
    check(
        "runner preserves the honest open-gate endpoint",
        "This row is `open_gate` and remains so until" in lift_text,
        "the missing dynamics theorem is still the named blocker",
    )

    print()
    print("Summary:")
    print("  Kinematic background candidate: yes, at inherited bounded/conditional scope")
    print("  Dynamical lift / GR closure: open")
    print("  Missing theorem: exact dynamics bridge from PL S^3 x R to the metric law")
    print()
    print(f"PASS={PASS} FAIL={FAIL}")

    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
