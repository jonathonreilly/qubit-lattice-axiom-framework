#!/usr/bin/env python3
"""Scope-repair runner for AUDITED_SYMMETRY_SYNTHESIS_NOTE.md.

The runner checks that the synthesis row is scoped to registered finite
authority surfaces and that mechanism language is explicitly non-binding.
It does not rerun the heavy mirror/Z2 validation programs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
NOTE = REPO / "docs" / "AUDITED_SYMMETRY_SYNTHESIS_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (B)"
    else:
        FAIL += 1
        tag = "FAIL (B)"
    suffix = f" | {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def main() -> int:
    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    flat_text = " ".join(text.split())
    print("Audited symmetry synthesis scope repair")
    print("Scope: registered finite-surface aggregation; mechanism language non-binding.")
    print()

    check("synthesis note exists", NOTE.exists(), str(NOTE.relative_to(REPO)))
    check("mechanism firewall present", "## Mechanism Firewall (2026-05-27)" in text)

    required_firewall_phrases = [
        "finite-surface aggregation only",
        "not load-bearing theorem claims",
        "does **not** claim",
        "retained one-hop mechanism theorem",
    ]
    for phrase in required_firewall_phrases:
        check(f"firewall phrase present: {phrase}", phrase in flat_text)

    old_unqualified_patterns = [
        r"random growth fails by a rank-1 / CLT-type mechanism",
        r"exact discrete symmetry can preserve distinct sectors and delay that failure",
    ]
    for pattern in old_unqualified_patterns:
        check(
            f"old unqualified mechanism claim absent: {pattern}",
            re.search(pattern, text) is None,
        )

    finite_surface_markers = [
        "registered finite surfaces",
        "N=15` and `N=25",
        "N=25,40,60,80",
        "N=40,60,80",
        "No dense `Z₂ × Z₂` `N=120` promotion",
        "no mechanism theorem claimed here",
    ]
    for marker in finite_surface_markers:
        check(f"finite boundary marker present: {marker}", marker in text)

    retained_dependency_links = [
        "MIRROR_CHOKEPOINT_NOTE.md",
        "MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md",
        "MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md",
        "MIRROR_2D_VALIDATION_NOTE.md",
        "HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md",
        "HIGHER_SYMMETRY_GRAVITY_PROBE_NOTE.md",
    ]
    for dep in retained_dependency_links:
        check(f"one-hop finite authority linked: {dep}", dep in text)

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
