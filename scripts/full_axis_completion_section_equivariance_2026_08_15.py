#!/usr/bin/env python3
"""G+-equivariant section of the two full-axis pair-completions.

Same opposite-letter write on the occupancy-named full axis as the age-bit
encoding. Each of the 24 (σ,b) pairs has two July-3 pair completions.
This runner counts G+ orbits on those 48 completions, asks whether a
section can pick one point per (σ,b) orbit-consistently, and if so
exhibits the leftover-frame-positive section (not lex-first) and scores
N_commute. Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/FULL_AXIS_COMPLETION_SECTION_EQUIVARIANCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/FULL_AXIS_COMPLETION_SECTION_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
EMPTY, PLUS, MINUS = 0, 1, 2
LETTER_SHOW = {EMPTY: "0", PLUS: "+", MINUS: "−"}
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the 12 perpendicular weight-4 masks, whether a '
    "G+-equivariant section of the two pair-completions of the age-bit "
    'encoding exists is reported. Displayed, not adopted."'
)
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))
FAIL_SIGMA: Coloring = (0, 1, 0, 1, 1, 1)
FAIL_G: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
OK_G: Matrix = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
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


def normalize(text: str) -> str:
    return " ".join(text.split())


def show_col(coloring: Coloring) -> str:
    return "(" + ", ".join(LETTER_SHOW[letter] for letter in coloring) + ")"


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


def weight4_masks() -> tuple[Coloring, ...]:
    return tuple(bits for bits in itertools.product((0, 1), repeat=6) if sum(bits) == 4)


def perp_masks() -> tuple[Coloring, ...]:
    return tuple(
        sigma
        for sigma in weight4_masks()
        if not same_axis(*empty_slots(sigma))
    )


def display_ticks(sigma: Coloring, axis_index: int, bit: int) -> Tick:
    plus, minus = AXES[axis_index]
    ticks: list[int | None] = [None] * 6
    for slot, occupied in enumerate(sigma):
        if occupied == 0:
            continue
        if slot == minus:
            ticks[slot] = 1 if bit == 1 else 2
        elif slot == plus:
            ticks[slot] = 2 if bit == 1 else 1
        else:
            ticks[slot] = 0
    return tuple(ticks)


def bit_on_axis(ticks: Tick, axis_index: int) -> int:
    plus, minus = AXES[axis_index]
    minus_tick = ticks[minus]
    plus_tick = ticks[plus]
    if minus_tick is not None and plus_tick is not None and minus_tick < plus_tick:
        return 1
    return 0


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


def leftover_frame_sign(coloring: Coloring) -> int:
    named = unique_full_axis(support(coloring))
    if named is None:
        raise AssertionError("completion has no unique full axis")
    leftover = [
        index
        for index in range(6)
        if support(coloring)[index] == 1 and index not in AXES[named]
    ]
    plus_left = next(index for index in leftover if coloring[index] == PLUS)
    minus_left = next(index for index in leftover if coloring[index] == MINUS)
    plus_full = next(index for index in AXES[named] if coloring[index] == PLUS)
    return det3((DIRS[plus_left], DIRS[minus_left], DIRS[plus_full]))


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


def commute_count(
    masks: tuple[Coloring, ...],
    perms: list[tuple[int, ...]],
    rule: dict[tuple[Coloring, int], Coloring],
) -> tuple[int, list[int]]:
    n_commute = 0
    per_mask: list[int] = []
    for sigma in masks:
        named = unique_full_axis(sigma)
        if named is None:
            per_mask.append(0)
            continue
        mask_commute = 0
        for bit in (0, 1):
            if (sigma, bit) not in rule:
                continue
            ticks = display_ticks(sigma, named, bit)
            coloring = rule[(sigma, bit)]
            for perm in perms:
                sigma_g = act_col(perm, sigma)
                named_g = unique_full_axis(sigma_g)
                if named_g is None:
                    continue
                bit_g = bit_on_axis(act_col(perm, ticks), named_g)
                image = rule.get((sigma_g, bit_g))
                if image is not None and image == act_col(perm, coloring):
                    n_commute += 1
                    mask_commute += 1
        per_mask.append(mask_commute)
    return n_commute, per_mask


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
    commute_denom = len(masks) * 2 * len(rotations)

    comps: dict[tuple[Coloring, int], tuple[Coloring, ...]] = {}
    points: list[Coloring] = []
    both_two = True
    for sigma in masks:
        for bit in (0, 1):
            found = completions(sigma, bit, pair)
            comps[(sigma, bit)] = found
            if len(found) != 2:
                both_two = False
            points.extend(found)
    all_colorings = tuple(points)
    orbits = coloring_orbits(all_colorings, perms)
    n_orbits = len(orbits)
    fiber_one = True
    covers_all = True
    all_keys = {(sigma, bit) for sigma in masks for bit in (0, 1)}
    for orbit in orbits:
        keys = set()
        for coloring in orbit:
            sigma = support(coloring)
            named = unique_full_axis(sigma)
            if named is None:
                fiber_one = False
                continue
            plus, minus = AXES[named]
            bit = 1 if coloring[minus] == MINUS and coloring[plus] == PLUS else 0
            if (sigma, bit) in keys:
                fiber_one = False
            keys.add((sigma, bit))
        if keys != all_keys:
            covers_all = False
    n_section = sum(1 for orbit in orbits if fiber_one and len(orbit) == len(all_keys))

    lex_rule: dict[tuple[Coloring, int], Coloring] = {}
    section: dict[tuple[Coloring, int], Coloring] = {}
    signs_ok = True
    for sigma in masks:
        for bit in (0, 1):
            found = comps[(sigma, bit)]
            if not found:
                continue
            lex_rule[(sigma, bit)] = found[0]
            positive = [item for item in found if leftover_frame_sign(item) == 1]
            negative = [item for item in found if leftover_frame_sign(item) == -1]
            if len(positive) != 1 or len(negative) != 1:
                signs_ok = False
                continue
            section[(sigma, bit)] = positive[0]
    n_lex_diff = sum(
        1
        for key in section
        if key in lex_rule and section[key] != lex_rule[key]
    )
    n_commute, per_mask = commute_count(masks, perms, section)
    n_lex, _ = commute_count(masks, perms, lex_rule)

    fail_perm = direction_perm(FAIL_G)
    fail_named = unique_full_axis(FAIL_SIGMA)
    fail_ticks = display_ticks(FAIL_SIGMA, fail_named, 0) if fail_named is not None else None
    fail_sigma_g = act_col(fail_perm, FAIL_SIGMA)
    fail_named_g = unique_full_axis(fail_sigma_g)
    fail_bit_g = (
        bit_on_axis(act_col(fail_perm, fail_ticks), fail_named_g)
        if fail_ticks is not None and fail_named_g is not None
        else None
    )
    fail_lhs = section.get((fail_sigma_g, fail_bit_g)) if fail_bit_g is not None else None
    fail_rhs = (
        act_col(fail_perm, section[(FAIL_SIGMA, 0)])
        if (FAIL_SIGMA, 0) in section
        else None
    )
    lex_lhs = lex_rule.get((fail_sigma_g, fail_bit_g)) if fail_bit_g is not None else None
    lex_rhs = (
        act_col(fail_perm, lex_rule[(FAIL_SIGMA, 0)])
        if (FAIL_SIGMA, 0) in lex_rule
        else None
    )

    ok_perm = direction_perm(OK_G)
    ok_ticks = display_ticks(FAIL_SIGMA, fail_named, 0) if fail_named is not None else None
    ok_sigma_g = act_col(ok_perm, FAIL_SIGMA)
    ok_named_g = unique_full_axis(ok_sigma_g)
    ok_bit_g = (
        bit_on_axis(act_col(ok_perm, ok_ticks), ok_named_g)
        if ok_ticks is not None and ok_named_g is not None
        else None
    )
    ok_lhs = section.get((ok_sigma_g, ok_bit_g)) if ok_bit_g is not None else None
    ok_rhs = (
        act_col(ok_perm, section[(FAIL_SIGMA, 0)])
        if (FAIL_SIGMA, 0) in section
        else None
    )

    print("full-axis completion section G+ equivariance")
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
    print(f"N_section={n_section}")
    print(f"section_fiber_one={fiber_one}")
    print(f"section_covers_all={covers_all}")
    print(f"N_denom={commute_denom}")
    print(f"N_commute={n_commute}")
    print(f"N_commute_over_denom={n_commute}/{commute_denom}")
    print(f"N_commute_eq_576={n_commute == 576}")
    print(f"N_lex_commute={n_lex}")
    print(f"N_lex_diff={n_lex_diff}")
    print("perp_rows:")
    for sigma, count in zip(masks, per_mask):
        named = unique_full_axis(sigma)
        axis = AXIS_NAME[named] if named is not None else None
        f0 = section.get((sigma, 0))
        f1 = section.get((sigma, 1))
        n0 = len(comps.get((sigma, 0), ()))
        n1 = len(comps.get((sigma, 1), ()))
        print(
            f"  {sigma} full={axis} n_comp={n0},{n1} "
            f"f0={show_col(f0) if f0 is not None else None} "
            f"f1={show_col(f1) if f1 is not None else None} "
            f"commute={count}/48"
        )

    expected_paths = (
        "docs/FULL_AXIS_COMPLETION_SECTION_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        and "12 perpendicular" in note
        and "`12 × 2 × 24 = 576`" in note,
        f"N_perp={len(masks)} N_completions={len(all_colorings)}",
    )
    checks.check(
        "theorem-1-n-orbits",
        n_orbits == 2
        and fiber_one
        and covers_all
        and n_section == 2
        and all(len(orbit) == 24 for orbit in orbits)
        and "N_orbits = 2" in note
        and "orbit-consistently" in note
        and "one point per" in note,
        f"N_orbits={n_orbits} N_section={n_section}",
    )
    checks.check(
        "theorem-2-n-commute",
        signs_ok
        and n_commute == 576
        and commute_denom == 576
        and n_section != 0
        and per_mask == [48] * 12
        and all(
            section[(sigma, bit)] == EXPECTED_F[(sigma, bit)]
            for sigma in masks
            for bit in (0, 1)
        )
        and n_lex_diff == 12
        and n_lex == 288
        and "N_commute = 576" in note
        and "not lex-first" in note,
        f"N_commute={n_commute}/{commute_denom} lex={n_lex} diff={n_lex_diff}",
    )
    checks.check(
        "section-witness",
        fail_lhs == fail_rhs == (PLUS, 0, 0, MINUS, MINUS, PLUS)
        and fail_bit_g == 0
        and fail_sigma_g == (1, 0, 0, 1, 1, 1)
        and lex_lhs == (PLUS, 0, 0, MINUS, MINUS, PLUS)
        and lex_rhs == (MINUS, 0, 0, PLUS, MINUS, PLUS)
        and lex_lhs != lex_rhs
        and ok_lhs == ok_rhs == (MINUS, 0, PLUS, 0, MINUS, PLUS)
        and "`g : (x, y, z) ↦ (−y, x, z)`" in note
        and "`f(σ_g, b_g) = g · f(σ,b)`" in note
        and "`(0, −, 0, +, −, +)`" in note,
        f"lhs={fail_lhs} rhs={fail_rhs}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a section into Admissibility" in note
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
        "not-leftover-bitenc",
        "not leftover of bitenc" in note_flat
        and "lex-first" in note
        and "N_commute=288/576" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_commute" not in axiom
        and "N_orbits" not in axiom
        and "bitenc" not in axiom,
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

    print("per_element: N_orbits, N_section, N_commute, and f(σ,b) are exact")
    print("per_site: 12 perpendicular weight-4 occupancy masks scored")
    print("per_mode: no spectral calculation")
    print("per_block: 6-NN star masks and G+ only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
