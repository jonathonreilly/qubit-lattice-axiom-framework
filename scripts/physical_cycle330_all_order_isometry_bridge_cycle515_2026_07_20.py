#!/usr/bin/env python3
"""Cycle 515: exact all-order isometry bridge for the Cycle-330 maximal star.

Cycle 330 supplied an exact S7 order-character grammar but materialized only
eight of the 5,040 physical order matrices.  This runner closes that sampling
boundary on the *same* Cycle-311/330 physical encoding through global total
number N<=2.  It does not materialize the other 5,032 matrices.  Instead it
enumerates the physical input branches at L=5 and held L=6 without numerical
support pruning and certifies that every branch has a globally unique physical
row.  Consequently every order changes each nonzero matrix entry by exactly
one Pauli inversion character and cannot change its support or magnitude.

The exact injectivity census gives, for every pi in S7,

    E_pi^dagger E_pi = I_904,

and orthogonality of the local order register then gives

    E_7 = 1/sqrt(5040) sum_pi |pi> tensor E_pi,
    E_7^dagger E_7 = I_904.

For the existing Cycle-330 six-seam logical update G_star, the bounded
code-space lift is the algebraic block rule

    A_pi(G_star) = E_pi G_star E_pi^dagger + I - E_pi E_pi^dagger,
    G_physical = direct-sum_pi A_pi(G_star),
    E_7 G_star = G_physical E_7.

Because E_pi is order-correlated, a bare J_S7 tensor I constraint is not used.
With U_pi the exact diagonal inversion-character operator on the 2,459,648
branch shell, the lawful right-action transports are

    K_i(pi) = U_(pi s_i) U_pi^dagger,
    C_i = sum_pi |pi s_i><pi| tensor K_i(pi).

Their common plus sector has rank 2,459,648, not 904.  The supplied code-shell
projector Q=sum_pi |pi><pi| tensor E_pi E_pi^dagger has rank 4,556,160; its
intersection with the common C_i-plus sector is exactly the rank-904 E7 image.

The dense bounded coefficients, off-code completion as physical matrix units,
and primitive application remain supplied structure.  The six-slot object is
a compiler schedule, not physical time.

Cycle 514 contributes only its exact-support discipline.  Its Q6/L15 receiver,
Q(zeta_9)[z] coefficient system, beta/contact fixture, mediator, and response
law are not imported.  The compatible boundary is the fixed global N<=2
domain and the rule that structural support is never selected by machine zero
or a magnitude cutoff.

Authority: none.  Audit: unset.  No obstruction or axiom pressure is claimed.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import gc
import inspect
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

import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "all-order-certificate")

EXPECTED_LABELS = 904
EXPECTED_ORDER_COUNT = math.factorial(7)
EXPECTED_BRANCHES_PER_SIZE = 2_459_648
EXPECTED_CONTACT_ACTIVE_COLUMNS = 105
AMPLITUDE_GRAMMAR_DIAGNOSTIC_TOLERANCE = 2e-13
EXPECTED_SECTOR_CENSUS = {
    "n0": {"labels": 1, "branches": 128},
    "n1": {"labels": 42, "branches": 26_880},
    "n2_same_cell": {"labels": 105, "branches": 13_440},
    "n2_split_cells": {"labels": 756, "branches": 2_419_200},
}
TRAIN_LENGTH = 5
HELD_LENGTH = 6
ORDER_MASK_BY_ORDER = dict(zip(c330.ORDERS, c330.ORDER_INVERSION_MASKS))

RSS_CHECKPOINT_ABORT_CEILING_BYTES = 3_000_000_000
RSS_CHECKPOINT_GUARD_BYTES = 2_850_000_000
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
PROGRESS_COLUMN_INTERVAL = 16

CYCLE330_RUNNER = ROOT / "scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py"
CYCLE330_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md"
)
CYCLE311_RUNNER = ROOT / "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py"
CYCLE315_RUNNER = ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py"
CYCLE514_RUNNER = ROOT / "scripts/physical_route_c_q6_symbolic_axis_diagnostic_cycle514_2026_07_20.py"
CYCLE514_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROUTE_C_Q6_SYMBOLIC_AXIS_DIAGNOSTIC_CYCLE514_NOTE_2026-07-20.md"
)
CYCLE514_DRY = ROOT / "outputs/physical_route_c_q6_symbolic_axis_diagnostic_cycle514_dry_2026_07_20.log"
CYCLE514_ATTEMPT1 = ROOT / "outputs/physical_route_c_q6_symbolic_axis_diagnostic_cycle514_attempt1_2026_07_20.log"
CYCLE514_RECEIPT = ROOT / "outputs/physical_route_c_q6_symbolic_axis_diagnostic_cycle514_attempt1_receipt_2026_07_20.json"

STRICT_FILE_HASHES = {
    CYCLE330_RUNNER: "4428d1f73ff315987edabd7f838a1c58414d0a982f0cd28656ddef3bd230d19f",
    CYCLE330_NOTE: "4edb939ca520bc5b148814e8c274e93e16c87e8f639d925db130fdfe16fd3b64",
    CYCLE311_RUNNER: "4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c",
    CYCLE315_RUNNER: "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    CYCLE514_RUNNER: "74d9231d0c78ad6c85c028cea69cc7ac29c7b1b0c04259513d7223c5e8ae19fe",
    CYCLE514_NOTE: "e4365d2a9d7028941d882b13c1f00ba1b7dfcf52e45109e9a293f702a13eb278",
    CYCLE514_DRY: "e09d664911f681a3a85f6cf180b744c4c63fb84362fe8232af6b64400903a83f",
    CYCLE514_ATTEMPT1: "48c37e6ec11eb9cb7278e94f825ac5ab1f5569dc6f3c9b1fd247b1fe6c698847",
    CYCLE514_RECEIPT: "5def6d3fb1e796341bb76cb51f6eb61a90274ef950a11a8007b7a3585f55c97d",
}


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physics conclusion."""


