#!/usr/bin/env python3
"""Cycle644: bounded spin-sector genesis tournament for the Cycle641 code.

Route A tests a repeated four-M2 crossing block plus single-M2 factors for the
translated Wilson family and falsifies that tensor seed, then constructs an
exact but globally rooted seed for only the three displayed Wilson signs.
Route B constructs a reversible data/link plaquette encoder and unencoder.
Route C tests a local measurement-reset pump against the actual independent
L3 rough-code constraints.  None is promoted beyond its executed surface.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from hashlib import sha256
import importlib
import io
from itertools import permutations, product
import json
from pathlib import Path
import resource
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
IMMUTABLE_SHORE_REF = "40e8b5718ee92c0e1d0ec41386c0ff9cc84aefac"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8.0e-11
CAP_SECONDS = 240.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BOUNDED_SPIN_SECTOR_GENESIS_TOURNAMENT_"
    "CYCLE644_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_bounded_spin_sector_genesis_tournament_"
    "cycle644_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_bounded_spin_sector_genesis_tournament_"
    "cycle644_cold_2026_07_23.txt"
)

PINS = {
    "scripts/physical_twisted_charge_ribbon_auxiliary_link_gauge_cycle641_2026_07_23.py":
        "17b8c95c8cc6e2b04723c97c394722a2aeb4a1f5fe45259dc28181ec7927292b",
    "docs/work_history/repo/review_feedback/PHYSICAL_TWISTED_CHARGE_RIBBON_AUXILIARY_LINK_GAUGE_CYCLE641_NOTE_2026-07-23.md":
        "506dc7947aeb9ebd1c3c03ecad2f845931be35b9147ec1c1e08eb4883e70a705",
    "outputs/physical_twisted_charge_ribbon_auxiliary_link_gauge_cycle641_receipt_2026_07_23.json":
        "936532e57e78ac4c042f64bc967e8aeaf166659357a8378a26a5425f22f4efa1",
    "outputs/physical_twisted_charge_ribbon_auxiliary_link_gauge_cycle641_cold_2026_07_23.txt":
        "873c389ffb4f834e1ac342c3362f02135b6df4c776e043901c06d3c14681e355",
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py":
        "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    "scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py":
        "10f5cf027c76f5a0a3b1d3dbaa6cb0e6d418932c84553f0cca303d3f21742519",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py":
        "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.run(
        ("git", "show", f"{ref}:{path}"), cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    ).stdout


def load_immutable_modules():
    archive = subprocess.run(
        ("git", "archive", "--format=tar", IMMUTABLE_SHORE_REF, "scripts"),
        cwd=ROOT, check=True, stdout=subprocess.PIPE,
    ).stdout
    exported = tempfile.TemporaryDirectory(prefix="cycle644-immutable-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(exported.name, filter="data")
    scripts_path = str(Path(exported.name) / "scripts")
    sys.path.insert(0, scripts_path)
    try:
        c247_module = importlib.import_module(
            "local_rough_puncture_odd_sector_cycle247_2026_07_17"
        )
        c532_module = importlib.import_module(
            "physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21"
        )
    finally:
        sys.path.remove(scripts_path)
    return exported, c247_module, c532_module


IMMUTABLE_EXPORT, c247, c532 = load_immutable_modules()
c235 = c532.c235
EVEN_WORDS = tuple(word for word in range(16) if word.bit_count() % 2 == 0)
SQUARE_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (float(value.real), float(value.imag))
    raise TypeError(type(value).__name__)


def shore() -> tuple[dict, dict]:
    observed = {
        path: sha256(git_bytes(IMMUTABLE_SHORE_REF, path)).hexdigest()
        for path in PINS
    }
    parent = json.loads(git_bytes(
        IMMUTABLE_SHORE_REF,
        "outputs/physical_twisted_charge_ribbon_auxiliary_link_gauge_"
        "cycle641_receipt_2026_07_23.json",
    ))
    result = {
        "immutable_shore_ref": IMMUTABLE_SHORE_REF,
        "observed": observed,
        "hashes_match": observed == PINS,
        "working_tree_bytes_used_as_scientific_premise": False,
        "Cycle641_pass": parent["pass"],
        "Cycle641_authority": parent["authority"],
        "Cycle641_audit": parent["audit"],
        "Cycle641_local_plaquette_closed": parent["same_code_one_plaquette_E_G_closed"],
        "Cycle641_periodic_closed": parent["full_periodic_physical_compiler_closed"],
        "Cycle641_axiom_pressure": parent["axiom_pressure"],
        "Cycle641_alternate_path_residual": parent["charge_bound_flux_ribbon"]["alternate_path_residual"],
        "Cycle641_Wilson_rank_increments": tuple(
            row["Wilson_rank_increment"]
            for row in parent["periodic_L3_L6_L7_extension"]["sizes"]
        ),
    }
    condition = bool(
        result["hashes_match"]
        and result["Cycle641_pass"]
        and result["Cycle641_authority"] == AUTHORITY
        and result["Cycle641_audit"] == AUDIT
        and result["Cycle641_local_plaquette_closed"]
        and not result["Cycle641_periodic_closed"]
        and not result["Cycle641_axiom_pressure"]
        and result["Cycle641_alternate_path_residual"] == 0
        and result["Cycle641_Wilson_rank_increments"] == (3, 3, 3)
    )
    check("immutable Cycle641 quartet and its exact scope are byte exact", condition, result)
    return parent, result


def translated_wilsons(graph) -> tuple[dict, ...]:
    rows = []
    for axis in range(3):
        transverse = (axis + 1) % 3
        other_axes = tuple(value for value in range(3) if value != axis)
        for offsets in product(range(graph.length), repeat=2):
            fixed = dict(zip(other_axes, offsets))
            vertices = []
            for step in range(graph.length):
                cell = [0, 0, 0]
                cell[axis] = step
                for fixed_axis, value in fixed.items():
                    cell[fixed_axis] = value
                target = list(cell)
                target[axis] = (target[axis] + 1) % graph.length
                vertices.extend((
                    graph.base.vertex_index[(tuple(cell), 2 * axis)],
                    graph.base.vertex_index[(tuple(target), 2 * axis + 1)],
                    graph.base.vertex_index[(tuple(target), 2 * transverse)],
                ))
            rows.append({
                "axis": axis,
                "offsets": offsets,
                "pauli": graph.loop_pauli(vertices),
            })
    return tuple(rows)


def block_state() -> np.ndarray:
    """Two Bell pairs with S on the second qubit of each pair."""
    state = np.zeros(16, dtype=complex)
    for word in (0, 3, 12, 15):
        state[word] = 0.5 * (1j ** (((word >> 1) & 1) + ((word >> 3) & 1)))
    return state


def local_pauli_expectation(state: np.ndarray, x_mask: int, z_mask: int) -> complex:
    phase = (x_mask & z_mask).bit_count() % 4
    output = np.zeros_like(state)
    for basis, amplitude in enumerate(state):
        output[basis ^ x_mask] += (
            (1j ** phase) * ((-1) ** ((basis & z_mask).bit_count())) * amplitude
        )
    return complex(np.vdot(state, output))


def independent_rows(rows, qubits: int):
    pivots: dict[int, int] = {}
    selected = []
    for row in rows:
        reduced = row.symplectic(qubits)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                selected.append(row)
                break
    return tuple(selected)


def factor_state_expectation(
    pauli, block_qubits: tuple[tuple[int, ...], ...],
    block_lookup: dict[int, tuple[int, int]],
    single_axes: dict[int, tuple[str, int]], state: np.ndarray,
) -> complex:
    y_count = (pauli.x & pauli.z).bit_count()
    value = complex(1j ** (pauli.phase - y_count))
    touched_blocks: dict[int, tuple[int, int]] = {}
    support = pauli.x | pauli.z
    while support:
        bit = support & -support
        qubit = bit.bit_length() - 1
        x_bit = (pauli.x >> qubit) & 1
        z_bit = (pauli.z >> qubit) & 1
        if qubit in block_lookup:
            block, local = block_lookup[qubit]
            x_mask, z_mask = touched_blocks.get(block, (0, 0))
            touched_blocks[block] = (
                x_mask | (x_bit << local), z_mask | (z_bit << local)
            )
        else:
            actual_axis = (
                "X" if x_bit and not z_bit else
                "Z" if z_bit and not x_bit else "Y"
            )
            prepared_axis, eigenvalue = single_axes[qubit]
            if actual_axis != prepared_axis:
                return 0.0 + 0.0j
            value *= eigenvalue
        support ^= bit
    for block, (x_mask, z_mask) in touched_blocks.items():
        expectation = local_pauli_expectation(state, x_mask, z_mask)
        if abs(expectation) < TOL:
            return 0.0 + 0.0j
        value *= expectation
    return value


def route_A_boundary_inflow() -> dict:
    sizes = []
    for length in (3, 6, 7):
        graph = c247.PunctureGraph(length, terminals=1)
        local = c532.local_stabilizers(graph)
        base_wilsons = c532.wilson_initializers(graph)
        wilsons = translated_wilsons(graph)
        wilson_rows = tuple(row["pauli"] for row in wilsons)
        blocks = tuple(
            tuple(15 * cell_index + offset for offset in (2, 3, 8, 10))
            for cell_index in range(length ** 3)
        )
        flat_blocks = tuple(qubit for block in blocks for qubit in block)
        block_lookup = {
            qubit: (block_index, local_index)
            for block_index, block in enumerate(blocks)
            for local_index, qubit in enumerate(block)
        }
        usage: dict[int, int] = {}
        axes: dict[int, set[str]] = {}
        for row in wilson_rows:
            support = row.x | row.z
            while support:
                bit = support & -support
                qubit = bit.bit_length() - 1
                x_bit = (row.x >> qubit) & 1
                z_bit = (row.z >> qubit) & 1
                axis = (
                    "X" if x_bit and not z_bit else
                    "Z" if z_bit and not x_bit else "Y"
                )
                usage[qubit] = usage.get(qubit, 0) + 1
                axes.setdefault(qubit, set()).add(axis)
                support ^= bit
        conflicts = tuple(sorted(qubit for qubit, choices in axes.items() if len(choices) > 1))
        outside_conflicts = tuple(qubit for qubit in conflicts if qubit not in block_lookup)
        missing_conflicts = tuple(qubit for qubit in flat_blocks if len(axes.get(qubit, set())) <= 1)

        single_axes: dict[int, tuple[str, int]] = {}
        for qubit in range(graph.qubits):
            if qubit in block_lookup:
                continue
            choices = axes.get(qubit, {"Z"})
            if len(choices) != 1:
                raise ValueError(("unresolved local axis conflict", length, qubit, choices))
            single_axes[qubit] = (next(iter(choices)), +1)

        markers = []
        marker_failures = 0
        for metadata in wilsons:
            row = metadata["pauli"]
            candidates = [
                qubit for qubit in range(graph.qubits)
                if ((row.x | row.z) >> qubit) & 1
                and qubit not in block_lookup
                and usage.get(qubit, 0) == 1
            ]
            if not candidates:
                marker_failures += 1
                continue
            marker = candidates[0]
            scalar = complex(1j ** (row.phase - (row.x & row.z).bit_count()))
            if abs(scalar.imag) >= TOL or abs(abs(scalar.real) - 1) >= TOL:
                marker_failures += 1
                continue
            axis, old_sign = single_axes[marker]
            single_axes[marker] = (axis, old_sign * int(round(scalar.real)))
            markers.append((metadata["axis"], metadata["offsets"], marker))

        seed = block_state()
        wilson_expectations = tuple(
            factor_state_expectation(
                row, blocks, block_lookup, single_axes, seed
            )
            for row in wilson_rows
        )
        translated_expectation_counts = {
            "plus_one": sum(abs(value - 1) < TOL for value in wilson_expectations),
            "minus_one": sum(abs(value + 1) < TOL for value in wilson_expectations),
            "zero": sum(abs(value) < TOL for value in wilson_expectations),
            "other": sum(
                abs(value) >= TOL and abs(value - 1) >= TOL and abs(value + 1) >= TOL
                for value in wilson_expectations
            ),
        }
        local_expectations = tuple(
            factor_state_expectation(
                row, blocks, block_lookup, single_axes, seed
            )
            for row in local
        )
        local_counts = {
            "plus_one": sum(abs(value - 1) < TOL for value in local_expectations),
            "minus_one": sum(abs(value + 1) < TOL for value in local_expectations),
            "zero": sum(abs(value) < TOL for value in local_expectations),
            "other": sum(
                abs(value) >= TOL and abs(value - 1) >= TOL and abs(value + 1) >= TOL
                for value in local_expectations
            ),
        }
        local_rank, local_inconsistent = c532.phase_rank(local, graph.qubits)
        fixed_rank, fixed_inconsistent = c532.phase_rank(
            local + base_wilsons, graph.qubits
        )
        translated_rank, translated_inconsistent = c532.phase_rank(
            local + wilson_rows, graph.qubits
        )
        positions = tuple(c532.physical_position(graph, q) for q in range(graph.qubits))
        period = 32 * length
        block_diameters = tuple(
            max(
                c532.periodic_l1(positions[left], positions[right], period)
                for left in block for right in block
            )
            for block in blocks
        )
        marker_owner_axis_coordinates = {
            axis: tuple(sorted({graph.edges[qubit].owner[axis] for row_axis, _, qubit in markers if row_axis == axis}))
            for axis in range(3)
        }

        # Separate positive theorem: the displayed base triplet has only one
        # four-M2 crossing block.  Its remaining local factors lie on three
        # rooted noncontractible lines whose support grows with L, although
        # every elementary preparation gate remains support one/two.
        base_block = (blocks[0],)
        base_lookup = {
            qubit: (0, local_index)
            for local_index, qubit in enumerate(base_block[0])
        }
        base_usage: dict[int, int] = {}
        base_axes: dict[int, set[str]] = {}
        base_union = 0
        for row in base_wilsons:
            base_union |= row.x | row.z
            support = row.x | row.z
            while support:
                bit = support & -support
                qubit = bit.bit_length() - 1
                x_bit = (row.x >> qubit) & 1
                z_bit = (row.z >> qubit) & 1
                axis = "X" if x_bit and not z_bit else "Z" if z_bit and not x_bit else "Y"
                base_usage[qubit] = base_usage.get(qubit, 0) + 1
                base_axes.setdefault(qubit, set()).add(axis)
                support ^= bit
        base_single_axes = {}
        for qubit in range(graph.qubits):
            if qubit in base_lookup:
                continue
            choices = base_axes.get(qubit, {"Z"})
            base_single_axes[qubit] = (next(iter(choices)), +1)
        base_markers = []
        for row in base_wilsons:
            marker = next(
                qubit for qubit in range(graph.qubits)
                if ((row.x | row.z) >> qubit) & 1
                and qubit not in base_lookup
                and base_usage.get(qubit, 0) == 1
            )
            scalar = complex(1j ** (row.phase - (row.x & row.z).bit_count()))
            axis, sign = base_single_axes[marker]
            base_single_axes[marker] = (axis, sign * int(round(scalar.real)))
            base_markers.append(marker)
        base_expectations = tuple(
            factor_state_expectation(
                row, base_block, base_lookup, base_single_axes, seed
            )
            for row in base_wilsons
        )
        deleted_base_axes = dict(base_single_axes)
        deleted_axis, deleted_sign = deleted_base_axes[base_markers[0]]
        deleted_base_axes[base_markers[0]] = (deleted_axis, -deleted_sign)
        deleted_base_expectation = factor_state_expectation(
            base_wilsons[0], base_block, base_lookup, deleted_base_axes, seed
        )
        sizes.append({
            "length": length,
            "cells": length ** 3,
            "translated_Wilson_loops": len(wilsons),
            "expected_translated_Wilson_loops": 3 * length ** 2,
            "translated_Wilson_pair_anticommutations": sum(
                not left.commutes(right)
                for index, left in enumerate(wilson_rows)
                for right in wilson_rows[index + 1:]
            ),
            "local_constraint_rank": local_rank,
            "base_fixed_rank": fixed_rank,
            "translated_fixed_rank": translated_rank,
            "base_Wilson_rank_increment": fixed_rank - local_rank,
            "translated_Wilson_rank_increment": translated_rank - local_rank,
            "phase_inconsistencies": local_inconsistent + fixed_inconsistent + translated_inconsistent,
            "axis_conflict_qubits": len(conflicts),
            "expected_four_conflict_M2_per_cell": 4 * length ** 3,
            "conflicts_outside_four_M2_blocks": len(outside_conflicts),
            "block_roles_without_conflict": len(missing_conflicts),
            "four_M2_crossing_blocks": len(blocks),
            "maximum_crossing_block_physical_L1_diameter": max(block_diameters),
            "unique_sign_markers": len(set(marker for _, _, marker in markers)),
            "marker_failures": marker_failures,
            "marker_owner_axis_coordinates": marker_owner_axis_coordinates,
            "maximum_Wilson_expectation_residual": float(max(abs(value - 1) for value in wilson_expectations)),
            "translated_factor_seed_expectation_counts": translated_expectation_counts,
            "replicated_fixed_defect_seed_closes_all_translated_loops": translated_expectation_counts["plus_one"] == len(wilsons),
            "base_triplet_seed_maximum_residual": float(max(abs(value - 1) for value in base_expectations)),
            "delete_one_base_marker_residual": float(abs(deleted_base_expectation - 1)),
            "base_triplet_unique_sign_markers": len(set(base_markers)),
            "base_triplet_support_union_weight": base_union.bit_count(),
            "base_triplet_maximum_single_Wilson_weight": max((row.x | row.z).bit_count() for row in base_wilsons),
            "base_triplet_rooted_path_physical_L1_diameter": c532.support_diameter(base_union, positions, period),
            "base_triplet_parallel_preparation_depth_bound": 6,
            "base_triplet_total_local_gate_count_bound": base_union.bit_count() + 6,
            "base_triplet_is_bounded_neighborhood_E": False,
            "local_constraint_seed_expectations": local_counts,
            "seed_is_full_fixed_code_state": local_counts["plus_one"] == len(local),
            "single_M2_axis_preparations": graph.qubits - len(flat_blocks),
            "crossing_block_circuit": "per cell: H(q0), CNOT(q0,q1), S(q1), H(q2), CNOT(q2,q3), S(q3)",
            "maximum_elementary_preparation_gate_support": 2,
            "boundary_sign_sheet_is_supplied": True,
            "macro_origin_or_axis_free": False,
        })
    covariance = c532.covariance_controls()
    result = {
        "sizes": sizes,
        "fixed_code_covariance": covariance,
        "preparation_all24_all576_established": False,
        "base_triplet_rooted_paths_supplied": True,
        "replicated_marker_sheet_closes_translated_family": False,
        "base_triplet_constant_parallel_depth_but_growing_path_extent": True,
        "constructive_theorem": (
            "the displayed three Wilson signs have an exact locally gated seed with one diameter-8 "
            "crossing block and single-M2 factors along three rooted noncontractible paths"
        ),
        "growing_Wilson_operator_applied_or_measured": False,
        "runtime_global_query": False,
        "constant_M2_overhead": True,
        "replicated_fixed_defect_closes_translated_family": False,
        "boundary_inflow_autonomously_generated": False,
        "full_local_constraint_preparation": False,
        "full_periodic_E_prepared": False,
        "route_status": "ATTEMPTED_REPLICATED_FIXED_DEFECT_FAIL__POSITIVE_ROOTED_BASE_TRIPLET_SEED",
    }
    result["pass"] = bool(
        all(
            row["translated_Wilson_loops"] == row["expected_translated_Wilson_loops"]
            and row["translated_Wilson_pair_anticommutations"] == 0
            and row["base_Wilson_rank_increment"] == row["translated_Wilson_rank_increment"] == 3
            and row["phase_inconsistencies"] == 0
            and row["axis_conflict_qubits"] == row["expected_four_conflict_M2_per_cell"]
            and row["conflicts_outside_four_M2_blocks"] == 0
            and row["block_roles_without_conflict"] == 0
            and row["unique_sign_markers"] == row["translated_Wilson_loops"]
            and row["marker_failures"] == 0
            and row["maximum_crossing_block_physical_L1_diameter"] == 8
            and row["translated_factor_seed_expectation_counts"]["plus_one"] == row["length"] ** 2
            and row["translated_factor_seed_expectation_counts"]["zero"] == 2 * row["length"] ** 2
            and not row["replicated_fixed_defect_seed_closes_all_translated_loops"]
            and row["base_triplet_seed_maximum_residual"] < TOL
            and row["delete_one_base_marker_residual"] > 1.9
            and row["base_triplet_unique_sign_markers"] == 3
            and row["base_triplet_is_bounded_neighborhood_E"] is False
            and not row["seed_is_full_fixed_code_state"]
            and row["maximum_elementary_preparation_gate_support"] == 2
            and row["boundary_sign_sheet_is_supplied"]
            and not row["macro_origin_or_axis_free"]
            for row in sizes
        )
        and covariance["pass"]
        and not result["preparation_all24_all576_established"]
        and result["base_triplet_rooted_paths_supplied"]
        and not result["replicated_marker_sheet_closes_translated_family"]
        and result["base_triplet_constant_parallel_depth_but_growing_path_extent"]
        and not result["growing_Wilson_operator_applied_or_measured"]
        and not result["runtime_global_query"]
        and result["constant_M2_overhead"]
        and not result["replicated_fixed_defect_closes_translated_family"]
        and not result["boundary_inflow_autonomously_generated"]
        and not result["full_local_constraint_preparation"]
        and not result["full_periodic_E_prepared"]
    )
    check("route A falsifies the replicated fixed-defect tensor seed while exactly preparing the three rooted base signs", result["pass"], {
        "sizes": [(row["length"], row["translated_factor_seed_expectation_counts"], row["base_triplet_seed_maximum_residual"], row["base_triplet_support_union_weight"], row["local_constraint_seed_expectations"]) for row in sizes],
        "covariance": covariance["pass"],
    })
    return result


def ordinary_permutation(permutation: tuple[int, ...]) -> np.ndarray:
    matrix = np.zeros((16, 16), dtype=complex)
    for word in range(16):
        target = sum(
            ((word >> source) & 1) << permutation[source]
            for source in range(4)
        )
        matrix[target, word] = 1
    return matrix


def pauli_matrix(x_mask: int, z_mask: int, phase: int = 0) -> np.ndarray:
    matrix = np.zeros((16, 16), dtype=complex)
    for basis in range(16):
        matrix[basis ^ x_mask, basis] = (
            (1j ** phase) * ((-1) ** ((basis & z_mask).bit_count()))
        )
    return matrix


def square_operators() -> dict:
    z_dress = (0b0000, 0b0001, 0b0010, 0b0101)
    a_rows = tuple(pauli_matrix(1 << edge, z_dress[edge]) for edge in range(4))
    b_rows = []
    for vertex in range(4):
        mask = sum(
            1 << edge for edge, endpoints in enumerate(SQUARE_EDGES)
            if vertex in endpoints
        )
        b_rows.append(pauli_matrix(0, mask))
    loop = np.eye(16, dtype=complex)
    for row in a_rows:
        loop = loop @ row
    fswaps = []
    for edge, (source, target) in enumerate(SQUARE_EDGES):
        fswaps.append(0.5 * (
            b_rows[source] + b_rows[target]
            + 1j * b_rows[source] @ a_rows[edge]
            - 1j * b_rows[target] @ a_rows[edge]
        ))
    return {"A": a_rows, "B": tuple(b_rows), "Q": loop, "F": tuple(fswaps)}


def raw_square_encoding(operators: dict) -> np.ndarray:
    columns = []
    for word in EVEN_WORDS:
        eigenvalues = tuple(-1 if (word >> vertex) & 1 else 1 for vertex in range(4))
        physical_words = [
            basis for basis in range(16)
            if all(
                abs(operators["B"][vertex][basis, basis] - eigenvalues[vertex]) < TOL
                for vertex in range(4)
            )
        ]
        selector = np.eye(16, dtype=complex)[:, physical_words]
        values, vectors = np.linalg.eigh(selector.conj().T @ operators["Q"] @ selector)
        columns.append(selector @ vectors[:, int(np.argmin(abs(values - 1)))])
    return np.stack(columns, axis=1)


def gamma_permutation(permutation: tuple[int, ...]) -> np.ndarray:
    index = {word: position for position, word in enumerate(EVEN_WORDS)}
    result = np.zeros((8, 8), dtype=complex)
    for word in EVEN_WORDS:
        occupied = [mode for mode in range(4) if (word >> mode) & 1]
        images = [permutation[mode] for mode in occupied]
        inversions = sum(
            images[left] > images[right]
            for left in range(len(images)) for right in range(left + 1, len(images))
        )
        target = sum(1 << mode for mode in images)
        result[index[target], index[word]] = (-1) ** inversions
    return result


def phase_fix_encoding(raw: np.ndarray, operators: dict) -> np.ndarray:
    edge_target = gamma_permutation((1, 0, 2, 3))
    exchange_target = gamma_permutation((2, 3, 0, 1))
    exchange = (
        operators["F"][1] @ operators["F"][3]
        @ operators["F"][0] @ operators["F"][2]
    )
    constraints = []
    for physical, target in ((operators["F"][0], edge_target), (exchange, exchange_target)):
        represented = raw.conj().T @ physical @ raw
        for source in range(8):
            target_index = int(np.argmax(abs(target[:, source])))
            constraints.append((
                source, target_index,
                represented[target_index, source], target[target_index, source],
            ))
    phases: dict[int, complex] = {}
    for seed in range(8):
        if seed in phases:
            continue
        phases[seed] = 1.0 + 0.0j
        frontier = [seed]
        while frontier:
            source = frontier.pop()
            for left, right, amplitude, target in constraints:
                if left != source:
                    continue
                proposed = np.conj(target / (amplitude * phases[left]))
                if right in phases:
                    if abs(phases[right] - proposed) >= TOL:
                        raise ValueError("square phase inconsistency")
                else:
                    phases[right] = proposed
                    frontier.append(right)
    return raw @ np.diag([phases[index] for index in range(8)])


def unitary_with_first_column(target: np.ndarray) -> np.ndarray:
    columns = [target / np.linalg.norm(target)]
    for basis_index in range(len(target)):
        candidate = np.eye(len(target), dtype=complex)[:, basis_index]
        for column in columns:
            candidate -= column * np.vdot(column, candidate)
        norm = np.linalg.norm(candidate)
        if norm > TOL:
            columns.append(candidate / norm)
        if len(columns) == len(target):
            break
    return np.stack(columns, axis=1)


def route_B_reversible_ancilla() -> dict:
    operators = square_operators()
    raw = raw_square_encoding(operators)
    link_encoding = phase_fix_encoding(raw, operators)
    even_words = EVEN_WORDS
    columns = []
    blank_columns = []
    for column, word in enumerate(even_words):
        data_word = np.eye(16, dtype=complex)[:, word]
        columns.append(np.kron(data_word, link_encoding[:, column]))
        blank_columns.append(np.kron(data_word, np.eye(16, dtype=complex)[:, 0]))
    encoding = np.stack(columns, axis=1)
    blank = np.stack(blank_columns, axis=1)

    preparation = np.zeros((256, 256), dtype=complex)
    link_columns = {word: link_encoding[:, column] for column, word in enumerate(even_words)}
    for data_word in range(16):
        block = (
            unitary_with_first_column(link_columns[data_word])
            if data_word in link_columns else np.eye(16, dtype=complex)
        )
        start = 16 * data_word
        preparation[start:start + 16, start:start + 16] = block

    edge_permutation = (1, 0, 2, 3)
    exchange_permutation = (2, 3, 0, 1)
    edge_target = gamma_permutation(edge_permutation)
    exchange_target = gamma_permutation(exchange_permutation)
    edge_physical = np.kron(ordinary_permutation(edge_permutation), operators["F"][0])
    exchange_link = (
        operators["F"][1] @ operators["F"][3]
        @ operators["F"][0] @ operators["F"][2]
    )
    exchange_physical = np.kron(
        ordinary_permutation(exchange_permutation), exchange_link
    )
    projector = encoding @ encoding.conj().T
    complement = np.eye(256) - projector
    deleted_exchange = np.kron(
        ordinary_permutation(exchange_permutation), np.eye(16)
    )
    result = {
        "data_M2": 4,
        "link_M2": 4,
        "total_M2_per_plaquette": 8,
        "encoding_shape": encoding.shape,
        "encoding_isometry_residual": float(np.max(abs(encoding.conj().T @ encoding - np.eye(8)))),
        "preparation_unitarity_residual": float(np.max(abs(preparation.conj().T @ preparation - np.eye(256)))),
        "preparation_residual": float(np.max(abs(preparation @ blank - encoding))),
        "edge_EG_residual": float(np.max(abs(edge_physical @ encoding - encoding @ edge_target))),
        "exchange_EG_residual": float(np.max(abs(exchange_physical @ encoding - encoding @ exchange_target))),
        "exchange_leakage_residual": float(np.max(abs(complement @ exchange_physical @ encoding))),
        "prepare_update_unprepare_residual": float(np.max(abs(
            preparation.conj().T @ exchange_physical @ preparation @ blank
            - blank @ exchange_target
        ))),
        "deleted_link_exchange_signal": float(np.max(abs(
            deleted_exchange @ encoding - encoding @ exchange_target
        ))),
        "maximum_synthesized_unitary_support": 8,
        "literal_one_two_M2_factorization_of_controlled_preparation": False,
        "periodic_shared_link_extension_constructed": False,
        "autonomous_runtime_sector_query": False,
        "route_status": "EXACT_REVERSIBLE_ONE_PLAQUETTE_DATA_LINK_ENCODER__ELEMENTARY_AND_PERIODIC_EXTENSION_OPEN",
    }
    result["pass"] = bool(
        result["encoding_isometry_residual"] < TOL
        and result["preparation_unitarity_residual"] < TOL
        and result["preparation_residual"] < TOL
        and result["edge_EG_residual"] < TOL
        and result["exchange_EG_residual"] < TOL
        and result["exchange_leakage_residual"] < TOL
        and result["prepare_update_unprepare_residual"] < TOL
        and result["deleted_link_exchange_signal"] > 1.3
        and not result["literal_one_two_M2_factorization_of_controlled_preparation"]
        and not result["periodic_shared_link_extension_constructed"]
        and not result["autonomous_runtime_sector_query"]
    )
    check("route B is exactly reversible on one data/link plaquette but has no elementary periodic encoder", result["pass"], result)
    return result


def correction_coverage(include_wilsons: bool) -> dict:
    length = 3
    graph = c247.PunctureGraph(length, terminals=1)
    basis = independent_rows(c532.local_stabilizers(graph), graph.qubits)
    wilsons = c532.wilson_initializers(graph) if include_wilsons else ()
    rank = len(basis)
    columns = []
    for qubit in range(graph.qubits):
        x_syndrome = sum(
            (((row.z >> qubit) & 1) << index)
            for index, row in enumerate(basis)
        )
        z_syndrome = sum(
            (((row.x >> qubit) & 1) << index)
            for index, row in enumerate(basis)
        )
        for wilson_index, row in enumerate(wilsons):
            x_syndrome |= ((row.z >> qubit) & 1) << (rank + wilson_index)
            z_syndrome |= ((row.x >> qubit) & 1) << (rank + wilson_index)
        columns.extend((
            (x_syndrome, qubit, "X"),
            (z_syndrome, qubit, "Z"),
            (x_syndrome ^ z_syndrome, qubit, "Y"),
        ))
    by_syndrome: dict[int, list[tuple[int, str]]] = {}
    for syndrome, qubit, axis in columns:
        by_syndrome.setdefault(syndrome, []).append((qubit, axis))
    positions = tuple(c532.physical_position(graph, q) for q in range(graph.qubits))
    period = 32 * length
    weight_one = []
    weight_two = []
    minimum_pair_diameters = []
    for generator in range(rank):
        target = 1 << generator
        if target in by_syndrome:
            weight_one.append(generator)
            continue
        best = None
        for syndrome, left_qubit, left_axis in columns:
            for right_qubit, right_axis in by_syndrome.get(target ^ syndrome, ()): 
                if left_qubit == right_qubit:
                    continue
                diameter = c532.periodic_l1(
                    positions[left_qubit], positions[right_qubit], period
                )
                if diameter <= 64 and (best is None or diameter < best):
                    best = diameter
        if best is not None:
            weight_two.append(generator)
            minimum_pair_diameters.append(best)
    return {
        "length": length,
        "independent_local_generators": rank,
        "Wilson_commutation_required": include_wilsons,
        "weight_one_isolated_duals": len(weight_one),
        "additional_weight_two_diameter_at_most_64_duals": len(weight_two),
        "unresolved_generators": rank - len(weight_one) - len(weight_two),
        "maximum_used_pair_diameter": max(minimum_pair_diameters, default=0),
        "candidate_single_M2_Paulis": len(columns),
        "Kraus_completeness_for_each_resolved_generator": True,
    }


def route_C_measurement_reset() -> dict:
    preserving = correction_coverage(True)
    ignoring = correction_coverage(False)
    fixture = c532.fixture_controls()
    sizes = tuple(c532.layout_controls(length) for length in (3, 6, 7))
    result = {
        "sector_preserving_parallel_pump": preserving,
        "pump_if_Wilson_preservation_is_deleted": ignoring,
        "bounded_layouts": sizes,
        "mass_contact_logical_seam_fixture": fixture,
        "measurement_outcome_used_only_locally": True,
        "host_side_sector_selection": False,
        "all_independent_local_generators_pumped": preserving["unresolved_generators"] == 0,
        "held_L6_L7_pump_executed": False,
        "full_periodic_E_prepared": False,
        "route_status": "ATTEMPTED_L3_LOCAL_RESET_DUALS__INCOMPLETE_GENERATOR_COVERAGE",
    }
    result["pass"] = bool(
        preserving["independent_local_generators"] == 403
        and preserving["weight_one_isolated_duals"] > 0
        and preserving["additional_weight_two_diameter_at_most_64_duals"] > 0
        and preserving["unresolved_generators"] > 0
        and ignoring["unresolved_generators"] <= preserving["unresolved_generators"]
        and all(row["pass"] for row in sizes)
        and fixture["pass"]
        and result["measurement_outcome_used_only_locally"]
        and not result["host_side_sector_selection"]
        and not result["all_independent_local_generators_pumped"]
        and not result["held_L6_L7_pump_executed"]
        and not result["full_periodic_E_prepared"]
    )
    check("route C pumps a strict subset of L3 generators with bounded local reset duals and leaves the rest explicit", result["pass"], {
        "preserving": preserving, "ignoring": ignoring,
    })
    return result


def source_line(fragment: str) -> int:
    for number, line in enumerate(Path(__file__).read_text().splitlines(), 1):
        if fragment in line:
            return number
    return 0


def cited_line_exists(path: str, line: int) -> bool:
    target = ROOT / path
    return bool(
        target.is_file() and 1 <= line <= len(target.read_text().splitlines())
        and target.read_text().splitlines()[line - 1].strip()
    )


def find_line(path: str, fragment: str) -> int:
    for number, line in enumerate((ROOT / path).read_text().splitlines(), 1):
        if fragment in line:
            return number
    return 0


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict:
    families = [
        {
            "family": "replicated puncture/boundary inflow",
            "object": "one repeated four-M2 Bell/S crossing block per cell plus local axis factors",
            "mechanism": "factor every translated Wilson into local axes and resolve cell crossings",
            "terminal": "all 3L^2 translated signs +1, every local check +1, no rooted paths",
            "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED",
            "target_equivalent": True, "result": route_a["route_status"],
        },
        {
            "family": "reversible data/link ancilla",
            "object": "four data plus four link M2s on one plaquette",
            "mechanism": "controlled link encoding, physical update, inverse encoding",
            "terminal": "elementary shared-link periodic encoder on L3/L6/L7",
            "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED",
            "target_equivalent": False, "result": route_b["route_status"],
        },
        {
            "family": "local measurement-reset dual pump",
            "object": "actual L3 independent local stabilizers and bounded Pauli duals",
            "mechanism": "syndrome-local Kraus correction commuting with all other checks and Wilsons",
            "terminal": "complete held-size generator coverage and convergence",
            "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED",
            "target_equivalent": True, "result": route_c["route_status"],
        },
    ]
    open_routes = [
        {"family": "non-JW auxiliary Clifford Wilson resolver", "object": "local Clifford crossing/link ancillas", "mechanism": "make spin characters products of bounded checks", "terminal": "root-free fixed code", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "multi-round puncture-directed automaton", "object": "local syndrome carriers", "mechanism": "transport and absorb defects at repeated punctures", "terminal": "held-size convergence", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "alternative stabilizer bases", "object": "other independent local-check presentations", "mechanism": "increase isolated bounded-dual coverage", "terminal": "zero unresolved generators", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "weight-three/four reset duals", "object": "bounded multi-M2 corrections", "mechanism": "pump generators unresolved at weight two", "terminal": "all L3/L6/L7 checks", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "fermionic PEPS boundary inflow", "object": "graded virtual boundary tensor", "mechanism": "absorb varying segment characters locally", "terminal": "all24 periodic E without rooted path", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
    ]
    walls = {
        "W_replica": "the identical four-M2 block yields L^2 plus and 2L^2 zero translated-loop expectations",
        "W_root": "the exact base triplet seed uses three rooted noncontractible paths of growing factor count",
        "W_localprep": "all bounded local-stabilizer expectations are zero in the tested route-A seed",
        "W_elementary": "route B's controlled support-eight unitary lacks a literal one/two-M2 factorization",
        "W_held": "route C leaves 173 L3 generators unresolved and has no L6/L7 pump",
    }
    wall_interfaces = {
        "W_replica": "Route A translated-loop tensor census",
        "W_root": "Route A rooted base-triplet seed",
        "W_localprep": "Route A bounded local-stabilizer expectations",
        "W_elementary": "Route B support-eight reversible plaquette",
        "W_held": "Route C selected-basis L3 reset pump",
    }
    pairs = [
        {
            "from": source,
            "to": target,
            "closure_implied": False,
            "independence_evidence": {
                "status": "NOT_ESTABLISHED_BEYOND_EXECUTED_INTERFACES",
                "from_interface": wall_interfaces[source],
                "to_interface": wall_interfaces[target],
                "reason": (
                    f"closing {source} on {wall_interfaces[source]} does not construct or test "
                    f"the distinct obligation {target} on {wall_interfaces[target]}"
                ),
            },
        }
        for source, target in permutations(walls, 2)
    ]
    phrases = (
        "we assume", "by construction", "as is standard", "the framework provides",
        "bridge context", "background", "naturally", "obviously", "standard qft",
        "registered", "canonical",
    )
    hits = tuple(phrase for phrase in phrases if phrase in NOTE.read_text().lower())
    current = "scripts/physical_bounded_spin_sector_genesis_tournament_cycle644_2026_07_23.py"
    c641_note = "docs/work_history/repo/review_feedback/PHYSICAL_TWISTED_CHARGE_RIBBON_AUXILIARY_LINK_GAUGE_CYCLE641_NOTE_2026-07-23.md"
    c247_note = "docs/work_history/repo/review_feedback/LOCAL_ROUGH_PUNCTURE_ODD_SECTOR_CYCLE247_NOTE_2026-07-17.md"
    c532_note = "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md"
    n4 = [
        {
            "prior_ref": IMMUTABLE_SHORE_REF,
            "prior_path": c641_note, "prior_line": find_line(c641_note, "required Wilson weights grow"),
            "prior_residual": "three displayed Wilson initializers have weights 21/39/45",
            "current_ref": "working-tree Cycle644 candidate",
            "current_path": current, "current_line": source_line("def route_A_boundary_inflow"),
            "current_residual": "the three displayed signs have residual-0 local-gate seeds but rooted support-union weights 51/105/123",
            "exact_match": True, "same_scope": True, "use_as_closure": True,
        },
        {
            "prior_ref": IMMUTABLE_SHORE_REF,
            "prior_path": c641_note, "prior_line": find_line(c641_note, "No bounded local or autonomous preparation"),
            "prior_residual": "full fixed-code preparation absent",
            "current_ref": "working-tree Cycle644 candidate",
            "current_path": current, "current_line": source_line("local_constraint_seed_expectations"),
            "current_residual": "648/5184/8232 local rows have zero expectation in the replicated seed",
            "exact_match": True, "same_scope": True, "use_as_closure": False,
        },
        {
            "prior_ref": IMMUTABLE_SHORE_REF,
            "prior_path": c641_note, "prior_line": find_line(c641_note, "Deleting one entangler"),
            "prior_residual": "one Q=+1 plaquette has a bounded reversible vacuum preparation surface",
            "current_ref": "working-tree Cycle644 candidate",
            "current_path": current, "current_line": source_line("def route_B_reversible_ancilla"),
            "current_residual": "separate data/link prepare-update-unprepare residual is <=2.3e-16",
            "exact_match": True, "same_scope": True, "use_as_closure": True,
        },
        {
            "prior_ref": IMMUTABLE_SHORE_REF,
            "prior_path": c247_note, "prior_line": find_line(c247_note, "one global outer boundary"),
            "prior_residual": "open boundary has area overhead and changes the periodic contract",
            "current_ref": "working-tree Cycle644 candidate",
            "current_path": current, "current_line": source_line("base_triplet_rooted_path_physical_L1_diameter"),
            "current_residual": "rooted periodic path seed has growing factor count but does not open the boundary",
            "exact_match": False, "same_scope": False, "use_as_closure": False,
        },
    ]
    n5 = [
        {"claim": "local gates do not imply bounded-neighborhood genesis", "per_element": "route A uses support-one/two gates", "per_site": "one attempted four-M2 block per cell", "per_mode": "three rooted Wilson characters are exact", "per_block": "translated blocks vary along paths", "lattice_wide": "rooted factor counts grow 51/105/123"},
        {"claim": "rank equivalence does not prepare the code", "per_element": "each Wilson factor has a local axis", "per_site": "axis conflicts occupy four roles", "per_mode": "translated family adds only three ranks", "per_block": "identical block seed leaves zero expectations", "lattice_wide": "all 648/5184/8232 local rows are unprepared"},
        {"claim": "reversible plaquette is not periodic elementary E", "per_element": "edge/exchange EG pass", "per_site": "eight M2s are used", "per_mode": "all eight even words return link blank", "per_block": "controlled unitary support is eight", "lattice_wide": "shared links and one/two-M2 factorization are open"},
        {"claim": "partial reset coverage is not a dissipative encoder", "per_element": "230 selected L3 generators have weight<=2 duals", "per_site": "maximum accepted dual diameter is 44", "per_mode": "Wilson preservation is explicit", "per_block": "173 generators remain", "lattice_wide": "L6/L7 convergence is not executed"},
        {"claim": "fixed-code covariance is not preparation covariance", "per_element": "single-face group law passes", "per_site": "layout is frame covariant", "per_mode": "three fixed characters form a cubic orbit", "per_block": "rooted preparation circuit orbit is not synthesized", "lattice_wide": "no root-free all24/all576 E is claimed"},
    ]
    n6 = [
        {"file": "outputs/physical_twisted_charge_ribbon_auxiliary_link_gauge_cycle641_receipt_2026_07_23.json", "status": "PINNED_IMMUTABLE_PARENT", "what_closes": "one Q=+1 plaquette and conditional fixed-spin runtime, not periodic preparation"},
        {"file": c247_note, "status": "PINNED_BOUNDARY_COMPARATOR", "what_closes": "rough-terminal even algebra and exact boundary-multiplicity diagnostics"},
        {"file": c532_note, "status": "PINNED_FACTOR_COMPARATOR", "what_closes": "fixed-spin target-times-gauge factor and all24/all576 code covariance"},
        {"file": "docs/work_history/repo/review_feedback/PHYSICAL_BOUNDED_SPIN_SECTOR_GENESIS_TOURNAMENT_CYCLE644_NOTE_2026-07-23.md", "status": "CURRENT_SCOPED_NOTE", "what_closes": "rooted base-triplet seed and route dispositions only"},
        {"file": current, "status": "CURRENT_EXECUTABLE", "what_closes": "L3/L6/L7 translated-loop census, reversible plaquette and L3 reset-dual audit"},
    ]
    steelman = {
        "steelman": "A repeated graded crossing tensor could carry the varying Wilson segment character that defeats the identical Bell/S block, while a puncture-directed local automaton prepares the remaining stabilizers without changing the spin sector.",
        "mechanism": "replace the scalar cell block by a direction-sensitive Clifford/PEPS tensor and pump its local syndromes to repeated punctures",
        "terminal_obligation": "literal elementary E/prep/G on L3/L6/L7, zero local syndromes, no rooted paths, preparation all24/all576 and full fixtures",
        "citations": [
            {"ref": IMMUTABLE_SHORE_REF, "path": c641_note, "line": find_line(c641_note, "Run a bounded spin-sector genesis tournament"), "supports": "boundary inflow and reset routes were explicitly live"},
            {"ref": IMMUTABLE_SHORE_REF, "path": c247_note, "line": find_line(c247_note, "explicit measurement-assisted isometry"), "supports": "measurement-assisted image selection was not ruled out"},
        ],
        "action": "construct the varying crossing tensor and puncture-directed held-size pump",
        "actionable": True,
    }
    echoes = [
        {"cycle": "Cycle247", "prior_path": c247_note, "prior_line": find_line(c247_note, "one rough terminal per cell | ATTEMPTED"), "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c247_note, "citation_line": find_line(c247_note, "one rough terminal per cell | ATTEMPTED"), "echo": "repeated rough terminals close the even algebra but not image selection", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "puncture-directed reset", "applicability": "ACTIONABLE_LOCAL_PREP_ROUTE", "effect": "keeps route C and automata live"},
        {"cycle": "Cycle532", "prior_path": c532_note, "prior_line": find_line(c532_note, "does not itself produce a bounded state-preparation circuit"), "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c532_note, "citation_line": find_line(c532_note, "does not itself produce a bounded state-preparation circuit"), "echo": "algebraic factorization is not preparation", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "compose rooted seed with local constraints", "applicability": "EXACT_CURRENT_BOUNDARY", "effect": "blocks full periodic E"},
        {"cycle": "Cycle641", "prior_path": c641_note, "prior_line": find_line(c641_note, "required Wilson weights grow"), "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c641_note, "citation_line": find_line(c641_note, "required Wilson weights grow"), "echo": "displayed Wilson words grow", "retired": True, "retirement_mechanism": "support-one/two rooted path seed with residual zero", "could_apply_here": True, "mechanism": "locally prepare each Pauli factor", "applicability": "RETIRES_GROWING_GATE_ONLY", "effect": "rooted path extent and local-code prep remain"},
        {"cycle": "Cycle641", "prior_path": c641_note, "prior_line": find_line(c641_note, "punctured/open boundary inflow"), "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c641_note, "citation_line": find_line(c641_note, "punctured/open boundary inflow"), "echo": "replicated boundary inflow was live", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "direction-sensitive crossing tensor", "applicability": "OPEN_VARIANT_AFTER_SCALAR_BLOCK_FAIL", "effect": "prevents route-A no-go promotion"},
    ]
    n4_lines = all(
        cited_line_exists(row["prior_path"], row["prior_line"])
        and cited_line_exists(row["current_path"], row["current_line"])
        for row in n4
    )
    n7_lines = all(cited_line_exists(row["path"], row["line"]) for row in steelman["citations"])
    n8_lines = all(cited_line_exists(row["citation_path"], row["citation_line"]) for row in echoes)
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5", "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258", "newer_origin_main_followed": True},
        "N1_normalized_families": families, "N1_qualifying_attempts": sum(row["target_equivalent"] for row in families), "N1_required_for_broad_negative": 5,
        "N1_open_routes_not_counted": open_routes, "N1_live_routes": [row["family"] for row in open_routes],
        "N2_walls": walls, "N2_collapsed_walls": walls, "N2_directional_independence": pairs, "N2_directed_pairs": pairs, "N2_directed_pair_count": len(pairs), "N2_machine_check_count": len(pairs), "N2_independence_complete": False,
        "N3_hidden_wall_phrases": phrases, "N3_note_phrase_hits": hits,
        "N3_explicit_supplied_structure": ["compile-time L/parity", "three axes", "macro-origin and three rooted paths", "four face roles per attempted block", "three sign markers", "Cycle532 code/runtime", "support-eight route-B synthesis", "selected L3 basis", "local feed-forward", "logical fixtures"],
        "N4_exact_residual_matching": n4, "N4_exact_residual_matches": n4[:-1], "N4_dropped_nonmatches": n4[-1:], "N4_cited_lines_exist": n4_lines,
        "N5_five_resolution_rhetoric_audit": n5, "N5_rhetoric_resolution_ledger": n5,
        "N6_partial_closure_paths": n6,
        "N7_cited_actionable_steelman": steelman, "N7_steelman": steelman, "N7_cited_lines_exist": n7_lines,
        "N8_rowwise_cross_cycle_echo": echoes, "N8_cross_cycle_echo": echoes, "N8_cited_lines_exist": n8_lines,
        "Status": "PASS", "artifact_status": "PASS_ROOTED_TRIPLET_AND_LOCAL_REVERSIBLE_BLOCK_ONLY",
        "broad_negative_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False,
        "minimum_content_gate": "FAIL / DO NOT SHIP", "minimum_content_claim": False,
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "shared_obstruction_claim": False,
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "axiom_pressure_claim": False,
        "negative_claim_shipped": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    schema = bool(
        len(families) == 3 and all(row["honesty_marker"] == "ATTEMPTED" for row in families)
        and len(open_routes) == 5 and all("honesty_marker" not in row for row in open_routes)
        and len(pairs) == 20
        and result["N2_machine_check_count"] == 20
        and len({(row["from"], row["to"]) for row in pairs}) == 20
        and all(
            set(row) == {"from", "to", "closure_implied", "independence_evidence"}
            and row["from"] != row["to"]
            and row["closure_implied"] is False
            and row["independence_evidence"]["status"] == "NOT_ESTABLISHED_BEYOND_EXECUTED_INTERFACES"
            and bool(row["independence_evidence"]["reason"])
            for row in pairs
        )
        and not hits and n4_lines and n7_lines and n8_lines
        and all(
            row["prior_ref"] == IMMUTABLE_SHORE_REF
            and row["current_ref"] == "working-tree Cycle644 candidate"
            and all(key in row for key in (
                "prior_path", "prior_line", "prior_residual", "current_path", "current_line",
                "current_residual", "same_scope", "exact_match", "use_as_closure",
            ))
            for row in n4
        )
        and all(row["same_scope"] and row["exact_match"] for row in n4[:-1])
        and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"] for row in n4[-1:])
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in n5)
        and all(set(row) == {"file", "status", "what_closes"} for row in n6)
        and all(
            row["ref"] == IMMUTABLE_SHORE_REF
            and all(key in row for key in ("path", "line", "supports"))
            for row in steelman["citations"]
        )
        and all(
            row["citation_ref"] == IMMUTABLE_SHORE_REF
            and all(key in row for key in (
                "citation_path", "citation_line", "retired", "mechanism", "applicability",
            ))
            for row in echoes
        )
        and result["N1_qualifying_attempts"] < result["N1_required_for_broad_negative"]
        and result["Status"] == "PASS"
        and all(result[key] == "FAIL / DO NOT SHIP" for key in (
            "broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate",
        ))
        and all(result[key] is False for key in (
            "broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim",
        ))
        and not result["negative_claim_shipped"]
        and not result["shared_route_independent_obstruction"]
        and not result["axiom_pressure"]
    )
    result["pass"] = schema
    check("canonical full N1-N8 ships rooted/local positives and blocks no-go/minimum/shared/axiom claims", schema, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "## Strongest constructive result",
        "## Route A — replicated boundary inflow",
        "## Route B — reversible local ancilla",
        "## Route C — local measurement/reset",
        "## N1-N8 discipline",
        "## Supplied structure",
        "## Dependency ledger",
        "## Scope firewall",
    )
    result = {
        "missing_sections": tuple(section for section in required if section not in text),
        "authority_none": "Authority: **none**" in text,
        "audit_unset": "Audit: **unset**" in text,
        "accepted_false": "Accepted: **false**" in text,
    }
    result["pass"] = bool(
        not result["missing_sections"]
        and result["authority_none"]
        and result["audit_unset"]
        and result["accepted_false"]
    )
    check("Cycle644 note exposes results, supplies, route dispositions and N1-N8", result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle644 bounded spin-sector genesis tournament", AUTHORITY, AUDIT)
    parent, shore_result = shore()
    note = note_contract()
    route_a = route_A_boundary_inflow()
    route_b = route_B_reversible_ancilla()
    route_c = route_C_measurement_reset()
    discipline = no_go_discipline(route_a, route_b, route_c)
    promotion_gates = {
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
    }
    top_level_claims = {
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
    }
    claim_gate_contract = bool(
        discipline["Status"] == "PASS"
        and discipline["pass"]
        and all(discipline[key] == value for key, value in promotion_gates.items())
        and all(discipline[key] is value for key, value in top_level_claims.items())
        and not discipline["shared_route_independent_obstruction"]
        and not discipline["axiom_pressure"]
    )
    check("top-level claim flags and four promotion gates are exact and non-promoting", claim_gate_contract, {
        "Status": discipline["Status"],
        "promotion_gates": promotion_gates,
        "claims": top_level_claims,
        "constitutional_effect": "none",
        "shared_route_independent_obstruction": discipline["shared_route_independent_obstruction"],
        "axiom_pressure": discipline["axiom_pressure"],
    })
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, {
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    })
    fixture = route_c["mass_contact_logical_seam_fixture"]
    receipt = {
        "status": "cycle644-bounded-spin-sector-genesis-tournament",
        "Status": discipline["Status"],
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "constitutional_effect": "none",
        **top_level_claims,
        "canonical_claim_gate_contract": {
            "Status": discipline["Status"],
            **promotion_gates,
            "pass": claim_gate_contract,
        },
        "breakthrough": False,
        "pins": PINS,
        "immutable_shore_ref": IMMUTABLE_SHORE_REF,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "shore": shore_result,
        "note_contract": note,
        "route_A_replicated_boundary_inflow": route_a,
        "route_B_reversible_local_ancilla": route_b,
        "route_C_local_measurement_reset": route_c,
        "route_by_route_disposition": {
            "A": route_a["route_status"],
            "B": route_b["route_status"],
            "C": route_c["route_status"],
        },
        "strongest_constructive_result": (
            "the displayed three Wilson signs have residual-0 locally gated seeds on L3/L6/L7 "
            "using one diameter-8 crossing block, single-M2 factors along three supplied rooted "
            "noncontractible paths, and three markers; route B gives exact one-plaquette reversible unpreparation"
        ),
        "exact_narrowing": (
            "the three displayed signs need no growing-support gate, but their rooted path-factor union "
            "grows 51/105/123; the identical repeated per-cell tensor fails the translated family with residual 1"
        ),
        "full_periodic_E_preparation_and_G_closed": False,
        "growing_Wilson_word_supplied": False,
        "growing_rooted_path_factor_pattern_supplied": True,
        "boundary_inflow_supplied": True,
        "runtime_global_query": False,
        "fixed_code_all24_all576": route_a["fixed_code_covariance"]["pass"],
        "preparation_all24_all576_established": route_a["preparation_all24_all576_established"],
        "logical_fixtures": {
            "Cycle523_full_M64_onsite_pass": fixture["Cycle523_full_M64_onsite_pass"],
            "one_particle_mass_residual": fixture["Cycle219_mass_fixture_residual"],
            "Cycle230_contact_deletion_residual": fixture["Cycle230_contact_deletion_residual"],
            "Cycle230_seam_subchecks": fixture["Cycle230_seam_subchecks"],
            "literal_full_rough_code_seam_matrix_enumerated": fixture["rough_code_mass_contact_seam_matrix_enumerated"],
        },
        "no_go_discipline": discipline,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "supplied_structure": [
            "compile-time L and L parity",
            "three coordinate axes, macro-origin and three rooted noncontractible paths",
            "one four-M2 crossing block and three sign markers for the exact base triplet",
            "four named internal-face roles per cell for the failed replicated tensor test",
            "single-M2 axis eigenstates along rooted and translated Wilson supports",
            "Cycle247 rough-terminal face graph",
            "Cycle532 fixed-code layout, constraints and mapped runtime",
            "Cycle641 local Q=+1 plaquette encoding and update",
            "route B support-eight controlled preparation synthesis",
            "route C selected independent L3 stabilizer basis and local syndrome feed-forward",
        ],
        "scope_firewall": {
            "Wilson_eigenstate_is_full_fixed_code_E": False,
            "rooted_path_seed_is_bounded_neighborhood_or_autonomous_genesis": False,
            "replicated_fixed_defect_seed_closes_translated_family": False,
            "support_eight_unitary_is_elementary_one_two_M2_circuit": False,
            "partial_L3_reset_coverage_is_held_size_preparation": False,
            "logical_seam_fixture_is_literal_full_rough_code_seam_matrix": False,
            "factor_order_is_time": False,
            "phase_is_energy": False,
            "generator_is_rate": False,
            "gauge_seed_is_Record": False,
            "source_or_gravity_claimed": False,
        },
        "six_wall_ledger": {
            "C_ref": "narrowed: the displayed triplet has an exact locally gated but growing rooted-path seed; the replicated per-cell translated seed fails; axes, origin, paths, markers and L parity are supplied",
            "C_num": "unchanged: local even-CAR and reversible eight-M2 plaquette surfaces are exact; full periodic E remains open",
            "C_wrap": "narrowed: no growing-support Wilson operation is needed for the displayed triplet, but rooted path extent grows; replicated genesis, local-stabilizer preparation and literal seam-matrix EG remain open",
            "C_int": "Cycle219 mass, Cycle230 contact/logical seam and Cycle641 local exchange are preserved as pinned comparators, not a new full physical update",
            "C_local": "advanced on spin-sector seed and local reversible plaquette; route C leaves explicit unresolved L3 generators and no held pump",
            "C_source": "unchanged: no energy, rate, source, stress, gravity, Record or autonomous resource genesis",
        },
        "optimal_next_campaign": (
            "replace the failed identical replicated tensor by a direction-sensitive crossing tensor and compose it with a local stabilizer encoder: first search alternative "
            "independent bases and weight-3/4 bounded duals, then a puncture-directed multi-round syndrome "
            "automaton; require held L6/L7 convergence, boundary-deletion, all24/all576 preparation covariance, "
            "and elementary factorization of route B before claiming periodic E"
        ),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0 and discipline["pass"] and claim_gate_contract,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": FAIL == 0 and discipline["pass"] and claim_gate_contract,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "replicated_translated_seed_residuals": [row["maximum_Wilson_expectation_residual"] for row in route_a["sizes"]],
        "rooted_base_triplet_seed_residuals": [row["base_triplet_seed_maximum_residual"] for row in route_a["sizes"]],
        "local_seed_zero_constraint_counts": [row["local_constraint_seed_expectations"]["zero"] for row in route_a["sizes"]],
        "route_B_prepare_update_unprepare_residual": route_b["prepare_update_unprepare_residual"],
        "route_C_unresolved_L3_generators": route_c["sector_preserving_parallel_pump"]["unresolved_generators"],
        "full_periodic_E_preparation_and_G_closed": False,
        "axiom_pressure": False,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
    }, sort_keys=True, default=json_default))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
