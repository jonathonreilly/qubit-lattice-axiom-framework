#!/usr/bin/env python3
"""Cycle 511 revision-4 Route-C response contract, cheap preflight only.

Freeze the missing Route-C law-level inputs without evolving a response or a
held row.  The preflight binds the immutable Cycle-509 A/B evidence and the
bounded Cycle-510 local certificate, fixes the rho_AB3 matter preparation,
ordinary-SWAP mediator statistics, update/free/deletion/boundary/observable
contracts, eight Route-C train identities, and an atomic thirteen-row held
menu with a matched-beta L19 size row.

Authority: none.  Audit: unset.  Response rows executed: zero.  Held rows
executed: zero.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from hashlib import sha256
from itertools import combinations
import json
import os
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_local_bond_character_bulk_tournament_preflight_cycle509_2026_07_20 as c509
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 4
MODE = "contract-preflight"
ROUTE_C = "C-open-octahedral-multimediator"
MIDDLE_BETA = "-4pi/9"
HELD_ALIAS_BETA = "-8pi/9"
DELETIONS = (
    "emitter",
    "collision",
    "mediator-stream",
    "contact",
    "probe-coin",
    "source-mass-factor",
    "probe-mass-factor",
)
REVERSE = (1, 0, 3, 2, 5, 4)
PACKET_NAME = "rho_AB3"
STATISTICS_LAW = "hard-core-qubit-spin-occupation-with-ordinary-SWAP"
NUMERIC_TOLERANCE = 1e-12
SIZE_STABILITY_RELATIVE_TOLERANCE = 0.10
SIGNAL_ABSOLUTE_FLOOR = 1e-10
LEDGER_ACTIVE_FLOOR = 1e-10
SOURCE_LEDGER_TOLERANCE = 1e-8

C509_PREFLIGHT = ROOT / "scripts/physical_local_bond_character_bulk_tournament_preflight_cycle509_2026_07_20.py"
C509_PREFLIGHT_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_BOND_CHARACTER_BULK_TOURNAMENT_PREFLIGHT_CYCLE509_NOTE_2026-07-20.md"
C509_SCIENCE_RUNNER = ROOT / "scripts/physical_local_bond_character_ab_science_train_cycle509_2026_07_20.py"
C509_SCIENCE_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_BOND_CHARACTER_AB_SCIENCE_TRAIN_CYCLE509_NOTE_2026-07-20.md"
C509_OUTPUT = ROOT / "outputs/physical_local_bond_character_ab_train_cycle509_2026_07_20"
C509_RECEIPT = C509_OUTPUT / "run_receipt.json"
C509_RESULT = C509_OUTPUT / "science_result.json"
C509_INDEX = C509_OUTPUT / "artifact_index.json"
C510_RUNNER = ROOT / "scripts/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.py"
C510_LOG = ROOT / "outputs/physical_route_c_local_seven_mode_receiver_cycle510_2026_07_20.log"
C510_RECEIPT = ROOT / "outputs/physical_route_c_local_seven_mode_receiver_cycle510_receipt_2026_07_20.json"
C510_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUTE_C_LOCAL_SEVEN_MODE_RECEIVER_CYCLE510_NOTE_2026-07-20.md"
C210_RUNNER = ROOT / "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py"
C219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
C220_RUNNER = ROOT / "scripts/generated_beta_phase_register_cycle220_2026_07_16.py"
C230_RUNNER = ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
C441_RUNNER = ROOT / "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py"
C501_RUNNER = ROOT / "scripts/physical_reciprocal_mediator_contact_dressed_tournament_cycle501_2026_07_20.py"

STRICT_HASHES = {
    C509_PREFLIGHT: "44a0430dafd31db471e6ada2435aa4a819637d09ac0af15ac387126e61ccd458",
    C509_PREFLIGHT_NOTE: "733aa72a2b2ef43f5b3a049903a85fa81b18c1413bcbe4d66f2a17345dce1d50",
    C509_SCIENCE_RUNNER: "970deb948966b8fc9b8d16233225356871f287d16ce34500897cb2cb441fe667",
    C509_SCIENCE_NOTE: "f23711fa31138610510e5294c06d399fac1d9d4731a44430fbcc099f24777385",
    C509_RECEIPT: "efa4e44da10bb2f5d968ededc5db8b2e9a6e9ec34bbfed278443271411b1d413",
    C509_RESULT: "fed10c31661cc1d2e5a3f0f2b04a9e06dcb32913621b032b39c177d35b41a7ba",
    C509_INDEX: "6974e078649be33bddade6bb6f3598aab909ffd68b6301a75e53bb707d38cffe",
    C510_RUNNER: "57592ac109321cb273f73b312d205cefc18427329d20c34f18f63d56dcbd5175",
    C510_LOG: "f8c12e463d6b44df22964b04a05d0b60e332ab408e4340fdd61421555762d84a",
    C510_RECEIPT: "32f6dc682a0b7372cd867fd0e84f0aea6ff6ebf74931cb7c72d46653ed5b7595",
    C510_NOTE: "3d3e7b44d7667fa39a0bfb1283e1d330ecd4b22bd212c217df1b4d0950579a36",
    C210_RUNNER: "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    C219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    C220_RUNNER: "252708e5adf782d9ad2869add0d64fa757d9d0473d054ee548e98e31d5f7276f",
    C230_RUNNER: "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    C441_RUNNER: "c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4",
    C501_RUNNER: "7e8a88c5b0cdd576d868a3932d820da7f9cf985b10de498c83d34eb35daa959d",
}

EXPECTED_C509_FULL_TRAIN_SHA256 = "d235ce413eaba7ac62c9100d45ef93824c246a4646f4cd9316c5a0191f1c73d8"
EXPECTED_C509_FULL_HELD_SHA256 = "7dcaf19fb91b49bbe6528f124e4f428d7d54774390ff608e6afef5841657facf"
EXPECTED_C509_AB34_SHA256 = "f6dfdbd48ef38a10f2b7659ef5192950a0c17c257c042be8515da355999a44b2"
EXPECTED_C509_AB_HELD10_SHA256 = "66c6e1a9a4667b367424c3d69208d7b3a9a98dcb308febb1e67035fb0388b1a3"

# Filled only from the declarations below.  These constants make accidental
# edits fail closed instead of silently creating a revision-5 contract.
EXPECTED_PACKET_SHA256 = "c77a770aeae53aa84bfd48a1692ea8f1599ca22f1d3121f6a5aac06cb5e4145c"
EXPECTED_UPDATE_SHA256 = "1f2aff2a0021afa3fd3584d3e460114945d46e59af23e4618f7b7195793ef545"
EXPECTED_FREE_SHA256 = "19f170f573833451e8025b70cc0ca8a01bdd75f3f6cbb9bc900900c2eb18f4af"
EXPECTED_DELETION_SHA256 = "00555251b807eb0b8040717f9a77c1c7af485b64317ace2973c299c7fb94520b"
EXPECTED_BOUNDARY_SHA256 = "5436bd18ae02e5fc88a508967094dc95a60e102738048a3730c1ce45867afc26"
EXPECTED_OBSERVABLE_SHA256 = "c1e36d84110591c225c3c6062ddd8e0dfa7c261bdc4647061225da8b18d30102"
EXPECTED_OCCUPATION_SPECIES_SHA256 = "7103fe496547e8c25117347aea7ab5cc0c20e3e5195a81c7571feb20609b6ecf"
EXPECTED_PRESERVATION_SHA256 = "ba9ae4779f05b0f79fd24f3149f2655957ec662ca61ad19e3e475d2cd94c4597"
EXPECTED_ROUTE_C8_SHA256 = "bb3ea5f4f6d951ea55071daab10b0417c99bbf8da95497165ecb5c6fd8ba59ef"
EXPECTED_ATOMIC_HELD13_SHA256 = "09912359e4a0ed89f256c16ba01893be9d596e26f7831b7291c71ac901c4e9f6"
EXPECTED_BOUNDARY_CONTROLS_SHA256 = "686274ee85550d7cff2cd55f6695044b1b861c6f0157b2375fe9c77f82fa4ae5"
EXPECTED_AUTHORIZATION_SHA256 = "b351db1be8de62acdbfacca9cbfa89424705d230f564d5c4bc6cb6358be3d83e"

EXPECTED_C509_ROUTE_C_TRAIN_ROW_SHA256 = (
    "e145c5775242005ef3e819a3c7987e08bdb91a2aac62a8ddf10b12536bfe567f",
    "528e127838c8b66b76b9e2083e2a4642bc25199e9a069ff162c2516348d3550c",
    "2111cf3a3b63ec8e63f1158f6ad850351b53280c03d6f8abb6962574348379bf",
    "820e65a1ae68676d123891d4aba1f3900144a4aaee8de60d12e4d33ea73bd843",
    "38d86784537303e418586d2116e7edc0a6844d4faf76ac082188810d238d601b",
    "125e44cb02183b57053cba075d0b73c21de93f35677762c683e1501694230c87",
    "87ebed692e14fe157c9d59dae20349bd9d98cb0c410a4aabf04b7e0fa3163320",
    "f62ecb670e4249a544caaf9fac524f782edff7c3790ab17616fc37fe68ce1e6b",
)
EXPECTED_C509_ROUTE_C_HELD_ROW_SHA256 = (
    "52ac4fb3b7d4f4ae5061da1f3924b812a296c9dd2c4ffc4088fb13aa48761a8e",
    "7432e46a0d46452914c9af08294e5daebc137a31b9b13121564ce6ab036d6b7a",
)

CYCLE511_SCOUT_AUTHORIZATION_ENV = "CYCLE511_ROUTE_C_SCOUT_AUTHORIZATION"
CYCLE511_SCOUT_AUTHORIZATION_TOKEN = (
    "root-cycle511-revision4-route-c-scout-after-dry-review-2026-07-20"
)
CYCLE511_TRAIN_AUTHORIZATION_ENV = "CYCLE511_ROUTE_C_TRAIN_AUTHORIZATION"
CYCLE511_TRAIN_AUTHORIZATION_TOKEN = (
    "root-cycle511-revision4-route-c-train-after-scout-review-2026-07-20"
)

AUTHORIZATION_VARIABLES = (
    "CYCLE509_SCOUT_AUTHORIZATION",
    "CYCLE509_TRAIN_AUTHORIZATION",
    CYCLE511_SCOUT_AUTHORIZATION_ENV,
    CYCLE511_TRAIN_AUTHORIZATION_ENV,
)

ROUTE_C_MATCHED_SIZE_HELD = c509.BulkGeometry(
    "blind-held-hard-wall-octahedral-Q6-L19-matched-r4-depth5",
    19,
    (9, 9, 9),
    4,
    c509.octahedral_sources((9, 9, 9), 4),
    tuple(range(6)),
    6,
    5,
    (2, 3, 4, 5),
    "hard-wall",
    True,
)


TESTS: list[dict] = []


def check(name: str, condition: bool, detail: object = None) -> None:
    TESTS.append({"name": name, "passed": bool(condition), "detail": detail})


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: object) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def json_default(value: object) -> object:
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"unsupported JSON value {type(value).__name__}")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    permutation = c210.direction_permutation(frame)
    return tuple(int(np.argmax(permutation[:, direction])) for direction in range(6))


def frame_cell(cell: tuple[int, int, int], frame: np.ndarray) -> tuple[int, int, int]:
    return tuple(int(value) for value in frame @ np.asarray(cell, dtype=int))


Mode = tuple[tuple[int, int, int], int]
Ray = dict[tuple[Mode, Mode], complex]


def packet_component(axis: int) -> Ray:
    """Exact normalized A/B corridor wedge on one centered axis."""
    positive = 2 * axis
    negative = positive + 1
    step = tuple(int(value) for value in c210.DIRECTIONS[positive])
    weights = (-1, 0, 1)
    envelope = (1 / np.sqrt(6), 2 / np.sqrt(6), 1 / np.sqrt(6))
    left: dict[Mode, complex] = {}
    right: dict[Mode, complex] = {}
    for offset, amplitude in zip(weights, envelope):
        cell = tuple(offset * value for value in step)
        left[(cell, positive)] = amplitude
        right[(cell, negative)] = amplitude
    result: Ray = {}
    for left_mode, left_value in left.items():
        for right_mode, right_value in right.items():
            raw = (left_mode, right_mode)
            ordered = tuple(sorted(raw))
            sign = 1 if raw == ordered else -1
            result[ordered] = result.get(ordered, 0j) + sign * left_value * right_value
    return {key: value for key, value in result.items() if abs(value) > 1e-15}


def transform_ray(ray: Ray, frame: np.ndarray) -> Ray:
    mapping = direction_map(frame)
    result: Ray = {}
    for pair, amplitude in ray.items():
        raw = tuple((frame_cell(cell, frame), mapping[direction]) for cell, direction in pair)
        ordered = tuple(sorted(raw))
        sign = 1 if raw == ordered else -1
        result[ordered] = result.get(ordered, 0j) + sign * amplitude
    return result


def ray_inner(left: Ray, right: Ray) -> complex:
    return sum(np.conj(value) * right.get(key, 0j) for key, value in left.items())


def packet_contract() -> dict:
    return {
        "name": PACKET_NAME,
        "matter_number": 2,
        "kind": "operational-density-operator-equal-mixture-of-three-orthogonal-pure-axis-wedges",
        "density_operator_exact": "rho_AB3=(|psi_x><psi_x|+|psi_y><psi_y|+|psi_z><psi_z|)/3",
        "mixture_weights_exact": ("1/3", "1/3", "1/3"),
        "components": tuple(
            {
                "axis": axis,
                "cells_relative_to_probe": tuple(
                    tuple(
                        offset * int(c210.DIRECTIONS[2 * axis, coordinate])
                        for coordinate in range(3)
                    )
                    for offset in (-1, 0, 1)
                ),
                "envelope_exact": "(1,2,1)/sqrt(6)",
                "antisymmetric_orbitals": (2 * axis, 2 * axis + 1),
            }
            for axis in range(3)
        ),
        "density_trace_exact": 1,
        "density_rank": 3,
        "purity_exact": "1/3",
        "union_support_relative_cells": (
            (-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 0),
            (0, 0, 1), (0, 1, 0), (1, 0, 0),
        ),
        "one_particle_modes_on_union_support": 18,
        "union_wedge_dimension": 153,
        "nonzero_wedge_configurations_per_component": 9,
        "initial_collision_active_weight_per_direction": {
            "outward_neighbor": "5/108",
            "center": "2/27",
            "inward_neighbor": "5/108",
            "three_cell_total": "1/6",
        },
        "initial_same_cell_contact_weight": "1/2",
        "density_evaluation_order": (
            "evolve all three pure components linearly; average signed branch "
            "expectations with weights 1/3 before abs, max, CV, classifier, or distance"
        ),
        "Born_or_actualization_claim": False,
        "proper_cubic_transport": "the three component projectors permute under all 24 frames",
        "autonomous_preparation_claim": False,
    }


def packet_numeric_controls(components: tuple[Ray, ...]) -> dict:
    wedge_basis = tuple(sorted({key for component in components for key in component}))
    one_particle_modes = {
        mode for component in components for pair in component for mode in pair
    }
    support_cells = {cell for cell, _direction in one_particle_modes}
    vectors = np.zeros((len(wedge_basis), len(components)), dtype=complex)
    for column, component in enumerate(components):
        for row, key in enumerate(wedge_basis):
            vectors[row, column] = component.get(key, 0j)
    density = vectors @ vectors.conj().T / 3
    eigenvalues = np.linalg.eigvalsh(density)

    envelope_probabilities = np.asarray((1 / 6, 4 / 6, 1 / 6), dtype=float)
    collision_weights = tuple(
        float(probability * (1 - probability) / 3)
        for probability in envelope_probabilities
    )
    contact_weights = tuple(
        float(
            sum(
                abs(amplitude) ** 2
                for pair, amplitude in component.items()
                if pair[0][0] == pair[1][0]
            )
        )
        for component in components
    )
    return {
        "component_nonzero_counts": tuple(len(component) for component in components),
        "one_particle_mode_count": len(one_particle_modes),
        "support_cell_count": len(support_cells),
        "nonzero_union_wedge_configuration_count": len(wedge_basis),
        "ambient_union_wedge_dimension": len(one_particle_modes) * (len(one_particle_modes) - 1) // 2,
        "density_trace_residual": float(abs(np.trace(density) - 1)),
        "density_Hermiticity_residual": float(np.linalg.norm(density - density.conj().T)),
        "density_rank": int(np.count_nonzero(eigenvalues > NUMERIC_TOLERANCE)),
        "density_purity": float(np.trace(density @ density).real),
        "density_nonzero_eigenvalues": tuple(
            float(value) for value in eigenvalues if value > NUMERIC_TOLERANCE
        ),
        "collision_active_weights_neighbor_center_neighbor": collision_weights,
        "contact_weights_by_component": contact_weights,
        "mixed_contact_weight": float(sum(contact_weights) / 3),
    }


def factor_coordinate_controls() -> dict:
    register, _mass, positive = c509.mass_stack()
    rows = {}
    for name, beta in (
        ("train_and_matched_size_beta_-4pi_over_9", -4 * np.pi / 9),
        ("held_beta_zero", 0.0),
        ("held_beta_-8pi_over_9", -8 * np.pi / 9),
    ):
        ray = c509.beta_ray(register, beta)
        raw = float(np.vdot(ray, positive @ ray).real)
        mass = 0.0 if abs(raw) < c509.NUMERIC_TOLERANCE else raw
        angle = c509.EMITTER_COUPLING * mass
        rows[name] = {
            "M_plus": mass,
            "emitter_and_collision_angle": angle,
            "per_source_update1_emitted_weight": float(np.sin(angle) ** 2),
        }
    rows["held_beta_zero"].update({
        "decoupling_null": True,
        "global_mediator_Q6_remains_parked": True,
    })
    rows["held_beta_-8pi_over_9"]["principal_mass_or_inertia_claim"] = False
    rows["angle_ceiling"] = 0.35
    return rows


def update_contract() -> dict:
    return {
        "displayed_word": (
            "G = S_mediator[J S_face] U_Cycle501_sum[0.02 M_plus(probe)] "
            "U_Cycle230_contact[0.37] S_signed_CAR_3D "
            "Gamma(Cycle219_coin(beta_probe)) "
            "U_six_source_emitter[0.02 M_plus(source)]"
        ),
        "operator_application_order": (
            "six-source-emitter",
            "Cycle219-matter-coin",
            "signed-CAR-stream",
            "Cycle230-contact",
            "one-exponential-of-summed-Cycle501-collision",
            "mediator-J-S_face-moving-stream",
        ),
        "emitter": {
            "coefficient": 0.02,
            "factor": "M_plus(source_beta)",
            "six_disjoint_sources": True,
            "parked_to_inward_direction": True,
            "local_generator": "H_e=|inward><parked|+|parked><inward|",
            "unitary": "exp(+i theta_e H_e)",
            "amplitude_convention": "+i sin(theta_e) on parked/inward exchange",
            "invocations": "all six disjoint source emitters exactly once per update",
        },
        "factor_coordinates": factor_coordinate_controls(),
        "matter_coin": "Cycle219 common six-direction coin at probe_beta",
        "matter_stream": (
            "exterior lift of the finite hard-wall one-body permutation: signed "
            "intrinsic-CAR face FSWAP layer followed by onsite antipodal reversal J"
        ),
        "contact": {"Cycle230_coupling": 0.37, "same_cell": True},
        "collision": {
            "coefficient": 0.02,
            "factor": "M_plus(probe_beta)",
            "local_generator": (
                "sum over d in {0,2,4} of "
                "a_d^dagger a_reverse(d) f_reverse(d)^dagger f_d plus Hermitian conjugate"
            ),
            "matter_signs": "canonical six-mode CAR exterior ordering",
            "mediator_ladders": "ordinary hard-core qubit/spin raising and lowering",
            "unitary": "exp(+i theta_c H_collision)",
            "simultaneous_rule": "one exponential of the summed local generator",
            "invocations": "all cells exactly once per update",
            "host_direction_order": False,
            "six_directed_terms_plus_HC_double_count_forbidden": True,
        },
        "mediator_statistics": STATISTICS_LAW,
        "mediator_stream": (
            "finite-no-wrap hard wall: ordinary internal-face SWAP first, "
            "outward rail fixed by face layer, then onsite antipodal reversal J"
        ),
        "stream_inverse": "S_face followed by J when read in forward application order (J acts first)",
        "inverse": "literal reverse adjoint complete word",
        "sample_surface": "after-complete-update-word",
        "causal_timing": {
            "incoming_neighbor_collision_update": "source_radius",
            "center_collision_update": "source_radius+1",
            "post_complete_word_surface_sees_same_update_collision_consequence": True,
        },
        "update_is_physical_time_claim": False,
    }


def free_contract() -> dict:
    return {
        "name": "matched-free",
        "same_initial_rho_AB3": True,
        "same_six_parked_Q6_state": True,
        "emitter_angle": 0,
        "collision_angle": 0,
        "same_probe_coin_CAR_stream_contact_and_boundary_law": True,
        "same_route_deletion_applied": True,
        "state_precedence": (
            "form interacting and free base angles first, then apply the named "
            "row deletion deterministically; factor deletion never turns a zero free angle on"
        ),
        "repeat_exactly": True,
        "interaction_minus_free": True,
        "free_is_not_zero_state": True,
    }


def authorization_contract() -> dict:
    return {
        "dry_preflight_rejects_variable_presence_even_empty": AUTHORIZATION_VARIABLES,
        "legacy_Cycle509_tokens_never_authorize_Cycle511": True,
        "scout": {
            "environment": CYCLE511_SCOUT_AUTHORIZATION_ENV,
            "exact_token": CYCLE511_SCOUT_AUTHORIZATION_TOKEN,
            "scope": "RouteC8 index0 intact L15 middle-beta resource sentinel only",
            "science_rows": 0,
            "response_quarantined": True,
            "selector": False,
            "refit": False,
            "resource_ceiling": {
                "wall_seconds": 1200,
                "RSS_bytes": 3000000000,
                "swap_count": 0,
            },
        },
        "train": {
            "environment": CYCLE511_TRAIN_AUTHORIZATION_ENV,
            "exact_token": CYCLE511_TRAIN_AUTHORIZATION_TOKEN,
            "scope": "all eight RouteC train rows atomically",
            "requires_reviewed_exact_scout_receipt": True,
            "selector": False,
            "refit": False,
            "per_row_resource_ceiling": {
                "wall_seconds": 600,
                "RSS_bytes": 3000000000,
                "swap_count": 0,
            },
        },
        "multiple_or_conflicting_authorization_variables_rejected": True,
        "held": {
            "authorization_environment": None,
            "evaluator_present": False,
            "status": "locked until complete A/B/C train disposition and a later fail-closed surface",
        },
        "authorization_is_host_execution_safety_not_physical_control": True,
    }


def deletion_contract() -> dict:
    return {
        "ordered_deletions": DELETIONS,
        "route_wide_and_proper_cubic": True,
        "applies_symmetrically_to": "interacting-and-matched-free",
        "definitions": {
            "emitter": "set all six source-emitter angles to zero",
            "collision": "set the summed collision angle to zero",
            "mediator-stream": "replace the complete J S_face layer by identity",
            "contact": "set Cycle230 g to zero in both partners",
            "probe-coin": "replace every Cycle219 probe coin by identity in both partners",
            "source-mass-factor": "replace M_plus(source_beta) by exactly one",
            "probe-mass-factor": "replace M_plus(probe_beta) by exactly one",
        },
        "Route_C_gate_supersedes_Cycle509_terminal_deletion_declarations": True,
        "numeric_thresholds": {
            "signal_absolute_floor": SIGNAL_ABSOLUTE_FLOOR,
            "ledger_active_floor": LEDGER_ACTIVE_FLOOR,
            "source_ledger_repeat_tolerance": SOURCE_LEDGER_TOLERANCE,
            "technical_residual_ceiling": 1e-8,
            "boundary_reflection_input_ceiling": 1e-12,
        },
        "maximum_row_numeric_residual": (
            "maximum of the reported interacting/free/repeated-free norm residuals, "
            "free-repeat state residual, interacting/free inverse-state residuals, "
            "matter-number residual, mediator-charge residual, and local-unitary residuals; "
            "physical response values, occupation weights, and deletion distances are excluded"
        ),
        "epsilon_signal": (
            "epsilon_signal(row)=max(1e-10,10*maximum_row_numeric_residual(row))"
        ),
        "null_ceiling": "epsilon_signal(deleted_row)",
        "distance_definitions": {
            "Z_full": "max over full retained matter field of abs(delta_b_deleted)",
            "Z_path": "max over six center anchors and window of abs(T_deleted)",
            "D_full": "max abs(delta_b_intact-delta_b_deleted)",
            "D_path": "max over six center anchors and window of abs(T_intact-T_deleted)",
            "comparison_floor": "max(epsilon_signal(intact),epsilon_signal(deleted))",
        },
        "mediator_ledger_definitions": {
            "Q_emit_update1": (
                "total directional-mediator occupation immediately after all six emitters "
                "in update1"
            ),
            "Q_center_window": (
                "maximum total directional-mediator occupation at the center on the "
                "post-complete-word response surfaces"
            ),
            "Q_off_source_window": (
                "maximum total mediator occupation outside the six source cells on the "
                "post-complete-word response surfaces"
            ),
            "Q_parked_update1": (
                "total parked-mediator occupation immediately after all six emitters in update1"
            ),
        },
        "gates": {
            "emitter": (
                "zero emitter angle, global Q6 remains parked, no moving-mediator "
                "source output or center arrival, and complete matter-CAR delta field null"
            ),
            "collision": (
                "zero collision angle with source output and center-arrival mediator ledger active; "
                "complete matter-CAR interaction-minus-free delta field null; report "
                "intact-vs-deleted primary and full-field distances"
            ),
            "mediator-stream": (
                "stream identity, zero mediator displacement, and null center arrival/anchor; "
                "do not require global matter-field null because source-tail collisions can begin "
                "by update3; classify primary/full-field distances"
            ),
            "contact": "executed g=0 plus primary/full-field deletion distances",
            "probe-coin": "executed identity coin plus primary/full-field deletion distances",
            "source-mass-factor": "executed source factor one plus source-ledger and response distances",
            "probe-mass-factor": (
                "executed probe factor one, unchanged source ledger within its separate tolerance, "
                "plus response distances"
            ),
        },
        "exact_validity_table": {
            "common": (
                "valid iff every reported response, distance, and ledger scalar is finite, every "
                "declared finite-row technical residual is <=1e-8, structural outside count is "
                "zero, Q_reflect_input<=1e-12, the named deletion is executed in both interacting "
                "and matched-free partners, and no selector/refit occurs"
            ),
            "emitter": (
                "common AND emitter angle exactly zero AND Q_emit_update1<=null_ceiling AND "
                "Q_center_window<=null_ceiling AND abs(Q_parked_update1-6)<=null_ceiling "
                "AND Z_full<=null_ceiling"
            ),
            "collision": (
                "common AND collision angle exactly zero AND Q_emit_update1>1e-10 AND "
                "Q_center_window>1e-10 AND Z_full<=null_ceiling"
            ),
            "mediator-stream": (
                "common AND mediator stream is exact identity AND Q_emit_update1>1e-10 AND "
                "Q_off_source_window<=null_ceiling AND Q_center_window<=null_ceiling "
                "AND Z_path<=null_ceiling; Z_full is unrestricted"
            ),
            "contact": "common AND executed Cycle230 contact coupling is exactly zero",
            "probe-coin": "common AND executed Cycle219 matter coin is exactly identity",
            "source-mass-factor": (
                "common AND applied source factor is exactly one AND "
                "abs(Q_emit_update1_deleted-Q_emit_update1_intact)>1e-8"
            ),
            "probe-mass-factor": (
                "common AND applied probe factor is exactly one AND "
                "abs(Q_emit_update1_deleted-Q_emit_update1_intact)<=1e-8"
            ),
        },
        "exact_disposition_table": (
            "invalid if the deletion-specific validity predicate is false; otherwise "
            "primary-sensitive if D_path>=comparison_floor; otherwise full-field-sensitive "
            "if D_full>=comparison_floor; otherwise coexistence-only"
        ),
        "dispositions": (
            "primary-sensitive", "full-field-sensitive", "coexistence-only", "invalid"
        ),
        "coexistence_only_is_not_load_bearing": True,
        "no_single_source_or_axis_deletion": True,
        "effect_distance_required_in_train": True,
        "metadata_only_pass_forbidden": True,
    }


def preservation_contract() -> dict:
    return {
        "scope": "inherited one-particle mass/coin coordinate preservation, not a new inertia derivation",
        "execution_obligation": (
            "execute and report once in every Cycle511 resource-scout and RouteC8 train invocation"
        ),
        "safe_Cycle219_betas": ("-2pi/9", "-4pi/9", "-2pi/3"),
        "for_each_safe_beta": {
            "Cycle219_rest_mass_equals_analytic_ceiling": 1e-8,
            "coin_unitarity_residual_ceiling": 1e-8,
            "coin_all24_covariance_residual_ceiling": 1e-10,
        },
        "Cycle230_contact_identity_on_N_le_1": True,
        "Cycle501_collision_identity_on_directional_mediator_Q0": True,
        "finite_hardwall_one_body_stream": {
            "exact_permutation": True,
            "inverse_failures": 0,
            "proper_cubic_frame_failures": 0,
            "reflection_input_ceiling": 1e-12,
        },
        "held_-8pi_over_9_principal_mass_or_inertia_test": False,
        "finite_hardwall_dispersion_claim": False,
    }


def revision_geometry(geometry: c509.BulkGeometry) -> dict:
    result = asdict(geometry)
    result["boundary"] = "finite-no-wrap-hard-wall-reflecting-J-S_face"
    return result


def boundary_contract() -> dict:
    return {
        "law": "finite-no-wrap-hard-wall-reflecting-J-S_face",
        "dynamical_lattice": "finite L^3 cube with no wrap, absorption, or clipping",
        "forward_direction_stream": (
            "S_med=J composed with S_face: internal facing rails SWAP; outward face rail "
            "is fixed by S_face and then mapped to its inward antipode by J"
        ),
        "inverse_direction_stream": "S_face composed with J",
        "matter_face_statistics": "FSWAP",
        "mediator_face_statistics": "ordinary SWAP",
        "declared_cubes": {
            "train": revision_geometry(c509.ROUTE_C_TRAIN),
            "held_joint_mass_volume": revision_geometry(c509.ROUTE_C_HELD),
            "held_matched_beta_size_only": revision_geometry(ROUTE_C_MATCHED_SIZE_HELD),
        },
        "finite_runner_rule": "execute the exact finite permutation; never allocate, wrap, drop, or query an exterior mode",
        "required_structural_outside_cube_occupation": 0,
        "boundary_shell_occupation": "retained and reported separately; not called outside leakage",
        "numerical_outside_leakage_ceiling": 1e-12,
        "reflection_input_gate": (
            "Q_reflect_input is occupation on an outward-directed boundary rail "
            "immediately before S_face; require <=1e-12 through the sample window"
        ),
        "boundary_shell_zero_requirement": False,
        "leakage_and_shell_are_separate_gates": True,
        "periodic_alias_forbidden": True,
    }


def observable_contract() -> dict:
    return {
        "surface": "after-complete-update-word",
        "primary_occupation_species": "matter-CAR-direction-occupation",
        "occupation": "n_postword_matter_CAR(x,d,t)",
        "oriented_bond_field": (
            "b_d(x,t)=n_postword_matter_CAR(x,d,t)"
            "-n_postword_matter_CAR(x-e_d,reverse(d),t)"
        ),
        "oriented_bond_domain": (
            "B_L={(x,d): x in Lambda_L and x-e_d in Lambda_L}; no exterior "
            "occupation or zero-extension convention"
        ),
        "oriented_bond_domain_count": "abs(B_L)=6*L^2*(L-1)",
        "oriented_bond_redundancy": "b_reverse(d)(x-e_d,t)=-b_d(x,t)",
        "oriented_bond_domain_proper_cubic_invariant": True,
        "response_field": "delta_b=b_interacting-b_matched_free",
        "full_field_retention": (
            "every interior oriented bond in the declared domain at every response-window update"
        ),
        "center_anchor_trace": (
            "for the source whose inward direction is d, T_d(t)=delta_b_d(c,t); "
            "the six-direction definition carries the sign for negative axes"
        ),
        "radial_path_field": (
            "retain delta_b_d(s+k e_d,t) for k=1..source_radius as a diagnostic path, "
            "but never substitute a fitted path average for the center anchor"
        ),
        "per_source_scalar": "R_d=max over the frozen response window of abs(T_d(t))",
        "primary_scalar": "Rbar=(1/6) sum_d R_d",
        "max_is_preregistered_not_a_row_selector": True,
        "symmetric_train_per_source_CV_ceiling": 0.10,
        "signal_absolute_floor": 1e-10,
        "field_norms_diagnostic_only": True,
        "mediator_ledger": (
            "retained separately: parked/emitted Q, source output, displacement, center arrival, "
            "boundary shell, and Q_reflect_input; never substituted for the matter bond contrast"
        ),
        "terminology": "directional occupation-difference field; not certified current, force, gravity, rate, or energy",
        "held_size_metric": {
            "row": "blind-held-matched-beta-size-control L19 source=probe=-4pi/9",
            "baseline": "intact L15 source=probe=-4pi/9",
            "isolated_geometry_change": "side 15 to 19 only; radius4, depth5, window(2,3,4,5) unchanged",
            "tau_alignment": "tau=t-(source_radius+1), so tau=0 is the center-collision update",
            "normalization": "per source with no volume, radius, shell-area, or distance rescaling",
            "epsilon_pair": "max(epsilon_signal_L15,epsilon_signal_L19)",
            "D_R": "abs(Rbar_L19-Rbar_L15)/max(Rbar_L15,epsilon_pair)",
            "D_trace": (
                "max over all six directions and aligned tau of abs(T_L19-T_L15) "
                "/ max(Rbar_L15,epsilon_pair)"
            ),
            "D_R_ceiling": SIZE_STABILITY_RELATIVE_TOLERANCE,
            "D_trace_ceiling": SIZE_STABILITY_RELATIVE_TOLERANCE,
            "eligibility": (
                "both rows active above their floors and technical, both six-source CVs<=0.10, "
                "zero boundary-reflection input, and no refit"
            ),
            "matched_source_weight_diagnostic": (
                "q_e=sin^2(0.02 M_plus(-4pi/9)) is identical on L15/L19; "
                "Rbar/q_e adds no geometry correction"
            ),
            "no_refit": True,
        },
        "causal_anchor_controls": {
            "incoming_neighbor_collision": "update source_radius",
            "center_collision": "update source_radius+1",
            "sample": "after complete word on that same update",
        },
    }


def occupation_species_contract() -> dict:
    return {
        "primary": "matter-CAR-direction-occupation",
        "primary_surface": "after-complete-update-word",
        "mediator": "separate-hard-core-qubit-occupation-ledger",
        "cross_species_substitution_forbidden": True,
    }


def radial_path(source: tuple[int, int, int], direction: int, radius: int) -> tuple[tuple[int, int, int], ...]:
    step = c210.DIRECTIONS[direction]
    return tuple(
        tuple(int(source[axis] + distance * step[axis]) for axis in range(3))
        for distance in range(1, radius + 1)
    )


def oriented_bond_domain_controls(geometry: c509.BulkGeometry) -> dict:
    side = geometry.side
    center = np.asarray(geometry.probe_center, dtype=int)
    domain = {
        ((x, y, z), direction)
        for x in range(side)
        for y in range(side)
        for z in range(side)
        for direction in range(6)
        if all(
            0 <= (x, y, z)[axis] - int(c210.DIRECTIONS[direction, axis]) < side
            for axis in range(3)
        )
    }
    redundancy_failures = 0
    for cell, direction in domain:
        predecessor = tuple(
            int(cell[axis] - c210.DIRECTIONS[direction, axis]) for axis in range(3)
        )
        partner = (predecessor, REVERSE[direction])
        redundancy_failures += partner not in domain
        if partner in domain:
            partner_predecessor = tuple(
                int(predecessor[axis] - c210.DIRECTIONS[REVERSE[direction], axis])
                for axis in range(3)
            )
            redundancy_failures += partner_predecessor != cell

    frame_failures = 0
    for frame in c210.proper_cubic_frames():
        mapping = direction_map(frame)
        for cell, direction in domain:
            moved_cell = tuple(
                int(value)
                for value in center + frame @ (np.asarray(cell, dtype=int) - center)
            )
            frame_failures += (moved_cell, mapping[direction]) not in domain

    center_anchor_failures = sum(
        (geometry.probe_center, direction) not in domain for direction in range(6)
    )
    radial_path_failures = sum(
        (cell, direction) not in domain
        for source, direction in zip(geometry.source_cells, geometry.inward_directions)
        for cell in radial_path(source, direction, geometry.source_radius)
    )
    return {
        "geometry": geometry.name,
        "side": side,
        "oriented_bond_count": len(domain),
        "expected_oriented_bond_count": 6 * side * side * (side - 1),
        "proper_cubic_domain_failures": frame_failures,
        "redundancy_partner_failures": redundancy_failures,
        "center_anchor_domain_failures": center_anchor_failures,
        "radial_path_domain_failures": radial_path_failures,
        "zero_extension_used": False,
    }


def finite_stream_mode(
    cell: tuple[int, int, int], direction: int, side: int
) -> tuple[tuple[int, int, int], int]:
    """Forward J S_face hard-wall moving shift for one direction mode."""
    target = tuple(
        int(cell[axis] + c210.DIRECTIONS[direction, axis]) for axis in range(3)
    )
    if any(value < 0 or value >= side for value in target):
        return cell, REVERSE[direction]
    return target, direction


def outward_boundary_mode(
    cell: tuple[int, int, int], direction: int, side: int
) -> bool:
    target = tuple(
        int(cell[axis] + c210.DIRECTIONS[direction, axis]) for axis in range(3)
    )
    return any(value < 0 or value >= side for value in target)


def finite_inverse_stream_mode(
    cell: tuple[int, int, int], direction: int, side: int
) -> tuple[tuple[int, int, int], int]:
    """Inverse S_face J: reverse onsite first, then apply the face permutation."""
    reversed_direction = REVERSE[direction]
    target = tuple(
        int(cell[axis] + c210.DIRECTIONS[reversed_direction, axis])
        for axis in range(3)
    )
    if any(value < 0 or value >= side for value in target):
        return cell, reversed_direction
    return target, direction


def matter_mode_support(
    center: tuple[int, int, int], side: int, depth: int
) -> tuple[
    tuple[set[tuple[tuple[int, int, int], int]], ...],
    tuple[int, ...],
]:
    initial_cells = {center}
    initial_cells.update(
        tuple(int(center[axis] + direction[axis]) for axis in range(3))
        for direction in c210.DIRECTIONS
    )
    current = {(cell, direction) for cell in initial_cells for direction in range(6)}
    rows = [set(current)]
    reflection_inputs = [
        sum(outward_boundary_mode(cell, direction, side) for cell, direction in current)
    ]
    for _update in range(depth):
        occupied_cells = {cell for cell, _direction in current}
        after_coin = {(cell, direction) for cell in occupied_cells for direction in range(6)}
        reflection_inputs.append(
            sum(
                outward_boundary_mode(cell, direction, side)
                for cell, direction in after_coin
            )
        )
        current = {
            finite_stream_mode(cell, direction, side)
            for cell, direction in after_coin
        }
        rows.append(set(current))
    return tuple(rows), tuple(reflection_inputs)


def mediator_support(
    geometry: c509.BulkGeometry, deletion: str
) -> tuple[
    tuple[set[tuple[tuple[int, int, int], int]], ...],
    tuple[int, ...],
]:
    active: set[tuple[tuple[int, int, int], int]] = set()
    matter_modes, _matter_reflection = matter_mode_support(
        geometry.probe_center, geometry.side, geometry.depth
    )
    matter = tuple({cell for cell, _direction in row} for row in matter_modes)
    rows = [set(active)]
    reflection_inputs = [0]
    for update in range(1, geometry.depth + 1):
        if deletion != "emitter":
            active.update(zip(geometry.source_cells, geometry.inward_directions))
        if deletion != "collision":
            for cell, direction in tuple(active):
                if cell in matter[update]:
                    active.add((cell, REVERSE[direction]))
        reflection_inputs.append(
            sum(
                outward_boundary_mode(cell, direction, geometry.side)
                for cell, direction in active
            )
            if deletion != "mediator-stream"
            else 0
        )
        if deletion != "mediator-stream":
            active = {
                finite_stream_mode(cell, direction, geometry.side)
                for cell, direction in active
            }
        rows.append(set(active))
    return tuple(rows), tuple(reflection_inputs)


def boolean_overlap_controls(geometry: c509.BulkGeometry) -> dict:
    """Compute conservative marginal overlap/timing; no amplitude claim."""
    matter_modes, _reflection = matter_mode_support(
        geometry.probe_center, geometry.side, geometry.depth
    )
    matter_cells = tuple({cell for cell, _direction in row} for row in matter_modes)
    active: set[Mode] = set()
    overlap_cells = []
    center_pre_collision = []
    center_postword = []
    for update in range(1, geometry.depth + 1):
        active.update(zip(geometry.source_cells, geometry.inward_directions))
        overlapping = {
            cell for cell, _direction in active if cell in matter_cells[update]
        }
        overlap_cells.append(len(overlapping))
        center_pre_collision.append(
            sum(cell == geometry.probe_center for cell, _direction in active)
        )
        for cell, direction in tuple(active):
            if cell in matter_cells[update]:
                active.add((cell, REVERSE[direction]))
        active = {
            finite_stream_mode(cell, direction, geometry.side)
            for cell, direction in active
        }
        center_postword.append(
            sum(cell == geometry.probe_center for cell, _direction in active)
        )

    source_cells = set(geometry.source_cells)
    no_stream_source_overlap = tuple(
        len(source_cells & matter_cells[update])
        for update in range(1, geometry.depth + 1)
    )
    return {
        "geometry": geometry.name,
        "scope": "conservative-marginal-Boolean-support-not-amplitude",
        "active_mediator_matter_overlap_cells_by_update": tuple(overlap_cells),
        "center_mediator_pre_collision_modes_by_update": tuple(center_pre_collision),
        "center_mediator_postword_modes_by_update": tuple(center_postword),
        "no_stream_source_overlap_cells_by_update": no_stream_source_overlap,
        "first_any_collision_update": next(
            index + 1 for index, value in enumerate(overlap_cells) if value
        ),
        "first_center_arrival_postword_update": next(
            index + 1 for index, value in enumerate(center_postword) if value
        ),
        "first_center_collision_update": next(
            index + 1 for index, value in enumerate(center_pre_collision) if value
        ),
    }


def boundary_counts(geometry: c509.BulkGeometry, deletion: str) -> dict:
    matter, matter_reflection_inputs = matter_mode_support(
        geometry.probe_center, geometry.side, geometry.depth
    )
    mediator, mediator_reflection_inputs = mediator_support(geometry, deletion)
    outside = 0
    shell_by_update = []
    for modes in matter:
        shell_modes = 0
        for cell, _direction in modes:
            outside += any(value < 0 or value >= geometry.side for value in cell)
            shell_modes += all(0 <= value < geometry.side for value in cell) and any(
                value in (0, geometry.side - 1) for value in cell
            )
        shell_by_update.append(shell_modes)
    mediator_shell_by_update = []
    for row in mediator:
        shell_modes = 0
        for cell, _direction in row:
            outside += any(value < 0 or value >= geometry.side for value in cell)
            shell_modes += all(0 <= value < geometry.side for value in cell) and any(
                value in (0, geometry.side - 1) for value in cell
            )
        mediator_shell_by_update.append(shell_modes)
    return {
        "geometry": geometry.name,
        "deletion": deletion,
        "support_scope": "conservative-marginal-Boolean-upper-bound",
        "structural_outside_count": outside,
        "matter_shell_modes_by_update": tuple(shell_by_update),
        "mediator_shell_modes_by_update": tuple(mediator_shell_by_update),
        "matter_reflect_input_modes_by_update": matter_reflection_inputs,
        "mediator_reflect_input_modes_by_update": mediator_reflection_inputs,
        "matter_final_modes": len(matter[-1]),
        "mediator_final_modes": len(mediator[-1]),
    }


def finite_stream_controls(side: int) -> dict:
    center = np.asarray(((side - 1) // 2,) * 3)
    modes = tuple(
        ((x, y, z), direction)
        for x in range(side)
        for y in range(side)
        for z in range(side)
        for direction in range(6)
    )
    outputs = tuple(
        finite_stream_mode(cell, direction, side) for cell, direction in modes
    )
    inverse_failures = sum(
        finite_inverse_stream_mode(*finite_stream_mode(cell, direction, side), side)
        != (cell, direction)
        for cell, direction in modes
    )
    covariance_failures = 0
    for frame in c210.proper_cubic_frames():
        mapping = direction_map(frame)
        for cell, direction in modes:
            moved_cell = tuple(
                int(value) for value in center + frame @ (np.asarray(cell) - center)
            )
            left_cell, left_direction = finite_stream_mode(
                moved_cell, mapping[direction], side
            )
            streamed_cell, streamed_direction = finite_stream_mode(
                cell, direction, side
            )
            right_cell = tuple(
                int(value)
                for value in center + frame @ (np.asarray(streamed_cell) - center)
            )
            covariance_failures += (left_cell, left_direction) != (
                right_cell,
                mapping[streamed_direction],
            )
    return {
        "side": side,
        "cells": side**3,
        "direction_modes": 6 * side**3,
        "mediator_modes_including_parked": 7 * side**3,
        "parked_fixed_modes": side**3,
        "internal_face_SWAP_or_FSWAP_pairs": 3 * side**2 * (side - 1),
        "outward_boundary_rails": 6 * side**2,
        "output_duplicate_count": len(outputs) - len(set(outputs)),
        "shell_cells": side**3 - (side - 2) ** 3,
        "onsite_J_pairs": 3 * side**3,
        "inverse_failures": inverse_failures,
        "all24_covariance_failures": covariance_failures,
    }


def geometry_controls(geometry: c509.BulkGeometry) -> dict:
    center = np.asarray(geometry.probe_center)
    pairs = tuple(zip(geometry.source_cells, geometry.inward_directions))
    failures = 0
    path_failures = 0
    for frame in c210.proper_cubic_frames():
        mapping = direction_map(frame)
        moved_pairs = {
            (
                tuple(int(value) for value in center + frame @ (np.asarray(source) - center)),
                mapping[direction],
            )
            for source, direction in pairs
        }
        failures += moved_pairs != set(pairs)
        for source, direction in pairs:
            moved_source = tuple(
                int(value) for value in center + frame @ (np.asarray(source) - center)
            )
            moved_direction = mapping[direction]
            moved_path = tuple(
                tuple(int(value) for value in center + frame @ (np.asarray(cell) - center))
                for cell in radial_path(source, direction, geometry.source_radius)
            )
            path_failures += moved_path != radial_path(
                moved_source, moved_direction, geometry.source_radius
            )
    inward_failures = sum(
        radial_path(source, direction, geometry.source_radius)[-1]
        != geometry.probe_center
        for source, direction in pairs
    )
    return {
        "geometry": geometry.name,
        "all24_pair_orbit_failures": failures,
        "all24_radial_path_failures": path_failures,
        "inward_center_endpoint_failures": inward_failures,
    }


def contract_hashes() -> dict:
    contracts = {
        "packet": packet_contract(),
        "update": update_contract(),
        "free": free_contract(),
        "deletion": deletion_contract(),
        "boundary": boundary_contract(),
        "observable": observable_contract(),
        "occupation_species": occupation_species_contract(),
        "preservation": preservation_contract(),
        "authorization": authorization_contract(),
    }
    return {name: canonical_sha(value) for name, value in contracts.items()}


def predecessor_identity(row: dict) -> dict:
    return {
        key: row[key]
        for key in (
            "disposition", "role", "route", "source_beta", "probe_beta",
            "geometry", "deletion",
        )
    }


def route_c_row(
    role: str,
    deletion: str,
    geometry: c509.BulkGeometry,
    beta: str,
    predecessor: dict | None,
    matched_train_revision4_row_sha256: str | None = None,
) -> dict:
    hashes = contract_hashes()
    return {
        "contract_revision": "Cycle511-RouteC-Revision4",
        "revision": REVISION,
        "disposition": "train" if not geometry.held else "blind-held",
        "role": role,
        "route": ROUTE_C,
        "source_beta": beta,
        "probe_beta": beta,
        "geometry": revision_geometry(geometry),
        "matter_packet": PACKET_NAME,
        "exact_packet": {
            "matter": packet_contract(),
            "mediator": {
                "state": "product computational basis state",
                "occupied_parked_sources": tuple(geometry.source_cells),
                "source_inward_direction_pairs": tuple(
                    zip(geometry.source_cells, geometry.inward_directions)
                ),
                "directional_rails": "all blank",
                "all_other_mediator_M2": "blank",
                "global_charge": 6,
            },
        },
        "matter_packet_sha256": hashes["packet"],
        "mediator_statistics": STATISTICS_LAW,
        "mediator_initial_state": "one parked occupation at each of six octahedral sources; global Q=6",
        "update_contract_sha256": hashes["update"],
        "free_contract_sha256": hashes["free"],
        "deletion_contract_sha256": hashes["deletion"],
        "boundary_contract_sha256": hashes["boundary"],
        "observable_contract_sha256": hashes["observable"],
        "occupation_species_contract_sha256": hashes["occupation_species"],
        "preservation_contract_sha256": hashes["preservation"],
        "authorization_contract_sha256": hashes["authorization"],
        "primary_occupation_species": "matter-CAR-direction-occupation",
        "mediator_occupation_role": "separate-source-transport-boundary-ledger",
        "deletion": deletion,
        "deletion_applies_symmetrically_to": "interacting-and-matched-free",
        "free_partner": True,
        "repeat_free": True,
        "authorization_required": True,
        "supersedes_cycle509_row_sha256": (
            canonical_sha(predecessor) if predecessor is not None else None
        ),
        "cycle509_predecessor_identity": (
            predecessor_identity(predecessor) if predecessor is not None else None
        ),
        "matched_train_revision4_row_sha256": matched_train_revision4_row_sha256,
        "row_selector": False,
        "refit": False,
        "execution_status": "frozen-unexecuted",
    }


def manifests() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    c509_train, c509_held = c509.row_manifests()
    ab34 = c509_train[:34]
    ab_held10 = c509_held[:10]
    old_route_c8 = c509_train[34:]
    route_c8 = []
    for index, old_row in enumerate(old_route_c8):
        route_c8.append(
            route_c_row(
                (
                    "implementation-resource-scout-sentinel-and-intact-train-baseline"
                    if index == 0 else "route-c-train-deletion"
                ),
                old_row["deletion"],
                c509.ROUTE_C_TRAIN,
                MIDDLE_BETA,
                old_row,
            )
        )
    old_route_c_held = c509_held[10:12]
    route_c_held = [
        route_c_row(
            "blind-held-zero-source-size-null", "none", c509.ROUTE_C_HELD,
            "0", old_route_c_held[0],
        ),
        route_c_row(
            "blind-held-mass-volume-control", "none", c509.ROUTE_C_HELD,
            HELD_ALIAS_BETA, old_route_c_held[1],
        ),
        route_c_row(
            "blind-held-matched-beta-size-control",
            "none",
            ROUTE_C_MATCHED_SIZE_HELD,
            MIDDLE_BETA,
            None,
            canonical_sha(route_c8[0]),
        ),
    ]
    held13 = list(ab_held10) + route_c_held
    return ab34, ab_held10, route_c8, held13


def evidence_controls() -> dict:
    actual_hashes = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_HASHES}
    hash_failures = {
        str(path.relative_to(ROOT)): {"expected": expected, "actual": actual_hashes[str(path.relative_to(ROOT))]}
        for path, expected in STRICT_HASHES.items()
        if actual_hashes[str(path.relative_to(ROOT))] != expected
    }
    c509_receipt = load_json(C509_RECEIPT)
    c509_result = load_json(C509_RESULT)
    c510_receipt = load_json(C510_RECEIPT)
    c510_log = load_json(C510_LOG)
    return {
        "strict_file_hashes": actual_hashes,
        "strict_hash_failures": hash_failures,
        "Cycle509": {
            "authority": c509_result["authority"],
            "audit": c509_result["audit"],
            "verdict": c509_result["verdict"],
            "AB_rows": c509_result["counts"]["route_A_rows"] + c509_result["counts"]["route_B_rows"],
            "RouteC_rows_executed": c509_result["counts"]["route_C_rows"],
            "RouteC_manifest_rows_open": c509_result["counts"]["route_C_open_manifest_rows"],
            "held_rows_executed": c509_result["counts"]["held_rows"],
            "atomic_34_pass": c509_receipt["atomic_34_row_audit_pass"],
            "science_runner_sha256": c509_receipt["science_runner_sha256"],
            "science_result_sha256": c509_receipt["science_result_sha256"],
            "artifact_index_sha256": c509_receipt["artifact_index_sha256"],
            "dependency_bundle_sha256": c509_receipt["dependency_bundle_sha256"],
        },
        "Cycle510": {
            "authority": c510_log["authority"],
            "audit": c510_log["audit"],
            "status": c510_log["status"],
            "tests": (c510_log["tests_passed"], c510_log["tests_total"]),
            "response_rows": c510_log["resources"]["response_rows"],
            "held_rows": c510_log["resources"]["held_rows"],
            "runner_sha256": c510_receipt["runner_sha256"],
            "result_transcript_sha256": c510_receipt["result_transcript_sha256"],
            "statistics": c510_log["statistics_discriminator"]["supplied_candidate_statistics"],
            "global_multi_edge_intertwiner_claim": c510_log["physical_inventory"]["global_multi_edge_intertwiner_claim"],
        },
    }


def main() -> int:
    present = tuple(name for name in AUTHORIZATION_VARIABLES if name in os.environ)
    check("dry preflight has no execution authorization variable", not present, present)

    evidence = evidence_controls()
    check("strict Cycle509/Cycle510 evidence hashes", not evidence["strict_hash_failures"], evidence["strict_hash_failures"])
    c509_evidence = evidence["Cycle509"]
    check(
        "immutable Cycle509 A/B failed-gate evidence bound without promotion",
        c509_evidence["authority"] == "none"
        and c509_evidence["audit"] == "unset"
        and c509_evidence["verdict"] == "science-train-complete-with-failed-gates"
        and c509_evidence["AB_rows"] == 34
        and c509_evidence["RouteC_rows_executed"] == 0
        and c509_evidence["RouteC_manifest_rows_open"] == 8
        and c509_evidence["held_rows_executed"] == 0
        and c509_evidence["atomic_34_pass"] is False,
        c509_evidence,
    )
    c510_evidence = evidence["Cycle510"]
    check(
        "Cycle510 local certificate bound at exact scope",
        c510_evidence["authority"] == "none"
        and c510_evidence["audit"] == "unset"
        and c510_evidence["status"] == "local-pre-response-certificate"
        and c510_evidence["tests"] == (18, 18)
        and c510_evidence["response_rows"] == 0
        and c510_evidence["held_rows"] == 0
        and c510_evidence["statistics"] == STATISTICS_LAW
        and c510_evidence["global_multi_edge_intertwiner_claim"] is False,
        c510_evidence,
    )

    c509_train, c509_held = c509.row_manifests()
    ab34, ab_held10, route_c8, held13 = manifests()
    check(
        "Cycle509 manifests and immutable A/B subsets exact",
        canonical_sha(c509_train) == EXPECTED_C509_FULL_TRAIN_SHA256
        and canonical_sha(c509_held) == EXPECTED_C509_FULL_HELD_SHA256
        and canonical_sha(ab34) == EXPECTED_C509_AB34_SHA256
        and canonical_sha(ab_held10) == EXPECTED_C509_AB_HELD10_SHA256,
        {
            "full_train": canonical_sha(c509_train),
            "full_held": canonical_sha(c509_held),
            "AB34": canonical_sha(ab34),
            "AB_held10": canonical_sha(ab_held10),
        },
    )
    old_route_c_train_hashes = tuple(canonical_sha(row) for row in c509_train[34:])
    old_route_c_held_hashes = tuple(canonical_sha(row) for row in c509_held[10:12])
    check(
        "Cycle509 Route-C predecessor rows are individually bound before supersession",
        old_route_c_train_hashes == EXPECTED_C509_ROUTE_C_TRAIN_ROW_SHA256
        and old_route_c_held_hashes == EXPECTED_C509_ROUTE_C_HELD_ROW_SHA256,
        {
            "train": old_route_c_train_hashes,
            "held": old_route_c_held_hashes,
        },
    )

    components = tuple(packet_component(axis) for axis in range(3))
    overlap = np.asarray([[ray_inner(left, right) for right in components] for left in components])
    packet_frame_residual = 0.0
    packet_frame_failures = 0
    for frame in c210.proper_cubic_frames():
        targets = []
        for component in components:
            moved = transform_ray(component, frame)
            matches = [abs(ray_inner(target, moved)) for target in components]
            target = int(np.argmax(matches))
            targets.append(target)
            packet_frame_residual = max(packet_frame_residual, abs(matches[target] - 1))
            packet_frame_failures += sum(value > NUMERIC_TOLERANCE for value in matches) != 1
        packet_frame_failures += sorted(targets) != [0, 1, 2]
    packet_numeric = packet_numeric_controls(components)
    expected_collision_weights = (5 / 108, 2 / 27, 5 / 108)
    check(
        "rho_AB3 is normalized rank-three equal mixture and all24 projector orbit",
        np.linalg.norm(overlap - np.eye(3)) < NUMERIC_TOLERANCE
        and packet_frame_residual < NUMERIC_TOLERANCE
        and packet_frame_failures == 0
        and packet_numeric["component_nonzero_counts"] == (9, 9, 9)
        and packet_numeric["one_particle_mode_count"] == 18
        and packet_numeric["support_cell_count"] == 7
        and packet_numeric["ambient_union_wedge_dimension"] == 153
        and packet_numeric["density_trace_residual"] < NUMERIC_TOLERANCE
        and packet_numeric["density_Hermiticity_residual"] < NUMERIC_TOLERANCE
        and packet_numeric["density_rank"] == 3
        and abs(packet_numeric["density_purity"] - 1 / 3) < NUMERIC_TOLERANCE
        and max(
            abs(left - right)
            for left, right in zip(
                packet_numeric["collision_active_weights_neighbor_center_neighbor"],
                expected_collision_weights,
            )
        ) < NUMERIC_TOLERANCE
        and abs(packet_numeric["mixed_contact_weight"] - 1 / 2) < NUMERIC_TOLERANCE,
        {
            "component_Gram_residual": float(np.linalg.norm(overlap - np.eye(3))),
            "maximum_projector_orbit_residual": float(packet_frame_residual),
            "frame_failures": packet_frame_failures,
            **packet_numeric,
        },
    )

    hashes = contract_hashes()
    expected_hashes = {
        "packet": EXPECTED_PACKET_SHA256,
        "update": EXPECTED_UPDATE_SHA256,
        "free": EXPECTED_FREE_SHA256,
        "deletion": EXPECTED_DELETION_SHA256,
        "boundary": EXPECTED_BOUNDARY_SHA256,
        "observable": EXPECTED_OBSERVABLE_SHA256,
        "occupation_species": EXPECTED_OCCUPATION_SPECIES_SHA256,
        "preservation": EXPECTED_PRESERVATION_SHA256,
        "authorization": EXPECTED_AUTHORIZATION_SHA256,
    }
    check("revision-4 law-level contract hashes frozen", hashes == expected_hashes, {"actual": hashes, "expected": expected_hashes})

    factor_coordinates = factor_coordinate_controls()
    middle_factor = factor_coordinates["train_and_matched_size_beta_-4pi_over_9"]
    zero_factor = factor_coordinates["held_beta_zero"]
    alias_factor = factor_coordinates["held_beta_-8pi_over_9"]
    check(
        "operator-first source/probe factors, angles, and exact held null are frozen",
        abs(middle_factor["M_plus"] - (-3 * np.tan((-4 * np.pi / 9) / 2)))
        < c509.RUNNER_TOLERANCE
        and zero_factor["M_plus"] == 0.0
        and zero_factor["emitter_and_collision_angle"] == 0.0
        and zero_factor["per_source_update1_emitted_weight"] == 0.0
        and alias_factor["emitter_and_collision_angle"] < factor_coordinates["angle_ceiling"]
        and alias_factor["principal_mass_or_inertia_claim"] is False,
        factor_coordinates,
    )

    geometry_rows = tuple(
        geometry_controls(geometry)
        for geometry in (
            c509.ROUTE_C_TRAIN,
            c509.ROUTE_C_HELD,
            ROUTE_C_MATCHED_SIZE_HELD,
        )
    )
    check(
        "train and held paired source-direction paths are exhaustive all24 inward orbits",
        all(
            row["all24_pair_orbit_failures"] == 0
            and row["all24_radial_path_failures"] == 0
            and row["inward_center_endpoint_failures"] == 0
            for row in geometry_rows
        ),
        geometry_rows,
    )

    observable_domain_rows = tuple(
        oriented_bond_domain_controls(geometry)
        for geometry in (
            c509.ROUTE_C_TRAIN,
            c509.ROUTE_C_HELD,
            ROUTE_C_MATCHED_SIZE_HELD,
        )
    )
    check(
        "finite oriented-bond observable domain is exact, all24 invariant, and contains every anchor",
        tuple(row["oriented_bond_count"] for row in observable_domain_rows)
        == (18900, 38988, 38988)
        and all(
            row["oriented_bond_count"] == row["expected_oriented_bond_count"]
            and row["proper_cubic_domain_failures"] == 0
            and row["redundancy_partner_failures"] == 0
            and row["center_anchor_domain_failures"] == 0
            and row["radial_path_domain_failures"] == 0
            and row["zero_extension_used"] is False
            for row in observable_domain_rows
        ),
        observable_domain_rows,
    )

    finite_stream_rows = tuple(
        finite_stream_controls(side) for side in (c509.ROUTE_C_TRAIN.side, c509.ROUTE_C_HELD.side)
    )
    check(
        "finite hard-wall J-S_face stream is invertible, all24 covariant, and exactly inventoried",
        finite_stream_rows
        == (
            {
                "side": 15,
                "cells": 3375,
                "direction_modes": 20250,
                "mediator_modes_including_parked": 23625,
                "parked_fixed_modes": 3375,
                "internal_face_SWAP_or_FSWAP_pairs": 9450,
                "outward_boundary_rails": 1350,
                "output_duplicate_count": 0,
                "shell_cells": 1178,
                "onsite_J_pairs": 10125,
                "inverse_failures": 0,
                "all24_covariance_failures": 0,
            },
            {
                "side": 19,
                "cells": 6859,
                "direction_modes": 41154,
                "mediator_modes_including_parked": 48013,
                "parked_fixed_modes": 6859,
                "internal_face_SWAP_or_FSWAP_pairs": 19494,
                "outward_boundary_rails": 2166,
                "output_duplicate_count": 0,
                "shell_cells": 1946,
                "onsite_J_pairs": 20577,
                "inverse_failures": 0,
                "all24_covariance_failures": 0,
            },
        ),
        finite_stream_rows,
    )

    boundary_rows = tuple(
        boundary_counts(geometry, deletion)
        for geometry in (
            c509.ROUTE_C_TRAIN,
            c509.ROUTE_C_HELD,
            ROUTE_C_MATCHED_SIZE_HELD,
        )
        for deletion in ("none",) + DELETIONS
    )
    check(
        "finite hard-wall structural outside leakage is zero for every deletion",
        all(
            row["structural_outside_count"] == 0
            for row in boundary_rows
        ),
        boundary_rows,
    )
    check(
        "boundary-shell occupation is separately frozen for train and held cones",
        canonical_sha(boundary_rows) == EXPECTED_BOUNDARY_CONTROLS_SHA256,
        {
            "sha256": canonical_sha(boundary_rows),
            "maximum_matter_shell_modes": max(
                max(row["matter_shell_modes_by_update"]) for row in boundary_rows
            ),
            "maximum_mediator_shell_modes": max(
                max(row["mediator_shell_modes_by_update"]) for row in boundary_rows
            ),
        },
    )
    check(
        "pre-S_face outward boundary reflection input is structurally absent through every sample window",
        all(
            max(row["matter_reflect_input_modes_by_update"]) == 0
            and max(row["mediator_reflect_input_modes_by_update"]) == 0
            for row in boundary_rows
        ),
        {
            "maximum_matter_Q_reflect_input_structural_modes": max(
                max(row["matter_reflect_input_modes_by_update"])
                for row in boundary_rows
            ),
            "maximum_mediator_Q_reflect_input_structural_modes": max(
                max(row["mediator_reflect_input_modes_by_update"])
                for row in boundary_rows
            ),
            "future_numerical_Q_reflect_input_ceiling": 1e-12,
            "shell_occupation_is_leakage": False,
        },
    )

    timing_rows = tuple(
        {
            "geometry": geometry.name,
            "incoming_neighbor_collision_update": geometry.source_radius,
            "center_collision_update": geometry.source_radius + 1,
            "response_window": geometry.response_window,
            "center_update_is_last_window_update": geometry.response_window[-1]
            == geometry.source_radius + 1,
            "post_complete_word_same_update_visibility": True,
        }
        for geometry in (
            c509.ROUTE_C_TRAIN,
            c509.ROUTE_C_HELD,
            ROUTE_C_MATCHED_SIZE_HELD,
        )
    )
    check(
        "incoming-neighbor and center collision timing is frozen inside both response windows",
        all(
            row["incoming_neighbor_collision_update"] in row["response_window"]
            and row["center_collision_update"] in row["response_window"]
            and row["center_update_is_last_window_update"]
            and row["post_complete_word_same_update_visibility"]
            for row in timing_rows
        ),
        timing_rows,
    )

    overlap_rows = tuple(
        boolean_overlap_controls(geometry)
        for geometry in (
            c509.ROUTE_C_TRAIN,
            c509.ROUTE_C_HELD,
            ROUTE_C_MATCHED_SIZE_HELD,
        )
    )
    check(
        "computed conservative Boolean overlap, arrival, center-collision, and no-stream source-tail oracles",
        overlap_rows[0]["first_any_collision_update"] == 2
        and overlap_rows[0]["first_center_arrival_postword_update"] == 4
        and overlap_rows[0]["first_center_collision_update"] == 5
        and overlap_rows[0]["no_stream_source_overlap_cells_by_update"]
        == (0, 0, 6, 6, 6)
        and overlap_rows[1]["first_any_collision_update"] == 3
        and overlap_rows[1]["first_center_arrival_postword_update"] == 5
        and overlap_rows[1]["first_center_collision_update"] == 6
        and overlap_rows[1]["no_stream_source_overlap_cells_by_update"]
        == (0, 0, 0, 6, 6, 6)
        and overlap_rows[2]["first_any_collision_update"] == 2
        and overlap_rows[2]["first_center_arrival_postword_update"] == 4
        and overlap_rows[2]["first_center_collision_update"] == 5
        and overlap_rows[2]["no_stream_source_overlap_cells_by_update"]
        == (0, 0, 6, 6, 6),
        overlap_rows,
    )

    route_c8_sha = canonical_sha(route_c8)
    held13_sha = canonical_sha(held13)
    train_deletions = tuple(row["deletion"] for row in route_c8)
    check(
        "RouteC8 is one intact sentinel/baseline plus the seven ordered deletions",
        len(route_c8) == 8
        and train_deletions == ("none",) + DELETIONS
        and all(row["source_beta"] == MIDDLE_BETA and row["probe_beta"] == MIDDLE_BETA for row in route_c8)
        and all(row["geometry"] == revision_geometry(c509.ROUTE_C_TRAIN) for row in route_c8)
        and all(row["execution_status"] == "frozen-unexecuted" for row in route_c8)
        and tuple(row["supersedes_cycle509_row_sha256"] for row in route_c8)
        == EXPECTED_C509_ROUTE_C_TRAIN_ROW_SHA256
        and all(row["exact_packet"]["matter"] == packet_contract() for row in route_c8)
        and route_c8_sha == EXPECTED_ROUTE_C8_SHA256,
        {"sha256": route_c8_sha, "deletions": train_deletions},
    )
    new_held = held13[-3:]
    check(
        "atomic held13 preserves A/B held10 and adds zero, alias, matched-beta L19 rows",
        len(held13) == 13
        and canonical_sha(held13[:10]) == EXPECTED_C509_AB_HELD10_SHA256
        and tuple(row["source_beta"] for row in new_held) == ("0", HELD_ALIAS_BETA, MIDDLE_BETA)
        and tuple(row["probe_beta"] for row in new_held) == ("0", HELD_ALIAS_BETA, MIDDLE_BETA)
        and new_held[-1]["role"] == "blind-held-matched-beta-size-control"
        and all(row["geometry"] == revision_geometry(c509.ROUTE_C_HELD) for row in new_held[:2])
        and new_held[-1]["geometry"] == revision_geometry(ROUTE_C_MATCHED_SIZE_HELD)
        and all(row["execution_status"] == "frozen-unexecuted" for row in new_held)
        and tuple(row["supersedes_cycle509_row_sha256"] for row in new_held[:2])
        == EXPECTED_C509_ROUTE_C_HELD_ROW_SHA256
        and new_held[-1]["supersedes_cycle509_row_sha256"] is None
        and new_held[-1]["matched_train_revision4_row_sha256"]
        == canonical_sha(route_c8[0])
        and held13_sha == EXPECTED_ATOMIC_HELD13_SHA256,
        {"sha256": held13_sha, "roles": tuple(row["role"] for row in new_held)},
    )

    combined_train = list(ab34) + route_c8
    held_limit_partition = {
        label: sum(c509.held_limit_classification(row) == label for row in held13)
        for label in {
            "zero-source-no-emission-null-response",
            "positive-source-zero-probe-active-source-null-transfer",
            "positive-positive-transfer-scaling-test",
        }
    }
    check(
        "combined train42 and held13 are disjoint, selector-free, and no-refit",
        len(combined_train) == 42
        and len(held13) == 13
        and not set(map(canonical_sha, combined_train)) & set(map(canonical_sha, held13))
        and all(not row.get("row_selector", False) and not row.get("refit", False) for row in combined_train + held13)
        and held_limit_partition == {
            "zero-source-no-emission-null-response": 5,
            "positive-source-zero-probe-active-source-null-transfer": 2,
            "positive-positive-transfer-scaling-test": 6,
        },
        {
            "train": len(combined_train),
            "held": len(held13),
            "held_exact_limit_partition": held_limit_partition,
        },
    )

    execution = {
        "preflight_mode": MODE,
        "response_rows_executed": 0,
        "held_rows_executed": 0,
        "resource_scout_executed": False,
        "held_evaluator_present": False,
        "RouteC8_execution_requires_fresh_authorization": True,
        "authorization_contract_sha256": hashes["authorization"],
        "atomic_held13_rule": "all thirteen rows in one fail-closed invocation; no selector; only after A/B/C train disposition",
        "refit_performed": False,
    }
    check(
        "preflight executes zero response, held, and scout rows",
        execution["response_rows_executed"] == 0
        and execution["held_rows_executed"] == 0
        and execution["resource_scout_executed"] is False
        and execution["refit_performed"] is False,
        execution,
    )

    passed = all(row["passed"] for row in TESTS)
    output = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "status": "response-revision4-contract-frozen" if passed else "preflight-failed",
        "pass": passed,
        "tests_passed": sum(row["passed"] for row in TESTS),
        "tests_total": len(TESTS),
        "tests": TESTS,
        "bound_evidence": evidence,
        "contracts": {
            "packet": packet_contract(),
            "update": update_contract(),
            "free": free_contract(),
            "deletion": deletion_contract(),
            "boundary": boundary_contract(),
            "observable": observable_contract(),
            "occupation_species": occupation_species_contract(),
            "preservation": preservation_contract(),
            "authorization": authorization_contract(),
            "hashes": hashes,
        },
        "packet_numeric_controls": packet_numeric,
        "geometry_controls": geometry_rows,
        "observable_domain_controls": observable_domain_rows,
        "finite_stream_controls": finite_stream_rows,
        "boundary_controls": boundary_rows,
        "causal_timing_controls": timing_rows,
        "Boolean_overlap_controls": overlap_rows,
        "manifests": {
            "immutable_AB34_sha256": canonical_sha(ab34),
            "immutable_AB_held10_sha256": canonical_sha(ab_held10),
            "RouteC8_sha256": route_c8_sha,
            "atomic_held13_sha256": held13_sha,
            "combined_train42_sha256": canonical_sha(combined_train),
            "RouteC8": route_c8,
            "atomic_held13": held13,
            "held_exact_limit_partition": held_limit_partition,
        },
        "execution": execution,
        "supplied_not_derived": (
            "rho_AB3 mixed preparation and equal one-third weights",
            "ordinary-SWAP hard-core mediator statistics",
            "all coefficients, mass factors, update order, boundary law, observable, thresholds, and rows",
        ),
        "open_after_preflight": (
            "resource feasibility and sparse global-Q6 evaluator",
            "autonomous packet/source preparation and global physical-M2 compiler",
            "finite-amplitude boundary/reflection ledger, response, deletion distances, size stability, and held performance",
            "time, energy, stress, source, gravity, probability, Records, and realized history",
        ),
    }
    print(
        json.dumps(
            output,
            sort_keys=True,
            separators=(",", ":"),
            default=json_default,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", nargs="?", default=MODE, choices=(MODE,))
    parser.parse_args()
    raise SystemExit(main())
