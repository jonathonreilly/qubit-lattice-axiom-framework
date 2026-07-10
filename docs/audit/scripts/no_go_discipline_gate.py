#!/usr/bin/env python3
"""Shared No-Go Discipline packet construction and validation.

The gate binds every N1-N8 statement to evidence visible in the restricted
audit packet.  It does not try to prove semantic correctness mechanically; it
does prevent empty prose, synthetic route counting, unsupported prior-authority
claims, unresolved steelmen, and failed checklists from authorizing a clean
negative verdict.
"""
from __future__ import annotations

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
    "partial_attempt_with_named_untested_routes",
    "partial_narrowing",
    "bounded_with_corrected_wall_count",
    "stretch_attempt_with_honest_residual",
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
SOURCE_NEGATIVE_RE = re.compile(
    r"structurally (?:closed|undecidable)|no route exists|"
    r"no retained primitive(?: supplies)?|requires? (?:a )?new axiom|"
    r"cannot be derived from|does not lift|cannot lift|"
    r"bounded with named walls|conditional on [^\n]{0,120}\b(?:walls?|admissions?)\b|"
    r"(?:^|\n)\s*(?:walls?|admissions?)\s*:",
    re.IGNORECASE,
)
OUTPUT_NEGATIVE_RE = re.compile(
    r"structurally (?:closed|undecidable)|no route exists|"
    r"no retained primitive(?: supplies)?|requires? (?:a )?new axiom|"
    r"cannot be derived from|does not lift|cannot lift|"
    r"conditional on [^\n]{0,120}\b(?:walls?|admissions?)\b|"
    r"residual wall|named walls?",
    re.IGNORECASE,
)
OUTPUT_BOUNDARY_FIELDS = (
    "claim_scope",
    "load_bearing_step",
    "chain_closure_explanation",
    "verdict_rationale",
    "notes_for_re_audit_if_any",
)

AXIOM_REGISTRY = "docs/audit/data/axiom_premise_nodes.json"
OWNER_REGISTRY = "docs/audit/data/owner_governed_premise_nodes.json"
TIER_A_REGISTRY = "docs/audit/data/tier_a_admissions.json"


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
        premise_type="tier_a_derivation_target_registry",
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
    return bool(SOURCE_NEGATIVE_RE.search(body))


def output_requires_no_go_discipline(audit: dict[str, Any]) -> bool:
    if audit.get("claim_type") == "no_go":
        return True
    boundary = "\n".join(str(audit.get(field) or "") for field in OUTPUT_BOUNDARY_FIELDS)
    return bool(OUTPUT_NEGATIVE_RE.search(boundary))


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any) -> bool:
    return isinstance(value, list)


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


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
        if status == "PASS" and disposition != "CLOSED":
            return f"No-Go Discipline PASS cannot contain N1 route {index} disposition={disposition}"
        route_ids.add(route_id)
        route_classes.add(route_class)
    if status == "PASS" and len(route_classes) < 5:
        return "No-Go Discipline PASS requires at least 5 distinct route_class values"
    mechanisms = [_norm(route["mechanism"]) for route in routes]
    attempts = [_norm(route["attempt"]) for route in routes]
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
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N3 scan")
    if error:
        return error
    hits = section.get("hits")
    if not _list(hits):
        return "N3.hits must be a list"
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
        if classification == "hidden_admission":
            if not _text(hit.get("promoted_wall")) or _norm(hit["promoted_wall"]) not in walls:
                return f"N3 hidden admission {index} must be promoted into N2.walls"
    return _unresolved_error(section, "N3", status)


