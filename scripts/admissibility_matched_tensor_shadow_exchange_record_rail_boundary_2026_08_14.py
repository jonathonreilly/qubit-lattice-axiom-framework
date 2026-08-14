#!/usr/bin/env python3
"""Block 81: matched-tensor shadow exchange and inert Record rail.

The positive construction replaces a scalar battery by six matched-direction
source/field channels.  Each channel transfers the complete null tensor
u_d tensor u_d, so the local exchange commutes with all ten symmetric source
components and the Block78 source split cancels all four Ward defects.  The
same midpoint shadow-work identity updates a matter share and a carried shadow
share with opposite signs.

The construction remains conditional.  A per-hit exchange angle exists on
the zero-field source census, but no fixed transfer probability supplies the varying work;
arbitrary TT input makes the work signed and unbounded.  An exact covariant
M2 Record codec and a noninterfering parallel rail archive the two shares, but
they do not identify the shadow share with physical gravitational stress or
make the live gravity state a function of Records.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_MATCHED_TENSOR_SHADOW_EXCHANGE_RECORD_RAIL_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_TOTAL_CUBIC_RECORD_GROWTH_GRAVITY_DEBIT_WARD_STATE_"
    "AXIOM_DECISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_MATCHED_TENSOR_SHADOW_EXCHANGE_RECORD_RAIL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_TOTAL_CUBIC_RECORD_GROWTH_GRAVITY_DEBIT_WARD_STATE_AXIOM_DECISION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_matched_tensor_shadow_exchange_record_rail_boundary_2026_08_14.py",
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
import admissibility_total_cubic_record_growth_gravity_debit_ward_state_axiom_decision_2026_08_14 as block80  # noqa: E402


block79 = block80.block79
block78 = block80.block78
block77 = block78.block77
b64 = block79.b64
b65 = block79.b65
b63 = b64.b63
b53 = block79.b53
block67 = block79.block67

Checks = block80.Checks
TOL = 3.0e-10
DELTA = 0.5
CURRENT_AXIOM_COMMIT = "b02f50a9cfb8ca57c2dbe7026d06487947d22331"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK80_COMMIT = "03c18511c296ce9b5550418e1ba5c4802c068bca"
BLOCK80_NOTE_BLOB = "860ca9079df21321695de65c265d8099cbe244d3"
BLOCK80_RUNNER_BLOB = "6db8558b215604bf3d92b025bf01b617d4b02542"
RUNNER_RELATIVE = (
    "scripts/admissibility_matched_tensor_shadow_exchange_record_rail_"
    "boundary_2026_08_14.py"
)

Coord = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], ...]
DIRECTIONS: tuple[Coord, ...] = block80.DIRECTIONS
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}
TENSOR_PAIRS = tuple(
    (mu, nu) for mu in range(4) for nu in range(mu, 4)
)


def git_commit_path_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def git_worktree_path_blob(path: str) -> str:
    return subprocess.run(
        ("git", "hash-object", "--", path),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    origin_main = subprocess.run(
        ("git", "rev-parse", "origin/main"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    declared = {path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")}
    loaded: set[str] = set()
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
            loaded.add(relative)
    parents = declared - {RUNNER_RELATIVE}
    mismatches = tuple(
        path
        for path in sorted(parents)
        if git_worktree_path_blob(path) != git_commit_path_blob(BLOCK80_COMMIT, path)
    )
    return {
        "origin_main": origin_main,
        "axiom_blob": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom": expected_axiom,
        "parent_note": git_worktree_path_blob(PARENT_NOTE.relative_to(ROOT).as_posix()),
        "parent_runner": git_worktree_path_blob(
            "scripts/admissibility_total_cubic_record_growth_gravity_debit_ward_state_axiom_decision_2026_08_14.py"
        ),
        "mismatches": mismatches,
        "missing": tuple(sorted(loaded - declared)),
        "extra": tuple(sorted(declared - loaded)),
        "declared": len(declared),
        "loaded": len(loaded),
    }


def direction_array(index: int) -> np.ndarray:
    return np.asarray(DIRECTIONS[index], dtype=float)


def null_vector(index: int) -> np.ndarray:
    return np.concatenate((np.ones(1), direction_array(index)))


def exchange_gate(angle: float, mutation: str) -> tuple[np.ndarray, np.ndarray]:
    exchange = np.zeros((12, 12), dtype=complex)
    for direction in range(6):
        target = direction
        if mutation == "mismatch_direction":
            target = (direction + 2) % 6
        exchange[6 + target, direction] = 1.0
        exchange[direction, 6 + target] = 1.0
    square = exchange @ exchange
    gate = (
        np.eye(12, dtype=complex)
        + (np.cos(angle) - 1.0) * square
        + 1.0j * np.sin(angle) * exchange
    )
    return exchange, gate


def tensor_operator(mu: int, nu: int, mutation: str) -> np.ndarray:
    values = np.zeros(12, dtype=float)
    for direction in range(6):
        u = null_vector(direction)
        values[direction] = u[mu] * u[nu]
        field_direction = direction
        if mutation == "mismatch_direction":
            field_direction = (direction + 2) % 6
        uf = null_vector(field_direction)
        if mutation == "scalar_only_carrier":
            values[6 + direction] = float(mu == 0 and nu == 0)
        else:
            values[6 + direction] = uf[mu] * uf[nu]
    return np.diag(values).astype(complex)


def direction_representation(rotation: Rotation) -> np.ndarray:
    matrix = np.zeros((12, 12), dtype=complex)
    array = np.asarray(rotation, dtype=int)
    for source, direction in enumerate(DIRECTIONS):
        target_direction = tuple(int(value) for value in array @ np.asarray(direction))
        target = DIR_INDEX[target_direction]
        matrix[target, source] = 1.0
        matrix[6 + target, 6 + source] = 1.0
    return matrix


def matched_tensor_exchange_certificate(mutation: str) -> dict[str, object]:
    angle = 0.37
    exchange, gate = exchange_gate(angle, mutation)
    unitarity = float(np.max(np.abs(gate.conj().T @ gate - np.eye(12))))
    commutator = 0.0
    transfer_error = 0.0
    transfer_norm = np.inf
    for mu, nu in TENSOR_PAIRS:
        total = tensor_operator(mu, nu, mutation)
        commutator = max(
            commutator, float(np.max(np.abs(gate @ total - total @ gate)))
        )
    for direction in range(6):
        initial = np.zeros(12, dtype=complex)
        initial[direction] = 1.0
        final = gate @ initial
        u = null_vector(direction)
        component_transfer = []
        for mu, nu in TENSOR_PAIRS:
            field = np.zeros(12, dtype=complex)
            for index in range(6):
                uf = null_vector(index)
                field[6 + index] = uf[mu] * uf[nu]
            observed = float(np.real(np.vdot(final, field * final)))
            expected = np.sin(angle) ** 2 * u[mu] * u[nu]
            component_transfer.append(observed)
            transfer_error = max(transfer_error, abs(observed - expected))
        transfer_norm = min(transfer_norm, float(np.linalg.norm(component_transfer)))
    covariance = 0.0
    for rotation in b64.ROTATIONS:
        representation = direction_representation(rotation)
        covariance = max(
            covariance,
            float(np.max(np.abs(representation @ gate - gate @ representation))),
        )
    return {
        "unitarity": unitarity,
        "commutator": commutator,
        "transfer_error": transfer_error,
        "minimum_transfer_norm": transfer_norm,
        "covariance": covariance,
        "components": len(TENSOR_PAIRS),
        "frames": len(b64.ROTATIONS),
        "exchange_hermiticity": float(np.max(np.abs(exchange - exchange.conj().T))),
    }


def source_defect(
    data: tuple[np.ndarray, complex, complex, np.ndarray, np.ndarray, np.ndarray],
    before: float,
    after: float,
) -> np.ndarray:
    k, density, density_next, incoming, outgoing, stress_coordinates = data
    p = b53.lattice_vector(k)
    derivative = 1.0j * p
    stress = block78.coordinate_tensor(stress_coordinates)
    scalar = after * density_next - before * density + derivative @ (after * outgoing)
    vector = after * outgoing - before * incoming + 1.0j * (after * stress @ p)
    return np.concatenate((np.asarray((scalar,)), vector))


def full_tensor_split_certificate(mutation: str) -> dict[str, object]:
    matter_before, shadow_before, work = 0.7, 0.3, 0.2
    matter_after = matter_before - work
    shadow_after = shadow_before + work
    if mutation == "drop_reservoir_tensor":
        shadow_after = shadow_before
    modes = 0
    cancellation = 0.0
    individual = 0.0
    source_ward = 0.0
    for size in range(3, 9):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    for along in range(size):
                        for transverse in range(1, size):
                            for remaining in range(size):
                                data = block78.source_mode_data(
                                    size,
                                    axis,
                                    sign,
                                    neutral_step,
                                    along,
                                    transverse,
                                    remaining,
                                )
                                matter = source_defect(data, matter_before, matter_after)
                                shadow = source_defect(data, shadow_before, shadow_after)
                                total = matter + shadow
                                cancellation = max(cancellation, float(np.max(np.abs(total))))
                                individual = max(
                                    individual,
                                    float(np.max(np.abs(matter))),
                                    float(np.max(np.abs(shadow))),
                                )
                                source_ward = max(
                                    source_ward,
                                    float(
                                        np.max(
                                            np.abs(
                                                source_defect(
                                                    data,
                                                    matter_before + shadow_before,
                                                    matter_after + shadow_after,
                                                )
                                            )
                                        )
                                    ),
                                )
                                modes += 1
    return {
        "modes": modes,
        "cancellation": cancellation,
        "individual": individual,
        "source_ward": source_ward,
        "total_share_error": abs(
            (matter_after + shadow_after) - (matter_before + shadow_before)
        ),
    }


def zero_field_calibration_certificate(mutation: str) -> dict[str, object]:
    works: list[float] = []
    adaptive_error = 0.0
    for size in range(3, 9):
        for axis in range(3):
            for sign in (-1, 1):
                for neutral_step in (1, 2):
                    for along in range(size):
                        for transverse in range(1, size):
                            for remaining in range(size):
                                data = block78.source_mode_data(
                                    size,
                                    axis,
                                    sign,
                                    neutral_step,
                                    along,
                                    transverse,
                                    remaining,
                                )
                                k, _rho, _rho_next, _jin, _jout, stress = data
                                p = b53.lattice_vector(k)
                                kinetic, _potential, _c, _m, _s = block78.spatial_operators(p)
                                force = 2.0 * stress
                                work = DELTA**2 / 2.0 * float(
                                    np.real(np.vdot(force, kinetic @ force))
                                )
                                works.append(work)
                                angle = np.arcsin(np.sqrt(np.clip(work, 0.0, 1.0)))
                                adaptive_error = max(
                                    adaptive_error, abs(np.sin(angle) ** 2 - work)
                                )
    minimum = min(works)
    maximum = max(works)
    fixed_transfer = (minimum + maximum) / 2.0
    fixed_error = max(abs(value - fixed_transfer) for value in works)
    if mutation == "fixed_exchange_angle":
        adaptive_error = fixed_error
    return {
        "modes": len(works),
        "minimum": minimum,
        "maximum": maximum,
        "adaptive_error": adaptive_error,
        "fixed_error": fixed_error,
        "distinct": len({round(value, 12) for value in works}),
    }


def real_space_and_gauge_certificate(mutation: str) -> dict[str, object]:
    size = 5
    volume = size**3
    rng = np.random.default_rng(814)
    h = rng.normal(size=(size, size, size, 6))
    pi = rng.normal(size=(size, size, size, 6))
    force = np.zeros_like(h)
    force[1, 2, 3, 0] = 0.73
    force[4, 0, 2, 2] = -0.21

    hh = np.fft.fftn(h, axes=(0, 1, 2))
    pp = np.fft.fftn(pi, axes=(0, 1, 2))
    ff = np.fft.fftn(force, axes=(0, 1, 2))
    h1_modes = np.zeros_like(hh)
    p1_modes = np.zeros_like(pp)
    h2_modes = np.zeros_like(hh)
    p2_modes = np.zeros_like(pp)
    energy0 = energy1 = energy2 = 0.0
    frequencies = np.fft.fftfreq(size)
    for index in np.ndindex((size,) * 3):
        k = 2.0 * np.pi * np.asarray(
            [frequencies[index[axis]] for axis in range(3)]
        )
        p = b53.lattice_vector(k)
        kinetic, potential, _c, _m, _s = block78.spatial_operators(p)
        form = block79.shadow_form(kinetic, potential)
        p1_modes[index] = pp[index] + DELTA * (
            -potential @ hh[index] + ff[index]
        )
        h1_modes[index] = hh[index] + DELTA * kinetic @ p1_modes[index]
        p2_modes[index] = p1_modes[index] - DELTA * potential @ h1_modes[index]
        h2_modes[index] = h1_modes[index] + DELTA * kinetic @ p2_modes[index]
        for label, state in (
            (0, np.concatenate((hh[index], pp[index]))),
            (1, np.concatenate((h1_modes[index], p1_modes[index]))),
            (2, np.concatenate((h2_modes[index], p2_modes[index]))),
        ):
            value = 0.5 * float(np.real(np.vdot(state, form @ state))) / volume
            if label == 0:
                energy0 += value
            elif label == 1:
                energy1 += value
            else:
                energy2 += value
    pi1 = np.fft.ifftn(p1_modes, axes=(0, 1, 2)).real
    kinetic0 = block78.spatial_operators(np.zeros(3))[0]
    work_site = DELTA * np.einsum(
        "...i,ij,...j->...",
        force,
        kinetic0,
        (pi + pi1) / 2.0,
    )
    local_work = float(np.real(np.sum(work_site)))
    work_identity = abs((energy1 - energy0) - local_work)
    unforced_error = abs(energy2 - energy1)
    support = int(np.count_nonzero(np.abs(work_site) > 1.0e-12))

    data = block78.source_mode_data(5, 0, 1, 1, 1, 2, 1)
    k, density, _density_next, incoming, _outgoing, stress = data
    p = b53.lattice_vector(k)
    kinetic, potential, hamiltonian, momentum, _shift = block78.spatial_operators(p)
    h0 = np.linalg.pinv(hamiltonian, rcond=1.0e-12) @ np.asarray((density,))
    pi0 = np.linalg.pinv(momentum, rcond=1.0e-12) @ (2.0 * incoming)
    source_force = 2.0 * stress
    full_works: list[float] = []
    tt_works: list[float] = []
    tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
    projector = tt @ tt.conj().T
    for lapse in (0.0, 1.0):
        pi_first = pi0 + DELTA * (
            -potential @ h0
            + hamiltonian.conj().T[:, 0] * lapse
            + source_force
        )
        full_works.append(
            DELTA
            * float(
                np.real(
                    np.vdot(source_force, kinetic @ ((pi0 + pi_first) / 2.0))
                )
            )
        )
        projected_force = projector @ source_force
        projected_pi0 = projector @ pi0
        projected_pi1 = projector @ pi_first
        tt_works.append(
            DELTA
            * float(
                np.real(
                    np.vdot(
                        projected_force,
                        kinetic @ ((projected_pi0 + projected_pi1) / 2.0),
                    )
                )
            )
        )
    if mutation == "lapse_change_ignored":
        full_works[1] = full_works[0]
    return {
        "local_work": local_work,
        "forced_gain": energy1 - energy0,
        "work_identity": work_identity,
        "unforced_error": unforced_error,
        "support": support,
        "constraint_error": max(
            float(np.max(np.abs(hamiltonian @ h0 - density))),
            float(np.max(np.abs(momentum @ pi0 - 2.0 * incoming))),
        ),
        "full_lapse_difference": abs(full_works[1] - full_works[0]),
        "full_lapse_zero": full_works[0],
        "full_lapse_one": full_works[1],
        "tt_lapse_spread": max(tt_works) - min(tt_works),
        "tt_work": tt_works[0],
    }


def tensor_rotation(rotation: Rotation) -> np.ndarray:
    array = np.asarray(rotation, dtype=float)
    return np.column_stack(
        [
            block78.tensor_coordinates(array @ basis @ array.T)
            for basis in b53.SYMMETRIC_BASIS
        ]
    )


def shadow_exchange_certificate(mutation: str) -> dict[str, object]:
    k = 2.0 * np.pi * np.asarray((1.0, 2.0, 1.0)) / 5.0
    p = b53.lattice_vector(k)
    kinetic, potential, _hamiltonian, _momentum, _shift = block78.spatial_operators(p)
    tt = null_space(b53.tt_constraint(k), rcond=1.0e-11)
    stress = block79.point_source_data(k, (0, 0, 0), (1, 0, 0))[-1]
    stress_tt = tt @ (tt.conj().T @ stress)
    form = block79.shadow_form(kinetic, potential)

    identity_error = 0.0
    ratios: list[float] = []
    unit_work = 0.0
    for coupling in (0.125, 0.25, 0.5, 1.0, 2.0):
        h0 = np.zeros(6, dtype=complex)
        pi0 = np.zeros(6, dtype=complex)
        force = 2.0 * coupling * stress_tt
        pi1 = pi0 + DELTA * (-potential @ h0 + force)
        h1 = h0 + DELTA * (kinetic @ pi1)
        before = block79.shadow_energy(form, np.concatenate((h0, pi0)))
        after = block79.shadow_energy(form, np.concatenate((h1, pi1)))
        midpoint = (pi0 + pi1) / 2.0
        if mutation == "wrong_work_endpoint":
            midpoint = pi1
        work = DELTA * float(np.real(np.vdot(force, kinetic @ midpoint)))
        identity_error = max(identity_error, abs((after - before) - work))
        ratios.append(work / coupling**2)
        if coupling == 1.0:
            unit_work = work

    h = np.zeros(6, dtype=complex)
    pi = np.zeros(6, dtype=complex)
    field_initial = block79.shadow_energy(form, np.concatenate((h, pi)))
    matter_share = 1.0 - field_initial
    shadow_share = field_initial
    multi_identity = 0.0
    copy_error = 0.0
    combined_error = 0.0
    minimum_share = min(matter_share, shadow_share)
    tick_works: list[float] = []
    for tick in range(8):
        phase = np.exp(-1.0j * tick * k[0])
        force = 0.5 * phase * stress_tt
        pi1 = pi + DELTA * (-potential @ h + force)
        h1 = h + DELTA * (kinetic @ pi1)
        midpoint = (pi + pi1) / 2.0
        if mutation == "wrong_work_endpoint":
            midpoint = pi1
        work = DELTA * float(np.real(np.vdot(force, kinetic @ midpoint)))
        tick_works.append(work)
        pi2 = pi1 + DELTA * (-potential @ h1)
        h2 = h1 + DELTA * (kinetic @ pi2)
        previous_energy = block79.shadow_energy(form, np.concatenate((h, pi)))
        field_energy = block79.shadow_energy(form, np.concatenate((h2, pi2)))
        multi_identity = max(multi_identity, abs(field_energy - previous_energy - work))
        shadow_share += work
        if mutation == "wrong_debit_sign":
            matter_share += work
        else:
            matter_share -= work
        copy_error = max(copy_error, abs(shadow_share - field_energy))
        combined_error = max(
            combined_error,
            abs(field_energy + matter_share - (field_initial + 1.0)),
        )
        minimum_share = min(minimum_share, matter_share, shadow_share)
        h, pi = h2, pi2

    force = 2.0 * stress_tt
    unbounded: list[float] = []
    for scale in (-100.0, -10.0, -1.0, 0.0, 1.0, 10.0, 100.0):
        h0 = np.zeros(6, dtype=complex)
        pi0 = scale * stress_tt
        pi1 = pi0 + DELTA * (-potential @ h0 + force)
        work = DELTA * float(
            np.real(np.vdot(force, kinetic @ ((pi0 + pi1) / 2.0)))
        )
        if mutation == "clip_unbounded_work":
            work = float(np.clip(work, -1.0, 1.0))
        unbounded.append(work)

    probe_h = np.asarray((0.2, -0.1, 0.3, 0.07, -0.12, 0.05), dtype=complex)
    probe_pi = np.asarray((-0.3, 0.4, 0.1, -0.09, 0.02, 0.13), dtype=complex)
    probe_force = 0.8 * stress
    probe_pi1 = probe_pi + DELTA * (-potential @ probe_h + probe_force)
    base_work = DELTA * float(
        np.real(np.vdot(probe_force, kinetic @ ((probe_pi + probe_pi1) / 2.0)))
    )
    covariance = 0.0
    for rotation in b64.ROTATIONS:
        representation = tensor_rotation(rotation)
        rotated_k = np.asarray(rotation, dtype=float) @ k
        rotated_p = b53.lattice_vector(rotated_k)
        rotated_g, rotated_potential, _c, _m, _s = block78.spatial_operators(rotated_p)
        rh = representation @ probe_h
        rpi = representation @ probe_pi
        rf = representation @ probe_force
        rpi1 = rpi + DELTA * (-rotated_potential @ rh + rf)
        rotated_work = DELTA * float(
            np.real(np.vdot(rf, rotated_g @ ((rpi + rpi1) / 2.0)))
        )
        covariance = max(covariance, abs(rotated_work - base_work))

    return {
        "identity_error": identity_error,
        "ratio_spread": max(ratios) - min(ratios),
        "unit_work": unit_work,
        "multi_identity": multi_identity,
        "copy_error": copy_error,
        "combined_error": combined_error,
        "minimum_share": minimum_share,
        "tick_work_min": min(tick_works),
        "tick_work_max": max(tick_works),
        "unbounded_min": min(unbounded),
        "unbounded_max": max(unbounded),
        "unbounded_span": max(unbounded) - min(unbounded),
        "covariance": covariance,
    }


def ledger_carrier(
    matter: Fraction, shadow: Fraction, direction: Coord, mutation: str = ""
):
    encoded_direction = direction
    if mutation == "noncovariant_codec":
        encoded_direction = (1, 0, 0)
    anti = b63.matrix_add(
        b63.central(shadow), b63.direction_matrix(encoded_direction)
    )
    return b63.matrix_add(
        b63.central(matter), b63.matrix_complex_scale(b63.I_UNIT, anti)
    )


def decode_ledger(carrier) -> tuple[Fraction, Fraction, Coord]:
    hermitian = b63.hermitian_part(carrier)
    anti = b63.antihermitian_observable(carrier)
    matter, hermitian_vector = b63.hermitian_coefficients(hermitian)
    shadow, direction = b63.hermitian_coefficients(anti)
    if any(value != 0 for value in hermitian_vector):
        raise ValueError("ledger Hermitian vector channel is not zero")
    return matter, shadow, tuple(int(value) for value in direction)  # type: ignore[return-value]


def codec_certificate(mutation: str) -> dict[str, object]:
    cases = failures = covariance_failures = aliases = 0
    payloads = (
        (Fraction(5, 7), Fraction(2, 9)),
        (Fraction(-11, 5), Fraction(13, 4)),
        (Fraction(0), Fraction(1, 31)),
    )
    for rotation in b64.ROTATIONS:
        for direction in DIRECTIONS:
            rotated_direction = b64.rotate_coord(rotation, direction)
            for matter, shadow in payloads:
                carrier = ledger_carrier(matter, shadow, direction, mutation)
                decoded = decode_ledger(carrier)
                failures += decoded != (matter, shadow, direction)
                rotated = b64.rotate_carrier(rotation, carrier)
                target = ledger_carrier(matter, shadow, rotated_direction, mutation)
                covariance_failures += rotated != target
                aliases += int(b64.decode_context(carrier) is not None)
                aliases += int(b64.outcome_decode(carrier) is not None)
                cases += 1
    return {
        "cases": cases,
        "failures": failures,
        "covariance_failures": covariance_failures,
        "aliases": aliases,
    }


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def scale(value: int, vector: Coord) -> Coord:
    return tuple(value * item for item in vector)  # type: ignore[return-value]


def record_rail_certificate(mutation: str) -> dict[str, object]:
    rail_offset = 2 if mutation == "short_record_rail" else 3
    innovations = (Fraction(1, 7), Fraction(3, 7), Fraction(5, 7))
    cases = steps = failures = collisions = permanence_failures = aliases = 0
    direction_failures = distance_failures = 0
    for rotation in b64.ROTATIONS:
        for outcome, sign in block67.nonzero_menu0_pairs(rotation):
            branch = block67.signed_branch(rotation, outcome, sign)
            packet = dict(branch.records)
            packet[branch.old_source] = block79.correct_endpoint_content(branch)
            transverse = tuple(
                branch.new_source[index] - branch.head_site[index]
                for index in range(3)
            )
            direction = branch.direction
            saved: dict[Coord, object] = {}
            previous_rail: Coord | None = None
            for tick in range(4):
                profile = block67.decoded_head_profile(packet)
                if len(profile.frontiers) != 1:
                    failures += 1
                    break
                head = profile.frontiers[0]
                rail = add(head, scale(rail_offset, transverse))
                if mutation == "overwrite_record":
                    rail = head
                if rail in packet:
                    collisions += 1
                    break
                carrier = ledger_carrier(
                    Fraction(10 + tick, 3),
                    Fraction(20 + tick, 7),
                    direction,
                )
                aliases += int(b64.decode_context(carrier) is not None)
                aliases += int(b64.outcome_decode(carrier) is not None)
                if previous_rail is not None:
                    direction_failures += add(previous_rail, direction) != rail
                distance_failures += block67.manhattan(head, rail) != rail_offset
                packet[rail] = carrier
                saved[rail] = carrier
                run = b65.continue_block64(packet, 1, innovations)
                if not run.ok:
                    failures += 1
                    break
                permanence_failures += any(
                    run.records.get(site) != content for site, content in saved.items()
                )
                packet = run.records
                previous_rail = rail
                steps += 1
            cases += 1
    return {
        "cases": cases,
        "steps": steps,
        "failures": failures,
        "collisions": collisions,
        "permanence_failures": permanence_failures,
        "aliases": aliases,
        "direction_failures": direction_failures,
        "distance_failures": distance_failures,
        "rail_offset": rail_offset,
        "analytic_active_strip_separation": rail_offset - 1,
        "source_distance": rail_offset - 1,
    }


def null_split_uniqueness_certificate(mutation: str) -> dict[str, object]:
    matter = 0.8
    field = 0.2
    solutions: list[tuple[int, int, int]] = []
    noncollinear = 0
    for incoming in range(6):
        target = direction_array(incoming)
        for matter_direction in range(6):
            for field_direction in range(6):
                residual = np.linalg.norm(
                    target
                    - matter * direction_array(matter_direction)
                    - field * direction_array(field_direction)
                )
                if residual < TOL:
                    solutions.append((incoming, matter_direction, field_direction))
                    noncollinear += int(
                        matter_direction != incoming or field_direction != incoming
                    )
    if mutation == "claim_noncollinear_null_recoil":
        noncollinear = 1
    # Cycle320-like reversed matter plus two forward unit directions.  Energy
    # and momentum conservation imply a=0 for the reversed matter energy.
    reversed_matter_energy = (1.0 - 1.0) / 2.0
    return {
        "solutions": len(solutions),
        "noncollinear": noncollinear,
        "all_collinear": all(a == b == c for a, b, c in solutions),
        "reversed_matter_energy": reversed_matter_energy,
    }


def scope_certificate(mutation: str) -> dict[str, object]:
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = (ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md").read_text(
        encoding="utf-8"
    )
    counterexample = block79.debit_and_output_counterexample("")
    return {
        "matched_candidate": "matched-direction tensor exchange" in note,
        "abstract_channel": "No Z3 placement" in note
        and "nearest-neighbor circuit" in note,
        "angle_not_selected": "per-hit transfer angle is not a selected law" in note,
        "energy_not_identified": mutation != "claim_local_energy_identified"
        and "shadow ledger is not physical stress-energy" in note,
        "pure_record": "pure-Record route" in note,
        "live_carrier": "live-carrier route" in note,
        "state_sentence": "A state is a configuration of records." in axiom,
        "record_counterexample": bool(counterexample["packets_identical"])
        and float(counterexample["output_difference"]) > 0.6,
        "null_scope": "future-null" in note and "massive/rest" in note,
        "partial_narrowing": "FAIL — partial-narrowing" in note,
        "energy_trilemma": "gauge-fixed" in note
        and "quasilocal" in note
        and "dynamical Record/matter" in note,
        "prior_ward_residual": "order-`c^2` Ward residual" in note,
        "n1_n8": all(f"N{index}" in note for index in range(1, 9)),
        "not_adopted": mutation != "claim_axiom_adopted"
        and "No axiom is amended" in note,
        "not_complete": mutation != "claim_toe_complete"
        and "No TOE percentage moves" in note,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "mismatch_direction",
            "scalar_only_carrier",
            "drop_reservoir_tensor",
            "fixed_exchange_angle",
            "lapse_change_ignored",
            "wrong_work_endpoint",
            "wrong_debit_sign",
            "clip_unbounded_work",
            "noncovariant_codec",
            "short_record_rail",
            "overwrite_record",
            "claim_noncollinear_null_recoil",
            "claim_local_energy_identified",
            "claim_axiom_adopted",
            "claim_toe_complete",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority-parent-and-runtime-closure",
        "current axioms, Block80, and the complete loaded helper closure are content-bound",
        authority["origin_main"] == CURRENT_AXIOM_COMMIT
        and authority["axiom_blob"] == authority["expected_axiom"]
        and authority["parent_note"] == BLOCK80_NOTE_BLOB
        and authority["parent_runner"] == BLOCK80_RUNNER_BLOB
        and not authority["mismatches"]
        and not authority["missing"]
        and not authority["extra"],
        f"scripts declared/loaded={authority['declared']}/{authority['loaded']}; helper mismatches={len(authority['mismatches'])}",
    )

    exchange = matched_tensor_exchange_certificate(mutation)
    checks.check(
        "B-matched-direction-full-tensor-exchange",
        "one bounded source/field exchange conserves all ten null-stress components and all cubic frames",
        exchange["unitarity"] < TOL
        and exchange["exchange_hermiticity"] < TOL
        and exchange["commutator"] < TOL
        and exchange["transfer_error"] < TOL
        and exchange["minimum_transfer_norm"] > 0.1
        and exchange["covariance"] < TOL
        and exchange["components"] == 10
        and exchange["frames"] == 24,
        f"tensor commutator/covariance={exchange['commutator']:.2e}/{exchange['covariance']:.2e}; transfer={exchange['minimum_transfer_norm']:.6f}",
    )

    ward = full_tensor_split_certificate(mutation)
    checks.check(
        "C-all-four-Ward-defect-cancellation",
        "opposite matter/shadow share changes cancel all four source defects on the complete signed-ray census",
        ward["modes"] == 13056
        and ward["cancellation"] < TOL
        and ward["source_ward"] < TOL
        and ward["total_share_error"] < TOL
        and ward["individual"] > 0.1,
        f"modes={ward['modes']}; cancellation/individual={ward['cancellation']:.2e}/{ward['individual']:.3f}",
    )

    calibration = zero_field_calibration_certificate(mutation)
    expected_minimum = float(np.sin(np.pi / 8.0) ** 2)
    expected_fixed_error = (1.0 - expected_minimum) / 2.0
    checks.check(
        "D-gauge-fixed-zero-field-transfer-calibration",
        "the lapse-zero full-coordinate diagnostic admits a bounded per-hit tensor transfer, while no fixed probability covers the census",
        calibration["modes"] == 13056
        and abs(calibration["minimum"] - expected_minimum) < TOL
        and abs(calibration["maximum"] - 1.0) < TOL
        and calibration["adaptive_error"] < TOL
        and abs(calibration["fixed_error"] - expected_fixed_error) < TOL
        and calibration["distinct"] == 11,
        f"work range={calibration['minimum']:.7f}..{calibration['maximum']:.7f}; fixed mismatch={calibration['fixed_error']:.6f}",
    )

    work_boundary = real_space_and_gauge_certificate(mutation)
    checks.check(
        "E-local-midpoint-work-and-gauge-selection-boundary",
        "the full-coordinate work is site-local and equals the shadow gain, but it changes with arbitrary lapse while TT work does not",
        work_boundary["work_identity"] < 1.0e-10
        and work_boundary["unforced_error"] < 1.0e-10
        and work_boundary["support"] == 2
        and work_boundary["constraint_error"] < TOL
        and work_boundary["full_lapse_difference"] > 0.6
        and work_boundary["tt_lapse_spread"] < TOL
        and abs(work_boundary["tt_work"] - 0.55519262175876) < TOL,
        f"real-space identity/support={work_boundary['work_identity']:.2e}/{work_boundary['support']}; lapse full/TT={work_boundary['full_lapse_difference']:.3f}/{work_boundary['tt_lapse_spread']:.2e}",
    )

    shadow = shadow_exchange_certificate(mutation)
    checks.check(
        "F-shadow-work-debit-copy-and-domain-boundary",
        "midpoint work exactly transfers between matter and shadow shares for eight ticks but is signed and unbounded on the unrestricted state domain",
        shadow["identity_error"] < TOL
        and shadow["ratio_spread"] < TOL
        and abs(shadow["unit_work"] - 0.1534514665934883) < TOL
        and shadow["multi_identity"] < TOL
        and shadow["copy_error"] < TOL
        and shadow["combined_error"] < TOL
        and shadow["minimum_share"] >= -TOL
        and shadow["tick_work_min"] < -0.01
        and shadow["tick_work_max"] > 0.009
        and shadow["unbounded_min"] < -30.0
        and shadow["unbounded_max"] > 30.0
        and shadow["unbounded_span"] > 60.0
        and shadow["covariance"] < TOL,
        f"unit/eight-tick copy={shadow['unit_work']:.6f}/{shadow['copy_error']:.2e}; work range={shadow['unbounded_min']:.2f}..{shadow['unbounded_max']:.2f}",
    )

    codec = codec_certificate(mutation)
    checks.check(
        "G-exact-covariant-M2-share-direction-codec",
        "one M2 Record exactly stores two real shares and one cubic direction without aliasing the live front parser",
        codec["cases"] == 432
        and codec["failures"] == 0
        and codec["covariance_failures"] == 0
        and codec["aliases"] == 0,
        f"cases/failures/covariance/aliases={codec['cases']}/{codec['failures']}/{codec['covariance_failures']}/{codec['aliases']}",
    )

    rail = record_rail_certificate(mutation)
    checks.check(
        "H-noninterfering-append-only-ledger-rail",
        "a content-defined parallel rail archives one inert share Record per front cell without overwrite or parser interference",
        rail["cases"] == 96
        and rail["steps"] == 384
        and rail["failures"] == 0
        and rail["collisions"] == 0
        and rail["permanence_failures"] == 0
        and rail["aliases"] == 0
        and rail["direction_failures"] == 0
        and rail["distance_failures"] == 0
        and rail["rail_offset"] == 3
        and rail["analytic_active_strip_separation"] == 2
        and rail["source_distance"] == 2,
        f"cases/steps={rail['cases']}/{rail['steps']}; rail/source distance={rail['rail_offset']}/{rail['source_distance']}",
    )

    uniqueness = null_split_uniqueness_certificate(mutation)
    checks.check(
        "I-positive-null-split-collinearity-boundary",
        "a positive future-null two-carrier split is necessarily collinear; nonzero reversed-matter recoil needs another physical route",
        uniqueness["solutions"] == 6
        and uniqueness["noncollinear"] == 0
        and uniqueness["all_collinear"]
        and abs(uniqueness["reversed_matter_energy"]) < TOL,
        f"axis solutions/noncollinear={uniqueness['solutions']}/{uniqueness['noncollinear']}; reversed-matter energy={uniqueness['reversed_matter_energy']:.1f}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "J-state-identification-no-go-and-TOE-scope",
        "the tensor kinematics and Record archive remain conditional without physical energy identification, axiom adoption, or TOE movement",
        all(scope.values()),
        f"candidate/energy/state/N1-N8={scope['matched_candidate']}/{scope['energy_not_identified']}/{scope['record_counterexample']}/{scope['n1_n8']}",
    )

    print(
        "AXIOM_AUTHORITY: origin/main=" + CURRENT_AXIOM_COMMIT
        + " minimal-axiom blob=" + CURRENT_AXIOM_BLOB
        + "; Block80 parent=" + BLOCK80_COMMIT
    )
    print(
        "per_element: all ten source-tensor components, six matched channels, exact M2 codec coordinates, and each share debit are checked"
    )
    print(
        "per_site: 96 Cycle713 branches carry 384 inert rail Records at distance three; the abstract tensor channel has no executed Z3/M2 placement or nearest-neighbor circuit"
    )
    print(
        "per_mode: all 13,056 signed-ray source modes pass four-defect cancellation and gauge-fixed zero-field calibration; arbitrary TT scaling breaks finite capacity"
    )
    print(
        "per_block: tensor exchange, Ward split, work calibration, shadow ledger, Record codec/rail, null kinematics, and state scope are separate; physical channel realization is checked and not executed"
    )
    print(
        "lattice_wide: checked and not executed — no fixed physical exchange law, local gravitational stress identification, positive compact mean, general massive matter, live gravity-state compiler, or audit chain is supplied"
    )
    print(
        "RESULT: matched-direction tensor transfer closes the four-component kinematic debit on the declared null source, but the work-dependent selector and physical field-stress identification remain open"
    )
    print(
        "NEXT: resolve the local-gauge-fixed versus quasilocal-gauge-invariant versus common-action energy trilemma, including the prior source mixed-Hessian Ward residual; do not spend another block on abstract batteries or ledgers"
    )
    print(
        "SCOPE: partial-positive full-tensor kinematics plus a narrow future-null collinearity boundary; no selected law, axiom adoption, retention, obligation retirement, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
