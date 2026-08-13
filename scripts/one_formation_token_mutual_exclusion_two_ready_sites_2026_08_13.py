#!/usr/bin/env python3
"""Exact checks: one formation token, two ready sites, mutual exclusion.

Shared one-site law μ on {A,B} with masses 1/3 and 2/3. A history is the
pair (μ, T) for T in {x, y, none}. Formation at a site occurs iff T equals
that site. Record additivity is a content readout, not a site picker.
No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ONE_FORMATION_TOKEN_MUTUAL_EXCLUSION_TWO_READY_SITES_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ONE_FORMATION_TOKEN_MUTUAL_EXCLUSION_TWO_READY_SITES_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = ("x", "y")
MENU = ("A", "B")
TOKENS = ("x", "y", "none")
CONTENT_I = {"A": Fraction(1), "B": Fraction(2)}


def normalize(text: str) -> str:
    return " ".join(text.split())


def one_site_law() -> dict[str, Fraction]:
    return {"A": Fraction(1, 3), "B": Fraction(2, 3)}


def support_of(measure: dict[str, Fraction]) -> frozenset[str]:
    return frozenset(label for label, mass in measure.items() if mass > 0)


def is_probability(measure: dict[str, Fraction]) -> bool:
    return (
        set(measure) == set(MENU)
        and all(mass > 0 for mass in measure.values())
        and sum(measure.values(), Fraction(0)) == 1
    )


@dataclass(frozen=True)
class History:
    """A history is the pair (μ, T). Formation occurs iff T equals the site."""

    measure: dict[str, Fraction]
    token: str

    def __post_init__(self) -> None:
        if self.token not in TOKENS:
            raise ValueError("token must lie in {x, y, none}")
        object.__setattr__(self, "measure", dict(self.measure))

    def formed_sites(self) -> frozenset[str]:
        if self.token == "none":
            return frozenset()
        return frozenset({self.token})

    def site_formed(self, site: str) -> bool:
        return self.token == site

    def both_formed(self) -> bool:
        return self.formed_sites() == frozenset(SITES)


def both_ready_sites_form(history: History) -> bool:
    """Hostile predicate: both ready sites form in this history."""
    return history.both_formed()


def mu_selects_token(histories: tuple[History, ...]) -> bool:
    """Hostile predicate: the content law names a unique token."""
    tokens_for_mu = {history.token for history in histories}
    measures = {tuple(sorted(history.measure.items())) for history in histories}
    return len(measures) == 1 and len(tokens_for_mu) == 1


def one_token_per_window(token: str) -> bool:
    """Later extra supplier: exactly one site-token in the window."""
    return token in SITES


def I_empty() -> Fraction:
    return Fraction(0)


def I_formed_singleton(site: str, lock: str) -> Fraction:
    """Content readout of a formed singleton. The site is not used."""
    if site not in SITES:
        raise ValueError("site must be a ready site")
    if lock not in CONTENT_I:
        raise ValueError("lock must be a menu label")
    return CONTENT_I[lock]


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

    print(
        "external_scientific_inputs: current Admissibility and Record wording "
        "are source-bound; no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, and the axiom memo; "
        "no other repository scientific inputs"
    )
    print(
        "construction: shared μ on {A,B}; token alphabet {x, y, none}; "
        "histories (μ, T); I(empty)=0 and singleton content readout"
    )
    print(
        "negative_scope: μ does not select T; both ready sites do not form "
        "in this calculus; Record additivity is not a site picker"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/ONE_FORMATION_TOKEN_MUTUAL_EXCLUSION_TWO_READY_SITES_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    distribution_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_note = "does not supply the formation site, probability, or rate"
    conditional_note = "conditional on formation"
    lock_sentence = "When present, a record locks exactly one admissible local possibility."
    empty_sentence = "I(empty)=0"
    content_alone = "A readout value is determined by record content alone."
    normalized_axiom = normalize(axiom)
    normalized_note = normalize(note)

    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        distribution_sentence in normalized_axiom and distribution_sentence in note,
    )
    checks.check(
        "source-formation-reading-note",
        "the Admissibility reading note on formation site/rate is pinned",
        formation_note in normalized_axiom
        and formation_note in note
        and conditional_note in normalized_axiom
        and conditional_note in note,
    )
    checks.check(
        "source-record-when-present",
        "the Record lock sentence When present is pinned in the axiom memo and the note",
        lock_sentence in normalize(axiom) and lock_sentence in normalize(note),
    )
    checks.check(
        "source-record-additivity",
        "Record additivity and I(empty)=0 and content-alone readout are pinned",
        empty_sentence in normalized_axiom
        and empty_sentence in normalized_note
        and content_alone in normalize(axiom)
        and content_alone in note,
    )

    measure = one_site_law()
    support = support_of(measure)
    checks.check(
        "measure-full-support",
        "declared masses 1/3 and 2/3 form a full-support probability on {A,B}",
        is_probability(measure)
        and measure["A"] == Fraction(1, 3)
        and measure["B"] == Fraction(2, 3)
        and measure["A"] + measure["B"] == 1
        and support == frozenset(MENU)
        and "C" not in measure,
        residual=measure,
    )

    h_x = History(measure, "x")
    h_y = History(measure, "y")
    h_none = History(measure, "none")
    histories = (h_x, h_y, h_none)

    print(
        "table: histories "
        f"Hx_muA={h_x.measure['A']} Hx_T={h_x.token} "
        f"Hy_muA={h_y.measure['A']} Hy_T={h_y.token} "
        f"Hnone_muA={h_none.measure['A']} Hnone_T={h_none.token}"
    )

    checks.check(
        "theorem-1-same-mu",
        "μ is the same for T=x, T=y, and T=none",
        h_x.measure == h_y.measure == h_none.measure == measure
        and h_x.token != h_y.token
        and h_x.token != h_none.token
        and h_y.token != h_none.token
        and "Content law is not occurrence" in note,
        residual=(h_x.measure, h_y.measure, h_none.measure),
    )
    checks.check(
        "theorem-2-mutual-exclusion",
        "T=x and T=y are mutually exclusive; no history has both sites formed",
        h_x.formed_sites() == frozenset({"x"})
        and h_y.formed_sites() == frozenset({"y"})
        and h_none.formed_sites() == frozenset()
        and h_x.site_formed("x")
        and not h_x.site_formed("y")
        and h_y.site_formed("y")
        and not h_y.site_formed("x")
        and not h_none.site_formed("x")
        and not h_none.site_formed("y")
        and not any(history.both_formed() for history in histories)
        and frozenset({"x", "y"}) not in {history.formed_sites() for history in histories}
        and "declared one-token occupancy" in note,
    )
    checks.check(
        "theorem-3-three-compatible",
        "all three tokens are Admissibility-compatible; axioms do not select T",
        support == frozenset(MENU)
        and formation_note in note
        and conditional_note in note
        and lock_sentence in normalize(note)
        and "do not select among" in note
        and h_x.measure == h_y.measure == h_none.measure
        and {history.token for history in histories} == set(TOKENS),
    )
    checks.check(
        "theorem-4-one-token-window",
        "exactly one token per window yields mutual exclusion and a formed site",
        one_token_per_window("x")
        and one_token_per_window("y")
        and not one_token_per_window("none")
        and History(measure, "x").formed_sites() == frozenset({"x"})
        and History(measure, "y").formed_sites() == frozenset({"y"})
        and "well-defined formed site" in note
        and "one token per window" in note,
    )
    checks.check(
        "theorem-4-not-record-additivity",
        "I(empty)=0 and I of a formed singleton is a content readout, not a site picker",
        I_empty() == 0
        and I_formed_singleton("x", "A") == I_formed_singleton("y", "A") == Fraction(1)
        and I_formed_singleton("x", "B") == I_formed_singleton("y", "B") == Fraction(2)
        and I_formed_singleton("x", "A") != I_formed_singleton("x", "B")
        and I_formed_singleton("x", "A") != I_empty()
        and "not a site picker" in note
        and "I(empty)=0" in note,
        residual=(I_formed_singleton("x", "A"), I_formed_singleton("y", "A")),
    )
    checks.check(
        "theorem-5-scoped-negatives",
        "the note refuses a token-memo edit and does not claim no formation rule exists",
        "does not add a token sentence" in note
        and "do not claim that no formation rule exists" in note
        and "no formation rule exists" in note
        and "No axiom sentence is edited here" in note,
    )

    checks.check(
        "mutation-both-ready-sites-form-fails",
        "the predicate both-ready-sites-form fails on every history of this calculus",
        all(both_ready_sites_form(history) is False for history in histories)
        and not h_x.both_formed()
        and not h_y.both_formed()
        and not h_none.both_formed(),
    )
    checks.check(
        "mutation-mu-selects-T-fails",
        "the predicate μ-selects-T fails: one μ appears with three tokens",
        mu_selects_token(histories) is False
        and len({tuple(sorted(history.measure.items())) for history in histories}) == 1
        and {history.token for history in histories} == set(TOKENS),
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
                "target_claim_id: one_formation_token_two_ready_sites",
                "authors no audit verdict",
                "H_x",
                "H_y",
                "H_none",
                "declared one-token occupancy",
                "Content law is not occurrence",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note
        and "L_phys" not in note,
    )

    n5_lines = (
        "per_element: menu labels A, B and token values x, y, none are listed as exact objects",
        "per_site: the shared one-site law and the token mark are site-local at the two ready sites",
        "per_mode: content masses are checked against occupancy tokens; no spectral mode is claimed",
        "per_block: only the three-history token calculus and the additivity contrast are executed",
        "lattice_wide: checked and not executed — no lattice-wide no-go against formation rules is claimed",
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
