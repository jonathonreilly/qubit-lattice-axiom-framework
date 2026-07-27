#!/usr/bin/env python3
"""Three-register cross-encoding taste-qubit teleportation certificate.

Scope: exact finite-algebra support for the ideal logical three-register
cross-encoding map.  It extends the bounded cross-encoding check from two
independently chosen
encodings to three independently chosen encodings:

    A = Alice unknown input encoding
    R = Alice Bell-resource-half encoding
    B = Bob Bell-resource-half encoding

The audited Hilbert surface is still the Kogut-Susskind cell/taste
factorization used by the protocol, portability, and cross-encoding runners:

    C^(side^dim) = C^((side/2)^dim cells) tensor C^(2^dim tastes)

This checks only the ideal finite-dimensional logical teleportation identity.
It does not claim a physical teleportation implementation, apparatus or
resource preparation, Hamiltonian or matter transport, noise tolerance,
durable-record production, an unbounded-lattice result, mass, charge, or
energy transfer, object transport, or faster-than-light signaling.
"""

from __future__ import annotations

import argparse
import collections
import sys

import numpy as np

from frontier_teleportation_three_register_cross_encoding_core import (
    Encoding,
    Geometry,
    I2,
    MapSummary,
    OUTCOME_LABELS,
    OUTCOME_ORDER,
    RequirementSummary,
    StructuralCertificate,
    X2,
    build_structural_certificate,
    classify_bob_fixed_failure,
    classify_fixed_bell_failure,
    decode_triple_index,
    enumerate_encodings,
    parse_csv_ints,
    run_teleportation_trials,
    select_triple_indices,
    valid_geometries,
)

AUDIT_INPUT_PATHS = (
    "scripts/frontier_teleportation_three_register_cross_encoding_core.py",
)


def format_counter(counter: collections.Counter[object]) -> str:
    if not counter:
        return "none"
    return ", ".join(
        f"{key}={value}"
        for key, value in sorted(counter.items(), key=lambda item: str(item[0]))
    )


def format_outcomes(outcomes: set[tuple[int, int]]) -> str:
    ordered = [outcome for outcome in OUTCOME_ORDER if outcome in outcomes]
    return ", ".join(OUTCOME_LABELS[outcome] for outcome in ordered)


def print_by_geometry(summary: MapSummary) -> None:
    print("  by geometry: dim side pass/total expected_pass")
    for (dim, side), (total, passed, expected) in sorted(summary.by_geometry.items()):
        print(f"    {dim:>3d} {side:>4d} {passed:>6d}/{total:<6d} {expected:>6d}")


def print_map_summary(summary: MapSummary, *, detailed: bool = False) -> None:
    print(f"{summary.label}:")
    print(f"  expected pass cases: {summary.expected_pass_cases}/{summary.total_cases}")
    print(
        "  teleportation/no-signaling pass: "
        f"{summary.teleportation_pass}/{summary.teleportation_run} run "
        f"({summary.skipped_before_teleportation} skipped before teleportation)"
    )
    print(f"  failure causes: {format_counter(summary.failure_causes)}")
    if summary.teleportation_run:
        print(f"  minimum corrected-state fidelity: {summary.min_fidelity:.16f}")
        print(f"  maximum infidelity: {summary.max_infidelity:.3e}")
        print(
            "  pairwise pre-message/corrected-trace errors: "
            f"{summary.max_pairwise_pre_message_distance:.3e}/"
            f"{summary.max_corrected_trace_error:.3e}"
        )
        if detailed:
            print(
                "  Bell-projector errors (resolution/idempotence/orthogonality): "
                f"{summary.max_projector_resolution_error:.3e}/"
                f"{summary.max_projector_idempotence_error:.3e}/"
                f"{summary.max_projector_orthogonality_error:.3e}"
            )
            print(
                "  probability errors (branch/total): "
                f"{summary.max_branch_probability_error:.3e}/"
                f"{summary.max_total_probability_error:.3e}"
            )
            print(
                "  Bob I/2 trace distances (before/after Alice measurement): "
                f"{summary.max_pre_measurement_trace_distance:.3e}/"
                f"{summary.max_post_measurement_trace_distance:.3e}"
            )
            print("  Bell outcomes seen: " + format_outcomes(summary.outcomes_seen))


