#!/usr/bin/env python3
"""Unique neighbor-lock vector reverse/face on opposite-lock z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. At each z-probe's formation tick, collect locks of already-recorded
six-neighbors. If that set of lock vectors is a singleton {v} subset {±e_i},
the unique letter is v; otherwise UNDEFINED. Reverse holds iff L(A) and L(B)
are defined and L(A)+L(B)=(0,0,0). Face holds iff L(C) and L(D) are defined
and L(C)+L(D)=(0,0,0). Not leftover of the opposite-lock x-probe or y-probe
lists. Not named-sign lettering. Occupancy n is not used. The probe's own
incoming lock is not used. Formation ticks are not scored. Uniqueness of
incoming locks is not required. A is not a seed site. This seed is not a
cubic image of the perp two-site seed +e_1/+e_2.
"""

from __future__ import annotations

import ast
from collections import deque
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Letter = Point | str
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (E1, NEG_E1, E2, NEG_E2, E3, NEG_E3)
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (0, 1, 1),
}
X_PROBES = {
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
LOCK_NAME = {
    E1: "+e_1",
    NEG_E1: "−e_1",
    E2: "+e_2",
    NEG_E2: "−e_2",
    E3: "+e_3",
    NEG_E3: "−e_3",
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
    "f(n)",
    "ndot",
)
CLAIM_SCOPE = (
    "Reverse and face from unique already-recorded 6-NN lock "
    "vectors on the four z-probes of the opposite-lock two-site seed are "
    "reported. Displayed, not adopted."
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def in_ball(site: Point) -> bool:
    return dot(site, site) <= BALL_SQ


def ball_sites() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if in_ball((x, y, z))
    )


def perpendicular(lock: Point, step: Point) -> bool:
    return dot(lock, step) == 0


def normalize(text: str) -> str:
    return " ".join(text.split())


def named_sign(lock: Point) -> str:
    """Named sign of a lock vector. Contrast only; not the unique letter."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def unique_vector_letter(locks: tuple[Point, ...]) -> Letter:
    """Unique letter if recorded-neighbor lock vectors are a singleton in NN."""
    if not locks:
        return "UNDEFINED"
    unique = set(locks)
    if len(unique) != 1:
        return "UNDEFINED"
    vector = next(iter(unique))
    if vector not in NN:
        return "UNDEFINED"
    return vector


def comparison_report(left: Letter, right: Letter) -> str:
    """Hold iff both letters are defined lock vectors that sum to zero."""
    if left == "UNDEFINED" or right == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(left, tuple) or not isinstance(right, tuple):
        return "UNDEFINED"
    if add(left, right) == ZERO:
        return "hold"
    return "fail"


def reverse_report(letter_a: Letter, letter_b: Letter) -> str:
    """Reverse iff L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)."""
    return comparison_report(letter_a, letter_b)


def face_report(letter_c: Letter, letter_d: Letter) -> str:
    """Face iff L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)."""
    return comparison_report(letter_c, letter_d)


def letter_display(letter: Letter) -> str:
    if letter == "UNDEFINED":
        return "UNDEFINED"
    if not isinstance(letter, tuple):
        raise TypeError(f"letter is not a lock vector: {letter!r}")
    return LOCK_NAME[letter]


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    rotations: list[tuple[tuple[int, int, int], ...]] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = tuple(
                tuple(signs[row] if col == perm[row] else 0 for col in range(3))
                for row in range(3)
            )
            rotations.append(matrix)
    return tuple(rotations)


def apply_matrix(matrix: tuple[tuple[int, int, int], ...], vector: Point) -> Point:
    return tuple(sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3))  # type: ignore[return-value]


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


def form(
    seeds: tuple[tuple[Point, Point], ...] = TWO_SITE_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {site: 0 for site, _lock in seeds}
    locks: dict[Point, set[Point]] = {site: {lock} for site, lock in seeds}
    queue: deque[tuple[Point, int]] = deque((site, 0) for site, _lock in seeds)
    while queue:
        parent, parent_tick = queue.popleft()
        for lock in tuple(locks[parent]):
            for step in NN:
                if require_perp and not perpendicular(lock, step):
                    continue
                child = add(parent, step)
                if not in_ball(child):
                    continue
                next_tick = parent_tick + 1
                if child not in ticks:
                    ticks[child] = next_tick
                    locks[child] = {step}
                    queue.append((child, next_tick))
                elif ticks[child] == next_tick:
                    locks[child].add(step)
    return ticks, locks


def recorded_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Locks of already-recorded six-neighbors at the formation tick of site."""
    formation = ticks[site]
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        if ticks[neighbor] >= formation:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def probe_letters(
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    probes: dict[str, Point] | None = None,
) -> tuple[dict[str, tuple[tuple[Point, Point], ...]], dict[str, Letter]]:
    if probes is None:
        probes = PROBES
    neighbor_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    letters: dict[str, Letter] = {}
    for name, site in probes.items():
        pairs = recorded_neighbor_locks(site, ticks, locks)
        neighbor_lists[name] = pairs
        letters[name] = unique_vector_letter(tuple(lock for _n, lock in pairs))
    return neighbor_lists, letters


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

    print("unique neighbor-lock vector reverse/face on opposite-lock z-probes")
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

    host = ball_sites()
    probe_sites = tuple(PROBES[name] for name in ("A", "B", "C", "D"))
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-z-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (0, 1, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites,
    )
    checks.check(
        "z-probes-are-not-x-or-y-probes",
        probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and x_probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and y_probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0)),
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(NEG_E2, E2) == ZERO
        and add(E3, NEG_E1) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and perpendicular(NEG_E1, E2)
        and not perpendicular(E1, E1)
        and not perpendicular(NEG_E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "unique-vector-letter-identity",
        unique_vector_letter((E1,)) == E1
        and unique_vector_letter((E1, E1)) == E1
        and unique_vector_letter((NEG_E1,)) == NEG_E1
        and unique_vector_letter((NEG_E2,)) == NEG_E2
        and unique_vector_letter((E1, E2)) == "UNDEFINED"
        and unique_vector_letter((E1, E3)) == "UNDEFINED"
        and unique_vector_letter((E1, NEG_E1)) == "UNDEFINED"
        and unique_vector_letter((E2, NEG_E2)) == "UNDEFINED"
        and unique_vector_letter(()) == "UNDEFINED",
    )
    checks.check(
        "not-named-sign-reduction",
        unique_vector_letter((E1, E3)) == "UNDEFINED"
        and named_sign(E1) == named_sign(E3) == "+"
        and unique_vector_letter((NEG_E1, E1)) == "UNDEFINED"
        and named_sign(NEG_E1) != named_sign(E1)
        and unique_vector_letter((E3, NEG_E1)) == "UNDEFINED"
        and named_sign(E3) != named_sign(NEG_E1),
    )
    checks.check(
        "reverse-face-identity",
        reverse_report("UNDEFINED", NEG_E1) == "UNDEFINED"
        and reverse_report(E1, "UNDEFINED") == "UNDEFINED"
        and reverse_report(E1, NEG_E1) == "hold"
        and reverse_report(E1, E1) == "fail"
        and reverse_report(E1, E3) == "fail"
        and face_report(NEG_E2, E2) == "hold"
        and face_report(E2, NEG_E2) == "hold"
        and face_report(NEG_E2, NEG_E2) == "fail"
        and face_report(E3, NEG_E1) == "fail"
        and face_report("UNDEFINED", E2) == "UNDEFINED"
        and face_report(NEG_E3, "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", "UNDEFINED") == "UNDEFINED",
    )

    ticks, locks = form()
    same_ticks, _same_locks = form(SAME_SEEDS)
    neighbor_lists, letters = probe_letters(ticks, locks)
    x_neighbor_lists, x_letters = probe_letters(ticks, locks, X_PROBES)
    y_neighbor_lists, y_letters = probe_letters(ticks, locks, Y_PROBES)
    for name, site in PROBES.items():
        pairs = neighbor_lists[name]
        lock_text = ", ".join(
            f"{lock_display(lock)} at {neighbor}" for neighbor, lock in pairs
        )
        incoming = ",".join(lock_display(step) for step in sorted(locks[site]))
        print(
            f"{name} t={ticks[site]} recorded-neighbor-locks=[{lock_text}] "
            f"L={letter_display(letters[name])} incoming={incoming}"
        )

    reverse_status = reverse_report(letters["A"], letters["B"])
    face_status = face_report(letters["C"], letters["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: unique letter is the singleton already-recorded "
        "six-neighbor lock vector in {±e_i}, else UNDEFINED"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
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
        "theorem1-A-neighbor-lock-list-and-letter",
        neighbor_lists["A"] == ((ORIGIN, E1),) and letters["A"] == E1,
        str((neighbor_lists["A"], letters["A"])),
    )
    checks.check(
        "theorem1-A-not-seed-same-tick-D-not-recorded",
        ticks[PROBES["A"]] == 1
        and PROBES["A"] != E2
        and ticks[PROBES["D"]] == 1
        and PROBES["D"] not in {neighbor for neighbor, _lock in neighbor_lists["A"]}
        and PROBES["A"] not in {neighbor for neighbor, _lock in neighbor_lists["D"]}
        and letters["A"] == E1,
    )
    checks.check(
        "theorem1-B-neighbor-lock-list-and-letter",
        neighbor_lists["B"] == ((PROBES["D"], E3),) and letters["B"] == E3,
        str((neighbor_lists["B"], letters["B"])),
    )
    checks.check(
        "theorem1-C-neighbor-lock-list-and-letter",
        neighbor_lists["C"]
        == (
            ((1, 0, 2), E3),
            ((-1, 0, 2), E3),
            ((0, -1, 2), E3),
            (PROBES["A"], E3),
        )
        and letters["C"] == E3,
        str((neighbor_lists["C"], letters["C"])),
    )
    checks.check(
        "theorem1-D-neighbor-lock-list-and-letter",
        neighbor_lists["D"] == ((E2, NEG_E1),) and letters["D"] == NEG_E1,
        str((neighbor_lists["D"], letters["D"])),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 1,
    )
    checks.check(
        "theorem1-all-four-letters-defined",
        letters["A"] == E1
        and letters["B"] == E3
        and letters["C"] == E3
        and letters["D"] == NEG_E1
        and all(neighbor_lists[name] for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and letters["A"] == E1
        and letters["B"] == E3
        and add(E1, E3) != ZERO
        and reverse_status != "hold"
        and reverse_status != "UNDEFINED",
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and letters["C"] == E3
        and letters["D"] == NEG_E1
        and add(E3, NEG_E1) != ZERO
        and face_status != "hold"
        and face_status != "UNDEFINED",
        face_status,
    )
    checks.check(
        "not-leftover-of-x-probe-lists",
        probe_sites != x_probe_sites
        and letters != x_letters
        and x_letters["A"] == E1
        and x_letters["B"] == E3
        and x_letters["C"] == "UNDEFINED"
        and x_letters["D"] == "UNDEFINED"
        and neighbor_lists["A"] != x_neighbor_lists["A"]
        and neighbor_lists["C"] != x_neighbor_lists["C"]
        and neighbor_lists["D"] != x_neighbor_lists["D"]
        and face_status != "UNDEFINED",
    )
    checks.check(
        "not-leftover-of-y-probe-lists",
        probe_sites != y_probe_sites
        and letters != y_letters
        and y_letters["A"] == "UNDEFINED"
        and y_letters["B"] == E3
        and y_letters["C"] == NEG_E1
        and y_letters["D"] == "UNDEFINED"
        and neighbor_lists["A"] != y_neighbor_lists["A"]
        and neighbor_lists["C"] != y_neighbor_lists["C"]
        and reverse_status != "UNDEFINED"
        and face_status != "UNDEFINED",
    )
    checks.check(
        "sign-lettering-loses-axis",
        letters["C"] == E3
        and letters["D"] == NEG_E1
        and named_sign(letters["C"]) == "+"
        and named_sign(letters["D"]) == "-"
        and unique_vector_letter((letters["C"], letters["D"])) == "UNDEFINED"  # type: ignore[arg-type]
        and face_status == "fail"
        and named_sign(letters["A"]) == named_sign(letters["B"]) == "+"
        and unique_vector_letter((letters["A"], letters["B"])) == "UNDEFINED"  # type: ignore[arg-type]
        and reverse_status == "fail",
    )
    checks.check(
        "not-probe-own-incoming-lock",
        locks[PROBES["A"]] == {E3}
        and letters["A"] == E1
        and letters["A"] not in locks[PROBES["A"]]
        and locks[PROBES["B"]] == {E1}
        and letters["B"] == E3
        and letters["B"] not in locks[PROBES["B"]]
        and locks[PROBES["D"]] == {E3}
        and letters["D"] == NEG_E1
        and letters["D"] not in locks[PROBES["D"]]
        and unique_vector_letter(tuple(sorted(locks[PROBES["C"]]))) == "UNDEFINED"
        and letters["C"] == E3,
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["C"]]) == 3
        and len(locks[PROBES["A"]]) == 1
        and letters["C"] == E3
        and letters["A"] == E1,
        str(sorted(locks[PROBES["C"]])),
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check(
        "already-recorded-not-self-or-later",
        all(neighbor != PROBES[name] for name in PROBES for neighbor, _lock in neighbor_lists[name])
        and all(
            ticks[neighbor] < ticks[PROBES[name]]
            for name in PROBES
            for neighbor, _lock in neighbor_lists[name]
        ),
    )
    checks.check(
        "formation-stays-in-host",
        set(ticks) <= host,
    )
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[(0, -1, 0)] == 1
        and ticks[E3] == 1
        and ticks[(0, 0, -1)] == 1
        and ticks[PROBES["A"]] == 1
        and ticks[PROBES["D"]] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    opposite_image = False
    for matrix in proper_cubic_rotations():
        image = frozenset(
            (apply_matrix(matrix, site), apply_matrix(matrix, lock))
            for site, lock in PERP_SEEDS
        )
        if image == frozenset(TWO_SITE_SEEDS):
            opposite_image = True
            break
    checks.check(
        "not-cubic-orbit-of-perp-seed",
        (not opposite_image)
        and len(proper_cubic_rotations()) == 24
        and TWO_SITE_SEEDS[0][1] == E1
        and TWO_SITE_SEEDS[1][1] == NEG_E1
        and add(E1, NEG_E1) == ZERO
        and add(E1, E2) != ZERO,
    )
    checks.check(
        "ticks-agree-with-same-lock-seed-and-are-not-scored",
        all(ticks[PROBES[name]] == same_ticks[PROBES[name]] for name in PROBES)
        and ticks[PROBES["A"]] == 1
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 1
        and reverse_status == "fail"
        and face_status == "fail"
        and "not scored from those ticks" in normalized_note,
    )
    checks.check(
        "mutation-empty-neighbor-locks-undefined",
        unique_vector_letter(()) == "UNDEFINED"
        and reverse_report("UNDEFINED", letters["B"]) == "UNDEFINED"
        and face_report("UNDEFINED", letters["D"]) == "UNDEFINED",
    )
    checks.check(
        "mutation-mixed-neighbor-vectors-undefined",
        unique_vector_letter((E1, E3)) == "UNDEFINED"
        and unique_vector_letter((E3, NEG_E1)) == "UNDEFINED"
        and reverse_report(E1, "UNDEFINED") == "UNDEFINED"
        and face_report("UNDEFINED", "UNDEFINED") == "UNDEFINED",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-neighbor-lock-lists-and-letters",
        "L(A) = +e_1" in note
        and "L(B) = +e_3" in note
        and "L(C) = +e_3" in note
        and "L(D) = −e_1" in note
        and "+e_1 at (0, 0, 0)" in note
        and "+e_3 at (0, 1, 1)" in note
        and "+e_3 at (1, 0, 2)" in note
        and "+e_3 at (-1, 0, 2)" in note
        and "+e_3 at (0, -1, 2)" in note
        and "+e_3 at (0, 0, 1)" in note
        and "−e_1 at (0, 1, 0)" in note,
    )
    checks.check(
        "note-reports-fail-and-fail",
        "Reverse: fail" in note
        and "Face: fail" in note
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
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-not-ndot-or-occupancy-inner-product",
        "not an occupancy-kernel inner product" in normalized_note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-does-not-identify-incoming",
        "not identified" in normalized_note
        and "incoming step" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
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
        "note-not-tick-reverse-face",
        "Formation ticks are not scored" in note
        and "allowed-step plane of `±e_1`" in note
        and "not a proper cubic image" in normalized_note
        and "leftover of the four x-probe lists" in normalized_note
        and "leftover of the four y-probe lists" in normalized_note,
    )
    checks.check(
        "note-not-x-or-y-probe-reprint",
        "not the x-probes" in normalized_note
        and "not the y-probes" in normalized_note
        and "A = (0,0,1)" in note
        and "D = (0,1,1)" in note,
    )
    checks.check(
        "note-a-and-d-same-tick",
        "`A` is not a seed" in note
        and "`D` is not a seed" in note
        and "same-tick partner" in normalized_note,
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
        all(line in allowed_retained for line in allowed_retained)
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/OPPOSITE_LOCK_ZPROBE_NEIGHBOR_VECTOR_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def unique_vector_letter(" in source
        and "def recorded_neighbor_locks(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["B"]] >= 1
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-neighbor-lock-vectors-only",
        "unique_vector_letter" in defined_fns
        and "recorded_neighbor_locks" in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
