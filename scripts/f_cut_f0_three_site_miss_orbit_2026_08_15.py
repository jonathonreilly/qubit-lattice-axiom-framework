#!/usr/bin/env python3
"""Orbit type of the eight 3-site seeds F_cut (1,1,1,1,0) misses.

On the two-cube {0,1,2} x {0,1} x {0,1} with off-patch occupancy 0,
f0 is the complement-even cut map with remaining bits
(wt1, opp2, adj2, vertex3, mixed3) = (1,1,1,1,0). This runner
recomputes the 220 three-site seeds, the missed set M, and the
number of orbits of M under two-cube-preserving proper cube
rotations about the box center. Values are derived, not embedded.
"""

from __future__ import annotations

import ast
from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_F0_THREE_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_F0_THREE_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

TWO_CUBE = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
F0_BITS = (1, 1, 1, 1, 0)
L1_BITS = (1, 0, 1, 1, 1)
F1_BITS = (1, 1, 1, 1, 1)
HAMMING_BITS = (1, 0, 0, 1, 1)
# Box center (1, 1/2, 1/2) in doubled coordinates (2, 1, 1).
CENTER_DOUBLED = (2, 1, 1)


def _add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def _sub(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cube_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                rows[i][perm[i]] = signs[i]
            matrix = tuple(tuple(row) for row in rows)
            if _det3(matrix) == 1:
                rotations.append(matrix)
    return tuple(rotations)


def apply_about_center(
    rotation: tuple[tuple[int, int, int], ...],
    site: tuple[int, int, int],
) -> tuple[int, int, int] | None:
    """Exact image of a site under a proper rotation about the box center."""
    doubled = (2 * site[0], 2 * site[1], 2 * site[2])
    delta = (
        doubled[0] - CENTER_DOUBLED[0],
        doubled[1] - CENTER_DOUBLED[1],
        doubled[2] - CENTER_DOUBLED[2],
    )
    rotated = (
        rotation[0][0] * delta[0] + rotation[0][1] * delta[1] + rotation[0][2] * delta[2],
        rotation[1][0] * delta[0] + rotation[1][1] * delta[1] + rotation[1][2] * delta[2],
        rotation[2][0] * delta[0] + rotation[2][1] * delta[1] + rotation[2][2] * delta[2],
    )
    image_doubled = (
        CENTER_DOUBLED[0] + rotated[0],
        CENTER_DOUBLED[1] + rotated[1],
        CENTER_DOUBLED[2] + rotated[2],
    )
    if any(component % 2 != 0 for component in image_doubled):
        return None
    return (
        image_doubled[0] // 2,
        image_doubled[1] // 2,
        image_doubled[2] // 2,
    )


def two_cube_preserving_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    sites = set(TWO_CUBE)
    kept = []
    for rotation in proper_cube_rotations():
        images = [apply_about_center(rotation, site) for site in TWO_CUBE]
        if all(image in sites for image in images) and len(set(images)) == 12:
            kept.append(rotation)
    return tuple(kept)


def axis_type(
    site: tuple[int, int, int], locked: set[tuple[int, int, int]]
) -> tuple[int, int, int]:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for step in AXES:
        occupied = int(_add(site, step) in locked) + int(_sub(site, step) in locked)
        if occupied == 0:
            n_empty += 1
        elif occupied == 2:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def fires(typ: tuple[int, int, int], bits: tuple[int, int, int, int, int]) -> bool:
    wt1, opp2, adj2, vertex3, mixed3 = bits
    table = {
        (0, 0, 3): 0,
        (0, 3, 0): 0,
        (1, 0, 2): wt1,
        (1, 2, 0): wt1,
        (0, 1, 2): opp2,
        (0, 2, 1): opp2,
        (2, 0, 1): adj2,
        (2, 1, 0): adj2,
        (3, 0, 0): vertex3,
        (1, 1, 1): mixed3,
    }
    return bool(table[typ])


def evolve(
    seed: tuple[tuple[int, int, int], ...], bits: tuple[int, int, int, int, int]
) -> tuple[tuple[int, ...], frozenset[tuple[int, int, int]]]:
    locked = set(seed)
    history = [len(locked)]
    while True:
        ready = [
            site
            for site in TWO_CUBE
            if site not in locked and fires(axis_type(site, locked), bits)
        ]
        if not ready:
            break
        locked.update(ready)
        history.append(len(locked))
        if len(locked) == 12:
            break
    return tuple(history), frozenset(locked)


def filled(seed: tuple[tuple[int, int, int], ...], bits: tuple[int, int, int, int, int]) -> bool:
    return len(evolve(seed, bits)[1]) == 12


def missed_three_site_seeds(
    bits: tuple[int, int, int, int, int],
) -> tuple[frozenset[tuple[int, int, int]], ...]:
    missed = []
    for seed in combinations(TWO_CUBE, 3):
        if not filled(seed, bits):
            missed.append(frozenset(seed))
    return tuple(missed)


def seed_key(seed: frozenset[tuple[int, int, int]]) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted(seed))


def act_seed(
    rotation: tuple[tuple[int, int, int], ...],
    seed: frozenset[tuple[int, int, int]],
) -> frozenset[tuple[int, int, int]]:
    images = []
    for site in seed:
        image = apply_about_center(rotation, site)
        if image is None:
            raise RuntimeError("rotation left the integer lattice")
        images.append(image)
    return frozenset(images)


