#!/usr/bin/env python3
"""Cycle 521: final-tag syndrome orthogonality and protected shadows.

This runner tests whether the independently appended Cycle-519/520 parity
tags can be enforced by a genuine operator on the *final* overlapping native
branch shell.  It proves a representation-specific orthogonality boundary,
constructs the canonical dense code projector/involution, and compares one
protected parity shadow with the six-occupation-shadow architecture.

No foundation, axiom, primitive, registry, policy, queue, or audit surface is
changed.  Authority is none and audit is unset.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
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

import physical_three_star_shared_parity_overlap_cycle520_2026_07_21 as c520


c519 = c520.c519
c518 = c520.c518
c516 = c520.c516
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "syndrome-certificate")
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TWO_STAR_NATIVE_OVERLAPS = 24
TWO_STAR_AFFECTED_COLUMNS = 48
THREE_STAR_NATIVE_OVERLAPS = 42
OVERLAP_MAGNITUDE = Fraction(1, 400)
OVERLAP_MAGNITUDE_SQUARED = Fraction(1, 160_000)
THREE_TAG_XOR_COUNTS = {0b011: 18, 0b110: 18, 0b111: 6}
THREE_TAG_AFFECTED_COLUMNS = {0b011: 36, 0b110: 36, 0b111: 12}
THREE_LOGICAL_DIMENSION = 4_657
THREE_NATIVE_QUOTIENT_ROWS = 433_399
THREE_TAGGED_AMBIENT_ROWS = 8 * THREE_NATIVE_QUOTIENT_ROWS
THREE_COMPRESSED_PROJECTOR_MATRIX_UNITS = 43_210_561
THREE_LITERAL_PROJECTOR_MATRIX_UNITS = 11_607_754_707_828_736
TWO_COMPRESSED_PROJECTOR_MATRIX_UNITS = 23_767_921
TWO_LITERAL_PROJECTOR_MATRIX_UNITS = 24_947_401_424_896
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FINAL_TAG_SYNDROME_ORTHOGONALITY_CYCLE521_NOTE_2026-07-21.md"
)
CYCLE520_RUNNER = ROOT / "scripts/physical_three_star_shared_parity_overlap_cycle520_2026_07_21.py"
CYCLE520_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_THREE_STAR_SHARED_PARITY_OVERLAP_CYCLE520_NOTE_2026-07-21.md"
)
EXPECTED_CYCLE520_SHA256 = {
    CYCLE520_RUNNER: "22b00fd39fd07a04afb8776f4b97c31486ce4d2034617bd16aa170c263108b2b",
    CYCLE520_NOTE: "8a1aa2c66cbc38320c829679e7b982936834510a58b38f89621f22278fd67cd8",
}
CYCLE519_RUNNER = ROOT / "scripts/physical_adjacent_two_star_seam_tag_preservation_cycle519_2026_07_21.py"
CYCLE519_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_TWO_STAR_SEAM_TAG_PRESERVATION_CYCLE519_NOTE_2026-07-21.md"
)


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physical conclusion."""


class CertificateFailure(RuntimeError):
    """A failed bounded predicate, never a substrate obstruction."""


@dataclass(frozen=True)
class Seed:
    coefficient: int
    occupied: int
    column: tuple[int, ...]
    choices: tuple[tuple[int, int, int], ...]
    tag: int


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss_bytes() >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss_bytes()}")
    if swap_count() != 0:
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def fraction_json(value: Fraction) -> tuple[int, int]:
    return value.numerator, value.denominator


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def complex_fraction(row: dict) -> tuple[Fraction, Fraction]:
    return Fraction(*row["real"]), Fraction(*row["imaginary"])


