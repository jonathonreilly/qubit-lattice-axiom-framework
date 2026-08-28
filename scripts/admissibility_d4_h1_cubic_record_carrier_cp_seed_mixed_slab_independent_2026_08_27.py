#!/usr/bin/env python3
"""Independent exact checker for the Block-218 carrier, CP, and slab claims.

This runner reconstructs its finite objects directly.  It deliberately does
not import another project module.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import itertools
import signal
import sys
from typing import Iterable

import numpy as np


AUDIT_TIMEOUT_SEC = 180
TOL = 2.0e-10
Vector = tuple[int, int, int]

AXES: tuple[Vector, ...] = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}
ANTIPODAL_PAIRS = ((0, 1), (2, 3), (4, 5))
ROLE_KINDS = ("PORT", "GPORT", "STEP", "END")

MUTATIONS = (
    "rotation_catalog",
    "label_set",
    "word_predicate",
    "six_shell_orbits",
    "g_frame",
    "code_gram",
    "rotation",
    "complement",
    "omega",
    "carrier_histogram",
    "product_collision",
    "writer_completeness",
    "locked_invariance",
    "bad_context",
    "deterministic_covariance",
    "mixed_covariance",
    "event_menu",
    "slab_predicate",
    "slab_equations",
    "plane_isometry",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            print(f"PASS {name}" + (f" — {detail}" if detail else ""))
        else:
            self.failed += 1
            print(f"FAIL {name}" + (f" — {detail}" if detail else ""))


def dot(left: Vector, right: Vector) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Vector, right: Vector) -> Vector:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def matrix_vector(matrix: tuple[Vector, Vector, Vector], vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def determinant(matrix: tuple[Vector, Vector, Vector]) -> int:
    return dot(matrix[0], cross(matrix[1], matrix[2]))


def proper_rotations() -> tuple[tuple[Vector, Vector, Vector], ...]:
    """Choose R ex and an orthogonal R ey, then define R ez by a cross product."""
    rotations = []
    for image_ex in AXES:
        for image_ey in AXES:
            if dot(image_ex, image_ey) != 0:
                continue
            image_ez = cross(image_ex, image_ey)
            matrix = tuple(
                tuple(column[row] for column in (image_ex, image_ey, image_ez))
                for row in range(3)
            )
            assert len(matrix) == 3
            rotations.append(matrix)  # type: ignore[arg-type]
    unique = tuple(dict.fromkeys(rotations))
    if len(unique) != 24 or any(determinant(matrix) != 1 for matrix in unique):
        raise AssertionError("cross-product rotation construction failed")
    return unique


def axis_permutation(matrix: tuple[Vector, Vector, Vector]) -> tuple[int, ...]:
    return tuple(AXIS_INDEX[matrix_vector(matrix, axis)] for axis in AXES)


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(((mask >> source) & 1) << target for source, target in enumerate(permutation))


def exact_word_predicate(mask: int) -> bool:
    opposite_xors = tuple(
        ((mask >> left) & 1) ^ ((mask >> right) & 1)
        for left, right in ANTIPODAL_PAIRS
    )
    return sum(opposite_xors) == 1 or (
        opposite_xors == (0, 0, 0) and mask in (0, 63)
    )


def decode_word(mask: int) -> tuple[object, ...] | None:
    if mask == 0:
        return ("dot", 1)
    if mask == 63:
        return ("dot", -1)
    negative = tuple((mask >> left) & 1 for left, _ in ANTIPODAL_PAIRS)
    positive = tuple((mask >> right) & 1 for _, right in ANTIPODAL_PAIRS)
    changed = tuple(index for index in range(3) if negative[index] != positive[index])
    if len(changed) != 1:
        return None
    direction = [0, 0, 0]
    direction[changed[0]] = 1 if sum(negative) % 2 == 0 else -1
    return ("cross", *direction)


def block213_labels() -> tuple[tuple[object, ...], ...]:
    scalars = tuple((kind, bit) for kind in ("LOCK", "BG") for bit in (0, 1))
    directed = tuple(
        (kind, direction, background)
        for kind in ROLE_KINDS
        for direction in AXES
        for background in (0, 1)
    )
    return scalars + directed


def rotate_label(
    label: tuple[object, ...], permutation: tuple[int, ...]
) -> tuple[object, ...]:
    if label[0] in ("LOCK", "BG"):
        return label
    direction = label[1]
    assert isinstance(direction, tuple)
    return (label[0], AXES[permutation[AXIS_INDEX[direction]]], label[2])


def complement_label(label: tuple[object, ...]) -> tuple[object, ...]:
    if label[0] in ("LOCK", "BG"):
        return (label[0], 1 - int(label[1]))
    return (label[0], label[1], 1 - int(label[2]))


def decoded_bit(label: tuple[object, ...]) -> int:
    if label[0] in ("LOCK", "BG"):
        return int(label[1])
    background = int(label[2])
    return background if label[0] == "STEP" else 1 - background


def label_orbits(
    labels: Iterable[tuple[object, ...]], permutations: tuple[tuple[int, ...], ...]
) -> tuple[frozenset[tuple[object, ...]], ...]:
    unseen = set(labels)
    orbits = []
    while unseen:
        label = next(iter(unseen))
        orbit = frozenset(rotate_label(label, permutation) for permutation in permutations)
        orbits.append(orbit)
        unseen -= orbit
    return tuple(orbits)


def configuration_orbits(
    bit_count: int, permutations: tuple[tuple[int, ...], ...]
) -> tuple[frozenset[int], ...]:
    unseen = set(range(1 << bit_count))
    orbits = []
    while unseen:
        mask = min(unseen)
        orbit = frozenset(permute_mask(mask, permutation) for permutation in permutations)
        orbits.append(orbit)
        unseen -= orbit
    return tuple(orbits)


def orbit_histogram(orbits: Iterable[frozenset[int]]) -> Counter[int]:
    return Counter(len(orbit) for orbit in orbits)


def build_code(
    labels: tuple[tuple[object, ...], ...], mutation: str | None
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, tuple[tuple[int, int], ...]]:
    perpendicular_pairs = tuple(
        (left, right)
        for left, right in itertools.combinations(range(6), 2)
        if dot(AXES[left], AXES[right]) == 0
    )
    incidence = np.zeros((6, len(perpendicular_pairs)))
    for column, (left, right) in enumerate(perpendicular_pairs):
        incidence[left, column] = 1.0
        incidence[right, column] = 1.0
    if mutation == "g_frame":
        incidence[0, 0] = 0.0

    gram = incidence @ incidence.T
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    inverse_sqrt = (eigenvectors * (1.0 / np.sqrt(eigenvalues))) @ eigenvectors.T
    frame = inverse_sqrt @ incidence

    code = np.zeros((128, len(labels)))
    for column, label in enumerate(labels):
        kind = str(label[0])
        if kind in ("LOCK", "BG"):
            bit = int(label[1])
            central = bit if kind == "LOCK" else 1 - bit
            shell_mask = 0 if bit == 0 else 63
            code[central * 64 + shell_mask, column] = 1.0
            continue

        direction = label[1]
        assert isinstance(direction, tuple)
        direction_index = AXIS_INDEX[direction]
        background = int(label[2])
        central = background if kind in ("PORT", "STEP") else 1 - background
        if kind in ("PORT", "GPORT"):
            shell_mask = 1 << direction_index
            if background:
                shell_mask ^= 63
            code[central * 64 + shell_mask, column] = 1.0
        else:
            for edge_index, (left, right) in enumerate(perpendicular_pairs):
                shell_mask = (1 << left) | (1 << right)
                if background:
                    shell_mask ^= 63
                code[central * 64 + shell_mask, column] = frame[direction_index, edge_index]

    if mutation == "code_gram":
        code[:, 0] *= 0.9
    return code, gram, inverse_sqrt, frame, perpendicular_pairs


def rotate_state(vector: np.ndarray, permutation: tuple[int, ...]) -> np.ndarray:
    result = np.zeros_like(vector)
    for central in range(2):
        for mask in range(64):
            result[central * 64 + permute_mask(mask, permutation)] = vector[central * 64 + mask]
    return result


def complement_state(vector: np.ndarray) -> np.ndarray:
    result = np.zeros_like(vector)
    for central in range(2):
        for mask in range(64):
            result[(1 - central) * 64 + (mask ^ 63)] = vector[central * 64 + mask]
    return result


def product_codeword(label: tuple[object, ...]) -> tuple[int, int]:
    kind = str(label[0])
    if kind in ("LOCK", "BG"):
        bit = int(label[1])
        if kind == "LOCK":
            return (63 * bit, 63 * bit)
        return (63 * (1 - bit), 63 * bit)
    direction = label[1]
    assert isinstance(direction, tuple)
    singleton = 1 << AXIS_INDEX[direction]
    background = int(label[2])
    if kind == "PORT":
        word = (singleton, 0)
    elif kind == "GPORT":
        word = (singleton, 63)
    elif kind == "STEP":
        word = (0, singleton)
    else:
        word = (63, singleton)
    if background:
        word = (word[0] ^ 63, word[1] ^ 63)
    return word


def pure_state_fixed(operators: Iterable[np.ndarray], vector: np.ndarray) -> bool:
    trace = 0.0
    fidelity = 0.0
    for operator in operators:
        output = operator @ vector
        trace += float(output @ output)
        fidelity += float(vector @ output) ** 2
    return abs(trace - 1.0) < TOL and abs(fidelity - 1.0) < TOL


def writer_checks(
    checks: Checks,
    code: np.ndarray,
    labels: tuple[tuple[object, ...], ...],
    precursor: np.ndarray,
    permutations: tuple[tuple[int, ...], ...],
    mutation: str | None,
) -> None:
    identity = np.eye(128)
    code_projector = code @ code.T
    precursor_projector = np.outer(precursor, precursor)
    label_index = {label: index for index, label in enumerate(labels)}

    deterministic_contexts: list[tuple[str, Vector | None, int]] = []
    targets: dict[tuple[str, Vector | None, int], tuple[object, ...]] = {}
    for role, target_kind in (("PORT_STEP", "STEP"), ("STEP_END", "END")):
        for direction in AXES:
            for background in (0, 1):
                context = (role, direction, background)
                deterministic_contexts.append(context)
                targets[context] = (target_kind, direction, background)
    for role in ("GATED_BG", "BG_BG"):
        for background in (0, 1):
            context = (role, None, background)
            deterministic_contexts.append(context)
            targets[context] = ("BG", background)
    if mutation == "deterministic_covariance":
        targets[("PORT_STEP", AXES[0], 0)] = ("STEP", AXES[1], 0)

    mixed_contexts = (("MIXED", None, 0), ("MIXED", None, 1))
    bad_context = ("BAD", None, 0)
    context_labels = tuple(deterministic_contexts) + mixed_contexts + (bad_context,)
    checks.check("WRITER_CONTEXT_CATALOG", len(context_labels) == len(set(context_labels)) == 31)

    def rotate_context(
        context: tuple[str, Vector | None, int], permutation: tuple[int, ...]
    ) -> tuple[str, Vector | None, int]:
        role, direction, background = context
        if direction is None:
            return context
        return (role, AXES[permutation[AXIS_INDEX[direction]]], background)

    def complement_context(
        context: tuple[str, Vector | None, int]
    ) -> tuple[str, Vector | None, int]:
        role, direction, background = context
        if role == "BAD":
            return context
        return (role, direction, 1 - background)

    covariance_ok = True
    for context in deterministic_contexts:
        target = targets[context]
        for permutation in permutations:
            transformed = rotate_context(context, permutation)
            covariance_ok &= (
                transformed in targets
                and targets[transformed] == rotate_label(target, permutation)
            )
        transformed = complement_context(context)
        covariance_ok &= (
            transformed in targets
            and targets[transformed] == complement_label(target)
        )
    checks.check(
        "DETERMINISTIC_WRITER_COVARIANCE",
        covariance_ok,
        "all 28 contexts intertwine 24 rotations and complement",
    )
    checks.check(
        "MIXED_BAD_CONTEXT_COVARIANCE",
        complement_context(mixed_contexts[0]) == mixed_contexts[1]
        and complement_context(mixed_contexts[1]) == mixed_contexts[0]
        and complement_context(bad_context) == bad_context,
    )

    record_lock = identity - precursor_projector
    if mutation == "locked_invariance":
        record_lock -= np.outer(code[:, 0], code[:, 0])
    by_context: dict[tuple[str, Vector | None, int], list[np.ndarray]] = {}
    for context in deterministic_contexts:
        operators = [
            record_lock,
            np.outer(code[:, label_index[targets[context]]], precursor),
        ]
        if mutation == "writer_completeness" and context == deterministic_contexts[0]:
            operators.pop()
        by_context[context] = operators

    mixed_left_label: tuple[object, ...] = ("BG", 0)
    mixed_right_label: tuple[object, ...] = ("BG", 1)
    if mutation == "mixed_covariance":
        mixed_right_label = ("LOCK", 1)
    mixed_operators = [
        record_lock,
        np.outer(code[:, label_index[mixed_left_label]], precursor) / np.sqrt(2.0),
        np.outer(code[:, label_index[mixed_right_label]], precursor) / np.sqrt(2.0),
    ]
    by_context[mixed_contexts[0]] = mixed_operators
    by_context[mixed_contexts[1]] = [operator.copy() for operator in mixed_operators]
    bad_precursor = precursor_projector.copy()
    if mutation == "bad_context":
        bad_precursor *= 0.0
    by_context[bad_context] = [record_lock, bad_precursor]

    completeness_residuals = {
        context: float(
            np.linalg.norm(
                sum(
                    (operator.T @ operator for operator in operators),
                    np.zeros((128, 128)),
                )
                - identity,
                ord=2,
            )
        )
        for context, operators in by_context.items()
    }
    maximum_completeness = max(completeness_residuals.values())
    checks.check(
        "WRITER_COMPLETENESS",
        maximum_completeness < TOL,
        f"31 context blocks; residual={maximum_completeness:.3g}",
    )
    choi_minima = []
    for operators in by_context.values():
        flat = np.stack([operator.reshape(-1) for operator in operators])
        choi_minima.append(float(np.linalg.eigvalsh(flat @ flat.T)[0]))
    checks.check(
        "WRITER_CHOI_POSITIVE",
        min(choi_minima) > TOL,
        f"direct-sum manifest Choi minimum={min(choi_minima):.6g}",
    )

    trace_ok = True
    for seed in (218, 823, 863):
        generator = np.random.default_rng(seed)
        vector = generator.normal(size=128)
        vector /= np.linalg.norm(vector)
        trace_ok &= all(
            abs(
                sum(
                    float(np.linalg.norm(operator @ vector) ** 2)
                    for operator in operators
                )
                - 1.0
            )
            < TOL
            for operators in by_context.values()
        )
    checks.check("WRITER_TRACE_PRESERVATION", trace_ok, "state seeds 218,823,863")

    locked_ok = all(
        pure_state_fixed(operators, code[:, column])
        for operators in by_context.values()
        for column in range(52)
    )
    checks.check("LOCKED_STATE_INVARIANCE", locked_ok, "all 31x52 context/code inputs")
    checks.check("BAD_CONTEXT_PRECURSOR", pure_state_fixed(by_context[bad_context], precursor))

    deterministic_actions = True
    for context in deterministic_contexts:
        outputs = [operator @ precursor for operator in by_context[context]]
        nonzero = [output for output in outputs if np.linalg.norm(output) > TOL]
        expected = code[:, label_index[targets[context]]]
        deterministic_actions &= len(nonzero) == 1 and np.allclose(
            nonzero[0], expected, atol=TOL, rtol=0.0
        )
    checks.check("DETERMINISTIC_WRITER_ACTIONS", deterministic_actions, "all 28 targets")

    mixed_actions = True
    for context in mixed_contexts:
        outputs = [operator @ precursor for operator in by_context[context]]
        nonzero = [output for output in outputs if np.linalg.norm(output) > TOL]
        expected = (
            code[:, label_index[("BG", 0)]] / np.sqrt(2.0),
            code[:, label_index[mixed_right_label]] / np.sqrt(2.0),
        )
        mixed_actions &= len(nonzero) == 2 and all(
            np.allclose(actual, wanted, atol=TOL, rtol=0.0)
            for actual, wanted in zip(nonzero, expected)
        )
    checks.check("MIXED_WRITER_ACTIONS", mixed_actions, "both event-order contexts")

    complement_matrix = np.column_stack(
        [complement_state(np.eye(128)[:, column]) for column in range(128)]
    )
    mixed_covariance = np.allclose(
        complement_matrix @ mixed_operators[1] @ complement_matrix.T,
        mixed_operators[2],
        atol=TOL,
        rtol=0.0,
    )
    checks.check(
        "MIXED_BRANCH_COVARIANCE",
        mixed_covariance,
        "equal BG branches swap under complement",
    )

    malformed = np.zeros(128)
    malformed[0b000111] = 1.0 / np.sqrt(2.0)
    malformed[0b001011] = -1.0 / np.sqrt(2.0)
    checks.check(
        "NONCODE_LOCK_SECTOR",
        np.linalg.norm(code_projector @ malformed) < TOL
        and abs(float(precursor @ malformed)) < TOL
        and np.allclose(record_lock @ malformed, malformed, atol=TOL, rtol=0.0),
    )

    deleted = np.outer(
        code[:, label_index[targets[deterministic_contexts[0]]]], precursor
    )
    deletion_residual = deleted.T @ deleted
    deletion_spectrum = np.linalg.eigvalsh(deletion_residual)
    checks.check(
        "WRITER_KRAUS_DELETION",
        deletion_spectrum[-1] > 0.99 and deletion_spectrum[0] > -TOL,
        f"positive completeness residual={deletion_spectrum[-1]:.6g}",
    )

def event_menu_checks(checks: Checks, mutation: str | None) -> None:
    event_dimension = 4
    xor_table = tuple(a ^ b for a in (0, 1) for b in (0, 1))
    checks.check("CYCLE823_XOR_POINTER", xor_table == (0, 1, 1, 0))
    pointer_basis = np.eye(2)
    branch_basis = np.eye(2)
    left = np.kron(pointer_basis[1], branch_basis[0])
    right = np.kron(pointer_basis[1], branch_basis[1])
    opportunity_projector = np.kron(
        np.outer(pointer_basis[1], pointer_basis[1]), np.eye(2)
    )
    plus = (left + right) / np.sqrt(2.0)
    minus = (left - right) / np.sqrt(2.0)
    base_effects = (
        0.5 * np.outer(left, left),
        0.5 * np.outer(right, right),
        0.5 * np.outer(plus, plus),
        0.5 * np.outer(minus, minus),
    )
    effects = list(base_effects)
    if mutation == "event_menu":
        effects.pop()
    effect_ok = (
        len(effects) == 4
        and all(np.linalg.eigvalsh(effect)[0] > -TOL for effect in effects)
        and np.allclose(
            sum(effects, np.zeros_like(opportunity_projector)),
            opportunity_projector,
            atol=TOL,
            rtol=0.0,
        )
        and any(
            np.linalg.norm(first @ second - second @ first) > 0.1
            for first, second in itertools.combinations(effects, 2)
        )
    )
    checks.check(
        "EVENT_BRANCH_EFFECTS",
        effect_ok,
        "four positive noncommuting effects sum to the opportunity projector",
    )

    bank_dimension = 5
    bank_basis = np.eye(bank_dimension)
    bank_precursor = bank_basis[4]
    bank_precursor_projector = np.outer(bank_precursor, bank_precursor)

    def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
        values, vectors = np.linalg.eigh(matrix)
        return (vectors * np.sqrt(np.maximum(values, 0.0))) @ vectors.T

    operators = [
        np.kron(
            positive_sqrt(effect),
            np.outer(bank_basis[index], bank_precursor),
        )
        for index, effect in enumerate(effects)
    ]
    operators.extend(
        (
            np.kron(
                np.eye(event_dimension) - opportunity_projector,
                bank_precursor_projector,
            ),
            np.kron(
                np.eye(event_dimension),
                np.eye(bank_dimension) - bank_precursor_projector,
            ),
        )
    )
    total_dimension = event_dimension * bank_dimension
    total = sum(
        (operator.T @ operator for operator in operators),
        np.zeros((total_dimension, total_dimension)),
    )
    checks.check(
        "EVENT_MENU_COMPLETENESS",
        np.linalg.norm(total - np.eye(total_dimension), ord=2) < TOL,
        "four-seed bank plus failure and lock Kraus operators",
    )
    checks.check(
        "EVENT_EFFECT_DELETIONS",
        all(
            np.linalg.eigvalsh(effect)[-1] > 0.49
            and np.linalg.eigvalsh(effect)[0] > -TOL
            for effect in base_effects
        ),
        "deleting any branch leaves a positive completeness residual",
    )

def gf2_rank(rows: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for initial in rows:
        row = initial
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def slab_checks(checks: Checks, mutation: str | None) -> tuple[int, ...]:
    predicate_table = [exact_word_predicate(mask) for mask in range(64)]
    if mutation == "slab_predicate":
        predicate_table[2] = False

    valid_planes = []
    touched_words = 0
    for plane in range(1 << 16):
        valid = True
        for y in range(4):
            for z in range(4):
                center_bit = (plane >> (4 * y + z)) & 1
                negative_boundary = center_bit << 1
                positive_boundary = 62 | center_bit
                center_word = 2
                center_word |= ((plane >> (4 * ((y - 1) % 4) + z)) & 1) << 2
                center_word |= ((plane >> (4 * ((y + 1) % 4) + z)) & 1) << 3
                center_word |= ((plane >> (4 * y + ((z - 1) % 4))) & 1) << 4
                center_word |= ((plane >> (4 * y + ((z + 1) % 4))) & 1) << 5
                word_results = (
                    predicate_table[negative_boundary],
                    predicate_table[center_word],
                    predicate_table[positive_boundary],
                )
                valid &= all(word_results)
                touched_words += 3
        if valid:
            valid_planes.append(plane)

    valid_set = set(valid_planes)
    complement_closed = all((plane ^ 0xFFFF) in valid_set for plane in valid_planes)
    checks.check(
        "SLAB_DIRECT_CENSUS",
        len(valid_planes) == 16
        and touched_words == (1 << 16) * 48
        and complement_closed,
        f"valid={len(valid_planes)}; touched words={touched_words}; complement={complement_closed}",
    )

    equation_rows = []
    for y in range(4):
        for z in range(4):
            equation_rows.append((1 << (4 * ((y - 1) % 4) + z)) | (1 << (4 * ((y + 1) % 4) + z)))
            equation_rows.append((1 << (4 * y + ((z - 1) % 4))) | (1 << (4 * y + ((z + 1) % 4))))
    if mutation == "slab_equations":
        equation_rows.append(1)
    rank = gf2_rank(equation_rows)
    equation_solutions = tuple(
        plane
        for plane in range(1 << 16)
        if all((plane & row).bit_count() % 2 == 0 for row in equation_rows)
    )
    checks.check(
        "SLAB_PARITY_EQUATIONS",
        rank == 12 and 16 - rank == 4 and len(equation_solutions) == 16
        and set(equation_solutions) == valid_set,
        f"rank={rank}; free bits={16-rank}; solutions={len(equation_solutions)}",
    )
    probability = Fraction(len(valid_planes), 1 << 16)
    checks.check(
        "SLAB_FAIR_SUCCESS",
        probability == Fraction(1, 1 << 12),
        f"independent fair success={probability}",
    )
    return tuple(valid_planes)


def isometry_checks(checks: Checks, valid_planes: tuple[int, ...], mutation: str | None) -> None:
    amplitudes = {plane: 0.25 for plane in valid_planes}
    if mutation == "plane_isometry" and amplitudes:
        amplitudes[valid_planes[0]] = 0.30
    norm = sum(amplitude * amplitude for amplitude in amplitudes.values())
    covariance = all(
        (plane ^ 0xFFFF) in amplitudes
        and abs(amplitudes[plane] - amplitudes[plane ^ 0xFFFF]) < TOL
        for plane in amplitudes
    )
    checks.check(
        "SHARED_FOUR_BIT_ISOMETRY",
        len(amplitudes) == 16 and abs(norm - 1.0) < TOL and covariance,
        f"outputs={len(amplitudes)}; amplitude=1/4; norm={norm:.6g}; complement={covariance}",
    )
    print("SCOPE plane isometry is nonlocal on the 16-site plane.")


def run(mutation: str | None) -> int:
    checks = Checks()
    rotations = proper_rotations()
    if mutation == "rotation_catalog":
        rotations = rotations[:-1]
    permutations = tuple(axis_permutation(rotation) for rotation in rotations)
    checks.check("PROPER_ROTATIONS", len(rotations) == 24 and len(set(permutations)) == 24)

    labels = block213_labels()
    checked_labels = labels[:-1] if mutation == "label_set" else labels
    rotations_of_labels = label_orbits(checked_labels, permutations)
    complement_pairs = {
        frozenset((label, complement_label(label))) for label in checked_labels
    }
    words = tuple(mask for mask in range(64) if exact_word_predicate(mask))
    if mutation == "word_predicate":
        words = words[:-1]
    checks.check(
        "LABEL_AND_WORD_CONVENTION",
        len(checked_labels) == 52
        and len(rotations_of_labels) == 12
        and len(complement_pairs) == 26
        and all(len(pair) == 2 for pair in complement_pairs)
        and len(words) == 26
        and all(decode_word(mask) is not None for mask in words),
        f"labels={len(checked_labels)}; rotation orbits={len(rotations_of_labels)}; complement pairs={len(complement_pairs)}; words={len(words)}",
    )

    shell_orbits = configuration_orbits(6, permutations)
    if mutation == "six_shell_orbits":
        shell_orbits = shell_orbits[:-1]
    checks.check(
        "SIX_SHELL_ORBITS",
        len(shell_orbits) == 10,
        f"64 patterns give {len(shell_orbits)} orbits",
    )
    print(
        "BOUNDARY 12 invariant label vectors cannot inject into 10 configuration orbits "
        "for the six-shell product representation."
    )

    code, frame_gram, inverse_sqrt, frame, pairs = build_code(labels, mutation)
    gram_spectrum = np.linalg.eigvalsh(frame_gram)
    inverse_check = inverse_sqrt @ frame_gram @ inverse_sqrt
    checks.check(
        "PAIR_FRAME",
        len(pairs) == 12
        and np.allclose(gram_spectrum, (2, 2, 4, 4, 4, 8), atol=TOL, rtol=0.0)
        and np.allclose(inverse_check, np.eye(6), atol=TOL, rtol=0.0)
        and np.allclose(frame @ frame.T, np.eye(6), atol=TOL, rtol=0.0),
        f"spec(G)={tuple(float(round(value, 10)) for value in gram_spectrum)}; symmetric eigh",
    )
    code_gram = code.T @ code
    checks.check(
        "CODE_GRAM",
        np.allclose(code_gram, np.eye(52), atol=TOL, rtol=0.0),
        f"52x52 residual={np.max(np.abs(code_gram-np.eye(52))):.3g}",
    )

    label_index = {label: index for index, label in enumerate(labels)}
    rotation_ok = True
    for rotation_index, permutation in enumerate(permutations):
        for column, label in enumerate(labels):
            target = label_index[rotate_label(label, permutation)]
            checked_permutation = permutation
            if mutation == "rotation" and rotation_index == 0:
                perturbed = list(permutation)
                perturbed[0], perturbed[2] = perturbed[2], perturbed[0]
                checked_permutation = tuple(perturbed)
            rotation_ok &= np.allclose(
                rotate_state(code[:, column], checked_permutation),
                code[:, target],
                atol=TOL,
                rtol=0.0,
            )
    checks.check("ROTATION_INTERTWINERS", rotation_ok, "all 24x52 actions")

    complement_ok = True
    for column, label in enumerate(labels):
        target = label_index[complement_label(label)]
        transformed = complement_state(code[:, column])
        if mutation == "complement" and column == 0:
            transformed = transformed.copy()
            transformed[0] += 0.1
        complement_ok &= np.allclose(
            transformed,
            code[:, target],
            atol=TOL,
            rtol=0.0,
        )
    checks.check("COMPLEMENT_INTERTWINERS", complement_ok, "all 52 actions")

    uniform_weight_three = np.zeros(64)
    weight_three_masks = tuple(mask for mask in range(64) if mask.bit_count() == 3)
    uniform_weight_three[list(weight_three_masks)] = 1.0 / np.sqrt(len(weight_three_masks))
    omega = np.concatenate((uniform_weight_three, uniform_weight_three)) / np.sqrt(2.0)
    if mutation == "omega":
        omega = omega + 0.1 * code[:, 0]
        omega /= np.linalg.norm(omega)
    omega_ok = (
        abs(float(omega @ omega) - 1.0) < TOL
        and np.max(np.abs(code.T @ omega)) < TOL
        and all(np.allclose(rotate_state(omega, permutation), omega, atol=TOL, rtol=0.0) for permutation in permutations)
        and np.allclose(complement_state(omega), omega, atol=TOL, rtol=0.0)
    )
    checks.check("OMEGA_PRECURSOR", omega_ok, "|+> tensor uniform weight-three; norm/code/symmetry")

    decode_zero = code[:, [decoded_bit(label) == 0 for label in labels]]
    decode_one = code[:, [decoded_bit(label) == 1 for label in labels]]
    projector_zero = decode_zero @ decode_zero.T
    projector_one = decode_one @ decode_one.T
    decode_ok = (
        np.linalg.matrix_rank(projector_zero, tol=TOL) == 26
        and np.linalg.matrix_rank(projector_one, tol=TOL) == 26
        and np.linalg.matrix_rank(projector_zero + projector_one, tol=TOL) == 52
        and np.allclose(projector_zero @ projector_one, 0.0, atol=TOL, rtol=0.0)
    )
    checks.check("DECODE_PROJECTORS", decode_ok, "ranks 26+26=52")

    face_orbits = configuration_orbits(6, permutations)
    if mutation == "carrier_histogram":
        face_orbits = face_orbits[:-1]
    face_histogram = orbit_histogram(face_orbits)
    center_face_permutations = tuple(
        (0,) + tuple(target + 1 for target in permutation)
        for permutation in permutations
    )
    center_face_histogram = orbit_histogram(
        configuration_orbits(7, center_face_permutations)
    )
    corners = tuple(itertools.product((-1, 1), repeat=3))
    corner_index = {corner: index for index, corner in enumerate(corners)}
    corner_permutations = tuple(
        tuple(corner_index[matrix_vector(rotation, corner)] for corner in corners)
        for rotation in rotations
    )
    corner_orbits = configuration_orbits(8, corner_permutations)
    corner_histogram = orbit_histogram(corner_orbits)
    center_corner_permutations = tuple(
        (0,) + tuple(target + 1 for target in permutation)
        for permutation in corner_permutations
    )
    center_corner_histogram = orbit_histogram(
        configuration_orbits(9, center_corner_permutations)
    )
    carrier_counts = (
        (face_histogram[1], face_histogram[6]),
        (center_face_histogram[1], center_face_histogram[6]),
        (corner_histogram[1], corner_histogram[6]),
        (center_corner_histogram[1], center_corner_histogram[6]),
    )
    checks.check(
        "CARRIER_HISTOGRAMS",
        carrier_counts == ((2, 2), (4, 4), (2, 2), (4, 4)),
        f"fixed/size-six={carrier_counts}",
    )

    product_words = [product_codeword(label) for label in labels]
    if mutation == "product_collision":
        product_words[1] = product_words[0]
    product_rotation = all(
        (
            permute_mask(product_words[column][0], permutation),
            permute_mask(product_words[column][1], permutation),
        )
        == product_words[label_index[rotate_label(label, permutation)]]
        for permutation in permutations
        for column, label in enumerate(labels)
    )
    product_complement = all(
        (word[0] ^ 63, word[1] ^ 63)
        == product_words[label_index[complement_label(labels[column])]]
        for column, word in enumerate(product_words)
    )
    checks.check(
        "TWO_SHELL_PRODUCT_CODE",
        len(set(product_words)) == 52 and product_rotation and product_complement,
        f"distinct={len(set(product_words))}; rotations={product_rotation}; complement={product_complement}",
    )

    writer_checks(checks, code, labels, omega, permutations, mutation)
    event_menu_checks(checks, mutation)
    valid_planes = slab_checks(checks, mutation)
    isometry_checks(checks, valid_planes, mutation)

    print(f"SUMMARY PASS {checks.passed} FAIL {checks.failed}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


def timeout_handler(_signum: int, _frame: object) -> None:
    print("FAIL AUDIT_TIMEOUT — exceeded 180 seconds")
    print("SUMMARY PASS 0 FAIL 1")
    print("TOTAL: PASS=0 FAIL=1")
    raise SystemExit(2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-mutations", action="store_true")
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    if arguments.list_mutations:
        print("\n".join(MUTATIONS))
        return 0
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        return run(arguments.mutation)
    except Exception as error:
        print(f"FAIL INTERNAL_EXCEPTION — {type(error).__name__}: {error}")
        print("SUMMARY PASS 0 FAIL 1")
        print("TOTAL: PASS=0 FAIL=1")
        return 2
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)


if __name__ == "__main__":
    sys.exit(main())
