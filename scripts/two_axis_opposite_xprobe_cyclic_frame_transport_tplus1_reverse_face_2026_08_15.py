#!/usr/bin/env python3
"""Cyclic-frame transport of (m,o_next,o_prev) at t+1 reverse/face.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process and x-probes as nm2axx.
Perp-step incoming lock. M, O, split as nm2ax12x. Orient as nm2oricyclz
(lex-largest cyclic). Unformed => UNDEFINED. When split HOLDs,
F(q)=(m,o_next,o_prev) is an oriented lattice frame. Transport HOLDs at q
iff split HOLDs at q, Orient(q) is +/-1, and some formed 6-NN r has split
HOLD, Orient(r) +/-1, and the 3x3 integer matrix sending the columns of
F(q) to the columns of F(r) is a signed permutation with determinant
Orient(q)*Orient(r). If split or Orient fails at q, transport fails, not
UNDEFINED. Reverse HOLDs iff transport at A and at B. Face on C,D.
Neighbor-read of the scalar Orient sign is a different object. Uniqueness
is not required. Occupancy of sites is not used. No larger host.
Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Cyclic-frame transport of (m,o_next,o_prev) at t+1 on the four x-probes "
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("cyclic-frame transport of (m,o_next,o_prev) reverse/face at t+1 on two-axis opposite x-probes")
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
        and probe_sites != z_probe_sites
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
        integer_det_columns(E2, E3, NEG_E1) == -1
        and integer_det_columns(E1, E2, NEG_E3) == -1
        and integer_det_columns(E3, NEG_E1, NEG_E2) == 1
        and integer_det_columns(E1, NEG_E2, NEG_E3) == 1
        and integer_det_columns(E2, E3, E1) == 1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(E3, E1, NEG_E2) == -1
        and integer_det_columns(E1, E1, E2) == 0,
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
        and frame_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == -1
        and frame_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == -1
        and frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == 1
        and frame_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == -1
        and frame_orient(frozenset({E1, NEG_E1}), frozenset({E2, E3})) == "fail"
        and cyclic_units(E2) == (E3, E1)
        and cyclic_units(E1) == (E2, E3)
        and cyclic_units(E3) == (E1, E2)
        and cyclic_units(NEG_E2) == (E3, E1)
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1
        and lex_largest_on_axis(frozenset({E1}), E1) == E1
        and lex_smallest_on_axis(frozenset({E1, NEG_E1}), E1) == E1
        and cyclic_signed_outgoing(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == (E3, NEG_E1)
        and cyclic_signed_outgoing(frozenset({E1}), frozenset({E2, E3, NEG_E3}))
        == (E2, NEG_E3)
        and cyclic_signed_outgoing(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2}))
        == (NEG_E1, NEG_E2)
        and cyclic_signed_outgoing(frozenset({E1}), frozenset({NEG_E2, E3, NEG_E3}))
        == (NEG_E2, NEG_E3)
        and cyclic_signed_outgoing(frozenset({E2}), frozenset({E1})) == "fail"
        and unique_signed_outgoing_plane(frozenset({E1, NEG_E1, E3})) == "fail"
        and unique_signed_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == "fail"
        and lex_frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == 1
        and leftover_pair_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == -1
        and cyclic_lex_smallest_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == 1
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
    identity_frame = (E2, E3, NEG_E1)
    identity_target = (E1, NEG_E2, NEG_E3)
    identity_sending = sending_matrix(identity_frame, identity_target)
    checks.check(
        "sending-identity",
        frame_triple(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == (E2, E3, NEG_E1)
        and sending_matrix(UNDEFINED, identity_frame) == UNDEFINED
        and sending_matrix(identity_frame, "fail") == "fail"
        and sending_matrix(identity_frame, identity_frame)
        == (E1, E2, E3)
        and is_signed_permutation((E1, E2, E3))
        and not is_signed_permutation((E1, E1, E2))
        and sending_holds(identity_frame, identity_frame, -1, -1) == "hold"
        and sending_holds(identity_frame, identity_target, -1, 1) == "hold"
        and integer_det_columns(*identity_sending) == -1
        and is_signed_permutation(identity_sending)
        and not is_nonnegative_permutation(identity_sending)
        and mul_columns(identity_frame, identity_sending) == identity_target,
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    live_ticks, live_locks, live_seeds = form(LIVE_THREE_AXIS_SEEDS)
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
    plane: dict[str, tuple[Point, Point] | str] = {}
    pair: dict[str, Point | str] = {}
    leftover: dict[str, Point | str] = {}
    det: dict[str, int | str] = {}
    lex: dict[str, OrientVal] = {}
    leftover_pair: dict[str, OrientVal] = {}
    unique_signed: dict[str, OrientVal] = {}
    pair_present: dict[str, str] = {}
    unique_plane: dict[str, tuple[Point, Point] | str] = {}
    lex_plane: dict[str, tuple[Point, Point] | str] = {}
    cyclic_plane: dict[str, tuple[Point, Point] | str] = {}
    cyclic_small: dict[str, OrientVal] = {}
    axis_i: dict[str, int | str] = {}
    orient: dict[str, OrientVal] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    frames: dict[str, FrameVal] = {}
    transport: dict[str, str] = {}
    scalar: dict[str, str] = {}
    unique_pos: dict[str, str] = {}
    witness: dict[str, tuple[Point, Sending] | str] = {}
    formed_nn: dict[str, tuple[Point, ...]] = {}
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
        plane[name] = outgoing_plane(axis_o[name])
        unique_plane[name] = unique_signed_outgoing_plane(o1[name])
        lex_plane[name] = lex_signed_outgoing_plane(o1[name])
        cyclic_plane[name] = cyclic_signed_outgoing(m1[name], o1[name], largest=True)
        pair[name] = opposite_pair_unit(o1[name])
        if isinstance(signed_m[name], tuple):
            axis_i[name] = axis_index(signed_m[name])
        else:
            axis_i[name] = "fail"
        if isinstance(signed_m[name], tuple) and isinstance(pair[name], tuple):
            leftover[name] = leftover_unit(signed_m[name], pair[name])
        else:
            leftover[name] = "fail"
        if isinstance(signed_m[name], tuple) and isinstance(cyclic_plane[name], tuple):
            det[name] = integer_det_columns(
                signed_m[name], cyclic_plane[name][0], cyclic_plane[name][1]
            )
        else:
            det[name] = "fail"
        pair_present[name] = has_opposite_pair(o1[name])
        lex[name] = lex_frame_orient(m1[name], o1[name])
        leftover_pair[name] = leftover_pair_orient(m1[name], o1[name])
        unique_signed[name] = unique_signed_orient(m1[name], o1[name])
        cyclic_small[name] = cyclic_lex_smallest_orient(m1[name], o1[name])
        orient[name] = frame_orient(m1[name], o1[name])
        frames[name] = frame_triple(m1[name], o1[name])
        transport[name] = frame_transport(site, ticks, locks, seed_map)
        scalar[name] = scalar_orient_neighbor(site, ticks, locks, seed_map)
        unique_pos[name] = unique_positive_sending(site, ticks, locks, seed_map)
        witness[name] = first_transport_witness(site, ticks, locks, seed_map)
        formed_nn[name] = formed_six_neighbors(site, ticks)
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        witness_text = "fail"
        if isinstance(witness[name], tuple):
            witness_text = (
                f"{witness[name][0]} P={matrix_display(witness[name][1])}"
            )
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"split={split[name]} "
            f"F={frame_display(frames[name])} "
            f"Orient={orient_display(orient[name])} "
            f"transport={transport[name]} "
            f"scalar={scalar[name]} "
            f"witness={witness_text}"
        )

    reverse = transport_reverse_report(transport["A"], transport["B"])
    face = transport_face_report(transport["C"], transport["D"])
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
    unsigned_orient = {
        name: unsigned_incoming_orient(m1[name], o1[name])
        for name in ("A", "B", "C", "D")
    }
    unique_o_orient_a = frame_orient(unique_letter(m1["A"]), unique_letter(o1["A"]))
    unique_o_orient_b = frame_orient(unique_letter(m1["B"]), unique_letter(o1["B"]))
    one_m1, one_o1 = probe_sides(PROBES, one_ticks, one_locks, one_seeds)
    one_cover = {name: axis_cover(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_split = {name: axis_split(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_orient = {
        name: frame_orient(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")
    }
    one_cover_face = pair_bit(one_cover["C"], one_cover["D"])
    one_split_face = pair_bit(one_split["C"], one_split["D"])
    one_orient_face = face_report(one_orient["C"], one_orient["D"])
    one_transport = {
        name: frame_transport(PROBES[name], one_ticks, one_locks, one_seeds)
        for name in ("A", "B", "C", "D")
    }
    one_transport_face = transport_face_report(
        one_transport["C"], one_transport["D"]
    )
    live_transport = {
        name: frame_transport(PROBES[name], live_ticks, live_locks, live_seeds)
        for name in ("A", "B", "C", "D")
    }
    live_transport_face = transport_face_report(
        live_transport["C"], live_transport["D"]
    )
    same_transport = {
        name: frame_transport(PROBES[name], same_ticks, same_locks, same_seeds)
        for name in ("A", "B", "C", "D")
    }
    same_transport_face = transport_face_report(
        same_transport["C"], same_transport["D"]
    )
    print(f"transport reverse={reverse} face={face}")
    print(f"Orient reverse={orient_reverse} face={orient_face}")
    print(f"scalar reverse={scalar_reverse} face={scalar_face}")
    print(f"split reverse={split_reverse} face={split_face}")
    print(f"cover reverse={cover_reverse} face={cover_face}")
    print(
        "per_element: cyclic frame F=(m,o_next,o_prev) and signed-permutation "
        "sending to a formed 6-NN at a probe's t+1"
    )
    print("per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four transport reports, reverse/face from transport at paired probes")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    z_transport = {
        name: frame_transport(Z_PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    z_transport_reverse = transport_reverse_report(z_transport["A"], z_transport["B"])
    z_transport_face = transport_face_report(z_transport["C"], z_transport["D"])
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
        and ticks[ORIGIN] == 0
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
        and frame_transport(PROBES["B"], {ORIGIN: 0}, {ORIGIN: {E1}}, {ORIGIN: E1})
        == UNDEFINED
        and frame_triple(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED,
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
        str({name: (lockset_display(m1[name]), split[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Orient",
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
        and unique_plane["A"] == "fail"
        and unique_plane["B"] == "fail"
        and unique_plane["C"] == "fail"
        and unique_plane["D"] == "fail"
        and det["A"] == "fail"
        and det["B"] == -1
        and det["C"] == 1
        and det["D"] == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["D"] == "fail"
        and plane["A"] == "fail"
        and pair["A"] == "fail"
        and frames["A"] == "fail"
        and frames["B"] == (E1, E2, NEG_E3)
        and frames["C"] == (E1, NEG_E2, NEG_E3)
        and frames["D"] == "fail",
        str({name: orient_display(orient[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-transport",
        transport["A"] == "fail"
        and transport["B"] == "hold"
        and transport["C"] == "hold"
        and transport["D"] == "fail"
        and witness["A"] == "fail"
        and isinstance(witness["B"], tuple)
        and isinstance(witness["C"], tuple)
        and witness["D"] == "fail"
        and witness["B"] == ((0, 1, 1), ((0, -1, 0), (0, 0, -1), (-1, 0, 0)))
        and witness["C"] == ((2, 1, 0), ((1, 0, 0), (0, -1, 0), (0, 0, 1)))
        and integer_det_columns(*witness["B"][1]) == -1
        and integer_det_columns(*witness["C"][1]) == -1
        and integer_det_columns(*witness["B"][1]) == orient["B"] * 1
        and integer_det_columns(*witness["C"][1]) == orient["C"] * -1
        and sending_holds(
            frames["B"],
            frame_triple(
                incoming_set(
                    witness["B"][0], ticks[witness["B"][0]] + 1, ticks, locks, seed_map
                ),
                outgoing_set(
                    witness["B"][0], ticks[witness["B"][0]] + 1, ticks, locks, seed_map
                ),
            ),
            orient["B"],
            frame_orient(
                incoming_set(
                    witness["B"][0], ticks[witness["B"][0]] + 1, ticks, locks, seed_map
                ),
                outgoing_set(
                    witness["B"][0], ticks[witness["B"][0]] + 1, ticks, locks, seed_map
                ),
            ),
        )
        == "hold"
        and scalar["A"] == "fail"
        and scalar["B"] == "fail"
        and scalar["C"] == "fail"
        and scalar["D"] == "fail"
        and all(unique_pos[name] == "fail" for name in ("A", "B", "C", "D"))
        and scalar["B"] != transport["B"]
        and unique_pos["C"] != transport["C"],
        str({name: (transport[name], scalar[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-mixed-O-cyclic-not-unique",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_plane["B"] == "fail"
        and unique_signed["B"] == "fail"
        and cyclic_plane["B"] == (E2, NEG_E3)
        and unique_o_orient_b == UNDEFINED
        and orient["B"] == -1
        and orient["B"] != UNDEFINED
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_o_orient_a == "fail"
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
        and all(frame_orient(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D"))
        and all(frame_triple(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D")),
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
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and m1["A"] == frozenset({NEG_E3})
        and E1 not in seed_map
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {NEG_E2},
    )
    checks.check(
        "theorem2-reverse-transport-fail",
        reverse == "fail"
        and transport["A"] == "fail"
        and transport["B"] == "hold"
        and reverse != UNDEFINED
        and reverse != "hold"
        and orient_reverse == "fail"
        and scalar_reverse == "fail"
        and unique_pos_reverse == "fail"
        and split_reverse == "fail"
        and cover_reverse == "fail"
        and z_transport_reverse == "hold"
        and z_transport_reverse != reverse,
    )
    checks.check(
        "theorem3-face-transport-fail",
        face == "fail"
        and transport["C"] == "hold"
        and transport["D"] == "fail"
        and face != UNDEFINED
        and face != "hold"
        and orient_face == "fail"
        and scalar_face == "fail"
        and unique_pos_face == "fail"
        and split_face == "fail"
        and cover_face == "fail"
        and z_transport_face == "hold"
        and z_transport_face != face
        and scalar["C"] != transport["C"],
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
        and leftover_pair["A"] == "fail"
        and leftover_pair["D"] == "fail"
        and face_report(leftover_pair["C"], leftover_pair["D"]) == "fail"
        and reverse_report(lex["A"], lex["B"]) == "fail"
        and lex["B"] == 1
        and orient["B"] == -1
        and lex["B"] != orient["B"]
        and cover["B"] == "hold"
        and split["B"] == "hold"
        and orient["C"] == 1
        and cover["C"] == "hold"
        and split["C"] == "hold"
        and cover["A"] == "fail"
        and cover["D"] == "fail",
    )
    checks.check(
        "split-fail-is-orient-fail-not-undefined",
        frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold"
        and two_one["A"] == "fail"
        and two_one["D"] == "fail"
        and split["A"] == "fail"
        and orient["A"] == "fail"
        and transport["A"] == "fail"
        and one_orient["C"] == 1
        and one_split["C"] == "hold"
        and one_cover["C"] == "hold"
        and one_cover["A"] == "hold"
        and one_split["A"] == "fail"
        and one_orient["A"] == "fail"
        and one_orient_face == "fail"
        and one_split_face == "fail"
        and one_cover_face == "hold"
        and one_transport["C"] == "hold"
        and one_transport["D"] == "fail"
        and one_transport_face == "fail"
        and frame_triple(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "fail",
    )
    checks.check(
        "empty-Oi-is-orient-fail-not-undefined",
        cyclic_signed_outgoing(frozenset({E2}), frozenset()) == "fail"
        and cyclic_signed_outgoing(frozenset({E2}), frozenset({E1})) == "fail"
        and cyclic_signed_outgoing(frozenset({E2}), frozenset({E3})) == "fail"
        and frame_orient(frozenset({E2}), frozenset()) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1})) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1,
    )
    checks.check(
        "not-leftover-of-1-axis-cover-face-hold",
        one_ticks[PROBES["A"]] == 3
        and one_ticks[PROBES["C"]] == 4
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["C"]] == 3
        and one_cover["A"] == "hold"
        and cover["A"] == "fail"
        and one_cover_face == "hold"
        and face == "fail"
        and one_cover_face != face
        and one_m1["A"] != m1["A"],
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and lx["A"] == frozenset({E2})
        and lx["B"] == frozenset()
        and lx["C"] == frozenset()
        and lx["D"] == frozenset({E2})
        and leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_match(frozenset({E2}), frozenset()) == "fail"
        and cover["B"] == "hold"
        and transport["B"] == "hold"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and leftover_axis(frozenset({E2}), frozenset({E1, E3})) == frozenset()
        and leftover_match(frozenset(), frozenset()) == "fail",
    )
    checks.check(
        "mutation-leftover-of-M-or-O-alone-differs",
        lx_m["A"] == frozenset({E1, E2})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_o["A"] == frozenset({E2, E3})
        and lx_o["B"] == frozenset({E1})
        and reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and reverse == "fail"
        and face == "fail"
        and lx_m["A"] != lx["A"]
        and lx["B"] == frozenset()
        and lx_m["B"] != lx["B"],
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and pair_present["A"] == "fail"
        and pair_present["B"] == "hold"
        and pair_present["C"] == "hold"
        and pair_present["D"] == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) != face
        and leftover_pair["A"] == "fail"
        and leftover_pair["B"] == -1
        and leftover_pair["C"] == -1
        and leftover_pair["D"] == "fail"
        and face_report(leftover_pair["C"], leftover_pair["D"]) == "fail",
    )
    checks.check(
        "mutation-unsigned-incoming-axis-agrees-here",
        unsigned_orient["A"] == "fail"
        and unsigned_orient["B"] == -1
        and unsigned_orient["C"] == 1
        and unsigned_orient["D"] == "fail"
        and unsigned_orient["B"] == orient["B"]
        and unsigned_orient["C"] == orient["C"]
        and frame_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == -1
        and unsigned_incoming_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == 1
        and frame_orient(frozenset({NEG_E2}), o1["B"]) == "fail"
        and unsigned_incoming_orient(frozenset({NEG_E2}), o1["B"]) == "fail"
        and orient["B"] == -1,
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["B"]) == frozenset({E1})
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_o_orient_b == UNDEFINED
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and unique_signed["D"] == "fail"
        and unique_signed["A"] == "fail"
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["B"] != UNDEFINED
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_o_orient_a == "fail",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["B"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E3
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["B"]) == E2
        and sum_of_set(o1["D"]) == ZERO
        and axis_o["A"] == frozenset({E1})
        and pair["A"] == "fail"
        and leftover["A"] == "fail"
        and cyclic_plane["A"] == "fail"
        and plane["A"] == "fail"
        and cyclic_plane["B"] == (E2, NEG_E3),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E3 in m1["A"]
        and NEG_E3 not in o1["A"]
        and E1 in o1["A"]
        and E1 not in m1["A"]
        and o1["A"] != m1["A"],
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
    y_m1, y_o1 = probe_sides(Y_PROBES, ticks, locks, seed_map)
    y_split = {name: axis_split(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient = {name: frame_orient(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_reverse = reverse_report(y_orient["A"], y_orient["B"])
    y_face = face_report(y_orient["C"], y_orient["D"])
    y_transport = {
        name: frame_transport(Y_PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    y_transport_reverse = transport_reverse_report(y_transport["A"], y_transport["B"])
    y_transport_face = transport_face_report(y_transport["C"], y_transport["D"])
    z_m1, z_o1 = probe_sides(Z_PROBES, ticks, locks, seed_map)
    z_orient = {name: frame_orient(z_m1[name], z_o1[name]) for name in ("A", "B", "C", "D")}
    z_reverse = reverse_report(z_orient["A"], z_orient["B"])
    z_face = face_report(z_orient["C"], z_orient["D"])
    z_transport = {
        name: frame_transport(Z_PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    z_transport_reverse = transport_reverse_report(z_transport["A"], z_transport["B"])
    z_transport_face = transport_face_report(z_transport["C"], z_transport["D"])
    perp_m1, perp_o1 = probe_sides(PROBES, perp_ticks, perp_locks, perp_seeds)
    same_m_a = incoming_set(
        PROBES["A"], same_ticks[PROBES["A"]] + 1, same_ticks, same_locks, same_seeds
    )
    zsym_m1, _zsym_o1 = probe_sides(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    checks.check(
        "not-z-probes-or-y-probes-or-z-symmetric-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != z_probe_sites
        and probe_sites != y_probe_sites
        and y_m1["A"] != m1["A"]
        and y_split["A"] == "hold"
        and y_orient["A"] == 1
        and y_orient["B"] == -1
        and y_reverse == "fail"
        and lex_frame_orient(y_m1["A"], y_o1["A"]) == -1
        and leftover_pair_orient(y_m1["A"], y_o1["A"]) == "fail"
        and unique_signed_orient(y_m1["A"], y_o1["A"]) == 1
        and y_split["D"] == "fail"
        and y_orient["D"] == "fail"
        and y_face == "fail"
        and y_transport["D"] == "fail"
        and y_transport_face == "fail"
        and y_transport_reverse == "hold"
        and z_reverse == "hold"
        and z_face == "hold"
        and z_transport_reverse == "hold"
        and z_transport_face == "hold"
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and reverse == "fail"
        and face == "fail"
        and y_transport_reverse != reverse
        and z_transport_face != face
        and y_transport_face == face,
    )
    checks.check(
        "not-same-lock-or-one-axis-or-live-three-axis-seed",
        TWO_AXIS_SEEDS != SAME_LOCK_SEEDS
        and TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_AXIS_SEEDS != LIVE_THREE_AXIS_SEEDS
        and same_m_a != m1["A"]
        and same_transport_face == "fail"
        and one_transport_face == "fail"
        and live_transport["B"] == "fail"
        and live_transport["C"] == "fail"
        and live_transport["D"] == "hold"
        and live_transport_face == "fail"
        and transport["D"] == "fail"
        and live_transport["D"] != transport["D"]
        and face == "fail"
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3
        and sum(time == 0 for time in live_ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-split-Orient",
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
        and "m(A) = −e_3" in note
        and "i(A) = 3" in note
        and "o_next(A) fail" in note
        and "o_prev(A) fail" in note
        and "det(A) = fail" in note
        and "Orient(A) = fail" in note
        and "m(B) = +e_1" in note
        and "i(B) = 1" in note
        and "o_next(B) = +e_2" in note
        and "o_prev(B) = −e_3" in note
        and "det(B) = -1" in note
        and "Orient(B) = −1" in note
        and "m(C) = +e_1" in note
        and "i(C) = 1" in note
        and "o_next(C) = −e_2" in note
        and "o_prev(C) = −e_3" in note
        and "det(C) = 1" in note
        and "Orient(C) = +1" in note
        and "m(D) = −e_3" in note
        and "i(D) = 3" in note
        and "o_next(D) fail" in note
        and "o_prev(D) fail" in note
        and "det(D) = fail" in note
        and "Orient(D) = fail" in note
        and "F(A) = fail" in note
        and "F(B) = (+e_1, +e_2, −e_3)" in note
        and "F(C) = (+e_1, −e_2, −e_3)" in note
        and "F(D) = fail" in note
        and "transport(A) = fail" in note
        and "transport(B) = hold" in note
        and "transport(C) = hold" in note
        and "transport(D) = fail" in note
        and "scalar neighbor-read(A) = fail" in note
        and "scalar neighbor-read(B) = fail" in note
        and "scalar neighbor-read(C) = fail" in note
        and "scalar neighbor-read(D) = fail" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-transport-reverse-face",
        "Reverse cyclic-frame transport at τ: fail" in note
        and "Face cyclic-frame transport at τ: fail" in note
        and "witness(A) = fail" in note
        and "witness(B) = (0, 1, 1)" in note
        and "witness(C) = (2, 1, 0)" in note
        and "witness(D) = fail" in note,
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
        and "not leftover of nm2axx axis-cover" in normalized_note
        and "not leftover of nm2ax12x 1-in 2-out split" in normalized_note
        and "not leftover of nm2chiralz lexicographic" in normalized_note
        and "not leftover of nm2orichz leftover-axis" in normalized_note
        and "not leftover of nm2orionez lex-one" in normalized_note
        and "not leftover of nm2oridetz unique signed" in normalized_note
        and "not leftover of nm2oricyclz cyclic Orient" in normalized_note
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
        and "Reverse cyclic-frame transport at τ: fail" in note
        and "Face cyclic-frame transport at τ: fail" in note,
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
        '    "docs/TWO_AXIS_OPPOSITE_XPROBE_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "lex_largest_on_axis" in defined_fns
        and "cyclic_units" in defined_fns
        and "unique_signed_outgoing_plane" in defined_fns
        and "leftover_pair_orient" in defined_fns
        and "lex_frame_orient" in defined_fns
        and "cyclic_lex_smallest_orient" in defined_fns
        and "integer_det_columns" in defined_fns
        and "frame_triple" in defined_fns
        and "sending_matrix" in defined_fns
        and "is_signed_permutation" in defined_fns
        and "frame_transport" in defined_fns
        and "scalar_orient_neighbor" in defined_fns
        and "unique_positive_sending" in defined_fns
        and "transport_reverse_report" in defined_fns
        and "transport_face_report" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[ORIGIN] == 0
        and ticks[PROBES["A"]] == 2
        and set(ticks) <= host,
    )
    checks.check(
        "transport-not-scalar-or-orient-equality-or-lex-one",
        reverse == "fail"
        and face == "fail"
        and split_reverse == "fail"
        and cover_reverse == "fail"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and one_orient_face == "fail"
        and one_transport_face == "fail"
        and scalar_reverse == "fail"
        and scalar_face == "fail"
        and unique_pos_reverse == "fail"
        and unique_pos_face == "fail"
        and transport["B"] == "hold"
        and scalar["B"] == "fail"
        and unique_pos["B"] == "fail"
        and transport["C"] == "hold"
        and scalar["C"] == "fail"
        and unique_pos["C"] == "fail"
        and scalar["B"] != transport["B"]
        and unique_pos["C"] != transport["C"]
        and orient_reverse == "fail"
        and orient_face == "fail"
        and lex["A"] == "fail"
        and lex["B"] == 1
        and lex["C"] == 1
        and lex["D"] == "fail"
        and reverse_report(lex["A"], lex["B"]) == "fail"
        and face_report(lex["C"], lex["D"]) == "fail"
        and lex["B"] != orient["B"]
        and leftover_pair["A"] == "fail"
        and leftover_pair["B"] == -1
        and leftover_pair["C"] == -1
        and leftover_pair["D"] == "fail"
        and reverse_report(leftover_pair["A"], leftover_pair["B"]) == "fail"
        and face_report(leftover_pair["C"], leftover_pair["D"]) == "fail"
        and cyclic_small["A"] == "fail"
        and cyclic_small["B"] == 1
        and cyclic_small["C"] == -1
        and cyclic_small["D"] == "fail"
        and reverse_report(cyclic_small["A"], cyclic_small["B"]) == "fail"
        and face_report(cyclic_small["C"], cyclic_small["D"]) == "fail"
        and cyclic_small["B"] != orient["B"]
        and unique_signed["A"] == "fail"
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and unique_signed["D"] == "fail"
        and reverse_report(unique_signed["A"], unique_signed["B"]) == "fail"
        and face_report(unique_signed["C"], unique_signed["D"]) == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and formed_nn["A"][:1] == ((2, 0, 0),)
        and z_transport_reverse != reverse
        and z_transport_face != face,
    )
    _ = (
        o0,
        unique_o_orient_a,
        one_cover_face,
        one_split_face,
        unsigned_orient,
        perp_o1,
        axis_m,
        axis_o,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
