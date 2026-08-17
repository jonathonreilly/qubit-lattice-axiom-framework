#!/usr/bin/env python3
"""Occupancy, age-bit, and cube-orientation naming of leftover-frame f.

Same 12 perpendicular weight-4 masks and leftover-frame-positive section
f as the bitsec residual. This runner asks whether leftover slots and the
unique full axis are functions of occupancy σ alone, and whether the sign
that selects the section uses only the proper-cube-oriented triple
(leftover +, leftover −, full-axis +). Displayed, not adopted. No cache
is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/LEFTOVER_FRAME_SECTION_NAMING_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/LEFTOVER_FRAME_SECTION_NAMING_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}
AXES: tuple[tuple[int, int], ...] = ((0, 1), (2, 3), (4, 5))
AXIS_NAME = ("x", "y", "z")
SLOT_NAME = ("+x", "−x", "+y", "−y", "+z", "−z")
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER_SHOW = {EMPTY: "0", PLUS: "+", MINUS: "−"}
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the 12 perpendicular weight-4 masks, whether the '
    "leftover-frame-positive section is named by occupancy, the age bit, "
    'and cube orientation alone is reported. Displayed, not adopted."'
)
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))
EXPECTED_F: dict[tuple[Coloring, int], Coloring] = {
    ((0, 1, 0, 1, 1, 1), 0): (0, MINUS, 0, PLUS, MINUS, PLUS),
    ((0, 1, 0, 1, 1, 1), 1): (0, PLUS, 0, MINUS, PLUS, MINUS),
    ((0, 1, 1, 0, 1, 1), 0): (0, PLUS, MINUS, 0, MINUS, PLUS),
    ((0, 1, 1, 0, 1, 1), 1): (0, MINUS, PLUS, 0, PLUS, MINUS),
    ((0, 1, 1, 1, 0, 1), 0): (0, PLUS, MINUS, PLUS, 0, MINUS),
    ((0, 1, 1, 1, 0, 1), 1): (0, MINUS, PLUS, MINUS, 0, PLUS),
    ((0, 1, 1, 1, 1, 0), 0): (0, MINUS, MINUS, PLUS, PLUS, 0),
    ((0, 1, 1, 1, 1, 0), 1): (0, PLUS, PLUS, MINUS, MINUS, 0),
    ((1, 0, 0, 1, 1, 1), 0): (PLUS, 0, 0, MINUS, MINUS, PLUS),
    ((1, 0, 0, 1, 1, 1), 1): (MINUS, 0, 0, PLUS, PLUS, MINUS),
    ((1, 0, 1, 0, 1, 1), 0): (MINUS, 0, PLUS, 0, MINUS, PLUS),
    ((1, 0, 1, 0, 1, 1), 1): (PLUS, 0, MINUS, 0, PLUS, MINUS),
    ((1, 0, 1, 1, 0, 1), 0): (MINUS, 0, MINUS, PLUS, 0, PLUS),
    ((1, 0, 1, 1, 0, 1), 1): (PLUS, 0, PLUS, MINUS, 0, MINUS),
    ((1, 0, 1, 1, 1, 0), 0): (PLUS, 0, MINUS, PLUS, MINUS, 0),
    ((1, 0, 1, 1, 1, 0), 1): (MINUS, 0, PLUS, MINUS, PLUS, 0),
    ((1, 1, 0, 1, 0, 1), 0): (MINUS, PLUS, 0, MINUS, 0, PLUS),
    ((1, 1, 0, 1, 0, 1), 1): (PLUS, MINUS, 0, PLUS, 0, MINUS),
    ((1, 1, 0, 1, 1, 0), 0): (MINUS, PLUS, 0, PLUS, MINUS, 0),
    ((1, 1, 0, 1, 1, 0), 1): (PLUS, MINUS, 0, MINUS, PLUS, 0),
    ((1, 1, 1, 0, 0, 1), 0): (MINUS, PLUS, PLUS, 0, 0, MINUS),
    ((1, 1, 1, 0, 0, 1), 1): (PLUS, MINUS, MINUS, 0, 0, PLUS),
    ((1, 1, 1, 0, 1, 0), 0): (MINUS, PLUS, MINUS, 0, PLUS, 0),
    ((1, 1, 1, 0, 1, 0), 1): (PLUS, MINUS, PLUS, 0, MINUS, 0),
}
EXPECTED_LEFTOVER: dict[Coloring, tuple[int, int]] = {
    (0, 1, 0, 1, 1, 1): (1, 3),
    (0, 1, 1, 0, 1, 1): (1, 2),
    (0, 1, 1, 1, 0, 1): (1, 5),
    (0, 1, 1, 1, 1, 0): (1, 4),
    (1, 0, 0, 1, 1, 1): (0, 3),
    (1, 0, 1, 0, 1, 1): (0, 2),
    (1, 0, 1, 1, 0, 1): (0, 5),
    (1, 0, 1, 1, 1, 0): (0, 4),
    (1, 1, 0, 1, 0, 1): (3, 5),
    (1, 1, 0, 1, 1, 0): (3, 4),
    (1, 1, 1, 0, 0, 1): (2, 5),
    (1, 1, 1, 0, 1, 0): (2, 4),
}


def normalize(text: str) -> str:
    return " ".join(text.split())


def show_col(coloring: Coloring) -> str:
    return "(" + ", ".join(LETTER_SHOW[letter] for letter in coloring) + ")"


def show_slots(slots: tuple[int, ...]) -> str:
    return "(" + ", ".join(SLOT_NAME[index] for index in slots) + ")"


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def direction_perm(matrix: Matrix) -> tuple[int, ...]:
    return tuple(DIR_INDEX[mat_vec(matrix, direction)] for direction in DIRS)


def act_col(perm: tuple[int, ...], coloring: Coloring | Tick) -> tuple:
    out = [None] * len(coloring)
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


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != EMPTY) for letter in coloring)


def empty_slots(sigma: Coloring) -> tuple[int, int]:
    emptied = tuple(index for index, bit in enumerate(sigma) if bit == 0)
    if len(emptied) != 2:
        raise AssertionError(f"expected two empty slots, got {emptied}")
    return (emptied[0], emptied[1])


def same_axis(left: int, right: int) -> bool:
    return any({left, right} == set(axis) for axis in AXES)


def unique_full_axis(sigma: Coloring) -> int | None:
    named = tuple(
        axis_index
        for axis_index, (plus, minus) in enumerate(AXES)
        if sigma[plus] == 1 and sigma[minus] == 1
    )
    if len(named) == 1:
        return named[0]
    return None


def leftover_slots(sigma: Coloring) -> tuple[int, int] | None:
    named = unique_full_axis(sigma)
    if named is None:
        return None
    leftover = tuple(
        index
        for index in range(6)
        if sigma[index] == 1 and index not in AXES[named]
    )
    if len(leftover) != 2:
        return None
    return leftover


def weight4_masks() -> tuple[Coloring, ...]:
    return tuple(bits for bits in itertools.product((0, 1), repeat=6) if sum(bits) == 4)


def perp_masks() -> tuple[Coloring, ...]:
    return tuple(
        sigma
        for sigma in weight4_masks()
        if not same_axis(*empty_slots(sigma))
    )


def axis_letters(bit: int) -> tuple[int, int]:
    if bit == 1:
        return (PLUS, MINUS)
    return (MINUS, PLUS)


def july3_pair(perms: list[tuple[int, ...]]) -> frozenset[Coloring]:
    unseen = set(itertools.product((EMPTY, PLUS, MINUS), repeat=6))
    inversion = direction_perm(((-1, 0, 0), (0, -1, 0), (0, 0, -1)))
    pair: set[Coloring] = set()
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        unseen -= orbit
        image = act_col(inversion, next(iter(orbit)))
        if image not in orbit:
            pair |= orbit
    return frozenset(pair)


def completions(
    sigma: Coloring,
    bit: int,
    pair: frozenset[Coloring],
) -> tuple[Coloring, ...]:
    named = unique_full_axis(sigma)
    if named is None:
        return ()
    plus, minus = AXES[named]
    plus_letter, minus_letter = axis_letters(bit)
    matches = [
        item
        for item in pair
        if support(item) == sigma
        and item[plus] == plus_letter
        and item[minus] == minus_letter
    ]
    return tuple(sorted(matches))


def leftover_frame(coloring: Coloring) -> tuple[int, int, int] | None:
    named = unique_full_axis(support(coloring))
    leftover = leftover_slots(support(coloring))
    if named is None or leftover is None:
        return None
    plus_left = next(
        (index for index in leftover if coloring[index] == PLUS),
        None,
    )
    minus_left = next(
        (index for index in leftover if coloring[index] == MINUS),
        None,
    )
    plus_full = next(
        (index for index in AXES[named] if coloring[index] == PLUS),
        None,
    )
    if plus_left is None or minus_left is None or plus_full is None:
        return None
    return (plus_left, minus_left, plus_full)


def leftover_frame_sign(coloring: Coloring) -> int | None:
    frame = leftover_frame(coloring)
    if frame is None:
        return None
    plus_left, minus_left, plus_full = frame
    return det3((DIRS[plus_left], DIRS[minus_left], DIRS[plus_full]))


def frame_is_proper_cube(coloring: Coloring) -> bool:
    frame = leftover_frame(coloring)
    if frame is None:
        return False
    vectors = [DIRS[index] for index in frame]
    if len(set(vectors)) != 3:
        return False
    if any(sum(abs(component) for component in vector) != 1 for vector in vectors):
        return False
    axes = tuple(next(axis for axis, value in enumerate(vector) if value != 0) for vector in vectors)
    if set(axes) != {0, 1, 2}:
        return False
    sign = det3((vectors[0], vectors[1], vectors[2]))
    return sign in (-1, 1)


def named_by_occupancy_age_orientation(sigma: Coloring, bit: int) -> Coloring | None:
    """Name f(σ,b) from occupancy leftover/full slots, age-bit letters, and det +1."""
    named = unique_full_axis(sigma)
    leftover = leftover_slots(sigma)
    if named is None or leftover is None:
        return None
    plus_ax, minus_ax = AXES[named]
    plus_letter, minus_letter = axis_letters(bit)
    left_a, left_b = leftover
    hits: list[Coloring] = []
    for plus_left, minus_left in ((left_a, left_b), (left_b, left_a)):
        coloring_list = [EMPTY] * 6
        coloring_list[plus_ax] = plus_letter
        coloring_list[minus_ax] = minus_letter
        coloring_list[plus_left] = PLUS
        coloring_list[minus_left] = MINUS
        coloring = tuple(coloring_list)
        if leftover_frame_sign(coloring) == 1:
            hits.append(coloring)
    if len(hits) != 1:
        return None
    return hits[0]


def coloring_orbits(
    colorings: tuple[Coloring, ...],
    perms: list[tuple[int, ...]],
) -> list[frozenset[Coloring]]:
    unseen = set(colorings)
    orbits: list[frozenset[Coloring]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        unseen -= orbit
        orbits.append(frozenset(orbit))
    return orbits


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
    pair = july3_pair(perms)
    masks = perp_masks()

    occupancy_only = True
    leftover_independent_of_bit = True
    both_two = True
    named_unique = True
    named_matches_section = True
    frames_proper = True
    signs_split = True
    only_leftover_swap = True
    n_name = 0
    named_rows: list[tuple] = []
    section: dict[tuple[Coloring, int], Coloring] = {}
    named_rule: dict[tuple[Coloring, int], Coloring] = {}
    points: list[Coloring] = []

    for sigma in masks:
        named = unique_full_axis(sigma)
        leftover = leftover_slots(sigma)
        if named is None or leftover is None or leftover != EXPECTED_LEFTOVER[sigma]:
            occupancy_only = False
        leftover_from_bits: list[tuple[int, int] | None] = []
        leftover_from_colorings: list[tuple[int, int] | None] = []
        mask_named = True
        for bit in (0, 1):
            found = completions(sigma, bit, pair)
            if len(found) != 2:
                both_two = False
                mask_named = False
                continue
            points.extend(found)
            leftover_from_bits.append(leftover)
            signs = [leftover_frame_sign(item) for item in found]
            if set(signs) != {1, -1}:
                signs_split = False
                mask_named = False
            positive = [item for item in found if leftover_frame_sign(item) == 1]
            if len(positive) != 1:
                mask_named = False
                continue
            section[(sigma, bit)] = positive[0]
            leftover_from_colorings.append(leftover_slots(support(positive[0])))
            if leftover_slots(support(found[0])) != leftover:
                leftover_independent_of_bit = False
            if leftover_slots(support(found[1])) != leftover:
                leftover_independent_of_bit = False
            letters_full = (
                found[0][AXES[named][0]],
                found[0][AXES[named][1]],
            )
            letters_full_other = (
                found[1][AXES[named][0]],
                found[1][AXES[named][1]],
            )
            if letters_full != letters_full_other:
                only_leftover_swap = False
            leftover_letters = tuple(found[0][index] for index in leftover)
            leftover_letters_other = tuple(found[1][index] for index in leftover)
            if leftover_letters == leftover_letters_other:
                only_leftover_swap = False
            if set(leftover_letters) != {PLUS, MINUS}:
                only_leftover_swap = False
            named_coloring = named_by_occupancy_age_orientation(sigma, bit)
            if named_coloring is None:
                named_unique = False
                mask_named = False
                continue
            named_rule[(sigma, bit)] = named_coloring
            if named_coloring != positive[0] or named_coloring != EXPECTED_F[(sigma, bit)]:
                named_matches_section = False
                mask_named = False
            if not frame_is_proper_cube(named_coloring):
                frames_proper = False
                mask_named = False
            if leftover_frame_sign(named_coloring) != 1:
                frames_proper = False
                mask_named = False
        if leftover_from_bits and len(set(leftover_from_bits)) != 1:
            leftover_independent_of_bit = False
            occupancy_only = False
        if leftover_from_colorings and leftover_from_colorings != [leftover, leftover]:
            leftover_independent_of_bit = False
            occupancy_only = False
        if (
            mask_named
            and occupancy_only
            and leftover_independent_of_bit
            and named_unique
            and named_matches_section
            and frames_proper
            and signs_split
        ):
            n_name += 1
        f0 = named_rule.get((sigma, 0))
        f1 = named_rule.get((sigma, 1))
        frame0 = leftover_frame(f0) if f0 is not None else None
        named_rows.append(
            (
                sigma,
                AXIS_NAME[named] if named is not None else None,
                leftover,
                f0,
                f1,
                leftover_frame_sign(f0) if f0 is not None else None,
                show_slots(frame0) if frame0 is not None else None,
            )
        )

    all_colorings = tuple(points)
    orbits = coloring_orbits(all_colorings, perms)
    n_orbits = len(orbits)
    sign_is_orbit_invariant = True
    for coloring in all_colorings:
        seed_sign = leftover_frame_sign(coloring)
        for perm in perms:
            if leftover_frame_sign(act_col(perm, coloring)) != seed_sign:
                sign_is_orbit_invariant = False
    orbit_signs = []
    for orbit in orbits:
        signs = {leftover_frame_sign(item) for item in orbit}
        if signs != {1} and signs != {-1}:
            sign_is_orbit_invariant = False
        orbit_signs.append(next(iter(signs)))
    no_second_gplus_invariant = (
        n_orbits == 2
        and set(orbit_signs) == {1, -1}
        and sign_is_orbit_invariant
        and only_leftover_swap
        and all(
            leftover_frame_sign(section[(sigma, bit)]) == 1
            and leftover_frame_sign(
                next(
                    item
                    for item in completions(sigma, bit, pair)
                    if item != section[(sigma, bit)]
                )
            )
            == -1
            for sigma in masks
            for bit in (0, 1)
            if (sigma, bit) in section
        )
    )
    no_second_occupancy_independent_bit = (
        named_unique
        and named_matches_section
        and only_leftover_swap
        and no_second_gplus_invariant
        and n_name == 12
    )

    print("leftover-frame section naming")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"N_perp={len(masks)}")
    print(f"N_pair={len(pair)}")
    print(f"N_completions={len(all_colorings)}")
    print(f"N_orbits={n_orbits}")
    print(f"N_name={n_name}")
    print(f"occupancy_only={occupancy_only}")
    print(f"leftover_independent_of_bit={leftover_independent_of_bit}")
    print(f"named_unique={named_unique}")
    print(f"named_matches_section={named_matches_section}")
    print(f"frames_proper={frames_proper}")
    print(f"signs_split={signs_split}")
    print(f"only_leftover_swap={only_leftover_swap}")
    print(f"sign_is_orbit_invariant={sign_is_orbit_invariant}")
    print(f"no_second_gplus_invariant={no_second_gplus_invariant}")
    print(f"no_second_occupancy_independent_bit={no_second_occupancy_independent_bit}")
    print("perp_rows:")
    for sigma, axis, leftover, f0, f1, sign0, frame0 in named_rows:
        print(
            f"  {sigma} full={axis} leftover={show_slots(leftover) if leftover else None} "
            f"f0={show_col(f0) if f0 is not None else None} "
            f"f1={show_col(f1) if f1 is not None else None} "
            f"frame0={frame0} sign0={sign0} named=1"
        )

    expected_paths = (
        "docs/LEFTOVER_FRAME_SECTION_NAMING_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        and det3(SWAPPER) == 1
        and SWAPPER in rotations,
        f"proper={len(rotations)}",
    )
    checks.check(
        "twelve-perp-masks",
        len(masks) == 12
        and all(unique_full_axis(sigma) is not None for sigma in masks)
        and both_two
        and len(all_colorings) == 48
        and len(set(all_colorings)) == 48
        and "12 perpendicular" in note,
        f"N_perp={len(masks)} N_completions={len(all_colorings)}",
    )
    checks.check(
        "theorem-1-occupancy-named",
        occupancy_only
        and leftover_independent_of_bit
        and all(leftover_slots(sigma) == EXPECTED_LEFTOVER[sigma] for sigma in masks)
        and all(
            leftover_slots(sigma) is not None
            and unique_full_axis(sigma) is not None
            for sigma in masks
        )
        and "functions of σ alone" in note_flat
        and "leftover slots" in note
        and "unique full axis" in note,
        "leftover slots and full axis are functions of occupancy alone",
    )
    checks.check(
        "theorem-2-n-name",
        n_name == 12
        and named_unique
        and named_matches_section
        and frames_proper
        and signs_split
        and no_second_occupancy_independent_bit
        and no_second_gplus_invariant
        and all(
            named_rule[(sigma, bit)] == EXPECTED_F[(sigma, bit)]
            for sigma in masks
            for bit in (0, 1)
        )
        and "N_name=12" in note
        and "proper-cube oriented" in note
        and "No second occupancy-independent bit" in note,
        f"N_name={n_name}",
    )
    checks.check(
        "same-f-as-bitsec",
        all(
            leftover_frame_sign(EXPECTED_F[(sigma, bit)]) == 1
            for sigma in masks
            for bit in (0, 1)
        )
        and "Same 12 masks and f as bitsec" in note_flat,
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write the frame into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-bitsec",
        "not leftover of bitsec" in note_flat
        and "existence" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_name" not in axiom
        and "bitsec" not in axiom
        and "leftover-frame" not in axiom,
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

    print("per_element: leftover slots, full axis, frame sign, and N_name are exact")
    print("per_site: 12 perpendicular weight-4 occupancy masks scored")
    print("per_mode: no spectral calculation")
    print("per_block: 6-NN star masks and G+ only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
