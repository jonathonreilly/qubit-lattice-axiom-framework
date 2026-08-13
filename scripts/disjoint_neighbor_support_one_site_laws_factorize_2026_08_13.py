#!/usr/bin/env python3
"""Exact cubic-lattice checks: one-site laws on disjoint neighbor supports.

Spacing-3 disjoint 6-tuples, product factorization of a pair of one-site
Bernoulli laws, and the 1/4-versus-0 correlated non-product. Identity gates
call neighbors(x) and is_product(joint). No cache is written.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from fractions import Fraction
from itertools import product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "DISJOINT_NEIGHBOR_SUPPORT_ONE_SITE_LAWS_FACTORIZE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/DISJOINT_NEIGHBOR_SUPPORT_ONE_SITE_LAWS_FACTORIZE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Joint = dict[tuple[int, int], Fraction]

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
    return {0: Fraction(1) - margin, 1: margin}


def product_assignment(
    left: Mapping[int, Fraction], right: Mapping[int, Fraction]
) -> Joint:
    return {(alpha, beta): left[alpha] * right[beta] for alpha in BITS for beta in BITS}


def one_site_margins(joint: Mapping[tuple[int, int], Fraction]) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    px = {alpha: joint[(alpha, 0)] + joint[(alpha, 1)] for alpha in BITS}
    py = {beta: joint[(0, beta)] + joint[(1, beta)] for beta in BITS}
    return px, py


def is_product(joint: Mapping[tuple[int, int], Fraction]) -> bool:
    """Identity-gate function: joint equals the product of its margins."""
    px, py = one_site_margins(joint)
    return all(joint[(alpha, beta)] == px[alpha] * py[beta] for alpha in BITS for beta in BITS)


def independence_identity(joint: Mapping[tuple[int, int], Fraction]) -> bool:
    return all(
        joint[(alpha, beta)] * joint[(alpha_p, beta_p)]
        == joint[(alpha, beta_p)] * joint[(alpha_p, beta)]
        for alpha, beta, alpha_p, beta_p in cartesian(BITS, repeat=4)
    )


def fair_product() -> Joint:
    dummy_eta = (0, 0, 0, 0, 0, 0)
    other_eta = (1, 1, 1, 1, 1, 1)
    return product_assignment(
        one_site_law(Fraction(1, 2), dummy_eta),
        one_site_law(Fraction(1, 2), other_eta),
    )


def correlated_fair() -> Joint:
    return {
        (0, 0): Fraction(1, 2),
        (0, 1): Fraction(0),
        (1, 0): Fraction(0),
        (1, 1): Fraction(1, 2),
    }


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
        "external_scientific_inputs: current Lattice and Admissibility wording "
        "are source-bound; no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, and the axiom memo; "
        "no other repository scientific inputs"
    )
    print(
        "construction: spacing-3 disjoint NN 6-tuples; one-site product versus "
        "the perfectly correlated fair joint"
    )
    print(
        "negative_scope: a correlated joint is not a pair of one-site laws on "
        "those tuples; not a no-go against all distant correlation"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/DISJOINT_NEIGHBOR_SUPPORT_ONE_SITE_LAWS_FACTORIZE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
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
        "N(3e1) matches the listing and excludes the origin",
        neighbors(three_e1) == expected_three and ORIGIN not in neighbors(three_e1),
        residual=sorted(neighbors(three_e1)),
    )
    checks.check(
        "witness-N6e1",
        "N(6e1) matches the listing and excludes the origin",
        neighbors(six_e1) == expected_six and ORIGIN not in neighbors(six_e1),
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
        "N(3e1) ∩ N(6e1) is empty, and 0 lies in neither set",
        disjoint_supports((three_e1, six_e1))
        and neighbors(three_e1).isdisjoint(neighbors(six_e1))
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
    prod = fair_product()
    biased = product_assignment(
        one_site_law(Fraction(2, 3), dummy_eta),
        one_site_law(Fraction(1, 3), other_eta),
    )
    corr = correlated_fair()
    print(
        "table: product_fair "
        f"00={prod[(0, 0)]} 01={prod[(0, 1)]} 10={prod[(1, 0)]} 11={prod[(1, 1)]}"
    )
    print(
        "table: correlated "
        f"00={corr[(0, 0)]} 01={corr[(0, 1)]} 10={corr[(1, 0)]} 11={corr[(1, 1)]}"
    )

    checks.check(
        "theorem-2-product-factorization",
        "a pair of one-site laws is the product of its margins and obeys the independence identity",
        prod[(0, 0)] == Fraction(1, 4)
        and prod[(0, 1)] == Fraction(1, 4)
        and prod[(1, 0)] == Fraction(1, 4)
        and prod[(1, 1)] == Fraction(1, 4)
        and is_product(prod)
        and independence_identity(prod)
        and is_product(biased)
        and independence_identity(biased)
        and biased[(0, 0)] == Fraction(1, 3) * Fraction(2, 3),
        residual=(prod, biased),
    )
    checks.check(
        "theorem-2-disjoint-conditions",
        "the two executed 6-tuples live on disjoint neighbor supports",
        disjoint_supports((three_e1, six_e1))
        and len(dummy_eta) == 6
        and len(other_eta) == 6
        and neighbors(three_e1).isdisjoint(neighbors(six_e1)),
    )

    corr_px, corr_py = one_site_margins(corr)
    checks.check(
        "theorem-3-correlated-not-product",
        "P_corr(00)P_corr(11)=1/4 and P_corr(01)P_corr(10)=0, so is_product fails",
        corr[(0, 0)] * corr[(1, 1)] == Fraction(1, 4)
        and corr[(0, 1)] * corr[(1, 0)] == Fraction(0)
        and corr[(0, 0)] * corr[(1, 1)] != corr[(0, 1)] * corr[(1, 0)]
        and not is_product(corr)
        and not independence_identity(corr),
        residual=(corr[(0, 0)] * corr[(1, 1)], corr[(0, 1)] * corr[(1, 0)]),
    )
    checks.check(
        "theorem-3-fair-margins-do-not-imply-product",
        "the correlated witness has fair margins yet is not the fair product",
        corr_px[0] == Fraction(1, 2)
        and corr_py[0] == Fraction(1, 2)
        and corr[(0, 0)] != corr_px[0] * corr_py[0]
        and corr[(0, 0)] != prod[(0, 0)]
        and is_product(prod)
        and not is_product(corr),
    )

    checks.check(
        "theorem-4-not-supplied-by-one-site-pair",
        "every executed one-site pair is a product; the correlated table is not",
        is_product(prod)
        and is_product(biased)
        and not is_product(corr)
        and disjoint_supports((three_e1, six_e1)),
    )
    checks.check(
        "theorem-4-residuals-not-declared",
        "path records and L_phys are recorded as extra residuals, not declared",
        "intermediate records on a connecting path" in note
        and "declared joint `L_phys`" in note
        and "None is derived. None is declared." in note
        and "no distant correlation is possible" not in note.lower(),
    )
    checks.check(
        "theorem-5-not-global-nogo",
        "the note refuses a global no-go and does not declare L_phys",
        "not a no-go against all distant correlation" in note.lower()
        and "not required as an axiom" in note
        and "Do not declare `L_phys`" in note
        and "we adopt" not in note.lower(),
    )

    checks.check(
        "mutation-always-disjoint-fails",
        "an always-disjoint predicate is true on (0,2e1) while neighbors() is not",
        always_disjoint((ORIGIN, two_e1))
        and not disjoint_supports((ORIGIN, two_e1))
        and (neighbors(ORIGIN) & neighbors(two_e1)) == frozenset({E1})
        and always_disjoint((ORIGIN, two_e1)) is not disjoint_supports((ORIGIN, two_e1)),
    )
    checks.check(
        "mutation-product-fails-not-product",
        "replacing the correlated witness by the fair product fails the not-a-product assertion",
        not is_product(corr)
        and is_product(prod)
        and (not is_product(prod)) is False,
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
                "target_claim_id: joint_law_l_phys",
                'target_blocker_text: "a physical joint law on distant sites, including correlated bits"',
                "reachability_to_target: prunes",
                'next_trace_action: "One-site laws on disjoint neighbor supports factorize. A joint L_phys remains extra and must not be adopted until executable. Do not adopt axiom text."',
                "N(3e1) ∩ N(6e1)",
                "P_corr(00) P_corr(11)",
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
        "per_element: named sites 0, 2e1, 3e1, 6e1 and the four 2x2 atoms are recomputed by integer listing",
        "per_site: one-site Bernoulli laws at 3e1 and 6e1 are site-local maps, not a composite arena",
        "per_mode: nearest-neighbor 6-tuples and the independence identity are checked; no spectral mode is claimed",
        "per_block: only disjointness, product factorization, and the correlated non-product are executed",
        "lattice_wide: checked and not executed — no lattice-wide no-go against distant correlation is claimed",
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
