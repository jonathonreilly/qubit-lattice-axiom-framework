#!/usr/bin/env python3
"""Cycle 703: one fixed local cellular decoder for open BKSF plaquettes.

The decoder is an axial-gauge prefix recurrence expressed in the transported
proper-cubic coframe.  It uses only radius-one rules and open-boundary seed
bits.  The same rule is iterated to a quiescent fixed point on every box; no
Gaussian table, selected path, or target-dependent correction is supplied.

The rule removes the host-selected correction wall, but its measurement record
and forward-only cellular memory are explicitly classified as dissipative
apparatus resources.  No physical-time meaning is assigned to iteration
rounds, and no autonomous returned-work implementation is claimed.
"""

from __future__ import annotations

from itertools import product
import json

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base
import frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25 as prep


AUDIT_INPUT_PATHS = (
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py",
)


Coord = tuple[int, int, int]
PlaquetteKey = tuple[Coord, tuple[int, int]]
ALL_CLAUSES = frozenset(
    (
        "seed_ay",
        "seed_az",
        "propagate_ay",
        "source_fxy",
        "propagate_az_boundary",
        "source_fyz",
        "propagate_az_x",
        "source_fxz",
        "one_shot_ready_latch",
        "emit_correction",
    )
)


def box_geometry(length: int) -> dict[str, object]:
    return prep.coarse_geometry(tuple(product(range(length), repeat=3)))


def syndrome_values(
    geometry: dict[str, object], syndrome: int
) -> dict[PlaquetteKey, int]:
    plaquettes = geometry["plaquettes"]
    if not isinstance(plaquettes, tuple):
        raise TypeError("malformed plaquettes")
    return {
        (row["anchor"], row["axes"]): (syndrome >> index) & 1
        for index, row in enumerate(plaquettes)
    }


def cellular_decode(
    length: int,
    syndrome: int,
    disabled: frozenset[str] = frozenset(),
) -> dict[str, object]:
    """Iterate the fixed radius-one recurrence to its quiescent state."""

    unknown = disabled - ALL_CLAUSES
    if unknown:
        raise ValueError(("unknown disabled clauses", sorted(unknown)))
    geometry = box_geometry(length)
    fields = syndrome_values(geometry, syndrome)
    edges = geometry["edges"]
    if not isinstance(edges, tuple):
        raise TypeError("malformed edges")
    edge_lookup = {
        (left, axis): index
        for index, (left, _, axis) in enumerate(edges)
    }
    correction = 0
    ay: dict[Coord, int] = {}
    az: dict[Coord, int] = {}
    if "seed_ay" not in disabled:
        for y in range(length - 1):
            for z in range(length):
                ay[(0, y, z)] = 0
    if "seed_az" not in disabled:
        for z in range(length - 1):
            az[(0, 0, z)] = 0

    rounds = 0
    emission_nonquiescence = False
    while True:
        ay_additions: dict[Coord, int] = {}
        az_additions: dict[Coord, int] = {}
        if "propagate_ay" not in disabled:
            for (x, y, z), value in ay.items():
                if x + 1 >= length or (x + 1, y, z) in ay:
                    continue
                source = 0
                if "source_fxy" not in disabled:
                    source = fields[((x, y, z), (0, 1))]
                ay_additions[(x + 1, y, z)] = value ^ source
        if "propagate_az_boundary" not in disabled:
            for (x, y, z), value in az.items():
                if x != 0 or y + 1 >= length or (0, y + 1, z) in az:
                    continue
                source = 0
                if "source_fyz" not in disabled:
                    source = fields[((0, y, z), (1, 2))]
                az_additions[(0, y + 1, z)] = value ^ source
        if "propagate_az_x" not in disabled:
            for (x, y, z), value in az.items():
                if x + 1 >= length or (x + 1, y, z) in az:
                    continue
                source = 0
                if "source_fxz" not in disabled:
                    source = fields[((x, y, z), (0, 2))]
                target = (x + 1, y, z)
                candidate = value ^ source
                if target in az_additions and az_additions[target] != candidate:
                    raise AssertionError(("nonunique az update", target))
                az_additions[target] = candidate
        if not ay_additions and not az_additions:
            if "one_shot_ready_latch" in disabled and any(
                tuple(ay.values()) + tuple(az.values())
            ):
                emission_nonquiescence = True
            break
        if "emit_correction" not in disabled:
            emit_ay = ay_additions
            emit_az = az_additions
            if "one_shot_ready_latch" in disabled:
                emit_ay = ay | ay_additions
                emit_az = az | az_additions
            for anchor, value in emit_ay.items():
                if value:
                    correction ^= 1 << edge_lookup[(anchor, 1)]
            for anchor, value in emit_az.items():
                if value:
                    correction ^= 1 << edge_lookup[(anchor, 2)]
        ay.update(ay_additions)
        az.update(az_additions)
        rounds += 1
        if rounds > 2 * length + 2:
            raise AssertionError(("cellular rule did not quiesce", length))

    expected_ay = length * length * (length - 1)
    expected_az = length * length * (length - 1)
    return {
        "correction": correction,
        "rounds_to_quiescence": rounds,
        "ay_ready": len(ay),
        "az_ready": len(az),
        "expected_ay": expected_ay,
        "expected_az": expected_az,
        "all_work_sites_ready": (
            len(ay) == expected_ay and len(az) == expected_az
        ),
        "emission_nonquiescence": emission_nonquiescence,
        "active_correction_edges": correction.bit_count(),
    }