def _validate_n4(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N4_residual_matching")
    if error:
        return error
    assert section is not None
    witnesses = section.get("witnesses")
    if not _list(witnesses):
        return "N4.witnesses must be a list"
    for index, witness in enumerate(witnesses, 1):
        if not isinstance(witness, dict):
            return f"N4 witness {index} must be an object"
        for field in ("witness_residual", "claim_residual"):
            if not _text(witness.get(field)):
                return f"N4 witness {index}.{field} must be non-empty"
        if not isinstance(witness.get("match"), bool):
            return f"N4 witness {index}.match must be boolean"
        error = _locator_error(witness.get("evidence_path"), witness.get("evidence_locator"), manifest, f"N4 witness {index}")
        if error:
            return error
        if status == "PASS" and not witness["match"]:
            return f"No-Go Discipline PASS cannot retain mismatched N4 witness {index}"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N4 scan")
    return error or _unresolved_error(section, "N4", status)


def _validate_n5(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N5_rhetoric_audit")
    if error:
        return error
    assert section is not None
    statements = section.get("statements")
    if not _list(statements):
        return "N5.statements must be a list"
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
    candidates = section.get("candidates")
    if not _list(candidates):
        return "N6.candidates must be a list"
    allowed_kinds = {"approved_primitive", "owner_governed", "tier_a", "convention_reframe", "definition_refactor"}
    for index, candidate in enumerate(candidates, 1):
        if not isinstance(candidate, dict) or candidate.get("kind") not in allowed_kinds:
            return f"N6 candidate {index}.kind is invalid"
        for field in ("could_close_wall", "addressed"):
            if not isinstance(candidate.get(field), bool):
                return f"N6 candidate {index}.{field} must be boolean"
        if not _text(candidate.get("disposition")):
            return f"N6 candidate {index}.disposition must be non-empty"
        error = _locator_error(candidate.get("evidence_path"), candidate.get("evidence_locator"), manifest, f"N6 candidate {index}")
        if error:
            return error
        if status == "PASS" and candidate["could_close_wall"] and not candidate["addressed"]:
            return f"No-Go Discipline PASS leaves N6 candidate {index} unaddressed"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N6 scan")
    return error or _unresolved_error(section, "N6", status)


def _validate_n7(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N7_steelman")
    if error:
        return error
    assert section is not None
    if not _text(section.get("argument")) or not _text(section.get("resolution")):
        return "N7.argument and N7.resolution must be non-empty"
    if not isinstance(section.get("resolved"), bool):
        return "N7.resolved must be boolean"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N7")
    if error:
        return error
    if status == "PASS" and not section["resolved"]:
        return "No-Go Discipline PASS requires the N7 steelman to be resolved"
    return None


def _validate_n8(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N8_cross_cycle_echo")
    if error:
        return error
    assert section is not None
    if not isinstance(section.get("packet_complete"), bool):
        return "N8.packet_complete must be boolean"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N8 search")
    if error:
        return error
    echoes = section.get("echoes")
    if not _list(echoes):
        return "N8.echoes must be a list"
    for index, echo in enumerate(echoes, 1):
        if not isinstance(echo, dict) or not _text(echo.get("mechanism")):
            return f"N8 echo {index} must name a mechanism"
        for field in ("retired", "applicable", "addressed"):
            if not isinstance(echo.get(field), bool):
                return f"N8 echo {index}.{field} must be boolean"
        error = _locator_error(echo.get("evidence_path"), echo.get("evidence_locator"), manifest, f"N8 echo {index}")
        if error:
            return error
        if status == "PASS" and echo["applicable"] and not echo["addressed"]:
            return f"No-Go Discipline PASS leaves applicable N8 echo {index} unaddressed"
    if status == "PASS" and not section["packet_complete"]:
        return "No-Go Discipline PASS requires packet_complete=true for N8"
    return _unresolved_error(section, "N8", status)


def validate_no_go_discipline(
    audit: dict[str, Any],
    *,
    source_required: bool = False,
    evidence_manifest: dict[str, dict] | None = None,
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
        if not _list(packet.get("corrected_wall_set")) or not all(_text(x) for x in packet["corrected_wall_set"]):
            return "No-Go Discipline FAIL corrected_wall_set must be a list of non-empty strings"
        if not _text(packet.get("next_route")):
            return "No-Go Discipline FAIL requires next_route"

    return None
