#!/usr/bin/env python3
"""Cycle 517: adjacent-two-star static order-character preflight.

This bounded runner does not attempt the 245,518,336-branch twelve-cell
census.  It first identifies the exact anticommutation graph of the native
Cycle-311/315 physical gauge terms on two adjacent Cycle-330 stars through
global total number N<=2.  It then derives the smallest exact *static*
factor-order character quotient for that graph and produces physical
singleton-mask witnesses at L=5, held L=6, and all 24 proper-cubic frames.

The result is a preflight for an adjacent-star compiler, not that compiler.
In particular it does not prove a twelve-cell encoding is injective or
isometric, does not construct E or G_physical, and does not synthesize the
local constraints that would exclude invalid role words.

Authority: none.  Audit: unset.  No obstruction or axiom pressure is claimed.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import heapq
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

import physical_cycle515_koszul_frame_bridge_cycle516_2026_07_20 as c516


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "preflight-certificate")
TRAIN_LENGTH = 5
HELD_LENGTH = 6
PATCH_CELL_COUNT = 12
LOCAL_MODE_COUNT = 6
MAX_TOTAL_NUMBER = 2
LOGICAL_DIMENSION = 1 + PATCH_CELL_COUNT * LOCAL_MODE_COUNT + math.comb(
    PATCH_CELL_COUNT * LOCAL_MODE_COUNT, 2
)
EXPECTED_LOGICAL_DIMENSION = 2629
EXPECTED_PROPER_FRAMES = 24
EXPECTED_FRAME_PRODUCTS = 576
EXPECTED_ACYCLIC_ORIENTATIONS = 19_208
EXPECTED_CYCLIC_ORIENTATION_WORDS = 13_560
EXPECTED_ROLE_M2 = 15
EXPECTED_PAIR_CASES = 3964
EXPECTED_PAIR_TESTS_PER_SIZE = math.comb(PATCH_CELL_COUNT, 2) * EXPECTED_PAIR_CASES
EXPECTED_FULL_BRANCHES_PER_SIZE = 245_518_336

RSS_CHECKPOINT_ABORT_CEILING_BYTES = 3_000_000_000
RSS_CHECKPOINT_GUARD_BYTES = 2_850_000_000
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0

CYCLE516_RUNNER = ROOT / "scripts/physical_cycle515_koszul_frame_bridge_cycle516_2026_07_20.py"
CYCLE516_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE515_KOSZUL_FRAME_BRIDGE_CYCLE516_NOTE_2026-07-21.md"
)
CYCLE516_LOG = ROOT / "outputs/physical_cycle515_koszul_frame_bridge_cycle516_attempt4_2026_07_21.log"
CYCLE516_RECEIPT = ROOT / "outputs/physical_cycle515_koszul_frame_bridge_cycle516_attempt4_receipt_2026_07_21.json"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_ORDER_CHARACTER_PREFLIGHT_CYCLE517_NOTE_2026-07-21.md"
)

STRICT_FILE_HASHES = {
    CYCLE516_RUNNER: "3c4318a84c661893932c8d41a90db36445f80cefd092a6a3fffb56cbf8abfa9c",
    CYCLE516_NOTE: "5f32e766fad91a960031bf68dac4ba3b2498b02b5fc4fce9ac1c795e67c23597",
    CYCLE516_LOG: "710673f10229675789ab84abe24d15238f0b9b1674608b0254a77c02860ebcce",
    CYCLE516_RECEIPT: "bfcf92c44e8b651f3866fa017a77ab7462988427d80178da6cbbddbe5d703cbb",
}

# Cell 0 and cell 1 are adjacent star centers.  Cells 2 and 7 are the two
# outer axial leaves; (3,8),...,(6,11) are transverse rung pairs.
PATCH_CELLS = (
    (1, 1, 1),
    (2, 1, 1),
    (0, 1, 1),
    (1, 0, 1),
    (1, 2, 1),
    (1, 1, 0),
    (1, 1, 2),
    (3, 1, 1),
    (2, 0, 1),
    (2, 2, 1),
    (2, 1, 0),
    (2, 1, 2),
)
LEFT_STAR_SEAMS = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6))
RIGHT_STAR_SEAMS = ((0, 1), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11))
UNIQUE_STAR_SEAMS = tuple(dict.fromkeys(LEFT_STAR_SEAMS + RIGHT_STAR_SEAMS))
TRANSVERSE_RUNGS = ((3, 8), (4, 9), (5, 10), (6, 11))
PAULI_EDGES = UNIQUE_STAR_SEAMS + TRANSVERSE_RUNGS
PAULI_EDGE_SET = set(PAULI_EDGES)
ALL_CELL_PAIRS = tuple(combinations(range(PATCH_CELL_COUNT), 2))
EDGE_INDEX = {edge: bit for bit, edge in enumerate(PAULI_EDGES)}
FRAMES = c516.FRAMES
CENTER = np.asarray(PATCH_CELLS[0], dtype=int)
IDENTITY = np.eye(3, dtype=int)
LOCAL_TERM_COUNTS = {0: 2, 1: 60, 2: 30}


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physical conclusion."""


