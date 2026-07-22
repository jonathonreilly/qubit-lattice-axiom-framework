#!/usr/bin/env python3
"""Shared semantic contract checks for audit verdict tuples.

Transport JSON schemas validate each field independently.  Cross-field policy
stays here so ordinary seats, stored summaries, judicial votes, and the final
apply gate cannot disagree about whether a tuple is applyable.
"""
from __future__ import annotations

import hashlib
import json
import re


JUDICIAL_VOTE_FIELDS = (
    "sided_with",
    "ratified_verdict",
    "ratified_claim_type",
    "ratified_claim_scope",
    "ratified_load_bearing_step_class",
    "negative_assertion_classes",
    "judgment_rationale",
    "first_auditor_error",
    "second_auditor_error",
)
JUDICIAL_SIDES = {"first", "second", "hybrid", "neither"}
TERMINAL_VERDICTS = {
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}
CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
}


def terminal_compute_required_error(payload: object) -> str | None:
    """Reject a compute deferral that is mixed with a terminal audit tuple."""
    if isinstance(payload, dict) and payload.get("compute_required") is not None:
        return "compute_required cannot accompany or produce a terminal audit verdict"
    return None


def verdict_claim_type_error(
    verdict: object,
    claim_type: object,
    decoration_parent_claim_id: object = None,
) -> str | None:
    """Return the canonical incompatibility for a verdict/type tuple."""
    if verdict == "audited_clean" and claim_type in {"decoration", "meta"}:
        return f"audited_clean cannot ratify claim_type={claim_type!r}"
    if verdict == "audited_decoration":
        if claim_type != "decoration":
            return "audited_decoration requires claim_type='decoration'"
        if not decoration_parent_claim_id:
            return "audited_decoration requires decoration_parent_claim_id"
    return None


def decoration_parent_tuple_key(
    verdict: object,
    decoration_parent_claim_id: object,
) -> object:
    """Return the authority-parent component of an agreement tuple."""
    if verdict != "audited_decoration":
        return None
    return decoration_parent_claim_id


def normalized_scope(value: object) -> str:
    """Normalize whitespace that carries no scientific scope distinction."""
    return re.sub(r"\s+", " ", str(value or "").strip())


def judicial_vote_tuple(vote: dict) -> tuple:
    """Project a judicial vote onto every field requiring 3-of-5 agreement."""
    classes = vote.get("negative_assertion_classes")
    classes_key = (
        tuple(sorted(classes)) if isinstance(classes, list) else ("<invalid>",)
    )
    return (
        vote.get("sided_with"),
        vote.get("ratified_verdict"),
        vote.get("ratified_claim_type"),
        normalized_scope(vote.get("ratified_claim_scope")),
        vote.get("ratified_load_bearing_step_class"),
        decoration_parent_tuple_key(
            vote.get("ratified_verdict"),
            vote.get("ratified_decoration_parent_claim_id"),
        ),
        classes_key,
    )


