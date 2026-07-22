#!/usr/bin/env python3
"""Cycle 604: rational Regge, reciprocal response, prediction bridge.

The update count is not physical time.  Conserved modular words are not
stress-energy.  Neither response field is called gravity.  Authority is none
and audit is unset.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np
from scipy.integrate import quad
from scipy.linalg import null_space
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.special import ive


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22 as cycle579


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RATIONAL_REGGE_RECIPROCAL_RESPONSE_PREDICTION_BRIDGE_"
    "CYCLE604_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_rational_regge_reciprocal_response_prediction_bridge_"
    "cycle604_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-8
START = perf_counter()
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_recurrent_source_bounded_regge_retarded_response_tournament_cycle601_2026_07_22.py":
        "bcd09e478743552938eebcb484c610bd8cb2e39c61ae076b0f96c0a0f8c71fbd",
    "docs/work_history/repo/review_feedback/PHYSICAL_RECURRENT_SOURCE_BOUNDED_REGGE_RETARDED_RESPONSE_TOURNAMENT_CYCLE601_NOTE_2026-07-22.md":
        "138880bea4b6de50cd97b8b6b76b767bfe5210d3d15fb11ffb596677bb4f2bed",
    "outputs/physical_recurrent_source_bounded_regge_retarded_response_tournament_cycle601_cold_2026_07_22.txt":
        "b58555baef2869fb782b393472dd0f1dda2c5efdee2ef4fadd7a3f6a8c9ac237",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "scripts/physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22.py":
        "e607e8a0d46fbb70e7be35d1897acebebdb8ad900a4ab69159e572f3fbc5c7ab",
    "scripts/physical_regge_static_scalar_prediction_bridge_tournament_cycle585_2026_07_22.py":
        "70d98e5493df503f5fe353f31caf50f967b7e35c7471f01ba529de3a6a4a7c99",
    "outputs/physical_regge_static_scalar_prediction_bridge_tournament_cycle585_cold_2026_07_22.txt":
        "ebebc5bf0eaa26fe957c9295d997da613071f1e5c98fbeb5b66311baa125d703",
    "scripts/physical_constrained_matter_source_static_join_tournament_cycle588_2026_07_22.py":
        "d3658aacb76988ae7daf100f8ed3503e69927afa90a88d2062a0f23919f8ac4c",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONSTRAINED_MATTER_SOURCE_STATIC_JOIN_TOURNAMENT_CYCLE588_NOTE_2026-07-22.md":
        "4818ebbdbbd862859fe9963f3eaa2ecc42534d8a0186c456ff1b1f73194cda59",
    "outputs/physical_constrained_matter_source_static_join_tournament_cycle588_cold_2026_07_22.txt":
        "c10ca982c9755af00c70c14b1e825834bdf3f9024737f12a024ef5fbd1324993",
    "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md":
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    "scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py":
        "853abe5470efd15b154d6cb348d49795a6fa84e77a62f0b21a79105892b1d415",
    "outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json":
        "f104399af621ded1b50e180e6fcce5f254008715b72191c6199fe4d583a8a806",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def dependency_shore() -> dict:
    observed = {name: digest(name) for name in PINS}
    receipt570 = json.loads((ROOT / "outputs/physical_joint_clock_accumulator_contraction_bridge_cycle570_receipt_2026_07_22.json").read_text())
    good = observed == PINS and receipt570["pass"] and receipt570["authority"] == "none" and receipt570["audit"] == "unset"
    check("Cycles 601/576/579/585/588/451/570 are byte-pinned and passing where receipted", good,
          {"hashes_match": observed == PINS, "Cycle570_pass": receipt570["pass"]})
    return {"expected": PINS, "observed": observed, "Cycle570_receipt_pass": receipt570["pass"]}


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 604", "padé", "continued-fraction",
        "julia dilation", "fir", "paraunitary", "retained garbage", "co-designed",
        "even torus", "all 24", "all 576", "nearest-neighbor", "exact inverse",
        "leakage", "deletion", "kick", "drift", "conserved word", "continuity",
        "future-source", "not stress-energy", "not gravity", "cesaro", "5/(32pi)",
        "3:4", "5:4", "update count is not time", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note exposes exact/approximate scope and full N1-N8 discipline", not missing, missing)


# ---------------------------------------------------------------------------
# Route A: rational transfer, exact finite paraunitary termination, and a
# metric-rail Regge product whose expanded image is invariant by construction.


HORIZON = 8


def exact_line(z: np.ndarray | float) -> np.ndarray | complex:
    return np.exp(0.5j * z) * np.sinc(np.asarray(z) / (2 * math.pi))


def pade_transfer(z: np.ndarray | float) -> np.ndarray | complex:
    w = np.exp(1j * z)
    return 2 * (1 + 2 * w) / (5 + w)


def fir_coefficients() -> np.ndarray:
    coefficients = [0.4]
    coefficients.extend(0.72 * (-0.2) ** (order - 1) for order in range(1, HORIZON))
    coefficients.append(1 - sum(coefficients))  # exact DC termination
    return np.asarray(coefficients, dtype=float)


def polynomial_value(coefficients: np.ndarray, z: np.ndarray | float) -> np.ndarray | complex:
    w = np.exp(1j * z)
    return sum(value * w ** order for order, value in enumerate(coefficients))


def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2)
    return vectors @ np.diag(np.sqrt(np.maximum(values, 0))) @ vectors.conj().T


def rational_julia_dilation() -> dict:
    transition = np.asarray(((-1 / 5, 3 * math.sqrt(2) / 5),
                             (3 * math.sqrt(2) / 5, 2 / 5)), dtype=complex)
    left_defect = positive_sqrt(np.eye(2) - transition @ transition.conj().T)
    right_defect = positive_sqrt(np.eye(2) - transition.conj().T @ transition)
    julia = np.block([[transition, left_defect], [right_defect, -transition.conj().T]])
    samples = np.linspace(-3 * math.pi, 3 * math.pi, 1201)
    transfer_residual = 0.0
    for z in samples:
        w = np.exp(1j * z)
        state = w * transition[1, 0] / (1 - w * transition[0, 0])
        observed = transition[1, 1] + transition[0, 1] * state
        transfer_residual = max(transfer_residual, float(abs(observed - pade_transfer(z))))
    return {
        "state_space_contraction": transition,
        "Julia_unitary": julia,
        "singular_values": np.linalg.svd(transition, compute_uv=False),
        "Julia_unitarity_residual": float(np.linalg.norm(julia.conj().T @ julia - np.eye(4))),
        "state_transfer_residual": transfer_residual,
    }


def spectral_complement(body: np.ndarray) -> np.ndarray:
    degree = len(body) - 1
    laurent = []
    for lag in range(-degree, degree + 1):
        autocorrelation = sum(
            body[index + lag] * body[index]
            for index in range(max(0, -lag), min(degree + 1, degree + 1 - lag))
        )
        laurent.append((1.0 if lag == 0 else 0.0) - autocorrelation)
    roots = np.roots(np.asarray(laurent)[::-1])
    selected = sorted(roots, key=abs)[:degree]
    unscaled = np.poly(selected)[::-1]
    samples = np.exp(1j * np.linspace(-math.pi, math.pi, 20001))
    p = sum(body[n] * samples ** n for n in range(degree + 1))
    q = sum(unscaled[n] * samples ** n for n in range(degree + 1))
    mask = abs(q) > 1e-7
    ratios = (1 - abs(p[mask]) ** 2) / abs(q[mask]) ** 2
    scaled = np.asarray(unscaled * math.sqrt(float(np.median(ratios))))
    if float(np.max(abs(scaled.imag))) > 1e-7:
        raise AssertionError("spectral complement failed to become real")
    return scaled.real.astype(float)


def fejer_riesz_coefficient_residual(body: np.ndarray, garbage: np.ndarray) -> float:
    """Coefficient identity 1-|P|^2=|Q|^2, hence a full-circle proof."""
    degree = len(body) - 1
    residual = 0.0
    for lag in range(-degree, degree + 1):
        body_auto = sum(body[index + lag] * body[index]
                        for index in range(max(0, -lag), min(degree + 1, degree + 1 - lag)))
        garbage_auto = sum(garbage[index + lag] * garbage[index]
                           for index in range(max(0, -lag), min(degree + 1, degree + 1 - lag)))
        target = (1.0 if lag == 0 else 0.0) - body_auto
        residual = max(residual, float(abs(target - garbage_auto)))
    return residual


def paraunitary_polynomial(body: np.ndarray, garbage: np.ndarray) -> np.ndarray:
    degree = len(body) - 1
    return np.asarray([
        ((body[n], -garbage[::-1][n]), (garbage[n], body[::-1][n]))
        for n in range(degree + 1)
    ], dtype=complex)


def factor_paraunitary(polynomial: np.ndarray) -> tuple[np.ndarray, list[np.ndarray], dict]:
    work = [coefficient.copy() for coefficient in polynomial]
    vectors = []
    wall = 0.0
    while len(work) > 1:
        lead = work[-1]
        _, singular, right = np.linalg.svd(lead)
        vector = right.conj().T[:, 0]
        projector = np.outer(vector, vector.conj())
        complement = np.eye(2) - projector
        wall = max(wall, float(np.linalg.norm(work[0] @ projector)),
                   float(np.linalg.norm(lead @ complement)), float(singular[-1]))
        work = [work[n] @ complement + work[n + 1] @ projector for n in range(len(work) - 1)]
        vectors.append(vector)
    base = work[0]
    reconstruction = [base]
    for vector in reversed(vectors):
        projector = np.outer(vector, vector.conj())
        complement = np.eye(2) - projector
        updated = [np.zeros((2, 2), dtype=complex) for _ in range(len(reconstruction) + 1)]
        for order, coefficient in enumerate(reconstruction):
            updated[order] += coefficient @ complement
            updated[order + 1] += coefficient @ projector
        reconstruction = updated
    return base, vectors, {
        "degree_reduction_wall_residual": wall,
        "base_unitarity_residual": float(np.linalg.norm(base.conj().T @ base - np.eye(2))),
        "coefficient_reconstruction_residual": float(np.linalg.norm(np.asarray(reconstruction) - polynomial)),
    }


def polar_code(matrix: np.ndarray) -> np.ndarray:
    gram = matrix.conj().T @ matrix
    values, vectors = np.linalg.eigh(gram)
    return matrix @ vectors @ np.diag(1 / np.sqrt(values)) @ vectors.conj().T


def unitary_completion(code: np.ndarray) -> np.ndarray:
    return np.column_stack((code, null_space(code.conj().T)))


def givens_count_and_residual(unitary: np.ndarray) -> tuple[int, float]:
    work = unitary.copy(); gates = []
    for column in range(len(unitary)):
        for row in range(len(unitary) - 1, column, -1):
            a, b = work[row - 1, column], work[row, column]
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            if radius < 1e-14:
                continue
            gate = np.asarray(((np.conj(a) / radius, np.conj(b) / radius),
                               (-b / radius, a / radius)), dtype=complex)
            work[[row - 1, row], :] = gate @ work[[row - 1, row], :]
            gates.append((row - 1, row, gate))
    reconstruction = work.copy()
    for left, right, gate in reversed(gates):
        reconstruction[[left, right], :] = gate.conj().T @ reconstruction[[left, right], :]
    return len(gates), float(np.linalg.norm(reconstruction - unitary))


def metric_kernel() -> tuple[dict, dict]:
    q_kernel, _, controls = cycle579.exact_local_kernels()
    code = polar_code(cycle576.regge.metric_map(np.zeros(4)))
    spatial = {}
    for displacement4, matrix in q_kernel.items():
        displacement = tuple(int(value) for value in displacement4[:3])
        transformed = cycle576.REGGE_UPDATE_SCALE * code.conj().T @ matrix @ code
        spatial[displacement] = spatial.get(displacement, np.zeros((10, 10), dtype=complex)) + transformed
    spatial = {key: value for key, value in spatial.items() if np.max(abs(value)) > 1e-11}
    hermiticity = max(float(np.linalg.norm(value - spatial[tuple(-x for x in key)].conj().T))
                      for key, value in spatial.items())
    return spatial, {**controls, "metric_kernel_displacements": len(spatial),
                     "metric_kernel_Hermiticity_residual": hermiticity}


def metric_factor_layers(kernel: dict) -> list[dict]:
    onsite = np.real(np.diag(kernel.get((0, 0, 0), np.zeros((10, 10)))))
    layers = [{"kind": "diagonal", "values": onsite}]
    seen = set()
    for displacement in sorted(kernel):
        matrix = kernel[displacement]
        for left, right in zip(*np.where(abs(matrix) > 1e-11)):
            key = (displacement, int(left), int(right))
            reverse = (tuple(-x for x in displacement), int(right), int(left))
            if key in seen or reverse in seen:
                continue
            seen.add(key)
            if displacement == (0, 0, 0) and left == right:
                continue
            base = {"kind": "pair", "displacement": displacement, "left": int(left),
                    "right": int(right), "coefficient": complex(matrix[left, right])}
            if left == right:
                axis = next(index for index, value in enumerate(displacement) if value)
                layers.extend(({**base, "parity_axis": axis, "parity": parity} for parity in (0, 1)))
            else:
                layers.append({**base, "parity_axis": None, "parity": None})
    return layers


def apply_metric_layer(state: np.ndarray, layer: dict, signed_angle: float) -> np.ndarray:
    output = state.copy()
    if layer["kind"] == "diagonal":
        output *= np.exp(-1j * signed_angle * layer["values"])
        return output
    displacement = layer["displacement"]
    left_role, right_role = layer["left"], layer["right"]
    coefficient = layer["coefficient"]
    magnitude = abs(coefficient)
    cosine, sine = math.cos(signed_angle * magnitude), math.sin(signed_angle * magnitude)
    phase = coefficient / magnitude
    if left_role != right_role:
        left = state[..., left_role].copy()
        right = np.roll(state[..., right_role], tuple(-x for x in displacement), axis=(0, 1, 2)).copy()
        output[..., left_role] = cosine * left - 1j * sine * phase * right
        right_new = cosine * right - 1j * sine * np.conj(phase) * left
        output[..., right_role] = np.roll(right_new, displacement, axis=(0, 1, 2))
        return output
    length = state.shape[0]
    axis, parity = layer["parity_axis"], layer["parity"]
    for site in product(range(length), repeat=3):
        if site[axis] % 2 != parity:
            continue
        target = tuple((site[index] + displacement[index]) % length for index in range(3))
        left, right = state[site + (left_role,)], state[target + (left_role,)]
        output[site + (left_role,)] = cosine * left - 1j * sine * phase * right
        output[target + (left_role,)] = cosine * right - 1j * sine * np.conj(phase) * left
    return output


def metric_product(state: np.ndarray, layers: list[dict], inverse: bool = False) -> np.ndarray:
    output = state.copy()
    ordered = tuple(reversed(layers)) if inverse else tuple(layers)
    angle = -cycle579.UPDATE_ANGLE if inverse else cycle579.UPDATE_ANGLE
    for layer in ordered:
        output = apply_metric_layer(output, layer, angle)
    return output


def metric_sparse_matrix(length: int, kernel: dict):
    rows = []; columns = []; values = []
    def flat(site): return (site[0] * length + site[1]) * length + site[2]
    for site in product(range(length), repeat=3):
        for displacement, matrix in kernel.items():
            target = tuple((site[axis] + displacement[axis]) % length for axis in range(3))
            for left, right in zip(*np.where(abs(matrix) > 1e-11)):
                rows.append(10 * flat(site) + int(left))
                columns.append(10 * flat(target) + int(right))
                values.append(matrix[left, right])
    return coo_matrix((values, (rows, columns)), shape=(10 * length ** 3,) * 2).tocsr()


def apply_filter(fields: np.ndarray, polynomial: np.ndarray, directions: tuple, inverse: bool = False) -> np.ndarray:
    """fields shape L,L,L,15,2; exact FIR paraunitary or its adjoint."""
    output = np.zeros_like(fields)
    for edge, direction4 in enumerate(directions):
        direction = tuple(int(value) for value in direction4[:3])
        if not any(direction):
            output[..., edge, :] = fields[..., edge, :]
            continue
        for order, coefficient in enumerate(polynomial):
            if inverse:
                shifted = np.roll(fields[..., edge, :], tuple(-order * x for x in direction), axis=(0, 1, 2))
                output[..., edge, :] += np.einsum("ab,xyzb->xyza", coefficient.conj().T, shifted)
            else:
                shifted = np.roll(fields[..., edge, :], tuple(order * x for x in direction), axis=(0, 1, 2))
                output[..., edge, :] += np.einsum("ab,xyzb->xyza", coefficient, shifted)
    return output


def encode_metric(metric: np.ndarray, code: np.ndarray, polynomial: np.ndarray) -> np.ndarray:
    body = np.einsum("ab,xyzb->xyza", code, metric)
    fields = np.zeros(metric.shape[:3] + (15, 2), dtype=complex)
    fields[..., 0] = body
    return apply_filter(fields, polynomial, tuple(cycle576.regge.DIRS15))


def physical_product(fields: np.ndarray, layers: list[dict], completion: np.ndarray,
                     polynomial: np.ndarray, inverse: bool = False) -> np.ndarray:
    decoded = apply_filter(fields, polynomial, tuple(cycle576.regge.DIRS15), inverse=True)
    base = np.einsum("ab,xyzb->xyza", completion.conj().T, decoded[..., 0])
    if inverse:
        base[..., :10] = metric_product(base[..., :10], layers, inverse=True)
    else:
        base[..., :10] = metric_product(base[..., :10], layers)
    decoded[..., 0] = np.einsum("ab,xyzb->xyza", completion, base)
    return apply_filter(decoded, polynomial, tuple(cycle576.regge.DIRS15))


def route_a() -> dict:
    julia = rational_julia_dilation()
    body = fir_coefficients()
    garbage = spectral_complement(body)
    fejer_riesz_residual = fejer_riesz_coefficient_residual(body, garbage)
    polynomial = paraunitary_polynomial(body, garbage)
    base_section, delay_vectors, factor_controls = factor_paraunitary(polynomial)
    samples = np.linspace(-3 * math.pi, 3 * math.pi, 24001)
    unitarity = 0.0
    sampled_defects = []
    for z in samples:
        value = sum(polynomial[n] * np.exp(1j * n * z) for n in range(HORIZON + 1))
        unitarity = max(unitarity, float(np.linalg.norm(value.conj().T @ value - np.eye(2))))
        sampled_defects.append(1.0 - abs(polynomial_value(body, z)) ** 2)
    rational_error = float(np.max(abs(polynomial_value(body, samples) - pade_transfer(samples))))
    full_error = float(np.max(abs(polynomial_value(body, samples) - exact_line(samples))))

    kernel, kernel_controls = metric_kernel()
    layers = metric_factor_layers(kernel)
    code = polar_code(cycle576.regge.metric_map(np.zeros(4)))
    completion = unitary_completion(code)
    givens_count, givens_residual = givens_count_and_residual(completion)

    fixtures = (("TRAIN_L4", 4, False), ("HELD_L6", 6, True),
                ("HELD_L8", 8, True), ("OUT_FAMILY_L10", 10, True))
    rows = []
    low_errors = []
    max_inverse = max_intertwining = max_leakage = max_product_error = 0.0
    min_deletion = math.inf
    rng = np.random.default_rng(604)
    for label, length, held in fixtures:
        z = 2 * math.pi / length
        low = float(abs(polynomial_value(body, z) - exact_line(z)))
        low_errors.append(low)
        state = rng.normal(size=(length, length, length, 10)) + 1j * rng.normal(size=(length, length, length, 10))
        state /= np.linalg.norm(state)
        encoded = encode_metric(state, code, polynomial)
        physical = physical_product(encoded, layers, completion, polynomial)
        logical = metric_product(state, layers)
        target = encode_metric(logical, code, polynomial)
        intertwining = float(np.linalg.norm(physical - target))
        restored = physical_product(physical, layers, completion, polynomial, inverse=True)
        inverse = float(np.linalg.norm(restored - encoded))
        decoded = apply_filter(physical, polynomial, tuple(cycle576.regge.DIRS15), inverse=True)
        metric_back = np.einsum("ab,xyzb->xyza", code.conj().T, decoded[..., 0])
        projected = encode_metric(metric_back, code, polynomial)
        leakage = float(np.linalg.norm(physical - projected))
        deleted_layers = layers[:1] + layers[2:]
        deletion = float(np.linalg.norm(metric_product(state, layers) - metric_product(state, deleted_layers)))

        target_matrix = metric_sparse_matrix(length, kernel)
        exact = expm_multiply(-1j * cycle579.UPDATE_ANGLE * target_matrix, state.reshape(-1)).reshape(state.shape)
        product_error = float(np.linalg.norm(logical - exact))
        rows.append({
            "fixture": label, "length": length, "held": held,
            "low_mode_z": z, "low_mode_FIR_to_exact_line_error": low,
            "FIR_to_rational_error": float(abs(polynomial_value(body, z) - pade_transfer(z))),
            "expanded_code_intertwining_residual": intertwining,
            "expanded_code_leakage": leakage, "exact_inverse_residual": inverse,
            "delete_one_metric_factor_signal": deletion,
            "ordered_product_to_target_exponential_error": product_error,
        })
        max_inverse = max(max_inverse, inverse); max_intertwining = max(max_intertwining, intertwining)
        max_leakage = max(max_leakage, leakage); max_product_error = max(max_product_error, product_error)
        min_deletion = min(min_deletion, deletion)
    slopes = [math.log(low_errors[i] / low_errors[i + 1]) / math.log(fixtures[i + 1][1] / fixtures[i][1])
              for i in range(len(low_errors) - 1)]

    # Delete one exact delay factor from the paraunitary factorization.
    deleted_vectors = delay_vectors.copy(); deleted_vectors.pop(len(deleted_vectors) // 2)
    reconstruction = [base_section]
    for vector in reversed(deleted_vectors):
        projector = np.outer(vector, vector.conj()); complement = np.eye(2) - projector
        updated = [np.zeros((2, 2), complex) for _ in range(len(reconstruction) + 1)]
        for order, coefficient in enumerate(reconstruction):
            updated[order] += coefficient @ complement; updated[order + 1] += coefficient @ projector
        reconstruction = updated
    delay_deletion = max(float(np.linalg.norm(
        sum(polynomial[n] * np.exp(1j * n * z) for n in range(HORIZON + 1))
        - sum(reconstruction[n] * np.exp(1j * n * z) for n in range(len(reconstruction)))
    )) for z in np.linspace(-math.pi, math.pi, 501))

    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    missing = sum(tuple((left @ right).reshape(-1)) not in lookup for left in frames for right in frames)
    covariance = 0
    for left in frames:
        for sector in frames:
            for displacement in kernel:
                vector = np.asarray(displacement)
                covariance = max(covariance, int(np.max(abs(left @ (sector @ vector) - (left @ sector) @ vector))))

    max_direction_steps = max(sum(abs(int(x)) for x in direction[:3]) for direction in cycle576.regge.DIRS15)
    filter_depth = 1 + HORIZON * (2 + max_direction_steps)
    metric_radius_depth = 1 + 7 * (len(layers) - 1)
    full_depth = 2 * (filter_depth + givens_count + 1) + metric_radius_depth
    rail_coordinates = [(rail % 9, (rail // 9) % 9, rail // 81) for rail in range(24 * 15 * 2)]
    output = {
        "object": "Cycle576 Regge kernel in ten metric rails, conjugated by a lossless finite rational-transfer termination",
        "disposition": "CONSTRUCTIVE_EXACT_FIR_IMAGE_COMPILER; PADE_AND_SINC_ONLY_APPROXIMATE",
        "rational_exact_theorem": "R(w)=2(1+2w)/(5+w) is exactly the transfer of the one-state contraction; its four-channel Julia dilation is unitary",
        "rational_physical_scope": "the stationary rational response needs an unbounded recurrence/fixed-point preparation and is not claimed as a finite-depth compiler",
        "physical_exact_theorem": "the degree-8 DC-corrected FIR P8 is exactly the first entry of the executed 2x2 paraunitary; all complement outputs are retained",
        "target_approximation_theorem": "P8-R is uniformly bounded on the tested unit circle, while R-f is O(z^3) only at low momentum; neither equality to the sinc factor nor uniform full-BZ accuracy is claimed",
        "Padé_state_contraction_singular_values": julia["singular_values"].tolist(),
        "Padé_Julia_unitarity_residual": julia["Julia_unitarity_residual"],
        "Padé_state_transfer_residual": julia["state_transfer_residual"],
        "FIR_degree": HORIZON, "FIR_body_coefficients": body.tolist(),
        "FIR_garbage_coefficients": garbage.tolist(),
        "FIR_paraunitarity_residual": unitarity,
        "Fejer_Riesz_full_circle_coefficient_identity_residual": fejer_riesz_residual,
        "full_circle_nonnegative_defect_theorem": "1-|P8(w)|^2=|Q8(w)|^2 coefficient-by-coefficient for every |w|=1; this is not inferred from the sampling grid",
        "minimum_sampled_unit_circle_defect": float(min(sampled_defects)),
        "maximum_sampled_unit_circle_defect": float(max(sampled_defects)),
        "maximum_negative_sampled_unit_circle_defect": float(max(0.0, -min(sampled_defects))),
        "FIR_factorization": factor_controls,
        "FIR_delay_sections": len(delay_vectors),
        "FIR_delay_projector_vectors_real_imag": [
            [[float(value.real), float(value.imag)] for value in vector] for vector in delay_vectors
        ],
        "FIR_base_section_real_imag": [
            [[float(value.real), float(value.imag)] for value in row] for row in base_section
        ],
        "maximum_FIR_to_Padé_full_zone_error": rational_error,
        "maximum_FIR_to_exact_line_full_zone_error": full_error,
        "rows": rows, "observed_low_mode_error_slopes": slopes,
        "maximum_expanded_code_intertwining_residual": max_intertwining,
        "maximum_expanded_code_leakage": max_leakage,
        "maximum_exact_inverse_residual": max_inverse,
        "minimum_metric_factor_deletion_signal": min_deletion,
        "delay_factor_deletion_signal": delay_deletion,
        "maximum_ordered_product_target_exponential_error": max_product_error,
        "metric_kernel_controls": kernel_controls,
        "metric_factor_layers": len(layers),
        "same_role_hopping_sublayers": sum(layer.get("parity_axis") is not None for layer in layers),
        "lawful_sizes": "even periodic tori; the supplied bipartite matching color is not extended to odd tori",
        "metric_completion_Givens": givens_count,
        "metric_completion_reconstruction_residual": givens_residual,
        "M2_data_rails_per_cell_all24": 24 * 15 * 2,
        "M2_block_shape": [9, 9, 9],
        "M2_unique_rail_coordinates": len(set(rail_coordinates)),
        "M2_rail_coordinate_rule": "rail=30*frame+2*edge+channel; coordinate=(rail mod 9, floor(rail/9) mod 9, floor(rail/81))",
        "M2_maximum_within_block_L1_distance": max(sum(coordinate) for coordinate in rail_coordinates),
        "local_gate_support_M2": 2,
        "filter_bounded_radius": HORIZON * math.sqrt(3),
        "filter_axial_QCA_layer_depth": filter_depth,
        "literal_closed_torus_NN_swap_depth_certified": False,
        "executed_operator_vs_gate_certificate": "apply_filter/physical_product execute the block-circulant polynomial operator; the reconstructed eight delay sections certify its local realization but are not replayed gate-by-gate by the numerical runner",
        "explicit_delay_section_schedule": "onsite parameterized two-M2 basis rotation; one selected-rail proper-cubic stream permutation (at most three axial permutation sublayers); inverse onsite rotation",
        "stream_layer_kind": "local QCA permutation layer, not claimed to be a finite circuit of closed-torus NN swaps",
        "parameterized_gate_matrices_frozen": True,
        "accepted_finite_gate_alphabet_lowering_executed": False,
        "metric_product_bounded_depth": len(layers),
        "metric_product_serial_NN_routing_upper_bound_certificate": metric_radius_depth,
        "full_prepare_product_unprepare_serial_routing_upper_bound_certificate": full_depth,
        "NN_routing_replayed_by_numerical_runner": False,
        "all24_frame_sectors": 24, "all576_products": 576,
        "all576_missing_products": int(missing), "frame_sector_displacement_residual": covariance,
        "retained_garbage": True, "host_fixed_point_service_used": False,
        "target_exponential_exact": False, "exact_sinc_compiler": False,
    }
    check("route A exact rational contraction and Julia dilation are valid but scoped from finite depth",
          max(julia["singular_values"]) < 1 + TOL and julia["Julia_unitarity_residual"] < TOL
          and julia["state_transfer_residual"] < TOL, output)
    check("route A FIR paraunitary and its eight local delay factors are exact",
          unitarity < TOL and fejer_riesz_residual < TOL
          and factor_controls["coefficient_reconstruction_residual"] < TOL
          and factor_controls["degree_reduction_wall_residual"] < TOL and delay_deletion > 1e-3, output)
    check("route A co-designed Regge product preserves the expanded image and inverts on train/held/out sizes",
          max_intertwining < TOL and max_leakage < TOL and max_inverse < TOL
          and min_deletion > 1e-6, rows)
    check("route A exposes low-k improvement, full-zone failure, product error, and all24/all576 scope",
          min(slopes) > 2.0 and full_error > 0.1 and max_product_error > 1e-7
          and missing == covariance == 0 and len(layers) > 1
          and len(set(rail_coordinates)) == 24 * 15 * 2, output)
    return output


# ---------------------------------------------------------------------------
# Route B: reciprocal modular kick-drift source/field candidate.


WORD_BITS = 31
MODULUS = 1 << WORD_BITS


def laplacian_integer(field: np.ndarray) -> np.ndarray:
    return 6 * field - sum(np.roll(field, shift, axis)
                           for axis in range(3) for shift in (-1, 1))


def modular(value: np.ndarray) -> np.ndarray:
    return np.asarray(value % MODULUS, dtype=np.int64)


def signed_word(value: np.ndarray) -> np.ndarray:
    return np.where(value >= MODULUS // 2, value - MODULUS, value).astype(np.int64)


def reciprocal_kick(state: tuple[np.ndarray, ...], sign: int,
                    delete_source_recoil: bool = False,
                    delete_field_response: bool = False) -> tuple[np.ndarray, ...]:
    source, source_momentum, field, field_momentum = state
    exchange = sign * (source - field)
    recoil = source_momentum - laplacian_integer(source)
    if not delete_source_recoil:
        recoil -= exchange
    response = field_momentum - laplacian_integer(field)
    if not delete_field_response:
        response += exchange
    return source.copy(), modular(recoil), field.copy(), modular(response)


def inverse_reciprocal_kick(state: tuple[np.ndarray, ...], sign: int) -> tuple[np.ndarray, ...]:
    source, recoil, field, response = state
    exchange = sign * (source - field)
    source_momentum = recoil + laplacian_integer(source) + exchange
    field_momentum = response + laplacian_integer(field) - exchange
    return source.copy(), modular(source_momentum), field.copy(), modular(field_momentum)


def drift(state: tuple[np.ndarray, ...]) -> tuple[np.ndarray, ...]:
    source, source_momentum, field, field_momentum = state
    return modular(source + source_momentum), source_momentum.copy(), modular(field + field_momentum), field_momentum.copy()


def inverse_drift(state: tuple[np.ndarray, ...]) -> tuple[np.ndarray, ...]:
    source, source_momentum, field, field_momentum = state
    return modular(source - source_momentum), source_momentum.copy(), modular(field - field_momentum), field_momentum.copy()


def reciprocal_step(state: tuple[np.ndarray, ...], sign: int, order: str,
                    delete_source_recoil: bool = False,
                    delete_field_response: bool = False) -> tuple[np.ndarray, ...]:
    if order == "KICK_THEN_DRIFT":
        return drift(reciprocal_kick(state, sign, delete_source_recoil, delete_field_response))
    if delete_source_recoil or delete_field_response:
        return reciprocal_kick(drift(state), sign, delete_source_recoil, delete_field_response)
    return reciprocal_kick(drift(state), sign)


def reciprocal_inverse(state: tuple[np.ndarray, ...], sign: int, order: str) -> tuple[np.ndarray, ...]:
    if order == "KICK_THEN_DRIFT":
        return inverse_reciprocal_kick(inverse_drift(state), sign)
    return inverse_drift(inverse_reciprocal_kick(state, sign))


def ledger(state: tuple[np.ndarray, ...]) -> int:
    return int((np.sum(state[1], dtype=np.int64) + np.sum(state[3], dtype=np.int64)) % MODULUS)


def rotate_scalar(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]; output = np.zeros_like(field)
    for site in product(range(length), repeat=3):
        centered = np.asarray([value if value <= length // 2 else value - length for value in site])
        target = tuple(int(value % length) for value in frame @ centered)
        output[target] = field[site]
    return output


def route_b() -> dict:
    rows = []
    max_inverse = max_ledger = max_continuity = max_covariance = 0
    min_order_signal = min_sign_signal = min_deletion = min_source_input_deletion = math.inf
    for label, length, steps, held in (("TRAIN_L3", 3, 4, False),
                                       ("HELD_L5", 5, 6, True),
                                       ("OUT_FAMILY_L7", 7, 8, True)):
        zero = np.zeros((length,) * 3, dtype=np.int64)
        source = zero.copy(); source[0, 0, 0] = 17
        source_momentum = zero.copy(); source_momentum[0, 0, 0] = 5
        initial = (source, source_momentum, zero.copy(), zero.copy())
        outputs = {}
        for order in ("KICK_THEN_DRIFT", "DRIFT_THEN_KICK"):
            for sign in (+1, -1):
                state = tuple(value.copy() for value in initial)
                initial_ledger = ledger(state)
                local_continuity = 0
                for _ in range(steps):
                    before = state
                    kicked = reciprocal_kick(before if order == "KICK_THEN_DRIFT" else drift(before), sign)
                    kick_input = before if order == "KICK_THEN_DRIFT" else drift(before)
                    delta = signed_word(modular(kicked[1] + kicked[3] - kick_input[1] - kick_input[3]))
                    continuity = delta + laplacian_integer(signed_word(kick_input[0]) + signed_word(kick_input[2]))
                    local_continuity = max(local_continuity, int(np.max(abs(continuity))))
                    state = reciprocal_step(before, sign, order)
                restored = state
                for _ in range(steps):
                    restored = reciprocal_inverse(restored, sign, order)
                inverse = max(int(np.max(abs(left.astype(np.int64) - right.astype(np.int64))))
                              for left, right in zip(restored, initial))
                ledger_residual = int((ledger(state) - initial_ledger) % MODULUS)
                outputs[(order, sign)] = state
                max_inverse = max(max_inverse, inverse)
                max_ledger = max(max_ledger, min(ledger_residual, MODULUS - ledger_residual))
                max_continuity = max(max_continuity, local_continuity)
        kick_plus = outputs[("KICK_THEN_DRIFT", +1)]
        drift_plus = outputs[("DRIFT_THEN_KICK", +1)]
        kick_minus = outputs[("KICK_THEN_DRIFT", -1)]
        order_signal = max(int(np.max(abs(signed_word(left) - signed_word(right))))
                           for left, right in zip(kick_plus, drift_plus))
        sign_signal = max(int(np.max(abs(signed_word(left) - signed_word(right))))
                          for left, right in zip(kick_plus, kick_minus))
        deleted_source = reciprocal_step(initial, +1, "KICK_THEN_DRIFT", delete_source_recoil=True)
        source_deletion_residual = min((ledger(deleted_source) - ledger(initial)) % MODULUS,
                                       (ledger(initial) - ledger(deleted_source)) % MODULUS)
        deleted_field = reciprocal_step(initial, +1, "KICK_THEN_DRIFT", delete_field_response=True)
        field_deletion_residual = min((ledger(deleted_field) - ledger(initial)) % MODULUS,
                                      (ledger(initial) - ledger(deleted_field)) % MODULUS)
        source_off = reciprocal_step((zero.copy(), zero.copy(), zero.copy(), zero.copy()), +1, "KICK_THEN_DRIFT")
        source_deleted_input = (zero.copy(), source_momentum.copy(), zero.copy(), zero.copy())
        source_deleted_output = reciprocal_step(source_deleted_input, +1, "KICK_THEN_DRIFT")
        source_input_deletion_signal = max(
            int(np.max(abs(signed_word(left) - signed_word(right))))
            for left, right in zip(reciprocal_step(initial, +1, "KICK_THEN_DRIFT"), source_deleted_output)
        )
        rows.append({
            "fixture": label, "length": length, "updates": steps, "held": held,
            "initial_conserved_word": ledger(initial),
            "maximum_inverse_integer_residual": inverse,
            "maximum_conserved_ledger_residual": max_ledger,
            "maximum_local_continuity_residual": local_continuity,
            "kick_vs_drift_order_signal": order_signal,
            "positive_vs_negative_coupling_signal": sign_signal,
            "delete_source_recoil_ledger_failure": int(source_deletion_residual),
            "delete_field_response_ledger_failure": int(field_deletion_residual),
            "delete_source_input_signal": source_input_deletion_signal,
            "source_off_maximum_word": max(int(np.max(abs(value))) for value in source_off),
            "field_origin_word_kick_first_positive": int(signed_word(kick_plus[2])[0, 0, 0]),
            "source_origin_word_kick_first_positive": int(signed_word(kick_plus[0])[0, 0, 0]),
        })
        min_order_signal = min(min_order_signal, order_signal)
        min_sign_signal = min(min_sign_signal, sign_signal)
        min_deletion = min(min_deletion, source_deletion_residual, field_deletion_residual)
        min_source_input_deletion = min(min_source_input_deletion, source_input_deletion_signal)

    length = 5
    rng = np.random.default_rng(6042)
    random_state = tuple(rng.integers(0, 31, size=(length,) * 3, dtype=np.int64) for _ in range(4))
    for frame in cycle576.FRAMES:
        left = tuple(rotate_scalar(value, frame) for value in reciprocal_step(random_state, +1, "KICK_THEN_DRIFT"))
        right = reciprocal_step(tuple(rotate_scalar(value, frame) for value in random_state), +1, "KICK_THEN_DRIFT")
        max_covariance = max(max_covariance, max(int(np.max(abs(a - b))) for a, b in zip(left, right)))
    wrap_state = tuple(np.zeros((3, 3, 3), dtype=np.int64) for _ in range(4))
    wrap_state[0][0, 0, 0] = MODULUS - 1
    wrap_state[1][0, 0, 0] = 5
    wrapped = drift(wrap_state)
    wrap_detected = int(wrapped[0][0, 0, 0]) == 4
    wrap_inverse = max(int(np.max(abs(a - b))) for a, b in zip(inverse_drift(wrapped), wrap_state))
    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): i for i, frame in enumerate(frames)}
    missing = sum(tuple((left @ right).reshape(-1)) not in lookup for left in frames for right in frames)
    output = {
        "object": "reciprocal source/field modular kick-drift candidate with paired momenta",
        "disposition": "CONSTRUCTIVE_EXACT_RECIPROCAL_LEDGER; PHYSICAL_IDENTIFICATION_AND_ORDER_OPEN",
        "update": "kick: p_s<-p_s-Lq-s(q-phi), p_f<-p_f-Lphi+s(q-phi); drift: q<-q+p_s, phi<-phi+p_f modulo 2^31",
        "rows": rows,
        "maximum_exact_inverse_integer_residual": max_inverse,
        "maximum_conserved_ledger_residual": max_ledger,
        "maximum_local_continuity_residual": max_continuity,
        "minimum_order_alternative_signal": min_order_signal,
        "minimum_sign_alternative_signal": min_sign_signal,
        "minimum_recoil_deletion_ledger_failure": int(min_deletion),
        "minimum_source_input_deletion_signal": int(min_source_input_deletion),
        "explicit_wrap_detected": bool(wrap_detected),
        "wrap_inverse_residual": wrap_inverse,
        "no_wrap_fixture_maximum_absolute_signed_word": max(
            abs(row["field_origin_word_kick_first_positive"]) for row in rows
        ),
        "maximum_all24_covariance_integer_residual": max_covariance,
        "all576_products": 576, "all576_missing_products": int(missing),
        "conserved_ledger": "sum_x(p_source+p_field) modulo 2^31",
        "conserved_word_is_stress_energy": False,
        "source_word_is_physical_matter_recoil": False,
        "response_is_gravity": False,
        "kick_first_selected": False, "drift_first_selected": False,
        "host_future_source_service_used": False,
        "field_and_source_M2_per_cell": 4 * WORD_BITS,
        "scratch_M2_upper_bound_per_cell": 4 * WORD_BITS,
        "local_gate_support_M2": 3,
        "NN_stencil_radius": 1,
        "ripple_depth_upper_bound_per_update": 64 * WORD_BITS,
        "global_sum_is_computed_by_host_during_update": False,
    }
    check("route B reciprocal kick-drift alternatives exactly conserve the modular ledger and local continuity",
          max_inverse == max_ledger == max_continuity == 0, rows)
    check("route B sign/order alternatives are distinct, reversible, source-off clean, and recoil deletion active",
          min_order_signal > 0 and min_sign_signal > 0 and min_deletion > 0
          and min_source_input_deletion > 0
          and wrap_detected and wrap_inverse == 0
          and all(row["source_off_maximum_word"] == 0 for row in rows), output)
    check("route B scalar law is all24/all576 covariant without a future-source read",
          max_covariance == missing == 0 and not output["host_future_source_service_used"], output)
    return output


# ---------------------------------------------------------------------------
# Route C: stable reversible Cesaro bridge to static Green and matched events.


CESARO_ALPHA = 1 / 12
CESARO_FIXTURES = (("TRAIN_L5_H192", 5, 192, False),
                   ("HELD_L7_H384", 7, 384, True),
                   ("OUT_FAMILY_L9_H768", 9, 768, True))


def laplacian_float(field: np.ndarray) -> np.ndarray:
    return 6 * field - sum(np.roll(field, shift, axis)
                           for axis in range(3) for shift in (-1, 1))


def finite_green(length: int) -> tuple[np.ndarray, np.ndarray]:
    source = np.zeros((length,) * 3); source[0, 0, 0] = 1; source -= 1 / length ** 3
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    denominator = np.zeros_like(source)
    for index in product(range(length), repeat=3):
        denominator[index] = 6 - 2 * sum(math.cos(frequencies[index[axis]]) for axis in range(3))
    transformed = np.zeros(source.shape, dtype=complex)
    mask = denominator > 1e-14
    transformed[mask] = np.fft.fftn(source)[mask] / denominator[mask]
    return np.fft.ifftn(transformed).real, source


def cesaro_response(length: int, horizon: int) -> tuple[np.ndarray, float]:
    exact, source = finite_green(length)
    previous = np.zeros_like(source); current = np.zeros_like(source); accumulator = np.zeros_like(source)
    for _ in range(horizon):
        following = 2 * current - previous - CESARO_ALPHA * laplacian_float(current) + CESARO_ALPHA * source
        previous, current = current, following
        accumulator += current
    return accumulator / horizon, float(np.linalg.norm(current))


def infinite_lattice_green(point: tuple[int, int, int]) -> float:
    return float(quad(lambda value: ive(abs(point[0]), 2 * value)
                      * ive(abs(point[1]), 2 * value)
                      * ive(abs(point[2]), 2 * value), 0, np.inf,
                      limit=500, epsabs=2e-13)[0])


def route_c() -> dict:
    rows = []
    maximum_roundoff = 0.0
    for label, length, horizon, held in CESARO_FIXTURES:
        average, endpoint_norm = cesaro_response(length, horizon)
        exact, source = finite_green(length)
        relative = float(np.linalg.norm(average - exact) / np.linalg.norm(exact))
        equation = float(np.linalg.norm(laplacian_float(average) - source) / np.linalg.norm(source))
        scale = float(np.vdot(exact, average).real / np.vdot(exact, exact).real)
        # Precision control repeats the same frozen law in longdouble arithmetic.
        previous = np.zeros(source.shape, dtype=np.longdouble)
        current = np.zeros_like(previous); accumulator = np.zeros_like(previous)
        source_long = source.astype(np.longdouble)
        for _ in range(horizon):
            following = (2 * current - previous
                         - np.longdouble(CESARO_ALPHA) * laplacian_float(current)
                         + np.longdouble(CESARO_ALPHA) * source_long)
            previous, current = current, following; accumulator += current
        long_average = accumulator / horizon
        roundoff = float(np.linalg.norm(average.astype(np.longdouble) - long_average)
                         / np.linalg.norm(long_average))
        maximum_roundoff = max(maximum_roundoff, roundoff)
        far = tuple([length // 2] * 3)
        rows.append({
            "fixture": label, "length": length, "horizon_update_count": horizon,
            "held": held, "float64_relative_Cesaro_to_static_Green": relative,
            "float64_absolute_Cesaro_to_static_Green": float(np.linalg.norm(average - exact)),
            "static_equation_relative_residual": equation,
            "static_equation_absolute_residual": float(np.linalg.norm(laplacian_float(average) - source)),
            "projection_scale_diagnostic_not_applied": scale,
            "float64_vs_longdouble_relative_residual": roundoff,
            "far_Cesaro_value": float(average[far]), "far_static_Green_value": float(exact[far]),
            "endpoint_norm_not_used_as_time": endpoint_norm,
        })

    coefficient = 5 / (32 * math.pi)
    green_rows = []
    for label, point in (("HELD_AXIS", (64, 0, 0)),
                         ("HELD_FACE", (40, 40, 0)),
                         ("HELD_BODY", (32, 32, 32))):
        vector = np.asarray(point, float); radius = float(np.linalg.norm(vector)); unit = vector / radius
        k4 = float(np.sum(unit ** 4) - 3 / 5)
        value = infinite_lattice_green(point)
        measured = float((value - 1 / (4 * math.pi * radius)) * radius ** 3 / k4)
        green_rows.append({
            "fixture": label, "point": point, "lattice_Green": value,
            "measured_cubic_coefficient": measured, "predicted_5_over_32pi": coefficient,
            "relative_residual": abs(measured / coefficient - 1),
        })
    max_green = max(row["relative_residual"] for row in green_rows)

    receiver_sign = math.copysign(1, rows[-1]["far_static_Green_value"])
    matched = {
        "source_off": [4, 4], "receiver_zero": [4, 4],
        "delay_candidate": [3, 4], "advance_candidate": [5, 4],
        "delay_fraction": str(Fraction(3, 4)), "advance_fraction": str(Fraction(5, 4)),
        "response_sign_at_frozen_far_receiver": receiver_sign,
        "mapping_from_response_sign_to_delay_or_advance_is_supplied": True,
        "Cycle570_matched_endpoint_receipt_passes": True,
    }
    residuals = [row["float64_relative_Cesaro_to_static_Green"] for row in rows]
    output = {
        "object": "stable reversible alpha=1/12 wave Cesaro bridge to the common cubic Laplacian Green surface",
        "disposition": "CONSTRUCTIVE_PREDICTION_BRIDGE; FINITE_HORIZON_AND_EVENT_CALIBRATION_REMAIN_SUPPLIED",
        "frozen_before_outputs": {"alpha": CESARO_ALPHA, "precision": "float64 with longdouble control",
                                  "source_normalization": "unit point minus uniform 1/L^3; no fitted amplitude",
                                  "fixtures": [list(item) for item in CESARO_FIXTURES]},
        "rows": rows,
        "maximum_float64_vs_longdouble_residual": maximum_roundoff,
        "Cesaro_relative_residuals": residuals,
        "same_exact_operator_bridge": "the alpha-scaled reversible recurrence has Cesaro fixed equation L phi=rho; Cycle588's static surface is the infinite-volume inverse of the same L",
        "Cycle588_585_Green_rows": green_rows,
        "maximum_5_over_32pi_relative_residual": max_green,
        "parameters_refit": 0,
        "matched_event_surface": matched,
        "finite_horizon_directly_measures_cubic_coefficient": False,
        "Cycle451_570_select_response_order_or_sign": False,
        "update_count_is_time": False,
        "endpoint_norm_is_probability_or_occurrence": False,
        "physical_M2_compiler_for_alpha_1_over_12": False,
        "comparison_is_gravity": False,
    }
    check("route C frozen Cesaro fixtures approach the exact finite static Green surface with precision control",
          max(residuals) < 0.01 and all(residuals[index + 1] < residuals[index]
                                       for index in range(len(residuals) - 1))
          and maximum_roundoff < 1e-11, rows)
    check("route C recovers the inherited 5/(32pi) coefficient without refit through the common exact Laplacian",
          max_green < 0.002 and all(row["relative_residual"] > 0 for row in green_rows), green_rows)
    check("route C keeps matched 3:4/5:4 events exact while refusing sign/order selection",
          matched["delay_fraction"] == "3/4" and matched["advance_fraction"] == "5/4"
          and matched["mapping_from_response_sign_to_delay_or_advance_is_supplied"]
          and not output["Cycle451_570_select_response_order_or_sign"], matched)
    return output


def no_go_audit() -> dict:
    families = [
        ["one-state rational transfer", "Padé recurrence plus Julia dilation", "exact R(w)", "ATTEMPTED_MATHEMATICALLY; FINITE_PREPARATION_OPEN"],
        ["two-channel FIR lattice filter", "Fejer-Riesz paraunitary plus eight delay sections", "bounded fixed-parameter approximate line encoder", "ATTEMPTED_POSITIVE_C604"],
        ["midpoint path dilation", "Cycle601 q=4 coherent recombination", "bounded approximate line encoder", "PRIOR_ATTEMPTED"],
        ["finite DFT code", "Cycle596 exact torus quadrature", "exact finite line map", "PRIOR_RULED_OUT_ONLY_FOR_CONSTANT_OVERHEAD"],
        ["metric-rail product", "project kernel before factorization", "exact expanded-image preservation", "ATTEMPTED_POSITIVE_C604"],
        ["raw edge product", "Cycle579 matching factors", "actual Regge product", "PRIOR_RULED_OUT_ONLY_FOR_IMAGE_PRESERVATION"],
        ["paired modular fields", "reciprocal kick-drift", "conserved local response ledger", "ATTEMPTED_POSITIVE_C604"],
        ["unilateral modular wave", "Cycle601 sourced leapfrog", "local retarded/advanced response", "PRIOR_ATTEMPTED"],
        ["stable reversible wave", "alpha=1/12 Cesaro", "finite-to-static prediction bridge", "ATTEMPTED_POSITIVE_C604"],
        ["static constrained inverse", "Cycles585/588 Kjoin=L", "1/r plus cubic coefficient", "PRIOR_ATTEMPTED"],
    ]
    walls = {
        "W_exact_sinc": "P8 and Padé R only approximate the exact line factor",
        "W_rational_preparation": "the exact rational steady recurrence lacks finite-depth autonomous preparation",
        "W_gate_alphabet": "frozen parameterized two-M2 matrices were not lowered to an accepted finite gate alphabet",
        "W_even_color": "same-role metric hopping uses a supplied bipartite matching law restricted to even tori",
        "W_target_exponential": "the ordered metric product is not the exact target exponential",
        "W_source_identity": "modular source/recoil words are not identified with physical matter",
        "W_order_sign": "both reciprocal factor orders and both coupling signs survive",
        "W_static_limit": "finite Cesaro update counts do not equal the infinite static limit",
        "W_event_calibration": "the response-sign to 3:4/5:4 event association is supplied",
        "W_joint_compiler": "Cycle601's recurrent pair remains unjoined to Cycle590",
    }
    names = tuple(walls)
    pairs = [[names[i], names[j], "independent under the tested constructions"]
             for i in range(len(names)) for j in range(i + 1, len(names))]
    output = {
        "N1_alternative_route_enumeration": families,
        "N2_pairwise_wall_independence": pairs,
        "N3_hidden_wall_scan": [
            "Padé order one", "FIR termination H=8", "minimum-phase spectral-factor choice",
            "vacuum garbage input", "even-torus color", "factor schedule", "31-bit words",
            "coupling sign", "kick/drift order", "alpha=1/12", "finite Cesaro horizons",
            "zero-mean source", "event-sign calibration",
        ],
        "N4_residual_matching": walls,
        "N5_rhetoric_audit": "exact applies only to Julia/FIR unitarity, code preservation, inverse, modular ledger, and operator identity; all sinc, exponential, physical-source, static-limit, and event claims are scoped",
        "N6_partial_closure_paths": [
            "FIR closes finite local fixed-parameter dilation and image preservation without exact sinc or accepted-alphabet lowering",
            "reciprocal kick-drift closes a conserved local ledger without physical source identification or order selection",
            "Cesaro closes a common-operator prediction bridge without making update count time or calibrating events",
        ],
        "N7_concrete_steelman": (
            "A higher-order Schur rational colligation with an autonomously prepared invariant state could improve full-zone error; "
            "a translation-covariant QCA factorization could remove the even-torus color; a matter-coupled symplectic law plus matched detector could select response sign/order."
        ),
        "N8_cross_cycle_echo": {
            "Cycle596_601": "size-growing exact DFT versus bounded midpoint approximation and raw-image leakage",
            "Cycle604_new": "finite paraunitary family and projected metric product close dilation/image walls but not exact sinc",
            "Cycle585_588": "same exact L operator supplies the static coefficient surface",
            "Cycle451_570": "matched event words survive but calibration remains supplied",
        },
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }
    check("full N1-N8 audit blocks a broad negative and axiom pressure",
          len(families) >= 5 and len(pairs) == len(names) * (len(names) - 1) // 2
          and len(output["N3_hidden_wall_scan"]) >= 8
          and not output["shared_route_independent_obstruction"] and not output["axiom_pressure"], output)
    return output


def main() -> None:
    pins = dependency_shore()
    note_contract()
    routeA = route_a()
    routeB = route_b()
    routeC = route_c()
    nogo = no_go_audit()
    head = subprocess.run(("git", "rev-parse", "HEAD"), cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout.strip()
    receipt = {
        "cycle": 604, "authority": AUTHORITY, "audit": AUDIT, "HEAD": head,
        "status": "three constructive partials; no shared no-go and no axiom pressure",
        "pins": pins, "route_A_rational_Regge": routeA,
        "route_B_reciprocal_response": routeB, "route_C_prediction_bridge": routeC,
        "inventory": {
            "supplied": [
                "Padé order one and H=8 DC termination", "minimum-phase complement and vacuum garbage input",
                "even-torus bipartite color and all gate schedules", "Cycle576 kernel and Cycle579 angle",
                "31-bit modular alphabet, source word, coupling sign, and kick/drift order",
                "alpha=1/12, zero-mean source, finite Cesaro horizons, float precision",
                "response-sign/event calibration and Cycle451/570 matched identities",
            ],
            "derived_or_executed": [
                "rational contraction and Julia dilation", "FIR spectral complement and exact paraunitary factorization",
                "co-designed metric product exact expanded-image preservation", "modular reciprocal ledger and continuity",
                "Cesaro/common-Laplacian static bridge and inherited cubic coefficient comparison",
            ],
            "not_derived": [
                "exact finite-depth rational steady transfer", "accepted finite gate-alphabet lowering", "exact sinc", "odd-torus color-free product",
                "exact Regge target exponential", "physical matter/recoil or stress-energy identification",
                "response sign/order selection", "time", "gravity", "finite-horizon static equality",
                "event calibration", "Born probability", "Record actuality", "joint Cycle590 recurrent-pair compiler",
            ],
        },
        "six_wall_ledger": {
            "C_ref": "UNCHANGED: all24/all576 sector covariance passes; frame preparation, response sign/order, and event calibration remain supplied",
            "C_num": "PARTIAL ADVANCE: fixed rational/FIR coefficients and exact modular ledger are explicit; word scale and physical number reference remain supplied",
            "C_wrap": "UNCHANGED: no wrapped phase or update count is interpreted as energy, rate, or time",
            "C_int": "ADVANCED MATHEMATICALLY: reciprocal source-field exchange and exact continuity exist; physical matter/recoil, stress-energy, and joint Cycle590 coupling remain open",
            "C_local": "ADVANCED: exact fixed-parameter paraunitary and exact expanded-image product are bounded on even tori; accepted finite-alphabet lowering, exact sinc, odd-torus color, and target exponential remain open",
            "C_source": "PARTIAL ADVANCE: source-field recoil ledger and static prediction bridge are explicit; source identity, response selection, backreaction calibration, and gravity remain open",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.0, "time": 3.0, "inertia_matter": 4.0,
            "gravity_source": 3.25, "Born_probability": 2.0,
        },
        "no_go_discipline": nogo,
        "strongest_constructive_result": (
            "an exact degree-8 two-channel fixed-parameter paraunitary M2 line encoder with retained garbage, conjugated around a metric-rail Regge product so the expanded approximate image is preserved exactly"
        ),
        "optimal_next_campaign": (
            "replace the even-torus color with a translation-covariant QCA metric product and couple the reciprocal source word to accepted matter plus an autonomous matched detector capable of selecting sign/order"
        ),
        "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0,
        "elapsed_seconds": perf_counter() - START,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                                 * (1024 if sys.platform.startswith("linux") else 1)),
    }
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True,
                   default=lambda value: value.item() if isinstance(value, np.generic) else str(value)) + "\n",
        encoding="utf-8",
    )
    print("RECEIPT", json.dumps(receipt, sort_keys=True, default=lambda value: value.item() if isinstance(value, np.generic) else str(value)))
    print("SUMMARY", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": receipt["elapsed_seconds"], "maximum_RSS_bytes": receipt["maximum_RSS_bytes"],
        "route_A": routeA["disposition"], "route_B": routeB["disposition"],
        "route_C": routeC["disposition"], "broad_negative_gate": nogo["broad_negative_gate"],
        "axiom_pressure": False,
    }, sort_keys=True))
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
