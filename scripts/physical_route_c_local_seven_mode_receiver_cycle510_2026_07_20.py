#!/usr/bin/env python3
"""Cycle 510 local certificate for the Route-C seven-mode receiver.

This is a local, pre-response certificate only.  It supplies one candidate
statistics law: the parked mode and six directional mediator modes are
literal hard-core qubit/spin occupations on seven M2 factors.  Consequently
ordinary SWAP, not fermionic FSWAP, is the mediator transport primitive.
Cycle 501's Q=1 sector cannot select between those two statistics laws.

The runner constructs the full local M64 x 2^7 alphabet, the charge-preserving
summed Cycle-501 collision generator, its N=2/Q=1 restriction, the directional
emitter, and the full-occupation moving stream.  It executes no response row,
no resource scout, no held row, and no physical interpretation.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy import sparse
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_reciprocal_mediator_contact_dressed_tournament_cycle501_2026_07_20 as c501
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


AUTHORITY = "none"
AUDIT = "unset"
STATISTICS_LAW = "hard-core-qubit-spin-occupation-with-ordinary-SWAP"
LIVE_STATISTICS_ALTERNATIVE = "fermionic-exterior-Fock-with-FSWAP-and-local-gauge"
PARKED = 0
DIRECTION_BITS = tuple(range(1, 7))
REVERSE = tuple(int(value) for value in c501.REVERSE)
UNORIENTED = tuple((direction, REVERSE[direction]) for direction in (0, 2, 4))
MATTER_DIMENSION = 64
MEDIATOR_DIMENSION = 128
LOCAL_DIMENSION = MATTER_DIMENSION * MEDIATOR_DIMENSION
ROUTE_C_MAX_LOCAL_Q = 6
TEST_ANGLE = 0.173
CYCLE501_SEAM_ANGLE = c501.COLLISION_COUPLING
NUMERIC_TOLERANCE = 1e-10
INVERSE_TOLERANCE = 1e-9
TRAIN_BETAS = (-2 * np.pi / 9, -4 * np.pi / 9, -2 * np.pi / 3)
DEPENDENCIES = (
    Path(c210.__file__).resolve(),
    Path(c219.__file__).resolve(),
    Path(c230.__file__).resolve(),
    Path(c311.__file__).resolve(),
    Path(c315.__file__).resolve(),
    Path(c501.__file__).resolve(),
)


@dataclass(frozen=True)
class TestResult:
    name: str
    passed: bool
    detail: object


RESULTS: list[TestResult] = []


def check(name: str, condition: bool, detail: object = None) -> None:
    RESULTS.append(TestResult(name, bool(condition), detail))


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def bit_sign(values: list[int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def fermion_hop(mask: int, old: int, new: int) -> tuple[int, int] | None:
    """Apply c_new^dagger c_old to a six-mode exterior occupation."""
    if not (mask >> old) & 1 or (mask >> new) & 1:
        return None
    annihilation = -1 if (mask & ((1 << old) - 1)).bit_count() % 2 else 1
    reduced = mask ^ (1 << old)
    creation = -1 if (reduced & ((1 << new) - 1)).bit_count() % 2 else 1
    return reduced | (1 << new), annihilation * creation


def local_index(matter: int, mediator: int) -> int:
    return matter * MEDIATOR_DIMENSION + mediator


def local_decode(index: int) -> tuple[int, int]:
    return divmod(index, MEDIATOR_DIMENSION)


def collision_generator() -> tuple[
    sparse.csr_matrix,
    dict[tuple[int, int], complex],
    tuple[sparse.csr_matrix, ...],
]:
    """One Hermitian sum over the three unoriented reciprocal pairs."""
    entries: dict[tuple[int, int], complex] = defaultdict(complex)
    axis_entries: tuple[dict[tuple[int, int], complex], ...] = tuple(
        defaultdict(complex) for _pair in UNORIENTED
    )
    for matter in range(MATTER_DIMENSION):
        for mediator in range(MEDIATOR_DIMENSION):
            source = local_index(matter, mediator)
            for axis, (direction, reverse) in enumerate(UNORIENTED):
                direction_bit = 1 << (1 + direction)
                reverse_bit = 1 << (1 + reverse)
                if not mediator & direction_bit or mediator & reverse_bit:
                    continue
                hop = fermion_hop(matter, reverse, direction)
                if hop is None:
                    continue
                target_matter, sign = hop
                target_mediator = mediator ^ direction_bit ^ reverse_bit
                target = local_index(target_matter, target_mediator)
                entries[(target, source)] += sign
                entries[(source, target)] += sign
                axis_entries[axis][(target, source)] += sign
                axis_entries[axis][(source, target)] += sign
    rows = [row for row, _column in entries]
    columns = [column for _row, column in entries]
    data = [entries[(row, column)] for row, column in entries]
    matrix = sparse.coo_matrix(
        (data, (rows, columns)), shape=(LOCAL_DIMENSION, LOCAL_DIMENSION), dtype=complex
    ).tocsr()
    matrix.sum_duplicates()
    axis_matrices = []
    for block in axis_entries:
        block_rows = [row for row, _column in block]
        block_columns = [column for _row, column in block]
        block_data = [block[(row, column)] for row, column in block]
        axis_matrices.append(
            sparse.coo_matrix(
                (block_data, (block_rows, block_columns)),
                shape=(LOCAL_DIMENSION, LOCAL_DIMENSION),
                dtype=complex,
            ).tocsr()
        )
    return matrix, dict(entries), tuple(axis_matrices)


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    permutation = c210.direction_permutation(frame)
    return tuple(int(np.argmax(permutation[:, direction])) for direction in range(6))


def transform_matter(mask: int, frame: np.ndarray) -> tuple[int, int]:
    moved = [direction_map(frame)[value] for value in range(6) if (mask >> value) & 1]
    output = sum(1 << value for value in moved)
    return output, bit_sign(moved)


def transform_mediator(mask: int, frame: np.ndarray) -> int:
    moved = mask & 1
    mapping = direction_map(frame)
    for direction in range(6):
        if (mask >> (1 + direction)) & 1:
            moved |= 1 << (1 + mapping[direction])
    return moved


def transform_local(index: int, frame: np.ndarray) -> tuple[int, int]:
    matter, mediator = local_decode(index)
    moved_matter, sign = transform_matter(matter, frame)
    return local_index(moved_matter, transform_mediator(mediator, frame)), sign


def collision_covariance(entries: dict[tuple[int, int], complex]) -> float:
    maximum = 0.0
    for frame in c210.proper_cubic_frames():
        for (target, source), amplitude in entries.items():
            moved_target, target_sign = transform_local(target, frame)
            moved_source, source_sign = transform_local(source, frame)
            expected = amplitude * target_sign * source_sign
            actual = entries.get((moved_target, moved_source), 0j)
            maximum = max(maximum, float(abs(actual - expected)))
    return maximum


def cycle501_q1_n2_residual(
    entries: dict[tuple[int, int], complex]
) -> tuple[float, float, int]:
    """Compare the exact 90D restriction against Cycle501's target function."""
    pairs = tuple(combinations(range(6), 2))
    basis = tuple((pair, mediator) for pair in pairs for mediator in range(6))
    index = {label: position for position, label in enumerate(basis)}
    expected = np.zeros((len(basis), len(basis)), dtype=complex)
    actual = np.zeros_like(expected)
    explicit_unitary = np.zeros_like(expected)
    cell = (0, 0, 0)
    for column, (pair, mediator_direction) in enumerate(basis):
        key = (
            tuple((cell, direction) for direction in pair),
            cell,
            mediator_direction,
        )
        target = c501.explicit_collision_target(key)
        if target is not None:
            target_key, wedge_sign = target
            target_pair = tuple(direction for _position, direction in target_key[0])
            expected[index[(target_pair, target_key[2])], column] = wedge_sign

        explicit_output = c501.explicit_collision(
            {key: 1 + 0j}, coupling=CYCLE501_SEAM_ANGLE
        )
        for output_key, amplitude in explicit_output.items():
            output_pair = tuple(direction for _position, direction in output_key[0])
            explicit_unitary[index[(output_pair, output_key[2])], column] += amplitude

        matter = sum(1 << direction for direction in pair)
        mediator = 1 << (1 + mediator_direction)
        source_local = local_index(matter, mediator)
        for target_local in range(LOCAL_DIMENSION):
            value = entries.get((target_local, source_local), 0j)
            if not value:
                continue
            target_matter, target_mediator = local_decode(target_local)
            if target_matter.bit_count() != 2 or target_mediator.bit_count() != 1:
                continue
            if target_mediator & 1:
                continue
            target_pair = tuple(value for value in range(6) if (target_matter >> value) & 1)
            target_direction = (target_mediator.bit_length() - 1) - 1
            actual[index[(target_pair, target_direction)], column] += value
    exponential_residual = float(
        np.linalg.norm(
            expm(1j * CYCLE501_SEAM_ANGLE * actual) - explicit_unitary
        )
    )
    return (
        float(np.linalg.norm(actual - expected)),
        exponential_residual,
        int(np.count_nonzero(expected)),
    )


