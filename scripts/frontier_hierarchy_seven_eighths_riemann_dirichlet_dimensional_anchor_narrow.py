#!/usr/bin/env python3
"""Exact runner for the repaired 7/8 dimensional-anchor narrow theorem.

For integer d >= 2, define

    R_lat(c) = (c + 1/2)/(c + 1), with c = d - 1,
    R_RD(d)  = eta(d)/zeta(d) = 1 - 2^(1-d),
    A(d)     = 2^(d-2) - d.

The theorem is

    R_lat(d-1) = R_RD(d)  iff  A(d) = 0  iff  d = 4,

with exact d=4 tuple

    (R_lat(3), R_RD(4), A(4)) = (7/8, 7/8, 0).

The two ratios equal 7/8 while the separate alignment residual vanishes.
The runner includes hostile arithmetic and source-prose controls that fail
if the residual is incorrectly treated as another 7/8-valued quantity.

The finite L_t trigonometric checks are preserved as non-load-bearing
context only; they do not assert physical or all-L_t selection.

Target: PASS = 20, FAIL = 0.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

try:
    import sympy as sp
    from sympy import Rational, simplify, sin, symbols
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


def r_lat(c: int) -> Fraction:
    return (Fraction(c) + Fraction(1, 2)) / (Fraction(c) + 1)


def r_rd(d: int) -> Fraction:
    return Fraction(1) - Fraction(1, 2 ** (d - 1))


def alignment_residual(d: int) -> int:
    return 2 ** (d - 2) - d


section("Context only: finite APBC sin^2 checks")

lt4_values = [
    simplify(sin((2 * n + 1) * sp.pi / 4) ** 2)
    for n in range(4)
]
check(
    "T1: L_t=4 sampled sin^2 values are uniformly 1/2",
    all(value == Rational(1, 2) for value in lt4_values),
    detail=f"values = {[str(value) for value in lt4_values]}",
)

lt6_values = [
    simplify(sin((2 * n + 1) * sp.pi / 6) ** 2)
    for n in range(6)
]
expected_lt6 = [
    Rational(1, 4),
    Rational(1),
    Rational(1, 4),
    Rational(1, 4),
    Rational(1),
    Rational(1, 4),
]
check(
    "T2: L_t=6 sampled sin^2 values have the exact non-uniform pattern",
    lt6_values == expected_lt6 and len(set(lt6_values)) > 1,
    detail=f"values = {[str(value) for value in lt6_values]}",
)

lt8_values = [
    simplify(sin((2 * n + 1) * sp.pi / 8) ** 2)
    for n in range(8)
]
check(
    "T3: L_t=8 sampled sin^2 values are non-uniform",
    len({simplify(value) for value in lt8_values}) > 1,
    detail=f"distinct = {sorted({str(value) for value in lt8_values})}",
)


section("Exact definitions and d=4 values")

c_sym, d_sym = symbols("c d", positive=True, integer=True)
lattice_from_c = (c_sym + Rational(1, 2)) / (c_sym + 1)
lattice_at_d = simplify(lattice_from_c.subs(c_sym, d_sym - 1))
lattice_closed = 1 - Rational(1, 2) / d_sym
check(
    "T4: (c+1/2)/(c+1) at c=d-1 equals 1-1/(2d)",
    simplify(lattice_at_d - lattice_closed) == 0,
    detail=f"difference = {simplify(lattice_at_d - lattice_closed)}",
)

s_sym = symbols("s", real=True)
zeta_symbol = symbols("Z", nonzero=True)
even_part = 2 ** (-s_sym) * zeta_symbol
odd_part = (1 - 2 ** (-s_sym)) * zeta_symbol
eta_from_split = odd_part - even_part
rd_closed = 1 - 2 ** (1 - s_sym)
check(
    "T5: odd/even split gives eta(s)/zeta(s)=1-2^(1-s)",
    simplify(eta_from_split / zeta_symbol - rd_closed) == 0,
    detail=f"difference = {simplify(eta_from_split / zeta_symbol - rd_closed)}",
)

d4_lat = r_lat(3)
d4_rd = r_rd(4)
d4_residual = alignment_residual(4)
check(
    "T6: R_lat(3)=7/8",
    d4_lat == Fraction(7, 8),
    detail=f"R_lat(3) = {d4_lat}",
)
check(
    "T7: R_RD(4)=eta(4)/zeta(4)=7/8",
    d4_rd == Fraction(7, 8),
    detail=f"R_RD(4) = {d4_rd}",
)
check(
    "T8: A(4)=2^(4-2)-4=0",
    d4_residual == 0,
    detail=f"A(4) = {d4_residual}",
)

d4_tuple = (d4_lat, d4_rd, d4_residual)
check(
    "T9: exact d=4 tuple is (7/8, 7/8, 0)",
    d4_tuple == (Fraction(7, 8), Fraction(7, 8), 0),
    detail=f"tuple = {d4_tuple}",
)
check(
    "T10 hostile: old mismatched tuple (7/8, 7/8, 7/8) is rejected",
    d4_tuple != (Fraction(7, 8), Fraction(7, 8), Fraction(7, 8))
    and Fraction(d4_residual) != Fraction(7, 8),
    detail=f"residual = {d4_residual}, not 7/8",
)


section("Ratio-gap/residual equivalence and integer uniqueness")

gap_symbolic = simplify(
    (1 - Rational(1, 2) / d_sym)
    - (1 - 2 ** (1 - d_sym))
)
residual_symbolic = 2 ** (d_sym - 2) - d_sym
bridge_identity = simplify(
    gap_symbolic + residual_symbolic / (d_sym * 2 ** (d_sym - 1))
)
check(
    "T11: R_lat(d-1)-R_RD(d)=-A(d)/(d*2^(d-1)) symbolically",
    bridge_identity == 0,
    detail=f"difference = {bridge_identity}",
)

scan = {}
equivalence_holds = True
for d in range(2, 65):
    gap = r_lat(d - 1) - r_rd(d)
    residual = alignment_residual(d)
    scan[d] = (gap, residual)
    if (gap == 0) != (residual == 0):
        equivalence_holds = False
check(
    "T12: exact scan d=2..64 has ratio equality iff residual zero",
    equivalence_holds,
    detail=f"zero pairs = {[d for d, pair in scan.items() if pair == (0, 0)]}",
)

scan_zeros = [d for d, (_gap, residual) in scan.items() if residual == 0]
check(
    "T13: exact scan d=2..64 finds the sole zero at d=4",
    scan_zeros == [4],
    detail=f"zeros = {scan_zeros}",
)

base_residuals = {d: alignment_residual(d) for d in (2, 3, 4, 5)}
check(
    "T14: uniqueness proof base values are A(2)=-1, A(3)=-1, A(4)=0, A(5)=3",
    base_residuals == {2: -1, 3: -1, 4: 0, 5: 3},
    detail=f"values = {base_residuals}",
)

forward_difference = simplify(
    (2 ** (d_sym - 1) - (d_sym + 1))
    - (2 ** (d_sym - 2) - d_sym)
)
check(
    "T15: A(d+1)-A(d)=2^(d-2)-1 symbolically",
    simplify(forward_difference - (2 ** (d_sym - 2) - 1)) == 0,
    detail=f"forward difference = {forward_difference}",
)

check(
    "T16: on integer d>=4 the forward difference has minimum 3 and is positive",
    2 ** (4 - 2) - 1 == 3
    and all(2 ** (d - 2) - 1 > 0 for d in range(4, 65)),
    detail="minimum at d=4 is 3; powers of two increase thereafter",
)

hostile_dimensions = (2, 3, 5, 6)
hostile_values = {
    d: (r_lat(d - 1), r_rd(d), alignment_residual(d))
    for d in hostile_dimensions
}
check(
    "T17 hostile: neighboring dimensions have unequal ratios and nonzero residual",
    all(lat != rd and residual != 0 for lat, rd, residual in hostile_values.values()),
    detail=" | ".join(
        f"d={d}: ({lat}, {rd}, {residual})"
        for d, (lat, rd, residual) in hostile_values.items()
    ),
)


section("Claim-bearing source-prose guards")

note_text = NOTE_PATH.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
required_tuple = (
    "(R_lat(3), R_RD(4), A(4)) = (7/8, 7/8, 0)."
)
check(
    "T18: source note states the corrected exact tuple",
    required_tuple in note_flat,
    detail=required_tuple,
)

required_distinction = (
    "`A(d)` is a residual, not a ratio, and is not a third "
    "`7/8`-valued quantity."
)
check(
    "T19: source note distinguishes the zero residual from the two ratios",
    required_distinction in note_flat,
    detail=required_distinction,
)

forbidden_fragments = [
    "all three quantities equal " + "`7/8`",
    "all three coincide on the rational value " + "`7/8`",
    "three independent identities all evaluate to " + "`7/8`",
    "dimensional-selector value) coincide on " + "`7/8`",
    "three quantities take three distinct rational values",
    "triple-" + "coincidence identity",
]
present_forbidden = [
    fragment for fragment in forbidden_fragments if fragment in note_flat
]
check(
    "T20 hostile: old three-way numeric-equality prose is absent from the source note",
    not present_forbidden,
    detail=f"present forbidden fragments = {present_forbidden}",
)


section("Narrow theorem summary")
print(
    """
  For integer d >= 2:

    R_lat(d-1) - R_RD(d) = -A(d)/(d*2^(d-1)),
    A(d) = 2^(d-2) - d.

  Hence the two ratios are equal exactly when the residual vanishes.
  The unique integer alignment is d=4, where

    R_lat(3) = R_RD(4) = 7/8,
    A(4) = 0.

  No physical dimension, temporal size, hierarchy parameter, or outer
  exponent is selected by this arithmetic theorem.
"""
)

print(f"\n{'=' * 88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'=' * 88}")
sys.exit(1 if FAIL else 0)
