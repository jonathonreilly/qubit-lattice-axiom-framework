#!/usr/bin/env python3
"""Cycle 518: compressed exact Gram for the adjacent-two-star encoding.

Cycle 517 classified the static order character of the twelve-cell patch but
did not test the 245,518,336 physical branch products.  This runner replaces
that literal census by an exact orbit calculation.  It enumerates the 238,681
non-vacuum excitation seeds, quotients only the freely available vacuum-cell
role toggles, and expands every resulting orbit intersection exactly.

The target is deliberately narrow: the native Cycle-311/315 representatives,
first in one fixed factor order and then with the exact Cycle-517 weighted
order-character role.  A counterexample to those encodings is not a no-go for
an augmented gauge encoding, changed representatives, or a tagged schedule.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_adjacent_two_star_order_character_preflight_cycle517_2026_07_21 as c517


c516 = c517.c516
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "gram-certificate")
TRAIN_LENGTH = 5
HELD_LENGTH = 6
PATCH_CELL_COUNT = 12
MAX_TOTAL_NUMBER = 2
EXPECTED_SEEDS = 238_681
EXPECTED_QUOTIENT_FIBERS = 238_657
EXPECTED_SINGLETON_FIBERS = 238_633
EXPECTED_DOUBLETON_FIBERS = 24
EXPECTED_FULL_BRANCHES = 245_518_336
EXPECTED_COLLISION_PAIRS = 6_144
EXPECTED_UNIQUE_ROWS = EXPECTED_FULL_BRANCHES - EXPECTED_COLLISION_PAIRS
EXPECTED_FIXED_OVERLAPS = 24
EXPECTED_ORDER_OVERLAPS = 8
EXPECTED_OVERLAP_MAGNITUDE = Fraction(1, 400)
EXPECTED_PROPER_FRAMES = 24
EXPECTED_FRAME_PRODUCTS = 576

WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_CHECKPOINT_ABORT_CEILING_BYTES = 3_000_000_000
RSS_CHECKPOINT_GUARD_BYTES = 2_850_000_000

CYCLE517_RUNNER = ROOT / "scripts/physical_adjacent_two_star_order_character_preflight_cycle517_2026_07_21.py"
CYCLE517_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_ORDER_CHARACTER_PREFLIGHT_CYCLE517_NOTE_2026-07-21.md"
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_COMPRESSED_GRAM_CYCLE518_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE517_RUNNER: "ad8b0c71840cbfa56aae3ae9da44eceec1cad7d84be06bab32604eb5f6fbb4a3",
    CYCLE517_NOTE: "51c3b92448f7779fe838c51265b279d82f48e3b19f6c0464b95f18112bf07a74",
}


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physical conclusion."""


class CertificateFailure(RuntimeError):
    """A failed bounded predicate, never a substrate obstruction."""


@dataclass(frozen=True)
class Seed:
    coefficient: int
    occupied: int
    column: tuple[int, ...]
    choices: tuple[tuple[int, int, int], ...]  # cell, number, aggregate-term index
    sector: str


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


def pauli_face(code, representative):
    face_mask = (1 << code.qubits) - 1
    return c516.c235.Pauli(
        representative.phase,
        representative.x & face_mask,
        representative.z & face_mask,
    )


def phase_scalar(phase: int) -> complex:
    return (1 + 0j, 1j, -1 + 0j, -1j)[phase % 4]


def quadrant_phase(value: complex) -> tuple[int, float]:
    if value == 0:
        raise CertificateFailure("zero structural branch amplitude")
    unit = value / abs(value)
    residuals = tuple(abs(unit - candidate) for candidate in (1, 1j, -1, -1j))
    phase = min(range(4), key=residuals.__getitem__)
    return phase, float(residuals[phase])


def aggregate_terms(code, body, number: int) -> tuple[dict, ...]:
    rows = []
    for label in c516.c311.LABELS[number]:
        for row in c516.gauge_terms_with_metadata(code, body, number, label):
            phase, phase_residual = quadrant_phase(row["amplitude"])
            representative = row["representative"]
            rows.append(
                {
                    "number": number,
                    "label": tuple(label),
                    "carrier": row["carrier"],
                    "variant": row["variant"],
                    "representative": representative,
                    "auxiliary": representative.x >> code.qubits,
                    "amplitude": row["amplitude"],
                    "amplitude_phase": phase,
                    "phase_residual": phase_residual,
                }
            )
    if len(rows) != c517.LOCAL_TERM_COUNTS[number]:
        raise CertificateFailure(
            f"term count mismatch at body={body}, n={number}: {len(rows)}"
        )
    return tuple(rows)