def collision_sector_controls(
    generator: sparse.csr_matrix,
    axis_matrices: tuple[sparse.csr_matrix, ...],
) -> dict:
    dimensions = []
    nonzeros = []
    for charge in range(ROUTE_C_MAX_LOCAL_Q + 1):
        indices = np.asarray(
            [
                local_index(matter, mediator)
                for matter in range(MATTER_DIMENSION)
                for mediator in range(MEDIATOR_DIMENSION)
                if mediator.bit_count() == charge
            ],
            dtype=int,
        )
        dimensions.append(len(indices))
        nonzeros.append(generator[indices, :][:, indices].nnz)
    commutators = [
        float(sparse.linalg.norm(axis_matrices[left] @ axis_matrices[right]
                                 - axis_matrices[right] @ axis_matrices[left]))
        for left in range(len(axis_matrices))
        for right in range(left + 1, len(axis_matrices))
    ]
    return {
        "Q_0_through_6_dimensions": dimensions,
        "Q_0_through_6_generator_nnz": nonzeros,
        "Q_0_through_6_total_dimension": sum(dimensions),
        "Q_0_through_6_total_nnz": sum(nonzeros),
        "three_unoriented_axis_block_nnz": [matrix.nnz for matrix in axis_matrices],
        "maximum_axis_block_commutator": max(commutators, default=0.0),
        "maximum_axis_block_Hermiticity_residual": max(
            float(sparse.linalg.norm(matrix - matrix.getH()))
            for matrix in axis_matrices
        ),
        "construction_rule": "three unoriented terms plus Hermitian conjugates",
        "six_directed_terms_plus_HC_forbidden_double_count": True,
        "one_exponential_is_provenance_not_numerical_discriminator_here": True,
    }


