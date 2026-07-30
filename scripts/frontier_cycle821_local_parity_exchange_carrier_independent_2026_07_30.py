#!/usr/bin/env python3
"""Independent Cycle-821 local parity-exchange-carrier checker.

This runner does not import the Cycle-821 primary.  It reconstructs the
landed Cycle-789 rank-23 character circuit from Cycle-720/789 dependencies,
adds one parity carrier M2 per coarse cell, and checks the complete
pump--Bell--correction marginal.  Circuit ordinals are structure, not time.

The physical claim is bounded-composite parity conservation.  A separate
local compiler check replaces every pair of parity-odd X/Y letters by the
identity U^dagger CZ U, U=exp(-i pi K/4).  The two-qubit Pauli rotations U
are not routed here; nearest-neighbour/radius-one synthesis and inclusion of
the non-Clifford recurrent G in this same executor remain open.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
import json
import sys

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T708
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q720
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P720
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_"
    "CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "docs/LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/FULL128_TWO_CELL_PARITY_SUPERSELECTED_EVEN_CAR_COVARIANCE_CYCLE820_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


SHAPE = (2, 1, 1)
ZERO = (0, 0, 0)
CARRIER_OFFSET = (3, -7, -4)
Row = tuple[int, int, int]
Gate = tuple[str, int] | tuple[str, int, int, str]


def fields(row: Row) -> Row:
    return row[0] % 4, int(row[1]), int(row[2])


def imported(row) -> Row:
    return int(row.phase) % 4, int(row.x), int(row.z)


def multiply(left: Row, right: Row) -> Row:
    phase = (
        left[0] + right[0] + 2 * (left[2] & right[1]).bit_count()
    ) % 4
    return phase, left[1] ^ right[1], left[2] ^ right[2]


def canonical(x: int, z: int, negative: bool = False) -> Row:
    return ((x & z).bit_count() + 2 * int(negative)) % 4, x, z


def shift(row: Row, offset: int) -> Row:
    return row[0] % 4, row[1] << offset, row[2] << offset


def pair_same(row: Row, left: int, right: int) -> Row:
    return canonical(
        (row[1] << left) | (row[1] << right),
        (row[2] << left) | (row[2] << right),
    )


def symplectic_vector(row: Row, width: int) -> int:
    return row[1] | (row[2] << width)


def anticommutes(left: Row, right: Row) -> int:
    return (
        (left[1] & right[2]).bit_count()
        ^ (left[2] & right[1]).bit_count()
    ) & 1


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def relation_masks(vectors: tuple[int, ...]) -> tuple[int, ...]:
    pivots: dict[int, tuple[int, int]] = {}
    relations = []
    for index, original in enumerate(vectors):
        vector = int(original)
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                prior, prior_combination = pivots[pivot]
                vector ^= prior
                combination ^= prior_combination
            else:
                pivots[pivot] = vector, combination
                break
        if not vector:
            relations.append(combination)
    return tuple(relations)


def span_pivots(basis: tuple[Row, ...], width: int):
    pivots: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(basis):
        vector = symplectic_vector(original, width)
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                prior, prior_combination = pivots[pivot]
                vector ^= prior
                combination ^= prior_combination
            else:
                pivots[pivot] = vector, combination
                break
    return pivots


def span_combination(target: Row, width: int, pivots) -> int | None:
    vector = symplectic_vector(target, width)
    combination = 0
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in pivots:
            return None
        prior, prior_combination = pivots[pivot]
        vector ^= prior
        combination ^= prior_combination
    return combination


def rows_from_mask(rows: tuple[Row, ...], mask: int) -> Row:
    output: Row = (0, 0, 0)
    while mask:
        bit = mask & -mask
        output = multiply(output, rows[bit.bit_length() - 1])
        mask ^= bit
    return output


def signed_span_failures(
    targets: tuple[Row, ...], basis: tuple[Row, ...], width: int
) -> tuple[int, int]:
    pivots = span_pivots(basis, width)
    binary = signed = 0
    for target in targets:
        combination = span_combination(target, width, pivots)
        if combination is None:
            binary += 1
            signed += 1
            continue
        replay = rows_from_mask(basis, combination)
        signed += fields(replay) != fields(target)
    return binary, signed


def apply_images(
    row: Row, images: tuple[tuple[Row, ...], tuple[Row, ...]]
) -> Row:
    output: Row = (row[0] % 4, 0, 0)
    for source_rows, mask in zip(images, (row[1], row[2])):
        while mask:
            bit = mask & -mask
            output = multiply(output, source_rows[bit.bit_length() - 1])
            mask ^= bit
    return output


def conjugate_h(row: Row, qubit: int) -> Row:
    bit = 1 << qubit
    x = int(bool(row[1] & bit))
    z = int(bool(row[2] & bit))
    output_x = (row[1] & ~bit) | (bit if z else 0)
    output_z = (row[2] & ~bit) | (bit if x else 0)
    return (row[0] + 2 * x * z) % 4, output_x, output_z


def conjugate_z_sign(row: Row, qubit: int) -> Row:
    return (row[0] + 2 * ((row[1] >> qubit) & 1)) % 4, row[1], row[2]


def letter_row(qubit: int, letter: str) -> Row:
    if letter == "X":
        return 0, 1 << qubit, 0
    if letter == "Z":
        return 0, 0, 1 << qubit
    if letter == "Y":
        return 1, 1 << qubit, 1 << qubit
    raise ValueError(letter)


def letter_at(row: Row, qubit: int) -> str:
    x = (row[1] >> qubit) & 1
    z = (row[2] >> qubit) & 1
    return ("I", "X", "Z", "Y")[x + 2 * z]


def hermitian_sign(row: Row) -> int:
    delta = (row[0] - (row[1] & row[2]).bit_count()) % 4
    if delta not in (0, 2):
        raise ValueError(("anti-Hermitian row", row))
    return delta // 2


def conjugate_controlled_letter(
    row: Row, control: int, target: int, letter: str
) -> Row:
    local_mask = (1 << control) | (1 << target)
    rest = row[0], row[1] & ~local_mask, row[2] & ~local_mask
    target_pauli = letter_row(target, letter)
    xc_image = multiply((0, 1 << control, 0), target_pauli)
    zc_image: Row = (0, 0, 1 << control)
    xt: Row = (0, 1 << target, 0)
    zt: Row = (0, 0, 1 << target)
    xt_image = multiply(zc_image, xt) if target_pauli[2] & (1 << target) else xt
    zt_image = multiply(zc_image, zt) if target_pauli[1] & (1 << target) else zt
    local: Row = (0, 0, 0)
    if row[1] & (1 << control):
        local = multiply(local, xc_image)
    if row[1] & (1 << target):
        local = multiply(local, xt_image)
    if row[2] & (1 << control):
        local = multiply(local, zc_image)
    if row[2] & (1 << target):
        local = multiply(local, zt_image)
    return multiply(rest, local)


def signed_controlled_gates(control: int, row: Row) -> tuple[Gate, ...]:
    gates: list[Gate] = []
    if hermitian_sign(row):
        gates.append(("Z_SIGN", control))
    mask = row[1] | row[2]
    while mask:
        bit = mask & -mask
        qubit = bit.bit_length() - 1
        gates.append(("CP", control, qubit, letter_at(row, qubit)))
        mask ^= bit
    return tuple(gates)


def conjugate_basis(
    rows: tuple[Row, ...], gates: tuple[Gate, ...]
) -> tuple[Row, ...]:
    output = list(rows)
    for gate in gates:
        if gate[0] == "H":
            output = [conjugate_h(row, gate[1]) for row in output]
        elif gate[0] == "Z_SIGN":
            output = [conjugate_z_sign(row, gate[1]) for row in output]
        elif gate[0] == "CP":
            output = [
                conjugate_controlled_letter(row, gate[1], gate[2], gate[3])
                for row in output
            ]
        else:
            raise ValueError(gate)
    return tuple(output)


def output_marginal(
    final: tuple[Row, ...], width: int, allowed: int
) -> tuple[Row, ...]:
    outside = ((1 << width) - 1) ^ allowed
    vectors = tuple(
        (row[1] & outside) | ((row[2] & outside) << width)
        for row in final
    )
    return tuple(rows_from_mask(final, mask) for mask in relation_masks(vectors))


def marginal_comparison(
    final: tuple[Row, ...],
    expected: tuple[Row, ...],
    width: int,
    allowed: int,
) -> dict[str, int]:
    marginal = output_marginal(final, width, allowed)
    left_binary, left_signed = signed_span_failures(expected, marginal, width)
    right_binary, right_signed = signed_span_failures(marginal, expected, width)
    return {
        "rank": gf2_rank(symplectic_vector(row, width) for row in marginal),
        "rows": len(marginal),
        "binary_failures": left_binary + right_binary,
        "signed_failures": left_signed + right_signed,
    }


def build_landed_data(atlas):
    fixture = O720.arbitrary_fixture(Q720.shape_cells(SHAPE))
    compiled = B.compile_fixture(fixture)
    rows = tuple(imported(word["physical"]) for word in compiled["words"])
    corrections = tuple(
        imported(P720.correction_from_atlas(fixture, tag, atlas))
        for tag in compiled["tags"]
    )
    owners = tuple(
        tag[1] if tag[0] != "edge" else fixture.edges[tag[1]][0]
        for tag in compiled["tags"]
    )
    matter_parity: Row = (0, 0, (1 << fixture.matter_qubits) - 1)
    odd = tuple(
        index for index, row in enumerate(corrections)
        if anticommutes(row, matter_parity)
    )
    return fixture, compiled, rows, corrections, owners, odd


def extended_correction(
    row: Row,
    index: int,
    owners: tuple[int, ...],
    odd: tuple[int, ...],
    carrier_positions: tuple[int, int],
    offset: int = 0,
) -> Row:
    output = shift(row, offset)
    if index in odd:
        output = multiply(
            output, (0, 1 << carrier_positions[owners[index]], 0)
        )
    return output


def epoch_word(
    rows: tuple[Row, ...],
    corrections: tuple[Row, ...],
    owners: tuple[int, ...],
    odd: tuple[int, ...],
    q: int,
    rank: int,
    block: int,
    carrier_positions: tuple[int, int],
    epoch: int,
    *,
    mutation: tuple[str, int, str] | None = None,
    pump_only: bool = False,
) -> tuple[Gate, ...]:
    base = epoch * block
    gates: list[Gate] = []

    def measurement(index: int, stage: str) -> tuple[Gate, ...]:
        bank = 0 if stage == "pump" else q
        control = base + 4 * q + (0 if stage == "pump" else rank) + index
        measured = pair_same(rows[index], base + bank, base + bank + q)
        return (
            (("H", control),)
            + signed_controlled_gates(control, measured)
            + (("H", control),)
        )

    def correction(index: int, stage: str) -> tuple[Gate, ...]:
        control = base + 4 * q + (0 if stage == "pump" else rank) + index
        kind = (
            mutation[2]
            if mutation is not None and mutation[:2] == (stage, index)
            else None
        )
        if kind == "entire":
            return ()
        matter = shift(corrections[index], base)
        carrier = (0, 1 << carrier_positions[owners[index]], 0)
        if kind == "matter":
            target = carrier
        elif kind == "carrier":
            target = matter
        elif index in odd:
            target = multiply(matter, carrier)
        else:
            target = matter
        return signed_controlled_gates(control, target)

    for index in range(rank):
        gates.extend(measurement(index, "pump"))
        gates.extend(correction(index, "pump"))
    if pump_only:
        return tuple(gates)
    for index in range(rank):
        gates.extend(measurement(index, "bell"))
    for index in range(rank):
        gates.extend(correction(index, "bell"))
    return tuple(gates)


def signed_state_row(axis: str, qubit: int) -> Row:
    return {
        "X": (0, 1 << qubit, 0),
        "Y": (1, 1 << qubit, 1 << qubit),
        "Z": (0, 0, 1 << qubit),
    }[axis]


def two_copy_shared_carrier_certificate(
    fixture, rows, corrections, owners, odd
) -> dict[str, object]:
    q = fixture.qubits
    rank = len(rows)
    copies = 2
    block = 4 * q + 2 * rank
    carriers = (copies * block, copies * block + 1)
    width = copies * block + 2
    gates = tuple(
        gate
        for copy in range(copies)
        for gate in epoch_word(
            rows,
            corrections,
            owners,
            odd,
            q,
            rank,
            block,
            carriers,
            copy,
        )
    )
    initial = tuple(
        row
        for copy in range(copies)
        for row in (
            tuple(
                pair_same(item, copy * block + 2 * q, copy * block + 3 * q)
                for item in rows
            )
            + tuple(
                (0, 0, 1 << (copy * block + 4 * q + index))
                for index in range(2 * rank)
            )
        )
    )
    expected = tuple(
        row
        for copy in range(copies)
        for row in tuple(
            pair_same(item, copy * block, copy * block + 3 * q)
            for item in rows
        )
    )
    allowed = 0
    for copy in range(copies):
        allowed |= ((1 << q) - 1) << (copy * block)
        allowed |= ((1 << q) - 1) << (copy * block + 3 * q)
    final_base = conjugate_basis(initial, gates)
    carrier_images = {
        (cell, axis): conjugate_basis(
            (signed_state_row(axis, carriers[cell]),), gates
        )[0]
        for cell in range(2)
        for axis in "XYZ"
    }

    state_rows = []
    failures = 0
    ranks = []
    for left, right in product(("I", "X", "Y", "Z"), repeat=2):
        extra = []
        if left != "I":
            extra.append(carrier_images[(0, left)])
        if right != "I":
            extra.append(carrier_images[(1, right)])
        comparison = marginal_comparison(
            final_base + tuple(extra), expected, width, allowed
        )
        ranks.append(comparison["rank"])
        failures += (
            comparison["binary_failures"]
            + comparison["signed_failures"]
            + int(comparison["rank"] != 2 * rank)
        )
        state_rows.append((left, right, comparison["rank"]))

    hostile = {}
    for label, initial_carrier_rows in {
        "Bell_Phi_plus": (
            canonical((1 << carriers[0]) | (1 << carriers[1]), 0),
            canonical(0, (1 << carriers[0]) | (1 << carriers[1])),
        ),
        "Bell_singlet": (
            canonical(
                (1 << carriers[0]) | (1 << carriers[1]), 0, True
            ),
            canonical(
                0, (1 << carriers[0]) | (1 << carriers[1]), True
            ),
        ),
    }.items():
        evolved = conjugate_basis(tuple(initial_carrier_rows), gates)
        hostile[label] = marginal_comparison(
            final_base + evolved, expected, width, allowed
        )

    update_failures = 0
    update_rows = []
    for cell in range(2):
        initial_x = (0, 1 << carriers[cell], 0)
        initial_z = (0, 0, 1 << carriers[cell])
        final_x, final_z = conjugate_basis((initial_x, initial_z), gates)
        expected_z = initial_z
        controls = []
        for copy in range(copies):
            for stage_offset in (0, rank):
                for index in odd:
                    if owners[index] != cell:
                        continue
                    control = copy * block + 4 * q + stage_offset + index
                    expected_z = multiply(expected_z, (0, 0, 1 << control))
                    controls.append(control)
        x_failure = fields(final_x) != fields(initial_x)
        z_failure = fields(final_z) != fields(expected_z)
        update_failures += x_failure + z_failure
        update_rows.append({
            "cell": cell,
            "retained_syndrome_controls": len(controls),
            "X_invariant_failure": int(x_failure),
            "Z_control_product_failure": int(z_failure),
        })

    # The pump resource is also checked independently of a carrier state by
    # using the maximally mixed carrier input (no carrier stabilizer rows).
    pump_gates = epoch_word(
        rows,
        corrections,
        owners,
        odd,
        q,
        rank,
        block,
        carriers,
        0,
        pump_only=True,
    )
    pump_initial = tuple((0, 0, 1 << (4 * q + index)) for index in range(rank))
    pump_expected = tuple(pair_same(item, 0, q) for item in rows)
    pump_allowed = (1 << (2 * q)) - 1
    pump_comparison = marginal_comparison(
        conjugate_basis(pump_initial, pump_gates),
        pump_expected,
        width,
        pump_allowed,
    )
    return {
        "disjoint_channel_copies": copies,
        "carrier_M2_per_cell": 1,
        "carrier_density_spanning_states": len(state_rows),
        "carrier_state_basis": ("I/2", "X+", "Y+", "Z+"),
        "expected_output_rank": 2 * rank,
        "output_rank_range": (min(ranks), max(ranks)),
        "carrier_state_binary_signed_or_rank_failures": failures,
        "hostile_carrier_states": hostile,
        "pump_resource": pump_comparison,
        "carrier_update_failures": update_failures,
        "carrier_updates": tuple(update_rows),
        "carrier_controls_per_cell_per_copy": len(odd),
        "conditional_update": (
            "rho_c -> X_c^r rho_c X_c^r, with r the xor of the six pump "
            "and six Bell odd-row syndromes in that cell"
        ),
        "two_copy_channel_identity_for_all_inputs_condition": (
            "r_cell_copy_1 xor r_cell_copy_2 = 0; cumulative r=1 still "
            "fixes state-specific X-invariant inputs"
        ),
    }


def frame_images(source, target, frame):
    target_seed = Q720.transported_seed(frame, ZERO, ZERO)
    solution = Q720.seeded_sheet_solution(
        frame, Q720.predicted_sheet_solution(frame), target_seed
    )
    x_images, z_images = Q720.corrected_images(
        source, target, frame, ZERO, solution
    )
    return tuple(map(imported, x_images)), tuple(map(imported, z_images))


def one_epoch_frame_state_certificate(
    fixture,
    rows,
    corrections,
    owners,
    frames,
) -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
    q = fixture.qubits
    rank = len(rows)
    block = 4 * q + 2 * rank
    carriers = (block, block + 1)
    width = block + 2
    allowed = ((1 << q) - 1) | (((1 << q) - 1) << (3 * q))
    matter_parity: Row = (0, 0, (1 << fixture.matter_qubits) - 1)
    extended_parity: Row = (
        0,
        0,
        ((1 << fixture.matter_qubits) - 1)
        | (1 << carriers[0])
        | (1 << carriers[1]),
    )
    contexts = failures = 0
    marginal_ranks = []
    duality_failures = 0
    mapped_rank_failures = extended_rank_failures = 0
    parity_failures = odd_census_failures = 0
    mapped_odd_outside_owner = 0
    support_histogram: Counter[tuple[int, int]] = Counter()
    maximum_extended_weight = 0
    compiler_rows = []

    for frame_id, frame in enumerate(frames):
        target = O720.arbitrary_fixture(
            Q720.affine_cells(fixture.cells, frame, ZERO)
        )
        images = frame_images(fixture, target, frame)
        mapped_rows = tuple(apply_images(row, images) for row in rows)
        mapped_corrections = tuple(
            apply_images(row, images) for row in corrections
        )
        mapped_owner_cells = tuple(
            tuple(int(value) for value in (
                frame @ np.asarray(fixture.cells[owner], dtype=int)
            ))
            for owner in owners
        )
        mapped_owners = tuple(
            target.cells.index(cell) for cell in mapped_owner_cells
        )
        local_odd = tuple(
            index for index, row in enumerate(mapped_corrections)
            if anticommutes(row, matter_parity)
        )
        expected_odd = tuple(range(6)) + tuple(range(11, 17))
        odd_census_failures += local_odd != expected_odd
        extended = tuple(
            extended_correction(
                row,
                index,
                mapped_owners,
                local_odd,
                carriers,
            )
            for index, row in enumerate(mapped_corrections)
        )
        mapped_rank_failures += (
            gf2_rank(symplectic_vector(row, q) for row in mapped_corrections)
            != rank
        )
        extended_rank_failures += (
            gf2_rank(symplectic_vector(row, width) for row in extended)
            != rank
        )
        parity_failures += sum(
            anticommutes(row, extended_parity) for row in extended
        )
        maximum_extended_weight = max(
            maximum_extended_weight,
            max((row[1] | row[2]).bit_count() for row in extended),
        )
        for index, correction in enumerate(mapped_corrections):
            for row_id, physical in enumerate(mapped_rows):
                duality_failures += (
                    anticommutes(correction, physical) != int(index == row_id)
                )
            support = set()
            for qubit in range(q):
                if not (((correction[1] | correction[2]) >> qubit) & 1):
                    continue
                if qubit < fixture.matter_qubits:
                    support.add(target.cells[qubit // 6])
                else:
                    support.add(
                        target.cells[(qubit - fixture.matter_qubits) // 3]
                    )
            is_odd = int(index in local_odd)
            support_histogram[(is_odd, len(support))] += 1
            if is_odd and not support <= {mapped_owner_cells[index]}:
                mapped_odd_outside_owner += 1
            compiler_rows.append({
                "row": extended[index],
                "matter_modes": fixture.matter_qubits,
                "width": width,
                "parity": extended_parity,
            })

        gates = epoch_word(
            mapped_rows,
            mapped_corrections,
            mapped_owners,
            local_odd,
            q,
            rank,
            block,
            carriers,
            0,
        )
        initial = (
            tuple(pair_same(row, 2 * q, 3 * q) for row in mapped_rows)
            + tuple((0, 0, 1 << (4 * q + index)) for index in range(2 * rank))
        )
        expected = tuple(pair_same(row, 0, 3 * q) for row in mapped_rows)
        final_base = conjugate_basis(initial, gates)
        carrier_images = {
            (cell, axis): conjugate_basis(
                (signed_state_row(axis, carriers[cell]),), gates
            )[0]
            for cell in range(2)
            for axis in "XYZ"
        }
        for left, right in product(("I", "X", "Y", "Z"), repeat=2):
            extra = []
            if left != "I":
                extra.append(carrier_images[(0, left)])
            if right != "I":
                extra.append(carrier_images[(1, right)])
            comparison = marginal_comparison(
                final_base + tuple(extra), expected, width, allowed
            )
            marginal_ranks.append(comparison["rank"])
            failures += (
                comparison["binary_failures"]
                + comparison["signed_failures"]
                + int(comparison["rank"] != rank)
            )
            contexts += 1

    report = {
        "proper_frames": len(frames),
        "carrier_density_spanning_states_per_frame": 16,
        "frame_state_contexts": contexts,
        "expected_marginal_rank": rank,
        "marginal_rank_range": (min(marginal_ranks), max(marginal_ranks)),
        "binary_signed_or_rank_failures": failures,
        "mapped_correction_rows": len(frames) * rank,
        "mapped_private_duality_failures": duality_failures,
        "mapped_correction_rank_failures": mapped_rank_failures,
        "extended_correction_rank_failures": extended_rank_failures,
        "extended_parity_failures": parity_failures,
        "odd_census_failures": odd_census_failures,
        "mapped_odd_rows_outside_transported_owner_cell": (
            mapped_odd_outside_owner
        ),
        "support_histogram": {
            f"odd={key[0]},cells={key[1]}": value
            for key, value in sorted(support_histogram.items())
        },
        "maximum_extended_correction_weight": maximum_extended_weight,
    }
    return report, tuple(compiler_rows)


def deletion_certificate(fixture, rows, corrections, owners, odd):
    q = fixture.qubits
    rank = len(rows)
    block = 4 * q + 2 * rank
    carriers = (block, block + 1)
    width = block + 2
    initial = (
        tuple(pair_same(row, 2 * q, 3 * q) for row in rows)
        + tuple((0, 0, 1 << (4 * q + index)) for index in range(2 * rank))
    )
    expected = tuple(pair_same(row, 0, 3 * q) for row in rows)
    allowed = ((1 << q) - 1) | (((1 << q) - 1) << (3 * q))
    extended_parity: Row = (
        0,
        0,
        ((1 << fixture.matter_qubits) - 1)
        | (1 << carriers[0])
        | (1 << carriers[1]),
    )
    report = {}
    for stage in ("pump", "bell"):
        for kind in ("entire", "matter", "carrier"):
            failures = []
            parity_detection = 0
            for index in odd:
                gates = epoch_word(
                    rows,
                    corrections,
                    owners,
                    odd,
                    q,
                    rank,
                    block,
                    carriers,
                    0,
                    mutation=(stage, index, kind),
                )
                comparison = marginal_comparison(
                    conjugate_basis(initial, gates),
                    expected,
                    width,
                    allowed,
                )
                failures.append(
                    comparison["binary_failures"]
                    + comparison["signed_failures"]
                )
                if kind in ("matter", "carrier"):
                    target = (
                        (0, 1 << carriers[owners[index]], 0)
                        if kind == "matter"
                        else corrections[index]
                    )
                    parity_detection += anticommutes(target, extended_parity)
            report[f"{stage}_{kind}"] = {
                "tested": len(failures),
                "undetected_by_output": sum(value == 0 for value in failures),
                "minimum_output_failure": min(failures),
                "maximum_output_failure": max(failures),
                "parity_detections": parity_detection,
            }
    return report


def pair_compiler_matrix_certificate() -> dict[str, object]:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    zero = np.asarray(((1, 0), (0, 0)), dtype=complex)
    one = np.asarray(((0, 0), (0, 1)), dtype=complex)
    parity = np.kron(identity, np.kron(z, z))
    z_pivot = np.kron(identity, np.kron(identity, z))
    cz = np.kron(zero, np.kron(identity, identity)) + np.kron(
        one, np.kron(identity, z)
    )
    rows = []
    maximum_identity_residual = 0.0
    maximum_gate_parity_residual = 0.0
    maximum_prefix_parity_residual = 0.0
    maximum_rotation_residual = 0.0
    for left_letter, right_letter in product(("X", "Y"), repeat=2):
        left = x if left_letter == "X" else y
        right = x if right_letter == "X" else y
        target = np.kron(left, right)
        q_full = np.kron(identity, target)
        k_target = -1j * target @ np.kron(identity, z)
        k_full = np.kron(identity, k_target)
        unitary = (np.eye(8, dtype=complex) - 1j * k_full) / np.sqrt(2.0)
        controlled_q = np.kron(zero, np.eye(4)) + np.kron(one, target)
        actual = unitary.conj().T @ cz @ unitary
        rotation = unitary.conj().T @ z_pivot @ unitary
        identity_residual = float(np.linalg.norm(actual - controlled_q))
        rotation_residual = float(np.linalg.norm(rotation - q_full))
        maximum_identity_residual = max(
            maximum_identity_residual, identity_residual
        )
        maximum_rotation_residual = max(
            maximum_rotation_residual, rotation_residual
        )
        emitted = (unitary.conj().T, cz, unitary)
        prefix = np.eye(8, dtype=complex)
        gate_residuals = []
        prefix_residuals = []
        for gate in emitted:
            gate_residuals.append(float(np.linalg.norm(gate @ parity - parity @ gate)))
            prefix = prefix @ gate
            prefix_residuals.append(
                float(np.linalg.norm(prefix @ parity - parity @ prefix))
            )
        maximum_gate_parity_residual = max(
            maximum_gate_parity_residual, *gate_residuals
        )
        maximum_prefix_parity_residual = max(
            maximum_prefix_parity_residual, *prefix_residuals
        )
        rows.append({
            "pair": left_letter + right_letter,
            "U_dagger_CZ_U_identity_residual": identity_residual,
            "U_dagger_Z_pivot_U_rotation_residual": rotation_residual,
            "maximum_elementary_gate_parity_commutator": max(gate_residuals),
            "maximum_prefix_parity_commutator": max(prefix_residuals),
        })
    return {
        "pairs": tuple(rows),
        "pair_types_tested": len(rows),
        "maximum_identity_residual": maximum_identity_residual,
        "maximum_rotation_residual": maximum_rotation_residual,
        "maximum_elementary_gate_parity_commutator": (
            maximum_gate_parity_residual
        ),
        "maximum_prefix_parity_commutator": maximum_prefix_parity_residual,
        "identity": (
            "C(A_left A_right) = U^dagger CZ(control,pivot) U, "
            "K=-i(A_left A_right)Z_pivot, U=exp(-i*pi*K/4)"
        ),
    }


def compiler_decomposition_certificate(compiler_rows):
    pair_types: Counter[str] = Counter()
    pair_compilers = single_letters = sign_repairs = 0
    binary_failures = signed_failures = 0
    factor_parity_failures = prefix_parity_failures = 0
    odd_letter_pairing_failures = 0
    emitted_elementary_gates = 0
    for record in compiler_rows:
        row = record["row"]
        matter_modes = int(record["matter_modes"])
        width = int(record["width"])
        parity = record["parity"]
        odd_positions = [
            qubit for qubit in range(matter_modes)
            if (row[1] >> qubit) & 1
        ]
        odd_positions.extend(
            qubit for qubit in range(matter_modes, width)
            if (row[1] >> qubit) & 1
            and (parity[2] >> qubit) & 1
        )
        odd_letter_pairing_failures += len(odd_positions) % 2
        paired = set(odd_positions)
        factors = []
        for offset in range(0, len(odd_positions), 2):
            if offset + 1 >= len(odd_positions):
                continue
            left = odd_positions[offset]
            right = odd_positions[offset + 1]
            left_letter = letter_at(row, left)
            right_letter = letter_at(row, right)
            factor = multiply(
                letter_row(left, left_letter),
                letter_row(right, right_letter),
            )
            factors.append(factor)
            pair_types[left_letter + right_letter] += 1
            pair_compilers += 1
            emitted_elementary_gates += 3
        for qubit in range(width):
            if qubit in paired or not (((row[1] | row[2]) >> qubit) & 1):
                continue
            factors.append(letter_row(qubit, letter_at(row, qubit)))
            single_letters += 1
            emitted_elementary_gates += 1
        replay: Row = (0, 0, 0)
        prefix: Row = (0, 0, 0)
        for factor in factors:
            factor_parity_failures += anticommutes(factor, parity)
            prefix = multiply(prefix, factor)
            prefix_parity_failures += anticommutes(prefix, parity)
            replay = multiply(replay, factor)
        binary_failures += replay[1:] != row[1:]
        delta = (row[0] - replay[0]) % 4
        if delta == 2:
            sign_repairs += 1
            emitted_elementary_gates += 1
            replay = ((replay[0] + 2) % 4, replay[1], replay[2])
        elif delta != 0:
            signed_failures += 1
        signed_failures += fields(replay) != fields(row)
    return {
        "corrections_compiled": len(compiler_rows),
        "pair_compilers": pair_compilers,
        "pair_type_counts": dict(sorted(pair_types.items())),
        "single_parity_even_controlled_letters": single_letters,
        "controlled_sign_repairs": sign_repairs,
        "emitted_elementary_gates": emitted_elementary_gates,
        "odd_letter_pairing_failures": odd_letter_pairing_failures,
        "target_binary_reconstruction_failures": binary_failures,
        "target_signed_reconstruction_failures": signed_failures,
        "factor_parity_failures": factor_parity_failures,
        "prefix_parity_failures": prefix_parity_failures,
    }


def schedule_certificate(atlas) -> dict[str, object]:
    rows = []
    for shape in (SHAPE, (6, 5, 4)):
        base, scratch = S789.box_certificate(shape, atlas)
        fixture = scratch["fixture"]
        centers = scratch["centers"]
        carrier_sites = {
            cell: S789.add(centers[cell], CARRIER_OFFSET)
            for cell in fixture.cells
        }
        carrier_palette = set(carrier_sites.values())
        persistent = set().union(*scratch["classes"].values())
        _centers, placed = S789.centers_and_placement(fixture)
        g_word, _update = U720.physical_word(fixture, placed)
        g_touch = {site for instruction in g_word for site in instruction.sites}
        matter_parity = B.Pauli(z=(1 << fixture.matter_qubits) - 1)
        odd = tuple(
            index for index, correction in enumerate(scratch["corrections"])
            if B.M.symplectic(
                correction.symplectic(fixture.qubits),
                matter_parity.symplectic(fixture.qubits),
                fixture.qubits,
            )
        )
        words = []
        macros = []
        for word_id, word in enumerate(scratch["words"]):
            updated = dict(word)
            primitives = list(word["primitives"])
            row_id = word_id // 3
            if row_id in odd and word["stage"] in ("pump", "bell_correction"):
                owner = word["owner"]
                center = centers[owner]
                target = carrier_sites[owner]
                path = S789.route_path(
                    word["ancilla"], center, target, center, word["stage"]
                )
                macro = S789.returned_macro(
                    word["stage"],
                    "parity_carrier_X",
                    owner,
                    word["slot"],
                    word["ancilla"],
                    target,
                    path,
                    "X",
                )
                primitives.extend(macro.primitives)
                macros.append(macro)
            updated["primitives"] = tuple(primitives)
            words.append(updated)
        conflicts, tested_microsteps = S789.primitive_conflicts(words)
        internal_hits = sum(
            len(set(macro.path[1:-1]) & (persistent | carrier_palette | g_touch))
            for macro in macros
        )
        rows.append({
            "shape": shape,
            "cells": len(fixture.cells),
            "carrier_offset": CARRIER_OFFSET,
            "carrier_M2_per_cell": 1,
            "total_M2_per_cell": (
                base["total_explicit_M2_per_cell_including_retained_syndromes"]
                + 1
            ),
            "odd_rows": len(odd),
            "added_macros": len(macros),
            "added_macros_per_cell": len(macros) // len(fixture.cells),
            "carrier_palette_collisions": (
                len(carrier_palette & persistent)
                + len(carrier_sites)
                - len(carrier_palette)
            ),
            "carrier_G_collisions": len(carrier_palette & g_touch),
            "nearest_neighbour_failures": sum(
                S789.manhattan(left, right) != 1
                for macro in macros
                for left, right in zip(macro.path, macro.path[1:])
            ),
            "returned_label_failures": sum(
                S789.label_return_failures(macro) for macro in macros
            ),
            "target_reconstruction_failures": sum(
                S789.routed_target_failures(macro) for macro in macros
            ),
            "internal_live_carrier_or_G_hits": internal_hits,
            "same_block_microstep_collisions": conflicts,
            "tested_active_microsteps": tested_microsteps,
            "route_distance_range": (
                min(len(macro.path) - 1 for macro in macros),
                max(len(macro.path) - 1 for macro in macros),
            ),
            "maximum_word_microsteps_before": base["maximum_word_microsteps"],
            "maximum_word_microsteps_after": max(
                len(word["primitives"]) for word in words
            ),
            "padded_microstep_bound": S789.PADDED_MICROSTEP_BOUND,
            "delete_reverse_SWAP_label_mismatches": min(
                S789.label_return_failures(macro, True)
                for macro in macros
                if any(primitive.kind == "SWAP" for primitive in macro.primitives)
            ),
        })
    return {"placements": tuple(rows)}


def main() -> None:
    atlas = P720.build_private_atlases()
    fixture, compiled, rows, corrections, owners, odd = build_landed_data(atlas)
    frames = tuple(T708.proper_cubic_frames())
    common = two_copy_shared_carrier_certificate(
        fixture, rows, corrections, owners, odd
    )
    frame_report, compiler_rows = one_epoch_frame_state_certificate(
        fixture, rows, corrections, owners, frames
    )
    deletions = deletion_certificate(
        fixture, rows, corrections, owners, odd
    )
    pair_compiler = pair_compiler_matrix_certificate()
    compiler = compiler_decomposition_certificate(compiler_rows)
    schedule = schedule_certificate(atlas)
    forbidden_imports = tuple(sorted(
        name for name in sys.modules
        if "frontier_cycle821_local_parity_exchange_carrier_recurrent_bell" in name
    ))

    checks = {
        "independent_import_firewall": not forbidden_imports,
        "landed_two_cell_rank_and_odd_census": (
            len(rows) == 23
            and gf2_rank(
                symplectic_vector(row, fixture.qubits) for row in rows
            ) == 23
            and odd == tuple(range(6)) + tuple(range(11, 17))
        ),
        "one_carrier_per_cell_two_copy_shared_carrier_executor": (
            common["carrier_M2_per_cell"] == 1
            and common["expected_output_rank"] == 46
            and common["output_rank_range"] == (46, 46)
            and common["carrier_state_binary_signed_or_rank_failures"] == 0
            and common["pump_resource"]["rank"] == 23
            and common["pump_resource"]["binary_failures"] == 0
            and common["pump_resource"]["signed_failures"] == 0
            and all(
                row["rank"] == 46
                and row["binary_failures"] == 0
                and row["signed_failures"] == 0
                for row in common["hostile_carrier_states"].values()
            )
        ),
        "two_copy_carrier_evolution_formula": (
            common["carrier_update_failures"] == 0
            and all(
                row["retained_syndrome_controls"] == 24
                for row in common["carrier_updates"]
            )
        ),
        "all_24_frames_and_arbitrary_carrier_states": (
            frame_report["proper_frames"] == 24
            and frame_report["frame_state_contexts"] == 384
            and frame_report["marginal_rank_range"] == (23, 23)
            and frame_report["binary_signed_or_rank_failures"] == 0
            and frame_report["mapped_private_duality_failures"] == 0
            and frame_report["mapped_correction_rank_failures"] == 0
            and frame_report["extended_correction_rank_failures"] == 0
            and frame_report["extended_parity_failures"] == 0
            and frame_report["odd_census_failures"] == 0
            and frame_report[
                "mapped_odd_rows_outside_transported_owner_cell"
            ] == 0
        ),
        "deletions_are_split_between_channel_and_parity_controls": (
            all(
                deletions[f"{stage}_{kind}"]["tested"] == 12
                and deletions[f"{stage}_{kind}"][
                    "minimum_output_failure"
                ] == 2
                and deletions[f"{stage}_{kind}"][
                    "maximum_output_failure"
                ] == 2
                for stage in ("pump", "bell")
                for kind in ("entire", "matter")
            )
            and all(
                deletions[f"{stage}_carrier"]["undetected_by_output"] == 12
                and deletions[f"{stage}_carrier"]["parity_detections"] == 12
                for stage in ("pump", "bell")
            )
        ),
        "U_dagger_CZ_U_pair_compiler_identity": (
            pair_compiler["pair_types_tested"] == 4
            and pair_compiler["maximum_identity_residual"] < 1.0e-12
            and pair_compiler["maximum_rotation_residual"] < 1.0e-12
            and pair_compiler[
                "maximum_elementary_gate_parity_commutator"
            ] < 1.0e-12
            and pair_compiler["maximum_prefix_parity_commutator"] < 1.0e-12
        ),
        "every_emitted_factor_and_prefix_is_parity_even": (
            compiler["corrections_compiled"] == 24 * 23
            and compiler["odd_letter_pairing_failures"] == 0
            and compiler["target_binary_reconstruction_failures"] == 0
            and compiler["target_signed_reconstruction_failures"] == 0
            and compiler["factor_parity_failures"] == 0
            and compiler["prefix_parity_failures"] == 0
        ),
        "literal_65_M2_schedule_on_base_and_held_box": all(
            row["total_M2_per_cell"] == 65
            and row["added_macros_per_cell"] == 12
            and row["carrier_palette_collisions"] == 0
            and row["carrier_G_collisions"] == 0
            and row["nearest_neighbour_failures"] == 0
            and row["returned_label_failures"] == 0
            and row["target_reconstruction_failures"] == 0
            and row["internal_live_carrier_or_G_hits"] == 0
            and row["same_block_microstep_collisions"] == 0
            and row["maximum_word_microsteps_after"]
            <= row["padded_microstep_bound"]
            and row["delete_reverse_SWAP_label_mismatches"] > 0
            for row in schedule["placements"]
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "artifact": "frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.py",
        "scope": (
            "independent bounded (2,1,1) one-carrier-per-cell parity-exchange "
            "dilation; parity-even observable channel; no fixed carrier state"
        ),
        "forbidden_primary_imports": forbidden_imports,
        "landed_fixture": {
            "shape": SHAPE,
            "cells": len(fixture.cells),
            "physical_M2_per_bank": fixture.qubits,
            "matter_modes": fixture.matter_qubits,
            "character_rank": len(rows),
            "odd_correction_indices": odd,
            "odd_corrections_per_cell": 6,
            "carrier_M2_per_cell": 1,
            "per_mode_carriers_required": False,
            "source_binary_rebuild_failures": (
                compiled["coarse_input_binary_replacement_failures"]
                + compiled["physical_tag_rebuild_failures"]
            ),
        },
        "two_copy_shared_carrier_executor": common,
        "frame_and_state_census": frame_report,
        "deletions": deletions,
        "parity_even_pair_compiler": pair_compiler,
        "emitted_compiler_census": compiler,
        "literal_schedule": schedule,
        "checks": checks,
        "supplied": [
            "one typed carrier M2 per coarse cell with local parity Z; its two-cell density matrix is arbitrary but initially factorized from the channel input",
            "the landed Cycle-720/789 fixture, private-dual atlas, clean definite pump and Bell syndrome stabilizer inputs, and L-R live/reference character resource; coherent syndrome/carrier inputs instead implement a controlled-X joint channel outside the scalar-r statement",
            "the proper-cubic frame/coframe chart, fixed stage order, finite boundary, and carrier site offset (3,-7,-4)",
        ],
        "derived": [
            "the exact rank-23 one-copy and rank-46 two-disjoint-copy shared-carrier O-R even-CAR marginals without a fixed carrier eigenstate; this is not an output-fed second epoch",
            "one carrier per cell shared by all six local odd rows; no per-mode carrier bank",
            "exact 24-frame by 16-carrier-state reconstruction, local support, private duality, and extended parity",
            "a parity-even abstract elementary compiler for every XX, XY, YX, and YY pair using U^dagger CZ U",
            "a collision-free 65-M2-per-cell returned-route schedule on (2,1,1) and held (6,5,4)",
        ],
        "open": [
            "nearest-neighbour/radius-one synthesis and routing of the two-target Pauli rotations U=exp(-i*pi*K/4)",
            "the non-Clifford recurrent Cycle-720 G in this same common state/tableau executor; only its landed parity-even, carrier-disjoint schedule firewall is imported",
            "parity-balanced carrier reset/renewal, carrier-bank genesis and typed separation, and fault rejection or repair",
            "channel gluing beyond the tested two-cell algebra and autonomous frame/epoch selection",
        ],
        "carrier_boundary": (
            "After each full epoch r_c is the xor of six pump and six Bell "
            "odd-row syndromes. X_c is invariant while Z_c and Y_c retain "
            "that syndrome parity. Across two disjoint channel copies, the carrier "
            "channel is the identity for every carrier input exactly when the "
            "cumulative local exchange parity is zero. For cumulative parity "
            "one, state-specific X-invariant inputs are still fixed."
        ),
        "physical_gate_boundary": (
            "Every emitted abstract gate and every cumulative prefix commutes "
            "with extended parity. This does not yet make U nearest-neighbour "
            "or radius one, and G is not executed in the same engine."
        ),
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