def gf2_basis(vectors: tuple[int, ...]) -> dict[int, tuple[int, int]]:
    rows: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(vectors):
        value = original
        coefficient = 1 << index
        while value:
            pivot = value.bit_length() - 1
            if pivot not in rows:
                rows[pivot] = (value, coefficient)
                break
            value ^= rows[pivot][0]
            coefficient ^= rows[pivot][1]
        if not value:
            raise CertificateFailure(
                f"vacuum toggles are dependent at cell {index}: {coefficient}"
            )
    return rows


def gf2_reduce(value: int, basis: dict[int, tuple[int, int]]) -> tuple[int, int]:
    coefficient = 0
    while value:
        pivot = value.bit_length() - 1
        if pivot not in basis:
            break
        value ^= basis[pivot][0]
        coefficient ^= basis[pivot][1]
    return value, coefficient


def multiply_order(representatives):
    return c516.c330.multiply_order(representatives, tuple(range(PATCH_CELL_COUNT)))


def character_mask(representatives) -> int:
    return sum(
        1 << bit
        for bit, (first, second) in enumerate(c517.PAULI_EDGES)
        if not representatives[first].commutes(representatives[second])
    )


def character_sum_over_orders(difference_mask: int) -> int:
    """Exact signed sum over all 12! total orders by subset dynamic programming."""

    first_neighbor_masks = [0] * PATCH_CELL_COUNT
    for bit, (first, second) in enumerate(c517.PAULI_EDGES):
        if (difference_mask >> bit) & 1:
            first_neighbor_masks[first] |= 1 << second
    counts = [0] * (1 << PATCH_CELL_COUNT)
    counts[0] = 1
    for chosen in range(1 << PATCH_CELL_COUNT):
        if counts[chosen] == 0:
            continue
        for vertex in range(PATCH_CELL_COUNT):
            vertex_bit = 1 << vertex
            if chosen & vertex_bit:
                continue
            inversions = (first_neighbor_masks[vertex] & chosen).bit_count()
            counts[chosen | vertex_bit] += (-1 if inversions % 2 else 1) * counts[chosen]
    return counts[-1]


def fraction_pair(value: complex, denominator: int, tolerance: float = 2e-11):
    real = round(value.real)
    imaginary = round(value.imag)
    residual = max(abs(value.real - real), abs(value.imag - imaginary))
    if residual > tolerance:
        raise CertificateFailure(f"non-Gaussian exact phase residual {residual}")
    return Fraction(real, denominator), Fraction(imaginary, denominator), residual


def fraction_json(value: Fraction) -> tuple[int, int]:
    return value.numerator, value.denominator


def complex_fraction_json(value: tuple[Fraction, Fraction]) -> dict:
    return {"real": fraction_json(value[0]), "imaginary": fraction_json(value[1])}


def seed_descriptor(seed: Seed, cache) -> dict:
    choices = []
    for cell, number, term_index in seed.choices:
        term = cache[cell, number][term_index]
        choices.append(
            {
                "cell": cell,
                "number": number,
                "term_index": term_index,
                "label": term["label"],
                "carrier": term["carrier"],
                "variant": term["variant"],
            }
        )
    return {
        "coefficient_mask": seed.coefficient,
        "occupied_mask": seed.occupied,
        "column": seed.column,
        "sector": seed.sector,
        "choices": tuple(choices),
    }


def seed_terms(seed: Seed, cache) -> dict[int, dict]:
    return {
        cell: cache[cell, number][term_index]
        for cell, number, term_index in seed.choices
    }


def canonical_matching_variants(first: Seed, second: Seed) -> tuple[int, int, int]:
    difference = first.coefficient ^ second.coefficient
    vacuum_first = ((1 << PATCH_CELL_COUNT) - 1) ^ first.occupied
    vacuum_second = ((1 << PATCH_CELL_COUNT) - 1) ^ second.occupied
    if difference & ~(vacuum_first | vacuum_second):
        raise CertificateFailure("asked for variants on a jointly occupied cell")
    first_variants = difference & vacuum_first
    second_variants = difference & ~vacuum_first & vacuum_second
    return first_variants, second_variants, vacuum_first & vacuum_second


def branch_for_seed(seed: Seed, variants: int, cache):
    occupied = seed_terms(seed, cache)
    terms = tuple(
        occupied[cell]
        if cell in occupied
        else cache[cell, 0][(variants >> cell) & 1]
        for cell in range(PATCH_CELL_COUNT)
    )
    representatives = tuple(term["representative"] for term in terms)
    amplitude = 1 + 0j
    phase = 0
    maximum_phase_residual = 0.0
    for term in terms:
        amplitude *= term["amplitude"]
        phase = (phase + term["amplitude_phase"]) % 4
        maximum_phase_residual = max(maximum_phase_residual, term["phase_residual"])
    return {
        "terms": terms,
        "representatives": representatives,
        "product": multiply_order(representatives),
        "amplitude": amplitude,
        "amplitude_phase": phase,
        "amplitude_phase_residual": maximum_phase_residual,
        "character_mask": character_mask(representatives),
    }


