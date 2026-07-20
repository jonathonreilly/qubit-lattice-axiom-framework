#!/usr/bin/env python3
"""Cycle 512: fail-closed Route-C Q6 factorized resource scout.

Dry mode binds the packaged Cycle-511 Revision-4 contract and executes only
small preservation, local-unitary, domain, authorization, and resource-model
fixtures.  It performs no joint amplitude evolution.

The separately authorized resource mode is intentionally narrower than a
science row.  It evolves the three rho_AB3 pure components in their frozen
order, keeps matter and the canonical hard-core Q6 occupation state exactly
factorized while the two species have not interacted, and materializes the
canonical packed joint state through the first nontrivial collision layer at
update 2.  It also executes the matched-free update-2 repeat and inverse
fixtures.  No response, occupation field, classifier, state digest, held row,
selector, or refit is emitted.

There is no labeled-mediator substitute: every mediator basis key is the
sorted six-element occupation configuration of the physical 7*L^3 hard-core
mode set.  There is no amplitude pruning.  This implementation has no
reviewed species-Schmidt continuation beyond update 2; consequently even a
successful authorized run is resource-algorithm evidence, not a completed
Cycle-511 sentinel and never science evidence.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
import os
from pathlib import Path
import resource
import sys
import time
from typing import Callable, Iterable

import numpy as np
from scipy.linalg import expm, svd
from scipy.sparse.csgraph import connected_components


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_route_c_response_revision4_preflight_cycle511_2026_07_20 as c511
import physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20 as c510


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "resource-scout")

CYCLE511_RUNNER = ROOT / "scripts/physical_route_c_response_revision4_preflight_cycle511_2026_07_20.py"
CYCLE511_TRANSCRIPT = ROOT / "outputs/physical_route_c_response_revision4_preflight_cycle511_2026_07_20.log"
CYCLE511_RECEIPT = ROOT / "outputs/physical_route_c_response_revision4_preflight_cycle511_receipt_2026_07_20.json"
CYCLE511_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUTE_C_RESPONSE_REVISION4_PREFLIGHT_CYCLE511_NOTE_2026-07-20.md"
CYCLE510_RUNNER = ROOT / "scripts/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.py"

STRICT_FILE_HASHES = {
    CYCLE511_RUNNER: "d80285b0338072dbf3053177c9685c669ed26aa2e7c9fd055b58ecaea963e5b0",
    CYCLE511_TRANSCRIPT: "ed623f427638319184fad61ad7ac0b6de1db2c1a04760a97e4e864dfacb0d4ec",
    CYCLE511_RECEIPT: "a205f8ddd3e3a17c8f8816d9298beb78edb38ff3634a3cea265554ecca77bb36",
    CYCLE511_NOTE: "dc83ba26789ec5409bcc895c1c6616dc39254582af39588a0478b4839eff64dd",
    CYCLE510_RUNNER: "57592ac109321cb273f73b312d205cefc18427329d20c34f18f63d56dcbd5175",
}

EXPECTED_CONTRACT_HASHES = {
    "packet": "c77a770aeae53aa84bfd48a1692ea8f1599ca22f1d3121f6a5aac06cb5e4145c",
    "update": "1f2aff2a0021afa3fd3584d3e460114945d46e59af23e4618f7b7195793ef545",
    "free": "19f170f573833451e8025b70cc0ca8a01bdd75f3f6cbb9bc900900c2eb18f4af",
    "deletion": "00555251b807eb0b8040717f9a77c1c7af485b64317ace2973c299c7fb94520b",
    "boundary": "5436bd18ae02e5fc88a508967094dc95a60e102738048a3730c1ce45867afc26",
    "observable": "c1e36d84110591c225c3c6062ddd8e0dfa7c261bdc4647061225da8b18d30102",
    "occupation_species": "7103fe496547e8c25117347aea7ab5cc0c20e3e5195a81c7571feb20609b6ecf",
    "preservation": "ba9ae4779f05b0f79fd24f3149f2655957ec662ca61ad19e3e475d2cd94c4597",
    "authorization": "b351db1be8de62acdbfacca9cbfa89424705d230f564d5c4bc6cb6358be3d83e",
}
EXPECTED_ROUTE_C8_SHA256 = "bb3ea5f4f6d951ea55071daab10b0417c99bbf8da95497165ecb5c6fd8ba59ef"
EXPECTED_INTACT_ROW_SHA256 = "076f0afe77d36d86d4c3429079be2352005c483776621e2ebb421f1f1a879045"
EXPECTED_CYCLE511_RECEIPT_SCHEMA = "cycle511-route-c-revision4-preflight-receipt-v1"
PACKAGED_PREDECESSOR_COMMIT = "41b5c5ef39869cf0b9b60fa87537031ce8b03970"

SCOUT_AUTHORIZATION_ENV = c511.CYCLE511_SCOUT_AUTHORIZATION_ENV
SCOUT_AUTHORIZATION_TOKEN = c511.CYCLE511_SCOUT_AUTHORIZATION_TOKEN
SCOUT_RUNNER_INTEGRITY_ENV = "CYCLE512_ROUTE_C_Q6_SCOUT_RUNNER_SHA256"
FORBIDDEN_AUTHORIZATION_ENVIRONMENTS = (
    "CYCLE509_SCOUT_AUTHORIZATION",
    "CYCLE509_TRAIN_AUTHORIZATION",
    "CYCLE509_REPLAY_AUTHORIZATION",
    "CYCLE509_HELD_AUTHORIZATION",
    "CYCLE509_SCIENCE_INTEGRITY_SHA256",
    "CYCLE511_SCOUT_AUTHORIZATION",
    "CYCLE511_TRAIN_AUTHORIZATION",
    "CYCLE511_ROUTE_C_TRAIN_AUTHORIZATION",
)
ALL_AUTHORIZATION_ENVIRONMENTS = FORBIDDEN_AUTHORIZATION_ENVIRONMENTS + (
    SCOUT_AUTHORIZATION_ENV,
)

SIDE = 15
CELL_COUNT = SIDE**3
MATTER_MODE_COUNT = 6 * CELL_COUNT
MEDIATOR_MODE_COUNT = 7 * CELL_COUNT
MATTER_NUMBER = 2
MEDIATOR_CHARGE = 6
DEPTH_IMPLEMENTED = 2
FROZEN_TARGET_DEPTH = 5
RESPONSE_WINDOW = (2, 3, 4, 5)
MIDDLE_BETA = -4 * np.pi / 9
CONTACT_COUPLING = 0.37
NUMERIC_CEILING = 1e-8
LOCAL_UNITARY_CEILING = 1e-12
RSS_LIMIT_BYTES = 3_000_000_000
RSS_PREALLOC_ABORT_BYTES = 2_700_000_000
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 100.0
PACKED_ENTRY_ESTIMATE_BYTES = 128
PACK_BITS = 15
PACK_MASK = (1 << PACK_BITS) - 1
PACK_FIELDS = 8
MAX_COLLISION_OUTPUTS_PER_BASIS = 4
SUPPORT_DIAGNOSTIC_CEILING = 1e-14
EXPECTED_UPDATE2_SCHMIDT_RANK = 9
SCHMIDT_RELATIVE_ZERO = 1e-12
SCHMIDT_NINTH_MINIMUM_RELATIVE = 2e-11
SCHMIDT_LOCAL_FACTOR_CEILING = 1e-12
SCHMIDT_QR_CEILING = 1e-11
SCHMIDT_CORE_CEILING = 1e-11
SCHMIDT_PACKED_L2_CEILING = 1e-12
SCHMIDT_PACKED_NINTH_RESOLUTION_FRACTION = 0.1
SCHMIDT_AXIS_SPECTRUM_CEILING = 1e-12
SCHMIDT_NORM_CEILING = 1e-11
EXPECTED_UPDATE2_FACTOR_LABELS = tuple(
    left + right for left, right in product(("I", "D", "X"), repeat=2)
)
EXPECTED_UPDATE2_FACTOR_SUPPORTS = (
    (4911, 729),
    (96, 243),
    (96, 243),
    (96, 243),
    (1, 81),
    (1, 81),
    (96, 243),
    (1, 81),
    (1, 81),
)
EXPECTED_UPDATE2_FACTOR_BASES = (5104, 1296)

# Each tuple is (cell, incoming matter direction, outgoing matter direction,
# incoming mediator slot, outgoing mediator slot).  These are frozen geometry
# fixtures, not state-dependent physical control.
FROZEN_UPDATE2_ACTIVE_SITES = (
    (((4, 7, 7), 1, 0, 1, 2), ((10, 7, 7), 0, 1, 2, 1)),
    (((7, 4, 7), 3, 2, 3, 4), ((7, 10, 7), 2, 3, 4, 3)),
    (((7, 7, 4), 5, 4, 5, 6), ((7, 7, 10), 4, 5, 6, 5)),
)

# These are conservative declarations for one axial pure component under the
# dense Cycle-219 coin and finite CAR stream, before mediator entanglement.
# The matter-pair sequence counts canonical keys reached by the declared
# floating-point expansion without tolerance pruning; it is *not* an analytic
# nonzero-support sequence because coherently cancelling contributions remain
# stored.  Updates 0--2 are checked by the authorized prefix.  Updates 3--5 are
# unexecuted projection inputs only.  Their Cartesian products therefore gate
# one in-core representation plan and say nothing about actual reachable
# post-collision support, physical feasibility, or axiom pressure.
DECLARED_STORED_MATTER_KEYS_BY_UPDATE = (9, 153, 4911, 46425, 229263, 800505)
DECLARED_REACHED_MATTER_MODES_BY_UPDATE = (6, 18, 102, 306, 678, 1266)
DECLARED_UNCOUPLED_MEDIATOR_KEYS_BY_UPDATE = (1, 64, 729, 4096, 15625, 46656)

# Independent support-oracle targets through the actually implemented prefix.
# They are compared to a diagnostic view of the unpruned state; the runner
# never deletes coefficients on the basis of this ceiling.
EXPECTED_DIAGNOSTIC_MATTER_SUPPORT_THROUGH_UPDATE2 = (9, 81, 2169)
EXPECTED_DIAGNOSTIC_MEDIATOR_SUPPORT_THROUGH_UPDATE2 = (1, 64, 729)
EXPECTED_DIAGNOSTIC_PACKED_SUPPORT_AT_UPDATE2 = 1_625_022
EXPECTED_UPDATE2_PACKED_STORED_KEYS = 3_626_856
EXPECTED_UPDATE2_PACKED_MACHINE_NONZERO_VALUES = 1_890_378
EXPECTED_UPDATE2_MATERIALIZATION_LEDGER = {
    "cartesian_inputs": 3_580_119,
    "source_occupied_cell_gate_stages": 7_098_273,
    "actual_local_lookup_calls": 7_121_601,
    "branch_histogram": {1: 3_533_544, 2: 46_494, 4: 81},
    "active_inputs": 46_575,
    "diagonal_contributions": 3_580_119,
    "off_diagonal_contributions": 46_737,
    "generated_contributions": 3_626_856,
    "unique_packed_keys": 3_626_856,
    "packed_key_collisions": 0,
    "maximum_branches": 4,
    "lawful_target_failures": 0,
    "pack_roundtrip_failures": 0,
    "nonfinite_amplitude_failures": 0,
}


MatterPair = tuple[int, int]
MediatorConfiguration = tuple[int, int, int, int, int, int]
MatterRay = dict[MatterPair, complex]
MediatorRay = dict[MediatorConfiguration, complex]
PackedState = dict[int, complex]
Cyclotomic = tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]
ContactTag = dict[int, Cyclotomic]
ExactMatterTags = dict[MatterPair, ContactTag]


class ResourceWall(RuntimeError):
    """A technical resource wall, never a physical or mathematical verdict."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: object) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


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
    if rss >= RSS_PREALLOC_ABORT_BYTES:
        raise ResourceWall(f"RSS preallocation guard reached at {label}: {rss}")
    if rss + projected_bytes >= RSS_PREALLOC_ABORT_BYTES:
        raise ResourceWall(
            f"projected allocation guard reached at {label}: "
            f"rss={rss}, projected={projected_bytes}"
        )
    if swap_count() != 0:
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "estimated_next_allocation_bytes": projected_bytes,
        "allocation_estimate_is_not_measured_RSS": True,
        "process_swap_count": swap_count(),
    }


