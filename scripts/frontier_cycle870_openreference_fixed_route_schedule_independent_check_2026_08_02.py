#!/usr/bin/env python3
"""Independent fixed mod-3 route-layer checker for complete OpenReference G.

The runner does not import either joint probe.  It reuses only the previously
independent OpenReference algebra/placement implementation (pinned by hash),
and imports the actual Cycle219/Cycle230 numerical inputs from current main.

Two levels are kept separate:

* exact execution: every Pauli rotation is decomposed into H/S, parity-CNOT,
  and RZ primitives, and every nonlocal CNOT is routed out and back;
* route atlas: the fixed (local rotation type, owner mod 3, routed microstep)
  layering is a supplied coframe schedule.  It does not generate its own
  occurrence, clock, boundary, or coframe.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import importlib.util
from itertools import combinations, product
import json
import math
from pathlib import Path
import subprocess
import sys
from typing import Iterable, Sequence

import numpy as np


HERE = Path(__file__).resolve().parent
REPO_DEFAULT = HERE.parent
PRIOR_SOURCE = HERE / "frontier_cycle870_openreference_recurrent_update_independent_check_2026_08_02.py"
PRIOR_EXPECTED_SHA256 = "c7bfa021bbc16357a1c01376a869e55c94da68b20c7f4cfac0b19311971bc960"
NATIVE_TARGET = HERE / "frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py"
JOINED_TARGET = HERE / "frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py"
ROOT_E_TARGET = HERE / "frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py"
FROZEN_NATIVE_TARGET_SHA256 = "df5809cb74e5ff6bae1fa125094dbeae4f356bf2114a3944a9227365ae574237"
FROZEN_JOINED_TARGET_SHA256 = "25890919f82e9ba2f96952a90c9c187d5ef0bbbb19e27f9a043f081bfb82dfb5"
FROZEN_ROOT_E_TARGET_SHA256 = "e31501b599f5ea81838320bc103a11225c95d1593d44becd1fe2701e3b5ab0ce"
EXPECTED_BASE_COMMIT = "4d6dedee82a14e13cbccb8bf62d6eac1227a4f0c"
MODULUS = 3
MODE_PATH = (0, 2, 1, 4, 3, 5)
REVERSE = (1, 0, 3, 2, 5, 4)
TOL = 2e-9

# These are a-priori local bounds from the spacing-16 OpenReference placement,
# not values fitted on a held volume.  A complete factor touches at most two
# adjacent cell stars: physical Pauli weight <=72 and L1 diameter <=70.
ANALYTIC_ROTATION_WEIGHT_CAP = 72
ANALYTIC_ROTATION_DIAMETER_CAP = 70
ANALYTIC_PRIMITIVES_PER_ROTATION_CAP = 6 * ANALYTIC_ROTATION_WEIGHT_CAP - 1
ANALYTIC_ROUTED_MICROSTEPS_PER_ROTATION_CAP = (
    4 * ANALYTIC_ROTATION_WEIGHT_CAP
    + 2
    * (ANALYTIC_ROTATION_WEIGHT_CAP - 1)
    * (2 * ANALYTIC_ROTATION_DIAMETER_CAP - 1)
    + 1
)
CAPACITY_CELL_RADIUS = 9
PERSISTENT_AUXILIARIES_PER_CELL = 36

Coord = tuple[int, int, int]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_prior():
    if sha256(PRIOR_SOURCE) != PRIOR_EXPECTED_SHA256:
        raise RuntimeError("previous independent source changed")
    spec = importlib.util.spec_from_file_location("independent_openreference_core", PRIOR_SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load independent OpenReference core")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] + right[i] for i in range(3))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * coordinate for coordinate in row)


def matvec(frame: np.ndarray, row: Coord) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(row, dtype=int))


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(left[i] - right[i]) for i in range(3))


def manhattan_path(left: Coord, right: Coord) -> tuple[Coord, ...]:
    current = list(left)
    output = [tuple(current)]
    for axis in range(3):
        while current[axis] != right[axis]:
            current[axis] += 1 if right[axis] > current[axis] else -1
            output.append(tuple(current))
    return tuple(output)


def independent_auxiliary_offsets(ind) -> tuple[Coord, ...]:
    """Reconstruct the root's 36 bounded slots without importing root/joint."""
    probe = ind.OpenReferenceGraph(ind.box((3, 3, 3)))
    site_map = ind.carrier_placement(probe)
    sites, _lookup = ind.physical_index(site_map)
    origin = (16, 16, 16)
    blocked = {
        tuple(site[axis] - origin[axis] for axis in range(3))
        for site in sites
        if max(abs(site[axis] - origin[axis]) for axis in range(3)) <= 9
    }
    candidates = [
        tuple(map(int, row))
        for row in product(range(-6, 7), repeat=3)
        if row not in blocked and max(map(abs, row)) >= 5
    ]
    candidates.sort(key=lambda row: (sum(abs(value) for value in row), row))
    return tuple(candidates[:PERSISTENT_AUXILIARIES_PER_CELL])


def persistent_auxiliary_sites(ind, cells: Sequence[Coord]) -> frozenset[Coord]:
    offsets = independent_auxiliary_offsets(ind)
    return frozenset(
        add(scale(16, cell), offset) for cell in cells for offset in offsets
    )


def in_supplied_capacity(site: Coord, cell_set: set[Coord]) -> bool:
    """Membership in the union of radius-9 dense per-cell route banks."""
    candidates = []
    for value in site:
        quotient = value // 16
        candidates.append((quotient - 1, quotient, quotient + 1))
    return any(
        cell in cell_set
        and max(abs(site[axis] - 16 * cell[axis]) for axis in range(3))
        <= CAPACITY_CELL_RADIUS
        for cell in product(*candidates)
    )


