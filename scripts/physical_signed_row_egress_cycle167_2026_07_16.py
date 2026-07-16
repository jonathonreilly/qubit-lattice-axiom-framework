#!/usr/bin/env python3
"""Cycle 167: verify physical signed-row egress and its membership boundary."""

from __future__ import annotations

from pathlib import Path

import factorized_commuting_signed_membership_probe_2026_07_16 as factorized
import physical_downstream_signed_row_decoder_probe_2026_07_16 as downstream
import physical_joint_stabilizer_update_geometry_probe_2026_07_16 as joint
import physical_ported_sign_reader_probe_2026_07_16 as reader
import physical_signed_row_egress_collision_probe_2026_07_16 as collision


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SIGNED_ROW_EGRESS_AND_MEMBERSHIP_SEAM_CYCLE167_NOTE_2026-07-16.md"
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def role_set(raw):
    return {
        role
        for outputs in raw.values()
        for role in outputs
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LOCAL LAW")
    check("Cycle-167 review note exists", NOTE.is_file())
    check(
        "the collision and positive reader use the same 32-row signed domain",
        len(collision.PROPOSED_TABLE)
        == len(reader.CANONICAL_TABLE)
        == len(downstream.SIGN_TABLE)
        == 32,
    )
    check(
        "the two positive sign-reader presentations are one covariant raw family",
        reader.SIGN_RAW == downstream.SIGN_RAW
        and len(reader.SIGN_RAW) == 768,
        len(reader.SIGN_RAW),
    )
    check(
        "the sign family adds no onsite role",
        role_set(reader.SIGN_RAW) <= role_set(joint.tap.MERGED_RAW),
        role_set(reader.SIGN_RAW) - role_set(joint.tap.MERGED_RAW),
    )

    print("\nEXACT ZERO-DELTA INTERFACE EXCLUSIONS")
    check("the narrow collision probe is green", collision.main() == 0)

    print("\nPOSITIVE SIGN EGRESS")
    check("the standalone ported sign reader is green", reader.main() == 0)
    check(
        "the tap-to-sign-to-cable composition is green",
        downstream.main() == 0,
    )

    print("\nUNIFIED CYCLE-166 LAW")
    unified = joint.cell.merge_raw(joint.MERGED_RAW, reader.SIGN_RAW)
    conflicts = {
        signature: outputs
        for signature, outputs in unified.items()
        if len(outputs) != 1
    }
    overlap = set(joint.MERGED_RAW) & set(reader.SIGN_RAW)
    check(
        "the sign family is a disjoint 768-row extension of Cycle 166",
        len(joint.MERGED_RAW) == 100_652
        and len(reader.SIGN_RAW) == 768
        and not overlap
        and len(unified) == 101_420,
        (len(joint.MERGED_RAW), len(overlap), len(unified)),
    )
    check(
        "the 101,420-row unified law remains deterministic",
        not conflicts and all(len(outputs) == 1 for outputs in unified.values()),
        len(conflicts),
    )

    reader.MERGED_RAW = unified
    downstream.MERGED_RAW = unified
    reader_failures = []
    downstream_failures = []
    downstream_shapes = set()
    for rotation_index, rotation in enumerate(joint.c53.ROTATIONS):
        for row in reader.ROWS:
            ok, detail = reader.graph(row, rotation)
            if not ok:
                reader_failures.append((rotation_index, row, detail))
            ok, detail = downstream.run(row, rotation)
            if not ok:
                downstream_failures.append((rotation_index, row, detail))
            else:
                downstream_shapes.add(detail)
    reader_deletions = reader.deletion_failures()
    downstream_deletions = downstream.deletion_failures()
    check(
        "all 768 standalone readers survive the unified law",
        not reader_failures and not reader_deletions,
        (reader_failures[:1], reader_deletions[:1]),
    )
    check(
        "all 768 tap-sign-cable histories survive the unified law",
        not downstream_failures and not downstream_deletions,
        (
            sorted(downstream_shapes),
            downstream_failures[:1],
            downstream_deletions[:1],
        ),
    )

    print("\nFACTORIZED MEMBERSHIP BOUNDARY")
    check(
        "the supplied-literal membership component remains green",
        factorized.main() == 0,
    )

    print("\nSCOPE AND NO-GO DISCIPLINE")
    note = (
        " ".join(
            NOTE.read_text(encoding="utf-8")
            .lower()
            .replace("*", "")
            .replace("`", "")
            .split()
        )
        if NOTE.is_file()
        else ""
    )
    for phrase in (
        "two exact zero-delta attempts fail",
        "those are exclusions of two specified interfaces, not a sign-egress no-go",
        "101,420",
        "literal-input component certificate",
        "status: fail for a general no-go",
        "n1 — alternative routes",
        "n2 — wall independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial closure and axiom classification",
        "n7 — strongest hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom, primitive, registry, policy, or audit edit follows",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_SIGNED_ROW_EGRESS" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
