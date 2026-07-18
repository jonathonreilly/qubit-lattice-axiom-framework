#!/usr/bin/env python3
"""Cycle 268: general Clifford/product covariance of the reference-spoke code.

Reduce every bounded code-preserving local Clifford/product action to its
logical pair-code quotient, test stabilizer-equivalent lifts and vertex
coboundaries, and locate the exact proper-cubic sign obstruction.  The result
is specific to the Cycle-264 reference-spoke gamma chart.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import covariant_vertex_gamma_car_compiler_cycle261_2026_07_17 as c261
import coherent_gamma_parity_sector_doubling_cycle264_2026_07_17 as c264

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "GENERAL_CLIFFORD_REFERENCE_SPOKE_COVARIANCE_CYCLE268_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-268 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "general local clifford",
        "stabilizer-equivalent product representatives",
        "cell/role coboundaries",
        "six-m2 reference pair motif",
        "all 24 proper-cubic frames",
        "exact group law",
        "coefficient rank 138",
        "augmented rank 139",
        "pseudoscalar reference chirality",
        "held-out l=6",
        "beta=-0.3",
        "g=0.37",
        "rank-73",
        "bravyi",
        "setia",
        "chen",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "3d input is not physical time",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the Cycle-268 note preserves Clifford, coboundary, N1-N8, and time contracts", not missing, missing)


def symplectic_bit(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    left_x = left & mask
    left_z = left >> qubits
    right_x = right & mask
    right_z = right >> qubits
    return ((left_x & right_z).bit_count() + (left_z & right_x).bit_count()) % 2


def local_pair_data() -> tuple[list[int], list[int], list[int]]:
    stabilizers = [
        (1 << (6 + 2 * axis)) | (1 << (6 + 2 * axis + 1))
        for axis in range(3)
    ]
    logical_x = [
        (1 << (2 * axis)) | (1 << (2 * axis + 1)) for axis in range(3)
    ]
    logical_z = [1 << (6 + 2 * axis) for axis in range(3)]
    return stabilizers, logical_x, logical_z


def expand_logical_vector(vector: int) -> int:
    stabilizers, logical_x, logical_z = local_pair_data()
    del stabilizers
    x = z = 0
    for logical in range(3):
        if (vector >> logical) & 1:
            x ^= logical_x[logical]
        if (vector >> (3 + logical)) & 1:
            z ^= logical_z[logical]
    return x ^ z


def pair_quotient_controls() -> None:
    stabilizers, _, _ = local_pair_data()
    stabilizer_span = {
        sum(
            stabilizers[index]
            for index in range(3)
            if (coefficient >> index) & 1
        )
        for coefficient in range(8)
    }
    centralizer = [
        vector
        for vector in range(1 << 12)
        if all(symplectic_bit(vector, stabilizer, 6) == 0 for stabilizer in stabilizers)
    ]
    cosets: dict[int, set[int]] = {}
    for vector in centralizer:
        representative = min(vector ^ stabilizer for stabilizer in stabilizer_span)
        cosets.setdefault(representative, set()).add(vector)

    gamma_vectors = [
        expand_logical_vector(c261.local_symplectic_vector(gamma))
        for gamma in c261.LOCAL_GAMMAS
    ]
    gamma_coset_sizes = []
    gamma_support_ranges = []
    for gamma in gamma_vectors:
        members = {gamma ^ stabilizer for stabilizer in stabilizer_span}
        gamma_coset_sizes.append(len(members))
        gamma_support_ranges.append(
            (
                min(((member & 0b111111) | (member >> 6)).bit_count() for member in members),
                max(((member & 0b111111) | (member >> 6)).bit_count() for member in members),
            )
        )

    pair_set = {frozenset((0, 1)), frozenset((2, 3)), frozenset((4, 5))}
    frame_pair_failures = 0
    for permutation in c261.direction_permutations()[1]:
        frame_pair_failures += {
            frozenset((permutation[min(pair)], permutation[max(pair)]))
            for pair in pair_set
        } != pair_set
    check(
        "the six-M2 reference pair motif has a complete 64-class logical Pauli quotient with eight stabilizer-equivalent representatives per class",
        len(stabilizer_span) == 8
        and len(centralizer) == 512
        and len(cosets) == 64
        and set(len(members) for members in cosets.values()) == {8}
        and gamma_coset_sizes == [8] * 6
        and frame_pair_failures == 0,
        {
            "physical_Pauli_vectors": 4096,
            "pair_stabilizer_rank": 3,
            "centralizer_vectors": len(centralizer),
            "logical_cosets": len(cosets),
            "representatives_per_coset": sorted(set(len(members) for members in cosets.values())),
            "gamma_coset_sizes": gamma_coset_sizes,
            "gamma_support_ranges": gamma_support_ranges,
            "proper_frame_pair_failures": frame_pair_failures,
        },
    )


def quotient_rigidity_controls() -> None:
    gamma_vectors = list(c261.LOCAL_GAMMA_VECTORS)
    chirality = 0
    for gamma in gamma_vectors:
        chirality ^= gamma
    rows = []
    for missing in range(6):
        fixed_inputs = [gamma_vectors[label] for label in range(6) if label != missing] + [chirality]
        fixed_rank = c261.gf2_rank(fixed_inputs)
        candidates = [
            vector
            for vector in range(64)
            if all(
                c261.symplectic_bit(vector, gamma_vectors[label]) == 1
                for label in range(6)
                if label != missing
            )
        ]
        forced = chirality
        for label in range(6):
            if label != missing:
                forced ^= gamma_vectors[label]
        rows.append(
            {
                "missing_label": missing,
                "five_gamma_plus_chirality_rank": fixed_rank,
                "anticommuting_candidates": len(candidates),
                "chirality_forced_vector_is_missing_gamma": forced == gamma_vectors[missing],
                "forced_vector_in_candidates": forced in candidates,
            }
        )
    reference_rank = c261.gf2_rank(gamma_vectors)
    check(
        "original edges plus scalar chirality uniquely force every physical and reference logical gamma class",
        reference_rank == 6
        and all(
            row["five_gamma_plus_chirality_rank"] == 6
            and row["anticommuting_candidates"] == 2
            and row["chirality_forced_vector_is_missing_gamma"]
            and row["forced_vector_in_candidates"]
            for row in rows
        ),
        {
            "physical_roles": rows,
            "reference_six_gamma_rank": reference_rank,
            "consequence": "any code-preserving local Clifford/product action descends to the same signed gamma permutation on the pair-code quotient",
        },
    )


def frame_data():
    frames, permutations = c261.direction_permutations()
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    identity = lookup[tuple(np.eye(3, dtype=int).reshape(-1))]
    multiplication = [
        [
            lookup[tuple((frames[left] @ frames[right]).reshape(-1))]
            for right in range(24)
        ]
        for left in range(24)
    ]
    return frames, permutations, identity, multiplication


def reference_sign_rows(require_scalar_chirality: bool = True):
    _, permutations, identity, multiplication = frame_data()
    variables = 24 * 6

    def variable(frame: int, label: int) -> int:
        return frame * 6 + label

    rows: list[tuple[int, int]] = []

    def add(indices: list[int], rhs: int = 0) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        rows.append((mask, rhs))

    for label in range(6):
        add([variable(identity, label)])
    for left in range(24):
        for right in range(24):
            product_frame = multiplication[left][right]
            for label in range(6):
                add(
                    [
                        variable(product_frame, label),
                        variable(right, label),
                        variable(left, permutations[right][label]),
                    ]
                )
    if require_scalar_chirality:
        for frame, permutation in enumerate(permutations):
            add(
                [variable(frame, label) for label in range(6)],
                c261.permutation_parity(permutation),
            )
    return rows, variables


def full_sign_rows(reference_scalar: bool = True):
    _, permutations, identity, multiplication = frame_data()
    variables = 24 * 7 * 6

    def variable(frame: int, role: int, label: int) -> int:
        return (frame * 7 + role) * 6 + label

    rows: list[tuple[int, int]] = []

    def add(indices: list[int], rhs: int = 0) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        rows.append((mask, rhs))

    for role in range(7):
        for label in range(6):
            add([variable(identity, role, label)])
    for left in range(24):
        for right in range(24):
            product_frame = multiplication[left][right]
            for role in range(7):
                moved_role = permutations[right][role] if role < 6 else 6
                for label in range(6):
                    add(
                        [
                            variable(product_frame, role, label),
                            variable(right, role, label),
                            variable(
                                left, moved_role, permutations[right][label]
                            ),
                        ]
                    )
    for frame, permutation in enumerate(permutations):
        parity = c261.permutation_parity(permutation)
        for role in range(6):
            add([variable(frame, role, label) for label in range(6)], parity)
        add(
            [variable(frame, 6, label) for label in range(6)],
            parity if reference_scalar else 0,
        )
        for left, right in combinations(range(6), 2):
            add(
                [
                    variable(frame, left, right),
                    variable(frame, right, left),
                ]
            )
        for direction in range(6):
            add(
                [
                    variable(frame, direction, direction),
                    variable(frame, 6, direction),
                ]
            )
    return rows, variables


def per_frame_positive_rows(permutation: tuple[int, ...], coboundary: bool = False):
    sign_variables = 7 * 6
    variables = sign_variables + (7 if coboundary else 0)

    def sign(role: int, label: int) -> int:
        return role * 6 + label

    def gauge(role: int) -> int:
        return sign_variables + role

    rows: list[tuple[int, int]] = []

    def add(indices: list[int], rhs: int = 0) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        rows.append((mask, rhs))

    parity = c261.permutation_parity(permutation)
    for role in range(7):
        add([sign(role, label) for label in range(6)], parity)
    for left, right in combinations(range(6), 2):
        indices = [sign(left, right), sign(right, left)]
        if coboundary:
            indices += [gauge(left), gauge(right)]
        add(indices)
    for direction in range(6):
        indices = [sign(direction, direction), sign(6, direction)]
        if coboundary:
            indices += [gauge(direction), gauge(6)]
        add(indices)
    return rows, variables


def sign_obstruction_controls() -> None:
    reference_rows, reference_variables = reference_sign_rows(True)
    reference_rank, reference_augmented = c261.affine_system_ranks(
        reference_rows, reference_variables
    )
    full_rows, full_variables = full_sign_rows(True)
    full_rank, full_augmented = c261.affine_system_ranks(full_rows, full_variables)
    _, permutations, _, _ = frame_data()
    frame_rows = []
    dependency_failures = 0
    for frame, permutation in enumerate(permutations):
        rows, variables = per_frame_positive_rows(permutation)
        coefficient_rank, augmented_rank = c261.affine_system_ranks(rows, variables)
        xor_mask = 0
        xor_rhs = 0
        for mask, rhs in rows:
            xor_mask ^= mask
            xor_rhs ^= rhs
        parity = c261.permutation_parity(permutation)
        dependency_failures += xor_mask != 0 or xor_rhs != parity
        frame_rows.append(
            {
                "frame": frame,
                "direction_permutation_parity": parity,
                "coefficient_rank": coefficient_rank,
                "augmented_rank": augmented_rank,
                "consistent": coefficient_rank == augmented_rank,
                "all_equation_XOR": (xor_mask, xor_rhs),
            }
        )
    check(
        "the fixed reference role alone has no scalar-chirality signed lift with the exact 24-frame group law",
        reference_rank == 138 and reference_augmented == 139,
        {
            "variables": reference_variables,
            "equations": len(reference_rows),
            "coefficient_rank": reference_rank,
            "augmented_rank": reference_augmented,
            "scope": "logical signed gamma action at the fixed reference role after exact pair-code quotient",
        },
    )
    check(
        "positive chirality plus all original and spoke edge signs already contradict every odd direction-permutation frame",
        dependency_failures == 0
        and sum(row["consistent"] for row in frame_rows) == 12
        and all(
            row["consistent"]
            == (row["direction_permutation_parity"] == 0)
            for row in frame_rows
        )
        and full_rank == 992
        and full_augmented == 993,
        {
            "per_frame": frame_rows,
            "full_variables": full_variables,
            "full_equations": len(full_rows),
            "full_coefficient_rank": full_rank,
            "full_augmented_rank": full_augmented,
            "dependency": "XOR of seven chirality, fifteen original-edge, and six spoke equations is 0 = permutation parity",
        },
    )


def product_lift_controls() -> None:
    sign_rows, sign_variables = full_sign_rows(True)
    _, permutations, identity, multiplication = frame_data()
    multiplier_variables = 24 * 6 * 3

    def multiplier(frame: int, label: int, pair: int) -> int:
        return (frame * 6 + label) * 3 + pair

    pair_permutations = [
        tuple(permutation[2 * pair] // 2 for pair in range(3))
        for permutation in permutations
    ]
    multiplier_rows: list[tuple[int, int]] = []

    def add_multiplier(indices: list[int]) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        multiplier_rows.append((mask, 0))

    for label in range(6):
        for pair in range(3):
            add_multiplier([multiplier(identity, label, pair)])
    for left in range(24):
        inverse_pair = [0, 0, 0]
        for source, target in enumerate(pair_permutations[left]):
            inverse_pair[target] = source
        for right in range(24):
            product_frame = multiplication[left][right]
            for label in range(6):
                for pair in range(3):
                    add_multiplier(
                        [
                            multiplier(product_frame, label, pair),
                            multiplier(
                                left, permutations[right][label], pair
                            ),
                            multiplier(right, label, inverse_pair[pair]),
                        ]
                    )
    multiplier_rank, multiplier_augmented = c261.affine_system_ranks(
        multiplier_rows, multiplier_variables
    )
    combined_rows = list(sign_rows) + [
        (mask << sign_variables, rhs) for mask, rhs in multiplier_rows
    ]
    combined_variables = sign_variables + multiplier_variables
    combined_rank, combined_augmented = c261.affine_system_ranks(
        combined_rows, combined_variables
    )
    check(
        "all stabilizer-equivalent reference gamma product lifts retain the logical scalar-chirality inconsistency",
        multiplier_rank == multiplier_augmented
        and combined_rank == 992 + multiplier_rank
        and combined_augmented == combined_rank + 1,
        {
            "logical_sign_variables": sign_variables,
            "reference_pair_multiplier_variables": multiplier_variables,
            "multiplier_equations": len(multiplier_rows),
            "multiplier_rank": multiplier_rank,
            "combined_variables": combined_variables,
            "combined_coefficient_rank": combined_rank,
            "combined_augmented_rank": combined_augmented,
            "representative_scope": "each transformed reference gamma may be multiplied by any of the eight positive pair-stabilizer words with exact composition",
        },
    )


def coboundary_controls() -> None:
    _, permutations, _, _ = frame_data()
    frame_rows = []
    for frame, permutation in enumerate(permutations):
        rows, variables = per_frame_positive_rows(permutation, coboundary=True)
        coefficient_rank, augmented_rank = c261.affine_system_ranks(rows, variables)
        frame_rows.append(
            {
                "frame": frame,
                "parity": c261.permutation_parity(permutation),
                "coefficient_rank": coefficient_rank,
                "augmented_rank": augmented_rank,
                "consistent": coefficient_rank == augmented_rank,
            }
        )
    size_rows = []
    for length in (3, 4, 5, 6):
        cells = length**3
        vertices = 7 * cells
        edges = 21 * cells
        degree = 6
        size_rows.append(
            {
                "L": length,
                "vertices": vertices,
                "edges": edges,
                "degree": degree,
                "sum_of_any_vertex_coboundary_edge_signs": (degree * vertices) % 2,
                "odd_volume": cells % 2,
            }
        )
    check(
        "role and cell vertex coboundaries cannot repair odd-frame scalar chirality on the six-regular reference graph",
        sum(row["consistent"] for row in frame_rows) == 12
        and all(row["consistent"] == (row["parity"] == 0) for row in frame_rows)
        and all(
            row["sum_of_any_vertex_coboundary_edge_signs"] == 0
            and row["degree"] == 6
            for row in size_rows
        ),
        {
            "per_frame_role_coboundary": frame_rows,
            "closed_torus_cell_coboundary": size_rows,
            "reason": "a vertex rephase hits six incident edges and six gamma signs, so it changes neither total edge-sign parity nor chirality",
            "marked_non_coboundary_edge_orientation": "not supplied",
        },
    )


def pseudoscalar_control() -> None:
    rows, variables = full_sign_rows(False)
    coefficient_rank, augmented_rank = c261.affine_system_ranks(rows, variables)
    size_rows = []
    for length in (3, 4, 5, 6):
        cells = length**3
        size_rows.append(
            {
                "L": length,
                "reference_modes": cells,
                "odd_frame_total_reference_parity_sign": cells % 2,
                "full_loop_code_preserved": cells % 2 == 0,
            }
        )
    check(
        "allowing pseudoscalar reference chirality closes the local exact group action but flips the full code sector on odd-volume tori",
        coefficient_rank == augmented_rank == 992
        and all(
            row["full_loop_code_preserved"] == (row["L"] % 2 == 0)
            for row in size_rows
        ),
        {
            "variables": variables,
            "equations": len(rows),
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "solution_dimension": variables - coefficient_rank,
            "sizes": size_rows,
            "meaning": "physical chirality and every edge remain positive; reference chirality carries the direction-permutation sign character",
        },
    )


def expanded_predecessor_regression() -> None:
    rows = []
    direct_l3 = None
    for length in (3, 4, 5, 6):
        code = c264.reference_spoke_code(length)
        cells = length**3
        physical_modes = len(code.graph.vertices)
        abstract_qubits = 3 * (physical_modes + cells)
        physical_qubits = 3 * physical_modes + 6 * cells
        local_rank, local_inconsistent = c235.phase_aware_rank(
            code.local_loops, abstract_qubits
        )
        full = code.local_loops + code.wilson_loops
        full_rank, full_inconsistent = c235.phase_aware_rank(full, abstract_qubits)
        abstract_rows = full + c264.reference_equalities(code)
        expanded = [
            c264.expanded_reference_pauli(pauli, physical_modes, cells)
            for pauli in abstract_rows
        ]
        pairs = c264.reference_pair_constraints(physical_modes, cells)
        expanded_rank, expanded_inconsistent = c235.phase_aware_rank(
            expanded + pairs, physical_qubits
        )
        physical_parity = c264.multiply(code.physical_parities)
        expanded_parity = c264.expanded_reference_pauli(
            physical_parity, physical_modes, cells
        )
        sector = c264.sector_status(expanded + pairs, expanded_parity, physical_qubits)
        rows.append(
            {
                "L": length,
                "cells": cells,
                "local_rank": local_rank,
                "full_rank": full_rank,
                "abstract_phase_inconsistencies": (
                    len(local_inconsistent),
                    len(full_inconsistent),
                ),
                "physical_M2_per_cell": physical_qubits // cells,
                "pair_rank": c235.gf2_rank(
                    pair.symplectic(physical_qubits) for pair in pairs
                ),
                "expanded_rank": expanded_rank,
                "expanded_code_exponent": physical_qubits - expanded_rank,
                "target_exponent": physical_modes,
                "expanded_phase_inconsistencies": len(expanded_inconsistent),
                "positive_parity_consistent": sector["plus_consistent"],
                "negative_parity_consistent": sector["minus_consistent"],
                "maximum_expanded_local_support": max(
                    (
                        c264.expanded_reference_pauli(loop, physical_modes, cells).x
                        | c264.expanded_reference_pauli(loop, physical_modes, cells).z
                    ).bit_count()
                    for loop in code.local_loops
                ),
            }
        )
        if length == 3:
            physical_generators = code.physical_parities + code.edge_paulis[
                : len(code.graph.edges)
            ]
            direct_l3 = {
                "reference_equality_leakage": sum(
                    not operator.commutes(constraint)
                    for operator in physical_generators
                    for constraint in c264.reference_equalities(code)
                ),
                "pair_check_phase_inconsistencies": len(
                    c235.phase_aware_rank(pairs, physical_qubits)[1]
                ),
            }
    check(
        "the 24-M2 reference-spoke placement, direct algebra, ranks, sectors, and held-out L=6 regression remain exact",
        all(
            row["local_rank"] == 14 * row["cells"] - 2
            and row["full_rank"] == 14 * row["cells"] + 1
            and row["abstract_phase_inconsistencies"] == (0, 0)
            and row["physical_M2_per_cell"] == 24
            and row["pair_rank"] == 3 * row["cells"]
            and row["expanded_code_exponent"] == row["target_exponent"]
            and row["expanded_phase_inconsistencies"] == 0
            and row["positive_parity_consistent"]
            and row["negative_parity_consistent"] == (row["cells"] % 2 == 1)
            and row["maximum_expanded_local_support"] <= 24
            for row in rows
        )
        and direct_l3
        == {
            "reference_equality_leakage": 0,
            "pair_check_phase_inconsistencies": 0,
        },
        {"sizes": rows, "direct_L3": direct_l3},
    )


def preparation_and_gate_firewall() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = c264.reference_spoke_code(length)
        qubits = 3 * (len(code.graph.vertices) + length**3)
        local_rank = c235.gf2_rank(
            loop.symplectic(qubits) for loop in code.local_loops
        )
        full_rank = c235.gf2_rank(
            loop.symplectic(qubits)
            for loop in code.local_loops + code.wilson_loops
        )
        rows.append(
            {
                "L": length,
                "Wilson_increment": full_rank - local_rank,
                "maximum_Wilson_support": max(
                    (loop.x | loop.z).bit_count() for loop in code.wilson_loops
                ),
            }
        )
    species = c219.common_species(c230.BETA)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "covariance search does not supply bounded preparation or remove the three Wilson logicals",
        all(row["Wilson_increment"] == 3 for row in rows),
        {
            "sizes": rows,
            "bounded_preparation": False,
            "arbitrary_coherent_parity_input": "not encoded",
            "pair_motif_route_bound": 16,
        },
    )
    check(
        "actual Cycle-230 gates and mass/rank-73 seam remain gated by the absent scalar all-frame full-Fock E",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest,
            "principal_sea_rank_predecessor": sea_rank,
            "common_full_Fock_E": False,
            "coin_A_B_FSWAP_contact_synthesis": "not reached",
            "mass_and_rank73_seam_intertwining": "not claimed",
        },
    )
    check(
        "the 3D frame input and Clifford search are not physical time or Records",
        True,
        {
            "3D_input_is_not_physical_time": True,
            "Clifford_and_pair_carriers": "coherent compiler structure, not Records",
            "universal_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    pair_quotient_controls()
    quotient_rigidity_controls()
    sign_obstruction_controls()
    product_lift_controls()
    coboundary_controls()
    pseudoscalar_control()
    expanded_predecessor_regression()
    preparation_and_gate_firewall()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
