#!/usr/bin/env python3
"""Exact checks: additive I(empty)=0 is a counting lemma of I_J.

C1 J arithmetic is reconstructed locally on W={x,y} with one displayed
double lock J11=(A,B). No axiom is edited. The product table stays extra.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADDITIVE_I_IS_A_LEMMA_OF_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADDITIVE_I_IS_A_LEMMA_OF_J_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

X = "x"
Y = "y"
W_SITES = (X, Y)
EMPTY = frozenset()
SX = frozenset({X})
SY = frozenset({Y})
WW = frozenset({X, Y})
SUBSETS = (EMPTY, SX, SY, WW)

# Displayed C1 double lock J11=(A,B). Both values are nonzero.
J = {X: "A", Y: "B"}


def I_J(S: frozenset[str]) -> int:
    return sum(1 for z in S if J[z] != 0)


def I_J_empty() -> int:
    return I_J(EMPTY)


def I_table() -> tuple[int, int, int, int]:
    return (I_J(EMPTY), I_J(SX), I_J(SY), I_J(WW))


def product_table() -> tuple[int, int, int, int]:
    return (0, 0, 0, 1)


def modular_holds(S: frozenset[str], T: frozenset[str]) -> bool:
    return I_J(S | T) + I_J(S & T) == I_J(S) + I_J(T)


def normalize(text: str) -> str:
    return " ".join(text.split())


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
    note_n = normalize(note).replace("> ", "")
    axiom_n = normalize(axiom)

    print("external_scientific_inputs: current Record wording only; C1 J arithmetic reconstructed locally")
    print("package_local_integrity_reads: proposed source note plus axiom memo; no runner cache")
    print("negative_scope: C1 and a pairing through I or I_J remain unadopted")

    record_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    checks.check(
        "source-record",
        "axiom memo still contains additive I and I(empty)=0",
        record_sentence in axiom_n,
    )
    checks.check(
        "note-displays-record",
        "note displays the two Record sentences and does not drop them",
        "scalar readout I is additive, with I(empty)=0" in note_n
        and record_sentence in note_n,
    )
    checks.check(
        "note-type-change",
        "note records primitive-to-theorem type change under displayed C1",
        "primitive to theorem" in note_n,
    )
    checks.check(
        "machine-hypothetical",
        "note pins the required hypothetical axiom status",
        'hypothetical_axiom_status: "C1 follow-on: additive I(empty)=0 is a lemma of I_J; product table still extra; not adopted"'
        in note,
    )
    checks.check(
        "machine-surface",
        "note pins actual_current_surface_status bounded-support",
        "actual_current_surface_status: bounded-support" in note,
    )

    checks.check(
        "identity-I_J_empty",
        "I_J(empty)=0 by counting",
        I_J_empty() == 0,
    )
    checks.check(
        "mutation-empty-nonzero",
        "predicate I_J(empty)!=0 fails",
        not (I_J_empty() != 0),
    )
    checks.check(
        "identity-unit-and-window",
        "I_J({x})=1, I_J({y})=1, I_J(W)=2",
        I_J(SX) == 1 and I_J(SY) == 1 and I_J(WW) == 2,
    )

    named_pairs = (
        (EMPTY, WW),
        (SX, SY),
        (SX, WW),
        (SX, SX),
    )
    named_ok = all(modular_holds(S, T) for S, T in named_pairs)
    checks.check(
        "identity-named-pairs",
        "I_J on union, intersection, S, T for (empty,W), ({x},{y}), ({x},W), ({x},{x})",
        named_ok,
    )

    all_pairs = tuple(product(SUBSETS, SUBSETS))
    checks.check(
        "modularity-all-16",
        "I_J(S union T)+I_J(S intersect T)=I_J(S)+I_J(T) on all 16 pairs",
        len(all_pairs) == 16 and all(modular_holds(S, T) for S, T in all_pairs),
    )
    checks.check(
        "mutation-additivity",
        "predicate I_J({x})+I_J({y}) != I_J({x,y})+I_J(empty) fails",
        not (I_J(SX) + I_J(SY) != I_J(WW) + I_J(EMPTY)),
    )

    checks.check(
        "identity-I_table",
        "I-table on the four occupancies is (0,1,1,2)",
        I_table() == (0, 1, 1, 2),
    )
    checks.check(
        "identity-product_table",
        "declared product table is (0,0,0,1)",
        product_table() == (0, 0, 0, 1),
    )
    checks.check(
        "mutation-tables-equal",
        "predicate I-table equals product table fails",
        I_table() != product_table(),
    )

    checks.check(
        "note-no-adoption",
        "note does not adopt C1, r=1/2, L_phys, or a pairing on J",
        "does not adopt C1" in note_n
        and "does not force `r=1/2`" in note_n
        and "does not adopt `L_phys`" in note_n
        and "does not put a pairing on `J`" in note_n,
    )

    print("per_element: I_J on four subsets; sixteen modular pairs")
    print("per_site: window {x,y}; double lock J11=(A,B)")
    print("per_mode: I-table is a cardinality; product table stays extra")
    print("per_block: additive-I type change under displayed C1 only")
    print("lattice_wide: checked and not executed — two-site window only")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
