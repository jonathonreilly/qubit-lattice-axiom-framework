#!/usr/bin/env python3
"""Displayed L1 neighbor data versus t on the uneqrad lex-first star.

U, v, t are the uneqrad lex-first breaker. Occupied slots carry
t=(1,1,3,2) on (+x,+y,+z,-z). Occupancy bits, n from each neighbor
six-star, Bloch from occupancy, k, and the formation-count of U are
compared with that 4-tuple. None equals t, so t is not a theorem of
displayed L1 on this star. Displayed, not adopted.
No cache is written.
"""

from __future__ import annotations

import ast
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_TICK_NOT_L1_NEIGHBOR_DATUM_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_TICK_NOT_L1_NEIGHBOR_DATUM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
Vec3 = tuple[int, int, int]
Frac3 = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXES: tuple[Point, ...] = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On the lex-first unequal-radius breaker, '
    "whether displayed L1 neighbor data equals the lock-tick 4-tuple "
    'is reported. Displayed, not adopted."'
)
SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
RADII = (2, 1, 3)
V: Point = (-3, -3, -1)
EXPECTED_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_TICKS: Tick = (1, None, 1, None, 3, 2)
EXPECTED_T_OCC: tuple[int, ...] = (1, 1, 3, 2)
EXPECTED_SIGMA_OCC: tuple[int, ...] = (1, 1, 1, 1)
EXPECTED_K_OCC: tuple[int, ...] = (3, 3, 3, 2)
EXPECTED_N_DIPOLE: tuple[Vec3, ...] = (
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (1, 1, 0),
)
EXPECTED_N_FRAC: tuple[Frac3, ...] = (
    ((0, 1), (1, 3), (0, 1)),
    ((1, 3), (0, 1), (0, 1)),
    ((1, 3), (1, 3), (1, 3)),
    ((1, 3), (1, 3), (0, 1)),
)
EXPECTED_FORMATION_COUNT = 81
I2_OVER_2_BLOCH = (0, 0, 0)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


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


def occupied_tuple(values: tuple[object, ...], sigma: Coloring) -> tuple[object, ...]:
    return tuple(value for bit, value in zip(sigma, values) if bit == 1)


def six_star_occupancy(
    site: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]
) -> Coloring:
    return tuple(int(in_union(add(site, direction), seeds, radii)) for direction in DIRS)


def dipole(star: Coloring) -> Vec3:
    return (
        star[0] - star[1],
        star[2] - star[3],
        star[4] - star[5],
    )


def n_from_dipole(dip: Vec3) -> Frac3:
    return tuple((component, 3) if component != 0 else (0, 1) for component in dip)


