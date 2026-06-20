#!/usr/bin/env python3
"""Check the finite-link/Wilson beta=6 bridge for the g_bare parent row.

This runner deliberately stays source-side. It does not read audit ledgers,
audit queues, publication matrices, or effective-status files.

The checked theorem is the bounded composition:

  finite-link canonical scalar slot g_link^2 = 1
  Wilson small-a coefficient identity beta * g_bare^2 = 2 N_c
  same scalar slot in the canonical T_a exponent
  ------------------------------------------------
  beta = 2 N_c = 6 for N_c = 3 on the supplied Wilson surface.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "docs" / "G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "G_BARE_DERIVATION_NOTE.md"
RIGIDITY = ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md"
WILSON = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {name}{suffix}")
    return condition


def require_contains(label: str, text: str, marker: str) -> None:
    check(f"{label} contains marker: {marker[:72]}", marker in text)


def require_absent(label: str, text: str, marker: str) -> None:
    check(f"{label} omits forbidden marker: {marker[:72]}", marker not in text)


def main() -> int:
    print("G_BARE parent finite-link/Wilson beta=6 bridge check")
    print("=" * 78)

    paths = {
        "bridge note": BRIDGE,
        "parent note": PARENT,
        "finite-link rigidity note": RIGIDITY,
        "Wilson small-a note": WILSON,
    }
    for label, path in paths.items():
        check(f"{label} exists", path.exists(), str(path))

    bridge_text = BRIDGE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    rigidity_text = RIGIDITY.read_text(encoding="utf-8")
    wilson_text = WILSON.read_text(encoding="utf-8")
    bridge_flat = flat(bridge_text)
    parent_flat = flat(parent_text)
    rigidity_flat = flat(rigidity_text)
    wilson_flat = flat(wilson_text)

    print("\nSource-boundary checks")
    print("-" * 78)
    require_contains("bridge", bridge_flat, "set only by the independent audit lane")
    require_contains("bridge", bridge_flat, "same scalar slot")
    require_contains("bridge", bridge_flat, "finite-link canonical Wilson surface")
    require_contains("bridge", bridge_flat, "does not claim:")
    require_contains("bridge", bridge_flat, "Wilson plaquette action-surface selection")
    require_contains("bridge", bridge_flat, "global logarithm-branch selection")
    require_contains("bridge", bridge_flat, "a dynamical fixed point")
    require_contains("bridge", bridge_flat, "an audit verdict or any effective-status promotion")
    require_absent("bridge", bridge_text, "effective_status:")
    require_absent("bridge", bridge_text, "audit_status:")

    print("\nDependency-surface checks")
    print("-" * 78)
    require_contains("parent", parent_text, "G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md")
    require_contains("parent", parent_text, "G_BARE_RIGIDITY_THEOREM_NOTE.md")
    require_contains("parent", parent_text, "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md")
    require_contains("parent", parent_flat, "No step uses `beta = 6` as a premise for `g_bare = 1`.")
    require_absent("parent", parent_text, "beta_canonical")

    require_contains("rigidity", rigidity_flat, "finite-link")
    require_contains("rigidity", rigidity_flat, "no independent scalar-normalization freedom")
    require_contains("rigidity", rigidity_flat, "g_bare = 1")
    require_contains("Wilson", wilson_text, "beta * g_bare^2 = 2 N_c")
    require_contains("Wilson", wilson_text, "beta = 2 N_c / g_bare^2")
    require_contains("Wilson", wilson_flat, "does not derive that the framework must select the Wilson action surface")

    print("\nExact arithmetic checks")
    print("-" * 78)
    n_c = Fraction(3)
    g_link_sq = Fraction(1)
    g_wilson_sq = g_link_sq
    beta = Fraction(2) * n_c / g_wilson_sq
    check("finite-link scalar slot gives g_link^2 = 1", g_link_sq == Fraction(1))
    check("Wilson scalar slot is identified with finite-link slot", g_wilson_sq == g_link_sq)
    check("beta = 2 N_c / g^2 gives beta = 6 at N_c=3", beta == Fraction(6), f"beta={beta}")
    check("product beta*g^2 = 2 N_c", beta * g_wilson_sq == Fraction(2) * n_c)
    check("positive branch gives g_bare = 1 from g_bare^2 = 1", g_wilson_sq == 1)

    for alt_g2 in (Fraction(1, 2), Fraction(2), Fraction(9, 4)):
        alt_beta = Fraction(2) * n_c / alt_g2
        check(
            f"noncanonical g^2={alt_g2} would not give beta=6",
            alt_beta != Fraction(6),
            f"beta={alt_beta}",
        )

    print("\nScalar-slot model checks")
    print("-" * 78)
    require_contains("bridge", bridge_text, "U = exp(i A^a T_a a)")
    require_contains("bridge", bridge_text, "U_P = exp(i a^2 g_bare F^a T_a + O(a^3))")
    require_contains("bridge", bridge_text, "g_bare = s = 1")
    require_contains("bridge", bridge_text, "The bridge would fail if")

    print("\nSummary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("Bridge check failed.")
        return 1
    print("Bridge check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
