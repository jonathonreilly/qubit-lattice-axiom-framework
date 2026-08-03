#!/usr/bin/env python3
"""Cold acceptance for the bounded Cycle 872 scratch package.

The acceptance lane imports neither package runner.  It pins the package and
upstream inputs, launches both runners under isolated Python from a fresh
working directory, byte-compares their receipts, and cross-checks their
independently named acceptance surfaces.
"""

from __future__ import annotations

import argparse
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import site
import subprocess
import sys
import tempfile


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PRIMARY = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py"
INDEPENDENT = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py"
ACCEPTANCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_acceptance_2026_08_03.py"
PRIMARY_RECEIPT = "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json"
INDEPENDENT_RECEIPT = "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json"
ACCEPTANCE_RECEIPT = "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_package_acceptance_receipt_2026_08_03.json"
NOTE = "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md"
DEFAULT_RECEIPT = PACKAGE_ROOT / ACCEPTANCE_RECEIPT
AUDIT_TIMEOUT_SEC = 1500
CHILD_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_acceptance_2026_08_03.py",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py",
    "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py",
    "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json",
)
DECLARED_INPUT_PATHS = (
    "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_acceptance_2026_08_03.py",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py",
    "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py",
    "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json",
)
EXPECTED_MANIFEST = tuple(sorted((
    NOTE, PRIMARY, INDEPENDENT, ACCEPTANCE,
    PRIMARY_RECEIPT, INDEPENDENT_RECEIPT, ACCEPTANCE_RECEIPT,
)))

EXPECTED_PACKAGE_SHA256 = {
    NOTE: "f8ef1a6951f9fdc62cfaa70c73b279d57ffd1e855d3c21c3cf1178270c1d2dd9",
    PRIMARY: "39f777c22707a6bba92b07367e5fc9ec945f55cd72f5df85148a52b915de757f",
    INDEPENDENT: "f73e1a2c19e5fc50b43228582af8aa8ad1a628c23692e201b0629660ef2c91e2",
    PRIMARY_RECEIPT: "080953c2726e1db2bc423ef32360bef097e6f48666b589cbf508e73ea4c6228a",
    INDEPENDENT_RECEIPT: "67183c686d0c5cb0bd33039522b8564b6b0317ea57f185adc50ced60f9be44c7",
}
PRIMARY_MARKER = "CYCLE872_ALL_SEAM_SPATIAL_PACKET_EPOCH_PASS"
INDEPENDENT_MARKER = "CYCLE872_ALL_SEAM_SPATIAL_PACKET_INDEPENDENT_PASS"


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def observed_hashes(root: Path, expected: dict[str, str]) -> dict[str, str | None]:
    return {
        label: file_sha256(root / label) if (root / label).is_file() else None
        for label in expected
    }


def discover_source_root(explicit: Path | None = None) -> Path:
    candidates = []
    if explicit is not None:
        candidates.append(explicit)
    supplied = os.environ.get("CYCLE872_SOURCE_ROOT")
    if supplied:
        candidates.append(Path(supplied))
    for start in (Path.cwd(), PACKAGE_ROOT):
        candidates.extend((start, *start.parents))
    marker = "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py"
    for candidate in candidates:
        resolved = candidate.resolve()
        if (resolved / marker).is_file():
            return resolved
    raise RuntimeError(
        "Cycle872 upstream repository not found; use --source-root, run from "
        "the repository root, or set CYCLE872_SOURCE_ROOT"
    )


def literal_assignment(path: Path, name: str):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            return ast.literal_eval(node.value)
    raise KeyError((path, name))


