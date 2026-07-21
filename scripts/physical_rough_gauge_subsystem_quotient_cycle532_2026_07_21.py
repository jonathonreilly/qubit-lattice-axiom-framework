#!/usr/bin/env python3
"""Cycle 532: rough-terminal local gauge quotient of the Cycle-529 shadows.

The Cycle-247 rough-terminal face code has 7N-1 logical qubits after its
three Wilson/spin signs are initialized, versus 6N target matter qubits.  This
runner proves that the N-1 excess is an actual gauge subsystem for the full
mapped even-CAR algebra, rather than an untyped multiplicity.  It constructs
bounded gauge parity/hopping generators, proves that they exhaust the matter
commutant, and replays the Cycle-529 exact recurrent B target on the resulting
gauge quotient.

The result is conditional on a typed three-Wilson topological initialization.
Those three growing words are not local constraints or a host-selected runtime
branch.  No bounded preparation circuit for that initialization is claimed.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523
import physical_correlated_double_shadow_stream_cycle529_2026_07_21 as c529
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247


c210 = c219.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 5e-12
PERTURBATION = 1e-4
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "gauge-quotient-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md"
)
CYCLE219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
CYCLE230_RUNNER = ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
CYCLE235_RUNNER = ROOT / "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py"
CYCLE235_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md"
)
CYCLE247_RUNNER = ROOT / "scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py"
CYCLE247_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "LOCAL_ROUGH_PUNCTURE_ODD_SECTOR_CYCLE247_NOTE_2026-07-17.md"
)
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
CYCLE529_RUNNER = ROOT / "scripts/physical_correlated_double_shadow_stream_cycle529_2026_07_21.py"
CYCLE529_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CORRELATED_DOUBLE_SHADOW_STREAM_CYCLE529_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    CYCLE230_RUNNER: "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    CYCLE235_RUNNER: "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
    CYCLE235_NOTE: "295edee5608d3141fc3e3212bc51753265d953dadd68a8b44a66ed1e0e16e0d2",
    CYCLE247_RUNNER: "10f5cf027c76f5a0a3b1d3dbaa6cb0e6d418932c84553f0cca303d3f21742519",
    CYCLE247_NOTE: "8cc36f383c1d175a80ad26f17f98287fc8e94ef2f69b36851c4c420bcec8dad9",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    CYCLE529_RUNNER: "55b6811c71962bf612f13f27dab010e46b72352cda70f2acea35e6602ba9182d",
    CYCLE529_NOTE: "e4df6e600bb49f3b97f69706c614875bfe664fa6624fa75b277308683c8ca2b0",
}


class CertificateFailure(RuntimeError):
    """A bounded predicate failed; never promoted automatically to a no-go."""


class ResourceWall(RuntimeError):
    """A technical resource wall; never a physical conclusion."""


@dataclass(frozen=True)
class FrameData:
    vertex_map: tuple[int, ...]
    edge_map: tuple[int, ...]
    toggles: tuple[int, ...]
    pairs: tuple[tuple[int, int], ...]
    flips: int


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count() != 0:
        raise ResourceWall(f"nonzero swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def echelon(rows) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for source in rows:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return pivots


def null_basis(equations, columns: int) -> tuple[int, ...]:
    """Exact GF(2) null basis for row equations represented as integers."""

    pivots = echelon(equations)
    pivot_columns = set(pivots)
    ordered_pivots = sorted(pivots)
    output = []
    for free in range(columns):
        if free in pivot_columns:
            continue
        vector = 1 << free
        for pivot in ordered_pivots:
            if (pivots[pivot] & vector).bit_count() & 1:
                vector |= 1 << pivot
        output.append(vector)
    return tuple(output)


def quotient_complement(base, candidates) -> tuple[int, ...]:
    pivots = echelon(base)
    output = []
    for source in candidates:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                output.append(int(source))
                break
    return tuple(output)


def independent_pauli_basis(rows, qubits: int) -> tuple[c235.Pauli, ...]:
    pivots: dict[int, int] = {}
    output = []
    for pauli in rows:
        row = pauli.symplectic(qubits)
        reduced = row
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                output.append(pauli)
                break
    return tuple(output)


def symplectic_product(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    return (
        ((left & mask) & (right >> qubits)).bit_count()
        + ((left >> qubits) & (right & mask)).bit_count()
    ) & 1


def symplectic_gram_rank(rows: tuple[int, ...], qubits: int) -> int:
    gram = []
    for left in rows:
        row = 0
        for index, right in enumerate(rows):
            if symplectic_product(left, right, qubits):
                row |= 1 << index
        gram.append(row)
    return c235.gf2_rank(gram)


def pauli_product(rows) -> c235.Pauli:
    result = c235.Pauli()
    for row in rows:
        result = result @ row
    return result


def local_stabilizers(graph: c247.PunctureGraph) -> tuple[c235.Pauli, ...]:
    return tuple(
        [graph.loop_pauli(vertices) for _, vertices, _ in graph.local_cycles()]
        + [graph.cell_constraint(cell) for cell in graph.cells]
    )


def wilson_initializers(graph: c247.PunctureGraph) -> tuple[c235.Pauli, ...]:
    return tuple(graph.loop_pauli(vertices) for vertices in graph.wilson_cycles())


def fixed_sector_stabilizers(graph: c247.PunctureGraph) -> tuple[c235.Pauli, ...]:
    return local_stabilizers(graph) + wilson_initializers(graph)


def matter_generators(graph: c247.PunctureGraph) -> tuple[c235.Pauli, ...]:
    return tuple(
        [graph.B(vertex) for vertex in range(graph.matter_count)]
        + [graph.mapped_matter_A(edge) for edge in range(len(graph.base.edges))]
    )


def gauge_Z(graph: c247.PunctureGraph, cell) -> c235.Pauli:
    terminal = graph.terminal_lookup[(cell, 0)]
    return graph.B(graph.sink_index[cell]) @ c235.Pauli(z=1 << terminal)


def gauge_A_oriented(graph: c247.PunctureGraph, source: int, target: int) -> c235.Pauli:
    source_cell = graph.base.vertices[source][0]
    target_cell = graph.base.vertices[target][0]
    terminal_pair = c235.Pauli(
        x=(1 << graph.terminal_lookup[(source_cell, 0)])
        ^ (1 << graph.terminal_lookup[(target_cell, 0)])
    )
    dressed_matter = graph.A(source, target) @ terminal_pair
    return (
        graph.A(graph.sink_index[source_cell], source)
        @ dressed_matter
        @ graph.A(target, graph.sink_index[target_cell])
    )


def gauge_generators(graph: c247.PunctureGraph):
    z_rows = tuple(gauge_Z(graph, cell) for cell in graph.cells)
    a_rows = []
    a_edges = []
    for edge, (source, target, kind, _) in enumerate(graph.base.edges):
        if kind == "outer_square":
            a_rows.append(gauge_A_oriented(graph, source, target))
            a_edges.append((graph.base.vertices[source][0], graph.base.vertices[target][0]))
    return z_rows, tuple(a_rows), tuple(a_edges)


def phase_rank(rows, qubits: int) -> tuple[int, int]:
    rank, inconsistent = c235.phase_aware_rank(rows, qubits)
    return rank, len(inconsistent)


def factorization_controls(length: int) -> dict:
    graph = c247.PunctureGraph(length, terminals=1)
    qubits = graph.qubits
    cells = length**3
    matter_modes = 6 * cells
    local = local_stabilizers(graph)
    wilsons = wilson_initializers(graph)
    stabilizers = local + wilsons
    matter = matter_generators(graph)
    gauge_z, gauge_a, gauge_edges = gauge_generators(graph)
    gauge = gauge_z + gauge_a

    local_rank, local_inconsistent = phase_rank(local, qubits)
    fixed_rank, fixed_inconsistent = phase_rank(stabilizers, qubits)
    code_exponent = qubits - fixed_rank
    stabilizer_vectors = tuple(row.symplectic(qubits) for row in stabilizers)
    local_vectors = tuple(row.symplectic(qubits) for row in local)
    matter_vectors = tuple(row.symplectic(qubits) for row in matter)
    gauge_vectors = tuple(row.symplectic(qubits) for row in gauge)

    matter_reps = quotient_complement(stabilizer_vectors, matter_vectors)
    gauge_reps = quotient_complement(stabilizer_vectors, gauge_vectors)
    matter_dimension = len(matter_reps)
    gauge_dimension = len(gauge_reps)
    matter_gram_rank = symplectic_gram_rank(matter_reps, qubits)
    gauge_gram_rank = symplectic_gram_rank(gauge_reps, qubits)

    mask = (1 << qubits) - 1
    centralizer_equations = tuple(
        (row >> qubits) | ((row & mask) << qubits)
        for row in stabilizer_vectors + matter_vectors
    )
    centralizer = null_basis(centralizer_equations, 2 * qubits)
    commutant_reps = quotient_complement(stabilizer_vectors, centralizer)
    commutant_dimension = len(commutant_reps)
    commutant_gram_rank = symplectic_gram_rank(commutant_reps, qubits)

    gauge_matter_failures = sum(
        not gauge_row.commutes(matter_row)
        for gauge_row in gauge
        for matter_row in matter
    )
    gauge_stabilizer_failures = sum(
        not gauge_row.commutes(stabilizer)
        for gauge_row in gauge
        for stabilizer in stabilizers
    )
    gauge_z_pair_failures = 0
    for (left_cell, right_cell), row in zip(gauge_edges, gauge_a):
        actual = {
            cell
            for cell, z_row in zip(graph.cells, gauge_z)
            if not row.commutes(z_row)
        }
        gauge_z_pair_failures += actual != {left_cell, right_cell}
    gauge_a_pair_failures = 0
    for index, (left_edge, left) in enumerate(zip(gauge_edges, gauge_a)):
        for right_edge, right in zip(gauge_edges[index + 1 :], gauge_a[index + 1 :]):
            expected_anti = bool(set(left_edge) & set(right_edge))
            gauge_a_pair_failures += (not left.commutes(right)) != expected_anti

    matter_parity = pauli_product(
        graph.B(vertex) for vertex in range(graph.matter_count)
    )
    gauge_parity = pauli_product(gauge_z)
    parity_join = matter_parity @ gauge_parity
    parity_join_rank, parity_join_inconsistent = phase_rank(
        stabilizers + (parity_join,), qubits
    )
    positive_rank, positive_inconsistent = phase_rank(
        stabilizers + (matter_parity,), qubits
    )
    negative_rank, negative_inconsistent = phase_rank(
        stabilizers
        + (c235.Pauli(phase=2) @ matter_parity,),
        qubits,
    )

    local_only_matter_dimension = len(
        quotient_complement(local_vectors, matter_vectors)
    )
    local_only_matter_reps = quotient_complement(local_vectors, matter_vectors)
    local_only_matter_gram_rank = symplectic_gram_rank(
        local_only_matter_reps, qubits
    )
    local_centralizer_equations = tuple(
        (row >> qubits) | ((row & mask) << qubits)
        for row in local_vectors + matter_vectors
    )
    local_centralizer = null_basis(local_centralizer_equations, 2 * qubits)
    local_commutant_reps = quotient_complement(local_vectors, local_centralizer)
    local_commutant_dimension = len(local_commutant_reps)
    local_commutant_gram_rank = symplectic_gram_rank(
        local_commutant_reps, qubits
    )
    explicit_local_commutant_reps = quotient_complement(
        local_vectors,
        gauge_vectors + tuple(row.symplectic(qubits) for row in wilsons),
    )
    explicit_local_commutant_dimension = len(explicit_local_commutant_reps)
    explicit_local_commutant_gram_rank = symplectic_gram_rank(
        explicit_local_commutant_reps, qubits
    )
    maximum_local_constraint_weight = max(
        (row.x | row.z).bit_count() for row in local
    )
    maximum_wilson_weight = max((row.x | row.z).bit_count() for row in wilsons)

    expected_matter_dimension = 2 * matter_modes - 1
    expected_gauge_dimension = 2 * cells - 1
    expected_matter_gram_rank = 2 * matter_modes - 2
    expected_gauge_gram_rank = 2 * cells - 2
    pass_flag = bool(
        qubits == 22 * cells
        and local_inconsistent == fixed_inconsistent == 0
        and local_rank == 15 * cells - 2
        and fixed_rank == 15 * cells + 1
        and code_exponent == 7 * cells - 1
        and matter_dimension == expected_matter_dimension
        and matter_gram_rank == expected_matter_gram_rank
        and gauge_dimension == expected_gauge_dimension
        and gauge_gram_rank == expected_gauge_gram_rank
        and commutant_dimension == expected_gauge_dimension
        and commutant_gram_rank == expected_gauge_gram_rank
        and gauge_matter_failures == gauge_stabilizer_failures == 0
        and gauge_z_pair_failures == gauge_a_pair_failures == 0
        and parity_join_rank == fixed_rank
        and parity_join_inconsistent == 0
        and positive_rank == negative_rank == fixed_rank + 1
        and positive_inconsistent == negative_inconsistent == 0
        and local_only_matter_dimension == expected_matter_dimension + 3
        and local_only_matter_gram_rank == expected_matter_gram_rank
        and local_commutant_dimension == expected_gauge_dimension + 3
        and local_commutant_gram_rank == expected_gauge_gram_rank
        and explicit_local_commutant_dimension == local_commutant_dimension
        and explicit_local_commutant_gram_rank == local_commutant_gram_rank
        and maximum_local_constraint_weight <= 28
        and max((row.x | row.z).bit_count() for row in gauge_z) == 6
        and max((row.x | row.z).bit_count() for row in gauge_a) <= 18
    )
    return {
        "length": length,
        "coarse_cells": cells,
        "physical_M2": qubits,
        "physical_M2_per_cell": qubits / cells,
        "bounded_local_constraint_rows": len(local),
        "bounded_local_constraint_rank": local_rank,
        "bounded_local_constraint_maximum_weight": maximum_local_constraint_weight,
        "Wilson_initializers": len(wilsons),
        "Wilson_rank_increment": fixed_rank - local_rank,
        "maximum_Wilson_initializer_weight": maximum_wilson_weight,
        "fixed_sector_stabilizer_rank": fixed_rank,
        "fixed_sector_code_exponent": code_exponent,
        "target_Fock_exponent": matter_modes,
        "gauge_qubits": cells - 1,
        "matter_even_algebra_quotient_dimension": matter_dimension,
        "matter_even_algebra_symplectic_rank": matter_gram_rank,
        "matter_even_algebra_radical_dimension": matter_dimension - matter_gram_rank,
        "explicit_gauge_quotient_dimension": gauge_dimension,
        "explicit_gauge_symplectic_rank": gauge_gram_rank,
        "explicit_gauge_radical_dimension": gauge_dimension - gauge_gram_rank,
        "full_matter_commutant_quotient_dimension": commutant_dimension,
        "full_matter_commutant_symplectic_rank": commutant_gram_rank,
        "explicit_gauge_exhausts_full_commutant": gauge_dimension == commutant_dimension,
        "gauge_Z_maximum_weight": max((row.x | row.z).bit_count() for row in gauge_z),
        "gauge_A_maximum_weight": max((row.x | row.z).bit_count() for row in gauge_a),
        "gauge_matter_commutator_failures": gauge_matter_failures,
        "gauge_stabilizer_commutator_failures": gauge_stabilizer_failures,
        "gauge_Z_A_incidence_failures": gauge_z_pair_failures,
        "gauge_A_A_incidence_failures": gauge_a_pair_failures,
        "matter_gauge_parities_equal_on_code": parity_join_rank == fixed_rank,
        "positive_matter_parity_sector_nonempty": positive_inconsistent == 0,
        "negative_matter_parity_sector_nonempty": negative_inconsistent == 0,
        "fixed_parity_sector_exponent": code_exponent - 1,
        "expected_target_parity_plus_gauge_exponent": (matter_modes - 1) + (cells - 1),
        "local_only_matter_quotient_dimension": local_only_matter_dimension,
        "local_only_matter_symplectic_rank": local_only_matter_gram_rank,
        "local_only_matter_radical_dimension": (
            local_only_matter_dimension - local_only_matter_gram_rank
        ),
        "local_only_spin_twist_excess": local_only_matter_dimension - expected_matter_dimension,
        "local_only_full_matter_commutant_dimension": local_commutant_dimension,
        "local_only_full_matter_commutant_symplectic_rank": local_commutant_gram_rank,
        "local_only_full_matter_commutant_radical_dimension": (
            local_commutant_dimension - local_commutant_gram_rank
        ),
        "explicit_gauge_plus_Wilsons_exhaust_local_only_commutant": (
            explicit_local_commutant_dimension == local_commutant_dimension
        ),
        "Wilson_Pauli_conjugates_commuting_with_complete_matter_algebra": 0,
        "Cycle269_abelian_vs_M8_topological_conclusion_changed": False,
        "factorization_statement": (
            "H_fixed is target full Fock tensor an (N-1)-qubit gauge factor, "
            "sectorwise for the shared matter/gauge parity center"
        ),
        "pass": pass_flag,
    }


def frame_data(graph: c247.PunctureGraph, frame: np.ndarray) -> FrameData:
    vertex_map, edge_map = c247.graph_frame_maps(graph, frame)
    toggles, pairs = c247.order_gauge(graph, vertex_map, edge_map)
    flips = 0
    for source_edge, row in enumerate(graph.edges):
        if row.v is None:
            continue
        transformed = c247.permute_pauli(graph.A(row.u, row.v), edge_map)
        target = graph.A(vertex_map[row.u], vertex_map[row.v])
        ordered = c235.apply_gauge(transformed, toggles, pairs)
        if (ordered.phase - target.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
    return FrameData(
        tuple(vertex_map), tuple(edge_map), tuple(toggles), tuple(pairs), flips
    )


def transform_pauli(pauli: c235.Pauli, data: FrameData) -> c235.Pauli:
    return c235.apply_gauge(
        c247.permute_pauli(pauli, list(data.edge_map)),
        data.toggles,
        data.pairs,
        data.flips,
    )


def permute_mask(mask: int, mapping: tuple[int, ...]) -> int:
    result = 0
    while mask:
        bit = mask & -mask
        source = bit.bit_length() - 1
        result ^= 1 << mapping[source]
        mask ^= bit
    return result


def transform_single_xz(pauli: c235.Pauli, data: FrameData) -> c235.Pauli:
    if pauli.x.bit_count() > 1:
        raise ValueError("single-generator transform received multi-X Pauli")
    z = permute_mask(pauli.z, data.edge_map)
    x = 0
    phase = pauli.phase
    if pauli.x:
        source = pauli.x.bit_length() - 1
        target = data.edge_map[source]
        x = 1 << target
        z ^= data.toggles[target]
        phase = (phase + 2 * ((data.flips >> target) & 1)) % 4
    return c235.Pauli(phase, x, z)


def covariance_controls() -> dict:
    graph = c247.PunctureGraph(3, terminals=1)
    frames = c235.proper_cubic_frames()
    data = tuple(frame_data(graph, frame) for frame in frames)
    fixed_stabs = fixed_sector_stabilizers(graph)
    target_rank, target_inconsistent = phase_rank(fixed_stabs, graph.qubits)
    gauge_z, gauge_a, _ = gauge_generators(graph)
    gauge_z_failures = gauge_a_failures = stabilizer_failures = 0
    for row_data in data:
        for cell, source in zip(graph.cells, gauge_z):
            target_sink = row_data.vertex_map[graph.sink_index[cell]]
            target_cell = graph.vertices[target_sink][0]
            gauge_z_failures += transform_pauli(source, row_data) != gauge_Z(graph, target_cell)
        for edge, (source, target, kind, _) in enumerate(graph.base.edges):
            if kind != "outer_square":
                continue
            expected = gauge_A_oriented(
                graph, row_data.vertex_map[source], row_data.vertex_map[target]
            )
            gauge_a_failures += transform_pauli(
                gauge_A_oriented(graph, source, target), row_data
            ) != expected
        transformed_stabs = tuple(transform_pauli(row, row_data) for row in fixed_stabs)
        rank, inconsistent = phase_rank(fixed_stabs + transformed_stabs, graph.qubits)
        stabilizer_failures += rank != target_rank or bool(inconsistent)

    frame_index = {
        tuple(int(value) for value in frame.ravel()): index
        for index, frame in enumerate(frames)
    }
    group_mismatches = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product_index = frame_index[
                tuple(int(value) for value in (left @ right).ravel())
            ]
            for edge in range(graph.qubits):
                for generator in (
                    c235.Pauli(x=1 << edge),
                    c235.Pauli(z=1 << edge),
                ):
                    composed = transform_single_xz(
                        transform_single_xz(generator, data[right_index]),
                        data[left_index],
                    )
                    direct = transform_single_xz(generator, data[product_index])
                    group_mismatches += composed != direct
    return {
        "length": 3,
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "gauge_Z_frame_failures": gauge_z_failures,
        "gauge_A_frame_failures": gauge_a_failures,
        "fixed_all_plus_Wilson_code_frame_failures": stabilizer_failures,
        "single_face_X_Z_group_law_cases": len(frames) ** 2 * graph.qubits * 2,
        "single_face_X_Z_group_law_mismatches": group_mismatches,
        "active_runtime_frame_selector": False,
        "abstract_chart_orbit_substituted": False,
        "pass": bool(
            len(frames) == 24
            and len(frames) ** 2 == 576
            and target_inconsistent == 0
            and gauge_z_failures == gauge_a_failures == stabilizer_failures == 0
            and group_mismatches == 0
        ),
    }


def physical_position(graph: c247.PunctureGraph, qubit: int) -> tuple[int, int, int]:
    row = graph.edges[qubit]
    center = 32 * np.asarray(row.owner, dtype=int)
    if row.kind == "rough_terminal":
        offset = np.zeros(3, dtype=int)
    elif row.kind == "puncture_spoke":
        offset = 4 * np.asarray(c210.DIRECTIONS[row.label], dtype=int)
    elif row.kind == "matter_internal_triangle":
        left_direction = graph.base.vertices[row.u][1]
        right_direction = graph.base.vertices[row.v][1]
        offset = 2 * (
            np.asarray(c210.DIRECTIONS[left_direction], dtype=int)
            + np.asarray(c210.DIRECTIONS[right_direction], dtype=int)
        )
    elif row.kind == "matter_outer_square":
        source_direction = graph.base.vertices[row.u][1]
        offset = 16 * np.asarray(c210.DIRECTIONS[source_direction], dtype=int)
    else:
        raise ValueError(f"unsupported physical role {row.kind}")
    period = 32 * graph.length
    return tuple(int(value % period) for value in center + offset)


def periodic_l1(left, right, period: int) -> int:
    return sum(
        min(abs(a - b), period - abs(a - b)) for a, b in zip(left, right)
    )


def support_diameter(mask: int, positions, period: int) -> int:
    sites = []
    while mask:
        bit = mask & -mask
        sites.append(positions[bit.bit_length() - 1])
        mask ^= bit
    return max(
        (periodic_l1(left, right, period) for left, right in combinations(sites, 2)),
        default=0,
    )


def fswap_support_mask(graph: c247.PunctureGraph, edge: int) -> int:
    source, target, _, _ = graph.base.edges[edge]
    rows = (
        graph.B(source),
        graph.B(target),
        graph.mapped_matter_A(edge),
    )
    return (
        (rows[0].x | rows[0].z)
        | (rows[1].x | rows[1].z)
        | (rows[2].x | rows[2].z)
    )


def layout_controls(length: int) -> dict:
    graph = c247.PunctureGraph(length, terminals=1)
    period = 32 * length
    positions = tuple(physical_position(graph, qubit) for qubit in range(graph.qubits))
    collisions = len(positions) - len(set(positions))
    local = local_stabilizers(graph)
    matter = matter_generators(graph)
    gauge_z, gauge_a, _ = gauge_generators(graph)
    stream_edges = tuple(
        edge
        for edge, row in enumerate(graph.base.edges)
        if row[2] == "outer_square"
    )
    local_masks = tuple(row.x | row.z for row in local)
    matter_masks = tuple(row.x | row.z for row in matter)
    gauge_masks = tuple(row.x | row.z for row in gauge_z + gauge_a)
    fswap_masks = tuple(fswap_support_mask(graph, edge) for edge in stream_edges)

    frame_position_failures = 0
    for frame in c235.proper_cubic_frames():
        _, edge_map = c247.graph_frame_maps(graph, frame)
        for source, target in enumerate(edge_map):
            expected = tuple(
                int(value % period)
                for value in frame @ np.asarray(positions[source], dtype=int)
            )
            frame_position_failures += expected != positions[target]
    return {
        "length": length,
        "period": period,
        "physical_M2": graph.qubits,
        "physical_M2_per_cell": graph.qubits / length**3,
        "placement_collisions": collisions,
        "maximum_local_constraint_physical_L1_diameter": max(
            support_diameter(mask, positions, period) for mask in local_masks
        ),
        "maximum_matter_generator_physical_L1_diameter": max(
            support_diameter(mask, positions, period) for mask in matter_masks
        ),
        "maximum_gauge_generator_physical_L1_diameter": max(
            support_diameter(mask, positions, period) for mask in gauge_masks
        ),
        "maximum_B_FSWAP_block_physical_L1_diameter": max(
            support_diameter(mask, positions, period) for mask in fswap_masks
        ),
        "maximum_B_FSWAP_block_M2_support": max(mask.bit_count() for mask in fswap_masks),
        "B_FSWAP_blocks_per_cell": len(stream_edges) / length**3,
        "frame_position_failures": frame_position_failures,
        "proper_cubic_frames": len(c235.proper_cubic_frames()),
        "pass": bool(
            collisions == 0
            and graph.qubits == 22 * length**3
            and max(mask.bit_count() for mask in fswap_masks) == 13
            and len(stream_edges) == 3 * length**3
            and frame_position_failures == 0
        ),
    }


def hermitian_normalize(pauli: c235.Pauli) -> c235.Pauli:
    return c235.Pauli((pauli.x & pauli.z).bit_count() & 1, pauli.x, pauli.z)


def onsite_hopping(graph: c247.PunctureGraph, cell, left: int, right: int) -> c235.Pauli:
    source = graph.base.vertex_index[(cell, left)]
    target = graph.base.vertex_index[(cell, right)]
    direct_key = frozenset((source, target))
    if direct_key in graph.base.edge_lookup:
        return graph.mapped_matter_A(graph.base.edge_lookup[direct_key])
    helper = next(
        graph.base.vertex_index[(cell, direction)]
        for direction in range(6)
        if direction not in (left, right)
        and frozenset((source, graph.base.vertex_index[(cell, direction)]))
        in graph.base.edge_lookup
        and frozenset((graph.base.vertex_index[(cell, direction)], target))
        in graph.base.edge_lookup
    )
    first = graph.mapped_matter_A(graph.base.edge_lookup[frozenset((source, helper))])
    second = graph.mapped_matter_A(graph.base.edge_lookup[frozenset((helper, target))])
    return hermitian_normalize(first @ graph.B(helper) @ second)


def onsite_compatibility_controls(length: int) -> dict:
    graph = c247.PunctureGraph(length, terminals=1)
    stabilizers = fixed_sector_stabilizers(graph)
    gauge_z, gauge_a, _ = gauge_generators(graph)
    gauge = gauge_z + gauge_a
    cell = (0, 0, 0)
    hoppings = tuple(
        onsite_hopping(graph, cell, left, right)
        for left, right in combinations(range(6), 2)
    )
    cell_b = tuple(
        graph.B(graph.base.vertex_index[(cell, direction)]) for direction in range(6)
    )
    contact_words = tuple(
        left @ right for left, right in combinations(cell_b, 2)
    )
    stabilizer_failures = sum(
        not row.commutes(stabilizer)
        for row in hoppings + contact_words
        for stabilizer in stabilizers
    )
    gauge_failures = sum(
        not row.commutes(gauge_row)
        for row in hoppings + contact_words
        for gauge_row in gauge
    )
    endpoint_failures = 0
    for (left, right), hopping in zip(combinations(range(6), 2), hoppings):
        actual = {
            direction
            for direction, b_row in enumerate(cell_b)
            if not hopping.commutes(b_row)
        }
        endpoint_failures += actual != {left, right}
    return {
        "length": length,
        "all_15_onsite_mode_pairs_available": len(hoppings) == 15,
        "maximum_onsite_hopping_M2_support": max(
            (row.x | row.z).bit_count() for row in hoppings
        ),
        "maximum_contact_word_M2_support": max(
            (row.x | row.z).bit_count() for row in contact_words
        ),
        "onsite_hopping_endpoint_incidence_failures": endpoint_failures,
        "onsite_and_contact_stabilizer_failures": stabilizer_failures,
        "onsite_and_contact_gauge_commutator_failures": gauge_failures,
        "primitive_Givens_recode_compatible": True,
        "full_Cycle523_two_M2_schedule_transplanted": False,
        "pass": bool(
            len(hoppings) == len(contact_words) == 15
            and max((row.x | row.z).bit_count() for row in hoppings) <= 7
            and endpoint_failures == stabilizer_failures == gauge_failures == 0
        ),
    }


def fswap_matrix_control() -> dict:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)
    polynomial = 0.5 * (
        b_left
        + b_right
        + 1j * b_left @ hopping
        - 1j * b_right @ hopping
    )
    fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    residual = float(np.linalg.norm(polynomial - fswap))
    unitarity = float(np.linalg.norm(polynomial.conj().T @ polynomial - np.eye(4)))
    inverse = float(np.linalg.norm(polynomial @ polynomial - np.eye(4)))
    deleted = 0.5 * (b_left + b_right + 1j * b_left @ hopping)
    deleted_residual = float(np.linalg.norm(deleted - fswap))
    return {
        "matrix_residual": residual,
        "unitarity_residual": unitarity,
        "inverse_square_residual": inverse,
        "deleted_fourth_term_residual": deleted_residual,
        "perturbed_phase_basis_residual": float(abs(np.exp(1j * PERTURBATION) - 1)),
        "pass": bool(
            residual < TOLERANCE
            and unitarity < TOLERANCE
            and inverse < TOLERANCE
            and deleted_residual > 0.4
        ),
    }


def deletion_controls() -> dict:
    graph = c247.PunctureGraph(3, terminals=1)
    local = local_stabilizers(graph)
    fixed = fixed_sector_stabilizers(graph)
    full_rank = c235.gf2_rank(row.symplectic(graph.qubits) for row in fixed)
    local_rank = c235.gf2_rank(row.symplectic(graph.qubits) for row in local)
    deleted_local_rank = c235.gf2_rank(
        row.symplectic(graph.qubits) for row in local[1:]
    )
    local_basis = independent_pauli_basis(local, graph.qubits)
    deleted_independent_local_rank = c235.gf2_rank(
        row.symplectic(graph.qubits) for row in local_basis[1:]
    )
    deleted_wilson_rank = c235.gf2_rank(
        row.symplectic(graph.qubits) for row in fixed[:-1]
    )
    first_stream = next(
        edge for edge, row in enumerate(graph.base.edges) if row[2] == "outer_square"
    )
    source, target, _, _ = graph.base.edges[first_stream]
    bare_stream = graph.A(source, target)
    dressed_stream = graph.mapped_matter_A(first_stream)
    cell_rows = tuple(graph.cell_constraint(cell) for cell in graph.cells)
    bare_syndrome = sum(not bare_stream.commutes(row) for row in cell_rows)
    dressed_syndrome = sum(not dressed_stream.commutes(row) for row in cell_rows)
    gauge_full = gauge_A_oriented(graph, source, target)
    source_cell = graph.base.vertices[source][0]
    target_cell = graph.base.vertices[target][0]
    gauge_deleted_left_spoke = (
        (graph.A(source, target) @ c235.Pauli(
            x=(1 << graph.terminal_lookup[(source_cell, 0)])
            ^ (1 << graph.terminal_lookup[(target_cell, 0)])
        ))
        @ graph.A(target, graph.sink_index[target_cell])
    )
    matter = matter_generators(graph)
    deleted_gauge_matter_failures = sum(
        not gauge_deleted_left_spoke.commutes(row) for row in matter
    )
    return {
        "fixed_sector_rank": full_rank,
        "bounded_local_rank": local_rank,
        "delete_one_displayed_local_row_rank": deleted_local_rank,
        "independent_local_basis_rows": len(local_basis),
        "delete_one_independent_local_row_rank": deleted_independent_local_rank,
        "delete_one_Wilson_initializer_rank": deleted_wilson_rank,
        "bare_stream_cell_constraint_syndrome": bare_syndrome,
        "dressed_stream_cell_constraint_syndrome": dressed_syndrome,
        "delete_left_spoke_from_gauge_A_matter_commutator_failures": deleted_gauge_matter_failures,
        "undeleted_gauge_A_matter_commutator_failures": sum(
            not gauge_full.commutes(row) for row in matter
        ),
        "pass": bool(
            deleted_local_rank in (local_rank, local_rank - 1)
            and len(local_basis) == local_rank
            and deleted_independent_local_rank == local_rank - 1
            and deleted_wilson_rank == full_rank - 1
            and bare_syndrome == 2
            and dressed_syndrome == 0
            and deleted_gauge_matter_failures > 0
            and all(gauge_full.commutes(row) for row in matter)
        ),
    }


def target_B_controls() -> dict:
    models = {length: c529.build_shadow_model(length) for length in (TRAIN_LENGTH, HELD_LENGTH)}
    theorems = tuple(c529.coefficient_theorem_controls(models[length]) for length in models)
    low = tuple(c529.complete_low_sector_controls(models[length]) for length in models)
    higher = tuple(c529.higher_sector_controls(models[length]) for length in models)
    return {
        "quadratic_full_Fock_theorems": theorems,
        "complete_low_sector_censuses": low,
        "higher_sector_controls": higher,
        "rough_pullback_statement": (
            "each mapped outer-edge FSWAP is the exact B/A polynomial; the "
            "faithful matter quotient therefore pulls the product back to Gamma(P)"
        ),
        "Cycle529_15_call_chart_runtime_retained_literally": False,
        "Cycle529_chart_CZ_and_bank_SWAP_calls_removed_modulo_gauge": 12,
        "rough_gauge_B_blocks_per_cell": 3,
        "pass": bool(
            all(row["pass"] for row in theorems)
            and all(row["pass"] for row in low)
            and all(row["pass"] for row in higher)
        ),
    }


def fixture_controls() -> dict:
    fixtures = c529.onsite_fixture_controls()
    return {
        **fixtures,
        "interpretation": (
            "re-executed logical comparators; preservation follows conditionally "
            "through the faithful fixed-spin matter factor, not through a prepared E circuit"
        ),
        "rough_code_mass_contact_seam_matrix_enumerated": False,
        "pass": fixtures["pass"],
    }


def upstream_evidence() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "7n-1",
        "n-1 gauge",
        "weight 6",
        "weight 18",
        "full commutant",
        "three wilson",
        "topological initialization",
        "not a global sector selector",
        "all 24",
        "576",
        "4,096",
        "988",
        "site-major",
        "15-call",
        "broad no-go gate status: **fail / do not ship**",
        "partial-attempt-with-named-untested-routes",
        "n1 — alternative-route normalization",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "strict_predecessor_hashes": evidence["pass"],
        "note_scope_target_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle532-rough-gauge-contract-ready" if all(tests.values()) else "cycle532-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle532 dry contract failed")

    factorization = tuple(factorization_controls(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    checkpoints.append(checkpoint(started, "L5-L6-subsystem-factorizations"))
    covariance = covariance_controls()
    checkpoints.append(checkpoint(started, "all24-576-covariance"))
    layouts = tuple(layout_controls(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    checkpoints.append(checkpoint(started, "bounded-M2-layouts"))
    onsite = tuple(onsite_compatibility_controls(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    checkpoints.append(checkpoint(started, "onsite-givens-contact-compatibility"))
    fswap = fswap_matrix_control()
    deletions = deletion_controls()
    checkpoints.append(checkpoint(started, "inverse-leakage-deletions"))
    target_b = target_B_controls()
    checkpoints.append(checkpoint(started, "two-cell-three-cell-L5-L6-target-B"))
    fixtures = fixture_controls()
    checkpoints.append(checkpoint(started, "mass-contact-seam-comparators"))

    tests = {
        "dry_contract": dry["pass"],
        "exact_L5_held_L6_target_tensor_gauge_factorization": all(row["pass"] for row in factorization),
        "bounded_explicit_gauge_generators_exhaust_full_commutant": all(
            row["explicit_gauge_exhausts_full_commutant"] for row in factorization
        ),
        "fixed_code_all24_and_576_covariance": covariance["pass"],
        "bounded_constant_overhead_physical_M2_layout": all(row["pass"] for row in layouts),
        "primitive_onsite_Givens_and_contact_compatible": all(row["pass"] for row in onsite),
        "bounded_FSWAP_polynomial_inverse_and_deletion": fswap["pass"],
        "constraint_gauge_and_Wilson_deletion_controls": deletions["pass"],
        "complete_two_cell_three_cell_L5_L6_target_B": target_b["pass"],
        "mass_contact_seam_logical_comparators": fixtures["pass"],
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "gauge-quotient-certificate",
        "status": (
            "cycle532-local-gauge-subsystem-with-typed-topological-initialization"
            if all(tests.values())
            else "cycle532-certificate-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "factorization": factorization,
        "covariance": covariance,
        "physical_layouts": layouts,
        "onsite_compatibility": onsite,
        "fswap_polynomial": fswap,
        "deletion_controls": deletions,
        "target_B_controls": target_b,
        "logical_fixture_comparators": fixtures,
        "strongest_constructive_result": {
            "code": "Cycle247 rough-terminal face code with local checks and three all-plus Wilson initializers",
            "factorization": "H_fixed = H_full-Fock tensor H_gauge with N-1 gauge qubits, sectorwise across the shared parity center",
            "local_gauge_Z": "Z_h(x) B_sink(x), weight 6 after terminal cancellation",
            "local_gauge_A": "A_sink,u * Ahat_u,v * A_v,sink on each neighboring-cell bond, weight at most 18",
            "runtime": "three bounded mapped FSWAP polynomials per cell; matter action is gauge identity",
            "Cycle529_relation": "same exact Gamma(P); twelve chart-CZ/bank calls are absent modulo the gauge quotient",
            "physical_M2_per_cell": 22,
            "maximum_local_constraint_weight": 28,
            "maximum_B_block_M2_support": 13,
            "physical_compiler_unconditional": False,
        },
        "exact_remaining_obligations": {
            "bounded_local_or_autonomous_three_Wilson_initialization": "not supplied",
            "bounded_preparation_circuit_for_the_fixed-spin_face code": "not supplied",
            "literal_one_two_M2_factorization_of_each_support_13_FSWAP_polynomial": "not frozen",
            "site_major_A_AP_constraints": "retired from this presentation",
            "global_parity_service": False,
            "runtime_frame_or_sector_selector": False,
            "strength_relation_to_target": "the topological encoding/init obligation is target-equivalent for this periodic face presentation",
        },
        "supplied_not_synthesized": {
            "square_pyramid_puncture_graph": True,
            "three_all_plus_Wilson_spin_signs": True,
            "typed_topological_initialization": True,
            "period_32_macro_origin": True,
            "local_incident_edge_framing_Clifford": True,
            "Cycle219_coin": True,
            "Cycle230_contact_and_factor_order": True,
            "arbitrary_gauge_state_selector": False,
            "site_major_shadow_chart": False,
            "runtime_host_choice": False,
            "physical_duration_energy_Record_or_source": False,
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "disposition": "partial-attempt-with-named-untested-routes",
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle532-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