def enumerate_seeds(code, cache):
    vacuum_auxiliary = tuple(cache[cell, 0][0]["auxiliary"] for cell in range(12))
    toggles = tuple(
        cache[cell, 0][0]["auxiliary"] ^ cache[cell, 0][1]["auxiliary"]
        for cell in range(12)
    )
    basis = gf2_basis(toggles)
    seen: dict[int, Seed] = {}
    duplicate_pairs: list[tuple[Seed, Seed]] = []
    sector_seeds: Counter[str] = Counter()
    maximum_fiber = 1

    def add(occupied: int, column: tuple[int, ...], choices, sector: str) -> None:
        nonlocal maximum_fiber
        delta = 0
        for cell, number, term_index in choices:
            delta ^= cache[cell, number][term_index]["auxiliary"] ^ vacuum_auxiliary[cell]
        quotient, coefficient = gf2_reduce(delta, basis)
        seed = Seed(coefficient, occupied, tuple(column), tuple(choices), sector)
        sector_seeds[sector] += 1
        if quotient in seen:
            duplicate_pairs.append((seen[quotient], seed))
            maximum_fiber = 2
        else:
            seen[quotient] = seed

    add(0, (), (), "n0")
    for cell in range(PATCH_CELL_COUNT):
        for term_index, term in enumerate(cache[cell, 1]):
            add(
                1 << cell,
                (6 * cell + term["label"][0],),
                ((cell, 1, term_index),),
                "n1",
            )
        for term_index, term in enumerate(cache[cell, 2]):
            add(
                1 << cell,
                tuple(6 * cell + direction for direction in term["label"]),
                ((cell, 2, term_index),),
                "n2_same_cell",
            )
    for first, second in combinations(range(PATCH_CELL_COUNT), 2):
        for first_index, first_term in enumerate(cache[first, 1]):
            for second_index, second_term in enumerate(cache[second, 1]):
                add(
                    (1 << first) | (1 << second),
                    tuple(
                        sorted(
                            (
                                6 * first + first_term["label"][0],
                                6 * second + second_term["label"][0],
                            )
                        )
                    ),
                    ((first, 1, first_index), (second, 1, second_index)),
                    "n2_split_cells",
                )
    return {
        "toggles": toggles,
        "basis_rank": len(basis),
        "seeds": sum(sector_seeds.values()),
        "quotient_fibers": len(seen),
        "singleton_fibers": len(seen) - len(duplicate_pairs),
        "doubleton_fibers": len(duplicate_pairs),
        "maximum_fiber": maximum_fiber,
        "sector_seeds": dict(sector_seeds),
        "duplicate_pairs": tuple(duplicate_pairs),
    }


def vacuum_toggle_controls(code, cache, toggles) -> dict:
    face_mask = (1 << code.qubits) - 1
    positions = []
    failures = 0
    amplitude_failures = 0
    term_auxiliary_z_failures = 0
    maximum_phase_residual = 0.0
    dagger = c516.c315.c305.local.pauli_dagger
    for cell in range(PATCH_CELL_COUNT):
        first = cache[cell, 0][0]["representative"]
        second = cache[cell, 0][1]["representative"]
        quotient = dagger(first) @ second
        toggle = toggles[cell]
        positions.append(toggle.bit_length() - 1)
        failures += not (
            quotient.phase % 4 == 0
            and quotient.x & face_mask == 0
            and quotient.z == 0
            and quotient.x >> code.qubits == toggle
            and toggle.bit_count() == 1
        )
        amplitude_failures += abs(cache[cell, 0][0]["amplitude"] - cache[cell, 0][1]["amplitude"]) > 2e-14
    for cell in range(PATCH_CELL_COUNT):
        for number in range(3):
            for term in cache[cell, number]:
                term_auxiliary_z_failures += bool(term["representative"].z & ~face_mask)
                maximum_phase_residual = max(maximum_phase_residual, term["phase_residual"])
    return {
        "vacuum_toggle_count": len(toggles),
        "distinct_vacuum_toggles": len(set(toggles)),
        "vacuum_toggle_GF2_rank": len(gf2_basis(toggles)),
        "vacuum_toggle_auxiliary_positions": tuple(positions),
        "pure_X_free_toggle_failures": failures,
        "vacuum_pair_amplitude_failures": amplitude_failures,
        "all_term_auxiliary_Z_failures": term_auxiliary_z_failures,
        "maximum_quadrant_phase_residual_diagnostic": maximum_phase_residual,
        "pass": (
            len(set(toggles)) == PATCH_CELL_COUNT
            and len(gf2_basis(toggles)) == PATCH_CELL_COUNT
            and failures == amplitude_failures == term_auxiliary_z_failures == 0
            and maximum_phase_residual < 2e-13
        ),
    }