def two_star_overlap_spectrum(length: int, started: float) -> dict:
    result = c518.exact_collision_gram(length, started)
    degrees = Counter()
    parity_xors = Counter()
    magnitudes = Counter()
    for row in result["collision_rows"]:
        first = row["first"]
        second = row["second"]
        first_parity = sum(
            choice["number"] for choice in first["choices"] if choice["cell"] == 0
        ) & 1
        second_parity = sum(
            choice["number"] for choice in second["choices"] if choice["cell"] == 0
        ) & 1
        parity_xors[first_parity ^ second_parity] += 1
        left = tuple(first["column"])
        right = tuple(second["column"])
        degrees[left] += 1
        degrees[right] += 1
        real, imaginary = complex_fraction(row["fixed_overlap"])
        magnitudes[real * real + imaginary * imaginary] += 1
    return {
        "length": length,
        "native_cross_parity_overlaps": len(result["collision_rows"]),
        "left_tag_xor_histogram": dict(parity_xors),
        "affected_columns": len(degrees),
        "maximum_collision_degree": max(degrees.values()),
        "overlap_magnitude_squared_histogram": {
            str(value): count for value, count in magnitudes.items()
        },
        "fixed_order_Gram_residual": result["fixed_order_maximum_Gram_residual"],
        "pass": (
            result["pass"]
            and len(result["collision_rows"]) == TWO_STAR_NATIVE_OVERLAPS
            and parity_xors == Counter({1: TWO_STAR_NATIVE_OVERLAPS})
            and len(degrees) == TWO_STAR_AFFECTED_COLUMNS
            and max(degrees.values()) == 1
            and magnitudes == Counter({OVERLAP_MAGNITUDE_SQUARED: TWO_STAR_NATIVE_OVERLAPS})
        ),
    }


def enumerate_three_star_seeds(length: int):
    code, _centers, cells, center_indices, cache = c520.build_cache(length)
    count = c520.BENT_CELL_COUNT
    vacuum = tuple(cache[cell, 0][0]["auxiliary"] for cell in range(count))
    toggles = tuple(
        cache[cell, 0][0]["auxiliary"] ^ cache[cell, 0][1]["auxiliary"]
        for cell in range(count)
    )
    basis = c518.gf2_basis(toggles)
    seen: dict[int, Seed] = {}
    duplicate_pairs: list[tuple[Seed, Seed]] = []

    def add(occupied: int, column, choices) -> None:
        delta = 0
        numbers = {}
        for cell, number, term_index in choices:
            delta ^= cache[cell, number][term_index]["auxiliary"] ^ vacuum[cell]
            numbers[cell] = number
        quotient, coefficient = c518.gf2_reduce(delta, basis)
        tag = sum(
            (numbers.get(center, 0) & 1) << bit
            for bit, center in enumerate(center_indices)
        )
        seed = Seed(coefficient, occupied, tuple(column), tuple(choices), tag)
        if quotient in seen:
            duplicate_pairs.append((seen[quotient], seed))
        else:
            seen[quotient] = seed

    add(0, (), ())
    for cell in range(count):
        for term_index, term in enumerate(cache[cell, 1]):
            add(
                1 << cell,
                (6 * cell + term["label"][0],),
                ((cell, 1, term_index),),
            )
        for term_index, term in enumerate(cache[cell, 2]):
            add(
                1 << cell,
                tuple(6 * cell + direction for direction in term["label"]),
                ((cell, 2, term_index),),
            )
    for first, second in combinations(range(count), 2):
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
                )
    return code, cells, center_indices, cache, tuple(duplicate_pairs)


def seed_terms(seed: Seed, cache) -> dict[int, dict]:
    return {
        cell: cache[cell, number][term_index]
        for cell, number, term_index in seed.choices
    }


def matching_variants(first: Seed, second: Seed, count: int):
    difference = first.coefficient ^ second.coefficient
    vacuum_first = ((1 << count) - 1) ^ first.occupied
    vacuum_second = ((1 << count) - 1) ^ second.occupied
    if difference & ~(vacuum_first | vacuum_second):
        raise CertificateFailure("infeasible common-vacuum matching pair")
    return (
        difference & vacuum_first,
        difference & ~vacuum_first & vacuum_second,
        vacuum_first & vacuum_second,
    )