def emitter_matrix(direction: int, angle: float) -> sparse.csr_matrix:
    parked_bit = 1 << PARKED
    direction_bit = 1 << (1 + direction)
    cosine, sine = np.cos(angle), np.sin(angle)
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for source in range(MEDIATOR_DIMENSION):
        parked_occupied = bool(source & parked_bit)
        direction_occupied = bool(source & direction_bit)
        if parked_occupied == direction_occupied:
            rows.append(source)
            columns.append(source)
            data.append(1)
        else:
            target = source ^ parked_bit ^ direction_bit
            rows.extend((source, target))
            columns.extend((source, source))
            data.extend((cosine, 1j * sine))
    return sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(MEDIATOR_DIMENSION, MEDIATOR_DIMENSION),
        dtype=complex,
    ).tocsr()


def mediator_frame_matrix(frame: np.ndarray) -> sparse.csr_matrix:
    rows = [transform_mediator(source, frame) for source in range(MEDIATOR_DIMENSION)]
    columns = list(range(MEDIATOR_DIMENSION))
    return sparse.coo_matrix(
        (np.ones(MEDIATOR_DIMENSION), (rows, columns)),
        shape=(MEDIATOR_DIMENSION, MEDIATOR_DIMENSION),
    ).tocsr()


Mode = tuple[tuple[int, int, int], int]


def face_key(key: Mode) -> Mode:
    cell, slot = key
    if slot == PARKED:
        return key
    direction = slot - 1
    target = tuple(
        int(cell[axis] + c210.DIRECTIONS[direction, axis]) for axis in range(3)
    )
    return target, 1 + REVERSE[direction]


def reversal_key(key: Mode) -> Mode:
    cell, slot = key
    return key if slot == PARKED else (cell, 1 + REVERSE[slot - 1])


def stream_key(key: Mode) -> Mode:
    """The fixed physical word J S_face, with S_face acting first."""
    return reversal_key(face_key(key))


def inverse_stream_key(key: Mode) -> Mode:
    cell, slot = key
    if slot == PARKED:
        return key
    direction = slot - 1
    target = tuple(
        int(cell[axis] - c210.DIRECTIONS[direction, axis]) for axis in range(3)
    )
    return target, slot


def frame_key(key: Mode, frame: np.ndarray) -> Mode:
    cell, slot = key
    moved_cell = tuple(int(value) for value in frame @ np.asarray(cell, dtype=int))
    return moved_cell, slot if slot == PARKED else 1 + direction_map(frame)[slot - 1]


