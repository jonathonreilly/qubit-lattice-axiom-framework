#!/usr/bin/env python3
"""1-in 2-out axis split of M and O at t+1 reverse/face on four x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin +e_1, (0,1,0) -e_1, (0,0,1) +e_2,
(0,1,1) -e_2. Same process and x-probes as nm2axx. A 6-NN step is allowed
iff it is perpendicular to the parent lock axis. Newly formed sites lock
the incoming step. Seeds keep their seed letters as a singleton. t(q) is
the formation tick. tau = t+1 is per-probe. M(q, tau) is the set of
earliest incoming nearest-neighbor steps at q using only records with
tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is the outgoing dual
of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is formed and e is in
M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is empty, not
UNDEFINED. Axis(S) is the unsigned lattice directions of signed locks in
S. Cover HOLD at q iff Axis(M) intersect Axis(O) is empty and Axis(M)
union Axis(O) equals {e_1,e_2,e_3}. Split HOLD at q iff cover HOLD and
|Axis(M)|=1. UNDEFINED if M or O is UNDEFINED. Else fail. Reverse HOLD
iff split at A and at B. Face HOLD iff split at C and at D. Either side
UNDEFINED is UNDEFINED. Cover FAIL on these x-probes; |Axis(M)|=1 at each
so split equals cover on this member. Uniqueness of locks is not required.
Occupancy of sites is not used. Named-sign lettering is not used. No
six-neighbor star. No larger host. Not leftover of cover reverse on
1-axis x-probes. Not leftover of y-probes on this seed. Not leftover of
same-lock two-axis. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_INCOMING_OUTGOING_ONE_TWO_SPLIT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_INCOMING_OUTGOING_ONE_TWO_SPLIT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
YZ: Point = (0, 1, 1)
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
TWO_AXIS_OPPOSITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (YZ, NEG_E2),
)
TWO_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    (YZ, E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
NNSEED_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
Y_AXIS_E2_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E2, NEG_E2),
)
SAME_E1_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
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
    "D": (1, 0, 1),
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
    "1-in 2-out axis split of M and O at t+1 on the four x-probes "
    "of the two-axis opposite seed, and reverse/face from that, are reported. "
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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_OPPOSITE_SEEDS,
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
    """Leftover contrast: {e_1,e_2,e_3} minus (Axis(M) union Axis(O))."""
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


def axis_count(value: AxisSet) -> int | str:
    """Cardinality of an unsigned axis set. UNDEFINED if unformed."""
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"axis set is not an axis set: {value!r}")
    return len(value)


def split_report(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff cover HOLD and |Axis(M)|=1. Else fail, or UNDEFINED if unformed."""
    cover = cover_report(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    axes_m = axis_set(incoming)
    if axes_m == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset):
        raise TypeError("split needs an Axis(M) set or UNDEFINED")
    if cover == "hold" and len(axes_m) == 1:
        return "hold"
    return "fail"


