#!/usr/bin/env python3
"""Formal-ratio repair runner for the Koide Q-delta linking row.

This runner checks only the exact rational identity:

    Q_d = 2/d, Delta_d = 2/d^2  =>  Delta_d = Q_d/d.

It explicitly avoids the radian/Berry-holonomy bridge, equal-sector-norm
selector, PDG comparators, and any physical charged-lepton claim.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md"
TARGET_CITATION = "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md"
CACHE_PATH = ROOT / "logs" / "runner-cache" / "frontier_koide_q_delta_formal_ratio_repair.txt"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def q_d(d: int) -> Fraction:
    return Fraction(2, d)


def delta_d(d: int) -> Fraction:
    return Fraction(2, d * d)


def q_alt(d: int) -> Fraction:
    return Fraction(d - 1, d)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    required = [
        "bounded-support formal algebra",
        "No Berry-holonomy radian bridge",
        "That exact rational identity is the entire repaired theorem.",
        "This repair withdraws both from the binding claim.",
        "The bridge from this formal algebra to physical Koide/Brannen geometry remains a separate open science problem.",
        "Citation firewall (2026-06-18)",
        "Direct citations to this note are allowed only for the definition-level",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in text)

    forbidden = [
        "uses PDG",
        "matches observed",
        "observed charged-lepton",
        "retained selected-line",
        "Berry holonomy in radians is derived",
        "equal-sector-norm input is retained",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim/token: {needle!r}", needle not in text)


def is_source_scan_path(path: Path) -> bool:
    if path == NOTE_PATH or path == Path(__file__).resolve() or path == CACHE_PATH:
        return False
    rel = path.relative_to(ROOT)
    rel_s = rel.as_posix()
    if path.suffix not in {".md", ".py"}:
        return False
    if rel_s.startswith("docs/audit/"):
        return False
    if rel.name == "KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20_NOTE_2026-05-17.md":
        return False
    if rel_s.startswith("docs/publication/ci3_z3/") and rel.name.endswith("_EFFECTIVE_STATUS.md"):
        return False
    if rel_s.startswith(".claude/") or rel_s.startswith("logs/"):
        return False
    return rel_s.startswith("docs/") or rel_s.startswith("scripts/")


def check_direct_citation_firewall() -> None:
    section("Direct citation firewall")
    allowed_markers = [
        "formal identity",
        "formal-only",
        "definition-level",
        "formal ratio",
        "formal q-delta identity",
        "formal q_d/delta_d identity",
        "formal delta_d = q_d/d",
        "context only",
        "reader context only",
        "not load-bearing",
        "not consumed",
        "does not close",
        "does not derive",
        "not derive",
        "remains open",
        "open",
        "conditional",
        "blocked",
        "no-go",
        "historical pre-repair",
        "historical/non-authority",
        "no retained physical",
        "current repaired note is formal-only",
        "under audit",
        "not promoted",
        "not closed",
    ]
    forbidden_patterns = [
        ("retained physical delta", re.compile(r"retained\s+(?:`?δ|delta)\s*=\s*2/9", re.I)),
        ("retained q-delta authority", re.compile(r"retained[^.\n]{0,80}q[-_ ]?delta", re.I)),
        ("partial physical closure", re.compile(r"partial closure", re.I)),
        ("PDG comparator", re.compile(r"matches observed|observed-mass comparator", re.I)),
        ("charged-lepton offset authority", re.compile(r"physical charged-lepton offset", re.I)),
        ("live radian-bridge authority", re.compile(r"original site naming|names primitive `?P`?|§4", re.I)),
    ]

    citation_count = 0
    for root in [ROOT / "docs", ROOT / "scripts"]:
        for path in sorted(root.rglob("*")):
            if not is_source_scan_path(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if TARGET_CITATION not in text:
                continue
            rel = path.relative_to(ROOT).as_posix()
            lines = text.splitlines()
            for idx, line in enumerate(lines):
                if TARGET_CITATION not in line:
                    continue
                citation_count += 1
                lo = max(0, idx - 4)
                hi = min(len(lines), idx + 5)
                window = "\n".join(lines[lo:hi])
                lower = window.lower()
                has_allowed_marker = any(marker in lower for marker in allowed_markers)
                forbidden_hits = [label for label, pattern in forbidden_patterns if pattern.search(window)]
                check(
                    f"{rel}:{idx + 1} citation is explicitly formal/open/contextual",
                    has_allowed_marker,
                    "" if has_allowed_marker else "window lacks a formal/open/context marker",
                )
                check(
                    f"{rel}:{idx + 1} citation avoids forbidden authority language",
                    not forbidden_hits,
                    "" if not forbidden_hits else ", ".join(forbidden_hits),
                )
    check("at least one direct citation was scanned", citation_count > 0, f"citations={citation_count}")


def check_exact_identity() -> None:
    section("Exact rational identity")
    for d in [1, 2, 3, 4, 5, 7, 11, 17, 32]:
        q = q_d(d)
        delta = delta_d(d)
        check(f"d={d}: Delta_d = Q_d/d", delta == q / d, f"Delta={delta}, Q/d={q/d}")
        check(f"d={d}: Delta_d/Q_d = 1/d", delta / q == Fraction(1, d), f"ratio={delta/q}")


def check_d3_values() -> None:
    section("d=3 exact values")
    check("Q_3 = 2/3", q_d(3) == Fraction(2, 3), str(q_d(3)))
    check("Delta_3 = 2/9", delta_d(3) == Fraction(2, 9), str(delta_d(3)))
    check("Delta_3 / Q_3 = 1/3", delta_d(3) / q_d(3) == Fraction(1, 3), str(delta_d(3) / q_d(3)))


def check_negative_control() -> None:
    section("Negative control: alternative Q'_d=(d-1)/d")
    for d in [2, 4, 5, 7, 11, 17]:
        check(
            f"d={d}: alternative Q'_d/d does not equal Delta_d",
            delta_d(d) != q_alt(d) / d,
            f"Delta={delta_d(d)}, Q_alt/d={q_alt(d)/d}",
        )
    check("d=3 is the unique tested coincidence for Q'_d=2/d", q_alt(3) == q_d(3), f"Q_alt(3)={q_alt(3)}")


def main() -> int:
    print("Koide Q-delta formal ratio repair")
    check_note_boundary()
    check_direct_citation_firewall()
    check_exact_identity()
    check_d3_values()
    check_negative_control()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
