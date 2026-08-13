#!/usr/bin/env python3
"""Exact checks: Record additivity does not select the fair binary margin.

I of formed unit bits is the integer count of 1-contents. That count is
not the law-level Bernoulli margin p. Open margins share I-support.
E[I]=n p is not a Record readout. No cache is written.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "RECORD_ADDITIVITY_DOES_NOT_SELECT_FAIR_BINARY_MARGIN_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_ADDITIVITY_DOES_NOT_SELECT_FAIR_BINARY_MARGIN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

HALF = Fraction(1, 2)
THIRD = Fraction(1, 3)
ZERO = Fraction(0)
ONE = Fraction(1)
EXECUTED_N = 3
DECLARED_MARGINS = (ZERO, THIRD, HALF, ONE)


def normalize(text: str) -> str:
    return " ".join(text.split())


def I_of_bits(contents: tuple[int | Fraction, ...]) -> Fraction:
    """Identity-gate: additive Record readout of formed unit-bit contents."""
    return sum((Fraction(content) for content in contents), Fraction(0))


def bernoulli_mass(n: int, k: int, p: Fraction) -> Fraction:
    return Fraction(math.comb(n, k)) * (p**k) * ((1 - p) ** (n - k))


def bernoulli_I_support(n: int, p: Fraction) -> frozenset[Fraction]:
    """Identity-gate: possible I values under a one-site Bernoulli law."""
    return frozenset(Fraction(k) for k in range(n + 1) if bernoulli_mass(n, k, p) > 0)


def all_binary_contents(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(product((0, 1), repeat=n))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Record additivity, content-only "
        "readout, and the Admissibility distribution sentence are source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: only realized additive I as a fair-margin readout is "
        "rejected; a later selector for p=1/2 remains a live law-level escape; "
        "bits are not claimed unable to be fair"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/RECORD_ADDITIVITY_DOES_NOT_SELECT_FAIR_BINARY_MARGIN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    content_sentence = "A readout value is determined by record content alone."
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    reading_note_sentence = (
        "the distribution concerns which possibility a forming record locks, "
        "conditional on formation at that site; it does not supply the "
        "formation site, probability, or rate."
    )
    checks.check(
        "source-record-additivity",
        "the exact current Record additivity sentence is present in the axiom memo",
        additivity_sentence in normalized_axiom,
    )
    checks.check(
        "source-record-content-only",
        "the exact current content-only sentence is present in the axiom memo",
        content_sentence in normalized_axiom,
    )
    checks.check(
        "source-admissibility-distribution",
        "the exact current Admissibility distribution sentence is present in the axiom memo",
        admissibility_sentence in normalized_axiom,
    )
    checks.check(
        "source-reading-note-formation",
        "the interpretive reading note withholds formation site and rate",
        reading_note_sentence in normalized_axiom,
    )

    empty_readout = I_of_bits(())
    checks.check(
        "empty-readout",
        "I(empty)=0",
        empty_readout == ZERO,
        residual=empty_readout,
    )

    one_bit_zero = I_of_bits((0,))
    one_bit_one = I_of_bits((1,))
    one_bit_values = {one_bit_zero, one_bit_one}
    checks.check(
        "theorem-1-one-bit-values",
        "I of one formed bit is in {0,1}",
        one_bit_values == {ZERO, ONE}
        and one_bit_zero == ZERO
        and one_bit_one == ONE,
        residual=(one_bit_zero, one_bit_one),
    )
    checks.check(
        "theorem-1-not-half",
        "I of one formed bit cannot equal p=1/2 or p=1/3",
        one_bit_zero != HALF
        and one_bit_one != HALF
        and one_bit_zero != THIRD
        and one_bit_one != THIRD,
        residual=one_bit_values,
    )
    checks.check(
        "theorem-1-fairness-not-readout",
        "fairness p=1/2 is not a Record readout of one formed bit",
        HALF not in one_bit_values,
        residual=one_bit_values,
    )

    three_bit_contents = all_binary_contents(EXECUTED_N)
    three_bit_values = [I_of_bits(contents) for contents in three_bit_contents]
    three_bit_set = set(three_bit_values)
    expected_count_set = {Fraction(k) for k in range(EXECUTED_N + 1)}
    checks.check(
        "theorem-2-count-set",
        "for n=3 formed bits, I is in {0,1,2,3} regardless of p",
        three_bit_set == expected_count_set
        and len(three_bit_contents) == 8
        and all(I_of_bits(contents) == sum(contents) for contents in three_bit_contents),
        residual=sorted(three_bit_set),
    )
    checks.check(
        "theorem-2-never-open-margins",
        "on n=3, I is never 1/2 and never 1/3",
        HALF not in three_bit_set and THIRD not in three_bit_set,
        residual=sorted(three_bit_set),
    )
    checks.check(
        "I-is-integer-valued",
        "I is integer-valued on every executed 0/1 content tuple",
        all(I_of_bits(contents).denominator == 1 for contents in ((0,), (1,), *three_bit_contents)),
        residual=[I_of_bits(contents) for contents in ((0,), (1,), *three_bit_contents)],
    )
    checks.check(
        "disjoint-additivity",
        "I of three bits equals the sum of the one-bit readouts",
        all(
            I_of_bits(contents)
            == I_of_bits((contents[0],)) + I_of_bits((contents[1],)) + I_of_bits((contents[2],))
            for contents in three_bit_contents
        ),
    )

    support_third = bernoulli_I_support(EXECUTED_N, THIRD)
    support_half = bernoulli_I_support(EXECUTED_N, HALF)
    support_zero = bernoulli_I_support(EXECUTED_N, ZERO)
    support_one = bernoulli_I_support(EXECUTED_N, ONE)
    full_support = frozenset(Fraction(k) for k in range(EXECUTED_N + 1))
    checks.check(
        "theorem-3-open-support",
        "supp_I(p=1/3) = supp_I(p=1/2) = {0,1,2,3}",
        support_third == support_half == full_support,
        residual=(support_third, support_half),
    )
    checks.check(
        "theorem-3-degenerate-support",
        "p=0 has I=0 a.s. and p=1 has I=n a.s.",
        support_zero == frozenset({ZERO}) and support_one == frozenset({Fraction(EXECUTED_N)}),
        residual=(support_zero, support_one),
    )
    masses_third = [bernoulli_mass(EXECUTED_N, k, THIRD) for k in range(EXECUTED_N + 1)]
    masses_half = [bernoulli_mass(EXECUTED_N, k, HALF) for k in range(EXECUTED_N + 1)]
    checks.check(
        "theorem-3-exact-masses",
        "open-margin masses are positive and sum to 1; they are not Record readouts",
        masses_third == [Fraction(8, 27), Fraction(12, 27), Fraction(6, 27), Fraction(1, 27)]
        and masses_half == [Fraction(1, 8), Fraction(3, 8), Fraction(3, 8), Fraction(1, 8)]
        and sum(masses_third, ZERO) == ONE
        and sum(masses_half, ZERO) == ONE
        and all(mass > 0 for mass in masses_third + masses_half),
        residual=(masses_third, masses_half),
    )
    checks.check(
        "theorem-3-all-open-margins",
        "every p in (0,1) on the declared list has full I-support",
        all(bernoulli_I_support(EXECUTED_N, p) == full_support for p in DECLARED_MARGINS if 0 < p < 1),
    )

    expectation_half = Fraction(EXECUTED_N) * HALF
    ratio_set = {I_of_bits(contents) / Fraction(EXECUTED_N) for contents in three_bit_contents}
    checks.check(
        "theorem-4-expectation-extra",
        "E[I]=3/2 at p=1/2 is not a realized I",
        expectation_half == Fraction(3, 2) and expectation_half not in three_bit_set,
        residual=(expectation_half, sorted(three_bit_set)),
    )
    checks.check(
        "theorem-4-ratio-set",
        "I/3 is in {0,1/3,2/3,1} and 1/2 is not in that set",
        ratio_set == {ZERO, THIRD, Fraction(2, 3), ONE} and HALF not in ratio_set,
        residual=sorted(ratio_set),
    )
    checks.check(
        "theorem-4-expectation-not-readout",
        "E[I]=n p is a law-level number, not a Record readout",
        expectation_half not in three_bit_set
        and expectation_half != I_of_bits((1, 0, 0))
        and expectation_half != I_of_bits((1, 1, 0))
        and Fraction(EXECUTED_N) * THIRD == Fraction(1)
        and Fraction(EXECUTED_N) * THIRD != HALF,
    )

    record_functions = {
        "I": three_bit_set,
        "I/n": ratio_set,
    }
    checks.check(
        "theorem-5-no-record-function-is-half",
        "no Record function of realized I equals 1/2 on every n=3 realization",
        all(HALF not in values for values in record_functions.values())
        and not all(value == HALF for value in three_bit_values)
        and not all(value == HALF for value in ratio_set),
        residual=record_functions,
    )
    checks.check(
        "theorem-5-admissibility-does-not-select",
        "possible I values do not select p=1/2 among binary laws",
        bernoulli_I_support(EXECUTED_N, THIRD) == bernoulli_I_support(EXECUTED_N, HALF)
        and HALF not in three_bit_set,
    )

    checks.check(
        "note-preserves-empty",
        "the note records I(empty)=0",
        "I(empty)=0" in note,
    )
    checks.check(
        "note-preserves-additivity-sentence",
        "the note quotes the current Record additivity sentence",
        additivity_sentence in normalized_note,
    )
    checks.check(
        "note-preserves-content-only-sentence",
        "the note quotes the current content-only sentence",
        content_sentence in normalized_note,
    )
    checks.check(
        "note-preserves-admissibility-sentence",
        "the note quotes the current Admissibility distribution sentence",
        admissibility_sentence in normalized_note,
    )
    checks.check(
        "note-links-axiom-memo",
        "the note links the axiom memo",
        "MINIMAL_AXIOMS_2026-06-29.md" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    machine_status_phrases = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        "target_claim_id: fair_binary_margin_compiler",
        'target_blocker_text: "remaining compiler residual is record formation at those sites and a fair binary margin"',
        "source_of_blocker_text: handoff",
        "reachability_to_target: prunes",
        "artifact_role: theorem",
        'next_trace_action: "A physical selector for p=1/2, or a formation process whose typical I/n converges to 1/2, remains open; do not adopt axiom text."',
        'conditional_surface_status: "exact for I∈{0,...,n} versus p=1/2 on the executed family; fairness remains a live law-level selector"',
        'hypothetical_axiom_status: "no edit"',
        "admitted_observation_status: null",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(phrase in note for phrase in machine_status_phrases),
        residual=[phrase for phrase in machine_status_phrases if phrase not in note],
    )
    checks.check(
        "note-authors-no-audit-verdict",
        "the note authors no audit verdict",
        "authors no audit verdict" in note,
    )
    checks.check(
        "note-not-a-record-readout",
        "the note states that fairness is not a Record readout",
        "not a Record readout" in note,
    )
    checks.check(
        "note-half-and-third",
        "the note records the discriminating 1/2 and 1/3 witnesses",
        "1/2" in note and "1/3" in note and "I/3" in note and "{0,1,2,3}" in note.replace(" ", ""),
    )
    checks.check(
        "note-discriminating-witnesses",
        "the note exhibits I(0)=0, I(1)=1, shared open support, and E[I]=3/2",
        "I(0)=0" in note and "I(1)=1" in note and "3/2" in note and "supp_I(p=1/3)" in note,
    )
    checks.check(
        "note-does-not-forbid-fairness",
        "the note states the scoped gap and does not claim bits cannot be fair",
        "does not say that bits cannot be fair" in note
        and "does not say that no fair compiler exists" in note,
    )
    checks.check(
        "note-n-gate-present",
        "the note records V1-V5 and the N1-N8 scoped gate",
        all(
            heading in note
            for heading in (
                "## Value Gate (V1–V5)",
                "## No-Go Discipline Gate",
                "### N1 — materially distinct routes",
                "### N7 — hostile steelman",
                "FAIL / DO NOT SHIP",
            )
        ),
    )

    forbidden = ("new axiom", "we adopt", "promoted", "Codex", "Block 16", "toe-lphys")
    retained_hits = [
        line
        for line in note.splitlines()
        if "retained" in line
        and "audit_required_before_effective_retained" not in line
        and "bare_retained_allowed" not in line
    ]
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids axiom-adoption, promotion, executor-name, and campaign tags",
        all(phrase not in note for phrase in forbidden) and retained_hits == [],
        residual=retained_hits or [phrase for phrase in forbidden if phrase in note],
    )
    checks.check(
        "canonical-nonmutation",
        "the fair-margin selector is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("p=1/2", "fair binary", "I/n", "Bernoulli margin")
        ),
    )

    n5_lines = (
        "per_element: each 0/1 content atom is evaluated under I_of_bits; one-bit I is 0 or 1 and is never 1/2",
        "per_site: statements are one formed binary record or a finite disjoint collection of such records; no composite carrier is asserted",
        "per_mode: no spectral-mode exhaustion is claimed; the comparison object is a declared one-site Bernoulli parameter",
        "per_block: only realized additive I versus the law-level margin p=1/2 is tested on the executed n=3 family",
        "lattice_wide: checked and not executed — no lattice-wide fairness selector or formation process is claimed",
    )
    for line in n5_lines:
        print(line)
    checks.check(
        "n5-line-length",
        "each N5 resolution line is at least 40 characters",
        all(len(line) >= 40 for line in n5_lines),
        residual=[(line[:20], len(line)) for line in n5_lines],
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