def cube_bianchi_masks(
    geometry: dict[str, object], length: int
) -> tuple[int, ...]:
    plaquettes = geometry["plaquettes"]
    if not isinstance(plaquettes, tuple):
        raise TypeError("malformed plaquettes")
    lookup = {
        (row["anchor"], row["axes"]): index
        for index, row in enumerate(plaquettes)
    }
    rows = []
    for x, y, z in product(range(length - 1), repeat=3):
        faces = (
            ((x, y, z), (0, 1)),
            ((x, y, z + 1), (0, 1)),
            ((x, y, z), (0, 2)),
            ((x, y + 1, z), (0, 2)),
            ((x, y, z), (1, 2)),
            ((x + 1, y, z), (1, 2)),
        )
        rows.append(sum(1 << lookup[face] for face in faces))
    return tuple(rows)


def box_basis_certificate(length: int) -> dict[str, object]:
    geometry = box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    failures = 0
    incomplete = 0
    nonquiescent = 0
    maximum_rounds = 0
    lawful_bianchi_failures = 0
    columns = []
    syndromes = []
    bianchi = cube_bianchi_masks(geometry, length)
    for edge_index in range(len(edges)):
        syndrome = prep.apply_matrix(masks, 1 << edge_index)
        lawful_bianchi_failures += prep.apply_matrix(bianchi, syndrome) != 0
        decoded = cellular_decode(length, syndrome)
        correction = decoded["correction"]
        failures += prep.apply_matrix(masks, correction) != syndrome
        incomplete += not decoded["all_work_sites_ready"]
        nonquiescent += decoded["emission_nonquiescence"]
        maximum_rounds = max(
            maximum_rounds, decoded["rounds_to_quiescence"]
        )
        columns.append(correction)
        syndromes.append(syndrome)

    linearity_failures = 0
    sample_count = min(64, len(edges) * len(edges))
    for sample in range(sample_count):
        left = (17 * sample + 3) % len(edges)
        right = (29 * sample + 5) % len(edges)
        combined = cellular_decode(
            length, syndromes[left] ^ syndromes[right]
        )["correction"]
        linearity_failures += combined != (columns[left] ^ columns[right])
    return {
        "L": length,
        "cells": length**3,
        "coarse_edges": len(edges),
        "plaquette_checks": len(masks),
        "plaquette_rank": prep.gf2_rank(list(masks)),
        "cube_bianchi_rows": len(bianchi),
        "cube_bianchi_rank": prep.gf2_rank(list(bianchi)),
        "closed_two_form_exponent": len(masks) - prep.gf2_rank(list(bianchi)),
        "image_equals_closed_exponent": (
            prep.gf2_rank(list(masks))
            == len(masks) - prep.gf2_rank(list(bianchi))
        ),
        "lawful_input_bianchi_failures": lawful_bianchi_failures,
        "unit_edge_basis_cases": len(edges),
        "basis_syndrome_failures": failures,
        "incomplete_wavefront_failures": incomplete,
        "emission_nonquiescence_failures": nonquiescent,
        "linearity_pairs_checked": sample_count,
        "linearity_failures": linearity_failures,
        "maximum_rounds_to_quiescence": maximum_rounds,
        "expected_round_formula": 2 * (length - 1),
        "rule_radius": 1,
    }


