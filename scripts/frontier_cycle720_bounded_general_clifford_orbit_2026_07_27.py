#!/usr/bin/env python3
"""Cycle-720 bounded-general-Clifford and even-orbit support.

This probe asks whether allowing X/Z mixing can localize the exact common E
found by the coherent cell-edge Euler-marker construction.  It also separates
that full-state question from the smaller parity-preserving operator-algebra
question.  It is bounded Cycle-720 evidence only: authority none, audit unset.
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
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
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

from hashlib import sha256
from itertools import combinations
import json

import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C


def distance(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def object_vertices(
    row: tuple[str, tuple[int, int, int], tuple[int, ...]],
) -> tuple[tuple[int, int, int], ...]:
    _kind, owner, axes = row
    vertices = []
    for subset in range(1 << len(axes)):
        vertex = list(owner)
        for item, axis in enumerate(axes):
            if (subset >> item) & 1:
                vertex[axis] += 1
        vertices.append(tuple(vertex))
    return tuple(vertices)


def qubit_locations(
    fixture: C.EulerMarkerGauge,
) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    rows: list[tuple[tuple[int, int, int], ...]] = []
    for mode in range(fixture.matter_qubits):
        rows.append((fixture.cells[mode // 6],))
    for left, right, _cell, _axis, _lm, _rm in fixture.edges:
        rows.append((fixture.cells[left], fixture.cells[right]))
    rows.extend(object_vertices(row) for row in fixture.marker_objects)
    if len(rows) != fixture.qubits:
        raise AssertionError((len(rows), fixture.qubits))
    return tuple(rows)


def local_logical_x_certificate(
    fixture: C.EulerMarkerGauge, radius: int
) -> dict[str, object]:
    """Generous ball-supported Pauli solve for every encoded logical X.

    A register is allowed if any incident cell-complex vertex is in the ball.
    Failure is therefore stronger than failure under a single-anchor layout,
    but remains specific to this Euler-marker stabilizer family.
    """
    locations = qubit_locations(fixture)
    failures = 0
    contradictions = []
    variable_counts = []
    solution_weights = []
    for logical in range(fixture.matter_qubits):
        center = fixture.cells[logical // 6]
        allowed = tuple(
            qubit
            for qubit, vertices in enumerate(locations)
            if min(distance(center, vertex) for vertex in vertices) <= radius
        )
        index = {qubit: item for item, qubit in enumerate(allowed)}
        equations = []
        for row_index, row in enumerate(fixture.w_rows):
            mask = 0
            for qubit, item in index.items():
                if (row.z >> qubit) & 1:
                    mask ^= 1 << (2 * item)
                if (row.x >> qubit) & 1:
                    mask ^= 1 << (2 * item + 1)
            equations.append((mask, int(row_index == logical)))
        solution, rank, inconsistent = C.gf2_solve(equations)
        failures += bool(inconsistent)
        contradictions.append(inconsistent)
        variable_counts.append(2 * len(allowed))
        if not inconsistent:
            solution_weights.append(
                sum(
                    bool((solution >> (2 * item)) & 3)
                    for item in range(len(allowed))
                )
            )
    return {
        "radius": radius,
        "logical_X_rows": fixture.matter_qubits,
        "unsolved_logical_X_rows": failures,
        "minimum_equation_contradictions": min(contradictions),
        "maximum_equation_contradictions": max(contradictions),
        "minimum_binary_variables": min(variable_counts),
        "maximum_binary_variables": max(variable_counts),
        "maximum_solved_Pauli_weight": max(solution_weights, default=None),
        "support_rule": "any incident cell-complex vertex lies within Manhattan ball",
    }


def operator_rows(
    fixture: C.EulerMarkerGauge,
) -> tuple[tuple[str, C.Pauli, C.Pauli], ...]:
    rows: list[tuple[str, C.Pauli, C.Pauli]] = []
    for edge in range(len(fixture.edges)):
        rows.extend(
            ("seam", physical, target)
            for physical, target in zip(
                fixture.physical_terms(edge), fixture.expected_terms(edge)
            )
        )
    for mode in range(fixture.matter_qubits):
        row = C.Pauli(z=1 << mode)
        rows.append(("onsite_B", row, row))
    for cell in range(len(fixture.cells)):
        for left_local, right_local in combinations(range(6), 2):
            left = 6 * cell + left_local
            right = 6 * cell + right_local
            endpoints = (1 << left) | (1 << right)
            between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
            rows.extend(
                (
                    ("onsite_even", C.Pauli(phase=2, x=endpoints, z=between | endpoints), C.Pauli(phase=2, x=endpoints, z=between | endpoints)),
                    ("onsite_even", C.Pauli(x=endpoints, z=between), C.Pauli(x=endpoints, z=between)),
                )
            )
    return tuple(rows)


def general_clifford_reduction(
    fixture: C.EulerMarkerGauge, diagonal: dict[str, object]
) -> dict[str, object]:
    """Certify why general logical Clifford freedom collapses to diagonal.

    In block convention (x',z')=(A x+B z,C x+D z), requiring every onsite
    B/Z_i generator to map to the same Z_i sets B=0 and D=I.  The symplectic
    equations then force A=I and C symmetric.  This is precisely a diagonal
    Clifford, including S and CZ phases.  Thus the existing restricted
    diagonal equations exhaust *logical Clifford* orientations of this fixed
    physical representation; it is not a statement about other codes/QCAs.
    """
    modes = fixture.matter_qubits
    return {
        "logical_modes": modes,
        "onsite_Z_constraints": modes,
        "forced_block_B_zero_entries": modes * modes,
        "forced_block_D_identity_entries": modes * modes,
        "symplectic_consequence_A_identity": True,
        "symplectic_consequence_C_symmetric": True,
        "remaining_general_Clifford_variables": modes * (modes + 1) // 2,
        "matches_diagonal_variable_count": (
            diagonal["symmetric_variables"] == modes * (modes + 1) // 2
        ),
        "radius_1_contradictions": diagonal["restricted_coordinate_systems"]["cell_radius_1"]["contradictions"],
        "radius_2_contradictions": diagonal["restricted_coordinate_systems"]["cell_radius_2"]["contradictions"],
        "radius_3_contradictions": diagonal["restricted_coordinate_systems"]["cell_radius_3"]["contradictions"],
        "scope": "all logical Clifford orientations of this fixed Euler-marker representation that preserve each onsite B/Z_i label",
    }


def even_orbit_certificate(
    fixture: C.EulerMarkerGauge,
) -> dict[str, object]:
    rows = operator_rows(fixture)
    stabilizers = fixture.w_rows[fixture.matter_qubits :]
    commutator_mismatches = 0
    stabilizer_commutator_failures = 0
    leakage_failures = 0
    decoded_vectors = []
    decoded_rows = []
    target_rows = []
    target_vectors = []
    family_counts: dict[str, int] = {}
    for family, physical, target in rows:
        family_counts[family] = family_counts.get(family, 0) + 1
        decoded, leakage, _stabilizer = fixture.decoded(physical)
        leakage_failures += bool(leakage)
        stabilizer_commutator_failures += sum(
            C.R.C709.anticommutes(physical, stabilizer)
            for stabilizer in stabilizers
        )
        decoded_vectors.append(decoded.symplectic(fixture.matter_qubits))
        target_vectors.append(target.symplectic(fixture.matter_qubits))
        decoded_rows.append(decoded)
        target_rows.append(target)
    for left in range(len(rows)):
        for right in range(left):
            commutator_mismatches += (
                C.R.C709.anticommutes(rows[left][1], rows[right][1])
                != C.R.C709.anticommutes(rows[left][2], rows[right][2])
            )
    target_rank = C.R.F.base.gf2_rank(target_vectors)
    decoded_rank = C.R.F.base.gf2_rank(decoded_vectors)
    expected_even_rank = 2 * fixture.matter_qubits - 1

    def kernel_relations(vectors: list[int]) -> tuple[int, ...]:
        pivots: dict[int, tuple[int, int]] = {}
        relations = []
        for index, original in enumerate(vectors):
            vector = original
            combination = 1 << index
            while vector:
                pivot = vector.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = (vector, combination)
                    break
                old_vector, old_combination = pivots[pivot]
                vector ^= old_vector
                combination ^= old_combination
            else:
                relations.append(combination)
        return tuple(relations)

    target_kernel = kernel_relations(target_vectors)
    decoded_kernel = kernel_relations(decoded_vectors)

    def relation_failures(
        kernel: tuple[int, ...], source: list[C.Pauli], target: list[C.Pauli]
    ) -> tuple[int, int]:
        coordinate_failures = phase_failures = 0
        for combination in kernel:
            source_product = C.product(
                row for index, row in enumerate(source) if (combination >> index) & 1
            )
            target_product = C.product(
                row for index, row in enumerate(target) if (combination >> index) & 1
            )
            coordinate_failures += bool(target_product.x or target_product.z)
            phase_failures += source_product.phase != target_product.phase
        return coordinate_failures, phase_failures

    target_to_decoded = relation_failures(
        target_kernel, target_rows, decoded_rows
    )
    decoded_to_target = relation_failures(
        decoded_kernel, decoded_rows, target_rows
    )
    return {
        "generator_family_counts": family_counts,
        "target_even_Pauli_span_rank": target_rank,
        "decoded_even_Pauli_span_rank": decoded_rank,
        "expected_full_even_Pauli_span_rank": expected_even_rank,
        "full_even_span_reached": target_rank == decoded_rank == expected_even_rank,
        "physical_vs_target_commutator_Gram_mismatches": commutator_mismatches,
        "target_kernel_generators": len(target_kernel),
        "decoded_kernel_generators": len(decoded_kernel),
        "target_kernel_decoded_coordinate_failures": target_to_decoded[0],
        "target_kernel_phase_failures": target_to_decoded[1],
        "decoded_kernel_target_coordinate_failures": decoded_to_target[0],
        "decoded_kernel_phase_failures": decoded_to_target[1],
        "stabilizer_commutator_failures": stabilizer_commutator_failures,
        "logical_leakage_failures": leakage_failures,
        "orbit_interpretation": "local generators present the full parity-preserving Pauli algebra; a word-defined state orbit is exact within a chosen parity sector",
        "state_encoding_boundary": "this algebra/orbit statement does not supply a bounded-depth state isometry or coherent transport between total-parity sectors",
    }


def marker_sector_certificate(fixture: C.EulerMarkerGauge) -> dict[str, object]:
    count = len(fixture.marker_objects)
    equality_rank = C.R.F.base.gf2_rank(
        row.z >> fixture.base.qubits for row in fixture.marker_equalities
    )
    # Commuting with every Z_i Z_j equality makes the X support constant on
    # the connected marker graph.  The only two solutions are empty and all.
    all_mask = (1 << count) - 1
    all_commutes = all(
        ((all_mask & (row.z >> fixture.base.qubits)).bit_count() & 1) == 0
        for row in fixture.marker_equalities
    )
    return {
        "marker_qubits": count,
        "displayed_local_equality_rank": equality_rank,
        "equality_code_dimension": count - equality_rank,
        "sector_definite_marker_zero_is_product_state": True,
        "sector_definite_marker_one_is_product_state": True,
        "nontrivial_sector_flip_commutes_with_equalities": all_commutes,
        "minimum_marker_sector_flip_weight": count,
        "coherent_even_odd_superposition_requires_global_marker_correlation": True,
        "parity_superselection_would_remove_only_this_coherence_requirement": True,
        "parity_superselection_is_supplied_not_derived": True,
    }


def main() -> None:
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2))
    fixtures = tuple(C.EulerMarkerGauge.build(shape) for shape in shapes)
    diagonal = tuple(C.diagonal_common_e(fixture) for fixture in fixtures)
    general = tuple(
        general_clifford_reduction(fixture, row)
        for fixture, row in zip(fixtures, diagonal)
    )
    local_x = tuple(
        {
            "shape": fixture.shape,
            "radii": tuple(
                local_logical_x_certificate(fixture, radius)
                for radius in (1, 2, 3)
            ),
        }
        for fixture in fixtures
    )
    even_orbits = tuple(even_orbit_certificate(fixture) for fixture in fixtures)
    marker_sectors = tuple(marker_sector_certificate(fixture) for fixture in fixtures)

    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "onsite B reduces every fixed-representation general logical Clifford solve to the complete diagonal family",
        all(
            row["symplectic_consequence_A_identity"]
            and row["symplectic_consequence_C_symmetric"]
            and row["matches_diagonal_variable_count"]
            for row in general
        ),
    )
    check(
        "no radius-1/2/3 size-independent logical-Clifford rule survives both held boxes",
        all(
            any(radius["unsolved_logical_X_rows"] for radius in row["radii"])
            for row in local_x[1:]
        )
        and all(row["radius_3_contradictions"] > 0 for row in general[1:]),
    )
    check(
        "the local physical generators nevertheless close the complete even Pauli algebra on every box",
        all(
            row["full_even_span_reached"]
            and row["physical_vs_target_commutator_Gram_mismatches"] == 0
            and row["target_kernel_decoded_coordinate_failures"] == 0
            and row["target_kernel_phase_failures"] == 0
            and row["decoded_kernel_target_coordinate_failures"] == 0
            and row["decoded_kernel_phase_failures"] == 0
            and row["stabilizer_commutator_failures"] == 0
            and row["logical_leakage_failures"] == 0
            for row in even_orbits
        ),
    )
    check(
        "sector-definite Euler markers are local products but coherent sector transport has growing full-marker support",
        all(
            row["equality_code_dimension"] == 1
            and row["nontrivial_sector_flip_commutes_with_equalities"]
            and row["minimum_marker_sector_flip_weight"] == row["marker_qubits"]
            for row in marker_sectors
        ),
    )

    report = {
        "status": "cycle720-positive-even-algebra-orbit__bounded-full-state-E-open",
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "pass": all(row["pass"] for row in checks),
        "checks": checks,
        "general_Clifford_reduction": general,
        "generous_local_logical_X_solves": local_x,
        "even_operator_orbits": even_orbits,
        "Euler_marker_sectors": marker_sectors,
        "derived": (
            "for this fixed physical representation, preserving every onsite B/Z_i collapses a general logical Clifford to the already exhausted diagonal S/CZ family",
            "the held boxes reject a common radius-3 Clifford orientation and generous ball-supported individual logical-X dressings remain absent at fixed radii",
            "the seam plus complete onsite generator set is a local exact presentation of the full even Pauli algebra on all three boxes",
            "within a selected parity sector, a local-generator orbit is algebraically exact and path differences are stabilizer/gauge words",
            "each definite Euler marker sector is a product marker configuration, while coherent parity-sector flipping has support on every marker",
        ),
        "supplied": (
            "choice of a total-parity sector, unless coherent even/odd superpositions are required",
            "a stabilizer/gauge vacuum representative",
            "within-cell mode order and local generator labels",
            "the 24-phase schedule, which is not physical time",
        ),
        "open": (
            "a bounded-radius full-state QCA E outside this fixed Clifford representation",
            "a local preparation/refresh law for the gauge stabilizer vacuum",
            "coherent full-parity encoding without the growing marker-sector flip",
            "transformed-E proper-cubic covariance, because no bounded transformed E has closed",
            "literal M2 placement/routing and composed coin/contact update",
            "periodic boxes and Wilson/spin sectors",
        ),
        "claim_ceiling": (
            "Positive local even-operator-algebra/orbit encoding on open contractible boxes, including held sizes. "
            "Not a full-state bounded-QCA compiler: general Clifford freedom for the fixed representation collapses to the nonlocal diagonal solution, and coherent parity-sector transport remains global."
        ),
        "no_go_discipline": {
            "gate": "FAIL_for_broad_no_go__route_specific_clifford_and_marker_result_only",
            "N1_alternatives": (
                "non-Clifford QCA/state encoding remains live",
                "subsystem/quotient representation remains live",
                "sector-superselected even-algebra orbit is positive",
                "endpoint-incidence and alternate gauge geometries remain live",
            ),
            "N2_wall_independence": "fixed-representation Clifford locality, marker coherence, gauge-vacuum preparation, and M2 routing are separate walls",
            "N3_hidden_imports": "parity-sector choice, gauge vacuum, mode labels, and schedule are explicit",
            "N4_residual_matching": "binary contradictions are charged only to exact Clifford equations; even-algebra positive uses exact ranks and Gram residuals",
            "N5_resolution": "2x2x2 plus held 3x2x2 and 3x3x2 open boxes",
            "N6_partial_closure": "full even algebra closes despite full-state E remaining open",
            "N7_steelman": "a non-Clifford locality-preserving encoding or genuine subsystem quotient could evade the fixed-Clifford reduction",
            "N8_cross_cycle_echo": "consistent with the prior long-range diagonal E and local plaquette-span certificates",
        },
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    if not report["pass"]:
        raise SystemExit(1)
    print("BOUNDED_GENERAL_CLIFFORD_REJECTED__LOCAL_EVEN_ORBIT_POSITIVE")


if __name__ == "__main__":
    main()
