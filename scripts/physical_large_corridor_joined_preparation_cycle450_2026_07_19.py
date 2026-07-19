#!/usr/bin/env python3
"""Cycle 450: larger physical corridor and joined-preparation stress test.

This is a bounded partial attempt.  It reuses the already constructed local
source and physical M64 corridor factors, enlarges the representative passive
trajectory from L9/depth12 to L17/depth24, and separately tests an eight-vector
Arnoldi/Ritz preparation of the joined source--probe update.  A predeclared
L25/depth36 held preparation exceeded its resource cap and is not replaced.

Authority is none.  Audit is unset.  No update phase is energy or time, and no
coordinate trace is called gravity, lapse, force, or proper time.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_dressed_source_corridor_trajectory_cycle447_2026_07_19 as c447


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LARGE_CORRIDOR_JOINED_PREPARATION_CYCLE450_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

# Frozen before the L17 representative run.  These are not refitted from the
# Cycle-447 L9 failure or the L17 result.
TRAIN = c447.Geometry("train-L17-D24", 17, 24, False)
HELD = c447.Geometry("held-L25-D36", 25, 36, True)
PACKET_MOMENTUM_WIDTH = 0.25
PACKET_CENTER = 5
HELD_PACKET_CENTER = 8
BOUNDARY_MAXIMUM = 0.15
BAND_MINIMUM = 0.85
DELETION_DEPTH = 12
DELETION_VISIBILITY = 1e-6

# The trace classifier is held fixed exactly from Cycle 447.
BIC_ADVANTAGE = c447.BIC_ADVANTAGE
TAIL_CV_MAXIMUM = c447.TAIL_CV_MAXIMUM
DURATION_RATIO_FRACTION = c447.DURATION_RATIO_FRACTION
CURVATURE_FLOOR_MULTIPLIER = c447.CURVATURE_FLOOR_MULTIPLIER
MINIMUM_SECOND_DIFFERENCES = c447.MINIMUM_SECOND_DIFFERENCES

# The joined preparation was frozen before execution.
ARNOLDI_DIMENSION = 8
JOINED_RESIDUAL_MAXIMUM = 1e-6
JOINED_WALL_CAP_SECONDS = 300.0
JOINED_RSS_CAP_BYTES = 3 * 1024**3

# This exact capped preflight is evidence, not an inferred physical failure.
HELD_PREPARATION_CAP_SECONDS = 900.0
HELD_OBSERVED_SECONDS = 930.78
HELD_MAX_RSS_BYTES = 2_838_315_008
HELD_PEAK_FOOTPRINT_BYTES = 8_527_518_368


@dataclass(frozen=True)
class TraceControls:
    source_enabled: bool = True
    test_enabled: bool = True
    field_stream_enabled: bool = True
    matter_stream_enabled: bool = True
    mass_law_enabled: bool = True
    dressed_preparation: bool = True


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
        "l17/depth24 frozen train corridor",
        "l25/depth36 frozen held corridor",
        "raw classifier",
        "two-update stroboscopic classifier",
        "no source refresh",
        "no per-update host force",
        "no c-number expectation gate",
        "all 24 proper-cubic frames",
        "l25-resource-refused",
        "k8-preparation-refused",
        "partial-attempt-with-named-untested-routes",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "no passive-gravity, no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle-450 note freezes the larger-corridor and preparation-refusal contract", not missing, missing)


def validate_geometry(geometry: c447.Geometry, packet_center: int) -> None:
    if geometry not in (TRAIN, HELD) or geometry.length < 17:
        raise ValueError("geometry is outside the frozen Cycle-450 domain")
    if geometry.depth < 24 or packet_center <= 1 or 2 * packet_center >= geometry.length:
        raise ValueError("geometry lacks the frozen corridor/boundary separation")


def prepare_packet(species, length: int, center: int) -> np.ndarray:
    _positions, _momenta, packet = c447.c210.prepare_molecular_packet(
        species, length, PACKET_MOMENTUM_WIDTH
    )
    return np.roll(packet, center - length // 2, axis=0)


def trace_case(
    geometry: c447.Geometry,
    source_mass: float,
    test_mass: float,
    beta: float,
    *,
    controls: TraceControls = TraceControls(),
    depth_override: int | None = None,
) -> dict[str, object]:
    center = PACKET_CENTER if geometry == TRAIN else HELD_PACKET_CENTER
    validate_geometry(geometry, center)
    depth = geometry.depth if depth_override is None else depth_override
    if depth < 1 or depth > geometry.depth:
        raise ValueError("depth override is outside the frozen geometry")

    source_angle = c447.c442.SOURCE_SCALE * source_mass
    eigenvalue, field, eigen_residual = c447.dressed_source(
        geometry.length, round(source_angle, 13)
    )
    if not controls.dressed_preparation:
        field = np.zeros_like(field)
        field[c447.c425.reservoir_index((0, 0, 0), geometry.length)] = 1
    species = c447.c219.common_species(beta)
    packet = prepare_packet(species, geometry.length, center)
    state = np.outer(field, packet.reshape(-1))
    initial = state.copy()
    free = packet.copy()
    deltas: list[float] = []
    boundaries: list[float] = []
    norms: list[float] = []
    reservoir_weights: list[float] = []

    for tick in range(depth + 1):
        density = c447.packet_density(state, geometry.length)
        free_density = c447.c210.position_density(free)
        coordinate = np.arange(geometry.length, dtype=float)
        deltas.append(float(density @ coordinate - free_density @ coordinate))
        boundaries.append(float(density[0] + density[-1]))
        norms.append(float(np.linalg.norm(state)))
        reservoir_weights.append(float(np.sum(np.abs(state[: geometry.length**3]) ** 2)))
        if tick < depth:
            state = c447.joint_step(
                state,
                geometry,
                source_angle,
                test_mass,
                species.coin,
                source_enabled=controls.source_enabled,
                test_enabled=controls.test_enabled,
                field_stream_enabled=controls.field_stream_enabled,
                matter_stream_enabled=controls.matter_stream_enabled,
                mass_law_enabled=controls.mass_law_enabled,
            )
            free = c447.free_step(
                free,
                species.coin if controls.mass_law_enabled else np.eye(6),
                stream_enabled=controls.matter_stream_enabled,
            )

    first = c447.joint_step(initial, geometry, source_angle, test_mass, species.coin)
    restored = c447.joint_inverse(first, geometry, source_angle, test_mass, species.coin)
    ideal = np.outer((eigenvalue**depth) * field, free.reshape(-1))
    delta = np.asarray(deltas)
    raw = c447.classify_trace(delta)
    strobe = c447.classify_trace(delta[::2])
    return {
        "geometry": geometry.name,
        "depth_executed": depth,
        "delta_centroid": tuple(float(value) for value in delta),
        "final_delta": float(delta[-1]),
        "maximum_abs_delta": float(np.max(np.abs(delta))),
        "raw_fit": asdict(raw),
        "two_update_stroboscopic_fit": asdict(strobe),
        "strict_sustained": bool(raw.genuine_acceleration and strobe.genuine_acceleration),
        "maximum_norm_error": max(abs(value - 1) for value in norms),
        "final_band_probability": c447.mixed_band_probability(state, geometry.length, species),
        "maximum_boundary_probability": max(boundaries),
        "source_only_eigen_residual": eigen_residual,
        "source_reservoir_weight_initial": reservoir_weights[0],
        "source_reservoir_weight_final": reservoir_weights[-1],
        "joined_source_reservoir_drift": reservoir_weights[-1] - reservoir_weights[0],
        "joined_backreaction_residual_final": float(np.linalg.norm(state - ideal)),
        "one_step_inverse_residual": float(np.linalg.norm(restored - initial)),
        "source_refresh_count": 0,
        "per_update_host_force_count": 0,
        "c_number_expectation_gate_count": 0,
    }


def inherited_physical_controls():
    print("\nINHERITED LOCAL PHYSICAL COMPILER CONTROLS")
    c447.PASS = 0
    c447.FAIL = 0
    functional, sectors, specifications, compiled = c447.construction_controls()
    c447.projected_source_join_controls(functional, sectors, specifications, compiled)
    c447.physical_corridor_compiler_controls(functional, sectors, specifications)
    c447.covariance_mass_contact_controls(sectors)
    check(
        "the local source/corridor compiler, leakage/inverse, all-24 covariance, mass, and contact controls rerun exactly",
        c447.PASS == 4 and c447.FAIL == 0,
        {"inherited_pass": c447.PASS, "inherited_fail": c447.FAIL},
    )
    return functional, sectors, specifications


def larger_corridor_trajectory(functional, sectors, specifications) -> dict[str, object]:
    print("\nFROZEN L17/DEPTH24 REPRESENTATIVE TRAJECTORY")
    source_sector = sectors[1]
    law = c447.c442.make_law(
        functional,
        specifications["cayley-functional"],
        source_sector,
        source_sector,
        "cayley-functional",
    )
    row = trace_case(TRAIN, law.source_mass, law.test_mass, source_sector.beta)
    row.update(
        {
            "law": "cayley-functional",
            "source_sector": source_sector.name,
            "test_sector": source_sector.name,
            "packet_momentum_width": PACKET_MOMENTUM_WIDTH,
            "packet_center": PACKET_CENTER,
        }
    )
    print("L17 TRAJECTORY ROW", row, flush=True)
    check(
        "the L17 no-refresh trajectory closes the Cycle-447 boundary control with norm, band, inverse, and source-state residuals explicit",
        row["maximum_boundary_probability"] < BOUNDARY_MAXIMUM
        and row["final_band_probability"] > BAND_MINIMUM
        and row["maximum_norm_error"] < 2e-10
        and row["source_only_eigen_residual"] < 2e-10
        and row["one_step_inverse_residual"] < 2e-9
        and row["source_refresh_count"] == 0
        and row["per_update_host_force_count"] == 0
        and row["c_number_expectation_gate_count"] == 0,
        {
            "boundary": row["maximum_boundary_probability"],
            "boundary_maximum": BOUNDARY_MAXIMUM,
            "band": row["final_band_probability"],
            "band_minimum": BAND_MINIMUM,
            "norm_error": row["maximum_norm_error"],
            "source_eigen_residual": row["source_only_eigen_residual"],
            "source_drift": row["joined_source_reservoir_drift"],
            "inverse": row["one_step_inverse_residual"],
        },
    )
    check(
        "raw and two-update stroboscopic classifiers are reported under the unchanged Cycle-447 rule without promotion",
        row["strict_sustained"]
        == (
            row["raw_fit"]["genuine_acceleration"]
            and row["two_update_stroboscopic_fit"]["genuine_acceleration"]
        ),
        {
            "frozen_classifier": {
                "BIC_advantage": BIC_ADVANTAGE,
                "second_difference_CV_maximum": TAIL_CV_MAXIMUM,
                "duration_ratio": f"4 +/- {4 * DURATION_RATIO_FRACTION}",
                "curvature_floor": CURVATURE_FLOOR_MULTIPLIER * c447.NUMERICAL_FLOOR,
                "minimum_same_sign_second_differences": MINIMUM_SECOND_DIFFERENCES,
            },
            "raw_fit": row["raw_fit"],
            "two_update_stroboscopic_fit": row["two_update_stroboscopic_fit"],
            "strict_sustained": row["strict_sustained"],
        },
    )
    return {"law": law, "source_sector": source_sector, "row": row}


def deletion_controls(tournament: dict[str, object]) -> None:
    print("\nFIXED L17 PREPARATION DELETIONS")
    law = tournament["law"]
    source_sector = tournament["source_sector"]
    intact = trace_case(
        TRAIN,
        law.source_mass,
        law.test_mass,
        source_sector.beta,
        depth_override=DELETION_DEPTH,
    )
    intact_trace = np.asarray(intact["delta_centroid"])
    variants = {
        "source_vertex": TraceControls(source_enabled=False),
        "test_recoil": TraceControls(test_enabled=False),
        "field_stream": TraceControls(field_stream_enabled=False),
        "matter_stream": TraceControls(matter_stream_enabled=False),
        "mass_law": TraceControls(mass_law_enabled=False),
        "dressed_preparation": TraceControls(dressed_preparation=False),
    }
    rows = {}
    for name, controls in variants.items():
        row = trace_case(
            TRAIN,
            law.source_mass,
            law.test_mass,
            source_sector.beta,
            controls=controls,
            depth_override=DELETION_DEPTH,
        )
        trace = np.asarray(row["delta_centroid"])
        rows[name] = {
            "maximum_abs_delta": float(np.max(np.abs(trace))),
            "trace_residual_from_intact": float(np.linalg.norm(trace - intact_trace)),
        }
    print("DELETION ROWS", rows, flush=True)
    check(
        "test-recoil and mass-law deletion collapse the trace while source, streams, and dressed preparation remain visible",
        rows["test_recoil"]["maximum_abs_delta"] < 2e-11
        and rows["mass_law"]["maximum_abs_delta"] < 2e-11
        and all(
            rows[name]["trace_residual_from_intact"] > DELETION_VISIBILITY
            for name in ("source_vertex", "field_stream", "matter_stream", "dressed_preparation")
        ),
        {
            "depth": DELETION_DEPTH,
            "visibility_floor": DELETION_VISIBILITY,
            "intact_maximum_abs_delta": intact["maximum_abs_delta"],
            "rows": rows,
        },
    )


def arnoldi_ritz_preparation(tournament: dict[str, object]) -> dict[str, object]:
    print("\nK=8 JOINED SOURCE--PROBE ARNOLDI/RITZ PREPARATION")
    geometry = TRAIN
    law = tournament["law"]
    source_sector = tournament["source_sector"]
    source_angle = c447.c442.SOURCE_SCALE * law.source_mass
    _source_eigenvalue, field, _source_residual = c447.dressed_source(
        geometry.length, round(source_angle, 13)
    )
    species = c447.c219.common_species(source_sector.beta)
    packet = prepare_packet(species, geometry.length, PACKET_CENTER)
    seed = np.outer(field, packet.reshape(-1)).reshape(-1)
    seed /= np.linalg.norm(seed)

    started = time.monotonic()
    basis = np.empty((seed.size, ARNOLDI_DIMENSION + 1), dtype=np.complex128)
    hessenberg = np.zeros((ARNOLDI_DIMENSION + 1, ARNOLDI_DIMENSION), dtype=np.complex128)
    basis[:, 0] = seed
    attained = ARNOLDI_DIMENSION
    for column in range(ARNOLDI_DIMENSION):
        candidate = c447.joint_step(
            basis[:, column].reshape(c447.field_dimension(geometry.length), c447.matter_dimension(geometry.length)),
            geometry,
            source_angle,
            law.test_mass,
            species.coin,
        ).reshape(-1)
        for row in range(column + 1):
            hessenberg[row, column] = np.vdot(basis[:, row], candidate)
            candidate -= hessenberg[row, column] * basis[:, row]
        # One reorthogonalization pass keeps the diagnostic reproducible.
        for row in range(column + 1):
            correction = np.vdot(basis[:, row], candidate)
            hessenberg[row, column] += correction
            candidate -= correction * basis[:, row]
        hessenberg[column + 1, column] = np.linalg.norm(candidate)
        if hessenberg[column + 1, column] < 1e-13:
            attained = column + 1
            break
        basis[:, column + 1] = candidate / hessenberg[column + 1, column]

    reduced = hessenberg[:attained, :attained]
    eigenvalues, eigenvectors = np.linalg.eig(reduced)
    selected = int(np.argmax(np.abs(eigenvectors[0, :])))
    reduced_vector = eigenvectors[:, selected]
    ritz = basis[:, :attained] @ reduced_vector
    ritz /= np.linalg.norm(ritz)
    image = c447.joint_step(
        ritz.reshape(c447.field_dimension(geometry.length), c447.matter_dimension(geometry.length)),
        geometry,
        source_angle,
        law.test_mass,
        species.coin,
    ).reshape(-1)
    value = eigenvalues[selected]
    residual = float(np.linalg.norm(image - value * ritz))
    elapsed = time.monotonic() - started
    rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    # Darwin reports bytes, Linux KiB.  This campaign runs on Darwin; retain
    # the raw platform value so independent reruns do not hide the convention.
    result = {
        "geometry": geometry.name,
        "arnoldi_dimension_requested": ARNOLDI_DIMENSION,
        "arnoldi_dimension_attained": attained,
        "selected_value_real": float(value.real),
        "selected_value_imag": float(value.imag),
        "selected_value_modulus": float(abs(value)),
        "residual": residual,
        "residual_maximum": JOINED_RESIDUAL_MAXIMUM,
        "seed_overlap": float(abs(np.vdot(seed, ritz))),
        "basis_orthogonality_residual": float(
            np.linalg.norm(basis[:, :attained].conj().T @ basis[:, :attained] - np.eye(attained))
        ),
        "elapsed_seconds": elapsed,
        "wall_cap_seconds": JOINED_WALL_CAP_SECONDS,
        "raw_maxrss_platform_units": rss,
        "rss_cap_bytes_on_Darwin": JOINED_RSS_CAP_BYTES,
        "source_refresh_count": 0,
        "per_update_host_force_count": 0,
        "c_number_expectation_gate_count": 0,
        "disposition": "accepted-joined-eigenpacket" if residual <= JOINED_RESIDUAL_MAXIMUM else "K8-PREPARATION-REFUSED",
    }
    print("JOINED PREPARATION ROW", result, flush=True)
    check(
        "the predeclared K=8 joined Ritz candidate is accepted only if its direct full-update residual meets 1e-6",
        residual <= JOINED_RESIDUAL_MAXIMUM,
        result,
    )
    return result


def held_resource_refusal() -> dict[str, object]:
    print("\nFROZEN L25 HELD RESOURCE DISPOSITION")
    row = {
        "geometry": HELD.name,
        "field_dimension": c447.field_dimension(HELD.length),
        "matter_dimension": c447.matter_dimension(HELD.length),
        "joint_complex128_GiB": (
            c447.field_dimension(HELD.length)
            * c447.matter_dimension(HELD.length)
            * np.dtype(np.complex128).itemsize
            / 1024**3
        ),
        "wall_cap_seconds": HELD_PREPARATION_CAP_SECONDS,
        "observed_before_termination_seconds": HELD_OBSERVED_SECONDS,
        "max_rss_bytes": HELD_MAX_RSS_BYTES,
        "peak_memory_footprint_bytes": HELD_PEAK_FOOTPRINT_BYTES,
        "disposition": "L25-RESOURCE-REFUSED",
        "physics_failure": False,
        "substitute_geometry_or_threshold": False,
    }
    check(
        "the predeclared L25/depth36 held eigensolve completed inside its resource cap",
        False,
        row,
    )
    return row


def prediction_supply_and_domain_controls(
    tournament: dict[str, object], joined: dict[str, object], held: dict[str, object]
) -> None:
    print("\nPREDICTION / SUPPLY / DOMAIN BOUNDARY")
    ledger = {
        "Cycle204_Hamiltonian_rows_reproduced": False,
        "Cycle204_strict_QCA_rows_reproduced": False,
        "Cycle204_bound_composite_rows_reproduced": False,
        "Cycle210_exact_mass_rows_reproduced": False,
        "Cycle210_supplied_lapse_acceleration_rows_reproduced": False,
        "L^-1=G_0_derived": False,
        "rho=|psi|^2_derived": False,
        "S=L(1-phi)_derived": False,
        "physical_energy_or_time_from_phase": False,
        "passive_gravity": False,
        "metric_or_proper_time": False,
        "Born_or_occurrence": False,
        "Record": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "supplied": (
            "two nine-M2 one-hot registers, Cayley source law, coupling scale, source/test sector, and host eigensolver",
            "periodic L17/L25 geometries, packet widths/centers, depths, factor order, fit thresholds, boundary/band gates, and readouts",
            "K=8 Arnoldi dimension, 1e-6 preparation gate, resource caps, repeated M64 identity completions, and diagnostic arithmetic",
        ),
        "derived": (
            "L17 joint amplitude trajectory, boundary/band/norm/inverse residuals, source drift, and backreaction",
            "raw and two-update-stroboscopic classifier outputs without sustained promotion",
            "local compiler/leakage/all-24/mass/contact checks, deletion residuals, and a direct K8 Ritz residual",
        ),
        "open": (
            "L25 held trajectory after scalable dressed-source preparation",
            "joined source-probe preparation at K>8 or by a different physical preparation route",
            "a held raw-and-stroboscopic sustained passive trajectory, many-Q source recurrence, energy/stress calibration, metric/proper time, Records, Born/occurrence, and realized history",
        ),
        "route_dispositions": (
            "L17-boundary-closed-classifier-failed",
            held["disposition"],
            joined["disposition"],
        ),
    }
    check(
        "the supplied/derived/open ledger prevents resource or preparation refusal from becoming a gravity or no-go claim",
        not any(
            value
            for key, value in ledger.items()
            if key.endswith("_reproduced") or key.endswith("_derived")
        )
        and not ledger["physical_energy_or_time_from_phase"]
        and not ledger["passive_gravity"]
        and AUTHORITY == "none"
        and AUDIT == "unset",
        ledger,
    )

    rejections = 0
    for probe in (
        lambda: validate_geometry(c447.Geometry("bad", 15, 24, False), PACKET_CENTER),
        lambda: validate_geometry(TRAIN, 0),
        lambda: c447.local_test_vertex(float("nan")),
    ):
        try:
            probe()
        except (ValueError, OverflowError):
            rejections += 1
    check("malformed geometry, packet center, and nonfinite mass domains are rejected", rejections == 3, rejections)


def main() -> int:
    print("CYCLE 450: PHYSICAL LARGE-CORRIDOR / JOINED-PREPARATION PARTIAL ATTEMPT")
    print(
        "FROZEN CONTRACT",
        {
            "train": TRAIN,
            "held": HELD,
            "packet_momentum_width": PACKET_MOMENTUM_WIDTH,
            "packet_centers_train_held": (PACKET_CENTER, HELD_PACKET_CENTER),
            "boundary_maximum": BOUNDARY_MAXIMUM,
            "band_minimum": BAND_MINIMUM,
            "classifier_unchanged_from_Cycle447": True,
            "joined_Arnoldi_dimension": ARNOLDI_DIMENSION,
            "joined_residual_maximum": JOINED_RESIDUAL_MAXIMUM,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    note_contract()
    functional, sectors, specifications = inherited_physical_controls()
    tournament = larger_corridor_trajectory(functional, sectors, specifications)
    deletion_controls(tournament)
    joined = arnoldi_ritz_preparation(tournament)
    held = held_resource_refusal()
    prediction_supply_and_domain_controls(tournament, joined, held)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_LARGE_CORRIDOR_JOINED_PREPARATION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_LARGE_CORRIDOR_JOINED_PREPARATION_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
