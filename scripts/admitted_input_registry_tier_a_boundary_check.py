#!/usr/bin/env python3
"""Verify that historical admissions have zero premise authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "docs" / "audit" / "scripts"))
import premise_nodes  # noqa: E402

DATA = ROOT / "docs" / "audit" / "data"
HISTORY = DATA / "premise_decision_history.json"
OBLIGATIONS = DATA / "derivation_obligations.json"
FOUNDATION = DATA / "axiom_premise_nodes.json"
OLD_OWNER_REGISTRY = DATA / "owner_governed_premise_nodes.json"
OLD_ADMISSION_REGISTRY = DATA / "tier_a_admissions.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(label: str, value: bool) -> None:
        checks.append((label, bool(value)))

    history = load(HISTORY)
    obligations = load(OBLIGATIONS)
    foundation = load(FOUNDATION)
    obligation_ids = set(obligations.get("canonical_ids") or [])

    check("admission registry is absent", not OLD_ADMISSION_REGISTRY.exists())
    check("decision history is explicitly non-authoritative", "Non-authoritative" in history.get("description", ""))
    check("historical admission count is zero", history.get("genuine_admitted_input_count") == 0)
    check("historical admission ids are empty", history.get("canonical_ids") == [])
    check("historical derivation-target map is empty", history.get("derivation_targets") == {})
    check("retired governance registry is absent", not OLD_OWNER_REGISTRY.exists())
    check(
        "exact AC obligations are live",
        obligation_ids
        == {
            "ac_orbit_occupancy_statistical_grain_derivation_obligation",
            "ac_reta_hclass_hunit_readout_derivation_obligation",
        },
    )
    check(
        "foundation contains axiom plus three approved primitives",
        set(foundation.get("canonical_ids") or [])
        == {
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        },
    )
    check(
        "accepted ids equal foundation ids",
        premise_nodes.accepted_premise_ids()
        == set(foundation.get("canonical_ids") or []),
    )
    check(
        "open obligations are not supplied premises",
        all(not premise_nodes.is_accepted_premise_dep(cid) for cid in obligation_ids),
    )

    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += not passed
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
