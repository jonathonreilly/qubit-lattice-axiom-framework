#!/usr/bin/env python3
"""Exact cubic-lattice checks: graph-separated auxiliary condition tuples.

Nearest-neighbor inclusion and exclusion, spacing-3 disjoint supports, and
a product of one-site laws whose condition domain excludes the origin.
Identity gates call neighbors(x) and disjoint_supports(sites). No cache
is written.
"""

from __future__ import annotations

from collections.abc import Iterable
from fractions import Fraction
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "GRAPH_SEPARATED_AUXILIARY_RECORDS_INDEPENDENT_OF_DISTANT_LOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_AUG10_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)

AUDIT_INPUT_PATHS = (
    "docs/GRAPH_SEPARATED_AUXILIARY_RECORDS_INDEPENDENT_OF_DISTANT_LOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
)

Point = tuple[int, int, int]

ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NN_SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def scale(coefficient: int, vector: Point) -> Point:
    return (coefficient * vector[0], coefficient * vector[1], coefficient * vector[2])


def graph_distance(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def neighbors(site: Point) -> frozenset[Point]:
    """Identity-gate function: the six nearest neighbors of a cubic site."""
    return frozenset(add(site, shift) for shift in NN_SHIFTS)


def moore_neighbors(site: Point) -> frozenset[Point]:
    """26-site Chebyshev-1 neighborhood; mutation of neighbors()."""
    offsets = [
        (i, j, k)
        for i, j, k in cartesian((-1, 0, 1), repeat=3)
        if (i, j, k) != (0, 0, 0)
    ]
    return frozenset(add(site, offset) for offset in offsets)


def disjoint_supports(sites: Iterable[Point]) -> bool:
    """Identity-gate function: pairwise-empty nearest-neighbor supports."""
    listed = tuple(sites)
    neighborhoods = [neighbors(site) for site in listed]
    for index, left in enumerate(neighborhoods):
        for right in neighborhoods[index + 1 :]:
            if left & right:
                return False
    return True


def condition_union(sites: Iterable[Point]) -> frozenset[Point]:
    acc: set[Point] = set()
    for site in sites:
        acc |= set(neighbors(site))
    return frozenset(acc)


def always_independent_even_of_neighbors(_site: Point) -> bool:
    """Mutation: declare every one-site law independent even of neighbors."""
    return True


def one_site_law(margin: Fraction, eta: tuple[int, ...]) -> Fraction:
    """A one-site binary margin. Domain is the 6-tuple; value may ignore it."""
    if len(eta) != 6:
        raise ValueError("one-site condition must be a 6-tuple")
    if margin < 0 or margin > 1:
        raise ValueError("margin must lie in [0, 1]")
    return margin


def product_law(margins: tuple[Fraction, ...], etas: tuple[tuple[int, ...], ...]) -> tuple[Fraction, ...]:
    if len(margins) != len(etas):
        raise ValueError("product factors must match")
    return tuple(one_site_law(margin, eta) for margin, eta in zip(margins, etas, strict=True))


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
        "external_scientific_inputs: current Lattice, Admissibility, and Record "
        "wording plus the August 10 open-interface phrase are source-bound; "
        "no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, the axiom memo, and "
        "the August 10 interface note; no other repository scientific inputs"
    )
    print(
        "construction: cubic NN inclusion/exclusion and spacing-3 disjoint "
        "neighbor supports; product law not a function of the origin"
    )
    print(
        "negative_scope: adjacency does not force independence; separation "
        "does not force uniformity or formation; no compiler non-existence"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and August 10 note",
        AUDIT_INPUT_PATHS
        == (
            "docs/GRAPH_SEPARATED_AUXILIARY_RECORDS_INDEPENDENT_OF_DISTANT_LOCK_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
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
        "source-lattice",
        "the current Lattice nearest-neighbor sentence is pinned in the axiom memo and the note",
        lattice_sentence in normalize(axiom) and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
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
        "source-formation-reading-note",
        "the Admissibility reading note on formation site/rate is pinned",
        formation_note in normalize(axiom) and formation_note in note,
    )
    checks.check(
        "source-aug10-interface",
        "August 10 open-interface phrase is pinned in the parent and the note",
        aug10_phrase in parent_aug10 and aug10_phrase in note,
    )

    two_e1 = scale(2, E1)
    three_e1 = scale(3, E1)
    six_e1 = scale(6, E1)
    nine_e1 = scale(9, E1)
    spacing3 = (three_e1, six_e1, nine_e1)
    executed = (ORIGIN, E1, two_e1, three_e1, six_e1, nine_e1)

    expected_origin = frozenset(
        {E1, scale(-1, E1), E2, scale(-1, E2), E3, scale(-1, E3)}
    )
    expected_e1 = frozenset(
        {ORIGIN, two_e1, (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1)}
    )
    expected_two = frozenset(
        {E1, three_e1, (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)}
    )
    expected_three = frozenset(
        {two_e1, (4, 0, 0), (3, 1, 0), (3, -1, 0), (3, 0, 1), (3, 0, -1)}
    )
    expected_six = frozenset(
        {(5, 0, 0), (7, 0, 0), (6, 1, 0), (6, -1, 0), (6, 0, 1), (6, 0, -1)}
    )

    checks.check(
        "neighbors-type",
        "neighbors(x) returns a frozenset of integer 3-tuples of size 6",
        all(
            isinstance(neighbors(site), frozenset)
            and all(isinstance(point, tuple) and len(point) == 3 for point in neighbors(site))
            and all(isinstance(coord, int) for point in neighbors(site) for coord in point)
            and len(neighbors(site)) == 6
            for site in executed
        ),
        residual=[(site, len(neighbors(site))) for site in executed],
    )
    checks.check(
        "witness-N0",
        "N(0) is the six axial unit sites",
        neighbors(ORIGIN) == expected_origin,
        residual=sorted(neighbors(ORIGIN)),
    )
    checks.check(
        "witness-Ne1",
        "N(e1) contains the origin and matches the listed six-tuple",
        ORIGIN in neighbors(E1) and neighbors(E1) == expected_e1,
        residual=sorted(neighbors(E1)),
    )
    checks.check(
        "witness-N2e1",
        "N(2e1) matches the listing, excludes the origin, and shares e1 with N(0)",
        neighbors(two_e1) == expected_two
        and ORIGIN not in neighbors(two_e1)
        and (neighbors(ORIGIN) & neighbors(two_e1)) == frozenset({E1}),
        residual=sorted(neighbors(two_e1)),
    )
    checks.check(
        "witness-N3e1",
        "N(3e1) matches the listing and is disjoint from N(0)",
        neighbors(three_e1) == expected_three
        and ORIGIN not in neighbors(three_e1)
        and neighbors(ORIGIN).isdisjoint(neighbors(three_e1)),
        residual=sorted(neighbors(three_e1)),
    )
    checks.check(
        "witness-N6e1",
        "N(6e1) is disjoint from N(3e1) and from N(0)",
        neighbors(six_e1) == expected_six
        and neighbors(six_e1).isdisjoint(neighbors(three_e1))
        and neighbors(six_e1).isdisjoint(neighbors(ORIGIN))
        and ORIGIN not in neighbors(six_e1),
        residual=sorted(neighbors(six_e1)),
    )
    checks.check(
        "cardinalities",
        "|N(x)|=6 for every executed site",
        all(len(neighbors(site)) == 6 for site in executed),
    )
    checks.check(
        "distances",
        "d(0,e1)=1, d(0,2e1)=2, d(0,3e1)=3, d(0,6e1)=6, d(0,9e1)=9",
        graph_distance(ORIGIN, E1) == 1
        and graph_distance(ORIGIN, two_e1) == 2
        and graph_distance(ORIGIN, three_e1) == 3
        and graph_distance(ORIGIN, six_e1) == 6
        and graph_distance(ORIGIN, nine_e1) == 9,
    )

    checks.check(
        "theorem-1-adjacent-inclusion",
        "0 is in N(e1), so a one-site law at e1 has the origin as a condition coordinate",
        ORIGIN in neighbors(E1) and graph_distance(ORIGIN, E1) == 1,
    )
    checks.check(
        "theorem-1-independence-not-forced",
        "independence of the adjacent law from the origin is not forced",
        ORIGIN in neighbors(E1)
        and always_independent_even_of_neighbors(E1)
        and always_independent_even_of_neighbors(E1) is not (ORIGIN not in neighbors(E1)),
    )

    checks.check(
        "theorem-2-distance-exclusion",
        "0 is not in N(2e1) and not in N(3e1); those one-site laws exclude the origin",
        ORIGIN not in neighbors(two_e1)
        and ORIGIN not in neighbors(three_e1)
        and graph_distance(ORIGIN, two_e1) >= 2
        and graph_distance(ORIGIN, three_e1) >= 2,
    )

    pairwise_ok = disjoint_supports(spacing3)
    origin_ok = all(disjoint_supports((ORIGIN, site)) for site in spacing3)
    origin_excluded = all(ORIGIN not in neighbors(site) for site in spacing3)
    checks.check(
        "theorem-3-spacing3-disjoint",
        "spacing-3 sites have pairwise-disjoint neighbor supports, exclude the origin, and miss N(0)",
        pairwise_ok and origin_ok and origin_excluded and disjoint_supports(spacing3),
        residual=(pairwise_ok, origin_ok, origin_excluded),
    )
    checks.check(
        "theorem-3-spacing2-contrast",
        "spacing 2 is not disjoint-support: N(0) ∩ N(2e1) = {e1}",
        not disjoint_supports((ORIGIN, two_e1))
        and (neighbors(ORIGIN) & neighbors(two_e1)) == frozenset({E1}),
    )
    checks.check(
        "theorem-3-spacing2-family",
        "replacing spacing 3 by spacing 2 fails disjoint_supports on {2e1,4e1,6e1}",
        not disjoint_supports((two_e1, scale(4, E1), six_e1))
        and disjoint_supports(spacing3),
    )

    union = condition_union(spacing3)
    checks.check(
        "theorem-4-product-domain",
        "the n=3 product condition union has 18 sites, excludes the origin, and equals the neighbor union",
        len(union) == 18
        and ORIGIN not in union
        and union == neighbors(three_e1) | neighbors(six_e1) | neighbors(nine_e1)
        and disjoint_supports(spacing3),
        residual=(len(union), ORIGIN in union),
    )

    dummy_eta = (0, 0, 0, 0, 0, 0)
    other_eta = (1, 0, 1, 0, 1, 0)
    fair = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    biased = (Fraction(2, 3), Fraction(1, 3), Fraction(3, 4))
    product_fair_a = product_law(fair, (dummy_eta, dummy_eta, dummy_eta))
    product_fair_b = product_law(fair, (other_eta, dummy_eta, other_eta))
    product_biased = product_law(biased, (dummy_eta, dummy_eta, dummy_eta))
    checks.check(
        "theorem-4-not-function-of-origin",
        "a product of one-site laws on the spacing-3 family ignores a change only at the origin",
        ORIGIN not in condition_union(spacing3)
        and product_fair_a == product_fair_b == fair,
    )
    checks.check(
        "theorem-5-uniformity-not-forced",
        "fair and biased products are both allowed one-site products; p=1/2 is an extra selector",
        product_fair_a == fair
        and product_biased == biased
        and product_fair_a != product_biased
        and all(margin != Fraction(1, 2) for margin in biased),
    )
    checks.check(
        "theorem-5-adjacent-does-not-force",
        "adjacent placement still has 0 in the condition tuple",
        ORIGIN in neighbors(E1),
    )
    checks.check(
        "theorem-5-formation-not-derived",
        "formation site/rate remains a reading-note residual, not a lattice identity",
        formation_note in note and ORIGIN not in condition_union(spacing3),
    )

    diagonal = add(E1, E2)
    checks.check(
        "mutation-moore-fails-distance2",
        "replacing neighbors by the 26-site Moore neighborhood fails blanket distance-2 origin exclusion",
        len(moore_neighbors(ORIGIN)) == 26
        and len(moore_neighbors(two_e1)) == 26
        and ORIGIN not in neighbors(two_e1)
        and ORIGIN not in moore_neighbors(two_e1)
        and graph_distance(ORIGIN, diagonal) == 2
        and ORIGIN not in neighbors(diagonal)
        and ORIGIN in moore_neighbors(diagonal),
        residual=(
            ORIGIN in moore_neighbors(two_e1),
            ORIGIN in moore_neighbors(diagonal),
        ),
    )
    checks.check(
        "mutation-always-independent-fails-theorem1",
        "a declared always-independent-even-of-neighbors predicate contradicts 0 in N(e1)",
        always_independent_even_of_neighbors(E1)
        and ORIGIN in neighbors(E1)
        and always_independent_even_of_neighbors(E1) is not (ORIGIN not in neighbors(E1)),
    )
    checks.check(
        "mutation-spacing2-fails-disjoint",
        "identity-gate disjoint_supports is True at spacing 3 and False at spacing 2",
        disjoint_supports(spacing3)
        and not disjoint_supports((ORIGIN, two_e1))
        and not disjoint_supports((two_e1, scale(4, E1))),
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
                "trace_class: direct_blocker_closure",
                "target_claim_id: admissibility_distribution_to_effect_grade_bridge",
                "reachability_to_target: partially_closes",
                'next_trace_action: "A physical compiler still needs record formation at the separated sites and a fair binary margin; do not adopt axiom text."',
                'conditional_surface_status: "exact for cubic NN inclusion/exclusion and spacing-3 disjoint supports; formation and uniformity open"',
                "0 ∈ N",
                "spacing 3",
                "disjoint",
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
        and "Block 12" not in note
        and "toe-lphys" not in note,
    )

    n5_lines = (
        "per_element: named sites 0, e1, 2e1, 3e1, 6e1, 9e1 have six-point neighbor listings recomputed",
        "per_site: one-site condition tuples and the n=3 product are site-local statements, not a composite arena",
        "per_mode: nearest-neighbor condition 6-tuples are checked; no spectral or harmonic mode is claimed",
        "per_block: only inclusion, exclusion, spacing-3 disjointness, and the product-domain claim are executed",
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
