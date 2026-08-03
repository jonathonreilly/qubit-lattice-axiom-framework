#!/usr/bin/env python3
"""Cold acceptance for the bounded Cycle873 candidate package.

This runner imports none of the Cycle873 computational children.  It validates
the citation and package pins, proves the recorded fetched base is an ancestor
of the current checkout, verifies Cycle873 was unused in that base tree,
launches the primary and independent runners from a temporary working
directory, and byte-compares both receipts and stdout logs.
"""

from __future__ import annotations

import argparse
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
PRIMARY = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.py"
INDEPENDENT = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.py"
ACCEPTANCE = "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_acceptance_2026_08_03.py"
PHYSICAL = "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
LOCAL = "scripts/frontier_cycle873_f17_open_box_local_constraints_core_2026_08_03.py"
AFFINE = "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py"
PRIMARY_RECEIPT = "outputs/cycle873_recurrent_f17_uniform_affine_open_box_primary_receipt_2026_08_03.json"
INDEPENDENT_RECEIPT = "outputs/cycle873_recurrent_f17_uniform_affine_open_box_independent_check_receipt_2026_08_03.json"
PHYSICAL_RECEIPT = "outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json"
LOCAL_RECEIPT = "outputs/cycle873_f17_open_box_local_constraints_core_receipt_2026_08_03.json"
AFFINE_RECEIPT = "outputs/cycle873_uniform_affine_gauss_intertwiner_core_receipt_2026_08_03.json"
ACCEPTANCE_RECEIPT = "outputs/cycle873_recurrent_f17_uniform_affine_open_box_package_acceptance_receipt_2026_08_03.json"
MANIFEST = "outputs/cycle873_recurrent_f17_uniform_affine_open_box_citation_manifest_2026_08_03.json"
NOTE = "docs/RECURRENT_F17_UNIFORM_AFFINE_OPEN_BOX_CYCLE873_BOUNDED_THEOREM_NOTE_2026-08-03.md"
PRIMARY_LOG = "logs/runner-cache/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.txt"
INDEPENDENT_LOG = "logs/runner-cache/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.txt"
DEFAULT_OUTPUT = ROOT / ACCEPTANCE_RECEIPT
EXPECTED_MANIFEST_SHA256 = "3ee9d12f1a0249abedfc56c7aaeadb497349d96b5e446120b229a391015e91fb"

EXPECTED_ARTIFACT_SHA256 = {
    NOTE: "4f189594d0e565f2fb2183acb0bd52765cfee45b3717a5e25c452ff8d44d7207",
    PRIMARY_LOG: "72be1cd183bf85663c6726223f9db9fb61be3e80b6ed0f3d386f32849312eb74",
    INDEPENDENT_LOG: "6689ee8aac078f36507af89c20a90a19ea0721d34af74b1a98318cec06c35812",
    PHYSICAL_RECEIPT: "486ed27ff7ecaaeb5dbe345f82c69a98f319410a2254bc05ab49d5811bfb840e",
    LOCAL_RECEIPT: "28c954d13a4d0a3d0b589c4a8a8fd9d31c3d0f9774e934abb4f84aae8d568233",
    AFFINE_RECEIPT: "d5d0dec904a034a0994d1e98e1c38b966240b91a3ad3435ac7bb01011c5b21b9",
    PRIMARY_RECEIPT: "1377569cebc4feb82a568460f3c730e2e6618c457fff10ca96ba35788dd517a1",
    INDEPENDENT_RECEIPT: "ce3dae5a6fafd675d69fdbaa0e0e651e07988b5409c3bff914a86341be18ced9",
    PHYSICAL: "69491f036463d9eb8947cdd4ad832f71f7c6e0cdd3f985adcbc29de4cdca37c7",
    LOCAL: "fffd77a8f8d0fcba644a69f0f5ed1bd3d3e21c874de4005de10156e6b1a12177",
    AFFINE: "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9",
    PRIMARY: "c7cc974a8a5ebe6481ba71bf210089b63bfe92a8ca76e60600484562380e6ef2",
    INDEPENDENT: "fa8d7d6b8f128452560d16d3f702e5536eb45dc3633a91e3dc8d5c7fa893e9fd",
}

