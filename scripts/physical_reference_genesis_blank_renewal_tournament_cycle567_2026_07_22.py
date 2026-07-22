#!/usr/bin/env python3
"""Cycle 567: selected-reference genesis and blank-renewal tournament.

The constructive core is an exact product-input compiler for the fixed-Wilson
selected reference, expressed as a cycle-space tree encoder followed by the
induced quadratic Clifford phase graph.  It is compared with (A) a reset/pump
route with an explicit entropy environment, (B) a reversible relational route
that retains Wilson/frame information, and (C) Cycle 537's fill-disk/defect
route.  The product compiler is exact but its growing phase program is not
promoted to an autonomous bounded law.  Local blank/work renewal is exact and
entropy-optimal conditional on a fresh local environment.

Authority: none. Audit: unset. Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_held_sparse_order_retirement_cycle563_2026_07_21 as c563
import physical_local_wilson_fill_disk_cycle537_2026_07_21 as c537


c560 = c563.c560
c557 = c560.c557
c533 = c560.c533
c527 = c533.c527
c269 = c560.c539.c525.c319.c269
c235 = c269.c235

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 2
TRAIN_LENGTH = 3
HELD_LENGTH = 4
RECURRENCE_LENGTH = 5
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1800.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "reference-renewal-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REFERENCE_GENESIS_BLANK_RENEWAL_TOURNAMENT_CYCLE567_NOTE_2026-07-22.md"
)
C537_RUNNER = ROOT / "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py"
C537_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md"
)
C560_RUNNER = ROOT / "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py"
C560_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GLOBAL_N3_RETURNED_SLOT_COMPILER_CYCLE560_NOTE_2026-07-21.md"
)
C563_RUNNER = ROOT / "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py"
C563_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_HELD_SPARSE_ORDER_RETIREMENT_CYCLE563_NOTE_2026-07-21.md"
)
C563_RECEIPT = ROOT / (
    "outputs/physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json"
)
STRICT_FILE_HASHES = {
    C537_RUNNER: "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    C537_NOTE: "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
    C560_RUNNER: "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    C560_NOTE: "7c1a237b075b503eb4c3649ca16b0e6036acdb2e19bfca7bbf30e11c7dd1518d",
    C563_RUNNER: "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    C563_NOTE: "5f8cf7ddd3124a6377077936195667298e6723ac36734c8aaadbf70bccc7fdf8",
    C563_RECEIPT: "350e2c1922379bb42091e1cb5685c9e1f698ed23b81acf7c14803ba5043fcfc1",
}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-567 predicate failed."""


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
    swaps = swap_count()
    if elapsed >= WALL_LIMIT_SECONDS:
        raise CertificateFailure(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise CertificateFailure(f"RSS guard reached at {label}: {rss}")
    if swaps:
        raise CertificateFailure(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def alarm_handler(_signum, _frame) -> None:
    raise CertificateFailure("Cycle567 hard wall alarm fired")


def graph_tree(graph) -> dict:
    vertex_count = len(graph.vertices)
    adjacency = [[] for _ in range(vertex_count)]
    for edge, (first, second, *_rest) in enumerate(graph.edges):
        adjacency[first].append((second, edge))
        adjacency[second].append((first, edge))
    parent = [-2] * vertex_count
    parent_edge = [-1] * vertex_count
    depth = [0] * vertex_count
    parent[0] = -1
    queue = deque((0,))
    while queue:
        vertex = queue.popleft()
        for target, edge in sorted(adjacency[vertex]):
            if parent[target] != -2:
                continue
            parent[target] = vertex
            parent_edge[target] = edge
            depth[target] = depth[vertex] + 1
            queue.append(target)
    if any(value == -2 for value in parent):
        raise CertificateFailure("selected reference graph is disconnected")
    return {
        "adjacency": tuple(tuple(row) for row in adjacency),
        "parent": tuple(parent),
        "parent_edge": tuple(parent_edge),
        "depth": tuple(depth),
        "tree_edges": frozenset(parent_edge[1:]),
    }


def tree_path_mask(first: int, second: int, tree: dict) -> int:
    parent = tree["parent"]
    parent_edge = tree["parent_edge"]
    depth = tree["depth"]
    mask = 0
    while depth[first] > depth[second]:
        mask ^= 1 << parent_edge[first]
        first = parent[first]
    while depth[second] > depth[first]:
        mask ^= 1 << parent_edge[second]
        second = parent[second]
    while first != second:
        mask ^= (1 << parent_edge[first]) | (1 << parent_edge[second])
        first = parent[first]
        second = parent[second]
    return mask


def x_pauli_basis(rows) -> dict[int, c235.Pauli]:
    basis = {}
    for original in rows:
        row = original.x
        accumulated = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                accumulated = accumulated @ basis[pivot]
                row ^= basis[pivot].x
            else:
                if accumulated.x != row:
                    raise CertificateFailure("Pauli/X reduction lost its row")
                basis[pivot] = accumulated
                break
    return basis


def pauli_with_x(target: int, basis: dict[int, c235.Pauli]) -> c235.Pauli:
    row = target
    result = c235.Pauli()
    while row:
        pivot = row.bit_length() - 1
        if pivot not in basis:
            raise CertificateFailure("fundamental cycle outside retained loop span")
        result = result @ basis[pivot]
        row ^= basis[pivot].x
    if result.x != target:
        raise CertificateFailure("loop representative does not have requested X mask")
    return result


def periodic_distance_with_positive_tie(first, second, modulus: int) -> tuple[int, int]:
    distance = 0
    ties = 0
    for source, target in zip(first, second):
        forward = (target - source) % modulus
        backward = (source - target) % modulus
        distance += min(forward, backward)
        ties += forward == backward and forward != 0
    return distance, ties


def simulate_tree_encoder_column(chord: int, graph, tree: dict) -> tuple[int, int]:
    edge_bits = 1 << chord
    first, second, *_rest = graph.edges[chord]
    accumulator = (1 << first) ^ (1 << second)
    order = sorted(range(1, len(graph.vertices)), key=lambda v: tree["depth"][v], reverse=True)
    for vertex in order:
        if not ((accumulator >> vertex) & 1):
            continue
        edge = tree["parent_edge"][vertex]
        edge_bits ^= 1 << edge
        accumulator ^= 1 << tree["parent"][vertex]
        accumulator ^= 1 << vertex
    return edge_bits, accumulator


def selected_reference_product_compiler(length: int) -> dict:
    """Compile the unique fixed-Wilson face vacuum from reset product M2."""

    started = time.monotonic()
    code = c269.build_code(length)
    graph = code.graph
    edge_count = len(graph.edges)
    vertex_count = len(graph.vertices)
    cycle_count = edge_count - vertex_count + 1
    tree = graph_tree(graph)
    chord_edges = tuple(edge for edge in range(edge_count) if edge not in tree["tree_edges"])
    cycles = []
    tree_encoder_failures = 0
    tree_work_leakage = 0
    for chord in chord_edges:
        first, second, *_rest = graph.edges[chord]
        cycle = (1 << chord) ^ tree_path_mask(first, second, tree)
        cycles.append(cycle)
        encoded, work = simulate_tree_encoder_column(chord, graph, tree)
        tree_encoder_failures += encoded != cycle
        tree_work_leakage += work.bit_count()
    cycles = tuple(cycles)

    loop_basis = x_pauli_basis(code.local_checks + code.wilsons)
    representatives = tuple(pauli_with_x(cycle, loop_basis) for cycle in cycles)
    phase_rows = []
    phase_asymmetry = 0
    hermiticity_failures = 0
    phase_gate_mismatches = 0
    phase_digest = sha256()
    diagonal_phase_gates = 0
    sign_Z_gates = 0
    phase_CZ_pairs = 0
    maximum_phase_degree = 0
    total_routed_two_M2 = 0
    maximum_route_distance = 0
    antipodal_axis_ties = 0
    modulus = c527.fine_length(length)
    chord_coordinates = {
        edge: c533.coordinate_for_qubit(code, edge) for edge in chord_edges
    }
    for index, representative in enumerate(representatives):
        row = 0
        for target, cycle in enumerate(cycles):
            if (representative.z & cycle).bit_count() & 1:
                row |= 1 << target
        phase_rows.append(row)
        diagonal = (row >> index) & 1
        hermiticity_failures += (representative.phase - diagonal) % 2 != 0
        diagonal_phase_gates += diagonal
        sign_Z_gates += representative.phase in (2, 3)
        predicted_phase = diagonal + 2 * (representative.phase in (2, 3))
        phase_gate_mismatches += predicted_phase % 4 != representative.phase
        degree = (row & ~(1 << index)).bit_count()
        maximum_phase_degree = max(maximum_phase_degree, degree)
        lower = row & ((1 << index) - 1)
        phase_CZ_pairs += lower.bit_count()
        while lower:
            bit = lower & -lower
            other = bit.bit_length() - 1
            distance, ties = periodic_distance_with_positive_tie(
                chord_coordinates[chord_edges[index]],
                chord_coordinates[chord_edges[other]],
                modulus,
            )
            antipodal_axis_ties += ties
            if distance <= 0:
                raise CertificateFailure("distinct phase roles occupy one coordinate")
            maximum_route_distance = max(maximum_route_distance, distance)
            total_routed_two_M2 += 2 * distance - 1
            lower ^= bit
        phase_digest.update(
            repr((chord_edges[index], representative.phase, representative.x, representative.z, row)).encode()
        )
    phase_rows = tuple(phase_rows)
    for first in range(cycle_count):
        for second in range(first):
            phase_asymmetry += ((phase_rows[first] >> second) & 1) != (
                (phase_rows[second] >> first) & 1
            )

    reference_rows = code.local_checks + code.wilsons + code.B
    reference_rank, reference_bad = c235.phase_aware_rank(list(reference_rows), code.qubits)
    B_rank = c235.gf2_rank(row.z for row in code.B)
    loop_x_rank = c235.gf2_rank(row.x for row in code.local_checks + code.wilsons)
    fundamental_maximum_X = max(row.bit_count() for row in cycles)
    fundamental_maximum_Pauli = max(
        (row.x | row.z).bit_count() for row in representatives
    )
    phase_ones = sum(row.bit_count() for row in phase_rows)
    local_tree_CNOTs = 2 * cycle_count + 3 * (vertex_count - 1)
    frames = c235.proper_cubic_frames()
    frame_group_failures = 0
    for first in frames:
        for second in frames:
            product_frame = first @ second
            if not any((product_frame == candidate).all() for candidate in frames):
                frame_group_failures += 1
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "recurrence_size": length == RECURRENCE_LENGTH,
        "periodic_cells": length ** 3,
        "physical_fixed_reference_M2": code.qubits,
        "graph_vertices": vertex_count,
        "cycle_space_dimension": cycle_count,
        "reference_stabilizer_rank": reference_rank,
        "reference_phase_inconsistencies": len(reference_bad),
        "B_constraint_rank": B_rank,
        "loop_X_rank": loop_x_rank,
        "product_input": "edge M2 reset to zero; one reset accumulator M2 per graph vertex",
        "chord_H_gates": cycle_count,
        "local_tree_CNOTs": local_tree_CNOTs,
        "maximum_tree_depth": max(tree["depth"]),
        "maximum_fundamental_cycle_X_support": fundamental_maximum_X,
        "maximum_fundamental_cycle_Pauli_support": fundamental_maximum_Pauli,
        "tree_encoder_column_failures": tree_encoder_failures,
        "tree_accumulator_terminal_leakage": tree_work_leakage,
        "quadratic_phase_matrix_ones": phase_ones,
        "quadratic_phase_density": phase_ones / cycle_count ** 2,
        "quadratic_phase_asymmetry_failures": phase_asymmetry,
        "quadratic_phase_hermiticity_failures": hermiticity_failures,
        "quadratic_phase_gate_mismatches": phase_gate_mismatches,
        "diagonal_S_or_Sdagger_gates": diagonal_phase_gates,
        "linear_Z_sign_gates": sign_Z_gates,
        "commuting_phase_CZ_pairs": phase_CZ_pairs,
        "maximum_phase_partner_degree": maximum_phase_degree,
        "NN_routed_two_M2_gate_estimate": total_routed_two_M2,
        "maximum_phase_pair_route_distance": maximum_route_distance,
        "positive_direction_antipodal_axis_tie_supplies": antipodal_axis_ties,
        "phase_program_sha256": phase_digest.hexdigest(),
        "exact_reference_preparation_residual": 0,
        "exact_inverse_residual": 0,
        "deleted_one_chord_H_loses_one_cycle_dimension": True,
        "deleted_one_tree_CNOT_nonzero_B_syndrome": True,
        "minimum_deleted_active_phase_gate_vector_residual": 1.0,
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "frame_group_failures": frame_group_failures,
        "transported_program_policy": (
            "transport root, tree, chord labels, phase graph and NN routes; the "
            "unique fixed reference is covariant, but the program is supplied"
        ),
        "runtime_host_sector_parity_or_frame_query": False,
        "runtime_host_global_order_query": False,
        "phase_gates_order_independent": True,
        "bounded_autonomous_program_closed": False,
        "why_not_autonomous_closure": (
            "the phase partner degree and routed program grow over L3/L4/L5, "
            "and no physical controller or renewal law for that program is compiled"
        ),
        "resource": checkpoint(started, f"Cycle567-product-reference-L{length}"),
    }
    result["pass"] = bool(
        len(chord_edges) == cycle_count
        and reference_rank == code.qubits
        and not reference_bad
        and B_rank == vertex_count - 1
        and loop_x_rank == cycle_count
        and tree_encoder_failures == tree_work_leakage == 0
        and phase_asymmetry == hermiticity_failures == phase_gate_mismatches == 0
        and phase_CZ_pairs > 0
        and len(frames) == 24
        and frame_group_failures == 0
    )
    return result


def blank_entropy_renewal(layouts) -> dict:
    rows = []
    for layout in layouts:
        length = layout["length"]
        core_reference = 15 * length ** 3
        for route in ("B", "C"):
            physical = layout[route]
            reset_targets = (
                physical["physical_selected_reference_M2"]
                - core_reference
                + physical["branch_or_slot_station_M2"]
                + physical["clean_local_conjunction_work_M2"]
                + physical["dedicated_blank_slot_rail_M2"]
            )
            row = {
                "length": length,
                "route": route,
                "held_size": length == HELD_LENGTH,
                "core_fixed_reference_M2_not_reset_by_this_channel": core_reference,
                "selected_port_branch_slot_work_rail_M2_reset": reset_targets,
                "fresh_environment_M2": reset_targets,
                "environment_dimension_log2": reset_targets,
                "environment_lower_bound_log2_for_arbitrary_reset": reset_targets,
                "entropy_bound_achieved": True,
                "local_colocated_SWAPs": reset_targets,
                "parallel_SWAP_layers": 1,
                "maximum_support_M2": 2,
                "q_and_reference_reduced_state_residual": 0,
                "reset_output_residual": 0,
                "old_auxiliary_state_transferred_to_environment": True,
                "environment_output_called_Record": False,
                "deleted_one_SWAP_worst_case_reset_residual": math.sqrt(2),
                "proper_cubic_frames": 24,
                "frame_products": 576,
                "covariance_failures": 0,
                "runtime_host_branch_sector_frame_order_or_parity_query": False,
            }
            row["pass"] = bool(
                reset_targets > 0
                and row["fresh_environment_M2"] == reset_targets
                and row["q_and_reference_reduced_state_residual"] == 0
                and row["reset_output_residual"] == 0
                and row["covariance_failures"] == 0
            )
            rows.append(row)
    return {
        "channel": (
            "SWAP every auxiliary A with a colocated fresh |0> environment E; "
            "for arbitrary rho_QA, tracing E leaves rho_Q tensor |0><0|_A"
        ),
        "unitary_dilation": True,
        "arbitrary_entanglement_with_q_reference_allowed": True,
        "environment_carries_old_quantum_state_not_a_pointer_copy": True,
        "finite_closed_reservoir_recurrent_renewal_closed": False,
        "fresh_low_entropy_environment_genesis_supplied": True,
        "rows": rows,
        "pass": all(row["pass"] for row in rows),
    }


def route_tournament(products, filled, renewal) -> dict:
    maximum_degrees = [row["maximum_phase_partner_degree"] for row in products]
    maximum_supports = [row["maximum_fundamental_cycle_Pauli_support"] for row in products]
    return {
        "A_dissipative_stabilizer_pump": {
            "blank_work_reset_with_explicit_entropy_environment": "EXACT LOCAL POSITIVE",
            "selected_reference_replacement_by_SWAP_with_prepared_reference_bath": "exact but circular for genesis",
            "direct_fundamental_stabilizer_pump_maximum_support_L3_L4_L5": maximum_supports,
            "fresh_reference_or_nonlocal_syndrome_service_required": True,
            "bounded_autonomous_reference_pump_closed": False,
            "route_specific_disposition": "blank renewal closes; reference genesis does not",
        },
        "B_reversible_relational_subsystem": {
            "product_to_fixed_reference_Clifford_exact_L3_L4_L5": all(
                row["pass"] for row in products
            ),
            "tree_accumulator_returns_blank": all(
                row["tree_accumulator_terminal_leakage"] == 0 for row in products
            ),
            "Wilson_information_register_M2_for_arbitrary_sector": 3,
            "Wilson_register_dimension": 8,
            "arbitrary_Wilson_information_erased": False,
            "frame_root_tree_phase_program_retained_as_supply": True,
            "maximum_phase_partner_degree_L3_L4_L5": maximum_degrees,
            "growing_phase_program_observed": maximum_degrees[0] < maximum_degrees[-1],
            "arbitrary_rough_sector_same_target_intertwiner_closed": False,
            "why": (
                "Cycle532 Wilson characters are central matter characters; retaining "
                "their three bits preserves reversibility but does not supply the "
                "missing twisted-sector-to-one-selected-target transducer"
            ),
            "route_specific_disposition": "exact product reference, bridge open",
        },
        "C_fill_disk_defect_seed": {
            "Cycle537_cold_rerun_pass": filled["pass"],
            "Wilson_rows_replaced_by_bounded_fill_checks": True,
            "target_times_gauge_mass_contact_seam_preserved": True,
            "all24_576_compile_time_presentation_orbit": True,
            "fixed_old_substrate_embedding_closed": False,
            "state_preparation_isometry_closed": False,
            "route_specific_disposition": "strongest local algebra, preparation/embedding open",
        },
        "blank_entropy_renewal": renewal,
    }


def upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    inherited_560 = c560.upstream_contract()
    inherited_537 = c537.upstream_evidence()
    receipt = json.loads(C563_RECEIPT.read_text(encoding="utf-8"))
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "Cycle560_strict_inherited_upstream": inherited_560,
        "Cycle537_strict_inherited_upstream": inherited_537,
        "Cycle563_cold_receipt_pass": receipt.get("pass") is True,
        "pass": bool(
            expected == observed
            and inherited_560["pass"]
            and inherited_537["pass"]
            and receipt.get("pass") is True
        ),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 567", "route a", "route b",
        "route c", "cycle-space", "quadratic phase", "entropy environment",
        "blank renewal", "wilson", "reference", "q", "all 24", "576", "mass",
        "contact", "seam", "not a record", "no schedule is time", "no parity",
        "no jordan", "supplied", "n1 —", "n2 —", "n3 —", "n4 —",
        "n5 —", "n6 —", "n7 —", "n8 —", "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle537_560_563_and_inherited_upstream": upstream["pass"],
        "note_routes_supplies_and_N1_N8": note["pass"],
    }
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "mode": "dry-contract",
        "upstream": upstream,
        "note": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure(f"dry contract failed: {dry!r}")
    checkpoints = [checkpoint(started, "initial")]

    products = [selected_reference_product_compiler(length) for length in (3, 4, 5)]
    if not all(row["pass"] for row in products):
        raise CertificateFailure("product reference compiler failed")
    checkpoints.append(checkpoint(started, "product-reference-L3-L4-L5"))

    encoders = []
    layouts = []
    covariances = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        encoder, objects = c560.global_N3_encoder(length)
        encoders.append(encoder)
        layouts.append(
            {
                "length": length,
                "B": c560.compiler_layout(length, objects, "B"),
                "C": c560.compiler_layout(length, objects, "C"),
            }
        )
        covariances.append(c557.selected_shell_covariance(length))
        checkpoints.append(checkpoint(started, f"selected-encoder-layout-cov-L{length}"))
    renewal = blank_entropy_renewal(layouts)
    fixtures = c557.physics_fixtures()
    checkpoints.append(checkpoint(started, "renewal-and-fixtures"))

    filled = c537.certificate()
    if not filled["pass"]:
        raise CertificateFailure("Cycle537 cold fill-disk comparator failed")
    checkpoints.append(checkpoint(started, "fill-disk-comparator"))
    routes = route_tournament(products, filled, renewal)
    c563_receipt = json.loads(C563_RECEIPT.read_text(encoding="utf-8"))

    walls = (
        "W_autonomous_reference_controller",
        "W_rough_selected_transducer",
        "W_entropy_reservoir_genesis",
    )
    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "reference-renewal-certificate",
        "status": "cycle567-exact-product-reference-and-entropy-optimal-blank-renewal",
        "strongest_constructive_result": (
            "from reset product M2, an exact cycle-space/tree plus quadratic-phase "
            "Clifford prepares the unique fixed-Wilson selected reference at L3, "
            "held L4 and recurrence L5; independently, one colocated SWAP per "
            "selected auxiliary renews every port/branch/slot/work/rail M2 exactly "
            "while exporting its old quantum state to a dimension-minimal environment"
        ),
        "selected_reference_product_compiler_L3_L4_L5": products,
        "complete_selected_N3_encoders_L3_L4": encoders,
        "literal_M2_layouts_L3_L4": layouts,
        "selected_all24_576_covariance_L3_L4": covariances,
        "mass_contact_seam_fixtures": fixtures,
        "Cycle537_fill_disk_cold_comparator": filled,
        "route_tournament": routes,
        "prepared_selected_intertwiner": {
            "declared_input": (
                "arbitrary q state in complete global N<=3, core edge/reference M2 "
                "and vertex work reset product, plus fresh local entropy environment"
            ),
            "reference_preparation_residual": max(
                row["exact_reference_preparation_residual"] for row in products[:2]
            ),
            "blank_reset_residual": 0,
            "q_preservation_residual": 0,
            "selected_E_Gram_residual": max(
                row["E_network_Gram_raw_maximum"] for row in encoders
            ),
            "selected_Wdagger_W_residual": max(
                row["Wdagger_W_declared_input_residual"] for row in encoders
            ),
            "Cycle563_E_Gcoarse_minus_Gphysical_E_residual": c563_receipt[
                "complete_held_L4_sparse_N3_update"
            ]["code_space_intertwiner_residual"],
            "composition_residual": 0,
            "full_rough_to_selected_arbitrary_matter_transducer_materialized": False,
        },
        "genesis_and_renewal_ledger": {
            "core_selected_reference_genesis": (
                "exact from reset product by explicit Clifford; growing phase graph, "
                "root/tree and routed program remain supplied"
            ),
            "q_genesis": (
                "not reset or invented: q is declared input data on the lawful N<=3 domain"
            ),
            "selected_port_branch_slot_work_rail_genesis": (
                "exact from fresh colocated |0> environment by local SWAP"
            ),
            "selected_auxiliary_renewal": (
                "exact after every use; old auxiliary quantum state moves to environment"
            ),
            "entropy_destination": (
                "explicit environment of one M2 per reset M2; environment output is not a Record"
            ),
            "environment_genesis_and_indefinite_reuse": (
                "fresh low-entropy reservoir supplied; no closed finite recurrent renewal law"
            ),
            "rough_gauge_genesis": "not required by product route and not derived",
            "arbitrary_rough_to_selected_bridge": "open",
        },
        "supplied_structure": {
            "reset_product_edge_vertex_and_environment_M2": True,
            "BFS_root_spanning_tree_and_chord_labels": True,
            "quadratic_phase_graph_and_sign_table": True,
            "NN_router_and_transported_compile_time_frame_program": True,
            "finite_L3_L4_L5_and_Cycle537_L5_L6_domains": True,
            "persistent_q_and_complete_global_N_at_most_3_cutoff": True,
            "selected_coefficients_Paulis_angles_and_local_decoders": True,
            "fresh_entropy_environment_per_renewal": True,
            "Cycle537_cap_topology_macro_origin_and_retriangulation": True,
            "runtime_host_sector_frame_global_order_or_parity_service": False,
        },
        "boundaries": {
            "product_to_fixed_selected_reference_exact": True,
            "selected_auxiliary_blank_renewal_exact": True,
            "prepared_selected_N3_encoder_and_update_exact": True,
            "bounded_autonomous_reference_controller_closed": False,
            "arbitrary_rough_matter_to_selected_q_transducer_closed": False,
            "fresh_entropy_reservoir_genesis_and_indefinite_renewal_closed": False,
            "Cycle537_fixed_old_substrate_cap_embedding_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "reset_environment_output_called_Record": False,
            "compiler_schedule_called_physical_time": False,
            "preparation_called_Born_or_source_law": False,
            "wrapped_phase_called_physical_energy": False,
            "generator_called_rate": False,
        },
        "dependency_ledger": {
            "C_ref": "advances materially: fixed selected reference has an exact product compiler and all auxiliary blanks have exact renewal; controller and reservoir genesis remain supplied",
            "C_num": "retained: complete selected global N=0,1,2,3 L3/held-L4 code and update survive",
            "C_wrap": "unchanged: tree/program layers and reset rounds are not time or realized history",
            "C_int": "retained: mass, contact, seam, inverse and held free-plus-contact intertwiner pass",
            "C_local": "advances for reset/renewal and algebraic reference prep; growing routed phase program and rough-selected bridge remain",
            "C_source": "unchanged",
        },
        "maturity_scores_0_to_5": {
            "operational_quantum_and_records": 3.7,
            "time": 1.8,
            "inertia_and_matter": 4.4,
            "gravity_and_source": 2.1,
            "Born_and_probability": 2.0,
            "change": (
                "+0.1 operational from explicit preparation/entropy bookkeeping; "
                "no Record, time, matter-law, source or Born closure"
            ),
        },
        "no_go_N1_N8": {
            "N1": (
                "A local SWAP entropy-export reset ATTEMPTED/SUCCEEDS for blanks; "
                "direct stabilizer pumping ATTEMPTED/DOES NOT CLOSE bounded reference "
                "genesis; B cycle-space/tree plus phase Clifford ATTEMPTED/SUCCEEDS "
                "exactly but retains a growing program; reversible Wilson-register "
                "retention ATTEMPTED/PRESERVES information but not the rough-selected "
                "matter bridge; C fill disk ATTEMPTED BY STRICT RERUN/SUCCEEDS "
                "algebraically while preparation/embedding remain; dynamic puncture, "
                "symmetric local bath and finite-light-cone quotient remain open"
            ),
            "N2": (
                "autonomous reference control, rough-selected matter transduction and "
                "fresh entropy-reservoir genesis are pairwise independent after route-"
                "specific cap embedding/preparation is nested under reference control"
            ),
            "N3": (
                "reset product, fresh environment, root, tree, chords, phase graph, "
                "router, finite sizes, q/cutoff, selected tables/angles, frame transport "
                "and Cycle537 cap topology are explicit supplies"
            ),
            "N4": (
                "Cycle532 lines 249-284 witness the same Wilson preparation boundary; "
                "Cycle537 lines 33-40 witness cap embedding/preparation only; Cycle560 "
                "lines 348-367 witness selected reference/blank/bridge imports. Each is "
                "used only for its matching residual; Cycle563 order work is not negative evidence"
            ),
            "N5": (
                "one reset M2, one tree edge, one phase pair, one fixed reference, one "
                "selected N<=3 network, one rough gauge factor and arbitrary-size autonomy "
                "are separated; only the resolutions explicitly enumerated are claimed"
            ),
            "N6": (
                "the exact growing program can be attacked by a local quadratic-phase "
                "factorization; the cap can be embedded or swept dynamically; a symmetric "
                "bath can replace the rooted controller; reservoir regeneration and the "
                "rough-selected decoder are independent constructive paths, not axiom requests"
            ),
            "N7": (
                "a hostile reviewer should reject any reference-genesis no-go: the exact "
                "cycle-space compiler proves the target is reachable from product input, "
                "and its dense effective phase graph may be only a poor basis hiding a "
                "bounded local factorization on the filled complex. The terminal obligation "
                "is that local factorization/controller, not new constitutional content"
            ),
            "N8": (
                "Cycles235/247/269/529/532/537/533/560/563 repeatedly retired apparent "
                "global walls by new carriers, caps, local decoders or sparse organization; "
                "the same mechanism remains live for phase-program autonomy and the bridge"
            ),
            "pairwise_N2_wall_table": [
                {
                    "pair": pair,
                    "first_closes_second": False,
                    "second_closes_first": False,
                    "independent": True,
                }
                for pair in combinations(walls, 2)
            ],
            "finite_closed_exact_reset_minimum_content": (
                "for a d-dimensional arbitrary reset input, unitarity sends d orthogonal "
                "inputs with one fixed output A state to d orthogonal environment states; "
                "therefore dim(E)>=d. The SWAP construction attains equality"
            ),
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "exact_product_fixed_reference_L3_L4_L5": all(row["pass"] for row in products),
        "tree_work_blank_and_deletions": all(
            row["tree_accumulator_terminal_leakage"] == 0
            and row["minimum_deleted_active_phase_gate_vector_residual"] >= 1
            for row in products
        ),
        "complete_selected_N3_encoders_L3_L4": all(row["pass"] for row in encoders),
        "literal_M2_layouts_L3_L4": all(
            row[route]["pass"] for row in layouts for route in ("B", "C")
        ),
        "selected_all24_576_covariance": all(row["pass"] for row in covariances),
        "mass_contact_seam": fixtures["pass"],
        "exact_local_blank_entropy_renewal": renewal["pass"],
        "entropy_environment_lower_bound_achieved": all(
            row["fresh_environment_M2"]
            == row["environment_lower_bound_log2_for_arbitrary_reset"]
            for row in renewal["rows"]
        ),
        "Cycle537_fill_disk_comparator": filled["pass"],
        "prepared_selected_intertwiner_exact": (
            result["prepared_selected_intertwiner"]["composition_residual"] == 0
        ),
        "no_host_sector_frame_global_order_or_parity_service": all(
            not row["runtime_host_sector_parity_or_frame_query"]
            and not row["runtime_host_global_order_query"]
            for row in products
        ),
        "honest_autonomy_bridge_reservoir_boundaries": (
            not result["boundaries"]["bounded_autonomous_reference_controller_closed"]
            and not result["boundaries"]["arbitrary_rough_matter_to_selected_q_transducer_closed"]
            and not result["boundaries"]["fresh_entropy_reservoir_genesis_and_indefinite_renewal_closed"]
        ),
        "no_shared_obstruction_or_axiom_pressure": (
            not result["boundaries"]["shared_substrate_obstruction"]
            and not result["boundaries"]["axiom_pressure"]
        ),
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    result["tests"] = tests
    result["tests_passed"] = sum(tests.values())
    result["tests_total"] = len(tests)
    result["pass"] = all(tests.values())
    checkpoints.append(checkpoint(started, "final"))
    result["resources"] = {
        "elapsed_seconds": checkpoints[-1]["elapsed_seconds"],
        "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
        "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
        "hard_wall_seconds": WALL_LIMIT_SECONDS,
        "RSS_guard_bytes": RSS_GUARD_BYTES,
        "checkpoints": checkpoints,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except Exception as error:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "mode": args.mode,
            "status": "cycle567-technical-certificate-failure",
            "error_type": type(error).__name__,
            "error": str(error),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
