#!/usr/bin/env python3
"""Shared semantic contract checks for audit verdict tuples.

Transport JSON schemas validate each field independently.  Cross-field policy
stays here so ordinary seats, stored summaries, judicial votes, and the final
apply gate cannot disagree about whether a tuple is applyable.
"""
from __future__ import annotations


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
