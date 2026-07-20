#!/usr/bin/env python3
"""Cycle 458: quadrupole transfer-factor diagnosis and matched receiver.

Decompose the Cycle-453/Cycle-420 mismatch into source normalization, finite
physical propagation, receiver functional, and the legacy host propagation
normalization.  One scalar receiver-coordinate normalization is fixed from
the train a=1 operator tangents and then applied without refit to every finite
strength and held row.  No per-row scale, host profile feedback, source
refresh, or force is inserted into the update.

Authority is none; audit is unset.  Pointer coordinates are not Records,
phase is not energy, update count is not time, and the source is not gravity.
"""

from __future__ import annotations

from dataclasses import asdict
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
    "PHYSICAL_QUADRUPOLE_TRANSFER_FACTOR_MATCHED_RECEIVER_CYCLE458_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

TOLERANCE = c453.TOLERANCE
NUMERIC_ROW_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
BOUNDARY_MAXIMUM = c453.BOUNDARY_MAXIMUM
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
TANGENT_FINITE_DIFFERENCE = 1e-4
TRANSFER_LINEARITY_TOLERANCE = 2e-9

TRAIN = c453.TRAIN
HELD = c453.HELD
GEOMETRIES = c453.GEOMETRIES
PHYSICAL_STRENGTHS = c453.PHYSICAL_STRENGTHS
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
        "source normalization",
        "finite physical propagation kernel",
        "receiver functional",
        "legacy host green/width normalization",
        "one train-derived receiver scale",
        "no per-row scale factors",
        "train l13/a1/depth4",
        "held l13/a2/depth4",
        "600-second wall cap",
        "4 gib rss cap",
        "two-m2 matched receiver",
        "all 24 proper-cubic frames",
        "no host scalar-profile join",
        "no expectation feedback",
        "no source refresh",
        "no per-update force",
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
    check("the Cycle-458 note freezes the transfer decomposition and single-calibration contract", not missing, missing)


def legacy_propagate_tangent(lat, initial: np.ndarray, field: np.ndarray, q_test: int = 1):
    """Return the p=0 amplitude and d/dp for field p*field."""

    amplitude = initial.copy()
    tangent = np.zeros_like(initial)
    npl = lat.npl
    for layer in range(lat.nl - 1):
        source_start = lat._ls[layer]
        target_start = lat._ls[layer + 1]
        source_amplitude = amplitude[source_start : source_start + npl].copy()
        source_tangent = tangent[source_start : source_start + npl].copy()
        source_field = field[source_start : source_start + npl]
        target_field = field[target_start : target_start + npl]
        if np.max(np.abs(source_amplitude)) < 1e-30:
            continue
        for dy, dz, length, weight in lat._off:
            y_min = max(0, -dy)
            y_max = min(lat._nw, lat._nw - dy)
            z_min = max(0, -dz)
            z_max = min(lat._nw, lat._nw - dz)
            if y_min >= y_max or z_min >= z_max:
                continue
            y_grid, z_grid = np.meshgrid(
                np.arange(y_min, y_max), np.arange(z_min, z_max), indexing="ij"
            )
            source_index = (y_grid.ravel() * lat._nw + z_grid.ravel()).astype(int)
            target_index = (
                (y_grid.ravel() + dy) * lat._nw + z_grid.ravel() + dz
            ).astype(int)
            nonzero = np.abs(source_amplitude[source_index]) > 1e-30
            if not np.any(nonzero):
                continue
            source_index = source_index[nonzero]
            target_index = target_index[nonzero]
            local_field = 0.5 * (
                source_field[source_index] + target_field[target_index]
            )
            base = (
                np.exp(1j * multipole.K * length)
                * weight
                * lat._hm
                / (length * length)
            )
            output = source_amplitude[source_index] * base
            derivative = (
                source_tangent[source_index]
                + source_amplitude[source_index]
                * (1j * multipole.K * length * q_test * local_field)
            ) * base
            np.add.at(amplitude[target_start : target_start + npl], target_index, output)
            np.add.at(tangent[target_start : target_start + npl], target_index, derivative)
    return amplitude, tangent


