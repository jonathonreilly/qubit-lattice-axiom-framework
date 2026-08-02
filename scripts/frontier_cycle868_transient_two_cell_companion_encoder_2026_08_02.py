#!/usr/bin/env python3
"""Portable Cycle-868 transient companion-E and global-target discriminator.

The runner imports only landed modules beneath ``--repo-root/scripts``.  It
reconstructs the expected pure companion-gauge encoder from the landed exact
factorization object; no prior Cycle-865/866/868 scratch module is imported.
It writes only the declared JSON receipt and performs no Git, PR, review, or
audit mutation.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha1, sha256
from itertools import product
import json
import math
from pathlib import Path
import subprocess
import sys
from time import perf_counter

import numpy as np


SCRIPT = Path(__file__).resolve()
ROOT = SCRIPT.parent
DEFAULT_REPO = ROOT.parent
DEFAULT_OUTPUT = DEFAULT_REPO / (
    "outputs/cycle868_transient_two_cell_companion_encoder_receipt_2026_08_02.json"
)
EXPECTED_ORIGIN_MAIN = "8622da346adf2db00f1e774faa63b542585353de"
PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    "--repo-root", type=Path, default=DEFAULT_REPO,
    help="repository root or a git-archive snapshot containing scripts/",
)
PARSER.add_argument(
    "--source-commit", default=EXPECTED_ORIGIN_MAIN,
    help="commit identifying the supplied repository snapshot",
)
PARSER.add_argument(
    "--output", type=Path, default=DEFAULT_OUTPUT,
)
ARGS = PARSER.parse_args()
REPO = ARGS.repo_root.resolve()
SCRIPTS = REPO / "scripts"
OUTPUT = ARGS.output.resolve()
if ARGS.source_commit != EXPECTED_ORIGIN_MAIN:
    raise SystemExit(
        f"source commit must be current pinned origin/main {EXPECTED_ORIGIN_MAIN}"
    )
if not SCRIPTS.is_dir():
    raise SystemExit(f"missing scripts directory: {SCRIPTS}")
sys.path.insert(0, str(SCRIPTS))


import frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25 as C703
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T708
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M720
import frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27 as S720
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q720
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O720
import frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27 as EB720
import frontier_factorization_object_api_2026_07_28 as FACTOR


DIRECT_IMPORT_SHA256 = {
    "frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py":
        "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4",
    "frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py":
        "f5b604b714e8fbb33e2b6284cb38199e900859d710cd9e1411ee941a021235f3",
    "frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py":
        "c2e7f261c47092f11e445b16bde703330ccfd3e3af06bec0dac078ba64cf2297",
    "frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py":
        "f2fc664a1d14a2d62562ff58395840a0174d4cc75239ef2c1589c6e0f65ed982",
    "frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py":
        "42ada20e51eaf48c14d9862ddce1467982af90874829ddac62ba75b424d45da5",
    "frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py":
        "808c4cc2bac321dbc55aa1195d0768e77ee54cf63432ed04b277cd0ceeb0993c",
    "frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py":
        "ed7cec59daa3a640a48706ed57d6a1699700a61d3d86964ad07a3e2b1c343721",
    "frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py":
        "990016c074cfc98cd2e4ba2f27afe0e7dd2da7a96b9a38a13d4062f778216a36",
    "frontier_factorization_object_api_2026_07_28.py":
        "a6fed8f34adbf36f82501fa827c756ce488d8b67e375e9ae28aa519cd727f0e7",
}
EXPECTED_LOADED_HELPER_COUNT = 45
EXPECTED_LOADED_HELPER_CLOSURE_SHA256 = (
    "23724607a21de418a45acc5783162a7833e4567df709fae761e48ab4ca675dfa"
)
MATTER = 12
PHYSICAL = 18
MATTER_MASK = (1 << MATTER) - 1
TOL = 3.0e-11
DELETE_TOL = 1.0e-7
PRUNE_TOL = 1.0e-13
Pauli = M720.Pauli
Sparse = dict[int, complex]


def file_digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def stable_digest(value) -> str:
    return sha256(repr(value).encode()).hexdigest()


def fields(row: Pauli) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def prune(state: Sparse) -> Sparse:
    return {key: value for key, value in state.items() if abs(value) > PRUNE_TOL}


def norm(state: Sparse) -> float:
    return math.sqrt(sum(abs(value) ** 2 for value in state.values()))


def residual(left: Sparse, right: Sparse) -> float:
    return math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    ))


def overlap(left: Sparse, right: Sparse) -> complex:
    return sum(
        value.conjugate() * right.get(key, 0.0j)
        for key, value in left.items()
    )


def set_bit(value: int, wire: int, bit: int) -> int:
    return (value & ~(1 << wire)) | ((int(bit) & 1) << wire)


def matrix_action(value: int, matrix: np.ndarray, wires: tuple[int, ...]):
    source = sum(
        ((value >> wire) & 1) << index for index, wire in enumerate(wires)
    )
    output = []
    for local_target in range(1 << len(wires)):
        coefficient = matrix[local_target, source]
        if abs(coefficient) <= 1.0e-15:
            continue
        target = value
        for index, wire in enumerate(wires):
            target = set_bit(target, wire, (local_target >> index) & 1)
        output.append((target, coefficient))
    return tuple(output)


def apply_sparse_matrix(
    state: Sparse, matrix: np.ndarray, wires: tuple[int, ...]
) -> Sparse:
    output: dict[int, complex] = defaultdict(complex)
    for basis, amplitude in state.items():
        for target, coefficient in matrix_action(basis, matrix, wires):
            output[target] += coefficient * amplitude
    return prune(dict(output))


def pauli_action(row: Pauli, basis: int) -> tuple[int, complex]:
    return (
        basis ^ row.x,
        (1j ** row.phase) * ((-1) ** ((row.z & basis).bit_count())),
    )


def apply_sparse_pauli(state: Sparse, row: Pauli) -> Sparse:
    output: dict[int, complex] = defaultdict(complex)
    for basis, amplitude in state.items():
        target, phase = pauli_action(row, basis)
        output[target] += phase * amplitude
    return prune(dict(output))


def apply_sparse_rotation(state: Sparse, row: Pauli) -> Sparse:
    rotated = apply_sparse_pauli(state, row)
    scale = 1.0 / math.sqrt(2.0)
    return prune({
        key: scale * (
            state.get(key, 0.0j) - 1j * rotated.get(key, 0.0j)
        )
        for key in set(state) | set(rotated)
    })


def canonical_phase(state: Sparse) -> Sparse:
    length = norm(state)
    if length < 1.0e-14:
        return {}
    normalized = {key: value / length for key, value in state.items()}
    anchor = min(normalized)
    phase = normalized[anchor] / abs(normalized[anchor])
    return {key: value / phase for key, value in normalized.items()}


def projector(state: Sparse, row: Pauli) -> Sparse:
    transformed = apply_sparse_pauli(state, row)
    return prune({
        key: state.get(key, 0.0j) + transformed.get(key, 0.0j)
        for key in set(state) | set(transformed)
    })


@dataclass(frozen=True)
class PairedTransition:
    mask: int
    physical: Pauli
    target: Pauli


class PhysicalEncoder:
    """Pure gauge slice reconstructed from the landed factorization object."""

    def __init__(self, fixture: M720.CompanionFixture):
        self.fixture = fixture
        self.factorization = FACTOR.build_factorization_object(fixture.shape)
        offset = self.factorization.logical_count
        stop = offset + self.factorization.gauge_count
        self.gauge_w = self.factorization.physical_w[offset:stop]
        self.raw_cache: dict[int, Sparse] = {}
        self.phase_cache: dict[int, complex] = {
            0: 1.0 + 0.0j,
            1: 1.0 + 0.0j,
        }
        self.transition_basis = self._transition_basis()

    def _transition_basis(self) -> tuple[PairedTransition, ...]:
        pivots: dict[int, PairedTransition] = {}
        for _family, original_physical, original_target in M720.operator_rows(
            self.fixture
        ):
            if not original_target.x:
                continue
            physical = original_physical
            target = original_target
            mask = target.x
            while mask:
                pivot = mask.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = PairedTransition(mask, physical, target)
                    break
                old = pivots[pivot]
                mask ^= old.mask
                physical = physical @ old.physical
                target = target @ old.target
        if len(pivots) != MATTER - 1:
            raise AssertionError(("even transition rank", len(pivots)))
        return tuple(pivots[key] for key in sorted(pivots, reverse=True))

    def raw_column(self, matter: int) -> Sparse:
        if matter in self.raw_cache:
            return self.raw_cache[matter]
        if matter & ~MATTER_MASK:
            raise ValueError("matter basis outside target width")
        if any(row.x & MATTER_MASK for row in self.gauge_w):
            raise AssertionError("gauge W moves a matter-Z signature")
        for auxiliary in range(1 << (PHYSICAL - MATTER)):
            state: Sparse = {matter | (auxiliary << MATTER): 1.0 + 0.0j}
            for row in self.gauge_w:
                state = projector(state, row)
            if norm(state) > 1.0e-10:
                state = canonical_phase(state)
                self.raw_cache[matter] = state
                return state
        raise AssertionError(("no gauge-signature seed", matter))

    def solve_path(self, difference: int) -> tuple[PairedTransition, ...]:
        output = []
        remainder = difference
        for row in self.transition_basis:
            pivot = row.mask.bit_length() - 1
            if (remainder >> pivot) & 1:
                remainder ^= row.mask
                output.append(row)
        if remainder:
            raise AssertionError(("transition outside even span", difference))
        return tuple(output)

    def phase(self, matter: int) -> complex:
        if matter in self.phase_cache:
            return self.phase_cache[matter]
        root = matter.bit_count() & 1
        current = root
        phase = 1.0 + 0.0j
        for row in self.solve_path(matter ^ root):
            target_matter = current ^ row.target.x
            physical_output = apply_sparse_pauli(
                self.raw_column(current), row.physical
            )
            coefficient = overlap(
                self.raw_column(target_matter), physical_output
            )
            _target_basis, target_phase = pauli_action(row.target, current)
            expected = {
                key: coefficient * value
                for key, value in self.raw_column(target_matter).items()
            }
            if (
                residual(physical_output, expected) > TOL
                or abs(abs(coefficient) - 1.0) > TOL
            ):
                raise AssertionError("encoder transition is not collinear")
            phase *= coefficient / target_phase
            current = target_matter
        if current != matter:
            raise AssertionError(("phase path endpoint", current, matter))
        phase /= abs(phase)
        self.phase_cache[matter] = phase
        return phase

    def column(self, matter: int) -> Sparse:
        phase = self.phase(matter)
        return {
            key: phase * value for key, value in self.raw_column(matter).items()
        }


@dataclass(frozen=True)
class Gate:
    kind: str
    wires: tuple[int, ...]
    matrix: np.ndarray


Z_GATE = np.diag((1.0, -1.0)).astype(complex)


def axis_shape(axis: int) -> tuple[int, int, int]:
    shape = [1, 1, 1]
    shape[axis] = 2
    return tuple(shape)


def e2_word(axis: int) -> tuple[Gate, ...]:
    left_companion = MATTER + axis
    right_companion = MATTER + 3 + axis
    word = [Gate("E2_H", (right_companion,), C712.c707.c655.H)]
    word.extend(
        Gate("E2_CNOT", (wire, left_companion), C712.c707.c655.CNOT)
        for wire in range(6)
    )
    word.extend(
        Gate("E2_Z", (wire,), Z_GATE) for wire in range(6, 12)
    )
    return tuple(word)


def inverse_word(word: tuple[Gate, ...]) -> tuple[Gate, ...]:
    return tuple(
        Gate("inverse_" + gate.kind, gate.wires, gate.matrix.conj().T)
        for gate in reversed(word)
    )


def expanded_word(word: tuple[Gate, ...]) -> tuple[C712.AGate, ...]:
    output = []
    for gate in word:
        if gate.kind.endswith("E2_H"):
            output.append(C712.one("E2_H", gate.wires[0], C712.c707.c655.H))
        elif gate.kind.endswith("E2_CNOT"):
            output.append(C712.cnot(*gate.wires, "E2_CNOT"))
        elif gate.kind.endswith("E2_Z"):
            output.extend((
                C712.one("E2_Z_S", gate.wires[0], C712.c707.S_GATE),
                C712.one("E2_Z_S", gate.wires[0], C712.c707.S_GATE),
            ))
        else:
            raise AssertionError(gate.kind)
    return tuple(output)


def execute(state: Sparse, word: tuple[Gate, ...]) -> Sparse:
    output = dict(state)
    for gate in word:
        output = apply_sparse_matrix(output, gate.matrix, gate.wires)
    return output


def stabilizer_group(rows) -> set[tuple[int, int, int]]:
    output = set()
    for mask in range(1 << len(rows)):
        row = Pauli()
        for index, generator in enumerate(rows):
            if (mask >> index) & 1:
                row = row @ generator
        output.add(fields(row))
    return output


def apply_rotations(state: Sparse, rows) -> Sparse:
    output = state
    for row in rows:
        output = apply_sparse_rotation(output, row)
    return output


def direct_axis_certificate(axis: int) -> dict:
    fixture = M720.CompanionFixture.build(axis_shape(axis))
    encoder = PhysicalEncoder(fixture)
    word = e2_word(axis)
    inverse = inverse_word(word)
    physical_factors = fixture.physical_terms(0)
    target_factors = fixture.target_terms(0)
    column_failures = 0
    maximum_column_residual = 0.0
    single_factor_failures = [0, 0, 0, 0]
    single_factor_maxima = [0.0, 0.0, 0.0, 0.0]
    four_factor_failures = 0
    maximum_four_factor_residual = 0.0
    logical_four_factor: dict[int, Sparse] = {}
    for matter in range(1 << MATTER):
        basis = {matter: 1.0 + 0.0j}
        observed = execute(basis, word)
        value = residual(observed, encoder.column(matter))
        column_failures += value > TOL
        maximum_column_residual = max(maximum_column_residual, value)
        for factor, (physical, target) in enumerate(zip(
            physical_factors, target_factors
        )):
            actual = execute(apply_sparse_rotation(observed, physical), inverse)
            expected = apply_sparse_rotation(basis, target)
            value = residual(actual, expected)
            single_factor_failures[factor] += value > TOL
            single_factor_maxima[factor] = max(
                single_factor_maxima[factor], value
            )
        actual = execute(apply_rotations(observed, physical_factors), inverse)
        expected = apply_rotations(basis, target_factors)
        logical_four_factor[matter] = expected
        value = residual(actual, expected)
        four_factor_failures += value > TOL
        maximum_four_factor_residual = max(
            maximum_four_factor_residual, value
        )

    expanded = expanded_word(word)
    canonical = C712.canonical_rows(PHYSICAL)
    images = C712.apply_word_rows(canonical, expanded)
    gauge_difference = stabilizer_group(
        images[MATTER:PHYSICAL]
    ) ^ stabilizer_group(encoder.gauge_w)
    inverse_tableau_failures = C712.tableau_failures(
        C712.apply_word_rows(
            canonical, expanded + C712.inverse_word(expanded)
        ),
        canonical,
    )
    paired_failures = 0
    paired_family_failures = Counter()
    seam_delta_masks = []
    inverse_expanded = C712.inverse_word(expanded)
    operator_rows = M720.operator_rows(fixture)
    encoded_gauge_group = stabilizer_group(encoder.gauge_w)
    decoded_gauge_rows = C712.apply_word_rows(
        [C712.c707.Pauli(row.phase, row.x, row.z) for row in encoder.gauge_w],
        inverse_expanded,
    )
    decoded_gauge_group = stabilizer_group(decoded_gauge_rows)
    explicit_clean_group = stabilizer_group(tuple(
        Pauli(z=1 << qubit) for qubit in range(MATTER, PHYSICAL)
    ))
    decoded_to_clean_difference = len(
        decoded_gauge_group ^ explicit_clean_group
    )
    encoded_frame_membership_mismatches = 0
    for family, physical, target in operator_rows:
        decoded = C712.apply_word_rows(
            [C712.c707.Pauli(physical.phase, physical.x, physical.z)],
            inverse_expanded,
        )[0]
        delta = decoded @ C712.c707.Pauli(
            target.phase, target.x, target.z
        )
        encoded_frame_membership_mismatches += (
            fields(delta) not in encoded_gauge_group
        )
        passed = fields(delta) in explicit_clean_group
        paired_failures += not passed
        paired_family_failures[family] += not passed
        if family == "seam":
            seam_delta_masks.append(delta.z >> MATTER)

    prepare_deletion_residuals = []
    for deleted in range(len(word)):
        damaged = word[:deleted] + word[deleted + 1:]
        maximum = 0.0
        for matter in range(1 << MATTER):
            state = execute({matter: 1.0 + 0.0j}, damaged)
            state = apply_rotations(state, physical_factors)
            state = execute(state, inverse)
            maximum = max(maximum, residual(
                state, logical_four_factor[matter]
            ))
        prepare_deletion_residuals.append(maximum)

    factor_deletion_residuals = []
    for deleted in range(4):
        maximum = 0.0
        retained = tuple(
            row for index, row in enumerate(physical_factors)
            if index != deleted
        )
        for matter in range(1 << MATTER):
            state = execute({matter: 1.0 + 0.0j}, word)
            state = apply_rotations(state, retained)
            state = execute(state, inverse)
            maximum = max(maximum, residual(
                state, logical_four_factor[matter]
            ))
        factor_deletion_residuals.append(maximum)

    inverse_deletion_residuals = []
    for deleted in range(len(inverse)):
        maximum = 0.0
        damaged = inverse[:deleted] + inverse[deleted + 1:]
        for matter in range(1 << MATTER):
            state = execute({matter: 1.0 + 0.0j}, word)
            state = apply_rotations(state, physical_factors)
            state = execute(state, damaged)
            maximum = max(maximum, residual(
                state, logical_four_factor[matter]
            ))
        inverse_deletion_residuals.append(maximum)

    return {
        "axis": axis,
        "shape": axis_shape(axis),
        "matter_columns_tested": 1 << MATTER,
        "paired_rows_tested": len(operator_rows),
        "seam_factors_tested_individually": 4,
        "abstract_gate_count": len(word),
        "gate_census": dict(sorted(Counter(
            gate.kind for gate in word
        ).items())),
        "column_failures": column_failures,
        "maximum_column_residual": maximum_column_residual,
        "single_factor_failures": single_factor_failures,
        "single_factor_maximum_residuals": single_factor_maxima,
        "four_factor_wrapper_failures": four_factor_failures,
        "maximum_four_factor_wrapper_residual": maximum_four_factor_residual,
        "paired_failures": paired_failures,
        "paired_family_failures": dict(sorted(paired_family_failures.items())),
        "paired_decoded_gauge_membership_failures": paired_failures,
        "decoded_gauge_vs_explicit_clean_group_symmetric_difference": (
            decoded_to_clean_difference
        ),
        "paired_encoded_frame_membership_mismatches": (
            encoded_frame_membership_mismatches
        ),
        "decoded_gauge_generators": [fields(row) for row in decoded_gauge_rows],
        "seam_decoded_clean_Z_masks": seam_delta_masks,
        "gauge_group_symmetric_difference": len(gauge_difference),
        "inverse_tableau_failures": inverse_tableau_failures,
        "factorization_tableau_sha256": encoder.factorization.tableau_digest,
        "prepare_deletion_occurrences": len(prepare_deletion_residuals),
        "prepare_deletion_columns_per_occurrence": 1 << MATTER,
        "prepare_deletion_residuals": prepare_deletion_residuals,
        "all_prepare_deletions_detected": all(
            value > DELETE_TOL for value in prepare_deletion_residuals
        ),
        "inverse_deletion_occurrences": len(inverse_deletion_residuals),
        "inverse_deletion_columns_per_occurrence": 1 << MATTER,
        "inverse_deletion_residuals": inverse_deletion_residuals,
        "all_inverse_deletions_detected": all(
            value > DELETE_TOL for value in inverse_deletion_residuals
        ),
        "factor_deletion_occurrences": len(factor_deletion_residuals),
        "factor_deletion_columns_per_occurrence": 1 << MATTER,
        "factor_deletion_residuals": factor_deletion_residuals,
        "all_factor_deletions_detected": all(
            value > DELETE_TOL for value in factor_deletion_residuals
        ),
    }


def embed_two_cell_row(fixture, edge_index: int, family: str) -> Pauli:
    left, right, _owner, axis, *_rest = fixture.edges[edge_index]
    local_fixture = M720.CompanionFixture.build(axis_shape(axis))
    local = EB720.canonical(getattr(local_fixture, family)(0)[2])
    x = z = 0
    for local_qubit in range(local_fixture.qubits):
        if local_qubit < local_fixture.matter_qubits:
            local_cell, mode = divmod(local_qubit, 6)
            cell = left if local_cell == 0 else right
            target_qubit = 6 * cell + mode
        else:
            local_cell, mode = divmod(
                local_qubit - local_fixture.matter_qubits, 3
            )
            cell = left if local_cell == 0 else right
            target_qubit = fixture.matter_qubits + 3 * cell + mode
        x |= ((local.x >> local_qubit) & 1) << target_qubit
        z |= ((local.z >> local_qubit) & 1) << target_qubit
    return Pauli(local.phase, x, z)


def canonical_delta(left: Pauli, right: Pauli) -> Pauli:
    return EB720.canonical(EB720.canonical(left) @ EB720.canonical(right))


def global_target_delta_certificate(shape: tuple[int, int, int]) -> dict:
    fixture = M720.CompanionFixture.build(shape)
    reference = O720.arbitrary_fixture(Q720.shape_cells(shape))
    fixture_identity_failures = int(
        fixture.cells != reference.cells
        or fixture.edges != reference.edges
        or fixture.qubits != reference.qubits
    )
    physical_local_failures = 0
    target_bridge_replay_failures = 0
    bridge_non_Z_failures = 0
    phase_two_failures = 0
    physical_target_phase_two_failures = 0
    weight_formula_failures = 0
    by_axis: dict[str, dict] = {}
    total_weight = 0
    maximum_weight = 0
    for edge, row in enumerate(fixture.edges):
        left, right, _owner, axis, *_rest = row
        local_physical = embed_two_cell_row(fixture, edge, "physical_terms")
        full_physical = fixture.physical_terms(edge)[2]
        local_target = embed_two_cell_row(fixture, edge, "target_terms")
        full_target = fixture.target_terms(edge)[2]
        physical_delta = canonical_delta(local_physical, full_physical)
        bridge = canonical_delta(local_target, full_target)
        replay = EB720.canonical(EB720.canonical(local_target) @ bridge)
        physical_local_failures += fields(physical_delta) != (0, 0, 0)
        target_bridge_replay_failures += fields(replay) != fields(
            EB720.canonical(full_target)
        )
        bridge_non_Z_failures += bool(bridge.x)
        phase_two_failures += (
            (full_target.phase - EB720.canonical(full_target).phase) % 4 != 2
        )
        physical_target_phase_two_failures += (
            (full_target.phase - full_physical.phase) % 4 != 2
        )
        distance = right - left
        weight = (bridge.x | bridge.z).bit_count()
        weight_formula_failures += weight != 6 * (distance - 1)
        total_weight += weight
        maximum_weight = max(maximum_weight, weight)
        axis_row = by_axis.setdefault(str(axis), {
            "edges": 0,
            "lexicographic_cell_index_distances": set(),
            "Z_bridge_weights": set(),
        })
        axis_row["edges"] += 1
        axis_row["lexicographic_cell_index_distances"].add(distance)
        axis_row["Z_bridge_weights"].add(weight)
    for axis_row in by_axis.values():
        axis_row["lexicographic_cell_index_distances"] = sorted(
            axis_row["lexicographic_cell_index_distances"]
        )
        axis_row["Z_bridge_weights"] = sorted(axis_row["Z_bridge_weights"])
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "Cycle789_fixture_identity_failures": fixture_identity_failures,
        "physical_equals_embedded_two_cell_failures": physical_local_failures,
        "target_bridge_replay_failures": target_bridge_replay_failures,
        "bridge_non_Z_failures": bridge_non_Z_failures,
        "raw_target_to_canonical_phase_two_failures": phase_two_failures,
        "raw_physical_to_target_phase_two_failures": (
            physical_target_phase_two_failures
        ),
        "weight_formula_6_times_lexicographic_distance_minus_one_failures": (
            weight_formula_failures
        ),
        "total_Z_bridge_weight": total_weight,
        "maximum_Z_bridge_weight": maximum_weight,
        "by_axis": by_axis,
        "boundary": (
            "the landed physical edge row is exactly two-cell local; the "
            "full target adds a Z-only lexicographic Jordan--Wigner bridge "
            "whose support grows with intervening cells"
        ),
    }


def gf2_rank(rows) -> int:
    pivots = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def target_character_census(shape: tuple[int, int, int]) -> dict:
    """Compare local term-2 targets with the full Cycle789 JW characters."""
    fixture = M720.CompanionFixture.build(shape)
    local_rows = tuple(
        EB720.canonical(embed_two_cell_row(fixture, edge, "target_terms"))
        for edge in range(len(fixture.edges))
    )
    full_rows = tuple(
        EB720.canonical(fixture.target_terms(edge)[2])
        for edge in range(len(fixture.edges))
    )

    def family(rows) -> dict:
        anticommuting_pairs = sum(
            not rows[left].commutes(rows[right])
            for left in range(len(rows)) for right in range(left)
        )
        gram_rows = tuple(
            sum(
                (not rows[left].commutes(rows[right])) << right
                for right in range(len(rows))
            )
            for left in range(len(rows))
        )
        return {
            "rows": len(rows),
            "GF2_character_rank": gf2_rank(
                row.symplectic(fixture.matter_qubits) for row in rows
            ),
            "anticommuting_pairs": anticommuting_pairs,
            "GF2_commutator_Gram_rank": gf2_rank(gram_rows),
        }

    return {
        "shape": shape,
        "embedded_local_term2": family(local_rows),
        "full_JW_term2": family(full_rows),
        "boundary": (
            "deleting the bridge while retaining the same Bell-character "
            "basis changes a commuting full-rank family into a noncommuting "
            "full-rank family; this is not an auxiliary-minimum theorem and "
            "does not exclude local gauge extensions"
        ),
    }


def landed_mass_contact_fixture() -> dict:
    """Rerun the landed Cycle720/Cycle822 one-particle fixture surface."""
    raw = M720.C.R.local_free_contact_mass()["mass_contact"]
    report = {
        key: value.item() if isinstance(value, np.generic) else value
        for key, value in raw.items()
    }
    rows = []
    for mode in range(6):
        matter = 1 << mode
        references = C703.encoded_reference_mask(matter, 1)
        total_parity = (matter.bit_count() + references.bit_count()) & 1
        flipped_total_parity = (
            matter.bit_count() + (references ^ 1).bit_count()
        ) & 1
        rows.append({
            "mode": mode,
            "reference_bits": references,
            "extended_total_parity": total_parity,
            "flipped_reference_total_parity": flipped_total_parity,
        })
    failures = sum(row["extended_total_parity"] != 0 for row in rows)
    flipped_detection_failures = sum(
        row["flipped_reference_total_parity"] != 1 for row in rows
    )
    report.update({
        "one_particle_extended_even_sector_columns_tested": len(rows),
        "one_particle_extended_even_sector_failures": failures,
        "one_particle_wrong_reference_flip_detection_failures": (
            flipped_detection_failures
        ),
        "one_particle_extended_even_sector_rows": rows,
        "one_particle_extended_even_sector_present": failures == 0,
    })
    return report


def six_layer_certificate(shape: tuple[int, int, int]) -> dict:
    fixture = M720.CompanionFixture.build(shape)
    colours = Counter()
    factor_coverage = Counter()
    cell_sets = []
    edge_colours = []
    for edge, row in enumerate(fixture.edges):
        colour = (int(row[3]), sum(row[2]) & 1)
        colours[colour] += 1
        edge_colours.append(colour)
        cell_sets.append(frozenset(row[:2]))
        for factor in range(4):
            factor_coverage[(edge, factor)] += 1
    conflicts = 0
    for left in range(len(fixture.edges)):
        for right in range(left):
            conflicts += (
                edge_colours[left] == edge_colours[right]
                and bool(cell_sets[left] & cell_sets[right])
            )
    return {
        "shape": shape,
        "edges": len(fixture.edges),
        "factors": 4 * len(fixture.edges),
        "colours_present": len(colours),
        "colour_census": {
            str(key): value for key, value in sorted(colours.items())
        },
        "same_colour_cell_conflicts": conflicts,
        "factor_coverage_failures": sum(
            value != 1 for value in factor_coverage.values()
        ) + 4 * len(fixture.edges) - len(factor_coverage),
        "layer_label": "(axis, positive-edge-owner body parity)",
    }


def frame_words(source, target, frame, native_expanded):
    matter_x, matter_z = Q720.matter_images(
        source, target, frame, (0, 0, 0)
    )
    physical_x, physical_z = Q720.corrected_images(
        source, target, frame, (0, 0, 0),
        Q720.predicted_sheet_solution(frame),
    )
    matter_decode = tuple(C712.synthesize_decode(matter_z, matter_x))
    physical_decode = tuple(C712.synthesize_decode(physical_z, physical_x))
    return (
        matter_decode + native_expanded + C712.inverse_word(physical_decode),
        (matter_x, matter_z),
        (physical_x, physical_z),
    )


def colour_action(frame, colour):
    axis, parity = colour
    target_axis = next(
        row for row in range(3) if int(frame[row, axis]) != 0
    )
    return target_axis, parity ^ (int(frame[target_axis, axis]) < 0)


def frame_covariance_certificate() -> dict:
    source = M720.CompanionFixture.build((2, 1, 1))
    encoder = PhysicalEncoder(source)
    native = expanded_word(e2_word(0))
    frames = tuple(T708.proper_cubic_frames())
    paired_failures = gauge_differences = inverse_failures = 0
    decoded_gauge_to_clean_differences = 0
    encoded_frame_membership_mismatches = 0
    active_gate_maximum = active_two_qubit_maximum = 0
    direct_native_matches = 0
    explicit_clean_group = stabilizer_group(tuple(
        Pauli(z=1 << qubit) for qubit in range(MATTER, PHYSICAL)
    ))
    for frame in frames:
        target = O720.arbitrary_fixture(Q720.affine_cells(
            source.cells, frame, (0, 0, 0)
        ))
        word, _matter_images, physical_images = frame_words(
            source, target, frame, native
        )
        canonical = C712.canonical_rows(PHYSICAL)
        images = C712.apply_word_rows(canonical, word)
        transported_gauge = tuple(
            S720.apply_images(S720.cpauli(row), physical_images)
            for row in encoder.gauge_w
        )
        transported_gauge_group = stabilizer_group(transported_gauge)
        gauge_differences += len(
            stabilizer_group(images[MATTER:PHYSICAL])
            ^ transported_gauge_group
        )
        inverse = C712.inverse_word(word)
        decoded_transported_gauge = C712.apply_word_rows(
            [
                C712.c707.Pauli(row.phase, row.x, row.z)
                for row in transported_gauge
            ],
            inverse,
        )
        decoded_transported_gauge_group = stabilizer_group(
            decoded_transported_gauge
        )
        decoded_gauge_to_clean_differences += len(
            decoded_transported_gauge_group ^ explicit_clean_group
        )
        for _family, physical, target_row in M720.operator_rows(target):
            decoded = C712.apply_word_rows(
                [C712.c707.Pauli(physical.phase, physical.x, physical.z)],
                inverse,
            )[0]
            delta = decoded @ C712.c707.Pauli(
                target_row.phase, target_row.x, target_row.z
            )
            encoded_frame_membership_mismatches += (
                fields(delta) not in transported_gauge_group
            )
            paired_failures += (
                fields(delta) not in explicit_clean_group
            )
        inverse_failures += C712.tableau_failures(
            C712.apply_word_rows(canonical, word + inverse), canonical
        )
        active_gate_maximum = max(active_gate_maximum, len(word))
        active_two_qubit_maximum = max(
            active_two_qubit_maximum,
            sum(len(gate.wires) == 2 for gate in word),
        )
        direct = expanded_word(e2_word(target.edges[0][3]))
        direct_native_matches += C712.tableau_failures(
            C712.apply_word_rows(canonical, word),
            C712.apply_word_rows(canonical, direct),
        ) == 0

    physical_product_failures = matter_product_failures = 0
    colour_bijection_failures = colour_product_failures = 0
    colours = tuple(product(range(3), range(2)))
    for right in frames:
        colour_bijection_failures += (
            len({colour_action(right, colour) for colour in colours}) != 6
        )
        middle = O720.arbitrary_fixture(Q720.affine_cells(
            source.cells, right, (0, 0, 0)
        ))
        right_p = Q720.corrected_images(
            source, middle, right, (0, 0, 0),
            Q720.predicted_sheet_solution(right),
        )
        right_m = Q720.matter_images(source, middle, right, (0, 0, 0))
        for left in frames:
            final = O720.arbitrary_fixture(Q720.affine_cells(
                middle.cells, left, (0, 0, 0)
            ))
            combined = left @ right
            left_p = Q720.corrected_images(
                middle, final, left, (0, 0, 0),
                Q720.predicted_sheet_solution(left),
            )
            combined_p = Q720.corrected_images(
                source, final, combined, (0, 0, 0),
                Q720.predicted_sheet_solution(combined),
            )
            physical_product_failures += not Q720.images_equal(
                S720.compose_images(left_p, right_p), combined_p
            )
            left_m = Q720.matter_images(
                middle, final, left, (0, 0, 0)
            )
            combined_m = Q720.matter_images(
                source, final, combined, (0, 0, 0)
            )
            matter_product_failures += not Q720.images_equal(
                S720.compose_images(left_m, right_m), combined_m
            )
            colour_product_failures += any(
                colour_action(left, colour_action(right, colour))
                != colour_action(combined, colour)
                for colour in colours
            )

    translation_failures = 0
    for shift in product(range(2), repeat=3):
        for axis, parity in colours:
            owner = [0, 0, 0]
            owner[(axis + 1) % 3] = parity
            translated = tuple(owner[index] + shift[index] for index in range(3))
            observed = (axis, sum(translated) & 1)
            expected = (axis, parity ^ (sum(shift) & 1))
            translation_failures += observed != expected
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "active_paired_failures": paired_failures,
        "active_encoded_frame_membership_mismatches": (
            encoded_frame_membership_mismatches
        ),
        "active_gauge_group_symmetric_difference": gauge_differences,
        "active_decoded_gauge_to_clean_group_symmetric_difference": (
            decoded_gauge_to_clean_differences
        ),
        "active_inverse_failures": inverse_failures,
        "physical_frame_product_failures": physical_product_failures,
        "matter_frame_product_failures": matter_product_failures,
        "six_colour_bijection_failures": colour_bijection_failures,
        "six_colour_product_failures": colour_product_failures,
        "translation_colour_law_failures": translation_failures,
        "active_gate_maximum": active_gate_maximum,
        "active_two_qubit_gate_maximum": active_two_qubit_maximum,
        "direct_13_gate_native_slice_frames": direct_native_matches,
        "boundary": (
            "abstract active Clifford/tableau covariance only; literal routing "
            "of the 23 non-selected active words is not claimed"
        ),
    }


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return sha1(header + data).hexdigest()


def landed_import_inventory() -> tuple[list[dict], list[str]]:
    files: dict[Path, set[str]] = {}
    foreign = []
    for name, module in tuple(sys.modules.items()):
        raw_path = getattr(module, "__file__", None)
        if not raw_path:
            continue
        path = Path(raw_path).resolve()
        if path.suffix == ".pyc" and path.parent.name == "__pycache__":
            path = path.parent.parent / (path.name.split(".")[0] + ".py")
        try:
            path.relative_to(SCRIPTS)
        except ValueError:
            if name.startswith("frontier_"):
                foreign.append(f"{name}:{path}")
            continue
        files.setdefault(path, set()).add(name)
    inventory = []
    for path, names in sorted(files.items(), key=lambda row: str(row[0])):
        data = path.read_bytes()
        inventory.append({
            "relative_path": str(path.relative_to(REPO)),
            "module_names": sorted(names),
            "bytes": len(data),
            "sha256": sha256(data).hexdigest(),
            "git_blob_sha1": git_blob_sha1(data),
        })
    return inventory, sorted(foreign)


def loaded_helper_closure_certificate(inventory: list[dict]) -> dict:
    """Content-pin the complete loaded repo-local helper closure.

    The changed Cycle868 runner is excluded because its hash is recorded
    separately as ``runner_sha256``.  Every other loaded Python source below
    ``scripts/`` contributes both its relative path and SHA-256 to the frozen
    closure digest, so a changed, missing, or newly loaded transitive helper
    changes this certificate.
    """
    runner_path = f"scripts/{SCRIPT.name}"
    rows = sorted(
        (row["relative_path"], row["sha256"])
        for row in inventory
        if row["relative_path"] != runner_path
    )
    observed = sha256(json.dumps(
        rows, separators=(",", ":")
    ).encode()).hexdigest()
    return {
        "runner_path_excluded": runner_path,
        "loaded_helper_count": len(rows),
        "expected_loaded_helper_count": EXPECTED_LOADED_HELPER_COUNT,
        "observed_closure_sha256": observed,
        "expected_closure_sha256": EXPECTED_LOADED_HELPER_CLOSURE_SHA256,
        "match": (
            len(rows) == EXPECTED_LOADED_HELPER_COUNT
            and observed == EXPECTED_LOADED_HELPER_CLOSURE_SHA256
        ),
    }


def source_commit_object_certificate() -> dict:
    """Verify the named source commit when Git metadata is available.

    Git-archive snapshots have no object database; for those, the complete
    loaded-helper closure pin remains the portable source-identity gate.
    """
    try:
        inside = subprocess.run(
            ("git", "-C", str(REPO), "rev-parse", "--is-inside-work-tree"),
            capture_output=True, text=True, check=False,
        )
        repository_has_git_metadata = (
            inside.returncode == 0 and inside.stdout.strip() == "true"
        )
        exists = subprocess.run(
            (
                "git", "-C", str(REPO), "cat-file", "-e",
                f"{ARGS.source_commit}^{{commit}}",
            ),
            capture_output=True, text=True, check=False,
        ) if repository_has_git_metadata else None
    except OSError:
        repository_has_git_metadata = False
        exists = None
    return {
        "named_source_commit": ARGS.source_commit,
        "repository_has_git_metadata": repository_has_git_metadata,
        "commit_object_exists": (
            None if exists is None else exists.returncode == 0
        ),
        "verification_mode": (
            "git_commit_object_plus_loaded_helper_closure"
            if repository_has_git_metadata
            else "portable_loaded_helper_closure_only"
        ),
    }


def main() -> None:
    started = perf_counter()
    direct_hash_failures = sum(
        file_digest(SCRIPTS / name) != expected
        for name, expected in DIRECT_IMPORT_SHA256.items()
    )
    axes = []
    for axis in range(3):
        axes.append(direct_axis_certificate(axis))
        print(f"axis {axis} complete", flush=True)
    shapes = ((3, 2, 2), (5, 3, 2))
    target_deltas = [global_target_delta_certificate(shape) for shape in shapes]
    character_census = [target_character_census(shape) for shape in shapes]
    layers = [six_layer_certificate(shape) for shape in shapes]
    covariance = frame_covariance_certificate()
    mass_contact = landed_mass_contact_fixture()
    inventory, foreign_imports = landed_import_inventory()
    helper_closure = loaded_helper_closure_certificate(inventory)
    source_commit_object = source_commit_object_certificate()
    inventory_paths = {row["relative_path"] for row in inventory}
    direct_inventory_failures = sum(
        f"scripts/{name}" not in inventory_paths
        for name in DIRECT_IMPORT_SHA256
    )
    checks = {
        "pinned_origin_main_direct_import_hashes": direct_hash_failures == 0,
        "pinned_origin_main_complete_loaded_helper_closure": (
            helper_closure["match"]
        ),
        "named_source_commit_object_exists_when_git_is_available": (
            not source_commit_object["repository_has_git_metadata"]
            or source_commit_object["commit_object_exists"] is True
        ),
        "all_frontier_imports_beneath_repo_scripts": not foreign_imports,
        "direct_import_inventory_complete": direct_inventory_failures == 0,
        "three_native_13_gate_words_exact": all(
            row["abstract_gate_count"] == 13
            and row["matter_columns_tested"] == 4096
            and row["column_failures"] == 0
            and row["paired_rows_tested"] == 76
            and row["paired_failures"] == 0
            and row["gauge_group_symmetric_difference"] == 0
            and row[
                "decoded_gauge_vs_explicit_clean_group_symmetric_difference"
            ] == 0
            for row in axes
        ),
        "four_seam_factors_and_complete_wrapper_exact": all(
            row["seam_factors_tested_individually"] == 4
            and not any(row["single_factor_failures"])
            and row["four_factor_wrapper_failures"] == 0
            and row["inverse_tableau_failures"] == 0
            for row in axes
        ),
        "all_prepare_inverse_factor_deletions_detected": all(
            row["all_prepare_deletions_detected"]
            and row["all_inverse_deletions_detected"]
            and row["all_factor_deletions_detected"]
            for row in axes
        ),
        "Cycle789_full_target_delta_is_exact_growing_Z_bridge": all(
            all(row[key] == 0 for key in (
                "Cycle789_fixture_identity_failures",
                "physical_equals_embedded_two_cell_failures",
                "target_bridge_replay_failures",
                "bridge_non_Z_failures",
                "raw_target_to_canonical_phase_two_failures",
                "raw_physical_to_target_phase_two_failures",
                "weight_formula_6_times_lexicographic_distance_minus_one_failures",
            ))
            for row in target_deltas
        ),
        "local_vs_full_term2_character_census_matches": all(
            row["embedded_local_term2"]["GF2_character_rank"] == expected[0]
            and row["embedded_local_term2"]["anticommuting_pairs"] == expected[1]
            and row["embedded_local_term2"]["GF2_commutator_Gram_rank"] == expected[2]
            and row["full_JW_term2"]["GF2_character_rank"] == expected[3]
            and row["full_JW_term2"]["anticommuting_pairs"] == expected[4]
            and row["full_JW_term2"]["GF2_commutator_Gram_rank"] == 0
            for row, expected in zip(
                character_census,
                ((20, 22, 16, 20, 0), (59, 76, 46, 59, 0)),
            )
        ),
        "six_disjoint_axis_parity_layers_cover_all_factors": all(
            row["colours_present"] == 6
            and row["same_colour_cell_conflicts"] == 0
            and row["factor_coverage_failures"] == 0
            for row in layers
        ),
        "abstract_active_24_frames_576_products_exact": all(
            covariance[key] == 0 for key in (
                "active_paired_failures",
                "active_gauge_group_symmetric_difference",
                "active_decoded_gauge_to_clean_group_symmetric_difference",
                "active_inverse_failures",
                "physical_frame_product_failures",
                "matter_frame_product_failures",
                "six_colour_bijection_failures",
                "six_colour_product_failures",
                "translation_colour_law_failures",
            )
        ),
        "landed_one_particle_mass_and_contact_fixture_rerun": (
            mass_contact["one_particle_coin_eigen_residual"] < 1.0e-12
            and mass_contact["one_particle_mass_residual"] < 1.0e-12
            and mass_contact[
                "contact_vacuum_and_one_particle_residual"
            ] < 1.0e-12
            and mass_contact[
                "contact_double_occupation_phase_residual"
            ] < 1.0e-12
            and mass_contact[
                "one_particle_extended_even_sector_columns_tested"
            ] == 6
            and mass_contact[
                "one_particle_extended_even_sector_failures"
            ] == 0
            and mass_contact[
                "one_particle_wrong_reference_flip_detection_failures"
            ] == 0
            and mass_contact["one_particle_extended_even_sector_present"]
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "PORTABLE_ORIGIN_MAIN_LOCAL_E2_AND_TARGET_DELTA",
        "source_commit": ARGS.source_commit,
        "runner_sha256": file_digest(Path(__file__).resolve()),
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "checks": checks,
        "native_axes": axes,
        "Cycle789_full_target_deltas": target_deltas,
        "local_vs_full_target_character_census": character_census,
        "six_axis_parity_layers": layers,
        "abstract_active_covariance": covariance,
        "landed_one_particle_mass_contact_fixture": mass_contact,
        "direct_import_sha256_pins": DIRECT_IMPORT_SHA256,
        "loaded_helper_closure_pin": helper_closure,
        "source_commit_object_certificate": source_commit_object,
        "loaded_landed_import_count": len(inventory),
        "loaded_landed_import_inventory": inventory,
        "foreign_frontier_imports": foreign_imports,
        "scope": {
            "claims_literal_active_routing": False,
            "claims_schedule_arbitration_no_go": False,
            "claims_global_JW_bridge_is_bounded_local": False,
            "claims_commutator_Gram_rank_is_an_auxiliary_minimum": False,
            "repository_mutations_beyond_declared_receipt": False,
        },
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = stable_digest(report)
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "receipt": str(OUTPUT),
        "runtime_seconds": report["runtime_seconds"],
        "report_sha256": report["report_sha256"],
    }, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