def package_manifest(root: Path = PACKAGE_ROOT) -> tuple[str, ...]:
    """Enumerate top-level Cycle872 package files in the three owned namespaces.

    Generated audit-ledger shards live below ``docs/audit`` and are validation
    outputs, not author-owned package files.  The package contract places all
    seven canonical artifacts directly in ``docs``, ``scripts``, or
    ``outputs``, so recurse into none of those repository subtrees.
    """
    output = []
    for directory in ("docs", "scripts", "outputs"):
        base = root / directory
        if not base.is_dir():
            continue
        output.extend(
            str(path.relative_to(root))
            for path in base.iterdir()
            if path.is_file()
            and "cycle872" in path.name.lower()
            and "__pycache__" not in path.parts
            and path.suffix != ".pyc"
        )
    return tuple(sorted(output))


def imported_modules(path: Path) -> tuple[str, ...]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    output = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            output.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            output.append(node.module)
    return tuple(sorted(output))


def isolated_support_paths() -> tuple[str, ...]:
    """Explicitly expose installed third-party packages to isolated Python."""
    candidates = [*site.getsitepackages(), site.getusersitepackages()]
    return tuple(dict.fromkeys(str(Path(row).resolve()) for row in candidates if Path(row).is_dir()))


def cold_run(
    script: Path, output: Path, cwd: Path, source_root: Path,
    extra_arguments: tuple[str, ...] = (),
) -> subprocess.CompletedProcess[str]:
    support = isolated_support_paths()
    argv = [str(script), "--output", str(output), *extra_arguments]
    bootstrap = (
        "import runpy,sys\n"
        f"sys.path.extend({support!r})\n"
        f"sys.argv={argv!r}\n"
        f"runpy.run_path({str(script)!r},run_name='__main__')\n"
    )
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONHASHSEED"] = "0"
    environment["CYCLE872_SOURCE_ROOT"] = str(source_root)
    return subprocess.run(
        [sys.executable, "-I", "-c", bootstrap],
        cwd=cwd,
        env=environment,
        text=True,
        capture_output=True,
        timeout=CHILD_TIMEOUT_SEC,
        check=False,
    )


