#!/usr/bin/env python3
"""Cycle 859: scoped adoption-impact manifest for Record completion E2.

The audited corpus is the top-level tracked ``scripts/*.py`` and ``docs/*.md``
tree at the pinned pre-Cycle-859 commit.  Source runners are inspected only as
text/AST.  This runner neither imports a cited primary nor writes an adoption.
"""
from __future__ import annotations

import ast
import base64
from collections import Counter
from hashlib import sha256
import importlib.abc
import json
import lzma
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic
from typing import Iterable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
SNAPSHOT_HEAD_SHA = "e3a77fa19d5a4840c19534e70df727751be3e0bb"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR29-20260729"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle828_axiom_edit_audit_2026_07_28.py",
    "scripts/frontier_cycle828_edit_audit_independent_check_2026_07_28.py",
    "logs/runner-cache/frontier_cycle828_axiom_edit_audit_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle828_edit_audit_independent_check_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[:2]
CACHE_PATHS = AUDIT_INPUT_PATHS[2:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "74d6aefee383ced099d04fde79b6389f9f22fd38379ce83c99f2518246248f7e",
    AUDIT_INPUT_PATHS[1]:
        "1be437ddb9623e3aea2370c41c1294f95edd8ab51cd01e31a69aee52fd0e4f44",
    AUDIT_INPUT_PATHS[2]:
        "5504ba516c7413956797040e1299856df4422f8fd0f7903bb31ab7f3bd28e803",
    AUDIT_INPUT_PATHS[3]:
        "2742da81f9b35d77b36311dc46cf6272989a8c96aae3e7c85db958f8f239b85b",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "fddeda1828e480ca963fc7940b20c84a15615e60",
    AUDIT_INPUT_PATHS[1]: "5f60605431e731b759c5b4301fe57da65ab868c5",
    AUDIT_INPUT_PATHS[2]: "083db6741d258d269a6bb29356038b1cc7213da2",
    AUDIT_INPUT_PATHS[3]: "62e0adb6802b31fd7e6f073e05c51637f037e4ae",
}

E2_COMPLETION = "Records form at first orbit admissibility."
E2_CERTIFIED_READING = (
    "record set = first-clean orbit-return selection-event set"
)
HYPOTHETICAL_REGISTRY_PATH = (
    "owner-lane/primitive-registry/record-formation.jsonl"
)
HYPOTHETICAL_PRIMITIVE_ID = (
    "record_formation_first_orbit_admissibility_v1"
)
HYPOTHETICAL_REGISTRY_LINE = json.dumps({
    "primitive_id": HYPOTHETICAL_PRIMITIVE_ID,
    "completion": "E2",
    "text": E2_COMPLETION,
    "certified_plain_reading": E2_CERTIFIED_READING,
    "operation": "additive_registry_entry_no_axiom_text_change",
}, sort_keys=True, separators=(",", ":"))

TOKEN_CLASSES = (
    "FORMATION_MOMENT",
    "RECORD_RULE",
    "EXPLICIT_E1_E2",
)
FORMATION_PATTERNS = (
    re.compile(r"\borbit[-_ ]moments?\b", re.IGNORECASE),
    re.compile(r"\babsolute_H\b"),
    re.compile(r"\b(?:MOMENT|[A-Z][A-Z0-9_]*_MOMENTS?)\b"),
)
RECORD_RULE_PATTERNS = (
    re.compile(r"\bfirst[-_ ]clean\b", re.IGNORECASE),
    re.compile(r"\borbit[-_ ]admissibility\b", re.IGNORECASE),
    re.compile(r"\borbit[-_ ]return\b", re.IGNORECASE),
)
EXPLICIT_E1_E2_PATTERNS = (
    re.compile(
        r"(?<![A-Za-z0-9])E[12]_(?:CANDIDATE|READING|EVERY_H|AXES|"
        r"OCCURRENCES?|EDIT|RECORD)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\bE[12]\s*(?:\N{EM DASH}|--|:|=|-)\s*[\"'\N{LEFT DOUBLE "
        r"QUOTATION MARK}]?(?:Records?\b|candidate|reading|every|orbit|first)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:candidate|reading|completion|adoption|adopted)\s+E[12]\b",
        re.IGNORECASE,
    ),
)
EXPLICIT_RULE_PATTERNS = (
    re.compile(
        r"Records form at first (?:orbit )?admissibility\.",
        re.IGNORECASE,
    ),
    re.compile(
        r"record set\s*=\s*first[-_ ]clean orbit[-_ ]return "
        r"selection[-_ ]event set",
        re.IGNORECASE,
    ),
)
TRACKED_PATH_PATTERN = re.compile(
    r"(?:scripts/[^/]+\.py|docs/[^/]+\.md)\Z"
)
ROOT = Path(__file__).resolve().parents[1]


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if either provenance-only Cycle-828 runner is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_bytes(*arguments: str, input_bytes: bytes | None = None) -> bytes:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        input=input_bytes,
        capture_output=True,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode("utf-8").strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def snapshot_entries() -> tuple[tuple[str, str], ...]:
    raw = git_bytes("ls-tree", "-rz", "--full-tree", SNAPSHOT_HEAD_SHA)
    rows = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, object_type, object_id = metadata.decode("ascii").split()
        path = raw_path.decode("utf-8")
        if TRACKED_PATH_PATTERN.fullmatch(path):
            if object_type != "blob" or mode not in {"100644", "100755"}:
                raise AssertionError(("non-blob corpus member", path, metadata))
            rows.append((path, object_id))
    return tuple(sorted(rows))


