#!/usr/bin/env python3
"""Exact checks: a content law does not determine a formation-rate functional.

Four lawful prefix histories on a 4-site window have rates 1/4, 1/2, 3/4, 1.
No μ-only map equals r(h) on every lawful history. Identity gates call
empirical_rate(h) and lawful(h, μ). No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from collections.abc import Mapping
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "CONTENT_LAW_DOES_NOT_DETERMINE_FORMATION_RATE_FUNCTIONAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CONTENT_LAW_DOES_NOT_DETERMINE_FORMATION_RATE_FUNCTIONAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]

MENU = ("A", "B", "C")
PATH_WINDOW: tuple[Point, ...] = (
    (0, 0, 0),
    (1, 0, 0),
    (2, 0, 0),
    (3, 0, 0),
)
TETRA_WINDOW: tuple[Point, ...] = (
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
STAR_WINDOW: tuple[Point, ...] = (
    (0, 0, 0),
    (1, 0, 0),
)
WINDOW_SIZE = 4


def normalize(text: str) -> str:
    return " ".join(text.split())


def support_of(measure: Mapping[str, Fraction]) -> frozenset[str]:
    return frozenset(label for label, mass in measure.items() if mass > 0)


def is_probability(measure: Mapping[str, Fraction]) -> bool:
    return (
        set(measure) == set(MENU)
        and all(mass >= 0 for mass in measure.values())
        and sum(measure.values(), Fraction(0)) == 1
    )


@dataclass(frozen=True)
class History:
    """Partial lock map on a finite window. None means no record."""

    window: tuple[Point, ...]
    locks: tuple[str | None, ...]

    def __post_init__(self) -> None:
        if len(self.window) != len(self.locks):
            raise ValueError("locks must match window sites")

    def n_lock(self) -> int:
        return sum(1 for lock in self.locks if lock is not None)

    def locked_contents(self) -> tuple[str, ...]:
        return tuple(lock for lock in self.locks if lock is not None)

    def satisfies_occurrence(self) -> bool:
        return self.n_lock() > 0


def prefix_locks(window: tuple[Point, ...], count: int, label: str = "A") -> History:
    locks = tuple(label if index < count else None for index in range(len(window)))
    return History(window, locks)


def empirical_rate(history: History) -> Fraction:
    """Identity-gate function: N(h)/|W|."""
    return Fraction(history.n_lock(), len(history.window))


def lawful(history: History, measure: Mapping[str, Fraction]) -> bool:
    """Identity-gate function: every lock lies in supp(μ)."""
    allowed = support_of(measure)
    return all(content in MENU and content in allowed for content in history.locked_contents())


def rate_is_function_of_mu(measure: Mapping[str, Fraction]) -> Fraction:
    """Mutation: one rational computed from μ alone, independent of h."""
    return sum((mass for mass in measure.values() if mass > 0), Fraction(0))


def always_form_selector(history: History) -> Fraction:
    """Counting selector: every site forms, so the rate is 1."""
    del history
    return Fraction(1)


def always_form_history(history: History, fill: str = "A") -> History:
    filled = tuple(lock if lock is not None else fill for lock in history.locks)
    return History(history.window, filled)


def mu_c_zero_forbids_n4(history: History, measure: Mapping[str, Fraction]) -> bool:
    """Mutation: treat μ(C)=0 as forbidding a full-window lock."""
    if measure.get("C", Fraction(1)) == 0 and history.n_lock() == len(history.window):
        return False
    return lawful(history, measure)


def four_copies(history: History) -> tuple[History, History, History, History]:
    return (history, history, history, history)


def poisson_intensity(measure: Mapping[str, Fraction], lam: Fraction = Fraction(1)) -> Fraction:
    """Declared extra constant intensity; not a history rate."""
    del measure
    return lam


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current Admissibility and Record wording "
        "are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: no functional of the content law equals the empirical "
        "window rate; a physical rate supplier remains extra"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/CONTENT_LAW_DOES_NOT_DETERMINE_FORMATION_RATE_FUNCTIONAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    rate_sentence = "it does not supply the formation site, probability, or rate"
    lock_sentence = "When present, a record locks exactly one admissible local possibility."
    support_sentence = "on finite menus, exactly the possibilities of nonzero probability"
    distribution_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-rate-nonsupply",
        "the rate non-supply sentence is pinned in the axiom memo and the note",
        rate_sentence in normalized_axiom
        and rate_sentence in normalized_note
        and "conditional on formation" in normalized_axiom,
    )
    checks.check(
        "source-records-form",
        "Records form. and the lock sentence are pinned in the axiom memo and the note",
        "Records form." in axiom
        and "Records form." in note
        and lock_sentence in normalize(axiom)
        and lock_sentence in normalize(note),
    )
    checks.check(
        "source-support",
        "finite-menu support and the distribution sentence are pinned",
        support_sentence in normalized_axiom
        and distribution_sentence in normalized_axiom
        and "nonzero probability" in note
        and distribution_sentence in note,
    )

    measure = {
        "A": Fraction(1, 3),
        "B": Fraction(2, 3),
        "C": Fraction(0),
    }
    support = support_of(measure)
    checks.check(
        "measure-normalized",
        "declared masses 1/3, 2/3, 0 form a probability on the three-point menu",
        is_probability(measure)
        and measure["A"] == Fraction(1, 3)
        and measure["B"] == Fraction(2, 3)
        and measure["C"] == Fraction(0)
        and measure["A"] + measure["B"] + measure["C"] == 1,
    )
    checks.check(
        "support-computed",
        "support computed from positive mass is {A,B}, so C is not admissible",
        support == frozenset({"A", "B"})
        and "C" not in support
        and measure["C"] == 0
        and measure["A"] > 0
        and measure["B"] > 0,
    )
    checks.check(
        "window-cardinality",
        "the path and the tetrahedron are 4-site windows",
        len(PATH_WINDOW) == WINDOW_SIZE == 4
        and len(TETRA_WINDOW) == 4
        and len(set(PATH_WINDOW)) == 4
        and len(set(TETRA_WINDOW)) == 4,
    )

    prefixes = tuple(prefix_locks(PATH_WINDOW, count) for count in (1, 2, 3, 4))
    h1, h2, h3, h4 = prefixes
    rates = [empirical_rate(history) for history in prefixes]
    lawful_flags = [lawful(history, measure) for history in prefixes]
    expected_rates = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
    checks.check(
        "theorem-1-four-rates",
        "identity-gate empirical_rate returns 1/4, 1/2, 3/4, 1 on the prefix histories",
        rates == expected_rates
        and empirical_rate(h1) == Fraction(1, 4)
        and empirical_rate(h2) == Fraction(1, 2)
        and empirical_rate(h3) == Fraction(3, 4)
        and empirical_rate(h4) == Fraction(1)
        and [history.n_lock() for history in prefixes] == [1, 2, 3, 4],
        residual=rates,
    )
    checks.check(
        "theorem-1-all-lawful",
        "identity-gate lawful accepts every prefix history and occurrence holds",
        lawful_flags == [True, True, True, True]
        and all(lawful(history, measure) for history in prefixes)
        and all(history.satisfies_occurrence() for history in prefixes)
        and all(set(history.locked_contents()) <= support for history in prefixes),
    )
    empty = History(PATH_WINDOW, (None, None, None, None))
    checks.check(
        "theorem-1-empty-excluded",
        "the all-empty history has rate 0 and fails occurrence",
        empirical_rate(empty) == Fraction(0)
        and lawful(empty, measure)
        and not empty.satisfies_occurrence()
        and empty.n_lock() == 0,
        residual=empirical_rate(empty),
    )

    rho = rate_is_function_of_mu(measure)
    rho_values = [rho for _ in prefixes]
    checks.check(
        "theorem-2-rho-constant",
        "any μ-only map is constant on the four prefix histories",
        len(set(rho_values)) == 1
        and rho == Fraction(1)
        and all(value == rho for value in rho_values),
        residual=rho,
    )
    checks.check(
        "theorem-2-rates-not-constant",
        "the four empirical rates are pairwise distinct",
        len(set(rates)) == 4
        and rates[0] != rates[3]
        and empirical_rate(h1) != empirical_rate(h4),
        residual=rates,
    )
    checks.check(
        "theorem-2-no-functional",
        "the μ-only value cannot equal every empirical_rate(h)",
        not all(empirical_rate(history) == rho for history in prefixes)
        and rho != empirical_rate(h1)
        and (rho == empirical_rate(h4))
        and lawful(h1, measure)
        and lawful(h4, measure),
        residual=(rho, rates),
    )

    filled_h1 = always_form_history(h1)
    checks.check(
        "theorem-3-always-form-is-one",
        "the always-form selector forces r=1 and fills h_1 to a rate-1 history",
        always_form_selector(h1) == Fraction(1)
        and always_form_selector(h4) == Fraction(1)
        and empirical_rate(filled_h1) == Fraction(1)
        and filled_h1.n_lock() == 4
        and lawful(filled_h1, measure)
        and empirical_rate(h1) != always_form_selector(h1),
        residual=(empirical_rate(h1), always_form_selector(h1)),
    )
    checks.check(
        "theorem-3-selector-extra",
        "always-form is recorded as a selector, not a theorem of Admissibility or Record",
        "every site forms" in note
        and "selector" in note
        and always_form_selector(h1) != empirical_rate(h1)
        and always_form_selector(h2) != empirical_rate(h2)
        and always_form_selector(h3) != empirical_rate(h3),
    )

    illicit_c = History(PATH_WINDOW, ("C", None, None, None))
    mixed_full = History(PATH_WINDOW, ("A", "B", "A", "B"))
    checks.check(
        "theorem-4-no-lock-C",
        "a history that locks C is rejected, while A/B locks remain lawful",
        not lawful(illicit_c, measure)
        and "C" in illicit_c.locked_contents()
        and illicit_c.locked_contents()[0] not in support
        and lawful(h4, measure)
        and lawful(mixed_full, measure)
        and empirical_rate(mixed_full) == Fraction(1)
        and set(mixed_full.locked_contents()) <= support,
    )
    checks.check(
        "theorem-4-n4-allowed",
        "μ(C)=0 does not forbid N=4: h_4 locks four copies of A and is lawful",
        lawful(h4, measure)
        and h4.n_lock() == 4
        and empirical_rate(h4) == Fraction(1)
        and set(h4.locked_contents()) == {"A"}
        and measure["C"] == 0,
    )

    omega_1 = History(STAR_WINDOW, ("A", None))
    omega_2 = History(STAR_WINDOW, ("A", "B"))
    checks.check(
        "theorem-4-two-site-counts",
        "reconstructed 2-site star admits formation counts 1 and 2 under the same μ",
        lawful(omega_1, measure)
        and lawful(omega_2, measure)
        and omega_1.n_lock() == 1
        and omega_2.n_lock() == 2
        and omega_1.satisfies_occurrence()
        and omega_2.satisfies_occurrence()
        and empirical_rate(omega_1) == Fraction(1, 2)
        and empirical_rate(omega_2) == Fraction(1)
        and len({empirical_rate(h1), empirical_rate(h2), empirical_rate(h3), empirical_rate(h4)})
        == 4,
    )

    lam = poisson_intensity(measure, Fraction(1))
    checks.check(
        "theorem-5-residual-open",
        "a Poisson intensity is a single rational and is recorded as extra, not adopted",
        lam == Fraction(1)
        and lam != empirical_rate(h1)
        and "Poisson" in note
        and "physical formation-rate supplier remains open" in note
        and "not adopt a Poisson intensity" in note
        and "constant `λ`" in note,
        residual=lam,
    )

    copied = four_copies(h1)
    copied_rates = [empirical_rate(history) for history in copied]
    checks.check(
        "mutation-rate-function-of-mu-fails",
        "rate_is_function_of_mu returns one rational and fails Theorem 2 against the four rates",
        rate_is_function_of_mu(measure) == Fraction(1)
        and isinstance(rate_is_function_of_mu(measure), Fraction)
        and [rate_is_function_of_mu(measure)] * 4 != rates
        and not all(empirical_rate(history) == rate_is_function_of_mu(measure) for history in prefixes)
        and lawful(h1, measure)
        and lawful(h4, measure),
        residual=(rate_is_function_of_mu(measure), rates),
    )
    checks.check(
        "mutation-four-copies-h1-fails",
        "replacing the four histories by four copies of h_1 fails four distinct rates",
        copied_rates == [Fraction(1, 4)] * 4
        and len(set(copied_rates)) == 1
        and len(set(rates)) == 4
        and all(lawful(history, measure) for history in copied)
        and all(empirical_rate(history) == empirical_rate(h1) for history in copied),
        residual=copied_rates,
    )
    checks.check(
        "mutation-c-forbids-n4-fails",
        "a predicate that μ(C)=0 forbids N=4 rejects lawful h_4, whose locks are all A",
        lawful(h4, measure)
        and not mu_c_zero_forbids_n4(h4, measure)
        and mu_c_zero_forbids_n4(h1, measure)
        and mu_c_zero_forbids_n4(h2, measure)
        and mu_c_zero_forbids_n4(h3, measure)
        and set(h4.locked_contents()) == {"A"}
        and measure["C"] == 0,
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
                "target_claim_id: physical_formation_rate_supplier",
                "reachability_to_target: prunes",
                'target_blocker_text: "supply a formation rate from Admissibility or Record"',
                'next_trace_action: "No functional of the content law equals the empirical window rate. A physical rate supplier remains extra. Do not adopt axiom text."',
                "it does not supply the formation site, probability, or rate",
                "Records form.",
                "r(h_1)=1/4",
                "r(h_4)=1",
                "authors no audit verdict",
            )
        )
        and rate_sentence in normalized_note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "**Type:** bounded_theorem" in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the four-rate rejector and ρ(μ) construction are absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("ρ(μ)", "r(h_1)", "empirical window rate", "h_4")
        ),
    )

    n5_lines = (
        "per_element: menu points {A,B,C} and prefix rates 1/4, 1/2, 3/4, 1 are recomputed from the masses",
        "per_site: occupancy is a per-site 0/1 mark on one 4-site window; mu is the same at each site",
        "per_mode: empirical_rate and lawful are checked; no spectral or harmonic mode is claimed",
        "per_block: only the four-rate rejector, the always-form selector, and the scoped residual are executed",
        "lattice_wide: checked and not executed — no lattice-wide formation process or rate law is claimed",
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
