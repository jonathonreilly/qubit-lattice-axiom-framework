#!/usr/bin/env python3
"""Name the first remaining-bit refuse of the lex-first Q10-false map.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. The Q10-false maps are the remaining-bit tuples with
adj2=vertex3=mixed3=0; they are exactly the four maps with cov10=0. This
runner names the lex-first such map f_z = (0,0,0,0,0), the lex-first
10-site seed that f1 fills, and the first remaining-bit refuse of f_z
from that seed, together with N_refuse on that first tick. The refuse is
displayed, not adopted. f_L1 is the unbalanced-axis predicate
(some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_Q10_FALSE_TEN_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_Q10_FALSE_TEN_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Remaining = tuple[int, int, int, int, int]

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
EMPTY: Config = (0, 0, 0, 0, 0, 0)
FULL: Config = (1, 1, 1, 1, 1, 1)
TWO_CUBE: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
TEN_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(combo) for combo in combinations(TWO_CUBE, 10)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: Remaining = (1, 0, 1, 1, 1)
F1_REMAINING: Remaining = (1, 1, 1, 1, 1)
F_Z: Remaining = (0, 0, 0, 0, 0)
Q10_FALSE: tuple[Remaining, ...] = (
    (0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
)


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Direction) -> Direction:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def rotate_config(config: Config, rotation: Rotation) -> Config:
    occupancy = {direction: config[index] for index, direction in enumerate(DIRECTIONS)}
    forward = {direction: rotate_vector(rotation, direction) for direction in DIRECTIONS}
    inverse = {image: source for source, image in forward.items()}
    return tuple(occupancy[inverse[direction]] for direction in DIRECTIONS)  # type: ignore[return-value]


def axis_type(config: Config) -> OrbitType:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for axis in range(3):
        plus = config[2 * axis]
        minus = config[2 * axis + 1]
        if plus != minus:
            n_unbalanced += 1
        elif plus == 1:
            n_both += 1
        else:
            n_empty += 1
    return (n_unbalanced, n_both, n_empty)


def complement_type(orbit_type: OrbitType) -> OrbitType:
    unbalanced, both, empty = orbit_type
    return (unbalanced, empty, both)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_value(config: Config, remaining: Remaining) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def q10(remaining: Remaining) -> bool:
    return remaining[2] == 1 or remaining[3] == 1 or remaining[4] == 1


def remaining_label(kind: OrbitType) -> str:
    if kind == axis_type(EMPTY):
        return "empty"
    if kind == axis_type(FULL):
        return "full"
    assignment = dict(zip(REMAINING_ORDER, REMAINING_LABELS, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def build_orbits() -> dict[OrbitType, frozenset[Config]]:
    orbits: dict[OrbitType, frozenset[Config]] = {}
    seen: set[Config] = set()
    for raw in product((0, 1), repeat=6):
        config: Config = (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5])
        if config in seen:
            continue
        orbit: set[Config] = set()
        stack = [config]
        while stack:
            current = stack.pop()
            if current in orbit:
                continue
            orbit.add(current)
            for rotation in ROTATIONS:
                stack.append(rotate_config(current, rotation))
        orbit_type = axis_type(config)
        if any(axis_type(member) != orbit_type for member in orbit):
            raise RuntimeError("orbit mixed axis types")
        orbits[orbit_type] = frozenset(orbit)
        seen.update(orbit)
    return orbits


def neighborhood(site: Site, locked: set[Site]) -> Config:
    values = []
    for direction in DIRECTIONS:
        neighbor = (
            site[0] + direction[0],
            site[1] + direction[1],
            site[2] + direction[2],
        )
        values.append(1 if neighbor in locked else 0)
    return (values[0], values[1], values[2], values[3], values[4], values[5])


def evolve(locked: set[Site], remaining: Remaining) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if remaining_value(neighborhood(site, locked), remaining):
            nxt.add(site)
    return nxt


def fills_from_seed(remaining: Remaining, seed: frozenset[Site]) -> bool:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, remaining)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def coverage10(remaining: Remaining) -> int:
    return sum(1 for seed in TEN_SITE_SEEDS if fills_from_seed(remaining, seed))


def all_remaining_maps() -> list[Remaining]:
    maps: list[Remaining] = []
    for mask in range(32):
        maps.append(tuple((mask >> rank) & 1 for rank in range(5)))  # type: ignore[arg-type]
    return maps


def bits_from_predicate(
    predicate, orbit_types: tuple[OrbitType, ...], orbits: dict[OrbitType, frozenset[Config]]
) -> tuple[int, ...]:
    bits = []
    for orbit_type in orbit_types:
        sample = next(iter(orbits[orbit_type]))
        value = int(predicate(sample))
        if any(int(predicate(member)) != value for member in orbits[orbit_type]):
            raise RuntimeError("predicate is not cube-covariant")
        bits.append(value)
    return tuple(bits)


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Remaining:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)  # type: ignore[return-value]


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> Remaining:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


def f_cut_free_data(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> tuple[list[tuple[OrbitType, OrbitType]], list[OrbitType]]:
    used: set[OrbitType] = set()
    pairs: list[tuple[OrbitType, OrbitType]] = []
    fixed: list[OrbitType] = []
    for orbit_type in orbit_types:
        if orbit_type in used:
            continue
        image = complement_type(orbit_type)
        if image == orbit_type:
            fixed.append(orbit_type)
        else:
            pair = tuple(sorted((orbit_type, image)))
            pairs.append((pair[0], pair[1]))
            used.add(orbit_type)
            used.add(image)
    free_pairs = [pair for pair in pairs if empty_type not in pair and full_type not in pair]
    free_fixed = [orbit_type for orbit_type in fixed if orbit_type not in (empty_type, full_type)]
    return free_pairs, free_fixed


def first_remaining_refuse(
    remaining: Remaining, seed: frozenset[Site]
) -> list[tuple[int, Site, OrbitType, str, Config]]:
    locked = set(seed)
    for tick in range(14):
        events: list[tuple[int, Site, OrbitType, str, Config]] = []
        for site in TWO_CUBE:
            if site in locked:
                continue
            nbhd = neighborhood(site, locked)
            if remaining_value(nbhd, F1_REMAINING) == 1 and remaining_value(nbhd, remaining) == 0:
                kind = axis_type(nbhd)
                events.append((tick, site, kind, remaining_label(kind), nbhd))
        if events:
            return events
        nxt = evolve(locked, remaining)
        if nxt == locked:
            return []
        locked = nxt
    return []


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    note_flat = normalize(note)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")

    orbits = build_orbits()
    orbit_types = tuple(sorted(orbits))
    orbit_sizes = {orbit_type: len(orbits[orbit_type]) for orbit_type in orbit_types}
    empty_type = axis_type(EMPTY)
    full_type = axis_type(FULL)
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    n_cut = 1 << n_free

    maps = all_remaining_maps()
    zeros = [remaining for remaining in maps if remaining[2] == remaining[3] == remaining[4] == 0]
    f_z = min(zeros)
    cov_by_map = {remaining: coverage10(remaining) for remaining in maps}
    cov10_zeros = {remaining: cov_by_map[remaining] for remaining in zeros}
    n_pos = sum(1 for cov in cov_by_map.values() if cov > 0)
    cov0_maps = sorted(remaining for remaining, cov in cov_by_map.items() if cov == 0)

    seed_f1 = next(seed for seed in TEN_SITE_SEEDS if fills_from_seed(F1_REMAINING, seed))
    refuse_events = first_remaining_refuse(f_z, seed_f1)
    first = refuse_events[0]
    first_tick, first_site, first_kind, first_type, first_nbhd = first
    n_refuse = len(refuse_events)
    refuse_types = tuple(sorted({event[3] for event in refuse_events}))

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"n_ten_site_seeds={len(TEN_SITE_SEEDS)}")
    print(f"Q10_false={sorted(zeros)}")
    print(f"f_z={f_z}")
    print(f"N_pos={n_pos}")
    print(f"cov0_maps={cov0_maps}")
    print(f"S={tuple(sorted(seed_f1))}")
    print(f"f1_fills_S={fills_from_seed(F1_REMAINING, seed_f1)}")
    print(f"f_z_fills_S={fills_from_seed(f_z, seed_f1)}")
    print(f"cov10_zeros={cov10_zeros}")
    print(f"q10_f_z={int(q10(f_z))}")
    print(f"first_refuse_tick={first_tick}")
    print(f"first_refuse_site={first_site}")
    print(f"first_refuse_type={first_type}")
    print(f"first_refuse_kind={first_kind}")
    print(f"N_refuse={n_refuse}")
    print(f"refuse_types={refuse_types}")
    print(f"f_L1_remaining={l1_remaining}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_Q10_FALSE_TEN_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_Q10_FALSE_TEN_SITE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )
    checks.check(
        "thm1-ten-orbits",
        "exactly 10 orbits partition the 64 cells of {0,1}^6",
        len(orbit_types) == 10 and sum(orbit_sizes.values()) == 64,
    )
    expected_sizes = {
        (0, 0, 3): 1,
        (0, 1, 2): 3,
        (0, 2, 1): 3,
        (0, 3, 0): 1,
        (1, 0, 2): 6,
        (1, 1, 1): 12,
        (1, 2, 0): 6,
        (2, 0, 1): 12,
        (2, 1, 0): 12,
        (3, 0, 0): 8,
    }
    checks.check(
        "thm1-orbit-sizes",
        "orbit sizes are the axis-type class sizes",
        orbit_sizes == expected_sizes,
    )
    checks.check(
        "thm1-f-cut-cardinality",
        "F_cut has five free bits and size 32",
        n_free == 5
        and n_cut == 32
        and len(free_pairs) == 3
        and len(free_fixed) == 2
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis has c_+ != c_-",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        ),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and l1_remaining == L1_REMAINING
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-ten-site-seeds",
        "the two-cube has twelve vertices and 66 ten-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(TEN_SITE_SEEDS) == 66
        and len(set(TEN_SITE_SEEDS)) == 66
        and all(seed <= set(TWO_CUBE) and len(seed) == 10 for seed in TEN_SITE_SEEDS),
    )
    checks.check(
        "thm1-q10-false-are-the-cov10-zeros",
        "the four maps with adj2=vertex3=mixed3=0 are exactly the cov10=0 maps",
        sorted(zeros) == sorted(Q10_FALSE)
        and f_z == F_Z
        and f_z == min(zeros)
        and all(not q10(remaining) for remaining in zeros)
        and all(q10(remaining) for remaining in maps if remaining not in zeros)
        and cov0_maps == sorted(zeros)
        and all(cov == 0 for cov in cov10_zeros.values())
        and n_pos == 28,
    )
    checks.check(
        "thm1-lex-first-seed-and-refuse",
        "first remaining-bit refuse of (0,0,0,0,0) from the lex-first 10-site f1 fill is tick 0, site (2,1,0), type adj2",
        seed_f1
        == frozenset(
            (
                (0, 0, 0),
                (0, 0, 1),
                (0, 1, 0),
                (0, 1, 1),
                (1, 0, 0),
                (1, 0, 1),
                (1, 1, 0),
                (1, 1, 1),
                (2, 0, 0),
                (2, 0, 1),
            )
        )
        and fills_from_seed(F1_REMAINING, seed_f1)
        and not fills_from_seed(f_z, seed_f1)
        and first_tick == 0
        and first_site == (2, 1, 0)
        and first_type == "adj2"
        and first_kind == (2, 0, 1)
        and remaining_value(first_nbhd, f_z) == 0
        and remaining_value(first_nbhd, F1_REMAINING) == 1,
    )
    checks.check(
        "thm2-n-refuse-first-tick",
        "N_refuse on the first refuse tick is 2",
        n_refuse == 2
        and refuse_types == ("adj2",)
        and [event[1] for event in refuse_events] == [(2, 1, 0), (2, 1, 1)]
        and [event[3] for event in refuse_events] == ["adj2", "adj2"],
    )
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site." in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted refuse, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "Displayed, not adopted" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "note-reports-seed-and-refuse",
        "the note reports S, the first remaining-bit refuse, and N_refuse=2",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "(0, 0, 0, 0, 0)" in note
        and "tick `0`" in note
        and "site `(2, 1, 0)`" in note
        and "remaining-bit type `adj2`" in note
        and "`N_refuse = 2`" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the refuse into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-inclusion",
        "the residual is the first refuse of the Q10-false map, not leftover of c10bit3/#6566",
        "Not leftover-character of c10bit3" in note
        and "Not leftover-character of #6566" in note
        and "first remaining-bit refuse" in note,
    )
    checks.check(
        "claim-scope-first-refuse",
        "claim_scope names the first remaining-bit refuse of the lex-first Q10-false F_cut map on the lex-first 10-site f1 fill",
        "On the two-cube with off-patch o=0" in note
        and "first remaining-bit refuse of the lex-first Q10-false" in note
        and "lex-first 10-site f1 fill" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "thm3-display-only",
        "the refuse is displayed, not adopted",
        "Do not adopt a remaining bit" in note
        and "Displayed, not adopted" in note
        and first_type == "adj2"
        and first_tick == 0
        and n_refuse == 2,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — the 32 F_cut maps are scored on the 66 ten-site seeds")
    print("per_block: checked exactly — the first remaining-bit refuse of f_z from S is named on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
