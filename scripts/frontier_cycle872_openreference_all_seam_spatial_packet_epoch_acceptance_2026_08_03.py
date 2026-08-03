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
from typing import TYPE_CHECKING


# These imports are intentionally type-check-only.  Each module is a readable,
# byte-exact source view with no imports of its own, so the restricted audit
# packet receives the complete child sources without executing or recursively
# importing the children in this acceptance process.
if TYPE_CHECKING:
    import frontier_cycle872_independent_source_audit_view_part1_2026_08_03  # noqa: F401
    import frontier_cycle872_independent_source_audit_view_part2_2026_08_03  # noqa: F401
    import frontier_cycle872_primary_source_audit_view_part1_2026_08_03  # noqa: F401
    import frontier_cycle872_primary_source_audit_view_part2_2026_08_03  # noqa: F401
    import frontier_cycle872_primary_source_audit_view_part3_2026_08_03  # noqa: F401
    import frontier_cycle872_primary_source_audit_view_part4_2026_08_03  # noqa: F401


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PRIMARY = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py"
INDEPENDENT = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py"
ACCEPTANCE = "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_acceptance_2026_08_03.py"
PRIMARY_RECEIPT = "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json"
INDEPENDENT_RECEIPT = "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json"
ACCEPTANCE_RECEIPT = "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_package_acceptance_receipt_2026_08_03.json"
NOTE = "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md"
PRIMARY_SOURCE_VIEWS = (
    "scripts/frontier_cycle872_primary_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part4_2026_08_03.py",
)
INDEPENDENT_SOURCE_VIEWS = (
    "scripts/frontier_cycle872_independent_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle872_independent_source_audit_view_part2_2026_08_03.py",
)
SOURCE_VIEW_SETS = {
    PRIMARY: PRIMARY_SOURCE_VIEWS,
    INDEPENDENT: INDEPENDENT_SOURCE_VIEWS,
}
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
    "scripts/frontier_cycle872_primary_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part4_2026_08_03.py",
    "scripts/frontier_cycle872_independent_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle872_independent_source_audit_view_part2_2026_08_03.py",
)
DECLARED_INPUT_PATHS = (
    "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_acceptance_2026_08_03.py",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03.py",
    "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json",
    "scripts/frontier_cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_2026_08_03.py",
    "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json",
    "scripts/frontier_cycle872_primary_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle872_primary_source_audit_view_part4_2026_08_03.py",
    "scripts/frontier_cycle872_independent_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle872_independent_source_audit_view_part2_2026_08_03.py",
)
EXPECTED_MANIFEST = tuple(sorted((
    NOTE, PRIMARY, INDEPENDENT, ACCEPTANCE,
    PRIMARY_RECEIPT, INDEPENDENT_RECEIPT, ACCEPTANCE_RECEIPT,
    *PRIMARY_SOURCE_VIEWS, *INDEPENDENT_SOURCE_VIEWS,
)))

