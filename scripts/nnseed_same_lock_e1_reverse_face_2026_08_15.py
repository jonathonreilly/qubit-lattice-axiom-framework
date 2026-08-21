#!/usr/bin/env python3
"""Exact perp-step formation ticks for the same-lock +e_1 two-site seed.

Host Euclidean B_3(0) = {n in Z^3 : n·n <= 9}. Seed at tick 0 records the
origin and (0,1,0), both locking +e_1. Growth uses only perp-step incoming
locks. Reverse and face are displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "NNSEED_SAME_LOCK_E1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NNSEED_SAME_LOCK_E1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
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
PROBE_A: Point = (1, 0, 0)
PROBE_B: Point = (1, 1, 1)
PROBE_C: Point = (2, 0, 0)
PROBE_D: Point = (1, 1, 0)


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


def origin_six_mask(
    recorded: dict[Point, tuple[int, frozenset[Point]]],
    *,
    exact_tick: int | None,
) -> tuple[int, ...]:
    bits: list[int] = []
    for step in STEPS:
        neighbor = add(ORIGIN, step)
        if neighbor not in recorded:
            bits.append(0)
            continue
        time, _locks = recorded[neighbor]
        if exact_tick is None:
            bits.append(int(time <= 1))
        else:
            bits.append(int(time == exact_tick))
    return tuple(bits)


def probe_tick(
    recorded: dict[Point, tuple[int, frozenset[Point]]], probe: Point
) -> int | None:
    if probe not in recorded:
        return None
    return recorded[probe][0]


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
    seed_one: tuple[tuple[Point, Point], ...] = ((ORIGIN, E1),)

    recorded_same = grow(host, seed_same)
    recorded_mixed = grow(host, seed_mixed)
    recorded_one = grow(host, seed_one)

    mask_occupancy = origin_six_mask(recorded_same, exact_tick=None)
    mask_formed = origin_six_mask(recorded_same, exact_tick=1)
    t_a = probe_tick(recorded_same, PROBE_A)
    t_b = probe_tick(recorded_same, PROBE_B)
    t_c = probe_tick(recorded_same, PROBE_C)
    t_d = probe_tick(recorded_same, PROBE_D)
    times_defined = None not in (t_a, t_b, t_c, t_d)
    reverse_hold = (
        times_defined and t_a is not None and t_b is not None and 3 * t_a * t_a > t_b * t_b
    )
    face_hold = (
        times_defined and t_c is not None and t_d is not None and t_c * t_c > 2 * t_d * t_d
    )

    print("external_scientific_inputs: none; exact integer formation ticks only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("host: Euclidean B_3(0) with n·n<=9")
    print(f"host_site_count: {len(host)}")
    print("seed: {0,(0,1,0)} both locking +e_1 at tick 0")
    print(f"origin_tick1_6mask_occupancy: {mask_occupancy}")
    print(f"origin_tick1_6mask_formed_at_t_eq_1: {mask_formed}")
    print(f"t(A)={t_a} t(B)={t_b} t(C)={t_c} t(D)={t_d}")
    print(
        "reverse 3 t(A)^2 > t(B)^2: "
        + ("hold" if reverse_hold else ("fail" if times_defined else "undefined"))
    )
    print(
        "face t(C)^2 > 2 t(D)^2: "
        + ("hold" if face_hold else ("fail" if times_defined else "undefined"))
    )
    print("claim_boundary: displayed, not adopted; not written into Admissibility")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")

    declared = audit_paths_literal(self_source)
    checks.check(
        "audit-input-paths-literal",
        "AUDIT_INPUT_PATHS is the declared two-path static tuple",
        declared == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "docs/NNSEED_SAME_LOCK_E1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        host == wide_host and all(dot(site, site) <= 9 for site in host),
    )
    checks.check(
        "seed-two-site-same-lock",
        "tick-0 records are origin and (0,1,0), both locking +e_1",
        recorded_same[ORIGIN] == (0, frozenset({E1}))
        and recorded_same[E2] == (0, frozenset({E1}))
        and sum(time == 0 for time, _locks in recorded_same.values()) == 2,
    )
    checks.check(
        "thm1-origin-tick1-6mask",
        "origin occupancy 6-mask at tick 1 is (0,0,1,1,1,1)",
        mask_occupancy == (0, 0, 1, 1, 1, 1)
        and mask_formed == (0, 0, 0, 1, 1, 1)
        and "(0, 0, 1, 1, 1, 1)" in note,
    )
    checks.check(
        "thm1-probe-ticks-defined",
        "t(A), t(B), t(C), t(D) are defined integers",
        times_defined
        and all(isinstance(value, int) for value in (t_a, t_b, t_c, t_d)),
    )
    checks.check(
        "thm1-probe-ticks-reported",
        "note records the computed probe ticks",
        times_defined
        and f"t(A) = {t_a}" in note
        and f"t(B) = {t_b}" in note
        and f"t(C) = {t_c}" in note
        and f"t(D) = {t_d}" in note,
    )
    reverse_text = (
        f"{3 * t_a * t_a} > {t_b * t_b}" if times_defined else "undefined"
    )
    face_text = (
        f"{t_c * t_c} > {2 * t_d * t_d} is false" if times_defined else "undefined"
    )
    checks.check(
        "thm2-reverse-hold",
        "3 t(A)^2 > t(B)^2 holds",
        reverse_hold and reverse_text in note,
    )
    checks.check(
        "thm3-face-fail",
        "t(C)^2 > 2 t(D)^2 fails and is displayed, not adopted",
        (not face_hold)
        and times_defined
        and face_text in note
        and "Displayed, not adopted." in note,
    )
    one_mask_formed = origin_six_mask(recorded_one, exact_tick=1)
    one_t_d = probe_tick(recorded_one, PROBE_D)
    one_t_b = probe_tick(recorded_one, PROBE_B)
    checks.check(
        "not-one-site-letter-clone",
        "one-site +e_1 seed differs in tick-1 +e_2 occupancy and probe ticks",
        one_mask_formed == (0, 0, 1, 1, 1, 1)
        and mask_formed != one_mask_formed
        and one_t_d != t_d
        and one_t_b != t_b,
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
    mixed_t = (
        probe_tick(recorded_mixed, PROBE_A),
        probe_tick(recorded_mixed, PROBE_B),
        probe_tick(recorded_mixed, PROBE_C),
        probe_tick(recorded_mixed, PROBE_D),
    )
    checks.check(
        "not-mixed-cubic-orbit",
        "same-lock seed is outside the proper cubic orbit of mixed +e_1/+e_2",
        (not mixed_orbit)
        and len(proper_cubic_rotations()) == 24
        and mixed_t != (t_a, t_b, t_c, t_d)
        and seed_same[0][1] == seed_same[1][1]
        and seed_mixed[0][1] != seed_mixed[1][1],
    )
    origin_parallel_blocked = all(
        recorded_same[ORIGIN][0] + 1
        != probe_tick(recorded_same, add(ORIGIN, step))
        for step in (E1, (-1, 0, 0))
    )
    checks.check(
        "perp-step-incoming-lock",
        "origin lock +e_1 blocks parallel steps and allows the four perpendicular steps",
        origin_parallel_blocked
        and probe_tick(recorded_same, (0, -1, 0)) == 1
        and probe_tick(recorded_same, E3) == 1
        and probe_tick(recorded_same, (0, 0, -1)) == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    claim_scope = (
        "Perp-step incoming-lock formation-tick reverse and face at k=1 on "
        "Euclidean B_3(0) with two-site seed {0,(0,1,0)} both locking +e_1 "
        "are reported. Displayed, not adopted."
    )
    checks.check(
        "note-claim-scope",
        "note claim_scope matches the displayed k=1 reverse/face report",
        claim_scope in note,
    )
    checks.check(
        "no-admissibility-write",
        "display is not written into Admissibility and names no extra axiom",
        "not written into Admissibility" in note
        and "hypothetical_axiom_status: \"none;" in note
        and "Admissibility / Local Constraint" in axiom,
    )
    checks.check(
        "forbidden-phrases-absent",
        "note omits excluded claim language and does not attach a first-lemma tag",
        "L" + "1" not in note
        and "par" + "nn" not in note
        and "k" + "20" not in note
        and "G_" + "N" not in note
        and "1/" + "r" not in note
        and "Lattice" + "-named" not in note
        and "not a " + "TOE" not in note,
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

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
