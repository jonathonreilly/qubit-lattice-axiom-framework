#!/usr/bin/env python3
"""Shared semantic contract checks for audit verdict tuples.

Transport JSON schemas validate each field independently.  Cross-field policy
stays here so ordinary seats, stored summaries, judicial votes, and the final
apply gate cannot disagree about whether a tuple is applyable.
"""
from __future__ import annotations


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
