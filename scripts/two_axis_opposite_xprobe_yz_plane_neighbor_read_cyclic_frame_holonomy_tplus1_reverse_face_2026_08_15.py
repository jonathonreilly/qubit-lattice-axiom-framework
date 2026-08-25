#!/usr/bin/env python3
"""Neighbor-read of yz-plane cyclic-frame holonomy at t+1 on four x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Perp-step incoming lock. F and Orient
as nm2cycfrmhol. Holonomy and neighbor-read as nm2holyzrd. x-probes as
nm2axx / nm2frmrdx: A=(1,0,0), B=(1,1,1), C=(2,0,0), D=(1,1,0). For each
probe q, S(q) is the yz unit square with a vertex at q as the SW corner
(q, q+e_2, q+e_2+e_3, q+e_3) in B_3(0); else fail, not UNDEFINED.
Neighbor-read of holonomy of S(q). Reverse A,B. Face C,D. Face is displayed,
not adopted. Uniqueness is not required. Occupancy of sites is not used. No
larger host. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_YZ_PLANE_NEIGHBOR_READ_CYCLIC_FRAME_HOLONOMY_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_YZ_PLANE_NEIGHBOR_READ_CYCLIC_FRAME_HOLONOMY_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
AxisSet = frozenset[Point] | str
OrientVal = int | str
FrameVal = tuple[Point, Point, Point] | str
Sending = tuple[Point, Point, Point] | str
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
SAME_LOCK_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
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
LIVE_THREE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
    (E3, E3),
)
Z_PROBES = {
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
    "Neighbor-read of yz-plane cyclic-frame holonomy at t+1 on the "
    "four x-probes of the two-axis opposite seed, and reverse/face from "
    "that, are reported. Displayed, not adopted."
)
IDENTITY_COLUMNS: tuple[Point, Point, Point] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
REVERSE_SQUARE: tuple[Point, Point, Point, Point] = (
    (0, 0, 0),
    (0, 1, 0),
    (0, 1, 1),
    (0, 0, 1),
)
FACE_SQUARE: tuple[Point, Point, Point, Point] = (
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (1, 0, 1),
)
Z_REVERSE_SQUARE: tuple[Point, Point, Point, Point] = (
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1),
)
Z_FACE_SQUARE: tuple[Point, Point, Point, Point] = (
    (0, 0, 2),
    (1, 0, 2),
    (1, 1, 2),
    (0, 1, 2),
)
SQUARE_NAMES = {
    (0, 0, 0): "A",
    (0, 1, 0): "D",
    (0, 1, 1): "B",
    (0, 0, 1): "E",
    (1, 0, 0): "C",
    (1, 1, 0): "C1",
    (1, 1, 1): "C2",
    (1, 0, 1): "C3",
}
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


def pair_display(value: tuple[Point, Point] | str) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if not isinstance(value, tuple):
        raise TypeError(f"signed pair is not a pair or fail: {value!r}")
    return ", ".join(LOCK_NAME[vec] for vec in value)


def frame_display(value: FrameVal) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if not isinstance(value, tuple) or len(value) != 3:
        raise TypeError(f"frame is not a triple or fail: {value!r}")
    return "(" + ", ".join(LOCK_NAME[vec] for vec in value) + ")"


def matrix_display(value: Sending) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if not isinstance(value, tuple) or len(value) != 3:
        raise TypeError(f"sending is not three columns or fail: {value!r}")
    rows = tuple(tuple(value[j][i] for j in range(3)) for i in range(3))
    return "[" + "; ".join(" ".join(str(entry) for entry in row) for row in rows) + "]"


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


def axis_index(lock: Point) -> int | str:
    """Axis index i in {1,2,3} of a signed nearest-neighbor letter."""
    axis = axis_of_letter(lock)
    if axis == E1:
        return 1
    if axis == E2:
        return 2
    if axis == E3:
        return 3
    return "fail"


def cyclic_units(signed_m: Point) -> tuple[Point, Point] | str:
    """e_next = e_{i+1} with 3+1->1. e_prev = e_{i-1} with 1-1->3."""
    idx = axis_index(signed_m)
    if idx == "fail" or not isinstance(idx, int):
        return "fail"
    e_next = AXES[idx % 3]
    e_prev = AXES[idx - 2]
    return e_next, e_prev


def lex_largest_on_axis(outgoing: Outgoing, axis: Point) -> Point | str:
    """Lex-largest signed letter in O intersect {+/-axis}. Order +e < -e."""
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
    """Lex-smallest signed letter in O intersect {+/-axis}. Mutation."""
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
    """o_next, o_prev on the two cyclic axes of Axis(M). Empty slot is fail."""
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
    """Mutation: sign of det(m, e, +l). Not this letter."""
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
    leftover = leftover_unit(signed_m, pair)
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
    det = integer_det_columns(signed_m, plane[0], plane[1])
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
    if signed_m == "fail":
        return "fail"
    if not isinstance(signed_m, tuple):
        return "fail"
    plane = cyclic_signed_outgoing(incoming, outgoing, largest=True)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail":
        return "fail"
    if not isinstance(plane, tuple):
        return "fail"
    o_next, o_prev = plane
    det = integer_det_columns(signed_m, o_next, o_prev)
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def frame_triple(incoming: Incoming, outgoing: Outgoing) -> FrameVal:
    """F=(m,o_next,o_prev) when split HOLDs. Else fail, not UNDEFINED unless unformed."""
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
    return signed_m, plane[0], plane[1]


def transpose_columns(frame: tuple[Point, Point, Point]) -> tuple[Point, Point, Point]:
    """Columns of the transpose. Inverse on signed permutation frames."""
    return tuple(tuple(frame[column][row] for column in range(3)) for row in range(3))  # type: ignore[return-value]


def mul_columns(
    left: tuple[Point, Point, Point], right: tuple[Point, Point, Point]
) -> tuple[Point, Point, Point]:
    """Integer matrix product of two column-triple matrices."""
    return tuple(
        tuple(
            sum(left[k][i] * right[j][k] for k in range(3)) for i in range(3)
        )
        for j in range(3)
    )  # type: ignore[return-value]


def sending_matrix(source: FrameVal, target: FrameVal) -> Sending:
    """Integer matrix P with F(r) = F(q) P, sending columns of F(q) to F(r)."""
    if source == UNDEFINED or target == UNDEFINED:
        return UNDEFINED
    if source == "fail" or target == "fail":
        return "fail"
    if not isinstance(source, tuple) or not isinstance(target, tuple):
        return "fail"
    return mul_columns(transpose_columns(source), target)


def is_signed_permutation(value: Sending) -> bool:
    """Exactly one nonzero +/-1 in each row and each column."""
    if not isinstance(value, tuple) or len(value) != 3:
        return False
    for column in value:
        if any(entry not in (-1, 0, 1) for entry in column):
            return False
        if sum(abs(entry) for entry in column) != 1:
            return False
    rows = tuple(tuple(value[j][i] for j in range(3)) for i in range(3))
    return all(sum(abs(entry) for entry in row) == 1 for row in rows)


def sending_holds(
    source: FrameVal, target: FrameVal, orient_q: OrientVal, orient_r: OrientVal
) -> str:
    """HOLD iff P is a signed permutation with det = Orient(q)Orient(r)."""
    sending = sending_matrix(source, target)
    if sending == UNDEFINED:
        return UNDEFINED
    if sending == "fail" or not isinstance(sending, tuple):
        return "fail"
    if orient_q not in (1, -1) or orient_r not in (1, -1):
        return "fail"
    det = integer_det_columns(sending[0], sending[1], sending[2])
    if is_signed_permutation(sending) and det == orient_q * orient_r:
        return "hold"
    return "fail"


def is_nonnegative_permutation(value: Sending) -> bool:
    """Unsigned permutation: signed permutation with no minus signs. Mutation."""
    if not is_signed_permutation(value):
        return False
    if not isinstance(value, tuple):
        return False
    return all(entry >= 0 for column in value for entry in column)


def site_sides(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Incoming, Outgoing]:
    if site not in ticks:
        return UNDEFINED, UNDEFINED
    tau = ticks[site] + 1
    return (
        incoming_set(site, tau, ticks, locks, seed_map),
        outgoing_set(site, tau, ticks, locks, seed_map),
    )


def formed_six_neighbors(site: Point, ticks: dict[Point, int]) -> tuple[Point, ...]:
    """Formed 6-NN of site in B_3(0). Not a six-neighbor star letter."""
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks:
            found.append(neighbor)
    return tuple(found)


def frame_transport(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff split HOLD, Orient +/-1, and some formed 6-NN r transports."""
    incoming, outgoing = site_sides(site, ticks, locks, seed_map)
    split = axis_split(incoming, outgoing)
    orient = frame_orient(incoming, outgoing)
    if split == UNDEFINED or orient == UNDEFINED:
        return UNDEFINED
    if split != "hold" or orient not in (1, -1):
        return "fail"
    source = frame_triple(incoming, outgoing)
    if not isinstance(source, tuple):
        return "fail"
    for neighbor in formed_six_neighbors(site, ticks):
        n_in, n_out = site_sides(neighbor, ticks, locks, seed_map)
        n_split = axis_split(n_in, n_out)
        n_orient = frame_orient(n_in, n_out)
        if n_split != "hold" or n_orient not in (1, -1):
            continue
        target = frame_triple(n_in, n_out)
        if sending_holds(source, target, orient, n_orient) == "hold":
            return "hold"
    return "fail"