def cell_linear(cell: tuple[int, int, int]) -> int:
    x, y, z = cell
    if not all(0 <= value < SIDE for value in cell):
        raise ValueError(f"cell outside L15: {cell}")
    return (x * SIDE + y) * SIDE + z


def linear_cell(index: int) -> tuple[int, int, int]:
    if not 0 <= index < CELL_COUNT:
        raise ValueError("cell index outside L15")
    x, rem = divmod(index, SIDE * SIDE)
    y, z = divmod(rem, SIDE)
    return x, y, z


def matter_mode(cell: tuple[int, int, int], direction: int) -> int:
    if not 0 <= direction < 6:
        raise ValueError("matter direction outside six-mode alphabet")
    return 6 * cell_linear(cell) + direction


def decode_matter_mode(index: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(index, 6)
    return linear_cell(cell), direction


def mediator_mode(cell: tuple[int, int, int], slot: int) -> int:
    if not 0 <= slot < 7:
        raise ValueError("mediator slot outside parked-plus-six alphabet")
    return 7 * cell_linear(cell) + slot


def decode_mediator_mode(index: int) -> tuple[tuple[int, int, int], int]:
    cell, slot = divmod(index, 7)
    return linear_cell(cell), slot


def canonical_pair(first: int, second: int) -> tuple[MatterPair, int] | None:
    if first == second:
        return None
    return ((first, second), 1) if first < second else ((second, first), -1)


def canonical_mediator(values: Iterable[int]) -> MediatorConfiguration:
    result = tuple(sorted(int(value) for value in values))
    if len(result) != MEDIATOR_CHARGE or len(set(result)) != MEDIATOR_CHARGE:
        raise ValueError("mediator state violates exact hard-core Q6")
    if result[0] < 0 or result[-1] >= MEDIATOR_MODE_COUNT:
        raise ValueError("mediator mode outside finite L15 alphabet")
    return result  # type: ignore[return-value]


def pack_state(pair: MatterPair, mediator: MediatorConfiguration) -> int:
    values = pair + mediator
    if len(values) != PACK_FIELDS or any(value > PACK_MASK for value in values):
        raise ValueError("packed key width is insufficient")
    key = 0
    for position, value in enumerate(values):
        key |= int(value) << (PACK_BITS * position)
    return key


def unpack_state(key: int) -> tuple[MatterPair, MediatorConfiguration]:
    values = tuple((key >> (PACK_BITS * position)) & PACK_MASK for position in range(PACK_FIELDS))
    pair: MatterPair = (values[0], values[1])
    mediator: MediatorConfiguration = values[2:]  # type: ignore[assignment]
    return pair, mediator


def add_amplitude(target: dict, key: object, value: complex) -> None:
    # No magnitude cutoff and no cancellation pruning are permitted.
    target[key] = target.get(key, 0j) + value


def ray_norm(ray: dict[object, complex]) -> float:
    return float(sum(abs(value) ** 2 for value in ray.values()))


def unpruned_support_diagnostics(ray: dict[object, complex]) -> dict:
    """Describe small cancellation residues without modifying the state."""
    machine_nonzero = 0
    above = 0
    below_squared_norm = 0.0
    maximum_below = 0.0
    nonfinite = 0
    for value in ray.values():
        magnitude = abs(value)
        machine_nonzero += value != 0j
        nonfinite += not (np.isfinite(value.real) and np.isfinite(value.imag))
        if magnitude > SUPPORT_DIAGNOSTIC_CEILING:
            above += 1
        else:
            below_squared_norm += float(magnitude**2)
            maximum_below = max(maximum_below, float(magnitude))
    return {
        "stored_canonical_keys": len(ray),
        "machine_nonzero_values": machine_nonzero,
        "machine_exact_zero_values": len(ray) - machine_nonzero,
        "values_above_diagnostic_ceiling": above,
        "values_at_or_below_diagnostic_ceiling": len(ray) - above,
        "diagnostic_ceiling": SUPPORT_DIAGNOSTIC_CEILING,
        "squared_norm_at_or_below_diagnostic_ceiling": below_squared_norm,
        "maximum_magnitude_at_or_below_diagnostic_ceiling": maximum_below,
        "nonfinite_value_count": nonfinite,
        "state_was_pruned": False,
    }


def ray_residual(left: MatterRay, right: MatterRay) -> float:
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def initial_matter_ray(axis: int) -> MatterRay:
    center = c511.c509.ROUTE_C_TRAIN.probe_center
    output: MatterRay = {}
    for relative_pair, amplitude in c511.packet_component(axis).items():
        values = []
        for relative_cell, direction in relative_pair:
            cell = tuple(center[index] + relative_cell[index] for index in range(3))
            values.append(matter_mode(cell, direction))
        ordered = canonical_pair(values[0], values[1])
        if ordered is None:
            raise RuntimeError("rho_AB3 packet contains a Pauli-forbidden pair")
        pair, sign = ordered
        add_amplitude(output, pair, sign * amplitude)
    return output


def initial_mediator_ray() -> MediatorRay:
    geometry = c511.c509.ROUTE_C_TRAIN
    configuration = canonical_mediator(
        mediator_mode(cell, 0) for cell in geometry.source_cells
    )
    return {configuration: 1 + 0j}


def apply_matter_coin(ray: MatterRay, coin: np.ndarray) -> MatterRay:
    output: MatterRay = {}
    for pair, amplitude in ray.items():
        (left_cell, left_direction), (right_cell, right_direction) = (
            decode_matter_mode(pair[0]), decode_matter_mode(pair[1])
        )
        for left_output in range(6):
            left_value = coin[left_output, left_direction]
            for right_output in range(6):
                right_value = coin[right_output, right_direction]
                ordered = canonical_pair(
                    matter_mode(left_cell, left_output),
                    matter_mode(right_cell, right_output),
                )
                if ordered is None:
                    continue
                target, sign = ordered
                add_amplitude(output, target, amplitude * left_value * right_value * sign)
    return output


def stream_matter_mode(index: int, *, inverse: bool = False) -> int:
    cell, direction = decode_matter_mode(index)
    mapped = (
        c511.finite_inverse_stream_mode(cell, direction, SIDE)
        if inverse else c511.finite_stream_mode(cell, direction, SIDE)
    )
    return matter_mode(*mapped)


def apply_matter_stream(ray: MatterRay, *, inverse: bool = False) -> MatterRay:
    output: MatterRay = {}
    for pair, amplitude in ray.items():
        ordered = canonical_pair(
            stream_matter_mode(pair[0], inverse=inverse),
            stream_matter_mode(pair[1], inverse=inverse),
        )
        if ordered is None:
            raise RuntimeError("finite CAR permutation created duplicate mode")
        target, sign = ordered
        add_amplitude(output, target, sign * amplitude)
    return output


def apply_contact(ray: MatterRay, coupling: float) -> MatterRay:
    phase = np.exp(1j * coupling)
    output: MatterRay = {}
    for pair, amplitude in ray.items():
        left_cell, _left_direction = decode_matter_mode(pair[0])
        right_cell, _right_direction = decode_matter_mode(pair[1])
        output[pair] = amplitude * (phase if left_cell == right_cell else 1)
    return output


def apply_emitters(ray: MediatorRay, angle: float) -> MediatorRay:
    geometry = c511.c509.ROUTE_C_TRAIN
    output = dict(ray)
    cosine, sine = np.cos(angle), np.sin(angle)
    for source, direction in zip(geometry.source_cells, geometry.inward_directions):
        parked = mediator_mode(source, 0)
        active = mediator_mode(source, 1 + direction)
        following: MediatorRay = {}
        for configuration, amplitude in output.items():
            occupied_parked = parked in configuration
            occupied_active = active in configuration
            if occupied_parked == occupied_active:
                add_amplitude(following, configuration, amplitude)
                continue
            old, new = (parked, active) if occupied_parked else (active, parked)
            add_amplitude(following, configuration, cosine * amplitude)
            moved = canonical_mediator(new if value == old else value for value in configuration)
            add_amplitude(following, moved, 1j * sine * amplitude)
        output = following
    return output


def stream_mediator_configuration(
    configuration: MediatorConfiguration, *, inverse: bool = False
) -> MediatorConfiguration:
    result = []
    for index in configuration:
        cell, slot = decode_mediator_mode(index)
        if slot == 0:
            result.append(index)
            continue
        direction = slot - 1
        mapped_cell, mapped_direction = (
            c511.finite_inverse_stream_mode(cell, direction, SIDE)
            if inverse else c511.finite_stream_mode(cell, direction, SIDE)
        )
        result.append(mediator_mode(mapped_cell, 1 + mapped_direction))
    return canonical_mediator(result)


def apply_mediator_stream(ray: MediatorRay, *, inverse: bool = False) -> MediatorRay:
    output: MediatorRay = {}
    for configuration, amplitude in ray.items():
        add_amplitude(
            output,
            stream_mediator_configuration(configuration, inverse=inverse),
            amplitude,
        )
    return output


def local_collision_lookup(
    angle: float,
) -> tuple[Callable[[int, int], tuple[tuple[int, int, complex], ...]], dict]:
    generator, _entries, _axes = c510.collision_generator()
    adjacency = (generator != 0).astype(np.int8).tocsr()
    cache: dict[int, tuple[tuple[int, int, complex], ...]] = {}
    maximum_component = 1
    maximum_unitarity = 0.0

    def lookup(matter_mask: int, mediator_mask: int) -> tuple[tuple[int, int, complex], ...]:
        nonlocal maximum_component, maximum_unitarity
        source = c510.local_index(matter_mask, mediator_mask)
        if source not in cache:
            seen = {source}
            frontier = [source]
            while frontier:
                current = frontier.pop()
                neighbors = adjacency.indices[
                    adjacency.indptr[current]:adjacency.indptr[current + 1]
                ]
                for neighbor_value in neighbors:
                    neighbor = int(neighbor_value)
                    if neighbor not in seen:
                        seen.add(neighbor)
                        frontier.append(neighbor)
            component = tuple(sorted(seen))
            maximum_component = max(maximum_component, len(component))
            if len(component) == 1:
                cache[source] = ((matter_mask, mediator_mask, 1 + 0j),)
            else:
                local_generator = generator[np.ix_(component, component)].toarray()
                unitary = expm(1j * angle * local_generator)
                maximum_unitarity = max(
                    maximum_unitarity,
                    float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(len(component)))),
                )
                for column, local_source in enumerate(component):
                    rows = []
                    for row, local_target in enumerate(component):
                        value = complex(unitary[row, column])
                        if value == 0j:
                            continue
                        target_matter, target_mediator = c510.local_decode(local_target)
                        rows.append((target_matter, target_mediator, value))
                    cache[local_source] = tuple(rows)
        return cache[source]

    controls = {
        "generator_dimension": tuple(generator.shape),
        "generator_nnz": int(generator.nnz),
        "cache": cache,
        "maximum_component_size": lambda: maximum_component,
        "maximum_local_unitarity_residual": lambda: maximum_unitarity,
    }
    return lookup, controls


def local_masks(
    pair: MatterPair, configuration: MediatorConfiguration, cell: tuple[int, int, int]
) -> tuple[int, int]:
    matter_mask = 0
    for index in pair:
        mode_cell, direction = decode_matter_mode(index)
        if mode_cell == cell:
            matter_mask |= 1 << direction
    mediator_mask = 0
    for index in configuration:
        mode_cell, slot = decode_mediator_mode(index)
        if mode_cell == cell:
            mediator_mask |= 1 << slot
    return matter_mask, mediator_mask


