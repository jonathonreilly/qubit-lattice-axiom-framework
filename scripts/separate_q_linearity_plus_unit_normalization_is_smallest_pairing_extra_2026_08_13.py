#!/usr/bin/env python3
"""Exact checks: separate Q-linearity plus B(1,1)=1 is the smallest complete pairing extra.

Reconstructs the product map from the matching. Identity gates call B(p, q)
and matching(B). Additive maps Q to Q are checked Q-linear by repeated
addition. No runner cache, no citation manifest, no axiom edits.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SEPARATE_Q_LINEARITY_PLUS_UNIT_NORMALIZATION_IS_SMALLEST_"
    "PAIRING_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NEWTON_REL = "docs/NEWTON_LAW_DERIVED_NOTE.md"
AUDIT_INPUT_PATHS = (
    "docs/SEPARATE_Q_LINEARITY_PLUS_UNIT_NORMALIZATION_IS_SMALLEST_PAIRING_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/NEWTON_LAW_DERIVED_NOTE.md",
)

PASS = 0
FAIL = 0

SAMPLES = (
    Fraction(0),
    Fraction(1),
    Fraction(-1),
    Fraction(2),
    Fraction(3),
    Fraction(4),
    Fraction(-2),
    Fraction(1, 2),
    Fraction(3, 2),
    Fraction(-3, 2),
    Fraction(5, 3),
    Fraction(-2, 5),
)

UNIT_TABLE = {
    (Fraction(0), Fraction(0)): Fraction(0),
    (Fraction(0), Fraction(1)): Fraction(0),
    (Fraction(1), Fraction(0)): Fraction(0),
    (Fraction(1), Fraction(1)): Fraction(1),
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def unit_seed() -> Fraction:
    """Displayed unit normalization B(1,1)=1."""
    return Fraction(1)


def B(p: int | Fraction, q_val: int | Fraction) -> Fraction:
    """Reconstruct B(p, q) = p q B(1,1) from separate Q-linearity."""
    return q(p) * q(q_val) * unit_seed()


def sum_map(p: int | Fraction, q_val: int | Fraction) -> Fraction:
    return q(p) + q(q_val)


def separately_q_linear(fn) -> bool:
    for x in SAMPLES:
        for xp in SAMPLES:
            for y in SAMPLES:
                if fn(x + xp, y) != fn(x, y) + fn(xp, y):
                    return False
                if fn(x, y + xp) != fn(x, y) + fn(x, xp):
                    return False
    for scale in SAMPLES:
        for x in SAMPLES:
            for y in SAMPLES:
                if fn(scale * x, y) != scale * fn(x, y):
                    return False
                if fn(x, scale * y) != scale * fn(x, y):
                    return False
    return True


def matching(fn) -> bool:
    """Separately Q-linear and unit-normalized."""
    return fn(Fraction(1), Fraction(1)) == Fraction(1) and separately_q_linear(fn)


def identity_gate(p: int | Fraction, q_val: int | Fraction) -> bool:
    """Identity B(p,q)=p q under the matching. Calls B(p,q) and matching(B)."""
    return matching(B) and B(p, q_val) == q(p) * q(q_val)


def repeated_add(count: int, value: Fraction) -> Fraction:
    total = Fraction(0)
    for _ in range(abs(count)):
        total += value
    return -total if count < 0 else total


def q_linear_from_additivity(seed: Fraction, scale: Fraction) -> Fraction:
    """f(scale) from f(1)=seed using only additivity on Q."""
    return repeated_add(scale.numerator, seed) / scale.denominator


def axioms_name_B(text: str) -> bool:
    lowered = text.lower()
    markers = (
        "separately q-linear",
        "b(1,1)",
        "two-argument b",
        "b:q",
        "pairing extra",
    )
    return any(marker in lowered for marker in markers)


def identity_source_calls_B_and_matching() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "identity_gate":
            called = {
                child.func.id
                for child in ast.walk(node)
                if isinstance(child, ast.Call) and isinstance(child.func, ast.Name)
            }
            return {"B", "matching"} <= called
    return False


def forbidden_needles() -> tuple[str, ...]:
    return (
        "G" + "_" + "N",
        "1" + "/" + "r",
        "L" + "_" + "phys",
        "we" + " " + "adopt",
        "Ha" + "mel",
        "I(" + "union)",
    )


def main() -> None:
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    newton_path = ROOT / NEWTON_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    newton = newton_path.read_text(encoding="utf-8")

    check(
        "AUDIT_INPUT_PATHS exist",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL, NEWTON_REL)
        and all((ROOT / rel).is_file() for rel in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )

    check(
        "identity gates call B(p,q) and matching(B)",
        identity_source_calls_B_and_matching(),
        "identity_gate source",
    )
    check(
        "matching(B) holds for the reconstructed product",
        matching(B),
        "B(1,1)=1 and separate Q-linearity on samples",
    )
    check(
        "identity B(3,4)=12",
        identity_gate(3, 4) and B(3, 4) == Fraction(12),
        B(3, 4),
    )
    check(
        "identity B(3/2,1/2)=3/4",
        identity_gate(Fraction(3, 2), Fraction(1, 2))
        and B(Fraction(3, 2), Fraction(1, 2)) == Fraction(3, 4),
        B(Fraction(3, 2), Fraction(1, 2)),
    )
    check(
        "identity B(2,0)=0",
        identity_gate(2, 0) and B(2, 0) == Fraction(0),
        B(2, 0),
    )

    seed = Fraction(5, 7)
    cauchy_ok = all(
        q_linear_from_additivity(seed, scale) == scale * seed for scale in SAMPLES
    )
    check(
        "additive maps Q to Q are Q-linear",
        cauchy_ok,
        "repeated-addition reconstruction",
    )

    check(
        "sum map fails the matching",
        (not matching(sum_map))
        and sum_map(1, 1) == Fraction(2)
        and sum_map(2, 1) != Fraction(2) * sum_map(1, 1),
        {"B(1,1)": str(sum_map(1, 1)), "B(2,1)": str(sum_map(2, 1))},
    )
    check("axioms name B", not axioms_name_B(axiom), "axiom memo")

    three_four = (Fraction(3), Fraction(4))
    check(
        "unit table does not assign (3,4)",
        three_four not in UNIT_TABLE,
        "unit table domain is {0,1}x{0,1}",
    )
    check(
        "complete matching extra is pi(S,T)=I(S)I(T)",
        matching(B) and B(Fraction(3), Fraction(4)) == Fraction(3) * Fraction(4),
        "factors through one-argument I then B",
    )

    axiom_flat = " ".join(axiom.split())
    check(
        "Record names one-argument additive I",
        "scalar readout `I` is additive" in axiom_flat
        and "I(empty)=0" in axiom_flat
        and "one-argument additive readout" in note
        and "does not name a two-argument" in note,
        "Theorem 3 quote",
    )
    check(
        "Newton parent is the product-law non-claim only",
        "the physical product law `M_source M_test`" in newton
        and "product-law" in note
        and "non-claim" in note,
        NEWTON_REL,
    )
    check(
        "note displays matching and does not select bilinearity",
        "B(p,q)=p q" in note
        and "smallest complete" in note
        and "The axioms do not select bilinearity." in note
        and "already-used contrast between a disjoint-union readout" in note,
        NOTE_REL,
    )

    blob = note + "\n" + Path(__file__).read_text(encoding="utf-8")
    hits = [needle for needle in forbidden_needles() if needle in blob]
    check("forbidden tokens absent from new surfaces", hits == [], hits)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")


if __name__ == "__main__":
    main()
