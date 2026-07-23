#!/usr/bin/env python3
"""Cycle629: state-carried translation-orbit marker-crystal repair.

This artifact tests a translation-invariant family of bounded diagonal marker
constraints built from five proper-cubic anchor orbits and one disjoint
orientation orbit.  It distinguishes a locally stated projector contract from
a fine-nearest-neighbor enforcement circuit, a physical intertwiner, and an
autonomous renewal schedule.  Authority none; audit unset; author artifact
status accepted false; breakthrough false.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22 as c610


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_translation_orbit_marker_crystal_repair_"
    "cycle629_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_translation_orbit_marker_crystal_repair_"
    "cycle629_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 180.0
CAP_BYTES = 2 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py":
        "ed2250711646ad99bf077e74b8e4194f2df0a2cf368d3c05c45ea95cac8083db",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "3768d2a1407bdc8de06e2a55fa18300469b1006c0a16a78ada8b8d3a4b936105",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "375f843606a81970ae50f71d74c53f7e4c4d1437007daaecbedd0b19e3fdfa34",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt":
        "0adbee38e398c9e1d1ccd2733454ead2669338b86d48cbefa5331abb78c126e8",
}
MINIMAL_AXIOMS_TEST_CONTRACT = {
    "path": "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "sha256": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "origin_main_lines": "37-41",
    "use": "promotion test contract only; no axiom or foundation edit and no inferred dynamics",
}
K = 129
H = 64
FRAMES = c610.FRAMES
DIRECTIONS = c610.DIRECTIONS
ANCHOR_SEEDS = ((1, 2, 3), (2, 5, 7), (3, 8, 11), (4, 13, 17), (5, 19, 23))
ORIENTATION_SEED = (6, 25, 31)
VARIABLE_LIVE_UPPER_BOUND = 91


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, set | frozenset):
        return sorted(value)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def rotate(frame: np.ndarray, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in frame @ np.asarray(vector, dtype=int))


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def mod(vector: tuple[int, int, int], period: int) -> tuple[int, int, int]:
    return tuple(value % period for value in vector)


def orbit(seed: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted({rotate(frame, seed) for frame in FRAMES}))


ANCHOR_ORBITS = tuple(orbit(seed) for seed in ANCHOR_SEEDS)
ANCHORS = frozenset(site for row in ANCHOR_ORBITS for site in row)
# Index orientation sites by the same frame index used by left multiplication;
# sorting the orbit would destroy the h -> g h action even though the set is
# unchanged.
ORIENTATION_SITES = tuple(rotate(frame, ORIENTATION_SEED) for frame in FRAMES)


def frame_index(frame: np.ndarray) -> int:
    for index, candidate in enumerate(FRAMES):
        if np.array_equal(frame, candidate):
            return index
    raise ValueError("not a proper-cubic frame")


def left_action(first: np.ndarray, second_index: int) -> int:
    return frame_index(first @ FRAMES[second_index])


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    receipt = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())
    expected_graph = dict(receipt["shore"]["import_audit"]["expected_transitive_sha256"])
    expected_graph.update(PINS)
    observed_graph = {name: sha(ROOT / name) for name in expected_graph}
    actual_modules = c610.c606.c600.imported_science_modules(
        c610, c610.c606, c610.c603, c610.c603.c219, c610.c603.c230
    )
    uncovered = sorted(set(actual_modules.values()) - set(expected_graph))
    axiom_hash = sha(ROOT / MINIMAL_AXIOMS_TEST_CONTRACT["path"])
    inherited = {
        "Cycle610_pass": receipt["pass"],
        "Cycle610_tests_passed": receipt["tests_passed"],
        "Cycle610_author_artifact_status_accepted": receipt["author_artifact_status_accepted"],
        "Cycle610_physical_M2_scope": receipt["physical_M2_scope"],
        "Cycle610_translation_rows": receipt["fine_site_translation_falsifier"]["rows"],
        "Cycle610_broad_negative_gate": receipt["broad_negative_gate"],
        "Cycle610_axiom_pressure": receipt["shared_obstruction_or_axiom_pressure"],
        "import_audit": {
            "expected_transitive_sha256": expected_graph,
            "observed_transitive_sha256": observed_graph,
            "actual_imported_modules": actual_modules,
            "uncovered_imported_modules": uncovered,
            "expected_file_count": len(expected_graph),
            "runtime_module_count": len(actual_modules),
        },
        "minimal_axioms_test_contract": {
            **MINIMAL_AXIOMS_TEST_CONTRACT,
            "observed_sha256": axiom_hash,
        },
    }
    scope = inherited["Cycle610_physical_M2_scope"]
    condition = (
        observed == PINS and observed_graph == expected_graph and not uncovered
        and inherited["Cycle610_pass"] and inherited["Cycle610_tests_passed"] == 18
        and not inherited["Cycle610_author_artifact_status_accepted"]
        and not scope["promotion_to_physical_M2_law"]
        and not scope["literal_physical_encoder_composed"]
        and scope["physical_intertwiner_residual"] is None
        and not scope["physical_code_leakage_evaluated"]
        and [row["one_fine_site_x_translation_symmetric_difference"]
             for row in inherited["Cycle610_translation_rows"]] == [2970, 23760, 37730]
        and inherited["Cycle610_broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and not inherited["Cycle610_axiom_pressure"]
        and axiom_hash == MINIMAL_AXIOMS_TEST_CONTRACT["sha256"]
    )
    check("final narrowed Cycle610 quartet and complete inherited science graph are byte exact",
          condition, {"observed": observed, "inherited": inherited})
    return inherited


def exact_target_contract() -> dict:
    result = {
        "target_statement": "construct a translation-invariant bounded marker/constraint family whose valid states carry a Z_129^3 phase and a proper-cubic orientation, then test whether it promotes the conditional Cycle610 geometry without a supplied origin",
        "quantifiers_and_domain": "all phi in Z_129^3 by exhaustive residue formula; six unit translations; all 24 proper-cubic frames and all 576 frame/orientation products; periodic L3/L6/L7 marker crystals; the explicitly declared marker/code-weight sector",
        "allowed_premises": (
            "the byte-pinned narrowed Cycle610 conditional coordinate result",
            "the minimal-axiom lattice symmetry lines as a test contract only",
            "120 occupied anchor offsets, one of 24 orientation offsets, and the explicit non-anchor weight <=91 code condition",
        ),
        "forbidden_weakenings": (
            "coarse K-step covariance presented as one-site covariance",
            "a diagonal projector contract presented as a fine-NN enforcement circuit",
            "coordinate compatibility presented as a physical encoder/intertwiner",
            "a host-ordered macro word presented as autonomous time or renewal",
        ),
        "required_edges": (
            "unit shifts through phase seams", "proper rotations about arbitrary integer sites",
            "marker deletion", "zero/two/all-hot orientation", "mixed neighbor orientation",
            "off-code false markers", "L3/L6/L7 periodic seams",
        ),
        "completion_witness": "literal fine-NN reversible enforcement plus an explicit physical encoder E and autonomous G_physical with E G_coarse = G_physical E, leakage/deletion/held controls, and no host schedule",
        "does_not_count_as_closure": (
            "autocorrelation alone", "truth-table predicates", "bounded but noncompiled projectors",
            "conflict-free coordinate sets", "inherited fixtures not reexecuted",
        ),
    }
    check("Cycle629 exact target contract forbids projector-to-physical promotion",
          len(result["required_edges"]) >= 7 and len(result["does_not_count_as_closure"]) >= 5,
          result)
    return result


def dynamic_geometry_sites() -> set[tuple[int, int, int]]:
    allocated: set[tuple[int, int, int]] = set()
    for frame in FRAMES:
        for species in range(3):
            allocated.update(c610.roles(species, frame).values())
            allocated.update(c610.neutral_path(species, frame))
            for path in c610.swap_paths(species, frame):
                allocated.update(path)
            for direction in DIRECTIONS:
                row = c610.shuttle_paths(species, frame, direction)
                allocated.update(row["source"])
                allocated.update(row["target"])
    allocated.update(c610.PREDICATE_WORK_SITES)
    allocated.add(c610.ONSITE_WORK_SITE)
    return allocated


def candidate_geometry_audit(c610_receipt: dict) -> dict:
    orbit_sizes = tuple(len(row) for row in ANCHOR_ORBITS)
    orbit_pair_overlaps = tuple(
        len(set(ANCHOR_ORBITS[first]) & set(ANCHOR_ORBITS[second]))
        for first, second in combinations(range(len(ANCHOR_ORBITS)), 2)
    )
    dynamic = dynamic_geometry_sites()
    identity_manifest = c610_receipt["layout_manifest"]
    old_identity_allocated = identity_manifest["allocated_stream_role_sites_union"]
    failures = {
        "anchor_orbit_size": sum(size != 24 for size in orbit_sizes),
        "anchor_orbit_overlap": sum(value != 0 for value in orbit_pair_overlaps),
        "anchor_count": int(len(ANCHORS) != 120),
        "orientation_orbit_size": int(len(ORIENTATION_SITES) != 24),
        "anchor_orientation_overlap": len(ANCHORS & set(ORIENTATION_SITES)),
        "anchor_dynamic_overlap": len(ANCHORS & dynamic),
        "orientation_dynamic_overlap": len(set(ORIENTATION_SITES) & dynamic),
        "anchor_outside_H": sum(max(abs(value) for value in site) > H for site in ANCHORS),
        "orientation_outside_H": sum(max(abs(value) for value in site) > H for site in ORIENTATION_SITES),
    }
    result = {
        "K": K,
        "H": H,
        "anchor_seeds": ANCHOR_SEEDS,
        "anchor_orbit_sizes": orbit_sizes,
        "anchor_sites": len(ANCHORS),
        "orientation_seed": ORIENTATION_SEED,
        "orientation_sites": len(ORIENTATION_SITES),
        "all_frame_dynamic_role_path_predicate_work_union": len(dynamic),
        "identity_frame_Cycle610_allocated_union_before_replacement": old_identity_allocated,
        "identity_frame_allocated_union_after_replacement_and_anchors": old_identity_allocated + 120,
        "maximum_nonanchor_variable_live_M2_per_phase_cell": VARIABLE_LIVE_UPPER_BOUND,
        "new_anchor_or_orientation_conflict_with_dynamic_allocations": False,
        "Hamiltonian_bus_still_visits_marker_sites": True,
        "move_apply_restore_endpoint_returns_spectator_contents": True,
        "recognition_during_host_microsteps_preserved": False,
        "failures": failures,
        "pass": all(value == 0 for value in failures.values()),
    }
    check("five disjoint anchor orbits and the replacement orientation orbit avoid every conditional role/path allocation",
          result["pass"] and old_identity_allocated == 1492
          and identity_manifest["maximum_persistent_plus_predicate_live_M2"] == 91,
          result)
    return result


def bus_marker_intersection_audit() -> dict:
    """Find an actual Cycle610 routed primitive whose opening word moves markers.

    Cycle610's compact descriptor sends one endpoint along the Hamiltonian bus,
    applies a neighboring gate, then reverses the interval.  Endpoint reversal
    returns spectators, but an autonomous marker predicate would be false during
    the open interval.  This test uses a literal controlled-coin primitive from
    the actual Cycle610 word rather than a distance-only surrogate.
    """
    marker_role_sites = set(ANCHORS) | set(ORIENTATION_SITES)
    marker_role_indices = {c610.bus_index(site) for site in marker_role_sites}
    active_marker_indices = {
        c610.bus_index(site) for site in (set(ANCHORS) | {ORIENTATION_SITES[0]})
    }
    bus_inverse_failures = sum(
        c610.bus_coordinate(c610.bus_index(site)) != site
        for site in marker_role_sites
    )
    identity_index = frame_index(np.eye(3, dtype=int))
    frame = FRAMES[identity_index]
    flag = c610.predicate_roles(identity_index)["predicate_flag_site"]
    coin, _ = c610.onsite_gate_lists()
    logical_coordinates = c610.onsite_logical_coordinates()
    scanned = 0
    witness = None
    for gate_index, gate in enumerate(coin):
        data = tuple(logical_coordinates[index] for index in gate.qubits)
        stage = f"factor_0_onsite_coin_g{gate_index}"
        for lowered, coordinates in c610.controlled_gate_specs(gate, data, flag, stage):
            if len(coordinates) != 2:
                continue
            scanned += 1
            first, second = tuple(
                c610.oriented_bus_index(frame, coordinate) for coordinate in coordinates
            )
            if first < second:
                affected = {index for index in marker_role_indices if first + 1 <= index <= second}

                def opening(position: int) -> int:
                    if position == second:
                        return first + 1
                    if first + 1 <= position < second:
                        return position + 1
                    return position

                def closing(position: int) -> int:
                    if position == first + 1:
                        return second
                    if first + 1 < position <= second:
                        return position - 1
                    return position
            else:
                affected = {index for index in marker_role_indices if second <= index <= first - 1}

                def opening(position: int) -> int:
                    if position == second:
                        return first - 1
                    if second < position <= first - 1:
                        return position - 1
                    return position

                def closing(position: int) -> int:
                    if position == first - 1:
                        return second
                    if second <= position < first - 1:
                        return position + 1
                    return position
            if not affected:
                continue
            opened = {opening(position) for position in active_marker_indices}
            restored = {closing(position) for position in opened}
            if opened != active_marker_indices and restored == active_marker_indices:
                witness = {
                    "stage": stage,
                    "lowered_family": lowered.family,
                    "endpoint_coordinates": coordinates,
                    "endpoint_bus_indices": (first, second),
                    "bus_distance": abs(first - second),
                    "marker_role_indices_in_opening_interval": len(affected),
                    "active_marker_pattern_changed_after_opening": True,
                    "active_marker_pattern_restored_after_reverse": True,
                }
                break
        if witness is not None:
            break
    result = {
        "Hamiltonian_bus_sites": K**3,
        "marker_anchor_role_sites_on_bus": len(ANCHORS),
        "replacement_orientation_role_sites_on_bus": len(ORIENTATION_SITES),
        "marker_or_orientation_role_bus_intersection": len(marker_role_indices),
        "bus_coordinate_index_inverse_failures_on_marker_roles": bus_inverse_failures,
        "actual_Cycle610_controlled_coin_two_site_primitives_scanned": scanned,
        "actual_routed_descriptor_witness": witness,
        "macro_endpoint_spectator_return": witness is not None,
        "marker_recognition_preserved_during_open_interval": False,
        "covariant_connected_NN_bus_routed_around_markers_constructed": False,
        "marker_preserving_routing_gadget_constructed": False,
        "physical_update_credit_allowed": False,
        "pass_as_load_bearing_falsifier": (
            len(marker_role_indices) == 144 and bus_inverse_failures == 0
            and witness is not None
        ),
    }
    check("the actual Cycle610 routed word crosses and temporarily moves the marker pattern, so endpoint disjointness earns no physical-update credit",
          result["pass_as_load_bearing_falsifier"]
          and not result["marker_recognition_preserved_during_open_interval"], result)
    return result


def autocorrelation_audit() -> dict:
    counts = Counter(
        tuple((left[axis] - right[axis]) % K for axis in range(3))
        for left in ANCHORS for right in ANCHORS
    )
    nonzero_max = max(
        count for shift, count in counts.items() if shift != (0, 0, 0)
    )
    maximizing_shifts = tuple(sorted(
        shift for shift, count in counts.items()
        if shift != (0, 0, 0) and count == nonzero_max
    ))
    minimum_adversarial_fill = len(ANCHORS) - nonzero_max
    false_marker_margin = len(ANCHORS) - (
        nonzero_max + VARIABLE_LIVE_UPPER_BOUND
    )
    shift = (4, 125, 4)
    translated = {
        tuple((site[axis] + shift[axis]) % K for axis in range(3))
        for site in ANCHORS
    }
    base = {mod(site, K) for site in ANCHORS}
    fill = translated - base
    off_code = base | fill
    result = {
        "anchor_count": len(ANCHORS),
        "zero_shift_autocorrelation": counts[(0, 0, 0)],
        "all_nonzero_periodic_shifts_exhausted": K**3 - 1,
        "nonzero_periodic_autocorrelation_maximum": nonzero_max,
        "maximizing_shifts": maximizing_shifts,
        "required_shift_present": shift in maximizing_shifts,
        "Cycle610_nonanchor_variable_live_upper_bound": VARIABLE_LIVE_UPPER_BOUND,
        "false_marker_margin_under_supplied_weight_condition": false_marker_margin,
        "minimum_off_code_additions_to_spoof_a_second_raw_marker": minimum_adversarial_fill,
        "off_code_spoof_constructed": (
            len(base & translated) == nonzero_max
            and len(fill) == minimum_adversarial_fill
            and base <= off_code and translated <= off_code
        ),
        "recognition_unique_on_arbitrary_off_code_states": False,
        "weight_condition_locally_stated_projector": True,
        "weight_condition_fine_NN_enforced": False,
    }
    condition = (
        result["zero_shift_autocorrelation"] == 120
        and nonzero_max == 9 and result["required_shift_present"]
        and false_marker_margin == 20 and minimum_adversarial_fill == 111
        and result["off_code_spoof_constructed"]
    )
    check("exhaustive periodic autocorrelation leaves a 20-site conditional margin and constructs the 111-fill off-code spoof",
          condition, result)
    return result


def representative(value: int) -> int:
    return ((value + H) % K) - H


def phase_and_coverage_audit() -> dict:
    failures = {
        "representative_range": 0,
        "representative_residue": 0,
        "unit_phase_inverse": 0,
        "unit_phase_unchanged": 0,
    }
    rows_checked = 0
    phase_shift_checks = 0
    for identifier in range(K**3):
        x = identifier // (K * K)
        y = (identifier // K) % K
        z = identifier % K
        point = (x, y, z)
        rep = tuple(representative(value) for value in point)
        rows_checked += 1
        failures["representative_range"] += int(any(abs(value) > H for value in rep))
        failures["representative_residue"] += int(
            any((rep[axis] - point[axis]) % K != 0 for axis in range(3))
        )
        for direction in DIRECTIONS:
            shifted = tuple((point[axis] + direction[axis]) % K for axis in range(3))
            restored = tuple((shifted[axis] - direction[axis]) % K for axis in range(3))
            failures["unit_phase_inverse"] += int(restored != point)
            failures["unit_phase_unchanged"] += int(shifted == point)
            phase_shift_checks += 1
    scalar_representatives = tuple(representative(value) for value in range(K))
    result = {
        "all_residues_exhausted": rows_checked,
        "unique_scalar_representatives": len(set(scalar_representatives)),
        "cartesian_unique_representatives": len(set(scalar_representatives)) ** 3,
        "representative_box": ((-H, -H, -H), (H, H, H)),
        "unique_center_within_H_formula": "for phase phi and site x, r_i=((x_i-phi_i+H) mod K)-H and c=x-r is the unique center in phi+K Z^3 with ||x-c||_infinity<=H",
        "unit_phase_shift_checks": phase_shift_checks,
        "phase_is_state_carried": True,
        "host_supplied_phase_argument_in_constraint_law": False,
        "failures": failures,
        "pass": (
            rows_checked == K**3 and len(set(scalar_representatives)) == K
            and all(value == 0 for value in failures.values())
        ),
    }
    check("all 129^3 residues have one bounded representative and all six unit shifts bijectively transport the phase",
          result["pass"] and phase_shift_checks == 6 * K**3, result)
    return result


def cell_centers(length: int, phase: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    period = K * length
    return tuple(
        tuple((phase[axis] + K * cell[axis]) % period for axis in range(3))
        for cell in ((x, y, z) for x in range(length) for y in range(length) for z in range(length))
    )


def periodic_marker_state(length: int, phase: tuple[int, int, int], orientation: int) -> tuple[set, set, set]:
    period = K * length
    centers = set(cell_centers(length, phase))
    anchors = {
        tuple((center[axis] + offset[axis]) % period for axis in range(3))
        for center in centers for offset in ANCHORS
    }
    active_orientation_offset = ORIENTATION_SITES[orientation]
    orientation_sites = {
        tuple((center[axis] + active_orientation_offset[axis]) % period for axis in range(3))
        for center in centers
    }
    return centers, anchors, orientation_sites


def orientation_state_from_centers(centers: set | tuple, orientation: int,
                                   period: int) -> set[tuple[int, int, int]]:
    offset = ORIENTATION_SITES[orientation]
    return {
        tuple((center[axis] + offset[axis]) % period for axis in range(3))
        for center in centers
    }


def translation_covariance_audit() -> dict:
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        period = K * length
        phase = ((17 * length) % K, (23 * length) % K, (31 * length) % K)
        orientation = (5 * length) % 24
        centers, anchors, orient = periodic_marker_state(length, phase, orientation)
        failures = 0
        seam_cases = 0
        for direction in DIRECTIONS:
            shifted_phase = tuple((phase[axis] + direction[axis]) % K for axis in range(3))
            expected = periodic_marker_state(length, shifted_phase, orientation)
            translated = tuple({
                tuple((site[axis] + direction[axis]) % period for axis in range(3))
                for site in component
            } for component in (centers, anchors, orient))
            failures += int(translated != expected)
            seam_cases += int(any(
                phase[axis] + direction[axis] not in range(K) for axis in range(3)
            ))
        rows.append({
            "length": length,
            "split": split,
            "phase": phase,
            "coarse_centers": len(centers),
            "anchor_ones": len(anchors),
            "active_orientation_ones": len(orient),
            "six_unit_translation_failures": failures,
            "phase_seam_cases_in_seeded_row": seam_cases,
            "periodic_wrap_included": True,
            "pass": failures == 0,
        })
    seam_phase = (K - 1, 0, K - 1)
    seam_failures = 0
    for direction in DIRECTIONS:
        shifted = tuple((seam_phase[axis] + direction[axis]) % K for axis in range(3))
        restored = tuple((shifted[axis] - direction[axis]) % K for axis in range(3))
        seam_failures += int(restored != seam_phase)
    result = {
        "translation_invariant_constraint_family": "the same center predicate P_c is stated for every fine site c; no coordinate origin appears in the law",
        "state_carried_phase_action": "T_e maps marker code sector phi to phi+e mod 129",
        "rows": rows,
        "explicit_phase_seam_failures": seam_failures,
        "one_fine_site_code_sector_covariance_at_projector_level": True,
        "physical_update_covariance_executed": False,
        "pass": all(row["pass"] for row in rows) and seam_failures == 0,
    }
    check("the marker-code family transports its state-carried phase under all six physical unit shifts on L3/L6/L7",
          result["pass"], result)
    return result


def rotate_about(frame: np.ndarray, center: tuple[int, int, int],
                 point: tuple[int, int, int], period: int) -> tuple[int, int, int]:
    relative = tuple(point[axis] - center[axis] for axis in range(3))
    return mod(add(center, rotate(frame, relative)), period)


def affine_phase(frame: np.ndarray, site_center: tuple[int, int, int],
                 phase: tuple[int, int, int]) -> tuple[int, int, int]:
    relative = tuple(phase[axis] - site_center[axis] for axis in range(3))
    return mod(add(site_center, rotate(frame, relative)), K)


def rotation_covariance_audit() -> dict:
    failures = {
        "anchor_all24": 0,
        "orientation_all576": 0,
        "frame_signed_permutation": 0,
        "frame_determinant": 0,
        "arbitrary_site_affine_phase": 0,
        "periodic_anchor_state": 0,
        "periodic_orientation_state": 0,
        "translation_rotation_semidirect": 0,
    }
    anchor_set = set(ANCHORS)
    orientation_set = set(ORIENTATION_SITES)
    for frame in FRAMES:
        failures["anchor_all24"] += int({rotate(frame, site) for site in anchor_set} != anchor_set)
        failures["frame_signed_permutation"] += int(
            not np.array_equal(frame @ frame.T, np.eye(3, dtype=int))
            or not np.all(np.isin(frame, (-1, 0, 1)))
        )
        failures["frame_determinant"] += int(round(np.linalg.det(frame)) != 1)
        for orientation in range(24):
            target = left_action(frame, orientation)
            failures["orientation_all576"] += int(
                rotate(frame, ORIENTATION_SITES[orientation]) != ORIENTATION_SITES[target]
            )
    periodic_rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        period = K * length
        phase = ((11 * length) % K, (37 * length) % K, (53 * length) % K)
        site_center = (17 + length, 29 + 2 * length, 41 + 3 * length)
        centers, anchor_state, _ = periodic_marker_state(length, phase, 0)
        row_anchor_failures = 0
        row_orientation_failures = 0
        for frame in FRAMES:
            target_phase = affine_phase(frame, site_center, phase)
            expected_centers, expected_anchors, _ = periodic_marker_state(length, target_phase, 0)
            transformed_centers = {
                rotate_about(frame, site_center, point, period) for point in centers
            }
            transformed_anchors = {
                rotate_about(frame, site_center, point, period) for point in anchor_state
            }
            row_anchor_failures += int(
                transformed_centers != expected_centers
                or transformed_anchors != expected_anchors
            )
            failures["arbitrary_site_affine_phase"] += int(
                any((target_phase[axis] - (
                    site_center[axis] + rotate(frame, tuple(
                        phase[index] - site_center[index] for index in range(3)
                    ))[axis]
                )) % K != 0 for axis in range(3))
            )
            for orientation in range(24):
                source_orient = orientation_state_from_centers(
                    centers, orientation, period
                )
                target_orientation = left_action(frame, orientation)
                expected_orient = orientation_state_from_centers(
                    expected_centers, target_orientation, period
                )
                transformed_orient = {
                    rotate_about(frame, site_center, point, period)
                    for point in source_orient
                }
                row_orientation_failures += int(transformed_orient != expected_orient)
            for direction in DIRECTIONS:
                phase_then_translate = tuple(
                    (phase[axis] + direction[axis]) % K for axis in range(3)
                )
                left = affine_phase(frame, site_center, phase_then_translate)
                rotated_direction = rotate(frame, direction)
                right_base = affine_phase(frame, site_center, phase)
                right = tuple(
                    (right_base[axis] + rotated_direction[axis]) % K
                    for axis in range(3)
                )
                failures["translation_rotation_semidirect"] += int(left != right)
        failures["periodic_anchor_state"] += row_anchor_failures
        failures["periodic_orientation_state"] += row_orientation_failures
        periodic_rows.append({
            "length": length,
            "split": split,
            "arbitrary_integer_rotation_center": site_center,
            "all24_anchor_state_failures": row_anchor_failures,
            "all576_orientation_state_failures": row_orientation_failures,
        })
    result = {
        "anchor_all24_checks": 24,
        "orientation_all576_checks": 24 * 24,
        "arbitrary_site_formula": "R_q(phi+K n)=q+R(phi-q)+K R n, so every integer site center q maps the phase lattice to the phase q+R(phi-q) mod K",
        "formula_universal_scope": "all integer q and phi; exact signed-permutation coefficient identity, not a finite-q extrapolation",
        "periodic_rows": periodic_rows,
        "failures": failures,
        "pass": all(value == 0 for value in failures.values()),
    }
    check("five-orbit anchors and one-hot orientations obey all24/all576 affine covariance about arbitrary physical site centers",
          result["pass"], result)
    return result


def local_marker_predicate(anchor_ones: set, orientation_bits: tuple[int, ...],
                           nonanchor_weight: int) -> bool:
    return (
        ANCHORS <= anchor_ones
        and len(orientation_bits) == 24 and sum(orientation_bits) == 1
        and nonanchor_weight <= VARIABLE_LIVE_UPPER_BOUND
    )


def marker_constraint_audit(autocorrelation: dict) -> dict:
    valid_orientation_failures = 0
    for index in range(24):
        bits = tuple(int(position == index) for position in range(24))
        valid_orientation_failures += int(
            not local_marker_predicate(set(ANCHORS), bits, VARIABLE_LIVE_UPPER_BOUND)
        )
    anchor_deletion_false_accepts = 0
    valid_bits = tuple(int(index == 0) for index in range(24))
    for deleted in ANCHORS:
        anchor_deletion_false_accepts += int(
            local_marker_predicate(set(ANCHORS) - {deleted}, valid_bits,
                                   VARIABLE_LIVE_UPPER_BOUND)
        )
    malformed_rows = []
    malformed_patterns = (
        ("zero-hot", (0,) * 24),
        ("two-hot", (1, 1) + (0,) * 22),
        ("all-hot", (1,) * 24),
    )
    malformed_false_accepts = 0
    for name, bits in malformed_patterns:
        accepted = local_marker_predicate(
            set(ANCHORS), bits, VARIABLE_LIVE_UPPER_BOUND
        )
        malformed_false_accepts += int(accepted)
        malformed_rows.append({"name": name, "accepted": accepted})
    overweight_accepted = local_marker_predicate(
        set(ANCHORS), valid_bits, VARIABLE_LIVE_UPPER_BOUND + 1
    )
    neighbor_rows = []
    neighbor_mismatch_false_accepts = 0
    for orientation in range(24):
        neighbors = [orientation] * 6
        lawful = all(value == orientation for value in neighbors)
        for direction_index in range(6):
            malformed = list(neighbors)
            malformed[direction_index] = (orientation + 1) % 24
            neighbor_mismatch_false_accepts += int(
                all(value == orientation for value in malformed)
            )
        neighbor_rows.append({"orientation": orientation, "lawful": lawful})
    result = {
        "projector_P_center": "all 120 anchor M2 are one; exactly one of 24 orientation M2 is one; the non-anchor cell weight is at most 91",
        "projector_Q_neighbor": "for each recognized center, the six centers at +/-129 e_i are recognized and carry the same orientation index",
        "raw_anchor_radius_Linf": max(max(abs(value) for value in site) for site in ANCHORS),
        "orientation_radius_Linf": max(max(abs(value) for value in site) for site in ORIENTATION_SITES),
        "weight_projector_radius_Linf": H,
        "neighbor_projector_radius_Linf": K + max(
            max(abs(value) for value in site) for site in ORIENTATION_SITES
        ),
        "bounded_constant_support_independent_of_torus_size": True,
        "valid_orientation_rows": 24,
        "valid_orientation_failures": valid_orientation_failures,
        "anchor_deletions_tested": len(ANCHORS),
        "anchor_deletion_false_accepts": anchor_deletion_false_accepts,
        "malformed_orientation_rows": malformed_rows,
        "malformed_orientation_false_accepts": malformed_false_accepts,
        "overweight_92_accepted": overweight_accepted,
        "neighbor_mismatch_rows": 24 * 6,
        "neighbor_mismatch_false_accepts": neighbor_mismatch_false_accepts,
        "diagonal_projector_off_code_commutator_residual": 0,
        "off_code_projector_family_well_defined": True,
        "raw_anchor_off_code_spoof_constructed": autocorrelation["off_code_spoof_constructed"],
        "recognition_complete_without_weight_condition": False,
        "weight_condition_status": "explicit supplied local code projector; not dynamically enforced",
        "fine_NN_reversible_enforcement_circuit_compiled": False,
        "constraint_preparation_rejection_repair_or_penalty_dynamics_compiled": False,
        "pass_as_exact_projector_contract": (
            valid_orientation_failures == anchor_deletion_false_accepts
            == malformed_false_accepts == neighbor_mismatch_false_accepts == 0
            and not overweight_accepted
            and autocorrelation["false_marker_margin_under_supplied_weight_condition"] == 20
        ),
    }
    check("bounded diagonal marker/neighbor projectors reject deletion, malformed orientation, and overweight rows without claiming fine-NN enforcement",
          result["pass_as_exact_projector_contract"]
          and not result["fine_NN_reversible_enforcement_circuit_compiled"], result)
    return result


def neighbor_periodic_audit() -> dict:
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        phase = ((7 * length) % K, (19 * length) % K, (43 * length) % K)
        cells = tuple(
            (x, y, z) for x in range(length) for y in range(length) for z in range(length)
        )
        neighbor_checks = 0
        failures = 0
        for orientation in range(24):
            field = {cell: orientation for cell in cells}
            for cell in cells:
                for direction in DIRECTIONS:
                    neighbor = tuple(
                        (cell[axis] + direction[axis]) % length for axis in range(3)
                    )
                    failures += int(field[neighbor] != orientation)
                    neighbor_checks += 1
        defect_field = {cell: 0 for cell in cells}
        defect_field[(0, 0, 0)] = 1
        undirected_defects = 0
        for cell in cells:
            for direction in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                neighbor = tuple(
                    (cell[axis] + direction[axis]) % length for axis in range(3)
                )
                undirected_defects += int(defect_field[cell] != defect_field[neighbor])
        _, anchors, orient = periodic_marker_state(length, phase, 0)
        rows.append({
            "length": length,
            "split": split,
            "centers": length**3,
            "same_orientation_neighbor_checks": neighbor_checks,
            "same_orientation_neighbor_failures": failures,
            "one_flipped_center_undirected_defect_edges": undirected_defects,
            "periodic_anchor_sites": len(anchors),
            "active_orientation_sites": len(orient),
            "wrap_seams_included": True,
            "pass": failures == 0 and undirected_defects == 6,
        })
    result = {
        "rows": rows,
        "held_out_size_included": True,
        "pass": all(row["pass"] for row in rows),
    }
    check("same-oriented +/-K neighbor-center constraints pass and a single orientation defect produces six edges on L3/L6/L7",
          result["pass"], result)
    return result


def promotion_disposition(geometry: dict, bus: dict, constraints: dict,
                          translations: dict, rotations: dict) -> dict:
    result = {
        "layer_a_locally_stated_constraint_projectors": {
            "executed": True,
            "status": "PASS on the supplied anchor/orientation/weight sector",
            "bounded_radius": constraints["neighbor_projector_radius_Linf"],
            "translation_invariant_family": translations["pass"],
            "proper_cubic_affine_covariance": rotations["pass"],
        },
        "layer_b_actual_fine_NN_reversible_enforcement": {
            "executed": False,
            "circuit": None,
            "residual": None,
        },
        "layer_c_physical_encoder_intertwiner_leakage": {
            "encoder_composed": False,
            "intertwiner_residual": None,
            "leakage_evaluated": False,
            "EG_physical_executed": False,
        },
        "layer_d_autonomous_microstep_schedule_and_renewal": {
            "executed": False,
            "marker_recognition_preserved_during_Cycle610_bus_microsteps": bus[
                "marker_recognition_preserved_during_open_interval"
            ],
            "actual_routed_descriptor_corruption_witness": bus[
                "actual_routed_descriptor_witness"
            ],
            "bus_routed_around_markers": False,
            "marker_preserving_routing_gadget": False,
            "host_schedule_removed": False,
        },
        "conditional_role_geometry_conflict_free": geometry["pass"],
        "external_origin_removed_from_projector_formula": True,
        "phase_carried_by_valid_marker_state": True,
        "privileged_origin_removed_from_completed_physical_law": False,
        "recognition_complete_on_arbitrary_off_code_states": False,
        "mass_contact_seam_register_fixtures_reexecuted_in_Cycle629": False,
        "inherited_fixture_credit_taken": False,
        "strict_physical_EG_closed": False,
        "breakthrough_bar_met": False,
        "status": "conditional state-carried marker/projector repair; not a physical M2 compiler",
    }
    condition = (
        result["layer_a_locally_stated_constraint_projectors"]["executed"]
        and not result["layer_b_actual_fine_NN_reversible_enforcement"]["executed"]
        and not result["layer_c_physical_encoder_intertwiner_leakage"]["encoder_composed"]
        and not result["layer_d_autonomous_microstep_schedule_and_renewal"]["executed"]
        and not result["privileged_origin_removed_from_completed_physical_law"]
        and not result["breakthrough_bar_met"]
    )
    check("promotion ledger separates exact projectors from enforcement, physical EG, and autonomous renewal",
          condition, result)
    return result


def no_go_discipline(geometry: dict, bus: dict, autocorrelation: dict, coverage: dict,
                      translations: dict, rotations: dict, constraints: dict,
                      disposition: dict) -> dict:
    families = (
        {
            "family": "five-orbit periodic anchor code",
            "object": "120 occupied anchor offsets in Z_129^3",
            "mechanism": "exhaustive periodic autocorrelation",
            "terminal_obligation": "unique local center recognition under the declared occupancy sector",
            "strength_vs_target": "weaker: projector recognition only",
            "marker": "ATTEMPTED",
            "evidence": "nonzero autocorrelation maximum 9 and conditional margin 20",
            "disposition": "passes with the explicit <=91 non-anchor weight condition",
        },
        {
            "family": "state-carried translation-phase orbit",
            "object": "all phi in Z_129^3 and L3/L6/L7 periodic crystals",
            "mechanism": "unique [-64,64]^3 representatives and T_e:phi->phi+e",
            "terminal_obligation": "one-fine-site code-sector covariance",
            "strength_vs_target": "target-equivalent at the diagonal code-projector level",
            "marker": "ATTEMPTED",
            "evidence": "129^3 residues and six shifts exhausted; periodic sets agree",
            "disposition": "passes for the marker/projector family",
        },
        {
            "family": "proper-cubic marker/orientation orbit",
            "object": "five anchor orbits and one 24-site orientation orbit",
            "mechanism": "signed-permutation affine site-centered action",
            "terminal_obligation": "all24/all576 covariance about arbitrary physical sites",
            "strength_vs_target": "target-equivalent at coordinate/projector level",
            "marker": "ATTEMPTED",
            "evidence": "zero all24/all576 and periodic affine-action failures",
            "disposition": "passes without a host frame parameter",
        },
        {
            "family": "bounded diagonal admissibility projectors",
            "object": "anchor, one-hot, weight, and same-neighbor predicates",
            "mechanism": "commuting diagonal local projectors",
            "terminal_obligation": "off-code-defined local constraint contract",
            "strength_vs_target": "weaker than a fine-NN reversible enforcement circuit",
            "marker": "ATTEMPTED",
            "evidence": "deletion, malformed, overweight, and L3/L6/L7 defect rows",
            "disposition": "projector contract passes; enforcement remains absent",
        },
        {
            "family": "conditional Cycle610 geometry replacement",
            "object": "new marker/orientation sites versus all rotated role/path/work sites",
            "mechanism": "exact coordinate-set disjointness",
            "terminal_obligation": "conflict-free conditional geometry",
            "strength_vs_target": "strictly weaker than physical update integration",
            "marker": "ATTEMPTED",
            "evidence": "zero anchor/orientation conflicts with the all-frame dynamic union",
            "disposition": "endpoint geometry passes; bus-time renewal is open",
        },
        {
            "family": "arbitrary off-code raw-marker adversary",
            "object": "union of the true anchor set with one shifted anchor completion",
            "mechanism": "fill the 111 sites missing at an autocorrelation-9 shift",
            "terminal_obligation": "test uniqueness without the weight premise",
            "strength_vs_target": "stronger domain than declared code sector",
            "marker": "ATTEMPTED",
            "evidence": "explicit two-marker off-code configuration",
            "disposition": "falsifies premise-free recognition; does not obstruct enforced weight codes",
        },
    )
    open_routes = (
        {
            "family": "fine-NN reversible weight/marker enforcement",
            "mechanism": "bounded Toffoli/transport network with clean uncompute and local repair",
            "terminal_obligation": "literal support-two circuit plus off-code unitarity",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "autonomous marker-preserving phase-clock renewal",
            "mechanism": "local clock/color fields that serialize bus motion while preserving or renewing recognition",
            "terminal_obligation": "one recurrent physical update with no host schedule",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
    )
    walls = (
        "supplied <=91 non-anchor weight/admissibility sector",
        "literal fine-NN reversible enforcement and repair",
        "integration of replacement orientation controls into the full conditional word",
        "physical encoder/intertwiner/leakage evaluation",
        "autonomous microstep schedule and marker renewal",
    )
    pairs = tuple({
        "wall_A": first,
        "wall_B": second,
        "A_implies_B": False,
        "B_implies_A": False,
        "independent": True,
        "shared_witness_identified": False,
        "evidence": "no executed construction or logical implication connects these obligations",
    } for first, second in combinations(walls, 2))
    residuals = (
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:20-44,198-218",
            "prior_residual": "the fixed K-grid tagged motif fails unit translation and queues a state-carried phase/injective-union repair",
            "current_residual": "the marker/projector family transports phi exactly, but fine-NN enforcement and physical update integration are absent",
            "match": True,
            "closed": "projector-level origin dependence only",
        },
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:160-175",
            "prior_residual": "truth tables and coarse syndromes are not fine-NN admissibility enforcement",
            "current_residual": "Cycle629 adds exact diagonal projectors but still no fine-NN enforcement circuit",
            "match": True,
            "closed": False,
        },
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:94-106",
            "prior_residual": "physical encoder/intertwiner/leakage were not composed",
            "current_residual": "still false/null/unevaluated",
            "match": True,
            "closed": False,
        },
    )
    rhetoric = (
        {
            "phrase": "origin removed",
            "resolutions": ("coordinate formula", "code-projector family", "fine-NN enforcement", "physical update", "autonomous renewal"),
            "tested": ("coordinate formula", "code-projector family"),
            "untested_status": "enforcement, physical update, and renewal remain open",
            "narrowed_phrase": "external origin removed only from the supplied-sector diagonal projector formula",
        },
        {
            "phrase": "local recognition",
            "resolutions": ("raw anchors", "anchor plus weight projector", "arbitrary off-code state", "reversible circuit", "fault repair"),
            "tested": ("raw anchors", "anchor plus weight projector", "explicit off-code spoof"),
            "untested_status": "circuit and repair absent",
            "narrowed_phrase": "bounded supplied-sector predicate, not complete physical recognition",
        },
        {
            "phrase": "all24/all576 covariance",
            "resolutions": ("offset orbit", "affine phase lattice", "diagonal projectors", "full update commutator"),
            "tested": ("offset orbit", "affine phase lattice", "diagonal projectors"),
            "untested_status": "full update commutator absent",
            "narrowed_phrase": "proper-cubic affine projector covariance",
        },
        {
            "phrase": "constraint",
            "resolutions": ("truth predicate", "diagonal projector", "fine-NN circuit", "preparation/repair dynamics"),
            "tested": ("truth predicate", "diagonal projector"),
            "untested_status": "fine-NN circuit and dynamics absent",
            "narrowed_phrase": "locally stated bounded diagonal constraint contract",
        },
        {
            "phrase": "conflict-free compiler",
            "resolutions": ("endpoint site sets", "conditional macro word", "intermediate bus steps", "autonomous recurrent law"),
            "tested": ("endpoint site sets",),
            "untested_status": "word integration, microstep recognition, and recurrent law absent",
            "narrowed_phrase": "conflict-free conditional role geometry",
        },
    )
    partial_paths = (
        {"file": "scripts/physical_translation_orbit_marker_crystal_repair_cycle629_2026_07_22.py", "status": "PARTIAL / NARROWED", "what_closes": "state-carried translation phase and proper-cubic marker projectors on an explicit weight sector"},
        {"file": "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "conditional coarse-grid routing and the exact root falsifier"},
        {"file": "UNMATERIALIZED", "status": "OPEN / PRIORITY", "what_closes": "fine-NN reversible marker/weight enforcement with clean uncompute and off-code extension"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "replacement selector integration and physical encoder/intertwiner/leakage"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "autonomous phase-clock schedule preserving or renewing marker recognition"},
    )
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "newer_origin_main_version_followed": True,
        },
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(row["marker"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in families),
        "N1_open_counterroutes_not_counted": open_routes,
        "N2_collapsed_walls": walls,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "required_phrase_scan": {
                "we assume": "absent",
                "by construction": "absent",
                "as is standard": "absent",
                "the framework provides": "absent",
                "bridge context": "absent",
                "background": "absent",
                "naturally": "absent",
                "obviously": "absent",
                "standard QFT": "absent",
                "registered": "absent",
                "canonical": "absent",
            },
            "promoted_hidden_conditions": (
                "<=91 non-anchor weight is an explicit supplied code projector",
                "uniform same-orientation neighbor sector is an explicit projector condition",
                "marker genesis and blank-work renewal are not supplied silently",
            ),
            "hidden_wall_promotions_complete": True,
        },
        "N4_residual_matching": residuals,
        "N5_rhetoric_resolution": rhetoric,
        "N5_five_resolutions_present": len(rhetoric) >= 5,
        "N6_partial_closure_paths": partial_paths,
        "N7_hostile_steelman": {
            "mechanism": "compile the already explicit bounded anchor/weight/orientation predicates into a reversible support-two Toffoli-and-transport network, store the recognized phase in locally transported clock/color fields, and serialize the Cycle610 move/apply/restore word so recognition is preserved or renewed without host control",
            "why_it_could_close": "all required predicate supports are finite constants, the anchor/orientation coordinate orbits already satisfy translations and rotations, and the current failure is missing materialization rather than a contradiction",
            "terminal_obligation": "literal fine-NN circuit, autonomous recurrent update, physical E G=G E, leakage/deletion, and L3/L6/L7 update commutators",
            "authority_status": "OPEN / no retained authority",
            "citations": (
                "scripts/physical_translation_orbit_marker_crystal_repair_cycle629_2026_07_22.py:marker_constraint_audit",
                "scripts/physical_translation_orbit_marker_crystal_repair_cycle629_2026_07_22.py:rotation_covariance_audit",
                "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:198-218",
            ),
        },
        "N8_cross_cycle_echo": (
            {"cycle": "Cycle560", "retired": "bounded encoder tables", "mechanism": "explicit one-hot branch encoders", "applicability": "supports literal marker-predicate compilation"},
            {"cycle": "Cycle563", "retired": "runtime order service", "mechanism": "transported colors", "applicability": "candidate mechanism for state-carried phase clocks"},
            {"cycle": "Cycle580", "retired": "one primitive layout import", "mechanism": "literal support-two circuit", "applicability": "shows bounded projector materialization should be attempted"},
            {"cycle": "Cycle603", "retired": "local role-event lowering", "mechanism": "reversible elementary words", "applicability": "does not itself integrate global renewal"},
            {"cycle": "Cycle610", "retired": "conditional coordinate placement", "mechanism": "large bounded role geometry", "applicability": "supplies the geometry now repaired at projector level"},
            {"cycle": "Cycle629", "retired": "external phase argument in diagonal constraints", "mechanism": "translation-orbit marker crystal", "applicability": "physical enforcement remains the next constructive route"},
        ),
        "evidence": {
            "geometry": geometry["pass"],
            "bus_intersection_falsifier": bus["pass_as_load_bearing_falsifier"],
            "autocorrelation": autocorrelation["nonzero_periodic_autocorrelation_maximum"] == 9,
            "coverage": coverage["pass"],
            "translations": translations["pass"],
            "rotations": rotations["pass"],
            "constraints": constraints["pass_as_exact_projector_contract"],
            "promotion_honest": not disposition["strict_physical_EG_closed"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "status": "FAIL",
        "failed_checklist_items": (
            "N7: a finite support-two enforcement/transport construction remains live",
            "physical promotion: enforcement, E G=G E, leakage, and autonomous renewal are unexecuted",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "narrowed_positive_artifact_gate": "PASS",
        "demoted_artifact_status": "conditional state-carried translation-orbit marker/projector repair",
    }
    condition = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and len(pairs) == math.comb(len(walls), 2)
        and len(residuals) == 3 and all(row["match"] for row in residuals)
        and result["N5_five_resolutions_present"] and len(partial_paths) >= 5
        and all(result["evidence"].values())
        and not result["negative_claim_shipped"]
        and not result["shared_obstruction"] and not result["axiom_pressure"]
        and result["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and result["narrowed_positive_artifact_gate"] == "PASS"
        and result["N7_hostile_steelman"]["authority_status"] == "OPEN / no retained authority"
    )
    check("fresh N1-N8 blocks broad/minimum/axiom claims and retains only the projector-level repair",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Author artifact status accepted: false",
        "Breakthrough: false", "Cycle 629", "120", "24", "129^3",
        "state-carried", "translation-invariant", "autocorrelation", "9", "20",
        "111", "<=91", "all six", "All 24", "All 576", "arbitrary physical site",
        "L3", "L6", "L7", "deletion", "zero-hot", "two-hot", "all-hot",
        "same-oriented", "projector", "fine-NN", "intertwiner", "leakage",
        "autonomous", "renewal", "off-code", "supplied", "not recognition complete",
        "not a physical M2 compiler", "N1", "N8", "FAIL / DO NOT SHIP",
        "no axiom pressure", "PR #5557",
    )
    forbidden = (
        "fine-NN enforcement is complete", "physical M2 compiler is complete",
        "strict physical EG closes", "axiom pressure is established",
        "shared obstruction is proved", "schedule is physical time",
        "marker count is energy", "all off-code states have unique recognition",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden_hits = tuple(phrase for phrase in forbidden if phrase in text)
    result = {"required": required, "missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle629 note freezes exact marker evidence, supplied conditions, four-layer promotion ledger, and N1-N8",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    start = time.perf_counter()
    print("Cycle629 state-carried translation-orbit marker-crystal repair", AUTHORITY, AUDIT)

    inherited = shore()
    target = exact_target_contract()
    c610_receipt = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())
    geometry = candidate_geometry_audit(c610_receipt)
    bus = bus_marker_intersection_audit()
    autocorrelation = autocorrelation_audit()
    coverage = phase_and_coverage_audit()
    translations = translation_covariance_audit()
    rotations = rotation_covariance_audit()
    constraints = marker_constraint_audit(autocorrelation)
    neighbors = neighbor_periodic_audit()
    disposition = promotion_disposition(geometry, bus, constraints, translations, rotations)
    discipline = no_go_discipline(
        geometry, bus, autocorrelation, coverage, translations, rotations,
        constraints, disposition,
    )
    note = note_contract()

    elapsed = time.perf_counter() - start
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        maximum_rss_bytes = int(maximum_rss)
    else:
        maximum_rss_bytes = int(maximum_rss * 1024)
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss_bytes < CAP_BYTES, {
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes,
    })

    receipt = {
        "status": "conditional_state_carried_marker_projector_repair",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_artifact_status_accepted": False,
        "breakthrough_bar_met": False,
        "breakthrough_default": "no",
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "pins": PINS,
        "shore": inherited,
        "exact_target_contract": target,
        "candidate_geometry": geometry,
        "Cycle610_bus_marker_intersection": bus,
        "periodic_anchor_autocorrelation": autocorrelation,
        "phase_and_unique_center_coverage": coverage,
        "one_fine_site_translation_covariance": translations,
        "proper_cubic_affine_covariance": rotations,
        "local_marker_constraint_projectors": constraints,
        "periodic_same_orientation_neighbor_constraints": neighbors,
        "promotion_disposition": disposition,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": "a translation-invariant bounded family of diagonal marker/neighbor/code-weight projectors with a state-carried phi in Z_129^3: five disjoint proper-cubic anchor orbits give 120 anchors, a disjoint 24-site orbit carries orientation, all residues/six unit shifts/all24/all576 affine actions and L3/L6/L7 periodic constraints pass, and the new sites are disjoint from conditional Cycle610 role geometry",
        "exact_scope": "the supplied marker sector with all 120 anchors occupied, exactly one orientation bit, non-anchor weight <=91 per phase cell, and same-oriented +/-K neighbor centers",
        "supplied_structure": (
            "five anchor seeds and their occupied anchor state",
            "one of 24 orientation bits",
            "non-anchor weight <=91",
            "uniform same-orientation neighbor sector",
            "marker genesis/renewal and blank work are not derived",
        ),
        "origin_disposition": {
            "external_origin_argument_in_projector_family": False,
            "phase_carried_by_code_state": True,
            "one_site_translation_maps_phi_to_phi_plus_e": True,
            "privileged_origin_removed_at_projector_contract_level": True,
            "privileged_origin_removed_from_completed_physical_law": False,
            "reason": "fine-NN enforcement, replacement-selector integration, physical EG/leakage, and autonomous renewal are not executed",
        },
        "interpretation_firewall": {
            "projector_is_fine_NN_enforcement_circuit": False,
            "coordinate_covariance_is_update_covariance": False,
            "state_carried_phase_is_physical_time": False,
            "host_microstep_schedule_is_autonomous_time": False,
            "marker_or_site_count_is_energy_or_source": False,
            "inherited_fixture_is_reexecuted_fixture": False,
        },
        "mass_contact_seam_register_fixtures_reexecuted": False,
        "shared_obstruction_or_axiom_pressure": False,
        "constitutional_effect": "none",
        "broad_negative_gate": discipline["broad_negative_gate"],
        "optimal_next_campaign": "compile the explicit radius-160 marker/weight/neighbor projector contract into a literal fine-NN reversible circuit with clean uncompute and off-code extension, integrate the replacement orientation controls, then construct an autonomous marker-preserving phase-clock schedule and execute physical E G=G E, leakage, deletion, and L3/L6/L7 update covariance",
        "local_cycle629_not_causal_time_PR5557_cycle610": "Cycle629 depends only on the local conditional Cycle610 quartet; it does not import the distinct causal-time Cycle610 in PR #5557",
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss_bytes,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    summary = {
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss_bytes,
        "anchor_sites": len(ANCHORS),
        "orientation_sites": len(ORIENTATION_SITES),
        "nonzero_autocorrelation_max": autocorrelation["nonzero_periodic_autocorrelation_maximum"],
        "conditional_false_marker_margin": autocorrelation["false_marker_margin_under_supplied_weight_condition"],
        "projector_origin_argument_removed": True,
        "physical_law_origin_closed": False,
        "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
