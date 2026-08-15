#!/usr/bin/env python3
"""First 3-site seed where the two F_cut cov=66 maximizers disagree.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
The two maps that fill every unordered 2-site seed on the twelve-vertex
two-cube with off-patch occupancy 0 have remaining-bit tuples
(1, 1, 1, 1, 0) and (1, 1, 1, 1, 1). This runner recomputes that they
agree on every 2-site fill, then walks combinations(TWO_CUBE, 3) until
the first 3-site seed at which their fill bits differ. That seed is
displayed. Neither map is adopted. This is not an |S| census and is not
leftover-character of #6427 (the f_min versus f_L1 |S|=3 census). f_L1 is
the unbalanced-axis predicate (some n_mu != 0), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_COV66_THREE_SITE_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COV66_THREE_SITE_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(pair) for pair in combinations(TWO_CUBE, 2)
)
THREE_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(triple) for triple in combinations(TWO_CUBE, 3)
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
F1_REMAINING: tuple[int, ...] = (1, 1, 1, 1, 1)
ONE_SITE_SEED: frozenset[Site] = frozenset(((0, 0, 0),))
EXPECTED_ONE_SITE_HISTORY: tuple[int, ...] = (1, 4, 8, 11, 12)
EXPECTED_S_STAR: frozenset[Site] = frozenset(((0, 0, 0), (1, 0, 1), (2, 0, 0)))
DISPLAY_SITE: Site = (1, 0, 0)
MIXED3: OrbitType = (1, 1, 1)


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


def f0(config: Config) -> int:
    """Displayed cov=66 maximizer: remaining bits (1, 1, 1, 1, 0).  Not adopted."""
    return remaining_value(config, F0_REMAINING)


def f1(config: Config) -> int:
    """Other cov=66 maximizer: remaining bits (1, 1, 1, 1, 1).  Not adopted."""
    return remaining_value(config, F1_REMAINING)


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


def lock_run(predicate, seed: frozenset[Site]) -> tuple[tuple[int, ...], bool]:
    locked = set(seed)
    history = [len(locked)]
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return (tuple(history), len(locked) == 12)
        locked = nxt
        history.append(len(locked))
    return (tuple(history), len(locked) == 12)


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    return lock_run(predicate, seed)[1]


def coverage(predicate) -> int:
    return sum(1 for seed in TWO_SITE_SEEDS if fills_from_seed(predicate, seed))


def two_site_fill_agreement(left, right) -> bool:
    return all(
        fills_from_seed(left, seed) == fills_from_seed(right, seed)
        for seed in TWO_SITE_SEEDS
    )


def first_three_site_fill_split(left, right) -> frozenset[Site] | None:
    for seed in THREE_SITE_SEEDS:
        if fills_from_seed(left, seed) != fills_from_seed(right, seed):
            return seed
    return None


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


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> tuple[int, ...]:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> tuple[int, ...]:
    assignment = dict(zip(orbit_types, bits, strict=True))
    return remaining_bits_from_assignment(assignment)


def in_f_cut(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> bool:
    assignment = dict(zip(orbit_types, bits, strict=True))
    if assignment[empty_type] != 0 or assignment[full_type] != 0:
        return False
    return all(
        assignment[orbit_type] == assignment[complement_type(orbit_type)]
        for orbit_type in orbit_types
    )


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

    f0_bits = bits_from_predicate(f0, orbit_types, orbits)
    f1_bits = bits_from_predicate(f1, orbit_types, orbits)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    f0_remaining = remaining_bits_from_full(f0_bits, orbit_types)
    f1_remaining = remaining_bits_from_full(f1_bits, orbit_types)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)

    cov0 = coverage(f0)
    cov1 = coverage(f1)
    agree_two_site = two_site_fill_agreement(f0, f1)
    first_split = first_three_site_fill_split(f0, f1)
    hist0, fill0 = lock_run(f0, first_split) if first_split is not None else ((), False)
    hist1, fill1 = lock_run(f1, first_split) if first_split is not None else ((), False)
    hist0_one, fill0_one = lock_run(f0, ONE_SITE_SEED)
    hist1_one, fill1_one = lock_run(f1, ONE_SITE_SEED)
    hist_l1_one, fill_l1_one = lock_run(f_L1, ONE_SITE_SEED)
    nbhd_display = neighborhood(DISPLAY_SITE, set(EXPECTED_S_STAR))
    display_kind = axis_type(nbhd_display)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"n_two_site_seeds={len(TWO_SITE_SEEDS)}")
    print(f"n_three_site_seeds={len(THREE_SITE_SEEDS)}")
    print(f"f0_remaining={f0_remaining}")
    print(f"f1_remaining={f1_remaining}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"cov_f0={cov0}")
    print(f"cov_f1={cov1}")
    print(f"two_site_fill_agreement={agree_two_site}")
    print(f"first_three_site_split={sorted(first_split) if first_split is not None else None}")
    print(f"f0_history={hist0} fill={fill0}")
    print(f"f1_history={hist1} fill={fill1}")
    print(f"one_site_f0_history={hist0_one} fill={fill0_one}")
    print(f"one_site_f1_history={hist1_one} fill={fill1_one}")
    print(f"one_site_f_L1_history={hist_l1_one} fill={fill_l1_one}")
    print(f"display_site={DISPLAY_SITE}")
    print(f"display_neighborhood={nbhd_display}")
    print(f"display_axis_type={display_kind}")
    print(f"f0_on_display={f0(nbhd_display)}")
    print(f"f1_on_display={f1(nbhd_display)}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COV66_THREE_SITE_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_COV66_THREE_SITE_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
    checks.check(
        "thm1-remaining-bits-and-f-cut",
        "f0 and f1 are the named F_cut remaining-bit tuples",
        f0_remaining == F0_REMAINING
        and f1_remaining == F1_REMAINING
        and l1_remaining == L1_REMAINING
        and in_f_cut(f0_bits, orbit_types, empty_type, full_type)
        and in_f_cut(f1_bits, orbit_types, empty_type, full_type)
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is unbalanced-axis / n != 0, not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-seed-counts",
        "the two-cube has twelve vertices, 66 two-site seeds, and 220 three-site seeds",
        len(TWO_CUBE) == 12
        and TWO_CUBE == tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
        and len(TWO_SITE_SEEDS) == 66
        and len(THREE_SITE_SEEDS) == 220
        and THREE_SITE_SEEDS[0] == frozenset(combinations(TWO_CUBE, 3).__next__()),
    )
    checks.check(
        "thm1-cov66-and-two-site-agreement",
        "both maps have two-site cov=66 and agree on every 2-site fill",
        cov0 == 66
        and cov1 == 66
        and agree_two_site
        and "cov=66" in note
        and "agree on every 2-site fill" in note_flat,
    )
    checks.check(
        "thm1-first-three-site-split",
        "the first 3-site fill disagreement is {(0,0,0),(1,0,1),(2,0,0)}",
        first_split == EXPECTED_S_STAR
        and fill0 is False
        and fill1 is True
        and "{(0,0,0),(1,0,1),(2,0,0)}" in note_flat.replace(" ", ""),
    )
    checks.check(
        "thm2-lock-histories",
        "on S* the lock histories are f0:(3,8,10) unfilled and f1:(3,9,12) filled",
        hist0 == (3, 8, 10)
        and hist1 == (3, 9, 12)
        and fill0 is False
        and fill1 is True
        and "(3, 8, 10)" in note
        and "(3, 9, 12)" in note,
    )
    checks.check(
        "thm2-one-site-agrees-with-l1",
        "1-site halt of either maximizer agrees with f_L1 history (1,4,8,11,12)",
        hist0_one == EXPECTED_ONE_SITE_HISTORY
        and hist1_one == EXPECTED_ONE_SITE_HISTORY
        and hist_l1_one == EXPECTED_ONE_SITE_HISTORY
        and fill0_one
        and fill1_one
        and fill_l1_one,
    )
    checks.check(
        "thm3-mixed3-display-neighborhood",
        "the first-wave neighborhood of (1,0,0) on S* is mixed3; f0=0, f1=1",
        display_kind == MIXED3
        and f0(nbhd_display) == 0
        and f1(nbhd_display) == 1
        and F0_REMAINING[4] == 0
        and F1_REMAINING[4] == 1
        and "mixed3" in note
        and "(1, 0, 0)" in note,
    )
    checks.check(
        "thm3-display-not-adopted",
        "the first-split seed and both maps are displayed and not adopted",
        "Displayed, not adopted" in note
        and "Do not adopt either" in note
        and "Do not write them into Admissibility" in note
        and "not written into Admissibility" in note_flat,
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
        "not-an-s-census-or-leftover-ten",
        "the residual is the first fill-split seed, not an |S| census and not leftover-character of #6427",
        "Not an `|S|` census" in note
        and ("N_" + "split") not in note
        and ("N_" + "split") not in self_source
        and "leftover-character of #6427" in note
        and "f_min versus f_L1" in note_flat.replace("`", "")
        and "do not list the other" in note_flat.lower(),
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-scope-first-split",
        "claim_scope names the first 3-site seed and the two fill verdicts",
        "first 3-site seed" in note
        and "off-patch o=0" in note
        and "(1,1,1,1,0)" in note_flat.replace(" ", "")
        and "(1,1,1,1,1)" in note_flat.replace(" ", "")
        and "does not fill" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write them into Admissibility" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — both cov=66 maximizers are scored on every 2-site seed and walked in combinations order on 3-site seeds until the first fill disagreement")
    print("per_block: checked exactly — the first-split seed, the two lock histories, and the mixed3 neighborhood of (1,0,0) are displayed")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
