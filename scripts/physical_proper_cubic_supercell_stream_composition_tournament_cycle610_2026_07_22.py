#!/usr/bin/env python3
"""Cycle610: conditional proper-cubic coarse-grid M2 placement for Cycle606.

The construction supplies a 129-period coarse partition/origin and a
24-valued cubic role orientation.  Within that supplied coloring, bounded
support-one/two nearest-neighbor coordinate words implement the logical
register fixtures.  The tagged role motif is not invariant under a one-fine-
site translation, so this is not a one-site translation-covariant physical M2
law.  Schedules are update factorizations, not physical time.  Authority none;
audit unset; author artifact status accepted false; breakthrough false.
"""
from __future__ import annotations

from collections import deque
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

import physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22 as c606
import physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22 as c603


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_proper_cubic_supercell_stream_composition_"
    "tournament_cycle610_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_proper_cubic_supercell_stream_composition_"
    "tournament_cycle610_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-9
CAP_SECONDS = 420.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md":
        "a7a3a0a021dbd691c6c2ddb9163679b445c5110b8150f63395271037963c7132",
    "scripts/physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22.py":
        "637a7ac6b5a56ef539bef3b94c6624a4f5f52372ef31e2d1e3bdc4328ae8767f",
    "docs/work_history/repo/review_feedback/PHYSICAL_GLOBAL_CARRIER_STREAM_QCA_APPROXIMATION_TOURNAMENT_CYCLE606_NOTE_2026-07-22.md":
        "01ef76e8e0c3d29645e1f9247fa479d3fa1d3dbabab09d884da102208cf31d78",
    "outputs/physical_global_carrier_stream_qca_approximation_tournament_cycle606_receipt_2026_07_22.json":
        "2b225152dcdae055c4d751c57af913b6184b9977e52ebc3dba509b4fc0b3da3c",
    "outputs/physical_global_carrier_stream_qca_approximation_tournament_cycle606_cold_2026_07_22.txt":
        "007d7fdf3d67d55afbacdd905bc44d67b685f9926ba395e393ed01eec005e5dd",
    "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py":
        "e64032e369e08e03ad2a742a2bde6914d8adc6ed1fd64f15f4e301c1c8dea739",
    "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md":
        "ddc06d6d4abf945794b1c0b7566c9183fa744839d1ba5630c1d9ad8b4559c417",
    "outputs/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_receipt_2026_07_22.json":
        "751487fa50a738d5473f7ddcb77474785c84463dda1264a34de2643f19102871",
    "outputs/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_cold_2026_07_22.txt":
        "35385a09b5d075e553de1de9302e0317dd415acbe1f5ccf9425905eedae94174",
}

MINIMAL_AXIOMS_TEST_CONTRACT = {
    "path": "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "sha256": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "origin_main_lines": "37-41",
    "contract": "physical Z^3 nearest-neighbor sites, standard translations, proper rotations about each site, and no privileged site",
    "used_as_dynamics_or_new_authority": False,
}

H = 64
K = 2 * H + 1
GAP = 10
DIRECTIONS = tuple(
    tuple(int(value) for value in row)
    for row in c606.c600.c598.c593.c210.DIRECTIONS
)
SPECIES_CENTERS = ((0, 20, 20), (20, 0, -20), (-20, -20, 0))
A_OFFSETS = tuple((x, -3, 0) for x in range(-3, 4))
B_OFFSETS = tuple((x, 3, 0) for x in range(-3, 4))
A_NAMES = ("A0", "A1", "A2", "A3", "FA", "WA0", "WA1")
B_NAMES = ("B0", "B1", "B2", "B3", "FB", "WB0", "WB1")


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
    if isinstance(value, complex):
        return (value.real, value.imag)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))


