#!/usr/bin/env python3
"""
Bounded-surface check for
docs/G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md.

This runner intentionally does not replace the shared
frontier_g_bare_derivation.py runner used by retained upstream rows. It checks
only the repaired constraint-vs-convention surface:

  CN: canonical trace normalization.
  WM: Wilson small-a matching relation beta = 2 N_c / g_bare^2.
  B6: explicit local Wilson surface N_c = 3, beta = 2 N_c = 6.

It does not derive beta = 6 from the one-qubit operator algebra plus the
Z^3 lattice, does not prove Wilson action-surface selection, and does not
apply an audit verdict.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md"
WM_NOTE = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"


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


def main() -> int:
    note_text = NOTE.read_text()
    normalized_note = " ".join(note_text.split())
    boundary_markers = [
        "conditional-support / bounded algebraic surface only",
        "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md",
        "the local Wilson coefficient surface `beta = 6` at `N_c = 3`",
        "It may not cite this row as a retained derivation of the Wilson action form",
        "conditional on that beta input",
    ]
    for marker in boundary_markers:
        check(
            f"source boundary marker present: {marker[:54]}",
            marker in normalized_note,
        )
    wm_text = WM_NOTE.read_text(encoding="utf-8")
    wm_flat = " ".join(wm_text.split())
    check(
        "Wilson small-a theorem contains beta = 2 N_c / g_bare^2",
        "beta = 2 N_c / g_bare^2" in wm_text,
    )
    check(
        "Wilson small-a theorem keeps action-surface selection outside scope",
        "does not derive that the framework must select the Wilson action surface" in wm_flat,
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
        "given CN + scoped WM + local beta = 6, g_bare^2 = 1 (exact)",
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

    print(
        "INFO scoped inputs: CN and WM are sourced by cited bounded surfaces; "
        "beta=6 remains the explicit local input. Dependency closure is owned "
        "by the audit pipeline. The source firewall forbids treating this row "
        "as a beta=6 derivation."
    )

    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Bounded-surface check failed.")
        return 1

    print("Bounded-surface check passed; no retained status is asserted by this runner.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
