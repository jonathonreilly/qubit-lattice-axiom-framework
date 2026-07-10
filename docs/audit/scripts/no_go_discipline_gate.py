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
    "owner_governed_residual",
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

PATH_TRIGGER_RE = re.compile(r"(?:^|[\s/._-])(no[\s_-]?go|obstruction|stretch[\s_-]?attempt)(?:$|[\s/._-])", re.IGNORECASE)
NEGATIVE_ASSERTION_RE = re.compile(
    r"structurally (?:closed|undecidable)|no route exists|"
    r"no retained primitive(?: supplies)?|requires? (?:a )?new axiom|"
    r"cannot be derived from|does not lift|cannot lift|"
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
    r"bounded with named walls|conditional on [^\n]{0,120}\b(?:walls?|admissions?)\b|"
    r"\b(?:residual|named|independent|unclosed|remaining|unresolved) (?:walls?|admissions?)\b|"
    r"\b(?:scoped|structural|bounded|remaining|unresolved) obstruction\b|"
    r"\bobstruction (?:to|rules out|blocks|precludes|prevents)\b|"
    r"\b(?:route|attempt|construction)\b[^\n]{0,80}\bdoes not close\b|"
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
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if)\b)[\w-]+\s+){0,8}"
    r"(?:routes?|arguments?|candidates?|shells?|constructions?|attempts?|inputs?|"
    r"primitives?|theorems?|methods?|maps?|carriers?|actions?|identities?)|"
    r"none\s+of\s+(?:the\s+)?"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if)\b)[\w-]+\s+){0,8}"
    r"(?:routes?|arguments?|candidates?|shells?|constructions?|attempts?|inputs?|"
    r"primitives?|theorems?|methods?|maps?|carriers?|actions?|identities?)|nothing)\s+"
    r"(?:(?:can\s+|is\s+able\s+to\s+|are\s+able\s+to\s+)?"
    r"(?:close[sd]?|remove[sd]?|resolve[sd]?|discharge[sd]?|suppl(?:y|ies|ied)|"
    r"derive[sd]?|select[sd]?|determine[sd]?|fix(?:es|ed)?|retire[sd]?|"
    r"eliminate[sd]?)|succeeds?\s+in\s+"
    r"(?:closing|removing|resolving|discharging|supplying|deriving|selecting|"
    r"determining|fixing|retiring|eliminating))\b",
    re.IGNORECASE,
)
NO_EXISTENCE_ASSERTION_RE = re.compile(
    r"\bno\s+"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if)\b)[\w-]+\s+){0,8}"
    r"(?:routes?|[\w-]*factorizations?|maps?|carriers?|solutions?|constructions?|"
    r"methods?|operators?|primitives?|theorems?)\s+exists\b",
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
OUTPUT_BOUNDARY_FIELDS = (
    "claim_scope",
    "load_bearing_step",
    "chain_closure_explanation",
    "verdict_rationale",
)

AXIOM_REGISTRY = "docs/audit/data/axiom_premise_nodes.json"
OWNER_REGISTRY = "docs/audit/data/owner_governed_premise_nodes.json"
TIER_A_REGISTRY = "docs/audit/data/tier_a_admissions.json"
CONTROLLED_VOCABULARY = "docs/repo/controlled_vocabulary.yaml"
ACTIVE_REVIEW_QUEUE = "docs/repo/ACTIVE_REVIEW_QUEUE.md"
PREMISE_CLASSES_CHECKED = {
    "axiom_or_approved_primitive",
    "owner_governed_residual",
    "tier_a_derivation_target",
    "tier_a_convention_not_accepted",
    "definition_or_scope_reframe",
}


