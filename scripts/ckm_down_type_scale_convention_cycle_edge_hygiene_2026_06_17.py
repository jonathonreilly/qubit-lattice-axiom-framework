#!/usr/bin/env python3
"""Source-edge and claim-boundary verifier for the repaired CKM scale note.

The original 2026-06-17 cycle-edge check pinned the former class-G numerical
support narrative. The 2026-07-12 source repair changes the claim itself, so
this verifier now checks the new foundation-only dependency set and the
bounded covariance firewall.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md"
RUNNER = ROOT / "scripts" / "frontier_ckm_down_type_scale_convention_support.py"
PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f" ({detail})"
    print(line)


def markdown_links(body: str) -> set[str]:
    return set(re.findall(r"\]\(([A-Za-z0-9_\-./]+\.md)\)", body))


def main() -> int:
    print("=" * 78)
    print("CKM down-type scale-convention source-edge hygiene")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    runner = RUNNER.read_text(encoding="utf-8")
    flat = " ".join(note.lower().split())
    links = markdown_links(note)

    expected_foundation = {
        "MINIMAL_AXIOMS_2026-06-29.md",
        "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    }
    co_cycle = {
        "CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
        "QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md",
        "DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
        "QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md",
    }

    check("note exists", NOTE.exists())
    check("runner exists", RUNNER.exists())
    check(
        "markdown dependencies are approved foundation notes only",
        links == expected_foundation,
        str(sorted(links)),
    )
    check("no co-cycle source edge remains", not (links & co_cycle), str(sorted(links & co_cycle)))

    required_note_phrases = [
        "bounded support theorem",
        "abstract algebraic lemma",
        "shared multiplicative transport",
        "one composite physical bridge",
        "comparator-only numerical illustration",
        "no global impossibility is claimed",
    ]
    missing_note = [phrase for phrase in required_note_phrases if phrase not in flat]
    check("new claim firewall is explicit", not missing_note, str(missing_note))

    forbidden_live_phrases = [
        "class-g numerical-match observation",
        "transport factor hard-coded to 1.14747",
        "threshold-local comparator is derived",
        "5/6 bridge is derived",
    ]
    hits = [phrase for phrase in forbidden_live_phrases if phrase in flat]
    check("former numerical-match claim is absent", not hits, str(hits))

    check(
        "runner proves shared-transport deviation invariance",
        "shared transport preserves relative deviation" in runner,
    )
    check(
        "runner separates exact and comparator pass classes",
        "EXACT_PASS" in runner and "COMPARATOR_PASS" in runner,
    )
    check(
        "runner pins the one-loop factor independently",
        "1.1625576195735408" in runner
        and "one-loop factor differs from observed-mass transport" in runner,
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
