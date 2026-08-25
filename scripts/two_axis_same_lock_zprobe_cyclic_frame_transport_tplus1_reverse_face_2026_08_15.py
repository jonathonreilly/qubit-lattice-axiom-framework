#!/usr/bin/env python3
"""Cyclic-frame transport of (m, o_next, o_prev) at t+1.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint same-lock pairs: origin locks +e_1, (0,1,0) locks +e_1,
(0,0,1) locks +e_2, (0,1,1) locks +e_2. Same process and z-probes as nm2slz.
M, O, split as nm2ax12z. Orient as nm2oricyccz (lex-smallest cyclic).
Perp-step incoming lock. Unformed => UNDEFINED. Split HOLDs iff cover HOLDs
and |Axis(M)|=1. Split HOLD required. When split HOLDs, F(q)=(m,o_next,
o_prev) with lex-smallest cyclic slots under +e < -e. Orient is the sign of
the integer determinant of those columns. If split fails, Orient fails, not
UNDEFINED. Transport HOLDs at q iff split HOLDs at q, Orient(q) is +/-1,
and some formed 6-NN r has split HOLD, Orient(r) +/-1, and the 3x3 integer
matrix sending the columns of F(q) to the columns of F(r) is a signed
permutation with determinant Orient(q)*Orient(r). If split or Orient fails
at q, transport fails not UNDEFINED. Reverse HOLDs iff transport at A and
B. Face on C,D. Uniqueness of O is not required. Occupancy of sites is not
used. No larger host. Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
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
FOUR_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    (PAIR2, E2),
)
TWO_AXIS_OPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
ONE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
TWO_SITE_OPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
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
    "Cyclic-frame transport of (m,o_next,o_prev) at t+1 on the four "
    "z-probes of the two-axis same-lock seed, and reverse/face from that, "
    "are reported. Displayed, not adopted."
)
FrameCols = tuple[Point, Point, Point] | str
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


def axis_card(value: AxisSet) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"axis set is not an axis set: {value!r}")
    return str(len(value))


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


def vec_display(value: Point | str | int) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if not isinstance(value, tuple):
        raise TypeError(f"vector is not a lock or fail: {value!r}")
    if value not in LOCK_NAME:
        raise TypeError(f"vector is not a six-neighbor step: {value!r}")
    return LOCK_NAME[value]


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
    seeds: tuple[tuple[Point, Point], ...] = FOUR_SITE_SEEDS,
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
    """Leftover-empty contrast: {e_1,e_2,e_3} minus (Axis(M) union Axis(O))."""
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
    """Leftover-empty fail contrast. Empty leftover => fail, not UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("leftover sides must be axis sets or UNDEFINED")
    if not left or not right:
        return "fail"
    if left == right:
        return "hold"
    return "fail"


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff axes disjoint and union is {e_1,e_2,e_3}. UNDEFINED if unformed."""
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


def axis_split(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff cover HOLD and |Axis(M)|=1 (hence |Axis(O)|=2)."""
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    if len(axes_m) != 1:
        return "fail"
    if len(axes_o) != 2:
        return "fail"
    return "hold"


def two_in_one_out(incoming: Incoming, outgoing: Outgoing) -> str:
    """Cover HOLD with |Axis(M)|=2. Not UNDEFINED."""
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    if len(axes_m) == 2 and len(axes_o) == 1:
        return "hold"
    return "fail"


def integer_det_columns(col1: Point, col2: Point, col3: Point) -> int:
    """Integer determinant of the 3x3 matrix with those columns."""
    a11, a21, a31 = col1
    a12, a22, a32 = col2
    a13, a23, a33 = col3
    return (
        a11 * (a22 * a33 - a23 * a32)
        - a12 * (a21 * a33 - a23 * a31)
        + a13 * (a21 * a32 - a22 * a31)
    )


def outgoing_plane(axes_o: AxisSet) -> tuple[Point, Point] | str:
    """Two Axis(O) unit vectors in axis order e1<e2<e3. Mutation: unsigned."""
    if axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_o, frozenset):
        raise TypeError("outgoing plane needs an axis set")
    ordered = tuple(axis for axis in AXES if axis in axes_o)
    if len(ordered) != 2:
        return "fail"
    return ordered[0], ordered[1]


def unique_signed_m(incoming: Incoming) -> Point | str:
    """Unique signed incoming letter. Else fail, not UNDEFINED."""
    if incoming == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or len(incoming) != 1:
        return "fail"
    letter = next(iter(incoming))
    if letter not in LOCK_NAME:
        return "fail"
    return letter


def axis_index_of(signed_m: Point | str) -> int | str:
    """Axis index i in {1,2,3} of unique signed m. Else fail, not UNDEFINED."""
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    axis = axis_of_letter(signed_m)
    if axis not in AXES:
        return "fail"
    return AXES.index(axis) + 1


def cyclic_units(index: int | str) -> tuple[Point, Point] | str:
    """(e_next, e_prev) with wrap 3+1->1 and 1-1->3."""
    if index == UNDEFINED:
        return UNDEFINED
    if not isinstance(index, int) or index not in (1, 2, 3):
        return "fail"
    e_next = AXES[index % 3]
    e_prev = AXES[(index - 2) % 3]
    return e_next, e_prev


def lex_smallest_on_axis(outgoing: Outgoing, axis: Point) -> Point | str:
    """Lex-smallest signed letter in O on axis under +e < -e. Empty => fail."""
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


def lex_largest_on_axis(outgoing: Outgoing, axis: Point) -> Point | str:
    """Lex-largest signed letter in O on axis under +e < -e. Mutation."""
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


def cyclic_outgoing_pair(
    incoming: Incoming,
    outgoing: Outgoing,
    *,
    largest: bool = False,
) -> tuple[Point, Point] | str:
    """(o_next, o_prev) lex-smallest (or lex-largest) on cyclic axes of m."""
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    units = cyclic_units(axis_index_of(signed_m))
    if units == UNDEFINED:
        return UNDEFINED
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


