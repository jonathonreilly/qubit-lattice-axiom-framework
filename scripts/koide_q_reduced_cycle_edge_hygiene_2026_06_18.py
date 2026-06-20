#!/usr/bin/env python3
"""Source-edge hygiene check for the Koide Q-reduced obstruction cycle.

This is not an audit runner and does not apply any verdict. It verifies that
the obstruction note can still name the parent claim as trace context without
creating a markdown dependency edge back to that parent row.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md"
PARENT_FILE = "KOIDE_Q_REDUCED_OBSERVABLE_RESTRICTION_THEOREM_2026-04-22.md"
PARENT_ID = "koide_q_reduced_observable_restriction_theorem_2026-04-22"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {name}{suffix}")


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())

    check("obstruction note exists", NOTE.exists())
    check("cycle-edge hygiene section present", "Cycle-edge hygiene (2026-06-18)" in text)
    check("parent claim id retained as context", PARENT_ID in text)
    check("parent filename not used as markdown link target", f"]({PARENT_FILE})" not in text)
    check("parent filename not used as bare markdown reference target", f"]: {PARENT_FILE}" not in text)
    check(
        "parent context is explicitly non-load-bearing",
        "context-only trace metadata, not a load-bearing dependency" in flat
        and "does not consume the parent determinant theorem as a premise" in flat,
    )
    check(
        "purpose keeps audit-review trace without markdown dependency edge",
        "parent reduced-observable restriction row" in flat
        and "(`koide_q_reduced_observable_restriction_theorem_2026-04-22`, context only)" in flat,
    )
    check(
        "obstruction proof still names live bridge residual",
        "physical charged-lepton observable carrier/readout" in flat
        and "D_red = I_2" in text,
    )
    check("no audit status authority claimed", "independent audit lane only" in flat)
    check("primary obstruction runner still cited", "frontier_koide_q_reduced_carrier_physical_identification_obstruction_2026_06_12.py" in text)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print("Koide Q-reduced obstruction edge is context-only; no audit verdict applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
