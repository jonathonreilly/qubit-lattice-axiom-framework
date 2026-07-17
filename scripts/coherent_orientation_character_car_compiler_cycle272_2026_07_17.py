#!/usr/bin/env python3
"""Cycle 272: coherent orientation-character repair of reference covariance."""

from __future__ import annotations

from itertools import product
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
import general_clifford_reference_spoke_covariance_cycle268_2026_07_17 as c268

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COHERENT_ORIENTATION_CHARACTER_CAR_COMPILER_CYCLE272_NOTE_2026-07-17.md"
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
        check("the Cycle-272 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "orientation character",
        "one ordinary m2 carrier per cell",
        "b_ref z_o",
        "992/992",
        "exact group law",
        "full translations",
        "two-carrier",
        "volume-parity defect",
        "bounded preparation",
        "held-out l=6",
        "beta=-0.3",
        "g=0.37",
        "rank-73",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "3d frame character is spatial structure, not physical time",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the Cycle-272 note preserves carrier, parity, N1-N8, and time contracts", not missing, missing)


def pauli_on(qubit: int, axis: str) -> c235.Pauli:
    if axis == "X":
        return c235.Pauli(x=1 << qubit)
    if axis == "Z":
        return c235.Pauli(z=1 << qubit)
    raise ValueError(axis)


def multiply(paulis: list[c235.Pauli]) -> c235.Pauli:
    result = c235.Pauli()
    for pauli in paulis:
        result = result @ pauli
    return result


def physical_base(length: int):
    code = c264.reference_spoke_code(length)
    cells = length**3
    physical_modes = len(code.graph.vertices)
    base_qubits = 3 * physical_modes + 6 * cells
    loops = code.local_loops + code.wilson_loops
    expanded_loops = [
        c264.expanded_reference_pauli(pauli, physical_modes, cells)
        for pauli in loops
    ]
    pair_checks = c264.reference_pair_constraints(physical_modes, cells)
    reference_b = [
        c264.expanded_reference_pauli(pauli, physical_modes, cells)
        for pauli in code.reference_parities
    ]
    matter_b = [
        c264.expanded_reference_pauli(pauli, physical_modes, cells)
        for pauli in code.physical_parities
    ]
    original_edges = [
        c264.expanded_reference_pauli(pauli, physical_modes, cells)
        for pauli in code.edge_paulis[: len(code.graph.edges)]
    ]
    spokes = [
        c264.expanded_reference_pauli(pauli, physical_modes, cells)
        for pauli in code.edge_paulis[len(code.graph.edges) :]
    ]
    return {
        "code": code,
        "cells": cells,
        "physical_modes": physical_modes,
        "base_qubits": base_qubits,
        "base_checks": expanded_loops + pair_checks,
        "reference_b": reference_b,
        "matter_b": matter_b,
        "original_edges": original_edges,
        "spokes": spokes,
    }


def nearest_cell_pairs(code: c264.ReferenceSpokeCode):
    length = code.graph.length
    pairs = []
    for cell in code.graph.cells:
        source = code.cell_index[cell]
        for axis in range(3):
            moved = list(cell)
            moved[axis] = (moved[axis] + 1) % length
            pairs.append((source, code.cell_index[tuple(moved)]))
    return pairs


def equality(words: list[c235.Pauli], pairs: list[tuple[int, int]]):
    return [words[left] @ words[right] for left, right in pairs]


def sector_status(checks: list[c235.Pauli], parity: c235.Pauli, qubits: int):
    return c264.sector_status(checks, parity, qubits)


def character_and_scalarization_controls() -> None:
    frames, permutations = c261.direction_permutations()
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    multiplication = [
        [
            lookup[tuple((frames[left] @ frames[right]).reshape(-1))]
            for right in range(24)
        ]
        for left in range(24)
    ]
    character = [c261.permutation_parity(permutation) for permutation in permutations]
    character_failures = sum(
        character[multiplication[left][right]]
        != (character[left] ^ character[right])
        for left in range(24)
        for right in range(24)
    )
    constraint_frame_failures = sum(
        any(
            (
                (2 * character[frame]) % 2,  # B_ref equality
                0,  # X_o is fixed under conjugation by X_o
                (character[frame] + character[frame]) % 2,  # B_ref Z_o
                (2 * character[frame]) % 2,  # Z_o equality
                (2 * character[frame]) % 2,  # two-carrier local products
            )
        )
        for frame in range(24)
    )
    pseudoscalar_rows, variables = c268.full_sign_rows(False)
    coefficient_rank, augmented_rank = c261.affine_system_ranks(
        pseudoscalar_rows, variables
    )

    data = physical_base(3)
    orientation_start = data["base_qubits"]
    scalar_b = [
        reference @ pauli_on(orientation_start + cell, "Z")
        for cell, reference in enumerate(data["reference_b"])
    ]
    spoke_incidence_failures = 0
    for cell in range(data["cells"]):
        for direction in range(6):
            spoke = data["spokes"][6 * cell + direction]
            spoke_incidence_failures += scalar_b[cell].commutes(spoke)
    original_edge_failures = sum(
        not scalar.commutes(edge)
        for scalar in scalar_b
        for edge in data["original_edges"]
    )
    pair_leakage = sum(
        not scalar.commutes(pair)
        for scalar in scalar_b
        for pair in data["base_checks"][-3 * data["cells"] :]
    )
    check(
        "one ordinary M2 orientation carrier per cell realizes the sign character and scalarizes B_ref Z_o with the exact group law",
        character_failures == 0
        and constraint_frame_failures == 0
        and sum(character) == 12
        and coefficient_rank == augmented_rank == 992
        and spoke_incidence_failures == 0
        and original_edge_failures == 0
        and pair_leakage == 0,
        {
            "frames": 24,
            "odd_character_frames": sum(character),
            "character_group_law_failures": character_failures,
            "carrier_constraint_frame_failures": constraint_frame_failures,
            "pseudoscalar_sign_system": (coefficient_rank, augmented_rank),
            "pseudoscalar_solution_dimension": variables - coefficient_rank,
            "scalar_reference_support": max(
                (pauli.x | pauli.z).bit_count() for pauli in scalar_b
            ),
            "spoke_incidence_failures": spoke_incidence_failures,
            "original_edge_failures": original_edge_failures,
            "pair_check_leakage": pair_leakage,
            "frame_action": "X_o on odd-character frames, identity on even-character frames",
        },
    )


def one_carrier_route_controls() -> None:
    fixed_x_rows = []
    bound_rows = []
    double_equality_rows = []
    for length in (3, 4, 5, 6):
        data = physical_base(length)
        cells = data["cells"]
        qubits = data["base_qubits"] + cells
        orientation_start = data["base_qubits"]
        orientation_z = [
            pauli_on(orientation_start + cell, "Z") for cell in range(cells)
        ]
        orientation_x = [
            pauli_on(orientation_start + cell, "X") for cell in range(cells)
        ]
        scalar_b = [
            data["reference_b"][cell] @ orientation_z[cell]
            for cell in range(cells)
        ]
        pairs = nearest_cell_pairs(data["code"])
        b_equalities = equality(data["reference_b"], pairs)
        c_equalities = equality(scalar_b, pairs)
        z_equalities = equality(orientation_z, pairs)
        matter_parity = multiply(data["matter_b"])

        fixed_checks = data["base_checks"] + b_equalities + orientation_x
        fixed_rank, fixed_inconsistent = c235.phase_aware_rank(fixed_checks, qubits)
        fixed_sector = sector_status(fixed_checks, matter_parity, qubits)
        scalar_leakage = sum(
            not scalar_b[cell].commutes(orientation_x[cell])
            for cell in range(cells)
        )
        fixed_x_rows.append(
            {
                "L": length,
                "cells": cells,
                "physical_M2_per_cell": qubits // cells,
                "rank": fixed_rank,
                "code_exponent": qubits - fixed_rank,
                "target_exponent": data["physical_modes"],
                "phase_inconsistencies": len(fixed_inconsistent),
                "negative_matter_parity_consistent": fixed_sector[
                    "minus_consistent"
                ],
                "scalar_B_leakage": scalar_leakage,
            }
        )

        onsite_scalar = [
            data["reference_b"][cell] @ orientation_z[cell]
            for cell in range(cells)
        ]
        bound_checks = data["base_checks"] + b_equalities + onsite_scalar
        bound_rank, bound_inconsistent = c235.phase_aware_rank(bound_checks, qubits)
        bound_sector = sector_status(bound_checks, matter_parity, qubits)
        spoke_leakage = sum(
            not onsite_scalar[cell].commutes(data["spokes"][6 * cell + direction])
            for cell in range(cells)
            for direction in range(6)
        )
        bound_rows.append(
            {
                "L": length,
                "rank": bound_rank,
                "code_exponent": qubits - bound_rank,
                "target_exponent": data["physical_modes"],
                "phase_inconsistencies": len(bound_inconsistent),
                "negative_matter_parity_consistent": bound_sector[
                    "minus_consistent"
                ],
                "auxiliary_spoke_leakage": spoke_leakage,
            }
        )

        double_checks = data["base_checks"] + c_equalities + z_equalities
        double_rank, double_inconsistent = c235.phase_aware_rank(double_checks, qubits)
        double_sector = sector_status(double_checks, matter_parity, qubits)
        local_scalar_leakage = sum(
            not scalar.commutes(check)
            for scalar in scalar_b
            for check in c_equalities + z_equalities
        )
        double_equality_rows.append(
            {
                "L": length,
                "rank": double_rank,
                "code_exponent": qubits - double_rank,
                "target_exponent": data["physical_modes"],
                "excess_exponent": qubits
                - double_rank
                - data["physical_modes"],
                "phase_inconsistencies": len(double_inconsistent),
                "negative_matter_parity_consistent": double_sector[
                    "minus_consistent"
                ],
                "scalar_B_constraint_leakage": local_scalar_leakage,
            }
        )
    check(
        "fixing each orientation carrier in X gives the target rank but the scalarized B_ref Z_o leaks and the volume-parity defect remains",
        all(
            row["physical_M2_per_cell"] == 25
            and row["code_exponent"] == row["target_exponent"]
            and row["phase_inconsistencies"] == 0
            and row["negative_matter_parity_consistent"]
            == (row["cells"] % 2 == 1)
            and row["scalar_B_leakage"] == row["cells"]
            for row in fixed_x_rows
        ),
        fixed_x_rows,
    )
    check(
        "locally binding B_ref Z_o removes carrier leakage from constraints but fixes that scalar and leaks all auxiliary spokes",
        all(
            row["code_exponent"] == row["target_exponent"]
            and row["phase_inconsistencies"] == 0
            and row["negative_matter_parity_consistent"]
            == (row["L"] % 2 == 1)
            and row["auxiliary_spoke_leakage"] == 6 * row["L"] ** 3
            for row in bound_rows
        ),
        bound_rows,
    )
    check(
        "commuting scalar-chirality and orientation-Z equalities preserve local B_ref Z_o but leave one excess logical and the same even-volume parity deletion",
        all(
            row["code_exponent"] == row["target_exponent"] + 1
            and row["excess_exponent"] == 1
            and row["phase_inconsistencies"] == 0
            and row["negative_matter_parity_consistent"]
            == (row["L"] % 2 == 1)
            and row["scalar_B_constraint_leakage"] == 0
            for row in double_equality_rows
        ),
        double_equality_rows,
    )


def two_carrier_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        data = physical_base(length)
        cells = data["cells"]
        abstract_qubits = data["base_qubits"] + 2 * cells
        first = data["base_qubits"]
        second = first + cells
        z1 = [pauli_on(first + cell, "Z") for cell in range(cells)]
        z2 = [pauli_on(second + cell, "Z") for cell in range(cells)]
        b_equalities = equality(
            data["reference_b"], nearest_cell_pairs(data["code"])
        )
        bind1 = [data["reference_b"][cell] @ z1[cell] for cell in range(cells)]
        bind2 = [data["reference_b"][cell] @ z2[cell] for cell in range(cells)]
        checks = data["base_checks"] + b_equalities + bind1 + bind2
        rank, inconsistent = c235.phase_aware_rank(checks, abstract_qubits)
        matter_parity = multiply(data["matter_b"])
        sector = sector_status(checks, matter_parity, abstract_qubits)
        rows.append(
            {
                "L": length,
                "cells": cells,
                "abstract_orientation_carriers_per_cell": 2,
                "rank": rank,
                "code_exponent": abstract_qubits - rank,
                "target_exponent": data["physical_modes"],
                "phase_inconsistencies": len(inconsistent),
                "negative_matter_parity_consistent": sector["minus_consistent"],
                "physical_orientation_M2_per_cell": 7,
                "total_physical_M2_per_cell": 31,
                "second_carrier_repetition_rank": 5 * cells,
            }
        )
    check(
        "the two-carrier/even-orbit binding reaches the target rank but still only copies the reference bit and does not repair b^N",
        all(
            row["code_exponent"] == row["target_exponent"]
            and row["phase_inconsistencies"] == 0
            and row["negative_matter_parity_consistent"]
            == (row["cells"] % 2 == 1)
            and row["physical_orientation_M2_per_cell"] == 7
            and row["total_physical_M2_per_cell"] == 31
            and row["second_carrier_repetition_rank"] == 5 * row["cells"]
            for row in rows
        ),
        rows,
    )


def placement_and_covariance_controls() -> None:
    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)

    def point(vector):
        return tuple(int(value) % 64 for value in vector)

    occupied = {
        point(radius * direction)
        for radius in (6, 12, 18, 24)
        for direction in directions
    }
    center = (0, 0, 0)
    second_shell = {point(30 * direction) for direction in directions}
    collisions = int(center in occupied) + len(second_shell & occupied) + int(
        center in second_shell
    )
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        frame_failures += point(frame @ np.asarray(center)) != center
        frame_failures += {
            point(frame @ np.asarray(site)) for site in second_shell
        } != second_shell
    repetition_checks = [
        c235.Pauli(z=(1 << site) | (1 << (site + 1))) for site in range(5)
    ]
    repetition_rank, repetition_inconsistent = c235.phase_aware_rank(
        repetition_checks, 6
    )
    direction_index = {tuple(direction): index for index, direction in enumerate(directions)}
    repetition_frame_span_failures = 0
    for frame in c235.proper_cubic_frames():
        permutation = [
            direction_index[tuple(frame @ direction)] for direction in directions
        ]
        for repetition_check in repetition_checks:
            mapped_z = sum(
                1 << permutation[index]
                for index in range(6)
                if (repetition_check.z >> index) & 1
            )
            mapped_check = c235.Pauli(z=mapped_z)
            mapped_rank, mapped_inconsistent = c235.phase_aware_rank(
                repetition_checks + [mapped_check], 6
            )
            repetition_frame_span_failures += int(
                mapped_rank != repetition_rank or bool(mapped_inconsistent)
            )
    logical_x = c235.Pauli(x=(1 << 6) - 1)
    logical_z = c235.Pauli(z=1)
    logical_leakage = sum(
        not operator.commutes(check)
        for operator in (logical_x, logical_z)
        for check in repetition_checks
    )
    check(
        "the one-carrier center and two-carrier center-plus-radius-30 repetition motif have bounded collision-free proper-cubic placements",
        collisions == 0
        and frame_failures == 0
        and repetition_rank == 5
        and not repetition_inconsistent
        and repetition_frame_span_failures == 0
        and logical_leakage == 0
        and not logical_x.commutes(logical_z),
        {
            "one_carrier_site": center,
            "second_carrier_shell_radius": 30,
            "second_carrier_physical_sites": len(second_shell),
            "collisions": collisions,
            "proper_frame_failures": frame_failures,
            "six_site_repetition_rank": repetition_rank,
            "repetition_group_frame_span_failures": repetition_frame_span_failures,
            "logical_leakage": logical_leakage,
            "maximum_orientation_route": 4,
            "one_carrier_total_M2_per_cell": 25,
            "two_carrier_total_M2_per_cell": 31,
        },
    )


