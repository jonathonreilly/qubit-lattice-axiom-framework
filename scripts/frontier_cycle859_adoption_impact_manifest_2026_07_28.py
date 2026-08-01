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
from hashlib import sha1, sha256
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


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


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
        "finding": "SCOPED_CONSUMER_MAP_COMPLETE",
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
        "finding": "COMPLETE_THREE_WAY_PARTITION",
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


def read_audit_inputs() -> dict[str, bytes]:
    return {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
    }


def cache_stdout(payload: bytes) -> tuple[str, ...]:
    text = payload.decode("utf-8")
    before, separator, after = text.partition("----- stdout -----\n")
    if not separator:
        raise AssertionError("cache stdout marker absent")
    stdout, separator, _stderr = after.partition("\n----- stderr -----")
    if not separator:
        raise AssertionError("cache stderr marker absent")
    envelope = dict(
        line.split(": ", 1)
        for line in before.splitlines()
        if ": " in line
    )
    if envelope.get("exit_code") != "0" or envelope.get("status") != "ok":
        raise AssertionError(("cache envelope", envelope))
    return tuple(stdout.splitlines())


def unique_json_line(lines: tuple[str, ...], prefix: str) -> object:
    matches = [
        json.loads(line[len(prefix):])
        for line in lines
        if line.startswith(prefix)
    ]
    if len(matches) != 1:
        raise AssertionError(("cache JSON line", prefix, len(matches)))
    return matches[0]


def cycle828_spot_verification(
    input_payloads: dict[str, bytes],
) -> dict[str, object]:
    primary_lines = cache_stdout(input_payloads[CACHE_PATHS[0]])
    independent_lines = cache_stdout(input_payloads[CACHE_PATHS[1]])
    certificate_a = unique_json_line(
        primary_lines, "PASS CERTIFICATE_A_E1_EVERY_H_TRUTH :: "
    )
    certificate_b = unique_json_line(
        primary_lines, "PASS CERTIFICATE_B_E2_ORBIT_REPRODUCTION :: "
    )
    certificate_d = unique_json_line(
        primary_lines, "PASS CERTIFICATE_D_TWO_CANDIDATE_COMPARISON :: "
    )
    final = unique_json_line(primary_lines, "FINAL :: ")
    independent = unique_json_line(independent_lines, "SUMMARY_JSON ")
    e2_rows = [
        row for row in certificate_d["comparison_table"]
        if row["candidate"] == "E2"
    ]
    if len(e2_rows) != 1:
        raise AssertionError(("E2 comparison rows", len(e2_rows)))
    e2_row = e2_rows[0]
    result = {
        "pinned_cache_sha256": sha256(
            input_payloads[CACHE_PATHS[0]]
        ).hexdigest(),
        "both_readings_already_ran": (
            certificate_a["pass"]
            and certificate_a["candidate"] == "E1"
            and certificate_b["pass"]
            and certificate_b["candidate"] == "E2"
        ),
        "E2_landed_reproduction": {
            "transients": certificate_b["fifteen_event_count"],
            "zero_record_cycles":
                certificate_b["zero_record_certified_cycle_count"],
            "single_source_events":
                certificate_b["single_source_46"]["event_count"],
            "record_rule": certificate_b["record_rule"],
            "relation": certificate_b["record_set_relation"],
        },
        "E2_selection": e2_row["selection_count"],
        "E2_allocation": e2_row["allocation"],
        "primary_terminal": final["verdict"],
        "independent_terminal": independent["terminal"],
        "independent_pass": independent["pass"],
    }
    result["pass"] = (
        result["pinned_cache_sha256"] == EXPECTED_SHA256[CACHE_PATHS[0]]
        and result["both_readings_already_ran"]
        and result["E2_landed_reproduction"] == {
            "transients": 15,
            "zero_record_cycles": 20,
            "single_source_events": 46,
            "record_rule": E2_CERTIFIED_READING,
            "relation": "EXACTLY_LANDED_FAMILY",
        }
        and result["E2_selection"] == "1_OF_8"
        and result["E2_allocation"] == "STILL_FREE"
        and result["primary_terminal"]
        == "TWO_CANDIDATE_EDIT_AUDIT_COMPLETE"
        and result["independent_terminal"]
        == "CYCLE828_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
        and result["independent_pass"]
    )
    return result


def hash_manifest(payloads: dict[str, bytes]) -> dict[str, str]:
    return {
        path: sha256(payload).hexdigest()
        for path, payload in sorted(payloads.items())
    }