def replace_local_masks(
    pair: MatterPair,
    configuration: MediatorConfiguration,
    cell: tuple[int, int, int],
    matter_mask: int,
    mediator_mask: int,
) -> tuple[MatterPair, MediatorConfiguration]:
    matter_values = [
        index for index in pair if decode_matter_mode(index)[0] != cell
    ]
    matter_values.extend(
        matter_mode(cell, direction)
        for direction in range(6)
        if (matter_mask >> direction) & 1
    )
    if len(matter_values) != MATTER_NUMBER:
        raise RuntimeError("local collision changed matter number")
    ordered = canonical_pair(matter_values[0], matter_values[1])
    if ordered is None:
        raise RuntimeError("local collision produced Pauli-forbidden matter state")
    # The local generator already supplies the CAR sign in canonical local
    # direction order.  Because the gate is even and conserves the matter
    # number at this cell, modes in earlier cells contribute two parity
    # crossings and no additional sign.  Canonical reconstruction therefore
    # sorts the target labels without multiplying by the incidental order in
    # which the nonlocal and replacement labels were collected.
    target_pair = tuple(sorted(matter_values))  # type: ignore[assignment]

    mediator_values = [
        index for index in configuration if decode_mediator_mode(index)[0] != cell
    ]
    mediator_values.extend(
        mediator_mode(cell, slot)
        for slot in range(7)
        if (mediator_mask >> slot) & 1
    )
    return target_pair, canonical_mediator(mediator_values)


def collide_basis_state(
    pair: MatterPair,
    configuration: MediatorConfiguration,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    operation_ledger: dict[str, int] | None = None,
) -> tuple[tuple[MatterPair, MediatorConfiguration, complex], ...]:
    cells = tuple(sorted({decode_matter_mode(index)[0] for index in pair}))
    branches = ((pair, configuration, 1 + 0j),)
    for cell in cells:
        following = []
        for branch_pair, branch_configuration, branch_amplitude in branches:
            if operation_ledger is not None:
                operation_ledger["actual_local_lookup_calls"] = (
                    operation_ledger.get("actual_local_lookup_calls", 0) + 1
                )
            matter_mask, mediator_mask = local_masks(
                branch_pair, branch_configuration, cell
            )
            for target_matter, target_mediator, coefficient in lookup(
                matter_mask, mediator_mask
            ):
                target_pair, target_configuration = replace_local_masks(
                    branch_pair,
                    branch_configuration,
                    cell,
                    target_matter,
                    target_mediator,
                )
                following.append(
                    (target_pair, target_configuration, branch_amplitude * coefficient)
                )
        branches = tuple(following)
    if len(branches) > MAX_COLLISION_OUTPUTS_PER_BASIS:
        raise RuntimeError("local collision exceeded frozen N2 maximum branch count")
    return branches


def collision_is_identity_on_product(
    matter: MatterRay,
    mediator: MediatorRay,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
) -> bool:
    for pair in matter:
        for configuration in mediator:
            branches = collide_basis_state(pair, configuration, lookup)
            if branches != ((pair, configuration, 1 + 0j),):
                return False
    return True


def materialize_update2_collision(
    matter: MatterRay,
    mediator: MediatorRay,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    started: float,
    checkpoints: list[dict],
) -> tuple[PackedState, dict]:
    product_count = len(matter) * len(mediator)
    projected = (
        product_count * MAX_COLLISION_OUTPUTS_PER_BASIS * PACKED_ENTRY_ESTIMATE_BYTES
    )
    checkpoints.append(resource_checkpoint(started, "before-update2-joint", projected))
    output: PackedState = {}
    processed = 0
    source_occupied_cell_gate_stages = 0
    operation_ledger = {"actual_local_lookup_calls": 0}
    branch_histogram: defaultdict[int, int] = defaultdict(int)
    active_inputs = 0
    diagonal_contributions = 0
    off_diagonal_contributions = 0
    generated_contributions = 0
    packed_key_collisions = 0
    lawful_target_failures = 0
    pack_roundtrip_failures = 0
    nonfinite_amplitude_failures = 0
    maximum_branches = 0
    for configuration, mediator_amplitude in mediator.items():
        for pair, matter_amplitude in matter.items():
            branches = collide_basis_state(
                pair, configuration, lookup, operation_ledger
            )
            branch_count = len(branches)
            branch_histogram[branch_count] += 1
            active_inputs += branch_count > 1
            maximum_branches = max(maximum_branches, branch_count)
            source_occupied_cell_gate_stages += len(
                {decode_matter_mode(index)[0] for index in pair}
            )
            for target_pair, target_configuration, coefficient in branches:
                generated_contributions += 1
                if target_pair == pair and target_configuration == configuration:
                    diagonal_contributions += 1
                else:
                    off_diagonal_contributions += 1
                streamed = stream_mediator_configuration(target_configuration)
                lawful = (
                    len(target_pair) == MATTER_NUMBER
                    and tuple(sorted(target_pair)) == target_pair
                    and len(set(target_pair)) == MATTER_NUMBER
                    and 0 <= target_pair[0] < target_pair[1] < MATTER_MODE_COUNT
                    and len(streamed) == MEDIATOR_CHARGE
                    and tuple(sorted(streamed)) == streamed
                    and len(set(streamed)) == MEDIATOR_CHARGE
                    and 0 <= streamed[0] <= streamed[-1] < MEDIATOR_MODE_COUNT
                )
                lawful_target_failures += not lawful
                key = pack_state(target_pair, streamed)
                pack_roundtrip_failures += unpack_state(key) != (
                    target_pair,
                    streamed,
                )
                packed_key_collisions += key in output
                value = matter_amplitude * mediator_amplitude * coefficient
                nonfinite_amplitude_failures += not (
                    np.isfinite(value.real) and np.isfinite(value.imag)
                )
                add_amplitude(
                    output,
                    key,
                    value,
                )
            processed += 1
            if processed % 50000 == 0:
                checkpoints.append(resource_checkpoint(started, "during-update2-joint"))
    checkpoints.append(resource_checkpoint(started, "after-update2-joint"))
    ledger = {
        "cartesian_inputs": processed,
        "source_occupied_cell_gate_stages": source_occupied_cell_gate_stages,
        "actual_local_lookup_calls": operation_ledger["actual_local_lookup_calls"],
        "branch_histogram": dict(sorted(branch_histogram.items())),
        "active_inputs": active_inputs,
        "diagonal_contributions": diagonal_contributions,
        "off_diagonal_contributions": off_diagonal_contributions,
        "generated_contributions": generated_contributions,
        "unique_packed_keys": len(output),
        "packed_key_collisions": packed_key_collisions,
        "maximum_branches": maximum_branches,
        "lawful_target_failures": lawful_target_failures,
        "pack_roundtrip_failures": pack_roundtrip_failures,
        "nonfinite_amplitude_failures": nonfinite_amplitude_failures,
    }
    return output, ledger


def apply_matter_factor_term(
    ray: MatterRay,
    site: tuple[tuple[int, int, int], int, int, int, int],
    term: str,
    coefficient: complex,
) -> MatterRay:
    """Apply one restricted I/D/X matter factor without tolerance pruning."""
    cell, incoming, outgoing, _incoming_slot, _outgoing_slot = site
    old = matter_mode(cell, incoming)
    new = matter_mode(cell, outgoing)
    output: MatterRay = {}
    for pair, amplitude in ray.items():
        if term == "I":
            add_amplitude(output, pair, amplitude)
        elif old in pair:
            if term == "D":
                add_amplitude(output, pair, coefficient * amplitude)
            elif term == "X":
                values = list(pair)
                values[values.index(old)] = new
                if len(set(values)) != MATTER_NUMBER:
                    raise RuntimeError("Schmidt matter exchange violated Pauli exclusion")
                # The local lookup coefficient already carries the CAR sign; as
                # in replace_local_masks, the even exchange adds no global sign.
                target: MatterPair = tuple(sorted(values))  # type: ignore[assignment]
                add_amplitude(output, target, coefficient * amplitude)
            else:
                raise ValueError(f"unknown Schmidt matter term {term}")
        elif term not in ("D", "X"):
            raise ValueError(f"unknown Schmidt matter term {term}")
    return output


def apply_mediator_factor_term(
    ray: MediatorRay,
    site: tuple[tuple[int, int, int], int, int, int, int],
    term: str,
) -> MediatorRay:
    """Apply one restricted I/D/X mediator factor without tolerance pruning."""
    cell, _incoming, _outgoing, incoming_slot, outgoing_slot = site
    old = mediator_mode(cell, incoming_slot)
    new = mediator_mode(cell, outgoing_slot)
    output: MediatorRay = {}
    for configuration, amplitude in ray.items():
        if term == "I":
            add_amplitude(output, configuration, amplitude)
        elif old in configuration:
            if term == "D":
                add_amplitude(output, configuration, amplitude)
            elif term == "X":
                values = list(configuration)
                values[values.index(old)] = new
                add_amplitude(output, canonical_mediator(values), amplitude)
            else:
                raise ValueError(f"unknown Schmidt mediator term {term}")
        elif term not in ("D", "X"):
            raise ValueError(f"unknown Schmidt mediator term {term}")
    return output


def factor_column_matrix(rays: tuple[dict, ...]) -> tuple[tuple, np.ndarray]:
    """Retain every stored key and coefficient; do not threshold small values."""
    basis = tuple(sorted(set().union(*(set(ray) for ray in rays))))
    index = {key: position for position, key in enumerate(basis)}
    matrix = np.zeros((len(basis), len(rays)), dtype=np.complex128)
    for column, ray in enumerate(rays):
        for key, value in ray.items():
            matrix[index[key], column] = value
    return basis, matrix


def update2_active_site_audit(
    axis: int,
    matter: MatterRay,
    mediator: MediatorRay,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    angle: float,
) -> dict:
    matter_by_cell: defaultdict[tuple[int, int, int], set[int]] = defaultdict(set)
    mediator_by_cell: defaultdict[tuple[int, int, int], set[int]] = defaultdict(set)
    for pair in matter:
        for mode in pair:
            cell, direction = decode_matter_mode(mode)
            matter_by_cell[cell].add(direction)
    for configuration in mediator:
        for mode in configuration:
            cell, slot = decode_mediator_mode(mode)
            mediator_by_cell[cell].add(slot)

    frozen = FROZEN_UPDATE2_ACTIVE_SITES[axis]
    overlap_cells = tuple(sorted(set(matter_by_cell) & set(mediator_by_cell)))
    local_rows = []
    maximum_formula_residual = 0.0
    for site in frozen:
        cell, incoming, outgoing, incoming_slot, outgoing_slot = site
        rows = lookup(1 << incoming, 1 << incoming_slot)
        diagonal = tuple(
            value
            for target_matter, target_mediator, value in rows
            if target_matter == 1 << incoming
            and target_mediator == 1 << incoming_slot
        )
        exchange = tuple(
            value
            for target_matter, target_mediator, value in rows
            if target_matter == 1 << outgoing
            and target_mediator == 1 << outgoing_slot
        )
        if len(rows) != 2 or len(diagonal) != 1 or len(exchange) != 1:
            raise RuntimeError("frozen update2 collision was not one diagonal plus exchange")
        coefficient_residual = max(
            abs(diagonal[0] - np.cos(angle)),
            abs(exchange[0] - 1j * np.sin(angle)),
            abs(abs(diagonal[0]) ** 2 + abs(exchange[0]) ** 2 - 1),
        )
        maximum_formula_residual = max(maximum_formula_residual, coefficient_residual)
        local_rows.append({
            "cell": cell,
            "incoming_matter_direction": incoming,
            "outgoing_matter_direction": outgoing,
            "incoming_mediator_slot": incoming_slot,
            "outgoing_mediator_slot": outgoing_slot,
            "matter_directions_present": tuple(sorted(matter_by_cell.get(cell, ()))),
            "mediator_slots_present": tuple(sorted(mediator_by_cell.get(cell, ()))),
            "diagonal_coefficient": diagonal[0],
            "exchange_coefficient": exchange[0],
            "local_formula_residual": coefficient_residual,
        })

    pass_geometry = (
        overlap_cells == tuple(site[0] for site in frozen)
        and all(
            row["matter_directions_present"] == (site[1],)
            and row["mediator_slots_present"] == (site[3],)
            and site[2] not in row["matter_directions_present"]
            and site[4] not in row["mediator_slots_present"]
            for row, site in zip(local_rows, frozen)
        )
    )
    return {
        "pass": pass_geometry
        and maximum_formula_residual <= SCHMIDT_LOCAL_FACTOR_CEILING,
        "frozen_not_state_selected": True,
        "overlap_cells": overlap_cells,
        "local_rows": tuple(local_rows),
        "maximum_local_factor_residual": maximum_formula_residual,
    }


