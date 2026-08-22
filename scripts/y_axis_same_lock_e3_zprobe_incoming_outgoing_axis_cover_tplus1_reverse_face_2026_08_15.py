#!/usr/bin/env python3
"""Axis-cover of M and O at t+1 reverse/face on four #7198 z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_3 and +e_3 (y-axis same-lock; same process
and z-probes as nsye3sz #7198). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. t(q) is the formation
tick. tau = t+1 is per-probe. M(q, tau) is the set of earliest incoming
nearest-neighbor steps at q using only records with tick <= tau. Unformed
at tau => UNDEFINED. O(q, tau) is the outgoing dual of M: the set of e in
{±e_1,±e_2,±e_3} such that q+e is formed and e is in M(q+e, tau). Unformed
q at tau => UNDEFINED. Empty O is empty, not UNDEFINED. Axis(S) is the
unsigned lattice directions of signed locks in S. Cover HOLD at q iff
Axis(M) intersect Axis(O) is empty and Axis(M) union Axis(O) equals
{e_1,e_2,e_3}. UNDEFINED if M or O is UNDEFINED. Else fail. Reverse HOLD
iff cover at A and at B. Face HOLD iff cover at C and at D. Either side
UNDEFINED is UNDEFINED. Uniqueness of locks is not required. Occupancy of
sites is not used. Named-sign lettering is not used. No six-neighbor star.
No larger host. Not leftover-axis reverse. Not exist-opposite of signed
locks. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_AXIS_SAME_LOCK_E3_ZPROBE_INCOMING_OUTGOING_AXIS_COVER_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_AXIS_SAME_LOCK_E3_ZPROBE_INCOMING_OUTGOING_AXIS_COVER_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E2, E3),
)
OPPOSITE_E3_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E2, NEG_E3),
)
Y_AXIS_E2_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E2, NEG_E2),
)
NNSEED_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
SAME_E1_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
}
Y_PROBES = {
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
    "Axis-cover of M and O at t+1 on the four #7198 z-probes, "
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


def leftover_axis(incoming: Incoming, outgoing: Outgoing) -> AxisSet:
    """Lx leftover contrast: {e_1,e_2,e_3} minus (Axis(M) union Axis(O))."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    return frozenset(AXES) - (axes_m | axes_o)


def leftover_of_one(value: Incoming) -> AxisSet:
    """One-sided leftover contrast. Not this letter."""
    occupied = axis_set(value)
    if occupied == UNDEFINED:
        return UNDEFINED
    if not isinstance(occupied, frozenset):
        raise TypeError("one-sided leftover needs an axis set")
    return frozenset(AXES) - occupied