def both_hold(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. Either UNDEFINED is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(split_a: str, split_b: str) -> str:
    """Reverse HOLD iff split at A and split at B."""
    return both_hold(split_a, split_b)


def face_report(split_c: str, split_d: str) -> str:
    """Face HOLD iff split at C and split at D."""
    return both_hold(split_c, split_d)


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


def probe_split(
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
        out[name] = split_report(
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

    print("1-in 2-out axis split of M and O reverse/face at t+1 on two-axis x-probes")
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
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-x-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != y_probe_sites
        and probe_sites != z_probe_sites,
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
        and add(E2, E3) == YZ
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and perpendicular(E1, E3)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "axis-identity",
        axis_set(UNDEFINED) == UNDEFINED
        and axis_set(frozenset({NEG_E3})) == frozenset({E3})
        and axis_set(frozenset({E1, NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E2, E3, NEG_E3})) == frozenset({E2, E3}),
    )
    checks.check(
        "cover-identity",
        cover_report(UNDEFINED, frozenset({E1})) == UNDEFINED
        and cover_report(frozenset({E1}), UNDEFINED) == UNDEFINED
        and cover_report(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and cover_report(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and cover_report(frozenset({E1}), frozenset({E2})) == "fail"
        and cover_report(frozenset({E1, E2, E3}), frozenset({E1, E2, E3})) == "fail"
        and leftover_axis(frozenset({NEG_E3}), frozenset({E1})) == frozenset({E2}),
    )
    checks.check(
        "both-hold-identity",
        both_hold(UNDEFINED, "hold") == UNDEFINED
        and both_hold("hold", UNDEFINED) == UNDEFINED
        and both_hold("hold", "hold") == "hold"
        and both_hold("hold", "fail") == "fail"
        and leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_match(frozenset({E2}), frozenset()) == "fail"
        and leftover_match(frozenset({E2}), frozenset({E2})) == "hold",
    )
    checks.check(
        "split-identity",
        split_report(UNDEFINED, frozenset({E1})) == UNDEFINED
        and split_report(frozenset({E1}), UNDEFINED) == UNDEFINED
        and split_report(frozenset({E1}), frozenset({E2, NEG_E2, E3})) == "hold"
        and split_report(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and split_report(frozenset({E1, E2}), frozenset({E3})) == "fail"
        and axis_count(frozenset({E3})) == 1
        and axis_count(frozenset({E1, E2})) == 2
        and axis_count(UNDEFINED) == UNDEFINED,
    )

    ticks, locks, seed_map = form()
    same_ticks, same_locks, same_seeds = form(TWO_AXIS_SAME_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(NSOPP_SEEDS)
    nnseed_ticks, nnseed_locks, nnseed_seeds = form(NNSEED_SEEDS)
    e2_ticks, e2_locks, e2_seeds = form(Y_AXIS_E2_SEEDS)
    same_e1_ticks, same_e1_locks, same_e1_seeds = form(SAME_E1_SEEDS)
    tau0: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    axis_m: dict[str, AxisSet] = {}
    axis_o: dict[str, AxisSet] = {}
    cover: dict[str, str] = {}
    n_axis_m: dict[str, int | str] = {}
    split: dict[str, str] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau0[name] + 1, ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau0[name] + 1, ticks, locks, seed_map)
        axis_m[name] = axis_set(m1[name])
        axis_o[name] = axis_set(o1[name])
        cover[name] = cover_report(m1[name], o1[name])
        n_axis_m[name] = axis_count(axis_m[name])
        split[name] = split_report(m1[name], o1[name])
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
            f"|Axis(M)|={n_axis_m[name]} "
            f"cover={cover[name]} "
            f"split={split[name]}"
        )

    cover_reverse = both_hold(cover["A"], cover["B"])
    cover_face = both_hold(cover["C"], cover["D"])
    reverse = reverse_report(split["A"], split["B"])
    face = face_report(split["C"], split["D"])
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
    unique_split_a = split_report(unique_letter(m1["A"]), unique_letter(o1["A"]))
    unique_cover_b = cover_report(unique_letter(m1["B"]), unique_letter(o1["B"]))
    unique_split_b = split_report(unique_letter(m1["B"]), unique_letter(o1["B"]))
    cover_at_t = {
        name: cover_report(m0[name], o0[name]) for name in ("A", "B", "C", "D")
    }
    split_at_t = {
        name: split_report(m0[name], o0[name]) for name in ("A", "B", "C", "D")
    }
    print(
        f"split reverse={reverse} face={face} "
        f"cover reverse={cover_reverse} face={cover_face}"
    )
    print(
        "per_element: each unsigned lattice axis among {e_1,e_2,e_3} "
        "occupied by M or by O at a probe's t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four split bits, reverse/face from 1-in 2-out at A,B and at C,D"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    second_pair_e2_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and second_pair_e2_parallel_blocked
        and ticks[ORIGIN] == 0
        and ticks[E2] == 0
        and ticks[E3] == 0
        and ticks[YZ] == 0
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and split_report(
            incoming_set(PROBES["A"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["A"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED
        and split_report(
            incoming_set(PROBES["D"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["D"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED
        and split_report(
            incoming_set(PROBES["C"], 2, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 2, ticks, locks, seed_map),
        )
        == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(YZ, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and PROBES["A"] not in seed_map
        and m1["A"] == frozenset({NEG_E3}),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau",
        m1["A"] == frozenset({NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({NEG_E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E1})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Axis-M-and-O",
        axis_m["A"] == frozenset({E3})
        and axis_o["A"] == frozenset({E1})
        and axis_m["B"] == frozenset({E1})
        and axis_o["B"] == frozenset({E2, E3})
        and axis_m["C"] == frozenset({E1})
        and axis_o["C"] == frozenset({E2, E3})
        and axis_m["D"] == frozenset({E3})
        and axis_o["D"] == frozenset({E1}),
    )
    checks.check(
        "theorem1-cover-fail-at-A-and-D",
        cover["A"] == "fail"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "fail"
        and lx["A"] == frozenset({E2})
        and lx["D"] == frozenset({E2})
        and lx["B"] == frozenset()
        and lx["C"] == frozenset(),
        str({name: cover[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Axis-M-card-one",
        n_axis_m["A"] == 1
        and n_axis_m["B"] == 1
        and n_axis_m["C"] == 1
        and n_axis_m["D"] == 1
        and axis_count(axis_o["A"]) == 1
        and axis_count(axis_o["B"]) == 2
        and axis_count(axis_o["C"]) == 2
        and axis_count(axis_o["D"]) == 1,
        str({name: n_axis_m[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-split-equals-cover",
        split["A"] == "fail"
        and split["B"] == "hold"
        and split["C"] == "hold"
        and split["D"] == "fail"
        and split["A"] == cover["A"]
        and split["B"] == cover["B"]
        and split["C"] == cover["C"]
        and split["D"] == cover["D"]
        and all(n_axis_m[name] == 1 for name in ("A", "B", "C", "D")),
        str({name: split[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-O-fills-at-tplus1",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E1})
        and all(cover_at_t[name] == "fail" for name in ("A", "B", "C", "D"))
        and all(split_at_t[name] == "fail" for name in ("A", "B", "C", "D"))
        and o1["A"] == frozenset({E1})
        and o1["D"] == frozenset({E1, NEG_E1}),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0),)
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet["D"] == ((2, 1, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem1-mixed-O-stays-a-set",
        isinstance(m1["A"], frozenset)
        and len(m1["A"]) == 1
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 2
        and unique_letter(o1["D"]) == UNDEFINED
        and split["B"] == "hold"
        and split["D"] == "fail",
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and PROBES["A"] not in seed_map
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"]
        and Y_PROBES["A"] in seed_map
        and Z_PROBES["A"] in seed_map,
    )
    checks.check(
        "theorem2-reverse-split-fail",
        reverse == "fail"
        and split["A"] == "fail"
        and split["B"] == "hold"
        and cover["A"] == "fail"
        and cover["B"] == "hold"
        and cover_reverse == "fail"
        and reverse == cover_reverse
        and reverse != UNDEFINED,
        reverse,
    )
    checks.check(
        "theorem3-face-split-fail",
        face == "fail"
        and split["C"] == "hold"
        and split["D"] == "fail"
        and cover["C"] == "hold"
        and cover["D"] == "fail"
        and cover_face == "fail"
        and face == cover_face
        and face != UNDEFINED,
        face,
    )
    checks.check(
        "mutation-leftover-empty-at-B-fails-leftover-reverse",
        lx["A"] == frozenset({E2})
        and lx["B"] == frozenset()
        and lx["C"] == frozenset()
        and lx["D"] == frozenset({E2})
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and reverse == "fail"
        and face == "fail",
    )
    checks.check(
        "mutation-leftover-of-M-alone-differs",
        lx_m["A"] == frozenset({E1, E2})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_m["C"] == frozenset({E2, E3})
        and lx_m["D"] == frozenset({E1, E2})
        and reverse_m_alone == "fail"
        and face_m_alone == "fail",
    )
    checks.check(
        "mutation-leftover-of-O-alone-differs",
        lx_o["A"] == frozenset({E2, E3})
        and lx_o["B"] == frozenset({E1})
        and lx_o["C"] == frozenset({E1})
        and lx_o["D"] == frozenset({E2, E3})
        and reverse_o_alone == "fail"
        and face_o_alone == "fail",
    )
    checks.check(
        "mutation-exist-opposite-of-M-fails",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and existential_opposite(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and existential_opposite(frozenset({E1}), frozenset({NEG_E1})) == "hold",
    )
    checks.check(
        "mutation-exist-opposite-of-O-is-not-split",
        o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and reverse == "fail"
        and face == "fail",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == frozenset({NEG_E3})
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_cover_a == "fail"
        and unique_split_a == "fail"
        and unique_cover_b == UNDEFINED
        and unique_split_b == UNDEFINED
        and split["A"] == "fail"
        and split["B"] == "hold"
        and unique_split_b != split["B"],
    )
    checks.check(
        "mutation-split-equals-cover-on-this-member",
        cover_reverse == "fail"
        and cover_face == "fail"
        and reverse == cover_reverse
        and face == cover_face
        and all(n_axis_m[name] == 1 for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "mutation-sum-is-not-axis",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["B"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E3
        and sum_of_set(m1["B"]) == E1
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["D"]) == ZERO
        and axis_o["D"] == frozenset({E1})
        and axis_o["D"] != frozenset({ZERO}),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E3 in m1["A"]
        and NEG_E3 not in o1["A"]
        and o1["A"] != m1["A"]
        and axis_m["A"] != axis_o["A"]
        and o1["B"] != m1["B"],
    )

    y_cover = probe_cover(Y_PROBES, ticks, locks, seed_map)
    y_split = probe_split(Y_PROBES, ticks, locks, seed_map)
    z_cover = probe_cover(Z_PROBES, ticks, locks, seed_map)
    z_split = probe_split(Z_PROBES, ticks, locks, seed_map)
    nsopp_cover = probe_cover(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    nsopp_split = probe_split(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    same_cover = probe_cover(PROBES, same_ticks, same_locks, same_seeds)
    same_split = probe_split(PROBES, same_ticks, same_locks, same_seeds)
    nnseed_split = probe_split(PROBES, nnseed_ticks, nnseed_locks, nnseed_seeds)
    e2_split = probe_split(PROBES, e2_ticks, e2_locks, e2_seeds)
    y_reverse = reverse_report(y_split["A"], y_split["B"])
    y_face = face_report(y_split["C"], y_split["D"])
    nsopp_cover_reverse = both_hold(nsopp_cover["A"], nsopp_cover["B"])
    nsopp_reverse = reverse_report(nsopp_split["A"], nsopp_split["B"])
    nsopp_face = face_report(nsopp_split["C"], nsopp_split["D"])
    same_d_o = outgoing_set(
        PROBES["D"],
        same_ticks[PROBES["D"]] + 1,
        same_ticks,
        same_locks,
        same_seeds,
    )
    checks.check(
        "not-y-probes-or-z-probes",
        probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and Y_PROBES["A"] == E2
        and Z_PROBES["A"] == E3
        and Y_PROBES["A"] in seed_map
        and Z_PROBES["A"] in seed_map
        and PROBES["A"] not in seed_map
        and y_cover["A"] == "hold"
        and y_cover["B"] == "hold"
        and y_split["A"] == "hold"
        and y_split["B"] == "hold"
        and y_reverse == "hold"
        and y_face == "fail"
        and reverse == "fail"
        and y_reverse != reverse
        and z_cover["A"] == "hold"
        and z_split["A"] == "hold",
        str((y_split, y_reverse, y_face, z_split)),
    )
    checks.check(
        "not-nsopp-one-axis-x-probes",
        TWO_AXIS_OPPOSITE_SEEDS != NSOPP_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in nsopp_ticks.values()) == 2
        and nsopp_ticks[E3] == 1
        and ticks[E3] == 0
        and nsopp_ticks[PROBES["A"]] == 3
        and ticks[PROBES["A"]] == 2
        and nsopp_cover["A"] == "hold"
        and nsopp_split["A"] == "fail"
        and nsopp_cover_reverse == "hold"
        and nsopp_reverse == "fail"
        and nsopp_face == "fail"
        and cover["A"] == "fail"
        and reverse == "fail"
        and cover_reverse != nsopp_cover_reverse
        and incoming_set(
            PROBES["A"],
            nsopp_ticks[PROBES["A"]] + 1,
            nsopp_ticks,
            nsopp_locks,
            nsopp_seeds,
        )
        == frozenset({E2, E3, NEG_E3})
        and m1["A"] == frozenset({NEG_E3}),
        str((nsopp_cover, nsopp_split)),
    )
    checks.check(
        "not-same-lock-two-axis",
        TWO_AXIS_OPPOSITE_SEEDS != TWO_AXIS_SAME_SEEDS
        and seed_map[E2] == NEG_E1
        and same_seeds[E2] == E1
        and seed_map[YZ] == NEG_E2
        and same_seeds[YZ] == E2
        and o1["D"] == frozenset({E1, NEG_E1})
        and same_d_o == frozenset({E1})
        and same_cover["A"] == "fail"
        and same_split["A"] == "fail"
        and same_cover["D"] == "fail"
        and o1["D"] != same_d_o,
    )
    checks.check(
        "not-nnseed-or-y-axis-e2-or-same-e1",
        TWO_AXIS_OPPOSITE_SEEDS != NNSEED_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != Y_AXIS_E2_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != SAME_E1_SEEDS
        and nnseed_split["A"] == "fail"
        and nnseed_split["B"] == "fail"
        and e2_split["B"] == "fail"
        and same_e1_seeds[E2] == E1
        and seed_map[E2] == NEG_E1,
    )
    checks.check(
        "two-axis-opposite-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[YZ] == 0
        and locks[YZ] == {NEG_E2}
        and add(E1, NEG_E1) == ZERO
        and add(E2, NEG_E2) == ZERO
        and sum(time == 0 for time in ticks.values()) == 4,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 1
        and len(o1["B"]) == 3
        and len(o1["D"]) == 2
        and reverse == "fail"
        and face == "fail",
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-Axis-cover-split",
        "t(A)=2" in note
        and "t(B)=1" in note
        and "t(C)=3" in note
        and "t(D)=2" in note
        and "M(A, τ) = {−e_3}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_1}" in note
        and "M(D, τ) = {−e_3}" in note
        and "O(A, τ) = {+e_1}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {−e_2, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_1, −e_1}" in note
        and "Axis(M)(A, τ) = {e_3}" in note
        and "Axis(O)(A, τ) = {e_1}" in note
        and "Axis(M)(B, τ) = {e_1}" in note
        and "Axis(O)(B, τ) = {e_2, e_3}" in note
        and "Axis(M)(C, τ) = {e_1}" in note
        and "Axis(O)(C, τ) = {e_2, e_3}" in note
        and "Axis(M)(D, τ) = {e_3}" in note
        and "Axis(O)(D, τ) = {e_1}" in note
        and "cover(A) = fail" in note
        and "cover(B) = hold" in note
        and "cover(C) = hold" in note
        and "cover(D) = fail" in note
        and "|Axis(M)|(A, τ) = 1" in note
        and "|Axis(M)|(B, τ) = 1" in note
        and "|Axis(M)|(C, τ) = 1" in note
        and "|Axis(M)|(D, τ) = 1" in note
        and "split(A) = fail" in note
        and "split(B) = hold" in note
        and "split(C) = hold" in note
        and "split(D) = fail" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)" in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-split-reverse-face",
        "Reverse 1-in 2-out at τ: fail" in note
        and "Face 1-in 2-out at τ: fail" in note,
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
        and "not leftover of y-probe 1-in 2-out" in normalized_note
        and "not leftover of 1-axis x-probe cover" in normalized_note
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
        '    "docs/TWO_AXIS_OPPOSITE_XPROBE_INCOMING_OUTGOING_ONE_TWO_SPLIT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "split_report" in defined_fns
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
        and ticks[PROBES["A"]] == 2
        and set(ticks) <= host,
    )
    checks.check(
        "source-letter-from-axis-split",
        "cover_report" in defined_fns
        and "split_report" in defined_fns
        and "both_hold" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and "inner_product" not in defined_fns,
    )
    _ = (unique_cover_a, same_e1_ticks, same_e1_locks, nnseed_ticks)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