def exhaustive_l2_certificate() -> dict[str, object]:
    length = 2
    geometry = box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    lawful = {
        prep.apply_matrix(masks, edge_pattern)
        for edge_pattern in range(1 << len(edges))
    }
    failures = 0
    for syndrome in lawful:
        decoded = cellular_decode(length, syndrome)
        failures += (
            prep.apply_matrix(masks, decoded["correction"]) != syndrome
        )
    return {
        "edge_error_patterns_enumerated": 1 << len(edges),
        "distinct_lawful_syndromes": len(lawful),
        "expected_from_rank": 1 << prep.gf2_rank(list(masks)),
        "lawful_syndrome_failures": failures,
    }


def mutation_certificate(length: int = 4) -> dict[str, object]:
    geometry = box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    rows = []
    for clause in sorted(ALL_CLAUSES):
        failures = 0
        incomplete = 0
        nonquiescent = 0
        for edge_index in range(len(edges)):
            syndrome = prep.apply_matrix(masks, 1 << edge_index)
            decoded = cellular_decode(length, syndrome, frozenset((clause,)))
            failures += prep.apply_matrix(
                masks, decoded["correction"]
            ) != syndrome
            incomplete += not decoded["all_work_sites_ready"]
            nonquiescent += decoded["emission_nonquiescence"]
        rows.append(
            {
                "deleted_clause": clause,
                "syndrome_failures": failures,
                "incomplete_wavefronts": incomplete,
                "nonquiescent_emissions": nonquiescent,
                "detected": failures > 0 or incomplete > 0 or nonquiescent > 0,
            }
        )
    return {
        "L": length,
        "unit_edge_cases_per_deletion": len(edges),
        "deletions": tuple(rows),
        "all_active_deletions_detected": all(row["detected"] for row in rows),
    }


def plaquette_vertices(row: dict[str, object]) -> tuple[Coord, ...]:
    anchor = row["anchor"]
    axes = row["axes"]
    if not isinstance(anchor, tuple) or not isinstance(axes, tuple):
        raise TypeError("malformed plaquette")
    first = list(anchor)
    first[axes[0]] += 1
    second = list(anchor)
    second[axes[1]] += 1
    diagonal = list(first)
    diagonal[axes[1]] += 1
    return anchor, tuple(first), tuple(second), tuple(diagonal)


def transform_coord(frame, shift: Coord, cell: Coord) -> Coord:
    return tuple(
        int(sum(int(frame[row, column]) * cell[column] for column in range(3)))
        + shift[row]
        for row in range(3)
    )


def transformed_edge_set(
    geometry: dict[str, object], mask: int, frame, shift: Coord
) -> frozenset[frozenset[Coord]]:
    edges = geometry["edges"]
    if not isinstance(edges, tuple):
        raise TypeError("malformed edges")
    return frozenset(
        frozenset(
            (
                transform_coord(frame, shift, left),
                transform_coord(frame, shift, right),
            )
        )
        for index, (left, right, _) in enumerate(edges)
        if (mask >> index) & 1
    )


def transformed_plaquette_set(
    geometry: dict[str, object], mask: int, frame, shift: Coord
) -> frozenset[frozenset[Coord]]:
    plaquettes = geometry["plaquettes"]
    if not isinstance(plaquettes, tuple):
        raise TypeError("malformed plaquettes")
    return frozenset(
        frozenset(
            transform_coord(frame, shift, vertex)
            for vertex in plaquette_vertices(row)
        )
        for index, row in enumerate(plaquettes)
        if (mask >> index) & 1
    )


