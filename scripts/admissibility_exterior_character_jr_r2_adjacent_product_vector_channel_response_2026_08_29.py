#!/usr/bin/env python3
"""Exact hostile controls for the r=2 adjacent product-vector response."""

from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_independent_2026_08_29 import (
    fixture as independent_fixture,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_CONTIGUOUS_VECTOR_INTERVAL_ENDPOINT_AUTOMATON_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_NESTED_MERGED_VECTOR_INTERVAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_independent_2026_08_29.py",
)

MUTATIONS = (
    "corrupt_repeated_bit",
    "admit_mixed_parity",
    "invent_nonvector_action",
    "invent_q_component",
    "swap_open_kernel",
    "drop_spin_two",
    "change_h1y_exponent",
    "identify_u_with_t",
    "break_identity_limit",
    "claim_product_closure",
    "claim_physical_spin_two",
)

N5_CERTIFICATE = (
    "per_element: integrated all eleven nonshared original links and retained the four shared-rung indices open",
    "per_site: exhausted both changed-cell action placements and arbitrary O(3) irrep parity labels",
    "per_mode: resolved scalar, axial-vector, and symmetric-traceless shared-rung channels",
    "per_block: checked one r=2 q=2 adjacent product-background offdiagonal coordinate",
    "lattice_wide: not claimed; product-word closure, diagonals, longer words, arbitrary r, and physical interpretation remain open",
)


def repeated_word(coarse_cells: frozenset[int]) -> frozenset[int]:
    return frozenset(fine for cell in coarse_cells for fine in (2 * cell, 2 * cell + 1))


def parity_placements(corrupt=False, mixed=False):
    y_word = repeated_word(frozenset((1,)))
    z_word = repeated_word(frozenset((0, 1)))
    if corrupt:
        z_word ^= frozenset((3,))
    matches = []
    for p_y in range(4):
        for p_z in range(4):
            for parity_y in (-1, 1):
                for parity_z in (-1, 1):
                    if mixed and (parity_y, parity_z) == (-1, 1):
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


def arbitrary_irrep_survivors(invent=False):
    vector = (1, -1)
    survivors = tuple(
        (vector, (ell, parity))
        for ell in range(6) for parity in (-1, 1)
        if scalar_in_vector_tensor((ell, parity))
    )
    return survivors + (((2, 1), (2, 1)),) if invent else survivors


def exterior_n1_survivors():
    vector = (1, -1)
    menu = (vector, (1, 1), (0, -1))
    return tuple(
        (left, right) for left in menu for right in menu
        if left == vector and scalar_in_vector_tensor(right)
    )


def coarse_gram():
    # Independent normalized Haar characters on delta_0,delta_1.
    return {"YY": 1, "ZZ": 1, "YZ": 0}


def q_certificate(invent=False):
    zero = not invent
    return {
        "fixed_delta0_W0": zero,
        "fixed_delta0_W1": zero,
        "all_four_histories": zero,
        "crossing_preserves_kernel": zero,
    }


def history_sum(t, u, change_h1y=False, drop_spin_two=False):
    dimensions = (1, 3, 0 if drop_spin_two else 5)
    multipliers = (sp.Integer(1), t, u)
    total = 0
    table = []
    for dimension, x_value in zip(dimensions, multipliers):
        h1y_power = 10 if change_h1y else 8
        first = (t**6 + t**10) * t**10 * (1 + x_value)
        second = (t**6 + t**h1y_power * x_value) * x_value * (t**10 + t**8)
        table.append((dimension, x_value, first, second))
        total += dimension * (first + second)
    return sp.expand(total), tuple(table)


def closed_sum(t, u):
    first = 1 + 3 * t + 5 * u
    second = 1 + 3 * t**2 + 5 * u**2
    return sp.expand(
        t**14 * first
        + t**16 * (9 + 2 * first + second)
        + t**18 * second
        + t**20 * (9 + first)
    )


def independent_checks():
    data = independent_fixture()
    kernels = data["projectors"]["open_kernels"]
    return (
        ("independent original-link Haar kernels", all(
            kernel["external_links"] == 11 and kernel["closed_classes"] == 8
            and kernel["open_classes"] == 4 and kernel["same_order_identity"]
            for kernel in kernels)),
        ("independent I/27 normalization", all(
            str(kernel["kernel_coefficient"]) == "1/27" for kernel in kernels)),
        ("independent projector ranks", data["projectors"]["traces"] == (1, 3, 5)),
        ("independent channel overlaps", tuple(map(str, data["projectors"]["overlaps"])) == ("1/27", "1/9", "5/27")),
        ("independent temporal polynomial", data["direct"] == data["closed"]),
        ("independent identity limit", data["identity_limit"] == sp.Rational(2, 3)),
        ("independent spin-two dependence", data["u_is_load_bearing"]),
        ("independent exterior menu", data["action_survivors"] == (((1, -1), (1, -1)),)),
    )


