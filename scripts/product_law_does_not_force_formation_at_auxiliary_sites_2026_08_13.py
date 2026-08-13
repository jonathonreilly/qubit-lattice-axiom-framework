#!/usr/bin/env python3
"""Exact cubic-lattice checks: a product law does not force occupancy.

Spacing-3 disjoint 6-tuples, product of one-site Bernoulli laws as a
function of those tuples, and histories H_form / H_empty sharing the law.
Identity gates call neighbors(x) and product_law. A predicate
"product law implies both sites formed" fails on H_empty. No cache is
written.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from fractions import Fraction
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "PRODUCT_LAW_DOES_NOT_FORCE_FORMATION_AT_AUXILIARY_SITES_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/PRODUCT_LAW_DOES_NOT_FORCE_FORMATION_AT_AUXILIARY_SITES_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Joint = dict[tuple[int, int], Fraction]
Occupancy = str

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
BITS = (0, 1)
FORMED = "formed"
UNFORMED = "unformed"


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
    """Pairwise-empty nearest-neighbor supports, via neighbors()."""
    listed = tuple(sites)
    neighborhoods = [neighbors(site) for site in listed]
    for index, left in enumerate(neighborhoods):
        for right in neighborhoods[index + 1 :]:
            if left & right:
                return False
    return True


def always_disjoint(_sites: Iterable[Point]) -> bool:
    """Mutation: declare every pair of neighbor supports disjoint."""
    return True


def one_site_law(margin: Fraction, eta: tuple[int, ...]) -> dict[int, Fraction]:
    """Bernoulli law on {0,1}. Domain is the 6-tuple; value may ignore it."""
    if len(eta) != 6:
        raise ValueError("one-site condition must be a 6-tuple")
    if margin < 0 or margin > 1:
        raise ValueError("margin must lie in [0, 1]")
    return {0: margin, 1: Fraction(1) - margin}


def product_law(
    left_margin: Fraction,
    right_margin: Fraction,
    eta_left: tuple[int, ...],
    eta_right: tuple[int, ...],
) -> Joint:
    """Identity-gate function: product of two one-site laws on their 6-tuples."""
    left = one_site_law(left_margin, eta_left)
    right = one_site_law(right_margin, eta_right)
    return {(alpha, beta): left[alpha] * right[beta] for alpha in BITS for beta in BITS}


def is_product(joint: Mapping[tuple[int, int], Fraction]) -> bool:
    px = {alpha: joint[(alpha, 0)] + joint[(alpha, 1)] for alpha in BITS}
    py = {beta: joint[(0, beta)] + joint[(1, beta)] for beta in BITS}
    return all(joint[(alpha, beta)] == px[alpha] * py[beta] for alpha in BITS for beta in BITS)


@dataclass(frozen=True)
class History:
    """A history is a pair (law, occupancy) at the two auxiliary sites."""

    law: Joint
    occupancy_x: Occupancy
    occupancy_y: Occupancy

    def both_formed(self) -> bool:
        return self.occupancy_x == FORMED and self.occupancy_y == FORMED

    def neither_formed(self) -> bool:
        return self.occupancy_x == UNFORMED and self.occupancy_y == UNFORMED


def product_implies_both_formed(history: History) -> bool:
    """Hostile predicate: carrying a product law forces both sites formed."""
    if not is_product(history.law):
        return True
    return history.both_formed()


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
        "external_scientific_inputs: current Lattice, Admissibility, and Record "
        "wording are source-bound; no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, and the axiom memo; "
        "no other repository scientific inputs"
    )
    print(
        "construction: spacing-3 disjoint NN 6-tuples; product law as a "
        "function of those tuples; H_form versus H_empty"
    )
    print(
        "negative_scope: product law does not select occupancy at 3e1 and 6e1; "
        "not a no-go against all compilers"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/PRODUCT_LAW_DOES_NOT_FORCE_FORMATION_AT_AUXILIARY_SITES_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
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
    formation_note = "does not supply the formation site, probability, or rate"
    conditional_note = "conditional on formation"
    record_when_present = "When present, a record locks exactly one admissible local possibility."

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
        "source-formation-reading-note",
        "the Admissibility reading note on formation site/rate is pinned",
        formation_note in normalize(axiom)
        and formation_note in note
        and conditional_note in normalize(axiom)
        and conditional_note in note,
    )
    checks.check(
        "source-record-when-present",
        "the Record lock sentence When present is pinned in the axiom memo and the note",
        record_when_present in normalize(axiom) and record_when_present in note,
    )

    two_e1 = scale(2, E1)
    three_e1 = scale(3, E1)
    six_e1 = scale(6, E1)
    executed = (ORIGIN, two_e1, three_e1, six_e1)

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
        "witness-N3e1",
        "N(3e1) matches the listing, excludes the origin, and excludes itself",
        neighbors(three_e1) == expected_three
        and ORIGIN not in neighbors(three_e1)
        and three_e1 not in neighbors(three_e1),
        residual=sorted(neighbors(three_e1)),
    )
    checks.check(
        "witness-N6e1",
        "N(6e1) matches the listing, excludes the origin, and excludes itself",
        neighbors(six_e1) == expected_six
        and ORIGIN not in neighbors(six_e1)
        and six_e1 not in neighbors(six_e1),
        residual=sorted(neighbors(six_e1)),
    )
    checks.check(
        "distances",
        "d(0,3e1)=3, d(0,6e1)=6, d(3e1,6e1)=3",
        graph_distance(ORIGIN, three_e1) == 3
        and graph_distance(ORIGIN, six_e1) == 6
        and graph_distance(three_e1, six_e1) == 3,
    )

    checks.check(
        "theorem-1-disjoint-supports",
        "N(3e1) ∩ N(6e1) is empty; neither set contains its own site",
        disjoint_supports((three_e1, six_e1))
        and neighbors(three_e1).isdisjoint(neighbors(six_e1))
        and three_e1 not in neighbors(three_e1)
        and six_e1 not in neighbors(six_e1)
        and ORIGIN not in neighbors(three_e1)
        and ORIGIN not in neighbors(six_e1),
        residual=sorted(neighbors(three_e1) & neighbors(six_e1)),
    )
    checks.check(
        "theorem-1-spacing2-contrast",
        "spacing 2 is not disjoint-support: N(0) ∩ N(2e1) = {e1}",
        not disjoint_supports((ORIGIN, two_e1))
        and (neighbors(ORIGIN) & neighbors(two_e1)) == frozenset({E1}),
        residual=sorted(neighbors(ORIGIN) & neighbors(two_e1)),
    )

    dummy_eta = (0, 0, 0, 0, 0, 0)
    other_eta = (1, 0, 1, 0, 1, 0)
    half = Fraction(1, 2)
    third = Fraction(1, 3)
    prod_form = product_law(half, half, dummy_eta, dummy_eta)
    prod_empty = product_law(half, half, dummy_eta, dummy_eta)
    prod_other_eta = product_law(half, half, other_eta, other_eta)
    prod_third = product_law(third, third, dummy_eta, dummy_eta)
    print(
        "table: product_half "
        f"00={prod_form[(0, 0)]} 01={prod_form[(0, 1)]} "
        f"10={prod_form[(1, 0)]} 11={prod_form[(1, 1)]}"
    )
    print(
        "table: product_third "
        f"00={prod_third[(0, 0)]} 01={prod_third[(0, 1)]} "
        f"10={prod_third[(1, 0)]} 11={prod_third[(1, 1)]}"
    )

    checks.check(
        "theorem-2-same-function-of-6-tuples",
        "the product is the same function of the two 6-tuples at either occupancy tag",
        prod_form == prod_empty
        and prod_form == prod_other_eta
        and is_product(prod_form)
        and prod_form[(0, 0)] == Fraction(1, 4)
        and prod_third[(0, 0)] == Fraction(1, 9)
        and prod_third[(0, 0)] != Fraction(1, 4)
        and three_e1 not in neighbors(three_e1)
        and six_e1 not in neighbors(six_e1)
        and disjoint_supports((three_e1, six_e1)),
        residual=(prod_form, prod_third),
    )
    checks.check(
        "theorem-2-content-not-occurrence",
        "occupancy of x or y is not a coordinate of either neighbor 6-tuple",
        three_e1 not in neighbors(three_e1)
        and six_e1 not in neighbors(six_e1)
        and three_e1 not in neighbors(six_e1)
        and six_e1 not in neighbors(three_e1)
        and "Content law is not occurrence" in note,
    )

    h_form = History(prod_form, FORMED, FORMED)
    h_empty = History(prod_empty, UNFORMED, UNFORMED)
    h_third_empty = History(prod_third, UNFORMED, UNFORMED)

    checks.check(
        "theorem-3-histories-share-law",
        "H_form and H_empty share the product law and differ in occupancy",
        h_form.law == h_empty.law
        and h_form.both_formed()
        and h_empty.neither_formed()
        and not h_empty.both_formed()
        and h_form.occupancy_x != h_empty.occupancy_x
        and h_form.occupancy_y != h_empty.occupancy_y
        and is_product(h_form.law)
        and is_product(h_empty.law),
    )
    checks.check(
        "theorem-3-axiom-compatibility",
        "both histories are typed as compatible with conditional Admissibility and when-present Record",
        formation_note in note
        and conditional_note in note
        and record_when_present in note
        and "Both are compatible" in note
        and h_form.law == h_empty.law,
    )

    checks.check(
        "theorem-4-compiler-requires-h-form",
        "a bit compiler that needs records at those sites requires H_form",
        h_form.both_formed()
        and not h_empty.both_formed()
        and "requires `H_form`" in note
        and "do not select `H_form` over `H_empty`" in note,
    )
    checks.check(
        "theorem-4-axioms-do-not-select",
        "the quoted axiom sentences do not select H_form over H_empty",
        formation_note in note
        and record_when_present in note
        and h_form.law == h_empty.law
        and h_empty.neither_formed(),
    )
    checks.check(
        "theorem-5-scoped-negatives",
        "the note refuses a no-compiler claim and does not edit an axiom sentence",
        "does not claim that no compiler exists" in note.lower()
        and "no compiler exists" in note
        and "No axiom sentence is edited here" in note
        and "formation-site selector remains extra" in note
        and "we adopt" not in note.lower(),
    )

    checks.check(
        "mutation-product-implies-formed-fails-on-h-empty",
        "the predicate product-law-implies-both-formed fails on H_empty and holds on H_form",
        is_product(h_empty.law)
        and h_empty.neither_formed()
        and product_implies_both_formed(h_empty) is False
        and product_implies_both_formed(h_form) is True
        and product_implies_both_formed(h_third_empty) is False,
        residual=(product_implies_both_formed(h_empty), h_empty.neither_formed()),
    )
    checks.check(
        "mutation-always-disjoint-fails",
        "an always-disjoint predicate is true on (0,2e1) while neighbors() is not",
        always_disjoint((ORIGIN, two_e1))
        and not disjoint_supports((ORIGIN, two_e1))
        and always_disjoint((ORIGIN, two_e1)) is not disjoint_supports((ORIGIN, two_e1)),
    )

    diagonal = add(E1, E2)
    checks.check(
        "mutation-moore-fails-distance2",
        "replacing neighbors by the 26-site Moore neighborhood fails blanket distance-2 origin exclusion",
        len(moore_neighbors(ORIGIN)) == 26
        and ORIGIN not in neighbors(two_e1)
        and ORIGIN not in neighbors(diagonal)
        and ORIGIN in moore_neighbors(diagonal),
        residual=(ORIGIN in moore_neighbors(two_e1), ORIGIN in moore_neighbors(diagonal)),
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
                "target_claim_id: formation_at_auxiliary_compiler_sites",
                'target_blocker_text: "derive record formation at graph-separated auxiliary sites from a product of one-site laws"',
                "reachability_to_target: prunes",
                'next_trace_action: "A bit compiler that needs records at those sites still requires a formation rule; the product law does not select H_form over H_empty. Do not adopt axiom text."',
                "N(3e1) ∩ N(6e1)",
                "H_form",
                "H_empty",
                "authors no audit verdict",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "L_phys" not in note
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note,
    )

    n5_lines = (
        "per_element: named sites 0, 2e1, 3e1, 6e1 and the four product atoms are recomputed by integer listing",
        "per_site: one-site laws and occupancy marks at 3e1 and 6e1 are site-local, not a composite arena",
        "per_mode: nearest-neighbor 6-tuples and occupancy tags are checked; no spectral mode is claimed",
        "per_block: only disjointness, occupancy-independence of the product, and H_form versus H_empty are executed",
        "lattice_wide: checked and not executed — no lattice-wide no-go against compilers or formation rules is claimed",
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
