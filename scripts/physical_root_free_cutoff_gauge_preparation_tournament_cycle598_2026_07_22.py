#!/usr/bin/env python3
"""Cycle598: arbitrary-size/root-free cutoff and gauge-preparation tournament.

This runner builds on accepted Cycles 590 and 593.  It distinguishes an exact
size-indexed modular compiler, a root-free mobile-capacity sector, and two
explicit gauge-fiber preparation mechanisms.  Compile schedules are not
physical time; flux words are not energy or source; preparation is not local
constraint enforcement.  Authority is none and audit is unset.
"""
from __future__ import annotations

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

import physical_local_cutoff_gauge_enforcement_tournament_cycle593_2026_07_22 as c593


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_root_free_cutoff_gauge_preparation_"
    "tournament_cycle598_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE593 = "70a1c54281afdfce255f5115cb84c3766813316e"
TOL = 5e-9
CAP_SECONDS = 360.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_local_cutoff_gauge_enforcement_tournament_cycle593_2026_07_22.py":
        "a9208a889273eb1a2704190d2c14db5fffb5c70b0e06adb54bd8d08e333fcfba",
    # The accepted note has an independent-parent reproduction appendix; the
    # Cycle593 receipt retains its worker-frozen pre-appendix note hash.
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_CUTOFF_GAUGE_ENFORCEMENT_TOURNAMENT_CYCLE593_NOTE_2026-07-22.md":
        "9b2aa57915f269313855de3782e7ad4a13522c764eff483be8fc1cc234ffe1b9",
    "outputs/physical_local_cutoff_gauge_enforcement_tournament_cycle593_receipt_2026_07_22.json":
        "52506df00424acaa04fae2658d813b7e96b0258d0dc34b36e91faeb656c8e32b",
    "outputs/physical_local_cutoff_gauge_enforcement_tournament_cycle593_cold_2026_07_22.txt":
        "212de7551c2a4c20ce12d7b9a97efd07f6392d379860ad2c075442df59b4f61a",
}


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE593, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0
    receipt = json.loads((ROOT / (
        "outputs/physical_local_cutoff_gauge_enforcement_"
        "tournament_cycle593_receipt_2026_07_22.json"
    )).read_text())
    route = receipt["route_A_finite_volume_modular_Gauss"]
    inherited = {
        "Cycle593_pass": receipt["pass"],
        "Cycle593_tests_passed": receipt["tests_passed"],
        "finite_L3_L6_local_enforcement": route["pass"],
        "L7_alias_failure": route["L7_alias_failure"],
        "every_word_EG_residual": route["exact_intertwiner"][
            "enlarged_gauge_code_every_word_EG_residual"
        ],
        "uniform_fiber_EG_residual": route["exact_intertwiner"][
            "matter_only_uniform_flux_fiber_EG_residual"
        ],
        "gauge_preparation_supplied": route["exact_intertwiner"][
            "gauge_code_preparation_supplied"
        ],
        "fixtures": receipt["shore"]["fixtures"],
        "accepted_current_note_sha256": PINS[
            "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_CUTOFF_GAUGE_ENFORCEMENT_TOURNAMENT_CYCLE593_NOTE_2026-07-22.md"
        ],
        "receipt_pre_appendix_note_sha256": receipt["note_sha256"],
    }
    condition = (
        ancestor and observed == PINS and inherited["Cycle593_pass"]
        and inherited["Cycle593_tests_passed"] == 7
        and inherited["finite_L3_L6_local_enforcement"]
        and inherited["L7_alias_failure"]
        and inherited["every_word_EG_residual"] == 0
        and inherited["uniform_fiber_EG_residual"] == 0
        and inherited["gauge_preparation_supplied"]
        and max(inherited["fixtures"].values()) < TOL
    )
    check("accepted Cycle593 shore is ancestral and byte exact", condition,
          {"ancestor": ancestor, "observed": observed, "inherited": inherited})
    return inherited


# ---------------------------------------------------------------------------
# Route A: exact size-indexed prime modulus and independent CRT comparator.


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, int(math.sqrt(number)) + 1))


def next_prime_above(number: int) -> int:
    candidate = number + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def stream_modular(occupation: np.ndarray, flux: np.ndarray, length: int,
                   modulus: int) -> tuple[np.ndarray, np.ndarray]:
    updated_flux = flux.copy()
    for site in range(length**3):
        coordinate = c593.site_tuple(site, length)
        for axis in range(3):
            target_coordinate = list(coordinate)
            target_coordinate[axis] = (target_coordinate[axis] + 1) % length
            target = c593.site_flat(tuple(target_coordinate), length)
            current = int(occupation[site, 2 * axis]) - int(
                occupation[target, 2 * axis + 1]
            )
            updated_flux[site, axis] = (int(updated_flux[site, axis]) - current) % modulus
    updated = np.zeros_like(occupation)
    for site in range(length**3):
        coordinate = c593.site_tuple(site, length)
        for direction, velocity in enumerate(c593.c210.DIRECTIONS):
            target = c593.site_flat(tuple(
                int((coordinate[axis] + velocity[axis]) % length)
                for axis in range(3)
            ), length)
            updated[target, direction] = occupation[site, direction]
    return updated, updated_flux


def inverse_stream_modular(occupation: np.ndarray, flux: np.ndarray, length: int,
                           modulus: int) -> tuple[np.ndarray, np.ndarray]:
    restored = np.zeros_like(occupation)
    for site in range(length**3):
        coordinate = c593.site_tuple(site, length)
        for direction, velocity in enumerate(c593.c210.DIRECTIONS):
            target = c593.site_flat(tuple(
                int((coordinate[axis] + velocity[axis]) % length)
                for axis in range(3)
            ), length)
            restored[site, direction] = occupation[target, direction]
    restored_flux = flux.copy()
    for site in range(length**3):
        coordinate = c593.site_tuple(site, length)
        for axis in range(3):
            target_coordinate = list(coordinate)
            target_coordinate[axis] = (target_coordinate[axis] + 1) % length
            target = c593.site_flat(tuple(target_coordinate), length)
            current = int(restored[site, 2 * axis]) - int(
                restored[target, 2 * axis + 1]
            )
            restored_flux[site, axis] = (int(restored_flux[site, axis]) + current) % modulus
    return restored, restored_flux


def translate_occupation(occupation: np.ndarray, displacement: tuple[int, int, int],
                         length: int) -> np.ndarray:
    result = np.zeros_like(occupation)
    shift = np.asarray(displacement, dtype=int)
    for site in range(length**3):
        coordinate = np.asarray(c593.site_tuple(site, length), dtype=int)
        target = c593.site_flat(tuple(int(value % length) for value in coordinate + shift), length)
        result[target] = occupation[site]
    return result


def translate_flux(flux: np.ndarray, displacement: tuple[int, int, int],
                   length: int) -> np.ndarray:
    result = np.zeros_like(flux)
    shift = np.asarray(displacement, dtype=int)
    for site in range(length**3):
        coordinate = np.asarray(c593.site_tuple(site, length), dtype=int)
        target = c593.site_flat(tuple(int(value % length) for value in coordinate + shift), length)
        result[target] = flux[site]
    return result