def leftover_match(left: AxisSet, right: AxisSet) -> str:
    """Leftover reverse contrast: nonempty equal leftovers. Empty => fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("leftover sides must be axis sets or UNDEFINED")
    if not left or not right:
        return "fail"
    if left == right:
        return "hold"
    return "fail"


def cover_report(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff Axis(M) intersect Axis(O) empty and union equals {e_1,e_2,e_3}."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("cover sides must be axis sets or UNDEFINED")
    if axes_m.isdisjoint(axes_o) and (axes_m | axes_o) == frozenset(AXES):
        return "hold"
    return "fail"


def both_hold(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. Either UNDEFINED is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(cover_a: str, cover_b: str) -> str:
    """Reverse HOLD iff cover at A and cover at B."""
    return both_hold(cover_a, cover_b)


def face_report(cover_c: str, cover_d: str) -> str:
    """Face HOLD iff cover at C and cover at D."""
    return both_hold(cover_c, cover_d)


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


def new_records_meeting_six_nn(
    site: Point,
    ticks: dict[Point, int],
) -> tuple[Point, ...]:
    """Records in B_3(0) that form at t(site)+1 and are 6-NN of site."""
    formation = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] == formation + 1:
            found.append(neighbor)
    return tuple(found)


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


def probe_cover(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = cover_report(
            incoming_set(
                site, site_ticks[site] + 1, site_ticks, site_locks, site_seeds
            ),
            outgoing_set(
                site, site_ticks[site] + 1, site_ticks, site_locks, site_seeds
            ),
        )
    return out


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("axis-cover of M and O reverse/face at t+1 on #7198 z-probes")
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
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-z-probes-in-host",
        probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (1, 0, 1))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != y_probe_sites
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
        and add(E3, E3) != ZERO
        and dot(E1, E3) == 0
        and perpendicular(E3, E1)
        and perpendicular(E3, E2)
        and not perpendicular(E3, E3)
        and in_ball(PROBES["C"])
        and not in_ball((0, 0, 4)),
    )
    checks.check(
        "axis-identity",
        axis_set(UNDEFINED) == UNDEFINED
        and axis_set(frozenset({NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E1, NEG_E1, E2})) == frozenset({E1, E2})
        and axis_set(frozenset({E3})) == frozenset({E3})
        and axis_set(frozenset({E1, NEG_E1, E2, NEG_E2})) == frozenset({E1, E2}),
    )
    checks.check(
        "cover-identity",
        cover_report(UNDEFINED, frozenset({E1})) == UNDEFINED
        and cover_report(frozenset({E1}), UNDEFINED) == UNDEFINED
        and cover_report(frozenset({E1, NEG_E1, E2}), frozenset({E3})) == "hold"
        and cover_report(frozenset({E3}), frozenset({E1, NEG_E1, E2})) == "hold"
        and cover_report(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == "hold"
        and cover_report(frozenset({E1}), frozenset({E1})) == "fail"
        and cover_report(frozenset({E1}), frozenset({E2})) == "fail"
        and cover_report(frozenset({E1, E2, E3}), frozenset({E1, E2, E3})) == "fail"
        and leftover_axis(frozenset({E1, E2, E3}), frozenset({E1, E2, E3}))
        == frozenset()
        and cover_report(frozenset({E1, E2}), frozenset()) == "fail",
    )
    checks.check(
        "both-hold-identity",
        both_hold(UNDEFINED, "hold") == UNDEFINED
        and both_hold("hold", UNDEFINED) == UNDEFINED
        and both_hold("hold", "hold") == "hold"
        and both_hold("hold", "fail") == "fail"
        and both_hold("fail", "fail") == "fail"
        and leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_match(frozenset({E1}), frozenset({E1})) == "hold"
        and leftover_match(frozenset({E3}), frozenset({E1, E2})) == "fail",
    )

    ticks, locks, seed_map = form()
    opp_ticks, opp_locks, opp_seeds = form(OPPOSITE_E3_SEEDS)
    e2_ticks, e2_locks, e2_seeds = form(Y_AXIS_E2_SEEDS)
    nnseed_ticks, nnseed_locks, nnseed_seeds = form(NNSEED_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(NSOPP_SEEDS)
    same_e1_ticks, same_e1_locks, same_e1_seeds = form(SAME_E1_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    axis_m: dict[str, AxisSet] = {}
    axis_o: dict[str, AxisSet] = {}
    cover: dict[str, str] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        axis_m[name] = axis_set(m1[name])
        axis_o[name] = axis_set(o1[name])
        cover[name] = cover_report(m1[name], o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"Axis(M)={axis_display(axis_m[name])} "
            f"Axis(O)={axis_display(axis_o[name])} "
            f"cover={cover[name]}"
        )

    reverse = reverse_report(cover["A"], cover["B"])
    face = face_report(cover["C"], cover["D"])
    leftover_reverse = leftover_match(lx["A"], lx["B"])
    leftover_face = leftover_match(lx["C"], lx["D"])
    reverse_m_alone = leftover_match(lx_m["A"], lx_m["B"])
    face_m_alone = leftover_match(lx_m["C"], lx_m["D"])
    reverse_o_alone = leftover_match(lx_o["A"], lx_o["B"])
    face_o_alone = leftover_match(lx_o["C"], lx_o["D"])
    m_exist_reverse = existential_opposite(m1["A"], m1["B"])
    m_exist_face = existential_opposite(m1["C"], m1["D"])
    o_exist_reverse = existential_opposite(o1["A"], o1["B"])
    o_exist_face = existential_opposite(o1["C"], o1["D"])
    unique_cover_a = cover_report(unique_letter(m1["A"]), unique_letter(o1["A"]))
    cover_at_t = {
        name: cover_report(m0[name], o0[name]) for name in ("A", "B", "C", "D")
    }
    print(f"cover reverse={reverse} face={face}")
    print(
        "per_element: each unsigned lattice axis among {e_1,e_2,e_3} "
        "occupied by M or by O at a probe's t+1"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four cover bits, reverse/face from cover at A,B and at C,D")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E3, NEG_E3)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E3, NEG_E3)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[ORIGIN] == 0
        and ticks[E2] == 0
        and ticks[E1] == 1
        and ticks[NEG_E1] == 1
        and ticks[NEG_E2] == 1
        and ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and cover_report(
            incoming_set(PROBES["B"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED
        and cover_report(
            incoming_set(PROBES["A"], 2, ticks, locks, seed_map),
            outgoing_set(PROBES["A"], 2, ticks, locks, seed_map),
        )
        == UNDEFINED
        and cover_report(
            incoming_set(PROBES["C"], 3, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 3, ticks, locks, seed_map),
        )
        == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E3})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({E3})
        and PROBES["A"] not in seed_map
        and m1["A"] == frozenset({E1, NEG_E1, E2}),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau",
        m1["A"] == frozenset({E1, NEG_E1, E2})
        and m1["B"] == frozenset({E3})
        and m1["C"] == frozenset({E3})
        and m1["D"] == frozenset({E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E3})
        and o1["B"] == frozenset({E1, NEG_E1, E2})
        and o1["C"] == frozenset({E1, NEG_E1, NEG_E2})
        and o1["D"] == frozenset({E1, NEG_E1, NEG_E2}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Axis-M-and-O",
        axis_m["A"] == frozenset({E1, E2})
        and axis_o["A"] == frozenset({E3})
        and axis_m["B"] == frozenset({E3})
        and axis_o["B"] == frozenset({E1, E2})
        and axis_m["C"] == frozenset({E3})
        and axis_o["C"] == frozenset({E1, E2})
        and axis_m["D"] == frozenset({E3})
        and axis_o["D"] == frozenset({E1, E2}),
        str(
            {
                name: (axis_display(axis_m[name]), axis_display(axis_o[name]))
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-cover-hold",
        all(cover[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(
            isinstance(axis_m[name], frozenset)
            and isinstance(axis_o[name], frozenset)
            and axis_m[name].isdisjoint(axis_o[name])
            and axis_m[name] | axis_o[name] == frozenset(AXES)
            for name in ("A", "B", "C", "D")
        ),
        str({name: cover[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-O-empty-at-t-fills-at-tplus1",
        all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(cover_at_t[name] == "fail" for name in ("A", "B", "C", "D"))
        and all(cover[name] == "hold" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((0, 0, 2),)
        and new_meet["B"] == ((2, 1, 1), (0, 1, 1), (1, 2, 1))
        and new_meet["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new_meet["D"] == ((2, 0, 1), (0, 0, 1), (1, -1, 1)),
        str(new_meet),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(m1["A"], frozenset)
        and len(m1["A"]) == 3
        and unique_letter(m1["A"]) == UNDEFINED
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and cover["A"] == "hold"
        and cover["B"] == "hold",
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E3
        and PROBES["A"] not in seed_map
        and ticks[E3] == 3
        and locks[E3] == {E1, NEG_E1, E2}
        and Y_PROBES["A"] != PROBES["A"]
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem2-reverse-cover-hold",
        reverse == "hold"
        and cover["A"] == "hold"
        and cover["B"] == "hold"
        and reverse != UNDEFINED
        and reverse != "fail",
        reverse,
    )
    checks.check(
        "theorem3-face-cover-hold",
        face == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "hold"
        and face != UNDEFINED
        and face != "fail",
        face,
    )
    checks.check(
        "mutation-leftover-empty-fails-leftover-reverse",
        all(lx[name] == frozenset() for name in ("A", "B", "C", "D"))
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-leftover-of-M-alone-differs",
        lx_m["A"] == frozenset({E3})
        and lx_m["B"] == frozenset({E1, E2})
        and lx_m["C"] == frozenset({E1, E2})
        and lx_m["D"] == frozenset({E1, E2})
        and reverse_m_alone == "fail"
        and face_m_alone == "hold"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-leftover-of-O-alone-differs",
        lx_o["A"] == frozenset({E1, E2})
        and lx_o["B"] == frozenset({E3})
        and lx_o["C"] == frozenset({E3})
        and lx_o["D"] == frozenset({E3})
        and reverse_o_alone == "fail"
        and face_o_alone == "hold"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-exist-opposite-of-M-fails",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and reverse == "hold"
        and face == "hold"
        and cover_report(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and existential_opposite(frozenset({E1}), frozenset({NEG_E1})) == "hold"
        and existential_opposite(frozenset({E1, NEG_E1, E2}), frozenset({E3}))
        == "fail"
        and existential_opposite(frozenset({E3}), frozenset({E3})) == "fail",
    )
    checks.check(
        "mutation-exist-opposite-of-O-is-not-cover",
        o_exist_reverse == "fail"
        and o_exist_face == "hold"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-M",
        unique_letter(m1["A"]) == UNDEFINED
        and unique_letter(o1["A"]) == frozenset({E3})
        and unique_letter(m1["B"]) == frozenset({E3})
        and unique_cover_a == UNDEFINED
        and cover["A"] == "hold",
    )
    checks.check(
        "mutation-shared-axis-fails-even-if-leftover-empty",
        leftover_axis(frozenset({E1, E2, E3}), frozenset({E1, E2, E3}))
        == frozenset()
        and cover_report(frozenset({E1, E2, E3}), frozenset({E1, E2, E3})) == "fail"
        and cover["A"] == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["B"], frozenset)
        and sum_of_set(m1["A"]) == E2
        and sum_of_set(m1["B"]) == E3
        and sum_of_set(o1["A"]) == E3
        and axis_m["A"] != frozenset({E2})
        and axis_m["A"] == frozenset({E1, E2}),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E3 in o1["A"]
        and E3 not in m1["A"]
        and o1["A"] != m1["A"]
        and axis_m["A"] != axis_o["A"]
        and o1["B"] != m1["B"],
    )

    x_cover = probe_cover(X_PROBES, ticks, locks, seed_map)
    y_cover = probe_cover(Y_PROBES, ticks, locks, seed_map)
    opp_cover = probe_cover(PROBES, opp_ticks, opp_locks, opp_seeds)
    e2_cover = probe_cover(PROBES, e2_ticks, e2_locks, e2_seeds)
    nnseed_cover = probe_cover(PROBES, nnseed_ticks, nnseed_locks, nnseed_seeds)
    nsopp_cover = probe_cover(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    same_e1_cover = probe_cover(PROBES, same_e1_ticks, same_e1_locks, same_e1_seeds)
    x_reverse = reverse_report(x_cover["A"], x_cover["B"])
    y_reverse = reverse_report(y_cover["A"], y_cover["B"])
    e2_reverse = reverse_report(e2_cover["A"], e2_cover["B"])
    e2_face = face_report(e2_cover["C"], e2_cover["D"])
    nnseed_reverse = reverse_report(nnseed_cover["A"], nnseed_cover["B"])
    nnseed_face = face_report(nnseed_cover["C"], nnseed_cover["D"])
    x_m_a = incoming_set(
        X_PROBES["A"], ticks[X_PROBES["A"]] + 1, ticks, locks, seed_map
    )
    y_m_a = incoming_set(
        Y_PROBES["A"], ticks[Y_PROBES["A"]] + 1, ticks, locks, seed_map
    )
    checks.check(
        "not-x-probes-or-y-probes",
        probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and X_PROBES["A"] == E1
        and Y_PROBES["A"] == E2
        and ticks[X_PROBES["A"]] == 1
        and ticks[Y_PROBES["A"]] == 0
        and Y_PROBES["A"] in seed_map
        and PROBES["A"] not in seed_map
        and x_m_a == frozenset({E1})
        and y_m_a == frozenset({E3})
        and m1["A"] == frozenset({E1, NEG_E1, E2})
        and x_cover["A"] == "hold"
        and y_cover["A"] == "hold"
        and x_reverse == "hold"
        and y_reverse == "hold"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "not-nnseed-or-y-axis-e2",
        TWO_SITE_SEEDS != NNSEED_SEEDS
        and TWO_SITE_SEEDS != Y_AXIS_E2_SEEDS
        and nnseed_cover["B"] == "fail"
        and nnseed_reverse == "fail"
        and nnseed_face == "hold"
        and e2_cover["B"] == "fail"
        and e2_cover["D"] == "fail"
        and e2_reverse == "fail"
        and e2_face == "fail"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "not-opposite-e3-or-nsopp-or-same-e1",
        TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and TWO_SITE_SEEDS != NSOPP_SEEDS
        and TWO_SITE_SEEDS != SAME_E1_SEEDS
        and locks[E2] == {E3}
        and opp_seeds[E2] == NEG_E3
        and nsopp_seeds[ORIGIN] == E1
        and same_e1_seeds[E2] == E1
        and opp_cover["A"] == "hold"
        and nsopp_cover["A"] == "hold"
        and same_e1_cover["A"] == "hold"
        and incoming_set(
            PROBES["A"],
            nsopp_ticks[PROBES["A"]] + 1,
            nsopp_ticks,
            nsopp_locks,
            nsopp_seeds,
        )
        == frozenset({E3})
        and m1["A"] == frozenset({E1, NEG_E1, E2})
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "y-axis-same-lock-e3-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E3}
        and ticks[E2] == 0
        and locks[E2] == {E3}
        and add(E3, E3) != ZERO
        and TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and TWO_SITE_SEEDS != Y_AXIS_E2_SEEDS
        and TWO_SITE_SEEDS != NNSEED_SEEDS
        and TWO_SITE_SEEDS != NSOPP_SEEDS
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 3
        and len(m1["B"]) == 1
        and len(o1["A"]) == 1
        and len(o1["B"]) == 3
        and reverse == "hold"
        and face == "hold",
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-Axis-cover",
        "t(A)=3" in note
        and "t(B)=2" in note
        and "t(C)=4" in note
        and "t(D)=2" in note
        and "M(A, τ) = {+e_1, −e_1, +e_2}" in note
        and "M(B, τ) = {+e_3}" in note
        and "M(C, τ) = {+e_3}" in note
        and "M(D, τ) = {+e_3}" in note
        and "O(A, τ) = {+e_3}" in note
        and "O(B, τ) = {+e_1, −e_1, +e_2}" in note
        and "O(C, τ) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ) = {+e_1, −e_1, −e_2}" in note
        and "Axis(M)(A, τ) = {e_1, e_2}" in note
        and "Axis(O)(A, τ) = {e_3}" in note
        and "Axis(M)(B, τ) = {e_3}" in note
        and "Axis(O)(B, τ) = {e_1, e_2}" in note
        and "Axis(M)(C, τ) = {e_3}" in note
        and "Axis(O)(C, τ) = {e_1, e_2}" in note
        and "Axis(M)(D, τ) = {e_3}" in note
        and "Axis(O)(D, τ) = {e_1, e_2}" in note
        and "cover(A) = hold" in note
        and "cover(B) = hold" in note
        and "cover(C) = hold" in note
        and "cover(D) = hold" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (0, 0, 2)" in note
        and "new 6-NN of B at t(B)+1: (2, 1, 1), (0, 1, 1), (1, 2, 1)" in note
        and "new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)" in note
        and "new 6-NN of D at t(D)+1: (2, 0, 1), (0, 0, 1), (1, -1, 1)" in note,
    )
    checks.check(
        "note-reports-cover-reverse-face",
        "Reverse axis cover at τ: hold" in note
        and "Face axis cover at τ: hold" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-leftover-or-exist-opposite",
        "not leftover-axis reverse" in normalized_note
        and "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover-of-`O` alone" in normalized_note
        and "O is not M" in note
        and "exist-opposite of signed M fails" in normalized_note,
    )
    checks.check(
        "note-not-star-or-occupancy",
        "does not use a six-neighbor star" in normalized_note
        and "does not use occupancy" in normalized_note
        and "A is not a seed" in note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ(q)=t(q)+1" in note.replace(" ", ""),
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
        '    "docs/Y_AXIS_SAME_LOCK_E3_ZPROBE_INCOMING_OUTGOING_AXIS_COVER_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "axis_set" in defined_fns
        and "cover_report" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 3
        and set(ticks) <= host,
    )
    checks.check(
        "source-letter-from-axis-cover",
        "cover_report" in defined_fns
        and "both_hold" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and "inner_product" not in defined_fns,
    )
    _ = (o0, unique_cover_a, same_e1_cover)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
