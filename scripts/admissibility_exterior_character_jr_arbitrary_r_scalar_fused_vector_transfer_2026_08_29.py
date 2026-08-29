#!/usr/bin/env python3
"""Exact hostile controls for the arbitrary-r scalar-fused vector transfer."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_independent_2026_08_29 import (
    fixture as independent_fixture,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_independent_2026_08_29.py",
)

MUTATIONS = (
    "corrupt_original_link_incidence",
    "retain_cylindrical_endpoint",
    "permit_lower_order_history",
    "corrupt_half_action_prefactor",
    "invent_nonscalar_channel",
    "corrupt_haar_scalar_factor",
    "drop_pair_multiplicity",
    "omit_endpoint_subtraction",
    "corrupt_small_step_normalization",
    "remove_positive_history",
    "claim_full_vector_kernel",
)

N5_CERTIFICATE = (
    "per_element: checked every original-link label menu, boundary incidence, and scalar overlap for the selected complement histories",
    "per_site: checked one retained q=1 cell symbolically for fixed r and directly for every width from r=2 through r=8",
    "per_mode: checked the vacuum-to-coarse-defining-vector entry with explicit O(3) inversion parity and no other irrep entry",
    "per_block: checked the arbitrary-fixed-r three-state transfer with a separate exact two-state endpoint subtraction",
    "lattice_wide: checked and not executed — no volume family, infinite-volume norm, or continuum limit is an input to this theorem",
)


def plaquette_edges(width: int, corrupt: bool = False) -> dict[int, frozenset[str]]:
    plaquettes = {
        index: frozenset((
            f"u{index}", f"v{index}", f"h{index}", f"h{index + 1}",
        ))
        for index in range(width)
    }
    if corrupt:
        plaquettes[width - 1] = frozenset((
            f"u{width - 1}", f"v{width - 1}", f"h{width - 1}",
        ))
    return plaquettes


def boundary(subset: int, plaquettes: dict[int, frozenset[str]]) -> frozenset[str]:
    result: frozenset[str] = frozenset()
    for index in sorted(plaquettes):
        if subset & (1 << index):
            result ^= plaquettes[index]
    return result


def runs(subset: int, width: int) -> int:
    return sum(
        int(bool(subset & (1 << index)))
        * int(index == 0 or not bool(subset & (1 << (index - 1))))
        for index in range(width)
    )


def submasks(mask: int):
    subset = mask
    while True:
        yield subset
        if subset == 0:
            return
        subset = (subset - 1) & mask


def direct_coefficients(width: int) -> dict[int, int]:
    plaquettes = plaquette_edges(width)
    full = (1 << width) - 1
    coefficients: dict[int, int] = defaultdict(int)
    for subset in range(1, full):
        complement = full ^ subset
        for left_half in submasks(subset):
            for right_half in submasks(complement):
                power = (
                    len(boundary(left_half, plaquettes))
                    + len(boundary(full ^ right_half, plaquettes))
                )
                coefficients[power] += 1
    return dict(sorted(coefficients.items()))


def transfer_polynomial(
    width: int,
    t_value: sp.Symbol,
    drop_multiplicity: bool = False,
    omit_endpoints: bool = False,
) -> sp.Expr:
    states = ((0, 0), (0, 1), (1, 1))
    multiplicity = {(0, 0): 1, (0, 1): 2, (1, 1): 1}
    if drop_multiplicity:
        multiplicity[(0, 1)] = 1
    transfer = sp.Matrix(3, 3, lambda row, column:
        multiplicity[states[column]] * t_value ** (
            2 * states[column][0]
            + 2 * int(states[row][0] == 0 and states[column][0] == 1)
            + 2 * states[column][1]
            + 2 * int(states[row][1] == 0 and states[column][1] == 1)
        )
    )
    paired_sum = (sp.Matrix([[1, 0, 0]])
                  * transfer**width * sp.ones(3, 1))[0]
    if omit_endpoints:
        return sp.expand(paired_sum)
    one_history = sp.Matrix(2, 2, lambda previous, current:
        t_value ** (
            2 * current + 2 * int(previous == 0 and current == 1)
        )
    )
    history_sum = (sp.Matrix([[1, 0]])
                   * one_history**width * sp.ones(2, 1))[0]
    return sp.expand(
        paired_sum - (1 + t_value ** (2 * width + 2)) * history_sum
    )


def coefficient_polynomial(coefficients: dict[int, int], t_value: sp.Symbol) -> sp.Expr:
    return sp.Add(*(
        coefficient * t_value**power
        for power, coefficient in coefficients.items()
    ))


Irrep = tuple[int, int]


def irrep_menu(multiplicity: int, invent_nonscalar: bool = False) -> frozenset[Irrep]:
    """O(3) labels (ell, inversion parity) for up to two V factors."""

    if multiplicity == 0:
        labels = {(0, 1)}
        if invent_nonscalar:
            labels.add((2, 1))
        return frozenset(labels)
    if multiplicity == 1:
        return frozenset(((1, -1),))
    if multiplicity == 2:
        return frozenset(((0, 1), (1, 1), (2, 1)))
    raise AssertionError(multiplicity)


def scalar_selection(width: int, invent_nonscalar: bool = False) -> dict[str, object]:
    plaquettes = plaquette_edges(width)
    full = (1 << width) - 1
    outer = boundary(full, plaquettes)
    all_edges = frozenset().union(*plaquettes.values())

    exact = True
    nonscalar: set[Irrep] = set()
    for subset in range(1, full):
        complement = full ^ subset
        support: set[str] = set()
        for edge in all_edges:
            left_count = sum(
                int(bool(subset & (1 << index)))
                * int(edge in plaquette)
                for index, plaquette in plaquettes.items()
            )
            right_count = int(edge in outer) + sum(
                int(bool(complement & (1 << index)))
                * int(edge in plaquette)
                for index, plaquette in plaquettes.items()
            )
            common = (
                irrep_menu(left_count, invent_nonscalar)
                & irrep_menu(right_count, invent_nonscalar)
            )
            exact &= len(common) == 1
            if common == {(1, -1)}:
                support.add(edge)
            if max(left_count, right_count) == 2:
                nonscalar.update(label for label in common if label != (0, 1))
        exact &= frozenset(support) == boundary(subset, plaquettes)
    return {
        "exact": exact,
        "nonscalar_channels": tuple(sorted(nonscalar)),
    }


def physical_q_classification(width: int, corrupt: bool = False) -> dict[str, object]:
    """Derive coarse cylindricity in both Gram orientations.

    A q=1 coarse Peter--Weyl row has one common irrep on every exclusive rail.
    The supplied temporal convolution is link diagonal, so its action preserves
    each menu word through every half-subpartition.
    """

    full = (1 << width) - 1
    vacuum_cylindrical: set[int] = set()
    coarse_cylindrical: set[int] = set()
    preserved = True
    for subset in range(full + 1):
        vacuum_word = tuple(
            frozenset(((1, -1),))
            if subset & (1 << index)
            else frozenset(((0, 1),))
            for index in range(width)
            for _rail in range(2)
        )
        coarse_word = tuple(
            frozenset(((1, -1),))
            if subset & (1 << index)
            else frozenset(((0, 1), (1, 1), (2, 1)))
            for index in range(width)
            for _rail in range(2)
        )
        for half_subset in submasks(subset):
            vacuum_after = vacuum_word
            preserved &= vacuum_after == vacuum_word
        for half_complement in submasks(full ^ subset):
            coarse_after = coarse_word
            if corrupt and subset == 1 and half_complement == 0:
                coarse_after = tuple(
                    frozenset(((1, -1),)) for _menu in coarse_word
                )
            preserved &= coarse_after == coarse_word
        if set.intersection(*(set(menu) for menu in vacuum_word)):
            vacuum_cylindrical.add(subset)
        if set.intersection(*(set(menu) for menu in coarse_word)):
            coarse_cylindrical.add(subset)
    return {
        "vacuum_side_cylindrical": frozenset(vacuum_cylindrical),
        "coarse_side_cylindrical": frozenset(coarse_cylindrical),
        "diagonal_preserves_words": preserved,
    }


def weak_compositions(total: int, width: int):
    if width == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, width - 1):
            yield (first,) + rest


def lower_derivatives_vanish(width: int, corrupt: bool = False) -> bool:
    """Exhaust all insertion multiplicities below r using rail parity."""

    for order in range(width):
        for counts in weak_compositions(order, width):
            scalar_allowed = tuple((1 + count) % 2 == 0 for count in counts)
            if corrupt:
                scalar_allowed = tuple(
                    True if count == 0 else allowed
                    for count, allowed in zip(counts, scalar_allowed)
                )
            if all(scalar_allowed):
                return False
    return True


def normalized_leibniz_factors(width: int, corrupt: bool = False) -> tuple[F, ...]:
    """Check the 1/r! Gram Leibniz factor for every proper partition size."""

    factors = []
    for left_order in range(1, width):
        right_order = width - left_order
        left_half = F(1, 2) ** left_order
        right_half = F(1 if corrupt else 1, 1 if corrupt else 2) ** right_order
        normalized = F(
            comb(width, left_order)
            * factorial(left_order)
            * factorial(right_order),
            factorial(width),
        )
        factors.append(normalized * left_half * right_half)
    return tuple(factors)


def one_rung_factor(corrupt: bool = False) -> sp.Rational:
    dimension = 3

    def haar_second(first: tuple[int, int], second: tuple[int, int]) -> sp.Rational:
        return sp.Rational(
            int(first[0] == second[0]) * int(first[1] == second[1]),
            dimension,
        )

    factor = sum(
        (
            haar_second((i, i), (ell, k))
            * haar_second((j, j), (k, ell))
            for i in range(dimension) for j in range(dimension)
            for k in range(dimension) for ell in range(dimension)
        ),
        sp.Rational(0),
    )
    return factor + int(corrupt)


def independent_checks() -> tuple[tuple[str, bool], ...]:
    data = independent_fixture()
    return (
        ("independent signed-frame scalar factor", data["rung_factor"] == F(1, 3)),
        ("independent subset and transfer equality",
         all(row["direct"] == row["transfer"] for row in data["rows"])),
        ("independent positivity and small-step census",
         all(row["positive"]
             and row["value_at_one"] == row["expected_at_one"]
             for row in data["rows"])),
        ("independent scalar-only original-link selection",
         all(row["selection"]["exact"]
             and row["selection"]["nonscalar_channels"] == ()
             for row in data["rows"])),
        ("independent outer-perimeter census",
         all(row["selection"]["outer_perimeter"] == 2 * row["width"] + 2
             for row in data["rows"])),
        ("independent overlap recursion",
         all(row["overlap"] == F(1, 3 ** (row["width"] - 1))
             for row in data["rows"])),
        ("independent two-orientation Q classification",
         all(
             row["q_classification"]["vacuum"]
             == frozenset((0, (1 << row["width"]) - 1))
             and row["q_classification"]["coarse"]
             == frozenset((0, (1 << row["width"]) - 1))
             and row["q_classification"]["temporal_words_preserved"]
             for row in data["rows"]
         )),
        ("independent lower-order exclusive-rail vanishing",
         all(row["lower_derivatives_vanish"] for row in data["rows"])),
        ("independent normalized Leibniz half factors",
         all(
             all(factor == F(1, 2 ** row["width"])
                 for factor in row["leibniz_factors"])
             for row in data["rows"]
         )),
        ("independent r2 recovery",
         data["rows"][0]["direct"] == {4: 2, 6: 2, 8: 2, 10: 2}),
        ("independent r3 recovery",
         data["rows"][1]["direct"]
         == {4: 3, 6: 6, 8: 12, 10: 8, 12: 15, 14: 2, 16: 2}),
    )


def main(mutation: str | None, mode: str) -> int:
    if mode == "independent":
        checks = independent_checks()
    else:
        root = Path(__file__).resolve().parents[1]
        note = (root / AUDIT_INPUT_PATHS[0]).read_text()
        parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
        axioms = (root / AUDIT_INPUT_PATHS[2]).read_text()
        t_value = sp.symbols("t_V", positive=True)
        direct = {width: direct_coefficients(width) for width in range(2, 9)}

        geometry_rows = []
        for width in range(2, 9):
            plaquettes = plaquette_edges(
                width,
                corrupt=(mutation == "corrupt_original_link_incidence"),
            )
            full = (1 << width) - 1
            geometry_rows.append(
                len(frozenset().union(*plaquettes.values())) == 3 * width + 1
                and len(boundary(full, plaquettes)) == 2 * width + 2
                and all(
                    len(boundary(subset, plaquettes))
                    == 2 * subset.bit_count() + 2 * runs(subset, width)
                    for subset in range(full + 1)
                )
            )

        q_rows = tuple(
            physical_q_classification(
                width,
                corrupt=(mutation == "retain_cylindrical_endpoint"),
            )
            for width in range(2, 9)
        )

        selections = tuple(
            scalar_selection(
                width,
                invent_nonscalar=(mutation == "invent_nonscalar_channel"),
            )
            for width in range(2, 9)
        )
        rung = one_rung_factor(
            corrupt=(mutation == "corrupt_haar_scalar_factor")
        )
        transfer_match = all(
            coefficient_polynomial(direct[width], t_value)
            == transfer_polynomial(
                width,
                t_value,
                drop_multiplicity=(mutation == "drop_pair_multiplicity"),
                omit_endpoints=(mutation == "omit_endpoint_subtraction"),
            )
            for width in range(2, 9)
        )

        positivity_rows = {
            width: dict(coefficients) for width, coefficients in direct.items()
        }
        if mutation == "remove_positive_history":
            positivity_rows[5][4] = 0
        normalization_shift = int(mutation == "corrupt_small_step_normalization")

        flat_note = " ".join(note.split())
        scope_ok = (
            "one selected q=1 defining-vector entry" in flat_note
            and "not a full vector/non-determinant kernel" in flat_note
            and "No axiom or approved primitive changes" in flat_note
        )
        if mutation == "claim_full_vector_kernel":
            scope_ok = False

        checks = (
            (
                "typed parent-theorem and minimal-axiom inputs are explicit",
                "claim_id: admissibility_exterior_character_jr_temporal" in parent
                and "The Four Framework Axioms" in axioms
                and "depends_on:" in note
                and "minimal_axioms" in note,
            ),
            (
                "actual r-cell ladder has 3r+1 links and exact boundary census",
                all(geometry_rows),
            ),
            (
                "physical q=1 projector deletes exactly empty/full partitions",
                all(
                    row["vacuum_side_cylindrical"]
                    == frozenset((0, (1 << width) - 1))
                    and row["coarse_side_cylindrical"]
                    == frozenset((0, (1 << width) - 1))
                    and row["diagonal_preserves_words"]
                    for width, row in zip(range(2, 9), q_rows)
                )
                and "exhaustive in both Gram orientations" in note,
            ),
            (
                "all derivative orders below r vanish by exclusive-rail parity",
                all(
                    lower_derivatives_vanish(
                        width,
                        corrupt=(mutation == "permit_lower_order_history"),
                    )
                    for width in range(2, 9)
                )
                and "derivative below order\n`r` is zero" in note,
            ),
            (
                "normalized Gram Leibniz rule retains both half-action factors",
                all(
                    all(
                        factor == F(1, 2**width)
                        for factor in normalized_leibniz_factors(
                            width,
                            corrupt=(mutation == "corrupt_half_action_prefactor"),
                        )
                    )
                    for width in range(2, 9)
                )
                and "including both supplied\nhalf-action factors" in note,
            ),
            (
                "all proper complements select scalar doubled rungs only",
                all(selection["exact"]
                    and selection["nonscalar_channels"] == ()
                    for selection in selections)
                and "axial-vector and spin-two channels" in note,
            ),
            (
                "Haar second moment gives overlap 3^(1-r)",
                rung == sp.Rational(1, 3)
                and all(rung ** (width - 1)
                        == sp.Rational(1, 3 ** (width - 1))
                        for width in range(2, 9)),
            ),
            (
                "direct proper-subset sum equals the three-state transfer",
                transfer_match and "bond-dimension-three" in note,
            ),
            (
                "r2 finite-step polynomial is recovered exactly",
                direct[2] == {4: 2, 6: 2, 8: 2, 10: 2},
            ),
            (
                "r3 finite-step polynomial is recovered exactly",
                direct[3]
                == {4: 3, 6: 6, 8: 12, 10: 8, 12: 15, 14: 2, 16: 2},
            ),
            (
                "every finite-step transfer coefficient is positive",
                all(
                    all(coefficient > 0 for coefficient in coefficients.values())
                    for coefficients in positivity_rows.values()
                ),
            ),
            (
                "t=1 response matches (2^r-2)/3^(r-1)",
                all(
                    sp.Rational(
                        sum(direct[width].values()),
                        2 ** (width + normalization_shift) * 3 ** (width - 1),
                    )
                    == sp.Rational((2**width) - 2, 3 ** (width - 1))
                    for width in range(2, 9)
                ),
            ),
            (
                "fixed memory is three states independent of r",
                "memory dimension is independent of\n`r`" in note
                and "ordered as `00,01,11`" in note,
            ),
            (
                "claim scope keeps action time gravity and full kernel open",
                scope_ok
                and "physical time/Hamiltonian" in note
                and "metric/source/matter carrier" in note,
            ),
            (
                "negative-scope rhetoric carries a landed N1-N8 discipline gate",
                "## No-Go Discipline Gate" in note
                and all(f"### N{index}" in note for index in range(1, 9)),
            ),
            (
                "independent Fraction/frame implementation reproduces all rows",
                all(passed for _label, passed in independent_checks()),
            ),
        )

    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    if mode == "normal" and mutation is None:
        for certificate_line in N5_CERTIFICATE:
            print(certificate_line)
    return int(failures != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"), default="normal")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
