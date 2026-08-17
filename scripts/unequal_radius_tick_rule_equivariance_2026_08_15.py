#!/usr/bin/env python3
"""Unequal-radius tick-ok pair-member cube-equivariance on one orbit.

U, v are the uneqrad lex-first breaker. c is the lex-first Stab(σ,t)-ok
July-3 pair member. G+ acts on seeds, radii (travel with seeds), v, and
slots. N_commute counts the proper cube rotations that send this host to
a weight-4 unread star whose Stab(σ_g, t_g)-ok set contains g·c.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_TICK_RULE_EQUIVARIANCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_TICK_RULE_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the G+ orbit of the lex-first unequal-radius breaker, '
    "whether a tick-ok pair member is cube-equivariant is reported. "
    'Displayed, not adopted."'
)
SWAPPER: Matrix = ((0, 1, 0), (1, 0, 0), (0, 0, -1))
SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
RADII = (2, 1, 3)
V: Point = (-3, -3, -1)
EXPECTED_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_TICKS: Tick = (1, None, 1, None, 3, 2)
EXPECTED_C: Coloring = (1, 0, 2, 0, 1, 2)
EXPECTED_MEMBERS: tuple[Coloring, ...] = (
    (1, 0, 2, 0, 1, 2),
    (1, 0, 2, 0, 2, 1),
    (2, 0, 1, 0, 1, 2),
    (2, 0, 1, 0, 2, 1),
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


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


def in_union(point: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]) -> bool:
    return any(l1(point, seed) <= radius for seed, radius in zip(seeds, radii))


def occupancy_ticks(
    seeds: tuple[Point, ...], radii: tuple[int, ...], site: Point
) -> tuple[Coloring, Tick]:
    sigma: list[int] = []
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if in_union(neighbor, seeds, radii):
            sigma.append(1)
            ticks.append(min(l1(neighbor, seed) for seed in seeds))
        else:
            sigma.append(0)
            ticks.append(None)
    return tuple(sigma), tuple(ticks)


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


def tick_ok(
    sigma: Coloring,
    ticks: Tick,
    perms: list[tuple[int, ...]],
    pair: frozenset[Coloring],
) -> tuple[Coloring, ...]:
    stab_tick_perms = [
        perm
        for perm in perms
        if act_col(perm, sigma) == sigma and act_col(perm, ticks) == ticks
    ]
    members = tuple(sorted(item for item in pair if support(item) == sigma))
    return tuple(
        item
        for item in members
        if all(act_col(perm, item) == item for perm in stab_tick_perms)
    )


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


def score_orbit(
    rotations: tuple[Matrix, ...],
    perms: list[tuple[int, ...]],
    pair: frozenset[Coloring],
    coloring: Coloring,
) -> dict:
    n_unread = 0
    n_weight4 = 0
    n_breaker = 0
    n_commute = 0
    n_box = 0
    images: list[tuple] = []
    for matrix, perm in zip(rotations, perms):
        seeds = tuple(mat_vec(matrix, seed) for seed in SEEDS)
        site = mat_vec(matrix, V)
        unread = not in_union(site, seeds, RADII)
        sigma, ticks = occupancy_ticks(seeds, RADII, site)
        n_stab, n_stab_tick = stab_orders(sigma, ticks, perms)
        ok = tick_ok(sigma, ticks, perms, pair)
        rotated = act_col(perm, coloring)
        weight4 = sum(sigma) == 4
        breaker = unread and weight4 and n_stab_tick < n_stab
        inbox = all(all(abs(coord) <= 2 for coord in seed) for seed in seeds) and all(
            abs(coord) <= 4 for coord in site
        )
        commute = unread and weight4 and rotated in ok
        n_unread += int(unread)
        n_weight4 += int(weight4)
        n_breaker += int(breaker)
        n_commute += int(commute)
        n_box += int(inbox)
        images.append((site, sigma, ticks, n_stab, n_stab_tick, rotated, commute))
    return {
        "n_unread": n_unread,
        "n_weight4": n_weight4,
        "n_breaker": n_breaker,
        "n_commute": n_commute,
        "n_box": n_box,
        "images": images,
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
    pair = july3_pair(perms)
    sigma, ticks = occupancy_ticks(SEEDS, RADII, V)
    n_stab, n_stab_tick = stab_orders(sigma, ticks, perms)
    ok = tick_ok(sigma, ticks, perms, pair)
    coloring = ok[0] if ok else None
    orbit = score_orbit(rotations, perms, pair, coloring) if coloring is not None else {
        "n_unread": 0,
        "n_weight4": 0,
        "n_breaker": 0,
        "n_commute": 0,
        "n_box": 0,
        "images": [],
    }
    n_commute = orbit["n_commute"]

    print("unequal-radius tick-rule cube-equivariance")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"G_plus={len(rotations)}")
    print(f"seeds={SEEDS}")
    print(f"radii={RADII}")
    print(f"v={V}")
    print(f"sigma={sigma}")
    print(f"ticks={ticks}")
    print(f"stab_sigma={n_stab}")
    print(f"stab_sigma_t={n_stab_tick}")
    print(f"N_tick_ok={len(ok)}")
    print(f"lex_first_c={coloring}")
    print(f"N_unread={orbit['n_unread']}")
    print(f"N_weight4={orbit['n_weight4']}")
    print(f"N_breaker={orbit['n_breaker']}")
    print(f"N_box={orbit['n_box']}")
    print(f"N_commute={n_commute}")
    print(f"N_commute_over_24={n_commute}/24")
    print(f"N_commute_eq_24={n_commute == 24}")

    expected_paths = (
        "docs/UNEQUAL_RADIUS_TICK_RULE_EQUIVARIANCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "host-lex-first-breaker",
        sigma == EXPECTED_SIGMA
        and ticks == EXPECTED_TICKS
        and n_stab == 2
        and n_stab_tick == 1
        and not in_union(V, SEEDS, RADII)
        and len(set(RADII)) > 1
        and "`v = (−3,−3,−1)`" in note
        and "radii `(2, 1, 3)`" in note
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "|Stab(σ,t)| = 1" in note,
        f"sigma={sigma} ticks={ticks} stab=({n_stab},{n_stab_tick})",
    )
    checks.check(
        "lex-first-tick-ok",
        ok == EXPECTED_MEMBERS
        and coloring == EXPECTED_C
        and "N_tick_ok = 4" in note
        and "`c = (1, 0, 2, 0, 1, 2)`" in note,
        f"c={coloring} N_tick_ok={len(ok)}",
    )
    checks.check(
        "theorem-1-n-commute",
        n_commute == 24
        and orbit["n_unread"] == 24
        and orbit["n_weight4"] == 24
        and orbit["n_breaker"] == 24
        and orbit["n_box"] == 24
        and "N_commute = 24" in note
        and "N_commute / 24 = 24/24" in note,
        f"N_commute={n_commute}",
    )
    checks.check(
        "theorem-2-commute-is-24",
        n_commute == 24
        and "N_commute = 24" in note
        and "Whether N_commute = 24" in note
        and "N_commute = 24 holds" in note,
        f"eq24={n_commute == 24}",
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
        "not-leftover-uneqrad-deleq",
        "not leftover of uneqrad" in note_flat
        and "one star" in note
        and "deleq" in note
        and "different map" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_commute" not in axiom
        and "unequal-radius" not in axiom
        and "tick-ok" not in axiom,
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

    print(
        "per_element: N_commute is the exact count of the 24 proper cube "
        "rotations whose image is a weight-4 unread star containing g·c"
    )
    print(
        "per_site: scored only the G+ orbit of the uneqrad lex-first "
        "unequal-radius breaker at v"
    )
    print("per_mode: no spectral calculation; occupancy and lock-ticks only")
    print("per_block: 3-ball unequal-radius host orbit only; no fourth ball")
    print(
        "lattice_wide: checked and not executed — one finite G+ orbit, "
        "not a lattice-wide rule"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
