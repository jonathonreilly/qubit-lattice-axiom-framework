#!/usr/bin/env python3
"""Cycle 516: Koszul-corrected proper-cubic frame bridge for Cycle 515.

Cycle 515 proves all 5,040 order isometries for one seven-cell maximal star
through global total number N<=2, but explicitly leaves physical all-order
proper-cubic covariance open.  This runner tests the missing frame bridge.

For a proper-cubic frame f, let rho_f be its affine permutation of the seven
cells, fixing the star center.  The true exterior block sign is

    C_f(label) = (-1)^sum_(i<j, rho_f(i)>rho_f(j)) n_i n_j.

The bare physical frame B_f acts on the order role by pi -> rho_f o pi and on
the physical factors by the affine Clifford map.  The exact D_pi order
characters cancel through that role transport, so B_f E7=E7 Rbar_f with only
the local direction signs.  The true exterior frame is R_f=Rbar_f C_f.
Therefore Y_f restricted to E7 is exactly C_f, with no additional D_rho
character, and K_f=B_f Y_f obeys K_f E7=E7 R_f on the declared code when the
physical cross-factor checks close.  Dense realizations of E_pi C_f E_pi^dagger,
Q, off-code completion, bounded-patch branch-shell matrix-unit application,
and constraint enforcement remain explicit supplied structure.  Primitive
synthesis and local-constraint synthesis are not proven.

The frame-certificate mode is bounded to L=5 and held L=6, the 904-dimensional
global-N<=2 code, all 24 proper-cubic frames, and all 5,040 local order roles.
Because every proper frame fixes the center cell, a nontrivial two-occupied-cell
Koszul inversion can occur only on the fifteen unordered arm--arm pairs, not
on the six center--arm pairs.
It makes no adjacent-star, recurrent-volume, Record, time, source, gravity,
Born, response, or broad TOE claim.

Authority: none.  Audit: unset.  No obstruction or axiom pressure is claimed.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
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

import physical_cycle330_all_order_isometry_bridge_cycle515_2026_07_20 as c515


c330 = c515.c330
c315 = c330.c315
c311 = c330.c311
c269 = c330.c269
c235 = c330.c235

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "frame-certificate")

TRAIN_LENGTH = 5
HELD_LENGTH = 6
EXPECTED_LABELS = 904
EXPECTED_ORDERS = math.factorial(7)
EXPECTED_FRAMES = 24
EXPECTED_FRAME_PRODUCTS = 576
EXPECTED_LOCAL_TERMS_PER_FRAME = 7 * (2 + 6 * 10 + 15 * 2)
EXPECTED_LOCAL_TERM_FRAME_TESTS = EXPECTED_FRAMES * EXPECTED_LOCAL_TERMS_PER_FRAME
LOCAL_TERM_COUNTS = {0: 2, 1: 6 * 10, 2: 15 * 2}
ALLOWED_DISTINCT_CELL_PAIR_TERMS = sum(
    LOCAL_TERM_COUNTS[left] * LOCAL_TERM_COUNTS[right]
    for left in range(3)
    for right in range(3)
    if left + right <= 2
)
EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE = (
    EXPECTED_FRAMES * 7 * 6 * ALLOWED_DISTINCT_CELL_PAIR_TERMS
)
TOLERANCE = 4e-12

RSS_CHECKPOINT_ABORT_CEILING_BYTES = 3_000_000_000
RSS_CHECKPOINT_GUARD_BYTES = 2_850_000_000
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0

CYCLE515_RUNNER = ROOT / "scripts/physical_cycle330_all_order_isometry_bridge_cycle515_2026_07_20.py"
CYCLE515_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE330_ALL_ORDER_ISOMETRY_BRIDGE_CYCLE515_NOTE_2026-07-20.md"
)
CYCLE515_DRY = ROOT / "outputs/physical_cycle330_all_order_isometry_bridge_cycle515_dry_2026_07_20.log"
CYCLE515_TARGET = ROOT / "outputs/physical_cycle330_all_order_isometry_bridge_cycle515_attempt2_2026_07_20.log"
CYCLE311_RUNNER = ROOT / "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py"
CYCLE315_RUNNER = ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py"
CYCLE330_RUNNER = ROOT / "scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py"

STRICT_FILE_HASHES = {
    CYCLE515_RUNNER: "93afe1600cb3fb8b7844729521b005ce62f957a128a6ffb9493a03a1d9932e96",
    CYCLE515_NOTE: "99696f55a6e1f8f29958d878bdbd5bb0f889c59be8707e93206d1648ba94850a",
    CYCLE515_DRY: "7ef8b552f8dd08770691c1281b354970641bb75191c5a15e26b1e54078204b56",
    CYCLE515_TARGET: "636d067ddd9284e59f24999666c5110fce425e60a7baa48d714b2a023abab1b1",
    CYCLE311_RUNNER: "4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c",
    CYCLE315_RUNNER: "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    CYCLE330_RUNNER: "4428d1f73ff315987edabd7f838a1c58414d0a982f0cd28656ddef3bd230d19f",
}

FRAMES = c235.proper_cubic_frames()
FRAME_INDEX = {tuple(frame.reshape(-1)): index for index, frame in enumerate(FRAMES)}
LABELS = c330.seven_cell_labels()
LABEL_INDEX = {label: index for index, label in enumerate(LABELS)}
PAIR_INDEX = {pair: index for index, pair in enumerate(c330.PAIR_LABELS)}
D_CHARACTER_BASIS_MASKS = (0,) + tuple(
    1 << bit for bit in range(len(c330.PAIR_LABELS))
)
EXPECTED_PHYSICAL_PAIR_MASKS = (0, 1, 2, 4, 8, 16, 32)
NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT = tuple(combinations(range(1, 7), 2))
CENTER = np.asarray(c330.CELLS[0], dtype=int)
CELL_INDEX = {cell: index for index, cell in enumerate(c330.CELLS)}


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never a physical conclusion."""


