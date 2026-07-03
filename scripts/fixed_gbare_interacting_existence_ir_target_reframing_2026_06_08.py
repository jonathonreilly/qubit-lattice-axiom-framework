#!/usr/bin/env python3
"""Fixed-g_bare interacting-existence target reframing.

Source note:
  docs/FIXED_GBARE_INTERACTING_EXISTENCE_IR_TARGET_REFRAMING_BOUNDED_NOTE_2026-06-08.md

This narrowed runner addresses the 2026-06-09 conditional audit repair target:
the earlier packet mixed a clean fixed-g_bare target clarification with imported
standard two-loop/asymptotic-scaling diagnostics. This runner removes those
diagnostics from the retained surface.

Load-bearing statement checked here:
  * the current ledger records the g_bare derivation row as retained_bounded;
  * on that scoped Wilson surface, g_bare=1 and N_c=3 give beta=6 by the
    algebra beta = 2 N_c / g_bare^2;
  * g_bare=1 is a fixed nonzero coupling, not the zero-coupling endpoint;
  * the interacting-existence target is therefore the fixed-lattice IR
    gap/clustering problem at beta=6, with Delta_gauge(beta=6)>0 still open.

No standard RG formula, two-loop coefficient, asymptotic-scaling formula, or
dimensional-transmutation estimate is load-bearing in this restricted packet.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
NOTE = ROOT / "docs" / "FIXED_GBARE_INTERACTING_EXISTENCE_IR_TARGET_REFRAMING_BOUNDED_NOTE_2026-06-08.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def row(claim_id: str) -> dict:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    return data["rows"][claim_id]


def section(title: str) -> None:
    print("=" * 78)
    print(title)
    print("=" * 78)


section("Part 1  Retained bounded dependencies for the fixed-g_bare surface")
g_bare_row = row("g_bare_derivation_note")
gap_row = row("interacting_transfer_matter_gap_and_gauge_reduction_bounded_note_2026-05-30")

check(
    "G_BARE parent is retained_bounded in the current ledger",
    g_bare_row.get("effective_status") == "retained_bounded",
    f"effective_status={g_bare_row.get('effective_status')}",
)
check(
    "G_BARE parent is audited as a bounded_theorem, not an unbounded positive theorem",
    g_bare_row.get("audit_status") == "audited_clean"
    and g_bare_row.get("claim_type") == "bounded_theorem",
    f"audit_status={g_bare_row.get('audit_status')}, claim_type={g_bare_row.get('claim_type')}",
)
check(
    "interacting transfer note is retained_bounded for the matter-sector floor dependency",
    gap_row.get("effective_status") == "retained_bounded",
    f"effective_status={gap_row.get('effective_status')}",
)

section("Part 2  Fixed Wilson-surface algebra")
g_bare = 1.0
nc = 3
beta = 2 * nc / (g_bare * g_bare)

check("beta = 2 N_c / g_bare^2 gives beta=6 for N_c=3, g_bare=1",
      abs(beta - 6.0) < 1e-12, f"beta={beta}")
check("g_bare=1 is fixed and nonzero", g_bare == 1.0 and g_bare != 0.0)
check("the zero-coupling endpoint is not taken on this fixed surface", abs(g_bare - 0.0) > 1e-12)

section("Part 3  Source note scope guard")
note = NOTE.read_text(encoding="utf-8")
required = [
    "No standard RG formula",
    "no two-loop coefficient",
    "asymptotic-scaling formula",
    "Delta_gauge(beta=6)>0",
    "fixed-lattice IR gap/clustering",
]
for marker in required:
    check(f"source note contains narrowed-scope marker: {marker}", marker in note)

for forbidden in [
    "b_1=26",
    "two-loop/one-loop diagnostic",
    "finite dimensional-transmutation scale",
    "mu_conf/mu_lattice",
]:
    check(f"source note no longer carries load-bearing RG diagnostic: {forbidden}",
          forbidden not in note)

section("Part 4  Target reframing")
print("   FIXED SURFACE: retained_bounded g_bare=1, beta=6.")
print("   TARGET: fixed-lattice IR mass gap / clustering at beta=6.")
print("   OPEN: Delta_gauge(beta=6)>0 and coupled spectral control.")
print("   REMOVED: two-loop/asymptotic-scaling diagnostic as load-bearing support.")
check(
    "reframing is bounded and does not assert interacting existence",
    "does not prove" in note and "does not solve" in note and "pure-gauge gap remains open" in note,
)

print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: This packet is a framework-native fixed-g_bare target clarification.")
print("  It depends on the retained_bounded G_BARE surface and does not import")
print("  two-loop RG, asymptotic-scaling, or dimensional-transmutation arithmetic.")
print("  The open science target remains Delta_gauge(beta=6)>0 plus full coupled")
print("  IR spectral control. No new axiom, primitive, or audit verdict.")
print("runner_check_breakdown = {A: %d, B: 0, C: 0, D: 0, total_pass: %d}" % (PASS, PASS))
if FAIL:
    raise SystemExit(1)
