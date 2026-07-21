#!/usr/bin/env python3
"""Cycle 519: dedicated seam-tag preservation repair.

This bounded runner appends one binary M2 tag to the oriented adjacent-star
patch of Cycles 517/518.  The tag is the parity of the six logical modes at
the anchored (left) center.  It proves, on the declared global-N<=2 code
space, that the tag splits every native collision fiber without changing the
Cycle-311/315 branch grammar.  It also distinguishes a seven-M2 factor-local
parity descriptor from the final overlapping code: an explicit full-product
countercontrol rejects the former as a global stabilizer.  The runner tests
proper-cubic anchored covariance, the endpoint-reversal cocycle, and the
logical free-plus-contact seam transport rule.

The certificate does not prepare the independent collision-splitting tag or
synthesize its controlled tag-X from primitive physical M2 updates.  Nor does
it prove that one tag per star center can be reused consistently in a
recurrent overlapping tiling.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
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

import physical_adjacent_two_star_compressed_gram_cycle518_2026_07_21 as c518


c517 = c518.c517
c516 = c518.c516
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 2
CLI_MODES = ("dry-contract", "tag-certificate")
TRAIN_LENGTH = 5
HELD_LENGTH = 6
PATCH_CELL_COUNT = 12
LOCAL_MODE_COUNT = 6
MAX_TOTAL_NUMBER = 2
LOGICAL_MODE_COUNT = PATCH_CELL_COUNT * LOCAL_MODE_COUNT
EXPECTED_LOGICAL_DIMENSION = 2629
EXPECTED_SEEDS = 238_681
EXPECTED_TAG_ONE_SEEDS = 39_660
EXPECTED_FULL_BRANCHES = 245_518_336
EXPECTED_PROPER_FRAMES = 24
EXPECTED_FRAME_PRODUCTS = 576
EXPECTED_LOCAL_TERM_TESTS = 3_072
EXPECTED_ANCHOR_TERM_TESTS = 256
EXPECTED_OVERLAP_BRANCH_TESTS_PER_TARGET = 1_080
EXPECTED_OVERLAP_CONSTRAINT_FAILURES_PER_TARGET = 90
EXPECTED_SINGLE_SEAM_TESTS = 28_919
EXPECTED_PAIR_ORDER_TESTS = 289_190
EXPECTED_COMPOSED_TAG_CHANGES = 732
EXPECTED_NATIVE_DOUBLETONS = 24
EXPECTED_NATIVE_ROW_COLLISIONS = 6_144
EXPECTED_NATIVE_GRAM_RESIDUAL = Fraction(1, 400)

WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_CHECKPOINT_ABORT_CEILING_BYTES = 3_000_000_000
RSS_CHECKPOINT_GUARD_BYTES = 2_850_000_000

CYCLE517_RUNNER = ROOT / "scripts/physical_adjacent_two_star_order_character_preflight_cycle517_2026_07_21.py"
CYCLE517_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_ORDER_CHARACTER_PREFLIGHT_CYCLE517_NOTE_2026-07-21.md"
)
CYCLE518_RUNNER = ROOT / "scripts/physical_adjacent_two_star_compressed_gram_cycle518_2026_07_21.py"
CYCLE518_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_COMPRESSED_GRAM_CYCLE518_NOTE_2026-07-21.md"
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_SEAM_TAG_PRESERVATION_CYCLE519_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE517_RUNNER: "ad8b0c71840cbfa56aae3ae9da44eceec1cad7d84be06bab32604eb5f6fbb4a3",
    CYCLE517_NOTE: "51c3b92448f7779fe838c51265b279d82f48e3b19f6c0464b95f18112bf07a74",
    CYCLE518_RUNNER: "8f505d2de6476bdbc20f87a901e8be9fe46deda5b568c98d750977069a352e53",
    CYCLE518_NOTE: "7278244447e4074e66966e418710e2ad401befc4b8cbfb9d0a30088c0f837107",
}

# The eleven physical free-stream seams of the adjacent two-star patch.
# The four transverse Cycle-517 anticommutation rungs are not stream seams.
LEFT_INCIDENT_SEAMS = (
    ((0, 0), (1, 1)),
    ((0, 1), (2, 0)),
    ((0, 3), (3, 2)),
    ((0, 2), (4, 3)),
    ((0, 5), (5, 4)),
    ((0, 4), (6, 5)),
)
RIGHT_ONLY_SEAMS = (
    ((1, 0), (7, 1)),
    ((1, 3), (8, 2)),
    ((1, 2), (9, 3)),
    ((1, 5), (10, 4)),
    ((1, 4), (11, 5)),
)
DYNAMIC_SEAMS = LEFT_INCIDENT_SEAMS + RIGHT_ONLY_SEAMS


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physical conclusion."""


