#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 independent source, part 4/4."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.py"
PART_ORDINAL = 4
PART_COUNT = 4
FIRST_SOURCE_LINE = 1397
LAST_SOURCE_LINE = 1546
TOTAL_SOURCE_LINES = 1546
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "02c3f321ba5ef1dce723ed04bd83919839648fd89202f607b6cc680645a97734"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 001397|        "eight_step_encoded_native_matrix_residual":
# C873SRC 001398|            eight_step_encoded_native_residual,
# C873SRC 001399|        "compressed_unitarity_residual": float(np.linalg.norm(compressed.conj().T @ compressed - np.eye(6*length))),
# C873SRC 001400|        "maximum_discrete_Bloch_block_residual": max(fourier_residuals),
# C873SRC 001401|        "maximum_discrete_Bloch_unitarity_residual": max(block_unitarity),
# C873SRC 001402|        "contact_one_particle_target_residual": onsite_star[
# C873SRC 001403|            "contact_one_particle_target_residual"
# C873SRC 001404|        ],
# C873SRC 001405|        "compiled_contact_all_occupation_residual_up_to_phase": contact["maximum_residual_up_to_global_phase"],
# C873SRC 001406|        "onsite_F17_star_preservation": onsite_star,
# C873SRC 001407|        "analytic_mass": float(species.analytic_mass), "rest_mass": float(C219.rest_mass(species)),
# C873SRC 001408|        "dispersion_mass_step_1e-4": dispersion_mass,
# C873SRC 001409|        "dispersion_relative_error": dispersion_mass / float(species.analytic_mass) - 1,
# C873SRC 001410|        "curvature_tensor": curvature.tolist(),
# C873SRC 001411|    }
# C873SRC 001412|
# C873SRC 001413|
# C873SRC 001414|def main():
# C873SRC 001415|    parser = argparse.ArgumentParser(); parser.add_argument("--source-root", type=Path, default=DEFAULT_ROOT); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
# C873SRC 001416|    args = parser.parse_args(); root = args.source_root.resolve()
# C873SRC 001417|    independence = source_ast_certificate(root)
# C873SRC 001418|    C870, C871, C714, C219, C210 = setup_imports(root)
# C873SRC 001419|    pins = {name: sha(root / name) for name in EXPECTED_SOURCE_SHA256}
# C873SRC 001420|    base_is_ancestor = subprocess.run(
# C873SRC 001421|        (
# C873SRC 001422|            "git", "merge-base", "--is-ancestor",
# C873SRC 001423|            EXPECTED_BASE_COMMIT, "HEAD",
# C873SRC 001424|        ),
# C873SRC 001425|        cwd=root,
# C873SRC 001426|        check=False,
# C873SRC 001427|    ).returncode == 0
# C873SRC 001428|    report = {
# C873SRC 001429|        "status": "pending", "schema": "cycle873-recurrent-f17-uniform-affine-open-box-independent-v1",
# C873SRC 001430|        "source_root": ".", "independence": independence,
# C873SRC 001431|        "provenance": {
# C873SRC 001432|            "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 001433|            "expected_base_is_ancestor_of_head": base_is_ancestor,
# C873SRC 001434|            "runner": str(Path(__file__).resolve().relative_to(root)),
# C873SRC 001435|        },
# C873SRC 001436|        "source_sha256": pins,
# C873SRC 001437|        "physical_selected_seam": physical_seam_certificate(C870, C871),
# C873SRC 001438|        "endpoint_extract": extraction_certificate(C870, C871),
# C873SRC 001439|        "reversible_primitives": reversible_primitive_certificate(C714),
# C873SRC 001440|        "effective_encoded_macro": effective_macro_certificate(),
# C873SRC 001441|        "literal_L2_emitted_schedule": emitted_schedule_certificate(root, C870, C871, C714),
# C873SRC 001442|        "repeated_factors": repeated_factor_certificate(),
# C873SRC 001443|        "six_mode_total_occupation_extension": six_mode_count_certificate(),
# C873SRC 001444|        "open_box_local_constraints": local_constraint_certificate(C870, C871),
# C873SRC 001445|        "cycle219_recurrence_dispersion": recurrence_dispersion_certificate(C870, C871, C219, C210),
# C873SRC 001446|        "phase_boundary": (
# C873SRC 001447|            "each raw grouped seam is -i times the augmented FSWAP; only the formal "
# C873SRC 001448|            "+i-corrected grouped macro is exact generally.  Raw seam-stage phases "
# C873SRC 001449|            "depend on the seam count, while the full epoch keeps Cycle870's separate "
# C873SRC 001450|            "ledgered global correction"
# C873SRC 001451|        ),
# C873SRC 001452|    }
# C873SRC 001453|    failures = []
# C873SRC 001454|    if not base_is_ancestor: failures.append("expected base is not an ancestor of HEAD")
# C873SRC 001455|    if independence["primary_sha256"] != PRIMARY_SHA256: failures.append("primary hash")
# C873SRC 001456|    if independence["physical_core_sha256"] != PHYSICAL_CORE_SHA256: failures.append("physical core hash")
# C873SRC 001457|    if independence["physical_receipt_sha256"] != PHYSICAL_RECEIPT_SHA256: failures.append("physical receipt hash")
# C873SRC 001458|    if independence["checker_runtime_imported_primary"]: failures.append("primary imported")
# C873SRC 001459|    if independence["physical_core_imports_cycle873_primary"]: failures.append("physical core imports primary")
# C873SRC 001460|    if not independence["rail_offsets_match"] or not independence["emit_field_order_match"] or independence["emit_required_semantics_missing"]: failures.append("primary AST")
# C873SRC 001461|    if pins != EXPECTED_SOURCE_SHA256: failures.append("source pins")
# C873SRC 001462|    physical = report["physical_selected_seam"]
# C873SRC 001463|    for key in ("compiler_signature_match_failures", "physical_constraint_anticommutators", "physical_lift_pair_homomorphism_failures"):
# C873SRC 001464|        if physical[key]: failures.append("physical:" + key)
# C873SRC 001465|    if physical["maximum_arbitrary_coherent_full_support_compiler_residual"] > TOL: failures.append("physical compiler")
# C873SRC 001466|    if physical["raw_to_minus_i_FSWAP_residual"] > TOL or physical["formal_i_corrected_to_FSWAP_residual"] > TOL: failures.append("seam factorization")
# C873SRC 001467|    if min(physical["four_rotation_deletion_residuals_up_to_global_phase"]) <= 0.1: failures.append("inactive rotation deletion")
# C873SRC 001468|    primitive = report["reversible_primitives"]
# C873SRC 001469|    for key in ("clean_target_reduced_Toffoli_column_residual", "fredkin_residual", "predicate_compute_clean_column_residual", "predicate_uncompute_supplied_column_residual"):
# C873SRC 001470|        if primitive[key] > TOL: failures.append("primitive:" + key)
# C873SRC 001471|    if min(primitive["clean_target_remaining_literal_deletion_residuals"]) <= TOL or min(primitive["fredkin_literal_deletion_residuals_on_onehot_controlled_columns"]) <= TOL or min(primitive["predicate_literal_deletion_residuals"]) <= TOL or min(primitive["uncompute_literal_deletion_residuals"]) <= TOL: failures.append("inactive primitive deletion")
# C873SRC 001472|    schedule_report = report["literal_L2_emitted_schedule"]
# C873SRC 001473|    if not schedule_report["schedule_hash_match"]: failures.append("literal schedule hash")
# C873SRC 001474|    if schedule_report["all_seam_rotation_physical_constraint_anticommutators"] or schedule_report["all_endpoint_B_physical_constraint_anticommutators"] or schedule_report["all_seam_maximum_raw_to_minus_i_FSWAP_residual"] > TOL or schedule_report["all_seam_maximum_formal_corrected_residual"] > TOL: failures.append("all-seam physical algebra")
# C873SRC 001475|    for family in report["effective_encoded_macro"]["families"]:
# C873SRC 001476|        if family["formal_corrected_basis_max_residual"] > TOL or family["formal_corrected_arbitrary_coherent_residual"] > TOL or family["scratch_cleanup_failures"]: failures.append("effective macro")
# C873SRC 001477|        if any(not row["changed_columns"] for row in family["component_mutations"].values()): failures.append("inactive macro component")
# C873SRC 001478|    repeated = report["repeated_factors"]
# C873SRC 001479|    if repeated["plaquette_four_raw_factor_max_residual"] > TOL or repeated["open_L2_incidence_failures"] or repeated["open_L2_repeated_uniform_intertwiner_failures"]: failures.append("repeated factors")
# C873SRC 001480|    if repeated["supplied_background_variant_columns"] != 192 or repeated["supplied_background_variant_max_residual"] > TOL: failures.append("fixed-star background variants")
# C873SRC 001481|    six_mode = report["six_mode_total_occupation_extension"]
# C873SRC 001482|    if (
# C873SRC 001483|        six_mode["rows"] != 2448
# C873SRC 001484|        or six_mode["FSWAP_minus_11_rows"] != 612
# C873SRC 001485|        or any(six_mode[key] for key in (
# C873SRC 001486|            "incidence_failures", "fixed_background_or_star_invariance_failures",
# C873SRC 001487|            "occupation_range_failures", "FSWAP_sign_failures",
# C873SRC 001488|        ))
# C873SRC 001489|        or six_mode["wrong_incidence_sign_detected_rows"] != 1224
# C873SRC 001490|        or six_mode["omitted_link_shift_detected_rows"] != 1224
# C873SRC 001491|    ): failures.append("six-mode total occupation extension")
# C873SRC 001492|    expected_stage_phases = {
# C873SRC 001493|        (2, 2, 2): [1.0, 0.0],
# C873SRC 001494|        (3, 3, 3): [-1.0, 0.0],
# C873SRC 001495|        (3, 2, 2): [1.0, 0.0],
# C873SRC 001496|    }
# C873SRC 001497|    if any(
# C873SRC 001498|        row["phase"] != expected_stage_phases[tuple(row["shape"])]
# C873SRC 001499|        for row in repeated["open_box_one_seam_stage_raw_phases"]
# C873SRC 001500|    ): failures.append("open-box raw seam-stage phase")
# C873SRC 001501|    local = report["open_box_local_constraints"]
# C873SRC 001502|    expected_local = {
# C873SRC 001503|        (2, 2, 2): (8, 12, 6, 5, 72),
# C873SRC 001504|        (3, 3, 3): (27, 54, 36, 28, 126),
# C873SRC 001505|        (3, 2, 2): (12, 20, 11, 9, 90),
# C873SRC 001506|    }
# C873SRC 001507|    for row in local["fixtures"]:
# C873SRC 001508|        shape = tuple(row["shape"]); V, E, Pn, beta, star = expected_local[shape]
# C873SRC 001509|        if (row["vertices"], row["oriented_links"], row["plaquettes"], row["cycle_space_rank"], row["maximum_star_support_M2"]) != (V, E, Pn, beta, star): failures.append("local constraint census")
# C873SRC 001510|        if row["incidence_rank_mod17"] != V - 1 or row["plaquette_boundary_rank_mod17"] != beta or row["uniform_plus_one_dimension"] != 1: failures.append("local constraint rank")
# C873SRC 001511|        if any(row[key] for key in ("boundary_of_boundary_nonzero_entries", "onehot_path_failures", "rail_pair_overlap_sites", "rail_carrier_aux_collision_sites", "plaquette_word_or_NN_failures", "plaquette_layer_collisions")): failures.append("local constraint physical")
# C873SRC 001512|        if row["plaquette_support_M2"] != 68: failures.append("plaquette support")
# C873SRC 001513|    if local["proper_frames"] != 24 or local["ordered_frame_products"] != 576: failures.append("local frames")
# C873SRC 001514|    if local["plaquette_SWAP_deletions_tested"] != 3392 or local["undetected_plaquette_SWAP_deletions"]: failures.append("local deletion controls")
# C873SRC 001515|    recurrence = report["cycle219_recurrence_dispersion"]
# C873SRC 001516|    if (
# C873SRC 001517|        recurrence["coin_reverse_seam_contact_intertwiner_max_residual"] > TOL
# C873SRC 001518|        or recurrence["compressed_native_matrix_residual"] > TOL
# C873SRC 001519|        or recurrence["eight_step_encoded_native_matrix_residual"] > TOL
# C873SRC 001520|        or recurrence["maximum_discrete_Bloch_block_residual"] > TOL
# C873SRC 001521|    ): failures.append("Cycle219 recurrence")
# C873SRC 001522|    if tuple(recurrence["C870_factor_stage_order"]) != ("coin", "reverse", "seam", "contact") or recurrence["onsite_reverse_helper_permutation_residual"] > TOL: failures.append("Cycle870 stage grammar")
# C873SRC 001523|    onsite_star = recurrence["onsite_F17_star_preservation"]
# C873SRC 001524|    if (
# C873SRC 001525|        any(value > TOL for value in onsite_star["star_clock_commutator_residuals"].values())
# C873SRC 001526|        or any(value > TOL for value in onsite_star["unitarity_residuals"].values())
# C873SRC 001527|        or onsite_star["contact_one_particle_target_residual"] > TOL
# C873SRC 001528|        or onsite_star["bare_occupation_flip_control_commutator"] <= 1.0e-3
# C873SRC 001529|    ): failures.append("onsite F17 star preservation")
# C873SRC 001530|    report["failures"] = failures; report["status"] = "pass" if not failures else "fail"
# C873SRC 001531|    output = args.output; output.write_text(json.dumps(report, indent=2, sort_keys=True, default=lambda x: x.item() if isinstance(x, np.generic) else list(x) if isinstance(x, tuple) else str(x)) + "\n")
# C873SRC 001532|    print(json.dumps({
# C873SRC 001533|        "status": report["status"],
# C873SRC 001534|        "base_commit": report["provenance"]["base_commit"],
# C873SRC 001535|        "expected_base_is_ancestor_of_head": report["provenance"]["expected_base_is_ancestor_of_head"],
# C873SRC 001536|        "receipt": str(DEFAULT_OUTPUT.relative_to(DEFAULT_ROOT)),
# C873SRC 001537|        "failures": failures,
# C873SRC 001538|        "primary_imported": independence["checker_runtime_imported_primary"],
# C873SRC 001539|        "physical_raw_to_minus_i_residual": report["physical_selected_seam"]["raw_to_minus_i_FSWAP_residual"],
# C873SRC 001540|        "C219_dispersion_mass": report["cycle219_recurrence_dispersion"]["dispersion_mass_step_1e-4"],
# C873SRC 001541|    }, indent=2, sort_keys=True))
# C873SRC 001542|    return int(bool(failures))
# C873SRC 001543|
# C873SRC 001544|
# C873SRC 001545|if __name__ == "__main__":
# C873SRC 001546|    raise SystemExit(main())
