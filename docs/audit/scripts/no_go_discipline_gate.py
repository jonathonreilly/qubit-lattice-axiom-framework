#!/usr/bin/env python3
"""Shared No-Go Discipline packet construction and validation.

The gate binds every N1-N8 statement to evidence visible in the restricted
audit packet.  It does not try to prove semantic correctness mechanically; it
does prevent empty prose, synthetic route counting, unsupported prior-authority
claims, unresolved steelmen, and failed checklists from authorizing a clean
negative verdict.
"""
from __future__ import annotations

import hashlib
import json
import re
from itertools import combinations
from pathlib import Path
from typing import Any


RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}
PRIOR_AUTHORITY_PREMISE_TYPES = {
    "axiom_or_approved_primitive",
}
ROUTE_CLASSES = {
    "algebraic_rearrangement",
    "symmetry_or_representation",
    "alternate_carrier_or_sector",
    "boundary_or_initial_condition",
    "normalization_or_units",
    "dynamical_or_effective_action",
    "lattice_scale_or_limit",
    "numerical_or_finite_case",
    "convention_or_relabeling",
    "alternate_observable_or_readout",
    "topology_or_global_structure",
    "dependency_or_registry_reclassification",
}
DEMOTIONS = {
    "partial-attempt-with-named-untested-routes",
    "partial-narrowing",
    "bounded-with-corrected-wall-count",
    "stretch-attempt-with-honest-residual",
}
NON_CLEAN_VERDICTS = {
    "audited_conditional",
    "audited_renaming",
    "audited_failed",
    "audited_numerical_match",
}
HONESTY_MARKERS = {"ATTEMPTED", "RULED OUT BY PRIOR"}
ROUTE_DISPOSITIONS = {"CLOSED", "OPEN", "UNTESTED"}
CROSS_CYCLE_CANDIDATE_LIMIT = 64

PATH_TRIGGER_RE = re.compile(
    r"(?:^|[\s/._-])(?:no[\s_-]?go|obstruction|firewall|negative[\s_-]?boundary|"
    r"no[\s_-]?uniform[\s_-]?sign|stretch[\s_-]?attempt)(?:$|[\s/._-])",
    re.IGNORECASE,
)
NEGATIVE_ASSERTION_RE = re.compile(
    r"\bno[- ]go\b|\b(?:exact|scoped|structural|finite|standalone)?[ -]?negative boundary\b|"
    r"\b(?:dependency|selector|source)[ -]?firewall\b|"
    r"\bfirewall\b[^\n.;:]{0,80}\b(?:remains?|blocks?|prevents?|boundary)\b|"
    r"structurally (?:closed|undecidable)|no (?:admissible )?route exists|"
    r"no retained primitive(?: supplies)?|requires? (?:a )?new axiom|"
    r"\bno derivation of\b[^\n.;:]{0,160}\b(?:from|under)\b|"
    r"\b(?:absence|nonexistence|impossibility|failure|lack)\s+of\b"
    r"[^\n.;:]{0,160}\b(?:route|derivation|selector|closure|solution|carrier|operator)s?\b|"
    r"\bfailure\s+of\s+(?:every|all)\s+(?:route|attempt|construction)s?\b|"
    r"\b(?:non[- ]?derivability|underdetermination|inability|non[- ]?supply|non[- ]?closure)\b|"
    r"(?:cannot|can not|is not|are not) (?:be )?deriv(?:ed|able)(?: from)?|"
    r"(?:does not|cannot|fails? to|failed to) lift|"
    r"\b(?:cannot|does not|do not)\s+(?:select|orient|factor|factorize|derive|supply|"
    r"determine|fix|close|produce|recover)\b|"
    r"\bthere\s+(?:still\s+)?(?:remains?|persists?)\s+(?:an?\s+)?"
    r"(?:scoped\s+|residual\s+|unresolved\s+)?(?:wall|admission|obstruction)\b|"
    r"\bfails?\s+to\s+(?:close|resolve|remove|discharge|supply|derive|select)\b|"
    r"\b[^\n.;:]{1,80}\s+(?:is|are|was|were)\s+"
    r"(?:blocked|prevented|precluded)\b[^\n.;:]{0,80}\b"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b|"
    r"\b(?:walls?|admissions?|obstructions?)\b[^\n.;:]{0,80}"
    r"\b(?:blocks?|prevents?|precludes?|rules?\s+out|persists?|remains?)\b|"
    r"bounded with named walls|conditional on [^\n]{0,120}\b(?:walls?|admissions?|"
    r"imported selectors?|supplied selectors?|bridges?)\b|"
    r"\b(?:assumes?|assuming) [^\n]{0,120}\b(?:bridge|selector|sector selection|standard QFT)\b|"
    r"\b(?:residual|named|independent|unclosed|remaining|unresolved) (?:walls?|admissions?)\b|"
    r"\b(?:scoped|structural|bounded|remaining|unresolved) obstruction\b|"
    r"\bobstruction (?:to|rules out|blocks|precludes|prevents)\b|"
    r"no uniform sign|\b(?:route|attempt|construction)\b[^\n]{0,80}\bdoes not close\b|"
    r"(?:^|\n)\s*(?:walls?|admissions?)\s*:",
    re.IGNORECASE,
)
# Check explicit negated closure phrases before removing affirmative closure
# clauses. This handles adverbial forms ("does not fully close"), negative
# perfect/passive forms, and "fails to resolve" without treating affirmative
# tense variants as no-go assertions.
EXPLICIT_NEGATIVE_CLOSURE_RE = re.compile(
    r"\b(?:(?:(?:does|do|did|has|have|had|is|are|was|were)\s+not)|"
    r"cannot|can\s+not)\s+"
    r"(?:(?:yet|still|fully|completely|entirely|exactly|ever|successfully)\s+){0,4}"
    r"(?:close[sd]?|remove[sd]?|resolve[sd]?|discharge[sd]?|suppl(?:y|ies|ied)|"
    r"retire[sd]?|eliminate[sd]?)\b[^\n.;:]{0,100}\b"
    r"(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b|"
    r"\bfails?\s+"
    r"(?:(?:yet|still|fully|completely|entirely|exactly|ever|successfully)\s+){0,4}"
    r"to\s+(?:(?:fully|completely|entirely|exactly|successfully)\s+){0,3}"
    r"(?:close|remove|resolve|discharge|supply|retire|eliminate)\b"
    r"[^\n.;:]{0,100}\b(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b",
    re.IGNORECASE,
)
NEGATIVE_SUBJECT_CLOSURE_RE = re.compile(
    r"\b(?:(?:no|neither|zero)\s+"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|exists?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){1,10}|"
    r"none\s+of\s+(?:the\s+)?"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|exists?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){1,10}|"
    r"nothing\s+"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|exists?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){0,8})"
    r"(?:(?:can\s+|is\s+able\s+to\s+|are\s+able\s+to\s+)?"
    r"(?:close[sd]?|remove[sd]?|resolve[sd]?|discharge[sd]?|suppl(?:y|ies|ied)|"
    r"derive[sd]?|select[sd]?|determine[sd]?|fix(?:es|ed)?|retire[sd]?|"
    r"eliminate[sd]?)|succeeds?\s+in\s+"
    r"(?:closing|removing|resolving|discharging|supplying|deriving|selecting|"
    r"determining|fixing|retiring|eliminating))\b",
    re.IGNORECASE,
)
NO_EXISTENCE_ASSERTION_RE = re.compile(
    r"\bno\s+(?P<subject>"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){1,10})exist(?:s)?\b",
    re.IGNORECASE,
)
BOUNDARY_ABSENCE_SUBJECT_RE = re.compile(
    r"\b(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b",
    re.IGNORECASE,
)
INABILITY_CLOSURE_RE = re.compile(
    r"\b(?:is|are|was|were|remains?)\s+"
    r"(?:(?:still|wholly|completely|entirely)\s+){0,3}unable\s+to\s+"
    r"(?:close|remove|resolve|discharge|supply|derive|select|determine|fix|retire|"
    r"eliminate)\b[^\n.;:]{0,100}\b"
    r"(?:walls?|admissions?|obstructions?|selectors?|boundar(?:y|ies))\b",
    re.IGNORECASE,
)
BOUNDARY_SUBJECT_NEGATIVE_RE = re.compile(
    r"\b(?:the\s+|an?\s+|this\s+|that\s+)?"
    r"(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|selectors?|boundar(?:y|ies))\s+"
    r"(?:(?:cannot|can\s+not)\s+be\s+|"
    r"(?:is|are|was|were|has|have|had)\s+not\s+(?:been\s+)?)"
    r"(?:closed|removed|resolved|discharged|supplied|derived|selected|determined|"
    r"fixed|retired|eliminated)\b",
    re.IGNORECASE,
)
# Remove only clauses that affirmatively close or supply the named boundary.
# This keeps "does not close the remaining obstruction" live while excluding
# "closes the remaining obstruction" and passive equivalents.
POSITIVE_BOUNDARY_CLOSURE_RE = re.compile(
    r"(?<!not )(?<!never )\b(?:closes?|closed|removes?|removed|discharges?|discharged|"
    r"supplies?|supplied|resolves?|resolved|retires?|retired|eliminates?|eliminated|"
    r"answers?|answered|overcomes?|overcame)\b\s+(?:all\s+|the\s+|an?\s+|"
    r"explicitly\s+)?(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b|"
    r"\b(?:all\s+|the\s+|an?\s+)?(?:residual\s+|remaining\s+|scoped\s+|"
    r"unresolved\s+)?(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b"
    r"[^\n.;:]{0,50}\b(?:is|are|was|were|has\s+been|have\s+been|had\s+been)\s+"
    r"(?:explicitly\s+)?"
    r"(?:closed|removed|discharged|supplied|resolved|retired|eliminated)\b",
    re.IGNORECASE,
)
NEGATED_BOUNDARY_RE = re.compile(
    r"\b(?:no|not|never|without)\s+(?:an?\s+|live\s+)?"
    r"(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?)\b",
    re.IGNORECASE,
)
NEGATED_NEGATIVE_ASSURANCE_RE = re.compile(
    r"\b(?:(?:does|do|did)(?:\s+not|n't)\s+(?:require|introduce|add|create|produce)|"
    r"(?:cannot|can't)\s+(?:require|introduce|add|create|produce))\s+"
    r"(?:an?\s+|any\s+|the\s+)?(?:new\s+)?"
    r"(?:axioms?|walls?|admissions?|obstructions?)\b",
    re.IGNORECASE,
)
NEGATED_LABEL_ASSURANCE_RE = re.compile(
    r"\b(?:not|never|without)\s+(?:an?\s+|the\s+)?"
    r"(?:no[- ]go|negative boundary|firewall)\b|"
    r"\b(?:does|do|did)\s+not\s+(?:establish|prove|imply|claim|constitute)\s+"
    r"(?:an?\s+|the\s+)?(?:no[- ]go|negative boundary|firewall)\b",
    re.IGNORECASE,
)
LOCAL_SCOPE_EXCLUSION_RE = re.compile(
    r"\b(?:is|are|was|were|has|have)\s+not\s+(?:been\s+)?"
    r"(?:derived|established|proved|shown)\s+"
    r"(?:here|in this (?:note|theorem|section|work)|within this (?:note|scope|theorem))\b",
    re.IGNORECASE,
)
OUTPUT_BOUNDARY_FIELDS = (
    "claim_scope",
    "load_bearing_step",
    "chain_closure_explanation",
    "verdict_rationale",
)

AXIOM_REGISTRY = "docs/audit/data/axiom_premise_nodes.json"
OBLIGATION_REGISTRY = "docs/audit/data/derivation_obligations.json"
CONTROLLED_VOCABULARY = "docs/repo/controlled_vocabulary.yaml"
ACTIVE_REVIEW_QUEUE = "docs/repo/ACTIVE_REVIEW_QUEUE.md"
PREMISE_CLASSES_CHECKED = {
    "axiom_or_approved_primitive",
    "open_gate",
    "convention_not_accepted",
    "definition_or_scope_reframe",
}
# Validation-only compatibility for packets signed before the 2026-07-11
# authority reset. New packets are always built with PREMISE_CLASSES_CHECKED;
# accepting this exact historical shape does not restore any premise authority.
LEGACY_PREMISE_CLASSES_CHECKED = {
    "axiom_or_approved_primitive",
    "owner_governed_residual",
    "tier_a_derivation_target",
    "tier_a_convention_not_accepted",
    "definition_or_scope_reframe",
}
N3_SCAN_PHRASES = (
    "admission", "ansatz", "axiom", "boundary", "bridge context",
    "by construction", "convention", "initial condition", "normalization",
    "obstruction", "primitive", "as is standard", "naturally", "sector",
    "standard QFT", "wall", "we assume", "the framework provides",
    "background", "obviously", "registered", "canonical",
)
N5_SCAN_PHRASES = (
    "absent", "cannot", "does not", "fails", "impossible", "no nonzero",
    "no-go", "obstruction", "requires a new axiom", "rule out",
    "rules out", "structurally undecidable", "unavailable", "is not", "are not",
)
N5_RESOLUTION_CLASSES = {
    "per_element", "per_site", "per_mode", "per_block", "lattice_wide",
}
DOCS_NEGATIVE_RE = re.compile(
    r"structurally undecidable|no retained primitive|requires? (?:a )?new axiom|"
    r"cannot be derived|not derivable|no[- ]go|negative boundary|firewall|"
    r"no admissible route|no uniform sign",
    re.IGNORECASE,
)
_DOCS_NEGATIVE_CORPUS_CACHE: dict[str, tuple[list[Path], list[dict[str, Any]]]] = {}
_LOOP_LEDGER_CORPUS_CACHE: dict[str, tuple[list[Path], list[dict[str, Any]]]] = {}
N8_SOURCE_CORPUS_VERSION = "source-markdown-v2-excludes-generated"


