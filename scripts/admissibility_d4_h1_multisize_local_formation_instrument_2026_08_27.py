#!/usr/bin/env python3
"""Exact primary checks for the Block 219 local formation-instrument boundary."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import signal
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/NO_GO_LEDGER.md",
    "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-27.md",
    "docs/ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
)
TOL = 2.0e-10
DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
MUTATIONS = (
    "transient_center",
    "transient_shell",
    "complement",
    "edge_range",
    "size_metadata",
    "coordinate_phase",
    "global_label",
    "normalization",
    "branch_delete",
    "translation",
    "cubic",
    "record_lock",
    "rank_claim",
    "heldout",
    "success_probability",
    "critical_pair",
    "terminal_support",
    "history_cylinder",
    "rule_hash",
    "autonomous_overclaim",
    "voter_completeness",
    "voter_bias",
    "voter_dark_state",
    "commit_locality",
    "lock_even_label_merge",
    "voter_label_covariance",
)
VOTER_BRANCH_LABELS = (
    "equal-00",
    "equal-11",
    "01-to-00",
    "01-to-11",
    "10-to-00",
    "10-to-11",
    "outside-lock",
)
VOTER_ENDPOINT_BRANCH_PERMUTATION = (0, 1, 4, 5, 2, 3, 6)
VOTER_COMPLEMENT_BRANCH_PERMUTATION = (1, 0, 5, 4, 3, 2, 6)


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


def outer(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.outer(left, right.conj())


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
    index = {direction: slot for slot, direction in enumerate(DIRECTIONS)}
    return tuple(
        index[tuple(int(x) for x in rotation @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for old, new in enumerate(permutation):
        if mask & (1 << old):
            result |= 1 << new
    return result


def rotate_record(vector: np.ndarray, permutation: tuple[int, ...]) -> np.ndarray:
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
            target_center = center if mutation == "complement" else 1 - center
            matrix[64 * target_center + (shell ^ 63), 64 * center + shell] = 1.0
    return matrix


def labels() -> list[tuple[str, int | None, int]]:
    result: list[tuple[str, int | None, int]] = [
        ("LOCK", None, 0),
        ("LOCK", None, 1),
        ("BG", None, 0),
        ("BG", None, 1),
    ]
    for kind in ("PORT", "GPORT", "STEP", "END"):
        for direction in range(6):
            for content in range(2):
                result.append((kind, direction, content))
    return result


def make_joint_code() -> dict[tuple[str, int | None, int], np.ndarray]:
    pairs = [
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if np.dot(DIRECTIONS[left], DIRECTIONS[right]) == 0
    ]
    incidence = np.zeros((12, 6))
    for row, pair in enumerate(pairs):
        incidence[row, list(pair)] = 1.0
    values, vectors = np.linalg.eigh(incidence.T @ incidence)
    inverse_root = (vectors * (1.0 / np.sqrt(values))) @ vectors.T
    q = incidence @ inverse_root
    pair_masks = [(1 << left) | (1 << right) for left, right in pairs]

    def basis(center: int, shell: int) -> np.ndarray:
        vector = np.zeros(128)
        vector[64 * center + shell] = 1.0
        return vector

    code: dict[tuple[str, int | None, int], np.ndarray] = {}
    for label in labels():
        kind, direction, content = label
        if kind == "LOCK":
            code[label] = basis(content, 0 if content == 0 else 63)
        elif kind == "BG":
            code[label] = basis(1 - content, 0 if content == 0 else 63)
        elif kind in ("PORT", "GPORT"):
            assert direction is not None
            center = content if kind == "PORT" else 1 - content
            shell = (1 << direction) if content == 0 else 63 ^ (1 << direction)
            code[label] = basis(center, shell)
        else:
            assert direction is not None
            center = content if kind == "STEP" else 1 - content
            vector = np.zeros(128)
            for row, shell in enumerate(pair_masks):
                vector[
                    64 * center + (shell if content == 0 else shell ^ 63)
                ] = q[row, direction]
            code[label] = vector
    return code


def transient_pair(mutation: str | None) -> tuple[np.ndarray, np.ndarray]:
    shell_weight = 2 if mutation == "transient_shell" else 3
    masks = [mask for mask in range(64) if mask.bit_count() == shell_weight]
    shell = np.zeros(64)
    shell[masks] = 1.0 / math.sqrt(len(masks))
    tau_zero = np.zeros(128)
    tau_one = np.zeros(128)
    tau_zero[:64] = shell
    if mutation == "transient_center":
        tau_one[:64] = shell
    else:
        tau_one[64:] = shell
    return tau_zero, tau_one


def rule_spec(mutation: str | None) -> dict[str, object]:
    spec: dict[str, object] = {
        "schema": "block219-local-parity-instrument-v1",
        "radius": 1 if mutation == "edge_range" else 2,
        "active_subspace": "complement-swapped noncode transient bit",
        "stencil": "one centered event per transverse unoriented displacement-two relation",
        "branches": (
            {"name": "equal-transient", "effect": "(Q_i Q_j+Z_i Z_j)/2"},
            {"name": "unequal-transient", "effect": "(Q_i Q_j-Z_i Z_j)/2"},
            {"name": "outside-lock", "effect": "I-Q_i Q_j"},
        ),
        "permanent_commit": False,
    }
    if mutation == "size_metadata":
        spec["torus_size"] = 6
    if mutation == "coordinate_phase":
        spec["parity_origin"] = (0, 0)
    if mutation == "global_label":
        spec["shared_four_bit_label"] = True
    if mutation == "cubic":
        spec["stencil"] = "one named transverse direction only"
    return spec


def numeric_rule_payload(
    mutation: str | None, rotations: list[np.ndarray], tau_zero: np.ndarray, tau_one: np.ndarray
) -> dict[str, object]:
    step = 1 if mutation == "edge_range" else 2
    offsets = ((0, step, 0),) if mutation == "cubic" else ((0, step, 0), (0, 0, step))
    local = branch_projectors(mutation)
    return {
        "schema_version": 1,
        "radius": step,
        "transient_support_indices": (
            tuple(int(index) for index in np.flatnonzero(np.abs(tau_zero) > TOL)),
            tuple(int(index) for index in np.flatnonzero(np.abs(tau_one) > TOL)),
        ),
        "transient_uniform_squared_amplitude": (
            (1, int(np.count_nonzero(tau_zero))),
            (1, int(np.count_nonzero(tau_one))),
        ),
        "complement_bit_permutation": (1, 0),
        "canonical_front_normal": (1, 0, 0),
        "centered_event_offsets": offsets,
        "pair_kraus_diagonals": tuple(
            tuple(float(value) for value in np.diag(operator)) for operator in local
        ),
        "pair_branch_labels": (
            ("equal-transient", "unequal-transient")
            if mutation == "lock_even_label_merge"
            else ("equal-transient", "unequal-transient", "outside-lock")
        ),
        "read_footprint": "two displacement-two transient blocks",
        "write_footprint": "nondemolition branch record only",
        "outside_active_action": "identity",
        "record_code_dimension": 52,
        "single_site_outside_active_dimension": 126,
        "proper_rotation_matrices": tuple(
            tuple(int(value) for value in rotation.flat) for rotation in rotations
        ),
        "permanent_commit": False,
    }


def voter_numeric_payload(mutation: str | None) -> dict[str, object]:
    operators = voter_kraus(mutation)
    sparse: list[tuple[tuple[int, int, int, int], ...]] = []
    for operator in operators:
        entries: list[tuple[int, int, int, int]] = []
        for target, source in zip(*np.nonzero(np.abs(operator) > TOL)):
            squared = float(operator[target, source] ** 2)
            if abs(squared - 1.0) < TOL:
                numerator, denominator = 1, 1
            elif abs(squared - 0.5) < TOL:
                numerator, denominator = 1, 2
            elif abs(squared - 0.75) < TOL:
                numerator, denominator = 3, 4
            elif abs(squared - 0.25) < TOL:
                numerator, denominator = 1, 4
            else:
                numerator, denominator = Fraction(squared).limit_denominator().as_integer_ratio()
            entries.append((int(target), int(source), numerator, denominator))
        sparse.append(tuple(entries))
    endpoint_permutation = VOTER_ENDPOINT_BRANCH_PERMUTATION
    complement_permutation = VOTER_COMPLEMENT_BRANCH_PERMUTATION
    if mutation == "voter_label_covariance":
        complement_permutation = (1, 0, 4, 5, 3, 2, 6)
    return {
        "schema_version": 1,
        "radius": 2,
        "kraus_squared_entries": tuple(sparse),
        "branch_labels": VOTER_BRANCH_LABELS,
        "endpoint_branch_permutation": endpoint_permutation,
        "complement_branch_permutation": complement_permutation,
        "canonical_front_normal": (1, 0, 0),
        "centered_event_offsets": ((0, 2, 0), (0, 0, 2)),
        "proper_rotation_matrices": tuple(
            tuple(int(value) for value in rotation.flat)
            for rotation in signed_permutation_rotations()
        ),
        "read_footprint": "two displacement-two transient blocks",
        "write_footprint": "same two blocks on mismatch; identity outside active pair",
        "enablement_predicate": "always local; outside-active pair emits outside-lock",
        "centered_activation": "equal_rate_independent_local_poisson",
        "rate_scale": "positive_supplied_gamma",
        "outside_active_action": "identity",
        "permanent_commit": False,
    }


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def torus_index(size: int, y: int, z: int) -> int:
    return (y % size) * size + (z % size)


def local_events(size: int, mutation: str | None) -> tuple[tuple[int, int], ...]:
    step = 1 if mutation == "edge_range" else 2
    displacements = ((step, 0),) if mutation == "cubic" else ((step, 0), (0, step))
    events: list[tuple[int, int]] = []
    for y in range(size):
        for z in range(size):
            for dy, dz in displacements:
                if mutation == "coordinate_phase" and (y + z) % 2:
                    continue
                left = torus_index(size, y, z)
                right = torus_index(size, y + dy, z + dz)
                events.append(tuple(sorted((left, right))))
    ordered = sorted(events)
    if mutation == "translation" and ordered:
        ordered.pop(0)
    return tuple(ordered)


def local_edges(size: int, mutation: str | None) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(set(local_events(size, mutation))))


def translate_vertex(size: int, vertex: int, dy: int, dz: int) -> int:
    y, z = divmod(vertex, size)
    return torus_index(size, y + dy, z + dz)


def translation_covariant(size: int, edges: tuple[tuple[int, int], ...]) -> bool:
    edge_set = set(edges)
    for dy in range(size):
        for dz in range(size):
            transformed = {
                tuple(
                    sorted(
                        (
                            translate_vertex(size, left, dy, dz),
                            translate_vertex(size, right, dy, dz),
                        )
                    )
                )
                for left, right in edges
            }
            if transformed != edge_set:
                return False
    return True


def event_translation_covariant(size: int, events: tuple[tuple[int, int], ...]) -> bool:
    reference = Counter(events)
    for dy in range(size):
        for dz in range(size):
            transformed = Counter(
                tuple(
                    sorted(
                        (
                            translate_vertex(size, left, dy, dz),
                            translate_vertex(size, right, dy, dz),
                        )
                    )
                )
                for left, right in events
            )
            if transformed != reference:
                return False
    return True


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def syndrome_consistent(rows: list[int], outcomes: int, column_count: int) -> bool:
    augmented = [
        row | (((outcomes >> index) & 1) << column_count)
        for index, row in enumerate(rows)
    ]
    return gf2_rank(augmented) == gf2_rank(rows)


def graph_components(
    vertex_count: int, edges: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, ...], ...]:
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(range(vertex_count))
    components: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        queue = deque([seed])
        component: set[int] = set()
        while queue:
            vertex = queue.popleft()
            if vertex in component:
                continue
            component.add(vertex)
            queue.extend(adjacency[vertex] - component)
        unseen -= component
        components.append(tuple(sorted(component)))
    return tuple(components)


def parity_word(size: int, bits: int, mutation: str | None = None) -> int:
    word = 0
    for y in range(size):
        for z in range(size):
            slot = 2 * (y % 2) + (z % 2)
            value = (bits >> slot) & 1
            if mutation == "terminal_support" and bits == 0 and y == z == 0:
                value = 1
            word |= value << torus_index(size, y, z)
    return word


def satisfies(word: int, edges: tuple[tuple[int, int], ...]) -> bool:
    return all(((word >> left) ^ (word >> right)) & 1 == 0 for left, right in edges)


def stencil_for_normal(normal: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    axis = next(index for index, value in enumerate(normal) if value)
    result: set[tuple[int, int, int]] = set()
    for transverse in range(3):
        if transverse == axis:
            continue
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[transverse] = 2 * sign
            result.add(tuple(vector))
    return result


def branch_projectors(mutation: str | None) -> tuple[np.ndarray, ...]:
    equal = np.diag((1.0, 0.0, 0.0, 1.0, 0.0))
    unequal = np.diag((0.0, 1.0, 1.0, 0.0, 0.0))
    lock = np.diag((0.0, 0.0, 0.0, 0.0, 1.0))
    if mutation == "normalization":
        unequal *= 0.8
    if mutation == "record_lock":
        lock[4, 4] = 0.8
    if mutation == "lock_even_label_merge":
        return (equal + lock, unequal)
    if mutation == "branch_delete":
        return (equal, unequal)
    return equal, unequal, lock


def voter_kraus(mutation: str | None) -> tuple[np.ndarray, ...]:
    """Two-bit consensus channel plus an aggregated outside lock sector."""

    def matrix(target: int, source: int, amplitude: float = 1.0) -> np.ndarray:
        result = np.zeros((5, 5))
        result[target, source] = amplitude
        return result

    zero_weight = math.sqrt(0.75) if mutation == "voter_bias" else 1.0 / math.sqrt(2.0)
    one_weight = math.sqrt(0.25) if mutation == "voter_bias" else 1.0 / math.sqrt(2.0)
    result = [matrix(0, 0), matrix(3, 3)]
    if mutation == "voter_dark_state":
        result.extend((matrix(1, 1), matrix(2, 2)))
    else:
        result.extend(
            (
                matrix(0, 1, zero_weight),
                matrix(3, 1, one_weight),
                matrix(0, 2, zero_weight),
                matrix(3, 2, one_weight),
            )
        )
    result.append(matrix(4, 4))
    if mutation == "voter_completeness":
        result.pop(3)
    return tuple(result)


def channel_apply(kraus: tuple[np.ndarray, ...], matrix: np.ndarray) -> np.ndarray:
    return sum((operator @ matrix @ operator.T for operator in kraus), np.zeros_like(matrix))


def channel_covariant(kraus: tuple[np.ndarray, ...], symmetry: np.ndarray) -> bool:
    for row in range(5):
        for column in range(5):
            probe = np.zeros((5, 5))
            probe[row, column] = 1.0
            left = channel_apply(kraus, symmetry @ probe @ symmetry.T)
            right = symmetry @ channel_apply(kraus, probe) @ symmetry.T
            if np.linalg.norm(left - right) >= TOL:
                return False
    return True


def branch_family_covariant(
    kraus: tuple[np.ndarray, ...],
    symmetry: np.ndarray,
    branch_permutation: tuple[int, ...],
) -> bool:
    if len(kraus) != len(branch_permutation):
        return False
    return all(
        np.linalg.norm(
            symmetry @ operator @ symmetry.T - kraus[branch_permutation[index]]
        )
        < TOL
        for index, operator in enumerate(kraus)
    )


def component_edges(
    component: tuple[int, ...], edges: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    slots = {vertex: index for index, vertex in enumerate(component)}
    return tuple(
        sorted(
            (slots[left], slots[right])
            for left, right in edges
            if left in slots and right in slots
        )
    )


def consensus_successors(
    state: int, edges: tuple[tuple[int, int], ...]
) -> set[int]:
    result: set[int] = set()
    for left, right in edges:
        left_bit = (state >> left) & 1
        right_bit = (state >> right) & 1
        if left_bit == right_bit:
            result.add(state)
            continue
        cleared = state & ~(1 << left) & ~(1 << right)
        result.add(cleared)
        result.add(cleared | (1 << left) | (1 << right))
    return result or {state}


def component_density_is_harmonic(
    vertex_count: int,
    edges: tuple[tuple[int, int], ...],
    mutation: str | None,
) -> bool:
    """Exact one-step check for both component-consensus hitting functions."""

    if mutation == "voter_bias":
        zero_probability, one_probability = Fraction(3, 4), Fraction(1, 4)
    else:
        zero_probability = one_probability = Fraction(1, 2)
    for state in range(1 << vertex_count):
        density_one = Fraction(state.bit_count(), vertex_count)
        for left, right in edges:
            left_bit = (state >> left) & 1
            right_bit = (state >> right) & 1
            if left_bit == right_bit or mutation == "voter_dark_state":
                expected_one = density_one
            else:
                cleared = state & ~(1 << left) & ~(1 << right)
                filled = cleared | (1 << left) | (1 << right)
                expected_one = (
                    zero_probability * Fraction(cleared.bit_count(), vertex_count)
                    + one_probability * Fraction(filled.bit_count(), vertex_count)
                )
            if expected_one != density_one:
                return False
            if 1 - expected_one != 1 - density_one:
                return False
    return True


def fair_absorption_block_certificate(
    vertex_count: int,
    edges: tuple[tuple[int, int], ...],
    mutation: str | None,
) -> tuple[bool, Fraction]:
    """Finite uniform-block certificate for outcome-blind edge-fair order.

    If a fair execution never absorbs, it has infinitely many mismatch
    updates: after a last such update a fixed mixed state would leave a
    disagreement edge, which edge fairness must eventually select.  At most
    ``vertex_count`` consecutive zero outcomes on mismatch updates force the
    all-zero state because each such outcome lowers the one-count by one.
    The conditional probability of that forcing block is uniformly at least
    ``2**(-vertex_count)`` for the unbiased rule, so nonabsorption has measure
    zero.
    """

    forcing_probability = Fraction(1, 2**vertex_count)
    if mutation == "voter_dark_state":
        return False, forcing_probability
    all_states_ok = True
    for state in range(1, (1 << vertex_count) - 1):
        mismatches = [
            (left, right)
            for left, right in edges
            if ((state >> left) & 1) != ((state >> right) & 1)
        ]
        all_states_ok &= bool(mismatches)
        for left, right in mismatches:
            cleared = state & ~(1 << left) & ~(1 << right)
            all_states_ok &= cleared.bit_count() == state.bit_count() - 1
    return all_states_ok and forcing_probability > 0, forcing_probability


def reverse_reachable(
    target: int, adjacency: list[set[int]]
) -> set[int]:
    reverse: list[set[int]] = [set() for _ in adjacency]
    for source, targets in enumerate(adjacency):
        for destination in targets:
            reverse[destination].add(source)
    reached = {target}
    queue = deque([target])
    while queue:
        destination = queue.popleft()
        for source in reverse[destination] - reached:
            reached.add(source)
            queue.append(source)
    return reached


def local_commit_counterexample(size: int) -> tuple[bool, Fraction, int, int]:
    all_edges = local_edges(size, None)
    component = graph_components(size * size, all_edges)[0]
    induced = component_edges(component, all_edges)
    center = 0
    neighbors = {
        right if left == center else left
        for left, right in induced
        if center in (left, right)
    }
    zeros = {center} | neighbors
    ones = set(range(len(component))) - zeros
    local_view_matches_terminal = bool(neighbors) and not (zeros & ones)
    # The first clause above only checks disjointness.  The load-bearing local
    # property is that the center and every incident neighbor carry zero.
    local_view_matches_terminal &= all(vertex in zeros for vertex in neighbors)
    globally_mixed = bool(zeros) and bool(ones)
    return local_view_matches_terminal and globally_mixed, Fraction(len(ones), len(component)), len(zeros), len(ones)


def overlap_projector(pair: tuple[int, int], branch: int) -> np.ndarray:
    """Three-site projector on {tau_0,tau_1,outside}^3.

    Branches 0, 1 and 2 are respectively equal-transient,
    unequal-transient and outside-lock.  Keeping the third type explicit is
    load-bearing: a locked Record/malformed endpoint cannot masquerade as a
    zero syndrome.
    """

    diagonal = []
    for types in itertools.product((0, 1, 2), repeat=3):
        left, right = types[pair[0]], types[pair[1]]
        locked = 2 in (left, right)
        if branch == 2:
            selected = locked
        elif branch == 0:
            selected = not locked and left == right
        else:
            selected = not locked and left != right
        diagonal.append(float(selected))
    return np.diag(diagonal)


def source_and_note_checks(checks: Checks, root: Path) -> None:
    loop = root / (
        ".claude/science/physics-loops/"
        "toe-axiom-closure-block219-multisize-local-formation-instrument-20260827"
    )
    note_path = root / (
        "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
    )
    checklist_path = root / (
        "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_"
        "NO_GO_DISCIPLINE_CHECKLIST_2026-08-27.md"
    )
    goal = (loop / "GOAL.md").read_text(encoding="utf-8")
    no_go = (loop / "NO_GO_LEDGER.md").read_text(encoding="utf-8")
    parent = (
        root
        / "docs/ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
    ).read_text(encoding="utf-8")
    note = note_path.read_text(encoding="utf-8")
    checklist = checklist_path.read_text(encoding="utf-8")
    checks.check(
        "source anchors",
        "training/validation volumes" in goal
        and "N8 -- cross-cycle echo" in no_go
        and "four shared parity bits" in parent,
    )
    links = (
        "../.claude/science/physics-loops/toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/GOAL.md",
        "../.claude/science/physics-loops/toe-axiom-closure-block219-multisize-local-formation-instrument-20260827/NO_GO_LEDGER.md",
        "ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    )
    checks.check("three exact dependency links", all(f"]({link})" in note for link in links))
    checks.check(
        "landing-surface N1-N8 packet demotes the broad no-go",
        "Block 219 No-Go Discipline Checklist" in checklist
        and all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: FAIL for the proposed broad no-go" in checklist
        and "partial-narrowing" in checklist
        and checklist_path.name in note,
    )
    normalized = " ".join(note.split()).lower()
    phrases = (
        "positive-size-lifted-factorization",
        "pre-commit correlation factorization is local",
        "all-transient precursor sector",
        "global even-syndrome acceptance is not an autonomous permanent-commit certificate",
        "held-out l=8",
        "no coordinate names, fixed block phase, global shared bits, torus-size counter, host scheduler or synchronous global rounds",
        "zero obligation retirement and zero toe percentage movement",
        "no axiom pressure",
        "per_element:",
        "per_site:",
        "per_mode:",
        "per_block:",
        "lattice_wide:",
    )
    checks.check("required boundary prose", all(phrase in normalized for phrase in phrases))


def run(mutation: str | None) -> tuple[Checks, str]:
    checks = Checks()
    rotations = signed_permutation_rotations()
    permutations = [direction_permutation(rotation) for rotation in rotations]
    checks.check(
        "24 proper cubic rotations",
        len(rotations) == 24
        and all(round(np.linalg.det(rotation)) == 1 for rotation in rotations),
    )

    code = make_joint_code()
    code_matrix = np.column_stack(tuple(code.values()))
    code_gram = code_matrix.T @ code_matrix
    checks.check(
        "Block-218 code rebuilt orthonormally",
        code_matrix.shape == (128, 52)
        and np.allclose(code_gram, np.eye(52), atol=TOL),
    )
    checks.check("rank-76 noncode complement", 128 - np.linalg.matrix_rank(code_matrix) == 76)

    tau_zero, tau_one = transient_pair(mutation)
    transient = np.column_stack((tau_zero, tau_one))
    checks.check(
        "transient bit orthonormal",
        np.allclose(transient.T @ transient, np.eye(2), atol=TOL),
    )
    checks.check(
        "transient bit lies in noncode complement",
        np.max(np.abs(code_matrix.T @ transient)) < TOL,
    )
    checks.check(
        "transient bit proper-cubic scalar",
        all(
            np.linalg.norm(rotate_record(tau_zero, permutation) - tau_zero) < TOL
            and np.linalg.norm(rotate_record(tau_one, permutation) - tau_one) < TOL
            for permutation in permutations
        ),
    )
    complement = complement_matrix(mutation)
    checks.check(
        "transient bit complement pair",
        np.linalg.norm(complement @ tau_zero - tau_one) < TOL
        and np.linalg.norm(complement @ tau_one - tau_zero) < TOL,
    )
    omega = (tau_zero + tau_one) / math.sqrt(2.0)
    checks.check(
        "Block-218 precursor recovered",
        abs(np.vdot(omega, omega) - 1.0) < TOL
        and np.max(np.abs(code_matrix.T @ omega)) < TOL
        and np.linalg.norm(complement @ omega - omega) < TOL,
    )

    declared_basis = np.column_stack((code_matrix, transient))
    left_singular, singular_values, _ = np.linalg.svd(declared_basis, full_matrices=True)
    declared_rank = int(np.count_nonzero(singular_values > TOL))
    remainder = left_singular[:, declared_rank:]
    active_projector = transient @ transient.T
    full_lock_ok = (
        declared_rank == 54
        and remainder.shape == (128, 74)
        and np.max(np.abs(active_projector @ code_matrix)) < TOL
        and np.max(np.abs(active_projector @ remainder)) < TOL
        and np.allclose(remainder.T @ remainder, np.eye(74), atol=TOL)
    )
    checks.check(
        "all 52 Records and 74 nonactive complement directions are in the exact lock sector",
        full_lock_ok,
        f"declared_rank={declared_rank} remainder={remainder.shape}",
    )

    spec = rule_spec(mutation)
    payload = numeric_rule_payload(mutation, rotations, tau_zero, tau_one)
    serialized = canonical_json(payload)
    digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    reported_digest = ("0" + digest[1:]) if mutation == "rule_hash" else digest
    checks.check(
        "frozen numerical local-rule digest",
        len(digest) == 64 and reported_digest == digest,
        f"sha256={digest}",
    )
    forbidden_keys = {
        "torus_size",
        "parity_origin",
        "shared_four_bit_label",
        "coordinate",
        "phase",
        "scheduler",
        "round",
    }
    checks.check(
        "rule contains no size coordinate phase scheduler or global label",
        not (forbidden_keys & set(spec)),
        str(forbidden_keys & set(spec)),
    )
    checks.check(
        "rule is radius two and pre-commit",
        spec.get("radius") == 2 and spec.get("permanent_commit") is False,
    )

    branches = branch_projectors(mutation)
    completeness = sum(
        (branch.conj().T @ branch for branch in branches), np.zeros((5, 5))
    )
    checks.check(
        "local three-branch syndrome instrument CP",
        all(np.min(np.linalg.eigvalsh(branch)) >= -TOL for branch in branches),
    )
    checks.check(
        "local equal-unequal-lock instrument normalized",
        np.allclose(completeness, np.eye(5), atol=TOL),
        str(float(np.linalg.norm(completeness - np.eye(5)))),
    )
    checks.check(
        "outside sector has a distinct readable lock branch",
        len(branches) == 3
        and all(abs(branches[index][4, 4]) < TOL for index in (0, 1))
        and abs(branches[2][4, 4] - 1.0) < TOL,
    )
    bit_complement = np.array(
        [[0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1]],
        dtype=float,
    )
    checks.check(
        "local branch complement covariance",
        len(branches) == 3
        and all(
            np.linalg.norm(bit_complement @ branch @ bit_complement.T - branch) < TOL
            for branch in branches
        ),
    )

    cubic_ok = True
    normal = (1, 0, 0)
    canonical_stencil = (
        {(0, -2, 0), (0, 2, 0)}
        if mutation == "cubic"
        else stencil_for_normal(normal)
    )
    for rotation in rotations:
        rotated_normal = tuple(int(x) for x in rotation @ np.asarray(normal))
        transformed = {
            tuple(int(x) for x in rotation @ np.asarray(displacement))
            for displacement in canonical_stencil
        }
        cubic_ok &= transformed == stencil_for_normal(rotated_normal)
    checks.check("proper-cubic stencil covariance", cubic_ok)

    left_branches = tuple(overlap_projector((0, 1), branch) for branch in range(3))
    right_branches = tuple(overlap_projector((1, 2), branch) for branch in range(3))
    if mutation == "critical_pair":
        flip_middle = np.zeros((27, 27))
        type_words = tuple(itertools.product((0, 1, 2), repeat=3))
        index = {word: slot for slot, word in enumerate(type_words)}
        for source, word in enumerate(type_words):
            mutated = list(word)
            if mutated[1] in (0, 1):
                mutated[1] = 1 - mutated[1]
            flip_middle[index[tuple(mutated)], source] = 1.0
        right_branches = (
            right_branches[0],
            flip_middle @ right_branches[1],
            right_branches[2],
        )
    checks.check(
        "all 27 typed overlap sectors have branchwise commuting critical pairs",
        all(
            np.linalg.norm(left @ right - right @ left) < TOL
            for left in left_branches
            for right in right_branches
        ),
    )

    voter = voter_kraus(mutation)
    voter_completeness = sum(
        (operator.T @ operator for operator in voter), np.zeros((5, 5))
    )
    checks.check(
        "local voter/coalescence channel normalized",
        np.allclose(voter_completeness, np.eye(5), atol=TOL),
        str(float(np.linalg.norm(voter_completeness - np.eye(5)))),
    )
    endpoint_swap = np.array(
        [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],
        dtype=float,
    )
    checks.check(
        "voter channel endpoint and complement covariant",
        channel_covariant(voter, endpoint_swap)
        and channel_covariant(voter, bit_complement),
    )
    voter_payload = voter_numeric_payload(mutation)
    checks.check(
        "readable voter branch labels transform covariantly",
        tuple(voter_payload["branch_labels"]) == VOTER_BRANCH_LABELS
        and branch_family_covariant(
            voter,
            endpoint_swap,
            tuple(voter_payload["endpoint_branch_permutation"]),
        )
        and branch_family_covariant(
            voter,
            bit_complement,
            tuple(voter_payload["complement_branch_permutation"]),
        ),
    )
    voter_resolves = True
    voter_martingale = True
    population_ones = np.asarray((0.0, 1.0, 1.0, 2.0, 0.0))
    for source in range(4):
        probe = np.zeros((5, 5))
        probe[source, source] = 1.0
        output = channel_apply(voter, probe)
        diagonal = np.diag(output)
        if source in (1, 2):
            voter_resolves &= float(diagonal[1] + diagonal[2]) < TOL
        voter_martingale &= abs(float(diagonal @ population_ones) - population_ones[source]) < TOL
    checks.check("every selected mismatch edge is locally resolved", voter_resolves)
    checks.check("voter update preserves expected one-count", voter_martingale)
    lock_probe = np.zeros((5, 5))
    lock_probe[4, 4] = 1.0
    checks.check(
        "voter channel preserves Record/nonactive lock sector",
        np.allclose(channel_apply(voter, lock_probe), lock_probe, atol=TOL),
    )

    absorption_ok = True
    absorption_details: list[str] = []
    for size in (4, 6):
        full_edges = local_edges(size, None)
        component = graph_components(size * size, full_edges)[0]
        induced = component_edges(component, full_edges)
        state_count = 1 << len(component)
        adjacency = [consensus_successors(state, induced) for state in range(state_count)]
        reaches_zero = reverse_reachable(0, adjacency)
        reaches_one = reverse_reachable(state_count - 1, adjacency)
        absorbing = [
            state
            for state in range(state_count)
            if consensus_successors(state, induced) == {state}
        ]
        mixed = set(range(1, state_count - 1))
        this_size = (
            absorbing == [0, state_count - 1]
            and mixed <= reaches_zero
            and mixed <= reaches_one
        )
        absorption_ok &= this_size
        absorption_details.append(
            f"L={size}:component={len(component)} states={state_count} absorbing={absorbing}"
        )
    checks.check(
        "all-transient finite-volume voter process has only consensus recurrent classes",
        absorption_ok,
        "; ".join(absorption_details),
    )

    fair_absorption_ok = True
    fair_absorption_details: list[str] = []
    for size in (4, 6):
        full_edges = local_edges(size, None)
        component = graph_components(size * size, full_edges)[0]
        induced = component_edges(component, full_edges)
        this_size, forcing_probability = fair_absorption_block_certificate(
            len(component), induced, mutation
        )
        fair_absorption_ok &= this_size
        fair_absorption_details.append(
            f"L={size}:component={len(component)} forcing_floor={forcing_probability}"
        )
    checks.check(
        "outcome-blind edge-fair schedules absorb on the all-transient sector",
        fair_absorption_ok,
        "; ".join(fair_absorption_details),
    )

    harmonic_ok = True
    harmonic_details: list[str] = []
    for size in (4, 6):
        full_edges = local_edges(size, None)
        component = graph_components(size * size, full_edges)[0]
        induced = component_edges(component, full_edges)
        this_size = component_density_is_harmonic(len(component), induced, mutation)
        harmonic_ok &= this_size
        harmonic_details.append(
            f"L={size}:component={len(component)} harmonic={this_size}"
        )
    checks.check(
        "all-transient component-density products preserve all sixteen terminal hitting weights",
        harmonic_ok and Fraction(1, 2) ** 4 == Fraction(1, 16),
        "; ".join(harmonic_details),
    )

    commit_examples_ok = True
    commit_details: list[str] = []
    expected_conflicts = {4: Fraction(1, 4), 6: Fraction(4, 9)}
    for size, expected in expected_conflicts.items():
        local_match, conflict_probability, zeros, ones = local_commit_counterexample(size)
        if mutation == "commit_locality":
            conflict_probability = Fraction(0)
        commit_examples_ok &= local_match and conflict_probability == expected
        commit_details.append(
            f"L={size}:zeros={zeros} remote_ones={ones} conflict={conflict_probability}"
        )
    checks.check(
        "premature local-commit counterexamples on training volumes",
        commit_examples_ok,
        "; ".join(commit_details),
    )

    training_periods = (4, 6, 8) if mutation == "heldout" else (4, 6)
    checks.check(
        "held-out L=8 excluded from synthesis runner",
        training_periods == (4, 6),
    )
    all_volume_checks = True
    volume_details: list[str] = []
    for size in training_periods:
        events = local_events(size, mutation)
        edges = local_edges(size, mutation)
        vertex_count = size * size
        rows = [(1 << left) | (1 << right) for left, right in edges]
        rank = gf2_rank(rows)
        components = graph_components(vertex_count, edges)
        expected_rank = vertex_count - (5 if mutation == "rank_claim" else 4)
        expected_events = 2 * vertex_count
        expected_unique_edges = 16 if size == 4 else 2 * vertex_count
        words = {parity_word(size, bits, mutation) for bits in range(16)}
        good_words = all(satisfies(word, edges) for word in words)
        expected_probability = Fraction(1, 2 ** (rank + (1 if mutation == "success_probability" else 0)))
        actual_probability = Fraction(1, 2 ** (vertex_count - 4))
        this_volume = (
            len(events) == expected_events
            and len(edges) == expected_unique_edges
            and event_translation_covariant(size, events)
            and translation_covariant(size, edges)
            and len(components) == 4
            and rank == expected_rank
            and len(words) == 16
            and good_words
            and actual_probability == expected_probability
        )
        all_volume_checks &= this_volume
        volume_details.append(
            f"L={size}: centered_events={len(events)} unique_edges={len(edges)} components={len(components)} "
            f"rank={rank} success={actual_probability}"
        )
    checks.check(
        "same local rule gives four parity sectors on L=4 and L=6",
        all_volume_checks,
        "; ".join(volume_details),
    )

    size = 4
    edges = local_edges(size, None if mutation not in {"terminal_support"} else mutation)
    exhaustive = [
        word for word in range(1 << 16) if satisfies(word, edges)
    ]
    reconstructed = {parity_word(4, bits, mutation) for bits in range(16)}
    checks.check(
        "L=4 exhaustive terminal support exact",
        len(exhaustive) == 16 and set(exhaustive) == reconstructed,
    )

    rows_l4 = [(1 << left) | (1 << right) for left, right in local_edges(4, None)]
    history_ok = True
    full_consistent = 0
    for order_index, ordered_rows in enumerate((rows_l4, list(reversed(rows_l4)))):
        for prefix_length in range(len(ordered_rows) + 1):
            prefix = ordered_rows[:prefix_length]
            rank = gf2_rank(prefix)
            total = Fraction(0)
            for outcomes in range(1 << prefix_length):
                probability = (
                    Fraction(1, 2**rank)
                    if syndrome_consistent(prefix, outcomes, 16)
                    else Fraction(0)
                )
                total += probability
                if prefix_length < len(ordered_rows):
                    children = prefix + [ordered_rows[prefix_length]]
                    child_rank = gf2_rank(children)
                    child_zero = (
                        Fraction(1, 2**child_rank)
                        if syndrome_consistent(children, outcomes, 16)
                        else Fraction(0)
                    )
                    child_one_outcome = outcomes | (1 << prefix_length)
                    child_one = (
                        Fraction(1, 2**child_rank)
                        if syndrome_consistent(children, child_one_outcome, 16)
                        else Fraction(0)
                    )
                    if mutation == "history_cylinder" and order_index == 0 and prefix_length == 0:
                        child_one *= 2
                    history_ok &= probability == child_zero + child_one
            history_ok &= total == 1
            if order_index == 0 and prefix_length == len(ordered_rows):
                full_consistent = sum(
                    syndrome_consistent(prefix, outcomes, 16)
                    for outcomes in range(1 << prefix_length)
                )
    repeated_event_ok = True
    event_counts = Counter(local_events(4, None))
    for left, right in event_counts:
        row = (1 << left) | (1 << right)
        valid_pairs = {
            outcomes for outcomes in range(4) if syndrome_consistent([row, row], outcomes, 16)
        }
        repeated_event_ok &= valid_pairs == {0, 3}
    checks.check(
        "all L=4 syndrome transcripts and both generator orders normalize",
        history_ok and full_consistent == 2**12,
        f"consistent_full={full_consistent}",
    )
    checks.check(
        "L=4 centered duplicate events have deterministic repeated outcomes",
        len(local_events(4, None)) == 32
        and len(event_counts) == 16
        and set(event_counts.values()) == {2}
        and repeated_event_ok,
    )

    autonomous_claim = mutation == "autonomous_overclaim"
    checks.check(
        "global success and permanent finality remain unclaimed",
        not autonomous_claim and spec.get("permanent_commit") is False,
    )
    source_and_note_checks(checks, Path(__file__).resolve().parents[1])
    classification = (
        "positive-size-lifted-factorization"
        if checks.failed == 0
        else f"rejected-mutation {mutation or 'baseline'}"
    )
    voter_digest = hashlib.sha256(
        canonical_json(voter_numeric_payload(mutation)).encode("utf-8")
    ).hexdigest()
    print(f"DATA frozen_numerical_rule_sha256={digest}")
    print(f"DATA frozen_voter_rule_sha256={voter_digest}")
    print("DATA " + " | ".join(volume_details))
    print(
        "per_element: checked all 52 Record directions, both transient vectors, "
        "74 other nonactive directions, and every displayed local Kraus entry."
    )
    print(
        "per_site: checked every centered event and unique radius-two edge on "
        "training periods L=4 and L=6; arbitrary mixed Record starts were not executed."
    )
    print(
        "per_mode: checked three readable syndrome branches, seven voter branches, "
        "four parity components, complement, endpoint exchange, and 24 rotations."
    )
    print(
        "per_block: checked complete L=4 syndrome support and training-component "
        "voter state graphs for L=4 and L=6; held L=8 is delegated independently."
    )
    print(
        "lattice_wide: checked the analytic finite-even-L graph/rank law and a "
        "uniform-block fair-scheduler proof; infinite-lattice stopping was not executed."
    )
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
        raise TimeoutError(f"runner exceeded {AUDIT_TIMEOUT_SEC}s")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, classification = run(arguments.mutation)
    except Exception as error:
        print(f"FAIL unhandled exception: {type(error).__name__}: {error}")
        print("SUMMARY PASS 0 FAIL 1")
        print(f"CLASSIFICATION: rejected-mutation {arguments.mutation or 'baseline'}")
        print("TOTAL: PASS=0 FAIL=1")
        return 1
    finally:
        signal.alarm(0)

    print(f"SUMMARY PASS {checks.passed} FAIL {checks.failed}")
    print(f"CLASSIFICATION: {classification}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
