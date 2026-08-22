#!/usr/bin/env python3
"""Own outgoing set exist-opposite reverse/face at t+1 on two-axis same-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint same-lock pairs: origin and (0,1,0) lock +e_1; (0,0,1)
and (0,1,1) lock +e_2. Same process and y-probes as nm2sl. A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. Seeds keep their seed letters as a singleton.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. O(q, tau) is the outgoing dual of M: the set
of e in {±e_1,±e_2,±e_3} such that q+e is formed and e is in M(q+e, tau).
Unformed at tau => UNDEFINED. Empty O is empty, not UNDEFINED. Reverse
holds iff some a in O(A, tau) and some b in O(B, tau) have a+b=(0,0,0).
Face holds iff some c in O(C, tau) and some d in O(D, tau) have c+d=(0,0,0).
Empty or UNDEFINED on either side is UNDEFINED; nonempty with no opposite
pair fails. Timed: tau = t(q)+1. Uniqueness of locks is not required.
Occupancy of sites is not used. Named-sign lettering is not used. No unique
projector. No larger host. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_YPROBE_OWN_OUTGOING_SET_EXISTENTIAL_OPPOSITE_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_YPROBE_OWN_OUTGOING_SET_EXISTENTIAL_OPPOSITE_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
AxisSet = frozenset[Point] | str
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
AXES: tuple[Point, ...] = (E1, E2, E3)
BALL_SQ = 9
TWO_AXIS_SAME_LOCK_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    ((0, 1, 1), E2),
)
ONE_AXIS_SAME_LOCK_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
TWO_AXIS_OPPOSITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    ((0, 1, 1), NEG_E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
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
    "P_+",
    "S^+",
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Reverse and face from the own outgoing *set* at t+1 on the "
    "four y-probes of the two-axis same-lock seed are reported. "
    "Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


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


def axis_of_letter(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def lockset_display(value: Incoming) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    return set_display(value)


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_SAME_LOCK_SEEDS,
    *,
    require_perp: bool = True,
) -> tuple[dict[Point, int], dict[Point, set[Point]], dict[Point, Point]]:
    """Earliest formation ticks and incoming locks on B_3(0)."""
    ticks: dict[Point, int] = {site: 0 for site, _lock in seeds}
    locks: dict[Point, set[Point]] = {site: {lock} for site, lock in seeds}
    seed_map: dict[Point, Point] = {site: lock for site, lock in seeds}
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
    return ticks, locks, seed_map


def incoming_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Incoming:
    """Earliest incoming NN steps at site using only records with tick <= tau."""
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    if site in seed_map:
        return frozenset({seed_map[site]})
    arrivals: dict[int, set[Point]] = {}
    for step in NN:
        parent = sub(site, step)
        if parent not in ticks or ticks[parent] > tau:
            continue
        if any(perpendicular(lock, step) for lock in locks[parent]):
            arrivals.setdefault(ticks[parent] + 1, set()).add(step)
    if not arrivals:
        return frozenset()
    earliest = min(arrivals)
    return frozenset(arrivals[earliest])


def outgoing_set(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Outgoing:
    """Outgoing dual of M. Unformed at tau => UNDEFINED. Empty O is empty."""
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    outgoing: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if not in_ball(neighbor):
            continue
        incoming = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if incoming == UNDEFINED:
            continue
        if not isinstance(incoming, frozenset):
            raise TypeError(f"incoming is not a lock set: {incoming!r}")
        if step in incoming:
            outgoing.add(step)
    return frozenset(outgoing)


def axis_set(value: Incoming) -> AxisSet:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    occupied: set[Point] = set()
    for lock in value:
        axis = axis_of_letter(lock)
        if axis not in AXES:
            raise ValueError(f"lock is not a six-neighbor step: {lock!r}")
        occupied.add(axis)
    return frozenset(occupied)


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    """Leftover: HOLD iff axes disjoint and union is {e_1,e_2,e_3}."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    if axes_m & axes_o:
        return "fail"
    if axes_m | axes_o != frozenset(AXES):
        return "fail"
    return "hold"


def pair_cover(left: str, right: str) -> str:
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right.

    UNDEFINED or empty on either side is UNDEFINED. Nonempty with no opposite
    pair fails. Mixed stays a set. Does not sum. Does not require a singleton.
    """
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: Incoming, set_b: Incoming) -> str:
    """Reverse iff some a in O(A, tau) and some b in O(B, tau) have a+b=0."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Face iff some c in O(C, tau) and some d in O(D, tau) have c+d=0."""
    return existential_opposite(set_c, set_d)


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def opposite_pair(left: Incoming, right: Incoming) -> tuple[Point, Point] | None:
    if left == UNDEFINED or right == UNDEFINED:
        return None
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        return None
    for a in NN:
        if a not in left:
            continue
        for b in NN:
            if b in right and add(a, b) == ZERO:
                return (a, b)
    return None


def internal_opposite(value: Incoming) -> str:
    """Leftover: opposite pair inside one set. Not this reverse."""
    if value == UNDEFINED or not isinstance(value, frozenset):
        return UNDEFINED
    return existential_opposite(value, value)


