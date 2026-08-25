#!/usr/bin/env python3
"""Neighbor-read of cyclic lex-largest Orient at t+1 reverse/face on four z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process and z-probes as nm2axz.
Perp-step incoming lock. Orient as nm2oricyclz: cyclic next/prev lex-largest
outgoing determinant of the 1-in 2-out frame at tau=t+1. Neighbor-read HOLDs
at q iff Orient(q) is +/-1 and some formed 6-NN r has Orient(r)=Orient(q)
both +/-1. If Orient fails at q, neighbor-read fails, not UNDEFINED.
Unformed q => UNDEFINED. Uniqueness is not required. Reverse HOLDs iff
neighbor-read at A and at B. Face on C, D. Occupancy of sites is not used.
Named-sign lettering is not used. No larger host. Displayed, not adopted.
Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_ZPROBE_NEIGHBOR_READ_CYCLIC_LEX_LARGEST_ORIENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_ZPROBE_NEIGHBOR_READ_CYCLIC_LEX_LARGEST_ORIENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = Incoming
AxisSet = frozenset[Point] | str
OrientVal = int | str
ORIGIN: Point = (0, 0, 0)
ZERO: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NEG_E1: Point = (-1, 0, 0)
NEG_E2: Point = (0, -1, 0)
NEG_E3: Point = (0, 0, -1)
PAIR2: Point = (0, 1, 1)
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
TWO_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
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
    "Neighbor-read of the cyclic lex-largest orientation at "
    "t+1 on the four z-probes of the two-axis opposite seed, and "
    "reverse/face from that, are reported. "
    "Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def neg(step: Point) -> Point:
    return (-step[0], -step[1], -step[2])


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


def orient_display(value: OrientVal) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if value == 1:
        return "+1"
    if value == -1:
        return "−1"
    raise TypeError(f"orient is not a signed unit or fail: {value!r}")


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_SEEDS,
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
        occupied.add(axis_of_letter(lock))
    return frozenset(occupied)


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    if axes_m & axes_o:
        return "fail"
    if axes_m | axes_o != frozenset(AXES):
        return "fail"
    return "hold"


def axis_split(incoming: Incoming, outgoing: Outgoing) -> str:
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    if len(axes_m) != 1 or len(axes_o) != 2:
        return "fail"
    return "hold"


def integer_det_columns(col1: Point, col2: Point, col3: Point) -> int:
    a11, a21, a31 = col1
    a12, a22, a32 = col2
    a13, a23, a33 = col3
    return (
        a11 * (a22 * a33 - a23 * a32)
        - a12 * (a21 * a33 - a23 * a31)
        + a13 * (a21 * a32 - a22 * a31)
    )


def unique_signed_m(incoming: Incoming) -> Point | str:
    if incoming == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or len(incoming) != 1:
        return "fail"
    letter = next(iter(incoming))
    if letter not in LOCK_NAME:
        return "fail"
    return letter


def axis_index(lock: Point) -> int | str:
    axis = axis_of_letter(lock)
    if axis == E1:
        return 1
    if axis == E2:
        return 2
    if axis == E3:
        return 3
    return "fail"


def cyclic_units(signed_m: Point) -> tuple[Point, Point] | str:
    idx = axis_index(signed_m)
    if idx == "fail" or not isinstance(idx, int):
        return "fail"
    e_next = AXES[idx % 3]
    e_prev = AXES[idx - 2]
    return e_next, e_prev


def lex_largest_on_axis(outgoing: Outgoing, axis: Point) -> Point | str:
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    negative = (-axis[0], -axis[1], -axis[2])
    occupied = outgoing & {axis, negative}
    if not occupied:
        return "fail"
    if negative in occupied:
        return negative
    return axis


def lex_smallest_on_axis(outgoing: Outgoing, axis: Point) -> Point | str:
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    negative = (-axis[0], -axis[1], -axis[2])
    occupied = outgoing & {axis, negative}
    if not occupied:
        return "fail"
    if axis in occupied:
        return axis
    return negative


def cyclic_signed_outgoing(
    incoming: Incoming, outgoing: Outgoing, *, largest: bool = True
) -> tuple[Point, Point] | str:
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    units = cyclic_units(signed_m)
    if units == "fail" or not isinstance(units, tuple):
        return "fail"
    picker = lex_largest_on_axis if largest else lex_smallest_on_axis
    o_next = picker(outgoing, units[0])
    o_prev = picker(outgoing, units[1])
    if o_next == UNDEFINED or o_prev == UNDEFINED:
        return UNDEFINED
    if o_next == "fail" or o_prev == "fail":
        return "fail"
    if not isinstance(o_next, tuple) or not isinstance(o_prev, tuple):
        return "fail"
    return o_next, o_prev


def opposite_pair_unit(outgoing: Outgoing) -> Point | str:
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    for axis in AXES:
        negative = (-axis[0], -axis[1], -axis[2])
        if axis in outgoing and negative in outgoing:
            return axis
    return "fail"


def leftover_unit(signed_m: Point, pair_unit: Point) -> Point | str:
    occupied = {axis_of_letter(signed_m), axis_of_letter(pair_unit)}
    leftover = tuple(axis for axis in AXES if axis not in occupied)
    if len(leftover) != 1:
        return "fail"
    return leftover[0]


def unique_signed_outgoing_plane(outgoing: Outgoing) -> tuple[Point, Point] | str:
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    axes = axis_set(outgoing)
    if not isinstance(axes, frozenset):
        raise TypeError("unique signed outgoing plane needs an axis set")
    ordered = tuple(axis for axis in AXES if axis in axes)
    if len(ordered) != 2:
        return "fail"
    picked: list[Point] = []
    for axis in ordered:
        negative = (-axis[0], -axis[1], -axis[2])
        occupied = outgoing & {axis, negative}
        if len(occupied) != 1:
            return "fail"
        picked.append(next(iter(occupied)))
    return picked[0], picked[1]


def outgoing_plane(axes_o: AxisSet) -> tuple[Point, Point] | str:
    if axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_o, frozenset):
        raise TypeError("outgoing plane needs an axis set")
    ordered = tuple(axis for axis in AXES if axis in axes_o)
    if len(ordered) != 2:
        return "fail"
    return ordered[0], ordered[1]


def _sign_det(signed_m: Point, col2: Point, col3: Point) -> OrientVal:
    det = integer_det_columns(signed_m, col2, col3)
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Sign of det(m, o_next, o_prev) with lex-largest cyclic slots."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    plane = cyclic_signed_outgoing(incoming, outgoing, largest=True)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return _sign_det(signed_m, plane[0], plane[1])


def leftover_pair_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: leftover-axis Orient. Not this letter."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    pair = opposite_pair_unit(outgoing)
    if pair == UNDEFINED:
        return UNDEFINED
    if pair == "fail" or not isinstance(pair, tuple):
        return "fail"
    leftover = leftover_unit(signed_m, pair)
    if leftover == "fail" or not isinstance(leftover, tuple):
        return "fail"
    return _sign_det(signed_m, pair, leftover)


def unique_signed_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: unique |O_i|=1 signed plane."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    plane = unique_signed_outgoing_plane(outgoing)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return _sign_det(signed_m, plane[0], plane[1])


def cyclic_lex_smallest_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: same cyclic axes, lex-smallest (+e if both signs)."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    plane = cyclic_signed_outgoing(incoming, outgoing, largest=False)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return _sign_det(signed_m, plane[0], plane[1])


def lex_frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: lexicographic unsigned o1,o2."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    plane = outgoing_plane(axis_set(outgoing))
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return _sign_det(signed_m, plane[0], plane[1])


def orient_at(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    orient_fn=frame_orient,
) -> OrientVal:
    incoming = incoming_set(site, tau, ticks, locks, seed_map)
    outgoing = outgoing_set(site, tau, ticks, locks, seed_map)
    return orient_fn(incoming, outgoing)


def matching_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    orient_fn=frame_orient,
) -> tuple[Point, ...] | str:
    """Formed 6-NN r with Orient(r, tau)=Orient(site, tau) both +/-1."""
    own = orient_at(site, tau, ticks, locks, seed_map, orient_fn)
    if own == UNDEFINED:
        return UNDEFINED
    if own not in (1, -1):
        return ()
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other = orient_at(neighbor, tau, ticks, locks, seed_map, orient_fn)
        if other == own:
            found.append(neighbor)
    return tuple(found)


def neighbor_read(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    orient_fn=frame_orient,
) -> str:
    """HOLD iff some formed 6-NN recovers the same +/-1 Orient. Orient fail => fail."""
    own = orient_at(site, tau, ticks, locks, seed_map, orient_fn)
    if own == UNDEFINED:
        return UNDEFINED
    if own not in (1, -1):
        return "fail"
    matches = matching_neighbors(site, tau, ticks, locks, seed_map, orient_fn)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def formed_neighbor_orients(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    orient_fn=frame_orient,
) -> tuple[tuple[Point, OrientVal], ...]:
    """Orient at each eventually-formed 6-NN of site, including UNDEFINED."""
    rows: list[tuple[Point, OrientVal]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        rows.append(
            (neighbor, orient_at(neighbor, tau, ticks, locks, seed_map, orient_fn))
        )
    return tuple(rows)


def matching_outgoing_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Leftover contrast: formed 6-NN r with O(r, tau)=O(site, tau)."""
    own = outgoing_set(site, tau, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if not isinstance(own, frozenset):
        raise TypeError(f"lock set is not a lock set: {own!r}")
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other = outgoing_set(neighbor, tau, ticks, locks, seed_map)
        if other == UNDEFINED:
            continue
        if not isinstance(other, frozenset):
            raise TypeError(f"lock set is not a lock set: {other!r}")
        if other == own:
            found.append(neighbor)
    return tuple(found)


def neighbor_read_outgoing(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover contrast: neighbor-read of O. Not this letter."""
    matches = matching_outgoing_neighbors(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def matching_incoming_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Leftover contrast: formed 6-NN r with M(r, tau)=M(site, tau)."""
    own = incoming_set(site, tau, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if not isinstance(own, frozenset):
        raise TypeError(f"lock set is not a lock set: {own!r}")
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if other == UNDEFINED:
            continue
        if not isinstance(other, frozenset):
            raise TypeError(f"lock set is not a lock set: {other!r}")
        if other == own:
            found.append(neighbor)
    return tuple(found)


def neighbor_read_incoming(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover contrast: neighbor-read of M. Not this letter."""
    matches = matching_incoming_neighbors(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def pair_read(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either side is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def pair_orient(left: OrientVal, right: OrientVal) -> str:
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left in (1, -1) and left == right:
        return "hold"
    return "fail"


def reverse_report(read_a: str, read_b: str) -> str:
    """Reverse HOLDs iff neighbor-read at A and at B."""
    return pair_read(read_a, read_b)


def face_report(read_c: str, read_d: str) -> str:
    """Face HOLDs iff neighbor-read at C and at D."""
    return pair_read(read_c, read_d)


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def new_records_meeting_six_nn(
    site: Point,
    ticks: dict[Point, int],
) -> tuple[Point, ...]:
    formation = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] == formation + 1:
            found.append(neighbor)
    return tuple(found)


def probe_reads(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    orient_fn=frame_orient,
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = neighbor_read(
            site,
            site_ticks[site] + 1,
            site_ticks,
            site_locks,
            site_seeds,
            orient_fn,
        )
    return out


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

    print(
        "neighbor-read of cyclic lex-largest Orient reverse/face at t+1 "
        "on two-axis opposite z-probes"
    )
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
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E3, E2) == PAIR2
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "pair-read-identity",
        pair_read(UNDEFINED, "hold") == UNDEFINED
        and pair_read("hold", UNDEFINED) == UNDEFINED
        and pair_read("hold", "hold") == "hold"
        and pair_read("hold", "fail") == "fail"
        and pair_read("fail", "hold") == "fail"
        and pair_read("fail", "fail") == "fail",
    )
    checks.check(
        "orient-identity",
        frame_orient(UNDEFINED, frozenset({E2, E3})) == UNDEFINED
        and frame_orient(frozenset({E2}), UNDEFINED) == UNDEFINED
        and frame_orient(frozenset(), frozenset({E1, E3})) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == -1
        and frame_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == -1
        and frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == 1
        and frame_orient(frozenset({E1}), frozenset({NEG_E2, E3, NEG_E3})) == 1
        and cyclic_units(E2) == (E3, E1)
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1,
    )
    checks.check(
        "neighbor-read-identity",
        neighbor_read(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and matching_neighbors(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["B"], -1, {}, {}, {}),
            outgoing_set(PROBES["B"], -1, {}, {}, {}),
        )
        == UNDEFINED
        and neighbor_read(
            ORIGIN,
            0,
            {ORIGIN: 0},
            {ORIGIN: {E1}},
            {ORIGIN: E1},
        )
        == "fail",
    )

    ticks, locks, seed_map = form()
    twosite_ticks, twosite_locks, twosite_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)

    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    split: dict[str, str] = {}
    cover: dict[str, str] = {}
    orient: dict[str, OrientVal] = {}
    reads: dict[str, str] = {}
    reads_o: dict[str, str] = {}
    reads_m: dict[str, str] = {}
    reads_left: dict[str, str] = {}
    reads_small: dict[str, str] = {}
    matches: dict[str, tuple[Point, ...] | str] = {}
    formed_or: dict[str, tuple[tuple[Point, OrientVal], ...]] = {}
    unique_signed: dict[str, OrientVal] = {}
    leftover_or: dict[str, OrientVal] = {}
    small_or: dict[str, OrientVal] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0 = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0, ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0, ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        split[name] = axis_split(m1[name], o1[name])
        cover[name] = axis_cover(m1[name], o1[name])
        orient[name] = frame_orient(m1[name], o1[name])
        leftover_or[name] = leftover_pair_orient(m1[name], o1[name])
        unique_signed[name] = unique_signed_orient(m1[name], o1[name])
        small_or[name] = cyclic_lex_smallest_orient(m1[name], o1[name])
        reads[name] = neighbor_read(site, tau1[name], ticks, locks, seed_map)
        reads_o[name] = neighbor_read_outgoing(
            site, tau1[name], ticks, locks, seed_map
        )
        reads_m[name] = neighbor_read_incoming(
            site, tau1[name], ticks, locks, seed_map
        )
        reads_left[name] = neighbor_read(
            site, tau1[name], ticks, locks, seed_map, leftover_pair_orient
        )
        reads_small[name] = neighbor_read(
            site, tau1[name], ticks, locks, seed_map, cyclic_lex_smallest_orient
        )
        matches[name] = matching_neighbors(
            site, tau1[name], ticks, locks, seed_map
        )
        formed_or[name] = formed_neighbor_orients(
            site, tau1[name], ticks, locks, seed_map
        )
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"Orient={orient_display(orient[name])} "
            f"neighbor-read={reads[name]}"
        )

    reverse = reverse_report(reads["A"], reads["B"])
    face = face_report(reads["C"], reads["D"])
    orient_reverse = pair_orient(orient["A"], orient["B"])
    orient_face = pair_orient(orient["C"], orient["D"])
    cover_reverse = pair_read(cover["A"], cover["B"])
    cover_face = pair_read(cover["C"], cover["D"])
    split_reverse = pair_read(split["A"], split["B"])
    split_face = pair_read(split["C"], split["D"])
    print(f"neighbor-read reverse={reverse} face={face}")
    print(
        "per_element: cyclic lex-largest Orient at a probe and at formed "
        "6-NN, compared as +/-1 signs at the probe's t+1"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four neighbor-read reports, reverse/face from those bits")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["D"], 0, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-O-Orient",
        m1["A"] == frozenset({E2})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E3})
        and m1["D"] == frozenset({E1})
        and o1["A"] == frozenset({E1, NEG_E1, E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, NEG_E2})
        and o1["D"] == frozenset({NEG_E2, E3, NEG_E3})
        and orient["A"] == -1
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["D"] == 1
        and all(split[name] == "hold" for name in ("A", "B", "C", "D")),
        str({name: orient_display(orient[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-formed-6nn-orients-A",
        formed_or["A"]
        == (
            ((1, 0, 1), "fail"),
            ((-1, 0, 1), "fail"),
            ((0, 1, 1), 1),
            ((0, -1, 1), UNDEFINED),
            ((0, 0, 2), "fail"),
            ((0, 0, 0), 1),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-orients-B",
        formed_or["B"]
        == (
            ((2, 1, 1), UNDEFINED),
            ((0, 1, 1), 1),
            ((1, 2, 1), "fail"),
            ((1, 0, 1), 1),
            ((1, 1, 2), "fail"),
            ((1, 1, 0), "fail"),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-orients-C",
        formed_or["C"]
        == (
            ((1, 0, 2), "fail"),
            ((-1, 0, 2), "fail"),
            ((0, 1, 2), -1),
            ((0, -1, 2), "fail"),
            ((0, 0, 1), -1),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-orients-D",
        formed_or["D"]
        == (
            ((2, 0, 1), UNDEFINED),
            ((0, 0, 1), -1),
            ((1, 1, 1), -1),
            ((1, -1, 1), "fail"),
            ((1, 0, 2), "fail"),
            ((1, 0, 0), "fail"),
        ),
    )
    checks.check(
        "theorem1-neighbor-read-bits",
        reads["A"] == "fail"
        and reads["B"] == "fail"
        and reads["C"] == "fail"
        and reads["D"] == "fail"
        and matches["A"] == ()
        and matches["B"] == ()
        and matches["C"] == ()
        and matches["D"] == (),
        str({name: (reads[name], matches[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        o1["A"] == frozenset({E1, NEG_E1, E3})
        and unique_letter(o1["A"]) == UNDEFINED
        and orient["A"] == -1
        and reads["A"] == "fail",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {NEG_E2}
        and orient_at(PAIR2, 1, ticks, locks, seed_map) == 1
        and orient["A"] == -1,
    )
    checks.check(
        "theorem1-M-frozen-O-empty-at-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(frame_orient(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D"))
        and neighbor_read(PROBES["A"], ticks[PROBES["A"]], ticks, locks, seed_map)
        == "fail",
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((1, 0, 1), (-1, 0, 1), (0, 0, 2))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new_meet["D"] == ((1, -1, 1), (1, 0, 2), (1, 0, 0)),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse == "fail"
        and reads["A"] == "fail"
        and reads["B"] == "fail"
        and reverse != UNDEFINED
        and reverse != "hold"
        and orient_reverse == "hold"
        and cover_reverse == "hold"
        and split_reverse == "hold",
    )
    checks.check(
        "theorem3-face-fail",
        face == "fail"
        and reads["C"] == "fail"
        and reads["D"] == "fail"
        and face != UNDEFINED
        and face != "hold"
        and orient_face == "hold"
        and cover_face == "hold"
        and split_face == "hold",
    )
    checks.check(
        "orient-fail-is-neighbor-read-fail-not-undefined",
        frame_orient(frozenset({E2}), frozenset()) == "fail"
        and neighbor_read(PROBES["A"], ticks[PROBES["A"]], ticks, locks, seed_map)
        == "fail"
        and unique_signed["A"] == "fail"
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and unique_signed["D"] == "fail"
        and neighbor_read(
            PROBES["A"], tau1["A"], ticks, locks, seed_map, unique_signed_orient
        )
        == "fail",
    )
    checks.check(
        "mutation-neighbor-read-of-O-differs",
        reads_o["A"] == "hold"
        and reads_o["B"] == "fail"
        and reads_o["C"] == "fail"
        and reads_o["D"] == "fail"
        and reads["A"] == "fail"
        and reads["B"] == "fail"
        and reverse_report(reads_o["A"], reads_o["B"]) == "fail"
        and face_report(reads_o["C"], reads_o["D"]) == "fail"
        and reads_o["A"] != reads["A"],
    )
    checks.check(
        "mutation-neighbor-read-of-M-differs",
        reads_m["A"] == "fail"
        and reads_m["B"] == "hold"
        and reads_m["C"] == "hold"
        and reads_m["D"] == "hold"
        and face_report(reads_m["C"], reads_m["D"]) == "hold"
        and face == "fail",
    )
    checks.check(
        "mutation-leftover-axis-neighbor-read-differs",
        leftover_or["A"] == -1
        and leftover_or["B"] == -1
        and leftover_or["C"] == 1
        and leftover_or["D"] == -1
        and reads_left["A"] == "fail"
        and reads_left["B"] == "hold"
        and reads_left["C"] == "hold"
        and reads_left["D"] == "hold"
        and reverse_report(reads_left["A"], reads_left["B"]) == "fail"
        and face_report(reads_left["C"], reads_left["D"]) == "hold"
        and face_report(reads_left["C"], reads_left["D"]) != face,
    )
    checks.check(
        "mutation-cyclic-lex-smallest-neighbor-read-differs",
        small_or["A"] == 1
        and small_or["B"] == 1
        and small_or["C"] == -1
        and small_or["D"] == -1
        and reads_small["A"] == "hold"
        and reads_small["B"] == "fail"
        and reads_small["C"] == "fail"
        and reads_small["D"] == "fail"
        and reads_small["A"] != reads["A"],
    )
    y_reads = probe_reads(Y_PROBES, ticks, locks, seed_map)
    x_reads = probe_reads(X_PROBES, ticks, locks, seed_map)
    perp_reads = probe_reads(PROBES, perp_ticks, perp_locks, perp_seeds)
    zsym_reads = probe_reads(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    twosite_reads = probe_reads(
        PROBES, twosite_ticks, twosite_locks, twosite_seeds
    )
    y_reverse = reverse_report(y_reads["A"], y_reads["B"])
    y_face = face_report(y_reads["C"], y_reads["D"])
    x_reverse = reverse_report(x_reads["A"], x_reads["B"])
    x_face = face_report(x_reads["C"], x_reads["D"])
    twosite_reverse = reverse_report(twosite_reads["A"], twosite_reads["B"])
    twosite_face = face_report(twosite_reads["C"], twosite_reads["D"])
    checks.check(
        "not-x-probes-or-y-probes-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and y_reads["A"] == "hold"
        and y_reads["B"] == "fail"
        and y_reads["C"] == "hold"
        and y_reads["D"] == "fail"
        and y_reverse == "fail"
        and y_face == "fail"
        and x_reads["A"] == "fail"
        and x_reverse == "fail"
        and x_face == "fail"
        and perp_reads["A"] == "hold"
        and reads["A"] == "fail"
        and y_reads["A"] != reads["A"]
        and perp_reads["A"] != reads["A"],
    )
    checks.check(
        "not-nsopp-leftover-second-pair-is-seed",
        TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in twosite_ticks.values()) == 2
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and twosite_ticks[E3] == 1
        and twosite_locks[E3] == {E3}
        and twosite_reads["A"] == "hold"
        and twosite_reverse == "hold"
        and twosite_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and twosite_reverse != reverse
        and zsym_reads["A"] == "fail",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-Orient-and-neighbor-read",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=1" in note
        and "M(A, τ) = {+e_2}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_3}" in note
        and "M(D, τ) = {+e_1}" in note
        and "O(A, τ) = {+e_1, −e_1, +e_3}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ) = {−e_2, +e_3, −e_3}" in note
        and "Orient(A) = −1" in note
        and "Orient(B) = −1" in note
        and "Orient(C) = +1" in note
        and "Orient(D) = +1" in note
        and "neighbor-read(A) = fail" in note
        and "neighbor-read(B) = fail" in note
        and "neighbor-read(C) = fail" in note
        and "neighbor-read(D) = fail" in note,
    )
    checks.check(
        "note-reports-formed-neighbors",
        "formed 6-NN of A at τ: (1, 0, 1)=fail, (-1, 0, 1)=fail, (0, 1, 1)=+1, (0, -1, 1)=UNDEFINED, (0, 0, 2)=fail, (0, 0, 0)=+1"
        in note
        and "formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)=+1, (1, 2, 1)=fail, (1, 0, 1)=+1, (1, 1, 2)=fail, (1, 1, 0)=fail"
        in note
        and "formed 6-NN of C at τ: (1, 0, 2)=fail, (-1, 0, 2)=fail, (0, 1, 2)=−1, (0, -1, 2)=fail, (0, 0, 1)=−1"
        in note
        and "formed 6-NN of D at τ: (2, 0, 1)=UNDEFINED, (0, 0, 1)=−1, (1, 1, 1)=−1, (1, -1, 1)=fail, (1, 0, 2)=fail, (1, 0, 0)=fail"
        in note
        and "matching 6-NN of A: none" in note
        and "matching 6-NN of B: none" in note
        and "matching 6-NN of C: none" in note
        and "matching 6-NN of D: none" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse neighbor-read at τ: fail" in note
        and "Face neighbor-read at τ: fail" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-split-or-O-leftover",
        "not leftover of nm2axz axis-cover" in normalized_note
        and "not leftover of nm2ax12z 1-in 2-out" in normalized_note
        and "not leftover of nm2oricyclz" in normalized_note
        and "not leftover of nm2oreadz neighbor-read of O" in normalized_note
        and "not leftover of nm2readz neighbor-read of M" in normalized_note
        and "not leftover of nm2orichz leftover-axis" in normalized_note
        and "not leftover of cyclic lex-smallest" in normalized_note,
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
        '    "docs/TWO_AXIS_OPPOSITE_ZPROBE_NEIGHBOR_READ_CYCLIC_LEX_LARGEST_ORIENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "frame_orient" in defined_fns
        and "neighbor_read" in defined_fns
        and "matching_neighbors" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "formed_neighbor_orients" in defined_fns
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
    checks.check(
        "neighbor-read-not-cover-or-split-or-orient-reverse",
        reverse == "fail"
        and face == "fail"
        and orient_reverse == "hold"
        and orient_face == "hold"
        and cover_reverse == "hold"
        and split_reverse == "hold"
        and reads["A"] == "fail"
        and reads["B"] == "fail"
        and reads["C"] == "fail"
        and reads["D"] == "fail",
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
