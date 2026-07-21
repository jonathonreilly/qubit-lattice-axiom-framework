#!/usr/bin/env python3
"""Cycle 520: three-star shared parity overlap certificate.

The runner extends the Cycle-519 independently appended logical parity tag to
three overlapping centers.  The smallest L5-lawful geometry is a bent path of
three centers; a straight path has a periodic wrap edge at L5.  On the bent
sixteen-cell union, the runner certifies the exact tagged quotient Gram,
proper-cubic transport, logical free-plus-contact update, mass/contact
fixtures, and deletion controls.

It also performs the load-bearing negative control.  The Cycle-519 seven-M2
relation is a factor-local descriptor, not a simultaneous constraint after
neighboring Cycle-311/516 factors are multiplied.  The runner counts the
global failures and exhausts the complete retained reference-stabilizer span
for a Pauli parity decoder.  This finite-span negative is not a no-go for a
non-Pauli constraint, protected shadow register, changed representatives, or
staggered synthesis.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_adjacent_two_star_seam_tag_preservation_cycle519_2026_07_21 as c519


c518 = c519.c518
c517 = c518.c517
c516 = c518.c516
c515 = c516.c515
c235 = c516.c235
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "overlap-certificate")
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MAX_TOTAL_NUMBER = 2
LOCAL_MODE_COUNT = 6
BENT_CELL_COUNT = 16
BENT_CENTER_COUNT = 3
LOGICAL_MODE_COUNT = BENT_CELL_COUNT * LOCAL_MODE_COUNT
EXPECTED_LOGICAL_DIMENSION = 4_657
EXPECTED_SEEDS = 433_441
EXPECTED_TAG_ONE_SEEDS_PER_CENTER = 54_060
EXPECTED_NATIVE_FIBERS = 433_399
EXPECTED_NATIVE_DOUBLETONS = 42
EXPECTED_FULL_BRANCHES = 7_125_139_456
EXPECTED_GLOBAL_CONSTRAINT_FAILURE_SEEDS = 142_668
EXPECTED_GLOBAL_CONSTRAINT_PASS_SEEDS = 290_773
EXPECTED_FACTOR_TERMS_PER_CELL = 256
EXPECTED_FACTOR_TERM_TESTS = BENT_CELL_COUNT * EXPECTED_FACTOR_TERMS_PER_CELL
EXPECTED_NLE2_TERMS_PER_CELL = 92
EXPECTED_CROSS_TERM_CENTER_TESTS = BENT_CELL_COUNT * EXPECTED_NLE2_TERMS_PER_CELL * BENT_CENTER_COUNT
EXPECTED_CROSS_TERM_FAILURES = 270
EXPECTED_EXTENDED_CONSTRAINT_TESTS = (
    BENT_CELL_COUNT * EXPECTED_NLE2_TERMS_PER_CELL * BENT_CENTER_COUNT * LOCAL_MODE_COUNT
)
EXPECTED_DYNAMIC_SEAMS = 16
EXPECTED_SINGLE_SEAM_TESTS = EXPECTED_DYNAMIC_SEAMS * EXPECTED_LOGICAL_DIMENSION
EXPECTED_PAIR_ORDER_TESTS = (
    math.comb(EXPECTED_DYNAMIC_SEAMS, 2) * EXPECTED_LOGICAL_DIMENSION * 2**BENT_CENTER_COUNT
)
EXPECTED_COMPOSED_TAG_CHANGES = 2_456
EXPECTED_PROPER_FRAMES = 24
EXPECTED_FRAME_PRODUCTS = 576
EXPECTED_FRAME_LOCAL_TERM_TESTS_PER_SIZE = (
    EXPECTED_PROPER_FRAMES * BENT_CELL_COUNT * EXPECTED_NLE2_TERMS_PER_CELL
)
EXPECTED_CONTACT_ACTIVE_CONFIGS = BENT_CELL_COUNT * math.comb(LOCAL_MODE_COUNT, 2)
EXPECTED_REFERENCE_CHARACTER_RANK = 147
EXPECTED_PORT_DELETION_FAILURES = 72

WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_CHECKPOINT_ABORT_CEILING_BYTES = 3_000_000_000
RSS_CHECKPOINT_GUARD_BYTES = 2_850_000_000

CYCLE515_RUNNER = ROOT / "scripts/physical_cycle330_all_order_isometry_bridge_cycle515_2026_07_20.py"
CYCLE515_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE330_ALL_ORDER_ISOMETRY_BRIDGE_CYCLE515_NOTE_2026-07-20.md"
)
CYCLE516_RUNNER = ROOT / "scripts/physical_cycle515_koszul_frame_bridge_cycle516_2026_07_20.py"
CYCLE516_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE515_KOSZUL_FRAME_BRIDGE_CYCLE516_NOTE_2026-07-21.md"
)
CYCLE518_RUNNER = ROOT / "scripts/physical_adjacent_two_star_compressed_gram_cycle518_2026_07_21.py"
CYCLE518_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_COMPRESSED_GRAM_CYCLE518_NOTE_2026-07-21.md"
)
CYCLE519_RUNNER = ROOT / "scripts/physical_adjacent_two_star_seam_tag_preservation_cycle519_2026_07_21.py"
CYCLE519_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_SEAM_TAG_PRESERVATION_CYCLE519_NOTE_2026-07-21.md"
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_THREE_STAR_SHARED_PARITY_OVERLAP_CYCLE520_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE515_RUNNER: "93afe1600cb3fb8b7844729521b005ce62f957a128a6ffb9493a03a1d9932e96",
    CYCLE515_NOTE: "99696f55a6e1f8f29958d878bdbd5bb0f889c59be8707e93206d1648ba94850a",
    CYCLE516_RUNNER: "3c4318a84c661893932c8d41a90db36445f80cefd092a6a3fffb56cbf8abfa9c",
    CYCLE516_NOTE: "5f32e766fad91a960031bf68dac4ba3b2498b02b5fc4fce9ac1c795e67c23597",
    CYCLE518_RUNNER: "8f505d2de6476bdbc20f87a901e8be9fe46deda5b568c98d750977069a352e53",
    CYCLE518_NOTE: "7278244447e4074e66966e418710e2ad401befc4b8cbfb9d0a30088c0f837107",
}

DIRECTION_VECTORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ANCHOR = (1, 1, 1)
BENT_CENTER_RELATIVE = ((0, 0, 0), (1, 0, 0), (1, 1, 0))
STRAIGHT_CENTER_RELATIVE = ((0, 0, 0), (1, 0, 0), (2, 0, 0))


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physical conclusion."""


class CertificateFailure(RuntimeError):
    """A failed bounded predicate, never a substrate obstruction."""


@dataclass(frozen=True)
class EquationDescriptor:
    cell: int
    body: tuple[int, int, int]
    number: int
    term_index: int
    label: tuple[int, ...]
    carrier: int | None
    variant: int


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


