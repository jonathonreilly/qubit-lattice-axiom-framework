#!/usr/bin/env python3
"""Scope checker for the narrowed broad gravity signature algebra packet."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


NOTE = Path("docs/BROAD_GRAVITY_DERIVATION_NOTE.md")
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    print("=" * 78)
    print("Broad gravity signature algebra scope check")
    print("=" * 78)

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "bounded-support algebra over a supplied weak-field action",
        "not a retained broad gravity derivation",
        "No gravitational response, source readout",
        "PHYSICAL_WEP_OR_TIME_DILATION_CLAIMED=FALSE",
        "CONTINUUM_OR_NULL_GEODESIC_BRIDGE_CLAIMED=FALSE",
    ]
    forbidden = [
        "WEP and gravitational time dilation follow as corollaries",
        "This IS the weak equivalence principle",
        "light-bending factor of 2 follow",
        "retained broad gravity theorem",
    ]

    for phrase in required:
        record(f"source note contains scope phrase: {phrase}", phrase in text)
    for phrase in forbidden:
        record(f"source note excludes overclaim phrase: {phrase}", phrase not in text)

    k, F, phi1, phi2 = sp.symbols("k F phi1 phi2", nonzero=True)
    delta_f = sp.symbols("delta_f")
    delta_s = k * delta_f
    omega1 = k * (1 - phi1)
    omega2 = k * (1 - phi2)

    record("delta S = k delta F", sp.simplify(delta_s - k * delta_f) == 0)
    record("k cancels from stationary equation for k != 0", sp.solve(sp.Eq(delta_s, 0), delta_f) == [0])
    record(
        "phase-rate ratio cancels k",
        sp.simplify((omega1 / omega2) - ((1 - phi1) / (1 - phi2))) == 0,
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    passed = sum(ok for _, ok, _ in PASSES)
    total = len(PASSES)
    print(f"PASSED: {passed}/{total}")

    if passed == total:
        print("BROAD_GRAVITY_SIGNATURE_ALGEBRA=TRUE")
        print("K_INDEPENDENT_STATIONARY_PATH_ALGEBRA=TRUE")
        print("PHASE_RATE_RATIO_ALGEBRA=TRUE")
        print("PHYSICAL_WEP_OR_TIME_DILATION_CLAIMED=FALSE")
        print("CONTINUUM_OR_NULL_GEODESIC_BRIDGE_CLAIMED=FALSE")
        print("ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT")
        return 0

    print("BROAD_GRAVITY_SIGNATURE_ALGEBRA=FALSE")
    print("PHYSICAL_WEP_OR_TIME_DILATION_CLAIMED=FALSE")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
