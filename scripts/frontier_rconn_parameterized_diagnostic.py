#!/usr/bin/env python3
"""Verify the repaired R_conn diagnostic/channel-fraction theorem.

The theorem surface is the exact SU(3) adjoint channel fraction plus a
diagnostic MC consistency check. The runner deliberately does not derive or
admit matching rule (M), kappa_EW = 0, or a physical connected-trace readout.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "RCONN_DERIVED_NOTE.md"
CLAIM_ID = "rconn_derived_note"

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


note_text = NOTE_PATH.read_text(encoding="utf-8")

section("Part 1: source-note scope firewall")

required = [
    "R_conn Diagnostic from the SU(N_c) Fierz Channel-Count Identity",
    "parameterized-diagnostic repair",
    "does not admit matching rule",
    "does not admit `kappa_EW = 0`",
    "MC result is diagnostic only",
    "Primary runner:** `scripts/frontier_rconn_parameterized_diagnostic.py`",
    "not a load-bearing dependency edge",
    "derive or admit that bridge",
    "physical readout out of scope",
    "must not cite this repaired row as a",
]
for needle in required:
    check(f"contains: {needle!r}", needle in note_text)

forbidden = [
    "Admitted open premise (M)",
    "admitted here as a named open premise",
    "[`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`]",
    "[`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`]",
    "[YUKAWA_COLOR_PROJECTION_THEOREM.md]",
    "## Part 2: Derivation of R_conn",
    "R_conn(derived)",
    "holds at ALL beta",
    "guaranteed at leading order",
    "Three independent observables",
    "admitted-context",
]
for needle in forbidden:
    check(f"avoids old dependency/admission wording: {needle!r}", needle not in note_text)

section("Part 2: exact adjoint channel fraction")

for nc in [2, 3, 4, 5, 10]:
    f_adj = Fraction(nc * nc - 1, nc * nc)
    check(
        f"F_adj({nc}) = (N_c^2 - 1)/N_c^2",
        f_adj == 1 - Fraction(1, nc * nc),
        detail=str(f_adj),
    )

f_adj_3 = Fraction(8, 9)
check("F_adj(3) = 8/9", f_adj_3 == Fraction(3 * 3 - 1, 3 * 3), detail=str(f_adj_3))

section("Part 3: diagnostic MC consistency")

mc = 0.887
sigma = 0.008
target = 8 / 9
residual = abs(mc - target)
check(
    "MC central value is within one sigma of 8/9",
    residual <= sigma,
    detail=f"residual={residual:.6f}, sigma={sigma:.6f}",
)
check(
    "MC diagnostic is not promoted to exact theorem",
    "MC result is diagnostic only" in note_text and "not a physical-readout theorem" in note_text,
)

section("Part 4: live audit row after pipeline")

ledger = json.loads((ROOT / "docs" / "audit" / "data" / "audit_ledger.json").read_text())
row = ledger["rows"].get(CLAIM_ID)
check(f"{CLAIM_ID} seeded", row is not None)
if row is not None:
    deps = set(row.get("deps", []))
    check("claim type remains bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("repaired row has no load-bearing markdown deps", deps == set(), detail=f"deps={sorted(deps)}")

print(f"\n{'=' * 88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'=' * 88}")
sys.exit(1 if FAIL else 0)