def survey(
    dims: tuple[int, ...],
    sides: tuple[int, ...],
    n_trials: int,
    seed: int,
    tolerance: float,
    max_triples_per_geometry: int,
) -> tuple[
    list[Geometry],
    list[tuple[int, int, str]],
    dict[Geometry, list[Encoding]],
    RequirementSummary,
    MapSummary,
    MapSummary,
    MapSummary,
    MapSummary,
    MapSummary,
]:
    geometries, skipped = valid_geometries(dims, sides)
    encodings_by_geometry = {
        geometry: enumerate_encodings(geometry, tolerance) for geometry in geometries
    }

    requirements = RequirementSummary()
    adapted_summary = MapSummary(label="axis_adapted_three_register_cross_encoding")
    missing_a_to_r_summary = MapSummary(label="missing_a_to_r_conversion_control")
    fixed_bell_summary = MapSummary(label="non_adapted_bell_measurement_control")
    bob_fixed_summary = MapSummary(label="non_adapted_bob_correction_control")
    wrong_resource_summary = MapSummary(label="wrong_b_resource_conversion_control")

    trial_rng = np.random.default_rng(seed)
    selection_rng = np.random.default_rng(seed + 1)

    for geometry in geometries:
        encodings = encodings_by_geometry[geometry]
        n_encodings = len(encodings)
        triple_indices = select_triple_indices(
            n_encodings,
            max_triples=max_triples_per_geometry,
            rng=selection_rng,
        )
        requirements.add_geometry(
            geometry,
            possible=n_encodings**3,
            surveyed=len(triple_indices),
        )

        for triple_index in triple_indices:
            a_index, r_index, b_index = decode_triple_index(triple_index, n_encodings)
            a_encoding = encodings[a_index]
            r_encoding = encodings[r_index]
            b_encoding = encodings[b_index]
            requirements.update(a_encoding, r_encoding, b_encoding)

            adapted_metrics = run_teleportation_trials(
                measure_z_a=a_encoding.canonical_z_logical,
                measure_x_a=a_encoding.canonical_adapted_x_logical,
                measure_z_r=r_encoding.canonical_z_logical,
                measure_x_r=r_encoding.canonical_adapted_x_logical,
                bob_z_op=b_encoding.canonical_z_logical,
                bob_x_op=b_encoding.canonical_adapted_x_logical,
                resource_conversion_map=I2,
                target_conversion_map=I2,
                n_trials=n_trials,
                rng=trial_rng,
            )
            adapted_summary.update_metrics(
                geometry=geometry,
                metrics=adapted_metrics,
                expected_pass=True,
                tolerance=tolerance,
            )

            if a_encoding.indices == r_encoding.indices:
                missing_a_to_r_summary.update_metrics(
                    geometry=geometry,
                    metrics=adapted_metrics,
                    expected_pass=True,
                    tolerance=tolerance,
                )
            else:
                missing_a_to_r_summary.update_skip(
                    geometry=geometry,
                    expected_pass=False,
                    cause="missing_explicit_a_to_r_site_conversion",
                )

            fixed_bell_expected = a_encoding.fixed_x_usable and r_encoding.fixed_x_usable
            if fixed_bell_expected:
                fixed_bell_metrics = run_teleportation_trials(
                    measure_z_a=a_encoding.canonical_z_logical,
                    measure_x_a=a_encoding.fixed_x_logical,
                    measure_z_r=r_encoding.canonical_z_logical,
                    measure_x_r=r_encoding.fixed_x_logical,
                    bob_z_op=b_encoding.canonical_z_logical,
                    bob_x_op=b_encoding.canonical_adapted_x_logical,
                    resource_conversion_map=I2,
                    target_conversion_map=I2,
                    n_trials=n_trials,
                    rng=trial_rng,
                )
                fixed_bell_summary.update_metrics(
                    geometry=geometry,
                    metrics=fixed_bell_metrics,
                    expected_pass=True,
                    tolerance=tolerance,
                )
            else:
                fixed_bell_summary.update_skip(
                    geometry=geometry,
                    expected_pass=False,
                    cause=classify_fixed_bell_failure(a_encoding, r_encoding),
                )

            bob_fixed_metrics = run_teleportation_trials(
                measure_z_a=a_encoding.canonical_z_logical,
                measure_x_a=a_encoding.canonical_adapted_x_logical,
                measure_z_r=r_encoding.canonical_z_logical,
                measure_x_r=r_encoding.canonical_adapted_x_logical,
                bob_z_op=b_encoding.canonical_z_logical,
                bob_x_op=b_encoding.fixed_x_logical,
                resource_conversion_map=I2,
                target_conversion_map=I2,
                n_trials=n_trials,
                rng=trial_rng,
            )
            bob_fixed_summary.update_metrics(
                geometry=geometry,
                metrics=bob_fixed_metrics,
                expected_pass=b_encoding.fixed_x_usable,
                tolerance=tolerance,
                failure_cause=(
                    None
                    if b_encoding.fixed_x_usable
                    else classify_bob_fixed_failure(b_encoding)
                ),
            )

            wrong_resource_metrics = run_teleportation_trials(
                measure_z_a=a_encoding.canonical_z_logical,
                measure_x_a=a_encoding.canonical_adapted_x_logical,
                measure_z_r=r_encoding.canonical_z_logical,
                measure_x_r=r_encoding.canonical_adapted_x_logical,
                bob_z_op=b_encoding.canonical_z_logical,
                bob_x_op=b_encoding.canonical_adapted_x_logical,
                resource_conversion_map=X2,
                target_conversion_map=I2,
                n_trials=n_trials,
                rng=trial_rng,
            )
            wrong_resource_summary.update_metrics(
                geometry=geometry,
                metrics=wrong_resource_metrics,
                expected_pass=False,
                tolerance=tolerance,
                failure_cause="wrong_b_resource_conversion_map",
            )

    return (
        geometries,
        skipped,
        encodings_by_geometry,
        requirements,
        adapted_summary,
        missing_a_to_r_summary,
        fixed_bell_summary,
        bob_fixed_summary,
        wrong_resource_summary,
    )


