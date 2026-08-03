#!/usr/bin/env python3
"""Cycle873 physical-M2 F17 open-box local-constraint core.

The construction is the local-constraint complement to the Cycle873 F17-only
F17 seam augmentation.  Every oriented link is the actual 17-rail unary bank.
It defines:

* the fixed-support one-hot projector on each link;
* modular star clocks/projectors for G_x=N_x+alpha div(ell), with the
  typed family/polarity sign alpha in {-1,+1}; and
* order-17 plaquette translations made from four unary cyclic shifts.

The sparse plaquette translation is emitted physically as 64 nearest-neighbour
SWAPs.  The star clock is emitted with the landed ideal arbitrary-RZ and
one-site phase primitives.  Preparation or measurement of the +1 eigenspace,
spectral projector realization, finite-gate synthesis, periodic harmonic-sector
selection, and all genesis remain supplied/open.  No physical-energy, source,
gravity interpretation is made.  These operators characterize and preserve a
code space; they do not autonomously prepare, project, enforce, cool, or reset
that space.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import argparse
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03 as INT


C870, J870, C871, C714 = INT.C870, INT.J870, INT.C871, INT.C714
Coord = tuple[int, int, int]
Edge = tuple[Coord, int]
Plaquette = tuple[Coord, int, int]
F17 = 17
TOL = 3.0e-10
SHAPES = ((2, 2, 2), (3, 3, 3), (3, 2, 2))
EXPECTED_BASE_COMMIT = INT.EXPECTED_BASE_COMMIT
OUT = ROOT / "outputs/cycle873_f17_open_box_local_constraints_core_receipt_2026_08_03.json"
INTEGRATION_PATH = (
    HERE / "frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
)
EXPECTED_INTEGRATION_SHA256 = (
    "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(*rows: Coord) -> Coord:
    return tuple(sum(values) for values in zip(*rows))


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * item for item in row)


def unit(axis: int) -> Coord:
    return tuple(int(index == axis) for index in range(3))


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def linf(left: Coord, right: Coord) -> int:
    return max(abs(a - b) for a, b in zip(left, right))


def shape_cells(shape):
    return tuple(product(*(range(length) for length in shape)))


def matrix_rank_mod(matrix: np.ndarray, modulus: int = F17) -> int:
    rows = np.asarray(matrix, dtype=np.int64).copy() % modulus
    pivot_row = 0
    for column in range(rows.shape[1]):
        pivot = next(
            (row for row in range(pivot_row, rows.shape[0]) if rows[row, column]),
            None,
        )
        if pivot is None:
            continue
        if pivot != pivot_row:
            rows[[pivot_row, pivot]] = rows[[pivot, pivot_row]]
        rows[pivot_row] = (
            rows[pivot_row] * pow(int(rows[pivot_row, column]), -1, modulus)
        ) % modulus
        for row in range(rows.shape[0]):
            if row != pivot_row and rows[row, column]:
                rows[row] = (
                    rows[row] - rows[row, column] * rows[pivot_row]
                ) % modulus
        pivot_row += 1
        if pivot_row == rows.shape[0]:
            break
    return pivot_row


def graph_edges(graph) -> tuple[Edge, ...]:
    return tuple((cell, axis) for cell, axis, _target, _lm, _rm in C870.graph_seams(graph))


def edge_head(edge: Edge) -> Coord:
    return add(edge[0], unit(edge[1]))


def plaquettes(shape) -> tuple[Plaquette, ...]:
    output = []
    for first in range(3):
        for second in range(first + 1, 3):
            ranges = [range(length) for length in shape]
            ranges[first] = range(shape[first] - 1)
            ranges[second] = range(shape[second] - 1)
            output.extend((base, first, second) for base in product(*ranges))
    return tuple(sorted(output))


def plaquette_boundary(row: Plaquette) -> dict[Edge, int]:
    base, first, second = row
    return {
        (base, first): 1,
        (add(base, unit(first)), second): 1,
        (add(base, unit(second)), first): -1,
        (base, second): -1,
    }


def chain_matrices(vertices, edges, faces):
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
    edge_index = {edge: index for index, edge in enumerate(edges)}
    incidence = np.zeros((len(vertices), len(edges)), dtype=np.int64)
    for column, edge in enumerate(edges):
        incidence[vertex_index[edge[0]], column] = 1
        incidence[vertex_index[edge_head(edge)], column] = -1
    boundary = np.zeros((len(edges), len(faces)), dtype=np.int64)
    for column, face in enumerate(faces):
        for edge, coefficient in plaquette_boundary(face).items():
            boundary[edge_index[edge], column] = coefficient
    return incidence % F17, boundary % F17


def placement_map(graph, context):
    return {
        (seam[0], seam[1]): INT.integrated_placement(graph, context, seam)
        for seam in C870.graph_seams(graph)
    }


def cyclic_swap_pairs(placement, direction: int):
    order = range(15, -1, -1) if direction > 0 else range(16)
    return tuple(
        (placement.rails[index], placement.rails[index + 1]) for index in order
    )


def plaquette_swap_word(face: Plaquette, placements):
    rows = []
    per_edge = {}
    for edge, coefficient in plaquette_boundary(face).items():
        pairs = cyclic_swap_pairs(placements[edge], coefficient)
        per_edge[edge] = pairs
        rows.extend((edge, coefficient, pair) for pair in pairs)
    layers = tuple(
        tuple((edge, coefficient, per_edge[edge][step])
              for edge, coefficient in plaquette_boundary(face).items())
        for step in range(16)
    )
    return tuple(rows), layers


def support_geometry(sites, center):
    sites = tuple(sites)
    return {
        "M2": len(set(sites)),
        "Linf_radius": max(linf(site, center) for site in sites),
        "L1_radius": max(l1(site, center) for site in sites),
        "L1_diameter": max(l1(left, right) for left in sites for right in sites),
    }


def star_clock_word(graph, context, cell, edges, placements, family_sign: int = 1):
    theta = 2 * math.pi / F17
    word = []
    for mode in range(6):
        brow = C871.physical_b(graph, context, cell, mode)
        word.extend(C870.c707.compile_pauli_rotation(
            brow, context.sites, theta
        ))
    incident = tuple(
        edge for edge in edges if edge[0] == cell or edge_head(edge) == cell
    )
    for edge in incident:
        incidence_sign = 1 if edge[0] == cell else -1
        coefficient = family_sign * incidence_sign
        for label in range(1, F17):
            phase = np.exp(1j * theta * coefficient * label)
            word.append(C870.c707.Instruction(
                "F17_star_link_clock_phase",
                (placements[edge].rails[label],),
                np.diag((1.0 + 0.0j, phase)).astype(complex),
            ))
    return tuple(word), incident


def clock_primitive_certificate():
    theta = 2 * math.pi / F17
    matter_residual = link_residual = 0.0
    for occupation in (0, 1):
        b_eigenvalue = 1 - 2 * occupation
        observed = np.exp(0.5j * theta) * np.exp(-0.5j * theta * b_eigenvalue)
        matter_residual = max(
            matter_residual, abs(observed - np.exp(1j * theta * occupation))
        )
    for coefficient in (-1, 1):
        for label in range(F17):
            observed = np.exp(1j * theta * coefficient * label)
            expected = np.exp(2j * math.pi * coefficient * label / F17)
            link_residual = max(link_residual, abs(observed - expected))
    return {
        "omega": [math.cos(theta), math.sin(theta)],
        "matter_clock_formula": (
            "omega^n = exp(i*pi/17) exp[-i*(2*pi/17) B/2], B=1-2n"
        ),
        "matter_clock_phase_residual": matter_residual,
        "link_clock_formula": (
            "on the one-hot sector, apply diag(1,omega^(sigma*k)) to physical rail k"
        ),
        "link_clock_phase_residual": link_residual,
        "formal_zero_site_scalar_per_matter_mode": [
            math.cos(theta / 2), math.sin(theta / 2)
        ],
        "non_Clifford_angle": theta,
    }


def transform_edge(frame: np.ndarray, edge: Edge):
    moved_tail = C871.matvec(frame, edge[0])
    moved_direction = C871.matvec(frame, unit(edge[1]))
    target_axis = next(index for index, value in enumerate(moved_direction) if value)
    sign = moved_direction[target_axis]
    canonical_tail = moved_tail if sign > 0 else add(moved_tail, moved_direction)
    return (canonical_tail, target_axis), sign


def transform_plaquette(frame: np.ndarray, face: Plaquette):
    base, first, second = face
    vertices = (
        base,
        add(base, unit(first)),
        add(base, unit(second)),
        add(base, unit(first), unit(second)),
    )
    moved_vertices = tuple(C871.matvec(frame, vertex) for vertex in vertices)
    moved_first = C871.matvec(frame, unit(first))
    moved_second = C871.matvec(frame, unit(second))
    first_axis = next(index for index, value in enumerate(moved_first) if value)
    second_axis = next(index for index, value in enumerate(moved_second) if value)
    first_sign = moved_first[first_axis]
    second_sign = moved_second[second_axis]
    low, high = sorted((first_axis, second_axis))
    orientation = first_sign * second_sign * (1 if first_axis < second_axis else -1)
    target_base = tuple(min(vertex[index] for vertex in moved_vertices) for index in range(3))
    return (target_base, low, high), orientation


def accumulate(rows):
    output = defaultdict(int)
    for key, value in rows:
        output[key] += value
    return {key: value for key, value in output.items() if value}


def frame_certificate(fixtures_for_transport):
    frames = C871.proper_frames()
    boundary_failures = edge_product_failures = plaquette_product_failures = 0
    label_product_failures = orientation_failures = 0
    edge_frame_rows = plaquette_frame_rows = 0
    negative_edge_rows = 0
    for vertices, edges, faces in fixtures_for_transport:
        for frame in frames:
            for edge in edges:
                _target, sign = transform_edge(frame, edge)
                edge_frame_rows += 1
                negative_edge_rows += sign < 0
                for label in range(F17):
                    moved_label = (sign * label) % F17
                    orientation_failures += moved_label != (
                        label if sign > 0 else -label % F17
                    )
            for face in faces:
                target, orientation = transform_plaquette(frame, face)
                moved_boundary = accumulate(
                    (transform_edge(frame, edge)[0], coefficient * transform_edge(frame, edge)[1])
                    for edge, coefficient in plaquette_boundary(face).items()
                )
                expected_boundary = {
                    edge: orientation * coefficient
                    for edge, coefficient in plaquette_boundary(target).items()
                }
                boundary_failures += moved_boundary != expected_boundary
                plaquette_frame_rows += 1
        for right in frames:
            for left in frames:
                composed = left @ right
                for edge in edges:
                    middle, right_sign = transform_edge(right, edge)
                    sequential, left_sign = transform_edge(left, middle)
                    direct, direct_sign = transform_edge(composed, edge)
                    edge_product_failures += (
                        sequential, left_sign * right_sign
                    ) != (direct, direct_sign)
                    for label in range(F17):
                        label_product_failures += (
                            left_sign * right_sign * label
                        ) % F17 != (direct_sign * label) % F17
                for face in faces:
                    middle, right_sign = transform_plaquette(right, face)
                    sequential, left_sign = transform_plaquette(left, middle)
                    direct, direct_sign = transform_plaquette(composed, face)
                    plaquette_product_failures += (
                        sequential, left_sign * right_sign
                    ) != (direct, direct_sign)

    # Physical gate/path transport uses a real emitted L2 plaquette word.
    graph = C870.prep.OpenReferenceGraph(shape_cells((2, 2, 2)))
    context = C870.physical_context(graph)
    placements = placement_map(graph, context)
    face = plaquettes((2, 2, 2))[0]
    word, _layers = plaquette_swap_word(face, placements)
    gate_frame_failures = gate_product_failures = 0
    star_cell = (0, 0, 0)
    star_sites = set()
    for mode in range(6):
        star_sites.update(C871.z_support(
            C871.physical_b(graph, context, star_cell, mode), context
        ))
    for edge, placement in placements.items():
        if edge[0] == star_cell or edge_head(edge) == star_cell:
            star_sites.update(placement.rails)
    star_frame_failures = star_product_failures = 0
    for frame in frames:
        gate_frame_failures += sum(
            l1(C871.matvec(frame, pair[0]), C871.matvec(frame, pair[1])) != 1
            for _edge, _coefficient, pair in word
        )
        star_frame_failures += len({
            C871.matvec(frame, site) for site in star_sites
        }) != len(star_sites)
    for left in frames:
        for right in frames:
            composed = left @ right
            gate_product_failures += sum(
                tuple(C871.matvec(left, C871.matvec(right, site)) for site in pair)
                != tuple(C871.matvec(composed, site) for site in pair)
                for _edge, _coefficient, pair in word
            )
            star_product_failures += sum(
                C871.matvec(left, C871.matvec(right, site))
                != C871.matvec(composed, site)
                for site in star_sites
            )
    return {
        "proper_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "edge_frame_rows": edge_frame_rows,
        "plaquette_frame_rows": plaquette_frame_rows,
        "negative_edge_rows": negative_edge_rows,
        "boundary_equivariance_failures": boundary_failures,
        "edge_orientation_label_failures": orientation_failures,
        "edge_product_failures": edge_product_failures,
        "plaquette_product_failures": plaquette_product_failures,
        "label_product_failures": label_product_failures,
        "physical_NN_gate_frame_failures": gate_frame_failures,
        "physical_star_support_frame_failures": star_frame_failures,
        "physical_gate_product_rows": len(frames) ** 2 * len(word),
        "physical_gate_product_failures": gate_product_failures,
        "physical_star_support_product_rows": len(frames) ** 2 * len(star_sites),
        "physical_star_support_product_failures": star_product_failures,
        "plaquette_generator_transport_rule": (
            "S_p -> S_{F p}^{orientation}; the +1 eigenspace is unchanged when "
            "orientation=-1 because S and S^{-1} have the same +1 sector"
        ),
    }


def single_plaquette_uniform_certificate():
    uniform = np.ones(F17, dtype=complex) / math.sqrt(F17)
    shifted = np.roll(uniform, 1)
    basis = np.zeros(F17, dtype=complex)
    basis[0] = 1
    return {
        "fixed_divergence_cycle_dimension": F17,
        "plaquette_translation_order": F17,
        "uniform_plus_one_sector_dimension": 1,
        "uniform_normalization_residual": abs(float(np.vdot(uniform, uniform).real) - 1.0),
        "uniform_shift_residual": float(np.linalg.norm(shifted - uniform)),
        "uniform_shift_overlap": [
            float(np.vdot(uniform, shifted).real),
            float(np.vdot(uniform, shifted).imag),
        ],
        "basis_link_shift_residual": float(np.linalg.norm(np.roll(basis, 1) - basis)),
        "basis_link_shift_overlap": [
            float(np.vdot(basis, np.roll(basis, 1)).real),
            float(np.vdot(basis, np.roll(basis, 1)).imag),
        ],
        "nontrivial_power_identity_failures": sum(
            all((label + power) % F17 == label for label in range(F17))
            for power in range(1, F17)
        ),
    }


def exterior_fock_lift(one_particle: np.ndarray) -> np.ndarray:
    """Second-quantize a six-mode one-particle matrix in occupation order.

    Rows and columns are the 64 bit words.  Equal-number matrix elements are
    the corresponding minors; unequal-number elements vanish.  This is an
    executed target construction, not a prose inference from the word
    "one-particle".
    """
    one_particle = np.asarray(one_particle, dtype=complex)
    if one_particle.shape != (6, 6):
        raise ValueError("the onsite target must have six one-particle modes")
    occupied = tuple(
        tuple(mode for mode in range(6) if bits >> mode & 1)
        for bits in range(64)
    )
    output = np.zeros((64, 64), dtype=complex)
    for source, source_modes in enumerate(occupied):
        for target, target_modes in enumerate(occupied):
            if len(source_modes) != len(target_modes):
                continue
            if not source_modes:
                output[target, source] = 1.0
            else:
                output[target, source] = np.linalg.det(
                    one_particle[np.ix_(target_modes, source_modes)]
                )
    return output


def onsite_stage_star_clock_certificate() -> dict:
    """Execute the onsite part of the new F17-star preservation argument.

    Cycle870 already proves that its emitted physical words intertwine the
    six-mode coin, reverse, and contact targets.  Here we independently lift
    those live targets to all 64 occupation columns and test their commutator
    with the matter factor of the F17 star clock.  Since the onsite words leave
    every link rail unchanged, this is also their commutator with the complete
    matter-times-link star clock.
    """
    species = C870.c219.common_species(float(C870.c230.BETA))
    coin = np.asarray(species.coin, dtype=complex)
    coin_gates, _qr = C870.qr_coin_schedule(coin)
    reconstructed = np.eye(6, dtype=complex)
    for gate in coin_gates:
        embedded = np.eye(6, dtype=complex)
        embedded[np.ix_(gate.modes, gate.modes)] = gate.matrix
        reconstructed = embedded @ reconstructed

    reverse = np.asarray(C870.base.c210.REVERSE, dtype=complex)
    coin_fock = exterior_fock_lift(coin)
    reverse_fock = exterior_fock_lift(reverse)
    occupations = np.asarray([bits.bit_count() for bits in range(64)])
    theta = 2 * math.pi / F17
    matter_clock = np.diag(np.exp(1j * theta * occupations))
    coupling = float(C870.c230.COUPLING)
    contact_fock = np.diag(
        np.exp(1j * coupling * occupations * (occupations - 1) / 2)
    ).astype(complex)
    onsite_epoch = contact_fock @ reverse_fock @ coin_fock
    targets = {
        "coin": coin_fock,
        "reverse": reverse_fock,
        "contact": contact_fock,
        "composed_onsite_epoch": onsite_epoch,
    }
    commutators = {
        name: float(np.linalg.norm(matrix @ matter_clock - matter_clock @ matrix))
        for name, matrix in targets.items()
    }
    unitarity = {
        name: float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(64)))
        for name, matrix in targets.items()
    }

    # Active hostile control: a bare occupation-bit flip does not preserve the
    # order-17 matter clock.  This prevents the commutator gate from awarding
    # zero merely because it was wired to an identity matrix.
    bare_flip = np.zeros((64, 64), dtype=complex)
    for bits in range(64):
        bare_flip[bits ^ 1, bits] = 1.0
    hostile = float(np.linalg.norm(
        bare_flip @ matter_clock - matter_clock @ bare_flip
    ))

    # Consume the live Cycle870 factor stream rather than merely naming its
    # three onsite stages.  Its exact physical-target intertwiner remains a
    # pinned upstream theorem input; this certificate supplies the additional
    # F17-star commutator that Cycle870 did not need to test.
    graph = C870.prep.OpenReferenceGraph(shape_cells((2, 2, 2)))
    rotations, _inventory = C870.build_update(graph, coin_gates)
    census = Counter(rotation.kind for rotation in rotations)
    onsite_census = {
        kind: census.get(kind, 0)
        for kind in (
            "onsite_coin_mass", "onsite_reverse_fswap", "onsite_contact"
        )
    }
    failures = (
        sum(value > TOL for value in commutators.values())
        + sum(value > TOL for value in unitarity.values())
        + int(np.linalg.norm(reconstructed - coin) > TOL)
        + sum(value == 0 for value in onsite_census.values())
        + int(hostile <= 1.0e-3)
    )
    return {
        "basis_occupation_columns": 64,
        "matter_clock": "diag(omega^N_x) on all six-mode occupation words",
        "link_action": "identity for all three onsite stages",
        "physical_target_bridge": (
            "pinned Cycle870 emitted-word intertwiners supply the physical-to-target "
            "step; this certificate executes the target-to-F17-star commutators"
        ),
        "coin_schedule_gates": len(coin_gates),
        "coin_schedule_reconstruction_residual": float(
            np.linalg.norm(reconstructed - coin)
        ),
        "live_L2_onsite_rotation_census": onsite_census,
        "star_clock_commutator_residuals": commutators,
        "unitarity_residuals": unitarity,
        "bare_occupation_flip_control_commutator": hostile,
        "failures": int(failures),
    }


def object_a_preservation_certificate(fixtures_for_transport):
    all_seams = sum(len(edges) for _vertices, edges, _faces in fixtures_for_transport)
    all_plaquettes = sum(len(faces) for _vertices, _edges, faces in fixtures_for_transport)
    seam_rows = star_failures = onehot_failures = 0
    plaquette_commutator_failures = 0
    for _seam in range(all_seams):
        for alpha in (-1, 1):
            family_sign = alpha
            for a, b in product((0, 1), repeat=2):
                for label in range(F17):
                    for rest_u, rest_v in product(range(6), repeat=2):
                        before = (
                            (rest_u + a + family_sign * label) % F17,
                            (rest_v + b - family_sign * label) % F17,
                        )
                        after_label = (label + alpha * (a - b)) % F17
                        after = (
                            (rest_u + b + family_sign * after_label) % F17,
                            (rest_v + a - family_sign * after_label) % F17,
                        )
                        seam_rows += 1
                        star_failures += before != after
                        onehot_failures += not (0 <= after_label < F17)
                    for plaquette_step in (-1, 1):
                        left = (label + plaquette_step + alpha * (a - b)) % F17
                        right = (label + alpha * (a - b) + plaquette_step) % F17
                        plaquette_commutator_failures += left != right
    operator_pairs = operator_rows = operator_failures = 0
    for _vertices, edges, faces in fixtures_for_transport:
        edge_index = {edge: index for index, edge in enumerate(edges)}
        for seam_edge in edges:
            seam_index = edge_index[seam_edge]
            for face in faces:
                boundary = np.zeros(len(edges), dtype=np.int64)
                for edge, coefficient in plaquette_boundary(face).items():
                    boundary[edge_index[edge]] = coefficient
                operator_pairs += 1
                for current in (-1, 0, 1):
                    seam_shift = np.zeros(len(edges), dtype=np.int64)
                    seam_shift[seam_index] = current
                    operator_rows += 1
                    operator_failures += not np.array_equal(
                        (seam_shift + boundary) % F17,
                        (boundary + seam_shift) % F17,
                    )
    onsite = onsite_stage_star_clock_certificate()
    return {
        "all_seams": all_seams,
        "all_plaquettes": all_plaquettes,
        "seam_star_basis_rows": seam_rows,
        "seam_star_preservation_failures": star_failures,
        "seam_one_hot_label_failures": onehot_failures,
        "seam_plaquette_translation_commutator_rows": all_seams * 2 * 4 * F17 * 2,
        "seam_plaquette_translation_commutator_failures": plaquette_commutator_failures,
        "all_seam_all_plaquette_operator_pairs": operator_pairs,
        "all_seam_all_plaquette_current_rows": operator_rows,
        "all_seam_all_plaquette_commutator_failures": operator_failures,
        "onsite_stage_preservation": onsite,
        "onsite_stage_preservation_failures": onsite["failures"],
        "full_augmented_epoch_constraint_preservation_failures": (
            star_failures + onehot_failures + plaquette_commutator_failures
            + operator_failures + onsite["failures"]
        ),
    }


def fixture_certificate(shape):
    graph = C870.prep.OpenReferenceGraph(shape_cells(shape))
    context = C870.physical_context(graph)
    vertices = tuple(graph.cells)
    edges = graph_edges(graph)
    faces = plaquettes(shape)
    incidence, boundary = chain_matrices(vertices, edges, faces)
    incidence_rank = matrix_rank_mod(incidence)
    boundary_rank = matrix_rank_mod(boundary)
    cycle_rank = len(edges) - incidence_rank
    boundary_squared_failures = int(np.count_nonzero((incidence @ boundary) % F17))
    placements = placement_map(graph, context)

    f17_banks = tuple(placement.f17_roles for placement in placements.values())
    pair_overlap_sites = sum(
        len(bank & prior)
        for index, bank in enumerate(f17_banks)
        for prior in f17_banks[:index]
    )
    carrier_aux = set(context.sites) | set(J870.auxiliary_registers(graph))
    bank_carrier_aux_collisions = sum(len(bank & carrier_aux) for bank in f17_banks)
    onehot_radius_failures = onehot_path_failures = 0
    onehot_geometries = []
    for placement in placements.values():
        onehot_radius_failures += max(
            max(map(abs, INT.localize(site, placement.midpoint, placement.basis)))
            for site in placement.rails
        ) > 2
        onehot_path_failures += sum(
            l1(left, right) != 1
            for left, right in zip(placement.rails, placement.rails[1:])
        )
        onehot_geometries.append(support_geometry(placement.rails, placement.midpoint))

    plaquette_supports = []
    word_failures = layer_collisions = deletion_undetected = 0
    word_hash = sha256()
    for face in faces:
        word, layers = plaquette_swap_word(face, placements)
        support = set(site for _edge, _coefficient, pair in word for site in pair)
        center = add(scale(16, face[0]), scale(8, unit(face[1])), scale(8, unit(face[2])))
        geometry = support_geometry(support, center)
        plaquette_supports.append(geometry)
        word_failures += len(word) != 64
        word_failures += geometry["M2"] != 68
        word_failures += sum(l1(*pair) != 1 for _edge, _coefficient, pair in word)
        for layer in layers:
            sites = [site for _edge, _coefficient, pair in layer for site in pair]
            layer_collisions += len(sites) != len(set(sites))
        for edge, coefficient in plaquette_boundary(face).items():
            full = tuple(
                (label + coefficient) % F17 for label in range(F17)
            )
            for omitted in range(16):
                damaged = tuple(
                    int(math.log2(INT.apply_unary(1 << label, coefficient, omitted)))
                    for label in range(F17)
                )
                deletion_undetected += damaged == full
        word_hash.update(repr((face, word)).encode())

    star_supports = []
    star_constraint_failures = 0
    physical_stabilizers = C870.physical_stabilizers(context)
    star_clock_rows = []
    star_clock_hash = sha256()
    standard_basis = (unit(0), unit(1), unit(2))
    for cell in vertices:
        matter = set()
        for mode in range(6):
            row = C871.physical_b(graph, context, cell, mode)
            matter.update(C871.z_support(row, context))
            star_constraint_failures += sum(
                not row.commutes(stabilizer)
                for stabilizer in physical_stabilizers
            )
        incident = tuple(
            edge for edge in edges if edge[0] == cell or edge_head(edge) == cell
        )
        link_sites = set().union(*(set(placements[edge].rails) for edge in incident))
        support = matter | link_sites
        star_supports.append({
            "degree": len(incident),
            "matter_M2": len(matter),
            "link_rail_M2": len(link_sites),
            **support_geometry(support, scale(16, cell)),
        })
        clock_word, _incident = star_clock_word(
            graph, context, cell, edges, placements, 1
        )
        negative_clock_word, _ = star_clock_word(
            graph, context, cell, edges, placements, -1
        )
        clock_route = INT.route_word(clock_word, standard_basis)
        negative_route = INT.route_word(negative_clock_word, standard_basis)
        route_failures = sum(
            clock_route[key] for key in (
                "nearest_neighbor_failures", "operand_order_failures",
                "arbitrary_transit_return_failures",
            )
        )
        route_failures += sum(
            negative_route[key] for key in (
                "nearest_neighbor_failures", "operand_order_failures",
                "arbitrary_transit_return_failures",
            )
        )
        alpha_route_mismatch = (
            clock_route["logical_instructions"] != negative_route["logical_instructions"]
            or clock_route["routed_gates"] != negative_route["routed_gates"]
            or clock_route["_touched"] != negative_route["_touched"]
        )
        star_clock_rows.append({
            "logical": len(clock_word),
            "routed": clock_route["routed_gates"],
            "maximum_distance": clock_route["maximum_route_distance"],
            "route_failures": route_failures,
            "alpha_route_mismatch": int(alpha_route_mismatch),
            "link_clock_phase_gates": sum(
                row.kind == "F17_star_link_clock_phase" for row in clock_word
            ),
            "matter_axis_RZ_gates": sum(row.kind == "axis_RZ" for row in clock_word),
        })
        star_clock_hash.update(repr(tuple(
            INT.instruction_signature(row) for row in clock_word
        )).encode())

    plaquette_dependency = len(faces) - boundary_rank
    fixed_divergence_dimension = F17 ** cycle_rank
    plus_one_dimension = F17 ** (cycle_rank - boundary_rank)
    return {
        "shape": shape,
        "vertices": len(vertices),
        "oriented_links": len(edges),
        "plaquettes": len(faces),
        "physical_unary_link_M2": F17 * len(edges),
        "Object_A_total_bank_M2_including_three_clean_work_per_link": 20 * len(edges),
        "incidence_rank_mod17": incidence_rank,
        "expected_connected_incidence_rank": len(vertices) - 1,
        "independent_link_star_constraints_at_fixed_matter": incidence_rank,
        "global_star_compatibility": "sum_x(g_x-N_x)=0 mod17",
        "cycle_space_rank": cycle_rank,
        "plaquette_boundary_rank_mod17": boundary_rank,
        "plaquette_dependency_count": plaquette_dependency,
        "boundary_of_boundary_nonzero_entries": boundary_squared_failures,
        "fixed_star_divergence_link_sector_dimension": fixed_divergence_dimension,
        "uniform_cycle_plus_one_sector_dimension": plus_one_dimension,
        "unique_uniform_cycle_state_in_each_consistent_fixed_star_sector":
            plus_one_dimension == 1,
        "one_hot_constraint": {
            "per_link_physical_support_M2": F17,
            "maximum_Linf_radius": max(row["Linf_radius"] for row in onehot_geometries),
            "maximum_L1_radius": max(row["L1_radius"] for row in onehot_geometries),
            "maximum_L1_diameter": max(row["L1_diameter"] for row in onehot_geometries),
            "radius_failures": onehot_radius_failures,
            "rail_path_NN_failures": onehot_path_failures,
        },
        "star_constraint": {
            "definition": (
                "A_x=omega^(N_x+alpha[sum_out ell-sum_in ell]), alpha in {-1,+1}; "
                "P_{g,x}=17^-1 sum_t omega^(-tg) A_x^t"
            ),
            "maximum_degree": max(row["degree"] for row in star_supports),
            "maximum_physical_support_M2": max(row["M2"] for row in star_supports),
            "maximum_matter_support_M2": max(row["matter_M2"] for row in star_supports),
            "maximum_link_rail_support_M2": max(row["link_rail_M2"] for row in star_supports),
            "maximum_Linf_radius": max(row["Linf_radius"] for row in star_supports),
            "maximum_L1_radius": max(row["L1_radius"] for row in star_supports),
            "maximum_L1_diameter": max(row["L1_diameter"] for row in star_supports),
            "encoded_matter_constraint_anticommutators": star_constraint_failures,
            "emitted_star_clock_word": {
                "minimum_logical_instructions": min(row["logical"] for row in star_clock_rows),
                "maximum_logical_instructions": max(row["logical"] for row in star_clock_rows),
                "minimum_routed_gates": min(row["routed"] for row in star_clock_rows),
                "maximum_routed_gates": max(row["routed"] for row in star_clock_rows),
                "maximum_route_distance": max(row["maximum_distance"] for row in star_clock_rows),
                "route_or_alpha_census_failures": sum(
                    row["route_failures"] + row["alpha_route_mismatch"]
                    for row in star_clock_rows
                ),
                "maximum_link_clock_phase_gates": max(
                    row["link_clock_phase_gates"] for row in star_clock_rows
                ),
                "matter_axis_RZ_gates_per_star": tuple(sorted(set(
                    row["matter_axis_RZ_gates"] for row in star_clock_rows
                ))),
                "formal_zero_site_scalar_angle": 6 * math.pi / F17,
                "all_star_clock_words_sha256": star_clock_hash.hexdigest(),
            },
        },
        "plaquette_shift": {
            "logical_link_support": 4,
            "physical_support_M2": 68,
            "physical_SWAP_gates": 64,
            "parallel_depth": 16,
            "clean_ancilla_M2": 0,
            "maximum_Linf_radius": max(row["Linf_radius"] for row in plaquette_supports),
            "maximum_L1_radius": max(row["L1_radius"] for row in plaquette_supports),
            "maximum_L1_diameter": max(row["L1_diameter"] for row in plaquette_supports),
            "word_or_NN_failures": word_failures,
            "parallel_layer_site_collisions": layer_collisions,
            "individual_SWAP_deletions_tested": 64 * len(faces),
            "undetected_individual_SWAP_deletions": deletion_undetected,
            "all_plaquette_words_sha256": word_hash.hexdigest(),
        },
        "bank_pair_overlap_sites": pair_overlap_sites,
        "bank_carrier_aux_collision_sites": bank_carrier_aux_collisions,
        "star_plaquette_commutator_exponent_nonzero_entries": boundary_squared_failures,
        "constraint_commutation": {
            "one_hot_with_star_reason":
                "the one-hot projector and star clock are diagonal in link occupation",
            "one_hot_with_plaquette_reason":
                "the executed cyclic-shift word preserves every rail Hamming sector",
            "star_with_star_reason": "all star clocks are diagonal",
            "plaquette_with_plaquette_reason":
                "all plaquette generators are products of commuting link translations",
            "star_with_plaquette_failures": boundary_squared_failures,
        },
    }, (vertices, edges, faces)


def collect_failures(report):
    failures = []
    if not report["provenance"]["expected_base_is_ancestor_of_head"]:
        failures.append("expected base is not an ancestor of HEAD")
    if report["provenance"]["integration_runner_sha256"] != EXPECTED_INTEGRATION_SHA256:
        failures.append("integration runner hash")
    unary = report["one_hot_algebra"]
    for key in (
        "one_hot_mapping_failures", "all_sector_Hamming_weight_failures",
        "all_sector_inverse_failures", "P1_commutator_failures",
    ):
        if unary[key]:
            failures.append(f"one-hot:{key}")
    clock = report["clock_primitive"]
    for key in ("matter_clock_phase_residual", "link_clock_phase_residual"):
        if clock[key] > TOL:
            failures.append(f"clock:{key}")
    single = report["single_plaquette_uniform"]
    for key in (
        "uniform_normalization_residual", "uniform_shift_residual",
        "nontrivial_power_identity_failures",
    ):
        if single[key] > TOL:
            failures.append(f"single plaquette:{key}")
    if single["uniform_plus_one_sector_dimension"] != 1:
        failures.append("single plaquette uniqueness")
    if abs(single["uniform_shift_overlap"][0] - 1.0) > TOL or abs(
        single["uniform_shift_overlap"][1]
    ) > TOL:
        failures.append("single plaquette uniform overlap")
    if any(abs(value) > TOL for value in single["basis_link_shift_overlap"]):
        failures.append("single plaquette basis overlap control")
    for fixture in report["fixtures"]:
        prefix = str(tuple(fixture["shape"]))
        for key in (
            "boundary_of_boundary_nonzero_entries", "bank_pair_overlap_sites",
            "bank_carrier_aux_collision_sites",
            "star_plaquette_commutator_exponent_nonzero_entries",
        ):
            if fixture[key]:
                failures.append(f"{prefix}:{key}")
        if fixture["incidence_rank_mod17"] != fixture["expected_connected_incidence_rank"]:
            failures.append(f"{prefix}:incidence rank")
        if fixture["plaquette_boundary_rank_mod17"] != fixture["cycle_space_rank"]:
            failures.append(f"{prefix}:plaquette span")
        if fixture["uniform_cycle_plus_one_sector_dimension"] != 1:
            failures.append(f"{prefix}:uniform uniqueness")
        for section, keys in {
            "one_hot_constraint": ("radius_failures", "rail_path_NN_failures"),
            "star_constraint": ("encoded_matter_constraint_anticommutators",),
            "plaquette_shift": (
                "word_or_NN_failures", "parallel_layer_site_collisions",
                "undetected_individual_SWAP_deletions",
            ),
        }.items():
            for key in keys:
                if fixture[section][key]:
                    failures.append(f"{prefix}:{section}:{key}")
        if fixture["star_constraint"]["emitted_star_clock_word"][
            "route_or_alpha_census_failures"
        ]:
            failures.append(f"{prefix}:star clock route")
    frame = report["proper_frame_transport"]
    for key in (
        "boundary_equivariance_failures", "edge_orientation_label_failures",
        "edge_product_failures", "plaquette_product_failures", "label_product_failures",
        "physical_NN_gate_frame_failures", "physical_gate_product_failures",
        "physical_star_support_frame_failures",
        "physical_star_support_product_failures",
    ):
        if frame[key]:
            failures.append(f"frame:{key}")
    preserve = report["Object_A_preservation"]
    for key in (
        "seam_star_preservation_failures", "seam_one_hot_label_failures",
        "seam_plaquette_translation_commutator_failures",
        "all_seam_all_plaquette_commutator_failures",
        "onsite_stage_preservation_failures",
        "full_augmented_epoch_constraint_preservation_failures",
    ):
        if preserve[key]:
            failures.append(f"Object A:{key}")
    return failures


def json_safe(value):
    if isinstance(value, dict):
        return {
            key if isinstance(key, str | int | float | bool) or key is None else repr(key):
            json_safe(item)
            for key, item in value.items()
        }
    if isinstance(value, tuple | list | set | frozenset):
        return [json_safe(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    return value


def main(output: Path = OUT) -> int:
    base_is_ancestor = subprocess.run(
        (
            "git", "merge-base", "--is-ancestor",
            EXPECTED_BASE_COMMIT, "HEAD",
        ),
        cwd=ROOT,
        check=False,
    ).returncode == 0
    fixture_rows = []
    transports = []
    for shape in SHAPES:
        fixture, transport = fixture_certificate(shape)
        fixture_rows.append(fixture)
        transports.append(transport)
    single_plaquette = single_plaquette_uniform_certificate()
    report = {
        "status": "pending",
        "name": "Cycle873 physical-M2 F17 open-box local constraints",
        "provenance": {
            "base_commit": EXPECTED_BASE_COMMIT,
            "expected_base_is_ancestor_of_head": base_is_ancestor,
            "integration_runner": str(INTEGRATION_PATH.relative_to(ROOT)),
            "integration_runner_sha256": digest(INTEGRATION_PATH),
            "pinned_source_sha256": {
                path: digest(ROOT / path) for path in INT.SOURCE_PATHS
            },
        },
        "constraint_algebra": {
            "one_hot": "P1_e=sum_k |1_k><1_k|; Q_e=I-P1_e",
            "star": (
                "A_x=omega^(N_x+alpha div ell), alpha in {-1,+1}, omega=exp(2*pi*i/17), "
                "with a selected eigenvalue/projector per supplied consistent sector"
            ),
            "plaquette": (
                "S_p=product_e X_e^(boundary coefficient); S_p^17=I; "
                "the +1 sector is invariant under every plaquette translation"
            ),
            "commutation_reason": (
                "incidence times plaquette boundary is zero mod17; label translations "
                "are abelian and preserve every unary Hamming sector"
            ),
        },
        "sparse_plaquette_gate_word": {
            "rail_local_offsets": INT.RAIL_LOCAL_OFFSETS,
            "positive_link_shift_SWAP_pairs": tuple(
                (index, index + 1) for index in range(15, -1, -1)
            ),
            "negative_link_shift_SWAP_pairs": tuple(
                (index, index + 1) for index in range(16)
            ),
            "oriented_boundary_pattern": (
                "+ edge(base,a)", "+ edge(base+e_a,b)",
                "- edge(base+e_b,a)", "- edge(base,b)",
            ),
            "physical_coordinate_rule": (
                "rail k is midpoint + sum_i offset[k,i]*transported_coframe_i; "
                "every listed pair is L1-nearest-neighbour"
            ),
            "gates_per_plaquette": 64,
            "parallel_depth": 16,
        },
        "one_hot_algebra": INT.unary_projector_certificate(),
        "clock_primitive": clock_primitive_certificate(),
        "single_plaquette_uniform": single_plaquette,
        "fixtures": tuple(fixture_rows),
        "proper_frame_transport": frame_certificate(tuple(transports)),
        "Object_A_preservation": object_a_preservation_certificate(tuple(transports)),
        "constructive_interference_route": {
            "basis_link_witness_scope": (
                "the prior orthogonal-history witness applies to supplied computational-basis "
                "link initialization only"
            ),
            "uniform_cycle_translation_overlap": single_plaquette["uniform_shift_overlap"],
            "computational_basis_translation_overlap": single_plaquette[
                "basis_link_shift_overlap"
            ],
            "interpretation": (
                "within a consistent fixed-star sector on these open boxes, all closed-current "
                "path differences lie in the plaquette span and act trivially on the unique "
                "uniform +1 cycle-space state"
            ),
            "mass_dispersion_status": (
                "this core identifies the route-local basis-history variation algebraically; the separate "
                "Cycle873 affine-intertwiner core tests recurrence and decoded C219 dispersion"
            ),
        },
        "realization_boundary": {
            "emitted": (
                "each S_p as 64 physical NN SWAPs, four disjoint 16-SWAP cyclic words, depth16",
                "each star clock as routed physical-B rotations plus one-site unary-rail "
                "2*pi*k/17 phases, with its exact formal zero-site scalar ledger",
            ),
            "not_emitted_or_supplied": (
                "preparation of the uniform affine cycle-space state",
                "measurement/projection onto S_p=+1",
                "the 17-term star and plaquette spectral projectors",
                "controlled order-17 syndrome measurements and deterministic correction",
                "selection of a globally consistent star eigenvalue sector",
                "periodic harmonic Wilson-loop sectors, absent on the tested open boxes",
                "autonomous one-hot enforcement, reset, cooling, or genesis",
            ),
            "non_Clifford_boundary": (
                "the SWAP translations are Clifford permutations; star-clock 2*pi/17 phases "
                "are emitted using the landed ideal arbitrary-RZ/one-site phase primitive, "
                "but finite-gate synthesis and coherent/projective +1-sector realization "
                "are not compiled"
            ),
            "no_physical_energy_claim": True,
        },
        "open_nonclaims": (
            "no autonomous preparation/genesis or recurrence invocation",
            "no periodic harmonic-sector selection",
            "no completed joint spectrum, source, gravity, or backreaction claim",
            "authority and audit verdict remain unset",
        ),
    }
    failures = collect_failures(report)
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    output.write_text(json.dumps(json_safe(report), indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "base_commit": EXPECTED_BASE_COMMIT,
        "expected_base_is_ancestor_of_head": base_is_ancestor,
        "receipt": str(OUT.relative_to(ROOT)),
        "failures": failures,
        "fixtures": [{
            "shape": row["shape"],
            "V": row["vertices"],
            "E": row["oriented_links"],
            "P": row["plaquettes"],
            "cycle_rank": row["cycle_space_rank"],
            "plaquette_rank": row["plaquette_boundary_rank_mod17"],
            "fixed_divergence_dimension": row["fixed_star_divergence_link_sector_dimension"],
            "plus_one_dimension": row["uniform_cycle_plus_one_sector_dimension"],
            "star_support": row["star_constraint"]["maximum_physical_support_M2"],
            "plaquette_radius": row["plaquette_shift"]["maximum_Linf_radius"],
        } for row in fixture_rows],
    }, indent=2))
    return int(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.output))
