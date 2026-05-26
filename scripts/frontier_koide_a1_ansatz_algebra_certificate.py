#!/usr/bin/env python3
"""Exact algebra certificate for the Koide A1 quartic-ansatz row."""

from __future__ import annotations

from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/KOIDE_A1_LOOP_FINAL_STATUS_2026-04-22.md"

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
    required = [
        "bounded support theorem",
        "admitted quartic ansatz",
        "input ansatz for this certificate",
        "Downstream use of this row must carry the ansatz premise explicitly",
        "a derivation of the quartic ansatz from the minimal axiom surface",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "Headline admission",
        "Theoretical status",
        "Rigorously established",
        "Route A (RECOMMENDED)",
        "retained scope after narrowing",
        "CLOSED",
    ]
    for phrase in forbidden:
        check(f"note omits stale package phrase: {phrase}", phrase not in text)


def algebra_checks() -> None:
    print("\n=== Koide quartic-ansatz algebra ===")
    a, r = sp.symbols("a r", positive=True, real=True)
    tr_phi = 3 * a
    tr_phi2 = 3 * a**2 + 6 * r**2
    v0 = 2 * tr_phi**2 - 3 * tr_phi2
    v = sp.expand(v0**2)
    expected_v0 = 9 * (a**2 - 2 * r**2)
    expected_v = 81 * (a**2 - 2 * r**2) ** 2
    zero_ratio = sp.sqrt(sp.Rational(1, 2))
    c = 2 * zero_ratio
    q = sp.Rational(1, 3) + c**2 / 6

    check("trace reduction identity", sp.simplify(v0 - expected_v0) == 0, str(sp.factor(v0)))
    check("squared ansatz identity", sp.simplify(v - expected_v) == 0, str(sp.factor(v)))
    check("ansatz is an explicit square", sp.factor(v).is_Pow or str(sp.factor(v)).endswith("**2"), str(sp.factor(v)))
    check("zero-locus forward direction", sp.simplify(expected_v.subs(r, a * zero_ratio)) == 0)
    check("zero-locus ratio solves a^2=2r^2", sp.simplify(a**2 - 2 * (a * zero_ratio) ** 2) == 0)
    check("Brannen c squared is two on zero-locus", sp.simplify(c**2 - 2) == 0, str(c))
    check("formal Q expression gives two thirds", sp.simplify(q - sp.Rational(2, 3)) == 0, str(q))


def main() -> int:
    note_boundary_checks()
    algebra_checks()
    print("\nKoide quartic-ansatz algebra certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