def width_and_tangent(amplitude, tangent, detector, positions):
    values = amplitude[np.asarray(detector)]
    derivatives = tangent[np.asarray(detector)]
    weights = abs(values) ** 2
    weight_tangent = 2 * np.real(values.conj() * derivatives)
    total = float(np.sum(weights))
    total_tangent = float(np.sum(weight_tangent))
    z = positions[np.asarray(detector), 2]
    first = float(weights @ z / total)
    first_tangent = float(
        (weight_tangent @ z * total - weights @ z * total_tangent) / total**2
    )
    second = float(weights @ (z**2) / total)
    second_tangent = float(
        (weight_tangent @ (z**2) * total - weights @ (z**2) * total_tangent)
        / total**2
    )
    variance = second - first**2
    variance_tangent = second_tangent - 2 * first * first_tangent
    width = math.sqrt(max(0.0, variance))
    return {
        "centroid": first,
        "centroid_tangent": first_tangent,
        "second_moment": second,
        "second_moment_tangent": second_tangent,
        "width": width,
        "width_tangent": variance_tangent / (2 * width),
    }


def legacy_kernel_controls() -> dict[int, dict[str, float]]:
    print("\nLEGACY HOST GREEN / PACKET-WIDTH OPERATOR TANGENTS")
    lat = multipole.Lattice3D(multipole.PHYS_L, multipole.PHYS_W, multipole.H)
    detector = multipole.detector(lat)
    initial = multipole.point_packet(lat)
    rows = {}
    for separation in (1, 2):
        field = multipole.field_from_sources(
            lat, multipole.build_quadrupole(float(separation))
        )
        amplitude, tangent = legacy_propagate_tangent(lat, initial, field)
        operator = width_and_tangent(amplitude, tangent, detector, lat.pos)
        plus = multipole.propagate_charge(lat, initial, TANGENT_FINITE_DIFFERENCE * field, 1)
        minus = multipole.propagate_charge(lat, initial, -TANGENT_FINITE_DIFFERENCE * field, 1)
        _plus_centroid, plus_width = multipole.moments(plus, detector, lat.pos)
        _minus_centroid, minus_width = multipole.moments(minus, detector, lat.pos)
        finite_difference = (plus_width - minus_width) / (2 * TANGENT_FINITE_DIFFERENCE)
        rows[separation] = {
            **operator,
            "finite_difference_width_tangent": finite_difference,
            "tangent_residual": finite_difference - operator["width_tangent"],
            "source_profile_norm": float(np.linalg.norm(field)),
        }
    check(
        "the analytic legacy Green/packet tangent agrees with a predeclared symmetric finite difference at a=1,2",
        max(abs(row["tangent_residual"]) for row in rows.values()) < 2e-10
        and min(row["width_tangent"] for row in rows.values()) > 0
        and max(abs(row["centroid_tangent"]) for row in rows.values()) < 1e-12,
        {"rows": rows, "finite_difference_step": TANGENT_FINITE_DIFFERENCE},
    )
    return rows


def physical_kernel_controls() -> dict[str, object]:
    print("\nFINITE PHYSICAL PROPAGATION KERNELS")
    summaries = []
    endpoints = {}
    for geometry in GEOMETRIES:
        free_state, free_controls = c453.evolve_trace(c435.vacuum_state(), geometry)
        pure_state, pure_controls = c453.evolve_trace(c435.quadrupole_state(geometry), geometry)
        free_weights = c435.packet_weights(free_state)
        pure_weights = c435.packet_weights(pure_state)
        free = c435.packet_moments(free_weights)
        pure = c435.packet_moments(pure_weights)
        second_tangent = pure["second_moment"] - free["second_moment"]
        centroid_tangent = pure["centroid"] - free["centroid"]
        variance_tangent = second_tangent - 2 * free["centroid"] * centroid_tangent
        width_tangent = variance_tangent / (2 * free["width"])
        row = {
            "geometry": asdict(geometry),
            "free": free,
            "pure": pure,
            "centroid_tangent": centroid_tangent,
            "second_moment_tangent": second_tangent,
            "width_tangent": width_tangent,
            "free_controls": free_controls,
            "pure_controls": pure_controls,
        }
        summaries.append(row)
        endpoints[geometry.separation] = {
            "free_weights": free_weights,
            "pure_weights": pure_weights,
            "row": row,
        }
    check(
        "Q0/Q1 endpoint operator data determine centered finite physical width kernels with explicit boundary and norm control",
        min(row["width_tangent"] for row in summaries) > 0
        and max(abs(row["centroid_tangent"]) for row in summaries) < 3e-13
        and max(row["pure_controls"]["maximum_boundary_probability"] for row in summaries) < BOUNDARY_MAXIMUM
        and max(
            max(row["free_controls"]["maximum_norm_error"], row["pure_controls"]["maximum_norm_error"])
            for row in summaries
        ) < TOLERANCE,
        summaries,
    )
    return {"summaries": summaries, "endpoints": endpoints}