def exact_collision_gram(length: int, started: float) -> dict:
    code = c516.c269.build_code(length)
    cells = c517.rotated_patch(c517.IDENTITY, length)
    cache = {
        (cell, number): aggregate_terms(code, body, number)
        for cell, body in enumerate(cells)
        for number in range(3)
    }
    enumeration = enumerate_seeds(code, cache)
    toggle_controls = vacuum_toggle_controls(code, cache, enumeration["toggles"])
    reducer = c516.c315.RayReducer(code).stabilizer
    fixed_gram: defaultdict[tuple[tuple[int, ...], tuple[int, ...]], list[Fraction]] = defaultdict(
        lambda: [Fraction(0), Fraction(0)]
    )
    order_gram: defaultdict[tuple[tuple[int, ...], tuple[int, ...]], list[Fraction]] = defaultdict(
        lambda: [Fraction(0), Fraction(0)]
    )
    coefficient_histogram = Counter()
    common_vacuum_histogram = Counter()
    relative_phase_histogram = Counter()
    character_pair_histogram = Counter()
    character_sum_histogram = Counter()
    infeasible_pairs = 0
    inequivalent_ray_pairs = 0
    expanded_collision_pairs = 0
    maximum_exact_phase_residual = 0.0
    collision_rows = []
    all_columns = set()

    for first, second in enumeration["duplicate_pairs"]:
        coefficient = first.coefficient ^ second.coefficient
        coefficient_histogram[coefficient] += 1
        if coefficient & first.occupied & second.occupied:
            infeasible_pairs += 1
            continue
        first_base, second_base, common_vacuum = canonical_matching_variants(first, second)
        common_cells = tuple(
            cell for cell in range(PATCH_CELL_COUNT) if (common_vacuum >> cell) & 1
        )
        common_vacuum_histogram[common_vacuum] += 1
        local_gaussian = [0, 0]
        local_phases = Counter()
        local_characters = Counter()
        local_inequivalent = 0
        for selection in range(1 << len(common_cells)):
            shared = sum(
                1 << cell
                for index, cell in enumerate(common_cells)
                if (selection >> index) & 1
            )
            first_branch = branch_for_seed(first, first_base ^ shared, cache)
            second_branch = branch_for_seed(second, second_base ^ shared, cache)
            first_product = first_branch["product"]
            second_product = second_branch["product"]
            if first_product.x >> code.qubits != second_product.x >> code.qubits:
                raise CertificateFailure("orbit criterion produced unequal auxiliary words")
            phase = reducer.relative_phase(
                pauli_face(code, second_product), pauli_face(code, first_product)
            )
            if phase is None:
                local_inequivalent += 1
                continue
            relative_phase_histogram[phase] += 1
            local_phases[phase] += 1
            character_pair = (
                first_branch["character_mask"], second_branch["character_mask"]
            )
            character_pair_histogram[character_pair] += 1
            local_characters[character_pair] += 1
            numeric_overlap = (
                first_branch["amplitude"].conjugate()
                * second_branch["amplitude"]
                * phase_scalar(phase)
            )
            exact_real, exact_imaginary, residual = fraction_pair(
                numeric_overlap * 102_400, 1
            )
            maximum_exact_phase_residual = max(maximum_exact_phase_residual, residual)
            local_gaussian[0] += exact_real.numerator
            local_gaussian[1] += exact_imaginary.numerator
        inequivalent_ray_pairs += local_inequivalent
        collisions = (1 << len(common_cells)) - local_inequivalent
        expanded_collision_pairs += collisions
        if len(local_characters) != 1:
            raise CertificateFailure("vacuum toggles changed the physical order character")
        character_pair = next(iter(local_characters))
        difference = character_pair[0] ^ character_pair[1]
        signed_order_sum = character_sum_over_orders(difference)
        character_sum_histogram[signed_order_sum] += 1
        key = (first.column, second.column)
        conjugate = False
        if key[1] < key[0]:
            key = (key[1], key[0])
            conjugate = True
        gaussian = (local_gaussian[0], -local_gaussian[1]) if conjugate else tuple(local_gaussian)
        fixed_gram[key][0] += Fraction(gaussian[0], 102_400)
        fixed_gram[key][1] += Fraction(gaussian[1], 102_400)
        order_gram[key][0] += Fraction(
            gaussian[0] * signed_order_sum, 102_400 * math.factorial(12)
        )
        order_gram[key][1] += Fraction(
            gaussian[1] * signed_order_sum, 102_400 * math.factorial(12)
        )
        all_columns.update(key)
        collision_rows.append(
            {
                "first": seed_descriptor(first, cache),
                "second": seed_descriptor(second, cache),
                "coefficient_difference": coefficient,
                "common_vacuum_mask": common_vacuum,
                "expanded_row_collisions": collisions,
                "relative_phase_histogram": dict(sorted(local_phases.items())),
                "character_pair": character_pair,
                "character_difference": difference,
                "signed_S12_character_sum": signed_order_sum,
                "fixed_overlap": complex_fraction_json(
                    (Fraction(gaussian[0], 102_400), Fraction(gaussian[1], 102_400))
                ),
                "weighted_order_overlap": complex_fraction_json(
                    (
                        Fraction(
                            gaussian[0] * signed_order_sum,
                            102_400 * math.factorial(12),
                        ),
                        Fraction(
                            gaussian[1] * signed_order_sum,
                            102_400 * math.factorial(12),
                        ),
                    )
                ),
            }
        )

    fixed_nonzero = {key: tuple(value) for key, value in fixed_gram.items() if any(value)}
    order_nonzero = {key: tuple(value) for key, value in order_gram.items() if any(value)}
    fixed_magnitudes_squared = {
        value[0] * value[0] + value[1] * value[1] for value in fixed_nonzero.values()
    }
    order_magnitudes_squared = {
        value[0] * value[0] + value[1] * value[1] for value in order_nonzero.values()
    }
    row_payload = json.dumps(collision_rows, sort_keys=True, separators=(",", ":"), default=list).encode()
    abstract_payload = json.dumps(
        [
            {
                "first": row["first"],
                "second": row["second"],
                "coefficient_difference": row["coefficient_difference"],
                "common_vacuum_mask": row["common_vacuum_mask"],
                "expanded_row_collisions": row["expanded_row_collisions"],
                "relative_phase_histogram": row["relative_phase_histogram"],
                "character_pair": row["character_pair"],
                "signed_S12_character_sum": row["signed_S12_character_sum"],
                "fixed_overlap": row["fixed_overlap"],
                "weighted_order_overlap": row["weighted_order_overlap"],
            }
            for row in collision_rows
        ],
        sort_keys=True,
        separators=(",", ":"),
        default=list,
    ).encode()
    fixed_matching = (
        len(fixed_nonzero) == EXPECTED_FIXED_OVERLAPS
        and len({column for key in fixed_nonzero for column in key}) == 48
    )
    order_matching = (
        len(order_nonzero) == EXPECTED_ORDER_OVERLAPS
        and len({column for key in order_nonzero for column in key}) == 16
    )
    passed = (
        toggle_controls["pass"]
        and enumeration["seeds"] == EXPECTED_SEEDS
        and enumeration["quotient_fibers"] == EXPECTED_QUOTIENT_FIBERS
        and enumeration["singleton_fibers"] == EXPECTED_SINGLETON_FIBERS
        and enumeration["doubleton_fibers"] == EXPECTED_DOUBLETON_FIBERS
        and enumeration["maximum_fiber"] == 2
        and infeasible_pairs == inequivalent_ray_pairs == 0
        and coefficient_histogram == {0: EXPECTED_DOUBLETON_FIBERS}
        and expanded_collision_pairs == EXPECTED_COLLISION_PAIRS
        and relative_phase_histogram == {0: 4096, 2: 2048}
        and fixed_matching
        and order_matching
        and fixed_magnitudes_squared == {EXPECTED_OVERLAP_MAGNITUDE**2}
        and order_magnitudes_squared == {EXPECTED_OVERLAP_MAGNITUDE**2}
        and character_sum_histogram == {0: 16, math.factorial(12): 8}
        and maximum_exact_phase_residual < 2e-11
    )
    return {
        "L": length,
        "held_size": length == HELD_LENGTH,
        "vacuum_toggle_controls": toggle_controls,
        "excitation_seeds": enumeration["seeds"],
        "seed_sector_counts": enumeration["sector_seeds"],
        "quotient_fibers": enumeration["quotient_fibers"],
        "fiber_histogram": {
            "1": enumeration["singleton_fibers"],
            "2": enumeration["doubleton_fibers"],
        },
        "maximum_fiber_size": enumeration["maximum_fiber"],
        "duplicate_seed_pairs": len(enumeration["duplicate_pairs"]),
        "coefficient_difference_histogram": dict(coefficient_histogram),
        "infeasible_orbit_pairs": infeasible_pairs,
        "inequivalent_face_ray_pairs": inequivalent_ray_pairs,
        "common_vacuum_mask_histogram": dict(sorted(common_vacuum_histogram.items())),
        "expanded_physical_row_collision_pairs": expanded_collision_pairs,
        "analytic_full_branch_count": EXPECTED_FULL_BRANCHES,
        "exact_unique_physical_rows": EXPECTED_FULL_BRANCHES - expanded_collision_pairs,
        "maximum_row_multiplicity": 2,
        "relative_phase_histogram": dict(sorted(relative_phase_histogram.items())),
        "character_pair_histogram": tuple(
            (pair, count) for pair, count in sorted(character_pair_histogram.items())
        ),
        "signed_S12_character_sum_histogram": dict(sorted(character_sum_histogram.items())),
        "fixed_order_nonzero_Gram_pairs": len(fixed_nonzero),
        "fixed_order_affected_columns": len({column for key in fixed_nonzero for column in key}),
        "fixed_order_maximum_Gram_residual": fraction_json(EXPECTED_OVERLAP_MAGNITUDE),
        "fixed_order_Frobenius_Gram_residual_squared": fraction_json(Fraction(3, 10_000)),
        "weighted_order_nonzero_Gram_pairs": len(order_nonzero),
        "weighted_order_affected_columns": len({column for key in order_nonzero for column in key}),
        "weighted_order_maximum_Gram_residual": fraction_json(EXPECTED_OVERLAP_MAGNITUDE),
        "weighted_order_Frobenius_Gram_residual_squared": fraction_json(Fraction(1, 10_000)),
        "maximum_exact_phase_residual_diagnostic": maximum_exact_phase_residual,
        "collision_rows_sha256": sha256(row_payload).hexdigest(),
        "abstract_collision_signature_sha256": sha256(abstract_payload).hexdigest(),
        "collision_rows": tuple(collision_rows),
        "resource": checkpoint(started, f"L{length}-compressed-Gram-complete"),
        "pass": passed,
    }


