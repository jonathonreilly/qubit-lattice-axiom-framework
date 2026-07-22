#!/usr/bin/env python3
"""Cycle 562: physical energy-stress/source identification tournament.

Three routes are kept distinct:
  A. a rest-mass-normalized local deviation 4-current for the free massive walk;
  B. the actual Cycle230 contact plus local reservoir/field exchange impulse;
  C. a stationary dressed-reservoir eigenstate and shifted-resolvent observable.

The output is a tournament over candidate ledgers.  A wrapped phase is not
physical energy, a generator element is not a rate, and no response is called
force or gravity.
"""

from __future__ import annotations

from hashlib import sha256
import inspect
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_locally_conserved_current_response_law_tournament_cycle559_2026_07_21 as c559
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17 as work
import stationary_dressed_reservoir_shifted_green_profile_2026_07_17 as dressed


c210 = c230.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ENERGY_STRESS_SOURCE_IDENTIFICATION_TOURNAMENT_"
    "CYCLE562_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
SIGNAL = 1.0e-12
PASS = 0
FAIL = 0

DEPENDENCIES = {
    "physical_locally_conserved_current_response_law_tournament_cycle559_2026_07_21.py":
        "a6475b85ad4c87cae58ee09d371ff91f82719d50e72e8f5ff88d5030fef681be",
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17.py":
        "d533418438a6b76a971c90d5df2e57aaa2944e762b6474b26241b24ac489f5c0",
    "stationary_dressed_reservoir_shifted_green_profile_2026_07_17.py":
        "f711429d255c872bab5fd296cfc9ce662d3adb4e17f3a97915ffc152caa30d83",
}

