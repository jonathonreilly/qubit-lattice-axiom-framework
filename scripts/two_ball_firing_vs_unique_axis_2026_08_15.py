#!/usr/bin/env python3
"""Four firing pair members versus unique-axis +y=+ and +z=+.

Rebuild the July-3 k=3 pair members on the two-ball witness mask
(1,1,1,0,1,0). Count how many of those four 6-tuples have +y=+ and +z=+.
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/TWO_BALL_FIRING_VS_UNIQUE_AXIS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
JULY3_PATH = ROOT / (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_"
    "OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_"
    "BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/TWO_BALL_FIRING_VS_UNIQUE_AXIS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

EMPTY, PLUS, MINUS, NO_AXIS = 0, 1, 2, 3
LETTERS = (EMPTY, PLUS, MINUS)
LETTER_SHOW = {EMPTY: "0", PLUS: "+", MINUS: "-", NO_AXIS: "*"}
PLUS_Y_SLOT = 2
PLUS_Z_SLOT = 4
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


def occupancy_bits(
    site: tuple[int, int, int], occupied: frozenset[tuple[int, int, int]]
) -> tuple[int, ...]:
    return tuple(1 if add(site, direction) in occupied else 0 for direction in DIRS)


def dipole(bits: tuple[int, ...]) -> tuple[int, int, int]:
    return (bits[0] - bits[1], bits[2] - bits[3], bits[4] - bits[5])


def kernel(bits: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    dx, dy, dz = dipole(bits)
    return (Fraction(dx, 3), Fraction(dy, 3), Fraction(dz, 3))


def unique_axis_label(n_vec: tuple[Fraction, Fraction, Fraction]) -> int:
    support = [index for index, value in enumerate(n_vec) if value != 0]
    if len(support) != 1:
        return NO_AXIS
    value = n_vec[support[0]]
    if value > 0:
        return PLUS
    if value < 0:
        return MINUS
    return NO_AXIS


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

    neighbor_labels = []
    for site, bit in zip(neighbor_sites, derived_mask):
        if bit == 0:
            neighbor_labels.append(EMPTY)
            continue
        neighbor_labels.append(unique_axis_label(kernel(occupancy_bits(site, occupied))))
    unique_axis_plus_y = neighbor_labels[PLUS_Y_SLOT]
    unique_axis_plus_z = neighbor_labels[PLUS_Z_SLOT]

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

    fillings: list[tuple[int, ...]] = []
    for bits in itertools.product((PLUS, MINUS), repeat=len(occupied_idx)):
        coloring = [EMPTY] * len(DIRS)
        for index, letter in zip(occupied_idx, bits):
            coloring[index] = letter
        fillings.append(tuple(coloring))
    firing = sorted(coloring for coloring in fillings if coloring in pair)
    n_fire = len(firing)
    agreeing = [
        coloring
        for coloring in firing
        if coloring[PLUS_Y_SLOT] == PLUS and coloring[PLUS_Z_SLOT] == PLUS
    ]
    n_agree = len(agreeing)
    excludes_every_firing = n_agree == 0

    print("Two-ball firing 6-tuples versus unique-axis +y=+ and +z=+")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"derived_mask: {derived_mask}")
    print(f"occupied_neighbors: {tuple(neighbor_sites[i] for i in occupied_idx)}")
    print(f"empty_neighbors: {tuple(neighbor_sites[i] for i in empty_idx)}")
    print(f"N_pair: {n_pair}")
    print(f"N_fire: {n_fire}")
    print(f"firing: {[show_tuple(item) for item in firing]}")
    print(f"unique_axis_plus_y: {LETTER_SHOW[unique_axis_plus_y]}")
    print(f"unique_axis_plus_z: {LETTER_SHOW[unique_axis_plus_z]}")
    print(f"N_agree: {n_agree}")
    print(f"agreeing: {[show_tuple(item) for item in agreeing]}")
    print(f"unique_axis_excludes_every_firing: {excludes_every_firing}")

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
            "docs/TWO_BALL_FIRING_VS_UNIQUE_AXIS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        n_pair == 48 and all(fully_mixed(coloring) for coloring in pair),
        f"N_pair={n_pair}",
    )
    expected_firing = [
        (PLUS, MINUS, PLUS, EMPTY, MINUS, EMPTY),
        (PLUS, MINUS, MINUS, EMPTY, PLUS, EMPTY),
        (MINUS, PLUS, PLUS, EMPTY, MINUS, EMPTY),
        (MINUS, PLUS, MINUS, EMPTY, PLUS, EMPTY),
    ]
    checks.check(
        "four-firing-six-tuples",
        n_fire == 4
        and firing == expected_firing
        and all(occupancy_mask(item) == derived_mask for item in firing),
        f"firing={[show_tuple(item) for item in firing]}",
    )
    checks.check(
        "unique-axis-fragment-plus-y-plus-z",
        unique_axis_plus_y == PLUS
        and unique_axis_plus_z == PLUS
        and neighbor_labels[0] == NO_AXIS
        and neighbor_labels[1] == NO_AXIS,
        f"+y={LETTER_SHOW[unique_axis_plus_y]} +z={LETTER_SHOW[unique_axis_plus_z]}",
    )
    checks.check(
        "n-agree",
        n_agree == 0 and agreeing == [],
        f"N_agree={n_agree}",
    )
    checks.check(
        "unique-axis-excludes-every-firing",
        excludes_every_firing is True
        and n_agree == 0
        and all(
            not (item[PLUS_Y_SLOT] == PLUS and item[PLUS_Z_SLOT] == PLUS)
            for item in firing
        ),
    )

    claim_scope = (
        "Among the 4 July-3 pair members on the two-ball witness mask, "
        "how many agree with unique-axis labels +y=+ and +z=+ is reported. "
        "Displayed, not adopted."
    )
    checks.check("claim-scope-pinned", claim_scope in note)
    checks.check(
        "note-report-numbers",
        "N_pair = 48" in note
        and "N_fire = 4" in note
        and "N_agree = 0" in note
        and "mask = (1, 1, 1, 0, 1, 0)" in note
        and "unique_axis_plus_y = +" in note
        and "unique_axis_plus_z = +" in note
        and "unique_axis_excludes_every_firing = true" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "displayed, not adopted" in normalized_note
        and "not written into Admissibility" in normalized_note
        and "written_into_admissibility = false" in note
        and "Do not write a tie-break into Admissibility" in note
        and "tie_break_written_into_admissibility = false" in note,
    )
    checks.check(
        "not-attached-to-l1",
        "not attached to L1" in normalized_note
        and "attached_to_L1 = false" in note
        and "Do not attach L1" in note,
    )
    checks.check(
        "not-leftover-char",
        "not leftover-char of the full occupancy-kernel" in normalized_note
        and "full kernel 6-tuple with" in normalized_note
        and "does not score a full kernel 6-tuple" in normalized_note,
    )
    checks.check(
        "same-six-tuple-census-only",
        "does not** open a new spatial patch" in normalized_note
        or "does not open a new spatial patch" in normalized_note,
    )
    checks.check(
        "no-forbidden-phrases",
        all(phrase not in note and phrase not in axiom for phrase in FORBIDDEN),
    )
    checks.check(
        "no-axiom-edit",
        'hypothetical_axiom_status: "no edit"' in note
        and "does not add a unique-axis clause" in normalized_note
        and "unique-axis" not in axiom
        and "tie-break" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