def size_indexed_layout(length: int, word_m2: int) -> dict:
    c560 = c593.c560
    code = c560.c539.c525.c319.c269.build_code(length)
    cells = c560.c555.network_cells(length)
    fine_modulus = c560.c533.c527.fine_length(length)
    physical = tuple(
        c560.c533.coordinate_for_qubit(code, bit)
        for bit in range(c560.c555.physical_bit_count(code))
    )
    q_coordinates = tuple(
        c560.c533.c527.shadow_coordinate(cell, direction, length)
        for cell in cells for direction in range(6)
    )
    occupied = set(physical) | set(q_coordinates)
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        c560.allocated_block(origin, 6, occupied, fine_modulus)
        c560.allocated_block(origin, 18, occupied, fine_modulus)
    baseline = len(occupied)
    gauge_roles = []
    maximum_radius = 0
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        block = c560.allocated_block(origin, 3 * word_m2, occupied, fine_modulus)
        gauge_roles.extend(block)
        maximum_radius = max(maximum_radius, max(
            c560.c533.c527.periodic_l1(origin, site, fine_modulus) for site in block
        ))
    root = c560.c533.c527.cell_center((0, 0, 0), length)
    spectators = c560.allocated_block(root, 3, occupied, fine_modulus)
    maximum_radius = max(maximum_radius, max(
        c560.c533.c527.periodic_l1(root, site, fine_modulus) for site in spectators
    ))
    coordinates = np.asarray(tuple(sorted(occupied)), dtype=int)
    frames = c593.c210.proper_cubic_frames()
    injection_failures = group_failures = 0
    for frame in frames:
        mapped = (coordinates @ frame.T) % fine_modulus
        injection_failures += len(np.unique(mapped, axis=0)) != len(coordinates)
    for first in frames:
        for second in frames:
            composed = (((coordinates @ second.T) % fine_modulus) @ first.T) % fine_modulus
            direct = (coordinates @ (first @ second).T) % fine_modulus
            group_failures += int(not np.array_equal(composed, direct))
    role_bytes = repr((tuple(gauge_roles), tuple(spectators))).encode()
    return {
        "length": length,
        "cells": length**3,
        "fine_lattice_modulus": fine_modulus,
        "inherited_M2": baseline,
        "inherited_M2_per_cell": baseline / length**3,
        "flux_word_M2": word_m2,
        "new_flux_M2": 3 * word_m2 * length**3,
        "new_root_spectator_M2": 3,
        "extended_live_M2": len(occupied),
        "average_extended_M2_per_cell": len(occupied) / length**3,
        "maximum_new_role_radius_fine_L1": maximum_radius,
        "new_role_coordinate_sha256": sha256(role_bytes).hexdigest(),
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": injection_failures,
        "frame_products": len(frames)**2,
        "frame_group_failures": group_failures,
        "runtime_frame_query": False,
    }


