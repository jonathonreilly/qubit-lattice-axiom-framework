#!/usr/bin/env python3
"""Exact 0-skeleton vs 1-skeleton checks on the unit cube.

Identity gates call vertex_count() and edge_count(). The predicate
|V| = |E| must fail because 8 != 12. Occupancy patterns are 2^8;
link fields are 2^12. No holonomy, Bianchi, or axiom edit is performed.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 60

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "CUBE_HAS_EIGHT_VERTICES_AND_TWELVE_EDGES_OCCUPANCY_IS_NOT_CONNECTION_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_HAS_EIGHT_VERTICES_AND_TWELVE_EDGES_OCCUPANCY_IS_NOT_CONNECTION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vertex = tuple[int, int, int]
Edge = tuple[Vertex, Vertex]


def vertices() -> tuple[Vertex, ...]:
    return tuple(product((0, 1), repeat=3))


def edges() -> tuple[Edge, ...]:
    verts = vertices()
    found: list[Edge] = []
    for index, left in enumerate(verts):
        for right in verts[index + 1 :]:
            if sum(a != b for a, b in zip(left, right)) == 1:
                found.append((left, right))
    return tuple(found)


def vertex_count() -> int:
    return len(vertices())


def edge_count() -> int:
    return len(edges())


def occupancy_count() -> int:
    return 2 ** vertex_count()


def link_field_count() -> int:
    return 2 ** edge_count()


def identity_vertex_gate() -> bool:
    return vertex_count() == 8


def identity_edge_gate() -> bool:
    return edge_count() == 12


def vertices_equal_edges_predicate() -> bool:
    return vertex_count() == edge_count()


def normalize(text: str) -> str:
    return " ".join(text.split())


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
    note_norm = normalize(note)
    axiom_norm = normalize(axiom)

    print("external_scientific_inputs: current axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("measure_boundary: exact finite enumeration of V={0,1}^3 and its 1-skeleton")
    print("negative_scope: occupancy is not identified with a connection; no holonomy or Bianchi is computed")

    verts = vertices()
    eds = edges()

    checks.check(
        "identity-vertex-gate",
        "identity gate calls vertex_count() and obtains 8",
        identity_vertex_gate() and vertex_count() == 8,
    )
    checks.check(
        "identity-edge-gate",
        "identity gate calls edge_count() and obtains 12",
        identity_edge_gate() and edge_count() == 12,
    )
    checks.check(
        "vertex-set",
        "V is exactly the product {0,1}^3",
        set(verts) == set(product((0, 1), repeat=3)) and len(verts) == vertex_count(),
    )
    checks.check(
        "edge-rule",
        "every edge differs in exactly one coordinate and E has edge_count() members",
        all(sum(a != b for a, b in zip(left, right)) == 1 for left, right in eds)
        and len(eds) == edge_count()
        and len(set(tuple(sorted((left, right))) for left, right in eds)) == edge_count(),
    )
    checks.check(
        "handshaking",
        "each of the eight vertices has degree three, so 2|E|=24",
        all(
            sum(sum(a != b for a, b in zip(vertex, other)) == 1 for other in verts) == 3
            for vertex in verts
        )
        and 2 * edge_count() == vertex_count() * 3,
    )
    checks.check(
        "mutation-equal-cardinality",
        "the predicate |V|=|E| fails because vertex_count() != edge_count()",
        vertices_equal_edges_predicate() is False
        and vertex_count() != edge_count()
        and vertex_count() == 8
        and edge_count() == 12,
    )
    checks.check(
        "no-bijection",
        "there is no bijection V <-> E",
        vertex_count() != edge_count(),
    )
    checks.check(
        "occupancy-count",
        "occupancy patterns are 2^8 = 256",
        occupancy_count() == 2 ** vertex_count() == 256,
    )
    checks.check(
        "link-field-count",
        "link fields are 2^12 = 4096",
        link_field_count() == 2 ** edge_count() == 4096,
    )
    checks.check(
        "unequal-configuration-sets",
        "256 occupancy patterns are not 4096 link fields",
        occupancy_count() != link_field_count(),
    )
    checks.check(
        "source-lattice",
        "Lattice names sites of Z^3 with nearest-neighbor adjacency",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency"
        in axiom_norm,
    )
    checks.check(
        "source-record",
        "Record locks a possibility at a site",
        "a record locks exactly one admissible local possibility" in axiom_norm
        and "conditional on formation at that site" in axiom_norm,
    )
    checks.check(
        "note-quotes-parents",
        "the note quotes Lattice sites/NN adjacency and Record locking at a site",
        "points of the cubic lattice `Z^3`" in note
        and "nearest-neighbor adjacency" in note
        and "locks a possibility at a site" in note,
    )
    checks.check(
        "note-displays-theta",
        "the note displays theta as a map on edges and refuses a connection axiom",
        "θ : E -> {0,1}" in note
        and "does not add a connection axiom" in note
        and "not a holonomy computation and is not Bianchi" in note,
    )
    checks.check(
        "note-integers-only",
        "the note uses the exact integer counts and makes no four-dimensional SU(3) claim",
        "|V| = 8" in note
        and "|E| = 12" in note
        and "2^8 = 256" in note
        and "2^{12} = 4096" in note
        and "does not claim four-dimensional `SU(3)`" in note,
    )
    checks.check(
        "forbidden-surface",
        "the note contains none of L_phys, 0.5934, or we adopt",
        "L_phys" not in note
        and "0.5934" not in note
        and "we adopt" not in note.lower(),
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
        "audit-inputs",
        "AUDIT_INPUT_PATHS is the new note and the axiom memo only",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_HAS_EIGHT_VERTICES_AND_TWELVE_EDGES_OCCUPANCY_IS_NOT_CONNECTION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "canonical-nonmutation",
        "the displayed link-field notation is absent from the canonical axiom file",
        "θ : E" not in axiom and "link field" not in axiom_norm,
    )

    print("per_element: eight vertices and twelve edges of the unit cube are enumerated")
    print("per_site: occupancy is typed on V; Record locking remains site-local")
    print("per_mode: no spectral or continuum mode is claimed")
    print("per_block: the 0-skeleton versus 1-skeleton inequality is the only negative block")
    print("lattice_wide: checked and not executed — Z^3 is quoted from Lattice; the identity is the unit cube")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