def print_requirement_summary(requirements: RequirementSummary) -> None:
    print("Three-register requirement classification:")
    print("  geometry: dim side surveyed/possible triples")
    for (dim, side), (possible, surveyed) in sorted(requirements.by_geometry.items()):
        print(f"    {dim:>3d} {side:>4d} {surveyed:>6d}/{possible:<8d}")
    print(f"  triples surveyed: {requirements.surveyed_triples}")
    print(f"  possible triples in requested geometries: {requirements.total_possible_triples}")
    print()
    print("  A input -> R Alice-resource-half map:")
    print(f"    no site conversion needed: {requirements.a_to_r_same_support}")
    print(f"    explicit A->R site maps needed: {requirements.explicit_a_to_r_maps}")
    print(f"    breakdown: {format_counter(requirements.a_to_r_pair_kinds)}")
    print()
    print("  R Alice-resource-half -> B Bob-resource-half map:")
    print(f"    no site conversion needed: {requirements.r_to_b_same_support}")
    print(f"    explicit R->B resource site maps needed: {requirements.explicit_r_to_b_maps}")
    print(f"    breakdown: {format_counter(requirements.r_to_b_pair_kinds)}")
    print()
    print("  Bell-measurement adaptation:")
    print(f"    cross-register A/R Bell pairing required: {requirements.cross_register_bell_pairing_required}")
    print(f"    axis-adapted Bell X required: {requirements.axis_adapted_bell_x_required}")
    print(f"    adapted Bell measurement required by either condition: {requirements.adapted_bell_measurement_required}")
    print(f"    fixed last-axis Bell X sufficient: {requirements.fixed_last_axis_bell_x_sufficient}")
    print()
    print("  Combined site-map requirements:")
    print(f"    no A->R or R->B site maps needed: {requirements.no_site_maps_needed}")
    print(f"    both A->R and R->B site maps needed: {requirements.both_site_maps_needed}")
    print(
        "    max partial-isometry error C^dag C=P_source, C C^dag=P_target: "
        f"{requirements.max_partial_isometry_error:.3e}"
    )


