#!/usr/bin/env python3
"""Centralized premise-node policy for the audit pipeline.

Single source of truth for which cited authorities count as *accepted
premises* — dependencies that satisfy chain closure even though their own
effective_status is not in a retained-grade bucket:

  - axiom-premise nodes (docs/audit/data/axiom_premise_nodes.json): the
    canonical A1+A2 axiom node. You do not audit axioms; deriving from the
    axiom is class (C). Stays effective_status=meta but is dependency-
    satisfied for downstream chain closure.
  - admitted-external-import nodes (docs/audit/data/external_import_nodes.json):
    allowlisted, scope-limited standard textbook theorems that make no
    framework-specific claim. Accepted as retained-grade upstream for their
    stated result only.

Every consumer that asks "is this dep satisfied as upstream?" — the LLM
prompt renderer, compute_effective_status, audit_lint, and
compute_reaudit_candidates — MUST go through `is_accepted_premise_dep` so
the policy cannot drift between them.

This module reads the registries lazily and tolerates their absence (returns
empty sets), so it is inert until the registries land.
"""
from __future__ import annotations

import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
_AXIOM_PREMISE_NODES_PATH = _DATA_DIR / "axiom_premise_nodes.json"
_EXTERNAL_IMPORT_NODES_PATH = _DATA_DIR / "external_import_nodes.json"

_AXIOM_PREMISE_IDS: set[str] | None = None
_EXTERNAL_IMPORT_IDS: set[str] | None = None


def _load_ids(path: Path, key: str) -> set[str]:
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return set()
    if key == "canonical_ids":
        return set(data.get("canonical_ids") or [])
    if key == "nodes":
        return set((data.get("nodes") or {}).keys())
    return set()


def axiom_premise_ids() -> set[str]:
    """Canonical axiom-premise claim_ids (see axiom_premise_nodes.json)."""
    global _AXIOM_PREMISE_IDS
    if _AXIOM_PREMISE_IDS is None:
        _AXIOM_PREMISE_IDS = _load_ids(_AXIOM_PREMISE_NODES_PATH, "canonical_ids")
    return _AXIOM_PREMISE_IDS


def external_import_ids() -> set[str]:
    """Allowlisted admitted-external-import claim_ids (see external_import_nodes.json)."""
    global _EXTERNAL_IMPORT_IDS
    if _EXTERNAL_IMPORT_IDS is None:
        _EXTERNAL_IMPORT_IDS = _load_ids(_EXTERNAL_IMPORT_NODES_PATH, "nodes")
    return _EXTERNAL_IMPORT_IDS


def accepted_premise_ids() -> set[str]:
    """Union of axiom-premise and admitted-external-import ids."""
    return axiom_premise_ids() | external_import_ids()


def is_axiom_premise(dep_id: str) -> bool:
    return dep_id in axiom_premise_ids()


def is_external_import(dep_id: str) -> bool:
    return dep_id in external_import_ids()


def is_accepted_premise_dep(dep_id: str) -> bool:
    """True if dep_id is an accepted premise (axiom or admitted external import).

    Such a dep satisfies chain closure even though its own effective_status
    is not retained-grade. The carve-out only removes the automatic
    not-retained-grade downgrade; the citing row must still pass its own
    audit (the LLM verdict is judged separately, per AUDIT_AGENT_PROMPT_TEMPLATE.md §4).
    """
    return dep_id in accepted_premise_ids()


def _reset_cache_for_tests() -> None:
    global _AXIOM_PREMISE_IDS, _EXTERNAL_IMPORT_IDS
    _AXIOM_PREMISE_IDS = None
    _EXTERNAL_IMPORT_IDS = None
