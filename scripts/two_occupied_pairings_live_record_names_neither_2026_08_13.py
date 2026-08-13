#!/usr/bin/env python3
"""Exact checks: two occupied pairings; live Record names neither.

Identity gates call B_pi(S, T) and B_plus(S, T). The predicate B_π == B_+
fails at the occupied-occupied cell. The predicate that the live Record
memo contains I(empty)=0 also fails. All displayed scalars are Fraction.
"""

from __future__ import annotations

import ast
import inspect
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "TWO_OCCUPIED_PAIRINGS_LIVE_RECORD_NAMES_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_OCCUPIED_PAIRINGS_LIVE_RECORD_NAMES_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
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
OCCUPIED_OCCUPIED = (S, T)

LIVE_RECORD_SENTENCES = (
    "Only records are readable.",
    "A readout value is determined by record content alone.",
    "A site with no record cannot be read.",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def B_pi(left: frozenset[str], right: frozenset[str]) -> Fraction:
    """Supplied product-pairing on occupied collections: |S| |T|."""
    return Fraction(len(left)) * Fraction(len(right))


def B_plus(left: frozenset[str], right: frozenset[str]) -> Fraction:
    """Supplied count-add pairing on occupied collections: |S| + |T|."""
    return Fraction(len(left)) + Fraction(len(right))


def pi_table() -> dict[tuple[frozenset[str], frozenset[str]], Fraction]:
    return {cell: B_pi(*cell) for cell in PAIR_CELLS}


def plus_table() -> dict[tuple[frozenset[str], frozenset[str]], Fraction]:
    return {cell: B_plus(*cell) for cell in PAIR_CELLS}


def identity_pi_table() -> bool:
    table = pi_table()
    expected = {
        (EMPTY, EMPTY): Fraction(0),
        (EMPTY, T): Fraction(0),
        (S, EMPTY): Fraction(0),
        (S, T): Fraction(1),
    }
    return table == expected and all(isinstance(table[cell], Fraction) for cell in PAIR_CELLS)


def identity_plus_table() -> bool:
    table = plus_table()
    expected = {
        (EMPTY, EMPTY): Fraction(0),
        (EMPTY, T): Fraction(1),
        (S, EMPTY): Fraction(1),
        (S, T): Fraction(2),
    }
    return table == expected and all(isinstance(table[cell], Fraction) for cell in PAIR_CELLS)


def tables_equal() -> bool:
    """Predicate B_π == B_+. Must fail."""
    return all(B_pi(*cell) == B_plus(*cell) for cell in PAIR_CELLS)


def disagreeing_cells() -> tuple[tuple[frozenset[str], frozenset[str]], ...]:
    return tuple(cell for cell in PAIR_CELLS if B_pi(*cell) != B_plus(*cell))


def live_record_section(axiom: str) -> str:
    start = axiom.index("### Record / Fixed Reality")
    end = axiom.index("## Qualification")
    return axiom[start:end]


def live_memo_contains_i_empty_zero(axiom: str) -> bool:
    """Predicate 'live memo contains I(empty)=0'. Must fail."""
    return "I(empty)=0" in live_record_section(axiom)


def audit_input_paths_literal() -> bool:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        if node.targets[0].id != "AUDIT_INPUT_PATHS":
            continue
        if not isinstance(node.value, ast.Tuple):
            return False
        values = []
        for element in node.value.elts:
            if not isinstance(element, ast.Constant) or not isinstance(element.value, str):
                return False
            values.append(element.value)
        return tuple(values) == AUDIT_INPUT_PATHS
    return False


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
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    live_record = live_record_section(axiom)
    normalized_live_record = normalize(live_record)

    print(
        "external_scientific_inputs: live Record wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: both pairings are extras; no pairing axiom, J-field pairing, G_N, or 1/r is installed")

    checks.check(
        "audit-input-paths-literal",
        "AUDIT_INPUT_PATHS is the string-literal tuple of the new note and the axiom memo",
        audit_input_paths_literal()
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_OCCUPIED_PAIRINGS_LIVE_RECORD_NAMES_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    checks.check(
        "source-live-record",
        "the live Record body names readable records, content-alone readout, and blank unreadability",
        all(sentence in normalized_live_record for sentence in LIVE_RECORD_SENTENCES),
    )
    checks.check(
        "source-i-not-axiom",
        "the axiom memo states that named I and I(empty)=0 are not Record axiom content",
        "are not Record axiom content" in normalized_axiom
        and "named scalar collection functional `I`" in axiom,
    )
    checks.check(
        "note-quotes-live-record",
        "the note quotes the three live Record readout sentences",
        all(sentence in normalized_note for sentence in LIVE_RECORD_SENTENCES),
    )
    checks.check(
        "identity-pi-table",
        "B_pi reconstructs the Fraction four-tuple (0, 0, 0, 1)",
        identity_pi_table(),
    )
    checks.check(
        "identity-plus-table",
        "B_plus reconstructs the Fraction four-tuple (0, 1, 1, 2)",
        identity_plus_table(),
    )
    identity_sources = (
        inspect.getsource(identity_pi_table)
        + inspect.getsource(identity_plus_table)
        + inspect.getsource(tables_equal)
        + inspect.getsource(pi_table)
        + inspect.getsource(plus_table)
    )
    checks.check(
        "identity-gate-calls",
        "identity gates call B_pi(S, T) and B_plus(S, T)",
        "B_pi(" in identity_sources and "B_plus(" in identity_sources,
    )
    checks.check(
        "theorem1-occupied-occupied",
        "B_π({s},{t})=1 ≠ 2=B_+({s},{t})",
        B_pi(S, T) == Fraction(1)
        and B_plus(S, T) == Fraction(2)
        and B_pi(S, T) != B_plus(S, T),
    )
    checks.check(
        "theorem1-disagreement-count",
        "the two supplied tables disagree at three of four cells",
        len(disagreeing_cells()) == 3 and OCCUPIED_OCCUPIED in disagreeing_cells(),
    )
    checks.check(
        "theorem2-no-two-argument-map",
        "live Record does not name a two-argument map and the note says so",
        "two-argument map" not in live_record
        and "does not name a two-argument map" in normalized_note,
    )
    checks.check(
        "theorem2-b-plus-not-axiom",
        "live Record does not name B_+ as axiom content",
        "B_+" not in live_record
        and "does not name `B_+` as axiom content" in note,
    )
    checks.check(
        "theorem3-both-extras",
        "the note declares both tables extras and displays them",
        "Both tables are extras" in note
        and "B_π({s},{t}) = 1" in note
        and "B_+({s},{t}) = 2" in note,
    )
    checks.check(
        "theorem3-do-not-adopt-pi",
        "the note does not adopt π and does not pair on a J field",
        "does not adopt `π`" in normalized_note
        and "does not pair on a `J` field" in normalized_note,
    )
    checks.check(
        "mutation-tables-equal-fails",
        "the predicate B_π == B_+ is false",
        tables_equal() is False,
    )
    checks.check(
        "mutation-live-memo-i-empty-fails",
        "the predicate live memo contains I(empty)=0 is false",
        live_memo_contains_i_empty_zero(axiom) is False,
    )
    checks.check(
        "fraction-types",
        "every B_π and B_+ cell is an exact Fraction",
        all(isinstance(value, Fraction) for value in pi_table().values())
        and all(isinstance(value, Fraction) for value in plus_table().values()),
    )
    checks.check(
        "nonclaims-surface",
        "the note refuses G_N, 1/r, J-field pairing, and restoring I",
        "does not install `G_N` or `1/r`" in normalized_note
        and "pair on a `J` field" in normalized_note
        and "Named additive `I` is not restored" in note,
    )
    checks.check(
        "independence-surface",
        "the note does not depend on the I-table versus T_π cut or a multiplicative I retype",
        "does not" in normalized_note
        and "empty/unit I-table versus `T_π`" in note
        and "multiplicative retype of `I`" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note,
    )

    print("per_element: four occupied-pair cells on two disjoint unit locks are checked")
    print("per_site: no lattice site composite is asserted")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: the two extra pairing tables are the only comparison tested")
    print("lattice_wide: checked and not executed — no G_N or 1/r installation is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
