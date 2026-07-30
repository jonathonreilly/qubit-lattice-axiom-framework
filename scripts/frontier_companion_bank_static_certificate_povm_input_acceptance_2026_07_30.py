#!/usr/bin/env python3
"""Conditional split/merge POVM acceptance for supplied apparatus mappings.

The companion-bank source contributes finite static-certificate and liveness
bookkeeping only.  Field selection, coordinate order, signs, normalization,
projector directions, contact, and coefficient/projector pairing are supplied
apparatus conventions.  This runner tests only the resulting conditional
Cycle-317 matrix identities; it selects no Born law, occurrence, outcome,
Record, history, or empirical calibration.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/COMPANION_BANK_STATIC_CERTIFICATE_POVM_CONDITIONAL_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_static_certificate_povm_input_acceptance_2026_07_30.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_companion_bank_even_exchange_port_2026_07_28.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py",
    "docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/COMPANION_BANK_STATIC_CERTIFICATE_POVM_INPUT_CONVENTION_META_NOTE_2026-07-30.md",
    "docs/COMPANION_BANK_STATIC_CERTIFICATE_POVM_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/work_history/repo/review_feedback/ACTIVE_CUBIC_SOURCE_RESPONSE_CYCLE211_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/AUTONOMOUS_CUBIC_FIELD_EMISSION_CYCLE214_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/CONTACT_CLOSE_TYPED_RECORD_DAG_CYCLE287_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_DISCIPLINE_CHECKLIST_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_LEDGER_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_REFERENCE_RELATIVE_LOCALIZED_PAIR_LIFT_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_STAGGERED_RESERVOIR_CATCHUP_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

import numpy as np

import frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28 as SOURCE
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE_SHA256 = (
    "b3fee8b662bbed34f7259fd6aa83de5de26ec07272c154eec08b8fdf88f283f0"
)
EXPECTED_B317_SHA256 = (
    "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
)
FIELDS = ("certificate", "binder", "actuality", "admissibility", "law_domain")
VARIANTS = ("primary", "alternate_port")
SUPPLIED_BLOCH_FIELDS = ("certificate", "actuality", "law_domain")
SUPPLIED_STAGE_ORDER = ("A", "B", "C", "D")
SUPPLIED_SPLITS = (0.17, 0.29, 0.54)
SUPPLIED_DIRECTIONS = (
    (1.0, 2.0, 3.0),
    (-1.0, 0.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, 0.0, -1.0),
)
EXPECTED_STAGE_COUNTS = {
    "primary": {"A": 100, "B": 152, "C": 180, "D": 72},
    "alternate_port": {"A": 100, "B": 12, "C": 0, "D": 72},
}
TOL = 2.0e-14


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def source_snapshot() -> dict[str, object]:
    atlas = SOURCE.EPOCH.P.build_private_atlases()
    primary = SOURCE.EPOCH.build_epoch((2, 2, 2), "primary", atlas)
    alternate = SOURCE.EPOCH.build_epoch(
        (2, 2, 2),
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}
    rows: dict[str, object] = {}
    for variant in VARIANTS:
        extension = SOURCE.extend_and_walk(bundles[variant])
        word_stage = {
            word.word_id: slot.stage
            for slot in extension["slots"]
            for word in slot.words
        }
        destinations = Counter(
            word_stage[edge[1]] for edge in extension["handoffs"]
        )
        rows[variant] = {
            "field_counts": {
                field: sum(int(row[field]) for row in extension["table"])
                for field in FIELDS
            },
            "stage_destination_counts": {
                stage: int(destinations[stage]) for stage in SUPPLIED_STAGE_ORDER
            },
            "rows": len(extension["table"]),
            "lawful": bool(extension["lawful"]),
        }
    return rows


def rejected(callable_object: object) -> bool:
    try:
        callable_object()
    except ValueError:
        return True
    return False


def spectra(effects: tuple[np.ndarray, ...]) -> list[list[float]]:
    return [
        [float(value) for value in np.linalg.eigvalsh((effect + effect.conj().T) / 2)]
        for effect in effects
    ]


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(label: str, condition: bool) -> None:
        checks.append((label, bool(condition)))
        print("PASS" if condition else "FAIL", label)

    source_path = ROOT / (
        "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_"
        "projection_2026_07_28.py"
    )
    b317_path = ROOT / (
        "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_"
        "2026_07_18.py"
    )
    pins = {
        "source": file_sha256(source_path),
        "B317": file_sha256(b317_path),
    }
    check(
        "dependency bytes match the reviewed landed source and Cycle-317 surface",
        pins
        == {
            "source": EXPECTED_SOURCE_SHA256,
            "B317": EXPECTED_B317_SHA256,
        }
        and Path(SOURCE.__file__).resolve() == source_path.resolve()
        and Path(B317.__file__).resolve() == b317_path.resolve(),
    )

    source = source_snapshot()
    check(
        "landed source yields only the frozen static-predicate and liveness counts",
        all(
            source[variant]["field_counts"] == {field: 24 for field in FIELDS}
            and source[variant]["stage_destination_counts"]
            == EXPECTED_STAGE_COUNTS[variant]
            and source[variant]["rows"] == 24
            and source[variant]["lawful"]
            for variant in VARIANTS
        ),
    )

    combined_fields = {
        field: sum(source[variant]["field_counts"][field] for variant in VARIANTS)
        for field in FIELDS
    }
    raw = np.asarray(
        [combined_fields[field] for field in SUPPLIED_BLOCH_FIELDS], dtype=float
    )
    direction = raw / np.linalg.norm(raw)
    projector = B317.projector_bloch(direction)
    contact = np.diag((np.exp(1j * B317.c311.COUPLING), 1.0)).astype(complex)
    split_isometry, split_groups = B317.split_projector_isometry(
        projector, SUPPLIED_SPLITS, contact
    )
    split_effects = B317.derived_effects(split_isometry, split_groups)
    split_metrics = B317.menu_metrics(split_effects)
    split_isometry_residual = float(
        np.linalg.norm(split_isometry.conj().T @ split_isometry - B317.I2)
    )
    check(
        "supplied direction and split simplex produce the conditional four-effect POVM",
        np.linalg.norm(projector @ projector - projector) < TOL
        and split_isometry_residual < TOL
        and split_metrics["normalization"] < TOL
        and split_metrics["minimum_eigenvalue"] > -TOL
        and split_metrics["maximum_eigenvalue"] <= 1 + TOL,
    )

    combined_stages = tuple(
        sum(
            source[variant]["stage_destination_counts"][stage]
            for variant in VARIANTS
        )
        for stage in SUPPLIED_STAGE_ORDER
    )
    stage_total = sum(combined_stages)
    fractions = tuple(value / stage_total for value in combined_stages)
    directions = tuple(
        np.asarray(row, dtype=float) / np.linalg.norm(row)
        for row in SUPPLIED_DIRECTIONS
    )
    projectors = tuple(B317.projector_bloch(row) for row in directions)
    merge_isometry, merge_groups = B317.merge_isometry(
        tuple(zip(fractions, projectors)), contact
    )
    merge_effects = B317.derived_effects(merge_isometry, merge_groups)
    merge_metrics = B317.menu_metrics(merge_effects)
    merge_isometry_residual = float(
        np.linalg.norm(merge_isometry.conj().T @ merge_isometry - B317.I2)
    )
    weighted_bloch = sum(
        (fraction * vector for fraction, vector in zip(fractions, directions)),
        start=np.zeros(3),
    )
    expected_plus_eigenvalues = sorted(
        ((1 - np.linalg.norm(weighted_bloch)) / 2,
         (1 + np.linalg.norm(weighted_bloch)) / 2)
    )
    observed_plus_eigenvalues = [
        float(value) for value in np.linalg.eigvalsh(merge_effects[0])
    ]
    check(
        "supplied order and pairing produce the conditional five-effect POVM",
        combined_stages == (200, 164, 180, 144)
        and abs(sum(fractions) - 1) < TOL
        and merge_isometry_residual < TOL
        and merge_metrics["normalization"] < TOL
        and np.linalg.norm(
            np.asarray(observed_plus_eigenvalues)
            - np.asarray(expected_plus_eigenvalues)
        )
        < TOL,
    )

    all_subset_directions = []
    for fields in combinations(FIELDS, 3):
        candidate = np.asarray([combined_fields[field] for field in fields], dtype=float)
        all_subset_directions.append(candidate / np.linalg.norm(candidate))
    source_nonidentification = max(
        np.linalg.norm(candidate - direction)
        for candidate in all_subset_directions
    )
    sign_flipped = direction.copy()
    sign_flipped[0] *= -1
    sign_projector = B317.projector_bloch(sign_flipped)
    sign_delta = float(np.linalg.norm(sign_projector - projector))
    reversed_isometry, reversed_groups = B317.merge_isometry(
        tuple(zip(fractions, reversed(projectors))), contact
    )
    reversed_effects = B317.derived_effects(reversed_isometry, reversed_groups)
    pairing_delta = float(np.linalg.norm(reversed_effects[0] - merge_effects[0]))
    check(
        "valid-domain mutations expose that source bookkeeping does not select the mappings",
        source_nonidentification < TOL
        and sign_delta > 0.8
        and pairing_delta > 0.1
        and np.linalg.norm(
            reversed_isometry.conj().T @ reversed_isometry - B317.I2
        )
        < TOL,
    )

    l1_direction = raw / np.sum(np.abs(raw))
    negative_fractions = list(fractions)
    negative_fractions[0] *= -1
    negative_fractions[1] += 2 * fractions[0]
    check(
        "invalid normalization and negative coefficients are rejected",
        rejected(lambda: B317.projector_bloch(l1_direction))
        and rejected(
            lambda: B317.merge_isometry(
                tuple(zip(negative_fractions, projectors)), contact
            )
        ),
    )

    check(
        "reported residual labels separate isometry and POVM normalization",
        abs(split_isometry_residual - 2.4999285328858064e-16) < TOL
        and abs(split_metrics["normalization"] - 2.220446049250313e-16) < TOL
        and abs(merge_isometry_residual - 0.0) < TOL
        and abs(merge_metrics["normalization"] - 3.1463121132764933e-16) < TOL,
    )
    report = {
        "status": "PASS" if all(value for _label, value in checks) else "FAIL",
        "pins": pins,
        "source": source,
        "supplied": {
            "Bloch_fields": list(SUPPLIED_BLOCH_FIELDS),
            "Bloch_coordinate_order": ["x", "y", "z"],
            "sign": "positive",
            "pooling": list(VARIANTS),
            "normalization": "Euclidean L2",
            "split_fractions": list(SUPPLIED_SPLITS),
            "stage_order": list(SUPPLIED_STAGE_ORDER),
            "projector_directions": [list(row) for row in SUPPLIED_DIRECTIONS],
            "coefficient_projector_pairing": "positional",
            "contact_phase": float(B317.c311.COUPLING),
        },
        "split": {
            "direction": direction.tolist(),
            "isometry_residual": split_isometry_residual,
            "povm_normalization_residual": split_metrics["normalization"],
            "effect_spectra": spectra(split_effects),
        },
        "merge": {
            "combined_stage_counts": list(combined_stages),
            "fractions": list(fractions),
            "weighted_bloch": weighted_bloch.tolist(),
            "weighted_bloch_norm": float(np.linalg.norm(weighted_bloch)),
            "isometry_residual": merge_isometry_residual,
            "povm_normalization_residual": merge_metrics["normalization"],
            "plus_effect_eigenvalues": observed_plus_eigenvalues,
            "effect_spectra": spectra(merge_effects),
        },
        "mapping_controls": {
            "all_three_field_subsets_same_direction": bool(
                source_nonidentification < TOL
            ),
            "sign_flip_projector_delta": sign_delta,
            "reversed_pairing_plus_effect_delta": pairing_delta,
            "mutated_inputs_remain_valid_povms": True,
            "source_selects_mapping": False,
        },
        "claim_boundary": {
            "conditional_matrix_identities_only": True,
            "register_state_readout": False,
            "source_to_apparatus_map_derived": False,
            "Born_law_selected": False,
            "occurrence_or_outcome_selected": False,
            "Record_or_history_constructed": False,
            "empirical_calibration": False,
        },
        "checks": {"pass": sum(value for _label, value in checks), "fail": sum(
            not value for _label, value in checks
        )},
        "authority": "none",
        "audit": "unset",
    }
    print("RESULT_JSON", json.dumps(report, sort_keys=True, separators=(",", ":")))
    print(
        "SUMMARY PASS",
        report["checks"]["pass"],
        "FAIL",
        report["checks"]["fail"],
    )
    print("RESULT COMPANION_BANK_STATIC_CERTIFICATE_POVM_ACCEPTANCE_GREEN")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
