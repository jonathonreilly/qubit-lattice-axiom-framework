#!/usr/bin/env python3
"""Premise-surface verifier for the post-2026-07-04 record-formation boundary.

The old no-occurrence target is false on the current axiom surface because the
Record axiom now says "Records form."
The surviving no-go is narrower: the minimal axioms do not supply a formation
rule/process/site/choice/weight/rate/clock/comparability selector.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PREMISE_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def has_any(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def main() -> int:
    axiom_text = AXIOMS.read_text(encoding="utf-8")
    premise_payload = json.loads(PREMISE_NODES.read_text(encoding="utf-8"))
    premise_note = premise_payload["nodes"]["minimal_axioms"]["note"]

    print("=" * 78)
    print("NO-GO: formation rule/process is not supplied by the minimal axioms")
    print("=" * 78)

    print("\n-- occurrence is now axiom content --")
    check(
        "Record axiom contains the occurrence sentence",
        "Records form." in axiom_text,
        "generic occurrence supplied",
    )
    check(
        "premise registry mirrors occurrence",
        "records form;" in premise_note,
        "minimal_axioms node includes occurrence content",
    )

    print("\n-- formation rule/process remains outside axioms --")
    required_boundary_phrases = [
        "formation rules",
        "admissible possibility a new record locks",
        "at which site",
        "with what weight",
        "at what rate",
        "record-production dynamics",
        "time metric",
    ]
    for phrase in required_boundary_phrases:
        check(
            f"open-gates boundary contains: {phrase}",
            phrase in axiom_text,
        )

    registry_boundary_phrases = [
        "formation rule (which admissible possibility a new record locks, at which site, with what weight, or at what rate)",
        "record-production process",
        "state-selection rule",
    ]
    for phrase in registry_boundary_phrases:
        check(
            f"premise registry boundary contains: {phrase}",
            phrase in premise_note,
        )

    print("\n-- no hidden default selector appears in the premise text --")
    forbidden_defaults = [
        "uniform formation rate",
        "default formation rate",
        "equal formation weight",
        "chosen formation site",
        "canonical formation site",
        "formation probability",
        "transition kernel",
        "one configuration of records",
        "single configuration of records",
    ]
    check(
        "axiom text contains no default formation selector/rate/weight/comparability phrase",
        not has_any(axiom_text, forbidden_defaults),
    )
    check(
        "premise registry contains no default formation selector/rate/weight/comparability phrase",
        not has_any(premise_note, forbidden_defaults),
    )

    print("\n-- underdetermination witness family --")
    admissible_local_possibilities = {
        "x": ["p", "q"],
        "y": ["p", "q"],
    }
    supplied_extension_a = {
        "first_site": "x",
        "locks": "p",
        "relative_weight": "not supplied by axioms",
        "rate": "not supplied by axioms",
    }
    supplied_extension_b = {
        "first_site": "y",
        "locks": "q",
        "relative_weight": "not supplied by axioms",
        "rate": "not supplied by axioms",
    }
    a_locks_admissible = supplied_extension_a["locks"] in admissible_local_possibilities[supplied_extension_a["first_site"]]
    b_locks_admissible = supplied_extension_b["locks"] in admissible_local_possibilities[supplied_extension_b["first_site"]]
    extensions_differ = supplied_extension_a != supplied_extension_b
    check(
        "two supplied extensions can both contain a forming record while selecting different site/possibility data",
        a_locks_admissible and b_locks_admissible and extensions_differ,
        "occurrence shared; rule content differs",
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: post-append formation-rule boundary check FAILED.")
        return 1
    print(
        "VERDICT: generic record occurrence is axiom content, but the minimal "
        "axioms do NOT supply a formation rule/process/site/choice/weight/rate/"
        "clock/comparability selector. Downstream uses of such content must cite "
        "a separate derivation, bridge, explicit admission, or approved primitive."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