def unique_signed_outgoing_plane(outgoing: Outgoing) -> tuple[Point, Point] | str:
    """Unique signed outgoing letter per Axis(O). Fail if |O_i| != 1."""
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    axes = axis_set(outgoing)
    if axes == UNDEFINED:
        return UNDEFINED
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


def lex_signed_outgoing_plane(outgoing: Outgoing) -> tuple[Point, Point] | str:
    """Lex-smallest signed letter per Axis(O) under +e_i < -e_i. Mutation."""
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    axes = axis_set(outgoing)
    if axes == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes, frozenset):
        raise TypeError("lex signed outgoing plane needs an axis set")
    ordered = tuple(axis for axis in AXES if axis in axes)
    if len(ordered) != 2:
        return "fail"
    picked: list[Point] = []
    for axis in ordered:
        negative = (-axis[0], -axis[1], -axis[2])
        occupied = outgoing & {axis, negative}
        if not occupied:
            return "fail"
        if axis in occupied:
            picked.append(axis)
        else:
            picked.append(negative)
    return picked[0], picked[1]


def opposite_pair_unit(outgoing: Outgoing) -> Point | str:
    """Positive unit of the smallest-index axis with both e and -e in O."""
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
    """Unique Axis not in {axis(m), axis(e)}, oriented as the unit +l."""
    occupied = {axis_of_letter(signed_m), axis_of_letter(pair_unit)}
    leftover = tuple(axis for axis in AXES if axis not in occupied)
    if len(leftover) != 1:
        return "fail"
    return leftover[0]


def leftover_signed(outgoing: Outgoing, leftover_axis: Point) -> Point | str:
    """Unique signed O vector on leftover axis. Fail if |O_l| != 1."""
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    negative = (-leftover_axis[0], -leftover_axis[1], -leftover_axis[2])
    occupied = outgoing & {leftover_axis, negative}
    if len(occupied) != 1:
        return "fail"
    return next(iter(occupied))


def has_opposite_pair(outgoing: Outgoing) -> str:
    """HOLD iff O contains some e and -e. Fail if none. UNDEFINED if unformed."""
    pair = opposite_pair_unit(outgoing)
    if pair == UNDEFINED:
        return UNDEFINED
    if pair == "fail":
        return "fail"
    return "hold"


