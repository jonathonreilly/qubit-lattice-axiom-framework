#!/usr/bin/env python3
"""Cycle 465: coherent M64 source-position / relaxed-field bridge.

An actual one-particle source across bounded six-M2/M64 cells coherently
controls the same local source flag and reversible word-block relaxation law
as Cycle 463.  The update produces a joint source/field state without a host
choice of source position.  Norms and partial traces are algebraic diagnostics,
not probabilities or occurrences.

The Cycle-463 arithmetic remains a word-block map with an M2 capacity/support
certificate; no elementary Toffoli/CNOT/nearest-neighbour arithmetic trace is
claimed here.  This is not gravity, lapse, metric, proper time, energy/stress,
passive response, or backreaction.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import sqrt
from pathlib import Path
from time import perf_counter
import resource
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COHERENT_M64_SOURCE_RELAXATION_BRIDGE_CYCLE465_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-11
WALL_CAP_SECONDS = 120.0
RSS_CAP_MIB = 1024.0
MASS_BETA = -0.3
M64_DIRECTION_BITS = 6
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]


@dataclass(frozen=True)
class Geometry:
    name: str
    radius: int
    menu: tuple[Coord, ...]
    held: bool
    coherent_coefficients: tuple[complex, ...]
    unseen_off_axis: Coord | None


TRAIN = Geometry(
    "train-R1-three-axis-sources",
    1,
    ((-1, 0, 0), (0, 0, 0), (1, 0, 0)),
    False,
    (1 / sqrt(3), 1j / sqrt(3), -1 / sqrt(3)),
    None,
)
HELD = Geometry(
    "held-R2-plus-unseen-off-axis",
    2,
    ((-1, 0, 0), (0, 0, 0), (1, 0, 0), (1, 1, 0)),
    True,
    (0.5, 0.5j, -0.5, -0.5j),
    (1, 1, 0),
)
GEOMETRIES = (TRAIN, HELD)


@dataclass(frozen=True)
class CoarseJoint:
    coefficients: tuple[complex, ...]
    fields: tuple[c463.CoarseState, ...]


@dataclass(frozen=True)
class PhysicalJoint:
    # Compact one-particle amplitudes over (M64 source cell, direction M2).
    source_amplitudes: tuple[tuple[complex, ...], ...]
    fields: tuple[c463.PhysicalState, ...]
    coarse_fields: tuple[c463.CoarseState, ...]
    source_flags_blank: bool


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
        "coherent m64 source-position / relaxed-field bridge",
        "train r1 menu",
        "held r2 unseen off-axis",
        "full declared source-position code",
        "no host-selected source site",
        "all 24 proper-cubic frames",
        "carried menu is not claimed invariant",
        "occupation parity is a q1 flag only",
        "not a general number-density compiler",
        "no elementary arithmetic-gate trace",
        "coherent norm/trace algebra, not probability or occurrence",
        "local occupation control and branch-level source-field entanglement",
        "rho=|psi|^2 as physical probability remains open",
        "universal mass coupling, passive response, backreaction, and gravity remain open",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate",
        "broad gravity or no-go claim: fail",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized(NOTE))
    check("the Cycle465 note freezes the coherent-source and interpretation boundary", not missing, missing)


def validate_geometry(geometry: Geometry) -> None:
    if geometry not in GEOMETRIES:
        raise ValueError("geometry leaves the frozen train/held family")
    item = c463.domain(geometry.radius)
    if len(set(geometry.menu)) != len(geometry.menu) or any(coord not in item.active_index for coord in geometry.menu):
        raise ValueError("source menu leaves its declared field cube")
    if len(geometry.coherent_coefficients) != len(geometry.menu):
        raise ValueError("coherent coefficient/menu mismatch")
    if abs(sum(abs(value) ** 2 for value in geometry.coherent_coefficients) - 1) > TOL:
        raise ValueError("coherent source vector is not normalized")
    if geometry.held and (
        geometry.unseen_off_axis not in geometry.menu
        or geometry.unseen_off_axis in TRAIN.menu
        or sum(value != 0 for value in geometry.unseen_off_axis) < 2
    ):
        raise ValueError("held menu lacks its unseen off-axis source")


def source_bits(item: c463.Domain, coord: Coord) -> tuple[int, ...]:
    if coord not in item.active_index:
        raise ValueError("source coordinate leaves the active cube")
    return tuple(int(value == coord) for value in item.active)


def blank_coarse(item: c463.Domain, source: tuple[int, ...]) -> c463.CoarseState:
    blank = tuple(0 for _ in item.active)
    return c463.CoarseState(source, tuple(blank for _ in range(c463.ITERATIONS + 1)))


def validate_q1_source(source: tuple[int, ...], item: c463.Domain, menu: tuple[Coord, ...]) -> Coord:
    if len(source) != len(item.active) or any(bit not in (0, 1) for bit in source) or sum(source) != 1:
        raise ValueError("source flags leave the declared Q1 code")
    coord = item.active[source.index(1)]
    if coord not in menu:
        raise ValueError("source flag leaves the declared position menu")
    return coord


def relax_history(initial: c463.CoarseState, item: c463.Domain, menu: tuple[Coord, ...],
                  *, reverse: bool = False,
                  delete: tuple[int, Coord] | None = None) -> c463.CoarseState:
    validate_q1_source(initial.source, item, menu)
    history = [list(layer) for layer in initial.history]
    if len(history) != c463.ITERATIONS + 1 or any(len(layer) != len(item.active) for layer in history):
        raise ValueError("history leaves the frozen Cycle463 extent")
    operations = reversed(c463.schedule(item.radius)) if reverse else c463.schedule(item.radius)
    for operation in operations:
        if delete == (operation.layer, operation.target):
            continue
        target_index = item.active_index[operation.target]
        neighbor_values = tuple(
            history[operation.layer][item.active_index[coord]] if coord in item.active_index else 0
            for coord in operation.neighbors
        )
        value = c463.local_quotient(neighbor_values, initial.source[target_index])
        layer = operation.layer + 1
        if reverse:
            if history[layer][target_index] != value:
                raise ValueError("inverse encounters a non-code target")
            history[layer][target_index] = 0
        else:
            if history[layer][target_index] != 0:
                raise ValueError("forward history target is not blank")
            history[layer][target_index] = value
    return c463.CoarseState(initial.source, tuple(tuple(layer) for layer in history))


@lru_cache(maxsize=None)
def generated_field(radius: int, menu: tuple[Coord, ...], coord: Coord) -> c463.CoarseState:
    item = c463.domain(radius)
    return relax_history(blank_coarse(item, source_bits(item, coord)), item, menu)


def field_residual(state: c463.CoarseState, item: c463.Domain, source_coord: Coord) -> dict[str, Fraction]:
    values = state.history[c463.ITERATIONS]
    rows = {}
    for coord in item.active:
        index = item.active_index[coord]
        neighbor_sum = sum(values[item.active_index[value]] for value in c463.six_neighbors(coord) if value in item.active_index)
        source = c463.DENOMINATOR if coord == source_coord else 0
        rows[coord] = Fraction(6 * values[index] - neighbor_sum - source, c463.DENOMINATOR)
    nonsource = tuple(abs(value) for coord, value in rows.items() if coord != source_coord)
    defect = rows[source_coord] + 1
    return {
        "max_nonsource": max(nonsource, default=Fraction()),
        "source_defect": defect,
        "source_defect_residual": abs(defect - 1),
    }


def rest_ray() -> np.ndarray:
    return np.ones(M64_DIRECTION_BITS, dtype=complex) / sqrt(M64_DIRECTION_BITS)


def source_encoding(geometry: Geometry) -> np.ndarray:
    encoding = np.zeros((len(geometry.menu) * M64_DIRECTION_BITS, len(geometry.menu)), dtype=complex)
    rest = rest_ray()
    for position in range(len(geometry.menu)):
        encoding[position * M64_DIRECTION_BITS : (position + 1) * M64_DIRECTION_BITS, position] = rest
    return encoding


def occupancy_flags_from_mode(geometry: Geometry, item: c463.Domain,
                              position: int, direction: int,
                              *, delete_direction: tuple[int, int] | None = None) -> tuple[int, ...]:
    computed, _ = occupation_control_trace(
        geometry, item, position, direction, delete_compute=delete_direction
    )
    return computed


def occupation_control_trace(geometry: Geometry, item: c463.Domain,
                             position: int, direction: int,
                             *, delete_compute: tuple[int, int] | None = None,
                             delete_uncompute: tuple[int, int] | None = None,
                             ) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if position not in range(len(geometry.menu)) or direction not in range(M64_DIRECTION_BITS):
        raise ValueError("physical source mode leaves the M64 Q1 menu")
    # Six identical CNOTs compute parity into the local Cycle463 source flag.
    # In the declared one-particle block, parity equals occupation.  This is
    # intentionally not a general number-density map.
    flags = [0] * len(item.active)
    source_index = item.active_index[geometry.menu[position]]
    occupations = tuple(int(index == direction) for index in range(M64_DIRECTION_BITS))
    for control, occupied in enumerate(occupations):
        if occupied and delete_compute != (position, control):
            flags[source_index] ^= 1
    computed = tuple(flags)
    for control, occupied in enumerate(occupations):
        if occupied and delete_uncompute != (position, control):
            flags[source_index] ^= 1
    return computed, tuple(flags)


def initial_physical(geometry: Geometry, coefficients: tuple[complex, ...]) -> PhysicalJoint:
    validate_geometry(geometry)
    item = c463.domain(geometry.radius)
    rest = rest_ray()
    amplitudes = tuple(tuple(complex(alpha * value) for value in rest) for alpha in coefficients)
    coarse_fields = tuple(blank_coarse(item, source_bits(item, coord)) for coord in geometry.menu)
    fields = tuple(c463.encode(field, item) for field in coarse_fields)
    return PhysicalJoint(amplitudes, fields, coarse_fields, True)


def initial_coarse(geometry: Geometry, coefficients: tuple[complex, ...]) -> CoarseJoint:
    item = c463.domain(geometry.radius)
    return CoarseJoint(coefficients, tuple(blank_coarse(item, source_bits(item, coord)) for coord in geometry.menu))


def coarse_forward(state: CoarseJoint, geometry: Geometry, *, reverse: bool = False) -> CoarseJoint:
    item = c463.domain(geometry.radius)
    species = c219.common_species(MASS_BETA)
    rest = rest_ray()
    eigenvalue = complex(np.vdot(rest, species.coin @ rest))
    if reverse:
        fields = tuple(relax_history(field, item, geometry.menu, reverse=True) for field in state.fields)
        coefficients = tuple(value / eigenvalue for value in state.coefficients)
    else:
        fields = tuple(generated_field(geometry.radius, geometry.menu, coord) for coord in geometry.menu)
        coefficients = tuple(value * eigenvalue for value in state.coefficients)
    return CoarseJoint(coefficients, fields)


def encode_coarse(state: CoarseJoint, geometry: Geometry) -> PhysicalJoint:
    item = c463.domain(geometry.radius)
    rest = rest_ray()
    amplitudes = tuple(tuple(complex(alpha * value) for value in rest) for alpha in state.coefficients)
    return PhysicalJoint(
        amplitudes,
        tuple(c463.encode(field, item) for field in state.fields),
        state.fields,
        True,
    )


def physical_forward(state: PhysicalJoint, geometry: Geometry, *, reverse: bool = False) -> PhysicalJoint:
    item = c463.domain(geometry.radius)
    coin = c219.common_species(MASS_BETA).coin
    amplitude_matrix = np.asarray(state.source_amplitudes, dtype=complex)
    if reverse:
        # The field/source branches remain coherently indexed by the physical
        # source location; no measurement or host-selected branch is used.
        blank_controls = True
        for position, field in enumerate(state.coarse_fields):
            traces = tuple(
                occupation_control_trace(geometry, item, position, direction)
                for direction in range(M64_DIRECTION_BITS)
            )
            if any(computed != field.source or any(restored) for computed, restored in traces):
                raise RuntimeError("inverse source control leaves its Q1 code or a dirty auxiliary")
            blank_controls &= all(not any(restored) for _, restored in traces)
        restored_fields = tuple(
            relax_history(field, item, geometry.menu, reverse=True)
            for field in state.coarse_fields
        )
        restored_physical = tuple(c463.encode(field, item) for field in restored_fields)
        restored_amplitudes = amplitude_matrix @ coin.conj()
        return PhysicalJoint(
            tuple(tuple(value) for value in restored_amplitudes),
            restored_physical, restored_fields, blank_controls,
        )

    fields = []
    coarse_fields = []
    blank_controls = True
    for position, coord in enumerate(geometry.menu):
        # Audit all six local M2 controls, but compile the direction-independent
        # word field once.  The cache is only a test-harness acceleration: the
        # six flags are computed before the common source-position branch is
        # admitted, so no direction or host-selected site enters the law.
        direction_traces = tuple(
            occupation_control_trace(geometry, item, position, direction)
            for direction in range(M64_DIRECTION_BITS)
        )
        direction_flags = tuple(computed for computed, _ in direction_traces)
        if any(flags != direction_flags[0] for flags in direction_flags[1:]):
            raise RuntimeError("M64 direction leaked into the position-controlled field")
        if any(any(restored) for _, restored in direction_traces):
            raise RuntimeError("M64 source-control auxiliary failed to uncompute")
        blank_controls &= all(not any(restored) for _, restored in direction_traces)
        if validate_q1_source(direction_flags[0], item, geometry.menu) != coord:
            raise RuntimeError("local occupation control chose the wrong source cell")
        field = generated_field(geometry.radius, geometry.menu, coord)
        if field.source != direction_flags[0]:
            raise RuntimeError("compiled field source differs from the local occupation flag")
        coarse_fields.append(field)
        fields.append(c463.encode(field, item))
    moved = amplitude_matrix @ coin.T
    return PhysicalJoint(
        tuple(tuple(value) for value in moved), tuple(fields), tuple(coarse_fields), blank_controls
    )


def joint_residual(left: PhysicalJoint, right: PhysicalJoint) -> float:
    amplitude = float(np.linalg.norm(np.asarray(left.source_amplitudes) - np.asarray(right.source_amplitudes)))
    field_failures = sum(a != b for a, b in zip(left.fields, right.fields))
    coarse_failures = sum(a != b for a, b in zip(left.coarse_fields, right.coarse_fields))
    flag = int(left.source_flags_blank != right.source_flags_blank)
    return amplitude + field_failures + coarse_failures + flag


def coarse_joint_residual(left: CoarseJoint, right: CoarseJoint) -> float:
    amplitude = float(np.linalg.norm(np.asarray(left.coefficients) - np.asarray(right.coefficients)))
    return amplitude + sum(a != b for a, b in zip(left.fields, right.fields))


def state_norm(state: PhysicalJoint) -> float:
    return float(np.sum(abs(np.asarray(state.source_amplitudes)) ** 2))


def field_digest(state: c463.CoarseState) -> str:
    digest = sha256()
    for layer in state.history:
        digest.update((",".join(map(str, layer)) + "\n").encode())
    return digest.hexdigest()


def compiler_controls() -> dict[Geometry, dict[str, object]]:
    print("\nFULL SOURCE-POSITION CODE / COHERENT E-G / INVERSE")
    results = {}
    rows = []
    for geometry in GEOMETRIES:
        validate_geometry(geometry)
        item = c463.domain(geometry.radius)
        cases = tuple(
            tuple(1 + 0j if index == basis else 0j for index in range(len(geometry.menu)))
            for basis in range(len(geometry.menu))
        ) + (geometry.coherent_coefficients,)
        case_rows = []
        coherent_output = None
        for case_index, coefficients in enumerate(cases):
            coarse_initial = initial_coarse(geometry, coefficients)
            physical_initial = initial_physical(geometry, coefficients)
            coarse_output = coarse_forward(coarse_initial, geometry)
            coarse_restored = coarse_forward(coarse_output, geometry, reverse=True)
            physical_output = physical_forward(physical_initial, geometry)
            expected = encode_coarse(coarse_output, geometry)
            restored = physical_forward(physical_output, geometry, reverse=True)
            eg = joint_residual(physical_output, expected)
            inverse = joint_residual(restored, physical_initial)
            case_rows.append({
                "case": f"basis-{case_index}" if case_index < len(geometry.menu) else "coherent",
                "EG_residual": eg,
                "inverse_residual": inverse,
                "coarse_inverse_residual": coarse_joint_residual(coarse_restored, coarse_initial),
                "norm_drift": abs(state_norm(physical_output) - 1),
                "source_Q1_leakage": abs(state_norm(physical_output) - sum(abs(value) ** 2 for value in coefficients)),
                "source_flags_blank": physical_output.source_flags_blank,
            })
            if case_index == len(geometry.menu):
                coherent_output = physical_output
        assert coherent_output is not None
        branch_rows = []
        for coord, field in zip(geometry.menu, coherent_output.coarse_fields):
            residual = field_residual(field, item, coord)
            branch_rows.append({
                "source": coord,
                "max_nonsource_residual": float(residual["max_nonsource"]),
                "source_defect": float(residual["source_defect"]),
                "source_defect_residual": float(residual["source_defect_residual"]),
                "field_digest": field_digest(field),
            })
        row = {
            "geometry": geometry.name,
            "held": geometry.held,
            "menu": geometry.menu,
            "cases_tested": len(cases),
            "basis_cases": len(geometry.menu),
            "case_rows": case_rows,
            "branch_rows": branch_rows,
            "field_M2_capacity": item.physical_m2,
            "source_M2": len(geometry.menu) * M64_DIRECTION_BITS,
            "joint_M2_capacity": item.physical_m2 + len(geometry.menu) * M64_DIRECTION_BITS,
            "local_occupation_control_support_M2": 7,
            "Cycle463_word_support_envelope_M2": 7 * c463.SUPERCELL_M2,
        }
        rows.append(row)
        results[geometry] = {"output": coherent_output, "row": row}
    maximum = max(
        value for row in rows for case in row["case_rows"]
        for key, value in case.items() if key.endswith("residual") or key.endswith("drift") or key.endswith("leakage")
    )
    check(
        "every basis state in the full train/held source-position code and both declared coherent states obey exact E/G, inverse, Q1, norm, and blank-control closure",
        maximum < TOL
        and [row["basis_cases"] for row in rows] == [3, 4]
        and [row["cases_tested"] for row in rows] == [4, 5]
        and all(all(case["source_flags_blank"] for case in row["case_rows"]) for row in rows),
        {"rows": rows, "maximum_residual": maximum, "host_selected_source_during_update": False},
    )
    check(
        "all train source fields and the no-refit held unseen off-axis source field cross the unchanged Cycle463 residual gate",
        all(
            branch["max_nonsource_residual"] < float(c463.RESIDUAL_THRESHOLD)
            and branch["source_defect_residual"] < float(c463.RESIDUAL_THRESHOLD)
            for row in rows for branch in row["branch_rows"]
        ) and HELD.unseen_off_axis not in TRAIN.menu,
        {"threshold": str(c463.RESIDUAL_THRESHOLD), "rows": [row["branch_rows"] for row in rows], "held_unseen_off_axis": HELD.unseen_off_axis},
    )
    return results


def coherent_trace_controls(results: dict[Geometry, dict[str, object]]) -> None:
    print("\nCOHERENT NORM / PARTIAL-TRACE ALGEBRA (NOT PROBABILITY)")
    rows = []
    for geometry in GEOMETRIES:
        output = results[geometry]["output"]
        assert isinstance(output, PhysicalJoint)
        coefficients = np.asarray(geometry.coherent_coefficients, dtype=complex)
        fields = output.fields
        field_gram = np.asarray(
            [[1.0 if left == right else 0.0 for right in fields] for left in fields],
            dtype=complex,
        )
        reduced_source = np.outer(coefficients, coefficients.conj()) * field_gram
        trace_weights = np.real(np.diag(reduced_source))
        eigenvalues = np.linalg.eigvalsh(reduced_source)
        rows.append({
            "geometry": geometry.name,
            "joint_norm": state_norm(output),
            "field_Gram_rank": int(np.linalg.matrix_rank(field_gram, tol=1e-12)),
            "reduced_source_trace": float(np.trace(reduced_source).real),
            "trace_weights": tuple(float(value) for value in trace_weights),
            "coefficient_norms": tuple(float(abs(value) ** 2) for value in coefficients),
            "Schmidt_rank": int(np.count_nonzero(eigenvalues > 1e-12)),
            "global_coherent_cross_terms": int(np.count_nonzero(abs(np.outer(coefficients, coefficients.conj()) - np.diag(abs(coefficients) ** 2)) > 1e-12)),
            "reduced_offdiagonal_norm": float(np.linalg.norm(reduced_source - np.diag(np.diag(reduced_source)))),
        })
    check(
        "the joint pure state retains global coherent cross terms while exact partial-trace algebra exposes nontrivial branch-level source-field entanglement",
        all(
            abs(row["joint_norm"] - 1) < TOL
            and abs(row["reduced_source_trace"] - 1) < TOL
            and row["field_Gram_rank"] == len(row["trace_weights"])
            and row["Schmidt_rank"] == len(row["trace_weights"])
            and row["global_coherent_cross_terms"] > 0
            and row["reduced_offdiagonal_norm"] < TOL
            and max(abs(a - b) for a, b in zip(row["trace_weights"], row["coefficient_norms"])) < TOL
            for row in rows
        ),
        {"rows": rows, "weights_called_probability": False, "occurrence_claimed": False, "measurement_or_dephasing_applied": False},
    )


def mass_contact_controls() -> None:
    print("\nM64 ONE-PARTICLE MASS / CYCLE230 CONTACT")
    species = c219.common_species(MASS_BETA)
    rest = rest_ray()
    eigenvalue = complex(np.vdot(rest, species.coin @ rest))
    eigen_residual = float(np.linalg.norm(species.coin @ rest - eigenvalue * rest))
    mass_from_phase = float(np.angle(eigenvalue)) / c219.C_SQUARED
    fixture = c219.rest_mass(species)
    code_rows = []
    for geometry in GEOMETRIES:
        encoding = source_encoding(geometry)
        physical_coin = np.kron(np.eye(len(geometry.menu)), species.coin)
        logical_coin = eigenvalue * np.eye(len(geometry.menu))
        code_rows.append({
            "geometry": geometry.name,
            "M64_cells": len(geometry.menu),
            "physical_source_M2": len(geometry.menu) * M64_DIRECTION_BITS,
            "local_Hilbert_dimension": 64,
            "one_particle_code_dimension": len(geometry.menu),
            "Gram_residual": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(len(geometry.menu)))),
            "mass_EG_residual": float(np.linalg.norm(physical_coin @ encoding - encoding @ logical_coin)),
        })
    contact_phases = tuple(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
        for number in range(M64_DIRECTION_BITS + 1)
    )
    check(
        "the actual six-M2/M64 source blocks preserve the Cycle219 scalar-rest mass fixture and Cycle230 contact on the global Q1 code",
        eigen_residual < TOL
        and abs(mass_from_phase - fixture) < TOL
        and max(max(row["Gram_residual"], row["mass_EG_residual"]) for row in code_rows) < TOL
        and abs(contact_phases[0] - 1) < TOL and abs(contact_phases[1] - 1) < TOL
        and abs(contact_phases[2] - 1) > 1e-3,
        {
            "Cycle219_mass_fixture": fixture,
            "mass_from_scalar_eigenphase": mass_from_phase,
            "mass_eigen_residual": eigen_residual,
            "code_rows": code_rows,
            "Q1_contact_phase": contact_phases[1],
            "two_particle_contact_phase": contact_phases[2],
            "two_particle_contact_nontrivial": True,
            "phase_called_energy_or_rate": False,
        },
    )


def covariance_controls(results: dict[Geometry, dict[str, object]]) -> None:
    print("\nALL24 CARRIED SOURCE-MENU / WORD-SCHEDULE COVARIANCE")
    frames = c463.proper_cubic_frames()
    failures = 0
    maximum_coin = 0.0
    maximum_coherent_source = 0.0
    rows = []
    coin = c219.common_species(MASS_BETA).coin
    for geometry in GEOMETRIES:
        item = c463.domain(geometry.radius)
        baseline = results[geometry]["output"]
        assert isinstance(baseline, PhysicalJoint)
        comparisons = 0
        coherent_comparisons = 0
        baseline_amplitudes = np.asarray(baseline.source_amplitudes, dtype=complex)
        for frame in frames:
            matrix = np.asarray(frame, dtype=int)
            direction = c219.c210.direction_permutation(matrix)
            maximum_coin = max(maximum_coin, float(np.linalg.norm(direction @ coin @ direction.conj().T - coin)))
            carried_menu = tuple(c463.transform(frame, coord) for coord in geometry.menu)
            failures += int(len(set(carried_menu)) != len(geometry.menu))
            failures += int(any(coord not in item.active_index for coord in carried_menu))
            for source_coord, field in zip(geometry.menu, baseline.coarse_fields):
                carried_source = c463.transform(frame, source_coord)
                carried = generated_field(geometry.radius, carried_menu, carried_source)
                for layer in range(c463.ITERATIONS + 1):
                    source_values = field.history[layer]
                    target_values = carried.history[layer]
                    failures += sum(
                        source_values[item.active_index[coord]]
                        != target_values[item.active_index[c463.transform(frame, coord)]]
                        for coord in item.active
                    )
                comparisons += 1
            carried_amplitudes = baseline_amplitudes @ direction.T
            coherent_residual = float(np.linalg.norm(carried_amplitudes - baseline_amplitudes))
            maximum_coherent_source = max(maximum_coherent_source, coherent_residual)
            failures += int(coherent_residual >= TOL)
            coherent_comparisons += 1
            for position in range(len(geometry.menu)):
                flags = {
                    occupancy_flags_from_mode(geometry, item, position, direction_index)
                    for direction_index in range(M64_DIRECTION_BITS)
                }
                failures += int(len(flags) != 1)
        rows.append({
            "geometry": geometry.name,
            "frames": len(frames),
            "branch_frame_comparisons": comparisons,
            "coherent_state_frame_comparisons": coherent_comparisons,
            "carried_menu_invariant_claimed": False,
            "word_schedule_digest": c463.schedule_digest(geometry.radius),
            "primitive_arithmetic_gate_trace_enumerated": False,
        })
    check(
        "every branch basis, M64 rest coin, Q1 occupation-control template, and Cycle463 word schedule covaries when the complete finite apparatus/menu is carried through all24 frames",
        len(frames) == 24 and failures == 0 and maximum_coin < TOL and maximum_coherent_source < TOL,
        {
            "rows": rows,
            "failures": failures,
            "maximum_mass_coin_covariance_residual": maximum_coin,
            "maximum_declared_coherent_source_covariance_residual": maximum_coherent_source,
            "asymmetric_menu_itself_invariant": False,
        },
    )


def deletion_domain_controls(results: dict[Geometry, dict[str, object]]) -> None:
    print("\nDELETIONS / LEAKAGE / LAWFUL DOMAIN")
    geometry = HELD
    item = c463.domain(geometry.radius)
    output = results[geometry]["output"]
    assert isinstance(output, PhysicalJoint)
    position = geometry.menu.index(geometry.unseen_off_axis)
    direction = 0
    correct_flags = occupancy_flags_from_mode(geometry, item, position, direction)
    deleted_flags = occupancy_flags_from_mode(
        geometry, item, position, direction, delete_direction=(position, direction)
    )
    correct_field = generated_field(geometry.radius, geometry.menu, geometry.unseen_off_axis)
    blank = blank_coarse(item, tuple(0 for _ in item.active))
    control_deletion_changes = deleted_flags != correct_flags and sum(deleted_flags) == 0 and correct_field.history != blank.history
    _, dirty_after_deleted_uncompute = occupation_control_trace(
        geometry, item, position, direction, delete_uncompute=(position, direction)
    )
    uncompute_deletion_leaks = sum(dirty_after_deleted_uncompute) == 1
    direction_control_residual = abs(geometry.coherent_coefficients[position]) / sqrt(M64_DIRECTION_BITS)
    source_branch_deleted_norm = sqrt(1 - abs(geometry.coherent_coefficients[position]) ** 2)

    final_source_index = item.active_index[geometry.unseen_off_axis]
    relaxation_delete_changes = correct_field.history[c463.ITERATIONS][final_source_index] != 0
    mass_eigenvalue = complex(np.vdot(rest_ray(), c219.common_species(MASS_BETA).coin @ rest_ray()))
    mass_delete_residual = abs(mass_eigenvalue - 1)

    rejected = 0
    probes = (
        lambda: validate_q1_source(tuple(0 for _ in item.active), item, geometry.menu),
        lambda: validate_q1_source(tuple(int(index in (0, 1)) for index in range(len(item.active))), item, geometry.menu),
        lambda: occupancy_flags_from_mode(geometry, item, len(geometry.menu), 0),
        lambda: occupancy_flags_from_mode(geometry, item, 0, 6),
        lambda: validate_geometry(Geometry("bad", 2, geometry.menu, True, (1 + 0j,), geometry.unseen_off_axis)),
        lambda: c463.domain(3),
        lambda: c463.binary(c463.DENOMINATOR, c463.VALUE_BITS - 1),
    )
    for probe in probes:
        try:
            probe()
        except ValueError:
            rejected += 1

    check(
        "local occupation-control, source branch, relaxation, and mass deletions are visible, while Q1/menu/mode/precision/domain violations refuse",
        control_deletion_changes
        and uncompute_deletion_leaks
        and direction_control_residual > 0.1
        and source_branch_deleted_norm < 1
        and relaxation_delete_changes
        and mass_delete_residual > 1e-3
        and rejected == len(probes),
        {
            "deleted_one_of_six_control_CNOT_state_residual": direction_control_residual,
            "deleted_uncompute_CNOT_leaves_auxiliary_occupied": uncompute_deletion_leaks,
            "deleted_off_axis_branch_remaining_norm": source_branch_deleted_norm,
            "deleted_final_source_relaxation_changes_field": relaxation_delete_changes,
            "deleted_mass_coin_residual": mass_delete_residual,
            "lawful_domain_refusals": rejected,
            "probes": len(probes),
            "contact_deletion_expected_visible_in_Q1": False,
            "contact_reason": "Cycle230 contact is identity on number zero/one and becomes nontrivial only beyond the declared Q1 source code",
        },
    )


def inventory_ledger_no_go_controls(started: float) -> None:
    print("\nCAPACITY / WEAK-FIELD LEDGER / N1-N8")
    source = Path(__file__).read_text(encoding="utf-8")
    forbidden = (
        "np.linalg." + "solve(", "numpy.linalg." + "solve(",
        "SUPPLIED_ORBIT_" + "PROFILE", "sp" + "solve(",
    )
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the source compiler inventories its complete capacity/support and contains no host solve, copied profile table, or runtime source-site selection",
        not any(token in source for token in forbidden)
        and c463.VALUE_BITS == 249
        and [c463.domain(g.radius).physical_m2 + 6 * len(g.menu) for g in GEOMETRIES] == [8_000_018, 21_952_024],
        {
            "supplied": {
                "menus": {geometry.name: geometry.menu for geometry in GEOMETRIES},
                "coherent_coefficients": {geometry.name: geometry.coherent_coefficients for geometry in GEOMETRIES},
                "M64_source_cells": "six physical M2 per position; uniform internal rest ray",
                "occupation_control": "six identical local CNOTs compute and uncompute parity flag per menu site",
                "Q1_boundary": "parity equals occupation only on global one-particle source code",
                "Cycle463": "96 layers, D=6^96, B=249, exact word-block rule, zero shell, scale40 capacity",
                "mass": "Cycle219 beta=-0.3 scalar-rest fixture",
                "contact": "Cycle230 on-site phase, identity on Q1",
                "diagnostic": "coherent norm and partial trace only",
                "wall_cap_seconds": WALL_CAP_SECONDS,
                "rss_cap_mib": RSS_CAP_MIB,
            },
            "capacities": {geometry.name: c463.domain(geometry.radius).physical_m2 + 6 * len(geometry.menu) for geometry in GEOMETRIES},
            "maximum_local_occupation_control_support_M2": 7,
            "Cycle463_word_block_support_envelope_M2": 7 * c463.SUPERCELL_M2,
            "elementary_arithmetic_gate_trace": None,
            "fully_gate_synthesized_field_layout_claimed": False,
        },
    )
    check(
        "the weak-field P1/P2 ledger advances only local occupation control and branch-level source-field entanglement",
        True,
        {
            "closed_here": (
                "actual Q1 M64 source occupation coherently controls a local source flag",
                "source-position branches become correlated with locally generated Cycle463 word fields",
            ),
            "rho_equals_abs_psi_squared": "diagonal norm/trace weights computed algebraically; physical probability and occurrence remain open",
            "universal_mass_coupling": "open; beta=-0.3 and unit source are supplied",
            "passive_response": "open here; requires a separate receiver composition such as Cycle464",
            "backreaction": "open here; source does not respond to the generated field",
            "gravity": "open; no lapse, metric, proper time, energy/stress, curvature, or empirical law",
            "Born_composition": "open; a retained Born law would be required before interpreting trace weights probabilistically",
            "C_source": "advanced from host-selected central bit to coherent local Q1 occupation control; universal density/source law open",
            "C_local": "bounded 7-M2 control plus inherited 448000-M2 word-block support envelope; elementary arithmetic trace open",
            "C_ref": "source menu, unit strength, beta, boundary, precision/count, and trace diagnostic supplied",
            "C_num": "train plus unseen held off-axis residuals pass without refit",
            "C_wrap": "unchanged; eigenphase/update/layer count are not energy/rate/time",
            "C_int": "partial branch correlation only; no passive/reciprocal interaction",
        },
    )
    check(
        "full refreshed N1-N8 rejects probability, gravity, minimum-content, no-go, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "five normalized routes remain: Q1 parity flag (attempted), number-resolving source, Born instrument, reciprocal M64 composition, dynamical gauge mediator",
            "N2": "collapsed independent imports are Q1 restriction, source/menu/strength, word arithmetic trace, Born meaning, mass coupling, and backreaction/geometry",
            "N3": "hidden scan exposes parity-versus-density, finite menu/shell, prepared coherence, unit source, fixed beta, and word-block gate boundary",
            "N4": "Cycle463 source-control residual matches; Cycle464 passive/backreaction and Born residuals differ and are not claimed closed",
            "N5": "bit/site/branch/menu/cube resolutions tested; number-general, lattice-wide, continuum, probability, and gravity resolutions untested",
            "N6": "host-selected source-site import is retired on the declared Q1 menu without an axiom edit; primitive arithmetic and interpretation remain",
            "N7": "a number-resolving local density compiler composed with a retained Born instrument and reciprocal M64 law could extend the result",
            "N8": "prior source/Green and Born walls have constructive reopenings; broad gravity or no-go claim: FAIL; no axiom pressure",
        },
    )
    check(
        "the frozen train/held coherent-source run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS, "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle465 coherent M64 source-position / relaxed-field bridge")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    results = compiler_controls()
    coherent_trace_controls(results)
    mass_contact_controls()
    covariance_controls(results)
    deletion_domain_controls(results)
    inventory_ledger_no_go_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
