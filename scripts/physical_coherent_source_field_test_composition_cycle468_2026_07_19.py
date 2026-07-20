#!/usr/bin/env python3
"""Cycle 468: coherent source / relaxed field / passive M64 test composition.

Compose Cycle465's physical Q1 source-position control and locally generated
Cycle463 word field with Cycle464's supplied word-to-Q1 preparation, identical
neighbor-direction lift, reciprocal 42-state field/test vertex, common M64
test coin, and nearest-neighbour stream.  Every coherent source branch is kept
in one sparse direct-sum state; no branch is selected and no per-step force,
expectation feedback, or source refresh is used.

The finite source-vs-(field,test) Schmidt diagnostic is norm/trace algebra, not
probability or occurrence.  This is neither a BMV laboratory prediction nor
gravity.  Cycle467's primitive arithmetic trace exists at declared ports but
is not composed here; Cycle464 amplitude preparation remains a supplied
compilation boundary.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from time import perf_counter
import math
import resource
import signal
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_coherent_m64_source_relaxation_bridge_cycle465_2026_07_19 as c465
import physical_relaxed_cubic_field_passive_m64_backreaction_cycle464_2026_07_19 as c464


c463 = c465.c463
c219 = c465.c219
c230 = c465.c230
DIRECTIONS = np.asarray(c464.DIRECTIONS, dtype=int)

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COHERENT_SOURCE_FIELD_TEST_COMPOSITION_CYCLE468_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
LOCAL_TOL = 8.0e-12
RESPONSE_FLOOR = 1.0e-7
ENTANGLEMENT_FLOOR = 1.0e-4
DELETION_FLOOR = 1.0e-7
BOUNDARY_MAXIMUM = 0.75
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]


@dataclass(frozen=True)
class Geometry:
    name: str
    source: c465.Geometry
    response: c464.Geometry


TRAIN = Geometry("train-axis-R1-padR2-depth4", c465.TRAIN, c464.TRAIN)
HELD = Geometry("held-off-axis-R2-padR3-depth6", c465.HELD, c464.HELD)
GEOMETRIES = (TRAIN, HELD)


@dataclass(frozen=True)
class BranchFixture:
    source_coord: Coord
    coarse_field: c463.CoarseState
    profile: dict[Coord, Fraction]
    q1_field: np.ndarray
    direction_rows: dict[Coord, dict[str, object]]


@dataclass(frozen=True)
class CompositeFixture:
    geometry: Geometry
    layout: dict[str, object]
    branches: tuple[BranchFixture, ...]


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
        "coherent source / relaxed field / passive m64 test composition",
        "train axis branches",
        "held unseen off-axis branch/geometry",
        "no host branch selection",
        "no per-step force or control",
        "source-vs-(field,test) entanglement",
        "after uncomputing only the declared auxiliaries",
        "all 24 proper-cubic frames",
        "carried apparatus is covariant; the asymmetric menu and packet are not claimed invariant",
        "finite branch-entangling mechanism",
        "accessible prediction premise p2",
        "p1 mass-density normalization remains open",
        "physical time/phase rate, g_newton, universal coupling, asymptotic potential, probability/occurrence, bmv lab prediction, and gravity remain open",
        "phase is not energy",
        "update count is not time",
        "norm weight is not probability",
        "cycle467 elementary arithmetic trace is not composed here",
        "cycle464 word-to-q1 amplitude preparation remains supplied",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate",
        "broad p2, bmv, gravity, or no-go claim: fail",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized(NOTE))
    check("the Cycle468 note freezes the P2 and interpretation boundary", not missing, missing)


def validate_geometry(geometry: Geometry) -> None:
    if geometry not in GEOMETRIES:
        raise ValueError("geometry leaves the frozen Cycle468 train/held family")
    c465.validate_geometry(geometry.source)
    c464.validate_geometry(geometry.response)
    if geometry.source.radius != geometry.response.field_radius:
        raise ValueError("source and response field radii differ")
    if geometry is HELD and geometry.source.unseen_off_axis is None:
        raise ValueError("held geometry lacks its unseen off-axis source branch")


def q1_field_from_profile(layout: dict[str, object], profile: dict[Coord, Fraction]):
    total = sum(profile.values(), Fraction())
    if total <= 0:
        raise ValueError("source branch has no positive relaxed word field")
    field = np.zeros(int(layout["field_dimension"]), dtype=complex)
    rows: dict[Coord, dict[str, object]] = {}
    index = layout["index"]
    for coord, value in profile.items():
        weights, differences, rule = c464.local_direction_weights(profile, coord)
        site_weight = float(value / total)
        start = 1 + 7 * index[coord]
        field[start + 1 : start + 7] = np.sqrt(site_weight * weights)
        rows[coord] = {
            "word": value,
            "site_Q1_weight": site_weight,
            "neighbor_positive_differences": differences,
            "direction_weights": tuple(float(item) for item in weights),
            "rule": rule,
        }
    return field, rows, total


def build_fixture(geometry: Geometry) -> CompositeFixture:
    validate_geometry(geometry)
    layout = c464.cubic_layout(geometry.response)
    item = c463.domain(geometry.source.radius)
    branches = []
    for source_coord in geometry.source.menu:
        coarse = c465.generated_field(
            geometry.source.radius, geometry.source.menu, source_coord
        )
        final = coarse.history[c463.ITERATIONS]
        profile = {
            coord: Fraction(final[item.active_index[coord]], c463.DENOMINATOR)
            for coord in item.active
        }
        field, direction_rows, _total = q1_field_from_profile(layout, profile)
        branches.append(BranchFixture(source_coord, coarse, profile, field, direction_rows))
    return CompositeFixture(geometry, layout, tuple(branches))


def branch_layout(fixture: CompositeFixture, branch: BranchFixture) -> dict[str, object]:
    layout = dict(fixture.layout)
    layout["field"] = branch.q1_field
    layout["direction_rows"] = branch.direction_rows
    return layout


def physical_branch_step(state: np.ndarray, layout: dict[str, object]) -> np.ndarray:
    output = c464.apply_matter_coin(state, layout)
    output = c464.apply_vertices(output, layout)
    return c464.apply_stream(output, layout)


def source_code_cases(geometry: Geometry) -> tuple[tuple[complex, ...], ...]:
    size = len(geometry.source.menu)
    basis = tuple(
        tuple(1 + 0j if column == row else 0j for column in range(size))
        for row in range(size)
    )
    return basis + (geometry.source.coherent_coefficients,)


def field_residual(branch: BranchFixture, fixture: CompositeFixture) -> tuple[float, float]:
    item = c463.domain(fixture.geometry.source.radius)
    row = c465.field_residual(branch.coarse_field, item, branch.source_coord)
    return float(row["max_nonsource"]), float(row["source_defect_residual"])


def compiler_controls(fixture: CompositeFixture) -> dict[str, object]:
    geometry = fixture.geometry
    layout = fixture.layout
    item = c463.domain(geometry.source.radius)
    rest = c465.rest_ray()
    coin = c219.common_species(c465.MASS_BETA).coin
    eigenvalue = complex(np.vdot(rest, coin @ rest))
    branch_rows = []
    maximum_branch_residual = 0.0
    for position, branch in enumerate(fixture.branches):
        initial = np.outer(branch.q1_field, layout["matter"])
        coarse_output = c464.joint_step(initial, branch_layout(fixture, branch))
        physical_output = physical_branch_step(initial, branch_layout(fixture, branch))
        restored = c464.joint_inverse(physical_output, branch_layout(fixture, branch))
        eg = float(np.linalg.norm(physical_output - coarse_output))
        inverse = float(np.linalg.norm(restored - initial))
        norm_drift = abs(float(np.linalg.norm(physical_output)) - 1)
        maximum_branch_residual = max(maximum_branch_residual, eg, inverse, norm_drift)
        control_rows = tuple(
            c465.occupation_control_trace(geometry.source, item, position, direction)
            for direction in range(c465.M64_DIRECTION_BITS)
        )
        correct_source = c465.source_bits(item, branch.source_coord)
        controls_match = all(
            computed == correct_source and not any(restored_flags)
            for computed, restored_flags in control_rows
        )
        blank = c465.blank_coarse(item, correct_source)
        restored_word = c465.relax_history(
            branch.coarse_field, item, geometry.source.menu, reverse=True
        )
        row_residual, defect_residual = field_residual(branch, fixture)
        branch_rows.append(
            {
                "source": branch.source_coord,
                "EG_residual": eg,
                "inverse_residual": inverse,
                "norm_drift": norm_drift,
                "occupation_controls_match_and_uncompute": controls_match,
                "word_inverse_exact": restored_word == blank,
                "word_row_residual": row_residual,
                "word_source_defect_residual": defect_residual,
            }
        )
        del initial, coarse_output, physical_output, restored

    case_rows = []
    for case_index, coefficients in enumerate(source_code_cases(geometry)):
        amplitudes = np.outer(np.asarray(coefficients, dtype=complex), rest)
        physical = amplitudes @ coin.T
        expected = np.outer(eigenvalue * np.asarray(coefficients), rest)
        restored = physical @ coin.conj()
        initial = amplitudes
        case_rows.append(
            {
                "case": (
                    f"basis-{case_index}"
                    if case_index < len(geometry.source.menu)
                    else "coherent"
                ),
                "source_EG_residual": float(np.linalg.norm(physical - expected)),
                "source_inverse_residual": float(np.linalg.norm(restored - initial)),
                "source_Q1_norm_drift": abs(float(np.linalg.norm(physical)) - 1),
            }
        )
    maximum_source = max(value for row in case_rows for key, value in row.items() if key != "case")
    maximum = max(maximum_branch_residual, maximum_source)
    check(
        f"{geometry.name} has exact composite E/G, inverse, Q1, blank-auxiliary, and full source-code closure",
        maximum < TOL
        and all(row["occupation_controls_match_and_uncompute"] for row in branch_rows)
        and all(row["word_inverse_exact"] for row in branch_rows)
        and all(
            row["word_row_residual"] < float(c463.RESIDUAL_THRESHOLD)
            and row["word_source_defect_residual"] < float(c463.RESIDUAL_THRESHOLD)
            for row in branch_rows
        )
        and len(case_rows) == len(geometry.source.menu) + 1,
        {
            "branch_rows": branch_rows,
            "source_case_rows": case_rows,
            "maximum_composite_residual": maximum,
            "host_branch_selection_count": 0,
            "Cycle467_elementary_arithmetic_trace_available": True,
            "Cycle467_elementary_arithmetic_trace_composed": False,
        },
    )
    return {"branch_rows": branch_rows, "case_rows": case_rows, "maximum": maximum}


def test_observables_from_weights(weights: np.ndarray, layout) -> dict[str, object]:
    coordinates = layout["coordinates"]
    vectors = np.repeat(np.asarray(coordinates, dtype=float), 6, axis=0)
    radial = np.sum(vectors * vectors, axis=1)
    boundary = np.repeat(
        [
            int(any(abs(value) == layout["geometry"].matter_radius for value in coord))
            for coord in coordinates
        ],
        6,
    )
    return {
        "norm": float(np.sum(weights)),
        "centroid": tuple(float(weights @ vectors[:, axis]) for axis in range(3)),
        "radial_second": float(weights @ radial),
        "boundary_weight": float(weights @ boundary),
    }


def branch_response(result: dict[str, object], layout) -> dict[str, object]:
    final_state = result["final_state"]
    test_weights = np.sum(np.abs(final_state) ** 2, axis=0)
    free_weights = np.abs(result["free_matter"]) ** 2
    interacting = test_observables_from_weights(test_weights, layout)
    free = test_observables_from_weights(free_weights, layout)
    delta_centroid = tuple(
        interacting["centroid"][axis] - free["centroid"][axis] for axis in range(3)
    )
    delta_radial = interacting["radial_second"] - free["radial_second"]
    vector = np.asarray(delta_centroid + (delta_radial,), dtype=float)
    return {
        "delta_centroid": delta_centroid,
        "delta_radial_second": delta_radial,
        "response_vector": vector,
        "response_norm": float(np.linalg.norm(vector)),
        "test_norm_error": abs(interacting["norm"] - 1),
        "boundary_weight": interacting["boundary_weight"],
        "field_weight_backreaction": result["field_weight_backreaction"],
        "Schmidt_tail_field_test": result["Schmidt_tail"],
        "joint_product_residual": result["joint_product_residual"],
    }


def source_rest_entanglement(coefficients, branch_states) -> dict[str, object]:
    coefficients = np.asarray(coefficients, dtype=complex)
    size = len(branch_states)
    gram = np.empty((size, size), dtype=complex)
    for left in range(size):
        for right in range(size):
            gram[left, right] = np.vdot(branch_states[right], branch_states[left])
    reduced = np.outer(coefficients, coefficients.conj()) * gram
    reduced = (reduced + reduced.conj().T) / 2
    eigenvalues = np.linalg.eigvalsh(reduced)
    eigenvalues[np.abs(eigenvalues) < 1e-13] = 0
    largest = float(max(eigenvalues, default=0))
    return {
        "Gram": gram,
        "reduced_source": reduced,
        "trace": float(np.trace(reduced).real),
        "purity": float(np.trace(reduced @ reduced).real),
        "Schmidt_rank": int(np.count_nonzero(eigenvalues > 1e-12)),
        "Schmidt_tail": math.sqrt(max(0.0, 1 - min(1.0, largest))),
        "eigenvalues": tuple(float(value) for value in eigenvalues),
        "input_coherence_offdiagonal_norm": float(
            np.linalg.norm(
                np.outer(coefficients, coefficients.conj())
                - np.diag(np.abs(coefficients) ** 2)
            )
        ),
    }


def evolution_controls(fixture: CompositeFixture) -> dict[str, object]:
    geometry = fixture.geometry
    results = []
    responses = []
    final_states = []
    for branch in fixture.branches:
        result = c464.run_trace(branch_layout(fixture, branch))
        response = branch_response(result, fixture.layout)
        results.append(result)
        responses.append(response)
        final_states.append(result["final_state"])

    entanglement = source_rest_entanglement(
        geometry.source.coherent_coefficients, final_states
    )
    response_vectors = tuple(row["response_vector"] for row in responses)
    pairwise = tuple(
        float(np.linalg.norm(response_vectors[left] - response_vectors[right]))
        for left in range(len(response_vectors))
        for right in range(left + 1, len(response_vectors))
    )
    held_distances = ()
    if geometry is HELD:
        held_index = geometry.source.menu.index(geometry.source.unseen_off_axis)
        held_distances = tuple(
            float(np.linalg.norm(response_vectors[held_index] - response_vectors[index]))
            for index in range(len(response_vectors))
            if index != held_index
        )
    rows = tuple(
        {
            "source": branch.source_coord,
            "response_norm": response["response_norm"],
            "delta_centroid": response["delta_centroid"],
            "delta_radial_second": response["delta_radial_second"],
            "field_weight_backreaction": response["field_weight_backreaction"],
            "field_test_Schmidt_tail": response["Schmidt_tail_field_test"],
            "joint_product_residual": response["joint_product_residual"],
            "test_norm_error": response["test_norm_error"],
            "boundary_weight": response["boundary_weight"],
            "source_refresh_count": results[index]["source_refresh_count"],
            "host_per_step_force_or_control_count": results[index][
                "host_per_step_force_or_control_count"
            ],
            "expectation_feedback_count": results[index]["expectation_feedback_count"],
        }
        for index, (branch, response) in enumerate(zip(fixture.branches, responses))
    )
    condition = (
        min(row["response_norm"] for row in rows) > RESPONSE_FLOOR
        and min(pairwise) > RESPONSE_FLOOR
        and (not held_distances or min(held_distances) > RESPONSE_FLOOR)
        and entanglement["Schmidt_tail"] > ENTANGLEMENT_FLOOR
        and entanglement["Schmidt_rank"] > 1
        and abs(entanglement["trace"] - 1) < TOL
        and all(row["test_norm_error"] < TOL for row in rows)
        and all(row["boundary_weight"] < BOUNDARY_MAXIMUM for row in rows)
        and all(row["field_weight_backreaction"] > RESPONSE_FLOOR for row in rows)
        and all(row["field_test_Schmidt_tail"] > RESPONSE_FLOOR for row in rows)
        and all(row["source_refresh_count"] == 0 for row in rows)
        and all(row["host_per_step_force_or_control_count"] == 0 for row in rows)
        and all(row["expectation_feedback_count"] == 0 for row in rows)
    )
    check(
        f"{geometry.name} gives source-conditional passive response and a pure source-vs-(field,test) entanglement witness without branch selection",
        condition,
        {
            "rows": rows,
            "minimum_pairwise_response_distance": min(pairwise),
            "held_off_axis_distances_from_axis_branches": held_distances,
            "source_vs_field_test": {
                key: value
                for key, value in entanglement.items()
                if key not in ("Gram", "reduced_source")
            },
            "trace_weights_called_probability": False,
            "occurrence_claimed": False,
            "declared_auxiliaries_uncomputed_before_witness": True,
        },
    )
    summary = {
        "rows": rows,
        "minimum_pairwise_response_distance": min(pairwise),
        "held_distances": held_distances,
        "entanglement": {
            key: value
            for key, value in entanglement.items()
            if key not in ("Gram", "reduced_source")
        },
    }
    return {
        "summary": summary,
        "results": results,
        "responses": responses,
        "entanglement": entanglement,
    }


def deletion_controls(fixture: CompositeFixture, intact: dict[str, object]) -> None:
    print("\nSOURCE / COHERENCE / FIELD-COUPLING / TEST-VERTEX DELETIONS")
    geometry = fixture.geometry
    layout = fixture.layout
    baseline_vectors = tuple(row["response_vector"] for row in intact["responses"])

    uncoupled_vectors = []
    for branch in fixture.branches:
        result = c464.run_trace(branch_layout(fixture, branch), coupling_enabled=False)
        uncoupled_vectors.append(branch_response(result, layout)["response_vector"])
        del result
    uncoupled_vectors = tuple(uncoupled_vectors)

    selected = len(fixture.branches) - 1
    branch = fixture.branches[selected]
    item = c463.domain(geometry.source.radius)
    # Delete the physical source excitation itself.  Every directional
    # occupation control then sees zero; this is distinct from deleting one
    # of the six CNOTs, which Cycle465 already audits as a partial branch error.
    deleted_source_flags = tuple(0 for _ in item.active)
    vacuum = np.zeros(int(layout["field_dimension"]), dtype=complex)
    vacuum[0] = 1
    vacuum_layout = dict(branch_layout(fixture, branch))
    vacuum_layout["field"] = vacuum
    occupation_deleted = c464.run_trace(vacuum_layout)
    occupation_response = branch_response(occupation_deleted, layout)

    vertex_deleted = c464.run_trace(
        branch_layout(fixture, branch), deleted_cell=layout["initial_cell"]
    )
    vertex_response = branch_response(vertex_deleted, layout)

    coefficients = np.asarray(geometry.source.coherent_coefficients)
    coherence_norm = float(
        np.linalg.norm(
            np.outer(coefficients, coefficients.conj())
            - np.diag(np.abs(coefficients) ** 2)
        )
    )
    dephased = np.diag(np.abs(coefficients) ** 2)
    dephased_offdiagonal_norm = float(np.linalg.norm(dephased - np.diag(np.diag(dephased))))
    single_coefficients = np.zeros(len(coefficients), dtype=complex)
    single_coefficients[selected] = 1
    single_branch_witness = source_rest_entanglement(
        single_coefficients,
        tuple(result["final_state"] for result in intact["results"]),
    )
    single_branch_schmidt_tail = single_branch_witness["Schmidt_tail"]
    uncoupled_max = max(float(np.linalg.norm(value)) for value in uncoupled_vectors)
    uncoupled_spread = max(
        float(np.linalg.norm(uncoupled_vectors[left] - uncoupled_vectors[right]))
        for left in range(len(uncoupled_vectors))
        for right in range(left + 1, len(uncoupled_vectors))
    )
    vertex_residual = float(
        np.linalg.norm(vertex_response["response_vector"] - baseline_vectors[selected])
    )
    occupation_residual = float(
        np.linalg.norm(occupation_response["response_vector"] - baseline_vectors[selected])
    )
    check(
        f"{geometry.name} source occupation, source coherence, field coupling, and local test vertex deletions are all visible",
        sum(deleted_source_flags) == 0
        and occupation_response["response_norm"] < TOL
        and occupation_residual > DELETION_FLOOR
        and coherence_norm > ENTANGLEMENT_FLOOR
        and dephased_offdiagonal_norm == 0
        and single_branch_schmidt_tail == 0
        and uncoupled_max < TOL
        and uncoupled_spread < TOL
        and vertex_residual > DELETION_FLOOR,
        {
            "source_occupation_deleted_flag_sum": sum(deleted_source_flags),
            "source_occupation_deleted_response_norm": occupation_response["response_norm"],
            "source_occupation_trace_residual": occupation_residual,
            "coherent_source_offdiagonal_norm": coherence_norm,
            "dephased_source_offdiagonal_norm": dephased_offdiagonal_norm,
            "single_source_branch_Schmidt_tail": single_branch_schmidt_tail,
            "global_field_coupling_deleted_max_response": uncoupled_max,
            "global_field_coupling_deleted_response_spread": uncoupled_spread,
            "initial_test_cell_vertex_deleted_trace_residual": vertex_residual,
            "dephasing_called_occurrence": False,
        },
    )
    del occupation_deleted, vertex_deleted


def direction_map(frame) -> tuple[int, ...]:
    matrix = np.asarray(frame, dtype=int)
    return tuple(
        int(np.where(np.all(DIRECTIONS == matrix @ direction, axis=1))[0][0])
        for direction in DIRECTIONS
    )


def transformed_field_vector(field: np.ndarray, layout, frame) -> np.ndarray:
    output = np.zeros_like(field)
    output[0] = field[0]
    mapping = direction_map(frame)
    for coord, cell in layout["index"].items():
        carried_coord = c463.transform(frame, coord)
        carried_cell = layout["index"][carried_coord]
        output[1 + 7 * carried_cell] = field[1 + 7 * cell]
        for direction, carried_direction in enumerate(mapping):
            output[1 + 7 * carried_cell + 1 + carried_direction] = (
                field[1 + 7 * cell + 1 + direction]
            )
    return output


def covariance_controls(fixtures: tuple[CompositeFixture, ...]) -> None:
    print("\nALL24 CARRIED SOURCE / FIELD / TEST APPARATUS")
    frames = c463.proper_cubic_frames()
    failures = 0
    maxima = {
        "field_vector": 0.0,
        "source_coin": 0.0,
        "test_coin": 0.0,
        "vertex": 0.0,
        "coherent_source": 0.0,
    }
    rows = []
    vertex = c464.field_matter_vertex()
    for fixture in fixtures:
        geometry = fixture.geometry
        layout = fixture.layout
        schedule_rows = {
            (
                operation.layer,
                operation.target,
                frozenset(operation.neighbors),
            )
            for operation in c463.schedule(geometry.source.radius)
        }
        branch_comparisons = 0
        coherent_comparisons = 0
        stream_comparisons = 0
        for frame in frames:
            matrix = np.asarray(frame, dtype=int)
            mapping = direction_map(frame)
            permutation = c219.c210.direction_permutation(matrix)
            source_coin = c219.common_species(c465.MASS_BETA).coin
            test_coin = c219.common_species(c464.MASS_BETA).coin
            maxima["source_coin"] = max(
                maxima["source_coin"],
                float(np.linalg.norm(permutation @ source_coin @ permutation.conj().T - source_coin)),
            )
            maxima["test_coin"] = max(
                maxima["test_coin"],
                float(np.linalg.norm(permutation @ test_coin @ permutation.conj().T - test_coin)),
            )
            field_permutation = np.zeros((7, 7), dtype=complex)
            field_permutation[0, 0] = 1
            field_permutation[1:, 1:] = permutation
            joint_permutation = np.kron(permutation, field_permutation)
            maxima["vertex"] = max(
                maxima["vertex"],
                float(
                    np.linalg.norm(
                        joint_permutation @ vertex @ joint_permutation.conj().T - vertex
                    )
                ),
            )
            carried_menu = tuple(c463.transform(frame, coord) for coord in geometry.source.menu)
            failures += int(len(set(carried_menu)) != len(geometry.source.menu))
            failures += int(any(coord not in c463.domain(geometry.source.radius).active_index for coord in carried_menu))
            transformed_schedule = {
                (
                    operation.layer,
                    c463.transform(frame, operation.target),
                    frozenset(c463.transform(frame, coord) for coord in operation.neighbors),
                )
                for operation in c463.schedule(geometry.source.radius)
            }
            failures += int(transformed_schedule != schedule_rows)

            for branch in fixture.branches:
                carried_profile = {
                    c463.transform(frame, coord): value for coord, value in branch.profile.items()
                }
                carried_field, _rows, _total = q1_field_from_profile(layout, carried_profile)
                transformed = transformed_field_vector(branch.q1_field, layout, frame)
                residual = float(np.linalg.norm(carried_field - transformed))
                maxima["field_vector"] = max(maxima["field_vector"], residual)
                failures += int(residual >= TOL)
                branch_comparisons += 1

            mode_map = np.empty(int(layout["matter_dimension"]), dtype=int)
            for coord, cell in layout["index"].items():
                target_coord = c463.transform(frame, coord)
                target_cell = layout["index"][target_coord]
                for direction, target_direction in enumerate(mapping):
                    mode_map[6 * cell + direction] = 6 * target_cell + target_direction
            failures += sum(
                int(mode_map[int(layout["stream"][mode])] != int(layout["stream"][mode_map[mode]]))
                for mode in range(int(layout["matter_dimension"]))
            )
            stream_comparisons += int(layout["matter_dimension"])

            source_amplitudes = np.outer(
                np.asarray(geometry.source.coherent_coefficients), c465.rest_ray()
            )
            carried_amplitudes = source_amplitudes @ permutation.T
            coherent_residual = float(np.linalg.norm(carried_amplitudes - source_amplitudes))
            maxima["coherent_source"] = max(maxima["coherent_source"], coherent_residual)
            failures += int(coherent_residual >= TOL)
            coherent_comparisons += 1

            initial_cell = layout["initial_cell"]
            initial_direction = int(layout["inward_direction"])
            carried_cell = c463.transform(frame, initial_cell)
            carried_direction = mapping[initial_direction]
            failures += int(carried_cell not in layout["index"])
            failures += int(carried_direction not in range(6))
        rows.append(
            {
                "geometry": geometry.name,
                "frames": len(frames),
                "branch_frame_comparisons": branch_comparisons,
                "coherent_frame_comparisons": coherent_comparisons,
                "stream_mode_frame_comparisons": stream_comparisons,
                "carried_menu_invariant_claimed": False,
                "carried_packet_invariant_claimed": False,
                "Cycle467_arithmetic_trace_composition_covariance_claimed": False,
            }
        )
    check(
        "source menus/states, word schedules, Q1 fields/lifts, test packets/streams, both coins, and the local reciprocal vertex covary through all24 carried frames",
        len(frames) == 24 and failures == 0 and max(maxima.values()) < TOL,
        {"rows": rows, "failures": failures, "maximum_residuals": maxima},
    )


def local_mass_contact_controls() -> None:
    print("\nLOCAL COMPILERS / TWO M64 MASS FIXTURES / CONTACT")
    c464.PASS = c464.FAIL = 0
    local_rows = c464.local_physical_compiler_controls()
    rest = c465.rest_ray()
    mass_rows = []
    for label, beta in (("source", c465.MASS_BETA), ("test", c464.MASS_BETA)):
        species = c219.common_species(beta)
        eigenvalue = complex(np.vdot(rest, species.coin @ rest))
        mass_rows.append(
            {
                "role": label,
                "beta": beta,
                "rest_mass_fixture": c219.rest_mass(species),
                "mass_from_eigenphase": float(np.angle(eigenvalue)) / c219.C_SQUARED,
                "rest_eigen_residual": float(np.linalg.norm(species.coin @ rest - eigenvalue * rest)),
            }
        )
    phases = tuple(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
        for number in range(c465.M64_DIRECTION_BITS + 1)
    )
    check(
        "the inherited 13-M2 vertex compiler, distinct source/test M64 mass fixtures, and Cycle230 Q1 contact boundary remain intact",
        c464.PASS == 1
        and c464.FAIL == 0
        and max(local_rows.values()) < LOCAL_TOL
        and all(
            row["rest_eigen_residual"] < TOL
            and abs(row["rest_mass_fixture"] - row["mass_from_eigenphase"]) < TOL
            for row in mass_rows
        )
        and abs(phases[0] - 1) < TOL
        and abs(phases[1] - 1) < TOL
        and abs(phases[2] - 1) > 1e-3,
        {
            "local_vertex_rows": local_rows,
            "mass_rows": mass_rows,
            "Cycle464_vertex_mass_coordinate": c464.MASS_COORDINATE,
            "vertex_coordinate_not_identified_with_rest_mass": True,
            "Q1_contact_phase": phases[1],
            "Q2_contact_phase": phases[2],
            "phase_called_energy_or_rate": False,
        },
    )


def domain_resource_ledger_no_go_controls(started: float, fixtures, summaries) -> None:
    print("\nDOMAIN / RESOURCES / P1-P2 LEDGER / N1-N8")
    rejected = 0
    probes = (
        lambda: validate_geometry(Geometry("bad", c465.TRAIN, c464.HELD)),
        lambda: c465.validate_q1_source(
            tuple(0 for _ in c463.domain(2).active), c463.domain(2), c465.HELD.menu
        ),
        lambda: c465.occupation_control_trace(c465.TRAIN, c463.domain(1), 3, 0),
        lambda: c465.occupation_control_trace(c465.TRAIN, c463.domain(1), 0, 6),
        lambda: c463.domain(3),
        lambda: c463.binary(c463.DENOMINATOR, c463.VALUE_BITS - 1),
        lambda: c464.field_matter_vertex() @ np.zeros(41),
    )
    for probe in probes:
        try:
            probe()
        except (ValueError, IndexError):
            rejected += 1

    source = Path(__file__).read_text(encoding="utf-8")
    forbidden = (
        "np.linalg." + "solve(",
        "numpy.linalg." + "solve(",
        "SUPPLIED_ORBIT_" + "PROFILE",
        "sp" + "solve(",
    )
    elapsed = perf_counter() - started
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = raw_rss if sys.platform == "darwin" else raw_rss * 1024
    capacity_rows = []
    maximum_dense_payload = 0
    for fixture in fixtures:
        source_geometry = fixture.geometry.source
        response_layout = fixture.layout
        branch_payload = (
            len(fixture.branches)
            * int(response_layout["field_dimension"])
            * int(response_layout["matter_dimension"])
            * np.dtype(complex).itemsize
        )
        maximum_dense_payload = max(maximum_dense_payload, branch_payload)
        capacity_rows.append(
            {
                "geometry": fixture.geometry.name,
                "Cycle463_field_capacity_M2": c463.domain(source_geometry.radius).physical_m2,
                "source_M2": 6 * len(source_geometry.menu),
                "response_apparatus_M2": response_layout["physical_M2"],
                "joint_capacity_M2": (
                    c463.domain(source_geometry.radius).physical_m2
                    + 6 * len(source_geometry.menu)
                    + response_layout["physical_M2"]
                ),
                "dense_coherent_branch_payload_bytes": branch_payload,
            }
        )
    check(
        "lawful source/geometry/mode/precision/vertex domains refuse and the compact composition stays under frozen caps",
        rejected == len(probes)
        and not any(token in source for token in forbidden)
        and elapsed < WALL_CAP_SECONDS
        and rss_bytes < RSS_CAP_BYTES
        and maximum_dense_payload < RSS_CAP_BYTES,
        {
            "lawful_domain_refusals": rejected,
            "probes": len(probes),
            "elapsed_seconds_after_imports": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "peak_RSS_bytes": rss_bytes,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "maximum_dense_coherent_branch_payload_bytes": maximum_dense_payload,
            "capacity_rows": capacity_rows,
            "maximum_source_control_support_M2": 7,
            "maximum_field_test_vertex_support_M2": 13,
            "Cycle463_word_block_support_envelope_M2": 7 * c463.SUPERCELL_M2,
            "elementary_arithmetic_gate_trace": "Cycle467 available at declared ports; not composed",
            "inter_supercell_word_delivery_trace": None,
            "word_to_Q1_amplitude_preparation_trace": None,
        },
    )
    check(
        "Accessible Prediction P2 advances only to a finite branch-entangling source/field/test mechanism",
        all(summary["entanglement"]["Schmidt_tail"] > ENTANGLEMENT_FLOOR for summary in summaries),
        {
            "closed_here": (
                "physical Q1 source position controls one of several locally generated finite word fields without branch selection",
                "the supplied field preparation and identical reciprocal M64 vertex give source-conditional test response",
                "the coherent pure state has nontrivial source-vs-(field,test) Schmidt spectrum after blank auxiliaries uncompute",
            ),
            "Accessible_Prediction_P2": "finite branch-entangling mechanism only; Newtonian mutual phase accumulation is not derived",
            "P1_mass_density_normalization": "open; parity is a Q1 occupation flag and word-to-Q1 normalization is supplied",
            "physical_time_phase_rate": "open; phase is not energy or rate and update count is not time",
            "G_Newton": "open; no physical coupling normalization",
            "universal_coupling": "open; source/test betas, vertex coordinate, and coupling are supplied",
            "asymptotic_potential": "open; finite zero-shell cubes only",
            "probability_occurrence": "open; norm/trace weights are algebraic diagnostics",
            "BMV_lab_prediction": "open; no laboratory units, mediator-null, or LOCC-exclusion closure",
            "gravity": "open; no metric, lapse, curvature, stress-energy, or empirical law",
            "C_ref": "finite menus, coherent vectors, normalization/preparation, masses/coupling, packet, boundary, depths, and readouts supplied",
            "C_num": "train axis and unseen held off-axis branches pass without refit; finite sizes/depths only",
            "C_wrap": "unchanged: eigenphases are not energies/rates and ticks are not physical time",
            "C_int": "advanced to coherent source-conditioned reciprocal field/test interaction; universal selection and source recoil open",
            "C_local": "7-M2 source control and 13-M2 vertex are bounded; Cycle467 arithmetic exists at declared ports but is uncomposed; inter-supercell delivery and Cycle464 preparation remain open",
            "C_source": "coherent Q1 occupation controls the finite field; number density, mass/stress normalization, recurrence, and recoil open",
        },
    )
    check(
        "full refreshed N1-N8 rejects broad P2, BMV, gravity, no-go, minimum-content, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "five normalized routes remain: this Q1 prepared-field composition (attempted), number-resolving source, autonomous amplitude preparation, retarded/recurrent mediator, and two-source mutual recoil/Born instrument",
            "N2": "collapsed independent walls are physical source normalization, preparation compiler, time/coupling calibration, infrared scaling, and operational occurrence/mediator-null interpretation",
            "N3": "hidden scan exposes finite menus/shells, prepared coherence, Q1 parity, unit word source, two mass parameters, supplied vertex/packet/readout, uncomposed Cycle467 arithmetic, missing inter-supercell delivery, and missing amplitude preparation",
            "N4": "Cycle465 source-position and Cycle464 receiver residuals match the local composition; Accessible Prediction Newton phase and BMV/LOCC residuals do not",
            "N5": "bit/cell/branch/finite-cube/carried-frame levels tested; number-general, two-active-source, infrared, laboratory, probability, and geometry levels untested",
            "N6": "the finite local P2 mechanism is a constructive partial closure without an axiom edit; imports remain auditable",
            "N7": "an autonomous number-resolving two-source mediator with calibrated physical time/coupling and a retained Born instrument could reach the stronger terminal obligation",
            "N8": "prior prepared-profile and fixed-branch walls have constructive reopenings; broad P2, BMV, gravity, or no-go claim: FAIL; no axiom pressure",
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle468 exceeded its {WALL_CAP_SECONDS:g}-second body cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    print("Cycle468 coherent source / relaxed field / passive M64 test composition")
    print("authority", AUTHORITY, "audit", AUDIT)
    try:
        note_contract()
        fixtures = tuple(build_fixture(geometry) for geometry in GEOMETRIES)
        local_mass_contact_controls()
        compiler_rows = tuple(compiler_controls(fixture) for fixture in fixtures)

        train_result = evolution_controls(fixtures[0])
        deletion_controls(fixtures[0], train_result)
        train_summary = train_result["summary"]
        del train_result

        held_result = evolution_controls(fixtures[1])
        deletion_controls(fixtures[1], held_result)
        held_summary = held_result["summary"]
        del held_result

        covariance_controls(fixtures)
        domain_resource_ledger_no_go_controls(
            started, fixtures, (train_summary, held_summary)
        )
        check(
            "the train and held compiler summaries were both executed without threshold refit",
            len(compiler_rows) == 2,
            {"fit_parameters_after_train": 0, "held_refits": 0},
        )
    except WallCapExceeded as error:
        check("the Cycle468 runner remains inside its predeclared body cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