def transported_cellular_decode(
    length: int,
    physical_syndrome: frozenset[frozenset[Coord]],
    frame,
    shift: Coord,
) -> frozenset[frozenset[Coord]]:
    """Run the same rule after pulling data into the transported coframe."""

    geometry = box_geometry(length)
    plaquettes = geometry["plaquettes"]
    if not isinstance(plaquettes, tuple):
        raise TypeError("malformed plaquettes")
    pulled = 0
    known = set()
    for index, row in enumerate(plaquettes):
        transformed = frozenset(
            transform_coord(frame, shift, vertex)
            for vertex in plaquette_vertices(row)
        )
        known.add(transformed)
        if transformed in physical_syndrome:
            pulled ^= 1 << index
    if not physical_syndrome <= known:
        raise AssertionError("physical syndrome lies outside transported box")
    correction = cellular_decode(length, pulled)["correction"]
    return transformed_edge_set(geometry, correction, frame, shift)


def covariance_certificate(length: int = 4) -> dict[str, object]:
    geometry = box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    frames = base.proper_cubic_frames()
    shifts = ((0, 0, 0), (7, -5, 11))
    failures = 0
    direct_rule_transport_failures = 0
    cases = 0
    transformed_box_size_failures = 0
    canonical_cells = tuple(product(range(length), repeat=3))
    for frame in frames:
        for shift in shifts:
            transformed_cells = {
                transform_coord(frame, shift, cell) for cell in canonical_cells
            }
            transformed_box_size_failures += len(transformed_cells) != length**3
            for edge_index in range(len(edges)):
                syndrome = prep.apply_matrix(masks, 1 << edge_index)
                correction = cellular_decode(length, syndrome)["correction"]
                physical_syndrome = transformed_plaquette_set(
                    geometry, syndrome, frame, shift
                )
                expected_correction = transformed_edge_set(
                    geometry, correction, frame, shift
                )
                direct_rule_transport_failures += transported_cellular_decode(
                    length, physical_syndrome, frame, shift
                ) != expected_correction
                observed = prep.apply_matrix(masks, correction)
                failures += transformed_plaquette_set(
                    geometry, observed, frame, shift
                ) != transformed_plaquette_set(
                    geometry, syndrome, frame, shift
                )
                # The transported chart must map the selected correction itself,
                # rather than only preserving its final syndrome.
                failures += len(expected_correction) != correction.bit_count()
                cases += 1
    return {
        "L": length,
        "proper_cubic_frames": len(frames),
        "translations": len(shifts),
        "unit_edge_transport_cases": cases,
        "transported_rule_failures": failures,
        "direct_transported_decode_failures": direct_rule_transport_failures,
        "transformed_box_size_failures": transformed_box_size_failures,
        "covariance_scope": (
            "coframe and the lower-face boundary corner are transported"
        ),
    }


def returned_work_and_measurement_certificate(length: int = 5) -> dict[str, object]:
    geometry = box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    error = 0
    for index in range(len(edges)):
        if (13 * index + 7) % 19 < 5:
            error ^= 1 << index
    syndrome = prep.apply_matrix(masks, error)
    decoded = cellular_decode(length, syndrome)
    corrected = prep.apply_matrix(masks, decoded["correction"])

    # Each recurrence bit is XOR into a blank target from a retained predecessor
    # and retained syndrome bit.  Its compute/uncompute truth table is exact.
    xor_roundtrip_failures = 0
    for predecessor, source, target in product((0, 1), repeat=3):
        computed = target ^ predecessor ^ source
        returned = computed ^ predecessor ^ source
        xor_roundtrip_failures += returned != target
    return {
        "L": length,
        "dense_input_error_weight": error.bit_count(),
        "dense_syndrome_weight": syndrome.bit_count(),
        "dense_output_syndrome_failures": corrected != syndrome,
        "local_XOR_compute_uncompute_truth_rows": 8,
        "local_XOR_roundtrip_failures": xor_roundtrip_failures,
        "coherent_scheduled_circuit_statement": (
            "stored syndrome -> compute recurrence into blank local work -> "
            "controlled Z correction -> reverse recurrence returns work"
        ),
        "autonomous_return_pulse_constructed": False,
        "retained_nonblank_register": "the measured syndrome record",
        "resource_classification": (
            "local measurement, classical record retention, and record reset "
            "are dissipative apparatus supply; the forward CA itself has no host-selected path"
        ),
    }


