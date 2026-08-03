#!/usr/bin/env python3
"""Cycle873 primary runner for the bounded recurrent F17 open-box package."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs/cycle873_recurrent_f17_uniform_affine_open_box_primary_receipt_2026_08_03.json"
EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
TOL = 3.0e-10

CHILDREN = {
    "physical": {
        "source": "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py",
        "receipt": "outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json",
        "sha256": "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7",
    },
    "constraints": {
        "source": "scripts/frontier_cycle873_f17_open_box_local_constraints_core_2026_08_03.py",
        "receipt": "outputs/cycle873_f17_open_box_local_constraints_core_receipt_2026_08_03.json",
        "sha256": "70d7362a2f534bd94b5b421f38e0c0509483ed8c1962b83f21f790b4c1dcb685",
    },
    "affine": {
        "source": "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py",
        "receipt": "outputs/cycle873_uniform_affine_gauss_intertwiner_core_receipt_2026_08_03.json",
        "sha256": "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9",
    },
}

EXPECTED_FIXTURES = {
    (2, 2, 2): {
        "V": 8, "E": 12, "P": 6, "cycle_rank": 5,
        "bank": 240, "logical": 24656, "routed": 204288, "depth": 204288,
    },
    (3, 3, 3): {
        "V": 27, "E": 54, "P": 36, "cycle_rank": 28,
        "bank": 1080, "logical": 95274, "routed": 842762, "depth": 688998,
    },
    (3, 2, 2): {
        "V": 12, "E": 20, "P": 11, "cycle_rank": 9,
        "bank": 400, "logical": 38740, "routed": 335316, "depth": 317116,
    },
}


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cold_children() -> tuple[dict, dict, list[str]]:
    reports = {}
    runs = {}
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="cycle873-primary-") as temporary:
        temporary_root = Path(temporary)
        for label, row in CHILDREN.items():
            source = ROOT / row["source"]
            canonical = ROOT / row["receipt"]
            fresh = temporary_root / f"{label}.json"
            process = subprocess.run(
                (sys.executable, "-B", str(source), "--output", str(fresh)),
                cwd=temporary_root,
                capture_output=True,
                text=True,
                check=False,
                env={**__import__("os").environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            canonical_bytes = canonical.read_bytes() if canonical.is_file() else b""
            fresh_bytes = fresh.read_bytes() if fresh.is_file() else b""
            runs[label] = {
                "returncode": process.returncode,
                "stdout": process.stdout,
                "stdout_sha256": sha256(process.stdout.encode()).hexdigest(),
                "stderr": process.stderr,
                "fresh_receipt_sha256": sha256(fresh_bytes).hexdigest(),
                "canonical_receipt_sha256": sha256(canonical_bytes).hexdigest(),
                "byte_identical_to_canonical": fresh_bytes == canonical_bytes,
            }
            if process.returncode:
                failures.append(f"{label}:cold return code")
            if process.stderr:
                failures.append(f"{label}:cold stderr")
            if not fresh_bytes:
                failures.append(f"{label}:missing cold receipt")
                continue
            if fresh_bytes != canonical_bytes:
                failures.append(f"{label}:cold receipt drift")
            reports[label] = json.loads(fresh_bytes)
    return reports, runs, failures


def build_report() -> tuple[dict, list[str]]:
    failures: list[str] = []
    base_is_ancestor = subprocess.run(
        (
            "git", "merge-base", "--is-ancestor",
            EXPECTED_BASE_COMMIT, "HEAD",
        ),
        cwd=ROOT,
        check=False,
    ).returncode == 0
    if not base_is_ancestor:
        failures.append("expected base is not an ancestor of HEAD")

    source_hashes = {
        row["source"]: file_sha256(ROOT / row["source"])
        for row in CHILDREN.values()
    }
    source_mismatches = {
        label: {
            "expected": row["sha256"],
            "observed": source_hashes[row["source"]],
        }
        for label, row in CHILDREN.items()
        if source_hashes[row["source"]] != row["sha256"]
    }
    if source_mismatches:
        failures.append("child source hash mismatch")

    reports, cold_runs, cold_failures = cold_children()
    failures.extend(cold_failures)
    for label in CHILDREN:
        if label not in reports:
            continue
        if reports[label].get("status") != "pass" or reports[label].get("failures"):
            failures.append(f"{label}:child status")
        child_provenance = reports[label].get("provenance", {})
        if child_provenance.get("base_commit") != EXPECTED_BASE_COMMIT:
            failures.append(f"{label}:base commit")
        if not child_provenance.get("expected_base_is_ancestor_of_head"):
            failures.append(f"{label}:base ancestry")

    if set(reports) != set(CHILDREN):
        report = {
            "status": "fail", "failures": failures,
            "provenance": {
                "base_commit": EXPECTED_BASE_COMMIT,
                "expected_base_is_ancestor_of_head": base_is_ancestor,
            },
            "cold_runs": cold_runs,
        }
        return report, failures

    physical = reports["physical"]
    constraints = reports["constraints"]
    affine = reports["affine"]
    physical_by_shape = {
        tuple(row["shape"]): row for row in physical["fixtures"]
    }
    constraint_by_shape = {
        tuple(row["shape"]): row for row in constraints["fixtures"]
    }
    fixture_rows = []
    for shape, expected in EXPECTED_FIXTURES.items():
        prow = physical_by_shape.get(shape)
        crow = constraint_by_shape.get(shape)
        if prow is None or crow is None:
            failures.append(f"{shape}:missing fixture")
            continue
        ledger = prow["augmented_epoch_ledgers"]["A_F17_only"]
        checks = {
            "vertices": crow["vertices"] == expected["V"],
            "links_equal_seams": crow["oriented_links"] == prow["seams"] == expected["E"],
            "plaquettes": crow["plaquettes"] == expected["P"],
            "cycle_rank": crow["cycle_space_rank"] == expected["cycle_rank"],
            "plaquette_span": crow["plaquette_boundary_rank_mod17"] == expected["cycle_rank"],
            "unique_uniform_plus_sector": crow["uniform_cycle_plus_one_sector_dimension"] == 1,
            "bank": prow["F17_only_all_seam_bank_union_M2"] == expected["bank"],
            "logical": ledger["complete_epoch_logical_instructions"] == expected["logical"],
            "routed": ledger["complete_epoch_routed_NN_gates"] == expected["routed"],
            "depth": ledger["complete_epoch_fixed_routed_depth"] == expected["depth"],
            "factor_order": ledger["factor_order_reconstruction_failures"] == 0,
            "routes": ledger["complete_epoch_non_NN_or_return_failures"] == 0,
            "raw_stage_phase": [
                float(((-1j) ** prow["seams"]).real),
                float(((-1j) ** prow["seams"]).imag),
            ] == ([-1.0, 0.0] if shape == (3, 3, 3) else [1.0, 0.0]),
            "constraint_preservation": constraints["Object_A_preservation"][
                "full_augmented_epoch_constraint_preservation_failures"
            ] == 0,
        }
        failures.extend(
            f"{shape}:{name}" for name, passed in checks.items() if not passed
        )
        fixture_rows.append({
            "shape": shape,
            "vertices": crow["vertices"],
            "links_and_seams": crow["oriented_links"],
            "plaquettes": crow["plaquettes"],
            "cycle_rank": crow["cycle_space_rank"],
            "fixed_divergence_dimension": crow[
                "fixed_star_divergence_link_sector_dimension"
            ],
            "uniform_plus_sector_dimension": crow[
                "uniform_cycle_plus_one_sector_dimension"
            ],
            "F17_bank_M2": prow["F17_only_all_seam_bank_union_M2"],
            "complete_epoch_logical": ledger["complete_epoch_logical_instructions"],
            "complete_epoch_routed": ledger["complete_epoch_routed_NN_gates"],
            "complete_epoch_depth": ledger["complete_epoch_fixed_routed_depth"],
            "raw_seam_stage_phase": [
                float(((-1j) ** prow["seams"]).real),
                float(((-1j) ** prow["seams"]).imag),
            ],
            "Cycle870_full_epoch_formal_correction_angle": prow["phase"][
                "unchanged_full_update_formal_correction_angle"
            ],
            "checks": checks,
        })

    factor_proof = physical["factor_level_proof"]
    required_factor_order = (
        "endpoint B extraction -> landed four-rotation seam factor -> mutually "
        "exclusive positive/negative predicate-controlled unary shifts -> endpoint cleanup"
    )
    if factor_proof["literal_emitted_order"] != required_factor_order:
        failures.append("factor-level emitted order")
    if not all(
        row["selected_factor_match_failures"] == 0
        and row["phase"]["maximum_raw_square_to_minus_identity_residual"] <= TOL
        and abs(row["phase"]["maximum_raw_square_to_identity_residual"] - 2.0) <= TOL
        and row["phase"]["maximum_formal_corrected_residual"] <= TOL
        and row["F17_only_added_instruction_census_failures"] == 0
        for row in physical["fixtures"]
    ):
        failures.append("factor-level physical certificate")
    if any(
        row[key]
        for row in physical["semantics"]
        for key in ("basis_failures", "scratch_cleanup_failures", "typed_G_failures")
    ):
        failures.append("factor-level semantic certificate")

    local_controls = {
        "plaquette_SWAP_deletions_tested": sum(
            row["plaquette_shift"]["individual_SWAP_deletions_tested"]
            for row in constraints["fixtures"]
        ),
        "plaquette_SWAP_deletions_undetected": sum(
            row["plaquette_shift"]["undetected_individual_SWAP_deletions"]
            for row in constraints["fixtures"]
        ),
        "basis_translation_overlap": constraints["single_plaquette_uniform"][
            "basis_link_shift_overlap"
        ],
        "uniform_translation_overlap": constraints["single_plaquette_uniform"][
            "uniform_shift_overlap"
        ],
    }
    if local_controls["plaquette_SWAP_deletions_tested"] != 3392:
        failures.append("plaquette deletion census")
    if local_controls["plaquette_SWAP_deletions_undetected"]:
        failures.append("plaquette deletion undetected")

    c219 = affine["actual_Cycle219_decoded_free_one_particle"]
    if c219["actual_Cycle870_beta"] != -0.3:
        failures.append("Cycle219 beta")
    if c219["actual_dense_coin_encoded_onsite_intertwiner_residual"] > TOL:
        failures.append("Cycle219 onsite intertwiner")
    if c219[
        "eight_step_same_block_multiplication_consistency_residual"
    ] > TOL:
        failures.append("Cycle219 recurrence")
    if c219["dispersion_relative_residual"] > 4.0e-6:
        failures.append("Cycle219 dispersion")
    if affine["filled_plaquette"]["direct_intertwiner_max_residual"] > TOL:
        failures.append("affine direct intertwiner")
    if (
        affine["fixed_star_background"]["filled_plaquette_variant_cases"] != 192
        or affine["fixed_star_background"][
            "filled_plaquette_variant_intertwiner_max_residual"
        ] > TOL
    ):
        failures.append("affine fixed-star background variants")
    six_mode = affine["six_mode_total_occupation_extension"]
    if (
        six_mode["rows"] != 2448
        or six_mode["FSWAP_minus_11_rows"] != 612
        or any(
            six_mode[key]
            for key in (
                "incidence_failures",
                "fixed_background_or_star_invariance_failures",
                "total_number_failures",
                "occupation_range_failures",
                "FSWAP_sign_failures",
            )
        )
    ):
        failures.append("affine six-mode total-occupation extension")
    if affine["open_cube_L2"][
        "repeated_uniform_intertwiner_incidence_failures"
    ]:
        failures.append("affine repeated intertwiner")

    optional = physical["secondary_optional_evidence"]
    if "excluded" not in optional["closure_role"]:
        failures.append("optional evidence closure label")

    report = {
        "status": "pending",
        "name": "Cycle873 recurrent F17 uniform-affine open-box primary",
        "claim_scope": (
            "recurrent F17-only physical-M2 all-seam augmentation plus uniform "
            "affine-Gauss/trivial-loop code and local constraint characterization "
            "and preservation on the three tested open boxes"
        ),
        "provenance": {
            "base_commit": EXPECTED_BASE_COMMIT,
            "expected_base_is_ancestor_of_head": base_is_ancestor,
            "runner": str(Path(__file__).relative_to(ROOT)),
            "child_source_sha256": source_hashes,
            "child_source_hash_mismatches": source_mismatches,
            "child_receipt_sha256": {
                row["receipt"]: file_sha256(ROOT / row["receipt"])
                for row in CHILDREN.values()
            },
        },
        "cold_child_runs": cold_runs,
        "factor_level_proof": {
            **factor_proof,
            "selected_seam_factors": sum(row["seams"] for row in physical["fixtures"]),
            "four_rotation_selection_failures": sum(
                row["selected_factor_match_failures"] for row in physical["fixtures"]
            ),
            "raw_per_seam_phase": [0.0, -1.0],
            "open_box_raw_seam_stage_phases": [
                {
                    "shape": row["shape"],
                    "seams": row["links_and_seams"],
                    "phase": row["raw_seam_stage_phase"],
                }
                for row in fixture_rows
            ],
            "phase_cancellation_boundary": (
                "L2 (12 seams) and held 3x2x2 (20 seams) have raw seam-stage "
                "phase +1; L3 (54 seams) has raw seam-stage phase -1.  Only the "
                "formal +i-corrected per-seam macro is exact generally, and the "
                "full epoch retains Cycle870's separate ledgered global correction"
            ),
            "individual_rotation_boundary": (
                "the four landed seam rotations are not claimed separately to preserve "
                "the affine star code; the effective affine identity is checked for the "
                "completed grouped factor through two separate pinned legs, and no "
                "monolithic physical affine encoder is executed"
            ),
        },
        "modular_evidence_boundary": (
            "the literal physical-word/effective-action leg and the effective-action/"
            "affine-encoder leg are separately reconstructed and pinned; no runner "
            "constructs or executes one physical affine encoder/Gauss-projector composition"
        ),
        "fixtures": fixture_rows,
        "schedule_input_boundary": physical["schedule_input_boundary"],
        "uniform_affine_code": {
            "fixed_star_background": affine["fixed_star_background"],
            "six_mode_total_occupation_extension": affine[
                "six_mode_total_occupation_extension"
            ],
            "filled_plaquette_direct_columns": affine["filled_plaquette"][
                "direct_fswap_columns_checked"
            ],
            "filled_plaquette_direct_residual": affine["filled_plaquette"][
                "direct_intertwiner_max_residual"
            ],
            "trivial_loop_overlap": affine["filled_plaquette"][
                "uniform_closed_loop_overlap"
            ],
            "nontrivial_character_loop_residual": affine["filled_plaquette"][
                "nonuniform_character_closed_loop_residual"
            ],
            "L2_repeated_factors": affine["open_cube_L2"]["repeated_factor_count"],
            "L2_repeated_incidence_failures": affine["open_cube_L2"][
                "repeated_uniform_intertwiner_incidence_failures"
            ],
            "covariance_boundary": (
                "full affine-encoder 24-frame, 576-product, and translation "
                "covariance with transported g is not established; the reported "
                "proper-frame checks belong to the separate local-constraint geometry"
            ),
        },
        "local_constraint_characterization": {
            "algebra": constraints["constraint_algebra"],
            "code_space_only": (
                "one-hot, star, and plaquette operators characterize and preserve the "
                "admitted code space; they do not prepare, enforce, cool, or reset it"
            ),
            "single_plaquette": constraints["single_plaquette_uniform"],
            "proper_frame_transport": constraints["proper_frame_transport"],
            "proper_frame_scope": (
                "physical local-constraint supports, gate words, and labels only; "
                "not a full affine encoder with background selection"
            ),
            "Object_A_preservation": constraints["Object_A_preservation"],
        },
        "actual_Cycle219_decoded_free_one_particle": c219,
        "active_controls": {
            "physical_component_mutations": physical["semantic_mutations"],
            "physical_structural_route_deletions": physical[
                "structural_route_deletions"
            ],
            "local": local_controls,
            "affine": affine["active_controls"],
            "raw_seam_square_to_identity_residual": max(
                row["phase"]["maximum_raw_square_to_identity_residual"]
                for row in physical["fixtures"]
            ),
            "naive_axis_schedule_collision_rows": sum(
                row["F17_only_naive_axis_only_route_footprint_collisions"]
                for row in physical["fixtures"]
            ),
        },
        "secondary_optional_evidence": {
            "closure_role": optional["closure_role"],
            "Cycle714_coexistence_status": physical["secondary_optional_status"],
            "Cycle714_coexistence_failures": physical[
                "secondary_optional_failures"
            ],
            "Cycle696_C700_boundary": (
                "not imported or tested by Cycle873; prior C696 is a classical-basis "
                "19V/18E six-ray-tree projection rather than the full link graph, and "
                "C700 is classical only; neither is a quantum uniform-sector or gravity bridge"
            ),
            "future_open_route": (
                "one candidate constructive route is a full-star coherent port rather "
                "than the literal ray-tree adapter; necessity and sufficiency are open"
            ),
        },
        "supplied_or_open": {
            "genesis_and_preparation": (
                "uniform affine-state preparation, code admission, one-hot enforcement, "
                "projector measurement, correction, cooling, reset, and recurrence invocation"
            ),
            "finite_synthesis": (
                "finite gate-set synthesis of ideal 2*pi/17 clock phases and order-17 projectors"
            ),
            "periodic_topology": (
                "periodic Wilson/harmonic sectors; the certified fixtures are contractible open boxes"
            ),
            "schedule_origin": (
                "the owner-coordinate parity origin and ordered 24-color traversal "
                "are supplied compiler inputs; unit-translation/origin-shift "
                "equivalence and host-free recurrence are not established"
            ),
        },
        "interpretation_firewall": (
            "no source, gravity, backreaction, continuum, time, tick, occurrence, Event, "
            "Record, Born rule/history, or autonomous genesis/preparation conclusion"
        ),
        "failures": failures,
    }
    report["status"] = "pass" if not failures else "fail"
    return report, failures


def main(output: Path = OUT) -> int:
    report, failures = build_report()
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "base_commit": report["provenance"]["base_commit"],
        "expected_base_is_ancestor_of_head": report["provenance"][
            "expected_base_is_ancestor_of_head"
        ],
        "receipt": str(OUT.relative_to(ROOT)),
        "failures": failures,
        "fixtures": report.get("fixtures", ()),
        "C219_dispersion_mass": report.get(
            "actual_Cycle219_decoded_free_one_particle", {}
        ).get("dispersion_mass"),
    }, indent=2, sort_keys=True))
    return int(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.output))