def print_structural_certificate(certificate: StructuralCertificate) -> None:
    logical = certificate.logical
    print("Exhaustive factorized structural certificate:")
    print(
        "  encoding supports enumerated from the closed-form count: "
        f"{certificate.total_encodings}/{certificate.expected_encodings}"
    )
    print(
        "  ordered encoding isometries certified: "
        f"{certificate.isometry_pass_count}/{certificate.total_encodings}"
    )
    print(
        "  distinct ordered encoding supports certified: "
        f"{certificate.unique_encoding_count}/{certificate.total_encodings}"
    )
    print(
        "  canonical logical Pauli pairs certified: "
        f"{certificate.canonical_pauli_pass_count}/{certificate.total_encodings}"
    )
    print(
        "  ordered A/R/B triples covered by the factorized theorem: "
        f"{certificate.certified_ordered_triples}/"
        f"{certificate.expected_ordered_triples}"
    )
    print(f"  max V_E^dag V_E-I error: {certificate.max_isometry_error:.3e}")
    print(f"  max P_E^2-P_E error: {certificate.max_projector_error:.3e}")
    print(f"  max canonical Z_E-Z error: {certificate.max_canonical_z_error:.3e}")
    print(f"  max canonical X_E-X error: {certificate.max_canonical_x_error:.3e}")
    print(f"  max logical Pauli square error: {certificate.max_pauli_square_error:.3e}")
    print(
        "  max logical Pauli anticommutator error: "
        f"{certificate.max_pauli_anticommutator_error:.3e}"
    )
    print(
        "  rank-one logical Bell projectors certified: "
        f"{logical.bell_projector_rank_one_count}/{len(OUTCOME_ORDER)}"
    )
    print(
        "  max logical Bell-projector resolution error: "
        f"{logical.bell_projector_resolution_error:.3e}"
    )
    print(
        "  max logical Bell-projector idempotence error: "
        f"{logical.bell_projector_idempotence_error:.3e}"
    )
    print(
        "  max logical Bell-projector orthogonality error: "
        f"{logical.bell_projector_orthogonality_error:.3e}"
    )
    print(
        "  max logical Bell-projector outer-product error: "
        f"{logical.bell_projector_outer_product_error:.3e}"
    )
    print(f"  max logical Bell-branch map error: {logical.branch_map_error:.3e}")
    print(
        "  max logical branch-channel error on the matrix-unit basis: "
        f"{logical.branch_channel_basis_error:.3e}"
    )
    print(
        "  max corrected logical branch-map error: "
        f"{logical.corrected_branch_map_error:.3e}"
    )
    print(
        "  max corrected channel error on the matrix-unit basis: "
        f"{logical.corrected_channel_basis_error:.3e}"
    )
    print(
        "  max Pauli-twirl error on the matrix-unit basis: "
        f"{logical.pauli_twirl_basis_error:.3e}"
    )


