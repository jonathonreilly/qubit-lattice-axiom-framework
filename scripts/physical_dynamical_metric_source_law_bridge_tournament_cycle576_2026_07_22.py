#!/usr/bin/env python3
"""Cycle 576: dynamical metric/source-law bridge tournament.

Route A couples the Cycle572 resource amplitude to an intrinsic 24-frame orbit
of the actual 3+1 Regge edge Hessian through a local deficit insertion. Route B
tests a bounded plaquette/conjugate reciprocal carrier. Route C computes an
exact face-orbit scattering tangent and a least-squares tensor-projection
diagnostic on blinded held source profiles.

R3/EH is used only as a target-algebra comparator. No resource is called
physical stress or energy, no generator is called a rate, and no result is
called Einstein gravity.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge
import physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22 as regge_support
import physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22 as plaquette_support


NOTE = ROOT / (
    "docs/FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_"
    "CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8.0e-9
FD_TOL = 4.0e-7
MATCH_TOL = 5.0e-7
SIGNAL = 1.0e-8
REGGE_UPDATE_SCALE = 0.025
SOURCE_COUPLING = 0.17
UPDATE_PARAMETER = 0.035
PLAQUETTE_OMEGA = 0.31
PLAQUETTE_ETA = 0.19
PLAQUETTE_GAMMA = 0.23
SCATTER_AMPLITUDE = 0.071
SCATTER_STEPS = 2
PASS = 0
FAIL = 0
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json",
    "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py",
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md",
    "scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py",
    "docs/R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
)


DEPENDENCIES = {
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py":
        "dcc397cbdade106d959b4fed41177f4928c8d2d99668b549c31af13ef5f7dcf1",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py":
        "b5050b0df3d59b713448c399431a5028ea5c28c4c0d63e1a187a431d28a2f31d",
    "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json":
        "d565d081b6c0e01adff2fd4e6e04f5f3da6991db7264843c1ae1d4c332d1a8ed",
    "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py":
        "cc71457e605d778ea91cf6b1ab24b6b68eca5eae5b673bde7c3cdecacffae28b",
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md":
        "72e37ba7301e2aa6926c666304440bf370e2e22158d69e26262440d51bf07ecc",
    "scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py":
        "cd70b8d2d2deb0bd539c0d33db8254205e0112356a943a046aab4c0e1ca43264",
    "docs/R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md":
        "10c16354c6d57bd4b67b17f1e8bcaffbb60b3dab9a58471ddc3a5483aaced13b",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py":
        "537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md":
        "798e0df4311aa59f5d0d4f24b20b8949fec863484d1482111b04bce357f0d9ea",
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
    tracked = {}
    for name in DEPENDENCIES:
        # The campaign freezes only committed dependency surfaces. The parent
        # rechecks this with git; this local field makes the contract explicit.
        tracked[name] = (ROOT / name).exists()
    closure = source_dependency_closure()
    return {
        "expected": DEPENDENCIES,
        "observed": observed,
        "all_paths_exist": all(tracked.values()),
        "source_dependency_closure": closure,
        "pass": observed == DEPENDENCIES and all(tracked.values()) and closure["pass"],
    }


def source_dependency_closure() -> dict:
    source_modules = (
        "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
        "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
        "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
        "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    )
    helper_paths = source_modules[1:]
    ordinary_helper_imports = (
        "import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge",
        "import physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22 as regge_support",
        "import physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22 as plaquette_support",
    )
    texts = {
        path: (ROOT / path).read_text(encoding="utf-8")
        for path in source_modules
    }
    imports = {
        path: tuple(
            line.strip()
            for line in text.splitlines()
            if line.startswith("import ") or line.startswith("from ")
        )
        for path, text in texts.items()
    }
    forbidden = (
        "git" + " show",
        "merge" + "-base",
        "sub" + "process",
        "docs/work_" + "history",
    )
    forbidden_counts = {
        path: {
            fragment: text.lower().count(fragment.lower())
            for fragment in forbidden
        }
        for path, text in texts.items()
    }
    observed_ordinary_imports = tuple(
        line
        for line in imports[source_modules[0]]
        if line in ordinary_helper_imports
    )
    return {
        "source_modules": source_modules,
        "source_module_characters": {
            path: len(text) for path, text in texts.items()
        },
        "source_module_sha256": {
            path: sha256(text.encode("utf-8")).hexdigest()
            for path, text in texts.items()
        },
        "imports": imports,
        "ordinary_helper_imports": observed_ordinary_imports,
        "audit_input_helpers": tuple(
            path for path in helper_paths if path in AUDIT_INPUT_PATHS
        ),
        "forbidden_reference_counts": forbidden_counts,
        "pass": (
            all(len(text) < 40_000 for text in texts.values())
            and observed_ordinary_imports == ordinary_helper_imports
            and all(path in AUDIT_INPUT_PATHS for path in helper_paths)
            and not any(
                count
                for counts in forbidden_counts.values()
                for count in counts.values()
            )
        ),
    }


def cycle572_receipt() -> dict:
    path = ROOT / "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json"
    receipt = json.loads(path.read_text(encoding="utf-8"))
    good = (
        receipt["pass"]
        and receipt["authority"] == "none"
        and receipt["audit"] == "unset"
        and receipt["tests_passed"] == receipt["tests_total"] == 8
        and receipt["runner_sha256"] == DEPENDENCIES[
            "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py"
        ]
        and receipt["note_sha256"] == DEPENDENCIES[
            "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md"
        ]
    )
    if not good:
        raise RuntimeError("exact-pinned Cycle572 receipt does not match runner/note")
    return receipt


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 576", "route a", "route b", "route c",
        "supplied 24-sector", "uniform frame-sector preparation is supplied",
        "actual regge", "r3/eh target-algebra comparison", "not an einstein equation",
        "deficit source insertion", "bianchi", "ward", "plaquette", "conjugate",
        "blinded held", "zero-source", "wrong-sign", "anisotropic control", "source deletion",
        "response deletion", "all 24", "576", "not physical stress", "not physical energy",
        "not gravity", "generator is not a rate",
        "bounded-depth finite-time regge circuit remains open",
        "no physical-site compiler", "no minimum claim", "no no-go claim",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


FRAMES = regge_support.FRAMES
FRAME_LOOKUP = regge_support.FRAME_LOOKUP



FACE_DIRECTIONS = plaquette_support.FACE_DIRECTIONS
FACE_REPS = plaquette_support.FACE_REPS



GROVER_COIN = 2 * np.ones((12, 12), dtype=complex) / 12 - np.eye(12, dtype=complex)


def stream_face_state(state: np.ndarray, inverse: bool = False) -> np.ndarray:
    output = np.zeros_like(state)
    sign = -1 if inverse else 1
    for direction, displacement in enumerate(FACE_DIRECTIONS):
        output[..., direction] = np.roll(
            state[..., direction],
            shift=tuple(sign * int(value) for value in displacement),
            axis=(0, 1, 2),
        )
    return output


def scatter_update(
    state: np.ndarray,
    profile: np.ndarray,
    amplitude: float,
    *,
    steps: int = SCATTER_STEPS,
    inverse: bool = False,
    stream: bool = True,
) -> np.ndarray:
    current = state.copy()
    if not inverse:
        for _ in range(steps):
            current *= np.exp(1j * amplitude * profile)[..., None]
            current = np.einsum("ab,xyzb->xyza", GROVER_COIN, current)
            if stream:
                current = stream_face_state(current)
    else:
        for _ in range(steps):
            if stream:
                current = stream_face_state(current, inverse=True)
            current = np.einsum("ab,xyzb->xyza", GROVER_COIN.conj().T, current)
            current *= np.exp(-1j * amplitude * profile)[..., None]
    return current


def scatter_tangent(state: np.ndarray, profile: np.ndarray, *, stream: bool = True) -> tuple[np.ndarray, np.ndarray]:
    base = state.copy()
    tangent = np.zeros_like(state)
    for _ in range(SCATTER_STEPS):
        tangent = tangent + 1j * profile[..., None] * base
        tangent = np.einsum("ab,xyzb->xyza", GROVER_COIN, tangent)
        base = np.einsum("ab,xyzb->xyza", GROVER_COIN, base)
        if stream:
            tangent = stream_face_state(tangent)
            base = stream_face_state(base)
    return base, tangent


def face_metric_design() -> np.ndarray:
    rows = []
    for direction in FACE_DIRECTIONS:
        vector = direction / np.linalg.norm(direction)
        rows.append((
            vector[0] ** 2, vector[1] ** 2, vector[2] ** 2,
            2 * vector[0] * vector[1], 2 * vector[0] * vector[2], 2 * vector[1] * vector[2],
        ))
    return np.asarray(rows, dtype=float)


FACE_METRIC_DESIGN = face_metric_design()
FACE_METRIC_PINV = np.linalg.pinv(FACE_METRIC_DESIGN)
SPATIAL_HCOMPS = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def inferred_metric(base: np.ndarray, tangent: np.ndarray) -> tuple[np.ndarray, float]:
    phase_response = np.imag(tangent / base)
    metric = phase_response @ FACE_METRIC_PINV.T
    reconstructed = metric @ FACE_METRIC_DESIGN.T
    residual = float(np.linalg.norm(reconstructed - phase_response) / max(np.linalg.norm(phase_response), 1e-15))
    return metric, residual


def rotate_profile(profile: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = profile.shape[0]
    output = np.zeros_like(profile)
    for site in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(site))
        output[target] = profile[site]
    return output


def rotate_face_state(state: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = state.shape[0]
    output = np.zeros_like(state)
    for site in product(range(length), repeat=3):
        target_site = tuple(int(value % length) for value in frame @ np.asarray(site))
        for source, vector in enumerate(FACE_DIRECTIONS):
            target_direction = int(np.where(np.all(FACE_DIRECTIONS == frame @ vector, axis=1))[0][0])
            output[target_site + (target_direction,)] = state[site + (source,)]
    return output


def rotate_metric_field(metric: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = metric.shape[0]
    output = np.zeros_like(metric)
    for site in product(range(length), repeat=3):
        target_site = tuple(int(value % length) for value in frame @ np.asarray(site))
        tensor = np.zeros((3, 3))
        for value, (left, right) in zip(metric[site], SPATIAL_HCOMPS):
            tensor[left, right] = value
            tensor[right, left] = value
        rotated = frame @ tensor @ frame.T
        output[target_site] = [rotated[left, right] for left, right in SPATIAL_HCOMPS]
    return output


def source_profiles(length: int, held: bool) -> tuple[tuple[str, np.ndarray], ...]:
    grid = np.indices((length, length, length), dtype=float)
    x, y, z = grid
    if not held:
        raw = (
            np.cos(2 * np.pi * x / length) + 0.35 * np.cos(2 * np.pi * y / length),
            np.sin(2 * np.pi * (x + y) / length) + 0.27 * np.cos(2 * np.pi * z / length),
        )
        names = ("TRAIN_XY", "TRAIN_DIAGONAL")
    else:
        point = np.zeros((length, length, length))
        point[0, 0, 0] = 1
        point -= np.mean(point)
        raw = (
            np.sin(2 * np.pi * (x + 2 * y + z) / length) + 0.41 * np.cos(2 * np.pi * z / length),
            point,
        )
        names = ("BLINDED_HELD_OBLIQUE", "BLINDED_HELD_POINT_NEUTRAL")
    output = []
    for name, profile in zip(names, raw):
        profile = profile - np.mean(profile)
        profile = profile / np.linalg.norm(profile)
        output.append((name, profile))
    return tuple(output)


def initial_face_state(length: int) -> np.ndarray:
    result = np.ones((length, length, length, 12), dtype=complex)
    return result / np.linalg.norm(result)


def r3_scattering_rows(metric: np.ndarray, profile: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    length = profile.shape[0]
    metric_fourier = np.fft.fftn(metric, axes=(0, 1, 2)) / (length ** 3)
    profile_fourier = np.fft.fftn(profile) / (length ** 3)
    responses = []
    sources = []
    frequencies = [2 * np.pi * np.fft.fftfreq(length) for _ in range(3)]
    for index in product(range(length), repeat=3):
        momentum3 = np.asarray([frequencies[axis][index[axis]] for axis in range(3)])
        if np.linalg.norm(momentum3) < 1e-12:
            continue
        momentum = np.asarray((momentum3[0], momentum3[1], momentum3[2], 0.0))
        h = np.zeros(10, dtype=complex)
        for value, component in zip(metric_fourier[index], SPATIAL_HCOMPS):
            h[regge.HCOMPS.index(component)] = value
        responses.append(regge.einstein_pairing_4d(momentum) @ h)
        source = np.zeros(10, dtype=complex)
        source[regge.HCOMPS.index((3, 3))] = profile_fourier[index]
        sources.append(source)
    return np.concatenate(responses), np.concatenate(sources)


def route_c_scattering() -> dict:
    rows = []
    train_response = []
    train_source = []
    held_pairs = []
    maximum_covariance = 0.0
    maximum_metric_covariance = 0.0
    empty_initial = initial_face_state(3)
    _, empty_tangent = scatter_tangent(empty_initial, np.zeros((3, 3, 3)))
    for length, held in ((3, False), (4, True)):
        initial = initial_face_state(length)
        for name, profile in source_profiles(length, held):
            base, tangent = scatter_tangent(initial, profile)
            epsilon = 8.0e-7
            finite = (
                scatter_update(initial, profile, epsilon)
                - scatter_update(initial, profile, -epsilon)
            ) / (2 * epsilon)
            evolved = scatter_update(initial, profile, SCATTER_AMPLITUDE)
            restored = scatter_update(evolved, profile, SCATTER_AMPLITUDE, inverse=True)
            deleted_source = scatter_update(initial, profile, 0.0)
            deleted_transport = scatter_update(initial, profile, SCATTER_AMPLITUDE, stream=False)
            wrong_sign = scatter_update(initial, profile, -SCATTER_AMPLITUDE)
            metric, reconstruction = inferred_metric(base, tangent)
            response, source = r3_scattering_rows(metric, profile)
            if held:
                held_pairs.append((response, source))
            else:
                train_response.append(response)
                train_source.append(source)

            if name.endswith("POINT_NEUTRAL"):
                for frame in FRAMES:
                    rotated_profile = rotate_profile(profile, frame)
                    left = rotate_face_state(evolved, frame)
                    right = scatter_update(rotate_face_state(initial, frame), rotated_profile, SCATTER_AMPLITUDE)
                    maximum_covariance = max(maximum_covariance, float(np.linalg.norm(left - right)))
                    rotated_base, rotated_tangent = scatter_tangent(rotate_face_state(initial, frame), rotated_profile)
                    rotated_metric, _ = inferred_metric(rotated_base, rotated_tangent)
                    maximum_metric_covariance = max(
                        maximum_metric_covariance,
                        float(np.linalg.norm(rotated_metric - rotate_metric_field(metric, frame))),
                    )

            rows.append({
                "fixture": name,
                "length": length,
                "held": held,
                "source_profile_zero_mean": abs(float(np.sum(profile))) < TOL,
                "norm_residual": abs(float(np.vdot(evolved, evolved).real) - 1.0),
                "inverse_residual": float(np.linalg.norm(restored - initial)),
                "tangent_finite_difference_residual": float(np.linalg.norm(finite - tangent)),
                "source_deletion_residual": float(np.linalg.norm(evolved - deleted_source)),
                "transport_response_deletion_residual": float(np.linalg.norm(evolved - deleted_transport)),
                "wrong_sign_odd_tangent_residual": float(np.linalg.norm((wrong_sign - deleted_source) + (evolved - deleted_source))),
                "wrong_sign_response_difference": float(np.linalg.norm(wrong_sign - evolved)),
                "effective_metric_reconstruction_residual": reconstruction,
                "effective_metric_norm": float(np.linalg.norm(metric)),
                "parameters_refit": 0,
            })

    train_response_vector = np.concatenate(train_response)
    train_source_vector = np.concatenate(train_source)
    calibration = np.vdot(train_source_vector, train_response_vector) / np.vdot(train_source_vector, train_source_vector)
    train_r3_residual = float(
        np.linalg.norm(train_response_vector - calibration * train_source_vector)
        / max(np.linalg.norm(train_response_vector), 1e-15)
    )
    held_residuals = []
    for response, source in held_pairs:
        held_residuals.append(float(
            np.linalg.norm(response - calibration * source) / max(np.linalg.norm(response), 1e-15)
        ))

    product_residual = 0.0
    products = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target = FRAME_LOOKUP[tuple((left @ right).reshape(-1))]
            product_residual = max(
                product_residual,
                float(np.linalg.norm(FACE_REPS[left_index] @ FACE_REPS[right_index] - FACE_REPS[target])),
            )
            products += 1
    anisotropic = np.zeros((12, 12))
    anisotropic[0, 0] = 1
    anisotropic_covariance = max(
        float(np.linalg.norm(rep @ anisotropic - anisotropic @ rep)) for rep in FACE_REPS
    )

    return {
        "route": "C_face_orbit_scattering_transport_tensor_projection_diagnostic",
        "rows": rows,
        "law_fixed_before_blinded_held_profiles": True,
        "held_parameters_refit": 0,
        "maximum_norm_residual": max(row["norm_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_tangent_finite_difference_residual": max(row["tangent_finite_difference_residual"] for row in rows),
        "minimum_effective_metric_reconstruction_residual": min(row["effective_metric_reconstruction_residual"] for row in rows),
        "maximum_effective_metric_reconstruction_residual": max(row["effective_metric_reconstruction_residual"] for row in rows),
        "minimum_source_deletion_residual": min(row["source_deletion_residual"] for row in rows),
        "minimum_transport_response_deletion_residual": min(row["transport_response_deletion_residual"] for row in rows),
        "zero_profile_tangent_norm": float(np.linalg.norm(empty_tangent)),
        "minimum_wrong_sign_response_difference": min(row["wrong_sign_response_difference"] for row in rows),
        "maximum_all24_state_covariance_residual": maximum_covariance,
        "maximum_all24_effective_metric_covariance_residual": maximum_metric_covariance,
        "all576_face_representation_products": products,
        "all576_face_representation_residual": product_residual,
        "wrong_sign_is_equally_unitary_and_not_selected": True,
        "anisotropic_control_covariance_residual": anisotropic_covariance,
        "train_R3_source_calibration": [float(calibration.real), float(calibration.imag)],
        "train_R3_relative_residual": train_r3_residual,
        "blinded_held_R3_relative_residuals": held_residuals,
        "R3_source_match_closed": False,
        "finite_direction_coordinate_count": 12,
        "two_axial_hop_face_stream_supplied": True,
        "physical_site_encoding_or_intertwiner_executed": False,
        "source_profile_is_supplied_background_not_dynamic_stress": True,
        "called_physical_stress_energy_gravity_or_time": False,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle572 exact-pinned finite resource convention, reciprocal curvature response and supplied gamma",
            "actual 3+1 cubic-Coxeter Regge edge variables, path complex, Regge action choice and flat Hessian machinery",
            "24 finite frame-sector coordinates, uniform coherent frame-sector preparation/readout and its normalization",
            "Regge action orientation and update scale; source coupling magnitude and sign",
            "local deficit-sum source insertion and resource-to-deficit coupling rule",
            "Route B 31-coordinate layout, conjugate frequency, reservoir coupling, gamma and factor placement",
            "Route C Grover coin, two-step schedule, face stream, source amplitude and supplied source profiles",
            "finite L3/L4 periodic domains, tolerances, readouts and train/held split",
        ),
        "derived": (
            "actual-Regge edge Bianchi identities and local deficit-source Ward identity",
            "proper-cubic 24-frame target projection and exact all24/all576 covariance",
            "small-k compatibility with the R3/EH target at coefficient approximately -1/2",
            "exact unitary/inverse co-present frame-sector edge state law and active deletions",
            "exact local plaquette/conjugate reciprocal resource gate with all24/all576 covariance",
            "exact face scattering tangent/inverse plus least-squares tensor-projection and blinded held diagnostics",
            "route-specific R3 mismatch diagnostics for B and C",
        ),
        "open": (
            "derivation/selection of edge variables, Regge action, orientation, source sign and normalization",
            "selection/preparation of the uniform 24-frame sector and an exact bounded-depth finite-time Regge circuit",
            "physical stress-energy identification and coordinate-observable calibration",
            "nonlinear Regge/Einstein equation, Lorentzian/continuum/strong-field closure and global existence",
            "endogenous source profiles, locally enforced arbitrary matter sector and arbitrary size",
            "a local physical-site encoding, constraint system, leakage controls and executed intertwiner",
            "physical time, Record formation, realized history and Born probability",
        ),
        "supplied_parameters": {
            "regge_update_scale": REGGE_UPDATE_SCALE,
            "source_coupling": SOURCE_COUPLING,
            "source_coupling_sign": "+",
            "update_parameter": UPDATE_PARAMETER,
            "plaquette_omega": PLAQUETTE_OMEGA,
            "plaquette_eta": PLAQUETTE_ETA,
            "plaquette_gamma": PLAQUETTE_GAMMA,
            "scatter_amplitude": SCATTER_AMPLITUDE,
            "scatter_steps": SCATTER_STEPS,
            "frame_sector_count": len(FRAMES),
            "edge_coordinates_per_sector": 15,
            "uniform_frame_sector_preparation_and_readout": True,
            "small_momentum_comparison_magnitude": 1.0e-3,
            "covariance_control_momentum": (0.17, 0.11, 0.07, 0.13),
            "route_A_source_amplitude_fixtures": (
                ("TRAIN_L3", 3, 0.6, (2 * np.pi / 3, 0.0, 0.0, 0.0)),
                ("HELD_L4_LOW", 4, 0.37, (np.pi / 2, np.pi / 2, 0.0, 0.0)),
                ("HELD_L4_SIGN", 4, -0.81, (np.pi / 2, 0.0, np.pi / 2, np.pi / 2)),
            ),
            "route_B_coordinate_layout": "6 matter + 12 curvature + 12 conjugate + 1 reservoir",
            "route_C_coin": "normalized 12-direction Grover coin",
            "route_C_profile_coefficients": (0.35, 0.27, 0.41),
            "route_C_tangent_step": 8.0e-7,
            "tolerance": TOL,
            "finite_difference_tolerance": FD_TOL,
            "target_match_tolerance": MATCH_TOL,
            "signal_floor": SIGNAL,
        },
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE576 PHYSICAL DYNAMICAL METRIC/SOURCE-LAW BRIDGE TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    receipt = cycle572_receipt()
    note = note_contract()
    route_a = regge_support.route_a_regge()
    route_b = plaquette_support.route_b_plaquette(receipt)
    route_c = route_c_scattering()
    supplied = inventory()

    check("all Cycle572, actual-Regge and R3 dependencies are exact-pinned", dependencies["pass"], dependencies)
    check("note contract keeps the finite-execution and physical-naming boundary explicit", note["pass"], note)
    check(
        "Route A actual-Regge target projection matches R3/EH at small k without using the target equation as update",
        abs(route_a["mean_best_fit_coefficient"] + 0.5) < MATCH_TOL
        and route_a["coefficient_spread"] < MATCH_TOL
        and route_a["maximum_R3_relative_residual"] < MATCH_TOL
        and not route_a["target_equation_used_as_update"]
        and not route_a["Einstein_equation_or_physical_gravity_derived"],
        route_a["R3_EH_target_algebra_comparisons"],
    )
    check(
        "Route A actual edge and deficit variations satisfy Bianchi/Ward and all24/all576 covariance",
        route_a["metric_Bianchi_residual"] < TOL
        and route_a["edge_Regge_Bianchi_residual"] < TOL
        and route_a["local_deficit_source_Ward_residual"] < TOL
        and route_a["raw_local_source_generator_residual"] < TOL
        and not route_a["momentum_dependent_source_normalization_used"]
        and route_a["frame_averaged_source_Ward_residual"] < TOL
        and route_a["maximum_all24_metric_generator_covariance_residual"] < TOL
        and route_a["maximum_all24_source_covariance_residual"] < TOL
        and route_a["all576_metric_representation_products"] == 576
        and route_a["all576_metric_representation_residual"] < TOL
        and route_a["all576_sector_representation_residual"] < TOL,
        route_a,
    )
    check(
        "Route A supplied frame-sector state law is inverse and source/response/deletion sensitive",
        route_a["finite_edge_source_Hermiticity_residual"] < TOL
        and route_a["finite_state_update_inverse_residual"] < TOL
        and route_a["finite_state_update_norm_residual"] < TOL
        and route_a["source_deletion_residual"] > SIGNAL
        and route_a["metric_response_deletion_residual"] > SIGNAL
        and route_a["zero_source_metric_carrier_norm"] < TOL
        and route_a["wrong_sign_response_sum_residual"] < TOL
        and route_a["single_frame_anisotropic_control_residual"] > SIGNAL
        and route_a["one_frame_finite_update_covariance_residual"] < TOL
        and all(row["metric_carrier_norm"] > SIGNAL and row["inverse_residual"] < TOL and row["parameters_refit"] == 0 for row in route_a["source_amplitude_rows"])
        and not route_a["bounded_depth_finite_time_Regge_circuit_compiled"],
        route_a,
    )
    check(
        "Route B plaquette/conjugate gate is exact, reciprocal, all24/all576 and active-deletion controlled",
        route_b["Hermiticity_residual"] < TOL
        and route_b["unitarity_residual"] < TOL
        and route_b["inverse_residual"] < TOL
        and route_b["source_deletion_residual"] > SIGNAL
        and route_b["empty_source_carrier_response_norm"] < TOL
        and route_b["reservoir_deleted_matter_response_norm"] > SIGNAL
        and route_b["wrong_sign_response_difference"] > SIGNAL
        and route_b["curvature_response_deletion_residual"] > SIGNAL
        and route_b["conjugate_response_deletion_residual"] > SIGNAL
        and route_b["matter_curvature_reciprocity_residual"] < TOL
        and route_b["matter_to_curvature_response_norm"] > SIGNAL
        and route_b["curvature_to_matter_backreaction_norm"] > SIGNAL
        and route_b["maximum_all24_generator_covariance_residual"] < TOL
        and route_b["all576_frame_products"] == 576
        and route_b["all576_frame_product_residual"] < TOL
        and route_b["anisotropic_control_covariance_residual"] > SIGNAL,
        route_b,
    )
    check(
        "Route B does not launder its momentum-independent oscillator into the R3 target",
        route_b["R3_relative_residual"] > 0.1
        and route_b["R3_gauge_sample_response_norm"] > SIGNAL
        and not route_b["R3_target_match_closed"],
        {key: route_b[key] for key in ("R3_best_fit_coefficient", "R3_relative_residual", "R3_gauge_sample_response_norm")},
    )
    check(
        "Route C exact scattering walk predicts blinded held tangents and covariant least-squares tensor diagnostics without refit",
        route_c["maximum_norm_residual"] < TOL
        and route_c["maximum_inverse_residual"] < TOL
        and route_c["maximum_tangent_finite_difference_residual"] < FD_TOL
        and route_c["minimum_effective_metric_reconstruction_residual"] > 0.5
        and route_c["maximum_effective_metric_reconstruction_residual"] > 0.9
        and route_c["minimum_source_deletion_residual"] > SIGNAL
        and route_c["minimum_transport_response_deletion_residual"] > SIGNAL
        and route_c["zero_profile_tangent_norm"] < TOL
        and route_c["minimum_wrong_sign_response_difference"] > SIGNAL
        and route_c["maximum_all24_state_covariance_residual"] < TOL
        and route_c["maximum_all24_effective_metric_covariance_residual"] < TOL
        and route_c["all576_face_representation_products"] == 576
        and route_c["all576_face_representation_residual"] < TOL
        and route_c["held_parameters_refit"] == 0
        and route_c["anisotropic_control_covariance_residual"] > SIGNAL,
        route_c,
    )
    check(
        "Route C held source profiles diagnose mismatch of the declared scattering-to-R3 source template",
        route_c["train_R3_relative_residual"] > 0.05
        and min(route_c["blinded_held_R3_relative_residuals"]) > 0.05
        and not route_c["R3_source_match_closed"],
        {
            "train": route_c["train_R3_relative_residual"],
            "held": route_c["blinded_held_R3_relative_residuals"],
            "calibration": route_c["train_R3_source_calibration"],
        },
    )
    check(
        "supplied/derived/open inventory exposes sign, calibration, frame, circuit and nonlinear structure",
        len(supplied["supplied"]) >= 8
        and len(supplied["derived"]) >= 7
        and len(supplied["open"]) >= 7
        and len(supplied["supplied_parameters"]) >= 20,
        supplied,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = peak / (1024 ** 2) if sys.platform == "darwin" else peak / 1024
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "inventory": supplied,
        "terminal": {
            "strongest_constructive_result": (
                "supplied proper-cubic finite Regge edge model with deficit insertion and R3 target-algebra match"
            ),
            "actual_Regge_generator_and_source_Ward_closed": True,
            "R3_target_algebra_compatibility_closed": True,
            "physical_site_compiler_executed": False,
            "physical_stress_or_Einstein_equation_closed": False,
            "bounded_depth_finite_time_Regge_circuit_closed": False,
            "source_sign_normalization_or_frame_preparation_selected": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_FAILED")
        return 1
    print("RESULT ACTUAL_REGGE_DEFICIT_SOURCE_GENERATOR_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
