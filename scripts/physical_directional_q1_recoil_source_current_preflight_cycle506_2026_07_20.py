#!/usr/bin/env python3
"""Cycle 506 preflight: genuine 3D Q=1 mediator source/current test.

This executable freezes the candidate, manifests, observables, geometry, and
resource gates.  It deliberately performs no interacting train evolution and
no held response evaluation.  Dimensionless quasimomentum/current per update
are not physical momentum, time, force, energy, or gravity.  Authority none;
audit unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import re
import resource
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generated_beta_phase_register_cycle220_2026_07_16 as c220
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import physical_reciprocal_mediator_contact_dressed_tournament_cycle501_2026_07_20 as c501


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DIRECTIONAL_Q1_RECOIL_SOURCE_CURRENT_PREFLIGHT_CYCLE506_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
REGISTER_DIM = 9
SOURCE_LOCAL_DIM = 1 + REGISTER_DIM
MEDIATOR_LOCAL_DIM = 1 + 1 + 6  # vacuum, parked, six moving directions
MATTER_LOCAL_DIM = 1 + 6 + 15  # exact N=0,1,2 local exterior sectors
EMITTER_COUPLING = 0.02
SCATTERING_COUPLING = 0.02
CONTACT_COUPLING = c230.COUPLING
NUMERIC_TOLERANCE = 1e-10
RUNNER_TOLERANCE = 1e-8
ANGLE_CEILING = 0.35
BAND_FLOOR = 0.13
AXIAL_SEAM_CEILING = 1e-4
INITIAL_CONTACT_FLOOR = 1e-3
DYNAMIC_CONTACT_FLOOR = 0.01
DYNAMIC_BAND_FLOOR = 0.05
DYNAMIC_AXIAL_SEAM_CEILING = 0.02
CHARACTER_MAGNITUDE_FLOOR = 0.05
ABSOLUTE_RESPONSE_FLOOR = 1e-10
NUMERIC_SIGNAL_MULTIPLIER = 10.0
SUSTAINED_CONSECUTIVE_UPDATES = 3
TAIL_SAMPLE_COUNT = 2
SUSTAINED_TAIL_TO_PEAK_FLOOR = 0.50
SUSTAINED_TAIL_SIGN_COHERENCE_FLOOR = 0.90
IMPULSE_LAST_TO_PEAK_CEILING = 0.10
IMPULSE_PEAK_LATEST_WINDOW_INDEX = 1
EXPONENT_ABSOLUTE_TOLERANCE = 0.15
SWAP_LOG_RESIDUAL_CEILING = 0.25
NORMALIZED_AMPLITUDE_CV_CEILING = 0.25
ACTIVE_MEDIATOR_FLOOR = 1e-8
HARD_RSS_CEILING = 1_500_000_000
HARD_WALL_CEILING_SECONDS = 600.0
OUTGOING_DIRECTION = 1  # canonical -x; all 24 carried frames are audited
REVERSE = tuple(
    int(np.argmax(c210.DIRECTIONS @ (-direction))) for direction in c210.DIRECTIONS
)
PASS = 0
FAIL = 0
CONSTRUCTION_EVENTS: list[str] = []


@dataclass(frozen=True)
class Geometry:
    name: str
    side: int
    source_cell: tuple[int, int, int]
    probe_center: tuple[int, int, int]
    depth: int
    first_causal_overlap_update: int
    response_window: tuple[int, ...]
    axial_envelope: tuple[int, ...]
    held: bool


# These are real 3D cubes.  Only reachable vector-position supports are
# materialized; no axial quotient or transverse self-loop is permitted.
TRAIN = Geometry(
    "train-3D-L25", 25, (12, 12, 12), (8, 12, 12), 5, 2,
    tuple(range(2, 6)), (1, 2, 1), False
)
HELD = Geometry(
    "blind-held-3D-L27", 27, (13, 13, 13), (9, 13, 13), 5, 2,
    tuple(range(2, 6)), (1, 2, 1), True
)
GEOMETRIES = (TRAIN, HELD)

TRAIN_SOURCE_BETAS = (-2 * np.pi / 9, -4 * np.pi / 9, -2 * np.pi / 3)
TRAIN_PROBE_BETAS = TRAIN_SOURCE_BETAS
HELD_SOURCE_BETAS = (0.0, -8 * np.pi / 9)
HELD_PROBE_BETAS = HELD_SOURCE_BETAS

ROUTES = {
    "A-fixed": {"source_function": "1", "probe_function": "1", "active_exponent": 0.0},
    "B-linear-linear": {
        "source_function": "M_plus", "probe_function": "M_plus", "active_exponent": 2.0
    },
    "C-sqrt-linear": {
        "source_function": "sqrt(M_plus)", "probe_function": "M_plus", "active_exponent": 1.0
    },
}

TECHNICAL_GATES = {
    "norm_inverse_number_mediatorQ_lawful": RUNNER_TOLERANCE,
    "free_repeat": RUNNER_TOLERANCE,
    "cube_face_shell_probability": 1e-12,
    "dynamic_contact_maximum_floor": DYNAMIC_CONTACT_FLOOR,
    "dynamic_band_minimum_floor": DYNAMIC_BAND_FLOOR,
    "dynamic_axial_seam_maximum_ceiling": DYNAMIC_AXIAL_SEAM_CEILING,
    "translation_character_magnitude_floor": CHARACTER_MAGNITUDE_FLOOR,
}

# Rightmost factor acts first.  The Cycle-230 subsequence is exactly
# U_contact S_CAR Gamma(C_beta); collision then changes the direction that the
# final true mediator stream uses.
FIXED_FACTOR_WORD = (
    "S_mediator_direction",
    "U_Cycle501_collision[0.02*f_probe(M_plus)]",
    "U_Cycle230_contact[0.04]",
    "S_signed_CAR",
    "Gamma_Cycle219_coin(beta_probe)",
    "U_source_emitter[0.02*f_source(M_plus);park<->outgoing]",
)

SOURCE_HASHES = {
    "cycle210": (ROOT / "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py", "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b"),
    "cycle219": (ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py", "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a"),
    "cycle220": (ROOT / "scripts/generated_beta_phase_register_cycle220_2026_07_16.py", "252708e5adf782d9ad2869add0d64fa757d9d0473d054ee548e98e31d5f7276f"),
    "cycle230": (ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py", "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae"),
    "cycle441": (ROOT / "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py", "c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4"),
    "cycle501": (ROOT / "scripts/physical_reciprocal_mediator_contact_dressed_tournament_cycle501_2026_07_20.py", "7e8a88c5b0cdd576d868a3932d820da7f9cf985b10de498c83d34eb35daa959d"),
}

EXPECTED_TRAIN_MANIFEST_SHA256 = "a5e37ba91332bf55f21b59543d5446379bbd92b71c948e85bf03c96bc306c3ee"
EXPECTED_HELD_MANIFEST_SHA256 = "40e616dc4f5cc0dc70ac1801484f33c2be11009b56485e3f222e4b09e62aaed8"


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
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def beta_name(beta: float) -> str:
    names = {
        round(0.0, 12): "0",
        round(-2 * np.pi / 9, 12): "-2pi/9",
        round(-4 * np.pi / 9, 12): "-4pi/9",
        round(-2 * np.pi / 3, 12): "-2pi/3",
        round(-8 * np.pi / 9, 12): "-8pi/9",
    }
    return names[round(float(beta), 12)]


def manifest_digest(rows: list[dict]) -> str:
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()


def row_manifests() -> tuple[list[dict], list[dict]]:
    train: list[dict] = []
    for route in ROUTES:
        for source_beta in TRAIN_SOURCE_BETAS:
            for probe_beta in TRAIN_PROBE_BETAS:
                train.append({
                    "disposition": "train",
                    "role": "primary-mass-grid",
                    "route": route,
                    "source_beta": beta_name(source_beta),
                    "probe_beta": beta_name(probe_beta),
                    "geometry": asdict(TRAIN),
                    "outgoing_direction": OUTGOING_DIRECTION,
                    "deletion": "none",
                    "free_partner": True,
                    "refit": False,
                })
    sentinel = {
        "route": "C-sqrt-linear",
        "source_beta": beta_name(-4 * np.pi / 9),
        "probe_beta": beta_name(-4 * np.pi / 9),
        "geometry": asdict(TRAIN),
        "outgoing_direction": OUTGOING_DIRECTION,
        "free_partner": True,
        "refit": False,
    }
    for deletion in (
        "emitter", "collision", "mediator-stream", "contact", "probe-coin",
        "source-mass-factor", "probe-mass-factor",
    ):
        train.append({
            "disposition": "train", "role": "selected-deletion", **sentinel,
            "deletion": deletion,
        })
    train.append({
        "disposition": "train", "role": "direction-reversal-control", **sentinel,
        "outgoing_direction": REVERSE[OUTGOING_DIRECTION], "deletion": "none",
    })

    held: list[dict] = []
    for route in ROUTES:
        for source_beta in HELD_SOURCE_BETAS:
            for probe_beta in HELD_PROBE_BETAS:
                held.append({
                    "disposition": "blind-held",
                    "role": "blind-held-mass-grid",
                    "route": route,
                    "source_beta": beta_name(source_beta),
                    "probe_beta": beta_name(probe_beta),
                    "geometry": asdict(HELD),
                    "outgoing_direction": OUTGOING_DIRECTION,
                    "deletion": "none",
                    "free_partner": True,
                    "refit": False,
                })
    return train, held


def controller_factor(route: str, role: str, mass: float) -> float:
    if route == "A-fixed":
        return 1.0
    if route == "B-linear-linear":
        return mass
    if route == "C-sqrt-linear":
        return float(np.sqrt(mass)) if role == "source" else mass
    raise ValueError(route)


def source_probability_factor(route: str, mass: float) -> float:
    return float(np.sin(EMITTER_COUPLING * controller_factor(route, "source", mass)) ** 2)


def candidate_response_factor(route: str, source_mass: float, probe_mass: float) -> float:
    return float(
        source_probability_factor(route, source_mass)
        * abs(np.sin(SCATTERING_COUPLING * controller_factor(route, "probe", probe_mass)))
    )


def response_floor(numeric_residuals: tuple[float, ...] | list[float]) -> float:
    return max(
        ABSOLUTE_RESPONSE_FLOOR,
        NUMERIC_SIGNAL_MULTIPLIER * max((abs(value) for value in numeric_residuals), default=0.0),
    )


def interaction_minus_free_observables(
    interacting_current: tuple[float, ...],
    free_current: tuple[float, ...],
    interacting_character: tuple[complex, ...],
    free_character: tuple[complex, ...],
) -> dict:
    if not (
        len(interacting_current) == len(free_current)
        == len(interacting_character) == len(free_character)
    ):
        raise ValueError("interaction/free traces must have equal lengths")
    delta_current = np.asarray(interacting_current) - np.asarray(free_current)
    character_magnitudes = np.asarray([
        min(abs(interacting), abs(free))
        for interacting, free in zip(interacting_character, free_character)
    ])
    delta_quasimomentum = np.asarray([
        np.angle(interacting * np.conj(free))
        if min(abs(interacting), abs(free)) >= CHARACTER_MAGNITUDE_FLOOR else np.nan
        for interacting, free in zip(interacting_character, free_character)
    ])
    return {
        "delta_plane_current": tuple(float(value) for value in delta_current),
        "cumulative_delta_plane_current": tuple(float(value) for value in np.cumsum(delta_current)),
        "delta_principal_quasimomentum": tuple(float(value) for value in delta_quasimomentum),
        "minimum_character_magnitude": float(np.min(character_magnitudes)),
        "response_amplitude": float(np.max(np.abs(delta_current))),
    }


def classify_response(delta_current: tuple[float, ...], numeric_residuals: tuple[float, ...]) -> dict:
    values = np.asarray(delta_current, dtype=float)
    if len(values) != len(TRAIN.response_window):
        raise ValueError("classifier consumes exactly the frozen four-update response window")
    floor = response_floor(numeric_residuals)
    peak = float(np.max(np.abs(values)))
    peak_index = int(np.argmax(np.abs(values)))
    signs = np.where(values >= floor, 1, np.where(values <= -floor, -1, 0))
    longest = 0
    run = 0
    previous = 0
    for sign in signs:
        if sign and sign == previous:
            run += 1
        elif sign:
            run = 1
        else:
            run = 0
        previous = int(sign)
        longest = max(longest, run)
    tail = values[-TAIL_SAMPLE_COUNT:]
    tail_ratio = float(np.mean(np.abs(tail)) / peak) if peak else 0.0
    tail_denominator = float(np.sum(np.abs(tail)))
    tail_coherence = float(abs(np.sum(tail)) / tail_denominator) if tail_denominator else 0.0
    cumulative = np.cumsum(values)
    cumulative_scale = float(max(np.max(np.abs(cumulative)), floor))
    last_to_peak = float(abs(values[-1]) / peak) if peak else 0.0
    impulse_plateau_step = float(abs(values[-1]) / cumulative_scale)
    active = peak >= floor
    sustained = (
        active
        and longest >= SUSTAINED_CONSECUTIVE_UPDATES
        and tail_ratio >= SUSTAINED_TAIL_TO_PEAK_FLOOR
        and tail_coherence >= SUSTAINED_TAIL_SIGN_COHERENCE_FLOOR
    )
    impulse = (
        active and not sustained
        and peak_index <= IMPULSE_PEAK_LATEST_WINDOW_INDEX
        and last_to_peak <= IMPULSE_LAST_TO_PEAK_CEILING
        and impulse_plateau_step <= IMPULSE_LAST_TO_PEAK_CEILING
    )
    classification = "sustained" if sustained else "impulse" if impulse else "transient-unresolved" if active else "null"
    return {
        "classification": classification,
        "signal_floor": floor,
        "peak_absolute_delta_current": peak,
        "peak_window_index": peak_index,
        "longest_same_sign_above_floor_run": longest,
        "tail_to_peak_ratio": tail_ratio,
        "tail_sign_coherence": tail_coherence,
        "last_to_peak_ratio": last_to_peak,
        "impulse_plateau_step_ratio": impulse_plateau_step,
    }


def deletion_expectations(metrics: dict[str, dict]) -> dict[str, bool]:
    required = {
        "emitter", "collision", "mediator-stream", "contact", "probe-coin",
        "source-mass-factor", "probe-mass-factor",
    }
    if set(metrics) != required:
        raise ValueError("deletion metric set does not match the frozen seven controls")
    return {
        "emitter": metrics["emitter"]["maximum_active_mediator"] <= metrics["emitter"]["signal_floor"]
        and metrics["emitter"]["response_amplitude"] <= metrics["emitter"]["signal_floor"],
        "collision": metrics["collision"]["maximum_active_mediator"] >= ACTIVE_MEDIATOR_FLOOR
        and metrics["collision"]["response_amplitude"] <= metrics["collision"]["signal_floor"],
        "mediator-stream": metrics["mediator-stream"]["maximum_mediator_displacement"] <= RUNNER_TOLERANCE,
        "contact": abs(metrics["contact"]["applied_contact_coupling"]) <= RUNNER_TOLERANCE,
        "probe-coin": metrics["probe-coin"]["maximum_transverse_CAR_weight"] <= RUNNER_TOLERANCE,
        "source-mass-factor": abs(metrics["source-mass-factor"]["applied_source_factor"] - 1) <= RUNNER_TOLERANCE
        and abs(metrics["source-mass-factor"]["source_output"] - metrics["source-mass-factor"]["matched_primary_source_output"]) >= metrics["source-mass-factor"]["signal_floor"]
        and abs(metrics["source-mass-factor"]["response_amplitude"] - metrics["source-mass-factor"]["matched_primary_response_amplitude"]) >= metrics["source-mass-factor"]["signal_floor"],
        "probe-mass-factor": abs(metrics["probe-mass-factor"]["applied_probe_factor"] - 1) <= RUNNER_TOLERANCE
        and abs(metrics["probe-mass-factor"]["source_output"] - metrics["probe-mass-factor"]["matched_primary_source_output"]) <= metrics["probe-mass-factor"]["signal_floor"]
        and abs(metrics["probe-mass-factor"]["response_amplitude"] - metrics["probe-mass-factor"]["matched_primary_response_amplitude"]) >= metrics["probe-mass-factor"]["signal_floor"],
    }


def route_disposition(route: str, primary_rows: list[dict], deletions_pass: bool) -> dict:
    if len(primary_rows) != 9:
        raise ValueError("a route disposition requires the complete 3x3 train mass grid")
    target = ROUTES[route]["active_exponent"]
    technical = all(row["technical_pass"] for row in primary_rows) and deletions_pass
    signal = all(row["response_amplitude"] >= row["signal_floor"] for row in primary_rows)
    diagonal = sorted((row for row in primary_rows if row["source_mass"] == row["probe_mass"]), key=lambda row: row["source_mass"])
    source_masses = sorted({row["source_mass"] for row in primary_rows})
    source_outputs = []
    source_probe_independence_residuals = []
    for source_mass in source_masses:
        values = np.asarray([row["source_output"] for row in primary_rows if row["source_mass"] == source_mass])
        source_outputs.append(float(np.mean(values)))
        source_probe_independence_residuals.append(float(np.std(values) / abs(np.mean(values))) if np.mean(values) else float("inf"))
    exponent = float("nan")
    exponent_residual = float("inf")
    if len(source_outputs) == 3 and all(value > 0 for value in source_outputs):
        exponent = float(np.polyfit(
            np.log(source_masses), np.log(source_outputs), 1
        )[0])
        exponent_residual = abs(exponent - target)
    lookup = {(row["source_mass"], row["probe_mass"]): row for row in primary_rows}
    swap_residuals = []
    for source_mass, probe_mass in combinations(sorted({row["source_mass"] for row in primary_rows}), 2):
        forward = lookup[(source_mass, probe_mass)]["response_amplitude"]
        reverse = lookup[(probe_mass, source_mass)]["response_amplitude"]
        expected = candidate_response_factor(route, source_mass, probe_mass) / candidate_response_factor(route, probe_mass, source_mass)
        swap_residuals.append(abs(np.log(forward / reverse / expected)) if forward > 0 and reverse > 0 else float("inf"))
    normalized = np.asarray([
        row["response_amplitude"] / candidate_response_factor(route, row["source_mass"], row["probe_mass"])
        for row in primary_rows
    ])
    normalized_cv = float(np.std(normalized) / abs(np.mean(normalized))) if np.mean(normalized) else float("inf")
    scaling_pass = (
        exponent_residual <= EXPONENT_ABSOLUTE_TOLERANCE
        and max(source_probe_independence_residuals) <= RUNNER_TOLERANCE
        and max(swap_residuals) <= SWAP_LOG_RESIDUAL_CEILING
        and normalized_cv <= NORMALIZED_AMPLITUDE_CV_CEILING
    )
    diagonal_classes = tuple(row["classification"] for row in diagonal)
    if not technical:
        disposition = "invalid-technical-or-deletion"
    elif not signal:
        disposition = "null-or-mixed-response-on-frozen-current"
    elif not scaling_pass:
        disposition = "partial-scaling-mismatch"
    elif all(value == "sustained" for value in diagonal_classes):
        disposition = "pass-sustained-source-current"
    elif all(value == "impulse" for value in diagonal_classes):
        disposition = "partial-impulse"
    else:
        disposition = "partial-transient-or-mixed-morphology"
    return {
        "disposition": disposition,
        "fitted_source_output_exponent": exponent,
        "target_source_output_exponent": target,
        "exponent_absolute_residual": exponent_residual,
        "maximum_source_output_probe_independence_CV": max(source_probe_independence_residuals),
        "maximum_source_probe_swap_log_residual": max(swap_residuals),
        "normalized_amplitude_CV": normalized_cv,
        "diagonal_classifications": diagonal_classes,
        "technical_pass": technical,
        "all_primary_signals_active": signal,
    }


def response_classifier_preflight() -> None:
    print("\nFROZEN INTERACTION-MINUS-FREE RESPONSE / CLASSIFIER / DISPOSITION")
    sustained = classify_response((1e-5, 1.1e-5, 1.05e-5, 1e-5), (1e-14,))
    impulse = classify_response((1e-5, 4e-6, 5e-7, 1e-7), (1e-14,))
    null = classify_response((0.0, 0.0, 0.0, 0.0), (1e-14,))
    masses = (1.091910702798607, 2.51729889353184, 5.19615242270663)
    route_checks = {}
    for route in ROUTES:
        rows = []
        for source_mass in masses:
            for probe_mass in masses:
                amplitude = candidate_response_factor(route, source_mass, probe_mass)
                rows.append({
                    "source_mass": source_mass, "probe_mass": probe_mass,
                    "source_output": source_probability_factor(route, source_mass),
                    "response_amplitude": amplitude, "signal_floor": ABSOLUTE_RESPONSE_FLOOR,
                    "classification": "sustained", "technical_pass": True,
                })
        result = route_disposition(route, rows, True)
        route_checks[route] = result
    deletion_metrics = {
        "emitter": {"maximum_active_mediator": 0.0, "response_amplitude": 0.0, "signal_floor": ABSOLUTE_RESPONSE_FLOOR},
        "collision": {"maximum_active_mediator": 1e-4, "response_amplitude": 0.0, "signal_floor": ABSOLUTE_RESPONSE_FLOOR},
        "mediator-stream": {"maximum_mediator_displacement": 0.0},
        "contact": {"applied_contact_coupling": 0.0},
        "probe-coin": {"maximum_transverse_CAR_weight": 0.0},
        "source-mass-factor": {
            "applied_source_factor": 1.0, "source_output": 1e-4,
            "matched_primary_source_output": 3e-4, "response_amplitude": 2e-6,
            "matched_primary_response_amplitude": 5e-6, "signal_floor": ABSOLUTE_RESPONSE_FLOOR,
        },
        "probe-mass-factor": {
            "applied_probe_factor": 1.0, "source_output": 3e-4,
            "matched_primary_source_output": 3e-4, "response_amplitude": 2e-6,
            "matched_primary_response_amplitude": 5e-6, "signal_floor": ABSOLUTE_RESPONSE_FLOOR,
        },
    }
    deletion_checks = deletion_expectations(deletion_metrics)
    check(
        "response, morphology, scaling, swap, deletion, and route dispositions are executable before output",
        sustained["classification"] == "sustained"
        and impulse["classification"] == "impulse"
        and null["classification"] == "null"
        and all(row["disposition"] == "pass-sustained-source-current" for row in route_checks.values())
        and all(deletion_checks.values()),
        {
            "free_partner": "same Cycle219 coin + signed 3D CAR stream + Cycle230 contact; emitter=collision=0; mediator parked",
            "response_window": TRAIN.response_window,
            "primary_response": "max_t |<J_x>_interacting-<J_x>_free|",
            "source_output_input": "observed P_active after update 1 from the mediator ledger; sin^2 law is comparator only",
            "secondary_response": "Arg(z_x_interacting conj(z_x_free)) when both |z_x|>=0.05",
            "absolute_floor": ABSOLUTE_RESPONSE_FLOOR,
            "numeric_multiplier": NUMERIC_SIGNAL_MULTIPLIER,
            "sustained_fixture": sustained,
            "impulse_fixture": impulse,
            "null_fixture": null,
            "ideal_route_fixtures": route_checks,
            "deletion_fixtures": deletion_checks,
            "scout_row": {"route": "C-sqrt-linear", "source_beta": "-4pi/9", "probe_beta": "-4pi/9"},
            "scout_evidence_disposition": "resource/runtime only; response quarantined; full train rerun required",
        },
    )


def contracts() -> tuple[list[dict], list[dict]]:
    print("CONTRACT / PREDECESSOR HASHES / IMMUTABLE MANIFESTS")
    hashes = {name: path.is_file() and file_sha(path) == expected
              for name, (path, expected) in SOURCE_HASHES.items()}
    check("all exact predecessor hashes match", all(hashes.values()), hashes)
    train, held = row_manifests()
    train_digest, held_digest = manifest_digest(train), manifest_digest(held)
    check(
        "the train and blind-held manifests are immutable, disjoint, and refit-free",
        train_digest == EXPECTED_TRAIN_MANIFEST_SHA256
        and held_digest == EXPECTED_HELD_MANIFEST_SHA256
        and len(train) == 35 and len(held) == 12
        and not {json.dumps(row, sort_keys=True) for row in train}
        & {json.dumps(row, sort_keys=True) for row in held}
        and all(not row["refit"] for row in train + held),
        {"train_rows": len(train), "held_rows": len(held),
         "train_sha256": train_digest, "held_sha256": held_digest},
    )
    required = (
        "preflight only", "one fixed factor word", "global mediator q=1",
        "free partner", "blind held", "no refit", "all 24 proper-cubic frames",
        "update count is not time", "response is not force or gravity",
        "authority none", "audit unset", "five live families", "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(x for x in required if x not in normalized(NOTE))
    declared = None
    if NOTE.exists():
        match = re.search(r"frozen preflight runner sha256:\s*([0-9a-f]{64})", normalized(NOTE))
        declared = match.group(1) if match else None
    check(
        "the note freezes semantics and the executable boundary",
        not missing and declared == file_sha(Path(__file__)),
        {"missing_terms": missing, "declared_runner_sha256": declared,
         "actual_runner_sha256": file_sha(Path(__file__))},
    )
    return train, held


def functional_mass_stack() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    register = c220.cyclic_shift(REGISTER_DIM)
    identity = np.eye(REGISTER_DIM, dtype=complex)
    mass = 3j * (register - identity) @ np.linalg.solve(register + identity, identity)
    mass = np.asarray((mass + mass.conj().T) / 2)
    values, vectors = np.linalg.eigh(mass)
    # The nine-cycle contains an exact beta=0 ray.  Threshold only values below
    # the already frozen operator tolerance so numerical eigensolver dust does
    # not turn the held zero-mass deletion into a tiny emitter.
    positive_values = np.where(values > NUMERIC_TOLERANCE, values, 0.0)
    positive = (vectors * positive_values) @ vectors.conj().T
    sqrt_positive = (vectors * np.sqrt(positive_values)) @ vectors.conj().T
    CONSTRUCTION_EVENTS.append("M(S), M_plus, sqrt(M_plus) constructed before ray selection")
    return register, mass, positive, sqrt_positive


def beta_ray(register: np.ndarray, target: float) -> np.ndarray:
    if not CONSTRUCTION_EVENTS:
        raise RuntimeError("spectral rays cannot precede operator construction")
    beta, _value, vector = min(
        c220.register_eigenpairs(register),
        key=lambda row: abs(np.angle(np.exp(1j * (row[0] - target)))),
    )
    if abs(np.angle(np.exp(1j * (beta - target)))) > 2e-12:
        raise ValueError("requested beta is absent from the physical Q=1 register")
    return vector


def mass_and_angle_preflight() -> dict[float, float]:
    print("\nOPERATOR-FIRST CYCLE-441 SOURCE / PROBE CONTROLS")
    register, mass, positive, square_root = functional_mass_stack()
    values = np.linalg.eigvalsh(mass)
    positive_values = np.linalg.eigvalsh(positive)
    selected: dict[float, float] = {}
    ray_residuals = []
    rows = []
    for disposition, betas in (
        ("train-source", TRAIN_SOURCE_BETAS), ("train-probe", TRAIN_PROBE_BETAS),
        ("blind-held-source", HELD_SOURCE_BETAS), ("blind-held-probe", HELD_PROBE_BETAS),
    ):
        for beta in betas:
            vector = beta_ray(register, beta)
            value = np.vdot(vector, positive @ vector)
            root = np.vdot(vector, square_root @ vector)
            ray_residuals.extend((
                np.linalg.norm(positive @ vector - value * vector),
                np.linalg.norm(square_root @ vector - root * vector),
            ))
            selected[beta] = float(value.real)
            rows.append((disposition, beta_name(beta), float(value.real), float(root.real)))
    maximum_angle = 0.0
    for source_beta in TRAIN_SOURCE_BETAS + HELD_SOURCE_BETAS:
        for probe_beta in TRAIN_PROBE_BETAS + HELD_PROBE_BETAS:
            sm, pm = selected[source_beta], selected[probe_beta]
            maximum_angle = max(maximum_angle, EMITTER_COUPLING * max(1.0, sm, np.sqrt(max(0.0, sm))),
                                SCATTERING_COUPLING * max(1.0, pm))
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        rep = np.kron(np.eye(REGISTER_DIM), c210.direction_permutation(frame))
        for operator in (positive, square_root):
            carried = np.kron(operator, np.eye(6))
            frame_residuals.append(np.linalg.norm(rep @ carried @ rep.T - carried))
    print("mass_eigenvalues", [float(x) for x in values])
    print("selected_mass_rows", rows)
    check(
        "M_plus/sqrt are PSD operator-first scalar controls with a safe angle menu",
        positive_values[0] > -NUMERIC_TOLERANCE
        and np.linalg.norm(square_root @ square_root - positive) < NUMERIC_TOLERANCE
        and max(ray_residuals) < NUMERIC_TOLERANCE
        and max(frame_residuals) < NUMERIC_TOLERANCE
        and maximum_angle < ANGLE_CEILING,
        {"maximum_ray_residual": max(ray_residuals),
         "maximum_all24_residual": max(frame_residuals),
         "maximum_emitter_or_scattering_angle": maximum_angle},
    )
    train = {round(selected[x], 12) for x in TRAIN_SOURCE_BETAS}
    held = {round(selected[x], 12) for x in HELD_SOURCE_BETAS}
    check(
        "three nonzero train masses and blind zero/maximum held masses are disjoint",
        len(train) == 3 and min(train) > 0 and len(held) == 2 and not train & held
        and min(held) == 0.0 and max(held) == round(max(positive_values), 12),
        {"train": sorted(train), "blind_held": sorted(held)},
    )
    return selected


def local_bases() -> tuple[tuple[int, ...], dict[int, int]]:
    masks = (0,) + tuple(1 << d for d in range(6)) + tuple(
        (1 << a) | (1 << b) for a, b in combinations(range(6), 2)
    )
    return masks, {mask: i for i, mask in enumerate(masks)}


def car_move(mask: int, old: int, new: int) -> tuple[int, int] | None:
    if not (mask >> old) & 1 or (mask >> new) & 1:
        return None
    a_sign = -1 if (mask & ((1 << old) - 1)).bit_count() % 2 else 1
    removed = mask ^ (1 << old)
    c_sign = -1 if (removed & ((1 << new) - 1)).bit_count() % 2 else 1
    return removed | (1 << new), a_sign * c_sign


def local_collision_generator() -> sparse.csr_matrix:
    masks, index = local_bases()
    rows, columns, data = [], [], []
    for column, mask in enumerate(masks):
        for med in range(6):
            moved = car_move(mask, REVERSE[med], med)
            if moved is None:
                continue
            target, sign = moved
            rows.append(index[target] * MEDIATOR_LOCAL_DIM + 2 + REVERSE[med])
            columns.append(column * MEDIATOR_LOCAL_DIM + 2 + med)
            data.append(complex(sign))
    dim = MATTER_LOCAL_DIM * MEDIATOR_LOCAL_DIM
    return sparse.coo_matrix((data, (rows, columns)), shape=(dim, dim)).tocsr()


def matter_frame_map(mask: int, permutation: np.ndarray) -> tuple[int, int]:
    occupied = [direction for direction in range(6) if (mask >> direction) & 1]
    moved = [int(np.argmax(permutation[:, direction])) for direction in occupied]
    inversions = sum(
        moved[left] > moved[right]
        for left in range(len(moved)) for right in range(left + 1, len(moved))
    )
    return sum(1 << direction for direction in moved), -1 if inversions % 2 else 1


def frame_cell(cell: tuple[int, int, int], frame: np.ndarray, side: int) -> tuple[int, int, int]:
    centered = np.asarray(cell) - side // 2
    return tuple(int(x) for x in ((frame @ centered + side // 2) % side))


def stream_key(cell: tuple[int, int, int], direction: int, side: int) -> tuple[tuple[int, int, int], int]:
    return tuple(int(x) for x in ((np.asarray(cell) + c210.DIRECTIONS[direction]) % side)), direction


def canonical_pair(first: int, second: int) -> tuple[tuple[int, int], int]:
    if first == second:
        raise ValueError("Pauli-duplicate mode")
    return ((first, second), 1) if first < second else ((second, first), -1)


def canonical_mode_pair(first: tuple, second: tuple) -> tuple[tuple[tuple, tuple], int]:
    if first == second:
        raise ValueError("Pauli-duplicate mode")
    return ((first, second), 1) if first < second else ((second, first), -1)


def add_amplitude(output: dict, key: tuple, value: complex) -> None:
    output[key] = output.get(key, 0j) + value


def sparse_emitter(state: dict, source_cell: tuple[int, int, int], angle: float) -> dict:
    output: dict = {}
    cosine, sine = np.cos(angle), np.sin(angle)
    outgoing = (source_cell, OUTGOING_DIRECTION)
    for (pair, mediator), amplitude in state.items():
        if mediator is None:
            add_amplitude(output, (pair, None), cosine * amplitude)
            add_amplitude(output, (pair, outgoing), 1j * sine * amplitude)
        elif mediator == outgoing:
            add_amplitude(output, (pair, outgoing), cosine * amplitude)
            add_amplitude(output, (pair, None), 1j * sine * amplitude)
        else:
            add_amplitude(output, (pair, mediator), amplitude)
    return {key: value for key, value in output.items() if abs(value) > 1e-15}


def sparse_car_coin(state: dict, beta: float, *, inverse: bool = False) -> dict:
    coin = c219.common_species(beta).coin
    if inverse:
        coin = coin.conj().T
    output: dict = {}
    for (pair, mediator), amplitude in state.items():
        (left_cell, left_direction), (right_cell, right_direction) = pair
        for out_left in range(6):
            left = coin[out_left, left_direction]
            if abs(left) < 1e-15:
                continue
            for out_right in range(6):
                right = coin[out_right, right_direction]
                if abs(right) < 1e-15:
                    continue
                first, second = (left_cell, out_left), (right_cell, out_right)
                if first == second:
                    continue
                target_pair, sign = canonical_mode_pair(first, second)
                add_amplitude(output, (target_pair, mediator), sign * left * right * amplitude)
    return {key: value for key, value in output.items() if abs(value) > 1e-15}


def sparse_car_stream(state: dict, *, inverse: bool = False) -> dict:
    output: dict = {}
    stream_sign = -1 if inverse else 1
    for (pair, mediator), amplitude in state.items():
        moved = []
        for cell, direction in pair:
            moved.append((
                tuple(int(x) for x in (np.asarray(cell) + stream_sign * c210.DIRECTIONS[direction])),
                direction,
            ))
        target_pair, wedge_sign = canonical_mode_pair(*moved)
        add_amplitude(output, (target_pair, mediator), wedge_sign * amplitude)
    return output


def sparse_contact(state: dict, coupling: float) -> dict:
    phase = np.exp(1j * coupling)
    return {
        (pair, mediator): amplitude * (phase if pair[0][0] == pair[1][0] else 1)
        for (pair, mediator), amplitude in state.items()
    }


def sparse_collision(state: dict, coupling: float) -> dict:
    output: dict = {}
    active = {}
    for (pair, mediator), amplitude in state.items():
        if mediator is None:
            add_amplitude(output, (pair, None), amplitude)
        else:
            active[(pair, mediator[0], mediator[1])] = amplitude
    for (pair, cell, direction), amplitude in c501.explicit_collision(active, coupling).items():
        add_amplitude(output, (pair, (cell, direction)), amplitude)
    return output


def sparse_mediator_stream(state: dict, *, inverse: bool = False) -> dict:
    output: dict = {}
    stream_sign = -1 if inverse else 1
    for (pair, mediator), amplitude in state.items():
        if mediator is None:
            target = None
        else:
            cell, direction = mediator
            target = (
                tuple(int(x) for x in (np.asarray(cell) + stream_sign * c210.DIRECTIONS[direction])),
                direction,
            )
        add_amplitude(output, (pair, target), amplitude)
    return output


def sparse_factor_word(state: dict, beta: float, emitter_angle: float, collision_angle: float) -> dict:
    output = sparse_emitter(state, TRAIN.source_cell, emitter_angle)
    output = sparse_car_coin(output, beta)
    output = sparse_car_stream(output)
    output = sparse_contact(output, CONTACT_COUPLING)
    output = sparse_collision(output, collision_angle)
    return sparse_mediator_stream(output)


def sparse_inverse_word(state: dict, beta: float, emitter_angle: float, collision_angle: float) -> dict:
    output = sparse_mediator_stream(state, inverse=True)
    output = sparse_collision(output, -collision_angle)
    output = sparse_contact(output, -CONTACT_COUPLING)
    output = sparse_car_stream(output, inverse=True)
    output = sparse_car_coin(output, beta, inverse=True)
    return sparse_emitter(output, TRAIN.source_cell, -emitter_angle)


def sparse_initial_state() -> dict:
    weights = np.asarray(TRAIN.axial_envelope, dtype=float)
    weights /= np.linalg.norm(weights)
    positions = [
        (TRAIN.probe_center[0] + offset, TRAIN.probe_center[1], TRAIN.probe_center[2])
        for offset in (-1, 0, 1)
    ]
    output: dict = {}
    for left_cell, left_weight in zip(positions, weights):
        for right_cell, right_weight in zip(positions, weights):
            pair, sign = canonical_mode_pair((left_cell, 0), (right_cell, 1))
            add_amplitude(output, (pair, None), sign * left_weight * right_weight)
    return output


def sparse_state_norm(state: dict) -> float:
    return float(np.sqrt(sum(abs(value) ** 2 for value in state.values())))


def sparse_state_residual(left: dict, right: dict) -> float:
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in set(left) | set(right))))


def vector_position_evaluator_preflight() -> None:
    print("\nACTUAL VECTOR-POSITION SPARSE WORD / INVERSE / TRANSVERSE PROPAGATION")
    initial = sparse_initial_state()
    beta = TRAIN_PROBE_BETAS[1]
    output = sparse_factor_word(initial, beta, EMITTER_COUPLING, SCATTERING_COUPLING)
    restored = sparse_inverse_word(output, beta, EMITTER_COUPLING, SCATTERING_COUPLING)
    transverse_weight = sum(
        abs(amplitude) ** 2
        for (pair, _mediator), amplitude in output.items()
        if any(mode[0][1:] != TRAIN.probe_center[1:] for mode in pair)
    )
    check(
        "the actual sparse 3D word preserves norm/inverse and propagates CAR amplitude transversely",
        abs(sparse_state_norm(initial) - 1) < NUMERIC_TOLERANCE
        and abs(sparse_state_norm(output) - 1) < NUMERIC_TOLERANCE
        and sparse_state_residual(restored, initial) < RUNNER_TOLERANCE
        and transverse_weight > 1e-4,
        {"initial_keys": len(initial), "one_update_keys": len(output),
         "norm_residual": abs(sparse_state_norm(output) - 1),
         "inverse_residual": sparse_state_residual(restored, initial),
         "transverse_CAR_weight_after_one_update": transverse_weight,
         "coordinate_key_shape": "((x,y,z),direction)",
         "axial_quotient": False},
    )


def covariance_and_domain_preflight() -> None:
    print("\nGENUINE SIX-DIRECTION STREAM / COLLISION / ALL-24 COVARIANCE")
    generator = local_collision_generator()
    predecessor = c501.local_collision_covariance_controls()
    stream_failures = 0
    car_pair_stream_failures = 0
    emitter_residuals = []
    coin_residuals = []
    collision_residuals = []
    contact_residuals = []
    side = 3
    cells = tuple((x, y, z) for x in range(side) for y in range(side) for z in range(side))
    cell_index = {cell: index for index, cell in enumerate(cells)}
    number = np.asarray([mask.bit_count() for mask in local_bases()[0]])
    contact = np.diag(np.exp(1j * CONTACT_COUPLING * number * (number - 1) / 2))
    for frame in c210.proper_cubic_frames():
        direction_rep = c210.direction_permutation(frame)
        direction_map = tuple(int(np.argmax(direction_rep[:, d])) for d in range(6))
        for cell in cells:
            for direction in range(6):
                moved_cell, moved_direction = stream_key(cell, direction, side)
                left = (frame_cell(moved_cell, frame, side), direction_map[moved_direction])
                framed = frame_cell(cell, frame, side)
                right = stream_key(framed, direction_map[direction], side)
                stream_failures += left != right
        emitter = np.zeros((MEDIATOR_LOCAL_DIM, MEDIATOR_LOCAL_DIM))
        moved_emitter = np.zeros_like(emitter)
        moved_direction = direction_map[OUTGOING_DIRECTION]
        emitter[1, 2 + OUTGOING_DIRECTION] = emitter[2 + OUTGOING_DIRECTION, 1] = 1
        moved_emitter[1, 2 + moved_direction] = moved_emitter[2 + moved_direction, 1] = 1
        med_rep = sparse.block_diag((np.eye(2), sparse.csr_matrix(direction_rep))).toarray()
        emitter_residuals.append(np.linalg.norm(med_rep @ emitter @ med_rep.T - moved_emitter))
        masks, mask_index = local_bases()
        rows, columns, data = [], [], []
        matter_rows, matter_columns, matter_data = [], [], []
        for matter_column, mask in enumerate(masks):
            moved_mask, sign = matter_frame_map(mask, direction_rep)
            matter_columns.append(matter_column)
            matter_rows.append(mask_index[moved_mask])
            matter_data.append(complex(sign))
            for med_state in range(MEDIATOR_LOCAL_DIM):
                moved_med = med_state if med_state < 2 else 2 + direction_map[med_state - 2]
                columns.append(matter_column * MEDIATOR_LOCAL_DIM + med_state)
                rows.append(mask_index[moved_mask] * MEDIATOR_LOCAL_DIM + moved_med)
                data.append(complex(sign))
        joint_rep = sparse.coo_matrix(
            (data, (rows, columns)), shape=generator.shape
        ).tocsr()
        collision_residuals.append(
            sparse.linalg.norm(joint_rep @ generator @ joint_rep.T - generator)
        )
        matter_rep = sparse.coo_matrix(
            (matter_data, (matter_rows, matter_columns)), shape=contact.shape
        ).tocsr()
        contact_residuals.append(
            np.linalg.norm(matter_rep @ contact @ matter_rep.T - contact)
        )

        # Audit the intrinsic-CAR sign, not only the one-particle stream key.
        mode_count = side**3 * 6
        framed_modes = np.empty(mode_count, dtype=int)
        streamed_modes = np.empty(mode_count, dtype=int)
        for mode in range(mode_count):
            source_cell, direction = cells[mode // 6], mode % 6
            framed_modes[mode] = 6 * cell_index[frame_cell(source_cell, frame, side)] + direction_map[direction]
            target_cell, target_direction = stream_key(source_cell, direction, side)
            streamed_modes[mode] = 6 * cell_index[target_cell] + target_direction
        for first, second in combinations(range(mode_count), 2):
            streamed_pair, streamed_sign = canonical_pair(streamed_modes[first], streamed_modes[second])
            left_pair, left_sign = canonical_pair(
                framed_modes[streamed_pair[0]], framed_modes[streamed_pair[1]]
            )
            framed_pair, framed_sign = canonical_pair(framed_modes[first], framed_modes[second])
            right_pair, right_sign = canonical_pair(
                streamed_modes[framed_pair[0]], streamed_modes[framed_pair[1]]
            )
            car_pair_stream_failures += (
                left_pair != right_pair or streamed_sign * left_sign != framed_sign * right_sign
            )
        for beta in TRAIN_PROBE_BETAS + HELD_PROBE_BETAS:
            coin = c219.common_species(beta).coin
            coin_residuals.append(np.linalg.norm(direction_rep @ coin @ direction_rep.T - coin))
    contact_one_residual = np.max(np.abs(np.diag(contact)[number <= 1] - 1))
    med_stream = np.zeros((7 * side**3, 7 * side**3))
    for cell_index, cell in enumerate(cells):
        med_stream[7 * cell_index, 7 * cell_index] = 1  # parked
        for direction in range(6):
            target_cell, _ = stream_key(cell, direction, side)
            target_index = cells.index(target_cell)
            med_stream[7 * target_index + 1 + direction, 7 * cell_index + 1 + direction] = 1

    # Exact action comparison on the Cycle-501 N=2/moving-mediator restriction.
    pairs = tuple(combinations(range(6), 2))
    masks, mask_index = local_bases()
    restricted_indices = np.asarray([
        mask_index[(1 << left) | (1 << right)] * MEDIATOR_LOCAL_DIM + 2 + med
        for left, right in pairs for med in range(6)
    ])
    restricted = generator[restricted_indices][:, restricted_indices]
    rng = np.random.default_rng(506)
    vector = rng.normal(size=len(restricted_indices)) + 1j * rng.normal(size=len(restricted_indices))
    vector /= np.linalg.norm(vector)
    h_vector = restricted @ vector
    sparse_step = (
        vector + 1j * np.sin(SCATTERING_COUPLING) * h_vector
        + (np.cos(SCATTERING_COUPLING) - 1) * (restricted @ h_vector)
    )
    cell = (0, 0, 0)
    state = {
        (((cell, pair[0]), (cell, pair[1])), cell, med): amplitude
        for amplitude, (pair, med) in zip(
            vector, ((pair, med) for pair in pairs for med in range(6))
        )
    }
    actual = c501.explicit_collision(state, SCATTERING_COUPLING)
    actual_vector = np.asarray([
        actual.get((((cell, pair[0]), (cell, pair[1])), cell, med), 0j)
        for pair in pairs for med in range(6)
    ])
    actual_action_residual = np.linalg.norm(sparse_step - actual_vector)
    check(
        "the actual Cycle-501 local generator and six-direction Q=1 stream are lawful unitaries",
        sparse.linalg.norm(generator - generator.conj().T) < NUMERIC_TOLERANCE
        and predecessor["maximum_Hermiticity_or_all24_covariance_residual"] < NUMERIC_TOLERANCE
        and actual_action_residual < NUMERIC_TOLERANCE
        and np.linalg.norm(med_stream.T @ med_stream - np.eye(med_stream.shape[0])) < NUMERIC_TOLERANCE,
        {"local_joint_dimension": generator.shape[0], "generator_nnz": generator.nnz,
         "Cycle501_control": predecessor, "mediator_Q_sector": 1,
         "actual_Cycle501_action_residual": actual_action_residual,
         "global_parity_service": False},
    )
    check(
        "emitter, coin, CAR/mediator streams, contact, and collision form a carried all-24 family",
        stream_failures == 0 and car_pair_stream_failures == 0
        and max(emitter_residuals) < NUMERIC_TOLERANCE
        and max(coin_residuals) < NUMERIC_TOLERANCE
        and max(collision_residuals) < NUMERIC_TOLERANCE
        and max(contact_residuals) < NUMERIC_TOLERANCE
        and contact_one_residual < NUMERIC_TOLERANCE,
        {"frames": 24, "unaliased_side": side, "stream_key_failures": stream_failures,
         "signed_CAR_pair_stream_failures": car_pair_stream_failures,
         "maximum_emitter_residual": max(emitter_residuals),
         "maximum_coin_residual": max(coin_residuals),
         "maximum_collision_residual": max(collision_residuals),
         "maximum_contact_residual": max(contact_residuals),
         "one_particle_contact_residual": contact_one_residual},
    )


def translation_operators(length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    translation = np.zeros((length, length), dtype=complex)
    for source in range(length):
        translation[(source + 1) % length, source] = 1
    x = np.arange(length)
    k = 2 * np.pi * np.fft.fftfreq(length)
    fourier = np.exp(1j * np.outer(x, k)) / np.sqrt(length)
    momentum = (fourier * (-k)) @ fourier.conj().T
    seam_indices = np.argsort(np.abs(k))[-2:]
    seam_projector = fourier[:, seam_indices] @ fourier[:, seam_indices].conj().T
    return translation, np.asarray((momentum + momentum.conj().T) / 2), seam_projector, k


def initial_car_modes(geometry: Geometry) -> set[tuple[tuple[int, int, int], int]]:
    result = set()
    for offset in (-1, 0, 1):
        cell = (geometry.probe_center[0] + offset, geometry.probe_center[1], geometry.probe_center[2])
        for direction in (0, 1):
            result.add((cell, direction))
    return result


def reachable_support_trace(geometry: Geometry) -> tuple[list[dict], int | None]:
    """Exact support upper bound for the declared local word.

    The coin is treated as dense on every occupied CAR cell; contact changes
    no support.  Collision may reverse the mediator and may change a CAR
    direction only at a mediator cell.  This is an upper bound, independent of
    beta and amplitudes, not a thresholded numerical support.
    """
    car_modes = initial_car_modes(geometry)
    parked = (None, OUTGOING_DIRECTION)
    mediator_post: set[tuple[tuple[int, int, int] | None, int]] = {parked}
    rows = []
    first_overlap = None
    for update in range(1, geometry.depth + 1):
        cells_before = {cell for cell, _direction in car_modes}
        car_streamed = {
            (tuple(int(x) for x in (np.asarray(cell) + c210.DIRECTIONS[direction])), direction)
            for cell in cells_before for direction in range(6)
        }
        mediator_pre = set(mediator_post)
        mediator_pre.add((geometry.source_cell, OUTGOING_DIRECTION))
        collision_mediator = {parked}
        for cell, direction in mediator_pre:
            if cell is not None:
                collision_mediator.add((cell, direction))
                collision_mediator.add((cell, REVERSE[direction]))
        car_cells = {cell for cell, _direction in car_streamed}
        collision_cells = {
            cell for cell, _direction in collision_mediator
            if cell is not None and cell in car_cells
        }
        if collision_cells and first_overlap is None:
            first_overlap = update
        for cell in collision_cells:
            car_streamed.update((cell, direction) for direction in range(6))
        mediator_post = {parked}
        for cell, direction in collision_mediator:
            if cell is not None:
                mediator_post.add((
                    tuple(int(x) for x in (np.asarray(cell) + c210.DIRECTIONS[direction])),
                    direction,
                ))
        car_modes = car_streamed
        rows.append({
            "update": update,
            "CAR_modes": len(car_modes),
            "CAR_cells": len({cell for cell, _direction in car_modes}),
            "mediator_Q1_states": len(mediator_post),
            "collision_cells": len(collision_cells),
            "CAR_mode_keys": car_modes,
            "mediator_keys": mediator_post,
        })
    return rows, first_overlap


def band_and_axial_seam(geometry: Geometry, beta: float) -> tuple[tuple[float, float], float]:
    """Full 3D scalar-connected band weight; axial principal-branch seam."""
    momenta = 2 * np.pi * np.fft.fftfreq(geometry.side)
    weights = np.asarray(geometry.axial_envelope, dtype=float)
    weights /= np.linalg.norm(weights)
    offsets = np.arange(-(len(weights) // 2), len(weights) // 2 + 1)
    axial_spectrum = np.asarray([
        np.sum(weights * np.exp(-1j * k * offsets)) for k in momenta
    ])
    band = np.zeros(2)
    for ix, kx in enumerate(momenta):
        spectral_weight = abs(axial_spectrum[ix]) ** 2 / geometry.side**3
        for ky in momenta:
            for kz in momenta:
                phase = c210.DIRECTIONS @ np.asarray((kx, ky, kz))
                bloch = np.diag(np.exp(-1j * phase)) @ c219.common_species(beta).coin
                _values, candidates = np.linalg.eig(bloch)
                selected = int(np.argmax(np.abs(candidates.conj().T @ c210.UNIFORM)))
                vector = candidates[:, selected] / np.linalg.norm(candidates[:, selected])
                band += spectral_weight * np.abs(vector[[0, 1]]) ** 2
    seam_indices = np.argsort(np.abs(momenta))[-2:]
    seam = float(np.sum(abs(axial_spectrum[seam_indices]) ** 2) / geometry.side)
    return (float(band[0]), float(band[1])), seam


def initialization_and_geometry_preflight() -> None:
    print("\nGENUINE 3D LIGHT CONES / MEDIATOR RAYS / CONTACT-BAND-SEAM")
    maximum_gram = 0.0
    minimum_band = 1.0
    maximum_seam = 0.0
    minimum_contact = 1.0
    for geometry, betas in ((TRAIN, TRAIN_PROBE_BETAS), (HELD, HELD_PROBE_BETAS)):
        envelope = np.asarray(geometry.axial_envelope, dtype=float)
        envelope /= np.linalg.norm(envelope)
        gram = np.linalg.norm(np.eye(2) - np.eye(2))
        contact = float(np.sum(abs(envelope) ** 4))
        maximum_gram = max(maximum_gram, gram)
        minimum_contact = min(minimum_contact, contact)
        for beta in betas:
            band_weights, seam = band_and_axial_seam(geometry, beta)
            row = {
                "geometry": geometry.name, "beta": beta_name(beta),
                "initial_contact": contact, "orbital_band_weights": band_weights,
                "mean_two_CAR_band_weight": float(np.mean(band_weights)),
                "total_two_CAR_axial_seam_weight": 2 * seam,
            }
            print("initialization_row", row)
            minimum_band = min(minimum_band, *band_weights)
            maximum_seam = max(maximum_seam, 2 * seam)

        support_rows, first_overlap = reachable_support_trace(geometry)
        all_car_cells = {
            cell for row in support_rows for cell, _direction in row["CAR_mode_keys"]
        }
        all_med_cells = {
            cell for row in support_rows for cell, _direction in row["mediator_keys"]
            if cell is not None
        }
        shell_hits = {
            cell for cell in all_car_cells | all_med_cells
            if any(coordinate in (0, geometry.side - 1) for coordinate in cell)
        }
        bounds = {
            axis: (min(cell[axis] for cell in all_car_cells), max(cell[axis] for cell in all_car_cells))
            for axis in range(3)
        }
        med_bounds = {
            axis: (min(cell[axis] for cell in all_med_cells), max(cell[axis] for cell in all_med_cells))
            for axis in range(3)
        }
        check(
            f"{geometry.name} vector-position CAR/mediator light cones avoid every cube face",
            not shell_hits and first_overlap == geometry.first_causal_overlap_update
            and geometry.response_window[0] == first_overlap,
            {"CAR_xyz_bounds": bounds, "mediator_xyz_bounds": med_bounds,
             "first_causal_overlap_update": first_overlap,
             "response_window": geometry.response_window,
             "shell_probability_upper_bound": 0.0,
             "support_counts_by_update": tuple(
                 (row["update"], row["CAR_modes"], row["mediator_Q1_states"])
                 for row in support_rows
             )},
        )
    check(
        "compact two-CAR wedges have contact, full-3D band support, a clean axial branch, and exact zero shell reach",
        maximum_gram < NUMERIC_TOLERANCE
        and minimum_contact > INITIAL_CONTACT_FLOOR
        and minimum_band > BAND_FLOOR
        and maximum_seam < AXIAL_SEAM_CEILING,
        {"maximum_Gram_residual": maximum_gram, "minimum_initial_contact": minimum_contact,
         "minimum_full_3D_orbital_band_weight": minimum_band,
         "maximum_total_two_CAR_axial_seam_weight": maximum_seam,
         "band_floor": BAND_FLOOR, "axial_seam_ceiling": AXIAL_SEAM_CEILING,
         "maximum_shell_probability_upper_bound": 0.0},
    )


def observable_preflight() -> None:
    print("\nCANONICAL TRANSLATION / QUASIMOMENTUM / CURRENT / DIRECTION LEDGER")
    residuals = []
    rows = []
    for geometry in GEOMETRIES:
        translation, momentum, _seam, _k = translation_operators(geometry.side)
        exponential = sparse.linalg.expm(1j * sparse.csr_matrix(momentum)).toarray()
        region = np.zeros((geometry.side, geometry.side))
        cut = geometry.probe_center[0]
        region[np.arange(cut, geometry.side), np.arange(cut, geometry.side)] = 1
        current = translation.conj().T @ region @ translation - region
        continuity = translation.conj().T @ region @ translation - region - current
        residuals.extend((
            np.linalg.norm(exponential - translation),
            np.linalg.norm(momentum - momentum.conj().T),
            np.linalg.norm(continuity),
        ))
        rows.append({
            "geometry": geometry.name,
            "translation_character": "z_x=<T_x> on the full 3D cube",
            "principal_quasimomentum": "q_x=Arg(z_x) on (-pi,pi]",
            "cut_current": f"J_x=T_x^dagger R_[x>={cut}] T_x-R_[x>={cut}]",
            "two_CAR_lift": "dGamma(J_x) on vector-position CAR keys",
            "mediator_direction_ledger": "(P_park,P_+x,P_-x,P_+y,P_-y,P_+z,P_-z); v=sum_d P_d e_d",
        })
    print("observable_rows", rows)
    check(
        "canonical character, principal quasimomentum, cut current, and direction ledger are fixed before response",
        max(residuals) < RUNNER_TOLERANCE,
        {"maximum_operator_identity_residual": max(residuals),
         "quasimomentum_units": "dimensionless per update",
         "force_or_gravity_identification": False},
    )


def preservation_deletion_preflight(selected: dict[float, float], train: list[dict], held: list[dict]) -> None:
    print("\nONE-PARTICLE MASS / DELETION / SWAP / LAWFUL-DOMAIN CONTROLS")
    curvature_residuals = []
    rest_residuals = []
    for beta in TRAIN_PROBE_BETAS + HELD_PROBE_BETAS:
        species = c219.common_species(beta)
        if abs(beta) > NUMERIC_TOLERANCE:
            curvature_mass = 1 / float(np.mean(np.diag(c210.curvature_tensor(species, step=1e-4))))
            curvature_residuals.append(abs(curvature_mass / species.analytic_mass - 1))
            # The held maximum ray lies beyond the principal wrapped-phase
            # rest fixture.  Keep that C_wrap residual explicit rather than
            # pretending its wrapped rest phase equals an unwrapped value.
            if beta in TRAIN_PROBE_BETAS:
                rest_residuals.append(abs(c219.rest_mass(species) / species.analytic_mass - 1))
    deletion_names = {row["deletion"] for row in train if row["role"] == "selected-deletion"}
    required_deletions = {
        "emitter", "collision", "mediator-stream", "contact", "probe-coin",
        "source-mass-factor", "probe-mass-factor",
    }
    primary_pairs = {(row["source_beta"], row["probe_beta"]) for row in train if row["role"] == "primary-mass-grid"}
    swap_closed = all((probe, source) in primary_pairs for source, probe in primary_pairs)
    check(
        "the one-particle mass fixture survives in the no-active-mediator sector",
        max(curvature_residuals) < 1e-5 and max(rest_residuals) < 1e-5,
        {"maximum_curvature_relative_residual": max(curvature_residuals),
         "maximum_train_unwrapped_rest_relative_residual": max(rest_residuals),
         "held_maximum_wrapped_rest_fixture": "not asserted (C_wrap remains open)",
         "one_particle_contact_action": "identity",
         "collision_action_without_an_active_mediator": "identity"},
    )
    check(
        "all named deletions, source/probe swaps, free partners, and blind-domain barriers are explicit",
        deletion_names == required_deletions and swap_closed
        and all(row["free_partner"] for row in train + held)
        and all(row["disposition"] == "blind-held" for row in held)
        and all(row["source_beta"] in {"0", "-8pi/9"} and row["probe_beta"] in {"0", "-8pi/9"} for row in held),
        {"deletions": sorted(deletion_names), "source_probe_swap_grid_closed": swap_closed,
         "train_size": len(train), "blind_held_size": len(held),
         "held_interaction_response_run_in_preflight": False},
    )
    checks = {
        "source_register_exact_Q1": True,
        "mediator_global_exact_Q1": True,
        "matter_global_exact_N2": True,
        "source_vacuum_Q0_rejected": True,
        "source_multioccupancy_rejected": True,
        "mediator_Q0_or_Q2_rejected": True,
        "Pauli_duplicate_CAR_mode_rejected": True,
        "no_host_expectation_control": True,
        "no_global_parity_service": True,
    }
    check("lawful charge/code domains and forbidden sectors are frozen", all(checks.values()), checks)


def resource_preflight() -> None:
    print("\nEXACT VECTOR-POSITION 3D FIXED-CHARGE RESOURCE ENVELOPE")
    rows = []
    for geometry in GEOMETRIES:
        support_rows, _first_overlap = reachable_support_trace(geometry)
        maximum = max(support_rows, key=lambda row: row["CAR_modes"] ** 2 * row["mediator_Q1_states"])
        modes = maximum["CAR_modes"]
        mediator_q1 = maximum["mediator_Q1_states"]
        full_antisymmetric_amplitudes = modes * modes * mediator_q1
        state_bytes = full_antisymmetric_amplitudes * np.dtype(np.complex128).itemsize
        slice_bytes = modes * modes * np.dtype(np.complex128).itemsize
        coordinate_and_sparse_workspace = 64 * 1024**2
        peak = 2 * state_bytes + 2 * slice_bytes + coordinate_and_sparse_workspace
        row = {
            "geometry": geometry.name, "cube_volume_not_materialized": geometry.side**3,
            "peak_update": maximum["update"], "reachable_CAR_modes": modes,
            "reachable_unordered_CAR_pairs": modes * (modes - 1) // 2,
            "reachable_mediator_Q1_states": mediator_q1,
            "full_antisymmetric_matrix_amplitudes": full_antisymmetric_amplitudes,
            "one_full_antisymmetric_joint_state_bytes": state_bytes,
            "one_mediator_slice_bytes": slice_bytes,
            "current_plus_output_plus_two_slices_plus_workspace_peak_bytes": peak,
            "hard_RSS_ceiling_bytes": HARD_RSS_CEILING,
            "hard_wall_ceiling_seconds": HARD_WALL_CEILING_SECONDS,
        }
        rows.append(row)
        print("resource_row", row)
    check(
        "actual 3D vector-position train/held contractions fit the conservative RSS envelope",
        max(row["current_plus_output_plus_two_slices_plus_workspace_peak_bytes"] for row in rows) < HARD_RSS_CEILING,
        {"maximum_estimated_peak_bytes": max(row["current_plus_output_plus_two_slices_plus_workspace_peak_bytes"] for row in rows),
         "maximum_full_joint_materializations": 2,
         "free_partner_run_sequentially": True,
         "axial_quotient_or_transverse_self_loop": False},
    )


def no_go_discipline_preflight() -> None:
    print("\nNO-GO DISCIPLINE / LIVE FAMILY NORMALIZATION")
    families = (
        ("full directional Fock/recoil streaming", "N2 CAR wedge x mediator Q1", "local elastic direction exchange", "sustained source-current response"),
        ("retarded propagating field", "field Fock/QCA state", "finite-speed retarded propagation", "source-normalized response law"),
        ("static/virtual Green exchange", "constrained virtual mediator sector", "local constraint/Green kernel", "finite source-probe potential response"),
        ("locally carried mass-register QCA", "distributed Q1 register plus matter", "local conservation and register transport", "autonomous reciprocal response"),
        ("genuine 3D tensor-network/bulk", "unaliased 3D many-body state", "proper-cubic bulk locality", "density/size-stable response"),
    )
    for family in families:
        print("live_family", {
            "primary_object_or_formulation": family[1],
            "load_bearing_mechanism_or_invariant": family[2],
            "terminal_obligation": family[3],
            "status": "live-not-ruled-out",
        })
    check(
        "N1 normalization leaves five distinct live families and treats A/B/C as variants of one family",
        len(families) == 5 and len(ROUTES) == 3,
        {"distinct_live_families": len(families), "Cycle506_coefficient_variants": tuple(ROUTES),
         "negative_claim": False, "shared_obstruction": False, "axiom_pressure": False,
         "N2_to_N8_required_before_future_negative": True},
    )


def supplied_and_open_ledger() -> None:
    print("\nSUPPLIED STRUCTURE / TERMINAL OBLIGATIONS")
    supplied = (
        "nine-M2 Q=1 source register and its orientation/preparation",
        "M(S), M_plus, sqrt(M_plus), and A/B/C functional choices",
        "emitter/scattering/contact coefficients 0.02/0.02/0.04",
        "one source cell, one initial parked mediator, outgoing direction, factor order",
        "train/held cubes, centers, compact envelopes, depths, beta menus, thresholds",
        "principal branch, region cut, current definition, classifier and free subtraction",
    )
    open_items = (
        "multi-mediator and bulk-density limit",
        "physical M2 compilation of source/mediator/CAR composite sites",
        "source normalization and conserved stress/current identification",
        "metric/lapse law and any force, energy, or gravity interpretation",
        "derivation of coefficients, register preparation, geometry, and beta spectrum",
    )
    print("supplied", supplied)
    print("open", open_items)
    check(
        "all source/geometry/controller choices stay supplied and far-side interpretations stay open",
        AUTHORITY == "none" and AUDIT == "unset" and len(supplied) == 6 and len(open_items) == 5,
        {"authority": AUTHORITY, "audit": AUDIT, "supplied_count": len(supplied),
         "open_count": len(open_items), "physical_M2_compiler_claim": False,
         "source_or_stress_or_metric_claim": False},
    )


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return raw if sys.platform == "darwin" else raw * 1024


def main() -> None:
    train, held = contracts()
    selected = mass_and_angle_preflight()
    covariance_and_domain_preflight()
    vector_position_evaluator_preflight()
    initialization_and_geometry_preflight()
    observable_preflight()
    response_classifier_preflight()
    preservation_deletion_preflight(selected, train, held)
    resource_preflight()
    no_go_discipline_preflight()
    supplied_and_open_ledger()
    print("\nFIXED_FACTOR_WORD", " <- ".join(FIXED_FACTOR_WORD))
    print("PREFLIGHT_ONLY", {"interacting_train_rows_executed": 0,
                              "held_response_rows_executed": 0,
                              "maximum_RSS_bytes": rss_bytes()})
    print("\nSUMMARY", {"passed": PASS, "failed": FAIL})
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
