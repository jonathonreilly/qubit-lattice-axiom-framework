#!/usr/bin/env python3
"""Exact 2-site fill-coverage ranking of F_cut maps with f(wt1)=0.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
F_W0 is the subclass with f(wt1)=0: a single occupied neighbor does not
form. Dynamics are occupancy-to-lock on the twelve-vertex two-cube with
off-patch occupancy 0. Coverage cov2(f) is the number of unordered 2-site
seeds from which f fills. f_L1 is the unbalanced-axis predicate (some
n_mu != 0), never Hamming |c|_1 mod 2. f_L1 has wt1=1 and is not in F_W0.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_WT1_ZERO_TWO_SITE_MAXIMIZER_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_ZERO_TWO_SITE_MAXIMIZER_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
WT1_TYPE: OrbitType = (1, 0, 2)
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
GENEROUS_WT0: tuple[int, ...] = (0, 1, 1, 1, 1)


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


def halt_size(predicate, seed: frozenset[Site]) -> int:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return len(locked)
        locked = nxt
    return len(locked)


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    return halt_size(predicate, seed) == 12


def coverage(predicate) -> int:
    return sum(1 for seed in TWO_SITE_SEEDS if fills_from_seed(predicate, seed))


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


def predicate_from_bits(
    bits: tuple[int, ...],
    orbit_types: tuple[OrbitType, ...],
    type_of: dict[Config, OrbitType],
):
    assignment = dict(zip(orbit_types, bits, strict=True))

    def predicate(config: Config) -> int:
        return assignment[type_of[config]]

    return predicate


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


def enumerate_f_cut(
    orbit_types: tuple[OrbitType, ...],
    empty_type: OrbitType,
    full_type: OrbitType,
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for mask in range(1 << n_free):
        assignment = {empty_type: 0, full_type: 0}
        for rank, pair in enumerate(free_pairs):
            value = (mask >> rank) & 1
            assignment[pair[0]] = value
            assignment[pair[1]] = value
        for rank, orbit_type in enumerate(free_fixed):
            assignment[orbit_type] = (mask >> (len(free_pairs) + rank)) & 1
        bits = tuple(assignment[orbit_type] for orbit_type in orbit_types)
        remaining = remaining_bits_from_assignment(assignment)
        members.append((bits, remaining))
    return members


def coverage_ranking(
    members: list[tuple[tuple[int, ...], tuple[int, ...]]],
    orbit_types: tuple[OrbitType, ...],
    orbits: dict[OrbitType, frozenset[Config]],
) -> list[tuple[int, tuple[int, ...], tuple[int, ...]]]:
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}
    ranked: list[tuple[int, tuple[int, ...], tuple[int, ...]]] = []
    for bits, remaining in members:
        cov = coverage(predicate_from_bits(bits, orbit_types, type_of))
        ranked.append((cov, remaining, bits))
    return ranked


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
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}

    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    wt0_members = [(bits, remaining) for bits, remaining in members if remaining[0] == 0]
    ranked = coverage_ranking(wt0_members, orbit_types, orbits)
    cov_by_remaining = {remaining: cov for cov, remaining, _bits in ranked}
    n_wt0 = len(wt0_members)
    m2 = max(cov for cov, _remaining, _bits in ranked)
    maximizers = sorted(remaining for cov, remaining, _bits in ranked if cov == m2)
    n_max = len(maximizers)

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    wt1_index = REMAINING_LABELS.index("wt1")
    generous_pred = predicate_from_bits(
        next(bits for bits, remaining in wt0_members if remaining == GENEROUS_WT0),
        orbit_types,
        type_of,
    )
    generous_halts = [halt_size(generous_pred, seed) for seed in TWO_SITE_SEEDS]
    max_halt_wt0 = max(generous_halts)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={n_cut}")
    print(f"|F_W0|={n_wt0}")
    print(f"n_two_site_seeds={len(TWO_SITE_SEEDS)}")
    print(f"m2={m2}")
    print(f"N_max={n_max}")
    print(f"unique_maximizer={n_max == 1}")
    print(f"f_L1_bits={l1_bits}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_L1_wt1={l1_remaining[wt1_index]}")
    print(f"f_hamming_bits={ham_bits}")
    print(f"max_halt_F_W0={max_halt_wt0}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_ZERO_TWO_SITE_MAXIMIZER_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_WT1_ZERO_TWO_SITE_MAXIMIZER_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and len(members) == 32
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
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-sixty-six-seeds",
        "the two-cube has twelve vertices and C(12,2)=66 two-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and len(TWO_SITE_SEEDS) == 66
        and len(set(TWO_SITE_SEEDS)) == 66
        and all(seed <= set(TWO_CUBE) and len(seed) == 2 for seed in TWO_SITE_SEEDS),
    )
    checks.check(
        "thm1-m2-n-max",
        f"max coverage on F_W0 is m2={m2} attained by N_max={n_max} of |F_W0|={n_wt0} maps",
        n_wt0 == 16
        and m2 == 0
        and n_max == 16
        and n_wt0 == sum(1 for _bits, remaining in members if remaining[wt1_index] == 0)
        and m2 == max(cov_by_remaining.values())
        and n_max == sum(1 for cov in cov_by_remaining.values() if cov == m2)
        and set(cov_by_remaining.values()) == {0}
        and f"m2 = {m2}" in note
        and f"N_max = {n_max}" in note
        and f"|F_W0| = {n_wt0}" in note,
    )
    checks.check(
        "thm2-not-unique",
        "N_max is not 1; two-site coverage does not select a unique F_W0 map",
        n_max != 1
        and n_max == n_wt0
        and l1_remaining[wt1_index] == 1
        and l1_remaining == L1_REMAINING
        and l1_remaining not in maximizers
        and "N_max is not 1" in note,
    )
    checks.check(
        "thm3-all-sixteen-attain-m2",
        "every remaining-bit tuple with wt1=0 attains m2; none is adopted",
        n_max == 16
        and maximizers == sorted(remaining for _bits, remaining in wt0_members)
        and all(remaining[wt1_index] == 0 for remaining in maximizers)
        and max_halt_wt0 < 12
        and max_halt_wt0 == 4
        and GENEROUS_WT0 in maximizers
        and "Displayed, not adopted" in note
        and "Do not re-list Max(2) of the full 32" in note,
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
        "bounded theorem, displayed-not-adopted uniqueness failure, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "two-site coverage does not select a unique member" in note
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
        and "This is **not** Hamming parity" in note
        and "f_L1 has remaining-bit tuple `(1, 0, 1, 1, 1)`" in note,
    )
    checks.check(
        "note-reports-ranking",
        "the note reports m2, N_max, |F_W0|, and the uniqueness failure",
        "(wt1, opp2, adj2, vertex3, mixed3)" in note
        and "m2 = 0" in note
        and "N_max = 16" in note
        and "|F_W0| = 16" in note
        and "N_max is not 1" in note
        and "wt1=0" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the ranking into Admissibility" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6429-or-6476-list",
        "the residual is the F_W0 coverage ranking, not leftover of #6429 or a re-list of Max(2)",
        "Not leftover-character of #6429" in note
        and "that ranked all 32" in note
        and "Do not re-list Max(2) of the full 32" in note
        and "new subclass" in note,
    )
    checks.check(
        "claim-scope-ranking",
        "claim_scope states m2, N_max, and displayed-not-adopted",
        "Among the 16 F_cut maps with remaining bit wt1=0" in note
        and "off-patch o=0" in note
        and "maximum 2-site coverage is 0" in note
        and "attained by 16 maps" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — every F_W0 map is scored by how many of the 66 two-site seeds it fills")
    print("per_block: checked exactly — m2 and N_max are the F_W0 coverage-ranking pair on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
