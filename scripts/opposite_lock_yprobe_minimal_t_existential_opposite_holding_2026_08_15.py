#!/usr/bin/env python3
"""Minimal T with later-tick exist-opposite HOLD on four opposite-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Let t(q) be the formation tick of probe q. Let T_max be the max of
t(A), t(B), t(C), t(D) among those defined in B_3(0). For each integer T from
0 through T_max, S_T(q) is the set of locks of 6-NN of q that formed at tick
<= T and are not q. Reverse_T holds iff some a in S_T(A) and some b in
S_T(B) have a+b=(0,0,0). Face_T holds iff some c in S_T(C) and some d in
S_T(D) have c+d=(0,0,0). Empty S_T on either side is UNDEFINED; nonempty
with no opposite pair fails. Report reverse_T and face_T at each T, and the
smallest T at which reverse_T HOLD and face_T HOLD, or none. Uniqueness is
not required. Occupancy n is not used. The probe's own incoming lock is not
used. Not leftover of the global-T=3 later-tick lists. Not leftover of
formation-tick already-recorded sets. Not named-sign lettering. Not unique
P_+. Not a Dijkstra search. Not a Gram readout.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_MINIMAL_T_EXISTENTIAL_OPPOSITE_HOLDING_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_MINIMAL_T_EXISTENTIAL_OPPOSITE_HOLDING_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
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
PROBES = {
    "A": (0, 1, 0),
    "B": (1, 1, 1),
    "C": (0, 2, 0),
    "D": (1, 1, 0),
}
X_PROBES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
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
    "P_+",
)
CLAIM_SCOPE = (
    "The later-tick exist-opposite reverse/face bits on nsopp y-probes at "
    "each T, and the smallest T at which both HOLD, are reported. "
    "Displayed, not adopted."
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
    """Named sign of a lock vector. Contrast only; not the scored predicate."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def recorded_lock_set(pairs: tuple[tuple[Point, Point], ...]) -> frozenset[Point]:
    """Set of later-tick six-neighbor locks. Duplicates collapse."""
    return frozenset(lock for _neighbor, lock in pairs)


