#!/usr/bin/env python3
"""Verify the repaired parameterized EW color-projection algebra.

This runner is intentionally lightweight: it checks the exact SU(3)
dimension arithmetic, the one-parameter K_EW(kappa) family, and source-note
scope discipline. It does not attempt to derive or admit kappa_EW = 0.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "YT_EW_COLOR_PROJECTION_THEOREM.md"
CLAIM_ID = "yt_ew_color_projection_theorem"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS (A)" if ok else "FAIL (A)"
    print(f"  [{tag}] {label}  ({detail})")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def k_ew(nc: int, kappa: Fraction) -> Fraction:
    f_adj = Fraction(nc * nc - 1, nc * nc)
    return Fraction(1, 1) / (f_adj + kappa * (1 - f_adj))


note_text = NOTE_PATH.read_text(encoding="utf-8")

section("Part 1: source-note scope firewall")

required = [
    "parameterized-algebra audit repair 2026-05-25",
    "bounded parameterized EW-normalization algebra support theorem",
    "kappa_EW` is a formal parameter here, not an admitted value",
    "The specialization `kappa_EW = 0`, and hence `K_EW = 9/8`, is recorded",
    "only as a diagnostic specialization outside the theorem scope",
    "Primary runner:** `scripts/frontier_yt_ew_color_projection_parameterized.py`",
    "Context authorities (not load-bearing one-hop deps for this repaired row)",
    "Formal parameter boundary (not an admission)",
    "The repaired theorem does not derive or admit",
    "Physical EW readout claims require an additional selector theorem",
]
for needle in required:
    check(f"contains: {needle!r}", needle in note_text)

forbidden = [
    "kappa_EW = 0   (admission)",
    "conditional on the admission",
    "not an unconditional theorem of this note",
    "[EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md]",
    "[EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md]",
]
for needle in forbidden:
    check(f"avoids old load-bearing/admission wording: {needle!r}", needle not in note_text)

section("Part 2: exact SU(N_c) dimension arithmetic")

for nc in [2, 3, 4, 5, 10]:
    f_adj = Fraction(nc * nc - 1, nc * nc)
    check(
        f"F_adj({nc}) = (N_c^2 - 1)/N_c^2",
        f_adj == 1 - Fraction(1, nc * nc),
        detail=str(f_adj),
    )

f_adj_3 = Fraction(3 * 3 - 1, 3 * 3)
check("F_adj(3) = 8/9", f_adj_3 == Fraction(8, 9), detail=str(f_adj_3))

section("Part 3: exact K_EW(kappa) family")

samples = {
    Fraction(0, 1): Fraction(9, 8),
    Fraction(1, 1): Fraction(1, 1),
    Fraction(1, 2): Fraction(18, 17),
    Fraction(2, 1): Fraction(9, 10),
}
for kappa, expected in samples.items():
    observed = k_ew(3, kappa)
    check(
        f"K_EW(kappa={kappa}) exact",
        observed == expected,
        detail=f"observed={observed}, expected={expected}",
    )

check(
    "K_EW(kappa) is positive for kappa >= 0 over sampled range",
    all(k_ew(3, Fraction(i, 4)) > 0 for i in range(0, 17)),
)
check(
    "K_EW(kappa) is strictly decreasing over sampled nonnegative range",
    all(k_ew(3, Fraction(i, 4)) > k_ew(3, Fraction(i + 1, 4)) for i in range(0, 16)),
)

section("Part 4: universal factor preserves sin^2(theta_W)")

g1_sq = Fraction(1, 5)
g2_sq = Fraction(1, 4)
baseline = g1_sq / (g1_sq + g2_sq)
for kappa in [Fraction(0, 1), Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)]:
    factor = k_ew(3, kappa)
    shifted = (g1_sq * factor) / (g1_sq * factor + g2_sq * factor)
    check(
        f"sin^2 invariant at kappa={kappa}",
        shifted == baseline,
        detail=f"baseline={baseline}, shifted={shifted}",
    )

section("Part 5: live audit row after pipeline")

ledger = json.loads((ROOT / "docs" / "audit" / "data" / "audit_ledger.json").read_text())
row = ledger["rows"].get(CLAIM_ID)
check(f"{CLAIM_ID} seeded", row is not None)
if row is not None:
    deps = set(row.get("deps", []))
    check("claim type remains bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("repaired row has no load-bearing markdown deps", deps == set(), detail=f"deps={sorted(deps)}")

print(f"\n{'=' * 88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'=' * 88}")
sys.exit(1 if FAIL else 0)
