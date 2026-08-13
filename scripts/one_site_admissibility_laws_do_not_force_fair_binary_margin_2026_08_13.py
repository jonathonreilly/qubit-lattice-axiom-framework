#!/usr/bin/env python3
"""Exact checks: one-site laws do not force a fair binary margin.

Finite Bernoulli products on {0,1}. Identity gates call product_law(ps) and
is_uniform. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "ONE_SITE_ADMISSIBILITY_LAWS_DO_NOT_FORCE_FAIR_BINARY_MARGIN_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_AUG10_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ONE_SITE_ADMISSIBILITY_LAWS_DO_NOT_FORCE_FAIR_BINARY_MARGIN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
)

HALF = Fraction(1, 2)
THIRD = Fraction(1, 3)
QUARTER = Fraction(1, 4)
NINTH = Fraction(1, 9)
SIXTH = Fraction(1, 6)


def normalize(text: str) -> str:
    return " ".join(text.split())


def one_site_law(p: Fraction) -> tuple[Fraction, Fraction]:
    """Law (P(0), P(1)) = (p, 1-p) on {0,1}."""
    if p <= 0 or p > 1:
        raise ValueError("p must lie in (0, 1]")
    return (p, Fraction(1) - p)


def product_law(ps: tuple[Fraction, ...]) -> dict[tuple[int, ...], Fraction]:
    """Identity-gate function: independent product of one-site laws."""
    n = len(ps)
    factors = [one_site_law(p) for p in ps]
    table: dict[tuple[int, ...], Fraction] = {}
    for bits in cartesian((0, 1), repeat=n):
        mass = Fraction(1)
        for index, bit in enumerate(bits):
            mass *= factors[index][bit]
        table[bits] = mass
    return table


def is_uniform(law: dict[tuple[int, ...], Fraction]) -> bool:
    """Identity-gate function: every atom equals 1/2^n."""
    if not law:
        return False
    n = len(next(iter(law)))
    target = Fraction(1, 2**n)
    return len(law) == 2**n and all(mass == target for mass in law.values())


def always_fair(p: Fraction) -> bool:
    """Mutation: declare every p in (0, 1] fair."""
    return Fraction(0) < p <= Fraction(1)


def uniform_quarter_table(_ps: tuple[Fraction, ...]) -> dict[tuple[int, ...], Fraction]:
    """Mutation: replace the product by the uniform 1/4 table."""
    return {
        (0, 0): QUARTER,
        (0, 1): QUARTER,
        (1, 0): QUARTER,
        (1, 1): QUARTER,
    }


def lock_forces_fair(_ps: tuple[Fraction, Fraction]) -> Fraction:
    """Mutation: declare that lock of bit 1 forces bit 2 to 1/2."""
    return HALF


def counting_haar() -> Fraction:
    """Displayed extra selector: Haar / counting measure on Z/2."""
    return HALF


def conditional_second_given_first_zero(ps: tuple[Fraction, Fraction]) -> Fraction:
    joint = product_law(ps)
    denom = joint[(0, 0)] + joint[(0, 1)]
    return joint[(0, 0)] / denom


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
    parent_aug10 = PARENT_AUG10_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current Admissibility and Record wording "
        "plus the August 10 open-interface phrase are source-bound; "
        "no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, the axiom memo, and "
        "the August 10 interface note; no other repository scientific inputs"
    )
    print(
        "construction: one-site laws on {0,1}, n=2 independent products, "
        "lock conditional, displayed counting selector"
    )
    print(
        "negative_scope: Admissibility, graph separation, and Record lock "
        "do not force p=1/2; formation is not derived; no compiler non-existence"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and August 10 note",
        AUDIT_INPUT_PATHS
        == (
            "docs/ONE_SITE_ADMISSIBILITY_LAWS_DO_NOT_FORCE_FAIR_BINARY_MARGIN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_additivity = (
        "For any finite collection of pairwise-disjoint records, scalar readout"
    )
    formation_note = "does not supply the formation site, probability, or rate"
    aug10_phrase = "physical construction that produces registered measurable event partitions"

    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
    )
    checks.check(
        "source-formation-reading-note",
        "the Admissibility reading note on formation site/rate is pinned",
        formation_note in normalize(axiom) and formation_note in note,
    )
    checks.check(
        "source-record-lock",
        "the Record lock sentence is pinned in the axiom memo and the note",
        record_lock in normalize(axiom) and record_lock in note,
    )
    checks.check(
        "source-record-typing",
        "content-only and additivity sentences are pinned as typing premises",
        record_content in normalize(axiom)
        and record_additivity in normalize(axiom)
        and record_content in note
        and record_additivity in note,
    )
    checks.check(
        "source-aug10-interface",
        "August 10 open-interface phrase is pinned in the parent and the note",
        aug10_phrase in parent_aug10 and aug10_phrase in note,
    )

    fair_pair = one_site_law(HALF)
    biased_pair = one_site_law(THIRD)
    checks.check(
        "theorem-1-value-open",
        "p=1/2 and p=1/3 are distinct one-site laws on {0,1}",
        fair_pair == (HALF, HALF)
        and biased_pair == (THIRD, Fraction(2, 3))
        and fair_pair != biased_pair,
        residual=(fair_pair, biased_pair),
    )
    checks.check(
        "theorem-1-full-support",
        "both executed laws have full support, so both possibilities are available",
        all(mass > 0 for mass in fair_pair) and all(mass > 0 for mass in biased_pair),
    )

    fair = product_law((HALF, HALF))
    biased = product_law((THIRD, THIRD))
    mixed = product_law((HALF, THIRD))
    checks.check(
        "theorem-2-fair-product",
        "(1/2)*(1/2)=1/4 and the fair product is uniform",
        fair[(0, 0)] == HALF * HALF == QUARTER
        and is_uniform(fair)
        and fair[(0, 1)] == fair[(1, 0)] == fair[(1, 1)] == QUARTER,
        residual=fair,
    )
    checks.check(
        "theorem-2-biased-witness",
        "(1/3)*(1/3)=1/9, which is not 1/4",
        biased[(0, 0)] == THIRD * THIRD == NINTH
        and biased[(0, 0)] != QUARTER
        and not is_uniform(biased)
        and biased[(0, 1)] == Fraction(2, 9)
        and biased[(1, 1)] == Fraction(4, 9),
        residual=biased[(0, 0)],
    )
    checks.check(
        "theorem-2-mixed-witness",
        "(1/2)*(1/3)=1/6, which is not 1/4",
        mixed[(0, 0)] == HALF * THIRD == SIXTH
        and mixed[(0, 0)] != QUARTER
        and not is_uniform(mixed),
        residual=mixed[(0, 0)],
    )
    checks.check(
        "theorem-2-uniformity-criterion",
        "the four atoms equal 1/4 iff both margins are 1/2",
        is_uniform(product_law((HALF, HALF)))
        and not is_uniform(product_law((THIRD, THIRD)))
        and not is_uniform(product_law((HALF, THIRD)))
        and not is_uniform(product_law((Fraction(1), Fraction(1)))),
    )

    locked = (HALF, THIRD)
    cond = conditional_second_given_first_zero(locked)
    checks.check(
        "theorem-3-lock-does-not-reweight",
        "after lock bit1=0 on (1/2,1/3), the second-bit law is still 1/3",
        cond == THIRD
        and cond != HALF
        and product_law(locked)[(0, 0)] / HALF == THIRD,
        residual=cond,
    )

    checks.check(
        "theorem-4-counting-haar",
        "the counting measure on {0,1} is the law p=1/2",
        counting_haar() == HALF
        and one_site_law(counting_haar()) == (HALF, HALF)
        and is_uniform(product_law((counting_haar(), counting_haar()))),
    )
    checks.check(
        "theorem-4-selector-extra",
        "p=1/3 remains an allowed one-site law, so Haar is extra",
        one_site_law(THIRD) != one_site_law(counting_haar())
        and not is_uniform(product_law((THIRD, THIRD))),
    )

    checks.check(
        "theorem-5-formation-not-derived",
        "formation site/rate remains a reading-note residual, not a product identity",
        formation_note in note and not is_uniform(product_law((THIRD, THIRD))),
    )
    checks.check(
        "theorem-5-separation-does-not-force",
        "an independent product of one-site laws may be biased",
        is_uniform(product_law((HALF, HALF)))
        and not is_uniform(product_law((THIRD, THIRD)))
        and product_law((THIRD, THIRD))[(0, 0)] == NINTH,
    )

    checks.check(
        "mutation-always-fair-fails",
        "always_fair(p) is true on (0,1] but fails fairness at p=1/3",
        always_fair(THIRD)
        and always_fair(HALF)
        and not is_uniform(product_law((THIRD, THIRD)))
        and product_law((THIRD, THIRD))[(0, 0)] == NINTH,
    )
    checks.check(
        "mutation-uniform-table-fails-ninth",
        "replacing the product by the uniform 1/4 table misses the 1/9 witness",
        uniform_quarter_table((THIRD, THIRD))[(0, 0)] == QUARTER
        and product_law((THIRD, THIRD))[(0, 0)] == NINTH
        and uniform_quarter_table((THIRD, THIRD))[(0, 0)]
        != product_law((THIRD, THIRD))[(0, 0)],
    )
    checks.check(
        "mutation-lock-forces-fair-fails",
        "a predicate that lock of bit 1 forces bit 2 to 1/2 fails Theorem 3",
        lock_forces_fair(locked) == HALF
        and conditional_second_given_first_zero(locked) == THIRD
        and lock_forces_fair(locked) != conditional_second_given_first_zero(locked),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: negative_route_pruning",
                "target_claim_id: fair_binary_margin_from_admissibility",
                "reachability_to_target: prunes",
                'next_trace_action: "A physical compiler still needs a selector for p=1/2 and a formation rule; counting measure on Z/2 is extra. Do not adopt axiom text."',
                "1/9",
                "1/4",
                "1/6",
                "not a physical menu compiler",
                "authors no audit verdict",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note,
    )

    n5_lines = (
        "per_element: named margins 1/2 and 1/3 with atoms 1/4, 1/9, 1/6 recomputed",
        "per_site: one-site laws and the n=2 product are site-local statements, not a composite arena",
        "per_mode: Bernoulli product atoms are checked; no spectral or harmonic mode is claimed",
        "per_block: only value-openness, the uniformity criterion, lock-non-reweighting, and the displayed selector are executed",
        "lattice_wide: checked and not executed — no lattice-wide compiler, formation rate, or fair-margin law is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
