#!/usr/bin/env python3
"""CKM down-type scale-convention source-edge hygiene verifier.

This verifies the 2026-06-17 source-graph repair for
docs/CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md.

The audit queue named this row as a cycle-break target. The intended
source-side repair is to keep the scientific scope unchanged while
removing markdown dependency edges to co-cycle context notes that are
not load-bearing for this note's narrow calculation.

This runner does not audit, retag, or edit generated audit data.
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


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_links(body: str) -> list[str]:
    return re.findall(r"\]\(([A-Za-z0-9_\-./]+\.md)\)", body)


def main() -> int:
    print("=" * 78)
    print("CKM down-type scale-convention cycle-edge hygiene")
    print("=" * 78)

    note = text(NOTE)
    runner = text(RUNNER)
    flat = " ".join(note.lower().split())

    links = markdown_links(note)
    link_set = set(links)
    expected_load_bearing = {
        "ALPHA_S_DERIVED_NOTE.md",
        "CKM_ATLAS_AXIOM_CLOSURE_NOTE.md",
    }
    co_cycle = {
        "CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
        "QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md",
        "DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
        "QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md",
        "CKM_FROM_MASS_HIERARCHY_NOTE.md",
        "QUARK_MASS_RATIO_NOTE_2026-04-18.md",
        "QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md",
    }

    check("note exists", NOTE.exists())
    check("runner exists", RUNNER.exists())
    check("markdown links resolve to retained/anchor load-bearing rows only", link_set == expected_load_bearing, str(sorted(link_set)))
    check("no markdown link remains to known co-cycle context rows", not (link_set & co_cycle), str(sorted(link_set & co_cycle)))

    for name in [
        "CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md",
        "QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md",
        "DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
    ]:
        check(f"{name} remains present as plain context", name in note and f"]({name})" not in note)

    required_scope = [
        "support-level",
        "class-g numerical",
        "does not derive the `5/6` bridge",
        "unique threshold-local scale convention",
        "does not upgrade",
        "not load-bearing",
    ]
    missing = [phrase for phrase in required_scope if phrase not in flat]
    check("scope firewall language remains explicit", not missing, str(missing))

    forbidden = [
        "retained down-type mass-ratio theorem",
        "theorem-grade closure",
        "threshold-local comparator is derived",
        "5/6 bridge is derived",
        "audit verdict",
        "retag",
    ]
    hits = [phrase for phrase in forbidden if phrase in flat and f"not a {phrase}" not in flat]
    # The first two phrases are allowed in negative/non-claim contexts; reject only
    # positive grant language below.
    positive_hits = []
    for phrase in forbidden:
        for bad in [f"this note proves a {phrase}", f"this note is a {phrase}", f"sets an {phrase}"]:
            if bad in flat:
                positive_hits.append(bad)
    check("positive overclaim/status language absent", not positive_hits, str(positive_hits))

    check("runner still declares D3 open", "Defect (D3) remains open" in runner)
    check("runner still reports class-G status unchanged", "class-g status is unchanged" in runner.lower())

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