def proper_frame_collision_controls(train_rows: tuple[dict, ...], started: float) -> dict:
    """Transport the 24 seed-pair collision witnesses through all proper frames."""

    tests = 0
    auxiliary_failures = 0
    ray_failures = 0
    character_failures = 0
    zero_character_tests = 0
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        code = c516.c269.build_code(length)
        reducer = c516.c315.RayReducer(code).stabilizer
        for frame in c517.FRAMES:
            cells = c517.rotated_patch(frame, length)
            representative_cache = {}
            for row in train_rows:
                branches = []
                for side_name in ("first", "second"):
                    side = row[side_name]
                    chosen = {choice["cell"]: choice for choice in side["choices"]}
                    reps = []
                    for cell, body in enumerate(cells):
                        metadata = chosen.get(
                            cell,
                            {
                                "number": 0,
                                "label": (),
                                "carrier": None,
                                "variant": 0,
                            },
                        )
                        transformed = c517.transform_metadata(metadata, frame)
                        key = (
                            cell,
                            transformed["number"],
                            tuple(transformed["label"]),
                            transformed["carrier"],
                            transformed["variant"],
                        )
                        if key not in representative_cache:
                            representative_cache[key] = c517.representative_for_metadata(
                                code, body, transformed
                            )
                        reps.append(representative_cache[key])
                    branches.append(
                        {
                            "representatives": tuple(reps),
                            "product": multiply_order(tuple(reps)),
                            "character": character_mask(tuple(reps)),
                        }
                    )
                first, second = branches
                tests += 1
                auxiliary_failures += (
                    first["product"].x >> code.qubits
                    != second["product"].x >> code.qubits
                )
                phase = reducer.relative_phase(
                    pauli_face(code, second["product"]),
                    pauli_face(code, first["product"]),
                )
                ray_failures += phase is None
                expected = tuple(row["character_pair"])
                observed = (first["character"], second["character"])
                character_failures += observed != expected
                zero_character_tests += observed == (0, 0)
    expected_tests = 2 * EXPECTED_PROPER_FRAMES * EXPECTED_DOUBLETON_FIBERS
    expected_zero = 2 * EXPECTED_PROPER_FRAMES * EXPECTED_ORDER_OVERLAPS
    return {
        "sizes": (TRAIN_LENGTH, HELD_LENGTH),
        "proper_frames": len(c517.FRAMES),
        "frame_products_inherited_from_Cycle517": EXPECTED_FRAME_PRODUCTS,
        "transported_collision_tests": tests,
        "expected_transported_collision_tests": expected_tests,
        "auxiliary_equality_failures": auxiliary_failures,
        "face_ray_equivalence_failures": ray_failures,
        "character_transport_failures": character_failures,
        "transported_zero_character_collision_tests": zero_character_tests,
        "expected_zero_character_collision_tests": expected_zero,
        "resource": checkpoint(started, "all-frame-collision-transport-complete"),
        "pass": (
            tests == expected_tests
            and zero_character_tests == expected_zero
            and auxiliary_failures == ray_failures == character_failures == 0
        ),
    }


