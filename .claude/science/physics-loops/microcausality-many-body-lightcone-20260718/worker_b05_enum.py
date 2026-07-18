#!/usr/bin/env python3
"""Exact finite-box enumeration of bond/plaquette adjacency on Z^3."""

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, product


Site = tuple[int, int, int]


@dataclass(frozen=True, order=True)
class Term:
    kind: str
    sites: tuple[Site, ...]


ORIGIN: Site = (0, 0, 0)
UNITS: tuple[Site, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(*sites: Site) -> Site:
    return tuple(sum(values) for values in zip(*sites))  # type: ignore[return-value]


def make_term(kind: str, sites: set[Site]) -> Term:
    return Term(kind, tuple(sorted(sites)))


def generate_terms(radius: int) -> tuple[set[Term], dict[Site, set[Term]]]:
    coordinates = range(-radius, radius + 1)
    site_set = set(product(coordinates, repeat=3))
    terms: set[Term] = set()

    for anchor in site_set:
        for unit in UNITS:
            endpoint = add(anchor, unit)
            if endpoint in site_set:
                terms.add(make_term("bond", {anchor, endpoint}))

        for i, j in combinations(range(3), 2):
            corner_i = add(anchor, UNITS[i])
            corner_j = add(anchor, UNITS[j])
            opposite = add(anchor, UNITS[i], UNITS[j])
            support = {anchor, corner_i, corner_j, opposite}
            if support <= site_set:
                terms.add(make_term("face", support))

    by_site: dict[Site, set[Term]] = defaultdict(set)
    for term in terms:
        for site in term.sites:
            by_site[site].add(term)
    return terms, by_site


def adjacent_terms(term: Term, by_site: dict[Site, set[Term]]) -> set[Term]:
    adjacent: set[Term] = set()
    for site in term.sites:
        adjacent.update(by_site[site])
    adjacent.discard(term)
    return adjacent


def l1(a: Site, b: Site) -> int:
    return sum(abs(x - y) for x, y in zip(a, b))


def support_diameter(term: Term) -> int:
    return max(l1(a, b) for a, b in combinations(term.sites, 2))


def fixed_terms() -> tuple[Term, Term]:
    bond = make_term("bond", {ORIGIN, add(ORIGIN, UNITS[0])})
    face = make_term(
        "face",
        {
            ORIGIN,
            add(ORIGIN, UNITS[0]),
            add(ORIGIN, UNITS[1]),
            add(ORIGIN, UNITS[0], UNITS[1]),
        },
    )
    return bond, face


def enumerate_box(radius: int) -> dict[str, object]:
    terms, by_site = generate_terms(radius)
    fixed_bond, fixed_face = fixed_terms()
    assert fixed_bond in terms and fixed_face in terms

    origin_terms = by_site[ORIGIN]
    origin_bonds = {term for term in origin_terms if term.kind == "bond"}
    origin_faces = {term for term in origin_terms if term.kind == "face"}

    bond_neighbors = adjacent_terms(fixed_bond, by_site)
    face_neighbors = adjacent_terms(fixed_face, by_site)
    bond_adj_bonds = {term for term in bond_neighbors if term.kind == "bond"}
    bond_adj_faces = {term for term in bond_neighbors if term.kind == "face"}
    face_adj_bonds = {term for term in face_neighbors if term.kind == "bond"}
    face_adj_faces = {term for term in face_neighbors if term.kind == "face"}

    bond_degree = len(bond_neighbors)
    face_degree = len(face_neighbors)
    maximum_degree = max(bond_degree, face_degree)

    reach_rows: list[tuple[int, int, int]] = []
    terminal_terms = set(origin_terms)
    for walk_length in range(1, 4):
        maximum_reach = max(
            l1(ORIGIN, site)
            for term in terminal_terms
            for site in term.sites
        )
        reach_rows.append((walk_length, len(terminal_terms), maximum_reach))
        terminal_terms = {
            neighbor
            for term in terminal_terms
            for neighbor in adjacent_terms(term, by_site)
        }

    transition_counts = {
        (start_kind, next_kind): 0
        for start_kind in ("bond", "face")
        for next_kind in ("bond", "face")
    }
    for start in origin_terms:
        for neighbor in adjacent_terms(start, by_site):
            transition_counts[(start.kind, neighbor.kind)] += 1
    length_2_walk_count = sum(transition_counts.values())
    product_bound = len(origin_terms) * maximum_degree

    return {
        "radius": radius,
        "total_bonds": sum(term.kind == "bond" for term in terms),
        "total_faces": sum(term.kind == "face" for term in terms),
        "site_bonds": len(origin_bonds),
        "site_faces": len(origin_faces),
        "bond_adj_bonds": len(bond_adj_bonds),
        "bond_adj_faces": len(bond_adj_faces),
        "face_adj_bonds": len(face_adj_bonds),
        "face_adj_faces": len(face_adj_faces),
        "bond_degree": bond_degree,
        "face_degree": face_degree,
        "maximum_degree": maximum_degree,
        "bond_diameter": support_diameter(fixed_bond),
        "face_diameter": support_diameter(fixed_face),
        "reach_rows": reach_rows,
        "origin_terms": len(origin_terms),
        "transition_counts": transition_counts,
        "length_2_walk_count": length_2_walk_count,
        "product_bound": product_bound,
        "within_bound": length_2_walk_count <= product_bound,
    }


def print_result(result: dict[str, object]) -> None:
    radius = result["radius"]
    print(f"=== CENTERED BOX radius={radius}, coordinates=[-{radius},{radius}] ===")
    print(
        f"generated terms: bonds={result['total_bonds']}, "
        f"faces={result['total_faces']}"
    )
    print("TABLE 1 / local incidence and adjacency")
    print(f"bonds incident to X: {result['site_bonds']}")
    print(f"faces containing X: {result['site_faces']}")
    print(f"fixed bond -> adjacent bonds: {result['bond_adj_bonds']}")
    print(f"fixed bond -> adjacent faces: {result['bond_adj_faces']}")
    print(f"fixed face -> adjacent bonds: {result['face_adj_bonds']}")
    print(f"fixed face -> adjacent faces (self excluded): {result['face_adj_faces']}")
    print(f"fixed bond total degree: {result['bond_degree']}")
    print(f"fixed face total degree: {result['face_degree']}")
    print(f"D=max(type degrees): {result['maximum_degree']}")
    print("TABLE 2 / diameters and reach")
    print(f"bond support l1 diameter: {result['bond_diameter']}")
    print(f"face support l1 diameter: {result['face_diameter']}")
    for walk_length, terminal_count, maximum_reach in result["reach_rows"]:  # type: ignore[union-attr]
        comparison = "=" if maximum_reach == 2 * walk_length else ("<" if maximum_reach < 2 * walk_length else ">")
        print(
            f"k={walk_length}: terminal terms={terminal_count}, "
            f"max distance={maximum_reach}, comparison to 2k: {comparison}"
        )
    transitions = result["transition_counts"]
    for start_kind in ("bond", "face"):
        for next_kind in ("bond", "face"):
            print(
                f"length-2 transitions {start_kind}->{next_kind}: "
                f"{transitions[(start_kind, next_kind)]}"  # type: ignore[index]
            )
    print(f"terms containing X: {result['origin_terms']}")
    print(f"exact length-2 mixed-walk count: {result['length_2_walk_count']}")
    print(f"product bound (#start terms)*D: {result['product_bound']}")
    print(f"exact count <= product bound: {result['within_bound']}")
    print()


def main() -> None:
    results = [enumerate_box(radius) for radius in (4, 6)]
    for result in results:
        print_result(result)

    ignored_for_stability = {"radius", "total_bonds", "total_faces"}
    stable_keys = [key for key in results[0] if key not in ignored_for_stability]
    unstable_keys = [key for key in stable_keys if results[0][key] != results[1][key]]
    print("=== BOX-STABILITY CHECK: radius 4 versus radius 6 ===")
    for key in stable_keys:
        print(f"{key}: {results[0][key] == results[1][key]}")
    print(f"all requested quantities stable: {not unstable_keys}")
    print(f"unstable keys: {unstable_keys}")


if __name__ == "__main__":
    main()