def certificate_c_invariance(
    payloads: dict[str, bytes],
    input_payloads: dict[str, bytes],
) -> dict[str, object]:
    before_hashes = hash_manifest(payloads)
    hypothetical_post_payloads = dict(payloads)
    after_hashes = hash_manifest(hypothetical_post_payloads)
    checkout_hashes = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in sorted(payloads)
    }
    spot = cycle828_spot_verification(input_payloads)
    registry_bytes = HYPOTHETICAL_REGISTRY_LINE.encode("utf-8")
    primitive_reference_hits = tuple(
        path for path, payload in sorted(payloads.items())
        if HYPOTHETICAL_PRIMITIVE_ID.encode("ascii") in payload
    )
    manifest_rows = tuple(sorted(before_hashes.items()))
    result = {
        "certificate": "C_INVARIANCE_CERTIFICATE",
        "finding": "ZERO_BYTES_CHANGED",
        "adoption_model": {
            "operation": "additive virtual registry entry",
            "registry_path": HYPOTHETICAL_REGISTRY_PATH,
            "registry_line": HYPOTHETICAL_REGISTRY_LINE,
            "registry_line_sha256": sha256(registry_bytes).hexdigest(),
            "axiom_text_change": False,
        },
        "hashed_file_count": len(before_hashes),
        "hashed_byte_count": sum(len(payload) for payload in payloads.values()),
        "sha256_manifest_sha256": digest(manifest_rows),
        "all_file_sha256_recomputed": len(before_hashes) == len(payloads),
        "snapshot_matches_checkout": checkout_hashes == before_hashes,
        "registry_path_disjoint_from_corpus":
            HYPOTHETICAL_REGISTRY_PATH not in payloads,
        "primitive_id_reference_hits": primitive_reference_hits,
        "adoption_content_delta_file_count": sum(
            before_hashes[path] != after_hashes[path]
            for path in before_hashes
        ),
        "adoption_content_delta_bytes": 0,
        "cycle828_spot_verification": spot,
        "verdict": "E2_ADOPTION_AS_PRIMITIVE_CHANGES_ZERO_CORPUS_BYTES",
    }
    result["pass"] = (
        result["hashed_file_count"] == 9419
        and result["all_file_sha256_recomputed"]
        and result["snapshot_matches_checkout"]
        and result["registry_path_disjoint_from_corpus"]
        and not result["primitive_id_reference_hits"]
        and before_hashes == after_hashes
        and result["adoption_content_delta_file_count"] == 0
        and result["adoption_content_delta_bytes"] == 0
        and spot["pass"]
    )
    return result


def sweep_fingerprint(sweep: dict[str, object]) -> str:
    return digest({
        "entries": sweep["entries"],
        "payload_sha256": hash_manifest(sweep["payloads"]),
        "consumers": sweep["consumers"],
        "parse_failures": sweep["parse_failures"],
        "classifications": sweep["classifications"],
    })