def sum_of_set(locks: Incoming) -> Point | str:
    if locks == UNDEFINED:
        return UNDEFINED
    if not isinstance(locks, frozenset):
        raise TypeError(f"lock set is not a lock set: {locks!r}")
    total = ZERO
    for lock in locks:
        total = add(total, lock)
    return total


def probe_sets(
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[dict[str, Incoming], dict[str, Outgoing]]:
    incoming: dict[str, Incoming] = {}
    outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau = ticks[site] + 1
        incoming[name] = incoming_set(site, tau, ticks, locks, seed_map)
        outgoing[name] = outgoing_set(site, tau, ticks, locks, seed_map)
    return incoming, outgoing


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

    print("own outgoing set exist-opposite reverse/face at t+1")
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E1, E1) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "existential-opposite-identity",
        existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset({E1}), UNDEFINED) == UNDEFINED
        and existential_opposite(frozenset(), frozenset({E3})) == UNDEFINED
        and existential_opposite(frozenset({E3}), frozenset()) == UNDEFINED
        and existential_opposite(frozenset(), frozenset()) == UNDEFINED
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold"
        and existential_opposite(frozenset({E2, NEG_E3}), frozenset({E2, E3, NEG_E3}))
        == "hold"
        and existential_opposite(
            frozenset({E1, NEG_E1, E3, NEG_E3}), frozenset({E1})
        )
        == "hold"
        and existential_opposite(frozenset({E2}), frozenset({NEG_E3})) == "fail",
    )

    ticks, locks, seed_map = form()
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    cover: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        cover[name] = axis_cover(m1[name], o1[name])
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])}"
        )

    reverse_status = reverse_report(o1["A"], o1["B"])
    face_status = face_report(o1["C"], o1["D"])
    m_reverse = reverse_report(m1["A"], m1["B"])
    m_face = face_report(m1["C"], m1["D"])
    cover_reverse = pair_cover(cover["A"], cover["B"])
    cover_face = pair_cover(cover["C"], cover["D"])
    unique_reverse = reverse_report(unique_letter(o1["A"]), unique_letter(o1["B"]))
    unique_face = face_report(unique_letter(o1["C"]), unique_letter(o1["D"]))
    empty_at_t_reverse = reverse_report(o0["A"], o0["B"])
    empty_at_t_face = face_report(o0["C"], o0["D"])
    o_opp_pair = opposite_pair(o1["A"], o1["B"])
    face_opp_pair = opposite_pair(o1["C"], o1["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(f"M exist-opposite reverse={m_reverse} face={m_face}")
    print(f"cover leftover reverse={cover_reverse} face={cover_face}")
    print(
        "per_element: each signed lock in own outgoing O at a probe's t+1"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four O reports, reverse/face from exist-opposite of O")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
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
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[E3] == 0
        and ticks[(0, 1, 1)] == 0
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and reverse_report(UNDEFINED, frozenset({E1})) == UNDEFINED
        and face_report(frozenset({E1}), UNDEFINED) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set((0, 1, 1), 1, ticks, locks, seed_map) == frozenset({E2})
        and TWO_AXIS_SAME_LOCK_SEEDS
        == ((ORIGIN, E1), (E2, E1), (E3, E2), ((0, 1, 1), E2)),
    )
    checks.check(
        "neither-pair-is-opposite",
        seed_map[ORIGIN] == seed_map[E2] == E1
        and seed_map[E3] == seed_map[(0, 1, 1)] == E2
        and add(seed_map[ORIGIN], seed_map[E2]) != ZERO
        and add(seed_map[E3], seed_map[(0, 1, 1)]) != ZERO
        and TWO_AXIS_SAME_LOCK_SEEDS != TWO_AXIS_OPPOSITE_SEEDS,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau",
        m1["A"] == frozenset({E1})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E2, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-O-empty-at-t-timed-cut",
        all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and empty_at_t_reverse == UNDEFINED
        and empty_at_t_face == UNDEFINED
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and E2 in seed_map
        and seed_map[E2] == E1
        and m1["A"] == frozenset({E1}),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and unique_letter(o1["C"]) == UNDEFINED
        and reverse_status == "hold",
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and o_opp_pair == (NEG_E3, E3)
        and reverse_status != "fail"
        and reverse_status != UNDEFINED,
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and face_opp_pair == (NEG_E1, E1)
        and face_status != "fail"
        and face_status != UNDEFINED,
        face_status,
    )
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SAME_LOCK_SEEDS)
    one_m, one_o = probe_sets(one_ticks, one_locks, one_seeds)
    one_reverse = reverse_report(one_o["A"], one_o["B"])
    one_face = face_report(one_o["C"], one_o["D"])
    checks.check(
        "not-one-axis-same-lock-leftover",
        TWO_AXIS_SAME_LOCK_SEEDS != ONE_AXIS_SAME_LOCK_SEEDS
        and ticks[PROBES["B"]] == 1
        and one_ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 2
        and one_ticks[PROBES["D"]] == 3
        and o1["A"] == frozenset({E2, NEG_E3})
        and one_o["A"] == frozenset({E2, E3, NEG_E3})
        and E3 not in o1["A"]
        and one_m["D"] != m1["D"]
        and one_reverse == "hold"
        and one_face == "hold",
    )
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPPOSITE_SEEDS)
    opp_m, opp_o = probe_sets(opp_ticks, opp_locks, opp_seeds)
    checks.check(
        "not-two-axis-opposite",
        TWO_AXIS_SAME_LOCK_SEEDS != TWO_AXIS_OPPOSITE_SEEDS
        and opp_m["A"] == frozenset({NEG_E1})
        and m1["A"] == frozenset({E1})
        and isinstance(opp_o["D"], frozenset)
        and NEG_E1 in opp_o["D"]
        and isinstance(o1["D"], frozenset)
        and NEG_E1 not in o1["D"],
    )
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(NSOPP_SEEDS)
    nsopp_m, _nsopp_o = probe_sets(nsopp_ticks, nsopp_locks, nsopp_seeds)
    nsopp_m_reverse = reverse_report(nsopp_m["A"], nsopp_m["B"])
    checks.check(
        "not-exist-opposite-of-M",
        m_reverse == "fail"
        and m_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and m_reverse != reverse_status
        and m_face != face_status
        and nsopp_m_reverse == "hold"
        and TWO_AXIS_SAME_LOCK_SEEDS != NSOPP_SEEDS,
    )
    checks.check(
        "not-axis-cover-leftover",
        cover["A"] == "hold"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "fail"
        and cover_reverse == "hold"
        and cover_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and cover_face != face_status,
    )
    checks.check(
        "not-unique-letter-leftover",
        unique_reverse == UNDEFINED
        and unique_face == UNDEFINED
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-internal-opposite-leftover",
        internal_opposite(o1["A"]) == "fail"
        and internal_opposite(o1["B"]) == "hold"
        and internal_opposite(o1["C"]) == "hold"
        and internal_opposite(o1["D"]) == "fail"
        and reverse_status == "hold"
        and reverse_status != internal_opposite(o1["A"]),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E1 in m1["A"]
        and E1 not in o1["A"]
        and o1["A"] != m1["A"],
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        existential_opposite(frozenset(), o1["A"]) == UNDEFINED
        and existential_opposite(UNDEFINED, o1["A"]) == UNDEFINED
        and reverse_report(UNDEFINED, o1["B"]) == UNDEFINED
        and face_report(o1["C"], UNDEFINED) == UNDEFINED
        and reverse_status == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["A"], frozenset)
        and isinstance(o1["B"], frozenset)
        and sum_of_set(o1["A"]) == add(E2, NEG_E3)
        and sum_of_set(o1["B"]) == E2
        and reverse_status == "hold"
        and add(sum_of_set(o1["A"]), sum_of_set(o1["B"])) != ZERO,
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 1
        and len(o1["A"]) == 2
        and len(o1["B"]) == 3
        and len(o1["C"]) == 4
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "two-axis-same-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E1}
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[(0, 1, 1)] == 0
        and locks[(0, 1, 1)] == {E2}
        and TWO_AXIS_SAME_LOCK_SEEDS != ONE_AXIS_SAME_LOCK_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != TWO_AXIS_OPPOSITE_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != NSOPP_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != X_AXIS_SAME_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    x_m1 = {
        name: incoming_set(
            X_PROBES[name],
            ticks[X_PROBES[name]] + 1,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if X_PROBES[name] in ticks
    }
    checks.check(
        "not-x-probes",
        probe_sites != x_probe_sites
        and x_m1["A"] != m1["A"]
        and reverse_status == "hold",
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=2" in note
        and "M(A, τ) = {+e_1}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_2}" in note
        and "M(D, τ) = {−e_3}" in note
        and "O(A, τ) = {+e_2, −e_3}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_1}" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse: hold" in note
        and "Face: hold" in note
        and "Reverse holds." in note
        and "Face holds." in note
        and "witness (−e_3, +e_3)" in note
        and "witness (−e_1, +e_1)" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-exist-opposite-of-M",
        "not exist-opposite of `M`" in normalized_note
        and "M exist-opposite reverse fail" in normalized_note
        and "M exist-opposite face fail" in normalized_note,
    )
    checks.check(
        "note-not-axis-cover-leftover",
        "not leftover of axis-cover" in normalized_note
        and "cover face fail" in normalized_note
        and "Face: hold" in note,
    )
    checks.check(
        "note-timed-cut-not-empty-at-t",
        "empty `O` at formation tick `t`" in normalized_note
        and "τ(q)=t(q)+1" in note.replace(" ", "")
        and "no global T" in normalized_note,
    )
    checks.check(
        "note-uniqueness-not-required",
        "Uniqueness of incoming or outgoing locks is not required."
        in normalized_note
        and "Mixed remains a set." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "own outgoing" in normalized_note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "{n:n·n<=9}" in note.replace(" ", "")
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
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/TWO_AXIS_SAME_LOCK_YPROBE_OWN_OUTGOING_SET_EXISTENTIAL_OPPOSITE_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "incoming_set" in defined_fns
        and "outgoing_set" in defined_fns
        and "existential_opposite" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