def load_snapshot_payloads(
    entries: tuple[tuple[str, str], ...],
) -> dict[str, bytes]:
    request = "".join(f"{object_id}\n" for _path, object_id in entries)
    raw = git_bytes("cat-file", "--batch", input_bytes=request.encode("ascii"))
    offset = 0
    payloads: dict[str, bytes] = {}
    for path, expected_object_id in entries:
        end = raw.index(b"\n", offset)
        header = raw[offset:end].decode("ascii")
        object_id, object_type, raw_size = header.split()
        if object_id != expected_object_id or object_type != "blob":
            raise AssertionError(("cat-file header", path, header))
        size = int(raw_size)
        start = end + 1
        finish = start + size
        payloads[path] = raw[start:finish]
        if raw[finish:finish + 1] != b"\n":
            raise AssertionError(("cat-file framing", path))
        offset = finish + 1
    if offset != len(raw):
        raise AssertionError(("cat-file trailing bytes", len(raw) - offset))
    return payloads


def count_patterns(text: str, patterns: Iterable[re.Pattern[str]]) -> int:
    return sum(len(tuple(pattern.finditer(text))) for pattern in patterns)


def contextual_e_mentions(text: str) -> int:
    """Count E1/E2 labels only when syntax identifies the Record reading."""

    return count_patterns(text, EXPLICIT_E1_E2_PATTERNS)


def scan_fragment(text: str) -> dict[str, int]:
    return {
        "FORMATION_MOMENT": count_patterns(text, FORMATION_PATTERNS),
        "RECORD_RULE": count_patterns(text, RECORD_RULE_PATTERNS),
        "EXPLICIT_E1_E2": contextual_e_mentions(text),
    }


class ScriptTokenVisitor(ast.NodeVisitor):
    """Count requested tokens in imports, strings, and loaded fields."""

    def __init__(self) -> None:
        self.counts = {
            token_class: Counter({
                "imports": 0,
                "string_constants": 0,
                "field_reads": 0,
            })
            for token_class in TOKEN_CLASSES
        }

    def add(self, channel: str, text: str) -> None:
        found = scan_fragment(text)
        for token_class, count in found.items():
            self.counts[token_class][channel] += count

    def visit_Import(self, node: ast.Import) -> None:  # noqa: N802
        for alias in node.names:
            self.add("imports", alias.name)
            if alias.asname:
                self.add("imports", alias.asname)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # noqa: N802
        if node.module:
            self.add("imports", node.module)
        for alias in node.names:
            self.add("imports", alias.name)
            if alias.asname:
                self.add("imports", alias.asname)

    def visit_Constant(self, node: ast.Constant) -> None:  # noqa: N802
        if isinstance(node.value, str):
            self.add("string_constants", node.value)

    def visit_Name(self, node: ast.Name) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            self.add("field_reads", node.id)

    def visit_Attribute(self, node: ast.Attribute) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            self.add("field_reads", node.attr)
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            key = node.slice
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                self.add("field_reads", key.value)
        self.generic_visit(node)


def normalized_map(
    counts: dict[str, Counter[str]],
) -> dict[str, dict[str, int]]:
    result = {}
    for token_class in TOKEN_CLASSES:
        channels = {
            name: count
            for name, count in sorted(counts[token_class].items())
            if count
        }
        total = sum(channels.values())
        if total:
            result[token_class] = {**channels, "total": total}
    return result


