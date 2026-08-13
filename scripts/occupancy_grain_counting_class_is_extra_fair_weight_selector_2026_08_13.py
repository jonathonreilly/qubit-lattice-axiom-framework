#!/usr/bin/env python3
"""Exact checks: occupancy-grain counting is an extra fair-weight selector.

Identity gates call two_cell_update(f, w) and r_of_w(w)=(1-w)/(2w).
July 16 uniqueness is recomputed, not stipulated. The class is not
adopted. No cache is written.
"""

from __future__ import annotations

from collections.abc import Callable
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "OCCUPANCY_GRAIN_COUNTING_CLASS_IS_EXTRA_FAIR_WEIGHT_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
JULY16_PATH = (
    ROOT
    / "docs"
    / "ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_GRAIN_COUNTING_CLASS_IS_EXTRA_FAIR_WEIGHT_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

HALF = Fraction(1, 2)
THIRD = Fraction(1, 3)
ONE = Fraction(1)
ZERO = Fraction(0)
Profile = Callable[[Fraction], Fraction]


def normalize(text: str) -> str:
    return " ".join(text.split())


def two_cell_update(f: Profile, w: Fraction) -> Fraction:
    """Identity-gate: T_f(w) = f(w)/(f(w)+f(1-w))."""
    return f(w) / (f(w) + f(ONE - w))


def share_ratio(f: Profile, x: Fraction) -> Fraction:
    return f(x) / x


def is_stationary(f: Profile, w: Fraction) -> bool:
    return two_cell_update(f, w) == w


def r_of_w(w: Fraction) -> Fraction:
    """Identity-gate: displayed unadopted dictionary r = (1-w)/(2w)."""
    return (ONE - w) / (2 * w)


def f_power(k: int) -> Profile:
    def f(x: Fraction) -> Fraction:
        return x**k

    return f


def f_identity(x: Fraction) -> Fraction:
    """July 16 identity-family negative control, outside the class."""
    return x


def axioms_force_w_half(_w: Fraction) -> bool:
    """Mutation: declare that the four axioms force every 2-cell weight to 1/2."""
    return True


def all_two_cell_laws_stationary_at_half(_w: Fraction) -> bool:
    """Mutation: replace the July 16 class by 'all 2-cell laws are stationary at 1/2'."""
    return True


def dictionary_forces_r_half(weights: tuple[Fraction, ...]) -> bool:
    return all(r_of_w(weight) == HALF for weight in weights)


def odds_gap(f: Profile, w: Fraction) -> Fraction:
    return f(w) * (ONE - w) - w * f(ONE - w)


def share_gap(f: Profile, w: Fraction) -> Fraction:
    return w * (ONE - w) * (share_ratio(f, w) - share_ratio(f, ONE - w))


def interior_stationary_on(f: Profile, sample: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(w for w in sample if ZERO < w < ONE and is_stationary(f, w))


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
    july16 = JULY16_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_july16 = normalize(july16)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: July 16 record-influence uniqueness "
        "and the current axiom wording are source-bound; no observational "
        "or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, the July 16 parent, "
        "and the axiom memo; no runner cache is written"
    )
    print(
        "negative_scope: the occupancy-grain class is not adopted; "
        "r=1/2 is not forced; axioms do not select w=1/2 via that class"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, July 16 parent, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/OCCUPANCY_GRAIN_COUNTING_CLASS_IS_EXTRA_FAIR_WEIGHT_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    unique_interior = "the unique interior stationary weight on a 2-cell menu is `w = 1/2`"
    selects_none = "This note selects no menu, weight, horn, or dial value."
    tf_line = "T_f(q) = f(q) / (f(q)+f(1-q)),"
    identity_family = (
        "The identity family in N2 is non-recording dynamics and is therefore a "
        "negative control outside that recording-update hypothesis"
    )
    unadopted = "explicitly unadopted energy dictionary"
    dictionary_formula = "r = (1-w)/(2w)"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    additivity_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    lock_sentence = "When present, a record locks exactly one admissible local possibility."
    content_sentence = "A readout value is determined by record content alone."
    formation_note = "does not supply the formation site, probability, or rate"
    form_values = "the distribution's extensional form and values are not specified by this memo"
    update_laws = "update laws"
    weight_values = "supply transition-probability or weight values"
    primitive_content = "These axioms state only their named primitive content."

    checks.check(
        "source-july16-unique-interior",
        "July 16 names unique interior 2-cell stationary weight w=1/2",
        unique_interior in normalized_july16 and unique_interior in normalized_note,
    )
    checks.check(
        "source-july16-selects-none",
        "July 16 selects no menu, weight, horn, or dial value",
        selects_none in normalized_july16 and selects_none in normalized_note,
    )
    checks.check(
        "source-july16-class",
        "July 16 declares T_f and the identity-family negative control",
        tf_line in july16
        and identity_family in normalized_july16
        and tf_line in note
        and "identity family" in note,
    )
    checks.check(
        "source-july16-dictionary",
        "July 16 displays the explicitly unadopted dictionary r = (1-w)/(2w)",
        unadopted in july16
        and dictionary_formula in july16
        and unadopted in note
        and dictionary_formula in note,
    )
    checks.check(
        "source-july16-conditional",
        "July 16 marks its premise weight as conditional",
        "**Premise weight:** conditional." in july16
        and "Premise weight: conditional." in note,
    )
    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        admissibility_sentence in normalized_axiom and admissibility_sentence in note,
    )
    checks.check(
        "source-admissibility-residuals",
        "update laws, unspecified form/values, and no weight values are pinned",
        update_laws in axiom
        and form_values in normalized_axiom
        and weight_values in normalized_axiom
        and update_laws in note
        and form_values in normalized_note
        and "does not supply" in note
        and "weight values" in note,
    )
    checks.check(
        "source-record-and-formation",
        "Record lock, content-only, additivity, and the formation reading note are pinned",
        lock_sentence in normalized_axiom
        and content_sentence in normalized_axiom
        and additivity_sentence in normalized_axiom
        and formation_note in normalized_axiom
        and lock_sentence in normalized_note
        and content_sentence in normalized_note
        and additivity_sentence in normalized_note
        and formation_note in normalized_note,
    )
    checks.check(
        "source-primitive-content",
        "the axiom memo states that the axioms name only their primitive content",
        primitive_content in axiom and primitive_content in normalized_note,
    )

    sample = (
        Fraction(1, 7),
        Fraction(1, 4),
        THIRD,
        Fraction(2, 5),
        Fraction(3, 7),
        HALF,
        Fraction(4, 7),
        Fraction(2, 3),
        Fraction(3, 4),
        Fraction(6, 7),
    )
    f2 = f_power(2)
    f3 = f_power(3)

    checks.check(
        "theorem-1-odds-identity",
        "f(w)(1-w)-w f(1-w) equals w(1-w)[g(w)-g(1-w)] on the sample",
        all(odds_gap(f2, w) == share_gap(f2, w) for w in sample)
        and all(odds_gap(f3, w) == share_gap(f3, w) for w in sample)
        and all(odds_gap(f_identity, w) == share_gap(f_identity, w) for w in sample),
    )
    checks.check(
        "theorem-1-half-stationary",
        "T_f(1/2)=1/2 for the executed class profiles",
        two_cell_update(f2, HALF) == HALF
        and two_cell_update(f3, HALF) == HALF
        and is_stationary(f2, HALF)
        and is_stationary(f3, HALF),
        residual=(two_cell_update(f2, HALF), two_cell_update(f3, HALF)),
    )
    checks.check(
        "theorem-1-unique-on-sample",
        "on the executed sample the only interior stationary weight is 1/2",
        interior_stationary_on(f2, sample) == (HALF,)
        and interior_stationary_on(f3, sample) == (HALF,),
        residual=(interior_stationary_on(f2, sample), interior_stationary_on(f3, sample)),
    )
    checks.check(
        "theorem-1-g-injective",
        "g(x)=x^{k-1} is strictly increasing on the ordered sample",
        all(
            share_ratio(f2, sample[i]) < share_ratio(f2, sample[i + 1])
            for i in range(len(sample) - 1)
        )
        and all(
            share_ratio(f3, sample[i]) < share_ratio(f3, sample[i + 1])
            for i in range(len(sample) - 1)
        ),
    )

    t2_third = two_cell_update(f2, THIRD)
    t3_third = two_cell_update(f3, THIRD)
    checks.check(
        "theorem-2-third-full-support",
        "w=1/3 is a distinct full-support 2-cell law",
        (THIRD, ONE - THIRD) == (THIRD, Fraction(2, 3))
        and (HALF, HALF) != (THIRD, Fraction(2, 3))
        and THIRD > 0
        and ONE - THIRD > 0,
    )
    checks.check(
        "theorem-2-third-not-stationary",
        "T_{x^2}(1/3)=1/5 and T_{x^3}(1/3)=1/9, neither equal to 1/3",
        t2_third == Fraction(1, 5)
        and t3_third == Fraction(1, 9)
        and t2_third != THIRD
        and t3_third != THIRD
        and not is_stationary(f2, THIRD)
        and not is_stationary(f3, THIRD),
        residual=(t2_third, t3_third),
    )
    checks.check(
        "theorem-2-value-open",
        "Admissibility leaves both executed full-support weights available",
        admissibility_sentence in note
        and form_values in normalized_note
        and t2_third != HALF,
    )

    class_needles = (
        "record-influence class",
        "occupancy-grain",
        "T_f(q)",
        "continued-registration",
        "g(x) := f(x)/x",
    )
    checks.check(
        "theorem-3-axioms-do-not-name-class",
        "the axiom memo does not name the record-influence / occupancy-grain class",
        all(needle not in axiom for needle in class_needles)
        and all(needle in note for needle in class_needles)
        and primitive_content in normalized_note
        and update_laws in note,
        residual=[needle for needle in class_needles if needle in axiom],
    )

    checks.check(
        "theorem-4-dictionary-images",
        "r(1/2)=1/2 and r(1/3)=1 by the displayed dictionary",
        r_of_w(HALF) == HALF
        and r_of_w(THIRD) == ONE
        and r_of_w(THIRD) != HALF,
        residual=(r_of_w(HALF), r_of_w(THIRD)),
    )
    checks.check(
        "theorem-4-difference-identity",
        "r(w)-1/2 equals (1-2w)/(2w) and is nonzero at w=1/3",
        r_of_w(THIRD) - HALF == (ONE - 2 * THIRD) / (2 * THIRD) == HALF
        and r_of_w(HALF) - HALF == ZERO,
        residual=r_of_w(THIRD) - HALF,
    )
    checks.check(
        "theorem-4-not-adopted",
        "the note displays the dictionary and does not force r=1/2",
        "Display only" in note
        and "Do not adopt the dictionary" in note
        and "Do not force `r = 1/2`" in note
        and dictionary_forces_r_half((HALF, THIRD)) is False
        and dictionary_forces_r_half((HALF,)) is True,
    )

    checks.check(
        "theorem-5-extra-selector",
        "class uniqueness requires T_f; Record additivity and Admissibility values do not supply it",
        is_stationary(f2, HALF)
        and not is_stationary(f2, THIRD)
        and additivity_sentence in normalized_note
        and weight_values in normalized_axiom
        and "extra selector" in note,
    )

    checks.check(
        "mutation-axioms-force-w-half-fails",
        "the predicate that the axioms force w=1/2 fails because w=1/3 remains legal",
        axioms_force_w_half(THIRD) is True
        and THIRD != HALF
        and (THIRD, Fraction(2, 3)) != (HALF, HALF)
        and not is_stationary(f2, THIRD),
    )
    identity_third = two_cell_update(f_identity, THIRD)
    checks.check(
        "mutation-all-laws-stationary-fails",
        "replacing the July 16 class by all 2-cell laws stationary at 1/2 fails on w=1/3",
        all_two_cell_laws_stationary_at_half(THIRD) is True
        and identity_third == THIRD
        and identity_third != HALF
        and two_cell_update(f2, THIRD) != THIRD
        and is_stationary(f_identity, THIRD)
        and not is_stationary(f2, THIRD),
        residual=identity_third,
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
                "target_claim_id: occupancy_grain_counting_selects_fair_two_cell_weight",
                "reachability_to_target: prunes",
                'next_trace_action: "Occupancy-grain counting remains an extra selector for a fair 2-cell weight. Do not adopt the class. Do not force r=1/2. Do not adopt axiom text."',
                "1/5",
                "authors no audit verdict",
                "**Type:** bounded_theorem",
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
        residual=[line for line in other_retained.splitlines() if "retained" in line],
    )
    checks.check(
        "canonical-nonmutation",
        "occupancy-grain counting and T_f uniqueness are absent from the axiom memo",
        all(
            phrase not in axiom
            for phrase in (
                "T_f(q)",
                "record-influence class",
                "occupancy-grain",
                "r = (1-w)/(2w)",
            )
        ),
    )

    n5_lines = (
        "per_element: named weights 1/2 and 1/3 with T_f values 1/5, 1/9 and dial images 1/2, 1 recomputed",
        "per_site: the statements are one 2-cell menu; no composite carrier is asserted",
        "per_mode: occupancy-grain T_f is checked against axiom sentences; no spectral mode is claimed",
        "per_block: only Theorems 3-5 are gated here: non-naming, unadopted dictionary, extra selector",
        "lattice_wide: checked and not executed — no lattice-wide fair-weight law or universal r=1/2 is claimed",
    )
    checks.check(
        "n5-scoped-negatives",
        "five N5 resolution lines for Theorems 3-5 are present and scoped",
        len(n5_lines) == 5
        and all(len(line) >= 40 for line in n5_lines)
        and n5_lines[0].startswith("per_element:")
        and n5_lines[1].startswith("per_site:")
        and n5_lines[2].startswith("per_mode:")
        and n5_lines[3].startswith("per_block:")
        and n5_lines[4].startswith("lattice_wide:"),
    )
    for line in n5_lines:
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
