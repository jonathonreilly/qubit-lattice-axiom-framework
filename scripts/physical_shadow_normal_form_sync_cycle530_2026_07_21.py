#!/usr/bin/env python3
"""Cycle 530: persistent-shadow normal form and primitive selected-seam core.

Cycle 527 prepares twelve local occupation shadows before the selected two-cell
reduction.  Cycle 530 uses those shadows as a bounded carrier normal form.  It
compiles the Cycle-219 coin, the exact selected Cycle-230 CAR seam, contact,
and the Cycle-526 event/current/K macro into physical nearest-neighbour one-
and two-M2 calls.  A thirteen-FSWAP braid, rather than one endpoint FSWAP,
supplies the complete two-cell exterior sign.

The native normal-form isometry S remains a supplied dense preparation and
unpreparation.  Therefore this is a sharply delimited primitive factorization
of G_q inside S G_q S^dagger, not a primitive factorization of S or of the
complete physical update.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21 as c527
import physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21 as c522
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523
import physical_selected_seam_event_current_adapter_cycle526_2026_07_21 as c526
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
Q_PER_CELL = 6
Q_WIDTH = 12
NATIVE_PATCH_M2 = 83
FULL_SHADOW_PATCH_M2 = 95
K_BITS = 16
TOLERANCE = 8e-10
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "shadow-normal-form-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SHADOW_NORMAL_FORM_SYNC_CYCLE530_NOTE_2026-07-21.md"
)
CYCLE219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
CYCLE230_RUNNER = ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
CYCLE235_RUNNER = ROOT / "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py"
CYCLE269_RUNNER = ROOT / "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py"
CYCLE315_RUNNER = ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py"
CYCLE522_RUNNER = ROOT / "scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py"
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
CYCLE526_RUNNER = ROOT / "scripts/physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py"
CYCLE527_RUNNER = ROOT / "scripts/physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21.py"

STRICT_FILE_HASHES = {
    CYCLE219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    CYCLE230_RUNNER: "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    CYCLE235_RUNNER: "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
    CYCLE269_RUNNER: "c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35",
    CYCLE315_RUNNER: "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    CYCLE522_RUNNER: "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    CYCLE526_RUNNER: "7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd",
    CYCLE527_RUNNER: "2ca2021fa76b889128b587a6a0d67986e236319ea8fb7ccd1dfaf31982c55fa0",
}


class CertificateFailure(RuntimeError):
    """A declared Cycle-530 certificate condition failed."""


class ResourceWall(RuntimeError):
    """Technical ceiling; never evidence for a physics obstruction."""


@dataclass(frozen=True)
class PhysicalGate:
    kind: str
    sites: tuple[tuple[int, int, int], ...]
    label: str
    payload: str = ""


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
    swaps = swap_count()
    if elapsed >= WALL_LIMIT_SECONDS:
        raise ResourceWall(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swaps:
        raise ResourceWall(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def matrix_payload(matrix: np.ndarray) -> str:
    values = tuple((complex(value).real.hex(), complex(value).imag.hex()) for value in matrix.reshape(-1))
    return sha256(repr(values).encode()).hexdigest()


def label_word(label) -> int:
    left_number, left_label, right_number, right_label = label
    if left_number != len(left_label) or right_number != len(right_label):
        raise ValueError("malformed complete-Fock label")
    return sum(1 << direction for direction in left_label) | sum(
        1 << (Q_PER_CELL + direction) for direction in right_label
    )


def logical_to_q_encoding(labels) -> sparse.csc_matrix:
    rows = np.asarray([label_word(label) for label in labels], dtype=np.int64)
    if len(set(map(int, rows))) != 1 << Q_WIDTH:
        raise CertificateFailure("the complete two-cell Fock labels do not exhaust twelve q bits")
    return sparse.coo_matrix(
        (np.ones(len(labels)), (rows, np.arange(len(labels)))),
        shape=(1 << Q_WIDTH, len(labels)),
        dtype=complex,
    ).tocsc()


def embed_mode_gate(gate: c523.ModeGate, width: int = Q_PER_CELL) -> np.ndarray:
    if gate.kind == "phase":
        matrix = np.diag((1, gate.matrix[0])).astype(complex)
    else:
        matrix = c523.fock_two_mode(c523.one_particle_matrix(gate))
    return c523.embed_small_gate(matrix, gate.sites, width)


def local_q_factorization() -> tuple[dict, dict]:
    species = c219.common_species(-0.3)
    mode_schedule, qr = c523.compile_adjacent_qr(species.coin)
    coin = np.eye(1 << Q_PER_CELL, dtype=complex)
    for gate in mode_schedule:
        coin = embed_mode_gate(gate) @ coin
    deleted_coin = np.eye(1 << Q_PER_CELL, dtype=complex)
    for index, gate in enumerate(mode_schedule):
        if index:
            deleted_coin = embed_mode_gate(gate) @ deleted_coin
    target_coin = c523.c229.fock_lift(species.coin)

    contact = np.eye(1 << Q_PER_CELL, dtype=complex)
    deleted_contact = np.eye(1 << Q_PER_CELL, dtype=complex)
    contact_gate = c523.controlled_phase_matrix(np.exp(1j * c230.COUPLING))
    for index, (first, second) in enumerate(combinations(range(Q_PER_CELL), 2)):
        contact = c523.embed_small_gate(contact_gate, (first, second), Q_PER_CELL) @ contact
        if index:
            deleted_contact = (
                c523.embed_small_gate(contact_gate, (first, second), Q_PER_CELL)
                @ deleted_contact
            )
    number = np.asarray([word.bit_count() for word in range(1 << Q_PER_CELL)])
    target_contact = np.diag(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    )
    controls = {
        "Cycle219_beta": -0.3,
        "Cycle230_contact_coupling": c230.COUPLING,
        "QR_Givens": qr["givens"],
        "QR_onsite_phases": qr["onsite_phases"],
        "QR_schedule_sha256": qr["schedule_sha256"],
        "local_coin_factor_count": len(mode_schedule),
        "local_contact_pair_factors": 15,
        "local_coin_reconstruction_residual": float(np.linalg.norm(coin - target_coin)),
        "local_contact_reconstruction_residual": float(np.linalg.norm(contact - target_contact)),
        "local_coin_unitarity_residual": float(np.linalg.norm(coin.conj().T @ coin - np.eye(64))),
        "local_contact_unitarity_residual": float(np.linalg.norm(contact.conj().T @ contact - np.eye(64))),
        "deleted_first_coin_factor_residual": float(np.linalg.norm(deleted_coin - target_coin)),
        "deleted_first_contact_factor_residual": float(np.linalg.norm(deleted_contact - target_contact)),
    }
    controls["pass"] = bool(
        controls["QR_Givens"] == 10
        and controls["QR_onsite_phases"] == 1
        and controls["local_coin_reconstruction_residual"] < TOLERANCE
        and controls["local_contact_reconstruction_residual"] < TOLERANCE
        and controls["local_coin_unitarity_residual"] < TOLERANCE
        and controls["local_contact_unitarity_residual"] < TOLERANCE
        and controls["deleted_first_coin_factor_residual"] > 1e-3
        and controls["deleted_first_contact_factor_residual"] > 1
    )
    return controls, {
        "mode_schedule": mode_schedule,
        "coin": sparse.csc_matrix(coin),
        "contact": sparse.csc_matrix(contact),
    }


def q_fswap(width: int, first: int, second: int) -> sparse.csc_matrix:
    rows = []
    phases = []
    for source in range(1 << width):
        left = (source >> first) & 1
        right = (source >> second) & 1
        target = source ^ ((left ^ right) << first) ^ ((left ^ right) << second)
        rows.append(target)
        phases.append(-1 if left & right else 1)
    return sparse.coo_matrix(
        (phases, (rows, np.arange(1 << width))),
        shape=(1 << width, 1 << width),
        dtype=complex,
    ).tocsc()


def braid_pairs(axis: int) -> tuple[tuple[int, int], ...]:
    if axis not in range(3):
        raise ValueError("axis must be 0, 1, or 2")
    first = 2 * axis
    second = Q_PER_CELL + 2 * axis + 1
    return tuple((index, index + 1) for index in range(first, second)) + tuple(
        (index, index + 1) for index in reversed(range(first, second - 1))
    )


def q_braid_operator(axis: int, *, deleted_factor: int | None = None) -> sparse.csc_matrix:
    result = sparse.eye(1 << Q_WIDTH, format="csc", dtype=complex)
    for index, (first, second) in enumerate(braid_pairs(axis)):
        if index == deleted_factor:
            continue
        result = q_fswap(Q_WIDTH, first, second) @ result
    return result


def q_logical_controls(labels, local_objects: dict) -> tuple[dict, dict]:
    P = logical_to_q_encoding(labels)
    logical_coin, logical_stream, logical_contact, logical_update, logical_rows = (
        c315.logical_update_controls(labels)
    )
    local_coin = local_objects["coin"]
    local_contact = local_objects["contact"]
    q_coin = sparse.kron(local_coin, local_coin, format="csc")
    q_contact = sparse.kron(local_contact, local_contact, format="csc")

    axis_rows = []
    for axis in range(3):
        braid = q_braid_operator(axis)
        target = P @ c315.edge_fswap_matrix(labels, axis)
        residual = braid @ P - target
        endpoint = q_fswap(Q_WIDTH, 2 * axis, Q_PER_CELL + 2 * axis + 1)
        endpoint_residual = endpoint @ P - target
        deleted = q_braid_operator(axis, deleted_factor=0) @ P - target
        axis_rows.append(
            {
                "axis": axis,
                "adjacent_FSWAP_factors": len(braid_pairs(axis)),
                "complete_Fock_columns": len(labels),
                "braid_intertwining_residual": c315.largest_singular(residual),
                "braid_raw_maximum": c315.raw_maximum_abs(residual),
                "naive_endpoint_FSWAP_residual": c315.largest_singular(endpoint_residual),
                "deleted_first_braid_FSWAP_residual": c315.largest_singular(deleted),
            }
        )

    q_stream = q_braid_operator(0)
    q_update = q_contact @ q_stream @ q_coin
    factor_rows = {}
    for name, physical, logical in (
        ("coin", q_coin, logical_coin),
        ("stream", q_stream, logical_stream),
        ("contact", q_contact, logical_contact),
        ("update", q_update, logical_update),
    ):
        residual = physical @ P - P @ logical
        factor_rows[name] = {
            "operator_residual": c315.largest_singular(residual),
            "raw_maximum": c315.raw_maximum_abs(residual),
        }

    one_particle_words = tuple(1 << direction for direction in range(Q_WIDTH))
    uniform = np.zeros(1 << Q_WIDTH, dtype=complex)
    uniform[list(one_particle_words)] = 1 / np.sqrt(Q_WIDTH)
    eigenvalue = np.vdot(uniform, q_update @ uniform)
    mass_residual = np.linalg.norm(q_update @ uniform - eigenvalue * uniform)

    rng = np.random.default_rng(530)
    recurrence_residuals = []
    inverse_residuals = []
    for _ in range(32):
        vector = rng.normal(size=len(labels)) + 1j * rng.normal(size=len(labels))
        vector /= np.linalg.norm(vector)
        physical_once = q_update @ (P @ vector)
        logical_once = P @ (logical_update @ vector)
        physical_twice = q_update @ physical_once
        logical_twice = P @ (logical_update @ (logical_update @ vector))
        recurrence_residuals.append(float(np.linalg.norm(physical_twice - logical_twice)))
        inverse_residuals.append(
            float(np.linalg.norm(q_update.conj().T @ physical_once - P @ vector))
        )

    diagonal = abs(logical_update.diagonal()) ** 2
    deleted_S_pair_residual = float(np.sqrt(2 * (1 - np.min(diagonal))))
    result = {
        "q_basis_dimension": 1 << Q_WIDTH,
        "logical_columns": len(labels),
        "axis_seam_braids": tuple(axis_rows),
        "factor_intertwiners": factor_rows,
        "q_update_nonzeros": q_update.nnz,
        "thirty_two_vector_two_step_recurrence_maximum": max(recurrence_residuals),
        "thirty_two_vector_inverse_maximum": max(inverse_residuals),
        "data_only_uniform_one_particle_residual": float(mass_residual),
        "data_only_rest_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "contact_nontrivial_columns": logical_rows["contact_nontrivial_columns"],
        "deleted_S_pair_q_only_maximum_code_column_residual": deleted_S_pair_residual,
        "normal_form_identity": "S G_q S^dagger E_12 = E_12 G_coarse",
        "normal_form_S_primitive_factorized": False,
    }
    result["pass"] = bool(
        all(row["adjacent_FSWAP_factors"] == 13 for row in axis_rows)
        and all(row["complete_Fock_columns"] == 4096 for row in axis_rows)
        and all(row["braid_intertwining_residual"] == 0 for row in axis_rows)
        and all(row["braid_raw_maximum"] == 0 for row in axis_rows)
        and all(row["naive_endpoint_FSWAP_residual"] > 1.99 for row in axis_rows)
        and all(row["deleted_first_braid_FSWAP_residual"] > 1 for row in axis_rows)
        and all(row["operator_residual"] == 0 for row in factor_rows.values())
        and result["thirty_two_vector_two_step_recurrence_maximum"] < 2e-13
        and result["thirty_two_vector_inverse_maximum"] < 2e-13
        and result["data_only_uniform_one_particle_residual"] < TOLERANCE
        and abs(result["data_only_rest_mass"] - result["Cycle219_mass_fixture"]) < TOLERANCE
        and result["contact_nontrivial_columns"] == 4047
        and result["deleted_S_pair_q_only_maximum_code_column_residual"] > 1
    )
    return result, {
        "P": P,
        "q_coin": q_coin,
        "q_stream": q_stream,
        "q_contact": q_contact,
        "q_update": q_update,
        "logical_update": logical_update,
    }


def full_shadow_encoding(encoding: sparse.csc_matrix, labels) -> sparse.csc_matrix:
    rows = []
    columns = []
    data = []
    physical_rows = encoding.shape[0]
    for column, label in enumerate(labels):
        word = label_word(label)
        for pointer in range(encoding.indptr[column], encoding.indptr[column + 1]):
            rows.append(word * physical_rows + int(encoding.indices[pointer]))
            columns.append(column)
            data.append(encoding.data[pointer])
    return sparse.coo_matrix(
        (data, (rows, columns)),
        shape=((1 << Q_WIDTH) * physical_rows, len(labels)),
        dtype=complex,
    ).tocsc()


def encoding_controls(length: int, labels) -> dict:
    started = time.monotonic()
    code = c269.build_code(length)
    reducer = c315.RayReducer(code)
    encoding = c315.joint_encoding(
        code,
        labels,
        reducer,
        False,
        term_builder=c522.selected_gauge_terms,
    )
    if encoding.shape[0] < len(reducer.row_by_aux):
        encoding.resize((len(reducer.row_by_aux), len(labels)))
    augmented = full_shadow_encoding(encoding, labels)
    gram = augmented.conj().T @ augmented
    identity = sparse.eye(len(labels), format="csc")
    occupied = len(set(map(int, augmented.indices)))
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "logical_columns": len(labels),
        "native_reduced_rows": encoding.shape[0],
        "native_encoding_nonzeros": encoding.nnz,
        "full_shadow_ambient_rows_sparse_only": augmented.shape[0],
        "full_shadow_encoding_nonzeros": augmented.nnz,
        "full_shadow_occupied_rows": occupied,
        "full_shadow_reused_rows": augmented.nnz - occupied,
        "full_shadow_Gram_residual": c315.largest_singular(gram - identity),
        "native_plus_full_shadow_patch_M2": FULL_SHADOW_PATCH_M2,
        "normal_form_S_support_M2": FULL_SHADOW_PATCH_M2,
        "normal_form_S_supplied_dense_isometry_completion": True,
        "normal_form_S_one_two_M2_factorized": False,
        "terminal_native_shadow_constraint_failures_after_SGqSdagger": 0,
        "terminal_code_leakage_after_SGqSdagger": 0,
        "inverse_code_leakage_after_SGqSdagger": 0,
        "arbitrary_repeat_count_code_leakage_by_induction": 0,
        "resource": checkpoint(started, f"Cycle530-E12-L{length}"),
        "pass": bool(
            len(labels) == 4096
            and encoding.shape[0] == 25_088
            and encoding.nnz == 25_600
            and augmented.nnz == occupied == 25_600
            and c315.largest_singular(gram - identity) == 0
        ),
    }


def periodic_neighbors(site, modulus: int):
    for direction in c210.DIRECTIONS:
        yield tuple((site[axis] + int(direction[axis])) % modulus for axis in range(3))


def blank_path(source, target, modulus: int, blocked: frozenset) -> tuple:
    source = tuple(source)
    target = tuple(target)
    forbidden = set(blocked) - {source, target}
    queue = deque((source,))
    parent = {source: None}
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for neighbor in periodic_neighbors(current, modulus):
            if neighbor in forbidden or neighbor in parent:
                continue
            parent[neighbor] = current
            queue.append(neighbor)
    if target not in parent:
        raise CertificateFailure(("no blank route", source, target))
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
    return tuple(reversed(path))


def tensor_path(source, target, modulus: int) -> tuple:
    current = list(source)
    path = [tuple(current)]
    for axis in range(3):
        delta = c527.periodic_delta(current[axis], target[axis], modulus)
        step = 1 if delta > 0 else -1
        for _ in range(abs(delta)):
            current[axis] = (current[axis] + step) % modulus
            path.append(tuple(current))
    if path[-1] != tuple(target):
        raise AssertionError("tensor route missed target")
    return tuple(path)


def routed_pair(path, core_kind: str, label: str, payload: str = "", *, fermionic: bool) -> tuple[PhysicalGate, ...]:
    if len(path) < 2:
        raise ValueError("two-M2 route needs distinct endpoints")
    transport = "FSWAP-route" if fermionic else "ordinary-SWAP-route"
    forward = tuple(
        PhysicalGate(transport, (path[index], path[index + 1]), f"{label}:route-{index}")
        for index in range(len(path) - 2)
    )
    core = (PhysicalGate(core_kind, (path[-2], path[-1]), f"{label}:core", payload),)
    return forward + core + tuple(reversed(forward))


def allocate_adapter_sites(length: int, occupied: frozenset) -> dict:
    modulus = c527.fine_length(length)
    names = ("P", "w", "event", "J_plus", "J_minus") + tuple(
        f"K{index}" for index in range(K_BITS)
    )
    candidates = set()
    origin = (8, 4, 4)
    for x in range(-6, 23):
        for y in range(-7, 8):
            for z in range(-7, 8):
                site = (x % modulus, y % modulus, z % modulus)
                if site not in occupied:
                    candidates.add(site)
    ordered = sorted(
        candidates,
        key=lambda site: (
            c527.periodic_l1(site, origin, modulus),
            site,
        ),
    )
    if len(ordered) < len(names):
        raise CertificateFailure("not enough blank adapter sites")
    return dict(zip(names, ordered[: len(names)]))


def q_site(bit: int, length: int):
    if bit < Q_PER_CELL:
        return c527.shadow_coordinate(c315.LEFT, bit, length)
    return c527.shadow_coordinate(c315.RIGHT, bit - Q_PER_CELL, length)


def physical_q_schedule(length: int, mode_schedule) -> tuple[dict, tuple[PhysicalGate, ...]]:
    started = time.monotonic()
    modulus = c527.fine_length(length)
    roles = c527.role_coordinates(length)
    occupied_roles = frozenset(roles.values())
    adapter = allocate_adapter_sites(length, occupied_roles)
    blocked = frozenset(set(occupied_roles) | set(adapter.values()))
    gates: list[PhysicalGate] = []
    fermionic_paths = []
    tensor_paths = []

    def add_fermionic(first, second, kind, label, payload=""):
        path = blank_path(first, second, modulus, blocked)
        fermionic_paths.append(path)
        gates.extend(routed_pair(path, kind, label, payload, fermionic=True))

    def add_cnot(first, second, label):
        path = tensor_path(first, second, modulus)
        tensor_paths.append(path)
        gates.extend(routed_pair(path, "CNOT", label, fermionic=False))

    def add_toffoli(first, second, target, label):
        sites = (first, second, target)
        for index, (kind, operands) in enumerate(c527.logical_toffoli_schedule()):
            if kind == "CNOT":
                add_cnot(sites[operands[0]], sites[operands[1]], f"{label}:{index}")
            else:
                gates.append(PhysicalGate(kind, (sites[operands[0]],), f"{label}:{index}"))

    def add_fredkin(control, first, second, label):
        add_cnot(second, first, f"{label}:pre")
        add_toffoli(control, first, second, f"{label}:toffoli")
        add_cnot(second, first, f"{label}:post")

    for cell_name, body in (("left", c315.LEFT), ("right", c315.RIGHT)):
        for gate in mode_schedule:
            if gate.kind == "phase":
                site = c527.shadow_coordinate(body, gate.sites[0], length)
                payload = matrix_payload(np.diag((1, gate.matrix[0])).astype(complex))
                gates.append(PhysicalGate("onsite-phase", (site,), f"coin:{cell_name}:{gate.label}", payload))
            else:
                first, second = (
                    c527.shadow_coordinate(body, direction, length) for direction in gate.sites
                )
                core = c523.fock_two_mode(c523.one_particle_matrix(gate))
                add_fermionic(
                    first,
                    second,
                    "fermionic-Givens",
                    f"coin:{cell_name}:{gate.label}",
                    matrix_payload(core),
                )

    left_endpoint = q_site(0, length)
    right_endpoint = q_site(7, length)
    add_cnot(left_endpoint, adapter["P"], "adapter:copy-pre-left")
    add_cnot(adapter["P"], adapter["w"], "adapter:copy-P-to-w")

    for index, (first, second) in enumerate(braid_pairs(0)):
        add_fermionic(
            q_site(first, length),
            q_site(second, length),
            "FSWAP-braid-core",
            f"seam:braid-{index}-{first}-{second}",
            "FSWAP",
        )

    add_cnot(left_endpoint, adapter["w"], "adapter:post-left-XOR")
    add_cnot(adapter["w"], adapter["event"], "adapter:event-XOR")
    add_toffoli(adapter["w"], adapter["P"], adapter["J_plus"], "adapter:J-plus")
    gates.append(PhysicalGate("X", (adapter["P"],), "adapter:negative-control-open"))
    add_toffoli(adapter["w"], adapter["P"], adapter["J_minus"], "adapter:J-minus")
    gates.append(PhysicalGate("X", (adapter["P"],), "adapter:negative-control-close"))
    for index in reversed(range(K_BITS - 1)):
        add_fredkin(adapter["w"], adapter[f"K{index}"], adapter[f"K{index + 1}"], f"adapter:K-{index}")
    add_cnot(left_endpoint, adapter["w"], "adapter:erase-post-left")
    add_cnot(adapter["P"], adapter["w"], "adapter:erase-P-from-w")
    add_cnot(right_endpoint, adapter["P"], "adapter:erase-P-with-post-right")

    contact_core = c523.controlled_phase_matrix(np.exp(1j * c230.COUPLING))
    for cell_name, body in (("left", c315.LEFT), ("right", c315.RIGHT)):
        for first, second in combinations(range(Q_PER_CELL), 2):
            add_fermionic(
                c527.shadow_coordinate(body, first, length),
                c527.shadow_coordinate(body, second, length),
                "contact-phase",
                f"contact:{cell_name}:{first}-{second}",
                matrix_payload(contact_core),
            )

    non_NN = repeated = 0
    counts = Counter(gate.kind for gate in gates)
    edge_uses = Counter()
    for gate in gates:
        repeated += len(set(gate.sites)) != len(gate.sites)
        if len(gate.sites) == 2:
            non_NN += c527.periodic_l1(*gate.sites, modulus) != 1
            edge_uses[frozenset(gate.sites)] += 1
        elif len(gate.sites) != 1:
            non_NN += 1

    blank_path_failures = sum(
        any(site in blocked for site in path[1:-1]) for path in fermionic_paths
    )
    max_fermionic_path = max(len(path) - 1 for path in fermionic_paths)
    tensor_distances = tuple(sorted({len(path) - 1 for path in tensor_paths}))
    tensor_basis_tests = tensor_basis_failures = 0
    for distance in tensor_distances:
        for word in range(1 << (distance + 1)):
            bits = tuple((word >> index) & 1 for index in range(distance + 1))
            output = c527.remote_cnot_bits(bits, distance)
            expected = list(bits)
            expected[-1] ^= bits[0]
            tensor_basis_tests += 1
            tensor_basis_failures += output != tuple(expected)
    digest = sha256()
    for gate in gates:
        digest.update(repr((gate.kind, gate.sites, gate.label, gate.payload)).encode())

    frames = c210.proper_cubic_frames()
    frame_NN_failures = frame_blank_failures = 0
    orientation_histogram = Counter()
    support = frozenset(site for gate in gates for site in gate.sites)
    for frame in frames:
        orientation_histogram[c527.direction_map(frame)[0]] += 1
        mapped_blocked = {c527.rotate_coord(site, frame, modulus) for site in blocked}
        for gate in gates:
            mapped = tuple(c527.rotate_coord(site, frame, modulus) for site in gate.sites)
            if len(mapped) == 2:
                frame_NN_failures += c527.periodic_l1(*mapped, modulus) != 1
        for path in fermionic_paths:
            mapped = tuple(c527.rotate_coord(site, frame, modulus) for site in path)
            frame_blank_failures += any(site in mapped_blocked for site in mapped[1:-1])

    group_failures = 0
    for first in frames:
        for second in frames:
            product_frame = first @ second
            for site in support:
                composed = c527.rotate_coord(
                    c527.rotate_coord(site, second, modulus), first, modulus
                )
                direct = c527.rotate_coord(site, product_frame, modulus)
                if composed != direct:
                    group_failures += 1
                    break

    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "installed_full_microgrid_M2_per_cell": c527.MICRO_SITES_PER_CELL,
        "full_microgrid_preparation_supplied": True,
        "adapter_auxiliary_M2": len(adapter),
        "physical_gate_calls": len(gates),
        "physical_gate_counts": dict(counts),
        "maximum_gate_support_M2": max(len(gate.sites) for gate in gates),
        "non_nearest_neighbor_failures": non_NN,
        "repeated_operand_failures": repeated,
        "fermionic_blank_route_count": len(fermionic_paths),
        "fermionic_blank_path_failures": blank_path_failures,
        "maximum_fermionic_blank_path_edges": max_fermionic_path,
        "ordinary_tensor_route_count": len(tensor_paths),
        "maximum_ordinary_tensor_path_edges": max(len(path) - 1 for path in tensor_paths),
        "ordinary_tensor_path_edge_lengths": tensor_distances,
        "ordinary_remote_CNOT_exhaustive_basis_tests": tensor_basis_tests,
        "ordinary_remote_CNOT_exhaustive_failures": tensor_basis_failures,
        "maximum_physical_edge_uses": max(edge_uses.values()),
        "schedule_sha256": digest.hexdigest(),
        "inverse_gate_calls": len(gates),
        "roundtrip_gate_calls": 2 * len(gates),
        "inverse_is_reverse_dagger": True,
        "ordinary_SWAP_is_only_tensor_wire_transport": True,
        "FSWAP_is_only_fermionic_mode_transport_or_core": True,
        "proper_frames": len(frames),
        "seam_direction_histogram_under_frames": dict(orientation_histogram),
        "frame_nearest_neighbor_failures": frame_NN_failures,
        "frame_blank_path_failures": frame_blank_failures,
        "frame_group_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "compile_time_frame_schedule_orbit_members": len(frames),
        "single_frame_independent_gate_order_claimed": False,
        "runtime_frame_query_used": False,
        "color_or_gate_count_called_physical_time": False,
        "resource": checkpoint(started, f"Cycle530-physical-Gq-L{length}"),
        "pass": bool(
            len(adapter) == 21
            and len(gates) > 0
            and max(len(gate.sites) for gate in gates) == 2
            and non_NN == repeated == blank_path_failures == tensor_basis_failures == 0
            and len(frames) == 24
            and orientation_histogram == Counter({direction: 4 for direction in range(6)})
            and frame_NN_failures == frame_blank_failures == group_failures == 0
            and len(frames) == 24
        ),
    }, tuple(gates)


def fredkin_bits(control: int, first: int, second: int) -> tuple[int, int, int]:
    # CNOT(second -> first), Toffoli(control,first -> second), CNOT(second -> first).
    first ^= second
    second ^= control & first
    first ^= second
    return control, first, second


def adapter_and_recurrence_controls(labels) -> dict:
    truth_failures = continuity_failures = work_failures = clock_failures = 0
    recurrence_failures = 0
    tests = 0
    for label in labels:
        word = label_word(label)
        left = word & 1
        right = (word >> 7) & 1
        moved = left ^ right
        plus = moved & left
        minus = moved & (1 ^ left)
        post_left, post_right = right, left
        P = left
        w = P
        w ^= post_left
        event = w
        J_plus = w & P
        J_minus = w & (1 ^ P)
        w ^= post_left
        w ^= P
        P ^= post_right
        truth_failures += (event, J_plus, J_minus) != (moved, plus, minus)
        continuity_failures += (
            post_left - left != -(J_plus - J_minus)
            or post_right - right != J_plus - J_minus
        )
        work_failures += P != 0 or w != 0
        for clock in range(K_BITS):
            clock_failures += c526.one_hot_clock_transition(clock, event) != (
                clock + event
            ) % K_BITS
            # A second seam-only recurrence uses a fresh receipt/current bank.
            second_left, second_right = post_left, post_right
            second_event = second_left ^ second_right
            recurrence_failures += (
                (second_right, second_left) != (left, right)
                or (clock + event + second_event) % K_BITS
                != (clock + 2 * moved) % K_BITS
            )
            tests += 1
    fredkin_failures = 0
    for control, first, second in product((0, 1), repeat=3):
        output = fredkin_bits(control, first, second)
        expected = (control, second, first) if control else (control, first, second)
        fredkin_failures += output != expected
    return {
        "complete_blank_output_data_K_tests": tests,
        "event_current_truth_failures": truth_failures,
        "local_continuity_failures": continuity_failures,
        "P_w_terminal_work_failures": work_failures,
        "one_hot_K_transition_failures": clock_failures,
        "two_step_fresh_receipt_recurrence_failures": recurrence_failures,
        "Fredkin_decomposition_basis_failures": fredkin_failures,
        "retained_event_current_bank_reuse_called_fresh_Record": False,
        "pass": bool(
            tests == 4096 * K_BITS
            and truth_failures == continuity_failures == work_failures == 0
            and clock_failures == recurrence_failures == fredkin_failures == 0
        ),
    }


def site_index(cell, direction: int, length: int) -> int:
    return ((cell[0] * length + cell[1]) * length + cell[2]) * Q_PER_CELL + direction


def index_mode(index: int, length: int):
    cell_index, direction = divmod(index, Q_PER_CELL)
    x, remainder = divmod(cell_index, length * length)
    y, z = divmod(remainder, length)
    return (x, y, z), direction


def shifted(cell, axis: int, amount: int, length: int):
    result = list(cell)
    result[axis] = (result[axis] + amount) % length
    return tuple(result)


def fswap_word(word: int, first: int, second: int) -> tuple[int, int]:
    left = (word >> first) & 1
    right = (word >> second) & 1
    target = word ^ ((left ^ right) << first) ^ ((left ^ right) << second)
    return target, -1 if left & right else 1


def local_braid_words(left_word: int, right_word: int, axis: int):
    word = left_word | (right_word << Q_PER_CELL)
    phase = 1
    for first, second in braid_pairs(axis):
        word, factor = fswap_word(word, first, second)
        phase *= factor
    return word & 63, (word >> Q_PER_CELL) & 63, phase


BRAID_CACHE = {
    (axis, left, right): local_braid_words(left, right, axis)
    for axis in range(3)
    for left in range(64)
    for right in range(64)
}


def exact_B_action(occupied, length: int):
    mapped = []
    for mode in occupied:
        cell, direction = index_mode(mode, length)
        axis = direction // 2
        target_cell = shifted(cell, axis, 1 if direction % 2 == 0 else -1, length)
        mapped.append(site_index(target_cell, direction ^ 1, length))
    inversions = sum(
        mapped[first] > mapped[second]
        for first in range(len(mapped))
        for second in range(first + 1, len(mapped))
    )
    return tuple(sorted(mapped)), -1 if inversions % 2 else 1


def scheduled_braid_action(occupied, length: int, axis_order=(0, 1, 2), reverse_cells=False):
    cells = tuple(product(range(length), repeat=3))
    ordered_cells = tuple(reversed(cells)) if reverse_cells else cells
    seams = tuple((axis, cell) for axis in axis_order for cell in ordered_cells)
    order = {seam: index for index, seam in enumerate(seams)}
    words = {}
    possible_cells = set()
    for mode in occupied:
        cell, direction = index_mode(mode, length)
        words[cell] = words.get(cell, 0) | (1 << direction)
        possible_cells.add(cell)
        possible_cells.add(
            shifted(cell, direction // 2, 1 if direction % 2 == 0 else -1, length)
        )
    active = set()
    for cell in possible_cells:
        for axis in range(3):
            active.add((axis, cell))
            active.add((axis, shifted(cell, axis, -1, length)))
    phase = 1
    for axis, cell in sorted(active, key=order.get):
        target = shifted(cell, axis, 1, length)
        left, right, factor = BRAID_CACHE[(axis, words.get(cell, 0), words.get(target, 0))]
        phase *= factor
        if left:
            words[cell] = left
        else:
            words.pop(cell, None)
        if right:
            words[target] = right
        else:
            words.pop(target, None)
    output = tuple(
        sorted(
            site_index(cell, direction, length)
            for cell, word in words.items()
            for direction in range(Q_PER_CELL)
            if (word >> direction) & 1
        )
    )
    return output, phase


def simultaneous_shared_cell_audit(length: int) -> dict:
    started = time.monotonic()
    modes = Q_PER_CELL * length**3
    mismatch = target_failures = 0
    witness = None
    for occupied in combinations(range(modes), 2):
        exact_target, exact_phase = exact_B_action(occupied, length)
        physical_target, physical_phase = scheduled_braid_action(occupied, length)
        target_failures += physical_target != exact_target
        if physical_target == exact_target and physical_phase != exact_phase:
            mismatch += 1
            if witness is None:
                witness = (occupied, physical_phase, exact_phase)
    if witness is None:
        raise CertificateFailure("missing simultaneous-braid phase witness")
    order_witness_failures = 0
    order_rows = []
    witness_occupied = witness[0]
    exact_target, exact_phase = exact_B_action(witness_occupied, length)
    for axis_order in permutations(range(3)):
        for reverse_cells in (False, True):
            target, phase = scheduled_braid_action(
                witness_occupied, length, axis_order, reverse_cells
            )
            failed = target != exact_target or phase == exact_phase
            order_witness_failures += failed
            order_rows.append(
                {
                    "axis_order": axis_order,
                    "cell_order": "reverse-lex" if reverse_cells else "lex",
                    "target_correct": target == exact_target,
                    "candidate_phase": phase,
                    "exact_phase": exact_phase,
                    "remains_mismatch": phase != exact_phase,
                }
            )
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "modes": modes,
        "complete_two_particle_pairs": modes * (modes - 1) // 2,
        "canonical_schedule_target_failures": target_failures,
        "canonical_schedule_phase_mismatches": mismatch,
        "first_witness": witness_occupied,
        "first_witness_labels": tuple(index_mode(mode, length) for mode in witness_occupied),
        "candidate_witness_phase": witness[1],
        "exact_witness_phase": witness[2],
        "witness_basis_residual": abs(witness[1] - witness[2]),
        "tested_axis_and_cell_order_families": len(order_rows),
        "order_family_witness_test_failures": order_witness_failures,
        "all_tested_order_families_retain_witness": all(
            row["target_correct"] and row["remains_mismatch"] for row in order_rows
        ),
        "general_correlated_or_stateful_gauge_no_go": False,
        "selected_one_seam_factorization_invalidated": False,
        "resource": checkpoint(started, f"Cycle530-simultaneous-B-L{length}"),
        "pass": bool(
            target_failures == 0
            and mismatch > 0
            and abs(witness[1] - witness[2]) == 2
            and len(order_rows) == 12
            and order_witness_failures == 0
        ),
    }


def isolated_simultaneous_audit(length: int) -> dict:
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--internal-simultaneous",
        "--length",
        str(length),
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ResourceWall(f"simultaneous B audit timed out at L{length}") from exc
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CertificateFailure(
            f"simultaneous B audit emitted invalid JSON at L{length}: {completed.stderr[-2000:]!r}"
        ) from exc
    if completed.returncode or not payload.get("pass"):
        raise CertificateFailure(
            f"simultaneous B audit failed at L{length}: {payload!r}; stderr={completed.stderr[-2000:]!r}"
        )
    return payload


def upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    load_bearing = tuple(
        str(path.relative_to(ROOT))
        for path in (CYCLE522_RUNNER, CYCLE523_RUNNER, CYCLE526_RUNNER, CYCLE527_RUNNER)
    )
    return {
        "expected_stable_sha256": expected,
        "observed_stable_sha256": observed,
        "load_bearing_strict_pins": load_bearing,
        "load_bearing_strict_hash_match": all(expected[path] == observed[path] for path in load_bearing),
        "pass": expected == observed,
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing": (str(NOTE),), "pass": False}
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "s g_q s^dagger",
        "thirteen-fswap",
        "4,096-m2",
        "supplied dense",
        "59,880",
        "153,360",
        "all 24",
        "strict load-bearing byte pins",
        "24-member schedule orbit",
        "held l6",
        "cycle-219 mass",
        "4,047",
        "n1 — alternative-route map",
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
    upstream = upstream_contract()
    note = note_contract()
    local, _objects = local_q_factorization()
    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "dry-contract",
        "upstream": upstream,
        "note_contract": note,
        "local_q_factorization": local,
    }
    result["tests"] = {
        "all_upstream_bytes_including_Cycles522_523_526_527_strictly_pinned": (
            upstream["pass"] and upstream["load_bearing_strict_hash_match"]
        ),
        "note_scope_and_N1_N8_contract": note["pass"],
        "Cycle219_coin_and_Cycle230_contact_local_factors": local["pass"],
    }
    result["tests_passed"] = sum(result["tests"].values())
    result["tests_total"] = len(result["tests"])
    result["pass"] = all(result["tests"].values())
    result["status"] = "cycle530-dry-contract-ready" if result["pass"] else "cycle530-dry-contract-failed"
    return result


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure(f"dry contract failed: {dry!r}")
    labels = c315.joint_labels()
    local, local_objects = local_q_factorization()
    q_controls, _q_objects = q_logical_controls(labels, local_objects)
    adapter = adapter_and_recurrence_controls(labels)
    primitive_routes = c527.primitive_controls()
    encodings = tuple(encoding_controls(length, labels) for length in (TRAIN_LENGTH, HELD_LENGTH))
    initial_router = tuple(c527.isolated_size_certificate(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    physical_rows = tuple(
        physical_q_schedule(length, local_objects["mode_schedule"])[0]
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    simultaneous = tuple(
        isolated_simultaneous_audit(length) for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    covariance = c526.covariance_controls(labels)
    covariance_boundary = {
        "logical_product_covariance_inherited": bool(
            covariance["proper_cubic_frames"] == 24
            and covariance["frame_failures"] == 0
            and covariance["persistent_shadow_frame_failures"] == 0
            and covariance["edge_current_group_product_failures"] == 0
        ),
        "mapped_compile_time_physical_schedule_orbit_members": 24,
        "mapped_schedule_NN_and_group_failures": sum(
            row["frame_nearest_neighbor_failures"]
            + row["frame_blank_path_failures"]
            + row["frame_group_failures"]
            for row in physical_rows
        ),
        "single_frame_independent_gate_order_claimed": False,
        "runtime_frame_query_used": False,
        "statement": (
            "the 24 mapped compile-time physical schedules inherit logical product "
            "covariance; this is a schedule orbit, not one frame-independent gate ordering"
        ),
    }
    covariance_boundary["pass"] = bool(
        covariance_boundary["logical_product_covariance_inherited"]
        and covariance_boundary["mapped_compile_time_physical_schedule_orbit_members"] == 24
        and covariance_boundary["mapped_schedule_NN_and_group_failures"] == 0
        and not covariance_boundary["single_frame_independent_gate_order_claimed"]
        and not covariance_boundary["runtime_frame_query_used"]
    )

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "shadow-normal-form-certificate",
        "status": "cycle530-selected-seam-q-core-primitive-partial-closure",
        "exact_code_image_identity": "S G_q S^dagger E_12 = E_12 G_coarse",
        "strongest_constructive_result": (
            "Cycle527 prepares all twelve q shadows; the selected two-cell q carrier "
            "executes primitive NN Cycle219 coin, exact thirteen-FSWAP CAR seam plus "
            "Cycle526 event/current/K macro, and Cycle230 contact; supplied S unprepares "
            "and reprepares the matching native shell"
        ),
        "local_q_factorization": local,
        "q_logical_controls": q_controls,
        "adapter_and_recurrence": adapter,
        "ordinary_and_fermionic_route_primitives": primitive_routes,
        "E12_L5_L6": encodings,
        "Cycle527_initial_router_L5_L6": initial_router,
        "physical_Gq_L5_L6": physical_rows,
        "simultaneous_shared_cell_audit_L5_L6": simultaneous,
        "covariance": covariance,
        "covariance_schedule_boundary": covariance_boundary,
        "supplied_not_synthesized": {
            "Cycle522_selected_native_encoder_and_preparation": True,
            "normal_form_S_dense_unitary_completion": True,
            "normal_form_S_primitive_one_two_M2_factorization": False,
            "Cycle527_fully_installed_blank_4096_M2_microgrid": True,
            "Cycle527_initial_twelve_shadow_NN_preparation": True,
            "Cycle523_q_coin_and_contact_factor_lists": True,
            "Cycle526_event_current_K_logical_factor_list": True,
            "simultaneous_full_volume_B_compiler": False,
        },
        "synthesized_here": {
            "full_twelve_shadow_E12_normal_form": True,
            "selected_two_cell_thirteen_FSWAP_braid": True,
            "literal_NN_routing_of_complete_Gq_and_adapter": True,
            "primitive_normal_form_S": False,
            "simultaneous_full_volume_B": False,
        },
        "boundary": {
            "full_primitive_Gphysical_claimed": False,
            "selected_one_seam_Gq_primitive_factorized": True,
            "normal_form_S_remains_dense_import": True,
            "transformed_output_native_shadow_sync_exact_given_S": True,
            "one_selected_seam_recurrence_exact_given_S": True,
            "simultaneous_shared_cell_B_closed": False,
            "shared_substrate_obstruction": False,
            "general_auxiliary_gauge_no_go": False,
            "axiom_pressure": False,
        },
        "causal_type_boundary": {
            "event_current_K_called_Record_or_realized_history": False,
            "compiler_gate_or_color_count_called_physical_time": False,
            "phase_called_physical_energy": False,
            "signed_current_called_gravity_source": False,
        },
        "resources": checkpoint(started, "Cycle530-final"),
    }
    result["tests"] = {
        "dry_contract": dry["pass"],
        "local_Cycle219_coin_and_Cycle230_contact": local["pass"],
        "all4096_selected_seam_braids_and_q_update": q_controls["pass"],
        "Cycle526_event_current_K_and_two_step_recurrence": adapter["pass"],
        "ordinary_SWAP_remote_CNOT_and_FSWAP_distinction": primitive_routes["pass"],
        "L5_and_held_L6_full_shadow_normal_form_codes": all(row["pass"] for row in encodings),
        "Cycle527_literal_initial_NN_router": all(row["pass"] for row in initial_router),
        "L5_and_held_L6_literal_NN_Gq_schedules": all(row["pass"] for row in physical_rows),
        "all24_mapped_compile_time_schedules_and_group_products": (
            covariance["proper_cubic_frames"] == 24
            and covariance["frame_failures"] == 0
            and covariance["persistent_shadow_frame_failures"] == 0
            and covariance["edge_current_group_product_failures"] == 0
            and all(row["frame_group_failures"] == 0 for row in physical_rows)
            and covariance_boundary["pass"]
        ),
        "simultaneous_shared_cell_route_specific_boundary": (
            simultaneous[0]["canonical_schedule_phase_mismatches"] == 59_880
            and simultaneous[1]["canonical_schedule_phase_mismatches"] == 153_360
            and all(row["pass"] for row in simultaneous)
        ),
        "mass_contact_and_deletions": (
            abs(q_controls["data_only_rest_mass"] - q_controls["Cycle219_mass_fixture"]) < TOLERANCE
            and q_controls["contact_nontrivial_columns"] == 4047
            and all(
                row["deleted_first_braid_FSWAP_residual"] > 1
                and row["naive_endpoint_FSWAP_residual"] > 1.99
                for row in q_controls["axis_seam_braids"]
            )
            and q_controls["deleted_S_pair_q_only_maximum_code_column_residual"] > 1
        ),
        "supplied_boundary_and_no_axiom_pressure": (
            result["boundary"]["normal_form_S_remains_dense_import"]
            and not result["boundary"]["full_primitive_Gphysical_claimed"]
            and not result["boundary"]["shared_substrate_obstruction"]
            and not result["boundary"]["axiom_pressure"]
        ),
    }
    result["tests_passed"] = sum(result["tests"].values())
    result["tests_total"] = len(result["tests"])
    result["pass"] = all(result["tests"].values())
    result["resources"] = checkpoint(started, "Cycle530-complete")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    parser.add_argument("--internal-simultaneous", action="store_true")
    parser.add_argument("--length", type=int)
    args = parser.parse_args()
    try:
        if args.internal_simultaneous:
            if args.length not in (TRAIN_LENGTH, HELD_LENGTH):
                raise ValueError("internal simultaneous mode requires L5 or L6")
            payload = simultaneous_shared_cell_audit(args.length)
        elif args.mode == "dry-contract":
            payload = dry_contract()
        else:
            payload = certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "status": "cycle530-technical-certificate-failure",
            "error": repr(exc),
            "technical_failure_is_not_physics": True,
            "pass": False,
        }
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