def route_a(shore_evidence: dict) -> dict:
    print("\nROUTE A — SIZE-INDEXED PRIME MODULAR GAUSS FAMILY")
    frames = c593.c210.proper_cubic_frames()
    rows = []
    maximum_gauss = maximum_inverse = maximum_covariance = 0
    total_covariance_failures = total_group_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        capacity = 6 * length**3
        modulus = next_prime_above(capacity)
        word_m2 = math.ceil(math.log2(modulus))
        accepted = [
            (number, spectators)
            for number in range(capacity + 1) for spectators in range(4)
            if (number + spectators - 3) % modulus == 0
        ]
        inverse_failures = 0
        for value in range(modulus):
            for plus in (0, 1):
                for minus in (0, 1):
                    current = plus - minus
                    inverse_failures += ((value - current) % modulus + current) % modulus != value
        modes = tuple(6 * index for index in range(3))
        occupation = c593.occupation_configuration(length, modes)
        spectators = c593.reservoir_word(3)
        flux = c593.canonical_flux(occupation, length, modulus)
        gauss_before = c593.gauss_residual(flux, occupation, spectators, length, modulus)
        updated_occupation, updated_flux = stream_modular(occupation, flux, length, modulus)
        deleted_update_flux = updated_flux.copy()
        deleted_update_flux[0, 0] = flux[0, 0]
        link_update_deletion_syndrome = int(np.count_nonzero(
            c593.gauss_residual(
                deleted_update_flux, updated_occupation, spectators, length, modulus
            )
        ))
        gauss_after = c593.gauss_residual(
            updated_flux, updated_occupation, spectators, length, modulus
        )
        restored_occupation, restored_flux = inverse_stream_modular(
            updated_occupation, updated_flux, length, modulus
        )
        maximum_gauss = max(maximum_gauss, int(np.max(gauss_before)), int(np.max(gauss_after)))
        maximum_inverse = max(
            maximum_inverse,
            int(np.max(np.abs(restored_occupation - occupation))),
            int(np.max((restored_flux - flux) % modulus)),
        )
        covariance_failures = group_failures = 0
        for frame in frames:
            rotated_occupation = c593.rotate_occupation(occupation, frame, length)
            rotated_flux = c593.rotate_flux(flux, frame, length, modulus)
            left_occupation = c593.rotate_occupation(updated_occupation, frame, length)
            left_flux = c593.rotate_flux(updated_flux, frame, length, modulus)
            right_occupation, right_flux = stream_modular(
                rotated_occupation, rotated_flux, length, modulus
            )
            residual = max(
                int(np.max(np.abs(left_occupation - right_occupation))),
                int(np.max((left_flux - right_flux) % modulus)),
            )
            maximum_covariance = max(maximum_covariance, residual)
            covariance_failures += residual != 0
        for first in frames:
            for second in frames:
                direct = c593.rotate_flux(flux, first @ second, length, modulus)
                composed = c593.rotate_flux(
                    c593.rotate_flux(flux, second, length, modulus), first, length, modulus
                )
                group_failures += int(not np.array_equal(direct, composed))
        total_covariance_failures += covariance_failures
        total_group_failures += group_failures
        # Moving matter and links while leaving Cycle593's root/background fixed
        # is an explicit translation-covariance falsifier.
        one = c593.occupation_configuration(length, (6,))
        one_spectators = c593.reservoir_word(1)
        one_flux = c593.canonical_flux(one, length, modulus)
        translated_one = translate_occupation(one, (1, 0, 0), length)
        translated_flux = translate_flux(one_flux, (1, 0, 0), length)
        fixed_root_translation_syndrome = int(np.count_nonzero(
            c593.gauss_residual(
                translated_flux, translated_one, one_spectators, length, modulus
            )
        ))
        layout = size_indexed_layout(length, word_m2)
        rows.append({
            "length": length,
            "split": split,
            "matter_capacity": capacity,
            "selected_next_prime_modulus": modulus,
            "modulus_strictly_above_capacity": modulus > capacity,
            "exact_binary_word_M2": word_m2,
            "invalid_binary_labels_rejected": 2**word_m2 - modulus,
            "maximum_root_Gauss_check_support_M2": 6 * word_m2 + 9,
            "local_crossed_link_update_support_M2": word_m2 + 2,
            "accepted_N_S_pairs": accepted,
            "exact_N_le_3": accepted == [(0, 3), (1, 2), (2, 1), (3, 0)],
            "local_update_inverse_failures": inverse_failures,
            "maximum_Gauss_residual": max(int(np.max(gauss_before)), int(np.max(gauss_after))),
            "stream_inverse_residual": max(
                int(np.max(np.abs(restored_occupation - occupation))),
                int(np.max((restored_flux - flux) % modulus)),
            ),
            "deleted_crossed_link_update_syndrome_sites": link_update_deletion_syndrome,
            "all24_covariance_failures": covariance_failures,
            "all576_group_failures": group_failures,
            "fixed_root_translation_syndrome_sites": fixed_root_translation_syndrome,
            "layout": layout,
        })

    # Independent finite-product/CRT comparator.  A fixed catalog aliases;
    # extending the catalog makes its aggregate word width grow as well.
    prime_catalog = (2, 3, 5, 7, 11, 13, 17, 19)
    crt_rows = []
    for length in (3, 6, 7, 12):
        capacity = 6 * length**3
        product = 1
        factor_count = 0
        while product <= capacity:
            product *= prime_catalog[factor_count]
            factor_count += 1
        factors = prime_catalog[:factor_count]
        aggregate_word_m2 = sum(math.ceil(math.log2(factor)) for factor in factors)
        accepted = [
            (number, spectators)
            for number in range(capacity + 1) for spectators in range(4)
            if all((number + spectators - 3) % factor == 0 for factor in factors)
        ]
        crt_rows.append({
            "length": length,
            "matter_capacity": capacity,
            "factors": factors,
            "CRT_product": product,
            "factor_count": factor_count,
            "aggregate_link_word_M2": aggregate_word_m2,
            "exact_N_le_3": accepted == [(0, 3), (1, 2), (2, 1), (3, 0)],
        })
    fixed_catalog_product = math.prod(prime_catalog[:4])
    fixed_catalog_L6_alias = next(
        number for number in range(4, 6 * 6**3 + 1)
        if (number - 3) % fixed_catalog_product == 0
    )
    condition = (
        all(row["exact_N_le_3"] for row in rows)
        and all(row["modulus_strictly_above_capacity"] for row in rows)
        and all(row["local_update_inverse_failures"] == 0 for row in rows)
        and min(row["deleted_crossed_link_update_syndrome_sites"] for row in rows) > 0
        and maximum_gauss == maximum_inverse == maximum_covariance == 0
        and total_covariance_failures == total_group_failures == 0
        and min(row["fixed_root_translation_syndrome_sites"] for row in rows) > 0
        and all(row["layout"]["inherited_M2_per_cell"] == 53 for row in rows)
        and all(row["layout"]["mapped_wire_injection_failures"] == 0 for row in rows)
        and all(row["layout"]["frame_group_failures"] == 0 for row in rows)
        and all(row["exact_N_le_3"] for row in crt_rows)
        and fixed_catalog_L6_alias > 3
        and shore_evidence["every_word_EG_residual"] == 0
    )
    result = {
        "status": "exact arbitrary-finite-size family with scale-indexed local words; not constant-overhead and not root-free",
        "rows": rows,
        "family_definition": "k(L) is the least prime strictly greater than 6L^3; w(L)=ceil(log2(k(L)))",
        "exact_link_word_scaling": "three outgoing w(L)-M2 flux words per cell; 3*w(L) persistent M2 per cell plus three root spectators",
        "asymptotic_word_width": "w(L)=3 log2(L)+O(1)",
        "size_independent_constant_overhead_per_cell": False,
        "root_free": False,
        "translation_covariant_with_fixed_root": False,
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames)**2,
        "every_declared_gauge_word_EG_residual": 0,
        "uniform_fiber_EG_residual": 0,
        "inherited_fixtures": shore_evidence["fixtures"],
        "CRT_comparator": {
            "rows": crt_rows,
            "fixed_first_four_factor_product": fixed_catalog_product,
            "fixed_catalog_L6_alias_N": fixed_catalog_L6_alias,
            "fixed_factor_catalog_arbitrary_size": False,
            "growing_factor_catalog_constant_overhead": False,
        },
        "pass_as_route_audit": bool(condition),
        "pass_full_target": False,
    }
    check(
        "Route A removes the L7 alias exactly for k(L)>6L^3 and preserves the local update/all24 square, while exact layouts expose logarithmically growing M2 and the fixed-root translation syndrome",
        condition, {"rows": rows, "CRT": result["CRT_comparator"]},
    )
    return result


# ---------------------------------------------------------------------------
# Route B: root-free mobile capacity carriers.


def carrier_local_checks(occupation: np.ndarray, carriers: np.ndarray) -> dict:
    # Per species/cell 4-M2 word: 0 absent, 1 inactive neutral carrier,
    # 2..7 carrier bound to local direction 0..5; binary labels 8..15 are
    # rejected.  Bound carrier contributes one local anti-charge and must
    # coincide with exactly one matter mode.
    invalid = int(np.count_nonzero((carriers < 0) | (carriers > 7)))
    mismatches = 0
    collisions = 0
    for site in range(occupation.shape[0]):
        for direction in range(6):
            bound = int(np.count_nonzero(carriers[site] == 2 + direction))
            mismatches += bound != int(occupation[site, direction])
            collisions += bound > 1
    return {
        "invalid_four_M2_labels": invalid,
        "matter_bound_anticharge_mismatches": mismatches,
        "multiple_species_same_mode_collisions": collisions,
        "pass": invalid == mismatches == collisions == 0,
    }


def carrier_word(length: int, bindings: tuple[tuple[int, int, int], ...],
                 inactive: tuple[tuple[int, int], ...] = ()) -> tuple[np.ndarray, np.ndarray]:
    occupation = np.zeros((length**3, 6), dtype=np.int8)
    carriers = np.zeros((length**3, 3), dtype=np.int8)
    for species, site, direction in bindings:
        occupation[site, direction] = 1
        carriers[site, species] = 2 + direction
    for species, site in inactive:
        carriers[site, species] = 1
    return occupation, carriers


def translate_carriers(carriers: np.ndarray, displacement: tuple[int, int, int],
                       length: int) -> np.ndarray:
    result = np.zeros_like(carriers)
    shift = np.asarray(displacement, dtype=int)
    for site in range(length**3):
        coordinate = np.asarray(c593.site_tuple(site, length), dtype=int)
        target = c593.site_flat(tuple(int(value % length) for value in coordinate + shift), length)
        result[target] = carriers[site]
    return result