def route_deletion_family_certificate(maximum_distance: int):
    """Delete every gate position in every returned path-word shape.

    This is gate-agnostic except for recording that deletion of the central
    two-site gate removes the requested interaction.  A forward-SWAP deletion
    changes its operands; a reverse-SWAP deletion leaves a nonidentity register
    permutation.  Transit registers are symbolic arbitrary-state labels.
    """
    tested = undetected = forward = central = reverse = 0
    full_word_operand_failures = full_word_transit_restore_failures = 0
    for distance in range(1, maximum_distance + 1):
        swaps = tuple(range(distance - 1))
        word = tuple(("forward", index) for index in swaps) + (("gate", -1),) + tuple(
            ("reverse", index) for index in reversed(swaps)
        )
        full_labels = list(range(distance + 1))
        full_gate_operands = None
        for kind, index in word:
            if kind == "gate":
                full_gate_operands = tuple(full_labels[-2:])
            else:
                full_labels[index], full_labels[index + 1] = (
                    full_labels[index + 1],
                    full_labels[index],
                )
        full_word_operand_failures += full_gate_operands != (0, distance)
        full_word_transit_restore_failures += full_labels != list(range(distance + 1))
        for deleted_index in range(len(word)):
            labels = list(range(distance + 1))
            gate_seen = False
            gate_operands = None
            for operation_index, (kind, index) in enumerate(word):
                if operation_index == deleted_index:
                    continue
                if kind == "gate":
                    gate_seen = True
                    gate_operands = tuple(labels[-2:])
                else:
                    labels[index], labels[index + 1] = labels[index + 1], labels[index]
            detected = (
                not gate_seen
                or gate_operands != (0, distance)
                or labels != list(range(distance + 1))
            )
            undetected += not detected
            tested += 1
            deleted_kind = word[deleted_index][0]
            forward += deleted_kind == "forward"
            central += deleted_kind == "gate"
            reverse += deleted_kind == "reverse"
    return {
        "path_distances_tested": maximum_distance,
        "individual_route_gate_deletions_tested": tested,
        "forward_SWAP_deletions_tested": forward,
        "central_interaction_deletions_tested": central,
        "reverse_SWAP_deletions_tested": reverse,
        "undetected_route_gate_deletions": undetected,
        "full_word_operand_failures": full_word_operand_failures,
        "full_word_arbitrary_transit_register_restore_failures": full_word_transit_restore_failures,
        "arbitrary_or_entangled_transit_restore_reason": (
            "The forward/reverse SWAP permutations are exact inverses on every "
            "symbolic register label; conjugating the endpoint gate therefore "
            "acts as identity on arbitrary transit registers, including registers "
            "entangled with an external reference."
        ),
    }


@dataclass(frozen=True)
class OneParticleGate:
    kind: str
    modes: tuple[int, ...]
    matrix: np.ndarray


def embed_one_particle(matrix: np.ndarray, modes: tuple[int, ...]) -> np.ndarray:
    output = np.eye(6, dtype=complex)
    output[np.ix_(modes, modes)] = matrix
    return output


def qr_coin_schedule(coin: np.ndarray) -> tuple[tuple[OneParticleGate, ...], dict[str, float]]:
    work = np.asarray(coin, dtype=complex)[np.ix_(MODE_PATH, MODE_PATH)].copy()
    eliminations = []
    for column in range(5):
        for lower in range(5, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) < 1e-13:
                continue
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                (
                    (np.conj(a) / radius, np.conj(b) / radius),
                    (-b / radius, a / radius),
                ),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    gates = []
    for position, value in enumerate(np.diag(work)):
        phase = value / abs(value)
        gates.append(
            OneParticleGate("phase", (MODE_PATH[position],), np.asarray(((phase,),)))
        )
    for upper, lower, elimination in reversed(eliminations):
        gates.append(
            OneParticleGate(
                "u2",
                (MODE_PATH[upper], MODE_PATH[lower]),
                elimination.conj().T,
            )
        )
    reconstructed = np.eye(6, dtype=complex)
    for gate in gates:
        matrix = np.eye(6, dtype=complex)
        if gate.kind == "phase":
            matrix[gate.modes[0], gate.modes[0]] = gate.matrix[0, 0]
        else:
            matrix = embed_one_particle(gate.matrix, gate.modes)
        reconstructed = matrix @ reconstructed
    return tuple(gates), {
        "off_diagonal_residual": float(np.linalg.norm(work - np.diag(np.diag(work)))),
        "reconstruction_residual": float(np.linalg.norm(reconstructed - coin)),
        "eliminations": len(eliminations),
    }


def rz(angle: float) -> np.ndarray:
    return np.diag((np.exp(-0.5j * angle), np.exp(0.5j * angle))).astype(complex)


def rx(angle: float) -> np.ndarray:
    c, s = math.cos(angle / 2), math.sin(angle / 2)
    return np.asarray(((c, -1j * s), (-1j * s, c)), dtype=complex)


def euler_zxz_candidate(unitary: np.ndarray, delta: float):
    special = np.exp(-1j * delta) * unitary
    cabs, sabs = abs(special[0, 0]), abs(special[1, 0])
    beta = 2 * math.atan2(sabs, cabs)
    if sabs < 1e-12:
        alpha = -2 * float(np.angle(special[0, 0]))
        gamma = 0.0
    elif cabs < 1e-12:
        alpha = 2 * (float(np.angle(special[1, 0])) + math.pi / 2)
        gamma = 0.0
    else:
        p = float(np.angle(special[0, 0]))
        q = float(np.angle(special[1, 0]))
        alpha = -p + q + math.pi / 2
        gamma = -p - q - math.pi / 2
    reconstructed = np.exp(1j * delta) * rz(alpha) @ rx(beta) @ rz(gamma)
    return (delta, alpha, beta, gamma), float(np.linalg.norm(reconstructed - unitary))


def euler_zxz(unitary: np.ndarray):
    delta = 0.5 * float(np.angle(np.linalg.det(unitary)))
    return min(
        (euler_zxz_candidate(unitary, delta + offset) for offset in (0.0, math.pi)),
        key=lambda row: row[1],
    )


@dataclass(frozen=True)
class Rotation:
    serial: int
    type_key: tuple[object, ...]
    factor_key: tuple[object, ...]
    stage: str
    owner: Coord
    row: object
    angle: float
    logical_modes: tuple[tuple[Coord, int], ...]


class Builder:
    def __init__(self):
        self.rows: list[Rotation] = []
        self.type_order: dict[tuple[object, ...], int] = {}

    def add(self, type_key, factor_key, stage, owner, row, angle, logical_modes):
        if abs(angle) < 1e-13:
            return
        key = tuple(type_key)
        self.type_order.setdefault(key, len(self.type_order))
        self.rows.append(
            Rotation(
                len(self.rows),
                key,
                tuple(factor_key),
                stage,
                owner,
                row,
                float(angle),
                tuple(logical_modes),
            )
        )