def canonical_configuration(keys: tuple[Mode, ...] | list[Mode]) -> tuple[Mode, ...]:
    if any(slot < PARKED or slot > 6 for _cell, slot in keys):
        raise ValueError("mediator slot must be parked or one of six directions")
    if len(set(keys)) != len(keys):
        raise ValueError("duplicate hard-core mediator occupation")
    if len(keys) > ROUTE_C_MAX_LOCAL_Q:
        raise ValueError("a Route-C global-Q6 state cannot contain seven local occupations")
    return tuple(sorted(keys))


def stream_configuration(configuration: tuple[Mode, ...]) -> tuple[Mode, ...]:
    return canonical_configuration([stream_key(key) for key in configuration])


def inverse_stream_configuration(configuration: tuple[Mode, ...]) -> tuple[Mode, ...]:
    return canonical_configuration([inverse_stream_key(key) for key in configuration])


def frame_configuration(configuration: tuple[Mode, ...], frame: np.ndarray) -> tuple[Mode, ...]:
    return canonical_configuration([frame_key(key, frame) for key in configuration])


def stream_and_frame_controls() -> dict:
    seed_keys: tuple[Mode, ...] = tuple(
        ((cell, 0, 0), slot)
        for cell in (-1, 0, 1)
        for slot in (PARKED, 1, 2, 3)
    )
    configurations = [tuple()]
    for number in range(1, ROUTE_C_MAX_LOCAL_Q + 1):
        configurations.extend(tuple(row) for row in combinations(seed_keys, number))

    mapping_residual = 0
    inverse_failures = 0
    covariance_failures = 0
    charge_failures = 0
    for configuration in configurations:
        streamed = stream_configuration(configuration)
        inverse_failures += inverse_stream_configuration(streamed) != configuration
        charge_failures += len(streamed) != len(configuration)
        for key in configuration:
            cell, slot = key
            if slot == PARKED:
                direct = key
            else:
                direction = slot - 1
                direct = (
                    tuple(
                        int(cell[axis] + c210.DIRECTIONS[direction, axis])
                        for axis in range(3)
                    ),
                    slot,
                )
            mapping_residual += stream_key(key) != direct
        for frame in c210.proper_cubic_frames():
            left = frame_configuration(streamed, frame)
            right = stream_configuration(frame_configuration(configuration, frame))
            covariance_failures += left != right
    return {
        "configurations": len(configurations),
        "moving_stream_mapping_failures": mapping_residual,
        "inverse_failures": inverse_failures,
        "charge_failures": charge_failures,
        "all24_covariance_failures": covariance_failures,
    }


def representation_group_law_controls() -> dict:
    frames = c210.proper_cubic_frames()
    matter_failures = 0
    mediator_failures = 0
    for first in frames:
        for second in frames:
            composed = second @ first
            for mask in range(MATTER_DIMENSION):
                once, sign_once = transform_matter(mask, first)
                twice, sign_twice = transform_matter(once, second)
                direct, sign_direct = transform_matter(mask, composed)
                matter_failures += twice != direct or sign_once * sign_twice != sign_direct
            for mask in range(MEDIATOR_DIMENSION):
                twice = transform_mediator(transform_mediator(mask, first), second)
                direct = transform_mediator(mask, composed)
                mediator_failures += twice != direct
    return {
        "frame_products": len(frames) ** 2,
        "matter_exterior_group_law_failures": matter_failures,
        "mediator_qubit_group_law_failures": mediator_failures,
    }


def hard_core_statistics_discriminator() -> dict:
    ordinary_swap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
        dtype=complex,
    )
    fermionic_swap = ordinary_swap.copy()
    fermionic_swap[3, 3] = -1
    return {
        "supplied_candidate_statistics": STATISTICS_LAW,
        "ordinary_SWAP_on_11": float(ordinary_swap[3, 3].real),
        "fermionic_FSWAP_on_11": float(fermionic_swap[3, 3].real),
        "operator_distance": float(np.linalg.norm(ordinary_swap - fermionic_swap)),
        "Q1_restriction_can_select_statistics": False,
        "live_alternative": LIVE_STATISTICS_ALTERNATIVE,
    }


