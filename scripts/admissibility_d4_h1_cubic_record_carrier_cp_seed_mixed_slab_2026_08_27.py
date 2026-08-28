#!/usr/bin/env python3
"""Exact finite checks for the Block 218 bounded carrier construction."""

from __future__ import annotations

import argparse
import itertools
import math
import signal
from collections import Counter
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block218-same-law-seed-instrument-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block218-same-law-seed-instrument-20260827/NO_GO_LEDGER.md",
    "docs/ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_D4_H1_FULL_SHELL_SFT_MERGEABILITY_AND_AUTONOMOUS_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/CYCLE823_CYCLE719_SAME_CHART_HISTORY_PORT_CYCLE863_BOUNDED_THEOREM_NOTE_2026-08-01.md",
)
TOL = 2.0e-10
D = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
MUTATIONS = (
    "status_count",
    "q_gram",
    "rotation",
    "complement",
    "product_code",
    "writer_deleted",
    "lock",
    "deterministic_covariance",
    "event_effect_completeness",
    "slab_predicate",
    "slab_count",
    "independent_coin",
    "benchmark_amplitude",
    "benchmark_correlation",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            suffix = f": {detail}" if detail else ""
            print(f"FAIL {name}{suffix}")


def signed_permutation_rotations() -> list[np.ndarray]:
    rotations: list[np.ndarray] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis, source_axis] = signs[source_axis]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    rotations.sort(key=lambda matrix: tuple(int(x) for x in matrix.flat))
    return rotations


def direction_permutation(rotation: np.ndarray) -> tuple[int, ...]:
    direction_index = {direction: index for index, direction in enumerate(D)}
    return tuple(
        direction_index[tuple(int(x) for x in rotation @ np.array(direction))]
        for direction in D
    )


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for old, new in enumerate(permutation):
        if mask & (1 << old):
            result |= 1 << new
    return result


def configuration_orbits(
    site_count: int, permutations: list[tuple[int, ...]]
) -> tuple[Counter[int], list[set[int]]]:
    unseen = set(range(1 << site_count))
    orbits: list[set[int]] = []
    while unseen:
        seed = min(unseen)
        orbit = {permute_mask(seed, permutation) for permutation in permutations}
        unseen -= orbit
        orbits.append(orbit)
    return Counter(len(orbit) for orbit in orbits), orbits


def all_statuses() -> list[tuple[str, int | None, int]]:
    labels: list[tuple[str, int | None, int]] = [
        ("LOCK", None, 0),
        ("LOCK", None, 1),
        ("BG", None, 0),
        ("BG", None, 1),
    ]
    for kind in ("PORT", "GPORT", "STEP", "END"):
        for direction in range(6):
            for content in range(2):
                labels.append((kind, direction, content))
    return labels


def rotate_status(
    label: tuple[str, int | None, int], permutation: tuple[int, ...]
) -> tuple[str, int | None, int]:
    kind, direction, content = label
    return (kind, None if direction is None else permutation[direction], content)


def complement_status(
    label: tuple[str, int | None, int]
) -> tuple[str, int | None, int]:
    kind, direction, content = label
    return (kind, direction, 1 - content)


def status_orbit_count(
    labels: list[tuple[str, int | None, int]],
    permutations: list[tuple[int, ...]],
) -> int:
    label_set = set(labels)
    unseen = set(labels)
    count = 0
    while unseen:
        seed = min(unseen, key=str)
        orbit = {rotate_status(seed, permutation) for permutation in permutations}
        unseen -= orbit & label_set
        count += 1
    return count


def rotate_record_vector(vector: np.ndarray, permutation: tuple[int, ...]) -> np.ndarray:
    result = np.zeros_like(vector)
    for center in range(2):
        for shell in range(64):
            result[64 * center + permute_mask(shell, permutation)] = vector[
                64 * center + shell
            ]
    return result


def complement_matrix(mutation: str | None) -> np.ndarray:
    matrix = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            new_center = center if mutation == "complement" else 1 - center
            old_index = 64 * center + shell
            new_index = 64 * new_center + (shell ^ 63)
            matrix[new_index, old_index] = 1.0
    return matrix


