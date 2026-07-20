#!/usr/bin/env python3
"""Cycle 513 generic local-block/factor-growth preflight for Route C.

Dry mode is a zero-global-amplitude contract.  It binds the complete packaged
Cycle-512 evidence, reconstructs the local N<=2, Q<=6 collision from generic
matter-matrix/mediator blocks (including every size-four component), and
checks authorization, covariance, inverse, geometry, domain, quarantine, and
resource contracts.

The separately gated factor-growth scout replays the frozen Cycle-512 prefix
without rematerializing its packed joint state.  It retains all nine update-2
structural factors, propagates them through update-3 free matter and emitter
words, proves that a fixed 18-cell shell is exactly equivalent to the full
3,375-cell collision schedule on the declared factor support, and applies the
generic local blocks with exact-zero/support filtering only.  It constructs
no packed joint state and no dense X/Y factor matrices.  Its terminal status
is only ``forward-factor-growth-prefix``: inverse update 3, depth 5, response,
deletions, training, and held surfaces remain open and quarantined.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
import os
from pathlib import Path
import resource
import sys
import time
from typing import Callable, Iterable

import numpy as np
from scipy import sparse
from scipy.linalg import svd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20 as c512


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "factor-growth-scout")

CYCLE512_RUNNER = ROOT / "scripts/physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20.py"
CYCLE512_RAW = ROOT / "outputs/physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20.log"
CYCLE512_RECEIPT = ROOT / "outputs/physical_route_c_q6_factorized_resource_scout_cycle512_receipt_2026_07_20.json"
CYCLE512_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUTE_C_Q6_FACTORIZED_RESOURCE_SCOUT_CYCLE512_NOTE_2026-07-20.md"
STRICT_FILE_HASHES = {
    CYCLE512_RUNNER: "d90525f7c25c92762851ac07b9ea58c28123c378fd0fdea6ce3ab565108834fe",
    CYCLE512_RAW: "203a24590329119b44ce13f2c3c39581f011457cd4db217e62c3f985ea840f67",
    CYCLE512_RECEIPT: "40de95deab66e3d32113d1f91cb14d9a1ac92e96fc7cae27b2ea87c56980b983",
    CYCLE512_NOTE: "f027e124f71450e3d24c9961b74c8445129621c52a1c2ea473a03ab7aef28506",
}
EXPECTED_RECEIPT_SCHEMA = "cycle512-route-c-q6-factorized-resource-scout-receipt-v1"
EXPECTED_RECEIPT_STATUS = "update2-unpruned-packed-numerical-rank9-qualified-depth5-open"

SCOUT_AUTHORIZATION_ENV = c512.SCOUT_AUTHORIZATION_ENV
SCOUT_AUTHORIZATION_TOKEN = c512.SCOUT_AUTHORIZATION_TOKEN
RUNNER_INTEGRITY_ENV = "CYCLE513_ROUTE_C_Q6_FACTOR_GROWTH_RUNNER_SHA256"
ALL_AUTHORIZATION_ENVIRONMENTS = c512.ALL_AUTHORIZATION_ENVIRONMENTS

SIDE = c512.SIDE
CELL_COUNT = c512.CELL_COUNT
RSS_LIMIT_BYTES = c512.RSS_LIMIT_BYTES
RSS_PREALLOC_ABORT_BYTES = c512.RSS_PREALLOC_ABORT_BYTES
WALL_LIMIT_SECONDS = c512.WALL_LIMIT_SECONDS
WALL_GRACE_SECONDS = c512.WALL_GRACE_SECONDS
LOCAL_RECONSTRUCTION_CEILING = 1e-12
LOCAL_INVERSE_CEILING = 1e-12
GRAM_HERMITICITY_CEILING = 1e-10
GRAM_NORM_CEILING = 1e-9
LOCAL_OS_RELATIVE_CUTOFFS = (1e-10, 1e-12, 1e-14)
EXPECTED_LOCAL_OS_RANKS = {"N0": 1, "N1": 12, "N2": 49, "combined_N_le_2": 61}
EXPECTED_COMPONENT_HISTOGRAM = {1: 1930, 2: 384, 4: 24}
EXPECTED_SOURCE_BRANCH_HISTOGRAM = {1: 1930, 2: 768, 4: 96}
EXPECTED_UPDATE3_FACTOR_SUPPORTS = (
    ("II", 46425, 35857, 4096, 4096, 14),
    ("ID", 1800, 1800, 1024, 1024, 12),
    ("IX", 1800, 1800, 1024, 1024, 11),
    ("DI", 1800, 1800, 1024, 1024, 12),
    ("DD", 36, 36, 256, 256, 0),
    ("DX", 36, 36, 256, 256, 0),
    ("XI", 1800, 1800, 1024, 1024, 11),
    ("XD", 36, 36, 256, 256, 0),
    ("XX", 36, 36, 256, 256, 0),
)
EXPECTED_FACTOR_GROWTH_ROWS = (
    ("II", 60, 1612, 300, 361, 43477, 142336),
    ("ID", 24, 264, 0, 25, 1942, 8704),
    ("IX", 22, 220, 0, 23, 1932, 6656),
    ("DI", 24, 264, 0, 25, 1942, 8704),
    ("DD", 0, 0, 0, 1, 36, 256),
    ("DX", 0, 0, 0, 1, 36, 256),
    ("XI", 22, 220, 0, 23, 1932, 6656),
    ("XD", 0, 0, 0, 1, 36, 256),
    ("XX", 0, 0, 0, 1, 36, 256),
)
EXPECTED_TOTAL_FACTOR_COUNT = 461
EXPECTED_TOTAL_MATTER_FACTOR_ENTRIES = 51369
EXPECTED_TOTAL_MEDIATOR_FACTOR_ENTRIES = 174080
EXPECTED_COMPACT_CANDIDATE_CELLS = (14, 12, 11, 12, 0, 0, 11, 0, 0)
EXPECTED_COMPACT_MATTER_PAIR_COUNTS = (91, 11, 0, 11, 0, 0, 0, 0, 0)
EXPECTED_COMPACT_SUPPORT_UPPER_ROWS = (393, 69, 23, 69, 1, 1, 23, 1, 1)
EXPECTED_COMPACT_SUPPORT_UPPER_TOTAL = 581
PRELIMINARY_STORED_KEY_GROUPED_DESCRIPTOR = 453
GRAM_COMPLEX128_BYTES_EACH = EXPECTED_TOTAL_FACTOR_COUNT**2 * np.dtype(np.complex128).itemsize
GRAM_COMPLEX128_BYTES_BOTH = 2 * GRAM_COMPLEX128_BYTES_EACH
X_GRAM_ROW_MULTIPLICITY_WORK_CEILING = (
    EXPECTED_TOTAL_FACTOR_COUNT * EXPECTED_TOTAL_MATTER_FACTOR_ENTRIES
)
Y_GRAM_ROW_MULTIPLICITY_WORK_CEILING = (
    EXPECTED_TOTAL_FACTOR_COUNT * EXPECTED_TOTAL_MEDIATOR_FACTOR_ENTRIES
)
TOTAL_GRAM_ROW_MULTIPLICITY_WORK_CEILING = (
    X_GRAM_ROW_MULTIPLICITY_WORK_CEILING + Y_GRAM_ROW_MULTIPLICITY_WORK_CEILING
)
DIAGNOSTIC_RELATIVE_CUTOFFS = (1e-10, 1e-12, 1e-14)

MatterRay = c512.MatterRay
MediatorRay = c512.MediatorRay
MatterBlock = tuple[int, int]
MediatorBlock = dict[int, dict[int, complex]]
GenericBlocks = dict[MatterBlock, MediatorBlock]
Factor = tuple[MatterRay, MediatorRay, str]


class ResourceWall(RuntimeError):
    """A technical cap, never a physical or mathematical conclusion."""


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
    if rss >= RSS_PREALLOC_ABORT_BYTES:
        raise ResourceWall(f"RSS preallocation guard reached at {label}: {rss}")
    if rss + projected_bytes >= RSS_PREALLOC_ABORT_BYTES:
        raise ResourceWall(
            f"projected allocation guard reached at {label}: rss={rss}, projected={projected_bytes}"
        )
    if swap_count() != 0:
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "estimated_next_allocation_bytes": projected_bytes,
        "allocation_estimate_is_not_measured_RSS": True,
        "process_swap_count": swap_count(),
    }


def exact_zero_filter(ray: dict) -> tuple[dict, int]:
    output = {key: value for key, value in ray.items() if value != 0j}
    return output, len(ray) - len(output)


def evidence_controls() -> dict:
    actual = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    failures = {
        str(path.relative_to(ROOT)): {
            "expected": expected,
            "actual": actual[str(path.relative_to(ROOT))],
        }
        for path, expected in STRICT_FILE_HASHES.items()
        if actual[str(path.relative_to(ROOT))] != expected
    }
    receipt = json.loads(CYCLE512_RECEIPT.read_text(encoding="utf-8"))
    source = receipt.get("source", {})
    execution = receipt.get("execution", {})
    return {
        "strict_file_hashes": actual,
        "strict_hash_failures": failures,
        "receipt_schema": receipt.get("schema"),
        "receipt_status": receipt.get("status"),
        "receipt_pass": receipt.get("pass"),
        "receipt_authority": receipt.get("authority"),
        "receipt_audit": receipt.get("audit"),
        "receipt_source_hashes_match": (
            source.get("runner_sha256") == STRICT_FILE_HASHES[CYCLE512_RUNNER]
            and source.get("raw_transcript_sha256") == STRICT_FILE_HASHES[CYCLE512_RAW]
            and source.get("raw_transcript_exit_code") == 0
        ),
        "receipt_execution": execution,
        "receipt_three_axis_rank9": receipt.get("all_axis_Schmidt", {}).get("pass") is True,
        "receipt_depth5_open": receipt.get("scope", {}).get("completed_unpruned_numerical_updates") == 2,
    }


def frozen_contract_matches() -> bool:
    frozen = c512.c511.authorization_contract()["scout"]
    return (
        frozen["environment"] == SCOUT_AUTHORIZATION_ENV
        and frozen["exact_token"] == SCOUT_AUTHORIZATION_TOKEN
        and frozen["scope"] == "RouteC8 index0 intact L15 middle-beta resource sentinel only"
        and frozen["science_rows"] == 0
        and frozen["response_quarantined"] is True
        and frozen["selector"] is False
        and frozen["refit"] is False
        and frozen["resource_ceiling"]
        == {
            "wall_seconds": int(WALL_LIMIT_SECONDS),
            "RSS_bytes": RSS_LIMIT_BYTES,
            "swap_count": 0,
        }
    )


def resource_authorization_inputs_allowed(
    present: tuple[str, ...],
    values: dict[str, str | None],
    integrity_present: bool,
    integrity_value: str | None,
    runner_sha: str,
    contract_matches: bool,
) -> bool:
    return (
        present == (SCOUT_AUTHORIZATION_ENV,)
        and values.get(SCOUT_AUTHORIZATION_ENV) == SCOUT_AUTHORIZATION_TOKEN
        and integrity_present
        and integrity_value == runner_sha
        and contract_matches
    )


def authorization_decision(mode: str) -> tuple[bool, dict]:
    present = tuple(name for name in ALL_AUTHORIZATION_ENVIRONMENTS if name in os.environ)
    values = {name: os.environ.get(name) for name in present}
    integrity_present = RUNNER_INTEGRITY_ENV in os.environ
    integrity_value = os.environ.get(RUNNER_INTEGRITY_ENV)
    runner_sha = file_sha(Path(__file__))
    contract_matches = frozen_contract_matches()
    base = {
        "mode": mode,
        "present_authorization_variables": present,
        "runner_integrity_variable_present": integrity_present,
        "presence_even_empty_rejected": True,
        "frozen_Cycle511_scout_contract_matches": contract_matches,
    }
    if mode == "dry-contract":
        return not present and not integrity_present, base
    allowed = resource_authorization_inputs_allowed(
        present,
        values,
        integrity_present,
        integrity_value,
        runner_sha,
        contract_matches,
    )
    return allowed, {
        **base,
        "runner_integrity_sha256_match": integrity_value == runner_sha,
        "current_runner_sha256": runner_sha,
        "exact_frozen_Cycle511_scout_token_match": values.get(SCOUT_AUTHORIZATION_ENV)
        == SCOUT_AUTHORIZATION_TOKEN,
        "new_execution_scope_or_token_introduced": False,
        "scope": "RouteC8 index0 intact L15 middle-beta resource sentinel only",
        "implementation_scope": (
            "one hash-bound Cycle513 forward generic-factor-growth technical prefix invocation"
        ),
        "science_rows": 0,
        "response_quarantined": True,
        "held_rows": 0,
        "selector": False,
        "refit": False,
    }


def shell_geometry() -> tuple[tuple[int, int, int], ...]:
    center = c512.c511.c509.ROUTE_C_TRAIN.probe_center
    return tuple(
        sorted(
            {
                tuple(
                    int(center[index] + radius * c512.c511.c210.DIRECTIONS[direction, index])
                    for index in range(3)
                )
                for direction in range(6)
                for radius in (2, 3, 4)
            }
        )
    )


def geometry_contract() -> dict:
    center = c512.c511.c509.ROUTE_C_TRAIN.probe_center
    shell = set(shell_geometry())
    frame_failures = 0
    for frame in c512.c511.c210.proper_cubic_frames():
        moved = {
            tuple(
                int(
                    center[index]
                    + sum(frame[index, j] * (cell[j] - center[j]) for j in range(3))
                )
                for index in range(3)
            )
            for cell in shell
        }
        frame_failures += moved != shell
    return {
        "full_physical_schedule_cell_count": CELL_COUNT,
        "support_equivalent_fixed_shell_cell_count": len(shell),
        "fixed_shell_cells": tuple(sorted(shell)),
        "construction": "six axial rays at radii 2, 3, and 4 from the frozen center",
        "proper_cubic_frame_count": len(c512.c511.c210.proper_cubic_frames()),
        "proper_cubic_frame_failures": frame_failures,
        "physical_selector": False,
        "compiler_optimization_only": True,
        "full_schedule_remains_defining_law": True,
    }


def compact_support_upper_contract() -> dict:
    labels = c512.EXPECTED_UPDATE2_FACTOR_LABELS
    rows = tuple(
        {
            "label": label,
            "candidate_cells_C_j": cells,
            "matter_cooccupied_pairs_P_j": pairs,
            "one_plus_2C_plus_4P": 1 + 2 * cells + 4 * pairs,
        }
        for label, cells, pairs in zip(
            labels,
            EXPECTED_COMPACT_CANDIDATE_CELLS,
            EXPECTED_COMPACT_MATTER_PAIR_COUNTS,
        )
    )
    observed = tuple(row["one_plus_2C_plus_4P"] for row in rows)
    total = sum(observed)
    return {
        "pass": observed == EXPECTED_COMPACT_SUPPORT_UPPER_ROWS
        and total == EXPECTED_COMPACT_SUPPORT_UPPER_TOTAL,
        "rows": rows,
        "total": total,
        "classification": (
            "analytic compact-D/X matter-support-only upper before mediator "
            "two-cell compatibility and exact-zero filtering"
        ),
        "upper_on_arbitrary_factor_decompositions": False,
        "retained_factor_descriptor": False,
        "preliminary_453_grouped_count": PRELIMINARY_STORED_KEY_GROUPED_DESCRIPTOR,
        "preliminary_453_preserved_or_reconciled": False,
        "preliminary_453_used_as_evidence": False,
    }


def structural_axis_terms(angle: float) -> tuple[tuple[tuple[str, str, str], complex], ...]:
    names = ("I", "DF", "XF", "DR", "XR")
    coefficient = {
        "I": 1 + 0j,
        "DF": np.cos(angle) - 1,
        "XF": 1j * np.sin(angle),
        "DR": np.cos(angle) - 1,
        "XR": 1j * np.sin(angle),
    }
    terms = []
    for choices in product(names, repeat=3):
        if sum(choice != "I" for choice in choices) <= 2:
            terms.append((choices, np.prod([coefficient[choice] for choice in choices])))
    return tuple(terms)


def apply_axis_choice(
    matter: int, mediator: int, axis: int, choice: str
) -> tuple[int, int, int] | None:
    if choice == "I":
        return matter, mediator, 1
    forward, reverse = c512.c510.UNORIENTED[axis]
    if choice.endswith("F"):
        old_matter, new_matter = reverse, forward
        old_mediator, new_mediator = 1 + forward, 1 + reverse
    else:
        old_matter, new_matter = forward, reverse
        old_mediator, new_mediator = 1 + reverse, 1 + forward
    matter_hop = c512.c510.fermion_hop(matter, old_matter, new_matter)
    old_bit, new_bit = 1 << old_mediator, 1 << new_mediator
    mediator_allowed = bool(mediator & old_bit) and not bool(mediator & new_bit)
    if matter_hop is None or not mediator_allowed:
        return None
    target_matter, sign = matter_hop
    if choice.startswith("D"):
        return matter, mediator, 1
    return target_matter, mediator ^ old_bit ^ new_bit, sign


def structural_lookup(
    matter: int,
    mediator: int,
    terms: tuple[tuple[tuple[str, str, str], complex], ...],
) -> dict[tuple[int, int], complex]:
    output: dict[tuple[int, int], complex] = defaultdict(complex)
    for choices, coefficient in terms:
        target_matter, target_mediator, sign = matter, mediator, 1
        lawful = True
        for axis, choice in enumerate(choices):
            result = apply_axis_choice(target_matter, target_mediator, axis, choice)
            if result is None:
                lawful = False
                break
            target_matter, target_mediator, local_sign = result
            sign *= local_sign
        if lawful:
            output[(target_matter, target_mediator)] += sign * coefficient
    return {key: value for key, value in output.items() if value != 0j}


def generic_matter_blocks(
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
) -> GenericBlocks:
    blocks: dict[MatterBlock, dict[int, dict[int, complex]]] = defaultdict(
        lambda: defaultdict(dict)
    )
    for matter in range(64):
        if matter.bit_count() > 2:
            continue
        for mediator in range(128):
            if mediator.bit_count() > 6:
                continue
            for target_matter, target_mediator, value in lookup(matter, mediator):
                delta = value - int(
                    target_matter == matter and target_mediator == mediator
                )
                if delta != 0j:
                    blocks[(target_matter, matter)][mediator][target_mediator] = delta
    return {
        key: {source: dict(targets) for source, targets in value.items()}
        for key, value in blocks.items()
    }


def operator_schmidt_row_matrix(
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    matter_masks: tuple[int, ...],
) -> tuple[np.ndarray, tuple[tuple[int, int], ...]]:
    mediator_masks = tuple(mask for mask in range(128) if mask.bit_count() <= 6)
    rows: list[dict[tuple[int, int], complex]] = []
    columns: set[tuple[int, int]] = set()
    for target_matter in matter_masks:
        for source_matter in matter_masks:
            row: dict[tuple[int, int], complex] = {}
            for source_mediator in mediator_masks:
                for target_matter_value, target_mediator, value in lookup(
                    source_matter, source_mediator
                ):
                    if target_matter_value == target_matter and value != 0j:
                        row[(target_mediator, source_mediator)] = value
            rows.append(row)
            columns.update(row)
    ordered_columns = tuple(sorted(columns))
    column_index = {key: index for index, key in enumerate(ordered_columns)}
    matrix = np.zeros((len(rows), len(ordered_columns)), dtype=np.complex128)
    for row_index, row in enumerate(rows):
        for key, value in row.items():
            matrix[row_index, column_index[key]] = value
    return matrix, ordered_columns


def local_block_certificate(angle: float) -> dict:
    lookup, controls = c512.local_collision_lookup(angle)
    terms = structural_axis_terms(angle)
    branch_histogram: Counter[int] = Counter()
    maximum_reconstruction = 0.0
    maximum_inverse = 0.0
    domain_failures = 0
    full_u_blocks: set[MatterBlock] = set()
    full_u_entry_count = 0
    forward_maps: dict[tuple[int, int], dict[tuple[int, int], complex]] = {}
    inverse_terms = structural_axis_terms(-angle)
    for matter in range(64):
        if matter.bit_count() > 2:
            continue
        for mediator in range(128):
            if mediator.bit_count() > 6:
                continue
            expected = {
                (target_matter, target_mediator): value
                for target_matter, target_mediator, value in lookup(matter, mediator)
            }
            for (target_matter, _target_mediator), value in expected.items():
                if value != 0j:
                    full_u_blocks.add((target_matter, matter))
                    full_u_entry_count += 1
            actual = structural_lookup(matter, mediator, terms)
            keys = set(expected) | set(actual)
            maximum_reconstruction = max(
                maximum_reconstruction,
                max((abs(expected.get(key, 0j) - actual.get(key, 0j)) for key in keys), default=0.0),
            )
            branch_histogram[len(expected)] += 1
            domain_failures += any(
                target_matter.bit_count() != matter.bit_count()
                or target_mediator.bit_count() != mediator.bit_count()
                for target_matter, target_mediator in expected
            )
            forward_maps[(matter, mediator)] = actual
            restored: dict[tuple[int, int], complex] = defaultdict(complex)
            for intermediate, value in actual.items():
                for target, inverse_value in structural_lookup(*intermediate, inverse_terms).items():
                    restored[target] += value * inverse_value
            inverse_keys = set(restored) | {(matter, mediator)}
            maximum_inverse = max(
                maximum_inverse,
                max(
                    (
                        abs(restored.get(key, 0j) - int(key == (matter, mediator)))
                        for key in inverse_keys
                    ),
                    default=0.0,
                ),
            )

    adjacency = (c512.c510.collision_generator()[0] != 0).astype(np.int8).tocsr()
    lawful_indices = np.asarray(
        [
            c512.c510.local_index(matter, mediator)
            for matter in range(64)
            if matter.bit_count() <= 2
            for mediator in range(128)
            if mediator.bit_count() <= 6
        ],
        dtype=int,
    )
    component_count, labels = sparse.csgraph.connected_components(
        adjacency[lawful_indices, :][:, lawful_indices], directed=False, return_labels=True
    )
    component_histogram = Counter(Counter(int(value) for value in labels).values())
    blocks = generic_matter_blocks(lookup)

    os_rows = {}
    maximum_driver_residual = 0.0
    for label, masks in (
        ("N0", tuple(mask for mask in range(64) if mask.bit_count() == 0)),
        ("N1", tuple(mask for mask in range(64) if mask.bit_count() == 1)),
        ("N2", tuple(mask for mask in range(64) if mask.bit_count() == 2)),
        ("combined_N_le_2", tuple(mask for mask in range(64) if mask.bit_count() <= 2)),
    ):
        matrix, columns = operator_schmidt_row_matrix(lookup, masks)
        singular_values = svd(matrix, compute_uv=False, lapack_driver="gesdd")
        alternate = svd(matrix, compute_uv=False, lapack_driver="gesvd")
        maximum_driver_residual = max(
            maximum_driver_residual,
            float(np.max(np.abs(singular_values - alternate), initial=0.0)),
        )
        ranks = {
            str(cutoff): int(
                np.count_nonzero(singular_values > cutoff * singular_values[0])
            )
            for cutoff in LOCAL_OS_RELATIVE_CUTOFFS
        }
        maximum_rank = max(ranks.values())
        os_rows[label] = {
            "matter_matrix_unit_rows": matrix.shape[0],
            "nonzero_mediator_matrix_unit_columns": len(columns),
            "operator_Schmidt_ranks_by_relative_cutoff": ranks,
            "smallest_retained_singular_value_at_most_inclusive_cutoff": float(
                singular_values[maximum_rank - 1]
            ),
            "largest_rejected_singular_value": (
                float(singular_values[maximum_rank])
                if maximum_rank < len(singular_values)
                else 0.0
            ),
        }

    generator, entries, axes = c512.c510.collision_generator()
    commutators = [
        float(sparse.linalg.norm(axes[left] @ axes[right] - axes[right] @ axes[left]))
        for left in range(3)
        for right in range(left + 1, 3)
    ]
    k_entry_count = sum(
        len(targets)
        for mediator_block in blocks.values()
        for targets in mediator_block.values()
    )
    passed = (
        len(terms) == 61
        and len(forward_maps) == 2794
        and dict(sorted(component_histogram.items())) == EXPECTED_COMPONENT_HISTOGRAM
        and dict(sorted(branch_histogram.items())) == EXPECTED_SOURCE_BRANCH_HISTOGRAM
        and controls["maximum_component_size"]() == 4
        and len(full_u_blocks) == 64
        and full_u_entry_count == 3850
        and len(blocks) == 60
        and k_entry_count == 1920
        and all(
            all(
                rank == expected
                for rank in os_rows[label][
                    "operator_Schmidt_ranks_by_relative_cutoff"
                ].values()
            )
            for label, expected in EXPECTED_LOCAL_OS_RANKS.items()
        )
        and maximum_reconstruction <= LOCAL_RECONSTRUCTION_CEILING
        and maximum_inverse <= LOCAL_INVERSE_CEILING
        and domain_failures == 0
        and c512.c510.collision_covariance(entries) == 0.0
        and max(commutators, default=0.0) == 0.0
        and maximum_driver_residual <= 1e-12
    )
    return {
        "pass": passed,
        "lawful_state_count": len(forward_maps),
        "lawful_domain": "local matter N<=2 and mediator Q<=6",
        "component_count": int(component_count),
        "component_histogram": dict(sorted(component_histogram.items())),
        "source_branch_histogram": dict(sorted(branch_histogram.items())),
        "size4_components_included": component_histogram[4] == 24,
        "size4_source_states_included": branch_histogram[4] == 96,
        "three_axis_product_structural_terms_after_N2_certificate": len(terms),
        "N2_certificate": "1 + 3*4 + C(3,2)*4^2 = 61; every triple-nonidentity axis term annihilates N<=2",
        "full_U_matter_matrix_block_grid": (64, 64),
        "full_U_nonzero_matter_matrix_blocks_on_lawful_domain": len(full_u_blocks),
        "full_U_nonzero_matrix_entries_on_lawful_domain": full_u_entry_count,
        "K_equals_U_minus_I_nonzero_matter_matrix_blocks": len(blocks),
        "K_equals_U_minus_I_nonzero_matrix_entries": k_entry_count,
        "operator_Schmidt": os_rows,
        "operator_Schmidt_relative_cutoffs": LOCAL_OS_RELATIVE_CUTOFFS,
        "operator_Schmidt_secondary_driver_maximum_residual": maximum_driver_residual,
        "maximum_structural_reconstruction_residual": maximum_reconstruction,
        "maximum_forward_inverse_residual": maximum_inverse,
        "maximum_component_unitarity_residual": controls["maximum_local_unitarity_residual"](),
        "domain_failures": domain_failures,
        "generator_Hermiticity_residual": float(sparse.linalg.norm(generator - generator.getH())),
        "maximum_axis_commutator": max(commutators, default=0.0),
        "all24_collision_covariance_residual": c512.c510.collision_covariance(entries),
        "matrix_unit_factorization_is_local_even_CAR": True,
        "additional_global_parity_service_used_by_this_even_numerical_update": False,
        "physical_parity_or_superselection_compiler_closed": False,
    }


def local_matter_mask(pair: c512.MatterPair, cell: tuple[int, int, int]) -> int:
    mask = 0
    for mode in pair:
        mode_cell, direction = c512.decode_matter_mode(mode)
        if mode_cell == cell:
            mask |= 1 << direction
    return mask


def local_mediator_mask(
    configuration: c512.MediatorConfiguration, cell: tuple[int, int, int]
) -> int:
    mask = 0
    for mode in configuration:
        mode_cell, slot = c512.decode_mediator_mode(mode)
        if mode_cell == cell:
            mask |= 1 << slot
    return mask


def apply_matter_block(
    ray: MatterRay, cell: tuple[int, int, int], target_mask: int, source_mask: int
) -> tuple[MatterRay, int]:
    output: MatterRay = {}
    for pair, amplitude in ray.items():
        if local_matter_mask(pair, cell) != source_mask:
            continue
        values = [mode for mode in pair if c512.decode_matter_mode(mode)[0] != cell]
        values.extend(
            c512.matter_mode(cell, direction)
            for direction in range(6)
            if (target_mask >> direction) & 1
        )
        if len(values) != c512.MATTER_NUMBER or len(set(values)) != c512.MATTER_NUMBER:
            raise RuntimeError("generic matter block left the N2 domain")
        target: c512.MatterPair = tuple(sorted(values))  # type: ignore[assignment]
        c512.add_amplitude(output, target, amplitude)
    return exact_zero_filter(output)


def apply_mediator_block(
    ray: MediatorRay, cell: tuple[int, int, int], block: MediatorBlock
) -> tuple[MediatorRay, int]:
    output: MediatorRay = {}
    for configuration, amplitude in ray.items():
        source_mask = local_mediator_mask(configuration, cell)
        for target_mask, coefficient in block.get(source_mask, {}).items():
            values = [
                mode
                for mode in configuration
                if c512.decode_mediator_mode(mode)[0] != cell
            ]
            values.extend(
                c512.mediator_mode(cell, slot)
                for slot in range(7)
                if (target_mask >> slot) & 1
            )
            target = c512.canonical_mediator(values)
            c512.add_amplitude(output, target, amplitude * coefficient)
    return exact_zero_filter(output)


def support_signature_sets(ray: dict, decoder: Callable[[int], tuple[tuple[int, int, int], int]]) -> dict:
    masks: dict[tuple[int, int, int], set[int]] = defaultdict(set)
    occupied_counts: Counter[tuple[int, int, int]] = Counter()
    for configuration in ray:
        local: dict[tuple[int, int, int], int] = defaultdict(int)
        for mode in configuration:
            cell, slot = decoder(mode)
            local[cell] |= 1 << slot
        for cell, mask in local.items():
            masks[cell].add(mask)
            occupied_counts[cell] += 1
    for cell in tuple(masks):
        if occupied_counts[cell] < len(ray):
            masks[cell].add(0)
    return masks


def geometry_equivalence_audit(
    factors: tuple[Factor, ...],
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    axis: int,
) -> dict:
    touched: set[tuple[int, int, int]] = set()
    omitted_nonidentity_failures = 0
    factor_rows = []
    shell = set(shell_geometry())
    all_cells = tuple(c512.linear_cell(index) for index in range(CELL_COUNT))
    for matter, mediator, label in factors:
        matter_masks = support_signature_sets(matter, c512.decode_matter_mode)
        mediator_masks = support_signature_sets(mediator, c512.decode_mediator_mode)
        factor_touched = set()
        for cell in set(matter_masks) & set(mediator_masks):
            if any(
                lookup(matter_mask, mediator_mask)
                != ((matter_mask, mediator_mask, 1 + 0j),)
                for matter_mask in matter_masks[cell]
                for mediator_mask in mediator_masks[cell]
            ):
                factor_touched.add(cell)
        touched.update(factor_touched)
        matter_cooccupied_pairs = set()
        for pair in matter:
            occupied_cells = {
                c512.decode_matter_mode(mode)[0] for mode in pair
            } & factor_touched
            matter_cooccupied_pairs.update(combinations(sorted(occupied_cells), 2))
        compact_upper = 1 + 2 * len(factor_touched) + 4 * len(
            matter_cooccupied_pairs
        )
        factor_rows.append(
            {
                "label": label,
                "touched_cells": tuple(sorted(factor_touched)),
                "matter_cooccupied_compatible_cell_pair_count": len(
                    matter_cooccupied_pairs
                ),
                "compact_DX_matter_support_upper": compact_upper,
            }
        )
        for cell in all_cells:
            if cell in shell:
                continue
            for matter_mask in matter_masks.get(cell, {0}):
                for mediator_mask in mediator_masks.get(cell, {0}):
                    omitted_nonidentity_failures += lookup(matter_mask, mediator_mask) != (
                        (matter_mask, mediator_mask, 1 + 0j),
                    )
    center = c512.c511.c509.ROUTE_C_TRAIN.probe_center
    expected_touched = shell - {
        tuple(
            int(center[index] + radius * c512.c511.c210.DIRECTIONS[direction, index])
            for index in range(3)
        )
        for direction in range(6)
        if direction // 2 != axis
        for radius in (4,)
    }
    passed = (
        touched == expected_touched
        and len(touched) == 14
        and touched <= shell
        and omitted_nonidentity_failures == 0
        and tuple(len(row["touched_cells"]) for row in factor_rows)
        == EXPECTED_COMPACT_CANDIDATE_CELLS
        and tuple(
            row["matter_cooccupied_compatible_cell_pair_count"]
            for row in factor_rows
        )
        == EXPECTED_COMPACT_MATTER_PAIR_COUNTS
        and tuple(row["compact_DX_matter_support_upper"] for row in factor_rows)
        == EXPECTED_COMPACT_SUPPORT_UPPER_ROWS
    )
    return {
        "pass": passed,
        "axis": axis,
        "full_schedule_cells": CELL_COUNT,
        "fixed_support_equivalent_shell_cells": len(shell),
        "axis_touched_cells": len(touched),
        "axis_touched_cell_list": tuple(sorted(touched)),
        "omitted_cells_per_axis": CELL_COUNT - len(shell),
        "omitted_nonidentity_failures": omitted_nonidentity_failures,
        "expected_axis_touched_matches": touched == expected_touched,
        "factor_rows": tuple(factor_rows),
        "compact_DX_matter_support_upper_total": sum(
            row["compact_DX_matter_support_upper"] for row in factor_rows
        ),
        "compact_DX_matter_support_upper_expected": EXPECTED_COMPACT_SUPPORT_UPPER_TOTAL,
        "compact_DX_count_is_matter_support_only_before_mediator_compatibility": True,
        "compact_DX_count_is_not_an_upper_on_arbitrary_factor_decompositions": True,
        "proof": (
            "For every one of the nine declared pre-collision product-factor supports and "
            "every cell outside the fixed 18-cell shell, K_cell=(U_cell-I) vanishes. "
            "Distinct-cell gates commute and preserve each cell's matter count, hence the "
            "fixed shell product equals the full 3375-cell product on those nine supports."
        ),
        "support_used_as_physical_selector": False,
        "state_dependent_law": False,
    }


def build_update3_factors(
    axis: int,
    coin: np.ndarray,
    angle: float,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
) -> tuple[tuple[Factor, ...], dict]:
    matter0 = c512.initial_matter_ray(axis)
    mediator0 = c512.initial_mediator_ray()
    matter1 = c512.forward_matter_word(matter0, coin)
    mediator1_pre = c512.apply_emitters(mediator0, angle)
    update1_identity = c512.collision_is_identity_on_product(matter1, mediator1_pre, lookup)
    mediator1 = c512.apply_mediator_stream(mediator1_pre)
    matter2 = c512.forward_matter_word(matter1, coin)
    mediator2_pre = c512.apply_emitters(mediator1, angle)
    active = c512.update2_active_site_audit(axis, matter2, mediator2_pre, lookup, angle)
    factors = []
    prefix_rows = []
    update3_rows = []
    for choices in product(("I", "D", "X"), repeat=2):
        matter = matter2
        mediator = mediator2_pre
        for choice, site, local_row in zip(
            choices, c512.FROZEN_UPDATE2_ACTIVE_SITES[axis], active["local_rows"]
        ):
            coefficient = 1 + 0j
            if choice == "D":
                coefficient = local_row["diagonal_coefficient"] - 1
            elif choice == "X":
                coefficient = local_row["exchange_coefficient"]
            matter = c512.apply_matter_factor_term(matter, site, choice, coefficient)
            mediator = c512.apply_mediator_factor_term(mediator, site, choice)
        label = "".join(choices)
        mediator = c512.apply_mediator_stream(mediator)
        prefix_rows.append((label, len(matter), len(mediator)))
        matter3 = c512.forward_matter_word(matter, coin)
        mediator3 = c512.apply_emitters(mediator, angle)
        factors.append((matter3, mediator3, label))
        update3_rows.append(
            (
                label,
                len(matter3),
                sum(value != 0j for value in matter3.values()),
                len(mediator3),
                sum(value != 0j for value in mediator3.values()),
            )
        )
    prefix_supports = tuple((matter, mediator) for _label, matter, mediator in prefix_rows)
    return tuple(factors), {
        "axis": axis,
        "update1_collision_identity": update1_identity,
        "update2_active_audit_pass": active["pass"],
        "update2_factor_labels": tuple(label for label, _matter, _mediator in prefix_rows),
        "update2_factor_supports": prefix_supports,
        "update2_factor_supports_match_Cycle512": prefix_supports
        == c512.EXPECTED_UPDATE2_FACTOR_SUPPORTS,
        "update3_pre_collision_rows_without_pruning": tuple(update3_rows),
        "stored_matter_support_through_update3": (
            len(matter0), len(matter1), len(matter2), len(factors[0][0])
        ),
        "stored_mediator_support_through_update3_for_II": (
            len(mediator0), len(mediator1_pre), len(mediator2_pre), len(factors[0][1])
        ),
    }


def expand_generic_collision(
    factors: tuple[Factor, ...], blocks: GenericBlocks
) -> tuple[tuple[Factor, ...], dict]:
    output: list[Factor] = []
    rows = []
    total_exact_zeros_removed = 0
    for matter_raw, mediator_raw, label in factors:
        matter, removed_matter = exact_zero_filter(matter_raw)
        mediator, removed_mediator = exact_zero_filter(mediator_raw)
        total_exact_zeros_removed += removed_matter + removed_mediator
        singles = []
        same_cell_counts: Counter[tuple[int, int, int]] = Counter()
        for cell in shell_geometry():
            for (target_mask, source_mask), mediator_block in sorted(blocks.items()):
                matter_term, removed = apply_matter_block(
                    matter, cell, target_mask, source_mask
                )
                total_exact_zeros_removed += removed
                if not matter_term:
                    continue
                mediator_term, removed = apply_mediator_block(
                    mediator, cell, mediator_block
                )
                total_exact_zeros_removed += removed
                if not mediator_term:
                    continue
                singles.append(
                    (cell, target_mask, source_mask, mediator_block, matter_term, mediator_term)
                )
                same_cell_counts[cell] += 1

        descendants: list[Factor] = [(matter, mediator, f"{label}:I")]
        descendants.extend(
            (entry[4], entry[5], f"{label}:K1:{entry[0]}:{entry[1]}<-{entry[2]}")
            for entry in singles
        )
        raw_pair_upper = len(singles) * (len(singles) - 1) // 2 - sum(
            count * (count - 1) // 2 for count in same_cell_counts.values()
        )
        nonempty_pairs = 0
        for left_index, left in enumerate(singles):
            for right in singles[left_index + 1 :]:
                if left[0] == right[0]:
                    continue
                matter_term, removed = apply_matter_block(
                    left[4], right[0], right[1], right[2]
                )
                total_exact_zeros_removed += removed
                if not matter_term:
                    continue
                mediator_term, removed = apply_mediator_block(
                    left[5], right[0], right[3]
                )
                total_exact_zeros_removed += removed
                if not mediator_term:
                    continue
                descendants.append(
                    (
                        matter_term,
                        mediator_term,
                        f"{label}:K2:{left[0]}:{right[0]}",
                    )
                )
                nonempty_pairs += 1
        output.extend(descendants)
        rows.append(
            {
                "label": label,
                "nonempty_single_blocks": len(singles),
                "raw_distinct_cell_pair_upper": raw_pair_upper,
                "nonempty_pair_blocks": nonempty_pairs,
                "retained_factor_count": len(descendants),
                "matter_factor_entries": sum(len(row[0]) for row in descendants),
                "mediator_factor_entries": sum(len(row[1]) for row in descendants),
                "three_or_more_distinct_cell_terms_omitted_by_exact_N2_certificate": True,
            }
        )
    observed_rows = tuple(
        (
            row["label"],
            row["nonempty_single_blocks"],
            row["raw_distinct_cell_pair_upper"],
            row["nonempty_pair_blocks"],
            row["retained_factor_count"],
            row["matter_factor_entries"],
            row["mediator_factor_entries"],
        )
        for row in rows
    )
    return tuple(output), {
        "pass": (
            observed_rows == EXPECTED_FACTOR_GROWTH_ROWS
            and len(output) == EXPECTED_TOTAL_FACTOR_COUNT
            and sum(len(row[0]) for row in output) == EXPECTED_TOTAL_MATTER_FACTOR_ENTRIES
            and sum(len(row[1]) for row in output) == EXPECTED_TOTAL_MEDIATOR_FACTOR_ENTRIES
        ),
        "rows": tuple(rows),
        "observed_frozen_rows": observed_rows,
        "retained_factor_count": len(output),
        "retained_factor_count_classification": (
            "exact unmerged nonempty descriptor count for this generic K=U-I "
            "matter-matrix-block decomposition in the represented floating arithmetic"
        ),
        "retained_factor_count_is_minimal_or_canonical": False,
        "compact_DX_matter_support_upper": EXPECTED_COMPACT_SUPPORT_UPPER_TOTAL,
        "compact_DX_upper_and_generic_descriptor_are_same_representation": False,
        "preliminary_453_grouped_count_used_as_evidence": False,
        "global_collision_equality_certificate": (
            "The exhaustive local block certificate proves K=sum_alpha "
            "E_alpha^matter tensor B_alpha^mediator on N<=2,Q<=6. K_cell "
            "preserves local matter count and annihilates n_cell=0, so every "
            "product on three distinct cells annihilates global N=2. The retained "
            "identity, single-cell, and two-cell terms therefore equal the fixed-shell "
            "collision product on each declared pre-collision factor support."
        ),
        "matter_factor_entries": sum(len(row[0]) for row in output),
        "mediator_factor_entries": sum(len(row[1]) for row in output),
        "exact_floating_zero_values_removed": total_exact_zeros_removed,
        "magnitude_threshold_used": False,
        "SVD_truncation_used": False,
        "discarded_nonzero_norm": 0.0,
        "full_joint_cartesian_state_materialized": False,
    }


def sparse_factor_matrix(rays: tuple[dict, ...]) -> tuple[sparse.csc_matrix, int]:
    basis = tuple(sorted(set().union(*(set(ray) for ray in rays))))
    index = {key: position for position, key in enumerate(basis)}
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for column, ray in enumerate(rays):
        for key, value in ray.items():
            rows.append(index[key])
            columns.append(column)
            values.append(value)
    matrix = sparse.coo_matrix(
        (values, (rows, columns)), shape=(len(basis), len(rays)), dtype=np.complex128
    ).tocsc()
    return matrix, len(basis)


def sparse_gram_diagnostics(
    factors: tuple[Factor, ...],
    started: float,
    checkpoints: list[dict],
    axis: int,
) -> dict:
    x, matter_basis = sparse_factor_matrix(tuple(row[0] for row in factors))
    y, mediator_basis = sparse_factor_matrix(tuple(row[1] for row in factors))
    x_row_multiplicities = np.diff(x.tocsr().indptr).astype(np.int64)
    y_row_multiplicities = np.diff(y.tocsr().indptr).astype(np.int64)
    x_row_work = int(x_row_multiplicities @ x_row_multiplicities)
    y_row_work = int(y_row_multiplicities @ y_row_multiplicities)
    total_row_work = x_row_work + y_row_work
    if (
        x_row_work > X_GRAM_ROW_MULTIPLICITY_WORK_CEILING
        or y_row_work > Y_GRAM_ROW_MULTIPLICITY_WORK_CEILING
        or total_row_work > TOTAL_GRAM_ROW_MULTIPLICITY_WORK_CEILING
    ):
        raise ResourceWall(
            f"axis{axis} sparse Gram row-multiplicity work exceeded frozen ceiling"
        )
    checkpoints.append(
        resource_checkpoint(
            started,
            f"axis{axis}-before-sparse-Gram-products",
            GRAM_COMPLEX128_BYTES_BOTH,
        )
    )
    gx = (x.getH() @ x).toarray()
    gy = (y.getH() @ y).toarray()
    hermiticity = max(
        float(np.linalg.norm(gx - gx.conj().T)),
        float(np.linalg.norm(gy - gy.conj().T)),
    )
    norm_squared = np.sum(gx * gy)
    eigen_x = np.linalg.eigvalsh(gx)
    eigen_y = np.linalg.eigvalsh(gy)
    # These counts are diagnostics only.  Gram squaring is not used to certify
    # a retained Schmidt rank and no mode is removed from the factor state.
    gram_counts = {
        str(cutoff): {
            "X_eigenvalues_above_squared_relative_cutoff": int(
                np.count_nonzero(eigen_x > cutoff**2 * max(eigen_x[-1], 0.0))
            ),
            "Y_eigenvalues_above_squared_relative_cutoff": int(
                np.count_nonzero(eigen_y > cutoff**2 * max(eigen_y[-1], 0.0))
            ),
        }
        for cutoff in DIAGNOSTIC_RELATIVE_CUTOFFS
    }
    return {
        "pass": (
            hermiticity <= GRAM_HERMITICITY_CEILING
            and abs(norm_squared.imag) <= GRAM_NORM_CEILING
            and abs(norm_squared.real - 1) <= GRAM_NORM_CEILING
        ),
        "factor_count": len(factors),
        "matter_basis_size": matter_basis,
        "mediator_basis_size": mediator_basis,
        "sparse_X_shape": x.shape,
        "sparse_Y_shape": y.shape,
        "sparse_X_nnz": int(x.nnz),
        "sparse_Y_nnz": int(y.nnz),
        "exact_CSR_row_multiplicity_squared_work": {
            "X": x_row_work,
            "Y": y_row_work,
            "total": total_row_work,
        },
        "frozen_CSR_row_multiplicity_squared_work_ceilings": {
            "X": X_GRAM_ROW_MULTIPLICITY_WORK_CEILING,
            "Y": Y_GRAM_ROW_MULTIPLICITY_WORK_CEILING,
            "total": TOTAL_GRAM_ROW_MULTIPLICITY_WORK_CEILING,
            "derivation": "R*nnz with R=461 retained factor columns",
        },
        "projected_dense_Gram_complex128_bytes_each": GRAM_COMPLEX128_BYTES_EACH,
        "projected_dense_Gram_complex128_bytes_both": GRAM_COMPLEX128_BYTES_BOTH,
        "dense_X_or_Y_constructed": False,
        "packed_joint_constructed": False,
        "Gram_shape": gx.shape,
        "maximum_Gram_Hermiticity_residual": hermiticity,
        "factor_norm_squared": float(norm_squared.real),
        "factor_norm_imaginary_residual": float(abs(norm_squared.imag)),
        "factor_norm_residual": float(abs(norm_squared.real - 1)),
        "Gram_eigenvalue_counts_are_diagnostic_not_rank_certificates": gram_counts,
        "minimum_X_Gram_eigenvalue": float(eigen_x[0]),
        "minimum_Y_Gram_eigenvalue": float(eigen_y[0]),
        "factor_columns_truncated": 0,
        "magnitude_pruning_used": False,
        "discarded_norm": 0.0,
    }


def run_dry() -> tuple[dict, int]:
    tests = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        tests.append({"name": name, "passed": bool(condition), "detail": detail})

    authorized, authorization = authorization_decision("dry-contract")
    if not authorized:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "mode": "dry-contract",
            "status": "authorization-rejected",
            "authorization": authorization,
            "global_amplitude_states_evolved": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
        }, 2

    evidence = evidence_controls()
    check("Cycle512 runner/raw/typed/note hashes are exact", not evidence["strict_hash_failures"], evidence)
    check(
        "typed Cycle512 receipt binds the qualified update2 prefix only",
        evidence["receipt_schema"] == EXPECTED_RECEIPT_SCHEMA
        and evidence["receipt_status"] == EXPECTED_RECEIPT_STATUS
        and evidence["receipt_pass"] is True
        and evidence["receipt_authority"] == AUTHORITY
        and evidence["receipt_audit"] == AUDIT
        and evidence["receipt_source_hashes_match"]
        and evidence["receipt_three_axis_rank9"]
        and evidence["receipt_depth5_open"],
        evidence,
    )
    angle = c512.c511.factor_coordinate_controls()[
        "train_and_matched_size_beta_-4pi_over_9"
    ]["emitter_and_collision_angle"]
    local = local_block_certificate(angle)
    check("generic local blocks reconstruct all 2794 lawful states including size4", local["pass"], local)
    geometry = geometry_contract()
    check(
        "fixed 18-cell compiler shell is invariant under all 24 proper-cubic frames",
        geometry["support_equivalent_fixed_shell_cell_count"] == 18
        and geometry["proper_cubic_frame_failures"] == 0
        and geometry["full_physical_schedule_cell_count"] == 3375,
        geometry,
    )
    compact_upper = compact_support_upper_contract()
    check(
        "compact D/X C_j/P_j ledger is a 581 matter-support-only upper",
        compact_upper["pass"]
        and compact_upper["total"] == 581
        and compact_upper["retained_factor_descriptor"] is False
        and compact_upper["preliminary_453_used_as_evidence"] is False,
        compact_upper,
    )
    check(
        "dry authorization is absent and the frozen Cycle511 token/caps remain exact",
        authorization["present_authorization_variables"] == ()
        and authorization["runner_integrity_variable_present"] is False
        and authorization["frozen_Cycle511_scout_contract_matches"],
        authorization,
    )
    runner_sha = file_sha(Path(__file__))
    auth_cases = {
        "absent": resource_authorization_inputs_allowed((), {}, False, None, runner_sha, True),
        "empty": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,), {SCOUT_AUTHORIZATION_ENV: ""}, True, runner_sha, runner_sha, True
        ),
        "wrong_token": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,), {SCOUT_AUTHORIZATION_ENV: "wrong"}, True, runner_sha, runner_sha, True
        ),
        "missing_integrity": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,), {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN}, False, None, runner_sha, True
        ),
        "wrong_integrity": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,), {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN}, True, "wrong", runner_sha, True
        ),
        "conflict": resource_authorization_inputs_allowed(
            ("CYCLE511_ROUTE_C_TRAIN_AUTHORIZATION", SCOUT_AUTHORIZATION_ENV),
            {"CYCLE511_ROUTE_C_TRAIN_AUTHORIZATION": "anything", SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
        "contract_mismatch": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,), {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN}, True, runner_sha, runner_sha, False
        ),
        "exact": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,), {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN}, True, runner_sha, runner_sha, True
        ),
    }
    check(
        "authorization matrix accepts only exact frozen token plus Cycle513 integrity",
        auth_cases["exact"]
        and not any(value for key, value in auth_cases.items() if key != "exact"),
        auth_cases,
    )
    execution = {
        "large_global_allocations": 0,
        "global_amplitude_states_evolved": 0,
        "factor_growth_scout_executed": False,
        "science_rows_executed": 0,
        "response_rows_executed": 0,
        "held_rows_executed": 0,
        "response_values_emitted": 0,
        "occupation_or_bond_fields_emitted": 0,
        "state_hashes_emitted": 0,
        "deletion_variants_executed": 0,
        "selector": False,
        "refit": False,
    }
    check("dry mode evolves no global amplitude and exposes no science surface", not any(execution.values()), execution)
    resource_contract = {
        "RSS_limit_bytes": RSS_LIMIT_BYTES,
        "preallocation_abort_bytes": RSS_PREALLOC_ABORT_BYTES,
        "wall_limit_seconds": WALL_LIMIT_SECONDS,
        "wall_grace_seconds": WALL_GRACE_SECONDS,
        "swap_count": 0,
        "caps_increased_from_Cycle511": False,
        "dense_joint_forbidden": True,
        "dense_X_Y_forbidden": True,
        "all_axes_sequential_only": True,
    }
    check(
        "resource and quarantine contracts are narrower than the frozen scout ceiling",
        resource_contract["RSS_limit_bytes"] == 3_000_000_000
        and resource_contract["preallocation_abort_bytes"] == 2_700_000_000
        and resource_contract["wall_limit_seconds"] == 1200.0,
        resource_contract,
    )
    passed = all(row["passed"] for row in tests)
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle513-generic-factor-growth-contract-ready" if passed else "dry-contract-failed",
        "pass": passed,
        "tests_passed": sum(row["passed"] for row in tests),
        "tests_total": len(tests),
        "authorization": authorization,
        "evidence": evidence,
        "local_block_certificate": local,
        "geometry_contract": geometry,
        "compact_support_upper_contract": compact_upper,
        "resource_contract": resource_contract,
        "execution": execution,
        "tests": tests,
    }, 0 if passed else 1


def run_factor_growth_scout() -> tuple[dict, int]:
    allowed, authorization = authorization_decision("factor-growth-scout")
    if not allowed:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "mode": "factor-growth-scout",
            "status": "authorization-rejected",
            "authorization": authorization,
            "factor_growth_invocations": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
        }, 2
    started = time.monotonic()
    checkpoints: list[dict] = []
    evidence = evidence_controls()
    if evidence["strict_hash_failures"] or not evidence["receipt_source_hashes_match"]:
        raise RuntimeError("Cycle512 evidence changed after authorization")
    angle = c512.c511.factor_coordinate_controls()[
        "train_and_matched_size_beta_-4pi_over_9"
    ]["emitter_and_collision_angle"]
    local = local_block_certificate(angle)
    if not local["pass"]:
        raise RuntimeError("generic local block certificate failed")
    lookup, _controls = c512.local_collision_lookup(angle)
    blocks = generic_matter_blocks(lookup)
    coin = c512.c511.c509.c219.common_species(c512.MIDDLE_BETA).coin
    checkpoints.append(resource_checkpoint(started, "after-local-certificate"))
    component_rows = []
    completed = True
    wall = None
    try:
        for axis in range(3):
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-start", 400_000_000))
            update3_factors, prefix = build_update3_factors(axis, coin, angle, lookup)
            geometry = geometry_equivalence_audit(update3_factors, lookup, axis)
            observed_update3 = tuple(
                row + (len(geometry["factor_rows"][index]["touched_cells"]),)
                for index, row in enumerate(prefix["update3_pre_collision_rows_without_pruning"])
            )
            prefix_pass = (
                prefix["update1_collision_identity"]
                and prefix["update2_active_audit_pass"]
                and prefix["update2_factor_labels"] == c512.EXPECTED_UPDATE2_FACTOR_LABELS
                and prefix["update2_factor_supports_match_Cycle512"]
                and prefix["stored_matter_support_through_update3"]
                == c512.DECLARED_STORED_MATTER_KEYS_BY_UPDATE[:4]
                and prefix["stored_mediator_support_through_update3_for_II"]
                == c512.DECLARED_UNCOUPLED_MEDIATOR_KEYS_BY_UPDATE[:4]
                and observed_update3 == EXPECTED_UPDATE3_FACTOR_SUPPORTS
                and geometry["compact_DX_matter_support_upper_total"]
                == EXPECTED_COMPACT_SUPPORT_UPPER_TOTAL
            )
            if not prefix_pass or not geometry["pass"]:
                raise RuntimeError(f"axis{axis} frozen prefix or geometry equivalence failed")
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-before-factor-growth", 500_000_000))
            grown, growth = expand_generic_collision(update3_factors, blocks)
            if not growth["pass"]:
                raise RuntimeError(f"axis{axis} generic factor-growth ledger changed")
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-before-sparse-Gram", 900_000_000))
            gram = sparse_gram_diagnostics(grown, started, checkpoints, axis)
            if not gram["pass"]:
                raise RuntimeError(f"axis{axis} sparse Gram diagnostics failed")
            component_rows.append(
                {
                    "axis": axis,
                    "pass": prefix_pass and geometry["pass"] and growth["pass"] and gram["pass"],
                    "Cycle512_prefix_replay": prefix,
                    "update3_observed_support_rows": observed_update3,
                    "full_geometry_equivalence": geometry,
                    "generic_factor_growth": growth,
                    "sparse_factor_Gram": gram,
                }
            )
            del update3_factors, grown
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-complete"))
    except (ResourceWall, MemoryError) as error:
        completed = False
        wall = f"{type(error).__name__}: {error}"
    technical = completed and len(component_rows) == 3 and all(row["pass"] for row in component_rows)
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "factor-growth-scout",
        "status": "forward-factor-growth-prefix" if technical else "fail-closed-partial-factor-growth-ledger",
        "pass": technical,
        "authorization": authorization,
        "evidence": evidence,
        "local_block_certificate": local,
        "geometry_contract": geometry_contract(),
        "component_results": tuple(component_rows),
        "resource": {
            "completed_all_three_axes_sequentially": completed and len(component_rows) == 3,
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "process_swap_count": swap_count(),
            "checkpoints": checkpoints,
            "wall": wall,
            "limits": {
                "RSS_bytes": RSS_LIMIT_BYTES,
                "preallocation_abort_bytes": RSS_PREALLOC_ABORT_BYTES,
                "wall_seconds": WALL_LIMIT_SECONDS,
                "swap_count": 0,
            },
        },
        "execution": {
            "factor_growth_invocations": 1,
            "update3_collision_factor_growth_pre_stream_executed": bool(component_rows),
            "full_update3_word_completed": False,
            "post_collision_update3_mediator_stream_executed": False,
            "joint_species_Schmidt_core_constructed": False,
            "joint_species_Schmidt_rank_computed": False,
            "forward_reverse_collision_cell_order_compared": False,
            "full_inverse_update3_executed": False,
            "state_orbit72_executed": False,
            "depth5_completed": False,
            "science_rows_executed": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "response_values_emitted": 0,
            "occupation_or_bond_fields_emitted": 0,
            "state_hashes_emitted": 0,
            "deletion_variants_executed": 0,
            "selector": False,
            "refit": False,
            "packed_joint_constructed": False,
            "dense_X_or_Y_constructed": False,
            "magnitude_pruning_used": False,
            "SVD_truncation_used": False,
        },
        "open": {
            "post_collision_update3_mediator_stream": True,
            "joint_species_Schmidt_core_and_rank": True,
            "forward_reverse_collision_cell_order": True,
            "full_inverse_update3": True,
            "state_orbit72": True,
            "depth5": True,
            "response": True,
            "train": True,
            "held": True,
            "deletions": True,
            "forward_factor_growth_is_completed_update3_science": False,
            "substrate_obstruction": False,
            "axiom_pressure": False,
        },
    }, 0 if technical else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    try:
        payload, code = (
            run_dry() if args.mode == "dry-contract" else run_factor_growth_scout()
        )
    except Exception as error:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": args.mode,
            "status": "fail-closed-exception",
            "error_type": type(error).__name__,
            "error": str(error),
            "science_rows_executed": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "response_values_emitted": 0,
            "occupation_or_bond_fields_emitted": 0,
            "state_hashes_emitted": 0,
            "deletion_variants_executed": 0,
            "selector": False,
            "refit": False,
            "packed_joint_constructed": False,
            "dense_X_or_Y_constructed": False,
            "post_collision_update3_mediator_stream_executed": False,
            "joint_species_Schmidt_core_constructed": False,
            "joint_species_Schmidt_rank_computed": False,
        }
        code = 1
    print(json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