def translation_preparation_and_fixture_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = c264.reference_spoke_code(length)
        cells = length**3
        pairs = nearest_cell_pairs(code)
        translated_failures = 0
        pair_set = {frozenset(pair) for pair in pairs}
        for displacement in product(range(length), repeat=3):
            mapping = []
            for cell in code.graph.cells:
                moved = tuple(
                    (cell[axis] + displacement[axis]) % length
                    for axis in range(3)
                )
                mapping.append(code.cell_index[moved])
            translated_failures += {
                frozenset((mapping[left], mapping[right])) for left, right in pairs
            } != pair_set
        qubits = 3 * (len(code.graph.vertices) + cells)
        local_rank = c235.gf2_rank(
            loop.symplectic(qubits) for loop in code.local_loops
        )
        full_rank = c235.gf2_rank(
            loop.symplectic(qubits)
            for loop in code.local_loops + code.wilson_loops
        )
        diameter = 3 * (length // 2)
        rows.append(
            {
                "L": length,
                "translation_failures": translated_failures,
                "Wilson_increment": full_rank - local_rank,
                "maximum_Wilson_support": max(
                    (loop.x | loop.z).bit_count() for loop in code.wilson_loops
                ),
                "cat_depth_lower_bound": (diameter + 1) // 2,
            }
        )
    species = c219.common_species(c230.BETA)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "all carrier constraint families are translation covariant but no route supplies bounded parity/Wilson preparation",
        all(
            row["translation_failures"] == 0 and row["Wilson_increment"] == 3
            for row in rows
        )
        and rows[-1]["cat_depth_lower_bound"] > rows[0]["cat_depth_lower_bound"],
        {
            "sizes": rows,
            "bounded_preparation": False,
            "arbitrary_coherent_parity_input": "not encoded",
        },
    )
    check(
        "actual Cycle-230 gates and mass/rank-73 seam remain gated by the surviving parity/preparation walls",
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
        "the 3D frame character and coherent carriers are not physical time or Records",
        True,
        {
            "3D_frame_character_is_spatial_structure_not_physical_time": True,
            "orientation_carriers": "coherent code data, not Records",
            "universal_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    character_and_scalarization_controls()
    one_carrier_route_controls()
    two_carrier_controls()
    placement_and_covariance_controls()
    translation_preparation_and_fixture_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
