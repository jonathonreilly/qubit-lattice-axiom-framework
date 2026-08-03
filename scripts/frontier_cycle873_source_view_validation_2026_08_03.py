#!/usr/bin/env python3
"""Byte-exact source-view validation used by the Cycle 873 acceptance runner."""

from __future__ import annotations

import ast
from hashlib import sha256
from pathlib import Path


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
    root: Path,
    target: str,
    view_paths: tuple[str, ...],
    expected_artifact_sha256: dict[str, str],
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
    expected_source_sha = expected_artifact_sha256[target]
    for ordinal, view_path in enumerate(view_paths, 1):
        raw = raw_overrides.get(view_path, (root / view_path).read_bytes())
        if (
            enforce_view_hashes
            and sha256(raw).hexdigest() != expected_artifact_sha256[view_path]
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
    actual = actual_override if actual_override is not None else (root / target).read_bytes()
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
    root: Path,
    target: str,
    view_paths: tuple[str, ...],
    expected_artifact_sha256: dict[str, str],
) -> dict[str, object]:
    certificate = validate_source_view_set(
        root, target, view_paths, expected_artifact_sha256
    )
    first_path = view_paths[0]
    original = (root / first_path).read_bytes()

    def rejected(raw: bytes, *, enforce_view_hashes: bool) -> bool:
        try:
            validate_source_view_set(
                root,
                target,
                view_paths,
                expected_artifact_sha256,
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
            root,
            target,
            view_paths,
            expected_artifact_sha256,
            actual_override=(root / target).read_bytes() + b" ",
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