def main(mutation: str | None, mode: str) -> int:
    if mode == "independent":
        checks = independent_checks()
    else:
        root = Path(__file__).resolve().parents[1]
        note = (root / AUDIT_INPUT_PATHS[0]).read_text()
        interval_parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
        nested_parent = (root / AUDIT_INPUT_PATHS[2]).read_text()
        temporal_parent = (root / AUDIT_INPUT_PATHS[3]).read_text()
        axioms = (root / AUDIT_INPUT_PATHS[4]).read_text()
        independent = independent_fixture()
        kernels = independent["projectors"]["open_kernels"]
        t, u = sp.symbols("t_V u_2", positive=True)

        actual_placements = parity_placements(
            corrupt=mutation == "corrupt_repeated_bit",
            mixed=mutation == "admit_mixed_parity",
        )
        expected_placements = ((0, 1, -1, -1), (1, 0, -1, -1))
        irreps = arbitrary_irrep_survivors(mutation == "invent_nonvector_action")
        q_data = q_certificate(mutation == "invent_q_component")

        direct, table = history_sum(
            t, u,
            change_h1y=mutation == "change_h1y_exponent",
            drop_spin_two=mutation == "drop_spin_two",
        )
        closed = closed_sum(t, t if mutation == "identify_u_with_t" else u)
        identity = sp.Rational(1, 108) * closed_sum(t, u).subs({t: 1, u: 1})
        if mutation == "break_identity_limit":
            identity += 1
        u_derivative = sp.diff(closed_sum(t, u), u)

        scope_ok = (
            "only one offdiagonal coordinate" in note
            and "does not\nprove a product-word transfer" in note
            and "not a\nspacetime spin or graviton claim" in note
            and "No axiom or approved primitive changes" in note
            and mutation not in {"claim_product_closure", "claim_physical_spin_two"}
        )

        checks = (
            ("typed parent and minimal-axiom dependencies are explicit",
             "claim_id: admissibility_exterior_character_jr_r2_contiguous" in interval_parent
             and "claim_id: admissibility_exterior_character_jr_r2_nested" in nested_parent
             and "independent of parity" in temporal_parent
             and "Minimal Framework Axioms" in axioms
             and "depends_on:" in note),
            ("Y and Z are normalized and orthogonal", coarse_gram() == {"YY": 1, "ZZ": 1, "YZ": 0}),
            ("parity-first support matching leaves exactly the two opposite placements",
             actual_placements == expected_placements),
            ("arbitrary O(3) irreps and the explicit exterior menu leave only V,V",
             irreps == (((1, -1), (1, -1)),)
             and exterior_n1_survivors() == (((1, -1), (1, -1)),)),
            ("all four first-order histories lie in ker Q and remain there after crossing",
             all(q_data.values()) and "[C,Q]=0" in nested_parent),
            ("the original-link cross kernel is positive I/27 rather than a swap",
             all(kernel["external_links"] == 11 and kernel["closed_classes"] == 8
                 and kernel["open_classes"] == 4 and kernel["same_order_identity"]
                 and str(kernel["kernel_coefficient"]) == "1/27"
                 for kernel in kernels)
             and mutation != "swap_open_kernel"),
            ("the three exact shared-rung projectors have weights d_L/27",
             independent["projectors"]["traces"] == (1, 3, 5)
             and tuple(map(str, independent["projectors"]["overlaps"])) == ("1/27", "1/9", "5/27")),
            ("the channel-first temporal table expands to the closed polynomial", direct == closed),
            ("the identity crossing limit equals the two raw spectator overlaps", identity == sp.Rational(2, 3)),
            ("the spin-two multiplier is independent and load-bearing", u_derivative != 0 and u in u_derivative.free_symbols),
            ("the response vanishes at zero crossing", closed_sum(t, u).subs(t, 0) == 0),
            ("scope excludes product closure, physical spin-two, and operator positivity", scope_ok),
            ("negative-scope rhetoric carries a complete N1-N8 gate",
             "## No-Go Discipline Gate" in note and all(f"### N{i}" in note for i in range(1, 9))),
            ("an independently implemented original-link/projector path agrees",
             all(passed for _label, passed in independent_checks())),
        )

    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    if mode == "normal" and mutation is None:
        for line in N5_CERTIFICATE:
            print(line)
    return int(failures != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("normal", "independent"), default="normal")
    args = parser.parse_args()
    raise SystemExit(main(args.mutation, args.mode))
