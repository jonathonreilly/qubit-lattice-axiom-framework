"""Canonical validation for one-use audit invocation identifiers."""

from __future__ import annotations

import re

AUDIT_INVOCATION_ID_RE = re.compile(r"[0-9a-f]{32}")
AUDIT_INVOCATION_ID_ERROR = (
    "audit_invocation_id must be 32 lowercase hexadecimal characters"
)


def validation_error(value: object, *, required: bool) -> str | None:
    """Return the canonical schema error for an invocation id, if any."""
    if value is None and not required:
        return None
    if not isinstance(value, str) or not AUDIT_INVOCATION_ID_RE.fullmatch(value):
        return AUDIT_INVOCATION_ID_ERROR
    return None
