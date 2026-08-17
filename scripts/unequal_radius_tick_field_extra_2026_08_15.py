#!/usr/bin/env python3
"""Unequal-radius lock-tick field versus 6-NN occupancy.

U_uneq, v are the uneqrad lex-first breaker (mixed t). Same-center
equal-r occupies that v, so the equal-radius control is the ticklab
star. Score those two hosts and the lex-first same-σ uneqrad star.
σ does not determine t: the tick field (or the three radii) is a
displayed extra relative to NN occupancy. Displayed, not adopted.
No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from array import array
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_TICK_FIELD_EXTRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_TICK_FIELD_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
EMPTY = 0
SHIFT = 5
STRIDE = 11
GRID = STRIDE * STRIDE * STRIDE
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "Whether the unequal-radius lock-tick field is determined '
    "by 6-NN occupancy, or is an extra, is reported. "
    'Displayed, not adopted."'
)
UNEQ_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
UNEQ_RADII = (2, 1, 3)
UNEQ_V: Point = (-3, -3, -1)
EXPECTED_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_TICKS: Tick = (1, None, 1, None, 3, 2)
FIRST_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 0),
)
FIRST_RADII = (2, 1, 2)
FIRST_TICKS: Tick = (1, None, 1, None, 2, 2)
EQ_SEEDS: tuple[Point, Point, Point] = (
    (0, 0, 0),
    (2, 0, 0),
    (1, 2, 1),
)
EQ_RADII = (2, 2, 2)
EQ_V: Point = (-1, 1, 1)
EQ_SIGMA: Coloring = (1, 0, 1, 1, 0, 1)
EQ_TICKS: Tick = (2, None, 2, 2, None, 2)
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


def enc(point: Point) -> int:
    return (point[0] + SHIFT) + STRIDE * (
        (point[1] + SHIFT) + STRIDE * (point[2] + SHIFT)
    )


def in_union(point: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]) -> bool:
    return any(l1(point, seed) <= radius for seed, radius in zip(seeds, radii))


def sigma_ticks(
    site: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]
) -> tuple[Coloring, Tick]:
    sigma_bits: list[int] = []
    ticks_bits: list[int | None] = []
    occupied = {add(seed, offset) for seed, radius in zip(seeds, radii) for offset in ball((0, 0, 0), radius)}
    for direction in DIRS:
        neighbor = add(site, direction)
        if neighbor in occupied:
            sigma_bits.append(1)
            ticks_bits.append(min(l1(neighbor, seed) for seed in seeds))
        else:
            sigma_bits.append(0)
            ticks_bits.append(None)
    return tuple(sigma_bits), tuple(ticks_bits)


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


def stab_orders(
    sigma: Coloring, ticks: Tick, perms: list[tuple[int, ...]]
) -> tuple[int, int]:
    n_stab = 0
    n_stab_tick = 0
    for perm in perms:
        if act_col(perm, sigma) == sigma:
            n_stab += 1
            if act_col(perm, ticks) == ticks:
                n_stab_tick += 1
    return n_stab, n_stab_tick


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


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


def first_star_and_breaker(perms: list[tuple[int, ...]]) -> dict:
    seed_box = tuple(itertools.product(range(-2, 3), repeat=3))
    v_box = tuple(itertools.product(range(-4, 5), repeat=3))
    radii_opts = tuple(
        radii
        for radii in itertools.product((1, 2, 3), repeat=3)
        if not (radii[0] == radii[1] == radii[2])
    )
    ball_enc = {
        (seed, radius): tuple(enc(site) for site in ball(seed, radius))
        for seed in seed_box
        for radius in (1, 2, 3)
    }
    v_enc = tuple(enc(site) for site in v_box)
    neighbor_enc = tuple(
        tuple(enc(add(site, direction)) for direction in DIRS) for site in v_box
    )
    neighbor_pts = tuple(
        tuple(add(site, direction) for direction in DIRS) for site in v_box
    )
    mark = array("I", [0]) * GRID
    generation = 0
    first_star: tuple | None = None
    first_sigma: Coloring | None = None
    first_ticks: Tick | None = None
    first_breaker: tuple | None = None
    first_breaker_detail: tuple | None = None

    for s1, s2, s3 in itertools.combinations(seed_box, 3):
        seeds = (s1, s2, s3)
        for radii in radii_opts:
            generation += 1
            for seed, radius in zip(seeds, radii):
                for index in ball_enc[(seed, radius)]:
                    mark[index] = generation
            for v_index, site in enumerate(v_box):
                if mark[v_enc[v_index]] == generation:
                    continue
                sigma_bits: list[int] = []
                ticks_bits: list[int | None] = []
                occupied_ticks: list[int] = []
                for slot, w_enc in enumerate(neighbor_enc[v_index]):
                    if mark[w_enc] == generation:
                        sigma_bits.append(1)
                        tick = min(
                            l1(neighbor_pts[v_index][slot], seed) for seed in seeds
                        )
                        ticks_bits.append(tick)
                        occupied_ticks.append(tick)
                    else:
                        sigma_bits.append(0)
                        ticks_bits.append(None)
                if len(occupied_ticks) != 4:
                    continue
                sigma = tuple(sigma_bits)
                ticks = tuple(ticks_bits)
                if first_star is None:
                    first_star = (seeds, radii, site)
                    first_sigma = sigma
                    first_ticks = ticks
                n_stab, n_stab_tick = stab_orders(sigma, ticks, perms)
                if n_stab_tick < n_stab and first_breaker is None:
                    first_breaker = (seeds, radii, site)
                    first_breaker_detail = (sigma, ticks, n_stab, n_stab_tick)
                    break
            else:
                continue
            break
        else:
            continue
        break

    return {
        "first_star": first_star,
        "first_sigma": first_sigma,
        "first_ticks": first_ticks,
        "first_breaker": first_breaker,
        "first_breaker_detail": first_breaker_detail,
    }


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

    uneq_unread = not in_union(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    uneq_sigma, uneq_ticks = sigma_ticks(UNEQ_V, UNEQ_SEEDS, UNEQ_RADII)
    same_eq_unread = not in_union(UNEQ_V, UNEQ_SEEDS, (2, 2, 2))
    same_eq_sigma, same_eq_ticks = sigma_ticks(UNEQ_V, UNEQ_SEEDS, (2, 2, 2))
    eq_unread = not in_union(EQ_V, EQ_SEEDS, EQ_RADII)
    eq_sigma, eq_ticks = sigma_ticks(EQ_V, EQ_SEEDS, EQ_RADII)
    first_direct_sigma, first_direct_ticks = sigma_ticks(
        UNEQ_V, FIRST_SEEDS, FIRST_RADII
    )
    perms = [direction_perm(matrix) for matrix in rotations]
    census = first_star_and_breaker(perms)
    breaker_detail = census["first_breaker_detail"]
    n_stab = breaker_detail[2] if breaker_detail is not None else 0
    n_stab_tick = breaker_detail[3] if breaker_detail is not None else 0

    print("unequal-radius tick field extra relative to NN occupancy")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"uneq_unread={uneq_unread}")
    print(f"uneq_sigma={uneq_sigma}")
    print(f"uneq_ticks={uneq_ticks}")
    print(f"same_center_eq_unread={same_eq_unread}")
    print(f"same_center_eq_sigma={same_eq_sigma}")
    print(f"same_center_eq_ticks={same_eq_ticks}")
    print("equal_radius_control=ticklab")
    print(f"eq_unread={eq_unread}")
    print(f"eq_sigma={eq_sigma}")
    print(f"eq_ticks={eq_ticks}")
    print(f"first_star={census['first_star']}")
    print(f"first_sigma={census['first_sigma']}")
    print(f"first_ticks={census['first_ticks']}")
    print(f"first_breaker={census['first_breaker']}")
    print(f"first_breaker_detail={census['first_breaker_detail']}")
    print(f"sigma_same={uneq_sigma == census['first_sigma']}")
    print(f"ticks_differ={uneq_ticks != census['first_ticks']}")

    expected_paths = (
        "docs/UNEQUAL_RADIUS_TICK_FIELD_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "theorem-1-lex-first-breaker",
        uneq_unread
        and uneq_sigma == EXPECTED_SIGMA
        and uneq_ticks == EXPECTED_TICKS
        and census["first_breaker"] == (UNEQ_SEEDS, UNEQ_RADII, UNEQ_V)
        and breaker_detail == (EXPECTED_SIGMA, EXPECTED_TICKS, 2, 1)
        and n_stab == 2
        and n_stab_tick == 1
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "radii `(2, 1, 3)`" in note
        and "`v = (−3,−3,−1)`" in note,
        f"sigma={uneq_sigma} ticks={uneq_ticks}",
    )
    checks.check(
        "theorem-1-same-center-eq-occupies-v",
        same_eq_unread is False
        and l1(UNEQ_V, UNEQ_SEEDS[1]) == 2
        and "v ∈ U_same" in note
        and "this `v` is not unread" in note,
        f"same_center_eq_unread={same_eq_unread}",
    )
    checks.check(
        "theorem-1-equal-radius-control",
        eq_unread
        and eq_sigma == EQ_SIGMA
        and eq_ticks == EQ_TICKS
        and set(tick for tick in eq_ticks if tick is not None) == {2}
        and "equal-radius control" in note
        and "`t_eq = (2, ·, 2, 2, ·, 2)`" in note
        and "`σ_eq = (1, 0, 1, 1, 0, 1)`" in note
        and "ticklab" in note,
        f"eq_sigma={eq_sigma} eq_ticks={eq_ticks}",
    )
    checks.check(
        "theorem-1-sigma-does-not-determine-t",
        census["first_star"] == (FIRST_SEEDS, FIRST_RADII, UNEQ_V)
        and census["first_sigma"] == EXPECTED_SIGMA
        and census["first_ticks"] == FIRST_TICKS
        and first_direct_sigma == EXPECTED_SIGMA
        and first_direct_ticks == FIRST_TICKS
        and uneq_sigma == census["first_sigma"]
        and uneq_ticks != census["first_ticks"]
        and "`t = (1, ·, 1, ·, 2, 2)`" in note
        and "does not determine" in note_flat,
        f"first_ticks={census['first_ticks']} uneq_ticks={uneq_ticks}",
    )
    checks.check(
        "theorem-2-extra-not-adopted",
        "newly named extra" in note
        and "relative to NN occupancy" in note
        and "NN-determined" in note
        and "Do not adopt the extra" in note
        and "Admissibility still requires" in note,
    )
    checks.check(
        "theorem-3-displayed",
        "Displayed, not adopted" in note
        and "Do not write radii or t into Admissibility" in note
        and "Do not write radii into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-uneqlaw",
        "not leftover of uneqlaw" in note_flat
        and "orbit count" in note
        and "N_commute = 24" in note
        and "N_fire = 4" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "lock-tick" not in axiom
        and "unequal-radius" not in axiom
        and "tick field" not in axiom,
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

    print("per_element: σ and t are exact 6-slot tuples; same-σ different-t is exact")
    print("per_site: lex-first breaker, lex-first same-σ star, and one equal-radius control")
    print("per_mode: no spectral calculation")
    print("per_block: 3-ball stars only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
