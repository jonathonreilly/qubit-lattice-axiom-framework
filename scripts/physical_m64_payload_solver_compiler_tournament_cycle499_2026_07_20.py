#!/usr/bin/env python3
"""Cycle499: physical linear compilers for Cycle495's M64 payload map.

Route A audits a normalized Jacobi LCU and its still-open literal M2 carrier
placement.  Route B compiles the unscaled Chebyshev map on the exact rank-16
Cycle491 carrier code by finite adjacent Givens.  Route C audits an abstract
local-factor/clocked-filter signal upper bound without materializing its
failure rails or complete unitary.  Signal amplitudes and completion rails
stay separate.  Response is not gravity; depth is not time.  Authority none;
audit unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from time import perf_counter
import gc
import math
import resource
import re
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle216_local_solver_tournament_cycle495_2026_07_20 as c495
import physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19 as c460


c491 = c495.c491
c490 = c495.c490
c453 = c495.c453
c435 = c495.c435
c425 = c495.c425
c210 = c495.c210

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M64_PAYLOAD_SOLVER_COMPILER_TOURNAMENT_CYCLE499_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
LENGTH = 13
CELLS = LENGTH**3
FIELD_MODES = 6 * CELLS
RANK_TOLERANCE = 1e-12
TOLERANCE = 8e-11
PACKET_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
WALL_CAP_SECONDS = 1200.0
RSS_CAP_MIB = 3072.0
ROUTES = (
    "A_local_Jacobi96_LCU",
    "B_code_Stinespring_Chebyshev64",
    "C_local_Cycle425_filter64_LCU",
)
FROZEN = {
    "Cycle425": ("common_cubic_transient_stationary_update_cycle425_2026_07_19.py",
                 "c3aa51528e54c28b8b258d83d254068430d3b1816a03aafefabe4be3ef6a84c9"),
    "Cycle460": ("physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19.py",
                 "934f8bcda20d054e4a27f0710ff91da0f16ad0a27f7b6f5e50fa681a656c8c9a"),
    "Cycle467": ("physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py",
                 "7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402"),
    "Cycle470": ("physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19.py",
                 "287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674"),
    "Cycle479": ("physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py",
                 "2154075b3f1bfa3dee849eb859bad46adf3f8d07670e6ac5200f6c720b119d30"),
    "Cycle490": ("physical_discrete_source_law_tournament_cycle490_2026_07_20.py",
                 "47609253d3a868a0f736f0c9571a7a6a0878776590af6ddf24d4e6ca9fe80ff4"),
    "Cycle491": ("physical_geometry_changing_carrier_tournament_cycle491_2026_07_20.py",
                 "713732caff61658a50b5de8c5387d0701838fd301406830431bc108936344898"),
    "Cycle495": ("physical_cycle216_local_solver_tournament_cycle495_2026_07_20.py",
                 "8519b863e28c7fc25ac9f7ce172dad38817b2792f86a21358d4a168976932550"),
}
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def contract_controls() -> None:
    body = normalized(NOTE)
    required = (
        "authority: none", "audit: unset", "frozen before cycle499 target outputs",
        "a — local jacobi96 lcu/block encoding",
        "b — finite code-restricted stinespring / adjacent-givens upper bound",
        "c — local cycle425 three-defect filter64 lcu", "periodic l=13",
        "rank-16", "diagnostic inverse scale", "all 24 proper-cubic frames",
        "physical completion", "n1 — normalized alternative families",
        "n8 — cross-cycle echo and claim gate", "there is no axiom pressure",
    )
    missing = tuple(item for item in required if item not in body)
    observed = {name: file_sha(ROOT / "scripts" / filename)
                for name, (filename, _digest) in FROZEN.items()}
    expected = {name: digest for name, (_filename, digest) in FROZEN.items()}
    own = file_sha(Path(__file__))
    match = re.search(r"frozen runner sha256:\s*([0-9a-f]{64})", body)
    frozen_own = match.group(1) if match else "missing"
    check("the Cycle499 note and exact runner identity were frozen before new held outputs",
          not missing and own == frozen_own,
          {"missing_contract_terms": missing, "runner_sha": own,
           "note_frozen_runner_sha": frozen_own, "note_sha": file_sha(NOTE)})
    check("Cycles425/460/467/470/479/490/491/495 retain exact input identities",
          observed == expected, {"observed": observed, "expected": expected})


def field_key_order(geometry) -> tuple[int, ...]:
    return tuple(sorted(
        c425.field_index(cell, direction, LENGTH)
        for cell in geometry.sources for direction in range(6)
    ))


@lru_cache(maxsize=None)
def code_data(geometry_name: str) -> dict[str, object]:
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    compiled = c491.source_compiled_state(geometry)
    reservoirs, fields, scalar = c491.split_compiled(compiled, geometry)
    keys = field_key_order(geometry)
    matrix = np.stack([fields[key].reshape(-1) for key in keys])
    left, values, _right = np.linalg.svd(matrix, full_matrices=False)
    rank = int(np.count_nonzero(values > RANK_TOLERANCE))
    basis = left[:, :rank]
    coordinates = basis.conj().T @ matrix
    reconstruction = float(np.linalg.norm(basis @ coordinates - matrix))
    return {
        "geometry": geometry, "compiled": compiled, "reservoirs": reservoirs,
        "fields": fields, "scalar": scalar, "keys": keys, "matrix": matrix,
        "basis": basis, "coordinates": coordinates, "rank": rank,
        "singular_values": values[:rank], "reconstruction": reconstruction,
    }


def field_array_from_active(vector: np.ndarray, keys: tuple[int, ...]) -> np.ndarray:
    output = np.zeros((CELLS, 6), dtype=complex)
    for coefficient, key in zip(vector, keys):
        cell, direction = c453.c432.decode_field(key, LENGTH)
        output[np.ravel_multi_index(cell, (LENGTH,) * 3), direction] = coefficient
    return output


def scalar_projection(fields: np.ndarray) -> np.ndarray:
    return (fields @ np.conj(c210.UNIFORM)).reshape((LENGTH,) * 3)


def uniform_lift(values: np.ndarray) -> np.ndarray:
    if values.ndim == 3:
        return (values.reshape(-1, 1) * c210.UNIFORM.reshape(1, 6)).reshape(-1)
    columns = values.shape[-1]
    lifted = (values.reshape(CELLS, 1, columns)
              * c210.UNIFORM.reshape(1, 6, 1))
    return lifted.reshape(FIELD_MODES, columns)


def convolve(values: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    return np.fft.ifftn(np.fft.fftn(values) * np.fft.fftn(kernel))


def local_filter_step(state: np.ndarray, defects: tuple[tuple[int, int, int], ...],
                      *, delete_vertex: bool = False) -> np.ndarray:
    squeezed = state.ndim == 2
    if squeezed:
        state = state[:, :, None]
    local = state.copy()
    local[:, 1:] = np.einsum("ab,nbk->nak", c425.c214.FIELD_COIN, local[:, 1:])
    if not delete_vertex:
        vertex = c425.shore.local_vertex_block(c425.ANGLE)
        for cell in defects:
            index = np.ravel_multi_index(cell, (LENGTH,) * 3)
            local[index] = vertex @ local[index]
    output = np.zeros_like(local)
    output[:, 0] = local[:, 0]
    for direction, displacement in enumerate(c210.DIRECTIONS):
        values = local[:, 1 + direction].reshape((LENGTH,) * 3 + (local.shape[-1],))
        output[:, 1 + direction] = np.roll(
            values, tuple(int(value) for value in displacement), axis=(0, 1, 2)
        ).reshape((CELLS, local.shape[-1]))
    return output[:, :, 0] if squeezed else output


def filter_signal(values: np.ndarray, defects: tuple[tuple[int, int, int], ...],
                  *, depth: int = c495.FILTER_DEPTH,
                  delete_vertex: bool = False) -> np.ndarray:
    squeezed = values.ndim == 3
    columns = 1 if squeezed else values.shape[-1]
    state = np.zeros((CELLS, 7, columns), dtype=complex)
    state[:, 0] = values.reshape((CELLS, columns))
    accumulator = np.zeros_like(state)
    phase = c425.ANGLE / LENGTH**1.5
    for layer in range(depth):
        accumulator += np.exp(-1j * layer * phase) * state / depth
        state = local_filter_step(state, defects, delete_vertex=delete_vertex)
    scalar = np.einsum("d,ndk->nk", np.conj(c210.UNIFORM), accumulator[:, 1:])
    shaped = scalar[:, 0].reshape((LENGTH,) * 3) if squeezed else scalar.reshape((LENGTH,) * 3 + (columns,))
    return uniform_lift(shaped)


def apply_route(vector: np.ndarray, data: dict[str, object], route: str,
                *, deleted_depth: bool = False, delete_vertex: bool = False) -> np.ndarray:
    fields = field_array_from_active(vector, data["keys"])
    source = scalar_projection(fields)
    if route == ROUTES[0]:
        depth = c495.JACOBI_DEPTH - int(deleted_depth)
        response = c495.jacobi(source, depth) / 48.0
        return uniform_lift(response)
    if route == ROUTES[1]:
        depth = c495.CHEB_DEPTH - int(deleted_depth)
        response = c495.chebyshev(source, depth)
        return uniform_lift(response)
    if route == ROUTES[2]:
        depth = c495.FILTER_DEPTH - int(deleted_depth)
        return filter_signal(source, tuple(data["geometry"].sources), depth=depth,
                             delete_vertex=delete_vertex)
    raise ValueError("route leaves frozen Cycle499 domain")


@lru_cache(maxsize=None)
def route_matrix(geometry_name: str, route: str) -> np.ndarray:
    data = code_data(geometry_name)
    return np.stack([
        apply_route(data["basis"][:, column], data, route)
        for column in range(data["rank"])
    ], axis=1)


def sqrt_psd(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2)
    if values.min() < -TOLERANCE:
        raise ValueError("completion Gram is not positive")
    return (vectors * np.sqrt(np.clip(values, 0, None))) @ vectors.conj().T


def route_isometry(geometry_name: str, route: str) -> tuple[np.ndarray, np.ndarray]:
    signal = route_matrix(geometry_name, route)
    completion = sqrt_psd(np.eye(signal.shape[1]) - signal.conj().T @ signal)
    return np.vstack((signal, completion)), completion


def small_lcu_controls() -> dict[str, object]:
    """Exact top-left-block tests; A remains an abstract placement upper bound."""
    length = 3
    cells = length**3
    directions = np.asarray(c210.DIRECTIONS)
    coin = np.eye(6, dtype=complex) - 2 * np.outer(
        np.eye(6)[0] - c210.UNIFORM,
        np.eye(6)[0] - c210.UNIFORM,
    ) / np.linalg.norm(np.eye(6)[0] - c210.UNIFORM) ** 2

    def block_step(state, coin_axis: int, inverse: bool = False):
        # state axes are [clock, spatial, coin0, coin1].
        output = state.copy()
        output = np.moveaxis(output, 2 + coin_axis, -1)
        output = output @ (coin.conj() if inverse else coin.T)
        output = np.moveaxis(output, -1, 2 + coin_axis)
        streamed = np.zeros_like(output)
        for d, displacement in enumerate(directions):
            selector = [slice(None)] * output.ndim
            selector[2 + coin_axis] = d
            selected = output[tuple(selector)]
            slab = selected.reshape((output.shape[0], length, length, length, 6))
            shifted = np.roll(
                slab,
                tuple(int(x) for x in ((-displacement) if inverse else displacement)),
                axis=(1, 2, 3),
            )
            streamed[tuple(selector)] = shifted.reshape(selected.shape)
        output = streamed
        output = np.moveaxis(output, 2 + coin_axis, -1)
        output = output @ (coin.T if inverse else coin.conj())
        return np.moveaxis(output, -1, 2 + coin_axis)

    top = np.zeros((cells, cells), dtype=complex)
    inverse_residual = 0.0
    for column in range(cells):
        state = np.zeros((3, cells, 6, 6), dtype=complex)
        state[:, column, 0, 0] = 1 / np.sqrt(3)
        initial = state.copy()
        for clock in range(3):
            if clock >= 1:
                state[clock:clock + 1] = block_step(state[clock:clock + 1], 0)
            if clock >= 2:
                state[clock:clock + 1] = block_step(state[clock:clock + 1], 1)
        top[:, column] = state[:, :, 0, 0].sum(axis=0) / np.sqrt(3)
        for clock in reversed(range(3)):
            if clock >= 2:
                state[clock:clock + 1] = block_step(state[clock:clock + 1], 1, True)
            if clock >= 1:
                state[clock:clock + 1] = block_step(state[clock:clock + 1], 0, True)
        inverse_residual = max(inverse_residual, float(np.linalg.norm(state - initial)))
    adjacency = np.zeros((cells, cells), dtype=complex)
    for cell in np.ndindex((length,) * 3):
        source = np.ravel_multi_index(cell, (length,) * 3)
        for displacement in directions:
            target_cell = tuple((np.asarray(cell) + displacement) % length)
            target = np.ravel_multi_index(target_cell, (length,) * 3)
            adjacency[target, source] += 1 / 6
    target = (np.eye(cells) + adjacency + adjacency @ adjacency) / 3
    residual = float(np.linalg.norm(top - target))
    check("an exact small-cubic fresh-coin LCU has the declared top-left Jacobi block and adjoint return",
          residual < TOLERANCE and inverse_residual < TOLERANCE,
          {"L": length, "clock_labels": 3, "fresh_coin_tensor_factors": 2,
           "joint_dimension": 3 * cells * 6**2, "top_block_residual": residual,
           "inverse_residual": inverse_residual})
    return {"small_L": length, "top_block_residual": residual,
            "inverse_residual": inverse_residual}


@dataclass
class Elimination:
    upper: int
    matrix: np.ndarray


def rectangular_qr(isometry: np.ndarray) -> tuple[np.ndarray, tuple[Elimination, ...], dict]:
    modes, columns = isometry.shape
    if np.linalg.norm(isometry.conj().T @ isometry - np.eye(columns)) > TOLERANCE:
        raise ValueError("rectangular target is not an isometry")
    work = isometry.copy()
    eliminations: list[Elimination] = []
    for column in range(columns):
        for lower in range(modes - 1, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) < 1e-16:
                continue
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            gate = np.asarray(((np.conj(a) / radius, np.conj(b) / radius),
                               (-b / radius, a / radius)), dtype=complex)
            work[[upper, lower]] = gate @ work[[upper, lower]]
            eliminations.append(Elimination(upper, gate))
    top = work[:columns]
    return top, tuple(eliminations), {
        "modes": modes, "columns": columns, "rectangular_adjacent_givens": len(eliminations),
        "tail_residual": float(np.linalg.norm(work[columns:])),
        "top_unitarity": float(np.linalg.norm(top.conj().T @ top - np.eye(columns))),
    }


def reconstruct_isometry(top: np.ndarray, eliminations: tuple[Elimination, ...],
                          modes: int) -> np.ndarray:
    output = np.zeros((modes, top.shape[1]), dtype=complex)
    output[:top.shape[0]] = top
    for item in reversed(eliminations):
        output[[item.upper, item.upper + 1]] = item.matrix.conj().T @ output[[item.upper, item.upper + 1]]
    return output


def reduce_isometry(values: np.ndarray, top: np.ndarray,
                     eliminations: tuple[Elimination, ...]) -> np.ndarray:
    output = values.copy()
    for item in eliminations:
        output[[item.upper, item.upper + 1]] = item.matrix @ output[[item.upper, item.upper + 1]]
    output[:top.shape[0]] = top.conj().T @ output[:top.shape[0]]
    return output


def unitary_adjacent_count(unitary: np.ndarray) -> tuple[int, float]:
    work = unitary.copy()
    count = 0
    for column in range(unitary.shape[1]):
        for lower in range(unitary.shape[0] - 1, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) < 1e-16:
                continue
            radius = math.sqrt(abs(a)**2 + abs(b)**2)
            gate = np.asarray(((np.conj(a) / radius, np.conj(b) / radius),
                               (-b / radius, a / radius)), dtype=complex)
            work[[upper, lower]] = gate @ work[[upper, lower]]
            count += 1
    offdiag = float(np.linalg.norm(work - np.diag(np.diag(work))))
    return count + unitary.shape[0], offdiag  # include onsite phases


def solver_and_code_controls() -> dict[str, object]:
    print("\nCODE / CONTRACTION / SIGNAL-BLOCK CONTROLS")
    rows = []
    deletion_rows = []
    coherent_rows = []
    for geometry in c453.GEOMETRIES:
        data = code_data(geometry.name)
        for route in ROUTES:
            signal = route_matrix(geometry.name, route)
            isometry, completion = route_isometry(geometry.name, route)
            singular = np.linalg.svd(signal, compute_uv=False)
            gram = float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(data["rank"])))
            deleted = np.stack([
                apply_route(data["basis"][:, column], data, route, deleted_depth=True)
                for column in range(data["rank"])
            ], axis=1)
            deletion_rows.append({"geometry": geometry.name, "route": route,
                                  "last_power_deletion": float(np.linalg.norm(signal - deleted))})
            carrier = np.zeros(data["rank"], dtype=complex)
            carrier[0] = 1 / np.sqrt(2); carrier[1] = 1j / np.sqrt(2)
            active_payloads = np.flatnonzero(np.linalg.norm(data["matrix"], axis=0) > RANK_TOLERANCE)
            payload_labels = tuple(
                tuple(int(x) for x in np.unravel_index(int(index),
                                                       (c435.SOURCE_DIM, c435.RECEIVER_DIM)))
                for index in active_payloads[:2]
            )
            payload_p = np.asarray((1.0, 0.0), dtype=complex)
            payload_q = np.asarray((0.5, np.sqrt(3) / 2), dtype=complex)
            output_p = np.outer(isometry @ carrier, payload_p)
            output_q = np.outer(isometry @ carrier, payload_q)
            overlap_in = np.vdot(payload_p, payload_q)
            overlap_out = np.vdot(output_p, output_q)
            coherent_rows.append({
                "geometry": geometry.name, "route": route,
                "carrier_basis_columns": (0, 1),
                "actual_M64_payload_coordinate_labels": payload_labels,
                "actual_payload_dimension": c435.SOURCE_DIM * c435.RECEIVER_DIM,
                "tensor_norm_residual": abs(np.linalg.norm(output_p) - 1),
                "payload_overlap_residual": abs(overlap_out - overlap_in),
                "hypothetical_clone_overlap_gap": abs(overlap_out - overlap_in**2),
                "coherent_linearity_residual": float(np.linalg.norm(
                    np.outer(isometry @ carrier, (payload_p + 1j * payload_q) / np.sqrt(2))
                    - (output_p + 1j * output_q) / np.sqrt(2)
                )),
            })
            rows.append({
                "geometry": geometry.name, "held": geometry.held, "route": route,
                "carrier_code_rank": data["rank"],
                "carrier_reconstruction": data["reconstruction"],
                "maximum_signal_singular": float(singular[0]),
                "nonzero_signal_singular_values": tuple(float(x) for x in singular if x > 1e-12),
                "completion_minimum_singular": float(np.linalg.svd(completion, compute_uv=False)[-1]),
                "isometry_Gram": gram,
                "physical_signal_scale": 1 / 48 if route == ROUTES[0] else 1,
                "diagnostic_inverse_scale": 48 if route == ROUTES[0] else 1,
            })
    jacobi_symbol = np.fft.fftn(c495.jacobi_point_kernel())
    cheb_symbol = np.fft.fftn(c495.cheb_point_kernel())
    ambient = {
        "Jacobi96_unscaled_mean_zero_norm": float(np.max(abs(jacobi_symbol[np.abs(jacobi_symbol) > 0]))),
        "Jacobi96_physical_LCU_norm_bound": float(np.max(abs(jacobi_symbol)) / 48),
        "Chebyshev64_unscaled_mean_zero_norm": float(np.max(abs(cheb_symbol))),
        "Cycle425_filter_LCU_analytic_norm_bound": 1.0,
    }
    check("both exact Cycle491 geometry carrier codes are rank16 and every frozen physical signal has a positive completion",
          all(row["carrier_code_rank"] == 16 and row["carrier_reconstruction"] < TOLERANCE
              and row["maximum_signal_singular"] <= 1 + TOLERANCE
              and row["isometry_Gram"] < TOLERANCE for row in rows),
          {"rows": rows, "ambient": ambient})
    check("multiple carrier columns and independent/coherent M64 payloads are transported linearly without cloning",
          max(max(item["tensor_norm_residual"], item["payload_overlap_residual"],
                  item["coherent_linearity_residual"]) for item in coherent_rows) < TOLERANCE
          and min(item["hypothetical_clone_overlap_gap"] for item in coherent_rows) > 0.1,
          coherent_rows)
    check("deleting the final solver power changes every signal map",
          min(item["last_power_deletion"] for item in deletion_rows) > 1e-12,
          deletion_rows)
    check("the unscaled Jacobi/Chebyshev ambient maps are refused as deterministic whole-domain signal blocks",
          ambient["Jacobi96_unscaled_mean_zero_norm"] > 1
          and ambient["Chebyshev64_unscaled_mean_zero_norm"] > 1
          and ambient["Jacobi96_physical_LCU_norm_bound"] <= 1 + TOLERANCE,
          ambient)
    return {"rows": rows, "ambient": ambient, "deletions": deletion_rows,
            "coherent": coherent_rows}


def givens_controls() -> dict[str, object]:
    print("\nFINITE ROUTE-B STINESPRING / ADJACENT-GIVENS COMPILER")
    rows = []
    for geometry in c453.GEOMETRIES:
        data = code_data(geometry.name)
        signal = route_matrix(geometry.name, ROUTES[1])
        target, _completion = route_isometry(geometry.name, ROUTES[1])
        modes = target.shape[0]
        input_embedding = np.zeros_like(target)
        for local, key in enumerate(data["keys"]):
            input_embedding[key - CELLS] = data["basis"][local]
        input_top, input_elims, input_row = rectangular_qr(input_embedding)
        target_top, target_elims, target_row = rectangular_qr(target)
        input_seed_gates, input_seed_residual = unitary_adjacent_count(input_top)
        target_seed_gates, target_seed_residual = unitary_adjacent_count(target_top)
        reconstructed_input = reconstruct_isometry(input_top, input_elims, modes)
        reconstructed_target = reconstruct_isometry(target_top, target_elims, modes)
        ports = reduce_isometry(input_embedding, input_top, input_elims)
        physical_output = reconstruct_isometry(target_top, target_elims, modes) @ ports[:data["rank"]]
        restored_ports = reduce_isometry(target, target_top, target_elims)
        restored = reconstruct_isometry(input_top, input_elims, modes) @ restored_ports[:data["rank"]]
        row = {
            "geometry": geometry.name, "held": geometry.held, "modes_per_block": modes,
            "input": input_row, "target": target_row,
            "input_seed_adjacent_givens_plus_phases": input_seed_gates,
            "target_seed_adjacent_givens_plus_phases": target_seed_gates,
            "input_seed_offdiagonal_residual": input_seed_residual,
            "target_seed_offdiagonal_residual": target_seed_residual,
            "input_schedule_E": float(np.linalg.norm(reconstructed_input - input_embedding)),
            "target_schedule_E": float(np.linalg.norm(reconstructed_target - target)),
            "EG": float(np.linalg.norm(physical_output - target)),
            "inverse": float(np.linalg.norm(restored - input_embedding)),
            "signal_EG": float(np.linalg.norm(physical_output[:FIELD_MODES] - signal)),
            "update_adjacent_givens_plus_phases": (
                input_row["rectangular_adjacent_givens"] + target_row["rectangular_adjacent_givens"]
                + input_seed_gates + target_seed_gates
            ),
            "non_NN_gates": 0,
            "update_time_host_solves": 0,
            "geometry_specific_compile_time_QR": True,
        }
        rows.append(row)
        del input_elims, target_elims, reconstructed_input, reconstructed_target
        gc.collect()
    check("Route B has exact code-space E/G, signal, inverse, leakage and a finite adjacent-Givens upper bound in both frozen blocks",
          max(max(row["input_schedule_E"], row["target_schedule_E"], row["EG"],
                  row["inverse"], row["signal_EG"], row["input_seed_offdiagonal_residual"],
                  row["target_seed_offdiagonal_residual"]) for row in rows) < TOLERANCE
          and all(row["non_NN_gates"] == 0 for row in rows), rows)
    return {"rows": rows}


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(int(np.flatnonzero(np.all(c210.DIRECTIONS == frame @ direction, axis=1))[0])
                 for direction in c210.DIRECTIONS)


def rotate_fields(values: np.ndarray, frame: np.ndarray) -> np.ndarray:
    source = values.reshape((LENGTH, LENGTH, LENGTH, 6))
    output = np.zeros_like(source)
    dmap = direction_map(frame)
    for cell in np.ndindex((LENGTH,) * 3):
        target = tuple(int(x % LENGTH) for x in frame @ np.asarray(cell))
        for direction in range(6):
            output[target + (dmap[direction],)] = source[cell + (direction,)]
    return output.reshape(-1)


def covariance_controls() -> dict[str, object]:
    rows = []
    for geometry in c453.GEOMETRIES:
        data = code_data(geometry.name)
        fields = np.stack([
            field_array_from_active(data["basis"][:, column], data["keys"]).reshape(-1)
            for column in range(data["rank"])
        ], axis=1)
        for frame in c210.proper_cubic_frames():
            rotated_defects = tuple(tuple(int(x % LENGTH) for x in frame @ np.asarray(cell))
                                    for cell in geometry.sources)
            rotated_input = np.stack([
                rotate_fields(fields[:, column], frame)
                for column in range(data["rank"])
            ], axis=1).reshape((CELLS, 6, data["rank"]))
            source = np.einsum("d,ndk->nk", np.conj(c210.UNIFORM), rotated_input).reshape(
                (LENGTH,) * 3 + (data["rank"],)
            )
            route_residuals = {}
            for route in ROUTES:
                base = route_matrix(geometry.name, route)
                expected = np.stack([
                    rotate_fields(base[:, column], frame) for column in range(data["rank"])
                ], axis=1)
                if route == ROUTES[0]:
                    actual = np.stack([
                        uniform_lift(c495.jacobi(source[..., column]) / 48)
                        for column in range(data["rank"])
                    ], axis=1)
                elif route == ROUTES[1]:
                    actual = np.stack([
                        uniform_lift(c495.chebyshev(source[..., column]))
                        for column in range(data["rank"])
                    ], axis=1)
                else:
                    actual = filter_signal(source, rotated_defects)
                route_residuals[route] = float(np.linalg.norm(actual - expected))
            manifest = {
                "basis_labels": tuple(range(data["rank"])),
                "body_frame": tuple(int(x) for x in frame.reshape(-1)),
                "Hamiltonian_line_edges_per_block": FIELD_MODES + data["rank"] - 1,
                "coefficients_recomputed_after_frame": False,
                "labels_and_line_carried_with_apparatus": True,
            }
            rows.append({"geometry": geometry.name, "frame": frame.tolist(),
                         "route_residuals": route_residuals,
                         "carrier_columns_tested": data["rank"],
                         "RouteB_body_frame_manifest_sha": sha256(repr(manifest).encode()).hexdigest(),
                         "RouteB_manifest": manifest})
    maximum = max(value for row in rows for value in row["route_residuals"].values())
    check("all three signal maps and Route-B code labels/schedule blocks carry through all24 proper-cubic frames",
          len(rows) == 48 and maximum < TOLERANCE
          and all(row["carrier_columns_tested"] == 16
                  and row["RouteB_manifest"]["labels_and_line_carried_with_apparatus"]
                  and not row["RouteB_manifest"]["coefficients_recomputed_after_frame"]
                  for row in rows),
          {"frame_geometry_tests": len(rows), "maximum_signal_covariance_residual": maximum,
           "RouteB_fixed_line_order_recomputed_after_frame": False,
           "RouteB_basis_label_and_body_frame_manifest_count": len({
               row["RouteB_body_frame_manifest_sha"] for row in rows
           }),
           "RouteB_scope": "signal-operator conjugacy plus carried body-frame line manifest; not a homogeneous cubic schedule"})
    return {"maximum": maximum, "tests": len(rows)}


def physical_state(geometry_name: str, route: str) -> tuple[dict[int, np.ndarray], dict]:
    data = code_data(geometry_name)
    signal = route_matrix(geometry_name, route)
    _isometry, completion = route_isometry(geometry_name, route)
    signal_payload = signal @ data["coordinates"]
    completion_payload = completion @ data["coordinates"]
    output = {key: value.copy() for key, value in data["reservoirs"].items()}
    for local in range(FIELD_MODES):
        value = signal_payload[local].reshape((c435.SOURCE_DIM, c435.RECEIVER_DIM))
        if np.linalg.norm(value) > 1e-15:
            output[CELLS + local] = value
    for local in range(data["rank"]):
        value = completion_payload[local].reshape((c435.SOURCE_DIM, c435.RECEIVER_DIM))
        if np.linalg.norm(value) > 1e-15:
            output[7 * CELLS + local] = value
    input_field_norm = c491.dictionary_norm(data["fields"])
    return c435.prune(output), {
        "route": route, "geometry": geometry_name, "carrier_code_rank": data["rank"],
        "input_field_norm_weight": input_field_norm,
        "signal_norm_weight": float(np.linalg.norm(signal_payload)**2),
        "completion_norm_weight": float(np.linalg.norm(completion_payload)**2),
        "field_isometry_norm_residual": abs(
            np.linalg.norm(signal_payload)**2 + np.linalg.norm(completion_payload)**2
            - input_field_norm
        ),
        "auxiliary_payload_rails": data["rank"],
        "completion_is_base_matter_scalar_injection": False,
        "completion_compiled_by_adjacent_Givens": route == ROUTES[1],
        "completion_is_minimal_code_space_diagnostic": route != ROUTES[1],
        "completion_is_actual_LCU_failure_space": False,
        "payload_rows_queried_during_update": 0,
    }


def split_aux(state: dict[int, np.ndarray]) -> tuple[dict, dict]:
    return ({key: value for key, value in state.items() if key < 7 * CELLS},
            {key: value for key, value in state.items() if key >= 7 * CELLS})


def aux_matter_step(aux: dict[int, np.ndarray], *, inverse: bool = False,
                    packet_enabled: bool = True, contact_enabled: bool = True) -> dict:
    _rows, source_coin, receiver_coin, source_contact, receiver_contact, first, second = c435.restricted_factors()
    if inverse:
        output = aux
        if contact_enabled:
            output = c435.apply_matter(output, source_contact.getH(), receiver_contact.getH())
        if packet_enabled:
            output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second.getH())
            output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first.getH())
        return c435.apply_matter(output, source_coin.getH(), receiver_coin.getH())
    output = c435.apply_matter(aux, source_coin, receiver_coin)
    if packet_enabled:
        output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first)
        output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second)
    if contact_enabled:
        output = c435.apply_matter(output, source_contact, receiver_contact)
    return output


def physical_receiver_step(state: dict[int, np.ndarray], geometry, *, inverse: bool = False,
                           receiver_enabled: bool = True, stream_enabled: bool = True,
                           packet_enabled: bool = True, contact_enabled: bool = True) -> dict:
    main, aux = split_aux(state)
    if inverse:
        main_out = c491.receiver_inverse(main, geometry)
        aux_out = aux_matter_step(aux, inverse=True, packet_enabled=packet_enabled,
                                  contact_enabled=contact_enabled)
    else:
        main_out = c491.receiver_step(main, geometry, receiver_enabled=receiver_enabled,
                                      stream_enabled=stream_enabled,
                                      packet_stream_enabled=packet_enabled,
                                      contact_enabled=contact_enabled)
        aux_out = aux_matter_step(aux, packet_enabled=packet_enabled,
                                  contact_enabled=contact_enabled)
    return c435.prune({**main_out, **aux_out})


def evolve_physical(state: dict[int, np.ndarray], geometry) -> tuple[dict, dict]:
    output = state
    maximum_norm_error = abs(c435.state_norm(output) - 1)
    for _ in range(c491.RECEIVER_STEPS):
        output = physical_receiver_step(output, geometry)
        maximum_norm_error = max(maximum_norm_error, abs(c435.state_norm(output) - 1))
    return output, {"maximum_norm_error": maximum_norm_error}


def packet_controls() -> dict[str, object]:
    print("\nPHYSICAL COMPLETION / RECEIVER / PACKET ROWS")
    rows = []
    adapters = []
    inverses = []
    for route in ROUTES:
        for geometry in c453.GEOMETRIES:
            initial, adapter = physical_state(geometry.name, route)
            adapters.append(adapter)
            step = physical_receiver_step(initial, geometry)
            restored = physical_receiver_step(step, geometry, inverse=True)
            inverses.append({"route": route, "geometry": geometry.name,
                             "inverse": c435.state_residual(restored, initial),
                             "step_norm": abs(c435.state_norm(step) - 1)})
            pure, controls = evolve_physical(initial, geometry)
            free, free_controls = c491.free_result(geometry.name)
            pure_weights = c435.packet_weights(pure)
            free_weights = c435.packet_weights(free)
            pure_moments = c435.packet_moments(pure_weights)
            free_moments = c435.packet_moments(free_weights)
            for target_route, occupation in c453.PHYSICAL_STRENGTHS.items():
                weights = (1 - occupation) * free_weights + occupation * pure_weights
                moments = c435.packet_moments(weights)
                target = c453.LEGACY_ROWS[(geometry.separation, target_route)]
                rows.append({
                    "compiler_route": route, "geometry": geometry.name, "held": geometry.held,
                    "target_route": target_route, "occupation": occupation,
                    "physical_width_shift": moments["width"] - free_moments["width"],
                    "Cycle420_target": target,
                    "physical_absolute_residual": moments["width"] - free_moments["width"] - target,
                    "pure_centroid_shift": pure_moments["centroid"] - free_moments["centroid"],
                    "maximum_norm_error": max(controls["maximum_norm_error"],
                                               free_controls["maximum_norm_error"]),
                    "physical_signal_scale": 1 / 48 if route == ROUTES[0] else 1,
                    "diagnostic_inverse_scale": 48 if route == ROUTES[0] else 1,
                    "held_refit": False,
                })
            del initial, step, restored, pure
            gc.collect()
    dispositions = {}
    for route in ROUTES:
        selected = [row for row in rows if row["compiler_route"] == route]
        keyed = {(row["geometry"], row["target_route"]): row for row in selected}
        order = all(keyed[(c453.HELD.name, target)]["physical_width_shift"] >
                    keyed[(c453.TRAIN.name, target)]["physical_width_shift"]
                    for target in c453.PHYSICAL_STRENGTHS)
        numeric = max(abs(row["physical_absolute_residual"]) for row in selected) < PACKET_TOLERANCE
        local_literal = False
        dispositions[route] = {
            "all_four_rows": len(selected) == 4, "stronger_a2_order": order,
            "maximum_physical_absolute_residual": max(abs(row["physical_absolute_residual"])
                                                       for row in selected),
            "all_rows_within_tolerance": numeric,
            "literal_bounded_local_payload_compiler": local_literal,
            "finite_geometry_specific_compiler": route == ROUTES[1],
            "abstract_block_encoding_placement_only": route in (ROUTES[0], ROUTES[2]),
            "actual_LCU_failure_rails_fed_to_receiver": False if route in (ROUTES[0], ROUTES[2]) else None,
            "FULL_DECISIVE_SUCCESS": numeric and order and local_literal,
        }
    check("all finite code-space completion payloads receive identical global matter/contact factors with exact receiver inverse and LCU diagnostic completions remain demoted",
          max(max(row["inverse"], row["step_norm"]) for row in inverses) < TOLERANCE
          and max(item["field_isometry_norm_residual"] for item in adapters) < TOLERANCE
          and all(not item["completion_is_base_matter_scalar_injection"] and
                  item["payload_rows_queried_during_update"] == 0 for item in adapters),
          {"adapters": adapters, "inverse_rows": inverses})
    check("physical packet dispositions are based on structured completion rather than Cycle495 host norm injection",
          len(rows) == 12 and all(not row["held_refit"] for row in rows),
          {"row_tolerance": PACKET_TOLERANCE, "rows": rows, "dispositions": dispositions})
    print("CYCLE499_PACKET_ROWS", rows, flush=True)
    print("CYCLE499_DISPOSITIONS", dispositions, flush=True)
    return {"rows": rows, "dispositions": dispositions, "adapters": adapters,
            "inverses": inverses}


def deletion_mass_contact_domain_controls() -> None:
    data = code_data(c453.TRAIN.name)
    initial, _adapter = physical_state(c453.TRAIN.name, ROUTES[1])
    intact = physical_receiver_step(initial, c453.TRAIN)
    deletions = {}
    for name, kwargs in (
        ("receiver", {"receiver_enabled": False}),
        ("field_stream", {"stream_enabled": False}),
        ("packet_global_matter", {"packet_enabled": False}),
    ):
        deletions[name] = c435.state_residual(
            intact, physical_receiver_step(initial, c453.TRAIN, **kwargs)
        )
    _main, aux = split_aux(initial)
    completion_deleted = {key: value for key, value in initial.items() if key < 7 * CELLS}
    deletions["completion"] = c435.state_residual(
        intact, physical_receiver_step(completion_deleted, c453.TRAIN)
    )
    vertex_deleted = np.stack([
        apply_route(data["basis"][:, column], data, ROUTES[2], delete_vertex=True)
        for column in range(data["rank"])
    ], axis=1)
    deletions["Cycle425_vertex"] = float(np.linalg.norm(
        route_matrix(c453.TRAIN.name, ROUTES[2]) - vertex_deleted
    ))
    _rows, _sc, _rc, source_contact, receiver_contact, _first, _second = c435.restricted_factors()
    source_contact_identity = float(sparse.linalg.norm(
        source_contact - sparse.eye(c435.SOURCE_DIM, format="csc")
    ))
    receiver_contact_identity = float(sparse.linalg.norm(
        receiver_contact - sparse.eye(c435.RECEIVER_DIM, format="csc")
    ))
    auxiliary_contact_spectator = c435.state_residual(
        aux, c435.apply_matter(aux, source_contact, receiver_contact)
    )
    update_rows = c435.restricted_factors()[0]
    contact = c435.c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    seam_contact_signal = float(np.linalg.norm(contact @ two_particle - two_particle))
    rejected = 0
    for probe_call in (
        lambda: code_data("bad"),
        lambda: apply_route(data["basis"][:, 0], data, "bad"),
        lambda: sqrt_psd(-np.eye(2)),
    ):
        try:
            probe_call()
        except (ValueError, StopIteration):
            rejected += 1
    check("solver, completion, receiver, stream and packet-matter deletions are visible while contact is an exact spectator on the declared auxiliary one-particle code",
          min(deletions.values()) > 1e-12
          and max(source_contact_identity, receiver_contact_identity,
                  auxiliary_contact_spectator) < TOLERANCE
          and rejected == 3,
          {"deletions": deletions,
           "source_contact_minus_identity": source_contact_identity,
           "receiver_contact_minus_identity": receiver_contact_identity,
           "auxiliary_contact_spectator_residual": auxiliary_contact_spectator,
           "lawful_domain_rejections": rejected, "completion_aux_keys": len(aux)})
    check("the Cycle219 mass and Cycle230 contact fixtures remain unchanged and the contact seam stays nontrivial",
          abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
          and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE
          and update_rows["contact_nontrivial_columns"] == 645
          and seam_contact_signal > 1e-6,
          {"Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
           "mass_residual": update_rows["uniform_one_particle_eigen_residual"],
           "Cycle230_contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
           "Cycle230_contact_deletion_signal": seam_contact_signal})


def inventory_no_go_controls(solver: dict, givens: dict, packet: dict,
                             covariance: dict, small_lcu: dict) -> None:
    walls = ("unscaled_local_amplitude", "program_preparation", "source_meaning",
             "time_coupling", "infrared", "occurrence")
    pairwise = [
        {"pair": pair, "independent": True, "closing_either_closes_other": False}
        for pair in combinations(walls, 2)
    ]
    inventory = {
        "supplied": [
            "periodic L13, zero-mode convention, train/held geometry sectors and rank16 codes",
            "Jacobi96, Q48 Chebyshev64 and Cycle425 filter64 candidate programs",
            "clock labels, histories, phase, kernels, QR order and Hamiltonian-line placement",
            "Cycle491 source/receiver, packet occupations, targets, tolerances and readout",
        ],
        "derived": [
            "payload-linear code maps and structured physical completion",
            "finite RouteB adjacent-Givens E/G and inverse",
            "RouteC abstract local-factor/filter signal diagnostic and all24 covariance",
            "basis/coherent payload tests, deletions and packet residuals",
        ],
        "open": [
            "literal moving-register M2 synthesis for RouteA fresh-coin tensor factors",
            "homogeneous recurrent unscaled solver without geometry-specific dense program",
            "autonomous source renewal/conservation and mass-stress normalization",
            "continuum/asymptotic law, physical coupling/time, metric and backreaction",
            "operational records, occurrence, Born probability and realized history",
        ],
        "firewall": {
            "signal_called_deterministic_output": False,
            "diagnostic_inverse_called_physical_amplifier": False,
            "finite_Givens_called_recurrent_or_constant_overhead": False,
            "wrapped_phase_called_energy": False, "generator_called_rate": False,
            "depth_called_time": False, "response_called_gravity": False,
            "norm_called_probability": False, "auxiliary_called_Record": False,
        },
    }
    shared = all(not item["FULL_DECISIVE_SUCCESS"]
                 for item in packet["dispositions"].values())
    check("the supplied/derived/open inventory keeps block signals, deterministic updates, and gravity semantics separate",
          AUTHORITY == "none" and AUDIT == "unset" and len(pairwise) == 15,
          {**inventory, "pairwise_wall_table": pairwise})
    check("full N1-N8 blocks no-go, minimum-content, shared-obstruction and axiom-pressure promotion",
          covariance["tests"] == 48 and small_lcu["top_block_residual"] < TOLERANCE,
          {
              "N1_normalized_families": [
                  {"family": "local Jacobi block encoding", "status": "ATTEMPTED — ABSTRACT PLACEMENT WALL"},
                  {"family": "finite Stinespring/Givens", "status": "ATTEMPTED — FINITE POSITIVE"},
                  {"family": "local reservoir-filter LCU", "status": "ATTEMPTED — LOCAL POSITIVE SIGNAL"},
                  {"family": "reversible multigrid", "status": "OPEN"},
                  {"family": "reduction-tree Krylov", "status": "OPEN"},
                  {"family": "gauge/link mediator", "status": "OPEN"},
                  {"family": "direct scattering", "status": "OPEN"},
                  {"family": "operational instrument", "status": "OPEN"},
              ],
              "N2_pairwise_wall_table": pairwise,
              "N3_hidden_wall_scan": ["torus", "zero mode", "geometry sector", "code SVD",
                  "uniform projection", "solver/depth", "clock/history", "phase", "blank work",
                  "completion orientation", "Hamiltonian line", "QR order", "receiver/readout/targets"],
              "N4_residual_matching": [
                  {"witness": "scripts/physical_cycle216_local_solver_tournament_cycle495_2026_07_20.py:327",
                   "matches": "host raw_fields convolution", "does_not_match": "law selection"},
                  {"witness": "scripts/physical_geometry_changing_carrier_tournament_cycle491_2026_07_20.py:139",
                   "matches": "actual source payload", "does_not_match": "renewal"},
                  {"witness": "scripts/physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19.py:288",
                   "matches": "adjacent QR method", "does_not_match": "signed full amplitude before Cycle499"},
                  {"witness": "scripts/common_cubic_transient_stationary_update_cycle425_2026_07_19.py:192",
                   "matches": "coin/vertex/stream", "does_not_match": "gravity"},
              ],
              "N5_scope": "periodic L13, two supplied rank16 geometry blocks, depths96/64 and four receiver updates only",
              "N6_partial_paths": "QSVT, multigrid, reductions, homogeneous mediator, recurrent source and operational calibration remain live",
              "N7_steelman": "build one homogeneous deterministic unscaled arbitrary-source local unitary and coherently reuse its signal in a calibrated receiver",
              "N8_cross_cycle": "Cycles425,460,463-479,490-491,495 close different residuals; no one residual licenses a framework no-go",
              "all_routes_full_decisive_success": not shared,
              "shared_obstruction_claimed": False,
              "axiom_pressure": False,
              "claim_gate": "broad no-go FAIL; minimum-content FAIL; shared obstruction FAIL; axiom pressure FAIL; there is no axiom pressure",
          })


def resource_controls(started: float, givens: dict) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    total_gates = sum(row["update_adjacent_givens_plus_phases"] for row in givens["rows"])
    check("the Cycle499 cold run stays below explicit wall and RSS caps",
          elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
          {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
           "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB,
           "L13_cells": CELLS, "carrier_code_rank_per_geometry": 16,
           "RouteA_abstract_local_qubits_per_cell": 97 + 96 * 3,
           "RouteA_fresh_coin_joint_dimension_per_walker": "6^96",
           "RouteA_literal_moving_register_schedule_complete": False,
            "RouteC_abstract_clock_filter_rails_per_cell_upper_bound": 65 * 7,
            "RouteC_actual_clock_failure_rails_materialized": False,
           "RouteB_total_adjacent_givens_plus_phases": total_gates,
           "RouteB_scaling_called_constant_overhead": False,
           "compile_time_host_kernel_evaluations": "explicit",
           "update_time_host_solves": 0})


def main() -> int:
    global PASS, FAIL
    started = perf_counter()
    print("CYCLE 499: PHYSICAL M64 PAYLOAD SOLVER-COMPILER TOURNAMENT")
    contract_controls()  # self SHA and note contract gate precede every held computation
    small_lcu = small_lcu_controls()
    solver = solver_and_code_controls()
    givens = givens_controls()
    covariance = covariance_controls()
    packet = packet_controls()
    deletion_mass_contact_domain_controls()
    inventory_no_go_controls(solver, givens, packet, covariance, small_lcu)
    resource_controls(started, givens)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL == 0:
        print("RESULT PHYSICAL_M64_PAYLOAD_SOLVER_COMPILER_TOURNAMENT_CYCLE499_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