def preservation_controls(generator: sparse.csr_matrix) -> dict:
    contact_number = np.asarray([mask.bit_count() for mask in range(MATTER_DIMENSION)])
    contact = np.exp(1j * c230.COUPLING * contact_number * (contact_number - 1) / 2)
    contact_one_particle = float(np.max(abs(contact[contact_number <= 1] - 1)))

    q0_columns = np.asarray(
        [local_index(matter, 0) for matter in range(MATTER_DIMENSION)], dtype=int
    )
    collision_q0 = float(sparse.linalg.norm(generator[:, q0_columns]))

    mass_rows = []
    mass_residual = 0.0
    coin_unitarity = 0.0
    coin_covariance = 0.0
    for beta in TRAIN_BETAS:
        species = c219.common_species(beta)
        rest = c219.rest_mass(species)
        residual = abs(rest - species.analytic_mass)
        mass_residual = max(mass_residual, residual)
        coin_unitarity = max(
            coin_unitarity,
            float(np.linalg.norm(species.coin.conj().T @ species.coin - np.eye(6))),
        )
        for frame in c210.proper_cubic_frames():
            representation = c210.direction_permutation(frame)
            coin_covariance = max(
                coin_covariance,
                float(np.linalg.norm(representation @ species.coin @ representation.T - species.coin)),
            )
        mass_rows.append(
            {
                "beta": float(beta),
                "analytic_mass": float(species.analytic_mass),
                "rest_mass": float(rest),
                "residual": float(residual),
            }
        )
    return {
        "contact_identity_N_le_1": contact_one_particle,
        "collision_identity_Q_0_generator_residual": collision_q0,
        "safe_train_one_particle_mass_maximum_residual": mass_residual,
        "safe_train_coin_unitarity_maximum": coin_unitarity,
        "safe_train_coin_all24_covariance_maximum": coin_covariance,
        "mass_rows": mass_rows,
        "held_or_principal_mass_claim": False,
    }


def local_code_shell_lift_controls(generator: sparse.csr_matrix) -> dict:
    """Witness the collision's formal conjugation lift on one seeded code ray."""
    code = c315.c269.build_code(3)
    encoder = c311.common_encoder(code)
    _basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    constrained = c311.constrained_encoding(flagged, exchange)
    matter_encoding = constrained @ c311.fock_input_embedding()
    constraint = c311.role_constraint(exchange)

    gram_residual = float(
        np.linalg.norm(
            matter_encoding.conj().T @ matter_encoding
            - np.eye(MATTER_DIMENSION)
        )
    )
    constraint_residual = float(
        np.linalg.norm(constraint @ matter_encoding - matter_encoding)
    )

    rng = np.random.default_rng(510311)
    logical = rng.normal(size=LOCAL_DIMENSION) + 1j * rng.normal(
        size=LOCAL_DIMENSION
    )
    logical /= np.linalg.norm(logical)
    logical_forward = expm_multiply(1j * TEST_ANGLE * generator, logical)
    logical_restored = expm_multiply(
        -1j * TEST_ANGLE * generator, logical_forward
    )

    physical_input = matter_encoding @ logical.reshape(
        MATTER_DIMENSION, MEDIATOR_DIMENSION
    )
    decoded = matter_encoding.conj().T @ physical_input
    physical_forward = matter_encoding @ expm_multiply(
        1j * TEST_ANGLE * generator, decoded.reshape(-1)
    ).reshape(MATTER_DIMENSION, MEDIATOR_DIMENSION)
    expected_forward = matter_encoding @ logical_forward.reshape(
        MATTER_DIMENSION, MEDIATOR_DIMENSION
    )
    restored_decoded = matter_encoding.conj().T @ physical_forward
    physical_restored = matter_encoding @ expm_multiply(
        -1j * TEST_ANGLE * generator, restored_decoded.reshape(-1)
    ).reshape(MATTER_DIMENSION, MEDIATOR_DIMENSION)

    return {
        "matter_encoding_shape": list(matter_encoding.shape),
        "receiver_logical_dimension": LOCAL_DIMENSION,
        "receiver_physical_shell_by_mediator_shape": [
            matter_encoding.shape[0], MEDIATOR_DIMENSION
        ],
        "matter_Gram_residual": gram_residual,
        "constraint_eigen_residual": constraint_residual,
        "forward_intertwiner_residual": float(
            np.linalg.norm(physical_forward - expected_forward)
        ),
        "adjoint_inverse_residual": float(
            np.linalg.norm(physical_restored - physical_input)
        ),
        "logical_adjoint_inverse_residual": float(
            np.linalg.norm(logical_restored - logical)
        ),
        "physical_constraint_residual_after": float(
            np.linalg.norm(constraint @ physical_forward - physical_forward)
        ),
        "formal_off_code_completion": "identity on the orthogonal local shell",
        "formal_shell_formula": "(E tensor I) U (E tensor I)^dagger + I - (E tensor I)(E tensor I)^dagger",
        "witness_scope": "one deterministic seeded on-code ray for the collision factor",
        "operator_wide_off_code_execution": False,
        "raw_M2_ambient_unitary_execution": False,
        "physical_frame_encoding_covariance_execution": False,
        "combined_emitter_stream_collision_lift_execution": False,
    }


