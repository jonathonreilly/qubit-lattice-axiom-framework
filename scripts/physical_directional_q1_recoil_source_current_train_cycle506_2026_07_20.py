#!/usr/bin/env python3
"""Cycle 506 exact 3D evaluator, currently locked to one resource scout.

The authorized invocation executes only the C-sqrt-linear, source=-4pi/9,
probe=-4pi/9, train-L25, no-deletion row and its sequential free partner.
Response and morphology are printed under quarantine and do not enter the
scout verdict.  No other train row and no held row is selectable.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_directional_q1_recoil_source_current_preflight_cycle506_2026_07_20 as pre


AUTHORITY = "none"
AUDIT = "unset"
PREFLIGHT_RUNNER = ROOT / "scripts/physical_directional_q1_recoil_source_current_preflight_cycle506_2026_07_20.py"
PREFLIGHT_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DIRECTIONAL_Q1_RECOIL_SOURCE_CURRENT_PREFLIGHT_CYCLE506_NOTE_2026-07-20.md"
)
PREFLIGHT_RUNNER_SHA256 = "216156a376dcefd3e2d355dff34b589eaf06099ae0edd73ec8a740a2017c1061"
PREFLIGHT_NOTE_SHA256 = "666fd75c00fe2eb5bafa7b47d226bff5a2cfa31ef3ef226e1bc36a5dfa4ce0ac"
TRAIN_MANIFEST_SHA256 = "a5e37ba91332bf55f21b59543d5446379bbd92b71c948e85bf03c96bc306c3ee"
HELD_MANIFEST_SHA256 = "40e616dc4f5cc0dc70ac1801484f33c2be11009b56485e3f222e4b09e62aaed8"
SCOUT_ROUTE = "C-sqrt-linear"
SCOUT_SOURCE_BETA = -4 * np.pi / 9
SCOUT_PROBE_BETA = -4 * np.pi / 9
SCOUT_DELETION = "none"
WALL_CEILING_SECONDS = 600
RSS_CEILING_BYTES = 1_500_000_000
NUMERIC_GATE = pre.RUNNER_TOLERANCE
BLOCK_PRUNE_FROBENIUS = 1e-13

Mode = tuple[tuple[int, int, int], int]
Mediator = tuple[tuple[int, int, int], int] | None
Blocks = dict[Mediator, np.ndarray]


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return raw if sys.platform == "darwin" else raw * 1024


def enforce_rss(stage: str) -> None:
    rss = rss_bytes()
    print("RESOURCE_STAGE", {"stage": stage, "maximum_RSS_bytes": rss}, flush=True)
    if rss > RSS_CEILING_BYTES:
        raise MemoryError(f"RSS ceiling exceeded at {stage}: {rss}")


def alarm_handler(_signum, _frame) -> None:
    raise TimeoutError("Cycle506 scout exceeded the frozen 600-second row ceiling")


def contracts() -> list[dict]:
    train, held = pre.row_manifests()
    checks = {
        "authority_none": AUTHORITY == "none",
        "audit_unset": AUDIT == "unset",
        "preflight_runner_hash": file_sha(PREFLIGHT_RUNNER) == PREFLIGHT_RUNNER_SHA256,
        "preflight_note_hash": file_sha(PREFLIGHT_NOTE) == PREFLIGHT_NOTE_SHA256,
        "train_manifest_hash": pre.manifest_digest(train) == TRAIN_MANIFEST_SHA256,
        "held_manifest_hash": pre.manifest_digest(held) == HELD_MANIFEST_SHA256,
        "train_size": len(train) == 35,
        "held_size": len(held) == 12,
    }
    if not all(checks.values()):
        raise RuntimeError(f"frozen preflight contract mismatch: {checks}")
    eligible = [
        row for row in train
        if row["role"] == "primary-mass-grid"
        and row["route"] == SCOUT_ROUTE
        and row["source_beta"] == pre.beta_name(SCOUT_SOURCE_BETA)
        and row["probe_beta"] == pre.beta_name(SCOUT_PROBE_BETA)
        and row["deletion"] == SCOUT_DELETION
        and row["geometry"]["name"] == pre.TRAIN.name
    ]
    if len(eligible) != 1:
        raise RuntimeError(f"eligible scout row count is {len(eligible)}, expected one")
    print("FROZEN_CONTRACT", checks)
    print("SCOUT_ROW", eligible[0])
    print("HELD_ROWS_SELECTED", 0)
    return eligible


def support_bases() -> list[tuple[Mode, ...]]:
    rows, first_overlap = pre.reachable_support_trace(pre.TRAIN)
    if first_overlap != pre.TRAIN.first_causal_overlap_update:
        raise RuntimeError("support preflight drift")
    bases = [tuple(sorted(pre.initial_car_modes(pre.TRAIN)))]
    bases.extend(tuple(sorted(row["CAR_mode_keys"])) for row in rows)
    return bases


def initial_blocks(basis: tuple[Mode, ...]) -> Blocks:
    index = {mode: position for position, mode in enumerate(basis)}
    weights = np.asarray(pre.TRAIN.axial_envelope, dtype=float)
    weights /= np.linalg.norm(weights)
    cells = [
        (pre.TRAIN.probe_center[0] + offset, pre.TRAIN.probe_center[1], pre.TRAIN.probe_center[2])
        for offset in (-1, 0, 1)
    ]
    left = np.zeros(len(basis), dtype=complex)
    right = np.zeros(len(basis), dtype=complex)
    for cell, weight in zip(cells, weights):
        left[index[(cell, 0)]] = weight
        right[index[(cell, 1)]] = weight
    amplitude = np.outer(left, right) - np.outer(right, left)
    return {None: amplitude}


def state_norm_squared(blocks: Blocks) -> float:
    return float(sum(np.vdot(block, block).real for block in blocks.values()) / 2)


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


def prune_blocks(blocks: Blocks) -> Blocks:
    return {
        key: block for key, block in blocks.items()
        if np.linalg.norm(block) > BLOCK_PRUNE_FROBENIUS
    }


def emitter(blocks: Blocks, angle: float) -> Blocks:
    source_key: Mediator = (pre.TRAIN.source_cell, pre.OUTGOING_DIRECTION)
    park = blocks.get(None)
    outgoing = blocks.get(source_key)
    template = park if park is not None else outgoing
    if template is None:
        raise RuntimeError("emitter has neither parked nor source-outgoing block")
    zero = np.zeros_like(template)
    park = zero if park is None else park
    outgoing = zero if outgoing is None else outgoing
    cosine, sine = np.cos(angle), np.sin(angle)
    result = {
        key: block for key, block in blocks.items()
        if key not in (None, source_key)
    }
    result[None] = cosine * park + 1j * sine * outgoing
    result[source_key] = cosine * outgoing + 1j * sine * park
    return prune_blocks(result)


def one_body_map(previous: tuple[Mode, ...], following: tuple[Mode, ...], beta: float) -> sparse.csr_matrix:
    target_index = {mode: index for index, mode in enumerate(following)}
    coin = pre.c219.common_species(beta).coin
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for column, (cell, incoming) in enumerate(previous):
        for outgoing in range(6):
            target_cell = tuple(int(x) for x in (np.asarray(cell) + pre.c210.DIRECTIONS[outgoing]))
            target = (target_cell, outgoing)
            if target not in target_index:
                raise RuntimeError("reachable support omitted a CAR stream target")
            rows.append(target_index[target])
            columns.append(column)
            data.append(coin[outgoing, incoming])
    result = sparse.coo_matrix(
        (data, (rows, columns)), shape=(len(following), len(previous)), dtype=complex
    ).tocsr()
    result.sum_duplicates()
    residual = sparse.linalg.norm(result.conj().T @ result - sparse.eye(len(previous)))
    if residual > NUMERIC_GATE:
        raise RuntimeError(f"restricted one-body map is not isometric: {residual}")
    return result


def apply_car_map(blocks: Blocks, operation: sparse.csr_matrix, *, inverse: bool = False) -> Blocks:
    result: Blocks = {}
    if inverse:
        left = operation.conj().T.tocsr()
    else:
        left = operation
    for key, block in blocks.items():
        temporary = left @ block
        result[key] = (left @ temporary.T).T
    return prune_blocks(result)


def apply_contact(blocks: Blocks, basis: tuple[Mode, ...], coupling: float) -> None:
    by_cell: dict[tuple[int, int, int], list[int]] = {}
    for index, (cell, _direction) in enumerate(basis):
        by_cell.setdefault(cell, []).append(index)
    phase = np.exp(1j * coupling)
    for block in blocks.values():
        for indices in by_cell.values():
            if len(indices) >= 2:
                selection = np.ix_(indices, indices)
                block[selection] *= phase


def collision(blocks: Blocks, basis: tuple[Mode, ...], angle: float) -> Blocks:
    if abs(angle) < 1e-18:
        return {key: block.copy() for key, block in blocks.items()}
    index = {mode: position for position, mode in enumerate(basis)}
    result = {key: block.copy() for key, block in blocks.items()}
    cosine, sine = np.cos(angle), np.sin(angle)
    size = len(basis)
    for mediator_key, block in blocks.items():
        if mediator_key is None:
            continue
        cell, direction = mediator_key
        old_mode = (cell, pre.REVERSE[direction])
        new_mode = (cell, direction)
        if old_mode not in index or new_mode not in index:
            continue
        old, new = index[old_mode], index[new_mode]
        partners = np.asarray([value for value in range(size) if value not in (old, new)], dtype=int)
        coefficients = block[old, partners].copy()
        adjustment = (cosine - 1) * coefficients
        result[mediator_key][old, partners] += adjustment
        result[mediator_key][partners, old] -= adjustment
        target_key: Mediator = (cell, pre.REVERSE[direction])
        if target_key not in result:
            result[target_key] = np.zeros_like(block)
        scattered = 1j * sine * coefficients
        result[target_key][new, partners] += scattered
        result[target_key][partners, new] -= scattered
    return prune_blocks(result)


def mediator_stream(blocks: Blocks, *, inverse: bool = False) -> Blocks:
    result: Blocks = {}
    sign = -1 if inverse else 1
    for key, block in blocks.items():
        if key is None:
            target = None
        else:
            cell, direction = key
            target = (
                tuple(int(x) for x in (np.asarray(cell) + sign * pre.c210.DIRECTIONS[direction])),
                direction,
            )
        if target in result:
            result[target] += block
        else:
            result[target] = block
    return prune_blocks(result)


def forward_step(
    blocks: Blocks,
    operation: sparse.csr_matrix,
    following_basis: tuple[Mode, ...],
    emitter_angle: float,
    collision_angle: float,
) -> Blocks:
    output = emitter(blocks, emitter_angle)
    output = apply_car_map(output, operation)
    apply_contact(output, following_basis, pre.CONTACT_COUPLING)
    output = collision(output, following_basis, collision_angle)
    return mediator_stream(output)


def inverse_step(
    blocks: Blocks,
    operation: sparse.csr_matrix,
    current_basis: tuple[Mode, ...],
    emitter_angle: float,
    collision_angle: float,
) -> Blocks:
    output = mediator_stream(blocks, inverse=True)
    output = collision(output, current_basis, -collision_angle)
    apply_contact(output, current_basis, -pre.CONTACT_COUPLING)
    output = apply_car_map(output, operation, inverse=True)
    return emitter(output, -emitter_angle)


def state_diagnostics(blocks: Blocks, basis: tuple[Mode, ...]) -> dict:
    norm_squared = state_norm_squared(blocks)
    occupation = np.zeros(len(basis))
    direction = np.zeros(7)
    maximum_displacement = 0
    contact = 0.0
    antisymmetry = 0.0
    diagonal = 0.0
    for mediator_key, block in blocks.items():
        occupation += np.sum(abs(block) ** 2, axis=1)
        weight = float(np.vdot(block, block).real / 2)
        if mediator_key is None:
            direction[0] += weight
        else:
            cell, med_direction = mediator_key
            direction[1 + med_direction] += weight
            maximum_displacement = max(
                maximum_displacement,
                sum(abs(cell[axis] - pre.TRAIN.source_cell[axis]) for axis in range(3)),
            )
        antisymmetry = max(antisymmetry, float(np.linalg.norm(block + block.T)))
        diagonal = max(diagonal, float(np.max(abs(np.diag(block)))))
        by_cell: dict[tuple[int, int, int], list[int]] = {}
        for index, (cell, _direction) in enumerate(basis):
            by_cell.setdefault(cell, []).append(index)
        for indices in by_cell.values():
            local = block[np.ix_(indices, indices)]
            contact += float(np.vdot(local, local).real / 2)
    cut = pre.TRAIN.probe_center[0]
    current_weights = []
    index = {mode: position for position, mode in enumerate(basis)}
    character = 0j
    for position, (cell, mode_direction) in enumerate(basis):
        target_x = (cell[0] + 1) % pre.TRAIN.side
        current_weights.append(float((target_x >= cut) - (cell[0] >= cut)))
        target = ((target_x, cell[1], cell[2]), mode_direction)
        if target in index:
            target_position = index[target]
            for block in blocks.values():
                character += np.vdot(block[target_position], block[position]) / 2
    plane_current = float(np.dot(current_weights, occupation))
    shell = float(sum(
        occupation[position]
        for position, (cell, _direction) in enumerate(basis)
        if any(coordinate in (0, pre.TRAIN.side - 1) for coordinate in cell)
    ))
    return {
        "norm_squared": norm_squared,
        "CAR_number": float(np.sum(occupation)),
        "mediator_Q": float(np.sum(direction)),
        "parked_weight": float(direction[0]),
        "active_weight": float(np.sum(direction[1:])),
        "direction_ledger": tuple(float(value) for value in direction),
        "maximum_mediator_L1_displacement": maximum_displacement,
        "contact": contact,
        "plane_current": plane_current,
        "translation_character": character,
        "shell_weight": shell,
        "antisymmetry_residual": antisymmetry,
        "Pauli_diagonal_residual": diagonal,
        "block_count": len(blocks),
        "basis_modes": len(basis),
    }


def evolve(
    initial: Blocks,
    bases: list[tuple[Mode, ...]],
    operations: list[sparse.csr_matrix],
    emitter_angle: float,
    collision_angle: float,
    label: str,
) -> tuple[Blocks, list[dict]]:
    blocks = {key: block.copy() for key, block in initial.items()}
    trace = [state_diagnostics(blocks, bases[0])]
    for update, operation in enumerate(operations, start=1):
        blocks = forward_step(
            blocks, operation, bases[update], emitter_angle, collision_angle
        )
        trace.append(state_diagnostics(blocks, bases[update]))
        enforce_rss(f"{label}-update-{update}")
    return blocks, trace


def inverse_evolve(
    final: Blocks,
    bases: list[tuple[Mode, ...]],
    operations: list[sparse.csr_matrix],
    emitter_angle: float,
    collision_angle: float,
) -> Blocks:
    # Consume the caller-owned dictionary in place.  Clearing each previous
    # layer after its successor exists prevents a hidden third 495 MB copy.
    blocks = final
    for update in reversed(range(1, len(bases))):
        previous = blocks
        blocks = inverse_step(
            blocks, operations[update - 1], bases[update], emitter_angle, collision_angle
        )
        previous.clear()
        enforce_rss(f"inverse-update-{update}")
    return blocks


def scout() -> None:
    started = time.monotonic()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(WALL_CEILING_SECONDS)
    contracts()
    print("COMMAND_CONTRACT", {
        "mode": "resource-scout", "route": SCOUT_ROUTE,
        "source_beta": pre.beta_name(SCOUT_SOURCE_BETA),
        "probe_beta": pre.beta_name(SCOUT_PROBE_BETA),
        "geometry": pre.TRAIN.name, "deletion": SCOUT_DELETION,
        "free_partner": "sequential", "other_train_rows": 0, "held_rows": 0,
    })
    bases = support_bases()
    operations = [
        one_body_map(bases[index], bases[index + 1], SCOUT_PROBE_BETA)
        for index in range(pre.TRAIN.depth)
    ]
    initial = initial_blocks(bases[0])
    mass = float(-3 * np.tan(SCOUT_SOURCE_BETA / 2))
    emitter_angle = pre.EMITTER_COUPLING * np.sqrt(mass)
    collision_angle = pre.SCATTERING_COUPLING * mass
    interacting, interacting_trace = evolve(
        initial, bases, operations, emitter_angle, collision_angle, "interacting"
    )
    maximum_interacting_rss = rss_bytes()
    free_one, free_trace = evolve(initial, bases, operations, 0.0, 0.0, "free-one")
    free_two, free_repeat_trace = evolve(initial, bases, operations, 0.0, 0.0, "free-repeat")
    free_repeat_residual = state_residual(free_one, free_two)
    del free_two
    restored = inverse_evolve(
        interacting, bases, operations, emitter_angle, collision_angle
    )
    inverse_residual = state_residual(restored, initial)
    del restored

    norm_residual = max(
        abs(row["norm_squared"] - 1)
        for row in interacting_trace + free_trace + free_repeat_trace
    )
    number_residual = max(
        abs(row["CAR_number"] - 2)
        for row in interacting_trace + free_trace + free_repeat_trace
    )
    mediator_q_residual = max(
        abs(row["mediator_Q"] - 1)
        for row in interacting_trace + free_trace + free_repeat_trace
    )
    domain_residual = max(
        max(row["antisymmetry_residual"], row["Pauli_diagonal_residual"])
        for row in interacting_trace + free_trace + free_repeat_trace
    )
    window = pre.TRAIN.response_window
    quarantined = pre.interaction_minus_free_observables(
        tuple(interacting_trace[t]["plane_current"] for t in window),
        tuple(free_trace[t]["plane_current"] for t in window),
        tuple(interacting_trace[t]["translation_character"] for t in window),
        tuple(free_trace[t]["translation_character"] for t in window),
    )
    quarantined["morphology_classifier"] = pre.classify_response(
        quarantined["delta_plane_current"],
        (norm_residual, inverse_residual, number_residual, mediator_q_residual, domain_residual, free_repeat_residual),
    )
    quarantined["observed_source_output_update1"] = interacting_trace[1]["active_weight"]
    quarantined["interacting_trace"] = interacting_trace
    quarantined["free_trace"] = free_trace
    print("QUARANTINED_RESPONSE_NOT_SCIENCE_EVIDENCE", quarantined)

    elapsed = time.monotonic() - started
    maximum_rss = rss_bytes()
    swaps = resource.getrusage(resource.RUSAGE_SELF).ru_nswap
    gates = {
        "implementation_completed": True,
        "wall_seconds": elapsed < WALL_CEILING_SECONDS,
        "RSS_bytes": maximum_rss < RSS_CEILING_BYTES,
        "swaps": swaps == 0,
        "norm": norm_residual < NUMERIC_GATE,
        "inverse": inverse_residual < NUMERIC_GATE,
        "CAR_number": number_residual < NUMERIC_GATE,
        "mediator_Q": mediator_q_residual < NUMERIC_GATE,
        "lawful_domain": domain_residual < NUMERIC_GATE,
        "free_repeat": free_repeat_residual < NUMERIC_GATE,
    }
    result = {
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "maximum_interacting_forward_RSS_bytes": maximum_interacting_rss,
        "swaps": swaps,
        "norm_residual": norm_residual,
        "inverse_residual": inverse_residual,
        "CAR_number_residual": number_residual,
        "mediator_Q_residual": mediator_q_residual,
        "lawful_domain_residual": domain_residual,
        "free_repeat_residual": free_repeat_residual,
        "gates": gates,
        "scout_verdict": "resource-eligible" if all(gates.values()) else "resource-blocked",
        "science_train_rows_counted": 0,
        "held_rows_executed": 0,
        "response_used_for_refit_or_disposition": False,
    }
    print("RESOURCE_SCOUT_RESULT", result)
    signal.alarm(0)
    raise SystemExit(0 if all(gates.values()) else 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("resource-scout",), required=True)
    parser.add_argument("--route", choices=(SCOUT_ROUTE,), required=True)
    parser.add_argument("--source-beta", choices=("-4pi/9",), required=True)
    parser.add_argument("--probe-beta", choices=("-4pi/9",), required=True)
    parser.add_argument("--geometry", choices=(pre.TRAIN.name,), required=True)
    parser.add_argument("--deletion", choices=(SCOUT_DELETION,), required=True)
    arguments = parser.parse_args()
    if (
        arguments.mode != "resource-scout"
        or arguments.route != SCOUT_ROUTE
        or arguments.source_beta != "-4pi/9"
        or arguments.probe_beta != "-4pi/9"
        or arguments.geometry != pre.TRAIN.name
        or arguments.deletion != SCOUT_DELETION
    ):
        raise SystemExit("only the frozen resource scout row is authorized")
    scout()


if __name__ == "__main__":
    main()
