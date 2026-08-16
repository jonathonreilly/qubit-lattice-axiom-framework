#!/usr/bin/env python3
"""Orbit type of distinct ambiguous n at the four N_uneq unread 4-NN sites.

U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1)). At each of the four #6654
unequal-n unread 4-occupied-NN sites, the distinct ambiguous kernels
n = d/3 are scored for G+ equivalence. Reports N_same_orb and N_split.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_UNEQ_SITES_KERNEL_ORBIT_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_UNEQ_SITES_KERNEL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BOX = 6
RADIUS = 2
SEEDS: tuple[tuple[int, int, int], ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
NEIGHBORS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_NAME = {
    (1, 0, 0): "+x",
    (-1, 0, 0): "-x",
    (0, 1, 0): "+y",
    (0, -1, 0): "-y",
    (0, 0, 1): "+z",
    (0, 0, -1): "-z",
}

Vector = tuple[Fraction, Fraction, Fraction]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
Site = tuple[int, int, int]


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Site, right: Site) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Site, radius: int = RADIUS) -> frozenset[Site]:
    lo = [axis - radius for axis in center]
    hi = [axis + radius for axis in center]
    return frozenset(
        (x, y, z)
        for x, y, z in product(
            range(lo[0], hi[0] + 1),
            range(lo[1], hi[1] + 1),
            range(lo[2], hi[2] + 1),
        )
        if l1((x, y, z), center) <= radius
    )


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


G_PLUS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Vector) -> Vector:
    permutation, signs = rotation
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def occupancy_kernel(site: Site, occupied: frozenset[Site]) -> Vector:
    components: list[Fraction] = []
    for axis in range(3):
        step = [0, 0, 0]
        step[axis] = 1
        plus = add(site, (step[0], step[1], step[2]))
        minus = add(site, (-step[0], -step[1], -step[2]))
        dipole = int(plus in occupied) - int(minus in occupied)
        components.append(Fraction(dipole, 3))
    return (components[0], components[1], components[2])


def support_size(kernel: Vector) -> int:
    return sum(component != 0 for component in kernel)


def format_kernel(kernel: Vector) -> str:
    return "(" + ", ".join(str(component) for component in kernel) + ")"


def format_map(rotation: Rotation) -> str:
    permutation, signs = rotation
    images = [""] * 3
    names = ("x", "y", "z")
    for source_axis, name in enumerate(names):
        signed = name if signs[source_axis] == 1 else f"−{name}"
        images[permutation[source_axis]] = signed
    return f"(x, y, z) ↦ ({images[0]}, {images[1]}, {images[2]})"


def same_orbit(left: Vector, right: Vector) -> bool:
    return any(rotate_vector(rotation, left) == right for rotation in G_PLUS)


def first_connector(left: Vector, right: Vector) -> Rotation:
    for rotation in G_PLUS:
        if rotate_vector(rotation, left) == right:
            return rotation
    raise AssertionError(f"no G+ element sends {left} to {right}")


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def uneq_rows(occupied: frozenset[Site]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for site in product(range(-BOX, BOX + 1), repeat=3):
        if site in occupied:
            continue
        occupied_slots = tuple(slot for slot in NEIGHBORS if add(site, slot) in occupied)
        if len(occupied_slots) != 4:
            continue
        kernels = {
            slot: occupancy_kernel(add(site, slot), occupied) for slot in occupied_slots
        }
        ambiguous = tuple(
            (slot, kernels[slot])
            for slot in occupied_slots
            if support_size(kernels[slot]) != 1
        )
        distinct_list: list[Vector] = []
        for _, kernel in ambiguous:
            if kernel not in distinct_list:
                distinct_list.append(kernel)
        distinct = tuple(distinct_list)
        unequal = len(distinct) >= 2
        if not unequal:
            continue
        orbit_tied = all(
            same_orbit(left, right) for left in distinct for right in distinct
        )
        connector = None
        if len(distinct) == 2 and orbit_tied:
            connector = first_connector(distinct[0], distinct[1])
        occupied_all_distinct = tuple(sorted(set(kernels.values())))
        mixed_support_split = not all(
            same_orbit(left, right)
            for left in occupied_all_distinct
            for right in occupied_all_distinct
        )
        rows.append(
            {
                "site": site,
                "occupied_slots": occupied_slots,
                "kernels": kernels,
                "ambiguous": ambiguous,
                "distinct": distinct,
                "orbit_tied": orbit_tied,
                "connector": connector,
                "mixed_support_split": mixed_support_split,
            }
        )
    rows.sort(key=lambda row: row["site"])
    return rows


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms Lattice covariance clause")
    print("declared_math: U occupancy; n = d/3; finite G+ acting on kernels")

    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS
        == (
            "docs/SKEW_THREE_SEED_UNEQ_SITES_KERNEL_ORBIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )
    checks.check(
        "g-plus-order",
        len(G_PLUS) == 24 and len(set(G_PLUS)) == 24,
        "finite G+ is exactly the 24 proper cube rotations",
    )

    balls = tuple(ball(seed) for seed in SEEDS)
    occupied = frozenset().union(*balls)
    pairwise = (
        len(balls[0] & balls[1]),
        len(balls[0] & balls[2]),
        len(balls[1] & balls[2]),
    )
    triple = len(balls[0] & balls[1] & balls[2])
    print(f"U_size: {len(occupied)}")
    print(f"ball_sizes: {[len(item) for item in balls]}")
    print(f"pairwise_overlaps: {list(pairwise)}")
    print(f"triple_overlap: {triple}")
    checks.check(
        "u-geometry",
        all(len(item) == 25 for item in balls)
        and pairwise == (7, 4, 4)
        and triple == 2
        and len(occupied) == 62
        and all(max(abs(axis) for axis in site) <= BOX for site in occupied),
        "U is the union of three radius-2 ℓ¹ balls and lies inside the box",
    )

    rows = uneq_rows(occupied)
    n_uneq = len(rows)
    n_same_orb = sum(1 for row in rows if row["orbit_tied"])
    n_split = sum(1 for row in rows if not row["orbit_tied"])
    print(f"N_uneq: {n_uneq}")
    print(f"N_same_orb: {n_same_orb}")
    print(f"N_split: {n_split}")
    for row in rows:
        distinct = ", ".join(format_kernel(kernel) for kernel in row["distinct"])
        connector = row["connector"]
        connector_text = format_map(connector) if connector is not None else "none"
        print(
            f"site {row['site']} same_orb={row['orbit_tied']} "
            f"distinct=[{distinct}] g={connector_text}"
        )

    expected_sites = ((-1, 1, 1), (0, 1, 2), (2, 1, 2), (3, 1, 1))
    expected_distinct = (
        (
            (Fraction(1, 3), Fraction(0), Fraction(-1, 3)),
            (Fraction(1, 3), Fraction(-1, 3), Fraction(0)),
        ),
        (
            (Fraction(0), Fraction(1, 3), Fraction(-1, 3)),
            (Fraction(1, 3), Fraction(0), Fraction(-1, 3)),
        ),
        (
            (Fraction(0), Fraction(1, 3), Fraction(-1, 3)),
            (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
        ),
        (
            (Fraction(-1, 3), Fraction(0), Fraction(-1, 3)),
            (Fraction(-1, 3), Fraction(-1, 3), Fraction(0)),
        ),
    )
    expected_maps = (
        "(x, y, z) ↦ (x, z, −y)",
        "(x, y, z) ↦ (y, −x, z)",
        "(x, y, z) ↦ (−y, x, z)",
        "(x, y, z) ↦ (x, z, −y)",
    )
    checks.check(
        "theorem-1-uneq-sites",
        n_uneq == 4
        and tuple(row["site"] for row in rows) == expected_sites
        and tuple(row["distinct"] for row in rows) == expected_distinct
        and "(−1, 1, 1)" in note
        and "(0, 1, 2)" in note
        and "(2, 1, 2)" in note
        and "(3, 1, 1)" in note,
        "the four unequal-n unread 4-NN sites and distinct n match the note",
    )
    checks.check(
        "theorem-1-n-same-orb",
        n_same_orb == 4
        and all(row["orbit_tied"] for row in rows)
        and all(len(row["distinct"]) == 2 for row in rows)
        and f"N_same_orb = {n_same_orb}" in note,
        f"every unequal-n site has G+-equivalent kernels; N_same_orb = {n_same_orb}",
    )
    checks.check(
        "theorem-1-n-split",
        n_split == 0 and "N_split = 0" in note,
        "no unequal-n site has kernels in different G+ orbits; N_split = 0",
    )

    two_support = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for signs in product((-1, 1), repeat=2):
            vector = [Fraction(0), Fraction(0), Fraction(0)]
            vector[i] = Fraction(signs[0], 3)
            vector[j] = Fraction(signs[1], 3)
            two_support.append(tuple(vector))
    seed_kernel = two_support[0]
    full_orbit = {rotate_vector(rotation, seed_kernel) for rotation in G_PLUS}
    displayed_maps = [format_map(row["connector"]) for row in rows]
    checks.check(
        "theorem-1-explicit-rotations",
        set(two_support) == full_orbit
        and len(full_orbit) == 12
        and displayed_maps == list(expected_maps)
        and all(item in note for item in expected_maps)
        and "orbit of size 12" in note,
        "each displayed connecting rotation is a proper cube rotation",
    )
    checks.check(
        "theorem-2-orbit-tied",
        n_split == 0
        and "N_split = 0" in note
        and "orbit-tied kernels" in note
        and "constant on those kernels" in note,
        "N_split = 0 so any G+-equivariant f(n) is constant on those kernels",
    )
    checks.check(
        "unique-axis-filter-load-bearing",
        all(row["mixed_support_split"] for row in rows)
        and "|supp n| ≠ 1" in note,
        "including unique-axis n would mix 1-support and 2-support orbits",
    )
    checks.check(
        "lattice-clause",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site" in axiom_flat
        and "proper cubic rotations about each site" in note_flat,
        "the current Lattice wording supplies finite proper cubic rotations",
    )
    checks.check(
        "admissibility-unedited",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat
        and "Do not write orbits into Admissibility" in note
        and "B_2((1,2,1))" not in axiom
        and "off-axis" not in axiom.lower(),
        "orbits are displayed and are not written into Admissibility",
    )
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not attach L1" in note
        and "not leftover-char of skeweq" in note_flat
        and "No 4th ball" in note
        and "finite G+ = 24 only" in note_flat.replace("`", "")
        and "No new patch family" in note,
        "the note reports the orbit census without adopting it, attaching L1, or cloning a 4th ball",
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    script_body = self_source.split("forbidden = ", 1)[0]
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in forbidden)
        and all(phrase not in script_body for phrase in forbidden),
        "the forbidden rhetoric strings are absent from the note and runner",
    )
    checks.check(
        "claim-scope",
        'claim_scope: "On the off-axis three-ball union, whether the distinct ambiguous occupancy kernels at each of the four unequal-n unread 4-NN sites lie in one G+ orbit is reported. Displayed, not adopted."'
        in note
        and "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status: no edit" in note,
        "claim_scope and machine status match the displayed-not-adopted residual",
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "no axiom edit" in note_flat.lower()
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS,
        "the only axiom authority is the current memo; no cache or axiom rewrite",
    )
    checks.check(
        "not-leftover-skeweq",
        "not leftover-char of skeweq" in note_flat
        and "one site" in note_flat
        and "four" in note_flat,
        "the residual is the four-site orbit census, not leftover-char of skeweq",
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
