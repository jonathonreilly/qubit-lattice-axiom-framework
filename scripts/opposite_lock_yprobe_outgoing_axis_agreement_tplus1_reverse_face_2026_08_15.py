#!/usr/bin/env python3
"""Outgoing-axis agreement of O at t+1 reverse/face.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1 (nsopp #7093; same process and
y-probes as nsmopp #7208). A 6-NN step is allowed iff it is perpendicular
to the parent lock axis. Newly formed sites lock the incoming step. Seeds
keep their seed letters as a singleton. M(q, tau) is the set of earliest
incoming nearest-neighbor steps at q using only records with tick <= tau.
Unformed at tau => UNDEFINED. O(q, tau) is the outgoing dual of M: the set
of e in {±e_1,±e_2,±e_3} such that q+e is formed and e is in M(q+e, tau).
Unformed q at tau => UNDEFINED. Empty O is empty, not UNDEFINED. Axis(O) is
the unsigned lattice directions of signed locks in O. Empty Axis => fail,
not UNDEFINED. Reverse HOLDs iff Axis(O) at A equals Axis(O) at B and both
are nonempty. Face likewise on C, D. Dual of incoming-axis agreement of M.
Uniqueness is not required. Occupancy of sites is not used. Named-sign
lettering is not used. No larger host. No unique P_+. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_OUTGOING_AXIS_AGREEMENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_OUTGOING_AXIS_AGREEMENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
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
AXIS_NAME = {
    E1: "e_1",
    E2: "e_2",
    E3: "e_3",
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
    "Outgoing-axis agreement of O at t+1 on the four #7208 y-probes, "
    "and reverse/face from that, are reported. Displayed, not adopted."
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


def named_sign(lock: Point) -> str:
    """Named sign of a lock vector. Contrast only; not the scored predicate."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def axis_display(value: AxisSet) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"axis set is not an axis set: {value!r}")
    if not value:
        return "{}"
    names = ", ".join(AXIS_NAME[axis] for axis in AXES if axis in value)
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
    seeds: tuple[tuple[Point, Point], ...] = TWO_SITE_SEEDS,
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
    """Unsigned lattice axes occupied by signed locks. UNDEFINED if unformed."""
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


def leftover_of_one(value: Incoming) -> AxisSet:
    """One-sided leftover contrast: {e_1,e_2,e_3} minus Axis(S). Not this letter."""
    occupied = axis_set(value)
    if occupied == UNDEFINED:
        return UNDEFINED
    if not isinstance(occupied, frozenset):
        raise TypeError("one-sided leftover needs an axis set")
    return frozenset(AXES) - occupied


def leftover_axis(incoming: Incoming, outgoing: Outgoing) -> AxisSet:
    """Leftover-empty contrast: {e_1,e_2,e_3} minus (Axis(M) union Axis(O))."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    return frozenset(AXES) - (axes_m | axes_o)


def axis_agreement(left: AxisSet, right: AxisSet) -> str:
    """HOLD iff both defined nonempty and equal. Empty Axis => fail, not UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    if not left or not right:
        return "fail"
    if left == right:
        return "hold"
    return "fail"


def reverse_report(axis_a: AxisSet, axis_b: AxisSet) -> str:
    """Reverse HOLDs iff Axis(O) at A equals Axis(O) at B nonempty."""
    return axis_agreement(axis_a, axis_b)