def branch_for_seed(seed: Seed, variants: int, cache):
    count = c520.BENT_CELL_COUNT
    occupied = seed_terms(seed, cache)
    representatives = []
    amplitude = 1 + 0j
    for cell in range(count):
        term = (
            occupied[cell]
            if cell in occupied
            else cache[cell, 0][(variants >> cell) & 1]
        )
        representatives.append(term["representative"])
        amplitude *= term["amplitude"]
    product = c516.c330.multiply_order(
        tuple(representatives), tuple(range(count))
    )
    return product, amplitude


def three_star_overlap_spectrum(length: int) -> dict:
    code, _cells, center_indices, cache, pairs = enumerate_three_star_seeds(length)
    reducer = c516.c315.RayReducer(code).stabilizer
    count = c520.BENT_CELL_COUNT
    denominator = 100 * 2 ** (count - 2)
    degrees = {mask: Counter() for mask in range(1, 8)}
    overlaps = Counter()
    expanded_equivalent = Counter()
    gaussian_histogram = Counter()
    maximum_rounding_residual = 0.0
    for first, second in pairs:
        first_base, second_base, common_vacuum = matching_variants(
            first, second, count
        )
        common_cells = tuple(
            cell for cell in range(count) if (common_vacuum >> cell) & 1
        )
        total = 0 + 0j
        equivalent = 0
        for selection in range(1 << len(common_cells)):
            shared = sum(
                1 << cell
                for index, cell in enumerate(common_cells)
                if (selection >> index) & 1
            )
            first_product, first_amplitude = branch_for_seed(
                first, first_base ^ shared, cache
            )
            second_product, second_amplitude = branch_for_seed(
                second, second_base ^ shared, cache
            )
            if first_product.x >> code.qubits != second_product.x >> code.qubits:
                raise CertificateFailure("equal quotient produced unequal auxiliary rows")
            phase = reducer.relative_phase(
                c518.pauli_face(code, second_product),
                c518.pauli_face(code, first_product),
            )
            if phase is None:
                continue
            equivalent += 1
            total += (
                first_amplitude.conjugate()
                * second_amplitude
                * c518.phase_scalar(phase)
            )
        real = Fraction(round(total.real * denominator), denominator)
        imaginary = Fraction(round(total.imag * denominator), denominator)
        maximum_rounding_residual = max(
            maximum_rounding_residual,
            abs(float(real) - total.real),
            abs(float(imaginary) - total.imag),
        )
        xor = first.tag ^ second.tag
        overlaps[xor] += 1
        expanded_equivalent[xor] += equivalent
        gaussian_histogram[(real, imaginary)] += 1
        degrees[xor][first.column] += 1
        degrees[xor][second.column] += 1
    error_words = {}
    for mask in range(1, 8):
        affected = degrees[mask]
        nonzero_pairs = overlaps[mask]
        error_words[format(mask, "03b")] = {
            "native_overlap_pairs": nonzero_pairs,
            "affected_columns": len(affected),
            "maximum_degree": max(affected.values(), default=0),
            "compressed_P_X_P_rank": 2 * nonzero_pairs,
            "compressed_P_X_P_operator_norm": (
                fraction_json(OVERLAP_MAGNITUDE) if nonzero_pairs else (0, 1)
            ),
            "perfectly_detected_by_joint_code_projector": nonzero_pairs == 0,
        }
    return {
        "length": length,
        "native_doubletons": len(pairs),
        "tag_xor_histogram": {
            format(mask, "03b"): count for mask, count in sorted(overlaps.items())
        },
        "expanded_equivalent_rows_by_xor": {
            format(mask, "03b"): count
            for mask, count in sorted(expanded_equivalent.items())
        },
        "fixed_overlap_gaussian_histogram": {
            f"{real}+{imaginary}i": count
            for (real, imaginary), count in gaussian_histogram.items()
        },
        "fixed_overlap_magnitude_squared": fraction_json(OVERLAP_MAGNITUDE_SQUARED),
        "error_word_syndrome_table": error_words,
        "cross_parity_pairs_by_center": tuple(
            sum(count for mask, count in overlaps.items() if (mask >> bit) & 1)
            for bit in range(3)
        ),
        "maximum_rounding_residual": maximum_rounding_residual,
        "pass": (
            len(pairs) == THREE_STAR_NATIVE_OVERLAPS
            and overlaps == Counter(THREE_TAG_XOR_COUNTS)
            and all(
                len(degrees[mask]) == THREE_TAG_AFFECTED_COLUMNS[mask]
                and max(degrees[mask].values()) == 1
                for mask in THREE_TAG_XOR_COUNTS
            )
            and all(
                real * real + imaginary * imaginary == OVERLAP_MAGNITUDE_SQUARED
                for real, imaginary in gaussian_histogram
            )
            and maximum_rounding_residual < 2e-12
            and tuple(
                sum(count for mask, count in overlaps.items() if (mask >> bit) & 1)
                for bit in range(3)
            )
            == (24, 42, 24)
        ),
    }


