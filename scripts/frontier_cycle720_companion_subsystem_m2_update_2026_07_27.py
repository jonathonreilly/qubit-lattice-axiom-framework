#!/usr/bin/env python3
"""Cycle-720 routed M2 update for the cell-Majorana companion subsystem code.

The local subsystem gauge is the complete radius-one Pauli commutant of one
frozen companion-dressed even-CAR generator dictionary.  The update is the
same in both fixed total-parity sectors and never queries the sector label.
An explicit pure-state encoding/preparation circuit is intentionally not
inferred from local gauge generators; its gauge-fixing locality is audited.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
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
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
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

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
import math

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P709
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_full128_cycle_encoder_2026_07_24 as F128
import frontier_full128_25site_nn_circuit_core_2026_07_24 as S25


c707 = P709.c707
Pauli = C.Pauli
Coord = tuple[int, int, int]
TOL = 4.0e-10


def pauli_from_vector(vector: int, qubits: int) -> Pauli:
    mask = (1 << qubits) - 1
    x, z = vector & mask, vector >> qubits
    return Pauli(phase=(x & z).bit_count() & 1, x=x, z=z)


def xor_rows(rows) -> int:
    output = 0
    for row in rows:
        output ^= row
    return output


def span_combination(target: int, generators: tuple[int, ...]) -> int | None:
    pivots: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(generators):
        row = original
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                old_row, old_combination = pivots[pivot]
                row ^= old_row
                combination ^= old_combination
            else:
                pivots[pivot] = (row, combination)
                break
    row = target
    combination = 0
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return None
        old_row, old_combination = pivots[pivot]
        row ^= old_row
        combination ^= old_combination
    return combination


def support_diameter(fixture: M.CompanionFixture, vector: int) -> int:
    mask = (1 << fixture.qubits) - 1
    support = (vector & mask) | (vector >> fixture.qubits)
    cells = tuple({
        M.qubit_cell(fixture, qubit)
        for qubit in range(fixture.qubits)
        if (support >> qubit) & 1
    })
    return max(
        (
            sum(
                abs(a - b)
                for a, b in zip(fixture.cells[left], fixture.cells[right])
            )
            for left in cells for right in cells
        ),
        default=0,
    )


def gauge_structure(
    fixture: M.CompanionFixture,
    physical_generators: tuple[Pauli, ...],
    relation_rows: tuple[Pauli, ...],
) -> tuple[dict[str, object], tuple[int, ...]]:
    gauge = M.local_centralizer_basis(fixture, physical_generators, 1)
    gram = tuple(
        sum(
            M.symplectic(left, right, fixture.qubits) << index
            for index, right in enumerate(gauge)
        )
        for left in gauge
    )
    gram_rank = C.R.F.base.gf2_rank(gram)
    center_coefficients = M.homogeneous_nullspace(gram, len(gauge))
    center = tuple(
        xor_rows(gauge[index] for index in range(len(gauge)) if (coeff >> index) & 1)
        for coeff in center_coefficients
    )
    center_rank = C.R.F.base.gf2_rank(center)
    gauge_pairs = gram_rank // 2
    logical_qubits = fixture.qubits - center_rank - gauge_pairs
    normalizer_rank = 2 * fixture.qubits - len(gauge)
    logical_pauli_quotient_rank = normalizer_rank - center_rank

    # Symplectic Gram-Schmidt gives one explicit commuting gauge fixing.  Its
    # rows may be products of local gauge generators, so their diameters audit
    # preparation locality rather than proving it.
    remaining = list(gauge)
    radicals = []
    pairs = []
    while remaining:
        left = remaining.pop()
        partner_index = next(
            (
                index for index, right in enumerate(remaining)
                if M.symplectic(left, right, fixture.qubits)
            ),
            None,
        )
        if partner_index is None:
            radicals.append(left)
            continue
        right = remaining.pop(partner_index)
        pairs.append((left, right))
        transformed = []
        for row in remaining:
            transformed.append(
                row
                ^ (left if M.symplectic(row, right, fixture.qubits) else 0)
                ^ (right if M.symplectic(row, left, fixture.qubits) else 0)
            )
        remaining = transformed
    gauge_fixing = tuple(radicals) + tuple(left for left, _right in pairs)
    gauge_fixing_commutator_failures = sum(
        M.symplectic(gauge_fixing[left], gauge_fixing[right], fixture.qubits)
        for left in range(len(gauge_fixing)) for right in range(left)
    )
    deletion_logical_changes = []
    for deleted in range(len(gauge)):
        reduced = gauge[:deleted] + gauge[deleted + 1 :]
        reduced_gram = tuple(
            sum(
                M.symplectic(left, right, fixture.qubits) << index
                for index, right in enumerate(reduced)
            )
            for left in reduced
        )
        reduced_gram_rank = C.R.F.base.gf2_rank(reduced_gram)
        reduced_center = len(reduced) - reduced_gram_rank
        reduced_logical = (
            fixture.qubits - reduced_center - reduced_gram_rank // 2
        )
        deletion_logical_changes.append(reduced_logical - logical_qubits)
    relation_vectors = tuple(
        row.symplectic(fixture.qubits) for row in relation_rows
    )
    base_fixing_paulis = tuple(
        pauli_from_vector(row, fixture.qubits) for row in gauge_fixing
    )
    relation_combinations = tuple(
        span_combination(row, gauge_fixing) for row in relation_vectors
    )
    parity_pauli = Pauli(
        z=sum(1 << mode for mode in range(fixture.matter_qubits))
    )
    parity_vector = parity_pauli.symplectic(fixture.qubits)
    parity_combination = span_combination(parity_vector, gauge_fixing)

    def phase_fixed_sector(odd: bool) -> dict[str, object]:
        equations = []
        quotient_failures = phase_parity_failures = 0
        for relation, combination in zip(relation_rows, relation_combinations):
            if combination is None:
                quotient_failures += 1
                continue
            base_product = M.product(
                base_fixing_paulis[index]
                for index in range(len(base_fixing_paulis))
                if (combination >> index) & 1
            )
            quotient_failures += (
                base_product.x != relation.x or base_product.z != relation.z
            )
            difference = (relation.phase - base_product.phase) % 4
            phase_parity_failures += difference & 1
            equations.append((combination, difference // 2))
        if parity_combination is None:
            quotient_failures += 1
        else:
            base_product = M.product(
                base_fixing_paulis[index]
                for index in range(len(base_fixing_paulis))
                if (parity_combination >> index) & 1
            )
            quotient_failures += (
                base_product.x != parity_pauli.x
                or base_product.z != parity_pauli.z
            )
            desired_phase = 2 * int(odd)
            difference = (desired_phase - base_product.phase) % 4
            phase_parity_failures += difference & 1
            equations.append((parity_combination, difference // 2))
        signs, phase_rank, phase_contradictions = C.gf2_solve(equations)
        signed = tuple(
            Pauli(
                phase=(row.phase + 2 * ((signs >> index) & 1)) % 4,
                x=row.x,
                z=row.z,
            )
            for index, row in enumerate(base_fixing_paulis)
        )
        replay_failures = 0
        for relation, combination in zip(relation_rows, relation_combinations):
            if combination is None:
                replay_failures += 1
                continue
            replay_failures += M.product(
                signed[index]
                for index in range(len(signed))
                if (combination >> index) & 1
            ) != relation
        if parity_combination is None:
            replay_failures += 1
        else:
            desired = Pauli(phase=2 * int(odd), z=parity_pauli.z)
            replay_failures += M.product(
                signed[index]
                for index in range(len(signed))
                if (parity_combination >> index) & 1
            ) != desired
        return {
            "sector": "odd" if odd else "even",
            "gauge_fixing_rows": len(signed),
            "relation_and_parity_phase_equations": len(equations),
            "phase_rank": phase_rank,
            "coordinate_quotient_failures": quotient_failures,
            "phase_parity_failures": phase_parity_failures,
            "phase_contradictions": phase_contradictions,
            "exact_relation_and_parity_replay_failures": replay_failures,
            "signed_gauge_fixing_digest": sha256(
                "|".join(
                    f"{row.phase}:{row.x:x}:{row.z:x}" for row in signed
                ).encode()
            ).hexdigest(),
        }

    sector_fixings = tuple(phase_fixed_sector(odd) for odd in (False, True))
    return ({
        "local_gauge_radius": 1,
        "displayed_independent_local_gauge_generators": len(gauge),
        "gauge_generator_maximum_diameter": max(
            (support_diameter(fixture, row) for row in gauge), default=0
        ),
        "gauge_symplectic_Gram_rank": gram_rank,
        "gauge_pairs": gauge_pairs,
        "gauge_center_rank": center_rank,
        "center_basis_rank": center_rank,
        "center_commutator_failures": sum(
            M.symplectic(row, generator, fixture.qubits)
            for row in center for generator in gauge
        ),
        "subsystem_quantum_logical_qubits": logical_qubits,
        "target_fixed_parity_logical_qubits": fixture.matter_qubits - 1,
        "normalizer_rank": normalizer_rank,
        "logical_Pauli_quotient_rank": logical_pauli_quotient_rank,
        "expected_logical_Pauli_quotient_rank": 2 * (fixture.matter_qubits - 1),
        "target_relation_rows_outside_gauge_span": M.span_failures(
            relation_vectors, gauge
        ),
        "target_relation_rows_outside_canonical_gauge_fixing_span": sum(
            combination is None for combination in relation_combinations
        ),
        "total_matter_parity_outside_canonical_gauge_fixing_span": int(
            parity_combination is None
        ),
        "total_matter_parity_outside_relation_center_span": M.span_failures(
            (parity_vector,), relation_vectors
        ),
        "physical_generator_gauge_commutator_failures": sum(
            M.symplectic(
                row, generator.symplectic(fixture.qubits), fixture.qubits
            )
            for row in gauge for generator in physical_generators
        ),
        "canonical_gauge_fixing_rows": len(gauge_fixing),
        "canonical_gauge_fixing_commutator_failures": gauge_fixing_commutator_failures,
        "canonical_gauge_fixing_maximum_diameter": max(
            (support_diameter(fixture, row) for row in gauge_fixing), default=0
        ),
        "canonical_gauge_fixing_binary_digest": sha256(
            "|".join(f"{row:x}" for row in gauge_fixing).encode()
        ).hexdigest(),
        "sectorwise_phase_fixed_gauge_maps": sector_fixings,
        "single_gauge_generator_deletion_logical_change_minimum": min(
            deletion_logical_changes, default=0
        ),
        "single_gauge_generator_deletion_logical_change_maximum": max(
            deletion_logical_changes, default=0
        ),
        "explicit_sectorwise_gauge_fixing_map_constructed": all(
            row["coordinate_quotient_failures"] == 0
            and row["phase_parity_failures"] == 0
            and row["phase_contradictions"] == 0
            and row["exact_relation_and_parity_replay_failures"] == 0
            for row in sector_fixings
        ),
        "explicit_pure_state_isometry_constructed": False,
        "gauge_preparation_locality_closed": False,
        "sector_boundary": "6N-1 quantum logical qubits plus one supplied total-parity superselection label",
    }, gauge)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))


def placement(fixture: M.CompanionFixture) -> dict[str, object]:
    minimum = tuple(min(cell[axis] for cell in fixture.cells) for axis in range(3))
    maximum = tuple(max(cell[axis] for cell in fixture.cells) for axis in range(3))
    shift = tuple(8 * (low + high) for low, high in zip(minimum, maximum))
    sites = []
    classes = []
    directions = tuple(tuple(int(v) for v in row) for row in c707.DIRECTIONS)
    for mode in range(fixture.matter_qubits):
        cell = fixture.cells[mode // 6]
        center = tuple(16 * value - offset for value, offset in zip(cell, shift))
        sites.append(add(center, tuple(4 * value for value in directions[mode % 6])))
        classes.append("matter_spoke")
    for cell in fixture.cells:
        center = tuple(16 * value - offset for value, offset in zip(cell, shift))
        for axis in range(3):
            sites.append(add(center, tuple(2 * int(index == axis) for index in range(3))))
            classes.append(f"companion_axis_{axis}")
    return {
        "sites_by_qubit": tuple(sites),
        "all_sites": tuple(sorted(sites)),
        "literal_M2": len(sites),
        "placement_collisions": len(sites) - len(set(sites)),
        "M2_per_cell": 9,
        "class_census": dict(Counter(classes)),
        "chart": "Cycle709 spacing-16 spokes plus three axis-companion sites at offset +2",
    }


def lift_pauli(row: Pauli, placed: dict[str, object]) -> c707.Pauli:
    index = {site: item for item, site in enumerate(placed["all_sites"])}
    x = z = 0
    for qubit, site in enumerate(placed["sites_by_qubit"]):
        target = index[site]
        x |= ((row.x >> qubit) & 1) << target
        z |= ((row.z >> qubit) & 1) << target
    return c707.Pauli(row.phase, x, z)


def physical_word(
    fixture: M.CompanionFixture, placed: dict[str, object]
) -> tuple[tuple[c707.Instruction, ...], dict[str, object]]:
    coin, _mass, _phase = F128.common_coin()
    coin_schedule, qr_residual = S25.compile_adjacent_qr(coin)
    sites = placed["sites_by_qubit"]
    all_sites = placed["all_sites"]
    word = []
    parity_residuals = []
    unitarity_residuals = []

    def onsite(kind, wires, matrix):
        parity = np.diag(tuple((-1) ** state.bit_count() for state in range(1 << len(wires))))
        parity_residuals.append(float(np.linalg.norm(matrix @ parity - parity @ matrix)))
        unitarity_residuals.append(float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(matrix.shape[0]))))
        word.append(c707.Instruction(kind, tuple(sites[wire] for wire in wires), matrix))

    for cell in range(len(fixture.cells)):
        offset = 6 * cell
        for kind, wires, matrix in coin_schedule:
            onsite(f"coin_{kind}", tuple(offset + wire for wire in wires), matrix)
    for cell in range(len(fixture.cells)):
        offset = 6 * cell
        for left, right in ((0, 1), (2, 3), (4, 5)):
            onsite("reverse_FSWAP", (offset + left, offset + right), S25.FSWAP)
    seam_order = sorted(
        range(len(fixture.edges)),
        key=lambda edge: (
            C.R.schedule_colour((fixture.edges[edge][2], fixture.edges[edge][3])),
            fixture.edges[edge][2], fixture.edges[edge][3],
        ),
    )
    colour_census = Counter()
    for edge in seam_order:
        owner, axis = fixture.edges[edge][2], fixture.edges[edge][3]
        colour = C.R.schedule_colour((owner, axis))
        for factor, row in enumerate(fixture.physical_terms(edge)):
            colour_census[colour] += 1
            lifted = lift_pauli(row, placed)
            word.extend(
                c707.Instruction(
                    f"seam_c{colour}_f{factor}_{instruction.kind}",
                    instruction.sites,
                    instruction.matrix,
                )
                for instruction in c707.compile_pauli_rotation(
                    lifted, all_sites, math.pi / 2
                )
            )
    contact = np.diag((1, 1, 1, np.exp(1j * F128.CONTACT))).astype(complex)
    for cell in range(len(fixture.cells)):
        offset = 6 * cell
        for left, right in combinations(range(6), 2):
            onsite("onsite_contact", (offset + left, offset + right), contact)
    dictionary = sha256(
        (
            "companion-v1|"
            + "|".join(
                kind + repr(wires) + c707.c655.matrix_digest(matrix)
                for kind, wires, matrix in coin_schedule
            )
            + "|reverse:" + c707.c655.matrix_digest(S25.FSWAP)
            + "|contact:" + c707.c655.matrix_digest(contact)
            + "|seam:gamma_matter*eta_port at both endpoints;angle=pi/2"
        ).encode()
    ).hexdigest()
    return tuple(word), {
        "local_dictionary_sha256": dictionary,
        "logical_update_factors": 29 * len(fixture.cells) + 4 * len(fixture.edges),
        "physical_primitives": len(word),
        "coin_QR_residual": float(qr_residual),
        "maximum_onsite_parity_commutator_residual": max(parity_residuals, default=0.0),
        "maximum_onsite_unitarity_residual": max(unitarity_residuals, default=0.0),
        "seam_factor_colour_census": {
            f"axis{axis}_parity{parity}": count
            for (axis, parity), count in sorted(colour_census.items())
        },
        "runtime_parity_queries": 0,
        "sector_conditioned_gates": 0,
        "word_sha256": sha256(
            "".join(
                row.kind + repr(row.sites) + c707.c655.matrix_digest(row.matrix)
                for row in word
            ).encode()
        ).hexdigest(),
    }


def companion_deletion(
    fixture: M.CompanionFixture,
    gauge: tuple[int, ...],
) -> dict[str, object]:
    rows = M.operator_rows(fixture)
    physical = tuple(row[1] for row in rows)
    target = tuple(row[2] for row in rows)
    edge = 0
    original = fixture.physical_terms(edge)[2]
    left = fixture.edges[edge][0]
    direction = fixture.edges[edge][4] % 6
    deleted = original @ fixture.companion_eta(left, direction)
    changed_index = next(
        index for index, (_family, row, _target) in enumerate(rows)
        if row == original
    )
    corrupted = list(physical)
    corrupted[changed_index] = deleted
    gram_mismatches = sum(
        C.R.C709.anticommutes(corrupted[left_index], corrupted[right_index])
        != C.R.C709.anticommutes(target[left_index], target[right_index])
        for left_index in range(len(rows)) for right_index in range(left_index)
    )
    gauge_syndromes = sum(
        M.symplectic(
            gauge_row, deleted.symplectic(fixture.qubits), fixture.qubits
        )
        for gauge_row in gauge
    )
    return {
        "deleted_companion_Gram_mismatches": gram_mismatches,
        "deleted_companion_local_gauge_syndromes": gauge_syndromes,
    }


def fixture_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = M.CompanionFixture.build(shape)
    rows = M.operator_rows(fixture)
    physical = tuple(row[1] for row in rows)
    relation = M.relation_certificate(fixture)
    relation_rows = relation.pop("relation_rows")
    gauge_report, gauge = gauge_structure(fixture, physical, relation_rows)
    placed = placement(fixture)
    word, update = physical_word(fixture, placed)
    routed, route = c707.route_word(word)
    covariance = P709.covariance_certificate(routed)
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "matter_modes": fixture.matter_qubits,
        "companion_qubits": fixture.qubits - fixture.matter_qubits,
        "relation_algebra": relation,
        "gauge": gauge_report,
        "placement": {
            key: value for key, value in placed.items()
            if key not in ("sites_by_qubit", "all_sites")
        },
        "update": update,
        "route": {
            "routed_gate_count": route["routed_gate_count"],
            "maximum_route_distance": route["maximum_route_distance"],
            "non_NN_failures": route["non_NN_failures"],
            "operand_order_failures": route["operand_order_failures"],
            "route_return_failures": route["route_return_failures"],
            "delete_first_swap_detected_macros": route["delete_first_swap_detected_macros"],
            "routed_word_sha256": route["word_sha256"],
        },
        "deletion": companion_deletion(fixture, gauge),
        "covariance": covariance,
    }


def main() -> None:
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    fixtures = tuple(fixture_certificate(shape) for shape in shapes)
    fswap = C.R.canonical_factorization()
    mass = C.R.local_free_contact_mass()["mass_contact"]
    cycle230 = C712.cycle230_semantic_certificate(C712.decoded_word(2)[0])
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "one R1 subsystem gauge closes 6N-1 quantum logical qubits plus parity label with no extra logical operators",
        all(
            row["gauge"]["subsystem_quantum_logical_qubits"]
            == row["gauge"]["target_fixed_parity_logical_qubits"]
            and row["gauge"]["logical_Pauli_quotient_rank"]
            == row["gauge"]["expected_logical_Pauli_quotient_rank"]
            and row["gauge"]["target_relation_rows_outside_gauge_span"] == 0
            and row["gauge"]["target_relation_rows_outside_canonical_gauge_fixing_span"] == 0
            and row["gauge"]["total_matter_parity_outside_canonical_gauge_fixing_span"] == 0
            and row["gauge"]["total_matter_parity_outside_relation_center_span"] == 1
            and row["gauge"]["explicit_sectorwise_gauge_fixing_map_constructed"]
            and row["gauge"]["physical_generator_gauge_commutator_failures"] == 0
            and row["relation_algebra"]["relation_phase_contradictions"] == 0
            for row in fixtures
        ),
    )
    check(
        "one frozen query-free coin/reverse/seam/contact dictionary acts on every held subsystem code",
        len({row["update"]["local_dictionary_sha256"] for row in fixtures}) == 1
        and all(
            row["update"]["runtime_parity_queries"] == 0
            and row["update"]["sector_conditioned_gates"] == 0
            and row["update"]["coin_QR_residual"] < TOL
            and row["update"]["maximum_onsite_parity_commutator_residual"] < TOL
            for row in fixtures
        )
        and fswap["four_rotation_residual_up_to_phase"] < TOL
        and cycle230["onsite_64_state_contact_residual"] < TOL
        and mass["one_particle_mass_residual"] < TOL,
    )
    check(
        "all four boxes have collision-free 9-M2/cell placement and complete NN routes with returned spectators",
        all(
            row["placement"]["placement_collisions"] == 0
            and row["placement"]["M2_per_cell"] == 9
            and row["route"]["non_NN_failures"] == 0
            and row["route"]["operand_order_failures"] == 0
            and row["route"]["route_return_failures"] == 0
            and row["route"]["delete_first_swap_detected_macros"] > 0
            for row in fixtures
        ),
    )
    check(
        "companion, gauge-generator, and routed-SWAP deletions are active",
        all(
            row["deletion"]["deleted_companion_Gram_mismatches"] > 0
            and row["deletion"]["deleted_companion_local_gauge_syndromes"] > 0
            and (
                row["gauge"]["single_gauge_generator_deletion_logical_change_minimum"] != 0
                or row["gauge"]["single_gauge_generator_deletion_logical_change_maximum"] != 0
            )
            and row["route"]["delete_first_swap_detected_macros"] > 0
            for row in fixtures
        ),
    )
    check(
        "transported route geometry closes 24 frames, 576 products, and 8 translations on every box",
        all(
            row["covariance"]["proper_cubic_frames"] == 24
            and row["covariance"]["ordered_frame_products"] == 576
            and row["covariance"]["translation_residue_diagrams"] == 8
            and row["covariance"]["rotated_word_NN_failures"] == 0
            and row["covariance"]["frame_product_site_diagram_failures"] == 0
            and row["covariance"]["translated_word_NN_failures"] == 0
            for row in fixtures
        ),
    )
    check(
        "pure-state compiler promotion is withheld because explicit isometry and local gauge preparation are not constructed",
        all(
            not row["gauge"]["explicit_pure_state_isometry_constructed"]
            and not row["gauge"]["gauge_preparation_locality_closed"]
            for row in fixtures
        ),
    )
    report = {
        "status": "cycle720-positive-local-companion-subsystem-M2-update__pure-state-E-open",
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "pass": all(row["pass"] for row in checks),
        "checks": checks,
        "fixtures": fixtures,
        "Cycle230_mass": {**cycle230, **mass},
        "supplied": (
            "one fixed total-parity superselection label at genesis",
            "one gauge-center sector/vacuum representative",
            "one within-cell order for matter and companion Majoranas",
            "Cycle709 spacing-16 chart, serial route schedule, and blank route-work M2",
            "Cycle219 coin and Cycle230 contact parameters",
        ),
        "derived": (
            "three companion qubits per cell and a radius-one local subsystem gauge",
            "exact complete even-CAR presentation modulo that gauge in four box sizes",
            "6N-1 quantum logical qubits plus one parity superselection label with no extra logical operators",
            "phase-fixed canonical even/odd gauge-fixing maps with exact target-relation and parity replay",
            "one query-free local full-update dictionary preserving the gauge",
            "literal 9-M2/cell placements and complete nearest-neighbour routed words in all four boxes",
            "active companion, gauge, seam-factor, and route deletion controls",
        ),
        "open": (
            "a bounded-local preparation circuit for the explicit sectorwise gauge-fixing maps",
            "autonomous gauge-center genesis and repair",
            "coherent even/odd parity transport",
            "active transformed operator/subsystem covariance rather than route geometry alone",
            "collision-free constant-depth parallel routing, periodic sectors, and fault tolerance",
            "physical time, source/gravity, Record, and Born/history bridges",
        ),
        "claim_ceiling": (
            "Positive size-independent radius-one subsystem-algebra compiler and literal M2 full-update route in fixed parity sectors. "
            "Not yet a pure-state physical compiler: a local encoding/preparation isometry and autonomous gauge genesis are unconstructed, and only route-geometry covariance is executed."
        ),
        "compiler_claim_gate": {
            "local_subsystem_algebra_and_update": "PASS",
            "explicit_bounded_state_isometry": "FAIL",
            "autonomous_gauge_genesis": "FAIL",
            "transformed_operator_covariance": "FAIL",
            "full_physical_compiler_claim_allowed": False,
        },
        "no_go_discipline": {
            "gate": "FAIL_for_broad_no_go__constructive_subsystem_positive",
            "N1_alternatives": "pure-state gauge fixing, non-Clifford isometry, Euler quotient, and other companion gauges remain live",
            "N2_wall_independence": "subsystem algebra/update, state E, gauge genesis, covariance, and routing depth are separate",
            "N3_hidden_imports": "parity label, gauge sector, local order, chart, schedule, blanks, and law parameters explicit",
            "N4_residual_matching": "rank/kernel/phase/gauge residuals separated from local-factor and route residuals",
            "N5_resolution": "2x2x2,3x2x2,3x3x2,5x3x2 without refit",
            "N6_partial_closure": "local subsystem compiler closes before pure-state E",
            "N7_steelman": "a bounded gauge-fixing preparation could promote this result",
            "N8_cross_cycle_echo": "uses Cycle658 endpoint incidence with factor-private local companions and Cycle709/718 M2 routing",
        },
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str, separators=(",", ":")).encode()
    ).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    if not report["pass"]:
        raise SystemExit(1)
    print("COMPANION_SUBSYSTEM_M2_UPDATE_POSITIVE__PURE_STATE_E_OPEN")


if __name__ == "__main__":
    main()
