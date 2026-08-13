#!/usr/bin/env python3
"""Exact checks: the Admissibility 6-site star is not a 4-link plaquette.

Identity gates call star_size() and plaquette_link_count(). All counts are
exact integers. The hostile predicate |S|=|L| must fail (6 != 4).
"""

from __future__ import annotations

import ast
import inspect
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SIX_STAR_IS_NOT_A_FOUR_LINK_PLAQUETTE"
    "_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_SIX_STAR_IS_NOT_A_FOUR_LINK_PLAQUETTE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec = tuple[int, int, int]
Link = tuple[Vec, Vec]

E1: Vec = (1, 0, 0)
E2: Vec = (0, 1, 0)
E3: Vec = (0, 0, 1)
ORIGIN: Vec = (0, 0, 0)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add_vec(left: Vec, right: Vec) -> Vec:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub_vec(left: Vec, right: Vec) -> Vec:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def l1_norm(vector: Vec) -> int:
    return abs(vector[0]) + abs(vector[1]) + abs(vector[2])


def star_sites() -> tuple[Vec, ...]:
    return (
        E1,
        (-1, 0, 0),
        E2,
        (0, -1, 0),
        E3,
        (0, 0, -1),
    )


def plaquette_links() -> tuple[Link, ...]:
    corner = add_vec(E1, E2)
    return (
        (ORIGIN, E1),
        (E1, corner),
        (corner, E2),
        (E2, ORIGIN),
    )


def star_size() -> int:
    return len(star_sites())


def plaquette_link_count() -> int:
    return len(plaquette_links())


def identity_star_size() -> int:
    """Identity gate for the neighbor-site star. Must call star_size()."""
    return star_size()


def identity_plaquette_link_count() -> int:
    """Identity gate for the unit-square links. Must call plaquette_link_count()."""
    return plaquette_link_count()


def predicate_star_size_equals_plaquette_link_count() -> bool:
    """Hostile identification: the six-site star has the same count as L."""
    return identity_star_size() == identity_plaquette_link_count()


def displayed_pairing() -> tuple[tuple[Link, Vec], ...]:
    """Extra site-versus-edge pairing. Displayed; not adopted."""
    sites = star_sites()
    links = plaquette_links()
    return tuple((links[index], sites[index]) for index in range(plaquette_link_count()))


def unused_star_sites() -> tuple[Vec, ...]:
    paired = {site for _link, site in displayed_pairing()}
    return tuple(site for site in star_sites() if site not in paired)


def neighbor_tuple(values: tuple[int, ...]) -> tuple[int, ...]:
    if len(values) != star_size():
        raise ValueError("neighbor function expects one value per star site")
    return values


def link_angle_tuple(values: tuple[int, ...]) -> tuple[int, ...]:
    if len(values) != plaquette_link_count():
        raise ValueError("link function expects one value per plaquette link")
    return values


