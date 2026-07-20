#!/usr/bin/env python3
"""Cycle 453: exact-strength physical quadrupole prediction bridge.

Carry the Cycle-420 signed (+1,-2,+1) quadrupole coefficients as phases of a
positive-occupation Cycle-435 source state.  The Q1 occupation is fixed by the
far-side runner's own normalization, route_strength / SOURCE_STRENGTH.  The
same local field update drives a physical M64 receiver packet; no host scalar
profile, expectation feedback, source refresh, or per-update force is used.

Authority is none and audit is unset.  Source/receiver coordinates and update
count are not gravity or time; phases are not energy; pointer labels are not
Records; coherent weights are not Born frequencies.
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_quadrupole_packet_width_bridge_cycle435_2026_07_19 as c435


c420 = c435.c420
c432 = c435.c432
c425 = c435.c425
c319 = c435.c319
c210 = c435.c210
multipole = c420.multipole

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EXACT_STRENGTH_QUADRUPOLE_PREDICTION_BRIDGE_CYCLE453_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

TOLERANCE = c435.TOLERANCE
CERTIFICATION_ERROR_FLOOR = c435.CERTIFICATION_ERROR_FLOOR
SIGNAL_FLOOR = 1000 * CERTIFICATION_ERROR_FLOOR
NUMERIC_ROW_TOLERANCE = 1000 * CERTIFICATION_ERROR_FLOOR
STRENGTH_RATIO_RELATIVE_TOLERANCE = 0.01
BOUNDARY_MAXIMUM = 0.10
RESOURCE_CAP_BYTES = 4 * 1024**3
L13_SHELL_ABORT_SECONDS = 862.84
L13_SHELL_MAX_RSS_BYTES = 1_504_165_888
L13_SHELL_PEAK_FOOTPRINT_BYTES = 3_892_677_920

# Frozen after predecessor/free-geometry reconstruction and before any
# interacting Cycle-453 row.  Equal L and depth isolate source separation.
TRAIN = c435.Geometry(
    "train_L13_a1_D4",
    13,
    1,
    ((4, 6, 5), (4, 6, 6), (4, 6, 7)),
    ((6, 6, 5), (6, 6, 6), (6, 6, 7)),
    4,
    False,
)
HELD = c435.Geometry(
    "held_L13_a2_D4",
    13,
    2,
    ((4, 6, 4), (4, 6, 6), (4, 6, 8)),
    ((6, 6, 5), (6, 6, 6), (6, 6, 7)),
    4,
    True,
)
GEOMETRIES = (TRAIN, HELD)

# This is the exact dimensionless coefficient used by the far-side runner:
# its field is built at SOURCE_STRENGTH and multiplied by route/source ratio.
PHYSICAL_STRENGTHS = {
    route: strength / multipole.SOURCE_STRENGTH
    for route, strength in c420.ROUTE_STRENGTHS.items()
}

LEGACY_ROWS = {
    (1, "unit_weight"): 6.692829912502418e-7,
    (1, "coefficient_two"): 3.3757457469363317e-6,
    (2, "unit_weight"): 1.3197896109318208e-6,
    (2, "coefficient_two"): 6.656001151128521e-6,
}


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
        "physical (+1,-2,+1) phase quadrupole",
        "no negative occupation",
        "p_route = route_strength / 5e-5",
        "train l13/a1/depth4",
        "held l13/a2/depth4",
        "numeric row tolerance 5e-10",
        "boundary ceiling 0.10",
        "no host scalar-profile join",
        "no expectation feedback",
        "no source refresh",
        "no per-update force",
        "all 24 proper-cubic frames",
        "source, receiver, field-stream, packet-stream, coherence, sign, and contact deletions",
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
    check("the Cycle-453 note freezes the exact-strength quadrupole contract before result promotion", not missing, missing)


def far_side_contract_controls() -> None:
    print("\nCYCLE-420 / EXACT FAR-SIDE CONTRACT")
    quadrupole = next(surface for surface in c420.SURFACES if surface.name == "quadrupole_width")
    impact = next(surface for surface in c420.SURFACES if surface.name == "impact_parameter")
    check(
        "the exact quadrupole-width and impact-parameter far-side contracts are imported without type conflation",
        multipole.build_quadrupole(1.0) == [(-1.0, 1.0), (0.0, -2.0), (1.0, 1.0)]
        and multipole.QUAD_SEPARATIONS == (1.0, 2.0)
        and multipole.SOURCE_STRENGTH == 5e-5
        and c420.impact.B_VALUES == (5, 6, 7, 8, 10)
        and quadrupole.source_interface.startswith("signed host")
        and impact.source_interface.startswith("positive host")
        and all(0 < value < 1 for value in PHYSICAL_STRENGTHS.values()),
        {
            "quadrupole_contract": asdict(quadrupole),
            "impact_contract": asdict(impact),
            "legacy_source_normalization": multipole.SOURCE_STRENGTH,
            "route_strengths": c420.ROUTE_STRENGTHS,
            "physical_Q1_occupations": PHYSICAL_STRENGTHS,
            "route_ratio": c420.ROUTE_STRENGTHS["coefficient_two"] / c420.ROUTE_STRENGTHS["unit_weight"],
            "impact_route_attempted_here": False,
        },
    )


def source_and_geometry_controls() -> None:
    print("\nPHYSICAL SOURCE COLUMN / FROZEN CENTERED GEOMETRIES")
    occupations = abs(c435.QUADRUPOLE) ** 2
    check(
        "the physical (+1,-2,+1) column carries sign by phase with nonnegative occupation at exact normalized strengths",
        np.linalg.norm(c435.QUADRUPOLE - np.asarray((1, -2, 1)) / np.sqrt(6)) < TOLERANCE
        and np.linalg.norm(occupations - np.asarray((1, 4, 1)) / 6) < TOLERANCE
        and abs(np.sum(c435.QUADRUPOLE)) < TOLERANCE
        and all(value >= 0 for value in occupations)
        and abs(
            PHYSICAL_STRENGTHS["coefficient_two"] / PHYSICAL_STRENGTHS["unit_weight"]
            - c420.ROUTE_STRENGTHS["coefficient_two"] / c420.ROUTE_STRENGTHS["unit_weight"]
        ) < TOLERANCE,
        {
            "amplitudes": c435.QUADRUPOLE,
            "occupations_within_Q1": occupations,
            "negative_occupations": 0,
            "Q1_occupations_by_route": PHYSICAL_STRENGTHS,
            "Q0_occupations_by_route": {key: 1 - value for key, value in PHYSICAL_STRENGTHS.items()},
            "autonomous_preparation": False,
        },
    )
    for geometry in GEOMETRIES:
        c435.validate_geometry(geometry)
    check(
        "train L13/a1/depth4 and held L13/a2/depth4 isolate separation without a periodic source placement",
        TRAIN.length == HELD.length == 13
        and TRAIN.depth == HELD.depth == 4
        and TRAIN.receivers == HELD.receivers
        and TRAIN.separation == 1
        and HELD.separation == 2
        and not TRAIN.held
        and HELD.held
        and all(0 < value < 12 for geometry in GEOMETRIES for cell in geometry.sources + geometry.receivers for value in cell),
        {"train": asdict(TRAIN), "held": asdict(HELD), "held_refits": 0},
    )


def strength_state(geometry: c435.Geometry, occupation: float, *, positive_phase: bool = False):
    if not 0 <= occupation <= 1:
        raise ValueError("normalized physical source strength must be in [0,1]")
    if positive_phase:
        quadrupole = c435.combine(
            tuple(c435.source_basis_state(geometry, index) for index in range(3)),
            np.asarray((1, 2, 1), dtype=complex) / np.sqrt(6),
        )
    else:
        quadrupole = c435.quadrupole_state(geometry)
    return c435.combine(
        (c435.vacuum_state(), quadrupole),
        np.asarray((np.sqrt(1 - occupation), np.sqrt(occupation)), dtype=complex),
    )


def field_cell(key: int, length: int):
    if key < 0:
        return None
    if key < length**3:
        return (key // (length * length), (key // length) % length, key % length)
    return c432.decode_field(key, length)[0]


def boundary_probability(state, geometry: c435.Geometry) -> float:
    total = 0.0
    for key, value in state.items():
        cell = field_cell(key, geometry.length)
        if cell is not None and any(coordinate in (0, geometry.length - 1) for coordinate in cell):
            total += float(np.vdot(value, value).real)
    return total


def evolve_trace(state, geometry: c435.Geometry, **kwargs):
    output = state
    boundaries = [boundary_probability(output, geometry)]
    norms = [c435.state_norm(output)]
    maximum_keys = len(output)
    maximum_bytes = sum(value.nbytes for value in output.values())
    for _ in range(geometry.depth):
        output = c435.logical_step(output, geometry, **kwargs)
        boundaries.append(boundary_probability(output, geometry))
        norms.append(c435.state_norm(output))
        maximum_keys = max(maximum_keys, len(output))
        maximum_bytes = max(maximum_bytes, sum(value.nbytes for value in output.values()))
    return output, {
        "maximum_boundary_probability": max(boundaries),
        "maximum_norm_error": max(abs(value - 1) for value in norms),
        "maximum_active_field_keys": maximum_keys,
        "maximum_logical_payload_bytes": maximum_bytes,
    }


def prediction_controls() -> dict[str, object]:
    print("\nEXACT-NORMALIZED-STRENGTH PHYSICAL WIDTH PREDICTIONS")
    summaries = []
    states = {}
    for geometry in GEOMETRIES:
        free_state, free_controls = evolve_trace(c435.vacuum_state(), geometry)
        pure_state, pure_controls = evolve_trace(c435.quadrupole_state(geometry), geometry)
        free = c435.packet_moments(c435.packet_weights(free_state))
        pure = c435.packet_moments(c435.packet_weights(pure_state))
        rows = []
        for route, occupation in PHYSICAL_STRENGTHS.items():
            initial = strength_state(geometry, occupation)
            output, controls = evolve_trace(initial, geometry)
            moments = c435.packet_moments(c435.packet_weights(output))
            legacy = LEGACY_ROWS[(geometry.separation, route)]
            row = {
                "route": route,
                "far_side_route_strength": c420.ROUTE_STRENGTHS[route],
                "Q1_occupation": occupation,
                "centroid_shift": moments["centroid"] - free["centroid"],
                "width": moments["width"],
                "width_shift": moments["width"] - free["width"],
                "legacy_width_shift": legacy,
                "legacy_numeric_residual": moments["width"] - free["width"] - legacy,
                "legacy_relative_ratio": (moments["width"] - free["width"]) / legacy,
                "maximum_boundary_probability": controls["maximum_boundary_probability"],
                "maximum_norm_error": controls["maximum_norm_error"],
                "source_refresh_count": 0,
                "host_scalar_profile_join_count": 0,
                "expectation_feedback_count": 0,
                "per_update_force_count": 0,
                "refit": False,
            }
            rows.append(row)
            states[(geometry.name, route)] = output
        summaries.append(
            {
                "geometry": asdict(geometry),
                "free": free,
                "pure_quadrupole": pure,
                "pure_controls": pure_controls,
                "free_controls": free_controls,
                "rows": rows,
            }
        )
    by_key = {
        (summary["geometry"]["separation"], row["route"]): row
        for summary in summaries
        for row in summary["rows"]
    }
    response_ratios = {
        separation: by_key[(separation, "coefficient_two")]["width_shift"]
        / by_key[(separation, "unit_weight")]["width_shift"]
        for separation in (1, 2)
    }
    source_ratio = c420.ROUTE_STRENGTHS["coefficient_two"] / c420.ROUTE_STRENGTHS["unit_weight"]
    print("PREDICTION ROWS", summaries, flush=True)
    check(
        "the exact-normalized physical source gives centered, resolved positive widths at both strengths and both separations without host control",
        max(abs(row["centroid_shift"]) for summary in summaries for row in summary["rows"]) < 3e-13
        and min(row["width_shift"] for summary in summaries for row in summary["rows"]) > SIGNAL_FLOOR
        and all(
            row["source_refresh_count"] == row["host_scalar_profile_join_count"]
            == row["expectation_feedback_count"] == row["per_update_force_count"] == 0
            and not row["refit"]
            for summary in summaries for row in summary["rows"]
        )
        and max(summary["pure_controls"]["maximum_norm_error"] for summary in summaries) < TOLERANCE,
        {"summaries": summaries, "signal_floor": SIGNAL_FLOOR},
    )
    check(
        "the frozen coefficient-two and held-a2 qualitative order and strength ratio survive without refit",
        all(
            by_key[(separation, "coefficient_two")]["width_shift"]
            > by_key[(separation, "unit_weight")]["width_shift"]
            for separation in (1, 2)
        )
        and all(
            by_key[(2, route)]["width_shift"] > by_key[(1, route)]["width_shift"]
            for route in PHYSICAL_STRENGTHS
        )
        and max(abs(value / source_ratio - 1) for value in response_ratios.values())
        < STRENGTH_RATIO_RELATIVE_TOLERANCE,
        {
            "source_ratio": source_ratio,
            "physical_response_ratios": response_ratios,
            "relative_tolerance": STRENGTH_RATIO_RELATIVE_TOLERANCE,
            "held_to_train": {
                route: by_key[(2, route)]["width_shift"] / by_key[(1, route)]["width_shift"]
                for route in PHYSICAL_STRENGTHS
            },
        },
    )
    numeric_residuals = {
        key: abs(row["legacy_numeric_residual"]) for key, row in by_key.items()
    }
    check(
        "the four physical rows reproduce the exact Cycle-420 quadrupole-width numbers at the frozen 5e-10 tolerance",
        max(numeric_residuals.values()) < NUMERIC_ROW_TOLERANCE,
        {
            "numeric_row_tolerance": NUMERIC_ROW_TOLERANCE,
            "rows": by_key,
            "absolute_residuals": numeric_residuals,
            "named_quadrupole_width_surface_closed": max(numeric_residuals.values()) < NUMERIC_ROW_TOLERANCE,
        },
    )
    return {"summaries": summaries, "states": states, "by_key": by_key}


def physical_compiler_controls() -> dict[str, object]:
    print("\nINHERITED LOCAL PHYSICAL E/G / L13 RESOURCE REFUSAL")
    c435.PASS = c435.FAIL = 0
    inherited = c435.physical_compiler_controls()
    rows = tuple(
        {
            **row,
            "leakage_upper_bound_from_EG": row["EG_residual"],
            "scope": "inherited Cycle435 L7/L9 local compiler; not an L13 substitute",
        }
        for row in inherited["rows"]
    )
    check(
        "the inherited L7/L9 local compiler reruns E/G, inverse, Gram, leakage bounds, and bounded support without substituting for L13",
        c435.PASS == 2
        and c435.FAIL == 0
        and max(
            max(
                row["all_order_Gram_raw_maximum"],
                row["EG_residual"],
                row["inverse_residual"],
                row["leakage_upper_bound_from_EG"],
                abs(row["output_norm"] - 1),
            )
            for row in rows
        ) < TOLERANCE
        and max(row["matter_support_M2"] for row in rows) < 200,
        {"rows": rows, "inherited_pass": c435.PASS, "inherited_fail": c435.FAIL},
    )

    logical_rows = []
    for geometry in GEOMETRIES:
        initial = strength_state(geometry, PHYSICAL_STRENGTHS["coefficient_two"])
        output = c435.logical_step(initial, geometry)
        restored = c435.logical_inverse(output, geometry)
        logical_rows.append(
            {
                "geometry": geometry.name,
                "logical_inverse_residual": c435.state_residual(restored, initial),
                "logical_output_norm_error": abs(c435.state_norm(output) - 1),
            }
        )
    check(
        "the frozen L13 train/held logical updates retain norm and exact adjoint inverse",
        max(max(row["logical_inverse_residual"], row["logical_output_norm_error"]) for row in logical_rows) < TOLERANCE,
        logical_rows,
    )
    check(
        "the frozen L13 physical shell E/G and explicit leakage projection completed inside a predeclared wall cap",
        False,
        {
            "disposition": "L13-PHYSICAL-SHELL-RESOURCE-REFUSED",
            "contract_defect": "the first run froze a 4GiB cap but omitted a wall cap",
            "terminated_during": "first L13 source-block multi-order encoding",
            "observed_seconds": L13_SHELL_ABORT_SECONDS,
            "max_rss_bytes": L13_SHELL_MAX_RSS_BYTES,
            "peak_memory_footprint_bytes": L13_SHELL_PEAK_FOOTPRINT_BYTES,
            "physics_EG_failure": False,
            "L7_L9_result_used_as_L13_substitute": False,
            "L13_physical_shell_EG_open": True,
        },
    )
    return {"rows": rows, "update_rows": inherited["update_rows"], "logical_rows": logical_rows}


def pointer_and_covariance_controls() -> dict[str, object]:
    print("\nINHERITED PHYSICAL WIDTH EFFECT / ALL-24 PROPER-CUBIC FAMILY")
    c435.PASS = c435.FAIL = 0
    pointer = c435.pointer_dilation_controls()
    c435.covariance_controls()
    pointer_rows = tuple(
        {**row, "scope": "inherited Cycle435 L7/L9 effect; not an L13 shell substitute"}
        for row in pointer["rows"]
    )
    check(
        "the inherited physical centroid/second-moment effects and whole labelled family rerun in all 24 frames without substituting for L13",
        c435.PASS == 2
        and c435.FAIL == 0,
        {
            "pointer_rows": pointer_rows,
            "proper_cubic_frames": 24,
            "inherited_covariance_pass": c435.PASS,
            "body_frame_and_coefficients_rotated_together": True,
            "local_pointer_coupling_gate_constructed": False,
            "pointer_labels_are_Records": False,
            "L13_physical_pointer_shell_open": True,
        },
    )
    return {"pointer_rows": pointer_rows}


def deletion_boundary_mass_resource_domain_controls(prediction, compiler, pointer) -> None:
    print("\nDELETION / BOUNDARY / MASS / CONTACT / RESOURCE / DOMAIN")
    geometry = TRAIN
    occupation = PHYSICAL_STRENGTHS["coefficient_two"]
    intact = prediction["states"][(geometry.name, "coefficient_two")]
    free = c435.evolve(c435.vacuum_state(), geometry)
    free_width = c435.packet_moments(c435.packet_weights(free))["width"]
    intact_width = c435.packet_moments(c435.packet_weights(intact))["width"]
    deletion_widths = {}
    for name, options in {
        "source": {"source_enabled": False},
        "receiver": {"receiver_enabled": False},
        "field_stream": {"stream_enabled": False},
        "packet_stream": {"packet_stream_enabled": False},
        "contact": {"contact_enabled": False},
    }.items():
        deleted = c435.evolve(strength_state(geometry, occupation), geometry, **options)
        deletion_widths[name] = c435.packet_moments(c435.packet_weights(deleted))["width"]

    basis_outputs = tuple(c435.evolve(c435.source_basis_state(geometry, index), geometry) for index in range(3))
    vacuum_weights = c435.packet_weights(free)
    incoherent_q1 = sum(
        (abs(coefficient) ** 2 * c435.packet_weights(state) for coefficient, state in zip(c435.QUADRUPOLE, basis_outputs)),
        start=np.zeros(3),
    )
    incoherent_width = c435.packet_moments((1 - occupation) * vacuum_weights + occupation * incoherent_q1)["width"]
    positive = c435.evolve(strength_state(geometry, occupation, positive_phase=True), geometry)
    positive_width = c435.packet_moments(c435.packet_weights(positive))["width"]
    check(
        "source, receiver, field-stream, packet-stream, coherence, sign, and contact deletions retain their declared scopes",
        max(abs(deletion_widths[name] - free_width) for name in ("source", "receiver", "field_stream")) < TOLERANCE
        and abs(deletion_widths["packet_stream"] - intact_width) > SIGNAL_FLOOR
        and abs(incoherent_width - intact_width) > 10 * CERTIFICATION_ERROR_FLOOR
        and abs(positive_width - intact_width) > 10 * CERTIFICATION_ERROR_FLOOR
        and abs(deletion_widths["contact"] - intact_width) < TOLERANCE,
        {
            "free_width": free_width,
            "intact_width": intact_width,
            "deletion_widths": deletion_widths,
            "coherence_erased_width": incoherent_width,
            "positive_phase_width": positive_width,
            "contact_inactive_on_prediction_sector": True,
            "visibility_floor": 10 * CERTIFICATION_ERROR_FLOOR,
        },
    )

    update_rows = compiler["update_rows"]
    contact = c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    full_contact_residual = float(np.linalg.norm(contact @ two_particle - two_particle))
    check(
        "Cycle-219 mass and Cycle-230 contact survive the exact-strength bridge",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and full_contact_residual > 1e-6,
        {
            "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_mass": update_rows["three_cell_rest_mass"],
            "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
            "contact_nontrivial_columns_per_block": update_rows["contact_nontrivial_columns"],
            "two_particle_contact_deletion_residual": full_contact_residual,
        },
    )

    pure_controls = [summary["pure_controls"] for summary in prediction["summaries"]]
    maximum_boundary = max(row["maximum_boundary_probability"] for row in pure_controls)
    maximum_payload = max(row["maximum_logical_payload_bytes"] for row in pure_controls)
    maximum_support = max(row["matter_support_M2"] for row in compiler["rows"])
    check(
        "held-size boundary and resource controls remain below their predeclared ceilings",
        maximum_boundary < BOUNDARY_MAXIMUM
        and maximum_payload < RESOURCE_CAP_BYTES
        and maximum_support < 200
        and all(row["pointer_M2"] == 2 for row in pointer["pointer_rows"]),
        {
            "L_train_held": (TRAIN.length, HELD.length),
            "maximum_pure_Q1_boundary_probability": maximum_boundary,
            "boundary_ceiling": BOUNDARY_MAXIMUM,
            "maximum_active_logical_payload_bytes": maximum_payload,
            "resource_cap_bytes": RESOURCE_CAP_BYTES,
            "maximum_matter_support_M2_per_block": maximum_support,
            "field_M2_per_cubic_cell": 7,
            "pointer_M2": 2,
            "local_constraints": "independent Cycle269/319 checks and Wilson sector per M64 block",
        },
    )

    rejected = 0
    for probe in (
        lambda: c435.validate_geometry(c435.Geometry("bad", 6, 1, TRAIN.sources, TRAIN.receivers, 4, False)),
        lambda: strength_state(TRAIN, -0.1),
        lambda: strength_state(TRAIN, 1.1),
        lambda: c435.source_basis_state(TRAIN, 3),
        lambda: c435.restricted_vertex("bad", 0),
    ):
        try:
            probe()
        except ValueError:
            rejected += 1
    check("geometry, strength, source-index, and vertex domains reject malformed inputs", rejected == 5, rejected)


def ledger_controls(prediction) -> None:
    print("\nEXACT NAMED-SURFACE / TOE DEPENDENCY LEDGER")
    numeric_closed = all(
        abs(row["legacy_numeric_residual"]) < NUMERIC_ROW_TOLERANCE
        for row in prediction["by_key"].values()
    )
    ledger = {
        "physical_phase_quadrupole": True,
        "exact_far_side_normalized_strengths": True,
        "physical_M64_packet_receiver": True,
        "physical_centroid_second_moment_effects": True,
        "host_scalar_profile_join": False,
        "expectation_feedback": False,
        "source_refresh": False,
        "per_update_force": False,
        "exact_legacy_numeric_rows_reproduced": numeric_closed,
        "named_quadrupole_width_surface_closed": numeric_closed,
        "impact_parameter_surface_attempted": False,
        "phase_called_energy": False,
        "step_called_time": False,
        "receiver_called_Record": False,
        "source_called_gravity": False,
        "Born_or_occurrence": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "supplied": (
            "two physical Cycle319/396 M64 blocks, local constraints, identity completions, Cycle425 field coin/stream, and Cycle426 recoil vertices",
            "Cycle420 route strengths, far-side 5e-5 normalization, phase column, centered geometries, fixed depth/order, packet preparation, and effect dilation",
            "numeric-row, signal, boundary, ratio, resource, and deletion criteria",
        ),
        "derived": (
            "exact-normalized positive-occupation phase source propagated into one physical M64 receiver packet",
            "train/held widths, qualitative order, exact row residuals, L13 logical inverse, inherited local E/G/inverse/leakage bounds/all24, mass/contact, deletion, boundary, and resource controls",
        ),
        "open": (
            "exact Cycle420 numeric-row reproduction if the direct normalization misses",
            "physical impact-parameter b=(5,6,7,8,10) family and no-refit exponent",
            "autonomous source/effect preparation, pointer coupling/inverse, many-Q recurrence, energy/stress calibration, metric/proper time, Records, Born/occurrence, and realized history",
        ),
    }
    check(
        "the supplied/derived/open ledger prevents a physical width bridge from being promoted to gravity or an unearned named prediction",
        ledger["physical_phase_quadrupole"]
        and ledger["exact_far_side_normalized_strengths"]
        and ledger["physical_M64_packet_receiver"]
        and not ledger["host_scalar_profile_join"]
        and not ledger["expectation_feedback"]
        and not ledger["phase_called_energy"]
        and not ledger["step_called_time"]
        and not ledger["receiver_called_Record"]
        and not ledger["source_called_gravity"]
        and AUTHORITY == "none"
        and AUDIT == "unset",
        ledger,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 453: PHYSICAL EXACT-STRENGTH QUADRUPOLE PREDICTION BRIDGE")
    print(
        "FROZEN BEFORE INTERACTING ROWS",
        {
            "train": asdict(TRAIN),
            "held": asdict(HELD),
            "physical_strengths": PHYSICAL_STRENGTHS,
            "signal_floor": SIGNAL_FLOOR,
            "numeric_row_tolerance": NUMERIC_ROW_TOLERANCE,
            "ratio_relative_tolerance": STRENGTH_RATIO_RELATIVE_TOLERANCE,
            "boundary_ceiling": BOUNDARY_MAXIMUM,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    note_contract()
    far_side_contract_controls()
    source_and_geometry_controls()
    prediction = prediction_controls()
    compiler = physical_compiler_controls()
    pointer = pointer_and_covariance_controls()
    deletion_boundary_mass_resource_domain_controls(prediction, compiler, pointer)
    ledger_controls(prediction)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_EXACT_STRENGTH_QUADRUPOLE_PREDICTION_BRIDGE_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_EXACT_STRENGTH_QUADRUPOLE_PREDICTION_BRIDGE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
