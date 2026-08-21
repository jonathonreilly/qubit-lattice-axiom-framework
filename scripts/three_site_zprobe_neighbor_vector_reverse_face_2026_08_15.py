#!/usr/bin/env python3
"""Unique already-recorded 6-NN lock-vector reverse/face on three-site z-probes.

Host: Euclidean integer ball B_3(0)={n:n·n<=9}. Seed and perp-step grow are
the three-site opposite-lock process. Incoming-step uniqueness is not
required. Reverse and face are displayed, not adopted. No cache or
governance surface is written.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "THREE_SITE_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THREE_SITE_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
ORIGIN: Point = (0, 0, 0)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
UNIT = frozenset(NN)

PROBE_A: Point = (0, 0, 1)
PROBE_B: Point = (1, 1, 1)
PROBE_C: Point = (0, 0, 2)
PROBE_D: Point = (1, 0, 1)
X_PROBE_A: Point = (1, 0, 0)
X_PROBE_C: Point = (2, 0, 0)
Y_PROBE_A: Point = (0, 1, 0)
Y_PROBE_C: Point = (0, 2, 0)

SEED: dict[Point, Point] = {
    ORIGIN: E1,
    (0, 1, 0): NEG_E1,
    (1, 0, 0): E2,
}


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def in_ball(point: Point) -> bool:
    return dot(point, point) <= 9


def integer_ball() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if x * x + y * y + z * z <= 9
    )


def axis(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def allowed_steps(locks: frozenset[Point]) -> frozenset[Point]:
    steps: set[Point] = set()
    for lock in locks:
        ei = axis(lock)
        for step in NN:
            if dot(step, ei) == 0:
                steps.add(step)
    return frozenset(steps)


def letter_name(vector: Point) -> str:
    axis_index = next(i for i, component in enumerate(vector) if component)
    sign = "+" if vector[axis_index] > 0 else "-"
    return f"{sign}e_{axis_index + 1}"


def grow() -> dict[Point, dict[str, object]]:
    recorded: dict[Point, dict[str, object]] = {
        site: {"t": 0, "locks": frozenset({lock})} for site, lock in SEED.items()
    }
    for tick in range(0, 16):
        proposals: dict[Point, list[tuple[Point, Point]]] = defaultdict(list)
        for site, info in recorded.items():
            if info["t"] != tick:
                continue
            locks = info["locks"]
            assert isinstance(locks, frozenset)
            for step in allowed_steps(locks):
                child = add(site, step)
                if not in_ball(child) or child in recorded:
                    continue
                proposals[child].append((site, step))
        if not proposals:
            continue
        for child, parents in proposals.items():
            recorded[child] = {
                "t": tick + 1,
                "locks": frozenset(step for _, step in parents),
                "parents": tuple(parents),
            }
    return recorded


def already_recorded_neighbors(
    site: Point, recorded: dict[Point, dict[str, object]]
) -> tuple[Point, ...]:
    tick = recorded[site]["t"]
    assert isinstance(tick, int)
    out: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in recorded:
            continue
        neighbor_tick = recorded[neighbor]["t"]
        assert isinstance(neighbor_tick, int)
        if tick == 0:
            if neighbor_tick == 0 and neighbor != site:
                out.append(neighbor)
        elif neighbor_tick < tick:
            out.append(neighbor)
    return tuple(out)


def neighbor_lock_list(
    site: Point, recorded: dict[Point, dict[str, object]]
) -> tuple[Point, ...]:
    locks: list[Point] = []
    for neighbor in already_recorded_neighbors(site, recorded):
        neighbor_locks = recorded[neighbor]["locks"]
        assert isinstance(neighbor_locks, frozenset)
        locks.extend(sorted(neighbor_locks))
    return tuple(locks)


def unique_letter(lock_list: tuple[Point, ...]) -> Point | None:
    unique = set(lock_list)
    if len(unique) == 1:
        vector = next(iter(unique))
        if vector in UNIT:
            return vector
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    source = Path(__file__).read_text(encoding="utf-8")
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    recorded = grow()
    ball = integer_ball()

    letter_a = unique_letter(neighbor_lock_list(PROBE_A, recorded))
    letter_b = unique_letter(neighbor_lock_list(PROBE_B, recorded))
    letter_c = unique_letter(neighbor_lock_list(PROBE_C, recorded))
    letter_d = unique_letter(neighbor_lock_list(PROBE_D, recorded))
    list_a = neighbor_lock_list(PROBE_A, recorded)
    list_b = neighbor_lock_list(PROBE_B, recorded)
    list_c = neighbor_lock_list(PROBE_C, recorded)
    list_d = neighbor_lock_list(PROBE_D, recorded)
    neigh_a = already_recorded_neighbors(PROBE_A, recorded)
    neigh_b = already_recorded_neighbors(PROBE_B, recorded)
    neigh_c = already_recorded_neighbors(PROBE_C, recorded)
    neigh_d = already_recorded_neighbors(PROBE_D, recorded)

    reverse_defined = letter_a is not None and letter_b is not None
    reverse_hold = reverse_defined and add(letter_a, letter_b) == ORIGIN
    reverse_status = (
        "hold" if reverse_hold else ("fail" if reverse_defined else "UNDEFINED")
    )
    face_defined = letter_c is not None and letter_d is not None
    face_hold = face_defined and add(letter_c, letter_d) == ORIGIN
    face_status = "hold" if face_hold else ("fail" if face_defined else "UNDEFINED")

    print("host: Euclidean B_3(0)={n:n·n<=9}")
    print("seed t=0: 0 lock +e_1, (0,1,0) lock -e_1, (1,0,0) lock +e_2")
    print(
        "T1 A",
        PROBE_A,
        "t",
        recorded[PROBE_A]["t"],
        "neighbors",
        neigh_a,
        "locks",
        tuple(letter_name(v) for v in list_a),
        "letter",
        letter_name(letter_a) if letter_a is not None else "UNDEFINED",
    )
    print(
        "T1 B",
        PROBE_B,
        "t",
        recorded[PROBE_B]["t"],
        "neighbors",
        neigh_b,
        "locks",
        tuple(letter_name(v) for v in list_b),
        "letter",
        letter_name(letter_b) if letter_b is not None else "UNDEFINED",
    )
    print(
        "T1 C",
        PROBE_C,
        "t",
        recorded[PROBE_C]["t"],
        "neighbors",
        neigh_c,
        "locks",
        tuple(letter_name(v) for v in list_c),
        "letter",
        letter_name(letter_c) if letter_c is not None else "UNDEFINED",
    )
    print(
        "T1 D",
        PROBE_D,
        "t",
        recorded[PROBE_D]["t"],
        "neighbors",
        neigh_d,
        "locks",
        tuple(letter_name(v) for v in list_d),
        "letter",
        "UNDEFINED" if letter_d is None else letter_name(letter_d),
    )
    print("T2 reverse", reverse_status)
    print("T3 face", face_status)

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the note and current axiom",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_SITE_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n    "docs/THREE_SITE_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )
    checks.check(
        "euclidean-ball",
        "host is the integer Euclidean ball of squared radius 9 with 123 sites",
        len(ball) == 123
        and all(in_ball(site) for site in ball)
        and all(dot(site, site) <= 9 for site in recorded)
        and max(dot(site, site) for site in recorded) <= 9,
    )
    checks.check(
        "three-site-seed",
        "tick-0 records are origin +e_1, (0,1,0) -e_1, and (1,0,0) +e_2",
        recorded[ORIGIN]["t"] == 0
        and recorded[ORIGIN]["locks"] == frozenset({E1})
        and recorded[Y_PROBE_A]["t"] == 0
        and recorded[Y_PROBE_A]["locks"] == frozenset({NEG_E1})
        and recorded[X_PROBE_A]["t"] == 0
        and recorded[X_PROBE_A]["locks"] == frozenset({E2})
        and sum(1 for info in recorded.values() if info["t"] == 0) == 3,
    )
    checks.check(
        "z-probes-not-x-or-y-lists",
        "the four z-probes are A=(0,0,1), B=(1,1,1), C=(0,0,2), D=(1,0,1)",
        PROBE_A == (0, 0, 1)
        and PROBE_B == (1, 1, 1)
        and PROBE_C == (0, 0, 2)
        and PROBE_D == (1, 0, 1)
        and PROBE_A != X_PROBE_A
        and PROBE_A != Y_PROBE_A
        and PROBE_C != X_PROBE_C
        and PROBE_C != Y_PROBE_C
        and letter_c == E3
        and letter_c != E2
        and letter_c != NEG_E1
        and letter_d == E2,
    )
    checks.check(
        "probe-A-not-seed",
        "A is not a seed; its already-recorded 6-NN is the origin at tick 0",
        PROBE_A not in SEED
        and recorded[PROBE_A]["t"] == 1
        and neigh_a == (ORIGIN,)
        and list_a == (E1,)
        and letter_a == E1,
    )
    checks.check(
        "probe-B-unique-e3",
        "B forms at tick 2 with already-recorded neighbor locks both +e_3",
        recorded[PROBE_B]["t"] == 2
        and set(neigh_b) == {(0, 1, 1), (1, 0, 1)}
        and list_b == (E3, E3)
        and letter_b == E3,
    )
    checks.check(
        "probe-C-unique-e3",
        "C forms at tick 4 with unique already-recorded neighbor lock +e_3",
        recorded[PROBE_C]["t"] == 4
        and neigh_c == ((-1, 0, 2), (0, -1, 2), PROBE_A)
        and list_c == (E3, E3, E3)
        and letter_c == E3,
    )
    checks.check(
        "probe-D-unique-e2",
        "D forms at tick 1 with unique already-recorded neighbor lock +e_2",
        recorded[PROBE_D]["t"] == 1
        and neigh_d == (X_PROBE_A,)
        and list_d == (E2,)
        and letter_d == E2,
    )
    checks.check(
        "incoming-uniqueness-not-required",
        "B and C are occupied with two distinct incoming steps, yet neighbor letters are unique",
        recorded[PROBE_B]["locks"] == frozenset({E1, E2})
        and letter_b == E3
        and recorded[PROBE_C]["locks"] == frozenset({E1, E2})
        and letter_c == E3,
    )
    checks.check(
        "reverse-fail",
        "reverse is defined and fails: +e_1 + +e_3 is not zero",
        reverse_status == "fail"
        and letter_a == E1
        and letter_b == E3
        and add(E1, E3) != ORIGIN,
    )
    checks.check(
        "face-fail",
        "face is defined and fails: +e_3 + +e_2 is not zero",
        face_status == "fail"
        and letter_c == E3
        and letter_d == E2
        and add(E3, E2) != ORIGIN,
    )
    checks.check(
        "note-reports-letters",
        "the note reports the four computed letters and reverse/face statuses",
        "unique letter `+e_1`" in note
        and "unique letter `+e_3`" in note
        and "unique letter `+e_2`" in note
        and "reverse fails" in note
        and "face fails" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "reverse and face are displayed and not adopted into Admissibility",
        "Displayed, not adopted." in note
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "claim-scope",
        "the note claim_scope matches the reported unique-vector reverse/face display",
        'claim_scope: "Reverse and face from unique already-recorded 6-NN lock '
        "vectors on the four z-probes of the three-site opposite-lock seed are "
        'reported. Displayed, not adopted."' in note,
    )
    checks.check(
        "not-x-y-leftover-not-two-site",
        "C is +e_3 and D is +e_2 on three-site z-probes, not x/y leftovers or two-site nsopz",
        "not a copied x-probe remainder" in note
        and "not a copied y-probe remainder" in note
        and "not the two-site opposite-lock z-probes" in note
        and letter_c == E3
        and letter_d == E2
        and face_status == "fail"
        and sum(1 for info in recorded.values() if info["t"] == 0) == 3,
    )
    axiom_flat = " ".join(axiom.split())
    checks.check(
        "axiom-boundary",
        "Lattice nearest-neighbor wording is read and the axiom file is not rewritten",
        "nearest-neighbor adjacency" in axiom_flat
        and "There is one fixed nearest-neighbor admissibility rule" in axiom_flat
        and "When present, a record locks exactly one admissible local possibility."
        in axiom_flat,
    )
    checks.check(
        "hygiene-forbidden-phrases",
        "note omits forbidden gravity, coinage, search, and projector phrases",
        all(
            phrase not in note
            for phrase in (
                "G_N",
                "1/r^2",
                "1/r",
                "Lattice-named",
                "not a TOE",
                "Dijkstra",
                "Gram",
                "P_+",
            )
        )
        and "B_4" not in note
        and "n·n<=16" not in note
        and "n·n<=10" not in note,
    )
    checks.check(
        "no-l1-attachment",
        "the note does not attach an L1 rule and names no larger ball",
        "attach L1" in note
        and "Admissibility" in note
        and "B_3(0)" in note
        and "{n:n·n<=9}" in note.replace(" ", ""),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
