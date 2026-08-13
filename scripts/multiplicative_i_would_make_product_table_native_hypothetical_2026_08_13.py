#!/usr/bin/env python3
"""Exact checks for the C8 one-argument multiplicative-I counterfactual.

I_plus is current additive cardinality. I_times is the displayed
multiplicative retype. Neither is a two-argument product table.
I_times is not adopted.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "MULTIPLICATIVE_I_WOULD_MAKE_PRODUCT_TABLE_NATIVE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/MULTIPLICATIVE_I_WOULD_MAKE_PRODUCT_TABLE_NATIVE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def I_plus(n: int) -> Fraction:
    """Current additive cardinality readout: I_+(n units) = n, I_+(empty) = 0."""
    if n < 0:
        raise ValueError("unit-lock count must be nonnegative")
    return Fraction(n)


def I_times(n: int, q: Fraction) -> Fraction:
    """Counterfactual multiplicative readout: I_×(empty)=1, I_×(n units)=q^n."""
    if n < 0:
        raise ValueError("unit-lock count must be nonnegative")
    return Fraction(q) ** n


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def i_union_table() -> tuple[Fraction, Fraction, Fraction, Fraction]:
    empty = I_plus(0)
    unit_t = I_plus(1)
    unit_s = I_plus(1)
    both = I_plus(1) + I_plus(1)
    return (empty, unit_t, unit_s, both)


def pi_table() -> tuple[Fraction, Fraction, Fraction, Fraction]:
    pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
    return tuple(I_plus(n) * I_plus(m) for n, m in pairs)


def i_times_pairing_table(q: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
    return tuple(I_times(n, q) * I_times(m, q) for n, m in pairs)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS: " + ", ".join(AUDIT_INPUT_PATHS))
    print(
        "external_scientific_inputs: current Record additive wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print("I_× adoption: displayed only; not installed as axiom content")

    q_one = Fraction(1)
    n_empty = 0
    n_two = 2

    checks.check(
        "theorem-1-identities",
        "I_+(empty)=0 and I_×(empty)=1, so the identities differ",
        I_plus(n_empty) == 0 and I_times(n_empty, q_one) == 1,
    )
    checks.check(
        "mutation-empty-identities",
        "the predicate I_+(empty)=I_×(empty) fails (0≠1)",
        I_plus(n_empty) != I_times(n_empty, q_one),
    )
    checks.check(
        "theorem-2-two-units",
        "I_+(2)=2 and I_×(2,q=1)=1",
        I_plus(n_two) == 2 and I_times(n_two, q_one) == 1,
    )
    checks.check(
        "mutation-two-units-q1",
        "the predicate I_+(2)=I_×(2) for q=1 fails (2≠1)",
        I_plus(n_two) != I_times(n_two, q_one),
    )

    product_two_three = I_plus(2) * I_plus(3)
    one_arg_candidates = (
        I_plus(2),
        I_plus(3),
        I_plus(5),
        I_times(2, q_one),
        I_times(3, q_one),
        I_times(5, q_one),
    )
    checks.check(
        "theorem-2-no-one-arg-product",
        "neither I_+ nor I_× on a single collection equals n m for n=2, m=3",
        product_two_three == 6 and all(value != product_two_three for value in one_arg_candidates),
    )

    reconstructed = i_union_table()
    t_pi = pi_table()
    t_times = i_times_pairing_table(q_one)
    checks.check(
        "i-table-from-additivity",
        "union I-table on (empty,empty),(empty,unit),(unit,empty),(unit,unit) is (0,1,1,2)",
        reconstructed == (Fraction(0), Fraction(1), Fraction(1), Fraction(2)),
    )
    checks.check(
        "product-table",
        "T_π on the four pairs is (0,0,0,1)",
        t_pi == (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )
    checks.check(
        "tables-disagree",
        "T_+ disagrees with T_π at the (unit,unit) cell 2≠1",
        reconstructed != t_pi and reconstructed[3] != t_pi[3],
    )
    checks.check(
        "i-times-pairing-not-pi",
        "the q=1 pairing I_×(S) I_×(T) is (1,1,1,1), not T_π",
        t_times == (Fraction(1), Fraction(1), Fraction(1), Fraction(1)) and t_times != t_pi,
    )

    q_other = Fraction(2)
    checks.check(
        "multiplicativity",
        "I_×(n+m,q)=I_×(n,q) I_×(m,q) and I_+(n+m)=I_+(n)+I_+(m)",
        I_times(2, q_other) == I_times(1, q_other) * I_times(1, q_other)
        and I_plus(2) == I_plus(1) + I_plus(1)
        and I_times(0, q_other) == 1,
    )
    checks.check(
        "additivity-forces-empty-zero",
        "I_+(empty)=I_+(empty)+I_+(empty) holds and I_×(empty)=I_×(empty)+I_×(empty) fails",
        I_plus(0) == I_plus(0) + I_plus(0) and I_times(0, q_one) != I_times(0, q_one) + I_times(0, q_one),
    )

    record_sentence = "`I` is additive, with `I(empty)=0`."
    checks.check(
        "source-record-additivity",
        "the current axiom memo names additive I with I(empty)=0",
        record_sentence in axiom,
    )
    checks.check(
        "axiom-does-not-name-i-times",
        "the current axiom memo does not name I_× or a product table T_π",
        "I_×" not in axiom and "T_π" not in axiom and "I_times" not in axiom,
    )
    checks.check(
        "machine-status-contract",
        "the note carries the required C8 counterfactual and bounded-support status lines",
        'hypothetical_axiom_status: "C8 counterfactual: Record readout is multiplicative I_× with I_×(empty)=1; not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "non-adoption-surface",
        "the note displays the C8 failure and refuses I_×, G_N, and 1/r",
        all(
            phrase in note
            for phrase in (
                "I_×` is displayed only. It is not",
                "fails to dissolve the two-argument Newton-B residual",
                "It does not adopt `I_×`",
                "It does not install `G_N` or `1/r`",
                "The current Record sentence is not edited",
            )
        ),
    )

    print(
        "per_element: empty and two-unit identity gates call I_plus(n) and I_times(n,q); "
        "the four-pair tables are reconstructed from those gates"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