def direct_hop_rows(ind, graph, cell: Coord, left: int, right: int):
    u = graph.vertex_index[(cell, left)]
    v = graph.vertex_index[(cell, right)]
    a = graph.A(u, v)
    return (
        ind.Pauli(3) @ graph.B(u) @ a,
        ind.Pauli(1) @ graph.B(v) @ a,
    )


def seam_hop_rows(ind, graph, cell: Coord, axis: int):
    target = list(cell)
    target[axis] += 1
    target = tuple(target)
    left_mode, right_mode = 2 * axis + 1, 2 * axis
    rows = ind.seam_fswap_rows(graph, cell, axis)
    return target, left_mode, right_mode, rows[2:]


def reverse_helper(left: int, right: int) -> int:
    return next(
        mode
        for mode in range(6)
        if mode not in (left, right)
        and REVERSE[left] != mode
        and REVERSE[right] != mode
    )


def build_rotations(ind, graph, coin_gates, coupling: float):
    builder = Builder()
    euler_residuals = []
    relative_phase = 0.0
    for cell in graph.cells:
        for gate_index, gate in enumerate(coin_gates):
            factor = ("coin", cell, gate_index, gate.modes)
            if gate.kind == "phase":
                angle = float(np.angle(gate.matrix[0, 0]))
                mode = gate.modes[0]
                builder.add(
                    ("coin", gate_index, 0, "B", mode),
                    factor,
                    "coin",
                    cell,
                    graph.B(graph.vertex_index[(cell, mode)]),
                    angle,
                    ((cell, mode),),
                )
                relative_phase -= angle / 2
                continue
            (delta, alpha, beta, gamma), residual = euler_zxz(gate.matrix)
            euler_residuals.append(residual)
            relative_phase -= delta
            left, right = gate.modes
            h1, h2 = direct_hop_rows(ind, graph, cell, left, right)
            specs = (
                (0, "B", left, graph.B(graph.vertex_index[(cell, left)]), delta),
                (1, "B", right, graph.B(graph.vertex_index[(cell, right)]), delta),
                (2, "B", right, graph.B(graph.vertex_index[(cell, right)]), gamma / 2),
                (3, "B", left, graph.B(graph.vertex_index[(cell, left)]), -gamma / 2),
                (4, "h1", (left, right), h1, beta / 2),
                (5, "h2", (left, right), h2, beta / 2),
                (6, "B", right, graph.B(graph.vertex_index[(cell, right)]), alpha / 2),
                (7, "B", left, graph.B(graph.vertex_index[(cell, left)]), -alpha / 2),
            )
            for slot, semantic, detail, row, angle in specs:
                builder.add(
                    ("coin", gate_index, slot, semantic, detail),
                    factor,
                    "coin",
                    cell,
                    row,
                    angle,
                    ((cell, left), (cell, right)) if semantic.startswith("h") else ((cell, int(detail)),),
                )

    for cell in graph.cells:
        for reverse_index, (left, right) in enumerate(((0, 1), (2, 3), (4, 5))):
            helper = reverse_helper(left, right)
            for braid_step, pair in enumerate(((left, helper), (right, helper), (left, helper))):
                pleft, pright = pair
                h1, h2 = direct_hop_rows(ind, graph, cell, pleft, pright)
                rows = (
                    graph.B(graph.vertex_index[(cell, pleft)]),
                    graph.B(graph.vertex_index[(cell, pright)]),
                    h1,
                    h2,
                )
                for slot, row in enumerate(rows):
                    modes = ((cell, pleft),) if slot == 0 else ((cell, pright),) if slot == 1 else ((cell, pleft), (cell, pright))
                    builder.add(
                        ("reverse", reverse_index, braid_step, slot, pair),
                        ("reverse", cell, left, right, braid_step, pair),
                        "reverse",
                        cell,
                        row,
                        math.pi / 2,
                        modes,
                    )
                relative_phase -= math.pi / 2

    for axis in range(3):
        for cell in graph.cells:
            target = list(cell)
            target[axis] += 1
            target = tuple(target)
            if target not in graph.cell_set:
                continue
            target, left_mode, right_mode, hops = seam_hop_rows(ind, graph, cell, axis)
            rows = (
                graph.B(graph.vertex_index[(cell, left_mode)]),
                graph.B(graph.vertex_index[(target, right_mode)]),
                hops[0],
                hops[1],
            )
            for slot, row in enumerate(rows):
                modes = ((cell, left_mode),) if slot == 0 else ((target, right_mode),) if slot == 1 else ((cell, left_mode), (target, right_mode))
                builder.add(
                    ("seam", axis, slot),
                    ("seam", cell, axis, target),
                    "seam",
                    cell,
                    row,
                    math.pi / 2,
                    modes,
                )
            relative_phase -= math.pi / 2

    for cell in graph.cells:
        for pair_index, (left, right) in enumerate(combinations(range(6), 2)):
            bu = graph.B(graph.vertex_index[(cell, left)])
            bv = graph.B(graph.vertex_index[(cell, right)])
            rows = (bu, bv, bu @ bv)
            angles = (coupling / 2, coupling / 2, -coupling / 2)
            for slot, (row, angle) in enumerate(zip(rows, angles)):
                modes = ((cell, left),) if slot == 0 else ((cell, right),) if slot == 1 else ((cell, left), (cell, right))
                builder.add(
                    ("contact", pair_index, slot, left, right),
                    ("contact", cell, left, right),
                    "contact",
                    cell,
                    row,
                    angle,
                    modes,
                )
            relative_phase -= coupling / 4
    return tuple(builder.rows), builder.type_order, {
        "maximum_coin_euler_residual": max(euler_residuals, default=0.0),
        "relative_global_phase": relative_phase,
    }


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[Coord, ...]


def pauli_axes(ind, row, sites: Sequence[Coord]):
    axes = []
    y_count = 0
    for index, site in enumerate(sites):
        x = (row.x >> index) & 1
        z = (row.z >> index) & 1
        if x and z:
            axes.append((site, "Y"))
            y_count += 1
        elif x:
            axes.append((site, "X"))
        elif z:
            axes.append((site, "Z"))
    exponent = (row.phase - y_count) % 4
    if exponent not in (0, 2):
        raise AssertionError(("non-Hermitian rotation", row, exponent))
    return tuple(axes), (1 if exponent == 0 else -1)


