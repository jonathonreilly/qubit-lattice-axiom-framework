#!/usr/bin/env python3
"""Centralized axiom-premise policy for the audit pipeline.

Single source of truth for which cited authorities count as *accepted
premises* — dependencies that satisfy chain closure even though their own
effective_status is not in a retained-grade bucket. Currently this is exactly
the canonical A1+A2 axiom node (docs/audit/data/axiom_premise_nodes.json):
you do not audit axioms, so deriving from the axiom is class (C), and the
axiom node stays effective_status=meta while still being dependency-satisfying
for downstream chain closure.

Standard textbook theorems are deliberately NOT handled here. Rather than
admit them on citation, the framework proves them inline at framework rigor
(e.g. the UHF tracial-uniqueness density argument in
POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE..., and the explicit Naimark
isometry construction in LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME...), so
they must earn retained-grade through the normal audit path and need no
carve-out.

PROPOSAL (governance-gated): a SECOND accepted-premise class,
`admitted_derivation_target`, for the framework's named Tier-A admitted inputs
(docs/audit/data/tier_a_admissions.json; human registry
docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md). These are admitted
non-axiom inputs that each carry a verified retained-no-go portfolio. Accepting
them as chain-satisfying makes their dependents resolve to retained_bounded
(cleanly bounded) rather than blocked; on deriving one, land a retained theorem
for it and remove its entry, after which compute_effective_status auto-cascades
the transitive dependents toward retained. This WIDENS the accepted-premise set
beyond pure axioms and is a deliberate governance decision. SAFE-BY-DEFAULT:
this module is inert w.r.t. Tier-A unless tier_a_admissions.json is present, so
landing this patch alone changes nothing until the registry file is landed.

Every consumer that asks "is this dep satisfied as upstream?" — the LLM
prompt renderer, compute_effective_status, audit_lint, and
compute_reaudit_candidates — MUST go through `is_accepted_premise_dep` so the
policy cannot drift between them.

Reads the registry lazily and tolerates its absence (returns an empty set),
so it is inert until the registry lands.
"""
from __future__ import annotations

import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
_AXIOM_PREMISE_NODES_PATH = _DATA_DIR / "axiom_premise_nodes.json"
_TIER_A_ADMISSIONS_PATH = _DATA_DIR / "tier_a_admissions.json"

_AXIOM_PREMISE_IDS: set[str] | None = None
_TIER_A_ADMITTED_IDS: set[str] | None = None


def axiom_premise_ids() -> set[str]:
    """Canonical axiom-premise claim_ids (see axiom_premise_nodes.json)."""
    global _AXIOM_PREMISE_IDS
    if _AXIOM_PREMISE_IDS is None:
        if not _AXIOM_PREMISE_NODES_PATH.exists():
            _AXIOM_PREMISE_IDS = set()
        else:
            try:
                data = json.loads(_AXIOM_PREMISE_NODES_PATH.read_text(encoding="utf-8"))
                _AXIOM_PREMISE_IDS = set(data.get("canonical_ids") or [])
            except Exception:
                _AXIOM_PREMISE_IDS = set()
    return _AXIOM_PREMISE_IDS


def admitted_derivation_target_ids() -> set[str]:
    """Tier-A admitted non-axiom inputs (see tier_a_admissions.json).

    Inert-by-default: returns the empty set if the registry file is absent, so
    landing the premise_nodes.py patch alone changes no statuses. Distinct from
    axioms: these are admitted-for-now with no-go portfolios, intended for
    eventual derivation. Governance-gated -- adopting widens the accepted set.
    """
    global _TIER_A_ADMITTED_IDS
    if _TIER_A_ADMITTED_IDS is None:
        if not _TIER_A_ADMISSIONS_PATH.exists():
            _TIER_A_ADMITTED_IDS = set()
        else:
            try:
                data = json.loads(_TIER_A_ADMISSIONS_PATH.read_text(encoding="utf-8"))
                _TIER_A_ADMITTED_IDS = set(data.get("canonical_ids") or [])
            except Exception:
                _TIER_A_ADMITTED_IDS = set()
    return _TIER_A_ADMITTED_IDS


def accepted_premise_ids() -> set[str]:
    """Ids accepted as chain-satisfying premises: axiom nodes plus, if the
    Tier-A registry is present, the admitted derivation-targets/conventions."""
    return axiom_premise_ids() | admitted_derivation_target_ids()


def is_axiom_premise(dep_id: str) -> bool:
    return dep_id in axiom_premise_ids()


def is_admitted_derivation_target(dep_id: str) -> bool:
    return dep_id in admitted_derivation_target_ids()


def is_accepted_premise_dep(dep_id: str) -> bool:
    """True if dep_id is an accepted premise (the canonical axiom node).

    Such a dep satisfies chain closure even though its own effective_status is
    not retained-grade. The carve-out only removes the automatic
    not-retained-grade downgrade; the citing row must still pass its own audit
    (the LLM verdict is judged separately, per AUDIT_AGENT_PROMPT_TEMPLATE.md §4).
    """
    return dep_id in accepted_premise_ids()


def _reset_cache_for_tests() -> None:
    global _AXIOM_PREMISE_IDS, _TIER_A_ADMITTED_IDS
    _AXIOM_PREMISE_IDS = None
    _TIER_A_ADMITTED_IDS = None
