#!/usr/bin/env python3
"""Exact 1-site miss lists of the two vertex3=0 k=4 F_cut maps.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. For f00=(1,1,1,0,0) and f01=(1,1,1,0,1), the runner reconfirms
cov1=8, lists the four missed one-site seeds in lex order, and checks that
the two miss sets are equal. f_L1 is the unbalanced-axis predicate (some
n_mu != 0), never Hamming |c|_1 mod 2. Displayed, not adopted.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_K4_V30_ONE_SITE_MISSES_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_K4_V30_ONE_SITE_MISSES_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
ONE_SITE_SEEDS: tuple[Site, ...] = TWO_CUBE
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
REMAINING_LABELS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
L1_REMAINING: tuple[int, ...] = (1, 0, 1, 1, 1)
F00: tuple[int, ...] = (1, 1, 1, 0, 0)
F01: tuple[int, ...] = (1, 1, 1, 0, 1)
SHARED_FACE: tuple[Site, ...] = (
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
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


def remaining_value(config: Config, remaining: tuple[int, ...]) -> int:
    kind = axis_type(config)
    if kind in (axis_type(EMPTY), axis_type(FULL)):
        return 0
    assignment = dict(zip(REMAINING_ORDER, remaining, strict=True))
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


def evolve(locked: set[Site], predicate) -> set[Site]:
    nxt = set(locked)
    for site in TWO_CUBE:
        if site in locked:
            continue
        if predicate(neighborhood(site, locked)):
            nxt.add(site)
    return nxt


def fills_from_seed(predicate, seed: Site) -> bool:
    locked = {seed}
    for _tick in range(13):
        nxt = evolve(locked, predicate)
        if nxt == locked:
            return len(locked) == 12
        locked = nxt
    return False


def miss_tuple(predicate) -> tuple[Site, ...]:
    return tuple(site for site in ONE_SITE_SEEDS if not fills_from_seed(predicate, site))


def coverage(predicate) -> int:
    return sum(1 for site in ONE_SITE_SEEDS if fills_from_seed(predicate, site))


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


def in_f_cut_remaining(remaining: tuple[int, ...]) -> bool:
    if len(remaining) != 5:
        return False
    assignment = {
        axis_type(EMPTY): 0,
        axis_type(FULL): 0,
    }
    for orbit_type, value in zip(REMAINING_ORDER, remaining, strict=True):
        assignment[orbit_type] = value
        image = complement_type(orbit_type)
        assignment[image] = value
    return all(
        assignment[orbit_type] == assignment[complement_type(orbit_type)]
        for orbit_type in assignment
    ) and assignment[axis_type(EMPTY)] == 0 and assignment[axis_type(FULL)] == 0


def predicate_from_remaining(remaining: tuple[int, ...]):
    def predicate(config: Config) -> int:
        return remaining_value(config, remaining)

    return predicate


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

    pred00 = predicate_from_remaining(F00)
    pred01 = predicate_from_remaining(F01)
    miss00 = miss_tuple(pred00)
    miss01 = miss_tuple(pred01)
    cov00 = coverage(pred00)
    cov01 = coverage(pred01)
    equal = miss00 == miss01

    l1_bits = bits_from_predicate(f_L1, orbit_types, orbits)
    ham_bits = bits_from_predicate(f_hamming, orbit_types, orbits)
    l1_remaining = remaining_bits_from_full(l1_bits, orbit_types)

    print(f"n_rotations={len(ROTATIONS)}")
    print(f"n_orbits={len(orbit_types)}")
    print("orbit_types_and_sizes=" + ",".join(f"{t}:{orbit_sizes[t]}" for t in orbit_types))
    print(f"remaining_labels={REMAINING_LABELS}")
    print(f"n_one_site_seeds={len(ONE_SITE_SEEDS)}")
    print(f"f00={F00}")
    print(f"f01={F01}")
    print(f"cov1_f00={cov00}")
    print(f"cov1_f01={cov01}")
    print(f"miss_f00={miss00}")
    print(f"miss_f01={miss01}")
    print(f"miss_sets_equal={equal}")
    print(f"f_L1_remaining={l1_remaining}")
    print(f"f_hamming_bits={ham_bits}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required note-plus-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_K4_V30_ONE_SITE_MISSES_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_K4_V30_ONE_SITE_MISSES_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )
    checks.check(
        "thm1-rotations-and-orbits",
        "exactly 24 proper cube rotations and 10 axis-type orbits",
        len(ROTATIONS) == 24
        and len(set(ROTATIONS)) == 24
        and len(orbit_types) == 10
        and sum(orbit_sizes.values()) == 64
        and empty_type == (0, 0, 3)
        and full_type == (0, 3, 0)
        and REMAINING_ORDER == ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1)),
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is unbalanced-axis and is not Hamming |c|_1 mod 2",
        l1_bits != ham_bits
        and l1_remaining == L1_REMAINING
        and l1_remaining not in (F00, F01)
        and all(
            f_L1(config) == int(axis_type(config)[0] >= 1)
            for config in product((0, 1), repeat=6)
        )
        and any(f_L1(config) != f_hamming(config) for config in product((0, 1), repeat=6))
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
    )
    checks.check(
        "thm1-two-cube-and-twelve-seeds",
        "the two-cube has twelve vertices in lex order and twelve one-site seeds",
        len(TWO_CUBE) == 12
        and len(set(TWO_CUBE)) == 12
        and TWO_CUBE == tuple(sorted(TWO_CUBE))
        and ONE_SITE_SEEDS == TWO_CUBE
        and set(SHARED_FACE) <= set(TWO_CUBE)
        and len(SHARED_FACE) == 4,
    )
    checks.check(
        "thm1-maps-in-f-cut",
        "f00 and f01 are F_cut maps with vertex3=0 and (wt1,opp2,adj2)=(1,1,1)",
        in_f_cut_remaining(F00)
        and in_f_cut_remaining(F01)
        and F00[:3] == (1, 1, 1)
        and F01[:3] == (1, 1, 1)
        and F00[3] == 0
        and F01[3] == 0
        and F00[4] == 0
        and F01[4] == 1,
    )
    checks.check(
        "thm1-cov1-eight",
        "reconfirm cov1((1,1,1,0,0))=8 and cov1((1,1,1,0,1))=8",
        cov00 == 8
        and cov01 == 8
        and cov00 == 12 - len(miss00)
        and cov01 == 12 - len(miss01)
        and "cov1((1, 1, 1, 0, 0)) = 8" in note
        and "cov1((1, 1, 1, 0, 1)) = 8" in note,
    )
    checks.check(
        "thm2-miss-f00-lex",
        "Miss(f00) is the four shared-face sites in lex order",
        miss00 == SHARED_FACE
        and miss00 == tuple(sorted(miss00))
        and len(miss00) == 4
        and "Miss((1, 1, 1, 0, 0)) = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))"
        in note,
    )
    checks.check(
        "thm2-miss-f01-lex",
        "Miss(f01) is the four shared-face sites in lex order",
        miss01 == SHARED_FACE
        and miss01 == tuple(sorted(miss01))
        and len(miss01) == 4
        and "Miss((1, 1, 1, 0, 1)) = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))"
        in note,
    )
    checks.check(
        "thm3-miss-sets-equal",
        "the two miss sets are equal",
        equal
        and miss00 == miss01
        and set(miss00) == set(SHARED_FACE)
        and "The two miss sets are equal" in note
        and "`Miss(f00) = Miss(f01)`" in note,
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
        "bounded theorem, displayed-not-adopted equality, and machine status",
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
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt vertex3",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not write `vertex3` into Admissibility" in note
        and "Do not adopt `vertex3`" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6444",
        "the residual is the missed-corner lists, not leftover-character of #6444",
        "Not leftover-character of #6444" in note
        and "that only reported 8" in note
        and "New object (the missed corners)" in note,
    )
    checks.check(
        "claim-scope-equality",
        "claim_scope states the two maps miss the reported seeds and the miss sets are equal",
        "On the two-cube with off-patch o=0" in note
        and "(1,1,1,0,0)" in note
        and "(1,1,1,0,1)" in note
        and "miss the reported 1-site seeds" in note
        and "those miss sets are equal" in note
        and "Displayed, not adopted" in note,
    )

    print("per_element: checked exactly — each of the 64 neighbor 6-tuples is assigned its axis-type orbit")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — each of the two vertex3=0 k=4 maps is scored on the 12 one-site seeds")
    print("per_block: checked exactly — the two lex miss sets are equal on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
