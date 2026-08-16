#!/usr/bin/env python3
"""Weight-4 occupancy-mask census of Stab vs July-3 pair members.

Score the 15 occupancy bitstrings of weight 4 on the six nearest-neighbor
slots. For each mask σ report |Stab(σ)|, N_pair_support, and N_stab_ok.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/WEIGHT4_OCCUPANCY_STAB_PAIR_CENSUS_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/WEIGHT4_OCCUPANCY_STAB_PAIR_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the 15 weight-4 occupancy masks, the counts |Stab|, '
    "N_pair_support, and N_stab_ok are reported. Displayed, not adopted.\""
)
STABORB_MASK: Coloring = (1, 0, 1, 1, 0, 1)


def normalize(text: str) -> str:
    return " ".join(text.split())


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != EMPTY) for letter in coloring)


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


def weight4_masks() -> tuple[Coloring, ...]:
    return tuple(
        mask
        for mask in itertools.product((0, 1), repeat=len(DIRS))
        if sum(mask) == 4
    )


def direct_orbits(perms: list[tuple[int, ...]]) -> list[set[Coloring]]:
    unseen = set(all_colorings())
    orbits: list[set[Coloring]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def july3_k3_pair(
    perms: list[tuple[int, ...]],
) -> tuple[frozenset[Coloring], list[set[Coloring]], set[int]]:
    orbits = direct_orbits(perms)
    inversion: Matrix = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    p_perm = direction_perm(inversion)
    orbit_id = {
        coloring: index for index, orbit in enumerate(orbits) for coloring in orbit
    }
    chiral_ids: set[int] = set()
    for coloring in all_colorings():
        if orbit_id[act_col(p_perm, coloring)] != orbit_id[coloring]:
            chiral_ids.add(orbit_id[coloring])
    pair = set().union(*(orbits[index] for index in sorted(chiral_ids)))
    return frozenset(pair), orbits, chiral_ids


def census_row(
    sigma: Coloring,
    perms: list[tuple[int, ...]],
    pair: frozenset[Coloring],
) -> tuple[Coloring, int, int, int]:
    stab_perms = [perm for perm in perms if act_col(perm, sigma) == sigma]
    support_members = [
        coloring for coloring in pair if support(coloring) == sigma
    ]
    stab_ok = [
        coloring
        for coloring in support_members
        if all(act_col(perm, coloring) == coloring for perm in stab_perms)
    ]
    return sigma, len(stab_perms), len(support_members), len(stab_ok)


def row_line(sigma: Coloring, n_stab: int, n_support: int, n_ok: int) -> str:
    return f"| `{sigma}` | {n_stab} | {n_support} | {n_ok} |"


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
    pair, orbits, chiral_ids = july3_k3_pair(perms)
    masks = weight4_masks()
    rows = [census_row(sigma, perms, pair) for sigma in masks]
    ok_masks = [sigma for sigma, _n_stab, _n_support, n_ok in rows if n_ok > 0]
    n_ok_masks = len(ok_masks)
    lex_first = ok_masks[0] if ok_masks else None
    n_pair_support_sum = sum(n_support for _sigma, _n_stab, n_support, _n_ok in rows)
    opposite_empty = [
        (sigma, n_stab, n_support, n_ok)
        for sigma, n_stab, n_support, n_ok in rows
        if any(sigma[2 * axis] == 0 and sigma[2 * axis + 1] == 0 for axis in range(3))
    ]
    perpendicular_empty = [
        row for row in rows if row not in opposite_empty
    ]
    staborb_row = next(row for row in rows if row[0] == STABORB_MASK)

    print("weight-4 occupancy stabilizer vs July-3 pair members")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"N_pair={len(pair)}")
    print(f"N_masks={len(masks)}")
    print("sigma |Stab| N_pair_support N_stab_ok")
    for sigma, n_stab, n_support, n_ok in rows:
        print(f"{sigma} {n_stab} {n_support} {n_ok}")
    print(f"N_ok_masks={n_ok_masks}")
    print(f"lex_first={lex_first}")
    print(f"N_pair_support_sum={n_pair_support_sum}")

    expected_paths = (
        "docs/WEIGHT4_OCCUPANCY_STAB_PAIR_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    checks.check(
        "g-plus-order",
        len(rotations) == 24
        and len(set(rotations)) == 24
        and all(det3(matrix) == 1 for matrix in rotations),
        f"proper={len(rotations)}",
    )
    checks.check(
        "weight-4-mask-count",
        len(masks) == 15
        and len(set(masks)) == 15
        and all(sum(mask) == 4 for mask in masks)
        and masks[0] == (0, 0, 1, 1, 1, 1)
        and masks[-1] == (1, 1, 1, 1, 0, 0)
        and "15" in note
        and "weight-4" in note,
        f"N_masks={len(masks)}",
    )
    table_in_note = all(
        row_line(sigma, n_stab, n_support, n_ok) in note
        for sigma, n_stab, n_support, n_ok in rows
    )
    checks.check(
        "theorem-1-table",
        len(rows) == 15
        and table_in_note
        and len(pair) == 48
        and len(chiral_ids) == 2
        and len(orbits) == 57
        and n_pair_support_sum == 48
        and f"N_ok_masks = {n_ok_masks}" in note
        and (
            (lex_first is None and "no lex-first" in note_flat)
            or (lex_first is not None and str(lex_first) in note)
        )
        and staborb_row == (STABORB_MASK, 2, 4, 0)
        and len(opposite_empty) == 3
        and all(row[1] == 8 and row[2] == 0 and row[3] == 0 for row in opposite_empty)
        and len(perpendicular_empty) == 12
        and all(
            row[1] == 2 and row[2] == 4 and row[3] == 0
            for row in perpendicular_empty
        ),
        f"N_ok_masks={n_ok_masks}",
    )
    theorem_2_zero = (
        n_ok_masks == 0
        and "N_ok_masks = 0" in note
        and "no occupancy of pair-support type admits a stab-invariant pair member"
        in note_flat.lower()
        and "no nn-determined g+-equivariant pair labeling exists on any 4-occupied 6-star"
        in note_flat.lower()
    )
    theorem_2_positive = (
        n_ok_masks > 0
        and f"N_ok_masks = {n_ok_masks}" in note
        and lex_first is not None
        and str(lex_first) in note
    )
    checks.check(
        "theorem-2-n-ok-masks",
        (theorem_2_zero if n_ok_masks == 0 else theorem_2_positive)
        and all(n_ok == 0 for _sigma, _n_stab, _n_support, n_ok in rows),
        f"N_ok_masks={n_ok_masks}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a mask or pair member into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note
        and "Do not write a mask or pair member into Admissibility" in note_flat,
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
        "not leftover of staborb" in note_flat
        and "one mask" in note_flat
        and "orbfire" in note_flat,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_stab_ok" not in axiom
        and "N_ok_masks" not in axiom
        and "weight-4 occupancy" not in axiom
        and "(1, 0, 1, 1, 0, 1)" not in axiom,
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
    checks.check(
        "masks-only-scope",
        "occupancy masks only" in note_flat
        and "Score occupancy masks only" in note
        and "4-occupied 6-star" in note,
    )

    print("per_element: |Stab|, N_pair_support, N_stab_ok are exact integers")
    print("per_site: occupancy masks only")
    print("per_mode: no spectral calculation")
    print("per_block: the 15 weight-4 6-bit occupancy masks")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