def first_transport_witness(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, Sending] | str:
    """First formed 6-NN in NN order that transports. Uniqueness is not required."""
    incoming, outgoing = site_sides(site, ticks, locks, seed_map)
    split = axis_split(incoming, outgoing)
    orient = frame_orient(incoming, outgoing)
    if split == UNDEFINED or orient == UNDEFINED:
        return UNDEFINED
    if split != "hold" or orient not in (1, -1):
        return "fail"
    source = frame_triple(incoming, outgoing)
    if not isinstance(source, tuple):
        return "fail"
    for neighbor in formed_six_neighbors(site, ticks):
        n_in, n_out = site_sides(neighbor, ticks, locks, seed_map)
        n_split = axis_split(n_in, n_out)
        n_orient = frame_orient(n_in, n_out)
        if n_split != "hold" or n_orient not in (1, -1):
            continue
        target = frame_triple(n_in, n_out)
        sending = sending_matrix(source, target)
        if sending_holds(source, target, orient, n_orient) == "hold":
            return neighbor, sending
    return "fail"


def scalar_orient_neighbor(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Mutation: HOLD iff some formed 6-NN has the same scalar Orient sign."""
    incoming, outgoing = site_sides(site, ticks, locks, seed_map)
    orient = frame_orient(incoming, outgoing)
    if orient == UNDEFINED:
        return UNDEFINED
    if orient not in (1, -1):
        return "fail"
    for neighbor in formed_six_neighbors(site, ticks):
        n_in, n_out = site_sides(neighbor, ticks, locks, seed_map)
        if frame_orient(n_in, n_out) == orient:
            return "hold"
    return "fail"


def unique_positive_sending(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Mutation: unique nonnegative permutation sending. Not this letter."""
    incoming, outgoing = site_sides(site, ticks, locks, seed_map)
    split = axis_split(incoming, outgoing)
    orient = frame_orient(incoming, outgoing)
    if split == UNDEFINED or orient == UNDEFINED:
        return UNDEFINED
    if split != "hold" or orient not in (1, -1):
        return "fail"
    source = frame_triple(incoming, outgoing)
    if not isinstance(source, tuple):
        return "fail"
    hits = 0
    for neighbor in formed_six_neighbors(site, ticks):
        n_in, n_out = site_sides(neighbor, ticks, locks, seed_map)
        n_orient = frame_orient(n_in, n_out)
        target = frame_triple(n_in, n_out)
        sending = sending_matrix(source, target)
        if (
            sending_holds(source, target, orient, n_orient) == "hold"
            and is_nonnegative_permutation(sending)
        ):
            hits += 1
    if hits == 1:
        return "hold"
    return "fail"


def site_frame_state(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[str, OrientVal, FrameVal]:
    """split, Orient, F at tau=t+1. Outside the host is fail, not UNDEFINED."""
    if not in_ball(site):
        return "fail", "fail", "fail"
    incoming, outgoing = site_sides(site, ticks, locks, seed_map)
    return (
        axis_split(incoming, outgoing),
        frame_orient(incoming, outgoing),
        frame_triple(incoming, outgoing),
    )


def edge_sending(
    source: Point,
    target: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Sending:
    """P(q,r) on a formed six-neighbor pair, else fail. Outside is fail."""
    if not in_ball(source) or not in_ball(target):
        return "fail"
    if source not in ticks or target not in ticks:
        return UNDEFINED
    if sub(target, source) not in NN:
        return "fail"
    _split_q, orient_q, frame_q = site_frame_state(source, ticks, locks, seed_map)
    _split_r, orient_r, frame_r = site_frame_state(target, ticks, locks, seed_map)
    sending = sending_matrix(frame_q, frame_r)
    if sending_holds(frame_q, frame_r, orient_q, orient_r) == "hold":
        return sending
    if sending == UNDEFINED:
        return UNDEFINED
    return "fail"


def product_columns(
    matrices: tuple[Sending, Sending, Sending, Sending],
) -> Sending:
    """Four-matrix product P12 P23 P34 P41 in column convention."""
    if any(item == UNDEFINED for item in matrices):
        return UNDEFINED
    if any(not isinstance(item, tuple) for item in matrices):
        return "fail"
    product: tuple[Point, Point, Point] = IDENTITY_COLUMNS
    for item in matrices:
        if not isinstance(item, tuple):
            return "fail"
        product = mul_columns(product, item)
    return product


def square_holonomy(
    vertices: tuple[Point, Point, Point, Point],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff split HOLD, Orient +/-1, every edge has P, product is I_3."""
    if any(not in_ball(site) for site in vertices):
        return "fail"
    splits: list[str] = []
    orients: list[OrientVal] = []
    sendings: list[Sending] = []
    for site in vertices:
        split, orient, _frame = site_frame_state(site, ticks, locks, seed_map)
        splits.append(split)
        orients.append(orient)
    if any(item == UNDEFINED for item in splits) or any(
        item == UNDEFINED for item in orients
    ):
        return UNDEFINED
    for index in range(4):
        sendings.append(
            edge_sending(
                vertices[index],
                vertices[(index + 1) % 4],
                ticks,
                locks,
                seed_map,
            )
        )
    if any(item == UNDEFINED for item in sendings):
        return UNDEFINED
    if any(split != "hold" for split in splits):
        return "fail"
    if any(orient not in (1, -1) for orient in orients):
        return "fail"
    if any(not isinstance(item, tuple) for item in sendings):
        return "fail"
    product = product_columns(
        (sendings[0], sendings[1], sendings[2], sendings[3])
    )
    if product == IDENTITY_COLUMNS:
        return "hold"
    return "fail"


def shift_square(
    vertices: tuple[Point, Point, Point, Point], step: Point
) -> tuple[Point, Point, Point, Point]:
    """Translate a unit square by one lattice step. Not a six-neighbor star."""
    return (
        add(vertices[0], step),
        add(vertices[1], step),
        add(vertices[2], step),
        add(vertices[3], step),
    )


def formed_square_translate(
    vertices: tuple[Point, Point, Point, Point], ticks: dict[Point, int]
) -> bool:
    """True iff every vertex is formed in B_3(0). Outside the host is not formed."""
    return all(in_ball(site) and site in ticks for site in vertices)


def square_neighbor_read(
    vertices: tuple[Point, Point, Point, Point],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff holonomy(S) HOLDs and some formed 6-NN translate has holonomy HOLD.

    If holonomy fails at S, neighbor-read fails, not UNDEFINED.
    """
    holonomy = square_holonomy(vertices, ticks, locks, seed_map)
    if holonomy != "hold":
        return "fail"
    for step in NN:
        neighbor = shift_square(vertices, step)
        if not formed_square_translate(neighbor, ticks):
            continue
        if square_holonomy(neighbor, ticks, locks, seed_map) == "hold":
            return "hold"
    return "fail"


def first_holonomy_neighbor_witness(
    vertices: tuple[Point, Point, Point, Point],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, tuple[Point, Point, Point, Point]] | str:
    """First formed 6-NN translate whose holonomy HOLDs, else fail."""
    holonomy = square_holonomy(vertices, ticks, locks, seed_map)
    if holonomy != "hold":
        return "fail"
    for step in NN:
        neighbor = shift_square(vertices, step)
        if not formed_square_translate(neighbor, ticks):
            continue
        if square_holonomy(neighbor, ticks, locks, seed_map) == "hold":
            return step, neighbor
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


def reverse_report(orient_a: OrientVal, orient_b: OrientVal) -> str:
    """Orient reverse HOLDs iff Orient(A)=Orient(B) both +/-1. Contrast."""
    return pair_orient(orient_a, orient_b)


def face_report(orient_c: OrientVal, orient_d: OrientVal) -> str:
    """Orient face HOLDs iff Orient(C)=Orient(D) both +/-1. Contrast."""
    return pair_orient(orient_c, orient_d)


def transport_reverse_report(left: str, right: str) -> str:
    """Reverse HOLDs iff transport at A and at B."""
    return pair_bit(left, right)


def transport_face_report(left: str, right: str) -> str:
    """Face HOLDs iff transport at C and at D."""
    return pair_bit(left, right)


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
    plane = cyclic_signed_outgoing(frozenset({unsigned_m}), outgoing, largest=True)
    if not isinstance(plane, tuple):
        return "fail"
    det = integer_det_columns(unsigned_m, plane[0], plane[1])
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



def yz_unit_square(vertex: Point) -> tuple[Point, Point, Point, Point]:
    """Yz-plane unit square with a vertex at the probe as SW corner."""
    return (
        vertex,
        add(vertex, E2),
        add(vertex, add(E2, E3)),
        add(vertex, E3),
    )


def square_or_fail_read(
    vertices: tuple[Point, Point, Point, Point],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[str, str, str]:
    """Holonomy, neighbor-read, witness. Outside B_3(0) is fail, not UNDEFINED."""
    if any(not in_ball(site) for site in vertices):
        return "fail", "fail", "fail"
    holonomy = square_holonomy(vertices, ticks, locks, seed_map)
    nread = square_neighbor_read(vertices, ticks, locks, seed_map)
    witness = first_holonomy_neighbor_witness(vertices, ticks, locks, seed_map)
    if holonomy == UNDEFINED:
        return UNDEFINED, UNDEFINED, UNDEFINED
    if holonomy != "hold":
        return "fail", "fail", "fail"
    return holonomy, nread, "fail" if witness == "fail" else witness


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("neighbor-read of yz-plane cyclic-frame holonomy reverse/face at t+1 on two-axis opposite x-probes")
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
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "x-probes-as-nm2axx-not-y-or-z",
        x_probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and y_probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and z_probe_sites == ((0, 0, 1), (1, 1, 1), (0, 0, 2), (1, 0, 1))
        and x_probe_sites != y_probe_sites
        and x_probe_sites != z_probe_sites
        and set(x_probe_sites) <= host,
    )
    checks.check(
        "yz-square-at-probe-is-sw-corner-in-host-or-fail",
        yz_unit_square(X_PROBES["A"]) == FACE_SQUARE
        and yz_unit_square(X_PROBES["B"])
        == ((1, 1, 1), (1, 2, 1), (1, 2, 2), (1, 1, 2))
        and yz_unit_square(X_PROBES["C"])
        == ((2, 0, 0), (2, 1, 0), (2, 1, 1), (2, 0, 1))
        and yz_unit_square(X_PROBES["D"])
        == ((1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 1, 1))
        and all(in_ball(site) for site in yz_unit_square(X_PROBES["A"]))
        and all(in_ball(site) for site in yz_unit_square(X_PROBES["B"]))
        and all(in_ball(site) for site in yz_unit_square(X_PROBES["C"]))
        and all(in_ball(site) for site in yz_unit_square(X_PROBES["D"]))
        and not all(in_ball(site) for site in yz_unit_square(Y_PROBES["C"]))
        and yz_unit_square(ORIGIN) == REVERSE_SQUARE,
    )
    checks.check(
        "host-is-euclidean-not-taxicab",
        (2, 2, 0) in host and dot((2, 2, 0), (2, 2, 0)) == 8 and 2 + 2 + 0 > 3,
    )
    checks.check(
        "id-add-dot-perp",
        add(ORIGIN, E1) == E1
        and add(NEG_E1, E1) == ZERO
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(X_PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "orient-identity",
        frame_orient(UNDEFINED, frozenset({E2, E3})) == UNDEFINED
        and frame_orient(frozenset({E2}), UNDEFINED) == UNDEFINED
        and frame_orient(frozenset(), frozenset({E1, E3})) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and frame_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == -1
        and cyclic_units(E1) == (E2, E3)
        and cyclic_units(E2) == (E3, E1)
        and cyclic_units(E3) == (E1, E2)
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1
        and leftover_match(frozenset(), frozenset()) == "fail",
    )
    identity_frame = (E2, E3, NEG_E1)
    identity_target = (E1, NEG_E2, NEG_E3)
    checks.check(
        "sending-identity",
        sending_holds(identity_frame, identity_frame, -1, -1) == "hold"
        and sending_holds(identity_frame, identity_target, -1, 1) == "hold"
        and is_signed_permutation((E1, E2, E3))
        and not is_nonnegative_permutation(
            sending_matrix(identity_frame, identity_target)
        ),
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
    live_ticks, live_locks, live_seeds = form(LIVE_THREE_AXIS_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)

    m1, o1 = probe_sides(X_PROBES, ticks, locks, seed_map)
    m0: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    split: dict[str, str] = {}
    cover: dict[str, str] = {}
    orient: dict[str, OrientVal] = {}
    frames: dict[str, FrameVal] = {}
    transport: dict[str, str] = {}
    scalar: dict[str, str] = {}
    unique_pos: dict[str, str] = {}
    signed_m: dict[str, Point | str] = {}
    cyclic_plane: dict[str, tuple[Point, Point] | str] = {}
    axis_i: dict[str, int | str] = {}
    det: dict[str, int | str] = {}
    lex: dict[str, OrientVal] = {}
    leftover_pair: dict[str, OrientVal] = {}
    unique_signed: dict[str, OrientVal] = {}
    cyclic_small: dict[str, OrientVal] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    pair_present: dict[str, str] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    squares: dict[str, tuple[Point, Point, Point, Point]] = {}
    hol: dict[str, str] = {}
    nread: dict[str, str] = {}
    hol_witness: dict[str, object] = {}
    sendings: dict[str, tuple[Sending, Sending, Sending, Sending]] = {}
    products: dict[str, Sending] = {}
    square_split: dict[str, dict[Point, str]] = {}
    square_orient: dict[str, dict[Point, OrientVal]] = {}
    square_frame: dict[str, dict[Point, FrameVal]] = {}
    translate_bits: dict[str, tuple[str, ...]] = {}

    for name in ("A", "B", "C", "D"):
        site = X_PROBES[name]
        tau = ticks[site]
        m0[name] = incoming_set(site, tau, ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau, ticks, locks, seed_map)
        split[name] = axis_split(m1[name], o1[name])
        cover[name] = axis_cover(m1[name], o1[name])
        orient[name] = frame_orient(m1[name], o1[name])
        frames[name] = frame_triple(m1[name], o1[name])
        transport[name] = frame_transport(site, ticks, locks, seed_map)
        scalar[name] = scalar_orient_neighbor(site, ticks, locks, seed_map)
        unique_pos[name] = unique_positive_sending(site, ticks, locks, seed_map)
        signed_m[name] = unique_signed_m(m1[name])
        cyclic_plane[name] = cyclic_signed_outgoing(m1[name], o1[name], largest=True)
        if isinstance(signed_m[name], tuple):
            axis_i[name] = axis_index(signed_m[name])
        else:
            axis_i[name] = "fail"
        if isinstance(signed_m[name], tuple) and isinstance(cyclic_plane[name], tuple):
            det[name] = integer_det_columns(
                signed_m[name], cyclic_plane[name][0], cyclic_plane[name][1]
            )
        else:
            det[name] = "fail"
        lex[name] = lex_frame_orient(m1[name], o1[name])
        leftover_pair[name] = leftover_pair_orient(m1[name], o1[name])
        unique_signed[name] = unique_signed_orient(m1[name], o1[name])
        cyclic_small[name] = cyclic_lex_smallest_orient(m1[name], o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        pair_present[name] = has_opposite_pair(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        squares[name] = yz_unit_square(site)
        hol[name], nread[name], hol_witness[name] = square_or_fail_read(
            squares[name], ticks, locks, seed_map
        )
        sendings[name] = tuple(
            edge_sending(
                squares[name][index],
                squares[name][(index + 1) % 4],
                ticks,
                locks,
                seed_map,
            )
            for index in range(4)
        )
        products[name] = product_columns(sendings[name])
        square_split[name] = {}
        square_orient[name] = {}
        square_frame[name] = {}
        for vertex in squares[name]:
            sp, ori, fr = site_frame_state(vertex, ticks, locks, seed_map)
            square_split[name][vertex] = sp
            square_orient[name][vertex] = ori
            square_frame[name][vertex] = fr
        translate_bits[name] = tuple(
            square_holonomy(shift_square(squares[name], step), ticks, locks, seed_map)
            if all(in_ball(v) for v in shift_square(squares[name], step))
            else "fail"
            for step in NN
        )
        print(
            f"{name} {site} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"split={split[name]} "
            f"F={frame_display(frames[name])} "
            f"Orient={orient_display(orient[name])} "
            f"S={squares[name]} "
            f"holonomy={hol[name]} "
            f"nread={nread[name]}"
        )

    reverse = pair_bit(nread["A"], nread["B"])
    face = pair_bit(nread["C"], nread["D"])
    reverse_holonomy = pair_bit(hol["A"], hol["B"])
    face_holonomy = pair_bit(hol["C"], hol["D"])
    transport_reverse = pair_bit(transport["A"], transport["B"])
    transport_face = pair_bit(transport["C"], transport["D"])
    orient_reverse = reverse_report(orient["A"], orient["B"])
    orient_face = face_report(orient["C"], orient["D"])
    scalar_reverse = pair_bit(scalar["A"], scalar["B"])
    scalar_face = pair_bit(scalar["C"], scalar["D"])
    unique_pos_reverse = pair_bit(unique_pos["A"], unique_pos["B"])
    unique_pos_face = pair_bit(unique_pos["C"], unique_pos["D"])
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
    orig_reverse = square_neighbor_read(REVERSE_SQUARE, ticks, locks, seed_map)
    orig_face = square_neighbor_read(FACE_SQUARE, ticks, locks, seed_map)
    orig_reverse_hol = square_holonomy(REVERSE_SQUARE, ticks, locks, seed_map)
    orig_face_hol = square_holonomy(FACE_SQUARE, ticks, locks, seed_map)
    outside_square = ((4, 0, 0), (4, 1, 0), (4, 1, 1), (4, 0, 1))
    outside_holonomy = square_holonomy(outside_square, ticks, locks, seed_map)
    outside_read = square_neighbor_read(outside_square, ticks, locks, seed_map)
    y_hol = {}
    y_nread = {}
    y_in_host = {}
    for name in ("A", "B", "C", "D"):
        ysq = yz_unit_square(Y_PROBES[name])
        y_in_host[name] = all(in_ball(site) for site in ysq)
        yh, yn, _yw = square_or_fail_read(ysq, ticks, locks, seed_map)
        y_hol[name] = yh
        y_nread[name] = yn
    y_reverse = pair_bit(y_nread["A"], y_nread["B"])
    y_face = pair_bit(y_nread["C"], y_nread["D"])
    y_transport = {
        name: frame_transport(Y_PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    y_transport_reverse = pair_bit(y_transport["A"], y_transport["B"])
    y_transport_face = pair_bit(y_transport["C"], y_transport["D"])
    z_transport = {
        name: frame_transport(Z_PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    z_transport_reverse = pair_bit(z_transport["A"], z_transport["B"])
    z_transport_face = pair_bit(z_transport["C"], z_transport["D"])
    z_nread = {}
    for name in ("A", "B", "C", "D"):
        _zh, zn, _zw = square_or_fail_read(
            yz_unit_square(Z_PROBES[name]), ticks, locks, seed_map
        )
        z_nread[name] = zn
    z_square_reverse = pair_bit(z_nread["A"], z_nread["B"])
    one_nread = {
        name: square_or_fail_read(
            yz_unit_square(X_PROBES[name]), one_ticks, one_locks, one_seeds
        )[1]
        for name in ("A", "B", "C", "D")
    }
    same_nread = {
        name: square_or_fail_read(
            yz_unit_square(X_PROBES[name]), same_ticks, same_locks, same_seeds
        )[1]
        for name in ("A", "B", "C", "D")
    }
    live_nread = {
        name: square_or_fail_read(
            yz_unit_square(X_PROBES[name]), live_ticks, live_locks, live_seeds
        )[1]
        for name in ("A", "B", "C", "D")
    }
    one_reverse = pair_bit(one_nread["A"], one_nread["B"])
    one_face = pair_bit(one_nread["C"], one_nread["D"])
    same_reverse = pair_bit(same_nread["A"], same_nread["B"])
    same_face = pair_bit(same_nread["C"], same_nread["D"])
    live_reverse = pair_bit(live_nread["A"], live_nread["B"])
    live_face = pair_bit(live_nread["C"], live_nread["D"])
    orig_one_reverse = square_neighbor_read(
        REVERSE_SQUARE, one_ticks, one_locks, one_seeds
    )
    orig_live_reverse = square_neighbor_read(
        REVERSE_SQUARE, live_ticks, live_locks, live_seeds
    )
    orig_same_reverse = square_neighbor_read(
        REVERSE_SQUARE, same_ticks, same_locks, same_seeds
    )
    neighbor_only_a = "fail"
    for step in NN:
        neighbor = shift_square(squares["A"], step)
        if not formed_square_translate(neighbor, ticks):
            continue
        if square_holonomy(neighbor, ticks, locks, seed_map) == "hold":
            neighbor_only_a = "hold"
            break

    print(f"holonomy reverse={reverse_holonomy} face={face_holonomy}")
    print(f"neighbor-read reverse={reverse} face={face}")
    print(f"transport reverse={transport_reverse} face={transport_face}")
    print(f"orig yz-square neighbor-read reverse={orig_reverse} face={orig_face}")
    print(
        "per_element: cyclic frame F and neighbor-read of four-edge holonomy of S(q) at t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: S(q), edge sendings, holonomy, neighbor-read, reverse/face")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    second_pair_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    ) and all(ticks.get(add(PAIR2, step)) != 1 for step in (E2, NEG_E2))
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and second_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[X_PROBES["A"]] == 2
        and ticks[X_PROBES["B"]] == 1
        and ticks[X_PROBES["C"]] == 3
        and ticks[X_PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(X_PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(X_PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and frame_orient(
            incoming_set(X_PROBES["C"], 0, ticks, locks, seed_map),
            outgoing_set(X_PROBES["C"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_transport(X_PROBES["B"], {ORIGIN: 0}, {ORIGIN: {E1}}, {ORIGIN: E1})
        == UNDEFINED,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[X_PROBES["A"]] == 2
        and ticks[X_PROBES["B"]] == 1
        and ticks[X_PROBES["C"]] == 3
        and ticks[X_PROBES["D"]] == 2
        and X_PROBES["A"] not in seed_map,
        str({name: ticks[X_PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-O-split",
        m1["A"] == frozenset({NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({NEG_E3})
        and o1["A"] == frozenset({E1})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1})
        and split["A"] == "fail"
        and split["B"] == "hold"
        and split["C"] == "hold"
        and split["D"] == "fail"
        and cover["A"] == "fail"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "fail",
    )
    checks.check(
        "theorem1-Orient-and-F",
        signed_m["A"] == NEG_E3
        and signed_m["B"] == E1
        and signed_m["C"] == E1
        and signed_m["D"] == NEG_E3
        and axis_i["A"] == 3
        and axis_i["B"] == 1
        and axis_i["C"] == 1
        and axis_i["D"] == 3
        and cyclic_plane["A"] == "fail"
        and cyclic_plane["B"] == (E2, NEG_E3)
        and cyclic_plane["C"] == (NEG_E2, NEG_E3)
        and cyclic_plane["D"] == "fail"
        and det["A"] == "fail"
        and det["B"] == -1
        and det["C"] == 1
        and det["D"] == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["D"] == "fail"
        and frames["A"] == "fail"
        and frames["B"] == (E1, E2, NEG_E3)
        and frames["C"] == (E1, NEG_E2, NEG_E3)
        and frames["D"] == "fail",
    )
    checks.check(
        "theorem1-squares-holonomy-neighbor-read",
        squares["A"] == FACE_SQUARE
        and hol["A"] == "fail"
        and hol["B"] == "fail"
        and hol["C"] == "fail"
        and hol["D"] == "fail"
        and nread["A"] == "fail"
        and nread["B"] == "fail"
        and nread["C"] == "fail"
        and nread["D"] == "fail"
        and hol_witness["A"] == "fail"
        and hol_witness["B"] == "fail"
        and hol_witness["C"] == "fail"
        and hol_witness["D"] == "fail"
        and products["A"] == "fail"
        and products["B"] == "fail"
        and products["C"] == "fail"
        and products["D"] == "fail"
        and sendings["A"][0] == "fail"
        and sendings["A"][1] == "fail"
        and sendings["A"][2] == ((1, 0, 0), (0, -1, 0), (0, 0, 1))
        and sendings["A"][3] == "fail"
        and sendings["B"][0] == ((0, 1, 0), (0, 0, -1), (1, 0, 0))
        and sendings["C"][0] == ((1, 0, 0), (0, -1, 0), (0, 0, 1))
        and sendings["D"][2] == ((0, 0, 1), (1, 0, 0), (0, -1, 0))
        and integer_det_columns(*sendings["A"][2]) == -1
        and square_split["A"][(1, 0, 0)] == "fail"
        and square_split["A"][(1, 1, 0)] == "fail"
        and square_split["A"][(1, 1, 1)] == "hold"
        and square_split["A"][(1, 0, 1)] == "hold"
        and square_split["B"][(1, 2, 2)] == "fail"
        and square_split["C"][(2, 1, 1)] == "fail"
        and square_split["C"][(2, 0, 1)] == "fail"
        and translate_bits["A"] == ("fail", "hold", "fail", "fail", "fail", "fail")
        and neighbor_only_a == "hold"
        and neighbor_only_a != nread["A"]
        and orig_face == nread["A"]
        and orig_face_hol == hol["A"],
        f"nread={ {name: nread[name] for name in ('A','B','C','D')} }",
    )
    checks.check(
        "theorem2-reverse-neighbor-read-fail",
        reverse == "fail"
        and reverse != UNDEFINED
        and reverse != "hold"
        and reverse_holonomy == "fail"
        and nread["A"] == "fail"
        and nread["B"] == "fail"
        and orig_reverse == "hold"
        and orig_reverse_hol == "hold"
        and orig_reverse != reverse
        and transport_reverse == "fail"
        and transport["B"] == "hold"
        and nread["B"] != transport["B"]
        and orient_reverse == "fail"
        and scalar_reverse == "fail"
        and unique_pos_reverse == "fail"
        and split_reverse == "fail"
        and cover_reverse == "fail",
    )
    checks.check(
        "theorem3-face-neighbor-read-fail",
        face == "fail"
        and face != UNDEFINED
        and face != "hold"
        and face_holonomy == "fail"
        and nread["C"] == "fail"
        and nread["D"] == "fail"
        and transport_face == "fail"
        and transport["C"] == "hold"
        and nread["C"] != transport["C"]
        and orient_face == "fail"
        and scalar_face == "fail"
        and unique_pos_face == "fail"
        and split_face == "fail"
        and cover_face == "fail"
        and outside_holonomy == "fail"
        and outside_holonomy != UNDEFINED
        and outside_read == "fail"
        and outside_read != UNDEFINED
        and all(in_ball(site) for site in squares["C"])
        and not y_in_host["C"],
    )
    checks.check(
        "not-leftover-of-nm2holyzrd-yz-square",
        orig_reverse == "hold"
        and orig_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and orig_reverse != reverse
        and squares["A"] == FACE_SQUARE
        and ORIGIN not in squares["A"]
        and ORIGIN not in squares["B"]
        and ORIGIN not in squares["C"]
        and ORIGIN not in squares["D"]
        and set(REVERSE_SQUARE).isdisjoint(set(x_probe_sites)),
    )
    checks.check(
        "not-leftover-of-y-probe-or-z-probe-or-transport",
        y_reverse == "fail"
        and y_face == "fail"
        and y_in_host["A"]
        and not y_in_host["C"]
        and y_nread["C"] == "fail"
        and nread["C"] == "fail"
        and all(in_ball(site) for site in squares["C"])
        and ticks[Y_PROBES["A"]] == 0
        and ticks[X_PROBES["A"]] == 2
        and y_transport_reverse == "hold"
        and y_transport_face == "fail"
        and y_transport_reverse != reverse
        and z_transport_reverse == "hold"
        and z_transport_face == "hold"
        and z_transport_reverse != reverse
        and z_square_reverse == "fail"
        and transport_reverse == "fail"
        and transport["B"] == "hold"
        and transport["C"] == "hold"
        and nread["B"] == "fail"
        and nread["C"] == "fail",
    )
    checks.check(
        "cover-and-split-do-not-score-handedness",
        split_reverse == "fail"
        and cover_reverse == "fail"
        and reverse == "fail"
        and split_face == "fail"
        and cover_face == "fail"
        and face == "fail"
        and leftover_pair["B"] == -1
        and leftover_pair["C"] == -1
        and lex["B"] == 1
        and lex["C"] == 1
        and lex["B"] != orient["B"]
        and cyclic_small["B"] == 1
        and cyclic_small["C"] == -1
        and cyclic_small["B"] != orient["B"],
    )
    checks.check(
        "split-fail-is-orient-fail-not-undefined",
        frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and orient["A"] == "fail"
        and orient["A"] != UNDEFINED
        and hol["A"] == "fail"
        and hol["A"] != UNDEFINED
        and nread["A"] == "fail"
        and nread["A"] != UNDEFINED,
    )
    checks.check(
        "empty-Oi-is-orient-fail-not-undefined",
        cyclic_signed_outgoing(frozenset({E2}), frozenset()) == "fail"
        and cyclic_signed_outgoing(frozenset({E3}), frozenset({E1})) == "fail"
        and frame_orient(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and cyclic_plane["A"] == "fail"
        and orient["A"] == "fail",
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E1})
        and all(frame_orient(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D")),
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
        "theorem1-mixed-O-cyclic-not-unique",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and orient["B"] == -1
        and orient["B"] != UNDEFINED,
    )
    checks.check(
        "not-leftover-of-1-axis-or-same-lock-or-live-three-axis",
        TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != SAME_LOCK_SEEDS
        and TWO_AXIS_SEEDS != LIVE_THREE_AXIS_SEEDS
        and TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and one_ticks[X_PROBES["A"]] == 3
        and one_ticks[X_PROBES["C"]] == 4
        and ticks[X_PROBES["A"]] == 2
        and ticks[X_PROBES["C"]] == 3
        and same_ticks[X_PROBES["A"]] == 3
        and live_ticks[X_PROBES["D"]] == 1
        and one_reverse == "fail"
        and one_face == "fail"
        and same_reverse == "fail"
        and same_face == "fail"
        and live_reverse == "fail"
        and live_face == "fail"
        and orig_one_reverse == "hold"
        and orig_same_reverse == "hold"
        and orig_live_reverse == "fail"
        and orig_one_reverse != reverse
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3
        and sum(time == 0 for time in live_ticks.values()) == 3
        and incoming_set(
            X_PROBES["A"],
            perp_ticks[X_PROBES["A"]] + 1,
            perp_ticks,
            perp_locks,
            perp_seeds,
        )
        != m1["A"]
        and incoming_set(
            X_PROBES["A"],
            zsym_ticks[X_PROBES["A"]] + 1,
            zsym_ticks,
            zsym_locks,
            zsym_seeds,
        )
        != m1["A"],
    )
    checks.check(
        "not-leftover-empty-or-one-sided",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and lx["A"] == frozenset({E2})
        and lx["B"] == frozenset()
        and pair_present["A"] == "fail"
        and pair_present["B"] == "hold"
        and pair_present["C"] == "hold"
        and pair_present["D"] == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) != face,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E3 in m1["A"]
        and NEG_E3 not in o1["A"]
        and o1["A"] != m1["A"]
        and sum_of_set(o1["B"]) == E2,
    )
    checks.check(
        "second-pair-is-seed-not-formed-child",
        PAIR2 in seed_map
        and seed_map[PAIR2] == NEG_E2
        and ticks[PAIR2] == 0
        and E3 in seed_map
        and seed_map[E3] == E2
        and ticks[E3] == 0
        and one_ticks[E3] == 1
        and PAIR2 not in new_meet["A"],
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-squares-holonomy-nread",
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
        and "split(A) = fail" in note
        and "split(B) = hold" in note
        and "split(C) = hold" in note
        and "split(D) = fail" in note
        and "F(A) = fail" in note
        and "F(B) = (+e_1, +e_2, −e_3)" in note
        and "F(C) = (+e_1, −e_2, −e_3)" in note
        and "F(D) = fail" in note
        and "Orient(A) = fail" in note
        and "Orient(B) = −1" in note
        and "Orient(C) = +1" in note
        and "Orient(D) = fail" in note
        and "S(A) = ((1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1))" in note
        and "S(B) = ((1, 1, 1), (1, 2, 1), (1, 2, 2), (1, 1, 2))" in note
        and "S(C) = ((2, 0, 0), (2, 1, 0), (2, 1, 1), (2, 0, 1))" in note
        and "S(D) = ((1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 1, 1))" in note
        and "holonomy(S(A)) = fail" in note
        and "holonomy(S(B)) = fail" in note
        and "holonomy(S(C)) = fail" in note
        and "holonomy(S(D)) = fail" in note
        and "neighbor-read(S(A)) = fail" in note
        and "neighbor-read(S(B)) = fail" in note
        and "neighbor-read(S(C)) = fail" in note
        and "neighbor-read(S(D)) = fail" in note
        and (
            "holonomy(S(A) − e_1) = hold" in note
            or "holonomy(C-C1-C2-C3 − e_1) = hold" in note
        ),
    )
    checks.check(
        "note-reports-P-and-split-on-squares",
        "P(S(A)_0→S(A)_1) = fail" in note
        and "P(S(A)_2→S(A)_3) = [1 0 0; 0 -1 0; 0 0 1]" in note
        and "split(S(A)_0) = fail" in note
        and "split(S(A)_2) = hold" in note
        and "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)" in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-split-or-leftovers",
        "Cover and split do not score handedness" in note
        and "not leftover of nm2holyzrd" in normalized_note
        and "not leftover of LIVE y-probe nm2yzrdy" in normalized_note
        and "not leftover of nm2frmrdx" in normalized_note
        and "not leftover of nm2axx axis-cover" in normalized_note
        and "not leftover of nm2ax12x 1-in 2-out split" in normalized_note
        and "not leftover of nm2cycfrmz cyclic-frame transport" in normalized_note
        and "not leftover of scalar neighbor-read" in normalized_note
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
        and "Reverse neighbor-read cyclic-frame holonomy at τ: fail" in note
        and "Face neighbor-read cyclic-frame holonomy at τ: fail" in note,
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
        '    "docs/TWO_AXIS_OPPOSITE_XPROBE_YZ_PLANE_NEIGHBOR_READ_CYCLIC_FRAME_HOLONOMY_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "cyclic_signed_outgoing" in defined_fns
        and "frame_triple" in defined_fns
        and "edge_sending" in defined_fns
        and "square_holonomy" in defined_fns
        and "square_neighbor_read" in defined_fns
        and "yz_unit_square" in defined_fns
        and "shift_square" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[X_PROBES["A"]] == 2
        and set(ticks) <= host,
    )
    checks.check(
        "holonomy-not-transport-or-orig-square-or-y-probe",
        reverse == "fail"
        and face == "fail"
        and orig_reverse == "hold"
        and orig_face == "fail"
        and transport["B"] == "hold"
        and transport["C"] == "hold"
        and nread["B"] == "fail"
        and nread["C"] == "fail"
        and y_transport_reverse == "hold"
        and y_reverse == "fail"
        and scalar_reverse == "fail"
        and unique_pos_reverse == "fail"
        and leftover_reverse == "fail"
        and reverse_report(lex["B"], lex["C"]) == "hold"
        and reverse_report(unique_signed["A"], unique_signed["B"]) == "fail"
        and o_exist_reverse == "fail",
    )
    _ = (
        unique_pos_face,
        scalar_face,
        reverse_holonomy,
        face_holonomy,
        neighbor_only_a,
        orig_face_hol,
        zsym_ticks,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
