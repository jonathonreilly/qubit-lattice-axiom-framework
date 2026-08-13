#!/usr/bin/env python3
"""Exact checks: a Record lock is a sample; a Born number is a law.

One site, menu {A,B}. Two full-support laws from positive odds.
History h locks A. Identity gates call mu1(), mu2(), and lock_content(h).
The predicate that lock A determines mu(A) must fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "RECORD_LOCK_IS_A_SAMPLE_BORN_NUMBER_IS_A_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVE_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

AUDIT_INPUT_PATHS = (
    "docs/RECORD_LOCK_IS_A_SAMPLE_BORN_NUMBER_IS_A_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

MENU = ("A", "B")


def normalize(text: str) -> str:
    return " ".join(text.split())


def law_from_positive_odds(odds_a: int, odds_b: int) -> dict[str, Fraction]:
    if odds_a <= 0 or odds_b <= 0:
        raise ValueError("full-support laws require positive odds")
    total = odds_a + odds_b
    return {"A": Fraction(odds_a, total), "B": Fraction(odds_b, total)}


def mu1() -> dict[str, Fraction]:
    return law_from_positive_odds(1, 2)


def mu2() -> dict[str, Fraction]:
    return law_from_positive_odds(3, 2)


@dataclass(frozen=True)
class History:
    locked: str

    @property
    def content(self) -> str:
        return self.locked


def lock_content(history: History) -> str:
    return history.content


def record_I(history: History | None) -> int:
    if history is None:
        return 0
    return 1


def is_probability_on_menu(law: dict[str, Fraction]) -> bool:
    return (
        set(law) == set(MENU)
        and all(law[outcome] >= 0 for outcome in MENU)
        and sum(law[outcome] for outcome in MENU) == 1
    )


def full_support(law: dict[str, Fraction]) -> bool:
    return all(law[outcome] > 0 for outcome in MENU)


def lock_a_determines_mu(history: History) -> bool:
    """Hostile predicate: the locked content names one Born number."""
    content = lock_content(history)
    return mu1()[content] == mu2()[content]


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
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_primitive = normalize(primitive)

    print("external_scientific_inputs: current axiom wording and the realized-state primitive are source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: only the identification of one Record lock with a Born number is rejected; a later compiler remains live")

    h = History("A")

    checks.check(
        "source-record-lock",
        "the axiom locks exactly one admissible local possibility",
        "a record locks exactly one admissible local possibility" in normalized_axiom,
    )
    checks.check(
        "source-content-only",
        "the axiom makes readout content-only",
        "Only records are readable." in axiom
        and "A readout value is determined by record content alone." in normalized_axiom,
    )
    checks.check(
        "source-record-I",
        "the axiom supplies additive I with I(empty)=0",
        "I(empty)=0" in axiom,
    )
    checks.check(
        "source-odds-versus-pick",
        "the axiom reading note separates law-level odds from the realized pick",
        "the law supplies the odds; the realized state supplies the pick" in normalized_axiom,
    )
    checks.check(
        "source-primitive-pointwise",
        "the realized-state primitive licenses only pointwise evaluation",
        "evaluate at the realized state, pointwise" in normalized_primitive
        and "no averaging over alternatives" in normalized_primitive
        and "no quoting a number that would differ had another law-admissible state been realized"
        in normalized_primitive,
    )

    checks.check(
        "laws-normalized",
        "both odds constructions are probability laws on the menu",
        is_probability_on_menu(mu1()) and is_probability_on_menu(mu2()),
    )
    checks.check(
        "laws-full-support",
        "both laws have full support, so A is admissible for both",
        full_support(mu1()) and full_support(mu2()),
    )
    checks.check(
        "theorem1-same-pair",
        "the pair (content, I) of the lock is independent of the law",
        lock_content(h) == "A"
        and record_I(h) == 1
        and record_I(None) == 0,
    )
    checks.check(
        "theorem2-born-numbers-differ",
        "the law-level numbers at the locked content differ",
        mu1()[lock_content(h)] != mu2()[lock_content(h)],
    )
    checks.check(
        "theorem2-not-a-function-of-h",
        "a single pair (content, I) cannot be a function to both Born numbers",
        len({mu1()[lock_content(h)], mu2()[lock_content(h)]}) == 2,
    )
    checks.check(
        "theorem3-born-is-not-readout",
        "quoting mu2 at the lock is not the Record readout of h",
        mu2()[lock_content(h)] != record_I(h)
        and lock_content(h) == "A",
    )
    checks.check(
        "mutation-lock-determines-mu",
        "the predicate that lock A determines mu(A) fails",
        lock_a_determines_mu(h) is False,
    )
    checks.check(
        "source-note-mismatch",
        "the note displays the two-law mismatch and refuses adoption",
        all(
            phrase in normalized_note
            for phrase in (
                "mu1(A)=1/3",
                "mu2(A)=3/5",
                "I(h)=1",
                "does not adopt `mu` as a readout",
                "does not claim that no later compiler exists",
                "Do not force `r=1/2`",
                "does not adopt `L_phys`",
                "Quoting `3/5` as the readout of `h`",
            )
        ),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support and negative-route-pruning fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "source_of_blocker_text: handoff",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the two-law witness is absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("mu1", "mu2", "lock_content", "L_phys")),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "no later compiler exists" in note,
    )

    print("per_element: both menu entries and both law values at the locked content are checked")
    print("per_site: one site, one unit lock of A; no composite carrier is asserted")
    print("per_mode: checked and not executed — no spectral mode is used")
    print("per_block: only the lock-versus-law identification is rejected")
    print("lattice_wide: checked and not executed — no lattice-wide frequency claim is made")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