def _read_text(repo_root: Path, path: str | None) -> str:
    if not path:
        return ""
    try:
        return (repo_root / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


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
    owners = _load_json(repo_root, OWNER_REGISTRY)
    if claim_id in set(owners.get("canonical_ids") or []):
        return "owner_governed_residual"
    tier_a = _load_json(repo_root, TIER_A_REGISTRY)
    if claim_id in set((tier_a.get("derivation_targets") or {}).keys()):
        return "tier_a_derivation_target"
    if claim_id in set((tier_a.get("conventions") or {}).keys()):
        return "tier_a_convention_not_accepted"
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
    return _search_terms(
        " ".join(
            str(row.get(field) or "")
            for field in ("claim_id", "claim_scope", "verdict_rationale", "note_path")
        )
    )


def build_cross_cycle_index(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> str:
    """Render the orchestrator-owned N8 search surface supplied to the auditor."""
    candidates: list[dict[str, Any]] = []
    cid = str(row.get("claim_id") or "")

    def add_history(source_id: str, history: list[Any]) -> None:
        for index, archived in enumerate(history):
            if not isinstance(archived, dict):
                continue
            candidates.append(
                {
                    "candidate_id": f"{source_id}:previous_audit:{index}",
                    "kind": "prior_audit_cycle",
                    "source_claim_id": source_id,
                    "audit_status": archived.get("audit_status"),
                    "claim_type": archived.get("claim_type"),
                    "claim_scope": archived.get("claim_scope"),
                    "verdict_rationale": archived.get("verdict_rationale"),
                    "invalidation_reason": archived.get("invalidation_reason"),
                }
            )

    add_history(cid, list(row.get("previous_audits") or []))
    for dep_id in row.get("deps") or []:
        add_history(dep_id, list(ledger_rows.get(dep_id, {}).get("previous_audits") or []))

    root = Path(repo_root)
    tier_a = _load_json(root, TIER_A_REGISTRY)
    for retired_id, record in sorted((tier_a.get("retired_derivation_targets") or {}).items()):
        candidates.append(
            {
                "candidate_id": f"tier_a_retirement:{retired_id}",
                "kind": "tier_a_retirement",
                "source_claim_id": retired_id,
                "record": record,
            }
        )
    owners = _load_json(root, OWNER_REGISTRY)
    for owner_id, record in sorted((owners.get("nodes") or {}).items()):
        candidates.append(
            {
                "candidate_id": f"owner_governed_retirement:{owner_id}",
                "kind": "owner_governed_retirement",
                "source_claim_id": owner_id,
                "record": record,
            }
        )

    current_terms = _row_search_terms(row)

    loop_ledger_glob = ".claude/science/physics-loops/**/NO_GO_LEDGER.md"
    loop_ledger_paths = sorted(root.glob(loop_ledger_glob))
    for ledger_path in loop_ledger_paths:
        try:
            ledger_text = ledger_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            ledger_text = f"[could not read loop no-go ledger: {exc}]"
        relative_path = ledger_path.relative_to(root).as_posix()
        candidates.append(
            {
                "candidate_id": f"physics_loop_no_go_ledger:{relative_path}",
                "kind": "physics_loop_no_go_ledger",
                "source_claim_id": relative_path,
                "note_path": relative_path,
                "content_sha256": hashlib.sha256(ledger_text.encode("utf-8")).hexdigest(),
                "content": ledger_text,
                "content_truncated": False,
                "matching_terms": sorted(current_terms.intersection(_search_terms(ledger_text))),
            }
        )

    similar: list[tuple[int, str, dict[str, Any], list[str]]] = []
    for other_id, other in ledger_rows.items():
        if other_id == cid or other.get("claim_type") != "no_go":
            continue
        other_text = " ".join(
            str(other.get(field) or "")
            for field in ("claim_id", "claim_scope", "verdict_rationale", "note_path")
        )
        overlap = sorted(current_terms.intersection(_search_terms(other_text)))
        if len(overlap) < 2:
            continue
        similar.append((len(overlap), other_id, other, overlap))
    for _score, other_id, other, overlap in sorted(
        similar, key=lambda item: (-item[0], item[1])
    )[:25]:
        candidates.append(
            {
                "candidate_id": f"similar_negative_boundary:{other_id}",
                "kind": "similar_negative_boundary",
                "source_claim_id": other_id,
                "note_path": other.get("note_path"),
                "audit_status": other.get("audit_status"),
                "effective_status": other.get("effective_status"),
                "claim_scope": other.get("claim_scope"),
                "verdict_rationale": other.get("verdict_rationale"),
                "matching_terms": overlap,
            }
        )
    return json.dumps(
        {
            "schema": "no_go_cross_cycle_index_v1",
            "claim_id": cid,
            "search_scope": {
                "current_row_audit_history": True,
                "one_hop_authority_audit_history": True,
                "tier_a_retirements": True,
                "owner_governed_retirements": True,
                "similar_no_go_rows": {
                    "source": "audit ledger rows with claim_type=no_go",
                    "minimum_shared_terms": 2,
                    "candidate_limit": 25,
                },
                "physics_loop_no_go_ledgers": {
                    "glob": loop_ledger_glob,
                    "scanned_count": len(loop_ledger_paths),
                    "scanned_paths": [
                        path.relative_to(root).as_posix() for path in loop_ledger_paths
                    ],
                    "candidate_policy": "every tracked ledger is included",
                },
            },
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
    owners = _load_json(root, OWNER_REGISTRY)
    for premise_id in sorted(owners.get("canonical_ids") or []):
        add_candidate(
            candidate_id=f"owner_governed:{premise_id}",
            kind="owner_governed",
            source_path=OWNER_REGISTRY,
            content=(owners.get("nodes") or {}).get(premise_id, {}),
            accepted_premise_type="owner_governed_residual",
        )
    tier_a = _load_json(root, TIER_A_REGISTRY)
    for premise_id, record in sorted((tier_a.get("derivation_targets") or {}).items()):
        add_candidate(
            candidate_id=f"tier_a:{premise_id}",
            kind="tier_a",
            source_path=TIER_A_REGISTRY,
            content=record,
            accepted_premise_type="tier_a_derivation_target",
        )
    for premise_id, record in sorted((tier_a.get("conventions") or {}).items()):
        add_candidate(
            candidate_id=f"convention_reframe:{premise_id}",
            kind="convention_reframe",
            source_path=TIER_A_REGISTRY,
            content=record,
            accepted_premise_type="tier_a_convention_not_accepted",
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
                "premise_registries": [AXIOM_REGISTRY, OWNER_REGISTRY, TIER_A_REGISTRY],
                "controlled_vocabulary": {
                    "path": CONTROLLED_VOCABULARY,
                    "content_sha256": hashlib.sha256(vocabulary_text.encode("utf-8")).hexdigest(),
                    "minimum_shared_terms": 1,
                    "candidate_limit": 10,
                },
                "meta_notes": {
                    "scanned_count": len(meta_paths),
                    "scanned_paths": meta_paths,
                    "minimum_shared_terms": 2,
                    "candidate_limit": 10,
                    "evidence_line_limit_per_candidate": 5,
                },
                "repository_visible_in_flight_reframes": {
                    "queue_path": ACTIVE_REVIEW_QUEUE,
                    "globs": list(reframe_globs),
                    "scanned_count": len(reframe_paths),
                    "scanned_paths": sorted(reframe_paths),
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
        (OWNER_REGISTRY, "owner_governed_residual"),
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
        path=TIER_A_REGISTRY,
        role="premise_registry",
        text=_read_text(root, TIER_A_REGISTRY),
        premise_type="tier_a_registry_mixed_entries",
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


def _index_candidates(
    entry: dict[str, Any], *, schema: str, stored_field: str
) -> dict[str, dict[str, Any]] | None:
    stored = entry.get(stored_field)
    if isinstance(stored, list) and all(_text(item) for item in stored):
        return {str(item): {} for item in stored}
    try:
        parsed = json.loads(str(entry.get("text") or ""))
    except json.JSONDecodeError:
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
    )
    return set(candidates) if candidates is not None else None


def _partial_closure_candidates(
    entry: dict[str, Any],
) -> dict[str, dict[str, Any]] | None:
    return _index_candidates(
        entry,
        schema="no_go_partial_closure_index_v1",
        stored_field="partial_closure_candidate_ids",
    )


def build_evidence_snapshot(
    packet: dict[str, Any], manifest: dict[str, dict]
) -> dict[str, Any]:
    """Persist exact locators authenticated against the rendered packet."""
    grouped: dict[str, set[str]] = {}
    for path, locator in _evidence_references(packet):
        grouped.setdefault(path, set()).add(locator)
    entries: dict[str, dict[str, Any]] = {}
    for path, locators in sorted(grouped.items()):
        entry = manifest.get(path)
        if not entry:
            raise ValueError(f"evidence path {path!r} missing while building snapshot")
        text = str(entry.get("text") or "")
        snapshot_entry: dict[str, Any] = {
            "path": path,
            "roles": list(entry.get("roles") or []),
            "effective_status": entry.get("effective_status"),
            "accepted_premise_type": entry.get("accepted_premise_type"),
            "content_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "verified_locators": sorted(locators),
        }
        if "cross_cycle_index" in set(entry.get("roles") or []):
            candidate_ids = _cross_cycle_candidate_ids(entry)
            if candidate_ids is None:
                raise ValueError("cross-cycle index is not orchestrator-authenticated")
            snapshot_entry["cross_cycle_candidate_ids"] = sorted(candidate_ids)
        if "partial_closure_index" in set(entry.get("roles") or []):
            candidates = _partial_closure_candidates(entry)
            if candidates is None:
                raise ValueError("partial-closure index is not orchestrator-authenticated")
            snapshot_entry["partial_closure_candidate_ids"] = sorted(candidates)
        entries[path] = snapshot_entry
    return {"schema": "no_go_evidence_snapshot_v1", "entries": entries}


def evidence_manifest_from_snapshot(packet: dict[str, Any]) -> dict[str, dict] | None:
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
        manifest[path] = {
            "path": path,
            "roles": list(stored.get("roles") or []),
            "text": "\n".join(locators),
            "effective_status": stored.get("effective_status"),
            "accepted_premise_type": stored.get("accepted_premise_type"),
            "content_sha256": stored.get("content_sha256"),
            "cross_cycle_candidate_ids": stored.get("cross_cycle_candidate_ids"),
            "partial_closure_candidate_ids": stored.get("partial_closure_candidate_ids"),
        }
    return manifest


def _has_negative_boundary_assertion(text: str) -> bool:
    cleaned = NEGATED_NEGATIVE_ASSURANCE_RE.sub("", text)
    if (
        EXPLICIT_NEGATIVE_CLOSURE_RE.search(cleaned)
        or NEGATIVE_SUBJECT_CLOSURE_RE.search(cleaned)
        or NO_EXISTENCE_ASSERTION_RE.search(cleaned)
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
    if _norm(evidence_locator) not in _norm(str(entry.get("text") or "")):
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
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N2")
    if error:
        return error
    walls = section.get("walls")
    collapsed = section.get("collapsed_wall_set")
    checks = section.get("pairwise_checks")
    if not _list(walls) or not all(_text(w) for w in walls) or len({_norm(w) for w in walls}) != len(walls):
        return "N2.walls must be a list of distinct non-empty strings"
    if not _list(collapsed) or not all(_text(w) for w in collapsed):
        return "N2.collapsed_wall_set must be a list of non-empty strings"
    wall_map = {_norm(w): w for w in walls}
    if any(_norm(w) not in wall_map for w in collapsed):
        return "N2.collapsed_wall_set must be a subset of walls"
    if not _list(checks):
        return "N2.pairwise_checks must be a list"
    expected_pairs = {frozenset((_norm(a), _norm(b))) for a, b in combinations(walls, 2)}
    seen_pairs = set()
    for index, check in enumerate(checks, 1):
        if not isinstance(check, dict) or not _text(check.get("left")) or not _text(check.get("right")):
            return f"N2 pairwise check {index} must name left and right walls"
        pair = frozenset((_norm(check["left"]), _norm(check["right"])))
        if pair not in expected_pairs or pair in seen_pairs:
            return f"N2 pairwise check {index} is duplicate or names unknown walls"
        for field in ("left_closes_right", "right_closes_left", "independent"):
            if not isinstance(check.get(field), bool):
                return f"N2 pairwise check {index}.{field} must be boolean"
        expected_independent = not check["left_closes_right"] and not check["right_closes_left"]
        if check["independent"] != expected_independent:
            return f"N2 pairwise check {index}.independent is inconsistent"
        if status == "PASS" and not check["independent"]:
            retained = {_norm(w) for w in collapsed}
            if pair.issubset(retained):
                return "N2 PASS keeps both walls from a dependent pair in collapsed_wall_set"
        seen_pairs.add(pair)
    if seen_pairs != expected_pairs:
        return "N2.pairwise_checks must cover every unordered wall pair"
    return _unresolved_error(section, "N2", status)


def _validate_n3(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N3_hidden_wall_scan")
    if error:
        return error
    assert section is not None
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
    for index, hit in enumerate(hits, 1):
        if not isinstance(hit, dict) or not _text(hit.get("phrase")):
            return f"N3 hit {index} must name a phrase"
        classification = hit.get("classification")
        if classification not in {"retained_authority", "hidden_admission", "non_load_bearing"}:
            return f"N3 hit {index}.classification is invalid"
        error = _locator_error(hit.get("evidence_path"), hit.get("evidence_locator"), manifest, f"N3 hit {index}")
        if error:
            return error
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
    return _unresolved_error(section, "N3", status)


def _validate_n4(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N4_residual_matching")
    if error:
        return error
    assert section is not None
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
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N4 scan")
    return error or _unresolved_error(section, "N4", status)


def _validate_n5(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N5_rhetoric_audit")
    if error:
        return error
    assert section is not None
    if not _text(section.get("scan_scope")):
        return "N5.scan_scope must name the negative rhetoric checked"
    statements = section.get("statements")
    if not _list(statements):
        return "N5.statements must be a list"
    error = _none_found_error(section, statements, "N5")
    if error:
        return error
    for index, statement in enumerate(statements, 1):
        if not isinstance(statement, dict) or not _text(statement.get("phrase")):
            return f"N5 statement {index} must name a phrase"
        if not _list(statement.get("tested_resolutions")) or not all(_text(x) for x in statement["tested_resolutions"]):
            return f"N5 statement {index}.tested_resolutions must be non-empty"
        if not _list(statement.get("untested_resolutions")) or not all(_text(x) for x in statement["untested_resolutions"]):
            return f"N5 statement {index}.untested_resolutions must be a list of non-empty strings"
        error = _locator_error(statement.get("evidence_path"), statement.get("evidence_locator"), manifest, f"N5 statement {index}")
        if error:
            return error
        if status == "PASS" and statement["untested_resolutions"]:
            return f"No-Go Discipline PASS cannot retain untested N5 resolutions for statement {index}"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N5 scan")
    return error or _unresolved_error(section, "N5", status)


def _validate_n6(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N6_partial_closure_scan")
    if error:
        return error
    assert section is not None
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
    if not _list(checked) or set(checked) != PREMISE_CLASSES_CHECKED:
        return f"N6.premise_classes_checked must equal {sorted(PREMISE_CLASSES_CHECKED)}"
    candidates = section.get("candidates")
    if not _list(candidates):
        return "N6.candidates must be a list"
    error = _none_found_error(section, candidates, "N6")
    if error:
        return error
    allowed_kinds = {"approved_primitive", "owner_governed", "tier_a", "convention_reframe", "definition_refactor"}
    seen_candidate_ids: set[str] = set()
    for index, candidate in enumerate(candidates, 1):
        if not isinstance(candidate, dict) or candidate.get("kind") not in allowed_kinds:
            return f"N6 candidate {index}.kind is invalid"
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
        for field in ("could_close_wall", "addressed"):
            if not isinstance(candidate.get(field), bool):
                return f"N6 candidate {index}.{field} must be boolean"
        if not _text(candidate.get("disposition")):
            return f"N6 candidate {index}.disposition must be non-empty"
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
                "owner_governed": "owner_governed_residual",
                "tier_a": "tier_a_derivation_target",
                "convention_reframe": "tier_a_convention_not_accepted",
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
    if not _text(section.get("route_id")) or not _text(section.get("argument")) or not _text(section.get("resolution")):
        return "N7.route_id, N7.argument, and N7.resolution must be non-empty"
    if not isinstance(section.get("resolved"), bool):
        return "N7.resolved must be boolean"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N7")
    if error:
        return error
    routes = {
        _norm(str(route.get("route_id") or "")): route
        for route in packet.get("N1_alternative_routes") or []
    }
    steelman_route = routes.get(_norm(section["route_id"]))
    if not steelman_route:
        return "N7.route_id must name an evidenced N1 route"
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
    error = _locator_error(
        section.get("evidence_path"),
        section.get("evidence_locator"),
        manifest,
        "N8 search",
    )
    if error:
        return error
    candidate_ids: set[str] | None = None
    if manifest is not None:
        entry = manifest.get(section.get("evidence_path"))
        if not entry:
            return "N8 evidence path is outside the restricted packet"
        if "cross_cycle_index" not in set(entry.get("roles") or []):
            return "N8 must cite the orchestrator-owned cross_cycle_index surface"
        candidate_ids = _cross_cycle_candidate_ids(entry)
        if candidate_ids is None:
            return "N8 cross-cycle index is malformed or not orchestrator-authenticated"
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
        candidate_id = str(echo["candidate_id"])
        if candidate_id in seen_candidate_ids:
            return f"N8 echo {index}.candidate_id is duplicated"
        if candidate_ids is not None and candidate_id not in candidate_ids:
            return f"N8 echo {index}.candidate_id is absent from the cross-cycle index"
        for field in ("retired", "applicable", "addressed"):
            if not isinstance(echo.get(field), bool):
                return f"N8 echo {index}.{field} must be boolean"
        error = _locator_error(echo.get("evidence_path"), echo.get("evidence_locator"), manifest, f"N8 echo {index}")
        if error:
            return error
        if status == "PASS" and echo["applicable"] and not echo["addressed"]:
            return f"No-Go Discipline PASS leaves applicable N8 echo {index} unaddressed"
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
    if packet.get("required") is not True:
        return "no_go_discipline.required must be true"
    status = packet.get("status")
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
        if audit.get("verdict") not in NON_CLEAN_VERDICTS:
            return "No-Go Discipline FAIL requires a conservative non-clean verdict"
        if audit.get("chain_closes") is not False:
            return "No-Go Discipline FAIL requires chain_closes=false"
        if packet.get("demotion") not in DEMOTIONS:
            return f"No-Go Discipline FAIL demotion must be one of {sorted(DEMOTIONS)}"
        if not _text(packet.get("narrowed_claim_scope")):
            return "No-Go Discipline FAIL requires narrowed_claim_scope"
        if _norm(packet["narrowed_claim_scope"]) != _norm(str(audit.get("claim_scope") or "")):
            return "No-Go Discipline FAIL narrowed_claim_scope must equal the applied claim_scope"
        if not _text(packet.get("prior_claim_scope")):
            return "No-Go Discipline FAIL requires prior_claim_scope"
        if prior_claim_scope and _norm(packet["prior_claim_scope"]) != _norm(prior_claim_scope):
            return "No-Go Discipline FAIL prior_claim_scope must equal the pre-audit ledger scope"
        if _norm(packet["prior_claim_scope"]) == _norm(packet["narrowed_claim_scope"]):
            return "No-Go Discipline FAIL must actually narrow the pre-audit claim scope"
        if not _list(packet.get("corrected_wall_set")) or not all(_text(x) for x in packet["corrected_wall_set"]):
            return "No-Go Discipline FAIL corrected_wall_set must be a list of non-empty strings"
        collapsed = packet.get("N2_wall_independence", {}).get("collapsed_wall_set") or []
        if {_norm(x) for x in packet["corrected_wall_set"]} != {_norm(x) for x in collapsed}:
            return "No-Go Discipline FAIL corrected_wall_set must equal N2.collapsed_wall_set"
        next_route = packet.get("next_route")
        if not isinstance(next_route, dict):
            return "No-Go Discipline FAIL next_route must be an object"
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