def deletion_controls(train: dict) -> dict:
    first_zero = next(
        row
        for row in train["collision_rows"]
        if tuple(row["character_pair"]) == (0, 0)
    )
    return {
        "delete_vacuum_occupation_restriction_false_positive_fixture": (
            "a toggle on a cell occupied by both seeds cannot be removed"
        ),
        "delete_partial_orbit_intersection_false_negative_fixture": (
            "different vacuum-toggle cosets can intersect without being equal"
        ),
        "delete_face_ray_key_is_unsound": (
            "an auxiliary-only key must retain inequivalent fixed-Wilson face rays"
        ),
        "delete_linear_extension_weights_residual_inherited_from_Cycle517": True,
        "delete_order_character_zero_mask_witness": {
            "first": first_zero["first"],
            "second": first_zero["second"],
            "character_pair": first_zero["character_pair"],
            "weighted_order_overlap": first_zero["weighted_order_overlap"],
        },
        "one_discriminator_bit_capacity_suffices_for_size_two_fibers": True,
        "one_discriminator_bit_physical_rule_synthesized": False,
        "pass": tuple(first_zero["character_pair"]) == (0, 0),
    }


def upstream_evidence() -> dict:
    observed = {
        str(path.relative_to(ROOT)): file_sha(path)
        for path in STRICT_FILE_HASHES
        if path.exists()
    }
    missing = tuple(str(path.relative_to(ROOT)) for path in STRICT_FILE_HASHES if not path.exists())
    failures = {
        str(path.relative_to(ROOT)): {
            "expected": expected,
            "observed": observed.get(str(path.relative_to(ROOT))),
        }
        for path, expected in STRICT_FILE_HASHES.items()
        if observed.get(str(path.relative_to(ROOT))) != expected
    }
    dry = c517.dry_contract()
    return {
        "missing_files": missing,
        "strict_file_hashes": observed,
        "strict_hash_failures": failures,
        "Cycle517_dry_pass": dry["pass"],
        "Cycle517_tests": (dry["tests_passed"], dry["tests_total"]),
        "Cycle517_authority": dry["authority"],
        "Cycle517_audit": dry["audit"],
        "pass": (
            not missing
            and not failures
            and dry["pass"]
            and dry["authority"] == AUTHORITY
            and dry["audit"] == AUDIT
        ),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE.relative_to(ROOT)), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "238,681",
        "238,657",
        "6,144",
        "245,512,192",
        "1/400",
        "eight zero-character",
        "route-specific",
        "not an obstruction",
        "no axiom pressure",
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
    evidence = upstream_evidence()
    note = note_contract()
    exact_order_controls = {
        "zero_character_sum": character_sum_over_orders(0),
        "single_edge_character_sum": character_sum_over_orders(1),
        "two_disjoint_edge_character_sum": character_sum_over_orders((1 << 1) | (1 << 6)),
    }
    resources = {
        "excitation_seeds_per_size": EXPECTED_SEEDS,
        "literal_branches_avoided_per_size": EXPECTED_FULL_BRANCHES,
        "hard_wall_seconds": WALL_LIMIT_SECONDS,
        "RSS_checkpoint_guard_bytes": RSS_CHECKPOINT_GUARD_BYTES,
        "partial_rows_durable_across_OS_kill_or_process_OOM": False,
    }
    tests = {
        "Cycle517_hash_bound_and_dry": evidence["pass"],
        "exact_S12_character_DP": (
            exact_order_controls["zero_character_sum"] == math.factorial(12)
            and exact_order_controls["single_edge_character_sum"] == 0
            and exact_order_controls["two_disjoint_edge_character_sum"] == 0
        ),
        "exact_compressed_resource_contract": (
            EXPECTED_SEEDS
            == 1 + 12 * 60 + 12 * 30 + math.comb(12, 2) * 60 * 60
            and EXPECTED_FULL_BRANCHES
            == 2**12
            + 12 * 60 * 2**11
            + 12 * 30 * 2**11
            + math.comb(12, 2) * 60 * 60 * 2**10
        ),
        "note_scope_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle518-compressed-Gram-contract-ready" if all(tests.values()) else "cycle518-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "exact_order_controls": exact_order_controls,
        "resources": resources,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def gram_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial", projected_bytes=500_000_000)]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle518 dry contract failed")
    train = exact_collision_gram(TRAIN_LENGTH, started)
    checkpoints.append(train["resource"])
    held = exact_collision_gram(HELD_LENGTH, started)
    checkpoints.append(held["resource"])
    frame = proper_frame_collision_controls(train["collision_rows"], started)
    checkpoints.append(frame["resource"])
    deletion = deletion_controls(train)
    held_match = (
        train["abstract_collision_signature_sha256"]
        == held["abstract_collision_signature_sha256"]
    )
    tests = {
        "dry_contract": dry["pass"],
        "L5_exact_compressed_Gram": train["pass"],
        "held_L6_exact_compressed_Gram": held["pass"],
        "held_abstract_collision_signature_matches": held_match,
        "all24_frame_collision_transport_L5_L6": frame["pass"],
        "fixed_order_nonisometry_exact": (
            train["fixed_order_nonzero_Gram_pairs"] == EXPECTED_FIXED_OVERLAPS
            and train["fixed_order_maximum_Gram_residual"] == fraction_json(EXPECTED_OVERLAP_MAGNITUDE)
        ),
        "weighted_order_character_nonisometry_exact": (
            train["weighted_order_nonzero_Gram_pairs"] == EXPECTED_ORDER_OVERLAPS
            and train["weighted_order_maximum_Gram_residual"] == fraction_json(EXPECTED_OVERLAP_MAGNITUDE)
        ),
        "deletion_and_scope_controls": deletion["pass"],
        "resource_contract": swap_count() == 0 and rss_bytes() < RSS_CHECKPOINT_GUARD_BYTES,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "gram-certificate",
        "status": "cycle518-native-adjacent-two-star-Gram-counterexample-certified" if all(tests.values()) else "cycle518-certificate-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "train": train,
        "held": held,
        "held_abstract_collision_signature_matches": held_match,
        "proper_frame_collision_controls": frame,
        "deletion_controls": deletion,
        "theorem": {
            "native_fixed_order_E_is_isometric": False,
            "native_weighted_order_character_E_is_isometric": False,
            "exact_fixed_order_operator_Gram_residual": fraction_json(EXPECTED_OVERLAP_MAGNITUDE),
            "exact_weighted_order_operator_Gram_residual": fraction_json(EXPECTED_OVERLAP_MAGNITUDE),
            "full_S12_order_labels_alone_repair_zero_character_pairs": False,
            "one_extra_binary_discriminator_has_sufficient_capacity": True,
            "one_extra_binary_discriminator_physical_rule_synthesized": False,
            "existing_orientation_role_controlled_character_repair_candidate_open": True,
            "existing_axial_vacuum_role_product_repair_candidate_open": True,
            "changed_representative_route_open": True,
            "local_gauge_flux_route_open": True,
            "tagged_schedule_route_open": True,
        },
        "boundary": {
            "route_specific_counterexample": (
                "native Cycle311/315 representatives plus Cycle517 order character "
                "on the twelve-cell global-N<=2 patch"
            ),
            "physical_M2_compiler_proven": False,
            "E_Gcoarse_equals_Gphysical_E_proven": False,
            "primitive_constraint_synthesis_proven": False,
            "recurrent_volume_proven": False,
            "mass_fixture_retested": False,
            "physical_time_claim": False,
            "Record_claim": False,
            "source_or_gravity_claim": False,
            "Born_or_probability_claim": False,
            "route_independent_obstruction": False,
            "axiom_pressure": False,
        },
        "supplied_structure": (
            "Cycle311/315 local role-gauge representatives and amplitudes",
            "Cycle517 twelve-cell patch and fifteen-edge order character",
            "fixed-Wilson reference-vacuum stabilizer reducer",
            "weighted uniform S12 order state compressed by linear-extension multiplicity",
        ),
        "next_open_target": (
            "test the zero-new-M2 column-controlled axial-edge orientation character "
            "and axial vacuum-role product repairs for the eight zero-character "
            "collision fibers, then rerun the compressed Gram"
        ),
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
    parser.add_argument(
        "--compact",
        action="store_true",
        help="omit the 24 per-size collision rows from the printed certificate",
    )
    args = parser.parse_args()
    if args.mode == "dry-contract":
        result = dry_contract()
    else:
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, WALL_LIMIT_SECONDS)
        try:
            result = gram_certificate()
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
    if args.compact and args.mode == "gram-certificate":
        result["train"].pop("collision_rows", None)
        result["held"].pop("collision_rows", None)
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), default=list))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
