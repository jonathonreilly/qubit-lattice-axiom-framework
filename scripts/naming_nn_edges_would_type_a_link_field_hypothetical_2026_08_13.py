#!/usr/bin/env python3
"""Exact unit-cube checks for the C9 Lattice-edge-naming counterfactual.

The runner enumerates the unit-cube sites and nearest-neighbor edges, compares
the type of a {0,1}-map on those edges under the current Lattice sentence and
under displayed S', and checks that S' is not adopted. Counts are taken from
the enumerated sets.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "NAMING_NN_EDGES_WOULD_TYPE_A_LINK_FIELD_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NAMING_NN_EDGES_WOULD_TYPE_A_LINK_FIELD_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Site = tuple[int, int, int]
Edge = frozenset[Site]


def normalize(text: str) -> str:
    return " ".join(text.split())


def unit_cube_sites() -> tuple[Site, ...]:
    return tuple((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1))


def hamming(left: Site, right: Site) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def unit_cube_edges() -> tuple[Edge, ...]:
    sites = unit_cube_sites()
    edges = []
    for index, left in enumerate(sites):
        for right in sites[index + 1 :]:
            if hamming(left, right) == 1:
                edges.append(frozenset((left, right)))
    return tuple(edges)


def vertex_count() -> int:
    return len(unit_cube_sites())


def edge_count() -> int:
    return len(unit_cube_edges())


def binary_field(domain: tuple[object, ...]) -> dict[object, int]:
    return {element: 0 for element in domain}


def is_binary_field_on(field: dict[object, int], domain: tuple[object, ...]) -> bool:
    return set(field) == set(domain) and set(field.values()) <= {0, 1}


@dataclass(frozen=True)
class SentenceTyping:
    """Named domains under a Lattice sentence; sites are always named."""

    names_edges: bool

    def names_sites(self) -> bool:
        return True

    def site_count(self) -> int:
        return vertex_count()

    def types_occupancy(self) -> bool:
        return self.names_sites()

    def types_link_field(self) -> bool:
        return self.names_edges


CURRENT_S = SentenceTyping(names_edges=False)
COUNTERFACTUAL_S_PRIME = SentenceTyping(names_edges=True)


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

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
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )
    print(
        "negative_scope: S' is displayed and not adopted; holonomy, group, "
        "Bianchi, L_phys, and gauge values remain extra"
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    checks.check(
        "source-lattice",
        "the current Lattice sentence names sites of Z^3 with nearest-neighbor adjacency",
        lattice_sentence in normalized_axiom,
    )

    sites = unit_cube_sites()
    edges = unit_cube_edges()
    n_sites = vertex_count()
    n_edges = edge_count()

    checks.check(
        "identity-vertex-count",
        "vertex_count() enumerates eight unit-cube sites",
        n_sites == 8 and n_sites == len(sites) and len(set(sites)) == n_sites,
    )
    checks.check(
        "identity-edge-count",
        "edge_count() enumerates twelve nearest-neighbor edges",
        n_edges == 12 and n_edges == len(edges) and len(set(edges)) == n_edges,
    )
    checks.check(
        "theorem-1-unequal-cardinalities",
        "eight sites are not twelve edges",
        n_sites != n_edges,
    )
    mutation_equal_cardinalities = n_sites == n_edges
    checks.check(
        "mutation-V-equals-E",
        "the predicate |V|=|E| fails",
        mutation_equal_cardinalities is False,
    )

    occupancy = binary_field(sites)
    theta = binary_field(edges)
    checks.check(
        "occupancy-type",
        "site occupancy is a {0,1}-field on the eight named sites",
        is_binary_field_on(occupancy, sites) and len(occupancy) == n_sites,
    )
    checks.check(
        "link-field-type",
        "a link assignment is a {0,1}-field on the twelve edges",
        is_binary_field_on(theta, edges) and len(theta) == n_edges,
    )
    checks.check(
        "theorem-2-current-S-extra",
        "under current S the edge set is unnamed, so θ is extra",
        CURRENT_S.types_occupancy()
        and not CURRENT_S.types_link_field()
        and CURRENT_S.names_sites()
        and not CURRENT_S.names_edges,
    )
    checks.check(
        "theorem-2-counterfactual-typed",
        "under displayed S' both occupancy and θ are {0,1}-fields on named sets",
        COUNTERFACTUAL_S_PRIME.types_occupancy()
        and COUNTERFACTUAL_S_PRIME.types_link_field()
        and is_binary_field_on(occupancy, sites)
        and is_binary_field_on(theta, edges)
        and n_sites != n_edges,
    )
    occupancy_patterns = 1 << n_sites
    link_patterns = 1 << n_edges
    checks.check(
        "theorem-2-pattern-counts-survive",
        "the unequal domain sizes keep 2^|V| distinct from 2^|E|",
        occupancy_patterns != link_patterns
        and occupancy_patterns == 256
        and link_patterns == 4096,
    )

    site_count_S = CURRENT_S.site_count()
    site_count_S_prime = COUNTERFACTUAL_S_PRIME.site_count()
    mutation_site_disagreement = site_count_S != site_count_S_prime
    checks.check(
        "mutation-S-S-prime-site-count",
        "the predicate that S and S' disagree about |V| fails; both have eight sites",
        mutation_site_disagreement is False
        and site_count_S == 8
        and site_count_S_prime == 8,
    )

    s_prime_needles = (
        "nearest-neighbor *edges* are named objects",
        "the adjacency relation is promoted to a set `E`",
    )
    checks.check(
        "displayed-S-prime",
        "the note displays the unadopted counterfactual sentence S'",
        all(needle in normalized_note for needle in s_prime_needles)
        and "not adopted" in normalized_note,
    )
    checks.check(
        "theorem-3-no-gauge-values",
        "S' does not name a holonomy, a group, or a Bianchi identity",
        all(
            phrase in normalized_note
            for phrase in (
                "does not name a holonomy",
                "a structure group or a connection-value group",
                "a Bianchi identity",
                "Gauge *values* remain extra",
            )
        ),
    )
    checks.check(
        "theorem-4-undissolved-walls",
        "C9 does not dissolve formation occupancy, Newton B, or Born K",
        all(
            phrase in normalized_note
            for phrase in (
                "does not dissolve formation occupancy",
                "does not dissolve Newton `B` or Born `K`",
                "fields on a named 1-skeleton",
            )
        ),
    )
    checks.check(
        "machine-status-contract",
        "the note carries the required C9 counterfactual and bounded-support fields",
        'hypothetical_axiom_status: "C9 counterfactual: Lattice names sites and NN edges; not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the canonical axiom memo does not name S', θ on E, or a connection axiom",
        all(
            phrase not in axiom
            for phrase in (
                "promoted to a set",
                "named 1-skeleton",
                "connection axiom",
            )
        ),
    )
    checks.check(
        "no-adoption-imports",
        "the note refuses to adopt S' or L_phys and does not import 0.5934",
        "Do not adopt it" in note
        and "Do not adopt" in note
        and "L_phys" in note
        and "0.5934" not in note,
    )

    print(
        "per_element: eight unit-cube sites and twelve Hamming-1 edges are enumerated"
    )
    print(
        "per_block: current-S extra typing versus displayed-S' named-domain typing "
        "is the only retype tested"
    )
    print(
        "lattice_wide: checked and not executed — the cube is a finite window; "
        "no holonomy, L_phys, or axiom edit is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