def make_joint_code(
    labels: list[tuple[str, int | None, int]], q: np.ndarray, pairs: list[tuple[int, int]]
) -> dict[tuple[str, int | None, int], np.ndarray]:
    pair_masks = [(1 << left) | (1 << right) for left, right in pairs]

    def basis(center: int, shell: int) -> np.ndarray:
        vector = np.zeros(128)
        vector[64 * center + shell] = 1.0
        return vector

    code: dict[tuple[str, int | None, int], np.ndarray] = {}
    for label in labels:
        kind, direction, content = label
        if kind == "LOCK":
            code[label] = basis(content, 0 if content == 0 else 63)
        elif kind == "BG":
            code[label] = basis(1 - content, 0 if content == 0 else 63)
        elif kind in ("PORT", "GPORT"):
            assert direction is not None
            center = content if kind == "PORT" else 1 - content
            shell = (1 << direction) if content == 0 else (63 ^ (1 << direction))
            code[label] = basis(center, shell)
        else:
            assert direction is not None
            center = content if kind == "STEP" else 1 - content
            vector = np.zeros(128)
            for row, shell in enumerate(pair_masks):
                target_shell = shell if content == 0 else shell ^ 63
                vector[64 * center + target_shell] = q[row, direction]
            code[label] = vector
    return code


def product_code() -> dict[tuple[str, int | None, int], tuple[int, int]]:
    code: dict[tuple[str, int | None, int], tuple[int, int]] = {}
    for label in all_statuses():
        kind, direction, content = label
        if kind == "LOCK":
            state = (0, 0) if content == 0 else (63, 63)
        elif kind == "BG":
            state = (63, 0) if content == 0 else (0, 63)
        else:
            assert direction is not None
            singleton = 1 << direction
            zero_states = {
                "PORT": (singleton, 0),
                "GPORT": (singleton, 63),
                "STEP": (0, singleton),
                "END": (63, singleton),
            }
            state = zero_states[kind]
            if content == 1:
                state = (state[0] ^ 63, state[1] ^ 63)
        code[label] = state
    return code


def projector(index: int, dimension: int) -> np.ndarray:
    result = np.zeros((dimension, dimension))
    result[index, index] = 1.0
    return result


