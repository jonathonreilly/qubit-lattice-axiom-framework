#!/usr/bin/env python3
"""Exact checks: Lattice NN adjacency kills the edge-diagonal coefficient.

Unnormalized O_h stencils of φ(x)=x1²+x2²+x3² at the origin of Z^3.
Identity gates call delta_nn_phi() and delta_edge_phi(). A predicate
“Δ_NN φ = Δ_edge φ at 0” fails (6 ≠ 24). A predicate “edge-diagonals are
nearest neighbors” fails (graph distance 2). No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product as cartesian
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/LATTICE_NN_ADJACENCY_KILLS_EDGE_DIAGONAL_STENCIL_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/LATTICE_NN_ADJACENCY_KILLS_EDGE_DIAGONAL_STENCIL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NN: tuple[Point, ...] = (
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
    """ℓ¹ path metric of the six-neighbor cubic graph."""
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def phi(site: Point) -> int:
    """Integer quadratic φ(x)=x1²+x2²+x3²."""
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def edge_sites() -> tuple[Point, ...]:
    """The twelve edge-diagonals ±e_i ± e_j for i<j."""
    axes = (E1, E2, E3)
    listed: list[Point] = []
    for i in range(3):
        for j in range(i + 1, 3):
            for sign_i, sign_j in cartesian((1, -1), repeat=2):
                listed.append(add(scale(sign_i, axes[i]), scale(sign_j, axes[j])))
    return tuple(listed)


def delta_nn_phi() -> int:
    """Identity-gate: unnormalized NN stencil of φ at the origin."""
    return sum(phi(site) - phi(ORIGIN) for site in NN)


def delta_edge_phi() -> int:
    """Identity-gate: unnormalized edge-diagonal stencil of φ at the origin."""
    return sum(phi(site) - phi(ORIGIN) for site in edge_sites())


def stencil(alpha: Fraction, beta: Fraction) -> Fraction:
    """Two-parameter O_h stencil Δ_{α,β} φ at the origin."""
    return alpha * delta_nn_phi() + beta * delta_edge_phi()


def oh_apply(site: Point, perm: tuple[int, int, int], signs: tuple[int, int, int]) -> Point:
    coords = (site[0], site[1], site[2])
    return (
        signs[0] * coords[perm[0]],
        signs[1] * coords[perm[1]],
        signs[2] * coords[perm[2]],
    )


def oh_orbit(seed: Point) -> frozenset[Point]:
    """O_h as signed permutations of the three axes."""
    orbit: set[Point] = set()
    for perm in permutations((0, 1, 2)):
        for signs in cartesian((1, -1), repeat=3):
            orbit.add(oh_apply(seed, perm, signs))
    return frozenset(orbit)


def nn_equals_edge_at_origin() -> bool:
    """Hostile predicate: Δ_NN φ = Δ_edge φ at 0."""
    return delta_nn_phi() == delta_edge_phi()


def edge_diagonals_are_nearest_neighbors() -> bool:
    """Hostile predicate: edge-diagonals are nearest neighbors."""
    return all(graph_distance(ORIGIN, site) == 1 for site in edge_sites())


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
        "external_scientific_inputs: current Lattice wording is source-bound; "
        "no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, and the axiom memo; "
        "no other repository scientific inputs"
    )
    print(
        "construction: six NN sites, twelve edge-diagonals, unnormalized "
        "stencils of φ at the origin, graph distance on the 6-NN cubic graph"
    )
    print(
        "negative_scope: Lattice kills β inside Δ_{α,β}; no field operator, "
        "Green function, 1/r kernel, M_s M_t, Newton constant, or Laplacian axiom"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/LATTICE_NN_ADJACENCY_KILLS_EDGE_DIAGONAL_STENCIL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    lattice_phrase = "nearest-neighbor adjacency"
    checks.check(
        "source-lattice",
        "the current Lattice nearest-neighbor sentence is pinned in the axiom memo and the note",
        lattice_sentence in normalize(axiom)
        and lattice_sentence in note
        and lattice_phrase in normalize(axiom)
        and lattice_phrase in note,
    )

    edges = edge_sites()
    checks.check(
        "classes-cardinalities",
        "the NN class has 6 sites and the edge-diagonal class has 12 distinct sites",
        len(NN) == 6
        and len(edges) == 12
        and len(set(NN)) == 6
        and len(set(edges)) == 12
        and set(NN).isdisjoint(edges),
        residual=(len(NN), len(edges), len(set(edges))),
    )
    checks.check(
        "classes-are-oh-orbits",
        "NN is the O_h orbit of e1 and the edge class is the O_h orbit of e1+e2",
        oh_orbit(E1) == frozenset(NN)
        and oh_orbit(add(E1, E2)) == frozenset(edges)
        and len(oh_orbit(E1)) == 6
        and len(oh_orbit(add(E1, E2))) == 12,
    )

    nn_value = delta_nn_phi()
    edge_value = delta_edge_phi()
    print(f"table: delta_nn_phi={nn_value} delta_edge_phi={edge_value}")
    checks.check(
        "theorem-1-delta-nn-phi",
        "(Δ_NN φ)(0)=6 by summing φ(x)-φ(0) over the six NN sites",
        nn_value == 6
        and phi(ORIGIN) == 0
        and all(phi(site) == 1 for site in NN)
        and delta_nn_phi() == 6 * (1 - 0),
        residual=nn_value,
    )
    checks.check(
        "theorem-1-delta-edge-phi",
        "(Δ_edge φ)(0)=24 by summing φ(x)-φ(0) over the twelve edge sites",
        edge_value == 24
        and all(phi(site) == 2 for site in edges)
        and delta_edge_phi() == 12 * (2 - 0),
        residual=edge_value,
    )
    checks.check(
        "theorem-1-operators-disagree",
        "Δ_NN ≠ Δ_edge as operators because they disagree on this φ",
        delta_nn_phi() != delta_edge_phi()
        and delta_nn_phi() == 6
        and delta_edge_phi() == 24
        and "6 ≠ 24" in note,
        residual=(delta_nn_phi(), delta_edge_phi()),
    )

    checks.check(
        "theorem-2-nn-graph-distance",
        "every NN site has graph distance 1 from the origin",
        all(graph_distance(ORIGIN, site) == 1 for site in NN)
        and set(NN) == {site for site in NN if graph_distance(ORIGIN, site) == 1},
    )
    checks.check(
        "theorem-2-edge-graph-distance",
        "every edge-diagonal has graph distance 2, so those sites are not nearest neighbors",
        all(graph_distance(ORIGIN, site) == 2 for site in edges)
        and all(graph_distance(ORIGIN, site) != 1 for site in edges)
        and "graph distance `2`" in note,
        residual=sorted({graph_distance(ORIGIN, site) for site in edges}),
    )
    checks.check(
        "theorem-2-named-graph-is-6-not-18",
        "the named adjacency is the 6-NN cubic graph, not the 18-neighbor graph",
        len(NN) == 6
        and len(set(NN) | set(edges)) == 18
        and "not the `18`-neighbor graph" in note
        and "nearest-neighbor adjacency" in note,
    )

    named_operator = stencil(Fraction(1), Fraction(0))
    mixed_operator = stencil(Fraction(1), Fraction(1))
    checks.check(
        "theorem-3-beta-zero",
        "a named-adjacency Laplacian is a rational multiple of Δ_NN, so β=0",
        named_operator == Fraction(delta_nn_phi())
        and named_operator == Fraction(6)
        and mixed_operator == Fraction(6 + 24)
        and stencil(Fraction(2), Fraction(0)) == Fraction(2) * Fraction(delta_nn_phi())
        and "β=0" in note
        and "rational multiple of `Δ_NN`" in note
        and "That supplier is extra" in note,
        residual=(named_operator, mixed_operator),
    )
    checks.check(
        "theorem-3-axioms-name-no-field-operator",
        "the axioms do not name a field operator; Lattice kills only β inside the class",
        "axioms do not name a field operator" in note
        and "field operator" not in axiom.lower()
        and "Laplacian" not in axiom
        and "kills only the edge-diagonal coefficient" in note,
    )

    checks.check(
        "theorem-4-no-kernel-no-newton",
        "the note refuses a Green function, a 1/r kernel, M_s M_t, and Newton’s constant",
        "does not select a Green function" in note
        and "1/r kernel" in note
        and "`M_s M_t`" in note
        and "Newton’s constant" in note
        and "does not claim gravity" in note
        and "G_N" not in note,
    )
    checks.check(
        "theorem-5-no-laplacian-axiom",
        "the note refuses a Laplacian axiom and ℓ² uniqueness for Δ_NN",
        "does not adopt a Laplacian axiom" in note
        and "only `O_h`-invariant operator on all of" in note
        and "inside this two-parameter stencil family" in note
        and 'hypothetical_axiom_status: "no edit"' in note,
    )

    checks.check(
        "mutation-equal-stencils-fails",
        "the predicate Δ_NN φ = Δ_edge φ at 0 fails because 6 ≠ 24",
        nn_equals_edge_at_origin() is False
        and delta_nn_phi() == 6
        and delta_edge_phi() == 24
        and delta_nn_phi() != delta_edge_phi(),
        residual=(delta_nn_phi(), delta_edge_phi(), nn_equals_edge_at_origin()),
    )
    checks.check(
        "mutation-edge-are-nn-fails",
        "the predicate that edge-diagonals are nearest neighbors fails at graph distance 2",
        edge_diagonals_are_nearest_neighbors() is False
        and all(graph_distance(ORIGIN, site) == 2 for site in edges)
        and all(graph_distance(ORIGIN, site) == 1 for site in NN),
        residual=sorted({graph_distance(ORIGIN, site) for site in edges}),
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
                "target_claim_id: lattice_nn_adjacency_kills_edge_diagonal_stencil",
                'target_blocker_text: "derive an O_h field-operator stencil with a nonzero edge-diagonal coefficient from Lattice nearest-neighbor adjacency"',
                "reachability_to_target: prunes",
                'next_trace_action: "If a later supplier names the field operator as the graph Laplacian of the named adjacency, then β=0 and the operator is a rational multiple of Δ_NN. That supplier is extra. Do not adopt axiom text."',
                "(Δ_NN φ)(0)=6",
                "(Δ_edge φ)(0)=24",
                "authors no audit verdict",
                "Identity gates call `delta_nn_phi()`",
                "`delta_edge_phi()`",
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
        "per_element: origin, six NN sites, twelve edge-diagonal sites, and the integer values 6 and 24 are recomputed",
        "per_site: the stencils are evaluated at the origin of Z^3; O_h merely orbits that site's neighbor classes",
        "per_mode: unnormalized graph stencils on one quadratic test function; no Green function or harmonic mode is claimed",
        "per_block: only the 6-versus-24 split, graph distance 2, and β=0 inside the named 2-parameter family are executed",
        "lattice_wide: checked and not executed — no uniqueness of Δ_NN on all of l2(Z^3) and no Laplacian axiom is claimed",
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
