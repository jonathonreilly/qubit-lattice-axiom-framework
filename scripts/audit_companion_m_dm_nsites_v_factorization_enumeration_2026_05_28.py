#!/usr/bin/env python3
"""Audit companion for the integer-16 factorization catalog.

The source note is a bounded catalog, not a derivation of
``m_DM = N_sites * v``. This runner checks only stable arithmetic and
source-surface hygiene: exact factorization identities, source-reading
distinctness, cited file presence, and anti-overclaim text in the note.
"""

from __future__ import annotations

from fractions import Fraction
import sys
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    note_path = repo_root / "docs" / "M_DM_NSITES_V_INTEGER_16_FACTORIZATION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-28.md"

    print("=" * 88)
    print("INTEGER-16 FACTORIZATION CATALOG COMPANION")
    print("Scope: exact arithmetic plus source-boundary hygiene only.")
    print("=" * 88)

    section("Part 1: exact arithmetic identities")
    d = sp.Integer(4)
    nc = sp.Integer(3)
    c_f = sp.Rational(nc**2 - 1, 2 * nc)
    two_c_f = 2 * c_f
    n_spinor = sp.Integer(2) ** (d // 2)
    n_taste = sp.Integer(2) ** (d // 2)
    l_t = sp.Integer(4)

    check("F1 arithmetic: 2^4 = 16", sp.Integer(2) ** d == 16)
    check("SU(3) C_F at N_c=3 equals 4/3", c_f == sp.Rational(4, 3), f"C_F={c_f}")
    check("F2 first factor: 2 C_F = 8/3", two_c_f == sp.Rational(8, 3), f"2 C_F={two_c_f}")
    check("F2 arithmetic: (8/3) * 6 = 16", two_c_f * 6 == 16)
    check("F2 arithmetic by Fraction independent path", Fraction(8, 3) * Fraction(6, 1) == Fraction(16, 1))
    check("F3 spinor factor at d=4 is 4", n_spinor == 4, f"N_spinor={n_spinor}")
    check("F3 taste factor at d=4 is 4", n_taste == 4, f"N_taste={n_taste}")
    check("F3 arithmetic: 4 * 4 = 16", n_spinor * n_taste == 16)
    check("F4 arithmetic: L_t * 4 = 16 at L_t=4", l_t * 4 == 16)
    check("Klein-four orbit count ceil(L_t/4)=1 at L_t=4", sp.ceiling(l_t / 4) == 1)

    section("Part 2: divisor and source-reading distinctness")
    divisors = [n for n in range(1, 17) if 16 % n == 0]
    integer_pairs = [(a, 16 // a) for a in divisors if a <= 16 // a]
    check("positive divisors of 16 are {1,2,4,8,16}", divisors == [1, 2, 4, 8, 16], str(divisors))
    check("integer divisor pairs are (1,16), (2,8), (4,4)", integer_pairs == [(1, 16), (2, 8), (4, 4)], str(integer_pairs))
    check("F2 rational factorization is not an integer divisor pair", Fraction(8, 3).denominator != 1)
    readings = {
        "F1": ("BZ corners", "Wick-rotated Z4"),
        "F2": ("SU3 Casimir", "Wilson bare"),
        "F3": ("chirality-pair", "half-cube parity"),
        "F4": ("Klein-four Lt=4", "chirality-pair"),
    }
    check("four catalog labels are present", sorted(readings) == ["F1", "F2", "F3", "F4"])
    check("F3 and F4 share arithmetic but have different source readings", readings["F3"] != readings["F4"])
    check("all four source readings are distinct", len(set(readings.values())) == 4)

    section("Part 3: cited source files")
    cited = [
        "docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md",
        "docs/CL3_CHIRAL_CUBE_WILSON_HOP_DOUBLING_FORECLOSED_NARROW_NO_GO_NOTE_2026-05-27.md",
        "docs/STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
        "docs/OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md",
        "docs/DM_ETA_BOUNDED_PREDICTION_FROM_SUPPLIED_NSITES_V_NARROW_THEOREM_NOTE_2026-05-28.md",
    ]
    for rel in cited:
        check(f"cited file exists: {rel}", (repo_root / rel).is_file())

    section("Part 4: source-note boundary hygiene")
    if not note_path.is_file():
        check("source note exists", False, str(note_path))
    else:
        text = note_path.read_text(encoding="utf-8")
        required = [
            "**Type:** bounded_theorem",
            "**Audit status:** assigned only by the independent audit lane.",
            "does not derive `m_DM = N_sites · v`",
            "does not assign audit status",
            "does not ship a new no-go",
            "not a claim that no future source can introduce another reading",
            "The audit ledger is the authority for live effective status.",
            "F1",
            "F2",
            "F3",
            "F4",
        ]
        for needle in required:
            check(f"required source boundary text: {needle[:64]!r}", needle in text)
        forbidden = [
            "audited_clean",
            "promotes the bounded eta prediction",
            "closes m_DM = N_sites · v",
            "new axiom proposed",
            "lattice-realization-invariant by definition",
        ]
        for needle in forbidden:
            check(f"forbidden source overclaim absent: {needle!r}", needle not in text)

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
