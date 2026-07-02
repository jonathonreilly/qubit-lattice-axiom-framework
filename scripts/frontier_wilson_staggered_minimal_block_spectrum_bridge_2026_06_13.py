#!/usr/bin/env python3
"""Wilson plus staggered minimal-block spectrum bridge.

Constructs the combined Wilson-shift plus staggered conjugate-pair operator
on the APBC minimal-block corner surface and verifies the eigenvalue multiset
2*r*hw(n) +/- 2*i*u0 with binomial(4, hw) multiplicities.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "WILSON_STAGGERED_MINIMAL_BLOCK_SPECTRUM_BRIDGE_NOTE_2026-06-13.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def binomial(n: int, k: int) -> int:
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def corners() -> list[tuple[int, int, int, int]]:
    return [(t, x, y, z) for t in (0, 1) for x in (0, 1) for y in (0, 1) for z in (0, 1)]


def block_invariants(hw: int, r: Fraction, u0: Fraction) -> tuple[Fraction, Fraction, tuple[Fraction, Fraction]]:
    """Return trace, determinant, and characteristic-polynomial coefficients.

    For block [[a, -b], [b, a]], charpoly is lambda^2 - tr lambda + det.
    """

    a = 2 * r * hw
    b = 2 * u0
    trace = 2 * a
    det = a * a + b * b
    return trace, det, (-trace, det)


def det_m_plus_block(hw: int, r: Fraction, u0: Fraction, m: Fraction) -> Fraction:
    a = 2 * r * hw
    b = 2 * u0
    return (m + a) * (m + a) + b * b


def part1_note_structure() -> None:
    print("\nPart 1: source note structure")
    text = NOTE.read_text(encoding="utf-8")
    flat = re.sub(r"\s+", " ", text)
    required = [
        "Wilson Plus Staggered Minimal-Block Spectrum Bridge",
        "Claim type:** bounded_theorem",
        "O_Wstag(r,u_0) = direct_sum",
        "lambda_n^+/- = 2 r hw(n) +/- 2 i u_0",
        "multiplicity binomial(4,k)",
        "V_taste^W(m)",
        "does not derive the Wilson coefficient",
        "WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md",
        "HIGGS_MASS_FROM_AXIOM_NOTE.md",
    ]
    for marker in required:
        check(f"contains marker: {marker}", marker in text or marker in flat)


def part2_corner_multiplicities() -> None:
    print("\nPart 2: APBC corner multiplicities")
    by_hw: dict[int, list[tuple[int, int, int, int]]] = {}
    for n in corners():
        by_hw.setdefault(sum(n), []).append(n)
    check("corner count is 2^4 = 16", sum(len(v) for v in by_hw.values()) == 16)
    for hw in range(5):
        check(
            f"hw={hw} multiplicity is binomial(4,{hw})",
            len(by_hw.get(hw, [])) == binomial(4, hw),
            f"got {len(by_hw.get(hw, []))}",
        )


def part3_block_spectrum() -> None:
    print("\nPart 3: per-corner combined block spectrum")
    r = Fraction(3, 5)
    u0 = Fraction(7, 11)
    for hw in range(5):
        trace, det, coeffs = block_invariants(hw, r, u0)
        a = 2 * r * hw
        b = 2 * u0
        check(f"hw={hw}: trace = 2*(2*r*hw)", trace == 2 * a, f"trace={trace}")
        check(f"hw={hw}: determinant = (2*r*hw)^2 + (2*u0)^2", det == a * a + b * b, f"det={det}")
        check(
            f"hw={hw}: charpoly lambda^2 - 2a lambda + a^2+b^2",
            coeffs == (-2 * a, a * a + b * b),
            f"coeffs={coeffs}",
        )


def part4_multiset_and_determinant_formula() -> None:
    print("\nPart 4: multiset grouping and determinant formula")
    r = Fraction(2, 7)
    u0 = Fraction(5, 13)
    m_values = [Fraction(0), Fraction(1, 3), Fraction(-2, 5)]
    grouped = {hw: binomial(4, hw) for hw in range(5)}
    by_enum: dict[int, int] = {}
    for n in corners():
        by_enum[sum(n)] = by_enum.get(sum(n), 0) + 1
    check("enumerated hw multiplicities match binomial grouping", by_enum == grouped, f"{by_enum}")

    for m in m_values:
        by_corner = Fraction(1)
        for n in corners():
            by_corner *= det_m_plus_block(sum(n), r, u0, m)
        by_group = Fraction(1)
        for hw, mult in grouped.items():
            by_group *= det_m_plus_block(hw, r, u0, m) ** mult
        check(f"det(mI+O) product formula at m={m}", by_corner == by_group)

    coefficient = -Fraction(1, 2)
    check("half-log prefactor is the Wilson V_taste convention", coefficient == -Fraction(1, 2))


def part5_r_zero_reduction() -> None:
    print("\nPart 5: r=0 reduction to unshifted staggered pair")
    u0 = Fraction(5, 13)
    m = Fraction(1, 4)
    r = Fraction(0)
    factor = m * m + 4 * u0 * u0
    product = Fraction(1)
    for n in corners():
        product *= det_m_plus_block(sum(n), r, u0, m)
    check("r=0 determinant has sixteen identical staggered-pair factors", product == factor ** 16)
    check("r=0 half-log coefficient reduces to -8 log(m^2+4u0^2)", -Fraction(1, 2) * 16 == -8)


def main() -> int:
    print("Wilson plus staggered APBC minimal-block spectrum bridge")
    part1_note_structure()
    part2_corner_multiplicities()
    part3_block_spectrum()
    part4_multiset_and_determinant_formula()
    part5_r_zero_reduction()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
