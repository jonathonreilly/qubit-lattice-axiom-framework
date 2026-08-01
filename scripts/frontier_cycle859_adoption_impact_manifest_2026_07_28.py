#!/usr/bin/env python3
"""Cycle 859 v3: snapshot-pinned adoption-impact manifest for Record E2.

The audited corpus is the top-level tracked ``scripts/*.py`` and ``docs/*.md``
tree at the pinned pre-Cycle-859 commit.  Source runners are inspected only as
text/AST.  Consumer detection is the union of the v1 primary design and the
independent checker's broader design.  This runner neither imports a cited
primary nor writes an adoption.
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


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
BASE_R28_SHA = "e3a77fa19d5a4840c19534e70df727751be3e0bb"
SNAPSHOT_COMMIT_SHA = "d6a514430ac9921882017ba6424d289e2dc6b288"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR29-20260729"
MANIFEST_PATH = "scripts/frontier_cycle859_adoption_impact_manifest_2026_07_28.py"
CACHE_CONTAMINATION_NOTE = (
    "Cycle 859 v2 swept the working-tree snapshot; after its clean run, "
    "the block note, runner caches, and receipt quoting the E2 wording "
    "contaminated the rebuild, and failing caches shipped. Cycle 859 v3 "
    "repairs that incident by sweeping only the Git tree pinned at "
    f"{SNAPSHOT_COMMIT_SHA} via git ls-tree and git show."
)
EXPECTED_CLASSIFICATION_COUNTS = {
    "NO_CONSUMPTION": 9320,
    "CORPUS_IMPLICIT": 69,
    "EXPLICIT_READING": 31,
}
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
)
BROAD_E1_E2_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])E[12](?![A-Za-z0-9])"
)
RECORD_CONTEXT_PATTERN = re.compile(
    r"\brecord(?:s|ed|ing)?\b|record[_-]", re.IGNORECASE
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
V1_DETECTOR_SET = "CYCLE859_V1_PRIMARY_TOKEN_NEEDLE_AST_DESIGN"
CHECKER_DETECTOR_SET = (
    "CYCLE859_INDEPENDENT_BROADER_NEEDLE_AST_DATAFLOW_DESIGN"
)
CONSUMER_DETECTOR_UNION = (V1_DETECTOR_SET, CHECKER_DETECTOR_SET)

# The independent design is reproduced here as a separately named detector
# set.  Broad candidates remain an attack surface; only lexical or bounded
# semantic evidence promotes a path into the consumer union.
CHECKER_DECLARED_NEEDLE_FAMILIES = {
    "formation": ("form", "forms", "formed", "formation"),
    "cadence": ("cadence", "clock", "boundary"),
    "orbit_return": ("orbit", "return", "admissible", "admissibility"),
    "stamp": ("stamp", "timestamp", "time", "tick"),
    "moment": ("moment", "moments"),
    "labels": ("E1", "E2"),
    "record_rule": ("record", "records", "selection", "event", "clean"),
}
CHECKER_FORMATION_STAMPS = frozenset({
    252, 371, 444, 532, 681, 1385, 14739, 14744, 33195, 51115,
})
CHECKER_LATE_FORMATION_STAMPS = frozenset({14739, 14744, 33195, 51115})
CHECKER_FORMATION_LANE_CYCLES = frozenset({
    792, 794, 796, 799, 813, 814, 818, 819, 820, 822, 828, 830, 832,
    837, 839, 842, 845, 848, 851, 853, 854, 855,
})
CHECKER_SEMANTIC_FIELDS = frozenset({
    "first_clean_t",
    "claimed_first_clean_t",
    "clean_moments",
    "observed_clean_moments",
    "period_clean_moments",
    "identity_moments",
    "resolution_moment",
    "moment_certificate",
    "moment_formula",
    "transient_cohort_keys",
    "earlier_transient_keys",
    "first_clean_events_found",
    "missed_first_clean_events",
})
CHECKER_E_LABEL = re.compile(r"(?<![A-Za-z0-9])E[12](?![A-Za-z0-9])")
CHECKER_RECORD_WORD = re.compile(
    r"\brecord(?:s|ed|ing)?\b|record[_-]", re.IGNORECASE
)
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
    raw = git_bytes(
        "ls-tree", "-r", "-z", "--full-tree", SNAPSHOT_COMMIT_SHA
    )
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
    payloads: dict[str, bytes] = {}
    for path, expected_object_id in entries:
        payload = git_bytes("show", f"{SNAPSHOT_COMMIT_SHA}:{path}")
        if git_blob_sha(payload) != expected_object_id:
            raise AssertionError(("git show blob mismatch", path))
        payloads[path] = payload
    return payloads


def count_patterns(text: str, patterns: Iterable[re.Pattern[str]]) -> int:
    return sum(len(tuple(pattern.finditer(text))) for pattern in patterns)


def contextual_e_mentions(text: str) -> int:
    """Count E1/E2 labels only when syntax identifies the Record reading."""

    positions = set()
    for pattern in EXPLICIT_E1_E2_PATTERNS:
        for match in pattern.finditer(text):
            label = BROAD_E1_E2_PATTERN.search(match.group())
            if label:
                positions.add(match.start() + label.start())
    for match in BROAD_E1_E2_PATTERN.finditer(text):
        window = text[max(0, match.start() - 200):match.end() + 200]
        if RECORD_CONTEXT_PATTERN.search(window):
            positions.add(match.start())
    return len(positions)


def checker_word_terms(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[A-Za-z]+|[0-9]+", text))


def checker_formation_lane_refs(text: str) -> tuple[str, ...]:
    found = set()
    for match in re.finditer(
        r"frontier_cycle([0-9]{3})_[A-Za-z0-9_]+", text
    ):
        if int(match.group(1)) in CHECKER_FORMATION_LANE_CYCLES:
            found.add(match.group())
    return tuple(sorted(found))


def checker_core_lexical_features(text: str) -> frozenset[str]:
    """Normalized-word replay of the independent lexical surface."""

    lowered = text.lower()
    if not any(
        token in lowered
        for token in ("orbit", "first", "moment", "absolute_h")
    ):
        return frozenset()
    features = set()

    def joined(left: str, right: str) -> bool:
        return bool(re.search(
            rf"(?<![A-Za-z0-9_]){left}[-_ ]{right}(?![A-Za-z0-9_])",
            text,
            re.IGNORECASE,
        ))

    if joined("orbit", "moments?"):
        features.add("ORBIT_MOMENT")
    if joined("orbit", "return"):
        features.add("ORBIT_RETURN")
    if joined("orbit", "admissibility"):
        features.add("ORBIT_ADMISSIBILITY")
    if joined("first", "clean"):
        features.add("FIRST_CLEAN")
    if re.search(
        r"(?<![A-Za-z0-9_])absolute_H(?![A-Za-z0-9_])", text
    ):
        features.add("ABSOLUTE_H_SYMBOL")
    for symbol in re.findall(
        r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9_]*(?![A-Za-z0-9_])", text
    ):
        components = symbol.split("_")
        if symbol == "MOMENT" or (
            len(components) >= 2
            and components[-1] in {"MOMENT", "MOMENTS"}
        ):
            features.add("CONSTANT_MOMENT_FIELD")
    return frozenset(features)


def checker_explicit_reading_features(text: str) -> frozenset[str]:
    if (
        "E1" not in text
        and "E2" not in text
        and "record" not in text.lower()
    ):
        return frozenset()
    features = set()
    for match in CHECKER_E_LABEL.finditer(text):
        window = text[max(0, match.start() - 200):match.end() + 200]
        if CHECKER_RECORD_WORD.search(window):
            features.add("E_LABEL_WITH_RECORD_CONTEXT")
    for symbol in re.findall(
        r"(?<![A-Za-z0-9_])E[12]_[A-Za-z0-9_]+", text
    ):
        components = {part.upper() for part in symbol.split("_")[1:]}
        if components & {
            "CANDIDATE", "READING", "EVERY", "AXES", "OCCURRENCE",
            "OCCURRENCES", "EDIT", "RECORD", "FORMATION",
        }:
            features.add("E_LABELED_READING_FIELD")
    lowered_terms = tuple(
        term.lower() for term in checker_word_terms(text)
    )
    phrases = (
        ("records", "form", "at", "first", "admissibility"),
        ("records", "form", "at", "first", "orbit", "admissibility"),
        (
            "record", "set", "first", "clean", "orbit", "return",
            "selection", "event", "set",
        ),
    )
    for phrase in phrases:
        width = len(phrase)
        if any(
            lowered_terms[index:index + width] == phrase
            for index in range(len(lowered_terms) - width + 1)
        ):
            features.add("PLAIN_RECORD_FORMATION_RULE")
    return frozenset(features)


def checker_broad_candidate_features(text: str) -> frozenset[str]:
    """Overinclusive independent needles; semantic evidence adjudicates."""

    lowered = text.lower()
    if not any(token in lowered for token in (
        "formation", "cadence", "orbit", "stamp", "moment", "record",
        "transient", "zero-record", "zero_record", "e1", "e2",
    )):
        return frozenset()
    terms = {term.lower() for term in checker_word_terms(text)}
    features = set()
    if "formation" in terms and terms & {
        "record", "records", "moment", "stamp",
    }:
        features.add("BROAD_FORMATION_CONTEXT")
    if "cadence" in terms and terms & {
        "record", "records", "orbit", "selection",
    }:
        features.add("BROAD_CADENCE_CONTEXT")
    if terms & {"stamp", "timestamp"} and terms & {
        "record", "records", "moment", "selection",
    }:
        features.add("BROAD_STAMP_CONTEXT")
    if terms & {"moment", "moments"} and terms & {
        "transient", "transients", "clean", "selection", "formation",
        "cohort", "cohorts",
    }:
        features.add("BROAD_MOMENT_CONTEXT")
    if "orbit" in terms and terms & {
        "return", "admissible", "admissibility",
    }:
        features.add("BROAD_ORBIT_RETURN_CONTEXT")
    if terms & {"e1", "e2"} and terms & {
        "record", "records", "reading", "formation",
    }:
        features.add("BROAD_E1_E2_CONTEXT")
    if re.search(r"\bzero[-_ ]record\w*\b", lowered):
        features.add("BROAD_ZERO_RECORD_CONTEXT")
    return frozenset(features)


class CheckerScriptProbe(ast.NodeVisitor):
    """Collect the independent AST/data-flow consumer channels."""

    def __init__(self) -> None:
        self.core_features: set[str] = set()
        self.explicit_features: set[str] = set()
        self.broad_features: set[str] = set()
        self.loaded_fields: set[str] = set()
        self.semantic_fields: set[str] = set()
        self.integer_constants: set[int] = set()
        self.lane_refs: set[str] = set()
        self.alias_edges: set[tuple[str, str]] = set()
        self.json_calls: set[str] = set()

    def add_fragment(self, channel: str, value: str) -> None:
        self.core_features.update(checker_core_lexical_features(value))
        self.explicit_features.update(
            checker_explicit_reading_features(value)
        )
        self.broad_features.update(
            checker_broad_candidate_features(value)
        )
        if channel in {"string", "import"}:
            self.lane_refs.update(checker_formation_lane_refs(value))
        lowered = value.lower()
        if lowered in CHECKER_SEMANTIC_FIELDS:
            self.semantic_fields.add(lowered)
        elif len(value) < 2048:
            for field in CHECKER_SEMANTIC_FIELDS:
                if re.search(
                    rf"(?<![A-Za-z0-9_]){re.escape(field)}"
                    rf"(?![A-Za-z0-9_])",
                    value,
                    re.IGNORECASE,
                ):
                    self.semantic_fields.add(field)

    def visit_Import(self, node: ast.Import) -> None:  # noqa: N802
        for alias in node.names:
            self.add_fragment("import", alias.name)
            if alias.asname:
                self.add_fragment("import", alias.asname)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # noqa: N802
        if node.module:
            self.add_fragment("import", node.module)
        for alias in node.names:
            self.add_fragment("import", alias.name)
            if alias.asname:
                self.add_fragment("import", alias.asname)

    def visit_Constant(self, node: ast.Constant) -> None:  # noqa: N802
        if isinstance(node.value, str):
            self.add_fragment("string", node.value)
        elif isinstance(node.value, int) and not isinstance(node.value, bool):
            self.integer_constants.add(node.value)

    def visit_Name(self, node: ast.Name) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            self.loaded_fields.add(node.id)
            self.add_fragment("field", node.id)

    def visit_Attribute(self, node: ast.Attribute) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            self.loaded_fields.add(node.attr)
            self.add_fragment("field", node.attr)
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            key = node.slice
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                self.loaded_fields.add(key.value)
                self.add_fragment("field", key.value)
                self.visit(node.value)
                return
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:  # noqa: N802
        source_fields = {
            child.value
            for child in ast.walk(node.value)
            if isinstance(child, ast.Constant)
            and isinstance(child.value, str)
            and child.value.lower() in CHECKER_SEMANTIC_FIELDS
        }
        targets = {
            child.id
            for target in node.targets
            for child in ast.walk(target)
            if isinstance(child, ast.Name)
        }
        self.alias_edges.update(
            (target, source)
            for target in targets
            for source in source_fields
        )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802
        function = node.func
        if isinstance(function, ast.Attribute) and function.attr in {
            "loads", "load", "dumps", "dump",
        }:
            self.json_calls.add(function.attr)
        self.generic_visit(node)


def checker_lexical_classification(
    text: str,
    probe: CheckerScriptProbe | None,
) -> tuple[str, tuple[str, ...]]:
    if probe is None:
        core = set(checker_core_lexical_features(text))
        explicit = set(checker_explicit_reading_features(text))
    else:
        core = set(probe.core_features)
        explicit = set(probe.explicit_features)
    if explicit:
        return "EXPLICIT_READING", tuple(sorted(explicit | core))
    if core:
        return "CORPUS_IMPLICIT", tuple(sorted(core))
    return "NO_CONSUMPTION", ()


def checker_document_semantic_evidence(
    path: str,
    text: str,
) -> tuple[str, ...]:
    cycle_match = re.search(r"CYCLE([0-9]{3})", path)
    if (
        not cycle_match
        or int(cycle_match.group(1)) not in CHECKER_FORMATION_LANE_CYCLES
    ):
        return ()
    lowered = " ".join(text.lower().split())
    evidence = set()
    if "record-candidate" in lowered and "moment" in lowered:
        evidence.add("NARRATIVE_RECORD_CANDIDATE_MOMENT")
    if re.search(
        r"\b(?:selection moment|simultaneous selections?)\b", lowered
    ):
        evidence.add("NARRATIVE_SELECTION_MOMENT")
    if re.search(r"cohort(?:'s|s')? own moment", lowered):
        evidence.add("NARRATIVE_COHORT_OWN_MOMENT")
    for match in re.finditer(r"\btransient\w*\b", lowered):
        window = lowered[
            max(0, match.start() - 320):match.end() + 320
        ]
        if re.search(
            r"\b(?:moment|clean|selection|resolved|cohort|funnel|basin)"
            r"\w*\b",
            window,
        ):
            evidence.add("NARRATIVE_TRANSIENT_FAMILY")
            break
    if re.search(r"\bzero[- ]record\w*\b", lowered) and re.search(
        r"\b(?:cycle|transient|clean|selection)\w*\b", lowered
    ):
        evidence.add("NARRATIVE_ZERO_RECORD_FAMILY")
    present_stamps = {
        stamp
        for stamp in CHECKER_LATE_FORMATION_STAMPS
        if str(stamp) in text
    }
    if present_stamps and re.search(
        r"\b(?:selection|clean|funnel|transient|moment)\w*\b", lowered
    ):
        evidence.add("NARRATIVE_PINNED_FORMATION_STAMP")
    return tuple(sorted(evidence))


def checker_script_semantic_evidence(
    path: str,
    probe: CheckerScriptProbe,
) -> tuple[str, ...]:
    cycle_match = re.search(r"frontier_cycle([0-9]{3})_", path)
    if (
        not cycle_match
        or int(cycle_match.group(1)) not in CHECKER_FORMATION_LANE_CYCLES
    ):
        return ()
    fields = {
        field.lower() for field in probe.semantic_fields | probe.loaded_fields
    } & CHECKER_SEMANTIC_FIELDS
    stamps = probe.integer_constants & CHECKER_FORMATION_STAMPS
    late_stamps = stamps & CHECKER_LATE_FORMATION_STAMPS
    evidence = set()
    if "first_clean_t" in fields and stamps:
        evidence.add("AST_ALIASED_FIRST_CLEAN_STAMP")
    if fields & {
        "resolution_moment", "moment_certificate", "transient_cohort_keys",
        "earlier_transient_keys",
    } and (probe.lane_refs or probe.json_calls):
        evidence.add("AST_DOWNSTREAM_FORMATION_RECEIPT")
    if late_stamps and probe.lane_refs:
        evidence.add("AST_PINNED_FUNNEL_STAMP_CONSUMER")
    if fields & {
        "clean_moments", "observed_clean_moments", "period_clean_moments",
        "first_clean_events_found", "missed_first_clean_events",
    } and (stamps or probe.lane_refs):
        evidence.add("AST_CLEAN_MOMENT_FAMILY_CONSUMER")
    if probe.alias_edges and stamps:
        evidence.add("AST_STAMP_ALIAS_DATAFLOW")
    return tuple(sorted(evidence))


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
                self.visit(node.value)
                return
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
) -> tuple[
    dict[str, dict[str, dict[str, int]]],
    dict[str, str],
    dict[str, tuple[str, ...]],
    dict[str, tuple[str, ...]],
    dict[str, tuple[str, ...]],
    tuple[str, ...],
]:
    v1_consumers = {}
    checker_lexical_rows = {}
    checker_lexical_features = {}
    checker_broad_candidates = {}
    checker_semantic_evidence = {}
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
            checker_probe = CheckerScriptProbe()
            checker_probe.visit(tree)
            checker_broad = tuple(sorted(checker_probe.broad_features))
            checker_semantic = checker_script_semantic_evidence(
                path, checker_probe
            )
        else:
            found = scan_fragment(text)
            token_map = {
                token_class: {"text": count, "total": count}
                for token_class, count in found.items()
                if count
            }
            checker_probe = None
            checker_broad = tuple(sorted(
                checker_broad_candidate_features(text)
            ))
            checker_semantic = checker_document_semantic_evidence(path, text)
        if token_map:
            v1_consumers[path] = token_map
        checker_label, checker_features = checker_lexical_classification(
            text, checker_probe
        )
        checker_lexical_rows[path] = checker_label
        if checker_features:
            checker_lexical_features[path] = checker_features
        if checker_broad:
            checker_broad_candidates[path] = checker_broad
        if checker_semantic:
            checker_semantic_evidence[path] = checker_semantic
    return (
        v1_consumers,
        checker_lexical_rows,
        checker_lexical_features,
        checker_broad_candidates,
        checker_semantic_evidence,
        tuple(parse_failures),
    )


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


def classify_v1(
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


def path_labels(
    classifications: dict[str, tuple[str, ...]],
) -> dict[str, str]:
    return {
        path: label
        for label, paths in classifications.items()
        for path in paths
    }


def classify_union(
    payloads: dict[str, bytes],
    v1_classifications: dict[str, tuple[str, ...]],
    checker_lexical_rows: dict[str, str],
    checker_lexical_features: dict[str, tuple[str, ...]],
    checker_semantic_evidence: dict[str, tuple[str, ...]],
) -> tuple[
    dict[str, tuple[str, ...]],
    dict[str, tuple[str, ...]],
    tuple[dict[str, object], ...],
]:
    """Return the monotone union partition and every v1-to-v2 movement."""

    v1_rows = path_labels(v1_classifications)
    rows: dict[str, list[str]] = {
        "NO_CONSUMPTION": [],
        "CORPUS_IMPLICIT": [],
        "EXPLICIT_READING": [],
    }
    union_evidence: dict[str, tuple[str, ...]] = {}
    movements = []
    for path in sorted(payloads):
        v1_label = v1_rows[path]
        checker_label = checker_lexical_rows[path]
        evidence = []
        if v1_label != "NO_CONSUMPTION":
            evidence.append(f"V1:{v1_label}")
        evidence.extend(
            f"CHECKER:LEXICAL:{item}"
            for item in checker_lexical_features.get(path, ())
        )
        evidence.extend(
            f"CHECKER:SEMANTIC:{item}"
            for item in checker_semantic_evidence.get(path, ())
        )
        if (
            v1_label == "EXPLICIT_READING"
            or checker_label == "EXPLICIT_READING"
        ):
            union_label = "EXPLICIT_READING"
        elif (
            v1_label == "CORPUS_IMPLICIT"
            or checker_label == "CORPUS_IMPLICIT"
            or path in checker_semantic_evidence
        ):
            union_label = "CORPUS_IMPLICIT"
        else:
            union_label = "NO_CONSUMPTION"
        rows[union_label].append(path)
        if union_label != "NO_CONSUMPTION":
            union_evidence[path] = tuple(evidence)
        if union_label != v1_label:
            movements.append({
                "path": path,
                "v1_class": v1_label,
                "union_class": union_label,
                "evidence": tuple(evidence),
            })
    return (
        {label: tuple(paths) for label, paths in rows.items()},
        union_evidence,
        tuple(movements),
    )


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
    v1_consumers: dict[str, dict[str, dict[str, int]]],
    checker_lexical_rows: dict[str, str],
    checker_broad_candidates: dict[str, tuple[str, ...]],
    checker_semantic_evidence: dict[str, tuple[str, ...]],
    union_evidence: dict[str, tuple[str, ...]],
    movements: tuple[dict[str, object], ...],
    parse_failures: tuple[str, ...],
) -> dict[str, object]:
    v1_consumer_map = {
        path: {
            token_class: total_for(token_map, token_class)
            for token_class in TOKEN_CLASSES
            if total_for(token_map, token_class)
        }
        for path, token_map in v1_consumers.items()
    }
    class_file_counts = {
        token_class: sum(
            total_for(token_map, token_class) > 0
            for token_map in v1_consumers.values()
        )
        for token_class in TOKEN_CLASSES
    }
    class_token_counts = {
        token_class: sum(
            total_for(token_map, token_class)
            for token_map in v1_consumers.values()
        )
        for token_class in TOKEN_CLASSES
    }
    result = {
        "certificate": "A_CONSUMER_SWEEP",
        "finding": "V2_UNION_CONSUMER_MAP_COMPLETE",
        "snapshot_commit_sha": SNAPSHOT_COMMIT_SHA,
        "snapshot_definition":
            "top-level tracked scripts/*.py and docs/*.md blobs at the "
            "literal pinned Cycle 859 v2 snapshot commit",
        "out_of_scope":
            "recent main landings outside this pinned lineage are out of scope",
        "scanned_file_count": len(payloads),
        "script_count": sum(path.startswith("scripts/") for path in payloads),
        "doc_count": sum(path.startswith("docs/") for path in payloads),
        "consumer_detector_union": CONSUMER_DETECTOR_UNION,
        "detector_designs": {
            V1_DETECTOR_SET: {
                "token_classes": TOKEN_CLASSES,
                "script_method":
                    "AST imports + string constants + loaded field reads",
                "docs_method": "full text",
            },
            CHECKER_DETECTOR_SET: {
                "declared_needle_families":
                    CHECKER_DECLARED_NEEDLE_FAMILIES,
                "script_method":
                    "AST imports/strings/loaded names/attributes/keys; "
                    "assignment alias edges; JSON receipt calls",
                "docs_method":
                    "full text plus bounded semantic-context windows",
            },
        },
        "v1_consumer_file_count": len(v1_consumers),
        "union_consumer_file_count": len(union_evidence),
        "v1_token_class_file_counts": class_file_counts,
        "v1_token_class_occurrence_counts": class_token_counts,
        "v1_consumer_map_sha256": digest(v1_consumer_map),
        "checker_lexical_consumer_file_count": sum(
            label != "NO_CONSUMPTION"
            for label in checker_lexical_rows.values()
        ),
        "checker_broad_candidate_file_count":
            len(checker_broad_candidates),
        "checker_semantic_evidence_file_count":
            len(checker_semantic_evidence),
        "union_consumer_evidence_sha256": digest(union_evidence),
        "v1_to_union_movement_count": len(movements),
        "v1_to_union_movements_sha256": digest(movements),
        "parse_failures": parse_failures,
    }
    result["pass"] = (
        len(payloads) > 0
        and result["script_count"] + result["doc_count"] == len(payloads)
        and all(TRACKED_PATH_PATTERN.fullmatch(path) for path in payloads)
        and not parse_failures
        and set(v1_consumers) <= set(payloads)
        and set(checker_lexical_rows) == set(payloads)
        and set(checker_broad_candidates) <= set(payloads)
        and set(checker_semantic_evidence) <= set(payloads)
        and set(union_evidence) <= set(payloads)
        and all(
            row["v1_class"] != row["union_class"]
            and row["evidence"]
            for row in movements
        )
    )
    return result


def certificate_b_classification(
    payloads: dict[str, bytes],
    classifications: dict[str, tuple[str, ...]],
    v1_classifications: dict[str, tuple[str, ...]],
    movements: tuple[dict[str, object], ...],
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
    v1_explicit = v1_classifications["EXPLICIT_READING"]
    union_explicit = classifications["EXPLICIT_READING"]
    explicit_refire_unchanged = union_explicit == v1_explicit
    if explicit_refire_unchanged:
        refire_statement = (
            "The EXPLICIT_READING refire list is unchanged at "
            f"{len(union_explicit)}; the guarantee stands with corrected "
            "class sizes."
        )
    else:
        refire_statement = (
            "The detector union changed the EXPLICIT_READING refire list "
            f"from {len(v1_explicit)} to {len(union_explicit)}; the prior "
            "guarantee requires review."
        )
    result = {
        "certificate": "B_CLASSIFICATION",
        "finding": "CORRECTED_COMPLETE_THREE_WAY_PARTITION",
        "definitions": {
            "NO_CONSUMPTION":
                "no scoped record-formation consumer evidence detected by "
                "the union of the named v1 and checker designs",
            "CORPUS_IMPLICIT":
                "non-explicit scoped lexical, AST/data-flow, or bounded "
                "narrative receipt: operationally uses landed behavior; "
                "under E2 the pinned 828 cache attests that behavior becomes "
                "exact with zero modeled content change",
            "EXPLICIT_READING":
                "strong E1/E2 Record-reading label or exact candidate/reading "
                "hit; re-ratification is confirmation under E2 because both "
                "readings already ran",
        },
        "classification_kind":
            "SCOPED_UNION_LEXICAL_SEMANTIC_OPERATIONAL_PARTITION",
        "semantic_exhaustiveness_claimed": False,
        "alias_paraphrase_caveat":
            "The partition is exhaustive for the union of both declared "
            "designs and the tracked snapshot, not for dependencies invisible "
            "to both specified sweeps.",
        "consumer_detector_union": CONSUMER_DETECTOR_UNION,
        "v1_counts": {
            label: len(paths)
            for label, paths in v1_classifications.items()
        },
        "counts": {
            label: len(paths) for label, paths in classifications.items()
        },
        "expected_counts": EXPECTED_CLASSIFICATION_COUNTS,
        "counts_exact": {
            label: len(paths) for label, paths in classifications.items()
        } == EXPECTED_CLASSIFICATION_COUNTS,
        "classification_counts_derived_not_expected_constants": True,
        "v1_to_union_movement_count": len(movements),
        "v1_to_union_movements_sha256": digest(movements),
        "explicit_reading_refire_count": len(union_explicit),
        "explicit_reading_refire_list_unchanged": explicit_refire_unchanged,
        "refire_guarantee_stands": explicit_refire_unchanged,
        "refire_statement": refire_statement,
        "full_consumer_lists": {
            label: encoded[label]
            for label in ("CORPUS_IMPLICIT", "EXPLICIT_READING")
        },
        "NO_CONSUMPTION_complement": {
            "definition":
                "sorted scoped snapshot paths minus both full consumer lists",
            "count": len(classifications["NO_CONSUMPTION"]),
            "path_list_sha256": digest(
                classifications["NO_CONSUMPTION"]
            ),
        },
        "full_list_encoding_note":
            "Both complete consumer lists are printed reversibly; the full "
            "NO_CONSUMPTION list is their exact complement in the printed "
            "pinned snapshot scope and is digest-bound.",
        "decode_recipe":
            "For each consumer list: base85-decode; xz-decompress; for each "
            "hexprefix:suffix line, path=previous[:int(hexprefix,16)]+suffix; "
            "then subtract both lists from sorted snapshot paths for NO.",
        "decode_roundtrip_exact": decoded == classifications,
        "partition_disjoint": disjoint,
        "partition_complete": all_paths == tuple(sorted(payloads)),
    }
    result["pass"] = (
        result["decode_roundtrip_exact"]
        and result["partition_disjoint"]
        and result["partition_complete"]
        and result["counts_exact"]
        and result["explicit_reading_refire_list_unchanged"]
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
        "verification_mode":
            "SHA_PINNED_CYCLE828_CACHE_ATTESTATION_NOT_FRESH_CYCLE859_REPLAY",
        "pinned_cache_sha256": sha256(
            input_payloads[CACHE_PATHS[0]]
        ).hexdigest(),
        "both_readings_already_ran": (
            certificate_a["pass"]
            and certificate_a["candidate"] == "E1"
            and certificate_b["pass"]
            and certificate_b["candidate"] == "E2"
        ),
        "E1_every_H_attestation": {
            "transients": certificate_a["full_record_set_count"],
            "zero_record_cycles":
                certificate_a["remaining_zero_record_cycle_count"],
            "single_source_46_reproduced":
                certificate_a["single_source_46_reproduced"],
        },
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
        and result["E1_every_H_attestation"] == {
            "transients": 58,
            "zero_record_cycles": 9,
            "single_source_46_reproduced": True,
        }
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
    entries = snapshot_entries()
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
        "snapshot_git_blob_ids_recomputed_exact": all(
            git_blob_sha(payloads[path]) == object_id
            for path, object_id in entries
        ),
        "registry_path_disjoint_from_corpus":
            HYPOTHETICAL_REGISTRY_PATH not in payloads,
        "primitive_id_reference_hits": primitive_reference_hits,
        "non_manifest_primitive_id_reference_hits": tuple(
            path for path in primitive_reference_hits
            if path != MANIFEST_PATH
        ),
        "adoption_content_delta_file_count": sum(
            before_hashes[path] != after_hashes[path]
            for path in before_hashes
        ),
        "adoption_content_delta_bytes": 0,
        "cycle828_spot_verification": spot,
        "verdict":
            "MODELED_HYPOTHETICAL_E2_PRIMITIVE_ADOPTION_CHANGES_ZERO_"
            "PINNED_SCRIPTS_DOCS_BYTES",
    }
    result["pass"] = (
        result["hashed_file_count"] == len(payloads)
        and result["all_file_sha256_recomputed"]
        and result["snapshot_git_blob_ids_recomputed_exact"]
        and result["registry_path_disjoint_from_corpus"]
        and not result["non_manifest_primitive_id_reference_hits"]
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
        "v1_consumers": sweep["v1_consumers"],
        "checker_lexical_rows": sweep["checker_lexical_rows"],
        "checker_lexical_features": sweep["checker_lexical_features"],
        "checker_broad_candidates": sweep["checker_broad_candidates"],
        "checker_semantic_evidence": sweep["checker_semantic_evidence"],
        "parse_failures": sweep["parse_failures"],
        "v1_classifications": sweep["v1_classifications"],
        "classifications": sweep["classifications"],
        "union_evidence": sweep["union_evidence"],
        "movements": sweep["movements"],
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
    scoped_tree_delta_from_R28 = tuple(
        line for line in git_text(
            "diff", "--name-status", BASE_R28_SHA, SNAPSHOT_COMMIT_SHA,
            "--", "scripts", "docs",
        ).splitlines()
        if line
    )
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
        "snapshot_commit_sha": SNAPSHOT_COMMIT_SHA,
        "literal_snapshot_commit_sha":
            literal_assignment(self_tree, "SNAPSHOT_COMMIT_SHA")
            == SNAPSHOT_COMMIT_SHA,
        "base_R28_ref_matches_pin": git_text(
            "rev-parse", "physics-loop/proof-grade-blockR28-20260729"
        ) == BASE_R28_SHA,
        "running_branch": git_text("rev-parse", "--abbrev-ref", "HEAD"),
        "execution_head_sha": current_head,
        "snapshot_is_execution_head": SNAPSHOT_COMMIT_SHA == current_head,
        "snapshot_is_execution_head_required": False,
        "base_R28_is_snapshot_ancestor": git_bytes(
            "merge-base", "--is-ancestor", BASE_R28_SHA,
            SNAPSHOT_COMMIT_SHA,
        ) == b"",
        "snapshot_is_execution_head_ancestor": git_bytes(
            "merge-base", "--is-ancestor", SNAPSHOT_COMMIT_SHA, current_head
        ) == b"",
        "scoped_tree_delta_from_R28": scoped_tree_delta_from_R28,
        "only_manifest_added_since_R28":
            scoped_tree_delta_from_R28 == (f"A\t{MANIFEST_PATH}",),
        "recent_main_landings_scope": "OUT_OF_SCOPE_IF_OUTSIDE_PINNED_LINEAGE",
        "owner_lane_live_main_action": "RERUN_ON_LIVE_MAIN_HEAD",
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
        and result["literal_snapshot_commit_sha"]
        and result["base_R28_ref_matches_pin"]
        and result["running_branch"] == EXPECTED_BRANCH
        and result["base_R28_is_snapshot_ancestor"]
        and result["snapshot_is_execution_head_ancestor"]
        and result["only_manifest_added_since_R28"]
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
    (
        v1_consumers,
        checker_lexical_rows,
        checker_lexical_features,
        checker_broad_candidates,
        checker_semantic_evidence,
        parse_failures,
    ) = sweep_payloads(payloads)
    v1_classifications = classify_v1(payloads, v1_consumers)
    classifications, union_evidence, movements = classify_union(
        payloads,
        v1_classifications,
        checker_lexical_rows,
        checker_lexical_features,
        checker_semantic_evidence,
    )
    return {
        "entries": entries,
        "payloads": payloads,
        "v1_consumers": v1_consumers,
        "checker_lexical_rows": checker_lexical_rows,
        "checker_lexical_features": checker_lexical_features,
        "checker_broad_candidates": checker_broad_candidates,
        "checker_semantic_evidence": checker_semantic_evidence,
        "parse_failures": parse_failures,
        "v1_classifications": v1_classifications,
        "classifications": classifications,
        "union_evidence": union_evidence,
        "movements": movements,
    }


def render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    controls: dict[str, object],
    movements: tuple[dict[str, object], ...],
) -> str:
    lines = [
        "CYCLE859_V3_ADOPTION_IMPACT_MANIFEST",
        "ADOPTION_MODEL :: registered additive primitive; no axiom-text change",
        "SCOPE :: pinned tracked Git tree " + SNAPSHOT_COMMIT_SHA,
        "OUT_OF_SCOPE :: recent main landings outside this lineage; the "
        "owner-lane adoption PR must repin and re-run on live main",
        "CONSUMER_DETECTION_UNION :: " + " + ".join(
            CONSUMER_DETECTOR_UNION
        ),
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
    for movement in movements:
        lines.append(
            "UNION_RECLASSIFICATION_EVIDENCE :: "
            + str(movement["path"])
            + " :: "
            + str(movement["v1_class"])
            + " -> "
            + str(movement["union_class"])
            + " :: evidence="
            + compact(movement["evidence"])
        )
    lines.append(
        "REFIRE_GUARANTEE :: " + str(classification["refire_statement"])
    )
    lines.append("FINAL :: " + compact({
        "classification_counts": classification["counts"],
        "classification_counts_derived_not_hardcoded": True,
        "v1_to_union_movement_count":
            classification["v1_to_union_movement_count"],
        "explicit_reading_refire_count":
            classification["explicit_reading_refire_count"],
        "explicit_reading_refire_list_unchanged":
            classification["explicit_reading_refire_list_unchanged"],
        "refire_guarantee_stands":
            classification["refire_guarantee_stands"],
        "invariance_verdict": invariance["verdict"],
        "snapshot_commit_sha": SNAPSHOT_COMMIT_SHA,
        "cache_contamination_note": CACHE_CONTAMINATION_NOTE,
        "runtime_seconds": controls["runtime_seconds"],
        "owner_lane_live_main_action": "RERUN_ON_LIVE_MAIN_HEAD",
        "pass": all(value["pass"] for _label, value in certificates)
            and controls["pass"],
    }))
    lines.append(
        "CYCLE859_V3_ADOPTION_IMPACT_MANIFEST_PASS"
        if all(value["pass"] for _label, value in certificates)
        and controls["pass"]
        else "CYCLE859_V3_ADOPTION_IMPACT_MANIFEST_FAIL"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    sweep = build_sweep()
    input_payloads_before = read_audit_inputs()
    certificate_a = certificate_a_consumer_sweep(
        sweep["payloads"],
        sweep["v1_consumers"],
        sweep["checker_lexical_rows"],
        sweep["checker_broad_candidates"],
        sweep["checker_semantic_evidence"],
        sweep["union_evidence"],
        sweep["movements"],
        sweep["parse_failures"],
    )
    certificate_b = certificate_b_classification(
        sweep["payloads"],
        sweep["classifications"],
        sweep["v1_classifications"],
        sweep["movements"],
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
    output = render(certificates, controls, sweep["movements"])
    for _attempt in range(3):
        output_bytes = len(output.encode("utf-8"))
        controls["stdout_bytes"] = output_bytes
        controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["pass"] and controls["stdout_within_limit"]
        updated = render(certificates, controls, sweep["movements"])
        if len(updated.encode("utf-8")) == output_bytes:
            output = updated
            break
        output = updated
    output_bytes = len(output.encode("utf-8"))
    controls["stdout_bytes"] = output_bytes
    controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
    output = render(certificates, controls, sweep["movements"])
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
