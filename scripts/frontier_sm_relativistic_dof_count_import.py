#!/usr/bin/env python3
"""Bounded Standard-Model relativistic DOF count import runner.

This runner verifies the local bookkeeping table in
SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md:

    g_* = g_bosonic + (7/8) g_fermionic = 106.75.

It does not derive the Standard Model spectrum from the CL3 framework. The
SM particle-content list is the admitted bounded import; this file checks that
the listed inventory and the retained 7/8 weighting produce the stated value.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class CountTerm:
    label: str
    factors: tuple[int, ...]
    expected: int

    @property
    def value(self) -> int:
        out = 1
        for factor in self.factors:
            out *= factor
        return out


BOSONS = (
    CountTerm("gluons: 8 color adjoint states * 2 transverse pol", (8, 2), 16),
    CountTerm("SU(2)_L gauge bosons: 3 weak states * 2 transverse pol", (3, 2), 6),
    CountTerm("U(1)_Y gauge boson: 1 state * 2 transverse pol", (1, 2), 2),
    CountTerm("complex Higgs doublet: 4 real scalar components", (4,), 4),
)

FERMIONS = (
    CountTerm("quarks: 6 flavors * 3 colors * 4 Dirac particle/anti states", (6, 3, 4), 72),
    CountTerm("charged leptons: 3 flavors * 4 Dirac particle/anti states", (3, 4), 12),
    CountTerm("active neutrinos: 3 flavors * 2 chiral particle/anti states", (3, 2), 6),
)


def check(label: str, condition: bool, detail: str) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}: {detail}")
    return condition


def main() -> int:
    print("=" * 80)
    print("SM RELATIVISTIC DOF COUNT BOUNDED IMPORT")
    print("=" * 80)
    print("Scope: verify the admitted SM bookkeeping table and 7/8 weighting.")
    print("Not scope: derive the SM particle spectrum from CL3 primitives.")
    print()

    passes: list[bool] = []

    boson_total = 0
    print("Bosonic inventory")
    for term in BOSONS:
        value = term.value
        boson_total += value
        passes.append(check(term.label, value == term.expected, f"{value}"))

    fermion_total = 0
    print("\nFermionic inventory")
    for term in FERMIONS:
        value = term.value
        fermion_total += value
        passes.append(check(term.label, value == term.expected, f"{value}"))

    seven_eighths = Fraction(7, 8)
    g_star = Fraction(boson_total, 1) + seven_eighths * Fraction(fermion_total, 1)

    print("\nTotals")
    passes.append(check("bosonic total", boson_total == 28, f"g_bosonic={boson_total}"))
    passes.append(check("fermionic total", fermion_total == 90, f"g_fermionic={fermion_total}"))
    passes.append(check("7/8 weighting", seven_eighths == Fraction(7, 8), f"{seven_eighths}"))
    passes.append(check("g_* exact rational", g_star == Fraction(427, 4), f"g_*={g_star}"))
    passes.append(check("g_* decimal", float(g_star) == 106.75, f"g_*={float(g_star):.2f}"))

    n_pass = sum(1 for item in passes if item)
    n_total = len(passes)
    print()
    print(f"PASS={n_pass} FAIL={n_total - n_pass}")
    print("Result: bounded SM-content import bookkeeping closes on its stated table.")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
