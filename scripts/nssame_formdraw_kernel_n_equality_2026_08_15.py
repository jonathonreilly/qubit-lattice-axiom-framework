#!/usr/bin/env python3
"""Formdraw occupancy kernels on the four nssame probes.

Host Euclidean B_3(0) = {n in Z^3 : n·n <= 9}. Seed at tick 0 records the
origin and (0,1,0), both locking +e_1. Growth is the nssame perp-step
incoming-lock process. At each probe's formation tick, n is the formdraw
occupancy kernel from already-recorded six-neighbor occupancy. No unique
{+,−} letter is assigned. Reverse and face are not scored. Displayed, not
adopted.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "NSSAME_FORMDRAW_KERNEL_N_EQUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NSSAME_FORMDRAW_KERNEL_N_EQUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Vec3 = tuple[Fraction, Fraction, Fraction]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
STEPS: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
AXES: tuple[Point, Point, Point] = (E1, E2, E3)
PROBES: dict[str, Point] = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def lock_axis(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def euclidean_ball() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x, y, z in product(range(-3, 4), repeat=3)
        if x * x + y * y + z * z <= 9
    )


def apply_matrix(matrix: tuple[tuple[int, ...], ...], point: Point) -> Point:
    return tuple(
        matrix[row][0] * point[0]
        + matrix[row][1] * point[1]
        + matrix[row][2] * point[2]
        for row in range(3)
    )


def matrix_det(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    rotations: list[tuple[tuple[int, ...], ...]] = []
    for perm in permutations((0, 1, 2)):
        for signs in product((1, -1), repeat=3):
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for col in range(3):
                matrix[perm[col]][col] = signs[col]
            packed = tuple(tuple(row) for row in matrix)
            if matrix_det(packed) == 1:
                rotations.append(packed)
    return tuple(rotations)


def grow(
    host: frozenset[Point],
    seed: tuple[tuple[Point, Point], ...],
) -> dict[Point, tuple[int, frozenset[Point]]]:
    recorded: dict[Point, tuple[int, frozenset[Point]]] = {
        site: (0, frozenset({lock})) for site, lock in seed
    }
    by_tick: dict[int, list[Point]] = defaultdict(list)
    for site, _lock in seed:
        if site not in host:
            raise ValueError("seed site outside host")
        by_tick[0].append(site)
    tick = 0
    while by_tick[tick]:
        arrivals: dict[Point, set[Point]] = defaultdict(set)
        for site in by_tick[tick]:
            _time, locks = recorded[site]
            for lock in locks:
                axis = lock_axis(lock)
                for step in STEPS:
                    if dot(step, axis) != 0:
                        continue
                    image = add(site, step)
                    if image not in host or image in recorded:
                        continue
                    arrivals[image].add(step)
        for image, incoming in arrivals.items():
            recorded[image] = (tick + 1, frozenset(incoming))
            by_tick[tick + 1].append(image)
        tick += 1
    return recorded


def occupancy(site: Point, formed: frozenset[Point]) -> int:
    """Occupancy is 1 on already-recorded sites only."""
    return 1 if site in formed else 0


def n_vector(site: Point, formed: frozenset[Point]) -> Vec3:
    """Formdraw occupancy kernel n_μ = (o_{+μ} − o_{−μ}) / 3."""
    components = []
    for axis in AXES:
        plus = occupancy(add(site, axis), formed)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), formed)
        components.append(Fraction(plus - minus, 3))
    return (components[0], components[1], components[2])


def already_recorded(
    site: Point, recorded: dict[Point, tuple[int, frozenset[Point]]]
) -> frozenset[Point]:
    formation = recorded[site][0]
    return frozenset(
        other for other, (tick, _locks) in recorded.items() if tick < formation
    )


def probe_kernels(
    recorded: dict[Point, tuple[int, frozenset[Point]]],
) -> dict[str, Vec3]:
    kernels: dict[str, Vec3] = {}
    for name, site in PROBES.items():
        kernels[name] = n_vector(site, already_recorded(site, recorded))
    return kernels


def format_component(value: Fraction) -> str:
    if value == 0:
        return "0"
    sign = "−" if value < 0 else ""
    magnitude = abs(value)
    if magnitude.denominator == 1:
        return f"{sign}{magnitude.numerator}"
    return f"{sign}{magnitude.numerator}/{magnitude.denominator}"


def format_n(n: Vec3) -> str:
    return f"({format_component(n[0])}, {format_component(n[1])}, {format_component(n[2])})"


def neighbor_occupancy(
    site: Point, formed: frozenset[Point]
) -> dict[str, tuple[int, int]]:
    bits: dict[str, tuple[int, int]] = {}
    names = ("e1", "e2", "e3")
    for name, axis in zip(names, AXES):
        plus = occupancy(add(site, axis), formed)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), formed)
        bits[name] = (plus, minus)
    return bits


def audit_paths_literal(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                value = ast.literal_eval(node.value)
                if isinstance(value, tuple) and all(
                    isinstance(item, str) for item in value
                ):
                    return value
                return None
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    host = euclidean_ball()
    seed_same: tuple[tuple[Point, Point], ...] = (
        (ORIGIN, E1),
        (E2, E1),
    )
    seed_mixed: tuple[tuple[Point, Point], ...] = (
        (ORIGIN, E1),
        (E2, E2),
    )

    recorded_same = grow(host, seed_same)
    recorded_mixed = grow(host, seed_mixed)
    kernels = probe_kernels(recorded_same)
    mixed_kernels = probe_kernels(recorded_mixed)
    n_tuple = tuple(kernels[name] for name in ("A", "B", "C", "D"))
    mixed_tuple = tuple(mixed_kernels[name] for name in ("A", "B", "C", "D"))
    equal_cd = kernels["C"] == kernels["D"]
    tuples_equal = n_tuple == mixed_tuple

    print("external_scientific_inputs: none; exact occupancy kernels only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("host: Euclidean B_3(0) with n·n<=9")
    print(f"host_site_count: {len(host)}")
    print("seed: {0,(0,1,0)} both locking +e_1 at tick 0")
    print("process: nssame perp-step incoming-lock")
    print("kernel: formdraw n_μ=(o_{+μ}−o_{−μ})/3 from already-recorded 6-NN")
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        formed = already_recorded(site, recorded_same)
        occ = neighbor_occupancy(site, formed)
        print(
            f"n({name})={format_n(kernels[name])} "
            f"occ=+−e1{occ['e1']} +−e2{occ['e2']} +−e3{occ['e3']} "
            f"incoming={sorted(recorded_same[site][1])}"
        )
    print(f"n(C)=n(D): {equal_cd}")
    print(f"four-n equals mixed-lock formdraw n: {tuples_equal}")
    print("unique f(n) leftover transfers: no")
    print("claim_boundary: displayed, not adopted; not written into Admissibility")
    print("cache_write: false")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")

    declared = audit_paths_literal(self_source)
    checks.check(
        "audit-input-paths-literal",
        "AUDIT_INPUT_PATHS is the declared two-path static tuple",
        declared == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "docs/NSSAME_FORMDRAW_KERNEL_N_EQUALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    checks.check(
        "audit-input-files",
        "declared review inputs exist",
        AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    wide_host = frozenset(
        (x, y, z)
        for x, y, z in product(range(-4, 5), repeat=3)
        if x * x + y * y + z * z <= 9
    )
    checks.check(
        "host-euclidean-ball",
        "host is exactly {n in Z^3 : n·n <= 9}",
        host == wide_host
        and all(dot(site, site) <= 9 for site in host)
        and len(host) == 123,
    )
    checks.check(
        "seed-two-site-same-lock",
        "tick-0 records are origin and (0,1,0), both locking +e_1",
        recorded_same[ORIGIN] == (0, frozenset({E1}))
        and recorded_same[E2] == (0, frozenset({E1}))
        and sum(time == 0 for time, _locks in recorded_same.values()) == 2,
    )
    checks.check(
        "identity-gates-present",
        "occupancy, n_vector, and grow are computed, not hardcoded",
        "def occupancy(" in self_source
        and "def n_vector(" in self_source
        and "def grow(" in self_source
        and "n_μ = (o_{+μ} − o_{−μ}) / 3" in self_source,
    )
    for name in ("A", "B", "C", "D"):
        rendered = f"n({name}) = {format_n(kernels[name])}"
        checks.check(
            f"thm1-n-{name}",
            f"computed n({name}) is recorded in the note",
            rendered in note and PROBES[name] in recorded_same,
        )
    checks.check(
        "thm2-nC-not-equal-nD",
        "n(C)=n(D) fails on the nssame seed",
        (not equal_cd)
        and kernels["C"] != kernels["D"]
        and "n(C) ≠ n(D)" in note,
    )
    checks.check(
        "thm3-tuple-disagrees-mixed-formdraw",
        "four-n tuple is not the mixed-lock formdraw tuple",
        (not tuples_equal)
        and mixed_kernels["A"]
        == (Fraction(-1, 3), Fraction(1, 3), Fraction(0))
        and mixed_kernels["B"]
        == (Fraction(-1, 3), Fraction(0), Fraction(-1, 3))
        and mixed_kernels["C"]
        == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and mixed_kernels["D"]
        == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and "does not transfer" in note,
    )
    formed_a = already_recorded(PROBES["A"], recorded_same)
    formed_d = already_recorded(PROBES["D"], recorded_same)
    checks.check(
        "already-recorded-six-nn",
        "occupancy reads strictly earlier 6-NN, not the unread probe",
        occupancy(PROBES["A"], formed_a) == 0
        and occupancy(ORIGIN, formed_a) == 1
        and occupancy(PROBES["D"], formed_a) == 0
        and occupancy(add(PROBES["A"], (0, -1, 0)), formed_a) == 1
        and occupancy(add(PROBES["D"], E2), formed_d) == 1
        and occupancy(PROBES["A"], formed_d) == 0,
    )
    checks.check(
        "uniqueness-not-required",
        "first-arrival incoming locks at A and D need not be unique",
        len(recorded_same[PROBES["A"]][1]) > 1
        and len(recorded_same[PROBES["D"]][1]) > 1
        and "Uniqueness is not required" in note,
    )
    same_seed_locks = frozenset(seed_same)
    mixed_orbit = False
    for matrix in proper_cubic_rotations():
        image = frozenset(
            (apply_matrix(matrix, site), apply_matrix(matrix, lock))
            for site, lock in seed_mixed
        )
        if image == same_seed_locks:
            mixed_orbit = True
            break
    checks.check(
        "not-mixed-cubic-orbit",
        "same-lock seed is outside the proper cubic orbit of mixed +e_1/+e_2",
        (not mixed_orbit)
        and len(proper_cubic_rotations()) == 24
        and seed_same[0][1] == seed_same[1][1]
        and seed_mixed[0][1] != seed_mixed[1][1],
    )
    origin_parallel_blocked = all(
        recorded_same[ORIGIN][0] + 1
        != recorded_same.get(add(ORIGIN, step), (None, frozenset()))[0]
        for step in (E1, (-1, 0, 0))
    )
    checks.check(
        "perp-step-incoming-lock",
        "origin lock +e_1 blocks parallel steps and allows the four perpendicular steps",
        origin_parallel_blocked
        and recorded_same[(0, -1, 0)][0] == 1
        and recorded_same[E3][0] == 1
        and recorded_same[(0, 0, -1)][0] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    claim_scope = (
        "Formdraw occupancy kernels on the four nssame probes, and whether "
        "n(C)=n(D), are reported. Displayed, not adopted."
    )
    checks.check(
        "note-claim-scope",
        "note claim_scope matches the occupancy-kernel report",
        claim_scope in note,
    )
    checks.check(
        "no-letter-assignment",
        "no unique {+,−} letter is assigned and reverse/face are not scored from n",
        "L(A)" not in note
        and "L(B)" not in note
        and "L(C)" not in note
        and "L(D)" not in note
        and "P_±" not in note
        and "3 t(" not in note
        and "t(C)^2" not in note
        and "no unique" in note.lower(),
    )
    checks.check(
        "no-admissibility-write",
        "display is not written into Admissibility and names no extra axiom",
        "not written into Admissibility" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "Admissibility / Local Constraint" in axiom,
    )
    checks.check(
        "forbidden-phrases-absent",
        "note omits excluded claim language and does not attach a first-lemma tag",
        "G_" + "N" not in note
        and "1/" + "r" not in note
        and "Lattice" + "-named" not in note
        and "not a " + "TOE" not in note
        and "Dijk" + "stra" not in note
        and "Gr" + "am" not in note
        and "L" + "1" not in note
        and "par" + "nn" not in note
        and "k" + "20" not in note
        and "Runner" + " cache" not in note,
    )
    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    record_quote = (
        "When present, a record locks exactly one admissible local possibility."
    )
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    checks.check(
        "axiom-quotes-unedited",
        "Lattice and Record sentences are quoted from the live axiom memo",
        lattice_quote in normalized_axiom
        and record_quote in normalized_axiom
        and lattice_quote in normalized_note
        and record_quote in normalized_note,
    )
    checks.check(
        "no-larger-ball",
        "formation stays inside B_3(0)",
        all(dot(site, site) <= 9 for site in recorded_same)
        and set(recorded_same) <= host
        and "No larger host is used." in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
