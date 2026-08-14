#!/usr/bin/env python3
"""Exact checks for cubic NN condition-domain separation.

The runner distinguishes direct-coordinate invariance of an explicitly
supplied conditional product kernel from stochastic independence after
averaging over a joint environment law.
"""

from __future__ import annotations

from collections.abc import Iterable
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "CUBIC_NN_CONDITION_DOMAIN_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_AUG10_PATH = ROOT / "docs" / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
PARENT_DYADIC_PATH = ROOT / "docs" / "FINITE_DYADIC_PRODUCT_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBIC_NN_CONDITION_DOMAIN_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/FINITE_DYADIC_PRODUCT_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
)

Point = tuple[int, int, int]
Outcome = tuple[int, ...]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
SHIFTS: tuple[Point, ...] = (E1, (-1, 0, 0), E2, (0, -1, 0), E3, (0, 0, -1))


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def scale(n: int, point: Point) -> Point:
    return (n * point[0], n * point[1], n * point[2])


def distance(left: Point, right: Point) -> int:
    return sum(abs(a - b) for a, b in zip(left, right, strict=True))


def neighbors(site: Point) -> frozenset[Point]:
    """The open six-neighbor set in the declared cubic graph."""
    return frozenset(add(site, shift) for shift in SHIFTS)


def moore_neighbors(site: Point) -> frozenset[Point]:
    offsets = (
        offset
        for offset in product((-1, 0, 1), repeat=3)
        if offset != ORIGIN
    )
    return frozenset(add(site, offset) for offset in offsets)


def condition_union(sites: tuple[Point, ...]) -> frozenset[Point]:
    return frozenset().union(*(neighbors(site) for site in sites))


def pairwise_disjoint(sites: tuple[Point, ...]) -> bool:
    domains = tuple(neighbors(site) for site in sites)
    return all(
        domains[i].isdisjoint(domains[j])
        for i in range(len(domains))
        for j in range(i + 1, len(domains))
    )


def selected_coordinate(site: Point) -> Point:
    """A reproducible condition coordinate used by a nonconstant kernel."""
    return min(neighbors(site))


def local_margin(site: Point, configuration: dict[Point, int]) -> Fraction:
    """Nonconstant Bernoulli margin using one declared NN coordinate."""
    bit = configuration[selected_coordinate(site)]
    if bit not in (0, 1):
        raise ValueError("condition value must be binary")
    return Fraction(1 + bit, 3)


def bernoulli_mass(outcome: int, margin: Fraction) -> Fraction:
    if outcome not in (0, 1):
        raise ValueError("outcome must be binary")
    return margin if outcome else 1 - margin


def product_kernel(
    sites: tuple[Point, ...], configuration: dict[Point, int]
) -> dict[Outcome, Fraction]:
    margins = tuple(local_margin(site, configuration) for site in sites)
    return {
        outcome: product_fraction(
            bernoulli_mass(bit, margin)
            for bit, margin in zip(outcome, margins, strict=True)
        )
        for outcome in product((0, 1), repeat=len(sites))
    }