def update2_schmidt_factor_fixture(
    axis: int,
    matter: MatterRay,
    mediator: MediatorRay,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    angle: float,
) -> tuple[dict, tuple[tuple, np.ndarray, tuple, np.ndarray]]:
    """Build the unpruned nine-term update2 prefix and its 9x9 Schmidt core."""
    active = update2_active_site_audit(axis, matter, mediator, lookup, angle)
    if not active["pass"]:
        raise RuntimeError("frozen update2 active-cell Schmidt audit failed")

    matter_factors: list[MatterRay] = []
    mediator_factors_pre_stream: list[MediatorRay] = []
    mediator_factors: list[MediatorRay] = []
    factor_rows = []
    for choices in product(("I", "D", "X"), repeat=2):
        matter_factor = matter
        mediator_factor = mediator
        for choice, site, local_row in zip(
            choices, FROZEN_UPDATE2_ACTIVE_SITES[axis], active["local_rows"]
        ):
            coefficient = 1 + 0j
            if choice == "D":
                coefficient = local_row["diagonal_coefficient"] - 1
            elif choice == "X":
                coefficient = local_row["exchange_coefficient"]
            matter_factor = apply_matter_factor_term(
                matter_factor, site, choice, coefficient
            )
            mediator_factor = apply_mediator_factor_term(
                mediator_factor, site, choice
            )
        streamed_factor = apply_mediator_stream(mediator_factor)
        label = "".join(choices)
        matter_factors.append(matter_factor)
        mediator_factors_pre_stream.append(mediator_factor)
        mediator_factors.append(streamed_factor)
        factor_rows.append({
            "label": label,
            "matter_stored_keys": len(matter_factor),
            "matter_machine_nonzero_values": sum(
                value != 0j for value in matter_factor.values()
            ),
            "mediator_stored_keys": len(streamed_factor),
            "mediator_machine_nonzero_values": sum(
                value != 0j for value in streamed_factor.values()
            ),
        })

    matter_basis, x_matrix = factor_column_matrix(tuple(matter_factors))
    mediator_basis_pre, y_matrix_pre = factor_column_matrix(
        tuple(mediator_factors_pre_stream)
    )
    mediator_basis, y_matrix = factor_column_matrix(tuple(mediator_factors))
    qx, rx = np.linalg.qr(x_matrix, mode="reduced")
    qy, ry = np.linalg.qr(y_matrix, mode="reduced")
    core = rx @ ry.T  # amplitude factorization uses transpose, never adjoint
    u, singular_values, vh = svd(
        core, full_matrices=False, lapack_driver="gesdd"
    )
    singular_values_gesvd = svd(
        core, full_matrices=False, compute_uv=False, lapack_driver="gesvd"
    )
    gx = x_matrix.conj().T @ x_matrix
    gy = y_matrix.conj().T @ y_matrix
    gy_pre = y_matrix_pre.conj().T @ y_matrix_pre
    factor_norm = np.sum(gx * gy)
    qr_residual = max(
        float(np.linalg.norm(qx.conj().T @ qx - np.eye(len(matter_factors)))),
        float(np.linalg.norm(qy.conj().T @ qy - np.eye(len(mediator_factors)))),
    )
    core_residual = float(
        np.linalg.norm(core - u @ np.diag(singular_values) @ vh)
    )
    driver_residual = float(
        np.max(np.abs(singular_values - singular_values_gesvd))
    )
    stream_gram_residual = float(np.linalg.norm(gy_pre - gy))
    stream_inverse_residual = max(
        ray_residual(
            pre,
            apply_mediator_stream(streamed, inverse=True),
        )
        for pre, streamed in zip(mediator_factors_pre_stream, mediator_factors)
    )
    stream_duplicate_failures = sum(
        len(pre) != len(streamed)
        for pre, streamed in zip(mediator_factors_pre_stream, mediator_factors)
    )
    rank_threshold = SCHMIDT_RELATIVE_ZERO * singular_values[0]
    numerical_rank = int(np.count_nonzero(singular_values > rank_threshold))
    x_singular_values = svd(
        x_matrix, full_matrices=False, compute_uv=False, lapack_driver="gesdd"
    )
    y_singular_values = svd(
        y_matrix, full_matrices=False, compute_uv=False, lapack_driver="gesdd"
    )
    factor_supports = tuple(
        (row["matter_stored_keys"], row["mediator_stored_keys"])
        for row in factor_rows
    )
    ninth_relative = float(singular_values[-1] / singular_values[0])
    norm_residual = float(abs(factor_norm - 1))
    passed = (
        tuple(row["label"] for row in factor_rows)
        == EXPECTED_UPDATE2_FACTOR_LABELS
        and factor_supports == EXPECTED_UPDATE2_FACTOR_SUPPORTS
        and (len(matter_basis), len(mediator_basis))
        == EXPECTED_UPDATE2_FACTOR_BASES
        and len(mediator_basis_pre) == EXPECTED_UPDATE2_FACTOR_BASES[1]
        and numerical_rank == EXPECTED_UPDATE2_SCHMIDT_RANK
        and np.count_nonzero(x_singular_values > SCHMIDT_RELATIVE_ZERO * x_singular_values[0])
        == EXPECTED_UPDATE2_SCHMIDT_RANK
        and np.count_nonzero(y_singular_values > SCHMIDT_RELATIVE_ZERO * y_singular_values[0])
        == EXPECTED_UPDATE2_SCHMIDT_RANK
        and ninth_relative >= SCHMIDT_NINTH_MINIMUM_RELATIVE
        and norm_residual <= SCHMIDT_NORM_CEILING
        and abs(factor_norm.imag) <= SCHMIDT_NORM_CEILING
        and qr_residual <= SCHMIDT_QR_CEILING
        and core_residual <= SCHMIDT_CORE_CEILING
        and driver_residual <= SCHMIDT_CORE_CEILING
        and stream_gram_residual <= SCHMIDT_LOCAL_FACTOR_CEILING
        and stream_inverse_residual <= SCHMIDT_LOCAL_FACTOR_CEILING
        and stream_duplicate_failures == 0
    )
    report = {
        "pass_before_packed_comparison": passed,
        "active_cell_audit": active,
        "factor_labels": EXPECTED_UPDATE2_FACTOR_LABELS,
        "factor_rows": tuple(factor_rows),
        "factor_count": len(factor_rows),
        "matter_basis_stored_keys": len(matter_basis),
        "mediator_basis_stored_keys": len(mediator_basis),
        "factor_matrix_shapes": {
            "X": x_matrix.shape,
            "Y": y_matrix.shape,
            "core": core.shape,
        },
        "numerical_Schmidt_rank_at_declared_cutoff": numerical_rank,
        "relative_rank_cutoff": SCHMIDT_RELATIVE_ZERO,
        "ninth_to_first_ratio": ninth_relative,
        "singular_values": tuple(float(value) for value in singular_values),
        "secondary_driver_singular_values": tuple(
            float(value) for value in singular_values_gesvd
        ),
        "X_singular_values": tuple(float(value) for value in x_singular_values),
        "Y_singular_values": tuple(float(value) for value in y_singular_values),
        "factor_norm_squared": float(factor_norm.real),
        "factor_norm_imaginary_residual": float(abs(factor_norm.imag)),
        "factor_norm_residual": norm_residual,
        "QR_orthogonality_residual": qr_residual,
        "core_SVD_reconstruction_residual": core_residual,
        "SVD_driver_spectrum_residual": driver_residual,
        "stream_Gram_residual": stream_gram_residual,
        "stream_inverse_residual": stream_inverse_residual,
        "stream_duplicate_failures": stream_duplicate_failures,
        "transpose_not_adjoint": True,
        "magnitude_pruning_used": False,
        "singular_values_truncated": 0,
        "discarded_norm": 0.0,
        "depth5_feasibility_established": False,
    }
    return report, (matter_basis, x_matrix, mediator_basis, y_matrix)


def factor_vs_packed_l2_comparison(
    factor_state: tuple[tuple, np.ndarray, tuple, np.ndarray],
    packed: PackedState,
    started: float,
    checkpoints: list[dict],
    axis: int,
) -> dict:
    matter_basis, x_matrix, mediator_basis, y_matrix = factor_state
    projected_bytes = (
        len(matter_basis) * len(mediator_basis) * np.dtype(np.complex128).itemsize
    )
    checkpoints.append(
        resource_checkpoint(
            started, f"axis{axis}-before-factor-packed-comparison", projected_bytes
        )
    )
    difference = x_matrix @ y_matrix.T
    matter_index = {key: position for position, key in enumerate(matter_basis)}
    mediator_index = {key: position for position, key in enumerate(mediator_basis)}
    outside_stored_keys = 0
    outside_machine_nonzero_values = 0
    outside_squared_norm = 0.0
    for key, amplitude in packed.items():
        pair, configuration = unpack_state(key)
        row = matter_index.get(pair)
        column = mediator_index.get(configuration)
        if row is None or column is None:
            outside_stored_keys += 1
            if amplitude != 0j:
                outside_machine_nonzero_values += 1
                outside_squared_norm += float(abs(amplitude) ** 2)
            continue
        difference[row, column] -= amplitude
    residual = float(
        np.sqrt(float(np.linalg.norm(difference) ** 2) + outside_squared_norm)
    )
    del difference
    checkpoints.append(
        resource_checkpoint(started, f"axis{axis}-after-factor-packed-comparison")
    )
    return {
        "pass": residual <= SCHMIDT_PACKED_L2_CEILING
        and outside_machine_nonzero_values == 0,
        "L2_residual": residual,
        "ceiling": SCHMIDT_PACKED_L2_CEILING,
        "scratch_complex128_bytes": projected_bytes,
        "outside_factor_basis_stored_keys": outside_stored_keys,
        "outside_factor_basis_machine_nonzero_values": outside_machine_nonzero_values,
        "magnitude_pruning_used": False,
    }


def packed_norm(state: PackedState) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def forward_matter_word(ray: MatterRay, coin: np.ndarray) -> MatterRay:
    return apply_contact(
        apply_matter_stream(apply_matter_coin(ray, coin)), CONTACT_COUPLING
    )


def inverse_matter_word(ray: MatterRay, coin: np.ndarray) -> MatterRay:
    return apply_matter_coin(
        apply_matter_stream(apply_contact(ray, -CONTACT_COUPLING), inverse=True),
        coin.conj().T,
    )


def matched_free_controls(axis: int, coin: np.ndarray) -> dict:
    initial = initial_matter_ray(axis)
    first = forward_matter_word(initial, coin)
    final = forward_matter_word(first, coin)
    repeated_first = forward_matter_word(initial, coin)
    repeated = forward_matter_word(repeated_first, coin)
    restored = inverse_matter_word(inverse_matter_word(final, coin), coin)
    return {
        "axis": axis,
        "stored_canonical_keys_by_update": (len(initial), len(first), len(final)),
        "maximum_norm_residual": max(
            abs(ray_norm(initial) - 1),
            abs(ray_norm(first) - 1),
            abs(ray_norm(final) - 1),
        ),
        "repeat_state_residual": ray_residual(final, repeated),
        "inverse_state_residual": ray_residual(initial, restored),
        "mediator_basis_configurations": 1,
        "response_computed": False,
    }


_CYCLOTOMIC_ZERO: Cyclotomic = (Fraction(0),) * 6


def cyclotomic_rational(value: Fraction | int) -> Cyclotomic:
    return (Fraction(value),) + (Fraction(0),) * 5


def cyclotomic_add(left: Cyclotomic, right: Cyclotomic) -> Cyclotomic:
    return tuple(left[index] + right[index] for index in range(6))  # type: ignore[return-value]


def cyclotomic_scale(value: Cyclotomic, scale: Fraction | int) -> Cyclotomic:
    factor = Fraction(scale)
    return tuple(factor * coefficient for coefficient in value)  # type: ignore[return-value]


