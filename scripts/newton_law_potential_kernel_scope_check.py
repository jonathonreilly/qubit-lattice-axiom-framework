#!/usr/bin/env python3
"""Scope checker for the narrowed Newton potential-kernel algebra packet."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


NOTE = Path("docs/NEWTON_LAW_DERIVED_NOTE.md")


PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    print("=" * 78)
    print("Newton potential-kernel algebra scope check")
    print("=" * 78)

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "bounded-support potential-kernel algebra",
        "not a retained Newton force-law derivation",
        "not yet a physical Newton force law",
        "test-mass force/source response rule",
        "BA3_TEST_MASS_COUPLING_DERIVED=FALSE",
        # 2026-07-11 premise wiring pins:
        "[`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`]"
        "(LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)",
        "(P-LIN)",
        "accepted-premise packet entry",
        "2026-07-11 premise wiring",
    ]
    forbidden = [
        "No additional physics is imported beyond",
        "unconditional closure from the framework baseline",
        "retained Newton-law closure",
    ]

    for phrase in required:
        record(f"source note contains scope phrase: {phrase}", phrase in text)
    for phrase in forbidden:
        record(f"source note excludes overclaim phrase: {phrase}", phrase not in text)

    r, M = sp.symbols("r M", positive=True)
    G = 1 / (4 * sp.pi * r)
    phi = M * G
    dphi = sp.diff(phi, r)
    grad_mag = -dphi

    record("supplied kernel is 1/(4*pi*r)", sp.simplify(G - 1 / (4 * sp.pi * r)) == 0)
    record("source-linearity gives phi=M/(4*pi*r)", sp.simplify(phi - M / (4 * sp.pi * r)) == 0)
    record("radial derivative is -M/(4*pi*r^2)", sp.simplify(dphi + M / (4 * sp.pi * r**2)) == 0)
    record("gradient magnitude is M/(4*pi*r^2)", sp.simplify(grad_mag - M / (4 * sp.pi * r**2)) == 0)

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    passed = sum(ok for _, ok, _ in PASSES)
    total = len(PASSES)
    print(f"PASSED: {passed}/{total}")

    if passed == total:
        print("NEWTON_POTENTIAL_KERNEL_ALGEBRA=TRUE")
        print("POTENTIAL_GRADIENT_INVERSE_SQUARE=TRUE")
        print("PHYSICAL_FORCE_LAW_CLAIMED=FALSE")
        print("BA3_TEST_MASS_COUPLING_DERIVED=FALSE")
        print("ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT")
        return 0

    print("NEWTON_POTENTIAL_KERNEL_ALGEBRA=FALSE")
    print("PHYSICAL_FORCE_LAW_CLAIMED=FALSE")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