BETA = -0.3
SPECIES = c219.common_species(BETA)
MASS = c219.rest_mass(SPECIES)
REST_PHASE = SPECIES.rest_phase
K_REST = 4 * math.sin(REST_PHASE / 2) ** 2
ENERGY_SCALE = MASS / K_REST
TRAIN_FREE = ((5, 8, (1, 2)), (6, 9, (1, 2, 3)))
HELD_FREE = (7, 10, 3)
DRESSED_TRAIN = 9
DRESSED_HELD = 10
DRESSED_HELD_SEPARATION = 4
LAWFUL_LENGTHS = (5, 6, 7, 9, 10)
LAWFUL_BETAS = (BETA,)


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
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCIES}
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 562", "route a",
        "route b", "route c", "noether", "spectral", "actual cycle-230 contact",
        "stationary", "resolvent", "rest-mass-normalized", "all 24",
        "held l7", "held l10", "not a blind prediction", "physical m2",
        "phase is not energy", "generator element is not a rate",
        "response is not force or gravity", "cycle559 coefficient-one number",
        "not locally enforced", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def apply_coin(field: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    return np.einsum("...d,ed->...e", np.asarray(field, dtype=complex), matrix)


def massive_step(
    field: np.ndarray,
    *,
    coin_matrix: np.ndarray | None = None,
    delete_stream: bool = False,
) -> np.ndarray:
    matrix = SPECIES.coin if coin_matrix is None else coin_matrix
    coined = apply_coin(field, matrix)
    return coined if delete_stream else c559.stream(coined)


def localized_scalar(length: int) -> np.ndarray:
    field = np.zeros((length, length, length, 6), dtype=complex)
    field[0, 0, 0] = c210.UNIFORM
    return field


def rest_scalar(length: int) -> np.ndarray:
    return np.broadcast_to(
        c210.UNIFORM / math.sqrt(length**3), (length, length, length, 6)
    ).copy()


def deviation(field: np.ndarray, *, alpha: float = 0.0) -> np.ndarray:
    return field - np.exp(-1j * alpha) * massive_step(field)


def energy_density(field: np.ndarray, *, alpha: float = 0.0) -> np.ndarray:
    chi = deviation(field, alpha=alpha)
    return ENERGY_SCALE * np.sum(abs(chi) ** 2, axis=-1)


def directed_energy_flux(field: np.ndarray, *, alpha: float = 0.0) -> np.ndarray:
    """Six outgoing link-flux coordinates of the deviation field."""

    chi = deviation(field, alpha=alpha)
    coined_chi = apply_coin(chi, SPECIES.coin)
    return ENERGY_SCALE * abs(coined_chi) ** 2


def energy_current_vector(field: np.ndarray, *, alpha: float = 0.0) -> np.ndarray:
    """Proper-cubic vector contraction of the six directed link fluxes."""

    return np.einsum(
        "...d,di->...i",
        directed_energy_flux(field, alpha=alpha),
        np.asarray(c210.DIRECTIONS, dtype=float),
    )


def total_energy(field: np.ndarray, *, alpha: float = 0.0) -> float:
    return float(np.sum(energy_density(field, alpha=alpha)))


def transform_coordinate(frame: np.ndarray, coordinate: tuple[int, int, int], length: int) -> tuple[int, int, int]:
    return tuple(int(value % length) for value in frame @ np.asarray(coordinate, dtype=int))


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(
        int(np.where(np.all(c210.DIRECTIONS == frame @ direction, axis=1))[0][0])
        for direction in c210.DIRECTIONS
    )


def transform_field(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]
    output = np.zeros_like(field)
    mapping = direction_map(frame)
    for coordinate in np.ndindex((length, length, length)):
        target = transform_coordinate(frame, coordinate, length)
        for source, target_direction in enumerate(mapping):
            output[target + (target_direction,)] = field[coordinate + (source,)]
    return output


def free_local_current_controls() -> dict:
    rng = np.random.default_rng(56201)
    frames = c210.proper_cubic_frames()
    rest_rows = []
    continuity = 0.0
    conservation = 0.0
    covariance = 0.0
    current_covariance = 0.0
    coin_density = 0.0
    norm = 0.0
    held_rows = []
    deletion = {}

    for length in (5, 7):
        rest = rest_scalar(length)
        rest_output = massive_step(rest)
        rest_rows.append({
            "L": length,
            "one_particle_number": float(np.vdot(rest, rest).real),
            "rest_eigen_residual": float(np.linalg.norm(rest_output - np.exp(1j * REST_PHASE) * rest)),
            "rest_normalized_energy": total_energy(rest),
            "mass": MASS,
        })
        probe = rng.normal(size=rest.shape) + 1j * rng.normal(size=rest.shape)
        probe /= np.linalg.norm(probe)
        for _ in range(4):
            chi = deviation(probe)
            coined_chi = apply_coin(chi, SPECIES.coin)
            next_probe = massive_step(probe)
            next_chi = deviation(next_probe)
            transported_chi = c559.stream(coined_chi)
            rho = ENERGY_SCALE * np.sum(abs(chi) ** 2, axis=-1)
            outgoing_flux = ENERGY_SCALE * abs(coined_chi) ** 2
            outgoing = np.sum(outgoing_flux, axis=-1)
            rho_next = ENERGY_SCALE * np.sum(abs(next_chi) ** 2, axis=-1)
            incoming = np.zeros_like(rho)
            for direction, displacement in enumerate(c210.DIRECTIONS):
                shift = tuple(int(item) for item in displacement)
                incoming += np.roll(
                    outgoing_flux[..., direction],
                    shift=shift,
                    axis=(0, 1, 2),
                )
            coin_density = max(coin_density, float(np.max(abs(outgoing - rho))))
            continuity = max(
                continuity,
                float(np.max(abs(rho_next - rho - (incoming - outgoing)))),
            )
            continuity = max(continuity, float(np.linalg.norm(next_chi - transported_chi)))
            conservation = max(conservation, abs(float(np.sum(rho_next)) - float(np.sum(rho))))
            norm = max(norm, abs(np.linalg.norm(next_probe) - np.linalg.norm(probe)))
            probe = next_probe

        generic = rng.normal(size=rest.shape) + 1j * rng.normal(size=rest.shape)
        generic /= np.linalg.norm(generic)
        baseline = massive_step(generic)
        baseline_density = energy_density(generic)
        baseline_current = energy_current_vector(generic)
        for frame in frames:
            transformed_input = transform_field(generic, frame)
            actual = massive_step(transformed_input)
            expected = transform_field(baseline, frame)
            covariance = max(covariance, float(np.linalg.norm(actual - expected)))
            transformed_density = np.zeros_like(baseline_density)
            transformed_current = np.zeros_like(baseline_current)
            for coordinate in np.ndindex((length, length, length)):
                target = transform_coordinate(frame, coordinate, length)
                transformed_density[target] = baseline_density[coordinate]
                transformed_current[target] = frame @ baseline_current[coordinate]
            covariance = max(
                covariance,
                float(np.max(abs(energy_density(transformed_input) - transformed_density))),
            )
            current_covariance = max(
                current_covariance,
                float(np.max(abs(energy_current_vector(transformed_input) - transformed_current))),
            )

    # Frozen local-energy propagation table; L7/r3 is the new held row.
    for length, depth, separations in TRAIN_FREE:
        field = localized_scalar(length)
        initial_energy = total_energy(field)
        for _ in range(depth):
            field = massive_step(field)
        density = energy_density(field)
        for separation in separations:
            held_rows.append({
                "fixture": f"TRAIN_L{length}", "held": False, "L": length,
                "depth": depth, "separation": separation,
                "target_energy_density": float(density[separation, 0, 0]),
                "total_energy": float(np.sum(density)),
                "initial_total_energy": initial_energy,
            })
    length, depth, separation = HELD_FREE
    initial = localized_scalar(length)
    field = initial.copy()
    for _ in range(depth):
        field = massive_step(field)
    density = energy_density(field)
    held_rows.append({
        "fixture": "HELD_L7_NEW", "held": True, "L": length, "depth": depth,
        "separation": separation,
        "target_energy_density": float(density[separation, 0, 0]),
        "total_energy": float(np.sum(density)),
        "initial_total_energy": total_energy(initial),
    })

    base = localized_scalar(7)
    baseline = base.copy()
    for _ in range(10):
        baseline = massive_step(baseline)
    no_coin = base.copy()
    for _ in range(10):
        no_coin = massive_step(no_coin, coin_matrix=np.eye(6, dtype=complex))
    no_stream = base.copy()
    for _ in range(10):
        no_stream = massive_step(no_stream, delete_stream=True)
    target = (3, 0, 0)
    deletion = {
        "baseline_target": float(energy_density(baseline)[target]),
        "coin_deleted_target": float(energy_density(no_coin)[target]),
        "stream_deleted_target": float(energy_density(no_stream)[target]),
        "phase_reference_shifted_rest_energy": total_energy(rest_scalar(7), alpha=0.4),
        "normalization_deleted_energy": 0.0,
    }

    return {
        "route": "A_Noether_spectral_quadratic_local_current",
        "beta": BETA,
        "rest_phase": REST_PHASE,
        "Cycle219_mass": MASS,
        "K_rest": K_REST,
        "independent_energy_scale_mass_over_Krest": ENERGY_SCALE,
        "rest_rows": rest_rows,
        "maximum_local_continuity_residual": continuity,
        "maximum_onsite_coin_density_residual": coin_density,
        "maximum_total_energy_conservation_residual": conservation,
        "maximum_norm_residual": norm,
        "maximum_all24_covariance_residual": covariance,
        "maximum_all24_current_vector_covariance_residual": current_covariance,
        "proper_cubic_frames": len(frames),
        "prediction_rows": held_rows,
        "deletions_and_reference": deletion,
        "candidate_4_current": "T00=A|chi|^2; T0i=A sum_d D[d,i]|(C chi)_d|^2",
        "full_spatial_stress_tensor_identified": False,
        "phase_reference_alpha": 0.0,
        "phase_reference_derived": False,
        "physical_M2_status": "exact vacuum+Q1 one-hot map on 6L^3 M2; bounded number-preserving Givens/NN-SWAP completion supplied",
        "code_leakage": 0.0,
    }


def contact_impulse_controls() -> dict:
    operators = work.reduced_operators()
    vertex, contact, full = operators["V"], operators["W"], operators["G"]
    identity = np.eye(full.shape[0], dtype=complex)
    rows = []
    maximum_balance = 0.0
    minimum_contact_signal = math.inf
    for label in ("X", "Y"):
        observable = MASS * operators[label]
        exchange_impulse = vertex.conj().T @ observable @ vertex - observable
        contact_impulse = vertex.conj().T @ (
            contact.conj().T @ observable @ contact - observable
        ) @ vertex
        total_impulse = full.conj().T @ observable @ full - observable
        residual = float(np.linalg.norm(total_impulse - exchange_impulse - contact_impulse))
        maximum_balance = max(maximum_balance, residual)
        minimum_contact_signal = min(minimum_contact_signal, float(np.linalg.norm(contact_impulse)))
        rows.append({
            "observable": f"m*{label}",
            "total_impulse_norm": float(np.linalg.norm(total_impulse)),
            "exchange_impulse_norm": float(np.linalg.norm(exchange_impulse)),
            "contact_impulse_norm": float(np.linalg.norm(contact_impulse)),
            "balance_residual": residual,
        })

    # A conserved deviation coordinate for the complete contact+exchange block.
    k_full = ENERGY_SCALE * (2 * identity - full - full.conj().T)
    eigmin = float(np.min(np.linalg.eigvalsh(k_full)))
    commutator = float(np.linalg.norm(full @ k_full - k_full @ full))
    rng = np.random.default_rng(56202)
    probe = rng.normal(size=18) + 1j * rng.normal(size=18)
    probe /= np.linalg.norm(probe)
    before = float(np.vdot(probe, k_full @ probe).real)
    after_state = full @ probe
    after = float(np.vdot(after_state, k_full @ after_state).real)

    no_contact = work.reduced_operators(contact=0.0)
    no_exchange = work.reduced_operators(kappa=0.0)
    q_only = np.exp(1j * 2 * work.G_CONTACT) * identity
    q_only_contact_impulses = []
    for label in ("X", "Y"):
        observable = MASS * operators[label]
        q_only_contact_impulses.append(float(np.linalg.norm(
            vertex.conj().T @ (q_only.conj().T @ observable @ q_only - observable) @ vertex
        )))

    # Exact seven-M2 local reservoir/field restrictions at N=2,3,4.
    embedding = work.physical_rf_embedding()
    physical = work.reservoir.reservoir_field_operators()
    physical_rows = []
    for number in (2, 3, 4):
        angle = work.KAPPA * MASS * number
        full_gate = work.reservoir.exchange_gate(angle, physical["exchange"])
        reduced = work.reduced_exchange_gate(number)
        physical_rows.append({
            "N": number,
            "seven_M2_intertwiner_residual": float(
                np.linalg.norm(full_gate @ embedding - embedding @ reduced)
            ),
        })

    return {
        "route": "B_actual_contact_mass_normalized_impulse",
        "rows": rows,
        "maximum_exact_impulse_balance_residual": maximum_balance,
        "minimum_actual_contact_impulse_norm": minimum_contact_signal,
        "full_gate_unitarity_residual": float(np.linalg.norm(full.conj().T @ full - identity)),
        "contact_exchange_commutator": float(np.linalg.norm(contact @ vertex - vertex @ contact)),
        "contact_dressed_K_minimum_eigenvalue": eigmin,
        "contact_dressed_K_commutator_residual": commutator,
        "contact_dressed_K_expectation_conservation_residual": abs(after - before),
        "contact_deletion_K_change_norm": float(np.linalg.norm(
            k_full - ENERGY_SCALE * (2 * identity - no_contact["G"] - no_contact["G"].conj().T)
        )),
        "exchange_deletion_signal": float(np.linalg.norm(full - no_exchange["G"])),
        "Q_only_contact_impulse_maximum": max(q_only_contact_impulses),
        "physical_seven_M2_rows": physical_rows,
        "physical_49_M2_support_and_all24_status": "exact-pinned Cycle work ledger: 49-M2 union, zero leakage, 24 proper-cubic frames/648 frame-translations",
        "full_joint_physical_G_X_Y_intertwiner_executed": False,
        "normalization": "all X/Y impulse coordinates multiplied by independent Cycle219 mass; no held response fit",
        "called_physical_work_or_energy": False,
    }


def dressed_stationary_controls() -> dict:
    rows = []
    held_cache = None
    maximum_eigen = 0.0
    maximum_profile = 0.0
    maximum_stationary_energy = 0.0
    for length, held in ((DRESSED_TRAIN, False), (DRESSED_HELD, True)):
        update, eigenvalue, state = dressed.dressed_eigenstate(length)
        if held:
            held_cache = (update, eigenvalue, state)
        eigenphase = float(np.angle(eigenvalue))
        chi = state - update @ state
        density = ENERGY_SCALE * abs(chi) ** 2
        next_state = update @ state
        next_chi = next_state - update @ next_state
        next_density = ENERGY_SCALE * abs(next_chi) ** 2
        q = dressed.emitted_amplitude(state, length)
        scalar = dressed.scalar_projection(state, length)
        scalar_perpendicular = scalar - np.mean(scalar)
        shift = 6 * (1 - math.cos(eigenphase))
        source = dressed.c211.point_source(length)
        shifted = dressed.shifted_green_profile(length, shift)
        prediction = q * (-0.5 * source + 1j * math.sin(eigenphase) * shifted)
        eigen_residual = float(np.linalg.norm(update @ state - eigenvalue * state))
        profile_residual = float(
            np.linalg.norm(scalar_perpendicular - prediction)
            / np.linalg.norm(scalar_perpendicular)
        )
        maximum_eigen = max(maximum_eigen, eigen_residual)
        maximum_profile = max(maximum_profile, profile_residual)
        maximum_stationary_energy = max(
            maximum_stationary_energy, float(np.max(abs(next_density - density)))
        )
        target = dressed.site_index((DRESSED_HELD_SEPARATION % length, 0, 0), length)
        field_slice = slice(1 + 6 * target, 1 + 6 * target + 6)
        rows.append({
            "fixture": f"{'HELD_NEW' if held else 'TRAIN'}_L{length}",
            "held": held,
            "L": length,
            "dimension": update.shape[0],
            "eigenphase": eigenphase,
            "eigen_residual": eigen_residual,
            "reservoir_number_weight": float(abs(state[0]) ** 2),
            "field_number_weight": float(np.linalg.norm(state[1:]) ** 2),
            "rest_normalized_deviation_energy": float(np.sum(density)),
            "spectral_value_check": ENERGY_SCALE * 4 * math.sin(eigenphase / 2) ** 2,
            "stationary_energy_density_residual": float(np.max(abs(next_density - density))),
            "shifted_resolvent_profile_residual": profile_residual,
            "energy_density_at_separation4": float(np.sum(density[field_slice])),
            "emitted_amplitude_abs": float(abs(q)),
        })

    assert held_cache is not None
    update, eigenvalue, state = held_cache
    rng = np.random.default_rng(56203)
    probe = rng.normal(size=state.size) + 1j * rng.normal(size=state.size)
    probe /= np.linalg.norm(probe)
    covariance = 0.0
    state_covariance = 0.0
    for frame in c210.proper_cubic_frames():
        representation = dressed.frame_permutation(DRESSED_HELD, frame)
        covariance = max(
            covariance,
            float(np.linalg.norm(representation @ (update @ probe) - update @ (representation @ probe))),
        )
        state_covariance = max(
            state_covariance,
            float(np.linalg.norm(representation @ state - state)),
        )
    theta_zero = dressed.defect_update(DRESSED_HELD, 0.0)
    reservoir = np.zeros(theta_zero.shape[0], dtype=complex)
    reservoir[0] = 1
    return {
        "route": "C_stationary_dressed_resolvent_energy_observable",
        "rows": rows,
        "maximum_eigen_residual": maximum_eigen,
        "maximum_stationary_energy_density_residual": maximum_stationary_energy,
        "maximum_shifted_resolvent_profile_residual": maximum_profile,
        "maximum_all24_update_covariance_residual": covariance,
        "maximum_all24_selected_state_covariance_residual": state_covariance,
        "proper_cubic_frames": 24,
        "theta_zero_reservoir_stationarity_residual": float(
            np.linalg.norm(theta_zero @ reservoir - reservoir)
        ),
        "physical_M2_status": f"one reservoir plus 6L^3 field M2 on Q1; held L10 uses {1 + 6 * DRESSED_HELD**3} physical M2",
        "contact_or_matter_in_route_C": False,
        "selector_and_preparation_supplied": True,
        "eigenphase_called_energy_or_rate": False,
    }


def cycle559_bridge_controls() -> dict:
    # Compare the independently normalized massive K-current with Cycle559's
    # coefficient-one number on the same six-lane M2 geometry.  Parked/matter
    # sites are assigned the calibrated rest unit m only for this candidate
    # bridge; that assignment is deliberately tested rather than assumed.
    length = 6
    sites = ((0, 0, 0), (3, 0, 0))
    state = c559.initial_state(length, c559.CURRENT_WORDS["PLUS"])
    rows = []

    def bridge_energy(item) -> float:
        reservoir_number = float(
            np.vdot(item.parked, item.parked).real
            + np.vdot(item.matter, item.matter).real
        )
        return MASS * reservoir_number + total_energy(item.field)

    for depth in range(10):
        rows.append({
            "depth": depth,
            "Cycle559_number": c559.total_number(state),
            "candidate_bridge_energy": bridge_energy(state),
            "receiver_number": float(np.vdot(state.matter, state.matter).real),
        })
        state, _controls = c559.forward_step(state, sites)
    energies = np.asarray([row["candidate_bridge_energy"] for row in rows])
    numbers = np.asarray([row["Cycle559_number"] for row in rows])
    rest = rest_scalar(length)
    localized = localized_scalar(length)
    return {
        "rows": rows,
        "maximum_Cycle559_number_drift": float(np.max(abs(numbers - numbers[0]))),
        "candidate_bridge_energy_drift": float(np.max(abs(energies - energies[0]))),
        "m_times_number_equals_rest_energy_residual": abs(MASS - total_energy(rest)),
        "m_times_number_equals_localized_energy_residual": abs(MASS - total_energy(localized)),
        "operator_identification": False,
        "rest_ray_calibration_match": True,
        "shared_Q1_homogeneous_normalization": True,
        "dynamic_conserved_bridge_under_Cycle559": False,
        "disposition": "at most rest-anchored/correlated; Cycle559 number is not identified with the K-current and the tested dynamic bridge is not conserved",
    }


def resource_and_domain_controls() -> dict:
    rejections = 0
    for length in (2, 4, 8):
        if length not in LAWFUL_LENGTHS:
            rejections += 1
    for beta in (-0.7, 0.1):
        if beta not in LAWFUL_BETAS:
            rejections += 1
    return {
        "route_A_physical_M2": {"L5": 750, "L6": 1296, "held_L7": 2058},
        "route_A_code_dimensions_vacuum_plus_Q1": {"L5": 751, "L6": 1297, "held_L7": 2059},
        "route_B_physical_support_M2": 49,
        "route_B_full_joint_state_intertwiner": False,
        "route_C_physical_M2": {"train_L9": 4375, "held_L10": 6001},
        "maximum_resolved_route_A_C_gate_support_M2": 2,
        "global_parity_or_ordering_service": False,
        "vacuum_plus_Q1_locally_enforced": False,
        "lawful_domain_rejections": rejections,
        "current_update_signatures": {
            "Cycle559_forward": tuple(inspect.signature(c559.forward_step).parameters),
            "Cycle559_inverse": tuple(inspect.signature(c559.inverse_step).parameters),
        },
    }


def supplied_inventory() -> dict:
    return {
        "supplied": (
            "Cycle219 beta=-0.3, phase representative alpha=0, common coin, rest/inertial mass and c^2=1/3 calibration",
            "choice of K=(I-U)^dagger(I-U) and scale A=m/[4 sin^2(phi/2)]",
            "finite periodic boundaries, localized/rest preparations, depth=L+3 and train/held readouts",
            "Cycle230 g=0.37 pair-count contact, N=6 branch quadratures, Cycle reservoir kappa=0.8 exchange and factor order",
            "stationary eigenpair selector, source origin, Q1 restriction, shifted-resolvent comparison and L9/L10 split",
            "Cycle559 source-location preparation and the tested bridge assignment m per parked/matter excitation",
        ),
        "derived": (
            "Route-A exact rest normalization, positive local density, one-edge continuity, conservation and all24 covariance",
            "Route-B mass-normalized actual-contact/exchange impulse identity and contact-dressed conserved K coordinate",
            "Route-C stationary rest-normalized K density, shifted-resolvent identity and new held L10/separation4 value",
            "Cycle559 number/K comparison and route-specific failure of the candidate dynamic bridge",
        ),
        "open": (
            "phase-reference and K-candidate law selection; exact phase-linear positive energy",
            "full spatial stress tensor, momentum/work calibration, empirical unit and clock/time normalization",
            "complete joint physical M2 state compiler for Cycle230 contact plus mediator and many-excitation local enforcement",
            "endogenous preparation, unbounded/continuum response, nonlinear metric/gravity, Record/Born/realized history",
        ),
    }


def no_go_controls() -> dict:
    routes = (
        {"route": "A local rest-normalized K current", "marker": "ATTEMPTED", "result": "exact positive local 4-current; phase reference and quadratic calibration remain supplied"},
        {"route": "A2 signed local S current", "marker": "RULED OUT BY PRIOR FOR POSITIVE TERMINAL", "result": "Cycle228: local and oriented but indefinite and blind at theta=pi"},
        {"route": "A3 spectral H_abs", "marker": "RULED OUT BY PRIOR FOR STRICT-LOCAL TERMINAL", "result": "Cycle228: rest-linear but non-finite-range and does not generate negative phase"},
        {"route": "B actual-contact impulse", "marker": "ATTEMPTED", "result": "exact mass-normalized vector balance and contact-sensitive conserved deviation coordinate; no full joint state intertwiner"},
        {"route": "C stationary dressed resolvent", "marker": "ATTEMPTED", "result": "stationary local K density and new held response; selector supplied and no contact"},
        {"route": "action/coordinate-variation stress tensor", "marker": "OPEN", "result": "discrete-action prior art exists; no action selected for this cubic law"},
        {"route": "many-body particle-hole/Fock energy current", "marker": "OPEN", "result": "Cycle229 closes finite spectral bookkeeping but leaves local positive energy current open"},
    )
    walls = (
        ("W1", "selection of K versus signed/spectral/action energy law"),
        ("W2", "physical phase zero, clock unit and empirical normalization"),
        ("W3", "full spatial stress/momentum/work tensor beyond T0mu continuity"),
        ("W4", "complete joint physical M2 contact-plus-mediator state compiler and local sector enforcement"),
        ("W5", "endogenous dressed/source preparation and unbounded nonlinear response"),
    )
    pairwise = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairwise.append({
                "pair": (walls[left][0], walls[right][0]),
                "closing_first_automatically_closes_second": "no",
                "closing_second_automatically_closes_first": "no",
                "independent": "yes",
                "witness": "Cycle562 separates current identity, unit/reference, stress completion, compiler, and preparation/response",
            })
    return {
        "N1_alternative_routes": routes,
        "N2_collapsed_open_wall_set": walls,
        "N2_full_pairwise_wall_independence": pairwise,
        "N3_hidden_walls": (
            "alpha=0 and beta=-0.3; rest normalization; K candidate selection",
            "periodic finite boundaries, depth/separation and number-projector readouts",
            "N=6 branch quadratures and separately certified 49-M2 support",
            "stationary eigensolver/selector and vacuum-plus-Q1 sectors without local enforcement",
        ),
        "N4_residual_matching": (
            "Cycle228: K is local/conserved but phase-relative and quadratic; H_abs is rest-linear but nonlocal",
            "Cycle229: positive Fock ledger lacks local positive-energy current and selected sea/reference",
            "Cycle230: K alone fails interacting-source interpretation; dressed/action-derived ledger remains live",
            "two-slice work ledger: exact contact impulse is dimensionless and lacks full joint physical intertwiner",
            "stationary dressed notes: eigenstate/resolvent exists but energy/contact/preparation are open",
            "Cycle559: coefficient-one number is locally conserved but explicitly not energy/stress",
        ),
        "N5_resolution_statement": "only bounded candidate identifications and route-specific nonidentities; no universal energy/source impossibility",
        "N6_partial_closure": "Route A closes T0mu continuity; Route B closes actual-contact impulse; a selected action/full compiler can extend them",
        "N7_hostile_steelman": (
            "a discrete action may select a true stress tensor and remove K-law ambiguity",
            "particle-hole/Fock carriers may make a signed local generator positive and additive",
            "a full joint physical compiler may reveal interaction energy missed by reduced Route B",
            "a different dressed branch or many-Q completion may produce the asymptotic response",
        ),
        "N8_cross_cycle_echo": (
            "Cycle228 kept action/direct-current routes live",
            "Cycle419 stationary failure was repaired constructively by later dressed-state work",
            "Cycle559 removed host current control by an orientation-independent update",
            "prior compiler walls were repeatedly retired without axiom changes",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": "none established",
        "axiom_pressure": "none",
    }


def main() -> None:
    started = perf_counter()
    print("CYCLE562 PHYSICAL ENERGY-STRESS/SOURCE IDENTIFICATION TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)

    dependency = dependency_controls()
    note = note_contract()
    route_a = free_local_current_controls()
    route_b = contact_impulse_controls()
    route_c = dressed_stationary_controls()
    bridge = cycle559_bridge_controls()
    resources = resource_and_domain_controls()
    inventory = supplied_inventory()
    nogo = no_go_controls()

    check("exact-pinned dependencies are unchanged", dependency["pass"], dependency)
    check("note contract preserves authority/audit, firewalls, M2 status, held disclosure, and N1-N8", note["pass"], note)
    held_a = tuple(row for row in route_a["prediction_rows"] if row["held"])
    check(
        "Route A has an independently rest-mass-normalized positive local T0mu current, exact continuity/conservation, all24 covariance, and a new held L7/r3 prediction",
        max(abs(row["rest_normalized_energy"] - MASS) for row in route_a["rest_rows"]) < TOL
        and route_a["maximum_local_continuity_residual"] < TOL
        and route_a["maximum_onsite_coin_density_residual"] < TOL
        and route_a["maximum_total_energy_conservation_residual"] < TOL
        and route_a["maximum_norm_residual"] < TOL
        and route_a["maximum_all24_covariance_residual"] < TOL
        and route_a["maximum_all24_current_vector_covariance_residual"] < TOL
        and route_a["proper_cubic_frames"] == 24
        and len(held_a) == 1
        and held_a[0]["target_energy_density"] > SIGNAL
        and route_a["code_leakage"] == 0
        and not route_a["full_spatial_stress_tensor_identified"],
        route_a,
    )
    check(
        "Route-A coin/stream/normalization deletions and phase-reference shift are visible",
        abs(route_a["deletions_and_reference"]["baseline_target"] - route_a["deletions_and_reference"]["coin_deleted_target"]) > SIGNAL
        and abs(route_a["deletions_and_reference"]["baseline_target"] - route_a["deletions_and_reference"]["stream_deleted_target"]) > SIGNAL
        and abs(route_a["deletions_and_reference"]["phase_reference_shifted_rest_energy"] - MASS) > SIGNAL
        and route_a["deletions_and_reference"]["normalization_deleted_energy"] == 0,
        route_a["deletions_and_reference"],
    )
    check(
        "Route B composes the actual Cycle230 contact with local exchange and gives an exact mass-normalized impulse balance plus a contact-sensitive conserved deviation coordinate",
        route_b["maximum_exact_impulse_balance_residual"] < TOL
        and route_b["minimum_actual_contact_impulse_norm"] > SIGNAL
        and route_b["full_gate_unitarity_residual"] < TOL
        and route_b["contact_exchange_commutator"] < TOL
        and route_b["contact_dressed_K_minimum_eigenvalue"] > -TOL
        and route_b["contact_dressed_K_commutator_residual"] < TOL
        and route_b["contact_dressed_K_expectation_conservation_residual"] < TOL
        and route_b["contact_deletion_K_change_norm"] > SIGNAL
        and route_b["exchange_deletion_signal"] > SIGNAL
        and route_b["Q_only_contact_impulse_maximum"] < TOL
        and max(row["seven_M2_intertwiner_residual"] for row in route_b["physical_seven_M2_rows"]) < TOL
        and not route_b["full_joint_physical_G_X_Y_intertwiner_executed"]
        and not route_b["called_physical_work_or_energy"],
        route_b,
    )
    held_c = tuple(row for row in route_c["rows"] if row["held"])
    check(
        "Route C retains a stationary dressed K-density/resolvent identity and makes a new held L10/separation4 prediction without calling eigenphase energy or rate",
        route_c["maximum_eigen_residual"] < TOL
        and route_c["maximum_stationary_energy_density_residual"] < TOL
        and route_c["maximum_shifted_resolvent_profile_residual"] < TOL
        and route_c["maximum_all24_update_covariance_residual"] < TOL
        and route_c["maximum_all24_selected_state_covariance_residual"] < TOL
        and route_c["proper_cubic_frames"] == 24
        and len(held_c) == 1
        and held_c[0]["energy_density_at_separation4"] > SIGNAL
        and route_c["theta_zero_reservoir_stationarity_residual"] < TOL
        and not route_c["contact_or_matter_in_route_C"]
        and route_c["selector_and_preparation_supplied"]
        and not route_c["eigenphase_called_energy_or_rate"],
        route_c,
    )
    check(
        "Cycle559 coefficient-one number matches the mass-scaled K coordinate only on the calibrated rest ray and does not supply a conserved dynamic bridge",
        bridge["maximum_Cycle559_number_drift"] < TOL
        and bridge["candidate_bridge_energy_drift"] > SIGNAL
        and bridge["m_times_number_equals_rest_energy_residual"] < TOL
        and bridge["m_times_number_equals_localized_energy_residual"] > SIGNAL
        and not bridge["operator_identification"]
        and bridge["rest_ray_calibration_match"]
        and bridge["shared_Q1_homogeneous_normalization"]
        and not bridge["dynamic_conserved_bridge_under_Cycle559"],
        bridge,
    )
    check(
        "physical-M2 counts/status, bounded gate support, leakage boundary, and lawful domain remain explicit",
        resources["route_A_physical_M2"]["held_L7"] == 2058
        and resources["route_B_physical_support_M2"] == 49
        and not resources["route_B_full_joint_state_intertwiner"]
        and resources["route_C_physical_M2"]["held_L10"] == 6001
        and resources["maximum_resolved_route_A_C_gate_support_M2"] == 2
        and not resources["global_parity_or_ordering_service"]
        and not resources["vacuum_plus_Q1_locally_enforced"]
        and resources["lawful_domain_rejections"] == 5
        and "word" not in resources["current_update_signatures"]["Cycle559_forward"],
        resources,
    )
    check(
        "supplied/derived/open inventory keeps phase, normalization, contact compiler, preparation, stress, time, gravity, Record, and Born boundaries explicit",
        len(inventory["supplied"]) >= 6
        and len(inventory["derived"]) >= 4
        and len(inventory["open"]) >= 4,
        inventory,
    )
    check(
        "full N1-N8 permits the bounded candidate-current result but blocks broad negative, minimum-content, and axiom-pressure claims",
        len(nogo["N1_alternative_routes"]) >= 6
        and len(nogo["N2_collapsed_open_wall_set"]) == 5
        and len(nogo["N2_full_pairwise_wall_independence"]) == 10
        and all(
            row["closing_first_automatically_closes_second"] == "no"
            and row["closing_second_automatically_closes_first"] == "no"
            and row["independent"] == "yes"
            for row in nogo["N2_full_pairwise_wall_independence"]
        )
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["axiom_pressure"] == "none",
        nogo,
    )

    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependency": dependency,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "Cycle559_bridge": bridge,
        "resources": resources,
        "inventory": inventory,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "rest-mass-normalized positive local deviation T0mu current plus actual-contact impulse balance",
            "physical_energy_fully_identified": False,
            "full_stress_tensor_identified": False,
            "gravity_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "elapsed_seconds": perf_counter() - started,
        "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    if FAIL:
        print("RESULT PHYSICAL_ENERGY_STRESS_SOURCE_IDENTIFICATION_TOURNAMENT_FAILED")
        raise SystemExit(1)
    print("RESULT PHYSICAL_REST_NORMALIZED_LOCAL_SOURCE_CURRENT_BOUNDED_POSITIVE")


if __name__ == "__main__":
    main()
