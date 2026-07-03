#!/usr/bin/env python3
"""Exact structural checks for the CKM mass-basis NNI identities.

This runner isolates the algebraic T1-T4 source theorem used by the older
Cabibbo mass-basis NNI route. It uses no quark masses, CKM comparators,
PDG values, or fitted coefficients.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md"
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def symbolic_checks() -> None:
    print("CKM mass-basis NNI structural identities")
    print("No PDG masses, CKM comparators, fitted coefficients, or observed targets are used.")
    print()

    m1, m2, m3 = sp.symbols("m1 m2 m3", positive=True)
    c12, c23 = sp.symbols("c12 c23", positive=True)

    r12 = sp.sqrt(m1 / m2)
    r23 = sp.sqrt(m2 / m3)
    r13 = sp.sqrt(m1 / m3)

    c13_geom = c12 * c23
    m12_geom = c12 * sp.sqrt(m1 * m2)
    m23_geom = c23 * sp.sqrt(m2 * m3)
    m13_geom = c13_geom * sp.sqrt(m1 * m3)

    c12_phys = c12 * r12
    c23_phys = c23 * r23
    c13_phys = c13_geom * r13

    check(
        "T1 symbolic chain rule",
        is_zero(r13 - r12 * r23),
        "sqrt(m1/m3) - sqrt(m1/m2)*sqrt(m2/m3) = 0",
    )
    check(
        "T2 symbolic geometric normalization",
        is_zero(m13_geom / (m12_geom * m23_geom) - 1 / m2),
        "M13/(M12*M23) - 1/m2 = 0",
    )
    check(
        "T3 symbolic phys-map closure",
        is_zero(c13_phys - c12_phys * c23_phys),
        "c13_phys - c12_phys*c23_phys = 0",
    )

    gap = sp.simplify(c13_phys / c13_geom)
    check(
        "T4 symbolic gap ratio",
        is_zero(gap - r13),
        "c13_phys/c13_geom - sqrt(m1/m3) = 0",
    )
    check(
        "T4 coefficient independence in c12",
        is_zero(sp.diff(gap, c12)),
        "d/dc12 gap = 0",
    )
    check(
        "T4 coefficient independence in c23",
        is_zero(sp.diff(gap, c23)),
        "d/dc23 gap = 0",
    )


def rational_controls() -> None:
    print()
    print("Deterministic exact rational controls")

    samples = [
        (sp.Rational(1, 25), sp.Rational(4, 9), sp.Rational(49, 4), sp.Rational(2, 3), sp.Rational(5, 7)),
        (sp.Rational(9, 100), sp.Rational(16, 9), sp.Rational(81, 4), sp.Rational(7, 5), sp.Rational(11, 13)),
        (sp.Rational(1, 64), sp.Rational(25, 16), sp.Rational(121, 9), sp.Rational(3, 2), sp.Rational(17, 19)),
    ]

    for idx, (m1, m2, m3, c12, c23) in enumerate(samples, start=1):
        r12 = sp.sqrt(m1 / m2)
        r23 = sp.sqrt(m2 / m3)
        r13 = sp.sqrt(m1 / m3)
        c13_geom = c12 * c23
        m12_geom = c12 * sp.sqrt(m1 * m2)
        m23_geom = c23 * sp.sqrt(m2 * m3)
        m13_geom = c13_geom * sp.sqrt(m1 * m3)
        c12_phys = c12 * r12
        c23_phys = c23 * r23
        c13_phys = c13_geom * r13

        check(f"control {idx}: T1", is_zero(r13 - r12 * r23))
        check(f"control {idx}: T2", is_zero(m13_geom / (m12_geom * m23_geom) - 1 / m2))
        check(f"control {idx}: T3", is_zero(c13_phys - c12_phys * c23_phys))
        check(f"control {idx}: T4", is_zero(c13_phys / c13_geom - r13))


def textual_checks() -> None:
    print()
    print("Companion note boundary checks")
    note = NOTE.read_text(encoding="utf-8")
    note_normalized = " ".join(note.split())
    check(
        "note uses canonical positive_theorem metadata",
        "**Type:** positive_theorem" in note and "**Claim type:** positive_theorem" in note,
    )
    check(
        "note links this runner and cached output",
        "scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py" in note
        and "logs/runner-cache/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.txt" in note,
    )
    check(
        "note keeps calibrated Cabibbo value outside the theorem",
        "No quark masses" in note_normalized
        and "CKM entries" in note_normalized
        and "fitted coefficients" in note_normalized
        and "PDG values" in note_normalized
        and "observed target values enter" in note_normalized
        and "may not use this file as a first-principles derivation of the numerical value" in note_normalized
        and "Cabibbo comparison remains a bounded/import-dependent illustration" in note_normalized,
    )


def main() -> int:
    symbolic_checks()
    rational_controls()
    textual_checks()
    print()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
