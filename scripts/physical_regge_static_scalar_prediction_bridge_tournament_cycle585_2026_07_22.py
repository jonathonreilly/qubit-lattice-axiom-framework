#!/usr/bin/env python3
"""Cycle 585: actual-Regge static-scalar/prediction bridge tournament.

Route A takes the Cycle-576 raw Regge Hessian and unnormalised deficit row at
zero fourth momentum, restricts them to the declared metric image, fixes only
the four null directions, and forms the gauge-invariant h_44 Schur complement.
Route B constructs and solves a finite-range cubic approximant frozen from that
Schur complement.  Route C applies a Cesaro phase filter to the Cycle-581
generalized symmetric update on the actual edge Hessian.

No fitted/held kernel from Cycle 460 is consumed.  Update steps are not called
time; a generator is not called a rate; no result is called gravity, energy,
stress, a Newtonian calibration, or an Einstein equation.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_2026_07_22 as cycle581


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REGGE_STATIC_SCALAR_PREDICTION_BRIDGE_TOURNAMENT_"
    "CYCLE585_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9.0e-9
SCALAR_INDEX = cycle576.regge.HCOMPS.index((3, 3))
GRAPH_CORRECTION = 5.0 / (32.0 * math.pi)
PHASE_REPETITIONS = 8
PHASE_N_PER_L2 = 2048
PASS = 0
FAIL = 0


DEPENDENCIES = {
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":
        "06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
        "2d5650c57d5518e274803f5c511886981c8572b553dda926739cc98199939c20",
    "scripts/physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_2026_07_22.py":
        "cd9cc6be42953660f46409e1ca414d59f0a23b7d10a1a34a7b300ebd00978db6",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGGE_SYMMETRIC_ACCURACY_ORDER_ORBIT_TOURNAMENT_CYCLE581_NOTE_2026-07-22.md":
        "24cbe67e1db2124c24b0aebd1ce563debb8ac8241520307c5f32c191a91a8037",
    "outputs/physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_cold_2026_07_22.txt":
        "b2d9c1af8714229330d4ca9e79849858c479dbc2a1e54b9387df246f455ee21e",
    "scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py":
        "dc022c84cdb8003b9f56f8587255d5bb14a5efbdb59faa9e64470f0d0826a66f",
    "docs/LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md":
        "1f9c4718f6e6c5f2d2a3e6ccc30f4499ff6248a909d924b33a250f97cee97540",
    "scripts/frontier_gravity_leading_lattice_correction_cubic_anisotropy.py":
        "e168cffdd005d58ec929e51e9122f3766efafc1cee82a86f9502427acece18a5",
    "docs/GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md":
        "933e516364782dc51c03e07863370ab891e9b7ff8d4afa4ebfd355576cb8f079",
}


RECON_ONLY_NOT_PREMISES = {
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_PREDICTION_BRIDGE_CONTRACT_CYCLE420_NOTE_2026-07-19.md":
        "565e74882e65be9d401fbfc13d8e0a18bb6deebd703220ae766c00e00230865c",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATIC_QUADRUPOLE_STINESPRING_NN_COMPILER_CYCLE460_NOTE_2026-07-19.md":
        "2f1bccef97dd5b5155bd6baaf73c7e1e0eba852066a52cd57b6cecfe3e34da41",
    "docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md":
        "a483e7c46af52794f68ebd40ddb118eaac8b6f7201a25ab4f3ab0beb20e11a4e",
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
    return sha256(path.read_bytes()).hexdigest() if path.exists() else "MISSING"


def dependency_controls() -> dict:
    observed = {path: file_sha(ROOT / path) for path in DEPENDENCIES}
    recon_observed = {path: file_sha(ROOT / path) for path in RECON_ONLY_NOT_PREMISES}
    return {
        "expected": DEPENDENCIES,
        "observed": observed,
        "recon_only_expected": RECON_ONLY_NOT_PREMISES,
        "recon_only_observed": recon_observed,
        "Cycle460_used_as_evidence_or_premise": False,
        "pass": observed == DEPENDENCIES and recon_observed == RECON_ONLY_NOT_PREMISES,
    }


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 585", "route a", "route b", "route c",
        "actual cycle-576", "raw unnormalized deficit", "zero fourth momentum", "schur",
        "four gauge null", "gauge-penalty invariance", "extra edge zero", "metric-image constraint", "not locally enforced",
        "no fit", "held", "graph laplacian", "5/(32pi)", "5/(24pi)", "contact response",
        "cesaro", "cycle-581", "not physical time", "generator is not a rate", "source deletion",
        "inverse", "proper-cubic", "all 24", "576", "no host inverse in the update",
        "cycle 460 is not evidence or a premise", "not gravity", "not physical energy",
        "not physical stress", "not a newtonian calibration", "actual cycle-230 contact", "mass",
        "seam", "leakage", "physical m2 arithmetic remains open", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no shared obstruction", "no axiom pressure",
        "positive partial construction with explicit residuals",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def graph_symbol(momentum3: np.ndarray) -> float:
    return float(6.0 - 2.0 * np.sum(np.cos(momentum3)))


def metric_static_reduction(momentum3: np.ndarray, null_penalty: float = 1.0) -> dict:
    """Gauge-fix the metric image and Schur-eliminate every field but h_44."""
    if null_penalty <= 0:
        raise ValueError("null-space penalty must be positive")
    momentum = np.r_[np.asarray(momentum3, dtype=float), 0.0]
    q = cycle576.frame_averaged_metric_hessian(momentum)
    source = cycle576.frame_averaged_source_row(momentum).conj()
    eigenvalues, eigenvectors = np.linalg.eigh((q + q.conj().T) / 2)
    cutoff = 1.0e-8 * max(float(np.max(abs(eigenvalues))), 1.0e-15)
    zero = abs(eigenvalues) < cutoff
    z = eigenvectors[:, zero]
    # Adding a unit penalty only on the exact null space chooses a gauge; it
    # does not change the h_44 Schur result because h_44 is static-gauge invariant.
    q_fixed = q + null_penalty * z @ z.conj().T
    rest = [index for index in range(10) if index != SCALAR_INDEX]
    a = q_fixed[np.ix_(rest, rest)]
    q_rs = q_fixed[rest, SCALAR_INDEX]
    source_r = source[rest]
    eliminated_q = np.linalg.solve(a, q_rs)
    eliminated_source = np.linalg.solve(a, source_r)
    schur = q_fixed[SCALAR_INDEX, SCALAR_INDEX] - q_fixed[SCALAR_INDEX, rest] @ eliminated_q
    reduced_source = source[SCALAR_INDEX] - q_fixed[SCALAR_INDEX, rest] @ eliminated_source
    return {
        "schur": complex(schur),
        "reduced_source": complex(reduced_source),
        "normalized_operator": float((-2.0 * schur).real),
        "normalized_source": complex(-2.0 * reduced_source),
        "scalar_response": complex(reduced_source / schur),
        "null_count": int(np.sum(zero)),
        "maximum_null_residual": float(np.max(abs(q @ z))),
        "maximum_source_Ward_residual": float(np.max(abs(z.conj().T @ source))),
        "maximum_static_scalar_gauge_overlap": float(np.max(abs(z[SCALAR_INDEX]))),
        "gauge_fixed_rest_condition_number": float(np.linalg.cond(a)),
        "null_space_penalty": float(null_penalty),
    }


def directional_quartic(direction: tuple[float, float, float], scale: float) -> float:
    direction_array = np.asarray(direction, dtype=float)
    value = metric_static_reduction(scale * direction_array)["normalized_operator"]
    return float((value - scale ** 2 * np.dot(direction_array, direction_array)) / scale ** 4)


def richardson_limit(direction: tuple[float, float, float], scale: float) -> tuple[float, dict]:
    coarse = directional_quartic(direction, scale)
    fine = directional_quartic(direction, scale / 2)
    richardson = float((4.0 * fine - coarse) / 3.0)
    return richardson, {"coarse": coarse, "fine": fine, "Richardson": richardson}


def gauge_penalty_controls() -> dict:
    penalties = (0.25, 1.0, 4.0)
    fixtures = (
        ("TRAIN_AXIS_TAYLOR", np.asarray((0.06, 0.0, 0.0)), False),
        ("TRAIN_CONTACT", np.asarray((0.08, 0.048, 0.016)), False),
        ("HELD_GENERIC", np.asarray((0.04, 0.028, 0.012)), True),
        ("HELD_BODY", np.asarray((0.03, 0.03, 0.03)), True),
        ("GENERIC_COVARIANCE", np.asarray((0.17, 0.11, 0.07)), True),
    )
    rows = []
    maximum_operator_change = 0.0
    maximum_source_change = 0.0
    maximum_response_change = 0.0
    for label, momentum, held in fixtures:
        reference = metric_static_reduction(momentum, 1.0)
        values = []
        for penalty in penalties:
            row = metric_static_reduction(momentum, penalty)
            operator_change = abs(row["normalized_operator"] - reference["normalized_operator"])
            source_change = abs(row["normalized_source"] - reference["normalized_source"])
            response_change = abs(row["scalar_response"] - reference["scalar_response"])
            maximum_operator_change = max(maximum_operator_change, operator_change)
            maximum_source_change = max(maximum_source_change, source_change)
            maximum_response_change = max(maximum_response_change, response_change)
            values.append({
                "penalty": penalty,
                "normalized_operator": row["normalized_operator"],
                "normalized_source": [float(row["normalized_source"].real), float(row["normalized_source"].imag)],
                "scalar_response": [float(row["scalar_response"].real), float(row["scalar_response"].imag)],
                "operator_change_from_unit_penalty": float(operator_change),
                "source_change_from_unit_penalty": float(source_change),
                "response_change_from_unit_penalty": float(response_change),
            })
        rows.append({
            "fixture": label,
            "held": held,
            "momentum": momentum.tolist(),
            "penalty_rows": values,
        })
    return {
        "positive_null_space_penalties": penalties,
        "fixtures": rows,
        "maximum_normalized_operator_change": maximum_operator_change,
        "maximum_normalized_source_change": maximum_source_change,
        "maximum_scalar_response_change": maximum_response_change,
        "penalty_selected_from_held_data": False,
    }


def edge_zero_mode_rows() -> tuple[dict, ...]:
    rows = []
    for label, momentum3, held in (
        ("TRAIN_L3_AXIS", (2 * math.pi / 3, 0.0, 0.0), False),
        ("HELD_L4_FACE", (math.pi / 2, math.pi / 2, 0.0), True),
        ("HELD_L5_BODY", (2 * math.pi / 5,) * 3, True),
    ):
        momentum = np.r_[momentum3, 0.0]
        q = cycle576.base_edge_hessian(momentum)
        source = cycle576.base_deficit_source(momentum).conj()
        values, vectors = np.linalg.eigh((q + q.conj().T) / 2)
        cutoff = 1.0e-9 * max(float(np.max(abs(values))), 1.0)
        zero = abs(values) < cutoff
        projection = vectors[:, zero] @ (vectors[:, zero].conj().T @ source)
        rows.append({
            "fixture": label,
            "held": held,
            "edge_zero_modes": int(np.sum(zero)),
            "discrete_gauge_modes": 4,
            "extra_edge_zero_modes": int(np.sum(zero)) - 4,
            "raw_source_null_projection_fraction": float(np.linalg.norm(projection) / np.linalg.norm(source)),
            "raw_edge_static_equation_solvable_without_projection": bool(np.linalg.norm(projection) < TOL),
        })
    return tuple(rows)


def route_a_static_reduction() -> dict:
    # Training data freeze two independent cubic quartic coefficients.  No
    # receiver value, Green kernel, or held momentum enters this freeze.
    axis, axis_rows = richardson_limit((1.0, 0.0, 0.0), 0.06)
    face, face_rows = richardson_limit((1.0, 1.0, 0.0), 0.06)
    cross = face - 2.0 * axis
    anisotropic_symbol_coefficient = axis - cross / 2.0
    correction_ratio = -12.0 * anisotropic_symbol_coefficient
    frozen_green_correction = correction_ratio * GRAPH_CORRECTION
    penalty_controls = gauge_penalty_controls()

    held_rows = []
    for label, direction, scale in (
        ("HELD_GENERIC_A", (1.0, 0.7, 0.3), 0.04),
        ("HELD_GENERIC_B", (0.4, 1.0, 0.8), 0.025),
        ("HELD_BODY", (1.0, 1.0, 1.0), 0.03),
    ):
        vector = scale * np.asarray(direction)
        exact = metric_static_reduction(vector)["normalized_operator"]
        sum4 = float(np.sum(vector ** 4))
        cross4 = float(sum(vector[left] ** 2 * vector[right] ** 2 for left, right in combinations(range(3), 2)))
        frozen = float(np.dot(vector, vector) + axis * sum4 + cross * cross4)
        held_rows.append({
            "fixture": label,
            "momentum": vector.tolist(),
            "held": True,
            "exact_Regge_scalar_symbol": exact,
            "frozen_quartic_symbol": frozen,
            "absolute_residual": abs(exact - frozen),
            "residual_over_abs_k_to_six": abs(exact - frozen) / np.linalg.norm(vector) ** 6,
            "parameters_refit": 0,
        })

    gauge_rows = []
    covariance = 0.0
    generic = np.asarray((0.17, 0.11, 0.07))
    base = metric_static_reduction(generic)
    for frame in cycle576.FRAMES:
        row = metric_static_reduction(frame @ generic)
        covariance = max(covariance, abs(row["normalized_operator"] - base["normalized_operator"]))
        gauge_rows.append(row)

    contact_rows = []
    for label, direction, scale, held in (
        ("TRAIN_CONTACT", (1.0, 0.6, 0.2), 0.08, False),
        ("HELD_CONTACT_HALF_K", (1.0, 0.6, 0.2), 0.04, True),
        ("HELD_CONTACT_OTHER_DIR", (0.3, 1.0, 0.7), 0.035, True),
    ):
        momentum = scale * np.asarray(direction)
        row = metric_static_reduction(momentum)
        contact_rows.append({
            "fixture": label,
            "held": held,
            "momentum": momentum.tolist(),
            "scalar_response": [float(row["scalar_response"].real), float(row["scalar_response"].imag)],
            "response_times_graph_symbol": float(abs(row["scalar_response"]) * graph_symbol(momentum)),
            "parameters_refit": 0,
        })

    return {
        "route": "A_metric_image_gauge_fixed_h44_Schur_reduction",
        "construction": "K_R(k)=-2 Schur_h44[M(k)^dag Q_R(k) M(k)] at k_4=0",
        "normalization_basis": "the derived Cycle576 continuum coefficient -1/2; no Green value or held datum",
        "raw_source_reduction": "B_R(k)=-2 times the Schur-reduced raw unnormalised deficit row",
        "metric_image_constraint_status": "declared exact line-averaged metric image; local physical-M2 enforcement not compiled",
        "gauge_null_modes": 4,
        "maximum_metric_null_residual": max(row["maximum_null_residual"] for row in gauge_rows),
        "maximum_metric_source_Ward_residual": max(row["maximum_source_Ward_residual"] for row in gauge_rows),
        "maximum_h44_gauge_overlap": max(row["maximum_static_scalar_gauge_overlap"] for row in gauge_rows),
        "gauge_penalty_invariance": penalty_controls,
        "maximum_all24_scalar_covariance_residual": covariance,
        "all576_group_products_inherited_exact_pinned": True,
        "train_axis_directional_quartic": axis_rows,
        "train_face_directional_quartic": face_rows,
        "frozen_sum_k_i4_coefficient": axis,
        "frozen_sum_cross_k_i2_k_j2_coefficient": cross,
        "reference_graph_sum_k_i4_coefficient": -1.0 / 12.0,
        "reference_graph_cross_coefficient": 0.0,
        "frozen_anisotropic_symbol_coefficient": anisotropic_symbol_coefficient,
        "frozen_cubic_correction_ratio_to_graph": correction_ratio,
        "reference_graph_Green_correction": GRAPH_CORRECTION,
        "frozen_Regge_scalar_Green_correction": frozen_green_correction,
        "reference_surface": "1/(4pi r)+[5/(32pi)]K4/r^3+O(r^-5)",
        "derived_scalar_operator_surface": "1/(4pi r)+c_R K4/r^3+O(r^-5), c_R frozen below",
        "exact_reference_surface_match": abs(frozen_green_correction - GRAPH_CORRECTION) < 2.0e-5,
        "held_quartic_rows": held_rows,
        "raw_source_contact_rows": contact_rows,
        "raw_source_has_inverse_L_pole": False,
        "edge_zero_mode_rows": edge_zero_mode_rows(),
        "actual_raw_edge_equation_requires_metric_constraint_or_range_projection": True,
        "parameters_fitted_to_Green_or_held_data": 0,
        "physical_gravity_or_Newtonian_calibration_derived": False,
    }


def apply_axis_laplacian(field: np.ndarray, axis: int) -> np.ndarray:
    return 2.0 * field - np.roll(field, 1, axis=axis) - np.roll(field, -1, axis=axis)


def apply_local_approximant(field: np.ndarray, cross: float) -> np.ndarray:
    axes = [apply_axis_laplacian(field, axis) for axis in range(3)]
    result = sum(axes)
    for left, right in combinations(range(3), 2):
        result = result + cross * apply_axis_laplacian(axes[left], right)
    return result


def approximant_symbol(momentum3: np.ndarray, cross: float) -> float:
    one = 2.0 - 2.0 * np.cos(momentum3)
    return float(np.sum(one) + cross * sum(one[left] * one[right] for left, right in combinations(range(3), 2)))


def rotate_field(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]
    output = np.empty_like(field)
    for index in np.ndindex(field.shape):
        source = tuple(int(value % length) for value in frame.T @ np.asarray(index))
        output[index] = field[source]
    return output


def source_fixture(length: int, kind: str) -> np.ndarray:
    source = np.zeros((length, length, length), dtype=float)
    if kind == "dipole":
        source[0, 0, 0] = 1.0
        source[1, 0, 0] = -1.0
    elif kind == "quadrupole":
        source[0, 0, 0] = 1.0
        source[1, 1, 0] = 1.0
        source[1, 0, 0] = -1.0
        source[0, 1, 0] = -1.0
    else:
        rng = np.random.default_rng(585 + length)
        source = rng.normal(size=source.shape)
        source -= np.mean(source)
    return source


def exact_periodic_solution(source: np.ndarray, cross: float) -> np.ndarray:
    length = source.shape[0]
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    symbol = np.empty(source.shape)
    for index in np.ndindex(source.shape):
        symbol[index] = approximant_symbol(np.asarray([frequencies[i] for i in index]), cross)
    transformed = np.fft.fftn(source)
    output = np.zeros_like(transformed)
    mask = symbol > 1.0e-13
    output[mask] = transformed[mask] / symbol[mask]
    return np.fft.ifftn(output).real


def richardson_fixture(length: int, kind: str, held: bool, cross: float) -> dict:
    source = source_fixture(length, kind)
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    spectrum = np.asarray([
        approximant_symbol(np.asarray([frequencies[i] for i in index]), cross)
        for index in np.ndindex(source.shape)
    ])
    nonzero = spectrum[spectrum > 1.0e-13]
    lambda_min = float(np.min(nonzero))
    lambda_max = float(np.max(nonzero))
    omega = 2.0 / (lambda_min + lambda_max)
    contraction = (lambda_max - lambda_min) / (lambda_max + lambda_min)
    target_relative_bound = 1.0e-8
    iterations = int(math.ceil(math.log(target_relative_bound) / math.log(contraction)))
    current = np.zeros_like(source)
    tape = []
    maximum_reverse_consistency = 0.0
    for _ in range(iterations):
        old = current.copy()
        tape.append(old)
        current = old + omega * (source - apply_local_approximant(old, cross))
    equation_residual = float(np.linalg.norm(apply_local_approximant(current, cross) - source) / np.linalg.norm(source))
    exact = exact_periodic_solution(source, cross)
    solution_residual = float(np.linalg.norm(current - exact) / np.linalg.norm(exact))
    restored = current.copy()
    while tape:
        old = tape.pop()
        predicted = old + omega * (source - apply_local_approximant(old, cross))
        maximum_reverse_consistency = max(maximum_reverse_consistency, float(np.linalg.norm(restored - predicted)))
        restored = old
    deleted = np.zeros_like(source)
    for _ in range(iterations):
        deleted = deleted + omega * (-apply_local_approximant(deleted, cross))
    return {
        "fixture": f"{'HELD' if held else 'TRAIN'}_L{length}_{kind}",
        "held": held,
        "length": length,
        "source_zero_mean_residual": abs(float(np.sum(source))),
        "lambda_min_exact": lambda_min,
        "lambda_max_exact": lambda_max,
        "Richardson_omega": omega,
        "contraction_q": contraction,
        "iterations": iterations,
        "rigorous_relative_solution_error_bound": contraction ** iterations,
        "observed_relative_solution_error": solution_residual,
        "relative_equation_residual": equation_residual,
        "reverse_tape_consistency_residual": maximum_reverse_consistency,
        "reverse_restoration_residual": float(np.linalg.norm(restored)),
        "source_deletion_output_norm": float(np.linalg.norm(deleted)),
        "real_registers_if_full_tape_retained": int((iterations + 2) * length ** 3),
        "parameters_refit": 0,
    }


def route_b_local_solver(route_a: dict) -> dict:
    cross = float(route_a["frozen_sum_cross_k_i2_k_j2_coefficient"])
    rows = (
        richardson_fixture(5, "dipole", False, cross),
        richardson_fixture(7, "quadrupole", True, cross),
        richardson_fixture(9, "random", True, cross),
    )
    rng = np.random.default_rng(585)
    field = rng.normal(size=(5, 5, 5))
    covariance = 0.0
    for frame in cycle576.FRAMES:
        covariance = max(covariance, float(np.linalg.norm(
            apply_local_approximant(rotate_field(field, frame), cross)
            - rotate_field(apply_local_approximant(field, cross), frame)
        )))
    return {
        "route": "B_local_19_point_reversible_tape_Richardson_approximant",
        "operator": "K_app=L+beta sum_(i<j) L_i L_j",
        "beta_frozen_from_Route_A_train_only": cross,
        "support": "onsite plus 6 axial and 12 face-diagonal sites; L1 radius 2",
        "stencil_points": 19,
        "proper_cubic_covariance_maximum_residual": covariance,
        "positive_semidefinite_on_every_periodic_volume": cross >= 0,
        "only_zero_mode": "uniform scalar mode",
        "zero_mode_handling": "zero-mean source code; k=0 is never divided",
        "solver_law": "x_(n+1)=x_n+omega(b-K_app x_n), with every x_n retained on a reversible tape",
        "rigorous_error_law": "||e_N||_2 <= q^N ||e_0||_2, q=(lambda_max-lambda_min)/(lambda_max+lambda_min)",
        "fixtures": rows,
        "held_parameters_refit": 0,
        "local_reversible_declared_approximant_constructed": True,
        "literal_physical_M2_real_arithmetic_compiled": False,
        "physical_M2_layout_boundary": "19-neighbour reads and reversible tape registers are explicit; signed real arithmetic, precision code, and off-domain M2 law are not compiled",
        "exact_Regge_Schur_operator_solved": False,
        "Cycle460_kernel_or_receiver_anchor_consumed": False,
    }


def cesaro_phase_filter(unitaries: np.ndarray, sources: np.ndarray, terms: int) -> np.ndarray:
    """No inverse: accumulate theta sum (1-n/(N+1)) sin(n theta H_eff)b."""
    forward = sources.copy()
    backward = sources.copy()
    output = np.zeros_like(sources)
    adjoints = unitaries.conj().transpose(0, 2, 1)
    for n in range(1, terms + 1):
        forward = np.einsum("fij,fj->fi", unitaries, forward, optimize=True)
        backward = np.einsum("fij,fj->fi", adjoints, backward, optimize=True)
        output += (1.0 - n / (terms + 1.0)) * (backward - forward) / (2.0j)
    return cycle581.ANGLE * output


def phase_fixture(length: int, direction: tuple[int, int, int], held: bool) -> dict:
    momentum = np.r_[2 * math.pi / length * np.asarray(direction, dtype=float), 0.0]
    unitaries = []
    sources = []
    targets = []
    projected_sources = []
    zero_bases = []
    factor_counts = []
    null_fractions = []
    unitary_residual = 0.0
    for frame in cycle576.LIFTED_FRAMES:
        local = frame @ momentum
        hamiltonian = cycle576.REGGE_UPDATE_SCALE * cycle576.base_edge_hessian(local)
        source = cycle576.SOURCE_COUPLING * cycle576.base_deficit_source(local).conj()
        unitary, factors = cycle581.dense_strang_unitary(hamiltonian, repetitions=PHASE_REPETITIONS)
        values, vectors = np.linalg.eigh((hamiltonian + hamiltonian.conj().T) / 2)
        cutoff = 1.0e-9 * max(float(np.max(abs(values))), 1.0)
        nonzero = abs(values) > cutoff
        zero = vectors[:, ~nonzero]
        projected = vectors[:, nonzero] @ (vectors[:, nonzero].conj().T @ source)
        target = (vectors[:, nonzero] / values[nonzero]) @ (vectors[:, nonzero].conj().T @ source)
        unitaries.append(unitary)
        sources.append(source)
        targets.append(target)
        projected_sources.append(projected)
        zero_bases.append(zero)
        factor_counts.append(factors)
        null_fractions.append(float(np.linalg.norm(source - projected) / np.linalg.norm(source)))
        unitary_residual = max(unitary_residual, float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(15))))
    unitaries_array = np.asarray(unitaries)
    sources_array = np.asarray(sources)
    targets_array = np.asarray(targets)
    projected_array = np.asarray(projected_sources)
    terms = PHASE_N_PER_L2 * length ** 2
    filtered = cesaro_phase_filter(unitaries_array, sources_array, terms)
    inverse_filter = cesaro_phase_filter(unitaries_array.conj().transpose(0, 2, 1), sources_array, terms)
    h_outputs = []
    null_output = 0.0
    for index, frame in enumerate(cycle576.LIFTED_FRAMES):
        hamiltonian = cycle576.REGGE_UPDATE_SCALE * cycle576.base_edge_hessian(frame @ momentum)
        h_outputs.append(hamiltonian @ filtered[index])
        null_output = max(null_output, float(np.linalg.norm(zero_bases[index].conj().T @ filtered[index]) / max(np.linalg.norm(filtered[index]), 1.0e-15)))
    h_outputs_array = np.asarray(h_outputs)
    deleted = cesaro_phase_filter(unitaries_array, np.zeros_like(sources_array), min(terms, 16))

    # The co-present sector law is covariant because F at Rk is the FR sector
    # at k.  Verify all 24x24 products and the associated momentum identities.
    covariance = 0.0
    products = 0
    for rotation in cycle576.FRAMES:
        for frame in cycle576.FRAMES:
            target = cycle576.FRAME_LOOKUP[tuple((frame @ rotation).reshape(-1))]
            covariance = max(covariance, float(np.linalg.norm(
                cycle576.lift_frame(frame) @ cycle576.lift_frame(rotation) @ momentum
                - cycle576.LIFTED_FRAMES[target] @ momentum
            )))
            products += 1

    return {
        "fixture": f"{'HELD' if held else 'TRAIN'}_L{length}_{''.join(map(str, direction))}",
        "held": held,
        "length": length,
        "momentum": momentum.tolist(),
        "Cycle581_Strang_repetitions": PHASE_REPETITIONS,
        "Cesaro_terms": terms,
        "phase_filter_law": "theta sum_n=1^N (1-n/(N+1))(U^-n-U^n)/(2i)",
        "factor_counts_per_sector": factor_counts,
        "maximum_unitarity_residual": unitary_residual,
        "inverse_filter_oddness_residual": float(np.linalg.norm(inverse_filter + filtered) / np.linalg.norm(filtered)),
        "relative_range_pseudoinverse_response_residual": float(np.linalg.norm(filtered - targets_array) / np.linalg.norm(targets_array)),
        "relative_range_equation_residual": float(np.linalg.norm(h_outputs_array - projected_array) / np.linalg.norm(projected_array)),
        "minimum_raw_source_null_fraction": min(null_fractions),
        "maximum_raw_source_null_fraction": max(null_fractions),
        "maximum_target_zero_subspace_leakage_fraction": null_output,
        "source_deletion_output_norm": float(np.linalg.norm(deleted)),
        "all576_sector_product_momentum_residual": covariance,
        "all576_sector_products": products,
        "parameters_refit": 0,
    }


def route_c_phase_filter() -> dict:
    rows = (
        phase_fixture(3, (1, 0, 0), False),
        phase_fixture(4, (1, 1, 0), True),
        phase_fixture(5, (1, 1, 1), True),
    )
    return {
        "route": "C_Cycle581_symmetric_update_Cesaro_phase_filter",
        "construction": "in-state forward/inverse powers of the actual scaled edge-Regge symmetric update; no inverse occurs in the update",
        "long_response_limit": "for a nonzero eigenvalue lambda and exact U=exp(-i theta H), the Cesaro multiplier tends to (theta/2)cot(theta lambda/2)=1/lambda+O(theta^2 lambda)",
        "zero_mode_multiplier": 0.0,
        "fixtures": rows,
        "held_parameters_refit": 0,
        "all24_co_present_sectors": True,
        "all576_covariance_products": 576,
        "source_deletion_tested": True,
        "inverse_tested": True,
        "host_inverse_used_in_update": False,
        "host_eigendecomposition_used_only_after_freeze_as_comparator": True,
        "update_steps_called_physical_time": False,
        "finite_volume_momentum_supplied_by_host": True,
        "literal_M2_filter_accumulator_and_program_layout_compiled": False,
        "full_raw_source_equation_closed": False,
        "residual": "the unprojected raw deficit source has a nonzero component in the fifth, nonmetric edge zero branch; the filter returns only a range response",
    }


def retained_controls() -> dict:
    retained = cycle581.retained_controls(cycle581.cycle579_receipt())
    retained.update({
        "Cycle585_changes_mass_contact_seam_or_leakage_law": False,
        "Cycle460_held_kernel_anchor_consumed": False,
        "generator_called_rate": False,
        "wrapped_phase_called_energy": False,
        "phase_filter_steps_called_time": False,
        "result_called_gravity": False,
    })
    return retained


def no_go_controls() -> dict:
    families = (
        {"family": "metric-image Schur reduction", "status": "ATTEMPTED", "result": "local long-wave scalar approximant derived; raw source cancels its pole"},
        {"family": "finite-range relaxation with reversible tape", "status": "ATTEMPTED", "result": "held finite-volume solves with rigorous error; M2 arithmetic open"},
        {"family": "unitary Cesaro phase filter", "status": "ATTEMPTED", "result": "range pseudoinverse approximated; raw source has extra-zero component"},
        {"family": "Cycle216 six-mode scalar resolvent", "status": "RULED OUT BY PRIOR ONLY AS A DERIVATION FROM REGGE", "result": "exact 3/L for its supplied operator, but not a reduction of the Cycle576 law"},
        {"family": "local constrained edge/metric gauge code", "status": "OPEN / NOT COUNTED", "result": "could remove the fifth edge zero before response"},
        {"family": "multigrid/domain-decomposition compiler", "status": "OPEN / NOT COUNTED", "result": "could improve solver resource scaling"},
        {"family": "block encoding and QSP inverse", "status": "OPEN / NOT COUNTED", "result": "could improve the phase filter and null control"},
    )
    walls = (
        ("W_constraint", "locally enforce the metric-image/nonmetric-zero constraint"),
        ("W_source", "derive a source whose reduced symbol does not cancel the scalar pole"),
        ("W_surface", "explain or change the 4/3 cubic-correction mismatch without fitting"),
        ("W_solver", "compile signed finite-precision solver arithmetic into physical M2"),
        ("W_filter", "compile coherent phase accumulation and exact range handling into M2"),
    )
    pairwise = []
    for left, right in combinations(walls, 2):
        pairwise.append({
            "pair": (left[0], right[0]),
            "close_first_implies_second": False,
            "close_second_implies_first": False,
            "independent": True,
        })
    return {
        "fresh_skill_source": "origin/main:docs/ai_methodology/skills/no-go-discipline/SKILL.md",
        "N1_approach_families": families,
        "N1_qualifying_ATTEMPTED_or_RULED_OUT_count": 3,
        "N1_required_count": 5,
        "N1_pass": False,
        "N1_failure": "fewer than five qualifying normalized families; constrained-code, multigrid, and QSP routes remain open",
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pairwise,
        "N3_hidden_condition_scan": (
            "action orientation, metric map, frame average, gauge penalty, -2 normalization, train momenta, finite volumes, solver tolerance, phase repetitions and filter length are explicit",
            "Cycle460 is explicitly recon-only and not load-bearing",
        ),
        "N4_residual_matching": (
            {"witness": "Cycle576", "witness_residual": "raw Regge law and downstream static scalar open", "current_residual": "actual raw-law static reduction", "match": True},
            {"witness": "Cycle216/420", "witness_residual": "supplied scalar K and unconstructed physical solver", "current_residual": "comparison surface/solver only", "match": False},
            {"witness": "Cycle460", "witness_residual": "compile supplied finite receiver kernel", "current_residual": "derive homogeneous Regge response", "match": False},
            {"witness": "Cycle581", "witness_residual": "finite symmetric raw-Regge update", "current_residual": "phase-filter response from that update", "match": True},
        ),
        "N5_rhetoric_audit": (
            {"statement": "raw source has no inverse-L pole", "tested": "gauge-invariant h44 metric-image reduction at k4=0, train/held directions", "untested": "other observables, nonlinear sectors, alternative sources", "scope": "only this reduction/source"},
            {"statement": "exact reference surface does not match", "tested": "quartic long-wave coefficient of this normalized scalar Schur operator", "untested": "other constraint reductions and source observables", "scope": "only Route A construction"},
            {"statement": "phase filter does not solve the full raw equation", "tested": "three finite fibers and all24 sectors", "untested": "constrained source preparation/QSP", "scope": "only this filter and unprojected source"},
        ),
        "N6_partial_closure_paths": (
            "derive and locally enforce the metric-image constraint, then rerun the exact Schur operator",
            "couple an independently derived scalar source to h44 rather than to the curvature/deficit row",
            "compile K_app relaxation or a block-encoded inverse with explicit precision and M2 registers",
        ),
        "N6_primitive_registry_check": "fresh origin/main primitive check read; no no-retained-primitive or new-axiom claim is made",
        "N7_hostile_steelman": {
            "mechanism": "A local constrained edge code could remove the fifth zero branch, while a matter-derived h44 source would expose the already-derived K_R pole; a QSP inverse could then produce the response without the Cesaro overhead.",
            "strongest_authority": "Route A's positive scalar Schur pole plus Route B's positive local quartic approximant",
            "terminal_obligation": "derive the constraint and source from the physical code, compile them in M2, and reproduce held response/covariance without normalization",
            "disposition": "actionable; any broad negative is premature",
        },
        "N8_cross_cycle_echo": (
            "Cycle576 retired a momentum-normalized source by returning to the raw local deficit law",
            "Cycles579/581 converted a generator-only wall into explicit finite product programs",
            "Cycle495 supplied several solver approximants without a physical arithmetic compiler",
            "the same constructive narrowing mechanisms remain applicable here",
        ),
        "gate_status": "FAIL",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "demoted_artifact_status": "POSITIVE_PARTIAL_CONSTRUCTION_WITH_EXPLICIT_RESIDUALS",
        "negative_claims_shipped": False,
        "shared_obstruction_established": False,
        "shared_obstruction_claim": "DO NOT SHIP",
        "minimum_content_claim": "FAIL / DO NOT SHIP",
        "axiom_pressure_established": False,
        "axiom_pressure_claim": "DO NOT SHIP",
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle576 actual 15-edge Regge Hessian, raw deficit row, action orientation/scale/coupling, metric map and co-present 24 sectors",
            "Cycle581 update angle, generalized symmetric factor law, eight repetitions and finite filter schedule",
            "zero fourth momentum, h44 scalar choice, train/held momenta and periodic volumes",
            "zero-mean source fixtures, solver tolerance, full reversible tape and terminal readout",
        ),
        "derived": (
            "gauge-invariant h44 Schur operator and raw-source reduction",
            "two cubic quartic coefficients and the resulting Green correction ratio",
            "19-point finite-range positive approximant and rigorous finite-volume Richardson error law",
            "in-state Cesaro range-response filter of the symmetric actual-Regge update",
            "raw source overlap with the fifth nonmetric edge zero branch",
        ),
        "open": (
            "locally enforced metric-image constraint and arbitrary-size physical edge/metric code",
            "physical source law that exposes rather than cancels the scalar pole",
            "reconciliation of the 4/3 cubic-correction mismatch with the graph-Laplacian surface",
            "literal M2 signed arithmetic, precision, solver/filter accumulator, program and off-domain law",
            "nonlinear source/backreaction, empirical calibration, physical gravity or Newtonian identification",
        ),
    }


def main() -> int:
    started = perf_counter()
    dependencies = dependency_controls()
    note = note_contract()
    route_a = route_a_static_reduction()
    route_b = route_b_local_solver(route_a)
    route_c = route_c_phase_filter()
    retained = retained_controls()
    no_go = no_go_controls()

    check("exact-pinned Cycle576/Cycle581/Green dependencies and recon-only boundaries", dependencies["pass"], dependencies)
    check("note contract states construction, comparison, physical-name and N1-N8 boundaries", note["pass"], note)
    check(
        "Route A has exactly four metric gauge nulls, a gauge-invariant h44 scalar and all24 covariance",
        route_a["gauge_null_modes"] == 4
        and route_a["maximum_metric_null_residual"] < TOL
        and route_a["maximum_metric_source_Ward_residual"] < TOL
        and route_a["maximum_h44_gauge_overlap"] < 1.0e-8
        and route_a["maximum_all24_scalar_covariance_residual"] < TOL,
        {key: route_a[key] for key in (
            "gauge_null_modes", "maximum_metric_null_residual", "maximum_metric_source_Ward_residual",
            "maximum_h44_gauge_overlap", "maximum_all24_scalar_covariance_residual",
        )},
    )
    check(
        "Route A h44 Schur operator, reduced raw source and response are invariant under positive null-space penalty",
        route_a["gauge_penalty_invariance"]["maximum_normalized_operator_change"] < 1.0e-11
        and route_a["gauge_penalty_invariance"]["maximum_normalized_source_change"] < 1.0e-11
        and route_a["gauge_penalty_invariance"]["maximum_scalar_response_change"] < 1.0e-10
        and not route_a["gauge_penalty_invariance"]["penalty_selected_from_held_data"],
        route_a["gauge_penalty_invariance"],
    )
    check(
        "Route A train-only derivatives freeze the Regge scalar quartic coefficients near -1/12 and +1/18",
        abs(route_a["frozen_sum_k_i4_coefficient"] + 1 / 12) < 2.0e-5
        and abs(route_a["frozen_sum_cross_k_i2_k_j2_coefficient"] - 1 / 18) < 2.0e-5,
        {key: route_a[key] for key in (
            "frozen_sum_k_i4_coefficient", "frozen_sum_cross_k_i2_k_j2_coefficient",
            "train_axis_directional_quartic", "train_face_directional_quartic",
        )},
    )
    check(
        "Route A frozen quartic law predicts all held momenta without refit",
        all(row["parameters_refit"] == 0 and row["residual_over_abs_k_to_six"] < 0.08 for row in route_a["held_quartic_rows"]),
        route_a["held_quartic_rows"],
    )
    check(
        "Route A scalar operator has the same leading pole but a frozen 4/3 cubic correction, not the reference 5/(32pi)",
        abs(route_a["frozen_cubic_correction_ratio_to_graph"] - 4 / 3) < 3.0e-4
        and abs(route_a["frozen_Regge_scalar_Green_correction"] - 5 / (24 * math.pi)) < 2.0e-5
        and not route_a["exact_reference_surface_match"],
        {key: route_a[key] for key in (
            "frozen_cubic_correction_ratio_to_graph", "reference_graph_Green_correction",
            "frozen_Regge_scalar_Green_correction", "exact_reference_surface_match",
        )},
    )
    check(
        "Route A actual raw deficit reduction is a bounded contact response rather than a 1/L pole",
        all(abs(row["scalar_response"][0] - 2.0) < 2.0e-4 for row in route_a["raw_source_contact_rows"])
        and route_a["raw_source_contact_rows"][1]["response_times_graph_symbol"]
        < 0.35 * route_a["raw_source_contact_rows"][0]["response_times_graph_symbol"],
        route_a["raw_source_contact_rows"],
    )
    check(
        "Route A exposes the fifth edge zero and nonzero unprojected raw-source overlap on train and held fixtures",
        all(row["edge_zero_modes"] == 5 and row["extra_edge_zero_modes"] == 1
                and row["raw_source_null_projection_fraction"] > 0.1
                and not row["raw_edge_static_equation_solvable_without_projection"]
                for row in route_a["edge_zero_mode_rows"]),
        route_a["edge_zero_mode_rows"],
    )
    check(
        "Route B is a positive semidefinite 19-point proper-cubic frozen approximant",
        route_b["stencil_points"] == 19
        and route_b["positive_semidefinite_on_every_periodic_volume"]
        and route_b["proper_cubic_covariance_maximum_residual"] < TOL
        and not route_b["Cycle460_kernel_or_receiver_anchor_consumed"],
        {key: route_b[key] for key in (
            "beta_frozen_from_Route_A_train_only", "stencil_points",
            "proper_cubic_covariance_maximum_residual", "Cycle460_kernel_or_receiver_anchor_consumed",
        )},
    )
    check(
        "Route B reversible-tape Richardson law meets its rigorous train/held error and deletion controls",
        all(row["source_zero_mean_residual"] < TOL
                and row["observed_relative_solution_error"] <= 1.05 * row["rigorous_relative_solution_error_bound"]
                and row["relative_equation_residual"] < 2.0e-8
                and row["reverse_tape_consistency_residual"] < TOL
                and row["reverse_restoration_residual"] < TOL
                and row["source_deletion_output_norm"] < TOL
                and row["parameters_refit"] == 0
                for row in route_b["fixtures"]),
        route_b["fixtures"],
    )
    check(
        "Route B keeps exact-Regge and literal physical-M2 compiler boundaries open",
        route_b["local_reversible_declared_approximant_constructed"]
        and not route_b["literal_physical_M2_real_arithmetic_compiled"]
        and not route_b["exact_Regge_Schur_operator_solved"],
        {key: route_b[key] for key in (
            "local_reversible_declared_approximant_constructed",
            "literal_physical_M2_real_arithmetic_compiled", "exact_Regge_Schur_operator_solved",
        )},
    )
    check(
        "Route C is unitary/inverse/source-deletion controlled with all24/all576 covariance",
        all(row["maximum_unitarity_residual"] < TOL
                and row["inverse_filter_oddness_residual"] < TOL
                and row["source_deletion_output_norm"] < TOL
                and row["all576_sector_products"] == 576
                and row["all576_sector_product_momentum_residual"] < TOL
                for row in route_c["fixtures"]),
        route_c["fixtures"],
    )
    check(
        "Route C approximates only the range pseudoinverse on train/held with no host inverse in the update",
        all(row["relative_range_pseudoinverse_response_residual"] < 0.05
                and row["relative_range_equation_residual"] < 0.02
                and row["minimum_raw_source_null_fraction"] > 0.1
                and row["parameters_refit"] == 0
                for row in route_c["fixtures"])
        and not route_c["host_inverse_used_in_update"]
        and not route_c["full_raw_source_equation_closed"],
        route_c["fixtures"],
    )
    check(
        "Cycle230 mass/contact/seam/leakage and raw-source shore remain exact-pinned",
        retained["Cycle572_EG_residual"] == 0
        and retained["one_particle_mass_residual"] < TOL
        and retained["actual_Cycle230_contact_factorization_residual"] < TOL
        and retained["Cycle230_seam_braid_residual"] < TOL
        and retained["target_code_leakage"] < TOL
        and retained["raw_unnormalized_deficit_preserved"]
        and not retained["Cycle585_changes_mass_contact_seam_or_leakage_law"],
        retained,
    )
    check(
        "N1-N8 blocks broad negative, minimum-content, shared-obstruction and axiom-pressure claims",
        no_go["gate_status"] == "FAIL"
        and not no_go["N1_pass"]
        and no_go["N1_qualifying_ATTEMPTED_or_RULED_OUT_count"] < no_go["N1_required_count"]
        and not no_go["negative_claims_shipped"]
        and not no_go["shared_obstruction_established"]
        and not no_go["axiom_pressure_established"],
        no_go,
    )

    elapsed = perf_counter() - started
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "passes": PASS,
        "failures": FAIL,
        "dependencies": dependencies,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "retained_controls": retained,
        "inventory": inventory(),
        "no_go": no_go,
        "terminal": {
            "strongest_constructive_result": "gauge-invariant Regge h44 Schur operator plus a frozen 19-point local solver approximant",
            "reference_cubic_Green_surface_reproduced_exactly": route_a["exact_reference_surface_match"],
            "actual_raw_deficit_source_exposes_scalar_Green_pole": route_a["raw_source_has_inverse_L_pole"],
            "full_physical_M2_static_compiler": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
            "optimal_next_campaign": "derive a locally enforced metric-image constraint and an independent physical scalar source, then compile a block-encoded inverse of the exact constrained operator",
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 ** 2),
        },
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=lambda value: list(value) if isinstance(value, tuple) else value))
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("RESULT REGGE_STATIC_SCALAR_POSITIVE_PARTIAL_WITH_QUARTIC_AND_RAW_SOURCE_RESIDUALS")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
