#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 affine source, part 3/3."""

TARGET_SOURCE = "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py"
PART_ORDINAL = 3
PART_COUNT = 3
FIRST_SOURCE_LINE = 1039
LAST_SOURCE_LINE = 1118
TOTAL_SOURCE_LINES = 1118
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 001039|    failures.append("filled plaquette direct intertwiner")
# C873SRC 001040|if result["filled_plaquette"]["four_factor_sequence_max_residual"] > TOL:
# C873SRC 001041|    failures.append("filled plaquette loop sequence")
# C873SRC 001042|if result["filled_plaquette"]["uniform_closed_loop_residual"] > TOL:
# C873SRC 001043|    failures.append("trivial-character loop")
# C873SRC 001044|if result["filled_plaquette"]["basis_link_closed_loop_residual"] <= 1.0:
# C873SRC 001045|    failures.append("inactive basis-link loop control")
# C873SRC 001046|if result["filled_plaquette"]["nonuniform_character_closed_loop_residual"] <= 0.3:
# C873SRC 001047|    failures.append("inactive nontrivial-character control")
# C873SRC 001048|if result["open_cube_L2"][
# C873SRC 001049|    "repeated_uniform_intertwiner_incidence_failures"
# C873SRC 001050|]:
# C873SRC 001051|    failures.append("L2 repeated intertwiner")
# C873SRC 001052|if result["open_cube_L2"]["correct_direct_incidence_failures"]:
# C873SRC 001053|    failures.append("L2 direct incidence")
# C873SRC 001054|if result["open_cube_L2"]["repeated_history_kernel_failures"]:
# C873SRC 001055|    failures.append("L2 repeated history kernel")
# C873SRC 001056|if result["open_cube_L2"]["wrong_alpha_active_cases_checked"] == 0:
# C873SRC 001057|    failures.append("inactive wrong-alpha controls")
# C873SRC 001058|if result["open_cube_L2"]["omitted_independent_generator_residual"] <= 1.0:
# C873SRC 001059|    failures.append("inactive omitted plaquette generator control")
# C873SRC 001060|for key in (
# C873SRC 001061|    "coin_unitarity_residual", "QR_reconstruction_residual",
# C873SRC 001062|    "QR_off_diagonal_residual", "trivial_cycle_uniform_normalization_residual",
# C873SRC 001063|    "trivial_cycle_translation_residual",
# C873SRC 001064|    "actual_dense_coin_encoded_onsite_intertwiner_residual",
# C873SRC 001065|    "maximum_Bloch_unitarity_residual",
# C873SRC 001066|    "eight_step_same_block_multiplication_consistency_residual",
# C873SRC 001067|):
# C873SRC 001068|    if C219_CERTIFICATE[key] > TOL:
# C873SRC 001069|        failures.append(f"Cycle219:{key}")
# C873SRC 001070|if C219_CERTIFICATE["selected_active_QR_gate_deletion_residual"] <= 1.0e-3:
# C873SRC 001071|    failures.append("Cycle219:inactive selected QR deletion control")
# C873SRC 001072|if C219_CERTIFICATE["rest_to_analytic_residual"] > TOL:
# C873SRC 001073|    failures.append("Cycle219:rest mass")
# C873SRC 001074|if C219_CERTIFICATE["dispersion_relative_residual"] > 4.0e-6:
# C873SRC 001075|    failures.append("Cycle219:dispersion mass")
# C873SRC 001076|result["active_controls"] = {
# C873SRC 001077|    "wrong_alpha_values": result["open_cube_L2"]["wrong_alpha_values_mod17"],
# C873SRC 001078|    "wrong_alpha_cases": result["open_cube_L2"]["wrong_alpha_active_cases_checked"],
# C873SRC 001079|    "nontrivial_character_residual": result["filled_plaquette"][
# C873SRC 001080|        "nonuniform_character_closed_loop_residual"
# C873SRC 001081|    ],
# C873SRC 001082|    "omitted_independent_generator_residual": result["open_cube_L2"][
# C873SRC 001083|        "omitted_independent_generator_residual"
# C873SRC 001084|    ],
# C873SRC 001085|    "selected_active_QR_gate_deletion_index": C219_CERTIFICATE[
# C873SRC 001086|        "selected_active_QR_gate_deletion_index"
# C873SRC 001087|    ],
# C873SRC 001088|    "selected_active_QR_gate_deletion_residual": C219_CERTIFICATE[
# C873SRC 001089|        "selected_active_QR_gate_deletion_residual"
# C873SRC 001090|    ],
# C873SRC 001091|}
# C873SRC 001092|result["failures"] = failures
# C873SRC 001093|result["status"] = "pass" if not failures else "fail"
# C873SRC 001094|
# C873SRC 001095|
# C873SRC 001096|def finish(output: Path = OUT) -> int:
# C873SRC 001097|    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
# C873SRC 001098|    print(json.dumps({
# C873SRC 001099|        "status": result["status"],
# C873SRC 001100|        "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 001101|        "expected_base_is_ancestor_of_head": EXPECTED_BASE_IS_ANCESTOR_OF_HEAD,
# C873SRC 001102|        "receipt": str(OUT.relative_to(ROOT)),
# C873SRC 001103|        "failures": failures,
# C873SRC 001104|        "filled_plaquette_direct_columns": result["filled_plaquette"][
# C873SRC 001105|            "direct_fswap_columns_checked"
# C873SRC 001106|        ],
# C873SRC 001107|        "L2_repeated_factor_count": result["open_cube_L2"]["repeated_factor_count"],
# C873SRC 001108|        "C219_beta": C219_CERTIFICATE["actual_Cycle870_beta"],
# C873SRC 001109|        "C219_dispersion_mass": C219_CERTIFICATE["dispersion_mass"],
# C873SRC 001110|    }, indent=2, sort_keys=True))
# C873SRC 001111|    return int(bool(failures))
# C873SRC 001112|
# C873SRC 001113|
# C873SRC 001114|if __name__ == "__main__":
# C873SRC 001115|    parser = argparse.ArgumentParser()
# C873SRC 001116|    parser.add_argument("--output", type=Path, default=OUT)
# C873SRC 001117|    arguments = parser.parse_args()
# C873SRC 001118|    raise SystemExit(finish(arguments.output))
