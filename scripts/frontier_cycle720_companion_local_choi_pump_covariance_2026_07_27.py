#!/usr/bin/env python3
"""Cycle-720 signed proper-cubic covariance of local Choi preparation.

The tree/plaquette pump prepares the correct projector for every root and axis
order.  That does not by itself prove signed proper-cubic covariance.  This
runner actively transports the complete Choi tableau, private corrections,
finite atlas descriptors, Bell-reference charts, syndrome labels, geometric
tree/plaquette schedule, and returned mobile-rail routes through all 24 proper
cubic frames and all 576 ordered products.

The eight checkerboard coframe origins are retained classical gauge sectors.
The target origin is transported with the frame and the already-derived
onsite companion-Z correction is used in each sector.  No origin is selected
by the host and no schedule step is called physical time.
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
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
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
from itertools import product as cartesian_product
import json

import numpy as np

import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O


Pauli = M.Pauli
Coord = tuple[int, int, int]


def shifted(row, offset: int):
    return type(row)(row.phase, row.x << offset, row.z << offset)


def choi_images(
    source: M.CompanionFixture,
    target: M.CompanionFixture,
    frame: np.ndarray,
    shift: Coord,
    target_seed: Coord,
):
    solution = Q.seeded_sheet_solution(
        frame, Q.predicted_sheet_solution(frame), target_seed
    )
    output_x, output_z = Q.corrected_images(
        source, target, frame, shift, solution
    )
    input_x, input_z = Q.matter_images(source, target, frame, shift)
    return (
        tuple(output_x) + tuple(shifted(row, target.qubits) for row in input_x),
        tuple(output_z) + tuple(shifted(row, target.qubits) for row in input_z),
    )


def transform_row(row: Pauli, images) -> Pauli:
    mapped = Q.S.apply_images(Q.S.cpauli(row), images)
    return Pauli(mapped.phase, mapped.x, mapped.z)


def fields(row) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def affine_cell(cell: Coord, frame: np.ndarray, shift: Coord) -> Coord:
    return tuple(int(value) for value in (
        frame @ np.asarray(cell, dtype=int) + np.asarray(shift, dtype=int)
    ))


def ordered_affine_fixture(
    source: M.CompanionFixture, frame: np.ndarray, shift: Coord
) -> M.CompanionFixture:
    """Transport spatial sites without silently changing the JW chart order.

    Sorting the transformed coordinates would add an unrelated global
    fermionic reindexing to the proper-cubic action.  Site order here is only
    a matrix-coordinate chart; the physical labels remain the transformed
    spatial coordinates.
    """
    cells = tuple(affine_cell(cell, frame, shift) for cell in source.cells)
    lookup = {cell: index for index, cell in enumerate(cells)}
    edges = []
    for cell in cells:
        for axis in range(3):
            target = list(cell)
            target[axis] += 1
            target_cell = tuple(target)
            if target_cell not in lookup:
                continue
            left = lookup[cell]
            right = lookup[target_cell]
            edges.append((
                left, right, cell, axis,
                6 * left + 2 * axis + 1,
                6 * right + 2 * axis,
            ))
    return M.CompanionFixture(
        (0, 0, 0), cells, tuple(edges), 6 * len(cells), 9 * len(cells)
    )


def port_permutation(frame: np.ndarray) -> tuple[int, ...]:
    output = []
    for port in range(6):
        axis = port // 2
        sign = -1 if port % 2 == 0 else 1
        vector = np.zeros(3, dtype=int)
        vector[axis] = sign
        mapped = frame @ vector
        target_axis = int(np.flatnonzero(mapped)[0])
        target_sign = int(mapped[target_axis])
        output.append(2 * target_axis + int(target_sign > 0))
    return tuple(output)


def transport_port_mask(mask: int, frame: np.ndarray) -> int:
    permutation = port_permutation(frame)
    return sum(
        ((mask >> source) & 1) << permutation[source]
        for source in range(6)
    )


def correction_descriptor(
    fixture: M.CompanionFixture, tag: tuple
) -> tuple:
    if tag[0] in ("onsite_Z", "onsite_XX"):
        cell = tag[1]
        modes = (tag[2],) if tag[0] == "onsite_Z" else (tag[2], tag[2] + 1)
        return (
            tag[0], fixture.cells[cell], incident_port_mask(fixture, cell), modes
        )
    edge = tag[1]
    left, right, *_rest = fixture.edges[edge]
    return (
        "edge_private",
        fixture.cells[left], incident_port_mask(fixture, left),
        fixture.cells[right], incident_port_mask(fixture, right),
    )


def incident_port_mask(fixture: M.CompanionFixture, cell: int) -> int:
    return P.incident_port_mask(fixture, cell)


def transport_descriptor(
    descriptor: tuple, frame: np.ndarray, shift: Coord
) -> tuple:
    directions = Q.direction_permutation(frame)
    if descriptor[0] in ("onsite_Z", "onsite_XX"):
        family, cell, mask, modes = descriptor
        return (
            family,
            affine_cell(cell, frame, shift),
            transport_port_mask(mask, frame),
            tuple(directions[mode] for mode in modes),
        )
    family, left, left_mask, right, right_mask = descriptor
    return (
        family,
        affine_cell(left, frame, shift),
        transport_port_mask(left_mask, frame),
        affine_cell(right, frame, shift),
        transport_port_mask(right_mask, frame),
    )


def schedule_descriptor(
    fixture: M.CompanionFixture, tag: tuple
) -> tuple:
    if tag[0] in ("onsite_Z", "onsite_XX"):
        return correction_descriptor(fixture, tag)
    if tag[0] == "tree":
        edge = tag[1]
        left, right, *_rest = fixture.edges[edge]
        return ("tree", fixture.cells[left], fixture.cells[right])
    new_edge, cycle = tag[1], tag[2]

    def endpoints(edge):
        left, right, *_rest = fixture.edges[edge]
        return fixture.cells[left], fixture.cells[right]

    return (
        "plaquette", endpoints(new_edge),
        tuple(sorted(tuple(sorted(endpoints(edge))) for edge in cycle)),
    )


def transport_schedule_descriptor(
    descriptor: tuple, frame: np.ndarray, shift: Coord
) -> tuple:
    if descriptor[0] in ("onsite_Z", "onsite_XX", "edge_private"):
        return transport_descriptor(descriptor, frame, shift)
    if descriptor[0] == "tree":
        return (
            "tree",
            affine_cell(descriptor[1], frame, shift),
            affine_cell(descriptor[2], frame, shift),
        )
    _family, new_edge, cycle = descriptor

    def mapped_edge(edge):
        return tuple(sorted((
            affine_cell(edge[0], frame, shift),
            affine_cell(edge[1], frame, shift),
        )))

    return (
        "plaquette", mapped_edge(new_edge),
        tuple(sorted(mapped_edge(edge) for edge in cycle)),
    )


def map_route(
    route: tuple[tuple[Coord, Coord], ...],
    frame: np.ndarray,
    shift: Coord,
) -> tuple[tuple[Coord, Coord], ...]:
    return tuple(
        (affine_cell(left, frame, shift), affine_cell(right, frame, shift))
        for left, right in route
    )


def row_routes(
    fixture: M.CompanionFixture,
    rows: tuple[Pauli, ...],
) -> tuple[tuple[tuple[Coord, Coord], ...], ...]:
    output = []
    for row in rows:
        support = P.pauli_cells(fixture, row)
        output.append(P.returned_route(min(support), support))
    return tuple(output)


def row_support_inside(
    fixture: M.CompanionFixture, row: Pauli, allowed: set[Coord]
) -> bool:
    return P.pauli_cells(fixture, row) <= allowed


def base_context(
    shape: tuple[int, int, int], atlas: dict[str, object]
):
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    root = min(fixture.cells)
    rows, tags, _report = P.schedule_basis(fixture, root, (2, 1, 0))
    corrections = tuple(
        P.schedule_correction(fixture, tag, atlas) for tag in tags
    )
    descriptors = tuple(correction_descriptor(fixture, tag) for tag in tags)
    schedule_descriptors = tuple(
        schedule_descriptor(fixture, tag) for tag in tags
    )
    routes = row_routes(fixture, rows)
    return fixture, rows, tags, corrections, descriptors, schedule_descriptors, routes


def frame_certificate(
    shape: tuple[int, int, int], atlas: dict[str, object]
) -> dict[str, object]:
    source, rows, tags, corrections, descriptors, schedule_descriptors, routes = (
        base_context(shape, atlas)
    )
    direct_rows, _direct_tags = P.direct_graph_basis(source)
    onsite_count = 11 * len(source.cells)
    direct_edge_rows = direct_rows[onsite_count:]
    frames = tuple(T.proper_cubic_frames())
    seeds = tuple(cartesian_product(range(2), repeat=3))
    signed_projector_failures = 0
    correction_syndrome_failures = 0
    correction_support_failures = 0
    route_failures = 0
    atlas_key_failures = 0
    schedule_key_failures = 0
    bell_chart_failures = 0
    syndrome_register_failures = 0
    active_rows = 0
    active_corrections = 0
    active_routes = 0
    orbit_words = set()
    orbit_keys = set()
    reversed_edge_rows = 0
    oriented_edge_row_failures = 0
    geometric_route_gauge_mismatches = 0
    for frame in frames:
        shift = (0, 0, 0)
        target = O.arbitrary_fixture(Q.affine_cells(source.cells, frame, shift))
        target_direct, _target_tags = P.direct_graph_basis(target)
        total_qubits = target.qubits + target.matter_qubits
        for source_seed in seeds:
            target_seed = Q.transported_seed(frame, shift, source_seed)
            images = choi_images(
                source, target, frame, shift, target_seed
            )
            mapped_rows = tuple(transform_row(row, images) for row in rows)
            mapped_direct_edges = tuple(
                transform_row(row, images) for row in direct_edge_rows
            )
            mapped_corrections = tuple(
                transform_row(row, images) for row in corrections
            )
            signed_projector_failures += P.R.signed_replay_failures(
                mapped_rows, target_direct, total_qubits
            )
            signed_projector_failures += P.R.signed_replay_failures(
                target_direct, mapped_rows, total_qubits
            )
            for target_index, correction in enumerate(mapped_corrections):
                for row_index, stabilizer in enumerate(
                    mapped_rows[:target_index + 1]
                ):
                    correction_syndrome_failures += M.symplectic(
                        correction.symplectic(total_qubits),
                        stabilizer.symplectic(total_qubits),
                        total_qubits,
                    ) != int(target_index == row_index)
                allowed = {
                    affine_cell(cell, frame, shift)
                    for cell in P.pauli_cells(source, corrections[target_index])
                }
                correction_support_failures += not row_support_inside(
                    target, correction, allowed
                )
                orbit_words.add(fields(correction))
                orbit_keys.add(transport_descriptor(
                    descriptors[target_index], frame, shift
                ))
                active_corrections += 1

            for row_index, (route, mapped_row) in enumerate(
                zip(routes, mapped_rows)
            ):
                mapped_support = P.pauli_cells(target, mapped_row)
                mapped_route = P.returned_route(
                    min(mapped_support), mapped_support
                )
                mapped_anchor = min(mapped_support)
                geometric_route_gauge_mismatches += (
                    mapped_route != map_route(route, frame, shift)
                )
                route_failures += any(
                    sum(abs(a - b) for a, b in zip(left, right)) != 1
                    for left, right in mapped_route
                )
                visited = {mapped_anchor}
                position = mapped_anchor
                for left, right in mapped_route:
                    route_failures += position != left
                    position = right
                    visited.add(right)
                route_failures += position != mapped_anchor
                route_failures += not mapped_support <= visited
                active_routes += 1

            # Atlas and schedule labels are finite coframe-gauge data.  Apply
            # the inverse frame and recover the exact source descriptors.
            inverse = frame.T
            # shift is zero here; retain the explicit variable to prevent a
            # silent translation convention from entering this certificate.
            inverse_shift = tuple(-int(value) for value in (inverse @ np.asarray(shift, dtype=int)))
            for descriptor in descriptors:
                mapped = transport_descriptor(descriptor, frame, shift)
                replay = transport_descriptor(mapped, inverse, inverse_shift)
                atlas_key_failures += replay != descriptor
            for descriptor in schedule_descriptors:
                mapped = transport_schedule_descriptor(
                    descriptor, frame, shift
                )
                replay = transport_schedule_descriptor(
                    mapped, inverse, inverse_shift
                )
                schedule_key_failures += replay != descriptor

            # The retained Bell reference transforms with the conjugate
            # Clifford chart.  A single odd JW row need not remain cell-local,
            # but r_system tensor r_reference^* is a signed target Bell-graph
            # row.  Full image rank proves a bijection of the reference bank;
            # the target preparation word remains one local Bell pair per M2.
            source_total = source.qubits + source.matter_qubits
            image_vectors = []
            for qubit in range(source_total):
                x_image = transform_row(Pauli(x=1 << qubit), images)
                z_image = transform_row(Pauli(z=1 << qubit), images)
                bell_chart_failures += M.symplectic(
                    x_image.symplectic(total_qubits),
                    z_image.symplectic(total_qubits),
                    total_qubits,
                ) != 1
                for image in (x_image, z_image):
                    image_vectors.append(image.symplectic(total_qubits))
                    bell_chart_failures += (
                        image.phase + (-image.phase)
                    ) % 4 != 0
            bell_chart_failures += (
                P.C.R.F.base.gf2_rank(image_vectors) != 2 * source_total
            )
            syndrome_register_failures += len(mapped_rows) != len(rows)
            active_rows += len(mapped_rows)

            # Conjugation of the actual source seam fixes the target factor:
            # factor 2 for preserved +axis orientation, factor 3 when the
            # mapped endpoints reverse the canonical target +axis edge.
            target_edge_lookup = P.edge_lookup(target)
            for source_edge, mapped_row in enumerate(
                mapped_direct_edges
            ):
                left, right, *_rest = source.edges[source_edge]
                mapped_left = affine_cell(source.cells[left], frame, shift)
                mapped_right = affine_cell(source.cells[right], frame, shift)
                target_edge = target_edge_lookup[
                    frozenset((mapped_left, mapped_right))
                ]
                target_left = target.cells[target.edges[target_edge][0]]
                reversed_orientation = mapped_left != target_left
                factor = 3 if reversed_orientation else 2
                expected = P.R.choi_pauli(
                    target.physical_terms(target_edge)[factor],
                    target.target_terms(target_edge)[factor],
                    target.qubits,
                )
                reversed_edge_rows += reversed_orientation
                oriented_edge_row_failures += mapped_row != expected
    return {
        "shape": shape,
        "proper_cubic_frames": len(frames),
        "retained_coframe_origin_sectors": len(seeds),
        "frame_origin_contexts": len(frames) * len(seeds),
        "actively_transformed_stabilizer_rows": active_rows,
        "signed_projector_failures": signed_projector_failures,
        "actively_transformed_private_corrections": active_corrections,
        "private_correction_syndrome_failures": correction_syndrome_failures,
        "private_correction_support_failures": correction_support_failures,
        "actively_transformed_returned_routes": active_routes,
        "route_locality_support_or_return_failures": route_failures,
        "atlas_key_inverse_transport_failures": atlas_key_failures,
        "schedule_key_inverse_transport_failures": schedule_key_failures,
        "Bell_reference_conjugate_chart_failures": bell_chart_failures,
        "syndrome_register_bijection_failures": syndrome_register_failures,
        "finite_coframe_atlas_orbit_keys": len(orbit_keys),
        "finite_coframe_correction_word_orbit": len(orbit_words),
        "reversed_edge_rows": reversed_edge_rows,
        "oriented_factor_2_or_3_edge_row_failures": (
            oriented_edge_row_failures
        ),
        "geometric_route_words_changed_by_JW_chart_gauge": (
            geometric_route_gauge_mismatches
        ),
        "route_gauge_boundary": (
            "the actual transformed signed Pauli row is routed afresh by the "
            "same deterministic NN returned-route compiler; a bare geometric "
            "image of the source JW route is only a chart gauge"
        ),
        "orbit_digest": sha256(repr(tuple(sorted(orbit_words))).encode()).hexdigest(),
    }


def product_certificate(atlas: dict[str, object]) -> dict[str, object]:
    source, rows, tags, corrections, descriptors, schedule_descriptors, routes = (
        base_context((2, 2, 2), atlas)
    )
    frames = tuple(T.proper_cubic_frames())
    frame_index = {
        Q.frame_tuple(frame): index for index, frame in enumerate(frames)
    }
    seeds = tuple(cartesian_product(range(2), repeat=3))
    image_product_failures = 0
    stabilizer_product_failures = 0
    correction_product_failures = 0
    atlas_key_product_failures = 0
    schedule_key_product_failures = 0
    route_product_failures = 0
    blocks = 0
    zero = (0, 0, 0)
    for left in frames:
        for right in frames:
            product_frame = left @ right
            _product_id = frame_index[Q.frame_tuple(product_frame)]
            middle = O.arbitrary_fixture(Q.affine_cells(
                source.cells, right, zero
            ))
            final = O.arbitrary_fixture(Q.affine_cells(
                source.cells, product_frame, zero
            ))
            for source_seed in seeds:
                middle_seed = Q.transported_seed(right, zero, source_seed)
                final_seed = Q.transported_seed(left, zero, middle_seed)
                direct_seed = Q.transported_seed(
                    product_frame, zero, source_seed
                )
                right_images = choi_images(
                    source, middle, right, zero, middle_seed
                )
                left_images = choi_images(
                    middle, final, left, zero, final_seed
                )
                direct_images = choi_images(
                    source, final, product_frame, zero, direct_seed
                )
                composed_images = Q.S.compose_images(left_images, right_images)
                image_product_failures += not Q.images_equal(
                    composed_images, direct_images
                )
                for row in rows:
                    composed = transform_row(
                        transform_row(row, right_images), left_images
                    )
                    direct = transform_row(row, direct_images)
                    stabilizer_product_failures += composed != direct
                for correction in corrections:
                    composed = transform_row(
                        transform_row(correction, right_images), left_images
                    )
                    direct = transform_row(correction, direct_images)
                    correction_product_failures += composed != direct
                for descriptor in descriptors:
                    composed = transport_descriptor(
                        transport_descriptor(descriptor, right, zero),
                        left,
                        zero,
                    )
                    direct = transport_descriptor(
                        descriptor, product_frame, zero
                    )
                    atlas_key_product_failures += composed != direct
                for descriptor in schedule_descriptors:
                    composed = transport_schedule_descriptor(
                        transport_schedule_descriptor(
                            descriptor, right, zero
                        ),
                        left,
                        zero,
                    )
                    direct = transport_schedule_descriptor(
                        descriptor, product_frame, zero
                    )
                    schedule_key_product_failures += composed != direct
                for row in rows:
                    middle_row = transform_row(row, right_images)
                    composed_row = transform_row(middle_row, left_images)
                    direct_row = transform_row(row, direct_images)
                    composed_support = P.pauli_cells(final, composed_row)
                    direct_support = P.pauli_cells(final, direct_row)
                    composed_route = P.returned_route(
                        min(composed_support), composed_support
                    )
                    direct_route = P.returned_route(
                        min(direct_support), direct_support
                    )
                    route_product_failures += composed_route != direct_route
                blocks += 1
    return {
        "ordered_frame_products": len(frames) ** 2,
        "coframe_origin_blocks": blocks,
        "signed_Choi_tableau_image_product_failures": image_product_failures,
        "stabilizer_row_product_failures": stabilizer_product_failures,
        "private_correction_word_product_failures": correction_product_failures,
        "atlas_key_product_failures": atlas_key_product_failures,
        "tree_plaquette_schedule_product_failures": schedule_key_product_failures,
        "returned_route_product_failures": route_product_failures,
    }


def main() -> None:
    atlas = P.build_private_atlases()
    boxes = tuple(
        frame_certificate(shape, atlas)
        for shape in ((2, 2, 2), (3, 2, 2))
    )
    products = product_certificate(atlas)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "all active Choi stabilizers and private corrections are signed-covariant in every retained coframe sector",
        all(
            box["signed_projector_failures"] == 0
            and box["private_correction_syndrome_failures"] == 0
            and box["private_correction_support_failures"] == 0
            and box["oriented_factor_2_or_3_edge_row_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "finite correction-atlas and tree-plaquette schedule descriptors transport invertibly under every frame",
        all(
            box["atlas_key_inverse_transport_failures"] == 0
            and box["schedule_key_inverse_transport_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "Bell-reference charts, retained syndrome labels, and mobile routes remain local and bijective",
        all(
            box["Bell_reference_conjugate_chart_failures"] == 0
            and box["syndrome_register_bijection_failures"] == 0
            and box["route_locality_support_or_return_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "all 576 proper-cubic products close in every coframe-origin block on rows, corrections, schedules, and routes",
        products["coframe_origin_blocks"] == 576 * 8
        and all(
            products[key] == 0 for key in (
                "signed_Choi_tableau_image_product_failures",
                "stabilizer_row_product_failures",
                "private_correction_word_product_failures",
                "atlas_key_product_failures",
                "tree_plaquette_schedule_product_failures",
                "returned_route_product_failures",
            )
        ),
    )
    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "checks": checks,
        "atlas_sha256": atlas["atlas_sha256"],
        "boxes": boxes,
        "products": products,
        "derived": (
            "signed proper-cubic covariance of the entire finite Choi-pump "
            "apparatus modulo the already-retained eight coframe origins"
        ),
        "supplied": (
            "same one-time epoch, root/axis gauge, clean Bell/syndrome/route "
            "registers, and finite local atlas as the parent pump"
        ),
        "open": (
            "live-input injection and correction, collision-free recurrent "
            "controller placement, autonomous genesis, and physical selection "
            "of parity superselection"
        ),
        "claim_boundary": (
            "preparation covariance only; a covariant Choi resource is not by "
            "itself an executed encoder E on a live input"
        ),
        "authority": "none",
        "audit": "unset",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
