#!/usr/bin/env python3
"""Occupied-slot census of the July-3 unique k=3 chiral pair.

Letters {0,1,2} with 0 empty/unread. Occupied count is the number of
nonzero slots on each 6-tuple in the two chiral G+ orbits.
"""

from __future__ import annotations

import itertools
from collections import Counter
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/JULY3_K3_PAIR_OCCUPIED_SLOT_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
JULY3_PATH = ROOT / (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_"
    "OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_"
    "BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/JULY3_K3_PAIR_OCCUPIED_SLOT_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
OCC_FRONT_MAX = 3
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def det3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply_mat(matrix: list[list[int]], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3)
    )


def direction_perm(matrix: list[list[int]]) -> tuple[int, ...]:
    return tuple(DIR_INDEX[apply_mat(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def signed_permutation_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    seen: set[tuple[int, ...]] = set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, col in enumerate(perm):
                matrix[row][col] = signs[row]
            key = tuple(entry for row in matrix for entry in row)
            if key not in seen:
                seen.add(key)
                records.append(
                    {
                        "matrix": matrix,
                        "det": det3(matrix),
                        "perm": direction_perm(matrix),
                    }
                )
    return records


def all_colorings(letters: int) -> list[tuple[int, ...]]:
    return list(itertools.product(range(letters), repeat=len(DIRS)))


def direct_orbits(
    perms: list[tuple[int, ...]], letters: int
) -> list[set[tuple[int, ...]]]:
    unseen = set(all_colorings(letters))
    orbits: list[set[tuple[int, ...]]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def occupied_count(coloring: tuple[int, ...]) -> int:
    return sum(1 for letter in coloring if letter != 0)


def fully_mixed(coloring: tuple[int, ...]) -> bool:
    axis_bicolored = all(coloring[2 * axis] != coloring[2 * axis + 1] for axis in range(3))
    counts = sorted(coloring.count(letter) for letter in range(3))
    return axis_bicolored and counts == [2, 2, 2]


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
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    july3 = JULY3_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_july3 = normalize(july3)

    records = signed_permutation_records()
    proper_perms = [record["perm"] for record in records if record["det"] == 1]
    inversion = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    p_perm = direction_perm(inversion)
    proper_orbits = direct_orbits(proper_perms, 3)
    orbit_id = {
        coloring: index
        for index, orbit in enumerate(proper_orbits)
        for coloring in orbit
    }

    chiral_ids: set[int] = set()
    for coloring in all_colorings(3):
        image = act_col(p_perm, coloring)
        if orbit_id[image] != orbit_id[coloring]:
            chiral_ids.add(orbit_id[coloring])
    chiral_ids_sorted = sorted(chiral_ids)
    pair = set().union(*(proper_orbits[index] for index in chiral_ids_sorted))
    occupied = [occupied_count(coloring) for coloring in pair]
    histogram = dict(sorted(Counter(occupied).items()))
    occupied_min = min(occupied)
    occupied_max = max(occupied)
    n_pair = len(pair)
    lex_reps = tuple(min(proper_orbits[index]) for index in chiral_ids_sorted)
    orbit_sizes = [len(proper_orbits[index]) for index in chiral_ids_sorted]
    min_ge_4 = occupied_min >= 4
    front_can_match = occupied_min <= OCC_FRONT_MAX

    print("July-3 k=3 chiral-pair occupied-slot census")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"N_pair: {n_pair}")
    print(f"orbit_sizes: {orbit_sizes}")
    print(f"lex_reps: {lex_reps}")
    print(f"occupied_min: {occupied_min}")
    print(f"occupied_max: {occupied_max}")
    print(f"occupied_histogram: {histogram}")
    print(f"occ_front_max: {OCC_FRONT_MAX}")
    print(f"min_occupied_ge_4: {min_ge_4}")
    print(f"front_site_can_match_pair_member: {front_can_match}")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "audit-input-paths-static-literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/JULY3_K3_PAIR_OCCUPIED_SLOT_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    unread_sentence = "A site with no record cannot be read."
    checks.check(
        "source-lattice",
        lattice_sentence in normalized_axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        admissibility_sentence in normalized_axiom
        and admissibility_sentence in note,
    )
    checks.check(
        "source-unread",
        unread_sentence in normalized_axiom and unread_sentence in note,
    )
    checks.check(
        "source-july3-unique-pair",
        "exactly one" in normalized_july3
        and "chiral pair" in normalized_july3
        and "handed fully-mixed" in normalized_note
        and "exactly one chiral pair" in normalized_note,
    )

    checks.check(
        "proper-group-order",
        len(records) == 48 and len(proper_perms) == 24 and len(set(proper_perms)) == 24,
        f"full={len(records)} proper={len(proper_perms)}",
    )
    checks.check(
        "unique-chiral-pair",
        len(chiral_ids_sorted) == 2 and len(proper_orbits) == 57,
        f"orbits={len(proper_orbits)} chiral_ids={chiral_ids_sorted}",
    )
    checks.check(
        "n-pair",
        n_pair == 48 and orbit_sizes == [24, 24],
        f"N_pair={n_pair} sizes={orbit_sizes}",
    )
    checks.check(
        "lex-first-representatives",
        lex_reps == ((0, 1, 0, 2, 1, 2), (0, 1, 0, 2, 2, 1)),
        f"lex_reps={lex_reps}",
    )
    checks.check(
        "pair-fully-mixed",
        all(fully_mixed(coloring) for coloring in pair),
    )
    checks.check(
        "occupied-min-max",
        occupied_min == 4 and occupied_max == 4,
        f"min={occupied_min} max={occupied_max}",
    )
    checks.check(
        "occupied-histogram",
        histogram == {4: 48} and sum(histogram.values()) == n_pair,
        f"histogram={histogram}",
    )
    checks.check(
        "min-occupied-ge-4",
        min_ge_4,
        f"min={occupied_min}",
    )
    checks.check(
        "front-cannot-match",
        min_ge_4 and occupied_min > OCC_FRONT_MAX and not front_can_match,
        f"min={occupied_min} front_max={OCC_FRONT_MAX}",
    )

    claim_scope = (
        "Among the July-3 unique k=3 chiral-pair 6-tuples, the occupied-slot "
        "count min/max/histogram, and whether that min exceeds the seed-grown "
        "front’s max occupied NN of 3, is reported. Displayed, not adopted."
    )
    checks.check("claim-scope-pinned", claim_scope in note)
    checks.check(
        "note-census-numbers",
        "N_pair = 48" in note
        and "occupied_min = 4" in note
        and "occupied_max = 4" in note
        and "occupied_histogram = {4: 48}" in note
        and "front_site_can_match_pair_member = false" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "displayed, not adopted" in normalized_note
        and "not written into Admissibility" in normalized_note
        and "written_into_admissibility = false" in note,
    )
    checks.check(
        "not-attached-to-l1",
        "not attached to L1" in normalized_note
        and "attached_to_L1 = false" in note
        and "attach L1" in note,
    )
    checks.check(
        "not-leftover-char-or-need6",
        "not leftover-char of pluschi" in normalized_note
        and "not need6" in normalized_note
        and "front-geometry bound" in normalized_note,
    )
    checks.check(
        "no-forbidden-phrases",
        all(phrase not in note and phrase not in axiom for phrase in FORBIDDEN),
    )
    checks.check(
        "no-axiom-edit",
        "hypothetical_axiom_status: \"no edit\"" in note
        and "does not add a histogram clause" in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
