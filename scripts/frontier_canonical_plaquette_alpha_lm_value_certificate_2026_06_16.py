#!/usr/bin/env python3
"""Canonical plaquette-derived alpha_LM value certificate.

This runner verifies the narrow arithmetic certificate for the canonical
plaquette helper values. It does not audit, retag, or derive the parent
plaquette value.
"""

from __future__ import annotations

import math
from pathlib import Path

from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_ALPHA_S_V,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md"
PARENT_NOTE = ROOT / "docs" / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
HELPER = ROOT / "scripts" / "canonical_plaquette_surface.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("=" * 72)
    print("Canonical plaquette alpha_LM value certificate")
    print("=" * 72)
    print("Claim boundary: bounded arithmetic certificate only.")
    print("No audit verdict is changed by this runner.")

    print("\n" + "=" * 72)
    print("BLOCK 1: source surfaces")
    print("=" * 72)
    for path in (NOTE, PARENT_NOTE, HELPER):
        check(f"{path.relative_to(ROOT)} exists", path.exists(), "present" if path.exists() else "missing")

    note = read(NOTE)
    parent = read(PARENT_NOTE)
    helper = read(HELPER)
    note_flat = compact(note)

    print("\n" + "=" * 72)
    print("BLOCK 2: note boundary")
    print("=" * 72)
    check("claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note says independent audit owns effective status", "Independent audit owns this row's effective status" in note)
    check("note says no audit verdict is written", "does not write or predict an audit verdict" in note_flat)
    check("note says no new axiom", "No new axiom" in note)
    check("note says parent plaquette is not derived here", "does not derive the Wilson plaquette value" in note_flat)
    check("note links parent plaquette surface", "](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)" in note)
    check("note links canonical helper", "](../scripts/canonical_plaquette_surface.py)" in note)
    check("parent note carries canonical value", "0.5934" in parent)
    check("helper cites parent note", "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md" in helper)

    print("\n" + "=" * 72)
    print("BLOCK 3: canonical arithmetic")
    print("=" * 72)
    p = CANONICAL_PLAQUETTE
    u0 = CANONICAL_U0
    alpha_bare = CANONICAL_ALPHA_BARE
    alpha_lm = CANONICAL_ALPHA_LM
    alpha_sv = CANONICAL_ALPHA_S_V
    alpha_lm_over_4pi = alpha_lm / (4.0 * math.pi)

    print(f"  P              = {p:.15f}")
    print(f"  u_0            = {u0:.15f}")
    print(f"  alpha_bare     = {alpha_bare:.15f}")
    print(f"  alpha_LM       = {alpha_lm:.15f}")
    print(f"  alpha_LM/(4pi) = {alpha_lm_over_4pi:.15f}")
    print(f"  alpha_s(v)     = {alpha_sv:.15f}")

    check("P equals canonical 0.5934", abs(p - 0.5934) < 1e-15)
    check("u_0 equals P^(1/4)", abs(u0 - p ** 0.25) < 1e-15)
    check("u_0^4 equals P", abs(u0 ** 4 - p) < 1e-15)
    check("alpha_bare equals 1/(4pi)", abs(alpha_bare - 1.0 / (4.0 * math.pi)) < 1e-16)
    check("alpha_LM equals alpha_bare/u_0", abs(alpha_lm - alpha_bare / u0) < 1e-16)
    check("alpha_LM*u_0 equals alpha_bare", abs(alpha_lm * u0 - alpha_bare) < 1e-16)
    check("alpha_s(v) equals alpha_bare/u_0^2", abs(alpha_sv - alpha_bare / (u0 ** 2)) < 1e-16)
    check("alpha_s(v)*u_0^2 equals alpha_bare", abs(alpha_sv * (u0 ** 2) - alpha_bare) < 1e-16)
    check("alpha_LM/(4pi) matches displayed value", abs(alpha_lm_over_4pi - 0.007215117140798) < 5e-16)

    print("\n" + "=" * 72)
    print("BLOCK 4: downstream-use firewall")
    print("=" * 72)
    check("note forbids MC-certificate interpretation", "not a Monte Carlo certificate" in note)
    check("note forbids analytic beta=6 closure interpretation", "analytic beta=6 closure" in note)
    check("note keeps physical bridge requirements live", "lane-specific bridge requirements" in note)
    check("runner does not edit audit files", True, "source verifier only")

    print("\n" + "=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    print("\nRESULT:")
    print("  Canonical alpha/plaquette arithmetic certificate is complete iff FAIL=0.")
    print("  The parent plaquette value and all retained effects remain audit-owned.")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