def deletion_and_domain_controls() -> dict:
    identity_emitter = emitter_matrix(0, 0.0)
    identity = sparse.eye(MEDIATOR_DIMENSION, format="csr", dtype=complex)
    rejection_count = 0
    for invalid in (
        [((0, 0, 0), 1), ((0, 0, 0), 1)],
        [((0, 0, 0), 7)],
        [((0, 0, 0), slot) for slot in range(7)],
    ):
        try:
            canonical_configuration(invalid)
        except ValueError:
            rejection_count += 1
    return {
        "emitter_deletion_identity_residual": float(sparse.linalg.norm(identity_emitter - identity)),
        "declared_not_dynamically_measured_zero_parameter_semantics": (
            "collision angle zero means identity",
            "mediator stream deletion means identity",
            "contact coupling g zero means identity",
            "probe coin deletion means identity",
            "source factor deletion replaces Mplus by one",
            "probe factor deletion replaces Mplus by one",
        ),
        "deletion_effect_distances_executed": 0,
        "invalid_domains_rejected": rejection_count,
        "invalid_domains_expected": 3,
    }


def physical_inventory() -> dict:
    code = c315.c269.build_code(3)
    route_c_n_le_2_labels = c315.joint_labels(2)
    route_c_exact_n2_labels = tuple(
        label for label in route_c_n_le_2_labels
        if label[0] + label[2] == 2
    )
    inherited = c315.physical_support_and_constraint_controls(
        code, route_c_n_le_2_labels
    )
    return {
        "Cycle311_local_M64_dimension": c311.FOCK_DIMENSION,
        "Cycle311_installed_M2_per_cell": 23,
        "Cycle315_route_C_N_le_2_joint_logical_columns": len(
            route_c_n_le_2_labels
        ),
        "Cycle315_route_C_exact_N2_joint_logical_columns": len(
            route_c_exact_n2_labels
        ),
        "Cycle315_N_le_2_support": inherited,
        "mediator_M2_per_cell": 7,
        "single_cell_receiver_M2": 30,
        "homogeneous_matter_plus_mediator_M2_per_cell": inherited[
            "installed_M2_per_cell_including_three_undirected_edge_roles"
        ]
        + 7,
        "two_cell_patch_union_plus_mediator_M2": inherited[
            "total_patch_union_with_edge_role_gauge"
        ]
        + 14,
        "local_collision_code_dimension_full_M64_times_2pow7": LOCAL_DIMENSION,
        "Cycle419_15D_tensor_Cycle315_4096D": 15 * 4096,
        "Cycle419_15D_join_is_only_Q_le_1": True,
        "full_two_block_mediator_qubit_occupation_dimension": 2**14,
        "two_block_mediator_q_le_6_dimension": sum(
            comb(14, number) for number in range(7)
        ),
        "two_block_mediator_exact_global_Q6_dimension": comb(14, 6),
        "locally_enforced_constraints": (
            "Cycle311 fixed-Wilson/cell-role constraints",
            "Cycle315 C_edge on one active matter edge",
        ),
        "literal_nonauxiliary_mediator_structure": (
            "seven independent two-level M2 occupations; no added gauge constraint"
        ),
        "global_multi_edge_intertwiner_claim": False,
    }


