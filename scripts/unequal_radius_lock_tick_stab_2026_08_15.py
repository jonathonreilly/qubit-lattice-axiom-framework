#!/usr/bin/env python3
"""Unequal-radius 3-ball lock-ticks versus occupancy Stab.

U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3) with distinct centers in
[-2,2]^3, radii in {1,2,3} not all equal. Score unread v with
||v||_∞ ≤ 4 and wt(σ)=4. t(w) = min_i ||w − si||_1 on occupied
nearest neighbors. Report the lex-first star with
|Stab(σ,t)| < |Stab(σ)|, the 2000-star prefix counts, and N_tick_ok
on that breaker. Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from array import array
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_LOCK_TICK_STAB_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_LOCK_TICK_STAB_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
PREFIX = 2000
SHIFT = 5
STRIDE = 11
GRID = STRIDE * STRIDE * STRIDE
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "Among unequal-radius 3-ball unions with radii in {1,2,3}, '
    "whether lock-ticks shrink Stab at an unread weight-4 star is reported. "
    'Displayed, not adopted."'
)
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))
EXPECTED_BREAKER_SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
EXPECTED_BREAKER_RADII = (2, 1, 3)
EXPECTED_BREAKER_V: Point = (-3, -3, -1)
EXPECTED_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_TICKS: Tick = (1, None, 1, None, 3, 2)


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


def support(coloring: Coloring) -> Coloring:
    return tuple(int(letter != EMPTY) for letter in coloring)


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


def n_tick_ok(
    sigma: Coloring,
    ticks: Tick,
    perms: list[tuple[int, ...]],
    pair: frozenset[Coloring],
) -> tuple[int, int, tuple[Coloring, ...]]:
    stab_tick_perms = [
        perm
        for perm in perms
        if act_col(perm, sigma) == sigma and act_col(perm, ticks) == ticks
    ]
    members = tuple(sorted(item for item in pair if support(item) == sigma))
    ok = tuple(
        item
        for item in members
        if all(act_col(perm, item) == item for perm in stab_tick_perms)
    )
    return len(members), len(ok), members


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


def census(perms: list[tuple[int, ...]]) -> dict:
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
    n_wt4 = 0
    n_prefix = 0
    n_uneq_prefix = 0
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
            for v_index, v in enumerate(v_box):
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
                n_wt4 += 1
                if first_star is None:
                    first_star = (seeds, radii, v)
                    first_sigma = sigma
                    first_ticks = ticks
                unequal = not (
                    occupied_ticks[0]
                    == occupied_ticks[1]
                    == occupied_ticks[2]
                    == occupied_ticks[3]
                )
                is_breaker = False
                if unequal:
                    n_stab, n_stab_tick = stab_orders(sigma, ticks, perms)
                    if n_stab_tick < n_stab:
                        is_breaker = True
                        if first_breaker is None:
                            first_breaker = (seeds, radii, v)
                            first_breaker_detail = (
                                sigma,
                                ticks,
                                n_stab,
                                n_stab_tick,
                            )
                if n_wt4 <= PREFIX:
                    n_prefix = n_wt4
                    if is_breaker:
                        n_uneq_prefix += 1
                elif first_breaker is not None:
                    break
            else:
                continue
            break
        else:
            continue
        break

    return {
        "n_wt4": n_wt4,
        "n_prefix": n_prefix,
        "n_uneq_prefix": n_uneq_prefix,
        "first_star": first_star,
        "first_sigma": first_sigma,
        "first_ticks": first_ticks,
        "first_breaker": first_breaker,
        "first_breaker_detail": first_breaker_detail,
        "exists": first_breaker is not None,
        "seed_count": len(seed_box),
        "v_count": len(v_box),
        "radii_count": len(radii_opts),
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
    perms = [direction_perm(matrix) for matrix in rotations]
    data = census(perms)
    pair = july3_pair(perms)
    breaker = data["first_breaker"]
    detail = data["first_breaker_detail"]
    n_pair_support = 0
    n_ok = 0
    members: tuple[Coloring, ...] = ()
    if breaker is not None and detail is not None:
        sigma, ticks, _n_stab, _n_stab_tick = detail
        n_pair_support, n_ok, members = n_tick_ok(sigma, ticks, perms, pair)

    print("unequal-radius lock-tick occupancy Stab")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"seed_box_card={data['seed_count']}")
    print(f"v_box_card={data['v_count']}")
    print(f"radii_card={data['radii_count']}")
    print(f"G_plus={len(rotations)}")
    print(f"N_prefix={data['n_prefix']}")
    print(f"N_uneq_prefix={data['n_uneq_prefix']}")
    print(f"exists_breaker={data['exists']}")
    print(f"first_star={data['first_star']}")
    print(f"first_sigma={data['first_sigma']}")
    print(f"first_ticks={data['first_ticks']}")
    print(f"first_breaker={data['first_breaker']}")
    print(f"first_breaker_detail={data['first_breaker_detail']}")
    print(f"N_pair={len(pair)}")
    print(f"N_pair_support={n_pair_support}")
    print(f"N_tick_ok={n_ok}")
    print("support_members=" + ",".join(str(item) for item in members))

    expected_paths = (
        "docs/UNEQUAL_RADIUS_LOCK_TICK_STAB_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "theorem-1-prefix",
        data["n_prefix"] == PREFIX
        and data["n_uneq_prefix"] == 1413
        and "N_prefix = 2000" in note
        and "N_uneq_prefix = 1413" in note,
        f"N_prefix={data['n_prefix']} N_uneq_prefix={data['n_uneq_prefix']}",
    )
    checks.check(
        "theorem-1-existence",
        data["exists"] is True
        and data["first_breaker"]
        == (EXPECTED_BREAKER_SEEDS, EXPECTED_BREAKER_RADII, EXPECTED_BREAKER_V)
        and detail
        == (EXPECTED_SIGMA, EXPECTED_TICKS, 2, 1)
        and "|Stab(σ)| = 2" in note
        and "|Stab(σ,t)| = 1" in note
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "radii `(2, 1, 3)`" in note,
        f"breaker={data['first_breaker']} detail={detail}",
    )
    swap_perm = direction_perm(SWAPPER)
    checks.check(
        "theorem-1-swapper-breaks-ticks",
        act_col(swap_perm, EXPECTED_SIGMA) == EXPECTED_SIGMA
        and act_col(swap_perm, EXPECTED_TICKS) != EXPECTED_TICKS
        and swap_perm[0] == 2
        and swap_perm[4] == 5
        and "s : (x, y, z) ↦ (y, x, −z)" in note,
    )
    checks.check(
        "theorem-2-tick-ok",
        n_ok == 4
        and n_pair_support == 4
        and members
        == (
            (1, 0, 2, 0, 1, 2),
            (1, 0, 2, 0, 2, 1),
            (2, 0, 1, 0, 1, 2),
            (2, 0, 1, 0, 2, 1),
        )
        and "N_tick_ok = 4" in note
        and "N_pair_support = 4" in note,
        f"N_tick_ok={n_ok} N_pair_support={n_pair_support}",
    )
    checks.check(
        "unequal-radii-not-all-equal",
        len(set(EXPECTED_BREAKER_RADII)) > 1
        and data["radii_count"] == 24
        and (1, 1, 1) not in {
            radii
            for radii in itertools.product((1, 2, 3), repeat=3)
            if not (radii[0] == radii[1] == radii[2])
        }
        and "not all equal" in note_flat,
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write radii into Admissibility" in note
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
        "not-leftover-tickhost",
        "not leftover of tickhost" in note_flat
        and "equal r=2" in note
        and "equal-radius" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "Stab(σ,t)" not in axiom
        and "N_tick_ok" not in axiom
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

    print("per_element: |Stab(σ)|, |Stab(σ,t)|, N_prefix, N_uneq_prefix, N_tick_ok are exact integers")
    print("per_site: unread weight-4 unequal-radius 3-ball stars in the declared box")
    print("per_mode: no spectral calculation")
    print("per_block: 3-ball stars only")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
