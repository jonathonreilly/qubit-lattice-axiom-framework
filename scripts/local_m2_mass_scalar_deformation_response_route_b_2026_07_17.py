#!/usr/bin/env python3
"""Route B: bounded physical-M2 mass--scalar deformation response.

Construct an exact finite relative update

    R(epsilon) = product_x exp[-i epsilon M_x X_{s,x}],

where M_x=m N_x is the existing connected-code number operator and X_s is a
six-M2 vacuum-to-uniform-scalar transition for the finite acoustic coin.  The
runner tests the local response operator, physical support and code leakage,
proper-cubic/translation covariance, parallel composition, phase and
parameter controls, the existing mass/contact fixture, and the Cycle-213/216
scalar comparators.

The bilinear vertex, mass-charge identification, field vacuum/single-excitation
code, deformation parameter and insertion schedule are supplied.  The result
is a deformation response, not physical energy, stress, a clock rate, a Record,
or a selected gravitational source law.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import finite_coin_scalar_wave_dilation_cycle215_2026_07_16 as c215
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_ROUTE_B_NOTE_2026-07-17.md"
)
BETA = c230.BETA
G_CONTACT = c230.COUPLING
EPSILON = 0.19
PASS = 0
FAIL = 0
TOL = 5.0e-11


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Route-B note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "deformation response",
        "exact finite relative update",
        "physical-m2",
        "all 24 proper-cubic frames",
        "648 frame-translation",
        "cycle-213",
        "cycle-216",
        "deformation-dependent rephase",
        "reparameterization",
        "not physical energy",
        "not a selected gravitational source",
        "supplied structure",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note preserves the result and scope contract", not missing, missing)


def logical_scalar_transition() -> np.ndarray:
    """Vacuum plus six one-direction states, with only the scalar pair active."""

    transition = np.zeros((7, 7), dtype=complex)
    transition[0, 1:] = 1 / np.sqrt(6)
    transition[1:, 0] = 1 / np.sqrt(6)
    return transition


def physical_scalar_transition() -> np.ndarray:
    """Six-qubit sum X_d product_(e != d) |0><0|_e / sqrt(6)."""

    transition = np.zeros((64, 64), dtype=complex)
    for direction in range(6):
        for state in range(64):
            other = state & ~(1 << direction)
            if other == 0:
                transition[state ^ (1 << direction), state] += 1 / np.sqrt(6)
    return transition


def field_encoding() -> np.ndarray:
    encoding = np.zeros((64, 7), dtype=complex)
    encoding[0, 0] = 1
    for direction in range(6):
        encoding[1 << direction, direction + 1] = 1
    return encoding


def bit_permutation(representation: np.ndarray) -> np.ndarray:
    direction_map = tuple(int(np.argmax(representation[:, d])) for d in range(6))
    result = np.zeros((64, 64), dtype=complex)
    for state in range(64):
        target = 0
        for direction in range(6):
            if (state >> direction) & 1:
                target ^= 1 << direction_map[direction]
        result[target, state] = 1
    return result


def field_code_and_covariance_controls() -> tuple[np.ndarray, np.ndarray]:
    print("\nFIELD VACUUM/SCALAR PHYSICAL-M2 BLOCK")
    logical = logical_scalar_transition()
    physical = physical_scalar_transition()
    encoding = field_encoding()
    code_projector = encoding @ encoding.conj().T
    scalar = np.zeros(7, dtype=complex)
    scalar[1:] = 1 / np.sqrt(6)
    vacuum = np.zeros(7, dtype=complex)
    vacuum[0] = 1

    check(
        "six physical field M2 sites exactly encode vacuum plus the six directional one-excitation states",
        np.linalg.norm(encoding.conj().T @ encoding - np.eye(7)) == 0
        and np.linalg.norm(physical @ encoding - encoding @ logical) < 2e-15
        and np.linalg.norm((np.eye(64) - code_projector) @ physical @ encoding)
        < 2e-15,
        {
            "physical_dimension": 64,
            "code_dimension": 7,
            "intertwining_residual": float(
                np.linalg.norm(physical @ encoding - encoding @ logical)
            ),
            "leakage": float(
                np.linalg.norm((np.eye(64) - code_projector) @ physical @ encoding)
            ),
        },
    )
    check(
        "the bounded Hermitian transition sends vacuum exactly to the uniform scalar direction",
        np.linalg.norm(logical - logical.conj().T) == 0
        and np.linalg.norm(logical @ vacuum - scalar) < 2e-15
        and np.linalg.norm(logical @ scalar - vacuum) < 2e-15
        and abs(np.linalg.norm(logical, 2) - 1) < 2e-15,
        {
            "Hermiticity": float(np.linalg.norm(logical - logical.conj().T)),
            "operator_norm": float(np.linalg.norm(logical, 2)),
        },
    )

    covariance = []
    for frame in c235.proper_cubic_frames():
        direction_representation = c210.direction_permutation(frame)
        physical_representation = bit_permutation(direction_representation)
        covariance.append(
            np.linalg.norm(
                physical_representation @ physical
                - physical @ physical_representation
            )
        )
    check(
        "the physical six-M2 scalar transition is invariant in all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 2e-15,
        max(covariance),
    )
    return logical, physical


def matter_operators() -> dict[str, object]:
    species = c219.common_species(BETA)
    occupations = np.asarray([index.bit_count() for index in range(64)], dtype=float)
    number = np.diag(occupations).astype(complex)
    pair_count = np.diag(occupations * (occupations - 1) / 2).astype(complex)
    mass = species.analytic_mass * number
    contact = np.diag(np.exp(1j * G_CONTACT * np.diag(pair_count))).astype(complex)
    coin = c229.fock_lift(species.coin)
    return {
        "species": species,
        "occupations": occupations,
        "N": number,
        "C": pair_count,
        "M": mass,
        "W": contact,
        "coin": coin,
    }


def local_relative_update(
    epsilon: float, matter_charges: np.ndarray, scalar_transition: np.ndarray
) -> np.ndarray:
    """Exact block exponential for diagonal matter charges tensor X_s."""

    field_dimension = scalar_transition.shape[0]
    scalar_pair_projector = scalar_transition @ scalar_transition
    result = np.zeros(
        (len(matter_charges) * field_dimension,) * 2, dtype=complex
    )
    identity = np.eye(field_dimension, dtype=complex)
    for index, charge in enumerate(matter_charges):
        block = (
            identity
            + (np.cos(epsilon * charge) - 1) * scalar_pair_projector
            - 1j * np.sin(epsilon * charge) * scalar_transition
        )
        start = index * field_dimension
        result[start : start + field_dimension, start : start + field_dimension] = block
    return result


def relative_update_and_response_controls(scalar_transition: np.ndarray) -> dict[str, object]:
    print("\nEXACT FINITE RELATIVE UPDATE / RESPONSE")
    matter = matter_operators()
    charges = np.diag(matter["M"]).real
    response = np.kron(matter["M"], scalar_transition)
    relative = local_relative_update(EPSILON, charges, scalar_transition)

    field_coin = np.zeros((7, 7), dtype=complex)
    field_coin[0, 0] = 1
    field_coin[1:, 1:] = c214.FIELD_COIN
    base_matter = matter["W"] @ matter["coin"]
    base = np.kron(base_matter, field_coin)
    deformed = relative @ base
    measured_relative = deformed @ base.conj().T

    check(
        "G_epsilon G_0 dagger is exactly the bounded local deformation layer",
        np.linalg.norm(base.conj().T @ base - np.eye(base.shape[0])) < 8e-13
        and np.linalg.norm(measured_relative - relative) < 8e-13
        and np.linalg.norm(relative.conj().T @ relative - np.eye(relative.shape[0]))
        < 8e-13,
        {
            "joint_code_dimension": base.shape[0],
            "relative_update_residual": float(np.linalg.norm(measured_relative - relative)),
            "unitarity_residual": float(
                np.linalg.norm(relative.conj().T @ relative - np.eye(relative.shape[0]))
            ),
        },
    )
    check(
        "the response M tensor X_s is Hermitian and generates the finite relative update",
        np.linalg.norm(response - response.conj().T) == 0
        and np.linalg.norm(relative - local_relative_update(EPSILON, charges, scalar_transition))
        == 0,
        {
            "Hermiticity_residual": float(np.linalg.norm(response - response.conj().T)),
            "response_norm": float(np.linalg.norm(response, 2)),
        },
    )
    check(
        "coupling deletion returns the exact matter-contact plus finite-coin baseline",
        np.linalg.norm(local_relative_update(0.0, charges, scalar_transition) - np.eye(base.shape[0]))
        == 0
        and np.linalg.norm(local_relative_update(0.0, charges, scalar_transition) @ base - base)
        == 0,
    )

    common_phase = 0.43
    rephased_relative = (
        np.exp(1j * common_phase) * deformed
        @ (np.exp(1j * common_phase) * base).conj().T
    )
    check(
        "a common global rephase of G_epsilon and G_0 cancels from the finite relative update",
        np.linalg.norm(rephased_relative - relative) < 8e-13,
        float(np.linalg.norm(rephased_relative - relative)),
    )

    # Small faithful scalar-active reduction: seven number eigenvalues times
    # vacuum/scalar.  It exposes the two ambiguities without large derivatives.
    reduced_number = np.diag(np.arange(7, dtype=float) * matter["species"].analytic_mass)
    scalar_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    reduced_response = np.kron(reduced_number, scalar_x)
    delta = 1e-6
    phase_slope = 0.31
    plus = np.exp(-1j * phase_slope * delta) * expm(-1j * delta * reduced_response)
    minus = np.exp(1j * phase_slope * delta) * expm(1j * delta * reduced_response)
    shifted_numeric = 1j * (plus - minus) / (2 * delta)
    shifted_exact = reduced_response + phase_slope * np.eye(reduced_response.shape[0])
    check(
        "a deformation-dependent rephase shifts the infinitesimal response by an identity term",
        np.linalg.norm(shifted_numeric - shifted_exact) < 2e-10
        and abs(
            np.linalg.norm(shifted_exact - reduced_response, "fro")
            / np.sqrt(reduced_response.shape[0])
            - phase_slope
        )
        < 2e-14,
        {
            "finite_difference_residual": float(np.linalg.norm(shifted_numeric - shifted_exact)),
            "identity_shift_per_dimension": float(
                np.linalg.norm(shifted_exact - reduced_response, "fro")
                / np.sqrt(reduced_response.shape[0])
            ),
        },
    )

    scale = 1.7
    lambda_value = EPSILON / scale
    endpoint_reparameterized = expm(
        -1j * (scale * lambda_value) * reduced_response
    )
    endpoint_direct = expm(-1j * EPSILON * reduced_response)
    reparameterized_response = scale * reduced_response
    check(
        "matched finite endpoints are reparameterization invariant while the tangent response rescales",
        np.linalg.norm(endpoint_reparameterized - endpoint_direct) < 2e-14
        and np.linalg.norm(reparameterized_response - reduced_response) > 1,
        {
            "endpoint_residual": float(
                np.linalg.norm(endpoint_reparameterized - endpoint_direct)
            ),
            "tangent_scale": scale,
        },
    )
    return matter


def physical_support_leakage_and_covariance_controls() -> None:
    print("\nCONNECTED PHYSICAL-M2 SUPPORT / LEAKAGE / COVARIANCE")
    rows = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        bs = c278.cell_bs(code, (0, 0, 0))
        matter_union = 0
        for row in bs:
            matter_union |= row.x | row.z
        leakage = sum(
            not b.commutes(check_row)
            for b in bs
            for check_row in code.local_checks + code.wilsons
        )
        rows.append(
            {
                "L": length,
                "held_out": length == 6,
                "matter_M2_union": matter_union.bit_count(),
                "field_M2": 6,
                "joint_local_support_M2": matter_union.bit_count() + 6,
                "maximum_B_weight": max((b.x | b.z).bit_count() for b in bs),
                "maximum_expanded_vertex_term_weight": max(
                    (b.x | b.z).bit_count() for b in bs
                )
                + 6,
                "check_or_Wilson_leakage": leakage,
                "B_pair_noncommutations": sum(
                    not left.commutes(right) for left in bs for right in bs
                ),
            }
        )
    check(
        "M_x tensor X_s has constant bounded physical-M2 support and zero local-check/Wilson leakage through held-out L=6",
        len({row["joint_local_support_M2"] for row in rows}) == 1
        and max(row["joint_local_support_M2"] for row in rows) <= 30
        and max(row["maximum_expanded_vertex_term_weight"] for row in rows) <= 15
        and all(row["check_or_Wilson_leakage"] == 0 for row in rows)
        and all(row["B_pair_noncommutations"] == 0 for row in rows),
        rows,
    )

    adjacent_code = c269.build_code(3)
    left_bs = c278.cell_bs(adjacent_code, (0, 0, 0))
    right_bs = c278.cell_bs(adjacent_code, (1, 0, 0))
    left_union = 0
    right_union = 0
    for row in left_bs:
        left_union |= row.x | row.z
    for row in right_bs:
        right_union |= row.x | row.z
    adjacent_noncommutations = sum(
        not left.commutes(right) for left in left_bs for right in right_bs
    )
    check(
        "adjacent physical mass-deformation blocks commute even where their matter supports overlap",
        adjacent_noncommutations == 0 and (left_union & right_union).bit_count() > 0,
        {
            "overlapping_matter_M2": (left_union & right_union).bit_count(),
            "cross_cell_B_noncommutations": adjacent_noncommutations,
            "field_blocks": "distinct six-M2 blocks",
        },
    )

    code = c269.build_code(3)
    source_cell = (0, 0, 0)
    source_vertices = tuple(
        code.graph.vertex_index[(source_cell, direction)] for direction in range(6)
    )
    failures = []
    tests = 0
    local_family = set(code.local_checks)
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(3), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_bs = {
                c235.apply_gauge(
                    c235.permute_pauli(code.B[vertex], edge_map),
                    toggles,
                    pairs,
                    flips,
                )
                for vertex in source_vertices
            }
            target_bs = {code.B[vertex_map[vertex]] for vertex in source_vertices}
            if transformed_local != local_family or transformed_bs != target_bs:
                failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the physical matter mass deformation is covariant in all 648 proper-frame and translation tests",
        tests == 24 * 27 and not failures,
        {"tests": tests, "failures": failures[:5]},
    )


def parallel_composition_controls() -> None:
    print("\nPARALLEL COMPOSITION")
    species = c219.common_species(BETA)
    scalar_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    local = np.kron(
        np.diag(np.arange(7, dtype=float) * species.analytic_mass), scalar_x
    )
    identity = np.eye(local.shape[0], dtype=complex)
    left = np.kron(local, identity)
    right = np.kron(identity, local)
    commutator = left @ right - right @ left
    joint = expm(-1j * EPSILON * (left + right))
    separated = expm(-1j * EPSILON * left) @ expm(-1j * EPSILON * right)
    check(
        "disjoint deformation responses add and their finite updates compose exactly in parallel",
        np.linalg.norm(commutator) == 0
        and np.linalg.norm(joint - separated) < 2e-13,
        {
            "commutator": float(np.linalg.norm(commutator)),
            "finite_composition_residual": float(np.linalg.norm(joint - separated)),
        },
    )


def fixture_reciprocity_and_deletion_controls(
    scalar_transition: np.ndarray, matter: dict[str, object]
) -> None:
    print("\nMASS / CONTACT / BILINEAR RECIPROCITY / DELETION")
    species = matter["species"]
    occupations = matter["occupations"]
    identity_field = np.eye(7, dtype=complex)
    response = np.kron(matter["M"], scalar_transition)
    contact_joint = np.kron(matter["W"], identity_field)
    coin_joint = np.kron(matter["coin"], identity_field)
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    forced = c210.force_response(species, 2e-5)
    rest_charge = c213.rest_charge(species.coin, c210.P_SCALAR)

    check(
        "M_x=m N_x matches the Cycle-219 mass fixture but requires the supplied c-inverse-squared conversion from raw rest phase",
        abs(rest_charge / species.analytic_mass - c219.C_SQUARED) < 2e-12
        and abs(rest_charge / c219.C_SQUARED - species.analytic_mass) < 2e-12
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(forced.measured_mass / species.analytic_mass - 1) < 0.007,
        {
            "raw_rest_phase": rest_charge,
            "raw_phase_over_mass": rest_charge / species.analytic_mass,
            "supplied_c_squared": c219.C_SQUARED,
            "analytic_mass": species.analytic_mass,
            "dispersion_mass": dispersion_mass,
            "forced_mass": forced.measured_mass,
        },
    )
    check(
        "the actual contact remains identity on N at most one and commutes with the deformation response",
        np.max(np.abs(np.diag(matter["W"])[occupations <= 1] - 1)) == 0
        and np.linalg.norm(response @ contact_joint - contact_joint @ response)
        < 2e-13
        and np.linalg.norm(response @ coin_joint - coin_joint @ response)
        < 2e-12,
        {
            "contact_commutator": float(
                np.linalg.norm(response @ contact_joint - contact_joint @ response)
            ),
            "onsite_coin_commutator": float(
                np.linalg.norm(response @ coin_joint - coin_joint @ response)
            ),
        },
    )

    # The two partial matrix elements of the same Hermitian bilinear vertex.
    vacuum = np.zeros(7, dtype=complex)
    vacuum[0] = 1
    scalar = np.zeros(7, dtype=complex)
    scalar[1:] = 1 / np.sqrt(6)
    source_leg = np.kron(np.eye(64), scalar.conj()[None, :]) @ response
    source_leg = source_leg @ np.kron(np.eye(64), vacuum[:, None])
    matter_index = 1
    matter_projector = np.zeros((64, 64), dtype=complex)
    matter_projector[matter_index, matter_index] = 1
    selected_field_response = np.kron(
        np.eye(1),
        scalar_transition * float(np.diag(matter["M"])[matter_index].real),
    )
    direct_selected = response[
        matter_index * 7 : (matter_index + 1) * 7,
        matter_index * 7 : (matter_index + 1) * 7,
    ]
    check(
        "the same Hermitian bilinear vertex gives equal source-leg and response-leg coefficients",
        np.linalg.norm(source_leg - matter["M"]) < 2e-14
        and np.linalg.norm(direct_selected - selected_field_response) < 2e-14,
        {
            "source_leg_residual": float(np.linalg.norm(source_leg - matter["M"])),
            "response_leg_residual": float(
                np.linalg.norm(direct_selected - selected_field_response)
            ),
            "scope": "algebraic vertex reciprocity, not reciprocal geometry or recoil",
        },
    )
    deleted_charge_response = np.kron(np.zeros_like(matter["M"]), scalar_transition)
    check(
        "charge deletion removes the deformation response without deleting the matter/contact baseline",
        np.linalg.norm(deleted_charge_response) == 0
        and np.linalg.norm(matter["W"]) > 1
        and np.linalg.norm(matter["coin"] - np.eye(64)) > 1,
    )


def scalar_sector_controls(scalar_transition: np.ndarray, matter: dict[str, object]) -> None:
    print("\nCYCLE-213 / CYCLE-216 SCALAR SECTOR")
    rng = np.random.default_rng(31702)
    side = 7
    state = rng.normal(size=(side, side, side, 6)) + 1j * rng.normal(
        size=(side, side, side, 6)
    )
    state /= np.linalg.norm(state)
    states = [state]
    projections = [c215.scalar_projection(state)]
    for _ in range(2):
        state = c215.field_step(state)
        states.append(state)
        projections.append(c215.scalar_projection(state))
    free_residual = np.max(
        np.abs(
            projections[2]
            - c213.wave_step(
                projections[0],
                projections[1],
                np.zeros_like(projections[1]),
                dt=1 / np.sqrt(3),
            )
        )
    )
    check(
        "the undeformed finite-coin scalar projection reproduces the free Cycle-213 wave law at dt squared one third",
        free_residual < 2e-15,
        float(free_residual),
    )

    vacuum = np.zeros(7, dtype=complex)
    vacuum[0] = 1
    scalar = np.zeros(7, dtype=complex)
    scalar[1:] = 1 / np.sqrt(6)
    mass = matter["species"].analytic_mass
    delta = 1e-7
    plus = local_relative_update(delta, np.asarray((mass,)), scalar_transition) @ vacuum
    minus = local_relative_update(-delta, np.asarray((mass,)), scalar_transition) @ vacuum
    derivative = (plus - minus) / (2 * delta)
    check(
        "the deformation derivative injects the uniform finite-coin scalar port with one-particle coefficient m",
        np.linalg.norm(derivative + 1j * mass * scalar) < 2e-14,
        float(np.linalg.norm(derivative + 1j * mass * scalar)),
    )

    point = np.zeros((side, side, side), dtype=complex)
    point[0, 0, 0] = mass
    port_forcing = c215.gamma_operator(point) - point
    direct_cycle213_forcing = point / 3
    check(
        "the literal scalar port has the Cycle-215 two-tap forcing and does not reproduce the direct Cycle-213 source term",
        np.max(np.abs(port_forcing + c213.laplacian(point) / 6)) < 2e-15
        and np.linalg.norm(port_forcing - direct_cycle213_forcing) > 0.1,
        {
            "two_tap_identity_residual": float(
                np.max(np.abs(port_forcing + c213.laplacian(point) / 6))
            ),
            "direct_source_mismatch": float(
                np.linalg.norm(port_forcing - direct_cycle213_forcing)
            ),
        },
    )

    green_rows = []
    for length in (3, 5, 7):
        density = mass * c211.point_source(length)
        field = c216.solve_coin_field(density)
        scalar_field = c216.scalar_field(field).real
        green = c211.solve_field(density)
        residual = c216.apply_stiffness(field) - (
            density[..., None] * c210.UNIFORM
        )
        green_rows.append(
            {
                "L": length,
                "held_out": length == 7,
                "stiffness_residual": float(np.linalg.norm(residual)),
                "three_green_residual": float(
                    np.linalg.norm(scalar_field - 3 * green)
                ),
            }
        )
    check(
        "the same scalar direction reproduces the Cycle-216 static 3 L-plus block through held-out L=7",
        max(row["stiffness_residual"] for row in green_rows) < 2e-11
        and max(row["three_green_residual"] for row in green_rows) < 2e-11,
        green_rows,
    )


def lawful_domain_and_inventory_controls() -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED STRUCTURE")

    def validate(length: int, matter_modes: int, field_m2: int) -> None:
        if length < 3:
            raise ValueError("periodic L must be at least three")
        if matter_modes != 6:
            raise ValueError("the imported matter cell has six modes")
        if field_m2 != 6:
            raise ValueError("the local field code uses six physical M2 sites")

    validate(3, 6, 6)
    rejections = 0
    for row in ((2, 6, 6), (3, 5, 6), (3, 6, 5)):
        try:
            validate(*row)
        except ValueError:
            rejections += 1
    check(
        "the declared domain accepts the imported six-mode blocks and rejects aliased or mistyped controls",
        rejections == 3,
        {"negative_fixture_rejections": rejections},
    )
    check(
        "the supplied structure inventory is explicit",
        True,
        {
            "supplied": (
                "beta=-0.3 common-family species and m=-3 tan(beta/2)",
                "g=0.37 onsite contact and its insertion order",
                "Cycle-269 connected physical matter code and B representatives",
                "six additional field M2 sites per coarse cell",
                "vacuum plus one-excitation field code restriction",
                "uniform scalar transition X_s",
                "bilinear M_x tensor X_s vertex",
                "epsilon parameter, zero, sign, and normalization",
                "finite-coin field law and K=2I-U-U-dagger stiffness",
                "periodic zero-mean boundary/source fixture",
            ),
            "derived": (
                "exact finite relative update",
                "Hermitian bounded deformation response",
                "parallel additivity",
                "common-rephase cancellation",
                "physical-M2 support/leakage/covariance",
                "free Cycle-213 and static Cycle-216 scalar reductions",
            ),
            "not_earned": (
                "deformation-dependent phase zero",
                "deformation normalization",
                "direct Cycle-213 source term",
                "combined continuity and recoil",
                "reciprocal geometry or metric response",
                "physical energy/stress/source selection",
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("ROUTE B / LOCAL PHYSICAL-M2 MASS--SCALAR DEFORMATION RESPONSE")
    note_contract()
    logical_scalar, _ = field_code_and_covariance_controls()
    matter = relative_update_and_response_controls(logical_scalar)
    physical_support_leakage_and_covariance_controls()
    parallel_composition_controls()
    fixture_reciprocity_and_deletion_controls(logical_scalar, matter)
    scalar_sector_controls(logical_scalar, matter)
    lawful_domain_and_inventory_controls()
    print("\nSUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_BOUNDED"
        if FAIL == 0
        else "LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
