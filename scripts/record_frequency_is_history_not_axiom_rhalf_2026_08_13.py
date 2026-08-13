#!/usr/bin/env python3
"""Exact checks: record frequency is history, not an axiom r=1/2.

Frequencies are computed as Fraction counts on declared finite words.
The runner does not adopt r=1/2, does not assign a frequency to the empty
history, and does not derive Koide Q.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "RECORD_FREQUENCY_IS_HISTORY_NOT_AXIOM_RHALF_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_FREQUENCY_IS_HISTORY_NOT_AXIOM_RHALF_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MENU = frozenset({"A", "B"})
H1 = "AAAB"
H2 = "AABB"
EMPTY = ""

READOUT_SENTENCES = (
    "Only records are readable.",
    "A readout value is determined by record content alone.",
    "A site with no record cannot be read.",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def frequency(history: str, label: str) -> Fraction | None:
    if any(letter not in MENU for letter in history):
        raise ValueError("history uses a letter outside the toy menu")
    if label not in MENU:
        raise ValueError("label is outside the toy menu")
    if len(history) == 0:
        return None
    return Fraction(history.count(label), len(history))


def supplied_equal_block_r(weights: tuple[int, int]) -> Fraction:
    total = weights[0] + weights[1]
    if total == 0:
        raise ValueError("equal-block weights must have positive sum")
    return Fraction(weights[0], total)


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

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
    note_norm = normalize(note)
    axiom_norm = normalize(axiom)

    print(
        "external_scientific_inputs: current Record wording from the axiom "
        "memo only; no observational, fitted, or Koide-Q inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency against the live axiom memo"
    )

    checks.check(
        "source-record-readout",
        "the three live Record readout sentences occur verbatim",
        all(sentence in axiom_norm for sentence in READOUT_SENTENCES),
    )
    checks.check(
        "source-named-I-not-content",
        "named I and I(empty)=0 are stated not to be Record axiom content",
        (
            "a named scalar collection functional `I`" in axiom
            and "`I(empty)=0` are not Record axiom content" in axiom_norm
        ),
    )

    f_h1 = frequency(H1, "A")
    f_h2 = frequency(H2, "A")
    checks.check(
        "theorem1-histories",
        "H1=AAAB and H2=AABB are length-4 words in the two-lock menu",
        len(H1) == 4
        and len(H2) == 4
        and set(H1) <= MENU
        and set(H2) <= MENU
        and H1 != H2,
    )
    checks.check(
        "theorem1-frequencies",
        "computed f(H1,A)=3/4 and f(H2,A)=1/2",
        f_h1 == Fraction(3, 4) and f_h2 == Fraction(1, 2),
    )
    checks.check(
        "theorem1-axiom-silent-on-frequencies",
        "the axiom memo names neither displayed history nor either frequency",
        all(
            needle not in axiom
            for needle in ("AAAB", "AABB", "f(H1", "f(H2", "3/4")
        ),
    )

    empty_freq = frequency(EMPTY, "A")
    checks.check(
        "theorem2-empty-undefined",
        "f(empty, ·) is undefined",
        empty_freq is None,
    )
    checks.check(
        "theorem2-half-on-blank-is-not-readout",
        "returning 1/2 on the empty history is not a Record readout",
        empty_freq != Fraction(1, 2)
        and "A site with no record cannot be read." in axiom_norm
        and "I(empty)=0" in axiom_norm
        and "are not Record axiom content" in axiom_norm,
    )

    selector = supplied_equal_block_r((1, 1))
    checks.check(
        "theorem3-supplied-selector",
        "equal-block (1,1) supplies r=1/2 by normalization, not by Record",
        selector == Fraction(1, 2) and f_h1 != selector and f_h2 == selector,
    )
    checks.check(
        "theorem3-histories-displayed",
        "the note displays both histories and types (1,1) as a supplied selector",
        "H1 = AAAB" in note
        and "H2 = AABB" in note
        and "supplied weighting plus a selector" in note_norm
        and "not a theorem of live Record" in note_norm,
    )
    checks.check(
        "theorem3-no-koide-q",
        "the note does not derive Koide Q and does not say quarks forbid the investigation",
        "does not derive Koide `Q`" in note_norm
        and "does not say quarks forbid the investigation" in note_norm,
    )

    length4 = ["".join(word) for word in product("AB", repeat=4)]
    half_on_all_length4 = all(
        frequency(word, "A") == Fraction(1, 2) for word in length4
    )
    length4_values = {frequency(word, "A") for word in length4}
    checks.check(
        "mutation-universal-half",
        "not every length-4 history has f(A)=1/2; H1 is the witness",
        half_on_all_length4 is False
        and frequency(H1, "A") == Fraction(3, 4)
        and H1 in length4
        and length4_values
        == {
            Fraction(0),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(3, 4),
            Fraction(1),
        },
    )
    checks.check(
        "mutation-empty-half-axiom",
        "f(empty)=1/2 is not axiom content",
        empty_freq is None
        and "f(empty)=1/2 is axiom content" not in axiom_norm
        and "A site with no record cannot be read." in axiom_norm,
    )

    checks.check(
        "note-quotes-live-record",
        "the note quotes the three readout sentences verbatim",
        all(sentence in note_norm for sentence in READOUT_SENTENCES),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "current-surface status is bounded-support and is not a retype",
        "actual_current_surface_status: bounded-support" in note
        and "This is current Record, not a retype." in note
        and "hypothetical_axiom_status" not in note,
    )
    checks.check(
        "no-adoption",
        "the note neither adopts nor universally forces r=1/2",
        "axioms do not select a frequency" in note_norm
        and "not adopted" in note_norm
        and "universal `r=1/2`" in note
        and "rejected" in note_norm,
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not edited and does not contain the toy frequency algebra",
        "f(H,A)" not in axiom and "H1 = AAAB" not in axiom,
    )
    checks.check(
        "parent-is-axiom-memo-only",
        "declared audit inputs are exactly the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_FREQUENCY_IS_HISTORY_NOT_AXIOM_RHALF_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print(
        "per_element: sixteen length-4 words and the two displayed histories "
        "are counted with exact Fraction"
    )
    print(
        "per_site: the toy menu is one site with two lock labels; no "
        "composite carrier is asserted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
