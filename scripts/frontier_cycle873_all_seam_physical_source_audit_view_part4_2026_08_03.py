#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 all seam physical source, part 4/5."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
PART_ORDINAL = 4
PART_COUNT = 5
FIRST_SOURCE_LINE = 1499
LAST_SOURCE_LINE = 1933
TOTAL_SOURCE_LINES = 2038
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 001499|        "F17_only_route_failures": sum(
# C873SRC 001500|            row["f17_route_failures"] for row in macro_rows
# C873SRC 001501|        ),
# C873SRC 001502|        "alpha_plus_minus_route_census_failures": alpha_route_census_failures,
# C873SRC 001503|        "schedule_color_rule": "(axis, owner_x mod2, owner_y mod2, owner_z mod2)",
# C873SRC 001504|        "schedule_color_templates": 24,
# C873SRC 001505|        "active_colors": len(groups),
# C873SRC 001506|        "ordered_active_colors": ordered_colors,
# C873SRC 001507|        "same_color_macro_pairs": same_color_pairs,
# C873SRC 001508|        "same_color_route_footprint_collisions": same_color_collisions,
# C873SRC 001509|        "F17_only_same_color_route_footprint_collisions": f17_same_color_collisions,
# C873SRC 001510|        "naive_axis_only_macro_pairs": naive_pairs,
# C873SRC 001511|        "naive_axis_only_route_footprint_collisions": naive_collisions,
# C873SRC 001512|        "F17_only_naive_axis_only_route_footprint_collisions":
# C873SRC 001513|            f17_naive_collisions,
# C873SRC 001514|        "repeated_color_groups": sum(len(rows) > 1 for rows in groups.values()),
# C873SRC 001515|        "maximum_parallel_macros": max(map(len, groups.values())),
# C873SRC 001516|        "fixed_schedule_parallel_routed_depth": parallel_depth,
# C873SRC 001517|        "fixed_schedule_identity_padding": identity_padding,
# C873SRC 001518|        "F17_only_total_macro_logical_instructions": sum(
# C873SRC 001519|            row["f17_logical"] for row in macro_rows
# C873SRC 001520|        ),
# C873SRC 001521|        "F17_only_total_macro_routed_gates": f17_serial_routed,
# C873SRC 001522|        "F17_only_macro_min_logical_instructions": min(
# C873SRC 001523|            row["f17_logical"] for row in macro_rows
# C873SRC 001524|        ),
# C873SRC 001525|        "F17_only_macro_max_logical_instructions": max(
# C873SRC 001526|            row["f17_logical"] for row in macro_rows
# C873SRC 001527|        ),
# C873SRC 001528|        "F17_only_macro_min_routed_gates": min(row["f17_routed"] for row in macro_rows),
# C873SRC 001529|        "F17_only_macro_max_routed_gates": max(row["f17_routed"] for row in macro_rows),
# C873SRC 001530|        "F17_only_fixed_schedule_parallel_routed_depth": f17_parallel_depth,
# C873SRC 001531|        "F17_only_fixed_schedule_identity_padding": f17_identity_padding,
# C873SRC 001532|        "fixed_schedule_sha256": schedule_digest,
# C873SRC 001533|        "active_schedule_color_deletions": schedule_deletions,
# C873SRC 001534|        "inactive_schedule_color_deletions": tuple(
# C873SRC 001535|            color for color, row in schedule_deletions.items()
# C873SRC 001536|            if not row["active_F17_basis_witnesses"]
# C873SRC 001537|        ),
# C873SRC 001538|        "local_route_footprint_envelopes": envelopes,
# C873SRC 001539|        "recurrent_separation_pitch": 32,
# C873SRC 001540|        "envelope_width_failures_at_pitch32": envelope_width_failures,
# C873SRC 001541|        "encoded_carrier_M2": len(carriers),
# C873SRC 001542|        "preparation_auxiliary_M2": len(auxiliary),
# C873SRC 001543|        "packet_M2_per_seam": C714.N,
# C873SRC 001544|        "F17_role_M2_per_seam": 20,
# C873SRC 001545|        "intentional_packet_F17_role_aliases_per_seam": 3,
# C873SRC 001546|        "incremental_persistent_F17_rail_M2_per_seam": F17,
# C873SRC 001547|        "combined_packet_plus_F17_bank_M2_per_seam": C714.N + F17,
# C873SRC 001548|        "F17_only_bank_M2_per_seam": 20,
# C873SRC 001549|        "F17_only_all_seam_bank_union_M2": len(f17_bank_union),
# C873SRC 001550|        "F17_only_expected_all_seam_bank_union_M2": 20 * len(seams),
# C873SRC 001551|        "F17_only_declared_assigned_M2": len(f17_assigned),
# C873SRC 001552|        "F17_only_route_touched_union_M2": len(f17_touched_union),
# C873SRC 001553|        "F17_only_restored_route_transit_not_assigned_M2": len(f17_route_transit),
# C873SRC 001554|        "F17_only_assigned_plus_route_support_union_M2": len(f17_support_union),
# C873SRC 001555|        "all_seam_bank_union_M2": len(bank_union),
# C873SRC 001556|        "expected_all_seam_bank_union_M2": (C714.N + F17) * len(seams),
# C873SRC 001557|        "declared_assigned_M2": len(assigned),
# C873SRC 001558|        "route_touched_union_M2": len(touched_union),
# C873SRC 001559|        "restored_route_transit_not_assigned_M2": len(route_transit),
# C873SRC 001560|        "assigned_plus_route_support_union_M2": len(support_union),
# C873SRC 001561|        "bank_radius": max(placement.radius for placement in placements),
# C873SRC 001562|        "bank_pair_overlap_pairs": bank_overlap_pairs,
# C873SRC 001563|        "bank_pair_overlap_sites": bank_overlap_sites,
# C873SRC 001564|        "F17_only_bank_pair_overlap_pairs": f17_bank_overlap_pairs,
# C873SRC 001565|        "F17_only_bank_pair_overlap_sites": f17_bank_overlap_sites,
# C873SRC 001566|        "bank_carrier_aux_collision_sites": len(bank_union & (carriers | set(auxiliary))),
# C873SRC 001567|        "F17_only_bank_carrier_aux_collision_sites": len(
# C873SRC 001568|            f17_bank_union & (carriers | set(auxiliary))
# C873SRC 001569|        ),
# C873SRC 001570|        "persistent_rail_packet_collision_sites": sum(
# C873SRC 001571|            len(set(placement.rails) & set(placement.packet.sites)) for placement in placements
# C873SRC 001572|        ),
# C873SRC 001573|        "shared_role_alias_failures": shared_alias_failures,
# C873SRC 001574|        "packet_entry_work_failures": packet_entry_work_failures,
# C873SRC 001575|        "single_rail_role_removal_census_cases": bank_delete_rows,
# C873SRC 001576|        "single_rail_role_removal_census_failures": bank_delete_undetected,
# C873SRC 001577|        "single_rail_role_removal_expected_remaining_roles": 19,
# C873SRC 001578|        "single_packet_site_role_removal_census_cases": packet_delete_rows,
# C873SRC 001579|        "single_packet_site_role_removal_census_failures": packet_delete_undetected,
# C873SRC 001580|        "single_packet_site_role_removal_expected_remaining_bank_M2": C714.N + F17 - 1,
# C873SRC 001581|        "role_removal_census_boundary": (
# C873SRC 001582|            "set-membership and expected-cardinality integrity only; no damaged "
# C873SRC 001583|            "circuit or state is executed, and these rows are not active deletion controls"
# C873SRC 001584|        ),
# C873SRC 001585|        "current_to_pointer_alias_collision_mutation_detected_seams":
# C873SRC 001586|            len(seams) - alias_collision_mutation_undetected,
# C873SRC 001587|        "current_to_pointer_alias_collision_mutation_undetected":
# C873SRC 001588|            alias_collision_mutation_undetected,
# C873SRC 001589|        "phase": {
# C873SRC 001590|            "seam_phase_rows": len(phase_rows),
# C873SRC 001591|            "raw_phase": [0.0, -1.0],
# C873SRC 001592|            "maximum_raw_square_to_minus_identity_residual": maximum_raw_minus_residual,
# C873SRC 001593|            "maximum_raw_square_to_identity_residual": maximum_raw_identity_residual,
# C873SRC 001594|            "maximum_formal_corrected_residual": maximum_phase_residual,
# C873SRC 001595|            "formal_scalar_angle_per_seam": math.pi / 2,
# C873SRC 001596|            "formal_scalar_routed_gates": 0,
# C873SRC 001597|            "unchanged_full_update_compiled_relative_phase_angle": inventory[
# C873SRC 001598|                "compiled_relative_to_target_global_phase_angle"
# C873SRC 001599|            ],
# C873SRC 001600|            "unchanged_full_update_formal_correction_angle": inventory[
# C873SRC 001601|                "exact_target_global_phase_correction_angle"
# C873SRC 001602|            ],
# C873SRC 001603|        },
# C873SRC 001604|    }
# C873SRC 001605|
# C873SRC 001606|
# C873SRC 001607|def coordinate_covariance_certificate(catalog):
# C873SRC 001608|    frames = C871.proper_frames()
# C873SRC 001609|    standard_basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
# C873SRC 001610|    paths = tuple(sorted(catalog["paths"], key=repr))
# C873SRC 001611|    signatures = tuple(sorted(catalog["signatures"], key=repr))
# C873SRC 001612|    banks = tuple(sorted(catalog["banks"], key=repr))
# C873SRC 001613|    frame_path_failures = frame_bank_failures = 0
# C873SRC 001614|    for frame in frames:
# C873SRC 001615|        moved_basis = tuple(C871.matvec(frame, row) for row in standard_basis)
# C873SRC 001616|        for path in paths:
# C873SRC 001617|            moved = tuple(C871.matvec(frame, site) for site in path)
# C873SRC 001618|            frame_path_failures += C871.coframe_path(
# C873SRC 001619|                moved[0], moved[-1], moved_basis
# C873SRC 001620|            ) != moved
# C873SRC 001621|        for bank in banks:
# C873SRC 001622|            moved = tuple(C871.matvec(frame, site) for site in bank)
# C873SRC 001623|            frame_bank_failures += len(set(moved)) != 20
# C873SRC 001624|    signature_products = path_products = bank_products = 0
# C873SRC 001625|    for left in frames:
# C873SRC 001626|        for right in frames:
# C873SRC 001627|            composed = left @ right
# C873SRC 001628|            signature_products += sum(
# C873SRC 001629|                tuple(C871.matvec(left, C871.matvec(right, site)) for site in signature[1])
# C873SRC 001630|                != tuple(C871.matvec(composed, site) for site in signature[1])
# C873SRC 001631|                for signature in signatures
# C873SRC 001632|            )
# C873SRC 001633|            path_products += sum(
# C873SRC 001634|                tuple(C871.matvec(left, C871.matvec(right, site)) for site in path)
# C873SRC 001635|                != tuple(C871.matvec(composed, site) for site in path)
# C873SRC 001636|                for path in paths
# C873SRC 001637|            )
# C873SRC 001638|            bank_products += sum(
# C873SRC 001639|                {C871.matvec(left, C871.matvec(right, site)) for site in bank}
# C873SRC 001640|                != {C871.matvec(composed, site) for site in bank}
# C873SRC 001641|                for bank in banks
# C873SRC 001642|            )
# C873SRC 001643|    # The color itself is an exact finite representation under endpoint-normalized frames.
# C873SRC 001644|    color_frame_failures = color_product_failures = 0
# C873SRC 001645|    representatives = tuple((axis, residue) for axis in range(3) for residue in product((0, 1), repeat=3))
# C873SRC 001646|
# C873SRC 001647|    def move_owner(axis, owner, frame):
# C873SRC 001648|        target_axis, sign = C871.signed_axis(frame, axis)
# C873SRC 001649|        moved = C871.matvec(frame, owner)
# C873SRC 001650|        if sign < 0:
# C873SRC 001651|            moved = add(moved, C871.matvec(frame, tuple(int(i == axis) for i in range(3))))
# C873SRC 001652|        return target_axis, moved
# C873SRC 001653|
# C873SRC 001654|    for axis, residue in representatives:
# C873SRC 001655|        for frame in frames:
# C873SRC 001656|            moved_axis, moved_owner = move_owner(axis, residue, frame)
# C873SRC 001657|            expected = (moved_axis, *(value & 1 for value in moved_owner))
# C873SRC 001658|            color_frame_failures += expected != schedule_color(
# C873SRC 001659|                (moved_owner, moved_axis, add(moved_owner, tuple(int(i == moved_axis) for i in range(3))), 0, 0)
# C873SRC 001660|            )
# C873SRC 001661|        for right in frames:
# C873SRC 001662|            mid_axis, mid_owner = move_owner(axis, residue, right)
# C873SRC 001663|            for left in frames:
# C873SRC 001664|                seq_axis, seq_owner = move_owner(mid_axis, mid_owner, left)
# C873SRC 001665|                direct_axis, direct_owner = move_owner(axis, residue, left @ right)
# C873SRC 001666|                color_product_failures += (
# C873SRC 001667|                    seq_axis, tuple(value & 1 for value in seq_owner)
# C873SRC 001668|                ) != (direct_axis, tuple(value & 1 for value in direct_owner))
# C873SRC 001669|    return {
# C873SRC 001670|        "proper_frames": len(frames),
# C873SRC 001671|        "ordered_frame_products": len(frames) ** 2,
# C873SRC 001672|        "unique_normalized_instruction_signatures": len(signatures),
# C873SRC 001673|        "unique_normalized_route_paths": len(paths),
# C873SRC 001674|        "unique_normalized_bank_templates": len(banks),
# C873SRC 001675|        "frame_route_path_failures": frame_path_failures,
# C873SRC 001676|        "frame_bank_failures": frame_bank_failures,
# C873SRC 001677|        "signature_product_rows": len(frames) ** 2 * len(signatures),
# C873SRC 001678|        "path_product_rows": len(frames) ** 2 * len(paths),
# C873SRC 001679|        "bank_product_rows": len(frames) ** 2 * len(banks),
# C873SRC 001680|        "signature_product_failures": signature_products,
# C873SRC 001681|        "path_product_failures": path_products,
# C873SRC 001682|        "bank_product_failures": bank_products,
# C873SRC 001683|        "color_frame_rows": len(representatives) * len(frames),
# C873SRC 001684|        "color_frame_failures": color_frame_failures,
# C873SRC 001685|        "color_product_rows": len(representatives) * len(frames) ** 2,
# C873SRC 001686|        "color_product_failures": color_product_failures,
# C873SRC 001687|    }
# C873SRC 001688|
# C873SRC 001689|
# C873SRC 001690|def collect_primary_failures(report):
# C873SRC 001691|    failures = []
# C873SRC 001692|    if not report["provenance"]["expected_base_is_ancestor_of_head"]:
# C873SRC 001693|        failures.append("provenance:expected base is not an ancestor of HEAD")
# C873SRC 001694|    if report["provenance"]["primary_source_hash_mismatches"]:
# C873SRC 001695|        failures.append("provenance:primary source hash mismatch")
# C873SRC 001696|    primitive = report["primitive"]
# C873SRC 001697|    for key in ("clean_target_column_residual", "unchanged_full_Toffoli_residual", "Fredkin_residual"):
# C873SRC 001698|        if primitive[key] > TOL:
# C873SRC 001699|            failures.append(f"primitive:{key}")
# C873SRC 001700|    if primitive["inactive_remaining_clean_target_primitive_deletions"]:
# C873SRC 001701|        failures.append("primitive:inactive reduced-word deletion")
# C873SRC 001702|    for row in report["semantics"]:
# C873SRC 001703|        for key in ("basis_failures", "scratch_cleanup_failures", "pointer_failures", "typed_G_failures"):
# C873SRC 001704|            if row[key]:
# C873SRC 001705|                failures.append(f"alpha{row['alpha']}:{key}")
# C873SRC 001706|        if row["distinct_output_columns"] != 68:
# C873SRC 001707|            failures.append(f"alpha{row['alpha']}:isometry")
# C873SRC 001708|        for key in ("coherent_forward_residual_with_formal_seam_scalar", "coherent_inverse_residual"):
# C873SRC 001709|            if row[key] > TOL:
# C873SRC 001710|                failures.append(f"alpha{row['alpha']}:{key}")
# C873SRC 001711|    if report["semantic_mutations"]["inactive_component_mutations"]:
# C873SRC 001712|        failures.append("semantic:inactive component mutation")
# C873SRC 001713|    recurrence = report["persistent_recurrence"]
# C873SRC 001714|    for key in (
# C873SRC 001715|        "F17_only_two_epoch_failures", "F17_only_two_epoch_work_cleanup_failures",
# C873SRC 001716|        "F17_only_eight_epoch_failures",
# C873SRC 001717|    ):
# C873SRC 001718|        if recurrence[key]:
# C873SRC 001719|            failures.append(f"recurrence:{key}")
# C873SRC 001720|    unary = report["unary_projector"]
# C873SRC 001721|    for key in ("one_hot_mapping_failures", "all_sector_Hamming_weight_failures", "all_sector_inverse_failures", "P1_commutator_failures"):
# C873SRC 001722|        if unary[key]:
# C873SRC 001723|            failures.append(f"unary:{key}")
# C873SRC 001724|    if unary["inactive_deleted_Fredkins"]:
# C873SRC 001725|        failures.append("unary:inactive Fredkin deletion")
# C873SRC 001726|    history = report["computational_basis_path_history_witness"]
# C873SRC 001727|    if not (
# C873SRC 001728|        history["same_endpoint_divergence"]
# C873SRC 001729|        and history["upper_G_matches_initial"]
# C873SRC 001730|        and history["lower_G_matches_initial"]
# C873SRC 001731|        and history["joint_F17_history_inner_product"] == 0
# C873SRC 001732|    ):
# C873SRC 001733|        failures.append("computational-basis path-history witness")
# C873SRC 001734|    signed = report["signed_transport"]
# C873SRC 001735|    for key in ("signed_law_failures", "typed_family_transport_failures", "ordered_product_failures"):
# C873SRC 001736|        if signed[key]:
# C873SRC 001737|            failures.append(f"signed:{key}")
# C873SRC 001738|    for key in (
# C873SRC 001739|        "negative_frame_endpoint_swap_omission_detected_rows",
# C873SRC 001740|        "negative_frame_rail_k_to_minus_k_omission_detected_rows",
# C873SRC 001741|        "negative_frame_spurious_alpha_family_flip_detected_rows",
# C873SRC 001742|    ):
# C873SRC 001743|        if not signed[key]:
# C873SRC 001744|            failures.append(f"signed:inactive {key}")
# C873SRC 001745|    for fixture in report["fixtures"]:
# C873SRC 001746|        prefix = str(tuple(fixture["shape"]))
# C873SRC 001747|        for key in (
# C873SRC 001748|            "baseline_partition_failure", "selected_factor_match_failures",
# C873SRC 001749|            "scheduled_missing_seams", "scheduled_duplicate_seams",
# C873SRC 001750|            "noncommuting_order_failures", "same_axis_parity_rotation_anticommutators",
# C873SRC 001751|            "F17_only_added_instruction_census_failures", "F17_only_route_failures",
# C873SRC 001752|            "alpha_plus_minus_route_census_failures",
# C873SRC 001753|            "F17_only_same_color_route_footprint_collisions",
# C873SRC 001754|            "envelope_width_failures_at_pitch32", "F17_only_bank_pair_overlap_pairs",
# C873SRC 001755|            "F17_only_bank_pair_overlap_sites",
# C873SRC 001756|            "F17_only_bank_carrier_aux_collision_sites",
# C873SRC 001757|            "endpoint_B_physical_constraint_anticommutators",
# C873SRC 001758|            "single_rail_role_removal_census_failures",
# C873SRC 001759|        ):
# C873SRC 001760|            if fixture[key]:
# C873SRC 001761|                failures.append(f"{prefix}:{key}")
# C873SRC 001762|        if fixture["F17_only_all_seam_bank_union_M2"] != fixture["F17_only_expected_all_seam_bank_union_M2"]:
# C873SRC 001763|            failures.append(f"{prefix}:F17-only bank union census")
# C873SRC 001764|        for label in ("A_F17_only",):
# C873SRC 001765|            ledger = fixture["augmented_epoch_ledgers"][label]
# C873SRC 001766|            if ledger["complete_epoch_non_NN_or_return_failures"]:
# C873SRC 001767|                failures.append(f"{prefix}:{label}:complete epoch route")
# C873SRC 001768|            if ledger["factor_order_reconstruction_failures"]:
# C873SRC 001769|                failures.append(f"{prefix}:{label}:factor order")
# C873SRC 001770|            if any(len(ledger[key]) != 64 for key in (
# C873SRC 001771|                "retained_nonseam_word_sha256", "seam_stage_schedule_sha256",
# C873SRC 001772|                "complete_epoch_logical_word_sha256", "complete_epoch_routed_schedule_sha256",
# C873SRC 001773|            )):
# C873SRC 001774|                failures.append(f"{prefix}:{label}:digest")
# C873SRC 001775|        for key in (
# C873SRC 001776|            "abstract_update_preservation_failures", "physical_update_preservation_failures",
# C873SRC 001777|        ):
# C873SRC 001778|            if fixture["C870_constraint_certificate"][key]:
# C873SRC 001779|                failures.append(f"{prefix}:C870 constraints:{key}")
# C873SRC 001780|        if any(fixture["stage_abstract_Gauss_preservation_failures"].values()):
# C873SRC 001781|            failures.append(f"{prefix}:stage Gauss preservation")
# C873SRC 001782|        if fixture["bank_radius"] != 2:
# C873SRC 001783|            failures.append(f"{prefix}:bank radius")
# C873SRC 001784|        if fixture["F17_only_naive_axis_only_route_footprint_collisions"] == 0:
# C873SRC 001785|            failures.append(f"{prefix}:inactive schedule collision control")
# C873SRC 001786|        if fixture["inactive_schedule_color_deletions"]:
# C873SRC 001787|            failures.append(f"{prefix}:inactive schedule deletion")
# C873SRC 001788|        if fixture["phase"]["maximum_raw_square_to_minus_identity_residual"] > TOL:
# C873SRC 001789|            failures.append(f"{prefix}:raw seam phase")
# C873SRC 001790|        if abs(fixture["phase"]["maximum_raw_square_to_identity_residual"] - 2.0) > TOL:
# C873SRC 001791|            failures.append(f"{prefix}:inactive raw-square phase control")
# C873SRC 001792|        if fixture["phase"]["maximum_formal_corrected_residual"] > TOL:
# C873SRC 001793|            failures.append(f"{prefix}:formal seam scalar")
# C873SRC 001794|    covariance = report["coordinate_covariance"]
# C873SRC 001795|    for key in (
# C873SRC 001796|        "frame_route_path_failures", "frame_bank_failures", "signature_product_failures",
# C873SRC 001797|        "path_product_failures", "bank_product_failures", "color_frame_failures",
# C873SRC 001798|        "color_product_failures",
# C873SRC 001799|    ):
# C873SRC 001800|        if covariance[key]:
# C873SRC 001801|            failures.append(f"covariance:{key}")
# C873SRC 001802|    route = report["structural_route_deletions"]
# C873SRC 001803|    for key in ("undetected_structural_deletions", "full_operand_failures", "full_arbitrary_register_return_failures"):
# C873SRC 001804|        if route[key]:
# C873SRC 001805|            failures.append(f"route:{key}")
# C873SRC 001806|    return failures
# C873SRC 001807|
# C873SRC 001808|
# C873SRC 001809|def collect_secondary_optional_failures(report):
# C873SRC 001810|    """Diagnostics intentionally excluded from the F17-only closure."""
# C873SRC 001811|    failures = []
# C873SRC 001812|    if report["provenance"]["secondary_optional_source_hash_mismatches"]:
# C873SRC 001813|        failures.append("provenance:secondary optional source hash mismatch")
# C873SRC 001814|    recurrence = report["persistent_recurrence"]
# C873SRC 001815|    if not recurrence["coexistence_second_epoch_without_packet_blank_detected_columns"]:
# C873SRC 001816|        failures.append("coexistence:inactive packet freshness control")
# C873SRC 001817|    packet = report["secondary_optional_evidence"]["Cycle714_coexistence"]
# C873SRC 001818|    for key in (
# C873SRC 001819|        "independent_packet_failures", "packet_inverse_failures",
# C873SRC 001820|        "packet_work_cleanup_failures", "retained_pointer_failures",
# C873SRC 001821|    ):
# C873SRC 001822|        if packet[key]:
# C873SRC 001823|            failures.append(f"Cycle714:{key}")
# C873SRC 001824|    for fixture in report["fixtures"]:
# C873SRC 001825|        prefix = str(tuple(fixture["shape"]))
# C873SRC 001826|        for key in (
# C873SRC 001827|            "route_failures", "same_color_route_footprint_collisions",
# C873SRC 001828|            "bank_pair_overlap_pairs", "bank_pair_overlap_sites",
# C873SRC 001829|            "bank_carrier_aux_collision_sites",
# C873SRC 001830|            "persistent_rail_packet_collision_sites", "shared_role_alias_failures",
# C873SRC 001831|            "packet_entry_work_failures",
# C873SRC 001832|            "single_packet_site_role_removal_census_failures",
# C873SRC 001833|            "current_to_pointer_alias_collision_mutation_undetected",
# C873SRC 001834|            "coexistence_added_instruction_census_failures",
# C873SRC 001835|        ):
# C873SRC 001836|            if fixture[key]:
# C873SRC 001837|                failures.append(f"{prefix}:optional:{key}")
# C873SRC 001838|        if fixture["all_seam_bank_union_M2"] != fixture["expected_all_seam_bank_union_M2"]:
# C873SRC 001839|            failures.append(f"{prefix}:optional:bank union census")
# C873SRC 001840|        ledger = fixture["augmented_epoch_ledgers"]["B_F17_plus_Cycle714"]
# C873SRC 001841|        if ledger["complete_epoch_non_NN_or_return_failures"]:
# C873SRC 001842|            failures.append(f"{prefix}:optional:complete epoch route")
# C873SRC 001843|        if ledger["factor_order_reconstruction_failures"]:
# C873SRC 001844|            failures.append(f"{prefix}:optional:factor order")
# C873SRC 001845|    return failures
# C873SRC 001846|
# C873SRC 001847|
# C873SRC 001848|def main(output: Path = OUT) -> int:
# C873SRC 001849|    observed_hashes = {path: digest(ROOT / path) for path in SOURCE_PATHS}
# C873SRC 001850|    mismatches = {
# C873SRC 001851|        path: {"expected": EXPECTED_SOURCE_SHA256[path], "observed": observed_hashes[path]}
# C873SRC 001852|        for path in SOURCE_PATHS if observed_hashes[path] != EXPECTED_SOURCE_SHA256[path]
# C873SRC 001853|    }
# C873SRC 001854|    primary_mismatches = {
# C873SRC 001855|        path: mismatches[path] for path in PRIMARY_SOURCE_PATHS if path in mismatches
# C873SRC 001856|    }
# C873SRC 001857|    secondary_mismatches = {
# C873SRC 001858|        path: mismatches[path]
# C873SRC 001859|        for path in SECONDARY_OPTIONAL_SOURCE_PATHS if path in mismatches
# C873SRC 001860|    }
# C873SRC 001861|    base_is_ancestor = subprocess.run(
# C873SRC 001862|        (
# C873SRC 001863|            "git", "merge-base", "--is-ancestor",
# C873SRC 001864|            EXPECTED_BASE_COMMIT, "HEAD",
# C873SRC 001865|        ),
# C873SRC 001866|        cwd=ROOT,
# C873SRC 001867|        check=False,
# C873SRC 001868|    ).returncode == 0
# C873SRC 001869|    catalog = {"paths": set(), "signatures": set(), "banks": set()}
# C873SRC 001870|    fixtures = tuple(fixture_certificate(shape, catalog) for shape in SHAPES)
# C873SRC 001871|    maximum_distance = max(row["maximum_route_distance"] for row in fixtures)
# C873SRC 001872|    report = {
# C873SRC 001873|        "status": "pending",
# C873SRC 001874|        "name": "Cycle873 recurrent F17-only all-seam physical core",
# C873SRC 001875|        "claim_scope": (
# C873SRC 001876|            "all landed directed seams on L2, L3, and held noncubic 3x2x2; supplied "
# C873SRC 001877|            "lawful matter, one-hot F17 banks, typed family/polarity, "
# C873SRC 001878|            "coframes, parity origin, ordered color traversal, recurrence invocation, "
# C873SRC 001879|            "and returned-route substrate"
# C873SRC 001880|        ),
# C873SRC 001881|        "provenance": {
# C873SRC 001882|            "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 001883|            "expected_base_is_ancestor_of_head": base_is_ancestor,
# C873SRC 001884|            "source_sha256": observed_hashes,
# C873SRC 001885|            "source_hash_mismatches": mismatches,
# C873SRC 001886|            "primary_source_hash_mismatches": primary_mismatches,
# C873SRC 001887|            "secondary_optional_source_hash_mismatches": secondary_mismatches,
# C873SRC 001888|            "runner": str(Path(__file__).relative_to(ROOT)),
# C873SRC 001889|        },
# C873SRC 001890|        "register_join": {
# C873SRC 001891|            "live_packet_M2": C714.N,
# C873SRC 001892|            "F17_roles": 20,
# C873SRC 001893|            "intentional_shared_packet_work_roles": 3,
# C873SRC 001894|            "new_persistent_F17_rails": F17,
# C873SRC 001895|            "combined_bank_M2": C714.N + F17,
# C873SRC 001896|            "local_alias_offsets": {
# C873SRC 001897|                "q_u_q56": (0, 1, 0),
# C873SRC 001898|                "q_v_q57": (0, -1, 0),
# C873SRC 001899|                "current_q58": (-2, 1, 1),
# C873SRC 001900|                "pointer_q44": (0, 0, 1),
# C873SRC 001901|            },
# C873SRC 001902|            "rail_local_offsets": RAIL_LOCAL_OFFSETS,
# C873SRC 001903|            "constant_radius": 2,
# C873SRC 001904|        },
# C873SRC 001905|        "objects": {
# C873SRC 001906|            "A_F17_only_recurrent_augmentation": {
# C873SRC 001907|                "persistent_bank_M2_per_seam": 20,
# C873SRC 001908|                "added_instructions_excluding_landed_seam": 634,
# C873SRC 001909|                "clean_returned_work_M2": 3,
# C873SRC 001910|                "packet_or_Cycle612_interface": False,
# C873SRC 001911|                "fresh_packet_or_address_required_per_epoch": False,
# C873SRC 001912|                "spectrum_status": (
# C873SRC 001913|                    "open for basis-link initialization; uniform cycle-space repair is not "
# C873SRC 001914|                    "excluded by the path-history witness"
# C873SRC 001915|                ),
# C873SRC 001916|            },
# C873SRC 001917|            "secondary_optional_B_F17_plus_unchanged_Cycle714_coexistence": {
# C873SRC 001918|                "combined_bank_M2_per_seam": 76,
# C873SRC 001919|                "incremental_M2_beyond_live_packet": 17,
# C873SRC 001920|                "added_instructions_excluding_landed_seam_and_packet": 636,
# C873SRC 001921|                "unchanged_packet_instructions": 718,
# C873SRC 001922|                "Cycle612_packet_interface_retained": True,
# C873SRC 001923|                "fresh_blank_packet_required_per_invocation": True,
# C873SRC 001924|            },
# C873SRC 001925|        },
# C873SRC 001926|        "factor_level_proof": {
# C873SRC 001927|            "literal_emitted_order": (
# C873SRC 001928|                "endpoint B extraction -> landed four-rotation seam factor -> "
# C873SRC 001929|                "mutually exclusive positive/negative predicate-controlled unary "
# C873SRC 001930|                "shifts -> endpoint cleanup"
# C873SRC 001931|            ),
# C873SRC 001932|            "landed_seam_phase": (
# C873SRC 001933|                "the four commuting pi/2 rotations emit raw -i*FSWAP; the formal "