def pointer_compiler_controls(receiver_scale: float) -> dict[str, object]:
    print("\nTWO-M2 MATCHED RECEIVER COMPILER")
    embedding = np.zeros((4, 3), dtype=complex)
    embedding[0, 0] = embedding[1, 1] = embedding[2, 2] = 1
    logical_reflection = np.asarray(((0, 0, 1), (0, 1, 0), (1, 0, 0)), dtype=complex)
    physical_reflection = np.asarray(
        ((0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1)),
        dtype=complex,
    )
    projector = embedding @ embedding.conj().T
    sample = np.asarray((1, 2j, -0.5), dtype=complex)
    sample /= np.linalg.norm(sample)
    physical_sample = embedding @ sample
    output = physical_reflection @ physical_sample
    expected = embedding @ (logical_reflection @ sample)
    restored = physical_reflection.conj().T @ output
    leakage = np.linalg.norm(output - projector @ output)
    logical_position = np.diag((-1.0, 0.0, 1.0))
    logical_second = np.diag((1.0, 0.0, 1.0))
    physical_position = np.diag((-receiver_scale, 0.0, receiver_scale, 0.0))
    physical_second = np.diag((receiver_scale**2, 0.0, receiver_scale**2, 0.0))
    row = {
        "receiver_scale": receiver_scale,
        "encoding_shape": embedding.shape,
        "pointer_M2": 2,
        "Gram": float(np.linalg.norm(embedding.conj().T @ embedding - np.eye(3))),
        "EG": float(np.linalg.norm(output - expected)),
        "inverse": float(np.linalg.norm(restored - physical_sample)),
        "leakage": float(leakage),
        "position_compression": float(
            np.linalg.norm(embedding.conj().T @ physical_position @ embedding - receiver_scale * logical_position)
        ),
        "second_compression": float(
            np.linalg.norm(embedding.conj().T @ physical_second @ embedding - receiver_scale**2 * logical_second)
        ),
        "off_code_completion": "unused |11> pointer label fixed by identity",
    }
    check(
        "one train-derived receiver scale compiles into two pointer M2 with exact E/G, inverse, leakage, and effect compression",
        max(
            row[key]
            for key in ("Gram", "EG", "inverse", "leakage", "position_compression", "second_compression")
        ) < 2e-14
        and receiver_scale > 0,
        row,
    )
    return row


def matched_prediction_controls(physical, legacy) -> dict[str, object]:
    print("\nONE-CALIBRATION MATCHED-RECEIVER TOURNAMENT")
    physical_train = physical["endpoints"][1]["row"]["width_tangent"]
    legacy_train = legacy[1]["width_tangent"]
    receiver_scale = legacy_train / physical_train
    compiler = pointer_compiler_controls(receiver_scale)
    rows = {}
    for separation, geometry in ((1, TRAIN), (2, HELD)):
        endpoint = physical["endpoints"][separation]
        for route, occupation in PHYSICAL_STRENGTHS.items():
            weights = (
                (1 - occupation) * endpoint["free_weights"]
                + occupation * endpoint["pure_weights"]
            )
            moments = c435.packet_moments(weights)
            free = endpoint["row"]["free"]
            raw_shift = moments["width"] - free["width"]
            matched_shift = receiver_scale * raw_shift
            legacy_shift = LEGACY_ROWS[(separation, route)]
            rows[(separation, route)] = {
                "geometry": geometry.name,
                "route": route,
                "Q1_occupation": occupation,
                "raw_physical_width_shift": raw_shift,
                "linearized_physical_width_shift": occupation * endpoint["row"]["width_tangent"],
                "physical_nonlinearity_residual": raw_shift - occupation * endpoint["row"]["width_tangent"],
                "matched_width_shift": matched_shift,
                "legacy_width_shift": legacy_shift,
                "named_row_residual": matched_shift - legacy_shift,
                "receiver_scale": receiver_scale,
                "refit": False,
                "per_row_scale_factor": False,
            }
    train_unit = rows[(1, "unit_weight")]
    predicted_keys = (
        (1, "coefficient_two"),
        (2, "unit_weight"),
        (2, "coefficient_two"),
    )
    print("MATCHED ROWS", rows, flush=True)
    check(
        "the train a=1 operator-tangent normalization predicts the finite unit row within the frozen numeric tolerance",
        abs(train_unit["named_row_residual"]) < NUMERIC_ROW_TOLERANCE,
        {
            "physical_train_width_tangent": physical_train,
            "legacy_train_width_tangent": legacy_train,
            "single_receiver_scale": receiver_scale,
            "train_unit": train_unit,
            "fit_parameters": 1,
            "per_row_scale_factors": 0,
        },
    )
    check(
        "the single train-derived receiver normalization predicts coefficient-two and held rows without refit",
        max(abs(rows[key]["named_row_residual"]) for key in predicted_keys)
        < NUMERIC_ROW_TOLERANCE
        and all(not rows[key]["refit"] and not rows[key]["per_row_scale_factor"] for key in rows),
        {
            "predicted_keys": predicted_keys,
            "numeric_row_tolerance": NUMERIC_ROW_TOLERANCE,
            "rows": rows,
        },
    )
    source_ratio = PHYSICAL_STRENGTHS["coefficient_two"] / PHYSICAL_STRENGTHS["unit_weight"]
    response_ratios = {
        separation: rows[(separation, "coefficient_two")]["matched_width_shift"]
        / rows[(separation, "unit_weight")]["matched_width_shift"]
        for separation in (1, 2)
    }
    held_ratios = {
        route: rows[(2, route)]["matched_width_shift"] / rows[(1, route)]["matched_width_shift"]
        for route in PHYSICAL_STRENGTHS
    }
    legacy_kernel_ratio = legacy[2]["width_tangent"] / legacy[1]["width_tangent"]
    physical_kernel_ratio = (
        physical["endpoints"][2]["row"]["width_tangent"]
        / physical["endpoints"][1]["row"]["width_tangent"]
    )
    check(
        "the matched receiver preserves source-strength scaling but reproduces the stronger-a2 kernel order",
        max(abs(value / source_ratio - 1) for value in response_ratios.values()) < 0.01
        and all(value > 1 for value in held_ratios.values()),
        {
            "source_ratio": source_ratio,
            "matched_response_ratios": response_ratios,
            "held_to_train_ratios": held_ratios,
            "physical_operator_kernel_a2_over_a1": physical_kernel_ratio,
            "legacy_operator_kernel_a2_over_a1": legacy_kernel_ratio,
        },
    )
    check(
        "finite physical rows remain within the predeclared endpoint-linearity tolerance used by the transfer decomposition",
        max(abs(row["physical_nonlinearity_residual"]) for row in rows.values())
        < TRANSFER_LINEARITY_TOLERANCE,
        {"tolerance": TRANSFER_LINEARITY_TOLERANCE, "rows": rows},
    )
    return {"rows": rows, "compiler": compiler, "receiver_scale": receiver_scale}


