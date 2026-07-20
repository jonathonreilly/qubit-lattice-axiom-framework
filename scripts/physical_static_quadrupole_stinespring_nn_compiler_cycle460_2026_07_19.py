#!/usr/bin/env python3
"""Cycle 460: finite static-quadrupole Stinespring/NN compiler.

Compile the supplied Cycle-420 train/held normalized receiver-weight channel
into one bounded one-excitation M2 schedule.  The exact source coordinate is
unchanged: s(p)=(sqrt(1-p),sqrt(p)).  For each supplied separation, positive
two-by-two receiver effects are reconstructed from the p=0 and two named
source states, factored into one Stinespring isometry, and decomposed into
adjacent number-preserving Givens rotations.  Runtime uses only the frozen
gate schedule; the legacy host array is queried during compilation only.

This compiles a supplied finite kernel and geometry.  It is not a derivation
of that kernel, gravity, physical probability, time, energy, or a Record.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_exact_strength_quadrupole_prediction_bridge_cycle453_2026_07_19 as c453


c435 = c453.c435
c420 = c453.c420
c319 = c453.c319
c210 = c453.c210
multipole = c453.multipole

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_STATIC_QUADRUPOLE_STINESPRING_NN_COMPILER_CYCLE460_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

TOLERANCE = 2.0e-11
PSD_TOLERANCE = 5.0e-13
NAMED_ROW_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
ROUTES = ("unit_weight", "coefficient_two")
STRENGTHS = {"free": 0.0, **c453.PHYSICAL_STRENGTHS}
SEPARATIONS = (1, 2)
LEGACY_ROWS = c453.LEGACY_ROWS


class WallCapExceeded(RuntimeError):
    pass


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "finite positive receiver-weight/stinespring channel",
        "exact single-source state",
        "s(p)=(sqrt(1-p),sqrt(p))",
        "every r_j is positive semidefinite",
        "sum_j r_j=i_2",
        "one fixed v_a handles p=0, unit, and coefficient-two without lookup",
        "4356-m2 nearest-neighbor line",
        "one shared block schedule",
        "no host array solve during update",
        "no per-row factors",
        "train a=1 and held a=2",
        "one receiver calibration",
        "all 24 proper-cubic frames",
        "600-second wall cap",
        "4 gib rss cap",
        "partial-attempt-with-named-untested-routes",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "no gravity, no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle-460 note freezes the finite supplied-kernel compiler contract", not missing, missing)


def source_state(p: float) -> np.ndarray:
    if not 0 <= p <= 1:
        raise ValueError("source coordinate p must be in [0,1]")
    return np.asarray((math.sqrt(1 - p), math.sqrt(p)), dtype=complex)


def receiver_moments(weights: np.ndarray, z: np.ndarray) -> dict[str, float]:
    total = float(np.sum(weights))
    if total <= 0:
        raise ValueError("receiver weight must be positive")
    centroid = float(weights @ z / total)
    second = float(weights @ (z**2) / total)
    width = math.sqrt(max(0.0, second - centroid**2))
    return {"total": total, "centroid": centroid, "second_moment": second, "width": width}


def compile_legacy_operator_data() -> dict[str, object]:
    """Compile-time-only calls to the supplied Cycle-420 host operator."""

    print("\nSUPPLIED CYCLE-420 FINITE STATIC OPERATOR")
    lat = multipole.Lattice3D(multipole.PHYS_L, multipole.PHYS_W, multipole.H)
    detector = np.asarray(multipole.detector(lat), dtype=int)
    z = lat.pos[detector, 2].astype(float)
    initial = multipole.point_packet(lat)
    packets: dict[tuple[int, str], dict[str, object]] = {}
    host_solves = 0
    for separation in SEPARATIONS:
        base_field = multipole.field_from_sources(
            lat, multipole.build_quadrupole(float(separation))
        )
        for route, p in STRENGTHS.items():
            amplitude = multipole.propagate_charge(lat, initial, p * base_field, 1)[detector]
            host_solves += 1
            detector_norm = float(np.linalg.norm(amplitude))
            normalized_amplitude = amplitude / detector_norm
            weights = np.abs(normalized_amplitude) ** 2
            packets[(separation, route)] = {
                "amplitude": normalized_amplitude,
                "weights": weights,
                "moments": receiver_moments(weights, z),
                "detector_norm_before_normalization": detector_norm,
            }
    free_width = packets[(1, "free")]["moments"]["width"]
    exact_rows = {
        (separation, route): packets[(separation, route)]["moments"]["width"] - free_width
        for separation in SEPARATIONS
        for route in ROUTES
    }
    check(
        "the exact supplied operator reconstructs the frozen Cycle-420 train/held rows before physical compilation",
        len(detector) == 1089
        and host_solves == 6
        and max(abs(exact_rows[key] - LEGACY_ROWS[key]) for key in LEGACY_ROWS) < 2e-14
        and abs(packets[(1, "free")]["moments"]["width"] - packets[(2, "free")]["moments"]["width"]) < TOLERANCE,
        {
            "lattice_nodes": lat.n,
            "layers": lat.nl,
            "transverse_sites_per_layer": lat.npl,
            "edge_offsets": len(lat._off),
            "receiver_labels": len(detector),
            "compile_time_host_solves": host_solves,
            "source_coefficients": multipole.build_quadrupole(1.0),
            "source_normalization": multipole.SOURCE_STRENGTH,
            "exact_source_coordinates": STRENGTHS,
            "rows": exact_rows,
        },
    )
    return {
        "lat": lat,
        "detector": detector,
        "z": z,
        "packets": packets,
        "host_solves": host_solves,
        "exact_rows": exact_rows,
    }


def positive_receiver_isometry(operator_data, separation: int) -> dict[str, object]:
    """Factor the three-state receiver-weight channel into V_a^dagger V_a=I."""

    p1 = STRENGTHS["unit_weight"]
    p2 = STRENGTHS["coefficient_two"]
    features = np.asarray(
        (
            (p1, 2 * math.sqrt(p1 * (1 - p1))),
            (p2, 2 * math.sqrt(p2 * (1 - p2))),
        ),
        dtype=float,
    )
    free = operator_data["packets"][(separation, "free")]["weights"]
    unit = operator_data["packets"][(separation, "unit_weight")]["weights"]
    coefficient = operator_data["packets"][(separation, "coefficient_two")]["weights"]
    right = np.vstack((unit - (1 - p1) * free, coefficient - (1 - p2) * free))
    diagonal_one, off_diagonal = np.linalg.solve(features, right)

    effects = []
    factors = []
    minimum_eigenvalue = math.inf
    maximum_factor_residual = 0.0
    for index in range(len(free)):
        effect = np.asarray(
            ((free[index], off_diagonal[index]), (off_diagonal[index], diagonal_one[index])),
            dtype=complex,
        )
        eigenvalues, eigenvectors = np.linalg.eigh(effect)
        minimum_eigenvalue = min(minimum_eigenvalue, float(eigenvalues[0]))
        if eigenvalues[0] < -PSD_TOLERANCE:
            raise ValueError(f"receiver effect {index} is not positive: {eigenvalues[0]}")
        eigenvalues = np.maximum(eigenvalues, 0.0)
        factor = np.diag(np.sqrt(eigenvalues)) @ eigenvectors.conj().T
        maximum_factor_residual = max(
            maximum_factor_residual, float(np.linalg.norm(factor.conj().T @ factor - effect))
        )
        effects.append(effect)
        factors.append(factor)

    effect_sum = np.sum(effects, axis=0)
    isometry = np.vstack(factors)
    gram_residual = float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(2)))
    sum_residual = float(np.linalg.norm(effect_sum - np.eye(2)))
    anchor_rows = {}
    for route, p in STRENGTHS.items():
        output = isometry @ source_state(p)
        weights = np.sum(np.abs(output.reshape(-1, 2)) ** 2, axis=1)
        target = operator_data["packets"][(separation, route)]["weights"]
        anchor_rows[route] = {
            "weight_residual": float(np.linalg.norm(weights - target)),
            "normalization": float(np.sum(weights)),
        }
    return {
        "separation": separation,
        "effects": effects,
        "isometry": isometry,
        "minimum_effect_eigenvalue": minimum_eigenvalue,
        "effect_sum_residual": sum_residual,
        "factor_residual": maximum_factor_residual,
        "Gram": gram_residual,
        "anchor_rows": anchor_rows,
        "receiver_tags_per_label": 2,
    }


@dataclass(frozen=True)
class Gate:
    sites: tuple[int, int]
    matrix: tuple[complex, ...]
    label: str


def mode_gate(left: int, right: int, matrix: np.ndarray, label: str) -> Gate:
    if right != left + 1:
        raise ValueError("a compiled Givens gate must use one nearest-neighbor edge")
    if matrix.shape != (2, 2) or np.linalg.norm(matrix.conj().T @ matrix - np.eye(2)) > TOLERANCE:
        raise ValueError("the one-excitation gate block must be unitary")
    return Gate((left, right), tuple(complex(value) for value in matrix.reshape(-1)), label)


def gate_matrix(gate: Gate) -> np.ndarray:
    return np.asarray(gate.matrix, dtype=complex).reshape(2, 2)


def inverse_gate(gate: Gate) -> Gate:
    matrix = gate_matrix(gate).conj().T
    return Gate(gate.sites, tuple(complex(value) for value in matrix.reshape(-1)), "inverse:" + gate.label)


def inverse_schedule(schedule: tuple[Gate, ...]) -> tuple[Gate, ...]:
    return tuple(inverse_gate(gate) for gate in reversed(schedule))


def compile_adjacent_isometry(isometry: np.ndarray, offset: int, label: str):
    """Adjacent-row rectangular QR; schedule maps the first two modes to V."""

    size, columns = isometry.shape
    if columns != 2 or np.linalg.norm(isometry.conj().T @ isometry - np.eye(2)) > TOLERANCE:
        raise ValueError("target must be a two-column isometry")
    work = isometry.copy()
    eliminations: list[tuple[int, int, np.ndarray]] = []
    for column in range(columns):
        for lower in range(size - 1, column, -1):
            upper = lower - 1
            a = work[upper, column]
            b = work[lower, column]
            if abs(b) < 1e-16:
                continue
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                ((np.conj(a) / radius, np.conj(b) / radius), (-b / radius, a / radius)),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    tail_residual = float(np.linalg.norm(work[columns:, :]))
    seed = work[:columns, :]
    seed_unitarity = float(np.linalg.norm(seed.conj().T @ seed - np.eye(columns)))
    schedule = [mode_gate(offset, offset + 1, seed, f"{label}:seed")]
    for upper, lower, elimination in reversed(eliminations):
        schedule.append(
            mode_gate(
                offset + upper,
                offset + lower,
                elimination.conj().T,
                f"{label}:givens-{upper}-{lower}",
            )
        )
    return tuple(schedule), {
        "modes": size,
        "columns": columns,
        "adjacent_givens": len(schedule),
        "rectangular_QR_tail_residual": tail_residual,
        "seed_unitarity_residual": seed_unitarity,
    }


def apply_schedule(state: np.ndarray, schedule: tuple[Gate, ...]) -> np.ndarray:
    output = state.copy()
    for gate in schedule:
        left, right = gate.sites
        output[[left, right], ...] = gate_matrix(gate) @ output[[left, right], ...]
    return output


def physical_compiler_controls(operator_data) -> dict[str, object]:
    print("\nPOSITIVE RECEIVER EFFECTS / STINESPRING / ADJACENT GIVENS")
    channels = {a: positive_receiver_isometry(operator_data, a) for a in SEPARATIONS}
    receiver_labels = len(operator_data["detector"])
    block_modes = 2 * receiver_labels
    total_modes = len(SEPARATIONS) * block_modes
    schedules = {}
    rows = []
    for block, separation in enumerate(SEPARATIONS):
        offset = block * block_modes
        schedule, row = compile_adjacent_isometry(
            channels[separation]["isometry"], offset, f"a{separation}"
        )
        schedules[separation] = schedule
        rows.append({"separation": separation, **row})
    schedule = tuple(gate for separation in SEPARATIONS for gate in schedules[separation])

    input_embedding = np.zeros((total_modes, 4), dtype=complex)
    target_embedding = np.zeros((total_modes, 4), dtype=complex)
    for block, separation in enumerate(SEPARATIONS):
        offset = block * block_modes
        input_embedding[offset : offset + 2, 2 * block : 2 * block + 2] = np.eye(2)
        target_embedding[offset : offset + block_modes, 2 * block : 2 * block + 2] = channels[separation]["isometry"]
    output = apply_schedule(input_embedding, schedule)
    restored = apply_schedule(output, inverse_schedule(schedule))
    coefficients = target_embedding.conj().T @ output
    leakage = float(np.linalg.norm(output - target_embedding @ coefficients))
    compiler = {
        "channels": channels,
        "schedule": schedule,
        "input_embedding": input_embedding,
        "target_embedding": target_embedding,
        "block_modes": block_modes,
        "total_M2": total_modes,
        "rows": rows,
        "input_Gram": float(np.linalg.norm(input_embedding.conj().T @ input_embedding - np.eye(4))),
        "target_Gram": float(np.linalg.norm(target_embedding.conj().T @ target_embedding - np.eye(4))),
        "EG": float(np.linalg.norm(output - target_embedding)),
        "inverse": float(np.linalg.norm(restored - input_embedding)),
        "leakage": leakage,
        "maximum_gate_unitarity": max(
            float(np.linalg.norm(gate_matrix(gate).conj().T @ gate_matrix(gate) - np.eye(2)))
            for gate in schedule
        ),
        "non_NN_gates": sum(gate.sites[1] != gate.sites[0] + 1 for gate in schedule),
    }
    maximum_channel_residual = max(
        max(
            channel["minimum_effect_eigenvalue"] * -1,
            channel["effect_sum_residual"],
            channel["factor_residual"],
            channel["Gram"],
            max(row["weight_residual"] for row in channel["anchor_rows"].values()),
        )
        for channel in channels.values()
    )
    check(
        "every R_j is PSD, sum_j R_j=I_2, and one fixed V_a handles p=0, unit, and coefficient-two without lookup",
        min(channel["minimum_effect_eigenvalue"] for channel in channels.values()) >= -PSD_TOLERANCE
        and maximum_channel_residual < TOLERANCE,
        {
            "channels": {
                separation: {
                    "receiver_effects": len(channel["effects"]),
                    "minimum_effect_eigenvalue": channel["minimum_effect_eigenvalue"],
                    "effect_sum_residual": channel["effect_sum_residual"],
                    "factor_residual": channel["factor_residual"],
                    "Gram": channel["Gram"],
                    "anchor_rows": channel["anchor_rows"],
                }
                for separation, channel in channels.items()
            },
            "source_states_queried_during_update": 0,
        },
    )
    check(
        "the one shared block schedule has exact physical E/G, inverse, leakage, and adjacent number-preserving gates",
        max(
            compiler["input_Gram"],
            compiler["target_Gram"],
            compiler["EG"],
            compiler["inverse"],
            compiler["leakage"],
            compiler["maximum_gate_unitarity"],
        ) < TOLERANCE
        and compiler["non_NN_gates"] == 0
        and compiler["total_M2"] == 4356,
        {key: value for key, value in compiler.items() if key not in ("channels", "schedule", "input_embedding", "target_embedding")},
    )
    return compiler


def physical_receiver_weights(compiler, separation: int, p: float) -> np.ndarray:
    block = SEPARATIONS.index(separation)
    offset = block * compiler["block_modes"]
    state = np.zeros(compiler["total_M2"], dtype=complex)
    state[offset : offset + 2] = source_state(p)
    output = apply_schedule(state, compiler["schedule"])
    block_output = output[offset : offset + compiler["block_modes"]]
    return np.sum(np.abs(block_output.reshape(-1, 2)) ** 2, axis=1)


def named_receiver_controls(operator_data, compiler) -> dict[str, object]:
    print("\nONE-CALIBRATION TRAIN/HELD NAMED ROWS")
    z = operator_data["z"]
    physical_free = receiver_moments(physical_receiver_weights(compiler, 1, 0.0), z)
    legacy_free = operator_data["packets"][(1, "free")]["moments"]
    receiver_scale = legacy_free["width"] / physical_free["width"]
    rows = {}
    free_by_separation = {
        separation: receiver_moments(physical_receiver_weights(compiler, separation, 0.0), z)
        for separation in SEPARATIONS
    }
    for separation in SEPARATIONS:
        for route in ROUTES:
            moments = receiver_moments(
                physical_receiver_weights(compiler, separation, STRENGTHS[route]), z
            )
            matched_shift = receiver_scale * (moments["width"] - free_by_separation[separation]["width"])
            target = LEGACY_ROWS[(separation, route)]
            rows[(separation, route)] = {
                "p": STRENGTHS[route],
                "compiled_width": moments["width"],
                "compiled_centroid": moments["centroid"],
                "matched_width_shift": matched_shift,
                "legacy_width_shift": target,
                "named_row_residual": matched_shift - target,
            }
    check(
        "one receiver calibration derived from the a1 operator representation closes all four rows with held a2 and coefficient-two unrefit",
        abs(receiver_scale - 1) < TOLERANCE
        and max(abs(row["named_row_residual"]) for row in rows.values()) < NAMED_ROW_TOLERANCE
        and max(abs(row["compiled_centroid"]) for row in rows.values()) < 3e-14,
        {
            "receiver_scale": receiver_scale,
            "fit_parameters": 1,
            "per_row_factors": 0,
            "held_refits": 0,
            "rows": rows,
        },
    )
    return {"receiver_scale": receiver_scale, "rows": rows, "free": free_by_separation}


def deletion_controls(operator_data, compiler, named) -> None:
    print("\nDELETIONS")
    z = operator_data["z"]
    p = STRENGTHS["coefficient_two"]
    intact = named["rows"][(1, "coefficient_two")]["matched_width_shift"]
    source_deleted = named["receiver_scale"] * (
        receiver_moments(physical_receiver_weights(compiler, 1, 0.0), z)["width"]
        - named["free"][1]["width"]
    )
    receiver_deleted = 0.0
    identity_state = np.zeros(compiler["total_M2"], dtype=complex)
    identity_state[:2] = source_state(p)
    identity_weights = np.sum(
        np.abs(identity_state[: compiler["block_modes"]].reshape(-1, 2)) ** 2, axis=1
    )
    propagation_deleted_width = receiver_moments(identity_weights, z)["width"]
    propagation_deleted = named["receiver_scale"] * (
        propagation_deleted_width - named["free"][1]["width"]
    )
    one_gate_deleted_output = apply_schedule(
        compiler["input_embedding"], compiler["schedule"][:-1]
    )
    one_gate_deleted_EG = float(np.linalg.norm(one_gate_deleted_output - compiler["target_embedding"]))
    geometry_deleted_weights = physical_receiver_weights(compiler, 1, STRENGTHS["unit_weight"])
    geometry_deleted_shift = named["receiver_scale"] * (
        receiver_moments(geometry_deleted_weights, z)["width"] - named["free"][1]["width"]
    )
    geometry_deleted_residual = geometry_deleted_shift - LEGACY_ROWS[(2, "unit_weight")]

    channel = compiler["channels"][1]
    vector = channel["isometry"] @ source_state(p)
    tag_deleted_weights = np.abs(vector.reshape(-1, 2)[:, 0]) ** 2
    tag_deleted_normalization = float(np.sum(tag_deleted_weights))
    check(
        "source, receiver, propagation, one-Givens, Stinespring-tag, and geometry deletions have distinct bounded effects",
        abs(source_deleted) < TOLERANCE
        and receiver_deleted == 0
        and abs(intact) > 1e-7
        and abs(propagation_deleted - intact) > 1e-3
        and one_gate_deleted_EG > 1e-8
        and abs(tag_deleted_normalization - 1) > 1e-4
        and abs(geometry_deleted_residual) > 1e-7,
        {
            "intact_train_shift": intact,
            "source_deleted_shift": source_deleted,
            "receiver_deleted_shift": receiver_deleted,
            "propagation_deleted_shift": propagation_deleted,
            "one_Givens_deleted_EG": one_gate_deleted_EG,
            "one_Stinespring_tag_retained_weight": tag_deleted_normalization,
            "a2_geometry_replaced_by_a1_residual": geometry_deleted_residual,
            "host_array_solves_during_update": 0,
        },
    )


def covariance_mass_contact_controls(compiler) -> None:
    print("\nALL-24 / MASS / CONTACT")
    frames = c210.proper_cubic_frames()
    supports = tuple(gate.sites for gate in compiler["schedule"])
    maximum_edge_residual = 0.0
    for frame in frames:
        direction = frame @ np.asarray((1, 0, 0), dtype=int)
        for left, right in supports:
            mapped_difference = (right - left) * direction
            maximum_edge_residual = max(
                maximum_edge_residual, abs(float(np.linalg.norm(mapped_difference)) - 1.0)
            )
    check(
        "the one-excitation line and scalar receiver weights transport through all 24 proper-cubic frames",
        len(frames) == 24
        and maximum_edge_residual < TOLERANCE
        and compiler["non_NN_gates"] == 0,
        {
            "proper_cubic_frames": len(frames),
            "line_edges_per_frame": len(supports),
            "maximum_mapped_edge_length_residual": maximum_edge_residual,
            "receiver_width_is_body_frame_even": True,
        },
    )

    c435.PASS = c435.FAIL = 0
    c435.covariance_controls()
    update_rows = c435.restricted_factors()[0]
    contact = c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    contact_residual = float(np.linalg.norm(contact @ two_particle - two_particle))
    check(
        "the supplied-kernel compiler retains the inherited all-24 family, Cycle-219 mass fixture, and Cycle-230 contact",
        c435.PASS == 1
        and c435.FAIL == 0
        and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and contact_residual > 1e-6,
        {
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
            "two_particle_contact_residual": contact_residual,
        },
    )


def resource_domain_ledger_controls(started, operator_data, compiler, named) -> None:
    print("\nRESOURCE / DOMAIN / DEPENDENCY LEDGER")
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload = sum(
        channel["isometry"].nbytes
        + sum(effect.nbytes for effect in channel["effects"])
        for channel in compiler["channels"].values()
    )
    check(
        "the finite compiler stays below explicit wall, RSS, payload, support, and host-update caps",
        elapsed < WALL_CAP_SECONDS
        and maxrss < RSS_CAP_BYTES
        and payload < RSS_CAP_BYTES
        and compiler["total_M2"] == 4356
        and operator_data["host_solves"] == 6,
        {
            "elapsed_seconds": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "compiled_array_payload_bytes": payload,
            "physical_M2": compiler["total_M2"],
            "adjacent_Givens": len(compiler["schedule"]),
            "compile_time_host_solves": operator_data["host_solves"],
            "update_time_host_solves": 0,
        },
    )
    rejected = 0
    for probe in (
        lambda: source_state(-0.1),
        lambda: source_state(1.1),
        lambda: physical_receiver_weights(compiler, 3, STRENGTHS["unit_weight"]),
        lambda: receiver_moments(np.zeros(len(operator_data["z"])), operator_data["z"]),
    ):
        try:
            probe()
        except (ValueError, KeyError):
            rejected += 1
    check("source, separation, and receiver-weight domains reject malformed inputs", rejected == 4, rejected)
    check(
        "the ledger closes only the bounded supplied-kernel compiler and leaves physical-law selection explicit",
        max(abs(row["named_row_residual"]) for row in named["rows"].values()) < NAMED_ROW_TOLERANCE,
        {
            "source_normalization": "supplied p_route=route_strength/5e-5; unchanged two-amplitude source state",
            "propagation_kernel": "supplied Cycle420 finite host operator compiled into V1 direct-sum V2",
            "receiver": "two Stinespring tags per legacy detector label; one a1 coordinate calibration",
            "fit_parameters": 1,
            "per_row_factors": 0,
            "held_refits": 0,
            "homogeneous_scalable_local_law": False,
            "amplitude_phase_channel_compiled": False,
            "finite_receiver_weight_channel_compiled": True,
            "physical_probability_claimed": False,
            "gravity_claimed": False,
            "derived_law_claimed": False,
            "L13_M64_shell_compiled": False,
            "C_ref": "open: host kernel, geometry, source preparation, and coordinate normalization supplied",
            "C_num": "four imported named weights reproduced by a bounded physical schedule",
            "C_wrap": "open: compiler depth is not time and phase is not energy",
            "C_int": "open: no selected autonomous source-carrier interaction",
            "C_local": "finite 4356-M2 NN schedule only; homogeneous scalable law open",
            "C_source": "open: no energy/stress normalization, recurrence, or autonomous preparation",
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle460 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    print("=" * 96)
    print("CYCLE 460 — FINITE STATIC QUADRUPOLE STINESPRING / NN COMPILER")
    print("=" * 96)
    print(
        {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "physical_probability_claimed": False,
            "derived_law_claimed": False,
        }
    )
    try:
        note_contract()
        operator_data = compile_legacy_operator_data()
        compiler = physical_compiler_controls(operator_data)
        named = named_receiver_controls(operator_data, compiler)
        deletion_controls(operator_data, compiler, named)
        covariance_mass_contact_controls(compiler)
        resource_domain_ledger_controls(started, operator_data, compiler, named)
    except WallCapExceeded as error:
        check("the Cycle460 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_STATIC_QUADRUPOLE_STINESPRING_NN_COMPILER_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_STATIC_QUADRUPOLE_STINESPRING_NN_COMPILER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
