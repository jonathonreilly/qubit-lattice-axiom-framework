#!/usr/bin/env python3
"""Centralized foundational-premise policy for the audit pipeline.

Exactly two kinds of supplied physics content satisfy a dependency without an
audited theorem row: framework axioms and explicitly approved primitives. Both
are registered in ``docs/audit/data/axiom_premise_nodes.json`` and neither
bounds downstream status.

Governance decisions, derivation targets, conventions, historical admissions,
and open obligations never satisfy a physics dependency. They must instead be
derived through the audit lane or remain explicit conditional/open content.

Standard textbook theorems are deliberately not handled here. The framework
proves consumed textbook results inline at framework rigor, so they must earn
retained-grade through the normal audit path and need no carve-out.

Every consumer that asks whether a dependency is supplied as foundational
upstream must go through ``is_accepted_premise_dep`` so policy cannot drift.
"""
from __future__ import annotations

import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
_AXIOM_PREMISE_NODES_PATH = _DATA_DIR / "axiom_premise_nodes.json"

_FOUNDATIONAL_PREMISE_IDS: set[str] | None = None


def foundational_premise_ids() -> set[str]:
    """Canonical axiom and approved-primitive ids."""
    global _FOUNDATIONAL_PREMISE_IDS
    if _FOUNDATIONAL_PREMISE_IDS is None:
        if not _AXIOM_PREMISE_NODES_PATH.exists():
            _FOUNDATIONAL_PREMISE_IDS = set()
        else:
            try:
                data = json.loads(
                    _AXIOM_PREMISE_NODES_PATH.read_text(encoding="utf-8")
                )
                _FOUNDATIONAL_PREMISE_IDS = set(data.get("canonical_ids") or [])
            except Exception:
                _FOUNDATIONAL_PREMISE_IDS = set()
    return _FOUNDATIONAL_PREMISE_IDS


def axiom_premise_ids() -> set[str]:
    """Compatibility name for callers; includes axioms and approved primitives."""
    return foundational_premise_ids()


def accepted_premise_ids() -> set[str]:
    """Ids supplied by the axiom or approved-primitive foundation."""
    return foundational_premise_ids()


def is_axiom_premise(dep_id: str) -> bool:
    """Compatibility predicate for an axiom or approved primitive."""
    return dep_id in foundational_premise_ids()


def is_accepted_premise_dep(dep_id: str) -> bool:
    """True only for a registered axiom or explicitly approved primitive."""
    return dep_id in foundational_premise_ids()


def _reset_cache_for_tests() -> None:
    global _FOUNDATIONAL_PREMISE_IDS
    _FOUNDATIONAL_PREMISE_IDS = None