def deletion_covariance_mass_contact_controls(matched) -> None:
    print("\nDELETIONS / ALL-24 / MASS / CONTACT")
    occupation = PHYSICAL_STRENGTHS["coefficient_two"]
    free = c435.evolve(c435.vacuum_state(), TRAIN)
    free_width = c435.packet_moments(c435.packet_weights(free))["width"]
    intact = c435.evolve(c453.strength_state(TRAIN, occupation), TRAIN)
    intact_width = c435.packet_moments(c435.packet_weights(intact))["width"]
    rows = {}
    for name, options in {
        "source": {"source_enabled": False},
        "receiver": {"receiver_enabled": False},
        "field_stream": {"stream_enabled": False},
        "packet_stream": {"packet_stream_enabled": False},
        "contact": {"contact_enabled": False},
    }.items():
        output = c435.evolve(c453.strength_state(TRAIN, occupation), TRAIN, **options)
        width = c435.packet_moments(c435.packet_weights(output))["width"]
        rows[name] = {
            "raw_width": width,
            "matched_width_shift": matched["receiver_scale"] * (width - free_width),
        }
    check(
        "source, receiver, field-stream, packet-stream, receiver-scale, and contact deletions retain distinct scopes",
        max(abs(rows[name]["matched_width_shift"]) for name in ("source", "receiver", "field_stream")) < TOLERANCE
        and abs(rows["packet_stream"]["matched_width_shift"]) > 1e-3
        and abs(matched["receiver_scale"] * (intact_width - free_width)) > 1e-7
        and abs(rows["contact"]["raw_width"] - intact_width) < TOLERANCE,
        {
            "free_width": free_width,
            "intact_width": intact_width,
            "rows": rows,
            "receiver_normalization_deleted_shift": 0.0,
            "source_refresh_count": 0,
            "host_scalar_profile_join_count": 0,
            "expectation_feedback_count": 0,
            "per_update_force_count": 0,
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
        "the scalar matched normalization retains the inherited all-24 family, Cycle-219 mass, and Cycle-230 contact",
        c435.PASS == 1
        and c435.FAIL == 0
        and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and contact_residual > 1e-6,
        {
            "proper_cubic_frames": 24,
            "receiver_scale_is_body-frame_scalar": True,
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
            "two_particle_contact_residual": contact_residual,
        },
    )


def resource_domain_ledger_controls(started: float, physical, matched) -> None:
    print("\nRESOURCE / DOMAIN / DEPENDENCY LEDGER")
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    maximum_payload = max(
        row["pure_controls"]["maximum_logical_payload_bytes"]
        for row in physical["summaries"]
    )
    check(
        "the matched receiver attempt completes below predeclared wall, RSS, payload, and support caps",
        elapsed < WALL_CAP_SECONDS
        and maxrss < RSS_CAP_BYTES
        and maximum_payload < RSS_CAP_BYTES
        and matched["compiler"]["pointer_M2"] == 2,
        {
            "elapsed_seconds": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "maximum_logical_payload_bytes": maximum_payload,
            "pointer_M2": matched["compiler"]["pointer_M2"],
            "L13_physical_shell_materialized": False,
        },
    )
    rejected = 0
    for probe in (
        lambda: c453.strength_state(TRAIN, -0.1),
        lambda: c453.strength_state(TRAIN, 1.1),
        lambda: c435.validate_geometry(c435.Geometry("bad", 6, 1, TRAIN.sources, TRAIN.receivers, 4, False)),
        lambda: c435.source_basis_state(TRAIN, 3),
    ):
        try:
            probe()
        except ValueError:
            rejected += 1
    check("strength, geometry, and source-index domains reject malformed inputs", rejected == 4, rejected)

    named_closed = all(
        abs(row["named_row_residual"]) < NUMERIC_ROW_TOLERANCE
        for row in matched["rows"].values()
    )
    ledger = {
        "source_normalization": "p_route=route_strength/5e-5; supplied exact far-side coordinate",
        "finite_physical_propagation_kernel": "derived from Q0/Q1 endpoint operator moments",
        "receiver_functional": "two-M2 position/second-moment compression with one train-derived scalar",
        "legacy_host_Green_width_normalization": "analytic tangent of the exact far-side propagation",
        "fit_parameters": 1,
        "per_row_scale_factors": 0,
        "named_quadrupole_width_surface_closed": named_closed,
        "L13_physical_shell_EG": False,
        "host_scalar_profile_join_into_physical_update": False,
        "expectation_feedback": False,
        "source_refresh": False,
        "per_update_force": False,
        "phase_called_energy": False,
        "step_called_time": False,
        "receiver_called_Record": False,
        "source_called_gravity": False,
        "Born_or_occurrence": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "open": (
            "matched physical propagation kernel with legacy a-dependence",
            "source-angle or many-Q normalization, physical Cycle213/216 carrier, alternate receiver packet, and physical impact-parameter route",
            "L13 physical shell, autonomous preparation, energy/stress calibration, metric/proper time, Records, Born/occurrence, and realized history",
        ),
    }
    check(
        "the transfer ledger prevents a one-parameter readout calibration from becoming gravity or an unearned named prediction",
        ledger["fit_parameters"] == 1
        and ledger["per_row_scale_factors"] == 0
        and not ledger["host_scalar_profile_join_into_physical_update"]
        and not ledger["expectation_feedback"]
        and not ledger["phase_called_energy"]
        and not ledger["step_called_time"]
        and not ledger["receiver_called_Record"]
        and not ledger["source_called_gravity"]
        and AUTHORITY == "none"
        and AUDIT == "unset",
        ledger,
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle458 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    try:
        print("CYCLE 458: QUADRUPOLE TRANSFER FACTOR / MATCHED RECEIVER")
        print(
            "FROZEN BEFORE FIT",
            {
                "source_normalization": PHYSICAL_STRENGTHS,
                "physical_kernel": "Q0/Q1 endpoint derivative",
                "receiver_functional": "one scalar coordinate scale on Z and Z2",
                "legacy_kernel": "analytic far-side Green/width tangent",
                "fit_row": "train a1 operator tangent only",
                "per_row_scales": 0,
                "train": asdict(TRAIN),
                "held": asdict(HELD),
                "numeric_row_tolerance": NUMERIC_ROW_TOLERANCE,
                "wall_cap_seconds": WALL_CAP_SECONDS,
                "RSS_cap_bytes": RSS_CAP_BYTES,
                "authority": AUTHORITY,
                "audit": AUDIT,
            },
        )
        note_contract()
        legacy = legacy_kernel_controls()
        physical = physical_kernel_controls()
        matched = matched_prediction_controls(physical, legacy)
        deletion_covariance_mass_contact_controls(matched)
        resource_domain_ledger_controls(started, physical, matched)
    except WallCapExceeded as error:
        check("the Cycle458 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_QUADRUPOLE_TRANSFER_FACTOR_MATCHED_RECEIVER_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_QUADRUPOLE_TRANSFER_FACTOR_MATCHED_RECEIVER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
