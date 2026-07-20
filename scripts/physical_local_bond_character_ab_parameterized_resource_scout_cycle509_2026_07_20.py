#!/usr/bin/env python3
"""Cycle 509 parameterized A/B resource scout.

Dry mode validates the frozen contract while executing zero amplitude
evolution.  The separately authorized resource mode is deliberately limited
to one canonical middle-mass A/B resource invocation: interacting,
matched-free, repeated-free, inverse, and a sequential literal all-24
proper-cubic interacting full-word covariance sentinel.  It emits technical
resource evidence only.  It never emits a response, local field, translation
character, phase, classifier, per-frame residual, or state hash.

The carried geometry, support recursion, initial CAR wedge, emitter, and all
diagnostics are parameterized here.  Only hash-frozen, geometry-neutral Cycle
506 numerical kernels are reused.  Authority none; audit unset; no selector,
held evaluator, Route-C evaluator, science mode, or refit path exists.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import asdict, dataclass
import gc
from hashlib import sha256
import inspect
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
from typing import Mapping

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_directional_q1_recoil_source_current_train_cycle506_2026_07_20 as c506kernels
import physical_local_bond_character_bulk_tournament_preflight_cycle509_2026_07_20 as contract


AUTHORITY = "none"
AUDIT = "unset"
CLI_MODES = ("dry-contract", "resource-scout")

CONTRACT_RUNNER = ROOT / "scripts/physical_local_bond_character_bulk_tournament_preflight_cycle509_2026_07_20.py"
CONTRACT_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_BOND_CHARACTER_BULK_TOURNAMENT_PREFLIGHT_CYCLE509_NOTE_2026-07-20.md"
)
C506_KERNEL_RUNNER = ROOT / "scripts/physical_directional_q1_recoil_source_current_train_cycle506_2026_07_20.py"
OLD_CYCLE509_SCOUT = ROOT / "scripts/physical_local_bond_character_ab_resource_scout_cycle509_2026_07_20.py"

CONTRACT_RUNNER_SHA256 = "44a0430dafd31db471e6ada2435aa4a819637d09ac0af15ac387126e61ccd458"
CONTRACT_NOTE_SHA256 = "733aa72a2b2ef43f5b3a049903a85fa81b18c1413bcbe4d66f2a17345dce1d50"
TRAIN_MANIFEST_SHA256 = "d235ce413eaba7ac62c9100d45ef93824c246a4646f4cd9316c5a0191f1c73d8"
HELD_MANIFEST_SHA256 = "7dcaf19fb91b49bbe6528f124e4f428d7d54774390ff608e6afef5841657facf"
C506_KERNEL_RUNNER_SHA256 = "91c3f96a164d08a4707c00e6f9903f799c5c80c37a2644ea047934cb628b550e"
OLD_CYCLE509_SCOUT_SHA256 = "fdb48e5bd2c7ec63f3e1c51a5296214675c6d68e0650fa5e722f961332f670bf"

DECLARED_OLD_SCOUT_HISTORY = {
    "revision1_runner_sha256": "be886bd745c7110a600f5abfdfd8aba2ad71d8cd889263c3ce7829739e4c8625",
    "revision1_note_sha256": "0868301115cf30b1397ae1f40310a7e69efa4b34aa85783dc4696b0bb4b611c3",
    "failed_scout_transcript_sha256": "30995f09cac05b09abf5aec59a7018cac18bd45ae1ec8a14ab702a5b36a55c34",
    "quarantined_resource_transcript_sha256": "e019f76b5a71d5b2a216f5d70db75eabfeec1bd998a2a03466fe22f8f4bf7102",
    "old_scout_runner_sha256": OLD_CYCLE509_SCOUT_SHA256,
    "retained_scope": (
        "compute/runtime/numerical/continuity only; old Route-A surface invalid; "
        "old Route-B diagnostic zero-weight"
    ),
}

EXPECTED_PREDECESSOR_HASHES = {
    name: expected for name, (_path, expected) in contract.SOURCE_HASHES.items()
}

SCOUT_BETA = -4 * np.pi / 9
SCOUT_BETA_NAME = "-4pi/9"
SCOUT_DELETION = "none"
FIRST_CAUSAL_OVERLAP_UPDATE = 2
DEPTH = 5
WALL_CEILING_SECONDS = 600
RSS_CEILING_BYTES = 3_000_000_000
SWAP_CEILING = 0
NUMERIC_GATE = 1e-8
CONTINUITY_GATE = 1e-10
BOUNDARY_GATE = 1e-12
BAND_FLOOR = 0.05
AXIAL_SEAM_CEILING = 0.02
CONTACT_FLOOR = 0.01
BLOCK_PRUNE_FROBENIUS = 1e-13

SCOUT_AUTHORIZATION_ENV = "CYCLE509_SCOUT_AUTHORIZATION"
SCOUT_AUTHORIZATION_TOKEN = "root-cycle509-revision2-scout-after-dry-review-2026-07-20"
TRAIN_AUTHORIZATION_ENV = "CYCLE509_TRAIN_AUTHORIZATION"

EXPECTED_OPERATION_COUNTS = {
    "resource_invocations": 1,
    "science_train_rows": 0,
    "held_rows": 0,
    "routeC_allocations": 0,
    "refit_performed": False,
    "canonical_interacting_forward_trajectories": 1,
    "canonical_matched_free_forward_trajectories": 1,
    "canonical_repeated_free_forward_trajectories": 1,
    "carried_interacting_forward_trajectories": 24,
    "forward_trajectories": 27,
    "inverse_trajectories": 1,
    "trajectory_calls": 28,
    "forward_update_calls": 135,
    "inverse_update_calls": 5,
    "post_car_technical_captures": 135,
    "post_word_technical_captures": 135,
}

# Filled by the first dry construction and then frozen below.  These are
# contract digests, never hashes of amplitude states.
EXPECTED_GEOMETRY_DIGEST = "13d6826584aeb200f50575d4eded8167fd08c8aa2e326609b9fe7e3807194b68"
EXPECTED_SUPPORT_DIGEST = "edde6241e7ebb9779bca7d014aaf77f53aba61ef1f2f2efc5770b8f2796d41e9"
EXPECTED_BASIS_DIGESTS = (
    "ce8c2fd9a4c35edf8ce5a35cda10a4d44fa8e356d2c6433560faccad65e1735d",
    "22e3ba0a2394b949f7b91362688aa31685ebe39bc708c6dc800f9da3e93877e2",
    "e20ae767fc70be5452c1514aaa3552c11815046b68c67a844505401b18fdd993",
    "ac2a7ee6e8aea997dee669c1220df93ada3b00329ee4d1324c431fb012d7ce91",
    "91442b93f9057228370abd641b6729bee6fc3ae3bda2b6376d24ddad0f167eb6",
    "f3f772bff37572487ad3fc74eb47c3230c76971dfa6a96619776e7ccb9cc4c74",
)
EXPECTED_BASIS_SHAPES = (6, 18, 107, 316, 688, 1276)
EXPECTED_MEDIATOR_KEY_COUNTS = (1, 3, 7, 11, 15, 19)
EXPECTED_STRUCTURAL_MASK_DIGEST = "6a39a03e19062bcf8aa7b59506f9ac508fa7ea959edec92e639c74b685053b57"
EXPECTED_STRUCTURAL_MASK_COUNTS = ((306, 0, 0), (14733, 0, 0), (187500, 3600, 212))

Mode = tuple[tuple[int, int, int], int]
Mediator = tuple[tuple[int, int, int], int] | None
Blocks = dict[Mediator, np.ndarray]


@dataclass(frozen=True)
class CarriedGeometry:
    name: str
    side: int
    source_cell: tuple[int, int, int]
    probe_center: tuple[int, int, int]
    outgoing_direction: int
    causal_axis: int
    depth: int
    packet_cells: tuple[tuple[int, int, int], ...]
    packet_directions: tuple[int, int]
    frame_flat: tuple[int, ...]


@dataclass(frozen=True)
class SupportSlice:
    update: int
    basis: tuple[Mode, ...]
    mediator_keys: tuple[Mediator, ...]
    collision_cells: tuple[tuple[int, int, int], ...]


@dataclass(frozen=True)
class CarStepOperators:
    coin_basis: tuple[Mode, ...]
    coin: sparse.csr_matrix
    stream: sparse.csr_matrix
    reference_residual: float
    isometry_residual: float


@dataclass
class ExecutionLedger:
    canonical_interacting_forward_trajectories: int = 0
    canonical_matched_free_forward_trajectories: int = 0
    canonical_repeated_free_forward_trajectories: int = 0
    carried_interacting_forward_trajectories: int = 0
    forward_trajectories: int = 0
    inverse_trajectories: int = 0
    forward_update_calls: int = 0
    inverse_update_calls: int = 0
    post_car_technical_captures: int = 0
    post_word_technical_captures: int = 0


@dataclass
class TechnicalControls:
    maximum_norm_residual: float = 0.0
    maximum_car_number_residual: float = 0.0
    maximum_mediator_charge_residual: float = 0.0
    maximum_lawfulness_residual: float = 0.0
    maximum_boundary_shell_weight: float = 0.0
    maximum_post_stream_continuity_residual: float = 0.0
    minimum_dynamic_band_fraction: float = float("inf")
    maximum_dynamic_axial_seam_weight: float = 0.0
    maximum_dynamic_contact_weight: float = 0.0
    maximum_car_kernel_residual: float = 0.0

    def absorb(self, other: "TechnicalControls") -> None:
        self.maximum_norm_residual = max(self.maximum_norm_residual, other.maximum_norm_residual)
        self.maximum_car_number_residual = max(
            self.maximum_car_number_residual, other.maximum_car_number_residual
        )
        self.maximum_mediator_charge_residual = max(
            self.maximum_mediator_charge_residual, other.maximum_mediator_charge_residual
        )
        self.maximum_lawfulness_residual = max(
            self.maximum_lawfulness_residual, other.maximum_lawfulness_residual
        )
        self.maximum_boundary_shell_weight = max(
            self.maximum_boundary_shell_weight, other.maximum_boundary_shell_weight
        )
        self.maximum_post_stream_continuity_residual = max(
            self.maximum_post_stream_continuity_residual,
            other.maximum_post_stream_continuity_residual,
        )
        self.minimum_dynamic_band_fraction = min(
            self.minimum_dynamic_band_fraction, other.minimum_dynamic_band_fraction
        )
        self.maximum_dynamic_axial_seam_weight = max(
            self.maximum_dynamic_axial_seam_weight, other.maximum_dynamic_axial_seam_weight
        )
        self.maximum_dynamic_contact_weight = max(
            self.maximum_dynamic_contact_weight, other.maximum_dynamic_contact_weight
        )
        self.maximum_car_kernel_residual = max(
            self.maximum_car_kernel_residual, other.maximum_car_kernel_residual
        )


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def object_digest(value: object) -> str:
    return sha256(json_bytes(value)).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def swap_count() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_nswap)


def alarm_handler(_signum: int, _frame: object) -> None:
    raise TimeoutError("Cycle509 parameterized A/B resource scout exceeded 600 seconds")


def authorization_allowed(mode: str, environ: Mapping[str, str]) -> bool:
    scout_present = SCOUT_AUTHORIZATION_ENV in environ
    train_present = TRAIN_AUTHORIZATION_ENV in environ
    if mode == "dry-contract":
        return not scout_present and not train_present
    if mode == "resource-scout":
        return (
            scout_present
            and environ[SCOUT_AUTHORIZATION_ENV] == SCOUT_AUTHORIZATION_TOKEN
            and not train_present
        )
    return False


def enforce_authorization(mode: str, environ: Mapping[str, str]) -> None:
    if not authorization_allowed(mode, environ):
        present = tuple(
            name for name in (SCOUT_AUTHORIZATION_ENV, TRAIN_AUTHORIZATION_ENV)
            if name in environ
        )
        print("REJECT authorization contract", {"mode": mode, "present": present})
        raise SystemExit(2)


def callable_signature(function: object) -> tuple[tuple[str, str, bool], ...] | None:
    if not callable(function):
        return None
    return tuple(
        (parameter.name, parameter.kind.name, parameter.default is not inspect.Signature.empty)
        for parameter in inspect.signature(function).parameters.values()
    )


def inherited_kernel_contract() -> dict[str, bool]:
    positional = "POSITIONAL_OR_KEYWORD"
    keyword_only = "KEYWORD_ONLY"
    expected = {
        "one_body_map": (
            ("previous", positional, False), ("following", positional, False),
            ("beta", positional, False),
        ),
        "apply_car_map": (
            ("blocks", positional, False), ("operation", positional, False),
            ("inverse", keyword_only, True),
        ),
        "apply_contact": (
            ("blocks", positional, False), ("basis", positional, False),
            ("coupling", positional, False),
        ),
        "collision": (
            ("blocks", positional, False), ("basis", positional, False),
            ("angle", positional, False),
        ),
        "mediator_stream": (
            ("blocks", positional, False), ("inverse", keyword_only, True),
        ),
    }
    functions = {name: getattr(c506kernels, name, None) for name in expected}
    forbidden_geometry_reads = (
        "pre.TRAIN", "OUTGOING_DIRECTION", "fixed_probe", "plane_current",
        "translation_character", "_BAND_KERNELS", "_BAND_PROJECTORS",
    )
    checks = {
        f"{name}_signature": callable_signature(functions[name]) == signature
        for name, signature in expected.items()
    }
    checks.update({
        f"{name}_geometry_neutral_source": all(
            token not in inspect.getsource(functions[name]) for token in forbidden_geometry_reads
        )
        for name in expected
    })
    localized = {
        "direct_one_body_map": direct_one_body_map,
        "apply_car_map": apply_car_map,
        "apply_contact": apply_contact,
        "collision": collision,
        "mediator_stream": mediator_stream,
    }
    checks.update({
        f"localized_{name}_has_no_c506_computational_call": (
            "c506kernels." not in inspect.getsource(function)
        )
        for name, function in localized.items()
    })
    return checks


def direction_image(frame: np.ndarray, direction: int) -> int:
    moved = frame @ contract.c210.DIRECTIONS[direction]
    matches = np.flatnonzero(np.all(contract.c210.DIRECTIONS == moved, axis=1))
    if len(matches) != 1:
        raise RuntimeError("proper-cubic frame has no unique direction image")
    return int(matches[0])


def canonical_geometry() -> CarriedGeometry:
    return CarriedGeometry(
        name="train-canonical-3D-L25",
        side=25,
        source_cell=(12, 12, 12),
        probe_center=(8, 12, 12),
        outgoing_direction=1,
        causal_axis=0,
        depth=DEPTH,
        packet_cells=((7, 12, 12), (8, 12, 12), (9, 12, 12)),
        packet_directions=(0, 1),
        frame_flat=tuple(int(value) for value in np.eye(3, dtype=int).ravel()),
    )


def carry_geometry(base: CarriedGeometry, frame: np.ndarray, index: int) -> CarriedGeometry:
    moved_outgoing = direction_image(frame, base.outgoing_direction)
    moved_packet_directions = tuple(
        direction_image(frame, direction) for direction in base.packet_directions
    )
    return CarriedGeometry(
        name=f"carried-proper-cubic-{index:02d}",
        side=base.side,
        source_cell=contract.frame_cell(base.source_cell, frame, base.side),
        probe_center=contract.frame_cell(base.probe_center, frame, base.side),
        outgoing_direction=moved_outgoing,
        causal_axis=moved_outgoing // 2,
        depth=base.depth,
        packet_cells=tuple(
            contract.frame_cell(cell, frame, base.side) for cell in base.packet_cells
        ),
        packet_directions=(int(moved_packet_directions[0]), int(moved_packet_directions[1])),
        frame_flat=tuple(int(value) for value in frame.ravel()),
    )


def proper_cubic_geometries() -> tuple[tuple[np.ndarray, CarriedGeometry], ...]:
    base = canonical_geometry()
    frames = tuple(np.asarray(frame, dtype=int) for frame in contract.c210.proper_cubic_frames())
    return tuple((frame, carry_geometry(base, frame, index)) for index, frame in enumerate(frames))


def initial_modes(geometry: CarriedGeometry) -> tuple[Mode, ...]:
    return tuple(sorted(
        (cell, direction)
        for cell in geometry.packet_cells
        for direction in geometry.packet_directions
    ))


def support_trace(geometry: CarriedGeometry) -> tuple[tuple[SupportSlice, ...], int | None]:
    car_modes = set(initial_modes(geometry))
    mediator_post: set[Mediator] = {None}
    rows: list[SupportSlice] = [
        SupportSlice(0, tuple(sorted(car_modes)), (None,), ())
    ]
    first_overlap: int | None = None
    for update in range(1, geometry.depth + 1):
        cells_before = {cell for cell, _direction in car_modes}
        car_streamed = {
            (
                tuple(int(value) for value in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                )),
                direction,
            )
            for cell in cells_before for direction in range(6)
        }
        mediator_pre = set(mediator_post)
        mediator_pre.add((geometry.source_cell, geometry.outgoing_direction))
        collision_mediator: set[Mediator] = {None}
        for key in mediator_pre:
            if key is not None:
                cell, direction = key
                collision_mediator.add((cell, direction))
                collision_mediator.add((cell, contract.REVERSE[direction]))
        car_cells = {cell for cell, _direction in car_streamed}
        collision_cells = {
            cell for key in collision_mediator if key is not None
            for cell, _direction in (key,) if cell in car_cells
        }
        if collision_cells and first_overlap is None:
            first_overlap = update
        for cell in collision_cells:
            car_streamed.update((cell, direction) for direction in range(6))
        mediator_post = {None}
        for key in collision_mediator:
            if key is not None:
                cell, direction = key
                mediator_post.add((
                    tuple(int(value) for value in (
                        np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                    )),
                    direction,
                ))
        car_modes = car_streamed
        rows.append(SupportSlice(
            update=update,
            basis=tuple(sorted(car_modes)),
            mediator_keys=tuple(sorted(mediator_post, key=repr)),
            collision_cells=tuple(sorted(collision_cells)),
        ))
    return tuple(rows), first_overlap


def support_summary(geometry: CarriedGeometry) -> dict:
    rows, first_overlap = support_trace(geometry)
    basis_digests = tuple(object_digest(row.basis) for row in rows)
    summary = {
        "first_overlap_update": first_overlap,
        "basis_shapes": tuple(len(row.basis) for row in rows),
        "mediator_key_counts": tuple(len(row.mediator_keys) for row in rows),
        "collision_cell_counts": tuple(len(row.collision_cells) for row in rows),
        "basis_digests": basis_digests,
    }
    summary["support_digest"] = object_digest(summary)
    return summary


def geometry_digest() -> str:
    base = canonical_geometry()
    carried = proper_cubic_geometries()
    payload = {
        "canonical": asdict(base),
        "carried": tuple(asdict(geometry) for _frame, geometry in carried),
    }
    return object_digest(payload)


def initial_blocks(geometry: CarriedGeometry, basis: tuple[Mode, ...]) -> Blocks:
    index = {mode: position for position, mode in enumerate(basis)}
    weights = np.asarray((1.0, 2.0, 1.0), dtype=float) / np.sqrt(6.0)
    left = np.zeros(len(basis), dtype=complex)
    right = np.zeros(len(basis), dtype=complex)
    for cell, weight in zip(geometry.packet_cells, weights):
        left[index[(cell, geometry.packet_directions[0])]] = weight
        right[index[(cell, geometry.packet_directions[1])]] = weight
    amplitude = np.outer(left, right) - np.outer(right, left)
    return {None: amplitude}


def copy_blocks(blocks: Blocks) -> Blocks:
    return {key: block.copy() for key, block in blocks.items()}


def prune_blocks(blocks: Blocks) -> Blocks:
    return {
        key: block for key, block in blocks.items()
        if np.linalg.norm(block) > BLOCK_PRUNE_FROBENIUS
    }


def emitter(blocks: Blocks, angle: float, geometry: CarriedGeometry) -> Blocks:
    source_key: Mediator = (geometry.source_cell, geometry.outgoing_direction)
    park = blocks.get(None)
    active = blocks.get(source_key)
    template = park if park is not None else active
    if template is None:
        raise RuntimeError("emitter lacks both parked and carried-source blocks")
    zero = np.zeros_like(template)
    park_value = zero if park is None else park
    active_value = zero if active is None else active
    cosine, sine = np.cos(angle), np.sin(angle)
    output = {
        key: block.copy() for key, block in blocks.items()
        if key not in (None, source_key)
    }
    output[None] = cosine * park_value + 1j * sine * active_value
    output[source_key] = cosine * active_value + 1j * sine * park_value
    return prune_blocks(output)


def coin_basis(previous: tuple[Mode, ...]) -> tuple[Mode, ...]:
    cells = {cell for cell, _direction in previous}
    return tuple(sorted((cell, direction) for cell in cells for direction in range(6)))


def direct_one_body_map(
    previous: tuple[Mode, ...], following: tuple[Mode, ...], beta: float
) -> sparse.csr_matrix:
    """Independent direct coin-plus-stream construction for the cold comparator."""
    target_index = {mode: position for position, mode in enumerate(following)}
    coin = contract.c219.common_species(beta).coin
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for column, (cell, incoming) in enumerate(previous):
        for outgoing in range(6):
            target = (
                tuple(int(value) for value in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[outgoing]
                )),
                outgoing,
            )
            if target not in target_index:
                raise RuntimeError("direct comparator support omitted a stream target")
            rows.append(target_index[target])
            columns.append(column)
            data.append(coin[outgoing, incoming])
    result = sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(following), len(previous)), dtype=complex,
    ).tocsr()
    result.sum_duplicates()
    return result


def build_step_operators(
    previous: tuple[Mode, ...], following: tuple[Mode, ...], beta: float
) -> CarStepOperators:
    middle = coin_basis(previous)
    middle_index = {mode: position for position, mode in enumerate(middle)}
    following_index = {mode: position for position, mode in enumerate(following)}
    coin = contract.c219.common_species(beta).coin

    coin_rows: list[int] = []
    coin_columns: list[int] = []
    coin_data: list[complex] = []
    for column, (cell, incoming) in enumerate(previous):
        for outgoing in range(6):
            coin_rows.append(middle_index[(cell, outgoing)])
            coin_columns.append(column)
            coin_data.append(coin[outgoing, incoming])
    coin_operation = sparse.coo_matrix(
        (coin_data, (coin_rows, coin_columns)),
        shape=(len(middle), len(previous)), dtype=complex,
    ).tocsr()
    coin_operation.sum_duplicates()

    stream_rows: list[int] = []
    stream_columns: list[int] = []
    for column, (cell, direction) in enumerate(middle):
        target = (
            tuple(int(value) for value in (
                np.asarray(cell) + contract.c210.DIRECTIONS[direction]
            )),
            direction,
        )
        if target not in following_index:
            raise RuntimeError("parameterized support omitted a CAR stream target")
        stream_rows.append(following_index[target])
        stream_columns.append(column)
    stream_operation = sparse.coo_matrix(
        (np.ones(len(stream_rows), dtype=complex), (stream_rows, stream_columns)),
        shape=(len(following), len(middle)), dtype=complex,
    ).tocsr()

    reference = direct_one_body_map(previous, following, beta)
    combined = stream_operation @ coin_operation
    reference_residual = float(sparse.linalg.norm(combined - reference))
    coin_isometry = float(sparse.linalg.norm(
        coin_operation.conj().T @ coin_operation - sparse.eye(len(previous))
    ))
    stream_isometry = float(sparse.linalg.norm(
        stream_operation.conj().T @ stream_operation - sparse.eye(len(middle))
    ))
    return CarStepOperators(
        coin_basis=middle,
        coin=coin_operation,
        stream=stream_operation,
        reference_residual=reference_residual,
        isometry_residual=max(coin_isometry, stream_isometry),
    )


def build_operations(rows: tuple[SupportSlice, ...], beta: float) -> tuple[CarStepOperators, ...]:
    return tuple(
        build_step_operators(rows[index].basis, rows[index + 1].basis, beta)
        for index in range(len(rows) - 1)
    )


def occupation_vector(blocks: Blocks, basis: tuple[Mode, ...]) -> np.ndarray:
    occupation = np.zeros(len(basis), dtype=float)
    for block in blocks.values():
        occupation += np.sum(abs(block) ** 2, axis=1)
    return occupation


def occupation_cube(blocks: Blocks, basis: tuple[Mode, ...], side: int) -> np.ndarray:
    output = np.zeros((side, side, side, 6), dtype=float)
    values = occupation_vector(blocks, basis)
    for value, (cell, direction) in zip(values, basis):
        output[cell + (direction,)] += float(value)
    return output


def apply_car_map(
    blocks: Blocks, operation: sparse.csr_matrix, *, inverse: bool = False
) -> Blocks:
    """Apply one explicit one-body map to both CAR slots."""
    left = operation.conj().T.tocsr() if inverse else operation
    output: Blocks = {}
    for key, block in blocks.items():
        temporary = left @ block
        output[key] = (left @ temporary.T).T
    return prune_blocks(output)


def apply_contact(blocks: Blocks, basis: tuple[Mode, ...], coupling: float) -> None:
    """Apply the frozen same-cell Cycle-230 phase without predecessor globals."""
    by_cell: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for index, (cell, _direction) in enumerate(basis):
        by_cell[cell].append(index)
    phase = np.exp(1j * coupling)
    for block in blocks.values():
        for indices in by_cell.values():
            if len(indices) >= 2:
                block[np.ix_(indices, indices)] *= phase


def collision(blocks: Blocks, basis: tuple[Mode, ...], angle: float) -> Blocks:
    """Apply the explicit local reciprocal mediator/CAR collision."""
    if abs(angle) < 1e-18:
        return copy_blocks(blocks)
    index = {mode: position for position, mode in enumerate(basis)}
    output = copy_blocks(blocks)
    cosine, sine = np.cos(angle), np.sin(angle)
    size = len(basis)
    for mediator_key, block in blocks.items():
        if mediator_key is None:
            continue
        cell, direction = mediator_key
        old_mode = (cell, contract.REVERSE[direction])
        new_mode = (cell, direction)
        if old_mode not in index or new_mode not in index:
            continue
        old, new = index[old_mode], index[new_mode]
        partners = np.asarray(
            [value for value in range(size) if value not in (old, new)], dtype=int
        )
        coefficients = block[old, partners].copy()
        adjustment = (cosine - 1) * coefficients
        output[mediator_key][old, partners] += adjustment
        output[mediator_key][partners, old] -= adjustment
        target_key: Mediator = (cell, contract.REVERSE[direction])
        if target_key not in output:
            output[target_key] = np.zeros_like(block)
        scattered = 1j * sine * coefficients
        output[target_key][new, partners] += scattered
        output[target_key][partners, new] -= scattered
    return prune_blocks(output)


def mediator_stream(blocks: Blocks, *, inverse: bool = False) -> Blocks:
    """Carry the mediator key with the explicit proper-cubic direction table."""
    output: Blocks = {}
    sign = -1 if inverse else 1
    for key, block in blocks.items():
        if key is None:
            target = None
        else:
            cell, direction = key
            target = (
                tuple(int(value) for value in (
                    np.asarray(cell) + sign * contract.c210.DIRECTIONS[direction]
                )),
                direction,
            )
        if target in output:
            output[target] += block
        else:
            output[target] = block
    return prune_blocks(output)


def post_stream_continuity_residual(pre_stream: np.ndarray, post_stream: np.ndarray) -> float:
    stream_residual = float(np.max(abs(contract.stream_occupation(pre_stream) - post_stream)))
    bond = contract.plane_bond_field(post_stream)
    continuity = 0.0
    for axis in range(3):
        change = (
            contract.plane_density(post_stream, axis)
            - contract.plane_density(pre_stream, axis)
        )
        divergence = bond[axis] - np.roll(bond[axis], -1)
        continuity = max(continuity, float(np.max(abs(change - divergence))))
    return max(stream_residual, continuity)


def state_residual(left: Blocks, right: Blocks) -> float:
    total = 0.0
    for key in set(left) | set(right):
        if key in left and key in right:
            difference = left[key] - right[key]
        elif key in left:
            difference = left[key]
        else:
            difference = -right[key]
        total += float(np.vdot(difference, difference).real / 2)
    return float(np.sqrt(total))


def selected_band_kernel(side: int, beta: float) -> np.ndarray:
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    spectral = np.empty((side, side, side, 6, 6), dtype=complex)
    coin = contract.c219.common_species(beta).coin
    for ix, kx in enumerate(momenta):
        for iy, ky in enumerate(momenta):
            for iz, kz in enumerate(momenta):
                wave = np.asarray((kx, ky, kz))
                bloch = np.diag(np.exp(-1j * (contract.c210.DIRECTIONS @ wave))) @ coin
                _values, candidates = np.linalg.eig(bloch)
                overlaps = np.abs(candidates.conj().T @ contract.c210.UNIFORM)
                selected = int(np.flatnonzero(overlaps == np.max(overlaps))[0])
                vector = candidates[:, selected] / np.linalg.norm(candidates[:, selected])
                spectral[ix, iy, iz] = np.outer(vector, vector.conj())
    return np.fft.ifftn(spectral, axes=(0, 1, 2))


def selected_band_projector(
    kernel: np.ndarray, basis: tuple[Mode, ...], side: int
) -> np.ndarray:
    cells = np.asarray([cell for cell, _direction in basis], dtype=int)
    directions = np.asarray([direction for _cell, direction in basis], dtype=int)
    displacement = (cells[:, None, :] - cells[None, :, :]) % side
    projector = kernel[
        displacement[:, :, 0], displacement[:, :, 1], displacement[:, :, 2],
        directions[:, None], directions[None, :],
    ]
    if float(np.max(abs(projector - projector.conj().T))) > NUMERIC_GATE:
        raise RuntimeError("restricted selected-band projector is not Hermitian")
    return projector


def axial_seam_weight(
    gamma: np.ndarray, basis: tuple[Mode, ...], geometry: CarriedGeometry
) -> float:
    side = geometry.side
    axis = geometry.causal_axis
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    seam_indices = np.argsort(np.abs(momenta))[-2:]
    kernel = np.fft.ifft(np.isin(np.arange(side), seam_indices).astype(float))
    transverse_axes = tuple(value for value in range(3) if value != axis)
    groups: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for index, (cell, direction) in enumerate(basis):
        groups[(cell[transverse_axes[0]], cell[transverse_axes[1]], direction)].append(index)
    total = 0j
    for indices in groups.values():
        rows = np.asarray(indices, dtype=int)
        coordinates = np.asarray([basis[index][0][axis] for index in indices], dtype=int)
        projector = kernel[(coordinates[:, None] - coordinates[None, :]) % side]
        total += np.einsum("ij,ji->", projector, gamma[np.ix_(rows, rows)], optimize=True)
    return float(np.real(total))


def technical_diagnostics(
    blocks: Blocks,
    support: SupportSlice,
    geometry: CarriedGeometry,
    band_projector: np.ndarray | None,
) -> dict[str, float]:
    basis = support.basis
    size = len(basis)
    norm_squared = float(sum(np.vdot(block, block).real for block in blocks.values()) / 2)
    occupation = occupation_vector(blocks, basis)
    mediator_charge = 0.0
    antisymmetry = 0.0
    diagonal = 0.0
    contact = 0.0
    gamma = np.zeros((size, size), dtype=complex) if band_projector is not None else None
    by_cell: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for index, (cell, _direction) in enumerate(basis):
        by_cell[cell].append(index)
    for block in blocks.values():
        mediator_charge += float(np.vdot(block, block).real / 2)
        antisymmetry = max(antisymmetry, float(np.linalg.norm(block + block.T)))
        diagonal = max(diagonal, float(np.max(abs(np.diag(block)))))
        for indices in by_cell.values():
            local = block[np.ix_(indices, indices)]
            contact += float(np.vdot(local, local).real / 2)
        if gamma is not None:
            gamma += block @ block.conj().T
    shell = float(sum(
        occupation[index] for index, (cell, _direction) in enumerate(basis)
        if any(coordinate in (0, geometry.side - 1) for coordinate in cell)
    ))
    unexpected_keys = not set(blocks).issubset(set(support.mediator_keys))
    malformed_shapes = any(block.shape != (size, size) for block in blocks.values())
    result = {
        "norm_residual": abs(norm_squared - 1.0),
        "car_number_residual": abs(float(np.sum(occupation)) - 2.0),
        "mediator_charge_residual": abs(mediator_charge - 1.0),
        "lawfulness_residual": max(
            antisymmetry, diagonal, float(unexpected_keys), float(malformed_shapes)
        ),
        "boundary_shell_weight": shell,
        "contact_weight": contact,
    }
    if gamma is not None and band_projector is not None:
        band_number = float(np.real(np.einsum("ij,ji->", band_projector, gamma, optimize=True)))
        result["dynamic_band_fraction"] = band_number / float(np.sum(occupation))
        result["dynamic_axial_seam_weight"] = axial_seam_weight(
            gamma, basis, geometry
        )
    del gamma
    return result


def absorb_diagnostic(controls: TechnicalControls, diagnostic: dict[str, float]) -> None:
    controls.maximum_norm_residual = max(
        controls.maximum_norm_residual, diagnostic["norm_residual"]
    )
    controls.maximum_car_number_residual = max(
        controls.maximum_car_number_residual, diagnostic["car_number_residual"]
    )
    controls.maximum_mediator_charge_residual = max(
        controls.maximum_mediator_charge_residual,
        diagnostic["mediator_charge_residual"],
    )
    controls.maximum_lawfulness_residual = max(
        controls.maximum_lawfulness_residual, diagnostic["lawfulness_residual"]
    )
    controls.maximum_boundary_shell_weight = max(
        controls.maximum_boundary_shell_weight, diagnostic["boundary_shell_weight"]
    )
    controls.maximum_dynamic_contact_weight = max(
        controls.maximum_dynamic_contact_weight, diagnostic["contact_weight"]
    )
    if "dynamic_band_fraction" in diagnostic:
        controls.minimum_dynamic_band_fraction = min(
            controls.minimum_dynamic_band_fraction,
            diagnostic["dynamic_band_fraction"],
        )
        controls.maximum_dynamic_axial_seam_weight = max(
            controls.maximum_dynamic_axial_seam_weight,
            diagnostic["dynamic_axial_seam_weight"],
        )


def forward_step(
    blocks: Blocks,
    operation: CarStepOperators,
    support: SupportSlice,
    geometry: CarriedGeometry,
    emitter_angle: float,
    collision_angle: float,
    band_projector: np.ndarray | None,
) -> tuple[Blocks, TechnicalControls]:
    emitted = emitter(blocks, emitter_angle, geometry)
    pre_stream_blocks = apply_car_map(emitted, operation.coin)
    pre_stream_occupation = occupation_cube(
        pre_stream_blocks, operation.coin_basis, geometry.side
    )
    post_car_blocks = apply_car_map(pre_stream_blocks, operation.stream)
    # This independent array is the only Route-A resource capture.  It is made
    # before contact/collision and is never emitted or used as a response.
    post_car_occupation = occupation_cube(post_car_blocks, support.basis, geometry.side)
    continuity = post_stream_continuity_residual(
        pre_stream_occupation, post_car_occupation
    )
    output = copy_blocks(post_car_blocks)
    apply_contact(output, support.basis, contract.CONTACT_COUPLING)
    output = collision(output, support.basis, collision_angle)
    output = mediator_stream(output)
    # Route-B technical capture occurs only here, after the complete word.
    diagnostic = technical_diagnostics(output, support, geometry, band_projector)
    controls = TechnicalControls(
        maximum_post_stream_continuity_residual=continuity,
        maximum_car_kernel_residual=max(
            operation.reference_residual, operation.isometry_residual
        ),
    )
    absorb_diagnostic(controls, diagnostic)
    del emitted, pre_stream_blocks, pre_stream_occupation
    del post_car_blocks, post_car_occupation, diagnostic
    return output, controls


def inverse_step(
    blocks: Blocks,
    operation: CarStepOperators,
    current_support: SupportSlice,
    previous_support: SupportSlice,
    geometry: CarriedGeometry,
    emitter_angle: float,
    collision_angle: float,
) -> Blocks:
    output = mediator_stream(blocks, inverse=True)
    output = collision(output, current_support.basis, -collision_angle)
    apply_contact(output, current_support.basis, -contract.CONTACT_COUPLING)
    output = apply_car_map(output, operation.stream, inverse=True)
    output = apply_car_map(output, operation.coin, inverse=True)
    output = emitter(output, -emitter_angle, geometry)
    if any(block.shape != (len(previous_support.basis), len(previous_support.basis))
           for block in output.values()):
        raise RuntimeError("inverse CAR basis shape drift")
    return output


def run_forward_trajectory(
    initial: Blocks,
    rows: tuple[SupportSlice, ...],
    operations: tuple[CarStepOperators, ...],
    geometry: CarriedGeometry,
    emitter_angle: float,
    collision_angle: float,
    spectral_projectors: tuple[np.ndarray | None, ...],
    ledger: ExecutionLedger,
    trajectory_kind: str,
) -> tuple[Blocks, TechnicalControls]:
    ledger_field = {
        "canonical-interacting": "canonical_interacting_forward_trajectories",
        "canonical-matched-free": "canonical_matched_free_forward_trajectories",
        "canonical-repeated-free": "canonical_repeated_free_forward_trajectories",
        "carried-interacting": "carried_interacting_forward_trajectories",
    }.get(trajectory_kind)
    if ledger_field is None:
        raise ValueError("unfrozen trajectory kind")
    setattr(ledger, ledger_field, getattr(ledger, ledger_field) + 1)
    ledger.forward_trajectories += 1
    blocks = copy_blocks(initial)
    controls = TechnicalControls()
    for update, operation in enumerate(operations, start=1):
        previous = blocks
        blocks, step_controls = forward_step(
            previous, operation, rows[update], geometry,
            emitter_angle, collision_angle, spectral_projectors[update],
        )
        previous.clear()
        controls.absorb(step_controls)
        ledger.forward_update_calls += 1
        ledger.post_car_technical_captures += 1
        ledger.post_word_technical_captures += 1
    return blocks, controls


def run_inverse_trajectory(
    final: Blocks,
    rows: tuple[SupportSlice, ...],
    operations: tuple[CarStepOperators, ...],
    geometry: CarriedGeometry,
    emitter_angle: float,
    collision_angle: float,
    ledger: ExecutionLedger,
) -> Blocks:
    ledger.inverse_trajectories += 1
    blocks = copy_blocks(final)
    for update in reversed(range(1, len(rows))):
        previous = blocks
        blocks = inverse_step(
            previous, operations[update - 1], rows[update], rows[update - 1],
            geometry, emitter_angle, collision_angle,
        )
        previous.clear()
        ledger.inverse_update_calls += 1
    return blocks


def carry_mode(mode: Mode, frame: np.ndarray, side: int) -> Mode:
    cell, direction = mode
    return contract.frame_cell(cell, frame, side), direction_image(frame, direction)


def carry_mediator(key: Mediator, frame: np.ndarray, side: int) -> Mediator:
    if key is None:
        return None
    cell, direction = key
    return contract.frame_cell(cell, frame, side), direction_image(frame, direction)


def basis_permutation(
    source: tuple[Mode, ...], target: tuple[Mode, ...], frame: np.ndarray, side: int
) -> sparse.csr_matrix:
    target_index = {mode: index for index, mode in enumerate(target)}
    rows = []
    for mode in source:
        moved = carry_mode(mode, frame, side)
        if moved not in target_index:
            raise RuntimeError("carried support basis is not a full CAR orbit")
        rows.append(target_index[moved])
    return sparse.coo_matrix(
        (np.ones(len(source)), (rows, np.arange(len(source)))),
        shape=(len(target), len(source)), dtype=float,
    ).tocsr()


def carried_state_residual(
    observed: Blocks,
    canonical: Blocks,
    canonical_basis: tuple[Mode, ...],
    carried_basis: tuple[Mode, ...],
    frame: np.ndarray,
    side: int,
) -> float:
    permutation = basis_permutation(
        canonical_basis, carried_basis, frame, side
    )
    expected: Blocks = {}
    for key, block in canonical.items():
        moved_key = carry_mediator(key, frame, side)
        # The antisymmetric two-CAR coefficient matrix transforms as P A P^T.
        moved_block = permutation @ block @ permutation.T
        if moved_key in expected:
            expected[moved_key] += np.asarray(moved_block)
        else:
            expected[moved_key] = np.asarray(moved_block)
    residual = state_residual(observed, expected)
    expected.clear()
    return residual


def structural_mask_summary() -> dict:
    fixture = contract.boolean_joint_cone_fixture()
    rows = fixture["rows"]
    counts = tuple(
        (
            int(row["joint_support_states"]),
            int(row["sample_tainted_joint_states"]),
            int(row["sample_tainted_bonds"]),
        )
        for row in rows
    )
    payload = {
        "counts": counts,
        "first_tainted_update": next(
            row["update"] for row in rows if row["sample_tainted_joint_states"]
        ),
        "amplitude_pruning_certifies_mask": False,
    }
    return {**payload, "digest": object_digest(payload)}


RESOURCE_OUTPUT_KEYS = {
    "digests", "counts", "shapes", "residuals", "structural_mask_sizes",
    "resource_usage", "passes", "verdict",
}
FORBIDDEN_OUTPUT_KEY_TOKENS = (
    "response", "delta", "field", "character", "phase", "classifier",
    "anchor", "argmax", "argmin", "peak", "current", "bond", "occupation",
    "trace", "morphology", "per_frame", "state_hash",
)


def validate_resource_output(payload: dict) -> bool:
    if set(payload) != RESOURCE_OUTPUT_KEYS:
        return False

    def walk(value: object) -> bool:
        if isinstance(value, dict):
            for key, child in value.items():
                lowered = str(key).lower()
                if any(token in lowered for token in FORBIDDEN_OUTPUT_KEY_TOKENS):
                    return False
                if not walk(child):
                    return False
            return True
        if isinstance(value, (tuple, list)):
            return all(walk(child) for child in value)
        return isinstance(value, (str, int, float, bool)) and not isinstance(value, complex)

    return walk(payload)


def resource_output_exemplar() -> dict:
    return {
        "digests": {
            "contract_runner_sha256": CONTRACT_RUNNER_SHA256,
            "contract_note_sha256": CONTRACT_NOTE_SHA256,
            "train_manifest_sha256": TRAIN_MANIFEST_SHA256,
            "held_manifest_sha256": HELD_MANIFEST_SHA256,
            "geometry_sha256": EXPECTED_GEOMETRY_DIGEST,
            "support_sha256": EXPECTED_SUPPORT_DIGEST,
            "basis_sha256": object_digest(EXPECTED_BASIS_DIGESTS),
            "structural_mask_sha256": EXPECTED_STRUCTURAL_MASK_DIGEST,
        },
        "counts": dict(EXPECTED_OPERATION_COUNTS),
        "shapes": {
            "basis_modes_by_update": EXPECTED_BASIS_SHAPES,
            "mediator_keys_by_update": EXPECTED_MEDIATOR_KEY_COUNTS,
            "proper_cubic_frames": 24,
        },
        "residuals": {
            "norm": 0.0,
            "inverse": 0.0,
            "car_number": 0.0,
            "mediator_charge": 0.0,
            "lawfulness": 0.0,
            "repeat": 0.0,
            "post_stream_continuity": 0.0,
            "boundary_shell": 0.0,
            "dynamic_band_floor": 0.0,
            "dynamic_axial_seam_ceiling": 0.0,
            "dynamic_contact_floor": 0.0,
            "safe_train_mass": 0.0,
            "car_kernel": 0.0,
            "maximum_all24_complete_word_state_covariance": 0.0,
        },
        "structural_mask_sizes": EXPECTED_STRUCTURAL_MASK_COUNTS,
        "resource_usage": {
            "elapsed_seconds": 0.0,
            "maximum_RSS_bytes": 0,
            "swaps": 0,
            "serialized_bytes": 0,
        },
        "passes": {
            "technical": True,
            "resource": True,
            "all": True,
        },
        "verdict": "technical-resource-qualified",
    }


def contract_checks() -> tuple[dict[str, bool], dict]:
    train, held = contract.row_manifests()
    canonical = canonical_geometry()
    carried = proper_cubic_geometries()
    support = support_summary(canonical)
    mask = structural_mask_summary()
    source_hashes = {
        name: path.is_file() and file_sha(path) == EXPECTED_PREDECESSOR_HASHES[name]
        for name, (path, _expected) in contract.SOURCE_HASHES.items()
    }
    eligible = [
        row for row in train
        if row["role"] == "primary-mass-grid"
        and row["route"] in ("A-local-bond-current", "B-global-translation-character")
        and row["source_beta"] == SCOUT_BETA_NAME
        and row["probe_beta"] == SCOUT_BETA_NAME
        and row["deletion"] == SCOUT_DELETION
        and row["geometry"]["name"] == canonical.name
    ]
    physical_keys = {
        (
            row["source_beta"], row["probe_beta"], row["deletion"],
            row["geometry"]["name"], object_digest(row["exact_packet"]),
        )
        for row in eligible
    }
    frames_unique = len({tuple(int(value) for value in frame.ravel()) for frame, _g in carried}) == 24
    mirror = np.diag((-1, -1, 1))
    mirror_present = any(np.array_equal(frame, mirror) for frame, _geometry in carried)
    identity_count = sum(
        np.array_equal(frame, np.eye(3, dtype=int)) for frame, _geometry in carried
    )
    support_covariant = True
    canonical_rows, _overlap = support_trace(canonical)
    for frame, geometry in carried:
        rows, first_overlap = support_trace(geometry)
        support_covariant &= first_overlap == FIRST_CAUSAL_OVERLAP_UPDATE
        for original, moved in zip(canonical_rows, rows):
            support_covariant &= {
                carry_mode(mode, frame, canonical.side) for mode in original.basis
            } == set(moved.basis)
            support_covariant &= {
                carry_mediator(key, frame, canonical.side)
                for key in original.mediator_keys
            } == set(moved.mediator_keys)

    auth_fixtures = {
        "dry_absent": authorization_allowed("dry-contract", {}),
        "dry_empty_scout_rejected": not authorization_allowed(
            "dry-contract", {SCOUT_AUTHORIZATION_ENV: ""}
        ),
        "dry_train_rejected": not authorization_allowed(
            "dry-contract", {TRAIN_AUTHORIZATION_ENV: "present"}
        ),
        "resource_exact": authorization_allowed(
            "resource-scout", {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN}
        ),
        "resource_wrong_rejected": not authorization_allowed(
            "resource-scout", {SCOUT_AUTHORIZATION_ENV: "wrong"}
        ),
        "resource_train_presence_rejected": not authorization_allowed(
            "resource-scout", {
                SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN,
                TRAIN_AUTHORIZATION_ENV: "",
            },
        ),
    }
    exemplar = resource_output_exemplar()
    forbidden_fixture = resource_output_exemplar()
    forbidden_fixture["residuals"]["response_value"] = 0.0
    checks = {
        "authority_none": AUTHORITY == "none",
        "audit_unset": AUDIT == "unset",
        "contract_runner_hash": file_sha(CONTRACT_RUNNER) == CONTRACT_RUNNER_SHA256,
        "contract_note_hash": file_sha(CONTRACT_NOTE) == CONTRACT_NOTE_SHA256,
        "train_manifest_hash": contract.manifest_digest(train) == TRAIN_MANIFEST_SHA256,
        "held_manifest_hash": contract.manifest_digest(held) == HELD_MANIFEST_SHA256,
        "train_42_held_12": len(train) == 42 and len(held) == 12,
        "predecessor_hashes": all(source_hashes.values()),
        "c506_kernel_hash": file_sha(C506_KERNEL_RUNNER) == C506_KERNEL_RUNNER_SHA256,
        "old_scout_hash": file_sha(OLD_CYCLE509_SCOUT) == OLD_CYCLE509_SCOUT_SHA256,
        "old_history_declared": DECLARED_OLD_SCOUT_HISTORY["old_scout_runner_sha256"] == OLD_CYCLE509_SCOUT_SHA256,
        "kernel_signatures_and_neutrality": all(inherited_kernel_contract().values()),
        "canonical_geometry_exact": (
            canonical.name == contract.TRAIN_CANONICAL.name
            and canonical.side == contract.TRAIN_CANONICAL.side
            and canonical.source_cell == contract.TRAIN_CANONICAL.source_cell
            and canonical.probe_center == contract.TRAIN_CANONICAL.probe_center
            and canonical.outgoing_direction == contract.TRAIN_CANONICAL.outgoing_direction
            and canonical.causal_axis == contract.TRAIN_CANONICAL.causal_axis
            and canonical.depth == contract.TRAIN_CANONICAL.depth
            and canonical.packet_cells
            == tuple(contract.corridor_packet(contract.TRAIN_CANONICAL)["cells"])
            and canonical.packet_directions
            == (
                contract.corridor_packet(contract.TRAIN_CANONICAL)["positive_direction"],
                contract.corridor_packet(contract.TRAIN_CANONICAL)["negative_direction"],
            )
            and canonical.frame_flat
            == tuple(int(value) for value in np.eye(3, dtype=int).ravel())
        ),
        "all24_unique_identity_once_and_mirror": (
            len(carried) == 24 and frames_unique and identity_count == 1 and mirror_present
        ),
        "all24_support_and_mediator_covariant": support_covariant,
        "first_overlap_update_2": support["first_overlap_update"] == FIRST_CAUSAL_OVERLAP_UPDATE,
        "geometry_digest": geometry_digest() == EXPECTED_GEOMETRY_DIGEST,
        "support_digest": support["support_digest"] == EXPECTED_SUPPORT_DIGEST,
        "basis_digests": support["basis_digests"] == EXPECTED_BASIS_DIGESTS,
        "basis_shapes": support["basis_shapes"] == EXPECTED_BASIS_SHAPES,
        "mediator_key_counts": support["mediator_key_counts"] == EXPECTED_MEDIATOR_KEY_COUNTS,
        "structural_mask_digest": mask["digest"] == EXPECTED_STRUCTURAL_MASK_DIGEST,
        "structural_mask_counts": mask["counts"] == EXPECTED_STRUCTURAL_MASK_COUNTS,
        "structural_mask_not_from_pruning": mask["amplitude_pruning_certifies_mask"] is False,
        "exact_joint_AB_physical_row": len(eligible) == 2 and len(physical_keys) == 1,
        "routeC_and_held_inaccessible": all(not row["disposition"].startswith("held") for row in eligible)
        and all(row["route"] != "C-open-octahedral-multimediator" for row in eligible),
        "cli_has_no_selector_or_refit": CLI_MODES == ("dry-contract", "resource-scout"),
        "authorization_logic_fixtures": all(auth_fixtures.values()),
        "operation_counts": EXPECTED_OPERATION_COUNTS["forward_update_calls"] == 27 * DEPTH
        and EXPECTED_OPERATION_COUNTS["inverse_update_calls"] == DEPTH
        and EXPECTED_OPERATION_COUNTS["trajectory_calls"] == 28,
        "resource_output_schema": validate_resource_output(exemplar)
        and not validate_resource_output(forbidden_fixture),
        "dry_evolution_calls": True,
    }
    observed = {
        "geometry_digest": geometry_digest(),
        "support_digest": support["support_digest"],
        "basis_digests": support["basis_digests"],
        "basis_shapes": support["basis_shapes"],
        "mediator_key_counts": support["mediator_key_counts"],
        "structural_mask_digest": mask["digest"],
        "structural_mask_counts": mask["counts"],
        "first_overlap_update": support["first_overlap_update"],
        "eligible_manifest_rows": len(eligible),
        "unique_physical_rows": len(physical_keys),
        "operation_counts": EXPECTED_OPERATION_COUNTS,
        "source_hashes": source_hashes,
        "auth_fixtures": auth_fixtures,
        "evolution_calls": 0,
    }
    return checks, observed


def dry_contract() -> None:
    checks, observed = contract_checks()
    payload = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "mode": "dry-contract",
        "checks": checks,
        "observed": observed,
        "old_scout_history": DECLARED_OLD_SCOUT_HISTORY,
        "pass": all(checks.values()),
    }
    print("DRY_CONTRACT", json_bytes(payload).decode())
    if not all(checks.values()):
        raise SystemExit(1)


def resource_scout() -> None:
    started = time.monotonic()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(WALL_CEILING_SECONDS)
    try:
        checks, observed = contract_checks()
    except BaseException:
        signal.alarm(0)
        raise
    if not all(checks.values()):
        signal.alarm(0)
        raise RuntimeError("dry contract must pass before resource execution")
    ledger = ExecutionLedger()
    controls = TechnicalControls()
    maximum_covariance = 0.0
    try:
        geometry = canonical_geometry()
        rows, first_overlap = support_trace(geometry)
        if first_overlap != FIRST_CAUSAL_OVERLAP_UPDATE:
            raise RuntimeError("canonical first-overlap drift")
        operations = build_operations(rows, SCOUT_BETA)
        kernel = selected_band_kernel(geometry.side, SCOUT_BETA)
        spectral_projectors: tuple[np.ndarray | None, ...] = (None,) + tuple(
            selected_band_projector(kernel, row.basis, geometry.side)
            for row in rows[1:]
        )
        del kernel
        initial = initial_blocks(geometry, rows[0].basis)
        species = contract.c219.common_species(SCOUT_BETA)
        mass_residual = abs(contract.c219.rest_mass(species) - species.analytic_mass)
        emitter_angle = contract.EMITTER_COUPLING * species.analytic_mass
        collision_angle = contract.SCATTERING_COUPLING * species.analytic_mass

        interacting, interacting_controls = run_forward_trajectory(
            initial, rows, operations, geometry, emitter_angle, collision_angle,
            spectral_projectors, ledger, "canonical-interacting",
        )
        controls.absorb(interacting_controls)
        free_one, free_controls = run_forward_trajectory(
            initial, rows, operations, geometry, 0.0, 0.0,
            spectral_projectors, ledger, "canonical-matched-free",
        )
        controls.absorb(free_controls)
        free_two, repeat_controls = run_forward_trajectory(
            initial, rows, operations, geometry, 0.0, 0.0,
            spectral_projectors, ledger, "canonical-repeated-free",
        )
        controls.absorb(repeat_controls)
        repeat_residual = state_residual(free_one, free_two)
        free_one.clear()
        free_two.clear()

        restored = run_inverse_trajectory(
            interacting, rows, operations, geometry,
            emitter_angle, collision_angle, ledger,
        )
        inverse_residual = state_residual(restored, initial)
        restored.clear()
        del spectral_projectors
        gc.collect()

        null_projectors = tuple(None for _row in rows)
        carried_rows = proper_cubic_geometries()
        for frame, carried_geometry in carried_rows:
            frame_support, frame_overlap = support_trace(carried_geometry)
            if frame_overlap != FIRST_CAUSAL_OVERLAP_UPDATE:
                raise RuntimeError("carried first-overlap drift")
            frame_operations = build_operations(frame_support, SCOUT_BETA)
            frame_initial = initial_blocks(carried_geometry, frame_support[0].basis)
            frame_final, frame_controls = run_forward_trajectory(
                frame_initial, frame_support, frame_operations, carried_geometry,
                emitter_angle, collision_angle, null_projectors, ledger,
                "carried-interacting",
            )
            controls.absorb(frame_controls)
            maximum_covariance = max(
                maximum_covariance,
                carried_state_residual(
                    frame_final, interacting, rows[-1].basis,
                    frame_support[-1].basis, frame, geometry.side,
                ),
            )
            frame_final.clear()
            frame_initial.clear()
            del frame_support, frame_operations, frame_controls
            gc.collect()

        interacting.clear()
        initial.clear()
        del rows, operations, carried_rows
        gc.collect()

        actual_counts = {
            "resource_invocations": 1,
            "science_train_rows": 0,
            "held_rows": 0,
            "routeC_allocations": 0,
            "refit_performed": False,
            "canonical_interacting_forward_trajectories": ledger.canonical_interacting_forward_trajectories,
            "canonical_matched_free_forward_trajectories": ledger.canonical_matched_free_forward_trajectories,
            "canonical_repeated_free_forward_trajectories": ledger.canonical_repeated_free_forward_trajectories,
            "carried_interacting_forward_trajectories": ledger.carried_interacting_forward_trajectories,
            "forward_trajectories": ledger.forward_trajectories,
            "inverse_trajectories": ledger.inverse_trajectories,
            "trajectory_calls": ledger.forward_trajectories + ledger.inverse_trajectories,
            "forward_update_calls": ledger.forward_update_calls,
            "inverse_update_calls": ledger.inverse_update_calls,
            "post_car_technical_captures": ledger.post_car_technical_captures,
            "post_word_technical_captures": ledger.post_word_technical_captures,
        }
        mask = structural_mask_summary()
        residuals = {
            "norm": controls.maximum_norm_residual,
            "inverse": inverse_residual,
            "car_number": controls.maximum_car_number_residual,
            "mediator_charge": controls.maximum_mediator_charge_residual,
            "lawfulness": controls.maximum_lawfulness_residual,
            "repeat": repeat_residual,
            "post_stream_continuity": controls.maximum_post_stream_continuity_residual,
            "boundary_shell": controls.maximum_boundary_shell_weight,
            "dynamic_band_floor": max(0.0, BAND_FLOOR - controls.minimum_dynamic_band_fraction),
            "dynamic_axial_seam_ceiling": max(
                0.0, controls.maximum_dynamic_axial_seam_weight - AXIAL_SEAM_CEILING
            ),
            "dynamic_contact_floor": max(
                0.0, CONTACT_FLOOR - controls.maximum_dynamic_contact_weight
            ),
            "safe_train_mass": mass_residual,
            "car_kernel": controls.maximum_car_kernel_residual,
            "maximum_all24_complete_word_state_covariance": maximum_covariance,
        }
        technical_pass = (
            actual_counts == EXPECTED_OPERATION_COUNTS
            and residuals["norm"] <= NUMERIC_GATE
            and residuals["inverse"] <= NUMERIC_GATE
            and residuals["car_number"] <= NUMERIC_GATE
            and residuals["mediator_charge"] <= NUMERIC_GATE
            and residuals["lawfulness"] <= NUMERIC_GATE
            and residuals["repeat"] <= NUMERIC_GATE
            and residuals["post_stream_continuity"] <= CONTINUITY_GATE
            and residuals["boundary_shell"] <= BOUNDARY_GATE
            and residuals["dynamic_band_floor"] == 0.0
            and residuals["dynamic_axial_seam_ceiling"] == 0.0
            and residuals["dynamic_contact_floor"] == 0.0
            and residuals["safe_train_mass"] <= NUMERIC_GATE
            and residuals["car_kernel"] <= NUMERIC_GATE
            and residuals["maximum_all24_complete_word_state_covariance"] <= NUMERIC_GATE
        )
        payload = resource_output_exemplar()
        payload["counts"] = actual_counts
        payload["residuals"] = residuals
        payload["structural_mask_sizes"] = mask["counts"]
        payload["passes"]["technical"] = technical_pass

        # Prepare the complete nontrivial payload first, then recompute the
        # final wall/RSS/swap gates.  No later large state or array exists.
        prepared = json_bytes(payload)
        elapsed = time.monotonic() - started
        usage = {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": rss_bytes(),
            "swaps": swap_count(),
            "serialized_bytes": len(prepared),
        }
        payload["resource_usage"] = usage
        resource_pass = (
            usage["elapsed_seconds"] < WALL_CEILING_SECONDS
            and usage["maximum_RSS_bytes"] < RSS_CEILING_BYTES
            and usage["swaps"] <= SWAP_CEILING
        )
        payload["passes"]["resource"] = resource_pass
        payload["passes"]["all"] = technical_pass and resource_pass
        final_prepared = json_bytes(payload)
        # Recompute after final serialization, as required by the resource
        # contract; update once more and serialize only the small final object.
        payload["resource_usage"] = {
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "swaps": swap_count(),
            "serialized_bytes": len(final_prepared),
        }
        final_resource_pass = (
            payload["resource_usage"]["elapsed_seconds"] < WALL_CEILING_SECONDS
            and payload["resource_usage"]["maximum_RSS_bytes"] < RSS_CEILING_BYTES
            and payload["resource_usage"]["swaps"] <= SWAP_CEILING
        )
        payload["passes"]["resource"] = final_resource_pass
        payload["passes"]["all"] = technical_pass and final_resource_pass
        payload["verdict"] = (
            "technical-resource-qualified"
            if payload["passes"]["all"] else "technical-resource-blocked"
        )
        if not validate_resource_output(payload):
            raise RuntimeError("resource output schema violation")
        print("RESOURCE_RESULT", json_bytes(payload).decode(), flush=True)
        if not payload["passes"]["all"]:
            raise SystemExit(1)
    finally:
        signal.alarm(0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, required=True)
    arguments = parser.parse_args()
    enforce_authorization(arguments.mode, os.environ)
    if arguments.mode == "dry-contract":
        dry_contract()
    elif arguments.mode == "resource-scout":
        resource_scout()
    else:
        raise SystemExit("unreachable mode")


if __name__ == "__main__":
    main()
