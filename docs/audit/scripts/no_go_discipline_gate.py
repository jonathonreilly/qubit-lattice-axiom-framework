#!/usr/bin/env python3
"""Shared enforcement for the audit lane's No-Go Discipline packet.

The isolated auditor cannot inspect the broad repository without violating the
fresh-look boundary.  It must therefore record what the restricted packet does
and does not establish for N1-N8.  A failed checklist may support a conservative
non-clean verdict; it may never support ``audited_clean``.
"""
from __future__ import annotations

import re
from typing import Any


SOURCE_TRIGGER_RE = re.compile(
    r"\bno[-_ ]?go\b|\bobstruction\b|\bstretch[-_ ]?attempt\b|"
    r"\bwall(?:s)?\b|\badmission(?:s)?\b|\bconditional on\b|"
    r"no retained primitive|requires? (?:a )?new axiom|cannot be derived",
    re.IGNORECASE,
)
OUTPUT_TRIGGER_RE = re.compile(
    r"\bwall(?:s)?\b|\badmission(?:s)?\b|\bobstruction\b|"
    r"no retained primitive|requires? (?:a )?new axiom|cannot be derived|"
    r"no route exists|structurally (?:closed|undecidable)",
    re.IGNORECASE,
)
REPAIR_PREFIX_TRIGGER_RE = re.compile(
    r"^(?:missing_dependency_edge|missing_bridge_theorem|scope_too_broad|other)\s*:",
    re.IGNORECASE,
)

CHECKLIST_TEXT_FIELDS = (
    "N2_wall_independence",
    "N3_hidden_wall_scan",
    "N4_residual_matching",
    "N5_rhetoric_audit",
    "N6_partial_closure_scan",
    "N7_steelman",
    "N8_cross_cycle_echo",
)
ROUTE_FIELDS = ("route", "outcome", "honesty_marker", "authority")
HONESTY_MARKERS = {"ATTEMPTED", "RULED OUT BY PRIOR"}


def source_requires_no_go_discipline(
    note_path: str | None,
    note_body: str | None,
    claim_type_hint: str | None,
) -> bool:
    """Return whether source metadata/prose requires the N1-N8 gate."""
    if claim_type_hint == "no_go":
        return True
    return bool(SOURCE_TRIGGER_RE.search(f"{note_path or ''}\n{note_body or ''}"))


def output_requires_no_go_discipline(audit: dict[str, Any]) -> bool:
    """Return whether the proposed verdict itself requires the N1-N8 gate."""
    if audit.get("claim_type") == "no_go":
        return True
    notes = str(audit.get("notes_for_re_audit_if_any") or "").strip()
    if REPAIR_PREFIX_TRIGGER_RE.search(notes):
        return True
    rationale = str(audit.get("verdict_rationale") or "")
    return bool(OUTPUT_TRIGGER_RE.search(rationale))


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_no_go_discipline(
    audit: dict[str, Any],
    *,
    source_required: bool = False,
) -> str | None:
    """Validate the structured N1-N8 packet for one proposed audit blob.

    ``FAIL`` is a valid documented gate result for a non-clean verdict.  It is
    rejected only when paired with ``audited_clean``.  ``PASS`` requires five
    distinct N1 routes and complete written answers for N2-N8.
    """
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
        return "no_go_discipline.required must be true when a packet is supplied"

    status = packet.get("status")
    if status not in {"PASS", "FAIL"}:
        return "no_go_discipline.status must be PASS or FAIL"

    routes = packet.get("N1_alternative_routes")
    if not isinstance(routes, list):
        return "no_go_discipline.N1_alternative_routes must be a list"
    normalized_routes: set[str] = set()
    for index, route in enumerate(routes, 1):
        if not isinstance(route, dict):
            return f"N1 route {index} must be an object"
        missing = [field for field in ROUTE_FIELDS if not _nonempty_text(route.get(field))]
        if missing:
            return f"N1 route {index} has empty fields: {missing}"
        marker = route["honesty_marker"].strip().upper()
        if marker not in HONESTY_MARKERS:
            return (
                f"N1 route {index} honesty_marker must be ATTEMPTED or "
                "RULED OUT BY PRIOR"
            )
        normalized_routes.add(re.sub(r"\s+", " ", route["route"].strip().lower()))

    for field in CHECKLIST_TEXT_FIELDS:
        if not _nonempty_text(packet.get(field)):
            return f"no_go_discipline.{field} must be a non-empty string"

    failures = packet.get("failures")
    if not isinstance(failures, list):
        return "no_go_discipline.failures must be a list"
    if status == "PASS":
        if len(normalized_routes) < 5:
            return "No-Go Discipline PASS requires at least 5 distinct N1 routes"
        if failures:
            return "No-Go Discipline PASS cannot carry failure items"
    elif not failures or not all(_nonempty_text(item) for item in failures):
        return "No-Go Discipline FAIL requires at least one non-empty failure item"

    if audit.get("verdict") == "audited_clean" and status != "PASS":
        return "audited_clean is forbidden when No-Go Discipline status is not PASS"
    return None