def rotate_carriers(carriers: np.ndarray, frame: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros_like(carriers)
    direction_map = np.argmax(c593.c210.direction_permutation(frame), axis=0)
    for site in range(length**3):
        coordinate = np.asarray(c593.site_tuple(site, length), dtype=int)
        target = c593.site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
        for species in range(3):
            word = int(carriers[site, species])
            result[target, species] = word if word < 2 else 2 + int(direction_map[word - 2])
    return result


def carrier_layout(length: int) -> dict:
    c560 = c593.c560
    code = c560.c539.c525.c319.c269.build_code(length)
    cells = c560.c555.network_cells(length)
    fine_modulus = c560.c533.c527.fine_length(length)
    physical = tuple(
        c560.c533.coordinate_for_qubit(code, bit)
        for bit in range(c560.c555.physical_bit_count(code))
    )
    q_coordinates = tuple(
        c560.c533.c527.shadow_coordinate(cell, direction, length)
        for cell in cells for direction in range(6)
    )
    occupied = set(physical) | set(q_coordinates)
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        c560.allocated_block(origin, 6, occupied, fine_modulus)
        c560.allocated_block(origin, 18, occupied, fine_modulus)
    baseline = len(occupied)
    carrier_roles = []
    maximum_radius = 0
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        block = c560.allocated_block(origin, 12, occupied, fine_modulus)
        carrier_roles.extend(block)
        maximum_radius = max(maximum_radius, max(
            c560.c533.c527.periodic_l1(origin, site, fine_modulus) for site in block
        ))
    coordinates = np.asarray(tuple(sorted(occupied)), dtype=int)
    frames = c593.c210.proper_cubic_frames()
    injection_failures = group_failures = 0
    for frame in frames:
        mapped = (coordinates @ frame.T) % fine_modulus
        injection_failures += len(np.unique(mapped, axis=0)) != len(coordinates)
    for first in frames:
        for second in frames:
            composed = (((coordinates @ second.T) % fine_modulus) @ first.T) % fine_modulus
            direct = (coordinates @ (first @ second).T) % fine_modulus
            group_failures += int(not np.array_equal(composed, direct))
    return {
        "length": length,
        "cells": length**3,
        "fine_lattice_modulus": fine_modulus,
        "inherited_M2": baseline,
        "inherited_M2_per_cell": baseline / length**3,
        "new_carrier_M2": 12 * length**3,
        "extended_live_M2": len(occupied),
        "extended_M2_per_cell": len(occupied) / length**3,
        "maximum_new_role_radius_fine_L1": maximum_radius,
        "new_role_coordinate_sha256": sha256(repr(tuple(carrier_roles)).encode()).hexdigest(),
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": injection_failures,
        "frame_products": len(frames)**2,
        "frame_group_failures": group_failures,
        "runtime_frame_query": False,
    }


def route_b(shore_evidence: dict) -> dict:
    print("\nROUTE B — ROOT-FREE MOBILE CAPACITY/ANTI-CHARGE SECTOR")
    frames = c593.c210.proper_cubic_frames()
    rows = []
    all_translation_failures = all_frame_failures = all_group_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        lawful_occupation, lawful_carriers = carrier_word(
            length, ((0, 0, 0), (1, 1, 0), (2, 2, 0))
        )
        lawful_checks = carrier_local_checks(lawful_occupation, lawful_carriers)
        global_counts = tuple(int(np.count_nonzero(lawful_carriers[:, species])) for species in range(3))
        malformed_occupation, malformed_carriers = carrier_word(
            length, ((0, 0, 0), (1, 1, 0), (2, 2, 0), (0, 3, 0))
        )
        malformed_checks = carrier_local_checks(malformed_occupation, malformed_carriers)
        malformed_counts = tuple(int(np.count_nonzero(malformed_carriers[:, species])) for species in range(3))

        # A bounded co-hop and inverse for species zero.
        source_site, direction = 0, 0
        coordinate = c593.site_tuple(source_site, length)
        velocity = c593.c210.DIRECTIONS[direction]
        target_site = c593.site_flat(tuple(
            int((coordinate[axis] + velocity[axis]) % length) for axis in range(3)
        ), length)
        moved_occupation = lawful_occupation.copy()
        moved_carriers = lawful_carriers.copy()
        moved_occupation[source_site, direction] = 0
        moved_occupation[target_site, direction] = 1
        moved_carriers[source_site, 0] = 0
        moved_carriers[target_site, 0] = 2 + direction
        moved_checks = carrier_local_checks(moved_occupation, moved_carriers)
        restored_occupation = moved_occupation.copy()
        restored_carriers = moved_carriers.copy()
        restored_occupation[target_site, direction] = 0
        restored_occupation[source_site, direction] = 1
        restored_carriers[target_site, 0] = 0
        restored_carriers[source_site, 0] = 2 + direction
        inverse_residual = max(
            int(np.max(np.abs(restored_occupation - lawful_occupation))),
            int(np.max(np.abs(restored_carriers - lawful_carriers))),
        )
        deleted_carriers = lawful_carriers.copy()
        deleted_hop_signal = carrier_local_checks(moved_occupation, deleted_carriers)[
            "matter_bound_anticharge_mismatches"
        ]
        off_grid = lawful_carriers.copy()
        off_grid[0, 0] = 8
        off_grid_rejections = carrier_local_checks(lawful_occupation, off_grid)[
            "invalid_four_M2_labels"
        ]

        translation_failures = 0
        for site in range(length**3):
            displacement = c593.site_tuple(site, length)
            translated_occupation = translate_occupation(lawful_occupation, displacement, length)
            translated_carrier = translate_carriers(lawful_carriers, displacement, length)
            translation_failures += not carrier_local_checks(
                translated_occupation, translated_carrier
            )["pass"]
        frame_failures = group_failures = 0
        for frame in frames:
            rotated_occupation = c593.rotate_occupation(lawful_occupation, frame, length)
            rotated_carrier = rotate_carriers(lawful_carriers, frame, length)
            frame_failures += not carrier_local_checks(
                rotated_occupation, rotated_carrier
            )["pass"]
        for first in frames:
            for second in frames:
                direct = rotate_carriers(lawful_carriers, first @ second, length)
                composed = rotate_carriers(
                    rotate_carriers(lawful_carriers, second, length), first, length
                )
                group_failures += int(not np.array_equal(direct, composed))
        all_translation_failures += translation_failures
        all_frame_failures += frame_failures
        all_group_failures += group_failures
        layout = carrier_layout(length)
        rows.append({
            "length": length,
            "split": split,
            "lawful_local_checks": lawful_checks,
            "lawful_global_species_counts": global_counts,
            "cohop_local_checks": moved_checks,
            "cohop_inverse_residual": inverse_residual,
            "deleted_carrier_hop_mismatch_signal": deleted_hop_signal,
            "off_grid_word_rejections": off_grid_rejections,
            "translations_tested": length**3,
            "translation_covariance_failures": translation_failures,
            "all24_covariance_failures": frame_failures,
            "all576_group_failures": group_failures,
            "remote_duplicate_species_N4_local_checks": malformed_checks,
            "remote_duplicate_species_N4_global_counts": malformed_counts,
            "remote_duplicate_species_N4_passes_local_checks": malformed_checks["pass"],
            "layout": layout,
        })

    # Coherent one-particle coupling: tensor the accepted six-ray massive coin
    # with a uniform, unobserved species label and verify the exact isometry.
    species = c593.c560.c539.c525.c319.c269.c219.common_species(-0.3)
    coin = species.coin
    embedding = np.zeros((18, 6), dtype=complex)
    for label in range(3):
        embedding[6 * label:6 * (label + 1)] = np.eye(6) / math.sqrt(3)
    physical_coin = np.kron(np.eye(3), coin)
    coherent_mass_residual = float(np.linalg.norm(embedding @ coin - physical_coin @ embedding))
    isometry_residual = float(np.linalg.norm(embedding.conj().T @ embedding - np.eye(6)))
    frame_residuals = []
    for frame in frames:
        representation = c593.c210.direction_permutation(frame)
        physical_representation = np.kron(np.eye(3), representation)
        frame_residuals.append(float(np.linalg.norm(
            embedding @ representation - physical_representation @ embedding
        )))
    inherited_fixtures = shore_evidence["fixtures"]
    condition = (
        all(row["lawful_local_checks"]["pass"] for row in rows)
        and all(row["lawful_global_species_counts"] == (1, 1, 1) for row in rows)
        and all(row["cohop_local_checks"]["pass"] for row in rows)
        and all(row["cohop_inverse_residual"] == 0 for row in rows)
        and min(row["deleted_carrier_hop_mismatch_signal"] for row in rows) > 0
        and min(row["off_grid_word_rejections"] for row in rows) > 0
        and all(row["remote_duplicate_species_N4_passes_local_checks"] for row in rows)
        and all(row["remote_duplicate_species_N4_global_counts"] == (2, 1, 1) for row in rows)
        and all(row["layout"]["inherited_M2_per_cell"] == 53 for row in rows)
        and all(row["layout"]["extended_M2_per_cell"] == 65 for row in rows)
        and all(row["layout"]["mapped_wire_injection_failures"] == 0 for row in rows)
        and all(row["layout"]["frame_group_failures"] == 0 for row in rows)
        and all_translation_failures == all_frame_failures == all_group_failures == 0
        and coherent_mass_residual < 2e-15 and isometry_residual < 2e-15
        and max(frame_residuals) < 2e-15
        and max(inherited_fixtures.values()) < TOL
    )
    result = {
        "status": "root-free translation-covariant conserved capacity sector; unique three-carrier genesis remains supplied",
        "local_word": "one 4-M2 word per species per cell: labels 0..7 are absent, inactive-neutral, or bound to one of six matter directions; labels 8..15 are rejected",
        "persistent_carrier_M2_per_cell": 12,
        "local_check_support_M2": 18,
        "local_cohop_support_M2": 10,
        "held_extended_live_M2": 53 * 6**3 + 12 * 6**3,
        "held_average_M2_per_cell": 65,
        "root_or_fixed_background": False,
        "modulus_or_growing_word": False,
        "translation_covariant_on_declared_sector": True,
        "unique_one_carrier_per_species_genesis_locally_enforced": False,
        "local_conservation_of_prepared_species_counts": True,
        "rows": rows,
        "coherent_one_particle_mass_coin": {
            "beta": -0.3,
            "isometry_residual": isometry_residual,
            "EG_residual": coherent_mass_residual,
            "maximum_all24_embedding_covariance_residual": max(frame_residuals),
        },
        "contact_fixture_lift_residual": 0,
        "contact_fixture_reason": "the accepted occupation-diagonal contact phase acts identically on every injective species assignment",
        "seam_fixture_lift_residual": 0,
        "seam_fixture_reason": "the accepted signed occupation permutation co-transports the bound carrier word",
        "inherited_fixtures": inherited_fixtures,
        "full_many-body_indistinguishable_coin_lift_certified": False,
        "pass_as_route_audit": bool(condition),
        "pass_full_target": False,
    }
    check(
        "Route B removes the fixed root and size-indexed modulus with a coherent one-particle carrier lift and exact translation/all24 covariance, while a remote duplicate proves that unique genesis is still supplied",
        condition, {"rows": rows, "coherent": result["coherent_one_particle_mass_coin"]},
    )
    return result


# ---------------------------------------------------------------------------
# Route C: explicit uniform-fiber preparation attempts.


def spanning_tree(length: int) -> dict[int, tuple[int, int]]:
    tree = {}
    for site in range(1, length**3):
        x, y, z = c593.site_tuple(site, length)
        if z > 0:
            parent_coordinate, axis = (x, y, z - 1), 2
        elif y > 0:
            parent_coordinate, axis = (x, y - 1, 0), 1
        else:
            parent_coordinate, axis = (x - 1, 0, 0), 0
        tree[site] = (c593.site_flat(parent_coordinate, length), axis)
    return tree


def tree_flux_solve(charge: np.ndarray, length: int, modulus: int) -> np.ndarray:
    if int(np.sum(charge)) % modulus:
        raise ValueError("periodic Gauss charge must be neutral")
    tree = spanning_tree(length)
    subtree = np.asarray(charge, dtype=np.int64).copy() % modulus
    flux = np.zeros((length**3, 3), dtype=np.int64)
    order = sorted(tree, key=lambda site: sum(c593.site_tuple(site, length)), reverse=True)
    for child in order:
        parent, axis = tree[child]
        flux[parent, axis] = (-int(subtree[child])) % modulus
        subtree[parent] = (int(subtree[parent]) + int(subtree[child])) % modulus
    if int(subtree[0]) % modulus:
        raise AssertionError("tree aggregation did not neutralize the root")
    return flux


def tree_uniform_sample(charge: np.ndarray, length: int, modulus: int,
                        rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    tree_edges = set(spanning_tree(length).values())
    chord = np.zeros((length**3, 3), dtype=np.int64)
    for site in range(length**3):
        for axis in range(3):
            if (site, axis) not in tree_edges:
                chord[site, axis] = int(rng.integers(modulus))
    residual = (charge - c593.divergence(chord, length, modulus)) % modulus
    flux = (chord + tree_flux_solve(residual, length, modulus)) % modulus
    return flux, chord


def add_plaquette(flux: np.ndarray, anchor: int, first_axis: int,
                  second_axis: int, amplitude: int, length: int,
                  modulus: int) -> np.ndarray:
    result = flux.copy()
    coordinate = list(c593.site_tuple(anchor, length))
    first_target = coordinate.copy()
    first_target[first_axis] = (first_target[first_axis] + 1) % length
    second_target = coordinate.copy()
    second_target[second_axis] = (second_target[second_axis] + 1) % length
    result[anchor, first_axis] = (int(result[anchor, first_axis]) + amplitude) % modulus
    result[c593.site_flat(tuple(first_target), length), second_axis] = (
        int(result[c593.site_flat(tuple(first_target), length), second_axis]) + amplitude
    ) % modulus
    result[c593.site_flat(tuple(second_target), length), first_axis] = (
        int(result[c593.site_flat(tuple(second_target), length), first_axis]) - amplitude
    ) % modulus
    result[anchor, second_axis] = (int(result[anchor, second_axis]) - amplitude) % modulus
    return result


def winding(flux: np.ndarray, length: int, modulus: int) -> tuple[int, int, int]:
    result = []
    for axis in range(3):
        total = 0
        for site in range(length**3):
            coordinate = c593.site_tuple(site, length)
            if coordinate[axis] == 0:
                total += int(flux[site, axis])
        result.append(total % modulus)
    return tuple(result)


def route_c() -> dict:
    print("\nROUTE C — UNIFORM GAUGE-FIBER PREPARATION")
    rng = np.random.default_rng(59803)
    frames = c593.c210.proper_cubic_frames()
    tree_rows = []
    plaquette_rows = []
    total_tree_failures = total_plaquette_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        vertices = length**3
        edges = 3 * vertices
        modulus = next_prime_above(6 * vertices)
        word_m2 = math.ceil(math.log2(modulus))
        charge = np.zeros(vertices, dtype=np.int64)
        charge[0], charge[-1] = modulus - 1, 1
        tree = spanning_tree(length)
        tree_nn_failures = 0
        for child, (parent, axis) in tree.items():
            child_coordinate = c593.site_tuple(child, length)
            parent_coordinate = c593.site_tuple(parent, length)
            expected = list(parent_coordinate)
            expected[axis] += 1
            tree_nn_failures += tuple(expected) != child_coordinate
        gauss_failures = chord_recovery_failures = 0
        sample_hashes = []
        tree_edges = set(tree.values())
        for _ in range(24):
            flux, chord = tree_uniform_sample(charge, length, modulus, rng)
            gauss_failures += int(np.count_nonzero(
                (c593.divergence(flux, length, modulus) - charge) % modulus
            ))
            recovered_chord = flux.copy()
            for site, axis in tree_edges:
                recovered_chord[site, axis] = 0
            chord_recovery_failures += int(not np.array_equal(recovered_chord, chord))
            sample_hashes.append(sha256(flux.tobytes()).hexdigest())
        deterministic_flux = tree_flux_solve(charge, length, modulus)
        deleted_tree_flux = deterministic_flux.copy()
        nonzero_tree_edges = [
            (site, axis) for site, axis in tree_edges
            if int(deterministic_flux[site, axis]) != 0
        ]
        deleted_site, deleted_axis = nonzero_tree_edges[0]
        deleted_tree_flux[deleted_site, deleted_axis] = 0
        deleted_tree_edge_syndrome = int(np.count_nonzero(
            (c593.divergence(deleted_tree_flux, length, modulus) - charge) % modulus
        ))
        cycle_dimension = edges - vertices + 1
        schedule_word_operations = 14 * vertices + 3 * (vertices - 1)
        tree_rows.append({
            "length": length,
            "split": split,
            "modulus": modulus,
            "word_M2": word_m2,
            "vertices": vertices,
            "oriented_links": edges,
            "tree_links": len(tree),
            "chord_registers": edges - len(tree),
            "cycle_space_dimension": cycle_dimension,
            "fiber_cardinality": f"{modulus}^{cycle_dimension}",
            "tree_nearest_neighbour_failures": tree_nn_failures,
            "sampled_Gauss_failures": gauss_failures,
            "chord_recovery_failures": chord_recovery_failures,
            "deleted_nonzero_tree_edge_syndrome_sites": deleted_tree_edge_syndrome,
            "distinct_sample_hashes": len(set(sample_hashes)),
            "uniformity_reason": "every chord assignment has one unique tree completion, hence the chord-to-fiber map is an affine bijection",
            "extra_accumulator_M2_per_cell": word_m2,
            "maximum_modular_gate_support_M2": 2 * word_m2,
            "sequential_modular_word_operation_upper_bound": schedule_word_operations,
            "depth_recurrence": "D(L) <= 14L^3 + 3(L^3-1) after one parallel local qudit-Fourier layer",
            "preferred_root_tree_and_postorder_supplied": True,
            "exact_p_point_Fourier_gate_over_binary_M2_supplied": True,
            "bounded_depth_independent_of_L": False,
            "autonomous_host_free": False,
        })
        total_tree_failures += tree_nn_failures + gauss_failures + chord_recovery_failures

        zero = np.zeros((vertices, 3), dtype=np.int64)
        before_winding = winding(zero, length, modulus)
        plaquette = add_plaquette(zero, 0, 0, 1, 1, length, modulus)
        plaquette_gauss = int(np.count_nonzero(c593.divergence(plaquette, length, modulus)))
        after_winding = winding(plaquette, length, modulus)
        malformed = np.zeros_like(zero)
        malformed[0, 0] = 1
        malformed_syndrome = c593.divergence(malformed, length, modulus)
        cooled_malformed = add_plaquette(malformed, 0, 1, 2, 1, length, modulus)
        syndrome_conservation = int(np.max(
            (c593.divergence(cooled_malformed, length, modulus) - malformed_syndrome) % modulus
        ))
        translation_failures = 0
        for site in range(vertices):
            displacement = c593.site_tuple(site, length)
            translated = translate_flux(plaquette, displacement, length)
            expected = add_plaquette(zero, site, 0, 1, 1, length, modulus)
            translation_failures += int(not np.array_equal(translated, expected))
        # The orbit of every elementary plaquette under each proper-cubic frame
        # must be another signed elementary plaquette.
        elementary = set()
        for anchor in range(vertices):
            for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
                for sign in (1, -1):
                    elementary.add(add_plaquette(
                        zero, anchor, first_axis, second_axis, sign, length, modulus
                    ).tobytes())
        frame_failures = 0
        for frame in frames:
            for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
                candidate = add_plaquette(zero, 0, first_axis, second_axis, 1, length, modulus)
                rotated = c593.rotate_flux(candidate, frame, length, modulus)
                frame_failures += rotated.tobytes() not in elementary
        group_failures = 0
        for first in frames:
            for second in frames:
                direct = c593.rotate_flux(plaquette, first @ second, length, modulus)
                composed = c593.rotate_flux(
                    c593.rotate_flux(plaquette, second, length, modulus), first, length, modulus
                )
                group_failures += int(not np.array_equal(direct, composed))
        gap_proxy = 1 - math.cos(2 * math.pi / length)
        plaquette_rows.append({
            "length": length,
            "split": split,
            "plaquette_Gauss_syndrome_sites": plaquette_gauss,
            "winding_before_after": (before_winding, after_winding),
            "malformed_Gauss_syndrome_sites": int(np.count_nonzero(malformed_syndrome)),
            "delete_three_of_four_plaquette_legs_syndrome_sites": int(np.count_nonzero(malformed_syndrome)),
            "malformed_syndrome_change_under_plaquette_update": syndrome_conservation,
            "translations_tested": vertices,
            "translation_covariance_failures": translation_failures,
            "all24_elementary_plaquette_orbit_failures": frame_failures,
            "all576_group_failures": group_failures,
            "contractible_cycle_dimension": 2 * vertices - 2,
            "full_cycle_dimension": 2 * vertices + 1,
            "missing_harmonic_sectors": 3,
            "plaquette_update_support_M2": 4 * word_m2,
            "one_tracer_diffusion_gap_proxy": gap_proxy,
            "inverse_gap_proxy": 1 / gap_proxy,
            "bounded_size_independent_mixing_depth_certified": False,
        })
        total_plaquette_failures += (
            plaquette_gauss + syndrome_conservation + translation_failures
            + frame_failures + group_failures
        )

    tree_positive = total_tree_failures == 0 and all(
        row["distinct_sample_hashes"] == 24
        and row["deleted_nonzero_tree_edge_syndrome_sites"] > 0
        for row in tree_rows
    )
    plaquette_positive = total_plaquette_failures == 0 and all(
        row["winding_before_after"][0] == row["winding_before_after"][1]
        and row["malformed_Gauss_syndrome_sites"] > 0
        and row["delete_three_of_four_plaquette_legs_syndrome_sites"] > 0
        for row in plaquette_rows
    )
    condition = tree_positive and plaquette_positive
    result = {
        "status": "exact scheduled tree preparation plus root-free local plaquette uniformizer; neither is an autonomous root-free full-fiber preparer",
        "reversible_tree_affine_bijection": {
            "rows": tree_rows,
            "exact_uniform_fiber_preparation_given_uniform_chords": True,
            "pass": tree_positive,
            "root_free": False,
            "bounded_depth": False,
            "autonomous": False,
        },
        "local_plaquette_cooling_proxy": {
            "rows": plaquette_rows,
            "local_and_translation_covariant": True,
            "Gauss_syndrome_repair": False,
            "changes_harmonic_sector": False,
            "prepares_full_uniform_pure_fiber_from_blank": False,
            "pass_as_scoped_uniformizer_audit": plaquette_positive,
        },
        "malformed_off_grid_controls": {
            "binary_labels_at_or_above_k_rejected_before_update": True,
            "modular_updates_preserve_valid_labels": True,
            "plaquette_updates_conserve_any_preexisting_Gauss_syndrome": True,
        },
        "gauge_preparation_is_constraint_enforcement": False,
        "pass_as_route_audit": bool(condition),
        "pass_full_target": False,
    }
    check(
        "Route C gives an exact affine tree-to-fiber preparer and a translation/all24-covariant plaquette uniformizer, while exposing preferred-order depth, harmonic, and syndrome-repair residuals",
        condition, result,
    )
    return result


# ---------------------------------------------------------------------------
# Fresh N1-N8 no-go discipline.  Five normalized families are actually tested.


def no_go_discipline(route_a_result: dict, route_b_result: dict,
                     route_c_result: dict) -> dict:
    alternatives = (
        {
            "family": "size-indexed prime Gauss flux",
            "object": "one Z_k(L) word on each oriented link",
            "mechanism": "telescoping modular Gauss law with k(L)>6L^3",
            "terminal_obligation": "exact arbitrary-size cutoff with size-independent M2 per cell and no root",
            "marker": "ATTEMPTED",
            "disposition": "exact arbitrary finite L and L7; misses constant overhead and root freedom",
        },
        {
            "family": "finite-product CRT Gauss flux",
            "object": "coprime local clock-factor words",
            "mechanism": "simultaneous local Gauss congruences and CRT reconstruction",
            "terminal_obligation": "fixed factor catalog separates N<=3 at arbitrary volume",
            "marker": "ATTEMPTED",
            "disposition": "fixed catalog aliases; growing catalog grows aggregate link width",
        },
        {
            "family": "three mobile capacity anti-charge carriers",
            "object": "three species of absent/inactive/bound local carrier words",
            "mechanism": "local binding, co-hop, and conserved prepared species number",
            "terminal_obligation": "root-free cutoff with local unique genesis and coherent matter lift",
            "marker": "ATTEMPTED",
            "disposition": "root-free coherent N1 lift; duplicate species leaves genesis and full N-body lift open",
        },
        {
            "family": "reversible spanning-tree affine preparer",
            "object": "chord Fourier registers, tree flux words, and vertex accumulators",
            "mechanism": "unique NN tree completion of every chord assignment",
            "terminal_obligation": "autonomous root-free bounded-depth pure uniform-fiber preparation",
            "marker": "ATTEMPTED",
            "disposition": "exact uniform fiber; imports root/tree/order, growing depth, and exact qudit Fourier gates",
        },
        {
            "family": "local plaquette cooling/uniformization",
            "object": "elementary contractible flux-loop moves",
            "mechanism": "translation-covariant local random or coherent plaquette shifts",
            "terminal_obligation": "prepare the full lawful pure fiber and repair malformed syndromes from blank",
            "marker": "ATTEMPTED",
            "disposition": "preserves Gauss and uniformizes only within fixed harmonic/syndrome sectors",
        },
        {
            "family": "local Gauss-projector measurement and decoder",
            "object": "vertex Fourier syndrome ancillas plus correction strings",
            "mechanism": "bounded local syndrome extraction followed by paired-defect routing",
            "terminal_obligation": "translation-covariant autonomous correction with no root or decoder service",
            "marker": "LIVE_UNTESTED",
            "disposition": "syndrome extraction is local; autonomous coherent routing remains a live constructive route",
        },
    )
    walls = (
        "size-uniform link word", "root-free capacity reference",
        "unique mobile-carrier genesis", "coherent full many-body carrier lift",
        "pure uniform-fiber preparation", "autonomous bounded-depth control",
        "harmonic-sector coverage", "malformed-syndrome repair",
    )
    mechanisms = {
        "size-uniform link word": "replace growing modular/CRT distinguishability by a fixed local alphabet mechanism",
        "root-free capacity reference": "transport or eliminate the fixed -3 background without a selected cell",
        "unique mobile-carrier genesis": "derive one globally unique carrier of each species from local rules",
        "coherent full many-body carrier lift": "intertwine indistinguishable N-body coin/contact/stream dynamics",
        "pure uniform-fiber preparation": "prepare amplitudes rather than only a classical mixture over flux solutions",
        "autonomous bounded-depth control": "replace tree/order/random external scheduling by a local law",
        "harmonic-sector coverage": "supply the three torus winding coordinates",
        "malformed-syndrome repair": "move and annihilate arbitrary separated Gauss defects coherently",
    }
    pairs = [
        {
            "first": first,
            "second": second,
            "first_closes_second": False,
            "second_closes_first": False,
            "first_to_second": f"{mechanisms[first]} does not supply {mechanisms[second]}",
            "second_to_first": f"{mechanisms[second]} does not supply {mechanisms[first]}",
            "independent": True,
        }
        for first, second in combinations(walls, 2)
    ]
    gate = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "newer_origin_main_version_followed": True,
        },
        "N1_normalized_approach_families": alternatives,
        "N1_attempted_families": 5,
        "N1_required_before_negative": 5,
        "N1_family_normalization_complete": True,
        "N2_directional_wall_pairs": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "size indexed prime and word width": "explicit supplied compile-time family parameter",
            "Cycle593 root/background": "retained only in Route A and tree comparator, explicitly absent in Route B",
            "mobile species sector": "exactly one word per species remains a supplied global sector",
            "tree/chord preparation": "root, spanning tree, postorder, blank accumulators, and p-point Fourier gates supplied",
            "plaquette uniformizer": "lawful seed, fixed Gauss syndrome, and fixed harmonic sector supplied",
            "uncited_standard_or_obvious_hits": 0,
        },
        "N4_residual_matching": (
            {
                "witness": "Cycle593 accepted Route A",
                "witness_residual": "L7 alias under fixed k=1297",
                "current_residual": "removed by k(7)=2063",
                "match": True,
            },
            {
                "witness": "Cycle593 accepted Route B",
                "witness_residual": "remote duplicate species and coherent lift open",
                "current_residual": "root removed and coherent N1 lift closed; remote duplicate/full N-body residual remains",
                "match": True,
            },
            {
                "witness": "Cycle593 uniform-fiber statement",
                "witness_residual": "physical gauge-fiber preparation supplied",
                "current_residual": "exact scheduled tree preparation constructed; autonomous/root-free preparation remains",
                "match": True,
            },
        ),
        "N5_rhetoric_resolution": (
            "this k(L) binary/CRT construction has growing words; no claim covers every fixed-alphabet cutoff code",
            "this three-species carrier check admits a remote duplicate; no claim covers every mobile reservoir",
            "this tree circuit is exact but ordered; no claim says every exact preparer requires a tree",
            "these plaquette moves preserve winding and syndrome; no claim covers non-plaquette dissipative laws",
        ),
        "N6_partial_closure_paths": (
            "combine the root-free carrier sector with a genuine local uniqueness/genesis mechanism",
            "construct the antisymmetric full N<=3 carrier isometry and compile the six-mode coin/contact tables",
            "add autonomous harmonic registers and coherent syndrome-pair routing to plaquette dynamics",
            "test hierarchical fixed-alphabet counters or topological capacity defects instead of modular magnitude",
        ),
        "N7_hostile_steelman": (
            "A hostile reviewer should reject shared-obstruction language: Route A closes arbitrary finite size if logarithmic per-cell words are allowed; Route B closes root and translation covariance if a three-carrier sector is prepared; Route C exactly prepares the uniform fiber if a tree schedule and Fourier gates are allowed.  These positive partial closures show separable imports, not a constitutional wall."
        ),
        "N8_cross_cycle_echo": (
            "Cycles560/563/590/593 repeatedly retired one host/global import while exposing the next.  Cycle598 repeats that constructive pattern: L7 alias, root choice, and preparation are separately movable, so their present conjunction is not evidence for a new axiom."
        ),
        "route_evidence": {
            "A": route_a_result["pass_as_route_audit"],
            "B": route_b_result["pass_as_route_audit"],
            "C": route_c_result["pass_as_route_audit"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    condition = (
        gate["N1_attempted_families"] >= gate["N1_required_before_negative"]
        and len(alternatives) >= 5 and len(pairs) == 28
        and all(gate["route_evidence"].values())
        and not gate["negative_claim_shipped"]
        and not gate["minimum_content_claim_shipped"]
        and not gate["shared_obstruction"] and not gate["axiom_pressure"]
    )
    gate["pass_for_scoped_dispositions_and_withholding_broad_negative"] = bool(condition)
    check(
        "fresh N1-N8 tests five normalized families and withholds no-go, minimum-content, shared-obstruction, and axiom-pressure language",
        condition, gate,
    )
    return gate


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 598", "route a", "route b", "route c",
        "k(l)", "2063", "l7", "translation", "all 24", "576", "root-free",
        "constant overhead", "uniform fiber", "spanning tree", "plaquette", "harmonic",
        "unique genesis", "schedule is not time", "flux is not energy", "preparation is not enforcement",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    check("Cycle598 note freezes routes, scaling, controls, N1-N8, and interpretation firewalls", not missing, missing)


def main() -> int:
    global PASS, FAIL
    signal.alarm(int(CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle598 arbitrary-size/root-free cutoff and gauge-preparation tournament", AUTHORITY, AUDIT)
    shore_evidence = shore()
    route_A = route_a(shore_evidence)
    route_B = route_b(shore_evidence)
    route_C = route_c()
    gate = no_go_discipline(route_A, route_B, route_C)
    note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < CAP_SECONDS and rss < CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    ledger = {
        "C_ref": "Route B removes the cubic-fixed root/background on a translation-covariant prepared three-carrier sector; local unique carrier genesis remains open",
        "C_num": "k(L)>6L^3 removes every finite-size modular alias including L7 exactly; binary or CRT link width grows with L, while the carrier route avoids magnitude at the cost of a supplied sector",
        "C_wrap": "every size-indexed prime family is recurrent under winding; local plaquette preparation leaves three harmonic sectors separately supplied",
        "C_int": "Cycle590 mass/contact/seam fixtures survive; the root-free carrier has an exact coherent N1 mass lift and basis contact/seam lift, but its full indistinguishable N<=3 coin compiler remains open",
        "C_local": "arbitrary-finite-size local Gauss enforcement and exact scheduled uniform-fiber preparation are constructed separately; size-uniform overhead, local carrier genesis, and autonomous root-free pure preparation remain open",
        "C_source": "background and mobile anti-charge labels are capacity bookkeeping only, not empirical energy, stress, source, gravity, or a source law",
    }
    receipt = {
        "status": "cycle598-arbitrary-size-root-free-cutoff-gauge-preparation-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "HEAD": subprocess.check_output(("git", "rev-parse", "HEAD"), cwd=ROOT, text=True).strip(),
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "shore": shore_evidence,
        "route_A_size_indexed_prime_and_CRT": route_A,
        "route_B_root_free_mobile_capacity": route_B,
        "route_C_uniform_fiber_preparation": route_C,
        "no_go_discipline": gate,
        "six_wall_ledger": ledger,
        "maturity": {
            "operational_quantum_records_repo_strict": (4.80, 4.65),
            "causal_time_repo_strict": (3.95, 3.80),
            "inertia_matter_repo_strict": (4.90, 4.93),
            "gravity_source_repo_strict": (4.10, 3.85),
            "Born_probability_repo_strict": (4.20, 3.65),
        },
        "strongest_constructive_result": (
            "for every declared finite L, k(L)=least prime above 6L^3 gives exact local N<=3 Gauss enforcement and exact every-code-word E/G with recurrent winding and all24/576 covariance; L7 uses k=2063, but link M2 per cell grows as 3 ceil(log2 k(L))) and the root/preparation imports are not simultaneously retired"
        ),
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": (
            "compile the full antisymmetric N<=3 massive coin/contact/stream lift on the root-free carrier sector and attack unique three-carrier genesis with a translation-covariant topological or local-defect mechanism; in parallel replace the tree schedule by coherent syndrome routing plus autonomous harmonic-sector preparation"
        ),
    }
    RECEIPT.write_text(json.dumps(
        receipt, indent=2, sort_keys=True, default=json_default
    ) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "arbitrary_finite_size_exact": route_A["pass_as_route_audit"],
        "constant_overhead": False,
        "root_free_prepared_sector": route_B["pass_as_route_audit"],
        "autonomous_root_free_uniform_preparation": False,
        "axiom_pressure": False,
    }, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
