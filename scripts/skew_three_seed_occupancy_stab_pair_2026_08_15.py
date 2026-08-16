#!/usr/bin/env python3
"""Occupancy stabilizer vs July-3 pair members on one unread star.

U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1)). Score only the unread star at
v = (−1, 1, 1). Occupancy σ is the 6-bit NN occupancy of U at v. G+ acts
on slots. Count |Stab(σ)|, N_pair_support, and N_stab_ok. Displayed, not
adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_OCCUPANCY_STAB_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_OCCUPANCY_STAB_PAIR_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER = {EMPTY: "0", PLUS: "+", MINUS: "−"}
V: Point = (-1, 1, 1)
SEEDS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
IDENTITY: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SWAPPER: Matrix = ((0, 0, -1), (0, -1, 0), (-1, 0, 0))
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(center: Point, radius: int = 2) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if l1(offset) <= radius:
            sites.add(add(center, offset))
    return frozenset(sites)


def locked_union(seeds: tuple[Point, ...] = SEEDS) -> frozenset[Point]:
    occupied: frozenset[Point] = frozenset()
    for seed in seeds:
        occupied = occupied | ball(seed)
    return occupied


def occupancy_tuple(site: Point, occupied: frozenset[Point]) -> Coloring:
    return tuple(int(add(site, direction) in occupied) for direction in DIRS)


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != 0) for letter in coloring)


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring) -> Coloring:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def proper_rotations() -> tuple[Matrix, ...]:
    records: list[Matrix] = []
    seen: set[Matrix] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row, col in enumerate(perm):
                entry = [0, 0, 0]
                entry[col] = signs[row]
                rows.append(tuple(entry))
            matrix = (rows[0], rows[1], rows[2])
            if matrix not in seen and det3(matrix) == 1:
                seen.add(matrix)
                records.append(matrix)
    return tuple(records)


def all_colorings(letters: int = 3) -> list[Coloring]:
    return list(itertools.product(range(letters), repeat=len(DIRS)))


def direct_orbits(perms: list[tuple[int, ...]]) -> list[set[Coloring]]:
    unseen = set(all_colorings())
    orbits: list[set[Coloring]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def fully_mixed(coloring: Coloring) -> bool:
    axis_bicolored = all(
        coloring[2 * axis] != coloring[2 * axis + 1] for axis in range(3)
    )
    counts = sorted(coloring.count(letter) for letter in range(3))
    return axis_bicolored and counts == [2, 2, 2]


def format_letters(coloring: Coloring) -> str:
    return "(" + ",".join(LETTER[letter] for letter in coloring) + ")"


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f" | {detail}" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


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

    occupied = locked_union()
    sigma = occupancy_tuple(V, occupied)
    rotations = proper_rotations()
    perms = [direction_perm(matrix) for matrix in rotations]
    stab_mats = tuple(
        matrix
        for matrix in rotations
        if act_col(direction_perm(matrix), sigma) == sigma
    )
    stab_perms = [direction_perm(matrix) for matrix in stab_mats]
    inversion: Matrix = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    p_perm = direction_perm(inversion)
    orbits = direct_orbits(perms)
    orbit_id = {
        coloring: index for index, orbit in enumerate(orbits) for coloring in orbit
    }
    chiral_ids: set[int] = set()
    for coloring in all_colorings():
        if orbit_id[act_col(p_perm, coloring)] != orbit_id[coloring]:
            chiral_ids.add(orbit_id[coloring])
    pair = set().union(*(orbits[index] for index in sorted(chiral_ids)))
    support_members = tuple(
        sorted(coloring for coloring in pair if support(coloring) == sigma)
    )
    stab_ok = tuple(
        coloring
        for coloring in support_members
        if all(act_col(perm, coloring) == coloring for perm in stab_perms)
    )
    n_stab = len(stab_mats)
    n_pair_support = len(support_members)
    n_stab_ok = len(stab_ok)
    sigma_orbit = {act_col(perm, sigma) for perm in perms}

    print("occupancy stabilizer vs July-3 pair members")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"U_card={len(occupied)}")
    print(f"v_in_U={V in occupied}")
    print(f"sigma={sigma}")
    print(f"G_plus={len(rotations)}")
    print(f"stab_order={n_stab}")
    print("stab_generating_list=" + ",".join(str(matrix) for matrix in stab_mats))
    print(f"N_pair={len(pair)}")
    print(f"N_pair_support={n_pair_support}")
    print("support_members=" + ",".join(str(item) for item in support_members))
    print("support_members_letters=" + ",".join(format_letters(item) for item in support_members))
    print(f"N_stab_ok={n_stab_ok}")
    print(f"sigma_orbit_size={len(sigma_orbit)}")

    expected_paths = (
        "docs/SKEW_THREE_SEED_OCCUPANCY_STAB_PAIR_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS == expected_paths
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    covariance_clause = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    unread_sentence = "A site with no record cannot be read."
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-lattice",
        lattice_sentence in axiom_flat and lattice_sentence in note_flat,
    )
    checks.check(
        "source-admissibility",
        covariance_clause in axiom_flat
        and admissibility_sentence in axiom_flat
        and covariance_clause in note_flat
        and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-unread-qubit",
        unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )

    balls = tuple(ball(seed) for seed in SEEDS)
    pairwise = (
        len(balls[0] & balls[1]),
        len(balls[0] & balls[2]),
        len(balls[1] & balls[2]),
    )
    triple = len(balls[0] & balls[1] & balls[2])
    checks.check(
        "g-plus-order",
        len(rotations) == 24 and len(set(rotations)) == 24 and det3(SWAPPER) == 1,
        f"proper={len(rotations)}",
    )
    checks.check(
        "center-unread",
        V not in occupied
        and l1(V) == 3
        and l1(sub(V, (2, 0, 0))) == 5
        and l1(sub(V, (1, 2, 1))) == 3,
    )
    checks.check(
        "u-geometry",
        all(len(item) == 25 for item in balls)
        and pairwise == (7, 4, 4)
        and triple == 2
        and len(occupied) == 62,
    )
    checks.check(
        "occupancy-sigma",
        sigma == (1, 0, 1, 1, 0, 1)
        and "(1, 0, 1, 1, 0, 1)" in note,
        f"sigma={sigma}",
    )
    checks.check(
        "theorem-1-stab",
        n_stab == 2
        and IDENTITY in stab_mats
        and SWAPPER in stab_mats
        and set(stab_mats) == {IDENTITY, SWAPPER}
        and "|Stab(σ)| = 2" in note
        and "s : (x, y, z) ↦ (−z, −y, −x)" in note
        and len(sigma_orbit) == 12,
        f"stab={n_stab} orbit={len(sigma_orbit)}",
    )
    checks.check(
        "theorem-1-pair-support",
        len(pair) == 48
        and len(chiral_ids) == 2
        and len(orbits) == 57
        and n_pair_support == 4
        and support_members
        == (
            (1, 0, 1, 2, 0, 2),
            (1, 0, 2, 1, 0, 2),
            (2, 0, 1, 2, 0, 1),
            (2, 0, 2, 1, 0, 1),
        )
        and all(fully_mixed(item) for item in support_members)
        and "N_pair_support = 4" in note,
        f"N_pair={len(pair)} N_pair_support={n_pair_support}",
    )
    implication_ok = n_stab != 1 or n_stab_ok == n_pair_support
    checks.check(
        "theorem-2-stab-ok",
        n_stab_ok == 0
        and implication_ok
        and n_stab == 2
        and "N_stab_ok = 0" in note
        and "if `|Stab(σ)| = 1` then" in note
        and "`N_stab_ok = N_pair_support`" in note
        and "equivariant local extensions" in note,
        f"N_stab_ok={n_stab_ok}",
    )
    swap_perm = direction_perm(SWAPPER)
    checks.check(
        "swapper-forces-y-bicolor-obstruction",
        swap_perm[2] == 3
        and swap_perm[3] == 2
        and swap_perm[0] == 5
        and all(item[2] != item[3] for item in support_members)
        and all(act_col(swap_perm, item) != item for item in support_members),
    )

    claim_scope = (
        'claim_scope: "On the off-axis three-ball star at v=(-1,1,1), '
        "the occupancy stabilizer and the count of Stab-invariant July-3 "
        'pair members with that support are reported. Displayed, not adopted."'
    )
    checks.check("claim-scope", claim_scope in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write any such `c` into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "Do not add a 4th ball" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-prior",
        "not leftover of deleq" in note_flat
        and "one named product" in note_flat
        and "not leftover of nstab" in note_flat
        and "two-ball tied" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "Stab(σ)" not in axiom
        and "N_stab_ok" not in axiom
        and "B_2((1,2,1))" not in axiom
        and "(+,0,+,−,0,−)" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(
            phrase not in self_source.split("FORBIDDEN = ", 1)[0]
            for phrase in FORBIDDEN
        ),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: |Stab|, N_pair_support, N_stab_ok are exact integers")
    print("per_site: only the unread star center v is scored")
    print("per_mode: no spectral calculation")
    print("per_block: the six-neighbor star at v only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
