#!/usr/bin/env python3
"""
Bounded-surface check for
docs/G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md.

This runner intentionally does not replace the shared
frontier_g_bare_derivation.py runner used by retained upstream rows. It checks
only the repaired constraint-vs-convention surface:

  CN: retained canonical trace normalization.
  WM: retained Wilson matching beta = 2 N_c / g_bare^2.
  B6: explicit local Wilson surface N_c = 3, beta = 2 N_c = 6.

It does not derive beta = 6 from A1 + A2 and does not apply an audit verdict.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return cond


def ledger_rows() -> dict:
    ledger = (
        Path(__file__).resolve().parent.parent
        / "docs"
        / "audit"
        / "data"
        / "audit_ledger.json"
    )
    return json.loads(ledger.read_text())["rows"]


def main() -> int:
    rows = ledger_rows()

    cl3_id = "cl3_color_automorphism_theorem"
    wm_id = "g_bare_rescaling_freedom_removal_theorem_note_2026-05-03"
    target_id = "g_bare_constraint_vs_convention_theorem_note_2026-05-03"

    check(
        "CN dependency is retained",
        rows.get(cl3_id, {}).get("effective_status") == "retained",
        f"{cl3_id}: {rows.get(cl3_id, {}).get('effective_status', 'missing')}",
    )
    check(
        "WM dependency is retained",
        rows.get(wm_id, {}).get("effective_status") == "retained",
        f"{wm_id}: {rows.get(wm_id, {}).get('effective_status', 'missing')}",
    )

    N_c = Fraction(3)
    beta_local = Fraction(2) * N_c
    check(
        "local Wilson surface beta = 2 N_c = 6 for SU(3) (explicit bounded input)",
        beta_local == Fraction(6),
        f"beta = {beta_local}",
    )

    g_bare_sq = Fraction(2) * N_c / beta_local
    check(
        "given CN + WM + local beta = 6, g_bare^2 = 1 forced (exact)",
        g_bare_sq == Fraction(1),
        f"g_bare^2 = 2 N_c / beta = {g_bare_sq}",
    )

    for g2_alt in [Fraction(1, 2), Fraction(2), Fraction(4)]:
        beta_alt = Fraction(2) * N_c / g2_alt
        check(
            f"alternative g^2 = {g2_alt} requires beta = {beta_alt} != 6",
            beta_alt != beta_local,
            "changes the declared local Wilson beta = 6 surface",
        )

    target = rows.get(target_id, {})
    deps = set(target.get("deps", []))
    check(
        "target row declares CN and WM as direct dependencies",
        {cl3_id, wm_id}.issubset(deps),
        f"deps = {sorted(deps)}",
    )
    print(
        "INFO target audit routing: "
        f"audit_status = {target.get('audit_status', 'missing')}; "
        f"effective_status = {target.get('effective_status', 'missing')}"
    )

    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Bounded-surface check failed.")
        return 1

    print("Bounded-surface check passed; no retained status is asserted by this runner.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