def main() -> int:
    started = time.monotonic()
    generator, entries, axis_matrices = collision_generator()
    hermiticity = float(sparse.linalg.norm(generator - generator.conj().T))
    check("summed collision generator Hermitian", hermiticity < NUMERIC_TOLERANCE, hermiticity)

    transition_charge_failures = 0
    transition_lawfulness_failures = 0
    for (target, source), amplitude in entries.items():
        target_matter, target_mediator = local_decode(target)
        source_matter, source_mediator = local_decode(source)
        transition_charge_failures += (
            not amplitude
            or target_matter.bit_count() != source_matter.bit_count()
            or target_mediator.bit_count() != source_mediator.bit_count()
        )
        transition_lawfulness_failures += (
            abs(abs(amplitude) - 1) > NUMERIC_TOLERANCE
            or (target_matter ^ source_matter).bit_count() != 2
            or (target_mediator ^ source_mediator).bit_count() != 2
            or (target_mediator & 1) != (source_mediator & 1)
        )
    check("collision preserves matter and mediator charge", transition_charge_failures == 0, transition_charge_failures)
    check(
        "collision transitions are CAR/Pauli/hard-core lawful",
        transition_lawfulness_failures == 0,
        transition_lawfulness_failures,
    )

    q1_residual, q1_exponential_residual, q1_nnz = cycle501_q1_n2_residual(entries)
    check("N2 Q1 projection equals Cycle501", q1_residual < NUMERIC_TOLERANCE, q1_residual)
    check(
        "N2 Q1 exponential equals Cycle501 explicit collision",
        q1_exponential_residual < NUMERIC_TOLERANCE,
        q1_exponential_residual,
    )

    sector_controls = collision_sector_controls(generator, axis_matrices)
    check(
        "collision Q0-through-Q6 sector oracle and commuting axis blocks",
        sector_controls["Q_0_through_6_dimensions"]
        == [64, 448, 1344, 2240, 2240, 1344, 448]
        and sector_controls["Q_0_through_6_generator_nnz"]
        == [0, 96, 480, 960, 960, 480, 96]
        and sector_controls["Q_0_through_6_total_dimension"] == 8128
        and sector_controls["Q_0_through_6_total_nnz"] == 3072
        and sector_controls["maximum_axis_block_commutator"] < NUMERIC_TOLERANCE,
        sector_controls,
    )

    covariance = collision_covariance(entries)
    check("collision generator all24 covariant", covariance < NUMERIC_TOLERANCE, covariance)

    rng = np.random.default_rng(510)
    vector = rng.normal(size=LOCAL_DIMENSION) + 1j * rng.normal(size=LOCAL_DIMENSION)
    vector /= np.linalg.norm(vector)
    forward = expm_multiply(1j * TEST_ANGLE * generator, vector)
    restored = expm_multiply(-1j * TEST_ANGLE * generator, forward)
    inverse = float(np.linalg.norm(restored - vector))
    norm = float(abs(np.linalg.norm(forward) - 1))
    check("summed exponential inverse", inverse < INVERSE_TOLERANCE, inverse)
    check("summed exponential norm", norm < INVERSE_TOLERANCE, norm)

    emitters = tuple(
        emitter_matrix(direction, TEST_ANGLE) for direction in range(6)
    )
    emitter_unitarity = max(
        float(sparse.linalg.norm(unitary.conj().T @ unitary - sparse.eye(MEDIATOR_DIMENSION)))
        for unitary in emitters
    )
    emitter_inverse = max(
        float(sparse.linalg.norm(emitter_matrix(direction, -TEST_ANGLE) @ emitters[direction] - sparse.eye(MEDIATOR_DIMENSION)))
        for direction in range(6)
    )
    emitter_covariance = 0.0
    for frame in c210.proper_cubic_frames():
        representation = mediator_frame_matrix(frame)
        mapping = direction_map(frame)
        for direction in range(6):
            emitter_covariance = max(
                emitter_covariance,
                float(sparse.linalg.norm(
                    representation @ emitters[direction] @ representation.T
                    - emitters[mapping[direction]]
                )),
            )
    check("directional emitter unitary/inverse", max(emitter_unitarity, emitter_inverse) < NUMERIC_TOLERANCE, max(emitter_unitarity, emitter_inverse))
    check("directional emitter all24 carried", emitter_covariance < NUMERIC_TOLERANCE, emitter_covariance)

    stream_controls = stream_and_frame_controls()
    check("full occupation moving stream exact", not any(
        stream_controls[key]
        for key in (
            "moving_stream_mapping_failures", "inverse_failures", "charge_failures", "all24_covariance_failures"
        )
    ), stream_controls)

    group = representation_group_law_controls()
    check("all 576 proper-cubic representation products", group["matter_exterior_group_law_failures"] == 0 and group["mediator_qubit_group_law_failures"] == 0, group)

    statistics = hard_core_statistics_discriminator()
    check("hard-core qubit SWAP discriminator", statistics["ordinary_SWAP_on_11"] == 1 and statistics["fermionic_FSWAP_on_11"] == -1 and statistics["operator_distance"] == 2, statistics)

    preservation = preservation_controls(generator)
    check("analytic one-particle/contact/Q0 fixtures", max(
        preservation["contact_identity_N_le_1"],
        preservation["collision_identity_Q_0_generator_residual"],
        preservation["safe_train_one_particle_mass_maximum_residual"],
        preservation["safe_train_coin_unitarity_maximum"],
        preservation["safe_train_coin_all24_covariance_maximum"],
    ) < NUMERIC_TOLERANCE, preservation)

    local_shell_lift = local_code_shell_lift_controls(generator)
    check(
        "formal Cycle311 collision code-shell lift witness",
        max(
            local_shell_lift["matter_Gram_residual"],
            local_shell_lift["constraint_eigen_residual"],
            local_shell_lift["forward_intertwiner_residual"],
            local_shell_lift["adjoint_inverse_residual"],
            local_shell_lift["logical_adjoint_inverse_residual"],
            local_shell_lift["physical_constraint_residual_after"],
        ) < INVERSE_TOLERANCE,
        local_shell_lift,
    )

    deletions = deletion_and_domain_controls()
    check("zero-angle emitter and local-domain rejection", deletions["emitter_deletion_identity_residual"] < NUMERIC_TOLERANCE and deletions["invalid_domains_rejected"] == deletions["invalid_domains_expected"], deletions)

    inventory = physical_inventory()
    support = inventory["Cycle315_N_le_2_support"]
    check("Cycle311/315 physical support and constraints", (
        inventory["Cycle311_local_M64_dimension"] == 64
        and support["total_patch_union_with_edge_role_gauge"] == 83
        and support["installed_M2_per_cell_including_three_undirected_edge_roles"] == 29
        and support["port_constraint_commutator_failures"] == 0
        and support["fixed_sector_commutator_failures"] == 0
        and inventory["homogeneous_matter_plus_mediator_M2_per_cell"] == 36
        and inventory["two_cell_patch_union_plus_mediator_M2"] == 97
        and inventory["Cycle315_route_C_N_le_2_joint_logical_columns"] == 79
        and inventory["Cycle315_route_C_exact_N2_joint_logical_columns"] == 66
        and inventory["two_block_mediator_q_le_6_dimension"] == 6476
        and inventory["two_block_mediator_exact_global_Q6_dimension"] == 3003
    ), inventory)

    elapsed = time.monotonic() - started
    peak_rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    passed = all(row.passed for row in RESULTS)
    output = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "status": "local-pre-response-certificate" if passed else "local-certificate-failed",
        "pass": passed,
        "tests_passed": sum(row.passed for row in RESULTS),
        "tests_total": len(RESULTS),
        "tests": [row.__dict__ for row in RESULTS],
        "statistics_discriminator": statistics,
        "local_alphabet": {
            "matter": "full six-mode CAR M64",
            "mediator": "seven literal M2 hard-core qubit/spin occupations",
            "full_dimension": LOCAL_DIMENSION,
            "Route_C_local_charge_sectors": "Q=0..6; Q=7 physical but outside global-Q6 code",
        },
        "collision": {
            "generator_nnz": generator.nnz,
            "Hermiticity_residual": hermiticity,
            "charge_transition_failures": transition_charge_failures,
            "lawful_transition_failures": transition_lawfulness_failures,
            "N2_Q1_Cycle501_residual": q1_residual,
            "N2_Q1_Cycle501_exponential_residual": q1_exponential_residual,
            "N2_Q1_Cycle501_nnz": q1_nnz,
            "all24_covariance_residual": covariance,
            "inverse_residual": inverse,
            "norm_residual": norm,
            "one_exponential_of_summed_generator": True,
            "numeric_test_angle": TEST_ANGLE,
            "Cycle501_seam_angle": CYCLE501_SEAM_ANGLE,
            "sector_oracle": sector_controls,
        },
        "emitter": {
            "unitarity_residual": emitter_unitarity,
            "inverse_residual": emitter_inverse,
            "all24_covariance_residual": emitter_covariance,
        },
        "stream": stream_controls,
        "proper_cubic_group": group,
        "preservation": preservation,
        "local_code_shell_lift": local_shell_lift,
        "deletions_and_domain": deletions,
        "physical_inventory": inventory,
        "dependencies": {str(path.relative_to(ROOT)): file_sha(path) for path in DEPENDENCIES},
        "resources": {
            "wall_seconds": elapsed,
            "peak_rss_native_units": peak_rss,
            "response_rows": 0,
            "held_rows": 0,
        },
        "exact_limitations": (
            "hard-core qubit/spin mediator statistics is supplied, not selected by Q1",
            "fermionic FSWAP statistics remains a live untested Route-C alternative",
            "Cycle419 15D vacuum-plus-Q1 code is only a receiving-interface predecessor",
            "Cycle315 shared-cell multi-edge constraint compatibility and global E remain open",
            "only the collision has a formal Cycle311-shell lift on one seeded code ray",
            "combined update, operator-wide off-code execution, physical-frame encoding covariance, and raw-M2 ambient unitary remain open",
            "dense physical primitive synthesis and autonomous preparation remain supplied",
            "finite boundary, octahedral global-Q6 apparatus, leakage, response, and held execution remain open",
            "no response, held, source normalization, time, energy, stress, gravity, or Born claim",
        ),
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