def _is_generated_markdown(path: Path) -> bool:
    """Keep N8 candidate bytes independent of pipeline-generated views."""
    try:
        prefix = path.read_text(encoding="utf-8", errors="replace")[:512]
    except OSError:
        return True
    return "AUTO-GENERATED" in prefix or path.name in {
        "AUDIT_LEDGER.md",
        "AUDIT_QUEUE.md",
        "AUDIT_DISPATCH_QUEUE.md",
        "PUBLICATION_AUDIT_DIVERGENCE.md",
        "FRONT_DOOR_STATUS.md",
    } or path.name.endswith("_EFFECTIVE_STATUS.md")


def _docs_negative_corpus(root: Path) -> tuple[list[Path], list[dict[str, Any]]]:
    key = str(root.resolve())
    if key in _DOCS_NEGATIVE_CORPUS_CACHE:
        return _DOCS_NEGATIVE_CORPUS_CACHE[key]
    paths = [
        path for path in sorted((root / "docs").rglob("*.md"))
        if not _is_generated_markdown(path)
    ]
    records: list[dict[str, Any]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        excerpts = [
            line.strip()[:400]
            for line in text.splitlines()
            if line.strip() and DOCS_NEGATIVE_RE.search(line)
        ]
        if excerpts:
            records.append({
                "path": path,
                "content_sha256": _read_bytes_sha256(
                    root, path.relative_to(root).as_posix()
                ),
                "excerpts": excerpts,
                "search_terms": _search_terms(" ".join(excerpts)),
            })
    _DOCS_NEGATIVE_CORPUS_CACHE[key] = (paths, records)
    return paths, records


def _loop_ledger_corpus(root: Path, pattern: str) -> tuple[list[Path], list[dict[str, Any]]]:
    key = f"{root.resolve()}::{pattern}"
    if key in _LOOP_LEDGER_CORPUS_CACHE:
        return _LOOP_LEDGER_CORPUS_CACHE[key]
    paths = sorted(root.glob(pattern))
    records: list[dict[str, Any]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            text = f"[could not read loop no-go ledger: {exc}]"
        records.append({
            "path": path,
            "text": text,
            "content_sha256": _read_bytes_sha256(root, path.relative_to(root).as_posix()),
            "search_terms": _search_terms(text),
        })
    _LOOP_LEDGER_CORPUS_CACHE[key] = (paths, records)
    return paths, records


def _read_text(repo_root: Path, path: str | None) -> str:
    if not path:
        return ""
    try:
        return (repo_root / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _read_bytes_sha256(repo_root: Path, path: str | None) -> str:
    if not path:
        return hashlib.sha256(b"").hexdigest()
    try:
        payload = (repo_root / path).read_bytes()
    except OSError:
        payload = b""
    return hashlib.sha256(payload).hexdigest()


def _load_json(repo_root: Path, path: str) -> dict:
    try:
        return json.loads((repo_root / path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _canonical_runner_path(repo_root: Path, raw: str | None) -> str:
    if not raw:
        return ""
    p = Path(raw)
    candidates = []
    if p.is_absolute() or not str(raw).startswith("scripts/"):
        candidates.append(f"scripts/{p.name}")
    candidates.append(str(raw))
    for candidate in candidates:
        if (repo_root / candidate).exists():
            return candidate
    return str(raw)


def premise_type_for_id(repo_root: Path, claim_id: str) -> str | None:
    axioms = _load_json(repo_root, AXIOM_REGISTRY)
    if claim_id in set(axioms.get("canonical_ids") or []):
        return "axiom_or_approved_primitive"
    return None


def _add_evidence(
    manifest: dict[str, dict],
    *,
    path: str,
    role: str,
    text: str,
    effective_status: str | None = None,
    premise_type: str | None = None,
) -> None:
    if not path:
        return
    entry = manifest.setdefault(
        path,
        {
            "path": path,
            "roles": [],
            "text": text,
            "effective_status": effective_status,
            "accepted_premise_type": premise_type,
        },
    )
    if role not in entry["roles"]:
        entry["roles"].append(role)
    if text and not entry.get("text"):
        entry["text"] = text
    if effective_status:
        entry["effective_status"] = effective_status
    if premise_type:
        entry["accepted_premise_type"] = premise_type


def set_packet_evidence(
    manifest: dict[str, dict],
    *,
    path: str,
    role: str,
    text: str,
    effective_status: str | None = None,
    premise_type: str | None = None,
    invocation_bound_rendered_text: bool = False,
) -> None:
    """Insert or replace one exact rendered packet surface."""
    _add_evidence(
        manifest,
        path=path,
        role=role,
        text=text,
        effective_status=effective_status,
        premise_type=premise_type,
    )
    if path in manifest:
        manifest[path]["text"] = text
        if invocation_bound_rendered_text:
            manifest[path]["invocation_bound_rendered_text"] = True


def cross_cycle_index_path(claim_id: str) -> str:
    return f"audit-packet://cross-cycle-index/{claim_id}"


def partial_closure_index_path(claim_id: str) -> str:
    return f"audit-packet://partial-closure-index/{claim_id}"


def runner_stdout_evidence_path(claim_id: str) -> str:
    return f"audit-packet://runner-stdout/{claim_id}"


SEARCH_STOPWORDS = {
    "about", "after", "against", "before", "bounded", "claim", "clean",
    "conditional", "current", "derived", "framework", "note", "result",
    "route", "scope", "supplied", "theorem", "their", "there", "these",
    "this", "under", "using", "with", "without",
}


def _search_terms(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9_]{5,}", text.casefold())
        if token not in SEARCH_STOPWORDS
    }


def _row_search_terms(row: dict[str, Any]) -> set[str]:
    stable_basis = " ".join(
        str(row.get(field) or "") for field in ("claim_id", "note_path")
    )
    return _search_terms(re.sub(r"[_/.-]+", " ", stable_basis))


def build_cross_cycle_index(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> str:
    """Render the orchestrator-owned N8 search surface supplied to the auditor."""
    candidates: list[dict[str, Any]] = []
    cid = str(row.get("claim_id") or "")
    current_terms = _row_search_terms(row)

    def add_history(
        source_id: str, history: list[Any], *, require_overlap: bool = False
    ) -> None:
        for index, archived in enumerate(history):
            if not isinstance(archived, dict):
                continue
            overlap = sorted(
                current_terms.intersection(
                    _search_terms(json.dumps(archived, sort_keys=True))
                )
            )
            if require_overlap and len(overlap) < 2:
                continue
            invalidation_reason = str(archived.get("invalidation_reason") or "")
            explicitly_retired = bool(
                re.search(
                    r"(?:^|[_:\s-])(?:retired|superseded|source_removed|note_removed)(?:$|[_:\s-])",
                    invalidation_reason,
                    re.IGNORECASE,
                )
            )
            candidates.append(
                {
                    "candidate_id": f"{source_id}:previous_audit:{index}",
                    "kind": "prior_audit_cycle",
                    "source_claim_id": source_id,
                    "claim_type": archived.get("claim_type"),
                    "claim_scope": archived.get("claim_scope"),
                    "invalidation_reason": invalidation_reason,
                    "matching_terms": overlap,
                    "lifecycle_state": "retired" if explicitly_retired else "active",
                    "retired": explicitly_retired,
                    # Lifecycle and current applicability are independent.
                    # The auditor must decide applicability from the indexed
                    # mechanism and record a substantive disposition.
                    "applicable": None,
                }
            )

    add_history(cid, list(row.get("previous_audits") or []))
    for dep_id in row.get("deps") or []:
        add_history(
            dep_id,
            list(ledger_rows.get(dep_id, {}).get("previous_audits") or []),
            require_overlap=True,
        )

    root = Path(repo_root)
    obligations = _load_json(root, OBLIGATION_REGISTRY)
    for obligation_id, record in sorted((obligations.get("nodes") or {}).items()):
        candidates.append(
            {
                "candidate_id": f"open_gate:{obligation_id}",
                "kind": "open_gate",
                "source_claim_id": obligation_id,
                "record": record,
                "lifecycle_state": "active",
                "retired": False,
                "applicable": None,
            }
        )

    docs_markdown_paths, docs_negative_records = _docs_negative_corpus(root)
    current_note_path = str(row.get("note_path") or "")
    for record in docs_negative_records:
        path = record["path"]
        relative_path = path.relative_to(root).as_posix()
        if relative_path == current_note_path:
            continue
        overlap = sorted(current_terms.intersection(record["search_terms"]))
        if len(overlap) < 2:
            continue
        candidates.append(
            {
                "candidate_id": f"repo_negative_scan:{relative_path}",
                "kind": "repo_negative_phrase_hit",
                "note_path": relative_path,
                "content_sha256": record["content_sha256"],
                "matched_excerpts": record["excerpts"][:5],
                "matching_terms": overlap,
                "lifecycle_state": "unknown",
                "retired": None,
                "applicable": None,
            }
        )

    loop_ledger_glob = ".claude/science/physics-loops/**/NO_GO_LEDGER.md"
    loop_ledger_paths, loop_ledger_records = _loop_ledger_corpus(root, loop_ledger_glob)
    for record in loop_ledger_records:
        ledger_path = record["path"]
        ledger_text = record["text"]
        relative_path = ledger_path.relative_to(root).as_posix()
        matching_terms = sorted(current_terms.intersection(record["search_terms"]))
        if len(matching_terms) < 2:
            continue
        ledger_excerpts = [
            line.strip()[:400]
            for line in ledger_text.splitlines()
            if line.strip() and (
                current_terms.intersection(_search_terms(line))
                or DOCS_NEGATIVE_RE.search(line)
            )
        ][:10]
        candidates.append(
            {
                "candidate_id": f"physics_loop_no_go_ledger:{relative_path}",
                "kind": "physics_loop_no_go_ledger",
                "source_claim_id": relative_path,
                "note_path": relative_path,
                "content_sha256": record["content_sha256"],
                "content": ledger_excerpts,
                "content_truncated": len("\n".join(ledger_excerpts)) < len(ledger_text),
                "matching_terms": matching_terms,
                "lifecycle_state": "unknown",
                "retired": None,
                "applicable": None,
            }
        )

    no_go_universe = [
        {
            "claim_id": other_id,
            "note_path": str(other.get("note_path") or ""),
            "note_sha256": _read_bytes_sha256(
                root, str(other.get("note_path") or "")
            ),
        }
        for other_id, other in sorted(ledger_rows.items())
        if str(other.get("claim_type") or "") == "no_go"
    ]
    no_go_universe_sha256 = hashlib.sha256(
        json.dumps(no_go_universe, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
    ).hexdigest()

    similar: list[tuple[int, str, dict[str, Any], list[str]]] = []
    for other_id, other in ledger_rows.items():
        if other_id == cid:
            continue
        other_path = str(other.get("note_path") or "")
        if (
            str(other.get("claim_type") or "") != "no_go"
            and not PATH_TRIGGER_RE.search(other_path)
        ):
            continue
        other_note = _read_text(root, other_path)
        other_text = " ".join((other_id, other_path, other_note))
        overlap = sorted(current_terms.intersection(_search_terms(other_text)))
        if len(overlap) < 2:
            continue
        similar.append((len(overlap), other_id, other, overlap))
    for _score, other_id, other, overlap in sorted(
        similar, key=lambda item: (-item[0], item[1])
    ):
        note_path = str(other.get("note_path") or "")
        note_text = _read_text(root, note_path)
        matched_excerpts = [
            line.strip()[:400]
            for line in note_text.splitlines()
            if line.strip() and current_terms.intersection(_search_terms(line))
        ][:5]
        candidates.append(
            {
                "candidate_id": f"similar_negative_boundary:{other_id}",
                "kind": "similar_negative_boundary",
                "source_claim_id": other_id,
                "note_path": note_path,
                "content_sha256": _read_bytes_sha256(root, note_path),
                "matched_excerpts": matched_excerpts,
                "matching_terms": overlap,
                "lifecycle_state": "unknown",
                "retired": None,
                "applicable": None,
            }
        )
    kind_priority = {
        "prior_audit_cycle": 0,
        "open_gate": 1,
        "similar_negative_boundary": 2,
        "repo_negative_phrase_hit": 3,
        "physics_loop_no_go_ledger": 4,
    }
    ordered_candidates = sorted(
        candidates,
        key=lambda candidate: (
            kind_priority.get(str(candidate.get("kind")), 9),
            -len(candidate.get("matching_terms") or []),
            str(candidate.get("candidate_id") or ""),
        ),
    )
    # Reserve one identity from every nonempty candidate class before filling
    # the bounded relevance window. A global cap must never erase an entire
    # evidence class merely because an earlier class is large.
    reserved: list[dict[str, Any]] = []
    reserved_ids: set[str] = set()
    for candidate in ordered_candidates:
        kind = str(candidate.get("kind") or "")
        if kind in {str(item.get("kind") or "") for item in reserved}:
            continue
        reserved.append(candidate)
        reserved_ids.add(str(candidate.get("candidate_id") or ""))
    candidates = (
        reserved
        + [
            candidate for candidate in ordered_candidates
            if str(candidate.get("candidate_id") or "") not in reserved_ids
        ]
    )[:CROSS_CYCLE_CANDIDATE_LIMIT]
    return json.dumps(
        {
            "schema": "no_go_cross_cycle_index_v1",
            "claim_id": cid,
            "search_scope": {
                "current_row_audit_history": True,
                "one_hop_authority_audit_history": True,
                "historical_dispositions": True,
                "open_gates": True,
                "candidate_limit": CROSS_CYCLE_CANDIDATE_LIMIT,
                "candidate_order": (
                    "one reserved identity per nonempty kind, then kind priority, "
                    "shared-term count descending, candidate_id"
                ),
                "source_corpus_version": N8_SOURCE_CORPUS_VERSION,
                "docs_markdown_files_scanned": len(docs_markdown_paths),
                "docs_negative_phrase_hits_complete": True,
                "docs_candidate_policy": "negative phrase plus at least two current-row search terms",
                "similar_no_go_rows": {
                    "source": (
                        "all audit-ledger claim_type=no_go rows, union paths "
                        "with explicit no-go/boundary triggers"
                    ),
                    "minimum_shared_terms": 2,
                    "candidate_limit": None,
                },
                "physics_loop_no_go_ledgers": {
                    "glob": loop_ledger_glob,
                    "scanned_count": len(loop_ledger_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(
                            [path.relative_to(root).as_posix() for path in loop_ledger_paths],
                            separators=(",", ":"),
                        ).encode("utf-8")
                    ).hexdigest(),
                    "candidate_policy": "at least two current-row search terms; every tracked ledger is scanned",
                },
            },
            "no_go_row_universe": no_go_universe,
            "no_go_row_universe_count": len(no_go_universe),
            "no_go_row_universe_sha256": no_go_universe_sha256,
            "candidates": candidates,
        },
        indent=2,
        sort_keys=True,
    )


def build_partial_closure_index(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> str:
    """Render the orchestrator-owned N6 convention/reframe search surface."""
    root = Path(repo_root)
    cid = str(row.get("claim_id") or "")
    current_terms = _row_search_terms(row)
    candidates: list[dict[str, Any]] = []

    def add_candidate(
        *,
        candidate_id: str,
        kind: str,
        source_path: str,
        content: Any,
        matching_terms: list[str] | None = None,
        accepted_premise_type: str | None = None,
        content_sha256: str | None = None,
    ) -> None:
        candidates.append(
            {
                "candidate_id": candidate_id,
                "kind": kind,
                "source_path": source_path,
                "accepted_premise_type": accepted_premise_type,
                "matching_terms": matching_terms or [],
                "content_sha256": content_sha256,
                "content": content,
            }
        )

    axioms = _load_json(root, AXIOM_REGISTRY)
    for premise_id in sorted(axioms.get("canonical_ids") or []):
        add_candidate(
            candidate_id=f"approved_primitive:{premise_id}",
            kind="approved_primitive",
            source_path=AXIOM_REGISTRY,
            content=(axioms.get("nodes") or {}).get(premise_id, {}),
            accepted_premise_type="axiom_or_approved_primitive",
        )
    obligations = _load_json(root, OBLIGATION_REGISTRY)
    for obligation_id in sorted(obligations.get("canonical_ids") or []):
        add_candidate(
            candidate_id=f"open_gate:{obligation_id}",
            kind="open_gate",
            source_path=OBLIGATION_REGISTRY,
            content=(obligations.get("nodes") or {}).get(obligation_id, {}),
        )
    keyword_re = re.compile(
        r"\b(?:axiom|primitive|convention|definition|label(?:ing)?|meta|ratif\w*|refram\w*)\b",
        re.IGNORECASE,
    )

    def evidence_lines(content: str) -> list[dict[str, Any]]:
        ranked: list[tuple[int, int, int, dict[str, Any]]] = []
        for line_number, line in enumerate(content.splitlines(), 1):
            overlap = sorted(current_terms.intersection(_search_terms(line)))
            if not overlap:
                continue
            keyword_hit = bool(keyword_re.search(line))
            ranked.append(
                (
                    len(overlap),
                    int(keyword_hit),
                    line_number,
                    {
                        "line": line_number,
                        "matching_terms": overlap,
                        "partial_closure_keyword": keyword_hit,
                        "text": line,
                    },
                )
            )
        return [
            item[3]
            for item in sorted(ranked, key=lambda item: (-item[0], -item[1], item[2]))[:5]
        ]

    vocabulary_text = _read_text(root, CONTROLLED_VOCABULARY)
    vocabulary_hits: list[tuple[int, int, str, list[str]]] = []
    for line_number, line in enumerate(vocabulary_text.splitlines(), 1):
        overlap = sorted(current_terms.intersection(_search_terms(line)))
        if overlap and keyword_re.search(line):
            vocabulary_hits.append((len(overlap), line_number, line, overlap))
    for _score, line_number, line, overlap in sorted(
        vocabulary_hits, key=lambda item: (-item[0], item[1])
    )[:10]:
        add_candidate(
            candidate_id=f"controlled_vocabulary:{line_number}",
            kind="definition_refactor",
            source_path=CONTROLLED_VOCABULARY,
            content=line,
            matching_terms=overlap,
        )

    meta_paths = sorted(
        {
            str(other.get("note_path"))
            for other in ledger_rows.values()
            if other.get("claim_type") == "meta" and other.get("note_path")
        }
    )
    meta_hits: list[tuple[int, str, str, list[str]]] = []
    for path in meta_paths:
        content = _read_text(root, path)
        overlap = sorted(current_terms.intersection(_search_terms(content)))
        if len(overlap) >= 2 and keyword_re.search(content):
            meta_hits.append((len(overlap), path, content, overlap))
    for _score, path, content, overlap in sorted(
        meta_hits, key=lambda item: (-item[0], item[1])
    )[:10]:
        add_candidate(
            candidate_id=f"meta_reframe:{path}",
            kind="definition_refactor",
            source_path=path,
            content=evidence_lines(content),
            matching_terms=overlap,
            content_sha256=hashlib.sha256(content.encode("utf-8")).hexdigest(),
        )

    reframe_globs = (
        ".claude/science/physics-loops/**/HANDOFF.md",
        ".claude/science/physics-loops/**/BRANCH_HANDOFF.md",
        ".claude/science/physics-loops/**/CLAIM_STATUS_CERTIFICATE*.md",
    )
    reframe_paths = {ACTIVE_REVIEW_QUEUE}
    for pattern in reframe_globs:
        reframe_paths.update(path.relative_to(root).as_posix() for path in root.glob(pattern))
    reframe_hits: list[tuple[int, str, str, list[str]]] = []
    for path in sorted(reframe_paths):
        content = _read_text(root, path)
        overlap = sorted(current_terms.intersection(_search_terms(content)))
        if len(overlap) >= 2 and keyword_re.search(content):
            reframe_hits.append((len(overlap), path, content, overlap))
    for _score, path, content, overlap in sorted(
        reframe_hits, key=lambda item: (-item[0], item[1])
    )[:10]:
        add_candidate(
            candidate_id=f"in_flight_reframe:{path}",
            kind="definition_refactor",
            source_path=path,
            content=evidence_lines(content),
            matching_terms=overlap,
            content_sha256=hashlib.sha256(content.encode("utf-8")).hexdigest(),
        )

    return json.dumps(
        {
            "schema": "no_go_partial_closure_index_v1",
            "claim_id": cid,
            "search_scope": {
                "foundation_registry": AXIOM_REGISTRY,
                "open_obligation_registry": OBLIGATION_REGISTRY,
                "controlled_vocabulary": {
                    "path": CONTROLLED_VOCABULARY,
                    "content_sha256": hashlib.sha256(vocabulary_text.encode("utf-8")).hexdigest(),
                    "minimum_shared_terms": 1,
                    "candidate_limit": 10,
                },
                "meta_notes": {
                    "scanned_count": len(meta_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(meta_paths, separators=(",", ":")).encode("utf-8")
                    ).hexdigest(),
                    "minimum_shared_terms": 2,
                    "candidate_limit": 10,
                    "evidence_line_limit_per_candidate": 5,
                },
                "repository_visible_in_flight_reframes": {
                    "queue_path": ACTIVE_REVIEW_QUEUE,
                    "globs": list(reframe_globs),
                    "scanned_count": len(reframe_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(sorted(reframe_paths), separators=(",", ":")).encode("utf-8")
                    ).hexdigest(),
                    "minimum_shared_terms": 2,
                    "candidate_limit": 10,
                    "evidence_line_limit_per_candidate": 5,
                },
            },
            "candidates": candidates,
        },
        indent=2,
        sort_keys=True,
    )


def build_evidence_manifest(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> dict[str, dict]:
    """Build the exact source/runner/authority universe visible to the auditor."""
    root = Path(repo_root)
    manifest: dict[str, dict] = {}
    note_path = str(row.get("note_path") or "")
    _add_evidence(
        manifest,
        path=note_path,
        role="source",
        text=_read_text(root, note_path),
    )

    runner_path = _canonical_runner_path(root, row.get("runner_path"))
    _add_evidence(
        manifest,
        path=runner_path,
        role="runner",
        text=_read_text(root, runner_path),
    )
    for helper_raw in row.get("helper_runner_paths") or []:
        helper = _canonical_runner_path(root, helper_raw)
        _add_evidence(
            manifest,
            path=helper,
            role="helper",
            text=_read_text(root, helper),
        )

    for dep_id in row.get("deps") or []:
        dep = ledger_rows.get(dep_id, {})
        dep_path = str(dep.get("note_path") or "")
        _add_evidence(
            manifest,
            path=dep_path,
            role="authority",
            text=_read_text(root, dep_path),
            effective_status=dep.get("effective_status"),
            premise_type=premise_type_for_id(root, dep_id),
        )

    for registry_path, premise_type in (
        (AXIOM_REGISTRY, "axiom_or_approved_primitive"),
    ):
        registry = _load_json(root, registry_path)
        _add_evidence(
            manifest,
            path=registry_path,
            role="premise_registry",
            text=_read_text(root, registry_path),
            premise_type=premise_type,
        )
        for claim_id in registry.get("canonical_ids") or []:
            node = (registry.get("nodes") or {}).get(claim_id, {})
            current_path = str(node.get("current_path") or "")
            _add_evidence(
                manifest,
                path=current_path,
                role="framework_premise",
                text=_read_text(root, current_path),
                premise_type=premise_type,
            )

    _add_evidence(
        manifest,
        path=OBLIGATION_REGISTRY,
        role="open_obligation_registry",
        text=_read_text(root, OBLIGATION_REGISTRY),
    )
    _add_evidence(
        manifest,
        path=cross_cycle_index_path(str(row.get("claim_id") or "")),
        role="cross_cycle_index",
        text=build_cross_cycle_index(row, ledger_rows, root),
    )
    _add_evidence(
        manifest,
        path=partial_closure_index_path(str(row.get("claim_id") or "")),
        role="partial_closure_index",
        text=build_partial_closure_index(row, ledger_rows, root),
    )
    attach_full_scan_authentication(manifest, root)
    return manifest


def render_evidence_manifest(manifest: dict[str, dict]) -> str:
    visible = []
    for path in sorted(manifest):
        entry = manifest[path]
        visible.append(
            {
                "path": path,
                "roles": entry.get("roles") or [],
                "effective_status": entry.get("effective_status"),
                "accepted_premise_type": entry.get("accepted_premise_type"),
                "full_content_sha256": entry.get("full_content_sha256"),
                "full_phrase_groups": entry.get("full_phrase_groups") or [],
            }
        )
    return json.dumps(visible, indent=2, sort_keys=True)


def render_framework_premise_context(manifest: dict[str, dict]) -> str:
    blocks = []
    for path in sorted(manifest):
        entry = manifest[path]
        roles = set(entry.get("roles") or [])
        if not roles.intersection({"premise_registry", "framework_premise"}):
            continue
        blocks.append(
            f"=== BEGIN FRAMEWORK PREMISE CONTEXT: {path} ===\n"
            f"accepted_premise_type: {entry.get('accepted_premise_type')}\n"
            f"{entry.get('text') or '[missing registry/source content]'}\n"
            f"=== END FRAMEWORK PREMISE CONTEXT: {path} ==="
        )
    return "\n\n".join(blocks)


def _evidence_references(value: Any) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    if isinstance(value, dict):
        path = value.get("evidence_path")
        locator = value.get("evidence_locator")
        if _text(path) and _text(locator):
            refs.append((path, locator))
        for child in value.values():
            refs.extend(_evidence_references(child))
    elif isinstance(value, list):
        for child in value:
            refs.extend(_evidence_references(child))
    return refs


def _string_leaves(value: Any) -> set[str]:
    leaves: set[str] = set()
    if isinstance(value, str) and value.strip():
        leaves.add(value)
    elif isinstance(value, dict):
        for child in value.values():
            leaves.update(_string_leaves(child))
    elif isinstance(value, list):
        for child in value:
            leaves.update(_string_leaves(child))
    return leaves


def _index_candidates(
    entry: dict[str, Any], *, schema: str, stored_field: str,
    stored_records_field: str,
) -> dict[str, dict[str, Any]] | None:
    stored_records = entry.get(stored_records_field)
    if isinstance(stored_records, list):
        candidates = stored_records
    else:
        candidates = None
    stored = entry.get(stored_field)
    if candidates is None and isinstance(stored, list) and all(_text(item) for item in stored):
        return {str(item): {} for item in stored}
    if candidates is None:
        try:
            parsed = json.loads(str(entry.get("text") or ""))
        except json.JSONDecodeError:
            return None
        if not isinstance(parsed, dict):
            return None
        if parsed.get("schema") != schema:
            return None
        candidates = parsed.get("candidates")
    if not isinstance(candidates, list):
        return None
    mapped = {
        str(candidate.get("candidate_id")): candidate
        for candidate in candidates
        if isinstance(candidate, dict) and _text(candidate.get("candidate_id"))
    }
    if len(mapped) != len(candidates):
        return None
    return mapped


def _cross_cycle_candidate_ids(entry: dict[str, Any]) -> set[str] | None:
    candidates = _index_candidates(
        entry,
        schema="no_go_cross_cycle_index_v1",
        stored_field="cross_cycle_candidate_ids",
        stored_records_field="cross_cycle_candidates",
    )
    return set(candidates) if candidates is not None else None


def _cross_cycle_no_go_universe(entry: dict[str, Any]) -> tuple[int, str] | None:
    count = entry.get("no_go_row_universe_count")
    digest = entry.get("no_go_row_universe_sha256")
    if count is None or digest is None:
        try:
            payload = json.loads(str(entry.get("text") or ""))
        except json.JSONDecodeError:
            return None
        count = payload.get("no_go_row_universe_count")
        digest = payload.get("no_go_row_universe_sha256")
    if (
        not isinstance(count, int)
        or count < 0
        or not isinstance(digest, str)
        or not re.fullmatch(r"[0-9a-f]{64}", digest)
    ):
        return None
    return count, digest


def _partial_closure_candidates(
    entry: dict[str, Any],
) -> dict[str, dict[str, Any]] | None:
    return _index_candidates(
        entry,
        schema="no_go_partial_closure_index_v1",
        stored_field="partial_closure_candidate_ids",
        stored_records_field="partial_closure_candidates",
    )


def build_evidence_snapshot(
    packet: dict[str, Any], manifest: dict[str, dict]
) -> dict[str, Any]:
    """Persist exact locators authenticated against the rendered packet."""
    grouped: dict[str, set[str]] = {}
    for path, locator in _evidence_references(packet):
        grouped.setdefault(path, set()).add(locator)
    entries: dict[str, dict[str, Any]] = {}
    packet_strings = _string_leaves(packet)
    for path, entry in sorted(manifest.items()):
        locators = grouped.get(path, set())
        text = str(entry.get("text") or "")
        snapshot_entry: dict[str, Any] = {
            "path": path,
            "roles": list(entry.get("roles") or []),
            "effective_status": entry.get("effective_status"),
            "accepted_premise_type": entry.get("accepted_premise_type"),
            "content_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "full_content_sha256": entry.get("full_content_sha256"),
            "full_phrase_groups": entry.get("full_phrase_groups") or [],
            "invocation_bound_rendered_text": bool(
                entry.get("invocation_bound_rendered_text")
            ),
            "verified_locators": sorted(locators),
            "verified_values": sorted(
                value for value in packet_strings if _norm(value) in _norm(text)
            ),
        }
        phrase_occurrences = required_phrase_occurrences(
            {path: entry},
            {"source", "authority"},
            tuple(dict.fromkeys((*N3_SCAN_PHRASES, *N5_SCAN_PHRASES))),
        )
        snapshot_entry["phrase_occurrences"] = [
            {
                "phrase": phrase,
                "occurrence_index": occurrence_index,
                "locator": locator,
            }
            for (_path, phrase, occurrence_index), locator
            in sorted(phrase_occurrences.items())
        ]
        if "cross_cycle_index" in set(entry.get("roles") or []):
            candidates = _index_candidates(
                entry, schema="no_go_cross_cycle_index_v1",
                stored_field="cross_cycle_candidate_ids",
                stored_records_field="cross_cycle_candidates",
            )
            if candidates is None:
                raise ValueError("cross-cycle index is not orchestrator-authenticated")
            snapshot_entry["cross_cycle_candidate_ids"] = sorted(candidates)
            snapshot_entry["cross_cycle_candidates"] = [
                candidates[candidate_id] for candidate_id in sorted(candidates)
            ]
            try:
                cross_payload = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValueError("cross-cycle index JSON is malformed") from exc
            snapshot_entry["no_go_row_universe_count"] = cross_payload.get(
                "no_go_row_universe_count"
            )
            snapshot_entry["no_go_row_universe_sha256"] = cross_payload.get(
                "no_go_row_universe_sha256"
            )
        if "partial_closure_index" in set(entry.get("roles") or []):
            candidates = _partial_closure_candidates(entry)
            if candidates is None:
                raise ValueError("partial-closure index is not orchestrator-authenticated")
            snapshot_entry["partial_closure_candidate_ids"] = sorted(candidates)
            snapshot_entry["partial_closure_candidates"] = [
                candidates[candidate_id] for candidate_id in sorted(candidates)
            ]
        entries[path] = snapshot_entry
    return {"schema": "no_go_evidence_snapshot_v1", "entries": entries}


def evidence_manifest_from_snapshot(packet: dict[str, Any]) -> dict[str, dict] | None:
    if not isinstance(packet, dict):
        return None
    snapshot = packet.get("evidence_snapshot")
    if not isinstance(snapshot, dict) or snapshot.get("schema") != "no_go_evidence_snapshot_v1":
        return None
    raw_entries = snapshot.get("entries")
    if not isinstance(raw_entries, dict):
        return None
    manifest: dict[str, dict] = {}
    for path, stored in raw_entries.items():
        if not _text(path) or not isinstance(stored, dict):
            return None
        locators = stored.get("verified_locators")
        if not isinstance(locators, list) or not all(_text(x) for x in locators):
            return None
        values = stored.get("verified_values")
        if not isinstance(values, list) or not all(_text(x) for x in values):
            return None
        roles = stored.get("roles")
        if not isinstance(roles, list) or not all(_text(role) for role in roles):
            return None
        content_sha256 = stored.get("content_sha256")
        if not isinstance(content_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", content_sha256):
            return None
        phrase_occurrences = stored.get("phrase_occurrences")
        if not isinstance(phrase_occurrences, list):
            return None
        for occurrence in phrase_occurrences:
            if (
                not isinstance(occurrence, dict)
                or not _text(occurrence.get("phrase"))
                or not isinstance(occurrence.get("occurrence_index"), int)
                or occurrence["occurrence_index"] <= 0
                or not _text(occurrence.get("locator"))
            ):
                return None
        full_content_sha256 = stored.get("full_content_sha256")
        if full_content_sha256 is not None and (
            not isinstance(full_content_sha256, str)
            or not re.fullmatch(r"[0-9a-f]{64}", full_content_sha256)
        ):
            return None
        full_phrase_groups = stored.get("full_phrase_groups")
        if not isinstance(full_phrase_groups, list):
            return None
        for group in full_phrase_groups:
            if (
                not isinstance(group, dict)
                or not _text(group.get("phrase"))
                or not isinstance(group.get("occurrence_group_id"), str)
                or not re.fullmatch(r"[0-9a-f]{16}", group["occurrence_group_id"])
                or not isinstance(group.get("occurrence_count"), int)
                or group["occurrence_count"] < 1
                or not isinstance(group.get("occurrence_locator_sha256"), str)
                or not re.fullmatch(
                    r"[0-9a-f]{64}", group["occurrence_locator_sha256"]
                )
                or not _text(group.get("evidence_locator"))
            ):
                return None
        invocation_bound_rendered_text = stored.get(
            "invocation_bound_rendered_text", False
        )
        if not isinstance(invocation_bound_rendered_text, bool):
            return None
        for field in ("cross_cycle_candidates", "partial_closure_candidates"):
            if stored.get(field) is not None and not isinstance(stored[field], list):
                return None
        universe_count = stored.get("no_go_row_universe_count")
        universe_sha256 = stored.get("no_go_row_universe_sha256")
        if "cross_cycle_index" in set(roles):
            if not isinstance(universe_count, int) or universe_count < 0:
                return None
            if not isinstance(universe_sha256, str) or not re.fullmatch(
                r"[0-9a-f]{64}", universe_sha256
            ):
                return None
        manifest[path] = {
            "path": path,
            "roles": list(roles),
            "text": "",
            "verified_locators": list(locators),
            "verified_values": list(values),
            "effective_status": stored.get("effective_status"),
            "accepted_premise_type": stored.get("accepted_premise_type"),
            "content_sha256": content_sha256,
            "full_content_sha256": full_content_sha256,
            "full_phrase_groups": full_phrase_groups,
            "invocation_bound_rendered_text": invocation_bound_rendered_text,
            "cross_cycle_candidate_ids": stored.get("cross_cycle_candidate_ids"),
            "cross_cycle_candidates": stored.get("cross_cycle_candidates"),
            "no_go_row_universe_count": universe_count,
            "no_go_row_universe_sha256": universe_sha256,
            "partial_closure_candidate_ids": stored.get("partial_closure_candidate_ids"),
            "partial_closure_candidates": stored.get("partial_closure_candidates"),
            "phrase_occurrences": phrase_occurrences,
        }
    return manifest


def evidence_snapshot_current_error(
    packet: dict[str, Any], current_manifest: dict[str, dict]
) -> str | None:
    """Reauthenticate stable file-backed snapshot entries against current bytes."""
    stored_manifest = evidence_manifest_from_snapshot(packet)
    if stored_manifest is None:
        return "evidence_snapshot is malformed or predates the current authenticated schema"
    stable_roles = {
        "source", "authority", "runner", "helper", "premise_registry",
        "framework_premise",
    }
    stored_stable_paths = {
        path for path, entry in stored_manifest.items()
        if stable_roles.intersection(set(entry.get("roles") or []))
    }
    current_stable_paths = {
        path for path, entry in current_manifest.items()
        if stable_roles.intersection(set(entry.get("roles") or []))
    }
    if stored_stable_paths != current_stable_paths:
        return "evidence_snapshot stable evidence path universe changed"
    for path, stored in stored_manifest.items():
        roles = set(stored.get("roles") or [])
        dynamic_index = bool(
            {"cross_cycle_index", "partial_closure_index"}.intersection(roles)
        )
        if not dynamic_index and not stable_roles.intersection(roles):
            # Live runner stdout is invocation-bound by the trusted transport
            # envelope, not reconstructed from repository state.
            continue
        current = current_manifest.get(path)
        if current is None:
            return f"evidence_snapshot path {path!r} is absent from the current packet"
        if dynamic_index or not stored.get("invocation_bound_rendered_text"):
            current_text_hash = hashlib.sha256(
                str(current.get("text") or "").encode("utf-8")
            ).hexdigest()
            if current_text_hash != stored.get("content_sha256"):
                return f"evidence_snapshot rendered content drifted for {path!r}"
        if dynamic_index:
            if "cross_cycle_index" in roles:
                current_candidates = _index_candidates(
                    current, schema="no_go_cross_cycle_index_v1",
                    stored_field="cross_cycle_candidate_ids",
                    stored_records_field="cross_cycle_candidates",
                )
                stored_candidates = _index_candidates(
                    stored, schema="no_go_cross_cycle_index_v1",
                    stored_field="cross_cycle_candidate_ids",
                    stored_records_field="cross_cycle_candidates",
                )
            else:
                current_candidates = _partial_closure_candidates(current)
                stored_candidates = _partial_closure_candidates(stored)
            if current_candidates != stored_candidates:
                return f"evidence_snapshot candidate set drifted for {path!r}"
            continue
        if not stable_roles.intersection(roles):
            continue
        if stored.get("full_content_sha256") is not None:
            if current.get("full_content_sha256") != stored.get("full_content_sha256"):
                return f"evidence_snapshot raw content hash drifted for {path!r}"
        if set(current.get("roles") or []) != roles:
            return f"evidence_snapshot roles drifted for {path!r}"
        for field in ("effective_status", "accepted_premise_type"):
            if current.get(field) != stored.get(field):
                return f"evidence_snapshot {field} drifted for {path!r}"
    return None


def _has_governed_no_existence(text: str) -> bool:
    return any(
        not BOUNDARY_ABSENCE_SUBJECT_RE.search(match.group("subject"))
        for match in NO_EXISTENCE_ASSERTION_RE.finditer(text)
    )


def _has_negative_boundary_assertion(text: str) -> bool:
    # Inline Markdown/TeX delimiters are presentation, not grammar. Removing
    # them lets `kappa_EW`, `$Z$`, and route labels such as `(S1)-(S3)` use the
    # same governed subject rules as plain prose.
    prose = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    prose = re.sub(
        r"`[^`\n]*(?:[/_.-]|\.(?:py|md|json|txt))[^`\n]*`", "", prose
    )
    prose = re.sub(
        r"\b[\w./-]*(?:firewall|no[-_]?go)[\w./-]*\.(?:py|md|json|txt)\b",
        "",
        prose,
        flags=re.IGNORECASE,
    )
    normalized = re.sub(r"[`*_~$(){}\[\]]", "", prose)
    cleaned = NEGATED_NEGATIVE_ASSURANCE_RE.sub("", normalized)
    cleaned = NEGATED_LABEL_ASSURANCE_RE.sub("", cleaned)
    cleaned = LOCAL_SCOPE_EXCLUSION_RE.sub("", cleaned)
    if (
        EXPLICIT_NEGATIVE_CLOSURE_RE.search(cleaned)
        or NEGATIVE_SUBJECT_CLOSURE_RE.search(cleaned)
        or _has_governed_no_existence(cleaned)
        or INABILITY_CLOSURE_RE.search(cleaned)
        or BOUNDARY_SUBJECT_NEGATIVE_RE.search(cleaned)
    ):
        return True
    cleaned = POSITIVE_BOUNDARY_CLOSURE_RE.sub("", cleaned)
    cleaned = NEGATED_BOUNDARY_RE.sub("", cleaned)
    return bool(NEGATIVE_ASSERTION_RE.search(cleaned))


def source_requires_no_go_discipline(
    note_path: str | None,
    note_body: str | None,
    claim_type_hint: str | None,
) -> bool:
    if claim_type_hint == "no_go":
        return True
    path_text = re.sub(r"[_-]+", " ", note_path or "")
    if PATH_TRIGGER_RE.search(path_text):
        return True
    body = note_body or ""
    metadata = "\n".join(body.splitlines()[:80])
    if re.search(r"(?:Type|Claim type)\s*:\s*`?no_go`?", metadata, re.IGNORECASE):
        return True
    return _has_negative_boundary_assertion(body)


def output_requires_no_go_discipline(audit: dict[str, Any]) -> bool:
    if audit.get("claim_type") == "no_go":
        return True
    boundary = "\n".join(str(audit.get(field) or "") for field in OUTPUT_BOUNDARY_FIELDS)
    if _has_negative_boundary_assertion(boundary):
        return True
    return _has_negative_boundary_assertion(
        str(audit.get("notes_for_re_audit_if_any") or "")
    )


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any) -> bool:
    return isinstance(value, list)


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def _semantic_norm(value: str) -> str:
    normalized = re.sub(
        r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|first|second|third|fourth|fifth)\b|\d+",
        " ",
        value.casefold(),
    )
    normalized = re.sub(r"[^a-z]+", " ", normalized)
    return _norm(normalized)


def _entry_contains(entry: dict[str, Any], value: str) -> bool:
    if _norm(value) in _norm(str(entry.get("text") or "")):
        return True
    return any(
        _norm(value) == _norm(candidate)
        for candidate in entry.get("verified_values") or []
        if _text(candidate)
    ) or any(
        _norm(value) in {
            _norm(str(group.get("phrase") or "")),
            _norm(str(group.get("evidence_locator") or "")),
        }
        for group in entry.get("full_phrase_groups") or []
        if isinstance(group, dict)
    )


def _scan_coverage_error(
    section: dict[str, Any],
    manifest: dict[str, dict] | None,
    roles: set[str],
    label: str,
) -> str | None:
    scanned = section.get("scanned_evidence_paths")
    if not isinstance(scanned, list) or not all(_text(path) for path in scanned):
        return f"{label}.scanned_evidence_paths must be a list of packet paths"
    if len(set(scanned)) != len(scanned):
        return f"{label}.scanned_evidence_paths contains duplicates"
    if manifest is None:
        return None
    required = {
        path
        for path, entry in manifest.items()
        if roles.intersection(set(entry.get("roles") or []))
    }
    if set(scanned) != required:
        return f"{label}.scanned_evidence_paths must exactly cover {sorted(required)}"
    return None


def required_phrase_occurrences(
    manifest: dict[str, dict] | None,
    roles: set[str],
    phrases: tuple[str, ...],
) -> dict[tuple[str, str, int], str]:
    """Return every orchestrator-visible phrase occurrence and exact locator."""
    if manifest is None:
        return {}
    required: dict[tuple[str, str, int], str] = {}
    for path, entry in manifest.items():
        if not roles.intersection(set(entry.get("roles") or [])):
            continue
        text = str(entry.get("text") or "")
        if not text and isinstance(entry.get("phrase_occurrences"), list):
            for occurrence in entry["phrase_occurrences"]:
                if not isinstance(occurrence, dict):
                    continue
                phrase = occurrence.get("phrase")
                index = occurrence.get("occurrence_index")
                locator = occurrence.get("locator")
                if phrase in phrases and isinstance(index, int) and index > 0 and _text(locator):
                    required[(path, _norm(phrase), index)] = locator
            continue
        lines = text.splitlines()
        for phrase in phrases:
            pattern = r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b"
            occurrence_index = 0
            for line_index, line in enumerate(lines):
                for _match in re.finditer(pattern, line, re.IGNORECASE):
                    occurrence_index += 1
                    locator = line.strip()
                    if len(_norm(locator)) < 12:
                        start = max(0, line_index - 1)
                        stop = min(len(lines), line_index + 2)
                        locator = " ".join(
                            part.strip() for part in lines[start:stop] if part.strip()
                        )
                    required[(path, _norm(phrase), occurrence_index)] = locator[:400]
    return required


def required_phrase_groups(
    manifest: dict[str, dict], roles: set[str], phrases: tuple[str, ...]
) -> dict[tuple[str, str, str], dict[str, Any]]:
    """Group only occurrences with identical normalized local context."""
    authenticated: dict[tuple[str, str, str], dict[str, Any]] = {}
    requested = {_norm(phrase) for phrase in phrases}
    for path, entry in manifest.items():
        if not roles.intersection(set(entry.get("roles") or [])):
            continue
        groups = entry.get("full_phrase_groups")
        if not isinstance(groups, list):
            continue
        for group in groups:
            if not isinstance(group, dict) or _norm(str(group.get("phrase") or "")) not in requested:
                continue
            phrase = _norm(str(group["phrase"]))
            group_id = str(group.get("occurrence_group_id") or "")
            if not group_id:
                continue
            authenticated[(path, phrase, group_id)] = {
                "occurrence_group_id": group_id,
                "occurrence_count": group.get("occurrence_count"),
                "occurrence_locator_sha256": group.get("occurrence_locator_sha256"),
                "evidence_locator": group.get("evidence_locator"),
            }
    if authenticated:
        return authenticated

    occurrences = required_phrase_occurrences(manifest, roles, phrases)
    grouped: dict[tuple[str, str, str], list[tuple[int, str]]] = {}
    for (path, phrase, occurrence_index), locator in occurrences.items():
        context_digest = hashlib.sha256(_norm(locator).encode("utf-8")).hexdigest()
        group_id = context_digest[:16]
        grouped.setdefault((path, phrase, group_id), []).append(
            (occurrence_index, locator)
        )
    result: dict[tuple[str, str, str], dict[str, Any]] = {}
    for key, items in grouped.items():
        ordered = sorted(items)
        digest_payload = json.dumps(ordered, ensure_ascii=False, separators=(",", ":"))
        result[key] = {
            "occurrence_group_id": key[2],
            "occurrence_count": len(ordered),
            "occurrence_locator_sha256": hashlib.sha256(
                digest_payload.encode("utf-8")
            ).hexdigest(),
            "evidence_locator": ordered[0][1],
        }
    return result


def attach_full_scan_authentication(
    manifest: dict[str, dict], repo_root: str | Path
) -> None:
    """Bind stable file evidence to raw bytes before any display clipping."""
    root = Path(repo_root)
    phrases = tuple(dict.fromkeys((*N3_SCAN_PHRASES, *N5_SCAN_PHRASES)))
    for path, entry in manifest.items():
        roles = set(entry.get("roles") or [])
        if not roles.intersection({
            "source", "authority", "runner", "helper", "premise_registry",
            "framework_premise",
        }):
            continue
        text = str(entry.get("text") or "")
        entry["full_content_sha256"] = _read_bytes_sha256(root, path)
        if not {"source", "authority"}.intersection(roles):
            entry["full_phrase_groups"] = []
            continue
        groups = required_phrase_groups(
            {path: {**entry, "full_phrase_groups": None}},
            {"source", "authority"},
            phrases,
        )
        entry["full_phrase_groups"] = [
            {
                "phrase": phrase,
                **group,
            }
            for (_path, phrase, _group_id), group in sorted(groups.items())
        ]


def _unknown_fields(value: dict[str, Any], allowed: set[str], label: str) -> str | None:
    unknown = set(value) - allowed
    if unknown:
        return f"{label} contains unknown fields {sorted(unknown)}"
    return None


def _scope_tokens(value: str) -> set[str]:
    stop = {"a", "an", "and", "for", "in", "of", "on", "the", "to", "with"}
    return {
        token
        for token in re.findall(r"[a-z0-9_]+", value.casefold())
        if token not in stop
    }


LOGICAL_SCOPE_TOKENS = {
    "all", "any", "cannot", "except", "no", "none", "not", "only",
    "unless", "without", "fail", "fails", "failed", "unable", "insufficient",
    "impossible", "never", "absence", "nonexistence", "impossibility",
    "failure", "lack",
    "non", "derivability", "underdetermination", "inability", "supply", "closure",
}


def _none_found_error(section: dict, items: list[Any], label: str) -> str | None:
    if items:
        return None
    if not _text(section.get("none_found_reason")):
        return f"{label} requires an explicit none_found_reason when its result list is empty"
    return None


def _locator_error(
    evidence_path: Any,
    evidence_locator: Any,
    manifest: dict[str, dict] | None,
    label: str,
) -> str | None:
    if not _text(evidence_path) or not _text(evidence_locator):
        return f"{label} requires non-empty evidence_path and evidence_locator"
    if len(_norm(evidence_locator)) < 12:
        return f"{label} evidence_locator must contain at least 12 normalized characters"
    if manifest is None:
        return None
    entry = manifest.get(evidence_path)
    if not entry:
        return f"{label} evidence_path {evidence_path!r} is outside the restricted packet"
    if not _entry_contains(entry, evidence_locator):
        return f"{label} evidence_locator is not present in {evidence_path!r}"
    return None


def _unresolved_error(section: dict, label: str, status: str) -> str | None:
    unresolved = section.get("unresolved")
    if not _list(unresolved) or not all(_text(item) for item in unresolved):
        return f"{label}.unresolved must be a list of non-empty strings"
    if status == "PASS" and unresolved:
        return f"No-Go Discipline PASS requires {label}.unresolved to be empty"
    return None


def _validate_n1(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    routes = packet.get("N1_alternative_routes")
    if not _list(routes):
        return "N1_alternative_routes must be a list"
    route_ids: set[str] = set()
    route_classes: set[str] = set()
    for index, route in enumerate(routes, 1):
        if not isinstance(route, dict):
            return f"N1 route {index} must be an object"
        error = _unknown_fields(
            route,
            {
                "route_id", "route_class", "mechanism", "attempt", "outcome",
                "honesty_marker", "disposition", "prior_witness_id",
                "evidence_path", "evidence_locator",
            },
            f"N1 route {index}",
        )
        if error:
            return error
        for field in (
            "route_id",
            "route_class",
            "mechanism",
            "attempt",
            "outcome",
            "honesty_marker",
            "disposition",
        ):
            if not _text(route.get(field)):
                return f"N1 route {index}.{field} must be non-empty"
        route_id = _norm(route["route_id"])
        route_class = route["route_class"].strip()
        if route_id in route_ids:
            return f"N1 route_id {route['route_id']!r} is duplicated"
        if route_class not in ROUTE_CLASSES:
            return f"N1 route {index}.route_class must be one of {sorted(ROUTE_CLASSES)}"
        marker = route["honesty_marker"].strip().upper()
        disposition = route["disposition"].strip().upper()
        if marker not in HONESTY_MARKERS:
            return f"N1 route {index}.honesty_marker is invalid"
        if disposition not in ROUTE_DISPOSITIONS:
            return f"N1 route {index}.disposition is invalid"
        error = _locator_error(
            route.get("evidence_path"), route.get("evidence_locator"), manifest, f"N1 route {index}"
        )
        if error:
            return error
        if manifest is not None:
            entry = manifest[route["evidence_path"]]
            for field in ("mechanism", "attempt", "outcome"):
                if not _entry_contains(entry, route[field]):
                    return f"N1 route {index}.{field} is not evidenced at evidence_path"
            if marker == "ATTEMPTED" and "runner_stdout" not in set(
                entry.get("roles") or []
            ):
                return (
                    f"N1 route {index} ATTEMPTED must cite current-cycle "
                    "live runner_stdout evidence"
                )
        if manifest is not None and marker == "RULED OUT BY PRIOR":
            entry = manifest[route["evidence_path"]]
            roles = set(entry.get("roles") or [])
            if not roles.intersection({"authority", "framework_premise", "premise_registry"}):
                return (
                    f"N1 route {index} RULED OUT BY PRIOR must cite a retained "
                    "one-hop authority or registered accepted premise"
                )
            if (
                entry.get("effective_status") not in RETAINED_GRADE
                and entry.get("accepted_premise_type") not in PRIOR_AUTHORITY_PREMISE_TYPES
            ):
                return f"N1 route {index} prior authority is not retained-grade or an accepted premise"
            if not _text(route.get("prior_witness_id")):
                return f"N1 route {index} RULED OUT BY PRIOR requires prior_witness_id"
        if status == "PASS" and disposition != "CLOSED":
            return f"No-Go Discipline PASS cannot contain N1 route {index} disposition={disposition}"
        route_ids.add(route_id)
        route_classes.add(route_class)
    if status == "PASS" and len(route_classes) < 5:
        return "No-Go Discipline PASS requires at least 5 distinct route_class values"
    mechanisms = [_semantic_norm(route["mechanism"]) for route in routes]
    attempts = [_semantic_norm(route["attempt"]) for route in routes]
    if not all(mechanisms) or not all(attempts):
        return "N1 mechanisms and attempts must contain semantic content beyond numbering"
    if len(set(mechanisms)) != len(mechanisms):
        return "N1 routes must name distinct mechanisms, not numbered paraphrases"
    if len(set(attempts)) != len(attempts):
        return "N1 routes must record distinct attempts, not duplicate prose"
    return None


def _section(packet: dict, field: str) -> tuple[dict | None, str | None]:
    value = packet.get(field)
    if not isinstance(value, dict):
        return None, f"{field} must be an object"
    return value, None


def _validate_n2(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N2_wall_independence")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"walls", "pairwise_checks", "collapsed_wall_set", "unresolved", "evidence_path", "evidence_locator"},
        "N2",
    )
    if error:
        return error
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N2")
    if error:
        return error
    walls = section.get("walls")
    collapsed = section.get("collapsed_wall_set")
    checks = section.get("pairwise_checks")
    if not _list(walls) or not all(_text(w) for w in walls) or len({_norm(w) for w in walls}) != len(walls):
        return "N2.walls must be a list of distinct non-empty strings"
    if manifest is not None:
        entry = manifest.get(section["evidence_path"])
        if entry is None or any(not _entry_contains(entry, wall) for wall in walls):
            return "N2.walls must each be evidenced at N2.evidence_path"
    if not _list(collapsed) or not all(_text(w) for w in collapsed):
        return "N2.collapsed_wall_set must be a list of non-empty strings"
    wall_map = {_norm(w): w for w in walls}
    if any(_norm(w) not in wall_map for w in collapsed):
        return "N2.collapsed_wall_set must be a subset of walls"
    if not _list(checks):
        return "N2.pairwise_checks must be a list"
    expected_pairs = {frozenset((_norm(a), _norm(b))) for a, b in combinations(walls, 2)}
    seen_pairs = set()
    dependent_walls: set[str] = set()
    directional_edges: list[tuple[str, str]] = []
    for index, check in enumerate(checks, 1):
        if not isinstance(check, dict) or not _text(check.get("left")) or not _text(check.get("right")):
            return f"N2 pairwise check {index} must name left and right walls"
        error = _unknown_fields(
            check,
            {
                "left", "right", "left_closes_right", "right_closes_left",
                "independent", "rationale", "evidence_path", "evidence_locator",
            },
            f"N2 pairwise check {index}",
        )
        if error:
            return error
        pair = frozenset((_norm(check["left"]), _norm(check["right"])))
        if pair not in expected_pairs or pair in seen_pairs:
            return f"N2 pairwise check {index} is duplicate or names unknown walls"
        for field in ("left_closes_right", "right_closes_left", "independent"):
            if not isinstance(check.get(field), bool):
                return f"N2 pairwise check {index}.{field} must be boolean"
        expected_independent = not check["left_closes_right"] and not check["right_closes_left"]
        if check["independent"] != expected_independent:
            return f"N2 pairwise check {index}.independent is inconsistent"
        if check["left_closes_right"] and check["right_closes_left"]:
            return f"N2 pairwise check {index} cannot claim both directional closures"
        if not _text(check.get("rationale")) or len(_norm(check["rationale"])) < 40:
            return f"N2 pairwise check {index}.rationale must explain the directional test"
        if _norm(check["left"]) not in _norm(check["rationale"]) or _norm(check["right"]) not in _norm(check["rationale"]):
            return f"N2 pairwise check {index}.rationale must name both walls"
        error = _locator_error(
            check.get("evidence_path"), check.get("evidence_locator"), manifest,
            f"N2 pairwise check {index}",
        )
        if error:
            return error
        if manifest is not None and not _entry_contains(
            manifest[check["evidence_path"]], check["rationale"]
        ):
            return f"N2 pairwise check {index}.rationale is not evidenced at evidence_path"
        if check["left_closes_right"]:
            dependent_walls.add(_norm(check["right"]))
            directional_edges.append((_norm(check["left"]), _norm(check["right"])))
        if check["right_closes_left"]:
            dependent_walls.add(_norm(check["left"]))
            directional_edges.append((_norm(check["right"]), _norm(check["left"])))
        seen_pairs.add(pair)
    if seen_pairs != expected_pairs:
        return "N2.pairwise_checks must cover every unordered wall pair"
    graph: dict[str, set[str]] = {wall: set() for wall in wall_map}
    for source, target in directional_edges:
        graph[source].add(target)
    visiting: set[str] = set()
    visited: set[str] = set()

    def has_cycle(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(has_cycle(target) for target in graph[node]):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    if any(has_cycle(wall) for wall in graph):
        return "N2 directional closure relation must be acyclic"
    expected_collapsed = set(wall_map) - dependent_walls
    if status == "PASS" and not expected_collapsed:
        return "No-Go Discipline PASS must retain at least one evidenced N2 wall"
    if {_norm(wall) for wall in collapsed} != expected_collapsed:
        return (
            "N2.collapsed_wall_set must retain exactly the walls not closed "
            "by a directional pairwise result"
        )
    return _unresolved_error(section, "N2", status)


def _validate_n3(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N3_hidden_wall_scan")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "scanned_evidence_paths", "hits", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N3",
    )
    if error:
        return error
    error = _scan_coverage_error(section, manifest, {"source", "authority"}, "N3")
    if error:
        return error
    if not _text(section.get("scan_scope")):
        return "N3.scan_scope must name the phrases and packet surfaces checked"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N3 scan")
    if error:
        return error
    hits = section.get("hits")
    if not _list(hits):
        return "N3.hits must be a list"
    error = _none_found_error(section, hits, "N3")
    if error:
        return error
    walls = {_norm(w) for w in packet["N2_wall_independence"].get("walls") or []}
    observed_hits: dict[tuple[str, str, str], dict[str, Any]] = {}
    for index, hit in enumerate(hits, 1):
        if not isinstance(hit, dict) or not _text(hit.get("phrase")):
            return f"N3 hit {index} must name a phrase"
        error = _unknown_fields(
            hit,
            {
                "phrase", "occurrence_group_id", "occurrence_count",
                "occurrence_locator_sha256",
                "classification", "promoted_wall",
                "rationale", "evidence_path", "evidence_locator",
            },
            f"N3 hit {index}",
        )
        if error:
            return error
        classification = hit.get("classification")
        if not isinstance(classification, str):
            return f"N3 hit {index}.classification is invalid"
        if classification not in {"retained_authority", "hidden_admission", "non_load_bearing"}:
            return f"N3 hit {index}.classification is invalid"
        if classification == "non_load_bearing" and (
            not _text(hit.get("rationale"))
            or len(_norm(hit["rationale"])) < 40
        ):
            return f"N3 hit {index}.rationale must explain why the occurrence is non-load-bearing"
        error = _locator_error(hit.get("evidence_path"), hit.get("evidence_locator"), manifest, f"N3 hit {index}")
        if error:
            return error
        if not isinstance(hit.get("occurrence_count"), int) or hit["occurrence_count"] <= 0:
            return f"N3 hit {index}.occurrence_count must be a positive integer"
        if not isinstance(hit.get("occurrence_group_id"), str) or not re.fullmatch(
            r"[0-9a-f]{16}", hit["occurrence_group_id"]
        ):
            return f"N3 hit {index}.occurrence_group_id must be a 16-hex context digest"
        if not isinstance(hit.get("occurrence_locator_sha256"), str) or not re.fullmatch(
            r"[0-9a-f]{64}", hit["occurrence_locator_sha256"]
        ):
            return f"N3 hit {index}.occurrence_locator_sha256 must be a SHA-256 digest"
        hit_key = (
            str(hit["evidence_path"]), _norm(hit["phrase"]),
            hit["occurrence_group_id"],
        )
        if hit_key in observed_hits:
            return f"N3 hit {index} duplicates a path/phrase occurrence disposition"
        observed_hits[hit_key] = {
            "occurrence_group_id": hit["occurrence_group_id"],
            "occurrence_count": hit["occurrence_count"],
            "occurrence_locator_sha256": hit["occurrence_locator_sha256"],
            "evidence_locator": hit["evidence_locator"],
        }
        if manifest is not None and not _entry_contains(
            manifest[hit["evidence_path"]], hit["phrase"]
        ):
            return f"N3 hit {index}.phrase is not evidenced at evidence_path"
        if manifest is not None and classification == "retained_authority":
            entry = manifest[hit["evidence_path"]]
            roles = set(entry.get("roles") or [])
            supported = (
                entry.get("effective_status") in RETAINED_GRADE
                or entry.get("accepted_premise_type") in PRIOR_AUTHORITY_PREMISE_TYPES
            )
            if not roles.intersection({"authority", "framework_premise", "premise_registry"}) or not supported:
                return f"N3 retained_authority hit {index} is not retained or accepted in the manifest"
        if classification == "hidden_admission":
            if not _text(hit.get("promoted_wall")) or _norm(hit["promoted_wall"]) not in walls:
                return f"N3 hidden admission {index} must be promoted into N2.walls"
    if manifest is not None:
        required_hits = required_phrase_groups(
            manifest, {"source", "authority"}, N3_SCAN_PHRASES
        )
        if set(observed_hits) != set(required_hits):
            missing = sorted(set(required_hits) - set(observed_hits))
            extra = sorted(set(observed_hits) - set(required_hits))
            return f"N3.hits must exactly disposition orchestrator phrase scan; missing={missing}, extra={extra}"
        for hit_key, observed in observed_hits.items():
            if observed != required_hits[hit_key]:
                return f"N3 hit {hit_key} must match its authenticated occurrence group"
    return _unresolved_error(section, "N3", status)


def _validate_n4(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N4_residual_matching")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "scanned_evidence_paths", "witnesses", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N4",
    )
    if error:
        return error
    error = _scan_coverage_error(section, manifest, {"authority"}, "N4")
    if error:
        return error
    if not _text(section.get("scan_scope")):
        return "N4.scan_scope must name the witness/residual surfaces checked"
    witnesses = section.get("witnesses")
    if not _list(witnesses):
        return "N4.witnesses must be a list"
    error = _none_found_error(section, witnesses, "N4")
    if error:
        return error
    witness_ids: set[str] = set()
    witness_routes: dict[str, str] = {}
    for index, witness in enumerate(witnesses, 1):
        if not isinstance(witness, dict):
            return f"N4 witness {index} must be an object"
        error = _unknown_fields(
            witness,
            {"witness_id", "route_id", "witness_residual", "claim_residual", "match", "evidence_path", "evidence_locator"},
            f"N4 witness {index}",
        )
        if error:
            return error
        for field in ("witness_id", "route_id", "witness_residual", "claim_residual"):
            if not _text(witness.get(field)):
                return f"N4 witness {index}.{field} must be non-empty"
        witness_id = _norm(witness["witness_id"])
        route_id = _norm(witness["route_id"])
        if witness_id in witness_ids:
            return f"N4 witness_id {witness['witness_id']!r} is duplicated"
        route_ids = {_norm(route.get("route_id") or "") for route in packet.get("N1_alternative_routes") or []}
        if route_id not in route_ids:
            return f"N4 witness {index}.route_id does not name an N1 route"
        if not isinstance(witness.get("match"), bool):
            return f"N4 witness {index}.match must be boolean"
        error = _locator_error(witness.get("evidence_path"), witness.get("evidence_locator"), manifest, f"N4 witness {index}")
        if error:
            return error
        if manifest is not None:
            if not _entry_contains(manifest[witness["evidence_path"]], witness["witness_residual"]):
                return f"N4 witness {index}.witness_residual is not evidenced at its path"
            source_entries = [
                entry for entry in manifest.values()
                if "source" in set(entry.get("roles") or [])
            ]
            if not any(_entry_contains(entry, witness["claim_residual"]) for entry in source_entries):
                return f"N4 witness {index}.claim_residual is not evidenced in the source"
        expected_match = _norm(witness["witness_residual"]) == _norm(witness["claim_residual"])
        if witness["match"] != expected_match:
            return f"N4 witness {index}.match is inconsistent with the residual comparison"
        if status == "PASS" and not witness["match"]:
            return f"No-Go Discipline PASS cannot retain mismatched N4 witness {index}"
        witness_ids.add(witness_id)
        witness_routes[witness_id] = route_id
    for index, route in enumerate(packet.get("N1_alternative_routes") or [], 1):
        if str(route.get("honesty_marker") or "").strip().upper() != "RULED OUT BY PRIOR":
            continue
        witness_id = _norm(str(route.get("prior_witness_id") or ""))
        if witness_id not in witness_routes:
            return f"N1 route {index} prior_witness_id does not name an N4 witness"
        if witness_routes[witness_id] != _norm(str(route.get("route_id") or "")):
            return f"N1 route {index} prior_witness_id is linked to a different route"
        witness = next(
            item for item in witnesses
            if _norm(str(item.get("witness_id") or "")) == witness_id
        )
        if witness.get("evidence_path") != route.get("evidence_path"):
            return f"N1 route {index} prior witness must bind the same authority path"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N4 scan")
    return error or _unresolved_error(section, "N4", status)


def _validate_n5(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N5_rhetoric_audit")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "scanned_evidence_paths", "statements", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N5",
    )
    if error:
        return error
    error = _scan_coverage_error(section, manifest, {"source"}, "N5")
    if error:
        return error
    if not _text(section.get("scan_scope")):
        return "N5.scan_scope must name the negative rhetoric checked"
    statements = section.get("statements")
    if not _list(statements):
        return "N5.statements must be a list"
    error = _none_found_error(section, statements, "N5")
    if error:
        return error
    observed_statements: dict[tuple[str, str, str], dict[str, Any]] = {}
    for index, statement in enumerate(statements, 1):
        if not isinstance(statement, dict) or not _text(statement.get("phrase")):
            return f"N5 statement {index} must name a phrase"
        error = _unknown_fields(
            statement,
            {
                "phrase", "occurrence_group_id", "occurrence_count",
                "occurrence_locator_sha256",
                "resolution_classes_checked",
                "tested_resolutions", "untested_resolutions", "evidence_path",
                "evidence_locator", "resolution_evidence_path",
                "resolution_evidence_locator",
            },
            f"N5 statement {index}",
        )
        if error:
            return error
        if not _list(statement.get("tested_resolutions")) or not all(_text(x) for x in statement["tested_resolutions"]):
            return f"N5 statement {index}.tested_resolutions must be non-empty"
        classes = statement.get("resolution_classes_checked")
        if (
            not isinstance(classes, list)
            or not all(_text(item) for item in classes)
            or set(classes) != N5_RESOLUTION_CLASSES
        ):
            return (
                f"N5 statement {index}.resolution_classes_checked must equal "
                f"{sorted(N5_RESOLUTION_CLASSES)}"
            )
        if len(statement["tested_resolutions"]) != len(N5_RESOLUTION_CLASSES):
            return f"N5 statement {index} must record one tested resolution per required class"
        for resolution_class in N5_RESOLUTION_CLASSES:
            if not any(
                _norm(resolution).startswith(_norm(resolution_class))
                and len(_norm(resolution)) >= 40
                for resolution in statement["tested_resolutions"]
            ):
                return f"N5 statement {index} lacks a substantive {resolution_class} tested resolution"
        if not _list(statement.get("untested_resolutions")) or not all(_text(x) for x in statement["untested_resolutions"]):
            return f"N5 statement {index}.untested_resolutions must be a list of non-empty strings"
        error = _locator_error(statement.get("evidence_path"), statement.get("evidence_locator"), manifest, f"N5 statement {index}")
        if error:
            return error
        error = _locator_error(
            statement.get("resolution_evidence_path"),
            statement.get("resolution_evidence_locator"), manifest,
            f"N5 statement {index} resolution test",
        )
        if error:
            return error
        if manifest is not None:
            resolution_entry = manifest[statement["resolution_evidence_path"]]
            if "runner_stdout" not in set(resolution_entry.get("roles") or []):
                return f"N5 statement {index} resolution tests must cite current-cycle execution evidence"
            for resolution in statement["tested_resolutions"]:
                if not _entry_contains(resolution_entry, resolution):
                    return f"N5 statement {index} tested resolution is not evidenced at resolution_evidence_path"
        if not isinstance(statement.get("occurrence_count"), int) or statement["occurrence_count"] <= 0:
            return f"N5 statement {index}.occurrence_count must be a positive integer"
        if not isinstance(statement.get("occurrence_locator_sha256"), str) or not re.fullmatch(
            r"[0-9a-f]{64}", statement["occurrence_locator_sha256"]
        ):
            return f"N5 statement {index}.occurrence_locator_sha256 must be a SHA-256 digest"
        if not isinstance(statement.get("occurrence_group_id"), str) or not re.fullmatch(
            r"[0-9a-f]{16}", statement["occurrence_group_id"]
        ):
            return f"N5 statement {index}.occurrence_group_id must be a 16-hex context digest"
        statement_key = (
            str(statement["evidence_path"]), _norm(statement["phrase"]),
            statement["occurrence_group_id"],
        )
        if statement_key in observed_statements:
            return f"N5 statement {index} duplicates a path/phrase disposition"
        observed_statements[statement_key] = {
            "occurrence_group_id": statement["occurrence_group_id"],
            "occurrence_count": statement["occurrence_count"],
            "occurrence_locator_sha256": statement["occurrence_locator_sha256"],
            "evidence_locator": statement["evidence_locator"],
        }
        if manifest is not None and not _entry_contains(
            manifest[statement["evidence_path"]], statement["phrase"]
        ):
            return f"N5 statement {index}.phrase is not evidenced at evidence_path"
        if status == "PASS" and statement["untested_resolutions"]:
            return f"No-Go Discipline PASS cannot retain untested N5 resolutions for statement {index}"
    if manifest is not None:
        required_statements = required_phrase_groups(
            manifest, {"source"}, N5_SCAN_PHRASES
        )
        if set(observed_statements) != set(required_statements):
            missing = sorted(set(required_statements) - set(observed_statements))
            extra = sorted(set(observed_statements) - set(required_statements))
            return f"N5.statements must exactly disposition orchestrator rhetoric scan; missing={missing}, extra={extra}"
        for statement_key, observed in observed_statements.items():
            if observed != required_statements[statement_key]:
                return f"N5 statement {statement_key} must match its authenticated occurrence group"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N5 scan")
    return error or _unresolved_error(section, "N5", status)


def _validate_n6(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N6_partial_closure_scan")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "premise_classes_checked", "candidates", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N6",
    )
    if error:
        return error
    error = _locator_error(
        section.get("evidence_path"),
        section.get("evidence_locator"),
        manifest,
        "N6 scan",
    )
    if error:
        return error
    indexed_candidates: dict[str, dict[str, Any]] | None = None
    if manifest is not None:
        index_entry = manifest.get(section.get("evidence_path"))
        if not index_entry or "partial_closure_index" not in set(index_entry.get("roles") or []):
            return "N6 must cite the orchestrator-owned partial_closure_index surface"
        indexed_candidates = _partial_closure_candidates(index_entry)
        if indexed_candidates is None:
            return "N6 partial-closure index is malformed or not orchestrator-authenticated"
    if not _text(section.get("scan_scope")):
        return "N6.scan_scope must name the primitive/reframe surfaces checked"
    checked = section.get("premise_classes_checked")
    if (
        not _list(checked)
        or not all(_text(item) for item in checked)
    ):
        return f"N6.premise_classes_checked must equal {sorted(PREMISE_CLASSES_CHECKED)}"
    checked_set = set(checked)
    if checked_set not in (PREMISE_CLASSES_CHECKED, LEGACY_PREMISE_CLASSES_CHECKED):
        return f"N6.premise_classes_checked must equal {sorted(PREMISE_CLASSES_CHECKED)}"
    candidates = section.get("candidates")
    if not _list(candidates):
        return "N6.candidates must be a list"
    error = _none_found_error(section, candidates, "N6")
    if error:
        return error
    allowed_kinds = {"approved_primitive", "open_gate", "convention_reframe", "definition_refactor"}
    if checked_set == LEGACY_PREMISE_CLASSES_CHECKED:
        allowed_kinds.add("owner_governed")
    seen_candidate_ids: set[str] = set()
    for index, candidate in enumerate(candidates, 1):
        if (
            not isinstance(candidate, dict)
            or not isinstance(candidate.get("kind"), str)
            or candidate.get("kind") not in allowed_kinds
        ):
            return f"N6 candidate {index}.kind is invalid"
        error = _unknown_fields(
            candidate,
            {
                "candidate_id", "kind", "indexed_basis", "affected_wall", "closure_mechanism",
                "could_close_wall", "addressed", "disposition",
                "evidence_path", "evidence_locator",
            },
            f"N6 candidate {index}",
        )
        if error:
            return error
        if not _text(candidate.get("candidate_id")):
            return f"N6 candidate {index}.candidate_id must be non-empty"
        candidate_id = str(candidate["candidate_id"])
        if candidate_id in seen_candidate_ids:
            return f"N6 candidate {index}.candidate_id is duplicated"
        indexed = indexed_candidates.get(candidate_id) if indexed_candidates is not None else None
        if indexed_candidates is not None and indexed is None:
            return f"N6 candidate {index}.candidate_id is absent from the partial-closure index"
        if indexed and indexed.get("kind") and candidate.get("kind") != indexed.get("kind"):
            return f"N6 candidate {index}.kind does not match the partial-closure index"
        if not _text(candidate.get("indexed_basis")) or len(_norm(candidate["indexed_basis"])) < 20:
            return f"N6 candidate {index}.indexed_basis must quote substantive indexed content"
        if indexed is not None and _norm(candidate["indexed_basis"]) not in _norm(
            json.dumps(indexed, sort_keys=True)
        ):
            return f"N6 candidate {index}.indexed_basis is not present in its indexed candidate"
        for field in ("could_close_wall", "addressed"):
            if not isinstance(candidate.get(field), bool):
                return f"N6 candidate {index}.{field} must be boolean"
        if not _text(candidate.get("disposition")):
            return f"N6 candidate {index}.disposition must be non-empty"
        if not _text(candidate.get("affected_wall")):
            return f"N6 candidate {index}.affected_wall must name an N2 wall"
        walls = {
            _norm(wall)
            for wall in packet.get("N2_wall_independence", {}).get("walls") or []
        }
        if _norm(candidate["affected_wall"]) not in walls:
            return f"N6 candidate {index}.affected_wall does not name an N2 wall"
        if (
            not _text(candidate.get("closure_mechanism"))
            or len(_norm(candidate["closure_mechanism"])) < 40
        ):
            return f"N6 candidate {index}.closure_mechanism must explain the partial-closure test"
        if _norm(candidate["indexed_basis"]) not in _norm(candidate["closure_mechanism"]):
            return f"N6 candidate {index}.closure_mechanism must use its indexed_basis"
        if _norm(candidate["affected_wall"]) not in _norm(candidate["disposition"]):
            return f"N6 candidate {index}.disposition must name its affected_wall"
        error = _locator_error(candidate.get("evidence_path"), candidate.get("evidence_locator"), manifest, f"N6 candidate {index}")
        if error:
            return error
        if manifest is not None:
            entry = manifest[candidate["evidence_path"]]
            if "partial_closure_index" in set(entry.get("roles") or []):
                seen_candidate_ids.add(candidate_id)
                if status == "PASS" and candidate["could_close_wall"] and not candidate["addressed"]:
                    return f"No-Go Discipline PASS leaves N6 candidate {index} unaddressed"
                continue
            expected_type = {
                "approved_primitive": "axiom_or_approved_primitive",
                "convention_reframe": "convention_not_accepted",
            }.get(candidate["kind"])
            if expected_type and entry.get("accepted_premise_type") != expected_type:
                return (
                    f"N6 candidate {index} kind={candidate['kind']!r} does not "
                    f"match manifest premise type {entry.get('accepted_premise_type')!r}"
                )
            if candidate["kind"] == "definition_refactor" and not set(entry.get("roles") or []).intersection(
                {"source", "authority", "runner", "helper"}
            ):
                return f"N6 definition_refactor candidate {index} must cite a source or code surface"
        if status == "PASS" and candidate["could_close_wall"] and not candidate["addressed"]:
            return f"No-Go Discipline PASS leaves N6 candidate {index} unaddressed"
        seen_candidate_ids.add(candidate_id)
    if indexed_candidates is not None and seen_candidate_ids != set(indexed_candidates):
        missing = sorted(set(indexed_candidates) - seen_candidate_ids)
        return f"N6.candidates must disposition every partial-closure candidate; missing {missing[:3]}"
    return _unresolved_error(section, "N6", status)


def _validate_n7(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N7_steelman")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {
            "route_id", "argument", "resolution", "resolved", "evidence_path",
            "evidence_locator", "resolution_evidence_path",
            "resolution_evidence_locator",
        },
        "N7",
    )
    if error:
        return error
    if not _text(section.get("route_id")) or not _text(section.get("argument")) or not _text(section.get("resolution")):
        return "N7.route_id, N7.argument, and N7.resolution must be non-empty"
    if not isinstance(section.get("resolved"), bool):
        return "N7.resolved must be boolean"
    if len(_norm(section["argument"])) < 80 or len(_norm(section["resolution"])) < 80:
        return "N7.argument and N7.resolution must each contain at least 80 normalized characters"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N7")
    if error:
        return error
    error = _locator_error(
        section.get("resolution_evidence_path"),
        section.get("resolution_evidence_locator"), manifest,
        "N7 independent resolution",
    )
    if error:
        return error
    routes = {
        _norm(str(route.get("route_id") or "")): route
        for route in packet.get("N1_alternative_routes") or []
    }
    steelman_route = routes.get(_norm(section["route_id"]))
    if not steelman_route:
        return "N7.route_id must name an evidenced N1 route"
    if section.get("evidence_path") != steelman_route.get("evidence_path"):
        return "N7 must cite the same evidence_path as its steelmanned N1 route"
    if section.get("resolution_evidence_path") == section.get("evidence_path"):
        return "N7 independent resolution must cite a different packet surface from its N1 route"
    if manifest is not None:
        argument_entry = manifest.get(section["evidence_path"])
        if argument_entry is None or not _entry_contains(
            argument_entry, section["argument"]
        ):
            return "N7.argument is not evidenced at its N1 execution path"
        resolution_entry = manifest.get(section["resolution_evidence_path"])
        if resolution_entry is None:
            return "N7 independent resolution evidence is absent"
        resolution_roles = set(resolution_entry.get("roles") or [])
        accepted_authority = (
            resolution_roles.intersection(
                {"authority", "framework_premise", "premise_registry"}
            )
            and (
                resolution_entry.get("effective_status") in RETAINED_GRADE
                or resolution_entry.get("accepted_premise_type")
                in PRIOR_AUTHORITY_PREMISE_TYPES
            )
            and isinstance(resolution_entry.get("full_content_sha256"), str)
        )
        independent_execution = "runner_stdout_independent" in resolution_roles
        if not (accepted_authority or independent_execution):
            return (
                "N7 independent resolution must cite authenticated independent "
                "execution or retained/accepted authority"
            )
        if not _entry_contains(resolution_entry, section["resolution"]):
            return "N7.resolution is not evidenced at resolution_evidence_path"
    if _norm(str(steelman_route.get("mechanism") or "")) not in _norm(section["argument"]):
        return "N7.argument must name the steelmanned route mechanism"
    if _norm(str(steelman_route.get("attempt") or "")) not in _norm(section["argument"]):
        return "N7.argument must name the steelmanned route attempt"
    walls = packet.get("N2_wall_independence", {}).get("walls") or []
    if not any(_norm(wall) in _norm(section["resolution"]) for wall in walls):
        return "N7.resolution must name at least one evidenced N2 wall"
    if status == "PASS" and str(steelman_route.get("disposition") or "").upper() != "CLOSED":
        return "No-Go Discipline PASS requires the N7 steelman route to be CLOSED"
    if status == "PASS" and not section["resolved"]:
        return "No-Go Discipline PASS requires the N7 steelman to be resolved"
    return None


def _validate_n8(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N8_cross_cycle_echo")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {
            "packet_complete", "echoes", "none_found_reason", "unresolved",
            "evidence_path", "evidence_locator", "no_go_row_universe_count",
            "no_go_row_universe_sha256",
        },
        "N8",
    )
    if error:
        return error
    error = _locator_error(
        section.get("evidence_path"),
        section.get("evidence_locator"),
        manifest,
        "N8 search",
    )
    if error:
        return error
    candidate_ids: set[str] | None = None
    candidate_records: dict[str, dict[str, Any]] | None = None
    if manifest is not None:
        entry = manifest.get(section.get("evidence_path"))
        if not entry:
            return "N8 evidence path is outside the restricted packet"
        if "cross_cycle_index" not in set(entry.get("roles") or []):
            return "N8 must cite the orchestrator-owned cross_cycle_index surface"
        candidate_records = _index_candidates(
            entry, schema="no_go_cross_cycle_index_v1",
            stored_field="cross_cycle_candidate_ids",
            stored_records_field="cross_cycle_candidates",
        )
        candidate_ids = set(candidate_records) if candidate_records is not None else None
        if candidate_records is None:
            return "N8 cross-cycle index is malformed or not orchestrator-authenticated"
        universe = _cross_cycle_no_go_universe(entry)
        if universe is None:
            return "N8 cross-cycle index lacks the complete no-go row universe digest"
        universe_count, universe_sha256 = universe
        if section.get("no_go_row_universe_count") != universe_count:
            return "N8.no_go_row_universe_count contradicts the authenticated index"
        if section.get("no_go_row_universe_sha256") != universe_sha256:
            return "N8.no_go_row_universe_sha256 contradicts the authenticated index"
    if not isinstance(section.get("packet_complete"), bool):
        return "N8.packet_complete must be boolean"
    echoes = section.get("echoes")
    if not _list(echoes):
        return "N8.echoes must be a list"
    error = _none_found_error(section, echoes, "N8")
    if error:
        return error
    seen_candidate_ids: set[str] = set()
    for index, echo in enumerate(echoes, 1):
        if not isinstance(echo, dict) or not _text(echo.get("candidate_id")) or not _text(echo.get("mechanism")):
            return f"N8 echo {index} must name candidate_id and mechanism"
        mechanism_tokens = re.findall(r"[a-z0-9_]+", _norm(echo["mechanism"]))
        if len(_norm(echo["mechanism"])) < 24 or len(mechanism_tokens) < 3:
            return f"N8 echo {index}.mechanism must identify a substantive indexed mechanism"
        error = _unknown_fields(
            echo,
            {
                "candidate_id", "mechanism", "retired", "applicable",
                "addressed", "disposition", "evidence_path", "evidence_locator",
            },
            f"N8 echo {index}",
        )
        if error:
            return error
        candidate_id = str(echo["candidate_id"])
        if candidate_id in seen_candidate_ids:
            return f"N8 echo {index}.candidate_id is duplicated"
        if candidate_ids is not None and candidate_id not in candidate_ids:
            return f"N8 echo {index}.candidate_id is absent from the cross-cycle index"
        if not isinstance(echo.get("addressed"), bool):
            return f"N8 echo {index}.addressed must be boolean"
        if not _text(echo.get("disposition")) or len(_norm(echo["disposition"])) < 40:
            return f"N8 echo {index}.disposition must explain the applicability decision"
        if _norm(echo["mechanism"]) not in _norm(echo["disposition"]):
            return f"N8 echo {index}.disposition must name its indexed mechanism"
        if candidate_records is not None:
            candidate_record = candidate_records[candidate_id]
            candidate_text = json.dumps(candidate_record, sort_keys=True)
            if _norm(echo["mechanism"]) not in _norm(candidate_text):
                return f"N8 echo {index}.mechanism is not evidenced in its indexed candidate"
            lifecycle = candidate_record.get("lifecycle_state")
            if lifecycle not in {"active", "retired", "unknown"}:
                return f"N8 indexed candidate {candidate_id!r} lacks valid lifecycle_state"
            if lifecycle == "unknown":
                if echo.get("retired") is not None:
                    return (
                        f"N8 echo {index} must preserve unknown retirement as null "
                        "until an authenticated registry/history record decides it"
                    )
            else:
                if not isinstance(candidate_record.get("retired"), bool):
                    return f"N8 indexed candidate {candidate_id!r} lacks orchestrator retired state"
                if not isinstance(echo.get("retired"), bool):
                    return f"N8 echo {index}.retired must be boolean for known lifecycle"
                if echo["retired"] != candidate_record["retired"]:
                    return f"N8 echo {index}.retired contradicts its indexed candidate"
            if status == "PASS" and not isinstance(echo.get("applicable"), bool):
                return (
                    f"No-Go Discipline PASS requires N8 echo {index}.applicable "
                    "to be decided independently of lifecycle"
                )
            if isinstance(candidate_record.get("addressed"), bool) and echo["addressed"] != candidate_record["addressed"]:
                return f"N8 echo {index}.addressed contradicts its indexed candidate"
        error = _locator_error(echo.get("evidence_path"), echo.get("evidence_locator"), manifest, f"N8 echo {index}")
        if error:
            return error
        if status == "PASS" and echo.get("applicable") is True and not echo["addressed"]:
            return f"No-Go Discipline PASS leaves applicable N8 echo {index} unaddressed"
        if status == "PASS" and not echo["addressed"]:
            return f"No-Go Discipline PASS leaves N8 echo {index} unaddressed"
        seen_candidate_ids.add(candidate_id)
    if candidate_ids is not None and seen_candidate_ids != candidate_ids:
        missing = sorted(candidate_ids - seen_candidate_ids)
        return f"N8.echoes must disposition every cross-cycle candidate; missing {missing[:3]}"
    if status == "PASS" and not section["packet_complete"]:
        return "No-Go Discipline PASS requires packet_complete=true for N8"
    return _unresolved_error(section, "N8", status)


def validate_no_go_discipline(
    audit: dict[str, Any],
    *,
    source_required: bool = False,
    evidence_manifest: dict[str, dict] | None = None,
    prior_claim_scope: str | None = None,
) -> str | None:
    required = source_required or output_requires_no_go_discipline(audit)
    packet = audit.get("no_go_discipline")
    if not required:
        if packet is None:
            return None
        if not isinstance(packet, dict):
            return "no_go_discipline must be an object or null"
    elif not isinstance(packet, dict):
        return "No-Go Discipline N1-N8 packet is required for this audit"
    if packet is None:
        return None
    if evidence_manifest is None:
        evidence_manifest = evidence_manifest_from_snapshot(packet)
    error = _unknown_fields(
        packet,
        {
            "required", "status", "N1_alternative_routes", "N2_wall_independence",
            "N3_hidden_wall_scan", "N4_residual_matching", "N5_rhetoric_audit",
            "N6_partial_closure_scan", "N7_steelman", "N8_cross_cycle_echo",
            "failures", "demotion", "prior_claim_scope", "narrowed_claim_scope",
            "corrected_wall_set", "next_route", "evidence_snapshot",
        },
        "no_go_discipline",
    )
    if error:
        return error
    if packet.get("required") is not True:
        return "no_go_discipline.required must be true"
    status = packet.get("status")
    if not isinstance(status, str):
        return "no_go_discipline.status must be PASS or FAIL"
    if status not in {"PASS", "FAIL"}:
        return "no_go_discipline.status must be PASS or FAIL"
    if audit.get("verdict") == "audited_clean" and status != "PASS":
        return "audited_clean is forbidden when No-Go Discipline status is not PASS"

    for validator in (_validate_n1, _validate_n2, _validate_n3, _validate_n4, _validate_n5, _validate_n6, _validate_n7, _validate_n8):
        error = validator(packet, status, evidence_manifest)
        if error:
            return error

    failures = packet.get("failures")
    if not _list(failures) or not all(_text(item) for item in failures):
        return "no_go_discipline.failures must be a list of non-empty strings"
    if status == "PASS":
        if failures:
            return "No-Go Discipline PASS cannot carry failure items"
        if audit.get("verdict") == "audited_clean" and audit.get("chain_closes") is not True:
            return "audited_clean with No-Go Discipline PASS requires chain_closes=true"
        if audit.get("verdict") != "audited_clean" and audit.get("chain_closes") is True:
            return "non-clean verdict cannot carry chain_closes=true"
    else:
        if not failures:
            return "No-Go Discipline FAIL requires at least one failure item"
        if not all(re.match(r"^N[1-8]\s*:", failure.strip()) for failure in failures):
            return "No-Go Discipline FAIL failures must identify the failing N1-N8 checks"
        if audit.get("verdict") not in NON_CLEAN_VERDICTS:
            return "No-Go Discipline FAIL requires a conservative non-clean verdict"
        if audit.get("chain_closes") is not False:
            return "No-Go Discipline FAIL requires chain_closes=false"
        if packet.get("demotion") not in DEMOTIONS:
            return f"No-Go Discipline FAIL demotion must be one of {sorted(DEMOTIONS)}"
        if not _text(packet.get("narrowed_claim_scope")):
            return "No-Go Discipline FAIL requires narrowed_claim_scope"
        if packet["narrowed_claim_scope"] != str(audit.get("claim_scope") or ""):
            return "No-Go Discipline FAIL narrowed_claim_scope must equal the applied claim_scope"
        if not _text(packet.get("prior_claim_scope")):
            return "No-Go Discipline FAIL requires prior_claim_scope"
        if prior_claim_scope is None:
            return "No-Go Discipline FAIL requires an authentic pre-audit ledger scope"
        if packet["prior_claim_scope"] != prior_claim_scope:
            return "No-Go Discipline FAIL prior_claim_scope must equal the pre-audit ledger scope"
        if _norm(packet["prior_claim_scope"]) == _norm(packet["narrowed_claim_scope"]):
            return "No-Go Discipline FAIL must actually narrow the pre-audit claim scope"
        prior_tokens = _scope_tokens(packet["prior_claim_scope"])
        narrowed_tokens = _scope_tokens(packet["narrowed_claim_scope"])
        if not narrowed_tokens or not narrowed_tokens < prior_tokens:
            return (
                "No-Go Discipline FAIL narrowed_claim_scope must be a strict lexical "
                "subset of prior_claim_scope"
            )
        if (
            prior_tokens.intersection(LOGICAL_SCOPE_TOKENS)
            != narrowed_tokens.intersection(LOGICAL_SCOPE_TOKENS)
        ):
            return (
                "No-Go Discipline FAIL narrowing must preserve logical polarity "
                "tokens such as no/not/without/only/all"
            )
        if not _list(packet.get("corrected_wall_set")) or not all(_text(x) for x in packet["corrected_wall_set"]):
            return "No-Go Discipline FAIL corrected_wall_set must be a list of non-empty strings"
        collapsed = packet.get("N2_wall_independence", {}).get("collapsed_wall_set") or []
        if {_norm(x) for x in packet["corrected_wall_set"]} != {_norm(x) for x in collapsed}:
            return "No-Go Discipline FAIL corrected_wall_set must equal N2.collapsed_wall_set"
        next_route = packet.get("next_route")
        if not isinstance(next_route, dict):
            return "No-Go Discipline FAIL next_route must be an object"
        error = _unknown_fields(next_route, {"route_id", "reason_untested"}, "next_route")
        if error:
            return error
        if not _text(next_route.get("route_id")) or not _text(next_route.get("reason_untested")):
            return "No-Go Discipline FAIL next_route requires route_id and reason_untested"
        routes = {
            _norm(str(route.get("route_id") or "")): route
            for route in packet.get("N1_alternative_routes") or []
        }
        queued = routes.get(_norm(next_route["route_id"]))
        if not queued or str(queued.get("disposition") or "").upper() not in {"OPEN", "UNTESTED"}:
            return "No-Go Discipline FAIL next_route must identify an OPEN or UNTESTED N1 route"

    return None
