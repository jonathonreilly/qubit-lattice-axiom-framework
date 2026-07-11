#!/usr/bin/env python3
"""Verify the corrected AC obligation surface."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "docs" / "audit" / "scripts"))
import premise_nodes  # noqa: E402


def main() -> int:
    data = ROOT / "docs" / "audit" / "data"
    obligations = json.loads((data / "derivation_obligations.json").read_text(encoding="utf-8"))
    tier = json.loads((data / "premise_decision_history.json").read_text(encoding="utf-8"))
    ids = set(obligations.get("canonical_ids") or [])
    expected = {
        "ac_orbit_occupancy_statistical_grain_derivation_obligation",
        "ac_reta_hclass_hunit_readout_derivation_obligation",
    }
    checks = {
        "exact two AC obligations": ids == expected,
        "obligations are not supplied premises": all(
            not premise_nodes.is_accepted_premise_dep(cid) for cid in ids
        ),
        "historical live admissions remain empty": (
            tier.get("genuine_admitted_input_count") == 0
            and tier.get("canonical_ids") == []
            and tier.get("derivation_targets") == {}
        ),
        "old governance registry absent": not (data / "owner_governed_premise_nodes.json").exists(),
    }
    failed = 0
    for label, passed in checks.items():
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failed += not passed
    print(f"TOTAL: PASS={len(checks)-failed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
