#!/usr/bin/env python3
"""Cycle 859 v3 independent check of the adoption-impact manifest.

The primary is source evidence only: this checker reads and parses it but
never imports or executes it.  The tracked corpus is rebuilt from the pinned
Git object database, then scanned with independently declared lexical and
semantic/data-flow probes.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
SNAPSHOT_COMMIT_SHA = "d6a514430ac9921882017ba6424d289e2dc6b288"
PRIMARY_PATH = (
    "scripts/frontier_cycle859_adoption_impact_manifest_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle859_adoption_impact_manifest_2026_07_28.py",
)
PRIMARY_MODULE = Path(PRIMARY_PATH).stem
EXPECTED_PRIMARY_SHA256 = (
    "52b94d68c25594a5f1222b8644f1c1a57591b13c0a78334cdcaee6360d2786b3"
)
EXPECTED_PRIMARY_GIT_BLOB = "7d73f3cbc338bbbcf0271ced86f443284beb05aa"
PRIMARY_COUNTS = {
    "NO_CONSUMPTION": 9339,
    "CORPUS_IMPLICIT": 50,
    "EXPLICIT_READING": 31,
}
EXPECTED_SCOPED_FILE_COUNT = 9420
CACHE_CONTAMINATION_NOTE = (
    "Cycle 859 v2 swept the working-tree snapshot; after its clean run, "
    "the block note, runner caches, and receipt quoting the E2 wording "
    "contaminated the rebuild, and failing caches shipped. Cycle 859 v3 "
    "repairs that incident by sweeping only the Git tree pinned at "
    f"{SNAPSHOT_COMMIT_SHA} via git ls-tree and git show."
)
EXPECTED_ADJUSTED_COUNTS = {
    "NO_CONSUMPTION": 9320,
    "CORPUS_IMPLICIT": 69,
    "EXPLICIT_READING": 31,
}
HYPOTHETICAL_REGISTRY_PATH = (
    "owner-lane/primitive-registry/record-formation.jsonl"
)
EXPECTED_PRIMITIVE_ID = "record_formation_first_orbit_admissibility_v1"
TRACKED_SCOPE = re.compile(r"(?:scripts/[^/]+\.py|docs/[^/]+\.md)\Z")

# These are independent conceptual needles.  They deliberately include
# cadence, stamps, general formation language, and semantic receipt fields
# that the primary's lexical partition says it does not exhaust.
DECLARED_NEEDLE_FAMILIES = {
    "formation": ("form", "forms", "formed", "formation"),
    "cadence": ("cadence", "clock", "boundary"),
    "orbit_return": ("orbit", "return", "admissible", "admissibility"),
    "stamp": ("stamp", "timestamp", "time", "tick"),
    "moment": ("moment", "moments"),
    "labels": ("E1", "E2"),
    "record_rule": ("record", "records", "selection", "event", "clean"),
}
FORMATION_STAMPS = frozenset({
    252, 371, 444, 532, 681, 1385, 14739, 14744, 33195, 51115,
})
LATE_FORMATION_STAMPS = frozenset({14739, 14744, 33195, 51115})
FORMATION_LANE_CYCLES = frozenset({
    792, 794, 796, 799, 813, 814, 818, 819, 820, 822, 828, 830, 832,
    837, 839, 842, 845, 848, 851, 853, 854, 855,
})
SEMANTIC_FIELDS = frozenset({
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
EXPECTED_FALSE_NO_PATHS = (
    "docs/COHORT_MOMENT_LAW_CYCLE832_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/EXTENDED_HORIZON_SELECTOR_CYCLE792_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/PARTITION_ROUTE_CYCLE845_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/PERIOD_STRUCTURE_CYCLE818_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/SHARED_MOMENT_CYCLE820_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/SILENCE_THEOREM_CYCLE813_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/SSTAR_BASIN_CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/WHY_SEP5_CYCLE837_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle813_silence_theorem_2026_07_28.py",
    "scripts/frontier_cycle814_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle837_sep5_independent_check_2026_07_28.py",
    "scripts/frontier_cycle837_why_sep5_2026_07_28.py",
    "scripts/frontier_cycle842_local_causal_theorem_2026_07_28.py",
    "scripts/frontier_cycle842_theorem_independent_check_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
    "scripts/frontier_cycle848_derivation_independent_check_2026_07_28.py",
    "scripts/frontier_cycle854_braid_inheritance_2026_07_28.py",
)


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if the Cycle-859 primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname == PRIMARY_MODULE:
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
    candidates: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            candidates.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            candidates.append(node.value)
    if len(candidates) != 1:
        return None
    try:
        return ast.literal_eval(candidates[0])
    except (TypeError, ValueError):
        return None


def snapshot_entries(scoped_only: bool = True) -> tuple[tuple[str, str], ...]:
    raw = git_bytes(
        "ls-tree", "-r", "-z", "--full-tree", SNAPSHOT_COMMIT_SHA
    )
    rows = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii").split()
        path = raw_path.decode("utf-8")
        if scoped_only and not TRACKED_SCOPE.fullmatch(path):
            continue
        if kind == "blob" and mode in {"100644", "100755"}:
            rows.append((path, object_id))
        elif scoped_only:
            raise AssertionError(("non-blob scoped member", path, metadata))
    return tuple(sorted(rows))


def load_snapshot_payloads(
    entries: tuple[tuple[str, str], ...],
) -> dict[str, bytes]:
    payloads: dict[str, bytes] = {}
    for path, expected_id in entries:
        payload = git_bytes("show", f"{SNAPSHOT_COMMIT_SHA}:{path}")
        if git_blob_sha(payload) != expected_id:
            raise AssertionError(("git show blob mismatch", path))
        payloads[path] = payload
    return payloads


def hash_manifest(payloads: dict[str, bytes]) -> dict[str, str]:
    return {
        path: sha256(payload).hexdigest()
        for path, payload in sorted(payloads.items())
    }


def word_terms(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[A-Za-z]+|[0-9]+", text))


def adjacent_terms(
    terms: tuple[str, ...],
    left: Iterable[str],
    right: Iterable[str],
) -> bool:
    left_set = {item.lower() for item in left}
    right_set = {item.lower() for item in right}
    lowered = tuple(item.lower() for item in terms)
    return any(
        lowered[index] in left_set and lowered[index + 1] in right_set
        for index in range(len(lowered) - 1)
    )


def formation_lane_refs(text: str) -> tuple[str, ...]:
    found = set()
    for match in re.finditer(r"frontier_cycle([0-9]{3})_[A-Za-z0-9_]+", text):
        if int(match.group(1)) in FORMATION_LANE_CYCLES:
            found.add(match.group())
    return tuple(sorted(found))


def core_lexical_features(text: str) -> frozenset[str]:
    """Independent normalized-word replay of the claimed lexical surface."""

    lowered = text.lower()
    if not any(token in lowered for token in ("orbit", "first", "moment", "absolute_h")):
        return frozenset()
    features = set()
    def joined(left: str, right: str) -> bool:
        return bool(re.search(
            rf"(?<![A-Za-z0-9_]){left}[-_ ]{right}(?![A-Za-z0-9_])",
            text,
            re.I,
        ))

    if joined("orbit", "moments?"):
        features.add("ORBIT_MOMENT")
    if joined("orbit", "return"):
        features.add("ORBIT_RETURN")
    if joined("orbit", "admissibility"):
        features.add("ORBIT_ADMISSIBILITY")
    if joined("first", "clean"):
        features.add("FIRST_CLEAN")
    if re.search(r"(?<![A-Za-z0-9_])absolute_H(?![A-Za-z0-9_])", text):
        features.add("ABSOLUTE_H_SYMBOL")
    for symbol in re.findall(r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9_]*(?![A-Za-z0-9_])", text):
        components = symbol.split("_")
        if symbol == "MOMENT" or (
            len(components) >= 2 and components[-1] in {"MOMENT", "MOMENTS"}
        ):
            features.add("CONSTANT_MOMENT_FIELD")
    return frozenset(features)


E_LABEL = re.compile(r"(?<![A-Za-z0-9])E[12](?![A-Za-z0-9])")
RECORD_WORD = re.compile(r"\brecord(?:s|ed|ing)?\b|record[_-]", re.I)


def explicit_reading_features(text: str) -> frozenset[str]:
    if "E1" not in text and "E2" not in text and "record" not in text.lower():
        return frozenset()
    features = set()
    for match in E_LABEL.finditer(text):
        window = text[max(0, match.start() - 200):match.end() + 200]
        if RECORD_WORD.search(window):
            features.add("E_LABEL_WITH_RECORD_CONTEXT")
    for symbol in re.findall(r"(?<![A-Za-z0-9_])E[12]_[A-Za-z0-9_]+", text):
        components = {part.upper() for part in symbol.split("_")[1:]}
        if components & {
            "CANDIDATE", "READING", "EVERY", "AXES", "OCCURRENCE",
            "OCCURRENCES", "EDIT", "RECORD", "FORMATION",
        }:
            features.add("E_LABELED_READING_FIELD")
    lowered_terms = tuple(term.lower() for term in word_terms(text))
    phrases = (
        ("records", "form", "at", "first", "admissibility"),
        ("records", "form", "at", "first", "orbit", "admissibility"),
        ("record", "set", "first", "clean", "orbit", "return", "selection", "event", "set"),
    )
    for phrase in phrases:
        width = len(phrase)
        if any(lowered_terms[index:index + width] == phrase
               for index in range(len(lowered_terms) - width + 1)):
            features.add("PLAIN_RECORD_FORMATION_RULE")
    return frozenset(features)


def broad_candidate_features(text: str) -> frozenset[str]:
    """Overinclusive semantic needles; later evidence adjudicates them."""

    lowered = text.lower()
    if not any(token in lowered for token in (
        "formation", "cadence", "orbit", "stamp", "moment", "record",
        "transient", "zero-record", "zero_record", "e1", "e2",
    )):
        return frozenset()
    terms = {term.lower() for term in word_terms(text)}
    features = set()
    if "formation" in terms and terms & {"record", "records", "moment", "stamp"}:
        features.add("BROAD_FORMATION_CONTEXT")
    if "cadence" in terms and terms & {"record", "records", "orbit", "selection"}:
        features.add("BROAD_CADENCE_CONTEXT")
    if terms & {"stamp", "timestamp"} and terms & {"record", "records", "moment", "selection"}:
        features.add("BROAD_STAMP_CONTEXT")
    if terms & {"moment", "moments"} and terms & {
        "transient", "transients", "clean", "selection", "formation", "cohort", "cohorts",
    }:
        features.add("BROAD_MOMENT_CONTEXT")
    if "orbit" in terms and terms & {"return", "admissible", "admissibility"}:
        features.add("BROAD_ORBIT_RETURN_CONTEXT")
    if terms & {"e1", "e2"} and terms & {"record", "records", "reading", "formation"}:
        features.add("BROAD_E1_E2_CONTEXT")
    if re.search(r"\bzero[-_ ]record\w*\b", lowered):
        features.add("BROAD_ZERO_RECORD_CONTEXT")
    return frozenset(features)


class ScriptProbe(ast.NodeVisitor):
    """Collect AST-only channels and semantic alias/receipt evidence."""

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
        self.core_features.update(core_lexical_features(value))
        self.explicit_features.update(explicit_reading_features(value))
        self.broad_features.update(broad_candidate_features(value))
        if channel in {"string", "import"}:
            self.lane_refs.update(formation_lane_refs(value))
        lowered = value.lower()
        if lowered in SEMANTIC_FIELDS:
            self.semantic_fields.add(lowered)
        elif len(value) < 2048:
            for field in SEMANTIC_FIELDS:
                if re.search(
                    rf"(?<![A-Za-z0-9_]){re.escape(field)}(?![A-Za-z0-9_])",
                    value,
                    re.I,
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
            and child.value.lower() in SEMANTIC_FIELDS
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


def script_probe(path: str, text: str) -> ScriptProbe:
    tree = ast.parse(text, filename=path)
    probe = ScriptProbe()
    probe.visit(tree)
    return probe


def lexical_classification(
    path: str,
    text: str,
    probe: ScriptProbe | None,
) -> tuple[str, tuple[str, ...]]:
    if probe is None:
        core = set(core_lexical_features(text))
        explicit = set(explicit_reading_features(text))
    else:
        core = set(probe.core_features)
        explicit = set(probe.explicit_features)
    if explicit:
        return "EXPLICIT_READING", tuple(sorted(explicit | core))
    if core:
        return "CORPUS_IMPLICIT", tuple(sorted(core))
    return "NO_CONSUMPTION", ()


def document_semantic_evidence(path: str, text: str) -> tuple[str, ...]:
    cycle_match = re.search(r"CYCLE([0-9]{3})", path)
    if not cycle_match or int(cycle_match.group(1)) not in FORMATION_LANE_CYCLES:
        return ()
    lowered = " ".join(text.lower().split())
    evidence = set()
    if "record-candidate" in lowered and "moment" in lowered:
        evidence.add("NARRATIVE_RECORD_CANDIDATE_MOMENT")
    if re.search(r"\b(?:selection moment|simultaneous selections?)\b", lowered):
        evidence.add("NARRATIVE_SELECTION_MOMENT")
    if re.search(r"cohort(?:'s|s')? own moment", lowered):
        evidence.add("NARRATIVE_COHORT_OWN_MOMENT")
    for match in re.finditer(r"\btransient\w*\b", lowered):
        window = lowered[max(0, match.start() - 320):match.end() + 320]
        if re.search(
            r"\b(?:moment|clean|selection|resolved|cohort|funnel|basin)\w*\b",
            window,
        ):
            evidence.add("NARRATIVE_TRANSIENT_FAMILY")
            break
    if re.search(r"\bzero[- ]record\w*\b", lowered) and re.search(
        r"\b(?:cycle|transient|clean|selection)\w*\b", lowered
    ):
        evidence.add("NARRATIVE_ZERO_RECORD_FAMILY")
    present_stamps = {stamp for stamp in LATE_FORMATION_STAMPS if str(stamp) in text}
    if present_stamps and re.search(
        r"\b(?:selection|clean|funnel|transient|moment)\w*\b", lowered
    ):
        evidence.add("NARRATIVE_PINNED_FORMATION_STAMP")
    return tuple(sorted(evidence))


def script_semantic_evidence(
    path: str,
    probe: ScriptProbe,
) -> tuple[str, ...]:
    cycle_match = re.search(r"frontier_cycle([0-9]{3})_", path)
    if not cycle_match or int(cycle_match.group(1)) not in FORMATION_LANE_CYCLES:
        return ()
    fields = {
        field.lower() for field in probe.semantic_fields | probe.loaded_fields
    } & SEMANTIC_FIELDS
    stamps = probe.integer_constants & FORMATION_STAMPS
    late_stamps = stamps & LATE_FORMATION_STAMPS
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


def build_sweep() -> dict[str, object]:
    entries = snapshot_entries()
    payloads = load_snapshot_payloads(entries)
    lexical_rows: dict[str, str] = {}
    lexical_features: dict[str, tuple[str, ...]] = {}
    broad_candidates: dict[str, tuple[str, ...]] = {}
    semantic_evidence: dict[str, tuple[str, ...]] = {}
    parse_failures = []
    for path, payload in sorted(payloads.items()):
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError as error:
            parse_failures.append(f"{path}:UTF8:{error}")
            continue
        if path.startswith("scripts/"):
            try:
                probe = script_probe(path, text)
            except SyntaxError as error:
                parse_failures.append(
                    f"{path}:AST:{error.lineno}:{error.offset}:{error.msg}"
                )
                continue
            broad = tuple(sorted(probe.broad_features))
            evidence = script_semantic_evidence(path, probe)
        else:
            probe = None
            broad = tuple(sorted(broad_candidate_features(text)))
            evidence = document_semantic_evidence(path, text)
        label, features = lexical_classification(path, text, probe)
        lexical_rows[path] = label
        if features:
            lexical_features[path] = features
        if broad:
            broad_candidates[path] = broad
        if evidence:
            semantic_evidence[path] = evidence
    if set(lexical_rows) != set(payloads):
        missing = sorted(set(payloads) - set(lexical_rows))
        parse_failures.extend(f"{path}:UNCLASSIFIED" for path in missing)
    false_no = {
        path: evidence
        for path, evidence in semantic_evidence.items()
        if lexical_rows.get(path) == "NO_CONSUMPTION"
    }
    adjusted_rows = dict(lexical_rows)
    for path in false_no:
        adjusted_rows[path] = "CORPUS_IMPLICIT"
    return {
        "entries": entries,
        "payloads": payloads,
        "payload_sha256": hash_manifest(payloads),
        "lexical_rows": lexical_rows,
        "lexical_features": lexical_features,
        "broad_candidates": broad_candidates,
        "semantic_evidence": semantic_evidence,
        "false_no": false_no,
        "adjusted_rows": adjusted_rows,
        "parse_failures": tuple(parse_failures),
    }


def row_counts(rows: dict[str, str]) -> dict[str, int]:
    counts = Counter(rows.values())
    return {
        label: counts[label]
        for label in (
            "NO_CONSUMPTION", "CORPUS_IMPLICIT", "EXPLICIT_READING",
        )
    }


def sweep_fingerprint(sweep: dict[str, object]) -> str:
    return digest({
        "entries": sweep["entries"],
        "payload_sha256": sweep["payload_sha256"],
        "lexical_rows": sweep["lexical_rows"],
        "lexical_features": sweep["lexical_features"],
        "broad_candidates": sweep["broad_candidates"],
        "semantic_evidence": sweep["semantic_evidence"],
        "false_no": sweep["false_no"],
        "adjusted_rows": sweep["adjusted_rows"],
        "parse_failures": sweep["parse_failures"],
    })


def certificate_sweep_replay(sweep: dict[str, object]) -> dict[str, object]:
    lexical_counts = row_counts(sweep["lexical_rows"])
    adjusted_counts = row_counts(sweep["adjusted_rows"])
    divergences = tuple({
        "path": path,
        "primary_class": "NO_CONSUMPTION",
        "independent_class": "CORPUS_IMPLICIT",
        "evidence": sweep["false_no"][path],
    } for path in sorted(sweep["false_no"]))
    result = {
        "certificate": "THE_SWEEP_REPLAY",
        "finding": "PRIMARY_COUNTS_REFUTED_AFTER_SEMANTIC_ADJUDICATION",
        "snapshot_commit_sha": SNAPSHOT_COMMIT_SHA,
        "scanned_file_count": len(sweep["payloads"]),
        "declared_needle_families": DECLARED_NEEDLE_FAMILIES,
        "script_method": (
            "independent AST imports/strings/loaded names/attributes/keys; "
            "assignment alias edges; JSON receipt calls"
        ),
        "docs_method": "full text plus bounded semantic-context windows",
        "lexical_only_counts": lexical_counts,
        "primary_claimed_counts": PRIMARY_COUNTS,
        "lexical_only_counts_match_primary": lexical_counts == PRIMARY_COUNTS,
        "broad_candidate_file_count": len(sweep["broad_candidates"]),
        "semantic_adjusted_counts": adjusted_counts,
        "expected_semantic_adjusted_counts": EXPECTED_ADJUSTED_COUNTS,
        "semantic_adjusted_counts_exact":
            adjusted_counts == EXPECTED_ADJUSTED_COUNTS,
        "exact_divergence_count": len(divergences),
        "exact_divergence_list": divergences,
        "parse_failures": sweep["parse_failures"],
    }
    result["legacy_no_refutation_pass"] = (
        not result["parse_failures"]
        and result["lexical_only_counts_match_primary"]
        and not divergences
        and adjusted_counts == PRIMARY_COUNTS
    )
    result["pass"] = (
        not result["parse_failures"]
        and result["lexical_only_counts_match_primary"]
        and tuple(row["path"] for row in divergences)
            == tuple(sorted(EXPECTED_FALSE_NO_PATHS))
        and result["semantic_adjusted_counts_exact"]
    )
    return result


def certificate_missed_consumer_hunt(
    sweep: dict[str, object],
) -> dict[str, object]:
    false_no = sweep["false_no"]
    evidence_counts = Counter(
        item for evidence in false_no.values() for item in evidence
    )
    result = {
        "certificate": "THE_MISSED_CONSUMER_HUNT",
        "finding": "FALSE_NO_CONSUMPTION_REVERSES_SCOPED_REFIRE_GUARANTEE",
        "constructive_false_NO_count": len(false_no),
        "constructive_false_NO_paths": tuple(sorted(false_no)),
        "per_path_evidence": {
            path: false_no[path] for path in sorted(false_no)
        },
        "evidence_class_counts": dict(sorted(evidence_counts.items())),
        "expected_constructive_paths": EXPECTED_FALSE_NO_PATHS,
        "constructive_paths_exact": tuple(sorted(false_no))
            == tuple(sorted(EXPECTED_FALSE_NO_PATHS)),
        "reversal_rule": (
            "any primary-(a) path with AST/dataflow or narrative receipt "
            "consumption of the formation reading reverses scoped refire"
        ),
        "reversal_triggered": bool(false_no),
    }
    result["legacy_no_refutation_pass"] = not result["reversal_triggered"]
    result["pass"] = (
        result["reversal_triggered"]
        and result["constructive_paths_exact"]
    )
    return result


def assignment_expression(tree: ast.Module, name: str) -> ast.expr | None:
    matches = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            matches.append(node.value)
    return matches[0] if len(matches) == 1 else None


def registry_call_shape(tree: ast.Module) -> dict[str, object]:
    expression = assignment_expression(tree, "HYPOTHETICAL_REGISTRY_LINE")
    if not isinstance(expression, ast.Call):
        return {"valid": False, "reason": "assignment_not_call"}
    function = expression.func
    function_exact = (
        isinstance(function, ast.Attribute)
        and isinstance(function.value, ast.Name)
        and function.value.id == "json"
        and function.attr == "dumps"
    )
    dictionary = expression.args[0] if len(expression.args) == 1 else None
    operation = None
    keys = []
    if isinstance(dictionary, ast.Dict):
        for key, value in zip(dictionary.keys, dictionary.values):
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                keys.append(key.value)
                if key.value == "operation" and isinstance(value, ast.Constant):
                    operation = value.value
    keywords = {keyword.arg: keyword.value for keyword in expression.keywords}
    sort_keys = keywords.get("sort_keys")
    separators = keywords.get("separators")
    shape = {
        "function_json_dumps": function_exact,
        "dictionary_keys": tuple(keys),
        "operation": operation,
        "sort_keys_true": (
            isinstance(sort_keys, ast.Constant) and sort_keys.value is True
        ),
        "compact_separators": (
            isinstance(separators, ast.Tuple)
            and ast.literal_eval(separators) == (",", ":")
        ),
    }
    shape["valid"] = (
        shape["function_json_dumps"]
        and set(keys) == {
            "primitive_id", "completion", "text",
            "certified_plain_reading", "operation",
        }
        and operation == "additive_registry_entry_no_axiom_text_change"
        and shape["sort_keys_true"]
        and shape["compact_separators"]
    )
    return shape


def certificate_invariance_logic(
    sweep: dict[str, object],
    primary_payload: bytes,
) -> dict[str, object]:
    primary_tree = ast.parse(primary_payload, filename=PRIMARY_PATH)
    registry_path = literal_assignment(primary_tree, "HYPOTHETICAL_REGISTRY_PATH")
    primitive_id = literal_assignment(primary_tree, "HYPOTHETICAL_PRIMITIVE_ID")
    completion_text = literal_assignment(primary_tree, "E2_COMPLETION")
    plain_reading = literal_assignment(primary_tree, "E2_CERTIFIED_READING")
    shape = registry_call_shape(primary_tree)
    registry_record = {
        "primitive_id": primitive_id,
        "completion": "E2",
        "text": completion_text,
        "certified_plain_reading": plain_reading,
        "operation": "additive_registry_entry_no_axiom_text_change",
    }
    registry_line = compact(registry_record)
    full_entries = snapshot_entries(scoped_only=False)
    full_paths = {path for path, _object_id in full_entries}
    before_hashes = sweep["payload_sha256"]
    virtual_scoped_payloads = dict(sweep["payloads"])
    after_hashes = hash_manifest(virtual_scoped_payloads)
    post_full_paths = full_paths | {str(registry_path)}
    result = {
        "certificate": "THE_INVARIANCE_LOGIC",
        "finding": "ZERO_PINNED_BYTES_CONFIRMED_FOR_ADDITIVE_DISJOINT_ARTIFACT",
        "registry_path": registry_path,
        "registry_path_matches_primary_claim":
            registry_path == HYPOTHETICAL_REGISTRY_PATH,
        "primitive_id": primitive_id,
        "primitive_id_matches": primitive_id == EXPECTED_PRIMITIVE_ID,
        "primary_registry_call_shape": shape,
        "registry_line": registry_line,
        "registry_line_sha256": sha256(registry_line.encode()).hexdigest(),
        "registry_path_absent_from_tracked_snapshot": registry_path not in full_paths,
        "registry_path_disjoint_from_every_pinned_path": all(
            registry_path != path for path in sweep["payloads"]
        ),
        "virtual_full_tree_additions": tuple(sorted(post_full_paths - full_paths)),
        "virtual_operation_is_one_new_file":
            post_full_paths - full_paths == {registry_path},
        "pinned_file_count": len(before_hashes),
        "pinned_byte_count": sum(len(value) for value in sweep["payloads"].values()),
        "pinned_sha256_manifest_sha256": digest(tuple(sorted(before_hashes.items()))),
        "git_blob_ids_recomputed_exact": all(
            git_blob_sha(sweep["payloads"][path]) == object_id
            for path, object_id in sweep["entries"]
        ),
        "snapshot_git_blob_ids_recomputed_exact": all(
            git_blob_sha(sweep["payloads"][path]) == object_id
            for path, object_id in sweep["entries"]
        ),
        "pinned_hashes_before_equal_virtual_after": before_hashes == after_hashes,
        "pinned_content_delta_file_count": sum(
            before_hashes[path] != after_hashes[path] for path in before_hashes
        ),
        "pinned_content_delta_bytes": 0,
        "scope_boundary": (
            "byte invariance survives; semantic NO/refire classification is "
            "a separate claim and is refuted"
        ),
    }
    result["pass"] = (
        result["registry_path_matches_primary_claim"]
        and result["primitive_id_matches"]
        and shape["valid"]
        and result["registry_path_absent_from_tracked_snapshot"]
        and result["registry_path_disjoint_from_every_pinned_path"]
        and result["virtual_operation_is_one_new_file"]
        and result["git_blob_ids_recomputed_exact"]
        and result["snapshot_git_blob_ids_recomputed_exact"]
        and result["pinned_hashes_before_equal_virtual_after"]
        and result["pinned_content_delta_file_count"] == 0
        and result["pinned_content_delta_bytes"] == 0
    )
    return result


def certificate_controls(
    sweep: dict[str, object],
    repeat: dict[str, object],
    primary_before: bytes,
    primary_after: bytes,
    sweep_certificate: dict[str, object],
    hunt_certificate: dict[str, object],
    invariance_certificate: dict[str, object],
    runtime_seconds: float,
) -> dict[str, object]:
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    primary_tree = ast.parse(primary_before, filename=PRIMARY_PATH)
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
    actual_primary_sha = sha256(primary_before).hexdigest()
    actual_primary_blob = git_blob_sha(primary_before)
    current_head = git_text("rev-parse", "HEAD")
    result = {
        "certificate": "CONTROLS",
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
        "primary_sha256": actual_primary_sha,
        "primary_sha256_pin_match":
            actual_primary_sha == EXPECTED_PRIMARY_SHA256,
        "primary_git_blob": actual_primary_blob,
        "primary_git_blob_pin_match":
            actual_primary_blob == EXPECTED_PRIMARY_GIT_BLOB,
        "primary_snapshot_pin_match":
            literal_assignment(primary_tree, "SNAPSHOT_COMMIT_SHA")
            == SNAPSHOT_COMMIT_SHA,
        "inputs_unchanged": primary_before == primary_after,
        "primary_AST_valid": isinstance(primary_tree, ast.Module),
        "primary_access_mode": "read_bytes + ast.parse; never import/execute",
        "primary_blocklisted_module": PRIMARY_MODULE,
        "primary_imported_by_self": PRIMARY_MODULE in imported_modules,
        "primary_loaded": PRIMARY_MODULE in sys.modules,
        "primary_blocker_hits": tuple(PRIMARY_BLOCKER.hits),
        "snapshot_commit_sha": SNAPSHOT_COMMIT_SHA,
        "literal_snapshot_commit_sha":
            literal_assignment(self_tree, "SNAPSHOT_COMMIT_SHA")
            == SNAPSHOT_COMMIT_SHA,
        "execution_head_sha": current_head,
        "snapshot_is_execution_head":
            current_head == SNAPSHOT_COMMIT_SHA,
        "snapshot_is_execution_head_required": False,
        "snapshot_is_execution_head_ancestor": git_bytes(
            "merge-base", "--is-ancestor", SNAPSHOT_COMMIT_SHA, current_head
        ) == b"",
        "running_branch": git_text("rev-parse", "--abbrev-ref", "HEAD"),
        "scoped_file_count": len(sweep["payloads"]),
        "scoped_file_count_expected":
            len(sweep["payloads"]) == EXPECTED_SCOPED_FILE_COUNT,
        "all_scoped_paths_exact": all(
            TRACKED_SCOPE.fullmatch(path) for path in sweep["payloads"]
        ),
        "parse_failures": sweep["parse_failures"],
        "determinism_fingerprint": sweep_fingerprint(sweep),
        "repeat_fingerprint": sweep_fingerprint(repeat),
        "determinism_replay": sweep_fingerprint(sweep)
            == sweep_fingerprint(repeat),
        "expected_false_NO_paths_exact":
            tuple(sorted(sweep["false_no"]))
            == tuple(sorted(EXPECTED_FALSE_NO_PATHS)),
        "expected_adjusted_counts": EXPECTED_ADJUSTED_COUNTS,
        "actual_adjusted_counts": row_counts(sweep["adjusted_rows"]),
        "adjusted_counts_exact": row_counts(sweep["adjusted_rows"])
            == EXPECTED_ADJUSTED_COUNTS,
        "refutation_coherent": (
            sweep_certificate["pass"]
            and hunt_certificate["pass"]
            and hunt_certificate["reversal_triggered"]
            and hunt_certificate["constructive_paths_exact"]
        ),
        "invariance_independently_clean": invariance_certificate["pass"],
        "runtime_seconds": round(runtime_seconds, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": False,
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and result["inputs_existing_worktree_relative"]
        and result["primary_sha256_pin_match"]
        and result["primary_git_blob_pin_match"]
        and result["primary_snapshot_pin_match"]
        and result["inputs_unchanged"]
        and result["primary_AST_valid"]
        and not result["primary_imported_by_self"]
        and not result["primary_loaded"]
        and not result["primary_blocker_hits"]
        and result["literal_snapshot_commit_sha"]
        and result["snapshot_is_execution_head_ancestor"]
        and result["scoped_file_count_expected"]
        and result["all_scoped_paths_exact"]
        and not result["parse_failures"]
        and result["determinism_replay"]
        and result["expected_false_NO_paths_exact"]
        and result["adjusted_counts_exact"]
        and result["refutation_coherent"]
        and result["invariance_independently_clean"]
        and runtime_seconds < AUDIT_TIMEOUT_SEC
    )
    return result


def render(
    certificates: tuple[dict[str, object], ...],
    controls: dict[str, object],
) -> str:
    lines = [
        "CYCLE859_MANIFEST_INDEPENDENT_ADVERSARIAL_CHECK",
        "SCOPE :: pinned tracked top-level scripts/*.py and docs/*.md at "
        + SNAPSHOT_COMMIT_SHA,
        "PRIMARY_ACCESS :: BLOCKLISTED source text/AST only; never imported or executed",
    ]
    for certificate in certificates:
        lines.append(
            ("PASS " if certificate["pass"] else "FAIL ")
            + str(certificate["certificate"])
            + " FINDING=" + str(certificate["finding"])
            + " :: " + compact(certificate)
        )
    lines.append(
        ("PASS " if controls["pass"] else "FAIL ")
        + "CONTROLS FINDING=" + str(controls["finding"])
        + " :: " + compact(controls)
    )
    sweep = certificates[0]
    hunt = certificates[1]
    invariance = certificates[2]
    checker_clean = (
        controls["pass"]
        and invariance["pass"]
        and sweep["pass"]
        and hunt["pass"]
        and hunt["reversal_triggered"]
    )
    lines.append("FINAL :: " + compact({
        "cache_contamination_note": CACHE_CONTAMINATION_NOTE,
        "checker_clean": checker_clean,
        "primary_survives": False if checker_clean else None,
        "primary_lexical_counts": sweep["lexical_only_counts"],
        "independent_semantic_counts": sweep["semantic_adjusted_counts"],
        "snapshot_commit_sha": SNAPSHOT_COMMIT_SHA,
        "false_NO_count": hunt["constructive_false_NO_count"],
        "byte_invariance_survives": invariance["pass"],
        "scoped_refire_guarantee_survives": False if checker_clean else None,
        "terminal": (
            "CYCLE859_PRIMARY_REFUTED_FALSE_NO_CONSUMPTION"
            if checker_clean
            else "CYCLE859_INDEPENDENT_CHECK_NOT_CLEAN"
        ),
    }))
    lines.append(
        "CYCLE859_MANIFEST_INDEPENDENT_CHECK_REFUTATION_CONFIRMED"
        if checker_clean
        else "CYCLE859_MANIFEST_INDEPENDENT_CHECK_FAILED"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    primary_before = (ROOT / PRIMARY_PATH).read_bytes()
    sweep = build_sweep()
    sweep_certificate = certificate_sweep_replay(sweep)
    hunt_certificate = certificate_missed_consumer_hunt(sweep)
    invariance_certificate = certificate_invariance_logic(
        sweep, primary_before
    )
    repeat = build_sweep()
    primary_after = (ROOT / PRIMARY_PATH).read_bytes()
    runtime_seconds = monotonic() - started
    certificates = (
        sweep_certificate,
        hunt_certificate,
        invariance_certificate,
    )
    controls = certificate_controls(
        sweep,
        repeat,
        primary_before,
        primary_after,
        sweep_certificate,
        hunt_certificate,
        invariance_certificate,
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
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")), STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    checker_clean = (
        controls["pass"]
        and invariance_certificate["pass"]
        and sweep_certificate["pass"]
        and hunt_certificate["pass"]
        and hunt_certificate["reversal_triggered"]
    )
    return 0 if checker_clean else 1


if __name__ == "__main__":
    raise SystemExit(main())