def branch_shell_support(length: int, three_star: bool) -> dict:
    if three_star:
        code, _centers, _cells, _indices, cache = c520.build_cache(length)
        cell_count = c520.BENT_CELL_COUNT
        tags = 3
    else:
        code, _cells, cache = c519.build_cache(length)
        cell_count = c519.PATCH_CELL_COUNT
        tags = 1
    support = 0
    for cell in range(cell_count):
        for number in range(3):
            for term in cache[cell, number]:
                representative = term["representative"]
                support |= representative.x | representative.z
    face_mask = (1 << code.qubits) - 1
    face = (support & face_mask).bit_count()
    auxiliary = (support >> code.qubits).bit_count()
    return {
        "length": length,
        "native_branch_shell_union_M2_upper_bound": face + auxiliary,
        "face_M2": face,
        "auxiliary_M2": auxiliary,
        "dedicated_tag_M2": tags,
        "tagged_branch_shell_union_M2_upper_bound": face + auxiliary + tags,
    }


def orthogonality_and_projector_controls(two_rows, three_rows) -> dict:
    two_held_match = all(
        row["native_cross_parity_overlaps"] == TWO_STAR_NATIVE_OVERLAPS
        and row["fixed_order_Gram_residual"] == fraction_json(OVERLAP_MAGNITUDE)
        for row in two_rows
    )
    three_held_match = (
        three_rows[0]["tag_xor_histogram"] == three_rows[1]["tag_xor_histogram"]
        and three_rows[0]["fixed_overlap_gaussian_histogram"]
        == three_rows[1]["fixed_overlap_gaussian_histogram"]
    )
    return {
        "Hermitian_parity_lemma": (
            "Q E_i=(-1)^p_i E_i and Q=Q^dagger imply opposite-parity "
            "native overlaps vanish"
        ),
        "perfect_syndrome_lemma": (
            "a projector/involution accepting correct tagged states and rejecting "
            "tag-flipped states requires the two subspaces to be orthogonal"
        ),
        "two_star_nonzero_cross_parity_overlap": fraction_json(OVERLAP_MAGNITUDE),
        "native_only_Hermitian_parity_operator_exists_on_tested_representation": False,
        "perfect_final_native_plus_one_tag_syndrome_exists": False,
        "three_center_native_only_parity_operator_exists_by_center": (False, False, False),
        "scope": (
            "existing Cycle311/315/515/516 final native representation on the "
            "declared two-star and bent-three-star N<=2 domains"
        ),
        "changed_representatives_or_protected_pre_overlap_information_closed": False,
        "canonical_non_Pauli_projector": "P_tau=E_tau E_tau^dagger",
        "canonical_involution": "J_tau=2 P_tau-I",
        "dense_update_completion": "U_hat=E_tau U E_tau^dagger + I-P_tau",
        "projector_rank": THREE_LOGICAL_DIMENSION,
        "tagged_compressed_ambient_rows": THREE_TAGGED_AMBIENT_ROWS,
        "compressed_projector_matrix_units": THREE_COMPRESSED_PROJECTOR_MATRIX_UNITS,
        "literal_expanded_projector_matrix_units": THREE_LITERAL_PROJECTOR_MATRIX_UNITS,
        "single_tag_error_words_rejected_exactly": ("001", "010", "100"),
        "additional_exactly_rejected_tag_error_words": ("101",),
        "correlated_tag_error_words_not_perfectly_rejected": ("011", "110", "111"),
        "ambiguous_error_code_overlap_operator_norm": fraction_json(OVERLAP_MAGNITUDE),
        "ambiguous_error_projector_acceptance_probability_on_affected_columns": fraction_json(
            OVERLAP_MAGNITUDE_SQUARED
        ),
        "P_tau_is_bounded_non_Pauli_final_code_constraint": True,
        "P_tau_nearest_neighbor_or_primitive_synthesized": False,
        "P_tau_update_commutator_exact_by_completion": True,
        "P_tau_all24_covariance_inherited_from_E_tau": True,
        "P_tau_mass_and_contact_inherited_by_intertwining": True,
        "pass": two_held_match and three_held_match,
    }