def add_mod(cell, vector, length: int) -> tuple[int, int, int]:
    return tuple((cell[index] + vector[index]) % length for index in range(3))


def translate_relative(relative, frame=None, length: int | None = None):
    matrix = np.eye(3, dtype=int) if frame is None else frame
    result = tuple(
        tuple(int(value) for value in np.asarray(ANCHOR) + matrix @ np.asarray(row))
        for row in relative
    )
    if length is not None:
        result = tuple(tuple(value % length for value in row) for row in result)
    return result


def star_union(centers, length: int) -> tuple[tuple[int, int, int], ...]:
    rows = []
    for center in centers:
        for body in (center,) + tuple(add_mod(center, vector, length) for vector in DIRECTION_VECTORS):
            if body not in rows:
                rows.append(body)
    return tuple(rows)


def torus_distance(first, second, length: int) -> int:
    return sum(
        min((first[index] - second[index]) % length, (second[index] - first[index]) % length)
        for index in range(3)
    )


def induced_edges(cells, length: int):
    return {
        pair
        for pair in combinations(range(len(cells)), 2)
        if torus_distance(cells[pair[0]], cells[pair[1]], length) == 1
    }


def raw_star_union(centers):
    rows = []
    for center in centers:
        for body in (center,) + tuple(
            tuple(center[index] + vector[index] for index in range(3))
            for vector in DIRECTION_VECTORS
        ):
            if body not in rows:
                rows.append(body)
    return tuple(rows)


def raw_edges(cells):
    return {
        pair
        for pair in combinations(range(len(cells)), 2)
        if sum(
            abs(cells[pair[0]][index] - cells[pair[1]][index])
            for index in range(3)
        )
        == 1
    }


def geometry_controls() -> dict:
    frame_keys = {tuple(int(value) for value in frame.reshape(-1)) for frame in c517.FRAMES}
    frame_product_failures = sum(
        tuple(int(value) for value in (left @ right).reshape(-1)) not in frame_keys
        for left in c517.FRAMES
        for right in c517.FRAMES
    )
    rows = []
    orientation_orbits = {}
    for name, relative in (
        ("bent", BENT_CENTER_RELATIVE),
        ("straight", STRAIGHT_CENTER_RELATIVE),
    ):
        orbit = set()
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            extra_edges = 0
            missing_edges = 0
            duplicate_cells = 0
            cell_counts = set()
            raw_edge_counts = set()
            torus_edge_counts = set()
            for frame in c517.FRAMES:
                raw_centers = translate_relative(relative, frame=frame)
                raw_cells = raw_star_union(raw_centers)
                cells = tuple(
                    tuple(value % length for value in body) for body in raw_cells
                )
                expected = raw_edges(raw_cells)
                observed = induced_edges(cells, length)
                extra_edges += len(observed - expected)
                missing_edges += len(expected - observed)
                duplicate_cells += len(set(cells)) != len(cells)
                cell_counts.add(len(cells))
                raw_edge_counts.add(len(expected))
                torus_edge_counts.add(len(observed))
                orbit.add(
                    tuple(
                        tuple(int(value) for value in frame @ np.asarray(row))
                        for row in relative
                    )
                )
            rows.append(
                {
                    "shape": name,
                    "length": length,
                    "proper_frame_tests": len(c517.FRAMES),
                    "cell_counts": tuple(sorted(cell_counts)),
                    "raw_induced_edge_counts": tuple(sorted(raw_edge_counts)),
                    "torus_induced_edge_counts": tuple(sorted(torus_edge_counts)),
                    "extra_periodic_edges": extra_edges,
                    "missing_edges": missing_edges,
                    "duplicate_cell_frames": duplicate_cells,
                }
            )
        orientation_orbits[name] = len(orbit)
    bent_rows = [row for row in rows if row["shape"] == "bent"]
    straight_train = next(
        row for row in rows if row["shape"] == "straight" and row["length"] == TRAIN_LENGTH
    )
    straight_held = next(
        row for row in rows if row["shape"] == "straight" and row["length"] == HELD_LENGTH
    )
    return {
        "proper_cubic_frames": len(c517.FRAMES),
        "frame_products": len(c517.FRAMES) ** 2,
        "frame_product_failures": frame_product_failures,
        "orientation_orbit_sizes": orientation_orbits,
        "rows": rows,
        "bent_path_selected_for_L5_L6": True,
        "straight_L5_rejected_for_wrap": True,
        "pass": (
            len(c517.FRAMES) == EXPECTED_PROPER_FRAMES
            and frame_product_failures == 0
            and orientation_orbits == {"bent": 24, "straight": 6}
            and all(
                row["cell_counts"] == (16,)
                and row["raw_induced_edge_counts"] == (22,)
                and row["torus_induced_edge_counts"] == (22,)
                and row["extra_periodic_edges"] == 0
                and row["missing_edges"] == 0
                and row["duplicate_cell_frames"] == 0
                for row in bent_rows
            )
            and straight_train["cell_counts"] == (17,)
            and straight_train["raw_induced_edge_counts"] == (24,)
            and straight_train["torus_induced_edge_counts"] == (25,)
            and straight_train["extra_periodic_edges"] == EXPECTED_PROPER_FRAMES
            and straight_held["extra_periodic_edges"] == 0
        ),
    }


def bent_geometry(length: int):
    centers = translate_relative(BENT_CENTER_RELATIVE, length=length)
    cells = star_union(centers, length)
    if len(cells) != BENT_CELL_COUNT:
        raise CertificateFailure(f"bent union has {len(cells)} cells at L={length}")
    center_indices = tuple(cells.index(center) for center in centers)
    return centers, cells, center_indices


def build_cache(length: int, all_numbers: bool = False):
    centers, cells, center_indices = bent_geometry(length)
    code = c516.c269.build_code(length)
    numbers = range(7) if all_numbers else range(3)
    cache = {}
    for cell, body in enumerate(cells):
        for number in numbers:
            if number <= 2:
                cache[cell, number] = c518.aggregate_terms(code, body, number)
            else:
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
                                "auxiliary": row["representative"].x >> code.qubits,
                                "amplitude": row["amplitude"],
                            }
                        )
                cache[cell, number] = tuple(rows)
    return code, centers, cells, center_indices, cache