def product_fraction(values: Iterable[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def correlated_environment_joint() -> dict[tuple[int, int], Fraction]:
    """Two distinct condition coordinates share one fair latent bit."""
    joint: dict[tuple[int, int], Fraction] = {}
    for latent in (0, 1):
        outcome = (latent, latent)
        joint[outcome] = joint.get(outcome, Fraction(0)) + Fraction(1, 2)
    return joint


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_aug10 = PARENT_AUG10_PATH.read_text(encoding="utf-8")
    parent_dyadic = PARENT_DYADIC_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries plus the August 10 and finite-dyadic parent interfaces are source-bound; no observations or fits")
    print("integrity_reads: this runner, its note, the axiom memo, and the two declared parent notes; no other scientific inputs")
    print("construction: exact cubic condition domains and an explicitly supplied nonconstant conditional product kernel")
    print("negative_scope: direct coordinate omission does not itself force stochastic independence, fair margins, formation, or a physical compiler")

    checks.check(
        "audit-inputs",
        "all four declared source-bound inputs exist",
        len(AUDIT_INPUT_PATHS) == 4
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    retired_boundary = "removed the named scalar functional `I`, finite additivity over disjoint record collections, and `I(empty)=0` from Record"
    formation_boundary = "does not supply the formation site, probability, or rate"
    aug10_interface = "physical construction that produces registered measurable event partitions"
    dyadic_boundary = ("auxiliary-register law", "physical compiler", "Record")

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalize(axiom) and lattice_sentence in note)
    checks.check("source-admissibility", "current local-distribution wording is pinned", admissibility_sentence in normalize(axiom) and admissibility_sentence in note)
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence and scalar retirement are pinned",
        all(phrase in normalize(axiom) for phrase in (record_lock, record_content, record_absence, retired_boundary))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check("source-formation-boundary", "formation site/probability/rate remains outside Admissibility", formation_boundary in normalize(axiom) and formation_boundary in normalized_note)
    checks.check("source-parent-aug10", "registered-partition construction remains the August 10 interface", aug10_interface in normalize(parent_aug10) and aug10_interface in normalized_note)
    checks.check("source-parent-dyadic", "finite-dyadic parent keeps the auxiliary law and physical compiler open", all(phrase in parent_dyadic for phrase in dyadic_boundary) and "finite-dyadic parent" in normalized_note)

    two = scale(2, E1)
    three = scale(3, E1)
    six = scale(6, E1)
    nine = scale(9, E1)
    sites = (three, six, nine)

    expected_origin = frozenset((E1, scale(-1, E1), E2, scale(-1, E2), E3, scale(-1, E3)))
    checks.check("neighbor-cardinality", "every executed open neighborhood has six integer sites", all(len(neighbors(site)) == 6 for site in (ORIGIN, E1, two, three, six, nine)))
    checks.check("origin-list", "N(0) is exactly the six axial unit sites", neighbors(ORIGIN) == expected_origin)
    checks.check("adjacent-visibility", "the origin is a direct condition coordinate at e1", ORIGIN in neighbors(E1))
    checks.check("distant-omission", "the origin is absent from N(2e1) and N(3e1)", ORIGIN not in neighbors(two) and ORIGIN not in neighbors(three))
    checks.check("distance-values", "declared axial graph distances are exact", [distance(ORIGIN, point) for point in (E1, two, three, six, nine)] == [1, 2, 3, 6, 9])

    union = condition_union(sites)
    checks.check("spacing3-disjoint", "declared spacing-3 open neighborhoods are pairwise disjoint", pairwise_disjoint(sites))
    checks.check("spacing3-origin-domain", "the three domains contain 18 sites and omit the origin and N(0)", len(union) == 18 and ORIGIN not in union and all(neighbors(site).isdisjoint(neighbors(ORIGIN)) for site in sites), residual=(len(union), ORIGIN in union))
    checks.check("spacing2-contrast", "the axial spacing-2 pair shares exactly e1", neighbors(ORIGIN) & neighbors(two) == frozenset({E1}))
    checks.check("adjacent-open-domains", "adjacent open neighborhoods are disjoint, so spacing 3 is sufficient rather than minimal", neighbors(ORIGIN).isdisjoint(neighbors(E1)))

    box = tuple(product(range(-2, 3), repeat=3))
    intersection_iff_distance2 = all(
        bool(neighbors(left) & neighbors(right)) == (distance(left, right) == 2)
        for left in box
        for right in box
        if left != right
    )
    checks.check("intersection-characterization", "within an exhaustive 5^3 box, distinct open neighborhoods intersect exactly at graph distance two", intersection_iff_distance2)

    base = {point: (sum(abs(c) for c in point) % 2) for point in union | {ORIGIN}}
    origin_changed = dict(base)
    origin_changed[ORIGIN] = 1 - base[ORIGIN]
    kernel_base = product_kernel(sites, base)
    kernel_origin_changed = product_kernel(sites, origin_changed)
    checks.check("kernel-normalization", "the supplied three-site Bernoulli product kernel sums exactly to one", sum(kernel_base.values(), Fraction(0)) == 1 and len(kernel_base) == 8)
    checks.check("origin-invariance", "a change only at the excluded origin coordinate leaves the nonconstant product kernel unchanged", kernel_base == kernel_origin_changed)

    focus = selected_coordinate(three)
    support_changed = dict(base)
    support_changed[focus] = 1 - base[focus]
    kernel_support_changed = product_kernel(sites, support_changed)
    checks.check("nonvacuous-condition-use", "changing one used support coordinate changes the product kernel", kernel_support_changed != kernel_base and local_margin(three, support_changed) != local_margin(three, base))

    adjacent_zero = dict(base)
    adjacent_zero[ORIGIN] = 0
    adjacent_one = dict(base)
    adjacent_one[ORIGIN] = 1
    adjacent_margin_zero = Fraction(1 + adjacent_zero[ORIGIN], 3)
    adjacent_margin_one = Fraction(1 + adjacent_one[ORIGIN], 3)
    checks.check("adjacent-not-guaranteed", "an allowed nonconstant kernel on N(e1) can use the visible origin coordinate", ORIGIN in neighbors(E1) and adjacent_margin_zero == Fraction(1, 3) and adjacent_margin_one == Fraction(2, 3))

    joint = correlated_environment_joint()
    margin_left = sum(mass for (left, _), mass in joint.items() if left == 1)
    margin_right = sum(mass for (_, right), mass in joint.items() if right == 1)
    checks.check("correlated-environment", "distinct support coordinates can be fair yet perfectly correlated", joint == {(0, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)} and margin_left == margin_right == Fraction(1, 2))
    checks.check("marginal-independence-not-forced", "the correlated joint differs from the product of its fair margins", joint.get((1, 1), Fraction(0)) == Fraction(1, 2) and margin_left * margin_right == Fraction(1, 4))

    biased = (Fraction(1, 3), Fraction(2, 3), Fraction(3, 4))
    checks.check("fairness-not-forced", "valid Bernoulli margins need not equal one half", all(0 < margin < 1 and margin != Fraction(1, 2) for margin in biased))
    checks.check("formation-not-derived", "the source-bound formation residual is not replaced by geometry", formation_boundary in normalized_note and "formation" in note.lower())

    diagonal = add(E1, E2)
    checks.check("mutation-moore", "a diagonal distance-two site excludes the origin under six-neighbor adjacency but includes it under Moore adjacency", distance(ORIGIN, diagonal) == 2 and ORIGIN not in neighbors(diagonal) and ORIGIN in moore_neighbors(diagonal) and len(moore_neighbors(diagonal)) == 26)
    checks.check("mutation-overlap", "replacing spacing 3 by the declared spacing-2 axis family breaks disjointness", pairwise_disjoint(sites) and not pairwise_disjoint((two, scale(4, E1), six)))

    allowed_retained = ("audit_required_before_effective_retained: true", "bare_retained_allowed: false")
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: upstream_support",
        "reachability_to_target: supports",
        'hypothetical_axiom_status: "no edit"',
        "direct-coordinate invariance",
        "not stochastic independence",
        "correlated-environment counterexample",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
    )
    forbidden = (
        "For any finite collection of pairwise-disjoint records",
        "scalar readout `I` is additive",
        "I(empty)=0",
        "conditional independence compiler",
        "disjoint if and only if",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
    )
    checks.check(
        "note-contract",
        "machine fields, semantic boundary, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in normalized_note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "new axiom" not in note.lower()
        and "Block 12" not in note
        and "toe-lphys" not in note,
    )

    print("per_element: origin visibility and omission are checked on named cubic sites and exact six-coordinate domains")
    print("per_site: supplied local kernels are tested with nonconstant dependence on an actual nearest-neighbor coordinate")
    print("per_mode: checked and not executed — no spectral or harmonic mode claim occurs in this finite graph theorem")
    print("per_block: the three-site conditional product and two-site correlated-environment counterexample are executed")
    print("lattice_wide: checked and not executed — no global independence, formation, or physical register compiler is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