def build_report(source_root: Path) -> dict[str, object]:
    failures: list[str] = []
    cross_checks: list[dict[str, object]] = []

    observed_manifest = package_manifest()
    if observed_manifest != EXPECTED_MANIFEST:
        failures.append("exact seven-file package manifest")
    package_hashes = observed_hashes(PACKAGE_ROOT, EXPECTED_PACKAGE_SHA256)
    audit_input_hashes = {
        label: file_sha256(PACKAGE_ROOT / label)
        if (PACKAGE_ROOT / label).is_file() else None
        for label in AUDIT_INPUT_PATHS
    }
    audit_missing = tuple(
        label for label, digest in audit_input_hashes.items() if digest is None
    )
    audit_pin_required = tuple(
        label for label in AUDIT_INPUT_PATHS if label != ACCEPTANCE
    )
    audit_unpinned = tuple(
        label for label in audit_pin_required if label not in EXPECTED_PACKAGE_SHA256
    )
    if DECLARED_INPUT_PATHS != AUDIT_INPUT_PATHS:
        failures.append("declared/audit input mismatch")
    if len(AUDIT_INPUT_PATHS) != len(set(AUDIT_INPUT_PATHS)):
        failures.append("duplicate audit inputs")
    if audit_missing:
        failures.append("missing audit inputs")
    if audit_unpinned:
        failures.append("unpinned audit inputs")
    if ACCEPTANCE_RECEIPT in AUDIT_INPUT_PATHS:
        failures.append("acceptance output receipt declared as audit input")
    primary_upstream_pins = literal_assignment(
        PACKAGE_ROOT / PRIMARY, "EXPECTED_INPUT_SHA256"
    )
    independent_upstream_pins = literal_assignment(
        PACKAGE_ROOT / INDEPENDENT, "EXPECTED_INPUT_SHA256"
    )
    if primary_upstream_pins != independent_upstream_pins:
        failures.append("runner literal upstream pin maps differ")
    if len(primary_upstream_pins) != 45:
        failures.append("literal upstream pin count")
    upstream_hashes = observed_hashes(source_root, primary_upstream_pins)
    for label, expected in EXPECTED_PACKAGE_SHA256.items():
        if package_hashes[label] != expected:
            failures.append("package hash: " + label)
    for label, expected in primary_upstream_pins.items():
        if upstream_hashes[label] != expected:
            failures.append("upstream hash: " + label)

    independent_imports = imported_modules(PACKAGE_ROOT / INDEPENDENT)
    primary_name = Path(PRIMARY).stem
    if any(primary_name in row for row in independent_imports):
        failures.append("independent checker imports primary")

    canonical_primary_bytes = (PACKAGE_ROOT / PRIMARY_RECEIPT).read_bytes()
    canonical_independent_bytes = (PACKAGE_ROOT / INDEPENDENT_RECEIPT).read_bytes()
    canonical_primary = json.loads(canonical_primary_bytes)
    canonical_independent = json.loads(canonical_independent_bytes)

    def require(label: str, condition: bool) -> None:
        if not condition:
            failures.append(label)

    def equal(label: str, left, right) -> None:
        same = left == right
        cross_checks.append({"label": label, "equal": same, "value": left})
        if not same:
            failures.append("cross-check: " + label)

    with tempfile.TemporaryDirectory(prefix="cycle872-cold-") as temporary:
        cold_root = Path(temporary)
        primary_output = cold_root / "primary.json"
        independent_output = cold_root / "independent.json"
        physical_stream_output = cold_root / "physical_stream.json"
        primary_process = cold_run(
            PACKAGE_ROOT / PRIMARY, primary_output, cold_root, source_root,
            ("--stream-output", str(physical_stream_output)),
        )
        independent_process = cold_run(
            PACKAGE_ROOT / INDEPENDENT, independent_output, cold_root, source_root
        )
        primary_cold_bytes = primary_output.read_bytes() if primary_output.is_file() else b""
        independent_cold_bytes = (
            independent_output.read_bytes() if independent_output.is_file() else b""
        )
        require("primary cold return code", primary_process.returncode == 0)
        require("independent cold return code", independent_process.returncode == 0)
        require("primary marker", primary_process.stdout.strip() == PRIMARY_MARKER)
        require("independent marker", independent_process.stdout.strip() == INDEPENDENT_MARKER)
        require("primary cold stderr", not primary_process.stderr)
        require("independent cold stderr", not independent_process.stderr)
        require("primary deterministic bytes", primary_cold_bytes == canonical_primary_bytes)
        require(
            "independent deterministic bytes",
            independent_cold_bytes == canonical_independent_bytes,
        )
        physical_stream_hash = (
            file_sha256(physical_stream_output)
            if physical_stream_output.is_file() else None
        )
        require(
            "materialized physical stream digest",
            physical_stream_hash
            == canonical_primary["physical_epoch_stream"]["serialized_stream_sha256"],
        )
        require(
            "materialized physical stream size",
            physical_stream_output.is_file()
            and physical_stream_output.stat().st_size
            == canonical_primary["physical_epoch_stream"]["serialized_stream_bytes"],
        )
        cold_runs = {
            "primary": {
                "isolated_python": True,
                "fresh_working_directory": True,
                "returncode": primary_process.returncode,
                "stdout": primary_process.stdout.strip(),
                "stderr_empty": not primary_process.stderr,
                "byte_identical_to_canonical": primary_cold_bytes == canonical_primary_bytes,
                "materialized_physical_stream_sha256": physical_stream_hash,
                "materialized_physical_stream_matches_receipt": (
                    physical_stream_hash
                    == canonical_primary["physical_epoch_stream"]["serialized_stream_sha256"]
                ),
            },
            "independent": {
                "isolated_python": True,
                "fresh_working_directory": True,
                "returncode": independent_process.returncode,
                "stdout": independent_process.stdout.strip(),
                "stderr_empty": not independent_process.stderr,
                "byte_identical_to_canonical": independent_cold_bytes == canonical_independent_bytes,
            },
        }

    require("primary status", canonical_primary.get("status") == "pass")
    require("primary failures", canonical_primary.get("failures") == [])
    require("independent status", canonical_independent.get("status") == "pass")
    require("independent failures", canonical_independent.get("failures") == [])
    require(
        "receipt independence flag",
        not canonical_independent["independence"]["primary_imported"],
    )
    require(
        "primary runner self hash",
        canonical_primary["provenance"]["runner_sha256"]
        == EXPECTED_PACKAGE_SHA256[PRIMARY],
    )
    require(
        "independent checker self hash",
        canonical_independent["provenance"]["checker_sha256"]
        == EXPECTED_PACKAGE_SHA256[INDEPENDENT],
    )
    require(
        "primary note pin",
        canonical_primary["provenance"]["theorem_note_sha256"]
        == EXPECTED_PACKAGE_SHA256[NOTE],
    )
    require(
        "independent note pin",
        canonical_independent["provenance"]["note_sha256"]
        == EXPECTED_PACKAGE_SHA256[NOTE],
    )
    require(
        "primary upstream pins",
        canonical_primary["provenance"]["input_sha256"] == upstream_hashes,
    )
    require(
        "independent upstream pins",
        canonical_independent["provenance"]["input_sha256"] == upstream_hashes,
    )
    require(
        "literal dependency closure count",
        canonical_primary["provenance"]["literal_dependency_pin_count"] == 45
        and canonical_independent["provenance"]["literal_dependency_pin_count"] == 45,
    )

    primary_stream = canonical_primary["physical_epoch_stream"]
    independent_stream = canonical_independent["physical_epoch_stream"]
    for key in (
        "length", "native_rotations", "native_factors",
        "unrouted_bound_instructions", "physical_local_gates",
        "matrix_registry_entries", "factor_manifest_sha256",
        "label_insensitive_instruction_binding_sha256",
        "normalized_physical_gate_sha256", "matrix_registry_sha256",
        "native_factor_sha256", "factor_stage_census", "physical_gate_stage_census",
        "first_forward_swap_deletion_detections",
    ):
        equal("physical stream " + key, primary_stream[key], independent_stream[key])
    require(
        "primary physical-stream construction",
        not any(primary_stream["construction_failure_census"].values()),
    )
    require(
        "independent physical-stream construction",
        not any(independent_stream["failure_census"].values())
        and not independent_stream["expected_mismatches"],
    )
    require(
        "exact local gate count",
        primary_stream["physical_local_gates"] == 220920,
    )

    primary_mutations = canonical_primary["physical_macro_mutations"]
    independent_mutations = canonical_independent["physical_macro_mutations"]
    for key in (
        "seams", "canonical_routed_macro_sha256",
        "wrong_side_routed_macro_sha256", "seam_deleted_routed_macro_sha256",
        "wrong_side_digest_detections", "seam_deletion_digest_detections",
    ):
        equal("physical mutation " + key, primary_mutations[key], independent_mutations[key])

    primary_epoch = {
        row["length"]: row for row in canonical_primary["epoch_fixtures"]
    }
    primary_held = {
        row["length"]: row for row in canonical_primary["held_schedule_fixtures"]
    }
    independent_fixtures = {
        row["length"]: row for row in canonical_independent["fixtures"]
    }
    common_fields = (
        ("cells", "cells"),
        ("seams", "seams"),
        ("fixed_color_schedule_routed_depth", "schedule_depth"),
        ("coarse_six_color_collision_control", "six_collisions"),
        ("used_packet_union_M2", "packet_union"),
        ("used_resource_union_M2", "resource_union"),
        ("total_resource_M2_per_seam", "total_resource_M2_per_seam"),
        ("spatial_output_local_coordinate", "spatial_output_local_coordinate"),
        ("lockstep_schedule_key", "lockstep_schedule_key"),
    )
    for length in (2, 3, 4, 5):
        primary_fixture = primary_epoch.get(length, primary_held.get(length))
        independent_fixture = independent_fixtures[length]
        for primary_key, independent_key in common_fields:
            equal(
                f"L{length} {primary_key}",
                primary_fixture[primary_key],
                independent_fixture[independent_key],
            )
        equal(
            f"L{length} fine-color collisions",
            primary_fixture[
                "fine_24_color_collision_count"
                if length in (2, 3)
                else "same_color_footprint_support_collisions"
            ],
            independent_fixture["fine_collisions"],
        )
        require(f"L{length} packet overlap", independent_fixture["packet_overlaps"] == 0)
        require(f"L{length} resource overlap", independent_fixture["resource_overlaps"] == 0)
        require(
            f"L{length} spatial geometry",
            independent_fixture["spatial_geometry_failures"] == 0,
        )
        if length in (2, 3):
            equal(
                f"L{length} augmented instructions",
                primary_fixture["augmented_instructions"],
                independent_fixture["instructions"],
            )
            equal(
                f"L{length} route differences",
                primary_fixture["retained_seam_route_reconciliation"]["path_differences"],
                independent_fixture["route_differences"],
            )
            equal(
                f"L{length} first-forward-SWAP deletion detections",
                primary_fixture["first_forward_swap_deletion_detections"],
                independent_fixture["first_forward_swap_deletion_detections"],
            )
            equal(
                f"L{length} dirty macro-bank pairs",
                primary_fixture["dirty_spectator"]["ordered_macro_bank_pairs"],
                independent_fixture["dirty_pairs"],
            )

    direction = canonical_primary["spatial_direction"]
    independent_direction = canonical_independent["direction"]
    for primary_key, independent_key in (
        ("rows", "rows"),
        ("moving", "moving"),
        ("wrong_side_detected", "wrong_side"),
        ("dirty_spatial_input_detected", "dirty_spatial"),
        ("ORIENT_overload_detected", "ORIENT_overload"),
        ("seam_deletion_detected", "seam_deletion"),
        ("exact_packet_equation_rows", "exact_packet_equation_rows"),
        ("packet_reuse_without_reset_changed_bits", "reuse_changed_bits"),
        ("spatial_causal_pairs", "spatial_causal_pairs"),
    ):
        equal(
            "direction " + primary_key,
            direction[primary_key],
            independent_direction[independent_key],
        )
    require(
        "exact packet equation",
        direction["exact_packet_equation"]
        == "PORIENT = POINTER AND BINDER AND ACTUAL AND ADMISS AND LAW AND FRESH AND ORIENT"
        and direction["failure_census"]["exact_packet_equation"] == 0,
    )

    continuity = canonical_primary["continuity"]
    independent_continuity = canonical_independent["continuity"]
    for primary_key, independent_key in (
        ("current_patterns", "patterns"),
        ("covered_full_occupation_columns", "covered_columns"),
        ("frame_rows", "frame_rows"),
        ("product_rows", "product_rows"),
    ):
        equal(
            "continuity " + primary_key,
            continuity[primary_key],
            independent_continuity[independent_key],
        )
    require(
        "continuity zero failures",
        not any(continuity["failure_census"].values())
        and continuity["frame_failures"] == 0
        and continuity["product_failures"] == 0,
    )
    require(
        "24/576 color covariance",
        canonical_primary["color_covariance"]["proper_frames"] == 24
        and canonical_primary["color_covariance"]["ordered_frame_products"] == 576
        and canonical_primary["color_covariance"]["bijection_failures"] == 0
        and canonical_primary["color_covariance"]["product_failures"] == 0,
    )
    passive = canonical_primary["used_epoch_passive_covariance"]
    require(
        "24/576 used-program passive covariance",
        passive["proper_frames"] == 24
        and passive["ordered_frame_products"] == 576
        and passive["frame_path_failures"] == 0
        and passive["signature_product_failures"] == 0
        and passive["path_product_failures"] == 0,
    )
    require(
        "causal/spatial separation",
        len(direction["spatial_causal_pairs"]) == 4
        and not canonical_primary["association_firewall"]["spatial_to_causal_is_function"]
        and canonical_primary["association_firewall"]["acceptance_failures"] == 0,
    )
    require(
        "stage reorder control",
        canonical_primary["noncommuting_stage_reorder_control"]["detected"],
    )

    primary_matter = canonical_primary["mass_contact"]
    independent_matter = canonical_independent["mass_contact"]
    equal("mass fixture", primary_matter["mass_fixture_pass"], independent_matter["mass"])
    equal(
        "contact fixture",
        primary_matter["contact_fixture_pass"],
        independent_matter["contact"],
    )
    equal("mass difference", primary_matter["mass_difference"], independent_matter["mass_difference"])
    equal("contact residual", primary_matter["contact_residual"], independent_matter["contact_residual"])

    return {
        "schema": "cycle872-all-seam-spatial-packet-package-acceptance-v1",
        "status": "pass" if not failures else "fail",
        "claim_scope": (
            "one complete all-seam spatial-direction packet epoch on supplied "
            "clean own-bank inputs; later reset/genesis remains open"
        ),
        "package_manifest": observed_manifest,
        "expected_package_manifest": EXPECTED_MANIFEST,
        "exact_manifest_match": observed_manifest == EXPECTED_MANIFEST,
        "manifest_scope": (
            "all top-level Cycle872-named files directly under repo/package docs, "
            "scripts, and outputs; generated subtrees such as docs/audit and unrelated "
            "repository files are outside this package manifest"
        ),
        "package_sha256": package_hashes,
        "upstream_sha256": upstream_hashes,
        "literal_upstream_pin_count": len(primary_upstream_pins),
        "package_binding_surface": {
            "hard_pinned_by_acceptance_source": tuple(EXPECTED_PACKAGE_SHA256),
            "acceptance_source": (
                "bound by runner_sha256 in this deterministic acceptance receipt"
            ),
            "unavoidable_self_reference_exclusions": (
                "acceptance source cannot hard-code its own final content hash",
                "acceptance receipt cannot contain its own final content hash",
            ),
        },
        "audit_surface": {
            "audit_timeout_sec": AUDIT_TIMEOUT_SEC,
            "child_timeout_sec": CHILD_TIMEOUT_SEC,
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "declared_input_paths": DECLARED_INPUT_PATHS,
            "audit_input_sha256": audit_input_hashes,
            "missing_inputs": audit_missing,
            "duplicate_inputs": len(AUDIT_INPUT_PATHS) - len(set(AUDIT_INPUT_PATHS)),
            "unpinned_nonself_inputs": audit_unpinned,
            "acceptance_source_binding": (
                "self hash recorded as runner_sha256 in the acceptance output receipt"
            ),
            "acceptance_output_receipt": ACCEPTANCE_RECEIPT,
            "acceptance_output_is_input": ACCEPTANCE_RECEIPT in AUDIT_INPUT_PATHS,
        },
        "independent_imported_modules": independent_imports,
        "independent_primary_imported": any(primary_name in row for row in independent_imports),
        "cold_runs": cold_runs,
        "cross_checks": cross_checks,
        "cross_check_count": len(cross_checks),
        "runner_sha256": file_sha256(Path(__file__)),
        "firewall": (
            "no time/tick/occurrence/Event/Record/Born/source/gravity derivation; "
            "causal orientation, couplings, scales, and later bank renewal remain supplied"
        ),
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument(
        "--source-root", type=Path,
        help="upstream repository root; otherwise use CYCLE872_SOURCE_ROOT or cwd",
    )
    args = parser.parse_args()
    source_root = discover_source_root(args.source_root)
    report = build_report(source_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        "CYCLE872_ALL_SEAM_SPATIAL_PACKET_PACKAGE_ACCEPTANCE_PASS"
        if report["status"] == "pass"
        else "CYCLE872_ALL_SEAM_SPATIAL_PACKET_PACKAGE_ACCEPTANCE_FAIL"
    )
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
