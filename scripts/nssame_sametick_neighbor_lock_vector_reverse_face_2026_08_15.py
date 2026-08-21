#!/usr/bin/env python3
"""Unique lock vector from same-tick-inclusive 6-NN locks on four nssame probes.

Host Euclidean B_3(0) = {n in Z^3 : n·n <= 9}. Seed at tick 0 records the
origin and (0,1,0), both locking +e_1. Growth is the nssame perp-step
incoming-lock process. At each probe's formation tick, collect locks of 6-NN
that formed at tick <= t(q) and are not q (same-tick partner counts). If that
set of lock vectors is a singleton {v} subset {±e_i}, the unique letter is v;
otherwise UNDEFINED. Reverse holds iff L(A) and L(B) are defined and
L(A)+L(B)=(0,0,0). Face holds iff L(C) and L(D) are defined and
L(C)+L(D)=(0,0,0). Occupancy n is not used. The probe's own incoming lock is
not used. Uniqueness of incoming locks is not required. Not the
strictly-earlier leftover of unique already-recorded 6-NN lock vectors.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NSSAME_SAMETICK_NEIGHBOR_LOCK_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NSSAME_SAMETICK_NEIGHBOR_LOCK_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
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
AXIS_LOCKS = frozenset(STEPS)
PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
Y_PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
Z_PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (0, 1, 1),
}
LOCK_NAME = {
    E1: "+e_1",
    (-1, 0, 0): "−e_1",
    E2: "+e_2",
    (0, -1, 0): "−e_2",
    E3: "+e_3",
    (0, 0, -1): "−e_3",
}
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "16-census",
    "16-letter",
    "L1",
    "Runner cache",
    "n_μ",
    "3 t(",
    "t(C)^2",
)
CLAIM_SCOPE = (
    "Reverse and face from the unique same-tick-inclusive 6-NN lock "
    "vector on the four nssame probes are reported. Displayed, not adopted."
)
SEED_SAME: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
SEED_MIXED: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)


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


def normalize(text: str) -> str:
    return " ".join(text.split())


def unique_vector_from_neighbor_locks(locks: tuple[Point, ...]) -> Letter:
    """Unique vector if recorded-neighbor locks are one vector in {±e_i}."""
    if not locks:
        return "UNDEFINED"
    unique = set(locks)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in AXIS_LOCKS:
        return "UNDEFINED"
    return vector


def reverse_report(letter_a: Letter, letter_b: Letter) -> str:
    """Reverse iff L(A)+L(B)=(0,0,0). UNDEFINED if a needed letter is UNDEFINED."""
    if letter_a == "UNDEFINED" or letter_b == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter_a, tuple) or not isinstance(letter_b, tuple):
        return "UNDEFINED"
    holds = add(letter_a, letter_b) == ORIGIN
    return "hold" if holds else "fail"


def face_report(letter_c: Letter, letter_d: Letter) -> str:
    """Face iff L(C)+L(D)=(0,0,0). UNDEFINED if a needed letter is UNDEFINED."""
    if letter_c == "UNDEFINED" or letter_d == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter_c, tuple) or not isinstance(letter_d, tuple):
        return "UNDEFINED"
    holds = add(letter_c, letter_d) == ORIGIN
    return "hold" if holds else "fail"


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def letter_display(letter: Letter) -> str:
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter, tuple):
        return "UNDEFINED"
    return lock_display(letter)


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


def recorded_neighbor_locks(
    site: Point,
    recorded: dict[Point, tuple[int, frozenset[Point]]],
) -> tuple[tuple[Point, Point], ...]:
    """Locks of 6-NN formed at tick <= t(q), excluding q (same-tick counts)."""
    formation = recorded[site][0]
    pairs: list[tuple[Point, Point]] = []
    for step in STEPS:
        neighbor = add(site, step)
        if neighbor not in recorded:
            continue
        if neighbor == site:
            continue
        neighbor_tick, locks = recorded[neighbor]
        if neighbor_tick > formation:
            continue
        for lock in sorted(locks):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def strictly_earlier_neighbor_locks(
    site: Point,
    recorded: dict[Point, tuple[int, frozenset[Point]]],
) -> tuple[tuple[Point, Point], ...]:
    """Strictly-earlier leftover collector, used only as a refused contrast."""
    formation = recorded[site][0]
    pairs: list[tuple[Point, Point]] = []
    for step in STEPS:
        neighbor = add(site, step)
        if neighbor not in recorded:
            continue
        neighbor_tick, locks = recorded[neighbor]
        if neighbor_tick >= formation:
            continue
        for lock in sorted(locks):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def assignment_string_tuple(tree: ast.AST, name: str) -> tuple[str, ...] | None:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    value = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    return None
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

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("unique lock vector from same-tick-inclusive 6-NN locks reverse/face")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths-literal",
        literal_paths == AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
        str(literal_paths),
    )
    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    host = euclidean_ball()
    probe_sites = tuple(PROBES[name] for name in ("A", "B", "C", "D"))
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    wide_host = frozenset(
        (x, y, z)
        for x, y, z in product(range(-4, 5), repeat=3)
        if x * x + y * y + z * z <= 9
    )
    checks.check(
        "host-euclidean-ball",
        host == wide_host
        and ORIGIN in host
        and len(host) == 123
        and all(dot(site, site) <= 9 for site in host),
    )
    checks.check(
        "four-x-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
    )
    checks.check(
        "x-probes-are-not-y-or-z-probes",
        probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and y_probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and z_probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (0, 1, 1)),
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and dot(E1, E2) == 0
        and dot(E1, lock_axis(E1)) == 1
        and add(E1, (-1, 0, 0)) == ORIGIN
        and PROBES["C"] in host
        and add((4, 0, 0), ORIGIN) not in host,
    )
    checks.check(
        "unique-vector-identity-from-neighbor-locks",
        unique_vector_from_neighbor_locks((E1,)) == E1
        and unique_vector_from_neighbor_locks((E1, E1)) == E1
        and unique_vector_from_neighbor_locks((E2,)) == E2
        and unique_vector_from_neighbor_locks(((0, -1, 0),)) == (0, -1, 0)
        and unique_vector_from_neighbor_locks((E1, E2)) == "UNDEFINED"
        and unique_vector_from_neighbor_locks((E1, E3)) == "UNDEFINED"
        and unique_vector_from_neighbor_locks((E1, (-1, 0, 0))) == "UNDEFINED"
        and unique_vector_from_neighbor_locks((E2, E2, E2)) == E2
        and unique_vector_from_neighbor_locks(()) == "UNDEFINED",
    )
    checks.check(
        "named-sign-same-plus-is-not-unique-vector",
        unique_vector_from_neighbor_locks((E1, E3)) == "UNDEFINED"
        and unique_vector_from_neighbor_locks((E1,)) == E1
        and unique_vector_from_neighbor_locks((E3,)) == E3,
    )
    checks.check(
        "reverse-face-hold-fail-undefined",
        reverse_report(E1, (-1, 0, 0)) == "hold"
        and reverse_report(E1, E3) == "fail"
        and reverse_report(E1, E1) == "fail"
        and reverse_report("UNDEFINED", E3) == "UNDEFINED"
        and reverse_report(E1, "UNDEFINED") == "UNDEFINED"
        and reverse_report("UNDEFINED", "UNDEFINED") == "UNDEFINED"
        and face_report(E3, (0, 0, -1)) == "hold"
        and face_report(E1, E3) == "fail"
        and face_report("UNDEFINED", E1) == "UNDEFINED"
        and face_report(E3, "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", "UNDEFINED") == "UNDEFINED",
    )

    recorded = grow(host, SEED_SAME)
    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    letters: dict[str, Letter] = {}
    leftover_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    leftover_letters: dict[str, Letter] = {}
    for name, site in PROBES.items():
        pairs = recorded_neighbor_locks(site, recorded)
        neighbor_lists[name] = pairs
        letter = unique_vector_from_neighbor_locks(tuple(lock for _n, lock in pairs))
        letters[name] = letter
        leftover = strictly_earlier_neighbor_locks(site, recorded)
        leftover_lists[name] = leftover
        leftover_letters[name] = unique_vector_from_neighbor_locks(
            tuple(lock for _n, lock in leftover)
        )
        lock_text = ", ".join(
            f"{lock_display(lock)} at {neighbor}" for neighbor, lock in pairs
        )
        incoming = ",".join(
            lock_display(step) for step in sorted(recorded[site][1])
        )
        print(
            f"{name} t={recorded[site][0]} recorded-neighbor-locks=[{lock_text}] "
            f"L={letter_display(letter)} incoming={incoming}"
        )

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    leftover_reverse = reverse_report(leftover_letters["A"], leftover_letters["B"])
    leftover_face = face_report(leftover_letters["C"], leftover_letters["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: unique letter is the singleton same-tick-inclusive "
        "six-neighbor lock vector in {±e_i}, else UNDEFINED"
    )
    print(
        "per_site: scored only at probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four unique lock vectors plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    checks.check(
        "theorem1-A-neighbor-lock-list-and-vector",
        neighbor_lists["A"]
        == (
            (ORIGIN, E1),
            (PROBES["D"], (0, -1, 0)),
            (PROBES["D"], (0, 0, -1)),
            (PROBES["D"], E3),
            ((1, -1, 0), E1),
            ((1, 0, 1), E1),
            ((1, 0, -1), E1),
        )
        and letters["A"] == "UNDEFINED",
        str((neighbor_lists["A"], letters["A"])),
    )
    checks.check(
        "theorem1-B-neighbor-lock-list-and-vector",
        neighbor_lists["B"]
        == (((0, 1, 1), E3), ((1, 0, 1), E1))
        and letters["B"] == "UNDEFINED",
        str((neighbor_lists["B"], letters["B"])),
    )
    checks.check(
        "theorem1-C-neighbor-lock-list-and-vector",
        neighbor_lists["C"]
        == (
            (PROBES["A"], (0, 0, -1)),
            (PROBES["A"], E3),
            (PROBES["A"], E2),
            ((2, 1, 0), E1),
        )
        and letters["C"] == "UNDEFINED",
        str((neighbor_lists["C"], letters["C"])),
    )
    checks.check(
        "theorem1-D-neighbor-lock-list-and-vector",
        neighbor_lists["D"]
        == (
            (E2, E1),
            ((1, 2, 0), E1),
            (PROBES["A"], (0, 0, -1)),
            (PROBES["A"], E3),
            (PROBES["A"], E2),
            (PROBES["B"], E1),
            ((1, 1, -1), E1),
        )
        and letters["D"] == "UNDEFINED",
        str((neighbor_lists["D"], letters["D"])),
    )
    checks.check(
        "theorem1-vectors-all-undefined",
        letters["A"] == "UNDEFINED"
        and letters["B"] == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED",
    )
    checks.check(
        "theorem1-formation-ticks",
        recorded[PROBES["A"]][0] == 3
        and recorded[PROBES["B"]][0] == 2
        and recorded[PROBES["C"]][0] == 4
        and recorded[PROBES["D"]][0] == 3,
    )
    checks.check(
        "theorem1-A-same-tick-partner-is-D",
        recorded[PROBES["A"]][0] == recorded[PROBES["D"]][0]
        and PROBES["D"] in {neighbor for neighbor, _lock in neighbor_lists["A"]}
        and PROBES["A"] in {neighbor for neighbor, _lock in neighbor_lists["D"]},
    )
    checks.check(
        "theorem1-B-mixed-vectors-include-same-tick",
        letters["B"] == "UNDEFINED"
        and {lock for _n, lock in neighbor_lists["B"]} == {E1, E3}
        and ((1, 0, 1), E1) in neighbor_lists["B"]
        and recorded[(1, 0, 1)][0] == recorded[PROBES["B"]][0],
    )
    checks.check(
        "theorem2-reverse-undefined",
        reverse_status == "UNDEFINED"
        and letters["A"] == "UNDEFINED"
        and letters["B"] == "UNDEFINED"
        and reverse_status != "hold"
        and reverse_status != "fail",
        reverse_status,
    )
    checks.check(
        "theorem3-face-undefined",
        face_status == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED"
        and face_status != "hold"
        and face_status != "fail",
        face_status,
    )
    checks.check(
        "not-probe-own-incoming-lock",
        recorded[PROBES["A"]][1] == frozenset({E2, E3, (0, 0, -1)})
        and unique_vector_from_neighbor_locks(tuple(sorted(recorded[PROBES["A"]][1])))
        == "UNDEFINED"
        and recorded[PROBES["B"]][1] == frozenset({E1})
        and unique_vector_from_neighbor_locks(tuple(sorted(recorded[PROBES["B"]][1])))
        == E1
        and letters["B"] != E1
        and recorded[PROBES["D"]][1] == frozenset({(0, -1, 0), E3, (0, 0, -1)}),
    )
    checks.check(
        "incoming-locks-are-nn-steps-not-letters",
        all(recorded[PROBES[name]][1] <= set(STEPS) for name in ("A", "B", "C", "D"))
        and all(
            letters[name] in AXIS_LOCKS or letters[name] == "UNDEFINED"
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        len(recorded[PROBES["A"]][1]) == 3
        and len(recorded[PROBES["D"]][1]) == 3
        and letters["A"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED",
        str(sorted(recorded[PROBES["A"]][1])),
    )
    checks.check(
        "two-site-same-lock-seed",
        recorded[ORIGIN] == (0, frozenset({E1}))
        and recorded[E2] == (0, frozenset({E1}))
        and sum(time == 0 for time, _locks in recorded.values()) == 2,
    )
    checks.check(
        "recorded-not-self-or-later-same-tick-included",
        all(
            neighbor != PROBES[name]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        )
        and all(
            recorded[neighbor][0] <= recorded[PROBES[name]][0]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        )
        and any(
            recorded[neighbor][0] == recorded[PROBES[name]][0]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        ),
    )
    checks.check(
        "not-strictly-earlier-leftover",
        leftover_letters["A"] == E1
        and leftover_letters["B"] == E3
        and leftover_letters["C"] == "UNDEFINED"
        and leftover_letters["D"] == E1
        and leftover_reverse == "fail"
        and leftover_face == "UNDEFINED"
        and letters["A"] != leftover_letters["A"]
        and letters["B"] != leftover_letters["B"]
        and letters["D"] != leftover_letters["D"]
        and reverse_status != leftover_reverse
        and leftover_lists["B"] == (((0, 1, 1), E3),)
        and ((1, 0, 1), E1) not in leftover_lists["B"],
    )
    checks.check(
        "formation-stays-in-host",
        set(recorded) <= host,
    )
    checks.check(
        "no-larger-ball",
        all(dot(site, site) <= 9 for site in recorded)
        and "No larger host is used." in normalized_note,
    )
    origin_parallel_blocked = all(
        recorded[ORIGIN][0] + 1
        != recorded.get(add(ORIGIN, step), (None, frozenset()))[0]
        for step in (E1, (-1, 0, 0))
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and recorded[(0, -1, 0)][0] == 1
        and recorded[E3][0] == 1
        and recorded[(0, 0, -1)][0] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    same_seed_locks = frozenset(SEED_SAME)
    mixed_orbit = False
    for matrix in proper_cubic_rotations():
        image = frozenset(
            (apply_matrix(matrix, site), apply_matrix(matrix, lock))
            for site, lock in SEED_MIXED
        )
        if image == same_seed_locks:
            mixed_orbit = True
            break
    checks.check(
        "not-mixed-cubic-orbit",
        (not mixed_orbit)
        and len(proper_cubic_rotations()) == 24
        and SEED_SAME[0][1] == SEED_SAME[1][1]
        and SEED_MIXED[0][1] != SEED_MIXED[1][1],
    )
    checks.check(
        "no-sixteen-combo-census",
        letters["A"] == "UNDEFINED"
        and letters["B"] == "UNDEFINED"
        and letters["C"] == "UNDEFINED"
        and letters["D"] == "UNDEFINED"
        and reverse_status == "UNDEFINED"
        and face_status == "UNDEFINED"
        and reverse_status != "some"
        and face_status != "some",
    )
    checks.check(
        "mutation-empty-neighbor-locks-undefined",
        unique_vector_from_neighbor_locks(()) == "UNDEFINED"
        and reverse_report("UNDEFINED", E3) == "UNDEFINED"
        and face_report(letters["C"], "UNDEFINED") == "UNDEFINED",
    )
    checks.check(
        "mutation-mixed-neighbor-vectors-undefined",
        unique_vector_from_neighbor_locks((E1, E2)) == "UNDEFINED"
        and unique_vector_from_neighbor_locks((E1, (0, -1, 0))) == "UNDEFINED"
        and unique_vector_from_neighbor_locks((E1, E3)) == "UNDEFINED"
        and face_report("UNDEFINED", E1) == "UNDEFINED",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-neighbor-lock-lists-and-vectors",
        "L(A) = UNDEFINED" in note
        and "L(B) = UNDEFINED" in note
        and "L(C) = UNDEFINED" in note
        and "L(D) = UNDEFINED" in note
        and "+e_1 at (0, 0, 0)" in note
        and "−e_2 at (1, 1, 0)" in note
        and "−e_3 at (1, 1, 0)" in note
        and "+e_3 at (1, 1, 0)" in note
        and "+e_1 at (1, -1, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "+e_1 at (1, 0, 1)" in note
        and "−e_3 at (1, 0, 0)" in note
        and "+e_3 at (1, 0, 0)" in note
        and "+e_2 at (1, 0, 0)" in note
        and "+e_1 at (2, 1, 0)" in note
        and "+e_1 at (0, 1, 0)" in note
        and "+e_1 at (1, 2, 0)" in note
        and "+e_1 at (1, 1, 1)" in note
        and "+e_1 at (1, 1, -1)" in note,
    )
    checks.check(
        "note-reports-undefined-undefined",
        note.count("Report: `UNDEFINED`.") == 2
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "note-does-not-use-occupancy-or-incoming",
        "does not use occupancy" in normalized_note
        and "does not use the probe" in normalized_note
        and "own incoming lock" in normalized_note,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "not identified" in normalized_note
        and "incoming step" in normalized_note,
    )
    checks.check(
        "note-not-unique-fn-or-ndot",
        "not unique `f(n)`" in note and "not ndot" in note,
    )
    checks.check(
        "note-not-strictly-earlier-leftover",
        "not the strictly-earlier leftover" in normalized_note
        and "unique *vector*" in note
        and "same-tick" in note
        and leftover_reverse == "fail"
        and reverse_status == "UNDEFINED",
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from same-tick-inclusive six-neighbor lock vectors"
        in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-not-sixteen-free-letters",
        "not a sixteen-combination free lettering" in normalized_note
        and "16-census" not in note
        and "16-letter" not in note,
    )
    checks.check(
        "note-not-tick-or-occupancy-reprint",
        "3 t(" not in note
        and "t(C)^2" not in note
        and "n_μ" not in note
        and "not a unique letter of occupancy" in normalized_note,
    )
    checks.check(
        "note-not-x-or-z-confusion",
        "same x-probes" in normalized_note
        and "not the y-probes" in normalized_note
        and "not the z-probes" in normalized_note
        and "A = (1,0,0)" in note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS),
    )
    checks.check(
        "axiom-record-sentences-current",
        "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "does not supply the formation site, probability, or rate"
        in normalized_axiom,
    )
    checks.check(
        "note-quotes-current-premises",
        "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "does not supply the formation site, probability, or rate"
        in normalized_note,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        'hypothetical_axiom_status: "no edit"' in note
        and "claim_type: bounded_theorem" in note
        and "authors no audit verdict" in normalized_note
        and "FAIL / DO NOT SHIP" in note,
    )
    checks.check(
        "note-n-gates-present",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-no-author-retained-verdict",
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/NSSAME_SAMETICK_NEIGHBOR_LOCK_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def unique_vector_from_neighbor_locks(" in source
        and "def recorded_neighbor_locks(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def grow(" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-vector-from-neighbor-locks-only",
        "unique_vector_from_neighbor_locks" in defined_fns
        and "recorded_neighbor_locks" in defined_fns
        and "named_sign" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and not any("ndot" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-tick",
        "by_tick" in source
        and "lock_axis" in source
        and "arrivals" in source
        and set(recorded) <= host,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
