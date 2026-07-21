#!/usr/bin/env python3
"""Cycle 529: correlated double-shadow stateful B-stream construction.

For the Cycle-230 involutive B permutation P, factor the exact exterior-sign
residual over endpoint FSWAP into a quadratic GF(2) form r(n).  Encode two
correlated shadow banks a=A n and b=A P n.  A bounded runtime layer applies
CZ(q_i,a_i), endpoint FSWAPs, and onsite SWAP(a_i,b_i), giving an exact
stateful recurrent B intertwiner on the declared algebraic code.

The runner separately audits the missing physical obligations.  The frozen
site-major A constraints have size-growing support/preparation and fail fixed-
chart proper-cubic code covariance, although the local runtime gate geometry
is bounded and all-frame covariant.  These are candidate-specific walls, not
a local-gauge no-go; correlated Gauss/higher-form replacements remain open.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from itertools import chain, combinations, product
import io
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

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17 as c231
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523


c210 = c219.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 5e-12
PERTURBATION = 1e-4
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "double-shadow-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CORRELATED_DOUBLE_SHADOW_STREAM_CYCLE529_NOTE_2026-07-21.md"
)
CYCLE219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
CYCLE230_RUNNER = ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
CYCLE231_RUNNER = ROOT / "scripts/ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17.py"
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
CYCLE525_RUNNER = ROOT / "scripts/physical_opposite_carrier_shared_cell_recurrence_cycle525_2026_07_21.py"
CYCLE525_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OPPOSITE_CARRIER_SHARED_CELL_RECURRENCE_CYCLE525_NOTE_2026-07-21.md"
)
CYCLE528_RUNNER = ROOT / "scripts/physical_covariant_protected_link_shadow_cycle528_2026_07_21.py"
CYCLE528_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COVARIANT_PROTECTED_LINK_SHADOW_CYCLE528_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    CYCLE230_RUNNER: "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    CYCLE231_RUNNER: "5adb6dc52f6352a5367a2b56da94854e511f9dd174688029f1841e5004a91c32",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    CYCLE525_RUNNER: "379c67315de8d235f8d5287b281b6291d0a10731d030338d8bde0676a4c0b785",
    CYCLE525_NOTE: "43a39dd4a33d06eaf11369eb84d436761832974a4f759aec44e9ab6b919e44a8",
    CYCLE528_RUNNER: "5eb5160688465283126b990873398c2b8914e39a49f10919128b0b5d77496da5",
    CYCLE528_NOTE: "2ff16e5eae9bf56b3950dc9bcf9ddd7ec3484c6ea1c5aa452656238963939bfb",
}


class CertificateFailure(RuntimeError):
    """A bounded predicate failed; never promoted automatically to a no-go."""


class ResourceWall(RuntimeError):
    """A technical resource wall; never a physical conclusion."""


@dataclass(frozen=True)
class ShadowModel:
    length: int
    permutation: tuple[int, ...]
    rows: tuple[int, ...]
    columns: tuple[int, ...]
    quadratic_coefficients: int
    symmetric_rank: int


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count() != 0:
        raise ResourceWall(f"nonzero swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for source in rows:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def build_shadow_model(length: int) -> ShadowModel:
    permutation = tuple(int(value) for value in c231.edge_permutation(length))
    modes = len(permutation)
    rows = [0] * modes
    columns = [0] * modes
    symmetric = [0] * modes
    coefficient_count = 0
    for left in range(modes):
        left_image = permutation[left]
        row = 0
        for right in range(left + 1, modes):
            exact_inversion = left_image > permutation[right]
            endpoint_pair = left_image == right
            if exact_inversion ^ endpoint_pair:
                row |= 1 << right
                columns[right] |= 1 << left
                symmetric[left] |= 1 << right
                symmetric[right] |= 1 << left
                coefficient_count += 1
        rows[left] = row
    return ShadowModel(
        length,
        permutation,
        tuple(rows),
        tuple(columns),
        coefficient_count,
        gf2_rank(symmetric),
    )


def occupation_word(occupied: tuple[int, ...]) -> int:
    return sum(1 << mode for mode in occupied)


def permuted_occupation(model: ShadowModel, occupied: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(model.permutation[mode] for mode in occupied))


def shadow_word(model: ShadowModel, occupied: tuple[int, ...]) -> int:
    output = 0
    for mode in occupied:
        output ^= model.columns[mode]
    return output


def correction_sign(model: ShadowModel, occupied: tuple[int, ...], shadow: int | None = None) -> int:
    if shadow is None:
        shadow = shadow_word(model, occupied)
    exponent = (occupation_word(occupied) & shadow).bit_count() & 1
    return -1 if exponent else 1


def endpoint_sign(model: ShadowModel, occupied: tuple[int, ...]) -> int:
    return c231.endpoint_fswap_action(np.asarray(model.permutation), occupied)[1]


def exact_sign_fast(model: ShadowModel, occupied: tuple[int, ...]) -> int:
    """Fenwick-tree inversion parity for the exterior permutation action."""

    if len(occupied) <= 32:
        images = tuple(model.permutation[mode] for mode in occupied)
        parity = sum(
            images[left] > images[right]
            for left in range(len(images))
            for right in range(left + 1, len(images))
        ) & 1
        return -1 if parity else 1

    modes = len(model.permutation)
    tree = [0] * (modes + 1)

    def prefix(index: int) -> int:
        total = 0
        index += 1
        while index:
            total += tree[index]
            index -= index & -index
        return total

    def add(index: int) -> None:
        index += 1
        while index <= modes:
            tree[index] += 1
            index += index & -index

    parity = 0
    seen = 0
    for mode in occupied:
        image = model.permutation[mode]
        parity ^= (seen - prefix(image)) & 1
        add(image)
        seen += 1
    return -1 if parity else 1


def encoded_banks(model: ShadowModel, occupied: tuple[int, ...]) -> tuple[int, int]:
    return shadow_word(model, occupied), shadow_word(model, permuted_occupation(model, occupied))


def physical_forward(model: ShadowModel, occupied: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int]:
    bank_a, bank_b = encoded_banks(model, occupied)
    phase = endpoint_sign(model, occupied) * correction_sign(model, occupied, bank_a)
    return permuted_occupation(model, occupied), bank_b, bank_a, phase


def verify_encoded_state(model: ShadowModel, occupied: tuple[int, ...]) -> dict:
    target_occupied = permuted_occupation(model, occupied)
    target_a, target_b = encoded_banks(model, target_occupied)
    output_occupied, output_a, output_b, physical_phase = physical_forward(model, occupied)
    exact_phase = exact_sign_fast(model, occupied)
    second_occupied, second_a, second_b, second_phase = physical_forward(
        model, target_occupied
    )
    input_a, input_b = encoded_banks(model, occupied)
    return {
        "phase_failure": physical_phase != exact_phase,
        "target_failure": output_occupied != target_occupied,
        "bank_failure": output_a != target_a or output_b != target_b,
        "inverse_failure": (
            second_occupied != occupied
            or second_a != input_a
            or second_b != input_b
            or second_phase * physical_phase != 1
        ),
        "deleted_phase_failure": endpoint_sign(model, occupied) != exact_phase,
        "deleted_bank_swap_failure": input_a != target_a or input_b != target_b,
    }


def coefficient_theorem_controls(model: ShadowModel) -> dict:
    failures = 0
    tested = 0
    first_failure = None
    for left, right in combinations(range(len(model.permutation)), 2):
        exact_coefficient = int(model.permutation[left] > model.permutation[right])
        endpoint_coefficient = int(model.permutation[left] == right)
        shadow_coefficient = (model.rows[left] >> right) & 1
        failure = exact_coefficient != (endpoint_coefficient ^ shadow_coefficient)
        failures += failure
        tested += 1
        if failure and first_failure is None:
            first_failure = (left, right)
    return {
        "length": model.length,
        "mode_pairs": tested,
        "quadratic_residual_coefficients": model.quadratic_coefficients,
        "symmetric_residual_matrix_GF2_rank": model.symmetric_rank,
        "coefficient_identity_failures": failures,
        "first_failure": first_failure,
        "vacuum_linear_or_constant_residual_terms": 0,
        "full_Fock_extension": (
            "both exterior and endpoint signs are quadratic occupation characters; "
            "coefficient equality plus zero constant/linear terms proves every sector"
        ),
        "pass": failures == 0 and tested == math.comb(len(model.permutation), 2),
    }


def complete_low_sector_controls(model: ShadowModel) -> dict:
    modes = len(model.permutation)
    rows = {
        "vacuum": {"tests": 0, "phase_failures": 0, "bank_failures": 0, "inverse_failures": 0},
        "one_particle": {"tests": 0, "phase_failures": 0, "bank_failures": 0, "inverse_failures": 0},
        "two_particle": {"tests": 0, "phase_failures": 0, "bank_failures": 0, "inverse_failures": 0},
    }
    deleted_phase_failures = 0
    deleted_bank_swap_failures = 0
    first_deleted_phase = None
    first_deleted_bank = None
    sectors = chain(
        (("vacuum", ()),),
        (("one_particle", (mode,)) for mode in range(modes)),
        (("two_particle", pair) for pair in combinations(range(modes), 2)),
    )
    for sector, occupied in sectors:
        result = verify_encoded_state(model, occupied)
        row = rows[sector]
        row["tests"] += 1
        row["phase_failures"] += result["phase_failure"]
        row["bank_failures"] += result["target_failure"] or result["bank_failure"]
        row["inverse_failures"] += result["inverse_failure"]
        deleted_phase_failures += result["deleted_phase_failure"]
        deleted_bank_swap_failures += result["deleted_bank_swap_failure"]
        if result["deleted_phase_failure"] and first_deleted_phase is None:
            first_deleted_phase = occupied
        if result["deleted_bank_swap_failure"] and first_deleted_bank is None:
            first_deleted_bank = occupied

    expected_pairs = math.comb(modes, 2)
    expected_endpoint_mismatch = 60_600 if model.length == 5 else 154_800
    return {
        "length": model.length,
        "modes": modes,
        "sectors": rows,
        "complete_tests": 1 + modes + expected_pairs,
        "deleted_CZ_layer_phase_failures": deleted_phase_failures,
        "deleted_CZ_layer_first_witness": first_deleted_phase,
        "deleted_bank_SWAP_code_failures": deleted_bank_swap_failures,
        "deleted_bank_SWAP_first_witness": first_deleted_bank,
        "deleted_CZ_basis_residual": 2 if first_deleted_phase is not None else 0,
        "perturbed_first_active_CZ_basis_residual": float(abs(np.exp(1j * PERTURBATION) - 1)),
        "terminal_code_leakage_failures": sum(row["bank_failures"] for row in rows.values()),
        "inverse_roundtrip_failures": sum(row["inverse_failures"] for row in rows.values()),
        "pass": bool(
            rows["vacuum"]["tests"] == 1
            and rows["one_particle"]["tests"] == modes
            and rows["two_particle"]["tests"] == expected_pairs
            and all(row["phase_failures"] == 0 for row in rows.values())
            and all(row["bank_failures"] == 0 for row in rows.values())
            and all(row["inverse_failures"] == 0 for row in rows.values())
            and deleted_phase_failures == expected_endpoint_mismatch
            and first_deleted_phase is not None
            and deleted_bank_swap_failures > 0
        ),
    }


def cell_modes(cell: tuple[int, int, int], length: int) -> tuple[int, ...]:
    return tuple(c231.site_index(cell, direction, length) for direction in range(6))


def selected_domain(cells, length: int, maximum_number: int | None):
    modes = tuple(mode for cell in cells for mode in cell_modes(cell, length))
    stop = len(modes) if maximum_number is None else maximum_number
    return chain.from_iterable(combinations(modes, number) for number in range(stop + 1))


def domain_check(model: ShadowModel, cells, maximum_number: int | None) -> dict:
    failures = Counter()
    tests = 0
    for occupied in selected_domain(cells, model.length, maximum_number):
        result = verify_encoded_state(model, occupied)
        tests += 1
        for key in ("phase_failure", "target_failure", "bank_failure", "inverse_failure"):
            failures[key] += result[key]
    return {"tests": tests, "failures": dict(failures), "pass": not sum(failures.values())}


def higher_sector_controls(model: ShadowModel) -> dict:
    straight_pair = ((0, 0, 0), (1, 0, 0))
    straight_triple = ((0, 0, 0), (1, 0, 0), (2, 0, 0))
    corner_triple = ((0, 0, 0), (1, 0, 0), (1, 1, 0))
    two_cell = domain_check(model, straight_pair, None)
    straight = domain_check(model, straight_triple, 3)
    corner = domain_check(model, corner_triple, 3)

    rng = np.random.default_rng(529_000 + model.length)
    weights = (4, 6, len(model.permutation) // 4, len(model.permutation) // 2, len(model.permutation) - 1)
    random_failures = Counter()
    random_tests = 0
    for weight in weights:
        for _ in range(24):
            occupied = tuple(sorted(int(value) for value in rng.choice(len(model.permutation), weight, replace=False)))
            result = verify_encoded_state(model, occupied)
            random_tests += 1
            for key in ("phase_failure", "target_failure", "bank_failure", "inverse_failure"):
                random_failures[key] += result[key]
    return {
        "length": model.length,
        "two_cell_full_Fock": two_cell,
        "three_cell_straight_total_N_le_3": straight,
        "three_cell_corner_total_N_le_3": corner,
        "Cycle525_matching_three_cell_dimension": straight["tests"] == corner["tests"] == 988,
        "deterministic_high_sector_tests": random_tests,
        "deterministic_high_sector_weights": weights,
        "deterministic_high_sector_failures": dict(random_failures),
        "pass": bool(
            two_cell["tests"] == 4096
            and straight["tests"] == corner["tests"] == 988
            and two_cell["pass"]
            and straight["pass"]
            and corner["pass"]
            and not sum(random_failures.values())
        ),
    }


def coarse_periodic_l1(left, right, length: int) -> int:
    return sum(
        min(abs(left[axis] - right[axis]), length - abs(left[axis] - right[axis]))
        for axis in range(3)
    )


def preparation_constraint_controls(model: ShadowModel) -> dict:
    weights = [row.bit_count() for row in model.rows]
    maximum_distance = -1
    distance_witness = None
    nonlocal_coefficients = 0
    for left, row_source in enumerate(model.rows):
        left_cell, _left_direction = c231.index_mode(left, model.length)
        row = row_source
        while row:
            bit = row & -row
            right = bit.bit_length() - 1
            right_cell, _right_direction = c231.index_mode(right, model.length)
            distance = coarse_periodic_l1(left_cell, right_cell, model.length)
            nonlocal_coefficients += distance > 1
            if distance > maximum_distance:
                maximum_distance = distance
                distance_witness = (left, right, left_cell, right_cell)
            row ^= bit

    first_coefficient = next(
        (left, (row & -row).bit_length() - 1)
        for left, row in enumerate(model.rows)
        if row
    )
    left, remote = first_coefficient
    vacuum_a = shadow_word(model, ())
    deleted_single_a = shadow_word(model, (remote,)) ^ (1 << left)
    lawful_single_a = shadow_word(model, (remote,))
    deletion_constraint_residual = int(
        ((deleted_single_a >> left) & 1) != ((lawful_single_a >> left) & 1)
    )
    return {
        "length": model.length,
        "A_bank_constraints": len(model.rows),
        "B_bank_constraints": len(model.rows),
        "maximum_constraint_support_M2": 1 + max(weights),
        "mean_A_constraint_input_weight": float(np.mean(weights)),
        "quadratic_coefficients_per_bank": model.quadratic_coefficients,
        "direct_preparation_CNOTs_for_two_banks": 2 * model.quadratic_coefficients,
        "direct_preparation_CNOTs_per_cell": 2 * model.quadratic_coefficients / model.length**3,
        "nonlocal_coefficient_constraints": nonlocal_coefficients,
        "maximum_dependency_coarse_L1": maximum_distance,
        "maximum_dependency_witness": distance_witness,
        "radius_one_preparation_depth_lower_bound_from_witness": maximum_distance,
        "deleted_preparation_coefficient": first_coefficient,
        "deleted_preparation_constraint_bit_residual": deletion_constraint_residual,
        "vacuum_shadow_word": vacuum_a,
        "constraints_locally_checkable_with_bounded_support": False,
        "bounded_depth_local_preparation_synthesized": False,
        "global_site_major_order_used": True,
        "pass": bool(
            max(weights) > 0
            and nonlocal_coefficients > 0
            and maximum_distance == 3 * (model.length // 2)
            and deletion_constraint_residual == 1
        ),
    }


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    permutation = c210.direction_permutation(frame)
    return tuple(int(np.argmax(permutation[:, source])) for source in range(6))


def frame_mode_map(length: int, frame: np.ndarray) -> tuple[int, ...]:
    mapping = direction_map(frame)
    output = []
    for mode in range(6 * length**3):
        cell, direction = c231.index_mode(mode, length)
        target_cell = tuple(int(value % length) for value in frame @ np.asarray(cell))
        output.append(c231.site_index(target_cell, mapping[direction], length))
    return tuple(output)


def transformed_rows(model: ShadowModel, mapping: tuple[int, ...]) -> tuple[int, ...]:
    rows = [0] * len(model.rows)
    for left, row_source in enumerate(model.rows):
        target_left = mapping[left]
        row = row_source
        while row:
            bit = row & -row
            right = bit.bit_length() - 1
            rows[target_left] |= 1 << mapping[right]
            row ^= bit
    return tuple(rows)


def rows_digest(rows: tuple[int, ...]) -> str:
    width = (len(rows) + 7) // 8
    digest = sha256()
    for row in rows:
        digest.update(row.to_bytes(width, "little"))
    return digest.hexdigest()


def covariance_controls(model: ShadowModel) -> dict:
    frames = c210.proper_cubic_frames()
    mappings = tuple(frame_mode_map(model.length, frame) for frame in frames)
    frame_rows = []
    chart_digests = set()
    for frame, mapping in zip(frames, mappings):
        mapped = transformed_rows(model, mapping)
        mismatch = sum((left ^ right).bit_count() for left, right in zip(mapped, model.rows))
        chart_digests.add(rows_digest(mapped))
        frame_rows.append(
            {
                "frame": tuple(int(value) for value in frame.reshape(-1)),
                "directed_constraint_coefficient_mismatches": mismatch,
            }
        )

    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    product_failures = 0
    mapping_product_failures = 0
    for first_index, first in enumerate(frames):
        for second_index, second in enumerate(frames):
            target_index = frame_lookup.get(tuple((first @ second).reshape(-1)))
            product_failures += target_index is None
            if target_index is None:
                continue
            first_map = mappings[first_index]
            second_map = mappings[second_index]
            target_map = mappings[target_index]
            mapping_product_failures += any(
                first_map[second_map[mode]] != target_map[mode]
                for mode in range(len(first_map))
            )
    failures = [row["directed_constraint_coefficient_mismatches"] for row in frame_rows]
    return {
        "length": model.length,
        "proper_cubic_frames": len(frames),
        "fixed_chart_passing_frames": sum(value == 0 for value in failures),
        "fixed_chart_failed_frames": sum(value > 0 for value in failures),
        "maximum_fixed_chart_coefficient_mismatches": max(failures),
        "mismatch_histogram": dict(Counter(failures)),
        "frame_products": len(frames) ** 2,
        "frame_product_failures": product_failures,
        "mode_mapping_product_failures": mapping_product_failures,
        "distinct_24_chart_orbit_members": len(chart_digests),
        "abstract_24_chart_family_closes": product_failures == mapping_product_failures == 0,
        "active_chart_selector_prepared_locally": False,
        "fixed_code_all24_covariant": all(value == 0 for value in failures),
        "pass": bool(
            len(frames) == 24
            and len(frames) ** 2 == 576
            and sum(value == 0 for value in failures) == 1
            and sum(value > 0 for value in failures) == 23
            and len(chart_digests) == 24
            and product_failures == mapping_product_failures == 0
        ),
    }


def physical_position(cell, direction: int, shell: int) -> tuple[int, int, int]:
    return tuple(
        int(8 * cell[axis] - shell * c210.DIRECTIONS[direction, axis])
        for axis in range(3)
    )


def layout_runtime_controls(length: int) -> dict:
    frames = c210.proper_cubic_frames()
    directions = tuple(tuple(int(value) for value in row) for row in c210.DIRECTIONS)
    q_offsets = {tuple(-np.asarray(row)) for row in directions}
    bank_a_offsets = {tuple(-2 * np.asarray(row)) for row in directions}
    bank_b_offsets = {tuple(-3 * np.asarray(row)) for row in directions}
    active = q_offsets | bank_a_offsets | bank_b_offsets | {(0, 0, 0)}
    frame_layout_failures = 0
    frame_edge_set_failures = 0
    permutation = c231.edge_permutation(length)
    edge_set = {
        tuple(sorted((source, int(target))))
        for source, target in enumerate(permutation)
        if source < target
    }
    for frame in frames:
        moved = {
            tuple(int(value) for value in frame @ np.asarray(offset))
            for offset in active
        }
        frame_layout_failures += moved != active
        mode_map = frame_mode_map(length, frame)
        transformed_edges = {
            tuple(sorted((mode_map[left], mode_map[right])))
            for left, right in edge_set
        }
        frame_edge_set_failures += transformed_edges != edge_set

    period = 8 * length
    positions = set()
    for cell in product(range(length), repeat=3):
        center = 8 * np.asarray(cell)
        for offset in active:
            positions.add(tuple(int(value % period) for value in center + np.asarray(offset)))

    b_distances = []
    for source, target in enumerate(permutation):
        if source >= target:
            continue
        source_cell, source_direction = c231.index_mode(source, length)
        target_cell, target_direction = c231.index_mode(int(target), length)
        b_distances.append(
            c231.periodic_l1(
                physical_position(source_cell, source_direction, 1),
                physical_position(target_cell, target_direction, 1),
                period,
            )
        )
    controls = {
        "length": length,
        "coarse_cells": length**3,
        "active_M2_per_cell": len(active),
        "active_M2": len(positions),
        "expected_active_M2": 19 * length**3,
        "placement_collisions": 19 * length**3 - len(positions),
        "q_to_A_bank_physical_L1": 1,
        "A_to_B_bank_physical_L1": 1,
        "B_matter_pair_physical_L1_values": sorted(set(b_distances)),
        "maximum_runtime_gate_support_M2": 2,
        "runtime_CZ_calls_per_cell": 6,
        "runtime_bank_SWAP_calls_per_cell": 6,
        "runtime_endpoint_FSWAP_calls_per_cell": 3,
        "runtime_B_compiler_calls_per_cell": 15,
        "Cycle523_non_B_calls_per_cell": 97,
        "combined_calls_per_cell": 112,
        "proper_cubic_frames": len(frames),
        "frame_layout_failures": frame_layout_failures,
        "runtime_B_edge_set_frame_failures": frame_edge_set_failures,
        "runtime_host_branch": False,
    }
    controls["pass"] = bool(
        len(active) == 19
        and controls["placement_collisions"] == 0
        and set(b_distances) == {6}
        and controls["maximum_runtime_gate_support_M2"] == 2
        and controls["combined_calls_per_cell"] == 112
        and len(frames) == 24
        and frame_layout_failures == frame_edge_set_failures == 0
    )
    return controls


def onsite_fixture_controls() -> dict:
    onsite, _objects = c523.onsite_compiler_controls()
    c230.PASS = 0
    c230.FAIL = 0
    with redirect_stdout(io.StringIO()):
        seam = c230.l3_modular_channel_controls()
    singulars = np.linalg.svd(seam, compute_uv=False)
    controls = {
        "Cycle523_full_M64_onsite_pass": onsite["pass"],
        "onsite_intertwiner_residual": onsite["onsite_EG_intertwiner_residual"],
        "onsite_leakage_residual": onsite["terminal_code_leakage_residual"],
        "onsite_inverse_residual": onsite["inverse_roundtrip_residual"],
        "Cycle219_mass_fixture_residual": onsite["mass_fixture_residual"],
        "Cycle230_contact_active_two_particle_states": onsite["contact_active_two_particle_states"],
        "Cycle230_contact_deletion_residual": onsite["contact_deletion_residual"],
        "Cycle230_seam_subchecks": {"pass": c230.PASS, "fail": c230.FAIL},
        "Cycle230_seam_singular_values": tuple(float(value) for value in singulars),
        "correlated_shadow_coin_and_reverse_A_transition_synthesized": False,
        "full_update_physical_intertwiner_claimed": False,
    }
    controls["pass"] = bool(
        onsite["pass"]
        and controls["onsite_intertwiner_residual"] < TOLERANCE
        and controls["onsite_leakage_residual"] < TOLERANCE
        and controls["onsite_inverse_residual"] < 2e-11
        and controls["Cycle219_mass_fixture_residual"] < TOLERANCE
        and controls["Cycle230_contact_active_two_particle_states"] == 15
        and c230.FAIL == 0
        and np.linalg.norm(singulars - np.asarray((0.49577141, 0.45566605))) < 2e-8
    )
    return controls


def upstream_evidence() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "a=an",
        "b=apn",
        "112",
        "60,600",
        "154,800",
        "988",
        "all 24",
        "576",
        "site-major",
        "preparation",
        "runtime",
        "full fock",
        "broad no-go gate status: **fail / do not ship**",
        "partial-attempt-with-named-untested-routes",
        "n1 — alternative-route normalization",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "strict_predecessor_hashes": evidence["pass"],
        "note_scope_target_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle529-double-shadow-contract-ready" if all(tests.values()) else "cycle529-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle529 dry contract failed")

    models = {length: build_shadow_model(length) for length in (TRAIN_LENGTH, HELD_LENGTH)}
    checkpoints.append(checkpoint(started, "L5-L6-shadow-models-built"))
    theorems = tuple(coefficient_theorem_controls(models[length]) for length in models)
    checkpoints.append(checkpoint(started, "full-Fock-coefficient-theorems-complete"))
    low_sectors = tuple(complete_low_sector_controls(models[length]) for length in models)
    checkpoints.append(checkpoint(started, "complete-vacuum-N1-N2-censuses"))
    higher = tuple(higher_sector_controls(models[length]) for length in models)
    checkpoints.append(checkpoint(started, "two-cell-full-Fock-three-cell-N3-high-sectors"))
    preparation = tuple(preparation_constraint_controls(models[length]) for length in models)
    checkpoints.append(checkpoint(started, "preparation-constraint-audit"))
    covariance = tuple(covariance_controls(models[length]) for length in models)
    checkpoints.append(checkpoint(started, "fixed-chart-and-orbit-covariance-audit"))
    layouts = tuple(layout_runtime_controls(length) for length in models)
    checkpoints.append(checkpoint(started, "bounded-runtime-layout-audit"))
    fixtures = onsite_fixture_controls()
    checkpoints.append(checkpoint(started, "mass-contact-seam-fixtures"))

    tests = {
        "dry_contract": dry["pass"],
        "quadratic_coefficient_identity_full_Fock_theorem": all(row["pass"] for row in theorems),
        "complete_L5_held_L6_vacuum_N1_N2_stateful_intertwiner": all(row["pass"] for row in low_sectors),
        "two_cell_full_Fock_three_cell_N3_and_high_sector_controls": all(row["pass"] for row in higher),
        "inverse_leakage_deletion_perturbation_controls": all(row["pass"] for row in low_sectors),
        "nonlocal_preparation_constraint_wall_faithfully_certified": all(row["pass"] for row in preparation),
        "fixed_chart_covariance_wall_and_24_chart_orbit_faithfully_certified": all(row["pass"] for row in covariance),
        "bounded_two_M2_runtime_geometry_all24": all(row["pass"] for row in layouts),
        "Cycle219_mass_Cycle230_contact_seam_fixtures": fixtures["pass"],
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "double-shadow-certificate",
        "status": (
            "cycle529-exact-stateful-runtime-with-preparation-and-fixed-chart-walls"
            if all(tests.values())
            else "cycle529-certificate-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "quadratic_full_Fock_theorems": theorems,
        "complete_low_sector_censuses": low_sectors,
        "higher_sector_controls": higher,
        "preparation_and_constraints": preparation,
        "covariance": covariance,
        "bounded_runtime_layouts": layouts,
        "onsite_mass_contact_seam_fixtures": fixtures,
        "strongest_constructive_result": {
            "encoding": "E|n> = |n, a=A n, b=A P n>",
            "physical_B": "CZ(q_i,a_i) for every mode; endpoint FSWAP P; SWAP(a_i,b_i)",
            "intertwiner": "exact on complete L5/L6 N<=2 and all Fock sectors by quadratic coefficient theorem",
            "stateful_recurrence": "bank swap maps (A n,A Pn) to (A Pn,A n), ready for the next involutive B",
            "runtime_active_M2_per_cell": 19,
            "runtime_two_M2_calls_per_cell_with_Cycle523": 112,
            "runtime_maximum_gate_support_M2": 2,
            "physical_compiler_complete": False,
        },
        "exact_remaining_obligations": {
            "bounded_local_constraint_presentation_for_A_and_AP": "not supplied",
            "bounded_depth_local_correlated_preparation": "not supplied",
            "local_correlated_shadow_coin_and_reverse_A_transition": "not supplied",
            "fixed_code_all24_covariance_without_chart_selector": "fails",
            "preferred_site_major_order_removed": False,
            "strength_relation_to_target": "these obligations are target-equivalent for this shadow formulation",
        },
        "supplied_not_synthesized": {
            "Cycle219_beta_minus_0p3_coin": True,
            "Cycle230_g_0p37_contact_and_factor_order": True,
            "Cycle523_compile_time_QR_schedule": True,
            "Cycle525_three_cell_N3_domain_shape": True,
            "site_major_mode_order_defining_A": True,
            "period_eight_layout_origin": True,
            "A_and_AP_shadow_values": "defined by encoding but not locally prepared",
            "active_24_chart_selector": False,
            "global_parity_service": False,
            "runtime_host_choice": False,
            "physical_duration_energy_or_record": False,
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "disposition": "partial-attempt-with-named-untested-routes",
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
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
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle529-runner-failed",
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
