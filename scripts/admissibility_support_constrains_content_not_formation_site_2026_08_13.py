#!/usr/bin/env python3
"""Exact checks for support-constrained content versus unfixed site and rate.

The runner takes the declared finite-menu masses as input, computes support
and occupancy counts from those objects, and pins the current axiom sentences.
It does not write a cache file.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MENU = ("A", "B", "C")
SITES = ("x", "y")


def normalize(text: str) -> str:
    return " ".join(text.split())


def support_of(measure: dict[str, Fraction]) -> frozenset[str]:
    return frozenset(label for label, mass in measure.items() if mass > 0)


def is_probability(measure: dict[str, Fraction]) -> bool:
    return (
        set(measure) == set(MENU)
        and all(mass >= 0 for mass in measure.values())
        and sum(measure.values(), Fraction(0)) == 1
    )


@dataclass(frozen=True)
class Occupancy:
    """Partial site-to-content map on the 2-site star. None means no record."""

    locks: dict[str, str | None]
    measure: dict[str, Fraction]

    def __post_init__(self) -> None:
        object.__setattr__(self, "locks", dict(self.locks))
        if set(self.locks) != set(SITES):
            raise ValueError("occupancy must assign both star sites")

    def formed_sites(self) -> frozenset[str]:
        return frozenset(site for site, content in self.locks.items() if content is not None)

    def formation_count(self) -> int:
        return len(self.formed_sites())

    def locked_contents(self) -> tuple[str, ...]:
        return tuple(content for content in self.locks.values() if content is not None)

    def one_record_per_site(self) -> bool:
        return all(
            content is None or (isinstance(content, str) and content in MENU)
            for content in self.locks.values()
        )

    def lawful(self) -> bool:
        allowed = support_of(self.measure)
        return self.one_record_per_site() and all(
            content in allowed for content in self.locked_contents()
        )

    def satisfies_occurrence(self) -> bool:
        return self.formation_count() > 0


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "finite_menu: masses 1/3, 2/3, 0 on {A,B,C}; support and occupancy "
        "counts are computed, not sampled"
    )
    print(
        "negative_scope: C is not lockable under this mu; site and rate remain "
        "unfixed; other content laws remain live"
    )

    distribution_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    lock_sentence = "When present, a record locks exactly one admissible local possibility."
    support_sentence = "on finite menus, exactly the possibilities of nonzero probability"
    no_site_sentence = "it does not supply the formation site, probability, or rate"
    normalized_axiom = normalize(axiom)

    checks.check(
        "source-admissibility",
        "the current distribution sentence and nearest-neighbor conditions are pinned",
        distribution_sentence in normalized_axiom
        and "nearest-neighbor conditions" in axiom
        and distribution_sentence in note
        and "nearest-neighbor conditions" in note,
    )
    checks.check(
        "source-record",
        "Records form. and the lock sentence are pinned in the axiom memo and the note",
        "Records form." in axiom
        and "Records form." in note
        and lock_sentence in normalize(axiom)
        and lock_sentence in normalize(note),
    )
    checks.check(
        "source-support",
        "finite-menu support is identified with nonzero probability in the axiom memo",
        support_sentence in normalized_axiom and "nonzero probability" in note,
    )
    checks.check(
        "source-conditional",
        "the axiom memo states that the distribution does not supply site or rate",
        no_site_sentence in normalized_axiom
        and "conditional on formation" in normalized_axiom,
    )

    measure = {
        "A": Fraction(1, 3),
        "B": Fraction(2, 3),
        "C": Fraction(0),
    }
    total = sum(measure.values(), Fraction(0))
    support = support_of(measure)
    lockable = support
    checks.check(
        "measure-normalized",
        "declared masses 1/3, 2/3, 0 form a probability on the three-point menu",
        is_probability(measure)
        and total == 1
        and measure["A"] == Fraction(1, 3)
        and measure["B"] == Fraction(2, 3)
        and measure["C"] == 0
        and measure["A"] + measure["B"] + measure["C"] == 1,
    )
    checks.check(
        "support-computed",
        "support computed from positive mass is {A,B}, so C is not admissible",
        support == frozenset({"A", "B"})
        and "C" not in support
        and "A" in support
        and "B" in support
        and measure["C"] == 0
        and measure["A"] > 0
        and measure["B"] > 0,
    )
    checks.check(
        "theorem1-cannot-lock-C",
        "a forming record may lock only the computed support, hence cannot lock C",
        lockable == support
        and "C" not in lockable
        and "A" in lockable
        and "B" in lockable
        and all((measure[label] > 0) == (label in lockable) for label in MENU),
    )

    omega_x = Occupancy({"x": "A", "y": None}, measure)
    omega_y = Occupancy({"x": None, "y": "A"}, measure)
    omega_1 = Occupancy({"x": "A", "y": None}, measure)
    omega_2 = Occupancy({"x": "A", "y": "B"}, measure)
    illicit_c = Occupancy({"x": "C", "y": None}, measure)

    same_measure = (
        omega_x.measure == omega_y.measure == omega_1.measure == omega_2.measure == measure
    )
    checks.check(
        "theorem2-site-patterns",
        "two 2-site-star patterns share mu and differ in which site forms",
        same_measure
        and omega_x.lawful()
        and omega_y.lawful()
        and omega_x.satisfies_occurrence()
        and omega_y.satisfies_occurrence()
        and omega_x.formed_sites() == frozenset({"x"})
        and omega_y.formed_sites() == frozenset({"y"})
        and omega_x.formed_sites() != omega_y.formed_sites()
        and omega_x.locks["x"] is not None
        and omega_x.locks["y"] is None
        and omega_y.locks["x"] is None
        and omega_y.locks["y"] is not None,
    )
    checks.check(
        "theorem3-unfixed-rate",
        "two lawful patterns with the same content law have formation counts 1 and 2",
        omega_1.lawful()
        and omega_2.lawful()
        and omega_1.satisfies_occurrence()
        and omega_2.satisfies_occurrence()
        and omega_1.formation_count() == 1
        and omega_2.formation_count() == 2
        and omega_1.formation_count() != omega_2.formation_count()
        and omega_1.measure == omega_2.measure == measure
        and set(omega_2.locked_contents()) <= support,
    )
    checks.check(
        "lawful-reject-C",
        "an occupancy that locks C is rejected by the computed support, while A and B pass",
        not illicit_c.lawful()
        and "C" in illicit_c.locked_contents()
        and illicit_c.locked_contents()[0] not in support
        and all(content in support for content in omega_2.locked_contents())
        and omega_x.one_record_per_site()
        and omega_2.one_record_per_site(),
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
                "hypothetical_axiom_status: no edit",
                "Records form.",
                "nearest-neighbor conditions",
                "2-site star",
                "1/3",
                "2/3",
                "cannot lock",
                "formation counts",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note,
    )

    print(
        "per_element: the three-point menu {A,B,C} and support {A,B} are read from the masses"
    )
    print(
        "per_site: occupancy is a per-site 0/1 mark; mu is the same at x and at y"
    )
    print(
        "per_mode: locked content is a label on the finite menu; C is excluded by zero mass"
    )
    print(
        "per_block: only the declared 2-site star fragment is exhibited"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide formation process or rate law is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