def judicial_vote_schema_error(vote: object) -> str | None:
    """Validate the semantic vote surface shared by panel and apply gates."""
    if not isinstance(vote, dict):
        return "vote must be a JSON object"
    missing = [field for field in JUDICIAL_VOTE_FIELDS if field not in vote]
    if missing:
        return f"vote_missing_fields:{','.join(missing)}"
    if vote.get("sided_with") not in JUDICIAL_SIDES:
        return "vote has invalid sided_with"
    if vote.get("ratified_verdict") not in TERMINAL_VERDICTS:
        return "vote has invalid ratified_verdict"
    if vote.get("ratified_claim_type") not in CLAIM_TYPES:
        return "vote has invalid ratified_claim_type"
    tuple_error = verdict_claim_type_error(
        vote.get("ratified_verdict"),
        vote.get("ratified_claim_type"),
        vote.get("ratified_decoration_parent_claim_id"),
    )
    if tuple_error:
        return f"vote has incompatible verdict/claim_type: {tuple_error}"
    for field in (
        "ratified_claim_scope",
        "ratified_load_bearing_step_class",
        "judgment_rationale",
        "first_auditor_error",
        "second_auditor_error",
    ):
        if not isinstance(vote.get(field), str) or not vote[field].strip():
            return f"vote field {field} must be a non-empty string"
    if vote.get("ratified_load_bearing_step_class") not in set("ABCDEFG"):
        return "vote has invalid ratified_load_bearing_step_class"
    declared = vote.get("negative_assertion_classes")
    if not isinstance(declared, list) or not all(
        isinstance(item, str) and item.strip() for item in declared
    ):
        return "negative_assertion_classes must be a list of non-empty strings"
    for field in (
        "hybrid_resolution_note",
        "ratified_decoration_parent_claim_id",
        "ratified_load_bearing_step",
        "notes_for_re_audit_if_any",
    ):
        if field in vote and vote[field] is not None and not isinstance(
            vote[field], str
        ):
            return f"vote field {field} must be a string or null"
    if "no_go_discipline" in vote and vote["no_go_discipline"] is not None:
        if not isinstance(vote["no_go_discipline"], dict):
            return "no_go_discipline must be an object or null"
    first_error = str(vote.get("first_auditor_error") or "").strip().lower()
    second_error = str(vote.get("second_auditor_error") or "").strip().lower()
    if vote.get("sided_with") == "first" and second_error == "none":
        return "a first-sided vote must explain the second auditor's error"
    if vote.get("sided_with") == "second" and first_error == "none":
        return "a second-sided vote must explain the first auditor's error"
    if vote.get("sided_with") in {"hybrid", "neither"} and (
        first_error == "none" or second_error == "none"
    ):
        return (
            f"a {vote.get('sided_with')}-sided vote must explain both "
            "auditors' errors"
        )
    return None


def sided_judicial_vote_context_error(row: dict, vote: dict) -> str | None:
    """Reject a sided vote that changes its selected stored seat tuple."""
    side = vote.get("sided_with")
    if side not in {"first", "second"}:
        return None
    chosen = ((row.get("cross_confirmation") or {}).get(f"{side}_audit") or {})
    comparisons = (
        ("verdict", vote.get("ratified_verdict"), chosen.get("verdict")),
        ("claim_type", vote.get("ratified_claim_type"), chosen.get("claim_type")),
        (
            "claim_scope",
            normalized_scope(vote.get("ratified_claim_scope")),
            normalized_scope(chosen.get("claim_scope")),
        ),
        (
            "load_bearing_step_class",
            vote.get("ratified_load_bearing_step_class"),
            chosen.get("load_bearing_step_class"),
        ),
        (
            "negative_assertion_classes",
            tuple(sorted(vote.get("negative_assertion_classes") or [])),
            tuple(sorted(chosen.get("negative_assertion_classes") or [])),
        ),
        (
            "decoration_parent_claim_id",
            decoration_parent_tuple_key(
                vote.get("ratified_verdict"),
                vote.get("ratified_decoration_parent_claim_id"),
            ),
            decoration_parent_tuple_key(
                chosen.get("verdict"), chosen.get("decoration_parent_claim_id")
            ),
        ),
    )
    mismatches = [name for name, actual, expected in comparisons if actual != expected]
    if mismatches:
        return (
            f"{side}-sided vote changes selected seat tuple fields: "
            f"{','.join(mismatches)}; use sided_with='hybrid' for corrections"
        )
    return None


def judicial_disagreement_fingerprint(row: dict) -> dict:
    """Bind a panel record to the exact source hash and two stored seats."""
    cross = row.get("cross_confirmation") or {}
    first = cross.get("first_audit") or {}
    second = cross.get("second_audit") or {}
    seat_payload = json.dumps(
        {"first_audit": first, "second_audit": second},
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return {
        "schema": "judicial_disagreement_fingerprint_v1",
        "claim_id": row.get("claim_id"),
        "note_hash": row.get("note_hash"),
        "first_audit_invocation_id": first.get("audit_invocation_id"),
        "second_audit_invocation_id": second.get("audit_invocation_id"),
        "seat_summaries_sha256": hashlib.sha256(
            seat_payload.encode("utf-8")
        ).hexdigest(),
    }
