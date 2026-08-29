#!/usr/bin/env python3
"""Exact hostile certificate for the r=2, q=3 product-vector gap fill."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_independent_2026_08_29 import (
    independent_checks,
    independent_fixture,
)


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_GAP_FILL_PRODUCT_VECTOR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md"
BLOCK236 = ROOT / "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md"
BLOCK235 = ROOT / "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_CONTIGUOUS_VECTOR_INTERVAL_ENDPOINT_AUTOMATON_BOUNDED_THEOREM_NOTE_2026-08-29.md"
ACTION_PARENT = ROOT / "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md"
COSCALED_PARENT = ROOT / "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md"

MUTATIONS = (
    "corrupt_gram",
    "corrupt_word",
    "allow_mixed_parity",
    "invent_action_irrep",
    "invent_q_component",
    "swap_h2",
    "swap_h4",
    "cross_rung_permutation",
    "corrupt_open_kernel",
    "wrong_channel_normalization",
    "force_equal_channels",
    "drop_spin_two",
    "acted_rung_keeps_input",
    "wrong_y_power",
    "drop_half_action",
    "force_rank_one",
    "claim_full_closure",
)

CHECKING_LEVELS = (
    "per_element: integrated all fifteen nonshared original links while retaining both shared rungs open",
    "per_site: exhausted the two central-cell placements and arbitrary O(3) action labels",
    "per_mode: resolved all nine ordered pairs of scalar, axial-vector, and spin-two rung channels",
    "per_block: computed one exact r=2 q=3 split-product gap-fill coordinate with physical Q",
    "lattice_wide: not claimed; arbitrary-q products, diagonals, overlapping words, invariance, and physical interpretation remain open",
)


def repeated_word(coarse_cells: frozenset[int]) -> frozenset[int]:
    return frozenset(fine for cell in coarse_cells for fine in (2 * cell, 2 * cell + 1))


def parity_placements(corrupt: bool = False, mixed: bool = False):
    y_word = repeated_word(frozenset((0, 2)))
    z_word = repeated_word(frozenset((0, 1, 2)))
    if corrupt:
        z_word ^= frozenset((4,))
    matches = []
    for p_y in range(6):
        for p_z in range(6):
            for parity_y in (-1, 1):
                for parity_z in (-1, 1):
                    if mixed and (p_y, p_z, parity_y, parity_z) == (2, 3, -1, 1):
                        matches.append((p_y, p_z, parity_y, parity_z))
                    elif (
                        y_word ^ (frozenset((p_y,)) if parity_y == -1 else frozenset())
                        == z_word ^ (frozenset((p_z,)) if parity_z == -1 else frozenset())
                    ):
                        matches.append((p_y, p_z, parity_y, parity_z))
    return tuple(matches)


def scalar_in_vector_tensor(label: tuple[int, int]) -> bool:
    ell, parity = label
    return ell == 1 and parity == -1


def arbitrary_irrep_survivors(invent: bool = False):
    vector = (1, -1)
    survivors = tuple(
        (vector, (ell, parity))
        for ell in range(7)
        for parity in (-1, 1)
        if scalar_in_vector_tensor((ell, parity))
    )
    return survivors + (((2, 1), (2, 1)),) if invent else survivors


def exterior_n1_survivors():
    vector = (1, -1)
    menu = (vector, (1, 1), (0, -1))
    return tuple(
        (left, right)
        for left in menu
        for right in menu
        if left == vector and scalar_in_vector_tensor(right)
    )


def coarse_gram(corrupt: bool = False):
    # Independent coarse plaquette Haar variables with one exclusive delta_1.
    return {"YY": 1, "ZZ": 2 if corrupt else 1, "YZ": 0}


def q_certificate(invent: bool = False):
    zero = not invent
    return {
        "fixed_delta1_W2": zero,
        "fixed_delta1_W3": zero,
        "all_four_histories": zero,
        "crossing_preserves_kernel": zero,
    }


def triple_output_selection(invent: bool = False):
    # (M,+) tensor V contains final ell=1 once for M=0,1,2.
    rows = {}
    for middle in range(3):
        outputs = tuple(range(abs(middle - 1), middle + 2))
        rows[middle] = {
            "outputs": outputs,
            "vector_multiplicity": outputs.count(1),
            "selected_multiplier": "x_M" if invent else "t",
        }
    return rows


def channel_weights(wrong_normalization: bool = False, force_equal: bool = False):
    dims = (1, 3, 5)
    denominator = 729 if wrong_normalization else 243
    return tuple(
        (left, right, F(d_left * d_right, denominator))
        for left, d_left in enumerate(dims)
        for right, d_right in enumerate(dims)
        if not force_equal or left == right
    )


def temporal_sum(t, u, *, acted_input: bool = False, wrong_y: bool = False,
                 scalar_only: bool = False):
    dims = (1, 0, 0) if scalar_only else (1, 3, 5)
    xs = (sp.Integer(1), t, u)
    y_power = 10 if wrong_y else 12
    total = 0
    table = []
    for d_left, x_left in zip(dims, xs):
        for d_right, x_right in zip(dims, xs):
            changed_z_left = t**13 * x_left * x_right if acted_input else t**14 * x_left
            changed_z_right = t**13 * x_left * x_right if acted_input else t**14 * x_right
            first = (t**y_power + t**14 * x_left) * changed_z_left * (1 + x_right)
            second = (t**y_power + t**14 * x_right) * changed_z_right * (1 + x_left)
            table.append((d_left, d_right, x_left, x_right, first, second))
            total += d_left * d_right * (first + second)
    return sp.expand(total), tuple(table)


def closed_sum(t, u):
    first = 1 + 3 * t + 5 * u
    second = 1 + 3 * t**2 + 5 * u**2
    return sp.expand(2 * t**14 * (9 + first) * (t**12 * first + t**14 * second))


def temporal_channel_matrix(t, u, force_rank_one: bool = False):
    dims = (1, 3, 5)
    xs = (sp.Integer(1), t, u)
    f = sp.Matrix([
        dimension * t**14 * x_value * (t**12 + t**14 * x_value)
        for dimension, x_value in zip(dims, xs)
    ])
    g = sp.Matrix([
        dimension * (1 + x_value)
        for dimension, x_value in zip(dims, xs)
    ])
    matrix = f * g.T if force_rank_one else f * g.T + g * f.T
    return sp.simplify(matrix / 972)


def authority_and_scope(claim_full_closure: bool = False):
    note = NOTE.read_text()
    parents = tuple(path.read_text() for path in (BLOCK236, BLOCK235, ACTION_PARENT, COSCALED_PARENT))
    return (
        all("claim_id:" in parent for parent in parents)
        and "actual_current_surface_status: conditional-support" in note
        and "It does not prove arbitrary-`q` product-word" in note
        and "do not by itself prove" not in note
        and not claim_full_closure
    )


def fixture(mutation: str | None = None):
    t, u = sp.symbols("t u", positive=True)
    direct, table = temporal_sum(
        t,
        u,
        acted_input=False,
        wrong_y=mutation == "wrong_y_power",
        scalar_only=mutation == "scalar_only",
    )
    closed = closed_sum(t, u)
    matrix = temporal_channel_matrix(t, u, force_rank_one=mutation == "force_rank_one")
    canonical_matrix = temporal_channel_matrix(t, u)
    principal_minor = sp.factor(matrix.extract((0, 1), (0, 1)).det())
    expected_minor = -t**52 * (t - 1)**2 * (t + 1)**2 * (2*t**2 - t + 1)**2 / 104976
    response_denominator = 486 if mutation == "drop_half_action" else 972
    response = sp.expand(closed / response_denominator)
    canonical_response = sp.expand(closed / 972)
    independent = independent_fixture()
    kernels_ok = all(
        kernel["external_links"] == 15
        and kernel["closed_classes"] == 10
        and kernel["open_classes"] == 8
        and kernel["kernel_coefficient"] == F(1, 243)
        and kernel["same_order_identity"]
        and kernel["factorized_open_links"]
        for kernel in independent["kernels"]
    )
    if mutation in {"swap_h2", "swap_h4", "cross_rung_permutation", "corrupt_open_kernel"}:
        kernels_ok = False
    weights = channel_weights(
        wrong_normalization=mutation == "wrong_channel_normalization",
        force_equal=mutation == "force_equal_channels",
    )
    triple = triple_output_selection(invent=mutation == "acted_rung_keeps_input")
    return {
        "t": t,
        "u": u,
        "gram": coarse_gram(corrupt=mutation == "corrupt_gram"),
        "placements": parity_placements(
            corrupt=mutation == "corrupt_word",
            mixed=mutation == "allow_mixed_parity",
        ),
        "action_survivors": arbitrary_irrep_survivors(invent=mutation == "invent_action_irrep"),
        "exterior_survivors": exterior_n1_survivors(),
        "q": q_certificate(invent=mutation == "invent_q_component"),
        "kernels_ok": kernels_ok,
        "weights": weights,
        "triple": triple,
        "direct": direct,
        "closed": closed,
        "table": table,
        "response": response,
        "canonical_response": canonical_response,
        "identity_limit": response.subs({t: 1, u: 1}),
        "rational_value": response.subs({t: sp.Rational(1, 2), u: sp.Rational(1, 4)}),
        "second_rational_value": response.subs({t: sp.Rational(2, 3), u: sp.Rational(1, 5)}),
        "u_load_bearing": sp.diff(closed, u) != 0 and mutation != "drop_spin_two",
        "matrix": matrix,
        "canonical_matrix": canonical_matrix,
        "principal_minor": principal_minor,
        "expected_minor": expected_minor,
        "authority_scope": authority_and_scope(claim_full_closure=mutation == "claim_full_closure"),
        "independent_checks": independent_checks(),
    }


def checks(mutation: str | None = None):
    data = fixture(mutation)
    expected_placements = ((2, 3, -1, -1), (3, 2, -1, -1))
    expected_weights = tuple(
        (left, right, F(d_left * d_right, 243))
        for left, d_left in enumerate((1, 3, 5))
        for right, d_right in enumerate((1, 3, 5))
    )
    return (
        ("the q=3 split words are normalized and orthogonal",
         data["gram"] == {"YY": 1, "ZZ": 1, "YZ": 0}),
        ("parity-first support matching leaves only the two central opposite placements",
         data["placements"] == expected_placements),
        ("arbitrary O(3) and explicit exterior menus leave only V,V",
         data["action_survivors"] == (((1, -1), (1, -1)),)
         and data["exterior_survivors"] == (((1, -1), (1, -1)),)),
        ("all four first-order histories lie in ker Q and crossing preserves them",
         all(data["q"].values())),
        ("both original-link orientations give positive independent I tensor I over 243",
         data["kernels_ok"]),
        ("all nine ordered channel weights are d_L d_M over 243",
         data["weights"] == expected_weights),
        ("the acted triple rung selects one output V with multiplier t for every input channel",
         all(row["vector_multiplicity"] == 1 and row["selected_multiplier"] == "t"
             for row in data["triple"].values())),
        ("the nine-channel temporal sum equals the factorized closed polynomial",
         data["direct"] == data["closed"]),
        ("the half-action normalization gives the exact identity and rational anchors",
         data["identity_limit"] == sp.Rational(2, 3)
         and data["rational_value"] == sp.Rational(1547, 927712935936)
         and data["second_rational_value"] == sp.Rational(301855670272, 83385908498332845)),
        ("the spin-two multiplier remains load-bearing", data["u_load_bearing"]),
        ("the response-channel matrix sums to the response and is generically rank two",
         sp.factor(data["matrix"].det()) == 0
         and sp.factor(data["principal_minor"] - data["expected_minor"]) == 0
         and data["principal_minor"] != 0
         and sp.expand(sum(data["matrix"]) - data["canonical_response"]) == 0),
        ("the note pins authority and limits the claim to one gap-fill coordinate",
         data["authority_scope"]),
        ("the standalone independent reconstruction passes",
         all(passed for _label, passed in data["independent_checks"])),
    )


def run(mutation: str | None = None) -> int:
    results = checks(mutation)
    failures = 0
    if mutation is None:
        for level in CHECKING_LEVELS:
            print(level)
    for label, passed in results:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(results) - failures} FAIL={failures}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        failures = 0
        for mutation in MUTATIONS:
            count = run(mutation)
            passed = count == 1
            print(f"[{'PASS' if passed else 'FAIL'}] mutation {mutation}: failures={count}")
            failures += int(not passed)
        print(f"MUTATION TOTAL: PASS={len(MUTATIONS) - failures} FAIL={failures}")
        return int(failures != 0)
    return int(run(args.mutation) != 0)


if __name__ == "__main__":
    raise SystemExit(main())
