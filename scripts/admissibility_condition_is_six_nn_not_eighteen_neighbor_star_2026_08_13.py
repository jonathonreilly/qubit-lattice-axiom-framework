#!/usr/bin/env python3
"""Exact neighbor-set checks: Admissibility names the 6-NN star, not S18.

The runner builds S6, D, and S18 from the standard generators of Z^3, counts
them, and computes graph distances. Identity gates call nn_count() and
graph_distance(e1+e2). Two hostile predicates are required to fail. A displayed
pair of occupancy laws shows that dependence on an edge-diagonal slot is extra.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_CONDITION_IS_SIX_NN_NOT_EIGHTEEN_NEIGHBOR_STAR_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CONDITION_IS_SIX_NN_NOT_EIGHTEEN_NEIGHBOR_STAR_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


class Vec(tuple):
    """Integer lattice vector with componentwise addition."""

    def __new__(cls, xs):
        return super().__new__(cls, tuple(int(x) for x in xs))

    def __add__(self, other: object) -> "Vec":
        if not isinstance(other, tuple):
            return NotImplemented
        return Vec(a + b for a, b in zip(self, other))

    def __neg__(self) -> "Vec":
        return Vec(-a for a in self)

    def __mul__(self, scalar: object) -> "Vec":
        if not isinstance(scalar, int):
            return NotImplemented
        return Vec(scalar * a for a in self)

    def __rmul__(self, scalar: object) -> "Vec":
        return self.__mul__(scalar)


e1 = Vec((1, 0, 0))
e2 = Vec((0, 1, 0))
e3 = Vec((0, 0, 1))


def graph_distance(displacement: tuple[int, ...]) -> int:
    """Nearest-neighbor path length from the origin on Z^3."""
    return sum(abs(int(component)) for component in displacement)


def s6_set() -> frozenset[Vec]:
    axes = (e1, e2, e3)
    return frozenset(sign * axis for axis in axes for sign in (1, -1))


def d_set() -> frozenset[Vec]:
    axes = (e1, e2, e3)
    out: set[Vec] = set()
    for i in range(3):
        for j in range(i + 1, 3):
            for si in (1, -1):
                for sj in (1, -1):
                    out.add((si * axes[i]) + (sj * axes[j]))
    return frozenset(out)


def s18_set() -> frozenset[Vec]:
    return s6_set() | d_set()


def nn_count() -> int:
    return len(s6_set())


def mu6(occupancy: dict[Vec, int]) -> int:
    return sum(int(occupancy[site]) for site in s6_set())


def mu18(occupancy: dict[Vec, int]) -> int:
    return mu6(occupancy) + int(occupancy[e1 + e2])


def occupancy(occupied: frozenset[Vec]) -> dict[Vec, int]:
    return {site: 1 if site in occupied else 0 for site in s18_set()}


def identity_nn_count() -> int:
    return nn_count()


def identity_edge_diagonal_distance() -> int:
    return graph_distance(e1+e2)


def normalize(text: str) -> str:
    return " ".join(text.split())


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
    note_n = normalize(note)
    axiom_n = normalize(axiom)

    s6 = s6_set()
    d = d_set()
    s18 = s18_set()

    print("external_scientific_inputs: current axiom wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: values of mu6, L_phys, gravity, and any Laplacian remain unselected")

    checks.check(
        "audit-inputs",
        "declared inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_CONDITION_IS_SIX_NN_NOT_EIGHTEEN_NEIGHBOR_STAR_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    checks.check(
        "theorem-1-cardinalities",
        "constructed |S6|=6, |D|=12, |S18|=18 with empty intersection",
        nn_count() == 6
        and len(d) == 12
        and len(s18) == 18
        and s6.isdisjoint(d)
        and s18 == s6 | d,
    )
    checks.check(
        "theorem-1-s6-distance",
        "every vector in S6 has graph distance 1",
        all(graph_distance(site) == 1 for site in s6) and len(s6) == nn_count(),
    )
    checks.check(
        "theorem-1-d-distance",
        "every edge-diagonal has graph distance 2",
        all(graph_distance(site) == 2 for site in d) and len(d) == 12,
    )

    lattice_phrase = "nearest-neighbor adjacency"
    admissibility_sentence = (
        "the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions"
    )
    checks.check(
        "theorem-2-lattice-quote",
        "Lattice names nearest-neighbor adjacency",
        lattice_phrase in axiom_n and lattice_phrase in note_n,
    )
    checks.check(
        "theorem-2-admissibility-quote",
        "Admissibility names nearest-neighbor conditions as the distribution's domain",
        admissibility_sentence in axiom_n and admissibility_sentence in note_n,
    )
    checks.check(
        "theorem-2-six-tuple",
        "the named condition is a 6-tuple, not an 18-tuple",
        "named condition is a 6-tuple, not an 18-tuple" in note_n
        and nn_count() != 18
        and len(s18) == 18,
    )

    omega0 = occupancy(frozenset({e1}))
    omega1 = occupancy(frozenset({e1, e1 + e2}))
    checks.check(
        "theorem-3-mu6-ignores-d",
        "mu6 is unchanged when only an edge-diagonal occupancy flips",
        mu6(omega0) == mu6(omega1) == 1
        and omega0[e1 + e2] != omega1[e1 + e2],
    )
    checks.check(
        "theorem-3-mu18-depends-on-d",
        "mu18 depends on the occupancy of e1+e2",
        mu18(omega0) == 1 and mu18(omega1) == 2 and mu18(omega0) != mu18(omega1),
    )
    checks.check(
        "theorem-3-domain",
        "the displayed pair names mu6's domain, not mu18",
        "Axioms name the domain of `μ6`, not the domain of `μ18`" in note
        or "axioms name the domain of `μ6`, not the domain of `μ18`" in note_n,
    )

    checks.check(
        "theorem-4-nonclaims",
        "note does not adopt L_phys and does not claim gravity or a Laplacian",
        "does not adopt `L_phys`" in note_n
        and "does not claim gravity" in note_n
        and "does not claim a Laplacian" in note_n
        and "does not select the values of `μ6`" in note_n,
    )
    checks.check(
        "theorem-5-no-half-weight",
        "displayed integer laws are not forced to r=1/2",
        mu6(omega0) != 1 / 2
        and mu18(omega1) != 1 / 2
        and "does not force a distinguished half-weight `r = 1/2`" in note_n,
    )

    edge_diagonals_are_nearest_neighbors = all(
        graph_distance(site) == 1 for site in d
    )
    s6_has_eighteen = nn_count() == 18
    checks.check(
        "mutation-edge-diagonals-are-nn",
        "predicate 'edge-diagonals are nearest neighbors' fails",
        edge_diagonals_are_nearest_neighbors is False,
    )
    checks.check(
        "mutation-s6-eq-18",
        "predicate '|S6|=18' fails",
        s6_has_eighteen is False,
    )

    checks.check(
        "identity-nn-count",
        "identity gate calls nn_count() and reads 6",
        identity_nn_count() == 6,
    )
    checks.check(
        "identity-graph-distance",
        "identity gate calls graph_distance(e1+e2) and reads 2",
        identity_edge_diagonal_distance() == 2,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
