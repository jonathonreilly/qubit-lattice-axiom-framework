#!/usr/bin/env python3
"""Lex-first |S|<=3 seed that splits F_cut (1,1,1,1,0) from its wt1=0 sibling.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. Remaining bits are (wt1, opp2, adj2, vertex3, mixed3). The
displayed map is f0=(1,1,1,1,0); its wt1=0 sibling is fwt=(0,1,1,1,0).
f_L1 is the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2. The first split seed and both lock histories are displayed,
not adopted.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_WT1_ZERO_F0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_ZERO_F0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]

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
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
F0_REMAINING: tuple[int, ...] = (1, 1, 1, 1, 0)
FWT_REMAINING: tuple[int, ...] = (0, 1, 1, 1, 0)


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


def remaining_value(config: Config, remaining: tuple[int, ...]) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
    if kind in assignment:
        return assignment[kind]
    return assignment[complement_type(kind)]


def predicate_from_remaining(remaining: tuple[int, ...]):
    def predicate(config: Config) -> int:
        return remaining_value(config, remaining)

    return predicate


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


def evolve(locked: set[Site], predicate) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if predicate(neighborhood(site, locked)):
            nxt.add(site)
    return nxt


def lock_history(predicate, seed: frozenset[Site]) -> list[frozenset[Site]]:
    locked = set(seed)
    history = [frozenset(locked)]
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return history
        locked = nxt
        history.append(frozenset(locked))
    return history


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    return len(lock_history(predicate, seed)[-1]) == 12


def k_site_seeds(k: int) -> tuple[frozenset[Site], ...]:
    return tuple(frozenset(combo) for combo in combinations(TWO_CUBE, k))


def seeds_size_at_most(max_size: int) -> tuple[frozenset[Site], ...]:
    return tuple(
        frozenset(combo)
        for size in range(1, max_size + 1)
        for combo in combinations(TWO_CUBE, size)
    )


def coverage_k(predicate, k: int) -> int:
    return sum(1 for seed in k_site_seeds(k) if fills_from_seed(predicate, seed))


def enumerate_remaining() -> tuple[tuple[int, ...], ...]:
    return tuple(tuple((mask >> index) & 1 for index in range(5)) for mask in range(32))


def maximizers_k(k: int) -> tuple[int, tuple[tuple[int, ...], ...], dict[tuple[int, ...], int]]:
    scores: dict[tuple[int, ...], int] = {}
    for remaining in enumerate_remaining():
        scores[remaining] = coverage_k(predicate_from_remaining(remaining), k)
    maximum = max(scores.values())
    winners = tuple(sorted(remaining for remaining, score in scores.items() if score == maximum))
    return maximum, winners, scores


def first_split_seed(
    pred_fill, pred_miss, max_size: int
) -> frozenset[Site] | None:
    for seed in seeds_size_at_most(max_size):
        if fills_from_seed(pred_fill, seed) and not fills_from_seed(pred_miss, seed):
            return seed
    return None


def seed_key(seed: frozenset[Site]) -> tuple[Site, ...]:
    return tuple(sorted(seed))


def history_key(history: list[frozenset[Site]]) -> list[tuple[Site, ...]]:
    return [tuple(sorted(step)) for step in history]


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

    pred_f0 = predicate_from_remaining(F0_REMAINING)
    pred_fwt = predicate_from_remaining(FWT_REMAINING)
    pred_l1 = f_L1

    m1, max1, cov1 = maximizers_k(1)
    m2, max2, cov2 = maximizers_k(2)
    cov11_fwt = coverage_k(pred_fwt, 11)
    cov11_f0 = coverage_k(pred_f0, 11)

    seed = first_split_seed(pred_f0, pred_fwt, 3)
    if seed is None:
        raise RuntimeError("no |S|<=3 seed splits f0 from fwt")
    hist_f0 = lock_history(pred_f0, seed)
    hist_fwt = lock_history(pred_fwt, seed)
    seed_tuple = seed_key(seed)
    hist_f0_tuples = history_key(hist_f0)
    hist_fwt_tuples = history_key(hist_fwt)

    l1_sample = next(iter(orbits[(1, 0, 2)]))
    ham_differs = any(
        f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6)
    )

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"|F_cut|=32")
    print(f"n_sites={len(TWO_CUBE)}")
    print(f"Max(1): m={m1} N_max={len(max1)} maximizers={list(max1)}")
    print(f"Max(2): m={m2} N_max={len(max2)} maximizers={list(max2)}")
    print(f"cov1_f0={cov1[F0_REMAINING]} cov1_fwt={cov1[FWT_REMAINING]}")
    print(f"cov2_f0={cov2[F0_REMAINING]} cov2_fwt={cov2[FWT_REMAINING]}")
    print(f"cov11_f0={cov11_f0} cov11_fwt={cov11_fwt}")
    print(f"|S|={len(seed)} S={seed_tuple}")
    print(f"f0_history={hist_f0_tuples}")
    print(f"fwt_history={hist_fwt_tuples}")
    print(f"f0_fills={len(hist_f0[-1]) == 12} fwt_fills={len(hist_fwt[-1]) == 12}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_ZERO_F0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_WT1_ZERO_F0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
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
        "thm1-ten-orbits",
        "exactly 10 orbits partition the 64 cells of {0,1}^6",
        len(orbit_types) == 10
        and sum(orbit_sizes.values()) == 64
        and orbit_sizes == expected_sizes
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is n != 0 on an axis and is not Hamming parity",
        all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and ham_differs
        and f_L1(l1_sample) == 1
        and L1_REMAINING != F0_REMAINING
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-f0-in-max1-and-max2",
        "f0=(1,1,1,1,0) attains Max(1) and Max(2)",
        F0_REMAINING in max1
        and F0_REMAINING in max2
        and cov1[F0_REMAINING] == m1 == 12
        and cov2[F0_REMAINING] == m2 == 66
        and len(max1) == 4
        and len(max2) == 2
        and "Max(1)" in note
        and "Max(2)" in note
        and "(1, 1, 1, 1, 0)" in note,
    )
    checks.check(
        "thm1-fwt-in-neither",
        "fwt=(0,1,1,1,0) is in neither Max(1) nor Max(2)",
        FWT_REMAINING not in max1
        and FWT_REMAINING not in max2
        and cov1[FWT_REMAINING] == 0
        and cov2[FWT_REMAINING] == 0
        and cov11_fwt == 12
        and "(0, 1, 1, 1, 0)" in note
        and "neither Max(1) nor Max(2)" in note,
    )
    checks.check(
        "thm2-lex-first-seed",
        "the lex-first |S|<=3 split seed is the singleton {(0, 0, 0)}",
        seed == frozenset({(0, 0, 0)})
        and len(seed) == 1
        and seed_tuple == ((0, 0, 0),)
        and seed == first_split_seed(pred_f0, pred_fwt, 3)
        and "{(0, 0, 0)}" in note
        and "|S| = 1" in note,
    )
    checks.check(
        "thm2-f0-fills-fwt-misses",
        "on that seed f0 fills and fwt does not",
        fills_from_seed(pred_f0, seed)
        and not fills_from_seed(pred_fwt, seed)
        and len(hist_f0[-1]) == 12
        and len(hist_fwt[-1]) == 1
        and fills_from_seed(pred_l1, seed),
    )
    expected_f0 = [
        ((0, 0, 0),),
        ((0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0)),
        ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)),
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
            (2, 1, 0),
        ),
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
            (2, 1, 0),
            (2, 1, 1),
        ),
    ]
    checks.check(
        "thm3-histories",
        "histories from S are computed and displayed; wt1 is not adopted",
        hist_f0_tuples == expected_f0
        and hist_fwt_tuples == [((0, 0, 0),)]
        and len(hist_f0) == 5
        and len(hist_fwt) == 1
        and "halt lock set" in note
        and "Do not adopt wt1" in note
        and "Displayed, not adopted" in note,
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
        "bounded theorem, displayed-not-adopted first split, and machine status",
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
        "claim-scope-first-split",
        "claim_scope reports the lex-first |S|<=3 f0-versus-fwt split",
        "lex-first seed of size at most 3" in note
        and "off-patch o=0" in note
        and "F_cut (1,1,1,1,0) fills and (0,1,1,1,0) does not" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt wt1",
        "no axiom or approved primitive is added" in note
        and "Do not write them into Admissibility" in note
        and "Do not adopt wt1" in note
        and "off-patch occupancy `0`" in note
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-max11-listing",
        "the residual is the first split seed, not leftover-character of the Max(11) listing",
        "Not leftover-character of the Max(11) listing" in note
        and "mixed3-silent" in note
        and "(wt1, opp2, adj2, vertex3, mixed3)" in note,
    )

    print("per_element: checked exactly — each neighbor 6-tuple is scored by axis type")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same stencil")
    print("per_mode: checked exactly — Max(1) and Max(2) are scored over all 32 F_cut maps")
    print("per_block: checked exactly — lex search of |S|<=3 seeds reports the first split")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