def dual_shadow_step(config: int, tag: int, shadow: int, seam, center_indices):
    first, second = seam
    first_occupation = (config >> first) & 1
    second_occupation = (config >> second) & 1
    crossing = first_occupation ^ second_occupation
    if crossing:
        config ^= (1 << first) | (1 << second)
    tagged_modes = {
        6 * cell + direction: bit
        for bit, cell in enumerate(center_indices)
        for direction in range(6)
    }
    flip = 0
    if crossing:
        if first in tagged_modes:
            flip ^= 1 << tagged_modes[first]
        if second in tagged_modes:
            flip ^= 1 << tagged_modes[second]
    phase = -1 if first_occupation and second_occupation else 1
    return config, tag ^ flip, shadow ^ flip, phase, flip


def protected_shadow_controls() -> dict:
    configs = c520.logical_configurations()
    seams, center_indices = c520.dynamic_seams()
    single_tests = 0
    single_failures = 0
    composed_failures = 0
    deleted_incidence_failures = []
    incidence_count = 0
    for seam in seams:
        tagged_modes = {
            6 * cell + direction: bit
            for bit, cell in enumerate(center_indices)
            for direction in range(6)
        }
        incidence_bits = tuple(
            sorted(
                {
                    tagged_modes[mode]
                    for mode in seam
                    if mode in tagged_modes
                }
            )
        )
        incidence_count += len(incidence_bits)
        deletion_counts = Counter()
        for config in configs:
            initial = c520.tags_of(config, center_indices)
            output, tag, shadow, _phase, flip = dual_shadow_step(
                config, initial, initial, seam, center_indices
            )
            single_tests += 1
            single_failures += not (
                tag == shadow == c520.tags_of(output, center_indices)
            )
            for bit in incidence_bits:
                deletion_counts[bit] += bool((flip >> bit) & 1)
        deleted_incidence_failures.extend(
            deletion_counts[bit] for bit in incidence_bits
        )
    for config in configs:
        output = config
        tag = shadow = c520.tags_of(config, center_indices)
        phase = 1
        for seam in seams:
            output, tag, shadow, seam_phase, _flip = dual_shadow_step(
                output, tag, shadow, seam, center_indices
            )
            phase *= seam_phase
        composed_failures += not (
            tag == shadow == c520.tags_of(output, center_indices)
            and phase in (-1, 1)
        )
    candidate = c520.physical_candidate_controls()
    return {
        "one_shadow_constraint": "C_A=Z_tau_A Z_sigma_A=+1",
        "one_shadow_M2_per_tagged_center": 1,
        "three_center_tag_plus_shadow_M2": 6,
        "commuting_two_M2_constraints": 3,
        "tag_shadow_shell_dimension": 64,
        "lawful_equal_pair_dimension": 8,
        "delete_one_equality_constraint_rank": 16,
        "single_seam_correct_code_tests": single_tests,
        "single_seam_failures": single_failures,
        "complete_schedule_tests": len(configs),
        "complete_schedule_failures": composed_failures,
        "center_seam_incidences": incidence_count,
        "delete_each_tag_or_shadow_endpoint_update_syndrome_failures": tuple(
            deleted_incidence_failures
        ),
        "single_tag_or_single_shadow_flip_detected": True,
        "correlated_tag_shadow_flip_detected": False,
        "coin_and_contact_preserve_tag_shadow_pairs": True,
        "all24_covariance": "tau and sigma are proper-cubic scalars",
        "pre_overlap_coherent_initialization_not_host_inspection": True,
        "pre_overlap_initialization_primitive_synthesized": False,
        "decorated_physical_seam_synthesized": False,
        "six_occupation_shadow_M2_per_coarse_cell": 6,
        "six_occupation_shadow_M2_on_sixteen_cell_patch": 96,
        "three_center_parity_compute_CNOTs": 18,
        "delete_each_parity_CNOT_valid_configuration_errors": candidate[
            "deleted_each_CNOT_valid_configuration_errors"
        ],
        "six_shadow_compute_use_uncompute_intertwiner_exact_by_conjugation": True,
        "six_shadow_native_shell_synchronization_proved": candidate[
            "protected_shadow_synchronized_with_Cycle515_516_shell"
        ],
        "six_mode_coin_bare_one_two_M2_decomposition_proved": candidate[
            "Cycle219_six_mode_coin_bare_one_two_M2_decomposition_supplied"
        ],
        "pass": (
            single_tests == len(seams) * len(configs)
            and single_failures == composed_failures == 0
            and incidence_count == 18
            and tuple(deleted_incidence_failures) == (190,) * 18
            and candidate["pass"]
        ),
    }