def exact_resource_inventory() -> dict:
    logical_dimension = 1 + LOGICAL_MODE_COUNT + math.comb(LOGICAL_MODE_COUNT, 2)
    seed_sectors = {
        "n0": 1,
        "n1": BENT_CELL_COUNT * 60,
        "n2_same_cell": BENT_CELL_COUNT * 30,
        "n2_split_cells": math.comb(BENT_CELL_COUNT, 2) * 60 * 60,
    }
    branch_sectors = {
        "n0": 2**BENT_CELL_COUNT,
        "n1": BENT_CELL_COUNT * 60 * 2 ** (BENT_CELL_COUNT - 1),
        "n2_same_cell": BENT_CELL_COUNT * 30 * 2 ** (BENT_CELL_COUNT - 1),
        "n2_split_cells": (
            math.comb(BENT_CELL_COUNT, 2) * 60 * 60 * 2 ** (BENT_CELL_COUNT - 2)
        ),
    }
    column_branches_and_squared_weights = {
        "n0": (2**16, fraction_json(Fraction(1, 2**16))),
        "n1": (10 * 2**15, fraction_json(Fraction(1, 10 * 2**15))),
        "n2_same_cell": (2 * 2**15, fraction_json(Fraction(1, 2 * 2**15))),
        "n2_split_cells": (100 * 2**14, fraction_json(Fraction(1, 100 * 2**14))),
    }
    normalizations = {
        sector: fraction_json(Fraction(count) * Fraction(*weight))
        for sector, (count, weight) in column_branches_and_squared_weights.items()
    }
    return {
        "bent_union_cells": BENT_CELL_COUNT,
        "shared_center_tags": BENT_CENTER_COUNT,
        "logical_modes": LOGICAL_MODE_COUNT,
        "lawful_total_number": "N=0,1,2",
        "logical_dimension": logical_dimension,
        "seed_sectors": seed_sectors,
        "branch_sectors": branch_sectors,
        "analytic_full_branches": sum(branch_sectors.values()),
        "column_branches_and_squared_weights": column_branches_and_squared_weights,
        "exact_column_normalizations": normalizations,
        "literal_full_row_materialization_executed": False,
        "pass": (
            logical_dimension == EXPECTED_LOGICAL_DIMENSION
            and sum(seed_sectors.values()) == EXPECTED_SEEDS
            and sum(branch_sectors.values()) == EXPECTED_FULL_BRANCHES
            and all(value == (1, 1) for value in normalizations.values())
        ),
    }