class CertificateFailure(RuntimeError):
    """A failed bounded predicate, never a substrate obstruction."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def last_json(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass
    for line in reversed(content.splitlines()):
        if line.strip().startswith("{"):
            return json.loads(line)
    raise CertificateFailure(f"no JSON payload in {path}")


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def resource_checkpoint(started: float, label: str, projected_bytes: int = 0) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_CHECKPOINT_GUARD_BYTES:
        raise ResourceWall(f"RSS checkpoint guard reached at {label}: {rss}")
    if rss + projected_bytes >= RSS_CHECKPOINT_ABORT_CEILING_BYTES:
        raise ResourceWall(
            f"projected checkpoint ceiling reached at {label}: "
            f"rss={rss}, projected={projected_bytes}"
        )
    if swap_count() != 0:
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "estimated_next_allocation_bytes": projected_bytes,
        "process_swap_count": swap_count(),
    }


def _alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def validate_length(length: int) -> None:
    if length < TRAIN_LENGTH:
        raise ValueError("Cycle517 requires non-aliased L>=5")


def validate_proper_frame(frame: np.ndarray) -> None:
    frame = np.asarray(frame, dtype=int)
    if frame.shape != (3, 3):
        raise ValueError("Cycle517 frame must be 3x3")
    if not np.array_equal(frame.T @ frame, IDENTITY) or round(np.linalg.det(frame)) != 1:
        raise ValueError("Cycle517 accepts only proper-cubic determinant-plus-one frames")


def validate_centers(left: tuple[int, ...], right: tuple[int, ...], length: int) -> None:
    validate_length(length)
    if left == right:
        raise ValueError("Cycle517 requires two distinct centers")
    differences = tuple((right[index] - left[index]) % length for index in range(3))
    nonzero = tuple(value for value in differences if value)
    if len(nonzero) != 1 or nonzero[0] not in (1, length - 1):
        raise ValueError("Cycle517 requires nearest-neighbor adjacent centers")


def rotated_patch(frame: np.ndarray, length: int) -> tuple[tuple[int, int, int], ...]:
    validate_length(length)
    validate_proper_frame(frame)
    cells = tuple(
        tuple(int(value % length) for value in CENTER + frame @ (np.asarray(cell) - CENTER))
        for cell in PATCH_CELLS
    )
    if len(set(cells)) != PATCH_CELL_COUNT:
        raise CertificateFailure(f"aliased Cycle517 patch at L={length}")
    return cells


def nearest_neighbor(first, second, length: int) -> bool:
    differences = tuple((first[axis] - second[axis]) % length for axis in range(3))
    nonzero = tuple(value for value in differences if value)
    return len(nonzero) == 1 and nonzero[0] in (1, length - 1)


def induced_edges(cells, length: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        pair
        for pair in ALL_CELL_PAIRS
        if nearest_neighbor(cells[pair[0]], cells[pair[1]], length)
    )


def geometry_controls() -> dict:
    frame_keys = {tuple(int(value) for value in frame.reshape(-1)) for frame in FRAMES}
    group_failures = 0
    patch_action_failures = 0
    for left in FRAMES:
        for right in FRAMES:
            product = left @ right
            group_failures += tuple(int(value) for value in product.reshape(-1)) not in frame_keys
            direct = tuple(
                tuple(int(value) for value in CENTER + product @ (np.asarray(cell) - CENTER))
                for cell in PATCH_CELLS
            )
            composed = tuple(
                tuple(
                    int(value)
                    for value in CENTER
                    + left @ (CENTER + right @ (np.asarray(cell) - CENTER) - CENTER)
                )
                for cell in PATCH_CELLS
            )
            patch_action_failures += direct != composed

    frame_graph_failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        for frame in FRAMES:
            frame_graph_failures += induced_edges(rotated_patch(frame, length), length) != PAULI_EDGES

    positive_x = np.asarray((1, 0, 0), dtype=int)
    directed_images = Counter(tuple(int(value) for value in frame @ positive_x) for frame in FRAMES)
    undirected_images = Counter(
        min(
            tuple(int(value) for value in frame @ positive_x),
            tuple(int(-value) for value in frame @ positive_x),
        )
        for frame in FRAMES
    )
    directed_stabilizer = sum(np.array_equal(frame @ positive_x, positive_x) for frame in FRAMES)
    unordered_stabilizer = sum(
        np.array_equal(frame @ positive_x, positive_x)
        or np.array_equal(frame @ positive_x, -positive_x)
        for frame in FRAMES
    )

    l4_raw_edges = induced_edges(PATCH_CELLS, 4)
    controls = {}
    for name, action in (
        ("aliased_L4", lambda: validate_length(4)),
        ("improper_frame", lambda: validate_proper_frame(np.diag((-1, 1, 1)))),
        ("duplicate_centers", lambda: validate_centers((1, 1, 1), (1, 1, 1), 5)),
        ("nonadjacent_centers", lambda: validate_centers((1, 1, 1), (3, 1, 1), 5)),
    ):
        try:
            action()
        except ValueError as error:
            controls[name] = {"rejected": True, "error": str(error)}
        else:
            controls[name] = {"rejected": False, "error": None}

    passed = (
        len(FRAMES) == EXPECTED_PROPER_FRAMES
        and all(round(np.linalg.det(frame)) == 1 for frame in FRAMES)
        and len(frame_keys) == EXPECTED_PROPER_FRAMES
        and group_failures == 0
        and patch_action_failures == 0
        and frame_graph_failures == 0
        and len(directed_images) == 6
        and set(directed_images.values()) == {4}
        and len(undirected_images) == 3
        and set(undirected_images.values()) == {8}
        and directed_stabilizer == 4
        and unordered_stabilizer == 8
        and len(UNIQUE_STAR_SEAMS) == 11
        and len(PAULI_EDGES) == 15
        and len(l4_raw_edges) == 16
        and (2, 7) in l4_raw_edges
        and all(row["rejected"] for row in controls.values())
    )
    return {
        "proper_cubic_frames": len(FRAMES),
        "frame_products": EXPECTED_FRAME_PRODUCTS,
        "frame_group_law_failures": group_failures,
        "patch_action_failures": patch_action_failures,
        "frame_induced_graph_failures_L5_L6": frame_graph_failures,
        "directed_bond_orbit_size": len(directed_images),
        "directed_bond_stabilizer_size": directed_stabilizer,
        "unordered_bond_orbit_size": len(undirected_images),
        "unordered_bond_stabilizer_size": unordered_stabilizer,
        "full24_placement_requirement": (
            "one oriented adjacent-center placement has stabilizer 4; full proper-cubic "
            "covariance therefore requires its six-direction orbit"
        ),
        "left_star_seams": len(LEFT_STAR_SEAMS),
        "right_star_seams": len(RIGHT_STAR_SEAMS),
        "shared_center_seams": len(set(LEFT_STAR_SEAMS) & set(RIGHT_STAR_SEAMS)),
        "unique_star_seams": len(UNIQUE_STAR_SEAMS),
        "transverse_rungs": len(TRANSVERSE_RUNGS),
        "induced_Pauli_edges": len(PAULI_EDGES),
        "aliased_L4_raw_edge_count": len(l4_raw_edges),
        "aliased_L4_extra_wrap_edge": [2, 7] if (2, 7) in l4_raw_edges else None,
        "lawful_domain_controls": controls,
        "pass": passed,
    }


def polynomial_multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            result[first + second] += left_value * right_value
    return tuple(result)


def polynomial_power(base: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result = (1,)
    for _ in range(exponent):
        result = polynomial_multiply(result, base)
    return result


def chromatic_subset_coefficients(
    vertex_count: int, edges: tuple[tuple[int, int], ...]
) -> tuple[int, ...]:
    coefficients = [0] * (vertex_count + 1)
    for subset in range(1 << len(edges)):
        parent = list(range(vertex_count))

        def find(item: int) -> int:
            while parent[item] != item:
                parent[item] = parent[parent[item]]
                item = parent[item]
            return item

        components = vertex_count
        for bit, (first, second) in enumerate(edges):
            if not (subset >> bit) & 1:
                continue
            root_first, root_second = find(first), find(second)
            if root_first != root_second:
                parent[root_second] = root_first
                components -= 1
        coefficients[components] += -1 if subset.bit_count() % 2 else 1
    return tuple(coefficients)


def polynomial_evaluate(coefficients: tuple[int, ...], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def symbolic_graph_controls() -> dict:
    # q(q-1)^3(q^2-3q+3)^4, represented in ascending powers.
    factorized = polynomial_multiply(
        (0, 1),
        polynomial_multiply(
            polynomial_power((-1, 1), 3),
            polynomial_power((3, -3, 1), 4),
        ),
    )
    subset = chromatic_subset_coefficients(PATCH_CELL_COUNT, PAULI_EDGES)
    deletion_rows = []
    for edge in PAULI_EDGES:
        reduced = tuple(candidate for candidate in PAULI_EDGES if candidate != edge)
        coefficients = chromatic_subset_coefficients(PATCH_CELL_COUNT, reduced)
        deletion_rows.append(
            {
                "deleted_edge": edge,
                "polynomial_changed": coefficients != subset,
                "acyclic_orientations_after_deletion": polynomial_evaluate(coefficients, -1),
            }
        )
    expected_expanded = (0, -81, 567, -1809, 3483, -4509, 4131, -2739, 1317, -451, 105, -15, 1)
    passed = (
        subset == factorized
        and subset == expected_expanded
        and polynomial_evaluate(subset, -1) == EXPECTED_ACYCLIC_ORIENTATIONS
        and all(row["polynomial_changed"] for row in deletion_rows)
    )
    return {
        "graph_vertices": PATCH_CELL_COUNT,
        "graph_edges": len(PAULI_EDGES),
        "structural_decomposition": (
            "one center edge, two axial leaves, and four independent "
            "four-cycle pages sharing the center edge"
        ),
        "factorized_chromatic_polynomial": "q(q-1)^3(q^2-3q+3)^4",
        "expanded_coefficients_ascending": subset,
        "subset_expansion_terms": 1 << len(PAULI_EDGES),
        "minus_one_evaluation": polynomial_evaluate(subset, -1),
        "edge_deletion_rows": deletion_rows,
        "pass": passed,
    }


def orientation_graph(mask: int, edges=PAULI_EDGES):
    outgoing = [[] for _ in range(PATCH_CELL_COUNT)]
    indegree = [0] * PATCH_CELL_COUNT
    for bit, (first, second) in enumerate(edges):
        source, target = (first, second) if (mask >> bit) & 1 else (second, first)
        outgoing[source].append(target)
        indegree[target] += 1
    return outgoing, indegree


def canonical_topological_order(mask: int) -> tuple[int, ...] | None:
    outgoing, indegree = orientation_graph(mask)
    ready = [vertex for vertex, degree in enumerate(indegree) if degree == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        source = heapq.heappop(ready)
        order.append(source)
        for target in outgoing[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                heapq.heappush(ready, target)
    return tuple(order) if len(order) == PATCH_CELL_COUNT else None


def orientation_induced_by_order(order: tuple[int, ...]) -> int:
    position = {vertex: index for index, vertex in enumerate(order)}
    return sum(
        (1 << bit) if position[first] < position[second] else 0
        for bit, (first, second) in enumerate(PAULI_EDGES)
    )


def orientation_controls() -> dict:
    acyclic_masks = []
    reconstruction_failures = 0
    for mask in range(1 << len(PAULI_EDGES)):
        order = canonical_topological_order(mask)
        if order is None:
            continue
        acyclic_masks.append(mask)
        reconstruction_failures += orientation_induced_by_order(order) != mask
    acyclic_set = set(acyclic_masks)
    deletion_witnesses = []
    for bit, edge in enumerate(PAULI_EDGES):
        pair = next(
            (
                (mask, mask ^ (1 << bit))
                for mask in acyclic_masks
                if (mask ^ (1 << bit)) in acyclic_set
            ),
            None,
        )
        deletion_witnesses.append(
            {
                "edge": edge,
                "acyclic_words_differing_only_on_deleted_character": pair,
                "quotient_collision_if_character_deleted": pair is not None,
            }
        )
    role_bits = math.ceil(math.log2(len(acyclic_masks)))
    passed = (
        len(acyclic_masks) == EXPECTED_ACYCLIC_ORIENTATIONS
        and (1 << len(PAULI_EDGES)) - len(acyclic_masks) == EXPECTED_CYCLIC_ORIENTATION_WORDS
        and reconstruction_failures == 0
        and role_bits == EXPECTED_ROLE_M2
        and (1 << (role_bits - 1)) < len(acyclic_masks) <= (1 << role_bits)
        and all(row["quotient_collision_if_character_deleted"] for row in deletion_witnesses)
    )
    payload = json.dumps(acyclic_masks, separators=(",", ":")).encode("utf-8")
    return {
        "orientation_words_tested": 1 << len(PAULI_EDGES),
        "acyclic_orientations": len(acyclic_masks),
        "cyclic_orientation_words": (1 << len(PAULI_EDGES)) - len(acyclic_masks),
        "canonical_topological_reconstruction_failures": reconstruction_failures,
        "acyclic_mask_list_sha256": sha256(payload).hexdigest(),
        "minimal_static_order_character_classes": len(acyclic_masks),
        "minimum_static_M2_address_bits": role_bits,
        "fourteen_M2_capacity_deficit": len(acyclic_masks) - (1 << (role_bits - 1)),
        "fifteen_M2_unused_words_requiring_exclusion": (1 << role_bits) - len(acyclic_masks),
        "character_deletion_witnesses": deletion_witnesses,
        "pass": passed,
    }


def linear_extension_count(mask: int) -> int:
    outgoing, _ = orientation_graph(mask)
    predecessors = [0] * PATCH_CELL_COUNT
    for source, targets in enumerate(outgoing):
        for target in targets:
            predecessors[target] |= 1 << source
    counts = [0] * (1 << PATCH_CELL_COUNT)
    counts[0] = 1
    for chosen in range(1 << PATCH_CELL_COUNT):
        if counts[chosen] == 0:
            continue
        for vertex in range(PATCH_CELL_COUNT):
            bit = 1 << vertex
            if chosen & bit or predecessors[vertex] & ~chosen:
                continue
            counts[chosen | bit] += counts[chosen]
    return counts[-1]


def fixed_position_swap(order: tuple[int, ...], left_position: int) -> tuple[int, ...]:
    result = list(order)
    result[left_position], result[left_position + 1] = (
        result[left_position + 1],
        result[left_position],
    )
    return tuple(result)


def schedule_adversarial_controls() -> dict:
    """Audit what does and does not descend from S12 to the static quotient."""

    fiber_histogram = Counter()
    extension_counts = {}
    for mask in range(1 << len(PAULI_EDGES)):
        count = linear_extension_count(mask)
        extension_counts[mask] = count
        if count:
            fiber_histogram[count] += 1
    histogram_rows = tuple(sorted(fiber_histogram.items()))
    histogram_sha = sha256(
        json.dumps(histogram_rows, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    # This bounded deletion fixture has an acyclic canonical word, an acyclic
    # axial-leaf flip, and a cyclic central-edge flip.
    canonical_mask = 1920
    leaf_flip_mask = canonical_mask ^ (1 << EDGE_INDEX[(0, 2)])
    central_flip_mask = canonical_mask ^ (1 << EDGE_INDEX[(0, 1)])

    # Both orders lie in one quotient fiber.  The same fixed swap of zero-based
    # positions 3 and 4 crosses an active rung in the first representative and
    # a nonedge in the second, so it cannot define a deterministic quotient
    # action.  This is a schedule-specific failure, not a compiler no-go.
    first_order = (0, 2, 7, 8, 3, 9, 4, 10, 5, 11, 1, 6)
    second_order = (0, 2, 7, 8, 9, 3, 4, 10, 5, 11, 1, 6)
    first_input = orientation_induced_by_order(first_order)
    second_input = orientation_induced_by_order(second_order)
    first_target = orientation_induced_by_order(fixed_position_swap(first_order, 3))
    second_target = orientation_induced_by_order(fixed_position_swap(second_order, 3))

    total_orders = math.factorial(PATCH_CELL_COUNT)
    weighted_total = sum(fiber_size * multiplicity for fiber_size, multiplicity in histogram_rows)
    passed = (
        len(extension_counts) == 1 << len(PAULI_EDGES)
        and len(fiber_histogram) == 375
        and min(fiber_histogram) == 54
        and max(fiber_histogram) == 2_727_432
        and histogram_sha == "fa2bf7a73849928daad03cbb74182ba46b7f8c06dd1c6449a99bc37ebe7ca379"
        and weighted_total == total_orders
        and extension_counts[canonical_mask] == 27_720
        and extension_counts[leaf_flip_mask] == 2_520
        and extension_counts[central_flip_mask] == 0
        and first_input == second_input
        and first_target != second_target
        and first_input == 63
        and first_target == 2111
        and second_target == 63
    )
    return {
        "total_S12_orders": total_orders,
        "orientation_fibers": sum(fiber_histogram.values()),
        "distinct_linear_extension_weights": len(fiber_histogram),
        "minimum_linear_extensions": min(fiber_histogram),
        "maximum_linear_extensions": max(fiber_histogram),
        "linear_extension_histogram_sha256": histogram_sha,
        "linear_extension_weighted_sum": weighted_total,
        "quotient_isometry_amplitudes": "sqrt(L(O)/12!), not uniform over acyclic orientations",
        "canonical_deletion_fixture": {
            "canonical_mask": canonical_mask,
            "canonical_linear_extensions": extension_counts[canonical_mask],
            "axial_leaf_flip_mask": leaf_flip_mask,
            "axial_leaf_flip_linear_extensions": extension_counts[leaf_flip_mask],
            "central_edge_flip_mask": central_flip_mask,
            "central_edge_flip_linear_extensions": extension_counts[central_flip_mask],
        },
        "fixed_position_swap_non_descent_witness": {
            "zero_based_swapped_positions": (3, 4),
            "first_order": first_order,
            "second_order": second_order,
            "common_input_mask": first_input,
            "first_target_mask": first_target,
            "second_target_mask": second_target,
            "same_fiber_unequal_targets": first_input == second_input and first_target != second_target,
        },
        "fixed_position_swap_descends_to_static_quotient": False,
        "schedule_or_autonomous_update_claim": False,
        "pass": passed,
    }


def exact_resource_inventory() -> dict:
    sectors = {
        "n0": 2**PATCH_CELL_COUNT,
        "n1": PATCH_CELL_COUNT * 60 * 2 ** (PATCH_CELL_COUNT - 1),
        "n2_same_cell": PATCH_CELL_COUNT * 30 * 2 ** (PATCH_CELL_COUNT - 1),
        "n2_split_cells": math.comb(PATCH_CELL_COUNT, 2) * 60 * 60 * 2 ** (PATCH_CELL_COUNT - 2),
    }
    pair_cases = sum(
        LOCAL_TERM_COUNTS[left] * LOCAL_TERM_COUNTS[right]
        for left in range(3)
        for right in range(3)
        if left + right <= MAX_TOTAL_NUMBER
    )
    return {
        "physical_M2_sites_in_patch": PATCH_CELL_COUNT,
        "local_M64_modes_per_cell": LOCAL_MODE_COUNT,
        "global_total_number_domain": "N=0,1,2",
        "logical_dimension": LOGICAL_DIMENSION,
        "logical_dimension_formula": "1+72+C(72,2)",
        "local_term_counts_by_number": LOCAL_TERM_COUNTS,
        "allowed_pair_cases": pair_cases,
        "full_branch_count_by_sector": sectors,
        "analytic_full_branch_count_per_size": sum(sectors.values()),
        "full_branch_census_executed": False,
        "machine_zero_support_queries": 0,
        "magnitude_cutoff_support_queries": 0,
        "pass": (
            LOGICAL_DIMENSION == EXPECTED_LOGICAL_DIMENSION
            and pair_cases == EXPECTED_PAIR_CASES
            and sum(sectors.values()) == EXPECTED_FULL_BRANCHES_PER_SIZE
        ),
    }


def aggregate_terms(code, body, number: int):
    rows = []
    for label in c516.c311.LABELS[number]:
        for row in c516.gauge_terms_with_metadata(code, body, number, label):
            rows.append(
                {
                    "number": number,
                    "label": tuple(label),
                    "carrier": row["carrier"],
                    "variant": row["variant"],
                    "representative": row["representative"],
                }
            )
    expected = LOCAL_TERM_COUNTS[number]
    if len(rows) != expected:
        raise CertificateFailure(
            f"local term count mismatch at body={body}, n={number}: {len(rows)} != {expected}"
        )
    return tuple(rows)


def physical_pair_census(length: int, started: float) -> dict:
    validate_length(length)
    code = c516.c269.build_code(length)
    cells = rotated_patch(IDENTITY, length)
    cache = {
        (cell_index, number): aggregate_terms(code, body, number)
        for cell_index, body in enumerate(cells)
        for number in range(3)
    }
    tests = 0
    pair_rows = []
    occupation_histogram = Counter()
    for first, second in ALL_CELL_PAIRS:
        anticommuting = 0
        pair_occupation_histogram = Counter()
        for left_number in range(3):
            for right_number in range(3):
                if left_number + right_number > MAX_TOTAL_NUMBER:
                    continue
                for left in cache[first, left_number]:
                    for right in cache[second, right_number]:
                        tests += 1
                        if not left["representative"].commutes(right["representative"]):
                            anticommuting += 1
                            pair_occupation_histogram[left_number, right_number] += 1
                            occupation_histogram[left_number, right_number] += 1
        pair_rows.append(
            {
                "pair": (first, second),
                "anticommuting_cases": anticommuting,
                "anticommuting_occupation_histogram": tuple(
                    (list(key), value) for key, value in sorted(pair_occupation_histogram.items())
                ),
            }
        )
    active = tuple(row["pair"] for row in pair_rows if row["anticommuting_cases"])
    canonical = tuple(
        (row["pair"], row["anticommuting_cases"], row["anticommuting_occupation_histogram"])
        for row in pair_rows
    )
    digest = sha256(json.dumps(canonical, separators=(",", ":")).encode("utf-8")).hexdigest()
    active_rows = tuple(row for row in pair_rows if row["pair"] in PAULI_EDGE_SET)
    inactive_rows = tuple(row for row in pair_rows if row["pair"] not in PAULI_EDGE_SET)
    passed = (
        tests == EXPECTED_PAIR_TESTS_PER_SIZE
        and active == PAULI_EDGES
        and len(active_rows) == 15
        and all(row["anticommuting_cases"] == 200 for row in active_rows)
        and all(row["anticommuting_occupation_histogram"] == (([1, 1], 200),) for row in active_rows)
        and len(inactive_rows) == 51
        and all(row["anticommuting_cases"] == 0 for row in inactive_rows)
    )
    return {
        "L": length,
        "held_size": length == HELD_LENGTH,
        "all_unordered_cell_pairs": len(ALL_CELL_PAIRS),
        "allowed_local_term_cases_per_pair": EXPECTED_PAIR_CASES,
        "physical_pair_tests": tests,
        "active_anticommutation_edges": active,
        "active_edge_count": len(active),
        "inactive_pair_count": len(inactive_rows),
        "anticommuting_cases_per_active_edge": tuple(
            row["anticommuting_cases"] for row in active_rows
        ),
        "all_active_cases_are_n1_n1": all(
            row["anticommuting_occupation_histogram"] == (([1, 1], 200),)
            for row in active_rows
        ),
        "total_anticommuting_pair_cases": sum(occupation_histogram.values()),
        "canonical_pair_summary_sha256": digest,
        "machine_zero_support_queries": 0,
        "magnitude_cutoff_support_queries": 0,
        "resource": resource_checkpoint(started, f"L{length}-pair-census-complete"),
        "pass": passed,
    }


def pair_mask(representatives) -> int:
    mask = 0
    for bit, (first, second) in enumerate(PAULI_EDGES):
        if not representatives[first].commutes(representatives[second]):
            mask |= 1 << bit
    return mask


def all_anticommuting_pairs(representatives) -> tuple[tuple[int, int], ...]:
    return tuple(
        pair
        for pair in ALL_CELL_PAIRS
        if not representatives[pair[0]].commutes(representatives[pair[1]])
    )


def metadata(term: dict) -> dict:
    return {
        "number": term["number"],
        "label": tuple(term["label"]),
        "carrier": term["carrier"],
        "variant": term["variant"],
    }


def derive_unit_witness_signatures(length: int) -> tuple[dict, ...]:
    """Bounded CSP search for one exact full-branch singleton per graph edge."""

    code = c516.c269.build_code(length)
    cells = rotated_patch(IDENTITY, length)
    candidates = {
        (cell, number): aggregate_terms(code, body, number)
        for cell, body in enumerate(cells)
        for number in (0, 1)
    }
    witness_rows = []
    for target in PAULI_EDGES:
        domains = tuple(candidates[cell, 1 if cell in target else 0] for cell in range(12))
        first, second = target
        unassigned = tuple(cell for cell in range(12) if cell not in target)
        trials = 0
        answer = None
        for first_index, first_term in enumerate(domains[first]):
            if answer is not None:
                break
            for second_index, second_term in enumerate(domains[second]):
                if first_term["representative"].commutes(second_term["representative"]):
                    continue
                assignment = {first: first_index, second: second_index}

                def search():
                    nonlocal trials
                    if len(assignment) == PATCH_CELL_COUNT:
                        return dict(assignment)
                    best_cell = None
                    best_options = None
                    for cell in unassigned:
                        if cell in assignment:
                            continue
                        options = []
                        for index, term in enumerate(domains[cell]):
                            lawful = True
                            for assigned_cell, assigned_index in assignment.items():
                                pair = (min(cell, assigned_cell), max(cell, assigned_cell))
                                if pair not in PAULI_EDGE_SET:
                                    continue
                                anti = not term["representative"].commutes(
                                    domains[assigned_cell][assigned_index]["representative"]
                                )
                                if anti != (pair == target):
                                    lawful = False
                                    break
                            if lawful:
                                options.append(index)
                        if not options:
                            return None
                        if best_options is None or len(options) < len(best_options):
                            best_cell, best_options = cell, options
                    for index in best_options:
                        trials += 1
                        assignment[best_cell] = index
                        result = search()
                        if result is not None:
                            return result
                        del assignment[best_cell]
                    return None

                solution = search()
                if solution is None:
                    continue
                representatives = tuple(
                    domains[cell][solution[cell]]["representative"] for cell in range(12)
                )
                if all_anticommuting_pairs(representatives) == (target,):
                    answer = tuple(metadata(domains[cell][solution[cell]]) for cell in range(12))
                    break
        if answer is None:
            raise CertificateFailure(f"no singleton-mask witness found for edge {target}")
        witness_rows.append(
            {
                "target_edge": target,
                "target_mask": 1 << EDGE_INDEX[target],
                "search_trials": trials,
                "signature": answer,
            }
        )
    return tuple(witness_rows)


def transform_metadata(row: dict, frame: np.ndarray) -> dict:
    return {
        "number": row["number"],
        "label": tuple(sorted(c516.c311.direction_map(frame, direction) for direction in row["label"])),
        "carrier": (
            None
            if row["carrier"] is None
            else c516.c311.direction_map(frame, row["carrier"])
        ),
        "variant": row["variant"],
    }


def representative_for_metadata(code, body, row: dict):
    matches = tuple(
        candidate["representative"]
        for candidate in c516.gauge_terms_with_metadata(
            code, body, row["number"], tuple(row["label"])
        )
        if candidate["carrier"] == row["carrier"] and candidate["variant"] == row["variant"]
    )
    if len(matches) != 1:
        raise CertificateFailure(f"metadata lookup multiplicity {len(matches)} at {body}: {row}")
    return matches[0]


def physical_unit_witness_controls(signatures, started: float) -> dict:
    rows = []
    failures = 0
    total_number_failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        code = c516.c269.build_code(length)
        length_masks = []
        for frame_index, frame in enumerate(FRAMES):
            cells = rotated_patch(frame, length)
            for witness in signatures:
                transformed = tuple(transform_metadata(row, frame) for row in witness["signature"])
                total_number_failures += sum(row["number"] for row in transformed) != 2
                representatives = tuple(
                    representative_for_metadata(code, cells[cell], transformed[cell])
                    for cell in range(PATCH_CELL_COUNT)
                )
                physical_pairs = all_anticommuting_pairs(representatives)
                physical_mask = pair_mask(representatives)
                expected_pair = tuple(witness["target_edge"])
                failed = (
                    physical_pairs != (expected_pair,)
                    or physical_mask != witness["target_mask"]
                )
                failures += failed
                length_masks.append(physical_mask)
        rows.append(
            {
                "L": length,
                "held_size": length == HELD_LENGTH,
                "proper_frames": len(FRAMES),
                "unit_witness_tests": len(length_masks),
                "distinct_unit_masks": len(set(length_masks)),
                "unit_masks": tuple(sorted(set(length_masks))),
                "failures": failures if length == TRAIN_LENGTH else failures,
            }
        )
        resource_checkpoint(started, f"L{length}-unit-witnesses-complete")
    signature_payload = json.dumps(signatures, sort_keys=True, separators=(",", ":")).encode("utf-8")
    passed = (
        failures == 0
        and total_number_failures == 0
        and all(row["unit_witness_tests"] == EXPECTED_PROPER_FRAMES * len(PAULI_EDGES) for row in rows)
        and all(row["distinct_unit_masks"] == len(PAULI_EDGES) for row in rows)
    )
    return {
        "derived_at_train_L": TRAIN_LENGTH,
        "derived_signature_count": len(signatures),
        "derived_signature_sha256": sha256(signature_payload).hexdigest(),
        "search_trials_by_edge": tuple(
            (row["target_edge"], row["search_trials"]) for row in signatures
        ),
        "transported_witness_rows": rows,
        "total_unit_witness_tests": sum(row["unit_witness_tests"] for row in rows),
        "proper_frame_or_held_failures": failures,
        "global_N2_failures": total_number_failures,
        "machine_zero_support_queries": 0,
        "magnitude_cutoff_support_queries": 0,
        "pass": passed,
    }


def upstream_evidence() -> dict:
    missing = tuple(str(path.relative_to(ROOT)) for path in STRICT_FILE_HASHES if not path.exists())
    observed = {
        str(path.relative_to(ROOT)): file_sha(path)
        for path in STRICT_FILE_HASHES
        if path.exists()
    }
    failures = {
        str(path.relative_to(ROOT)): {"expected": expected, "observed": observed.get(str(path.relative_to(ROOT)))}
        for path, expected in STRICT_FILE_HASHES.items()
        if observed.get(str(path.relative_to(ROOT))) != expected
    }
    receipt = last_json(CYCLE516_RECEIPT) if CYCLE516_RECEIPT.exists() else {}
    passed = (
        not missing
        and not failures
        and receipt.get("pass") is True
        and receipt.get("authority") == AUTHORITY
        and receipt.get("audit") == AUDIT
        and receipt.get("status") == "cycle516-koszul-corrected-all-order-frame-certified"
    )
    return {
        "missing_files": missing,
        "strict_file_hashes": observed,
        "strict_hash_failures": failures,
        "Cycle516_status": receipt.get("status"),
        "Cycle516_pass": receipt.get("pass"),
        "Cycle516_authority": receipt.get("authority"),
        "Cycle516_audit": receipt.get("audit"),
        "Cycle516_adjacent_star_claim": receipt.get("boundary", {}).get("adjacent_star_claim"),
        "pass": passed,
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE.relative_to(ROOT)), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "q(q-1)^3(q^2-3q+3)^4",
        "19,208",
        "15 m2",
        "13,560",
        "245,518,336",
        "full branch census was not run",
        "e g_coarse = g_physical e remains open",
        "no obstruction and no axiom pressure",
        "n1 — alternative-route map",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    geometry = geometry_controls()
    symbolic = symbolic_graph_controls()
    orientations = orientation_controls()
    schedule = schedule_adversarial_controls()
    resources = exact_resource_inventory()
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "upstream_Cycle516_bound": evidence["pass"],
        "lawful_geometry_and_proper_frames": geometry["pass"],
        "exact_chromatic_polynomial_and_deletions": symbolic["pass"],
        "acyclic_orientation_quotient_and_deletions": orientations["pass"],
        "linear_extension_weights_and_schedule_non_descent": schedule["pass"],
        "exact_resource_inventory_without_full_census": resources["pass"],
        "note_scope_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle517-adjacent-two-star-preflight-contract-ready" if all(tests.values()) else "cycle517-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "geometry": geometry,
        "symbolic_graph": symbolic,
        "orientation_quotient": orientations,
        "schedule_adversarial": schedule,
        "resources": resources,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def preflight_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [resource_checkpoint(started, "initial", projected_bytes=250_000_000)]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle517 dry contract failed")
    train = physical_pair_census(TRAIN_LENGTH, started)
    checkpoints.append(train["resource"])
    held = physical_pair_census(HELD_LENGTH, started)
    checkpoints.append(held["resource"])
    signatures = derive_unit_witness_signatures(TRAIN_LENGTH)
    checkpoints.append(resource_checkpoint(started, "L5-unit-signatures-derived"))
    witnesses = physical_unit_witness_controls(signatures, started)
    checkpoints.append(resource_checkpoint(started, "all-frame-held-witnesses-complete"))
    held_match = train["canonical_pair_summary_sha256"] == held["canonical_pair_summary_sha256"]
    tests = {
        "dry_contract": dry["pass"],
        "L5_all66_times3964_pair_census": train["pass"],
        "held_L6_all66_times3964_pair_census": held["pass"],
        "held_pair_summary_matches_train": held_match,
        "all_15_physical_unit_masks_all24_frames_L5_L6": witnesses["pass"],
        "no_full_245518336_branch_census": not dry["resources"]["full_branch_census_executed"],
        "checkpoint_resource_contract": swap_count() == 0 and rss_bytes() < RSS_CHECKPOINT_GUARD_BYTES,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "preflight-certificate",
        "status": "cycle517-adjacent-two-star-static-character-preflight-certified" if all(tests.values()) else "cycle517-preflight-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "geometry": dry["geometry"],
        "symbolic_graph": dry["symbolic_graph"],
        "orientation_quotient": dry["orientation_quotient"],
        "schedule_adversarial": dry["schedule_adversarial"],
        "resources": dry["resources"],
        "physical_pair_rows": (train, held),
        "held_pair_summary_matches_train": held_match,
        "physical_unit_witnesses": witnesses,
        "deletion_and_domain_controls": {
            "all_15_graph_edge_deletions_change_chromatic_polynomial": all(
                row["polynomial_changed"] for row in dry["symbolic_graph"]["edge_deletion_rows"]
            ),
            "all_15_character_deletions_have_explicit_collisions": all(
                row["quotient_collision_if_character_deleted"]
                for row in dry["orientation_quotient"]["character_deletion_witnesses"]
            ),
            "delete_one_role_bit_capacity_deficit": dry["orientation_quotient"]["fourteen_M2_capacity_deficit"],
            "invalid_15_bit_words_requiring_exclusion": dry["orientation_quotient"]["fifteen_M2_unused_words_requiring_exclusion"],
            "lawful_domain_controls": dry["geometry"]["lawful_domain_controls"],
            "pass": dry["geometry"]["pass"],
        },
        "boundary": {
            "static_local_order_character_preflight": True,
            "twelve_cell_encoding_injectivity_proven": False,
            "twelve_cell_encoding_isometry_proven": False,
            "E_Gcoarse_equals_Gphysical_E_proven": False,
            "local_invalid_role_constraint_synthesis_proven": False,
            "primitive_update_synthesis_proven": False,
            "fixed_position_swap_schedule_descends_to_quotient": False,
            "mass_fixture_retested": False,
            "adjacent_star_recurrent_volume_proven": False,
            "physical_time_claim": False,
            "Record_claim": False,
            "source_or_gravity_claim": False,
            "Born_or_probability_claim": False,
            "obstruction_claim": False,
            "axiom_pressure": False,
        },
        "supplied_structure": (
            "Cycle311/315 local gauge-term grammar",
            "Cycle516 proper-cubic affine Clifford action",
            "a bounded fifteen-M2 static orientation address",
            "exclusion of 13,560 cyclic role words if that address is realized",
            "initialization and enforcement of the role address",
        ),
        "next_open_target": (
            "synthesize locally enforced overlapping adjacent-star orientation constraints "
            "and then prove a twelve-cell injective/isometric E before defining G_physical"
        ),
        "resource_limits": {
            "hard_wall_alarm_seconds": WALL_LIMIT_SECONDS,
            "RSS_checkpoint_abort_ceiling_bytes": RSS_CHECKPOINT_ABORT_CEILING_BYTES,
            "RSS_checkpoint_guard_bytes": RSS_CHECKPOINT_GUARD_BYTES,
            "zero_swap_checkpoint_monitored": True,
            "partial_rows_durable_across_OS_kill_or_process_OOM": False,
        },
        "resource_checkpoints": checkpoints,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
        "elapsed_seconds": elapsed,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, required=True)
    args = parser.parse_args()
    if args.mode == "dry-contract":
        result = dry_contract()
    else:
        signal.signal(signal.SIGALRM, _alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, WALL_LIMIT_SECONDS)
        try:
            result = preflight_certificate()
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), default=list))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
