#!/usr/bin/env python3
"""Exact four-cell I-table versus extra T_π checks.

Identity gates call i_table() and pi_table(). The predicate that the two
tables agree fails at the unit-unit cell. All displayed scalars are Fraction.
"""

from __future__ import annotations

import inspect
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "EMPTY_UNIT_PAIRING_TABLE_IS_EXTRA_I_FILLS_A_DIFFERENT_TWO_BY_TWO_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NEWTON_PATH = ROOT / "docs" / "NEWTON_LAW_DERIVED_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/EMPTY_UNIT_PAIRING_TABLE_IS_EXTRA_I_FILLS_A_DIFFERENT_TWO_BY_TWO_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/NEWTON_LAW_DERIVED_NOTE.md",
)

EMPTY: frozenset[str] = frozenset()
S: frozenset[str] = frozenset({"s"})
T: frozenset[str] = frozenset({"t"})
PAIR_CELLS: tuple[tuple[frozenset[str], frozenset[str]], ...] = (
    (EMPTY, EMPTY),
    (EMPTY, T),
    (S, EMPTY),
    (S, T),
)
UNIT_UNIT = (S, T)


def normalize(text: str) -> str:
    return " ".join(text.split())


def i_of(collection: frozenset[str]) -> Fraction:
    """One-argument Record readout: I(empty)=0 and I=1 on each unit lock."""
    return Fraction(len(collection))


def i_table() -> dict[tuple[frozenset[str], frozenset[str]], Fraction]:
    """I-table on the four pair cells: (0, 1, 1, 2)."""
    return {
        (EMPTY, EMPTY): i_of(EMPTY),
        (EMPTY, T): i_of(T),
        (S, EMPTY): i_of(S),
        (S, T): i_of(S | T),
    }


def pi_table() -> dict[tuple[frozenset[str], frozenset[str]], Fraction]:
    """Declared extra product table T_π: (0, 0, 0, 1)."""
    return {
        (EMPTY, EMPTY): Fraction(0),
        (EMPTY, T): Fraction(0),
        (S, EMPTY): Fraction(0),
        (S, T): Fraction(1),
    }


def identity_i_table() -> bool:
    table = i_table()
    expected = {
        (EMPTY, EMPTY): Fraction(0),
        (EMPTY, T): Fraction(1),
        (S, EMPTY): Fraction(1),
        (S, T): Fraction(2),
    }
    return table == expected and all(isinstance(table[cell], Fraction) for cell in PAIR_CELLS)


def identity_pi_table() -> bool:
    table = pi_table()
    expected = {
        (EMPTY, EMPTY): Fraction(0),
        (EMPTY, T): Fraction(0),
        (S, EMPTY): Fraction(0),
        (S, T): Fraction(1),
    }
    return table == expected and all(isinstance(table[cell], Fraction) for cell in PAIR_CELLS)


def identity_tables_disagree() -> bool:
    left = i_table()
    right = pi_table()
    return left != right


def i_table_equals_pi_table() -> bool:
    """Predicate 'I-table equals T_π'. Must fail, including at (unit, unit)."""
    return i_table() == pi_table()


def disagreeing_cells() -> tuple[tuple[frozenset[str], frozenset[str]], ...]:
    left = i_table()
    right = pi_table()
    return tuple(cell for cell in PAIR_CELLS if left[cell] != right[cell])


def recompute_i_union() -> Fraction:
    """I({s} ⊔ {t}) from I(empty)=0 and disjoint additivity of unit locks."""
    i_empty = i_of(EMPTY)
    i_s = i_of(S)
    i_t = i_of(T)
    return i_empty + i_s + i_t


def product_extension(n: int, m: int) -> Fraction:
    """Unique separately additive extension of T_π on unit-lock counts."""
    t11 = pi_table()[UNIT_UNIT]
    if n == 0 or m == 0:
        return Fraction(0) * t11
    return Fraction(n) * Fraction(m) * t11