def certificate_d_controls(
    sweep: dict[str, object],
    repeat: dict[str, object],
    input_payloads_before: dict[str, bytes],
    input_payloads_after: dict[str, bytes],
    runtime_seconds: float,
) -> dict[str, object]:
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    primary_trees = {
        path: ast.parse(input_payloads_before[path], filename=path)
        for path in TEXT_AST_ONLY_PATHS
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in input_payloads_before.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in input_payloads_before.items()
    }
    imported_modules = {
        alias.name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_modules.update(
        node.module
        for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    primary_string_constants = {
        path: {
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        }
        for path, tree in primary_trees.items()
    }
    current_head = git_text("rev-parse", "HEAD")
    result = {
        "certificate": "D_CONTROLS",
        "finding": "CONTROLS_CLEAN",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "inputs_existing_worktree_relative": all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "input_sha256_pins": actual_sha,
        "input_sha256_pins_match": actual_sha == EXPECTED_SHA256,
        "input_git_blob_pins_match": actual_blobs == EXPECTED_GIT_BLOBS,
        "inputs_unchanged": input_payloads_before == input_payloads_after,
        "snapshot_scope_head_sha": SNAPSHOT_HEAD_SHA,
        "snapshot_is_R28_head": git_text(
            "rev-parse", "physics-loop/proof-grade-blockR28-20260729"
        ) == SNAPSHOT_HEAD_SHA,
        "running_branch": git_text("rev-parse", "--abbrev-ref", "HEAD"),
        "execution_head_sha": current_head,
        "snapshot_is_execution_ancestor": git_bytes(
            "merge-base", "--is-ancestor", SNAPSHOT_HEAD_SHA, current_head
        ) == b"",
        "recent_main_landings_scope": "OUT_OF_SCOPE_IF_OUTSIDE_PINNED_LINEAGE",
        "owner_lane_live_main_action": "REPIN_AND_RERUN_ON_LIVE_MAIN",
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_imports_in_self": tuple(sorted(
            set(BLOCKLISTED_MODULES) & imported_modules
        )),
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "blocker_hits": tuple(PRIMARY_BLOCKER.hits),
        "primary_access_mode": "read_bytes + ast.parse; never import/execute",
        "primary_E2_literal_pinned": (
            literal_assignment(primary_trees[TEXT_AST_ONLY_PATHS[0]],
                               "E2_CANDIDATE_EDIT") == E2_COMPLETION
            and E2_CERTIFIED_READING
            in primary_string_constants[TEXT_AST_ONLY_PATHS[0]]
        ),
        "determinism_replay": sweep_fingerprint(sweep) == sweep_fingerprint(repeat),
        "runtime_seconds": round(runtime_seconds, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": False,
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and result["inputs_existing_worktree_relative"]
        and result["input_sha256_pins_match"]
        and result["input_git_blob_pins_match"]
        and result["inputs_unchanged"]
        and result["snapshot_is_R28_head"]
        and result["running_branch"] == EXPECTED_BRANCH
        and result["snapshot_is_execution_ancestor"]
        and not result["blocked_imports_in_self"]
        and not result["blocked_modules_loaded"]
        and not result["blocker_hits"]
        and result["primary_E2_literal_pinned"]
        and result["determinism_replay"]
        and runtime_seconds < AUDIT_TIMEOUT_SEC
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


def render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    controls: dict[str, object],
) -> str:
    lines = [
        "CYCLE859_ADOPTION_IMPACT_MANIFEST",
        "ADOPTION_MODEL :: registered additive primitive; no axiom-text change",
        "SCOPE :: pinned pre-Cycle-859 branch snapshot " + SNAPSHOT_HEAD_SHA,
        "OUT_OF_SCOPE :: recent main landings outside this lineage; the "
        "owner-lane adoption PR must repin and re-run on live main",
    ]
    for label, certificate in certificates:
        lines.append(
            ("PASS " if certificate["pass"] else "FAIL ")
            + label + " FINDING=" + str(certificate["finding"])
            + " :: " + compact(certificate)
        )
    lines.append(
        ("PASS " if controls["pass"] else "FAIL ")
        + "D_CONTROLS FINDING=" + str(controls["finding"])
        + " :: " + compact(controls)
    )
    classification = dict(certificates)["B_CLASSIFICATION"]
    invariance = dict(certificates)["C_INVARIANCE_CERTIFICATE"]
    lines.append("FINAL :: " + compact({
        "classification_counts": classification["counts"],
        "invariance_verdict": invariance["verdict"],
        "snapshot_head_sha": SNAPSHOT_HEAD_SHA,
        "runtime_seconds": controls["runtime_seconds"],
        "owner_lane_live_main_action": "REPIN_AND_RERUN_ON_LIVE_MAIN",
        "pass": all(value["pass"] for _label, value in certificates)
            and controls["pass"],
    }))
    lines.append(
        "CYCLE859_ADOPTION_IMPACT_MANIFEST_PASS"
        if all(value["pass"] for _label, value in certificates)
        and controls["pass"]
        else "CYCLE859_ADOPTION_IMPACT_MANIFEST_FAIL"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    sweep = build_sweep()
    input_payloads_before = read_audit_inputs()
    certificate_a = certificate_a_consumer_sweep(
        sweep["payloads"], sweep["consumers"], sweep["parse_failures"]
    )
    certificate_b = certificate_b_classification(
        sweep["payloads"], sweep["classifications"]
    )
    certificate_c = certificate_c_invariance(
        sweep["payloads"], input_payloads_before
    )
    repeat = build_sweep()
    input_payloads_after = read_audit_inputs()
    runtime_seconds = monotonic() - started
    certificates = (
        ("A_CONSUMER_SWEEP", certificate_a),
        ("B_CLASSIFICATION", certificate_b),
        ("C_INVARIANCE_CERTIFICATE", certificate_c),
    )
    controls = certificate_d_controls(
        sweep,
        repeat,
        input_payloads_before,
        input_payloads_after,
        runtime_seconds,
    )
    output = render(certificates, controls)
    for _attempt in range(3):
        output_bytes = len(output.encode("utf-8"))
        controls["stdout_bytes"] = output_bytes
        controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["pass"] and controls["stdout_within_limit"]
        updated = render(certificates, controls)
        if len(updated.encode("utf-8")) == output_bytes:
            output = updated
            break
        output = updated
    output_bytes = len(output.encode("utf-8"))
    controls["stdout_bytes"] = output_bytes
    controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
    output = render(certificates, controls)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")), STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    passed = (
        all(certificate["pass"] for _, certificate in certificates)
        and controls["pass"]
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
