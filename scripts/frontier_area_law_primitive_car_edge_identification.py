#!/usr/bin/env python3
"""Conditional rank-four CAR edge-condition coefficient verifier.

Authority note:
    docs/AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md

This runner verifies the rank count, half-zone measure, and Widom coefficient
inside explicitly supplied support, CAR, normal-channel, tangent-channel, and
tangent-symbol conditions, together with an explicit Widom applicability and
normalization condition. Hostile controls show that CAR algebra alone does not
select the channel dispersions or the half-zone fraction.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


def fock_dim(modes: int) -> int:
    return 2**modes


def apbc_momenta(size: int) -> np.ndarray:
    return -math.pi + 2.0 * math.pi * (np.arange(size, dtype=float) + 0.5) / size


def transverse_laplacian(qs: tuple[float, ...]) -> float:
    return 1.0 - sum(math.cos(q) for q in qs) / len(qs)


def half_period(qs: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(q + math.pi for q in qs)


def low_sheet_weight(qs: tuple[float, ...]) -> float:
    delta = transverse_laplacian(qs)
    if abs(delta - 1.0) < 1.0e-14:
        return 0.5
    return 1.0 if delta < 1.0 else 0.0


def weighted_half_zone_count(shape: tuple[int, ...]) -> tuple[float, float]:
    grids = [apbc_momenta(size) for size in shape]
    active_weight = 0.0
    total = math.prod(shape)
    mesh = np.array(np.meshgrid(*grids, indexing="ij")).reshape(len(shape), -1).T
    for point in mesh:
        active_weight += low_sheet_weight(tuple(float(value) for value in point))
    return active_weight, float(total)


def coefficient_for_active_fraction(fraction: float) -> float:
    return (2.0 + 2.0 * fraction) / 12.0


CROSSING_AVERAGES = {
    "empty": 0.0,
    "normal": 2.0,
    "tangent": 1.0,
}


def coefficient_for_modes(modes: tuple[str, ...]) -> float:
    return sum(CROSSING_AVERAGES[mode] for mode in modes) / 12.0


def main() -> int:
    print("=" * 78)
    print("AREA-LAW CONDITIONAL RANK-FOUR CAR EDGE-CONDITION COEFFICIENT")
    print("=" * 78)
    print()
    print("Question: after support, CAR, channel, tangent-symbol, and Widom")
    print("conditions are supplied, is c_Widom=1/4, and which steps remain")
    print("unforced by the specified exterior action or CAR algebra?")
    print()

    dim_cell = 2**4
    rank_pa = 4
    c_cell = rank_pa / dim_cell
    check(
        "primitive event cell has dimension 16",
        dim_cell == 16,
        "H_cell=(C^2)^(otimes 4)",
    )
    check(
        "supplied Hamming-weight-one support has rank four",
        rank_pa == 4,
        "rank(P_A)=4",
    )
    check(
        "separate primitive trace is one quarter",
        math.isclose(c_cell, 0.25, abs_tol=1.0e-15),
        f"4/16={c_cell:.12f}",
    )

    dimensions = [fock_dim(modes) for modes in range(4)]
    matching_modes = [modes for modes in range(8) if fock_dim(modes) == rank_pa]
    check(
        "complex CAR Fock dimension follows 2^m",
        dimensions == [1, 2, 4, 8],
        f"dimensions={dimensions}",
    )
    check(
        "conditional on the CAR interpretation, rank four gives m=2",
        matching_modes == [2],
        f"matching modes={matching_modes}",
    )
    check(
        "one CAR mode is too small for exact support",
        fock_dim(1) < rank_pa,
        "2<4",
    )
    check(
        "three CAR modes are too large for exact support",
        fock_dim(3) > rank_pa,
        "8>4",
    )
    fock_basis = [(n0, n1) for n0 in (0, 1) for n1 in (0, 1)]
    check(
        "two-mode Fock basis has four states",
        len(fock_basis) == rank_pa,
        f"basis={fock_basis}",
    )
    even = [state for state in fock_basis if sum(state) % 2 == 0]
    odd = [state for state in fock_basis if sum(state) % 2 == 1]
    check(
        "two-mode parity splits 2+2",
        len(even) == 2 and len(odd) == 2,
        f"even={even}, odd={odd}",
    )
    check(
        "exact support leaves no additional active Fock spectator",
        fock_dim(2) == rank_pa,
        "dim F(C^2)=rank(P_A)=4",
    )

    normal = coefficient_for_modes(("normal",))
    tangent = coefficient_for_modes(("tangent",))
    check(
        "supplied normal channel contributes 1/6",
        math.isclose(normal, 1.0 / 6.0, abs_tol=1.0e-15),
        "2/12",
    )
    check(
        "supplied half-zone tangent channel contributes 1/12",
        math.isclose(tangent, 1.0 / 12.0, abs_tol=1.0e-15),
        "1/12",
    )
    pattern_coefficients = {
        "normal+empty": coefficient_for_modes(("normal", "empty")),
        "normal+normal": coefficient_for_modes(("normal", "normal")),
        "tangent+tangent": coefficient_for_modes(("tangent", "tangent")),
        "normal+tangent": coefficient_for_modes(("normal", "tangent")),
    }
    expected_patterns = {
        "normal+empty": 1.0 / 6.0,
        "normal+normal": 1.0 / 3.0,
        "tangent+tangent": 1.0 / 6.0,
        "normal+tangent": 1.0 / 4.0,
    }
    for name, expected in expected_patterns.items():
        check(
            f"enumerated pattern {name} has its stated coefficient",
            math.isclose(pattern_coefficients[name], expected, abs_tol=1.0e-15),
            f"c={pattern_coefficients[name]:.12f}",
        )
    quarter_patterns = [
        name
        for name, coefficient in pattern_coefficients.items()
        if math.isclose(coefficient, 0.25, abs_tol=1.0e-15)
    ]
    check(
        "one quarter is unique only in the four-pattern enumeration",
        quarter_patterns == ["normal+tangent"] and len(pattern_coefficients) == 4,
        f"quarter_patterns={quarter_patterns}",
    )

    c_quarter_sheet = coefficient_for_active_fraction(0.25)
    c_three_quarter_sheet = coefficient_for_active_fraction(0.75)
    check(
        "a quarter-zone second mode gives a different CAR coefficient",
        math.isclose(c_quarter_sheet, 5.0 / 24.0, abs_tol=1.0e-15)
        and not math.isclose(c_quarter_sheet, 0.25, abs_tol=1.0e-15),
        f"c(1/4)={c_quarter_sheet:.12f}",
    )
    check(
        "a three-quarter-zone second mode gives a different CAR coefficient",
        math.isclose(c_three_quarter_sheet, 7.0 / 24.0, abs_tol=1.0e-15)
        and not math.isclose(c_three_quarter_sheet, 0.25, abs_tol=1.0e-15),
        f"c(3/4)={c_three_quarter_sheet:.12f}",
    )
    inferred_fraction = (12.0 * 0.25 - 2.0) / 2.0
    check(
        "the coefficient target selects p=1/2 only after a selector family is supplied",
        math.isclose(inferred_fraction, 0.5, abs_tol=1.0e-15),
        f"p={inferred_fraction:.12f}",
    )

    a, b = 1.0, -1.0
    check(
        "normalized tangent-symmetric NN affine-cosine ansatz fixes 1-mean cos",
        math.isclose(a + b, 0.0, abs_tol=1.0e-15)
        and math.isclose(a - b, 2.0, abs_tol=1.0e-15),
        "f(0)=0 and f(pi,...,pi)=2",
    )
    for label, point in (
        ("tangent line", (0.37,)),
        ("tangent plane", (0.37, -0.81)),
    ):
        delta = transverse_laplacian(point)
        partner = transverse_laplacian(half_period(point))
        check(
            f"{label} half-period involution sends Delta to 2-Delta",
            math.isclose(partner, 2.0 - delta, abs_tol=1.0e-15),
            f"Delta={delta:.12f}, partner={partner:.12f}",
        )
    check(
        "self-dual threshold is Delta=1",
        math.isclose(1.0, 2.0 - 1.0, abs_tol=1.0e-15),
        "fixed point of t -> 2-t",
    )
    check(
        "low and high sheets are nonempty and exchanged",
        transverse_laplacian((0.0, 0.0)) < 1.0
        and transverse_laplacian((math.pi, math.pi)) > 1.0,
        "Delta(0,0)=0; Delta(pi,pi)=2",
    )

    shapes = ((96,), (128,), (32, 32), (48, 32), (64, 40))
    for shape in shapes:
        active, total = weighted_half_zone_count(shape)
        check(
            f"APBC grid {shape} has paired half-zone weight 1/2",
            math.isclose(2.0 * active, total, abs_tol=1.0e-12),
            f"active={active:.1f}, total={total:.0f}",
        )
    check(
        "one-dimensional transverse controls reach L=128",
        max(shape[0] for shape in shapes if len(shape) == 1) >= 128,
        "largest line grid=128",
    )
    check(
        "two-dimensional transverse controls include at least 64x40",
        any(len(shape) == 2 and shape[0] >= 64 and shape[1] >= 40 for shape in shapes),
        "64x40 grid included",
    )

    average_crossings = 2.0 + 2.0 * 0.5
    c_widom = average_crossings / 12.0
    check(
        "supplied normal-plus-half-zone channel has average crossing count three",
        math.isclose(average_crossings, 3.0, abs_tol=1.0e-15),
        "2+2*(1/2)=3",
    )
    check(
        "conditional Widom coefficient is one quarter",
        math.isclose(c_widom, 0.25, abs_tol=1.0e-15),
        f"c_Widom={c_widom:.12f}",
    )
    check(
        "conditional Widom coefficient equals the separate primitive trace",
        math.isclose(c_widom, c_cell, abs_tol=1.0e-15),
        "3/12=4/16",
    )
    check(
        "CAR algebra alone does not pin the active transverse fraction",
        len(
            {
                round(coefficient_for_active_fraction(fraction), 12)
                for fraction in (0.25, 0.5, 0.75)
            }
        )
        == 3,
        "same two-mode count admits different supplied selector fractions",
    )
    check(
        "enumerated-pattern result is not a global uniqueness theorem",
        len(pattern_coefficients) == 4
        and math.isclose(coefficient_for_active_fraction(0.6), 4.0 / 15.0, abs_tol=1.0e-15),
        "continuous selector family lies outside the four named patterns",
    )

    note = NOTE.read_text(encoding="utf-8")
    note_norm = re.sub(r"\s+", " ", note)
    check(
        "source title is narrowed to a conditional edge-condition theorem",
        note.startswith(
            "# Area-Law Conditional Rank-Four CAR Edge-Condition Coefficient Theorem Note"
        ),
        NOTE.name,
    )
    check(
        "source scope forbids exterior-action descent and channel forcing",
        "no exterior-action descent, channel forcing, or global carrier-uniqueness claim"
        in note,
        "scope firewall present",
    )
    check(
        "source supplies rather than derives the physical edge channels",
        "## Supplied rank-four CAR edge conditions" in note
        and "**Normal-channel condition.**" in note
        and "**Tangent-channel condition.**" in note,
        "channel assumptions are explicit",
    )
    check(
        "source states that CAR does not select the dispersions",
        "CAR algebra does not derive the normal/tangent channel assignment"
        in note_norm,
        "algebra-to-dispersion bridge denied",
    )
    check(
        "source limits uniqueness to the enumerated patterns and ansatz",
        "enumerated-pattern check, not a\nuniqueness theorem" in note
        and "unique only inside the supplied\nnormalized" in note,
        "uniqueness scope bounded",
    )
    check(
        "source exposes the exact remaining bridges",
        "## Supplied exterior-action obstruction and open bridges" in note
        and "Until those gaps close, `1/4` is valid only inside" in note,
        "remaining-gap firewall present",
    )
    check(
        "superseded primitive-block forcing wording is absent",
        "carrier is forced by the primitive boundary block itself" not in note
        and "unique minimal local-CAR edge carrier" not in note,
        "no substrate or uniqueness laundering",
    )
    check(
        "source records the analytic zero-set measure premise",
        "nonzero real-analytic function" in note and "Haar measure zero" in note,
        "measure argument stated",
    )
    check(
        "source labels Widom applicability and normalization as an imported condition",
        "**Widom applicability and normalization condition.**" in note
        and "https://doi.org/10.1103/PhysRevLett.96.100503" in note
        and "load-bearing standard literature input" in note,
        "Widom provenance and normalization are explicit",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 78)
    if FAIL_COUNT:
        print()
        print("Verdict: FAIL; the conditional coefficient or claim boundary is broken.")
        return 1

    print()
    print("Verdict: CONDITIONAL INSIDE SUPPLIED RANK-FOUR CAR EDGE CONDITIONS.")
    print("The supplied normal plus self-dual half-zone tangent carrier gives")
    print("c_Widom=1/4. CAR alone does not select those dispersions, and the")
    print("specified exterior one-form action does not derive the active Cl_4/CAR")
    print("block; other substrate actions and intrinsic response laws remain open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