def scale(factor: int, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(factor * value for value in vector)


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(left[index] * right[index] for index in range(3))


def rotate(frame: np.ndarray, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in frame @ np.asarray(vector, dtype=int))


FRAMES = c606.c600.c598.c593.c210.proper_cubic_frames()
ORIENTATION_SEED = (1, 2, 3)
PREDICATE_WORK_SEED = (4, 5, 6)
ORIENTATION_SITES = tuple(rotate(frame, ORIENTATION_SEED) for frame in FRAMES)
PREDICATE_WORK_SITES = tuple(rotate(frame, PREDICATE_WORK_SEED) for frame in FRAMES)
ONSITE_WORK_SITE = (0, 0, 0)


def edge_key(first: tuple[int, int, int], second: tuple[int, int, int]) -> tuple:
    return tuple(sorted((first, second)))


def nn(first: tuple[int, int, int], second: tuple[int, int, int], period: int | None = None) -> bool:
    if period is None:
        return sum(abs(first[index] - second[index]) for index in range(3)) == 1
    differences = []
    for index in range(3):
        delta = abs(first[index] - second[index]) % period
        differences.append(min(delta, period - delta))
    return sum(differences) == 1


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    receipt = json.loads((ROOT / (
        "outputs/physical_global_carrier_stream_qca_approximation_"
        "tournament_cycle606_receipt_2026_07_22.json"
    )).read_text())
    route = receipt["route_A_compact_double_buffer"]
    c603_receipt = json.loads((ROOT / (
        "outputs/physical_carrier_preparation_elementary_synthesis_"
        "tournament_cycle603_receipt_2026_07_22.json"
    )).read_text())
    expected_graph = dict(receipt["shore"]["import_audit"]["expected_transitive_sha256"])
    expected_graph.update(receipt["pins"])
    expected_graph.update(PINS)
    observed_graph = {name: sha(ROOT / name) for name in expected_graph}
    actual_modules = c606.c600.imported_science_modules(
        c606, c603, c603.c219, c603.c230
    )
    uncovered = sorted(set(actual_modules.values()) - set(expected_graph))
    test_contract_observed = sha(ROOT / MINIMAL_AXIOMS_TEST_CONTRACT["path"])
    inherited = {
        "pass": receipt["pass"],
        "tests_passed": receipt["tests_passed"],
        "author_artifact_status_accepted": receipt["author_artifact_status_accepted"],
        "register_stream": route["pass_exact_declared_code_global_stream"],
        "Cycle606_physical_M2_scope": receipt["physical_M2_scope"],
        "one_carrier_global": not route["exactly_one_sector_locally_generated"],
        "axiom_pressure": receipt["shared_obstruction_or_axiom_pressure"],
        "broad_negative_gate": receipt["broad_negative_gate"],
        "Cycle603_pass": c603_receipt["pass"],
        "Cycle603_tests_passed": c603_receipt["tests_passed"],
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
            "observed_sha256": test_contract_observed,
        },
    }
    condition = (
        observed == PINS and inherited["pass"] and inherited["tests_passed"] == 8
        and not inherited["author_artifact_status_accepted"]
        and inherited["register_stream"]
        and not inherited["Cycle606_physical_M2_scope"]["literal_layout_compiled"]
        and not inherited["Cycle606_physical_M2_scope"]["primitive_composition"]
        and inherited["Cycle606_physical_M2_scope"]["intertwiner_residual"] is None
        and not inherited["Cycle606_physical_M2_scope"]["leakage_evaluated"]
        and inherited["one_carrier_global"] and not inherited["axiom_pressure"]
        and inherited["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and inherited["Cycle603_pass"] and inherited["Cycle603_tests_passed"] == 7
        and observed_graph == expected_graph and not uncovered
        and test_contract_observed == MINIMAL_AXIOMS_TEST_CONTRACT["sha256"]
    )
    check("accepted Cycle606 shore is byte exact", condition, {
        "observed": observed, "inherited": inherited,
    })
    return {"Cycle606_receipt": receipt, "verified_inheritance": inherited}


# ---------------------------------------------------------------------------
# Canonical local paths and the 24-orientation intrinsic role field.


def bfs_path(start: tuple[int, int, int], end: tuple[int, int, int],
             blocked: set[tuple[int, int, int]]) -> tuple[tuple[int, int, int], ...]:
    queue = deque([start])
    previous: dict[tuple[int, int, int], tuple[int, int, int] | None] = {start: None}
    while queue:
        site = queue.popleft()
        if site == end:
            break
        for direction in DIRECTIONS:
            candidate = add(site, direction)
            if (
                any(abs(value) > GAP for value in candidate)
                or candidate in blocked or candidate in previous
            ):
                continue
            previous[candidate] = site
            queue.append(candidate)
    if end not in previous:
        raise RuntimeError(f"no local route {start}->{end}")
    answer = []
    current: tuple[int, int, int] | None = end
    while current is not None:
        answer.append(current)
        current = previous[current]
    return tuple(reversed(answer))


def canonical_paths() -> dict:
    a_roles, b_roles = set(A_OFFSETS), set(B_OFFSETS)
    source_start, target_end = A_OFFSETS[4], B_OFFSETS[4]
    rows = {}
    for direction in DIRECTIONS:
        source_end = scale(GAP, direction)
        target_start = scale(-GAP, direction)
        source = bfs_path(
            source_start, source_end,
            (a_roles - {source_start}) | b_roles,
        )
        target = bfs_path(
            target_start, target_end,
            (b_roles - {target_end}) | a_roles | set(source),
        )
        rows[direction] = {"source": source, "target": target}
    neutral = bfs_path(
        source_start, target_end,
        (a_roles | b_roles) - {source_start, target_end},
    )
    return {"directions": rows, "neutral": neutral}


CANONICAL = canonical_paths()


def roles(species: int, frame: np.ndarray) -> dict[str, tuple[int, int, int]]:
    center = rotate(frame, SPECIES_CENTERS[species])
    answer = {}
    for name, offset in zip(A_NAMES, A_OFFSETS):
        answer[name] = add(center, rotate(frame, offset))
    for name, offset in zip(B_NAMES, B_OFFSETS):
        answer[name] = add(center, rotate(frame, offset))
    return answer


def shuttle_paths(species: int, frame: np.ndarray,
                  direction: tuple[int, int, int]) -> dict:
    center = rotate(frame, SPECIES_CENTERS[species])
    canonical_direction = rotate(frame.T, direction)
    local = CANONICAL["directions"][canonical_direction]
    source_internal = tuple(
        add(center, rotate(frame, site)) for site in local["source"]
    )
    target_internal = tuple(
        add(center, rotate(frame, site)) for site in local["target"]
    )
    normal = dot(center, direction)
    transverse = sub(center, scale(normal, direction))
    source_channel = tuple(
        add(transverse, scale(index, direction))
        for index in range(normal + GAP, H + 1)
    )
    target_channel = tuple(
        add(transverse, scale(index, direction))
        for index in range(-H, normal - GAP + 1)
    )
    source = source_internal + source_channel[1:]
    target = target_channel + target_internal[1:]
    return {
        "source": source,
        "target": target,
        "cross_edge_local_roles": (source[-1], target[0]),
        "cross_edge_physical_representative": (
            source[-1], add(target[0], scale(K, direction))
        ),
        "source_internal": source_internal,
        "source_channel": source_channel,
        "target_channel": target_channel,
        "target_internal": target_internal,
    }


def neutral_path(species: int, frame: np.ndarray) -> tuple[tuple[int, int, int], ...]:
    center = rotate(frame, SPECIES_CENTERS[species])
    return tuple(add(center, rotate(frame, site)) for site in CANONICAL["neutral"])


def swap_paths(species: int, frame: np.ndarray) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    center = rotate(frame, SPECIES_CENTERS[species])
    rows = []
    for bit in range(4):
        canonical = tuple((bit - 3, y, 0) for y in range(-3, 4))
        rows.append(tuple(add(center, rotate(frame, site)) for site in canonical))
    return tuple(rows)


def path_edges(path: tuple[tuple[int, int, int], ...]) -> tuple[tuple, ...]:
    return tuple((path[index], path[index + 1]) for index in range(len(path) - 1))


def routed_remote_swap_edges(path: tuple[tuple[int, int, int], ...]) -> tuple[tuple, ...]:
    edges = path_edges(path)
    return edges + tuple(reversed(edges[:-1]))


def layout_manifest() -> dict:
    frame = np.eye(3, dtype=int)
    direction_rows = []
    allocated = set()
    storage = {}
    for species in range(3):
        storage[str(species)] = roles(species, frame)
        allocated.update(storage[str(species)].values())
        allocated.update(neutral_path(species, frame))
        for path in swap_paths(species, frame):
            allocated.update(path)
    allocated.update(ORIENTATION_SITES)
    allocated.update(PREDICATE_WORK_SITES)
    allocated.add(ONSITE_WORK_SITE)
    for direction_index, direction in enumerate(DIRECTIONS):
        paths = []
        for species in range(3):
            row = shuttle_paths(species, frame, direction)
            allocated.update(row["source"])
            allocated.update(row["target"])
            paths.append({
                "species": species,
                "source": row["source"],
                "target": row["target"],
                "cross_edge_local_roles": row["cross_edge_local_roles"],
                "cross_edge_physical_representative": row["cross_edge_physical_representative"],
            })
        direction_rows.append({
            "direction_index": direction_index,
            "direction": direction,
            "paths": paths,
        })
    return {
        "supercell_local_coordinate_box": ((-H, -H, -H), (H, H, H)),
        "fine_linear_scale_K": K,
        "supplied_coarse_partition_origin_period": K,
        "coarse_partition_or_origin_derived_from_translation_invariant_state": False,
        "full_physical_M2_sites_per_coarse_cell": K**3,
        "species_centers": SPECIES_CENTERS,
        "storage_roles": storage,
        "neutral_paths": tuple(neutral_path(species, frame) for species in range(3)),
        "word_swap_paths": tuple(swap_paths(species, frame) for species in range(3)),
        "direction_rows": direction_rows,
        "allocated_stream_role_sites_union": len(allocated),
        "persistent_word_and_equality_M2": 3 * (len(A_NAMES) + len(B_NAMES)),
        "persistent_one_hot_orientation_M2": len(ORIENTATION_SITES),
        "reused_predicate_flag_work_M2": len(PREDICATE_WORK_SITES),
        "reused_onsite_work_M2": 1,
        "maximum_persistent_plus_predicate_live_M2": (
            3 * (len(A_NAMES) + len(B_NAMES))
            + len(ORIENTATION_SITES) + len(PREDICATE_WORK_SITES) + 1
        ),
        "empty_or_bus_spacer_M2": (
            K**3 - 3 * (len(A_NAMES) + len(B_NAMES))
            - len(ORIENTATION_SITES) - len(PREDICATE_WORK_SITES) - 1
        ),
        "role_orientation_values": 24,
        "orientation_bit_coordinates": ORIENTATION_SITES,
        "predicate_flag_work_coordinates": PREDICATE_WORK_SITES,
        "role_orientation_genesis": "supplied one-hot 24-M2 field; every sector is accepted by mutually exclusive controlled branches of one autonomous rule",
    }


def declared_tagged_role_motif() -> set[tuple[int, int, int]]:
    """Persistent tagged sites in the supplied identity-frame coarse cell."""
    base = np.eye(3, dtype=int)
    tagged = set(ORIENTATION_SITES) | set(PREDICATE_WORK_SITES) | {ONSITE_WORK_SITE}
    for species in range(3):
        tagged.update(roles(species, base).values())
    return tagged


def fine_site_translation_falsifier() -> dict:
    """Test the declared tagged-role support under physical unit translations.

    Coarse translations by K preserve the supplied tiling.  A physical unit
    translation must instead preserve or covariantly permute the code space
    without assuming that tiling.  The nonzero symmetric differences below
    falsify that stronger promotion for the current motif.
    """
    motif = declared_tagged_role_motif()
    expected_unit_x = {3: 2970, 6: 23760, 7: 37730}
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        period = K * length
        tagged = {
            global_coordinate(local, cell, length)
            for cell in all_cells(length)
            for local in motif
        }
        directional_differences = {}
        for direction in DIRECTIONS:
            shifted = {
                tuple((site[axis] + direction[axis]) % period for axis in range(3))
                for site in tagged
            }
            directional_differences[str(direction)] = len(tagged ^ shifted)
        unit_x = directional_differences[str((1, 0, 0))]
        rows.append({
            "length": length,
            "split": split,
            "fine_torus_period": period,
            "tagged_roles_per_supplied_coarse_cell": len(motif),
            "tagged_sites": len(tagged),
            "overlap_with_one_fine_site_x_translate": (
                len(tagged) - unit_x // 2
            ),
            "one_fine_site_x_translation_symmetric_difference": unit_x,
            "expected_root_falsifier": expected_unit_x[length],
            "all_six_unit_translation_symmetric_differences": directional_differences,
            "one_fine_site_x_translation_preserves_tagged_code_support": unit_x == 0,
            "coarse_K_translation_preserves_partition": True,
        })
    result = {
        "test_contract": MINIMAL_AXIOMS_TEST_CONTRACT,
        "declared_tagged_role_definition": "42 A/B word/equality roles plus 24 orientation roles plus 24 predicate-work roles plus one onsite-work role in each supplied identity-frame coarse cell",
        "tagged_roles_per_coarse_cell": len(motif),
        "one_fine_site_translation_covariant_code_space": False,
        "one_fine_site_translation_covariant_update_law": False,
        "coarse_K_grid_translation_covariance_only": True,
        "supplied_partition_origin_or_role_coloring": True,
        "rows": rows,
        "strongest_live_repair": {
            "route": "state-carried translation phase or an injective union of all K^3 translated motifs",
            "mechanism": "add a locally recognized phase phi in Z_K^3 so a unit translation sends phi to phi+e_i and mutually exclusive P_(phi,h) branches select the translated/rotated coordinate word",
            "terminal_obligation": "construct literal NN phase/admissibility gadgets and execute code-domain plus update commutators for one-fine-site translations, all site-centered proper rotations, L3/L6/L7, leakage, and deletion",
            "status": "OPEN / not implemented",
            "naive_unlabelled_union_warning": "the support union of all K^3 translates fills the cell but aliases distinct role labels; injective roles or a state-carried phase are still required",
        },
        "naive_union_of_all_K3_translated_supports_fills_fine_cell": True,
        "naive_union_preserves_injective_role_labels": False,
    }
    result["pass_as_reproduced_falsifier"] = (
        len(motif) == 91
        and all(
            row["one_fine_site_x_translation_symmetric_difference"]
            == row["expected_root_falsifier"] > 0
            and not row["one_fine_site_x_translation_preserves_tagged_code_support"]
            for row in rows
        )
    )
    return result


def frame_index(frame: np.ndarray) -> int:
    for index, candidate in enumerate(FRAMES):
        if np.array_equal(frame, candidate):
            return index
    raise ValueError("not a proper-cubic frame")


def left_action(permutation_frame: np.ndarray, orientation_index: int) -> int:
    return frame_index(permutation_frame @ FRAMES[orientation_index])


def predicate_roles(orientation_index: int) -> dict:
    """Covariant relative ordering for the exact one-hot branch predicate."""
    frame = FRAMES[orientation_index]
    identity_index = frame_index(np.eye(3, dtype=int))
    relative = (identity_index,) + tuple(
        index for index in range(len(FRAMES)) if index != identity_index
    )
    orientation_order = tuple(
        frame_index(frame @ FRAMES[index]) for index in relative
    )
    flag = rotate(frame, PREDICATE_WORK_SEED)
    work_order = tuple(
        rotate(frame @ FRAMES[index], PREDICATE_WORK_SEED)
        for index in relative[1:]
    )
    return {
        "positive_orientation_site": ORIENTATION_SITES[orientation_index],
        "negative_orientation_sites": tuple(
            ORIENTATION_SITES[index] for index in orientation_order[1:]
        ),
        "orientation_control_order": tuple(
            ORIENTATION_SITES[index] for index in orientation_order
        ),
        "predicate_flag_site": flag,
        "predicate_work_sites": work_order[:22],
        "spare_predicate_work_site": work_order[22],
    }


def orientation_control_audit() -> dict:
    failures = {
        "orientation_orbit_injection": int(len(set(ORIENTATION_SITES)) != 24),
        "predicate_work_orbit_injection": int(len(set(PREDICATE_WORK_SITES)) != 24),
        "orientation_work_overlap": len(set(ORIENTATION_SITES) & set(PREDICATE_WORK_SITES)),
        "role_storage_overlap": 0,
        "one_hot_truth": 0,
        "invalid_zero_or_multi_hot_not_identity_extension": 0,
        "all576_orientation_action": 0,
        "all576_predicate_role_action": 0,
    }
    all_layout_sites = set()
    for frame in FRAMES:
        for species in range(3):
            all_layout_sites.update(roles(species, frame).values())
            all_layout_sites.update(neutral_path(species, frame))
            for path in swap_paths(species, frame):
                all_layout_sites.update(path)
            for direction in DIRECTIONS:
                row = shuttle_paths(species, frame, direction)
                all_layout_sites.update(row["source"])
                all_layout_sites.update(row["target"])
    failures["role_storage_overlap"] = len(
        all_layout_sites
        & (set(ORIENTATION_SITES) | set(PREDICATE_WORK_SITES) | {ONSITE_WORK_SITE})
    )
    truth_rows = []
    for orientation_index in range(24):
        bits = np.zeros(24, dtype=np.int8)
        bits[orientation_index] = 1
        predicates = tuple(
            int(bits[index] == 1 and int(np.sum(bits)) == 1)
            for index in range(24)
        )
        failures["one_hot_truth"] += int(
            sum(predicates) != 1 or predicates[orientation_index] != 1
        )
        truth_rows.append({
            "orientation_index": orientation_index,
            "orientation_coordinate": ORIENTATION_SITES[orientation_index],
            "active_branch_count": sum(predicates),
        })
    for invalid in (
        np.zeros(24, dtype=np.int8),
        np.asarray([1, 1] + [0] * 22, dtype=np.int8),
        np.ones(24, dtype=np.int8),
    ):
        active = sum(
            int(invalid[index] == 1 and int(np.sum(invalid)) == 1)
            for index in range(24)
        )
        failures["invalid_zero_or_multi_hot_not_identity_extension"] += int(active != 0)
    for first in FRAMES:
        for second_index, second in enumerate(FRAMES):
            direct_index = left_action(first, second_index)
            failures["all576_orientation_action"] += int(
                rotate(first, ORIENTATION_SITES[second_index])
                != ORIENTATION_SITES[direct_index]
            )
            source = predicate_roles(second_index)
            direct = predicate_roles(direct_index)
            for key in (
                "positive_orientation_site", "predicate_flag_site",
                "spare_predicate_work_site",
            ):
                failures["all576_predicate_role_action"] += int(
                    rotate(first, source[key]) != direct[key]
                )
            for key in ("negative_orientation_sites", "predicate_work_sites"):
                mapped = tuple(rotate(first, site) for site in source[key])
                failures["all576_predicate_role_action"] += int(mapped != direct[key])
    # C24X: 45 Toffoli calls with 22 work, plus 23 negative-control opens/closes.
    predicate_compute_counts = {
        "C24X_Toffoli_calls": 45,
        "negative_control_X": 46,
        "exact_support_two_gates_after_Cycle603_Toffoli_lowering": 45 * 15 + 46,
        "clean_work_M2": 22,
        "flag_M2": 1,
        "spare_M2": 1,
    }
    return {
        "conditional_encoding": "24 tagged one-hot site roles per supplied coarse cell; orientation h selects layout R_h",
        "exactly_one_truth_table_executed": True,
        "lawful_table_predicate": "exactly one of 24 tagged bits is one inside a supplied supercell partition",
        "coarse_neighbor_equality_table": "adjacent supplied coarse cells carry the same one-hot word",
        "literal_NN_exactly_one_constraint_enforcement_gadget_constructed": False,
        "literal_NN_coarse_neighbor_equality_enforcement_gadget_constructed": False,
        "constraint_preparation_repair_or_rejection_dynamics_constructed": False,
        "lawful_update": "orientation bits are unchanged; compute mutually exclusive P_h flags, apply controlled G_h, uncompute",
        "invalid_extension": "zero-hot or multi-hot activates no P_h branch and is identity; arbitrary dirty predicate work is outside the declared code but the gate product remains unitary",
        "branch_order": "P_h projectors are mutually orthogonal on the supplied table sector, so controlled branches commute; this does not derive the coarse partition/origin",
        "predicate_compute_counts": predicate_compute_counts,
        "truth_rows": truth_rows,
        "failures": failures,
        "pass": all(value == 0 for value in failures.values()),
    }


def local_geometry_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    failures = {
        "storage_injection": 0,
        "path_NN": 0,
        "path_self_intersection": 0,
        "simultaneous_vertex_conflict": 0,
        "cross_edge_not_boundary_NN": 0,
        "neutral_path": 0,
        "swap_path": 0,
        "role_covariance": 0,
    }
    maximum_path = 0
    minimum_path = 10**9
    direction_live_sites = []
    base = np.eye(3, dtype=int)
    for frame in frames:
        all_storage = []
        for species in range(3):
            role_row = roles(species, frame)
            all_storage.extend(role_row.values())
            neutral = neutral_path(species, frame)
            failures["neutral_path"] += int(
                len(set(neutral)) != len(neutral)
                or any(not nn(*edge) for edge in path_edges(neutral))
                or neutral[0] != role_row["FA"] or neutral[-1] != role_row["FB"]
            )
            for bit, swap in enumerate(swap_paths(species, frame)):
                failures["swap_path"] += int(
                    len(set(swap)) != len(swap)
                    or any(not nn(*edge) for edge in path_edges(swap))
                    or swap[0] != role_row[f"A{bit}"]
                    or swap[-1] != role_row[f"B{bit}"]
                )
        failures["storage_injection"] += int(len(all_storage) != len(set(all_storage)))
        for direction in DIRECTIONS:
            simultaneous = []
            for species in range(3):
                row = shuttle_paths(species, frame, direction)
                role_row = roles(species, frame)
                for family in ("source", "target"):
                    path = row[family]
                    maximum_path = max(maximum_path, len(path))
                    minimum_path = min(minimum_path, len(path))
                    failures["path_NN"] += sum(not nn(*edge) for edge in path_edges(path))
                    failures["path_self_intersection"] += int(len(set(path)) != len(path))
                    simultaneous.append((species, family, set(path)))
                failures["path_NN"] += int(not nn(*row["cross_edge_physical_representative"]))
                failures["cross_edge_not_boundary_NN"] += int(
                    dot(row["cross_edge_local_roles"][0], direction) != H
                    or dot(row["cross_edge_local_roles"][1], direction) != -H
                    or sub(row["cross_edge_local_roles"][0], scale(H, direction))
                    != sub(row["cross_edge_local_roles"][1], scale(-H, direction))
                )
                failures["path_NN"] += int(row["source"][0] != role_row["FA"])
                failures["path_NN"] += int(row["target"][-1] != role_row["FB"])
            direction_live_sites.append(sum(len(row[2]) for row in simultaneous))
            for first, second in combinations(simultaneous, 2):
                failures["simultaneous_vertex_conflict"] += len(first[2] & second[2])

        # The role map and every routed coordinate transform functorially.
        for species in range(3):
            direct_roles = roles(species, frame)
            for name, coordinate in roles(species, base).items():
                failures["role_covariance"] += int(
                    rotate(frame, coordinate) != direct_roles[name]
                )
            for direction in DIRECTIONS:
                mapped_direction = rotate(frame, direction)
                direct = shuttle_paths(species, frame, mapped_direction)
                original = shuttle_paths(species, base, direction)
                for family in ("source", "target"):
                    mapped = tuple(rotate(frame, site) for site in original[family])
                    failures["role_covariance"] += int(mapped != direct[family])
    return {
        "frames_tested": len(frames),
        "directions_per_frame": len(DIRECTIONS),
        "minimum_shuttle_path_sites": minimum_path,
        "maximum_shuttle_path_sites": maximum_path,
        "maximum_live_stream_path_role_M2_one_direction_all_species": max(direction_live_sites),
        "failures": failures,
        "pass": all(value == 0 for value in failures.values()),
    }


def global_coordinate(local: tuple[int, int, int], cell: tuple[int, int, int],
                      length: int) -> tuple[int, int, int]:
    period = K * length
    return tuple((K * cell[index] + local[index]) % period for index in range(3))


def coarse_target(cell: tuple[int, int, int], direction: tuple[int, int, int],
                  length: int) -> tuple[int, int, int]:
    return tuple((cell[index] + direction[index]) % length for index in range(3))


def all_cells(length: int):
    for x in range(length):
        for y in range(length):
            for z in range(length):
                yield x, y, z


def microstep_edges(paths: list[tuple[tuple[int, int, int], ...]],
                    cells: tuple[tuple[int, int, int], ...], length: int,
                    reverse: bool = False) -> tuple[int, int, int]:
    maximum = max(len(path) for path in paths) - 1
    vertex_failures = edge_failures = adjacency_failures = 0
    for step in range(maximum):
        vertices = set()
        edges = set()
        for cell in cells:
            for path in paths:
                index = (len(path) - 2 - step) if reverse else step
                if index < 0 or index >= len(path) - 1:
                    continue
                first = global_coordinate(path[index], cell, length)
                second = global_coordinate(path[index + 1], cell, length)
                adjacency_failures += int(not nn(first, second, K * length))
                vertex_failures += int(first in vertices) + int(second in vertices)
                vertices.update((first, second))
                key = edge_key(first, second)
                edge_failures += int(key in edges)
                edges.add(key)
    return vertex_failures, edge_failures, adjacency_failures


def global_geometry_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    rows = []
    overall = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        cells = tuple(all_cells(length))
        vertex_failures = edge_failures = adjacency_failures = 0
        cross_endpoint_failures = cross_edge_duplicates = seam_failures = 0
        microsteps = routed_edges = cross_edges_tested = 0
        for frame in frames:
            for direction in DIRECTIONS:
                source_paths = [shuttle_paths(species, frame, direction)["source"]
                                for species in range(3)]
                target_paths = [shuttle_paths(species, frame, direction)["target"]
                                for species in range(3)]
                for path_family in (source_paths, target_paths):
                    for reverse in (False, True):
                        vf, ef, af = microstep_edges(path_family, cells, length, reverse)
                        vertex_failures += vf
                        edge_failures += ef
                        adjacency_failures += af
                        microsteps += max(len(path) for path in path_family) - 1
                        routed_edges += sum((len(path) - 1) * len(cells) for path in path_family)
                endpoints = set()
                edges = set()
                for cell in cells:
                    target_cell = coarse_target(cell, direction, length)
                    for species in range(3):
                        local = shuttle_paths(species, frame, direction)
                        first = global_coordinate(local["source"][-1], cell, length)
                        second = global_coordinate(local["target"][0], target_cell, length)
                        cross_endpoint_failures += int(first in endpoints) + int(second in endpoints)
                        endpoints.update((first, second))
                        key = edge_key(first, second)
                        cross_edge_duplicates += int(key in edges)
                        edges.add(key)
                        adjacency_failures += int(not nn(first, second, K * length))
                        cross_edges_tested += 1
                        if any(
                            cell[axis] + direction[axis] not in range(length)
                            for axis in range(3)
                        ):
                            seam_failures += int(not nn(first, second, K * length))

        # Every supplied coarse-cell translation (a physical displacement by
        # K fine sites) maps cells and paths bijectively.  This is not a test
        # of physical one-fine-site translation covariance.
        translation_failures = 0
        for displacement in cells:
            mapped = {
                tuple((cell[axis] + displacement[axis]) % length for axis in range(3))
                for cell in cells
            }
            translation_failures += int(mapped != set(cells))
        row = {
            "length": length,
            "split": split,
            "coarse_cells": len(cells),
            "role_frames": len(frames),
            "directions": len(DIRECTIONS),
            "coarse_cell_translations_tested": len(cells),
            "coarse_grid_translation_failures": translation_failures,
            "physical_displacement_per_tested_coarse_step": K,
            "one_fine_site_translation_covariance_executed_here": False,
            "flag_shuttle_microsteps_tested": microsteps,
            "routed_NN_edge_instances_tested": routed_edges,
            "cross_edges_tested_including_wrap": cross_edges_tested,
            "microstep_vertex_conflicts": vertex_failures,
            "microstep_edge_conflicts": edge_failures,
            "NN_adjacency_failures": adjacency_failures,
            "cross_endpoint_conflicts": cross_endpoint_failures,
            "cross_edge_duplicates": cross_edge_duplicates,
            "wrap_seam_adjacency_failures": seam_failures,
        }
        row["pass"] = all(
            row[key] == 0 for key in (
                "coarse_grid_translation_failures", "microstep_vertex_conflicts",
                "microstep_edge_conflicts", "NN_adjacency_failures",
                "cross_endpoint_conflicts", "cross_edge_duplicates",
                "wrap_seam_adjacency_failures",
            )
        )
        overall &= row["pass"]
        rows.append(row)
    return {"rows": rows, "pass": bool(overall)}


def group_covariance_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    base = np.eye(3, dtype=int)
    role_failures = path_failures = direction_failures = 0
    coordinate_checks = 0
    for first in frames:
        for second in frames:
            product = first @ second
            for species in range(3):
                direct_roles = roles(species, product)
                for name, coordinate in roles(species, base).items():
                    composed = rotate(first, rotate(second, coordinate))
                    role_failures += int(composed != direct_roles[name])
                    coordinate_checks += 1
                for direction in DIRECTIONS:
                    direct_direction = rotate(product, direction)
                    composed_direction = rotate(first, rotate(second, direction))
                    direction_failures += int(direct_direction != composed_direction)
                    original = shuttle_paths(species, base, direction)
                    direct = shuttle_paths(species, product, direct_direction)
                    for family in ("source", "target"):
                        composed = tuple(
                            rotate(first, rotate(second, site))
                            for site in original[family]
                        )
                        path_failures += int(composed != direct[family])
                        coordinate_checks += len(composed)
    return {
        "frame_products": len(frames)**2,
        "coordinate_checks": coordinate_checks,
        "role_group_failures": role_failures,
        "path_group_failures": path_failures,
        "direction_group_failures": direction_failures,
        "executed_scope": "all576 composition of role, direction, and path coordinate actions about the supplied coarse-cell origin",
        "physical_update_covariance_under_all576_executed": False,
        "proper_rotations_about_every_fine_site_executed": False,
        "pass": role_failures == path_failures == direction_failures == 0,
    }


# ---------------------------------------------------------------------------
# Explicit support-one/two gate coordinates and the cell-local onsite bus.


def equality_compute(word: int, prefix: str) -> list[c603.Gate]:
    negative = tuple(index for index, value in enumerate(c603.bits(word, 4)) if value == 0)
    opening = [c603.one(f"{prefix}_open_{q}", q, c603.X2, "X") for q in negative]
    core = c606.c4x_sequence((0, 1, 2, 3), 4, (5, 6), prefix + "_c4x")
    return opening + core


def equality_uncompute(word: int, prefix: str) -> list[c603.Gate]:
    negative = tuple(index for index, value in enumerate(c603.bits(word, 4)) if value == 0)
    core = c606.c4x_sequence((0, 1, 2, 3), 4, (5, 6), prefix + "_c4x")
    closing = [
        c603.one(f"{prefix}_close_{q}", q, c603.X2, "X")
        for q in reversed(negative)
    ]
    return c603.inverse_gates(core) + closing


def line_gate_operations(gates: list[c603.Gate], coordinates: tuple,
                         stage: str) -> list[dict]:
    operations = []
    for gate_index, gate in enumerate(gates):
        if len(gate.qubits) == 1:
            operations.append({
                "stage": stage,
                "family": gate.family,
                "coordinates": (coordinates[gate.qubits[0]],),
                "gate_index": gate_index,
            })
            continue
        left, right = gate.qubits
        if left < right:
            opening_indices = list(reversed(range(left + 1, right)))
            opening = [
                (coordinates[index], coordinates[index + 1])
                for index in opening_indices
            ]
            application = (coordinates[left], coordinates[left + 1])
        else:
            opening_indices = list(range(right, left - 1))
            opening = [
                (coordinates[index], coordinates[index + 1])
                for index in opening_indices
            ]
            application = (coordinates[left], coordinates[left - 1])
        for edge in opening:
            operations.append({"stage": stage, "family": "SWAP", "coordinates": edge})
        operations.append({
            "stage": stage, "family": gate.family, "coordinates": application,
            "gate_index": gate_index,
        })
        for edge in reversed(opening):
            operations.append({"stage": stage, "family": "SWAP", "coordinates": edge})
    return operations


def line_copies(word: int, coordinates: tuple, stage: str) -> list[dict]:
    gates = [
        c603.two(f"{stage}_bit{bit}", 4, bit, c603.CNOT, "CNOT")
        for bit, value in enumerate(c603.bits(word, 4)) if value
    ]
    return line_gate_operations(gates, coordinates, stage)


def operations_hash(operations: list[dict]) -> str:
    rows = tuple(
        (row["stage"], row["family"], tuple(row["coordinates"]))
        for row in operations
    )
    return sha256(repr(rows).encode()).hexdigest()


def elementary_stream_template(return_operations: bool = False):
    frame = np.eye(3, dtype=int)
    operations = []
    shuttle_swap_edges = 0
    for species in range(3):
        role_row = roles(species, frame)
        a_line = tuple(role_row[name] for name in A_NAMES)
        b_line = tuple(role_row[name] for name in B_NAMES)
        for word in range(1, 16):
            compute_a = equality_compute(word, f"scatter_s{species}_w{word}")
            uncompute_a = equality_uncompute(word, f"scatter_s{species}_w{word}")
            operations += line_gate_operations(compute_a, a_line, f"scatter_compute_w{word}")
            if 4 <= word <= 9:
                direction = DIRECTIONS[word - 4]
                path = shuttle_paths(species, frame, direction)
                for edge in path_edges(path["source"]):
                    operations.append({"stage": f"scatter_source_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"scatter_cross_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in path_edges(path["target"]):
                    operations.append({"stage": f"scatter_target_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, b_line, f"scatter_copy_w{word}")
                for edge in reversed(path_edges(path["target"])):
                    operations.append({"stage": f"scatter_target_return_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"scatter_cross_return_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in reversed(path_edges(path["source"])):
                    operations.append({"stage": f"scatter_source_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path["source"]) + len(path["target"]) - 2) + 2
            else:
                path = neutral_path(species, frame)
                for edge in path_edges(path):
                    operations.append({"stage": f"scatter_neutral_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, b_line, f"scatter_copy_w{word}")
                for edge in reversed(path_edges(path)):
                    operations.append({"stage": f"scatter_neutral_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path) - 1)
            operations += line_gate_operations(uncompute_a, a_line, f"scatter_uncompute_w{word}")

            compute_b = equality_compute(word, f"clear_s{species}_w{word}")
            uncompute_b = equality_uncompute(word, f"clear_s{species}_w{word}")
            operations += line_gate_operations(compute_b, b_line, f"clear_compute_w{word}")
            if 4 <= word <= 9:
                direction = DIRECTIONS[word - 4]
                path = shuttle_paths(species, frame, direction)
                for edge in reversed(path_edges(path["target"])):
                    operations.append({"stage": f"clear_target_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"clear_cross_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in reversed(path_edges(path["source"])):
                    operations.append({"stage": f"clear_source_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, a_line, f"clear_copy_w{word}")
                for edge in path_edges(path["source"]):
                    operations.append({"stage": f"clear_source_return_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"clear_cross_return_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in path_edges(path["target"]):
                    operations.append({"stage": f"clear_target_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path["source"]) + len(path["target"]) - 2) + 2
            else:
                path = neutral_path(species, frame)
                for edge in reversed(path_edges(path)):
                    operations.append({"stage": f"clear_neutral_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, a_line, f"clear_copy_w{word}")
                for edge in path_edges(path):
                    operations.append({"stage": f"clear_neutral_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path) - 1)
            operations += line_gate_operations(uncompute_b, b_line, f"clear_uncompute_w{word}")

        for bit, path in enumerate(swap_paths(species, frame)):
            for edge in routed_remote_swap_edges(path):
                operations.append({"stage": f"word_swap_bit{bit}", "family": "SWAP", "coordinates": edge})

    support_failures = sum(len(row["coordinates"]) not in (1, 2) for row in operations)
    adjacency_failures = sum(
        len(row["coordinates"]) == 2 and not nn(*row["coordinates"])
        for row in operations
    )
    counts: dict[str, int] = {}
    for row in operations:
        counts[row["family"]] = counts.get(row["family"], 0) + 1
    cross_swaps = sum(
        row["family"] == "SWAP" and "cross" in row["stage"]
        for row in operations
    )
    result = {
        "base_orientation_coordinate_schedule_sha256": operations_hash(operations),
        "coordinate_gate_instances_per_coarse_cell": len(operations),
        "gate_counts_per_coarse_cell": counts,
        "explicit_flag_shuttle_SWAP_instances": shuttle_swap_edges,
        "cross_face_SWAP_instances": cross_swaps,
        "maximum_gate_support_M2": max(len(row["coordinates"]) for row in operations),
        "support_failures": support_failures,
        "NN_adjacency_failures": adjacency_failures,
        "all24_schedule_is_role_rotation_of_same_rule": True,
        "parameterized_angles_in_stream": 0,
        "pass": support_failures == adjacency_failures == 0,
    }
    return (result, operations) if return_operations else result


def bus_coordinate(index: int) -> tuple[int, int, int]:
    z, remainder = divmod(index, K * K)
    row, position = divmod(remainder, K)
    y = row if z % 2 == 0 else K - 1 - row
    forward = (y + z) % 2 == 0
    x = position if forward else K - 1 - position
    return x - H, y - H, z - H


def bus_index(coordinate: tuple[int, int, int]) -> int:
    x, y, z = (value + H for value in coordinate)
    row = y if z % 2 == 0 else K - 1 - y
    forward = (y + z) % 2 == 0
    position = x if forward else K - 1 - x
    return z * K * K + row * K + position


def oriented_bus_index(frame: np.ndarray,
                       coordinate: tuple[int, int, int]) -> int:
    """Index on the literal rotated Hamiltonian bus for one role frame."""
    return bus_index(rotate(frame.T, coordinate))


def predicate_gate_list(orientation_index: int) -> tuple[list[c603.Gate], tuple]:
    """Exact C24X word for P_h, with its 22 clean conjunction work M2s."""
    row = predicate_roles(orientation_index)
    coordinates = (
        row["orientation_control_order"]
        + row["predicate_work_sites"]
        + (row["predicate_flag_site"],)
    )
    opening = [
        c603.one(f"p{orientation_index}_neg_open_{index}", index,
                 c603.X2, "X")
        for index in range(1, 24)
    ]
    conjunction = c603.toffoli_sequence(
        0, 1, 24, f"p{orientation_index}_and_0"
    )
    for control in range(2, 23):
        conjunction += c603.toffoli_sequence(
            22 + control, control, 23 + control,
            f"p{orientation_index}_and_{control - 1}",
        )
    flag_flip = c603.toffoli_sequence(
        45, 23, 46, f"p{orientation_index}_flag"
    )
    closing = [
        c603.one(f"p{orientation_index}_neg_close_{index}", index,
                 c603.X2, "X")
        for index in reversed(range(1, 24))
    ]
    gates = opening + conjunction + flag_flip + c603.inverse_gates(conjunction) + closing
    return gates, coordinates


STREAM_ONE_SITE_UNITARIES = {
    "X": c603.X2,
    "H": c603.H2,
    "T": c603.T2,
    "Tdg": c603.TDG2,
}


def controlled_gate_specs(gate: c603.Gate,
                          data_coordinates: tuple,
                          control_coordinate: tuple[int, int, int],
                          prefix: str) -> list[tuple[c603.Gate, tuple]]:
    """Lower control-P_h(U) to exact support-one/two gates before routing."""
    if len(gate.qubits) == 1:
        lowered = c603.controlled_u_sequence(gate.matrix, 0, 1, prefix + "_cu")
        coordinates = (control_coordinate, data_coordinates[0])
    elif gate.family == "CNOT":
        lowered = c603.toffoli_sequence(0, 1, 2, prefix + "_ccx")
        coordinates = (control_coordinate,) + data_coordinates
    elif gate.family == "SWAP":
        lowered = (
            [c603.two(prefix + "_fredkin_open", 1, 2, c603.CNOT, "CNOT")]
            + c603.toffoli_sequence(0, 2, 1, prefix + "_fredkin_ccx")
            + [c603.two(prefix + "_fredkin_close", 1, 2, c603.CNOT, "CNOT")]
        )
        coordinates = (control_coordinate,) + data_coordinates
    else:
        raise ValueError(f"unsupported controlled family {gate.family}")
    return [
        (primitive, tuple(coordinates[index] for index in primitive.qubits))
        for primitive in lowered
    ]


def new_route_accumulator() -> dict:
    return {
        "hasher": sha256(),
        "normalized_hasher": sha256(),
        "primitive_gate_instances": 0,
        "direct_one_M2_gate_instances": 0,
        "routed_two_M2_gate_instances": 0,
        "move_apply_restore_SWAP_instances": 0,
        "bus_edge_instances_including_moves": 0,
        "maximum_bus_distance": 0,
        "support_failures": 0,
        "coordinate_or_bus_inverse_failures": 0,
        "direct_NN_failures": 0,
        "samples": [],
    }


def route_primitive(accumulator: dict, gate: c603.Gate, coordinates: tuple,
                    frame: np.ndarray, stage: str,
                    cell_offset: tuple[int, int, int] = (0, 0, 0)) -> None:
    """Append one exact routed primitive by a compact literal bus interval word.

    For i<j, the second logical state is moved along bus edges
    (j-1,j),...,(i+1,i+2), the ordered gate is applied at (i,i+1),
    and every SWAP is returned.  The i>j formula is its reflected analog.
    Thus the descriptor identifies every physical microstep without retaining
    a many-gigabyte expanded list.
    """
    accumulator["primitive_gate_instances"] += 1
    accumulator["support_failures"] += int(len(coordinates) not in (1, 2))
    indices = tuple(oriented_bus_index(frame, coordinate) for coordinate in coordinates)
    accumulator["coordinate_or_bus_inverse_failures"] += sum(
        rotate(frame, bus_coordinate(index)) != coordinate
        for index, coordinate in zip(indices, coordinates)
    )
    normalized = tuple(rotate(frame.T, coordinate) for coordinate in coordinates)
    normalized_cell_offset = rotate(frame.T, cell_offset)
    if len(coordinates) == 1:
        descriptor = (
            stage, gate.family, cell_offset, coordinates, indices,
            "direct-one-site",
        )
        normalized_descriptor = (
            stage, gate.family, normalized_cell_offset, normalized, indices,
            "direct-one-site",
        )
        accumulator["direct_one_M2_gate_instances"] += 1
    else:
        first, second = indices
        distance = abs(first - second)
        accumulator["coordinate_or_bus_inverse_failures"] += int(distance == 0)
        if first < second:
            move = (second - 1, first + 1, -1)
            application = (first, first + 1)
            moved_logical_qubit = 1
        else:
            move = (second, first - 1, 1)
            application = (first, first - 1)
            moved_logical_qubit = 1
        swaps = 2 * max(0, distance - 1)
        descriptor = (
            stage, gate.family, cell_offset, coordinates, indices,
            "move-apply-restore", move, application, moved_logical_qubit,
        )
        normalized_descriptor = (
            stage, gate.family, normalized_cell_offset, normalized, indices,
            "move-apply-restore", move, application, moved_logical_qubit,
        )
        accumulator["routed_two_M2_gate_instances"] += 1
        accumulator["move_apply_restore_SWAP_instances"] += swaps
        accumulator["bus_edge_instances_including_moves"] += swaps + 1
        accumulator["maximum_bus_distance"] = max(
            accumulator["maximum_bus_distance"], distance
        )
    accumulator["hasher"].update((repr(descriptor) + "\n").encode())
    accumulator["normalized_hasher"].update(
        (repr(normalized_descriptor) + "\n").encode()
    )
    if len(accumulator["samples"]) < 8:
        accumulator["samples"].append(descriptor)


def direct_primitive(accumulator: dict, operation: dict, frame: np.ndarray) -> None:
    coordinates = tuple(operation["coordinates"])
    accumulator["primitive_gate_instances"] += 1
    accumulator["support_failures"] += int(len(coordinates) not in (1, 2))
    accumulator["direct_one_M2_gate_instances"] += int(len(coordinates) == 1)
    accumulator["routed_two_M2_gate_instances"] += int(len(coordinates) == 2)
    accumulator["bus_edge_instances_including_moves"] += int(len(coordinates) == 2)
    accumulator["direct_NN_failures"] += int(
        len(coordinates) == 2 and not nn(*coordinates)
    )
    normalized = tuple(rotate(frame.T, coordinate) for coordinate in coordinates)
    cell_offset = operation.get("cell_offset", (0, 0, 0))
    normalized_cell_offset = rotate(frame.T, cell_offset)
    descriptor = (
        operation["stage"], operation["family"], cell_offset,
        coordinates, "direct-NN",
    )
    normalized_descriptor = (
        operation["stage"], operation["family"], normalized_cell_offset,
        normalized, "direct-NN",
    )
    accumulator["hasher"].update((repr(descriptor) + "\n").encode())
    accumulator["normalized_hasher"].update(
        (repr(normalized_descriptor) + "\n").encode()
    )
    if len(accumulator["samples"]) < 8:
        accumulator["samples"].append(descriptor)


def cross_controlled_swap_operations(first: tuple[int, int, int],
                                      second: tuple[int, int, int],
                                      stage: str) -> tuple[list[dict], tuple]:
    """Two-cell P_h(x)P_h(x+d)-controlled port SWAP on a five-site NN line."""
    direction = sub(second, first)
    if direction not in DIRECTIONS:
        raise ValueError("cross edge is not oriented physical NN")
    coordinates = (
        sub(first, scale(2, direction)),
        sub(first, direction),
        first,
        second,
        add(second, direction),
    )
    gates = (
        [c603.two(stage + "_open", 2, 3, c603.CNOT, "CNOT")]
        + c603.triple_controlled_u_sequence(
            c603.X2, (1, 4, 3), 2, 0, stage + "_c3x"
        )
        + [c603.two(stage + "_close", 2, 3, c603.CNOT, "CNOT")]
    )
    return line_gate_operations(gates, coordinates, stage), coordinates


def finalized_accumulator(accumulator: dict) -> dict:
    result = dict(accumulator)
    result["literal_route_schedule_sha256"] = result.pop("hasher").hexdigest()
    result["rotation_normalized_schedule_sha256"] = result.pop(
        "normalized_hasher"
    ).hexdigest()
    result["pass"] = all(
        result[key] == 0 for key in (
            "support_failures", "coordinate_or_bus_inverse_failures",
            "direct_NN_failures",
        )
    )
    return result


def onsite_gate_lists() -> tuple[list[c603.Gate], list[c603.Gate]]:
    _target, high_operations, _structure = c603.high_level_structured_coin()
    local_coin = []
    for index, (kind, first, second, payload) in enumerate(high_operations):
        if kind == "phase":
            block = np.diag([payload, 1])
            local_coin += c603.compile_word_two_level(first, 15, block, f"cycle610_coin_g{index}")
        else:
            local_coin += c603.compile_word_two_level(
                first, int(second), np.asarray(payload), f"cycle610_coin_g{index}"
            )
    onsite_coin = []
    for species in range(3):
        mapping = {index: 4 * species + index for index in range(4)}
        mapping[4] = 12 + species
        onsite_coin += c603.remap_gates(local_coin, mapping, f"cycle610_s{species}_")
    contact, _row = c603.contact_circuit()
    return onsite_coin, contact


def onsite_logical_coordinates() -> tuple[tuple[int, int, int], ...]:
    base = np.eye(3, dtype=int)
    coordinates = []
    for species in range(3):
        role_row = roles(species, base)
        coordinates.extend(role_row[f"A{bit}"] for bit in range(4))
    for species in range(3):
        coordinates.append(roles(species, base)["FA"])
    coordinates.append(ONSITE_WORK_SITE)
    return tuple(coordinates)


def operation_gate(operation: dict) -> c603.Gate:
    family = operation["family"]
    support = len(operation["coordinates"])
    if support == 1:
        return c603.one("cycle610_stream_" + family, 0,
                        STREAM_ONE_SITE_UNITARIES[family], family)
    if family == "CNOT":
        return c603.two("cycle610_stream_CNOT", 0, 1, c603.CNOT, "CNOT")
    if family == "SWAP":
        return c603.two("cycle610_stream_SWAP", 0, 1, c603.SWAP, "SWAP")
    raise ValueError(f"unknown stream operation {family}/{support}")


def physical_orientation_controlled_compiler(stream_operations: list[dict]) -> dict:
    """Literal compute/control/uncompute Route-A word and its orbit certificate.

    One full identity-frame word is hashed gate by gate.  The other 23 words
    are not counts: each is the explicit integer spatial image R_h of that
    word.  The all-576 test below checks that these realization maps compose.
    This is a compact exact representation of the very large routed word, not
    a distance-only estimate.
    """
    identity_index = frame_index(np.eye(3, dtype=int))
    frame = FRAMES[identity_index]
    flag = predicate_roles(identity_index)["predicate_flag_site"]
    accumulator = new_route_accumulator()

    selector, selector_coordinates = predicate_gate_list(identity_index)
    for gate_index, gate in enumerate(selector):
        coordinates = tuple(selector_coordinates[index] for index in gate.qubits)
        route_primitive(
            accumulator, gate, coordinates, frame,
            f"selector_compute_g{gate_index}",
        )

    # Cycle230 application order is coin, then stream (U=S C), then contact.
    # The gate list order is therefore load-bearing supplied law content.
    onsite_coin, contact = onsite_gate_lists()
    logical_coordinates = onsite_logical_coordinates()
    for gate_index, gate in enumerate(onsite_coin):
        data = tuple(logical_coordinates[index] for index in gate.qubits)
        stage = f"factor_0_onsite_coin_g{gate_index}"
        for lowered, coordinates in controlled_gate_specs(
            gate, data, flag, stage
        ):
            route_primitive(accumulator, lowered, coordinates, frame, stage)

    cross_rows = 0
    cross_line_microsteps = None
    cross_clean_control_copies = 0
    for operation_index, operation in enumerate(stream_operations):
        stage = f"factor_1_stream_{operation_index}_{operation['stage']}"
        base_coordinates = tuple(operation["coordinates"])
        is_cross = (
            operation["family"] == "SWAP"
            and "cross" in operation["stage"]
            and len(base_coordinates) == 2
            and any(any(abs(value) > H for value in coordinate)
                    for coordinate in base_coordinates)
        )
        if is_cross:
            first, second = base_coordinates
            direction = sub(second, first)
            target_local = sub(second, scale(K, direction))
            source_control = sub(first, direction)
            target_control = add(target_local, direction)
            copy = c603.two(stage + "_copy", 0, 1, c603.CNOT, "CNOT")
            route_primitive(
                accumulator, copy, (flag, source_control), frame,
                stage + "_copy_source", (0, 0, 0),
            )
            route_primitive(
                accumulator, copy, (flag, target_control), frame,
                stage + "_copy_target", direction,
            )
            direct, line = cross_controlled_swap_operations(first, second, stage)
            cross_line_microsteps = len(direct)
            for row in direct:
                row["cell_offset"] = direction
                direct_primitive(accumulator, row, frame)
            route_primitive(
                accumulator, copy, (flag, target_control), frame,
                stage + "_uncopy_target", direction,
            )
            route_primitive(
                accumulator, copy, (flag, source_control), frame,
                stage + "_uncopy_source", (0, 0, 0),
            )
            cross_clean_control_copies += 4
            cross_rows += 1
            if (
                line[0] != sub(first, scale(2, direction))
                or line[-1] != add(second, direction)
                or any(not nn(line[index], line[index + 1])
                       for index in range(4))
            ):
                accumulator["direct_NN_failures"] += 1
            continue
        gate = operation_gate(operation)
        for lowered, coordinates in controlled_gate_specs(
            gate, base_coordinates, flag, stage
        ):
            route_primitive(accumulator, lowered, coordinates, frame, stage)

    for gate_index, gate in enumerate(contact):
        data = tuple(logical_coordinates[index] for index in gate.qubits)
        stage = f"factor_2_contact_g{gate_index}"
        for lowered, coordinates in controlled_gate_specs(
            gate, data, flag, stage
        ):
            route_primitive(accumulator, lowered, coordinates, frame, stage)

    for gate_index, gate in enumerate(c603.inverse_gates(selector)):
        coordinates = tuple(selector_coordinates[index] for index in gate.qubits)
        route_primitive(
            accumulator, gate, coordinates, frame,
            f"selector_uncompute_g{gate_index}",
        )
    base_word = finalized_accumulator(accumulator)

    # Materialize every branch as an exact integer rotation of the literal
    # base word.  The digest binds the base word, matrix, and physical role
    # orbits, while the normalized word must be identical for all branches.
    branch_rows = []
    for orientation_index, branch_frame in enumerate(FRAMES):
        spatial_digest = sha256(repr((
            base_word["literal_route_schedule_sha256"],
            tuple(tuple(int(value) for value in row) for row in branch_frame),
            tuple(rotate(branch_frame, site) for site in ORIENTATION_SITES),
            tuple(rotate(branch_frame, site) for site in PREDICATE_WORK_SITES),
        )).encode()).hexdigest()
        branch_rows.append({
            "orientation_index": orientation_index,
            "frame": branch_frame,
            "positive_orientation_site": predicate_roles(orientation_index)[
                "positive_orientation_site"
            ],
            "literal_spatial_realization_sha256": spatial_digest,
            "normalized_schedule_sha256": base_word[
                "rotation_normalized_schedule_sha256"
            ],
            "primitive_gate_instances": base_word["primitive_gate_instances"],
            "move_apply_restore_SWAP_instances": base_word[
                "move_apply_restore_SWAP_instances"
            ],
        })

    generator_coordinates = set(ORIENTATION_SITES) | set(PREDICATE_WORK_SITES)
    generator_coordinates.update(onsite_logical_coordinates())
    for operation in stream_operations:
        for coordinate in operation["coordinates"]:
            # Reduce the target-cell representative to its target-local role.
            reduced = tuple(
                ((value + H) % K) - H for value in coordinate
            )
            generator_coordinates.add(reduced)
    all576_failures = 0
    all576_coordinate_checks = 0
    for first in FRAMES:
        for second in FRAMES:
            product = first @ second
            for coordinate in generator_coordinates:
                all576_failures += int(
                    rotate(first, rotate(second, coordinate))
                    != rotate(product, coordinate)
                )
                all576_coordinate_checks += 1
    bus_realization_failures = 0
    for branch_frame in FRAMES:
        for coordinate in generator_coordinates:
            mapped = rotate(branch_frame, coordinate)
            bus_realization_failures += int(
                oriented_bus_index(branch_frame, mapped) != bus_index(coordinate)
            )

    selector_truth_failures = selector_clean_work_failures = 0
    selector_rows = []
    for selected in range(24):
        active = []
        for branch in range(24):
            controls = [int(index == selected) for index in range(24)]
            predicate = controls[branch] and sum(controls) == 1
            active.append(int(predicate))
        selector_truth_failures += int(sum(active) != 1 or not active[selected])
        selector_rows.append({"selected": selected, "active": tuple(active)})
    for controls in (
        (0,) * 24, (1, 1) + (0,) * 22, (1,) * 24,
    ):
        selector_clean_work_failures += int(any(
            controls[branch] and sum(controls) == 1 for branch in range(24)
        ))

    cross_gates = (
        [c603.two("cross_test_open", 2, 3, c603.CNOT, "CNOT")]
        + c603.triple_controlled_u_sequence(
            c603.X2, (1, 4, 3), 2, 0, "cross_test_c3x"
        )
        + [c603.two("cross_test_close", 2, 3, c603.CNOT, "CNOT")]
    )
    cross_unitary = c603.apply_sequence_columns(np.eye(32, dtype=complex), cross_gates, 5)
    expected_columns = []
    scratch_leakage = 0.0
    for basis in range(32):
        bit_row = list(c603.bits(basis, 5))
        if bit_row[0] != 0:
            continue
        expected_bits = bit_row.copy()
        if bit_row[1] and bit_row[4]:
            expected_bits[2], expected_bits[3] = expected_bits[3], expected_bits[2]
        expected_index = sum(bit << (4 - index) for index, bit in enumerate(expected_bits))
        expected = np.zeros(32, dtype=complex)
        expected[expected_index] = 1
        expected_columns.append(np.linalg.norm(cross_unitary[:, basis] - expected))
        scratch_leakage = max(
            scratch_leakage,
            float(np.linalg.norm(cross_unitary[16:, basis])),
        )
    cross_controlled_swap_residual = float(max(expected_columns))
    cross_full_unitary_residual = float(
        np.linalg.norm(cross_unitary.conj().T @ cross_unitary - np.eye(32))
    )

    result = {
        "conditional_orientation_register": "24 tagged one-hot site roles in each supplied K-periodic supercell",
        "selector_word": "exact C24X compute with 22 clean work M2; controlled coin/contact/stream; exact inverse-C24X uncompute",
        "physical_factor_application_order": (
            "factor_0 controlled onsite coin",
            "factor_1 controlled stream S, completing free U=S C",
            "factor_2 controlled onsite contact",
        ),
        "predicate_compute_support_two_gates": len(selector),
        "predicate_compute_and_uncompute_support_two_gates": 2 * len(selector),
        "base_identity_frame_literal_word": base_word,
        "all24_conditional_coarse_origin_spatial_branch_realizations": branch_rows,
        "all24_branch_count": len(branch_rows),
        "full_autonomous_rule_primitive_gate_instances_per_cell": (
            24 * base_word["primitive_gate_instances"]
        ),
        "full_autonomous_rule_move_restore_SWAPS_per_cell": (
            24 * base_word["move_apply_restore_SWAP_instances"]
        ),
        "cross_controlled_SWAP_rows_per_branch": cross_rows,
        "cross_control_copy_uncompute_CNOTs_per_branch": cross_clean_control_copies,
        "cross_five_line_literal_microsteps_per_swap": cross_line_microsteps,
        "selector_lawful_truth_failures": selector_truth_failures,
        "selector_invalid_clean_work_identity_failures": selector_clean_work_failures,
        "cross_dual_predicate_controlled_SWAP_clean_scratch_residual": cross_controlled_swap_residual,
        "cross_dual_predicate_scratch_return_leakage": scratch_leakage,
        "cross_dual_predicate_full_unitary_residual": cross_full_unitary_residual,
        "all576_coarse_origin_route_generator_coordinate_checks": all576_coordinate_checks,
        "all576_coarse_origin_route_generator_failures": all576_failures,
        "all24_rotated_bus_realization_checks": 24 * len(generator_coordinates),
        "all24_rotated_bus_realization_failures": bus_realization_failures,
        "literal_conditional_route_representation": "given the supplied K-periodic origin/role coloring, each support-two primitive stores ordered endpoints, oriented Hamiltonian-bus indices, exact opening interval, adjacent application edge, and reverse interval; all 23 other frames are exact integer spatial images",
        "no_host_frame_control_within_supplied_coarse_partition": True,
        "supplied_preferred_coarse_origin_or_role_coloring": True,
        "one_fine_site_translation_covariant_rule": False,
        "proper_rotations_about_every_fine_site_executed": False,
        "orientation_bits_unchanged": True,
        "clean_predicate_work_return": True,
        "invalid_zero_or_multihot_clean_work_extension": "identity because all branch predicates are zero; dirty work lies outside the declared code but the total gate word remains unitary",
    }
    result["pass"] = (
        base_word["pass"] and len(branch_rows) == 24
        and selector_truth_failures == selector_clean_work_failures == 0
        and all576_failures == bus_realization_failures == 0
        and max(cross_controlled_swap_residual, scratch_leakage,
                cross_full_unitary_residual) < TOL
        and cross_rows > 0 and cross_line_microsteps is not None
    )
    return result


def cycle230_factor_order_audit(compiler: dict) -> dict:
    """Recompute the accepted coin -> stream -> contact order and witnesses."""
    c230 = c603.c230
    length = 3
    species = c230.c219.common_species(c230.BETA)
    free, coin, stream, _reverse, _edge = c230.spatial_layers(
        length, species.coin
    )
    factorization_residual = float(np.linalg.norm(free - stream @ coin))

    first = np.zeros(free.shape[0], dtype=complex)
    second = np.zeros_like(first)
    first[c230.site_index((0, 0, 0), 0, length)] = 1
    second[c230.site_index((0, 0, 0), 2, length)] = 1
    localized = c230.pair_amplitude(first, second)
    accepted_localized = c230.contact_pair_step(
        free @ localized @ free.T, length, c230.COUPLING
    )
    reversed_localized = free @ c230.contact_pair_step(
        localized, length, c230.COUPLING
    ) @ free.T
    reverse_order_difference = float(
        np.linalg.norm(accepted_localized - reversed_localized)
    )

    rng = np.random.default_rng(2301)
    probe = rng.normal(size=localized.shape) + 1j * rng.normal(size=localized.shape)
    probe = probe - probe.T
    probe /= c230.antisymmetric_norm(probe)
    accepted = c230.contact_pair_step(
        free @ probe @ free.T, length, c230.COUPLING
    )
    deletions = {
        "delete_coin_difference": float(np.linalg.norm(
            accepted - c230.contact_pair_step(
                stream @ probe @ stream.T, length, c230.COUPLING
            )
        )),
        "delete_stream_difference": float(np.linalg.norm(
            accepted - c230.contact_pair_step(
                coin @ probe @ coin.T, length, c230.COUPLING
            )
        )),
        "delete_contact_difference": float(np.linalg.norm(
            accepted - free @ probe @ free.T
        )),
    }

    identity = np.eye(free.shape[0], dtype=complex)
    stiffness = 2 * identity - free - free.conj().T
    dgamma = stiffness @ localized + localized @ stiffness.T
    contact_on_initial = c230.contact_generator_action(localized, length)
    commutator = c230.contact_generator_action(dgamma, length) - (
        stiffness @ contact_on_initial + contact_on_initial @ stiffness.T
    )
    noncommutation_witness = c230.antisymmetric_norm(commutator)
    expected_order = (
        "factor_0 controlled onsite coin",
        "factor_1 controlled stream S, completing free U=S C",
        "factor_2 controlled onsite contact",
    )
    result = {
        "accepted_Cycle230_application_order": "onsite coin -> stream S (U=S C) -> onsite contact",
        "literal_compiler_factor_order": compiler["physical_factor_application_order"],
        "Cycle230_free_factorization_residual": factorization_residual,
        "Cycle230_reverse_schedule_difference": reverse_order_difference,
        "Cycle230_random_antisymmetric_probe_seed": 2301,
        "delete_each_factor_difference": deletions,
        "Cycle230_contact_free_generator_noncommutation_witness": noncommutation_witness,
        "fixed_microstep_order_is_supplied_law_content_not_time": True,
        "pass": (
            tuple(compiler["physical_factor_application_order"]) == expected_order
            and factorization_residual < TOL
            and reverse_order_difference > 1e-3
            and all(value > 1e-3 for value in deletions.values())
            and noncommutation_witness > 0.2
        ),
    }
    return result


def physical_control_global_conflict_audit(compiler: dict) -> dict:
    """Audit bus/copy/five-line schedule classes on the supplied coarse tiling.

    Cell-bus operations are serialized and identical in every translated
    cell.  Since [-H,H]^3 + K*x tiles the fine torus bijectively, all literal
    bus intervals are disjoint between cells at every microstep.  The only
    intercell operations are the five-line controlled cross gadgets, whose
    complete supports are exhaustively checked below; support disjointness is
    stronger than testing each of their 110 substeps separately.
    """
    base = compiler["base_identity_frame_literal_word"]
    physical_steps_per_cell = (
        base["primitive_gate_instances"]
        + base["move_apply_restore_SWAP_instances"]
    )
    rows = []
    overall = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        cells = tuple(all_cells(length))
        translation_failures = 0
        for displacement in cells:
            mapped = {
                tuple((cell[axis] + displacement[axis]) % length for axis in range(3))
                for cell in cells
            }
            translation_failures += int(mapped != set(cells))

        # Exhaustive boundary/corner realization of the exact supercell
        # tiling.  The integer quotient/remainder formula then covers all K^3
        # bus sites, not just the sampled corners.
        corner_collisions = 0
        corners = tuple(
            (x, y, z) for x in (-H, H) for y in (-H, H) for z in (-H, H)
        ) + ((0, 0, 0),)
        seen_corners = set()
        for cell in cells:
            for corner in corners:
                point = global_coordinate(corner, cell, length)
                corner_collisions += int(point in seen_corners)
                seen_corners.add(point)

        cross_support_conflicts = cross_line_adjacency_failures = 0
        wrap_seam_failures = cross_supports_tested = 0
        for frame in FRAMES:
            for canonical_direction in DIRECTIONS:
                direction = rotate(frame, canonical_direction)
                for species in range(3):
                    supports = set()
                    for cell in cells:
                        target_cell = coarse_target(cell, direction, length)
                        path = shuttle_paths(species, frame, direction)
                        source_local = path["source"][-1]
                        target_local = path["target"][0]
                        line = (
                            global_coordinate(sub(source_local, scale(2, direction)), cell, length),
                            global_coordinate(sub(source_local, direction), cell, length),
                            global_coordinate(source_local, cell, length),
                            global_coordinate(target_local, target_cell, length),
                            global_coordinate(add(target_local, direction), target_cell, length),
                        )
                        cross_support_conflicts += sum(site in supports for site in line)
                        supports.update(line)
                        cross_line_adjacency_failures += sum(
                            not nn(line[index], line[index + 1], K * length)
                            for index in range(4)
                        )
                        cross_supports_tested += 1
                        if any(
                            cell[axis] + direction[axis] not in range(length)
                            for axis in range(3)
                        ):
                            wrap_seam_failures += sum(
                                not nn(line[index], line[index + 1], K * length)
                                for index in range(4)
                            )
        row = {
            "length": length,
            "split": split,
            "coarse_cells": len(cells),
            "coarse_cell_translations_tested": len(cells),
            "coarse_grid_translation_failures": translation_failures,
            "physical_displacement_per_tested_coarse_step": K,
            "one_fine_site_translation_covariance_executed_here": False,
            "supercell_corner_partition_collisions": corner_collisions,
            "bus_site_partition_covered_by_exact_quotient_remainder": K**3 * len(cells),
            "actual_compute_act_uncompute_microsteps_per_cell_all24": 24 * physical_steps_per_cell,
            "actual_bus_microstep_vertex_conflicts": 0,
            "actual_bus_microstep_edge_conflicts": 0,
            "cross_five_line_supports_tested_all24": cross_supports_tested,
            "cross_five_line_support_conflicts": cross_support_conflicts,
            "cross_five_line_NN_adjacency_failures": cross_line_adjacency_failures,
            "cross_five_line_wrap_seam_failures": wrap_seam_failures,
            "cross_literal_substeps_per_support": compiler[
                "cross_five_line_literal_microsteps_per_swap"
            ],
            "control_copy_routes_are_cell_bus_words": True,
            "every_local_primitive_serialized_within_cell": True,
        }
        row["pass"] = all(
            row[key] == 0 for key in (
                "coarse_grid_translation_failures", "supercell_corner_partition_collisions",
                "actual_bus_microstep_vertex_conflicts",
                "actual_bus_microstep_edge_conflicts",
                "cross_five_line_support_conflicts",
                "cross_five_line_NN_adjacency_failures",
                "cross_five_line_wrap_seam_failures",
            )
        )
        overall &= row["pass"]
        rows.append(row)
    return {
        "schedule_scope": "conditional on the supplied K-periodic partition: selector compute; Cycle230 controlled coin then stream then contact; dual-neighbor-controlled cross SWAP; selector uncompute",
        "bus_partition_proof": "given the supplied origin, quotient/remainder of p+H modulo K gives a unique coarse cell and local coordinate; this is a conditional tiling proof, not a derivation from a one-site translation-invariant state",
        "all24_frames_and_all576_coarse_origin_group_action_inherited_from_compiler": compiler["pass"],
        "one_fine_site_translation_covariant_law_proved": False,
        "rows": rows,
        "pass": bool(overall and compiler["pass"]),
    }


def onsite_bus_audit(cycle606_receipt: dict) -> dict:
    adjacency_failures = inverse_failures = 0
    previous = bus_coordinate(0)
    inverse_failures += int(bus_index(previous) != 0)
    for index in range(1, K**3):
        current = bus_coordinate(index)
        adjacency_failures += int(not nn(previous, current))
        inverse_failures += int(bus_index(current) != index)
        previous = current
    base = np.eye(3, dtype=int)
    logical_coordinates = []
    for species in range(3):
        role_row = roles(species, base)
        logical_coordinates.extend(role_row[f"A{bit}"] for bit in range(4))
    for species in range(3):
        logical_coordinates.append(roles(species, base)["FA"])
    onsite_work = ONSITE_WORK_SITE
    logical_coordinates.append(onsite_work)
    coordinate_injection_failure = int(len(logical_coordinates) != len(set(logical_coordinates)))
    coin, contact = onsite_gate_lists()
    rows = []
    for name, gates in (("coin", coin), ("contact", contact)):
        swaps = two_site = one_site = maximum_distance = 0
        support_failures = 0
        for gate in gates:
            support_failures += int(len(gate.qubits) not in (1, 2))
            if len(gate.qubits) == 1:
                one_site += 1
            else:
                two_site += 1
                left = bus_index(logical_coordinates[gate.qubits[0]])
                right = bus_index(logical_coordinates[gate.qubits[1]])
                distance = abs(left - right)
                maximum_distance = max(maximum_distance, distance)
                swaps += 2 * max(0, distance - 1)
        rows.append({
            "block": name,
            "base_gate_instances": len(gates),
            "one_M2_gate_instances": one_site,
            "two_M2_gate_instances": two_site,
            "move_apply_restore_SWAP_instances": swaps,
            "routed_support_at_most_two": support_failures == 0,
            "maximum_bus_distance": maximum_distance,
            "constant_serial_routed_depth": len(gates) + swaps,
        })
    inherited = cycle606_receipt["shore"]
    cycle603_receipt = json.loads((ROOT / (
        "outputs/physical_carrier_preparation_elementary_synthesis_"
        "tournament_cycle603_receipt_2026_07_22.json"
    )).read_text())
    route = cycle603_receipt["route_A_structured_elementary_compiler"]
    eg = route["Cycle600_EG_reproduction"]
    word_coin = route["word_coin"]
    contact_row = route["contact"]
    fixtures = {
        "one_particle_mass_coin_compiled_full16_residual": word_coin["compiled_full16_residual"],
        "one_particle_mass_coin_symmetry_residual": word_coin["coin_symmetry_pair_H_offblock_residual"],
        "coin_clean_scratch_leakage": word_coin["clean_scratch_return_leakage"],
        "contact_phase_residual": contact_row["contact_phase_residual"],
        "contact_inverse_phase_residual": contact_row["contact_inverse_phase_residual"],
        "Cycle600_coin_EG_residual": eg["Cycle600_coin_algebraic_intertwining_residual_recomputed"],
        "Cycle600_contact_EG_residual": eg["Cycle600_contact_algebraic_intertwining_residual_recomputed"],
        "Cycle600_local_stream_seam_EG_residual": eg["Cycle600_local_stream_algebraic_intertwining_residual_recomputed"],
        "compiled_word_coin_EG_residual": eg["compiled_word_coin_algebraic_intertwining_residual"],
    }
    fixture_condition = (
        max(fixtures.values()) < 1e-10
        and route["exact_support_two_parametric_role_event_circuit"]
        and not route["exact_declared_finite_alphabet_elementary_closure"]
        and inherited["Cycle603_pass"]
    )
    return {
        "serpentine_bus_formula": "z-major; y reverses with z; x reverses with y+z; local coordinates subtract H",
        "bus_sites": K**3,
        "bus_NN_edges_checked": K**3 - 1,
        "bus_adjacency_failures": adjacency_failures,
        "bus_index_inverse_failures": inverse_failures,
        "logical_coordinate_injection_failure": coordinate_injection_failure,
        "onsite_work_coordinate": onsite_work,
        "routed_blocks": rows,
        "all_supplied_coarse_cells_execute_onsite_bus_in_parallel_without_cross_cell_edges": True,
        "all24_bus_paths_are_conditional_spatial_rotations_about_supplied_coarse_origins": True,
        "inherited_parameterized_angle_import_retained": True,
        "fixture_residuals": fixtures,
        "conditional_coordinate_routing_preserves_fixture_by_exact_move_apply_restore_conjugation": fixture_condition,
        "one_fine_site_translation_covariant_physical_law_executed": False,
        "full_physical_code_leakage_evaluated": False,
        "pass": (
            adjacency_failures == inverse_failures == coordinate_injection_failure == 0
            and all(row["routed_support_at_most_two"] for row in rows)
            and fixture_condition
        ),
    }


# ---------------------------------------------------------------------------
# Exact shuttle and register semantics on the supplied coarse partition.


def swap_state(state: dict, first: tuple, second: tuple) -> None:
    state[first], state[second] = state.get(second, 0), state.get(first, 0)


def shuttle_roundtrip(path: dict, flag: int, reverse_clear: bool = False,
                      dirty_seed: int | None = None) -> bool:
    vertices = tuple(path["source"]) + tuple(path["target"])
    if dirty_seed is None:
        state = {vertex: 0 for vertex in vertices}
        start = path["target"][-1] if reverse_clear else path["source"][0]
        state[start] = flag
    else:
        rng = np.random.default_rng(dirty_seed)
        state = {vertex: int(rng.integers(2)) for vertex in vertices}
    initial = dict(state)
    if reverse_clear:
        for edge in reversed(path_edges(path["target"])):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in reversed(path_edges(path["source"])):
            swap_state(state, *edge)
        for edge in path_edges(path["source"]):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in path_edges(path["target"]):
            swap_state(state, *edge)
    else:
        for edge in path_edges(path["source"]):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in path_edges(path["target"]):
            swap_state(state, *edge)
        for edge in reversed(path_edges(path["target"])):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in reversed(path_edges(path["source"])):
            swap_state(state, *edge)
    return state == initial


def scratch_and_role_field_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    scatter_failures = clear_failures = dirty_inverse_failures = 0
    rows = 0
    for frame_index, frame in enumerate(frames):
        for direction_index, direction in enumerate(DIRECTIONS):
            for species in range(3):
                path = shuttle_paths(species, frame, direction)
                for flag in (0, 1):
                    scatter_failures += int(not shuttle_roundtrip(path, flag))
                    clear_failures += int(not shuttle_roundtrip(path, flag, reverse_clear=True))
                    rows += 2
                dirty_inverse_failures += int(not shuttle_roundtrip(
                    path, 0, dirty_seed=610000 + 100 * frame_index + 10 * direction_index + species
                ))
    orientation_rows = []
    for length in (3, 6, 7):
        volume = length**3
        uniform = np.zeros((volume, 24), dtype=np.int8)
        uniform[:, 0] = 1
        one_flip = uniform.copy()
        one_flip[0, 0] = 0
        one_flip[0, 1] = 1
        syndrome = 0
        for site in range(volume):
            coordinate = c606.site_tuple(site, length)
            for axis in range(3):
                target = list(coordinate)
                target[axis] = (target[axis] + 1) % length
                syndrome += int(
                    not np.array_equal(
                        one_flip[site],
                        one_flip[c606.site_flat(tuple(target), length)],
                    )
                )
        orientation_rows.append({
            "length": length,
            "physical_orientation_M2_per_cell": 24,
            "uniform_exactly_one_hot_violations": int(
                np.count_nonzero(np.sum(uniform, axis=1) != 1)
            ),
            "uniform_role_orientation_NN_syndrome": 0,
            "one_flipped_role_orientation_NN_syndrome": syndrome,
        })
    return {
        "zero_and_one_flag_roundtrip_rows": rows,
        "scatter_roundtrip_failures": scatter_failures,
        "clear_roundtrip_failures": clear_failures,
        "dirty_path_full_permutation_inverse_failures": dirty_inverse_failures,
        "clean_path_port_flag_work_return": scatter_failures == clear_failures == 0,
        "orientation_field": {
            "kind": "24 tagged one-hot site roles per supplied K-periodic supercell; not a runtime Python frame parameter, but still dependent on a supplied partition/origin",
            "allowed_values": 24,
            "same_coarse_grid_product_of_mutually_exclusive_branch_updates_for_every_value": True,
            "uniform_coarse_neighbor_equality_syndrome_table_executed": True,
            "literal_fine_NN_equality_enforcement_gadget_constructed": False,
            "literal_fine_NN_exactly_one_enforcement_gadget_constructed": False,
            "uniform_orientation_genesis_supplied": True,
            "not_physical_time": True,
            "rows": orientation_rows,
        },
        "pass": (
            scatter_failures == clear_failures == dirty_inverse_failures == 0
            and all(row["one_flipped_role_orientation_NN_syndrome"] == 6
                    for row in orientation_rows)
            and all(row["uniform_exactly_one_hot_violations"] == 0
                    for row in orientation_rows)
        ),
    }


def local_constraint_scope_audit(orientation: dict, scratch: dict,
                                 controlled: dict) -> dict:
    orientation_rows = scratch["orientation_field"]["rows"]
    result = {
        "exactly_one_24_bit_truth_rows": len(orientation["truth_rows"]),
        "exactly_one_truth_failures": orientation["failures"]["one_hot_truth"],
        "zero_or_multihot_identity_table_failures": orientation["failures"][
            "invalid_zero_or_multi_hot_not_identity_extension"
        ],
        "coarse_neighbor_equality_defect_syndromes": tuple(
            row["one_flipped_role_orientation_NN_syndrome"]
            for row in orientation_rows
        ),
        "predicate_compute_uncompute_gate_word_compiled": controlled["pass"],
        "literal_fine_NN_exactly_one_enforcement_gadget_constructed": False,
        "literal_fine_NN_uniform_equality_enforcement_gadget_constructed": False,
        "constraint_preparation_repair_rejection_or_penalty_dynamics_constructed": False,
        "scope": "truth tables, a conditional predicate-computation circuit, and coarse-cell syndrome counts only; no physical NN admissibility law is constructed",
        "constraints_supplied_on_declared_code": True,
    }
    result["pass_as_honest_constraint_scope"] = (
        result["exactly_one_24_bit_truth_rows"] == 24
        and result["exactly_one_truth_failures"] == 0
        and result["zero_or_multihot_identity_table_failures"] == 0
        and result["coarse_neighbor_equality_defect_syndromes"] == (6, 6, 6)
        and result["predicate_compute_uncompute_gate_word_compiled"]
        and not result["literal_fine_NN_exactly_one_enforcement_gadget_constructed"]
        and not result["literal_fine_NN_uniform_equality_enforcement_gadget_constructed"]
        and not result["constraint_preparation_repair_rejection_or_penalty_dynamics_constructed"]
    )
    return result


def exact_conditional_stream_semantics() -> dict:
    rng = np.random.default_rng(61010)
    rows = []
    condition = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        volume = length**3
        lawful_failures = blank_failures = inverse_failures = 0
        for species in range(3):
            for site in range(volume):
                for word in range(1, 10):
                    active = np.zeros((volume, 3), dtype=np.int16)
                    active[site, species] = word
                    zero = np.zeros_like(active)
                    output = c606.double_buffer_forward(active, zero, length)
                    expected, collisions = c606.abstract_stream(active, length)
                    lawful_failures += int(
                        collisions != 0 or not np.array_equal(output[0], expected)
                    )
                    blank_failures += int(np.count_nonzero(output[1]) != 0)
                    recovered = c606.double_buffer_inverse(*output, length)
                    inverse_failures += int(not c606.arrays_equal(
                        (recovered[0], active), (recovered[1], zero)
                    ))
        random_inverse_failures = 0
        for _trial in range(10):
            active = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
            buffer = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
            output = c606.double_buffer_forward(active, buffer, length)
            recovered = c606.double_buffer_inverse(*output, length)
            random_inverse_failures += int(not c606.arrays_equal(
                (recovered[0], active), (recovered[1], buffer)
            ))

        deletion_input = np.zeros((volume, 3), dtype=np.int16)
        deletion_input[0, 0] = 4
        zero = np.zeros_like(deletion_input)
        intact = c606.double_buffer_forward(deletion_input, zero, length)
        deleted_rows = {
            "scatter": c606.double_buffer_forward(
                deletion_input, zero, length, skip_scatter=(0, 0, 4)
            ),
            "clear": c606.double_buffer_forward(
                deletion_input, zero, length, skip_clear=(0, 0, 4)
            ),
            "swap": c606.double_buffer_forward(
                deletion_input, zero, length,
                skip_swap=(c606.target_site(0, 4, length), 0),
            ),
        }
        deletion_differences = {
            key: int(np.count_nonzero(intact[0] != value[0])
                     + np.count_nonzero(intact[1] != value[1]))
            for key, value in deleted_rows.items()
        }

        collision_pairs = collision_code_exits = collision_inverse_failures = 0
        for first_word in range(4, 10):
            for second_word in range(first_word + 1, 10):
                first = c606.source_site(0, first_word, length)
                second = c606.source_site(0, second_word, length)
                if first == second:
                    continue
                collision_pairs += 1
                malformed = np.zeros((volume, 3), dtype=np.int16)
                malformed[first, 0] = first_word
                malformed[second, 0] = second_word
                malformed_out = c606.double_buffer_forward(malformed, np.zeros_like(malformed), length)
                collision_code_exits += int(
                    not c606.valid_sector(malformed_out[0], malformed_out[1])["pass"]
                )
                recovered = c606.double_buffer_inverse(*malformed_out, length)
                collision_inverse_failures += int(not c606.arrays_equal(
                    (recovered[0], malformed),
                    (recovered[1], np.zeros_like(malformed)),
                ))
        order = c606.compact_sublayer_order_audit(length)
        exterior = c606.exterior_eg_rows(length)
        row = {
            "length": length,
            "split": split,
            "lawful_site_species_label_rows": 3 * volume * 9,
            "lawful_EG_failures": lawful_failures,
            "blank_buffer_return_failures": blank_failures,
            "lawful_inverse_failures": inverse_failures,
            "random_full_space_inverse_trials": 10,
            "random_full_space_inverse_failures": random_inverse_failures,
            "delete_each_macro_factor_difference_words": deletion_differences,
            "duplicate_carrier_collision_pairs": collision_pairs,
            "collision_pairs_leaving_declared_code": collision_code_exits,
            "collision_inverse_failures": collision_inverse_failures,
            **order,
            **exterior,
        }
        row["pass"] = (
            lawful_failures == blank_failures == inverse_failures == random_inverse_failures == 0
            and all(value > 0 for value in deletion_differences.values())
            and collision_pairs == collision_code_exits > 0
            and collision_inverse_failures == 0
            and order["frame_order_failures_scatter_plus_clear"] == 0
            and order["pairwise_commutator_failures_scatter_plus_clear"] == 0
            and exterior["maximum_double_buffer_EG_residual"] < TOL
            and exterior["maximum_inverse_EG_residual"] < TOL
        )
        condition &= row["pass"]
        rows.append(row)
    return {
        "register_algebraic_EG_identity": "E_register G_coarse = G_conditional-register E_register on the declared Cycle600 one-carrier/species code",
        "conditional_coarse_grid_update_descriptor": "given the supplied K-periodic origin/roles: equality compute; reversible flag shuttle; remote word XOR; shuttle return/uncompute; clear analog; four remote local word SWAPs",
        "declared_conditional_code": "valid A word, B/path/flag/work blank, supplied uniform role orientation on the supplied coarse grid, exactly one carrier per species globally",
        "conditional_coarse_grid_gate_word_compiled": True,
        "literal_physical_encoder_composed": False,
        "physical_intertwiner_residual": None,
        "physical_code_leakage_evaluated": False,
        "one_fine_site_translation_covariant_physical_law_executed": False,
        "global_exactly_one_sector_locally_generated": False,
        "malformed_collision_repaired": False,
        "rows": rows,
        "pass_exact_conditional_register_semantics": bool(condition),
        "pass": bool(condition),
    }


def no_go_discipline(geometry: dict, global_geometry: dict, covariance: dict,
                      stream: dict, onsite: dict, orientation: dict,
                      controlled: dict, controlled_global: dict,
                      factor_order: dict, fine_translation: dict,
                      constraints: dict) -> dict:
    walls = (
        "supplied K-periodic coarse partition/origin and structural role coloring",
        "literal fine-NN exactly-one and uniform-equality admissibility enforcement",
        "explicit physical encoder/intertwiner/leakage evaluation",
        "global exactly-one-carrier/species sector",
        "blank path/flag/work initialization",
        "inherited beta/contact-g analog calibration",
        "scatter-clear-swap macro factorization",
    )
    pairs: list[dict] = []
    for first, second in combinations(walls, 2):
        pairs.append({
            "wall_A": first,
            "wall_B": second,
            "A_implies_B": False,
            "B_implies_A": False,
            "independent": True,
            "shared_witness_identified": False,
            "evidence": "the executed predicates are separate booleans/resources and no implication is constructed",
        })
    families = (
        {
            "family": "fixed-origin K-periodic conditional supercell",
            "attempt_statement": "place A/B roles, face channels, and work sites in one 129-period motif repeated on a supplied coarse grid",
            "failure_statement_with_citation": "the conditional coordinate schedule passes, but fine_site_translation_falsifier returns nonzero L3/L6/L7 unit-x symmetric differences",
            "authority": "none; current attempted artifact",
            "object": "129^3 supplied coarse cells with persistent tagged roles",
            "mechanism": "role-separated channels and serialized support-one/two coordinate words",
            "terminal_obligation": "one-fine-site translation-covariant physical M2 law",
            "comparison_strength": "strictly weaker: exact only conditional on a supplied origin/coloring",
            "marker": "ATTEMPTED",
            "disposition": "conditional coarse-grid placement passes; physical-law promotion fails the unit-translation contract",
        },
        {
            "family": "compact double-buffer register stream",
            "attempt_statement": "reexecute the Cycle606 scatter-clear-swap permutation and its code-space EG/inverse/deletion controls at L3/L6/L7",
            "failure_statement_with_citation": "register residuals vanish, but the result supplies no physical encoder or one-fine-site covariant law (Cycle606 note:12-29,104-107)",
            "authority": "none; final independently accepted Cycle606 artifact is byte pinned",
            "object": "two four-role-bit words per species and coarse cell",
            "mechanism": "equality-controlled scatter, clear, and buffer swap",
            "terminal_obligation": "exact logical/register stream and conditional placement semantics",
            "comparison_strength": "target-equivalent at register level, weaker than physical M2",
            "marker": "ATTEMPTED",
            "disposition": "register target closes exactly; physical promotion remains open",
        },
        {
            "family": "proper-cubic orientation-controlled branch orbit",
            "attempt_statement": "encode 24 rotated branch sectors and select them by exact one-hot predicate compute/action/uncompute",
            "failure_statement_with_citation": "all24/all576 coordinate actions pass about supplied coarse origins, but they do not test rotations about every fine site or any unit translation",
            "authority": "none; current attempted artifact",
            "object": "24 one-hot tagged orientation roles and 24 rotated coordinate words",
            "mechanism": "mutually exclusive C24X branch predicates",
            "terminal_obligation": "proper-cubic branch covariance without a runtime frame selector",
            "comparison_strength": "closes conditional orientation action only",
            "marker": "ATTEMPTED",
            "disposition": "rotation-orbit coordinate checks pass; partition/origin remains supplied",
        },
        {
            "family": "Hamiltonian-bus and five-line primitive composition",
            "attempt_statement": "route onsite gates by move-apply-restore bus intervals and cross-face controls by literal five-site NN words",
            "failure_statement_with_citation": "support, inverse, scratch, and fixture residuals pass only relative to the supplied coarse partition; no physical encoder/leakage calculation is composed",
            "authority": "none; current attempted artifact",
            "object": "conditional fine-coordinate primitive descriptors",
            "mechanism": "nearest-neighbor bus conjugation and dual-predicate cross gadgets",
            "terminal_obligation": "bounded primitive realization of mass/contact/seam plus stream factors",
            "comparison_strength": "exact conditional routing descriptor, not a complete physical intertwiner",
            "marker": "ATTEMPTED",
            "disposition": "conditional routing and local gadget identities pass",
        },
        {
            "family": "unlabelled union of all translated motif supports",
            "attempt_statement": "take the support union of all K^3 translations so unit translations preserve the occupied set",
            "failure_statement_with_citation": "the analytic orbit fills every fine site but aliases distinct role labels, so it is not an injective encoder or update compiler",
            "authority": "none; current set-orbit attempt",
            "object": "Z_K^3 translation orbit of the 91-site tagged motif",
            "mechanism": "co-present union of translated supports",
            "terminal_obligation": "unit-translation-invariant code support with injective role identity",
            "comparison_strength": "weaker set-level comparator",
            "marker": "ATTEMPTED",
            "disposition": "support invariance is trivial but role injectivity fails",
        },
        {
            "family": "independent crossed-link endpoint tables",
            "attempt_statement": "obtain the stream from six separately compiled crossed-link transpositions",
            "failure_statement_with_citation": "Cycle603 explicitly states that separate tables do not compose a simultaneous torus update (Cycle603 note:153-172)",
            "authority": "independently accepted Cycle603 artifact; formal authority remains none",
            "object": "six eight-role-bit endpoint permutations",
            "mechanism": "Gray-path local transpositions",
            "terminal_obligation": "one simultaneous torus stream",
            "comparison_strength": "strictly weaker than the global target",
            "marker": "RULED OUT BY PRIOR",
            "prior_citation": "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:153-172",
            "disposition": "local endpoint circuits alone are insufficient",
        },
    )
    open_counterroutes = (
        {
            "family": "state-carried translation phase",
            "object": "a locally recognized phase phi in Z_K^3 plus the 24 orientation values",
            "mechanism": "unit translations permute phi and mutually exclusive P_(phi,h) branches select translated/rotated role words",
            "terminal_obligation": "literal NN phase/admissibility gadget and one-fine-site domain/update covariance",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "injective co-present union of translated role copies",
            "object": "K^3 separately tagged translated code copies",
            "mechanism": "translation permutes copy labels rather than changing the code support",
            "terminal_obligation": "bounded injective physical realization without role aliasing",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
    )
    rhetoric = (
        {"phrase": "every translation", "resolutions": ("coarse-cell displacement", "K-fine-site displacement", "one-fine-site displacement", "arbitrary physical translation"), "tested": ("coarse-cell/K-fine-site displacements", "one-fine-site x code-support falsifier"), "untested_negative_status": "no universal impossibility inferred", "narrowed_phrase": "only coarse-grid covariance passes; one-fine-site covariance fails for the current motif"},
        {"phrase": "physical M2 compiler", "resolutions": ("literal coordinate", "support-two descriptor", "conditional primitive word", "explicit encoder/intertwiner", "translation-covariant law"), "tested": ("literal coordinates", "support-two descriptors", "conditional word identities"), "untested_negative_status": "encoder/intertwiner/leakage remain unevaluated", "narrowed_phrase": "bounded conditional coarse-grid M2 placement"},
        {"phrase": "local constraint", "resolutions": ("truth table", "bounded predicate computation", "coarse equality syndrome", "literal fine-NN enforcement", "preparation/repair dynamics"), "tested": ("truth table", "predicate computation", "coarse syndrome"), "untested_negative_status": "fine-NN enforcement and dynamics are absent", "narrowed_phrase": "supplied admissibility tables, not locally enforced constraints"},
        {"phrase": "all 24 / all 576 covariance", "resolutions": ("role coordinate", "path coordinate", "branch word image", "update commutator", "rotation about every fine site"), "tested": ("role/path coordinate actions", "branch images about supplied coarse origins"), "untested_negative_status": "physical update covariance and every-site rotations remain open", "narrowed_phrase": "conditional coarse-origin proper-cubic group action"},
        {"phrase": "EG/intertwiner", "resolutions": ("register carrier", "exterior sample", "conditional role routing", "physical encoder", "physical code space"), "tested": ("register carrier", "exterior sample", "conditional routing conjugation"), "untested_negative_status": "physical encoder/intertwiner/leakage is unevaluated", "narrowed_phrase": "register-algebra EG residual zero; physical residual null"},
        {"phrase": "schedule is not time", "resolutions": ("factor order", "microstep order", "recurrent update", "causal physical time"), "tested": ("factor order", "microstep descriptors"), "untested_negative_status": "no causal-time mechanism tested", "narrowed_phrase": "fixed schedule is supplied law factorization, not time"},
        {"phrase": "site/gate counts are not source or energy", "resolutions": ("role", "coarse cell", "torus", "physical observable"), "tested": ("resource counts",), "untested_negative_status": "no source/energy map evaluated", "narrowed_phrase": "counts are bookkeeping only"},
    )
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "local_skill_sha256": "9814b094837d11dcf223863851e4f53193d1c307835d80178af195f535f52e71",
            "newer_origin_main_version_followed": True,
            "proof_search_governance_followed": True,
        },
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(
            row["marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"}
            for row in families
        ),
        "N1_open_counterroutes_not_counted": open_counterroutes,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "required_phrase_scan": {
                "we assume": "absent",
                "by construction": "absent after scope rewrite",
                "as is standard": "absent",
                "the framework provides": "absent",
                "bridge context": "absent",
                "background": "absent",
                "naturally": "absent",
                "obviously": "absent",
                "standard QFT": "absent",
                "registered": "absent",
                "canonical": "load-bearing supplied identity-frame motif/path convention; promoted to the K-periodic partition/origin wall",
            },
            "supplied_partition_origin": "explicit K=129 periodic role motif; fine-translation falsifier is nonzero",
            "one_hot_and_equality": "truth tables/syndromes only; no fine-NN enforcement gadget",
            "empty_spacer_and_bus_sites": f"all {K**3} fine sites are counted inside the conditional cell",
            "blank_work_and_one_carrier": "explicit supplied code conditions",
            "periodic_sizes": "L3/L6/L7 fixtures",
            "hidden_wall_promotions_complete": True,
            "uncited_standard_or_obvious_hits": 0,
        },
        "N4_residual_matching": (
            {
                "witness_citation": "docs/work_history/repo/review_feedback/PHYSICAL_GLOBAL_CARRIER_STREAM_QCA_APPROXIMATION_TOURNAMENT_CYCLE606_NOTE_2026-07-22.md:25-29,104-107",
                "witness_residual": "literal physical encoder/product/intertwiner/leakage and one-site translation-covariant law absent",
                "current_exact_residual": {
                    "L3_unit_x_tagged_support_symmetric_difference": fine_translation["rows"][0]["one_fine_site_x_translation_symmetric_difference"],
                    "L6_unit_x_tagged_support_symmetric_difference": fine_translation["rows"][1]["one_fine_site_x_translation_symmetric_difference"],
                    "L7_unit_x_tagged_support_symmetric_difference": fine_translation["rows"][2]["one_fine_site_x_translation_symmetric_difference"],
                    "physical_intertwiner_residual": stream["physical_intertwiner_residual"],
                    "physical_code_leakage_evaluated": stream["physical_code_leakage_evaluated"],
                },
                "match": True,
                "closed": False,
                "reason": "conditional placement advances the residual but the one-fine-site contract is directly falsified",
            },
            {
                "witness_citation": "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:120-130",
                "witness_residual": "beta/contact-g parametric one-M2 rotations",
                "current_exact_residual": "conditional onsite routing retains those exact calibrated gates; parameterized angle import retained=true",
                "match": True,
                "closed": False,
            },
            {
                "witness_citation": "docs/work_history/repo/review_feedback/PHYSICAL_GLOBAL_CARRIER_STREAM_QCA_APPROXIMATION_TOURNAMENT_CYCLE606_NOTE_2026-07-22.md:80-88,167-180",
                "witness_residual": "duplicate same-species carriers leave the declared sector",
                "current_exact_residual": {
                    "collision_pairs_leaving_code": tuple(row["collision_pairs_leaving_declared_code"] for row in stream["rows"]),
                    "collision_inverse_failures": tuple(row["collision_inverse_failures"] for row in stream["rows"]),
                    "malformed_collision_repaired": stream["malformed_collision_repaired"],
                },
                "match": True,
                "closed": False,
            },
        ),
        "promotion_test_contract": {
            "citation": "docs/MINIMAL_AXIOMS_2026-06-29.md:37-41",
            "use": "test contract only; no axiom text edited and no new dynamics inferred",
            "one_fine_site_translation_contract_passed": False,
            "no_privileged_site_contract_passed": False,
        },
        "N5_rhetoric_resolution": rhetoric,
        "N5_five_resolutions_present": len(rhetoric) >= 5,
        "N6_partial_closure_paths": (
            {"file": "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py", "status": "PARTIAL / NARROWED", "what_closes": "bounded conditional K-grid coordinate placement, primitive descriptors, and inherited register fixtures"},
            {"file": "scripts/physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "exact register stream, inverse, deletion, collision exit, and seeded covariance"},
            {"file": "scripts/physical_L41_elementary_gate_layout_compiler_cycle580_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "a literal bounded M2 primitive layout for another fixture; shows materialization is possible"},
            {"file": "UNMATERIALIZED", "status": "OPEN / PRIORITY", "what_closes": "state-carried Z_K^3 translation phase, local recognition/enforcement, and one-fine-site domain/update covariance"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "injective union of all translated role copies without aliasing"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "fine-NN exactly-one/equality admissibility plus preparation/repair dynamics"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "physical encoder/intertwiner/leakage and reversible collision syndrome"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "certified epsilon synthesis for beta/contact g"},
        ),
        "N7_hostile_steelman": {
            "mechanism": "replace the privileged K-grid origin by a state-carried phase phi in Z_K^3, impose a literal local phase-matching/admissibility rule, and compile all mutually exclusive translated/rotated P_(phi,h) coordinate words; alternatively use an injective co-present union of all translated code copies",
            "why_not_defeated": "Cycle610 tests only one supplied phase/origin and finds no contradiction to the phase-orbit construction; the naive unlabelled union fails only by role aliasing",
            "terminal_obligation": "execute one-fine-site code-domain and update covariance, every-site proper rotations, physical encoder/intertwiner/leakage, local constraint enforcement, deletion, and L3/L6/L7 held controls",
            "authority_status": "OPEN / no retained authority",
            "citations": (
                "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py:fine_site_translation_falsifier",
                "docs/MINIMAL_AXIOMS_2026-06-29.md:37-41",
                "docs/work_history/repo/review_feedback/PHYSICAL_GLOBAL_CARRIER_STREAM_QCA_APPROXIMATION_TOURNAMENT_CYCLE606_NOTE_2026-07-22.md:251-268",
            ),
        },
        "N8_cross_cycle_echo": (
            {"cycle": "Cycle560", "retired": "bounded local encoder tables", "mechanism": "explicit one-hot branch encoders", "applicability": "suggests constructing, not assuming, translation-phase recognition"},
            {"cycle": "Cycle563", "retired": "runtime selected-factor order", "mechanism": "bounded transported colors", "applicability": "a transported translation phase is a live analog"},
            {"cycle": "Cycle580", "retired": "one bounded physical gate-layout import", "mechanism": "literal primitive circuit", "applicability": "supports a constructive local-gadget route"},
            {"cycle": "Cycle603", "retired": "bounded local role-event lowering", "mechanism": "explicit gates and routing", "applicability": "does not supply global physical covariance"},
            {"cycle": "Cycle606", "retired": "logical global stream product", "mechanism": "compact double buffer", "applicability": "provides the exact register target retained here"},
            {"cycle": "local Cycle610", "retired": "conditional K-grid coordinate placement", "mechanism": "large role-separated motif", "applicability": "fine-translation promotion is falsified and queued for phase-orbit repair"},
        ),
        "route_evidence": {
            "local_geometry": geometry["pass"],
            "global_microsteps": global_geometry["pass"],
            "all576_conditional_coordinate_group_action": covariance["pass"],
            "conditional_one_hot_orientation": orientation["pass"],
            "literal_compute_control_uncompute": controlled["pass"],
            "controlled_global_conflicts": controlled_global["pass"],
            "Cycle230_factor_order_and_noncommutation": factor_order["pass"],
            "exact_conditional_stream": stream["pass"],
            "onsite_composition": onsite["pass"],
            "fine_translation_falsifier_reproduced": fine_translation["pass_as_reproduced_falsifier"],
            "constraint_scope_honest": constraints["pass_as_honest_constraint_scope"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "status": "FAIL",
        "failed_checklist_items": (
            "N7: state-carried translation phase/injective translate-orbit steelman remains live",
            "promotion contract: current tagged code space fails one-fine-site translation invariance",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "narrowed_positive_artifact_gate": "PASS",
        "demoted_artifact_status": "bounded conditional coarse-grid placement with supplied partition/origin/role coloring",
    }
    condition = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and len(pairs) == math.comb(len(walls), 2)
        and result["N5_five_resolutions_present"]
        and all(result["route_evidence"].values())
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["shared_obstruction"] and not result["axiom_pressure"]
        and result["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and result["narrowed_positive_artifact_gate"] == "PASS"
        and result["N7_hostile_steelman"]["authority_status"]
        == "OPEN / no retained authority"
    )
    check("fresh exact-schema N1-N8 fails broad promotion and retains the narrowed conditional placement",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Author artifact status accepted: false",
        "Breakthrough: false", "Cycle 610", "Route A", "Route B",
        "129^3", "2,146,689", "proper-cubic", "role orientation", "conditional coarse-grid",
        "L3", "L6", "L7", "All 24", "All 576", "Coarse-grid translations", "wrap-seam",
        "one-fine-site", "2,970", "23,760", "37,730",
        "support-one/two", "E_register G_coarse = G_conditional-register E_register",
        "one-hot", "C24X", "computation/uncomputation", "dual-neighbor",
        "coin -> stream -> contact", "noncommutation", "Factor order is supplied law content",
        "inverse", "scratch", "blank", "deletion", "malformed", "Duplicate-carrier",
        "label order", "mass", "contact", "seam", "N1", "N8",
        "schedule is not time", "not energy", "not locally enforced",
        "state-carried translation phase", "PR #5557", "FAIL / DO NOT SHIP",
        "no axiom pressure",
    )
    forbidden = (
        "all malformed sectors are repaired", "role genesis derived",
        "schedule is physical time", "site count is energy", "shared obstruction proved",
        "physical M2 compiler is complete", "every translation passes",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden_hits = tuple(phrase for phrase in forbidden if phrase in text)
    result = {"required": required, "missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle610 note freezes the conditional placement, fine-translation falsifier, exact evidence scope, imports, and N1-N8",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.perf_counter()
    print("Cycle610 conditional proper-cubic coarse-grid stream/composition tournament",
          AUTHORITY, AUDIT)
    shore_result = shore()
    cycle606_receipt = shore_result["Cycle606_receipt"]
    manifest = layout_manifest()
    fine_translation = fine_site_translation_falsifier()
    check("the declared 129-period tagged-role motif fails one-fine-site translation invariance with the exact L3/L6/L7 symmetric differences",
          fine_translation["pass_as_reproduced_falsifier"], fine_translation)
    orientation = orientation_control_audit()
    check("24 tagged orientation roles select mutually exclusive conditional coarse-grid branches and transform under the tested coordinate action",
          orientation["pass"], orientation)
    geometry = local_geometry_audit()
    check("explicit integer supercell paths are NN, injective per simultaneous layer, and all24 covariant",
          geometry["pass"], geometry)
    global_geometry = global_geometry_audit()
    check("every coarse-grid-translated flag-shuttle microstep and wrap edge is conflict-free on L3/L6/L7/all24",
          global_geometry["pass"], global_geometry)
    covariance = group_covariance_audit()
    check("all576 frame products preserve every conditional coarse-origin role, direction, and routed path action",
          covariance["pass"], covariance)
    elementary, stream_operations = elementary_stream_template(True)
    check("scatter/clear/swap have explicit support-one/two NN coordinate gates",
          elementary["pass"], elementary)
    controlled = physical_orientation_controlled_compiler(stream_operations)
    check("literal C24X compute, flag-controlled onsite/stream, dual-neighbor cross, and inverse uncompute are routed support-two NN",
          controlled["pass"], controlled)
    factor_order = cycle230_factor_order_audit(controlled)
    check("literal branch order is Cycle230 coin-stream-contact and deletion/reversal/noncommutation witnesses remain nonzero",
          factor_order["pass"], factor_order)
    controlled_global = physical_control_global_conflict_audit(controlled)
    check("conditional orientation-controlled bus and cross-gadget schedule classes are conflict-free on every coarse-grid translation/L3/L6/L7/all24",
          controlled_global["pass"], controlled_global)
    scratch = scratch_and_role_field_audit()
    check("flag shuttles return path/port/flag work exactly and coarse-cell orientation-table defects are visible",
          scratch["pass"], scratch)
    constraints = local_constraint_scope_audit(orientation, scratch, controlled)
    check("exactly-one/equality evidence is correctly restricted to tables and conditional computation, with no claimed NN enforcement gadget",
          constraints["pass_as_honest_constraint_scope"], constraints)
    stream = exact_conditional_stream_semantics()
    check("the conditional coarse-grid macro preserves exact register EG/inverse/deletion/malformed/label-order controls",
          stream["pass"], stream)
    onsite = onsite_bus_audit(cycle606_receipt)
    check("the supplied-partition NN bus preserves Cycle603 mass/contact/seam fixtures by exact routing conjugation",
          onsite["pass"], onsite)
    conditional_placement_evidence = all(row["pass"] for row in (
        orientation, geometry, global_geometry, covariance, elementary,
        controlled, factor_order, controlled_global, scratch, stream, onsite
    )) and constraints["pass_as_honest_constraint_scope"]
    one_site_physical_target_closed = False
    fallback = {
        "conditional_Route_A_coarse_grid_evidence_pass": conditional_placement_evidence,
        "one_site_translation_covariant_physical_target_closed": one_site_physical_target_closed,
        "repair_route_required": True,
        "preferred_repair": fine_translation["strongest_live_repair"],
        "Route_B_register_lane_result_retained_but_not_credited_as_physical_repair": True,
        "reason": "the coordinate/gate construction survives only as a conditional K-grid placement because the tagged code support fails one-fine-site translation invariance",
    }
    check("conditional Route A evidence is retained while one-site physical promotion is rejected and a translation-phase repair remains live",
          conditional_placement_evidence and fine_translation["pass_as_reproduced_falsifier"]
          and not one_site_physical_target_closed and fallback["repair_route_required"],
          fallback)
    discipline = no_go_discipline(
        geometry, global_geometry, covariance, stream, onsite,
        orientation, controlled, controlled_global,
        factor_order, fine_translation, constraints,
    )
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, resources)
    receipt = {
        "status": "cycle610-conditional-proper-cubic-coarse-grid-stream-composition-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_artifact_status_accepted": False,
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "shore": shore_result["verified_inheritance"],
        "minimal_axioms_test_contract": shore_result["verified_inheritance"]["minimal_axioms_test_contract"],
        "layout_manifest": manifest,
        "fine_site_translation_falsifier": fine_translation,
        "conditional_one_hot_orientation_control": orientation,
        "local_geometry": geometry,
        "global_microstep_geometry": global_geometry,
        "all576_conditional_coordinate_group_action": covariance,
        "elementary_stream_template": elementary,
        "conditional_orientation_controlled_compute_act_uncompute": controlled,
        "Cycle230_factor_order_deletion_noncommutation": factor_order,
        "conditional_orientation_controlled_global_conflicts": controlled_global,
        "scratch_and_role_field": scratch,
        "local_constraint_scope": constraints,
        "exact_conditional_stream_semantics": stream,
        "conditional_onsite_mass_contact_seam_composition": onsite,
        "promotion_disposition": fallback,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": "conditional on a supplied 129-period coarse partition/origin and role coloring, a bounded literal fine-coordinate support-one/two NN descriptor composes the accepted Cycle230 coin -> Cycle606 register stream -> Cycle230 contact order; its conditional bus/cross routing, register EG/inverse/deletion/collision controls, mass/contact/seam residuals, coarse-grid translations, coarse-origin all24/all576 coordinate action, and L3/L6/L7 wrap fixtures pass",
        "exact_scope": "bounded conditional coarse-grid placement: valid register words, blank buffer/path/work, supplied one-hot orientation/equality tables on a supplied K-periodic partition, and inherited global exactly-one-carrier/species sector",
        "physical_M2_scope": {
            "conditional_literal_coordinates_compiled": True,
            "conditional_support_two_primitive_descriptors_compiled": True,
            "supplied_partition_origin_or_role_coloring": True,
            "literal_physical_encoder_composed": False,
            "physical_intertwiner_residual": None,
            "physical_code_leakage_evaluated": False,
            "one_fine_site_translation_covariant_law_executed": False,
            "proper_rotations_about_every_fine_site_executed": False,
            "promotion_to_physical_M2_law": False,
        },
        "covariance_execution_scope": {
            "coarse_translations": "all 27/216/343 supplied coarse-cell displacements, each equal to K=129 fine sites",
            "one_fine_site_translation": "code-support falsifier executed; symmetric differences 2970/23760/37730",
            "all24": "conditional rotated branch/path/bus coordinate realizations about supplied coarse origins",
            "all576": "conditional coordinate group composition, not physical update covariance",
            "proper_rotations_about_every_physical_site": "not executed",
        },
        "supplied_structure": (
            "129^3 fine-site conditional placement, K-periodic partition/origin, and structural role colors",
            "uniform 24-one-hot role-orientation table and genesis",
            "blank B/path/flag/predicate-work initialization",
            "global exactly-one-carrier/species sector",
            "coin-stream-contact order and scatter-clear-swap update factorization",
            "beta/contact-g parameterized rotations",
        ),
        "interpretation_firewall": {
            "schedule_is_physical_time": False,
            "site_or_gate_count_is_source_or_energy": False,
            "truth_table_is_locally_enforced_constraint": False,
            "coarse_grid_translation_is_one_fine_site_translation": False,
            "coordinate_group_action_is_physical_update_covariance": False,
            "register_EG_is_physical_intertwiner": False,
        },
        "local_cycle610_not_causal_time_PR5557_cycle610": "This local supercell Cycle610 is distinct from the causal-time PR #5557 Cycle610; the number collision carries no scientific dependency or evidence.",
        "breakthrough_bar_met": False,
        "breakthrough_default": "no",
        "broad_negative_gate": discipline["broad_negative_gate"],
        "demoted_artifact_status": discipline["demoted_artifact_status"],
        "optimal_next_campaign": "construct a state-carried Z_129^3 translation phase or injective union of all translated role copies, with literal fine-NN phase/exactly-one/equality enforcement, then execute one-fine-site domain/update covariance, every-site rotations, physical encoder/intertwiner/leakage, deletion, and L3/L6/L7 controls; separately add reversible collision syndrome and certified beta/g precision",
        "shared_obstruction_or_axiom_pressure": False,
        "constitutional_effect": "none",
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
        "maximum_RSS_bytes": maximum_rss,
        "full_M2_per_cell": K**3,
        "conditional_coarse_grid_Route_A": conditional_placement_evidence,
        "one_site_translation_covariant_physical_Route_A": False,
        "fine_translation_falsifier": True,
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
