#!/usr/bin/env python3
"""Finite declared-inventory arithmetic for the SM relativistic DOF row."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import prod
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class InventoryEntry:
    name: str
    factors: tuple[int, ...]
    expected: int

    @property
    def count(self) -> int:
        return prod(self.factors)


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


BOSONS = [
    InventoryEntry("gluons", (8, 2), 16),
    InventoryEntry("su2_l_gauge_bosons", (3, 2), 6),
    InventoryEntry("u1_y_gauge_boson", (1, 2), 2),
    InventoryEntry("complex_higgs_doublet", (4,), 4),
]

FERMIONS = [
    InventoryEntry("quarks", (6, 3, 2, 2), 72),
    InventoryEntry("charged_leptons", (3, 2, 2), 12),
    InventoryEntry("active_neutrinos", (3, 2), 6),
]

BROKEN_BOSONS = [
    InventoryEntry("gluons_broken_bookkeeping", (8, 2), 16),
    InventoryEntry("photon", (1, 2), 2),
    InventoryEntry("massive_w_w_z", (3, 3), 9),
    InventoryEntry("higgs_scalar", (1,), 1),
]


def note_boundary_checks() -> None:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "finite declared-inventory arithmetic certificate",
        "not a framework derivation",
        "does not claim:",
        "a framework derivation of the Standard Model particle inventory",
        "a framework derivation of the fermion thermal factor",
        "any new axiom or audit verdict",
        "Downstream physical use of `g_* = 106.75` still has to carry",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "one-hop dependency rather than carry the count",
        "This wrapper note is a named-import-only bounded theorem",
        "This count is NOT derived",
    ]
    for phrase in forbidden:
        check(f"note omits stale wrapper phrase: {phrase}", phrase not in text)


def inventory_checks() -> None:
    print("\n=== finite inventory arithmetic ===")
    for entry in [*BOSONS, *FERMIONS, *BROKEN_BOSONS]:
        check(
            f"{entry.name} count",
            entry.count == entry.expected,
            f"{entry.factors} -> {entry.count}",
        )

    g_bosonic = sum(entry.count for entry in BOSONS)
    g_fermionic = sum(entry.count for entry in FERMIONS)
    broken_bosonic = sum(entry.count for entry in BROKEN_BOSONS)
    fermion_weight = Fraction(7, 8)
    g_star = Fraction(g_bosonic, 1) + fermion_weight * g_fermionic

    check("bosonic total is 28", g_bosonic == 28, str(g_bosonic))
    check("fermionic total is 90", g_fermionic == 90, str(g_fermionic))
    check("broken-phase bosonic total matches unbroken total", broken_bosonic == g_bosonic, str(broken_bosonic))
    check("fermion weight is 7/8", fermion_weight == Fraction(7, 8), str(fermion_weight))
    check("g_star exact fraction is 427/4", g_star == Fraction(427, 4), str(g_star))
    check("g_star decimal is 106.75", float(g_star) == 106.75, str(float(g_star)))
    check("no right-handed-neutrino states are counted", FERMIONS[-1].count == 6, str(FERMIONS[-1].count))


def main() -> int:
    note_boundary_checks()
    inventory_checks()
    print("\nSM relativistic DOF finite inventory certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
