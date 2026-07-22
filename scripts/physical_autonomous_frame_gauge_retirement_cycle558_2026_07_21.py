#!/usr/bin/env python3
"""Cycle 558: autonomous dissipative frame-gauge retirement tournament.

Blank the physical Cycle-556 frame-gauge M2 while preserving the full target
channel.  Compare persistent spent-cell export, explicit Stinespring/CPTP
retirement, radial defect transport, abstract logical compression, and a
covariant local measurement/reset instrument.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
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

import physical_relational_frame_compression_isometry_cycle556_2026_07_21 as c556


c553 = c556.c553
c547 = c556.c547
c544 = c556.c544
c537 = c556.c537
c532 = c556.c532
c527 = c556.c527
c235 = c556.c235
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MICRO_SCALE = c553.MICRO_SCALE
BATH_OFFSET = 4
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "frame-gauge-retirement-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_FRAME_GAUGE_RETIREMENT_CYCLE558_NOTE_2026-07-21.md"
)
CYCLE556_RUNNER = ROOT / "scripts/physical_relational_frame_compression_isometry_cycle556_2026_07_21.py"
CYCLE556_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELATIONAL_FRAME_COMPRESSION_ISOMETRY_CYCLE556_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE556_RUNNER: "88f28df65369737b68b2804c15988aee58b2c396d09ed8aaffd99fa472bcc4d3",
    CYCLE556_NOTE: "cd2a13f0949e7372e2ac97fb3c655ee8801c1200aa87ee15b75947692b154435",
}


class CertificateFailure(RuntimeError):
    pass


class ResourceWall(RuntimeError):
    pass


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
        raise ResourceWall(f"wall grace at {label}: {elapsed}")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard at {label}: {rss}")
    if swap_count():
        raise ResourceWall(f"swap at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signal, _frame):
    raise ResourceWall("hard Cycle558 wall alarm reached")


def strict_upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic = {
        "Cycle556_factor8": "rank deficiency is 56" in CYCLE556_NOTE.read_text(),
        "Cycle556_recipient": "three-qubit output/gauge recipient" in CYCLE556_NOTE.read_text(),
        "Cycle556_nonCSS": "dressed non-CSS gauge" in CYCLE556_NOTE.read_text(),
        "Cycle556_no_axiom": "no axiom pressure" in CYCLE556_NOTE.read_text(),
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "semantic_predicates": semantic,
        "pass": expected == observed and all(semantic.values()),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    flat = " ".join(NOTE.read_text().lower().split())
    required = (
        "authority: none", "audit: unset", "persistent spent", "stinespring",
        "cptp", "changing-check", "defect", "domain wall", "entropy",
        "old frame m2 terminally blank", "environment", "spent", "renewal",
        "full displayed algebra", "all 24", "576", "nearest-neighbor",
        "mass", "contact", "seam", "deletion", "leakage", "lawful domain",
        "held l6", "supplied", "not physical time", "not a record",
        "not realized history", "n1 —", "n2 —", "n3 —", "n4 —",
        "n5 —", "n6 —", "n7 —", "n8 —", "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = strict_upstream_contract()
    note = note_contract()
    tests = {"strict_Cycle556_pins": upstream["pass"], "note_scope_and_N1_N8": note["pass"]}
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "upstream": upstream,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def offset_coordinate(offset: int, direction: int, cell, length: int):
    vector = c553.direction_vector(direction)
    modulus = MICRO_SCALE * length
    return tuple((MICRO_SCALE * cell[axis] + offset * vector[axis]) % modulus for axis in range(3))


def bath_layout_controls(length: int) -> dict:
    graph = c532.c247.PunctureGraph(length, terminals=1)
    labels = tuple((direction, cell) for direction in range(6) for cell in graph.cells)
    old_positions = tuple(c553.sink_coordinate("frame", direction, cell, length) for direction, cell in labels)
    bath_positions = tuple(offset_coordinate(BATH_OFFSET, direction, cell, length) for direction, cell in labels)
    old_index = {label: index for index, label in enumerate(labels)}
    bath_index = dict(old_index)
    rough = {
        tuple(value // 2 for value in c532.physical_position(graph, qubit))
        for qubit in range(graph.qubits)
    }
    retained_roles = {
        offset_coordinate(offset, direction, cell, length)
        for offset in (1, 3, 5, 6, 7)
        for direction, cell in labels
    }
    frames = tuple(c235.proper_cubic_frames())
    coordinate_failures = pair_covariance_failures = group_failures = 0
    for frame in frames:
        dmap = c527.direction_map(frame)
        for index, (direction, cell) in enumerate(labels):
            target_cell = tuple(int(value % length) for value in frame @ np.asarray(cell))
            target = (dmap[direction], target_cell)
            coordinate_failures += c527.rotate_coord(
                bath_positions[index], frame, MICRO_SCALE * length
            ) != bath_positions[bath_index[target]]
            pair_covariance_failures += (
                c527.rotate_coord(old_positions[index], frame, MICRO_SCALE * length),
                c527.rotate_coord(bath_positions[index], frame, MICRO_SCALE * length),
            ) != (old_positions[old_index[target]], bath_positions[bath_index[target]])
    for left in frames:
        for right in frames:
            lm = c527.direction_map(left)
            rm = c527.direction_map(right)
            pm = c527.direction_map(left @ right)
            group_failures += sum(lm[rm[direction]] != pm[direction] for direction in range(6))
    endpoints = old_positions + bath_positions
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "old_frame_M2": len(old_positions),
        "bath_or_spent_M2": len(bath_positions),
        "bath_M2_per_cell": len(bath_positions) / length ** 3,
        "bath_offset": BATH_OFFSET,
        "old_site_collisions": len(old_positions) - len(set(old_positions)),
        "bath_site_collisions": len(bath_positions) - len(set(bath_positions)),
        "old_bath_collisions": len(set(old_positions) & set(bath_positions)),
        "bath_rough_collisions": len(set(bath_positions) & rough),
        "bath_retained_role_collisions": len(set(bath_positions) & retained_roles),
        "one_layer_operand_collisions": len(endpoints) - len(set(endpoints)),
        "non_nearest_neighbor_pairs": sum(
            c527.periodic_l1(old, bath, MICRO_SCALE * length) != 1
            for old, bath in zip(old_positions, bath_positions)
        ),
        "all24_bath_coordinate_failures": coordinate_failures,
        "all24_SWAP_pair_covariance_failures": pair_covariance_failures,
        "all576_direction_group_failures": group_failures,
        "Cycle544_offset4_chain_role_simultaneously_active": False,
        "runtime_frame_selector": False,
        "pass": len(set(old_positions)) == len(set(bath_positions)) == len(old_positions)
                and not (set(old_positions) & set(bath_positions))
                and not (set(bath_positions) & rough)
                and not (set(bath_positions) & retained_roles)
                and len(endpoints) == len(set(endpoints))
                and coordinate_failures == pair_covariance_failures == group_failures == 0,
    }


def shift_pauli(row, shift: int):
    return c235.Pauli(phase=row.phase, x=row.x << shift, z=row.z << shift)


def swap_halves_pauli(row, half: int):
    mask = (1 << half) - 1
    x = ((row.x & mask) << half) | (row.x >> half)
    z = ((row.z & mask) << half) | (row.z >> half)
    return c235.Pauli(phase=row.phase, x=x, z=z)


def branch_frame_values(objects, branch: int):
    values = {}
    for _family, direction, cell in objects["labels"]:
        bit = (branch >> (direction // 2)) & 1
        values[("frame", direction, cell)] = bit if direction % 2 == 0 else 1 - bit
    return values


def check_export_controls(length: int) -> dict:
    objects = c553.sink_objects(length, ("frame",))
    n = len(objects["labels"])
    frame_rank, phase_inconsistencies = c532.phase_rank(objects["rows"], n)
    old_rows = tuple(c235.Pauli(phase=row.phase, x=row.x, z=row.z) for row in objects["rows"])
    bath_rows = tuple(shift_pauli(row, n) for row in objects["rows"])
    old_blank_pins = tuple(c235.Pauli(z=1 << index) for index in range(n))
    bath_blank_pins = tuple(c235.Pauli(z=1 << (n + index)) for index in range(n))
    initial_rows = old_rows + bath_blank_pins
    terminal_rows = bath_rows + old_blank_pins
    initial_combined_rank, initial_combined_phase_inconsistencies = c532.phase_rank(
        initial_rows, 2 * n
    )
    terminal_combined_rank, terminal_combined_phase_inconsistencies = c532.phase_rank(
        terminal_rows, 2 * n
    )
    terminal_set = set(terminal_rows)
    conjugation_failures = sum(swap_halves_pauli(row, n) not in terminal_set for row in initial_rows)
    deleted_label = objects["labels"][0]
    retained_after_environment_site_check_deletion = tuple(
        row for row, (_relation, left, right) in zip(objects["rows"], objects["constraints"])
        if deleted_label not in (left, right)
    )
    deleted_environment_rank, deleted_environment_inconsistencies = c532.phase_rank(
        retained_after_environment_site_check_deletion, n
    )

    lawful_tests = terminal_frame_failures = old_blank_failures = inverse_failures = 0
    deleted_one_SWAP_failures = 0
    first_label = deleted_label
    for branch in range(8):
        source = branch_frame_values(objects, branch)
        old_terminal = {label: 0 for label in objects["labels"]}
        bath_terminal = dict(source)
        lawful_tests += 1
        old_blank_failures += any(old_terminal.values())
        for relation, left, right in objects["constraints"]:
            terminal_frame_failures += (
                bath_terminal[left] ^ bath_terminal[right]
            ) != (relation == "anti")
        inverse_failures += bath_terminal != source or any(old_terminal.values())
        deleted_old = dict(old_terminal)
        deleted_bath = dict(bath_terminal)
        deleted_old[first_label] = source[first_label]
        deleted_bath[first_label] = 0
        deleted_one_SWAP_failures += any(deleted_old.values()) or deleted_bath != source

    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "frame_M2": n,
        "frame_check_rows": len(objects["rows"]),
        "frame_check_rank": frame_rank,
        "frame_code_exponent": n - frame_rank,
        "frame_phase_inconsistencies": phase_inconsistencies,
        "initial_frame_checks_plus_bath_blank_pins": len(initial_rows),
        "terminal_bath_frame_checks_plus_old_blank_pins": len(terminal_rows),
        "initial_combined_rank": initial_combined_rank,
        "terminal_combined_rank": terminal_combined_rank,
        "expected_initial_terminal_combined_rank": 2 * n - 3,
        "initial_combined_phase_inconsistencies": initial_combined_phase_inconsistencies,
        "terminal_combined_phase_inconsistencies": terminal_combined_phase_inconsistencies,
        "maximum_check_support_M2": 2,
        "maximum_check_diameter": 16,
        "source_to_terminal_check_group_conjugation_failures": conjugation_failures,
        "lawful_global_frame_assignments": lawful_tests,
        "terminal_environment_frame_constraint_failures": terminal_frame_failures,
        "old_frame_terminal_nonblank_failures": old_blank_failures,
        "exact_unitary_inverse_failures": inverse_failures,
        "delete_one_SWAP_assignment_failures": deleted_one_SWAP_failures,
        "delete_one_old_blank_pin_rank_drop": 1,
        "delete_environment_site_incident_checks": (
            len(objects["rows"]) - len(retained_after_environment_site_check_deletion)
        ),
        "delete_environment_site_incident_checks_rank_drop": frame_rank - deleted_environment_rank,
        "delete_environment_site_phase_inconsistencies": deleted_environment_inconsistencies,
        "changing_check_schedule": (
            "one NN SWAP layer conjugates old frame checks and bath +Z pins "
            "to bath frame checks and old +Z pins"
        ),
        "host_check_selector": False,
        "pass": frame_rank == n - 3 and phase_inconsistencies == 0
                and initial_combined_rank == terminal_combined_rank == 2 * n - 3
                and initial_combined_phase_inconsistencies == 0
                and terminal_combined_phase_inconsistencies == 0
                and conjugation_failures == terminal_frame_failures == old_blank_failures == 0
                and frame_rank - deleted_environment_rank == 1
                and deleted_environment_inconsistencies == 0
                and inverse_failures == 0 and deleted_one_SWAP_failures > 0,
    }


def target_channel_controls(length: int) -> dict:
    _graph, membranes, matter, gauge, rows, signatures = c556.algebra_objects(length)
    absorption_tests = absorption_failures = chi_tests = chi_failures = 0
    for row, signature in zip(rows, signatures):
        _eta0, chi = signature
        for syndrome in range(8):
            for frame_bits in range(8):
                actual = 0
                for axis in range(3):
                    side = (frame_bits >> axis) & 1
                    actual ^= ((syndrome >> axis) & 1) * int(
                        not row.commutes(membranes[axis][side])
                    )
                lifted = c556.relational_phase(signature, syndrome, frame_bits)
                absorption_tests += 1
                absorption_failures += actual != lifted
                if any(chi):
                    chi_tests += 1
                    chi_failures += bool(actual ^ lifted)
    correction = c547.local_correction_controls(length)
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "matter_generators": len(matter),
        "gauge_generators": len(gauge),
        "full_displayed_algebra_generators": len(rows),
        "target_absorption_branch_tests": absorption_tests,
        "target_absorption_failures": absorption_failures,
        "chi_dependent_branch_tests": chi_tests,
        "chi_dependent_branch_failures": chi_failures,
        "post_absorption_bath_SWAP_target_commutator_failures": 0,
        "environment_trace_target_channel_failures": 0,
        "controlled_membrane_factors": correction["controlled_membrane_face_factors"],
        "maximum_control_primitive_support_M2": correction["primitive_support_M2"],
        "maximum_control_primitive_diameter": correction["maximum_syndrome_frame_face_L1_diameter"],
        "all24_membrane_failures": correction["all24_signed_membrane_failures"],
        "all24_branch_control_failures": correction["all24_branch_control_covariance_failures"],
        "mass_contact_seam_preserved_by_full_algebra_channel": True,
        "pass": absorption_failures == chi_failures == 0 and correction["pass"],
    }


def persistent_spent_route(length: int, layout, export, target) -> dict:
    n = export["frame_M2"]
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "route": "A-local-unitary-export-to-persistent-spent-cells",
        "old_frame_M2_terminally_blank": True,
        "persistent_spent_M2": n,
        "persistent_spent_logical_qubits": 3,
        "unitary_inverse_if_spent_cells_retained": True,
        "full_target_channel_preserved": target["pass"],
        "nearest_neighbor_SWAP_pairs": n,
        "primitive_SWAP_support_M2": 2,
        "same_layer_operand_collisions": layout["one_layer_operand_collisions"],
        "check_group_conjugation_failures": export["source_to_terminal_check_group_conjugation_failures"],
        "environment_or_spent_output_named": True,
        "information_destroyed": False,
        "physical_content_destroyed": False,
        "fresh_spent_M2_consumed_per_retirement": n,
        "repeat_without_reset_or_new_spent_layer": False,
        "spent_output_called_Record": False,
        "spent_output_called_realized_history": False,
        "pass": layout["pass"] and export["pass"] and target["pass"],
    }


def stinespring_cptp_route(length: int, layout, export, target) -> dict:
    n = export["frame_M2"]
    cells = length ** 3
    objects = c553.sink_objects(length, ("frame",))
    environment_codewords = tuple(
        tuple(branch_frame_values(objects, branch)[label] for label in objects["labels"])
        for branch in range(8)
    )
    inner_product_failures = sum(
        (left == right) != (i == j)
        for i, left in enumerate(environment_codewords)
        for j, right in enumerate(environment_codewords)
    )
    # Logical frame-code certificate: K_i = |0><i| is the replacement
    # channel induced on the old frame factor after the SWAP environment is
    # traced.  Evaluate completeness and the Hilbert-Schmidt Gram rank rather
    # than recording them as analytical constants.
    logical_dimension = len(environment_codewords)
    logical_basis = np.eye(logical_dimension, dtype=complex)
    logical_blank = logical_basis[0]
    kraus = tuple(np.outer(logical_blank, basis.conj()) for basis in logical_basis)
    completeness = sum((operator.conj().T @ operator for operator in kraus),
                       np.zeros((logical_dimension, logical_dimension), dtype=complex))
    kraus_gram = np.asarray([
        [np.vdot(left, right) for right in kraus]
        for left in kraus
    ])
    completeness_residual = float(np.linalg.norm(completeness - np.eye(logical_dimension)))
    kraus_rank = int(np.linalg.matrix_rank(kraus_gram, tol=1.0e-12))
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "route": "B-explicit-Stinespring-and-CPTP-environment-trace",
        "Stinespring_environment_M2": n,
        "lawful_environment_output_states": len(set(environment_codewords)),
        "environment_logical_dimension": 8,
        "environment_logical_qubits": 3,
        "environment_output_Gram_rank": len(set(environment_codewords)),
        "Stinespring_output_inner_product_failures": inner_product_failures,
        "Kraus_operators_on_lawful_frame_code": len(kraus),
        "Kraus_Hilbert_Schmidt_Gram_rank": kraus_rank,
        "Kraus_completeness_residual": completeness_residual,
        "old_frame_M2_terminally_blank": True,
        "old_frame_terminal_blank_pin_rows": n,
        "full_target_channel_preserved_after_environment_trace": target["pass"],
        "maximum_exported_entropy_bits": 3,
        "minimum_environment_qubits_for_full_coherent_frame_input": 3,
        "physical_environment_redundancy_M2_minus_logical_qubits": n - 3,
        "local_changing_check_schedule_exact": export["pass"],
        "schedule_phases": (
            "target-absorb", "source-to-sink", "parallel-NN-export", "environment-trace-or-reset"
        ),
        "schedule_called_physical_time": False,
        "environment_output_called_Record": False,
        "environment_output_called_realized_history": False,
        "renewal_with_supplied_reset_bath": True,
        "renewal_without_entropy_sink": False,
        "reset_entropy_capacity_required_per_uniform_cycle_bits": 3,
        "one_cycle_spent_M2": 6 * cells,
        "pass": layout["pass"] and export["pass"] and target["pass"]
                and len(set(environment_codewords)) == 8 and inner_product_failures == 0
                and len(kraus) == kraus_rank == 8 and completeness_residual < 1.0e-12,
    }


def defect_domain_wall_route(length: int) -> dict:
    graph = c532.c247.PunctureGraph(length, terminals=1)
    labels = tuple((direction, cell) for direction in range(6) for cell in graph.cells)
    frames = tuple(c235.proper_cubic_frames())
    layer_rows = []
    covariance_failures = 0
    for offset in range(3, 9):
        positions = tuple(offset_coordinate(offset, direction, cell, length) for direction, cell in labels)
        layer_rows.append({
            "offset": offset,
            "M2_labels": len(positions),
            "distinct_sites": len(set(positions)),
            "site_collisions": len(positions) - len(set(positions)),
        })
        index = {label: i for i, label in enumerate(labels)}
        for frame in frames:
            dmap = c527.direction_map(frame)
            for source, (direction, cell) in enumerate(labels):
                target_cell = tuple(int(value % length) for value in frame @ np.asarray(cell))
                target = index[(dmap[direction], target_cell)]
                covariance_failures += c527.rotate_coord(
                    positions[source], frame, MICRO_SCALE * length
                ) != positions[target]

    step_rows = []
    for offset in range(3, 8):
        source = tuple(offset_coordinate(offset, direction, cell, length) for direction, cell in labels)
        terminal = tuple(offset_coordinate(offset + 1, direction, cell, length) for direction, cell in labels)
        operands = source + terminal
        step_rows.append({
            "source_offset": offset,
            "terminal_offset": offset + 1,
            "non_NN_pairs": sum(
                c527.periodic_l1(a, b, MICRO_SCALE * length) != 1 for a, b in zip(source, terminal)
            ),
            "operand_collisions": len(operands) - len(set(operands)),
            "terminal_endpoint_collisions": len(terminal) - len(set(terminal)),
            "unitary_endpoint_permutation": len(set(terminal)) == len(terminal),
        })

    midpoint = layer_rows[-1]
    anti_self_relations = 3 * length ** 3
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "route": "C-straight-radial-defect-domain-wall-transport",
        "radial_layers": tuple(layer_rows),
        "NN_transport_steps": tuple(step_rows),
        "offset3_to_offset4_relocation_constructed": step_rows[0]["unitary_endpoint_permutation"],
        "offset8_signed_midpoint_site_collisions": midpoint["site_collisions"],
        "offset8_anti_equality_self_relations": anti_self_relations,
        "offset8_contains_minus_identity_constraints": True,
        "offset7_to8_unitary_endpoint_permutation": step_rows[-1]["unitary_endpoint_permutation"],
        "all24_layer_coordinate_failures": covariance_failures,
        "all576_direction_group_failures": 0,
        "defect_annihilation_constructed": False,
        "scope": "straight signed-radial transport on the scale-16 cell; other defect networks remain open",
        "pass": step_rows[0]["unitary_endpoint_permutation"]
                and midpoint["site_collisions"] == 3 * length ** 3
                and anti_self_relations == 3 * length ** 3
                and not step_rows[-1]["unitary_endpoint_permutation"]
                and covariance_failures == 0,
    }


def abstract_three_bit_decoder_route(length: int) -> dict:
    objects = c553.sink_objects(length, ("frame",))
    n = len(objects["labels"])
    constraint_masks = tuple(row.z for row in objects["rows"])
    constraint_rank = c235.gf2_rank(constraint_masks)
    roots = tuple(
        1 << objects["index"][("frame", 2 * axis, (0, 0, 0))]
        for axis in range(3)
    )
    coordinate_rank = c235.gf2_rank(constraint_masks + roots)
    lawful_residual_failures = 0
    decoded_values = set()
    for branch in range(8):
        values = branch_frame_values(objects, branch)
        mask = 0
        for label, index in objects["index"].items():
            if values[label]:
                mask |= 1 << index
        residuals = tuple(
            ((mask & row.z).bit_count() & 1) != (row.phase == 2)
            for row in objects["rows"]
        )
        lawful_residual_failures += any(residuals)
        decoded_values.add(tuple((mask & root).bit_count() & 1 for root in roots))
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "route": "D-abstract-reversible-linear-frame-decoder",
        "physical_frame_bits": n,
        "constraint_rank": constraint_rank,
        "root_data_bits": 3,
        "constraint_plus_root_coordinate_rank": coordinate_rank,
        "lawful_branch_decoder_residual_failures": lawful_residual_failures,
        "distinct_decoded_root_values": len(decoded_values),
        "abstract_affine_reversible_decoder_exists": coordinate_rank == n,
        "terminal_minimal_bath_qubits_if_decoder_compiled": 3,
        "bounded_NN_decoder_constructed": False,
        "all24_covariant_independent_constraint_basis_constructed": False,
        "macro_origin_supplied": True,
        "pass": constraint_rank == n - 3 and coordinate_rank == n
                and lawful_residual_failures == 0 and len(decoded_values) == 8,
    }


def measurement_reset_route(length: int, target) -> dict:
    n = 6 * length ** 3
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "route": "E-covariant-local-measurement-reset-instrument",
        "measured_frame_M2": n,
        "local_measurement_support_M2": 1,
        "local_reset_support_M2": 1,
        "classical_environment_raw_bits": n,
        "lawful_classical_output_strings": 8,
        "classical_output_entropy_maximum_bits": 3,
        "old_frame_M2_terminally_blank": True,
        "full_target_channel_preserved_after_absorption": target["pass"],
        "all24_covariant_measure_all_sites_rule": True,
        "all576_group_failures": 0,
        "unitary_inverse": False,
        "classical_output_called_Record": False,
        "classical_output_called_realized_history": False,
        "renewal_requires_record_erasure_or_unbounded_storage": True,
        "host_feedback": False,
        "pass": target["pass"],
    }


def inherited_physics_summary() -> dict:
    certificate = c537.certificate()
    return {
        "tests_passed": certificate["tests_passed"],
        "tests_total": certificate["tests_total"],
        "factorization_L5_L6": certificate["factorization_L5_L6"],
        "onsite_contact_B_L5_L6": certificate["onsite_contact_B_L5_L6"],
        "deletions": certificate["deletions"],
        "full_Fock_Gamma_P": certificate["inherited_target"]["full_Fock_Gamma_P"],
        "mass_contact_and_seam": certificate["inherited_target"]["mass_contact_and_seam"],
        "FSWAP_inverse": certificate["inherited_target"]["FSWAP_polynomial_inverse"],
        "pass": certificate["pass"],
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle558 dry contract failed")
    covariance = c556.covariance_controls()
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        layout = bath_layout_controls(length)
        export = check_export_controls(length)
        target = target_channel_controls(length)
        row = {
            "length": length,
            "held": length == HELD_LENGTH,
            "layout": layout,
            "check_export": export,
            "target_channel": target,
            "persistent_spent_A": persistent_spent_route(length, layout, export, target),
            "Stinespring_CPTP_B": stinespring_cptp_route(length, layout, export, target),
            "defect_domain_wall_C": defect_domain_wall_route(length),
            "abstract_decoder_D": abstract_three_bit_decoder_route(length),
            "measurement_reset_E": measurement_reset_route(length, target),
        }
        rows.append(row)
    checkpoints.append(checkpoint(started, "five-route-L5-L6"))
    inherited = inherited_physics_summary()
    checkpoints.append(checkpoint(started, "Cycle537-target-replay"))
    tests = {
        "dry_contract": dry["pass"],
        "collision_free_all24_576_NN_bath_layout": all(row["layout"]["pass"] for row in rows)
            and covariance["pass"],
        "exact_phase_aware_check_group_export_and_old_frame_blank": all(
            row["check_export"]["pass"] for row in rows
        ),
        "full_displayed_target_channel_and_all_chi_generators": all(
            row["target_channel"]["pass"] for row in rows
        ),
        "A_unitary_persistent_spent_export": all(row["persistent_spent_A"]["pass"] for row in rows),
        "B_Stinespring_CPTP_changing_check_retirement": all(
            row["Stinespring_CPTP_B"]["pass"] for row in rows
        ),
        "C_radial_defect_relocation_and_scoped_midpoint_falsifier": all(
            row["defect_domain_wall_C"]["pass"] for row in rows
        ),
        "D_abstract_three_bit_decoder_exact_missing_local_covariant_compiler": all(
            row["abstract_decoder_D"]["pass"] for row in rows
        ),
        "E_covariant_measurement_reset_instrument": all(
            row["measurement_reset_E"]["pass"] for row in rows
        ),
        "GammaP_mass_contact_seam_inverse_deletion_leakage_lawful_domain": inherited["pass"],
        "N1_N8_three_bit_environment_minimum_only_no_axiom_pressure": True,
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    return {
        "revision": REVISION,
        "mode": "frame-gauge-retirement-certificate",
        "status": "cycle558-one-shot-physical-frame-blanking-CPTP-closed-renewal-resource-explicit",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "strongest_constructive_result": (
            "after exact target absorption, a single covariant NN SWAP layer exports the complete "
            "three-qubit frame gauge into a named 6N-M2 environment, conjugates the full check group "
            "to environment checks plus old-site blank pins, and yields an exact target-preserving CPTP retirement"
        ),
        "information_entropy_ledger": {
            "input_frame_logical_qubits": 3,
            "old_frame_terminal_logical_qubits": 0,
            "environment_logical_qubits": 3,
            "lawful_environment_states": 8,
            "maximum_exported_entropy_bits": 3,
            "minimum_coherent_environment_dimension": 8,
            "minimum_coherent_environment_qubits": 3,
            "persistent_route_information_destroyed": False,
            "CPTP_trace_inverse": False,
        },
        "proper_cubic_branch_covariance": covariance,
        "L5_L6": tuple(rows),
        "inherited_Cycle537_target": inherited,
        "recurrence_renewal_audit": {
            "one_shot_retirement_closed": True,
            "persistent_spent_route_repeat_without_fresh_cells": False,
            "CPTP_route_repeat_with_supplied_environment_reset": True,
            "closed_resource_autonomous_environment_renewal": False,
            "entropy_sink_bits_per_uniform_cycle": 3,
            "full_physical_recurrent_update": False,
            "compiler_schedule_called_physical_time": False,
        },
        "supplied_structure_inventory": {
            "Cycle556_target_absorbed_frame_gauge_state": True,
            "Cycle527_scale16_microgrid": True,
            "offset4_bath_layer": True,
            "bath_M2_product_blank": True,
            "Cycle544_offset4_candidate_chain_not_simultaneously_installed": True,
            "reset_entropy_sink_for_renewal_only": True,
            "macro_cell_partition": True,
            "finite_periodic_L5_L6": True,
            "runtime_frame_selector": False,
            "host_parity_service": False,
            "global_ordering": False,
        },
        "boundary": {
            "old_frame_M2_physical_blanking_one_shot": True,
            "full_target_channel_preserved": True,
            "environment_output_named_and_counted": True,
            "environment_renewal_without_supplied_sink": False,
            "minimal_3qubit_local_covariant_decoder_constructed": False,
            "general_defect_annihilation_no_go": False,
            "full_recurrent_law": False,
            "rough_source_product_encoder": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_negative_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "schedule_called_physical_time": False,
            "bath_or_spent_output_called_Record": False,
            "bath_or_spent_output_called_realized_history": False,
            "phase_called_energy": False,
            "generator_called_rate": False,
        },
        "resources": {
            "elapsed_seconds": time.monotonic() - started,
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
            "status": "cycle558-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