def outer(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.outer(left, right.conj())


def sqrt_psd(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T


def allowed_shell(shell: tuple[int, ...], include_loops: bool = True) -> bool:
    negative = (shell[0], shell[2], shell[4])
    positive = (shell[1], shell[3], shell[5])
    hamming = sum(left != right for left, right in zip(negative, positive))
    loop = negative == positive and negative in ((0, 0, 0), (1, 1, 1))
    return hamming == 1 or (include_loops and loop)


def plane_bit(plane: int, y: int, z: int) -> int:
    return (plane >> (4 * (y % 4) + (z % 4))) & 1


def slab_value(plane: int, x: int, y: int, z: int) -> int:
    if x < 0:
        return 0
    if x > 0:
        return 1
    return plane_bit(plane, y, z)


def valid_slab_plane(plane: int, include_loops: bool) -> bool:
    for x in (-1, 0, 1):
        for y in range(4):
            for z in range(4):
                shell = tuple(
                    slab_value(plane, x + dx, y + dy, z + dz)
                    for dx, dy, dz in D
                )
                if not allowed_shell(shell, include_loops=include_loops):
                    return False
    return True


def terminal_equations(plane: int) -> bool:
    for y in range(4):
        for z in range(4):
            if plane_bit(plane, y - 1, z) != plane_bit(plane, y + 1, z):
                return False
            if plane_bit(plane, y, z - 1) != plane_bit(plane, y, z + 1):
                return False
    return True


def source_and_note_checks(checks: Checks, root: Path) -> None:
    sources = (
        root
        / ".claude/science/physics-loops/toe-axiom-closure-block218-same-law-seed-instrument-20260827/GOAL.md",
        root
        / ".claude/science/physics-loops/toe-axiom-closure-block218-same-law-seed-instrument-20260827/NO_GO_LEDGER.md",
        root
        / "docs/ADMISSIBILITY_D4_H1_FULL_SHELL_SFT_MERGEABILITY_AND_AUTONOMOUS_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
        root
        / "docs/COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md",
        root
        / "docs/CYCLE823_CYCLE719_SAME_CHART_HISTORY_PORT_CYCLE863_BOUNDED_THEOREM_NOTE_2026-08-01.md",
    )
    note_path = (
        root
        / "docs/ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
    )
    texts = [path.read_text(encoding="utf-8") for path in sources]
    note = note_path.read_text(encoding="utf-8")
    source_anchors = (
        "positive-carrier-boundary",
        "N8 -- cross-cycle echo",
        "52 visible symbols",
        "p=a xor b",
        "same-chart physical-M2 port",
    )
    checks.check(
        "allowed source anchors",
        all(anchor in text for anchor, text in zip(source_anchors, texts)),
    )
    links = (
        "../.claude/science/physics-loops/toe-axiom-closure-block218-same-law-seed-instrument-20260827/GOAL.md",
        "../.claude/science/physics-loops/toe-axiom-closure-block218-same-law-seed-instrument-20260827/NO_GO_LEDGER.md",
        "ADMISSIBILITY_D4_H1_FULL_SHELL_SFT_MERGEABILITY_AND_AUTONOMOUS_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
        "COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md",
        "CYCLE823_CYCLE719_SAME_CHART_HISTORY_PORT_CYCLE863_BOUNDED_THEOREM_NOTE_2026-08-01.md",
    )
    checks.check("five exact dependency links", all(f"]({link})" in note for link in links))
    normalized_note = " ".join(note.split()).lower()
    phrases = (
        "joint-block Record interpretation remains supplied",
        "select a block-lattice phase",
        "unrecorded operational precursor, not readable Record content",
        "Generic Kraus normalization is prior art",
        "CP writer does not derive physical many-site implementation, branch effects, site, rate, time or history",
        "opportunity is not occurrence",
        "independent coins are not a local arbitration solution",
        "nonlocal on the tested plane",
        "No broad M2/compiler/formation no-go or axiom pressure is claimed",
        "no canonical axiom is edited and no TOE percentage moves",
        "locked-sector nondemolition",
        "per_element:",
        "per_site:",
        "per_mode:",
        "per_block:",
        "lattice_wide:",
    )
    checks.check(
        "required boundary prose",
        all(phrase.lower() in normalized_note for phrase in phrases),
    )


def run(mutation: str | None) -> tuple[Checks, str]:
    checks = Checks()

    rotations = signed_permutation_rotations()
    if mutation == "rotation":
        rotations[0] = np.diag((-1, 1, 1))
    rotation_keys = {tuple(int(x) for x in rotation.flat) for rotation in rotations}
    permutations = [direction_permutation(rotation) for rotation in rotations]
    checks.check("24 proper cubic rotations", len(rotation_keys) == 24)
    checks.check(
        "rotation signed-permutation determinants",
        all(
            np.array_equal(rotation.T @ rotation, np.eye(3, dtype=int))
            and round(np.linalg.det(rotation)) == 1
            for rotation in rotations
        ),
    )
    checks.check(
        "rotation group closure",
        all(
            tuple(int(x) for x in (left @ right).flat) in rotation_keys
            for left in rotations
            for right in rotations
        ),
    )

    labels = all_statuses()
    if mutation == "status_count":
        labels.pop()
    checks.check("52 status labels", len(labels) == 52 and len(set(labels)) == 52)
    status_orbits = status_orbit_count(labels, permutations)
    checks.check("12 status rotation orbits", status_orbits == 12, str(status_orbits))
    checks.check("six-bit information bound for 52", math.ceil(math.log2(52)) == 6)
    checks.check("six-bit information bound for 53", math.ceil(math.log2(53)) == 6)

    shell_histogram, shell_orbits = configuration_orbits(6, permutations)
    checks.check("six-shell orbit-sum dimension 10", len(shell_orbits) == 10, str(shell_histogram))
    checks.check(
        "literal six-shell invariant nonembedding",
        len(shell_orbits) == 10 and status_orbits == 12 and len(shell_orbits) < status_orbits,
    )

    pairs = [
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if np.dot(D[left], D[right]) == 0
    ]
    incidence = np.zeros((len(pairs), 6))
    for row, pair in enumerate(pairs):
        incidence[row, list(pair)] = 1.0
    if mutation == "q_gram":
        incidence[0, pairs[0][0]] = 0.0
    checks.check(
        "12 perpendicular incidence rows",
        len(pairs) == 12
        and all(int(np.sum(incidence[row])) == 2 for row in range(len(pairs))),
    )
    gram = incidence.T @ incidence
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    checks.check(
        "incidence Gram spectrum 2,2,4,4,4,8",
        np.allclose(eigenvalues, (2, 2, 4, 4, 4, 8), atol=TOL),
        np.array2string(eigenvalues, precision=8),
    )
    inverse_roots = np.array(
        [0.0 if value <= TOL else 1.0 / math.sqrt(value) for value in eigenvalues]
    )
    gram_inverse_root = (eigenvectors * inverse_roots) @ eigenvectors.T
    q = incidence @ gram_inverse_root
    checks.check("q column Gram identity", np.allclose(q.T @ q, np.eye(6), atol=TOL))

    code = make_joint_code(labels, q, pairs)
    code_matrix = np.column_stack(list(code.values()))
    checks.check("joint code has 52 vectors", code_matrix.shape == (128, 52))
    checks.check(
        "joint code orthonormal",
        code_matrix.shape[1] == 52
        and np.allclose(code_matrix.T @ code_matrix, np.eye(52), atol=TOL),
    )
    rotation_residual = 0.0
    for permutation in permutations:
        for label, vector in code.items():
            rotated_label = rotate_status(label, permutation)
            if rotated_label not in code:
                rotation_residual = math.inf
                break
            rotation_residual = max(
                rotation_residual,
                float(np.linalg.norm(rotate_record_vector(vector, permutation) - code[rotated_label])),
            )
    checks.check("joint code rotation intertwiner", rotation_residual < TOL, str(rotation_residual))

    complement = complement_matrix(mutation)
    complement_residual = 0.0
    for label, vector in code.items():
        target = complement_status(label)
        if target not in code:
            complement_residual = math.inf
            break
        complement_residual = max(
            complement_residual,
            float(np.linalg.norm(complement @ vector - code[target])),
        )
    checks.check("seven-bit complement covariance", complement_residual < TOL, str(complement_residual))

    omega = np.zeros(128)
    for center in range(2):
        for shell in range(64):
            if shell.bit_count() == 3:
                omega[64 * center + shell] = 1.0 / math.sqrt(40.0)
    checks.check("Omega unit norm", abs(np.vdot(omega, omega) - 1.0) < TOL)
    checks.check(
        "Omega orthogonal to all code vectors",
        np.max(np.abs(code_matrix.T @ omega)) < TOL,
    )
    checks.check(
        "Omega proper-cubic invariant",
        max(np.linalg.norm(rotate_record_vector(omega, permutation) - omega) for permutation in permutations)
        < TOL,
    )
    checks.check("Omega complement invariant", np.linalg.norm(complement @ omega - omega) < TOL)

    content_zero = []
    content_one = []
    for label, vector in code.items():
        kind, _, content = label
        decoded = content if kind in ("LOCK", "BG", "STEP") else 1 - content
        (content_zero if decoded == 0 else content_one).append(vector)
    pi_zero = sum((outer(vector, vector) for vector in content_zero), np.zeros((128, 128)))
    pi_one = sum((outer(vector, vector) for vector in content_one), np.zeros((128, 128)))
    code_projector = code_matrix @ code_matrix.T
    checks.check(
        "decoder effects are orthogonal projectors",
        np.allclose(pi_zero @ pi_zero, pi_zero, atol=TOL)
        and np.allclose(pi_one @ pi_one, pi_one, atol=TOL)
        and np.linalg.norm(pi_zero @ pi_one) < TOL,
    )
    checks.check(
        "decoder effects sum to code projector",
        np.allclose(pi_zero + pi_one, code_projector, atol=TOL)
        and round(np.trace(pi_zero)) == 26
        and round(np.trace(pi_one)) == 26,
    )
    checks.check(
        "decoder is not full identity",
        round(np.trace(code_projector)) == 52
        and not np.allclose(code_projector, np.eye(128), atol=TOL),
    )

    corners = list(itertools.product((-1, 1), repeat=3))
    corner_index = {corner: index for index, corner in enumerate(corners)}
    corner_permutations = [
        tuple(
            corner_index[tuple(int(x) for x in rotation @ np.array(corner))]
            for corner in corners
        )
        for rotation in rotations
    ]
    centered_axis_permutations = [tuple([0] + [1 + x for x in permutation]) for permutation in permutations]
    centered_corner_permutations = [
        tuple([0] + [1 + x for x in permutation]) for permutation in corner_permutations
    ]
    carrier_histograms = {
        "six": configuration_orbits(6, permutations)[0],
        "center+six": configuration_orbits(7, centered_axis_permutations)[0],
        "corner": configuration_orbits(8, corner_permutations)[0],
        "center+corner": configuration_orbits(9, centered_corner_permutations)[0],
    }
    print(
        "DATA product-orbit histograms "
        + "; ".join(
            f"{name}={dict(sorted(histogram.items()))}"
            for name, histogram in carrier_histograms.items()
        )
    )
    checks.check(
        "centered candidates have four fixed configurations",
        carrier_histograms["center+six"][1] == 4
        and carrier_histograms["center+corner"][1] == 4,
    )
    checks.check(
        "centered candidates have only four size-six orbits",
        carrier_histograms["center+six"][6] == 4
        and carrier_histograms["center+corner"][6] == 4,
    )
    checks.check(
        "sub-12 complete-orbit product candidates fail status supply",
        all(
            histogram[1] < 4 or histogram[6] < 8
            for histogram in carrier_histograms.values()
        ),
    )

    product = product_code()
    if mutation == "product_code":
        product[("END", 5, 1)] = product[("END", 5, 0)]
    checks.check("product code has 52 labels", len(product) == 52)
    checks.check("product code states distinct", len(set(product.values())) == 52)
    product_rotation_ok = True
    for permutation in permutations:
        for label, state in product.items():
            target = rotate_status(label, permutation)
            if target not in product or (
                permute_mask(state[0], permutation), permute_mask(state[1], permutation)
            ) != product[target]:
                product_rotation_ok = False
                break
    checks.check("two-shell product rotation covariance", product_rotation_ok)
    checks.check(
        "two-shell product complement covariance",
        all(
            (state[0] ^ 63, state[1] ^ 63) == product[complement_status(label)]
            for label, state in product.items()
        ),
    )

    # Total precursor/lock writer on the complete symmetry orbit of the four
    # supplied deterministic transition roles.  Context labels are physical
    # controls only in this bounded construction; their genesis remains open.
    deterministic_contexts: list[tuple[str, int | None, int]] = []
    target_by_context: dict[
        tuple[str, int | None, int], tuple[str, int | None, int]
    ] = {}
    for role, target_kind in (("PORT_STEP", "STEP"), ("STEP_END", "END")):
        for direction in range(6):
            for content in range(2):
                context_label = (role, direction, content)
                deterministic_contexts.append(context_label)
                target_by_context[context_label] = (target_kind, direction, content)
    for role in ("GATED_BG", "BG_BG"):
        for content in range(2):
            context_label = (role, None, content)
            deterministic_contexts.append(context_label)
            target_by_context[context_label] = ("BG", None, content)
    if mutation == "deterministic_covariance":
        target_by_context[("PORT_STEP", 0, 0)] = ("STEP", 1, 0)

    mixed_contexts = (("MIXED", None, 0), ("MIXED", None, 1))
    bad_context = ("BAD", None, 0)
    context_labels = tuple(deterministic_contexts) + mixed_contexts + (bad_context,)
    context_index = {label: index for index, label in enumerate(context_labels)}
    context_dimension = len(context_labels)
    identity_context = np.eye(context_dimension)
    deterministic_projectors = {
        label: projector(context_index[label], context_dimension)
        for label in deterministic_contexts
    }
    mixed_projector = sum(
        (projector(context_index[label], context_dimension) for label in mixed_contexts),
        np.zeros((context_dimension, context_dimension)),
    )
    bad_projector = projector(context_index[bad_context], context_dimension)
    checks.check(
        "31 writer contexts partition identity",
        context_dimension == 31
        and np.allclose(
            sum(deterministic_projectors.values(), np.zeros_like(identity_context))
            + mixed_projector
            + bad_projector,
            identity_context,
            atol=TOL,
        ),
    )

    def rotate_context(
        label: tuple[str, int | None, int], permutation: tuple[int, ...]
    ) -> tuple[str, int | None, int]:
        role, direction, content = label
        return (role, None if direction is None else permutation[direction], content)

    def complement_context(
        label: tuple[str, int | None, int]
    ) -> tuple[str, int | None, int]:
        role, direction, content = label
        if role == "BAD":
            return label
        return (role, direction, 1 - content)

    deterministic_covariance_ok = True
    for context_label in deterministic_contexts:
        target_label = target_by_context[context_label]
        for permutation in permutations:
            transformed_context = rotate_context(context_label, permutation)
            deterministic_covariance_ok &= (
                transformed_context in target_by_context
                and target_by_context[transformed_context]
                == rotate_status(target_label, permutation)
            )
        transformed_context = complement_context(context_label)
        deterministic_covariance_ok &= (
            transformed_context in target_by_context
            and target_by_context[transformed_context] == complement_status(target_label)
        )
    checks.check(
        "deterministic writer target map cubic and complement covariant",
        deterministic_covariance_ok,
    )
    checks.check(
        "mixed contexts exchange and bad context is fixed",
        complement_context(mixed_contexts[0]) == mixed_contexts[1]
        and complement_context(mixed_contexts[1]) == mixed_contexts[0]
        and complement_context(bad_context) == bad_context,
    )

    precursor = outer(omega, omega)
    record_lock = np.eye(128) if mutation == "lock" else np.eye(128) - precursor
    deterministic_targets = tuple(
        code[target_by_context[label]] for label in deterministic_contexts
    )
    mixed_targets = (code[("BG", None, 0)], code[("BG", None, 1)])
    writer_factors: list[tuple[np.ndarray, np.ndarray, str]] = [
        (
            deterministic_projectors[label],
            outer(code[target_by_context[label]], omega),
            f"det-{index}",
        )
        for index, label in enumerate(deterministic_contexts)
    ]
    if mutation == "writer_deleted":
        writer_factors.pop(1)
    writer_factors.extend(
        [
            (mixed_projector, outer(mixed_targets[0], omega) / math.sqrt(2.0), "mixed-0"),
            (mixed_projector, outer(mixed_targets[1], omega) / math.sqrt(2.0), "mixed-1"),
            (bad_projector, precursor, "bad"),
            (identity_context, record_lock, "lock"),
        ]
    )

    # All context factors are diagonal.  Accumulating the 128x128 completeness
    # block for each context is exact and avoids materializing a dense 3968x3968
    # matrix that carries no additional information.
    completeness_blocks = np.zeros((context_dimension, 128, 128))
    off_diagonal_residual = 0.0
    for left, right, _name in writer_factors:
        left_weight = left.conj().T @ left
        off_diagonal_residual = max(
            off_diagonal_residual,
            float(np.linalg.norm(left_weight - np.diag(np.diag(left_weight)))),
        )
        right_weight = right.conj().T @ right
        for index, weight in enumerate(np.diag(left_weight)):
            completeness_blocks[index] += float(np.real(weight)) * right_weight
    completeness_residual = max(
        float(np.linalg.norm(block - np.eye(128))) for block in completeness_blocks
    )
    checks.check(
        "writer Kraus completeness",
        off_diagonal_residual < TOL and completeness_residual < TOL,
        str(completeness_residual),
    )
    choi_gram = np.array(
        [
            [
                np.vdot(left_a, left_b) * np.vdot(right_a, right_b)
                for left_b, right_b, _ in writer_factors
            ]
            for left_a, right_a, _ in writer_factors
        ]
    )
    checks.check(
        "writer manifest Choi positive",
        np.min(np.linalg.eigvalsh(choi_gram)) >= -TOL,
    )
    rng = np.random.default_rng(218)
    trace_residual = 0.0
    for _ in range(3):
        context_vector = rng.normal(size=context_dimension) + 1j * rng.normal(
            size=context_dimension
        )
        record_vector = rng.normal(size=128) + 1j * rng.normal(size=128)
        context_vector /= np.linalg.norm(context_vector)
        record_vector /= np.linalg.norm(record_vector)
        output_trace = sum(
            float(np.linalg.norm(left @ context_vector) ** 2)
            * float(np.linalg.norm(right @ record_vector) ** 2)
            for left, right, _ in writer_factors
        )
        trace_residual = max(trace_residual, abs(output_trace - 1.0))
    checks.check("writer trace preservation controls", trace_residual < TOL, str(trace_residual))
    lock_residual = max(
        max(abs(np.vdot(omega, vector)), np.linalg.norm(record_lock @ vector - vector))
        for vector in code.values()
    )
    checks.check("all 52 recorded states exactly locked", lock_residual < TOL, str(lock_residual))

    bad_basis = np.eye(context_dimension)[context_index[bad_context]]
    bad_outputs = [
        (left @ bad_basis, right @ omega) for left, right, _ in writer_factors
    ]
    bad_nonzero = [
        (left, right)
        for left, right in bad_outputs
        if np.linalg.norm(left) * np.linalg.norm(right) > TOL
    ]
    checks.check(
        "bad context preserves precursor",
        len(bad_nonzero) == 1
        and np.linalg.norm(bad_nonzero[0][0] - bad_basis) < TOL
        and np.linalg.norm(bad_nonzero[0][1] - omega) < TOL,
    )
    deterministic_action_ok = True
    for context_label, target in zip(deterministic_contexts, deterministic_targets):
        context_basis = np.eye(context_dimension)[context_index[context_label]]
        outputs = [
            (left @ context_basis, right @ omega)
            for left, right, _ in writer_factors
        ]
        nonzero = [
            (left, right)
            for left, right in outputs
            if np.linalg.norm(left) * np.linalg.norm(right) > TOL
        ]
        deterministic_action_ok &= (
            len(nonzero) == 1
            and np.linalg.norm(nonzero[0][0] - context_basis) < TOL
            and np.linalg.norm(nonzero[0][1] - target) < TOL
        )
    checks.check("all 28 deterministic good writes exact", deterministic_action_ok)
    mixed_action_ok = True
    for context_label in mixed_contexts:
        context_basis = np.eye(context_dimension)[context_index[context_label]]
        outputs = [
            (left @ context_basis, right @ omega)
            for left, right, _ in writer_factors
        ]
        nonzero = [
            (left, right)
            for left, right in outputs
            if np.linalg.norm(left) * np.linalg.norm(right) > TOL
        ]
        expected = [target / math.sqrt(2.0) for target in mixed_targets]
        mixed_action_ok &= (
            len(nonzero) == 2
            and all(np.linalg.norm(left - context_basis) < TOL for left, _ in nonzero)
            and all(
                np.linalg.norm(actual - wanted) < TOL
                for (_left, actual), wanted in zip(nonzero, expected)
            )
        )
    checks.check("equal mixed write pair exact on both event orders", mixed_action_ok)
    checks.check(
        "good writes have zero code leakage",
        max(
            np.linalg.norm((np.eye(128) - code_projector) @ target)
            for target in deterministic_targets + mixed_targets
        )
        < TOL,
    )
    checks.check(
        "good writes create code probability from Omega",
        np.linalg.norm(code_projector @ omega) < TOL
        and all(
            abs(np.vdot(target, code_projector @ target) - 1.0) < TOL
            for target in deterministic_targets
        ),
    )
    malformed = np.zeros(128)
    malformed[0 * 64 + 0b000111] = 1.0 / math.sqrt(2.0)
    malformed[0 * 64 + 0b001011] = -1.0 / math.sqrt(2.0)
    checks.check(
        "orthogonal non-code sector is locked rather than reset",
        np.linalg.norm(code_projector @ malformed) < TOL
        and abs(np.vdot(omega, malformed)) < TOL
        and np.linalg.norm(record_lock @ malformed - malformed) < TOL,
    )
    mixed_covariance_residual = np.linalg.norm(
        complement @ outer(mixed_targets[0], omega) @ complement.T
        - outer(mixed_targets[1], omega)
    )
    checks.check(
        "mixed event-swap complement covariance",
        mixed_covariance_residual < TOL,
        str(mixed_covariance_residual),
    )

    # Cycle-823/863 opportunity-control composition.  The p=1 sector of the
    # exact endpoint XOR pointer carries a supplied two-dimensional branch menu.
    pointer_table = {(a, b): a ^ b for a in (0, 1) for b in (0, 1)}
    checks.check(
        "Cycle-823 endpoint pointer is exact XOR opportunity control",
        pointer_table == {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0},
    )
    pointer_basis = np.eye(2)
    branch_basis = np.eye(2)
    active_left = np.kron(pointer_basis[1], branch_basis[0])
    active_right = np.kron(pointer_basis[1], branch_basis[1])
    plus = (active_left + active_right) / math.sqrt(2.0)
    minus = (active_left - active_right) / math.sqrt(2.0)
    effects = [
        0.5 * outer(active_left, active_left),
        0.5 * outer(active_right, active_right),
        0.5 * outer(plus, plus),
        0.5 * outer(minus, minus),
    ]
    if mutation == "event_effect_completeness":
        effects[0] *= 1.2
    opportunity = np.kron(outer(pointer_basis[1], pointer_basis[1]), np.eye(2))
    checks.check(
        "event effects positive and nontrivial",
        all(np.min(np.linalg.eigvalsh(effect)) >= -TOL for effect in effects)
        and np.linalg.norm(effects[0] @ effects[2] - effects[2] @ effects[0]) > TOL,
    )
    checks.check(
        "event effects sum to opportunity",
        np.allclose(sum(effects, np.zeros_like(opportunity)), opportunity, atol=TOL),
    )
    event_dimension = 4
    bank_dimension = 5
    bank_basis = np.eye(bank_dimension)
    omega_bank = bank_basis[4]
    omega_bank_projector = outer(omega_bank, omega_bank)
    bank_lock = np.eye(bank_dimension) - omega_bank_projector
    event_factors = [
        (sqrt_psd(effect), outer(bank_basis[index], omega_bank))
        for index, effect in enumerate(effects)
    ]
    event_factors.extend(
        [
            (np.eye(event_dimension) - opportunity, omega_bank_projector),
            (np.eye(event_dimension), bank_lock),
        ]
    )
    event_completeness = sum(
        (
            np.kron(left.conj().T @ left, right.conj().T @ right)
            for left, right in event_factors
        ),
        np.zeros((event_dimension * bank_dimension, event_dimension * bank_dimension)),
    )
    checks.check(
        "opportunity-control Kraus completeness",
        np.allclose(
            event_completeness,
            np.eye(event_dimension * bank_dimension),
            atol=TOL,
        ),
    )
    event_probe = (active_left + 2.0j * active_right) / math.sqrt(5.0)
    event_probabilities = np.array(
        [np.vdot(event_probe, effect @ event_probe).real for effect in effects]
    )
    checks.check(
        "opportunity-control outcome normalization",
        abs(float(np.sum(event_probabilities)) - 1.0) < TOL
        and np.count_nonzero(event_probabilities > TOL) >= 3,
    )

    include_loops = mutation != "slab_predicate"
    valid_planes = [
        plane for plane in range(1 << 16) if valid_slab_plane(plane, include_loops)
    ]
    equation_planes = [plane for plane in range(1 << 16) if terminal_equations(plane)]
    expected_slab_count = 15 if mutation == "slab_count" else 16
    checks.check(
        "mixed slab exact 26-word census",
        len(valid_planes) == expected_slab_count,
        f"found {len(valid_planes)} expected {expected_slab_count}",
    )
    checks.check(
        "mixed slab independent terminal equations",
        include_loops and set(valid_planes) == set(equation_planes),
    )
    parity_reconstructions = {
        sum(
            (((bits >> (2 * (y % 2) + (z % 2))) & 1) << (4 * y + z))
            for y in range(4)
            for z in range(4)
        )
        for bits in range(16)
    }
    checks.check(
        "mixed slab four parity-class bits",
        set(valid_planes) == parity_reconstructions and len(parity_reconstructions) == 16,
    )
    computed_coin_probability = len(valid_planes) / float(1 << 16)
    expected_coin_probability = 2.0 ** (-11 if mutation == "independent_coin" else -12)
    checks.check(
        "independent-coin success is 2^-12",
        abs(computed_coin_probability - expected_coin_probability) < TOL,
        f"{computed_coin_probability}",
    )
    precursor_symbol = 2
    complement_symbol = {0: 1, 1: 0, precursor_symbol: precursor_symbol}
    mixed_input = {-1: 0, 0: precursor_symbol, 1: 1}
    transformed_input = {
        x: complement_symbol[mixed_input[-x]] for x in (-1, 0, 1)
    }
    checks.check(
        "mixed precursor symmetry has no fixed binary output",
        transformed_input == mixed_input
        and all(complement_symbol[bit] != bit for bit in (0, 1)),
    )

    benchmark_dimension = 17
    benchmark_basis = np.eye(benchmark_dimension)
    benchmark_omega = benchmark_basis[16]
    benchmark_precursor = outer(benchmark_omega, benchmark_omega)
    benchmark_amplitude = 0.3 if mutation == "benchmark_amplitude" else 0.25
    benchmark_kraus = [
        benchmark_amplitude * outer(benchmark_basis[index], benchmark_omega)
        for index in range(16)
    ]
    benchmark_sum = sum(
        (kraus.conj().T @ kraus for kraus in benchmark_kraus),
        np.zeros((benchmark_dimension, benchmark_dimension)),
    )
    checks.check(
        "shared-four-bit benchmark precursor completeness",
        np.allclose(benchmark_sum, benchmark_precursor, atol=TOL),
    )
    benchmark_complement = np.zeros((benchmark_dimension, benchmark_dimension))
    for index in range(16):
        benchmark_complement[index ^ 15, index] = 1.0
    benchmark_complement[16, 16] = 1.0
    checks.check(
        "shared-four-bit benchmark complement covariance",
        all(
            np.linalg.norm(
                benchmark_complement @ benchmark_kraus[index] @ benchmark_complement.T
                - benchmark_kraus[index ^ 15]
            )
            < TOL
            for index in range(16)
        ),
    )
    probabilities = np.full(16, 1.0 / 16.0)
    def outcome_site(bits: int, y: int, z: int) -> int:
        parity_index = 2 * (y % 2) + (z % 2)
        if mutation == "benchmark_correlation" and (y % 4, z % 4) == (2, 0):
            parity_index = 2
        return (bits >> parity_index) & 1

    same_parity_equal_probability = sum(
        probability
        for bits, probability in enumerate(probabilities)
        if outcome_site(bits, 0, 0) == outcome_site(bits, 2, 0)
    )
    different_parity_equal_probability = sum(
        probability
        for bits, probability in enumerate(probabilities)
        if outcome_site(bits, 0, 0) == outcome_site(bits, 1, 0)
    )
    one_marginal = sum(
        probability for bits, probability in enumerate(probabilities) if bits & 1
    )
    checks.check(
        "shared-four-bit benchmark is correlated nonlocal",
        abs(same_parity_equal_probability - 1.0) < TOL
        and abs(different_parity_equal_probability - 0.5) < TOL
        and abs(one_marginal - 0.5) < TOL
        and len(valid_planes) == 16,
    )

    source_and_note_checks(checks, Path(__file__).resolve().parents[1])
    classification = "positive-carrier-boundary" if checks.failed == 0 else f"rejected-mutation {mutation or 'baseline'}"
    return checks, classification


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    def timeout_handler(_signum: int, _frame: object) -> None:
        raise TimeoutError(f"exceeded {AUDIT_TIMEOUT_SEC} seconds")

    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, classification = run(arguments.mutation)
    except Exception as error:  # fail closed while retaining the required footer
        checks = Checks()
        checks.check("internal exception", False, f"{type(error).__name__}: {error}")
        classification = f"rejected-mutation {arguments.mutation or 'baseline'}"
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(f"SUMMARY PASS {checks.passed} FAIL {checks.failed}")
    print(f"CLASSIFICATION: {classification}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