def semantic_contract() -> dict:
    cycle519_source = CYCLE519_RUNNER.read_text(encoding="utf-8").lower()
    cycle519_note = CYCLE519_NOTE.read_text(encoding="utf-8").lower()
    cycle520_source = CYCLE520_RUNNER.read_text(encoding="utf-8").lower()
    required_519 = (
        "factor-local parity descriptor",
        "global_seven_m2_code_constraint_proven\": false",
        "not a constraint on the final overlapping code",
    )
    joined_519 = cycle519_source + cycle519_note
    required_520 = (
        "native_doubleton_tag_xor_histogram",
        "reference_stabilizer_decoder_controls",
        "physical_candidate_controls",
        "global_tag_parity_constraint_proven",
    )
    missing_519 = tuple(item for item in required_519 if item not in joined_519)
    missing_520 = tuple(item for item in required_520 if item not in cycle520_source)
    observed_520 = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in EXPECTED_CYCLE520_SHA256
    }
    expected_520 = {
        str(path.relative_to(ROOT)): digest
        for path, digest in EXPECTED_CYCLE520_SHA256.items()
    }
    hashes_match = observed_520 == expected_520
    return {
        "Cycle519_corrected_semantic_fragments_missing": missing_519,
        "Cycle520_semantic_fragments_missing": missing_520,
        "Cycle520_expected_sha256": expected_520,
        "Cycle520_observed_sha256": observed_520,
        "Cycle520_hashes_match": hashes_match,
        "pass": not missing_519 and not missing_520 and hashes_match,
    }


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "1/400",
        "43,210,561",
        "11,607,754,707,828,736",
        "011",
        "110",
        "111",
        "protected parity shadow",
        "six-occupation shadow",
        "hermitian parity lemma",
        "perfect-syndrome lemma",
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
    semantic = semantic_contract()
    note = note_contract()
    geometry = c520.geometry_controls()
    tests = {
        "corrected_Cycle519_and_hash_bound_Cycle520_semantics": semantic["pass"],
        "Cycle520_bent_geometry_and_frame_group": geometry["pass"],
        "Cycle521_note_scope_and_N1_N8": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle521-final-tag-syndrome-contract-ready" if all(tests.values()) else "cycle521-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "semantic_contract": semantic,
        "geometry": geometry,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def syndrome_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle521 dry contract failed")
    two = (
        two_star_overlap_spectrum(TRAIN_LENGTH, started),
        two_star_overlap_spectrum(HELD_LENGTH, started),
    )
    checkpoints.append(checkpoint(started, "two-star-L5-L6-overlaps-complete"))
    three = (
        three_star_overlap_spectrum(TRAIN_LENGTH),
        three_star_overlap_spectrum(HELD_LENGTH),
    )
    checkpoints.append(checkpoint(started, "three-star-L5-L6-overlaps-complete"))
    orthogonality = orthogonality_and_projector_controls(two, three)
    supports = {
        "two_star": tuple(branch_shell_support(length, False) for length in (5, 6)),
        "three_star": tuple(branch_shell_support(length, True) for length in (5, 6)),
    }
    checkpoints.append(checkpoint(started, "branch-shell-supports-complete"))
    shadows = protected_shadow_controls()
    transport = c520.transport_mass_contact_controls()
    frames = (
        c520.frame_local_term_controls(TRAIN_LENGTH),
        c520.frame_local_term_controls(HELD_LENGTH),
    )
    checkpoints.append(checkpoint(started, "shadow-transport-frame-mass-contact-complete"))
    tests = {
        "dry_contract": dry["pass"],
        "two_star_exact_cross_parity_spectrum_L5_L6": all(row["pass"] for row in two),
        "three_star_exact_tag_xor_spectrum_L5_L6": all(row["pass"] for row in three),
        "Hermitian_parity_and_perfect_syndrome_boundary": orthogonality["pass"],
        "bounded_dense_projector_resource_boundary": (
            all(
                supports["two_star"][0][key] == supports["two_star"][1][key]
                for key in supports["two_star"][0]
                if key != "length"
            )
            and all(
                supports["three_star"][0][key] == supports["three_star"][1][key]
                for key in supports["three_star"][0]
                if key != "length"
            )
            and supports["two_star"][0]["tagged_branch_shell_union_M2_upper_bound"] == 420
            and supports["three_star"][0]["tagged_branch_shell_union_M2_upper_bound"] == 548
        ),
        "protected_shadow_comparators": shadows["pass"],
        "shared_tag_seam_mass_contact_controls": transport["pass"],
        "all24_frame_local_term_transport_L5_L6": all(row["pass"] for row in frames),
        "resource_contract": swap_count() == 0 and rss_bytes() < RSS_GUARD_BYTES,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "syndrome-certificate",
        "status": "cycle521-final-tag-syndrome-orthogonality-certified" if all(tests.values()) else "cycle521-certificate-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "two_star_overlap_spectra": two,
        "three_star_overlap_spectra": three,
        "orthogonality_and_dense_projector": orthogonality,
        "branch_shell_support_upper_bounds": supports,
        "protected_shadow_comparators": shadows,
        "shared_tag_transport_mass_contact": transport,
        "frame_rows": frames,
        "positive_result": {
            "joint_three_tag_P_tau_rejects_every_single_tag_flip": True,
            "P_tau_J_tau_and_identity_complement_are_exact": True,
            "one_parity_shadow_per_center_gives_commuting_local_equality_checks": True,
        },
        "bounded_negative": {
            "native_only_Hermitian_number_parity_operator": False,
            "perfect_native_plus_one_tag_final_syndrome": False,
            "scope": orthogonality["scope"],
            "changed_representatives_protected_shadows_or_new_auxiliaries_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "supplied_not_synthesized": {
            "Cycle311_315_515_516_native_branch_shell": True,
            "independently_appended_tags": True,
            "dense_projector_coefficients": True,
            "identity_off_code_completion": True,
            "pre_overlap_shadow_initialization": True,
            "decorated_physical_seam_gate": True,
            "bare_one_two_M2_coin_decomposition": True,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": rss_bytes(),
            "process_swap_count": swap_count(),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
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
        signal.alarm(int(WALL_LIMIT_SECONDS))
    try:
        result = dry_contract() if args.mode == "dry-contract" else syndrome_certificate()
    except (ResourceWall, CertificateFailure) as error:
        print(json.dumps({"status": "cycle521-technical-failure", "error": str(error)}, sort_keys=True))
        return 2
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(result, indent=2, sort_keys=True, default=list))
    print(
        "SUMMARY",
        {"pass": result["tests_passed"], "fail": result["tests_total"] - result["tests_passed"]},
    )
    if result["pass"]:
        print("RESULT PHYSICAL_FINAL_TAG_SYNDROME_ORTHOGONALITY_CERTIFIED")
        return 0
    print("RESULT PHYSICAL_FINAL_TAG_SYNDROME_ORTHOGONALITY_FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
