#!/usr/bin/env python3
"""All 4-NN unread sites of U versus unique-axis July-3 agreement.

On U = B_2(0) ∪ B_2((2,0,0)), enumerate every unread site in the
|x|,|y|,|z| ≤ 6 box with exactly four occupied 6-NN. For each, rebuild
the occupancy mask, count July-3 k=3 pair members on that mask, label
unambiguous occupied neighbors by unique-axis sign, and count how many
pair members match every unique-axis label.
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/TWO_BALL_ALL_4NN_UNIQUE_AXIS_AGREE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
JULY3_PATH = ROOT / (
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_"
    "OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_"
    "BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/TWO_BALL_ALL_4NN_UNIQUE_AXIS_AGREE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
CENTER_P = (2, 0, 0)
RADIUS = 2
BOX = 6
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


def matches_unique_axis(coloring: tuple[int, ...], labels: tuple[int, ...]) -> bool:
    for letter, label in zip(coloring, labels):
        if label in (PLUS, MINUS) and letter != label:
            return False
    return True


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


def july3_pair() -> tuple[set[tuple[int, ...]], int, int, int]:
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
    pair = set().union(*(proper_orbits[index] for index in chiral_ids))
    return pair, len(records), len(proper_perms), len(proper_orbits)


def score_site(
    site: tuple[int, int, int],
    occupied: frozenset[tuple[int, int, int]],
    pair: set[tuple[int, ...]],
) -> dict[str, object]:
    neighbor_sites = tuple(add(site, direction) for direction in DIRS)
    mask = tuple(1 if neighbor in occupied else 0 for neighbor in neighbor_sites)
    occupied_idx = tuple(index for index, bit in enumerate(mask) if bit == 1)
    labels: list[int] = []
    for neighbor, bit in zip(neighbor_sites, mask):
        if bit == 0:
            labels.append(EMPTY)
            continue
        labels.append(unique_axis_label(kernel(occupancy_bits(neighbor, occupied))))
    labels_t = tuple(labels)
    n_unique_axis = sum(1 for label in labels_t if label in (PLUS, MINUS))
    fillings: list[tuple[int, ...]] = []
    for bits in itertools.product((PLUS, MINUS), repeat=len(occupied_idx)):
        coloring = [EMPTY] * len(DIRS)
        for index, letter in zip(occupied_idx, bits):
            coloring[index] = letter
        fillings.append(tuple(coloring))
    firing = sorted(coloring for coloring in fillings if coloring in pair)
    agreeing = [
        coloring for coloring in firing if matches_unique_axis(coloring, labels_t)
    ]
    return {
        "site": site,
        "mask": mask,
        "labels": labels_t,
        "N_fire": len(firing),
        "N_unique_axis": n_unique_axis,
        "N_agree": len(agreeing),
        "firing": firing,
        "agreeing": agreeing,
        "occupied_neighbors": tuple(neighbor_sites[i] for i in occupied_idx),
    }


def box_unread_4nn(
    occupied: frozenset[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for coords in itertools.product(range(-BOX, BOX + 1), repeat=3):
        if coords in occupied:
            continue
        count = sum(1 for direction in DIRS if add(coords, direction) in occupied)
        if count == 4:
            sites.append(coords)
    return sites


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
    pair, n_signed, n_proper, n_orbits = july3_pair()
    n_pair = len(pair)
    four_nn = box_unread_4nn(occupied)
    rows = [score_site(site, occupied, pair) for site in four_nn]
    n_4 = len(rows)
    positive = [row for row in rows if int(row["N_agree"]) > 0]
    n_pos = len(positive)
    lex_first_four = rows[0]["site"] if rows else None
    lex_first_pos = positive[0]["site"] if positive else None
    one_agreeing = positive[0]["agreeing"][0] if positive and positive[0]["agreeing"] else None
    forbids_every = n_pos == 0
    u_inside_box = all(max(abs(coord) for coord in site) <= BOX for site in occupied)

    print("All 4-NN unread sites of two-ball U versus unique-axis agreement")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"|U|: {len(occupied)}")
    print(f"box: |x|,|y|,|z|<={BOX}")
    print(f"N_pair: {n_pair}")
    print(f"N_4: {n_4}")
    for row in rows:
        print(
            "site={0} mask={1} labels={2} N_fire={3} N_unique_axis={4} N_agree={5}".format(
                row["site"],
                row["mask"],
                show_tuple(row["labels"]),
                row["N_fire"],
                row["N_unique_axis"],
                row["N_agree"],
            )
        )
    print(f"N_pos: {n_pos}")
    print(f"lex_first_4nn: {lex_first_four}")
    print(f"lex_first_positive: {lex_first_pos}")
    print(
        "one_agreeing: {0}".format(
            show_tuple(one_agreeing) if one_agreeing is not None else None
        )
    )
    print(f"unique_axis_forbids_every_4nn: {forbids_every}")

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
            "docs/TWO_BALL_ALL_4NN_UNIQUE_AXIS_AGREE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "score-radius-6-box-only",
        BOX == 6
        and u_inside_box
        and all(max(abs(coord) for coord in row["site"]) <= BOX for row in rows)
        and "radius-6 box" in normalized_note
        and "|x|,|y|,|z| ≤ 6" in note,
    )
    checks.check(
        "proper-group-order",
        n_signed == 48 and n_proper == 24,
        f"full={n_signed} proper={n_proper}",
    )
    checks.check(
        "unique-chiral-pair",
        n_orbits == 57 and n_pair == 48 and all(fully_mixed(item) for item in pair),
        f"orbits={n_orbits} N_pair={n_pair}",
    )

    expected_sites = ((1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1))
    expected_masks = {
        (1, -1, -1): (1, 1, 1, 0, 1, 0),
        (1, -1, 1): (1, 1, 1, 0, 0, 1),
        (1, 1, -1): (1, 1, 0, 1, 1, 0),
        (1, 1, 1): (1, 1, 0, 1, 0, 1),
    }
    expected_labels = {
        (1, -1, -1): (NO_AXIS, NO_AXIS, PLUS, EMPTY, PLUS, EMPTY),
        (1, -1, 1): (NO_AXIS, NO_AXIS, MINUS, EMPTY, EMPTY, PLUS),
        (1, 1, -1): (NO_AXIS, NO_AXIS, EMPTY, PLUS, MINUS, EMPTY),
        (1, 1, 1): (NO_AXIS, NO_AXIS, EMPTY, MINUS, EMPTY, MINUS),
    }
    expected_agree = {
        (1, -1, -1): 0,
        (1, -1, 1): 2,
        (1, 1, -1): 2,
        (1, 1, 1): 0,
    }
    site_ok = (
        n_4 == 4
        and tuple(row["site"] for row in rows) == expected_sites
        and all(row["mask"] == expected_masks[row["site"]] for row in rows)
        and all(row["labels"] == expected_labels[row["site"]] for row in rows)
        and all(row["N_fire"] == 4 for row in rows)
        and all(row["N_unique_axis"] == 2 for row in rows)
        and all(row["N_agree"] == expected_agree[row["site"]] for row in rows)
    )
    checks.check(
        "theorem-1-four-unread-4nn",
        site_ok and len(occupied) == 43,
        f"N_4={n_4} sites={[row['site'] for row in rows]}",
    )
    checks.check(
        "lex-first-4nn-n-agree-zero",
        lex_first_four == (1, -1, -1)
        and rows[0]["N_agree"] == 0
        and rows[0]["mask"] == (1, 1, 1, 0, 1, 0),
    )
    expected_one = (PLUS, MINUS, MINUS, EMPTY, EMPTY, PLUS)
    checks.check(
        "theorem-2-n-pos",
        n_pos == 2
        and lex_first_pos == (1, -1, 1)
        and one_agreeing == expected_one
        and forbids_every is False
        and expected_one in positive[0]["agreeing"],
        f"N_pos={n_pos} v={lex_first_pos} c={show_tuple(one_agreeing) if one_agreeing else None}",
    )

    claim_scope = (
        "On U=B_2(0)∪B_2((2,0,0)) inside the radius-6 box, whether any "
        "unread 4-occupied-NN site has a July-3 pair member agreeing with "
        "that site’s unique-axis labels is reported. Displayed, not adopted."
    )
    checks.check("claim-scope-pinned", claim_scope in note)
    checks.check(
        "note-report-numbers",
        "N_4 = 4" in note
        and "N_pos = 2" in note
        and "N_pair = 48" in note
        and "lex_first_positive = (1, -1, 1)" in note
        and "one_agreeing = (+, -, -, 0, 0, +)" in note
        and "unique_axis_forbids_every_4nn = false" in note
        and "N_agree = [0, 2, 2, 0]" in note
        and "N_fire = [4, 4, 4, 4]" in note
        and "N_unique_axis = [2, 2, 2, 2]" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "displayed, not adopted" in normalized_note
        and "not written into Admissibility" in normalized_note
        and "written_into_admissibility = false" in note
        and "Do not write a site list into Admissibility" in note
        and "site_list_written_into_admissibility = false" in note,
    )
    checks.check(
        "not-attached-to-l1",
        "not attached to L1" in normalized_note
        and "attached_to_L1 = false" in note
        and "Do not attach L1" in note,
    )
    checks.check(
        "not-leftover-char-one-witness",
        "not leftover-char of the one-witness unique-axis agreement" in normalized_note
        and "lex-first 4-NN unread site" in normalized_note
        and "does not stop at the lex-first witness" in normalized_note,
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
        and "site list" not in axiom
        and axiom.count("B_2") == 0,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
