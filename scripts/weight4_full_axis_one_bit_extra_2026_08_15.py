#!/usr/bin/env python3
"""Occupancy names the unique full axis; the extra is one age bit.

Score all 15 weight-4 occupancy masks. N_perp=12 empty two perpendicular
slots and have a unique full axis. N_axis=3 empty a whole axis and have
no pair support. On each of the 12, a single older/newer bit on the
named axis kills every occupancy stabilizer that swaps those two ends.
Report that for the uneqrad mask; the pattern is the same for all 12.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/WEIGHT4_FULL_AXIS_ONE_BIT_EXTRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/WEIGHT4_FULL_AXIS_ONE_BIT_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
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
AXES: tuple[tuple[int, int], ...] = ((0, 1), (2, 3), (4, 5))
AXIS_NAME = ("x", "y", "z")
SLOT_PLUS_Z = 4
SLOT_MINUS_Z = 5
EMPTY = 0
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the 15 weight-4 occupancy masks, whether occupancy '
    "names a unique full axis whose one-bit age extra kills Stab is "
    'reported. Displayed, not adopted."'
)
UNEQ_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
UNEQ_RADII = (2, 1, 3)
UNEQ_V: Point = (-3, -3, -1)
UNEQ_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
UNEQ_TICKS: Tick = (1, None, 1, None, 3, 2)
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Point, radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if abs(offset[0]) + abs(offset[1]) + abs(offset[2]) <= radius:
            sites.append(add(center, offset))
    return tuple(sites)


def in_union(point: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]) -> bool:
    return any(l1(point, seed) <= radius for seed, radius in zip(seeds, radii))


def sigma_ticks(
    site: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]
) -> tuple[Coloring, Tick]:
    occupied = {
        add(seed, offset)
        for seed, radius in zip(seeds, radii)
        for offset in ball((0, 0, 0), radius)
    }
    sigma_bits: list[int] = []
    ticks_bits: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            sigma_bits.append(1)
            ticks_bits.append(min(l1(neighbor, seed) for seed in seeds))
        else:
            sigma_bits.append(0)
            ticks_bits.append(None)
    return tuple(sigma_bits), tuple(ticks_bits)


def weight4_masks() -> tuple[Coloring, ...]:
    return tuple(
        bits
        for bits in itertools.product((0, 1), repeat=6)
        if sum(bits) == 4
    )


def empty_slots(sigma: Coloring) -> tuple[int, int]:
    emptied = tuple(index for index, bit in enumerate(sigma) if bit == 0)
    if len(emptied) != 2:
        raise AssertionError(f"expected two empty slots, got {emptied}")
    return (emptied[0], emptied[1])


def same_axis(left: int, right: int) -> bool:
    return any({left, right} == set(axis) for axis in AXES)


def full_axes(sigma: Coloring) -> tuple[int, ...]:
    return tuple(
        axis_index
        for axis_index, (plus, minus) in enumerate(AXES)
        if sigma[plus] == 1 and sigma[minus] == 1
    )


def unique_full_axis(sigma: Coloring) -> int | None:
    named = full_axes(sigma)
    if len(named) == 1:
        return named[0]
    return None


def bit_on_axis(ticks: Tick, axis_index: int) -> int:
    plus, minus = AXES[axis_index]
    minus_tick = ticks[minus]
    plus_tick = ticks[plus]
    if minus_tick is not None and plus_tick is not None and minus_tick < plus_tick:
        return 1
    return 0


def display_ticks(sigma: Coloring, axis_index: int) -> Tick:
    plus, minus = AXES[axis_index]
    ticks: list[int | None] = [None] * 6
    for slot, bit in enumerate(sigma):
        if bit == 0:
            continue
        if slot == minus:
            ticks[slot] = 1
        elif slot == plus:
            ticks[slot] = 2
        else:
            ticks[slot] = 0
    return tuple(ticks)


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


def stab_perms(sigma: Coloring, perms: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    return [perm for perm in perms if act_col(perm, sigma) == sigma]


def swaps_axis_ends(perm: tuple[int, ...], axis_index: int) -> bool:
    plus, minus = AXES[axis_index]
    return perm[plus] == minus and perm[minus] == plus


def july3_pair(perms: list[tuple[int, ...]]) -> frozenset[Coloring]:
    unseen = set(itertools.product(range(3), repeat=6))
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


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != EMPTY) for letter in coloring)


def n_pair_support(sigma: Coloring, pair: frozenset[Coloring]) -> int:
    return sum(1 for item in pair if support(item) == sigma)


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
    masks = weight4_masks()

    perp: list[Coloring] = []
    axis_masks: list[Coloring] = []
    named_ok = True
    bit_kills = True
    stab_orders_ok = True
    pair_axis_zero = True
    for sigma in masks:
        emptied = empty_slots(sigma)
        named = unique_full_axis(sigma)
        stab = stab_perms(sigma, perms)
        n_ps = n_pair_support(sigma, pair)
        if same_axis(*emptied):
            axis_masks.append(sigma)
            if named is not None or n_ps != 0 or len(stab) != 8:
                pair_axis_zero = False
        else:
            perp.append(sigma)
            if named is None or len(full_axes(sigma)) != 1:
                named_ok = False
                continue
            plus, minus = AXES[named]
            if len(stab) != 2:
                stab_orders_ok = False
            non_id = [perm for perm in stab if perm != tuple(range(6))]
            if len(non_id) != 1 or not swaps_axis_ends(non_id[0], named):
                bit_kills = False
            ticks = display_ticks(sigma, named)
            bit = bit_on_axis(ticks, named)
            n_stab_bit = 0
            for perm in stab:
                if bit_on_axis(act_col(perm, ticks), named) == bit:
                    n_stab_bit += 1
            if n_stab_bit != 1 or bit != 1:
                bit_kills = False

    uneq_unread = not in_union(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    uneq_sigma, uneq_ticks = sigma_ticks(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    uneq_named = unique_full_axis(uneq_sigma)
    uneq_bit = (
        bit_on_axis(uneq_ticks, uneq_named) if uneq_named is not None else None
    )
    uneq_stab = stab_perms(uneq_sigma, perms)
    n_uneq_bit = 0
    if uneq_named is not None:
        for perm in uneq_stab:
            if bit_on_axis(act_col(perm, uneq_ticks), uneq_named) == uneq_bit:
                n_uneq_bit += 1
    swap_perm = direction_perm(SWAPPER)
    swap_ticks = act_col(swap_perm, uneq_ticks)
    swap_bit = (
        bit_on_axis(swap_ticks, uneq_named) if uneq_named is not None else None
    )

    print("weight-4 occupancy unique full axis one-bit extra")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"N_masks={len(masks)}")
    print(f"N_perp={len(perp)}")
    print(f"N_axis={len(axis_masks)}")
    print(f"N_pair={len(pair)}")
    print(f"uneq_unread={uneq_unread}")
    print(f"uneq_sigma={uneq_sigma}")
    print(f"uneq_ticks={uneq_ticks}")
    print(f"uneq_full_axis={None if uneq_named is None else AXIS_NAME[uneq_named]}")
    print(f"uneq_b={uneq_bit}")
    print(f"|Stab(uneq)|={len(uneq_stab)}")
    print(f"|Stab(uneq,b)|={n_uneq_bit}")
    print(f"swapper_excluded={swap_bit != uneq_bit}")
    print("perp_rows:")
    for sigma in perp:
        named = unique_full_axis(sigma)
        axis = AXIS_NAME[named] if named is not None else None
        print(f"  {sigma} full={axis} |Stab|={len(stab_perms(sigma, perms))} Nps={n_pair_support(sigma, pair)}")
    print("axis_rows:")
    for sigma in axis_masks:
        print(f"  {sigma} |Stab|={len(stab_perms(sigma, perms))} Nps={n_pair_support(sigma, pair)}")

    expected_paths = (
        "docs/WEIGHT4_FULL_AXIS_ONE_BIT_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "theorem-1-split",
        len(masks) == 15
        and len(perp) == 12
        and len(axis_masks) == 3
        and "N_perp = 12" in note
        and "N_axis = 3" in note
        and "C(6,4) = 15" in note,
        f"N_perp={len(perp)} N_axis={len(axis_masks)}",
    )
    checks.check(
        "theorem-1-unique-full-axis",
        named_ok
        and all(unique_full_axis(sigma) is not None for sigma in perp)
        and all(unique_full_axis(sigma) is None for sigma in axis_masks)
        and "unique full axis" in note
        and "both ends occupied" in note,
    )
    checks.check(
        "theorem-1-axis-no-pair-support",
        pair_axis_zero
        and all(n_pair_support(sigma, pair) == 0 for sigma in axis_masks)
        and "10→no pair support" in note
        and "N_pair_support = 0" in note,
        f"N_pair={len(pair)}",
    )
    checks.check(
        "theorem-2-bit-kills-swapper",
        bit_kills
        and stab_orders_ok
        and "pattern is the same for all 12" in note
        and "which end is older" in note
        and "kills every occupancy stabilizer that swaps those two ends" in note,
    )
    checks.check(
        "theorem-2-uneqrad-mask",
        uneq_unread
        and uneq_sigma == UNEQ_SIGMA
        and uneq_ticks == UNEQ_TICKS
        and uneq_named == 2
        and uneq_bit == 1
        and len(uneq_stab) == 2
        and n_uneq_bit == 1
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "unique full axis is `z`" in note
        and "`b = 1`" in note
        and "|Stab(σ)| = 2" in note
        and "|Stab(σ,b)| = 1" in note,
        f"sigma={uneq_sigma} axis={uneq_named} b={uneq_bit}",
    )
    checks.check(
        "theorem-2-uneqrad-swapper",
        act_col(swap_perm, UNEQ_SIGMA) == UNEQ_SIGMA
        and swap_bit != uneq_bit
        and swap_bit == 0
        and swap_perm[4] == 5
        and "s : (x, y, z) ↦ (y, x, −z)" in note
        and "occupancy swapper is excluded" in note,
        f"swap_bit={swap_bit}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write the bit into Admissibility" in note
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
        "not-leftover-uneqbit",
        "not leftover of uneqbit" in note_flat
        and "one star" in note
        and "uneqbit #6680" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "Stab(σ,b)" not in axiom
        and "N_perp" not in axiom
        and "lock-tick" not in axiom
        and "unequal-radius" not in axiom,
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

    print("per_element: N_perp, N_axis, |Stab(σ)|, |Stab(σ,b)| are exact integers")
    print("per_site: 15 weight-4 occupancy masks; uneqrad mask named only")
    print("per_mode: no spectral calculation")
    print("per_block: 6-NN star masks only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
