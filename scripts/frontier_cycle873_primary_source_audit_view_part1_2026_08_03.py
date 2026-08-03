#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 primary source, part 1/1."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 1
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 491
TOTAL_SOURCE_LINES = 491
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "ab9f365c167b8fafb4f54508c0fb38b325bf687fdf8f222bc9aa833ad65dfc62"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000001|#!/usr/bin/env python3
# C873SRC 000002|"""Cycle873 primary runner for the bounded recurrent F17 open-box package."""
# C873SRC 000003|
# C873SRC 000004|from __future__ import annotations
# C873SRC 000005|
# C873SRC 000006|import argparse
# C873SRC 000007|from hashlib import sha256
# C873SRC 000008|import json
# C873SRC 000009|from pathlib import Path
# C873SRC 000010|import subprocess
# C873SRC 000011|import sys
# C873SRC 000012|import tempfile
# C873SRC 000013|
# C873SRC 000014|
# C873SRC 000015|ROOT = Path(__file__).resolve().parents[1]
# C873SRC 000016|OUT = ROOT / "outputs/cycle873_recurrent_f17_uniform_affine_open_box_primary_receipt_2026_08_03.json"
# C873SRC 000017|EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
# C873SRC 000018|TOL = 3.0e-10
# C873SRC 000019|
# C873SRC 000020|CHILDREN = {
# C873SRC 000021|    "physical": {
# C873SRC 000022|        "source": "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py",
# C873SRC 000023|        "receipt": "outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json",
# C873SRC 000024|        "sha256": "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7",
# C873SRC 000025|    },
# C873SRC 000026|    "constraints": {
# C873SRC 000027|        "source": "scripts/frontier_cycle873_f17_open_box_local_constraints_core_2026_08_03.py",
# C873SRC 000028|        "receipt": "outputs/cycle873_f17_open_box_local_constraints_core_receipt_2026_08_03.json",
# C873SRC 000029|        "sha256": "70d7362a2f534bd94b5b421f38e0c0509483ed8c1962b83f21f790b4c1dcb685",
# C873SRC 000030|    },
# C873SRC 000031|    "affine": {
# C873SRC 000032|        "source": "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py",
# C873SRC 000033|        "receipt": "outputs/cycle873_uniform_affine_gauss_intertwiner_core_receipt_2026_08_03.json",
# C873SRC 000034|        "sha256": "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9",
# C873SRC 000035|    },
# C873SRC 000036|}
# C873SRC 000037|
# C873SRC 000038|EXPECTED_FIXTURES = {
# C873SRC 000039|    (2, 2, 2): {
# C873SRC 000040|        "V": 8, "E": 12, "P": 6, "cycle_rank": 5,
# C873SRC 000041|        "bank": 240, "logical": 24656, "routed": 204288, "depth": 204288,
# C873SRC 000042|    },
# C873SRC 000043|    (3, 3, 3): {
# C873SRC 000044|        "V": 27, "E": 54, "P": 36, "cycle_rank": 28,
# C873SRC 000045|        "bank": 1080, "logical": 95274, "routed": 842762, "depth": 688998,
# C873SRC 000046|    },
# C873SRC 000047|    (3, 2, 2): {
# C873SRC 000048|        "V": 12, "E": 20, "P": 11, "cycle_rank": 9,
# C873SRC 000049|        "bank": 400, "logical": 38740, "routed": 335316, "depth": 317116,
# C873SRC 000050|    },
# C873SRC 000051|}
# C873SRC 000052|
# C873SRC 000053|
# C873SRC 000054|def file_sha256(path: Path) -> str:
# C873SRC 000055|    return sha256(path.read_bytes()).hexdigest()
# C873SRC 000056|
# C873SRC 000057|
# C873SRC 000058|def load_json(path: Path) -> dict:
# C873SRC 000059|    return json.loads(path.read_text(encoding="utf-8"))
# C873SRC 000060|
# C873SRC 000061|
# C873SRC 000062|def cold_children() -> tuple[dict, dict, list[str]]:
# C873SRC 000063|    reports = {}
# C873SRC 000064|    runs = {}
# C873SRC 000065|    failures: list[str] = []
# C873SRC 000066|    with tempfile.TemporaryDirectory(prefix="cycle873-primary-") as temporary:
# C873SRC 000067|        temporary_root = Path(temporary)
# C873SRC 000068|        for label, row in CHILDREN.items():
# C873SRC 000069|            source = ROOT / row["source"]
# C873SRC 000070|            canonical = ROOT / row["receipt"]
# C873SRC 000071|            fresh = temporary_root / f"{label}.json"
# C873SRC 000072|            process = subprocess.run(
# C873SRC 000073|                (sys.executable, "-B", str(source), "--output", str(fresh)),
# C873SRC 000074|                cwd=temporary_root,
# C873SRC 000075|                capture_output=True,
# C873SRC 000076|                text=True,
# C873SRC 000077|                check=False,
# C873SRC 000078|                env={**__import__("os").environ, "PYTHONDONTWRITEBYTECODE": "1"},
# C873SRC 000079|            )
# C873SRC 000080|            canonical_bytes = canonical.read_bytes() if canonical.is_file() else b""
# C873SRC 000081|            fresh_bytes = fresh.read_bytes() if fresh.is_file() else b""
# C873SRC 000082|            runs[label] = {
# C873SRC 000083|                "returncode": process.returncode,
# C873SRC 000084|                "stdout": process.stdout,
# C873SRC 000085|                "stdout_sha256": sha256(process.stdout.encode()).hexdigest(),
# C873SRC 000086|                "stderr": process.stderr,
# C873SRC 000087|                "fresh_receipt_sha256": sha256(fresh_bytes).hexdigest(),
# C873SRC 000088|                "canonical_receipt_sha256": sha256(canonical_bytes).hexdigest(),
# C873SRC 000089|                "byte_identical_to_canonical": fresh_bytes == canonical_bytes,
# C873SRC 000090|            }
# C873SRC 000091|            if process.returncode:
# C873SRC 000092|                failures.append(f"{label}:cold return code")
# C873SRC 000093|            if process.stderr:
# C873SRC 000094|                failures.append(f"{label}:cold stderr")
# C873SRC 000095|            if not fresh_bytes:
# C873SRC 000096|                failures.append(f"{label}:missing cold receipt")
# C873SRC 000097|                continue
# C873SRC 000098|            if fresh_bytes != canonical_bytes:
# C873SRC 000099|                failures.append(f"{label}:cold receipt drift")
# C873SRC 000100|            reports[label] = json.loads(fresh_bytes)
# C873SRC 000101|    return reports, runs, failures
# C873SRC 000102|
# C873SRC 000103|
# C873SRC 000104|def build_report() -> tuple[dict, list[str]]:
# C873SRC 000105|    failures: list[str] = []
# C873SRC 000106|    base_is_ancestor = subprocess.run(
# C873SRC 000107|        (
# C873SRC 000108|            "git", "merge-base", "--is-ancestor",
# C873SRC 000109|            EXPECTED_BASE_COMMIT, "HEAD",
# C873SRC 000110|        ),
# C873SRC 000111|        cwd=ROOT,
# C873SRC 000112|        check=False,
# C873SRC 000113|    ).returncode == 0
# C873SRC 000114|    if not base_is_ancestor:
# C873SRC 000115|        failures.append("expected base is not an ancestor of HEAD")
# C873SRC 000116|
# C873SRC 000117|    source_hashes = {
# C873SRC 000118|        row["source"]: file_sha256(ROOT / row["source"])
# C873SRC 000119|        for row in CHILDREN.values()
# C873SRC 000120|    }
# C873SRC 000121|    source_mismatches = {
# C873SRC 000122|        label: {
# C873SRC 000123|            "expected": row["sha256"],
# C873SRC 000124|            "observed": source_hashes[row["source"]],
# C873SRC 000125|        }
# C873SRC 000126|        for label, row in CHILDREN.items()
# C873SRC 000127|        if source_hashes[row["source"]] != row["sha256"]
# C873SRC 000128|    }
# C873SRC 000129|    if source_mismatches:
# C873SRC 000130|        failures.append("child source hash mismatch")
# C873SRC 000131|
# C873SRC 000132|    reports, cold_runs, cold_failures = cold_children()
# C873SRC 000133|    failures.extend(cold_failures)
# C873SRC 000134|    for label in CHILDREN:
# C873SRC 000135|        if label not in reports:
# C873SRC 000136|            continue
# C873SRC 000137|        if reports[label].get("status") != "pass" or reports[label].get("failures"):
# C873SRC 000138|            failures.append(f"{label}:child status")
# C873SRC 000139|        child_provenance = reports[label].get("provenance", {})
# C873SRC 000140|        if child_provenance.get("base_commit") != EXPECTED_BASE_COMMIT:
# C873SRC 000141|            failures.append(f"{label}:base commit")
# C873SRC 000142|        if not child_provenance.get("expected_base_is_ancestor_of_head"):
# C873SRC 000143|            failures.append(f"{label}:base ancestry")
# C873SRC 000144|
# C873SRC 000145|    if set(reports) != set(CHILDREN):
# C873SRC 000146|        report = {
# C873SRC 000147|            "status": "fail", "failures": failures,
# C873SRC 000148|            "provenance": {
# C873SRC 000149|                "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 000150|                "expected_base_is_ancestor_of_head": base_is_ancestor,
# C873SRC 000151|            },
# C873SRC 000152|            "cold_runs": cold_runs,
# C873SRC 000153|        }
# C873SRC 000154|        return report, failures
# C873SRC 000155|
# C873SRC 000156|    physical = reports["physical"]
# C873SRC 000157|    constraints = reports["constraints"]
# C873SRC 000158|    affine = reports["affine"]
# C873SRC 000159|    physical_by_shape = {
# C873SRC 000160|        tuple(row["shape"]): row for row in physical["fixtures"]
# C873SRC 000161|    }
# C873SRC 000162|    constraint_by_shape = {
# C873SRC 000163|        tuple(row["shape"]): row for row in constraints["fixtures"]
# C873SRC 000164|    }
# C873SRC 000165|    fixture_rows = []
# C873SRC 000166|    for shape, expected in EXPECTED_FIXTURES.items():
# C873SRC 000167|        prow = physical_by_shape.get(shape)
# C873SRC 000168|        crow = constraint_by_shape.get(shape)
# C873SRC 000169|        if prow is None or crow is None:
# C873SRC 000170|            failures.append(f"{shape}:missing fixture")
# C873SRC 000171|            continue
# C873SRC 000172|        ledger = prow["augmented_epoch_ledgers"]["A_F17_only"]
# C873SRC 000173|        checks = {
# C873SRC 000174|            "vertices": crow["vertices"] == expected["V"],
# C873SRC 000175|            "links_equal_seams": crow["oriented_links"] == prow["seams"] == expected["E"],
# C873SRC 000176|            "plaquettes": crow["plaquettes"] == expected["P"],
# C873SRC 000177|            "cycle_rank": crow["cycle_space_rank"] == expected["cycle_rank"],
# C873SRC 000178|            "plaquette_span": crow["plaquette_boundary_rank_mod17"] == expected["cycle_rank"],
# C873SRC 000179|            "unique_uniform_plus_sector": crow["uniform_cycle_plus_one_sector_dimension"] == 1,
# C873SRC 000180|            "bank": prow["F17_only_all_seam_bank_union_M2"] == expected["bank"],
# C873SRC 000181|            "logical": ledger["complete_epoch_logical_instructions"] == expected["logical"],
# C873SRC 000182|            "routed": ledger["complete_epoch_routed_NN_gates"] == expected["routed"],
# C873SRC 000183|            "depth": ledger["complete_epoch_fixed_routed_depth"] == expected["depth"],
# C873SRC 000184|            "factor_order": ledger["factor_order_reconstruction_failures"] == 0,
# C873SRC 000185|            "routes": ledger["complete_epoch_non_NN_or_return_failures"] == 0,
# C873SRC 000186|            "raw_stage_phase": [
# C873SRC 000187|                float(((-1j) ** prow["seams"]).real),
# C873SRC 000188|                float(((-1j) ** prow["seams"]).imag),
# C873SRC 000189|            ] == ([-1.0, 0.0] if shape == (3, 3, 3) else [1.0, 0.0]),
# C873SRC 000190|            "constraint_preservation": constraints["Object_A_preservation"][
# C873SRC 000191|                "full_augmented_epoch_constraint_preservation_failures"
# C873SRC 000192|            ] == 0,
# C873SRC 000193|        }
# C873SRC 000194|        failures.extend(
# C873SRC 000195|            f"{shape}:{name}" for name, passed in checks.items() if not passed
# C873SRC 000196|        )
# C873SRC 000197|        fixture_rows.append({
# C873SRC 000198|            "shape": shape,
# C873SRC 000199|            "vertices": crow["vertices"],
# C873SRC 000200|            "links_and_seams": crow["oriented_links"],
# C873SRC 000201|            "plaquettes": crow["plaquettes"],
# C873SRC 000202|            "cycle_rank": crow["cycle_space_rank"],
# C873SRC 000203|            "fixed_divergence_dimension": crow[
# C873SRC 000204|                "fixed_star_divergence_link_sector_dimension"
# C873SRC 000205|            ],
# C873SRC 000206|            "uniform_plus_sector_dimension": crow[
# C873SRC 000207|                "uniform_cycle_plus_one_sector_dimension"
# C873SRC 000208|            ],
# C873SRC 000209|            "F17_bank_M2": prow["F17_only_all_seam_bank_union_M2"],
# C873SRC 000210|            "complete_epoch_logical": ledger["complete_epoch_logical_instructions"],
# C873SRC 000211|            "complete_epoch_routed": ledger["complete_epoch_routed_NN_gates"],
# C873SRC 000212|            "complete_epoch_depth": ledger["complete_epoch_fixed_routed_depth"],
# C873SRC 000213|            "raw_seam_stage_phase": [
# C873SRC 000214|                float(((-1j) ** prow["seams"]).real),
# C873SRC 000215|                float(((-1j) ** prow["seams"]).imag),
# C873SRC 000216|            ],
# C873SRC 000217|            "Cycle870_full_epoch_formal_correction_angle": prow["phase"][
# C873SRC 000218|                "unchanged_full_update_formal_correction_angle"
# C873SRC 000219|            ],
# C873SRC 000220|            "checks": checks,
# C873SRC 000221|        })
# C873SRC 000222|
# C873SRC 000223|    factor_proof = physical["factor_level_proof"]
# C873SRC 000224|    required_factor_order = (
# C873SRC 000225|        "endpoint B extraction -> landed four-rotation seam factor -> mutually "
# C873SRC 000226|        "exclusive positive/negative predicate-controlled unary shifts -> endpoint cleanup"
# C873SRC 000227|    )
# C873SRC 000228|    if factor_proof["literal_emitted_order"] != required_factor_order:
# C873SRC 000229|        failures.append("factor-level emitted order")
# C873SRC 000230|    if not all(
# C873SRC 000231|        row["selected_factor_match_failures"] == 0
# C873SRC 000232|        and row["phase"]["maximum_raw_square_to_minus_identity_residual"] <= TOL
# C873SRC 000233|        and abs(row["phase"]["maximum_raw_square_to_identity_residual"] - 2.0) <= TOL
# C873SRC 000234|        and row["phase"]["maximum_formal_corrected_residual"] <= TOL
# C873SRC 000235|        and row["F17_only_added_instruction_census_failures"] == 0
# C873SRC 000236|        for row in physical["fixtures"]
# C873SRC 000237|    ):
# C873SRC 000238|        failures.append("factor-level physical certificate")
# C873SRC 000239|    if any(
# C873SRC 000240|        row[key]
# C873SRC 000241|        for row in physical["semantics"]
# C873SRC 000242|        for key in ("basis_failures", "scratch_cleanup_failures", "typed_G_failures")
# C873SRC 000243|    ):
# C873SRC 000244|        failures.append("factor-level semantic certificate")
# C873SRC 000245|
# C873SRC 000246|    local_controls = {
# C873SRC 000247|        "plaquette_SWAP_deletions_tested": sum(
# C873SRC 000248|            row["plaquette_shift"]["individual_SWAP_deletions_tested"]
# C873SRC 000249|            for row in constraints["fixtures"]
# C873SRC 000250|        ),
# C873SRC 000251|        "plaquette_SWAP_deletions_undetected": sum(
# C873SRC 000252|            row["plaquette_shift"]["undetected_individual_SWAP_deletions"]
# C873SRC 000253|            for row in constraints["fixtures"]
# C873SRC 000254|        ),
# C873SRC 000255|        "basis_translation_overlap": constraints["single_plaquette_uniform"][
# C873SRC 000256|            "basis_link_shift_overlap"
# C873SRC 000257|        ],
# C873SRC 000258|        "uniform_translation_overlap": constraints["single_plaquette_uniform"][
# C873SRC 000259|            "uniform_shift_overlap"
# C873SRC 000260|        ],
# C873SRC 000261|    }
# C873SRC 000262|    if local_controls["plaquette_SWAP_deletions_tested"] != 3392:
# C873SRC 000263|        failures.append("plaquette deletion census")
# C873SRC 000264|    if local_controls["plaquette_SWAP_deletions_undetected"]:
# C873SRC 000265|        failures.append("plaquette deletion undetected")
# C873SRC 000266|
# C873SRC 000267|    c219 = affine["actual_Cycle219_decoded_free_one_particle"]
# C873SRC 000268|    if c219["actual_Cycle870_beta"] != -0.3:
# C873SRC 000269|        failures.append("Cycle219 beta")
# C873SRC 000270|    if c219["actual_dense_coin_encoded_onsite_intertwiner_residual"] > TOL:
# C873SRC 000271|        failures.append("Cycle219 onsite intertwiner")
# C873SRC 000272|    if c219[
# C873SRC 000273|        "eight_step_same_block_multiplication_consistency_residual"
# C873SRC 000274|    ] > TOL:
# C873SRC 000275|        failures.append("Cycle219 recurrence")
# C873SRC 000276|    if c219["dispersion_relative_residual"] > 4.0e-6:
# C873SRC 000277|        failures.append("Cycle219 dispersion")
# C873SRC 000278|    if affine["filled_plaquette"]["direct_intertwiner_max_residual"] > TOL:
# C873SRC 000279|        failures.append("affine direct intertwiner")
# C873SRC 000280|    if (
# C873SRC 000281|        affine["fixed_star_background"]["filled_plaquette_variant_cases"] != 192
# C873SRC 000282|        or affine["fixed_star_background"][
# C873SRC 000283|            "filled_plaquette_variant_intertwiner_max_residual"
# C873SRC 000284|        ] > TOL
# C873SRC 000285|    ):
# C873SRC 000286|        failures.append("affine fixed-star background variants")
# C873SRC 000287|    six_mode = affine["six_mode_total_occupation_extension"]
# C873SRC 000288|    if (
# C873SRC 000289|        six_mode["rows"] != 2448
# C873SRC 000290|        or six_mode["FSWAP_minus_11_rows"] != 612
# C873SRC 000291|        or any(
# C873SRC 000292|            six_mode[key]
# C873SRC 000293|            for key in (
# C873SRC 000294|                "incidence_failures",
# C873SRC 000295|                "fixed_background_or_star_invariance_failures",
# C873SRC 000296|                "total_number_failures",
# C873SRC 000297|                "occupation_range_failures",
# C873SRC 000298|                "FSWAP_sign_failures",
# C873SRC 000299|            )
# C873SRC 000300|        )
# C873SRC 000301|    ):
# C873SRC 000302|        failures.append("affine six-mode total-occupation extension")
# C873SRC 000303|    if affine["open_cube_L2"][
# C873SRC 000304|        "repeated_uniform_intertwiner_incidence_failures"
# C873SRC 000305|    ]:
# C873SRC 000306|        failures.append("affine repeated intertwiner")
# C873SRC 000307|
# C873SRC 000308|    optional = physical["secondary_optional_evidence"]
# C873SRC 000309|    if "excluded" not in optional["closure_role"]:
# C873SRC 000310|        failures.append("optional evidence closure label")
# C873SRC 000311|
# C873SRC 000312|    report = {
# C873SRC 000313|        "status": "pending",
# C873SRC 000314|        "name": "Cycle873 recurrent F17 uniform-affine open-box primary",
# C873SRC 000315|        "claim_scope": (
# C873SRC 000316|            "recurrent F17-only physical-M2 all-seam augmentation plus uniform "
# C873SRC 000317|            "affine-Gauss/trivial-loop code and local constraint characterization "
# C873SRC 000318|            "and preservation on the three tested open boxes"
# C873SRC 000319|        ),
# C873SRC 000320|        "provenance": {
# C873SRC 000321|            "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 000322|            "expected_base_is_ancestor_of_head": base_is_ancestor,
# C873SRC 000323|            "runner": str(Path(__file__).relative_to(ROOT)),
# C873SRC 000324|            "child_source_sha256": source_hashes,
# C873SRC 000325|            "child_source_hash_mismatches": source_mismatches,
# C873SRC 000326|            "child_receipt_sha256": {
# C873SRC 000327|                row["receipt"]: file_sha256(ROOT / row["receipt"])
# C873SRC 000328|                for row in CHILDREN.values()
# C873SRC 000329|            },
# C873SRC 000330|        },
# C873SRC 000331|        "cold_child_runs": cold_runs,
# C873SRC 000332|        "factor_level_proof": {
# C873SRC 000333|            **factor_proof,
# C873SRC 000334|            "selected_seam_factors": sum(row["seams"] for row in physical["fixtures"]),
# C873SRC 000335|            "four_rotation_selection_failures": sum(
# C873SRC 000336|                row["selected_factor_match_failures"] for row in physical["fixtures"]
# C873SRC 000337|            ),
# C873SRC 000338|            "raw_per_seam_phase": [0.0, -1.0],
# C873SRC 000339|            "open_box_raw_seam_stage_phases": [
# C873SRC 000340|                {
# C873SRC 000341|                    "shape": row["shape"],
# C873SRC 000342|                    "seams": row["links_and_seams"],
# C873SRC 000343|                    "phase": row["raw_seam_stage_phase"],
# C873SRC 000344|                }
# C873SRC 000345|                for row in fixture_rows
# C873SRC 000346|            ],
# C873SRC 000347|            "phase_cancellation_boundary": (
# C873SRC 000348|                "L2 (12 seams) and held 3x2x2 (20 seams) have raw seam-stage "
# C873SRC 000349|                "phase +1; L3 (54 seams) has raw seam-stage phase -1.  Only the "
# C873SRC 000350|                "formal +i-corrected per-seam macro is exact generally, and the "
# C873SRC 000351|                "full epoch retains Cycle870's separate ledgered global correction"
# C873SRC 000352|            ),
# C873SRC 000353|            "individual_rotation_boundary": (
# C873SRC 000354|                "the four landed seam rotations are not claimed separately to preserve "
# C873SRC 000355|                "the affine star code; the effective affine identity is checked for the "
# C873SRC 000356|                "completed grouped factor through two separate pinned legs, and no "
# C873SRC 000357|                "monolithic physical affine encoder is executed"
# C873SRC 000358|            ),
# C873SRC 000359|        },
# C873SRC 000360|        "modular_evidence_boundary": (
# C873SRC 000361|            "the literal physical-word/effective-action leg and the effective-action/"
# C873SRC 000362|            "affine-encoder leg are separately reconstructed and pinned; no runner "
# C873SRC 000363|            "constructs or executes one physical affine encoder/Gauss-projector composition"
# C873SRC 000364|        ),
# C873SRC 000365|        "fixtures": fixture_rows,
# C873SRC 000366|        "schedule_input_boundary": physical["schedule_input_boundary"],
# C873SRC 000367|        "uniform_affine_code": {
# C873SRC 000368|            "fixed_star_background": affine["fixed_star_background"],
# C873SRC 000369|            "six_mode_total_occupation_extension": affine[
# C873SRC 000370|                "six_mode_total_occupation_extension"
# C873SRC 000371|            ],
# C873SRC 000372|            "filled_plaquette_direct_columns": affine["filled_plaquette"][
# C873SRC 000373|                "direct_fswap_columns_checked"
# C873SRC 000374|            ],
# C873SRC 000375|            "filled_plaquette_direct_residual": affine["filled_plaquette"][
# C873SRC 000376|                "direct_intertwiner_max_residual"
# C873SRC 000377|            ],
# C873SRC 000378|            "trivial_loop_overlap": affine["filled_plaquette"][
# C873SRC 000379|                "uniform_closed_loop_overlap"
# C873SRC 000380|            ],
# C873SRC 000381|            "nontrivial_character_loop_residual": affine["filled_plaquette"][
# C873SRC 000382|                "nonuniform_character_closed_loop_residual"
# C873SRC 000383|            ],
# C873SRC 000384|            "L2_repeated_factors": affine["open_cube_L2"]["repeated_factor_count"],
# C873SRC 000385|            "L2_repeated_incidence_failures": affine["open_cube_L2"][
# C873SRC 000386|                "repeated_uniform_intertwiner_incidence_failures"
# C873SRC 000387|            ],
# C873SRC 000388|            "covariance_boundary": (
# C873SRC 000389|                "full affine-encoder 24-frame, 576-product, and translation "
# C873SRC 000390|                "covariance with transported g is not established; the reported "
# C873SRC 000391|                "proper-frame checks belong to the separate local-constraint geometry"
# C873SRC 000392|            ),
# C873SRC 000393|        },
# C873SRC 000394|        "local_constraint_characterization": {
# C873SRC 000395|            "algebra": constraints["constraint_algebra"],
# C873SRC 000396|            "code_space_only": (
# C873SRC 000397|                "one-hot, star, and plaquette operators characterize and preserve the "
# C873SRC 000398|                "admitted code space; they do not prepare, enforce, cool, or reset it"
# C873SRC 000399|            ),
# C873SRC 000400|            "single_plaquette": constraints["single_plaquette_uniform"],
# C873SRC 000401|            "proper_frame_transport": constraints["proper_frame_transport"],
# C873SRC 000402|            "proper_frame_scope": (
# C873SRC 000403|                "physical local-constraint supports, gate words, and labels only; "
# C873SRC 000404|                "not a full affine encoder with background selection"
# C873SRC 000405|            ),
# C873SRC 000406|            "Object_A_preservation": constraints["Object_A_preservation"],
# C873SRC 000407|        },
# C873SRC 000408|        "actual_Cycle219_decoded_free_one_particle": c219,
# C873SRC 000409|        "active_controls": {
# C873SRC 000410|            "physical_component_mutations": physical["semantic_mutations"],
# C873SRC 000411|            "physical_structural_route_deletions": physical[
# C873SRC 000412|                "structural_route_deletions"
# C873SRC 000413|            ],
# C873SRC 000414|            "local": local_controls,
# C873SRC 000415|            "affine": affine["active_controls"],
# C873SRC 000416|            "raw_seam_square_to_identity_residual": max(
# C873SRC 000417|                row["phase"]["maximum_raw_square_to_identity_residual"]
# C873SRC 000418|                for row in physical["fixtures"]
# C873SRC 000419|            ),
# C873SRC 000420|            "naive_axis_schedule_collision_rows": sum(
# C873SRC 000421|                row["F17_only_naive_axis_only_route_footprint_collisions"]
# C873SRC 000422|                for row in physical["fixtures"]
# C873SRC 000423|            ),
# C873SRC 000424|        },
# C873SRC 000425|        "secondary_optional_evidence": {
# C873SRC 000426|            "closure_role": optional["closure_role"],
# C873SRC 000427|            "Cycle714_coexistence_status": physical["secondary_optional_status"],
# C873SRC 000428|            "Cycle714_coexistence_failures": physical[
# C873SRC 000429|                "secondary_optional_failures"
# C873SRC 000430|            ],
# C873SRC 000431|            "Cycle696_C700_boundary": (
# C873SRC 000432|                "not imported or tested by Cycle873; prior C696 is a classical-basis "
# C873SRC 000433|                "19V/18E six-ray-tree projection rather than the full link graph, and "
# C873SRC 000434|                "C700 is classical only; neither is a quantum uniform-sector or gravity bridge"
# C873SRC 000435|            ),
# C873SRC 000436|            "future_open_route": (
# C873SRC 000437|                "one candidate constructive route is a full-star coherent port rather "
# C873SRC 000438|                "than the literal ray-tree adapter; necessity and sufficiency are open"
# C873SRC 000439|            ),
# C873SRC 000440|        },
# C873SRC 000441|        "supplied_or_open": {
# C873SRC 000442|            "genesis_and_preparation": (
# C873SRC 000443|                "uniform affine-state preparation, code admission, one-hot enforcement, "
# C873SRC 000444|                "projector measurement, correction, cooling, reset, and recurrence invocation"
# C873SRC 000445|            ),
# C873SRC 000446|            "finite_synthesis": (
# C873SRC 000447|                "finite gate-set synthesis of ideal 2*pi/17 clock phases and order-17 projectors"
# C873SRC 000448|            ),
# C873SRC 000449|            "periodic_topology": (
# C873SRC 000450|                "periodic Wilson/harmonic sectors; the certified fixtures are contractible open boxes"
# C873SRC 000451|            ),
# C873SRC 000452|            "schedule_origin": (
# C873SRC 000453|                "the owner-coordinate parity origin and ordered 24-color traversal "
# C873SRC 000454|                "are supplied compiler inputs; unit-translation/origin-shift "
# C873SRC 000455|                "equivalence and host-free recurrence are not established"
# C873SRC 000456|            ),
# C873SRC 000457|        },
# C873SRC 000458|        "interpretation_firewall": (
# C873SRC 000459|            "no source, gravity, backreaction, continuum, time, tick, occurrence, Event, "
# C873SRC 000460|            "Record, Born rule/history, or autonomous genesis/preparation conclusion"
# C873SRC 000461|        ),
# C873SRC 000462|        "failures": failures,
# C873SRC 000463|    }
# C873SRC 000464|    report["status"] = "pass" if not failures else "fail"
# C873SRC 000465|    return report, failures
# C873SRC 000466|
# C873SRC 000467|
# C873SRC 000468|def main(output: Path = OUT) -> int:
# C873SRC 000469|    report, failures = build_report()
# C873SRC 000470|    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
# C873SRC 000471|    print(json.dumps({
# C873SRC 000472|        "status": report["status"],
# C873SRC 000473|        "base_commit": report["provenance"]["base_commit"],
# C873SRC 000474|        "expected_base_is_ancestor_of_head": report["provenance"][
# C873SRC 000475|            "expected_base_is_ancestor_of_head"
# C873SRC 000476|        ],
# C873SRC 000477|        "receipt": str(OUT.relative_to(ROOT)),
# C873SRC 000478|        "failures": failures,
# C873SRC 000479|        "fixtures": report.get("fixtures", ()),
# C873SRC 000480|        "C219_dispersion_mass": report.get(
# C873SRC 000481|            "actual_Cycle219_decoded_free_one_particle", {}
# C873SRC 000482|        ).get("dispersion_mass"),
# C873SRC 000483|    }, indent=2, sort_keys=True))
# C873SRC 000484|    return int(bool(failures))
# C873SRC 000485|
# C873SRC 000486|
# C873SRC 000487|if __name__ == "__main__":
# C873SRC 000488|    parser = argparse.ArgumentParser()
# C873SRC 000489|    parser.add_argument("--output", type=Path, default=OUT)
# C873SRC 000490|    arguments = parser.parse_args()
# C873SRC 000491|    raise SystemExit(main(arguments.output))