def function_calls(name: str) -> set[str]:
    source = inspect.getsource(globals()[name])
    tree = ast.parse(source)
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            names.add(node.func.id)
    return names


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
    runner_text = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: current axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: proposed source note plus axiom memo")
    print("audit_input_paths: " + ", ".join(AUDIT_INPUT_PATHS))

    sites = star_sites()
    links = plaquette_links()
    corner = add_vec(E1, E2)

    checks.check(
        "audit-inputs",
        "declared inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_SIX_STAR_IS_NOT_A_FOUR_LINK_PLAQUETTE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "source-lattice",
        "Lattice names nearest-neighbor adjacency of sites of Z^3",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "nearest-neighbor adjacency" in axiom_norm,
    )
    checks.check(
        "source-admissibility",
        "Admissibility determines the site distribution by nearest-neighbor conditions",
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
        in axiom_norm,
    )

    checks.check(
        "identity-star-size",
        "identity gate: identity_star_size calls star_size and returns 6",
        "star_size" in function_calls("identity_star_size")
        and identity_star_size() == 6
        and star_size() == 6
        and len(sites) == 6
        and len(set(sites)) == 6
        and all(l1_norm(site) == 1 for site in sites)
        and ORIGIN not in sites
        and corner not in sites,
    )
    checks.check(
        "identity-plaquette-link-count",
        "identity gate: identity_plaquette_link_count calls plaquette_link_count and returns 4",
        "plaquette_link_count" in function_calls("identity_plaquette_link_count")
        and identity_plaquette_link_count() == 4
        and plaquette_link_count() == 4
        and len(links) == 4
        and len(set(links)) == 4
        and all(l1_norm(sub_vec(head, tail)) == 1 for tail, head in links)
        and links == ((ORIGIN, E1), (E1, corner), (corner, E2), (E2, ORIGIN)),
    )
    checks.check(
        "theorem-1-no-bijection",
        "six neighbor sites are not in bijection with four plaquette links",
        star_size() == 6
        and plaquette_link_count() == 4
        and star_size() != plaquette_link_count()
        and len(sites) != len(links),
    )
    mutation = predicate_star_size_equals_plaquette_link_count()
    checks.check(
        "mutation-cardinalities-equal",
        "predicate '|S|=|L|' fails because 6 != 4",
        mutation is False
        and identity_star_size() != identity_plaquette_link_count()
        and 6 != 4,
    )
    checks.check(
        "types-sites-versus-edges",
        "star members are sites; plaquette members are edges",
        all(isinstance(site, tuple) and len(site) == 3 for site in sites)
        and all(
            isinstance(link, tuple)
            and len(link) == 2
            and all(isinstance(end, tuple) and len(end) == 3 for end in link)
            for link in links
        )
        and all(not isinstance(site[0], tuple) for site in sites),
    )
    pairing = displayed_pairing()
    unused = unused_star_sites()
    neighbor_values = neighbor_tuple((0, 1, 0, 1, 0, 1))
    link_values = link_angle_tuple((0, 0, 0, 1))
    checks.check(
        "theorem-3-pairing-extra",
        "displayed pairing is extra: four pairs, two unused sites, unequal arities",
        len(pairing) == 4
        and unused == (E3, (0, 0, -1))
        and len(neighbor_values) == 6
        and len(link_values) == 4
        and len(neighbor_values) != len(link_values)
        and all(pair[0] in links and pair[1] in sites for pair in pairing),
    )

    required_note = (
        "`|S|=6`",
        "`|L|=4`",
        "There is no bijection of neighbor sites to plaquette links",
        "Neither sentence names a four-link holonomy",
        "Do not adopt a holonomy axiom",
        "16-atom product",
        "Do not adopt `L_phys`",
        "`N_p=1`",
        "Not June 10",
        "Do not import `0.5934`",
        "### N5 — rhetoric and resolution audit (Theorem 5)",
    )
    checks.check(
        "note-theorems",
        "the source note states Theorems 1-5 and the N5 fence on Theorem 5",
        all(needle in note for needle in required_note)
        and "## Theorem 5" in note
        and "minimal_axioms" in note
        and "holo" + "type" not in note.lower()
        and "cube" + "bianchi" not in note.lower()
        and "#61" + "90" not in note
        and "#61" + "96" not in note,
    )
    checks.check(
        "note-axiom-quotes",
        "the note quotes Lattice adjacency and the Admissibility distribution sentence",
        "nearest-neighbor adjacency" in note_norm
        and "determined by, and varies with, the nearest-neighbor conditions"
        in note_norm
        and "the 6-tuple of neighboring possibilities" in note,
    )
    checks.check(
        "theorem-5-one-square",
        "N_p of this one square is 1 and is not 96",
        1 != 96
        and "`N_p=1`" in note
        and "not `96`" in note_norm
        and "0.5934" in note
        and "Do not import `0.5934`" in note,
    )
    adopt_phrase = "we" + " adopt"
    checks.check(
        "display-not-adopt",
        "the pairing is displayed and a holonomy axiom is not adopted",
        "Display one extra pairing; do not adopt it." in note
        and adopt_phrase not in note.lower()
        and "Do not adopt a holonomy axiom" in note
        and "Do not adopt `L_phys`" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "upstream_dependencies:" in note
        and "- minimal_axioms" in note,
    )
    checks.check(
        "forbidden-rhetoric",
        "note and runner avoid adoption rhetoric and unmerged-PR citations",
        adopt_phrase not in note.lower()
        and adopt_phrase not in runner_text.lower()
        and "#61" + "90" not in runner_text
        and "#61" + "96" not in runner_text
        and "holo" + "type" not in runner_text.lower()
        and "cube" + "bianchi" not in runner_text.lower(),
    )

    print("per_element: six star sites and four plaquette links are enumerated exactly")
    print("negative_scope: only the 6-versus-4 site/edge split is decided; no holonomy law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