def cyclotomic_multiply(left: Cyclotomic, right: Cyclotomic) -> Cyclotomic:
    """Multiply in Q(zeta_9), reduced by Phi_9(x)=x^6+x^3+1."""
    coefficients = [Fraction(0) for _ in range(11)]
    for left_power, left_value in enumerate(left):
        if left_value == 0:
            continue
        for right_power, right_value in enumerate(right):
            if right_value != 0:
                coefficients[left_power + right_power] += left_value * right_value
    for power in range(10, 5, -1):
        value = coefficients[power]
        if value == 0:
            continue
        coefficients[power] = Fraction(0)
        coefficients[power - 3] -= value
        coefficients[power - 6] -= value
    return tuple(coefficients[:6])  # type: ignore[return-value]


def exact_relative_coin_entry(output_direction: int, input_direction: int) -> Cyclotomic:
    """Cycle-219 coin with its common scalar phase factored out exactly."""
    reversed_input = c511.REVERSE[input_direction]
    diagonal = int(output_direction == input_direction)
    antipodal = int(output_direction == reversed_input)
    rational = Fraction(1, 3) - Fraction(diagonal + antipodal, 2)
    zeta = Fraction(diagonal - antipodal, 2)
    return (
        rational,
        zeta,
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )


def contact_tag_multiply_cyclotomic(
    tag: ContactTag, factor: Cyclotomic, sign: int = 1
) -> ContactTag:
    output = {}
    for power, value in tag.items():
        multiplied = cyclotomic_multiply(value, factor)
        if multiplied != _CYCLOTOMIC_ZERO:
            output[power] = cyclotomic_scale(multiplied, sign)
    return output


def add_contact_tag(target: ExactMatterTags, pair: MatterPair, tag: ContactTag) -> None:
    """Accumulate exactly while retaining the canonical key even when it cancels."""
    accumulated = target.setdefault(pair, {})
    for power, value in tag.items():
        total = cyclotomic_add(accumulated.get(power, _CYCLOTOMIC_ZERO), value)
        if total == _CYCLOTOMIC_ZERO:
            accumulated.pop(power, None)
        else:
            accumulated[power] = total


def exact_initial_matter_tags(axis: int) -> ExactMatterTags:
    center = c511.c509.ROUTE_C_TRAIN.probe_center
    direction = c511.c210.DIRECTIONS[2 * axis]
    weights = (1, 2, 1)
    offsets = (-1, 0, 1)
    output: ExactMatterTags = {}
    for left_offset, left_weight in zip(offsets, weights):
        left_cell = tuple(
            int(center[index] + left_offset * direction[index]) for index in range(3)
        )
        for right_offset, right_weight in zip(offsets, weights):
            right_cell = tuple(
                int(center[index] + right_offset * direction[index])
                for index in range(3)
            )
            ordered = canonical_pair(
                matter_mode(left_cell, 2 * axis),
                matter_mode(right_cell, 2 * axis + 1),
            )
            if ordered is None:
                raise RuntimeError("exact rho_AB3 tag produced a duplicate matter mode")
            pair, sign = ordered
            coefficient = cyclotomic_rational(
                Fraction(sign * left_weight * right_weight, 6)
            )
            add_contact_tag(output, pair, {0: coefficient})
    return output


def exact_apply_matter_coin_tags(
    ray: ExactMatterTags,
) -> tuple[ExactMatterTags, int]:
    output: ExactMatterTags = {}
    raw_contributions = 0
    for pair, tag in ray.items():
        (left_cell, left_direction), (right_cell, right_direction) = (
            decode_matter_mode(pair[0]),
            decode_matter_mode(pair[1]),
        )
        for left_output in range(6):
            left_factor = exact_relative_coin_entry(left_output, left_direction)
            for right_output in range(6):
                ordered = canonical_pair(
                    matter_mode(left_cell, left_output),
                    matter_mode(right_cell, right_output),
                )
                if ordered is None:
                    continue
                raw_contributions += 1
                target, sign = ordered
                factor = cyclotomic_multiply(
                    left_factor,
                    exact_relative_coin_entry(right_output, right_direction),
                )
                add_contact_tag(
                    output,
                    target,
                    contact_tag_multiply_cyclotomic(tag, factor, sign),
                )
    return output, raw_contributions


def exact_apply_matter_stream_tags(ray: ExactMatterTags) -> ExactMatterTags:
    output: ExactMatterTags = {}
    for pair, tag in ray.items():
        ordered = canonical_pair(
            stream_matter_mode(pair[0]),
            stream_matter_mode(pair[1]),
        )
        if ordered is None:
            raise RuntimeError("exact tag stream produced duplicate matter mode")
        target, sign = ordered
        signed = {
            power: cyclotomic_scale(value, sign) for power, value in tag.items()
        }
        add_contact_tag(output, target, signed)
    return output


def exact_apply_contact_tags(ray: ExactMatterTags) -> ExactMatterTags:
    output: ExactMatterTags = {}
    for pair, tag in ray.items():
        left_cell, _left_direction = decode_matter_mode(pair[0])
        right_cell, _right_direction = decode_matter_mode(pair[1])
        shifted = (
            {power + 1: value for power, value in tag.items()}
            if left_cell == right_cell
            else dict(tag)
        )
        add_contact_tag(output, pair, shifted)
    return output


def exact_forward_matter_tag_word(
    ray: ExactMatterTags,
) -> tuple[ExactMatterTags, int]:
    coined, raw_contributions = exact_apply_matter_coin_tags(ray)
    streamed = exact_apply_matter_stream_tags(coined)
    return exact_apply_contact_tags(streamed), raw_contributions


def exact_tag_support(ray: ExactMatterTags) -> int:
    return sum(bool(tag) for tag in ray.values())


def collision_opportunity_counts(
    ray: ExactMatterTags,
) -> tuple[dict[int, int], int]:
    geometry = c511.c509.ROUTE_C_TRAIN
    modes = []
    for source, direction in zip(geometry.source_cells, geometry.inward_directions):
        collision_cell = tuple(
            int(source[index] + c511.c210.DIRECTIONS[direction, index])
            for index in range(3)
        )
        modes.append(
            (
                matter_mode(collision_cell, c511.REVERSE[direction]),
                matter_mode(collision_cell, direction),
            )
        )
    counts = {0: 0, 1: 0, 2: 0}
    outgoing_only_incidents = 0
    for pair, tag in ray.items():
        if not tag:
            continue
        occupied = set(pair)
        opportunities = sum(
            old in occupied and target not in occupied for old, target in modes
        )
        outgoing_only_incidents += sum(
            target in occupied and old not in occupied for old, target in modes
        )
        if opportunities not in counts:
            raise RuntimeError("N2 exact tag exceeded two collision opportunities")
        counts[opportunities] += 1
    return counts, outgoing_only_incidents


def abstract_collision_output_injectivity() -> bool:
    """Exhaust the local category map used by the update-2 sector count."""
    for opportunity_count in (0, 1, 2):
        seen = set()
        for categories in product(range(3), repeat=opportunity_count):
            incoming = tuple(index for index, value in enumerate(categories) if value == 2)
            for subset_bits in range(1 << len(incoming)):
                flipped = {
                    incoming[index]
                    for index in range(len(incoming))
                    if (subset_bits >> index) & 1
                }
                output_categories = tuple(
                    3 if index in flipped else value
                    for index, value in enumerate(categories)
                )
                signature = (output_categories, tuple(sorted(flipped)))
                if signature in seen:
                    return False
                seen.add(signature)
    return True


def exact_cyclotomic_contact_tag_diagnostic() -> dict:
    rows = []
    for axis in range(3):
        matter0 = exact_initial_matter_tags(axis)
        matter1, raw1 = exact_forward_matter_tag_word(matter0)
        matter2, raw2 = exact_forward_matter_tag_word(matter1)
        stored = (len(matter0), len(matter1), len(matter2))
        analytic = tuple(exact_tag_support(ray) for ray in (matter0, matter1, matter2))
        opportunities, outgoing_only_incidents = collision_opportunity_counts(matter2)
        k0 = opportunities[0] * 729 + opportunities[1] * 486 + opportunities[2] * 324
        k1 = opportunities[1] * 243 + opportunities[2] * 324
        k2 = opportunities[2] * 81
        packed_support = k0 + 2 * k1 + 4 * k2
        rows.append({
            "axis": axis,
            "stored_canonical_keys_through_update2": stored,
            "analytic_nonzero_support_through_update2": analytic,
            "analytic_zero_stored_keys_through_update2": tuple(
                stored[index] - analytic[index] for index in range(3)
            ),
            "raw_coin_contributions_updates1_2": (raw1, raw2),
            "analytic_collision_opportunity_counts": opportunities,
            "outgoing_only_active_mode_incidents": outgoing_only_incidents,
            "analytic_pre_collision_product_support": analytic[-1] * 729,
            "analytic_collision_sectors_k0_k1_k2": (k0, k1, k2),
            "analytic_packed_support_update2": packed_support,
        })
    injective = abstract_collision_output_injectivity()
    passed = (
        all(
            row["stored_canonical_keys_through_update2"]
            == DECLARED_STORED_MATTER_KEYS_BY_UPDATE[:3]
            and row["analytic_nonzero_support_through_update2"]
            == EXPECTED_DIAGNOSTIC_MATTER_SUPPORT_THROUGH_UPDATE2
            and row["raw_coin_contributions_updates1_2"] == (306, 5502)
            and row["analytic_collision_opportunity_counts"]
            == {0: 1990, 1: 178, 2: 1}
            and row["outgoing_only_active_mode_incidents"] == 0
            and row["analytic_collision_sectors_k0_k1_k2"]
            == (1537542, 43578, 81)
            and row["analytic_packed_support_update2"]
            == EXPECTED_DIAGNOSTIC_PACKED_SUPPORT_AT_UPDATE2
            for row in rows
        )
        and injective
    )
    return {
        "pass": passed,
        "coefficient_field": "Q(zeta_9), reduced by Phi_9=x^6+x^3+1",
        "contact_tag": "formal z=exp(i*37/100), polynomial degree at most two",
        "supplied_contact_decimal_interpretation": "0.37 is treated as exact 37/100",
        "analytic_support_theorem_import": (
            "Lindemann-Weierstrass: exp(i*37/100) is transcendental over the "
            "algebraic field Q(zeta_9), so a nonzero formal contact polynomial "
            "cannot vanish at the declared contact phase"
        ),
        "common_Cycle219_scalar_phase_factored": True,
        "analytic_zero_criterion": "every exact contact-polynomial cyclotomic coefficient is zero",
        "collision_output_map_has_constructive_inverse": injective,
        "floating_physical_state_read_or_modified": False,
        "tag_used_to_prune_or_skip_floating_transition": False,
        "discarded_floating_norm": 0.0,
        "rows": tuple(rows),
    }


def evidence_controls() -> dict:
    actual = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    failures = {
        str(path.relative_to(ROOT)): {"expected": expected, "actual": actual[str(path.relative_to(ROOT))]}
        for path, expected in STRICT_FILE_HASHES.items()
        if actual[str(path.relative_to(ROOT))] != expected
    }
    receipt = json.loads(CYCLE511_RECEIPT.read_text(encoding="utf-8"))
    ab34, abheld10, route_c8, held13 = c511.manifests()
    contract_hashes = c511.contract_hashes()
    return {
        "strict_file_hashes": actual,
        "strict_hash_failures": failures,
        "packaged_predecessor_commit": PACKAGED_PREDECESSOR_COMMIT,
        "receipt_schema": receipt.get("schema"),
        "receipt_status": receipt.get("status"),
        "receipt_tests": (receipt.get("tests_passed"), receipt.get("tests_total")),
        "receipt_authority": receipt.get("authority"),
        "receipt_audit": receipt.get("audit"),
        "receipt_zero_execution": {
            "resource_scout": receipt.get("resource_scout_executed"),
            "response_rows": receipt.get("response_rows_executed"),
            "held_rows": receipt.get("held_rows_executed"),
        },
        "contract_hashes": contract_hashes,
        "contract_hashes_match": contract_hashes == EXPECTED_CONTRACT_HASHES,
        "RouteC8_sha256": c511.canonical_sha(route_c8),
        "intact_row_sha256": c511.canonical_sha(route_c8[0]),
        "intact_row_execution_status": route_c8[0]["execution_status"],
        "immutable_AB34_sha256": c511.canonical_sha(ab34),
        "immutable_ABheld10_sha256": c511.canonical_sha(abheld10),
        "atomic_held13_sha256": c511.canonical_sha(held13),
    }


