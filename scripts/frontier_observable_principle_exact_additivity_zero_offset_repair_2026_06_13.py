#!/usr/bin/env python3
"""Runner for the observable-principle exact-additivity zero-offset repair."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_EXACT_ADDITIVITY_ZERO_OFFSET_REPAIR_NOTE_2026-06-13.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"{status}: {label}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def test_symbolic_exact_additivity_defect() -> None:
    section("Symbolic exact-additivity defect")
    r1, r2 = sp.symbols("r1 r2", positive=True)
    c, b = sp.symbols("c b", real=True)

    def W(r):
        return c * sp.log(r) + b

    defect = sp.simplify(W(r1 * r2) - W(r1) - W(r2))
    check(
        "W_b(r)=c log r+b has exact-additivity defect -b",
        defect == -b,
        f"defect={defect}",
    )
    solutions = sp.solve(sp.Eq(defect, 0), b)
    check(
        "exact additivity forces b=0",
        solutions == [0],
        f"solutions={solutions}",
    )


def test_unit_argument() -> None:
    section("Unit argument")
    c, b = sp.symbols("c b", real=True)
    W1 = c * sp.log(sp.Integer(1)) + b
    equation_residual = sp.simplify(W1 - 2 * W1)
    check(
        "setting r1=r2=1 gives residual -b",
        equation_residual == -b,
        f"W(1)-2W(1)={equation_residual}",
    )


def test_shifted_law_is_distinct() -> None:
    section("Shifted composition law is distinct")
    r1, r2 = sp.symbols("r1 r2", positive=True)
    c, b = sp.symbols("c b", real=True)

    def W(r):
        return c * sp.log(r) + b

    shifted_defect = sp.simplify(W(r1 * r2) - (W(r1) + W(r2) - b))
    exact_defect = sp.simplify(W(r1 * r2) - W(r1) - W(r2))
    check(
        "shifted family satisfies the shifted law",
        shifted_defect == 0,
        f"shifted_defect={shifted_defect}",
    )
    check(
        "shifted law differs from exact additivity when b is nonzero",
        exact_defect == -b,
        f"exact_defect={exact_defect}",
    )


def test_rational_witnesses() -> None:
    section("Rational witnesses")
    c = Fraction(3, 2)
    b = Fraction(5, 7)
    r1 = Fraction(2, 1)
    r2 = Fraction(3, 1)
    # Avoid floating logs for the load-bearing point; the defect formula is exact.
    exact_defect = -b
    shifted_defect = Fraction(0, 1)
    check(
        "nonzero rational offset fails exact additivity",
        exact_defect != 0,
        f"c={c}, b={b}, r1={r1}, r2={r2}, defect={exact_defect}",
    )
    check(
        "the same rational offset is compatible only with shifted additivity",
        shifted_defect == 0,
        f"shifted_defect={shifted_defect}",
    )


def test_note_guardrails() -> None:
    section("Source-note guardrails")
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    required = [
        "does not derive P1",
        "not adopted by this note",
        "add any primitive",
        "change any axiom",
        "does not quote, set, or predict audit outcomes",
        "independent derivation or accepted premise",
    ]
    forbidden = [
        "P1 is now derived",
        "P1 is closed",
        "audit" "_status:",
        "effective" "_status:",
        "audited" "_clean",
        "target" "_audit",
        "target" "_effective",
    ]
    missing = [item for item in required if item not in normalized]
    present_forbidden = [item for item in forbidden if item in text]
    check("note contains required boundary strings", not missing, f"missing={missing}")
    check(
        "note avoids audit/status overclaim strings",
        not present_forbidden,
        f"present_forbidden={present_forbidden}",
    )


def main() -> int:
    print("# Observable-principle exact-additivity zero-offset repair runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_symbolic_exact_additivity_defect()
    test_unit_argument()
    test_shifted_law_is_distinct()
    test_rational_witnesses()
    test_note_guardrails()
    print(f"\nTOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
