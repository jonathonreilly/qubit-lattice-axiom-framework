#!/usr/bin/env python3
"""Cycle-821 bounded local parity-exchange carrier construction.

The landed Cycle-789 Bell/correction channel is exact on the even-CAR
observable algebra, but Cycle 820 showed that twelve of its twenty-three
private correction rows are odd with respect to physical matter parity.  This
runner attaches one local carrier mode to each coarse cell and replaces every
odd correction C by C X_carrier.  The extended
corrections are parity even.  No carrier value is queried or fixed.

The certificate is deliberately finite and conditional.  It proves an exact
two-epoch stabilizer/Heisenberg channel, a bounded cell/edge-local atomic gate
factorization, a fixed collision-free block schedule, and proper-cubic carrier
covariance.  It does not derive carrier genesis, the fixed schedule's
occurrence, total-parity superselection, or a translation-invariant law.
Circuit ordinals are not physical time.

The channel and carrier inputs are initially factorized and the syndrome
controls begin in the declared clean, definite stabilizer states. Coherent
syndrome/carrier inputs instead undergo the corresponding controlled-X joint
channel and are outside the scalar conditional-carrier statement.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
import json
import math
from pathlib import Path

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q720
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_cycle789_three_register_even_car_channel_2026_07_30 as C789
import frontier_cycle794_literal_prefix_recurrent_G_substitution_2026_07_30 as C794
import frontier_full128_cycle_encoder_2026_07_24 as F655
import frontier_full128_two_cell_even_car_frame_core_2026_07_30 as E820


AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_"
    "CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "docs/LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
    "scripts/frontier_companion_bank_even_exchange_port_2026_07_28.py",
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
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_genesis_broadcast_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_companion_three_route_independent_adversary_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py",
    "scripts/frontier_cycle789_two_bank_input_collision_discriminator_2026_07_30.py",
    "scripts/frontier_cycle794_actual_frame_shear_three_bank_schedule_2026_07_30.py",
    "scripts/frontier_cycle794_literal_prefix_recurrent_G_substitution_2026_07_30.py",
    "scripts/frontier_cycle794_literal_three_bank_prefix_core_2026_07_30.py",
    "scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_two_cell_even_car_frame_core_2026_07_30.py",
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
IMPORT_MODULES = (
    "frontier_companion_bank_bell_character_dilation_2026_07_28",
    "frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27",
    "frontier_cycle720_companion_subsystem_m2_update_2026_07_27",
    "frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30",
    "frontier_cycle789_three_register_even_car_channel_2026_07_30",
    "frontier_cycle794_literal_prefix_recurrent_G_substitution_2026_07_30",
    "frontier_full128_cycle_encoder_2026_07_24",
    "frontier_full128_two_cell_even_car_frame_core_2026_07_30",
)


Pauli = B.Pauli
Coord = tuple[int, int, int]
CARRIER_OFFSET: Coord = (3, -7, -4)


def fields(row: Pauli) -> tuple[int, int, int]:
    return B.fields(row)


def shift(row: Pauli, offset: int) -> Pauli:
    return Pauli(row.phase, row.x << offset, row.z << offset)


def product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = B.multiply(result, row)
    return result


def pair(row: Pauli, left: int, right: int) -> Pauli:
    return B.multiply(shift(row, left), shift(row, right))


def matter_parity(fixture) -> Pauli:
    return Pauli(z=(1 << fixture.matter_qubits) - 1)


def is_odd_correction(fixture, correction: Pauli) -> bool:
    q = fixture.qubits
    return bool(B.M.symplectic(
        correction.symplectic(q),
        matter_parity(fixture).symplectic(q),
        q,
    ))


def tag_owner(fixture, tag) -> int:
    if tag[0].startswith("onsite_"):
        return int(tag[1])
    if tag[0] == "edge":
        return int(fixture.edges[int(tag[1])][0])
    raise ValueError(tag)


def carrier_for_tag(fixture, tag, carrier_start: int) -> int:
    if tag[0] != "onsite_Z":
        raise AssertionError(("odd non-onsite correction", tag))
    cell = int(tag[1])
    return carrier_start + cell


def extend_correction(
    fixture,
    correction: Pauli,
    tag,
    bank_offset: int,
    carrier_start: int,
) -> tuple[Pauli, int | None]:
    output = shift(correction, bank_offset)
    if not is_odd_correction(fixture, correction):
        return output, None
    carrier = carrier_for_tag(fixture, tag, carrier_start)
    return B.multiply(output, Pauli(x=1 << carrier)), carrier


def layout(obj) -> dict[str, int]:
    q = int(obj["q"])
    rank = int(obj["rank"])
    cells = len(obj["fixture"].cells)
    carrier_start = 6 * q
    a1 = carrier_start + cells
    a2 = a1 + rank
    return {
        "O1": 0,
        "I1": q,
        "L": 2 * q,
        "R": 3 * q,
        "O2": 4 * q,
        "I2": 5 * q,
        "carrier": carrier_start,
        "A1": a1,
        "A2": a2,
        "width": a2 + rank,
    }


def global_physical_parity(obj, slots) -> Pauli:
    fixture = obj["fixture"]
    bits = 0
    # R is a diagnostic algebraic reference, not a physical prefix bank.
    for name in ("O1", "I1", "L", "O2", "I2"):
        bits |= ((1 << fixture.matter_qubits) - 1) << slots[name]
    bits |= ((1 << len(fixture.cells)) - 1) << slots["carrier"]
    return Pauli(z=bits)


def row_letter_product(row: Pauli) -> Pauli:
    return product(
        B.pauli_letter(qubit, B.letter_at(row, qubit))
        for qubit in B.supported_qubits(row)
    )


def make_epoch_gates(obj, slots, epoch: int, *, carrier_legs=True):
    if epoch == 1:
        bell_left, bell_right = slots["I1"], slots["L"]
        output = slots["O1"]
        ancilla_start = slots["A1"]
    elif epoch == 2:
        bell_left, bell_right = slots["I2"], slots["O1"]
        output = slots["O2"]
        ancilla_start = slots["A2"]
    else:
        raise ValueError(epoch)
    gates = []
    for index, (row, tag) in enumerate(zip(
        obj["rows"], obj["compiled"]["tags"]
    )):
        control = ancilla_start + index
        target = pair(row, bell_left, bell_right)
        gates.append(("H", control, tag, "measurement", index))
        gates.append(("CROW", control, target, tag, "measurement", index))
        gates.append(("H", control, tag, "measurement", index))
    for index, (correction, tag) in enumerate(zip(
        obj["corrections"], obj["compiled"]["tags"]
    )):
        control = ancilla_start + index
        target, carrier = extend_correction(
            obj["fixture"], correction, tag, output, slots["carrier"]
        )
        if not carrier_legs and carrier is not None:
            target = shift(correction, output)
        gates.append(("CROW", control, target, tag, "correction", index))
    return tuple(gates)


def conjugate_gate(row: Pauli, gate) -> Pauli:
    if gate[0] == "H":
        return B.conjugate_h(row, gate[1])
    if gate[0] == "CROW":
        output = row
        target = gate[2]
        if fields(row_letter_product(target)) != fields(target):
            raise AssertionError(("controlled-row phase is not letter exact", gate))
        for qubit in B.supported_qubits(target):
            output = B.conjugate_controlled_letter(
                output, gate[1], qubit, B.letter_at(target, qubit)
            )
        return output
    if gate[0] == "CP":
        return B.conjugate_controlled_letter(
            row, gate[1], gate[2], gate[3]
        )
    if gate[0] == "R":
        generator = gate[1]
        sign = int(gate[2])
        width = max(
            row.x.bit_length(), row.z.bit_length(),
            generator.x.bit_length(), generator.z.bit_length(),
        )
        if not B.M.symplectic(
            row.symplectic(width), generator.symplectic(width), width
        ):
            return row
        rotated = B.multiply(generator, row)
        # U_s=exp(-i s pi K/4): U_s Q U_s^dag=-i s KQ.
        phase = 3 if sign == 1 else 1
        return Pauli(
            (rotated.phase + phase) % 4, rotated.x, rotated.z
        )
    raise ValueError(gate)


def conjugate_basis(basis, gates) -> tuple[Pauli, ...]:
    output = tuple(basis)
    for gate in gates:
        output = tuple(conjugate_gate(row, gate) for row in output)
    return output


def initial_basis(obj, slots, carrier_axis: str | None = None):
    rows = tuple(obj["rows"])
    resource1 = tuple(pair(row, slots["O1"], slots["I1"]) for row in rows)
    live_reference = tuple(pair(row, slots["L"], slots["R"]) for row in rows)
    resource2 = tuple(pair(row, slots["O2"], slots["I2"]) for row in rows)
    ancillas = tuple(
        Pauli(z=1 << (slots[name] + index))
        for name in ("A1", "A2") for index in range(obj["rank"])
    )
    carriers = ()
    if carrier_axis is not None:
        carriers = tuple(
            B.pauli_letter(
                slots["carrier"] + index,
                carrier_axis,
            )
            for index in range(len(obj["fixture"].cells))
        )
    return resource1 + live_reference + resource2 + ancillas + carriers


def target_rows(obj, slots, output: str) -> tuple[Pauli, ...]:
    return tuple(pair(row, slots[output], slots["R"]) for row in obj["rows"])


def channel_failures(target, basis, width) -> tuple[int, int]:
    return C789.signed_span_failures(target, basis, width)


def parity_failures(gates, parity: Pauli, width: int) -> int:
    failures = 0
    for gate in gates:
        if gate[0] == "H":
            continue
        if gate[0] == "CROW":
            operator = gate[2]
        elif gate[0] == "CP":
            operator = B.pauli_letter(gate[2], gate[3])
        elif gate[0] == "R":
            operator = gate[1]
        else:
            raise ValueError(gate)
        failures += B.M.symplectic(
            operator.symplectic(width),
            parity.symplectic(width),
            width,
        )
    return failures


def atomize_target(row: Pauli, matter_sites: frozenset[int]):
    odd = tuple(
        qubit for qubit in B.supported_qubits(row)
        if qubit in matter_sites and ((row.x >> qubit) & 1)
    )
    if len(odd) % 2:
        raise AssertionError(("odd target", fields(row), odd))
    odd_set = set(odd)
    groups = [odd[index:index + 2] for index in range(0, len(odd), 2)]
    groups.extend(
        (qubit,) for qubit in B.supported_qubits(row) if qubit not in odd_set
    )
    factors = tuple(product(
        (B.pauli_letter(qubit, B.letter_at(row, qubit)) for qubit in group)
    ) for group in groups)
    return tuple(groups), factors


def pair_rotation_generator(
    first: int,
    first_letter: str,
    second: int,
    second_letter: str,
) -> Pauli:
    """K with exp(-i pi K/4) Z_first exp(+i pi K/4)=P1 P2."""
    if first_letter == "X":
        return product((
            B.pauli_letter(first, "Y"),
            B.pauli_letter(second, second_letter),
        ))
    if first_letter == "Y":
        row = product((
            B.pauli_letter(first, "X"),
            B.pauli_letter(second, second_letter),
        ))
        return Pauli((row.phase + 2) % 4, row.x, row.z)
    raise ValueError((first_letter, second_letter))


def compile_even_word(obj, slots, gates):
    """Compile every even controlled row into parity-even two-site gates.

    A paired fermionic target A=P_i P_j is compiled as
    U^dag, controlled-Z(control,i), U with
    U=exp(-i pi K/4) and U Z_i U^dag=A.  Singles already commute with the
    extended parity.  Every emitted tuple ends in (role,index).
    """
    fixture = obj["fixture"]
    matter = set()
    for name in ("O1", "I1", "L", "O2", "I2"):
        matter.update(range(
            slots[name], slots[name] + fixture.matter_qubits
        ))
    matter.update(range(
        slots["carrier"], slots["carrier"] + len(fixture.cells)
    ))
    output = []
    replay_failures = 0
    maximum_pair_weight = 0
    for gate in gates:
        if gate[0] == "H":
            output.append(gate)
            continue
        if gate[0] != "CROW":
            raise ValueError(gate)
        control, target, tag, role, index = gate[1:]
        groups, factors = atomize_target(target, frozenset(matter))
        replay_failures += fields(product(factors)) != fields(target)
        for group in groups:
            maximum_pair_weight = max(maximum_pair_weight, len(group))
            if len(group) == 1:
                qubit = group[0]
                output.append((
                    "CP", control, qubit, B.letter_at(target, qubit),
                    tag, role, index,
                ))
                continue
            first, second = group
            first_letter = B.letter_at(target, first)
            second_letter = B.letter_at(target, second)
            generator = pair_rotation_generator(
                first, first_letter, second, second_letter
            )
            output.extend((
                ("R", generator, -1, tag, role, index),
                ("CP", control, first, "Z", tag, role, index),
                ("R", generator, 1, tag, role, index),
            ))
    if replay_failures:
        raise AssertionError(("even-word replay", replay_failures))
    return tuple(output), maximum_pair_weight


def dense_even_pair_selftest() -> dict[str, object]:
    control, first, second, width = 0, 1, 2, 3
    identity = np.eye(1 << width, dtype=complex)
    residuals = []
    map_residuals = []
    parity_residuals = []
    parity = B.dense_pauli(Pauli(z=(1 << first) | (1 << second)), width)
    z_first = B.dense_pauli(Pauli(z=1 << first), width)
    for first_letter in ("X", "Y"):
        for second_letter in ("X", "Y"):
            target = product((
                B.pauli_letter(first, first_letter),
                B.pauli_letter(second, second_letter),
            ))
            generator = pair_rotation_generator(
                first, first_letter, second, second_letter
            )
            dense_k = B.dense_pauli(generator, width)
            u = (identity - 1j * dense_k) / np.sqrt(2)
            cz = B.dense_controlled_target(
                Pauli(z=1 << first), control, width
            )
            compiled = u @ cz @ u.conj().T
            desired = B.dense_controlled_target(target, control, width)
            residuals.append(float(np.linalg.norm(compiled - desired)))
            map_residuals.append(float(np.linalg.norm(
                u @ z_first @ u.conj().T - B.dense_pauli(target, width)
            )))
            for primitive in (u.conj().T, cz, u):
                parity_residuals.append(float(np.linalg.norm(
                    primitive @ parity - parity @ primitive
                )))
    return {
        "letter_pairs": 4,
        "maximum_compiled_controlled_pair_residual": max(residuals),
        "maximum_rotation_conjugacy_residual": max(map_residuals),
        "maximum_elementary_parity_commutator_residual": max(
            parity_residuals
        ),
    }


def abstract_qubit_cell(obj, slots, qubit: int) -> int | None:
    fixture = obj["fixture"]
    q = fixture.qubits
    for name in ("O1", "I1", "L", "R", "O2", "I2"):
        start = slots[name]
        if start <= qubit < start + q:
            local = qubit - start
            if local < fixture.matter_qubits:
                return local // 6
            return (local - fixture.matter_qubits) // 3
    start = slots["carrier"]
    if start <= qubit < start + len(fixture.cells):
        return qubit - start
    return None


def atom_certificate(obj, slots, gates):
    fixture = obj["fixture"]
    matter = set()
    for name in ("O1", "I1", "L", "O2", "I2"):
        matter.update(range(
            slots[name], slots[name] + fixture.matter_qubits
        ))
    matter.update(range(
        slots["carrier"], slots["carrier"] + len(fixture.cells)
    ))
    parity = global_physical_parity(obj, slots)
    atom_count = 0
    maximum_targets = 0
    maximum_cell_diameter = 0
    row_replay_failures = 0
    atom_parity_failures = 0
    for gate in gates:
        if gate[0] != "CROW":
            continue
        groups, factors = atomize_target(gate[2], frozenset(matter))
        atom_count += len(groups)
        maximum_targets = max(maximum_targets, *(len(group) for group in groups))
        row_replay_failures += fields(product(factors)) != fields(gate[2])
        for group, factor in zip(groups, factors):
            atom_parity_failures += B.M.symplectic(
                factor.symplectic(slots["width"]),
                parity.symplectic(slots["width"]),
                slots["width"],
            )
            cells = [
                abstract_qubit_cell(obj, slots, qubit) for qubit in group
            ]
            cells = [cell for cell in cells if cell is not None]
            if cells:
                coords = [fixture.cells[cell] for cell in cells]
                maximum_cell_diameter = max(
                    maximum_cell_diameter,
                    max((sum(abs(a - b) for a, b in zip(left, right))
                         for left in coords for right in coords), default=0),
                )
    return {
        "controlled_composites": sum(gate[0] == "CROW" for gate in gates),
        "parity_even_atoms": atom_count,
        "maximum_atom_targets_excluding_control": maximum_targets,
        "maximum_atom_cell_diameter": maximum_cell_diameter,
        "controlled_row_letter_replay_failures": row_replay_failures,
        "atom_parity_commutator_failures": atom_parity_failures,
    }


def two_epoch_certificate(shape, atlas, *, deletion_controls=False):
    obj = C789.circuit_objects(shape, atlas)
    slots = layout(obj)
    initial = initial_basis(obj, slots)
    semantic_epoch1 = make_epoch_gates(obj, slots, 1)
    semantic_epoch2 = make_epoch_gates(obj, slots, 2)
    epoch1, max_targets1 = compile_even_word(
        obj, slots, semantic_epoch1
    )
    epoch2, max_targets2 = compile_even_word(
        obj, slots, semantic_epoch2
    )
    after1 = conjugate_basis(initial, epoch1)
    after2 = conjugate_basis(after1, epoch2)
    intermediate = channel_failures(
        target_rows(obj, slots, "O1"), after1, slots["width"]
    )
    final = channel_failures(
        target_rows(obj, slots, "O2"), after2, slots["width"]
    )
    carrier_axis_failures = {}
    for axis in ("X", "Y", "Z"):
        basis = initial_basis(obj, slots, axis)
        candidate = conjugate_basis(
            conjugate_basis(basis, epoch1), epoch2
        )
        carrier_axis_failures[axis] = channel_failures(
            target_rows(obj, slots, "O2"), candidate, slots["width"]
        )

    parity = global_physical_parity(obj, slots)
    unextended_semantic = make_epoch_gates(
        obj, slots, 2, carrier_legs=False
    )
    unextended = unextended_semantic
    unextended_after2 = conjugate_basis(after1, unextended)
    unextended_channel = channel_failures(
        target_rows(obj, slots, "O2"),
        unextended_after2,
        slots["width"],
    )
    unextended_parity = parity_failures(
        unextended, parity, slots["width"]
    )

    carrier_count = len(obj["fixture"].cells)
    z_rows = tuple(
        Pauli(z=1 << (slots["carrier"] + index))
        for index in range(carrier_count)
    )
    x_rows = tuple(
        Pauli(x=1 << (slots["carrier"] + index))
        for index in range(carrier_count)
    )
    carrier_z_return_failures = sum(
        fields(conjugate_gate_sequence(row, epoch1 + epoch2)) != fields(row)
        for row in z_rows
    )
    carrier_x_return_failures = sum(
        fields(conjugate_gate_sequence(row, epoch1 + epoch2)) != fields(row)
        for row in x_rows
    )

    deletions = []
    if deletion_controls:
        for deleted in range(obj["rank"]):
            damaged = tuple(
                gate for gate in epoch2
                if not (
                    gate[-2] == "correction"
                    and gate[-1] == deleted
                )
            )
            damaged_final = conjugate_basis(after1, damaged)
            deletions.append(channel_failures(
                target_rows(obj, slots, "O2"),
                damaged_final,
                slots["width"],
            ))

    atoms = atom_certificate(
        obj, slots, semantic_epoch1 + semantic_epoch2
    )
    return {
        "shape": shape,
        "cells": len(obj["fixture"].cells),
        "rank": obj["rank"],
        "physical_M2_per_companion_bank": obj["q"],
        "carrier_modes": carrier_count,
        "carrier_modes_per_cell": 1,
        "parity_odd_corrections_per_epoch": sum(
            is_odd_correction(obj["fixture"], correction)
            for correction in obj["corrections"]
        ),
        "intermediate_binary_signed_failures": intermediate,
        "two_epoch_binary_signed_failures": final,
        "hostile_carrier_axis_binary_signed_failures": carrier_axis_failures,
        "extended_gate_parity_commutator_failures": parity_failures(
            epoch1 + epoch2, parity, slots["width"]
        ),
        "compiled_elementary_gates": len(epoch1) + len(epoch2),
        "maximum_compiled_atom_targets": max(max_targets1, max_targets2),
        "unextended_second_epoch_channel_binary_signed_failures": (
            unextended_channel
        ),
        "unextended_second_epoch_parity_commutator_failures": (
            unextended_parity
        ),
        "carrier_Z_rows_not_returned_after_two_epochs": (
            carrier_z_return_failures
        ),
        "carrier_X_rows_not_returned_after_two_epochs": (
            carrier_x_return_failures
        ),
        "deleted_second_epoch_corrections_tested": len(deletions),
        "deleted_second_epoch_corrections_detected": sum(
            binary + signed > 0 for binary, signed in deletions
        ),
        "minimum_deleted_correction_failures": min(
            (binary + signed for binary, signed in deletions), default=0
        ),
        "atomic_factorization": atoms,
    }


def full_layout(obj) -> dict[str, int]:
    q = int(obj["q"])
    rank = int(obj["rank"])
    cells = len(obj["fixture"].cells)
    carrier = 6 * q
    p1 = carrier + cells
    b1 = p1 + rank
    p2 = b1 + rank
    b2 = p2 + rank
    return {
        "O1": 0, "I1": q, "L": 2 * q, "R": 3 * q,
        "O2": 4 * q, "I2": 5 * q,
        "carrier": carrier,
        "P1": p1, "B1": b1, "P2": p2, "B2": b2,
        "width": b2 + rank,
    }


def make_measure_correct_block(
    obj,
    slots,
    left: int,
    right: int,
    output: int,
    ancilla_start: int,
    stage: str,
):
    gates = []
    for index, (row, tag) in enumerate(zip(
        obj["rows"], obj["compiled"]["tags"]
    )):
        control = ancilla_start + index
        target = pair(row, left, right)
        gates.extend((
            ("H", control, tag, stage + "_measurement", index),
            ("CROW", control, target, tag, stage + "_measurement", index),
            ("H", control, tag, stage + "_measurement", index),
        ))
    for index, (correction, tag) in enumerate(zip(
        obj["corrections"], obj["compiled"]["tags"]
    )):
        target, _carrier = extend_correction(
            obj["fixture"], correction, tag, output, slots["carrier"]
        )
        gates.append((
            "CROW", ancilla_start + index, target, tag,
            stage + "_correction", index,
        ))
    return tuple(gates)


def full_initial_basis(obj, slots, carrier_axis: str | None = None):
    rows = tuple(obj["rows"])
    live_reference = tuple(
        pair(row, slots["L"], slots["R"]) for row in rows
    )
    ancillas = tuple(
        Pauli(z=1 << (slots[name] + index))
        for name in ("P1", "B1", "P2", "B2")
        for index in range(obj["rank"])
    )
    carriers = ()
    if carrier_axis is not None:
        carriers = tuple(
            B.pauli_letter(slots["carrier"] + index, carrier_axis)
            for index in range(len(obj["fixture"].cells))
        )
    return live_reference + ancillas + carriers


def full_executor_certificate(shape, atlas):
    """Execute pump, Bell and correction twice with one shared carrier/cell."""
    obj = C789.circuit_objects(shape, atlas)
    slots = full_layout(obj)
    pump1_semantic = make_measure_correct_block(
        obj, slots, slots["O1"], slots["I1"], slots["O1"],
        slots["P1"], "pump1",
    )
    bell1_semantic = make_measure_correct_block(
        obj, slots, slots["I1"], slots["L"], slots["O1"],
        slots["B1"], "bell1",
    )
    pump2_semantic = make_measure_correct_block(
        obj, slots, slots["O2"], slots["I2"], slots["O2"],
        slots["P2"], "pump2",
    )
    bell2_semantic = make_measure_correct_block(
        obj, slots, slots["I2"], slots["O1"], slots["O2"],
        slots["B2"], "bell2",
    )
    pump1, _ = compile_even_word(obj, slots, pump1_semantic)
    bell1, _ = compile_even_word(obj, slots, bell1_semantic)
    pump2, _ = compile_even_word(obj, slots, pump2_semantic)
    bell2, _ = compile_even_word(obj, slots, bell2_semantic)
    initial = full_initial_basis(obj, slots)
    after_pump1 = conjugate_basis(initial, pump1)
    resource1 = tuple(
        pair(row, slots["O1"], slots["I1"]) for row in obj["rows"]
    )
    pump1_failures = channel_failures(
        resource1, after_pump1, slots["width"]
    )
    after_bell1 = conjugate_basis(after_pump1, bell1)
    output1 = channel_failures(
        target_rows(obj, slots, "O1"), after_bell1, slots["width"]
    )
    after_pump2 = conjugate_basis(after_bell1, pump2)
    resource2 = tuple(
        pair(row, slots["O2"], slots["I2"]) for row in obj["rows"]
    )
    pump2_failures = channel_failures(
        resource2, after_pump2, slots["width"]
    )
    final_basis = conjugate_basis(after_pump2, bell2)
    output2 = channel_failures(
        target_rows(obj, slots, "O2"), final_basis, slots["width"]
    )
    dirty_axes = {}
    word = pump1 + bell1 + pump2 + bell2
    for axis in ("X", "Y", "Z"):
        candidate = conjugate_basis(
            full_initial_basis(obj, slots, axis), word
        )
        dirty_axes[axis] = channel_failures(
            target_rows(obj, slots, "O2"), candidate, slots["width"]
        )
    parity = global_physical_parity(obj, slots)
    return {
        "shape": shape,
        "cells": len(obj["fixture"].cells),
        "rank": obj["rank"],
        "initial_system_stabilizers_on_OI_resources": 0,
        "pump1_resource_binary_signed_failures": pump1_failures,
        "first_complete_epoch_binary_signed_failures": output1,
        "pump2_resource_binary_signed_failures": pump2_failures,
        "second_complete_epoch_binary_signed_failures": output2,
        "dirty_carrier_axis_binary_signed_failures": dirty_axes,
        "elementary_gate_count": len(word),
        "elementary_parity_commutator_failures": parity_failures(
            word, parity, slots["width"]
        ),
        "carrier_Z_rows_not_returned": sum(
            fields(conjugate_gate_sequence(
                Pauli(z=1 << (slots["carrier"] + index)), word
            )) != fields(Pauli(z=1 << (slots["carrier"] + index)))
            for index in range(len(obj["fixture"].cells))
        ),
    }


def conjugate_gate_sequence(row: Pauli, gates) -> Pauli:
    output = row
    for gate in gates:
        output = conjugate_gate(output, gate)
    return output


def carrier_sites(fixture, centers) -> tuple[Coord, ...]:
    return tuple(
        S789.add(centers[cell], CARRIER_OFFSET)
        for cell in fixture.cells
    )


def schedule_certificate(shape, atlas):
    report, scratch = S789.box_certificate(shape, atlas)
    fixture = scratch["fixture"]
    obj = C789.circuit_objects(shape, atlas)
    carriers = carrier_sites(fixture, scratch["centers"])
    existing = set().union(*scratch["classes"].values())
    all_paths = {
        point for macro in scratch["macros"] for point in macro.path
    }
    placed = S789.U.placement(fixture)
    g_word, _ = S789.U.physical_word(fixture, placed)
    routed_g, _ = S789.U.c707.route_word(g_word)
    g_sites = {tuple(site) for gate in routed_g for site in gate.sites}
    carrier_set = set(carriers)
    labels = {site: site for site in (g_sites | carrier_set)}
    g_carrier_active_gate_hits = 0
    for gate in routed_g:
        sites = tuple(tuple(site) for site in gate.sites)
        if gate.kind == "route_swap":
            left, right = sites
            labels[left], labels[right] = labels[right], labels[left]
        else:
            g_carrier_active_gate_hits += sum(
                labels[site] in carrier_set for site in sites
            )
    g_carrier_return_failures = sum(
        labels[site] != site for site in carrier_set
    )

    # Every odd correction has one geometrically adjacent outward carrier.
    pair_geometry_failures = 0
    pair_gate_diameters = []
    odd_macro_count = 0
    for word in scratch["words"]:
        if word["stage"] not in ("pump", "bell_correction"):
            continue
        tag = word["tag"]
        if tag[0] != "onsite_Z":
            continue
        x_macros = tuple(
            macro for macro in word["macros"]
            if macro.role == "correction" and macro.letter == "X"
        )
        if len(x_macros) != 1:
            pair_geometry_failures += 1
            continue
        macro = x_macros[0]
        carrier = carriers[int(tag[1])]
        sites = (macro.path[-2], macro.target, carrier)
        distances = tuple(
            S789.manhattan(left, right) for left in sites for right in sites
        )
        pair_gate_diameters.append(max(distances))
        pair_geometry_failures += S789.manhattan(macro.path[-2], macro.target) != 1
        pair_geometry_failures += tag_owner(fixture, tag) != int(tag[1])
        odd_macro_count += 1

    # The fixed colour/slot schedule serializes the one shared carrier in a cell.
    # Same-block words have distinct owners, so adding the owner-local carrier
    # at the correction ordinal cannot create a new shared-site collision.
    grouped = defaultdict(list)
    for word in scratch["words"]:
        grouped[(word["stage"], word["colour"], word["slot"])].append(word)
    carrier_block_collisions = 0
    for words in grouped.values():
        occupied = set()
        for word in words:
            if word["stage"] not in ("pump", "bell_correction"):
                continue
            tag = word["tag"]
            if tag[0] != "onsite_Z":
                continue
            site = carriers[int(tag[1])]
            carrier_block_collisions += site in occupied
            occupied.add(site)

    # Replace the routed single-letter controlled gates by literal bounded
    # atoms.  Odd fermionic letters are paired inside each cell/edge support;
    # odd corrections are paired with the matching outward carrier.  The
    # inherited colour/slot blocks are retained, but this is a bounded-range
    # atom schedule, not a nearest-neighbour synthesis of those atoms.
    q = fixture.qubits
    n = len(fixture.cells)
    o_sites = tuple(S789.U.placement(fixture)["sites_by_qubit"])
    i_sites = S789.bank_sites(
        fixture, scratch["centers"], 1, S789.I_PAIRS
    )
    l_sites = S789.bank_sites(
        fixture, scratch["centers"], 2, S789.L_PAIRS
    )
    abstract_carrier_start = 3 * q
    matter_sites = frozenset(
        tuple(range(fixture.matter_qubits))
        + tuple(range(q, q + fixture.matter_qubits))
        + tuple(range(2 * q, 2 * q + fixture.matter_qubits))
        + tuple(range(abstract_carrier_start, abstract_carrier_start + n))
    )

    def physical_site(qubit: int) -> Coord:
        if qubit < q:
            return o_sites[qubit]
        if qubit < 2 * q:
            return i_sites[qubit - q]
        if qubit < 3 * q:
            return l_sites[qubit - 2 * q]
        if qubit < abstract_carrier_start + n:
            return carriers[qubit - abstract_carrier_start]
        raise ValueError(qubit)

    tag_to_index = {
        tuple(tag): index for index, tag in enumerate(obj["compiled"]["tags"])
    }
    atomic_words = []
    atom_replay_failures = 0
    atom_count = 0
    atom_max_targets = 0
    atom_max_m2_diameter = 0
    for word in scratch["words"]:
        index = tag_to_index[tuple(word["tag"])]
        if word["stage"] == "pump":
            targets = [obj["compiled"]["words"][index]["row"]]
            correction, _ = extend_correction(
                fixture,
                obj["corrections"][index],
                word["tag"],
                0,
                abstract_carrier_start,
            )
            targets.append(correction)
            include_h = True
        elif word["stage"] == "bell_measure":
            targets = [obj["bell_rows"][index]]
            include_h = True
        elif word["stage"] == "bell_correction":
            correction, _ = extend_correction(
                fixture,
                obj["corrections"][index],
                word["tag"],
                0,
                abstract_carrier_start,
            )
            targets = [correction]
            include_h = False
        else:
            raise ValueError(word["stage"])
        primitives = []
        if include_h:
            primitives.append(("H", (word["ancilla"],)))
        for target_index, target in enumerate(targets):
            groups, factors = atomize_target(target, matter_sites)
            atom_replay_failures += fields(product(factors)) != fields(target)
            for group in groups:
                sites = (word["ancilla"],) + tuple(
                    physical_site(qubit) for qubit in group
                )
                primitives.append((f"ATOM_{target_index}", sites))
                atom_count += 1
                atom_max_targets = max(atom_max_targets, len(group))
                atom_max_m2_diameter = max(
                    atom_max_m2_diameter,
                    max((S789.manhattan(left, right)
                         for left in sites for right in sites), default=0),
                )
            if include_h and target_index == 0:
                primitives.append(("H", (word["ancilla"],)))
        atomic_words.append((word, tuple(primitives)))

    atomic_grouped = defaultdict(list)
    for word, primitives in atomic_words:
        atomic_grouped[
            (word["stage"], word["colour"], word["slot"])
        ].append(primitives)
    atomic_same_block_collisions = 0
    atomic_microsteps = 0
    for rows in atomic_grouped.values():
        for ordinal in range(max(len(row) for row in rows)):
            occupied = set()
            for row in rows:
                if ordinal >= len(row):
                    continue
                sites = row[ordinal][1]
                atomic_same_block_collisions += bool(
                    occupied.intersection(sites)
                )
                occupied.update(sites)
            atomic_microsteps += 1

    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "baseline_M2_per_cell": report[
            "total_explicit_M2_per_cell_including_retained_syndromes"
        ],
        "carrier_M2_per_cell": 1,
        "extended_M2_per_cell": report[
            "total_explicit_M2_per_cell_including_retained_syndromes"
        ] + 1,
        "carrier_site_count": len(carriers),
        "carrier_site_uniqueness_failures": len(carriers) - len(set(carriers)),
        "carrier_palette_collisions": len(set(carriers) & existing),
        "carrier_hits_existing_returned_routes": len(set(carriers) & all_paths),
        "carrier_hits_recurrent_G_routes": len(set(carriers) & g_sites),
        "routed_G_active_gate_carrier_label_hits": (
            g_carrier_active_gate_hits
        ),
        "routed_G_carrier_label_return_failures": (
            g_carrier_return_failures
        ),
        "odd_pump_and_Bell_correction_pair_macros": odd_macro_count,
        "local_pair_gate_geometry_failures": pair_geometry_failures,
        "maximum_pair_gate_M2_manhattan_diameter": max(
            pair_gate_diameters, default=0
        ),
        "same_colour_slot_carrier_collisions": carrier_block_collisions,
        "bounded_atomic_gate_count": atom_count,
        "bounded_atomic_maximum_targets_excluding_control": atom_max_targets,
        "bounded_atomic_maximum_M2_manhattan_diameter": (
            atom_max_m2_diameter
        ),
        "bounded_atomic_row_replay_failures": atom_replay_failures,
        "bounded_atomic_same_block_collisions": (
            atomic_same_block_collisions
        ),
        "bounded_atomic_active_microsteps": atomic_microsteps,
        "inherited_schedule_collisions": report["same_block_microstep_collisions"],
        "inherited_returned_label_failures": report["returned_label_failures"],
        "inherited_G_sites_outside_O": report["G_sites_outside_O"],
    }


def carrier_covariance_certificate(atlas):
    frames = tuple(F655.FRAMES)
    base_cells = tuple(sorted(((0, 0, 0), (1, 0, 0))))
    frame_key = {E820.frame_key(frame): index for index, frame in enumerate(frames)}
    _report, scratch = S789.box_certificate((2, 1, 1), atlas)
    fixture = scratch["fixture"]
    centers = scratch["centers"]
    carriers = carrier_sites(fixture, centers)
    existing = tuple(sorted(set().union(*scratch["classes"].values())))
    contexts = 0
    carrier_rows = 0
    frame_failures = 0
    product_failures = 0
    origin_failures = 0
    physical_offset_failures = 0
    physical_collision_failures = 0
    physical_distance_failures = 0
    physical_product_failures = 0
    fixed_lab_offset_mutation_detections = 0

    def permutation(source_cells, frame):
        target_cells = Q720.affine_cells(source_cells, frame, E820.ZERO)
        index = {cell: item for item, cell in enumerate(target_cells)}
        cell_map = tuple(index[tuple(int(value) for value in (
            frame @ np.asarray(cell, dtype=int)
        ))] for cell in source_cells)
        return cell_map, target_cells

    direct = {}
    for frame_id, frame in enumerate(frames):
        mapping, target = permutation(base_cells, frame)
        direct[frame_id] = (mapping, target)
        contexts += len(E820.ORIGIN_SECTORS)
        carrier_rows += len(mapping) * len(E820.ORIGIN_SECTORS)
        frame_failures += len(set(mapping)) != len(mapping)
        frame_tuple = tuple(
            tuple(int(value) for value in row) for row in frame
        )
        rotated_offset = S789.matvec(frame_tuple, CARRIER_OFFSET)
        fixed_lab_offset_mutation_detections += (
            rotated_offset != CARRIER_OFFSET
        )
        for cell, carrier in zip(fixture.cells, carriers):
            mapped_center = S789.matvec(frame_tuple, centers[cell])
            mapped_carrier = S789.matvec(frame_tuple, carrier)
            physical_offset_failures += tuple(
                right - left
                for left, right in zip(mapped_center, mapped_carrier)
            ) != rotated_offset
        base_distance_rows = tuple(
            tuple(S789.manhattan(carrier, site) for site in existing)
            for carrier in carriers
        )
        for origin in E820.ORIGIN_SECTORS:
            mapped_existing = {
                S789.transform(site, frame_tuple, origin)
                for site in existing
            }
            mapped_carriers = tuple(
                S789.transform(site, frame_tuple, origin)
                for site in carriers
            )
            physical_collision_failures += len(mapped_carriers) != len(
                set(mapped_carriers)
            )
            physical_collision_failures += bool(
                set(mapped_carriers) & mapped_existing
            )
            for carrier_index, mapped_carrier in enumerate(mapped_carriers):
                mapped_distances = tuple(
                    S789.manhattan(mapped_carrier, mapped_site)
                    for mapped_site in (
                        S789.transform(site, frame_tuple, origin)
                        for site in existing
                    )
                )
                physical_distance_failures += (
                    mapped_distances != base_distance_rows[carrier_index]
                )

    for left_id, left in enumerate(frames):
        for right_id, right in enumerate(frames):
            product_frame = left @ right
            product_id = frame_key[E820.frame_key(product_frame)]
            right_map, middle_cells = direct[right_id]
            left_map, _final_cells = permutation(middle_cells, left)
            composed = tuple(
                left_map[right_map[index]] for index in range(2)
            )
            product_failures += composed != direct[product_id][0]
            for seed in E820.ORIGIN_SECTORS:
                middle_seed = Q720.transported_seed(right, E820.ZERO, seed)
                final_seed = Q720.transported_seed(left, E820.ZERO, middle_seed)
                direct_seed = Q720.transported_seed(
                    product_frame, E820.ZERO, seed
                )
                origin_failures += final_seed != direct_seed
            left_tuple = tuple(
                tuple(int(value) for value in row) for row in left
            )
            right_tuple = tuple(
                tuple(int(value) for value in row) for row in right
            )
            product_tuple = tuple(
                tuple(int(value) for value in row) for row in product_frame
            )
            physical_product_failures += (
                S789.matvec(
                    left_tuple,
                    S789.matvec(right_tuple, CARRIER_OFFSET),
                ) != S789.matvec(product_tuple, CARRIER_OFFSET)
            )
    return {
        "proper_cubic_frames": len(frames),
        "frame_origin_contexts": contexts,
        "carrier_slot_comparisons": carrier_rows,
        "ordered_frame_products": len(frames) ** 2,
        "frame_carrier_permutation_failures": frame_failures,
        "product_carrier_cocycle_failures": product_failures,
        "origin_product_failures": origin_failures,
        "coframe_transported_physical_offset_failures": (
            physical_offset_failures
        ),
        "frame_origin_physical_carrier_palette_failures": (
            physical_collision_failures
        ),
        "frame_origin_physical_distance_failures": (
            physical_distance_failures
        ),
        "physical_offset_product_failures": physical_product_failures,
        "fixed_laboratory_offset_mutation_detected_frames": int(
            fixed_lab_offset_mutation_detections
        ),
        "identity_frame_carrier_offset": CARRIER_OFFSET,
        "physical_covariance_boundary": (
            "the identity-frame carrier offset is transported by the "
            "supplied coframe; it is not held fixed in laboratory "
            "coordinates under an active cubic rotation"
        ),
    }


def recurrent_G_even_factor_certificate(shape):
    """Replace parity-odd seam synthesis prefixes by their even factors.

    Coin, reverse-FSWAP and contact instructions are already parity preserving.
    Each seam semantic factor is one exact exp(-i pi P/4) for a bounded
    parity-even physical Pauli P.  The older H/CNOT/RZ synthesis is retained
    only as an equality witness and hostile prefix control.
    """
    fixture = S789.fixture_for(shape)
    placed = U720.placement(fixture)
    word, update = U720.physical_word(fixture, placed)
    all_sites = tuple(placed["all_sites"])
    site_index = {site: index for index, site in enumerate(all_sites)}
    matter_sites = set(placed["sites_by_qubit"][:fixture.matter_qubits])
    matter_z = sum(1 << site_index[site] for site in matter_sites)
    matter_parity_row = U720.c707.Pauli(0, 0, matter_z)
    rng = np.random.default_rng(821000 + len(fixture.cells))
    seam_rows = 0
    seam_parity_failures = 0
    seam_direct_compiled_residuals = []
    seam_support_weights = []
    seam_support_diameters = []
    compiled_seam_elementary_parity_failures = 0
    for edge in range(len(fixture.edges)):
        for row in fixture.physical_terms(edge):
            seam_rows += 1
            lifted = U720.lift_pauli(row, placed)
            seam_parity_failures += not lifted.commutes(matter_parity_row)
            support = tuple(
                site for index, site in enumerate(all_sites)
                if ((lifted.x | lifted.z) >> index) & 1
            )
            local = U720.P709.restrict_pauli(lifted, all_sites, support)
            state = rng.normal(size=1 << len(support)) + 1j * rng.normal(
                size=1 << len(support)
            )
            state /= np.linalg.norm(state)
            compiled_word = U720.c707.compile_pauli_rotation(
                lifted, all_sites, math.pi / 2
            )
            compiled = U720.P709.execute_word(
                state, compiled_word, support
            )
            direct = U720.c707.direct_rotation(
                state, local, math.pi / 2, len(support)
            )
            seam_direct_compiled_residuals.append(
                U720.P709.phase_aligned_residual(compiled, direct)
            )
            seam_support_weights.append(len(support))
            seam_support_diameters.append(max((
                S789.manhattan(left, right)
                for left in support for right in support
            ), default=0))
            for instruction in compiled_word:
                local_matter = tuple(
                    site for site in instruction.sites if site in matter_sites
                )
                parity = np.diag(tuple(
                    (-1) ** sum(
                        (state >> instruction.sites.index(site)) & 1
                        for site in local_matter
                    )
                    for state in range(1 << len(instruction.sites))
                )).astype(complex)
                compiled_seam_elementary_parity_failures += (
                    np.linalg.norm(
                        instruction.matrix @ parity
                        - parity @ instruction.matrix
                    ) > 1.0e-12
                )

    # Independently recompute parity of every non-seam primitive in the
    # submitted physical word.  Seam primitives are replaced at their factor
    # boundary above.
    onsite_parity_residuals = []
    for instruction in word:
        if instruction.kind.startswith("seam_"):
            continue
        local_matter = tuple(
            site for site in instruction.sites if site in matter_sites
        )
        parity = np.diag(tuple(
            (-1) ** sum(
                (state >> instruction.sites.index(site)) & 1
                for site in local_matter
            )
            for state in range(1 << len(instruction.sites))
        )).astype(complex)
        onsite_parity_residuals.append(float(np.linalg.norm(
            instruction.matrix @ parity - parity @ instruction.matrix
        )))
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "semantic_factors": update["logical_update_factors"],
        "submitted_physical_primitives": update["physical_primitives"],
        "direct_even_seam_factors": seam_rows,
        "direct_even_seam_parity_failures": seam_parity_failures,
        "maximum_sampled_phase_aligned_seam_state_residual": max(
            seam_direct_compiled_residuals, default=0.0
        ),
        "maximum_direct_seam_support_M2": max(
            seam_support_weights, default=0
        ),
        "maximum_direct_seam_M2_manhattan_diameter": max(
            seam_support_diameters, default=0
        ),
        "submitted_seam_elementary_parity_failures": (
            int(compiled_seam_elementary_parity_failures)
        ),
        "maximum_nonseam_elementary_parity_residual": max(
            onsite_parity_residuals, default=0.0
        ),
        "direct_factor_program_parity_failures": (
            seam_parity_failures
            + sum(value > 1.0e-12 for value in onsite_parity_residuals)
        ),
        "one_particle_mass_residual": U720.C.R.local_free_contact_mass()[
            "mass_contact"
        ]["one_particle_mass_residual"],
    }


def composed_recurrent_substitution_certificate(atlas):
    """Join the new exact prepared prefix to landed factorwise recurrent G."""
    boxes = tuple(
        C794.box_certificate(shape, atlas, powers=powers)
        for shape, powers in (
            ((2, 1, 1), (1, 2, 3, 5, 8)),
            ((3, 1, 1), (1, 2, 3)),
        )
    )
    factors = tuple(
        recurrent_G_even_factor_certificate(shape)
        for shape in ((2, 1, 1), (3, 1, 1), (3, 2, 2))
    )
    return {
        "boxes": tuple({
            "shape": row["shape"],
            "postcomposition_substitution_failures": row[
                "substitution"
            ]["postcomposition_substitution_failures"],
            "shared_output_register_exact": row["substitution"][
                "shared_output_register_exact"
            ],
            "one_particle_mass_residual": row["recurrent"][
                "one_particle_mass_residual"
            ],
            "free_seam_contact_recurrent_powers": tuple(
                item["physical_update_power"]
                for item in row["recurrent"]["recurrent_powers"]
            ),
        } for row in boxes),
        "parity_audited_G_factors": factors,
        "composition_rule": (
            "the new pump/Bell/correction executor reproduces the complete "
            "rank-(2m-1) signed Choi graph on the identical O sites; Cycle794 "
            "proves linear postcomposition by recurrent G; replacing each "
            "submitted seam synthesis by its exact direct even factor leaves "
            "G unchanged and makes every declared factor parity preserving"
        ),
    }


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    atlas = B.P.build_private_atlases()
    dense_pairs = dense_even_pair_selftest()
    two_cell = two_epoch_certificate(
        (2, 1, 1), atlas, deletion_controls=True
    )
    held = two_epoch_certificate((3, 2, 2), atlas)
    full_two_cell = full_executor_certificate((2, 1, 1), atlas)
    full_held = full_executor_certificate((3, 2, 2), atlas)
    schedules = tuple(
        schedule_certificate(shape, atlas)
        for shape in ((2, 1, 1), (3, 2, 2), (5, 3, 2))
    )
    covariance = carrier_covariance_certificate(atlas)
    recurrent = composed_recurrent_substitution_certificate(atlas)
    checks = {
        "two_consecutive_epochs_share_dirty_carriers_and_close": (
            two_cell["intermediate_binary_signed_failures"] == (0, 0)
            and two_cell["two_epoch_binary_signed_failures"] == (0, 0)
            and held["two_epoch_binary_signed_failures"] == (0, 0)
            and all(
                tuple(value) == (0, 0)
                for box in (two_cell, held)
                for value in box[
                    "hostile_carrier_axis_binary_signed_failures"
                ].values()
            )
        ),
        "pump_Bell_and_correction_execute_in_one_parity_even_word": (
            all(
                box["pump1_resource_binary_signed_failures"] == (0, 0)
                and box["first_complete_epoch_binary_signed_failures"]
                    == (0, 0)
                and box["pump2_resource_binary_signed_failures"] == (0, 0)
                and box["second_complete_epoch_binary_signed_failures"]
                    == (0, 0)
                and box["elementary_parity_commutator_failures"] == 0
                and box["carrier_Z_rows_not_returned"] == box["cells"]
                and all(
                    tuple(value) == (0, 0)
                    for value in box[
                        "dirty_carrier_axis_binary_signed_failures"
                    ].values()
                )
                for box in (full_two_cell, full_held)
            )
        ),
        "all_extended_measurement_and_correction_atoms_are_parity_even": (
            dense_pairs["maximum_compiled_controlled_pair_residual"] < 1.0e-12
            and dense_pairs["maximum_rotation_conjugacy_residual"] < 1.0e-12
            and dense_pairs[
                "maximum_elementary_parity_commutator_residual"
            ] < 1.0e-12
            and two_cell["extended_gate_parity_commutator_failures"] == 0
            and held["extended_gate_parity_commutator_failures"] == 0
            and two_cell["atomic_factorization"][
                "controlled_row_letter_replay_failures"
            ] == 0
            and two_cell["atomic_factorization"][
                "atom_parity_commutator_failures"
            ] == 0
            and held["atomic_factorization"][
                "atom_parity_commutator_failures"
            ] == 0
            and held["atomic_factorization"][
                "maximum_atom_cell_diameter"
            ] <= 1
        ),
        "carrier_is_reusable_without_being_falsely_called_reset": (
            two_cell["carrier_Z_rows_not_returned_after_two_epochs"]
                == two_cell["carrier_modes"]
            and two_cell["carrier_X_rows_not_returned_after_two_epochs"] == 0
            and held["carrier_Z_rows_not_returned_after_two_epochs"]
                == held["carrier_modes"]
        ),
        "channel_only_test_would_hide_missing_parity_legs": (
            two_cell[
                "unextended_second_epoch_channel_binary_signed_failures"
            ] == (0, 0)
            and two_cell[
                "unextended_second_epoch_parity_commutator_failures"
            ] == two_cell["parity_odd_corrections_per_epoch"]
        ),
        "all_second_epoch_correction_deletions_are_detected": (
            two_cell["deleted_second_epoch_corrections_tested"]
                == two_cell["rank"]
            and two_cell["deleted_second_epoch_corrections_detected"]
                == two_cell["rank"]
            and two_cell["minimum_deleted_correction_failures"] > 0
        ),
        "one_local_carrier_fits_the_landed_palette_and_schedule": all(
            row["carrier_site_uniqueness_failures"] == 0
            and row["carrier_palette_collisions"] == 0
            and row["carrier_hits_existing_returned_routes"] == 0
            and row["routed_G_active_gate_carrier_label_hits"] == 0
            and row["routed_G_carrier_label_return_failures"] == 0
            and row["local_pair_gate_geometry_failures"] == 0
            and row["same_colour_slot_carrier_collisions"] == 0
            and row["bounded_atomic_maximum_targets_excluding_control"] <= 2
            and row["bounded_atomic_row_replay_failures"] == 0
            and row["bounded_atomic_same_block_collisions"] == 0
            and row["inherited_schedule_collisions"] == 0
            and row["inherited_returned_label_failures"] == 0
            and row["inherited_G_sites_outside_O"] == 0
            for row in schedules
        ),
        "carrier_placement_and_ownership_are_coframe_covariant": (
            covariance["proper_cubic_frames"] == 24
            and covariance["frame_origin_contexts"] == 24 * 8
            and covariance["ordered_frame_products"] == 576
            and covariance["frame_carrier_permutation_failures"] == 0
            and covariance["product_carrier_cocycle_failures"] == 0
            and covariance["origin_product_failures"] == 0
            and covariance[
                "coframe_transported_physical_offset_failures"
            ] == 0
            and covariance[
                "frame_origin_physical_carrier_palette_failures"
            ] == 0
            and covariance[
                "frame_origin_physical_distance_failures"
            ] == 0
            and covariance["physical_offset_product_failures"] == 0
            and covariance[
                "fixed_laboratory_offset_mutation_detected_frames"
            ] == 23
        ),
        "prepared_even_CAR_channel_composes_exactly_with_recurrent_G": (
            all(
                row["postcomposition_substitution_failures"] == 0
                and row["shared_output_register_exact"]
                and row["one_particle_mass_residual"] < 1.0e-12
                for row in recurrent["boxes"]
            )
            and tuple(
                row["free_seam_contact_recurrent_powers"]
                for row in recurrent["boxes"]
            ) == ((1, 2, 3, 5, 8), (1, 2, 3))
        ),
        "recurrent_G_has_exact_bounded_parity_even_semantic_factors": all(
            row["direct_even_seam_factors"] == 4 * row["edges"]
            and row["semantic_factors"] == 29 * row["cells"] + 4 * row["edges"]
            and row["direct_even_seam_parity_failures"] == 0
            and row["direct_factor_program_parity_failures"] == 0
            and row[
                "maximum_sampled_phase_aligned_seam_state_residual"
            ] < 1.0e-12
            and row["maximum_direct_seam_support_M2"] <= 17
            and row["maximum_direct_seam_M2_manhattan_diameter"] <= 24
            and row["maximum_nonseam_elementary_parity_residual"] < 1.0e-12
            and row["submitted_seam_elementary_parity_failures"] > 0
            and row["one_particle_mass_residual"] < 1.0e-12
            for row in recurrent["parity_audited_G_factors"]
        ),
    }
    output = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "two_cell_two_epoch": two_cell,
        "held_overlap_two_epoch": held,
        "full_pump_Bell_correction_two_cell": full_two_cell,
        "full_pump_Bell_correction_held_overlap": full_held,
        "dense_even_pair_compiler": dense_pairs,
        "schedule_boxes": schedules,
        "carrier_covariance": covariance,
        "recurrent_G_composition": recurrent,
        "equation": (
            "on the declared even-observable code, the prepared input-side "
            "channel satisfies E B_even = B_physical E for two sequential "
            "pump/Bell/correction epochs; linear postcomposition with the "
            "landed recurrent G gives E (G B_even) = "
            "(G_physical B_physical) E on the same output coordinates; the "
            "same carrier modes are reused"
        ),
        "supplied": (
            "one parity-exchange M2 mode per coarse cell; total-parity "
            "superselection as the observable domain; landed O/I Choi and "
            "encoded live banks; a carrier input initially factorized from "
            "the channel input; clean definite syndrome banks; finite chart, local "
            "tag atlas, colour/slot schedule, boundary and stage order"
        ),
        "derived": (
            "all Bell and correction composites factor into at most two-"
            "target parity-even atoms; exact two-epoch reuse without a fixed "
            "carrier value or carrier reset; 65-M2/cell full palette; "
            "bounded pair geometry; 24/576 carrier covariance; exact "
            "factorwise recurrent-G composition with parity-even seam "
            "semantic factors of at most 17 M2 and diameter 24"
        ),
        "open": (
            "derivation/genesis of the carrier modes and total-parity domain; "
            "nearest-neighbour/radius-one routing of the exact bounded "
            "two-M2 Bell rotations and the up-to-17-M2 recurrent seam "
            "rotations; one monolithic dense executor rather than the exact "
            "signed-graph/factorwise composition proof; autonomous schedule "
            "occurrence/renewal; "
            "translation-invariant enforcement; "
            "time, source/gravity, Record/Born and prediction bridges"
        ),
        "input_sha256": {
            path: file_sha256(Path(path))
            for path in AUDIT_INPUT_PATHS if Path(path).is_file()
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if output["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
