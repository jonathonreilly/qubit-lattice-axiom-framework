#!/usr/bin/env python3
"""Cycle 309: primitive local synthesis of the Cycle-306 comparator.

Three explicit finite grammars are compared on the accepted Cycle-306 code:

1. direct QR/two-level gates on the 180 local face/tag/flag/r sectors;
2. two-level gates lifted from the 42-dimensional C_role=+1 code; and
3. proper-cubic spectral-projector layers on that same gauge code.

The local operations are built only from the Pauli-transition, tag-projector,
and matrix-unit grammar already executed in Cycles 302, 304, and 306.  A
finite layer list is a compiler schedule.  It is not a clock or an autonomous
update law.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import re
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17 as c304
import physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17 as c302
import physical_cycle269_relational_role_marker_gauge_cycle306_2026_07_17 as c306


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_PRIMITIVE_MATRIX_UNIT_SYNTHESIS_CYCLE309_NOTE_2026-07-17.md"
)
TRAINING_SIZE = 3
HELD_SIZE = 6
TOLERANCE = 2e-10
MICRO_DIMENSION = 180
LOGICAL_DIMENSION = 42
SPECTRAL_CLUSTER_TOLERANCE = 2e-8
MAXIMUM_WITHIN_CLUSTER_TOLERANCE_RATIO = 1e-5
MINIMUM_INTER_CLUSTER_TOLERANCE_RATIO = 1e4

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Rotation:
    left: int
    right: int
    elimination: np.ndarray


@dataclass(frozen=True)
class QRFactorization:
    rotations: tuple[Rotation, ...]
    diagonal: np.ndarray
    triangular_residual: float


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-309 note exists", False, NOTE)
        return
    body = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "direct conditional-pauli",
        "local gauge-generator",
        "finite covariant spectral layers",
        "complete logical update",
        "ninety commuting swaps",
        "exact on the cycle-306 code",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "twenty-three m2 per cell",
        "forty-four-m2 patch",
        "host schedule",
        "not physical time",
        "not an autonomous law",
        "spectral clustering uses the supplied numerical tolerance 2e-8",
        "maximum within-group eigenvalue spread",
        "minimum inter-eigenspace gap",
        "separate synced born pr",
        "33% | 14% | 82% | 1.8/5",
        "broad gate status: fail / do not ship",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in body)
    check("the note pins the primitive-synthesis theorem and boundary", not missing, missing)


def qr_factorization(unitary: np.ndarray, tolerance: float = 2e-12) -> QRFactorization:
    if unitary.ndim != 2 or unitary.shape[0] != unitary.shape[1]:
        raise ValueError("two-level synthesis requires a square matrix")
    dimension = unitary.shape[0]
    if np.linalg.norm(unitary.conj().T @ unitary - np.eye(dimension)) > 1e-8:
        raise ValueError("two-level synthesis requires a unitary matrix")
    work = unitary.astype(complex).copy()
    rotations: list[Rotation] = []
    for column in range(dimension - 1):
        for row in range(dimension - 1, column, -1):
            a, b = work[row - 1, column], work[row, column]
            if abs(b) <= tolerance:
                continue
            radius = float(np.sqrt(abs(a) ** 2 + abs(b) ** 2))
            elimination = np.asarray(
                (
                    (np.conj(a) / radius, np.conj(b) / radius),
                    (-b / radius, a / radius),
                ),
                dtype=complex,
            )
            work[[row - 1, row], :] = elimination @ work[[row - 1, row], :]
            rotations.append(Rotation(row - 1, row, elimination))
    diagonal = np.diag(work).copy()
    residual = float(np.linalg.norm(work - np.diag(diagonal)))
    return QRFactorization(tuple(rotations), diagonal, residual)


def reconstruct_qr(
    factorization: QRFactorization,
    skip_rotation: int | None = None,
    skip_phase: int | None = None,
) -> np.ndarray:
    diagonal = factorization.diagonal.copy()
    if skip_phase is not None:
        diagonal[skip_phase] = 1
    result = np.diag(diagonal)
    for index in range(len(factorization.rotations) - 1, -1, -1):
        if index == skip_rotation:
            continue
        rotation = factorization.rotations[index]
        result[[rotation.left, rotation.right], :] = (
            rotation.elimination.conj().T
            @ result[[rotation.left, rotation.right], :]
        )
    return result


def delta_for_two_level(left: int, right: int, block: np.ndarray) -> dict[tuple[int, int], complex]:
    delta: dict[tuple[int, int], complex] = {}
    for row_index, row in enumerate((left, right)):
        for column_index, column in enumerate((left, right)):
            value = block[row_index, column_index] - (row_index == column_index)
            if abs(value) > 1e-13:
                delta[(row, column)] = complex(value)
    return delta


def delta_for_phase(index: int, phase: complex) -> dict[tuple[int, int], complex]:
    return {} if abs(phase - 1) <= 1e-13 else {(index, index): complex(phase - 1)}


def primitive_deltas(factorization: QRFactorization) -> tuple[dict[tuple[int, int], complex], ...]:
    result = [
        delta_for_two_level(
            rotation.left, rotation.right, rotation.elimination.conj().T
        )
        for rotation in factorization.rotations
    ]
    result.extend(
        delta_for_phase(index, phase)
        for index, phase in enumerate(factorization.diagonal)
        if abs(phase - 1) > 1e-12
    )
    return tuple(result)


def signed_permutation(matrix: np.ndarray) -> tuple[tuple[int, ...], tuple[complex, ...]]:
    mapping = []
    signs = []
    for source in range(matrix.shape[1]):
        targets = np.where(abs(matrix[:, source]) > 0.5)[0]
        if len(targets) != 1:
            raise ValueError("representation must be a signed permutation")
        target = int(targets[0])
        mapping.append(target)
        signs.append(complex(matrix[target, source]))
    return tuple(mapping), tuple(signs)


def transformed_delta(
    delta: dict[tuple[int, int], complex],
    mapping: tuple[int, ...],
    signs: tuple[complex, ...],
) -> dict[tuple[int, int], complex]:
    transformed: dict[tuple[int, int], complex] = {}
    for (row, column), value in delta.items():
        key = (mapping[row], mapping[column])
        transformed[key] = transformed.get(key, 0) + signs[row] * np.conj(signs[column]) * value
    return {key: value for key, value in transformed.items() if abs(value) > 1e-12}


def sparse_residual(
    left: dict[tuple[int, int], complex], right: dict[tuple[int, int], complex]
) -> float:
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0) - right.get(key, 0)) ** 2 for key in keys)))


def frame_permutations() -> tuple[
    tuple[tuple[tuple[int, ...], tuple[complex, ...]], ...],
    tuple[tuple[tuple[int, ...], tuple[complex, ...]], ...],
]:
    physical = []
    logical = []
    for frame in c235.proper_cubic_frames():
        logical_r, micro_r = c304.frame_representations(frame)
        physical_r = c306.block_diagonal(micro_r, micro_r)
        physical.append(signed_permutation(physical_r))
        logical.append(signed_permutation(logical_r))
    return tuple(physical), tuple(logical)


def covariance_census(
    deltas: tuple[dict[tuple[int, int], complex], ...],
    representations: tuple[tuple[tuple[int, ...], tuple[complex, ...]], ...],
) -> tuple[int, float]:
    all_frame = 0
    maximum = 0.0
    for delta in deltas:
        residuals = [
            sparse_residual(delta, transformed_delta(delta, mapping, signs))
            for mapping, signs in representations
        ]
        maximum = max(maximum, max(residuals, default=0.0))
        all_frame += max(residuals, default=0.0) < 1e-11
    return all_frame, maximum


def permutation_from_operator(operator: np.ndarray) -> tuple[int, ...]:
    result = []
    for source in range(operator.shape[1]):
        targets = np.where(abs(operator[:, source]) > 0.5)[0]
        if len(targets) != 1:
            raise ValueError("operator is not a permutation")
        result.append(int(targets[0]))
    return tuple(result)


def constraint_commutator_residual(
    delta: dict[tuple[int, int], complex], constraint_permutation: tuple[int, ...]
) -> float:
    transformed = {
        (constraint_permutation[row], constraint_permutation[column]): value
        for (row, column), value in delta.items()
    }
    return sparse_residual(delta, transformed)


def direct_conditional_pauli_controls(physical_frames) -> dict[str, object]:
    _old, _logical, physical = c306.old_and_new_operators(-0.3)
    constraint = c306.role_constraint()
    constraint_permutation = permutation_from_operator(constraint)
    counts = {}
    reconstruction = {}
    leaking = {}
    covariant = {}
    maximum_constraint = 0.0
    maximum_frame = 0.0
    used_pairs: set[tuple[int, int]] = set()
    factorizations = {}
    for name, operator in physical.items():
        factorization = qr_factorization(operator)
        factorizations[name] = factorization
        reconstructed = reconstruct_qr(factorization)
        deltas = primitive_deltas(factorization)
        phase_count = sum(abs(value - 1) > 1e-12 for value in factorization.diagonal)
        counts[name] = (len(factorization.rotations), int(phase_count))
        reconstruction[name] = float(np.linalg.norm(reconstructed - operator))
        commutators = [
            constraint_commutator_residual(delta, constraint_permutation)
            for delta in deltas
        ]
        leaking[name] = sum(value > 1e-11 for value in commutators)
        maximum_constraint = max(maximum_constraint, max(commutators, default=0.0))
        covariant[name], frame_residual = covariance_census(deltas, physical_frames)
        maximum_frame = max(maximum_frame, frame_residual)
        used_pairs.update(
            tuple(sorted((rotation.left, rotation.right)))
            for rotation in factorization.rotations
        )
    final_constraint = max(
        float(np.linalg.norm(constraint @ operator - operator @ constraint))
        for operator in physical.values()
    )
    check(
        "direct conditional-Pauli QR exactly synthesizes the full 180-sector completions but its ordered primitives leave C_role",
        counts == {
            "coin": (312, 8),
            "stream": (2250, 90),
            "contact": (0, 30),
        }
        and max(reconstruction.values()) < TOLERANCE
        and all(leaking[name] > 0 for name in leaking)
        and all(covariant[name] < sum(counts[name]) for name in covariant)
        and maximum_constraint > 0.1
        and maximum_frame > 0.1
        and final_constraint < TOLERANCE,
        {
            "two_level_and_phase_counts": counts,
            "total_primitives": sum(sum(row) for row in counts.values()),
            "reconstruction_residuals": reconstruction,
            "C_role_noncommuting_primitives": leaking,
            "all_frame_covariant_primitives": covariant,
            "maximum_primitive_constraint_commutator": maximum_constraint,
            "maximum_primitive_frame_residual": maximum_frame,
            "final_target_constraint_commutator": final_constraint,
            "host_order": "reverse lexicographic QR elimination",
        },
    )
    return {
        "pairs": used_pairs,
        "factorizations": factorizations,
        "counts": counts,
        "reconstruction": reconstruction,
    }


def constraint_swap_controls(physical_frames) -> dict[str, object]:
    constraint = c306.role_constraint()
    permutation = permutation_from_operator(constraint)
    pairs = tuple((index, target) for index, target in enumerate(permutation) if index < target)
    product_operator = np.eye(MICRO_DIMENSION, dtype=complex)
    deltas = []
    for left, right in pairs:
        product_operator[[left, right], :] = product_operator[[right, left], :]
        deltas.append(delta_for_two_level(left, right, np.asarray(((0, 1), (1, 0)))))
    pair_commutators = [constraint_commutator_residual(delta, permutation) for delta in deltas]
    pair_overlaps = sum(
        bool(set(left) & set(right))
        for index, left in enumerate(pairs)
        for right in pairs[index + 1 :]
    )
    all_frame, maximum_frame = covariance_census(tuple(deltas), physical_frames)
    full_frame = max(
        float(np.linalg.norm(rep @ constraint - constraint @ rep))
        for frame in c235.proper_cubic_frames()
        for _logical, micro in (c304.frame_representations(frame),)
        for rep in (c306.block_diagonal(micro, micro),)
    )
    encoding = c306.constrained_encoding()
    deletion_residuals = []
    syndrome_residuals = []
    for left, right in pairs:
        deleted = constraint.copy()
        deleted[[left, right], :] = deleted[[right, left], :]
        deletion_residuals.append(float(np.linalg.norm((deleted - constraint) @ encoding, 2)))
        negative = np.zeros(180, dtype=complex)
        negative[left], negative[right] = 1 / np.sqrt(2), -1 / np.sqrt(2)
        syndrome_residuals.append(float(np.linalg.norm((deleted - constraint) @ negative)))
    check(
        "K_exchange X_r is the unordered product of ninety commuting disjoint local conditional swaps",
        len(pairs) == 90
        and pair_overlaps == 0
        and np.linalg.norm(product_operator - constraint) == 0
        and max(pair_commutators) == 0
        and all_frame < len(pairs)
        and maximum_frame > 0
        and full_frame < TOLERANCE
        and max(deletion_residuals) == 0
        and min(syndrome_residuals) > 1.99,
        {
            "commuting_swap_factors": len(pairs),
            "pair_support_overlaps": pair_overlaps,
            "product_residual": float(np.linalg.norm(product_operator - constraint)),
            "maximum_factor_constraint_commutator": max(pair_commutators),
            "individually_all_frame_factors": all_frame,
            "maximum_individual_frame_residual": maximum_frame,
            "unordered_full_product_frame_residual": full_frame,
            "maximum_one_factor_deletion_Cplus_code_residual": max(deletion_residuals),
            "minimum_one_factor_deletion_Cminus_syndrome_residual": min(syndrome_residuals),
        },
    )
    return {"pairs": set(pairs), "deltas": tuple(deltas)}


def raw_terms_for_logical_delta(delta: dict[tuple[int, int], complex]) -> np.ndarray:
    logical_delta = np.zeros((LOGICAL_DIMENSION, LOGICAL_DIMENSION), dtype=complex)
    for (row, column), value in delta.items():
        logical_delta[row, column] = value
    encoding = c306.constrained_encoding()
    return encoding @ logical_delta @ encoding.conj().T


def nonzero_pairs(matrix: np.ndarray, tolerance: float = 2e-12) -> set[tuple[int, int]]:
    rows, columns = np.where(abs(matrix) > tolerance)
    return set(zip(rows.tolist(), columns.tolist()))


def gauge_generator_controls(logical_frames) -> dict[str, object]:
    _old, logical, physical = c306.old_and_new_operators(-0.3)
    encoding = c306.constrained_encoding()
    constraint = c306.role_constraint()
    projector = encoding @ encoding.conj().T
    counts = {}
    reconstruction = {}
    covariant = {}
    maximum_frame = 0.0
    maximum_raw_terms = 0
    used_pairs: set[tuple[int, int]] = set()
    factorizations = {}
    maximum_logical_unitarity = 0.0
    for name, operator in logical.items():
        factorization = qr_factorization(operator)
        factorizations[name] = factorization
        reconstructed = reconstruct_qr(factorization)
        deltas = primitive_deltas(factorization)
        phase_count = sum(abs(value - 1) > 1e-12 for value in factorization.diagonal)
        counts[name] = (len(factorization.rotations), int(phase_count))
        reconstruction[name] = float(np.linalg.norm(reconstructed - operator))
        covariant[name], frame_residual = covariance_census(deltas, logical_frames)
        maximum_frame = max(maximum_frame, frame_residual)
        for delta in deltas:
            raw = raw_terms_for_logical_delta(delta)
            pairs = nonzero_pairs(raw)
            used_pairs.update(pairs)
            maximum_raw_terms = max(maximum_raw_terms, len(pairs))
            logical_gate = np.eye(LOGICAL_DIMENSION, dtype=complex)
            for (row, column), value in delta.items():
                logical_gate[row, column] += value
            maximum_logical_unitarity = max(
                maximum_logical_unitarity,
                float(np.linalg.norm(logical_gate.conj().T @ logical_gate - np.eye(42))),
            )
    code_residual = max(
        float(np.linalg.norm(encoding @ reconstruct_qr(factorizations[name]) - physical[name] @ encoding))
        for name in logical
    )
    base_constraint = float(np.linalg.norm(constraint @ encoding - encoding))
    base_projector = float(np.linalg.norm(projector - c306.constrained_projector()))
    check(
        "local gauge-generator QR gives a 379-primitive C_role-preserving synthesis exact on the Cycle-306 code",
        counts == {
            "coin": (78, 4),
            "stream": (261, 21),
            "contact": (0, 15),
        }
        and max(reconstruction.values()) < TOLERANCE
        and code_residual < TOLERANCE
        and base_constraint < TOLERANCE
        and base_projector < TOLERANCE
        and maximum_logical_unitarity < TOLERANCE
        and all(covariant[name] < sum(counts[name]) for name in covariant)
        and maximum_frame > 0.1
        and maximum_raw_terms <= 400,
        {
            "two_level_and_phase_counts": counts,
            "total_primitives": sum(sum(row) for row in counts.values()),
            "logical_reconstruction_residuals": reconstruction,
            "physical_code_action_residual": code_residual,
            "constraint_eigen_residual": base_constraint,
            "code_projector_residual": base_projector,
            "maximum_primitive_unitarity_residual": maximum_logical_unitarity,
            "all_frame_covariant_primitives": covariant,
            "maximum_primitive_frame_residual": maximum_frame,
            "maximum_raw_matrix_units_per_gauge_primitive": maximum_raw_terms,
            "host_order": "logical reverse lexicographic QR elimination",
        },
    )
    return {
        "pairs": used_pairs,
        "factorizations": factorizations,
        "counts": counts,
        "reconstruction": reconstruction,
    }


def clustered_eigenvalue_indices(
    eigenvalues: np.ndarray, tolerance: float
) -> tuple[tuple[int, ...], ...]:
    groups: list[list[int]] = []
    for index, eigenvalue in enumerate(eigenvalues):
        for group in groups:
            if abs(eigenvalue - eigenvalues[group[0]]) < tolerance:
                group.append(index)
                break
        else:
            groups.append([index])
    return tuple(tuple(group) for group in groups)


def spectral_separation_metrics(
    eigenvalues: np.ndarray, groups: tuple[tuple[int, ...], ...]
) -> tuple[float, float]:
    within_group_spread = 0.0
    inter_eigenspace_gap = float("inf")
    group_by_index = {
        index: group_index
        for group_index, group in enumerate(groups)
        for index in group
    }
    for left in range(len(eigenvalues)):
        for right in range(left + 1, len(eigenvalues)):
            distance = float(abs(eigenvalues[left] - eigenvalues[right]))
            if group_by_index[left] == group_by_index[right]:
                within_group_spread = max(within_group_spread, distance)
            else:
                inter_eigenspace_gap = min(inter_eigenspace_gap, distance)
    return within_group_spread, inter_eigenspace_gap


def spectral_layers_with_metrics(
    unitary: np.ndarray, tolerance: float = SPECTRAL_CLUSTER_TOLERANCE
) -> tuple[tuple[tuple[complex, np.ndarray, int], ...], float, float]:
    eigenvalues, eigenvectors = np.linalg.eig(unitary)
    groups = clustered_eigenvalue_indices(eigenvalues, tolerance)
    within_group_spread, inter_eigenspace_gap = spectral_separation_metrics(
        eigenvalues, groups
    )
    layers = []
    for group in groups:
        eigenvalue = sum(eigenvalues[index] for index in group) / len(group)
        eigenvalue /= abs(eigenvalue)
        basis, _ = np.linalg.qr(eigenvectors[:, group])
        projector = basis @ basis.conj().T
        layers.append((complex(eigenvalue), projector, len(group)))
    return tuple(layers), within_group_spread, inter_eigenspace_gap


def spectral_layers(
    unitary: np.ndarray, tolerance: float = SPECTRAL_CLUSTER_TOLERANCE
):
    layers, _within_group_spread, _inter_eigenspace_gap = spectral_layers_with_metrics(
        unitary, tolerance
    )
    return layers


def finite_spectral_layer_controls(logical_frames) -> dict[str, object]:
    encoding = c306.constrained_encoding()
    constraint = c306.role_constraint()
    code_projector = encoding @ encoding.conj().T
    all_pairs: set[tuple[int, int]] = set()
    beta_details = {}
    global_residual = 0.0
    global_projector = 0.0
    global_orthogonality = 0.0
    global_covariance = 0.0
    global_constraint = 0.0
    global_code_leakage = 0.0
    stable_counts = []
    layerwise_raw_terms = []
    deletion_residuals = []
    global_within_group_spread = 0.0
    global_inter_eigenspace_gap = float("inf")
    within_group_witness = None
    inter_eigenspace_witness = None
    for beta in (-0.2, -0.3, -0.4, -0.35):
        _old, logical, physical = c306.old_and_new_operators(beta)
        logical_targets = dict(logical)
        physical_targets = dict(physical)
        logical_targets["update"] = logical["contact"] @ logical["stream"] @ logical["coin"]
        physical_targets["update"] = physical["contact"] @ physical["stream"] @ physical["coin"]
        detail = {}
        products = {}
        for name, operator in logical_targets.items():
            layers, within_group_spread, inter_eigenspace_gap = (
                spectral_layers_with_metrics(operator)
            )
            if within_group_spread > global_within_group_spread:
                global_within_group_spread = within_group_spread
                within_group_witness = (beta, name)
            if inter_eigenspace_gap < global_inter_eigenspace_gap:
                global_inter_eigenspace_gap = inter_eigenspace_gap
                inter_eigenspace_witness = (beta, name)
            nontrivial = [row for row in layers if abs(row[0] - 1) > 1e-10]
            product_operator = np.eye(LOGICAL_DIMENSION, dtype=complex)
            for eigenvalue, projector, _multiplicity in nontrivial:
                factor = np.eye(LOGICAL_DIMENSION) + (eigenvalue - 1) * projector
                product_operator = product_operator @ factor
                projector_residual = float(np.linalg.norm(projector @ projector - projector))
                global_projector = max(global_projector, projector_residual)
                for other_value, other_projector, _ in layers:
                    if other_projector is projector:
                        continue
                    global_orthogonality = max(
                        global_orthogonality,
                        float(np.linalg.norm(projector @ other_projector)),
                    )
                for mapping, signs in logical_frames:
                    representation = np.zeros((42, 42), dtype=complex)
                    for source, target in enumerate(mapping):
                        representation[target, source] = signs[source]
                    global_covariance = max(
                        global_covariance,
                        float(np.linalg.norm(representation @ projector - projector @ representation)),
                    )
                physical_factor = np.eye(180) + encoding @ (factor - np.eye(42)) @ encoding.conj().T
                global_constraint = max(
                    global_constraint,
                    float(np.linalg.norm(constraint @ physical_factor - physical_factor @ constraint)),
                )
                global_code_leakage = max(
                    global_code_leakage,
                    float(np.linalg.norm((np.eye(180) - code_projector) @ physical_factor @ encoding)),
                )
                raw = encoding @ (factor - np.eye(42)) @ encoding.conj().T
                pairs = nonzero_pairs(raw)
                all_pairs.update(pairs)
                layerwise_raw_terms.append(len(pairs))
                deletion_residuals.append(float(np.linalg.norm((product_operator / 1) - operator)))
            residual = float(np.linalg.norm(product_operator - operator))
            global_residual = max(global_residual, residual)
            products[name] = product_operator
            detail[name] = {
                "distinct_eigenspaces": len(layers),
                "nontrivial_layers": len(nontrivial),
                "multiplicities": tuple(row[2] for row in layers),
                "reconstruction_residual": residual,
                "maximum_within_group_eigenvalue_spread": within_group_spread,
                "minimum_inter_eigenspace_gap": inter_eigenspace_gap,
            }
        counts = tuple(
            detail[name]["nontrivial_layers"]
            for name in ("coin", "stream", "contact", "update")
        )
        stable_counts.append(counts)
        staged_composition_residual = float(
            np.linalg.norm(
                encoding @ (products["contact"] @ products["stream"] @ products["coin"])
                - physical["contact"] @ physical["stream"] @ physical["coin"] @ encoding
            )
        )
        complete_update_residual = float(
            np.linalg.norm(
                encoding @ products["update"] - physical_targets["update"] @ encoding
            )
        )
        global_residual = max(
            global_residual, staged_composition_residual, complete_update_residual
        )
        detail["staged_composition_code_residual"] = staged_composition_residual
        detail["complete_update_code_residual"] = complete_update_residual
        beta_details[beta] = detail
    check(
        "finite covariant spectral layers give either ten staged layers or sixteen unordered layers for the complete logical update",
        set(stable_counts) == {(8, 1, 1, 16)}
        and global_residual < TOLERANCE
        and global_projector < TOLERANCE
        and global_orthogonality < TOLERANCE
        and global_covariance < TOLERANCE
        and global_constraint < TOLERANCE
        and global_code_leakage < TOLERANCE
        and max(layerwise_raw_terms) <= 32400
        and global_within_group_spread
        < SPECTRAL_CLUSTER_TOLERANCE * MAXIMUM_WITHIN_CLUSTER_TOLERANCE_RATIO
        and global_inter_eigenspace_gap
        > SPECTRAL_CLUSTER_TOLERANCE * MINIMUM_INTER_CLUSTER_TOLERANCE_RATIO,
        {
            "beta_details": beta_details,
            "nontrivial_coin_stream_contact_update_layers": stable_counts,
            "maximum_reconstruction_or_composition_residual": global_residual,
            "maximum_projector_residual": global_projector,
            "maximum_projector_overlap": global_orthogonality,
            "maximum_layer_frame_commutator": global_covariance,
            "maximum_layer_constraint_commutator": global_constraint,
            "maximum_layer_code_leakage": global_code_leakage,
            "maximum_raw_matrix_units_in_one_layer": max(layerwise_raw_terms),
            "supplied_spectral_clustering_tolerance": SPECTRAL_CLUSTER_TOLERANCE,
            "maximum_within_group_eigenvalue_spread": global_within_group_spread,
            "maximum_within_group_witness_beta_and_operator": within_group_witness,
            "maximum_within_group_spread_to_tolerance_ratio": (
                global_within_group_spread / SPECTRAL_CLUSTER_TOLERANCE
            ),
            "minimum_inter_eigenspace_gap": global_inter_eigenspace_gap,
            "minimum_inter_eigenspace_witness_beta_and_operator": inter_eigenspace_witness,
            "minimum_inter_eigenspace_gap_to_tolerance_ratio": (
                global_inter_eigenspace_gap / SPECTRAL_CLUSTER_TOLERANCE
            ),
            "within_operator_layer_order": "unordered commuting eigenspace factors",
            "staged_outer_schedule": "supplied coin, then stream/catch-up, then contact",
            "complete_update_schedule": "one supplied G coefficient block factored into sixteen unordered eigenspace layers",
        },
    )
    return {"pairs": all_pairs, "details": beta_details}


def basis_representatives(code) -> tuple[c235.Pauli, ...]:
    columns = c304.micro_columns(code)
    r_qubit = c306.gauge_qubit(code, c304.BODY)
    result = []
    for r_value in range(2):
        for column in columns:
            representative = column.representative
            if r_value:
                representative = c235.Pauli(
                    representative.phase,
                    representative.x | (1 << r_qubit),
                    representative.z,
                )
            result.append(representative)
    return tuple(result)


def physical_locality_and_leakage_controls(code, route_pairs, label: str) -> None:
    representatives = basis_representatives(code)
    columns = c304.micro_columns(code)
    active_patterns = {
        (column.tags, column.stream_slice, r_value)
        for r_value in range(2)
        for column in columns
    }
    representative_constraint_failures = 0
    representative_sector_failures = 0
    for representative in representatives:
        representative_constraint_failures += sum(
            not representative.commutes(c302.constraint_pauli(code, vertex))
            for vertex in range(len(code.graph.vertices))
        )
        representative_sector_failures += sum(
            not representative.commutes(row) for row in code.local_checks + code.wilsons
        )
    details = {}
    overall_union = 0
    overall_maximum = 0
    for route, pairs in route_pairs.items():
        route_union = 0
        maximum = 0
        for row, column in pairs:
            transition = representatives[row] @ c302.pauli_dagger(representatives[column])
            support = transition.x | transition.z
            route_union |= support
            maximum = max(maximum, support.bit_count())
        overall_union |= route_union
        overall_maximum = max(overall_maximum, maximum)
        details[route] = {
            "matrix_unit_pairs": len(pairs),
            "transition_union_M2": route_union.bit_count(),
            "maximum_transition_support_M2": maximum,
        }
    check(
        f"{label}: every primitive uses the same bounded 44-M2 patch and preserves inherited local constraints",
        len(active_patterns) == 180
        and representative_constraint_failures == 0
        and representative_sector_failures == 0
        and overall_union.bit_count() == 44
        and overall_maximum <= 30,
        {
            "distinct_local_tag_flag_r_projectors": len(active_patterns),
            "projector_control_M2": 14,
            "route_details": details,
            "overall_transition_union_M2": overall_union.bit_count(),
            "overall_maximum_transition_support_M2": overall_maximum,
            "installed_overhead_M2_per_cell": 23,
            "representative_port_constraint_failures": representative_constraint_failures,
            "representative_fixed_sector_failures": representative_sector_failures,
        },
    )


def covariance_translation_and_held_controls(training, held) -> None:
    encoding = c306.constrained_encoding()
    constraint = c306.role_constraint()
    maximum_target_frame = 0.0
    maximum_constraint_frame = 0.0
    for frame in c235.proper_cubic_frames():
        logical_r, micro_r = c304.frame_representations(frame)
        physical_r = c306.block_diagonal(micro_r, micro_r)
        maximum_constraint_frame = max(
            maximum_constraint_frame,
            float(np.linalg.norm(physical_r @ constraint - constraint @ physical_r)),
        )
        _old, logical, physical = c306.old_and_new_operators(-0.3)
        for name in logical:
            maximum_target_frame = max(
                maximum_target_frame,
                float(np.linalg.norm(physical_r @ physical[name] - physical[name] @ physical_r)),
                float(np.linalg.norm(logical_r @ logical[name] - logical[name] @ logical_r)),
                float(np.linalg.norm(physical_r @ encoding - encoding @ logical_r)),
            )

    solver = c304.reference_solver(training)
    source = c304.micro_columns(training, c304.BODY)
    translation_failures = 0
    r_targets = set()
    for displacement in product(range(training.length), repeat=3):
        vertex_map, edge_map = c304.c269.graph_translation_maps(training.graph, displacement)
        toggles, pairs, flips = c304.c269.repair_data(training.graph, vertex_map, edge_map)
        target = c304.micro_columns(training, displacement)
        r_targets.add(c306.gauge_qubit(training, displacement))
        for source_column, target_column in zip(source, target):
            phase = c304.state_relative_phase(
                training,
                solver,
                source_column.face_pauli,
                target_column.face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            translation_failures += phase != 0
            translation_failures += (
                c304.local.ports.permute_bits(source_column.tags, vertex_map)
                != target_column.tags
            )
    translation_failures += len(r_targets) != training.length**3

    held_patterns = {
        (column.tags, column.stream_slice, r_value)
        for r_value in range(2)
        for column in c304.micro_columns(held)
    }
    held_r = {c306.gauge_qubit(held, body) for body in held.graph.cells}
    check(
        "complete primitive products are all-frame covariant, translation homogeneous, and retain the held L=6 role placement",
        max(maximum_target_frame, maximum_constraint_frame) < TOLERANCE
        and translation_failures == 0
        and len(held_patterns) == 180
        and len(held_r) == HELD_SIZE**3,
        {
            "proper_cubic_frames": 24,
            "maximum_target_frame_residual": maximum_target_frame,
            "maximum_constraint_frame_residual": maximum_constraint_frame,
            "L3_translation_ray_tests": TRAINING_SIZE**3 * 90,
            "translation_failures": translation_failures,
            "held_local_projectors": len(held_patterns),
            "held_homogeneous_r_sites": len(held_r),
        },
    )


def deletion_controls(direct, gauge, spectral, constraint_data) -> None:
    direct_coin = direct["factorizations"]["coin"]
    direct_rotation = max(
        range(len(direct_coin.rotations)),
        key=lambda index: np.linalg.norm(direct_coin.rotations[index].elimination - np.eye(2)),
    )
    direct_deleted = reconstruct_qr(direct_coin, skip_rotation=direct_rotation)
    direct_target = c306.old_and_new_operators(-0.3)[2]["coin"]
    direct_deletion = float(np.linalg.norm(direct_deleted - direct_target, 2))

    gauge_coin = gauge["factorizations"]["coin"]
    gauge_rotation = max(
        range(len(gauge_coin.rotations)),
        key=lambda index: np.linalg.norm(gauge_coin.rotations[index].elimination - np.eye(2)),
    )
    gauge_deleted = reconstruct_qr(gauge_coin, skip_rotation=gauge_rotation)
    logical_target = c306.old_and_new_operators(-0.3)[1]["coin"]
    gauge_deletion = float(np.linalg.norm(gauge_deleted - logical_target, 2))

    spectral_coin = spectral_layers(logical_target)
    spectral_deletion = max(
        abs(eigenvalue - 1)
        for eigenvalue, _projector, _multiplicity in spectral_coin
        if abs(eigenvalue - 1) > 1e-10
    )
    _old, logical, _physical = c306.old_and_new_operators(-0.3)
    complete_update = logical["contact"] @ logical["stream"] @ logical["coin"]
    complete_update_deletion = max(
        abs(eigenvalue - 1)
        for eigenvalue, _projector, _multiplicity in spectral_layers(complete_update)
    )

    constraint = c306.role_constraint()
    left, right = next(iter(constraint_data["pairs"]))
    deleted_constraint = constraint.copy()
    deleted_constraint[[left, right], :] = deleted_constraint[[right, left], :]
    negative = np.zeros(180, dtype=complex)
    negative[left], negative[right] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    constraint_deletion = float(np.linalg.norm((deleted_constraint - constraint) @ negative))
    contact_deletion = float(
        np.linalg.norm(
            c306.lift_physical(c304.physical_contact(0.0))
            - c306.lift_physical(c304.physical_contact(c304.contact.COUPLING)),
            2,
        )
    )
    check(
        "deleting one direct, gauge, spectral, constraint, or contact primitive is detected",
        direct_deletion > 0.1
        and gauge_deletion > 0.1
        and spectral_deletion > 0.1
        and complete_update_deletion > 0.1
        and constraint_deletion > 0
        and contact_deletion > 0.3,
        {
            "direct_coin_rotation_deletion": direct_deletion,
            "gauge_coin_rotation_deletion": gauge_deletion,
            "spectral_coin_layer_deletion": spectral_deletion,
            "complete_update_spectral_layer_deletion": complete_update_deletion,
            "constraint_swap_deletion_on_Cminus_syndrome": constraint_deletion,
            "contact_g_to_zero_deletion": contact_deletion,
        },
    )


def lawful_domain_and_inventory() -> None:
    rejects = 0
    for invalid in (np.eye(2)[:, :1], np.asarray(((1, 1), (0, 1)), dtype=complex)):
        try:
            qr_factorization(invalid)
        except ValueError:
            rejects += 1
    try:
        c304.c269.build_code(2)
    except (KeyError, ValueError):
        rejects += 1
    check("lawful-domain controls reject nonsquare, nonunitary, and aliased-L inputs", rejects == 3, rejects)
    inventory = {
        "supplied coefficients": "Cycle-219 C, declared wedge^2 C, Cycle-230 g=0.37, complete G, and Cycle-306 K/F/projectors",
        "supplied local grammar": "Pauli transitions W_i W_j^dagger, fourteen-bit tag/flag/r projectors, and matrix-unit sums",
        "supplied numerical structure": "spectral eigenspace clustering tolerance 2e-8, stress-tested against within-group spreads and inter-eigenspace gaps",
        "derived direct": "180-sector QR coefficients, factor counts, full-completion residuals, leakage census",
        "derived gauge": "42-sector QR coefficients and C_role-centralizing lifted primitives",
        "derived spectral": "degenerate-eigenspace projectors from the supplied G, ten staged or sixteen complete-update covariant layers, code intertwiners",
        "host schedule": "coin then stream/catch-up then contact; QR ordering only for Routes 1/2",
        "genuinely local structure": "homogeneous C_role constraint and unordered swap grammar; spectral gates are local and covariant but scheduled",
        "still supplied": "application/occurrence of a finite circuit, initial code state, fixed Wilson ray, macrocell framing",
        "excluded": "physical time, autonomous recurrence law, energy/rate, Record, source/gravity semantics",
    }
    check("the primitive-synthesis supplied and derived structure is explicit", len(inventory) == 10, inventory)


def markdown_section(body: str, start: str, end: str | None) -> str:
    start_index = body.index(start)
    end_index = len(body) if end is None else body.index(end, start_index)
    return body[start_index:end_index]


def release_certificate_controls() -> None:
    body = NOTE.read_text(encoding="utf-8")
    n1 = markdown_section(body, "### N1", "### N2")
    n1_statuses = tuple(
        re.findall(r"^\|[^\n]*\|\s*\*\*([^*\n]+)\*\*\s*\|", n1, flags=re.MULTILINE)
    )
    expected_n1_statuses = (
        "ATTEMPTED",
        "ATTEMPTED",
        "ATTEMPTED",
        "ATTEMPTED",
        "OPEN / UNTESTED",
        "OPEN / UNTESTED",
        "OPEN / UNTESTED",
    )
    check(
        "the N1 route table has exactly seven accepted status markers",
        n1_statuses == expected_n1_statuses,
        n1_statuses,
    )

    n2 = markdown_section(body, "### N2", "### N3")
    directional_rows = tuple(
        re.findall(
            r"^\|\s*`(W_[a-z]+)`\s*\|\s*`(W_[a-z]+)`\s*\|\s*no\s*\|",
            n2,
            flags=re.MULTILINE,
        )
    )
    walls = ("W_gate", "W_apply", "W_rec", "W_prep")
    expected_directional_rows = set(permutations(walls, 2))
    check(
        "the N2 audit contains all twelve and only the directed wall separators",
        len(directional_rows) == 12
        and len(set(directional_rows)) == 12
        and set(directional_rows) == expected_directional_rows,
        directional_rows,
    )

    n4 = markdown_section(body, "### N4", "### N5")
    witness_locations = tuple(
        (name, int(line))
        for name, line in re.findall(r"`([^`\n]+\.md):(\d+)`", n4)
    )
    location_results = []
    for name, line in witness_locations:
        path = NOTE.parent / name
        lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
        location_results.append((name, line, bool(lines) and line <= len(lines) and bool(lines[line - 1].strip())))
    check(
        "all six N4 file-line witnesses resolve to nonempty source lines",
        len(location_results) == 6 and all(row[2] for row in location_results),
        location_results,
    )

    n5 = markdown_section(body, "### N5", "### N6")
    n6 = markdown_section(body, "### N6", "### N7")
    n7 = markdown_section(body, "### N7", "### N8")
    n8 = markdown_section(body, "### N8", "## Optimal next probe")
    normalized_sections = tuple(" ".join(section.lower().split()) for section in (n5, n6, n7, n8))
    broad_markers = (
        "**Broad gate status: FAIL / DO NOT SHIP.**",
        "Gate disposition: **FAIL / DO NOT SHIP for the broad negative.**",
    )
    section_markers_present = (
        "| statement | raw term | primitive/layer | complete local block | translated/held domain | outside scope |"
        in normalized_sections[0]
        and "the gauge qr and spectral routes are the partial-closure paths"
        in normalized_sections[1]
        and "reject any primitive no-go" in normalized_sections[2]
        and all(cycle in normalized_sections[3] for cycle in ("cycle 302", "cycle 306", "cycle 309"))
        and "no broad negative or axiom pressure" in normalized_sections[3]
    )
    check(
        "the N5-N8 and broad-negative release markers are exact",
        section_markers_present and all(marker in body for marker in broad_markers),
        {"sections": section_markers_present, "broad_markers": tuple(marker in body for marker in broad_markers)},
    )

    trailing_whitespace = []
    for path in (Path(__file__).resolve(), NOTE):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.endswith((" ", "\t")):
                trailing_whitespace.append((path.name, line_number))
    check("the Cycle-309 release paths contain no trailing whitespace", not trailing_whitespace, trailing_whitespace)


def hidden_premise_scan() -> None:
    phrases = (
        " ".join(("we", "assume")),
        " ".join(("by", "construction")),
        " ".join(("as", "is", "standard")),
        " ".join(("the", "framework", "provides")),
        " ".join(("bridge", "context")),
        "".join(("back", "ground")),
        "".join(("natural", "ly")),
        "".join(("obvious", "ly")),
        " ".join(("standard", "qft")),
        "".join(("register", "ed")),
        "".join(("canoni", "cal")),
    )
    hits = []
    for path in (Path(__file__).resolve(), NOTE):
        body = path.read_text(encoding="utf-8").lower()
        for phrase in phrases:
            if phrase in body:
                hits.append((path.name, phrase))
    check("the two-path hidden-premise scan has zero literal hits", not hits, hits)


def main() -> int:
    print("CYCLE 309: PRIMITIVE MATRIX-UNIT SYNTHESIS")
    print("authority=none; audit=unset")
    note_contract()
    physical_frames, logical_frames = frame_permutations()
    direct = direct_conditional_pauli_controls(physical_frames)
    constraint_data = constraint_swap_controls(physical_frames)
    gauge = gauge_generator_controls(logical_frames)
    spectral = finite_spectral_layer_controls(logical_frames)
    training = c304.c269.build_code(TRAINING_SIZE)
    held = c304.c269.build_code(HELD_SIZE)
    route_pairs = {
        "direct": direct["pairs"],
        "constraint": constraint_data["pairs"],
        "gauge": gauge["pairs"],
        "spectral": spectral["pairs"],
    }
    physical_locality_and_leakage_controls(training, route_pairs, "training L=3")
    physical_locality_and_leakage_controls(held, route_pairs, "held L=6")
    covariance_translation_and_held_controls(training, held)
    deletion_controls(direct, gauge, spectral, constraint_data)
    lawful_domain_and_inventory()
    release_certificate_controls()
    hidden_premise_scan()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
