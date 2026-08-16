#!/usr/bin/env python3
"""2-site and 4-site fill coverage of F_cut remaining bits (0,0,1,1,0).

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. f_ex0 is the remaining-bit map (wt1, opp2, adj2, vertex3,
mixed3)=(0,0,1,1,0). Coverage covk(f) is the number of unordered k-site
seeds from which f fills. The new object is the pair (cov2, cov4) of this
named map. P(f):=(wt1=1) and (adj2,vertex3,mixed3)!=(0,0,0). P=0 implies
cov2=0; cov2(f_ex0) is the control. f_L1 is the unbalanced-axis predicate
(some n_mu != 0), never Hamming |c|_1 mod 2. Scores are displayed, not
adopted.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_EX0_COV2_COV4_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_EX0_COV2_COV4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Direction = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
OrbitType = tuple[int, int, int]
Site = tuple[int, int, int]
Bits = tuple[int, int, int, int, int]

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
FOUR_SITE_SEEDS: tuple[frozenset[Site], ...] = tuple(
    frozenset(quad) for quad in combinations(TWO_CUBE, 4)
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
EX0_REMAINING: Bits = (0, 0, 1, 1, 0)
L1_REMAINING: Bits = (1, 0, 1, 1, 1)
EMPTY_TYPE: OrbitType = (0, 0, 3)
FULL_TYPE: OrbitType = (0, 3, 0)


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


def orbit_name(config: Config) -> str:
    weight = sum(config)
    n_full = sum(1 for axis in range(3) if config[2 * axis] == 1 and config[2 * axis + 1] == 1)
    if weight == 0:
        return "empty"
    if weight == 6:
        return "full"
    if weight == 1:
        return "wt1"
    if weight == 5:
        return "wt5"
    if weight == 2:
        return "opp2" if n_full == 1 else "adj2"
    if weight == 4:
        return "opp4" if n_full == 2 else "adj4"
    if weight == 3:
        return "mixed3" if n_full == 1 else "vertex3"
    raise ValueError(config)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    return int(any(config[2 * axis] != config[2 * axis + 1] for axis in range(3)))


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def f_ex0(config: Config) -> int:
    """F_cut remaining bits (0, 0, 1, 1, 0): adj2/adj4 and vertex3 only."""
    return int(orbit_name(config) in ("adj2", "adj4", "vertex3"))


def selector_p(bits: Bits) -> bool:
    wt1, _opp2, adj2, vertex3, mixed3 = bits
    return wt1 == 1 and (adj2, vertex3, mixed3) != (0, 0, 0)


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


def fills_from_seed(predicate, seed: frozenset[Site]) -> bool:
    locked = set(seed)
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def coverage(predicate, seeds: tuple[frozenset[Site], ...]) -> int:
    return sum(1 for seed in seeds if fills_from_seed(predicate, seed))


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


def remaining_bits_from_assignment(assignment: dict[OrbitType, int]) -> Bits:
    return tuple(assignment[orbit_type] for orbit_type in REMAINING_ORDER)  # type: ignore[return-value]


def remaining_bits_from_full(
    bits: tuple[int, ...], orbit_types: tuple[OrbitType, ...]
) -> Bits:
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
) -> list[tuple[tuple[int, ...], Bits]]:
    free_pairs, free_fixed = f_cut_free_data(orbit_types, empty_type, full_type)
    n_free = len(free_pairs) + len(free_fixed)
    members: list[tuple[tuple[int, ...], Bits]] = []
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


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")
        if not condition and residual is not None:
            print(f"  residual: {residual}")

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
    members = enumerate_f_cut(orbit_types, empty_type, full_type)
    type_of = {config: orbit_type for orbit_type, group in orbits.items() for config in group}

    ex0_bits = bits_from_predicate(f_ex0, orbit_types, orbits)
    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    ex0_remaining = remaining_bits_from_full(ex0_bits, orbit_types)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)
    p_ex0 = selector_p(ex0_remaining)

    cov2_ex0 = coverage(f_ex0, TWO_SITE_SEEDS)
    cov3_ex0 = coverage(f_ex0, THREE_SITE_SEEDS)
    cov4_ex0 = coverage(f_ex0, FOUR_SITE_SEEDS)

    p_false_cov2_positive: list[Bits] = []
    for bits, remaining in members:
        if selector_p(remaining):
            continue
        predicate = predicate_from_bits(bits, orbit_types, type_of)
        if coverage(predicate, TWO_SITE_SEEDS) > 0:
            p_false_cov2_positive.append(remaining)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"N_free={n_free}")
    print(f"|F_cut|={len(members)}")
    print(f"n_two_site_seeds={len(TWO_SITE_SEEDS)}")
    print(f"n_three_site_seeds={len(THREE_SITE_SEEDS)}")
    print(f"n_four_site_seeds={len(FOUR_SITE_SEEDS)}")
    print(f"f_ex0_remaining={ex0_remaining}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"P_f_ex0={int(p_ex0)}")
    print(f"cov2_f_ex0={cov2_ex0}")
    print(f"cov3_f_ex0={cov3_ex0}")
    print(f"cov4_f_ex0={cov4_ex0}")
    print(f"n_P_false_with_cov2_positive={len(p_false_cov2_positive)}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_EX0_COV2_COV4_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_EX0_COV2_COV4_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source,
    )
    checks.check(
        "thm1-twenty-four-rotations",
        "exactly 24 proper cube rotations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
    )
    checks.check(
        "thm1-f-cut-and-two-cube",
        "F_cut has five free bits and size 32; two-cube has 12 vertices",
        n_free == 5
        and len(members) == 32
        and len(orbit_types) == 10
        and sum(orbit_sizes.values()) == 64
        and len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and empty_type == EMPTY_TYPE
        and full_type == FULL_TYPE
        and len(TWO_SITE_SEEDS) == 66
        and len(FOUR_SITE_SEEDS) == 495,
    )
    checks.check(
        "thm1-f-ex0-remaining-bits",
        "f_ex0 is the F_cut remaining-bit tuple (0,0,1,1,0)",
        in_f_cut(ex0_bits, orbit_types, empty_type, full_type)
        and ex0_remaining == EX0_REMAINING
        and f_ex0((1, 0, 1, 0, 0, 0)) == 1
        and f_ex0((1, 0, 1, 0, 1, 0)) == 1
        and f_ex0((1, 0, 0, 0, 0, 0)) == 0
        and f_ex0((1, 1, 0, 0, 0, 0)) == 0
        and f_ex0((1, 0, 1, 1, 0, 0)) == 0
        and f_ex0(EMPTY) == 0
        and f_ex0(FULL) == 0,
        residual=ex0_remaining,
    )
    checks.check(
        "thm1-p-false",
        "P(f_ex0)=0 because wt1=0",
        p_ex0 is False
        and EX0_REMAINING[0] == 0
        and selector_p(EX0_REMAINING) is False
        and "P(f_ex0)=0" in note,
    )
    checks.check(
        "thm1-cov2-zero",
        "cov2(f_ex0)=0 on all 66 two-site seeds",
        cov2_ex0 == 0
        and cov2_ex0 == coverage(f_ex0, TWO_SITE_SEEDS)
        and "cov2(f_ex0) = 0" in note,
        residual=cov2_ex0,
    )
    checks.check(
        "thm1-p-implies-cov2-zero",
        "P=0 implies cov2=0, and f_ex0 matches that implication",
        (not p_ex0) and cov2_ex0 == 0
        and p_false_cov2_positive == []
        and all((not selector_p(remaining)) or True for _bits, remaining in members)
        and "P=0" in note
        and "cov2=0" in note,
        residual=p_false_cov2_positive,
    )
    checks.check(
        "thm1-investment-cov3",
        "reconfirm #6511 scores P=0 and cov3(f_ex0)=24",
        cov3_ex0 == 24
        and len(THREE_SITE_SEEDS) == 220
        and "cov3(f_ex0)=24" in note
        and "#6511" in note,
        residual=cov3_ex0,
    )
    checks.check(
        "thm2-cov4",
        "cov4(f_ex0)=232 among the 495 four-site seeds",
        cov4_ex0 == 232
        and cov4_ex0 == coverage(f_ex0, FOUR_SITE_SEEDS)
        and "cov4(f_ex0) = 232" in note
        and EX0_REMAINING[2] == 1
        and EX0_REMAINING[0] == 0,
        residual=cov4_ex0,
    )
    checks.check(
        "thm3-display-not-adopt",
        "the note displays the scores and refuses adoption of a bit",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write" in note
        and "not written into Admissibility" in note_flat,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is n!=0 (some-axis-unbalanced), not Hamming parity",
        l1_remaining == L1_REMAINING
        and l1_bits != ham_bits
        and in_f_cut(l1_bits, orbit_types, empty_type, full_type)
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
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
        "bounded theorem, machine status, and N1-N8 are source-visible",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "target_claim_type: bounded_theorem" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "audit_required_before_effective_retained: true" in note
        and "bare_retained_allowed: false" in note
        and "authors no audit verdict" in note
        and "FAIL / DO NOT SHIP" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note,
    )
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden)
        and "promoted" not in note.lower()
        and "new axiom" not in note
        and "Block 12" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6511-6509",
        "the residual is the (cov2,cov4) pair of this named map, not leftover of #6511 or #6509",
        "Not leftover-character of #6511" in note
        and "Not leftover-character of #6509" in note
        and "New scores of a newly named map" in note
        and "#6511" in note
        and "#6509" in note,
    )
    checks.check(
        "claim-scope",
        "claim_scope reports 2-site and 4-site coverage of F_cut (0,0,1,1,0)",
        "On the two-cube with off-patch o=0, the 2-site and 4-site coverage of F_cut (0,0,1,1,0) are reported."
        in note
        and "Displayed, not adopted" in note
        and "(0,0,1,1,0)" in note.replace(" ", "").replace("(", "(")
        and "cov2(f_ex0) = 0" in note
        and "cov4(f_ex0) = 232" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write the scores into Admissibility" in note,
    )
    checks.check(
        "seeds-not-listed",
        "the note does not list two-site or four-site seeds",
        "Do not list the seeds" in note
        and "combinations(TWO_CUBE" not in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — f_ex0 is scored by 2-site and 4-site fill coverage")
    print("per_block: checked exactly — (cov2,cov4)=(0,232) is the displayed pair for remaining bits (0,0,1,1,0)")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
