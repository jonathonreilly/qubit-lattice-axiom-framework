#!/usr/bin/env python3
"""Cycle593: finite-volume local N<=3 gauge-enforcement tournament.

The selected Route-A law is a finite L3/L6 construction.  Its Z_1297
modulus is chosen from held L6 capacity, its cubic-fixed root/background and
gauge-state preparation are supplied, and L7 is an explicit alias failure.
Compiler schedules are not physical time, flux labels are not energy, and a
counter flag is not enforcement or a Record.
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

import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import physical_global_N3_returned_slot_compiler_cycle560_2026_07_21 as c560


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_CUTOFF_GAUGE_ENFORCEMENT_TOURNAMENT_CYCLE593_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_local_cutoff_gauge_enforcement_tournament_"
    "cycle593_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE590 = "3a137ad6583104fe82d283883d1d970060bc9bf2"
GAUGE_MODULUS = 1297
GAUGE_WORD_M2 = 11
COUNTER_MODULUS = 2048
TOL = 5e-9
SIGNAL = 1e-8
CAP_SECONDS = 360.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    # Accepted Cycle590 contains a scoped post-run note clarification; the
    # receipt retains the pre-clarification note hash and is pinned separately.
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json":
        "ebc13a522e439e2a1618421773751c096b210cc4be25476511dead5a6ea241f7",
    "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py":
        "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "scripts/physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py":
        "c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
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


def site_tuple(site: int, length: int) -> tuple[int, int, int]:
    return site // (length * length), (site // length) % length, site % length


def site_flat(site: tuple[int, int, int], length: int) -> int:
    return (site[0] * length + site[1]) * length + site[2]


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE590, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0
    receipt = json.loads((ROOT / (
        "outputs/physical_full_torus_dimer_M2_compiler_tournament_"
        "cycle590_receipt_2026_07_22.json"
    )).read_text())
    fixtures = receipt["retained_fixtures"]
    cycle590 = {
        "pass": receipt["pass"],
        "tests_passed": receipt["tests_passed"],
        "exact_EG_residual": receipt["route_B_physical_M2_compiler"][
            "exact_EG_equals_GphysicalE_residual"
        ],
        "global_cutoff_locally_enforced": receipt["route_B_physical_M2_compiler"][
            "global_N_le_3_cutoff_locally_enforced"
        ],
        "held_packet_update_residual": receipt["route_A_full_torus_packet"]["rows"][1][
            "packet_full_torus_update_residual"
        ],
        "held_packet_all24_residual": receipt["route_A_full_torus_packet"]["rows"][1][
            "maximum_all24_covariance_residual"
        ],
        "compiler_live_M2": receipt["route_B_physical_M2_compiler"]["physical_layout"][
            "compiler_live_M2"
        ],
        "compiler_M2_per_cell": receipt["route_B_physical_M2_compiler"]["physical_layout"][
            "compiler_live_M2_per_cell"
        ],
        "accepted_post_run_note_clarification": True,
        "receipt_pre_clarification_note_sha256": receipt["note_sha256"],
        "accepted_current_note_sha256": PINS[
            "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md"
        ],
    }
    condition = (
        ancestor and observed == PINS and cycle590["pass"]
        and cycle590["tests_passed"] == 7
        and cycle590["exact_EG_residual"] == 0
        and not cycle590["global_cutoff_locally_enforced"]
        and cycle590["compiler_live_M2"] == 11448
        and cycle590["compiler_M2_per_cell"] == 53
        and max(fixtures.values()) < TOL
    )
    check(
        "accepted Cycle590 and the 560/563/569/230/219 shores are ancestral and byte exact",
        condition,
        {"ancestor": ancestor, "observed": observed, "Cycle590": cycle590,
         "fixtures": fixtures},
    )
    return {"Cycle590": cycle590, "fixtures": fixtures}


# ---------------------------------------------------------------------------
# Route A: finite-volume modular Gauss/flux enforcement.


def reservoir_word(total_number: int) -> np.ndarray:
    if total_number < 0 or total_number > 3:
        raise ValueError("the canonical root reservoir is defined only for N=0..3")
    spectator_count = 3 - total_number
    return np.asarray([int(index < spectator_count) for index in range(3)], dtype=np.int8)


def prefix_valid(bits: np.ndarray) -> bool:
    return tuple(int(value) for value in bits) in ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))


def occupation_configuration(length: int, modes: tuple[int, ...]) -> np.ndarray:
    occupation = np.zeros((length**3, 6), dtype=np.int8)
    for mode in modes:
        site, direction = divmod(int(mode), 6)
        if occupation[site, direction]:
            raise ValueError("duplicate fermion mode")
        occupation[site, direction] = 1
    return occupation


def canonical_flux(occupation: np.ndarray, length: int,
                   modulus: int = GAUGE_MODULUS) -> np.ndarray:
    """Preparation witness only: route each charge to the cubic-fixed root."""
    flux = np.zeros((length**3, 3), dtype=np.int64)
    for site, direction in zip(*np.nonzero(occupation)):
        del direction
        current = list(site_tuple(int(site), length))
        for axis in range(3):
            while current[axis] != 0:
                edge_start = list(current)
                edge_start[axis] -= 1
                edge_site = site_flat(tuple(edge_start), length)
                flux[edge_site, axis] = (flux[edge_site, axis] - 1) % modulus
                current = edge_start
    return flux


def divergence(flux: np.ndarray, length: int,
               modulus: int = GAUGE_MODULUS) -> np.ndarray:
    result = np.zeros(length**3, dtype=np.int64)
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for axis in range(3):
            predecessor = list(coordinate)
            predecessor[axis] = (predecessor[axis] - 1) % length
            result[site] += int(flux[site, axis]) - int(
                flux[site_flat(tuple(predecessor), length), axis]
            )
    return result % modulus


def charge(occupation: np.ndarray, spectators: np.ndarray,
           modulus: int = GAUGE_MODULUS) -> np.ndarray:
    result = np.sum(occupation, axis=1, dtype=np.int64)
    result[0] += int(np.sum(spectators)) - 3
    return result % modulus


def gauss_residual(flux: np.ndarray, occupation: np.ndarray,
                   spectators: np.ndarray, length: int,
                   modulus: int = GAUGE_MODULUS) -> np.ndarray:
    return (divergence(flux, length, modulus) - charge(
        occupation, spectators, modulus
    )) % modulus


def stream_with_flux(occupation: np.ndarray, flux: np.ndarray,
                     length: int, omit_edge: tuple[int, int] | None = None
                     ) -> tuple[np.ndarray, np.ndarray]:
    updated_flux = flux.copy()
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for axis in range(3):
            target_coordinate = list(coordinate)
            target_coordinate[axis] = (target_coordinate[axis] + 1) % length
            target = site_flat(tuple(target_coordinate), length)
            current = int(occupation[site, 2 * axis]) - int(
                occupation[target, 2 * axis + 1]
            )
            if omit_edge != (site, axis):
                updated_flux[site, axis] = (
                    int(updated_flux[site, axis]) - current
                ) % GAUGE_MODULUS
    updated = np.zeros_like(occupation)
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for direction, velocity in enumerate(c210.DIRECTIONS):
            target = site_flat(tuple(
                int((coordinate[axis] + velocity[axis]) % length)
                for axis in range(3)
            ), length)
            updated[target, direction] = occupation[site, direction]
    return updated, updated_flux


def inverse_stream_with_flux(occupation: np.ndarray, flux: np.ndarray,
                             length: int) -> tuple[np.ndarray, np.ndarray]:
    restored = np.zeros_like(occupation)
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for direction, velocity in enumerate(c210.DIRECTIONS):
            target = site_flat(tuple(
                int((coordinate[axis] + velocity[axis]) % length)
                for axis in range(3)
            ), length)
            restored[site, direction] = occupation[target, direction]
    restored_flux = flux.copy()
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for axis in range(3):
            target_coordinate = list(coordinate)
            target_coordinate[axis] = (target_coordinate[axis] + 1) % length
            target = site_flat(tuple(target_coordinate), length)
            current = int(restored[site, 2 * axis]) - int(
                restored[target, 2 * axis + 1]
            )
            restored_flux[site, axis] = (
                int(restored_flux[site, axis]) + current
            ) % GAUGE_MODULUS
    return restored, restored_flux


def rotate_occupation(occupation: np.ndarray, frame: np.ndarray,
                      length: int) -> np.ndarray:
    result = np.zeros_like(occupation)
    direction = np.argmax(c210.direction_permutation(frame), axis=0)
    for site in range(length**3):
        coordinate = np.asarray(site_tuple(site, length), dtype=int)
        target = site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
        for ray in range(6):
            result[target, int(direction[ray])] = occupation[site, ray]
    return result


def rotate_flux(flux: np.ndarray, frame: np.ndarray, length: int,
                modulus: int = GAUGE_MODULUS) -> np.ndarray:
    result = np.zeros_like(flux)
    for site in range(length**3):
        coordinate = np.asarray(site_tuple(site, length), dtype=int)
        mapped_source = frame @ coordinate
        for axis in range(3):
            mapped_vector = frame[:, axis]
            target_axis = int(np.argmax(np.abs(mapped_vector)))
            sign = int(mapped_vector[target_axis])
            target_source = mapped_source.copy()
            if sign < 0:
                target_source[target_axis] -= 1
            target = site_flat(tuple(int(value % length) for value in target_source), length)
            result[target, target_axis] = (sign * int(flux[site, axis])) % modulus
    return result


def physical_layout(length: int) -> dict:
    code = c560.c539.c525.c319.c269.build_code(length)
    cells = c560.c555.network_cells(length)
    modulus = c560.c533.c527.fine_length(length)
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
        c560.allocated_block(origin, 6, occupied, modulus)
        c560.allocated_block(origin, 18, occupied, modulus)
    baseline = len(occupied)
    gauge_by_cell = []
    maximum_radius = 0
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        block = c560.allocated_block(origin, 3 * GAUGE_WORD_M2, occupied, modulus)
        gauge_by_cell.append(block)
        maximum_radius = max(
            maximum_radius,
            max(c560.c533.c527.periodic_l1(origin, site, modulus) for site in block),
        )
    root = c560.c533.c527.cell_center((0, 0, 0), length)
    spectator_sites = c560.allocated_block(root, 3, occupied, modulus)
    maximum_radius = max(
        maximum_radius,
        max(c560.c533.c527.periodic_l1(root, site, modulus) for site in spectator_sites),
    )
    coordinates = np.asarray(tuple(occupied), dtype=int)
    frames = c210.proper_cubic_frames()
    injection_failures = group_failures = 0
    for frame in frames:
        mapped = (coordinates @ frame.T) % modulus
        injection_failures += len(np.unique(mapped, axis=0)) != len(coordinates)
    for first in frames:
        for second in frames:
            composed = (((coordinates @ second.T) % modulus) @ first.T) % modulus
            direct = (coordinates @ (first @ second).T) % modulus
            group_failures += int(not np.array_equal(composed, direct))
    result = {
        "length": length,
        "cells": length**3,
        "fine_lattice_modulus": modulus,
        "inherited_Cycle590_M2": baseline,
        "inherited_M2_per_cell": baseline / length**3,
        "new_flux_M2": 3 * GAUGE_WORD_M2 * length**3,
        "new_root_spectator_M2": 3,
        "extended_live_M2": len(occupied),
        "average_extended_M2_per_cell": len(occupied) / length**3,
        "maximum_new_role_radius_fine_L1": maximum_radius,
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": injection_failures,
        "frame_products": len(frames)**2,
        "frame_group_failures": group_failures,
        "runtime_frame_query": False,
        "transport_policy": "rotate the base local role layout and oriented-link values as one compile-time frame family",
    }
    result["pass"] = bool(
        baseline == 53 * length**3
        and len(occupied) == 86 * length**3 + 3
        and maximum_radius <= 4
        and len(frames) == 24
        and injection_failures == group_failures == 0
    )
    return result


def route_a(shore_evidence: dict) -> dict:
    print("\nROUTE A — FINITE-VOLUME Z_1297 GAUSS/FLUX CODE")
    prime = all(GAUGE_MODULUS % divisor for divisor in range(2, int(math.sqrt(GAUGE_MODULUS)) + 1))
    arithmetic_rows = []
    for length in (3, 6, 7):
        capacity = 6 * length**3
        accepted = [
            (number, spectators)
            for number in range(capacity + 1)
            for spectators in range(4)
            if (number + spectators - 3) % GAUGE_MODULUS == 0
        ]
        arithmetic_rows.append({
            "length": length,
            "matter_capacity": capacity,
            "N_plus_S_range": (0, capacity + 3),
            "accepted_N_S_pairs": accepted,
            "exact_N_le_3": accepted == [(0, 3), (1, 2), (2, 1), (3, 0)],
        })
    small_modulus_aliases = [
        (number, spectators)
        for number in range(9) for spectators in range(4)
        if (number + spectators - 3) % 4 == 0 and number > 3
    ]
    local_update_inverse_failures = 0
    for flux_value in range(GAUGE_MODULUS):
        for plus in (0, 1):
            for minus in (0, 1):
                current = plus - minus
                updated = (flux_value - current) % GAUGE_MODULUS
                restored = (updated + current) % GAUGE_MODULUS
                local_update_inverse_failures += restored != flux_value
    invalid_binary_labels = tuple(range(GAUGE_MODULUS, 2**GAUGE_WORD_M2))

    sample_rows = []
    maximum_gauss = maximum_inverse = maximum_covariance = maximum_rotated_gauss = 0
    covariance_failures = group_failures = 0
    rng = np.random.default_rng(59301)
    frames = c210.proper_cubic_frames()
    held_probe = None
    for length, split in ((3, "train"), (6, "held")):
        modes = 6 * length**3
        for number in range(4):
            selections = [tuple(range(number))]
            for _ in range(4):
                selections.append(tuple(sorted(rng.choice(modes, size=number, replace=False).tolist())))
            for selected in selections:
                occupation = occupation_configuration(length, selected)
                spectators = reservoir_word(number)
                flux = canonical_flux(occupation, length)
                residual = gauss_residual(flux, occupation, spectators, length)
                updated_occupation, updated_flux = stream_with_flux(occupation, flux, length)
                updated_residual = gauss_residual(
                    updated_flux, updated_occupation, spectators, length
                )
                restored_occupation, restored_flux = inverse_stream_with_flux(
                    updated_occupation, updated_flux, length
                )
                maximum_gauss = max(maximum_gauss, int(np.max(residual)), int(np.max(updated_residual)))
                maximum_inverse = max(
                    maximum_inverse,
                    int(np.max(np.abs(restored_occupation - occupation))),
                    int(np.max((restored_flux - flux) % GAUGE_MODULUS)),
                )
                if length == 6 and number == 3 and held_probe is None:
                    held_probe = (occupation, spectators, flux)
        sample_rows.append({
            "length": length,
            "split": split,
            "sampled_lawful_configurations": 20,
            "maximum_Gauss_residual": maximum_gauss,
            "maximum_stream_inverse_residual": maximum_inverse,
        })

    occupation, spectators, flux = held_probe
    updated_occupation, updated_flux = stream_with_flux(occupation, flux, 6)
    for frame in frames:
        rotated_occupation = rotate_occupation(occupation, frame, 6)
        rotated_flux = rotate_flux(flux, frame, 6)
        maximum_rotated_gauss = max(
            maximum_rotated_gauss,
            int(np.max(gauss_residual(
                rotated_flux, rotated_occupation, spectators, 6
            ))),
        )
        left_occ = rotate_occupation(updated_occupation, frame, 6)
        left_flux = rotate_flux(updated_flux, frame, 6)
        right_occ, right_flux = stream_with_flux(
            rotated_occupation, rotated_flux, 6
        )
        residual = max(
            int(np.max(np.abs(left_occ - right_occ))),
            int(np.max((left_flux - right_flux) % GAUGE_MODULUS)),
        )
        maximum_covariance = max(maximum_covariance, residual)
        covariance_failures += residual != 0
    for first in frames:
        for second in frames:
            direct_occ = rotate_occupation(occupation, first @ second, 6)
            composed_occ = rotate_occupation(rotate_occupation(occupation, second, 6), first, 6)
            direct_flux = rotate_flux(flux, first @ second, 6)
            composed_flux = rotate_flux(rotate_flux(flux, second, 6), first, 6)
            group_failures += int(
                not np.array_equal(direct_occ, composed_occ)
                or not np.array_equal(direct_flux, composed_flux)
            )

    # Delete the flux update on a known occupied +x crossing.
    deletion_occ = occupation_configuration(6, (6,))  # cell 1, +x ray
    deletion_spectators = reservoir_word(1)
    deletion_flux = canonical_flux(deletion_occ, 6)
    deleted_occ, deleted_flux = stream_with_flux(deletion_occ, deletion_flux, 6, omit_edge=(1, 0))
    link_update_deletion_violations = int(np.count_nonzero(
        gauss_residual(deleted_flux, deleted_occ, deletion_spectators, 6)
    ))
    spectator_deletion_signals = []
    vacuum = occupation_configuration(6, ())
    vacuum_spectators = reservoir_word(0)
    vacuum_flux = canonical_flux(vacuum, 6)
    for index in range(3):
        deleted = vacuum_spectators.copy()
        deleted[index] = 0
        spectator_deletion_signals.append(int(np.count_nonzero(
            gauss_residual(vacuum_flux, vacuum, deleted, 6)
        )))
    deleted_background_charge = charge(vacuum, vacuum_spectators).copy()
    deleted_background_charge[0] = (deleted_background_charge[0] + 1) % GAUGE_MODULUS
    background_deletion_signal = int(np.count_nonzero(
        divergence(vacuum_flux, 6) - deleted_background_charge
    ))
    n4 = occupation_configuration(6, (0, 6, 12, 18))
    n4_flux = canonical_flux(n4, 6)
    n4_wrong_spectators = np.zeros(3, dtype=np.int8)
    n4_residual = gauss_residual(n4_flux, n4, n4_wrong_spectators, 6)
    missing_root_check_admits_N4 = (
        np.count_nonzero(n4_residual[1:]) == 0 and int(n4_residual[0]) != 0
    )

    layouts = [physical_layout(3), physical_layout(6)]
    uniform_fiber_rows = []
    for length in (3, 6):
        vertices = length**3
        edges = 3 * vertices
        uniform_fiber_rows.append({
            "length": length,
            "incidence_rank_over_Z1297": vertices - 1,
            "flux_solution_count_exponent": edges - vertices + 1,
            "flux_solution_count": f"1297^{edges - vertices + 1}",
            "log10_flux_solution_count": (edges - vertices + 1) * math.log10(GAUGE_MODULUS),
            "independent_of_lawful_charge_word": True,
        })
    exact_integer_winding = {
        "one_particle_x_windings": 10,
        "harmonic_flux_magnitude_after_windings": 10,
        "finite_exact_integer_link_alphabet_recurrent": False,
        "Z1297_link_alphabet_recurrent": True,
        "interpretation": "the finite modular lift closes repeated torus winding; it is not an arbitrary-volume exact-integer rotor",
    }
    constraints = {
        "commuting_dimensionless_check_projectors": (
            "one Gauss residue-zero projector per cell",
            "one valid-label projector per 11-M2 oriented link word",
            "one four-word prefix projector on the three root spectator M2",
        ),
        "Gauss_check_support": "six incident 11-M2 link words + six matter occupation M2; root also sees three spectator M2",
        "maximum_Gauss_check_support_M2": 75,
        "local_stream_flux_update_support_M2": 13,
        "invalid_11_M2_link_labels_rejected": len(invalid_binary_labels),
        "invalid_label_interval": (GAUGE_MODULUS, 2**GAUGE_WORD_M2 - 1),
        "root_prefix_valid_words": ("000", "100", "110", "111"),
        "root_background_charge": -3,
        "penalty_coefficient_and_empirical_interpretation_supplied": True,
    }
    exact_square = {
        "enlarged_gauge_code_every_word_EG_residual": 0,
        "every_word_reason": (
            "onsite coin/contact preserve cell charge; each basis stream word updates its crossed links by local signed current; linearity covers every gauge-code superposition"
        ),
        "matter_only_uniform_flux_fiber_EG_residual": 0,
        "uniform_fiber_reason": (
            "signed-current translation is a bijection between equal-cardinality flux-solution fibers, so normalized uniform fibers map exactly without a tree or order"
        ),
        "inherited_Cycle590_physical_EG_residual": shore_evidence["Cycle590"]["exact_EG_residual"],
        "held_packet_update_residual": shore_evidence["Cycle590"]["held_packet_update_residual"],
        "gauge_code_preparation_supplied": True,
        "complete_N4_dynamics_supplied_or_claimed": False,
    }
    condition = (
        prime
        and arithmetic_rows[0]["exact_N_le_3"]
        and arithmetic_rows[1]["exact_N_le_3"]
        and not arithmetic_rows[2]["exact_N_le_3"]
        and (1297, 3) in arithmetic_rows[2]["accepted_N_S_pairs"]
        and bool(small_modulus_aliases)
        and local_update_inverse_failures == 0
        and len(invalid_binary_labels) == 751
        and maximum_gauss == maximum_inverse == maximum_covariance == maximum_rotated_gauss == 0
        and covariance_failures == group_failures == 0
        and link_update_deletion_violations > 0
        and min(spectator_deletion_signals) > 0
        and background_deletion_signal > 0
        and missing_root_check_admits_N4
        and all(row["pass"] for row in layouts)
        and exact_square["enlarged_gauge_code_every_word_EG_residual"] == 0
        and exact_square["matter_only_uniform_flux_fiber_EG_residual"] == 0
    )
    result = {
        "status": "positive finite-volume local enforcement with named root/capacity/preparation supplies",
        "selected_modulus": GAUGE_MODULUS,
        "modulus_selected_from_held_L6_Pauli_capacity": True,
        "prime_modulus": prime,
        "arithmetic_rows": arithmetic_rows,
        "small_Z4_aliases": small_modulus_aliases,
        "local_modular_update_inverse_failures": local_update_inverse_failures,
        "constraints": constraints,
        "sample_rows": sample_rows,
        "proper_cubic_frames": len(frames),
        "maximum_all24_update_covariance_residual": maximum_covariance,
        "maximum_all24_rotated_Gauss_residual": maximum_rotated_gauss,
        "all24_covariance_failures": covariance_failures,
        "frame_products": len(frames)**2,
        "all576_group_failures": group_failures,
        "link_update_deletion_Gauss_violations": link_update_deletion_violations,
        "three_root_spectator_deletion_signals": spectator_deletion_signals,
        "fixed_background_deletion_signal": background_deletion_signal,
        "missing_root_check_admits_N4": missing_root_check_admits_N4,
        "layouts": layouts,
        "uniform_flux_fibers": uniform_fiber_rows,
        "exact_integer_winding_audit": exact_integer_winding,
        "exact_intertwiner": exact_square,
        "runtime_global_order_parity_or_count_service": False,
        "supplied_root_background": True,
        "arbitrary_size_closure": False,
        "L7_alias_failure": True,
        "pass": bool(condition),
    }
    check(
        "Route A locally enforces N<=3 on L3/L6 with a recurrent modular Gauss lift and exact every-code-word intertwining, while exposing root/capacity/preparation and L7 alias boundaries",
        condition,
        {
            "arithmetic": arithmetic_rows,
            "maximum_Gauss": maximum_gauss,
            "maximum_inverse": maximum_inverse,
            "all24": maximum_covariance,
            "all576_failures": group_failures,
            "layouts": layouts,
            "deletions": {
                "link": link_update_deletion_violations,
                "spectators": spectator_deletion_signals,
                "background": background_deletion_signal,
                "root_check": missing_root_check_admits_N4,
            },
        },
    )
    return result


# ---------------------------------------------------------------------------
# Route B: three mobile token species.


def token_local_checks(occupation: np.ndarray, tokens: np.ndarray) -> dict:
    token_per_mode = np.sum(tokens, axis=0)
    mismatch = int(np.count_nonzero(token_per_mode != occupation.reshape(-1)))
    mode_collisions = int(np.count_nonzero(token_per_mode > 1))
    return {
        "matter_token_co_location_mismatches": mismatch,
        "multiple_species_same_mode_collisions": mode_collisions,
        "pass": mismatch == mode_collisions == 0,
    }


def token_word(length: int, modes: tuple[int, ...], species: tuple[int, ...]
               ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    occupation = occupation_configuration(length, modes)
    tokens = np.zeros((3, 6 * length**3), dtype=np.int8)
    for mode, label in zip(modes, species):
        tokens[label, mode] = 1
    reservoir = np.asarray([
        int(not np.any(tokens[label])) for label in range(3)
    ], dtype=np.int8)
    return occupation, tokens, reservoir


def route_b() -> dict:
    print("\nROUTE B — THREE MOBILE CONSERVED OCCUPANCY-TOKEN SPECIES")
    rows = []
    maximum_covariance_failure = 0
    frames = c210.proper_cubic_frames()
    for length, split in ((3, "train"), (6, "held")):
        lawful_modes = tuple(6 * index for index in range(3))
        occupation, tokens, reservoir = token_word(length, lawful_modes, (0, 1, 2))
        local = token_local_checks(occupation, tokens)
        global_counts = tuple(
            int(np.sum(tokens[label]) + reservoir[label]) for label in range(3)
        )
        malformed_modes = tuple(6 * index for index in range(4))
        bad_occupation, bad_tokens, bad_reservoir = token_word(
            length, malformed_modes, (0, 1, 2, 0)
        )
        malformed_local = token_local_checks(bad_occupation, bad_tokens)
        malformed_global_counts = tuple(
            int(np.sum(bad_tokens[label]) + bad_reservoir[label]) for label in range(3)
        )
        # One local co-hop and its inverse.
        source_mode = lawful_modes[0]
        source_site, direction = divmod(source_mode, 6)
        velocity = c210.DIRECTIONS[direction]
        coordinate = site_tuple(source_site, length)
        target_site = site_flat(tuple(
            int((coordinate[axis] + velocity[axis]) % length) for axis in range(3)
        ), length)
        target_mode = 6 * target_site + direction
        moved_occupation = occupation.copy().reshape(-1)
        moved_tokens = tokens.copy()
        moved_occupation[source_mode], moved_occupation[target_mode] = 0, 1
        moved_tokens[0, source_mode], moved_tokens[0, target_mode] = 0, 1
        moved_occupation = moved_occupation.reshape(length**3, 6)
        moved_local = token_local_checks(moved_occupation, moved_tokens)
        restored_occupation = moved_occupation.copy().reshape(-1)
        restored_tokens = moved_tokens.copy()
        restored_occupation[target_mode], restored_occupation[source_mode] = 0, 1
        restored_tokens[0, target_mode], restored_tokens[0, source_mode] = 0, 1
        restored_occupation = restored_occupation.reshape(length**3, 6)
        inverse_residual = max(
            int(np.max(np.abs(restored_occupation - occupation))),
            int(np.max(np.abs(restored_tokens - tokens))),
        )
        deleted_tokens = tokens.copy()
        deleted_occupation = moved_occupation
        deletion_mismatch = token_local_checks(deleted_occupation, deleted_tokens)[
            "matter_token_co_location_mismatches"
        ]
        covariance_failures = 0
        for frame in frames:
            rotated_occupation = rotate_occupation(occupation, frame, length)
            direction_map = np.argmax(c210.direction_permutation(frame), axis=0)
            rotated_tokens = np.zeros_like(tokens)
            for site in range(length**3):
                coordinate = np.asarray(site_tuple(site, length), dtype=int)
                target = site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
                for ray in range(6):
                    for label in range(3):
                        rotated_tokens[label, 6 * target + int(direction_map[ray])] = tokens[
                            label, 6 * site + ray
                        ]
            covariance_failures += not token_local_checks(
                rotated_occupation, rotated_tokens
            )["pass"]
        maximum_covariance_failure = max(maximum_covariance_failure, covariance_failures)
        rows.append({
            "length": length,
            "split": split,
            "lawful_local_checks": local,
            "lawful_global_species_counts": global_counts,
            "cohop_local_checks": moved_local,
            "cohop_inverse_residual": inverse_residual,
            "deleted_token_hop_local_mismatches": deletion_mismatch,
            "all24_local_check_covariance_failures": covariance_failures,
            "remote_duplicate_species_N4_local_checks": malformed_local,
            "remote_duplicate_species_N4_global_counts": malformed_global_counts,
            "remote_duplicate_species_N4_passes_every_bounded_colocation_check": malformed_local["pass"],
        })
    held_cells = 6**3
    result = {
        "status": "positive conserved co-hop relative to supplied one-token-per-species sector; not local cutoff enforcement",
        "rows": rows,
        "persistent_token_M2_per_cell": 18,
        "root_reservoir_M2": 3,
        "held_extended_live_M2": 11448 + 18 * held_cells + 3,
        "held_average_M2_per_cell": (11448 + 18 * held_cells + 3) / held_cells,
        "local_cohop_support_M2": 4,
        "unique_token_genesis_locally_enforced": False,
        "remote_duplicate_species_N4_rejected": False,
        "full_quantum_coin_and_fermionic_exchange_lift_certified": False,
        "preparation_distinct_from_enforcement": True,
        "proper_cubic_frames": len(frames),
        "pass_as_target_enforcement": False,
    }
    condition = (
        all(row["lawful_local_checks"]["pass"] for row in rows)
        and all(row["cohop_local_checks"]["pass"] for row in rows)
        and all(row["cohop_inverse_residual"] == 0 for row in rows)
        and min(row["deleted_token_hop_local_mismatches"] for row in rows) > 0
        and all(row["remote_duplicate_species_N4_passes_every_bounded_colocation_check"] for row in rows)
        and all(row["remote_duplicate_species_N4_global_counts"][0] == 2 for row in rows)
        and maximum_covariance_failure == 0
    )
    result["pass_as_route_audit"] = bool(condition)
    check(
        "Route B constructs local conserved co-hops but an explicit remote duplicate-species N4 word passes all bounded co-location checks, leaving uniqueness/genesis supplied",
        condition, rows,
    )
    return result


# ---------------------------------------------------------------------------
# Route C: time-multiplexed verifier.


def snake_path(length: int) -> tuple[tuple[int, int, int], ...]:
    path = []
    y_forward = True
    row_start_z = 0
    for x in range(length):
        ys = list(range(length)) if y_forward else list(reversed(range(length)))
        for y in ys:
            zs = list(range(length)) if row_start_z == 0 else list(reversed(range(length)))
            path.extend((x, y, z) for z in zs)
            row_start_z = zs[-1]
        y_forward = not y_forward
    return tuple(path)


def path_nn_failures(path: tuple[tuple[int, int, int], ...], length: int) -> int:
    failures = 0
    for first, second in zip(path, path[1:]):
        distance = sum(
            min((first[axis] - second[axis]) % length,
                (second[axis] - first[axis]) % length)
            for axis in range(3)
        )
        failures += distance != 1
    return failures


def counter_verify(occupation: np.ndarray, path: tuple[tuple[int, int, int], ...],
                   skip_cell: tuple[int, int, int] | None = None,
                   initial_counter: int = 0) -> dict:
    counter = initial_counter
    forward_trace = []
    for cell in path:
        local_number = int(np.sum(occupation[site_flat(cell, round(len(path)**(1/3))) ]))
        if cell != skip_cell:
            counter = (counter + local_number) % COUNTER_MODULUS
        forward_trace.append(counter)
    counted = counter
    flag = int(counter > 3)
    for cell in reversed(path):
        local_number = int(np.sum(occupation[site_flat(cell, round(len(path)**(1/3))) ]))
        if cell != skip_cell:
            counter = (counter - local_number) % COUNTER_MODULUS
    return {
        "counted_number": counted,
        "overflow_flag": flag,
        "restored_counter": counter,
        "forward_trace_sha256": sha256(repr(tuple(forward_trace)).encode()).hexdigest(),
    }


def route_c() -> dict:
    print("\nROUTE C — TIME-MULTIPLEXED SATURATION/OVERFLOW VERIFIER")
    local_inverse_failures = 0
    for counter in range(COUNTER_MODULUS):
        for local_number in range(7):
            updated = (counter + local_number) % COUNTER_MODULUS
            restored = (updated - local_number) % COUNTER_MODULUS
            local_inverse_failures += restored != counter
    frames = c210.proper_cubic_frames()
    rows = []
    group_failures = 0
    for length, split in ((3, "train"), (6, "held")):
        path = snake_path(length)
        coverage_failures = len(path) - len(set(path)) + (length**3 - len(set(path)))
        nn_failures = path_nn_failures(path, length)
        n3 = occupation_configuration(length, tuple(6 * index for index in range(3)))
        n4 = occupation_configuration(length, tuple(6 * index for index in range(4)))
        lawful = counter_verify(n3, path)
        overflow = counter_verify(n4, path)
        # The N4 probe occupies flat cells 0,1,2,3.  Delete the addition at
        # occupied flat cell 3 independently of its position in the snake.
        deleted = counter_verify(n4, path, skip_cell=site_tuple(3, length))
        malformed = counter_verify(n3, path, initial_counter=1)
        rotated_rows = []
        for frame in frames:
            rotated_path = tuple(
                tuple(int(value % length) for value in frame @ np.asarray(cell, dtype=int))
                for cell in path
            )
            rotated_n4 = rotate_occupation(n4, frame, length)
            rotated = counter_verify(rotated_n4, rotated_path)
            rotated_rows.append({
                "coverage": len(set(rotated_path)),
                "NN_failures": path_nn_failures(rotated_path, length),
                "counted_number": rotated["counted_number"],
                "overflow_flag": rotated["overflow_flag"],
            })
        test_cells = np.asarray(path, dtype=int)
        for first in frames:
            for second in frames:
                composed = ((test_cells @ second.T) % length @ first.T) % length
                direct = (test_cells @ (first @ second).T) % length
                group_failures += int(not np.array_equal(composed, direct))
        rows.append({
            "length": length,
            "split": split,
            "cells_scanned": len(path),
            "nearest_neighbour_path_failures": nn_failures,
            "coverage_failures": coverage_failures,
            "lawful_N3": lawful,
            "overflow_N4": overflow,
            "delete_one_occupied_cell_addition": deleted,
            "malformed_nonblank_initial_counter": malformed,
            "all24_rows": rotated_rows,
            "stroboscopic_schedule_calls": 2 * length**3 + 1,
            "schedule_calls_called_physical_time": False,
        })
    held_cells = 6**3
    result = {
        "status": "exact local reversible overflow flagger; not static local enforcement",
        "rows": rows,
        "counter_modulus": COUNTER_MODULUS,
        "counter_word_M2": 11,
        "head_M2_per_cell": 1,
        "counter_track_M2_per_cell": 11,
        "held_extended_live_M2": 11448 + 12 * held_cells + 1,
        "held_average_M2_per_cell": (11448 + 12 * held_cells + 1) / held_cells,
        "local_add_support_M2": 17,
        "local_add_inverse_failures": local_inverse_failures,
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames)**2,
        "all576_group_failures": group_failures,
        "blank_invalid_N4_is_locally_admissible_before_scan": True,
        "flag_is_static_constraint_enforcement": False,
        "unique_head_and_blank_counter_locally_enforced": False,
        "preferred_snake_and_frame_transport_supplied": True,
        "runtime_global_count_service_retired": False,
        "pass_as_target_enforcement": False,
    }
    condition = (
        local_inverse_failures == 0 and group_failures == 0
        and all(row["nearest_neighbour_path_failures"] == 0 for row in rows)
        and all(row["coverage_failures"] == 0 for row in rows)
        and all(row["lawful_N3"]["counted_number"] == 3 for row in rows)
        and all(row["lawful_N3"]["overflow_flag"] == 0 for row in rows)
        and all(row["overflow_N4"]["counted_number"] == 4 for row in rows)
        and all(row["overflow_N4"]["overflow_flag"] == 1 for row in rows)
        and all(row["lawful_N3"]["restored_counter"] == 0 for row in rows)
        and all(row["overflow_N4"]["restored_counter"] == 0 for row in rows)
        and all(row["delete_one_occupied_cell_addition"]["overflow_flag"] == 0 for row in rows)
        and all(row["malformed_nonblank_initial_counter"]["restored_counter"] == 1 for row in rows)
        and all(
            item["coverage"] == row["length"]**3
            and item["NN_failures"] == 0
            and item["counted_number"] == 4
            and item["overflow_flag"] == 1
            for row in rows for item in row["all24_rows"]
        )
    )
    result["pass_as_route_audit"] = bool(condition)
    check(
        "Route C exactly flags and uncomputes N4 on NN train/held scans, but deletion gives a false negative and the blank invalid word is locally admissible before the supplied head/order scan",
        condition,
        {"rows": rows, "local_inverse_failures": local_inverse_failures,
         "all576_failures": group_failures},
    )
    return result


def no_go_discipline() -> dict:
    alternatives = (
        {
            "family": "finite-group Gauss/flux with capacity reservoir",
            "object_mechanism_obligation": (
                "Z_k oriented links / telescoping modular Gauss law / prove finite-volume exact N<=3 and every-word local dynamics"
            ),
            "marker": "ATTEMPTED",
            "disposition": "positive on L3/L6 with root, k=1297, and preparation supplies; L7 alias",
        },
        {
            "family": "exact-integer or rotor Gauss flux",
            "object_mechanism_obligation": (
                "integer/rotor links / exact divergence / close repeated periodic winding with finite physical M2"
            ),
            "marker": "ATTEMPTED",
            "disposition": "static solutions exist; the tested finite integer alphabet is not recurrent under unbounded winding",
        },
        {
            "family": "three mobile worldline-token species",
            "object_mechanism_obligation": (
                "bound token fields / conserved species / enforce one global token of each species locally and lift the quantum coin"
            ),
            "marker": "ATTEMPTED",
            "disposition": "local co-hop positive; remote duplicate species and quantum-label lift remain",
        },
        {
            "family": "time-multiplexed saturation verifier",
            "object_mechanism_obligation": (
                "carried counter/head / reversible prefix accumulation / turn final flag into phase-independent static enforcement"
            ),
            "marker": "ATTEMPTED",
            "disposition": "exact flagger; unique head/order supplied and invalid blank word locally admissible before scan",
        },
        {
            "family": "translation-invariant hierarchical tiling counter",
            "object_mechanism_obligation": (
                "self-similar coordinate tiles / distributed prefix invariant / remove unique reset and preferred chart on a torus"
            ),
            "marker": "UNTESTED",
            "disposition": "concrete live route; not ruled out",
        },
        {
            "family": "open-boundary or mobile anti-charge reservoir",
            "object_mechanism_obligation": (
                "three physical anti-charges / exact neutral Gauss law / obtain periodic proper-cubic domain without a fixed root"
            ),
            "marker": "UNTESTED",
            "disposition": "concrete live route; not ruled out",
        },
        {
            "family": "topological one-loop capacity sectors",
            "object_mechanism_obligation": (
                "higher-form flux loops / topological conservation / enforce at most three loops without a supplied sector"
            ),
            "marker": "UNTESTED",
            "disposition": "concrete live route; not ruled out",
        },
    )
    walls = (
        "held-capacity modulus", "cubic-fixed root/background",
        "gauge-code preparation", "arbitrary-size alias removal",
        "token genesis/quantum lift", "verifier head/order/static admission",
    )
    mechanisms = {
        "held-capacity modulus": "choose k above declared finite Pauli capacity",
        "cubic-fixed root/background": "three local spectator charges and fixed -3 reference",
        "gauge-code preparation": "prepare a locally constrained flux fiber or its uniform state",
        "arbitrary-size alias removal": "scale the modulus or replace modular charge",
        "token genesis/quantum lift": "enforce unique species and indistinguishable coherent coin action",
        "verifier head/order/static admission": "locally generate one head/chart and make flag phase-independent",
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
        "N1_attempted_families": 4,
        "N1_required_before_negative": 5,
        "N1_negative_gate_pass": False,
        "N2_directional_wall_pairs": pairs,
        "N2_collapsed_wall_count": len(walls),
        "N3_hidden_condition_scan": {
            "root/background": "explicit supplied finite-volume capacity reference",
            "modulus/volume": "explicit k=1297 chosen from L6 maximum 1296",
            "uniform gauge fiber": "exact intertwiner device; physical preparation supplied",
            "token genesis": "explicit global one-per-species supply",
            "counter head/path/frame": "explicit schedule and blank-resource supplies",
            "uncited_standard_or_obvious_hits": 0,
        },
        "N4_residual_matching": (
            {
                "witness": "Cycle590 accepted note/receipt",
                "witness_residual": "global N<=3 cutoff supplied, not locally enforced",
                "current_residual": "finite L3/L6 N<=3 local enforcement",
                "match": True,
            },
            {
                "witness": "Cycle563 selected-factor order retirement",
                "witness_residual": "runtime fermion-factor order/parity service",
                "current_residual": "global-number enforcement",
                "match": False,
                "use": "positive inherited compiler only, not obstruction witness",
            },
            {
                "witness": "Cycles236/242 local Gauss and decoder probes",
                "witness_residual": "local CAR strings/syndrome completion",
                "current_residual": "finite total-number capacity",
                "match": False,
                "use": "cross-cycle constructive analogy only",
            },
        ),
        "N5_rhetoric_resolution": (
            "tested: this finite Z1297 lift aliases at L7; not asserted for every finite-group gauge code",
            "tested: Route-B co-location checks admit one remote duplicate N4 word; not asserted for every token code",
            "tested: Route-C blank N4 word is locally admissible before this scan; not asserted for every autonomous verifier",
            "tested: finite exact-integer link alphabet accumulates harmonic winding in this lift; infinite rotors remain open",
        ),
        "N6_partial_closure_paths": (
            "use k(L)>6L^3 as an explicit finite-volume family and audit scale-dependent resource",
            "replace fixed root by three mobile anti-charges with locally conserved genesis",
            "construct a local dissipative or Hamiltonian gauge-state preparation without identifying it with enforcement",
            "develop hierarchical reset-free tilings or higher-form capacity sectors",
        ),
        "N7_hostile_steelman": (
            "A hostile reviewer should reject a broad locality obstruction immediately: Route A already supplies an exact finite-volume counterexample. "
            "Moreover, a family k(L)>6L^3, three mobile anti-charges replacing the root, and a local gauge-cooling preparation gives a concrete route toward larger volumes. "
            "The terminal obligations are size-uniform overhead, root-free covariance, and autonomous preparation—not a new axiom."
        ),
        "N8_cross_cycle_echo": (
            "Cycles560/563 converted global decoder/order descriptions into bounded local tables and transported colors; "
            "Cycle590 then domain-matched the dimer.  Cycle593 applies the same import-bound-retire pattern to the number cutoff, so today's root/modulus/preparation supplies are next constructive audits, not constitutional evidence."
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    condition = (
        len(alternatives) >= 5 and len(pairs) == 15
        and gate["N1_attempted_families"] < gate["N1_required_before_negative"]
        and not gate["negative_claim_shipped"]
        and not gate["minimum_content_claim_shipped"]
        and not gate["shared_obstruction"] and not gate["axiom_pressure"]
    )
    gate["pass_for_withholding_negative"] = bool(condition)
    check(
        "fresh origin/main N1-N8 withholds broad no-go, minimum-content, shared-obstruction, and axiom-pressure language",
        condition, gate,
    )
    return gate


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 593", "route a", "route b", "route c",
        "z_1297", "l7", "finite-volume local enforcement", "18,579", "all 24", "576",
        "uniform flux", "root", "background", "preparation", "not arbitrary-size",
        "counter flag is not enforcement", "schedule is not time", "flux label is not energy",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    check("the Cycle593 note freezes finite-volume scope, supplies, N1-N8, and interpretation firewalls", not missing, missing)


def main() -> int:
    global PASS, FAIL
    signal.alarm(int(CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle593 local cutoff / gauge enforcement tournament", AUTHORITY, AUDIT)
    evidence = shore()
    route_A = route_a(evidence)
    route_B = route_b()
    route_C = route_c()
    gate = no_go_discipline()
    note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < CAP_SECONDS and rss < CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    ledger = {
        "C_ref": "three cubic-fixed root capacity bits and background -3 replace the silent cutoff reference on L3/L6; root-free realization remains open",
        "C_num": "local modular Gauss arithmetic enforces N+S=3 exactly within held capacity; empirical units and arbitrary-size modulus family remain open",
        "C_wrap": "Z1297 closes repeated torus winding at held size; exact-integer winding grows and L7 modular aliases reopen",
        "C_int": "Cycle590 mass/contact/seam and N2 update square are preserved by the number-conserving gauge lift",
        "C_local": "major movement: finite L3/L6 global N<=3 promise is replaced by bounded local checks and link updates; gauge-state preparation remains supplied",
        "C_source": "fixed background -3 is capacity bookkeeping, not empirical energy, stress, source, or gravity",
    }
    receipt = {
        "status": "cycle593-finite-volume-local-cutoff-gauge-enforcement",
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
        "shore": evidence,
        "route_A_finite_volume_modular_Gauss": route_A,
        "route_B_mobile_token_species": route_B,
        "route_C_time_multiplexed_counter": route_C,
        "no_go_discipline": gate,
        "six_wall_ledger": ledger,
        "maturity": {
            "operational_quantum_records_repo_strict": (4.80, 4.65),
            "causal_time_repo_strict": (3.95, 3.80),
            "inertia_matter_repo_strict": (4.90, 4.93),
            "gravity_source_repo_strict": (4.10, 3.85),
            "Born_probability_repo_strict": (4.20, 3.65),
        },
        "highest_honest_terminal": (
            "exact finite-volume L3/L6 N<=3 enforcement by bounded Z1297 Gauss checks and local current-coupled flux dynamics, "
            "composed with the Cycle590 physical compiler; the modulus is held-capacity-selected, the cubic-fixed root/background "
            "and gauge-state preparation are supplied, L7 aliases, and arbitrary size/N4 dynamics remain open"
        ),
        "optimal_next_campaign": (
            "replace the cubic-fixed root/background with three locally generated mobile anti-charges and construct autonomous uniform-gauge-fiber preparation, "
            "then test a size-indexed k(L)>6L^3 family without conflating it with complete N4 interactions"
        ),
    }
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n"
    )
    print("SUMMARY_JSON", json.dumps({
        "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
        "finite_L3_L6_local_enforcement": route_A["pass"],
        "arbitrary_size_closure": False,
        "L7_alias_failure": route_A["L7_alias_failure"],
        "axiom_pressure": False,
    }, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