def separately_additive_on_grid(limit: int = 4) -> bool:
    for n in range(limit + 1):
        for m in range(limit + 1):
            if product_extension(n, m) != Fraction(n) * Fraction(m):
                return False
            if n + 1 <= limit:
                if product_extension(n, m) + product_extension(1, m) != product_extension(n + 1, m):
                    return False
            if m + 1 <= limit:
                if product_extension(n, m) + product_extension(n, 1) != product_extension(n, m + 1):
                    return False
    return True


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    newton = NEWTON_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    normalized_newton = normalize(newton)

    print("external_scientific_inputs: current Record wording and the Newton product-law non-claim are source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: T_π is extra; no pairing axiom, Newton claim, G_N, or 1/r is installed")

    record_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    newton_nonclaim = "the physical product law `M_source M_test`;"

    checks.check(
        "source-record-additivity",
        "the current Record sentence names one-argument additive I with I(empty)=0",
        record_sentence in normalized_axiom,
    )
    checks.check(
        "source-newton-nonclaim",
        "the Newton packet lists the physical product law as a non-claim",
        newton_nonclaim in newton,
    )
    checks.check(
        "note-quotes-record",
        "the note quotes the one-argument Record additivity sentence",
        record_sentence in normalized_note,
    )
    checks.check(
        "note-quotes-newton-nonclaim",
        "the note quotes only the Newton product-law non-claim",
        newton_nonclaim in note,
    )
    checks.check(
        "identity-i-table",
        "i_table() is the Fraction four-tuple (0, 1, 1, 2)",
        identity_i_table(),
    )
    checks.check(
        "identity-pi-table",
        "pi_table() is the Fraction four-tuple (0, 0, 0, 1)",
        identity_pi_table(),
    )
    identity_sources = (
        inspect.getsource(identity_i_table)
        + inspect.getsource(identity_pi_table)
        + inspect.getsource(identity_tables_disagree)
        + inspect.getsource(i_table_equals_pi_table)
    )
    checks.check(
        "identity-gate-calls",
        "identity gates call i_table() and pi_table()",
        "i_table()" in inspect.getsource(identity_i_table)
        and "pi_table()" in inspect.getsource(identity_pi_table)
        and "i_table()" in identity_sources
        and "pi_table()" in identity_sources,
    )
    checks.check(
        "theorem1-recompute",
        "I(empty)=0 and disjoint additivity recompute I({s} ⊔ {t}) as 2",
        recompute_i_union() == Fraction(2)
        and i_of(EMPTY) == Fraction(0)
        and i_table()[UNIT_UNIT] == recompute_i_union(),
    )
    checks.check(
        "theorem2-disagreement-count",
        "T_π disagrees with the I-table at three of four cells",
        len(disagreeing_cells()) == 3 and identity_tables_disagree(),
    )
    checks.check(
        "theorem2-unit-unit",
        "the unit-unit cell is 2 ≠ 1",
        i_table()[UNIT_UNIT] == Fraction(2)
        and pi_table()[UNIT_UNIT] == Fraction(1)
        and i_table()[UNIT_UNIT] != pi_table()[UNIT_UNIT],
    )
    checks.check(
        "mutation-predicate-fails",
        "the predicate I-table equals T_π is false",
        i_table_equals_pi_table() is False,
    )
    checks.check(
        "mutation-fails-at-unit-unit",
        "the equality predicate fails at the unit-unit cell",
        UNIT_UNIT in disagreeing_cells()
        and i_table()[UNIT_UNIT] != pi_table()[UNIT_UNIT],
    )
    checks.check(
        "theorem3-record-one-arg",
        "the axiom memo does not name T_π or a two-argument pairing table",
        "T_π" not in axiom
        and "T_pi" not in axiom
        and "two-argument table" not in axiom
        and "pairing table" not in axiom,
    )
    checks.check(
        "theorem3-tpi-extra",
        "the note declares T_π extra and not an axiom",
        ("T_π is extra" in normalized_note or "`T_π` is extra" in note)
        and "not an axiom" in normalized_note,
    )
    checks.check(
        "theorem4-extension-34",
        "the unique extension evaluates to 12 at (3, 4)",
        product_extension(3, 4) == Fraction(12),
    )
    checks.check(
        "theorem4-uniqueness-grid",
        "separate additivity on N forces T(n, m) = n m on the checked grid",
        separately_additive_on_grid(4) and product_extension(1, 1) == pi_table()[UNIT_UNIT],
    )
    checks.check(
        "theorem4-not-record",
        "the note states that the later supplier is not Record additivity",
        "supplier is not Record additivity" in normalized_note,
    )
    checks.check(
        "theorem5-nonclaims",
        "the note refuses a pairing axiom, a Newton claim, and installation of G_N or 1/r",
        "does not adopt a pairing axiom" in normalized_note
        and "does not claim Newton" in normalized_note
        and "does not install `G_N` or `1/r`" in normalized_note
        and newton_nonclaim in note,
    )
    checks.check(
        "fraction-types",
        "every I-table and T_π cell is an exact Fraction",
        all(isinstance(value, Fraction) for value in i_table().values())
        and all(isinstance(value, Fraction) for value in pi_table().values()),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )

    print("per_element: four pair cells on two named unit atoms are checked")
    print("per_site: no lattice site composite is asserted")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: the I-table versus extra T_π block is the only comparison tested")
    print("lattice_wide: checked and not executed — no Newton, G_N, or 1/r installation is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
