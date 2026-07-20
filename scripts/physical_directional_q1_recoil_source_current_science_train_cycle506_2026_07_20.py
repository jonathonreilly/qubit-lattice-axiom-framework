#!/usr/bin/env python3
"""Cycle 506 immutable 35-row science-train evaluator.

This evaluator imports the accepted resource-scout implementation and refuses
to run unless its exact hash, the preflight hashes, and both immutable manifest
hashes match.  Its science mode always executes all 35 train rows in manifest
order, with sequential matched free partners and repeated-free controls.  It
has no row selector and no held-evolution path.  The dry-contract mode checks
only contracts and executes zero science rows.

Dimensionless current/quasimomentum per update are not force, gravity,
physical momentum, or time.  Authority none; audit unset.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
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
import physical_directional_q1_recoil_source_current_train_cycle506_2026_07_20 as scout


AUTHORITY = "none"
AUDIT = "unset"
SCOUT_EVALUATOR = ROOT / "scripts/physical_directional_q1_recoil_source_current_train_cycle506_2026_07_20.py"
SCOUT_EVALUATOR_SHA256 = "91c3f96a164d08a4707c00e6f9903f799c5c80c37a2644ea047934cb628b550e"
PREFLIGHT_RUNNER_SHA256 = "216156a376dcefd3e2d355dff34b589eaf06099ae0edd73ec8a740a2017c1061"
PREFLIGHT_NOTE_SHA256 = "666fd75c00fe2eb5bafa7b47d226bff5a2cfa31ef3ef226e1bc36a5dfa4ce0ac"
TRAIN_MANIFEST_SHA256 = "a5e37ba91332bf55f21b59543d5446379bbd92b71c948e85bf03c96bc306c3ee"
HELD_MANIFEST_SHA256 = "40e616dc4f5cc0dc70ac1801484f33c2be11009b56485e3f222e4b09e62aaed8"
SCIENCE_ROWS = 35
HELD_ROWS_EXECUTED = 0
WALL_CEILING_SECONDS = 600
RSS_CEILING_BYTES = 1_500_000_000
NUMERIC_GATE = pre.RUNNER_TOLERANCE

Mode = scout.Mode
Mediator = scout.Mediator
Blocks = scout.Blocks

_BAND_KERNELS: dict[float, np.ndarray] = {}
_BAND_PROJECTORS: dict[tuple[float, str], np.ndarray] = {}


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value: object) -> object:
    if isinstance(value, complex):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, (np.floating, np.integer, np.bool_)):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def emit(label: str, value: object) -> None:
    print(label, json.dumps(value, sort_keys=True, separators=(",", ":"), default=json_default), flush=True)


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return raw if sys.platform == "darwin" else raw * 1024


def enforce_rss(stage: str) -> None:
    current = rss_bytes()
    emit("RESOURCE_STAGE", {"stage": stage, "maximum_RSS_bytes": current})
    if current > RSS_CEILING_BYTES:
        raise MemoryError(f"RSS ceiling exceeded at {stage}: {current}")


def alarm_handler(_signum: int, _frame: object) -> None:
    raise TimeoutError("Cycle506 science-train row exceeded the frozen 600-second ceiling")


def contracts() -> list[dict]:
    train, held = pre.row_manifests()
    roles = {name: sum(row["role"] == name for row in train) for name in (
        "primary-mass-grid", "selected-deletion", "direction-reversal-control"
    )}
    checks = {
        "authority_none": AUTHORITY == "none",
        "audit_unset": AUDIT == "unset",
        "accepted_scout_evaluator_hash": file_sha(SCOUT_EVALUATOR) == SCOUT_EVALUATOR_SHA256,
        "preflight_runner_hash": file_sha(scout.PREFLIGHT_RUNNER) == PREFLIGHT_RUNNER_SHA256,
        "preflight_note_hash": file_sha(scout.PREFLIGHT_NOTE) == PREFLIGHT_NOTE_SHA256,
        "train_manifest_hash": pre.manifest_digest(train) == TRAIN_MANIFEST_SHA256,
        "held_manifest_hash": pre.manifest_digest(held) == HELD_MANIFEST_SHA256,
        "train_size": len(train) == SCIENCE_ROWS,
        "held_size_frozen_but_unselectable": len(held) == 12,
        "train_role_counts": roles == {
            "primary-mass-grid": 27,
            "selected-deletion": 7,
            "direction-reversal-control": 1,
        },
        "all_train_rows_free_refit_locked": all(row["free_partner"] and not row["refit"] for row in train),
        "train_only_geometry": all(row["geometry"]["name"] == pre.TRAIN.name for row in train),
    }
    if not all(checks.values()):
        raise RuntimeError(f"frozen science-train contract mismatch: {checks}")
    emit("FROZEN_SCIENCE_TRAIN_CONTRACT", checks)
    emit("IMMUTABLE_MANIFEST", {
        "train_rows": len(train),
        "train_sha256": pre.manifest_digest(train),
        "train_role_counts": roles,
        "held_manifest_sha256_contract_only": pre.manifest_digest(held),
        "held_rows_selectable": 0,
        "row_filtering_available": False,
    })
    return train


def beta_value(name: str) -> float:
    values = {
        "-2pi/9": -2 * np.pi / 9,
        "-4pi/9": -4 * np.pi / 9,
        "-2pi/3": -2 * np.pi / 3,
    }
    return float(values[name])


def mass_value(beta: float) -> float:
    return float(-3 * np.tan(beta / 2))


def factor_values(row: dict, source_mass: float, probe_mass: float) -> tuple[float, float]:
    source_factor = pre.controller_factor(row["route"], "source", source_mass)
    probe_factor = pre.controller_factor(row["route"], "probe", probe_mass)
    if row["deletion"] == "source-mass-factor":
        source_factor = 1.0
    if row["deletion"] == "probe-mass-factor":
        probe_factor = 1.0
    return float(source_factor), float(probe_factor)


def support_bases(outgoing_direction: int) -> list[tuple[Mode, ...]]:
    previous = pre.OUTGOING_DIRECTION
    try:
        pre.OUTGOING_DIRECTION = outgoing_direction
        rows, first_overlap = pre.reachable_support_trace(pre.TRAIN)
    finally:
        pre.OUTGOING_DIRECTION = previous
    expected_overlap = pre.TRAIN.first_causal_overlap_update if outgoing_direction == previous else None
    if outgoing_direction == previous and first_overlap != expected_overlap:
        raise RuntimeError("canonical support preflight drift")
    bases = [tuple(sorted(pre.initial_car_modes(pre.TRAIN)))]
    bases.extend(tuple(sorted(row["CAR_mode_keys"])) for row in rows)
    return bases


def basis_digest(basis: tuple[Mode, ...]) -> str:
    payload = json.dumps(basis, separators=(",", ":")).encode()
    return sha256(payload).hexdigest()


def one_body_map(
    previous: tuple[Mode, ...],
    following: tuple[Mode, ...],
    beta: float,
    *,
    delete_probe_coin: bool,
) -> sparse.csr_matrix:
    if not delete_probe_coin:
        return scout.one_body_map(previous, following, beta)
    target_index = {mode: index for index, mode in enumerate(following)}
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for column, (cell, incoming) in enumerate(previous):
        target_cell = tuple(int(x) for x in (np.asarray(cell) + pre.c210.DIRECTIONS[incoming]))
        target = (target_cell, incoming)
        if target not in target_index:
            raise RuntimeError("reachable support omitted an identity-coin stream target")
        rows.append(target_index[target])
        columns.append(column)
        data.append(1.0 + 0j)
    result = sparse.coo_matrix(
        (data, (rows, columns)), shape=(len(following), len(previous)), dtype=complex
    ).tocsr()
    residual = sparse.linalg.norm(result.conj().T @ result - sparse.eye(len(previous)))
    if residual > NUMERIC_GATE:
        raise RuntimeError(f"identity-coin one-body map is not isometric: {residual}")
    return result


def emitter(blocks: Blocks, angle: float, outgoing_direction: int) -> Blocks:
    source_key: Mediator = (pre.TRAIN.source_cell, outgoing_direction)
    park = blocks.get(None)
    outgoing = blocks.get(source_key)
    template = park if park is not None else outgoing
    if template is None:
        raise RuntimeError("emitter has neither parked nor carried-outgoing block")
    zero = np.zeros_like(template)
    park = zero if park is None else park
    outgoing = zero if outgoing is None else outgoing
    cosine, sine = np.cos(angle), np.sin(angle)
    result = {key: block for key, block in blocks.items() if key not in (None, source_key)}
    result[None] = cosine * park + 1j * sine * outgoing
    result[source_key] = cosine * outgoing + 1j * sine * park
    return scout.prune_blocks(result)


def forward_step(
    blocks: Blocks,
    operation: sparse.csr_matrix,
    following_basis: tuple[Mode, ...],
    emitter_angle: float,
    collision_angle: float,
    outgoing_direction: int,
    contact_coupling: float,
    mediator_stream_enabled: bool,
) -> Blocks:
    output = emitter(blocks, emitter_angle, outgoing_direction)
    output = scout.apply_car_map(output, operation)
    scout.apply_contact(output, following_basis, contact_coupling)
    output = scout.collision(output, following_basis, collision_angle)
    return scout.mediator_stream(output) if mediator_stream_enabled else output


def inverse_step(
    blocks: Blocks,
    operation: sparse.csr_matrix,
    current_basis: tuple[Mode, ...],
    emitter_angle: float,
    collision_angle: float,
    outgoing_direction: int,
    contact_coupling: float,
    mediator_stream_enabled: bool,
) -> Blocks:
    output = scout.mediator_stream(blocks, inverse=True) if mediator_stream_enabled else {
        key: block.copy() for key, block in blocks.items()
    }
    output = scout.collision(output, current_basis, -collision_angle)
    scout.apply_contact(output, current_basis, -contact_coupling)
    output = scout.apply_car_map(output, operation, inverse=True)
    return emitter(output, -emitter_angle, outgoing_direction)


def band_kernel(beta: float) -> np.ndarray:
    key = round(beta, 12)
    if key in _BAND_KERNELS:
        return _BAND_KERNELS[key]
    side = pre.TRAIN.side
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    spectral = np.empty((side, side, side, 6, 6), dtype=complex)
    coin = pre.c219.common_species(beta).coin
    for ix, kx in enumerate(momenta):
        for iy, ky in enumerate(momenta):
            for iz, kz in enumerate(momenta):
                phase = pre.c210.DIRECTIONS @ np.asarray((kx, ky, kz))
                bloch = np.diag(np.exp(-1j * phase)) @ coin
                _values, candidates = np.linalg.eig(bloch)
                selected = int(np.argmax(np.abs(candidates.conj().T @ pre.c210.UNIFORM)))
                vector = candidates[:, selected] / np.linalg.norm(candidates[:, selected])
                spectral[ix, iy, iz] = np.outer(vector, vector.conj())
    kernel = np.fft.ifftn(spectral, axes=(0, 1, 2))
    _BAND_KERNELS[key] = kernel
    return kernel


def band_projector(beta: float, basis: tuple[Mode, ...]) -> np.ndarray:
    cache_key = (round(beta, 12), basis_digest(basis))
    if cache_key in _BAND_PROJECTORS:
        return _BAND_PROJECTORS[cache_key]
    side = pre.TRAIN.side
    cells = np.asarray([cell for cell, _direction in basis], dtype=int)
    directions = np.asarray([direction for _cell, direction in basis], dtype=int)
    displacement = (cells[:, None, :] - cells[None, :, :]) % side
    kernel = band_kernel(beta)
    projector = kernel[
        displacement[:, :, 0], displacement[:, :, 1], displacement[:, :, 2],
        directions[:, None], directions[None, :],
    ]
    hermitian_residual = float(np.max(abs(projector - projector.conj().T)))
    if hermitian_residual > NUMERIC_GATE:
        raise RuntimeError(f"restricted selected-band projector is not Hermitian: {hermitian_residual}")
    _BAND_PROJECTORS[cache_key] = projector
    return projector


def axial_seam_weight(gamma: np.ndarray, basis: tuple[Mode, ...]) -> float:
    side = pre.TRAIN.side
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    seam_indices = np.argsort(np.abs(momenta))[-2:]
    kernel = np.fft.ifft(np.isin(np.arange(side), seam_indices).astype(float))
    groups: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for index, (cell, direction) in enumerate(basis):
        groups[(cell[1], cell[2], direction)].append(index)
    result = 0j
    for indices in groups.values():
        rows = np.asarray(indices, dtype=int)
        x = np.asarray([basis[index][0][0] for index in indices], dtype=int)
        projector = kernel[(x[:, None] - x[None, :]) % side]
        reduced = gamma[np.ix_(rows, rows)]
        result += np.einsum("ij,ji->", projector, reduced, optimize=True)
    return float(np.real(result))


def augmented_diagnostics(blocks: Blocks, basis: tuple[Mode, ...], beta: float) -> dict:
    diagnostics = scout.state_diagnostics(blocks, basis)
    size = len(basis)
    gamma = np.zeros((size, size), dtype=complex)
    transverse = 0.0
    transverse_indices = np.asarray([
        index for index, (cell, _direction) in enumerate(basis)
        if cell[1:] != pre.TRAIN.probe_center[1:]
    ], dtype=int)
    for block in blocks.values():
        gamma += block @ block.conj().T
        if len(transverse_indices):
            transverse += float(np.sum(abs(block[transverse_indices, :]) ** 2))
    projector = band_projector(beta, basis)
    band_number = float(np.real(np.einsum("ij,ji->", projector, gamma, optimize=True)))
    diagnostics["full_3D_selected_band_fraction"] = band_number / diagnostics["CAR_number"]
    diagnostics["total_two_CAR_axial_seam_weight"] = axial_seam_weight(gamma, basis)
    diagnostics["transverse_CAR_fraction"] = transverse / diagnostics["CAR_number"]
    del gamma
    return diagnostics


def evolve(
    initial: Blocks,
    bases: list[tuple[Mode, ...]],
    operations: list[sparse.csr_matrix],
    beta: float,
    emitter_angle: float,
    collision_angle: float,
    outgoing_direction: int,
    contact_coupling: float,
    mediator_stream_enabled: bool,
    label: str,
) -> tuple[Blocks, list[dict]]:
    blocks = {key: block.copy() for key, block in initial.items()}
    trace = [augmented_diagnostics(blocks, bases[0], beta)]
    for update, operation in enumerate(operations, start=1):
        blocks = forward_step(
            blocks, operation, bases[update], emitter_angle, collision_angle,
            outgoing_direction, contact_coupling, mediator_stream_enabled,
        )
        trace.append(augmented_diagnostics(blocks, bases[update], beta))
        enforce_rss(f"{label}-update-{update}")
    return blocks, trace


def inverse_evolve(
    final: Blocks,
    bases: list[tuple[Mode, ...]],
    operations: list[sparse.csr_matrix],
    emitter_angle: float,
    collision_angle: float,
    outgoing_direction: int,
    contact_coupling: float,
    mediator_stream_enabled: bool,
) -> Blocks:
    blocks = final
    for update in reversed(range(1, len(bases))):
        previous = blocks
        blocks = inverse_step(
            blocks, operations[update - 1], bases[update], emitter_angle,
            collision_angle, outgoing_direction, contact_coupling,
            mediator_stream_enabled,
        )
        previous.clear()
        enforce_rss(f"inverse-update-{update}")
    return blocks


def row_numeric_residuals(
    traces: tuple[list[dict], ...], inverse_residual: float, free_repeat_residual: float
) -> dict:
    rows = [entry for trace in traces for entry in trace]
    return {
        "norm": max(abs(row["norm_squared"] - 1) for row in rows),
        "inverse": inverse_residual,
        "CAR_number": max(abs(row["CAR_number"] - 2) for row in rows),
        "mediator_Q": max(abs(row["mediator_Q"] - 1) for row in rows),
        "lawful_domain": max(max(row["antisymmetry_residual"], row["Pauli_diagonal_residual"]) for row in rows),
        "free_repeat": free_repeat_residual,
    }


def run_row(index: int, row: dict) -> dict:
    started = time.monotonic()
    signal.alarm(WALL_CEILING_SECONDS)
    source_beta = beta_value(row["source_beta"])
    probe_beta = beta_value(row["probe_beta"])
    source_mass, probe_mass = mass_value(source_beta), mass_value(probe_beta)
    source_factor, probe_factor = factor_values(row, source_mass, probe_mass)
    emitter_angle = 0.0 if row["deletion"] == "emitter" else pre.EMITTER_COUPLING * source_factor
    collision_angle = 0.0 if row["deletion"] == "collision" else pre.SCATTERING_COUPLING * probe_factor
    contact_coupling = 0.0 if row["deletion"] == "contact" else pre.CONTACT_COUPLING
    mediator_stream_enabled = row["deletion"] != "mediator-stream"
    delete_probe_coin = row["deletion"] == "probe-coin"
    outgoing_direction = int(row["outgoing_direction"])

    bases = support_bases(outgoing_direction)
    operations = [
        one_body_map(bases[step], bases[step + 1], probe_beta, delete_probe_coin=delete_probe_coin)
        for step in range(pre.TRAIN.depth)
    ]
    initial = scout.initial_blocks(bases[0])
    interacting, interacting_trace = evolve(
        initial, bases, operations, probe_beta, emitter_angle, collision_angle,
        outgoing_direction, contact_coupling, mediator_stream_enabled, f"row-{index}-interacting",
    )
    maximum_interacting_forward_rss = rss_bytes()
    free_one, free_trace = evolve(
        initial, bases, operations, probe_beta, 0.0, 0.0, outgoing_direction,
        contact_coupling, mediator_stream_enabled, f"row-{index}-free-one",
    )
    free_two, free_repeat_trace = evolve(
        initial, bases, operations, probe_beta, 0.0, 0.0, outgoing_direction,
        contact_coupling, mediator_stream_enabled, f"row-{index}-free-repeat",
    )
    free_repeat_residual = scout.state_residual(free_one, free_two)
    del free_two
    restored = inverse_evolve(
        interacting, bases, operations, emitter_angle, collision_angle,
        outgoing_direction, contact_coupling, mediator_stream_enabled,
    )
    inverse_residual = scout.state_residual(restored, initial)
    del restored

    residuals = row_numeric_residuals(
        (interacting_trace, free_trace, free_repeat_trace), inverse_residual, free_repeat_residual
    )
    window = pre.TRAIN.response_window
    response = pre.interaction_minus_free_observables(
        tuple(interacting_trace[t]["plane_current"] for t in window),
        tuple(free_trace[t]["plane_current"] for t in window),
        tuple(interacting_trace[t]["translation_character"] for t in window),
        tuple(free_trace[t]["translation_character"] for t in window),
    )
    classification = pre.classify_response(
        response["delta_plane_current"], tuple(residuals.values())
    )
    dynamic_rows = [entry for trace in (interacting_trace, free_trace, free_repeat_trace) for entry in trace[1:]]
    shell_maximum = max(entry["shell_weight"] for trace in (interacting_trace, free_trace, free_repeat_trace) for entry in trace)
    contact_maximum = max(entry["contact"] for entry in dynamic_rows)
    band_minimum = min(entry["full_3D_selected_band_fraction"] for entry in dynamic_rows)
    seam_maximum = max(entry["total_two_CAR_axial_seam_weight"] for entry in dynamic_rows)
    transverse_maximum = max(entry["transverse_CAR_fraction"] for entry in dynamic_rows)
    technical_gates = {
        **{name: value <= NUMERIC_GATE for name, value in residuals.items()},
        "cube_face_shell": shell_maximum <= 1e-12,
        "dynamic_contact": contact_maximum >= pre.DYNAMIC_CONTACT_FLOOR,
        "dynamic_full_3D_band": band_minimum >= pre.DYNAMIC_BAND_FLOOR,
        "dynamic_axial_seam": seam_maximum <= pre.DYNAMIC_AXIAL_SEAM_CEILING,
        "translation_character": response["minimum_character_magnitude"] >= pre.CHARACTER_MAGNITUDE_FLOOR,
    }
    elapsed = time.monotonic() - started
    technical_gates["row_wall_seconds"] = elapsed < WALL_CEILING_SECONDS
    technical_gates["process_RSS_bytes"] = rss_bytes() < RSS_CEILING_BYTES
    technical_gates["process_swaps"] = resource.getrusage(resource.RUSAGE_SELF).ru_nswap == 0
    result = {
        "manifest_index": index,
        "role": row["role"],
        "route": row["route"],
        "source_beta": row["source_beta"],
        "probe_beta": row["probe_beta"],
        "source_mass": source_mass,
        "probe_mass": probe_mass,
        "outgoing_direction": outgoing_direction,
        "deletion": row["deletion"],
        "applied_source_factor": source_factor,
        "applied_probe_factor": probe_factor,
        "applied_emitter_angle": emitter_angle,
        "applied_collision_angle": collision_angle,
        "applied_contact_coupling": contact_coupling,
        "mediator_stream_enabled": mediator_stream_enabled,
        "probe_coin_enabled": not delete_probe_coin,
        "source_output": interacting_trace[1]["active_weight"],
        "maximum_active_mediator": max(entry["active_weight"] for entry in interacting_trace),
        "maximum_mediator_displacement": max(entry["maximum_mediator_L1_displacement"] for entry in interacting_trace),
        "maximum_transverse_CAR_weight": transverse_maximum,
        "response_amplitude": response["response_amplitude"],
        "signal_floor": classification["signal_floor"],
        "classification": classification["classification"],
        "response": response,
        "classifier": classification,
        "numeric_residuals": residuals,
        "shell_weight_maximum": shell_maximum,
        "dynamic_contact_maximum": contact_maximum,
        "dynamic_full_3D_band_minimum": band_minimum,
        "dynamic_axial_seam_maximum": seam_maximum,
        "technical_gates": technical_gates,
        "technical_pass": all(technical_gates.values()),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss_bytes(),
        "maximum_interacting_forward_RSS_bytes": maximum_interacting_forward_rss,
        "swaps": resource.getrusage(resource.RUSAGE_SELF).ru_nswap,
        "interacting_trace": interacting_trace,
        "free_trace": free_trace,
        "free_repeat_trace": free_repeat_trace,
    }
    signal.alarm(0)
    emit("SCIENCE_TRAIN_ROW", result)
    return result


def deletion_metrics(rows: list[dict]) -> tuple[dict[str, dict], dict[str, bool]]:
    primary = next(
        row for row in rows
        if row["role"] == "primary-mass-grid"
        and row["route"] == "C-sqrt-linear"
        and row["source_beta"] == "-4pi/9"
        and row["probe_beta"] == "-4pi/9"
    )
    metrics: dict[str, dict] = {}
    for row in rows:
        if row["role"] != "selected-deletion":
            continue
        metrics[row["deletion"]] = {
            "maximum_active_mediator": row["maximum_active_mediator"],
            "response_amplitude": row["response_amplitude"],
            "signal_floor": row["signal_floor"],
            "maximum_mediator_displacement": row["maximum_mediator_displacement"],
            "applied_contact_coupling": row["applied_contact_coupling"],
            "maximum_transverse_CAR_weight": row["maximum_transverse_CAR_weight"],
            "applied_source_factor": row["applied_source_factor"],
            "applied_probe_factor": row["applied_probe_factor"],
            "source_output": row["source_output"],
            "matched_primary_source_output": primary["source_output"],
            "matched_primary_response_amplitude": primary["response_amplitude"],
        }
    checks = pre.deletion_expectations(metrics)
    return metrics, checks


def science_train() -> None:
    train = contracts()
    emit("SCIENCE_TRAIN_COMMAND_CONTRACT", {
        "mode": "science-train",
        "manifest_order": True,
        "science_train_rows": SCIENCE_ROWS,
        "primary_rows": 27,
        "deletion_rows": 7,
        "direction_reversal_rows": 1,
        "free_partner": "sequential matched probe word with emitter=collision=0 and mediator parked",
        "repeated_free_per_row": True,
        "row_filtering": False,
        "held_rows": HELD_ROWS_EXECUTED,
        "refit": False,
    })
    started = time.monotonic()
    results = [run_row(index, row) for index, row in enumerate(train, start=1)]
    metrics, deletion_checks = deletion_metrics(results)
    deletion_pass = all(deletion_checks.values())
    route_results = {}
    for route in pre.ROUTES:
        primary_rows = [
            row for row in results if row["role"] == "primary-mass-grid" and row["route"] == route
        ]
        route_results[route] = pre.route_disposition(route, primary_rows, deletion_pass)
    reversal = next(row for row in results if row["role"] == "direction-reversal-control")
    canonical = next(
        row for row in results
        if row["role"] == "primary-mass-grid"
        and row["route"] == "C-sqrt-linear"
        and row["source_beta"] == "-4pi/9"
        and row["probe_beta"] == "-4pi/9"
    )
    summary = {
        "science_train_rows_completed": len(results),
        "science_train_manifest_sha256": TRAIN_MANIFEST_SHA256,
        "held_rows_executed": HELD_ROWS_EXECUTED,
        "refit_performed": False,
        "deletion_metrics": metrics,
        "deletion_checks": deletion_checks,
        "all_deletions_pass": deletion_pass,
        "route_dispositions": route_results,
        "direction_reversal_control": {
            "classification": reversal["classification"],
            "response_amplitude": reversal["response_amplitude"],
            "canonical_response_amplitude": canonical["response_amplitude"],
            "technical_pass": reversal["technical_pass"],
        },
        "total_elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": rss_bytes(),
        "swaps": resource.getrusage(resource.RUSAGE_SELF).ru_nswap,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "interpretation_boundary": "route-specific finite current/source tournament only; no shared obstruction or axiom pressure",
    }
    emit("SCIENCE_TRAIN_RESULT", summary)
    raise SystemExit(0 if len(results) == SCIENCE_ROWS else 1)


def dry_contract() -> None:
    train = contracts()
    emit("DRY_CONTRACT_RESULT", {
        "mode": "dry-contract",
        "contract_pass": True,
        "manifest_rows_verified": len(train),
        "science_train_rows_executed": 0,
        "held_rows_executed": 0,
        "row_filtering_available": False,
        "science_mode_is_all_or_nothing": True,
        "accepted_scout_evaluator_sha256": file_sha(SCOUT_EVALUATOR),
        "authority": AUTHORITY,
        "audit": AUDIT,
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("dry-contract", "science-train"), required=True)
    arguments = parser.parse_args()
    signal.signal(signal.SIGALRM, alarm_handler)
    if arguments.mode == "dry-contract":
        dry_contract()
    else:
        science_train()


if __name__ == "__main__":
    main()