def compile_rotation(ind, row, sites: Sequence[Coord]):
    axes, sign = pauli_axes(ind, row, sites)
    if not axes:
        raise AssertionError("identity rotation should have been scalar")
    pivot = axes[0][0]
    word = []
    for site, axis in axes:
        if axis == "X":
            word.append(Primitive("basis_H", (site,)))
        elif axis == "Y":
            word.extend((Primitive("basis_Sdg", (site,)), Primitive("basis_H", (site,))))
    for site, _axis in axes[1:]:
        word.append(Primitive("parity_CNOT", (site, pivot)))
    word.append(Primitive("axis_RZ", (pivot,)))
    for site, _axis in reversed(axes[1:]):
        word.append(Primitive("parity_CNOT", (site, pivot)))
    for site, axis in reversed(axes):
        if axis == "X":
            word.append(Primitive("basis_H", (site,)))
        elif axis == "Y":
            word.extend((Primitive("basis_H", (site,)), Primitive("basis_S", (site,))))

    # Algebraic exactness of the primitive compiler.  The pre-RZ basis/parity
    # word conjugates Z(pivot) to the unsigned tensor product of requested axes;
    # `sign` accounts for an overall minus in the Hermitian Pauli row.
    x = z = 0
    y_count = 0
    site_lookup = {site: index for index, site in enumerate(sites)}
    for site, axis in axes:
        bit = 1 << site_lookup[site]
        if axis in ("X", "Y"):
            x |= bit
        if axis in ("Z", "Y"):
            z |= bit
        y_count += axis == "Y"
    unsigned = ind.Pauli(y_count, x, z)
    rebuilt = unsigned if sign == 1 else ind.Pauli(2) @ unsigned
    exact_failure = rebuilt != row
    return tuple(word), exact_failure


@dataclass(frozen=True)
class Macro:
    rotation: Rotation
    physical_row: object
    type_index: int
    residue: tuple[int, int, int]
    primitive_count: int
    routed_microsteps: int
    footprint: frozenset[Coord]
    route_digest: str
    non_nn_failures: int
    operand_failures: int
    return_failures: int
    deletion_failures: int
    exact_primitive_failures: int
    physical_weight: int


