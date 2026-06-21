#!/usr/bin/env python3
"""Source-hygiene check for audit-cycle false dependency edges.

This is not an audit verdict runner. It verifies that source notes no longer
present known non-authority peer/downstream pointers as markdown one-hop
dependency links that the audit graph can reasonably treat as load-bearing.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def no_markdown_edge(source: str, target: str) -> bool:
    text = read(source)
    return f"]({target})" not in text and f"](./{target})" not in text


def contains(source: str, needle: str) -> bool:
    return needle in read(source)


def main() -> int:
    print("Source cycle false-edge hygiene check")
    print("=" * 72)

    false_edges = [
        (
            "s3_bilinear_to_spacetime_peer",
            "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
            "S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md",
        ),
        (
            "s3_spacetime_to_theta_peer",
            "docs/S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md",
            "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        ),
        (
            "quark_boundary_to_ckm_five_sixths_peer",
            "docs/QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md",
            "CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
        ),
        (
            "quark_boundary_to_taste_staircase_downstream",
            "docs/QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md",
            "QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md",
        ),
        (
            "ckm_five_sixths_to_ckm_mass_hierarchy_peer",
            "docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
            "CKM_FROM_MASS_HIERARCHY_NOTE.md",
        ),
        (
            "ckm_five_sixths_to_down_type_downstream",
            "docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
            "DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
        ),
    ]

    for name, source, target in false_edges:
        check(name, no_markdown_edge(source, target), f"{source} -> {target}")

    marker_checks = [
        (
            "s3 bilinear says non-authority peer pointer",
            "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
            "non-authority peer pointer",
        ),
        (
            "s3 spacetime says not one-hop authority",
            "docs/S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md",
            "not a one-hop authority",
        ),
        (
            "quark boundary states load-bearing inputs",
            "docs/QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md",
            "The load-bearing inputs for this boundary are the",
        ),
        (
            "ckm five-sixths marks peer/downstream orientation",
            "docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
            "non-authority peer or",
        ),
        (
            "down-type marks follow-up not dependency",
            "docs/DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
            "is not a one-hop dependency of this earlier",
        ),
    ]

    for name, source, needle in marker_checks:
        check(name, contains(source, needle), f"needle={needle!r}")

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