EXPECTED_PACKAGE_SHA256 = {
    NOTE: "dd218e18d3a24506b11db9fdbad909f899187eeda5bf579a2b1a984afd10c8f7",
    PRIMARY: "c1b32ef8e2a870128b7081a88b920b85c84123d04f98a165bfc7225dcfc716e4",
    INDEPENDENT: "2350243e16aeb39a6a0f20b9a036468c82e541477e206566664c1103fa145523",
    PRIMARY_RECEIPT: "604263a745e50005348ed62fc841520daa6d60b9bb88484240faf219d901058f",
    INDEPENDENT_RECEIPT: "b1007ebffa91a8433e86cf4488bddce4b7c140c03ef40b33987baf9a5f2ba202",
    PRIMARY_SOURCE_VIEWS[0]: "7b1b0e6f767fdd6175935c5afdd00965c3f03bceb0d6051f01037005812df518",
    PRIMARY_SOURCE_VIEWS[1]: "571a3ddb16880a6e73115a2c50214aa046a268f3b8bf9fe0af889bcdfceb4183",
    PRIMARY_SOURCE_VIEWS[2]: "7303cad27a7c65c710f65e75aabdb49195088ad470c51229d853b4c032ae08fa",
    PRIMARY_SOURCE_VIEWS[3]: "46c2fab4bf9ebc71880c4329d15f7847d064f7ea570bbc552fdf3376ae5c600a",
    INDEPENDENT_SOURCE_VIEWS[0]: "4dd5ae62e9573f0c3fe84d49f2e379b3ccd2fcf12226868d61d261618f2740d7",
    INDEPENDENT_SOURCE_VIEWS[1]: "b26fc999db1e1f0bda9bfcb885fd0ab4f8497cd9fe8bfb9fd2d5fba4522eca34",
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


def literal_assignment_bytes(source: bytes, name: str):
    tree = ast.parse(source.decode("utf-8", errors="strict"))
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def literal_assignment(path: Path, name: str):
    return literal_assignment_bytes(path.read_bytes(), name)


def parse_source_view(raw: bytes, label: str) -> dict[str, object]:
    """Parse one readable source mirror without normalizing any source byte."""
    metadata = {
        key: literal_assignment_bytes(raw, key)
        for key in (
            "TARGET_SOURCE", "PART_ORDINAL", "PART_COUNT", "FIRST_SOURCE_LINE",
            "LAST_SOURCE_LINE", "TOTAL_SOURCE_LINES", "SOURCE_FINAL_NEWLINE",
            "EXPECTED_SOURCE_SHA256",
        )
    }
    prefix = b"# C872SRC "
    rows: list[tuple[int, bytes]] = []
    for line in raw.splitlines(keepends=True):
        if line.startswith(prefix):
            if not line.endswith(b"\n") or line.endswith(b"\r\n"):
                raise ValueError(f"{label}: payload newline")
            number_raw, separator, payload = line[len(prefix):].partition(b"|")
            if separator != b"|" or len(number_raw) != 6 or not number_raw.isdigit():
                raise ValueError(f"{label}: payload prefix")
            rows.append((int(number_raw), payload[:-1]))
        elif line.startswith(b"# C872SRC"):
            raise ValueError(f"{label}: malformed payload prefix")
    first = int(metadata["FIRST_SOURCE_LINE"])
    last = int(metadata["LAST_SOURCE_LINE"])
    expected_numbers = list(range(first, last + 1))
    if [number for number, _ in rows] != expected_numbers:
        raise ValueError(f"{label}: noncontiguous payload rows")
    metadata["rows"] = rows
    metadata["view_path"] = label
    return metadata


def validate_source_view_set(
    target: str,
    view_paths: tuple[str, ...],
    *,
    raw_overrides: dict[str, bytes] | None = None,
    actual_override: bytes | None = None,
    enforce_view_hashes: bool = True,
) -> dict[str, object]:
    """Reconstruct one child source exactly from ordered, fixed view parts."""
    raw_overrides = raw_overrides or {}
    parts = []
    expected_next = 1
    total_lines = None
    final_newline = None
    expected_source_sha = EXPECTED_PACKAGE_SHA256[target]
    for ordinal, view_path in enumerate(view_paths, 1):
        raw = raw_overrides.get(view_path, (PACKAGE_ROOT / view_path).read_bytes())
        if enforce_view_hashes and sha256(raw).hexdigest() != EXPECTED_PACKAGE_SHA256[view_path]:
            raise ValueError(f"{view_path}: view hash")
        part = parse_source_view(raw, view_path)
        if part["TARGET_SOURCE"] != target:
            raise ValueError(f"{view_path}: target")
        if part["PART_ORDINAL"] != ordinal or part["PART_COUNT"] != len(view_paths):
            raise ValueError(f"{view_path}: ordinal")
        if part["FIRST_SOURCE_LINE"] != expected_next:
            raise ValueError(f"{view_path}: gap or overlap")
        if part["EXPECTED_SOURCE_SHA256"] != expected_source_sha:
            raise ValueError(f"{view_path}: source hash declaration")
        if total_lines is None:
            total_lines = part["TOTAL_SOURCE_LINES"]
            final_newline = part["SOURCE_FINAL_NEWLINE"]
        if (
            part["TOTAL_SOURCE_LINES"] != total_lines
            or part["SOURCE_FINAL_NEWLINE"] != final_newline
        ):
            raise ValueError(f"{view_path}: inconsistent source metadata")
        expected_next = int(part["LAST_SOURCE_LINE"]) + 1
        parts.append(part)
    if total_lines is None or expected_next != int(total_lines) + 1:
        raise ValueError(f"{target}: incomplete source range")
    numbered_rows = [row for part in parts for row in part["rows"]]
    numbers = [number for number, _ in numbered_rows]
    if numbers != list(range(1, int(total_lines) + 1)):
        raise ValueError(f"{target}: global line range")
    reconstructed = b"".join(
        payload
        + (b"\n" if number < int(total_lines) or bool(final_newline) else b"")
        for number, payload in numbered_rows
    )
    actual = actual_override if actual_override is not None else (PACKAGE_ROOT / target).read_bytes()
    if reconstructed != actual:
        raise ValueError(f"{target}: reconstructed bytes")
    if sha256(actual).hexdigest() != expected_source_sha:
        raise ValueError(f"{target}: literal source hash")
    return {
        "target_source": target,
        "view_paths": view_paths,
        "part_count": len(parts),
        "total_source_lines": total_lines,
        "source_final_newline": final_newline,
        "source_bytes": len(actual),
        "source_sha256": sha256(actual).hexdigest(),
        "line_range": (numbers[0], numbers[-1]),
        "contiguous": len(numbers) == len(set(numbers)) == int(total_lines),
        "byte_identical": reconstructed == actual,
    }


def source_view_certificate(target: str, view_paths: tuple[str, ...]) -> dict[str, object]:
    certificate = validate_source_view_set(target, view_paths)
    first_path = view_paths[0]
    original = (PACKAGE_ROOT / first_path).read_bytes()

    def rejected(raw: bytes, *, enforce_view_hashes: bool) -> bool:
        try:
            validate_source_view_set(
                target,
                view_paths,
                raw_overrides={first_path: raw},
                enforce_view_hashes=enforce_view_hashes,
            )
        except (KeyError, SyntaxError, UnicodeDecodeError, ValueError):
            return True
        return False

    prefix_mutation = original.replace(b"# C872SRC ", b"# C872SRX ", 1)
    ordinal_mutation = original.replace(b"PART_ORDINAL = 1\n", b"PART_ORDINAL = 9\n", 1)
    first_payload_end = original.index(b"\n", original.index(b"# C872SRC "))
    payload_mutation = original[:first_payload_end] + b"X" + original[first_payload_end:]
    try:
        validate_source_view_set(
            target,
            view_paths,
            actual_override=(PACKAGE_ROOT / target).read_bytes() + b" ",
        )
    except ValueError:
        child_mutation_detected = True
    else:
        child_mutation_detected = False
    certificate["mutation_controls"] = {
        "hard_pin_view_mutation_detected": rejected(payload_mutation, enforce_view_hashes=True),
        "malformed_prefix_detected": rejected(prefix_mutation, enforce_view_hashes=False),
        "ordinal_mutation_detected": rejected(ordinal_mutation, enforce_view_hashes=False),
        "payload_mutation_detected": rejected(payload_mutation, enforce_view_hashes=False),
        "actual_child_mutation_detected": child_mutation_detected,
    }
    return certificate


def package_manifest(root: Path = PACKAGE_ROOT) -> tuple[str, ...]:
    """Enumerate top-level Cycle872 package files in the three owned namespaces.

    Generated audit-ledger shards live below ``docs/audit`` and are validation
    outputs, not author-owned package files.  The package contract places all
    thirteen canonical artifacts directly in ``docs``, ``scripts``, or
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
        failures.append("exact thirteen-file package manifest")
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

    source_views: dict[str, object] = {}
    for target, view_paths in SOURCE_VIEW_SETS.items():
        try:
            certificate = source_view_certificate(target, view_paths)
        except (KeyError, SyntaxError, UnicodeDecodeError, ValueError) as error:
            failures.append(f"source view: {target}: {error}")
        else:
            source_views[target] = certificate
            if not all(certificate["mutation_controls"].values()):
                failures.append("source view mutation controls: " + target)

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
        "source_views": source_views,
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
