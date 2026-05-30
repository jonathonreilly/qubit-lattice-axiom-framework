#!/usr/bin/env python3
"""Open-gate certificate for the charged-lepton Koide packet."""

from __future__ import annotations

from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_boundary_checks() -> None:
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    required = [
        "Claim type:** open_gate",
        "Status:** open gate",
        "two remaining charged-lepton Koide gates",
        "Koide surface selection gate",
        "Brannen phase identification gate",
        "does not claim",
        "any new axiom or audit verdict",
        "open-gate map",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in normalized)

    forbidden = [
        "current support packet",
        "authoritative support surface",
        "clean enough for package use",
        "conditional closure",
        "promoted on the current package surface",
        "retained closure",
        "retained promotion",
    ]
    for phrase in forbidden:
        check(f"note omits stale package phrase: {phrase}", phrase not in text)


def algebra_checks() -> None:
    print("\n=== charged-lepton Koide gate algebra ===")
    c, q, delta = sp.symbols("c q delta", real=True)
    q_expr = sp.Rational(1, 3) + c**2 / 6
    c2_at_target = sp.solve(sp.Eq(q_expr, sp.Rational(2, 3)), c**2)[0]
    r_over_a_sq = c2_at_target / 4
    delta_expr = q / 3

    check("Q target solves c^2=2", sp.simplify(c2_at_target - 2) == 0, str(c2_at_target))
    check("Q target solves r^2/a^2=1/2", sp.simplify(r_over_a_sq - sp.Rational(1, 2)) == 0, str(r_over_a_sq))
    check("c^2=2 implies Q=2/3", sp.simplify(q_expr.subs(c**2, 2) - sp.Rational(2, 3)) == 0)
    check("delta=Q/3 sends Q=2/3 to 2/9", sp.simplify(delta_expr.subs(q, sp.Rational(2, 3)) - sp.Rational(2, 9)) == 0)
    check("delta=2/9 is equivalent to Q=2/3 under delta=Q/3", sp.simplify(3 * sp.Rational(2, 9) - sp.Rational(2, 3)) == 0)
    check("Brannen phase bridge is a declared extra rule", "delta := Q/3" in NOTE.read_text(encoding="utf-8"), kind="B")


def main() -> int:
    note_boundary_checks()
    algebra_checks()
    print("\nCharged-lepton Koide two-gate open certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