def main() -> None:
    box_rows = tuple(box_basis_certificate(length) for length in range(2, 9))
    exhaustive = exhaustive_l2_certificate()
    mutations = mutation_certificate()
    covariance = covariance_certificate()
    resources = returned_work_and_measurement_certificate()
    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "uniform-local-cellular-open-plaquette-decoder-positive",
        "rule": {
            "gauge": "A_x=0 axial gauge in the transported coframe",
            "boundary_seed": "lower x face and its lower-y edge",
            "A_y_recurrence": "A_y(x+1)=A_y(x) xor F_xy(x)",
            "A_z_boundary_recurrence": "A_z(0,y+1)=A_z(0,y) xor F_yz(0,y)",
            "A_z_bulk_recurrence": "A_z(x+1)=A_z(x) xor F_xz(x)",
            "emission": (
                "a newly ready local value controls its colocated edge Z once"
            ),
            "per_iteration_neighborhood_radius": 1,
            "same_rule_at_every_size": True,
            "host_selected_paths_or_Gaussian_tables": False,
            "host_selected_stop_or_global_apply_barrier": False,
            "round_counter_is_physical_time": False,
        },
        "open_box_basis_and_held_sizes": box_rows,
        "exhaustive_L2_lawful_domain": exhaustive,
        "active_rule_deletions": mutations,
        "proper_cubic_and_boundary_covariance": covariance,
        "auxiliary_and_measurement_resources": resources,
        "code_behavior": {
            "correction_type": "Z on matter-stream edge M2 only",
            "B_and_D_preserved": True,
            "cell_triangles_reopened": False,
            "bond_rectangles_may_change_before_stage_3": True,
            "periodic_fixed_Wilson_tested": False,
        },
        "supplied": (
            "the open boundary and its lower coframe corner",
            "the transported Cycle232 proper-cubic coframe",
            "local plaquette measurement records",
            "blank local classical CA memory and dissipative record reset",
            "uniform iteration of the fixed local rule until local quiescence",
        ),
        "not_claimed": (
            "a closed-unitary autonomous decoder",
            "an autonomous returned-work reversal pulse",
            "a periodic fixed-Wilson decoder",
            "that iteration rounds are physical time",
            "a Record, Born rule, source law, or axiom pressure",
        ),
    }
    print("CYCLE703_LOCAL_CELLULAR_PLAQUETTE_DECODER")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert all(row["basis_syndrome_failures"] == 0 for row in box_rows)
    assert all(row["incomplete_wavefront_failures"] == 0 for row in box_rows)
    assert all(row["emission_nonquiescence_failures"] == 0 for row in box_rows)
    assert all(row["linearity_failures"] == 0 for row in box_rows)
    assert all(row["lawful_input_bianchi_failures"] == 0 for row in box_rows)
    assert all(row["image_equals_closed_exponent"] for row in box_rows)
    assert all(
        row["maximum_rounds_to_quiescence"] == row["expected_round_formula"]
        for row in box_rows
    )
    assert exhaustive == {
        "edge_error_patterns_enumerated": 4096,
        "distinct_lawful_syndromes": 32,
        "expected_from_rank": 32,
        "lawful_syndrome_failures": 0,
    }
    assert mutations["all_active_deletions_detected"]
    assert covariance["proper_cubic_frames"] == 24
    assert covariance["transported_rule_failures"] == 0
    assert covariance["direct_transported_decode_failures"] == 0
    assert covariance["transformed_box_size_failures"] == 0
    assert resources["dense_output_syndrome_failures"] == 0
    assert resources["local_XOR_roundtrip_failures"] == 0
    print("CYCLE703_UNIFORM_RADIUS1_CA_CLEARS_ALL_OPEN_L2_L8_BASIS_SYNDROMES")


if __name__ == "__main__":
    main()