def print_summary(
    geometries: list[Geometry],
    skipped: list[tuple[int, int, str]],
    encodings_by_geometry: dict[Geometry, list[Encoding]],
    requirements: RequirementSummary,
    adapted_summary: MapSummary,
    missing_a_to_r_summary: MapSummary,
    fixed_bell_summary: MapSummary,
    bob_fixed_summary: MapSummary,
    wrong_resource_summary: MapSummary,
    structural_certificate: StructuralCertificate,
    dims: tuple[int, ...],
    sides: tuple[int, ...],
    n_trials: int,
    seed: int,
    tolerance: float,
    max_triples_per_geometry: int,
) -> bool:
    print("THREE-REGISTER CROSS-ENCODING TASTE-QUBIT TELEPORTATION CERTIFICATE")
    print("Scope: exact finite logical algebra; ideal state-transfer identity only")
    print()
    print(
        f"Configuration: dims={dims}, sides={sides}, geometries={len(geometries)}, "
        f"trials={n_trials}, seed={seed}, triple_cap={max_triples_per_geometry}, "
        f"tolerance={tolerance:.1e}"
    )
    print()

    if skipped:
        print("Skipped geometries:")
        for dim, side, reason in skipped:
            print(f"  dim={dim} side={side}: {reason}")
        print()

    total_encodings = sum(len(encodings) for encodings in encodings_by_geometry.values())
    print("Encoding totals:")
    print(f"  encoding supports across geometries: {total_encodings}")
    print()

    print_structural_certificate(structural_certificate)
    print()

    print_requirement_summary(requirements)
    print()

    print_map_summary(adapted_summary, detailed=True)
    print()
    print_map_summary(missing_a_to_r_summary)
    print()
    print_map_summary(fixed_bell_summary)
    print()
    print_map_summary(bob_fixed_summary)
    print()
    print_map_summary(wrong_resource_summary)
    print()

    logical = structural_certificate.logical
    pass_checks = {
        "exhaustive encoding-isometry premises": (
            structural_certificate.isometry_pass_count
            == structural_certificate.total_encodings
            == structural_certificate.expected_encodings
        ),
        "distinct ordered encoding supports": (
            structural_certificate.unique_encoding_count
            == structural_certificate.total_encodings
        ),
        "exhaustive canonical logical-Pauli premises": (
            structural_certificate.canonical_pauli_pass_count
            == structural_certificate.total_encodings
        ),
        "logical Bell-projector algebra": (
            logical.bell_projector_rank_one_count == len(OUTCOME_ORDER)
            and logical.bell_projector_resolution_error < tolerance
            and logical.bell_projector_idempotence_error < tolerance
            and logical.bell_projector_orthogonality_error < tolerance
            and logical.bell_projector_outer_product_error < tolerance
        ),
        "logical branch and correction channels on operator basis": (
            logical.branch_map_error < tolerance
            and logical.branch_channel_basis_error < tolerance
            and logical.corrected_branch_map_error < tolerance
            and logical.corrected_channel_basis_error < tolerance
        ),
        "logical Pauli twirl on operator basis": (
            logical.pauli_twirl_basis_error < tolerance
        ),
        "factorized ordered-triple coverage": (
            structural_certificate.certified_ordered_triples
            == structural_certificate.expected_ordered_triples
            == requirements.total_possible_triples
        ),
        "axis-adapted three-register maps": adapted_summary.unexpected_results == 0
        and adapted_summary.teleportation_pass == adapted_summary.total_cases,
        "axis-adapted all Bell outcomes": adapted_summary.outcomes_seen == set(OUTCOME_ORDER),
        "axis-adapted Bob pre-message input-independence": (
            adapted_summary.max_pre_measurement_trace_distance < tolerance
            and adapted_summary.max_post_measurement_trace_distance < tolerance
            and adapted_summary.max_pairwise_pre_message_distance < tolerance
        ),
        "missing A->R conversion control": (
            missing_a_to_r_summary.unexpected_results == 0
            and missing_a_to_r_summary.expected_pass_cases
            == missing_a_to_r_summary.teleportation_pass
            and missing_a_to_r_summary.skipped_before_teleportation
            == requirements.explicit_a_to_r_maps
        ),
        "non-adapted Bell measurement boundary": (
            fixed_bell_summary.unexpected_results == 0
            and fixed_bell_summary.expected_pass_cases == fixed_bell_summary.teleportation_pass
        ),
        "non-adapted Bob correction control": (
            bob_fixed_summary.unexpected_results == 0
            and bob_fixed_summary.expected_pass_cases == bob_fixed_summary.teleportation_pass
            and bob_fixed_summary.max_infidelity > 0.5
        ),
        "wrong B resource conversion control": (
            wrong_resource_summary.unexpected_results == 0
            and wrong_resource_summary.teleportation_pass == 0
            and wrong_resource_summary.max_infidelity > 0.5
        ),
    }
    print()
    print("Acceptance gates:")
    for name, ok in pass_checks.items():
        print(f"  {name}: {'PASS' if ok else 'FAIL'}")

    return all(pass_checks.values())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dims",
        default="1,2,3",
        help="comma-separated dimensions to audit; default is context dimensions 1,2,3",
    )
    parser.add_argument(
        "--sides",
        default="2,4",
        help="comma-separated even side lengths; default keeps three-register count bounded",
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=4,
        help="random teleportation trials per surveyed A/R/B triple",
    )
    parser.add_argument(
        "--max-triples-per-geometry",
        type=int,
        default=512,
        help="bounded deterministic sample per geometry; use 0 for exhaustive triples",
    )
    parser.add_argument("--seed", type=int, default=20260425, help="random seed")
    parser.add_argument("--tolerance", type=float, default=1e-12, help="pass/fail tolerance")
    args = parser.parse_args()

    if args.trials <= 0:
        raise ValueError("--trials must be positive")
    if args.max_triples_per_geometry < 0:
        raise ValueError("--max-triples-per-geometry must be nonnegative")

    dims = parse_csv_ints(args.dims)
    sides = parse_csv_ints(args.sides)

    (
        geometries,
        skipped,
        encodings_by_geometry,
        requirements,
        adapted_summary,
        missing_a_to_r_summary,
        fixed_bell_summary,
        bob_fixed_summary,
        wrong_resource_summary,
    ) = survey(
        dims=dims,
        sides=sides,
        n_trials=args.trials,
        seed=args.seed,
        tolerance=args.tolerance,
        max_triples_per_geometry=args.max_triples_per_geometry,
    )
    structural_certificate = build_structural_certificate(
        encodings_by_geometry,
        tolerance=args.tolerance,
    )
    ok = print_summary(
        geometries=geometries,
        skipped=skipped,
        encodings_by_geometry=encodings_by_geometry,
        requirements=requirements,
        adapted_summary=adapted_summary,
        missing_a_to_r_summary=missing_a_to_r_summary,
        fixed_bell_summary=fixed_bell_summary,
        bob_fixed_summary=bob_fixed_summary,
        wrong_resource_summary=wrong_resource_summary,
        structural_certificate=structural_certificate,
        dims=dims,
        sides=sides,
        n_trials=args.trials,
        seed=args.seed,
        tolerance=args.tolerance,
        max_triples_per_geometry=args.max_triples_per_geometry,
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
