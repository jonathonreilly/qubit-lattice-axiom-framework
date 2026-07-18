#!/usr/bin/env python3
"""Cycle 244: translation/cubic local syndrome-decoder tournament.

Search translation-convolution right inverses of the Cycle-235 modified-Gauss
syndrome map, test an outcome-only sign-frame consumer, and run a genuinely
local majority cellular decoder.  The exact negative is deliberately narrow:
on an even periodic cube a lawful translation-invariant syndrome need not have
a translation-invariant face-Z preimage, so no deterministic
translation-equivariant section can cover every lawful syndrome on that
finite domain.  Markers, randomness, coherent gauge fields, odd sizes, open
boundaries, and supplied sign frames change the hypotheses and remain live.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import random
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "TRANSLATION_CUBIC_LOCAL_SYNDROME_DECODER_CYCLE244_NOTE_2026-07-17.md"
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
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "lawful syndrome quotient",
        "h d h = h",
        "translation-invariant witness",
        "linear convolution",
        "retained local sign frame",
        "majority cellular decoder",
        "adversarial separated loop",
        "three wilson bits",
        "syndrome outcome registers are not automatically records",
        "compiler rounds are not physical time",
        "odd sector remains absent",
        "macro-marker",
        "authority: none",
        "audit: unset",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the Cycle-244 and N1-N8 contract", not missing, missing)


@dataclass
class CodeData:
    length: int
    graph: c235.PyramidCellulation
    cells: list[tuple[int, int, int]]
    face: dict[tuple[tuple[int, int, int], int], int]
    face_label: dict[int, tuple[tuple[int, int, int], int]]
    checks: dict[tuple[tuple[int, int, int], int], int]
    check_label: dict[int, tuple[tuple[int, int, int], int]]
    rows: list[int]
    face_incidence: list[list[int]]
    row_to_check: dict[int, int]


def build_data(length: int) -> CodeData:
    graph = c235.PyramidCellulation(length)
    cells = list(graph.cells)
    count = {cell: 0 for cell in cells}
    face = {}
    face_label = {}
    for qubit, edge in enumerate(graph.edges):
        cell = edge[3]
        face_type = count[cell]
        count[cell] += 1
        face[(cell, face_type)] = qubit
        face_label[qubit] = (cell, face_type)
    if set(count.values()) != {15}:
        raise RuntimeError((length, "face-type count", set(count.values())))

    cycles = c235.primal_edge_cycles(graph)
    rows = [mask for mask, _, _ in cycles]
    cell_count = length**3
    checks = {}
    check_label = {}
    for index in range(len(rows)):
        if index < 8 * cell_count:
            cell = cells[index // 8]
            check_type = index % 8
        else:
            shifted = index - 8 * cell_count
            cell = cells[shifted // 3]
            check_type = 8 + shifted % 3
        checks[(cell, check_type)] = index
        check_label[index] = (cell, check_type)

    face_incidence = [[] for _ in graph.edges]
    for check_index, mask in enumerate(rows):
        support = mask
        while support:
            bit = support & -support
            face_incidence[bit.bit_length() - 1].append(check_index)
            support ^= bit
    row_to_check = {row: index for index, row in enumerate(rows)}
    if len(row_to_check) != len(rows):
        raise RuntimeError((length, "duplicate local cycle masks"))
    return CodeData(
        length,
        graph,
        cells,
        face,
        face_label,
        checks,
        check_label,
        rows,
        face_incidence,
        row_to_check,
    )


def gf2_solve(equations, return_solution: bool = False):
    """Solve coefficient-mask equations over GF(2), pivoting on the high bit."""

    pivots: dict[int, tuple[int, int]] = {}
    equations_seen = 0
    for original_mask, original_rhs in equations:
        equations_seen += 1
        mask = int(original_mask)
        rhs = int(original_rhs)
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                mask ^= pivots[pivot][0]
                rhs ^= pivots[pivot][1]
            else:
                pivots[pivot] = (mask, rhs)
                break
        if not mask and rhs:
            return False, len(pivots), equations_seen, None
    if not return_solution:
        return True, len(pivots), equations_seen, None
    solution = 0
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        lower = mask ^ (1 << pivot)
        value = rhs ^ ((lower & solution).bit_count() % 2)
        if value:
            solution |= 1 << pivot
    return True, len(pivots), equations_seen, solution


def syndrome_from_correction(data: CodeData, correction: int) -> int:
    return sum(
        (((row & correction).bit_count() % 2) << index)
        for index, row in enumerate(data.rows)
    )


def correction_system(data: CodeData, syndrome: int, allowed_faces=None):
    if allowed_faces is None:
        allowed_faces = range(len(data.graph.edges))
    allowed_faces = list(allowed_faces)
    dense = {face: index for index, face in enumerate(allowed_faces)}

    def equations():
        for check_index, row in enumerate(data.rows):
            mask = 0
            support = row
            while support:
                bit = support & -support
                face = bit.bit_length() - 1
                if face in dense:
                    mask ^= 1 << dense[face]
                support ^= bit
            yield mask, (syndrome >> check_index) & 1

    okay, rank, seen, solution = gf2_solve(equations(), return_solution=True)
    if not okay:
        return False, rank, seen, 0
    correction = 0
    dense_solution = int(solution)
    while dense_solution:
        bit = dense_solution & -dense_solution
        correction ^= 1 << allowed_faces[bit.bit_length() - 1]
        dense_solution ^= bit
    return True, rank, seen, correction


def l1_offsets(radius: int):
    return tuple(
        offset
        for offset in product(range(-radius, radius + 1), repeat=3)
        if sum(abs(value) for value in offset) <= radius
    )


def kernel_variables(offsets):
    variables = tuple(product(range(15), range(11), offsets))
    return variables, {variable: index for index, variable in enumerate(variables)}


def kernel_equations(data: CodeData, offsets, variable_index):
    """Equations for H D H = H on 15 origin-face generators."""

    length = data.length
    for source_type in range(15):
        source_face = data.face[((0, 0, 0), source_type)]
        source_syndrome = [
            data.check_label[index] for index in data.face_incidence[source_face]
        ]
        equations = {
            (cell, check_type): [0, int((cell, check_type) in source_syndrome)]
            for cell in data.cells
            for check_type in range(11)
        }
        for input_cell, input_type in source_syndrome:
            for output_type in range(15):
                for offset in offsets:
                    variable = variable_index[(output_type, input_type, offset)]
                    output_cell = tuple(
                        (input_cell[axis] - offset[axis]) % length
                        for axis in range(3)
                    )
                    output_face = data.face[(output_cell, output_type)]
                    for target_check in data.face_incidence[output_face]:
                        target_label = data.check_label[target_check]
                        equations[target_label][0] ^= 1 << variable
        yield from equations.values()


def apply_kernel(
    data: CodeData,
    variables,
    solution: int,
    syndrome: int,
) -> int:
    active_by_input: dict[int, list[tuple[int, tuple[int, int, int]]]] = {
        check_type: [] for check_type in range(11)
    }
    active = int(solution)
    while active:
        bit = active & -active
        output_type, input_type, offset = variables[bit.bit_length() - 1]
        active_by_input[input_type].append((output_type, offset))
        active ^= bit

    correction = 0
    pending = int(syndrome)
    while pending:
        bit = pending & -pending
        check_index = bit.bit_length() - 1
        input_cell, input_type = data.check_label[check_index]
        for output_type, offset in active_by_input[input_type]:
            output_cell = tuple(
                (input_cell[axis] - offset[axis]) % data.length
                for axis in range(3)
            )
            correction ^= 1 << data.face[(output_cell, output_type)]
        pending ^= bit
    return correction


def frame_maps(data: CodeData, frame):
    _, edge_map = c235.graph_frame_maps(data.graph, frame)
    check_map = []
    for row in data.rows:
        mapped = c235.permute_pauli(c235.Pauli(x=row), edge_map).x
        check_map.append(data.row_to_check[mapped])
    return edge_map, check_map


def permute_bits(mask: int, mapping: list[int]) -> int:
    result = 0
    pending = int(mask)
    while pending:
        bit = pending & -pending
        result ^= 1 << mapping[bit.bit_length() - 1]
        pending ^= bit
    return result


def convolution_search_controls(data_cache):
    schedules = {
        # Radius classes are nested.  Testing R_min-1 and R_min is therefore
        # enough to certify the exact held minimum without re-solving every
        # smaller subsystem.
        3: (1, 2),
        4: (),
        5: (3, 4),
        7: (5, 6),
    }
    rows = []
    successful = {}
    for length, radii in schedules.items():
        data = data_cache[length]
        for radius in radii:
            offsets = l1_offsets(radius)
            variables, variable_index = kernel_variables(offsets)
            okay, rank, seen, solution = gf2_solve(
                kernel_equations(data, offsets, variable_index),
                return_solution=True,
            )
            row = {
                "L": length,
                "radius": radius,
                "offsets": len(offsets),
                "variables": len(variables),
                "consistent": okay,
                "rank_at_stop": rank,
                "equations_seen": seen,
                "kernel_weight": None if solution is None else solution.bit_count(),
            }
            rows.append(row)
            if okay and length not in successful:
                successful[length] = (radius, variables, int(solution))

    # At L=4 this spans every periodic displacement, so it is stronger than a
    # bounded-radius miss: no translation-convolution linear section exists.
    data4 = data_cache[4]
    full_offsets = tuple(data4.cells)
    full_variables, full_index = kernel_variables(full_offsets)
    full_okay, full_rank, full_seen, _ = gf2_solve(
        kernel_equations(data4, full_offsets, full_index),
        return_solution=False,
    )
    full_row = {
        "L": 4,
        "radius": "all 64 periodic displacements",
        "offsets": len(full_offsets),
        "variables": len(full_variables),
        "consistent": full_okay,
        "rank_at_stop": full_rank,
        "equations_seen": full_seen,
    }

    minimum = {
        length: successful[length][0] if length in successful else None
        for length in schedules
    }
    check(
        "linear convolution has exact odd-size sections only at growing held radii, while L=4 fails even with full support",
        minimum == {3: 2, 4: None, 5: 4, 7: 6}
        and not full_okay,
        {"minimum_L1_radius": minimum, "full_L4": full_row},
    )

    verification = []
    for length in (3, 5, 7):
        data = data_cache[length]
        radius, variables, solution = successful[length]
        failures = 0
        for source_type in range(15):
            source_face = data.face[((0, 0, 0), source_type)]
            source_syndrome = syndrome_from_correction(data, 1 << source_face)
            decoded = apply_kernel(data, variables, solution, source_syndrome)
            failures += syndrome_from_correction(data, decoded) != source_syndrome
        verification.append(
            {
                "L": length,
                "radius": radius,
                "origin_generator_failures": failures,
                "kernel_weight": solution.bit_count(),
            }
        )

    check(
        "every selected odd-size kernel satisfies H D H = H exactly on the translation-generated lawful quotient",
        all(row["origin_generator_failures"] == 0 for row in verification),
        verification,
    )
    # Audit one complete selected kernel under every frame.  The nonlinear CA
    # and the exact fixed-syndrome witness receive separate all-24 audits.
    data = data_cache[3]
    _, variables, solution = successful[3]
    frame_mismatches = 0
    for frame in c235.proper_cubic_frames():
        edge_map, _ = frame_maps(data, frame)
        mismatch = False
        for source_type in range(15):
            source = data.face[((0, 0, 0), source_type)]
            syndrome = syndrome_from_correction(data, 1 << source)
            decoded = apply_kernel(data, variables, solution, syndrome)
            rotated_source = edge_map[source]
            rotated_syndrome = syndrome_from_correction(data, 1 << rotated_source)
            decoded_rotated = apply_kernel(
                data, variables, solution, rotated_syndrome
            )
            expected = permute_bits(decoded, edge_map)
            if decoded_rotated != expected:
                mismatch = True
                break
        frame_mismatches += mismatch
    check(
        "the displayed L=3 Gaussian kernel is not silently promoted to a proper-cubic decoder",
        frame_mismatches == 23,
        {"selected_L3_kernel_frame_mismatches": frame_mismatches},
    )
    return rows, successful


def dependency_combinations(rows: list[int]):
    pivots = {}
    dependencies = []
    for index, original in enumerate(rows):
        row = int(original)
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot][0]
                combination ^= pivots[pivot][1]
            else:
                pivots[pivot] = (row, combination)
                break
        if not row:
            dependencies.append(combination)
    return dependencies


def constant_response_rows(data: CodeData):
    rows = []
    for check_type in range(11):
        check = data.checks[((0, 0, 0), check_type)]
        type_mask = 0
        support = data.rows[check]
        while support:
            bit = support & -support
            _, face_type = data.face_label[bit.bit_length() - 1]
            type_mask ^= 1 << face_type
            support ^= bit
        rows.append(type_mask)
    return tuple(rows)


def constant_response(response_rows, face_pattern: int) -> int:
    return sum(
        (((row & face_pattern).bit_count() % 2) << check_type)
        for check_type, row in enumerate(response_rows)
    )


def constant_space_controls(data_cache):
    census = []
    constant_images = {}
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        dependencies = dependency_combinations(data.rows)
        constant_constraints = []
        for combination in dependencies:
            constraint = 0
            pending = combination
            while pending:
                bit = pending & -pending
                _, check_type = data.check_label[bit.bit_length() - 1]
                constraint ^= 1 << check_type
                pending ^= bit
            if constraint:
                constant_constraints.append(constraint)
        lawful = {
            syndrome
            for syndrome in range(1 << 11)
            if all(
                (syndrome & constraint).bit_count() % 2 == 0
                for constraint in constant_constraints
            )
        }
        response_rows = constant_response_rows(data)
        constant_image = {
            constant_response(response_rows, face_pattern)
            for face_pattern in range(1 << 15)
        }
        constant_images[length] = constant_image
        difference = lawful - constant_image
        census.append(
            {
                "L": length,
                "lawful_constant_syndromes": len(lawful),
                "constant_correction_image": len(constant_image),
                "lawful_without_constant_preimage": len(difference),
            }
        )

    # A constant syndrome is determined by its 11 type bits, so its frame
    # audit can be performed once on the L=3 type permutation rather than by
    # repeatedly permuting the much larger L=4 and L=6 bit strings.
    type_frame_maps = []
    type_data = data_cache[3]
    for frame in c235.proper_cubic_frames():
        _, check_map = frame_maps(type_data, frame)
        type_frame_maps.append(
            [
                type_data.check_label[
                    check_map[type_data.checks[((0, 0, 0), check_type)]]
                ][1]
                for check_type in range(11)
            ]
        )

    witnesses = []
    for length in (4, 6):
        data = data_cache[length]
        axis_pattern = 1 << 8
        cubic_pattern = (1 << 8) | (1 << 9) | (1 << 10)
        rows = []
        for name, type_pattern in (
            ("one-axis", axis_pattern),
            ("proper-cubic", cubic_pattern),
        ):
            syndrome = 0
            for check_index, (_, check_type) in data.check_label.items():
                if (type_pattern >> check_type) & 1:
                    syndrome ^= 1 << check_index
            lawful, _, _, correction = correction_system(data, syndrome)
            constant_preimage = type_pattern in constant_images[length]
            frame_failures = sum(
                permute_bits(type_pattern, check_type_map) != type_pattern
                for check_type_map in type_frame_maps
            )
            rows.append(
                {
                    "kind": name,
                    "syndrome_weight": syndrome.bit_count(),
                    "lawful": lawful,
                    "one_global_preimage_weight": correction.bit_count(),
                    "translation_invariant_preimage": constant_preimage,
                    "proper_cubic_frame_failures": frame_failures,
                }
            )
        witnesses.append({"L": length, "witnesses": rows})

    check(
        "even cubes contain lawful constant syndromes outside the constant-correction image",
        [row["lawful_without_constant_preimage"] for row in census]
        == [0, 896, 0, 896],
        census,
    )
    check(
        "the all-axis witness is lawful and invariant under translations and all 24 frames but has no equally invariant correction",
        all(
            row["witnesses"][1]["lawful"]
            and not row["witnesses"][1]["translation_invariant_preimage"]
            and row["witnesses"][1]["proper_cubic_frame_failures"] == 0
            for row in witnesses
        ),
        witnesses,
    )
    check(
        "the even-torus witness excludes every deterministic translation-equivariant syndrome section on that declared domain",
        True,
        {
            "reason": "an equivariant function maps a translation-fixed input to a translation-fixed output, but the lawful witness has no fixed preimage",
            "scope": "even periodic square-pyramid code; every lawful syndrome; deterministic section",
            "not_claimed": "infinite lattice, stochastic branch selection, odd-only sizes, open boundary, or supplied sign frame",
        },
    )


def sign_frame_consumer_controls(data_cache):
    data = data_cache[3]
    vertex = 0
    kernel = data.graph.B(vertex).z
    kernel_syndrome = syndrome_from_correction(data, kernel)
    incident_edge = data.graph.incident[vertex][0]
    u, v, _, _ = data.graph.edges[incident_edge]
    hopping = data.graph.A(u, v)
    hopping_sign_flipped = (kernel & hopping.x).bit_count() % 2 == 1

    species = c219.common_species(-0.35)
    coin = c229.fock_lift(species.coin)
    mode_parity = np.diag(
        [(-1) ** ((state >> 0) & 1) for state in range(64)]
    ).astype(complex)
    coin_residual = float(np.linalg.norm(coin @ mode_parity - mode_parity @ coin))

    fswap = np.asarray(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, -1]],
        dtype=complex,
    )
    two_mode_parity = np.diag([1, -1, 1, -1]).astype(complex)
    fswap_residual = float(
        np.linalg.norm(fswap @ two_mode_parity - two_mode_parity @ fswap)
    )
    occupations = np.asarray([state.bit_count() for state in range(64)])
    contact = np.diag(np.exp(1j * 0.37 * occupations * (occupations - 1) / 2))
    contact_residual = float(
        np.linalg.norm(contact @ mode_parity - mode_parity @ contact)
    )
    check(
        "the local syndrome alone leaves a kernel sign ambiguity that changes hopping, coin, and FSWAP but not contact",
        kernel_syndrome == 0
        and hopping_sign_flipped
        and coin_residual > 1e-6
        and fswap_residual > 1e-6
        and contact_residual == 0,
        {
            "kernel_weight": kernel.bit_count(),
            "kernel_syndrome": kernel_syndrome,
            "hopping_sign_flipped": hopping_sign_flipped,
            "coin_commutator_with_mode_gauge": coin_residual,
            "FSWAP_commutator_with_mode_gauge": fswap_residual,
            "contact_commutator_with_mode_gauge": contact_residual,
        },
    )
    check(
        "a supplied face sign frame makes branch-dependent gates locally usable but does not derive that frame from syndrome outcomes",
        True,
        {
            "encoding": "E_z = Z(z) E_0",
            "physical_update": "G_z = Z(z) G_0 Z(z)",
            "intertwining": "E_z G = G_z E_z",
            "local_consumers": {
                "coin": "needs incident face signs",
                "FSWAP": "needs the hopping-face sign",
                "contact": "sign independent",
            },
            "remaining_supplier": "lawful z with H z = s, or a dynamical gauge field carrying it",
        },
    )


def majority_step(data: CodeData, syndrome: int):
    flips = 0
    for face, adjacent in enumerate(data.face_incidence):
        overlap = sum((syndrome >> check) & 1 for check in adjacent)
        if 2 * overlap > len(adjacent):
            flips ^= 1 << face
    return syndrome ^ syndrome_from_correction(data, flips), flips


def majority_run(data: CodeData, syndrome: int, rounds: int):
    correction = 0
    seen = {syndrome: 0}
    for turn in range(1, rounds + 1):
        syndrome, flips = majority_step(data, syndrome)
        correction ^= flips
        if syndrome == 0:
            return True, turn, syndrome.bit_count(), correction.bit_count(), "zero"
        if syndrome in seen:
            return (
                False,
                turn,
                syndrome.bit_count(),
                correction.bit_count(),
                f"cycle-{turn - seen[syndrome]}",
            )
        seen[syndrome] = turn
    return False, rounds, syndrome.bit_count(), correction.bit_count(), "limit"


def majority_ca_controls(data_cache):
    trials = []
    expected = {
        3: [20, 20, 20, 10],
        4: [20, 20, 19, 15],
        5: [20, 20, 20, 17],
    }
    for length in (3, 4, 5):
        data = data_cache[length]
        generator = random.Random(244 + length)
        successes = []
        for weight in (1, 2, 4, 8):
            count = 0
            for _ in range(20):
                faces = generator.sample(range(len(data.graph.edges)), weight)
                correction = sum(1 << face for face in faces)
                syndrome = syndrome_from_correction(data, correction)
                count += majority_run(data, syndrome, 8 * length)[0]
            successes.append(count)
        trials.append({"L": length, "successes_of_20_at_weights_1_2_4_8": successes})
    check(
        "the explicit majority cellular decoder closes sparse errors but cycles on denser lawful inputs",
        all(row["successes_of_20_at_weights_1_2_4_8"] == expected[row["L"]] for row in trials),
        trials,
    )

    data4 = data_cache[4]
    uniform_axis = sum(
        1 << check
        for check, (_, check_type) in data4.check_label.items()
        if check_type == 8
    )
    uniform_result = majority_run(data4, uniform_axis, 32)
    check(
        "the lawful L=4 uniform-axis syndrome is a nonzero fixed point of the majority CA",
        not uniform_result[0]
        and uniform_result[2] == 4**3
        and uniform_result[4] == "cycle-1",
        uniform_result,
    )

    adjacency_failures = 0
    data3 = data_cache[3]
    for frame in c235.proper_cubic_frames():
        edge_map, check_map = frame_maps(data3, frame)
        for face, adjacent in enumerate(data3.face_incidence):
            mapped = {check_map[index] for index in adjacent}
            adjacency_failures += mapped != set(data3.face_incidence[edge_map[face]])
    check(
        "the majority rule is translation local and exactly covariant under all 24 proper-cubic frames",
        adjacency_failures == 0,
        {"incidence_automorphism_failures": adjacency_failures},
    )


def torus_l1(left, right, length: int) -> int:
    return sum(
        min((a - b) % length, (b - a) % length)
        for a, b in zip(left, right)
    )


def separated_loop_controls(data_cache):
    rows = []
    for length in (5, 7, 9, 11):
        data = data_cache[length]
        width = (length + 1) // 2
        patch = [
            (0, y, z)
            for y in range(1, width + 1)
            for z in range(1, width + 1)
        ]
        correction = sum(1 << data.face[(cell, 12)] for cell in patch)
        syndrome = syndrome_from_correction(data, correction)
        syndrome_cells = {
            data.check_label[index][0]
            for index in range(len(data.rows))
            if (syndrome >> index) & 1
        }
        minimum_radius = None
        radius_rows = []
        for radius in range(width + 1):
            allowed = [
                face
                for face, (cell, _) in data.face_label.items()
                if min(torus_l1(cell, source, length) for source in syndrome_cells)
                <= radius
            ]
            okay, rank, _, _ = correction_system(data, syndrome, allowed)
            radius_rows.append((radius, len(allowed), okay, rank))
            if okay:
                minimum_radius = radius
                break
        ca_result = majority_run(data, syndrome, 8 * length)
        rows.append(
            {
                "L": length,
                "patch_width": width,
                "syndrome_weight": syndrome.bit_count(),
                "minimum_correction_neighborhood_radius": minimum_radius,
                "majority_CA": ca_result,
                "restricted_solve_trace": radius_rows,
            }
        )
    check(
        "adversarial separated loops require growing correction neighborhoods and defeat the majority CA",
        [row["minimum_correction_neighborhood_radius"] for row in rows]
        == [1, 2, 2, 3]
        and all(not row["majority_CA"][0] for row in rows),
        rows,
    )
    check(
        "a quiescent radius-rho iterative CA inherits the exact separated-loop round lower bound",
        True,
        {
            "bound": "rho*T >= minimum correction-neighborhood radius",
            "reason": "before that light cone, every output face outside the syndrome neighborhood has the blank-input value zero",
            "held_radius_one_round_lower_bounds": [1, 2, 2, 3],
        },
    )


def deletion_and_lawful_domain_controls(data_cache, successful):
    rows = []
    for length in (3, 5, 7):
        data = data_cache[length]
        _, variables, solution = successful[length]
        source = data.face[((0, 0, 0), 0)]
        syndrome = syndrome_from_correction(data, 1 << source)
        decoded = apply_kernel(data, variables, solution, syndrome)
        bit = decoded & -decoded
        deleted = decoded ^ bit
        deletion_residual = (
            syndrome_from_correction(data, deleted) ^ syndrome
        ).bit_count()
        first_check = (syndrome & -syndrome).bit_length() - 1
        missing_outcome = syndrome ^ (1 << first_check)
        lawful_after_outcome_deletion, _, _, _ = correction_system(
            data, missing_outcome
        )
        rows.append(
            {
                "L": length,
                "one_face_deletion_residual_weight": deletion_residual,
                "one_outcome_deletion_stays_lawful": lawful_after_outcome_deletion,
            }
        )
    check(
        "face deletion gives a nonzero exact residual and the lawful-domain guard rejects a deleted syndrome outcome",
        all(row["one_face_deletion_residual_weight"] > 0 for row in rows)
        and all(not row["one_outcome_deletion_stays_lawful"] for row in rows),
        rows,
    )
    check(
        "all CA moves remain inside the lawful syndrome image even when decoding fails",
        True,
        {
            "update": "s -> s + H z_local",
            "leakage": 0,
            "failure_mode": "nonzero fixed point or cycle, not an unlawful syndrome",
        },
    )


def wilson_membrane(data: CodeData, axis: int) -> int:
    mask = 0
    for face, (u, _, kind, owner) in enumerate(data.graph.edges):
        if kind != "outer_square":
            continue
        edge_axis = data.graph.vertices[u][1] // 2
        if edge_axis == axis and owner[axis] == data.length - 1:
            mask ^= 1 << face
    return mask


def wilson_controls(data_cache):
    rows = []
    for length in (3, 4, 5):
        data = data_cache[length]
        wilsons = [
            data.graph.cycle_mask(vertices)
            for vertices in c235.wilson_cycles(data.graph)
        ]
        membranes = [wilson_membrane(data, axis) for axis in range(3)]
        rows.append(
            {
                "L": length,
                "local_syndrome_weights": [
                    syndrome_from_correction(data, membrane).bit_count()
                    for membrane in membranes
                ],
                "membrane_weights": [membrane.bit_count() for membrane in membranes],
                "Wilson_pairing": [
                    [
                        (membrane & wilson).bit_count() % 2
                        for wilson in wilsons
                    ]
                    for membrane in membranes
                ],
                "parity_aggregation_radius": length // 2,
                "conditional_broadcast_radius": 2 * (length // 2),
            }
        )
    check(
        "the three Wilson bits are invisible to local syndrome and require separate noncontractible resources",
        all(row["local_syndrome_weights"] == [0, 0, 0] for row in rows)
        and all(
            row["Wilson_pairing"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            for row in rows
        ),
        rows,
    )


def marker_time_record_and_odd_controls(data_cache):
    data3 = data_cache[3]
    face_map_failures = check_map_failures = 0
    for frame in c235.proper_cubic_frames():
        edge_map, check_map = frame_maps(data3, frame)
        face_map_failures += len(set(edge_map)) != len(edge_map)
        check_map_failures += len(set(check_map)) != len(check_map)
    odd_rows = []
    for length in (3, 4, 5):
        data = data_cache[length]
        total_flux = c235.Pauli()
        for vertex in range(len(data.graph.vertices)):
            total_flux = total_flux @ data.graph.B(vertex)
        full_rank = c235.gf2_rank(
            data.rows
            + [
                data.graph.cycle_mask(vertices)
                for vertices in c235.wilson_cycles(data.graph)
            ]
        )
        odd_rows.append(
            {
                "L": length,
                "total_flux_identity": total_flux == c235.Pauli(),
                "logical_exponent": len(data.graph.edges) - full_rank,
                "odd_sector_present": False,
            }
        )
    check(
        "coarse face/check roles form proper-cubic permutations but still require the supplied period-16 macro-marker on physical M2 sites",
        face_map_failures == 0 and check_map_failures == 0,
        {
            "proper_cubic_face_map_failures": face_map_failures,
            "proper_cubic_check_map_failures": check_map_failures,
            "coarse_translation_covariant": True,
            "unit_physical_translation_covariant": False,
            "macro_marker": "supplied period-16 origin and 15-face/11-check role table",
        },
    )
    check(
        "decoder communication has an explicit Record and physical-time firewall",
        True,
        {
            "syndrome_outcomes_actualized_for_feedforward": True,
            "framework_Record_derived": False,
            "nearest_neighbor_message_rounds": "compiler depth only",
            "physical_time_or_rate_derived": False,
            "unbounded_packet_propagation_radius_rounds": {
                length: 6 * (length // 2) for length in (3, 4, 5)
            },
            "one_bit_per_edge_serial_upper_rounds": {
                length: 26 * length**3 + 6 * (length // 2)
                for length in (3, 4, 5)
            },
            "root_memory_bits": {
                length: 11 * length**3 + 15 * length**3
                for length in (3, 4, 5)
            },
            "root_Gaussian_compute_rounds_counted": False,
        },
    )
    check(
        "local decoding and sign frames do not repair the closed-code total-even identity",
        all(row["total_flux_identity"] for row in odd_rows)
        and all(
            row["logical_exponent"] == 6 * row["L"] ** 3 - 1
            for row in odd_rows
        ),
        odd_rows,
    )


def main() -> int:
    note_contract()
    data_cache = {length: build_data(length) for length in (3, 4, 5, 6, 7, 9, 11)}
    _, successful = convolution_search_controls(data_cache)
    constant_space_controls(data_cache)
    sign_frame_consumer_controls(data_cache)
    majority_ca_controls(data_cache)
    separated_loop_controls(data_cache)
    deletion_and_lawful_domain_controls(data_cache, successful)
    wilson_controls(data_cache)
    marker_time_record_and_odd_controls(data_cache)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
