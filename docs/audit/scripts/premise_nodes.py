#!/usr/bin/env python3
"""Centralized accepted-premise policy for the audit pipeline.

Single source of truth for which cited authorities count as *accepted
premises* -- dependencies that satisfy chain closure even though their own
effective_status is not in a retained-grade bucket.

There are three supported classes:

* axiom/primitive premises from docs/audit/data/axiom_premise_nodes.json. These
  are framework axioms or explicitly approved primitives, are not audited,
  and do not bound downstream status.
* owner-governed residual premises from
  docs/audit/data/owner_governed_premise_nodes.json. These are explicit
  owner-adopted governance premises that retire formerly Tier-A residuals
  without making them axioms or approved primitives. They satisfy chain closure
  without Tier-A bounding, but only inside the recorded boundaries.
* Tier-A derivation-target admissions from docs/audit/data/tier_a_admissions.json.
  These are named non-axiom inputs accepted as chain-satisfying only at the
  bounded tier until a retained derivation lands and the entry is removed.
  Conventions listed in that file are survey metadata, not accepted premises:
  the existing convention parent rows contain more than the vacuous convention
  itself and must not be laundered as chain-satisfying theorem inputs.

Standard textbook theorems are deliberately NOT handled here. Rather than
admit them on citation, the framework proves them inline at framework rigor
(e.g. the UHF tracial-uniqueness density argument in
POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE..., and the explicit Naimark
isometry construction in LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME...), so
they must earn retained-grade through the normal audit path and need no
carve-out.

Every consumer that asks "is this dep satisfied as upstream?" -- the LLM
prompt renderer, compute_effective_status, audit_lint, and
compute_reaudit_candidates -- MUST go through `is_accepted_premise_dep` so the
policy cannot drift between them.

Reads registries lazily and tolerates absence, so the Tier-A path is inert
until docs/audit/data/tier_a_admissions.json lands.
"""
from __future__ import annotations

import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
_AXIOM_PREMISE_NODES_PATH = _DATA_DIR / "axiom_premise_nodes.json"
_OWNER_GOVERNED_PREMISE_NODES_PATH = _DATA_DIR / "owner_governed_premise_nodes.json"
_TIER_A_ADMISSIONS_PATH = _DATA_DIR / "tier_a_admissions.json"

_AXIOM_PREMISE_IDS: set[str] | None = None
_OWNER_GOVERNED_PREMISE_IDS: set[str] | None = None
_TIER_A_DATA: dict | None = None
_TIER_A_DERIVATION_TARGET_IDS: set[str] | None = None
_TIER_A_CONVENTION_IDS: set[str] | None = None


def axiom_premise_ids() -> set[str]:
    """Canonical axiom/approved-primitive premise ids.

    Historical function name retained for callers. Entries in
    axiom_premise_nodes.json chain-satisfy without bounding downstream rows.
    """
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


def owner_governed_premise_ids() -> set[str]:
    """Canonical owner-governed residual premise ids.

    Entries in owner_governed_premise_nodes.json chain-satisfy without bounding
    downstream rows. They are not axioms, not approved primitives, and not
    theorem derivations; they are explicit owner-governance retirements of
    formerly Tier-A residuals.
    """
    global _OWNER_GOVERNED_PREMISE_IDS
    if _OWNER_GOVERNED_PREMISE_IDS is None:
        if not _OWNER_GOVERNED_PREMISE_NODES_PATH.exists():
            _OWNER_GOVERNED_PREMISE_IDS = set()
        else:
            try:
                data = json.loads(
                    _OWNER_GOVERNED_PREMISE_NODES_PATH.read_text(encoding="utf-8")
                )
                _OWNER_GOVERNED_PREMISE_IDS = set(data.get("canonical_ids") or [])
            except Exception:
                _OWNER_GOVERNED_PREMISE_IDS = set()
    return _OWNER_GOVERNED_PREMISE_IDS


def tier_a_admissions_data() -> dict:
    """Raw Tier-A admission registry data, or {} when absent/invalid."""
    global _TIER_A_DATA
    if _TIER_A_DATA is None:
        if not _TIER_A_ADMISSIONS_PATH.exists():
            _TIER_A_DATA = {}
        else:
            try:
                _TIER_A_DATA = json.loads(
                    _TIER_A_ADMISSIONS_PATH.read_text(encoding="utf-8")
                )
            except Exception:
                _TIER_A_DATA = {}
    return _TIER_A_DATA


def admitted_derivation_target_ids() -> set[str]:
    """Tier-A admitted non-axiom derivation targets.

    Inert-by-default: returns the empty set if the registry file is absent, so
    landing the code patch alone changes no statuses. Distinct from axioms:
    these are admitted-for-now with no-go portfolios and make dependents
    bounded until the admission is retired by a retained derivation.
    """
    global _TIER_A_DERIVATION_TARGET_IDS
    if _TIER_A_DERIVATION_TARGET_IDS is None:
        data = tier_a_admissions_data()
        _TIER_A_DERIVATION_TARGET_IDS = set((data.get("derivation_targets") or {}).keys())
    return _TIER_A_DERIVATION_TARGET_IDS


def admitted_convention_ids() -> set[str]:
    """Tier-A convention rows listed for survey completeness only."""
    global _TIER_A_CONVENTION_IDS
    if _TIER_A_CONVENTION_IDS is None:
        data = tier_a_admissions_data()
        _TIER_A_CONVENTION_IDS = set((data.get("conventions") or {}).keys())
    return _TIER_A_CONVENTION_IDS


def tier_a_admission_ids() -> set[str]:
    """All Tier-A accepted non-axiom premises."""
    return admitted_derivation_target_ids()


def accepted_premise_ids() -> set[str]:
    """Ids accepted as chain-satisfying premises."""
    return axiom_premise_ids() | owner_governed_premise_ids() | tier_a_admission_ids()


def is_axiom_premise(dep_id: str) -> bool:
    return dep_id in axiom_premise_ids()


def is_owner_governed_premise(dep_id: str) -> bool:
    return dep_id in owner_governed_premise_ids()


def is_admitted_derivation_target(dep_id: str) -> bool:
    return dep_id in admitted_derivation_target_ids()


def is_admitted_convention(dep_id: str) -> bool:
    return dep_id in admitted_convention_ids()


def is_tier_a_admission(dep_id: str) -> bool:
    return dep_id in tier_a_admission_ids()


def is_accepted_premise_dep(dep_id: str) -> bool:
    """True if dep_id is an accepted premise.

    Such a dep satisfies chain closure even though its own effective_status is
    not retained-grade. The citing row must still pass its own independent
    audit. Axiom/primitive premises do not bound downstream rows;
    `compute_effective_status` separately downgrades rows that depend on Tier-A
    derivation targets to `retained_bounded`.
    """
    return dep_id in accepted_premise_ids()


def _reset_cache_for_tests() -> None:
    global _AXIOM_PREMISE_IDS, _OWNER_GOVERNED_PREMISE_IDS, _TIER_A_DATA
    global _TIER_A_DERIVATION_TARGET_IDS, _TIER_A_CONVENTION_IDS
    _AXIOM_PREMISE_IDS = None
    _OWNER_GOVERNED_PREMISE_IDS = None
    _TIER_A_DATA = None
    _TIER_A_DERIVATION_TARGET_IDS = None
    _TIER_A_CONVENTION_IDS = None
