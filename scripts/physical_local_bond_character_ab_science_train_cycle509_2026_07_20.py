#!/usr/bin/env python3
"""Cycle 509 Route-A/B science-train evaluator.

``dry-contract`` performs no amplitude evolution.  It checks the frozen
Revision-3 contract, the separately qualified parameterized resource
transcript, the explicit 34-row A/B train manifest, output schemas, operation
counts, and authorization separation.  ``science-train`` is a separately
authorized, selector-free execution of exactly those 34 rows.  It has no held
or Route-C execution path and performs no refit.

Route A samples the post-CAR-stream/pre-contact/pre-collision occupation and
retains the complete interaction-minus-matched-free local and plane bond
fields together with the complete conservative Boolean mask.  Route B samples
the translation character only after the complete word and uses unit phasors
and chord geometry.  The literal all-24 controls evolve full states and compare
exact carried masks; they never select or modify a response.

Authority none; audit unset.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
import io
import json
import multiprocessing
import os
from pathlib import Path
import resource
from queue import Empty
import sys
import tempfile
import time
from typing import Mapping
import zipfile

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_local_bond_character_bulk_tournament_preflight_cycle509_2026_07_20 as contract
import physical_local_bond_character_ab_parameterized_resource_scout_cycle509_2026_07_20 as engine
import fock_modular_boundary_current_cycle229_2026_07_17 as c229


AUTHORITY = "none"
AUDIT = "unset"
CLI_MODES = ("dry-contract", "science-train")

CONTRACT_RUNNER = ROOT / "scripts/physical_local_bond_character_bulk_tournament_preflight_cycle509_2026_07_20.py"
CONTRACT_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_BOND_CHARACTER_BULK_TOURNAMENT_PREFLIGHT_CYCLE509_NOTE_2026-07-20.md"
)
RESOURCE_RUNNER = ROOT / "scripts/physical_local_bond_character_ab_parameterized_resource_scout_cycle509_2026_07_20.py"
FOCK_RUNNER = ROOT / "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py"
RESOURCE_TRANSCRIPT = ROOT / "outputs/physical_local_bond_character_ab_resource_scout_cycle509_2026_07_20.log"
OUTPUT_ROOT = ROOT / "outputs/physical_local_bond_character_ab_train_cycle509_2026_07_20"
PACKAGE_CEILING_BYTES = 64 * 1024 * 1024

CONTRACT_RUNNER_SHA256 = "44a0430dafd31db471e6ada2435aa4a819637d09ac0af15ac387126e61ccd458"
CONTRACT_NOTE_SHA256 = "733aa72a2b2ef43f5b3a049903a85fa81b18c1413bcbe4d66f2a17345dce1d50"
RESOURCE_RUNNER_SHA256 = "bb1811aba604937ecf706c35b83ffb44f7b5155ca91145c1f33b66359022b924"
RESOURCE_TRANSCRIPT_SHA256 = "0c4ca3eadd9b4a078af7f7d63fb513ada1270a99b210ef2801cd1d660cf7b597"
RESOURCE_PAYLOAD_SHA256 = "12a0620d7a80466e3d13ea0a6db42e3a047f926644e04c05c13a70f74bb0c8ff"
FOCK_RUNNER_SHA256 = "fbf434a94c8dae57ffb6e68776642e4342a91f0d39f071ee1388fcb89ff846d7"
FULL_TRAIN_MANIFEST_SHA256 = "d235ce413eaba7ac62c9100d45ef93824c246a4646f4cd9316c5a0191f1c73d8"
HELD_MANIFEST_SHA256_BINDING_ONLY = "7dcaf19fb91b49bbe6528f124e4f428d7d54774390ff608e6afef5841657facf"
AB_TRAIN_MANIFEST_SHA256 = "f6dfdbd48ef38a10f2b7659ef5192950a0c17c257c042be8515da355999a44b2"

TRAIN_AUTHORIZATION_ENV = "CYCLE509_TRAIN_AUTHORIZATION"
TRAIN_AUTHORIZATION_TOKEN = "root-cycle509-revision2-train-after-dry-review-2026-07-20"
SCOUT_AUTHORIZATION_ENV = "CYCLE509_SCOUT_AUTHORIZATION"
HELD_AUTHORIZATION_ENV = "CYCLE509_HELD_AUTHORIZATION"
SCIENCE_INTEGRITY_ENV = "CYCLE509_SCIENCE_INTEGRITY_SHA256"

NUMERIC_GATE = 1e-8
CONTINUITY_GATE = 1e-10
BOUNDARY_GATE = 1e-12
CHARACTER_FLOOR = 0.05
FIELD_ZERO_GATE = 1e-12
DEPTH = 5
RESPONSE_WINDOW = (2, 3, 4, 5)

ROUTE_A = "A-local-bond-current"
ROUTE_B = "B-global-translation-character"
ROUTE_C = "C-open-octahedral-multimediator"
NO_DELETION = "none"
DELETIONS = (
    "emitter", "collision", "mediator-stream", "contact", "probe-coin",
    "source-mass-factor", "probe-mass-factor",
)

# This tuple is the immutable row schedule.  It is explicit, ordered, and complete: no
# runtime filtering of the 42-row train manifest and no construction of the
# held manifest occurs in this runner.  Entry fields are
# (route, role, source beta name, probe beta name, geometry, deletion).
ORDERED_AB_TRAIN_KEYS = (
    (ROUTE_A, "primary-mass-grid", "-2pi/9", "-2pi/9", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-2pi/9", "-4pi/9", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-2pi/9", "-2pi/3", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-4pi/9", "-2pi/9", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-4pi/9", "-4pi/9", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-4pi/9", "-2pi/3", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-2pi/3", "-2pi/9", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-2pi/3", "-4pi/9", "train-canonical", NO_DELETION),
    (ROUTE_A, "primary-mass-grid", "-2pi/3", "-2pi/3", "train-canonical", NO_DELETION),
    (ROUTE_A, "mirrored-direction-control", "-4pi/9", "-4pi/9", "train-mirrored", NO_DELETION),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "emitter"),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "collision"),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "mediator-stream"),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "contact"),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "probe-coin"),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "source-mass-factor"),
    (ROUTE_A, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "probe-mass-factor"),
    (ROUTE_B, "primary-mass-grid", "-2pi/9", "-2pi/9", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-2pi/9", "-4pi/9", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-2pi/9", "-2pi/3", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-4pi/9", "-2pi/9", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-4pi/9", "-4pi/9", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-4pi/9", "-2pi/3", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-2pi/3", "-2pi/9", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-2pi/3", "-4pi/9", "train-canonical", NO_DELETION),
    (ROUTE_B, "primary-mass-grid", "-2pi/3", "-2pi/3", "train-canonical", NO_DELETION),
    (ROUTE_B, "mirrored-direction-control", "-4pi/9", "-4pi/9", "train-mirrored", NO_DELETION),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "emitter"),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "collision"),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "mediator-stream"),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "contact"),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "probe-coin"),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "source-mass-factor"),
    (ROUTE_B, "selected-deletion", "-4pi/9", "-4pi/9", "train-canonical", "probe-mass-factor"),
)

BETA_VALUES = {
    "-2pi/9": -2 * np.pi / 9,
    "-4pi/9": -4 * np.pi / 9,
    "-2pi/3": -2 * np.pi / 3,
}

EXPECTED_EXACT_MASK_DIGESTS = {
    ("train-canonical-3D-L25", "intact"): (
        "e3997a01c7009fabbe52bd3932071935abade6cf4a547ddd0fb9d2ccf31a4550",
        "65dc9fdf976c633ea6cc66eb3f93c6ad2b96d3ab9f6c2303e668b03d9651d14b",
    ),
    ("train-canonical-3D-L25", "identity-coin"): (
        "12c4dd30dd9031002cb2ef3ffa7f4f2afb2a722bf1ae15d777afb22d5b7586a0",
        "8f4eea888cacd9f1272c9e1a987b986c7b32d0012aa3433733f19d2e9c53c1f7",
    ),
    ("train-canonical-3D-L25", "parked-mediator"): (
        "c00375088307ad4a24e0468eb03c1186f89a96515e6c334b76cc37dfbb32b41c",
        "98f3ddd3f29cce960dd8d19a1bae4acb0de402a2c349f9801b1fc0c130bf0378",
    ),
    ("train-mirrored-3D-L25", "intact"): (
        "d77beb6081f2055dd5b3c9aea8130f29202284cc842619dd5e6c10b84f9a1789",
        "924611139b018195ccd361f066963f805e8017e887b2c238ef902fda3d9ff51c",
    ),
}
EXPECTED_EXACT_MASK_BUNDLE_SHA256 = (
    "fdfc8800e6a6725458c9bf9f6ce095060018d937abbddd25e8c9fe015221bfaa"
)

EXPECTED_COUNTS = {
    "science_train_invocations": 1,
    "science_train_rows": 34,
    "route_A_rows": 17,
    "route_B_rows": 17,
    "route_C_rows": 0,
    "route_C_open_manifest_rows": 8,
    "held_rows": 0,
    "refit_performed": False,
    "canonical_interacting_forward_trajectories": 34,
    "canonical_matched_free_forward_trajectories": 34,
    "canonical_repeated_free_forward_trajectories": 34,
    "carried_interacting_forward_trajectories": 816,
    "carried_matched_free_forward_trajectories": 816,
    "forward_trajectories": 1734,
    "inverse_trajectories": 34,
    "trajectory_calls": 1768,
    "forward_update_calls": 8670,
    "inverse_update_calls": 170,
    "post_car_technical_captures": 8670,
    "post_word_technical_captures": 8670,
}

RESOURCE_TOP_LEVEL_ALLOWLIST = {
    "verdict", "passes", "counts", "digests", "residuals",
    "resource_usage", "shapes", "structural_mask_sizes",
}
COMMON_ARTIFACT_MEMBERS = {
    "canonical_mask_packbits", "carried_mask_packbits_all24",
    "mask_unpacked_shape", "all24_state_residuals",
    "all24_response_residuals", "artifact_metadata_utf8",
}
ROUTE_A_ARTIFACT_MEMBERS = COMMON_ARTIFACT_MEMBERS | {
    "delta_j", "delta_J", "front_trace_lab", "front_trace_carried",
    "fixed_trace_lab", "fixed_trace_carried",
}
ROUTE_B_ARTIFACT_MEMBERS = COMMON_ARTIFACT_MEMBERS | {
    "interacting_characters_all_axes", "free_characters_all_axes",
    "repeated_free_characters_all_axes", "response_phasors_all_axes",
    "principal_angles_diagnostic_only",
    "interacting_character_magnitudes", "matched_free_character_magnitudes",
    "repeated_free_character_magnitudes",
}


@dataclass
class Ledger:
    science_train_invocations: int = 1
    science_train_rows: int = 0
    route_A_rows: int = 0
    route_B_rows: int = 0
    route_C_rows: int = 0
    route_C_open_manifest_rows: int = 8
    held_rows: int = 0
    refit_performed: bool = False
    canonical_interacting_forward_trajectories: int = 0
    canonical_matched_free_forward_trajectories: int = 0
    canonical_repeated_free_forward_trajectories: int = 0
    carried_interacting_forward_trajectories: int = 0
    carried_matched_free_forward_trajectories: int = 0
    forward_trajectories: int = 0
    inverse_trajectories: int = 0
    trajectory_calls: int = 0
    forward_update_calls: int = 0
    inverse_update_calls: int = 0
    post_car_technical_captures: int = 0
    post_word_technical_captures: int = 0


def json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def object_digest(value: object) -> str:
    return sha256(json_bytes(value)).hexdigest()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def authorization_allowed(mode: str, environ: Mapping[str, str]) -> bool:
    train = TRAIN_AUTHORIZATION_ENV in environ
    scout = SCOUT_AUTHORIZATION_ENV in environ
    held = HELD_AUTHORIZATION_ENV in environ
    integrity = SCIENCE_INTEGRITY_ENV in environ
    if mode == "dry-contract":
        return not train and not scout and not held and not integrity
    if mode == "science-train":
        return (
            train and integrity and not scout and not held
            and environ[TRAIN_AUTHORIZATION_ENV] == TRAIN_AUTHORIZATION_TOKEN
            and environ[SCIENCE_INTEGRITY_ENV] == file_sha(Path(__file__))
        )
    return False


def enforce_authorization(mode: str, environ: Mapping[str, str]) -> None:
    if authorization_allowed(mode, environ):
        return
    present = tuple(
        name for name in (
            TRAIN_AUTHORIZATION_ENV, SCOUT_AUTHORIZATION_ENV,
            HELD_AUTHORIZATION_ENV,
            SCIENCE_INTEGRITY_ENV,
        ) if name in environ
    )
    raise SystemExit(
        "authorization gate rejected mode=" + mode
        + " present=" + repr(present)
    )


def geometry_by_name(name: str) -> contract.CorridorGeometry:
    if name == "train-canonical":
        return contract.TRAIN_CANONICAL
    if name == "train-mirrored":
        return contract.TRAIN_MIRRORED
    raise ValueError("non-train geometry is unreachable")


def build_ab_train_manifest() -> tuple[dict, ...]:
    rows = []
    for route, role, source_name, probe_name, geometry_name, deletion in ORDERED_AB_TRAIN_KEYS:
        rows.append(contract.corridor_row(
            "train", role, route, BETA_VALUES[source_name], BETA_VALUES[probe_name],
            geometry_by_name(geometry_name), deletion,
        ))
    return tuple(rows)


def row_identity(index: int, row: dict) -> dict:
    return {
        "index": index,
        "route": row["route"],
        "role": row["role"],
        "source_beta": row["source_beta"],
        "probe_beta": row["probe_beta"],
        "geometry": row["geometry"]["name"],
        "deletion": row["deletion"],
        "row_sha256": object_digest(row),
    }


def parse_qualified_resource() -> dict:
    if file_sha(RESOURCE_TRANSCRIPT) != RESOURCE_TRANSCRIPT_SHA256:
        raise RuntimeError("qualified resource transcript hash drift")
    with RESOURCE_TRANSCRIPT.open(encoding="utf-8") as stream:
        first = stream.readline().rstrip("\n")
    prefix = "RESOURCE_RESULT "
    if not first.startswith(prefix):
        raise RuntimeError("resource transcript lacks first-line RESOURCE_RESULT")
    payload = json.loads(first[len(prefix):])
    if set(payload) != RESOURCE_TOP_LEVEL_ALLOWLIST:
        raise RuntimeError("resource transcript exposed a nontechnical field")
    if object_digest(payload) != RESOURCE_PAYLOAD_SHA256:
        raise RuntimeError("resource technical payload drift")
    expected_digests = {
        "contract_runner_sha256": CONTRACT_RUNNER_SHA256,
        "contract_note_sha256": CONTRACT_NOTE_SHA256,
        "train_manifest_sha256": FULL_TRAIN_MANIFEST_SHA256,
        "held_manifest_sha256": HELD_MANIFEST_SHA256_BINDING_ONLY,
        "geometry_sha256": engine.EXPECTED_GEOMETRY_DIGEST,
        "support_sha256": engine.EXPECTED_SUPPORT_DIGEST,
        "structural_mask_sha256": engine.EXPECTED_STRUCTURAL_MASK_DIGEST,
    }
    exact = (
        payload["verdict"] == "technical-resource-qualified"
        and payload["passes"] == {"all": True, "resource": True, "technical": True}
        and all(payload["digests"].get(key) == value for key, value in expected_digests.items())
        and payload["counts"] == engine.EXPECTED_OPERATION_COUNTS
        and payload["shapes"]["proper_cubic_frames"] == 24
        and payload["shapes"]["basis_modes_by_update"] == list(engine.EXPECTED_BASIS_SHAPES)
        and payload["shapes"]["mediator_keys_by_update"] == list(engine.EXPECTED_MEDIATOR_KEY_COUNTS)
        and payload["structural_mask_sizes"] == [list(row) for row in engine.EXPECTED_STRUCTURAL_MASK_COUNTS]
        and payload["resource_usage"]["elapsed_seconds"] < engine.WALL_CEILING_SECONDS
        and payload["resource_usage"]["maximum_RSS_bytes"] < engine.RSS_CEILING_BYTES
        and payload["resource_usage"]["swaps"] == 0
    )
    if not exact:
        raise RuntimeError("resource transcript is not the exact qualified technical result")
    return payload


def science_dependency_bundle() -> dict:
    """Rehash every consumed executable/evidence dependency."""
    bindings = {
        "Revision3_contract_runner": (CONTRACT_RUNNER, CONTRACT_RUNNER_SHA256),
        "Revision3_contract_note": (CONTRACT_NOTE, CONTRACT_NOTE_SHA256),
        "parameterized_resource_runner": (RESOURCE_RUNNER, RESOURCE_RUNNER_SHA256),
        "qualified_resource_transcript": (
            RESOURCE_TRANSCRIPT, RESOURCE_TRANSCRIPT_SHA256
        ),
        "Cycle229_Fock_lift": (FOCK_RUNNER, FOCK_RUNNER_SHA256),
        "Cycle506_numeric_kernels": (
            engine.C506_KERNEL_RUNNER, engine.C506_KERNEL_RUNNER_SHA256
        ),
    }
    for name, (path, expected) in contract.SOURCE_HASHES.items():
        bindings["predecessor_" + name] = (path, expected)
    rows = {}
    for name, (path, expected) in bindings.items():
        observed = file_sha(path)
        rows[name] = {
            "path": str(path.relative_to(ROOT)),
            "expected_sha256": expected,
            "observed_sha256": observed,
            "pass": observed == expected,
        }
    parse_qualified_resource()
    observed_runner_sha256 = file_sha(Path(__file__))
    reviewed_runner_sha256 = os.environ.get(SCIENCE_INTEGRITY_ENV)
    if (
        reviewed_runner_sha256 is not None
        and observed_runner_sha256 != reviewed_runner_sha256
    ):
        raise RuntimeError(
            "science runner no longer matches externally reviewed integrity hash"
        )
    bundle = {
        "science_runner": {
            "path": str(Path(__file__).resolve().relative_to(ROOT)),
            "observed_sha256": observed_runner_sha256,
            "externally_reviewed_sha256": reviewed_runner_sha256,
            "review_authority": "external exact integrity environment",
        },
        "dependencies": rows,
        "qualified_resource_payload_sha256": RESOURCE_PAYLOAD_SHA256,
        "all_dependencies_pass": all(row["pass"] for row in rows.values()),
    }
    bundle["bundle_sha256"] = object_digest(bundle)
    if not bundle["all_dependencies_pass"]:
        raise RuntimeError("science dependency hash bundle failed")
    return bundle


def geometry_from_row(row: dict) -> engine.CarriedGeometry:
    data = row["geometry"]
    packet = row["exact_packet"]
    return engine.CarriedGeometry(
        name=data["name"], side=int(data["side"]),
        source_cell=tuple(data["source_cell"]),
        probe_center=tuple(data["probe_center"]),
        outgoing_direction=int(data["outgoing_direction"]),
        causal_axis=int(data["causal_axis"]), depth=int(data["depth"]),
        packet_cells=tuple(tuple(cell) for cell in packet["cells"]),
        packet_directions=(int(packet["positive_direction"]), int(packet["negative_direction"])),
        frame_flat=tuple(int(value) for value in np.eye(3, dtype=int).ravel()),
    )


def structural_support_trace(
    geometry: engine.CarriedGeometry, *, probe_coin_identity: bool,
    mediator_stream_enabled: bool = True,
) -> tuple[engine.SupportSlice, ...]:
    """Amplitude-independent support recursion for the chosen deletion word."""
    car_modes = set(engine.initial_modes(geometry))
    mediator_post: set[engine.Mediator] = {None}
    rows = [engine.SupportSlice(0, tuple(sorted(car_modes)), (None,), ())]
    for update in range(1, geometry.depth + 1):
        if probe_coin_identity:
            car_streamed = {
                (
                    tuple(int(value) for value in (
                        np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                    )), direction,
                )
                for cell, direction in car_modes
            }
        else:
            cells_before = {cell for cell, _direction in car_modes}
            car_streamed = {
                (
                    tuple(int(value) for value in (
                        np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                    )), direction,
                )
                for cell in cells_before for direction in range(6)
            }
        mediator_pre = set(mediator_post)
        mediator_pre.add((geometry.source_cell, geometry.outgoing_direction))
        collision_mediator: set[engine.Mediator] = {None}
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
        for cell in collision_cells:
            car_streamed.update((cell, direction) for direction in range(6))
        mediator_post = {None}
        for key in collision_mediator:
            if key is None:
                continue
            cell, direction = key
            target_cell = (
                tuple(int(value) for value in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                )) if mediator_stream_enabled else cell
            )
            mediator_post.add((target_cell, direction))
        car_modes = car_streamed
        rows.append(engine.SupportSlice(
            update, tuple(sorted(car_modes)),
            tuple(sorted(mediator_post, key=repr)),
            tuple(sorted(collision_cells)),
        ))
    return tuple(rows)


def propagate_tainted_modes(
    tainted: set[engine.Mode], *, probe_coin_identity: bool,
) -> set[engine.Mode]:
    if probe_coin_identity:
        return {
            (
                tuple(int(value) for value in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                )), direction,
            )
            for cell, direction in tainted
        }
    cells = {cell for cell, _direction in tainted}
    return {
        (
            tuple(int(value) for value in (
                np.asarray(cell) + contract.c210.DIRECTIONS[direction]
            )), direction,
        )
        for cell in cells for direction in range(6)
    }


def modes_to_bond_mask(
    modes: set[engine.Mode], side: int,
) -> np.ndarray:
    mask = np.zeros((side, side, side, 3), dtype=bool)
    for cell, direction in modes:
        axis = direction // 2
        anchor = np.asarray(cell, dtype=int).copy()
        if direction % 2 == 1:
            anchor += np.eye(3, dtype=int)[axis]
        mask[tuple(int(value % side) for value in anchor) + (axis,)] = True
    return mask


BooleanAdjacency = dict[engine.Mediator, np.ndarray]


def boolean_state_count(matrices: BooleanAdjacency) -> int:
    """Count unordered, Pauli-lawful joint states in symmetric adjacencies."""
    return sum(int(np.count_nonzero(matrix)) // 2 for matrix in matrices.values())


def direct_joint_state_digest(states: set[tuple]) -> str:
    return object_digest(tuple(sorted(states, key=repr)))


def adjacency_joint_state_digest(
    matrices: BooleanAdjacency, basis: tuple[engine.Mode, ...],
) -> str:
    states = []
    for mediator, matrix in sorted(matrices.items(), key=lambda item: repr(item[0])):
        left, right = np.nonzero(matrix)
        for left_index, right_index in zip(left, right):
            if left_index < right_index:
                states.append((
                    mediator, basis[int(left_index)], basis[int(right_index)]
                ))
    return object_digest(tuple(sorted(states, key=repr)))


def validate_boolean_adjacency(
    support: BooleanAdjacency, taint: BooleanAdjacency,
) -> None:
    """Enforce the exact quotient invariants at every substep."""
    for label, matrices in (("support", support), ("taint", taint)):
        for mediator, matrix in matrices.items():
            if matrix.dtype != np.bool_ or matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
                raise RuntimeError(f"{label} Boolean adjacency schema drift: {mediator!r}")
            if np.any(np.diag(matrix)) or not np.array_equal(matrix, matrix.T):
                raise RuntimeError(f"{label} Boolean adjacency lost wedge symmetry: {mediator!r}")
    for mediator, matrix in taint.items():
        if mediator not in support or np.any(matrix & ~support[mediator]):
            raise RuntimeError(f"taint is not a subset of support: {mediator!r}")


def boolean_cell_quotient_count(
    matrices: BooleanAdjacency, basis: tuple[engine.Mode, ...],
) -> int:
    """Count occupied mediator/cell-pair blocks without losing direction data."""
    cells = tuple(sorted({cell for cell, _direction in basis}))
    cell_index = {cell: index for index, cell in enumerate(cells)}
    inverse = np.asarray([cell_index[cell] for cell, _direction in basis], dtype=np.intp)
    total = 0
    for matrix in matrices.values():
        left, right = np.nonzero(matrix)
        quotient = np.zeros((len(cells), len(cells)), dtype=bool)
        quotient[inverse[left], inverse[right]] = True
        total += (
            int(np.count_nonzero(quotient))
            + int(np.count_nonzero(np.diag(quotient)))
        ) // 2
    return total


def initial_boolean_adjacency(
    geometry: engine.CarriedGeometry,
) -> tuple[tuple[engine.Mode, ...], BooleanAdjacency, BooleanAdjacency]:
    basis = tuple(sorted(engine.initial_modes(geometry)))
    index = {mode: position for position, mode in enumerate(basis)}
    support = np.zeros((len(basis), len(basis)), dtype=bool)
    positive, negative = geometry.packet_directions
    for left_cell in geometry.packet_cells:
        for right_cell in geometry.packet_cells:
            left = index[(left_cell, positive)]
            right = index[(right_cell, negative)]
            if left != right:
                support[left, right] = True
                support[right, left] = True
    return basis, {None: support}, {}


def emit_boolean_adjacency(
    matrices: BooleanAdjacency, source_key: engine.Mediator,
) -> BooleanAdjacency:
    """Exact generic-nonzero emitter image, sector by sector."""
    output = {
        mediator: matrix
        for mediator, matrix in matrices.items()
        if mediator not in (None, source_key)
    }
    candidates = [
        matrices[mediator] for mediator in (None, source_key)
        if mediator in matrices
    ]
    if candidates:
        combined = candidates[0].copy()
        for matrix in candidates[1:]:
            np.logical_or(combined, matrix, out=combined)
        output[None] = combined
        output[source_key] = combined.copy()
    return output


def dense_stream_boolean_adjacency(
    matrices: BooleanAdjacency,
    old_basis: tuple[engine.Mode, ...], new_basis: tuple[engine.Mode, ...],
) -> BooleanAdjacency:
    """Exact Boolean dense-coin/stream image via the old-cell quotient.

    Every outgoing direction has the same six-dimensional dense-coin support.
    Thus only existence of an old joint edge between two origin cells is needed
    during this substep; expanding that cell relation on the new directed-mode
    basis is an exact Boolean image, not a marginal approximation.
    """
    old_cells = tuple(sorted({cell for cell, _direction in old_basis}))
    old_cell_index = {cell: index for index, cell in enumerate(old_cells)}
    old_inverse = np.asarray(
        [old_cell_index[cell] for cell, _direction in old_basis], dtype=np.intp
    )
    origins = []
    for cell, direction in new_basis:
        origin = tuple(int(value) for value in (
            np.asarray(cell) - contract.c210.DIRECTIONS[direction]
        ))
        origins.append(old_cell_index.get(origin, -1))
    valid_new = np.asarray([value >= 0 for value in origins], dtype=bool)
    origin_index = np.asarray([max(value, 0) for value in origins], dtype=np.intp)
    output: BooleanAdjacency = {}
    for mediator, matrix in matrices.items():
        left, right = np.nonzero(matrix)
        cell_relation = np.zeros((len(old_cells), len(old_cells)), dtype=bool)
        cell_relation[old_inverse[left], old_inverse[right]] = True
        expanded = cell_relation[np.ix_(origin_index, origin_index)]
        expanded &= valid_new[:, None]
        expanded &= valid_new[None, :]
        np.fill_diagonal(expanded, False)
        if np.any(expanded):
            output[mediator] = expanded
    return output


def identity_stream_boolean_adjacency(
    matrices: BooleanAdjacency,
    old_basis: tuple[engine.Mode, ...], new_basis: tuple[engine.Mode, ...],
) -> BooleanAdjacency:
    """Exact identity-coin stream image on the directed-mode basis."""
    new_index = {mode: position for position, mode in enumerate(new_basis)}
    moved = np.asarray([
        new_index[(
            tuple(int(value) for value in (
                np.asarray(cell) + contract.c210.DIRECTIONS[direction]
            )),
            direction,
        )]
        for cell, direction in old_basis
    ], dtype=np.intp)
    output: BooleanAdjacency = {}
    for mediator, matrix in matrices.items():
        expanded = np.zeros((len(new_basis), len(new_basis)), dtype=bool)
        expanded[np.ix_(moved, moved)] = matrix
        if np.any(expanded):
            output[mediator] = expanded
    return output


def add_boolean_edges(
    matrices: BooleanAdjacency, mediator: engine.Mediator,
    dimension: int, fixed: int, partners: np.ndarray,
) -> None:
    if partners.size == 0:
        return
    matrix = matrices.get(mediator)
    if matrix is None:
        matrix = np.zeros((dimension, dimension), dtype=bool)
        matrices[mediator] = matrix
    matrix[fixed, partners] = True
    matrix[partners, fixed] = True


def collision_boolean_adjacency(
    support: BooleanAdjacency, taint: BooleanAdjacency,
    basis: tuple[engine.Mode, ...],
) -> tuple[BooleanAdjacency, BooleanAdjacency, int]:
    """Exact old/new collision image and exact taint seed on joint edges."""
    index = {mode: position for position, mode in enumerate(basis)}
    events = []
    for mediator, matrix in tuple(support.items()):
        if mediator is None:
            continue
        cell, direction = mediator
        old = index.get((cell, contract.REVERSE[direction]))
        new = index.get((cell, direction))
        if old is None or new is None:
            continue
        partners = np.flatnonzero(matrix[old]).astype(np.intp, copy=False)
        # If the partner already is the new mode, the scattered wedge vanishes;
        # the frozen direct recursion consequently seeds neither edge.
        partners = partners[partners != new]
        if partners.size:
            events.append((mediator, (cell, contract.REVERSE[direction]), old, new, partners.copy()))
    dimension = len(basis)
    for mediator, reversed_mediator, old, new, partners in events:
        add_boolean_edges(support, reversed_mediator, dimension, new, partners)
        add_boolean_edges(taint, mediator, dimension, old, partners)
        add_boolean_edges(taint, reversed_mediator, dimension, new, partners)
    return support, taint, len(events)


def mediator_stream_boolean_adjacency(
    matrices: BooleanAdjacency, *, enabled: bool,
) -> BooleanAdjacency:
    if not enabled:
        return matrices
    output: BooleanAdjacency = {}
    for mediator, matrix in matrices.items():
        if mediator is None:
            target = None
        else:
            cell, direction = mediator
            target = (
                tuple(int(value) for value in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                )),
                direction,
            )
        if target in output:
            np.logical_or(output[target], matrix, out=output[target])
        else:
            output[target] = matrix
    return output


def adjacency_taint_mask(
    taint: BooleanAdjacency, basis: tuple[engine.Mode, ...], side: int,
) -> np.ndarray:
    active = np.zeros(len(basis), dtype=bool)
    for matrix in taint.values():
        active |= np.any(matrix, axis=0)
    return modes_to_bond_mask(
        {basis[index] for index in np.flatnonzero(active)}, side
    )


def mask_digest(masks: tuple[np.ndarray, ...]) -> str:
    return sha256(b"".join(
        np.packbits(mask.ravel(), bitorder="little").tobytes()
        for mask in masks
    )).hexdigest()


def exact_factorized_boolean_certificate(
    geometry: engine.CarriedGeometry, *, probe_coin_identity: bool,
    mediator_stream_enabled: bool, retain_joint_digests: bool = False,
) -> dict:
    """Exact joint Boolean recursion in factorized symmetric adjacencies."""
    structural_rows = structural_support_trace(
        geometry, probe_coin_identity=probe_coin_identity,
        mediator_stream_enabled=mediator_stream_enabled,
    )
    basis, support, taint = initial_boolean_adjacency(geometry)
    source_key: engine.Mediator = (
        geometry.source_cell, geometry.outgoing_direction
    )
    validate_boolean_adjacency(support, taint)
    route_a = []
    route_b = []
    rows = []
    for update in range(1, geometry.depth + 1):
        support = emit_boolean_adjacency(support, source_key)
        taint = emit_boolean_adjacency(taint, source_key)
        validate_boolean_adjacency(support, taint)
        next_basis = structural_rows[update].basis
        stream = (
            identity_stream_boolean_adjacency
            if probe_coin_identity else dense_stream_boolean_adjacency
        )
        support = stream(support, basis, next_basis)
        taint = stream(taint, basis, next_basis)
        validate_boolean_adjacency(support, taint)
        pre_support = boolean_state_count(support)
        pre_taint = boolean_state_count(taint)
        pre_support_digest = (
            adjacency_joint_state_digest(support, next_basis)
            if retain_joint_digests else None
        )
        pre_taint_digest = (
            adjacency_joint_state_digest(taint, next_basis)
            if retain_joint_digests else None
        )
        route_a.append(adjacency_taint_mask(taint, next_basis, geometry.side))
        support, taint, collision_sector_count = collision_boolean_adjacency(
            support, taint, next_basis
        )
        validate_boolean_adjacency(support, taint)
        post_support = boolean_state_count(support)
        post_taint = boolean_state_count(taint)
        post_support_digest = (
            adjacency_joint_state_digest(support, next_basis)
            if retain_joint_digests else None
        )
        post_taint_digest = (
            adjacency_joint_state_digest(taint, next_basis)
            if retain_joint_digests else None
        )
        route_b.append(adjacency_taint_mask(taint, next_basis, geometry.side))
        support = mediator_stream_boolean_adjacency(
            support, enabled=mediator_stream_enabled
        )
        taint = mediator_stream_boolean_adjacency(
            taint, enabled=mediator_stream_enabled
        )
        validate_boolean_adjacency(support, taint)
        row_record = {
            "update": update,
            "pre_collision_support_states": pre_support,
            "post_collision_support_states": post_support,
            "pre_collision_tainted_states": pre_taint,
            "post_collision_tainted_states": post_taint,
            "post_stream_support_states": boolean_state_count(support),
            "post_stream_tainted_states": boolean_state_count(taint),
            "post_stream_support_cell_blocks": boolean_cell_quotient_count(
                support, next_basis
            ),
            "post_stream_taint_cell_blocks": boolean_cell_quotient_count(
                taint, next_basis
            ),
            "collision_mediator_sectors": collision_sector_count,
        }
        if retain_joint_digests:
            row_record.update({
                "pre_collision_support_joint_sha256": pre_support_digest,
                "pre_collision_taint_joint_sha256": pre_taint_digest,
                "post_collision_support_joint_sha256": post_support_digest,
                "post_collision_taint_joint_sha256": post_taint_digest,
                "post_stream_support_joint_sha256": adjacency_joint_state_digest(
                    support, next_basis
                ),
                "post_stream_taint_joint_sha256": adjacency_joint_state_digest(
                    taint, next_basis
                ),
            })
        rows.append(row_record)
        basis = next_basis
    route_a_masks = tuple(route_a)
    route_b_masks = tuple(route_b)
    return {
        "route_A_masks": route_a_masks,
        "route_B_masks": route_b_masks,
        "metadata": {
            "geometry": geometry.name,
            "probe_coin_identity": probe_coin_identity,
            "mediator_stream_enabled": mediator_stream_enabled,
            "representation": "exact-factorized-symmetric-Boolean-joint-adjacency",
            "rows": rows,
            "route_A_bond_counts": [int(np.count_nonzero(mask)) for mask in route_a_masks],
            "route_B_bond_counts": [int(np.count_nonzero(mask)) for mask in route_b_masks],
            "route_A_mask_sha256": mask_digest(route_a_masks),
            "route_B_mask_sha256": mask_digest(route_b_masks),
            "amplitudes_or_responses_used": False,
            "symmetric_zero_diagonal_and_taint_subset_support": True,
        },
    }


def mask_certificate_class(deletion: str) -> str:
    if deletion in ("emitter", "collision"):
        return "terminal-zero-" + deletion
    if deletion == "probe-coin":
        return "identity-coin"
    if deletion == "mediator-stream":
        return "parked-mediator"
    return "intact"


def build_exact_mask_library(manifest: tuple[dict, ...]) -> dict:
    """Build each exact geometry/deletion-class certificate once in the parent."""
    geometries = {}
    required = set()
    for row in manifest:
        geometry = geometry_from_row(row)
        geometries[geometry.name] = geometry
        certificate_class = mask_certificate_class(row["deletion"])
        if not certificate_class.startswith("terminal-zero"):
            required.add((geometry.name, certificate_class))
    certificates = {}
    for geometry_name, certificate_class in sorted(required):
        geometry = geometries[geometry_name]
        certificates[(geometry_name, certificate_class)] = (
            exact_factorized_boolean_certificate(
                geometry,
                probe_coin_identity=certificate_class == "identity-coin",
                mediator_stream_enabled=certificate_class != "parked-mediator",
            )
        )
    summary = {
        geometry_name + "::" + certificate_class: certificate["metadata"]
        for (geometry_name, certificate_class), certificate in certificates.items()
    }
    for key, (expected_a, expected_b) in EXPECTED_EXACT_MASK_DIGESTS.items():
        if key not in certificates:
            continue
        metadata = certificates[key]["metadata"]
        if (
            metadata["route_A_mask_sha256"] != expected_a
            or metadata["route_B_mask_sha256"] != expected_b
        ):
            raise RuntimeError("frozen exact Boolean mask digest drift: " + repr(key))
    summary["certificate_bundle_sha256"] = object_digest(summary)
    if summary["certificate_bundle_sha256"] != EXPECTED_EXACT_MASK_BUNDLE_SHA256:
        raise RuntimeError("frozen exact Boolean certificate bundle digest drift")
    return {"certificates": certificates, "summary": summary}


def route_structural_masks(
    geometry: engine.CarriedGeometry, route: str, deletion: str,
    mask_library: dict,
) -> tuple[tuple[np.ndarray, ...], dict]:
    """Return the exact preregistered route/surface/deletion mask certificate."""
    if route not in (ROUTE_A, ROUTE_B):
        raise ValueError("mask route is not A/B")
    surface = (
        contract.ROUTE_A_SAMPLE_SURFACE if route == ROUTE_A
        else contract.ROUTE_B_SAMPLE_SURFACE
    )
    certificate_class = mask_certificate_class(deletion)
    if certificate_class.startswith("terminal-zero"):
        zero = tuple(
            np.zeros((geometry.side, geometry.side, geometry.side, 3), dtype=bool)
            for _ in range(geometry.depth)
        )
        return zero, {
            "kind": "exact-terminal-null", "surface": surface,
            "deletion": deletion,
            "proof": (
                "emitter deletion creates no active mediator"
                if deletion == "emitter"
                else "collision deletion makes the only CAR/mediator coupling identity"
            ),
        }
    key = (geometry.name, certificate_class)
    if key not in mask_library["certificates"]:
        raise RuntimeError("exact Boolean mask certificate absent: " + repr(key))
    certificate = mask_library["certificates"][key]
    masks = certificate[
        "route_A_masks" if route == ROUTE_A else "route_B_masks"
    ]
    return masks, {
        "kind": "exact-factorized-Boolean-joint-transported-under-proper-cubic",
        "surface": surface, "deletion": deletion,
        "certificate_class": certificate_class,
        "base_geometry": geometry.name,
        "base_mask_sha256": (
            certificate["metadata"]["route_A_mask_sha256"]
            if route == ROUTE_A else
            certificate["metadata"]["route_B_mask_sha256"]
        ),
        "factorized_joint_certificate_bundle_sha256": (
            mask_library["summary"]["certificate_bundle_sha256"]
        ),
        "amplitude_or_response_used": False,
    }


def carry_mask(mask: np.ndarray, frame: np.ndarray) -> np.ndarray:
    side = mask.shape[0]
    output = np.zeros_like(mask)
    for cell_axis in np.argwhere(mask):
        cell = tuple(int(x) for x in cell_axis[:3])
        axis = int(cell_axis[3])
        positive = 2 * axis
        moved_vector = frame @ contract.c210.DIRECTIONS[positive]
        moved_direction = int(np.where(np.all(contract.c210.DIRECTIONS == moved_vector, axis=1))[0][0])
        target_axis = moved_direction // 2
        if moved_direction % 2 == 0:
            target_cell = contract.frame_cell(cell, frame, side)
        else:
            predecessor = tuple(int(x) for x in (
                (np.asarray(cell) - contract.c210.DIRECTIONS[positive]) % side
            ))
            target_cell = contract.frame_cell(predecessor, frame, side)
        output[target_cell + (target_axis,)] = True
    return output


def mask_covariance_residual(
    base_masks: tuple[np.ndarray, ...], frame: np.ndarray,
    carried_masks: tuple[np.ndarray, ...],
) -> tuple[int, tuple[np.ndarray, ...]]:
    mismatch = 0
    for base, observed in zip(base_masks, carried_masks):
        mismatch += int(np.count_nonzero(carry_mask(base, frame) != observed))
    return mismatch, carried_masks


def linear_morphology(samples_3_to_5: tuple[float, float, float], numeric_residuals: tuple[float, ...]) -> dict:
    """Frozen linear signed classifier; update 2 is intentionally absent."""
    values = np.asarray(samples_3_to_5, dtype=float)
    floor = max(contract.SIGNAL_ABSOLUTE_FLOOR, contract.NUMERIC_SIGNAL_MULTIPLIER * max(numeric_residuals, default=0.0))
    peak = float(np.max(abs(values)))
    active = abs(values) >= floor
    same_sign = bool(np.all(active) and (np.all(values > 0.0) or np.all(values < 0.0)))
    tail_ratio = float(np.mean(abs(values[-2:])) / peak) if peak else 0.0
    tail_coherence = float(abs(np.sum(values[-2:])) / np.sum(abs(values[-2:]))) if np.sum(abs(values[-2:])) else 0.0
    sustained = peak >= floor and same_sign and tail_ratio >= 0.50 and tail_coherence >= 0.90
    peak_index = int(np.argmax(abs(values)))
    cumulative_scale = float(max(np.max(abs(np.cumsum(values))), floor))
    impulse = (
        peak >= floor and not sustained and peak_index == 0
        and abs(values[-1]) / peak <= 0.10
        and abs(values[-1]) / cumulative_scale <= 0.10
    )
    classification = "sustained" if sustained else "impulse" if impulse else "transient-unresolved" if peak >= floor else "null"
    return {
        "classification": classification, "floor": floor, "peak": peak,
        "tail_signed_coherence": tail_coherence,
        "samples_used": (3, 4, 5),
    }


@dataclass(frozen=True)
class RowDynamics:
    emitter_angle: float
    collision_angle: float
    contact_coupling: float
    mediator_stream_enabled: bool
    probe_coin_deleted: bool


@dataclass
class Trajectory:
    final: engine.Blocks
    post_car_occupations: list[np.ndarray]
    post_word_occupations: list[np.ndarray]
    post_word_characters: list[tuple[complex, complex, complex]]
    active_mediator_weights: list[float]
    maximum_mediator_displacement: float
    controls: engine.TechnicalControls


def build_identity_coin_operations(
    rows: tuple[engine.SupportSlice, ...],
) -> tuple[engine.CarStepOperators, ...]:
    operations = []
    for previous_row, following_row in zip(rows[:-1], rows[1:]):
        previous = previous_row.basis
        following = following_row.basis
        middle = engine.coin_basis(previous)
        middle_index = {mode: index for index, mode in enumerate(middle)}
        following_index = {mode: index for index, mode in enumerate(following)}
        coin_rows = [middle_index[mode] for mode in previous]
        coin = sparse.coo_matrix(
            (np.ones(len(previous), dtype=complex), (coin_rows, np.arange(len(previous)))),
            shape=(len(middle), len(previous)),
        ).tocsr()
        stream_rows = []
        for cell, direction in middle:
            target = (
                tuple(int(x) for x in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                )), direction,
            )
            if target not in following_index:
                raise RuntimeError("identity-coin stream escaped frozen support")
            stream_rows.append(following_index[target])
        stream = sparse.coo_matrix(
            (np.ones(len(middle), dtype=complex), (stream_rows, np.arange(len(middle)))),
            shape=(len(following), len(middle)),
        ).tocsr()
        residual = float(sparse.linalg.norm(coin.conj().T @ coin - sparse.eye(len(previous))))
        residual = max(
            residual,
            float(sparse.linalg.norm(stream.conj().T @ stream - sparse.eye(len(middle)))),
        )
        operations.append(engine.CarStepOperators(
            coin_basis=middle, coin=coin, stream=stream,
            reference_residual=0.0, isometry_residual=residual,
        ))
    return tuple(operations)


def build_row_operations(
    rows: tuple[engine.SupportSlice, ...], probe_beta: float,
    probe_coin_deleted: bool,
) -> tuple[engine.CarStepOperators, ...]:
    return (
        build_identity_coin_operations(rows)
        if probe_coin_deleted else engine.build_operations(rows, probe_beta)
    )


def translation_characters(
    blocks: engine.Blocks, basis: tuple[engine.Mode, ...], side: int,
) -> tuple[complex, complex, complex]:
    """Normalized one-particle translation characters on all lab axes."""
    index = {mode: position for position, mode in enumerate(basis)}
    gamma = np.zeros((len(basis), len(basis)), dtype=complex)
    for block in blocks.values():
        gamma += block @ block.conj().T
    characters = []
    for axis in range(3):
        value = 0.0j
        offset = np.eye(3, dtype=int)[axis]
        for column, (cell, direction) in enumerate(basis):
            target_cell = tuple(int(x) for x in ((np.asarray(cell) + offset) % side))
            target = (target_cell, direction)
            if target in index:
                value += gamma[column, index[target]]
        characters.append(complex(value / 2.0))
    del gamma
    return tuple(characters)  # type: ignore[return-value]


def active_mediator_weight(blocks: engine.Blocks) -> float:
    return float(sum(
        np.vdot(block, block).real / 2.0
        for key, block in blocks.items() if key is not None
    ))


def mediator_displacement(
    blocks: engine.Blocks, geometry: engine.CarriedGeometry,
) -> float:
    result = 0.0
    for key, block in blocks.items():
        if key is None or np.linalg.norm(block) <= engine.BLOCK_PRUNE_FROBENIUS:
            continue
        cell, _direction = key
        result = max(result, float(np.linalg.norm(
            np.asarray(cell, dtype=float) - np.asarray(geometry.source_cell, dtype=float)
        )))
    return result


def diagnostic_support(
    support: engine.SupportSlice, blocks: engine.Blocks,
    mediator_stream_enabled: bool,
) -> engine.SupportSlice:
    if mediator_stream_enabled:
        return support
    # The deletion parks keys at their pre-stream cells.  The explicit key set
    # is still lawfully generated by the same local emitter/collision word; it
    # is not the intact streamed support declaration.
    return replace(support, mediator_keys=tuple(sorted(set(blocks), key=repr)))


def forward_step(
    blocks: engine.Blocks, operation: engine.CarStepOperators,
    support: engine.SupportSlice, geometry: engine.CarriedGeometry,
    dynamics: RowDynamics, band_projector: np.ndarray | None,
) -> tuple[engine.Blocks, np.ndarray, engine.TechnicalControls]:
    emitted = engine.emitter(blocks, dynamics.emitter_angle, geometry)
    pre_stream_blocks = engine.apply_car_map(emitted, operation.coin)
    pre_stream_occupation = engine.occupation_cube(
        pre_stream_blocks, operation.coin_basis, geometry.side
    )
    post_car_blocks = engine.apply_car_map(pre_stream_blocks, operation.stream)
    post_car_occupation = engine.occupation_cube(
        post_car_blocks, support.basis, geometry.side
    )
    continuity = engine.post_stream_continuity_residual(
        pre_stream_occupation, post_car_occupation
    )
    output = engine.copy_blocks(post_car_blocks)
    engine.apply_contact(output, support.basis, dynamics.contact_coupling)
    output = engine.collision(output, support.basis, dynamics.collision_angle)
    if dynamics.mediator_stream_enabled:
        output = engine.mediator_stream(output)
    effective_support = diagnostic_support(
        support, output, dynamics.mediator_stream_enabled
    )
    diagnostic = engine.technical_diagnostics(
        output, effective_support, geometry, band_projector
    )
    controls = engine.TechnicalControls(
        maximum_post_stream_continuity_residual=continuity,
        maximum_car_kernel_residual=max(
            operation.reference_residual, operation.isometry_residual
        ),
    )
    engine.absorb_diagnostic(controls, diagnostic)
    return output, post_car_occupation, controls


def run_forward(
    initial: engine.Blocks, rows: tuple[engine.SupportSlice, ...],
    operations: tuple[engine.CarStepOperators, ...],
    geometry: engine.CarriedGeometry, dynamics: RowDynamics,
    spectral_projectors: tuple[np.ndarray | None, ...], ledger: Ledger,
    kind: str, retain_observables: bool,
) -> Trajectory:
    field = {
        "canonical-interacting": "canonical_interacting_forward_trajectories",
        "canonical-matched-free": "canonical_matched_free_forward_trajectories",
        "canonical-repeated-free": "canonical_repeated_free_forward_trajectories",
        "carried-interacting": "carried_interacting_forward_trajectories",
        "carried-matched-free": "carried_matched_free_forward_trajectories",
    }.get(kind)
    if field is None:
        raise ValueError("unfrozen trajectory kind")
    setattr(ledger, field, getattr(ledger, field) + 1)
    ledger.forward_trajectories += 1
    ledger.trajectory_calls += 1
    blocks = engine.copy_blocks(initial)
    controls = engine.TechnicalControls()
    occupations: list[np.ndarray] = []
    post_word_occupations: list[np.ndarray] = []
    characters: list[tuple[complex, complex, complex]] = []
    active_weights: list[float] = []
    maximum_displacement = 0.0
    for update, operation in enumerate(operations, start=1):
        next_blocks, occupation, step_controls = forward_step(
            blocks, operation, rows[update], geometry, dynamics,
            spectral_projectors[update],
        )
        blocks.clear()
        blocks = next_blocks
        controls.absorb(step_controls)
        ledger.forward_update_calls += 1
        ledger.post_car_technical_captures += 1
        ledger.post_word_technical_captures += 1
        active_weights.append(active_mediator_weight(blocks))
        maximum_displacement = max(
            maximum_displacement, mediator_displacement(blocks, geometry)
        )
        if retain_observables:
            occupations.append(occupation)
            post_word_occupations.append(engine.occupation_cube(
                blocks, rows[update].basis, geometry.side
            ))
            characters.append(translation_characters(
                blocks, rows[update].basis, geometry.side
            ))
    return Trajectory(
        final=blocks, post_car_occupations=occupations,
        post_word_occupations=post_word_occupations,
        post_word_characters=characters,
        active_mediator_weights=active_weights,
        maximum_mediator_displacement=maximum_displacement,
        controls=controls,
    )


def run_inverse(
    final: engine.Blocks, initial: engine.Blocks,
    rows: tuple[engine.SupportSlice, ...],
    operations: tuple[engine.CarStepOperators, ...],
    geometry: engine.CarriedGeometry, dynamics: RowDynamics, ledger: Ledger,
) -> float:
    ledger.inverse_trajectories += 1
    ledger.trajectory_calls += 1
    blocks = engine.copy_blocks(final)
    for update in reversed(range(1, len(rows))):
        output = (
            engine.mediator_stream(blocks, inverse=True)
            if dynamics.mediator_stream_enabled else engine.copy_blocks(blocks)
        )
        output = engine.collision(
            output, rows[update].basis, -dynamics.collision_angle
        )
        engine.apply_contact(
            output, rows[update].basis, -dynamics.contact_coupling
        )
        output = engine.apply_car_map(
            output, operations[update - 1].stream, inverse=True
        )
        output = engine.apply_car_map(
            output, operations[update - 1].coin, inverse=True
        )
        output = engine.emitter(output, -dynamics.emitter_angle, geometry)
        blocks.clear()
        blocks = output
        ledger.inverse_update_calls += 1
    residual = engine.state_residual(blocks, initial)
    blocks.clear()
    return residual


def controls_dict(controls: engine.TechnicalControls) -> dict:
    return {
        key: float(value) for key, value in asdict(controls).items()
    }


def numeric_residual_tuple(
    controls: engine.TechnicalControls, inverse_residual: float,
    repeat_residual: float, covariance_residual: float,
) -> tuple[float, ...]:
    return (
        controls.maximum_norm_residual,
        controls.maximum_car_number_residual,
        controls.maximum_mediator_charge_residual,
        controls.maximum_lawfulness_residual,
        controls.maximum_post_stream_continuity_residual,
        controls.maximum_car_kernel_residual,
        inverse_residual, repeat_residual, covariance_residual,
    )


def technical_pass(
    controls: engine.TechnicalControls, inverse_residual: float,
    repeat_residual: float, covariance_residual: float,
    mask_mismatch: int, mass_residual: float,
) -> bool:
    return (
        controls.maximum_norm_residual <= NUMERIC_GATE
        and controls.maximum_car_number_residual <= NUMERIC_GATE
        and controls.maximum_mediator_charge_residual <= NUMERIC_GATE
        and controls.maximum_lawfulness_residual <= NUMERIC_GATE
        and controls.maximum_boundary_shell_weight <= BOUNDARY_GATE
        and controls.maximum_post_stream_continuity_residual <= CONTINUITY_GATE
        and controls.minimum_dynamic_band_fraction >= contract.BAND_FLOOR
        and controls.maximum_dynamic_axial_seam_weight <= contract.AXIAL_SEAM_CEILING
        and controls.maximum_dynamic_contact_weight >= contract.CONTACT_FLOOR
        and controls.maximum_car_kernel_residual <= NUMERIC_GATE
        and inverse_residual <= NUMERIC_GATE
        and repeat_residual <= NUMERIC_GATE
        and covariance_residual <= NUMERIC_GATE
        and mask_mismatch == 0
        and mass_residual <= NUMERIC_GATE
    )


def complex_json(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def row_dynamics(row: dict) -> tuple[RowDynamics, RowDynamics, float]:
    source_beta = BETA_VALUES[row["source_beta"]]
    probe_beta = BETA_VALUES[row["probe_beta"]]
    source_species = contract.c219.common_species(source_beta)
    probe_species = contract.c219.common_species(probe_beta)
    source_mass = float(source_species.analytic_mass)
    probe_mass = float(probe_species.analytic_mass)
    mass_residual = max(
        abs(contract.c219.rest_mass(source_species) - source_mass),
        abs(contract.c219.rest_mass(probe_species) - probe_mass),
    )
    source_factor = 1.0 if row["deletion"] == "source-mass-factor" else source_mass
    probe_factor = 1.0 if row["deletion"] == "probe-mass-factor" else probe_mass
    emitter_angle = contract.EMITTER_COUPLING * source_factor
    collision_angle = contract.SCATTERING_COUPLING * probe_factor
    if row["deletion"] == "emitter":
        emitter_angle = 0.0
    if row["deletion"] == "collision":
        collision_angle = 0.0
    common = {
        "contact_coupling": 0.0 if row["deletion"] == "contact" else contract.CONTACT_COUPLING,
        "mediator_stream_enabled": row["deletion"] != "mediator-stream",
        "probe_coin_deleted": row["deletion"] == "probe-coin",
    }
    interacting = RowDynamics(
        emitter_angle=float(emitter_angle),
        collision_angle=float(collision_angle), **common,
    )
    matched_free = RowDynamics(
        emitter_angle=0.0, collision_angle=0.0, **common,
    )
    return interacting, matched_free, float(mass_residual)


def route_a_observable(
    row: dict, geometry: engine.CarriedGeometry,
    interacting: Trajectory, free: Trajectory,
    masks: tuple[np.ndarray, ...], numeric_residuals: tuple[float, ...],
) -> dict:
    local_fields = []
    plane_fields = []
    retained_masks = []
    front_lab = []
    fixed_lab = []
    leakage = 0.0
    row_geometry = row["geometry"]
    causal_axis = int(row_geometry["causal_axis"])
    orientation = int(contract.c210.DIRECTIONS[geometry.outgoing_direction][causal_axis])
    for sample_index, update in enumerate(RESPONSE_WINDOW):
        delta_occupation = (
            interacting.post_car_occupations[update - 1]
            - free.post_car_occupations[update - 1]
        )
        local = contract.local_bond_field(delta_occupation)
        plane = contract.plane_bond_field(delta_occupation)
        mask = masks[update - 1]
        outside = abs(local[~mask])
        leakage = max(leakage, float(np.max(outside)) if outside.size else 0.0)
        cut = int(row_geometry["front_anchor_cuts"][sample_index])
        front_lab.append(float(plane[causal_axis, cut]))
        fixed_lab.append(float(plane[causal_axis, int(row_geometry["fixed_probe_cut"])]))
        local_fields.append(np.moveaxis(local, -1, 0))
        plane_fields.append(plane)
        retained_masks.append(np.moveaxis(mask, -1, 0))
    front_carried = [orientation * value for value in front_lab]
    fixed_carried = [orientation * value for value in fixed_lab]
    floor = max(
        contract.SIGNAL_ABSOLUTE_FLOOR,
        contract.NUMERIC_SIGNAL_MULTIPLIER * max(numeric_residuals, default=0.0),
    )
    update2_null = abs(front_carried[0]) < floor and abs(fixed_carried[0]) < floor
    morphology = linear_morphology(tuple(front_carried[1:]), numeric_residuals)
    fixed_arrival = abs(fixed_carried[-1]) >= floor
    tail_sign_consistent = bool(
        fixed_arrival and abs(front_carried[-1]) >= floor
        and fixed_carried[-1] * front_carried[-1] > 0.0
    )
    return {
        "full_local_field_delta": np.stack(local_fields).astype("<f8", copy=False),
        "full_plane_field_delta": np.stack(plane_fields).astype("<f8", copy=False),
        "full_structural_masks": np.stack(retained_masks).astype(bool, copy=False),
        "front_trace_lab": front_lab,
        "front_trace_carried": front_carried,
        "fixed_trace_lab": fixed_lab,
        "fixed_trace_carried": fixed_carried,
        "update2_null": {"pass": update2_null, "floor": floor},
        "morphology_updates3_to5": morphology,
        "fixed_arrival_update5": fixed_arrival,
        "tail_sign_consistent": tail_sign_consistent,
        "primary_response_gate": bool(
            update2_null and morphology["classification"] == "sustained"
            and fixed_arrival and tail_sign_consistent
        ),
        "response_statistic": contract.route_a_response_statistic(tuple(front_carried)),
        "structural_cone_leakage": leakage,
    }


def route_b_observable(
    row: dict, interacting: Trajectory, free: Trajectory,
    repeated_free: Trajectory, masks: tuple[np.ndarray, ...],
    numeric_residuals: tuple[float, ...],
) -> dict:
    interacting_rows = interacting.post_word_characters[1:]
    free_rows = free.post_word_characters[1:]
    repeated_rows = repeated_free.post_word_characters[1:]
    phasors = []
    valid = True
    for left, right in zip(interacting_rows, free_rows):
        axes = []
        for z_int, z_free in zip(left, right):
            if min(abs(z_int), abs(z_free)) < CHARACTER_FLOOR:
                valid = False
                axes.append(1.0 + 0.0j)
            else:
                axes.append((z_int / abs(z_int)) * np.conj(z_free / abs(z_free)))
        phasors.append(tuple(axes))
    primary_axis = int(row["geometry"]["causal_axis"])
    primary = tuple(values[primary_axis] for values in phasors)
    morphology = (
        contract.circular_phase_morphology(primary, numeric_residuals)
        if valid else {"classification": "invalid-character-floor"}
    )
    response_floor = max(
        contract.SIGNAL_ABSOLUTE_FLOOR,
        contract.NUMERIC_SIGNAL_MULTIPLIER * max(
            numeric_residuals, default=0.0
        ),
    )
    structural_leakage = 0.0
    for update in RESPONSE_WINDOW:
        delta = (
            interacting.post_word_occupations[update - 1]
            - free.post_word_occupations[update - 1]
        )
        local = contract.local_bond_field(delta)
        outside = abs(local[~masks[update - 1]])
        structural_leakage = max(
            structural_leakage,
            float(np.max(outside)) if outside.size else 0.0,
        )
    return {
        "interacting_characters_all_axes": [
            [complex_json(value) for value in row_values] for row_values in interacting_rows
        ],
        "free_characters_all_axes": [
            [complex_json(value) for value in row_values] for row_values in free_rows
        ],
        "repeated_free_characters_all_axes": [
            [complex_json(value) for value in row_values]
            for row_values in repeated_rows
        ],
        "character_magnitudes_all_branches": {
            "interacting": [[float(abs(value)) for value in values] for values in interacting_rows],
            "matched_free": [[float(abs(value)) for value in values] for values in free_rows],
            "repeated_free": [[float(abs(value)) for value in values] for values in repeated_rows],
        },
        "response_phasors_all_axes": [
            [complex_json(value) for value in row_values] for row_values in phasors
        ],
        "principal_angles_diagnostic_only": [
            [float(np.angle(value)) for value in row_values] for row_values in phasors
        ],
        "primary_response_phasors": [complex_json(value) for value in primary],
        "character_floor_valid": valid,
        "response_floor": response_floor,
        "post_word_structural_cone_leakage": structural_leakage,
        "circular_morphology": morphology,
        "response_statistic": (
            contract.route_b_response_statistic(primary) if valid else None
        ),
    }


def carry_local_bond_field(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    side = field.shape[0]
    output = np.zeros_like(field)
    for axis in range(3):
        moved = frame @ np.eye(3, dtype=int)[axis]
        target_axis = int(np.argmax(abs(moved)))
        sign = int(moved[target_axis])
        for cell in np.ndindex((side, side, side)):
            if sign > 0:
                target_cell = contract.frame_cell(cell, frame, side)
            else:
                predecessor = tuple(int(value) for value in (
                    (np.asarray(cell) - np.eye(3, dtype=int)[axis]) % side
                ))
                target_cell = contract.frame_cell(predecessor, frame, side)
            output[target_cell + (target_axis,)] = sign * field[cell + (axis,)]
    return output


def route_a_carried_response_residual(
    row: dict, base_interacting: Trajectory, base_free: Trajectory,
    carried_interacting: Trajectory, carried_free: Trajectory,
    frame: np.ndarray,
) -> dict:
    maximum_raw_interacting = 0.0
    maximum_raw_free = 0.0
    maximum_delta = 0.0
    maximum_plane = 0.0
    maximum_raw_interacting_front_fixed = 0.0
    maximum_raw_free_front_fixed = 0.0
    maximum_front = 0.0
    maximum_fixed = 0.0
    source_center = tuple(row["geometry"]["source_cell"])
    source_axis = int(row["geometry"]["causal_axis"])
    for sample_index, update in enumerate(RESPONSE_WINDOW):
        base_int = contract.local_bond_field(
            base_interacting.post_car_occupations[update - 1]
        )
        base_free_field = contract.local_bond_field(
            base_free.post_car_occupations[update - 1]
        )
        carried_int = contract.local_bond_field(
            carried_interacting.post_car_occupations[update - 1]
        )
        carried_free_field = contract.local_bond_field(
            carried_free.post_car_occupations[update - 1]
        )
        expected_int = carry_local_bond_field(base_int, frame)
        expected_free = carry_local_bond_field(base_free_field, frame)
        expected_delta = expected_int - expected_free
        observed_delta = carried_int - carried_free_field
        maximum_raw_interacting = max(
            maximum_raw_interacting,
            float(np.max(abs(carried_int - expected_int))),
        )
        maximum_raw_free = max(
            maximum_raw_free,
            float(np.max(abs(carried_free_field - expected_free))),
        )
        maximum_delta = max(
            maximum_delta, float(np.max(abs(observed_delta - expected_delta)))
        )
        expected_plane = np.stack([
            np.sum(expected_delta[..., axis], axis=tuple(
                candidate for candidate in range(3) if candidate != axis
            )) for axis in range(3)
        ])
        observed_plane = np.stack([
            np.sum(observed_delta[..., axis], axis=tuple(
                candidate for candidate in range(3) if candidate != axis
            )) for axis in range(3)
        ])
        maximum_plane = max(
            maximum_plane, float(np.max(abs(observed_plane - expected_plane)))
        )
        front_cut = int(row["geometry"]["front_anchor_cuts"][sample_index])
        front_axis, front_sign, target_front = contract.carried_bond_cut(
            front_cut, source_center, source_axis, frame
        )
        fixed_axis, fixed_sign, target_fixed = contract.carried_bond_cut(
            int(row["geometry"]["fixed_probe_cut"]), source_center,
            source_axis, frame,
        )
        base_plane = contract.plane_bond_field(
            base_interacting.post_car_occupations[update - 1]
            - base_free.post_car_occupations[update - 1]
        )
        base_int_plane = contract.plane_bond_field(
            base_interacting.post_car_occupations[update - 1]
        )
        base_free_plane = contract.plane_bond_field(
            base_free.post_car_occupations[update - 1]
        )
        carried_int_plane = contract.plane_bond_field(
            carried_interacting.post_car_occupations[update - 1]
        )
        carried_free_plane = contract.plane_bond_field(
            carried_free.post_car_occupations[update - 1]
        )
        for target_axis, sign, target_cut, source_cut in (
            (front_axis, front_sign, target_front, front_cut),
            (
                fixed_axis, fixed_sign, target_fixed,
                int(row["geometry"]["fixed_probe_cut"]),
            ),
        ):
            maximum_raw_interacting_front_fixed = max(
                maximum_raw_interacting_front_fixed,
                abs(
                    carried_int_plane[target_axis, target_cut]
                    - sign * base_int_plane[source_axis, source_cut]
                ),
            )
            maximum_raw_free_front_fixed = max(
                maximum_raw_free_front_fixed,
                abs(
                    carried_free_plane[target_axis, target_cut]
                    - sign * base_free_plane[source_axis, source_cut]
                ),
            )
        maximum_front = max(
            maximum_front,
            abs(
                observed_plane[front_axis, target_front]
                - front_sign * base_plane[source_axis, front_cut]
            ),
        )
        maximum_fixed = max(
            maximum_fixed,
            abs(
                observed_plane[fixed_axis, target_fixed]
                - fixed_sign * base_plane[
                    source_axis, int(row["geometry"]["fixed_probe_cut"])
                ]
            ),
        )
    return {
        "raw_interacting_full_field": maximum_raw_interacting,
        "raw_free_full_field": maximum_raw_free,
        "delta_full_field": maximum_delta,
        "delta_plane_field": maximum_plane,
        "raw_interacting_front_fixed": float(
            maximum_raw_interacting_front_fixed
        ),
        "raw_free_front_fixed": float(maximum_raw_free_front_fixed),
        "front_anchor": float(maximum_front),
        "fixed_anchor": float(maximum_fixed),
        "maximum": float(max(
            maximum_raw_interacting, maximum_raw_free, maximum_delta,
            maximum_plane, maximum_raw_interacting_front_fixed,
            maximum_raw_free_front_fixed, maximum_front, maximum_fixed,
        )),
    }


def character_response_phasors(
    interacting: list[tuple[complex, complex, complex]],
    free: list[tuple[complex, complex, complex]],
) -> tuple[np.ndarray, bool]:
    output = np.ones((len(interacting), 3), dtype=complex)
    valid = True
    for update, (left, right) in enumerate(zip(interacting, free)):
        for axis, (z_int, z_free) in enumerate(zip(left, right)):
            if min(abs(z_int), abs(z_free)) < CHARACTER_FLOOR:
                valid = False
            else:
                output[update, axis] = (
                    z_int / abs(z_int) * np.conj(z_free / abs(z_free))
                )
    return output, valid


def route_b_carried_response_residual(
    base_interacting: Trajectory, base_free: Trajectory,
    carried_interacting: Trajectory, carried_free: Trajectory,
    frame: np.ndarray,
) -> dict:
    base_int = base_interacting.post_word_characters[1:]
    base_matched = base_free.post_word_characters[1:]
    carried_int = carried_interacting.post_word_characters[1:]
    carried_matched = carried_free.post_word_characters[1:]
    base_phasors, base_valid = character_response_phasors(
        base_int, base_matched
    )
    carried_phasors, carried_valid = character_response_phasors(
        carried_int, carried_matched
    )
    maximum_int = 0.0
    maximum_free = 0.0
    maximum_phasor = 0.0
    for axis in range(3):
        moved = frame @ np.eye(3, dtype=int)[axis]
        target_axis = int(np.argmax(abs(moved)))
        sign = int(moved[target_axis])
        for update in range(len(RESPONSE_WINDOW)):
            expected_int = (
                base_int[update][axis] if sign > 0
                else np.conj(base_int[update][axis])
            )
            expected_free = (
                base_matched[update][axis] if sign > 0
                else np.conj(base_matched[update][axis])
            )
            expected_phasor = (
                base_phasors[update, axis] if sign > 0
                else np.conj(base_phasors[update, axis])
            )
            maximum_int = max(
                maximum_int,
                abs(carried_int[update][target_axis] - expected_int),
            )
            maximum_free = max(
                maximum_free,
                abs(carried_matched[update][target_axis] - expected_free),
            )
            maximum_phasor = max(
                maximum_phasor,
                abs(carried_phasors[update, target_axis] - expected_phasor),
            )
    valid = base_valid and carried_valid
    return {
        "raw_interacting_character": float(maximum_int),
        "raw_free_character": float(maximum_free),
        "response_phasor_chord": float(maximum_phasor),
        "character_floor_valid": valid,
        "maximum": float(max(maximum_int, maximum_free, maximum_phasor))
        if valid else 1.0,
    }


def all24_state_mask_response_covariance(
    row: dict, base_interacting: Trajectory, base_free: Trajectory,
    base_rows: tuple[engine.SupportSlice, ...],
    base_masks: tuple[np.ndarray, ...], base_geometry: engine.CarriedGeometry,
    probe_beta: float, interacting_dynamics: RowDynamics,
    free_dynamics: RowDynamics, ledger: Ledger,
) -> tuple[
    float, float, int, list[dict], np.ndarray, engine.TechnicalControls
]:
    maximum_state = 0.0
    maximum_response = 0.0
    total_mask_mismatch = 0
    frames = []
    packed_carried_masks = []
    carried_controls = engine.TechnicalControls()
    for index, frame in enumerate(contract.c210.proper_cubic_frames()):
        carried_geometry = engine.carry_geometry(base_geometry, frame, index)
        carried_rows, first_overlap = engine.support_trace(carried_geometry)
        if first_overlap != 2:
            raise RuntimeError("carried first-overlap drift")
        carried_operations = build_row_operations(
            carried_rows, probe_beta, interacting_dynamics.probe_coin_deleted
        )
        carried_initial = engine.initial_blocks(
            carried_geometry, carried_rows[0].basis
        )
        carried = run_forward(
            carried_initial, carried_rows, carried_operations,
            carried_geometry, interacting_dynamics,
            tuple(None for _ in carried_rows), ledger,
            "carried-interacting", retain_observables=True,
        )
        carried_free = run_forward(
            carried_initial, carried_rows, carried_operations,
            carried_geometry, free_dynamics,
            tuple(None for _ in carried_rows), ledger,
            "carried-matched-free", retain_observables=True,
        )
        carried_controls.absorb(carried.controls)
        carried_controls.absorb(carried_free.controls)
        interacting_state_residual = engine.carried_state_residual(
            carried.final, base_interacting.final, base_rows[-1].basis,
            carried_rows[-1].basis, frame, base_geometry.side,
        )
        free_state_residual = engine.carried_state_residual(
            carried_free.final, base_free.final, base_rows[-1].basis,
            carried_rows[-1].basis, frame, base_geometry.side,
        )
        # The expensive exact joint recursion is executed once on each actual
        # base geometry/deletion class.  Proper-cubic frames then transport
        # that already certified Boolean object; an independent direct-joint
        # all-24 small oracle is part of the dry contract.
        carried_masks = tuple(carry_mask(mask, frame) for mask in base_masks)
        mask_mismatch, observed_masks = mask_covariance_residual(
            base_masks, frame, carried_masks
        )
        projected = np.stack([
            np.moveaxis(observed_masks[update - 1], -1, 0)
            for update in RESPONSE_WINDOW
        ]).astype(bool, copy=False)
        packed_carried_masks.append(np.packbits(projected.ravel(), bitorder="little"))
        response = (
            route_a_carried_response_residual(
                row, base_interacting, base_free, carried, carried_free, frame
            ) if row["route"] == ROUTE_A else
            route_b_carried_response_residual(
                base_interacting, base_free, carried, carried_free, frame
            )
        )
        maximum_state = max(
            maximum_state, interacting_state_residual, free_state_residual
        )
        maximum_response = max(maximum_response, response["maximum"])
        total_mask_mismatch += mask_mismatch
        frames.append({
            "frame_index": index,
            "frame_flat": [int(value) for value in frame.ravel()],
            "interacting_state_residual": interacting_state_residual,
            "matched_free_state_residual": free_state_residual,
            "elementwise_mask_mismatch_count": mask_mismatch,
            "mask_certificate": "transported-exact-base-certificate",
            "response_covariance": response,
        })
        carried.final.clear()
        carried_free.final.clear()
        carried_initial.clear()
    if len(frames) != 24:
        raise RuntimeError("literal all24 execution count drift")
    return (
        maximum_state, maximum_response, total_mask_mismatch, frames,
        np.stack(packed_carried_masks).astype(np.uint8, copy=False),
        carried_controls,
    )


def run_science_row(
    index: int, row: dict, ledger: Ledger, mask_library: dict,
) -> dict:
    started = time.monotonic()
    starting_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    geometry = geometry_from_row(row)
    rows, first_overlap = engine.support_trace(geometry)
    if first_overlap != 2 or len(rows) != DEPTH + 1:
        raise RuntimeError("science geometry causal-overlap drift")
    masks, mask_contract = route_structural_masks(
        geometry, row["route"], row["deletion"], mask_library
    )
    interacting_dynamics, free_dynamics, mass_residual = row_dynamics(row)
    probe_beta = BETA_VALUES[row["probe_beta"]]
    operations = build_row_operations(
        rows, probe_beta, interacting_dynamics.probe_coin_deleted
    )
    kernel = engine.selected_band_kernel(geometry.side, probe_beta)
    projectors: tuple[np.ndarray | None, ...] = (None,) + tuple(
        engine.selected_band_projector(kernel, support.basis, geometry.side)
        for support in rows[1:]
    )
    del kernel
    initial = engine.initial_blocks(geometry, rows[0].basis)
    interacting = run_forward(
        initial, rows, operations, geometry, interacting_dynamics,
        projectors, ledger, "canonical-interacting", retain_observables=True,
    )
    free = run_forward(
        initial, rows, operations, geometry, free_dynamics,
        projectors, ledger, "canonical-matched-free", retain_observables=True,
    )
    repeated_free = run_forward(
        initial, rows, operations, geometry, free_dynamics,
        projectors, ledger, "canonical-repeated-free",
        retain_observables=row["route"] == ROUTE_B,
    )
    repeat_residual = engine.state_residual(free.final, repeated_free.final)
    repeated_character_residual = (
        max(
            abs(left - right)
            for left_row, right_row in zip(
                free.post_word_characters, repeated_free.post_word_characters
            )
            for left, right in zip(left_row, right_row)
        ) if row["route"] == ROUTE_B else 0.0
    )
    inverse_residual = run_inverse(
        interacting.final, initial, rows, operations, geometry,
        interacting_dynamics, ledger,
    )
    controls = engine.TechnicalControls()
    controls.absorb(interacting.controls)
    controls.absorb(free.controls)
    controls.absorb(repeated_free.controls)
    covariance_residual, response_covariance_residual, mask_mismatch, frame_results, carried_mask_packbits, carried_controls = (
        all24_state_mask_response_covariance(
            row, interacting, free, rows, masks, geometry, probe_beta,
            interacting_dynamics, free_dynamics, ledger,
        )
    )
    controls.absorb(carried_controls)
    residuals = {
        "inverse": inverse_residual,
        "matched_free_repeat": repeat_residual,
        "matched_free_repeat_character": repeated_character_residual,
        "maximum_all24_full_state_covariance": covariance_residual,
        "maximum_all24_response_covariance": response_covariance_residual,
        "all24_elementwise_mask_mismatch_count": mask_mismatch,
        "mass_fixture": mass_residual,
        "source_ledger_update1": abs(
            interacting.active_mediator_weights[0]
            - np.sin(interacting_dynamics.emitter_angle) ** 2
        ),
    }
    causal_axis = int(row["geometry"]["causal_axis"])
    transverse_directions = tuple(
        direction for direction in range(6)
        if direction // 2 != causal_axis
    )
    maximum_transverse_car_weight = max(
        float(np.sum(occupation[..., transverse_directions]))
        for occupation in interacting.post_car_occupations
    )
    numeric_residuals = numeric_residual_tuple(
        controls, inverse_residual, repeat_residual, covariance_residual
    ) + (response_covariance_residual, repeated_character_residual)
    passed = technical_pass(
        controls, inverse_residual, repeat_residual, covariance_residual,
        mask_mismatch, mass_residual,
    ) and (
        residuals["source_ledger_update1"] <= contract.SOURCE_LEDGER_TOLERANCE
        and repeated_character_residual <= NUMERIC_GATE
        and response_covariance_residual <= NUMERIC_GATE
    )
    elapsed = time.monotonic() - started
    ending_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_scale = 1 if sys.platform == "darwin" else 1024
    maximum_rss = int(max(starting_rss, ending_rss) * rss_scale)
    passed = passed and elapsed < contract.ROW_WALL_CEILING_SECONDS and maximum_rss < contract.ROW_RSS_CEILING_BYTES
    common = {
        "row": row_identity(index, row),
        "technical": controls_dict(controls),
        "residuals": residuals,
        "full_state_covariance_all24": {
            "executed_frames": 24, "frames": frame_results,
            "maximum_residual": covariance_residual,
            "response_used_for_selection": False,
        },
        "full_response_covariance_all24": {
            "executed_frames": 24,
            "carried_interacting_trajectories": 24,
            "carried_matched_free_trajectories": 24,
            "maximum_residual": response_covariance_residual,
            "raw_interacting_raw_free_and_delta_compared": True,
            "response_used_for_selection": False,
        },
        "elementwise_mask_covariance_all24": {
            "executed_frames": 24,
            "total_mismatch_count": mask_mismatch,
            "representation": mask_contract["kind"],
            "mask_contract": mask_contract,
            "amplitude_or_response_used": False,
        },
        "source_ledger": {
            "active_mediator_weight_update1": interacting.active_mediator_weights[0],
            "expected_emitter_weight_update1": float(np.sin(interacting_dynamics.emitter_angle) ** 2),
            "update1_residual": abs(
                interacting.active_mediator_weights[0]
                - np.sin(interacting_dynamics.emitter_angle) ** 2
            ),
            "maximum_mediator_displacement": interacting.maximum_mediator_displacement,
            "maximum_transverse_CAR_weight": maximum_transverse_car_weight,
            "applied_source_factor": (
                1.0 if row["deletion"] == "source-mass-factor"
                else float(contract.c219.common_species(BETA_VALUES[row["source_beta"]]).analytic_mass)
            ),
            "applied_probe_factor": (
                1.0 if row["deletion"] == "probe-mass-factor"
                else float(contract.c219.common_species(BETA_VALUES[row["probe_beta"]]).analytic_mass)
            ),
            "executable_emitter_angle": interacting_dynamics.emitter_angle,
            "executable_collision_angle": interacting_dynamics.collision_angle,
            "executable_contact_coupling": interacting_dynamics.contact_coupling,
            "executable_probe_coin": (
                "identity" if interacting_dynamics.probe_coin_deleted
                else "Cycle219-common-family"
            ),
            "mediator_stream_enabled": interacting_dynamics.mediator_stream_enabled,
        },
        "deletion_audit": {"status": "pending-atomic-comparison"},
        "_artifact_arrays": {
            "canonical_mask_packbits": np.packbits(np.stack([
                np.moveaxis(masks[update - 1], -1, 0)
                for update in RESPONSE_WINDOW
            ]).ravel(), bitorder="little"),
            "carried_mask_packbits_all24": carried_mask_packbits,
            "mask_unpacked_shape": np.asarray((4, 3, 25, 25, 25), dtype=np.int64),
        },
        "resource": {
            "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
            "row_wall_ceiling_seconds": contract.ROW_WALL_CEILING_SECONDS,
            "row_RSS_ceiling_bytes": contract.ROW_RSS_CEILING_BYTES,
        },
        "row_pass": bool(passed),
    }
    if row["route"] == ROUTE_A:
        common["route_A"] = route_a_observable(
            row, geometry, interacting, free, masks, numeric_residuals
        )
        common["row_pass"] = bool(
            common["row_pass"]
            and common["route_A"]["structural_cone_leakage"]
            <= FIELD_ZERO_GATE
        )
    else:
        common["route_B"] = route_b_observable(
            row, interacting, free, repeated_free, masks, numeric_residuals
        )
        common["row_pass"] = bool(
            common["row_pass"]
            and common["route_B"]["post_word_structural_cone_leakage"]
            <= FIELD_ZERO_GATE
        )
    interacting.final.clear()
    free.final.clear()
    repeated_free.final.clear()
    initial.clear()
    ledger.science_train_rows += 1
    if row["route"] == ROUTE_A:
        ledger.route_A_rows += 1
    elif row["route"] == ROUTE_B:
        ledger.route_B_rows += 1
    else:
        raise RuntimeError("Route-C allocation attempted")
    return common


def fsync_file(path: Path) -> None:
    with path.open("rb") as stream:
        os.fsync(stream.fileno())


def fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_deterministic_npz(path: Path, arrays: Mapping[str, np.ndarray]) -> None:
    """Write a byte-deterministic compressed NumPy archive."""
    with path.open("wb") as raw:
        with zipfile.ZipFile(
            raw, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9,
        ) as archive:
            for name in sorted(arrays):
                buffer = io.BytesIO()
                np.lib.format.write_array(
                    buffer, np.asarray(arrays[name]), allow_pickle=False
                )
                info = zipfile.ZipInfo(
                    filename=name + ".npy", date_time=(1980, 1, 1, 0, 0, 0)
                )
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o600 << 16
                archive.writestr(
                    info, buffer.getvalue(),
                    compress_type=zipfile.ZIP_DEFLATED, compresslevel=9,
                )
        raw.flush()
        os.fsync(raw.fileno())


def logical_array_sha256(value: np.ndarray) -> str:
    array = np.ascontiguousarray(value)
    header = json_bytes({
        "dtype": array.dtype.str, "shape": list(array.shape),
        "order": "C",
    })
    return sha256(header + b"\0" + array.tobytes(order="C")).hexdigest()


def seal_row_artifact(
    index: int, result: dict, staging: Path, dependency_bundle: dict,
) -> dict:
    hidden = result.pop("_artifact_arrays")
    arrays: dict[str, np.ndarray] = {
        "canonical_mask_packbits": np.asarray(hidden["canonical_mask_packbits"], dtype=np.uint8),
        "carried_mask_packbits_all24": np.asarray(hidden["carried_mask_packbits_all24"], dtype=np.uint8),
        "mask_unpacked_shape": np.asarray(hidden["mask_unpacked_shape"], dtype=np.int64),
        "all24_state_residuals": np.asarray([
            max(
                frame["interacting_state_residual"],
                frame["matched_free_state_residual"],
            )
            for frame in result["full_state_covariance_all24"]["frames"]
        ], dtype="<f8"),
        "all24_response_residuals": np.asarray([
            frame["response_covariance"]["maximum"]
            for frame in result["full_state_covariance_all24"]["frames"]
        ], dtype="<f8"),
    }
    if "route_A" in result:
        route = result["route_A"]
        delta_j = np.asarray(route.pop("full_local_field_delta"), dtype="<f8")
        delta_J = np.asarray(route.pop("full_plane_field_delta"), dtype="<f8")
        masks = np.asarray(route.pop("full_structural_masks"), dtype=bool)
        if delta_j.shape != (4, 3, 25, 25, 25) or delta_J.shape != (4, 3, 25):
            raise RuntimeError("Route-A lossless field shape drift")
        if masks.shape != (4, 3, 25, 25, 25):
            raise RuntimeError("Route-A mask shape drift")
        if not np.array_equal(
            np.packbits(masks.ravel(), bitorder="little"),
            arrays["canonical_mask_packbits"],
        ):
            raise RuntimeError("Route-A retained mask/pack mismatch")
        arrays.update({
            "delta_j": delta_j, "delta_J": delta_J,
            "front_trace_lab": np.asarray(route["front_trace_lab"], dtype="<f8"),
            "front_trace_carried": np.asarray(route["front_trace_carried"], dtype="<f8"),
            "fixed_trace_lab": np.asarray(route["fixed_trace_lab"], dtype="<f8"),
            "fixed_trace_carried": np.asarray(route["fixed_trace_carried"], dtype="<f8"),
        })
    else:
        route = result["route_B"]
        interacting_values = route.pop("interacting_characters_all_axes")
        free_values = route.pop("free_characters_all_axes")
        repeated_values = route.pop("repeated_free_characters_all_axes")
        response_values = route.pop("response_phasors_all_axes")
        magnitude_values = route.pop("character_magnitudes_all_branches")
        principal_values = route.pop("principal_angles_diagnostic_only")
        arrays.update({
            "interacting_characters_all_axes": np.asarray([
                [decode_complex(value) for value in values]
                for values in interacting_values
            ], dtype="<c16"),
            "free_characters_all_axes": np.asarray([
                [decode_complex(value) for value in values]
                for values in free_values
            ], dtype="<c16"),
            "repeated_free_characters_all_axes": np.asarray([
                [decode_complex(value) for value in values]
                for values in repeated_values
            ], dtype="<c16"),
            "response_phasors_all_axes": np.asarray([
                [decode_complex(value) for value in values]
                for values in response_values
            ], dtype="<c16"),
            "principal_angles_diagnostic_only": np.asarray(
                principal_values, dtype="<f8"
            ),
            "interacting_character_magnitudes": np.asarray(
                magnitude_values["interacting"], dtype="<f8"
            ),
            "matched_free_character_magnitudes": np.asarray(
                magnitude_values["matched_free"], dtype="<f8"
            ),
            "repeated_free_character_magnitudes": np.asarray(
                magnitude_values["repeated_free"], dtype="<f8"
            ),
        })
    logical_hashes = {
        name: logical_array_sha256(value) for name, value in arrays.items()
    }
    geometry_contract = geometry_by_name(
        "train-mirrored" if "mirrored" in result["row"]["geometry"]
        else "train-canonical"
    )
    artifact_metadata = {
        "schema": "Cycle509-A/B-row-artifact-v2",
        "row_identity": result["row"],
        "updates": list(RESPONSE_WINDOW),
        "axis_order": ["x", "y", "z"],
        "lattice_coordinate_order": ["x", "y", "z"],
        "delta_j_coordinate_order": ["update", "axis", "x", "y", "z"],
        "delta_J_coordinate_order": ["update", "axis", "cut"],
        "causal_axis": int(geometry_contract.causal_axis),
        "source_cell": list(geometry_contract.source_cell),
        "probe_center": list(geometry_contract.probe_center),
        "front_anchor_cuts": list(geometry_contract.front_anchor_cuts),
        "front_anchor_pairs_update_cut": [
            [int(update), int(cut)] for update, cut in zip(
                RESPONSE_WINDOW, geometry_contract.front_anchor_cuts
            )
        ],
        "fixed_probe_cut": int(geometry_contract.fixed_probe_cut),
        "positive_bond_anchor_definition": (
            "j_a(r)=n_post(r,+a)-n_post(r-e_a,-a); cut c is bond (c-1,c)"
        ),
        "boundary": "periodic-torus-L25-with-zero-boundary-shell-gate",
        "mask_bitorder": "little",
        "mask_unpacked_shape": [4, 3, 25, 25, 25],
        "mask_kind": result["elementwise_mask_covariance_all24"]["mask_contract"]["kind"],
        "mask_surface": result["elementwise_mask_covariance_all24"]["mask_contract"]["surface"],
        "mask_deletion": result["row"]["deletion"],
        "response_floor": (
            float(result["route_B"]["response_floor"])
            if "route_B" in result else
            float(result["route_A"]["update2_null"]["floor"])
        ),
        "proper_cubic_frame_order": [
            [int(value) for value in frame.ravel()]
            for frame in contract.c210.proper_cubic_frames()
        ],
        "logical_raw_array_sha256": logical_hashes,
        "science_runner_sha256": dependency_bundle["science_runner"]["observed_sha256"],
        "dependency_bundle_sha256": dependency_bundle["bundle_sha256"],
        "qualified_resource_transcript_sha256": RESOURCE_TRANSCRIPT_SHA256,
    }
    arrays["artifact_metadata_utf8"] = np.frombuffer(
        json_bytes(artifact_metadata), dtype=np.uint8
    ).copy()
    expected_members = (
        ROUTE_A_ARTIFACT_MEMBERS if "route_A" in result
        else ROUTE_B_ARTIFACT_MEMBERS
    )
    if set(arrays) != expected_members:
        raise RuntimeError("row artifact member contract drift")
    temporary = staging / f".row-{index:02d}.npz.partial"
    write_deterministic_npz(temporary, arrays)
    with np.load(temporary, allow_pickle=False) as reopened:
        if set(reopened.files) != set(arrays):
            raise RuntimeError("sealed row member set drift")
        for name, expected in arrays.items():
            observed = reopened[name]
            if observed.shape != expected.shape or observed.dtype != expected.dtype:
                raise RuntimeError("sealed row member schema drift: " + name)
            if not np.array_equal(observed, expected):
                raise RuntimeError("sealed row member reopen mismatch: " + name)
    digest = file_sha(temporary)
    target = staging / f"row-{index:02d}-{digest[:16]}.npz"
    os.replace(temporary, target)
    fsync_directory(staging)
    result["artifact"] = {
        "path": target.name, "sha256": digest,
        "bytes": target.stat().st_size,
        "members": {
            name: {
                "shape": list(value.shape), "dtype": value.dtype.str,
                "logical_raw_sha256": (
                    logical_hashes[name]
                    if name in logical_hashes else logical_array_sha256(value)
                ),
            }
            for name, value in arrays.items()
        },
        "metadata_schema": artifact_metadata["schema"],
        "dependency_bundle_sha256": dependency_bundle["bundle_sha256"],
    }
    if "route_A" in result:
        result["route_A"]["lossless_artifact_members"] = tuple(
            sorted(ROUTE_A_ARTIFACT_MEMBERS)
        )
    else:
        result["route_B"]["lossless_artifact_members"] = tuple(
            sorted(ROUTE_B_ARTIFACT_MEMBERS)
        )
    return result


def row_worker(
    index: int, row: dict, staging_text: str,
    dependency_bundle: dict, mask_library: dict, queue: object,
) -> None:
    started = time.monotonic()
    try:
        child_dependency_bundle = science_dependency_bundle()
        if child_dependency_bundle != dependency_bundle:
            raise RuntimeError(
                "executable dependency bundle changed between parent and row child"
            )
        ledger = Ledger()
        result = run_science_row(index, row, ledger, mask_library)
        result = seal_row_artifact(
            index, result, Path(staging_text), dependency_bundle
        )
        result["resource"] = {
            "elapsed_seconds_including_compression_reopen": time.monotonic() - started,
            "maximum_RSS_bytes": engine.rss_bytes(),
            "swaps_absolute_fresh_process": engine.swap_count(),
            "row_wall_ceiling_seconds": contract.ROW_WALL_CEILING_SECONDS,
            "row_RSS_ceiling_bytes": contract.ROW_RSS_CEILING_BYTES,
        }
        result["row_pass"] = bool(
            result["row_pass"]
            and result["resource"]["elapsed_seconds_including_compression_reopen"]
            < contract.ROW_WALL_CEILING_SECONDS
            and result["resource"]["maximum_RSS_bytes"]
            < contract.ROW_RSS_CEILING_BYTES
            and result["resource"]["swaps_absolute_fresh_process"] == 0
        )
        queue.put({"ok": True, "result": result, "ledger": asdict(ledger)})
    except BaseException as error:
        queue.put({
            "ok": False, "error_type": type(error).__name__,
            "error": str(error), "row_index": index,
        })


def accumulate_child_ledger(parent: Ledger, child: dict) -> None:
    additive = (
        "science_train_rows", "route_A_rows", "route_B_rows", "route_C_rows",
        "held_rows", "canonical_interacting_forward_trajectories",
        "canonical_matched_free_forward_trajectories",
        "canonical_repeated_free_forward_trajectories",
        "carried_interacting_forward_trajectories", "forward_trajectories",
        "carried_matched_free_forward_trajectories",
        "inverse_trajectories", "trajectory_calls", "forward_update_calls",
        "inverse_update_calls", "post_car_technical_captures",
        "post_word_technical_captures",
    )
    for field in additive:
        setattr(parent, field, getattr(parent, field) + child[field])
    if child["refit_performed"]:
        raise RuntimeError("child reported an unauthorized refit")


def run_rows_in_fresh_processes(
    manifest: tuple[dict, ...], staging: Path, dependency_bundle: dict,
    mask_library: dict,
) -> tuple[list[dict], Ledger]:
    context = multiprocessing.get_context("spawn")
    results = []
    ledger = Ledger()
    for index, row in enumerate(manifest):
        parent_started = time.monotonic()
        queue = context.Queue()
        process = context.Process(
            target=row_worker,
            args=(
                index, row, str(staging), dependency_bundle,
                mask_library, queue,
            ),
        )
        process.start()
        deadline = parent_started + contract.ROW_WALL_CEILING_SECONDS
        message = None
        while message is None:
            remaining = deadline - time.monotonic()
            if remaining <= 0.0:
                process.terminate()
                process.join()
                raise RuntimeError(
                    f"row {index} exceeded sealed-row wall ceiling"
                )
            try:
                # Receive before join: the result is deliberately richer than
                # a pipe buffer, so joining first can deadlock on Queue flush.
                message = queue.get(timeout=min(1.0, remaining))
            except Empty:
                if not process.is_alive():
                    process.join()
                    raise RuntimeError(
                        f"row {index} child exit={process.exitcode} without receipt"
                    )
        process.join(max(0.0, deadline - time.monotonic()))
        if process.exitcode != 0:
            if process.is_alive():
                process.terminate()
                process.join()
            raise RuntimeError(f"row {index} child exit={process.exitcode}")
        queue.close()
        if not message["ok"]:
            raise RuntimeError(
                f"row {index} failed: {message['error_type']}: {message['error']}"
            )
        parent_elapsed = time.monotonic() - parent_started
        message["result"]["resource"][
            "parent_elapsed_seconds_including_spawn_compression_reopen"
        ] = parent_elapsed
        message["result"]["row_pass"] = bool(
            message["result"]["row_pass"]
            and parent_elapsed < contract.ROW_WALL_CEILING_SECONDS
        )
        results.append(message["result"])
        accumulate_child_ledger(ledger, message["ledger"])
    return results, ledger


def decode_complex(value: list[float]) -> complex:
    return complex(float(value[0]), float(value[1]))


def artifact_path(staging: Path, result: dict) -> Path:
    return staging / result["artifact"]["path"]


def deletion_distance(
    route: str, baseline: dict, deleted: dict, staging: Path,
) -> dict:
    if route == ROUTE_A:
        base = baseline["route_A"]
        candidate = deleted["route_A"]
        with np.load(artifact_path(staging, baseline), allow_pickle=False) as base_npz:
            with np.load(artifact_path(staging, deleted), allow_pickle=False) as deleted_npz:
                full_distance = float(np.max(abs(
                    base_npz["delta_J"] - deleted_npz["delta_J"]
                )))
        primary_distance = max(
            max(abs(a - b) for a, b in zip(base["front_trace_carried"], candidate["front_trace_carried"])),
            max(abs(a - b) for a, b in zip(base["fixed_trace_carried"], candidate["fixed_trace_carried"])),
        )
        floor = max(
            float(base["update2_null"]["floor"]),
            float(candidate["update2_null"]["floor"]),
        )
        valid = bool(deleted["row_pass"])
        if not valid:
            disposition = "invalid"
        elif primary_distance >= floor:
            disposition = "primary-sensitive"
        elif full_distance >= floor:
            disposition = "full-field-sensitive"
        else:
            disposition = "coexistence-only"
        return {
            "valid": valid, "comparison_floor": floor,
            "full_field_distance": full_distance,
            "primary_front_fixed_distance": primary_distance,
            "disposition": disposition,
        }
    base_phasors = [decode_complex(value) for value in baseline["route_B"]["primary_response_phasors"]]
    candidate_phasors = [decode_complex(value) for value in deleted["route_B"]["primary_response_phasors"]]
    distance = max(abs(a - b) for a, b in zip(base_phasors, candidate_phasors))
    floor = max(
        float(baseline["route_B"]["response_floor"]),
        float(deleted["route_B"]["response_floor"]),
    )
    valid = bool(
        deleted["row_pass"] and deleted["route_B"]["character_floor_valid"]
    )
    return {
        "valid": valid, "comparison_floor": floor,
        "response_phasor_chord_distance": float(distance),
        "disposition": (
            "invalid" if not valid else "sensitive" if distance >= floor
            else "coexistence-only"
        ),
    }


def apply_deletion_audits(results: list[dict], staging: Path) -> None:
    baselines = {}
    for result in results:
        identity = result["row"]
        if (
            identity["role"] == "primary-mass-grid"
            and identity["source_beta"] == "-4pi/9"
            and identity["probe_beta"] == "-4pi/9"
            and identity["geometry"] == "train-canonical"
        ):
            baselines[identity["route"]] = result
    if set(baselines) != {ROUTE_A, ROUTE_B}:
        raise RuntimeError("intact middle-mass deletion baselines missing")
    for result in results:
        identity = result["row"]
        if identity["role"] != "selected-deletion":
            result["deletion_audit"] = {"status": "not-a-deletion-row"}
            continue
        audit = deletion_distance(
            identity["route"], baselines[identity["route"]], result, staging
        )
        deletion = identity["deletion"]
        baseline = baselines[identity["route"]]
        if identity["route"] == ROUTE_A:
            response_magnitude = max(
                max(abs(value) for value in result["route_A"]["front_trace_carried"]),
                max(abs(value) for value in result["route_A"]["fixed_trace_carried"]),
            )
        else:
            response = [
                decode_complex(value)
                for value in result["route_B"]["primary_response_phasors"]
            ]
            response_magnitude = max(abs(value - 1.0) for value in response)
        audit["deleted_primary_response_magnitude"] = float(response_magnitude)
        structural_gate = bool(audit["valid"])
        if deletion == "emitter":
            structural_gate = bool(
                structural_gate
                and result["source_ledger"]["executable_emitter_angle"] == 0.0
                and result["source_ledger"]["active_mediator_weight_update1"]
                < audit["comparison_floor"]
                and response_magnitude < audit["comparison_floor"]
            )
            audit["emitter_terminal_gate"] = structural_gate
        if deletion == "collision":
            structural_gate = bool(
                structural_gate
                and result["source_ledger"]["executable_collision_angle"] == 0.0
                and result["source_ledger"]["active_mediator_weight_update1"]
                > NUMERIC_GATE
                and response_magnitude < audit["comparison_floor"]
            )
            audit["collision_terminal_gate"] = structural_gate
        if deletion == "mediator-stream":
            response_null = response_magnitude < audit["comparison_floor"]
            audit["mediator_stream_terminal_gate"] = bool(
                structural_gate
                and result["source_ledger"]["mediator_stream_enabled"] is False
                and result["source_ledger"]["maximum_mediator_displacement"] <= NUMERIC_GATE
                and response_null
            )
            structural_gate = audit["mediator_stream_terminal_gate"]
        if deletion == "contact":
            structural_gate = bool(
                structural_gate
                and result["source_ledger"]["executable_contact_coupling"] == 0.0
            )
            audit["contact_structural_gate"] = structural_gate
        if deletion == "probe-coin":
            structural_gate = bool(
                structural_gate
                and result["source_ledger"]["executable_probe_coin"] == "identity"
                and result["source_ledger"]["maximum_transverse_CAR_weight"]
                <= NUMERIC_GATE
            )
            audit["probe_coin_structural_gate"] = structural_gate
        if deletion in ("source-mass-factor", "probe-mass-factor"):
            distance = audit.get(
                "primary_front_fixed_distance",
                audit.get("response_phasor_chord_distance", 0.0),
            )
            source_ledger_change = abs(
                result["source_ledger"]["active_mediator_weight_update1"]
                - baseline["source_ledger"]["active_mediator_weight_update1"]
            )
            audit["source_ledger_distance_from_intact"] = source_ledger_change
            audit["factor_effect_observed"] = bool(
                audit["valid"] and distance >= audit["comparison_floor"]
            )
            if deletion == "source-mass-factor":
                structural_gate = bool(
                    structural_gate
                    and result["source_ledger"]["applied_source_factor"] == 1.0
                    and source_ledger_change > contract.SOURCE_LEDGER_TOLERANCE
                )
                audit["source_factor_ledger_gate"] = structural_gate
            else:
                structural_gate = bool(
                    structural_gate
                    and result["source_ledger"]["applied_probe_factor"] == 1.0
                    and source_ledger_change <= contract.SOURCE_LEDGER_TOLERANCE
                )
                audit["probe_factor_ledger_gate"] = structural_gate
        audit["structural_deletion_gate"] = structural_gate
        audit["deletion_contract_pass"] = bool(
            structural_gate
            and (
                deletion not in ("source-mass-factor", "probe-mass-factor")
                or audit.get("factor_effect_observed", False)
            )
        )
        if not structural_gate:
            audit["valid"] = False
            audit["disposition"] = "invalid"
        result["deletion_audit"] = audit


def mirror_audits(results: list[dict]) -> dict:
    audits = {}
    for route in (ROUTE_A, ROUTE_B):
        canonical = next(
            result for result in results
            if result["row"]["route"] == route
            and result["row"]["role"] == "primary-mass-grid"
            and result["row"]["source_beta"] == "-4pi/9"
            and result["row"]["probe_beta"] == "-4pi/9"
        )
        mirrored = next(
            result for result in results
            if result["row"]["route"] == route
            and result["row"]["role"] == "mirrored-direction-control"
        )
        if route == ROUTE_A:
            carried = max(abs(a - b) for a, b in zip(
                canonical["route_A"]["front_trace_carried"],
                mirrored["route_A"]["front_trace_carried"],
            ))
            lab_reversal = max(abs(a + b) for a, b in zip(
                canonical["route_A"]["front_trace_lab"],
                mirrored["route_A"]["front_trace_lab"],
            ))
            audits[route] = {
                "carried_response_residual": carried,
                "lab_axis_sign_reversal_residual": lab_reversal,
                "pass": max(carried, lab_reversal) <= NUMERIC_GATE,
            }
        else:
            left = [decode_complex(value) for value in canonical["route_B"]["primary_response_phasors"]]
            right = [decode_complex(value) for value in mirrored["route_B"]["primary_response_phasors"]]
            residual = max(abs(np.conj(a) - b) for a, b in zip(left, right))
            audits[route] = {
                "response_phasor_conjugacy_residual": float(residual),
                "pass": residual <= NUMERIC_GATE,
            }
    return audits


def response_gate_audits(results: list[dict]) -> dict:
    primary = [
        result for result in results
        if result["row"]["role"] in (
            "primary-mass-grid", "mirrored-direction-control"
        )
    ]
    route_a_gates = [
        bool(result["route_A"]["primary_response_gate"])
        for result in primary if result["row"]["route"] == ROUTE_A
    ]
    route_b_gates = [
        bool(
            result["route_B"]["character_floor_valid"]
            and result["route_B"]["circular_morphology"].get("classification")
            == "sustained"
        )
        for result in primary if result["row"]["route"] == ROUTE_B
    ]
    deletions = [
        result for result in results
        if result["row"]["role"] == "selected-deletion"
    ]
    structural_valid = all(
        result["deletion_audit"].get("valid", False) for result in deletions
    )
    mediator_terminal = all(
        result["deletion_audit"].get("mediator_stream_terminal_gate", False)
        for result in deletions if result["row"]["deletion"] == "mediator-stream"
    )
    factor_effects = all(
        result["deletion_audit"].get("factor_effect_observed", False)
        for result in deletions
        if result["row"]["deletion"] in (
            "source-mass-factor", "probe-mass-factor"
        )
    )
    return {
        "Route_A": {
            "rows": len(route_a_gates), "passed_rows": sum(route_a_gates),
            "all_primary_and_mirror_response_gates": all(route_a_gates),
        },
        "Route_B": {
            "rows": len(route_b_gates), "passed_rows": sum(route_b_gates),
            "all_primary_and_mirror_response_gates": all(route_b_gates),
        },
        "deletions": {
            "all_structurally_valid": structural_valid,
            "mediator_stream_terminal_gates": mediator_terminal,
            "mass_factor_effects_observed": factor_effects,
            "contact_probe_coin_dispositions_reported_separately": all(
                "disposition" in result["deletion_audit"]
                for result in deletions
                if result["row"]["deletion"] in ("contact", "probe-coin")
            ),
        },
        "all": bool(
            all(route_a_gates) and all(route_b_gates)
            and structural_valid and mediator_terminal and factor_effects
        ),
    }


def swap_scaling_audits(results: list[dict]) -> list[dict]:
    output = []
    for route in (ROUTE_A, ROUTE_B):
        primary = {
            (result["row"]["source_beta"], result["row"]["probe_beta"]): result
            for result in results
            if result["row"]["route"] == route
            and result["row"]["role"] == "primary-mass-grid"
        }
        for (source_name, probe_name), result in sorted(primary.items()):
            response = result[
                "route_A" if route == ROUTE_A else "route_B"
            ]["response_statistic"]
            source_mass = contract.c219.common_species(
                BETA_VALUES[source_name]
            ).analytic_mass
            probe_mass = contract.c219.common_species(
                BETA_VALUES[probe_name]
            ).analytic_mass
            factor = contract.finite_angle_response_factor(
                source_mass, probe_mass
            )
            defined = response is not None and response > 0.0 and factor > 0.0
            output.append({
                "audit": "finite-angle-factor-scaling-coordinate",
                "route": route, "source_beta": source_name,
                "probe_beta": probe_name,
                "status": "defined" if defined else "undefined-nonpositive-or-character-floor-response",
                "response": response,
                "finite_angle_factor": factor,
                "normalized_response": float(response / factor) if defined else None,
                "refit": False,
            })
        for source_name, probe_name in sorted(primary):
            if source_name >= probe_name:
                continue
            left = primary[(source_name, probe_name)]
            right = primary[(probe_name, source_name)]
            left_response = left["route_A" if route == ROUTE_A else "route_B"]["response_statistic"]
            right_response = right["route_A" if route == ROUTE_A else "route_B"]["response_statistic"]
            if left_response is None or right_response is None or min(left_response, right_response) <= 0.0:
                output.append({
                    "audit": "swap-log-residual",
                    "route": route, "source_beta": source_name,
                    "probe_beta": probe_name,
                    "status": "undefined-nonpositive-or-character-floor-response",
                    "swap_log_residual": None,
                })
                continue
            source_mass = contract.c219.common_species(BETA_VALUES[source_name]).analytic_mass
            probe_mass = contract.c219.common_species(BETA_VALUES[probe_name]).analytic_mass
            factor_left = contract.finite_angle_response_factor(source_mass, probe_mass)
            factor_right = contract.finite_angle_response_factor(probe_mass, source_mass)
            output.append({
                "audit": "swap-log-residual",
                "route": route, "source_beta": source_name,
                "probe_beta": probe_name, "status": "defined",
                "swap_log_residual": contract.swap_log_residual(
                    left_response, right_response, factor_left, factor_right
                ),
            })
        for beta_name in BETA_VALUES:
            output.append({
                "audit": "swap-log-residual",
                "route": route, "source_beta": beta_name,
                "probe_beta": beta_name,
                "status": "undefined-diagonal-swap-identity",
                "swap_log_residual": None,
            })
    return output


def population_cv(values: list[float]) -> float:
    array = np.asarray(values, dtype=float)
    mean = float(np.mean(array))
    return float(np.std(array, ddof=0) / mean) if mean > 0.0 else float("inf")


def source_law_scaling_summary(
    results: list[dict], audits: list[dict],
) -> dict:
    route_summaries = {}
    source_tables = {}
    for route in (ROUTE_A, ROUTE_B):
        primary = [
            result for result in results
            if result["row"]["route"] == route
            and result["row"]["role"] == "primary-mass-grid"
        ]
        primary_by_key = {
            (result["row"]["source_beta"], result["row"]["probe_beta"]): result
            for result in primary
        }
        source_table = {
            key: float(result["source_ledger"]["active_mediator_weight_update1"])
            for key, result in primary_by_key.items()
        }
        source_tables[route] = source_table
        probe_cvs = {}
        source_mean_weights = {}
        for source_name in BETA_VALUES:
            source_weights = [
                source_table[(source_name, probe_name)]
                for probe_name in BETA_VALUES
            ]
            probe_cvs[source_name] = population_cv(source_weights)
            source_mean_weights[source_name] = float(np.mean(source_weights))
        log_masses = []
        log_weights = []
        for source_name, weight in source_mean_weights.items():
            mass = float(contract.c219.common_species(
                BETA_VALUES[source_name]
            ).analytic_mass)
            if mass <= 0.0 or weight <= 0.0:
                continue
            log_masses.append(np.log(mass))
            log_weights.append(np.log(weight))
        design = np.column_stack((np.ones(len(log_masses)), log_masses))
        intercept, exponent = np.linalg.lstsq(
            design, np.asarray(log_weights), rcond=None
        )[0]
        normalized = []
        source_rows_eligible = bool(
            len(primary) == 9
            and all(result.get("row_pass", False) for result in primary)
            and all(weight > 0.0 for weight in source_table.values())
        )
        scaling_eligible = source_rows_eligible
        for (source_name, probe_name), result in primary_by_key.items():
            route_data = result["route_A" if route == ROUTE_A else "route_B"]
            response = route_data["response_statistic"]
            valid = (
                result.get("row_pass", False)
                and response is not None and response > 0.0
            )
            if route == ROUTE_A:
                valid = bool(
                    valid and route_data["update2_null"]["pass"]
                    and response >= route_data["update2_null"]["floor"]
                )
            else:
                valid = bool(
                    valid and route_data["character_floor_valid"]
                    and response >= route_data["response_floor"]
                )
            source_mass = contract.c219.common_species(
                BETA_VALUES[source_name]
            ).analytic_mass
            probe_mass = contract.c219.common_species(
                BETA_VALUES[probe_name]
            ).analytic_mass
            factor = contract.finite_angle_response_factor(
                source_mass, probe_mass
            )
            valid = valid and factor > 0.0
            scaling_eligible = scaling_eligible and valid
            if valid:
                normalized.append(float(response / factor))
        normalized_cv = (
            population_cv(normalized) if scaling_eligible and len(normalized) == 9
            else None
        )
        swaps = [
            audit for audit in audits
            if audit.get("audit") == "swap-log-residual"
            and audit["route"] == route
            and audit["status"] != "undefined-diagonal-swap-identity"
        ]
        swaps_defined = (
            len(swaps) == 3
            and all(audit["status"] == "defined" for audit in swaps)
        )
        maximum_swap = (
            max(float(audit["swap_log_residual"]) for audit in swaps)
            if swaps_defined else None
        )
        source_law_pass = bool(
            source_rows_eligible
            and len(log_masses) == 3
            and abs(float(exponent) - 2.0) <= 0.15
            and max(probe_cvs.values()) <= 1e-8
        )
        scaling_pass = bool(
            scaling_eligible
            and normalized_cv is not None and normalized_cv <= 0.25
            and swaps_defined and maximum_swap is not None
            and maximum_swap <= 0.25
        )
        disposition = (
            "source-law-failed" if not source_law_pass
            else "scaling-ineligible-failed" if not scaling_eligible or not swaps_defined
            else "scaling-mismatch" if not scaling_pass
            else "source-law-and-scaling-qualified"
        )
        route_summaries[route] = {
            "observed_update1_source_exponent": float(exponent),
            "free_intercept_OLS_intercept": float(intercept),
            "exponent_target": 2.0, "exponent_tolerance": 0.15,
            "maximum_probe_beta_population_CV": max(probe_cvs.values()),
            "probe_beta_population_CV_by_source": probe_cvs,
            "collapsed_mean_source_weight_by_source": source_mean_weights,
            "source_law_eligible_all9": source_rows_eligible,
            "source_law_fit_points": len(log_masses),
            "scaling_eligible_all9": scaling_eligible,
            "R_over_finite_angle_factor_population_CV": normalized_cv,
            "maximum_nontrivial_swap_log_residual": maximum_swap,
            "nontrivial_swap_rows": len(swaps),
            "source_law_pass": source_law_pass,
            "scaling_pass": scaling_pass,
            "disposition": disposition,
            "refit": False,
        }
    cross_route_source_residual = max(
        abs(source_tables[ROUTE_A][key] - source_tables[ROUTE_B][key])
        for key in source_tables[ROUTE_A]
    )
    exponent_cross_route_residual = abs(
        route_summaries[ROUTE_A]["observed_update1_source_exponent"]
        - route_summaries[ROUTE_B]["observed_update1_source_exponent"]
    )
    cross_route_pass = (
        cross_route_source_residual <= 1e-8
        and exponent_cross_route_residual <= 1e-8
    )
    return {
        "routes": route_summaries,
        "cross_route_update1_ledger_residual": cross_route_source_residual,
        "cross_route_exponent_residual": exponent_cross_route_residual,
        "cross_route_pass": cross_route_pass,
        "all": bool(
            cross_route_pass
            and all(row["source_law_pass"] and row["scaling_pass"]
                    for row in route_summaries.values())
        ),
    }


def source_law_scaling_dry_fixture() -> dict:
    results = []
    audits = []
    for route in (ROUTE_A, ROUTE_B):
        for source_name in BETA_VALUES:
            for probe_name in BETA_VALUES:
                source_mass = contract.c219.common_species(
                    BETA_VALUES[source_name]
                ).analytic_mass
                probe_mass = contract.c219.common_species(
                    BETA_VALUES[probe_name]
                ).analytic_mass
                factor = contract.finite_angle_response_factor(
                    source_mass, probe_mass
                )
                route_key = "route_A" if route == ROUTE_A else "route_B"
                results.append({
                    "row": {
                        "route": route, "role": "primary-mass-grid",
                        "source_beta": source_name,
                        "probe_beta": probe_name,
                    },
                    "source_ledger": {
                        "active_mediator_weight_update1": float(source_mass**2)
                    },
                    "row_pass": True,
                    route_key: {
                        "response_statistic": float(7.0 * factor),
                        **(
                            {
                                "character_floor_valid": True,
                                "response_floor": 1e-12,
                            }
                            if route == ROUTE_B else
                            {"update2_null": {"pass": True, "floor": 1e-12}}
                        ),
                    },
                })
        beta_names = tuple(BETA_VALUES)
        for left_index in range(len(beta_names)):
            for right_index in range(left_index + 1, len(beta_names)):
                audits.append({
                    "audit": "swap-log-residual", "route": route,
                    "source_beta": beta_names[left_index],
                    "probe_beta": beta_names[right_index],
                    "status": "defined", "swap_log_residual": 0.0,
                })
    summary = source_law_scaling_summary(results, audits)
    return {
        "summary": summary,
        "target_exponent": 2.0, "exponent_tolerance": 0.15,
        "maximum_probe_beta_population_CV": 1e-8,
        "maximum_R_over_F_population_CV": 0.25,
        "maximum_nontrivial_swap_log_residual": 0.25,
        "undefined_or_nonpositive_disposition": "scaling-ineligible-failed",
        "pass": summary["all"],
    }


def atomic_34_row_audit(
    manifest: tuple[dict, ...], results: list[dict], ledger: Ledger,
    staging: Path,
) -> dict:
    observed_identities = tuple(result["row"] for result in results)
    expected_identities = tuple(
        row_identity(index, row) for index, row in enumerate(manifest)
    )
    counts = asdict(ledger)
    artifacts_valid = True
    lossless_a = True
    package_bytes = 0
    for result in results:
        path = artifact_path(staging, result)
        package_bytes += path.stat().st_size
        artifacts_valid = artifacts_valid and file_sha(path) == result["artifact"]["sha256"]
        with np.load(path, allow_pickle=False) as payload:
            artifacts_valid = artifacts_valid and set(payload.files) == set(result["artifact"]["members"])
            metadata = json.loads(
                payload["artifact_metadata_utf8"].tobytes().decode("utf-8")
            )
            artifacts_valid = artifacts_valid and (
                metadata["row_identity"] == result["row"]
                and metadata["mask_bitorder"] == "little"
                and metadata["updates"] == list(RESPONSE_WINDOW)
                and len(metadata["proper_cubic_frame_order"]) == 24
                and metadata["dependency_bundle_sha256"]
                == result["artifact"]["dependency_bundle_sha256"]
            )
            for name in payload.files:
                observed_logical = logical_array_sha256(payload[name])
                artifacts_valid = artifacts_valid and (
                    observed_logical
                    == result["artifact"]["members"][name]["logical_raw_sha256"]
                )
                if name != "artifact_metadata_utf8":
                    artifacts_valid = artifacts_valid and (
                        observed_logical
                        == metadata["logical_raw_array_sha256"][name]
                    )
            if result["row"]["route"] == ROUTE_A:
                lossless_a = lossless_a and (
                    payload["delta_j"].shape == (4, 3, 25, 25, 25)
                    and payload["delta_j"].dtype == np.dtype("<f8")
                    and payload["delta_J"].shape == (4, 3, 25)
                    and payload["canonical_mask_packbits"].dtype == np.uint8
                    and payload["carried_mask_packbits_all24"].shape[0] == 24
                )
            else:
                artifacts_valid = artifacts_valid and (
                    payload["interacting_characters_all_axes"].shape == (4, 3)
                    and payload["free_characters_all_axes"].shape == (4, 3)
                    and payload["repeated_free_characters_all_axes"].shape == (4, 3)
                    and payload["response_phasors_all_axes"].shape == (4, 3)
                    and payload["principal_angles_diagnostic_only"].shape == (4, 3)
                    and payload["interacting_character_magnitudes"].shape == (4, 3)
                    and payload["matched_free_character_magnitudes"].shape == (4, 3)
                    and payload["repeated_free_character_magnitudes"].shape == (4, 3)
                )
    exact = (
        len(results) == 34
        and observed_identities == expected_identities
        and counts == EXPECTED_COUNTS
        and all(result["row_pass"] for result in results)
        and sum("route_A" in result for result in results) == 17
        and sum("route_B" in result for result in results) == 17
        and artifacts_valid and lossless_a
        and package_bytes <= PACKAGE_CEILING_BYTES
    )
    return {
        "pass": exact, "rows": len(results),
        "ordered_identity_sha256": object_digest(observed_identities),
        "expected_identity_sha256": object_digest(expected_identities),
        "counts_exact": counts == EXPECTED_COUNTS,
        "lossless_route_A_fields_and_masks_present": lossless_a,
        "artifact_hashes_and_members_reopened": artifacts_valid,
        "row_artifact_bytes": package_bytes,
        "package_ceiling_bytes": PACKAGE_CEILING_BYTES,
        "held_rows": 0, "route_C_rows": 0, "refit_performed": False,
    }


def science_train() -> None:
    # Hash qualification and the safe-train fixture precede every output
    # directory, support, operator, or amplitude allocation.
    dependency_bundle = science_dependency_bundle()
    one_particle_fixture = safe_train_one_particle_fixture()
    if not one_particle_fixture["pass"]:
        raise RuntimeError("safe-train one-particle preservation fixture failed")
    manifest = build_ab_train_manifest()
    if object_digest(manifest) != AB_TRAIN_MANIFEST_SHA256:
        raise RuntimeError("A/B manifest drift before science")
    mask_library = build_exact_mask_library(manifest)
    if OUTPUT_ROOT.exists():
        raise RuntimeError("science output root already exists; refusing overwrite")
    OUTPUT_ROOT.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(
        prefix=".physical_local_bond_character_ab_train_cycle509_", dir=OUTPUT_ROOT.parent
    ))
    results, ledger = run_rows_in_fresh_processes(
        manifest, staging, dependency_bundle, mask_library
    )
    apply_deletion_audits(results, staging)
    mirror = mirror_audits(results)
    response_gates = response_gate_audits(results)
    scaling = swap_scaling_audits(results)
    source_scaling = source_law_scaling_summary(results, scaling)
    atomic = atomic_34_row_audit(manifest, results, ledger, staging)
    route_a = [result for result in results if result["row"]["route"] == ROUTE_A]
    route_b = [result for result in results if result["row"]["route"] == ROUTE_B]
    all_pass = (
        atomic["pass"] and all(value["pass"] for value in mirror.values())
        and response_gates["all"] and source_scaling["all"]
        and one_particle_fixture["pass"]
    )
    payload = {
        "authority": AUTHORITY, "audit": AUDIT,
        "contract": {
            "revision": 3, "contract_runner_sha256": CONTRACT_RUNNER_SHA256,
            "contract_note_sha256": CONTRACT_NOTE_SHA256,
            "ab_train_manifest_sha256": AB_TRAIN_MANIFEST_SHA256,
            "science_runner_sha256": dependency_bundle["science_runner"]["observed_sha256"],
            "dependency_bundle_sha256": dependency_bundle["bundle_sha256"],
            "selector": None, "refit": False,
        },
        "dependency_bundle": dependency_bundle,
        "safe_train_one_particle_fixture": one_particle_fixture,
        "resource_qualification_technical_only": {
            "runner_sha256": RESOURCE_RUNNER_SHA256,
            "transcript_sha256": RESOURCE_TRANSCRIPT_SHA256,
            "payload_sha256": RESOURCE_PAYLOAD_SHA256,
            "verdict": "technical-resource-qualified",
        },
        "exact_boolean_mask_certificate": mask_library["summary"],
        "counts": asdict(ledger),
        "route_A_results": route_a, "route_B_results": route_b,
        "route_C": {"status": "open-unimplemented", "manifest_rows_not_executed": 8},
        "held": {"rows_executed": 0, "evaluator_present": False},
        "artifact_index": {},
        "mirror_audits": mirror,
        "response_gate_audits": response_gates,
        "source_law_scaling_summary": source_scaling,
        "swap_scaling_audits": scaling,
        "atomic_34_row_audit": atomic,
        "passes": {
            "technical": atomic["pass"],
            "mirror": all(value["pass"] for value in mirror.values()),
            "response": response_gates["all"],
            "source_law_scaling": source_scaling["all"],
            "one_particle_preservation": one_particle_fixture["pass"],
            "all": all_pass,
        },
        "verdict": "science-train-complete" if all_pass else "science-train-complete-with-failed-gates",
    }
    index_payload = {
        "authority": AUTHORITY, "audit": AUDIT,
        "ab_train_manifest_sha256": AB_TRAIN_MANIFEST_SHA256,
        "science_runner_sha256": dependency_bundle["science_runner"]["observed_sha256"],
        "dependency_bundle_sha256": dependency_bundle["bundle_sha256"],
        "rows": [
            {"row_identity": result["row"], "artifact": result["artifact"]}
            for result in results
        ],
    }
    index_path = staging / "artifact_index.json"
    index_path.write_bytes(json_bytes(index_payload) + b"\n")
    fsync_file(index_path)
    payload["artifact_index"] = {
        "path": index_path.name, "sha256": file_sha(index_path),
        "bytes": index_path.stat().st_size,
    }
    result_path = staging / "science_result.json"
    result_path.write_bytes(json_bytes(payload) + b"\n")
    fsync_file(result_path)
    transcript_path = staging / "transcript.log"
    transcript_line = b"SCIENCE_RESULT " + json_bytes(payload) + b"\n"
    transcript_path.write_bytes(transcript_line)
    fsync_file(transcript_path)
    preserved_resource_path = staging / "qualified_resource_transcript.log"
    preserved_resource_path.write_bytes(RESOURCE_TRANSCRIPT.read_bytes())
    fsync_file(preserved_resource_path)
    if file_sha(preserved_resource_path) != RESOURCE_TRANSCRIPT_SHA256:
        raise RuntimeError("preserved qualified resource transcript hash drift")
    receipt = {
        "authority": AUTHORITY, "audit": AUDIT,
        "artifact_index_sha256": file_sha(index_path),
        "science_result_sha256": file_sha(result_path),
        "transcript_sha256": file_sha(transcript_path),
        "resource_runner_sha256": RESOURCE_RUNNER_SHA256,
        "resource_transcript_sha256": RESOURCE_TRANSCRIPT_SHA256,
        "preserved_resource_transcript_sha256": file_sha(preserved_resource_path),
        "science_runner_sha256": dependency_bundle["science_runner"]["observed_sha256"],
        "dependency_bundle_sha256": dependency_bundle["bundle_sha256"],
        "ab_train_manifest_sha256": AB_TRAIN_MANIFEST_SHA256,
        "atomic_34_row_audit_pass": atomic["pass"],
    }
    receipt_path = staging / "run_receipt.json"
    receipt_path.write_bytes(json_bytes(receipt) + b"\n")
    fsync_file(receipt_path)
    package_bytes = sum(
        path.stat().st_size for path in staging.iterdir() if path.is_file()
    )
    if package_bytes > PACKAGE_CEILING_BYTES:
        raise RuntimeError(
            f"sealed package {package_bytes} exceeds cap {PACKAGE_CEILING_BYTES}"
        )
    # The staging directory and final root share a parent/filesystem.  Every
    # member has been reopened and hashed before the single directory rename.
    fsync_directory(staging)
    fsync_directory(OUTPUT_ROOT.parent)
    os.replace(staging, OUTPUT_ROOT)
    fsync_directory(OUTPUT_ROOT.parent)
    # Post-rename acceptance reopens every content-addressed row and every
    # hash-DAG surface from the final repo-local path.
    for result in results:
        final_row = OUTPUT_ROOT / result["artifact"]["path"]
        if file_sha(final_row) != result["artifact"]["sha256"]:
            raise RuntimeError("post-rename row artifact hash drift")
        with np.load(final_row, allow_pickle=False) as reopened:
            if set(reopened.files) != set(result["artifact"]["members"]):
                raise RuntimeError("post-rename row artifact member drift")
    final_hashes = {
        "artifact_index_sha256": file_sha(OUTPUT_ROOT / index_path.name),
        "science_result_sha256": file_sha(OUTPUT_ROOT / result_path.name),
        "transcript_sha256": file_sha(OUTPUT_ROOT / transcript_path.name),
        "preserved_resource_transcript_sha256": file_sha(
            OUTPUT_ROOT / preserved_resource_path.name
        ),
    }
    if any(final_hashes[key] != receipt[key] for key in final_hashes):
        raise RuntimeError("post-rename packet hash-DAG drift")
    reopened_receipt = json.loads(
        (OUTPUT_ROOT / receipt_path.name).read_text(encoding="utf-8")
    )
    if reopened_receipt != receipt:
        raise RuntimeError("post-rename run receipt drift")
    fsync_directory(OUTPUT_ROOT)
    print(transcript_line.decode("utf-8"), end="")


def science_output_exemplar(rows: tuple[dict, ...]) -> dict:
    common = {
        "row": row_identity(0, rows[0]), "technical": {}, "residuals": {},
        "full_state_covariance_all24": {}, "full_response_covariance_all24": {},
        "elementwise_mask_covariance_all24": {},
        "source_ledger": {}, "deletion_audit": {}, "resource": {},
        "artifact": {}, "row_pass": True,
    }
    route_a = {
        **common,
        "route_A": {
            "lossless_artifact_members": sorted(ROUTE_A_ARTIFACT_MEMBERS),
            "front_trace_lab": [],
            "front_trace_carried": [], "fixed_trace_lab": [],
            "fixed_trace_carried": [], "update2_null": {},
            "morphology_updates3_to5": {}, "response_statistic": 0.0,
            "structural_cone_leakage": 0.0,
        },
    }
    route_b = {
        **common,
        "route_B": {
            "lossless_artifact_members": sorted(ROUTE_B_ARTIFACT_MEMBERS),
            "primary_response_phasors": [],
            "character_floor_valid": True, "response_floor": 1e-10,
            "circular_morphology": {}, "response_statistic": 0.0,
        },
    }
    return {
        "authority": AUTHORITY, "audit": AUDIT,
        "contract": {}, "dependency_bundle": {},
        "safe_train_one_particle_fixture": {},
        "resource_qualification_technical_only": {},
        "exact_boolean_mask_certificate": {},
        "counts": EXPECTED_COUNTS, "route_A_results": [route_a],
        "route_B_results": [route_b], "route_C": {
            "status": "open-unimplemented", "manifest_rows_not_executed": 8,
        },
        "held": {"rows_executed": 0, "evaluator_present": False},
        "artifact_index": {}, "mirror_audits": {},
        "response_gate_audits": {}, "source_law_scaling_summary": {},
        "swap_scaling_audits": [],
        "atomic_34_row_audit": {},
        "passes": {
            "technical": True, "mirror": True,
            "response": True, "source_law_scaling": True,
            "one_particle_preservation": True, "all": True,
        },
        "verdict": "science-train-complete",
    }


def validate_science_schema(payload: dict) -> bool:
    top = {
        "authority", "audit", "contract", "dependency_bundle",
        "safe_train_one_particle_fixture", "resource_qualification_technical_only",
        "exact_boolean_mask_certificate",
        "counts", "route_A_results", "route_B_results", "route_C", "held",
        "artifact_index", "mirror_audits", "response_gate_audits",
        "source_law_scaling_summary",
        "swap_scaling_audits", "atomic_34_row_audit",
        "passes", "verdict",
    }
    common = {
        "row", "technical", "residuals", "full_state_covariance_all24",
        "full_response_covariance_all24",
        "elementwise_mask_covariance_all24", "source_ledger",
        "deletion_audit", "resource", "artifact", "row_pass",
    }
    if set(payload) != top or set(payload["route_A_results"][0]) != common | {"route_A"}:
        return False
    if set(payload["route_B_results"][0]) != common | {"route_B"}:
        return False
    route_a = payload["route_A_results"][0]["route_A"]
    route_b = payload["route_B_results"][0]["route_B"]
    return (
        set(route_a["lossless_artifact_members"]) == ROUTE_A_ARTIFACT_MEMBERS
        and set(route_b["lossless_artifact_members"]) == ROUTE_B_ARTIFACT_MEMBERS
        and payload["held"] == {"rows_executed": 0, "evaluator_present": False}
        and payload["route_C"]["status"] == "open-unimplemented"
    )


def identity_joint_stream_boolean(states: set[tuple]) -> set[tuple]:
    output = set()
    for mediator, left, right in states:
        moved = []
        for cell, direction in (left, right):
            moved.append((
                tuple(int(value) for value in (
                    np.asarray(cell) + contract.c210.DIRECTIONS[direction]
                )), direction,
            ))
        pair = contract.canonical_joint_pair(moved[0], moved[1])
        if pair is not None:
            output.add((mediator, pair[0], pair[1]))
    return output


def direct_boolean_oracle_masks(
    geometry: engine.CarriedGeometry, *, probe_coin_identity: bool,
    mediator_stream_enabled: bool = True, retain_joint_states: bool = False,
    compute_joint_digests: bool = True,
) -> dict:
    """Independent tuple-set oracle for small exact-joint dry fixtures."""
    source = geometry.source_cell
    packet_cells = geometry.packet_cells
    positive, negative = geometry.packet_directions
    support = {
        (None, pair[0], pair[1])
        for left_cell in packet_cells for right_cell in packet_cells
        for pair in [contract.canonical_joint_pair(
            (left_cell, positive), (right_cell, negative)
        )] if pair is not None
    }
    taint: set[tuple] = set()
    route_a = []
    route_b = []
    rows = []
    joint_stages = []
    for update in range(1, geometry.depth + 1):
        support = contract.emit_boolean_support(
            support, source, geometry.outgoing_direction
        )
        taint = contract.emit_boolean_support(
            taint, source, geometry.outgoing_direction
        )
        if probe_coin_identity:
            support = identity_joint_stream_boolean(support)
            taint = identity_joint_stream_boolean(taint)
        else:
            support = contract.car_dense_stream_boolean(support)
            taint = contract.car_dense_stream_boolean(taint)
        pre_support_count = len(support)
        pre_taint_count = len(taint)
        pre_support_digest = (
            direct_joint_state_digest(support) if compute_joint_digests else None
        )
        pre_taint_digest = (
            direct_joint_state_digest(taint) if compute_joint_digests else None
        )
        pre_support_states = support.copy() if retain_joint_states else None
        pre_taint_states = taint.copy() if retain_joint_states else None
        route_a.append(modes_to_bond_mask(
            {mode for state in taint for mode in state[1:]}, geometry.side
        ))
        support, taint, _cells = contract.collision_boolean_support(
            support, taint
        )
        post_support_count = len(support)
        post_taint_count = len(taint)
        post_support_digest = (
            direct_joint_state_digest(support) if compute_joint_digests else None
        )
        post_taint_digest = (
            direct_joint_state_digest(taint) if compute_joint_digests else None
        )
        post_support_states = support.copy() if retain_joint_states else None
        post_taint_states = taint.copy() if retain_joint_states else None
        route_b.append(modes_to_bond_mask(
            {mode for state in taint for mode in state[1:]}, geometry.side
        ))
        if mediator_stream_enabled:
            support = contract.mediator_stream_boolean(support)
            taint = contract.mediator_stream_boolean(taint)
        rows.append({
            "update": update,
            "pre_collision_support_states": pre_support_count,
            "pre_collision_tainted_states": pre_taint_count,
            "post_collision_support_states": post_support_count,
            "post_collision_tainted_states": post_taint_count,
            "pre_collision_support_joint_sha256": pre_support_digest,
            "pre_collision_taint_joint_sha256": pre_taint_digest,
            "post_collision_support_joint_sha256": post_support_digest,
            "post_collision_taint_joint_sha256": post_taint_digest,
            "post_stream_support_joint_sha256": (
                direct_joint_state_digest(support) if compute_joint_digests else None
            ),
            "post_stream_taint_joint_sha256": (
                direct_joint_state_digest(taint) if compute_joint_digests else None
            ),
            "collision_cells": len(_cells),
        })
        if retain_joint_states:
            joint_stages.append({
                "pre_collision_support": pre_support_states,
                "pre_collision_taint": pre_taint_states,
                "post_collision_support": post_support_states,
                "post_collision_taint": post_taint_states,
                "post_stream_support": support.copy(),
                "post_stream_taint": taint.copy(),
            })
    output = {
        "route_A_masks": tuple(route_a),
        "route_B_masks": tuple(route_b),
        "rows": rows,
    }
    if retain_joint_states:
        output["_joint_stages"] = joint_stages
    return output


def small_boolean_oracle_geometry() -> engine.CarriedGeometry:
    center = (5, 5, 5)
    return engine.CarriedGeometry(
        "revision3-exact-joint-oracle", 11, (9, 5, 5), center, 1, 0, 3,
        ((4, 5, 5), (5, 5, 5), (6, 5, 5)), (0, 1),
        tuple(int(value) for value in np.eye(3, dtype=int).ravel()),
    )


def mask_tuple_mismatch(
    expected: tuple[np.ndarray, ...], observed: tuple[np.ndarray, ...],
) -> int:
    return sum(
        int(np.count_nonzero(left != right))
        for left, right in zip(expected, observed)
    )


def carry_direct_joint_states(
    states: set[tuple], frame: np.ndarray, side: int,
    mode_cache: dict | None = None, mediator_cache: dict | None = None,
) -> set[tuple]:
    # The state set has millions of repeated references to only O(10^3) modes
    # and O(10) mediator keys.  Memoizing the exact finite permutation avoids
    # repeating frame-cell arithmetic without changing a single Boolean edge.
    mode_cache = {} if mode_cache is None else mode_cache
    mediator_cache = {} if mediator_cache is None else mediator_cache
    output = set()
    for mediator, left, right in states:
        if left not in mode_cache:
            mode_cache[left] = engine.carry_mode(left, frame, side)
        if right not in mode_cache:
            mode_cache[right] = engine.carry_mode(right, frame, side)
        if mediator not in mediator_cache:
            mediator_cache[mediator] = engine.carry_mediator(
                mediator, frame, side
            )
        moved_left = mode_cache[left]
        moved_right = mode_cache[right]
        pair = contract.canonical_joint_pair(moved_left, moved_right)
        if pair is None:
            raise RuntimeError("proper-cubic carry collapsed a lawful wedge")
        output.add((
            mediator_cache[mediator], pair[0], pair[1]
        ))
    return output


def independent_small_oracle_contract() -> dict:
    """Direct tuple oracle: joint equality and all-24 P_F equivariance."""
    geometry = small_boolean_oracle_geometry()
    cases = []
    mismatch = 0
    relation_mismatch = 0
    projected_mismatch = 0
    for probe_coin_identity, mediator_stream_enabled in (
        (False, True), (True, True), (False, False),
    ):
        direct = direct_boolean_oracle_masks(
            geometry, probe_coin_identity=probe_coin_identity,
            mediator_stream_enabled=mediator_stream_enabled,
            retain_joint_states=True,
        )
        factorized = exact_factorized_boolean_certificate(
            geometry, probe_coin_identity=probe_coin_identity,
            mediator_stream_enabled=mediator_stream_enabled,
            retain_joint_digests=True,
        )
        projected_mask_mismatch = (
            mask_tuple_mismatch(
                direct["route_A_masks"], factorized["route_A_masks"]
            )
            + mask_tuple_mismatch(
                direct["route_B_masks"], factorized["route_B_masks"]
            )
        )
        digest_fields = (
            "pre_collision_support_joint_sha256",
            "pre_collision_taint_joint_sha256",
            "post_collision_support_joint_sha256",
            "post_collision_taint_joint_sha256",
            "post_stream_support_joint_sha256",
            "post_stream_taint_joint_sha256",
        )
        joint_digest_mismatch = sum(
            direct_row[field] != factorized_row[field]
            for direct_row, factorized_row in zip(
                direct["rows"], factorized["metadata"]["rows"]
            )
            for field in digest_fields
        )
        frame_mask_mismatch = 0
        frame_joint_set_mismatch = 0
        for index, frame in enumerate(contract.c210.proper_cubic_frames()):
            carried_geometry = engine.carry_geometry(geometry, frame, index)
            carried = direct_boolean_oracle_masks(
                carried_geometry, probe_coin_identity=probe_coin_identity,
                mediator_stream_enabled=mediator_stream_enabled,
                retain_joint_states=True, compute_joint_digests=False,
            )
            frame_mask_mismatch += mask_tuple_mismatch(
                tuple(carry_mask(mask, frame) for mask in direct["route_A_masks"]),
                carried["route_A_masks"],
            )
            frame_mask_mismatch += mask_tuple_mismatch(
                tuple(carry_mask(mask, frame) for mask in direct["route_B_masks"]),
                carried["route_B_masks"],
            )
            mode_cache = {}
            mediator_cache = {}
            for base_stage, carried_stage in zip(
                direct["_joint_stages"], carried["_joint_stages"]
            ):
                for stage_name in (
                    "pre_collision_support", "pre_collision_taint",
                    "post_collision_support", "post_collision_taint",
                    "post_stream_support", "post_stream_taint",
                ):
                    expected_states = carry_direct_joint_states(
                        base_stage[stage_name], frame, geometry.side,
                        mode_cache, mediator_cache,
                    )
                    frame_joint_set_mismatch += (
                        expected_states != carried_stage[stage_name]
                    )
        case_relation_mismatch = joint_digest_mismatch + frame_joint_set_mismatch
        case_projected_mismatch = projected_mask_mismatch + frame_mask_mismatch
        relation_mismatch += case_relation_mismatch
        projected_mismatch += case_projected_mismatch
        mismatch += case_relation_mismatch + case_projected_mismatch
        cases.append({
            "probe_coin_identity": probe_coin_identity,
            "mediator_stream_enabled": mediator_stream_enabled,
            "direct_tuple_vs_factorized_joint_digest_mismatch": joint_digest_mismatch,
            "direct_tuple_vs_factorized_projected_mask_mismatch": projected_mask_mismatch,
            "all24_direct_joint_P_F_A_P_FT_set_mismatch": (
                frame_joint_set_mismatch
            ),
            "all24_projected_bond_mask_mismatch": frame_mask_mismatch,
            "route_A_bond_counts": [
                int(np.count_nonzero(mask)) for mask in direct["route_A_masks"]
            ],
            "route_B_bond_counts": [
                int(np.count_nonzero(mask)) for mask in direct["route_B_masks"]
            ],
        })
    return {
        "cases": cases,
        "proper_cubic_frames_per_case": 24,
        "exact_joint_relation_mismatch_count": relation_mismatch,
        "projected_bond_mask_mismatch_count": projected_mismatch,
        "total_relation_or_mask_mismatch_count": mismatch,
        "pass": mismatch == 0,
        "amplitudes_evolved": 0,
    }


def actual_mask_acceptance(mask_library: dict) -> dict:
    canonical = contract.TRAIN_CANONICAL.name
    expected = {
        "intact": {
            "pre_support": [306, 14733, 187500, 1178121, 5045739],
            "post_support": [306, 14829, 188404, 1180816, 5052014],
            "pre_taint": [0, 0, 3600, 63597, 477813],
            "post_taint": [0, 192, 5403, 68947, 490220],
            "cell_support": [274, 3980, 26587, 118510, 407358],
            "cell_taint": [0, 100, 1773, 13307, 62678],
            "route_A": [0, 0, 212, 442, 792],
            "route_B": [0, 75, 213, 442, 792],
        },
        "identity-coin": {
            "post_support": [18, 30, 48, 63, 75],
            "post_taint": [0, 6, 24, 36, 42],
            "route_A": [0, 0, 5, 7, 9],
            "route_B": [0, 5, 7, 7, 9],
        },
        "parked-mediator": {
            "cell_support": [274, 2620, 12962, 46154, 133453],
            "cell_taint": [0, 0, 224, 4158, 25569],
            "route_A": [0, 0, 0, 442, 792],
            "route_B": [0, 0, 209, 442, 792],
        },
    }
    rows = []
    passed = True
    for certificate_class, targets in expected.items():
        metadata = mask_library["certificates"][
            (canonical, certificate_class)
        ]["metadata"]
        observed_rows = metadata["rows"]
        observed = {
            "pre_support": [row["pre_collision_support_states"] for row in observed_rows],
            "post_support": [row["post_collision_support_states"] for row in observed_rows],
            "pre_taint": [row["pre_collision_tainted_states"] for row in observed_rows],
            "post_taint": [row["post_collision_tainted_states"] for row in observed_rows],
            "cell_support": [row["post_stream_support_cell_blocks"] for row in observed_rows],
            "cell_taint": [row["post_stream_taint_cell_blocks"] for row in observed_rows],
            "route_A": metadata["route_A_bond_counts"],
            "route_B": metadata["route_B_bond_counts"],
        }
        case_pass = all(observed[key] == value for key, value in targets.items())
        passed = passed and case_pass
        rows.append({
            "certificate_class": certificate_class,
            "observed": observed, "expected": targets,
            "route_A_mask_sha256": metadata["route_A_mask_sha256"],
            "route_B_mask_sha256": metadata["route_B_mask_sha256"],
            "pass": case_pass,
        })
    canonical_geometry = engine.canonical_geometry()
    mirror_row = contract.corridor_row(
        "train", "mask-mirror-fixture", ROUTE_A,
        BETA_VALUES["-4pi/9"], BETA_VALUES["-4pi/9"],
        contract.TRAIN_MIRRORED,
    )
    mirror_geometry = geometry_from_row(mirror_row)
    mirror_frame = None
    mirror_frame_index = None
    for index, frame in enumerate(contract.c210.proper_cubic_frames()):
        carried = engine.carry_geometry(canonical_geometry, frame, index)
        if (
            carried.source_cell == mirror_geometry.source_cell
            and carried.probe_center == mirror_geometry.probe_center
            and carried.outgoing_direction == mirror_geometry.outgoing_direction
            and set(carried.packet_cells) == set(mirror_geometry.packet_cells)
            and set(carried.packet_directions) == set(mirror_geometry.packet_directions)
        ):
            mirror_frame = frame
            mirror_frame_index = index
            break
    if mirror_frame is None:
        raise RuntimeError("no proper-cubic frame maps actual canonical to mirror")
    canonical_certificate = mask_library["certificates"][
        (contract.TRAIN_CANONICAL.name, "intact")
    ]
    mirror_certificate = mask_library["certificates"][
        (contract.TRAIN_MIRRORED.name, "intact")
    ]
    mirror_mismatch = 0
    for route_key in ("route_A_masks", "route_B_masks"):
        mirror_mismatch += mask_tuple_mismatch(
            tuple(
                carry_mask(mask, mirror_frame)
                for mask in canonical_certificate[route_key]
            ),
            mirror_certificate[route_key],
        )
    passed = passed and mirror_mismatch == 0
    return {
        "rows": rows,
        "actual_canonical_to_mirror": {
            "proper_cubic_frame_index": mirror_frame_index,
            "A_and_B_elementwise_mismatch": mirror_mismatch,
            "pass": mirror_mismatch == 0,
        },
        "terminal_zero_classes": ["emitter", "collision"],
        "shared_intact_deletions": [
            NO_DELETION, "contact", "source-mass-factor", "probe-mass-factor",
        ],
        "pass": passed,
    }


def factored_mask_dry_contract() -> dict:
    """Validate exact factorized joint masks without amplitude evolution."""
    started = time.monotonic()
    starting_rss = engine.rss_bytes()
    manifest = build_ab_train_manifest()
    mask_library = build_exact_mask_library(manifest)
    acceptance = actual_mask_acceptance(mask_library)
    oracle = independent_small_oracle_contract()
    terminal_zero = True
    for row in manifest:
        if row["deletion"] not in ("emitter", "collision"):
            continue
        geometry = geometry_from_row(row)
        for route in (ROUTE_A, ROUTE_B):
            masks, _metadata = route_structural_masks(
                geometry, route, row["deletion"], mask_library
            )
            terminal_zero = terminal_zero and not any(np.any(mask) for mask in masks)
    return {
        "representation": "exact-factorized-symmetric-Boolean-joint-adjacency",
        "claim_scope": "exact Boolean joint taint projected to directed bonds",
        "amplitudes_evolved": 0,
        "proper_cubic_frames_per_oracle_case": 24,
        "independent_small_tuple_oracle": oracle,
        "actual_geometry_acceptance": acceptance,
        "terminal_emitter_collision_masks_zero": terminal_zero,
        "certificate_summary": mask_library["summary"],
        "dominance_pass": acceptance["pass"],
        "induction_pass": oracle["pass"],
        "exact_joint_relation_mismatch_count": (
            oracle["exact_joint_relation_mismatch_count"]
        ),
        "elementwise_mask_mismatch_count": (
            oracle["projected_bond_mask_mismatch_count"]
        ),
        "elapsed_seconds": time.monotonic() - started,
        "wall_ceiling_seconds": contract.ROW_WALL_CEILING_SECONDS,
        "maximum_RSS_bytes": max(starting_rss, engine.rss_bytes()),
    }


def safe_train_one_particle_fixture() -> dict:
    """Operator-first safe-train preservation fixture; no held inference."""
    rows = []
    maximum_unitarity = 0.0
    maximum_cubic_covariance = 0.0
    maximum_fock_restriction = 0.0
    maximum_rest_residual = 0.0
    for beta_name, beta in BETA_VALUES.items():
        species = contract.c219.common_species(beta)
        scalar_eigenvalue = np.trace(
            contract.c210.P_SCALAR @ species.coin
        )
        principal_rest_phase = float(np.angle(scalar_eigenvalue))
        operator_mass = principal_rest_phase / contract.c219.C_SQUARED
        principal_rest_mass = contract.c219.rest_mass(species)
        rest_residual = max(
            abs(operator_mass - species.analytic_mass),
            abs(principal_rest_mass - species.analytic_mass),
        )
        unitarity = float(np.linalg.norm(
            species.coin.conj().T @ species.coin - np.eye(6)
        ))
        cubic = max(
            float(np.linalg.norm(
                contract.c210.direction_permutation(frame)
                @ species.coin
                @ contract.c210.direction_permutation(frame).conj().T
                - species.coin
            ))
            for frame in contract.c210.proper_cubic_frames()
        )
        fock = c229.fock_lift(species.coin)
        one_indices = [1 << mode for mode in range(6)]
        fock_restriction = float(np.linalg.norm(
            fock[np.ix_(one_indices, one_indices)] - species.coin
        ))
        maximum_unitarity = max(maximum_unitarity, unitarity)
        maximum_cubic_covariance = max(maximum_cubic_covariance, cubic)
        maximum_fock_restriction = max(
            maximum_fock_restriction, fock_restriction
        )
        maximum_rest_residual = max(maximum_rest_residual, rest_residual)
        rows.append({
            "beta": beta_name,
            "M_plus_operator_coordinate": float(species.analytic_mass),
            "operator_scalar_principal_rest_mass": float(operator_mass),
            "Cycle219_principal_rest_mass": float(principal_rest_mass),
            "principal_rest_phase": principal_rest_phase,
            "principal_branch": abs(principal_rest_phase) < np.pi,
            "coin_unitarity_residual": unitarity,
            "maximum_all24_coin_covariance_residual": cubic,
            "Cycle229_Fock_one_particle_restriction_residual": fock_restriction,
        })
    occupations = c229.occupation_table(6)
    particle_number = np.sum(occupations, axis=1)
    contact_diagonal = np.exp(
        1j * contract.CONTACT_COUPLING
        * particle_number * (particle_number - 1.0) / 2.0
    )
    n_le_one = particle_number <= 1.0
    contact_n_le_one_residual = float(np.max(abs(
        contact_diagonal[n_le_one] - 1.0
    )))
    geometry = engine.canonical_geometry()
    support, _ = engine.support_trace(geometry)
    initial = engine.initial_blocks(geometry, support[0].basis)
    collision_without_active = engine.collision(
        initial, support[0].basis, 0.137
    )
    collision_none_residual = engine.state_residual(
        collision_without_active, initial
    )
    initial.clear()
    collision_without_active.clear()
    passed = (
        maximum_rest_residual < 2e-12
        and maximum_unitarity < 2e-12
        and maximum_cubic_covariance < 2e-12
        and maximum_fock_restriction < 2e-12
        and all(row["principal_branch"] for row in rows)
        and contact_n_le_one_residual < NUMERIC_GATE
        and collision_none_residual < NUMERIC_GATE
    )
    return {
        "scope": "safe-train Cycle219 one-particle preservation only",
        "rows": rows,
        "Cycle230_contact_N_le_1_identity_residual": contact_n_le_one_residual,
        "collision_identity_without_active_mediator_residual": collision_none_residual,
        "held_dispersion_or_inertial_extension": "open-not-evaluated",
        "legacy_prepared_response_nomenclature_promoted": False,
        "pass": passed,
    }


def contract_checks() -> tuple[dict[str, bool], dict]:
    rows = build_ab_train_manifest()
    resource_payload = parse_qualified_resource()
    manifest_digest = object_digest(rows)
    identities = tuple(row_identity(index, row) for index, row in enumerate(rows))
    exemplar = science_output_exemplar(rows)
    mask_contract = factored_mask_dry_contract()
    one_particle_fixture = safe_train_one_particle_fixture()
    source_scaling_fixture = source_law_scaling_dry_fixture()
    dependency_bundle = science_dependency_bundle()
    unique = len({object_digest(row) for row in rows}) == 34
    route_a = [row for row in rows if row["route"] == ROUTE_A]
    route_b = [row for row in rows if row["route"] == ROUTE_B]
    deletion_counts = {
        route: tuple(row["deletion"] for row in rows if row["route"] == route and row["role"] == "selected-deletion")
        for route in (ROUTE_A, ROUTE_B)
    }
    source_text = Path(__file__).read_text(encoding="utf-8")
    checks = {
        "contract_runner_hash": file_sha(CONTRACT_RUNNER) == CONTRACT_RUNNER_SHA256,
        "contract_note_hash": file_sha(CONTRACT_NOTE) == CONTRACT_NOTE_SHA256,
        "resource_runner_hash": file_sha(RESOURCE_RUNNER) == RESOURCE_RUNNER_SHA256,
        "resource_transcript_hash": file_sha(RESOURCE_TRANSCRIPT) == RESOURCE_TRANSCRIPT_SHA256,
        "resource_payload_exact_technical_qualified": resource_payload["verdict"] == "technical-resource-qualified",
        "revision3": contract.REVISION == 3,
        "full_manifest_hash_bindings": (
            contract.EXPECTED_TRAIN_MANIFEST_SHA256 == FULL_TRAIN_MANIFEST_SHA256
            and contract.EXPECTED_HELD_MANIFEST_SHA256 == HELD_MANIFEST_SHA256_BINDING_ONLY
        ),
        "authority_none_audit_unset": AUTHORITY == "none" and AUDIT == "unset",
        "cli_exact": CLI_MODES == ("dry-contract", "science-train"),
        "authorization_dry_clean_only": authorization_allowed("dry-contract", {}),
        "authorization_dry_rejects_train_even_empty": not authorization_allowed("dry-contract", {TRAIN_AUTHORIZATION_ENV: ""}),
        "authorization_dry_rejects_scout_even_empty": not authorization_allowed("dry-contract", {SCOUT_AUTHORIZATION_ENV: ""}),
        "authorization_dry_rejects_held_even_empty": not authorization_allowed("dry-contract", {HELD_AUTHORIZATION_ENV: ""}),
        "authorization_dry_rejects_integrity_even_empty": not authorization_allowed("dry-contract", {SCIENCE_INTEGRITY_ENV: ""}),
        "authorization_train_exact_distinct": authorization_allowed("science-train", {
            TRAIN_AUTHORIZATION_ENV: TRAIN_AUTHORIZATION_TOKEN,
            SCIENCE_INTEGRITY_ENV: file_sha(Path(__file__)),
        }),
        "authorization_train_missing_integrity_rejected": not authorization_allowed("science-train", {TRAIN_AUTHORIZATION_ENV: TRAIN_AUTHORIZATION_TOKEN}),
        "authorization_train_wrong_integrity_rejected": not authorization_allowed("science-train", {
            TRAIN_AUTHORIZATION_ENV: TRAIN_AUTHORIZATION_TOKEN,
            SCIENCE_INTEGRITY_ENV: "wrong",
        }),
        "authorization_train_wrong_rejected": not authorization_allowed("science-train", {
            TRAIN_AUTHORIZATION_ENV: "wrong",
            SCIENCE_INTEGRITY_ENV: file_sha(Path(__file__)),
        }),
        "authorization_train_plus_scout_rejected": not authorization_allowed("science-train", {
            TRAIN_AUTHORIZATION_ENV: TRAIN_AUTHORIZATION_TOKEN,
            SCIENCE_INTEGRITY_ENV: file_sha(Path(__file__)),
            SCOUT_AUTHORIZATION_ENV: "",
        }),
        "authorization_train_plus_held_rejected": not authorization_allowed("science-train", {
            TRAIN_AUTHORIZATION_ENV: TRAIN_AUTHORIZATION_TOKEN,
            SCIENCE_INTEGRITY_ENV: file_sha(Path(__file__)),
            HELD_AUTHORIZATION_ENV: "",
        }),
        "ordered_tuple_exactly_34": len(ORDERED_AB_TRAIN_KEYS) == len(rows) == 34,
        "ordered_rows_unique": unique,
        "ab_manifest_hash": manifest_digest == AB_TRAIN_MANIFEST_SHA256,
        "routes_17_each": len(route_a) == len(route_b) == 17,
        "roles_exact": sum(row["role"] == "primary-mass-grid" for row in rows) == 18 and sum(row["role"] == "mirrored-direction-control" for row in rows) == 2 and sum(row["role"] == "selected-deletion" for row in rows) == 14,
        "deletions_exact_each_route": all(deletion_counts[route] == DELETIONS for route in (ROUTE_A, ROUTE_B)),
        "routeC_unreachable": all(row["route"] != ROUTE_C for row in rows),
        "held_rows_never_constructed": all(row["disposition"] == "train" for row in rows),
        "held_bytes_absent_from_runner": all(
            token not in source_text
            for token in (
                "HELD" + "_" + "BETAS",
                "HELD" + "_" + "CANONICAL",
                "HELD" + "_" + "MIRRORED",
                "-8" + "pi/9", "L" + "27",
            )
        ),
        "no_runtime_full_or_held_manifest_builder": (
            "row_" + "manifests(" not in source_text
        ),
        "no_selector_no_refit": all(row["row_selector"] is False and row["refit"] is False for row in rows),
        "sample_surfaces_exact": all(row["route_sample_surface"] == (contract.ROUTE_A_SAMPLE_SURFACE if row["route"] == ROUTE_A else contract.ROUTE_B_SAMPLE_SURFACE) for row in rows),
        "routeA_full_field_required": all(row["retain_full_field"] is True for row in route_a),
        "symmetric_deletions": all(row["deletion_applies_symmetrically_to"] == "interacting-and-matched-free" for row in rows),
        "operation_counts_exact": EXPECTED_COUNTS["science_train_rows"] == 34 and EXPECTED_COUNTS["forward_trajectories"] == 34 * 51 and EXPECTED_COUNTS["inverse_trajectories"] == 34 and EXPECTED_COUNTS["held_rows"] == 0 and EXPECTED_COUNTS["carried_matched_free_forward_trajectories"] == 34 * 24,
        "classifier_excludes_update2": linear_morphology((1.0, 1.0, 1.0), (0.0,))["samples_used"] == (3, 4, 5),
        "route_surface_deletion_masks_qualified": (
            mask_contract["amplitudes_evolved"] == 0
            and mask_contract["proper_cubic_frames_per_oracle_case"] == 24
            and mask_contract["exact_joint_relation_mismatch_count"] == 0
            and mask_contract["elementwise_mask_mismatch_count"] == 0
            and mask_contract["dominance_pass"]
            and mask_contract["induction_pass"]
            and mask_contract["elapsed_seconds"]
            < mask_contract["wall_ceiling_seconds"]
            and mask_contract["maximum_RSS_bytes"] < contract.ROW_RSS_CEILING_BYTES
        ),
        "safe_train_one_particle_fixture": one_particle_fixture["pass"],
        "source_law_scaling_summary_contract": source_scaling_fixture["pass"],
        "science_dependency_bundle_rehashed": dependency_bundle["all_dependencies_pass"],
        "artifact_strategy_frozen": (
            not OUTPUT_ROOT.exists()
            and PACKAGE_CEILING_BYTES == 64 * 1024 * 1024
        ),
        "science_schema": validate_science_schema(exemplar),
    }
    details = {
        "ab_train_manifest_sha256": manifest_digest,
        "ordered_rows": identities,
        "counts": EXPECTED_COUNTS,
        "resource_binding": {
            "runner_sha256": RESOURCE_RUNNER_SHA256,
            "transcript_sha256": RESOURCE_TRANSCRIPT_SHA256,
            "payload_sha256": RESOURCE_PAYLOAD_SHA256,
            "verdict": resource_payload["verdict"],
        },
        "schema_sha256": object_digest(exemplar),
        "factored_mask_contract": mask_contract,
        "safe_train_one_particle_fixture": one_particle_fixture,
        "source_law_scaling_contract": source_scaling_fixture,
        "science_dependency_bundle": dependency_bundle,
        "artifact_contract": {
            "output_root": str(OUTPUT_ROOT.relative_to(ROOT)),
            "fresh_spawn_per_row": True,
            "same_filesystem_atomic_directory_rename": True,
            "reopen_and_sha256_before_acceptance": True,
            "package_ceiling_bytes": PACKAGE_CEILING_BYTES,
            "dry_creates_output_root": False,
        },
    }
    return checks, details


def dry_contract() -> None:
    checks, details = contract_checks()
    payload = {
        "authority": AUTHORITY, "audit": AUDIT, "mode": "dry-contract",
        "checks": checks, "details": details,
        "counts": {
            "states_evolved": 0, "science_rows_executed": 0,
            "held_rows_executed": 0, "route_C_rows_executed": 0,
            "resource_scouts_executed": 0, "refits": 0,
        },
        "passes": {"all": all(checks.values())},
        "verdict": "dry-contract-qualified" if all(checks.values()) else "dry-contract-failed",
    }
    print("DRY_CONTRACT " + json.dumps(payload, sort_keys=True, separators=(",", ":")))
    if not all(checks.values()):
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=CLI_MODES)
    arguments = parser.parse_args()
    enforce_authorization(arguments.mode, os.environ)
    if arguments.mode == "dry-contract":
        dry_contract()
    else:
        science_train()


if __name__ == "__main__":
    main()