def lex_frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Lexicographic unsigned o1,o2 orientation. Mutation: not this letter."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    plane = outgoing_plane(axis_set(outgoing))
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail":
        return "fail"
    if not isinstance(plane, tuple):
        return "fail"
    o1, o2 = plane
    det = integer_det_columns(signed_m, o1, o2)
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def leftover_pair_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: sign of det(m, e, o_l). Not this letter."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    pair = opposite_pair_unit(outgoing)
    if pair == UNDEFINED:
        return UNDEFINED
    if pair == "fail":
        return "fail"
    if not isinstance(pair, tuple):
        return "fail"
    leftover_ax = leftover_unit(signed_m, pair)
    if leftover_ax == "fail" or not isinstance(leftover_ax, tuple):
        return "fail"
    leftover = leftover_signed(outgoing, leftover_ax)
    if leftover == UNDEFINED:
        return UNDEFINED
    if leftover == "fail" or not isinstance(leftover, tuple):
        return "fail"
    det = integer_det_columns(signed_m, pair, leftover)
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def unique_signed_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: unique |O_i|=1 signed plane. Fail if an opposite pair occupies O_i."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    plane = unique_signed_outgoing_plane(outgoing)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail":
        return "fail"
    if not isinstance(plane, tuple):
        return "fail"
    det = integer_det_columns(signed_m, plane[0], plane[1])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def lex_one_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: nm2orionez lex-smallest signed O_i in axis order. Not this letter."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    plane = lex_signed_outgoing_plane(outgoing)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail":
        return "fail"
    if not isinstance(plane, tuple):
        return "fail"
    det = integer_det_columns(signed_m, plane[0], plane[1])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def lex_largest_cyclic_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: lex-largest o_next, o_prev on the same cyclic axes."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    pair = cyclic_outgoing_pair(incoming, outgoing, largest=True)
    if pair == UNDEFINED:
        return UNDEFINED
    if pair == "fail":
        return "fail"
    if not isinstance(pair, tuple):
        return "fail"
    det = integer_det_columns(signed_m, pair[0], pair[1])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Sign of det(m, o_next, o_prev) with lex-smallest cyclic slots."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    pair = cyclic_outgoing_pair(incoming, outgoing)
    if pair == UNDEFINED:
        return UNDEFINED
    if pair == "fail":
        return "fail"
    if not isinstance(pair, tuple):
        return "fail"
    det = integer_det_columns(signed_m, pair[0], pair[1])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def pair_bit(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either side is UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def pair_orient(left: OrientVal, right: OrientVal) -> str:
    """HOLD iff both signs are equal and each is +/-1."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left in (1, -1) and left == right:
        return "hold"
    return "fail"


def reverse_report(left: str, right: str) -> str:
    """Reverse HOLDs iff transport at A and at B both HOLD."""
    return pair_bit(left, right)


def face_report(left: str, right: str) -> str:
    """Face HOLDs iff transport at C and at D both HOLD."""
    return pair_bit(left, right)


def minor_det(cols: tuple[Point, Point, Point], skip_row: int, skip_col: int) -> int:
    """2x2 minor determinant of a 3x3 column-matrix."""
    rows = tuple(index for index in range(3) if index != skip_row)
    keep = tuple(index for index in range(3) if index != skip_col)
    return (
        cols[keep[0]][rows[0]] * cols[keep[1]][rows[1]]
        - cols[keep[1]][rows[0]] * cols[keep[0]][rows[1]]
    )


def integer_inverse_columns(cols: tuple[Point, Point, Point]) -> FrameCols:
    """Integer inverse of a det +/-1 column-matrix, by adjugate."""
    det = integer_det_columns(*cols)
    if det not in (1, -1):
        return "fail"
    adj: list[Point] = []
    for col in range(3):
        adj.append(
            tuple((-1) ** (row + col) * minor_det(cols, col, row) for row in range(3))
        )
    if det == 1:
        return adj[0], adj[1], adj[2]
    return (
        (-adj[0][0], -adj[0][1], -adj[0][2]),
        (-adj[1][0], -adj[1][1], -adj[1][2]),
        (-adj[2][0], -adj[2][1], -adj[2][2]),
    )


def mat_times_vec(cols: tuple[Point, Point, Point], vec: Point) -> Point:
    return (
        cols[0][0] * vec[0] + cols[1][0] * vec[1] + cols[2][0] * vec[2],
        cols[0][1] * vec[0] + cols[1][1] * vec[1] + cols[2][1] * vec[2],
        cols[0][2] * vec[0] + cols[1][2] * vec[1] + cols[2][2] * vec[2],
    )


def mat_times_mat(
    left: tuple[Point, Point, Point], right: tuple[Point, Point, Point]
) -> tuple[Point, Point, Point]:
    return (
        mat_times_vec(left, right[0]),
        mat_times_vec(left, right[1]),
        mat_times_vec(left, right[2]),
    )


def is_signed_permutation(cols: tuple[Point, Point, Point]) -> bool:
    """Each row and each column has a single nonzero entry in {+1,-1}."""
    axes: list[Point] = []
    for col in cols:
        if not all(entry in (-1, 0, 1) for entry in col):
            return False
        if sum(abs(entry) for entry in col) != 1:
            return False
        axes.append((abs(col[0]), abs(col[1]), abs(col[2])))
    if len(set(axes)) != 3:
        return False
    for row in range(3):
        if sum(abs(cols[col][row]) for col in range(3)) != 1:
            return False
    return True


def sending_matrix(
    source: tuple[Point, Point, Point], target: tuple[Point, Point, Point]
) -> FrameCols:
    """Integer T with T source = target: T sends columns of source to target."""
    inverse = integer_inverse_columns(source)
    if inverse == "fail" or not isinstance(inverse, tuple):
        return "fail"
    return mat_times_mat(target, inverse)


def frame_columns(incoming: Incoming, outgoing: Outgoing) -> FrameCols:
    """F=(m,o_next,o_prev) when split HOLDs. Else fail, not UNDEFINED if formed."""
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
    pair = cyclic_outgoing_pair(incoming, outgoing)
    if pair == UNDEFINED:
        return UNDEFINED
    if pair == "fail" or not isinstance(pair, tuple):
        return "fail"
    return signed_m, pair[0], pair[1]


def formed_six_neighbors(site: Point, ticks: dict[Point, int]) -> tuple[Point, ...]:
    """Formed six-neighbors of site in B_3(0). Not a scored star letter."""
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks:
            found.append(neighbor)
    return tuple(found)


def transport_report(
    incoming: Incoming,
    outgoing: Outgoing,
    neighbor_frames: tuple[tuple[Incoming, Outgoing], ...],
) -> str:
    """HOLD iff F(q) maps to some formed 6-NN F(r) by a signed permutation."""
    split = axis_split(incoming, outgoing)
    orient = frame_orient(incoming, outgoing)
    source = frame_columns(incoming, outgoing)
    if split == UNDEFINED or orient == UNDEFINED or source == UNDEFINED:
        return UNDEFINED
    if split != "hold" or orient not in (1, -1) or not isinstance(source, tuple):
        return "fail"
    for neighbor_in, neighbor_out in neighbor_frames:
        neighbor_split = axis_split(neighbor_in, neighbor_out)
        neighbor_orient = frame_orient(neighbor_in, neighbor_out)
        target = frame_columns(neighbor_in, neighbor_out)
        if neighbor_split != "hold" or neighbor_orient not in (1, -1):
            continue
        if not isinstance(target, tuple):
            continue
        sending = sending_matrix(source, target)
        if not isinstance(sending, tuple):
            continue
        if not is_signed_permutation(sending):
            continue
        if integer_det_columns(*sending) != orient * neighbor_orient:
            continue
        return "hold"
    return "fail"


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


def unsigned_incoming_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: replace signed m by the unsigned Axis(M) unit. Not this letter."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    if not isinstance(axes_m, frozenset) or len(axes_m) != 1:
        return "fail"
    unsigned_m = next(iter(axes_m))
    pair = cyclic_outgoing_pair(incoming, outgoing)
    if not isinstance(pair, tuple):
        return "fail"
    det = integer_det_columns(unsigned_m, pair[0], pair[1])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


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


def probe_sides(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> tuple[dict[str, Incoming], dict[str, Outgoing]]:
    incoming: dict[str, Incoming] = {}
    outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            incoming[name] = UNDEFINED
            outgoing[name] = UNDEFINED
            continue
        tau = site_ticks[site] + 1
        incoming[name] = incoming_set(site, tau, site_ticks, site_locks, site_seeds)
        outgoing[name] = outgoing_set(site, tau, site_ticks, site_locks, site_seeds)
    return incoming, outgoing


def site_sides(
    site: Point,
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> tuple[Incoming, Outgoing]:
    if site not in site_ticks:
        return UNDEFINED, UNDEFINED
    tau = site_ticks[site] + 1
    return (
        incoming_set(site, tau, site_ticks, site_locks, site_seeds),
        outgoing_set(site, tau, site_ticks, site_locks, site_seeds),
    )


def transport_at_site(
    site: Point,
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> str:
    incoming, outgoing = site_sides(site, site_ticks, site_locks, site_seeds)
    neighbor_frames: list[tuple[Incoming, Outgoing]] = []
    if site in site_ticks:
        for neighbor in formed_six_neighbors(site, site_ticks):
            neighbor_frames.append(
                site_sides(neighbor, site_ticks, site_locks, site_seeds)
            )
    return transport_report(incoming, outgoing, tuple(neighbor_frames))


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("cyclic-frame transport of (m,o_next,o_prev) reverse/face at t+1 on two-axis same-lock z-probes")
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
        and add(NEG_E2, E2) == ZERO
        and add(E3, E2) == PAIR2
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "det-identity",
        integer_det_columns(E2, E3, E1) == 1
        and integer_det_columns(E1, E2, NEG_E3) == -1
        and integer_det_columns(E3, NEG_E1, NEG_E2) == 1
        and integer_det_columns(E1, NEG_E2, NEG_E3) == 1
        and integer_det_columns(E2, E3, NEG_E1) == -1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(E1, E1, E2) == 0,
    )
    checks.check(
        "cyclic-wrap-and-lex-smallest",
        cyclic_units(1) == (E2, E3)
        and cyclic_units(2) == (E3, E1)
        and cyclic_units(3) == (E1, E2)
        and axis_index_of(E1) == 1
        and axis_index_of(NEG_E2) == 2
        and axis_index_of(E3) == 3
        and lex_smallest_on_axis(frozenset({E1, NEG_E1}), E1) == E1
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1
        and lex_smallest_on_axis(frozenset({E3}), E3) == E3
        and lex_smallest_on_axis(frozenset({NEG_E2}), E2) == NEG_E2
        and lex_smallest_on_axis(frozenset(), E1) == "fail"
        and cyclic_outgoing_pair(frozenset({E2}), frozenset({E1, E3})) == (E3, E1)
        and cyclic_outgoing_pair(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == (E3, E1)
        and cyclic_outgoing_pair(
            frozenset({E2}), frozenset({E1, NEG_E1, E3}), largest=True
        )
        == (E3, NEG_E1)
        and cyclic_outgoing_pair(frozenset({E1}), frozenset({E2, E3, NEG_E3}))
        == (E2, E3)
        and cyclic_outgoing_pair(frozenset({E2}), frozenset({E1})) == "fail",
    )
    identity_send = sending_matrix((E1, E2, E3), (E1, NEG_E2, E3))
    checks.check(
        "signed-permutation-sending-identity",
        integer_inverse_columns((E1, E2, E3)) == (E1, E2, E3)
        and sending_matrix((E1, E2, E3), (E1, E2, E3)) == (E1, E2, E3)
        and identity_send == (E1, NEG_E2, E3)
        and is_signed_permutation(identity_send)
        and integer_det_columns(*identity_send) == -1
        and is_signed_permutation((E1, E2, E3))
        and is_signed_permutation((E3, E1, NEG_E2))
        and not is_signed_permutation((E1, E1, E2))
        and not is_signed_permutation((E1, E2, (2, 0, 0)))
        and frame_columns(frozenset({E2}), frozenset({E1, E3})) == (E2, E3, E1)
        and frame_columns(frozenset({E2, E3}), frozenset({E1})) == "fail"
        and transport_report(
            frozenset({E1}),
            frozenset({E2, E3}),
            ((frozenset({E1}), frozenset({NEG_E2, E3})),),
        )
        == "hold"
        and transport_report(
            frozenset({E2, E3, NEG_E3}),
            frozenset({E1, NEG_E1}),
            ((frozenset({E1}), frozenset({E2, E3})),),
        )
        == "fail"
        and transport_report(UNDEFINED, UNDEFINED, ()) == UNDEFINED,
    )
    checks.check(
        "orient-identity",
        frame_orient(UNDEFINED, frozenset({E2, E3})) == UNDEFINED
        and frame_orient(frozenset({E2}), UNDEFINED) == UNDEFINED
        and frame_orient(frozenset(), frozenset({E1, E3})) == "fail"
        and frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and frame_orient(frozenset({E2}), frozenset({NEG_E1, E3})) == -1
        and frame_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == 1
        and frame_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == 1
        and frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == -1
        and frame_orient(frozenset({E1}), frozenset({NEG_E2, E3, NEG_E3})) == -1
        and frame_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == -1
        and frame_orient(frozenset({E1, NEG_E1}), frozenset({E2, E3})) == "fail"
        and frame_orient(frozenset({E2}), frozenset()) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1})) == "fail"
        and lex_one_orient(frozenset({E2}), frozenset({E1, E3})) == -1
        and lex_frame_orient(frozenset({E2}), frozenset({E1, E3})) == -1
        and lex_largest_cyclic_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == -1
        and leftover_pair_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == -1
        and leftover_axis(frozenset({E2}), frozenset({E1, E3})) == frozenset()
        and leftover_match(frozenset(), frozenset()) == "fail",
    )
    checks.check(
        "pair-orient-identity",
        pair_orient(UNDEFINED, 1) == UNDEFINED
        and pair_orient(1, UNDEFINED) == UNDEFINED
        and pair_orient(1, 1) == "hold"
        and pair_orient(-1, -1) == "hold"
        and pair_orient(-1, 1) == "fail"
        and pair_orient(1, "fail") == "fail"
        and pair_orient("fail", "fail") == "fail",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    xsame_ticks, xsame_locks, xsame_seeds = form(X_AXIS_SAME_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(TWO_SITE_OPP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    tau0: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    axis_m: dict[str, AxisSet] = {}
    axis_o: dict[str, AxisSet] = {}
    cover: dict[str, str] = {}
    split: dict[str, str] = {}
    two_one: dict[str, str] = {}
    signed_m: dict[str, Point | str] = {}
    index: dict[str, int | str] = {}
    cyclic_pair: dict[str, tuple[Point, Point] | str] = {}
    plane: dict[str, tuple[Point, Point] | str] = {}
    pair: dict[str, Point | str] = {}
    leftover: dict[str, Point | str] = {}
    det: dict[str, int | str] = {}
    lex: dict[str, OrientVal] = {}
    leftover_pair: dict[str, OrientVal] = {}
    unique_signed: dict[str, OrientVal] = {}
    lex_one: dict[str, OrientVal] = {}
    largest: dict[str, OrientVal] = {}
    pair_present: dict[str, str] = {}
    unique_plane: dict[str, tuple[Point, Point] | str] = {}
    lex_plane: dict[str, tuple[Point, Point] | str] = {}
    orient: dict[str, OrientVal] = {}
    frame: dict[str, FrameCols] = {}
    transport: dict[str, str] = {}
    witnesses: dict[str, tuple[Point, ...]] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1 = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1, ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1, ticks, locks, seed_map)
        axis_m[name] = axis_set(m1[name])
        axis_o[name] = axis_set(o1[name])
        cover[name] = axis_cover(m1[name], o1[name])
        split[name] = axis_split(m1[name], o1[name])
        two_one[name] = two_in_one_out(m1[name], o1[name])
        signed_m[name] = unique_signed_m(m1[name])
        index[name] = axis_index_of(signed_m[name])
        cyclic_pair[name] = cyclic_outgoing_pair(m1[name], o1[name])
        plane[name] = outgoing_plane(axis_o[name])
        unique_plane[name] = unique_signed_outgoing_plane(o1[name])
        lex_plane[name] = lex_signed_outgoing_plane(o1[name])
        pair[name] = opposite_pair_unit(o1[name])
        if isinstance(signed_m[name], tuple) and isinstance(pair[name], tuple):
            leftover_ax = leftover_unit(signed_m[name], pair[name])
            if isinstance(leftover_ax, tuple):
                leftover[name] = leftover_signed(o1[name], leftover_ax)
            else:
                leftover[name] = "fail"
        else:
            leftover[name] = "fail"
        if (
            split[name] == "hold"
            and isinstance(signed_m[name], tuple)
            and isinstance(cyclic_pair[name], tuple)
        ):
            det[name] = integer_det_columns(
                signed_m[name], cyclic_pair[name][0], cyclic_pair[name][1]
            )
        else:
            det[name] = "fail"
        pair_present[name] = has_opposite_pair(o1[name])
        lex[name] = lex_frame_orient(m1[name], o1[name])
        leftover_pair[name] = leftover_pair_orient(m1[name], o1[name])
        unique_signed[name] = unique_signed_orient(m1[name], o1[name])
        lex_one[name] = lex_one_orient(m1[name], o1[name])
        largest[name] = lex_largest_cyclic_orient(m1[name], o1[name])
        orient[name] = frame_orient(m1[name], o1[name])
        frame[name] = frame_columns(m1[name], o1[name])
        transport[name] = transport_at_site(site, ticks, locks, seed_map)
        found_hits: list[Point] = []
        source_frame = frame[name]
        if isinstance(source_frame, tuple) and orient[name] in (1, -1):
            for neighbor in formed_six_neighbors(site, ticks):
                n_in, n_out = site_sides(neighbor, ticks, locks, seed_map)
                n_orient = frame_orient(n_in, n_out)
                target = frame_columns(n_in, n_out)
                if n_orient not in (1, -1) or not isinstance(target, tuple):
                    continue
                sending = sending_matrix(source_frame, target)
                if (
                    isinstance(sending, tuple)
                    and is_signed_permutation(sending)
                    and integer_det_columns(*sending) == orient[name] * n_orient
                ):
                    found_hits.append(neighbor)
        witnesses[name] = tuple(found_hits)
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        o_next_s = (
            vec_display(cyclic_pair[name][0])
            if isinstance(cyclic_pair[name], tuple)
            else vec_display(cyclic_pair[name])
        )
        o_prev_s = (
            vec_display(cyclic_pair[name][1])
            if isinstance(cyclic_pair[name], tuple)
            else vec_display(cyclic_pair[name])
        )
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"split={split[name]} "
            f"i={vec_display(index[name])} "
            f"o_next={o_next_s} "
            f"o_prev={o_prev_s} "
            f"det={det[name]} "
            f"Orient={orient_display(orient[name])} "
            f"transport={transport[name]}"
        )

    reverse = reverse_report(transport["A"], transport["B"])
    face = face_report(transport["C"], transport["D"])
    orient_reverse = pair_orient(orient["A"], orient["B"])
    orient_face = pair_orient(orient["C"], orient["D"])
    cover_reverse = pair_bit(cover["A"], cover["B"])
    cover_face = pair_bit(cover["C"], cover["D"])
    split_reverse = pair_bit(split["A"], split["B"])
    split_face = pair_bit(split["C"], split["D"])
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
    unsigned_orient = {
        name: unsigned_incoming_orient(m1[name], o1[name])
        for name in ("A", "B", "C", "D")
    }
    unique_o_orient_a = frame_orient(unique_letter(m1["A"]), unique_letter(o1["A"]))
    one_m1, one_o1 = probe_sides(PROBES, one_ticks, one_locks, one_seeds)
    one_cover = {name: axis_cover(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_split = {name: axis_split(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_orient = {
        name: frame_orient(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")
    }
    one_cover_face = pair_bit(one_cover["C"], one_cover["D"])
    one_split_face = pair_bit(one_split["C"], one_split["D"])
    one_orient_face = pair_orient(one_orient["C"], one_orient["D"])
    opp_m1, opp_o1 = probe_sides(PROBES, opp_ticks, opp_locks, opp_seeds)
    opp_orient = {
        name: frame_orient(opp_m1[name], opp_o1[name]) for name in ("A", "B", "C", "D")
    }
    opp_split = {name: axis_split(opp_m1[name], opp_o1[name]) for name in ("A", "B", "C", "D")}
    opp_reverse = pair_orient(opp_orient["A"], opp_orient["B"])
    opp_face = pair_orient(opp_orient["C"], opp_orient["D"])
    print(f"transport reverse={reverse} face={face}")
    print(f"Orient reverse={orient_reverse} face={orient_face}")
    print(f"split reverse={split_reverse} face={split_face}")
    print(f"cover reverse={cover_reverse} face={cover_face}")
    print(
        f"nm2oricyccz opposite z-probe Orient reverse={opp_reverse} face={opp_face} "
        f"A={orient_display(opp_orient['A'])}"
    )
    print(
        "per_element: cyclic frame F=(m,o_next,o_prev) and signed-permutation "
        "transport to a formed six-neighbor at a probe's t+1"
    )
    print("per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four transport reports, reverse/face from transport HOLD")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_a_parallel_blocked = ticks.get(add(E3, NEG_E2)) != 1
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_a_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[E3] == 0
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(PAIR2, 1, ticks, locks, seed_map) == frozenset({E2})
        and FOUR_SITE_SEEDS
        == ((ORIGIN, E1), (E2, E1), (E3, E2), (PAIR2, E2)),
    )
    checks.check(
        "neither-pair-is-opposite",
        seed_map[ORIGIN] == seed_map[E2] == E1
        and seed_map[E3] == seed_map[PAIR2] == E2
        and add(seed_map[ORIGIN], seed_map[E2]) != ZERO
        and add(seed_map[E3], seed_map[PAIR2]) != ZERO
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS,
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["C"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["D"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["D"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and transport_report(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
            (),
        )
        == UNDEFINED,
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
        "theorem1-M-O-split",
        m1["A"] == frozenset({E2})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E3})
        and m1["D"] == frozenset({E1})
        and o1["A"] == frozenset({E1, NEG_E1, E2, E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, NEG_E2})
        and o1["D"] == frozenset({NEG_E2, E3, NEG_E3})
        and split["A"] == "fail"
        and split["B"] == "hold"
        and split["C"] == "hold"
        and split["D"] == "hold"
        and cover["A"] == "fail"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "hold",
        str({name: (lockset_display(m1[name]), split[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Orient",
        signed_m["A"] == E2
        and signed_m["B"] == E1
        and signed_m["C"] == E3
        and signed_m["D"] == E1
        and index["A"] == 2
        and index["B"] == 1
        and index["C"] == 3
        and index["D"] == 1
        and cyclic_pair["A"] == (E3, E1)
        and cyclic_pair["B"] == (E2, E3)
        and cyclic_pair["C"] == (E1, NEG_E2)
        and cyclic_pair["D"] == (NEG_E2, E3)
        and unique_plane["A"] == "fail"
        and unique_plane["B"] == "fail"
        and unique_plane["C"] == "fail"
        and unique_plane["D"] == "fail"
        and det["A"] == "fail"
        and det["B"] == 1
        and det["C"] == -1
        and det["D"] == -1
        and orient["A"] == "fail"
        and orient["B"] == 1
        and orient["C"] == -1
        and orient["D"] == -1
        and frame["A"] == "fail"
        and frame["B"] == (E1, E2, E3)
        and frame["C"] == (E3, E1, NEG_E2)
        and frame["D"] == (E1, NEG_E2, E3)
        and plane["A"] == "fail"
        and pair["A"] == E1,
        str({name: orient_display(orient[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-mixed-O-lex-smallest-not-unique",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 4
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(m1["A"]) == frozenset({E2})
        and unique_plane["A"] == "fail"
        and unique_signed["A"] == "fail"
        and cyclic_pair["A"] == (E3, E1)
        and unique_o_orient_a == UNDEFINED
        and orient["A"] == "fail"
        and orient["A"] != UNDEFINED
        and transport["A"] == "fail"
        and transport["A"] != UNDEFINED,
    )
    checks.check(
        "theorem1-transport",
        transport["A"] == "fail"
        and transport["B"] == "hold"
        and transport["C"] == "hold"
        and transport["D"] == "hold"
        and PROBES["D"] in witnesses["B"]
        and (0, 1, 2) in witnesses["C"]
        and PROBES["B"] in witnesses["D"]
        and not witnesses["A"]
        and sending_matrix(frame["B"], frame["D"]) == (E1, NEG_E2, E3)
        and integer_det_columns(*sending_matrix(frame["B"], frame["D"]))
        == orient["B"] * orient["D"],
        str({name: transport[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and o0["A"] == frozenset({E2})
        and all(o0[name] == frozenset() for name in ("B", "C", "D"))
        and all(frame_orient(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((1, 0, 1), (-1, 0, 1), (0, 0, 2))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new_meet["D"] == ((1, -1, 1), (1, 0, 2), (1, 0, 0)),
        str(new_meet),
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and m1["A"] == frozenset({E2})
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {E2}
        and Y_PROBES["A"] != PROBES["A"]
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem2-reverse-transport-fail",
        reverse == "fail"
        and transport["A"] == "fail"
        and transport["B"] == "hold"
        and orient["A"] == "fail"
        and orient["B"] == 1
        and reverse != UNDEFINED
        and reverse != "hold"
        and split_reverse == "fail"
        and cover_reverse == "fail"
        and orient_reverse == "fail",
    )
    checks.check(
        "theorem3-face-transport-hold",
        face == "hold"
        and transport["C"] == "hold"
        and transport["D"] == "hold"
        and orient["C"] == -1
        and orient["D"] == -1
        and face != UNDEFINED
        and face != "fail"
        and split_face == "hold"
        and cover_face == "hold"
        and orient_face == "hold",
    )
    checks.check(
        "cover-and-split-do-not-score-handedness",
        split_reverse == "fail"
        and cover_reverse == "fail"
        and reverse == "fail"
        and split_face == "hold"
        and cover_face == "hold"
        and face == "hold"
        and orient["C"] == -1
        and orient["D"] == -1
        and transport["C"] == "hold"
        and transport["D"] == "hold"
        and cover["C"] == "hold"
        and split["C"] == "hold",
    )
    checks.check(
        "split-fail-is-orient-fail-not-undefined",
        frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold"
        and two_one["C"] == "fail"
        and two_one["D"] == "fail"
        and one_orient["C"] == "fail"
        and one_split["C"] == "fail"
        and one_cover["C"] == "hold"
        and one_orient_face == "fail"
        and one_split_face == "fail"
        and one_cover_face == "hold",
    )
    checks.check(
        "empty-cyclic-side-is-orient-fail-not-undefined",
        cyclic_outgoing_pair(frozenset({E2}), frozenset()) == "fail"
        and cyclic_outgoing_pair(frozenset({E2}), frozenset({E1})) == "fail"
        and frame_orient(frozenset({E2}), frozenset()) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1})) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1,
    )
    checks.check(
        "not-leftover-of-1-axis-cover-face-hold",
        one_ticks[PROBES["A"]] == 1
        and one_ticks[PROBES["C"]] == 4
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["C"]] == 1
        and one_orient["C"] == "fail"
        and one_orient_face == "fail"
        and face == "hold"
        and one_orient_face != face
        and one_m1["A"] != m1["A"],
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and leftover_reverse == reverse
        and leftover_face != face
        and all(lx[name] == frozenset() for name in ("A", "B", "C", "D"))
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and leftover_axis(frozenset({E2}), frozenset({E1, E3})) == frozenset()
        and leftover_match(frozenset(), frozenset()) == "fail",
    )
    checks.check(
        "mutation-leftover-of-M-or-O-alone-differs",
        lx_m["A"] == frozenset({E1, E3})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_o["A"] == frozenset()
        and lx_o["B"] == frozenset({E1})
        and reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and reverse == "fail"
        and face == "hold"
        and face_m_alone != face
        and lx_m["A"] != lx["A"],
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "hold"
        and o_exist_face == "fail"
        and reverse == "fail"
        and face == "hold"
        and o_exist_reverse != reverse
        and o_exist_face != face
        and pair_present["A"] == "hold"
        and pair_present["B"] == "hold"
        and pair_present["C"] == "hold"
        and pair_present["D"] == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) == "hold"
        and pair_bit(pair_present["A"], pair_present["B"]) != reverse,
    )
    checks.check(
        "mutation-unsigned-incoming-axis-agrees-here",
        unsigned_orient["A"] == "fail"
        and unsigned_orient["B"] == 1
        and unsigned_orient["C"] == -1
        and unsigned_orient["D"] == -1
        and frame_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == -1
        and unsigned_incoming_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == 1
        and frame_orient(frozenset({NEG_E2}), o1["A"]) == "fail"
        and unsigned_incoming_orient(frozenset({NEG_E2}), o1["A"]) == "fail"
        and orient["A"] == "fail",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == frozenset({E2})
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_o_orient_a == UNDEFINED
        and unique_signed["A"] == "fail"
        and unique_signed["C"] == "fail"
        and unique_signed["D"] == "fail"
        and orient["A"] == "fail"
        and orient["D"] == -1
        and transport["D"] == "hold"
        and orient["A"] != UNDEFINED,
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["A"], frozenset)
        and sum_of_set(m1["A"]) == E2
        and sum_of_set(o1["A"]) == add(E2, E3)
        and axis_o["A"] == frozenset({E1, E2, E3})
        and pair["A"] == E1
        and leftover["A"] == E3
        and cyclic_pair["A"] == (E3, E1)
        and plane["A"] == "fail",
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E2 in m1["A"]
        and E2 in o1["A"]
        and o1["A"] != m1["A"]
        and axis_m["A"] != axis_o["A"],
    )
    checks.check(
        "second-pair-is-seed-not-formed-child",
        PAIR2 in seed_map
        and seed_map[PAIR2] == E2
        and ticks[PAIR2] == 0
        and E3 in seed_map
        and seed_map[E3] == E2
        and ticks[E3] == 0
        and one_ticks[E3] == 1
        and PAIR2 not in new_meet["A"],
    )
    checks.check(
        "compare-nm2oricyccz-opposite-orient",
        opp_orient["A"] == 1
        and opp_orient["B"] == 1
        and opp_orient["C"] == -1
        and opp_orient["D"] == -1
        and opp_split["A"] == "hold"
        and opp_reverse == "hold"
        and opp_face == "hold"
        and isinstance(opp_o1["A"], frozenset)
        and E2 not in opp_o1["A"]
        and isinstance(o1["A"], frozenset)
        and E2 in o1["A"]
        and orient["A"] == "fail"
        and reverse == "fail"
        and face == "hold"
        and opp_reverse != reverse
        and orient["A"] != opp_orient["A"],
    )
    y_m1, y_o1 = probe_sides(Y_PROBES, ticks, locks, seed_map)
    y_split = {name: axis_split(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient = {name: frame_orient(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_reverse = pair_orient(y_orient["A"], y_orient["B"])
    y_face = pair_orient(y_orient["C"], y_orient["D"])
    x_m1, x_o1 = probe_sides(X_PROBES, ticks, locks, seed_map)
    x_orient = {name: frame_orient(x_m1[name], x_o1[name]) for name in ("A", "B", "C", "D")}
    x_reverse = pair_orient(x_orient["A"], x_orient["B"])
    x_face = pair_orient(x_orient["C"], x_orient["D"])
    perp_m1, perp_o1 = probe_sides(PROBES, perp_ticks, perp_locks, perp_seeds)
    xsame_m1, _xsame_o1 = probe_sides(PROBES, xsame_ticks, xsame_locks, xsame_seeds)
    nsopp_m_a = incoming_set(
        PROBES["A"],
        nsopp_ticks[PROBES["A"]] + 1,
        nsopp_ticks,
        nsopp_locks,
        nsopp_seeds,
    )
    zsym_m1, _zsym_o1 = probe_sides(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    checks.check(
        "not-x-probes-or-y-probes-or-z-symmetric-or-perp",
        FOUR_SITE_SEEDS != PERP_SEEDS
        and FOUR_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and y_m1["A"] != m1["A"]
        and y_split["A"] == "hold"
        and y_orient["A"] == -1
        and y_orient["B"] == 1
        and y_reverse == "fail"
        and lex_frame_orient(y_m1["A"], y_o1["A"]) == 1
        and leftover_pair_orient(y_m1["A"], y_o1["A"]) == "fail"
        and unique_signed_orient(y_m1["A"], y_o1["A"]) == -1
        and y_split["D"] == "fail"
        and y_orient["D"] == "fail"
        and y_face == "fail"
        and x_reverse == "fail"
        and x_face == "fail"
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and reverse == "fail"
        and face == "hold"
        and y_reverse == reverse
        and y_face != face,
    )
    checks.check(
        "not-one-axis-or-x-axis-same-or-y-symmetric-seed",
        FOUR_SITE_SEEDS != ONE_AXIS_SEEDS
        and FOUR_SITE_SEEDS != TWO_SITE_OPP_SEEDS
        and FOUR_SITE_SEEDS != X_AXIS_SAME_SEEDS
        and FOUR_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and nsopp_m_a != m1["A"]
        and xsame_m1["A"] != m1["A"]
        and one_m1["A"] != m1["A"]
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-split-Orient",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=1" in note
        and "M(A, τ) = {+e_2}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_3}" in note
        and "M(D, τ) = {+e_1}" in note
        and "O(A, τ) = {+e_1, −e_1, +e_2, +e_3}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ) = {−e_2, +e_3, −e_3}" in note
        and "split(A) = fail" in note
        and "split(B) = hold" in note
        and "split(C) = hold" in note
        and "split(D) = hold" in note
        and "i(A) = 2" in note
        and "o_next(A) = +e_3" in note
        and "o_prev(A) = +e_1" in note
        and "det(A) = fail" in note
        and "Orient(A) = fail" in note
        and "transport(A) = fail" in note
        and "i(B) = 1" in note
        and "o_next(B) = +e_2" in note
        and "o_prev(B) = +e_3" in note
        and "det(B) = 1" in note
        and "Orient(B) = +1" in note
        and "transport(B) = hold" in note
        and "i(C) = 3" in note
        and "o_next(C) = +e_1" in note
        and "o_prev(C) = −e_2" in note
        and "det(C) = -1" in note
        and "Orient(C) = −1" in note
        and "transport(C) = hold" in note
        and "i(D) = 1" in note
        and "o_next(D) = −e_2" in note
        and "o_prev(D) = +e_3" in note
        and "det(D) = -1" in note
        and "Orient(D) = −1" in note
        and "transport(D) = hold" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)"
        in note
        and "new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)" in note
        and "transport witnesses of B include (1, 0, 1)" in note
        and "transport witnesses of C include (0, 1, 2)" in note
        and "transport witnesses of D include (1, 1, 1)" in note,
    )
    checks.check(
        "note-reports-transport-reverse-face",
        "Reverse cyclic-frame transport at τ: fail" in note
        and "Face cyclic-frame transport at τ: hold" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-split",
        "Cover and split do not score handedness" in note
        and "not leftover of nm2oricyccz cyclic" in normalized_note
        and "not leftover of nm2oricyclslz lex-largest" in normalized_note
        and "not leftover of nm2orionez lex-one" in normalized_note
        and "not leftover of nm2slz axis-cover" in normalized_note
        and "not leftover of nm2axz axis-cover" in normalized_note
        and "not leftover of nm2ax12z 1-in 2-out split" in normalized_note
        and "not leftover of nm2chiralz lexicographic" in normalized_note
        and "not leftover of nm2orichz opposite-pair" in normalized_note
        and "not leftover of nm2oridetz unique signed" in normalized_note
        and "O is not M" in note
        and "second pair is a new seed, not a formed child" in normalized_note,
    )
    checks.check(
        "note-not-one-sided-or-leftover-empty",
        "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover-of-`O` alone" in normalized_note
        and "not leftover-empty fail" in normalized_note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-mixed-7188-fail-fail",
        "not leftover of mixed #7188 fail/fail" in normalized_note
        and "Reverse cyclic-frame transport at τ: fail" in note
        and "Face cyclic-frame transport at τ: hold" in note,
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
        '    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "axis_split" in defined_fns
        and "frame_orient" in defined_fns
        and "cyclic_outgoing_pair" in defined_fns
        and "lex_smallest_on_axis" in defined_fns
        and "lex_largest_on_axis" in defined_fns
        and "cyclic_units" in defined_fns
        and "axis_index_of" in defined_fns
        and "lex_one_orient" in defined_fns
        and "lex_largest_cyclic_orient" in defined_fns
        and "unique_signed_outgoing_plane" in defined_fns
        and "leftover_pair_orient" in defined_fns
        and "lex_frame_orient" in defined_fns
        and "integer_det_columns" in defined_fns
        and "sending_matrix" in defined_fns
        and "is_signed_permutation" in defined_fns
        and "frame_columns" in defined_fns
        and "transport_report" in defined_fns
        and "formed_six_neighbors" in defined_fns
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
    checks.check(
        "transport-not-unsigned-or-unique-or-lex-largest",
        reverse == "fail"
        and face == "hold"
        and split_reverse == "fail"
        and cover_reverse == "fail"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and one_orient_face == "fail"
        and lex["A"] == "fail"
        and lex["B"] == 1
        and lex["C"] == 1
        and lex["D"] == 1
        and pair_orient(lex["A"], lex["B"]) == "fail"
        and pair_orient(lex["C"], lex["D"]) == "hold"
        and lex["C"] != orient["C"]
        and lex_one["A"] == "fail"
        and lex_one["B"] == 1
        and lex_one["C"] == -1
        and lex_one["D"] == -1
        and pair_orient(lex_one["A"], lex_one["B"]) == "fail"
        and pair_orient(lex_one["C"], lex_one["D"]) == "hold"
        and lex_one["B"] == orient["B"]
        and lex_one["C"] == orient["C"]
        and lex_one["D"] == orient["D"]
        and leftover_pair["A"] == "fail"
        and leftover_pair["B"] == -1
        and leftover_pair["C"] == -1
        and leftover_pair["D"] == 1
        and pair_orient(leftover_pair["A"], leftover_pair["B"]) == "fail"
        and pair_orient(leftover_pair["C"], leftover_pair["D"]) == "fail"
        and leftover_pair["C"] == orient["C"]
        and leftover_pair["D"] != orient["D"]
        and unique_signed["A"] == "fail"
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and unique_signed["D"] == "fail"
        and pair_orient(unique_signed["A"], unique_signed["B"]) == "fail"
        and pair_orient(unique_signed["C"], unique_signed["D"]) == "fail"
        and pair_orient(unique_signed["C"], unique_signed["D"]) != face
        and largest["A"] == "fail"
        and largest["B"] == -1
        and largest["C"] == 1
        and largest["D"] == 1
        and pair_orient(largest["A"], largest["B"]) == "fail"
        and pair_orient(largest["C"], largest["D"]) == "hold"
        and largest["B"] != orient["B"]
        and largest["C"] != orient["C"]
        and orient_reverse == reverse
        and orient_face == face
        and transport["B"] == "hold"
        and orient["B"] == 1
        and transport["C"] == "hold"
        and orient["C"] == -1
        and o_exist_reverse == "hold"
        and o_exist_face == "fail",
    )
    _ = (
        o0,
        unique_o_orient_a,
        one_cover_face,
        one_split_face,
        unsigned_orient,
        perp_o1,
        nsopp_m_a,
        x_o1,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