def independent_global_car_hop(
    pair: MatterPair, old: int, new: int
) -> tuple[MatterPair, int] | None:
    """Apply a global two-mode CAR hop without using the local CAR helper."""
    if old not in pair or new in pair:
        return None
    ordered = list(pair)
    annihilation_position = ordered.index(old)
    ordered.pop(annihilation_position)
    creation_position = sum(value < new for value in ordered)
    sign = -1 if (annihilation_position + creation_position) % 2 else 1
    ordered.insert(creation_position, new)
    return tuple(ordered), sign  # type: ignore[return-value]


def global_car_spectator_sign_fixture() -> dict:
    """Compare the local even gate against global CAR ordering in 12 cases."""
    _generator, entries, _axes = c510.collision_generator()
    center = (7, 7, 7)
    spectator_cells = ((7, 7, 6), (7, 7, 8))
    inert = tuple(mediator_mode((0, 0, offset), 0) for offset in range(5))
    rows = []
    generator_sign_failures = 0
    matter_target_failures = 0
    mediator_target_failures = 0
    stream_target_failures = 0
    packed_key_failures = 0
    unpack_failures = 0
    for axis, (forward, reverse) in enumerate(c510.UNORIENTED):
        for orientation, old, new, incoming_slot, outgoing_slot in (
            ("forward", reverse, forward, 1 + forward, 1 + reverse),
            ("Hermitian-conjugate", forward, reverse, 1 + reverse, 1 + forward),
        ):
            for spectator_cell in spectator_cells:
                spectator = matter_mode(spectator_cell, 0)
                source_pair: MatterPair = tuple(
                    sorted((spectator, matter_mode(center, old)))
                )  # type: ignore[assignment]
                expected_hop = independent_global_car_hop(
                    source_pair, matter_mode(center, old), matter_mode(center, new)
                )
                if expected_hop is None:
                    raise RuntimeError("global CAR spectator fixture hop was unlawful")
                expected_pair, expected_sign = expected_hop
                source_mediator: MediatorConfiguration = tuple(
                    sorted(inert + (mediator_mode(center, incoming_slot),))
                )  # type: ignore[assignment]
                expected_mediator: MediatorConfiguration = tuple(
                    sorted(inert + (mediator_mode(center, outgoing_slot),))
                )  # type: ignore[assignment]

                source_local = c510.local_index(
                    1 << old, 1 << incoming_slot
                )
                target_local = c510.local_index(
                    1 << new, 1 << outgoing_slot
                )
                generator_value = entries.get((target_local, source_local), 0j)
                generator_sign_failures += generator_value != expected_sign

                actual_pair, actual_mediator = replace_local_masks(
                    source_pair,
                    source_mediator,
                    center,
                    1 << new,
                    1 << outgoing_slot,
                )
                matter_target_failures += actual_pair != expected_pair
                mediator_target_failures += actual_mediator != expected_mediator

                mediator_direction = outgoing_slot - 1
                moved_cell = tuple(
                    int(
                        center[index]
                        + c511.c210.DIRECTIONS[mediator_direction, index]
                    )
                    for index in range(3)
                )
                expected_streamed: MediatorConfiguration = tuple(
                    sorted(inert + (mediator_mode(moved_cell, outgoing_slot),))
                )  # type: ignore[assignment]
                actual_streamed = stream_mediator_configuration(actual_mediator)
                stream_target_failures += actual_streamed != expected_streamed

                values = expected_pair + expected_streamed
                manual_key = sum(
                    int(value) << (PACK_BITS * position)
                    for position, value in enumerate(values)
                )
                actual_key = pack_state(actual_pair, actual_streamed)
                packed_key_failures += actual_key != manual_key
                unpack_failures += unpack_state(actual_key) != (
                    actual_pair,
                    actual_streamed,
                )
                rows.append({
                    "axis": axis,
                    "orientation": orientation,
                    "spectator_position": (
                        "earlier" if spectator_cell == spectator_cells[0] else "later"
                    ),
                    "independent_global_CAR_sign": expected_sign,
                    "local_generator_value": generator_value,
                    "target_pair": expected_pair,
                    "post_stream_active_mediator_mode": mediator_mode(
                        moved_cell, outgoing_slot
                    ),
                    "packed_key": actual_key,
                })
    failures = {
        "generator_sign": generator_sign_failures,
        "matter_target": matter_target_failures,
        "mediator_target": mediator_target_failures,
        "stream_target": stream_target_failures,
        "packed_key": packed_key_failures,
        "unpack_roundtrip": unpack_failures,
    }
    return {
        "pass": len(rows) == 12 and not any(failures.values()),
        "case_count": len(rows),
        "earlier_spectator_has_two_parity_crossings": True,
        "later_spectator_has_zero_parity_crossings": True,
        "failures": failures,
        "rows": tuple(rows),
    }


def preservation_controls() -> dict:
    generator, entries, axes = c510.collision_generator()
    inherited = c510.preservation_controls(generator)
    sectors = c510.collision_sector_controls(generator, axes)
    generator_hermiticity = float(
        c510.sparse.linalg.norm(generator - generator.conj().T)
    )
    axis_hermiticity = max(
        float(c510.sparse.linalg.norm(block - block.conj().T)) for block in axes
    )
    collision_covariance = c510.collision_covariance(entries)
    finite_stream = c511.finite_stream_controls(SIDE)
    angle = c511.factor_coordinate_controls()[
        "train_and_matched_size_beta_-4pi_over_9"
    ]["emitter_and_collision_angle"]
    lookup, collision_meta = local_collision_lookup(angle)
    for matter_mask in range(64):
        if matter_mask.bit_count() > MATTER_NUMBER:
            continue
        for mediator_mask in range(128):
            if mediator_mask.bit_count() <= MEDIATOR_CHARGE:
                lookup(matter_mask, mediator_mask)
    emitters = tuple(c510.emitter_matrix(direction, angle) for direction in range(6))
    identity = c510.sparse.eye(c510.MEDIATOR_DIMENSION)
    emitter_unitarity = max(
        float(c510.sparse.linalg.norm(emitter.getH() @ emitter - identity))
        for emitter in emitters
    )
    emitter_inverse = max(
        float(
            c510.sparse.linalg.norm(
                c510.emitter_matrix(direction, -angle) @ emitters[direction]
                - identity
            )
        )
        for direction in range(6)
    )
    emitter_covariance = 0.0
    for frame in c511.c210.proper_cubic_frames():
        representation = c510.mediator_frame_matrix(frame)
        mapping = c510.direction_map(frame)
        for direction in range(6):
            emitter_covariance = max(
                emitter_covariance,
                float(
                    c510.sparse.linalg.norm(
                        representation @ emitters[direction] @ representation.T
                        - emitters[mapping[direction]]
                    )
                ),
            )
    packet_norms = tuple(ray_norm(initial_matter_ray(axis)) for axis in range(3))
    return {
        "Cycle219_Cycle230_Cycle501": inherited,
        "collision_sectors": {
            "Q_0_through_6_dimensions": sectors["Q_0_through_6_dimensions"],
            "Q_0_through_6_generator_nnz": sectors["Q_0_through_6_generator_nnz"],
            "Q_0_through_6_total_dimension": sectors[
                "Q_0_through_6_total_dimension"
            ],
            "Q_0_through_6_total_nnz": sectors["Q_0_through_6_total_nnz"],
            "maximum_axis_block_commutator": sectors["maximum_axis_block_commutator"],
        },
        "collision_generator_Hermiticity_residual": generator_hermiticity,
        "collision_axis_block_Hermiticity_maximum": axis_hermiticity,
        "collision_generator_all24_covariance_residual": collision_covariance,
        "local_collision_maximum_connected_component_N_le_2_Q_le_6": collision_meta[
            "maximum_component_size"
        ](),
        "local_collision_maximum_unitarity_residual": collision_meta[
            "maximum_local_unitarity_residual"
        ](),
        "emitter_unitarity_residual": emitter_unitarity,
        "emitter_inverse_residual": emitter_inverse,
        "emitter_all24_carried_covariance_residual": emitter_covariance,
        "packet_component_norms": packet_norms,
        "finite_stream": finite_stream,
        "global_CAR_spectator_sign_fixture": global_car_spectator_sign_fixture(),
    }


def preservation_pass(preservation: dict) -> bool:
    inherited = preservation["Cycle219_Cycle230_Cycle501"]
    stream = preservation["finite_stream"]
    sectors = preservation["collision_sectors"]
    scalars = (
        inherited["contact_identity_N_le_1"],
        inherited["collision_identity_Q_0_generator_residual"],
        inherited["safe_train_one_particle_mass_maximum_residual"],
        inherited["safe_train_coin_unitarity_maximum"],
        inherited["safe_train_coin_all24_covariance_maximum"],
        preservation["emitter_unitarity_residual"],
        preservation["emitter_inverse_residual"],
        preservation["emitter_all24_carried_covariance_residual"],
        preservation["local_collision_maximum_unitarity_residual"],
        preservation["collision_generator_Hermiticity_residual"],
        preservation["collision_axis_block_Hermiticity_maximum"],
        preservation["collision_generator_all24_covariance_residual"],
        sectors["maximum_axis_block_commutator"],
        *preservation["packet_component_norms"],
    )
    return (
        all(np.isfinite(value) for value in scalars)
        and inherited["contact_identity_N_le_1"] <= NUMERIC_CEILING
        and inherited["collision_identity_Q_0_generator_residual"] <= NUMERIC_CEILING
        and inherited["safe_train_one_particle_mass_maximum_residual"] <= NUMERIC_CEILING
        and inherited["safe_train_coin_unitarity_maximum"] <= NUMERIC_CEILING
        and inherited["safe_train_coin_all24_covariance_maximum"] <= 1e-10
        and preservation["emitter_unitarity_residual"] <= LOCAL_UNITARY_CEILING
        and preservation["emitter_inverse_residual"] <= LOCAL_UNITARY_CEILING
        and preservation["emitter_all24_carried_covariance_residual"]
        <= LOCAL_UNITARY_CEILING
        and preservation["collision_generator_Hermiticity_residual"]
        <= LOCAL_UNITARY_CEILING
        and preservation["collision_axis_block_Hermiticity_maximum"]
        <= LOCAL_UNITARY_CEILING
        and preservation["collision_generator_all24_covariance_residual"]
        <= LOCAL_UNITARY_CEILING
        and sectors["Q_0_through_6_dimensions"]
        == [64, 448, 1344, 2240, 2240, 1344, 448]
        and sectors["Q_0_through_6_generator_nnz"]
        == [0, 96, 480, 960, 960, 480, 96]
        and sectors["Q_0_through_6_total_dimension"] == 8128
        and sectors["Q_0_through_6_total_nnz"] == 3072
        and sectors["maximum_axis_block_commutator"] <= LOCAL_UNITARY_CEILING
        and preservation["local_collision_maximum_unitarity_residual"]
        <= LOCAL_UNITARY_CEILING
        and preservation["local_collision_maximum_connected_component_N_le_2_Q_le_6"]
        <= 4
        and max(abs(value - 1) for value in preservation["packet_component_norms"])
        <= NUMERIC_CEILING
        and stream["inverse_failures"] == 0
        and stream["output_duplicate_count"] == 0
        and stream["all24_covariance_failures"] == 0
        and preservation["global_CAR_spectator_sign_fixture"]["pass"]
    )