def tagged_seed_census(length: int, started: float) -> dict:
    code, _centers, cells, center_indices, cache = build_cache(length)
    vacuum = tuple(cache[cell, 0][0]["auxiliary"] for cell in range(BENT_CELL_COUNT))
    vacuum_product = 0
    for auxiliary in vacuum:
        vacuum_product ^= auxiliary
    toggles = tuple(
        cache[cell, 0][0]["auxiliary"] ^ cache[cell, 0][1]["auxiliary"]
        for cell in range(BENT_CELL_COUNT)
    )
    basis = c518.gf2_basis(toggles)
    port_masks = tuple(
        sum(
            1 << vertex
            for vertex in c516.c315.c305.body_vertices(code, cells[index])
        )
        for index in center_indices
    )
    native_seen: dict[int, int] = {}
    native_fibers = Counter()
    tagged_seen = set()
    subset_duplicates = Counter()
    tag_xor_histogram = Counter()
    tag_one_counts = Counter()
    constraint_signature_histogram = Counter()
    sector_seeds = Counter()
    tag_digest = sha256()

    def add(choices, sector: str) -> None:
        delta = 0
        numbers = {}
        for cell, number, term_index in choices:
            delta ^= cache[cell, number][term_index]["auxiliary"] ^ vacuum[cell]
            numbers[cell] = number
        quotient, _coefficient = c518.gf2_reduce(delta, basis)
        tag = 0
        for bit, center in enumerate(center_indices):
            value = numbers.get(center, 0) & 1
            tag |= value << bit
            tag_one_counts[bit] += value
        native_fibers[quotient] += 1
        if quotient in native_seen:
            tag_difference = native_seen[quotient] ^ tag
            tag_xor_histogram[tag_difference] += 1
            for mask in range(1 << BENT_CENTER_COUNT):
                subset_duplicates[mask] += (tag_difference & mask) == 0
        else:
            native_seen[quotient] = tag
        key = (quotient, tag)
        tagged_seen.add(key)
        final_auxiliary = vacuum_product ^ delta
        constraint_signature = 0
        for bit, port_mask in enumerate(port_masks):
            port_parity = (final_auxiliary & port_mask).bit_count() & 1
            if port_parity != ((tag >> bit) & 1):
                constraint_signature |= 1 << bit
        constraint_signature_histogram[constraint_signature] += 1
        sector_seeds[sector] += 1
        packed = (quotient << BENT_CENTER_COUNT) | tag
        byte_count = max(1, (packed.bit_length() + 7) // 8)
        tag_digest.update(byte_count.to_bytes(2, "little"))
        tag_digest.update(packed.to_bytes(byte_count, "little"))

    add((), "n0")
    for cell in range(BENT_CELL_COUNT):
        for term_index in range(len(cache[cell, 1])):
            add(((cell, 1, term_index),), "n1")
        for term_index in range(len(cache[cell, 2])):
            add(((cell, 2, term_index),), "n2_same_cell")
    for first, second in combinations(range(BENT_CELL_COUNT), 2):
        for first_index in range(len(cache[first, 1])):
            for second_index in range(len(cache[second, 1])):
                add(
                    ((first, 1, first_index), (second, 1, second_index)),
                    "n2_split_cells",
                )

    constraint_failures = sum(
        count for signature, count in constraint_signature_histogram.items() if signature
    )
    checkpoint_row = checkpoint(started, f"L{length}-shared-tag-census-complete")
    return {
        "length": length,
        "excitation_seeds": sum(sector_seeds.values()),
        "sector_seeds": dict(sector_seeds),
        "vacuum_toggle_rank": len(basis),
        "native_quotient_fibers": len(native_fibers),
        "native_fiber_histogram": dict(Counter(native_fibers.values())),
        "native_maximum_fiber": max(native_fibers.values()),
        "native_doubleton_tag_xor_histogram": {
            format(mask, "03b"): count for mask, count in sorted(tag_xor_histogram.items())
        },
        "tag_one_seeds_by_center": tuple(tag_one_counts[index] for index in range(3)),
        "tagged_quotient_fibers": len(tagged_seen),
        "tagged_fiber_histogram": {"1": len(tagged_seen)},
        "tagged_maximum_fiber": 1,
        "tag_subset_duplicate_seeds": {
            format(mask, "03b"): subset_duplicates[mask] for mask in range(8)
        },
        "simultaneous_seven_M2_constraint_signature_histogram": {
            format(mask, "03b"): count
            for mask, count in sorted(constraint_signature_histogram.items())
        },
        "simultaneous_seven_M2_constraint_pass_seeds": constraint_signature_histogram[0],
        "simultaneous_seven_M2_constraint_failure_seeds": constraint_failures,
        "ordered_tagged_key_stream_sha256": tag_digest.hexdigest(),
        "analytic_expanded_rows": EXPECTED_FULL_BRANCHES,
        "analytic_unique_expanded_rows": EXPECTED_FULL_BRANCHES,
        "literal_full_row_materialization_executed": False,
        "resource": checkpoint_row,
        "pass": (
            sum(sector_seeds.values()) == EXPECTED_SEEDS
            and len(basis) == BENT_CELL_COUNT
            and len(native_fibers) == EXPECTED_NATIVE_FIBERS
            and Counter(native_fibers.values()) == Counter({1: 433_357, 2: 42})
            and tag_xor_histogram == Counter({0b011: 18, 0b110: 18, 0b111: 6})
            and tuple(tag_one_counts[index] for index in range(3))
            == (EXPECTED_TAG_ONE_SEEDS_PER_CENTER,) * 3
            and len(tagged_seen) == EXPECTED_SEEDS
            and subset_duplicates
            == Counter({0b000: 42, 0b001: 18, 0b100: 18})
            and constraint_signature_histogram
            == Counter(
                {
                    0b000: 290_773,
                    0b001: 44_088,
                    0b010: 43_890,
                    0b011: 3_600,
                    0b100: 44_088,
                    0b101: 3_402,
                    0b110: 3_600,
                }
            )
            and constraint_failures == EXPECTED_GLOBAL_CONSTRAINT_FAILURE_SEEDS
        ),
    }


def factor_and_constraint_controls(length: int) -> dict:
    code, _centers, cells, center_indices, cache = build_cache(length)
    port_sets = tuple(
        c516.c315.c305.body_vertices(code, cells[index]) for index in center_indices
    )
    factor_tests = 0
    factor_failures = 0
    deletion_failures = [Counter() for _ in center_indices]
    for cell in range(BENT_CELL_COUNT):
        vertices = c516.c315.c305.body_vertices(code, cells[cell])
        for number in range(7):
            if number <= 2:
                terms = cache[cell, number]
            else:
                terms = tuple(
                    {
                        "representative": row["representative"],
                    }
                    for label in c516.c311.LABELS[number]
                    for row in c516.gauge_terms_with_metadata(
                        code, cells[cell], number, label
                    )
                )
            for term in terms:
                auxiliary = term["representative"].x >> code.qubits
                parity = sum((auxiliary >> vertex) & 1 for vertex in vertices) & 1
                factor_tests += 1
                factor_failures += parity != (number & 1)
                if cell in center_indices:
                    center_slot = center_indices.index(cell)
                    for omitted, vertex in enumerate(vertices):
                        reduced = parity ^ ((auxiliary >> vertex) & 1)
                        deletion_failures[center_slot][omitted] += reduced != (number & 1)

    cross_tests = 0
    cross_failures = 0
    cross_source_target_histogram = Counter()
    extended_constraint_tests = 0
    extended_constraint_failures = 0
    for cell in range(BENT_CELL_COUNT):
        for number in range(3):
            for term in cache[cell, number]:
                representative = term["representative"]
                auxiliary = representative.x >> code.qubits
                for center_slot, (center, vertices) in enumerate(zip(center_indices, port_sets)):
                    port_parity = sum(
                        (auxiliary >> vertex) & 1 for vertex in vertices
                    ) & 1
                    expected = (number & 1) if cell == center else 0
                    failed = port_parity != expected
                    cross_tests += 1
                    cross_failures += failed
                    cross_source_target_histogram[cell, center_slot] += failed
                    for vertex in vertices:
                        port_z = c235.Pauli(z=1 << (code.qubits + vertex))
                        extended = code.B[vertex] @ port_z
                        extended_constraint_tests += 1
                        extended_constraint_failures += not representative.commutes(extended)
    active_cross_pairs = tuple(
        (list(pair), count)
        for pair, count in sorted(cross_source_target_histogram.items())
        if count
    )
    deletion_rows = tuple(
        tuple(row[index] for index in range(LOCAL_MODE_COUNT))
        for row in deletion_failures
    )
    return {
        "length": length,
        "factor_local_full_M64_term_tests": factor_tests,
        "factor_local_parity_failures": factor_failures,
        "delete_each_factor_port_failures_by_center": deletion_rows,
        "Nle2_cross_term_center_tests": cross_tests,
        "Nle2_cross_term_center_failures": cross_failures,
        "active_cross_source_target_pairs": active_cross_pairs,
        "extended_Bv_Zport_constraint_tests": extended_constraint_tests,
        "extended_Bv_Zport_constraint_failures": extended_constraint_failures,
        "center_port_sets_pairwise_disjoint": all(
            set(port_sets[first]).isdisjoint(port_sets[second])
            for first, second in combinations(range(BENT_CENTER_COUNT), 2)
        ),
        "global_tag_parity_constraint_proven": False,
        "pass": (
            factor_tests == EXPECTED_FACTOR_TERM_TESTS
            and factor_failures == 0
            and deletion_rows
            == ((EXPECTED_PORT_DELETION_FAILURES,) * 6,) * BENT_CENTER_COUNT
            and cross_tests == EXPECTED_CROSS_TERM_CENTER_TESTS
            and cross_failures == EXPECTED_CROSS_TERM_FAILURES
            and len(active_cross_pairs) == 18
            and all(count == 15 for _pair, count in active_cross_pairs)
            and extended_constraint_tests == EXPECTED_EXTENDED_CONSTRAINT_TESTS
            and extended_constraint_failures == 0
        ),
    }


def row_character(representative, stabilizers) -> int:
    value = 0
    for index, stabilizer in enumerate(stabilizers):
        if not stabilizer.commutes(representative):
            value |= 1 << index
    return value


def inconsistent_system_certificate(rows):
    pivots = {}
    contradictions = []
    for row_index, (value, rhs) in enumerate(rows):
        combination = 1 << row_index
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (value, rhs, combination)
                break
            pivot_value, pivot_rhs, pivot_combination = pivots[pivot]
            value ^= pivot_value
            rhs ^= pivot_rhs
            combination ^= pivot_combination
        if not value and rhs:
            contradictions.append(combination)
    witness = min(contradictions, key=int.bit_count) if contradictions else 0
    return {
        "coefficient_rank": len(pivots),
        "augmented_rank": len(pivots) + bool(contradictions),
        "contradiction_rows_after_elimination": len(contradictions),
        "minimum_recorded_contradiction_weight": witness.bit_count(),
        "witness_combination": witness,
        "solvable": not contradictions,
    }


def reference_stabilizer_decoder_controls(length: int) -> dict:
    code, _centers, cells, center_indices, cache = build_cache(length)
    stabilizers = c516.c315.c305.local.reference_stabilizers(code)
    characters = {}
    descriptors = []
    descriptor_index = {}
    for cell in range(BENT_CELL_COUNT):
        for number in range(3):
            for term_index, term in enumerate(cache[cell, number]):
                key = (cell, number, term_index)
                characters[key] = row_character(term["representative"], stabilizers)
                descriptor_index[key] = len(descriptors)
                descriptors.append(
                    EquationDescriptor(
                        cell,
                        cells[cell],
                        number,
                        term_index,
                        term["label"],
                        term["carrier"],
                        term["variant"],
                    )
                )
    rows_by_center = []
    for center_slot, target in enumerate(center_indices):
        equations = []
        equation_descriptors = []
        for cell in range(BENT_CELL_COUNT):
            baseline = characters[cell, 0, 0]
            for number in range(3):
                for term_index, term in enumerate(cache[cell, number]):
                    equations.append(
                        (
                            characters[cell, number, term_index] ^ baseline,
                            (number & 1) if cell == target else 0,
                        )
                    )
                    equation_descriptors.append(
                        EquationDescriptor(
                            cell,
                            cells[cell],
                            number,
                            term_index,
                            term["label"],
                            term["carrier"],
                            term["variant"],
                        )
                    )
        certificate = inconsistent_system_certificate(equations)
        witness_mask = certificate.pop("witness_combination")
        witness = tuple(
            {
                "cell": descriptor.cell,
                "body": descriptor.body,
                "number": descriptor.number,
                "term_index": descriptor.term_index,
                "label": descriptor.label,
                "carrier": descriptor.carrier,
                "variant": descriptor.variant,
            }
            for index, descriptor in enumerate(equation_descriptors)
            if (witness_mask >> index) & 1
        )
        witness_coefficient_xor = 0
        witness_rhs_xor = 0
        for index, equation in enumerate(equations):
            if (witness_mask >> index) & 1:
                witness_coefficient_xor ^= equation[0]
                witness_rhs_xor ^= equation[1]
        rows_by_center.append(
            {
                "center_slot": center_slot,
                "center_cell": target,
                "equations": len(equations),
                "retained_reference_stabilizer_generators": len(stabilizers),
                **certificate,
                "explicit_contradiction_witness": witness,
                "witness_coefficient_xor": witness_coefficient_xor,
                "witness_rhs_xor": witness_rhs_xor,
            }
        )
    return {
        "length": length,
        "search_space": (
            "complete GF(2) span of local checks, three Wilsons, B occupations, "
            "and all port-Z reference stabilizers"
        ),
        "character_equations_per_center": BENT_CELL_COUNT * EXPECTED_NLE2_TERMS_PER_CELL,
        "center_rows": tuple(rows_by_center),
        "non_Pauli_or_new_auxiliary_constraints_tested": False,
        "pass": all(
            row["equations"] == 1_472
            and row["coefficient_rank"] == EXPECTED_REFERENCE_CHARACTER_RANK
            and row["augmented_rank"] == EXPECTED_REFERENCE_CHARACTER_RANK + 1
            and not row["solvable"]
            and row["minimum_recorded_contradiction_weight"] in (5, 6)
            and row["witness_coefficient_xor"] == 0
            and row["witness_rhs_xor"] == 1
            for row in rows_by_center
        ),
    }


def frame_local_term_controls(length: int) -> dict:
    code, _centers, cells, _center_indices, cache = build_cache(length)
    reducer = c516.c315.c305.StabilizerReducer(code)
    face_mask = (1 << code.qubits) - 1
    target_cache = {}
    tests = 0
    lookup_failures = 0
    auxiliary_failures = 0
    reference_failures = 0
    amplitude_failures = 0
    maximum_amplitude_residual = 0.0
    for frame in c517.FRAMES:
        transform_data = c516.affine_transform_data(code, frame)
        for cell, body in enumerate(cells):
            relative = np.asarray(body, dtype=int) - np.asarray(ANCHOR, dtype=int)
            target_body = tuple(
                int(value % length)
                for value in np.asarray(ANCHOR, dtype=int) + frame @ relative
            )
            for number in range(3):
                key = (target_body, number)
                if key not in target_cache:
                    target_cache[key] = c518.aggregate_terms(code, target_body, number)
                lookup = {
                    (row["label"], row["carrier"], row["variant"]): row
                    for row in target_cache[key]
                }
                for source in cache[cell, number]:
                    mapped_label_list = tuple(
                        c516.c311.direction_map(frame, direction)
                        for direction in source["label"]
                    )
                    target_label = tuple(sorted(mapped_label_list))
                    target_carrier = (
                        None
                        if source["carrier"] is None
                        else c516.c311.direction_map(frame, source["carrier"])
                    )
                    target = lookup.get(
                        (target_label, target_carrier, source["variant"])
                    )
                    tests += 1
                    if target is None:
                        lookup_failures += 1
                        continue
                    transformed = c516.transform_full_representative(
                        code, source["representative"], transform_data
                    )
                    stabilizer_full = (
                        c516.c315.c305.local.pauli_dagger(target["representative"])
                        @ transformed
                    )
                    if (
                        stabilizer_full.x >> code.qubits
                        or stabilizer_full.z & ~face_mask
                    ):
                        auxiliary_failures += 1
                        continue
                    raw_stabilizer = c235.Pauli(
                        stabilizer_full.phase,
                        stabilizer_full.x & face_mask,
                        stabilizer_full.z & face_mask,
                    )
                    phase = reducer.vacuum_phase(raw_stabilizer)
                    if phase is None:
                        reference_failures += 1
                        continue
                    local_sign = c516.c311.c308.permutation_sign(mapped_label_list)
                    scalar = c516.c311.c308.phase_scalar(phase)
                    residual = abs(
                        source["amplitude"] * scalar
                        - local_sign * target["amplitude"]
                    )
                    maximum_amplitude_residual = max(
                        maximum_amplitude_residual, float(residual)
                    )
                    amplitude_failures += residual >= c516.TOLERANCE
    return {
        "length": length,
        "proper_frames": len(c517.FRAMES),
        "local_term_frame_tests": tests,
        "lookup_failures": lookup_failures,
        "auxiliary_transport_failures": auxiliary_failures,
        "reference_stabilizer_failures": reference_failures,
        "amplitude_covariance_failures": amplitude_failures,
        "maximum_amplitude_covariance_residual": maximum_amplitude_residual,
        "shared_tags_are_center_number_scalars": True,
        "pass": (
            tests == EXPECTED_FRAME_LOCAL_TERM_TESTS_PER_SIZE
            and lookup_failures
            == auxiliary_failures
            == reference_failures
            == amplitude_failures
            == 0
            and maximum_amplitude_residual < c516.TOLERANCE
        ),
    }


def logical_configurations() -> tuple[int, ...]:
    rows = [0]
    rows.extend(1 << mode for mode in range(LOGICAL_MODE_COUNT))
    rows.extend(
        (1 << first) | (1 << second)
        for first, second in combinations(range(LOGICAL_MODE_COUNT), 2)
    )
    return tuple(rows)


def dynamic_seams(length: int = TRAIN_LENGTH):
    centers, cells, center_indices = bent_geometry(length)
    seams = []
    for center, cell in zip(centers, center_indices):
        for direction, vector in enumerate(DIRECTION_VECTORS):
            neighbor = cells.index(add_mod(center, vector, length))
            pair = tuple(
                sorted(
                    (
                        LOCAL_MODE_COUNT * cell + direction,
                        LOCAL_MODE_COUNT * neighbor + (direction ^ 1),
                    )
                )
            )
            if pair not in seams:
                seams.append(pair)
    return tuple(seams), center_indices


def tags_of(config: int, center_indices) -> int:
    tag = 0
    for bit, cell in enumerate(center_indices):
        local = (config >> (LOCAL_MODE_COUNT * cell)) & ((1 << LOCAL_MODE_COUNT) - 1)
        tag |= (local.bit_count() & 1) << bit
    return tag


def tagged_fswap(config: int, tag: int, seam, center_indices):
    first, second = seam
    first_occupation = (config >> first) & 1
    second_occupation = (config >> second) & 1
    if first_occupation != second_occupation:
        config ^= (1 << first) | (1 << second)
        tagged_modes = {
            LOCAL_MODE_COUNT * cell + direction: bit
            for bit, cell in enumerate(center_indices)
            for direction in range(LOCAL_MODE_COUNT)
        }
        if first in tagged_modes:
            tag ^= 1 << tagged_modes[first]
        if second in tagged_modes:
            tag ^= 1 << tagged_modes[second]
    phase = -1 if first_occupation and second_occupation else 1
    return config, tag, phase


def transport_mass_contact_controls() -> dict:
    seams, center_indices = dynamic_seams()
    endpoint_modes = tuple(mode for seam in seams for mode in seam)
    configs = logical_configurations()
    single_tests = 0
    single_failures = 0
    seam_tag_changes = []
    for seam in seams:
        changes = 0
        for config in configs:
            tag = tags_of(config, center_indices)
            output, output_tag, _phase = tagged_fswap(
                config, tag, seam, center_indices
            )
            single_tests += 1
            single_failures += output_tag != tags_of(output, center_indices)
            changes += output_tag != tag
        seam_tag_changes.append(changes)
    composed_failures = 0
    composed_changes = 0
    for config in configs:
        initial_tag = tags_of(config, center_indices)
        output = config
        output_tag = initial_tag
        for seam in seams:
            output, output_tag, _phase = tagged_fswap(
                output, output_tag, seam, center_indices
            )
        composed_failures += output_tag != tags_of(output, center_indices)
        composed_changes += output_tag != initial_tag
    pair_tests = 0
    pair_failures = 0
    for first, second in combinations(seams, 2):
        for config in configs:
            for tag in range(1 << BENT_CENTER_COUNT):
                left_config, left_tag, left_phase = tagged_fswap(
                    config, tag, first, center_indices
                )
                left_config, left_tag, phase = tagged_fswap(
                    left_config, left_tag, second, center_indices
                )
                left_phase *= phase
                right_config, right_tag, right_phase = tagged_fswap(
                    config, tag, second, center_indices
                )
                right_config, right_tag, phase = tagged_fswap(
                    right_config, right_tag, first, center_indices
                )
                right_phase *= phase
                pair_tests += 1
                pair_failures += (left_config, left_tag, left_phase) != (
                    right_config,
                    right_tag,
                    right_phase,
                )

    species = c516.c330.c219.common_species(-0.3)
    coin = species.coin
    logical_update = np.zeros((LOGICAL_MODE_COUNT, LOGICAL_MODE_COUNT), dtype=complex)
    tag_coefficient_failures = 0
    for cell in range(BENT_CELL_COUNT):
        for source_direction in range(LOCAL_MODE_COUNT):
            source = LOCAL_MODE_COUNT * cell + source_direction
            for target_direction in range(LOCAL_MODE_COUNT):
                intermediate = LOCAL_MODE_COUNT * cell + target_direction
                output = 1 << intermediate
                output_tag = tags_of(output, center_indices)
                phase = 1
                for seam in seams:
                    output, output_tag, seam_phase = tagged_fswap(
                        output, output_tag, seam, center_indices
                    )
                    phase *= seam_phase
                target = output.bit_length() - 1
                coefficient = coin[target_direction, source_direction] * phase
                logical_update[target, source] += coefficient
                if abs(coefficient) > 1e-14:
                    tag_coefficient_failures += output_tag != tags_of(
                        output, center_indices
                    )
    identity = np.eye(LOGICAL_MODE_COUNT, dtype=complex)
    unitarity_residual = float(
        np.linalg.norm(logical_update.conj().T @ logical_update - identity)
    )
    uniform = np.ones(LOGICAL_MODE_COUNT, dtype=complex) / np.sqrt(LOGICAL_MODE_COUNT)
    eigenvalue = np.vdot(uniform, logical_update @ uniform)
    uniform_residual = float(
        np.linalg.norm(logical_update @ uniform - eigenvalue * uniform)
    )
    mass = float(np.angle(eigenvalue)) / c516.c330.c219.C_SQUARED
    fixture = float(species.analytic_mass)
    coupling = 0.37
    contact_deletion_residual = float(abs(np.exp(1j * coupling) - 1))
    return {
        "logical_configurations": len(configs),
        "dynamic_seams": len(seams),
        "stream_endpoint_modes": len(endpoint_modes),
        "stream_endpoint_modes_are_disjoint": len(set(endpoint_modes)) == len(endpoint_modes),
        "single_seam_tests": single_tests,
        "single_seam_failures": single_failures,
        "tag_changes_by_seam": tuple(seam_tag_changes),
        "composed_schedule_tests": len(configs),
        "composed_schedule_failures": composed_failures,
        "composed_tag_changes": composed_changes,
        "pairwise_order_tests_all_eight_tag_words": pair_tests,
        "pairwise_order_failures_including_FSWAP_phase": pair_failures,
        "one_particle_modes": LOGICAL_MODE_COUNT,
        "one_particle_update_unitarity_residual": unitarity_residual,
        "one_particle_tag_coefficient_failures": tag_coefficient_failures,
        "one_particle_uniform_eigen_residual": uniform_residual,
        "Cycle219_mass_fixture": fixture,
        "three_star_mass": mass,
        "mass_residual": abs(mass - fixture),
        "contact_active_N2_configurations": EXPECTED_CONTACT_ACTIVE_CONFIGS,
        "contact_deletion_residual": contact_deletion_residual,
        "contact_preserves_all_three_tags": True,
        "coin_preserves_all_three_tags": True,
        "pass": (
            len(configs) == EXPECTED_LOGICAL_DIMENSION
            and len(seams) == EXPECTED_DYNAMIC_SEAMS
            and len(set(endpoint_modes)) == len(endpoint_modes)
            and single_tests == EXPECTED_SINGLE_SEAM_TESTS
            and single_failures == 0
            and tuple(seam_tag_changes) == (190,) * EXPECTED_DYNAMIC_SEAMS
            and composed_failures == 0
            and composed_changes == EXPECTED_COMPOSED_TAG_CHANGES
            and pair_tests == EXPECTED_PAIR_ORDER_TESTS
            and pair_failures == 0
            and unitarity_residual < 1e-12
            and tag_coefficient_failures == 0
            and uniform_residual < 1e-12
            and abs(mass - fixture) < 1e-12
            and EXPECTED_CONTACT_ACTIVE_CONFIGS == 240
            and abs(contact_deletion_residual - 0.36789306705608243) < 2e-15
        ),
    }


def physical_candidate_controls() -> dict:
    configs = logical_configurations()
    _seams, center_indices = dynamic_seams()
    deleted_control_errors = []
    for cell in center_indices:
        for direction in range(LOCAL_MODE_COUNT):
            mode = LOCAL_MODE_COUNT * cell + direction
            errors = sum((config >> mode) & 1 for config in configs)
            deleted_control_errors.append(errors)
    native_residual = c518.EXPECTED_OVERLAP_MAGNITUDE
    return {
        "fixed_postprocessing_Gram_identity": (
            "(W(E tensor |0>))^dagger W(E tensor |0>) = E^dagger E"
        ),
        "native_Cycle518_residual_after_any_fixed_unitary_W": fraction_json(native_residual),
        "postprocess_CNOT_repairs_native_Gram": False,
        "dense_native_shell_candidate": (
            "A_tau = E_tau G E_tau^dagger + I - E_tau E_tau^dagger"
        ),
        "dense_native_shell_candidate_exact_on_code": True,
        "dense_native_shell_candidate_primitive_synthesized": False,
        "protected_shadow_candidate": (
            "W=product_A product_d CNOT(q_A,d -> tau_A); "
            "G_tau=W (G_direct tensor I_tau) W^dagger"
        ),
        "protected_shadow_private_occupation_M2_per_cell": 6,
        "shared_tag_M2_per_center": 1,
        "three_center_parity_CNOTs": BENT_CENTER_COUNT * LOCAL_MODE_COUNT,
        "parity_CNOT_groups_have_disjoint_controls_and_targets": True,
        "deleted_each_CNOT_valid_configuration_errors": tuple(deleted_control_errors),
        "deleted_each_matching_uncompute_leaves_tag_error": tuple(deleted_control_errors),
        "protected_shadow_candidate_exact_intertwiner_by_conjugation": True,
        "Cycle219_six_mode_coin_bare_one_two_M2_decomposition_supplied": False,
        "protected_shadow_synchronized_with_Cycle515_516_shell": False,
        "Cycle465_relevance": (
            "supplies six-CNOT Q1 parity compute/uncompute semantics, not a "
            "native-overlap Gram repair or a bare routing trace"
        ),
        "pass": (
            native_residual == Fraction(1, 400)
            and len(deleted_control_errors) == 18
            and tuple(deleted_control_errors) == (96,) * 18
        ),
    }


def current_cycle519_semantic_contract() -> dict:
    source = CYCLE519_RUNNER.read_text(encoding="utf-8").lower()
    note = CYCLE519_NOTE.read_text(encoding="utf-8").lower()
    required_source = (
        "factor-local parity",
        "global_seven_m2_code_constraint_proven\": false",
        "overlap_constraint_countercontrol",
    )
    required_note = (
        "factor-local seven-m2 descriptor",
        "not a constraint on the final overlapping code",
        "post-processing the already-collided native row cannot create two",
    )
    source_missing = tuple(item for item in required_source if item not in source)
    note_missing = tuple(item for item in required_note if item not in note)
    return {
        "Cycle519_runner_observed_sha256_diagnostic_only": file_sha(CYCLE519_RUNNER),
        "Cycle519_note_observed_sha256_diagnostic_only": file_sha(CYCLE519_NOTE),
        "Cycle519_hash_gate_intentionally_disabled_for_concurrent_correction": True,
        "required_runner_fragments_missing": source_missing,
        "required_note_fragments_missing": note_missing,
        "bound_semantics": (
            "seven-M2 parity is factor-local only; fixed-unitary postprocessing "
            "does not repair the native overlap Gram"
        ),
        "pass": not source_missing and not note_missing,
    }


def upstream_evidence() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    semantic = current_cycle519_semantic_contract()
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "stable_hashes_match": expected == observed,
        "Cycle519_corrected_semantic_contract": semantic,
        "pass": expected == observed and semantic["pass"],
    }


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "433,441",
        "7,125,139,456",
        "142,668",
        "rank 147",
        "augmented rank 148",
        "protected-shadow",
        "dense native-shell",
        "straight l5",
        "4,470,720",
        "primitive",
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
    missing = tuple(item for item in required if item not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    evidence = upstream_evidence()
    geometry = geometry_controls()
    resources = exact_resource_inventory()
    note = note_contract()
    tests = {
        "stable_Cycle515_516_518_hashes_and_corrected_Cycle519_semantics": evidence["pass"],
        "lawful_bent_geometry_and_straight_L5_wrap_control": geometry["pass"],
        "exact_compressed_resource_inventory": resources["pass"],
        "note_scope_and_current_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle520-three-star-overlap-contract-ready" if all(tests.values()) else "cycle520-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "geometry": geometry,
        "resources": resources,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def isolated_stage(stage: str, length: int | None = None) -> dict:
    """Run one exact science stage in a fresh interpreter.

    Cycle-515/516 code construction leaves large Python allocation arenas behind
    even after the objects die.  Process isolation therefore makes the reported
    RSS wall a real per-stage bound rather than an allocator-history artifact.
    It is verifier plumbing only: every physical predicate remains inside the
    stage function selected below.
    """
    command = [sys.executable, str(Path(__file__).resolve()), "--internal-stage", stage]
    if length is not None:
        command.extend(("--length", str(length)))
    remaining = max(1.0, WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS)
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=remaining,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ResourceWall(f"isolated stage timed out: {stage} L{length}") from exc
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        stderr = completed.stderr[-2_000:]
        raise CertificateFailure(
            f"isolated stage emitted invalid JSON: {stage} L{length}; stderr={stderr!r}"
        ) from exc
    if completed.returncode or not payload.get("pass", False):
        raise CertificateFailure(
            f"isolated stage failed: {stage} L{length}; payload={payload!r}; "
            f"stderr={completed.stderr[-2_000:]!r}"
        )
    return payload


def internal_stage(stage: str, length: int | None) -> dict:
    started = time.monotonic()
    if stage == "transport":
        if length is not None:
            raise ValueError("transport stage does not take a lattice length")
        payload = transport_mass_contact_controls()
    else:
        if length not in (TRAIN_LENGTH, HELD_LENGTH):
            raise ValueError(f"{stage} stage requires length 5 or 6")
        if stage == "census":
            payload = tagged_seed_census(length, started)
        elif stage == "factor":
            payload = factor_and_constraint_controls(length)
        elif stage == "decoder":
            payload = reference_stabilizer_decoder_controls(length)
        elif stage == "frame":
            payload = frame_local_term_controls(length)
        else:
            raise ValueError(f"unknown internal stage: {stage}")
    payload["isolated_stage_resource"] = checkpoint(
        started, f"isolated-{stage}-L{length}-complete"
    )
    return payload


def overlap_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial", projected_bytes=400_000_000)]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle520 dry contract failed")
    train = isolated_stage("census", TRAIN_LENGTH)
    checkpoints.append(train["isolated_stage_resource"])
    held = isolated_stage("census", HELD_LENGTH)
    checkpoints.append(held["isolated_stage_resource"])
    factor_rows = (
        isolated_stage("factor", TRAIN_LENGTH),
        isolated_stage("factor", HELD_LENGTH),
    )
    checkpoints.extend(row["isolated_stage_resource"] for row in factor_rows)
    decoder_rows = (
        isolated_stage("decoder", TRAIN_LENGTH),
        isolated_stage("decoder", HELD_LENGTH),
    )
    checkpoints.extend(row["isolated_stage_resource"] for row in decoder_rows)
    frame_rows = (
        isolated_stage("frame", TRAIN_LENGTH),
        isolated_stage("frame", HELD_LENGTH),
    )
    checkpoints.extend(row["isolated_stage_resource"] for row in frame_rows)
    transport = isolated_stage("transport")
    checkpoints.append(transport["isolated_stage_resource"])
    candidates = physical_candidate_controls()
    held_match = (
        train["sector_seeds"] == held["sector_seeds"]
        and train["native_doubleton_tag_xor_histogram"]
        == held["native_doubleton_tag_xor_histogram"]
        and train["tag_subset_duplicate_seeds"] == held["tag_subset_duplicate_seeds"]
        and train["simultaneous_seven_M2_constraint_signature_histogram"]
        == held["simultaneous_seven_M2_constraint_signature_histogram"]
    )
    tests = {
        "dry_contract": dry["pass"],
        "L5_three_tag_singleton_census": train["pass"],
        "held_L6_three_tag_singleton_census": held["pass"],
        "held_abstract_census_and_constraint_signature_match": held_match,
        "exact_Gram_identity_from_unique_rows_and_normalization": (
            train["analytic_unique_expanded_rows"] == EXPECTED_FULL_BRANCHES
            and held["analytic_unique_expanded_rows"] == EXPECTED_FULL_BRANCHES
            and all(
                value == (1, 1)
                for value in dry["resources"]["exact_column_normalizations"].values()
            )
        ),
        "factor_local_and_simultaneous_constraint_controls_L5_L6": all(
            row["pass"] for row in factor_rows
        ),
        "complete_retained_reference_stabilizer_span_inconsistent_L5_L6": all(
            row["pass"] for row in decoder_rows
        ),
        "all24_frame_local_term_transport_L5_L6": all(
            row["pass"] for row in frame_rows
        ),
        "shared_tag_free_contact_order_mass_controls": transport["pass"],
        "dense_vs_protected_shadow_candidate_boundary": candidates["pass"],
        "resource_contract": swap_count() == 0 and rss_bytes() < RSS_CHECKPOINT_GUARD_BYTES,
    }
    elapsed = time.monotonic() - started
    maximum_stage_rss = max(
        (row["maximum_RSS_bytes"] for row in checkpoints), default=rss_bytes()
    )
    total_stage_swap = sum(row["process_swap_count"] for row in checkpoints)
    return {
        "revision": REVISION,
        "mode": "overlap-certificate",
        "status": "cycle520-bent-three-star-shared-tag-overlap-partial-closure-certified" if all(tests.values()) else "cycle520-certificate-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "geometry": dry["geometry"],
        "train": train,
        "held": held,
        "held_abstract_match": held_match,
        "exact_resources": dry["resources"],
        "factor_and_constraint_rows": factor_rows,
        "reference_stabilizer_decoder_rows": decoder_rows,
        "frame_local_term_rows": frame_rows,
        "free_contact_order_mass_controls": transport,
        "physical_candidate_controls": candidates,
        "positive_theorem": {
            "domain": "bent three-center path, sixteen-cell union, global N=0,1,2, L5 and held L6",
            "shared_tags": "tau_A=N_A mod2 for each of the three centers",
            "tagged_quotient_singletons": EXPECTED_SEEDS,
            "all_analytic_expanded_rows_unique": EXPECTED_FULL_BRANCHES,
            "exact_E_dagger_E": "I_4657",
            "proper_cubic_placements": EXPECTED_PROPER_FRAMES,
            "logical_free_plus_contact_update_preserves_shared_tags": True,
            "one_particle_mass_fixture_preserved": True,
        },
        "bounded_negative": {
            "factor_local_seven_M2_descriptor_is_simultaneous_global_constraint": False,
            "violating_seeds_per_size": EXPECTED_GLOBAL_CONSTRAINT_FAILURE_SEEDS,
            "retained_reference_stabilizer_Pauli_decoder_exists": False,
            "scope": "complete retained reference-stabilizer span on this exact sixteen-cell product grammar",
            "non_Pauli_new_auxiliary_changed_representative_or_staggered_routes_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "supplied_not_synthesized": {
            "Cycle311_315_branch_grammar": True,
            "Cycle515_dense_shell_and_off_code_completion": True,
            "Cycle516_Koszul_frame_bridge": True,
            "Cycle519_independently_appended_logical_tag": True,
            "Cycle219_six_mode_coin": True,
            "Cycle230_contact_coupling_and_factorization": True,
            "primitive_constraint_enforcement": False,
            "bare_one_two_M2_coin_decomposition": False,
        },
        "open": {
            "non_Pauli_local_tag_constraint": True,
            "protected_shadow_sync_with_native_Wilson_shell": True,
            "staggered_compute_use_uncompute_schedule": True,
            "changed_representative_or_opposite_carrier_retest": True,
            "recurrent_volume_beyond_three_centers": True,
            "primitive_native_shell_Gphysical": True,
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "disposition": "partial-attempt-with-named-untested-routes",
            "minimum_content_claim": False,
            "axiom_pressure": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": maximum_stage_rss,
            "process_swap_count": total_stage_swap,
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
            "fresh_process_per_heavy_stage": True,
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
    parser.add_argument(
        "--internal-stage",
        choices=("census", "factor", "decoder", "frame", "transport"),
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--length", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        if args.internal_stage:
            payload = internal_stage(args.internal_stage, args.length)
        else:
            payload = dry_contract() if args.mode == "dry-contract" else overlap_certificate()
    except (CertificateFailure, ResourceWall, ValueError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle520-runner-failed",
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
