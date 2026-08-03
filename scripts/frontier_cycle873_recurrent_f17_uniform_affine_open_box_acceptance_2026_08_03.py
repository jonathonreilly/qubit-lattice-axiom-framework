#!/usr/bin/env python3
"""Cold acceptance for the bounded Cycle873 candidate package.

The static Cycle873 imports are intentional: they expose every computational
child to the repository's restricted audit packet.  The executable path still
validates the citation and package pins, proves the recorded fetched base is an
ancestor of the current checkout, verifies Cycle873 was unused in that base
tree, launches the primary and independent runners from a temporary working
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
from typing import TYPE_CHECKING


# These imports are intentionally type-check-only.  Each module is an
# import-free, byte-exact source view, so the restricted audit packet receives
# the complete Cycle873 computational children without recursively importing
# their large transitive implementation closure.
if TYPE_CHECKING:
    import frontier_cycle873_affine_source_audit_view_part1_2026_08_03  # noqa: F401
    import frontier_cycle873_affine_source_audit_view_part2_2026_08_03  # noqa: F401
    import frontier_cycle873_affine_source_audit_view_part3_2026_08_03  # noqa: F401
    import frontier_cycle873_all_seam_physical_source_audit_view_part1_2026_08_03  # noqa: F401
    import frontier_cycle873_all_seam_physical_source_audit_view_part2_2026_08_03  # noqa: F401
    import frontier_cycle873_all_seam_physical_source_audit_view_part3_2026_08_03  # noqa: F401
    import frontier_cycle873_all_seam_physical_source_audit_view_part4_2026_08_03  # noqa: F401
    import frontier_cycle873_all_seam_physical_source_audit_view_part5_2026_08_03  # noqa: F401
    import frontier_cycle873_independent_source_audit_view_part1_2026_08_03  # noqa: F401
    import frontier_cycle873_independent_source_audit_view_part2_2026_08_03  # noqa: F401
    import frontier_cycle873_independent_source_audit_view_part3_2026_08_03  # noqa: F401
    import frontier_cycle873_independent_source_audit_view_part4_2026_08_03  # noqa: F401
    import frontier_cycle873_local_constraints_source_audit_view_part1_2026_08_03  # noqa: F401
    import frontier_cycle873_local_constraints_source_audit_view_part2_2026_08_03  # noqa: F401
    import frontier_cycle873_local_constraints_source_audit_view_part3_2026_08_03  # noqa: F401
    import frontier_cycle873_primary_source_audit_view_part1_2026_08_03  # noqa: F401


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
EXPECTED_MANIFEST_SHA256 = "f5239fc8436f39c4043e1028968d79407934d9c9b9464cbcb415d1700db8591d"

LOCAL_SOURCE_VIEWS = (
    "scripts/frontier_cycle873_local_constraints_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_local_constraints_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_local_constraints_source_audit_view_part3_2026_08_03.py",
)
PHYSICAL_SOURCE_VIEWS = (
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part4_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part5_2026_08_03.py",
)
INDEPENDENT_SOURCE_VIEWS = (
    "scripts/frontier_cycle873_independent_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part4_2026_08_03.py",
)
PRIMARY_SOURCE_VIEWS = (
    "scripts/frontier_cycle873_primary_source_audit_view_part1_2026_08_03.py",
)
AFFINE_SOURCE_VIEWS = (
    "scripts/frontier_cycle873_affine_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_affine_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_affine_source_audit_view_part3_2026_08_03.py",
)
SOURCE_VIEW_SETS = {
    LOCAL: LOCAL_SOURCE_VIEWS,
    PHYSICAL: PHYSICAL_SOURCE_VIEWS,
    INDEPENDENT: INDEPENDENT_SOURCE_VIEWS,
    PRIMARY: PRIMARY_SOURCE_VIEWS,
    AFFINE: AFFINE_SOURCE_VIEWS,
}
SOURCE_VIEW_FILES = tuple(
    path for paths in SOURCE_VIEW_SETS.values() for path in paths
)

AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_F17_UNIFORM_AFFINE_OPEN_BOX_CYCLE873_BOUNDED_THEOREM_NOTE_2026-08-03.md",
    "logs/runner-cache/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.txt",
    "logs/runner-cache/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.txt",
    "outputs/cycle873_f17_open_box_local_constraints_core_receipt_2026_08_03.json",
    "outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json",
    "outputs/cycle873_recurrent_f17_uniform_affine_open_box_citation_manifest_2026_08_03.json",
    "outputs/cycle873_recurrent_f17_uniform_affine_open_box_independent_check_receipt_2026_08_03.json",
    "outputs/cycle873_recurrent_f17_uniform_affine_open_box_primary_receipt_2026_08_03.json",
    "outputs/cycle873_uniform_affine_gauss_intertwiner_core_receipt_2026_08_03.json",
    "scripts/frontier_cycle873_f17_open_box_local_constraints_core_2026_08_03.py",
    "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py",
    "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_acceptance_2026_08_03.py",
    "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_independent_check_2026_08_03.py",
    "scripts/frontier_cycle873_recurrent_f17_uniform_affine_open_box_primary_2026_08_03.py",
    "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py",
    "scripts/frontier_cycle873_local_constraints_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_local_constraints_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_local_constraints_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part4_2026_08_03.py",
    "scripts/frontier_cycle873_all_seam_physical_source_audit_view_part5_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part3_2026_08_03.py",
    "scripts/frontier_cycle873_independent_source_audit_view_part4_2026_08_03.py",
    "scripts/frontier_cycle873_primary_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_affine_source_audit_view_part1_2026_08_03.py",
    "scripts/frontier_cycle873_affine_source_audit_view_part2_2026_08_03.py",
    "scripts/frontier_cycle873_affine_source_audit_view_part3_2026_08_03.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_ARTIFACT_SHA256 = {
    NOTE: "3cd18032e6f14007e11c2709e70021b9fbcd81fcfc8974cbc650f64cd4df010e",
    PRIMARY_LOG: "72be1cd183bf85663c6726223f9db9fb61be3e80b6ed0f3d386f32849312eb74",
    INDEPENDENT_LOG: "6689ee8aac078f36507af89c20a90a19ea0721d34af74b1a98318cec06c35812",
    PHYSICAL_RECEIPT: "397657af570393fad9967edc55e74f7a66f46e8284fd5102be0f5e1df9247d0b",
    LOCAL_RECEIPT: "ed30056eaeeac03301849d3f386a6d8d0b7accbef2237b4c388e85a595212f1e",
    AFFINE_RECEIPT: "d5d0dec904a034a0994d1e98e1c38b966240b91a3ad3435ac7bb01011c5b21b9",
    PRIMARY_RECEIPT: "08a2ad65a8d17e308ca08a0a9c51882bf8df4b0a13005103f17890d77a27a5ec",
    INDEPENDENT_RECEIPT: "4fdff3e14f0c0253b13c38349fbe0e1bff9c6b9bdee60b7e86d58f9b98d6b5bd",
    PHYSICAL: "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7",
    LOCAL: "70d7362a2f534bd94b5b421f38e0c0509483ed8c1962b83f21f790b4c1dcb685",
    AFFINE: "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9",
    PRIMARY: "ab9f365c167b8fafb4f54508c0fb38b325bf687fdf8f222bc9aa833ad65dfc62",
    INDEPENDENT: "02c3f321ba5ef1dce723ed04bd83919839648fd89202f607b6cc680645a97734",
    LOCAL_SOURCE_VIEWS[0]: "b85d277b1fc6e4a8fabd1e62c52d369bbe8d2f5762ce7f44eac35539c09ff16e",
    LOCAL_SOURCE_VIEWS[1]: "24441e0224609c66bfd3cb3e7e924e2cef071125d1f90f8ca26b84487074f779",
    LOCAL_SOURCE_VIEWS[2]: "207f75b20961a5c33d40dc2a38fa26c753ce3287d5655f7bb6815b35ddae2aeb",
    PHYSICAL_SOURCE_VIEWS[0]: "5079d8aacdfe2ab0154714526043dab928a85e83727a8783d93a36daa893adf0",
    PHYSICAL_SOURCE_VIEWS[1]: "62ec0b8329ec6169985c4d27e38d36ea03cd67a8e0dc831c21eb3c231babd4a6",
    PHYSICAL_SOURCE_VIEWS[2]: "91c7f8b8c2d866f9782a4770b4686d920ff2b6b505133f71eb5edaea9a95b6b3",
    PHYSICAL_SOURCE_VIEWS[3]: "dceec4cc66669c9aa98b9bc7dcae53d9b4b70c244b7323986d246d66b4d17725",
    PHYSICAL_SOURCE_VIEWS[4]: "2f1158a27ab6f9a2d55580b4dbcaf4c740b30434f5e8b9ff2ecc5d353d77ddc0",
    INDEPENDENT_SOURCE_VIEWS[0]: "bb8adcca563d1c70c9e491ff75127b8c9d41240afa040deb742e478f353788e9",
    INDEPENDENT_SOURCE_VIEWS[1]: "74aa3ba5a44dd478c81247703ed545c176154a877bcdd3270ebbaa35629a396c",
    INDEPENDENT_SOURCE_VIEWS[2]: "755a6c2e4e63fc6d6238b7ad053a32d0218e4a415a9c23c0973a3aa367658a1f",
    INDEPENDENT_SOURCE_VIEWS[3]: "8801f70904fa2cb54e1be6458b349b154e0f29d533df218574ddabc7a7efd412",
    PRIMARY_SOURCE_VIEWS[0]: "59e7bc8fbefbf318d0dec4d79535a49f96278bde2c310fccb1ba65cddcad8669",
    AFFINE_SOURCE_VIEWS[0]: "f2dc97037cdab023921274ff47b4a07c5de0f7f94d63df24cdc374363f8bd52b",
    AFFINE_SOURCE_VIEWS[1]: "3bed3a64dfd06ac42b304af088e4be06dc5d2a14432dccb0037772987ffbb7a5",
    AFFINE_SOURCE_VIEWS[2]: "b826bb8cc96dde8aa7d2f6cc89fbd924b7e0fb25fc134c4a47a9bb89f0d0e50c",
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
    *SOURCE_VIEW_FILES,
)))

EXPECTED_EXCLUSIONS = {
    MANIFEST,
    ACCEPTANCE,
    ACCEPTANCE_RECEIPT,
}

NOTE_REQUIRED_TEXT = (
    "Type: bounded_theorem",
    "Status: bounded construction candidate.",
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
    "No-go gate status: `FAIL`. Controlled demotion: `partial-narrowing`.",
    "2,448 rows with seam bits",
    "612 `a=b=1` rows carry the FSWAP minus sign",
    "supplied lattice parity origin",
    "does not prove unit-translation/origin-shift equivalence",
    "The 20 M2 persistent bank is not the whole routing substrate.",
    "The exact candidate surface has 32 files:",
    "16 import-free byte-exact source-view modules",
    "[Minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md)",
    "[Cycle 870 recurrent physical-M2 matter compiler]",
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def literal_assignment_bytes(source: bytes, name: str):
    tree = ast.parse(source.decode("utf-8", errors="strict"))
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def parse_source_view(raw: bytes, label: str) -> dict[str, object]:
    metadata = {
        key: literal_assignment_bytes(raw, key)
        for key in (
            "TARGET_SOURCE", "PART_ORDINAL", "PART_COUNT", "FIRST_SOURCE_LINE",
            "LAST_SOURCE_LINE", "TOTAL_SOURCE_LINES", "SOURCE_FINAL_NEWLINE",
            "EXPECTED_SOURCE_SHA256",
        )
    }
    prefix = b"# C873SRC "
    rows: list[tuple[int, bytes]] = []
    for line in raw.splitlines(keepends=True):
        if line.startswith(prefix):
            if not line.endswith(b"\n") or line.endswith(b"\r\n"):
                raise ValueError(f"{label}: payload newline")
            number_raw, separator, payload = line[len(prefix):].partition(b"|")
            if separator != b"|" or len(number_raw) != 6 or not number_raw.isdigit():
                raise ValueError(f"{label}: payload prefix")
            rows.append((int(number_raw), payload[:-1]))
        elif line.startswith(b"# C873SRC"):
            raise ValueError(f"{label}: malformed payload prefix")
    first = int(metadata["FIRST_SOURCE_LINE"])
    last = int(metadata["LAST_SOURCE_LINE"])
    if [number for number, _ in rows] != list(range(first, last + 1)):
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
    raw_overrides = raw_overrides or {}
    parts = []
    expected_next = 1
    total_lines = None
    final_newline = None
    expected_source_sha = EXPECTED_ARTIFACT_SHA256[target]
    for ordinal, view_path in enumerate(view_paths, 1):
        raw = raw_overrides.get(view_path, (ROOT / view_path).read_bytes())
        if (
            enforce_view_hashes
            and sha256(raw).hexdigest() != EXPECTED_ARTIFACT_SHA256[view_path]
        ):
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
    actual = actual_override if actual_override is not None else (ROOT / target).read_bytes()
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


def source_view_certificate(
    target: str, view_paths: tuple[str, ...]
) -> dict[str, object]:
    certificate = validate_source_view_set(target, view_paths)
    first_path = view_paths[0]
    original = (ROOT / first_path).read_bytes()

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

    prefix_mutation = original.replace(b"# C873SRC ", b"# C873SRX ", 1)
    ordinal_mutation = original.replace(
        b"PART_ORDINAL = 1\n", b"PART_ORDINAL = 9\n", 1
    )
    first_payload_end = original.index(b"\n", original.index(b"# C873SRC "))
    payload_mutation = original[:first_payload_end] + b"X" + original[first_payload_end:]
    try:
        validate_source_view_set(
            target,
            view_paths,
            actual_override=(ROOT / target).read_bytes() + b" ",
        )
    except ValueError:
        child_mutation_detected = True
    else:
        child_mutation_detected = False
    certificate["mutation_controls"] = {
        "hard_pin_view_mutation_detected": rejected(
            payload_mutation, enforce_view_hashes=True
        ),
        "malformed_prefix_detected": rejected(
            prefix_mutation, enforce_view_hashes=False
        ),
        "ordinal_mutation_detected": rejected(
            ordinal_mutation, enforce_view_hashes=False
        ),
        "payload_mutation_detected": rejected(
            payload_mutation, enforce_view_hashes=False
        ),
        "actual_child_mutation_detected": child_mutation_detected,
    }
    return certificate


def package_manifest() -> tuple[str, ...]:
    output: list[str] = []
    for directory in ("docs", "scripts", "outputs", "logs/runner-cache"):
        base = ROOT / directory
        if not base.is_dir():
            continue
        output.extend(
            str(path.relative_to(ROOT))
            for path in base.iterdir()
            if path.is_file()
            and "cycle873" in path.name.lower()
            and path.suffix != ".pyc"
        )
    return tuple(sorted(output))


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

    observed_package_files = package_manifest()
    if observed_package_files != EXPECTED_PACKAGE_FILES:
        failures.append("exact Cycle873 package manifest")

    audit_missing = tuple(
        path for path in AUDIT_INPUT_PATHS if not (ROOT / path).is_file()
    )
    audit_unpinned = tuple(
        path
        for path in AUDIT_INPUT_PATHS
        if path not in {ACCEPTANCE, MANIFEST}
        and path not in EXPECTED_ARTIFACT_SHA256
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

    physical_l2 = next(
        (
            row for row in receipts["physical"].get("fixtures", ())
            if tuple(row.get("shape", ())) == (2, 2, 2)
        ),
        {},
    )
    physical_l2_schedule_sha256 = physical_l2.get(
        "augmented_epoch_ledgers", {}
    ).get("A_F17_only", {}).get("seam_stage_schedule_sha256")
    independent_l2_schedule = receipts["independent"].get(
        "literal_L2_emitted_schedule", {}
    )
    grouped_macro_literal_crosscheck = {
        "scope": "all 12 F17-only seams of the 2x2x2 fixture",
        "physical_core_schedule_sha256": physical_l2_schedule_sha256,
        "independent_schedule_sha256": independent_l2_schedule.get(
            "schedule_sha256"
        ),
        "independent_word_count": len(
            independent_l2_schedule.get("independent_word_sha256", ())
        ),
        "larger_fixture_boundary": (
            "the 3x3x3 and held 3x2x2 fixtures use the same pinned generic "
            "emitter but do not receive a second per-word digest reconstruction"
        ),
    }
    grouped_macro_literal_crosscheck["exact_match"] = (
        independent_l2_schedule.get("shape") == [2, 2, 2]
        and independent_l2_schedule.get("seams") == 12
        and grouped_macro_literal_crosscheck["independent_word_count"] == 12
        and independent_l2_schedule.get("schedule_sha256")
            == physical_l2_schedule_sha256
        and independent_l2_schedule.get("physical_core_F17_only_schedule_sha256")
            == physical_l2_schedule_sha256
        and independent_l2_schedule.get("schedule_hash_match") is True
    )
    if not grouped_macro_literal_crosscheck["exact_match"]:
        failures.append("L2 grouped-macro literal-emission crosscheck")

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
        "observed_package_files": observed_package_files,
        "candidate_artifact_sha256": observed,
        "candidate_artifact_hash_drift": drift,
        "citation_manifest_sha256": manifest_hash,
        "upstream_citation_hash_drift": upstream_drift,
        "self_reference_exclusions": manifest.get("self_reference_exclusions", {}),
        "missing_package_files_before_acceptance_output": missing_files,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "audit_input_missing": audit_missing,
        "audit_input_unpinned": audit_unpinned,
        "source_views": source_views,
        "missing_note_required_text": missing_note_text,
        "independent_imports": sorted(independent_imports),
        "forbidden_independent_imports": forbidden_imports,
        "canonical_receipt_status": {
            label: receipt.get("status") for label, receipt in receipts.items()
        },
        "L2_grouped_macro_literal_emission_crosscheck": (
            grouped_macro_literal_crosscheck
        ),
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