EXPECTED_PACKAGE_FILES = tuple(sorted((
    NOTE,
    PRIMARY_LOG,
    INDEPENDENT_LOG,
    PHYSICAL_RECEIPT,
    LOCAL_RECEIPT,
    AFFINE_RECEIPT,
    PRIMARY_RECEIPT,
    INDEPENDENT_RECEIPT,
    MANIFEST,
    ACCEPTANCE_RECEIPT,
    PHYSICAL,
    LOCAL,
    AFFINE,
    PRIMARY,
    INDEPENDENT,
    ACCEPTANCE,
)))

EXPECTED_EXCLUSIONS = {
    MANIFEST,
    ACCEPTANCE,
    ACCEPTANCE_RECEIPT,
}

NOTE_REQUIRED_TEXT = (
    "Type: bounded_theorem",
    "Status: proposed_retained.",
    "Authority: none. Audit: unset.",
    "endpoint B extraction -> landed four-rotation seam factor -> mutually exclusive positive/negative predicate-controlled unary shifts -> endpoint cleanup",
    "The grouped augmented macro is the literal emitted M2 word.",
    "selected endpoint-mode occupations",
    "Its four landed seam rotations are not separately claimed",
    "raw seam as exactly `-i * FSWAP`",
    "formal `+i` zero-site scalar correction",
    "54 seams, raw seam-stage phase `-1`",
    "characterize and preserve the admitted code space",
    "not a preparation, admission, enforcement, projection, cooling, reset, or genesis result",
    "no runner constructs or executes a single physical affine encoder/Gauss-projector composition",
    "executable global affine-fiber fixture is normalized to `alpha=+1`",
    "`div ell` is outgoing-minus-incoming, equal to `-B ell`",
    "Full affine-encoder covariance under 24 proper frames, 576 frame products, or translations with transported `g` is not established here.",
    "Cycle 714 packet coexistence is a secondary diagnostic only",
    "Cycle 696 is neither imported nor pinned",
    "classical 19-vertex/18-edge six-ray-tree projection",
    "Cycle 700 is classical only",
    "This concept is not Cycle 873 evidence.",
    "FAIL_AS_NO_GO; DEMOTED_TO_COMPUTATIONAL_BASIS_WITNESS",
    "2,448 rows with seam bits",
    "612 `a=b=1` rows carry the FSWAP minus sign",
    "supplied lattice parity origin",
    "does not prove unit-translation/origin-shift equivalence",
    "The 20 M2 persistent bank is not the whole routing substrate.",
    "[Minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md)",
    "[Cycle 870 recurrent physical-M2 matter compiler]",
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def base_certificate() -> dict:
    ancestor = subprocess.run(
        (
            "git", "merge-base", "--is-ancestor",
            EXPECTED_BASE_COMMIT, "HEAD",
        ),
        cwd=ROOT,
        check=False,
    ).returncode == 0
    unused = subprocess.run(
        (
            "git", "grep", "-n", "-I", "-E",
            "Cycle[ _-]?873|cycle873",
            EXPECTED_BASE_COMMIT,
            "--", ".",
        ),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "base_commit": EXPECTED_BASE_COMMIT,
        "base_is_ancestor_of_head": ancestor,
        "unused_git_grep_returncode": unused.returncode,
        "unused_git_grep_stdout": unused.stdout,
        "unused_git_grep_stderr": unused.stderr,
        "cycle873_unused_on_base": (
            unused.returncode == 1 and not unused.stdout and not unused.stderr
        ),
    }


def cold_run(source: str, canonical_receipt: str, canonical_log: str) -> dict:
    with tempfile.TemporaryDirectory(prefix="cycle873-acceptance-") as temporary:
        temporary_root = Path(temporary)
        fresh = temporary_root / "receipt.json"
        process = subprocess.run(
            (
                sys.executable,
                "-B",
                str(ROOT / source),
                "--output",
                str(fresh),
            ),
            cwd=temporary_root,
            capture_output=True,
            check=False,
            timeout=240,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        fresh_bytes = fresh.read_bytes() if fresh.is_file() else b""
    canonical_bytes = (ROOT / canonical_receipt).read_bytes()
    log_bytes = (ROOT / canonical_log).read_bytes()
    return {
        "source": source,
        "returncode": process.returncode,
        "stderr": process.stderr.decode("utf-8", errors="replace"),
        "stdout_sha256": sha256(process.stdout).hexdigest(),
        "canonical_log_sha256": sha256(log_bytes).hexdigest(),
        "stdout_byte_identical_to_log": process.stdout == log_bytes,
        "fresh_receipt_sha256": sha256(fresh_bytes).hexdigest(),
        "canonical_receipt_sha256": sha256(canonical_bytes).hexdigest(),
        "fresh_receipt_byte_identical_to_canonical": fresh_bytes == canonical_bytes,
    }


def build_report() -> tuple[dict, list[str]]:
    failures: list[str] = []
    base = base_certificate()
    if not base["base_is_ancestor_of_head"]:
        failures.append("recorded base is not an ancestor of HEAD")
    if not base["cycle873_unused_on_base"]:
        failures.append("Cycle873 was not unused on the recorded base")

    observed = {
        path: digest(ROOT / path) if (ROOT / path).is_file() else None
        for path in EXPECTED_ARTIFACT_SHA256
    }
    drift = {
        path: {"expected": expected, "observed": observed[path]}
        for path, expected in EXPECTED_ARTIFACT_SHA256.items()
        if observed[path] != expected
    }
    if drift:
        failures.append("candidate artifact hash drift")

    manifest_hash = digest(ROOT / MANIFEST)
    if manifest_hash != EXPECTED_MANIFEST_SHA256:
        failures.append("citation manifest hash drift")
    manifest = load_json(ROOT / MANIFEST)
    if manifest.get("schema") != "cycle873-recurrent-f17-uniform-affine-open-box-citation-manifest-v1":
        failures.append("citation manifest schema")
    if manifest.get("base", {}).get("commit") != EXPECTED_BASE_COMMIT:
        failures.append("citation manifest base")
    if manifest.get("candidate_artifacts_sha256") != EXPECTED_ARTIFACT_SHA256:
        failures.append("citation manifest artifact map")
    if tuple(sorted(manifest.get("package_candidate_files", ()))) != EXPECTED_PACKAGE_FILES:
        failures.append("citation manifest package file set")
    exclusions = set(manifest.get("self_reference_exclusions", {}))
    if exclusions != EXPECTED_EXCLUSIONS:
        failures.append("citation manifest self-reference exclusions")

    upstream = manifest.get("upstream_citations_sha256", {})
    upstream_drift = {}
    for path, row in upstream.items():
        observed_hash = digest(ROOT / path) if (ROOT / path).is_file() else None
        if observed_hash != row.get("sha256"):
            upstream_drift[path] = {
                "expected": row.get("sha256"),
                "observed": observed_hash,
            }
    if upstream_drift:
        failures.append("upstream citation hash drift")
    if any("cycle696" in path.lower() or "cycle700" in path.lower() for path in upstream):
        failures.append("Cycle696/Cycle700 leaked into citation pins")

    missing_files = [
        path for path in EXPECTED_PACKAGE_FILES
        if path != ACCEPTANCE_RECEIPT and not (ROOT / path).is_file()
    ]
    if missing_files:
        failures.append("candidate package file missing")

    note = (ROOT / NOTE).read_text(encoding="utf-8")
    missing_note_text = [text for text in NOTE_REQUIRED_TEXT if text not in note]
    if missing_note_text:
        failures.append("theorem note boundary text")

    physical_text = (ROOT / PHYSICAL).read_text(encoding="utf-8")
    if "C696" in physical_text or "cycle696" in physical_text.lower():
        failures.append("Cycle696 leaked into physical core")
    if "rev-parse" in "\n".join(
        (ROOT / path).read_text(encoding="utf-8")
        for path in (PHYSICAL, LOCAL, AFFINE, PRIMARY, INDEPENDENT)
    ):
        failures.append("mutable HEAD provenance leaked into a runner")

    independent_imports = imported_modules(ROOT / INDEPENDENT)
    forbidden_imports = sorted(
        name for name in independent_imports
        if "frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary" in name
        or "frontier_cycle873_recurrent_f17_all_seam_physical_core" in name
    )
    if forbidden_imports:
        failures.append("independent checker imports a Cycle873 primary/core")

    receipts = {
        "physical": load_json(ROOT / PHYSICAL_RECEIPT),
        "local": load_json(ROOT / LOCAL_RECEIPT),
        "affine": load_json(ROOT / AFFINE_RECEIPT),
        "primary": load_json(ROOT / PRIMARY_RECEIPT),
        "independent": load_json(ROOT / INDEPENDENT_RECEIPT),
    }
    for label, receipt in receipts.items():
        if receipt.get("status") != "pass" or receipt.get("failures"):
            failures.append(f"{label} canonical receipt status")
        provenance = receipt.get("provenance", {})
        if provenance.get("base_commit") != EXPECTED_BASE_COMMIT:
            failures.append(f"{label} canonical base commit")
        if not provenance.get("expected_base_is_ancestor_of_head"):
            failures.append(f"{label} canonical base ancestry")

    factor = receipts["primary"].get("factor_level_proof", {})
    expected_phases = {
        (2, 2, 2): [1.0, 0.0],
        (3, 3, 3): [-1.0, 0.0],
        (3, 2, 2): [1.0, 0.0],
    }
    observed_phases = {
        tuple(row["shape"]): row["phase"]
        for row in factor.get("open_box_raw_seam_stage_phases", ())
    }
    if factor.get("raw_per_seam_phase") != [0.0, -1.0]:
        failures.append("raw per-seam phase boundary")
    if observed_phases != expected_phases:
        failures.append("open-box raw seam-stage phase boundary")
    if not factor.get("grouped_macro_is_literal_emitted_M2_word"):
        failures.append("grouped literal macro certificate")

    semantic_mutations = receipts["primary"].get("active_controls", {}).get(
        "physical_component_mutations", {}
    ).get("component_mutations", {})
    if set(semantic_mutations) != {
        "delete_cleanup", "delete_minus_shift", "delete_plus_shift", "delete_seam"
    }:
        failures.append("F17-only primary semantic mutation surface")

    expected_transit = {
        (2, 2, 2): (2787, 2079),
        (3, 3, 3): (11886, 9186),
        (3, 2, 2): (4547, 3439),
    }
    observed_transit = {
        tuple(row["shape"]): (
            row["F17_only_assigned_plus_route_support_union_M2"],
            row["F17_only_restored_route_transit_not_assigned_M2"],
        )
        for row in receipts["physical"].get("fixtures", ())
    }
    if observed_transit != expected_transit:
        failures.append("F17 transit-capacity census")
    if any(
        row.get("maximum_route_distance") != 33
        or row.get("recurrent_separation_pitch") != 32
        or row.get("envelope_width_failures_at_pitch32")
        for row in receipts["physical"].get("fixtures", ())
    ):
        failures.append("F17 transit envelope/pitch boundary")

    background = receipts["affine"].get("fixed_star_background", {})
    if (
        background.get("filled_plaquette_variant_cases") != 192
        or background.get("filled_plaquette_variant_intertwiner_max_residual") != 0.0
        or "not established" not in background.get("covariance_boundary", "")
    ):
        failures.append("fixed-star background/covariance boundary")
    six_mode_primary = receipts["affine"].get(
        "six_mode_total_occupation_extension", {}
    )
    if (
        six_mode_primary.get("rows") != 2448
        or six_mode_primary.get("alpha_normalization") != "+1"
        or six_mode_primary.get("FSWAP_minus_11_rows") != 612
        or any(
            six_mode_primary.get(key)
            for key in (
                "incidence_failures",
                "fixed_background_or_star_invariance_failures",
                "total_number_failures",
                "occupation_range_failures",
                "FSWAP_sign_failures",
            )
        )
        or six_mode_primary.get("wrong_incidence_sign_detected_rows") != 1224
        or six_mode_primary.get("omitted_link_shift_detected_rows") != 1224
    ):
        failures.append("primary six-mode total-occupation extension")

    schedule_boundary = receipts["primary"].get("schedule_input_boundary", {})
    if (
        "supplied lattice parity origin" not in schedule_boundary.get(
            "parity_origin", ""
        )
        or "supplied compiler schedule phase" not in schedule_boundary.get(
            "color_traversal", ""
        )
        or "unit-translation/origin-shift equivalence" not in
            schedule_boundary.get("not_proved", "")
    ):
        failures.append("parity-origin/color-traversal schedule boundary")

    independent = receipts["independent"]
    if independent.get("schema") != "cycle873-recurrent-f17-uniform-affine-open-box-independent-v1":
        failures.append("independent receipt schema")
    if independent.get("source_root") != ".":
        failures.append("independent receipt source_root portability")
    independence = independent.get("independence", {})
    if independence.get("checker_runtime_imported_primary") is not False:
        failures.append("independent runtime imported primary")
    if independence.get("physical_core_imports_cycle873_primary") is not False:
        failures.append("physical core imported primary")
    repeated = independent.get("repeated_factors", {})
    if (
        repeated.get("supplied_background_variant_columns") != 192
        or repeated.get("supplied_background_variant_max_residual") != 0.0
    ):
        failures.append("independent fixed-star background variants")
    six_mode_independent = independent.get(
        "six_mode_total_occupation_extension", {}
    )
    if (
        six_mode_independent.get("rows") != 2448
        or six_mode_independent.get("alpha_normalization") != "+1"
        or six_mode_independent.get("FSWAP_minus_11_rows") != 612
        or any(
            six_mode_independent.get(key)
            for key in (
                "incidence_failures",
                "fixed_background_or_star_invariance_failures",
                "occupation_range_failures",
                "FSWAP_sign_failures",
            )
        )
        or six_mode_independent.get("wrong_incidence_sign_detected_rows") != 1224
        or six_mode_independent.get("omitted_link_shift_detected_rows") != 1224
    ):
        failures.append("independent six-mode total-occupation extension")

    optional = receipts["primary"].get("secondary_optional_evidence", {})
    if "excluded" not in optional.get("closure_role", ""):
        failures.append("Cycle714 optional closure boundary")
    if "not imported or tested" not in optional.get("Cycle696_C700_boundary", ""):
        failures.append("Cycle696/Cycle700 primary boundary")

    c219 = receipts["primary"].get("actual_Cycle219_decoded_free_one_particle", {})
    modular = receipts["primary"].get("modular_evidence_boundary", "")
    onsite = receipts["local"].get("Object_A_preservation", {}).get(
        "onsite_stage_preservation", {}
    )
    independent_onsite = independent.get(
        "cycle219_recurrence_dispersion", {}
    ).get("onsite_F17_star_preservation", {})
    if "no runner constructs or executes one physical affine encoder" not in modular:
        failures.append("modular physical/affine evidence boundary")
    if (
        onsite.get("failures")
        or onsite.get("basis_occupation_columns") != 64
        or any(onsite.get("star_clock_commutator_residuals", {}).values())
        or any(
            value > 3.0e-10
            for value in onsite.get("unitarity_residuals", {}).values()
        )
        or onsite.get("coin_schedule_reconstruction_residual", 1.0) > 3.0e-10
        or any(
            value <= 0
            for value in onsite.get("live_L2_onsite_rotation_census", {}).values()
        )
        or onsite.get("bare_occupation_flip_control_commutator", 0.0) <= 1.0e-3
        or independent_onsite.get("basis_occupation_columns") != 64
        or any(independent_onsite.get(
            "star_clock_commutator_residuals", {}
        ).values())
        or any(
            value > 3.0e-10
            for value in independent_onsite.get("unitarity_residuals", {}).values()
        )
        or independent_onsite.get("contact_one_particle_target_residual", 1.0)
            > 3.0e-10
        or independent_onsite.get(
            "bare_occupation_flip_control_commutator", 0.0
        ) <= 1.0e-3
    ):
        failures.append("executed onsite F17-star preservation")
    if (
        c219.get("actual_Cycle870_beta") != -0.3
        or abs(c219.get("dispersion_mass", 0.0) - 0.4534056690336209) > 1.0e-15
        or "not a periodic F17 physical-box" not in c219.get("scope_boundary", "")
    ):
        failures.append("Cycle219 recurrence/dispersion scope")
    independent_c219 = independent.get("cycle219_recurrence_dispersion", {})
    if (
        c219.get(
            "eight_step_same_block_multiplication_consistency_residual", 1.0
        ) > 3.0e-10
        or independent_c219.get(
            "eight_step_encoded_native_matrix_residual", 1.0
        ) > 3.0e-10
    ):
        failures.append("primary/independent eighth-power recurrence")

    cold = {
        "primary": cold_run(PRIMARY, PRIMARY_RECEIPT, PRIMARY_LOG),
        "independent": cold_run(
            INDEPENDENT, INDEPENDENT_RECEIPT, INDEPENDENT_LOG
        ),
    }
    for label, row in cold.items():
        if row["returncode"]:
            failures.append(f"{label} cold return code")
        if row["stderr"]:
            failures.append(f"{label} cold stderr")
        if not row["stdout_byte_identical_to_log"]:
            failures.append(f"{label} cold stdout drift")
        if not row["fresh_receipt_byte_identical_to_canonical"]:
            failures.append(f"{label} cold receipt drift")

    report = {
        "status": "pass" if not failures else "fail",
        "schema": "cycle873-recurrent-f17-uniform-affine-open-box-package-acceptance-v1",
        "base": base,
        "package_candidate_files": EXPECTED_PACKAGE_FILES,
        "package_file_count": len(EXPECTED_PACKAGE_FILES),
        "candidate_artifact_sha256": observed,
        "candidate_artifact_hash_drift": drift,
        "citation_manifest_sha256": manifest_hash,
        "upstream_citation_hash_drift": upstream_drift,
        "self_reference_exclusions": manifest.get("self_reference_exclusions", {}),
        "missing_package_files_before_acceptance_output": missing_files,
        "missing_note_required_text": missing_note_text,
        "independent_imports": sorted(independent_imports),
        "forbidden_independent_imports": forbidden_imports,
        "canonical_receipt_status": {
            label: receipt.get("status") for label, receipt in receipts.items()
        },
        "cold_runs": cold,
        "acceptance_source": ACCEPTANCE,
        "acceptance_source_sha256": digest(ROOT / ACCEPTANCE),
        "acceptance_receipt_self_hash_excluded": True,
        "failures": failures,
    }
    return report, failures


def main(output: Path = DEFAULT_OUTPUT) -> int:
    report, failures = build_report()
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "base_commit": EXPECTED_BASE_COMMIT,
        "base_is_ancestor_of_head": report["base"]["base_is_ancestor_of_head"],
        "cycle873_unused_on_base": report["base"]["cycle873_unused_on_base"],
        "package_file_count": report["package_file_count"],
        "primary_cold_receipt_match": report["cold_runs"]["primary"][
            "fresh_receipt_byte_identical_to_canonical"
        ],
        "independent_cold_receipt_match": report["cold_runs"]["independent"][
            "fresh_receipt_byte_identical_to_canonical"
        ],
        "failures": failures,
        "receipt": str(DEFAULT_OUTPUT.relative_to(ROOT)),
    }, indent=2, sort_keys=True))
    return int(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.output))
