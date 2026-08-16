#!/usr/bin/env python3
"""Two-ball unread witness occupancy mask versus the July-3 k=3 pair.

Letters {0, +, −} with 0 empty. Occupancy mask of the 6-NN star at
v = (1,-1,-1) for U = B_2(0) ∪ B_2((2,0,0)) is compared to the 48 pair
members; the 16 {+,−} fillings of the four occupied slots are then tested.
"""

from __future__ import annotations

import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/TWO_BALL_WITNESS_CHIRAL_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
JULY3_PATH = ROOT / (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_"
    "OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_"
    "BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/TWO_BALL_WITNESS_CHIRAL_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

EMPTY, PLUS, MINUS = 0, 1, 2
LETTERS = (EMPTY, PLUS, MINUS)
LETTER_SHOW = {EMPTY: "0", PLUS: "+", MINUS: "-"}
WITNESS = (1, -1, -1)
CENTER_P = (2, 0, 0)
RADIUS = 2
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def normalize(text: str) -> str:
    return " ".join(text.split())


def show_tuple(coloring: tuple[int, ...]) -> str:
    return "(" + ", ".join(LETTER_SHOW[letter] for letter in coloring) + ")"


def add(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(
    left: tuple[int, int, int], right: tuple[int, int, int] = (0, 0, 0)
) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: tuple[int, int, int], radius: int) -> frozenset[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for offset in itertools.product(range(-radius, radius + 1), repeat=3):
        if l1(offset) <= radius:
            sites.append(add(center, offset))
    return frozenset(sites)


def occupancy_mask(coloring: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(0 if letter == EMPTY else 1 for letter in coloring)


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


def all_colorings() -> list[tuple[int, ...]]:
    return list(itertools.product(LETTERS, repeat=len(DIRS)))


def direct_orbits(perms: list[tuple[int, ...]]) -> list[set[tuple[int, ...]]]:
    unseen = set(all_colorings())
    orbits: list[set[tuple[int, ...]]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def fully_mixed(coloring: tuple[int, ...]) -> bool:
    axis_bicolored = all(
        coloring[2 * axis] != coloring[2 * axis + 1] for axis in range(3)
    )
    counts = sorted(coloring.count(letter) for letter in LETTERS)
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

    occupied = ball((0, 0, 0), RADIUS) | ball(CENTER_P, RADIUS)
    neighbor_sites = tuple(add(WITNESS, direction) for direction in DIRS)
    derived_mask = tuple(1 if site in occupied else 0 for site in neighbor_sites)
    occupied_idx = tuple(index for index, bit in enumerate(derived_mask) if bit == 1)
    empty_idx = tuple(index for index, bit in enumerate(derived_mask) if bit == 0)

    records = signed_permutation_records()
    proper_perms = [record["perm"] for record in records if record["det"] == 1]
    inversion = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    p_perm = direction_perm(inversion)
    proper_orbits = direct_orbits(proper_perms)
    orbit_id = {
        coloring: index
        for index, orbit in enumerate(proper_orbits)
        for coloring in orbit
    }

    chiral_ids: set[int] = set()
    for coloring in all_colorings():
        image = act_col(p_perm, coloring)
        if orbit_id[image] != orbit_id[coloring]:
            chiral_ids.add(orbit_id[coloring])
    chiral_ids_sorted = sorted(chiral_ids)
    pair = set().union(*(proper_orbits[index] for index in chiral_ids_sorted))
    n_pair = len(pair)
    orbit_sizes = [len(proper_orbits[index]) for index in chiral_ids_sorted]
    lex_reps = tuple(min(proper_orbits[index]) for index in chiral_ids_sorted)

    mask_members = sorted(
        coloring for coloring in pair if occupancy_mask(coloring) == derived_mask
    )
    n_mask = len(mask_members)

    fillings: list[tuple[int, ...]] = []
    for bits in itertools.product((PLUS, MINUS), repeat=len(occupied_idx)):
        coloring = [EMPTY] * len(DIRS)
        for index, letter in zip(occupied_idx, bits):
            coloring[index] = letter
        fillings.append(tuple(coloring))
    firing = [coloring for coloring in fillings if coloring in pair]
    n_fire = len(firing)
    lex_first = min(firing) if firing else None

    print("Two-ball witness occupancy mask versus July-3 k=3 pair")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"derived_mask: {derived_mask}")
    print(f"occupied_neighbors: {tuple(neighbor_sites[i] for i in occupied_idx)}")
    print(f"empty_neighbors: {tuple(neighbor_sites[i] for i in empty_idx)}")
    print(f"N_pair: {n_pair}")
    print(f"orbit_sizes: {orbit_sizes}")
    print(f"lex_reps: {tuple(show_tuple(rep) for rep in lex_reps)}")
    print(f"N_mask: {n_mask}")
    print(f"N_fire: {n_fire}")
    print(f"lex_first_firing: {show_tuple(lex_first) if lex_first else None}")
    print(f"firing: {[show_tuple(item) for item in firing]}")

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
            "docs/TWO_BALL_WITNESS_CHIRAL_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "two-ball-mask-derived",
        derived_mask == (1, 1, 1, 0, 1, 0)
        and l1(WITNESS) == 3
        and l1(WITNESS, CENTER_P) == 3
        and WITNESS not in occupied
        and tuple(neighbor_sites[i] for i in occupied_idx)
        == ((2, -1, -1), (0, -1, -1), (1, 0, -1), (1, -1, 0))
        and tuple(neighbor_sites[i] for i in empty_idx)
        == ((1, -2, -1), (1, -1, -2)),
        f"mask={derived_mask}",
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
        "pair-two-empties",
        all(coloring.count(EMPTY) == 2 for coloring in pair)
        and all(fully_mixed(coloring) for coloring in pair),
    )
    checks.check(
        "n-mask",
        n_mask == 4 and derived_mask == (1, 1, 1, 0, 1, 0),
        f"N_mask={n_mask}",
    )
    checks.check(
        "sixteen-fillings",
        len(fillings) == 16
        and len(set(fillings)) == 16
        and all(occupancy_mask(item) == derived_mask for item in fillings),
        f"n_fillings={len(fillings)}",
    )
    checks.check(
        "n-fire",
        n_mask > 0 and n_fire == 4 and set(firing) == set(mask_members),
        f"N_fire={n_fire}",
    )
    checks.check(
        "lex-first-firing",
        lex_first == (PLUS, MINUS, PLUS, EMPTY, MINUS, EMPTY),
        f"lex_first={show_tuple(lex_first) if lex_first else None}",
    )

    claim_scope = (
        "Whether the two-ball unread witness occupancy mask (1,1,1,0,1,0) "
        "appears among the July-3 k=3 chiral-pair 6-tuples, and whether any "
        "{+,−} labeling of its four occupied slots is a pair member, is "
        "reported. Displayed, not adopted."
    )
    checks.check("claim-scope-pinned", claim_scope in note)
    checks.check(
        "note-report-numbers",
        "N_pair = 48" in note
        and "N_mask = 4" in note
        and "N_fire = 4" in note
        and "mask = (1, 1, 1, 0, 1, 0)" in note
        and "lex_first_firing = (+, -, +, 0, -, 0)" in note
        and "witness_can_host_pair_occupancy = true" in note,
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
        and "Do not attach L1" in note,
    )
    checks.check(
        "not-leftover-char",
        "not leftover-char of the two-ball occupied-NN count" in normalized_note
        and "not leftover-char of the pair occupied-slot census" in normalized_note
        and "6-NN star at" in normalized_note,
    )
    checks.check(
        "no-forbidden-phrases",
        all(phrase not in note and phrase not in axiom for phrase in FORBIDDEN),
    )
    checks.check(
        "no-axiom-edit",
        'hypothetical_axiom_status: "no edit"' in note
        and "does not add a mask clause" in normalized_note
        and "occupancy mask" not in axiom
        and "chiral-pair" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