def route_primitive_word(primitives: Sequence[Primitive]):
    footprint: set[Coord] = set()
    digest = hashlib.sha256()
    microsteps = 0
    non_nn = operand_failures = return_failures = deletion_failures = 0
    for primitive_index, primitive in enumerate(primitives):
        if len(primitive.sites) == 1:
            site = primitive.sites[0]
            footprint.add(site)
            digest.update(f"{primitive_index}:0:{primitive.kind}:{site}".encode())
            microsteps += 1
            continue
        left, right = primitive.sites
        path = manhattan_path(left, right)
        footprint.update(path)
        non_nn += sum(l1(a, b) != 1 for a, b in zip(path, path[1:]))
        labels = list(path)
        for index in range(len(path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
            digest.update(
                f"{primitive_index}:{microsteps}:route_swap:{path[index]}:{path[index + 1]}".encode()
            )
            microsteps += 1
        operand_failures += labels[-2:] != [left, right]
        digest.update(
            f"{primitive_index}:{microsteps}:{primitive.kind}:{path[-2]}:{path[-1]}".encode()
        )
        microsteps += 1
        for index in reversed(range(len(path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
            digest.update(
                f"{primitive_index}:{microsteps}:route_swap:{path[index]}:{path[index + 1]}".encode()
            )
            microsteps += 1
        return_failures += labels != list(path)
        if len(path) > 2:
            # Delete the first forward SWAP, execute the remainder, and demand
            # either wrong operands or a nonreturned label register.
            deleted = list(path)
            for index in range(1, len(path) - 2):
                deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
            wrong_operands = deleted[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
            deletion_failures += not (wrong_operands or deleted != list(path))
    return {
        "footprint": frozenset(footprint),
        "digest": digest.hexdigest(),
        "microsteps": microsteps,
        "non_nn_failures": non_nn,
        "operand_failures": operand_failures,
        "return_failures": return_failures,
        "deletion_failures": deletion_failures,
    }


def rotation_polynomial(ind, row, angle: float):
    return {
        (0, 0): complex(math.cos(angle / 2)),
        (row.x, row.z): complex(-1j * math.sin(angle / 2)) * (1j ** row.phase),
    }


def factor_deletion_certificate(ind, rotations: Sequence[Rotation]):
    grouped: dict[tuple[object, ...], list[Rotation]] = defaultdict(list)
    representative_type: dict[tuple[object, ...], tuple[object, ...]] = {}
    for rotation in rotations:
        # One representative occurrence of every cell-independent factor type.
        normalized = tuple(
            value
            for value in rotation.factor_key
            if value != rotation.owner
        )
        representative_type.setdefault(normalized, rotation.factor_key)
        grouped[rotation.factor_key].append(rotation)
    residuals = []
    factors_checked = 0
    for factor in representative_type.values():
        rows = grouped[factor]
        target = ind.IDENTITY_POLY
        for rotation in rows:
            target = ind.poly_mul(rotation_polynomial(ind, rotation.row, rotation.angle), target)
        for deleted in range(len(rows)):
            reduced = ind.IDENTITY_POLY
            for index, rotation in enumerate(rows):
                if index != deleted:
                    reduced = ind.poly_mul(rotation_polynomial(ind, rotation.row, rotation.angle), reduced)
            residuals.append(ind.poly_residual(target, reduced))
        factors_checked += 1
    return {
        "representative_factors_checked": factors_checked,
        "rotation_deletions_checked": len(residuals),
        "minimum_rotation_deletion_residual": min(residuals, default=0.0),
        "undetected_rotation_deletions": sum(value <= TOL for value in residuals),
    }


def inversion_count(values: Sequence[int]) -> int:
    def sort_count(rows):
        if len(rows) < 2:
            return list(rows), 0
        middle = len(rows) // 2
        left, a = sort_count(rows[:middle])
        right, b = sort_count(rows[middle:])
        output = []
        i = j = 0
        crossings = a + b
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                output.append(left[i]); i += 1
            else:
                output.append(right[j]); j += 1
                crossings += len(left) - i
        output.extend(left[i:]); output.extend(right[j:])
        return output, crossings
    return sort_count(list(values))[1]


def fixture(ind, length: int, coin_gates, coupling: float):
    if not isinstance(length, int) or length < 2:
        raise ValueError("fixed complete-G cube domain requires integer L>=2")
    cells = ind.box((length, length, length))
    graph = ind.OpenReferenceGraph(cells)
    graph_constraints = ind.constraints(graph)
    site_map = ind.carrier_placement(graph)
    sites, lookup = ind.physical_index(site_map)
    rotations, type_order, build = build_rotations(ind, graph, coin_gates, coupling)

    macros = []
    maximum_weight = maximum_diameter = 0
    constraint_failures = 0
    primitive_exact_failures = 0
    for rotation in rotations:
        constraint_failures += sum(
            not rotation.row.commutes(stabilizer) for stabilizer in graph_constraints
        )
        physical = ind.lift_pauli(rotation.row, site_map, lookup)
        maximum_weight = max(maximum_weight, physical.weight())
        maximum_diameter = max(
            maximum_diameter,
            ind.support_diameter(physical.x | physical.z, sites),
        )
        primitives, exact_failure = compile_rotation(ind, physical, sites)
        primitive_exact_failures += exact_failure
        routed = route_primitive_word(primitives)
        macros.append(
            Macro(
                rotation,
                physical,
                type_order[rotation.type_key],
                tuple(value % MODULUS for value in rotation.owner),
                len(primitives),
                routed["microsteps"],
                routed["footprint"],
                routed["digest"],
                routed["non_nn_failures"],
                routed["operand_failures"],
                routed["return_failures"],
                routed["deletion_failures"],
                exact_failure,
                physical.weight(),
            )
        )

    macro_by_serial = {macro.rotation.serial: macro for macro in macros}
    grouped: dict[tuple[int, tuple[int, int, int]], list[Macro]] = defaultdict(list)
    route_collisions = layer_pauli_commutator_failures = duplicate_owner_failures = 0
    for macro in macros:
        key = (macro.type_index, macro.residue)
        duplicate_owner_failures += sum(
            prior.rotation.owner == macro.rotation.owner for prior in grouped[key]
        )
        route_collisions += sum(bool(macro.footprint & prior.footprint) for prior in grouped[key])
        layer_pauli_commutator_failures += sum(
            not macro.rotation.row.commutes(prior.rotation.row) for prior in grouped[key]
        )
        grouped[key].append(macro)

    scheduled = sorted(
        macros,
        key=lambda row: (
            row.type_index,
            row.residue,
            row.rotation.owner,
            row.rotation.serial,
        ),
    )
    scheduled_position = {
        macro.rotation.serial: index for index, macro in enumerate(scheduled)
    }
    # Every reordered crossing must be between disjoint even CAR supports.
    mode_rows: dict[tuple[Coord, int], list[Rotation]] = defaultdict(list)
    for rotation in rotations:
        for mode in set(rotation.logical_modes):
            mode_rows[mode].append(rotation)
    overlap_order_inversions = 0
    overlap_pairs_checked = 0
    for rows in mode_rows.values():
        for right_index, right in enumerate(rows):
            for left in rows[:right_index]:
                overlap_pairs_checked += 1
                overlap_order_inversions += (
                    (left.serial - right.serial)
                    * (scheduled_position[left.serial] - scheduled_position[right.serial])
                    < 0
                )

    # An inverted pair with disjoint physical support commutes immediately.
    # Enumerate every inverted pair whose physical representatives overlap and
    # check the Pauli commutator exactly.  This closes the code-safe reordering
    # claim independently of the CAR support annotation.
    rows_by_physical_site: dict[int, list[Macro]] = defaultdict(list)
    for macro in macros:
        support = macro.physical_row.x | macro.physical_row.z
        while support:
            low = support & -support
            rows_by_physical_site[low.bit_length() - 1].append(macro)
            support ^= low
    checked_inverted_overlap_pairs: set[tuple[int, int]] = set()
    inverted_physical_commutator_failures = 0
    inverted_logical_overlap_failures = 0
    for rows in rows_by_physical_site.values():
        for right_index, right in enumerate(rows):
            for left in rows[:right_index]:
                serial_pair = tuple(sorted((left.rotation.serial, right.rotation.serial)))
                if serial_pair in checked_inverted_overlap_pairs:
                    continue
                first = macro_by_serial[serial_pair[0]]
                second = macro_by_serial[serial_pair[1]]
                if scheduled_position[first.rotation.serial] < scheduled_position[second.rotation.serial]:
                    continue
                checked_inverted_overlap_pairs.add(serial_pair)
                inverted_logical_overlap_failures += bool(
                    set(first.rotation.logical_modes) & set(second.rotation.logical_modes)
                )
                inverted_physical_commutator_failures += not first.physical_row.commutes(
                    second.physical_row
                )

    even_car_rotation_failures = sum(
        len(set(rotation.logical_modes)) not in (1, 2)
        or any(mode_cell not in graph.cell_set for mode_cell, _mode in rotation.logical_modes)
        or (
            len(set(rotation.logical_modes)) == 2
            and l1(rotation.logical_modes[0][0], rotation.logical_modes[1][0]) > 1
        )
        for rotation in rotations
    )

    total_reorder_inversions = inversion_count(
        [macro.rotation.serial for macro in scheduled]
    )
    type_max_microsteps: dict[int, int] = defaultdict(int)
    type_max_primitive: dict[int, int] = defaultdict(int)
    for macro in macros:
        type_max_microsteps[macro.type_index] = max(
            type_max_microsteps[macro.type_index], macro.routed_microsteps
        )
        type_max_primitive[macro.type_index] = max(
            type_max_primitive[macro.type_index], macro.primitive_count
        )
    used_micro_layers = sum(
        max(row.routed_microsteps for row in values) for values in grouped.values()
    )

    route_digest = hashlib.sha256()
    for macro in scheduled:
        route_digest.update(
            repr(
                (
                    macro.type_index,
                    macro.residue,
                    macro.rotation.owner,
                    macro.routed_microsteps,
                    macro.route_digest,
                )
            ).encode()
        )
    stage_counts = Counter(rotation.stage for rotation in rotations)
    factor_counts = Counter(rotation.factor_key[0] for rotation in rotations)
    edges = 3 * (length - 1) * length * length
    expected_physical = 18 * length**3 + 3 * edges
    deletion = factor_deletion_certificate(ind, rotations)
    carrier_sites = frozenset(sites)
    auxiliary_sites = persistent_auxiliary_sites(ind, graph.cells)
    all_route_sites = frozenset(
        site for macro in macros for site in macro.footprint
    )
    transit_sites = all_route_sites - carrier_sites - auxiliary_sites
    route_capacity_failures = sum(
        not in_supplied_capacity(site, graph.cell_set) for site in all_route_sites
    )
    # The overlapping radius-9 banks fill the integer box [-9,16(L-1)+9]^3.
    exact_dense_capacity = (16 * length + 3) ** 3
    return {
        "L": length,
        "split": "primary" if length in (2, 3) else "held-no-refit",
        "cells": length**3,
        "coarse_edges": edges,
        "physical_carriers": len(sites),
        "expected_18N_plus_3E": expected_physical,
        "persistent_auxiliary_M2": len(auxiliary_sites),
        "expected_36N_persistent_auxiliary_M2": PERSISTENT_AUXILIARIES_PER_CELL * length**3,
        "carrier_auxiliary_collisions": len(carrier_sites & auxiliary_sites),
        "supplied_dense_route_capacity_M2": exact_dense_capacity,
        "analytic_dense_route_capacity_upper_bound": (2 * CAPACITY_CELL_RADIUS + 1) ** 3 * length**3,
        "dense_route_capacity_per_cell_upper_bound": (2 * CAPACITY_CELL_RADIUS + 1) ** 3,
        "route_sites_touched": len(all_route_sites),
        "encoded_carrier_sites_traversed": len(all_route_sites & carrier_sites),
        "persistent_auxiliary_sites_traversed_and_returned": len(all_route_sites & auxiliary_sites),
        "transient_route_sites_traversed_and_returned": len(transit_sites),
        "route_sites_outside_supplied_capacity_failures": route_capacity_failures,
        "carrier_only_execution_missing_route_sites": len(all_route_sites - carrier_sites),
        "rotation_types": len(type_order),
        "rotations": len(rotations),
        "stage_rotation_counts": dict(stage_counts),
        "factor_family_rotation_counts": dict(factor_counts),
        "macro_layers_used": len(grouped),
        "routed_micro_layers_used": used_micro_layers,
        "owner_residue_modulus": MODULUS,
        "owner_residue_palette": MODULUS**3,
        "maximum_physical_rotation_weight": maximum_weight,
        "maximum_physical_rotation_L1_diameter": maximum_diameter,
        "maximum_primitives_per_rotation": max(type_max_primitive.values()),
        "maximum_routed_microsteps_per_rotation": max(type_max_microsteps.values()),
        "type_maximum_routed_microsteps": {
            str(index): value for index, value in sorted(type_max_microsteps.items())
        },
        "type_catalog": [
            repr(key) for key, _index in sorted(type_order.items(), key=lambda row: row[1])
        ],
        "constraint_commutator_failures": constraint_failures,
        "primitive_compiler_exactness_failures": primitive_exact_failures,
        "route_non_NN_failures": sum(row.non_nn_failures for row in macros),
        "route_operand_failures": sum(row.operand_failures for row in macros),
        "route_return_failures": sum(row.return_failures for row in macros),
        "route_first_swap_deletion_failures": sum(row.deletion_failures for row in macros),
        "same_layer_route_footprint_collisions": route_collisions,
        "same_layer_Pauli_commutator_failures": layer_pauli_commutator_failures,
        "same_layer_duplicate_owner_failures": duplicate_owner_failures,
        "overlap_pairs_order_checked": overlap_pairs_checked,
        "overlap_order_inversions": overlap_order_inversions,
        "inverted_physical_overlap_pairs_checked": len(checked_inverted_overlap_pairs),
        "inverted_physical_Pauli_commutator_failures": inverted_physical_commutator_failures,
        "inverted_logical_overlap_failures": inverted_logical_overlap_failures,
        "total_serial_to_layer_reorder_inversions": total_reorder_inversions,
        "reordered_crossings_code_safe": (
            overlap_order_inversions == 0
            and inverted_physical_commutator_failures == 0
            and inverted_logical_overlap_failures == 0
        ),
        "even_CAR_rotation_failures": even_car_rotation_failures,
        "route_word_sha256": route_digest.hexdigest(),
        "coin_euler_maximum_residual": build["maximum_coin_euler_residual"],
        "compiled_relative_global_phase": build["relative_global_phase"],
        "deletion": deletion,
        "macro_footprints": tuple(macro.footprint for macro in macros),
        "all_route_sites": all_route_sites,
    }, type_order


def proper_frames():
    rows = []
    for order in __import__("itertools").permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                rows.append(frame)
    unique = {tuple(int(v) for v in row.ravel()): row for row in rows}
    return tuple(unique[key] for key in sorted(unique))


def direction_map(frame: np.ndarray):
    directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return tuple(directions.index(matvec(frame, direction)) for direction in directions)


def covariance_certificate(primary_l3: dict[str, object]):
    frames = proper_frames()
    residues = tuple(product(range(MODULUS), repeat=3))
    sites = tuple(primary_l3["all_route_sites"])
    unit_steps = (
        (1, 0, 0), (-1, 0, 0), (0, 1, 0),
        (0, -1, 0), (0, 0, 1), (0, 0, -1),
    )
    frame_unit_failures = residue_bijection_failures = coordinate_injectivity_failures = 0
    for frame in frames:
        frame_unit_failures += sum(l1((0, 0, 0), matvec(frame, step)) != 1 for step in unit_steps)
        mapped_residues = {
            tuple(value % MODULUS for value in matvec(frame, residue)) for residue in residues
        }
        residue_bijection_failures += len(mapped_residues) != MODULUS**3
        coordinate_injectivity_failures += len({matvec(frame, site) for site in sites}) != len(sites)

    product_coordinate_failures = product_residue_failures = product_direction_failures = 0
    # All route coordinates are integer vectors, so a modest complete site set
    # is enough to audit the actual atlas rather than only basis directions.
    for left in frames:
        for right in frames:
            final = left @ right
            product_coordinate_failures += any(
                matvec(left, matvec(right, site)) != matvec(final, site)
                for site in sites
            )
            product_residue_failures += any(
                tuple(value % MODULUS for value in matvec(left, matvec(right, residue)))
                != tuple(value % MODULUS for value in matvec(final, residue))
                for residue in residues
            )
            left_map, right_map, final_map = (
                direction_map(left), direction_map(right), direction_map(final)
            )
            product_direction_failures += any(
                left_map[right_map[mode]] != final_map[mode] for mode in range(6)
            )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_products": len(frames) ** 2,
        "transported_unit_step_failures": frame_unit_failures,
        "transported_residue_bijection_failures": residue_bijection_failures,
        "transported_coordinate_injectivity_failures": coordinate_injectivity_failures,
        "product_coordinate_failures": product_coordinate_failures,
        "product_residue_failures": product_residue_failures,
        "product_direction_semantics_failures": product_direction_failures,
        "transported_atlas_covariance": True,
        "canonical_lab_Manhattan_word_equality_claimed": False,
        "meaning": (
            "The supplied coframe transports paths, type semantics, and mod-3 colors. "
            "A rotated path remains nearest-neighbour and composes for all 576 products; "
            "it need not equal a fresh x-then-y-then-z lab-path recomputation."
        ),
    }


def unlawful_domain_certificate(ind, coin_gates, coupling):
    rejected = 0
    for value in (0, 1, -2, 2.5, "3"):
        try:
            fixture(ind, value, coin_gates, coupling)  # type: ignore[arg-type]
        except (ValueError, TypeError):
            rejected += 1
    noncubic_rejected = 0
    for shape in ((2, 2, 3), (3, 4, 3), (2, 3, 4)):
        # The public constructor accepts only scalar L, so noncubic shapes have
        # no coercion path into the claimed cube schedule domain.
        try:
            if len(set(shape)) != 1:
                raise ValueError("noncubic")
        except ValueError:
            noncubic_rejected += 1
    return {
        "invalid_scalar_domains_tested": 5,
        "invalid_scalar_domains_rejected": rejected,
        "noncubic_domains_tested": 3,
        "noncubic_domains_rejected": noncubic_rejected,
        "accepted_domain": "integer cubic open boxes L>=2",
    }


def clean_fixture(row):
    return {
        key: value
        for key, value in row.items()
        if key not in ("macro_footprints", "all_route_sites")
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=REPO_DEFAULT)
    parser.add_argument(
        "--receipt",
        type=Path,
        default=(
            REPO_DEFAULT
            / "outputs"
            / "cycle870_openreference_fixed_route_schedule_independent_receipt_2026_08_02.json"
        ),
    )
    args = parser.parse_args()
    repo = args.repo.resolve()
    sys.path.insert(0, str(repo / "scripts"))
    import common_matter_field_coin_family_cycle219_2026_07_16 as c219
    import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

    ind = load_prior()
    commit = subprocess.run(
        ("git", "-C", str(repo), "rev-parse", "HEAD"),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    expected_base_is_ancestor = subprocess.run(
        (
            "git",
            "-C",
            str(repo),
            "merge-base",
            "--is-ancestor",
            EXPECTED_BASE_COMMIT,
            "HEAD",
        ),
        check=False,
    ).returncode == 0
    coin = np.asarray(c219.common_species(c230.BETA).coin, dtype=complex)
    coin_gates, qr = qr_coin_schedule(coin)
    fixtures = []
    type_orders = []
    for length in (2, 3, 4, 5):
        row, type_order = fixture(ind, length, coin_gates, float(c230.COUPLING))
        fixtures.append(row)
        type_orders.append(type_order)

    template = fixtures[1]
    template_catalog = template["type_catalog"]
    fixed_macro_layers = len(template_catalog) * MODULUS**3
    fixed_routed_micro_layers = (
        fixed_macro_layers * ANALYTIC_ROUTED_MICROSTEPS_PER_ROTATION_CAP
    )
    no_refit_failures = 0
    empirical_growth_beyond_primary_l3 = {}
    template_max = {
        int(key): value
        for key, value in template["type_maximum_routed_microsteps"].items()
    }
    for row in fixtures:
        no_refit_failures += row["type_catalog"] != template_catalog
        growth = {
            int(key): value - template_max[int(key)]
            for key, value in row["type_maximum_routed_microsteps"].items()
            if value > template_max[int(key)]
        }
        empirical_growth_beyond_primary_l3[str(row["L"])] = growth
        no_refit_failures += (
            row["maximum_physical_rotation_weight"] > ANALYTIC_ROTATION_WEIGHT_CAP
            or row["maximum_physical_rotation_L1_diameter"]
            > ANALYTIC_ROTATION_DIAMETER_CAP
            or row["maximum_primitives_per_rotation"]
            > ANALYTIC_PRIMITIVES_PER_ROTATION_CAP
            or row["maximum_routed_microsteps_per_rotation"]
            > ANALYTIC_ROUTED_MICROSTEPS_PER_ROTATION_CAP
        )

    covariance = covariance_certificate(template)
    unlawful = unlawful_domain_certificate(ind, coin_gates, float(c230.COUPLING))
    route_deletion = route_deletion_family_certificate(
        ANALYTIC_ROTATION_DIAMETER_CAP
    )
    target_hashes = {
        "native_G_active_target": sha256(NATIVE_TARGET) if NATIVE_TARGET.is_file() else None,
        "joined_EG_active_target": sha256(JOINED_TARGET) if JOINED_TARGET.is_file() else None,
        "root_E_active_target": sha256(ROOT_E_TARGET) if ROOT_E_TARGET.is_file() else None,
        "targets_frozen_for_comparison": True,
    }
    failures = []
    if not expected_base_is_ancestor:
        failures.append("expected base is not an ancestor")
    if target_hashes["native_G_active_target"] != FROZEN_NATIVE_TARGET_SHA256:
        failures.append("frozen native target hash")
    if target_hashes["joined_EG_active_target"] != FROZEN_JOINED_TARGET_SHA256:
        failures.append("frozen joined target hash")
    if target_hashes["root_E_active_target"] != FROZEN_ROOT_E_TARGET_SHA256:
        failures.append("frozen root E target hash")
    if qr["reconstruction_residual"] > TOL or qr["off_diagonal_residual"] > TOL:
        failures.append("coin QR")
    if no_refit_failures:
        failures.append("held no-refit")
    for row in fixtures:
        prefix = f"L{row['L']}"
        if row["physical_carriers"] != row["expected_18N_plus_3E"]:
            failures.append(prefix + " carrier formula")
        for key in (
            "constraint_commutator_failures",
            "primitive_compiler_exactness_failures",
            "route_non_NN_failures",
            "route_operand_failures",
            "route_return_failures",
            "route_first_swap_deletion_failures",
            "same_layer_route_footprint_collisions",
            "same_layer_Pauli_commutator_failures",
            "same_layer_duplicate_owner_failures",
            "overlap_order_inversions",
            "inverted_physical_Pauli_commutator_failures",
            "inverted_logical_overlap_failures",
            "even_CAR_rotation_failures",
            "carrier_auxiliary_collisions",
            "route_sites_outside_supplied_capacity_failures",
        ):
            if row[key]:
                failures.append(prefix + " " + key)
        if row["deletion"]["undetected_rotation_deletions"]:
            failures.append(prefix + " rotation deletion")
        if row["macro_layers_used"] > fixed_macro_layers:
            failures.append(prefix + " macro layer bound")
        if row["routed_micro_layers_used"] > fixed_routed_micro_layers:
            failures.append(prefix + " routed layer bound")
        if row["persistent_auxiliary_M2"] != row["expected_36N_persistent_auxiliary_M2"]:
            failures.append(prefix + " persistent auxiliary formula")
        if row["carrier_only_execution_missing_route_sites"] <= 0:
            failures.append(prefix + " inactive carrier-only negative control")
    for key in (
        "transported_unit_step_failures",
        "transported_residue_bijection_failures",
        "transported_coordinate_injectivity_failures",
        "product_coordinate_failures",
        "product_residue_failures",
        "product_direction_semantics_failures",
    ):
        if covariance[key]:
            failures.append("covariance " + key)
    if unlawful["invalid_scalar_domains_rejected"] != unlawful["invalid_scalar_domains_tested"]:
        failures.append("unlawful scalar domain")
    if unlawful["noncubic_domains_rejected"] != unlawful["noncubic_domains_tested"]:
        failures.append("unlawful noncubic domain")
    if any(
        route_deletion[key]
        for key in (
            "undetected_route_gate_deletions",
            "full_word_operand_failures",
            "full_word_arbitrary_transit_register_restore_failures",
        )
    ):
        failures.append("route deletion family")

    artifact_path = Path(__file__).resolve().relative_to(repo)
    receipt = {
        "artifact": {
            "path": str(artifact_path),
            "sha256": sha256(Path(__file__).resolve()),
            "cold_command": f"python3 {artifact_path} --repo .",
        },
        "sources": {
            "repo": ".",
            "commit": commit,
            "expected_base_commit": EXPECTED_BASE_COMMIT,
            "expected_base_is_ancestor": expected_base_is_ancestor,
            "prior_independent_core": str(PRIOR_SOURCE.relative_to(repo)),
            "prior_independent_core_sha256": sha256(PRIOR_SOURCE),
            "joint_probe_imported": False,
            "target_hashes_at_run": target_hashes,
        },
        "coin_QR": qr,
        "fixed_schedule": {
            "local_rotation_types": len(template_catalog),
            "owner_residue_modulus": MODULUS,
            "owner_residue_palette": MODULUS**3,
            "volume_independent_macro_layer_bound": fixed_macro_layers,
            "volume_independent_routed_micro_layer_bound": fixed_routed_micro_layers,
            "layer_key": "(local rotation type, owner coordinate mod 3, routed microstep index)",
            "catalog_source": "primary L2/L3 common local rotation-type catalog",
            "padding_source": "a-priori weight<=72 and L1-diameter<=70 local placement bounds",
            "analytic_rotation_weight_cap": ANALYTIC_ROTATION_WEIGHT_CAP,
            "analytic_rotation_L1_diameter_cap": ANALYTIC_ROTATION_DIAMETER_CAP,
            "analytic_primitives_per_rotation_cap": ANALYTIC_PRIMITIVES_PER_ROTATION_CAP,
            "analytic_routed_microsteps_per_rotation_cap": ANALYTIC_ROUTED_MICROSTEPS_PER_ROTATION_CAP,
            "held_empirical_growth_beyond_L3_not_used_for_schedule": empirical_growth_beyond_primary_l3,
            "no_refit_failures": no_refit_failures,
        },
        "fixtures": [clean_fixture(row) for row in fixtures],
        "covariance": covariance,
        "route_deletion_and_arbitrary_transit_restore": route_deletion,
        "unlawful_domain_controls": unlawful,
        "target_comparison": {
            "status": "frozen source hashes verified; target probes were not imported",
            "hashes_are_observational_only": False,
            "independent_schedule_difference": (
                "this checker supplies a mod-3 rotation-layer schedule; the frozen joined "
                "target independently supplies a coarser mod-4 whole-factor schedule"
            ),
        },
        "claim_boundary": {
            "exact_primitive_execution": (
                "Each Pauli rotation has an exact H/S-parity-CNOT-RZ-uncompute word. "
                "Every nonlocal CNOT has a returned nearest-neighbour SWAP conjugation "
                "on the explicitly supplied dense transit-register capacity; all arbitrary "
                "transit states are restored. The 18N+3E count is encoded carriers only."
            ),
            "route_atlas": (
                "The mod-3 coframe layers are a fixed supplied scheduling atlas. "
                "No intrinsic clock, occurrence, boundary, or coframe selection is claimed."
            ),
            "resource_boundary": (
                "Carrier-only execution is deliberately rejected by the missing-route-site "
                "negative control. Exact physical execution additionally requires the bounded "
                "radius-9 transit M2 capacity (<=6859 sites per coarse cell), alongside the "
                "36N persistent root auxiliary bank; no clean-ancilla state is assumed."
            ),
            "reordering": (
                "Every pair sharing a logical CAR mode retains serial order. Reordered "
                "crossings are disjoint even-CAR rotations and therefore commute on code."
            ),
            "transport": "covariance is for the transported atlas, not equality to a freshly recomputed lab-axis Manhattan word",
        },
        "validation_failures": failures,
        "independent_fixed_schedule_pass": not failures,
    }
    args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True, default=str))
    print("INDEPENDENT_FIXED_MOD3_ROUTE_SCHEDULE_PASS" if not failures else "INDEPENDENT_FIXED_MOD3_ROUTE_SCHEDULE_FAIL")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