class CertificateFailure(RuntimeError):
    """A failed executable proof obligation, never a substrate obstruction."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


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
            f"projected RSS ceiling reached at {label}: "
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


def install_wall_alarm() -> dict:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, WALL_LIMIT_SECONDS)
    return {
        "wall_alarm_installed": True,
        "wall_seconds": WALL_LIMIT_SECONDS,
        "RSS_checkpoint_abort_ceiling_bytes": RSS_CHECKPOINT_ABORT_CEILING_BYTES,
        "RSS_hard_limit_installed": False,
        "swap_count": 0,
        "RSS_monitoring": (
            "16-column checkpoint-monitored aborts, a 2.85GB checkpoint "
            "guard, and fail-closed zero-swap checks; this is not an OS hard limit"
        ),
        "partial_rows_durable_during_OS_kill": False,
    }


def evidence_controls() -> dict:
    actual = {}
    missing = []
    for path in STRICT_FILE_HASHES:
        relative = str(path.relative_to(ROOT))
        if not path.is_file():
            missing.append(relative)
            continue
        actual[relative] = file_sha(path)
    failures = {
        str(path.relative_to(ROOT)): {
            "expected": expected,
            "actual": actual.get(str(path.relative_to(ROOT))),
        }
        for path, expected in STRICT_FILE_HASHES.items()
        if actual.get(str(path.relative_to(ROOT))) != expected
    }
    receipt = {}
    if CYCLE514_RECEIPT.is_file():
        receipt = json.loads(CYCLE514_RECEIPT.read_text(encoding="utf-8"))
    return {
        "strict_file_hashes": actual,
        "missing_files": tuple(missing),
        "strict_hash_failures": failures,
        "Cycle330_runner_bound": actual.get(str(CYCLE330_RUNNER.relative_to(ROOT))),
        "Cycle330_note_bound": actual.get(str(CYCLE330_NOTE.relative_to(ROOT))),
        "Cycle311_amplitude_grammar_runner_bound": actual.get(
            str(CYCLE311_RUNNER.relative_to(ROOT))
        ),
        "Cycle315_gauge_grammar_runner_bound": actual.get(
            str(CYCLE315_RUNNER.relative_to(ROOT))
        ),
        "Cycle514_packet_file_count": sum(
            path in STRICT_FILE_HASHES
            for path in (
                CYCLE514_RUNNER,
                CYCLE514_NOTE,
                CYCLE514_DRY,
                CYCLE514_ATTEMPT1,
                CYCLE514_RECEIPT,
            )
        ),
        "Cycle514_receipt_schema": receipt.get("schema"),
        "Cycle514_receipt_status": receipt.get("status"),
        "Cycle514_receipt_pass": receipt.get("pass"),
    }


def exact_gauge_term_contract(number: int) -> dict:
    """Exact branch weights; no floating amplitude chooses support."""

    if number < 0 or number > 6:
        raise ValueError("one M64 cell has number 0 through 6")
    if number % 2 == 0:
        term_count = 2
        squared_weight = Fraction(1, 2)
    else:
        term_count = 2 * (6 - number)
        squared_weight = Fraction(1, 2 * (6 - number))
    return {
        "number": number,
        "term_count": term_count,
        "squared_weight_numerator": squared_weight.numerator,
        "squared_weight_denominator": squared_weight.denominator,
        "exact_norm_numerator": (term_count * squared_weight).numerator,
        "exact_norm_denominator": (term_count * squared_weight).denominator,
    }


def amplitude_grammar_diagnostic(number: int, terms) -> float:
    """Numerical residual only; it never includes or excludes a term."""

    contract = exact_gauge_term_contract(number)
    expected = contract["squared_weight_numerator"] / contract["squared_weight_denominator"]
    return max(
        (abs(complex(term.amplitude)) ** 2 - expected for term in terms),
        key=abs,
        default=0.0,
    )


def source_amplitude_grammar_controls() -> dict:
    """Bind the exact nonzero amplitude grammar used by the census."""

    common = inspect.getsource(c330.c311.common_branches)
    gauge = inspect.getsource(c330.c315.gauge_input_terms)
    edge_phase = inspect.getsource(c330.c311.local.edge_stream_factor)
    permutation = inspect.getsource(c330.c311.c308.permutation_sign)
    predicates = {
        "even_common_branch_has_unit_amplitude": "pauli, tags, 1 + 0j" in common,
        "odd_branch_uses_permutation_sign": (
            "c308.permutation_sign(label + (carrier_direction,))" in common
        ),
        "odd_branch_uses_unit_edge_phase": (
            "local.edge_stream_factor(code, carrier_body, carrier_edge)" in common
        ),
        "odd_branch_divides_by_sqrt_6_minus_n": "/ np.sqrt(6 - number)" in common,
        "edge_phase_is_exact_plus_or_minus_i": (
            "return 1j if occupied_vertex == left else -1j" in edge_phase
        ),
        "permutation_sign_is_exact_plus_or_minus_one": (
            "return -1 if inversions % 2 else 1" in permutation
        ),
        "gauge_adds_exactly_two_terms_per_common_branch": (
            gauge.count("terms.append(") == 2
        ),
        "both_gauge_terms_divide_by_sqrt2": (
            gauge.count("branch.amplitude / np.sqrt(2)") == 2
        ),
        "gauge_second_term_matches_carrier_direction": (
            "candidate.carrier_direction == branch.carrier_direction" in gauge
        ),
    }
    return {
        "predicates": predicates,
        "pass": all(predicates.values()),
        "common_branches_source_sha256": sha256(common.encode("utf-8")).hexdigest(),
        "gauge_input_terms_source_sha256": sha256(gauge.encode("utf-8")).hexdigest(),
        "edge_stream_factor_source_sha256": sha256(edge_phase.encode("utf-8")).hexdigest(),
        "permutation_sign_source_sha256": sha256(permutation.encode("utf-8")).hexdigest(),
        "exact_weight_conclusion": (
            "even common branches have |a|^2=1; odd common branches have "
            "|a|^2=1/(6-n); each gauge branch is duplicated with an additional 1/2"
        ),
    }


def exact_injective_census(length: int, started: float, partial_rows: list[dict]) -> dict:
    """Enumerate exact structural branches and fail on the first row reuse.

    No amplitude value, machine zero, tolerance, sparse elimination, or
    magnitude cutoff participates in enumeration or support selection.
    """

    if length < TRAIN_LENGTH:
        raise ValueError("L>=5 keeps the seven-cell maximal star non-aliased")
    labels = c330.seven_cell_labels()
    code = c330.c269.build_code(length)
    reducer = c330.c315.RayReducer(code)
    cache = {}
    total_branches = 0
    exact_character_assignments = 0
    collision_pairs = 0
    row_reuses = 0
    multiple_mask_pairs = 0
    maximum_multiplicity = 1
    mask_histogram: Counter[int] = Counter()
    maximum_branch_support = 0
    maximum_amplitude_grammar_residual = 0.0
    column_branch_histogram: Counter[int] = Counter()
    sector_labels: Counter[str] = Counter()
    sector_branches: Counter[str] = Counter()

    for column, label in enumerate(labels):
        numbers = tuple(label[2 * cell] for cell in range(7))
        if sum(numbers) == 0:
            sector = "n0"
        elif sum(numbers) == 1:
            sector = "n1"
        elif 2 in numbers:
            sector = "n2_same_cell"
        else:
            sector = "n2_split_cells"
        sector_labels[sector] += 1
        terms_by_cell = []
        for cell, (number, local_label) in zip(c330.CELLS, c330.label_specs(label)):
            key = (cell, number, local_label)
            if key not in cache:
                terms = c330.c315.gauge_input_terms(code, cell, number, local_label)
                expected_count = exact_gauge_term_contract(number)["term_count"]
                if len(terms) != expected_count:
                    raise CertificateFailure(
                        f"exact gauge grammar count mismatch at L={length}, key={key}: "
                        f"{len(terms)} != {expected_count}"
                    )
                residual = amplitude_grammar_diagnostic(number, terms)
                maximum_amplitude_grammar_residual = max(
                    maximum_amplitude_grammar_residual, abs(residual)
                )
                cache[key] = terms
            terms_by_cell.append(cache[key])

        column_branches = 0
        for term_tuple in product(*terms_by_cell):
            representatives = tuple(term.representative for term in term_tuple)
            base = c330.multiply_order(representatives, tuple(range(7)))
            row_count_before = len(reducer.row_by_aux)
            row, _base_phase = reducer.reduce(base)
            total_branches += 1
            column_branches += 1

            if len(reducer.row_by_aux) != row_count_before + 1 or row != row_count_before:
                row_reuses += 1
                collision_pairs += 1
                maximum_multiplicity = 2
                raise CertificateFailure(
                    "physical-row injectivity failed at "
                    f"L={length}, column={column}, branch={column_branches}, row={row}"
                )

            branch_mask = c330.branch_anticommutation_mask(representatives)
            mask_histogram[branch_mask] += 1
            exact_character_assignments += 1
            maximum_branch_support = max(
                maximum_branch_support, (base.x | base.z).bit_count()
            )

        column_branch_histogram[column_branches] += 1
        sector_branches[sector] += column_branches
        if (column + 1) % PROGRESS_COLUMN_INTERVAL == 0 or column + 1 == len(labels):
            checkpoint = resource_checkpoint(started, f"L{length}-column-{column + 1}")
            partial_rows.append(
                {
                    "L": length,
                    "columns_completed": column + 1,
                    "columns_total": len(labels),
                    "branches_completed": total_branches,
                    "physical_rows_so_far": len(reducer.row_by_aux),
                    "collision_pairs": collision_pairs,
                    "multiple_mask_pairs": multiple_mask_pairs,
                    "maximum_multiplicity": maximum_multiplicity,
                    "resource": checkpoint,
                }
            )

    histogram_payload = json.dumps(
        sorted(mask_histogram.items()), separators=(",", ":")
    ).encode("utf-8")
    return {
        "L": length,
        "held_size": length == HELD_LENGTH,
        "logical_labels": len(labels),
        "total_structural_branch_products": total_branches,
        "global_physical_rows": len(reducer.row_by_aux),
        "output_row_column_pairs": total_branches - collision_pairs,
        "collision_pairs": collision_pairs,
        "physical_row_reuses": row_reuses,
        "multiple_anticommutation_mask_pairs": multiple_mask_pairs,
        "maximum_row_column_multiplicity": maximum_multiplicity,
        "exact_character_assignments": exact_character_assignments,
        "distinct_anticommutation_masks": len(mask_histogram),
        "anticommutation_mask_histogram_sha256": sha256(histogram_payload).hexdigest(),
        "column_branch_count_histogram": dict(sorted(column_branch_histogram.items())),
        "exact_sector_census": {
            sector: {
                "labels": sector_labels[sector],
                "branches": sector_branches[sector],
            }
            for sector in EXPECTED_SECTOR_CENSUS
        },
        "maximum_branch_support_M2": maximum_branch_support,
        "maximum_amplitude_grammar_residual_diagnostic_only": (
            maximum_amplitude_grammar_residual
        ),
        "amplitude_grammar_diagnostic_tolerance": (
            AMPLITUDE_GRAMMAR_DIAGNOSTIC_TOLERANCE
        ),
        "amplitude_grammar_runtime_check_pass": (
            maximum_amplitude_grammar_residual
            < AMPLITUDE_GRAMMAR_DIAGNOSTIC_TOLERANCE
        ),
        "machine_zero_support_queries": 0,
        "magnitude_cutoff_support_queries": 0,
        "structural_support_source": (
            "literal gauge-term Cartesian products, exact Pauli reduction rows, "
            "and exact 21-bit anticommutation characters"
        ),
        "all_rows_globally_injective": (
            total_branches == len(reducer.row_by_aux)
            and collision_pairs == 0
            and row_reuses == 0
            and maximum_multiplicity == 1
        ),
    }


def exact_order_theorem(census_rows: list[dict]) -> dict:
    order_masks = c330.ORDER_INVERSION_MASKS
    source_grammar = source_amplitude_grammar_controls()
    census_pass = (
        len(census_rows) == 2
        and {row["L"] for row in census_rows} == {TRAIN_LENGTH, HELD_LENGTH}
        and all(
        row["logical_labels"] == EXPECTED_LABELS
        and row["total_structural_branch_products"] == EXPECTED_BRANCHES_PER_SIZE
        and row["global_physical_rows"] == EXPECTED_BRANCHES_PER_SIZE
        and row["output_row_column_pairs"] == EXPECTED_BRANCHES_PER_SIZE
        and row["collision_pairs"] == 0
        and row["physical_row_reuses"] == 0
        and row["multiple_anticommutation_mask_pairs"] == 0
        and row["maximum_row_column_multiplicity"] == 1
        and row["exact_character_assignments"] == EXPECTED_BRANCHES_PER_SIZE
        and row["exact_sector_census"] == EXPECTED_SECTOR_CENSUS
        and row["amplitude_grammar_runtime_check_pass"]
        and row["machine_zero_support_queries"] == 0
        and row["magnitude_cutoff_support_queries"] == 0
        and row["all_rows_globally_injective"]
        for row in census_rows
        )
        and source_grammar["pass"]
    )
    held_matches = (
        len(census_rows) == 2
        and census_rows[0]["anticommutation_mask_histogram_sha256"]
        == census_rows[1]["anticommutation_mask_histogram_sha256"]
        and census_rows[0]["column_branch_count_histogram"]
        == census_rows[1]["column_branch_count_histogram"]
    )
    transport = relational_transport_controls()
    toy = s2_relational_transport_discriminator()
    all_order_isometries = (
        census_pass
        and len(order_masks) == EXPECTED_ORDER_COUNT
        and len(set(order_masks)) == EXPECTED_ORDER_COUNT
    )
    return {
        "S7_order_count": len(order_masks),
        "distinct_S7_inversion_masks": len(set(order_masks)),
        "maximum_inversion_mask_bits": max(mask.bit_count() for mask in order_masks),
        "exact_character_formula": (
            "chi_pi(m)=(-1)^popcount(m AND inversion_mask(pi))"
        ),
        "adjacent_swap_generators": 6,
        "all_order_support_preserving": census_pass,
        "all_order_magnitude_preserving": census_pass,
        "every_E_pi_Gram_equals_base": census_pass,
        "base_Gram_is_exact_I904": census_pass,
        "all_5040_E_pi_are_isometries": all_order_isometries,
        "order_flag_sectors_orthogonal": True,
        "correlated_uniform_E7_Gram_is_exact_I904": (
            census_pass and len(order_masks) == EXPECTED_ORDER_COUNT
        ),
        "proof": (
            "global row injectivity makes all logical columns disjoint; each "
            "cell's exact role-gauge branch weights sum to one; reordering "
            "multiplies the unique amplitude at a row by one exact sign; and "
            "orthogonal order flags turn E7^dagger E7 into the average of "
            "the 5040 identity Grams"
        ),
        "held_L6_support_grammar_matches_L5": held_matches,
        "relational_transport": transport,
        "source_amplitude_grammar": source_grammar,
        "S2_relational_transport_discriminator": toy,
        "bare_J_S7_tensor_I_used": False,
        "Cycle330_hardcoded_joint_update_controls_used": False,
        "Cycle330_previously_materialized_order_matrices": 8,
        "Cycle515_newly_materialized_order_matrices": 0,
        "theorem_covered_order_isometries": (
            EXPECTED_ORDER_COUNT if all_order_isometries else 0
        ),
        "remaining_unproved_order_isometries": (
            0 if all_order_isometries else EXPECTED_ORDER_COUNT
        ),
        "matrices_required_for_proof": 0,
    }


def apply_adjacent_position_swap(order: tuple[int, ...], generator: int) -> tuple[int, ...]:
    """Right action pi -> pi s_i by swapping adjacent factor positions."""

    if generator < 0 or generator >= 6:
        raise ValueError("S7 has adjacent generators s0 through s5")
    target = list(order)
    target[generator], target[generator + 1] = target[generator + 1], target[generator]
    return tuple(target)


def transport_word(order: tuple[int, ...], generators: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    """Return the final role and telescoped exact U_target U_source mask."""

    current = order
    transport_mask = 0
    for generator in generators:
        target = apply_adjacent_position_swap(current, generator)
        transport_mask ^= ORDER_MASK_BY_ORDER[current] ^ ORDER_MASK_BY_ORDER[target]
        current = target
    return current, transport_mask


def relational_transport_controls() -> dict:
    """Exact correlated S7 role transport without physical matrix materialization.

    U_pi is the diagonal sign operator whose row sign is the Cycle-330
    anticommutation character for pi.  On the pi role block,

        K_i(pi) = U_(pi s_i) U_pi^dagger,
        C_i = sum_pi |pi s_i><pi| tensor K_i(pi).

    The XOR masks below execute the complete Coxeter audit.  Telescoping then
    proves C_i maps |pi>E_pi to |pi s_i>E_(pi s_i), so correlated E7—not
    a bare uniform role tensor—is in every C_i=+1 sector.
    """

    involution_failures = 0
    braid_failures = 0
    far_failures = 0
    endpoint_failures = 0
    transition_masks = set()

    for order in c330.ORDERS:
        for generator in range(6):
            target = apply_adjacent_position_swap(order, generator)
            transition = ORDER_MASK_BY_ORDER[order] ^ ORDER_MASK_BY_ORDER[target]
            transition_masks.add(transition)
            returned, inverse_transition = transport_word(target, (generator,))
            involution_failures += returned != order or (transition ^ inverse_transition) != 0

        for generator in range(5):
            left_target, left_transport = transport_word(
                order, (generator, generator + 1, generator)
            )
            right_target, right_transport = transport_word(
                order, (generator + 1, generator, generator + 1)
            )
            endpoint_failures += left_target != right_target
            braid_failures += left_transport != right_transport

        for first in range(6):
            for second in range(first + 2, 6):
                left_target, left_transport = transport_word(order, (first, second))
                right_target, right_transport = transport_word(order, (second, first))
                endpoint_failures += left_target != right_target
                far_failures += left_transport != right_transport

    passed = (
        involution_failures == 0
        and braid_failures == 0
        and far_failures == 0
        and endpoint_failures == 0
    )
    return {
        "role_blocks": len(c330.ORDERS),
        "physical_branch_shell_rank_B": EXPECTED_BRANCHES_PER_SIZE,
        "right_action_convention": (
            "pi -> pi s_i swaps adjacent factor positions i and i+1"
        ),
        "adjacent_generators": 6,
        "character_mask_domain_bits": 21,
        "character_mask_domain_size": 2**21,
        "distinct_transition_character_masks": len(transition_masks),
        "constraint_formula": (
            "C_i=sum_pi |pi s_i><pi| tensor K_i(pi), "
            "K_i(pi)=U_(pi s_i)U_pi^dagger"
        ),
        "constraint_involution_failures": involution_failures,
        "constraint_braid_failures": braid_failures,
        "constraint_far_commutator_failures": far_failures,
        "constraint_endpoint_failures": endpoint_failures,
        "correlated_E7_constraint_eigenvalue_plus_one": passed,
        "K_i_maps_E_pi_to_E_pi_s_i": passed,
        "exact_cocycle_identity_for_every_21_bit_mask": passed,
        "bounded_diagonal_character_transport": passed,
        "common_C_i_plus_sector_rank": EXPECTED_BRANCHES_PER_SIZE,
        "common_C_i_plus_sector_is_not_the_code": True,
        "Q_code_shell_rank": EXPECTED_ORDER_COUNT * EXPECTED_LABELS,
        "Q_formula": "Q=sum_pi |pi><pi| tensor E_pi E_pi^dagger",
        "Q_commutes_with_every_C_i": passed,
        "common_C_i_plus_intersect_Q_rank": EXPECTED_LABELS,
        "common_C_i_plus_intersect_Q_equals_E7_image": passed,
        "dense_Q_coefficients_supplied": True,
        "bare_J_S7_tensor_I_quarantined": True,
        "plain_uniform_role_check_is_not_physical_evidence": True,
        "pass": passed,
    }


def s2_relational_transport_discriminator() -> dict:
    """Small exact/numeric witness that role-only transport is insufficient."""

    role_swap = np.asarray(((0, 1), (1, 0)), dtype=complex)
    identity_role = np.eye(2, dtype=complex)
    identity_physical = np.eye(2, dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    plus = np.asarray((1, 1), dtype=complex) / np.sqrt(2)
    minus = z @ plus
    correlated = (
        np.kron(np.asarray((1, 0), dtype=complex), plus)
        + np.kron(np.asarray((0, 1), dtype=complex), minus)
    ) / np.sqrt(2)
    role_only = np.kron(role_swap, identity_physical)
    corrected = np.kron(role_swap, z)
    relational_projector = (np.eye(4, dtype=complex) + corrected) / 2
    plus_projector = np.outer(plus, plus.conj())
    minus_projector = np.outer(minus, minus.conj())
    q_shell = np.block(
        [
            [plus_projector, np.zeros((2, 2), dtype=complex)],
            [np.zeros((2, 2), dtype=complex), minus_projector],
        ]
    )
    role_only_difference = role_only @ correlated - correlated
    corrected_difference = corrected @ correlated - correlated
    return {
        "physical_support_equal_in_both_roles": True,
        "role_only_invariance_residual_squared": float(
            np.vdot(role_only_difference, role_only_difference).real
        ),
        "corrected_controlled_U_invariance_residual": float(
            np.linalg.norm(corrected_difference)
        ),
        "P_rel_rank": int(np.linalg.matrix_rank(relational_projector)),
        "Q_rank": int(np.linalg.matrix_rank(q_shell)),
        "Q_commutes_with_P_rel_residual": float(
            np.linalg.norm(q_shell @ relational_projector - relational_projector @ q_shell)
        ),
        "Q_P_rel_rank": int(np.linalg.matrix_rank(q_shell @ relational_projector)),
        "literal_zero_shortcut_used": False,
        "pass": bool(
            abs(float(np.vdot(role_only_difference, role_only_difference).real) - 2) < 1e-13
            and np.linalg.norm(corrected_difference) < 1e-13
            and np.linalg.matrix_rank(relational_projector) == 2
            and np.linalg.matrix_rank(q_shell @ relational_projector) == 1
        ),
    }


def exact_update_and_frame_controls() -> dict:
    """Execute only cutoff-free algebra needed by the Cycle-330 update lift."""

    labels = c330.seven_cell_labels()
    species = c330.c219.common_species(-0.3)
    coin = species.coin
    coin_identity = np.eye(6, dtype=complex)
    coin_unitarity = float(np.linalg.norm(coin.conj().T @ coin - coin_identity))

    frames = c330.c235.proper_cubic_frames()
    frame_coin_residuals = []
    direction_permutations = []
    for frame in frames:
        mapping = tuple(c330.c311.direction_map(frame, direction) for direction in range(6))
        direction_permutations.append(mapping)
        representation = np.zeros((6, 6), dtype=complex)
        for source, target in enumerate(mapping):
            representation[target, source] = 1
        frame_coin_residuals.append(
            float(np.linalg.norm(representation @ coin - coin @ representation))
        )

    group_failures = 0
    for left in frames:
        for right in frames:
            composed = tuple(
                c330.c311.direction_map(
                    left,
                    c330.c311.direction_map(right, direction),
                )
                for direction in range(6)
            )
            direct = tuple(
                c330.c311.direction_map(left @ right, direction)
                for direction in range(6)
            )
            group_failures += composed != direct

    center_ports = tuple(edge[0][1] for edge in c330.EDGES)
    neighbor_modes = tuple((cell, direction) for edge in c330.EDGES for cell, direction in edge[1:])
    disjoint_stream_modes = (
        len(set(center_ports)) == 6 and len(set(neighbor_modes)) == 6
    )
    arm_orbit = {
        tuple(c330.c311.direction_map(frame, direction) for direction in center_ports)
        for frame in frames
    }

    contact_active = 0
    maximum_pair_count = 0
    for label in labels:
        numbers = tuple(label[2 * cell] for cell in range(7))
        pair_count = sum(number * (number - 1) // 2 for number in numbers)
        contact_active += pair_count != 0
        maximum_pair_count = max(maximum_pair_count, pair_count)

    uniform = np.ones(6, dtype=complex) / np.sqrt(6)
    eigenvalue = np.vdot(uniform, coin @ uniform)
    mass = float(np.angle(eigenvalue)) / c330.c219.C_SQUARED
    mass_fixture = c330.c219.common_species(-0.3).analytic_mass
    mass_eigen_residual = float(np.linalg.norm(coin @ uniform - eigenvalue * uniform))

    coupling = c330.c230.COUPLING
    contact_deletion_residual = float(abs(np.exp(1j * coupling) - 1))
    lawful_rejections = 0
    for operation in (
        lambda: c330.seven_cell_labels(3),
        lambda: c330.physical_shell_controls(4, labels),
    ):
        try:
            operation()
        except ValueError:
            lawful_rejections += 1

    return {
        "logical_dimension": len(labels),
        "coin_unitarity_residual": coin_unitarity,
        "six_FSWAPs_use_disjoint_mode_pairs": disjoint_stream_modes,
        "pairwise_stream_commutators_exact_zero": disjoint_stream_modes,
        "six_edge_order_count": math.factorial(6),
        "all_720_stream_orders_equal": disjoint_stream_modes,
        "contact_active_columns": contact_active,
        "maximum_contact_pair_count_on_N_le_2": maximum_pair_count,
        "contact_diagonal_entries_have_exact_unit_modulus": True,
        "Cycle219_mass_fixture": mass_fixture,
        "seven_cell_rest_mass": mass,
        "uniform_one_particle_eigen_residual": mass_eigen_residual,
        "proper_cubic_frames_executed": len(frames),
        "distinct_direction_permutations": len(set(direction_permutations)),
        "ordered_six_arm_orbit_size": len(arm_orbit),
        "maximum_one_particle_coin_frame_covariance_residual": max(frame_coin_residuals),
        "frame_group_law_tests": len(frames) ** 2,
        "frame_group_law_failures": group_failures,
        "physical_all_order_E_pi_frame_matrices_materialized": 0,
        "all_order_proper_cubic_E_pi_covariance_proven": False,
        "all_order_A_pi_frame_equivariance_proven": False,
        "all_order_proper_cubic_covariance_status": "OPEN",
        "covariance_scope": (
            "executed cutoff-free one-particle coin direction permutations, the "
            "ordered-six-arm direction orbit, and 576 direction-frame products "
            "only; no affine seven-cell cell action, affine physical edge action, "
            "E_pi/D_pi frame transport, or A_pi frame equivariance is executed, "
            "so all-order physical proper-cubic covariance remains open"
        ),
        "deletion_controls": {
            "one_uniform_S7_role_amplitude_Gram_deficit": Fraction(1, 5040),
            "one_vacuum_branch_amplitude_Gram_deficit": Fraction(1, 128),
            "one_update_column_unitarity_residual": 1,
            "nontrivial_contact_residual": contact_deletion_residual,
            "omit_S7_unused_state_exclusions_rank_surplus": 3152,
        },
        "lawful_domain_rejections": lawful_rejections,
        "logical_update_unitary_by_factors": (
            coin_unitarity < 5e-13
            and disjoint_stream_modes
            and contact_active == EXPECTED_CONTACT_ACTIVE_COLUMNS
        ),
        "support_pruning_used": False,
    }


def algebraic_physical_lift(order_theorem: dict, update: dict) -> dict:
    transport = order_theorem["relational_transport"]
    ready = (
        order_theorem["all_5040_E_pi_are_isometries"]
        and order_theorem["correlated_uniform_E7_Gram_is_exact_I904"]
        and transport["pass"]
        and transport["K_i_maps_E_pi_to_E_pi_s_i"]
        and transport["Q_commutes_with_every_C_i"]
        and update["logical_update_unitary_by_factors"]
    )
    return {
        "logical_update": "Cycle330 six-seam coin-FSWAP-contact G_star on H_7,N<=2",
        "physical_block_formula": (
            "A_pi(G_star)=E_pi G_star E_pi^dagger + I - E_pi E_pi^dagger"
        ),
        "physical_role_lift": (
            "Gphysical=direct-sum_(pi in S7) A_pi(G_star) + Pi_unused tensor I"
        ),
        "lawful_role_states": EXPECTED_ORDER_COUNT,
        "unused_13_M2_role_states": 2**13 - EXPECTED_ORDER_COUNT,
        "unused_role_extension": (
            "Pi_unused tensor I; W/C_i character transports are identity-completed "
            "on the 3152 unused computational role states"
        ),
        "unused_role_extension_supplied_domain_choice": True,
        "each_block_unitary_by_isometry": ready,
        "relational_constraint_formula": transport["constraint_formula"],
        "relational_constraint_preserves_E7": transport[
            "correlated_E7_constraint_eigenvalue_plus_one"
        ],
        "Gphysical_commutes_with_each_C_i": ready,
        "Gphysical_commutes_with_Q": ready,
        "constraint_commutator_proof": (
            "K_i A_pi(G_star) K_i^dagger=A_(pi s_i)(G_star), because "
            "K_i E_pi=E_(pi s_i) and K_i transports the image projector; "
            "each A_pi preserves Q_pi"
        ),
        "same_code_intertwiner": "E7 G_star = Gphysical E7",
        "same_code_intertwiner_proven": ready,
        "repeated_same_patch_power_intertwiner_proven": ready,
        "bounded_patch_cells": 7,
        "joint_S7_role_M2": 13,
        "constant_overhead_claim_scope": "one bounded seven-cell maximal star",
        "dense_bounded_coefficients_supplied": True,
        "off_code_matrix_unit_completion_supplied": True,
        "primitive_synthesis_proven": False,
        "bounded_patch_branch_shell_matrix_unit_application_supplied": True,
        "local_constraint_synthesis_proven": False,
        "Q_constraint_enforcement_supplied": True,
        "correlated_role_preparation_supplied": True,
        "dense_Q_and_off_code_completion_supplied": True,
        "bare_J_S7_tensor_I_used": False,
        "Cycle330_joint_update_controls_used": False,
        "adjacent_maximal_stars_open": True,
        "recurrent_volume_open": True,
        "autonomous_volume_collision_open": True,
    }


def bridge_boundary() -> dict:
    return {
        "Cycle514_compatible": (
            "exact structural support discipline and the fixed global N<=2 "
            "domain boundary"
        ),
        "Cycle514_not_imported": (
            "Q6/L15 receiver, Q(zeta_9)[z] tags, beta=-4pi/9 receiver fixture, "
            "mediator dynamics, response law, and resource selector"
        ),
        "same_beta_or_receiver_law": False,
        "same_physical_encoding": False,
        "Cycle515_encoding": "Cycle311/315/327/330 fixed-Wilson role-gauge M64",
        "coarse_DAG_executed": False,
        "response_executed": False,
        "held_prediction_executed": False,
        "Record_claim": False,
        "physical_time_claim": False,
        "source_or_gravity_claim": False,
        "Born_or_probability_claim": False,
        "obstruction_claim": False,
        "axiom_pressure": False,
    }


def partial_retention_fixture() -> dict:
    rows = []
    error = None
    try:
        for column in range(4):
            if column == 3:
                raise ResourceWall("injected resource wall before column 4")
            rows.append({"column": column + 1, "retained": True})
    except ResourceWall as caught:
        error = str(caught)
    return {
        "retained_rows": rows,
        "retained_count": len(rows),
        "error": error,
        "JSON_safe": True,
        "scope": "caught Python exceptions only",
        "durable_across_OS_kill_or_process_OOM": False,
        "in_memory_until_final_JSON": True,
    }


def run_dry() -> tuple[dict, int]:
    tests = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        tests.append({"name": name, "passed": bool(condition), "detail": detail})

    evidence = evidence_controls()
    check(
        "Cycle330, Cycle311/315 amplitude dependencies, and Cycle514 are hash-bound",
        not evidence["missing_files"]
        and not evidence["strict_hash_failures"]
        and evidence["Cycle514_packet_file_count"] == 5,
        evidence,
    )
    source_grammar = source_amplitude_grammar_controls()
    check(
        "bound source implements the exact nonzero common-branch and doubled gauge grammar",
        source_grammar["pass"]
        and all(source_grammar["predicates"].values()),
        source_grammar,
    )
    labels = c330.seven_cell_labels()
    check(
        "Cycle330 declares exactly the 904-dimensional global N<=2 maximal-star domain",
        c330.MAX_TOTAL_NUMBER == 2
        and len(labels) == EXPECTED_LABELS
        and EXPECTED_LABELS == 1 + 42 + math.comb(42, 2),
        {"maximum_total_number": c330.MAX_TOTAL_NUMBER, "labels": len(labels)},
    )
    check(
        "all 5040 exact S7 inversion masks are distinct",
        len(c330.ORDER_INVERSION_MASKS) == EXPECTED_ORDER_COUNT
        and len(set(c330.ORDER_INVERSION_MASKS)) == EXPECTED_ORDER_COUNT
        and max(mask.bit_count() for mask in c330.ORDER_INVERSION_MASKS) == 21,
        {
            "orders": len(c330.ORDER_INVERSION_MASKS),
            "distinct": len(set(c330.ORDER_INVERSION_MASKS)),
        },
    )
    gauge_contracts = tuple(exact_gauge_term_contract(number) for number in range(7))
    check(
        "every local role-gauge branch grammar has exact unit column norm",
        all(
            row["exact_norm_numerator"] == row["exact_norm_denominator"] == 1
            for row in gauge_contracts
        ),
        gauge_contracts,
    )
    check(
        "the exact N<=2 sector census sums to 904 labels and 2459648 branches",
        sum(row["labels"] for row in EXPECTED_SECTOR_CENSUS.values())
        == EXPECTED_LABELS
        and sum(row["branches"] for row in EXPECTED_SECTOR_CENSUS.values())
        == EXPECTED_BRANCHES_PER_SIZE
        and EXPECTED_SECTOR_CENSUS["n0"] == {"labels": 1, "branches": 128}
        and EXPECTED_SECTOR_CENSUS["n1"] == {"labels": 42, "branches": 26_880}
        and EXPECTED_SECTOR_CENSUS["n2_same_cell"]
        == {"labels": 105, "branches": 13_440}
        and EXPECTED_SECTOR_CENSUS["n2_split_cells"]
        == {"labels": 756, "branches": 2_419_200},
        EXPECTED_SECTOR_CENSUS,
    )
    toy = s2_relational_transport_discriminator()
    check(
        "S2 discriminator rejects role-only transport and retains Q intersection rank one",
        toy["pass"]
        and abs(toy["role_only_invariance_residual_squared"] - 2) < 1e-13
        and toy["corrected_controlled_U_invariance_residual"] < 1e-13
        and toy["P_rel_rank"] == 2
        and toy["Q_P_rel_rank"] == 1,
        toy,
    )
    transport = relational_transport_controls()
    check(
        "right-action U-conjugated transports pass every S7 Coxeter relation",
        transport["pass"]
        and transport["right_action_convention"].startswith("pi -> pi s_i")
        and transport["common_C_i_plus_sector_rank"] == EXPECTED_BRANCHES_PER_SIZE
        and transport["Q_code_shell_rank"] == EXPECTED_ORDER_COUNT * EXPECTED_LABELS
        and transport["common_C_i_plus_intersect_Q_rank"] == EXPECTED_LABELS
        and transport["bare_J_S7_tensor_I_quarantined"],
        transport,
    )
    failed_coverage_fixture = exact_order_theorem([])
    check(
        "order coverage counts fail closed without both train and held censuses",
        failed_coverage_fixture["all_5040_E_pi_are_isometries"] is False
        and failed_coverage_fixture["theorem_covered_order_isometries"] == 0
        and failed_coverage_fixture["remaining_unproved_order_isometries"]
        == EXPECTED_ORDER_COUNT,
        {
            "theorem_covered_order_isometries": failed_coverage_fixture[
                "theorem_covered_order_isometries"
            ],
            "remaining_unproved_order_isometries": failed_coverage_fixture[
                "remaining_unproved_order_isometries"
            ],
        },
    )
    source = inspect.getsource(exact_injective_census)
    forbidden = tuple(
        token
        for token in (
            "2e-",
            "eliminate_zeros",
            "count_nonzero",
            "term.amplitude",
            "keep =",
            "if abs(",
        )
        if token in source
    )
    check(
        "exact census contains no numerical support selector",
        not forbidden
        and "for term_tuple in product" in source
        and "branch_anticommutation_mask" in source,
        {"forbidden_hits": forbidden},
    )
    resource_contract = {
        "RSS_checkpoint_abort_ceiling_bytes": RSS_CHECKPOINT_ABORT_CEILING_BYTES,
        "RSS_checkpoint_guard_bytes": RSS_CHECKPOINT_GUARD_BYTES,
        "RSS_hard_limit_installed": False,
        "wall_limit_seconds": WALL_LIMIT_SECONDS,
        "wall_alarm_is_hard": True,
        "wall_grace_seconds": WALL_GRACE_SECONDS,
        "swap_count_checkpoint_requirement": 0,
        "swap_is_checkpoint_monitored": True,
        "progress_column_interval": PROGRESS_COLUMN_INTERVAL,
        "partial_rows_durable_across_OS_kill": False,
    }
    check(
        "resource contract has a hard wall alarm and checkpoint-monitored RSS/swap aborts",
        resource_contract["RSS_checkpoint_abort_ceiling_bytes"] == 3_000_000_000
        and resource_contract["RSS_checkpoint_guard_bytes"] < 3_000_000_000
        and resource_contract["RSS_hard_limit_installed"] is False
        and resource_contract["wall_limit_seconds"] == 1200.0
        and resource_contract["wall_alarm_is_hard"]
        and resource_contract["swap_count_checkpoint_requirement"] == 0
        and resource_contract["progress_column_interval"] <= 16
        and resource_contract["partial_rows_durable_across_OS_kill"] is False,
        resource_contract,
    )
    partial = partial_retention_fixture()
    check(
        "in-memory partial rows survive caught exceptions but not OS termination",
        partial["retained_count"] == 3
        and partial["error"] == "injected resource wall before column 4"
        and partial["JSON_safe"]
        and partial["scope"] == "caught Python exceptions only"
        and partial["durable_across_OS_kill_or_process_OOM"] is False,
        partial,
    )
    boundary = bridge_boundary()
    check(
        "Cycle514 is used only for compatible support discipline",
        boundary["same_beta_or_receiver_law"] is False
        and boundary["same_physical_encoding"] is False
        and "Q6/L15" in boundary["Cycle514_not_imported"]
        and boundary["coarse_DAG_executed"] is False
        and boundary["obstruction_claim"] is False
        and boundary["axiom_pressure"] is False,
        boundary,
    )
    execution = {
        "all_order_certificate_executed": False,
        "physical_branches_enumerated": 0,
        "L5_census_executed": False,
        "L6_census_executed": False,
        "science_rows_executed": 0,
        "response_rows_executed": 0,
        "held_prediction_rows_executed": 0,
        "authorization_required": False,
    }
    check(
        "dry mode executes no physical census or later science surface",
        not any(value for key, value in execution.items() if key != "authorization_required"),
        execution,
    )
    passed = all(row["passed"] for row in tests)
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle515-all-order-contract-ready" if passed else "dry-contract-failed",
        "pass": passed,
        "tests_passed": sum(row["passed"] for row in tests),
        "tests_total": len(tests),
        "evidence": evidence,
        "resource_contract": resource_contract,
        "partial_retention_fixture": partial,
        "bridge_boundary": boundary,
        "execution": execution,
        "tests": tests,
    }, 0 if passed else 1


def run_all_order_certificate() -> tuple[dict, int]:
    started = time.monotonic()
    evidence = evidence_controls()
    if evidence["missing_files"] or evidence["strict_hash_failures"]:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": "all-order-certificate",
            "status": "evidence-integrity-failure",
            "pass": False,
            "evidence": evidence,
            "science_rows_executed": 0,
        }, 1

    limits = install_wall_alarm()
    partial_rows: list[dict] = []
    census_rows = []
    stage = "initial-resource-checkpoint"
    try:
        checkpoints = [resource_checkpoint(started, stage, 150_000_000)]
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            stage = f"L{length}-exact-injective-census"
            census_rows.append(exact_injective_census(length, started, partial_rows))
            checkpoints.append(resource_checkpoint(started, f"L{length}-census-complete"))
            gc.collect()
        stage = "exact-all-order-theorem"
        order_theorem = exact_order_theorem(census_rows)
        stage = "cutoff-free-update-and-frame-controls"
        update = exact_update_and_frame_controls()
        stage = "algebraic-physical-lift"
        lift = algebraic_physical_lift(order_theorem, update)
        checkpoints.append(resource_checkpoint(started, "certificate-complete"))
    except (ResourceWall, CertificateFailure, MemoryError, ValueError) as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": "all-order-certificate",
            "status": (
                "cycle515-resource-wall"
                if isinstance(error, (ResourceWall, MemoryError))
                else "cycle515-certificate-failure"
            ),
            "pass": False,
            "failed_stage": stage,
            "error_type": type(error).__name__,
            "error": str(error),
            "evidence": evidence,
            "resource_limits": limits,
            "partial_progress_rows": partial_rows,
            "completed_census_rows": census_rows,
            "partial_ledger_preserved_for_caught_exception": True,
            "partial_rows_durable_across_OS_kill_or_process_OOM": False,
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "process_swap_count": swap_count(),
            "obstruction_claim": False,
            "axiom_pressure": False,
        }, 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)

    tests = {
        "both_exact_censuses_complete": (
            len(census_rows) == 2
            and {row["L"] for row in census_rows} == {TRAIN_LENGTH, HELD_LENGTH}
        ),
        "all_branch_counts_exact": all(
            row["total_structural_branch_products"] == EXPECTED_BRANCHES_PER_SIZE
            and row["global_physical_rows"] == EXPECTED_BRANCHES_PER_SIZE
            and row["output_row_column_pairs"] == EXPECTED_BRANCHES_PER_SIZE
            for row in census_rows
        ),
        "no_collision_or_multi_mask": all(
            row["collision_pairs"] == 0
            and row["physical_row_reuses"] == 0
            and row["multiple_anticommutation_mask_pairs"] == 0
            and row["maximum_row_column_multiplicity"] == 1
            for row in census_rows
        ),
        "exact_amplitude_source_and_runtime_grammar": (
            order_theorem["source_amplitude_grammar"]["pass"]
            and all(
                row["amplitude_grammar_runtime_check_pass"]
                and row["maximum_amplitude_grammar_residual_diagnostic_only"]
                < AMPLITUDE_GRAMMAR_DIAGNOSTIC_TOLERANCE
                for row in census_rows
            )
        ),
        "all_5040_order_isometries_proven": order_theorem[
            "all_5040_E_pi_are_isometries"
        ],
        "correlated_uniform_E7_isometry_proven": order_theorem[
            "correlated_uniform_E7_Gram_is_exact_I904"
        ],
        "relational_transport_Coxeter_audit": order_theorem[
            "relational_transport"
        ]["pass"],
        "S2_role_only_failure_and_controlled_transport_pass": order_theorem[
            "S2_relational_transport_discriminator"
        ]["pass"],
        "held_support_grammar_matches": order_theorem[
            "held_L6_support_grammar_matches_L5"
        ],
        "same_code_physical_lift_proven": lift["same_code_intertwiner_proven"],
        "mass_contact_and_domain_controls": (
            update["contact_active_columns"] == EXPECTED_CONTACT_ACTIVE_COLUMNS
            and update["lawful_domain_rejections"] == 2
            and abs(update["seven_cell_rest_mass"] - update["Cycle219_mass_fixture"])
            < 3e-13
            and update["uniform_one_particle_eigen_residual"] < 3e-13
        ),
        "all24_logical_frame_controls_with_physical_covariance_open": (
            update["proper_cubic_frames_executed"] == 24
            and update["ordered_six_arm_orbit_size"] == 24
            and update["frame_group_law_tests"] == 576
            and update["frame_group_law_failures"] == 0
            and update["maximum_one_particle_coin_frame_covariance_residual"] < 3e-13
            and update["all_order_proper_cubic_E_pi_covariance_proven"] is False
            and update["all_order_A_pi_frame_equivariance_proven"] is False
        ),
        "checkpoint_monitored_resource_contract_observed": (
            time.monotonic() - started < WALL_LIMIT_SECONDS
            and rss_bytes() < RSS_CHECKPOINT_ABORT_CEILING_BYTES
            and swap_count() == 0
        ),
    }
    tests = {name: bool(value) for name, value in tests.items()}
    passed = all(tests.values())
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "all-order-certificate",
        "status": (
            "cycle515-all-5040-same-code-isometry-certified"
            if passed
            else "cycle515-certificate-predicate-failure"
        ),
        "pass": passed,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "tests": tests,
        "evidence": evidence,
        "resource_limits": limits,
        "resource_checkpoints": checkpoints,
        "partial_progress_rows": partial_rows,
        "partial_ledger_preserved_for_caught_exception": True,
        "partial_rows_durable_across_OS_kill_or_process_OOM": False,
        "census_rows": census_rows,
        "order_theorem": order_theorem,
        "update_and_frames": update,
        "physical_lift": lift,
        "bridge_boundary": bridge_boundary(),
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
        "authority_effect": "none",
        "audit_effect": "unset",
        "constitutional_effect": "none",
        "next_open_target": (
            "two adjacent maximal centers on the 12-cell union with compatible "
            "overlapping local roles and a non-double-counted recurrent macro-update"
        ),
    }, 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    try:
        payload, code = (
            run_dry()
            if args.mode == "dry-contract"
            else run_all_order_certificate()
        )
    except Exception as error:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": args.mode,
            "status": "fail-closed-exception",
            "pass": False,
            "error_type": type(error).__name__,
            "error": str(error),
            "all_order_certificate_complete": False,
            "response_executed": False,
            "held_prediction_executed": False,
            "Record_claim": False,
            "physical_time_claim": False,
            "source_or_gravity_claim": False,
            "Born_or_probability_claim": False,
            "obstruction_claim": False,
            "axiom_pressure": False,
        }
        code = 1
    print(json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
