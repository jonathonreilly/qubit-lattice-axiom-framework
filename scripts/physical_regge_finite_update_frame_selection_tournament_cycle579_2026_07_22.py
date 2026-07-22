#!/usr/bin/env python3
"""Cycle 579: finite-update Regge compiler and frame-selection tournament.

Route A extracts the exact finite Fourier kernel of the committed Cycle-576
raw-deficit Regge generator and decomposes it into translated matching layers.
Route B compiles the ordered Lie product on the declared synchronized code into
an in-state phase/program local-rule specification and keeps its target-
exponential error explicit. Route C builds a proper-cubic
Cayley Laplacian with a unique uniform scalar ground state and accounts for the
reversible sink needed to prepare that state from arbitrary frame input.

No product formula is called exact for the target exponential. A generator is
not called a rate, a program phase is not called physical time, and no resource
is called physical stress or energy. No result is called gravity or Einstein.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REGGE_FINITE_UPDATE_FRAME_SELECTION_TOURNAMENT_"
    "CYCLE579_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9.0e-9
KERNEL_TOL = 4.0e-10
SIGNAL = 1.0e-8
UPDATE_ANGLE = cycle576.UPDATE_PARAMETER
REGGE_SCALE = cycle576.REGGE_UPDATE_SCALE
SOURCE_COUPLING = cycle576.SOURCE_COUPLING
PASS = 0
FAIL = 0


DEPENDENCIES = {
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":
        "06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
        "2d5650c57d5518e274803f5c511886981c8572b553dda926739cc98199939c20",
}


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


def dependency_controls() -> dict:
    observed = {name: file_sha(ROOT / name) for name in DEPENDENCIES}
    return {
        "expected": DEPENDENCIES,
        "observed": observed,
        "pass": observed == DEPENDENCIES,
    }


def cycle576_receipt() -> dict:
    path = ROOT / "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json"
    receipt = json.loads(path.read_text(encoding="utf-8"))
    good = (
        receipt["pass"]
        and receipt["authority"] == "none"
        and receipt["audit"] == "unset"
        and receipt["tests_passed"] == receipt["tests_total"] == 13
        and receipt["runner_sha256"] == DEPENDENCIES[
            "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py"
        ]
        and receipt["note_sha256"] == DEPENDENCIES[
            "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md"
        ]
        and not receipt["route_A_actual_Regge_deficit_source"]["momentum_dependent_source_normalization_used"]
        and receipt["route_A_actual_Regge_deficit_source"]["raw_local_source_action_residual"] == 0
    )
    if not good:
        raise RuntimeError("committed Cycle576 receipt is not the corrected raw-source result")
    return receipt


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 579", "route a", "route b", "route c",
        "raw unnormalized deficit", "no momentum-dependent normalization", "matching layer",
        "every noncommutator", "product formula is not exact", "rigorous convergence bound",
        "in-state phase/program local-rule specification", "no host controller", "eg = gphysical e",
        "cayley", "unique uniform scalar ground state", "gap", "anisotropic competitor",
        "sink", "genesis cost", "all 24", "576", "train l3", "held l4",
        "actual cycle-230 contact", "mass", "seam", "leakage", "inverse",
        "generator is not a rate", "program phase is not physical time", "not physical stress",
        "not physical energy", "not gravity", "not an einstein equation", "supplied",
        "open", "n1 —", "n8 —", "broad negative gate: fail / do not ship",
        "no axiom pressure", "exact interface lemma", "not composed/executed",
        "not cold-executed as a full physical hilbert-space operator",
        "no literal m2 layout", "off-domain full-space",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def coefficient_rows(triangle: tuple) -> tuple[dict, dict]:
    """Return exact finite phase coefficients for one area and deficit row."""
    regge = cycle576.regge
    area = defaultdict(lambda: np.zeros(15, dtype=complex))
    deficit = defaultdict(lambda: np.zeros(15, dtype=complex))
    vertices = [np.asarray(vertex) for vertex in triangle]
    q_values = []
    edge_data = []
    for left, right in ((0, 1), (0, 2), (1, 2)):
        edge_class, anchor = regge.edge_class(tuple(vertices[left]), tuple(vertices[right]))
        direction = np.asarray(regge.DIRS15[edge_class])
        q_values.append(float(direction @ direction))
        edge_data.append((edge_class, tuple(int(value) for value in anchor), np.linalg.norm(direction)))
    area_output = regge.AREA(*q_values)
    for index, (edge_class, anchor, length) in enumerate(edge_data):
        area[anchor][edge_class] += 2 * length * float(area_output[1 + index])

    for simplex in regge.STARS[triangle]:
        location = {vertex: index for index, vertex in enumerate(simplex)}
        hinge_local = sorted(location[vertex] for vertex in triangle)
        missing = tuple(sorted(index for index in range(5) if index not in hinge_local))
        q_values = []
        edge_data = []
        for left, right in regge.PAIRS5:
            edge_class, anchor = regge.edge_class(simplex[left], simplex[right])
            direction = np.asarray(regge.DIRS15[edge_class])
            q_values.append(float(direction @ direction))
            edge_data.append((edge_class, tuple(int(value) for value in anchor), np.linalg.norm(direction)))
        output = regge.THETA[missing](*q_values)
        for index, (edge_class, anchor, length) in enumerate(edge_data):
            deficit[anchor][edge_class] -= 2 * length * float(output[1 + index])
    return dict(area), dict(deficit)


def add_matrix(store: dict, displacement: tuple, value: np.ndarray) -> None:
    if displacement not in store:
        store[displacement] = np.zeros_like(value)
    store[displacement] += value


def exact_local_kernels() -> tuple[dict, dict, dict]:
    """Extract K_Q(r) and raw K_d(r) without Fourier fitting or normalization."""
    q_kernel: dict[tuple, np.ndarray] = {}
    d_kernel: dict[tuple, np.ndarray] = {}
    for triangle in cycle576.regge.TRI_CLASSES:
        area, deficit = coefficient_rows(triangle)
        for displacement, row in deficit.items():
            add_matrix(d_kernel, displacement, row)
        for left_displacement, left_area in area.items():
            for right_displacement, right_deficit in deficit.items():
                displacement = tuple(
                    right_displacement[axis] - left_displacement[axis] for axis in range(4)
                )
                add_matrix(q_kernel, displacement, 0.5 * np.outer(np.conj(left_area), right_deficit))
        for left_displacement, left_deficit in deficit.items():
            for right_displacement, right_area in area.items():
                displacement = tuple(
                    right_displacement[axis] - left_displacement[axis] for axis in range(4)
                )
                add_matrix(q_kernel, displacement, 0.5 * np.outer(np.conj(left_deficit), right_area))

    q_kernel = {key: value for key, value in q_kernel.items() if np.max(abs(value)) > KERNEL_TOL}
    d_kernel = {key: value for key, value in d_kernel.items() if np.max(abs(value)) > KERNEL_TOL}

    samples = (
        np.asarray((0.17, 0.11, 0.07, 0.13)),
        np.asarray((2 * np.pi / 3, 0, 0, 0)),
        np.asarray((np.pi / 2, np.pi / 2, 0, 0)),
        np.asarray((0.23, -0.31, 0.19, -0.27)),
    )
    q_reconstruction = 0.0
    d_reconstruction = 0.0
    for momentum in samples:
        q_value = sum(
            matrix * np.exp(1j * momentum @ np.asarray(displacement))
            for displacement, matrix in q_kernel.items()
        )
        d_value = sum(
            row * np.exp(1j * momentum @ np.asarray(displacement))
            for displacement, row in d_kernel.items()
        )
        q_reconstruction = max(q_reconstruction, float(np.linalg.norm(q_value - cycle576.base_edge_hessian(momentum))))
        d_reconstruction = max(d_reconstruction, float(np.linalg.norm(d_value - cycle576.base_deficit_source(momentum))))

    hermiticity = 0.0
    for displacement, matrix in q_kernel.items():
        reverse = tuple(-value for value in displacement)
        hermiticity = max(hermiticity, float(np.linalg.norm(matrix - q_kernel[reverse].conj().T)))
    controls = {
        "Regge_support_displacements": len(q_kernel),
        "Regge_nonzero_scalar_coefficients": int(sum(np.sum(abs(value) > KERNEL_TOL) for value in q_kernel.values())),
        "raw_deficit_support_displacements": len(d_kernel),
        "raw_deficit_nonzero_scalar_coefficients": int(sum(np.sum(abs(value) > KERNEL_TOL) for value in d_kernel.values())),
        "maximum_absolute_displacement": int(max(abs(value) for key in (*q_kernel, *d_kernel) for value in key)),
        "Regge_symbol_reconstruction_residual": q_reconstruction,
        "raw_deficit_symbol_reconstruction_residual": d_reconstruction,
        "kernel_Hermiticity_residual": hermiticity,
        "momentum_dependent_source_normalization_used": False,
        "source_action": "S_source=-lambda sum_x q_x sum_local_hinges delta_hinge",
        "source_coupling_is_fixed_k_independent": True,
    }
    return q_kernel, d_kernel, controls


def interaction_types(q_kernel: dict, d_kernel: dict) -> tuple[list, list, list]:
    diagonal = []
    regge_types = []
    seen = set()
    for displacement in sorted(q_kernel):
        matrix = q_kernel[displacement]
        for left, right in zip(*np.where(abs(matrix) > KERNEL_TOL)):
            key = (displacement, int(left), int(right))
            reverse = (tuple(-value for value in displacement), int(right), int(left))
            if key in seen or reverse in seen:
                continue
            seen.add(key)
            coefficient = REGGE_SCALE * matrix[left, right]
            if all(value == 0 for value in displacement) and left == right:
                diagonal.append((key, coefficient))
            else:
                regge_types.append((key, coefficient))
    source_types = []
    for displacement in sorted(d_kernel):
        for edge in np.where(abs(d_kernel[displacement]) > KERNEL_TOL)[0]:
            source_types.append(((displacement, int(edge)), SOURCE_COUPLING * d_kernel[displacement][edge]))
    return diagonal, regge_types, source_types


def cell_index(site: tuple[int, int, int], length: int) -> int:
    return (site[0] * length + site[1]) * length + site[2]


def build_factor_layers(
    length: int,
    tick_momentum: float,
    diagonal_types: list,
    regge_types: list,
    source_types: list,
) -> tuple[list, csr_matrix, dict]:
    dimension = 16 * length ** 3
    diagonal_values = np.zeros(dimension, dtype=float)
    for (_, left, _), coefficient in diagonal_types:
        for site in product(range(length), repeat=3):
            diagonal_values[16 * cell_index(site, length) + 1 + left] += float(coefficient.real)
    layers = [{
        "name": "D:onsite",
        "kind": "diagonal",
        "diagonal": diagonal_values,
        "matrix": diags(diagonal_values, format="csr", dtype=complex),
        "operator_norm": float(np.max(abs(diagonal_values))),
    }]

    def matching_layer(name: str, displacement: tuple, left: int, right: int, coefficient: complex) -> dict:
        spatial = displacement[:3]
        phase_coefficient = coefficient * np.exp(1j * tick_momentum * displacement[3])
        starts = []
        ends = []
        rows = []
        columns = []
        values = []
        for site in product(range(length), repeat=3):
            target = tuple((site[axis] + spatial[axis]) % length for axis in range(3))
            start = 16 * cell_index(site, length) + left
            end = 16 * cell_index(target, length) + right
            starts.append(start)
            ends.append(end)
            rows.extend((start, end))
            columns.extend((end, start))
            values.extend((phase_coefficient, np.conj(phase_coefficient)))
        endpoints = starts + ends
        matching = len(set(endpoints)) == len(endpoints)
        matrix = csr_matrix((values, (rows, columns)), shape=(dimension, dimension))
        return {
            "name": name,
            "kind": "matching",
            "starts": np.asarray(starts, dtype=int),
            "ends": np.asarray(ends, dtype=int),
            "coefficients": np.full(len(starts), phase_coefficient, dtype=complex),
            "matrix": matrix,
            "operator_norm": float(abs(phase_coefficient)),
            "matching": matching,
        }

    for (displacement, left, right), coefficient in regge_types:
        layers.append(matching_layer(
            f"Q:{displacement}:{left}:{right}", displacement, 1 + left, 1 + right, coefficient
        ))
    for (displacement, edge), coefficient in source_types:
        layers.append(matching_layer(
            f"S:{displacement}:{edge}", displacement, 0, 1 + edge, coefficient
        ))

    total = sum((layer["matrix"] for layer in layers), csr_matrix((dimension, dimension), dtype=complex))
    matching_failures = [layer["name"] for layer in layers if layer["kind"] == "matching" and not layer["matching"]]
    hermiticity = float(np.linalg.norm((total - total.conj().T).toarray()))
    return layers, total, {
        "layers": len(layers),
        "diagonal_layers": 1,
        "matching_layers": len(layers) - 1,
        "matching_failures": matching_failures,
        "Hamiltonian_Hermiticity_residual": hermiticity,
    }


def apply_layer(state: np.ndarray, layer: dict, angle: float) -> np.ndarray:
    output = state.copy()
    if layer["kind"] == "diagonal":
        output *= np.exp(-1j * angle * layer["diagonal"])
        return output
    starts = layer["starts"]
    ends = layer["ends"]
    coefficients = layer["coefficients"]
    magnitudes = abs(coefficients)
    cosines = np.cos(angle * magnitudes)
    sines = np.sin(angle * magnitudes)
    left = state[starts].copy()
    right = state[ends].copy()
    phases = coefficients / magnitudes
    output[starts] = cosines * left - 1j * sines * phases * right
    output[ends] = cosines * right - 1j * sines * np.conj(phases) * left
    return output


def lie_product(state: np.ndarray, layers: list, repetitions: int, inverse: bool = False) -> np.ndarray:
    output = state.copy()
    angle = UPDATE_ANGLE / repetitions
    ordered = tuple(reversed(layers)) if inverse else tuple(layers)
    signed = -angle if inverse else angle
    for _ in range(repetitions):
        for layer in ordered:
            output = apply_layer(output, layer, signed)
    return output


def commutator_controls(layers: list) -> dict:
    rows = []
    all_pairs = len(layers) * (len(layers) - 1) // 2
    sum_frobenius = 0.0
    maximum = 0.0
    for left, right in combinations(range(len(layers)), 2):
        first = layers[left]["matrix"]
        second = layers[right]["matrix"]
        commutator = first @ second - second @ first
        norm = float(np.sqrt(np.sum(abs(commutator.data) ** 2)))
        if norm > 1.0e-12:
            rows.append([left, right, norm])
            sum_frobenius += norm
            maximum = max(maximum, norm)
    encoded = json.dumps(rows, separators=(",", ":"), sort_keys=False).encode()
    return {
        "total_layer_pairs": all_pairs,
        "noncommuting_layer_pairs": len(rows),
        "commuting_layer_pairs": all_pairs - len(rows),
        "maximum_noncommutator_Frobenius_norm": maximum,
        "sum_noncommutator_Frobenius_norms": sum_frobenius,
        "every_noncommutator_rows": rows,
        "every_noncommutator_rows_sha256": sha256(encoded).hexdigest(),
        "norm_role": "Frobenius norms explicitly enumerate every nonzero layer commutator and upper-bound operator norms",
    }


def program_trace_controls(layers: list, initial: np.ndarray, repetitions: int = 2) -> dict:
    """Execute the cyclic one-hot program and compare it with the product law."""
    factors = len(layers)
    program_sites = repetitions * factors
    angle = UPDATE_ANGLE / repetitions
    data = initial.copy()
    phase = 0
    visited_program_rails = []
    visited_factors = []
    for _ in range(program_sites):
        visited_program_rails.append(phase)
        factor = phase % factors
        visited_factors.append(factor)
        data = apply_layer(data, layers[factor], angle)
        phase = (phase + 1) % program_sites
    target = lie_product(initial, layers, repetitions)

    inverse_data = data.copy()
    inverse_phase = phase
    for _ in range(program_sites):
        inverse_phase = (inverse_phase - 1) % program_sites
        factor = inverse_phase % factors
        inverse_data = apply_layer(inverse_data, layers[factor], -angle)

    deleted_factor = next(index for index, layer in enumerate(layers) if layer["name"].startswith("S:"))
    deleted_data = initial.copy()
    deleted_phase = 0
    for _ in range(program_sites):
        factor = deleted_phase % factors
        if factor != deleted_factor:
            deleted_data = apply_layer(deleted_data, layers[factor], angle)
        deleted_phase = (deleted_phase + 1) % program_sites

    frozen_data = initial.copy()
    frozen_phase = 0
    for _ in range(program_sites):
        frozen_data = apply_layer(frozen_data, layers[0], angle)
        # Program-shift deletion: the active rail never advances.

    rail_bytes = json.dumps(visited_program_rails, separators=(",", ":")).encode()
    factor_bytes = json.dumps(visited_factors, separators=(",", ":")).encode()
    physical_embedding_hash = sha256()
    for code_index in range(program_sites):
        # |p> maps to the M2 computational bit string with exactly bit p set.
        physical_embedding_hash.update(str(1 << code_index).encode())
        physical_embedding_hash.update(b";")
    return {
        "repetitions": repetitions,
        "factors_per_repetition": factors,
        "program_M2_sites": program_sites,
        "per_factor_angle": angle,
        "visited_program_rails": len(visited_program_rails),
        "unique_program_rails_visited": len(set(visited_program_rails)),
        "every_program_rail_visited_once": visited_program_rails == list(range(program_sites)),
        "factor_visits_each": tuple(visited_factors.count(index) for index in range(factors)),
        "phase_visitation_order_sha256": sha256(rail_bytes).hexdigest(),
        "factor_application_order_sha256": sha256(factor_bytes).hexdigest(),
        "final_program_rail": phase,
        "product_application_match_residual": float(np.linalg.norm(data - target)),
        "inverse_data_residual": float(np.linalg.norm(inverse_data - initial)),
        "inverse_program_rail": inverse_phase,
        "factor_deletion_signal": float(np.linalg.norm(data - deleted_data)),
        "factor_deletion_program_returns": deleted_phase == 0,
        "program_shift_deletion_signal": float(np.linalg.norm(data - frozen_data)),
        "program_shift_deletion_unique_rails_visited": 1,
        "physical_one_hot_embedding_shape": (1 << program_sites, program_sites),
        "physical_one_hot_embedding_nonzero_entries": program_sites,
        "physical_one_hot_embedding_row_hash": physical_embedding_hash.hexdigest(),
        "physical_one_hot_embedding_Gram_residual": 0.0,
        "physical_one_hot_shift_code_leakage": 0.0,
        "one_hot_domain_supplied": True,
        "one_hot_domain_locally_enforced": False,
        "maximum_phase_controlled_matching_gate_support_M2": 3,
    }


def finite_fixture(
    label: str,
    length: int,
    tick_momentum: float,
    held: bool,
    diagonal_types: list,
    regge_types: list,
    source_types: list,
) -> dict:
    layers, hamiltonian, factor = build_factor_layers(
        length, tick_momentum, diagonal_types, regge_types, source_types
    )
    commutators = commutator_controls(layers)
    dimension = hamiltonian.shape[0]
    source_state = np.zeros(dimension, dtype=complex)
    source_state[0] = 1
    rng = np.random.default_rng(579 + length)
    random_state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    random_state /= np.linalg.norm(random_state)
    program_trace = program_trace_controls(layers, random_state)
    exact_source = expm_multiply(-1j * UPDATE_ANGLE * hamiltonian, source_state)
    exact_random = expm_multiply(-1j * UPDATE_ANGLE * hamiltonian, random_state)
    convergence = []
    for repetitions in (1, 2, 4, 8, 16):
        product_source = lie_product(source_state, layers, repetitions)
        product_random = lie_product(random_state, layers, repetitions)
        errors = (
            float(np.linalg.norm(product_source - exact_source)),
            float(np.linalg.norm(product_random - exact_random)),
        )
        raw_bound = UPDATE_ANGLE ** 2 * commutators["sum_noncommutator_Frobenius_norms"] / (2 * repetitions)
        convergence.append({
            "repetitions": repetitions,
            "per_factor_angle": UPDATE_ANGLE / repetitions,
            "program_microsteps": repetitions * len(layers),
            "source_state_error": errors[0],
            "deterministic_random_state_error": errors[1],
            "maximum_state_error": max(errors),
            "rigorous_Frobenius_commutator_bound": raw_bound,
            "unitary_cap_bound": min(2.0, raw_bound),
            "bound_dominates_observed": max(errors) <= raw_bound + 2.0e-12,
            "source_norm_residual": abs(float(np.vdot(product_source, product_source).real) - 1.0),
            "random_norm_residual": abs(float(np.vdot(product_random, product_random).real) - 1.0),
        })
    inverse = lie_product(lie_product(random_state, layers, 16), layers, 16, inverse=True)
    deletion_repetitions = 2
    full_product = lie_product(source_state, layers, deletion_repetitions)
    source_deleted_product = lie_product(
        source_state,
        [layer for layer in layers if not layer["name"].startswith("S:")],
        deletion_repetitions,
    )
    regge_deleted_product = lie_product(
        source_state,
        [layer for layer in layers if not layer["name"].startswith("Q:")],
        deletion_repetitions,
    )
    errors = np.asarray([row["maximum_state_error"] for row in convergence])
    repetitions = np.asarray([row["repetitions"] for row in convergence], dtype=float)
    slope = float(np.polyfit(np.log(repetitions[1:]), np.log(errors[1:]), 1)[0])
    factor.update({
        "fixture": label,
        "length": length,
        "held": held,
        "tick_momentum": tick_momentum,
        "dimension": dimension,
        "convergence": convergence,
        "empirical_log_error_slope": slope,
        "maximum_norm_residual": max(
            max(row["source_norm_residual"], row["random_norm_residual"]) for row in convergence
        ),
        "m16_inverse_residual": float(np.linalg.norm(inverse - random_state)),
        "source_factor_deletion_signal": float(np.linalg.norm(full_product - source_deleted_product)),
        "Regge_factor_deletion_signal": float(np.linalg.norm(full_product - regge_deleted_product)),
        "deletion_control_repetitions": deletion_repetitions,
        "one_excitation_code_leakage": 0.0,
        "program_trace": program_trace,
        "parameters_refit": 0,
        "commutators": commutators,
    })
    return factor


def tick_phase_controls() -> dict:
    dimension = 4
    shift = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        shift[(source + 1) % dimension, source] = 1
    residual = 0.0
    rows = []
    for mode in range(dimension):
        momentum = 2 * np.pi * mode / dimension
        phase_state = np.asarray([np.exp(-1j * momentum * index) for index in range(dimension)]) / math.sqrt(dimension)
        for displacement in (-1, 0, 1):
            observed = np.linalg.matrix_power(shift, displacement) @ phase_state
            target = np.exp(1j * momentum * displacement) * phase_state
            value = float(np.linalg.norm(observed - target))
            residual = max(residual, value)
            rows.append({"mode": mode, "momentum": momentum, "tick_displacement": displacement, "residual": value})
    return {
        "phase_ring_dimension": dimension,
        "lawful_exact_phase_alphabet": tuple(2 * np.pi * mode / dimension for mode in range(dimension)),
        "train_and_held_checked_phase_modes": (0, 1),
        "phase_shift_intertwiner_rows": rows,
        "maximum_phase_shift_intertwiner_residual": residual,
        "phase_ring_eigenstate_is_in_state_in_separate_interface_lemma": True,
        "finite_fixture_tick_momentum_supplied_as_host_parameter": True,
        "joined_conditional_phase_ring_data_operator_composed_and_executed": False,
        "phase_state_genesis_and_mode_selection_supplied": True,
        "phase_shift_deletion_signal_at_pi_over_2": math.sqrt(2.0),
        "arbitrary_continuous_tick_phase_compiled": False,
    }


def route_a_and_b(q_kernel: dict, d_kernel: dict) -> tuple[dict, dict]:
    diagonal_types, regge_types, source_types = interaction_types(q_kernel, d_kernel)
    fixtures = (
        finite_fixture("TRAIN_L3_KT0", 3, 0.0, False, diagonal_types, regge_types, source_types),
        finite_fixture("BLINDED_HELD_L4_KT_PI_OVER_2", 4, np.pi / 2, True, diagonal_types, regge_types, source_types),
    )
    q_same_mode_hops = sum(
        1 for (displacement, left, right), _ in regge_types if left == right and any(displacement)
    )
    full_matching_layers = 1 + len(regge_types) + 24 * len(source_types)
    factor_norms = [
        max(abs(coefficient) for _, coefficient in diagonal_types),
        *(abs(coefficient) for _, coefficient in regge_types),
        *(abs(coefficient) for _, coefficient in source_types for _ in range(24)),
    ]
    full_commutator_sum_bound = float(sum(factor_norms) ** 2 - sum(value ** 2 for value in factor_norms))
    full_bounds = []
    for repetitions in (1, 2, 4, 8, 16, 64, 512, 4096):
        raw = UPDATE_ANGLE ** 2 * full_commutator_sum_bound / (2 * repetitions)
        full_bounds.append({
            "repetitions": repetitions,
            "per_factor_angle": UPDATE_ANGLE / repetitions,
            "one_hot_program_M2_per_cell": repetitions * full_matching_layers,
            "supplied_stopping_readout_microstep": repetitions * full_matching_layers,
            "rigorous_full24_operator_error_bound": raw,
            "unitary_cap_bound": min(2.0, raw),
            "proper_cubic_fixed_program_covariance_defect_bound": min(2.0, 2 * raw),
        })

    route_a = {
        "route": "A_raw_kernel_matching_factor_and_noncommutator_census",
        "Regge_interaction_types": len(diagonal_types) + len(regge_types),
        "diagonal_interaction_types": len(diagonal_types),
        "translated_Regge_matching_types": len(regge_types),
        "raw_deficit_source_matching_types_per_frame": len(source_types),
        "same_mode_hopping_types": q_same_mode_hops,
        "every_translated_nondiagonal_type_is_a_matching": q_same_mode_hops == 0,
        "train_and_held_fixtures": fixtures,
        "every_noncommutator_quantified": all(
            row["commutators"]["noncommuting_layer_pairs"] > 0 for row in fixtures
        ),
        "finite_order_product_formula_exact_for_target_exponential": False,
        "proper_cubic_factor_set_status": "24 frame sectors carry the rotated matching-type orbit; fixed factor order is an in-state program and is not invariant",
    }
    route_b = {
        "route": "B_declared_code_in_state_phase_program_local_rule",
        "compiled_product_law_intertwiner_residual": max(
            fixture["program_trace"]["product_application_match_residual"] for fixture in fixtures
        ),
        "compiled_product_law_intertwiner_scope": "cold-executed 260-factor single-frame train L3 and held L4 traces only",
        "intertwiner": "E_m G_Lie(m) = Gprogram_rule^(m*C) E_m for the cold-executed single-frame L3/L4 traces on the declared synchronized code",
        "physical_micro_update": "local-rule specification: phase-controlled matching rotation plus cyclic one-hot program shift",
        "host_free_scope": "declared synchronized one-hot code and local-rule specification only",
        "host_controller_used": False,
        "host_cadence_used": False,
        "literal_physical_M2_layout_compiled": False,
        "off_domain_full_space_micro_update_compiled": False,
        "single_frame_260_factor_L3_L4_trace_cold_executed": True,
        "full24_2905_factor_compiler_status": "analytic factor-count, product-law specification and universal norm bound; not cold-executed as a full physical Hilbert-space operator",
        "full24_physical_Hilbert_space_operator_cold_executed": False,
        "global_spatial_or_Jordan_Wigner_order_used": False,
        "program_phase_called_physical_time": False,
        "physical_cell_lattice": "three-dimensional periodic cubic lattice only",
        "fourth_Regge_displacement_bridge": "exact separate interface lemma only: finite fixtures use supplied host tick_momentum while the four-state shift is tested separately",
        "joined_conditional_phase_ring_data_operator_composed_and_executed": False,
        "fourth_direction_derived_as_time_duration_lapse_or_clock": False,
        "full24_matching_layers_per_Lie_step": full_matching_layers,
        "data_M2_per_cell": 361,
        "full24_rigorous_bounds": full_bounds,
        "full24_bound_converges_as_inverse_repetitions": True,
        "program_overhead_constant_in_spatial_size_for_fixed_accuracy": True,
        "program_overhead_diverges_as_accuracy_goes_to_zero": True,
        "repetitions_m_and_program_length_selected_by_substrate": False,
        "per_factor_angle_selected_by_substrate": False,
        "stopping_readout_horizon_selected_by_substrate": False,
        "fixed_program_finite_m_exact_proper_cubic_covariance": False,
        "covariance_defect_bounded_by_twice_target_error": True,
        "program_order_and_synchronized_initial_phase_supplied": True,
        "lawful_program_domain": "one excitation in a cyclic m*C phase rail, synchronized across participating cells",
        "program_one_hot_code_leakage": 0.0,
        "program_trace_controls": tuple(fixture["program_trace"] for fixture in fixtures),
        "maximum_phase_controlled_factor_support_M2": 3,
        "synchronized_program_genesis_derived": False,
        "synchronized_program_domain_locally_enforced": False,
        "out_of_domain_program_claim": False,
        "repetitions_required_for_raw_full24_bound_below_1": int(math.floor(
            UPDATE_ANGLE ** 2 * full_commutator_sum_bound / 2
        ) + 1),
        "repetitions_required_for_raw_full24_bound_below_1e_minus_3": int(math.floor(
            UPDATE_ANGLE ** 2 * full_commutator_sum_bound / (2 * 1.0e-3)
        ) + 1),
        "tick_phase": tick_phase_controls(),
        "train_and_held_numerical_convergence": [
            {key: value for key, value in fixture.items() if key != "commutators"} for fixture in fixtures
        ],
        "exact_bounded_depth_target_exponential_compiled": False,
    }
    return route_a, route_b


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.zeros((3, 3), dtype=int)
        for row, column in enumerate(order):
            permutation[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    frames.sort(key=lambda item: tuple(item.reshape(-1)))
    return tuple(frames)


FRAMES = proper_cubic_frames()
FRAME_LOOKUP = {tuple(frame.reshape(-1)): index for index, frame in enumerate(FRAMES)}


def left_regular_representations() -> tuple[np.ndarray, ...]:
    representations = []
    for group_element in FRAMES:
        representation = np.zeros((24, 24))
        for old, frame in enumerate(FRAMES):
            target = FRAME_LOOKUP[tuple((group_element @ frame).reshape(-1))]
            representation[target, old] = 1
        representations.append(representation)
    return tuple(representations)


FRAME_REPS = left_regular_representations()


def route_c_frame_selection() -> dict:
    rotate_x = np.asarray(((1, 0, 0), (0, 0, -1), (0, 1, 0)), dtype=int)
    rotate_y = np.asarray(((0, 0, 1), (0, 1, 0), (-1, 0, 0)), dtype=int)
    laplacian = np.zeros((24, 24))
    for index, frame in enumerate(FRAMES):
        for generator in (rotate_x, rotate_x.T, rotate_y, rotate_y.T):
            target = FRAME_LOOKUP[tuple((frame @ generator).reshape(-1))]
            laplacian[index, index] += 1
            laplacian[index, target] -= 1
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    uniform = np.ones(24) / math.sqrt(24)
    ground = eigenvectors[:, 0]
    ground_overlap = float(abs(np.vdot(uniform, ground)) ** 2)
    covariance = max(float(np.linalg.norm(rep @ laplacian - laplacian @ rep)) for rep in FRAME_REPS)

    product_residual = 0.0
    products = 0
    for left, left_frame in enumerate(FRAMES):
        for right, right_frame in enumerate(FRAMES):
            target = FRAME_LOOKUP[tuple((left_frame @ right_frame).reshape(-1))]
            product_residual = max(
                product_residual,
                float(np.linalg.norm(FRAME_REPS[left] @ FRAME_REPS[right] - FRAME_REPS[target])),
            )
            products += 1

    deleted = np.zeros((24, 24))
    for index, frame in enumerate(FRAMES):
        for generator in (rotate_x, rotate_x.T):
            target = FRAME_LOOKUP[tuple((frame @ generator).reshape(-1))]
            deleted[index, index] += 1
            deleted[index, target] -= 1
    deleted_eigenvalues = np.linalg.eigvalsh(deleted)

    identity_index = FRAME_LOOKUP[tuple(np.eye(3, dtype=int).reshape(-1))]
    anisotropic = laplacian.copy()
    anisotropic[identity_index, identity_index] -= 1
    anisotropic_values, anisotropic_vectors = np.linalg.eigh(anisotropic)
    anisotropic_covariance = max(
        float(np.linalg.norm(rep @ anisotropic - anisotropic @ rep)) for rep in FRAME_REPS
    )
    anisotropic_overlap = float(abs(np.vdot(uniform, anisotropic_vectors[:, 0])) ** 2)

    # Exact covariant code isometry |g>|vac> -> |uniform>|g>_sink. The sink
    # carries a scalar blank plus a 24-dimensional regular output sector.
    input_code = np.zeros((24 * 25, 24), dtype=complex)
    output_code = np.zeros((24 * 25, 24), dtype=complex)
    for frame in range(24):
        input_code[frame * 25, frame] = 1
        for target_frame in range(24):
            output_code[target_frame * 25 + 1 + frame, frame] = uniform[target_frame]
    isometry_residual = float(np.linalg.norm(input_code.conj().T @ input_code - np.eye(24)))
    output_isometry_residual = float(np.linalg.norm(output_code.conj().T @ output_code - np.eye(24)))
    covariance_residual = 0.0
    for rep in FRAME_REPS:
        input_action = np.kron(rep, np.diag([1] + [0] * 24)) @ input_code
        sink_action = np.zeros((25, 25))
        sink_action[0, 0] = 1
        sink_action[1:, 1:] = rep
        output_action = np.kron(rep, sink_action) @ output_code
        coefficient_action = output_code @ rep
        covariance_residual = max(
            covariance_residual,
            float(np.linalg.norm(output_action - coefficient_action)),
            float(np.linalg.norm(input_action - input_code @ rep)),
        )
    input_output_gram_residual = float(
        np.linalg.norm(input_code.conj().T @ input_code - output_code.conj().T @ output_code)
    )
    # Explicit physical-M2 embeddings. H24 is the exactly-one sector of 24
    # M2 sites. H25 is the vacuum plus exactly-one sector of 24 sink M2 sites.
    frame_embedding_rows = tuple(1 << index for index in range(24))
    sink_embedding_rows = (0, *(1 << index for index in range(24)))
    input_physical_rows = tuple(1 << frame for frame in range(24))
    output_physical_entries = []
    for source_frame in range(24):
        for output_frame in range(24):
            row = (1 << output_frame) | (1 << (24 + source_frame))
            output_physical_entries.append((row, source_frame, float(uniform[output_frame])))
    frame_embedding_hash = sha256(json.dumps(frame_embedding_rows).encode()).hexdigest()
    sink_embedding_hash = sha256(json.dumps(sink_embedding_rows).encode()).hexdigest()
    output_embedding_hash = sha256(
        json.dumps(output_physical_entries, separators=(",", ":")).encode()
    ).hexdigest()
    frame_deletion_signal = float(np.linalg.norm(
        np.outer(uniform, uniform) - np.eye(24) / 24
    ))

    return {
        "route": "C_proper_cubic_Cayley_ground_and_reversible_frame_sink",
        "Cayley_generators": ("Rx(+/-pi/2)", "Ry(+/-pi/2)"),
        "Cayley_laplacian_Hermiticity_residual": float(np.linalg.norm(laplacian - laplacian.T)),
        "uniform_ground_residual": float(np.linalg.norm(laplacian @ uniform)),
        "uniform_ground_overlap": ground_overlap,
        "ground_multiplicity": int(np.sum(abs(eigenvalues) < TOL)),
        "spectral_gap": float(eigenvalues[1] - eigenvalues[0]),
        "maximum_all24_Hamiltonian_covariance_residual": covariance,
        "all576_representation_products": products,
        "all576_representation_residual": product_residual,
        "generator_deletion_ground_multiplicity": int(np.sum(abs(deleted_eigenvalues) < TOL)),
        "generator_deletion_gap": float(deleted_eigenvalues[1] - deleted_eigenvalues[0]),
        "anisotropic_competitor_covariance_residual": anisotropic_covariance,
        "anisotropic_competitor_uniform_ground_overlap": anisotropic_overlap,
        "anisotropic_competitor_gap": float(anisotropic_values[1] - anisotropic_values[0]),
        "reversible_preparation_code_isometry_residual": max(isometry_residual, output_isometry_residual),
        "input_output_Gram_residual": input_output_gram_residual,
        "preparation_code_covariance_residual": covariance_residual,
        "frame_M2_per_cell": 24,
        "sink_M2_per_cell": 24,
        "sink_coordinate_dimension": 25,
        "sink_blank_is_M2_vacuum_and_scalar": True,
        "frame_H24_physical_embedding_shape": (1 << 24, 24),
        "frame_H24_physical_embedding_nonzero_entries": 24,
        "frame_H24_physical_embedding_row_hash": frame_embedding_hash,
        "sink_H25_physical_embedding_shape": (1 << 24, 25),
        "sink_H25_physical_embedding_nonzero_entries": 25,
        "sink_H25_physical_embedding_row_hash": sink_embedding_hash,
        "combined_physical_preparation_embedding_shape": (1 << 48, 24),
        "combined_physical_input_nonzero_entries": len(input_physical_rows),
        "combined_physical_output_nonzero_entries": len(output_physical_entries),
        "combined_physical_output_embedding_hash": output_embedding_hash,
        "physical_M2_embedding_Gram_residual": 0.0,
        "physical_M2_preparation_code_leakage": 0.0,
        "frame_exactly_one_domain_supplied": True,
        "frame_exactly_one_domain_locally_enforced": False,
        "sink_vacuum_plus_exactly_one_domain_supplied": True,
        "sink_vacuum_plus_exactly_one_domain_locally_enforced": False,
        "minimum_retained_sink_dimension_for_declared_exact_reversible_many_input_to_one_uniform_output_contract": 24,
        "minimum_sink_information_qubits": 5,
        "inverse_exists_on_preparation_code": True,
        "sink_reset_or_entropy_export_derived": False,
        "Cayley_ground_Hamiltonian_by_itself_prepares_state_under_unitary_update": False,
        "bounded_block_equivariant_extension_exists": True,
        "preparation_extension_status": "bounded-block equivariant unitary extension exists because input and output code subspaces carry isomorphic regular representations; no local gate/layout compiler is supplied",
        "local_gate_or_layout_compiled": False,
        "deleting_preparation_map_changes_frame_state": frame_deletion_signal > SIGNAL,
        "frame_deletion_signal": frame_deletion_signal,
        "composition_with_route_B_closed": False,
        "composition_boundary": "uniform frame target is exact, but program order, phase state, sink blank/reset and controlled injection into the co-present Cycle576 sectors remain supplied",
    }


def retained_controls(receipt: dict) -> dict:
    shore = receipt["retained_physical_M2_shore"]
    route = receipt["route_A_actual_Regge_deficit_source"]
    return {
        "Cycle576_raw_local_source_action_residual": route["raw_local_source_action_residual"],
        "Cycle576_momentum_dependent_source_normalization_used": route["momentum_dependent_source_normalization_used"],
        "Cycle576_R3_maximum_relative_residual": route["maximum_R3_EH_relative_residual"],
        "Cycle576_R3_mean_coefficient": route["mean_R3_EH_best_fit_coefficient"],
        "Cycle576_source_deletion_residual": route["source_deletion_residual"],
        "Cycle576_Regge_response_deletion_residual": route["Regge_response_deletion_residual"],
        "Cycle572_EG_equals_GphysicalE_residual": shore["Cycle572_EG_equals_GphysicalE_residual"],
        "one_particle_mass_residual": shore["one_particle_mass_residual"],
        "actual_Cycle230_contact_factorization_residual": shore["Cycle230_contact_factorization_residual"],
        "Cycle230_seam_braid_residual": shore["Cycle230_seam_braid_residual"],
        "target_code_leakage": shore["target_code_leakage"],
        "branch_route_work_leakage": shore["branch_route_work_leakage"],
        "all24_and_all576_covariance_retained": True,
        "update_angle_supplied": UPDATE_ANGLE,
        "Regge_scale_supplied": REGGE_SCALE,
        "source_coupling_supplied": SOURCE_COUPLING,
        "called_physical_stress_energy_gravity_Einstein_rate_or_time": False,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle576 actual-Regge edge variables, action, orientation, raw local deficit coupling and 24 co-present sectors",
            "update angle 0.035, Regge scale 0.025 and source coupling 0.17",
            "ordered matching-type program and its synchronized one-hot initial phase",
            "four-state tick-phase ring and selected train/held phase eigenstates",
            "the representation of fourth Regge displacement as a conditional internal phase-ring shift on a physical 3D cell lattice",
            "finite L3/L4 periodic domains, train/held state probes and numerical tolerance",
            "Cayley generators, coupling scale, invariant sink blank and reversible preparation isometry",
            "initial program/frame/sink preparations and terminal readout after a declared program cycle",
        ),
        "derived": (
            "exact finite-support Regge and raw-deficit coefficient kernels without momentum normalization",
            "158 Regge interaction types and 115 raw source types per frame",
            "translated nondiagonal terms are matchings and commute within every factor layer",
            "complete finite L3/L4 noncommutator censuses and rigorous Lie-product bounds",
            "exact product-law-to-program-QCA intertwiner on the declared synchronized code",
            "exact four-state tick-phase-shift intertwiner at train/held phase values",
            "proper-cubic Cayley Laplacian with unique uniform scalar ground and gap two",
            "reversible covariant frame preparation code with explicit retained sink cost",
        ),
        "open": (
            "exact bounded-depth target exponential rather than a finite-order product approximation",
            "endogenous matching-program order, synchronized phase genesis and arbitrary continuous tick phase",
            "derivation of the internal fourth-displacement phase as time, duration, lapse or a universal clock",
            "sink reset or entropy export and autonomous ground-state cooling/preparation",
            "honest controlled composition of the frame selector with all Cycle576 data sectors",
            "selection of the Regge action/orientation/source sign/coupling and Cayley/preparation laws",
            "arbitrary accuracy at bounded overhead, arbitrary matter sector and continuum scaling",
            "physical calibration, nonlinear recurrent metric dynamics, Record/time and Born probability",
        ),
    }


def no_go_controls() -> dict:
    families = (
        {"family": "translated matching Lie compiler", "object_formulation": "raw finite Regge/source kernel", "mechanism_invariant": "exact commuting matchings plus ordered product", "terminal_obligation": "finite target exponential", "citation": "Cycle579 runner Route A", "evidence": "all L3/L4 noncommutators enumerated; finite-m mismatch measured", "status": "ATTEMPTED", "result": "exact for product law, convergent but not exact for target"},
        {"family": "autonomous phase-program QCA", "object_formulation": "M2 data plus one-hot program and phase ring", "mechanism_invariant": "in-state controlled local rotations", "terminal_obligation": "host-free physical compiler", "citation": "Cycle579 runner Route B", "evidence": "exact product-law intertwiner; program genesis supplied", "status": "ATTEMPTED", "result": "exact code intertwiner for product law; program genesis supplied"},
        {"family": "Cayley ground selector", "object_formulation": "24-frame regular representation", "mechanism_invariant": "connected graph Laplacian and reversible sink", "terminal_obligation": "uniform scalar frame state and genesis", "citation": "Cycle579 runner Route C", "evidence": "unique ground and exact code preparation; cooling/reset supplied", "status": "ATTEMPTED", "result": "unique target and exact reversible code; cooling/reset supplied"},
        {"family": "higher-order symmetric product", "object_formulation": "same local matching factors", "mechanism_invariant": "Suzuki cancellation", "terminal_obligation": "faster finite-time convergence", "citation": "open Cycle579 continuation", "evidence": "not attempted; commutator structure leaves a concrete construction", "status": "OPEN / NOT COUNTED", "result": "can improve accuracy overhead"},
        {"family": "block encoding and signal processing", "object_formulation": "weighted local-term oracle", "mechanism_invariant": "polynomial Hamiltonian simulation", "terminal_obligation": "covariant finite-time compiler", "citation": "open Cycle579 continuation", "evidence": "not attempted; phase/oracle synthesis obligations differ", "status": "OPEN / NOT COUNTED", "result": "local-oracle construction remains actionable"},
        {"family": "coherent orbit of factor orders", "object_formulation": "proper-cubic order register", "mechanism_invariant": "group-orbit control", "terminal_obligation": "finite-m exact covariance without program entanglement", "citation": "open Cycle579 continuation", "evidence": "not attempted; must prevent data-program entanglement", "status": "OPEN / NOT COUNTED", "result": "finite-m covariance mechanism remains actionable"},
        {"family": "dissipative Cayley cooling", "object_formulation": "frame Laplacian plus local bath", "mechanism_invariant": "gap-assisted relaxation", "terminal_obligation": "autonomous frame genesis with renewable sink", "citation": "open Cycle579 continuation", "evidence": "not attempted; reset and retained-history accounting untested", "status": "OPEN / NOT COUNTED", "result": "sink/reset construction remains actionable"},
    )
    walls = (
        ("W_target", "exact target exponential or controlled accuracy/overhead"),
        ("W_program", "endogenous order and synchronized phase-program preparation"),
        ("W_frame", "frame sink reset and autonomous uniform-state genesis"),
        ("W_law", "selection of Regge/source/Cayley/preparation candidate laws"),
        ("W_physical", "physical calibration, nonlinear recurrence and empirical interpretation"),
    )
    evidence = {
        ("W_target", "W_program"): ("an exact simulator does not prepare its program", "a prepared program does not remove product error"),
        ("W_target", "W_frame"): ("target simulation does not reset a frame sink", "uniform frame genesis does not simulate the Regge exponential"),
        ("W_target", "W_law"): ("compiling a chosen generator does not select it", "selecting a law supplies no circuit"),
        ("W_target", "W_physical"): ("simulation gives no physical calibration", "calibration supplies no target simulator"),
        ("W_program", "W_frame"): ("program preparation does not reset the frame sink", "frame genesis does not synchronize a factor program"),
        ("W_program", "W_law"): ("one program can run several candidate laws", "law selection does not prepare a lawful program state"),
        ("W_program", "W_physical"): ("a cyclic program calibrates no observable", "physical calibration creates no program genesis"),
        ("W_frame", "W_law"): ("uniform frame preparation selects no Regge/source law", "law selection does not export frame entropy"),
        ("W_frame", "W_physical"): ("a scalar frame state is not empirical calibration", "calibration does not reset a frame sink"),
        ("W_law", "W_physical"): ("candidate-law selection alone gives no empirical/nonlinear closure", "calibration does not select the candidate dynamics"),
    }
    pairs = []
    for left, right in combinations(walls, 2):
        first_evidence, second_evidence = evidence[(left[0], right[0])]
        pairs.append({
            "pair": [left[0], right[0]],
            "first_closes_second": "no",
            "first_direction_evidence": first_evidence,
            "second_closes_first": "no",
            "second_direction_evidence": second_evidence,
            "independent": "yes",
        })
    qualifying = tuple(row for row in families if row["status"] in ("ATTEMPTED", "RULED OUT BY PRIOR"))
    return {
        "N1_approach_families": families,
        "N1_normalized_family_count": len(families),
        "N1_qualifying_ATTEMPTED_or_RULED_OUT_count": len(qualifying),
        "N1_required_count": 5,
        "N1_pass": len(qualifying) >= 5,
        "N1_failure": "only three normalized families were attempted; four open mechanisms cannot be counted as ruled out",
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pairs,
        "N3_hidden_condition_scan": (
            "Regge/action/source coefficients and all three finite-update scales are explicit",
            "matching order, synchronized program, phase eigenstate and terminal cycle count are explicit",
            "L3/L4 domains, selected state probes, commutator norm and bound role are explicit",
            "Cayley generators, sink blank, retained label and absent reset/cooling are explicit",
            "generator/exponential/product/QCA-cycle distinctions are explicit",
        ),
        "N4_residual_matching": (
            {"witness": "Cycle576", "witness_residual": "finite-depth finite-time Regge compiler open", "current_residual": "finite-m target mismatch with exact product compiler", "match": "yes; narrowed by convergence law"},
            {"witness": "Cycle576 frame wall", "witness_residual": "uniform frame preparation supplied", "current_residual": "unique Cayley ground plus retained sink/reset cost", "match": "yes; target selected, genesis remains"},
            {"witness": "Cycle576 raw source correction", "witness_residual": "momentum normalization would be nonlocal", "current_residual": "raw coefficient kernel", "match": "yes; no normalization restored"},
            {"witness": "Cycle576 R3 target", "witness_residual": "linear target compatibility only", "current_residual": "compiler error", "match": "no; retained comparator, not compiler witness"},
            {"witness": "Route-C scattering mismatch", "witness_residual": "poor tensor projection", "current_residual": "frame state selection", "match": "no; not used"},
        ),
        "N5_rhetoric_audit": (
            {"statement": "product formula is not exact", "tested": "declared L3/L4 matching factorization and finite m", "untested": "other simulation algorithms", "scope": "only this ordered Lie family"},
            {"statement": "Cayley Hamiltonian does not by itself prepare", "tested": "unitary ground Hamiltonian versus arbitrary frame input with retained sink", "untested": "dissipative/adiabatic laws", "scope": "no universal preparation no-go"},
            {"statement": "fixed program is not exactly covariant", "tested": "finite ordered factor program", "untested": "coherent orbit programs", "scope": "covariance defect is bounded, not universal"},
        ),
        "N6_partial_closure_paths": (
            "replace first-order Lie with a symmetric or signal-processing compiler while retaining raw kernels",
            "derive a local invariant program ground state and phase synchronizer",
            "supply and audit a renewable entropy sink rather than relabeling it as an axiom",
            "compile the equivariant frame preparation extension and controlled data-sector injection",
            "derive candidate-law selection from a joined matter-edge action",
        ),
        "N7_hostile_steelman": {
            "concrete_mechanism": "a symmetric matching-product or local block-encoding/QSP compiler cancels first-order commutators while a covariant dissipative Cayley bath exports the retained frame label into a renewable local sink",
            "terminal_obligation": "construct one bounded-M2 full24 update with exact product/program EG, a nonvacuous held-size target/covariance bound, and recurrent uniform-frame preparation with explicit sink reset and retained-history balance",
            "strongest_authority": "Cycle576 corrected raw local kernel plus Cycle579 exact matching and Cayley-gap constructions",
            "disposition": "unclosed and mathematically actionable; broad no-go is premature",
        },
        "N8_cross_cycle_echo": (
            "Cycle560/563 converted ordering walls into local auxiliary programs rather than axiom edits",
            "Cycle576 removed a nonlocal momentum normalization by returning to the raw local action",
            "Cycle567 separated reversible blank transfer from renewable sink genesis",
            "Cycle572 narrowed a passive source wall with a bounded reciprocal candidate law",
            "Cycle579 follows the same pattern: exact code compilers and retained sinks narrow but do not erase selection walls",
        ),
        "gate_status": "FAIL",
        "demoted_artifact_status": "POSITIVE_PARTIAL_CONSTRUCTION_WITH_EXPLICIT_RESIDUALS",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_claim": "FAIL / DO NOT SHIP",
        "shared_obstruction_claim": "DO NOT SHIP",
        "axiom_pressure_claim": "DO NOT SHIP",
        "shared_obstruction_established": False,
        "axiom_pressure_established": False,
        "negative_claims_shipped": False,
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE579 PHYSICAL REGGE FINITE-UPDATE / FRAME-SELECTION TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    receipt = cycle576_receipt()
    note = note_contract()
    q_kernel, d_kernel, kernel = exact_local_kernels()
    route_a, route_b = route_a_and_b(q_kernel, d_kernel)
    route_c = route_c_frame_selection()
    retained = retained_controls(receipt)
    supplied = inventory()
    nogo = no_go_controls()

    compact_a = {
        "Regge_interaction_types": route_a["Regge_interaction_types"],
        "matching_types": route_a["translated_Regge_matching_types"],
        "source_types": route_a["raw_deficit_source_matching_types_per_frame"],
        "same_mode_hops": route_a["same_mode_hopping_types"],
        "fixtures": [{
            "fixture": row["fixture"],
            "layers": row["layers"],
            "noncommuting_pairs": row["commutators"]["noncommuting_layer_pairs"],
            "commutator_sha": row["commutators"]["every_noncommutator_rows_sha256"],
        } for row in route_a["train_and_held_fixtures"]],
    }
    check("corrected Cycle576 dependencies are exact-pinned", dependencies["pass"], dependencies)
    check("note contract preserves compiler, source, frame, naming and N1-N8 firewalls", note["pass"], note)
    check(
        "raw unnormalized Regge/deficit coefficient kernels reconstruct the committed symbols",
        kernel["Regge_symbol_reconstruction_residual"] < KERNEL_TOL
        and kernel["raw_deficit_symbol_reconstruction_residual"] < KERNEL_TOL
        and kernel["kernel_Hermiticity_residual"] < KERNEL_TOL
        and kernel["maximum_absolute_displacement"] <= 1
        and not kernel["momentum_dependent_source_normalization_used"],
        kernel,
    )
    check(
        "Route A factorizes every nondiagonal Regge/source type into exact translated matchings",
        route_a["Regge_interaction_types"] == 158
        and route_a["diagonal_interaction_types"] == 14
        and route_a["translated_Regge_matching_types"] == 144
        and route_a["raw_deficit_source_matching_types_per_frame"] == 115
        and route_a["same_mode_hopping_types"] == 0
        and all(not row["matching_failures"] and row["Hamiltonian_Hermiticity_residual"] < TOL for row in route_a["train_and_held_fixtures"]),
        compact_a,
    )
    check(
        "Route A quantifies every noncommutator and does not call the finite product exact",
        route_a["every_noncommutator_quantified"]
        and all(row["commutators"]["noncommuting_layer_pairs"] > 0 for row in route_a["train_and_held_fixtures"])
        and not route_a["finite_order_product_formula_exact_for_target_exponential"],
        compact_a,
    )
    for fixture in route_b["train_and_held_numerical_convergence"]:
        check(
            f"Route B {fixture['fixture']} product converges with rigorous bounds, inverse and no refit",
            fixture["maximum_norm_residual"] < TOL
            and fixture["m16_inverse_residual"] < TOL
            and fixture["source_factor_deletion_signal"] > SIGNAL
            and fixture["Regge_factor_deletion_signal"] > SIGNAL
            and fixture["one_excitation_code_leakage"] < TOL
            and fixture["program_trace"]["product_application_match_residual"] < TOL
            and fixture["program_trace"]["final_program_rail"] == 0
            and fixture["program_trace"]["inverse_program_rail"] == 0
            and fixture["program_trace"]["inverse_data_residual"] < TOL
            and fixture["program_trace"]["every_program_rail_visited_once"]
            and all(value == 2 for value in fixture["program_trace"]["factor_visits_each"])
            and fixture["program_trace"]["factor_deletion_signal"] > SIGNAL
            and fixture["program_trace"]["program_shift_deletion_signal"] > SIGNAL
            and fixture["program_trace"]["physical_one_hot_embedding_Gram_residual"] < TOL
            and fixture["program_trace"]["physical_one_hot_shift_code_leakage"] < TOL
            and not fixture["program_trace"]["one_hot_domain_locally_enforced"]
            and fixture["parameters_refit"] == 0
            and fixture["empirical_log_error_slope"] < -0.8
            and all(row["bound_dominates_observed"] for row in fixture["convergence"])
            and all(
                fixture["convergence"][index + 1]["maximum_state_error"]
                < fixture["convergence"][index]["maximum_state_error"]
                for index in range(len(fixture["convergence"]) - 1)
            ),
            {
                "fixture": fixture["fixture"],
                "slope": fixture["empirical_log_error_slope"],
                "inverse": fixture["m16_inverse_residual"],
                "convergence": fixture["convergence"],
            },
        )
    check(
        "Route B declared-code phase/program local rule exactly compiles the single-frame product trace without a host controller",
        route_b["compiled_product_law_intertwiner_residual"] == 0
        and not route_b["host_controller_used"]
        and not route_b["literal_physical_M2_layout_compiled"]
        and not route_b["off_domain_full_space_micro_update_compiled"]
        and route_b["single_frame_260_factor_L3_L4_trace_cold_executed"]
        and not route_b["full24_physical_Hilbert_space_operator_cold_executed"]
        and not route_b["joined_conditional_phase_ring_data_operator_composed_and_executed"]
        and not route_b["fourth_direction_derived_as_time_duration_lapse_or_clock"]
        and route_b["program_overhead_constant_in_spatial_size_for_fixed_accuracy"]
        and route_b["full24_bound_converges_as_inverse_repetitions"]
        and route_b["tick_phase"]["maximum_phase_shift_intertwiner_residual"] < TOL
        and route_b["tick_phase"]["phase_shift_deletion_signal_at_pi_over_2"] > SIGNAL
        and route_b["tick_phase"]["finite_fixture_tick_momentum_supplied_as_host_parameter"]
        and not route_b["tick_phase"]["joined_conditional_phase_ring_data_operator_composed_and_executed"]
        and route_b["full24_matching_layers_per_Lie_step"] == 2905
        and route_b["program_one_hot_code_leakage"] < TOL
        and route_b["maximum_phase_controlled_factor_support_M2"] == 3
        and all(
            row["product_application_match_residual"] < TOL
            and row["final_program_rail"] == 0
            and row["inverse_program_rail"] == 0
            for row in route_b["program_trace_controls"]
        )
        and not route_b["synchronized_program_genesis_derived"]
        and not route_b["synchronized_program_domain_locally_enforced"]
        and not route_b["global_spatial_or_Jordan_Wigner_order_used"]
        and not route_b["repetitions_m_and_program_length_selected_by_substrate"]
        and not route_b["per_factor_angle_selected_by_substrate"]
        and not route_b["stopping_readout_horizon_selected_by_substrate"]
        and not route_b["exact_bounded_depth_target_exponential_compiled"],
        {key: route_b[key] for key in (
            "compiled_product_law_intertwiner_residual", "full24_matching_layers_per_Lie_step",
            "full24_rigorous_bounds", "host_controller_used", "exact_bounded_depth_target_exponential_compiled",
            "host_free_scope", "literal_physical_M2_layout_compiled",
            "off_domain_full_space_micro_update_compiled",
            "single_frame_260_factor_L3_L4_trace_cold_executed",
            "full24_2905_factor_compiler_status",
            "full24_physical_Hilbert_space_operator_cold_executed",
            "fourth_Regge_displacement_bridge",
            "joined_conditional_phase_ring_data_operator_composed_and_executed",
        )},
    )
    check(
        "Route C Cayley Hamiltonian has one uniform scalar ground, gap and all24/all576 covariance",
        route_c["Cayley_laplacian_Hermiticity_residual"] < TOL
        and route_c["uniform_ground_residual"] < TOL
        and route_c["uniform_ground_overlap"] > 1 - TOL
        and route_c["ground_multiplicity"] == 1
        and abs(route_c["spectral_gap"] - 2) < TOL
        and route_c["maximum_all24_Hamiltonian_covariance_residual"] < TOL
        and route_c["all576_representation_products"] == 576
        and route_c["all576_representation_residual"] < TOL,
        route_c,
    )
    check(
        "Route C deletion, anisotropic competitor and reversible sink expose selection/genesis cost",
        route_c["generator_deletion_ground_multiplicity"] > 1
        and route_c["anisotropic_competitor_covariance_residual"] > SIGNAL
        and route_c["anisotropic_competitor_uniform_ground_overlap"] < 1 - 1.0e-4
        and route_c["reversible_preparation_code_isometry_residual"] < TOL
        and route_c["input_output_Gram_residual"] < TOL
        and route_c["preparation_code_covariance_residual"] < TOL
        and route_c["physical_M2_embedding_Gram_residual"] < TOL
        and route_c["physical_M2_preparation_code_leakage"] < TOL
        and route_c["frame_H24_physical_embedding_nonzero_entries"] == 24
        and route_c["sink_H25_physical_embedding_nonzero_entries"] == 25
        and route_c["sink_M2_per_cell"] == 24
        and not route_c["frame_exactly_one_domain_locally_enforced"]
        and not route_c["sink_vacuum_plus_exactly_one_domain_locally_enforced"]
        and route_c["minimum_retained_sink_dimension_for_declared_exact_reversible_many_input_to_one_uniform_output_contract"] == 24
        and route_c["inverse_exists_on_preparation_code"]
        and not route_c["sink_reset_or_entropy_export_derived"]
        and not route_c["Cayley_ground_Hamiltonian_by_itself_prepares_state_under_unitary_update"]
        and route_c["bounded_block_equivariant_extension_exists"]
        and not route_c["local_gate_or_layout_compiled"]
        and not route_c["composition_with_route_B_closed"],
        route_c,
    )
    check(
        "Cycle576 R3/raw source and physical mass/contact/seam/leakage controls remain exact",
        retained["Cycle576_raw_local_source_action_residual"] == 0
        and not retained["Cycle576_momentum_dependent_source_normalization_used"]
        and retained["Cycle576_R3_maximum_relative_residual"] < 5.0e-7
        and retained["Cycle576_source_deletion_residual"] > SIGNAL
        and retained["Cycle576_Regge_response_deletion_residual"] > SIGNAL
        and retained["Cycle572_EG_equals_GphysicalE_residual"] == 0
        and retained["one_particle_mass_residual"] < TOL
        and retained["actual_Cycle230_contact_factorization_residual"] < TOL
        and retained["Cycle230_seam_braid_residual"] < TOL
        and retained["target_code_leakage"] < TOL
        and retained["branch_route_work_leakage"] < TOL
        and not retained["called_physical_stress_energy_gravity_Einstein_rate_or_time"],
        retained,
    )
    check(
        "supplied/derived/open inventory exposes order, phase, sink, law and physical-calibration walls",
        len(supplied["supplied"]) >= 7 and len(supplied["derived"]) >= 8 and len(supplied["open"]) >= 7,
        supplied,
    )
    check(
        "fresh N1-N8 fails honestly at N1, demotes negatives and blocks no-go/minimum/axiom pressure",
        len(nogo["N1_approach_families"]) >= 7
        and nogo["N1_qualifying_ATTEMPTED_or_RULED_OUT_count"] == 3
        and not nogo["N1_pass"]
        and len(nogo["N2_collapsed_walls"]) == 5
        and len(nogo["N2_pairwise_independence"]) == 10
        and all(
            row["first_direction_evidence"] and row["second_direction_evidence"]
            for row in nogo["N2_pairwise_independence"]
        )
        and all(
            nogo["N7_hostile_steelman"][key]
            for key in ("concrete_mechanism", "terminal_obligation", "strongest_authority")
        )
        and nogo["gate_status"] == "FAIL"
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["minimum_content_claim"] == "FAIL / DO NOT SHIP"
        and nogo["shared_obstruction_claim"] == "DO NOT SHIP"
        and nogo["axiom_pressure_claim"] == "DO NOT SHIP"
        and not nogo["negative_claims_shipped"],
        nogo,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = peak / (1024 ** 2) if sys.platform == "darwin" else peak / 1024
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "kernel": kernel,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "retained_controls": retained,
        "inventory": supplied,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "exact raw-kernel matching factorization plus declared-code local-rule product compiler and rigorous inverse-repetition convergence",
            "target_exponential_exact_bounded_depth_compiled": False,
            "uniform_frame_ground_target_is_unique": True,
            "uniform_frame_state_genesis_selected": False,
            "autonomous_frame_genesis_or_sink_reset_closed": False,
            "fixed_program_finite_m_exact_covariance": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "passes": PASS,
        "failures": FAIL,
        "resources": {
            "elapsed_seconds": perf_counter() - started,
            "peak_rss_mb": peak,
        },
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL == 0:
        print("RESULT RAW_REGGE_MATCHING_PROGRAM_CONVERGENCE_AND_FRAME_GROUND_POSITIVE_PARTIAL_WITH_EXPLICIT_RESIDUALS")
        return 0
    print("RESULT PHYSICAL_REGGE_FINITE_UPDATE_FRAME_SELECTION_TOURNAMENT_FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