def sweep_payloads(
    payloads: dict[str, bytes],
) -> tuple[dict[str, dict[str, dict[str, int]]], tuple[str, ...]]:
    consumers = {}
    parse_failures = []
    for path in sorted(payloads):
        try:
            text = payloads[path].decode("utf-8")
        except UnicodeDecodeError as error:
            parse_failures.append(f"{path}:UTF8:{error}")
            continue
        if path.startswith("scripts/"):
            try:
                tree = ast.parse(text, filename=path)
            except SyntaxError as error:
                parse_failures.append(
                    f"{path}:AST:{error.lineno}:{error.offset}:{error.msg}"
                )
                continue
            visitor = ScriptTokenVisitor()
            visitor.visit(tree)
            token_map = normalized_map(visitor.counts)
        else:
            found = scan_fragment(text)
            token_map = {
                token_class: {"text": count, "total": count}
                for token_class, count in found.items()
                if count
            }
        if token_map:
            consumers[path] = token_map
    return consumers, tuple(parse_failures)


def total_for(
    token_map: dict[str, dict[str, int]],
    token_class: str,
) -> int:
    return token_map.get(token_class, {}).get("total", 0)


def is_explicit_reading(
    path: str,
    payload: bytes,
    token_map: dict[str, dict[str, int]],
) -> bool:
    if total_for(token_map, "EXPLICIT_E1_E2"):
        return True
    text = payload.decode("utf-8")
    return any(pattern.search(text) for pattern in EXPLICIT_RULE_PATTERNS)


def classify(
    payloads: dict[str, bytes],
    consumers: dict[str, dict[str, dict[str, int]]],
) -> dict[str, tuple[str, ...]]:
    rows: dict[str, list[str]] = {
        "NO_CONSUMPTION": [],
        "CORPUS_IMPLICIT": [],
        "EXPLICIT_READING": [],
    }
    for path in sorted(payloads):
        token_map = consumers.get(path)
        if not token_map:
            label = "NO_CONSUMPTION"
        elif is_explicit_reading(path, payloads[path], token_map):
            label = "EXPLICIT_READING"
        else:
            label = "CORPUS_IMPLICIT"
        rows[label].append(path)
    return {label: tuple(paths) for label, paths in rows.items()}


def common_prefix_length(left: str, right: str) -> int:
    limit = min(len(left), len(right))
    for index in range(limit):
        if left[index] != right[index]:
            return index
    return limit


def encode_path_list(paths: tuple[str, ...]) -> dict[str, object]:
    previous = ""
    delta_rows = []
    for path in paths:
        prefix = common_prefix_length(previous, path)
        delta_rows.append(f"{prefix:x}:{path[prefix:]}")
        previous = path
    raw = "\n".join(delta_rows).encode("utf-8")
    encoded = base64.b85encode(lzma.compress(
        raw, format=lzma.FORMAT_XZ, preset=9 | lzma.PRESET_EXTREME
    )).decode("ascii")
    return {
        "codec": "sorted-prefix-delta-lines+xz9e+base85",
        "count": len(paths),
        "decoded_sha256": sha256(raw).hexdigest(),
        "data": encoded,
    }


def decode_path_list(package: dict[str, object]) -> tuple[str, ...]:
    compressed = base64.b85decode(str(package["data"]).encode("ascii"))
    raw = lzma.decompress(compressed, format=lzma.FORMAT_XZ)
    if sha256(raw).hexdigest() != package["decoded_sha256"]:
        raise AssertionError("classification list digest mismatch")
    if not raw:
        return ()
    previous = ""
    paths = []
    for row in raw.decode("utf-8").splitlines():
        raw_prefix, suffix = row.split(":", 1)
        prefix = int(raw_prefix, 16)
        path = previous[:prefix] + suffix
        paths.append(path)
        previous = path
    return tuple(paths)


