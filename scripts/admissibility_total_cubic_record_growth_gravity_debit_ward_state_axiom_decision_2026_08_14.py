#!/usr/bin/env python3
"""Block 80: total Record law, gravity debit/Ward, and state-axiom fork.

This runner first repairs the displayed occupancy-to-Bloch construction into
a total probability measure on all sixty-four nearest-neighbour occupancy
conditions.  It then iterates the corresponding readiness rule from one
supplied seed and proves exact L1-ball Record growth.  Those are positive
controls, not a selected physical law.

The gravity test conditionally identifies the exact positive Block79 shadow
work of one declared Fourier mode with a candidate scalar T00 loss carried by
its single conserved point source.  This is not a normalized total real-space
point-source energy theorem.  On a closed periodic carrier the zero mode of a
divergence is zero, so changing the source amplitude fails the Ward identity
by exactly the debit.  A nearby compensating carrier restores scalar
continuity with two local edges, keeping the result narrow and identifying the
missing physical choice.  Finally, the runner reuses Block79's
identical-Record/different-TT-state witness to expose the independent
live-state ontology fork.

No law or axiom is adopted, no nonlinear gravity theorem is claimed, and no
TOE obligation or percentage is moved.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import null_space
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TOTAL_CUBIC_RECORD_GROWTH_GRAVITY_DEBIT_WARD_STATE_"
    "AXIOM_DECISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_TOTAL_CUBIC_RECORD_GROWTH_GRAVITY_DEBIT_WARD_STATE_AXIOM_DECISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_total_cubic_record_growth_gravity_debit_ward_state_axiom_decision_2026_08_14.py",
    "scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/admissibility_canonical_two_tt_positive_transfer_record_source_continuity_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_endpoint_record_attachment_intertwiner_boundary_2026_08_12.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_physical_state_to_record_attachment_selection_cut_2026_08_12.py",
    "scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py",
    "scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14 as block79  # noqa: E402


b64 = block79.b64
b53 = block79.b53
block78 = block79.block78

TOL = 2.0e-10
CURRENT_AXIOM_COMMIT = "b02f50a9cfb8ca57c2dbe7026d06487947d22331"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK79_COMMIT = "d7d4d6ecb55ce5c0f6948eba14984b2b93c4730a"
BLOCK79_NOTE_BLOB = "c3b119a3749dcdc5797d88697bbd29664cd6dff8"
BLOCK79_RUNNER_BLOB = "5e6d246b233f1e4761d0443d7fcc636dfd0fc1cb"

Coord = tuple[int, int, int]
Occ = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], ...]
SymVec = tuple[sp.Expr, sp.Expr, sp.Expr]
Atom = tuple[sp.Expr, SymVec]

ORIGIN: Coord = (0, 0, 0)
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_OF = {direction: index for index, direction in enumerate(DIRECTIONS)}
ALL_OCCUPANCIES: tuple[Occ, ...] = tuple(product((0, 1), repeat=6))  # type: ignore[assignment]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 152 else detail[:149] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return int(self.failed != 0)


def git_commit_path_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_worktree_path_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", "--", path),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom_blob = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    origin_main = subprocess.run(
        ("git", "rev-parse", "origin/main"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    declared_scripts = {
        path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")
    }
    loaded_scripts: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        path = Path(file_name).resolve()
        try:
            relative = path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded_scripts.add(relative)

    parent_scripts = declared_scripts - {
        "scripts/admissibility_total_cubic_record_growth_gravity_debit_ward_state_axiom_decision_2026_08_14.py"
    }
    helper_mismatches = tuple(
        path
        for path in sorted(parent_scripts)
        if git_worktree_path_blob(path) != git_commit_path_blob(BLOCK79_COMMIT, path)
    )
    return {
        "origin_main": origin_main,
        "axiom_blob": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom_blob": expected_axiom_blob,
        "parent_note_blob": git_worktree_path_blob(PARENT_NOTE.relative_to(ROOT).as_posix()),
        "parent_runner_blob": git_worktree_path_blob(
            "scripts/admissibility_cycle713_record_head_adm_work_archive_state_boundary_2026_08_14.py"
        ),
        "helper_mismatches": helper_mismatches,
        "missing_runtime_inputs": tuple(sorted(loaded_scripts - declared_scripts)),
        "extra_declared_scripts": tuple(sorted(declared_scripts - loaded_scripts)),
        "declared_scripts": len(declared_scripts),
        "loaded_scripts": len(loaded_scripts),
    }


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def l1(site: Coord) -> int:
    return sum(abs(value) for value in site)


def rotate_coord(rotation: Rotation, vector: Coord) -> Coord:
    return tuple(
        sum(rotation[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotate_occupancy(rotation: Rotation, occupancy: Occ) -> Occ:
    result = [0] * 6
    for slot, value in enumerate(occupancy):
        if value:
            result[SLOT_OF[rotate_coord(rotation, DIRECTIONS[slot])]] = value
    return tuple(result)  # type: ignore[return-value]


def bloch(occupancy: Occ) -> SymVec:
    third = sp.Rational(1, 3)
    return (
        third * (occupancy[0] - occupancy[1]),
        third * (occupancy[2] - occupancy[3]),
        third * (occupancy[4] - occupancy[5]),
    )


def rotate_symvec(rotation: Rotation, vector: SymVec) -> SymVec:
    return tuple(
        sp.simplify(
            sum(rotation[row][column] * vector[column] for column in range(3))
        )
        for row in range(3)
    )  # type: ignore[return-value]


def probability_measure(occupancy: Occ, mutation: str = "") -> tuple[Atom, ...]:
    vector = bloch(occupancy)
    nonzero_components = sum(value != 0 for value in vector)
    if mutation == "partial_menu" and nonzero_components > 1:
        return ()
    norm_squared = sp.simplify(sum(value * value for value in vector))
    if norm_squared == 0:
        return ((sp.Integer(1), (sp.Integer(0),) * 3),)
    radius = sp.sqrt(norm_squared)
    unit = tuple(sp.simplify(value / radius) for value in vector)
    return (
        (sp.simplify((1 + radius) / 2), unit),
        (sp.simplify((1 - radius) / 2), tuple(-value for value in unit)),
    )


def expression_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def vector_equal(left: SymVec, right: SymVec) -> bool:
    return all(expression_equal(a, b) for a, b in zip(left, right))


def measure_equal(left: tuple[Atom, ...], right: tuple[Atom, ...]) -> bool:
    if len(left) != len(right):
        return False
    return all(
        expression_equal(weight0, weight1) and vector_equal(vector0, vector1)
        for (weight0, vector0), (weight1, vector1) in zip(left, right)
    )


def total_measure_certificate(mutation: str) -> dict[str, object]:
    missing = normalization_failures = positivity_failures = barycenter_failures = 0
    pure_support_failures = 0
    ready = axis_ready = 0
    maximum_norm_squared = sp.Integer(0)
    for occupancy in ALL_OCCUPANCIES:
        vector = bloch(occupancy)
        norm_squared = sp.simplify(sum(value * value for value in vector))
        maximum_norm_squared = max(maximum_norm_squared, norm_squared)
        current_ready = norm_squared != 0
        ready += int(current_ready)
        axis_ready += int(sum(value != 0 for value in vector) == 1)
        atoms = probability_measure(occupancy, mutation)
        missing += len(atoms) == 0
        if not atoms:
            continue
        normalization_failures += not expression_equal(
            sum(weight for weight, _ in atoms), sp.Integer(1)
        )
        positivity_failures += any(float(sp.N(weight)) < -TOL for weight, _ in atoms)
        barycenter = tuple(
            sp.simplify(sum(weight * support[index] for weight, support in atoms))
            for index in range(3)
        )
        barycenter_failures += not vector_equal(barycenter, vector)
        if norm_squared != 0:
            pure_support_failures += any(
                not expression_equal(
                    sum(component * component for component in support),
                    sp.Integer(1),
                )
                for _, support in atoms
            )
    return {
        "conditions": len(ALL_OCCUPANCIES),
        "ready": ready,
        "axis_ready": axis_ready,
        "missing": missing,
        "normalization_failures": normalization_failures,
        "positivity_failures": positivity_failures,
        "barycenter_failures": barycenter_failures,
        "pure_support_failures": pure_support_failures,
        "maximum_norm_squared": maximum_norm_squared,
    }


def measure_covariance_certificate(mutation: str) -> dict[str, object]:
    cases = failures = 0
    for rotation in b64.ROTATIONS:
        for occupancy in ALL_OCCUPANCIES:
            actual = probability_measure(rotate_occupancy(rotation, occupancy))
            base = probability_measure(occupancy)
            if mutation == "break_measure_covariance" and rotation != b64.IDENTITY_ROTATION:
                expected = base
            else:
                expected = tuple(
                    (weight, rotate_symvec(rotation, support))
                    for weight, support in base
                )
            failures += not measure_equal(actual, expected)
            cases += 1
    return {"cases": cases, "failures": failures}


def occupancy_of(records: set[Coord], target: Coord) -> Occ:
    return tuple(int(add(target, direction) in records) for direction in DIRECTIONS)  # type: ignore[return-value]


def ready(records: set[Coord], target: Coord) -> bool:
    return any(value != 0 for value in bloch(occupancy_of(records, target)))


def next_record_shell(records: set[Coord]) -> set[Coord]:
    candidates = {
        add(site, direction)
        for site in records
        for direction in DIRECTIONS
        if add(site, direction) not in records
    }
    return {site for site in candidates if ready(records, site)}


def ball3(radius: int) -> set[Coord]:
    return {
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    }


def ball3_count(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def record_growth_certificate(mutation: str) -> dict[str, object]:
    records = {ORIGIN}
    exact_failures = distribution_failures = overwrite_failures = 0
    appended = 0
    for depth in range(1, 9):
        shell = next_record_shell(records)
        if mutation == "skip_growth_site" and depth == 3:
            shell.remove(sorted(shell)[0])
        overwrite_failures += len(shell & records)
        distribution_failures += sum(
            len(probability_measure(occupancy_of(records, site))) == 0
            for site in shell
        )
        appended += len(shell)
        records |= shell
        exact_failures += records != ball3(depth)
        exact_failures += len(records) != ball3_count(depth)
        expected_shell = 4 * depth**2 + 2
        exact_failures += len(shell) != expected_shell
    return {
        "depth": 8,
        "records": len(records),
        "appended": appended,
        "exact_failures": exact_failures,
        "distribution_failures": distribution_failures,
        "overwrite_failures": overwrite_failures,
    }


def torus_incidence(size: int) -> tuple[np.ndarray, dict[tuple[Coord, int], int]]:
    sites = tuple(product(range(size), repeat=3))
    site_index = {site: index for index, site in enumerate(sites)}
    edges: list[tuple[Coord, int]] = []
    for site in sites:
        for axis in range(3):
            edges.append((site, axis))
    incidence = np.zeros((len(sites), len(edges)), dtype=float)
    lookup: dict[tuple[Coord, int], int] = {}
    for column, (site, axis) in enumerate(edges):
        neighbor = list(site)
        neighbor[axis] = (neighbor[axis] + 1) % size
        head = tuple(neighbor)
        incidence[site_index[site], column] = -1.0
        incidence[site_index[head], column] = 1.0
        lookup[(site, axis)] = column
    return incidence, lookup


def constant_source_ward_certificate(mutation: str) -> dict[str, object]:
    failures = 0
    maximum_error = column_sum_error = 0.0
    for size in range(3, 8):
        incidence, lookup = torus_incidence(size)
        column_sum_error = max(column_sum_error, float(np.max(np.abs(np.sum(incidence, axis=0)))))
        density_change = np.zeros(size**3)
        density_change[0] = -1.0
        density_change[size**2] = 1.0
        current = np.zeros(incidence.shape[1])
        current[lookup[((0, 0, 0), 0)]] = 1.0
        if mutation == "break_constant_source_current":
            current[lookup[((0, 0, 0), 0)]] = -1.0
        error = float(np.max(np.abs(incidence @ current - density_change)))
        maximum_error = max(maximum_error, error)
        failures += error > TOL
    return {
        "sizes": 5,
        "failures": failures,
        "maximum_error": maximum_error,
        "column_sum_error": column_sum_error,
    }


def baseline_vacuum_work() -> float:
    k = 2.0 * np.pi * np.asarray((1, 2, 1), dtype=float) / 5.0
    data = block79.point_source_data(k, b64.ORIGIN, (1, 0, 0))
    stress = data[-1]
    p = b53.lattice_vector(k)
    kinetic, _potential, _hamiltonian, _momentum, _shift = block78.spatial_operators(p)
    tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
    projected = tt @ (tt.conj().T @ stress)
    force = 2.0 * projected
    return (
        block79.DELTA**2
        * float(np.real(force.conj() @ kinetic @ force))
        / 2.0
    )


def closed_debit_ward_certificate(mutation: str) -> dict[str, object]:
    debit = baseline_vacuum_work()
    if mutation == "drop_debit_zero_mode":
        debit = 0.0
    initial_energy = 1.0
    final_energy = initial_energy - debit
    sizes = tuple(range(3, 8))
    residual_error = 0.0
    minimum_residuals: list[float] = []
    for size in sizes:
        incidence, _lookup = torus_incidence(size)
        density_change = np.zeros(size**3)
        density_change[0] = -initial_energy
        density_change[size**2] = final_energy
        solution = np.linalg.lstsq(incidence, density_change, rcond=1.0e-12)[0]
        residual = incidence @ solution - density_change
        minimum_residuals.append(float(np.linalg.norm(residual)))
        expected = abs(debit) / np.sqrt(size**3)
        residual_error = max(residual_error, abs(minimum_residuals[-1] - expected))

    pole_sizes = (64, 128, 256, 512, 1024, 2048)
    pole_magnitudes = []
    pole_scaled = []
    for size in pole_sizes:
        angle = 2.0 * np.pi / size
        derivative = np.exp(-1.0j * angle) - 1.0
        source = final_energy * np.exp(-1.0j * angle) - initial_energy
        current = source / derivative
        pole_magnitudes.append(abs(current))
        pole_scaled.append(abs(derivative) * abs(current))
    zero_mode = abs(final_energy - initial_energy)
    if mutation == "claim_local_debit_current":
        zero_mode = 0.0
    return {
        "debit": debit,
        "zero_mode": zero_mode,
        "residual_error": residual_error,
        "minimum_residuals": tuple(minimum_residuals),
        "pole_magnitudes": tuple(pole_magnitudes),
        "pole_scaled_limit": pole_scaled[-1],
        "pole_scaled_error": abs(pole_scaled[-1] - abs(debit)),
        "pole_growth": pole_magnitudes[-1] / pole_magnitudes[0],
    }


def compensating_carrier_certificate(mutation: str) -> dict[str, object]:
    debit = baseline_vacuum_work()
    failures = 0
    maximum_error = total_change = 0.0
    for size in range(4, 8):
        incidence, lookup = torus_incidence(size)
        density_change = np.zeros(size**3)
        x = 0
        y = size**2
        z = 2 * size**2
        density_change[x] = -1.0
        density_change[y] = 1.0 - debit
        density_change[z] = debit
        current = np.zeros(incidence.shape[1])
        current[lookup[((0, 0, 0), 0)]] = 1.0
        if mutation != "omit_compensating_carrier":
            current[lookup[((1, 0, 0), 0)]] = debit
        error = float(np.max(np.abs(incidence @ current - density_change)))
        maximum_error = max(maximum_error, error)
        total_change = max(total_change, abs(float(np.sum(density_change))))
        failures += error > TOL
    return {
        "sizes": 4,
        "debit": debit,
        "failures": failures,
        "maximum_error": maximum_error,
        "total_change": total_change,
        "edges": 2,
    }


def field_work_certificate(mutation: str) -> dict[str, object]:
    k = 2.0 * np.pi * np.asarray((1, 2, 1), dtype=float) / 5.0
    data = block79.point_source_data(k, b64.ORIGIN, (1, 0, 0))
    stress = data[-1]
    p = b53.lattice_vector(k)
    kinetic, potential, _hamiltonian, _momentum, _shift = block78.spatial_operators(p)
    tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
    projected = tt @ (tt.conj().T @ stress)
    form = block79.shadow_form(kinetic, potential)
    initial = np.zeros(12, dtype=complex)
    initial_energy = block79.shadow_energy(form, initial)
    identity_error = ratio_spread = formal_residual = 0.0
    omitted_residual = minimum_work = np.inf
    ratios: list[float] = []
    for coupling in (0.125, 0.25, 0.5, 1.0, 2.0):
        effective = np.sqrt(coupling) if mutation == "wrong_work_scaling" else coupling
        force = 2.0 * effective * projected
        pi1 = block79.DELTA * force
        h1 = block79.DELTA * kinetic @ pi1
        state1 = np.concatenate((h1, pi1))
        work = block79.DELTA * float(
            np.real(force.conj() @ kinetic @ (pi1 / 2.0))
        )
        field_gain = block79.shadow_energy(form, state1) - initial_energy
        identity_error = max(identity_error, abs(field_gain - work))
        ratios.append(work / coupling**2)
        minimum_work = min(minimum_work, work)
        debit = 0.0 if mutation == "omit_physical_debit" else -work
        formal_residual = max(formal_residual, abs(field_gain + debit))
        omitted_residual = max(omitted_residual, abs(field_gain))
    ratio_spread = max(ratios) - min(ratios)
    return {
        "couplings": 5,
        "identity_error": identity_error,
        "ratio_spread": ratio_spread,
        "formal_residual": formal_residual,
        "omitted_residual": omitted_residual,
        "minimum_work": minimum_work,
        "unit_work": baseline_vacuum_work(),
    }


def record_state_boundary_certificate(mutation: str) -> dict[str, object]:
    counterexample = block79.debit_and_output_counterexample("")
    work_difference = float(counterexample["work_difference"])
    output_difference = float(counterexample["output_difference"])
    if mutation == "claim_records_encode_field":
        work_difference = 0.0
        output_difference = 0.0
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    return {
        "packets_identical": bool(counterexample["packets_identical"]),
        "work_difference": work_difference,
        "output_difference": output_difference,
        "output_constraint_error": float(counterexample["output_constraint_error"]),
        "state_sentence": "A state is a configuration of records." in axiom,
        "only_records": "Only records are readable." in axiom,
        "no_live_pair": "A state is a pair" not in axiom,
    }


def scope_certificate(mutation: str) -> dict[str, object]:
    note = NOTE_PATH.read_text(encoding="utf-8")
    adopted = mutation == "claim_axiom_adopted"
    complete = mutation == "claim_toe_complete"
    return {
        "pure_record_route": "pure-Record route" in note,
        "live_carrier_route": "live-carrier route" in note,
        "product_role_decision": "product-domain or covariant-role decision" in note,
        "nonlinear_route": "nonlinear gravitational self-stress" in note,
        "partial_narrowing": "partial-narrowing" in note,
        "n1_n8": all(f"N{index}" in note for index in range(1, 9)),
        "not_adopted": not adopted and "No axiom is amended" in note,
        "not_complete": not complete and "No TOE percentage moves" in note,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "partial_menu",
            "break_measure_covariance",
            "skip_growth_site",
            "break_constant_source_current",
            "drop_debit_zero_mode",
            "claim_local_debit_current",
            "omit_compensating_carrier",
            "wrong_work_scaling",
            "omit_physical_debit",
            "claim_records_encode_field",
            "claim_axiom_adopted",
            "claim_toe_complete",
        ),
        default="",
    )
    args = parser.parse_args()
    mutation = args.mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority-parent-and-runtime-closure",
        "current axioms, Block79, and the complete loaded helper closure are content-bound",
        authority["origin_main"] == CURRENT_AXIOM_COMMIT
        and authority["axiom_blob"] == authority["expected_axiom_blob"]
        and authority["parent_note_blob"] == BLOCK79_NOTE_BLOB
        and authority["parent_runner_blob"] == BLOCK79_RUNNER_BLOB
        and not authority["helper_mismatches"]
        and not authority["missing_runtime_inputs"]
        and not authority["extra_declared_scripts"],
        f"scripts declared/loaded={authority['declared_scripts']}/{authority['loaded_scripts']}; helper mismatches={len(authority['helper_mismatches'])}",
    )

    total = total_measure_certificate(mutation)
    checks.check(
        "B-total-covariant-local-probability-measure",
        "the repaired occupancy law supplies a normalized positive M2 measure on all 64 conditions",
        total["conditions"] == 64
        and total["ready"] == 56
        and total["axis_ready"] == 24
        and total["missing"] == 0
        and total["normalization_failures"] == 0
        and total["positivity_failures"] == 0
        and total["barycenter_failures"] == 0
        and total["pure_support_failures"] == 0
        and total["maximum_norm_squared"] == sp.Rational(1, 3),
        f"conditions/ready/axis/missing={total['conditions']}/{total['ready']}/{total['axis_ready']}/{total['missing']}; max |n|^2={total['maximum_norm_squared']}",
    )

    covariance = measure_covariance_certificate(mutation)
    checks.check(
        "C-full-proper-cubic-measure-covariance",
        "every probability atom and weight intertwines on all 24x64 rotated conditions",
        covariance["cases"] == 1536 and covariance["failures"] == 0,
        f"cases/failures={covariance['cases']}/{covariance['failures']}",
    )

    growth = record_growth_certificate(mutation)
    checks.check(
        "D-unbounded-round-indexed-record-recurrence",
        "one supplied seed grows exact L1 balls through the total local readiness rule without overwrite",
        growth["depth"] == 8
        and growth["records"] == ball3_count(8)
        and growth["appended"] == ball3_count(8) - 1
        and growth["exact_failures"] == 0
        and growth["distribution_failures"] == 0
        and growth["overwrite_failures"] == 0,
        f"depth/Records/appended={growth['depth']}/{growth['records']}/{growth['appended']}; failures={growth['exact_failures']}",
    )

    constant = constant_source_ward_certificate(mutation)
    checks.check(
        "E-constant-amplitude-point-source-positive-control",
        "a unit source transfer across one edge is an exact closed-torus divergence",
        constant["sizes"] == 5
        and constant["failures"] == 0
        and constant["maximum_error"] < TOL
        and constant["column_sum_error"] < TOL,
        f"sizes/failures={constant['sizes']}/{constant['failures']}; residual={constant['maximum_error']:.3e}",
    )

    debit_ward = closed_debit_ward_certificate(mutation)
    checks.check(
        "F-single-source-debit-zero-mode-and-locality-boundary",
        "conditional on the one-mode-shadow-work-to-T00 identification, changing the lone source by that debit violates the closed Ward zero mode and needs a pole",
        debit_ward["debit"] > TOL
        and abs(debit_ward["zero_mode"] - debit_ward["debit"]) < TOL
        and debit_ward["residual_error"] < TOL
        and debit_ward["pole_growth"] > 20.0
        and debit_ward["pole_scaled_error"] < 1.0e-4,
        f"debit/zero={debit_ward['debit']:.6f}/{debit_ward['zero_mode']:.6f}; pole growth={debit_ward['pole_growth']:.2f}",
    )

    compensator = compensating_carrier_certificate(mutation)
    checks.check(
        "G-adjacent-compensating-carrier-positive-control",
        "one explicit adjacent reservoir restores scalar continuity with two local edges",
        compensator["sizes"] == 4
        and compensator["failures"] == 0
        and compensator["maximum_error"] < TOL
        and compensator["total_change"] < TOL
        and compensator["edges"] == 2,
        f"sizes/failures={compensator['sizes']}/{compensator['failures']}; debit={compensator['debit']:.6f}",
    )

    work = field_work_certificate(mutation)
    checks.check(
        "H-positive-quadratic-vacuum-field-work-and-formal-debit",
        "the TT field gain is exact, positive, quadratic in coupling, and canceled only by an explicit opposite debit",
        work["couplings"] == 5
        and work["identity_error"] < TOL
        and work["ratio_spread"] < TOL
        and work["formal_residual"] < TOL
        and work["omitted_residual"] > 0.1
        and work["minimum_work"] > TOL,
        f"unit work={work['unit_work']:.6f}; identity/scaling/debit={work['identity_error']:.2e}/{work['ratio_spread']:.2e}/{work['formal_residual']:.2e}",
    )

    state = record_state_boundary_certificate(mutation)
    checks.check(
        "I-current-record-state-does-not-determine-live-gravity",
        "identical permanent Record packets admit distinct constrained TT work and outputs",
        state["packets_identical"]
        and state["work_difference"] > 0.5
        and state["output_difference"] > 0.6
        and state["output_constraint_error"] < TOL
        and state["state_sentence"]
        and state["only_records"]
        and state["no_live_pair"],
        f"work/output separation={state['work_difference']:.6f}/{state['output_difference']:.6f}; constraint={state['output_constraint_error']:.2e}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "J-axiom-decision-and-toe-scope",
        "the exact pure-Record/live-carrier fork is exposed without adopting an axiom or moving TOE scores",
        all(scope.values()),
        f"pure/live/product/nonlinear/N1-N8={scope['pure_record_route']}/{scope['live_carrier_route']}/{scope['product_role_decision']}/{scope['nonlinear_route']}/{scope['n1_n8']}",
    )

    print(
        "AXIOM_AUTHORITY: origin/main=" + CURRENT_AXIOM_COMMIT
        + " minimal-axiom blob=" + CURRENT_AXIOM_BLOB
        + "; Block79 parent=" + BLOCK79_COMMIT
    )
    print(
        "per_element: all 64 occupancy conditions, every algebraic measure atom, and each debit term are checked"
    )
    print(
        "per_site: exact L1 balls through depth 8, 833 permanent Records, and closed-torus source/reservoir sites are checked"
    )
    print(
        "per_mode: 1,536 cubic measure intertwiners, the Ward zero mode, the inverse-derivative pole, and one nonzero TT work mode are checked"
    )
    print(
        "per_block: total law, recurrence, constant source, debit obstruction, compensator, field work, state boundary, and scope are separate"
    )
    print(
        "lattice_wide: checked and not executed — no selected law, physical clock, full tensor compensator, nonlinear self-stress, live-state carrier, or audit chain is supplied"
    )
    print(
        "RESULT: local probability totality and unbounded Record recurrence are constructive; conditional on identifying one declared mode's shadow work with a candidate T00 loss, the lone closed-carrier source cannot pay that debit by changing its own T00"
    )
    print(
        "NEXT: test a typed full-tensor physical compensating carrier first; use nonlinear gravitational self-stress as the fallback, while the pure-Record versus live-carrier state decision remains owner-facing"
    )
    print(
        "SCOPE: partial-positive construction plus partial-narrowing Ward/state boundary; no axiom adoption, retention, obligation retirement, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