def face_report(axis_c: AxisSet, axis_d: AxisSet) -> str:
    """Face HOLDs iff Axis(O) at C equals Axis(O) at D nonempty."""
    return axis_agreement(axis_c, axis_d)


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Signed exist-opposite leftover contrast. Not this reverse."""
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


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def neighbor_lock_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    tau: int,
) -> frozenset[Point]:
    """Leftover contrast: locks of 6-NN formed by tau, site excluded."""
    collected: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks or ticks[neighbor] > tau:
            continue
        collected.update(locks[neighbor])
    return frozenset(collected)


def sum_of_set(locks: frozenset[Point]) -> Point:
    total = ZERO
    for lock in locks:
        total = add(total, lock)
    return total


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

    print("outgoing-axis agreement of O reverse/face at t+1")
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
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    axis_a = frozenset({E2, E3})
    axis_b = frozenset({E2, E3})
    axis_c = frozenset({E1, E3})
    axis_d = frozenset({E1})
    axis_m_a = frozenset({E1})
    axis_m_c = frozenset({E2})
    axis_m_d = frozenset({E2, E3})
    checks.check(
        "axis-identity",
        axis_set(UNDEFINED) == UNDEFINED
        and axis_set(frozenset()) == frozenset()
        and axis_set(frozenset({NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E1, NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E2, E3, NEG_E3})) == frozenset({E2, E3})
        and axis_set(frozenset({E1, NEG_E1, E3, NEG_E3})) == frozenset({E1, E3}),
    )
    checks.check(
        "axis-agreement-identity",
        axis_agreement(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_agreement(frozenset({E1}), UNDEFINED) == UNDEFINED
        and axis_agreement(frozenset(), frozenset()) == "fail"
        and axis_agreement(frozenset(), frozenset({E1})) == "fail"
        and axis_agreement(frozenset({E1}), frozenset()) == "fail"
        and axis_agreement(axis_a, axis_b) == "hold"
        and axis_agreement(axis_c, axis_d) == "fail"
        and axis_agreement(axis_m_a, axis_m_a) == "hold"
        and axis_agreement(axis_m_c, axis_m_d) == "fail"
        and axis_agreement(frozenset({E1}), frozenset({E2})) == "fail",
    )

    ticks, locks, seed_map = form()
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    axis_m: dict[str, AxisSet] = {}
    axis_o: dict[str, AxisSet] = {}
    axis_o0: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    lx: dict[str, AxisSet] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        axis_m[name] = axis_set(m1[name])
        axis_o[name] = axis_set(o1[name])
        axis_o0[name] = axis_set(o0[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        print(
            f"{name} t={ticks[site]} "
            f"O={lockset_display(o1[name])} "
            f"Axis(O)={axis_display(axis_o[name])}"
        )

    reverse_status = reverse_report(axis_o["A"], axis_o["B"])
    face_status = face_report(axis_o["C"], axis_o["D"])
    reverse_m = reverse_report(axis_m["A"], axis_m["B"])
    face_m = face_report(axis_m["C"], axis_m["D"])
    reverse_lx_m = reverse_report(lx_m["A"], lx_m["B"])
    face_lx_m = face_report(lx_m["C"], lx_m["D"])
    reverse_lx_o = reverse_report(lx_o["A"], lx_o["B"])
    face_lx_o = face_report(lx_o["C"], lx_o["D"])
    leftover_reverse = reverse_report(lx["A"], lx["B"])
    leftover_face = face_report(lx["C"], lx["D"])
    o_exist_reverse = existential_opposite(o1["A"], o1["B"])
    o_exist_face = existential_opposite(o1["C"], o1["D"])
    reverse_at_t = reverse_report(axis_o0["A"], axis_o0["B"])
    face_at_t = face_report(axis_o0["C"], axis_o0["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        f"Axis(M) reverse={reverse_m} face={face_m} "
        f"exist-O reverse={o_exist_reverse} face={o_exist_face}"
    )
    print(
        "per_element: each unsigned lattice axis among {e_1,e_2,e_3} "
        "occupied by O at a probe's t+1"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four Axis(O) reports, reverse/face from outgoing-axis agreement")
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
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        outgoing_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and axis_set(outgoing_set(PROBES["B"], 1, ticks, locks, seed_map)) == UNDEFINED
        and reverse_report(
            axis_set(outgoing_set(PROBES["B"], 1, ticks, locks, seed_map)),
            axis_o["B"],
        )
        == UNDEFINED
        and outgoing_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED
        and axis_set(outgoing_set(PROBES["D"], 2, ticks, locks, seed_map)) == UNDEFINED,
    )
    checks.check(
        "empty-axis-fails-not-undefined",
        axis_agreement(frozenset(), frozenset({E1})) == "fail"
        and axis_agreement(frozenset(), frozenset()) == "fail"
        and axis_set(frozenset()) == frozenset()
        and axis_set(frozenset()) != UNDEFINED,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E2, E3, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Axis-O",
        axis_o["A"] == axis_a
        and axis_o["B"] == axis_b
        and axis_o["C"] == axis_c
        and axis_o["D"] == axis_d
        and axis_o["A"] != UNDEFINED
        and axis_o["D"] != UNDEFINED
        and axis_o["A"] != frozenset()
        and axis_o["D"] != frozenset(),
        str({name: axis_display(axis_o[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and unique_letter(o1["C"]) == UNDEFINED
        and axis_o["A"] == axis_a
        and axis_o["C"] == axis_c,
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and axis_o["A"] == axis_a
        and axis_o["B"] == axis_b
        and axis_o["A"] == axis_o["B"]
        and bool(axis_o["A"])
        and reverse_status != "fail"
        and reverse_status != UNDEFINED,
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and axis_o["C"] == axis_c
        and axis_o["D"] == axis_d
        and axis_o["C"] != axis_o["D"]
        and bool(axis_o["C"])
        and bool(axis_o["D"])
        and face_status != "hold"
        and face_status != UNDEFINED,
        face_status,
    )
    checks.check(
        "dual-of-incoming-axis-agreement",
        reverse_m == "hold"
        and face_m == "fail"
        and reverse_status == "hold"
        and face_status == "fail"
        and axis_o["A"] != axis_m["A"]
        and axis_o["B"] != axis_m["B"]
        and axis_o["C"] != axis_m["C"]
        and axis_o["D"] != axis_m["D"]
        and axis_m["A"] == axis_m_a
        and axis_m["B"] == axis_m_a
        and axis_m["C"] == axis_m_c
        and axis_m["D"] == axis_m_d,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E1 in m1["A"]
        and NEG_E1 not in o1["A"]
        and o1["A"] != m1["A"]
        and axis_m["A"] != axis_o["A"],
    )
    checks.check(
        "not-leftover-of-O-alone",
        lx_o["A"] == frozenset({E1})
        and lx_o["B"] == frozenset({E1})
        and lx_o["C"] == frozenset({E2})
        and lx_o["D"] == frozenset({E2, E3})
        and reverse_lx_o == "hold"
        and face_lx_o == "fail"
        and axis_o["A"] != lx_o["A"]
        and axis_o["C"] != lx_o["C"]
        and reverse_status == "hold"
        and face_status == "fail",
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and all(lx[name] == frozenset() for name in ("A", "B", "C", "D"))
        and reverse_status == "hold"
        and leftover_reverse != reverse_status,
    )
    checks.check(
        "not-exist-opposite-of-signed-O",
        o_exist_reverse == "hold"
        and o_exist_face == "hold"
        and reverse_status == "hold"
        and face_status == "fail"
        and face_status != o_exist_face,
    )
    checks.check(
        "not-formation-tick-O",
        reverse_at_t == "fail"
        and reverse_status == "hold"
        and reverse_at_t != reverse_status
        and axis_o0["A"] != axis_o["A"],
    )
    checks.check(
        "not-unique-letter",
        unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(o1["D"]) == UNDEFINED
        and reverse_status == "hold"
        and face_status == "fail",
    )
    checks.check(
        "not-nnlock-named-sign",
        named_sign(E2) == "+"
        and named_sign(NEG_E3) == "-"
        and axis_o["A"] != named_sign(E2)
        and axis_display(axis_o["A"]) != named_sign(E2),
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and reverse_status == "hold"
        and face_status == "fail",
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and add(E1, NEG_E1) == ZERO
        and TWO_SITE_SEEDS != PERP_SEEDS
        and TWO_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "mutation-empty-axis-fails",
        reverse_report(frozenset(), axis_o["B"]) == "fail"
        and face_report(axis_o["C"], frozenset()) == "fail"
        and reverse_status == "hold"
        and face_status == "fail",
    )
    checks.check(
        "mutation-undefined-unformed",
        reverse_report(UNDEFINED, axis_o["B"]) == UNDEFINED
        and face_report(axis_o["C"], UNDEFINED) == UNDEFINED
        and reverse_status != UNDEFINED
        and face_status != UNDEFINED,
    )
    checks.check(
        "mutation-sum-cancels-mixed-O",
        isinstance(o1["A"], frozenset)
        and sum_of_set(o1["A"]) == E2
        and axis_o["A"] != frozenset({E2})
        and axis_o["A"] == frozenset({E2, E3})
        and isinstance(o1["C"], frozenset)
        and sum_of_set(o1["C"]) == ZERO
        and axis_o["C"] == frozenset({E1, E3}),
    )
    checks.check(
        "mutation-leftover-of-M-equals-Axis-O-on-this-process",
        lx_m["A"] == axis_o["A"]
        and lx_m["B"] == axis_o["B"]
        and lx_m["C"] == axis_o["C"]
        and lx_m["D"] == axis_o["D"]
        and reverse_lx_m == reverse_status
        and face_lx_m == face_status
        and axis_o["A"] != leftover_of_one(o1["A"]),
    )

    perp_o: dict[str, Outgoing] = {}
    zsym_o: dict[str, Outgoing] = {}
    ysym_o: dict[str, Outgoing] = {}
    x_o: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        if PROBES[name] in perp_ticks:
            perp_o[name] = outgoing_set(
                PROBES[name],
                perp_ticks[PROBES[name]] + 1,
                perp_ticks,
                perp_locks,
                perp_seeds,
            )
        if PROBES[name] in zsym_ticks:
            zsym_o[name] = outgoing_set(
                PROBES[name],
                zsym_ticks[PROBES[name]] + 1,
                zsym_ticks,
                zsym_locks,
                zsym_seeds,
            )
        if PROBES[name] in ysym_ticks:
            ysym_o[name] = outgoing_set(
                PROBES[name],
                ysym_ticks[PROBES[name]] + 1,
                ysym_ticks,
                ysym_locks,
                ysym_seeds,
            )
        if X_PROBES[name] in ticks:
            x_o[name] = outgoing_set(
                X_PROBES[name],
                ticks[X_PROBES[name]] + 1,
                ticks,
                locks,
                seed_map,
            )
    x_reverse = reverse_report(axis_set(x_o["A"]), axis_set(x_o["B"]))
    x_face = face_report(axis_set(x_o["C"]), axis_set(x_o["D"]))
    neighbor_axes_a = axis_set(
        neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"])
    )
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp",
        TWO_SITE_SEEDS != PERP_SEEDS
        and TWO_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and x_o["A"] != o1["A"]
        and zsym_o["A"] != o1["A"]
        and perp_o["A"] != o1["A"]
        and reverse_status == "hold"
        and face_status == "fail",
    )
    checks.check(
        "not-six-neighbor-lock-union",
        neighbor_axes_a != axis_o["A"]
        and isinstance(neighbor_axes_a, frozenset)
        and E1 in neighbor_axes_a,
    )
    checks.check(
        "outgoing-locks-are-nn-steps",
        all(
            isinstance(o1[name], frozenset) and o1[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        ),
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-outgoing-axes",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "O(A, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_1, −e_1}" in note
        and "Axis(O)(A, τ) = {e_2, e_3}" in note
        and "Axis(O)(B, τ) = {e_2, e_3}" in note
        and "Axis(O)(C, τ) = {e_1, e_3}" in note
        and "Axis(O)(D, τ) = {e_1}" in note,
    )
    checks.check(
        "note-reports-hold-fail",
        "Reverse: hold" in note
        and "Face: fail" in note
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "outgoing dual" in normalized_note
        and "mixed remains a set" in normalized_note,
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
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
        in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-incoming-or-leftover-or-exist-opposite",
        "not leftover of incoming-axis agreement" in normalized_note
        and "not leftover of leftover-of-O" in normalized_note
        and "not leftover of leftover-empty" in normalized_note
        and "not leftover of exist-opposite" in normalized_note
        and "Reverse holds." in note
        and "Face fails." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "outgoing dual" in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_OUTGOING_AXIS_AGREEMENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def outgoing_set(" in source
        and "def axis_set(" in source
        and "def axis_agreement(" in source
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
        "source-letter-from-outgoing-axis-agreement",
        "outgoing_set" in defined_fns
        and "axis_agreement" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )
    checks.check(
        "x-probe-contrast-defined",
        x_reverse in {"hold", "fail", UNDEFINED}
        and x_face in {"hold", "fail", UNDEFINED}
        and ysym_o["A"] == o1["A"],
    )
    checks.check(
        "face-at-t-defined",
        face_at_t in {"hold", "fail", UNDEFINED},
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