def existential_opposite(left: frozenset[Point], right: frozenset[Point]) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right.

    Empty set on either side is UNDEFINED. Nonempty with no opposite pair fails.
    Does not sum. Does not require a singleton.
    """
    if not left or not right:
        return "UNDEFINED"
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: frozenset[Point], set_b: frozenset[Point]) -> str:
    """Reverse_T iff some a in S_T(A) and some b in S_T(B) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: frozenset[Point], set_d: frozenset[Point]) -> str:
    """Face_T iff some c in S_T(C) and some d in S_T(D) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def lock_display(lock: Point) -> str:
    return LOCK_NAME[lock]


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


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


def max_probe_tick(
    ticks: dict[Point, int],
    probes: dict[str, Point] = PROBES,
) -> int | None:
    """Max formation tick of the four named probes, or None if any is missing."""
    defined = [
        ticks[probes[name]] for name in ("A", "B", "C", "D") if probes[name] in ticks
    ]
    if len(defined) != 4:
        return None
    return max(defined)


def later_tick_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    common_tick: int,
) -> tuple[tuple[Point, Point], ...]:
    """Locks of 6-NN of site formed at tick <= common_tick, site excluded."""
    pairs: list[tuple[Point, Point]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor == site:
            continue
        if neighbor not in ticks:
            continue
        if ticks[neighbor] > common_tick:
            continue
        for lock in sorted(locks[neighbor]):
            pairs.append((neighbor, lock))
    return tuple(pairs)


def strictly_earlier_neighbor_locks(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> tuple[tuple[Point, Point], ...]:
    """Formation-time leftover: already-recorded 6-NN locks at formation of site."""
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


def sum_of_set(locks: frozenset[Point]) -> Point:
    """Z^3 sum leftover of a lock set. Contrast only; not this letter."""
    total = ZERO
    for lock in locks:
        total = add(total, lock)
    return total


def smallest_holding_t(
    reverse_by_t: dict[int, str],
    face_by_t: dict[int, str],
) -> int | None:
    """Smallest T with reverse_T hold and face_T hold, or None."""
    for tick in sorted(reverse_by_t):
        if reverse_by_t[tick] == "hold" and face_by_t[tick] == "hold":
            return tick
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

    print("minimal T later-tick exist-opposite HOLD on opposite-lock y-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != x_probe_sites,
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
        and add(E1, E1) == (2, 0, 0)
        and add(E2, E2) == (0, 2, 0)
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    mixed_ab_t3 = frozenset({E1, E2, NEG_E2, E3, NEG_E3})
    mixed_cd_t3 = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    set_a_t2 = frozenset({E1, E2, E3, NEG_E3})
    set_b_t2 = frozenset({E1, E3})
    set_c_t2 = frozenset({E1, NEG_E1, E2, E3, NEG_E3})
    set_d_t2 = frozenset({E1, NEG_E1})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(frozenset(), frozenset({E1})) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset(), frozenset()) == "UNDEFINED"
        and existential_opposite(frozenset({E1}), frozenset({E1, E2, E3})) == "fail"
        and existential_opposite(frozenset({NEG_E1}), frozenset({NEG_E1})) == "fail"
        and existential_opposite(set_a_t2, set_b_t2) == "hold"
        and existential_opposite(set_c_t2, set_d_t2) == "hold"
        and existential_opposite(mixed_ab_t3, mixed_ab_t3) == "hold"
        and existential_opposite(mixed_cd_t3, mixed_cd_t3) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold",
    )

    ticks, locks = form()
    t_max = max_probe_tick(ticks)
    perp_ticks, perp_locks = form(PERP_SEEDS)
    checks.check(
        "theorem1-all-four-probes-recorded",
        all(PROBES[name] in ticks for name in ("A", "B", "C", "D"))
        and t_max is not None,
    )
    assert t_max is not None

    neighbor_by_t: dict[int, dict[str, tuple[tuple[Point, Point], ...]]] = {}
    sets_by_t: dict[int, dict[str, frozenset[Point]]] = {}
    reverse_by_t: dict[int, str] = {}
    face_by_t: dict[int, str] = {}
    for tick in range(0, t_max + 1):
        neighbor_by_t[tick] = {}
        sets_by_t[tick] = {}
        for name in ("A", "B", "C", "D"):
            pairs = later_tick_neighbor_locks(PROBES[name], ticks, locks, tick)
            neighbor_by_t[tick][name] = pairs
            sets_by_t[tick][name] = recorded_lock_set(pairs)
        reverse_by_t[tick] = reverse_report(
            sets_by_t[tick]["A"], sets_by_t[tick]["B"]
        )
        face_by_t[tick] = face_report(sets_by_t[tick]["C"], sets_by_t[tick]["D"])
        print(
            f"T={tick} "
            f"S_T(A)={set_display(sets_by_t[tick]['A'])} "
            f"S_T(B)={set_display(sets_by_t[tick]['B'])} "
            f"S_T(C)={set_display(sets_by_t[tick]['C'])} "
            f"S_T(D)={set_display(sets_by_t[tick]['D'])} "
            f"reverse={reverse_by_t[tick]} face={face_by_t[tick]}"
        )

    holding_t = smallest_holding_t(reverse_by_t, face_by_t)
    leftover_lists: dict[str, tuple[tuple[Point, Point], ...]] = {}
    leftover_sets: dict[str, frozenset[Point]] = {}
    for name in ("A", "B", "C", "D"):
        leftover = strictly_earlier_neighbor_locks(PROBES[name], ticks, locks)
        leftover_lists[name] = leftover
        leftover_sets[name] = recorded_lock_set(leftover)
    leftover_reverse = reverse_report(leftover_sets["A"], leftover_sets["B"])
    leftover_face = face_report(leftover_sets["C"], leftover_sets["D"])
    print(
        f"T_max={t_max} "
        f"t(A)={ticks[PROBES['A']]} t(B)={ticks[PROBES['B']]} "
        f"t(C)={ticks[PROBES['C']]} t(D)={ticks[PROBES['D']]} "
        f"smallest_holding_T={holding_t}"
    )

    nslate_sets: dict[str, frozenset[Point]] = {}
    perp_common = max_probe_tick(perp_ticks, X_PROBES)
    assert perp_common is not None
    for name in ("A", "B", "C", "D"):
        pairs = later_tick_neighbor_locks(
            X_PROBES[name], perp_ticks, perp_locks, perp_common
        )
        nslate_sets[name] = recorded_lock_set(pairs)
    nslate_reverse = reverse_report(nslate_sets["A"], nslate_sets["B"])
    nslate_face = face_report(nslate_sets["C"], nslate_sets["D"])

    checks.check(
        "theorem1-max-probe-tick",
        t_max == 3
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and list(range(0, t_max + 1)) == [0, 1, 2, 3],
        str(t_max),
    )
    checks.check(
        "theorem1-T0-sets-and-bits",
        neighbor_by_t[0]["A"] == ((ORIGIN, E1),)
        and neighbor_by_t[0]["B"] == ()
        and neighbor_by_t[0]["C"] == ((PROBES["A"], NEG_E1),)
        and neighbor_by_t[0]["D"] == ((PROBES["A"], NEG_E1),)
        and sets_by_t[0]["A"] == frozenset({E1})
        and sets_by_t[0]["B"] == frozenset()
        and sets_by_t[0]["C"] == frozenset({NEG_E1})
        and sets_by_t[0]["D"] == frozenset({NEG_E1})
        and reverse_by_t[0] == "UNDEFINED"
        and face_by_t[0] == "fail",
        f"reverse={reverse_by_t[0]} face={face_by_t[0]}",
    )
    checks.check(
        "theorem1-T1-sets-and-bits",
        neighbor_by_t[1]["A"]
        == (
            (PROBES["C"], E2),
            (ORIGIN, E1),
            ((0, 1, 1), E3),
            ((0, 1, -1), NEG_E3),
        )
        and neighbor_by_t[1]["B"] == (((0, 1, 1), E3),)
        and neighbor_by_t[1]["C"] == ((PROBES["A"], NEG_E1),)
        and neighbor_by_t[1]["D"] == ((PROBES["A"], NEG_E1),)
        and sets_by_t[1]["A"] == frozenset({E1, E2, E3, NEG_E3})
        and sets_by_t[1]["B"] == frozenset({E3})
        and sets_by_t[1]["C"] == frozenset({NEG_E1})
        and sets_by_t[1]["D"] == frozenset({NEG_E1})
        and reverse_by_t[1] == "hold"
        and face_by_t[1] == "fail"
        and NEG_E3 in sets_by_t[1]["A"]
        and E3 in sets_by_t[1]["B"]
        and add(NEG_E3, E3) == ZERO,
        f"reverse={reverse_by_t[1]} face={face_by_t[1]}",
    )
    checks.check(
        "theorem1-T2-sets-and-bits",
        neighbor_by_t[2]["A"]
        == (
            (PROBES["C"], E2),
            (ORIGIN, E1),
            ((0, 1, 1), E3),
            ((0, 1, -1), NEG_E3),
        )
        and neighbor_by_t[2]["B"]
        == (
            ((0, 1, 1), E3),
            ((1, 0, 1), E1),
        )
        and neighbor_by_t[2]["C"]
        == (
            ((1, 2, 0), E1),
            ((-1, 2, 0), NEG_E1),
            (PROBES["A"], NEG_E1),
            ((0, 2, 1), E3),
            ((0, 2, 1), E2),
            ((0, 2, -1), NEG_E3),
            ((0, 2, -1), E2),
        )
        and neighbor_by_t[2]["D"]
        == (
            (PROBES["A"], NEG_E1),
            ((1, 2, 0), E1),
            (PROBES["B"], E1),
            ((1, 1, -1), E1),
        )
        and sets_by_t[2]["A"] == set_a_t2
        and sets_by_t[2]["B"] == set_b_t2
        and sets_by_t[2]["C"] == set_c_t2
        and sets_by_t[2]["D"] == set_d_t2
        and reverse_by_t[2] == "hold"
        and face_by_t[2] == "hold"
        and NEG_E3 in sets_by_t[2]["A"]
        and E3 in sets_by_t[2]["B"]
        and NEG_E1 in sets_by_t[2]["C"]
        and E1 in sets_by_t[2]["D"],
        f"reverse={reverse_by_t[2]} face={face_by_t[2]}",
    )
    checks.check(
        "theorem1-T3-sets-and-bits",
        neighbor_by_t[3]["A"]
        == (
            (PROBES["D"], NEG_E2),
            (PROBES["D"], NEG_E3),
            (PROBES["D"], E3),
            ((-1, 1, 0), NEG_E2),
            ((-1, 1, 0), NEG_E3),
            ((-1, 1, 0), E3),
            (PROBES["C"], E2),
            (ORIGIN, E1),
            ((0, 1, 1), E3),
            ((0, 1, -1), NEG_E3),
        )
        and neighbor_by_t[3]["B"]
        == (
            ((0, 1, 1), E3),
            ((1, 2, 1), E3),
            ((1, 2, 1), E2),
            ((1, 2, 1), E1),
            ((1, 0, 1), E1),
            ((1, 1, 2), E3),
            (PROBES["D"], NEG_E2),
            (PROBES["D"], NEG_E3),
            (PROBES["D"], E3),
        )
        and neighbor_by_t[3]["C"]
        == (
            ((1, 2, 0), E1),
            ((-1, 2, 0), NEG_E1),
            (PROBES["A"], NEG_E1),
            ((0, 2, 1), E3),
            ((0, 2, 1), E2),
            ((0, 2, -1), NEG_E3),
            ((0, 2, -1), E2),
        )
        and neighbor_by_t[3]["D"]
        == (
            (PROBES["A"], NEG_E1),
            ((1, 2, 0), E1),
            ((1, 0, 0), NEG_E3),
            ((1, 0, 0), E3),
            ((1, 0, 0), E2),
            (PROBES["B"], E1),
            ((1, 1, -1), E1),
        )
        and sets_by_t[3]["A"] == mixed_ab_t3
        and sets_by_t[3]["B"] == mixed_ab_t3
        and sets_by_t[3]["C"] == mixed_cd_t3
        and sets_by_t[3]["D"] == mixed_cd_t3
        and reverse_by_t[3] == "hold"
        and face_by_t[3] == "hold",
        f"reverse={reverse_by_t[3]} face={face_by_t[3]}",
    )
    checks.check(
        "theorem2-smallest-T-both-hold",
        holding_t == 2
        and reverse_by_t[2] == "hold"
        and face_by_t[2] == "hold"
        and reverse_by_t[0] != "hold"
        and face_by_t[0] != "hold"
        and face_by_t[1] != "hold"
        and all(
            not (
                reverse_by_t[tick] == "hold" and face_by_t[tick] == "hold"
            )
            for tick in range(0, 2)
        ),
        str(holding_t),
    )
    checks.check(
        "not-leftover-of-global-T3-lists",
        sets_by_t[2]["A"] != sets_by_t[3]["A"]
        and sets_by_t[2]["B"] != sets_by_t[3]["B"]
        and sets_by_t[2]["D"] != sets_by_t[3]["D"]
        and NEG_E2 not in sets_by_t[2]["A"]
        and NEG_E2 in sets_by_t[3]["A"]
        and sets_by_t[2]["B"] == frozenset({E1, E3})
        and sets_by_t[3]["B"] == mixed_ab_t3
        and sets_by_t[2]["D"] == frozenset({E1, NEG_E1})
        and sets_by_t[3]["D"] == mixed_cd_t3
        and holding_t == 2
        and holding_t != 3,
    )
    checks.check(
        "not-leftover-of-formation-time",
        leftover_sets["A"] == frozenset()
        and leftover_sets["B"] == frozenset({E3})
        and leftover_sets["C"] == frozenset({NEG_E1})
        and leftover_sets["D"] == frozenset({NEG_E1, E1})
        and leftover_reverse == "UNDEFINED"
        and leftover_face == "hold"
        and leftover_sets["A"] != sets_by_t[2]["A"]
        and reverse_by_t[2] == "hold"
        and leftover_reverse != reverse_by_t[2],
    )
    checks.check(
        "not-leftover-of-nslate-nnseed-x-probes",
        TWO_SITE_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and nslate_sets["A"] == frozenset({E1})
        and nslate_sets["B"] == frozenset({E1, E2, E3})
        and nslate_sets["C"] == frozenset({NEG_E2})
        and nslate_sets["D"] == frozenset({E1, E2, NEG_E2, E3, NEG_E3})
        and nslate_reverse == "fail"
        and nslate_face == "hold"
        and reverse_by_t[2] == "hold"
        and reverse_by_t[2] != nslate_reverse
        and sets_by_t[2]["A"] != nslate_sets["A"],
    )
    checks.check(
        "not-leftover-of-unique-own-incoming",
        locks[PROBES["A"]] == {NEG_E1}
        and locks[PROBES["B"]] == {E1}
        and locks[PROBES["C"]] == {E2}
        and locks[PROBES["D"]] == {NEG_E2, NEG_E3, E3}
        and NEG_E1 not in sets_by_t[2]["A"]
        and sets_by_t[2]["A"] != frozenset({NEG_E1})
        and sets_by_t[2]["C"] != frozenset({E2})
        and sets_by_t[2]["D"] != frozenset()
        and face_by_t[2] == "hold"
        and face_by_t[2] != "UNDEFINED",
    )
    checks.check(
        "sign-lettering-loses-axis-and-would-hide-hold",
        named_sign(E2) == "+"
        and named_sign(NEG_E2) == "-"
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and reverse_by_t[2] == "hold"
        and face_by_t[2] == "hold",
    )
    checks.check(
        "not-probe-own-incoming-lock",
        locks[PROBES["A"]] == {NEG_E1}
        and NEG_E1 not in sets_by_t[2]["A"]
        and locks[PROBES["C"]] == {E2}
        and sets_by_t[2]["C"] != frozenset({E2}),
    )
    checks.check(
        "not-sum-leftover",
        sum_of_set(sets_by_t[2]["A"]) == add(E1, E2)
        and sum_of_set(sets_by_t[2]["B"]) == add(E1, E3)
        and add(sum_of_set(sets_by_t[2]["A"]), sum_of_set(sets_by_t[2]["B"])) != ZERO
        and reverse_by_t[2] == "hold"
        and face_by_t[2] == "hold",
    )
    checks.check(
        "not-unique-vector-leftover",
        len(sets_by_t[2]["A"]) > 1
        and len(sets_by_t[2]["B"]) > 1
        and len(sets_by_t[2]["C"]) > 1
        and len(sets_by_t[2]["D"]) > 1
        and reverse_by_t[2] == "hold"
        and face_by_t[2] == "hold",
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(locks[PROBES[name]] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(locks[PROBES["D"]]) == 3
        and sets_by_t[2]["D"] == set_d_t2
        and face_by_t[2] == "hold",
        str(sorted(locks[PROBES["D"]])),
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and TWO_SITE_SEEDS != PERP_SEEDS,
    )
    checks.check(
        "later-tick-not-self-and-formed-by-T",
        all(
            neighbor != PROBES[name]
            for tick in range(0, t_max + 1)
            for name in PROBES
            for neighbor, _lock in neighbor_by_t[tick][name]
        )
        and all(
            ticks[neighbor] <= tick
            for tick in range(0, t_max + 1)
            for name in PROBES
            for neighbor, _lock in neighbor_by_t[tick][name]
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
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "mutation-empty-neighbor-locks-undefined",
        recorded_lock_set(()) == frozenset()
        and reverse_report(frozenset(), sets_by_t[2]["B"]) == "UNDEFINED"
        and face_report(sets_by_t[2]["C"], frozenset()) == "UNDEFINED",
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E2, E3})) == "fail"
        and reverse_by_t[2] == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-each-T-bits",
        "T=0: reverse UNDEFINED, face fail" in note
        and "T=1: reverse hold, face fail" in note
        and "T=2: reverse hold, face hold" in note
        and "T=3: reverse hold, face hold" in note
        and "S_0(A) = {+e_1}" in note
        and "S_0(B) = {}" in note
        and "S_1(A) = {+e_1, +e_2, +e_3, −e_3}" in note
        and "S_1(B) = {+e_3}" in note
        and "S_2(A) = {+e_1, +e_2, +e_3, −e_3}" in note
        and "S_2(B) = {+e_1, +e_3}" in note
        and "S_2(C) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note
        and "S_2(D) = {+e_1, −e_1}" in note
        and "S_3(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}" in note
        and "S_3(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}" in note,
    )
    checks.check(
        "note-reports-smallest-T",
        "Smallest T: 2" in note
        and "smallest T" in normalized_note
        and "T=2" in note,
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
        and "incoming step" in normalized_note
        and "S_2(A)` has no `−e_1`" in note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from later-tick six-neighbor locks"
        in normalized_note
        and "Do not attach" not in note,
    )
    checks.check(
        "note-not-unique-or-sum-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "uniqueness is not required" in normalized_note.lower(),
    )
    checks.check(
        "note-not-leftover-of-T3-lists",
        "not leftover of the global-T=3 later-tick lists" in normalized_note
        and "S_2(A)" in note
        and "S_3(A)" in note,
    )
    checks.check(
        "note-not-leftover-of-formation-tick",
        "not leftover of formation-tick" in normalized_note
        and "empty" in normalized_note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-later-tick-T-defined",
        "for each integer T" in normalized_note
        and "tick `≤ T`" in note
        and "max" in normalized_note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "No runner cache is written." in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_MINIMAL_T_EXISTENTIAL_OPPOSITE_HOLDING_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def existential_opposite(" in source
        and "def recorded_lock_set(" in source
        and "def later_tick_neighbor_locks(" in source
        and "def max_probe_tick(" in source
        and "def smallest_holding_t(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-existential-opposite-only",
        "existential_opposite" in defined_fns
        and "recorded_lock_set" in defined_fns
        and "later_tick_neighbor_locks" in defined_fns
        and "smallest_holding_t" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns
        and "dijkstra" not in {name.lower() for name in defined_fns}
        and "gram" not in {name.lower() for name in defined_fns},
    )
    checks.check(
        "theorem3-displayed-not-adopted",
        reverse_by_t[2] == "hold"
        and face_by_t[2] == "hold"
        and holding_t == 2
        and "displayed, not adopted" in normalized_note.lower()
        and "not written into Admissibility" in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