def dimension_and_algorithm_contract() -> dict:
    joint = comb(MATTER_MODE_COUNT, MATTER_NUMBER) * comb(
        MEDIATOR_MODE_COUNT, MEDIATOR_CHARGE
    )
    product_counts = tuple(
        DECLARED_STORED_MATTER_KEYS_BY_UPDATE[index]
        * DECLARED_UNCOUPLED_MEDIATOR_KEYS_BY_UPDATE[index]
        for index in range(FROZEN_TARGET_DEPTH + 1)
    )
    return {
        "formal": {
            "matter_modes": MATTER_MODE_COUNT,
            "mediator_modes": MEDIATOR_MODE_COUNT,
            "matter_N2_dimension": comb(MATTER_MODE_COUNT, MATTER_NUMBER),
            "mediator_Q6_dimension": comb(MEDIATOR_MODE_COUNT, MEDIATOR_CHARGE),
            "joint_N2_Q6_dimension": joint,
            "dense_complex128_bytes": 16 * joint,
        },
        "counterfactual_no_collision_cartesian_generated_key_reference": {
            "classification": "counterfactual-no-collision-cartesian-generated-key-reference",
            "actual_entangled_update3_propagated": False,
            "matter_reached_modes_by_update": DECLARED_REACHED_MATTER_MODES_BY_UPDATE,
            "matter_stored_keys_by_update": DECLARED_STORED_MATTER_KEYS_BY_UPDATE,
            "uncoupled_Q6_stored_keys_by_update": DECLARED_UNCOUPLED_MEDIATOR_KEYS_BY_UPDATE,
            "uncoupled_cartesian_slots_by_update": product_counts,
            "packed_128B_estimate_by_update": tuple(
                value * PACKED_ENTRY_ESTIMATE_BYTES for value in product_counts
            ),
            "complex128_values_only_bytes_by_update": tuple(
                value * np.dtype(np.complex128).itemsize for value in product_counts
            ),
            "packed_entry_bytes_is_estimate": True,
            "updates_3_through_5_are_unexecuted_declarations": True,
            "lower_bound_on_interacting_continuation": False,
            "upper_bound_on_interacting_continuation": False,
            "bounds_exact_tensorized_algorithm": False,
        },
        "representation": {
            "matter": "canonical ordered two-CAR mode pair with exterior signs",
            "mediator": "canonical sorted six-mode physical hard-core occupation",
            "joint": "120-bit packed canonical key in Python integer",
            "hidden_labeled_mediator": False,
            "amplitude_pruning": False,
            "numerical_rank_compression": False,
            "discarded_norm": 0.0,
        },
        "implemented_unpruned_numerical_depth": DEPTH_IMPLEMENTED,
        "frozen_target_depth": FROZEN_TARGET_DEPTH,
        "continuation": {
            "species_Schmidt_update2_fixture_present": True,
            "species_Schmidt_continuation_beyond_update2_present": False,
            "update2_expected_factor_count": EXPECTED_UPDATE2_SCHMIDT_RANK,
            "update2_expected_factor_bases": EXPECTED_UPDATE2_FACTOR_BASES,
            "update2_relative_rank_cutoff": SCHMIDT_RELATIVE_ZERO,
            "reason_not_attempted_without_new_review": (
                "no reviewed factor-Schmidt continuation beyond update2 is implemented; "
                "the counterfactual no-collision update3 Cartesian reference rejects "
                "only its own full in-core materialization and does not bound an exact "
                "tensorized continuation"
            ),
            "factor_Schmidt_route_status": (
                "implemented-numerical-rank9-update2-fixture-execution-receipt-dependent-depth5-open"
            ),
            "update3_rank_bound_present": False,
            "depth5_feasibility_established": False,
            "resource_failure_is_substrate_obstruction": False,
            "resource_failure_is_axiom_pressure": False,
        },
        "resource_limits": {
            "RSS_bytes": RSS_LIMIT_BYTES,
            "preallocation_abort_bytes": RSS_PREALLOC_ABORT_BYTES,
            "wall_seconds": WALL_LIMIT_SECONDS,
            "swap_count": 0,
        },
        "quarantine": {
            "response_values_emitted": False,
            "occupation_or_bond_field_emitted": False,
            "response_or_state_hash_emitted": False,
            "classifier_emitted": False,
            "held_surface_present": False,
            "selector": False,
            "refit": False,
        },
    }


def resource_authorization_inputs_allowed(
    present: tuple[str, ...],
    values: dict[str, str | None],
    integrity_present: bool,
    integrity_value: str | None,
    current_runner_sha: str,
    frozen_contract_matches: bool,
) -> bool:
    return (
        present == (SCOUT_AUTHORIZATION_ENV,)
        and values.get(SCOUT_AUTHORIZATION_ENV) == SCOUT_AUTHORIZATION_TOKEN
        and integrity_present
        and integrity_value == current_runner_sha
        and frozen_contract_matches
    )


def authorization_decision(mode: str) -> tuple[bool, dict]:
    present = tuple(name for name in ALL_AUTHORIZATION_ENVIRONMENTS if name in os.environ)
    values = {name: os.environ.get(name) for name in present}
    integrity_present = SCOUT_RUNNER_INTEGRITY_ENV in os.environ
    integrity_value = os.environ.get(SCOUT_RUNNER_INTEGRITY_ENV)
    current_runner_sha = file_sha(Path(__file__))
    frozen = c511.authorization_contract()["scout"]
    frozen_contract_matches = (
        frozen["environment"] == SCOUT_AUTHORIZATION_ENV
        and frozen["exact_token"] == SCOUT_AUTHORIZATION_TOKEN
        and frozen["scope"] == "RouteC8 index0 intact L15 middle-beta resource sentinel only"
        and frozen["science_rows"] == 0
        and frozen["response_quarantined"] is True
        and frozen["selector"] is False
        and frozen["refit"] is False
        and frozen["resource_ceiling"]
        == {
            "wall_seconds": int(WALL_LIMIT_SECONDS),
            "RSS_bytes": RSS_LIMIT_BYTES,
            "swap_count": 0,
        }
    )
    if mode == "dry-contract":
        return not present and not integrity_present, {
            "mode": mode,
            "present_authorization_variables": present,
            "runner_integrity_variable_present": integrity_present,
            "presence_even_empty_rejected": True,
            "frozen_Cycle511_scout_contract_matches": frozen_contract_matches,
        }
    allowed = resource_authorization_inputs_allowed(
        present,
        values,
        integrity_present,
        integrity_value,
        current_runner_sha,
        frozen_contract_matches,
    )
    return allowed, {
        "mode": mode,
        "present_authorization_variables": present,
        "runner_integrity_variable_present": integrity_present,
        "runner_integrity_sha256_match": integrity_value == current_runner_sha,
        "current_runner_sha256": current_runner_sha,
        "exact_frozen_Cycle511_scout_token_match": values.get(SCOUT_AUTHORIZATION_ENV)
        == SCOUT_AUTHORIZATION_TOKEN,
        "frozen_Cycle511_scout_contract_matches": frozen_contract_matches,
        "new_execution_scope_or_token_introduced": False,
        "scope": frozen["scope"],
        "implementation_scope": (
            "one hash-bound Cycle512 Q6 update2/numerical-rank9 technical prefix invocation"
        ),
        "science_rows": 0,
        "response_quarantined": True,
        "held_rows": 0,
        "selector": False,
        "refit": False,
    }


def run_dry() -> tuple[dict, int]:
    tests = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        tests.append({"name": name, "passed": bool(condition), "detail": detail})

    authorized, authorization = authorization_decision("dry-contract")
    if not authorized:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "mode": "dry-contract",
            "status": "authorization-rejected",
            "authorization": authorization,
            "large_allocations": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
        }, 2

    evidence = evidence_controls()
    check("strict Cycle511/Cycle510 evidence is exact", not evidence["strict_hash_failures"], evidence)
    check(
        "Cycle511 receipt is the packaged zero-execution preflight",
        evidence["receipt_schema"] == EXPECTED_CYCLE511_RECEIPT_SCHEMA
        and evidence["receipt_status"] == "response-revision4-contract-frozen"
        and evidence["receipt_tests"] == (21, 21)
        and evidence["receipt_authority"] == AUTHORITY
        and evidence["receipt_audit"] == AUDIT
        and evidence["receipt_zero_execution"]
        == {"resource_scout": False, "response_rows": 0, "held_rows": 0},
        evidence["receipt_zero_execution"],
    )
    check(
        "Cycle511 contracts and intact RouteC row are hash locked",
        evidence["contract_hashes_match"]
        and evidence["RouteC8_sha256"] == EXPECTED_ROUTE_C8_SHA256
        and evidence["intact_row_sha256"] == EXPECTED_INTACT_ROW_SHA256
        and evidence["intact_row_execution_status"] == "frozen-unexecuted",
        {
            "contract_hashes": evidence["contract_hashes"],
            "RouteC8_sha256": evidence["RouteC8_sha256"],
            "intact_row_sha256": evidence["intact_row_sha256"],
        },
    )

    dimensions = dimension_and_algorithm_contract()
    projection = dimensions[
        "counterfactual_no_collision_cartesian_generated_key_reference"
    ]
    check(
        "formal sectors are exact and the in-core projection is narrowly classified",
        dimensions["formal"]["matter_N2_dimension"] == 205021125
        and dimensions["formal"]["mediator_Q6_dimension"]
        == 241336295876895845944500
        and dimensions["formal"]["joint_N2_Q6_dimension"]
        == 49479038884014047843368077562500
        and projection["classification"]
        == "counterfactual-no-collision-cartesian-generated-key-reference"
        and projection["uncoupled_cartesian_slots_by_update"][3] == 190156800
        and projection["complex128_values_only_bytes_by_update"][3]
        == 3042508800
        and projection["actual_entangled_update3_propagated"] is False
        and projection["bounds_exact_tensorized_algorithm"] is False,
        dimensions,
    )
    check(
        "engine is canonical Q6, no-prune, depth2, and response quarantined",
        dimensions["representation"]["hidden_labeled_mediator"] is False
        and dimensions["representation"]["amplitude_pruning"] is False
        and dimensions["representation"]["numerical_rank_compression"] is False
        and dimensions["implemented_unpruned_numerical_depth"] == 2
        and not any(dimensions["quarantine"].values()),
        dimensions["representation"],
    )

    exact_tags = exact_cyclotomic_contact_tag_diagnostic()
    check(
        "exact cyclotomic/contact tags certify update2 analytic support without pruning",
        exact_tags["pass"]
        and exact_tags["floating_physical_state_read_or_modified"] is False
        and exact_tags["tag_used_to_prune_or_skip_floating_transition"] is False
        and exact_tags["discarded_floating_norm"] == 0.0,
        exact_tags,
    )

    preservation = preservation_controls()
    check(
        "Cycle511 preservation fixtures pass on the exact supplied coordinates",
        preservation_pass(preservation),
        preservation,
    )
    check(
        "dry authorization is absent and executable decision is fail closed",
        authorization["present_authorization_variables"] == ()
        and authorization["runner_integrity_variable_present"] is False
        and authorization["presence_even_empty_rejected"]
        and authorization["frozen_Cycle511_scout_contract_matches"],
        authorization,
    )
    runner_sha = file_sha(Path(__file__))
    authorization_cases = {
        "absent": resource_authorization_inputs_allowed(
            (), {}, False, None, runner_sha, True
        ),
        "empty_token": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: ""},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
        "wrong_token": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: "wrong"},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
        "missing_integrity": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            False,
            None,
            runner_sha,
            True,
        ),
        "wrong_integrity": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            "wrong",
            runner_sha,
            True,
        ),
        "conflicting_train": resource_authorization_inputs_allowed(
            ("CYCLE511_ROUTE_C_TRAIN_AUTHORIZATION", SCOUT_AUTHORIZATION_ENV),
            {
                "CYCLE511_ROUTE_C_TRAIN_AUTHORIZATION": "anything",
                SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN,
            },
            True,
            runner_sha,
            runner_sha,
            True,
        ),
        "frozen_contract_mismatch": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            runner_sha,
            runner_sha,
            False,
        ),
        "exact_frozen_token_and_integrity": resource_authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
    }
    check(
        "authorization case matrix rejects every weakening and accepts only exact inputs",
        authorization_cases["exact_frozen_token_and_integrity"]
        and not any(
            value
            for key, value in authorization_cases.items()
            if key != "exact_frozen_token_and_integrity"
        ),
        authorization_cases,
    )

    execution = {
        "large_allocations": 0,
        "amplitude_states_evolved": 0,
        "resource_scout_executed": False,
        "response_rows_executed": 0,
        "held_rows_executed": 0,
        "response_values_emitted": 0,
        "state_hashes_emitted": 0,
        "refit_performed": False,
        "exact_symbolic_tag_diagnostic_executed": True,
    }
    check(
        "dry mode evolves zero amplitudes and exposes no science surface",
        all(
            execution[key] in (0, False)
            for key in execution
            if key != "exact_symbolic_tag_diagnostic_executed"
        )
        and execution["exact_symbolic_tag_diagnostic_executed"] is True,
        execution,
    )
    passed = all(row["passed"] for row in tests)
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle512-q6-resource-contract-ready" if passed else "dry-contract-failed",
        "pass": passed,
        "tests_passed": sum(row["passed"] for row in tests),
        "tests_total": len(tests),
        "authorization": authorization,
        "evidence": evidence,
        "dimensions_and_algorithm": dimensions,
        "exact_cyclotomic_contact_tag_diagnostic": exact_tags,
        "preservation": preservation,
        "execution": execution,
        "tests": tests,
    }, 0 if passed else 1


