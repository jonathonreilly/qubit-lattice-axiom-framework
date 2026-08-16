#!/usr/bin/env python3
"""Weight-4 occupancy 3-ball realization on Stab-ok masks.

Rebuild the 15 weight-4 occupancy-mask census (same pair and G+ as
maskstab). N_ok_masks is the number of masks with N_stab_ok>0. If that
count is zero, set N_real=0 and stop. Otherwise count how many ok-masks
appear as 6-NN occupancy of an unread site on a 3-ball union. Displayed,
not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/WEIGHT4_OCCUPANCY_THREE_BALL_REALIZATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/WEIGHT4_OCCUPANCY_THREE_BALL_REALIZATION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
CENTER_BOX = tuple(
    itertools.product(range(-2, 3), repeat=3)
)
UNREAD_BOX = tuple(
    itertools.product(range(-3, 4), repeat=3)
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "Among weight-4 occupancies that admit a Stab-invariant '
    "July-3 pair member, whether a 3-ball union realizes one at an unread "
    'site is reported. Displayed, not adopted."'
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def ball(center: Point, radius: int = 2) -> frozenset[Point]:
    sites: set[Point] = set()
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if l1(offset) <= radius:
            sites.add(add(center, offset))
    return frozenset(sites)


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


def july3_pair(perms: list[tuple[int, ...]]) -> tuple[set[Coloring], int, int]:
    orbits = direct_orbits(perms)
    orbit_id = {
        coloring: index for index, orbit in enumerate(orbits) for coloring in orbit
    }
    inversion: Matrix = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    p_perm = direction_perm(inversion)
    chiral_ids: set[int] = set()
    for coloring in all_colorings():
        if orbit_id[act_col(p_perm, coloring)] != orbit_id[coloring]:
            chiral_ids.add(orbit_id[coloring])
    pair = set().union(*(orbits[index] for index in sorted(chiral_ids)))
    return pair, len(orbits), len(chiral_ids)


def weight4_masks() -> tuple[Coloring, ...]:
    return tuple(
        mask
        for mask in itertools.product((0, 1), repeat=len(DIRS))
        if sum(mask) == 4
    )


def mask_census(
    perms: list[tuple[int, ...]], pair: set[Coloring]
) -> list[tuple[Coloring, int, int, int]]:
    rows: list[tuple[Coloring, int, int, int]] = []
    for sigma in weight4_masks():
        stab = [perm for perm in perms if act_col(perm, sigma) == sigma]
        support_members = [
            coloring for coloring in pair if support(coloring) == sigma
        ]
        stab_ok = [
            coloring
            for coloring in support_members
            if all(act_col(perm, coloring) == coloring for perm in stab)
        ]
        rows.append((sigma, len(stab), len(support_members), len(stab_ok)))
    return rows


def realize_ok_masks(
    ok_masks: tuple[Coloring, ...],
) -> tuple[int, tuple[tuple[Point, Point, Point], Point, Coloring] | None]:
    """Lex-first (centers, v, σ) per ok-mask; stop after the first hit each."""
    if not ok_masks:
        return 0, None
    remaining = set(ok_masks)
    first: tuple[tuple[Point, Point, Point], Point, Coloring] | None = None
    balls = {center: ball(center) for center in CENTER_BOX}
    for centers in itertools.combinations(CENTER_BOX, 3):
        occupied = balls[centers[0]] | balls[centers[1]] | balls[centers[2]]
        for site in UNREAD_BOX:
            if site in occupied:
                continue
            sigma = occupancy_tuple(site, occupied)
            if sigma not in remaining:
                continue
            remaining.remove(sigma)
            if first is None:
                first = (centers, site, sigma)
            if not remaining:
                return len(ok_masks), first
    return len(ok_masks) - len(remaining), first


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

    rotations = proper_rotations()
    perms = [direction_perm(matrix) for matrix in rotations]
    pair, n_orbits, n_chiral = july3_pair(perms)
    rows = mask_census(perms, pair)
    ok_masks = tuple(sigma for sigma, _stab, _supp, n_ok in rows if n_ok > 0)
    n_ok_masks = len(ok_masks)
    search_ran = n_ok_masks > 0
    if n_ok_masks == 0:
        n_real = 0
        first = None
    else:
        n_real, first = realize_ok_masks(ok_masks)

    print("weight-4 occupancy 3-ball realization")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"N_pair={len(pair)}")
    print(f"N_orbits={n_orbits}")
    print(f"N_chiral_orbits={n_chiral}")
    print(f"N_weight4={len(rows)}")
    print("census_rows: sigma |Stab| N_pair_support N_stab_ok")
    for sigma, n_stab, n_support, n_ok in rows:
        print(f"  {sigma} {n_stab} {n_support} {n_ok}")
    print(f"N_ok_masks={n_ok_masks}")
    print(f"search_ran={search_ran}")
    print(f"N_real={n_real}")
    print(f"lex_first_realizing={first}")

    expected_paths = (
        "docs/WEIGHT4_OCCUPANCY_THREE_BALL_REALIZATION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

    type_a = [row for row in rows if row[1] == 8]
    type_b = [row for row in rows if row[1] == 2]
    checks.check(
        "g-plus-order",
        len(rotations) == 24
        and len(set(rotations)) == 24
        and all(det3(matrix) == 1 for matrix in rotations)
        and len(pair) == 48
        and n_orbits == 57
        and n_chiral == 2,
        f"proper={len(rotations)} pair={len(pair)}",
    )
    checks.check(
        "weight4-mask-count",
        len(rows) == 15
        and rows[0][0] == (0, 0, 1, 1, 1, 1)
        and rows[-1][0] == (1, 1, 1, 1, 0, 0)
        and all(sum(row[0]) == 4 for row in rows)
        and "15 weight-4" in note_flat,
        f"N_weight4={len(rows)}",
    )
    checks.check(
        "theorem-1-n-ok-masks",
        n_ok_masks == 0
        and all(row[3] == 0 for row in rows)
        and len(type_a) == 3
        and all(row[2] == 0 and row[3] == 0 for row in type_a)
        and len(type_b) == 12
        and all(row[2] == 4 and row[3] == 0 for row in type_b)
        and "N_ok_masks = 0" in note
        and "no lex-first ok-mask" in note_flat,
        f"N_ok_masks={n_ok_masks}",
    )
    checks.check(
        "theorem-1-stop-search",
        n_ok_masks == 0
        and search_ran is False
        and n_real == 0
        and first is None
        and "stop the search" in note_flat
        and "set `N_real = 0`" in note,
    )
    checks.check(
        "theorem-2-n-real",
        n_real == 0
        and first is None
        and "N_real = 0" in note
        and "no lex-first realizing" in note_flat,
        f"N_real={n_real}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a realizing U into Admissibility" in note
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
        "not leftover of staborb/orbfire (one mask)" in note_flat
        and "not leftover of 3ball (tied-n geometry only)" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_ok_masks" not in axiom
        and "N_real" not in axiom
        and "realizing U" not in axiom
        and "weight-4 occupancy" not in axiom,
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

    print("per_element: N_ok_masks and N_real are exact integers")
    print("per_site: 3-ball unions and unread stars only")
    print("per_mode: no spectral calculation")
    print("per_block: weight-4 6-NN occupancy masks and 3-ball stars")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