def orbits_of(
    seeds: tuple[frozenset[tuple[int, int, int]], ...],
    group: tuple[tuple[tuple[int, int, int], ...], ...],
) -> tuple[tuple[frozenset[tuple[int, int, int]], ...], ...]:
    remaining = set(seeds)
    orbits: list[tuple[frozenset[tuple[int, int, int]], ...]] = []
    while remaining:
        start = min(remaining, key=seed_key)
        seen: set[frozenset[tuple[int, int, int]]] = set()
        stack = [start]
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            for rotation in group:
                image = act_seed(rotation, current)
                if image in remaining and image not in seen:
                    stack.append(image)
        remaining -= seen
        orbits.append(tuple(sorted(seen, key=seed_key)))
    return tuple(orbits)


def audit_paths_are_static_literals(source: str) -> bool:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
            continue
        value = node.value
        if not isinstance(value, ast.Tuple):
            return False
        return all(
            isinstance(element, ast.Constant) and isinstance(element.value, str)
            for element in value.elts
        )
    return False


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; two-cube occupancy and cut-map bits only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer lock counts; no floating-point inputs")
    print("claim_boundary: displayed orbit type; f0 is not adopted")

    seeds3 = tuple(combinations(TWO_CUBE, 3))
    checks.check("geometry-two-cube", "the two-cube has 12 sites", len(TWO_CUBE) == 12)
    checks.check(
        "geometry-three-site-count",
        "there are exactly 220 three-site seeds",
        len(seeds3) == 220,
    )

    group = two_cube_preserving_rotations()
    all_rots = proper_cube_rotations()
    checks.check(
        "group-from-proper-cube",
        "G is the two-cube-preserving subset of the 24 proper cube rotations",
        len(all_rots) == 24 and len(group) == 8,
    )
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    checks.check(
        "group-contains-identity",
        "the identity is two-cube-preserving",
        identity in group,
    )

    cov3_f0 = sum(1 for seed in seeds3 if filled(seed, F0_BITS))
    cov3_l1 = sum(1 for seed in seeds3 if filled(seed, L1_BITS))
    cov3_f1 = sum(1 for seed in seeds3 if filled(seed, F1_BITS))
    missed = missed_three_site_seeds(F0_BITS)
    checks.check("thm1-cov3-reconfirm", "cov3(f0) = 212", cov3_f0 == 212)
    checks.check("thm1-miss-count", "|M| = 8", len(missed) == 8)
    checks.check(
        "thm1-complement",
        "220 - cov3(f0) equals |M|",
        220 - cov3_f0 == len(missed),
    )
    checks.check(
        "control-l1-and-f1-fill-all",
        "f_L1 and f1 fill all 220 three-site seeds",
        cov3_l1 == 220 and cov3_f1 == 220,
    )

    orbits = orbits_of(missed, group)
    n_orb = len(orbits)
    representatives = tuple(seed_key(orbit[0]) for orbit in orbits)
    checks.check("thm2-orbit-count", "N_orb = 1", n_orb == 1)
    checks.check(
        "thm2-orbit-size",
        "the single orbit contains all eight missed seeds",
        n_orb == 1 and len(orbits[0]) == 8,
    )
    lex_rep = ((0, 0, 0), (1, 0, 1), (2, 0, 0))
    checks.check(
        "thm2-lex-representative",
        "the lex representative is {(0,0,0),(1,0,1),(2,0,0)}",
        representatives == (lex_rep,),
    )
    history, halt_locks = evolve(lex_rep, F0_BITS)
    checks.check(
        "thm2-rep-unfilled",
        "f0 does not fill the representative (halt history (3, 8, 10))",
        history == (3, 8, 10) and len(halt_locks) == 10,
    )

    print(f"N_orb={n_orb}")
    print(f"lex_representatives={representatives}")

    checks.check(
        "thm3-f0-not-l1",
        "f0 is not f_L1; L1 is n!=0 (some axis unbalanced)",
        F0_BITS != L1_BITS,
    )
    checks.check(
        "thm3-f0-not-hamming",
        "f0 is not Hamming parity of the six neighbor bits",
        F0_BITS != HAMMING_BITS,
    )
    checks.check(
        "mutation-eight-orbits-fails",
        "the leftover 8-row reading N_orb=8 is rejected",
        n_orb != 8,
    )
    checks.check(
        "mutation-rep-is-not-all-of-M",
        "one representative is displayed; M is not republished as eight types",
        n_orb == 1 and len(representatives) == 1,
    )

    forbidden = ("G" + "_N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-substrings",
        "the note omits the dispatch-forbidden phrases",
        all(phrase not in note for phrase in forbidden),
    )
    checks.check(
        "display-not-adopt",
        "the note displays N_orb and refuses adoption of f0",
        "Displayed, not adopted" in note
        and "Do not adopt f0" in note
        and "N_orb = 1" in note
        and "{(0,0,0), (1,0,1), (2,0,0)}" in note,
    )
    checks.check(
        "no-eight-row-claim-table",
        "the claim surface does not publish an 8-row leftover table",
        "one lex representative" in note
        and "|M| leftover table" not in note
        and note.count("(1, 0, 1)") < 4,
    )
    checks.check(
        "live-parent-quotes",
        "Lattice, Admissibility, and Record sentences are quoted without rewrite",
        "proper cubic rotations about each site" in axiom
        and "proper cubic rotations about each site" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "one fixed nearest-neighbor admissibility rule" in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and no axiom adoption are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status:" in note
        and "no axiom or approved primitive is added" in note
        and "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_F0_THREE_SITE_MISS_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals(self_source)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "scope-not-nogo",
        "the note is a bounded display, not a no-go",
        "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and "These are scope boundaries, not impossibility" in note
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: each missed 3-site seed is tested by the lock evolution of f0")
    print("per_site: occupancy is the two-cube with off-patch o=0; no other patch is used")
    print("per_mode: G is the two-cube-preserving subset of the 24 proper cube rotations")
    print("per_block: N_orb and one lex representative are the displayed claim")
    print("lattice_wide: checked and not executed — no Z^3-wide selector or adoption")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