def certificate_a_consumer_sweep(
    payloads: dict[str, bytes],
    consumers: dict[str, dict[str, dict[str, int]]],
    parse_failures: tuple[str, ...],
) -> dict[str, object]:
    output_consumer_map = {
        path: {
            token_class: total_for(token_map, token_class)
            for token_class in TOKEN_CLASSES
            if total_for(token_map, token_class)
        }
        for path, token_map in consumers.items()
    }
    class_file_counts = {
        token_class: sum(
            total_for(token_map, token_class) > 0
            for token_map in consumers.values()
        )
        for token_class in TOKEN_CLASSES
    }
    class_token_counts = {
        token_class: sum(
            total_for(token_map, token_class)
            for token_map in consumers.values()
        )
        for token_class in TOKEN_CLASSES
    }
    result = {
        "certificate": "A_CONSUMER_SWEEP",
        "snapshot_scope_head_sha": SNAPSHOT_HEAD_SHA,
        "snapshot_definition":
            "top-level tracked scripts/*.py and docs/*.md blobs in pinned tree",
        "out_of_scope":
            "recent main landings outside this pinned lineage are out of scope",
        "scanned_file_count": len(payloads),
        "script_count": sum(path.startswith("scripts/") for path in payloads),
        "doc_count": sum(path.startswith("docs/") for path in payloads),
        "consumer_file_count": len(consumers),
        "token_class_file_counts": class_file_counts,
        "token_class_occurrence_counts": class_token_counts,
        "script_method": "AST imports + string constants + loaded field reads",
        "docs_method": "text",
        "consumer_file_to_token_class_counts": output_consumer_map,
        "parse_failures": parse_failures,
    }
    result["pass"] = (
        len(payloads) == 9419
        and result["script_count"] == 5468
        and result["doc_count"] == 3951
        and not parse_failures
        and set(consumers) <= set(payloads)
    )
    return result


def certificate_b_classification(
    payloads: dict[str, bytes],
    classifications: dict[str, tuple[str, ...]],
) -> dict[str, object]:
    encoded = {
        label: encode_path_list(paths)
        for label, paths in classifications.items()
    }
    decoded = {
        label: decode_path_list(package)
        for label, package in encoded.items()
    }
    all_paths = tuple(sorted(
        path for paths in classifications.values() for path in paths
    ))
    disjoint = sum(len(paths) for paths in classifications.values()) == len(
        set(all_paths)
    )
    result = {
        "certificate": "B_CLASSIFICATION",
        "definitions": {
            "NO_CONSUMPTION": "never touches record formation tokens",
            "CORPUS_IMPLICIT":
                "uses records only via landed behavior; zero content change "
                "under E2; becomes exact",
            "EXPLICIT_READING":
                "quantifies over the E1/E2 reading; re-ratification is "
                "confirmation under E2 because both readings already ran",
        },
        "counts": {
            label: len(paths) for label, paths in classifications.items()
        },
        "full_lists": encoded,
        "full_list_encoding_note":
            "Each complete path list is printed in reversible compressed form "
            "to satisfy the 150KB stdout control.",
        "decode_roundtrip_exact": decoded == classifications,
        "partition_disjoint": disjoint,
        "partition_complete": all_paths == tuple(sorted(payloads)),
    }
    result["pass"] = (
        result["decode_roundtrip_exact"]
        and result["partition_disjoint"]
        and result["partition_complete"]
    )
    return result


def build_sweep() -> dict[str, object]:
    entries = snapshot_entries()
    payloads = load_snapshot_payloads(entries)
    consumers, parse_failures = sweep_payloads(payloads)
    classifications = classify(payloads, consumers)
    return {
        "entries": entries,
        "payloads": payloads,
        "consumers": consumers,
        "parse_failures": parse_failures,
        "classifications": classifications,
    }


def main() -> int:
    started = monotonic()
    sweep = build_sweep()
    certificate_a = certificate_a_consumer_sweep(
        sweep["payloads"], sweep["consumers"], sweep["parse_failures"]
    )
    certificate_b = certificate_b_classification(
        sweep["payloads"], sweep["classifications"]
    )
    runtime_seconds = monotonic() - started
    certificates = (
        ("A_CONSUMER_SWEEP", certificate_a),
        ("B_CLASSIFICATION", certificate_b),
    )
    lines = [
        "CYCLE859_ADOPTION_IMPACT_MANIFEST",
        "SCOPE :: pinned pre-Cycle-859 branch snapshot " + SNAPSHOT_HEAD_SHA,
        "OUT_OF_SCOPE :: recent main landings outside this lineage; the "
        "owner-lane adoption PR must repin and re-run on live main",
    ]
    for label, certificate in certificates:
        lines.append(
            ("PASS " if certificate["pass"] else "FAIL ")
            + label + " :: " + compact(certificate)
        )
    lines.append("RUNTIME_SECONDS :: " + f"{runtime_seconds:.6f}")
    output = "\n".join(lines) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", output_bytes, STDOUT_LIMIT_BYTES))
    sys.stdout.write(output)
    return 0 if all(certificate["pass"] for _, certificate in certificates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