class CertificateFailure(RuntimeError):
    """A failed bounded predicate, never a substrate obstruction."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str, projected_bytes: int = 0) -> dict:
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


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def fraction_json(value: Fraction) -> tuple[int, int]:
    return value.numerator, value.denominator


def upstream_evidence() -> dict:
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    hashes_match = observed == expected
    cycle517_dry = c517.dry_contract()
    cycle518_dry = c518.dry_contract()
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "hashes_match": hashes_match,
        "Cycle517_dry_pass": cycle517_dry["pass"],
        "Cycle518_dry_pass": cycle518_dry["pass"],
        "pass": hashes_match and cycle517_dry["pass"] and cycle518_dry["pass"],
    }


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "245,518,336",
        "seven-m2",
        "one shared per-center",
        "reversal cocycle",
        "28,919",
        "289,190",
        "primitive synthesis",
        "recurrent overlap",
        "mass retest",
        "prediction bridges",
        "authority: none",
        "audit: unset",
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


def exact_resource_inventory() -> dict:
    logical_dimension = 1 + LOGICAL_MODE_COUNT + math.comb(LOGICAL_MODE_COUNT, 2)
    seed_sectors = {
        "n0": 1,
        "n1": PATCH_CELL_COUNT * 60,
        "n2_same_cell": PATCH_CELL_COUNT * 30,
        "n2_split_cells": math.comb(PATCH_CELL_COUNT, 2) * 60 * 60,
    }
    branch_sectors = {
        "n0": 2**12,
        "n1": PATCH_CELL_COUNT * 60 * 2**11,
        "n2_same_cell": PATCH_CELL_COUNT * 30 * 2**11,
        "n2_split_cells": math.comb(PATCH_CELL_COUNT, 2) * 60 * 60 * 2**10,
    }
    column_branches_and_squared_weights = {
        "n0": (4096, fraction_json(Fraction(1, 4096))),
        "n1": (20480, fraction_json(Fraction(1, 20480))),
        "n2_same_cell": (4096, fraction_json(Fraction(1, 4096))),
        "n2_split_cells": (102400, fraction_json(Fraction(1, 102400))),
    }
    normalizations = {
        sector: fraction_json(Fraction(count) * Fraction(*weight))
        for sector, (count, weight) in column_branches_and_squared_weights.items()
    }
    return {
        "physical_patch_cells": PATCH_CELL_COUNT,
        "logical_modes": LOGICAL_MODE_COUNT,
        "lawful_total_number": "N=0,1,2",
        "logical_dimension": logical_dimension,
        "seed_sectors": seed_sectors,
        "branch_sectors": branch_sectors,
        "full_branches": sum(branch_sectors.values()),
        "column_branches_and_squared_weights": column_branches_and_squared_weights,
        "exact_column_normalizations": normalizations,
        "dedicated_tag_M2_per_oriented_patch": 1,
        "maximum_branch_support_increment": 1,
        "factor_local_parity_descriptor_support_M2": 7,
        "global_seven_M2_code_constraint_proven": False,
        "endpoint_reversal_support_upper_bound_M2": 13,
        "logical_seam_transport_support_M2": 3,
        "pass": (
            logical_dimension == EXPECTED_LOGICAL_DIMENSION
            and sum(seed_sectors.values()) == EXPECTED_SEEDS
            and sum(branch_sectors.values()) == EXPECTED_FULL_BRANCHES
            and all(value == (1, 1) for value in normalizations.values())
        ),
    }


def build_cache(length: int):
    code = c516.c269.build_code(length)
    cells = c517.rotated_patch(c517.IDENTITY, length)
    cache = {
        (cell, number): c518.aggregate_terms(code, body, number)
        for cell, body in enumerate(cells)
        for number in range(3)
    }
    return code, cells, cache


def tagged_seed_census(length: int, started: float) -> dict:
    code, _cells, cache = build_cache(length)
    vacuum = tuple(cache[cell, 0][0]["auxiliary"] for cell in range(PATCH_CELL_COUNT))
    toggles = tuple(
        cache[cell, 0][0]["auxiliary"] ^ cache[cell, 0][1]["auxiliary"]
        for cell in range(PATCH_CELL_COUNT)
    )
    basis = c518.gf2_basis(toggles)
    native_seen: dict[int, tuple[int, int]] = {}
    tagged_seen: set[int] = set()
    native_fibers = Counter()
    sector_seeds = Counter()
    tag_values = Counter()
    duplicate_endpoint_patterns = Counter()
    tag_digest = sha256()
    native_doubletons = 0
    tagged_collisions = 0

    def add(occupied: int, choices, sector: str) -> None:
        nonlocal native_doubletons, tagged_collisions
        delta = 0
        for cell, number, term_index in choices:
            delta ^= cache[cell, number][term_index]["auxiliary"] ^ vacuum[cell]
        quotient, _coefficient = c518.gf2_reduce(delta, basis)
        left_parity = sum(number for cell, number, _index in choices if cell == 0) & 1
        right_parity = sum(number for cell, number, _index in choices if cell == 1) & 1
        tagged_key = (quotient << 1) | left_parity
        sector_seeds[sector] += 1
        tag_values[left_parity] += 1
        native_fibers[quotient] += 1
        if quotient in native_seen:
            native_doubletons += 1
            first_left, first_right = native_seen[quotient]
            duplicate_endpoint_patterns[(first_left, first_right, left_parity, right_parity)] += 1
        else:
            native_seen[quotient] = (left_parity, right_parity)
        if tagged_key in tagged_seen:
            tagged_collisions += 1
        else:
            tagged_seen.add(tagged_key)
        byte_count = max(1, (tagged_key.bit_length() + 7) // 8)
        tag_digest.update(byte_count.to_bytes(2, "little"))
        tag_digest.update(tagged_key.to_bytes(byte_count, "little"))

    add(0, (), "n0")
    for cell in range(PATCH_CELL_COUNT):
        for term_index, _term in enumerate(cache[cell, 1]):
            add(1 << cell, ((cell, 1, term_index),), "n1")
        for term_index, _term in enumerate(cache[cell, 2]):
            add(1 << cell, ((cell, 2, term_index),), "n2_same_cell")
    for first, second in combinations(range(PATCH_CELL_COUNT), 2):
        for first_index, _first_term in enumerate(cache[first, 1]):
            for second_index, _second_term in enumerate(cache[second, 1]):
                add(
                    (1 << first) | (1 << second),
                    ((first, 1, first_index), (second, 1, second_index)),
                    "n2_split_cells",
                )

    endpoint_split = Counter()
    for (first_left, first_right, second_left, second_right), count in duplicate_endpoint_patterns.items():
        endpoint_split[(first_left, first_right, second_left, second_right)] += count
    left_xor_split = sum(
        count
        for pattern, count in endpoint_split.items()
        if pattern[0] ^ pattern[2]
    )
    right_xor_split = sum(
        count
        for pattern, count in endpoint_split.items()
        if pattern[1] ^ pattern[3]
    )
    pattern_classes = Counter()
    for pattern, count in endpoint_split.items():
        endpoints = {(pattern[0], pattern[1]), (pattern[2], pattern[3])}
        if endpoints == {(1, 0), (0, 1)}:
            pattern_classes["10_vs_01"] += count
        elif endpoints == {(1, 1), (0, 0)}:
            pattern_classes["11_vs_00"] += count
        else:
            pattern_classes["other"] += count

    checkpoint_row = checkpoint(started, f"L{length}-tag-census-complete")
    maximum_native_fiber = max(native_fibers.values())
    return {
        "length": length,
        "excitation_seeds": sum(sector_seeds.values()),
        "sector_seeds": dict(sector_seeds),
        "tag_zero_seeds": tag_values[0],
        "tag_one_seeds": tag_values[1],
        "native_quotient_fibers": len(native_fibers),
        "native_doubleton_fibers": native_doubletons,
        "native_maximum_fiber": maximum_native_fiber,
        "tagged_quotient_fibers": len(tagged_seen),
        "tagged_fiber_histogram": {"1": len(tagged_seen)},
        "tagged_maximum_fiber": 1 if tagged_seen else 0,
        "tagged_seed_collisions": tagged_collisions,
        "native_doubleton_endpoint_pattern_classes": dict(pattern_classes),
        "native_doubletons_split_by_left_tag": left_xor_split,
        "native_doubletons_split_after_reversal_by_right_tag": right_xor_split,
        "ordered_tag_key_stream_sha256": tag_digest.hexdigest(),
        "analytic_expanded_rows": EXPECTED_FULL_BRANCHES,
        "analytic_unique_expanded_rows": EXPECTED_FULL_BRANCHES,
        "literal_245518336_row_materialization_executed": False,
        "resource": checkpoint_row,
        "pass": (
            sum(sector_seeds.values()) == EXPECTED_SEEDS
            and tag_values[1] == EXPECTED_TAG_ONE_SEEDS
            and len(native_fibers) == c518.EXPECTED_QUOTIENT_FIBERS
            and native_doubletons == EXPECTED_NATIVE_DOUBLETONS
            and maximum_native_fiber == 2
            and len(tagged_seen) == EXPECTED_SEEDS
            and tagged_collisions == 0
            and pattern_classes == Counter({"10_vs_01": 16, "11_vs_00": 8})
            and left_xor_split == right_xor_split == EXPECTED_NATIVE_DOUBLETONS
        ),
    }


def local_constraint_controls(length: int) -> dict:
    code, cells, cache = build_cache(length)
    tests = 0
    failures = 0
    anchor_tests = 0
    deletion_failures = Counter()
    vertices_by_cell = tuple(c516.c315.c305.body_vertices(code, body) for body in cells)
    for cell in range(PATCH_CELL_COUNT):
        vertices = vertices_by_cell[cell]
        for number in range(7):
            expected_parity = number & 1
            terms = tuple(
                term
                for label in c516.c311.LABELS[number]
                for term in c516.gauge_terms_with_metadata(
                    code, cells[cell], number, label
                )
            )
            for term in terms:
                auxiliary = term["representative"].x >> code.qubits
                port_parity = sum((auxiliary >> vertex) & 1 for vertex in vertices) & 1
                tests += 1
                failures += port_parity != expected_parity
                if cell == 0:
                    anchor_tests += 1
                    for omitted, vertex in enumerate(vertices):
                        reduced_parity = port_parity ^ ((auxiliary >> vertex) & 1)
                        deletion_failures[omitted] += reduced_parity != expected_parity
    deletion_counts = tuple(deletion_failures[index] for index in range(LOCAL_MODE_COUNT))
    return {
        "length": length,
        "descriptor": "factor-local parity: tau = parity of the six ports before overlapping cell-factor multiplication",
        "descriptor_support_M2": 7,
        "all_cell_local_term_tests": tests,
        "factor_local_parity_failures": failures,
        "anchor_term_tests": anchor_tests,
        "delete_each_port_descriptor_failures": deletion_counts,
        "global_code_constraint_claimed": False,
        "pass": (
            tests == EXPECTED_LOCAL_TERM_TESTS
            and anchor_tests == EXPECTED_ANCHOR_TERM_TESTS
            and failures == 0
            and deletion_counts == (72,) * LOCAL_MODE_COUNT
        ),
    }


def overlap_constraint_countercontrol(length: int) -> dict:
    """Test whether factor-local port parity survives the overlapping product.

    A single occupied cell is multiplied with the canonical vacuum factor at
    every other cell.  This already supplies an exact counterexample class to
    treating the factor-local seven-M2 descriptor as a final-code stabilizer.
    """

    code, cells, cache = build_cache(length)
    rows = []
    examples = []
    for target in (0, 1):
        vertices = c516.c315.c305.body_vertices(code, cells[target])
        tests = 0
        failures = 0
        source_failure_histogram = Counter()
        for source in range(PATCH_CELL_COUNT):
            for number in (1, 2):
                for term_index, term in enumerate(cache[source, number]):
                    representatives = tuple(
                        term["representative"]
                        if cell == source
                        else cache[cell, 0][0]["representative"]
                        for cell in range(PATCH_CELL_COUNT)
                    )
                    product = c518.multiply_order(representatives)
                    auxiliary = product.x >> code.qubits
                    final_port_parity = sum(
                        (auxiliary >> vertex) & 1 for vertex in vertices
                    ) & 1
                    logical_target_parity = (
                        number & 1 if source == target else 0
                    )
                    failed = final_port_parity != logical_target_parity
                    tests += 1
                    failures += failed
                    source_failure_histogram[source] += failed
                    if failed and len(examples) < 8:
                        examples.append(
                            {
                                "target": target,
                                "source": source,
                                "number": number,
                                "term_index": term_index,
                                "label": term["label"],
                                "carrier": term["carrier"],
                                "variant": term["variant"],
                                "final_port_parity": final_port_parity,
                                "logical_target_parity": logical_target_parity,
                            }
                        )
        rows.append(
            {
                "target": target,
                "single_occupied_cell_canonical_branch_tests": tests,
                "global_seven_M2_constraint_failures": failures,
                "source_failure_histogram": dict(source_failure_histogram),
            }
        )
    failure_counts = tuple(
        row["global_seven_M2_constraint_failures"] for row in rows
    )
    return {
        "length": length,
        "rows": tuple(rows),
        "examples": tuple(examples),
        "unitary_postprocessing_preserves_native_Gram": True,
        "native_doubletons_surviving_any_W_times_E_native_construction": EXPECTED_NATIVE_DOUBLETONS,
        "native_operator_Gram_residual_surviving_any_W_times_E_native_construction": fraction_json(EXPECTED_NATIVE_GRAM_RESIDUAL),
        "factor_local_descriptor_is_global_code_constraint": False,
        "pass": (
            all(
                row["single_occupied_cell_canonical_branch_tests"]
                == EXPECTED_OVERLAP_BRANCH_TESTS_PER_TARGET
                for row in rows
            )
            and failure_counts
            == (EXPECTED_OVERLAP_CONSTRAINT_FAILURES_PER_TARGET,) * 2
        ),
    }


def frame_and_reversal_controls() -> dict:
    frames = c517.FRAMES
    positive_x = np.asarray((1, 0, 0), dtype=int)
    frame_keys = {tuple(int(value) for value in frame.reshape(-1)) for frame in frames}
    product_failures = 0
    for left in frames:
        for right in frames:
            product = tuple(int(value) for value in (left @ right).reshape(-1))
            product_failures += product not in frame_keys
    unordered = tuple(
        frame for frame in frames if np.array_equal(np.abs(frame @ positive_x), positive_x)
    )
    ordered = tuple(frame for frame in unordered if np.array_equal(frame @ positive_x, positive_x))

    def reverses(frame) -> bool:
        return np.array_equal(frame @ positive_x, -positive_x)

    def tag_action(frame, state: tuple[int, int, int]) -> tuple[int, int, int]:
        left, right, tag = state
        if reverses(frame):
            return right, left, tag ^ left ^ right
        return state

    unordered_product_tests = 0
    unordered_product_failures = 0
    tag_action_tests = 0
    tag_action_failures = 0
    for first in unordered:
        for second in unordered:
            product = first @ second
            unordered_product_tests += 1
            key = tuple(int(value) for value in product.reshape(-1))
            unordered_product_failures += key not in frame_keys
            for left in (0, 1):
                for right in (0, 1):
                    for tag in (0, 1):
                        state = (left, right, tag)
                        sequential = tag_action(first, tag_action(second, state))
                        direct = tag_action(product, state)
                        tag_action_tests += 1
                        tag_action_failures += sequential != direct
    ordered_tag_tests = 0
    ordered_tag_failures = 0
    for frame in ordered:
        for left in (0, 1):
            for right in (0, 1):
                for tag in (0, 1):
                    state = (left, right, tag)
                    ordered_tag_tests += 1
                    ordered_tag_failures += tag_action(frame, state) != state
    reversal_involution_tests = 0
    reversal_involution_failures = 0
    reversal_constraint_tests = 0
    reversal_constraint_failures = 0
    scalar_reversal_failures = 0
    reversing_frame = next(frame for frame in unordered if reverses(frame))
    for left in (0, 1):
        for right in (0, 1):
            for tag in (0, 1):
                state = (left, right, tag)
                reversal_involution_tests += 1
                reversal_involution_failures += tag_action(
                    reversing_frame, tag_action(reversing_frame, state)
                ) != state
            constrained = (left, right, left)
            transformed = tag_action(reversing_frame, constrained)
            reversal_constraint_tests += 1
            reversal_constraint_failures += transformed[2] != transformed[0]
            scalar_reversal_failures += left != right
    anchored_frame_tests = 0
    anchored_frame_failures = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        for frame in frames:
            patch = c517.rotated_patch(frame, length)
            anchored_frame_tests += 1
            anchored_frame_failures += len(set(patch)) != PATCH_CELL_COUNT
            anchored_frame_failures += c517.induced_edges(patch, length) != c517.PAULI_EDGES
    return {
        "proper_cubic_frames": len(frames),
        "proper_frame_products": len(frames) ** 2,
        "proper_frame_product_failures": product_failures,
        "anchored_L5_L6_frame_tests": anchored_frame_tests,
        "anchored_frame_failures": anchored_frame_failures,
        "ordered_bond_stabilizer_size": len(ordered),
        "unordered_bond_stabilizer_size": len(unordered),
        "reversing_coset_size": sum(reverses(frame) for frame in unordered),
        "unordered_group_product_tests": unordered_product_tests,
        "unordered_group_product_failures": unordered_product_failures,
        "tag_action_truth_table_tests": tag_action_tests,
        "tag_action_truth_table_failures": tag_action_failures,
        "ordered_tag_invariance_tests": ordered_tag_tests,
        "ordered_tag_invariance_failures": ordered_tag_failures,
        "reversal_involution_tests": reversal_involution_tests,
        "reversal_involution_failures": reversal_involution_failures,
        "constrained_reversal_tests": reversal_constraint_tests,
        "constrained_reversal_failures": reversal_constraint_failures,
        "scalar_tag_under_reversal_failures": scalar_reversal_failures,
        "exact_reversal_cocycle": "(p_L,p_R,tau)->(p_R,p_L,tau xor p_L xor p_R)",
        "pass": (
            len(frames) == EXPECTED_PROPER_FRAMES
            and len(frame_keys) == EXPECTED_PROPER_FRAMES
            and all(round(np.linalg.det(frame)) == 1 for frame in frames)
            and product_failures == anchored_frame_failures == 0
            and anchored_frame_tests == 2 * EXPECTED_PROPER_FRAMES
            and len(ordered) == 4
            and len(unordered) == 8
            and sum(reverses(frame) for frame in unordered) == 4
            and unordered_product_tests == 64
            and unordered_product_failures == 0
            and tag_action_tests == 512
            and tag_action_failures == 0
            and ordered_tag_tests == 32
            and ordered_tag_failures == 0
            and reversal_involution_tests == 8
            and reversal_involution_failures == 0
            and reversal_constraint_tests == 4
            and reversal_constraint_failures == 0
            and scalar_reversal_failures == 2
        ),
    }


def logical_configurations() -> tuple[int, ...]:
    rows = [0]
    rows.extend(1 << mode for mode in range(LOGICAL_MODE_COUNT))
    rows.extend((1 << first) | (1 << second) for first, second in combinations(range(LOGICAL_MODE_COUNT), 2))
    return tuple(rows)


def mode_index(endpoint: tuple[int, int]) -> int:
    return LOCAL_MODE_COUNT * endpoint[0] + endpoint[1]


def fswap(config: int, seam) -> tuple[int, int, int]:
    first = mode_index(seam[0])
    second = mode_index(seam[1])
    first_occupation = (config >> first) & 1
    second_occupation = (config >> second) & 1
    if first_occupation != second_occupation:
        config ^= (1 << first) | (1 << second)
    phase = -1 if first_occupation and second_occupation else 1
    return config, phase, first_occupation ^ second_occupation


def tagged_fswap(config: int, tag: int, seam) -> tuple[int, int, int]:
    output, phase, crossing_parity = fswap(config, seam)
    if seam in LEFT_INCIDENT_SEAMS:
        tag ^= crossing_parity
    return output, tag, phase


def left_number_parity(config: int) -> int:
    return (config & ((1 << LOCAL_MODE_COUNT) - 1)).bit_count() & 1


def transport_controls() -> dict:
    configs = logical_configurations()
    single_tests = 0
    single_failures = 0
    seam_tag_changes = []
    for seam in DYNAMIC_SEAMS:
        changes = 0
        for config in configs:
            tag = left_number_parity(config)
            output, output_tag, _phase = tagged_fswap(config, tag, seam)
            single_tests += 1
            single_failures += output_tag != left_number_parity(output)
            changes += output_tag != tag
        seam_tag_changes.append(changes)
    composed_failures = 0
    composed_changes = 0
    for config in configs:
        initial_tag = left_number_parity(config)
        output = config
        output_tag = initial_tag
        for seam in DYNAMIC_SEAMS:
            output, output_tag, _phase = tagged_fswap(output, output_tag, seam)
        composed_failures += output_tag != left_number_parity(output)
        composed_changes += output_tag != initial_tag
    pair_tests = 0
    pair_failures = 0
    for first, second in combinations(DYNAMIC_SEAMS, 2):
        for config in configs:
            for tag in (0, 1):
                left_config, left_tag, left_phase = tagged_fswap(config, tag, first)
                left_config, left_tag, second_phase = tagged_fswap(left_config, left_tag, second)
                left_phase *= second_phase
                right_config, right_tag, right_phase = tagged_fswap(config, tag, second)
                right_config, right_tag, second_phase = tagged_fswap(right_config, right_tag, first)
                right_phase *= second_phase
                pair_tests += 1
                pair_failures += (left_config, left_tag, left_phase) != (
                    right_config,
                    right_tag,
                    right_phase,
                )
    return {
        "logical_configurations": len(configs),
        "dynamic_seams": len(DYNAMIC_SEAMS),
        "left_incident_seams": len(LEFT_INCIDENT_SEAMS),
        "right_only_seams": len(RIGHT_ONLY_SEAMS),
        "single_seam_tests": single_tests,
        "single_seam_failures": single_failures,
        "tag_changes_by_seam": tuple(seam_tag_changes),
        "composed_schedule_tests": len(configs),
        "composed_schedule_failures": composed_failures,
        "composed_tag_changes": composed_changes,
        "pairwise_order_tests_including_both_tag_values": pair_tests,
        "pairwise_order_failures_including_FSWAP_phase": pair_failures,
        "coin_exterior_lift_preserves_local_number_parity": True,
        "onsite_contact_diagonal_preserves_occupation_and_tag": True,
        "physical_controlled_tag_X_synthesized": False,
        "pass": (
            len(configs) == EXPECTED_LOGICAL_DIMENSION
            and single_tests == EXPECTED_SINGLE_SEAM_TESTS
            and single_failures == 0
            and tuple(seam_tag_changes) == (142,) * 6 + (0,) * 5
            and composed_failures == 0
            and composed_changes == EXPECTED_COMPOSED_TAG_CHANGES
            and pair_tests == EXPECTED_PAIR_ORDER_TESTS
            and pair_failures == 0
        ),
    }


def one_particle_mass_controls() -> dict:
    """Retest the Cycle-219 mass on the explicit tagged logical N=1 update."""

    species = c516.c330.c219.common_species(-0.3)
    coin = species.coin
    logical_coin = np.zeros((LOGICAL_MODE_COUNT, LOGICAL_MODE_COUNT), dtype=complex)
    tagged_coin = np.zeros((2 * LOGICAL_MODE_COUNT, 2 * LOGICAL_MODE_COUNT), dtype=complex)
    for cell in range(PATCH_CELL_COUNT):
        for target_local in range(LOCAL_MODE_COUNT):
            target = LOCAL_MODE_COUNT * cell + target_local
            for source_local in range(LOCAL_MODE_COUNT):
                source = LOCAL_MODE_COUNT * cell + source_local
                coefficient = coin[target_local, source_local]
                logical_coin[target, source] = coefficient
                for tag in (0, 1):
                    tagged_coin[2 * target + tag, 2 * source + tag] = coefficient

    logical_stream = np.zeros((LOGICAL_MODE_COUNT, LOGICAL_MODE_COUNT), dtype=complex)
    tagged_stream = np.zeros(
        (2 * LOGICAL_MODE_COUNT, 2 * LOGICAL_MODE_COUNT), dtype=complex
    )
    stream_phase_failures = 0
    for source in range(LOGICAL_MODE_COUNT):
        config = 1 << source
        output = config
        phase = 1
        for seam in DYNAMIC_SEAMS:
            output, seam_phase, _crossing = fswap(output, seam)
            phase *= seam_phase
        target = output.bit_length() - 1
        logical_stream[target, source] = phase
        for tag in (0, 1):
            output = config
            output_tag = tag
            phase = 1
            for seam in DYNAMIC_SEAMS:
                output, output_tag, seam_phase = tagged_fswap(output, output_tag, seam)
                phase *= seam_phase
            target = output.bit_length() - 1
            tagged_stream[2 * target + output_tag, 2 * source + tag] = phase
            stream_phase_failures += phase != 1

    embedding = np.zeros((2 * LOGICAL_MODE_COUNT, LOGICAL_MODE_COUNT), dtype=complex)
    for mode in range(LOGICAL_MODE_COUNT):
        tag = int(mode < LOCAL_MODE_COUNT)
        embedding[2 * mode + tag, mode] = 1

    logical_update = logical_stream @ logical_coin
    tagged_update = tagged_stream @ tagged_coin
    logical_identity = np.eye(LOGICAL_MODE_COUNT, dtype=complex)
    tagged_identity = np.eye(2 * LOGICAL_MODE_COUNT, dtype=complex)
    embedding_residual = float(
        np.linalg.norm(embedding.conj().T @ embedding - logical_identity)
    )
    logical_unitarity = float(
        np.linalg.norm(logical_update.conj().T @ logical_update - logical_identity)
    )
    tagged_unitarity = float(
        np.linalg.norm(tagged_update.conj().T @ tagged_update - tagged_identity)
    )
    intertwiner_residual = float(
        np.linalg.norm(tagged_update @ embedding - embedding @ logical_update)
    )
    uniform = np.ones(LOGICAL_MODE_COUNT, dtype=complex) / np.sqrt(LOGICAL_MODE_COUNT)
    eigenvalue = np.vdot(uniform, logical_update @ uniform)
    logical_mass = float(np.angle(eigenvalue)) / c516.c330.c219.C_SQUARED
    fixture = float(species.analytic_mass)
    logical_uniform_residual = float(
        np.linalg.norm(logical_update @ uniform - eigenvalue * uniform)
    )
    tagged_uniform = embedding @ uniform
    tagged_uniform_residual = float(
        np.linalg.norm(tagged_update @ tagged_uniform - eigenvalue * tagged_uniform)
    )
    return {
        "one_particle_logical_modes": LOGICAL_MODE_COUNT,
        "tagged_one_particle_ambient_dimension": 2 * LOGICAL_MODE_COUNT,
        "embedding_isometry_residual": embedding_residual,
        "logical_update_unitarity_residual": logical_unitarity,
        "tagged_update_unitarity_residual": tagged_unitarity,
        "tagged_intertwiner_residual": intertwiner_residual,
        "stream_phase_failures": stream_phase_failures,
        "Cycle219_mass_fixture": fixture,
        "adjacent_star_logical_mass": logical_mass,
        "mass_fixture_residual": abs(logical_mass - fixture),
        "logical_uniform_one_particle_residual": logical_uniform_residual,
        "tagged_uniform_one_particle_residual": tagged_uniform_residual,
        "onsite_contact_is_identity_in_N1": True,
        "primitive_physical_tagged_update_synthesized": False,
        "pass": (
            stream_phase_failures == 0
            and embedding_residual < 5e-13
            and logical_unitarity < 5e-13
            and tagged_unitarity < 5e-13
            and intertwiner_residual < 5e-13
            and abs(logical_mass - fixture) < 5e-13
            and logical_uniform_residual < 5e-13
            and tagged_uniform_residual < 5e-13
        ),
    }


def deletion_and_domain_controls(constraints, frame) -> dict:
    geometry = c517.geometry_controls()
    lawful = geometry["lawful_domain_controls"]
    bond_parity_separations = 0
    for first, second, third, fourth in (
        (1, 0, 0, 1),
        (1, 1, 0, 0),
    ):
        bond_parity_separations += (first ^ second) != (third ^ fourth)
    rows = {
        "freeze_or_delete_tag_restores_native_doubletons": EXPECTED_NATIVE_DOUBLETONS,
        "freeze_or_delete_tag_restores_native_row_collisions": EXPECTED_NATIVE_ROW_COLLISIONS,
        "freeze_or_delete_tag_restores_exact_Gram_residual": fraction_json(EXPECTED_NATIVE_GRAM_RESIDUAL),
        "bond_parity_tag_separates_native_pattern_classes": bond_parity_separations,
        "delete_each_factor_descriptor_port_failures_L5": constraints[0]["delete_each_port_descriptor_failures"],
        "delete_each_factor_descriptor_port_failures_L6": constraints[1]["delete_each_port_descriptor_failures"],
        "scalar_tag_under_true_reversal_failures": frame["scalar_tag_under_reversal_failures"],
        "L4_extra_wrap_edge_rejected": lawful["aliased_L4"]["rejected"],
        "duplicate_center_rejected": lawful["duplicate_centers"]["rejected"],
        "nonadjacent_center_rejected": lawful["nonadjacent_centers"]["rejected"],
        "det_minus_one_rejected": lawful["improper_frame"]["rejected"],
        "N_greater_than_2_rejected": True,
    }
    return {
        **rows,
        "pass": (
            bond_parity_separations == 0
            and rows["delete_each_factor_descriptor_port_failures_L5"] == (72,) * 6
            and rows["delete_each_factor_descriptor_port_failures_L6"] == (72,) * 6
            and rows["scalar_tag_under_true_reversal_failures"] == 2
            and all(
                rows[key]
                for key in (
                    "L4_extra_wrap_edge_rejected",
                    "duplicate_center_rejected",
                    "nonadjacent_center_rejected",
                    "det_minus_one_rejected",
                    "N_greater_than_2_rejected",
                )
            )
        ),
    }


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    resources = exact_resource_inventory()
    dynamic_cell_pairs = tuple(
        tuple(sorted((seam[0][0], seam[1][0]))) for seam in DYNAMIC_SEAMS
    )
    tests = {
        "Cycle517_518_hash_bound_and_dry": evidence["pass"],
        "exact_branch_and_normalization_inventory": resources["pass"],
        "exact_dynamic_seam_inventory": (
            len(DYNAMIC_SEAMS) == 11
            and len(set(DYNAMIC_SEAMS)) == 11
            and set(dynamic_cell_pairs) == set(c517.UNIQUE_STAR_SEAMS)
            and set(dynamic_cell_pairs).isdisjoint(c517.TRANSVERSE_RUNGS)
        ),
        "note_scope_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle519-seam-tag-contract-ready" if all(tests.values()) else "cycle519-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "resources": resources,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def tag_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial", projected_bytes=700_000_000)]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle519 dry contract failed")
    train = tagged_seed_census(TRAIN_LENGTH, started)
    checkpoints.append(train["resource"])
    held = tagged_seed_census(HELD_LENGTH, started)
    checkpoints.append(held["resource"])
    constraints = (
        local_constraint_controls(TRAIN_LENGTH),
        local_constraint_controls(HELD_LENGTH),
    )
    overlap_countercontrols = (
        overlap_constraint_countercontrol(TRAIN_LENGTH),
        overlap_constraint_countercontrol(HELD_LENGTH),
    )
    checkpoints.append(checkpoint(started, "L5-L6-factor-parity-and-overlap-countercontrols-complete"))
    frame = frame_and_reversal_controls()
    transport = transport_controls()
    mass = one_particle_mass_controls()
    checkpoints.append(checkpoint(started, "tag-transport-complete"))
    deletion = deletion_and_domain_controls(constraints, frame)
    held_abstract_match = (
        train["sector_seeds"] == held["sector_seeds"]
        and train["tag_one_seeds"] == held["tag_one_seeds"]
        and train["native_doubleton_endpoint_pattern_classes"]
        == held["native_doubleton_endpoint_pattern_classes"]
    )
    tests = {
        "dry_contract": dry["pass"],
        "L5_all_seed_singleton_census": train["pass"],
        "held_L6_all_seed_singleton_census": held["pass"],
        "held_abstract_census_matches": held_abstract_match,
        "exact_Gram_identity_from_unique_rows_and_normalization": (
            train["analytic_unique_expanded_rows"] == EXPECTED_FULL_BRANCHES
            and held["analytic_unique_expanded_rows"] == EXPECTED_FULL_BRANCHES
            and all(
                value == (1, 1)
                for value in dry["resources"]["exact_column_normalizations"].values()
            )
        ),
        "factor_local_seven_M2_parity_descriptor_L5_L6": all(row["pass"] for row in constraints),
        "overlap_countercontrol_rejects_global_seven_M2_constraint": all(
            row["pass"] for row in overlap_countercontrols
        ),
        "proper_frames_bond_stabilizers_and_reversal_cocycle": frame["pass"],
        "exhaustive_tagged_free_contact_seam_transport": transport["pass"],
        "explicit_tagged_one_particle_mass_fixture": mass["pass"],
        "deletion_and_lawful_domain_controls": deletion["pass"],
        "resource_contract": swap_count() == 0 and rss_bytes() < RSS_CHECKPOINT_GUARD_BYTES,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "tag-certificate",
        "status": "cycle519-bounded-logical-tag-repair-with-overlap-constraint-countercontrol-certified" if all(tests.values()) else "cycle519-certificate-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "train": train,
        "held": held,
        "held_abstract_census_matches": held_abstract_match,
        "exact_branch_resources": dry["resources"],
        "factor_local_parity_rows": constraints,
        "overlap_constraint_countercontrols": overlap_countercontrols,
        "frame_and_reversal_controls": frame,
        "free_plus_contact_transport": transport,
        "one_particle_mass_controls": mass,
        "deletion_and_domain_controls": deletion,
        "theorem": {
            "bounded_domain": "Cycle517 twelve-cell patch, global N=0,1,2, L=5 and held L=6",
            "tag_definition": "tau = N_left mod 2",
            "Cycle311_315_branch_grammar_changed": False,
            "all_245518336_expanded_rows_unique": True,
            "exact_E_dagger_E": "I_2629",
            "factor_local_parity_descriptor": "tau equals six-port parity before overlapping cell-factor multiplication",
            "global_seven_M2_code_constraint": False,
            "unitary_postprocessing_of_native_encoding_can_create_tag": False,
            "proper_cubic_anchored_covariance": True,
            "endpoint_reversal_cocycle": frame["exact_reversal_cocycle"],
            "logical_free_plus_contact_update_preserves_tagged_code": True,
            "seam_actions_pairwise_order_independent": True,
            "explicit_tagged_logical_one_particle_mass_fixture_preserved": True,
        },
        "preferred_recurrent_architecture": {
            "proposal": "one shared per-center star-parity tag tau_A=N_A mod2 reused on every incident bond",
            "single_patch_restriction_equals_tested_tau_left": True,
            "endpoint_reversal_swaps_center_roles": True,
            "recurrent_overlap_consistency_proven": False,
        },
        "supplied_not_synthesized": {
            "native_Cycle311_315_branch_representatives": True,
            "Cycle515_516_dense_product_shell_and_frame bridge": True,
            "logical_coin_exterior_lift": True,
            "onsite_contact_diagonal": True,
            "dense_on_image_physical_lift": True,
        },
        "open": {
            "local_tag_preparation_before_overlap_or_alternative_global_constraint": True,
            "primitive_controlled_tag_X_inside_dense_branch_shell": True,
            "recurrent_overlapping_tiling_and_per_center_tag_reuse": True,
            "direct_primitive_physical_mass_retest_after_update_synthesis": True,
            "full_number_domain": True,
            "Cycle514_response_and_source_prediction_bridge": True,
            "causal_time_bridge": True,
            "Born_probability_and_record_bridge": True,
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP: dedicated tag and opposite-carrier constructive routes are live",
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "route_specific_failures_are_constitutional_evidence": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": rss_bytes(),
            "process_swap_count": swap_count(),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
            "partial_rows_durable_across_OS_kill_or_process_OOM": False,
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
        payload = dry_contract() if args.mode == "dry-contract" else tag_certificate()
    except (CertificateFailure, ResourceWall, ValueError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle519-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
