#!/usr/bin/env python3
"""Firewall runner for the fractional-instanton action-core split.

The audited conditional parent mixes a safe fractional charge/action algebra
core with external dilute-gas determinant, measure, coupling-scale,
convergence, and condensate-regime data.  This runner checks the narrow
source-side split: the action core is bounded support over the retained-bounded
topological instanton infrastructure, while the dilute-gas/condensate pieces
remain open external model-regime inputs.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "FRACTIONAL_INSTANTON_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)


def ledger_status(claim_id: str) -> str | None:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = rows.get(claim_id, {})
    return row.get("effective_status") or row.get("audit_status")


def s_frac_coeff(k: int, n: int) -> Fraction:
    """Coefficient c where S_frac = c*pi^2/g^2."""
    return Fraction(8 * abs(k), n)


def boltzmann_at_g2_one(k: int, n: int) -> float:
    return math.exp(-float(s_frac_coeff(k, n)) * math.pi**2)


def main() -> int:
    print("FRACTIONAL INSTANTON ACTION-CORE SPLIT")
    print("=" * 72)

    statuses = {
        "topological_instanton_textbook_infrastructure_import_note_2026-05-17":
            ledger_status("topological_instanton_textbook_infrastructure_import_note_2026-05-17"),
        "instanton_4d_action_8pi2_over_g2_external_narrow_theorem_note_2026-05-16":
            ledger_status("instanton_4d_action_8pi2_over_g2_external_narrow_theorem_note_2026-05-16"),
    }
    check(
        "upstream action/fractional-charge authorities are retained-bounded",
        all(status == "retained_bounded" for status in statuses.values()),
        ", ".join(f"{cid}={status}" for cid, status in statuses.items()),
    )

    arithmetic_cases = {
        (1, 1): Fraction(8, 1),
        (1, 2): Fraction(4, 1),
        (1, 3): Fraction(8, 3),
        (1, 4): Fraction(2, 1),
        (2, 5): Fraction(16, 5),
    }
    bad = []
    for (k, n), expected in arithmetic_cases.items():
        got = s_frac_coeff(k, n)
        if got != expected:
            bad.append(f"k={k},N={n}: got {got}, expected {expected}")
    check(
        "fractional action coefficient is 8*|k|/N times pi^2/g^2",
        not bad,
        "; ".join(bad) if bad else "checked N=1,2,3,4 and k=2,N=5",
    )

    collapse_ok = s_frac_coeff(1, 1) == Fraction(8, 1)
    half_ok = s_frac_coeff(1, 2) == Fraction(4, 1)
    check(
        "integer and half-charge limits match BPST and half-action scales",
        collapse_ok and half_ok,
        f"N=1 coeff={s_frac_coeff(1,1)}, N=2 coeff={s_frac_coeff(1,2)}",
    )

    numeric = {
        2: (4 * math.pi**2, 7.16e-18),
        3: (8 * math.pi**2 / 3, 3.7e-12),
        4: (2 * math.pi**2, 2.7e-9),
    }
    numeric_ok = True
    details = []
    for n, (expected_s, expected_b) in numeric.items():
        got_s = float(s_frac_coeff(1, n)) * math.pi**2
        got_b = boltzmann_at_g2_one(1, n)
        numeric_ok &= abs(got_s - expected_s) < 1e-12
        numeric_ok &= abs(math.log(got_b) - math.log(expected_b)) < 0.03
        details.append(f"N={n}: S={got_s:.6g}, exp(-S)={got_b:.3g}")
    check(
        "canonical g^2=1 numerical factors reproduce the parent table",
        numeric_ok,
        "; ".join(details),
    )

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    flat_parent = " ".join(parent.split())

    check(
        "new note isolates only the action core as bounded support",
        "action core" in flat_note.lower()
        and "retained-bounded topological-instanton infrastructure" in flat_note
        and "does not derive a dilute-gas determinant" in flat_note,
    )
    check(
        "parent cites action-core note, runner, and cache",
        "FRACTIONAL_INSTANTON_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md" in parent
        and "fractional_instanton_action_core_split_2026_06_18.py" in parent
        and "fractional_instanton_action_core_split_2026_06_18.txt" in parent,
    )
    check(
        "parent preserves dilute-gas and condensate blockers",
        "it is **not** authority for the dilute-gas determinant, measure, phase-space density, coupling-scale prescription, finite-volume/temperature regime, convergence, or condensate formation" in flat_parent
        and "dilute-gas/condensate content segregated as the unsupplied bridge" in flat_parent,
    )
    check(
        "parent remains an open gate with no status promotion",
        "**Claim type:** open_gate" in parent
        and "audited_clean" not in parent
        and "proposed_retained" not in parent
        and "Status authority" in parent,
    )
    check(
        "new note forbids hierarchy and substrate closure",
        "does not identify the framework substrate" in flat_note
        and "does not close alpha_LM^16" in flat_note
        and "does not derive a hierarchy scale ratio" in flat_note,
    )

    print()
    print(
        "VERDICT: the fractional charge/action algebra is split into a "
        "bounded support core over retained-bounded topological infrastructure; "
        "dilute-gas, determinant/measure, convergence, condensate, substrate, "
        "and hierarchy bridges remain open."
    )
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