class CertificateFailure(RuntimeError):
    """A failed bounded predicate, never a substrate obstruction."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def last_json(path: Path) -> dict:
    for line in reversed(path.read_text(encoding="utf-8").splitlines()):
        if line.strip().startswith("{"):
            return json.loads(line)
    raise ValueError(f"no JSON payload in {path}")


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


def _alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def install_wall_alarm() -> dict:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, WALL_LIMIT_SECONDS)
    return {
        "hard_wall_alarm_seconds": WALL_LIMIT_SECONDS,
        "RSS_checkpoint_abort_ceiling_bytes": RSS_CHECKPOINT_ABORT_CEILING_BYTES,
        "RSS_hard_limit_installed": False,
        "zero_swap_checkpoint_monitored": True,
        "partial_rows_durable_across_OS_kill_or_process_OOM": False,
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
    dry = last_json(CYCLE515_DRY) if CYCLE515_DRY.is_file() else {}
    target = last_json(CYCLE515_TARGET) if CYCLE515_TARGET.is_file() else {}
    census = target.get("census_rows", [])
    return {
        "strict_file_hashes": actual,
        "missing_files": tuple(missing),
        "strict_hash_failures": failures,
        "Cycle515_dry_status": dry.get("status"),
        "Cycle515_dry_pass": dry.get("pass"),
        "Cycle515_dry_tests": (dry.get("tests_passed"), dry.get("tests_total")),
        "Cycle515_target_status": target.get("status"),
        "Cycle515_target_pass": target.get("pass"),
        "Cycle515_target_tests": (
            target.get("tests_passed"),
            target.get("tests_total"),
        ),
        "Cycle515_census_lengths": tuple(row.get("L") for row in census),
        "Cycle515_branch_counts": tuple(
            row.get("total_structural_branch_products") for row in census
        ),
        "Cycle515_distinct_masks": tuple(
            row.get("distinct_anticommutation_masks") for row in census
        ),
        "Cycle515_mask_hashes": tuple(
            row.get("anticommutation_mask_histogram_sha256") for row in census
        ),
        "Cycle515_maximum_RSS_bytes": target.get("maximum_RSS_bytes"),
        "Cycle515_elapsed_seconds": target.get("elapsed_seconds"),
        "Cycle515_swap_count": target.get("process_swap_count"),
        "Cycle515_all_order_covariance_status": target.get(
            "update_and_frames", {}
        ).get("all_order_proper_cubic_covariance_status"),
    }


def direction_permutation(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(c311.direction_map(frame, direction) for direction in range(6))


def validate_proper_frame(frame: np.ndarray) -> np.ndarray:
    candidate = np.asarray(frame)
    if candidate.shape != (3, 3):
        raise ValueError(f"frame must be 3x3, received {candidate.shape}")
    integral = candidate.astype(int)
    if not np.array_equal(candidate, integral):
        raise ValueError("frame entries must be integral")
    key = tuple(int(value) for value in integral.reshape(-1))
    determinant = int(round(float(np.linalg.det(integral))))
    if determinant != 1 or key not in FRAME_INDEX:
        raise ValueError(
            "Cycle516 accepts only the 24 determinant-plus-one proper-cubic frames"
        )
    return integral


def cell_permutation(frame: np.ndarray) -> tuple[int, ...]:
    frame = validate_proper_frame(frame)
    targets = []
    for cell in c330.CELLS:
        relative = np.asarray(cell, dtype=int) - CENTER
        target = tuple(int(value) for value in CENTER + frame @ relative)
        if target not in CELL_INDEX:
            raise CertificateFailure(f"frame leaves maximal star at cell {cell}: {target}")
        targets.append(CELL_INDEX[target])
    return tuple(targets)


def frame_geometry_contract() -> dict:
    cell_permutations = tuple(cell_permutation(frame) for frame in FRAMES)
    direction_permutations = tuple(direction_permutation(frame) for frame in FRAMES)
    group_failures = 0
    for left in FRAMES:
        for right in FRAMES:
            target = FRAME_INDEX[tuple((left @ right).reshape(-1))]
            left_cells = cell_permutation(left)
            right_cells = cell_permutation(right)
            composed_cells = tuple(left_cells[right_cells[index]] for index in range(7))
            group_failures += composed_cells != cell_permutations[target]
            left_directions = direction_permutation(left)
            right_directions = direction_permutation(right)
            composed_directions = tuple(
                left_directions[right_directions[index]] for index in range(6)
            )
            group_failures += composed_directions != direction_permutations[target]
    return {
        "proper_cubic_frames": len(FRAMES),
        "distinct_affine_cell_permutations": len(set(cell_permutations)),
        "distinct_direction_permutations": len(set(direction_permutations)),
        "center_fixed_failures": sum(permutation[0] != 0 for permutation in cell_permutations),
        "geometry_group_law_tests": len(FRAMES) ** 2,
        "geometry_group_law_failures": group_failures,
        "pass": (
            len(FRAMES) == EXPECTED_FRAMES
            and len(set(cell_permutations)) == EXPECTED_FRAMES
            and len(set(direction_permutations)) == EXPECTED_FRAMES
            and group_failures == 0
        ),
    }


def koszul_sign(numbers: tuple[int, ...], rho: tuple[int, ...]) -> int:
    exponent = sum(
        numbers[first] * numbers[second]
        for first in range(7)
        for second in range(first + 1, 7)
        if rho[first] > rho[second]
    )
    return -1 if exponent % 2 else 1


def local_direction_sign(label: tuple[int, ...], frame: np.ndarray) -> int:
    mapped = tuple(c311.direction_map(frame, direction) for direction in label)
    return c311.c308.permutation_sign(mapped)


def label_specs(label) -> tuple[tuple[int, tuple[int, ...]], ...]:
    return tuple(label[2 * cell : 2 * cell + 2] for cell in range(7))


def label_from_modes(modes) -> tuple:
    ordered = tuple(sorted(modes))
    result = []
    for cell in range(7):
        local = tuple(mode - 6 * cell for mode in ordered if 6 * cell <= mode < 6 * (cell + 1))
        result.extend((len(local), local))
    return tuple(result)


def logical_frame_signed_map(frame: np.ndarray, graded: bool = True):
    rho = cell_permutation(frame)
    targets = []
    phases = []
    koszul_rows = []
    factorization_failures = 0
    for label in LABELS:
        specs = label_specs(label)
        numbers = tuple(number for number, _local in specs)
        mapped_modes = tuple(
            6 * rho[cell] + c311.direction_map(frame, direction)
            for cell, (_number, local) in enumerate(specs)
            for direction in local
        )
        target_label = label_from_modes(mapped_modes)
        targets.append(LABEL_INDEX[target_label])
        full_sign = c311.c308.permutation_sign(mapped_modes)
        local_sign = math.prod(
            local_direction_sign(local, frame) for _number, local in specs
        )
        block_sign = koszul_sign(numbers, rho)
        factorization_failures += full_sign != local_sign * block_sign
        phases.append(full_sign if graded else local_sign)
        koszul_rows.append(block_sign)
    return (
        np.asarray(targets, dtype=np.int32),
        np.asarray(phases, dtype=np.int8),
        np.asarray(koszul_rows, dtype=np.int8),
        factorization_failures,
    )


def pair_cocycle_controls() -> dict:
    occupation_pairs = tuple(
        (left, right)
        for left in range(3)
        for right in range(3)
        if left + right <= 2
    )
    pair_rows = 0
    pair_failures = 0
    nontrivial_rows = 0
    for frame in FRAMES:
        rho = cell_permutation(frame)
        for first, second in combinations(range(7), 2):
            inversion = rho[first] > rho[second]
            for left_number, right_number in occupation_pairs:
                expected = -1 if inversion and (left_number * right_number) % 2 else 1
                numbers = [0] * 7
                numbers[first] = left_number
                numbers[second] = right_number
                actual = koszul_sign(tuple(numbers), rho)
                pair_rows += 1
                pair_failures += actual != expected
                nontrivial_rows += actual == -1
    return {
        "distinct_cell_pair_rows": pair_rows,
        "occupation_pairs_per_cell_pair": len(occupation_pairs),
        "nontrivial_minus_rows": nontrivial_rows,
        "pair_cocycle_failures": pair_failures,
        "pass": pair_rows == EXPECTED_FRAMES * math.comb(7, 2) * 6 and pair_failures == 0,
    }


def affine_graph_maps(code, frame: np.ndarray):
    graph = code.graph
    dmap = direction_permutation(frame)
    center = CENTER % graph.length
    vertex_map = []
    for cell, direction in graph.vertices:
        relative = np.asarray(cell, dtype=int) - center
        target_cell = tuple(
            int(value % graph.length) for value in center + frame @ relative
        )
        vertex_map.append(graph.vertex_index[(target_cell, dmap[direction])])
    edge_map = [
        graph.edge_between(vertex_map[left], vertex_map[right])
        for left, right, _kind, _owner in graph.edges
    ]
    return vertex_map, edge_map


def affine_cell_map(code, frame: np.ndarray) -> tuple[int, ...]:
    center = CENTER % code.length
    result = []
    for cell in code.graph.cells:
        relative = np.asarray(cell, dtype=int) - center
        target = tuple(int(value % code.length) for value in center + frame @ relative)
        result.append(code.graph.cells.index(target))
    return tuple(result)


def affine_transform_data(code, frame: np.ndarray):
    vertex_map, edge_map = affine_graph_maps(code, frame)
    toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
    return {
        "vertex_map": vertex_map,
        "edge_map": edge_map,
        "toggles": toggles,
        "pairs": pairs,
        "flips": flips,
        "cell_map": affine_cell_map(code, frame),
    }


def transform_full_representative(code, representative, transform_data):
    vertex_map = transform_data["vertex_map"]
    edge_map = transform_data["edge_map"]
    face_mask = (1 << code.qubits) - 1
    face = c235.Pauli(
        representative.phase,
        representative.x & face_mask,
        representative.z & face_mask,
    )
    transformed_face = c311.local.transform_pauli(
        code,
        face,
        edge_map,
        transform_data["toggles"],
        transform_data["pairs"],
        transform_data["flips"],
    )
    if representative.z & ~face_mask:
        raise CertificateFailure("Cycle516 gauge terms must have no auxiliary Z word")
    cell_map = transform_data["cell_map"]
    auxiliary = representative.x >> code.qubits
    vertex_count = len(code.graph.vertices)
    cell_count = len(code.graph.cells)
    mapped_auxiliary = 0
    for source in range(vertex_count):
        if (auxiliary >> source) & 1:
            mapped_auxiliary |= 1 << vertex_map[source]
    for source in range(cell_count):
        if (auxiliary >> (vertex_count + source)) & 1:
            mapped_auxiliary |= 1 << (vertex_count + cell_map[source])
        if (auxiliary >> (vertex_count + cell_count + source)) & 1:
            mapped_auxiliary |= 1 << (vertex_count + cell_count + cell_map[source])
    known_auxiliary_bits = vertex_count + 2 * cell_count
    if auxiliary >> known_auxiliary_bits:
        raise CertificateFailure("unexpected auxiliary word above tag/flag/companion ranges")
    return transformed_face @ c235.Pauli(x=mapped_auxiliary << code.qubits)


def gauge_terms_with_metadata(code, body, number: int, label: tuple[int, ...]):
    rows = []
    for branch in c311.common_branches(code, body, number, label, 0):
        rows.append(
            {
                "carrier": branch.carrier_direction,
                "variant": 0,
                "representative": c311.branch_representative(code, body, branch, 0),
                "amplitude": branch.amplitude / np.sqrt(2),
            }
        )
        target_slice = 0 if number == 0 else 1
        exchanged = c311.common_branches(code, body, number, label, target_slice)
        target = next(
            candidate
            for candidate in exchanged
            if candidate.carrier_direction == branch.carrier_direction
        )
        rows.append(
            {
                "carrier": branch.carrier_direction,
                "variant": 1,
                "representative": c311.branch_representative(code, body, target, 1),
                "amplitude": branch.amplitude / np.sqrt(2),
            }
        )
    return tuple(rows)


def affine_local_term_controls(length: int, started: float, partial_rows: list[dict]):
    """Test every local term and ordered cross-cell product without pruning."""

    if length < TRAIN_LENGTH:
        raise ValueError("Cycle516 requires non-aliased L>=5")
    code = c269.build_code(length)
    total_tests = 0
    target_failures = 0
    auxiliary_failures = 0
    phase_failures = 0
    normalized_stabilizer_failures = 0
    amplitude_residual = 0.0
    term_count_failures = 0
    physical_pair_tests = 0
    physical_pair_target_failures = 0
    physical_pair_reference_failures = 0
    physical_pair_cross_commutator_failures = 0
    physical_pair_stabilizer_commutator_failures = 0
    physical_pair_mask_transport_failures = 0
    physical_pair_phase_failures = 0
    physical_pair_amplitude_residual = 0.0
    physical_pair_mask_histogram = Counter()
    physical_source_pair_masks = set()
    physical_target_pair_masks = set()
    bare_physical_koszul_mismatch_witness = None
    commuting_occupied_nontrivial_koszul_arm_pairs = set()
    term_cache = {}
    mapped_cache = {}
    reducer = c315.c305.StabilizerReducer(code)
    face_mask = (1 << code.qubits) - 1
    for frame_index, frame in enumerate(FRAMES):
        rho = cell_permutation(frame)
        transform_data = affine_transform_data(code, frame)
        frame_terms = {}
        for source_cell, body in enumerate(c330.CELLS):
            frame_terms[source_cell] = {number: [] for number in range(3)}
            target_body = c330.CELLS[rho[source_cell]]
            for number in range(3):
                for label in c311.LABELS[number]:
                    source_key = (body, number, label)
                    source_rows = term_cache.setdefault(
                        source_key,
                        gauge_terms_with_metadata(code, body, number, label),
                    )
                    expected_count = c515.exact_gauge_term_contract(number)["term_count"]
                    term_count_failures += len(source_rows) != expected_count
                    mapped_label_list = tuple(
                        c311.direction_map(frame, direction) for direction in label
                    )
                    target_label = tuple(sorted(mapped_label_list))
                    local_sign = c311.c308.permutation_sign(mapped_label_list)
                    target_key = (target_body, number, target_label)
                    target_rows = mapped_cache.setdefault(
                        target_key,
                        gauge_terms_with_metadata(
                            code, target_body, number, target_label
                        ),
                    )
                    target_lookup = {
                        (row["carrier"], row["variant"]): row for row in target_rows
                    }
                    for source in source_rows:
                        target_carrier = (
                            None
                            if source["carrier"] is None
                            else c311.direction_map(frame, source["carrier"])
                        )
                        target = target_lookup.get((target_carrier, source["variant"]))
                        total_tests += 1
                        audit_row = {
                            "source_representative": source["representative"],
                            "source_amplitude": source["amplitude"],
                            "source_label": label,
                            "source_variant": source["variant"],
                            "source_carrier": source["carrier"],
                            "local_direction_sign": local_sign,
                            "transformed_representative": None,
                            "target_representative": None,
                            "target_amplitude": None,
                            "reference_stabilizer": None,
                            "reference_phase": None,
                        }
                        frame_terms[source_cell][number].append(audit_row)
                        if target is None:
                            target_failures += 1
                            continue
                        transformed = transform_full_representative(
                            code, source["representative"], transform_data
                        )
                        audit_row["transformed_representative"] = transformed
                        audit_row["target_representative"] = target["representative"]
                        audit_row["target_amplitude"] = target["amplitude"]
                        stabilizer_full = (
                            c311.local.pauli_dagger(target["representative"])
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
                            auxiliary_failures += 1
                            continue
                        normalized_stabilizer = c235.Pauli(
                            (raw_stabilizer.phase - phase) % 4,
                            raw_stabilizer.x,
                            raw_stabilizer.z,
                        )
                        if reducer.vacuum_phase(normalized_stabilizer) != 0:
                            normalized_stabilizer_failures += 1
                            continue
                        audit_row["reference_stabilizer"] = normalized_stabilizer
                        audit_row["reference_phase"] = phase
                        scalar = c311.c308.phase_scalar(phase)
                        residual = abs(
                            source["amplitude"] * scalar
                            - local_sign * target["amplitude"]
                        )
                        amplitude_residual = max(amplitude_residual, float(residual))
                        phase_failures += (
                            scalar not in (1, -1, 1j, -1j)
                            or residual >= TOLERANCE
                        )

        for first_cell in range(7):
            for second_cell in range(7):
                if first_cell == second_cell:
                    continue
                target_pair = tuple(sorted((rho[first_cell], rho[second_cell])))
                target_pair_bit = 1 << PAIR_INDEX[target_pair]
                source_pair = tuple(sorted((first_cell, second_cell)))
                source_pair_bit = 1 << PAIR_INDEX[source_pair]
                for first_number in range(3):
                    for second_number in range(3 - first_number):
                        for left in frame_terms[first_cell][first_number]:
                            for right in frame_terms[second_cell][second_number]:
                                physical_pair_tests += 1
                                transformed_left = left["transformed_representative"]
                                transformed_right = right["transformed_representative"]
                                target_left = left["target_representative"]
                                target_right = right["target_representative"]
                                left_stabilizer = left["reference_stabilizer"]
                                right_stabilizer = right["reference_stabilizer"]
                                if (
                                    transformed_left is None
                                    or transformed_right is None
                                    or target_left is None
                                    or target_right is None
                                ):
                                    physical_pair_target_failures += 1
                                    continue
                                if left_stabilizer is None or right_stabilizer is None:
                                    physical_pair_reference_failures += 1
                                    continue
                                if not left_stabilizer.commutes(target_right):
                                    physical_pair_cross_commutator_failures += 1
                                if not left_stabilizer.commutes(right_stabilizer):
                                    physical_pair_stabilizer_commutator_failures += 1

                                source_anticommutes = not left[
                                    "source_representative"
                                ].commutes(right["source_representative"])
                                transformed_anticommutes = not transformed_left.commutes(
                                    transformed_right
                                )
                                target_anticommutes = not target_left.commutes(target_right)
                                source_mask = source_pair_bit if source_anticommutes else 0
                                target_mask = target_pair_bit if target_anticommutes else 0
                                physical_source_pair_masks.add(source_mask)
                                physical_target_pair_masks.add(target_mask)
                                physical_pair_mask_histogram[
                                    (first_number, second_number, int(source_anticommutes))
                                ] += 1
                                physical_pair_mask_transport_failures += (
                                    source_anticommutes != transformed_anticommutes
                                    or permute_pair_mask(source_mask, rho) != target_mask
                                )

                                phase = (
                                    left["reference_phase"]
                                    + right["reference_phase"]
                                ) % 4
                                scalar = c311.c308.phase_scalar(phase)
                                expected_sign = (
                                    left["local_direction_sign"]
                                    * right["local_direction_sign"]
                                )
                                residual = abs(
                                    left["source_amplitude"]
                                    * right["source_amplitude"]
                                    * scalar
                                    - expected_sign
                                    * left["target_amplitude"]
                                    * right["target_amplitude"]
                                )
                                physical_pair_amplitude_residual = max(
                                    physical_pair_amplitude_residual,
                                    float(residual),
                                )
                                physical_pair_phase_failures += (
                                    scalar not in (1, -1, 1j, -1j)
                                    or residual >= TOLERANCE
                                )
                                numbers = [0] * 7
                                numbers[first_cell] = first_number
                                numbers[second_cell] = second_number
                                exterior_sign = koszul_sign(tuple(numbers), rho)
                                if (
                                    first_number == second_number == 1
                                    and not source_anticommutes
                                    and not target_anticommutes
                                    and exterior_sign == -1
                                    and scalar == expected_sign
                                    and residual < TOLERANCE
                                ):
                                    commuting_occupied_nontrivial_koszul_arm_pairs.add(
                                        source_pair
                                    )
                                    if bare_physical_koszul_mismatch_witness is None:
                                        bare_physical_koszul_mismatch_witness = {
                                            "L": length,
                                            "frame_index": frame_index,
                                            "cell_permutation": rho,
                                            "ordered_source_cells": (
                                                first_cell,
                                                second_cell,
                                            ),
                                            "numbers": tuple(numbers),
                                            "source_labels": (
                                                left["source_label"],
                                                right["source_label"],
                                            ),
                                            "source_variants": (
                                                left["source_variant"],
                                                right["source_variant"],
                                            ),
                                            "source_carriers": (
                                                left["source_carrier"],
                                                right["source_carrier"],
                                            ),
                                            "source_representatives_commute": True,
                                            "mapped_target_representatives_commute": True,
                                            "transformed_product_relative_phase": int(
                                                phase
                                            ),
                                            "bare_physical_frame_sign": int(
                                                expected_sign
                                            ),
                                            "local_direction_sign_product": int(
                                                expected_sign
                                            ),
                                            "true_exterior_Koszul_sign": exterior_sign,
                                            "deleted_Y_pair_phase_residual": float(
                                                abs(
                                                    scalar
                                                    - exterior_sign * expected_sign
                                                )
                                            ),
                                        }
        partial_rows.append(
            {
                "stage": "affine-local-and-cross-factor-terms",
                "L": length,
                "frames_completed": frame_index + 1,
                "tests_completed": total_tests,
                "ordered_distinct_cell_pair_tests_completed": physical_pair_tests,
                "failures_so_far": (
                    target_failures
                    + auxiliary_failures
                    + phase_failures
                    + normalized_stabilizer_failures
                    + physical_pair_target_failures
                    + physical_pair_reference_failures
                    + physical_pair_cross_commutator_failures
                    + physical_pair_stabilizer_commutator_failures
                    + physical_pair_mask_transport_failures
                    + physical_pair_phase_failures
                ),
                "resource": resource_checkpoint(
                    started, f"L{length}-affine-frame-{frame_index + 1}"
                ),
            }
        )
    pair_histogram_payload = json.dumps(
        sorted((key, value) for key, value in physical_pair_mask_histogram.items()),
        separators=(",", ":"),
    ).encode("utf-8")
    physical_pair_pass = (
        physical_pair_tests == EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE
        and physical_pair_target_failures == 0
        and physical_pair_reference_failures == 0
        and physical_pair_cross_commutator_failures == 0
        and physical_pair_stabilizer_commutator_failures == 0
        and physical_pair_mask_transport_failures == 0
        and physical_pair_phase_failures == 0
        and physical_pair_amplitude_residual < TOLERANCE
        and tuple(sorted(physical_source_pair_masks))
        == EXPECTED_PHYSICAL_PAIR_MASKS
        and tuple(sorted(physical_target_pair_masks))
        == EXPECTED_PHYSICAL_PAIR_MASKS
        and bare_physical_koszul_mismatch_witness is not None
        and tuple(sorted(commuting_occupied_nontrivial_koszul_arm_pairs))
        == NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT
    )
    return {
        "L": length,
        "held_size": length == HELD_LENGTH,
        "affine_local_term_frame_tests": total_tests,
        "expected_affine_local_term_frame_tests": EXPECTED_LOCAL_TERM_FRAME_TESTS,
        "target_lookup_failures": target_failures,
        "auxiliary_or_reference_failures": auxiliary_failures,
        "discrete_phase_failures": phase_failures,
        "normalized_Splus_reference_failures": normalized_stabilizer_failures,
        "term_count_failures": term_count_failures,
        "maximum_amplitude_covariance_residual": amplitude_residual,
        "ordered_distinct_cell_physical_pair_tests": physical_pair_tests,
        "expected_ordered_distinct_cell_physical_pair_tests": (
            EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE
        ),
        "ordered_distinct_cell_pairs_per_frame": 7 * 6,
        "allowed_local_term_pairs_per_ordered_cell_pair": (
            ALLOWED_DISTINCT_CELL_PAIR_TERMS
        ),
        "physical_pair_target_lookup_failures": physical_pair_target_failures,
        "physical_pair_reference_stabilizer_failures": (
            physical_pair_reference_failures
        ),
        "physical_pair_Si_Qrhoj_commutator_failures": (
            physical_pair_cross_commutator_failures
        ),
        "physical_pair_Si_Sj_commutator_failures": (
            physical_pair_stabilizer_commutator_failures
        ),
        "physical_pair_mask_transport_failures": physical_pair_mask_transport_failures,
        "physical_pair_phase_failures": physical_pair_phase_failures,
        "maximum_physical_pair_amplitude_covariance_residual": (
            physical_pair_amplitude_residual
        ),
        "physical_source_pair_masks_all_allowed_occupations": tuple(
            sorted(physical_source_pair_masks)
        ),
        "physical_target_pair_masks_all_allowed_occupations": tuple(
            sorted(physical_target_pair_masks)
        ),
        "physical_pair_mask_histogram_sha256": sha256(
            pair_histogram_payload
        ).hexdigest(),
        "bare_physical_koszul_mismatch_witness": (
            bare_physical_koszul_mismatch_witness
        ),
        "commuting_occupied_nontrivial_koszul_arm_pair_count": len(
            commuting_occupied_nontrivial_koszul_arm_pairs
        ),
        "commuting_occupied_nontrivial_koszul_arm_pairs": tuple(
            sorted(commuting_occupied_nontrivial_koszul_arm_pairs)
        ),
        "reference_stabilizer_formula": (
            "S_i=Q_rho(i)^dagger F(P_i), q_i=vacuum_phase(S_i), "
            "S_i^+=i^(-q_i) S_i with vacuum_phase(S_i^+)=0"
        ),
        "physical_pair_source_product_convention": (
            "F(P_i)F(P_j)=Q_rho(i)S_i Q_rho(j)S_j; the audited "
            "commutators reduce its reference phase to q_i+q_j"
        ),
        "physical_pair_target_product_convention": (
            "same ordered cell roles after affine mapping"
        ),
        "physical_distinct_cell_pair_pass": physical_pair_pass,
        "machine_zero_support_queries": 0,
        "magnitude_cutoff_support_queries": 0,
        "exact_structural_term_source": (
            "bound Cycle311 common branches and Cycle315 doubled gauge terms"
        ),
        "pass": (
            total_tests == EXPECTED_LOCAL_TERM_FRAME_TESTS
            and target_failures == auxiliary_failures == phase_failures == 0
            and normalized_stabilizer_failures == 0
            and term_count_failures == 0
            and amplitude_residual < TOLERANCE
            and physical_pair_pass
        ),
    }


def permute_pair_mask(mask: int, rho: tuple[int, ...]) -> int:
    output = 0
    for bit, (first, second) in enumerate(c330.PAIR_LABELS):
        if (mask >> bit) & 1:
            target = tuple(sorted((rho[first], rho[second])))
            output |= 1 << PAIR_INDEX[target]
    return output


def order_character(mask: int, order: tuple[int, ...]) -> int:
    inversion = c330.inversion_mask(order)
    return -1 if (mask & inversion).bit_count() % 2 else 1


def order_frame_transport_controls(masks: tuple[int, ...]):
    """Audit the D_pi character under the left cell action pi -> rho pi."""

    failures = 0
    role_rows = 0
    character_rows = 0
    for frame in FRAMES:
        rho = cell_permutation(frame)
        rho_order = tuple(rho)
        for order in c330.ORDERS:
            mapped_order = tuple(rho[item] for item in order)
            role_rows += 1
            for mask in masks:
                mapped_mask = permute_pair_mask(mask, rho)
                source_character = order_character(mask, order)
                transported_character = (
                    order_character(mapped_mask, mapped_order)
                    * order_character(mapped_mask, rho_order)
                )
                character_rows += 1
                failures += source_character != transported_character
    return {
        "D_character_basis_masks_tested": len(masks),
        "mask_domain": (
            "zero plus all 21 one-bit generators; character multiplicativity "
            "extends the checked identity to every 21-bit branch mask"
        ),
        "frame_order_role_rows": role_rows,
        "frame_order_character_rows": character_rows,
        "D_character_frame_transport_failures": failures,
        "D_character_relation": (
            "D_pi(m)=D_(rho pi)(rho m) D_rho(rho m)"
        ),
        "role_action_convention": (
            "pi -> rho o pi, with (rho o pi)[a]=rho[pi[a]]"
        ),
        "pass": (
            role_rows == EXPECTED_FRAMES * EXPECTED_ORDERS
            and character_rows
            == EXPECTED_FRAMES * EXPECTED_ORDERS * len(masks)
            and masks == D_CHARACTER_BASIS_MASKS
            and failures == 0
        ),
    }


def signed_map_group_controls():
    graded_maps = []
    ungraded_maps = []
    corrected_maps = []
    koszul_maps = []
    factorization_failures = 0
    combined_relation_rows = 0
    combined_relation_failures = 0
    restricted_K_intertwiner_failures = 0
    deleted_Y_residual = 0
    deleted_Y_witness = None
    for frame_index, frame in enumerate(FRAMES):
        target, phase, koszul, failures = logical_frame_signed_map(
            frame, graded=True
        )
        graded_maps.append((target, phase))
        target_u, phase_u, _ignored, failures_u = logical_frame_signed_map(
            frame, graded=False
        )
        ungraded_maps.append((target_u, phase_u))
        corrected_phase = phase_u * koszul
        corrected_maps.append((target_u, corrected_phase))
        koszul_maps.append(koszul)
        factorization_failures += failures + failures_u
        combined_relation_rows += EXPECTED_LABELS
        combined_relation_failures += np.count_nonzero(target_u != target)
        combined_relation_failures += np.count_nonzero(phase_u != phase * koszul)
        restricted_K_intertwiner_failures += np.count_nonzero(target_u != target)
        restricted_K_intertwiner_failures += np.count_nonzero(
            corrected_phase != phase
        )
        frame_deleted_residual = int(np.max(np.abs(phase_u - phase)))
        deleted_Y_residual = max(deleted_Y_residual, frame_deleted_residual)
        if frame_deleted_residual and deleted_Y_witness is None:
            label_index = int(np.flatnonzero(phase_u != phase)[0])
            deleted_Y_witness = {
                "frame_index": frame_index,
                "logical_label_index": label_index,
                "numbers": tuple(
                    number for number, _local in label_specs(LABELS[label_index])
                ),
                "R_true_exterior_sign": int(phase[label_index]),
                "Rbar_bare_physical_sign": int(phase_u[label_index]),
                "C_Koszul_sign": int(koszul[label_index]),
                "deleted_Y_intertwiner_residual": int(
                    abs(int(phase_u[label_index]) - int(phase[label_index]))
                ),
            }
    group_failures = 0
    ungraded_group_failures = 0
    restricted_K_group_failures = 0
    C_cocycle_failures = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target_index = FRAME_INDEX[tuple((left @ right).reshape(-1))]
            left_map, left_phase = graded_maps[left_index]
            right_map, right_phase = graded_maps[right_index]
            target_map, target_phase = graded_maps[target_index]
            composed_map = left_map[right_map]
            composed_phase = right_phase * left_phase[right_map]
            group_failures += np.count_nonzero(composed_map != target_map)
            group_failures += np.count_nonzero(composed_phase != target_phase)

            left_u_map, left_u_phase = ungraded_maps[left_index]
            right_u_map, right_u_phase = ungraded_maps[right_index]
            target_u_map, target_u_phase = ungraded_maps[target_index]
            composed_u_map = left_u_map[right_u_map]
            composed_u_phase = right_u_phase * left_u_phase[right_u_map]
            ungraded_group_failures += np.count_nonzero(composed_u_map != target_u_map)
            ungraded_group_failures += np.count_nonzero(
                composed_u_phase != target_u_phase
            )

            left_k_map, left_k_phase = corrected_maps[left_index]
            right_k_map, right_k_phase = corrected_maps[right_index]
            target_k_map, target_k_phase = corrected_maps[target_index]
            composed_k_map = left_k_map[right_k_map]
            composed_k_phase = right_k_phase * left_k_phase[right_k_map]
            restricted_K_group_failures += np.count_nonzero(
                composed_k_map != target_k_map
            )
            restricted_K_group_failures += np.count_nonzero(
                composed_k_phase != target_k_phase
            )
            left_C = koszul_maps[left_index]
            right_C = koszul_maps[right_index]
            target_C = koszul_maps[target_index]
            composed_C = right_C * left_C[right_k_map]
            C_cocycle_failures += np.count_nonzero(composed_C != target_C)
    return {
        "logical_code_rank": EXPECTED_LABELS,
        "proper_cubic_signed_permutations": len(graded_maps),
        "frame_group_law_products": len(FRAMES) ** 2,
        "graded_frame_group_law_failures": int(group_failures),
        "ungraded_frame_group_law_failures": int(ungraded_group_failures),
        "restricted_K_frame_group_law_failures": int(
            restricted_K_group_failures
        ),
        "C_Koszul_cocycle_rows": len(FRAMES) ** 2 * EXPECTED_LABELS,
        "C_Koszul_cocycle_failures": int(C_cocycle_failures),
        "exterior_sign_factorization_failures": factorization_failures,
        "combined_B_D_C_Y_relation_rows": combined_relation_rows,
        "combined_B_D_C_Y_relation_failures": int(combined_relation_failures),
        "combined_relation": (
            "B_f E7=E7 Rbar_f; Rbar_f=R_f C_f; "
            "Y_f E7=E7 C_f; K_f=B_f Y_f; K_f E7=E7 R_f"
        ),
        "Y_f_formula": "Y_f restricted to E7 is exactly C_f",
        "extra_bare_D_rho_character_in_Y_f": False,
        "restricted_K_E7_intertwiner_rows": len(FRAMES) * EXPECTED_LABELS,
        "restricted_K_E7_intertwiner_failures": int(
            restricted_K_intertwiner_failures
        ),
        "deleted_Y_maximum_intertwiner_residual": deleted_Y_residual,
        "deleted_Y_witness": deleted_Y_witness,
        "graded_maps": graded_maps,
        "ungraded_maps": ungraded_maps,
        "corrected_maps": corrected_maps,
        "pass": (
            len(graded_maps) == EXPECTED_FRAMES
            and group_failures == 0
            and ungraded_group_failures == 0
            and restricted_K_group_failures == 0
            and C_cocycle_failures == 0
            and factorization_failures == 0
            and combined_relation_rows == EXPECTED_FRAMES * EXPECTED_LABELS
            and combined_relation_failures == 0
            and restricted_K_intertwiner_failures == 0
            and deleted_Y_residual > 0
            and deleted_Y_witness is not None
        ),
    }


def logical_coin_without_support_pruning():
    coin = c330.c219.common_species(-0.3).coin
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(3)}
    matrix = np.zeros((EXPECTED_LABELS, EXPECTED_LABELS), dtype=complex)
    assigned_structural_entries = 0
    for source, label in enumerate(LABELS):
        specs = label_specs(label)
        source_indices = tuple(
            c311.LABEL_INDEX[number][local] for number, local in specs
        )
        target_ranges = tuple(c311.LABELS[number] for number, _local in specs)
        for target_locals in product(*target_ranges):
            coefficient = 1 + 0j
            target_label = []
            for cell, target_local in enumerate(target_locals):
                number = specs[cell][0]
                coefficient *= wedges[number][
                    c311.LABEL_INDEX[number][target_local], source_indices[cell]
                ]
                target_label.extend((number, target_local))
            matrix[LABEL_INDEX[tuple(target_label)], source] = coefficient
            assigned_structural_entries += 1
    return matrix, assigned_structural_entries


def stream_signed_map():
    mode_mapping = {}
    for edge in c330.EDGES:
        (first_cell, first_direction), (second_cell, second_direction) = edge
        first = 6 * first_cell + first_direction
        second = 6 * second_cell + second_direction
        mode_mapping[first] = second
        mode_mapping[second] = first
    targets = []
    phases = []
    for label in LABELS:
        occupied = tuple(
            6 * cell + direction
            for cell, (_number, local) in enumerate(label_specs(label))
            for direction in local
        )
        mapped = tuple(mode_mapping.get(mode, mode) for mode in occupied)
        phases.append(c311.c308.permutation_sign(mapped))
        targets.append(LABEL_INDEX[label_from_modes(mapped)])
    return np.asarray(targets, dtype=np.int32), np.asarray(phases, dtype=np.int8)


def signed_permutation_matrix(mapping, phases):
    matrix = np.zeros((len(mapping), len(mapping)), dtype=complex)
    matrix[mapping, np.arange(len(mapping))] = phases
    return matrix


def gstar_covariance_controls(group_rows: dict):
    coin, assigned_entries = logical_coin_without_support_pruning()
    stream_map, stream_phases = stream_signed_map()
    stream = signed_permutation_matrix(stream_map, stream_phases)
    contact = np.asarray(
        [
            np.exp(
                1j
                * c330.c230.COUPLING
                * sum(number * (number - 1) // 2 for number, _local in label_specs(label))
            )
            for label in LABELS
        ],
        dtype=complex,
    )
    update = contact[:, None] * (stream @ coin)
    identity = np.eye(EXPECTED_LABELS, dtype=complex)
    unitarity = float(np.linalg.norm(update.conj().T @ update - identity))
    corrected_K_residuals = []
    ungraded_residuals = []
    ungraded_witness = None
    for frame_index in range(EXPECTED_FRAMES):
        for graded, destination in (
            (True, corrected_K_residuals),
            (False, ungraded_residuals),
        ):
            mapping, phases = (
                group_rows["corrected_maps"][frame_index]
                if graded
                else group_rows["ungraded_maps"][frame_index]
            )
            left = np.empty_like(update)
            left[mapping, :] = phases[:, None] * update
            right = update[:, mapping] * phases[None, :]
            residual = float(np.linalg.norm(left - right))
            destination.append(residual)
            if not graded and residual > TOLERANCE and ungraded_witness is None:
                difference = abs(left - right)
                row, column = np.unravel_index(np.argmax(difference), difference.shape)
                ungraded_witness = {
                    "frame_index": frame_index,
                    "row": int(row),
                    "column": int(column),
                    "entry_residual": float(difference[row, column]),
                    "operator_Frobenius_residual": residual,
                }
    return {
        "logical_update_dimension": update.shape[0],
        "coin_structural_entries_assigned_without_pruning": assigned_entries,
        "machine_zero_support_queries": 0,
        "magnitude_cutoff_support_queries": 0,
        "Gstar_unitarity_residual": unitarity,
        "corrected_K_all904_frame_columns_per_frame": EXPECTED_LABELS,
        "maximum_corrected_K_Gstar_covariance_residual": max(
            corrected_K_residuals
        ),
        "maximum_ungraded_Gstar_covariance_residual": max(ungraded_residuals),
        "ungraded_Gstar_failure_witness": ungraded_witness,
        "corrected_K_frame_count": len(corrected_K_residuals),
        "ungraded_frame_count": len(ungraded_residuals),
        "pass": (
            update.shape == (EXPECTED_LABELS, EXPECTED_LABELS)
            and unitarity < TOLERANCE
            and max(corrected_K_residuals) < TOLERANCE
            and max(ungraded_residuals) > 1e-3
            and ungraded_witness is not None
        ),
    }


def supplied_physical_closure(frame_rows, order_rows, group_rows, gstar_rows):
    physical_pair_ready = all(
        row["physical_distinct_cell_pair_pass"] for row in frame_rows
    )
    restricted_K_ready = (
        group_rows["restricted_K_E7_intertwiner_failures"] == 0
        and group_rows["restricted_K_frame_group_law_failures"] == 0
        and group_rows["combined_B_D_C_Y_relation_failures"] == 0
        and group_rows["C_Koszul_cocycle_failures"] == 0
    )
    ready = (
        all(row["pass"] for row in frame_rows)
        and physical_pair_ready
        and order_rows["pass"]
        and group_rows["pass"]
        and restricted_K_ready
        and gstar_rows["pass"]
    )
    return {
        "corrected_frame": "K_f=B_f Y_f",
        "correlated_E7_frame_intertwiner": "K_f E7 = E7 R_f",
        "correlated_E7_frame_intertwiner_proven_algebraically": ready,
        "rank904_code_group_law_proven": ready,
        "Gphysical_frame_covariance_on_code_proven_algebraically": ready,
        "restricted_K_physical_group_law_proven_algebraically": ready,
        "physical_cross_factor_stabilizer_gate_pass": physical_pair_ready,
        "dense_E_pi_C_f_E_pi_dagger_supplied": True,
        "dense_Q_supplied": True,
        "off_code_completion_supplied": True,
        "bounded_patch_branch_shell_matrix_unit_application_supplied": True,
        "primitive_synthesis_proven": False,
        "local_constraint_synthesis_proven": False,
        "constraint_enforcement_supplied": True,
        "unused_13_M2_role_states_identity_completed": True,
        "physical_closure_scope": (
            "bounded seven-cell global-N<=2 Cycle515 code only; closure is "
            "conditional on supplied bounded-patch branch-shell matrix-unit "
            "application and constraint enforcement"
        ),
        "adjacent_maximal_stars_open": True,
        "recurrent_volume_open": True,
    }


def lawful_domain_controls(started: float) -> dict:
    aliased_error = None
    improper_error = None
    try:
        affine_local_term_controls(TRAIN_LENGTH - 1, started, [])
    except ValueError as error:
        aliased_error = str(error)
    reflection = np.diag((-1, 1, 1))
    try:
        validate_proper_frame(reflection)
    except ValueError as error:
        improper_error = str(error)
    return {
        "L4_attempted": True,
        "aliased_L4_rejected": aliased_error is not None,
        "aliased_L4_error": aliased_error,
        "det_minus_one_reflection_attempted": True,
        "improper_det_minus_one_frame_rejected": improper_error is not None,
        "improper_frame_error": improper_error,
        "pass": aliased_error is not None and improper_error is not None,
    }


def deletion_and_held_controls(frame_rows, group_rows, gstar_rows, lawful_rows):
    train_masks = tuple(
        frame_rows[0]["physical_source_pair_masks_all_allowed_occupations"]
    )
    held_masks = tuple(
        frame_rows[1]["physical_source_pair_masks_all_allowed_occupations"]
    )
    train_target_masks = tuple(
        frame_rows[0]["physical_target_pair_masks_all_allowed_occupations"]
    )
    held_target_masks = tuple(
        frame_rows[1]["physical_target_pair_masks_all_allowed_occupations"]
    )
    mismatch_witnesses = tuple(
        row["bare_physical_koszul_mismatch_witness"] for row in frame_rows
    )
    mismatch_residuals = tuple(
        witness["deleted_Y_pair_phase_residual"]
        for witness in mismatch_witnesses
        if witness is not None
    )
    return {
        "held_L6_matches_L5": (
            len(frame_rows) == 2
            and frame_rows[0]["affine_local_term_frame_tests"]
            == frame_rows[1]["affine_local_term_frame_tests"]
            and frame_rows[0]["maximum_amplitude_covariance_residual"]
            < TOLERANCE
            and frame_rows[1]["maximum_amplitude_covariance_residual"]
            < TOLERANCE
            and train_masks == held_masks
            and train_masks == train_target_masks
            and held_masks == held_target_masks
            and train_masks == EXPECTED_PHYSICAL_PAIR_MASKS
            and frame_rows[0]["physical_pair_mask_histogram_sha256"]
            == frame_rows[1]["physical_pair_mask_histogram_sha256"]
            and frame_rows[0]["ordered_distinct_cell_physical_pair_tests"]
            == frame_rows[1]["ordered_distinct_cell_physical_pair_tests"]
            == EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE
            and all(witness is not None for witness in mismatch_witnesses)
            and all(
                tuple(row["commuting_occupied_nontrivial_koszul_arm_pairs"])
                == NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT
                for row in frame_rows
            )
        ),
        "L5_physical_pair_masks_all_allowed_occupations": train_masks,
        "L6_physical_pair_masks_all_allowed_occupations": held_masks,
        "L5_target_pair_masks_all_allowed_occupations": train_target_masks,
        "L6_target_pair_masks_all_allowed_occupations": held_target_masks,
        "physical_bare_frame_mismatch_witnesses": mismatch_witnesses,
        "delete_Koszul_Y_pair_phase_residual": (
            max(mismatch_residuals) if mismatch_residuals else None
        ),
        "logical_delete_Koszul_Y_residual": group_rows[
            "deleted_Y_maximum_intertwiner_residual"
        ],
        "ungraded_Gstar_deletion_residual": gstar_rows[
            "maximum_ungraded_Gstar_covariance_residual"
        ],
        "lawful_domain_controls": lawful_rows,
        "aliased_L4_rejected": lawful_rows["aliased_L4_rejected"],
        "improper_det_minus_one_frames_rejected": lawful_rows[
            "improper_det_minus_one_frame_rejected"
        ],
        "deletion_pass": (
            all(witness is not None for witness in mismatch_witnesses)
            and group_rows["deleted_Y_maximum_intertwiner_residual"] > 0
            and gstar_rows["maximum_ungraded_Gstar_covariance_residual"] > 1e-3
            and lawful_rows["pass"]
        ),
    }


def boundary_contract() -> dict:
    return {
        "Cycle514_beta_or_mediator_imported": False,
        "adjacent_star_claim": False,
        "recurrent_volume_claim": False,
        "Record_claim": False,
        "physical_time_claim": False,
        "source_or_gravity_claim": False,
        "Born_or_probability_claim": False,
        "response_claim": False,
        "TOE_lane_maturity_claim": False,
        "obstruction_claim": False,
        "axiom_pressure": False,
    }


def partial_retention_fixture() -> dict:
    rows = []
    error = None
    try:
        for frame in range(4):
            if frame == 3:
                raise ResourceWall("injected caught resource wall before frame 4")
            rows.append({"frame": frame + 1, "retained": True})
    except ResourceWall as caught:
        error = str(caught)
    return {
        "retained_rows": rows,
        "retained_count": len(rows),
        "error": error,
        "scope": "caught Python exceptions only",
        "durable_across_OS_kill_or_process_OOM": False,
    }


def run_dry() -> tuple[dict, int]:
    tests = []

    def check(name: str, condition: bool, detail=None):
        tests.append({"name": name, "passed": bool(condition), "detail": detail})

    evidence = evidence_controls()
    check(
        "Cycle515 packet and Cycle311/315/330 dependencies are hash-bound",
        not evidence["missing_files"]
        and not evidence["strict_hash_failures"]
        and evidence["Cycle515_dry_status"] == "cycle515-all-order-contract-ready"
        and evidence["Cycle515_dry_pass"] is True
        and evidence["Cycle515_dry_tests"] == (14, 14)
        and evidence["Cycle515_target_status"]
        == "cycle515-all-5040-same-code-isometry-certified"
        and evidence["Cycle515_target_pass"] is True
        and evidence["Cycle515_target_tests"] == (13, 13)
        and evidence["Cycle515_census_lengths"] == (5, 6)
        and evidence["Cycle515_branch_counts"] == (2_459_648, 2_459_648)
        and evidence["Cycle515_distinct_masks"] == (7, 7)
        and len(set(evidence["Cycle515_mask_hashes"])) == 1
        and evidence["Cycle515_all_order_covariance_status"] == "OPEN",
        evidence,
    )
    geometry = frame_geometry_contract()
    check(
        "24 affine maximal-star maps and all 576 geometry products close",
        geometry["pass"],
        geometry,
    )
    pair_rows = pair_cocycle_controls()
    check(
        "the exact distinct-cell N<=2 Koszul pair cocycle closes",
        pair_rows["pass"] and pair_rows["nontrivial_minus_rows"] > 0,
        pair_rows,
    )
    source = inspect.getsource(affine_local_term_controls)
    forbidden = tuple(
        token
        for token in (
            "keep =",
            "if abs(",
            "eliminate_zeros",
            "count_nonzero",
            "term.amplitude",
        )
        if token in source
    )
    check(
        "frame target uses structural local terms without support pruning",
        not forbidden
        and "for source in source_rows" in source
        and "transform_full_representative" in source,
        {"forbidden_hits": forbidden},
    )
    target_contract = {
        "local_term_counts_by_number": LOCAL_TERM_COUNTS,
        "allowed_term_pairs_per_ordered_cell_pair": (
            ALLOWED_DISTINCT_CELL_PAIR_TERMS
        ),
        "ordered_cell_pairs_per_frame": 7 * 6,
        "proper_cubic_frames": EXPECTED_FRAMES,
        "expected_cases_per_size": EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE,
        "fixed_center_cell_index": 0,
        "nontrivial_Koszul_arm_pair_support": NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT,
        "nontrivial_Koszul_arm_pair_count": len(
            NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT
        ),
        "required_source_fragments_missing": tuple(
            fragment
            for fragment in (
                '"reference_stabilizer_formula"',
                "left_stabilizer.commutes(target_right)",
                "left_stabilizer.commutes(right_stabilizer)",
                "physical_pair_mask_transport_failures",
                "bare_physical_koszul_mismatch_witness",
                "commuting_occupied_nontrivial_koszul_arm_pairs",
            )
            if fragment not in source
        ),
    }
    check(
        "target declares the exhaustive physical cross-factor stabilizer audit",
        ALLOWED_DISTINCT_CELL_PAIR_TERMS == 3964
        and EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE == 3_995_712
        and len(NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT) == math.comb(6, 2) == 15
        and all(0 not in pair for pair in NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT)
        and not target_contract["required_source_fragments_missing"],
        target_contract,
    )
    group_source = inspect.getsource(signed_map_group_controls)
    combined_contract = {
        "required_source_fragments_missing": tuple(
            fragment
            for fragment in (
                "phase_u != phase * koszul",
                "corrected_phase = phase_u * koszul",
                "ungraded_group_failures == 0",
                "restricted_K_group_failures == 0",
                '"extra_bare_D_rho_character_in_Y_f": False',
            )
            if fragment not in group_source
        )
    }
    check(
        "target declares the combined B-D-C-Y relation and restricted K group gate",
        not combined_contract["required_source_fragments_missing"],
        combined_contract,
    )
    resource_contract = {
        "hard_wall_alarm_seconds": WALL_LIMIT_SECONDS,
        "RSS_checkpoint_abort_ceiling_bytes": RSS_CHECKPOINT_ABORT_CEILING_BYTES,
        "RSS_hard_limit_installed": False,
        "zero_swap_checkpoint_monitored": True,
        "partial_rows_durable_across_OS_kill_or_process_OOM": False,
        "planning_forecast_peak_RSS_bytes": 1_800_000_000,
        "planning_forecast_wall_seconds": 1000,
        "forecast_is_not_a_guarantee": True,
    }
    check(
        "resource contract is honest about hard wall versus monitored RSS and non-durability",
        resource_contract["hard_wall_alarm_seconds"] == 1200.0
        and resource_contract["RSS_checkpoint_abort_ceiling_bytes"] == 3_000_000_000
        and resource_contract["RSS_hard_limit_installed"] is False
        and resource_contract["zero_swap_checkpoint_monitored"]
        and resource_contract["partial_rows_durable_across_OS_kill_or_process_OOM"]
        is False,
        resource_contract,
    )
    partial = partial_retention_fixture()
    check(
        "partial rows survive caught exceptions only",
        partial["retained_count"] == 3
        and partial["durable_across_OS_kill_or_process_OOM"] is False,
        partial,
    )
    boundary = boundary_contract()
    check(
        "dry contract imports no Cycle514 law and makes no adjacent-star or TOE claim",
        not any(boundary.values()),
        boundary,
    )
    execution = {
        "frame_certificate_executed": False,
        "L5_physical_term_rows": 0,
        "L6_physical_term_rows": 0,
        "Gstar_columns_tested": 0,
        "science_rows_executed": 0,
        "adjacent_star_rows": 0,
        "response_rows": 0,
    }
    check(
        "dry mode executes no physical frame certificate",
        not any(execution.values()),
        execution,
    )
    passed = all(row["passed"] for row in tests)
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle516-koszul-frame-contract-ready" if passed else "dry-contract-failed",
        "pass": passed,
        "tests_passed": sum(row["passed"] for row in tests),
        "tests_total": len(tests),
        "evidence": evidence,
        "geometry_contract": geometry,
        "pair_cocycle_contract": pair_rows,
        "physical_cross_factor_target_contract": target_contract,
        "combined_B_D_C_Y_target_contract": combined_contract,
        "resource_contract": resource_contract,
        "partial_retention_fixture": partial,
        "boundary": boundary,
        "execution": execution,
        "tests": tests,
    }, 0 if passed else 1


def run_frame_certificate() -> tuple[dict, int]:
    started = time.monotonic()
    evidence = evidence_controls()
    if evidence["missing_files"] or evidence["strict_hash_failures"]:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": "frame-certificate",
            "status": "evidence-integrity-failure",
            "pass": False,
            "evidence": evidence,
            "science_rows_executed": 0,
        }, 1
    limits = install_wall_alarm()
    partial_rows = []
    frame_rows = []
    checkpoints = []
    stage = "initial-checkpoint"
    try:
        checkpoints.append(resource_checkpoint(started, stage, 300_000_000))
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            stage = f"L{length}-affine-local-terms"
            frame_rows.append(
                affine_local_term_controls(length, started, partial_rows)
            )
            checkpoints.append(resource_checkpoint(started, f"L{length}-complete"))
            gc.collect()

        stage = "reconcile-L5-L6-physical-pair-censuses"
        train_masks = set(
            frame_rows[0]["physical_source_pair_masks_all_allowed_occupations"]
        )
        held_masks = set(
            frame_rows[1]["physical_source_pair_masks_all_allowed_occupations"]
        )
        train_target_masks = set(
            frame_rows[0]["physical_target_pair_masks_all_allowed_occupations"]
        )
        held_target_masks = set(
            frame_rows[1]["physical_target_pair_masks_all_allowed_occupations"]
        )
        if (
            train_masks != held_masks
            or train_masks != train_target_masks
            or held_masks != held_target_masks
            or train_masks != set(EXPECTED_PHYSICAL_PAIR_MASKS)
            or frame_rows[0]["physical_pair_mask_histogram_sha256"]
            != frame_rows[1]["physical_pair_mask_histogram_sha256"]
        ):
            raise CertificateFailure(
                f"held L6 physical pair masks differ from L5: "
                f"{sorted(train_masks)} != "
                f"{sorted(held_masks)}"
            )
        checkpoints.append(
            resource_checkpoint(started, "physical-pair-censuses-reconciled")
        )

        stage = "frame-order-character-transport"
        order_rows = order_frame_transport_controls(D_CHARACTER_BASIS_MASKS)
        order_rows["L5_ordered_distinct_cell_physical_pair_tests"] = frame_rows[0][
            "ordered_distinct_cell_physical_pair_tests"
        ]
        order_rows["L6_ordered_distinct_cell_physical_pair_tests"] = frame_rows[1][
            "ordered_distinct_cell_physical_pair_tests"
        ]
        stage = "logical-frame-group-laws"
        group_rows = signed_map_group_controls()
        stage = "Gstar-covariance"
        gstar_rows = gstar_covariance_controls(group_rows)
        stage = "supplied-physical-closure"
        physical_closure = supplied_physical_closure(
            frame_rows, order_rows, group_rows, gstar_rows
        )
        lawful_rows = lawful_domain_controls(started)
        deletion_rows = deletion_and_held_controls(
            frame_rows, group_rows, gstar_rows, lawful_rows
        )
        pair_rows = pair_cocycle_controls()
        geometry = frame_geometry_contract()
        checkpoints.append(resource_checkpoint(started, "frame-certificate-complete"))
    except (ResourceWall, CertificateFailure, MemoryError, ValueError) as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": "frame-certificate",
            "status": (
                "cycle516-resource-wall"
                if isinstance(error, (ResourceWall, MemoryError))
                else "cycle516-certificate-failure"
            ),
            "pass": False,
            "failed_stage": stage,
            "error_type": type(error).__name__,
            "error": str(error),
            "partial_progress_rows": partial_rows,
            "completed_frame_rows": frame_rows,
            "partial_rows_preserved_for_caught_exception": True,
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
        "both_L5_L6_affine_term_certificates": (
            len(frame_rows) == 2
            and {row["L"] for row in frame_rows} == {5, 6}
            and all(row["pass"] for row in frame_rows)
        ),
        "held_local_term_counts_match": deletion_rows["held_L6_matches_L5"],
        "both_L5_L6_exhaustive_physical_pair_certificates": (
            len(frame_rows) == 2
            and all(row["physical_distinct_cell_pair_pass"] for row in frame_rows)
            and all(
                row["ordered_distinct_cell_physical_pair_tests"]
                == EXPECTED_PHYSICAL_PAIR_TESTS_PER_SIZE
                for row in frame_rows
            )
        ),
        "distinct_cell_pair_cocycle": pair_rows["pass"],
        "Cycle515_exact_mask_receipt_bound_and_physical_pair_masks_reconciled": (
            evidence["Cycle515_distinct_masks"] == (7, 7)
            and len(set(evidence["Cycle515_mask_hashes"])) == 1
            and train_masks == held_masks
            and train_masks == train_target_masks == held_target_masks
            and train_masks == set(EXPECTED_PHYSICAL_PAIR_MASKS)
            and frame_rows[0]["physical_pair_mask_histogram_sha256"]
            == frame_rows[1]["physical_pair_mask_histogram_sha256"]
        ),
        "all_24_times_5040_role_transports": order_rows["pass"],
        "all_15_commuting_occupied_arm_pair_Koszul_mismatches_at_L5_L6": (
            all(
                row["bare_physical_koszul_mismatch_witness"] is not None
                and tuple(
                    row["commuting_occupied_nontrivial_koszul_arm_pairs"]
                )
                == NONTRIVIAL_KOSZUL_ARM_PAIR_SUPPORT
                for row in frame_rows
            )
        ),
        "rank904_all24_576_group_laws": group_rows["pass"],
        "corrected_K_Gstar_covariance_and_ungraded_failure": gstar_rows["pass"],
        "physical_closure_with_supplied_bounded_patch_rules": physical_closure[
            "Gphysical_frame_covariance_on_code_proven_algebraically"
        ],
        "deletion_controls": deletion_rows["deletion_pass"],
        "checkpoint_resource_contract": (
            time.monotonic() - started < WALL_LIMIT_SECONDS
            and rss_bytes() < RSS_CHECKPOINT_ABORT_CEILING_BYTES
            and swap_count() == 0
        ),
    }
    tests = {name: bool(value) for name, value in tests.items()}
    passed = all(tests.values())
    group_output = {
        key: value
        for key, value in group_rows.items()
        if key not in {"graded_maps", "ungraded_maps", "corrected_maps"}
    }
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "frame-certificate",
        "status": (
            "cycle516-koszul-corrected-all-order-frame-certified"
            if passed
            else "cycle516-frame-predicate-failure"
        ),
        "pass": passed,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "tests": tests,
        "evidence": evidence,
        "resource_limits": limits,
        "resource_checkpoints": checkpoints,
        "partial_progress_rows": partial_rows,
        "partial_rows_preserved_for_caught_exception": True,
        "partial_rows_durable_across_OS_kill_or_process_OOM": False,
        "frame_rows": frame_rows,
        "geometry": geometry,
        "pair_cocycle": pair_rows,
        "order_transport": order_rows,
        "group_laws": group_output,
        "Gstar_covariance": gstar_rows,
        "physical_closure": physical_closure,
        "deletion_and_held": deletion_rows,
        "boundary": boundary_contract(),
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
        "authority_effect": "none",
        "audit_effect": "unset",
        "constitutional_effect": "none",
        "next_open_target": (
            "two adjacent maximal centers with overlapping corrected frame roles"
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
            else run_frame_certificate()
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
            "frame_certificate_complete": False,
            "adjacent_star_claim": False,
            "recurrent_volume_claim": False,
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