def run_resource_scout() -> tuple[dict, int]:
    allowed, authorization = authorization_decision("resource-scout")
    if not allowed:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "mode": "resource-scout",
            "status": "authorization-rejected",
            "authorization": authorization,
            "resource_invocations": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
        }, 2

    started = time.monotonic()
    checkpoints: list[dict] = []
    evidence = evidence_controls()
    if (
        evidence["strict_hash_failures"]
        or not evidence["contract_hashes_match"]
        or evidence["RouteC8_sha256"] != EXPECTED_ROUTE_C8_SHA256
        or evidence["intact_row_sha256"] != EXPECTED_INTACT_ROW_SHA256
    ):
        raise RuntimeError("Cycle511 evidence changed after authorization")
    preservation = preservation_controls()
    exact_tags = exact_cyclotomic_contact_tag_diagnostic()
    checkpoints.append(resource_checkpoint(started, "after-preservation"))

    species = c511.c509.c219.common_species(MIDDLE_BETA)
    coin = species.coin
    angle = c511.factor_coordinate_controls()[
        "train_and_matched_size_beta_-4pi_over_9"
    ]["emitter_and_collision_angle"]
    lookup, collision_meta = local_collision_lookup(angle)
    component_rows = []
    schmidt_spectra: list[tuple[float, ...]] = []
    completed = True
    resource_wall = None
    maximum_completed_update = 0
    try:
        for axis in range(3):
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-start"))
            matter0 = initial_matter_ray(axis)
            mediator0 = initial_mediator_ray()

            mediator1_pre = apply_emitters(mediator0, angle)
            matter1 = forward_matter_word(matter0, coin)
            if not collision_is_identity_on_product(matter1, mediator1_pre, lookup):
                raise RuntimeError("update1 collision was not the frozen causal identity")
            mediator1 = apply_mediator_stream(mediator1_pre)
            maximum_completed_update = max(maximum_completed_update, 1)

            mediator2_pre = apply_emitters(mediator1, angle)
            matter2 = forward_matter_word(matter1, coin)
            schmidt, factor_state = update2_schmidt_factor_fixture(
                axis, matter2, mediator2_pre, lookup, angle
            )
            exact_joint2, materialization_ledger = materialize_update2_collision(
                matter2, mediator2_pre, lookup, started, checkpoints
            )
            factor_packed = factor_vs_packed_l2_comparison(
                factor_state, exact_joint2, started, checkpoints, axis
            )
            ninth_value = schmidt["singular_values"][-1]
            factor_packed["L2_to_ninth_singular_value_ratio"] = (
                factor_packed["L2_residual"] / ninth_value
            )
            factor_packed["resolves_ninth_component"] = (
                factor_packed["L2_to_ninth_singular_value_ratio"]
                <= SCHMIDT_PACKED_NINTH_RESOLUTION_FRACTION
            )
            factor_packed["pass"] = (
                factor_packed["pass"]
                and factor_packed["resolves_ninth_component"]
            )
            schmidt["factor_vs_packed"] = factor_packed
            schmidt["pass"] = (
                schmidt["pass_before_packed_comparison"] and factor_packed["pass"]
            )
            schmidt_spectra.append(schmidt["singular_values"])
            del factor_state
            maximum_completed_update = max(maximum_completed_update, 2)
            joint_norm = packed_norm(exact_joint2)
            free = matched_free_controls(axis, coin)
            matter_support = tuple(
                unpruned_support_diagnostics(ray)
                for ray in (matter0, matter1, matter2)
            )
            mediator_support = tuple(
                unpruned_support_diagnostics(ray)
                for ray in (mediator0, mediator1, mediator2_pre)
            )
            joint_support = unpruned_support_diagnostics(exact_joint2)
            support_oracles_pass = (
                tuple(row["stored_canonical_keys"] for row in matter_support)
                == DECLARED_STORED_MATTER_KEYS_BY_UPDATE[:3]
                and tuple(
                    row["values_above_diagnostic_ceiling"] for row in matter_support
                )
                == EXPECTED_DIAGNOSTIC_MATTER_SUPPORT_THROUGH_UPDATE2
                and tuple(row["stored_canonical_keys"] for row in mediator_support)
                == EXPECTED_DIAGNOSTIC_MEDIATOR_SUPPORT_THROUGH_UPDATE2
                and tuple(
                    row["values_above_diagnostic_ceiling"] for row in mediator_support
                )
                == EXPECTED_DIAGNOSTIC_MEDIATOR_SUPPORT_THROUGH_UPDATE2
                and joint_support["values_above_diagnostic_ceiling"]
                == EXPECTED_DIAGNOSTIC_PACKED_SUPPORT_AT_UPDATE2
                and joint_support["stored_canonical_keys"]
                == EXPECTED_UPDATE2_PACKED_STORED_KEYS
                and joint_support["machine_nonzero_values"]
                == EXPECTED_UPDATE2_PACKED_MACHINE_NONZERO_VALUES
                and joint_support["nonfinite_value_count"] == 0
                and materialization_ledger
                == EXPECTED_UPDATE2_MATERIALIZATION_LEDGER
            )
            component_rows.append({
                "axis": axis,
                "interacting_factor_stored_keys_before_first_collision": {
                    "matter_unpruned_by_update": matter_support,
                    "mediator_unpruned_by_update": mediator_support,
                    "species_Schmidt_rank_before_collision": 1,
                },
                "update2_packed_joint_unpruned_support": joint_support,
                "update2_materialization_ledger": materialization_ledger,
                "support_oracles_pass": support_oracles_pass,
                "update2_species_Schmidt_fixture": schmidt,
                "update2_joint_norm_residual": abs(joint_norm - 1),
                "matched_free": free,
                "numerical_rank_compression_used": False,
                "discarded_norm": 0.0,
                "response_computed_or_emitted": False,
            })
            del exact_joint2, matter0, matter1, matter2
            del mediator0, mediator1_pre, mediator1, mediator2_pre
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-released"))
    except (ResourceWall, MemoryError) as error:
        completed = False
        resource_wall = f"{type(error).__name__}: {error}"

    elapsed = time.monotonic() - started
    axis_spectrum_residual = (
        max(
            max(abs(left - right) for left, right in zip(spectrum, schmidt_spectra[0]))
            for spectrum in schmidt_spectra[1:]
        )
        if len(schmidt_spectra) == 3
        else float("inf")
    )
    all_axis_schmidt_pass = (
        len(schmidt_spectra) == 3
        and axis_spectrum_residual <= SCHMIDT_AXIS_SPECTRUM_CEILING
        and all(
            row["update2_species_Schmidt_fixture"]["pass"]
            for row in component_rows
        )
    )
    numeric_residuals = [
        row["update2_joint_norm_residual"] for row in component_rows
    ] + [
        row["matched_free"]["maximum_norm_residual"] for row in component_rows
    ] + [
        row["matched_free"]["repeat_state_residual"] for row in component_rows
    ] + [
        row["matched_free"]["inverse_state_residual"] for row in component_rows
    ] + [
        row["update2_species_Schmidt_fixture"]["active_cell_audit"][
            "maximum_local_factor_residual"
        ]
        for row in component_rows
    ] + [
        row["update2_species_Schmidt_fixture"][key]
        for row in component_rows
        for key in (
            "factor_norm_residual",
            "factor_norm_imaginary_residual",
            "QR_orthogonality_residual",
            "core_SVD_reconstruction_residual",
            "SVD_driver_spectrum_residual",
            "stream_Gram_residual",
            "stream_inverse_residual",
        )
    ] + [
        row["update2_species_Schmidt_fixture"]["factor_vs_packed"]["L2_residual"]
        for row in component_rows
    ]
    maximum_numeric = max(numeric_residuals) if numeric_residuals else None
    unpruned_update2_complete = completed and len(component_rows) == 3
    technical = (
        unpruned_update2_complete
        and preservation_pass(preservation)
        and exact_tags["pass"]
        and all(row["support_oracles_pass"] for row in component_rows)
        and all_axis_schmidt_pass
        and maximum_numeric is not None
        and np.isfinite(maximum_numeric)
        and maximum_numeric <= NUMERIC_CEILING
        and rss_bytes() < RSS_LIMIT_BYTES
        and elapsed < WALL_LIMIT_SECONDS
        and swap_count() == 0
    )
    # Depth 5 is deliberately not claimed: no reviewed species-Schmidt
    # continuation exists in this revision.
    status = (
        "update2-unpruned-packed-numerical-rank9-qualified-depth5-open"
        if technical else "technical-resource-unqualified"
    )
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "resource-scout",
        "status": status,
        "technical_update2_pass": technical,
        "completed_unpruned_numerical_updates": maximum_completed_update,
        "frozen_target_depth": FROZEN_TARGET_DEPTH,
        "Cycle511_full_sentinel_complete": False,
        "authorization": authorization,
        "evidence": {
            "Cycle511_runner_sha256": file_sha(CYCLE511_RUNNER),
            "Cycle511_receipt_sha256": file_sha(CYCLE511_RECEIPT),
            "RouteC8_sha256": evidence["RouteC8_sha256"],
            "intact_row_sha256": evidence["intact_row_sha256"],
            "contract_hashes": evidence["contract_hashes"],
        },
        "component_resource_rows": component_rows,
        "exact_cyclotomic_contact_tag_diagnostic": exact_tags,
        "preservation": preservation,
        "update2_species_Schmidt_all_axis": {
            "pass": all_axis_schmidt_pass,
            "component_count": len(schmidt_spectra),
            "numerical_rank_at_declared_cutoff_each": tuple(
                row["update2_species_Schmidt_fixture"][
                    "numerical_Schmidt_rank_at_declared_cutoff"
                ]
                for row in component_rows
            ),
            "maximum_spectrum_residual": axis_spectrum_residual,
            "ceiling": SCHMIDT_AXIS_SPECTRUM_CEILING,
            "numerical_rank9_is_update2_prefix_only": True,
            "depth5_feasibility_established": False,
        },
        "local_collision": {
            "generator_dimension": collision_meta["generator_dimension"],
            "generator_nnz": collision_meta["generator_nnz"],
            "maximum_connected_component": collision_meta["maximum_component_size"](),
            "maximum_unitarity_residual": collision_meta[
                "maximum_local_unitarity_residual"
            ](),
        },
        "resource": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": rss_bytes(),
            "process_swap_count": swap_count(),
            "checkpoints": checkpoints,
            "wall": resource_wall,
        },
        "residuals": {"maximum_reported_technical_residual": maximum_numeric},
        "algorithm_limits": dimension_and_algorithm_contract(),
        "execution": {
            "resource_invocations": 1,
            "resource_scout_executed": True,
            "science_rows_executed": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "response_values_emitted": 0,
            "occupation_or_bond_fields_emitted": 0,
            "state_hashes_emitted": 0,
            "classifier_emitted": False,
            "selector": False,
            "refit": False,
        },
        "interpretation": (
            "resource-algorithm evidence only; the unpruned numerical rank-9 update2 "
            "prefix at the declared cutoff supplies "
            "no update3 rank bound or depth5 feasibility result, and an update2 failure "
            "or absent continuation is neither a substrate obstruction nor axiom pressure"
        ),
    }, 0 if technical else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    try:
        payload, code = run_dry() if args.mode == "dry-contract" else run_resource_scout()
    except Exception as error:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": args.mode,
            "status": "fail-closed-exception",
            "error_type": type(error).__name__,
            "error": str(error),
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "response_values_emitted": 0,
            "state_hashes_emitted": 0,
        }
        code = 1
    print(json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