def formation_count(seeds: tuple[Point, ...], radii: tuple[int, ...]) -> int:
    seen: set[Point] = set()
    for seed, radius in zip(seeds, radii):
        span = range(-radius, radius + 1)
        for dx in span:
            for dy in span:
                for dz in span:
                    point = add(seed, (dx, dy, dz))
                    if l1(point, seed) <= radius:
                        seen.add(point)
    return len(seen)


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

    sigma, ticks = occupancy_ticks(SEEDS, RADII, V)
    unread = not in_union(V, SEEDS, RADII)
    occupied_sites = tuple(
        add(V, DIRS[index]) for index, bit in enumerate(sigma) if bit == 1
    )
    t_occ = tuple(clock for clock in occupied_tuple(ticks, sigma))
    sigma_occ = tuple(1 for _ in occupied_sites)
    stars = tuple(six_star_occupancy(site, SEEDS, RADII) for site in occupied_sites)
    k_occ = tuple(sum(star) for star in stars)
    dipoles = tuple(dipole(star) for star in stars)
    n_frac = tuple(n_from_dipole(dip) for dip in dipoles)
    bloch_i2 = tuple(I2_OVER_2_BLOCH for _ in occupied_sites)
    bloch_occ_map = sigma_occ
    union_count = formation_count(SEEDS, RADII)
    n_equals_t = n_frac == t_occ
    lists_equal_t = any(
        candidate == t_occ
        for candidate in (sigma_occ, k_occ, bloch_occ_map, bloch_i2, union_count)
    ) or n_equals_t
    t_is_displayed_l1_theorem = lists_equal_t

    print("unequal-radius tick not L1 neighbor datum")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"seeds={SEEDS}")
    print(f"radii={RADII}")
    print(f"v={V}")
    print(f"unread={unread}")
    print(f"sigma={sigma}")
    print(f"ticks={ticks}")
    print(f"occupied_sites={occupied_sites}")
    print(f"t_occ={t_occ}")
    print(f"sigma_occ={sigma_occ}")
    print(f"n_dipole={dipoles}")
    print(f"n_frac={n_frac}")
    print(f"k_occ={k_occ}")
    print(f"bloch_I2_over_2={bloch_i2}")
    print(f"bloch_occupancy_map={bloch_occ_map}")
    print(f"formation_count={union_count}")
    print(f"any_displayed_list_equals_t={lists_equal_t}")
    print(f"t_is_theorem_of_displayed_L1={t_is_displayed_l1_theorem}")

    expected_paths = (
        "docs/UNEQUAL_RADIUS_TICK_NOT_L1_NEIGHBOR_DATUM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content"
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
        "source-record-qubit",
        record_lock in axiom
        and record_lock in note
        and record_content in axiom
        and record_content in note
        and unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )
    checks.check(
        "host-lex-first-breaker",
        unread
        and sigma == EXPECTED_SIGMA
        and ticks == EXPECTED_TICKS
        and occupied_sites
        == ((-2, -3, -1), (-3, -2, -1), (-3, -3, 0), (-3, -3, -2))
        and len(set(RADII)) > 1
        and "`v = (−3,−3,−1)`" in note
        and "radii `(2, 1, 3)`" in note
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note
        and "`t_occ = (1, 1, 3, 2)`" in note,
        f"sigma={sigma} ticks={ticks}",
    )
    checks.check(
        "theorem-1-t-not-occupancy-bits",
        t_occ == EXPECTED_T_OCC
        and sigma_occ == EXPECTED_SIGMA_OCC
        and sigma_occ != t_occ
        and "`σ_occ = (1, 1, 1, 1)`" in note
        and "occupancy bits (all 1)" in note,
        f"sigma_occ={sigma_occ}",
    )
    checks.check(
        "theorem-1-t-not-n-from-six-star",
        dipoles == EXPECTED_N_DIPOLE
        and n_frac == EXPECTED_N_FRAC
        and n_frac != t_occ
        and not n_equals_t
        and "`n_occ = ((0, 1/3, 0), (1/3, 0, 0), (1/3, 1/3, 1/3), (1/3, 1/3, 0))`"
        in note
        and "n_μ from the six-star of each neighbor" in note_flat.replace("`", ""),
        f"n_dipole={dipoles}",
    )
    checks.check(
        "theorem-1-t-not-bloch-from-occupancy",
        bloch_i2 == (I2_OVER_2_BLOCH,) * 4
        and bloch_occ_map == EXPECTED_SIGMA_OCC
        and bloch_i2 != t_occ
        and bloch_occ_map != t_occ
        and "Bloch `I_2/2`" in note
        and "occupancy map `(1, 1, 1, 1)`" in note,
        f"bloch_i2={bloch_i2} bloch_occ_map={bloch_occ_map}",
    )
    checks.check(
        "theorem-1-t-not-k",
        k_occ == EXPECTED_K_OCC
        and k_occ != t_occ
        and "`k_occ = (3, 3, 3, 2)`" in note,
        f"k_occ={k_occ}",
    )
    checks.check(
        "theorem-1-t-not-formation-count",
        union_count == EXPECTED_FORMATION_COUNT
        and union_count != t_occ
        and not isinstance(union_count, tuple)
        and "`|U| = 81`" in note
        and "Formation-count of `U` is one integer" in note,
        f"formation_count={union_count}",
    )
    checks.check(
        "theorem-1-t-not-equal-any-four-site-l1-list",
        not lists_equal_t
        and "t` is not equal to any of those four-site L1 lists" in note,
    )
    checks.check(
        "theorem-2-not-theorem-of-displayed-l1",
        t_is_displayed_l1_theorem is False
        and "Therefore `t` is not a theorem of displayed L1 on this" in note
        and "not a theorem of displayed L1" in note_flat,
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write `t` into L1 or Admissibility" in note
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
        "not-leftover-uneqrec",
        "not leftover of uneqrec" in note_flat
        and "one `M_2` lock" in note
        and "uneqrec" in note,
    )
    checks.check(
        "admissibility-record-unedited",
        covariance_clause in axiom_flat
        and record_lock in axiom
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

    print(
        "per_element: scored occupancy bits, n, Bloch from occupancy, "
        "k, and formation-count against t_occ"
    )
    print("per_site: scored only the uneqrad lex-first star at v")
    print("per_mode: no spectral calculation; displayed L1 lists only")
    print("per_block: 3-ball unequal-radius host only; no fourth ball")
    print(
        "lattice_wide: checked and not executed — one finite 6-star, "
        "not a lattice-wide rule"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
