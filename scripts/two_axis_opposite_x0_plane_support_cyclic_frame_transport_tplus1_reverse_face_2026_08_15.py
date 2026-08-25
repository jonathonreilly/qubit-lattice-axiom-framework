#!/usr/bin/env python3
"""x=0 plane support of cyclic-frame transport at t+1 reverse/face.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process as nm2axz. Perp-step
incoming lock. M, O, split as nm2ax12z. Orient as nm2oricyclz (lex-largest
cyclic). Transport as nm2cycfrmz (existential 6-NN sending). Unformed =>
UNDEFINED. Let Q0 be the formed-at-tau sites q in B_3(0) with q_1=0. Let
Q1 be the formed-at-tau sites q in B_3(0) with q_1=1. tau=t(q)+1 is
per-site; a formed site is formed at that cut. Empty Q0 or Q1 is fail, not
UNDEFINED. Reverse HOLDs iff Q0 is nonempty and transport HOLDs at every
q in Q0. Face HOLDs iff Q1 is nonempty and transport HOLDs at every q in
Q1. Not a 6-NN forall. HOLDING transport #7490 on four z-probes, HOLDING
existential neighbor-read #7511, and universal 6-NN neighbor-read fail/fail
#7556 are leftover. Uniqueness is not required. Occupancy of sites is not
used. No larger host. Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_X0_PLANE_SUPPORT_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_X0_PLANE_SUPPORT_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Plane support of cyclic-frame transport on the x=0 versus x=1 formed "
    "sites in B_3 at t+1 on the two-axis opposite seed, and reverse/face from "
    "that, are reported. Displayed, not adopted."
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


def formed_neighbors_at_tau(site: Point, ticks: dict[Point, int]) -> tuple[Point, ...]:
    """N(q): formed 6-NN of q that lie in B_3(0) at tau=t(q)+1."""
    if site not in ticks:
        return ()
    tau = ticks[site] + 1
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] <= tau:
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


def transport_neighbor_read(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover existential #7511: some formed 6-NN r has transport HOLD."""
    own = frame_transport(site, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if own != "hold":
        return "fail"
    for neighbor in formed_six_neighbors(site, ticks):
        if frame_transport(neighbor, ticks, locks, seed_map) == "hold":
            return "hold"
    return "fail"


def first_read_witness(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Point | str:
    """First formed 6-NN in NN order with transport HOLD. Uniqueness is not required."""
    own = frame_transport(site, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if own != "hold":
        return "fail"
    for neighbor in formed_six_neighbors(site, ticks):
        if frame_transport(neighbor, ticks, locks, seed_map) == "hold":
            return neighbor
    return "fail"


def universal_neighbor_read(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff transport HOLDs, N(q) nonempty, and every r in N(q) transports."""
    own = frame_transport(site, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    neighbors = formed_neighbors_at_tau(site, ticks)
    if own != "hold" or not neighbors:
        return "fail"
    for neighbor in neighbors:
        if frame_transport(neighbor, ticks, locks, seed_map) != "hold":
            return "fail"
    return "hold"


def first_universal_fail_witness(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Point | str:
    """First r in N(q) whose transport fails. Uniqueness is not required."""
    own = frame_transport(site, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    neighbors = formed_neighbors_at_tau(site, ticks)
    if own != "hold" or not neighbors:
        return "fail"
    for neighbor in neighbors:
        if frame_transport(neighbor, ticks, locks, seed_map) != "hold":
            return neighbor
    return "fail"


def neighbor_set_display(neighbors: tuple[Point, ...]) -> str:
    if not neighbors:
        return "()"
    return "(" + ", ".join(str(item) for item in neighbors) + ")"


def equal_transport_bit(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover: some formed 6-NN has the same transport bit, including fail=fail."""
    own = frame_transport(site, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    for neighbor in formed_six_neighbors(site, ticks):
        if frame_transport(neighbor, ticks, locks, seed_map) == own:
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
    """Face HOLDs iff transport at C and at D. Leftover contrast."""
    return pair_bit(left, right)


def neighbor_read_reverse_report(left: str, right: str) -> str:
    """Reverse HOLDs iff universal neighbor-read at A and at B."""
    return pair_bit(left, right)


def neighbor_read_face_report(left: str, right: str) -> str:
    """Face HOLDs iff universal neighbor-read at C and at D."""
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


def formed_plane(ticks: dict[Point, int], axis_index: int, value: int) -> tuple[Point, ...]:
    """Formed-at-tau sites in B_3(0) with the named coordinate. Lex order."""
    return tuple(sorted(site for site in ticks if site[axis_index] == value))


def transport_bits(
    sites: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[str, ...]:
    return tuple(frame_transport(site, ticks, locks, seed_map) for site in sites)


def plane_support(
    sites: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff sites nonempty and transport HOLDs at every listed site."""
    if not sites:
        return "fail"
    bits = transport_bits(sites, ticks, locks, seed_map)
    if any(bit == UNDEFINED for bit in bits):
        return UNDEFINED
    if all(bit == "hold" for bit in bits):
        return "hold"
    return "fail"


def first_plane_fail_witness(
    sites: tuple[Point, ...],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Point | str:
    """First listed site whose transport is not HOLD. Uniqueness is not required."""
    if not sites:
        return "fail"
    for site in sites:
        bit = frame_transport(site, ticks, locks, seed_map)
        if bit == UNDEFINED:
            return UNDEFINED
        if bit != "hold":
            return site
    return "fail"


def site_row(site: Point, ticks: dict[Point, int], bit: str) -> str:
    return f"{site} t={ticks[site]} transport={bit}"


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("x=0 plane support of cyclic-frame transport reverse/face at t+1")
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
        integer_det_columns(E2, E3, NEG_E1) == -1
        and integer_det_columns(E1, E2, NEG_E3) == -1
        and integer_det_columns(E3, NEG_E1, NEG_E2) == 1
        and integer_det_columns(E1, NEG_E2, NEG_E3) == 1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(E1, E1, E2) == 0,
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
        and sending_matrix(identity_frame, identity_frame) == (E1, E2, E3)
        and is_signed_permutation((E1, E2, E3))
        and not is_signed_permutation((E1, E1, E2))
        and sending_holds(identity_frame, identity_frame, -1, -1) == "hold"
        and sending_holds(identity_frame, identity_target, -1, 1) == "hold"
        and integer_det_columns(*identity_sending) == -1
        and is_signed_permutation(identity_sending)
        and not is_nonnegative_permutation(identity_sending)
        and mul_columns(identity_frame, identity_sending) == identity_target,
    )
    checks.check(
        "empty-plane-is-fail-not-undefined",
        plane_support((), {}, {}, {}) == "fail"
        and plane_support((), {}, {}, {}) != UNDEFINED
        and first_plane_fail_witness((), {}, {}, {}) == "fail",
    )
    checks.check(
        "orient-identity",
        frame_orient(UNDEFINED, frozenset({E2, E3})) == UNDEFINED
        and frame_orient(frozenset({E2}), UNDEFINED) == UNDEFINED
        and frame_orient(frozenset(), frozenset({E1, E3})) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and cyclic_units(E2) == (E3, E1)
        and cyclic_units(E1) == (E2, E3)
        and cyclic_units(E3) == (E1, E2)
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1
        and leftover_match(frozenset(), frozenset()) == "fail",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    live_ticks, live_locks, live_seeds = form(LIVE_THREE_AXIS_SEEDS)

    q0 = formed_plane(ticks, 0, 0)
    q1 = formed_plane(ticks, 0, 1)
    q0_ticks = tuple(ticks[site] for site in q0)
    q1_ticks = tuple(ticks[site] for site in q1)
    q0_bits = transport_bits(q0, ticks, locks, seed_map)
    q1_bits = transport_bits(q1, ticks, locks, seed_map)
    reverse = plane_support(q0, ticks, locks, seed_map)
    face = plane_support(q1, ticks, locks, seed_map)
    fail0 = first_plane_fail_witness(q0, ticks, locks, seed_map)
    fail1 = first_plane_fail_witness(q1, ticks, locks, seed_map)
    early0 = tuple(site for site in q0 if ticks[site] <= 1)
    early1 = tuple(site for site in q1 if ticks[site] <= 1)
    early_reverse = plane_support(early0, ticks, locks, seed_map)
    early_face = plane_support(early1, ticks, locks, seed_map)
    y0 = formed_plane(ticks, 1, 0)
    y0_support = plane_support(y0, ticks, locks, seed_map)
    xm1 = formed_plane(ticks, 0, -1)
    xm1_support = plane_support(xm1, ticks, locks, seed_map)
    x3 = formed_plane(ticks, 0, 3)
    x3_support = plane_support(x3, ticks, locks, seed_map)

    m1, o1 = probe_sides(PROBES, ticks, locks, seed_map)
    split = {name: axis_split(m1[name], o1[name]) for name in ("A", "B", "C", "D")}
    orient = {name: frame_orient(m1[name], o1[name]) for name in ("A", "B", "C", "D")}
    transport = {
        name: frame_transport(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    univ = {
        name: universal_neighbor_read(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    exist = {
        name: transport_neighbor_read(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    scalar = {
        name: scalar_orient_neighbor(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    unique_pos = {
        name: unique_positive_sending(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    equal_bit = {
        name: equal_transport_bit(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    cover = {name: axis_cover(m1[name], o1[name]) for name in ("A", "B", "C", "D")}
    transport_reverse = transport_reverse_report(transport["A"], transport["B"])
    transport_face = transport_face_report(transport["C"], transport["D"])
    univ_reverse = neighbor_read_reverse_report(univ["A"], univ["B"])
    univ_face = neighbor_read_face_report(univ["C"], univ["D"])
    exist_reverse = neighbor_read_reverse_report(exist["A"], exist["B"])
    exist_face = neighbor_read_face_report(exist["C"], exist["D"])
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
    fail_site: Point = (0, -1, 1)
    fail_transport = frame_transport(fail_site, ticks, locks, seed_map)
    fail_equal = equal_transport_bit(fail_site, ticks, locks, seed_map)
    fail_univ = universal_neighbor_read(fail_site, ticks, locks, seed_map)
    isolated_ticks = {ORIGIN: 0}
    isolated_locks = {ORIGIN: {E1}}
    isolated_seeds = {ORIGIN: E1}
    isolated_transport = frame_transport(
        ORIGIN, isolated_ticks, isolated_locks, isolated_seeds
    )
    one_transport = {
        name: frame_transport(PROBES[name], one_ticks, one_locks, one_seeds)
        for name in ("A", "B", "C", "D")
    }
    one_q0 = formed_plane(one_ticks, 0, 0)
    one_q1 = formed_plane(one_ticks, 0, 1)
    one_reverse = plane_support(one_q0, one_ticks, one_locks, one_seeds)
    one_face = plane_support(one_q1, one_ticks, one_locks, one_seeds)
    same_q0 = formed_plane(same_ticks, 0, 0)
    same_q1 = formed_plane(same_ticks, 0, 1)
    same_reverse = plane_support(same_q0, same_ticks, same_locks, same_seeds)
    same_face = plane_support(same_q1, same_ticks, same_locks, same_seeds)
    live_q0 = formed_plane(live_ticks, 0, 0)
    live_q1 = formed_plane(live_ticks, 0, 1)
    live_reverse = plane_support(live_q0, live_ticks, live_locks, live_seeds)
    live_face = plane_support(live_q1, live_ticks, live_locks, live_seeds)
    expected_q0 = (
        (0, -3, 0),
        (0, -2, -2),
        (0, -2, -1),
        (0, -2, 0),
        (0, -2, 1),
        (0, -2, 2),
        (0, -1, -2),
        (0, -1, -1),
        (0, -1, 0),
        (0, -1, 1),
        (0, -1, 2),
        (0, 0, -3),
        (0, 0, -2),
        (0, 0, -1),
        (0, 0, 0),
        (0, 0, 1),
        (0, 0, 2),
        (0, 1, -2),
        (0, 1, -1),
        (0, 1, 0),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, -2),
        (0, 2, -1),
        (0, 2, 0),
        (0, 2, 1),
        (0, 2, 2),
    )
    expected_q1 = (
        (1, -2, -2),
        (1, -2, -1),
        (1, -2, 0),
        (1, -2, 1),
        (1, -2, 2),
        (1, -1, -2),
        (1, -1, -1),
        (1, -1, 0),
        (1, -1, 1),
        (1, -1, 2),
        (1, 0, -2),
        (1, 0, -1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 0, 2),
        (1, 1, -2),
        (1, 1, -1),
        (1, 1, 0),
        (1, 1, 1),
        (1, 1, 2),
        (1, 2, -2),
        (1, 2, -1),
        (1, 2, 0),
        (1, 2, 1),
        (1, 2, 2),
    )
    expected_t0 = (
        5, 4, 3, 4, 3, 4, 3, 2, 1, 2, 2, 5, 4, 1, 0, 0, 1, 4, 1, 0, 0, 1, 3, 2, 1, 2, 2
    )
    expected_t1 = (
        5, 4, 3, 4, 4, 4, 3, 2, 2, 3, 3, 2, 2, 1, 2, 3, 2, 2, 1, 2, 4, 3, 2, 2, 3
    )
    expected_b0 = (
        "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "hold",
        "fail", "fail", "fail", "fail", "hold", "hold", "hold", "hold", "fail",
        "hold", "hold", "hold", "hold", "fail", "fail", "hold", "fail", "fail",
    )
    expected_b1 = (
        "fail", "fail", "hold", "fail", "fail", "fail", "fail", "hold", "hold",
        "fail", "hold", "hold", "fail", "hold", "fail", "hold", "hold", "fail",
        "hold", "fail", "fail", "fail", "fail", "hold", "fail",
    )

    print(f"|Q0|={len(q0)} hold={q0_bits.count('hold')} fail={q0_bits.count('fail')}")
    print(f"|Q1|={len(q1)} hold={q1_bits.count('hold')} fail={q1_bits.count('fail')}")
    for site, bit in zip(q0, q0_bits):
        print(f"Q0 {site_row(site, ticks, bit)}")
    for site, bit in zip(q1, q1_bits):
        print(f"Q1 {site_row(site, ticks, bit)}")
    print(f"plane-support reverse={reverse} face={face}")
    print(f"fail-witness Q0={fail0} Q1={fail1}")
    print(f"z-probe transport reverse={transport_reverse} face={transport_face}")
    print(f"universal 6-NN reverse={univ_reverse} face={univ_face}")
    print(f"existential 6-NN reverse={exist_reverse} face={exist_face}")
    print(f"early-tick plane reverse={early_reverse} face={early_face}")
    print("per_element: cyclic-frame transport at every formed-at-tau site on the x=0 and x=1 planes")
    print("per_site: scored on formed sites with q_1=0 and q_1=1 in Euclidean B_3(0)")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: Q0/Q1 transport reports, reverse/face from those plane foralls")
    print("lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed")

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
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and frame_transport(PROBES["B"], {ORIGIN: 0}, {ORIGIN: {E1}}, {ORIGIN: E1})
        == UNDEFINED
        and isolated_transport == "fail"
        and isolated_transport != UNDEFINED,
    )
    checks.check(
        "theorem1-Q0-Q1-sites",
        q0 == expected_q0
        and q1 == expected_q1
        and len(q0) == 27
        and len(q1) == 25
        and q0
        and q1
        and all(site[0] == 0 for site in q0)
        and all(site[0] == 1 for site in q1)
        and set(q0) <= set(ticks) <= host
        and set(q1) <= set(ticks)
        and PROBES["A"] in q0
        and PROBES["C"] in q0
        and PROBES["B"] in q1
        and PROBES["D"] in q1
        and ORIGIN in q0
        and PAIR2 in q0,
        f"|Q0|={len(q0)} |Q1|={len(q1)}",
    )
    checks.check(
        "theorem1-ticks-and-transport-bits",
        q0_ticks == expected_t0
        and q1_ticks == expected_t1
        and q0_bits == expected_b0
        and q1_bits == expected_b1
        and q0_bits.count("hold") == 10
        and q0_bits.count("fail") == 17
        and q1_bits.count("hold") == 10
        and q1_bits.count("fail") == 15
        and UNDEFINED not in q0_bits
        and UNDEFINED not in q1_bits
        and transport["A"] == "hold"
        and transport["B"] == "hold"
        and transport["C"] == "hold"
        and transport["D"] == "hold"
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1
        and fail_transport == "fail",
    )
    checks.check(
        "theorem2-reverse-x0-plane-support-fail",
        reverse == "fail"
        and reverse != UNDEFINED
        and reverse != "hold"
        and q0
        and fail0 == (0, -3, 0)
        and fail0 in q0
        and q0_bits[0] == "fail"
        and transport_reverse == "hold"
        and transport_reverse != reverse
        and exist_reverse == "hold"
        and exist_reverse != reverse
        and univ_reverse == "fail"
        and univ["A"] == "hold"
        and univ["B"] == "fail"
        and early_reverse == "hold"
        and early_reverse != reverse
        and y0_support == "fail"
        and xm1_support == "fail"
        and x3_support == "fail"
        and x3 == ()
        and x3_support != UNDEFINED,
    )
    checks.check(
        "theorem3-face-x1-plane-support-fail",
        face == "fail"
        and face != UNDEFINED
        and face != "hold"
        and q1
        and fail1 == (1, -2, -2)
        and fail1 in q1
        and q1_bits[0] == "fail"
        and transport_face == "hold"
        and transport_face != face
        and exist_face == "hold"
        and exist_face != face
        and univ_face == "fail"
        and univ["C"] == "fail"
        and univ["D"] == "fail"
        and early_face == "hold"
        and early_face != face
        and early1 == ((1, 0, 1), (1, 1, 1)),
    )
    checks.check(
        "not-6nn-forall-and-not-zprobe-transport",
        univ_reverse == "fail"
        and univ_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and transport_reverse == "hold"
        and transport_face == "hold"
        and all(exist[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(transport[name] == "hold" for name in ("A", "B", "C", "D"))
        and q0_bits.count("fail") == 17
        and q1_bits.count("fail") == 15
        and formed_six_neighbors(PROBES["A"], ticks)
        != q0
        and fail0 not in formed_six_neighbors(PROBES["A"], ticks),
    )
    checks.check(
        "cover-and-split-do-not-score-plane-support",
        split_reverse == "hold"
        and cover_reverse == "hold"
        and split_face == "hold"
        and cover_face == "hold"
        and orient_reverse == "hold"
        and orient_face == "hold"
        and reverse == "fail"
        and face == "fail"
        and scalar_reverse == "fail"
        and scalar_face == "fail"
        and unique_pos_reverse == "fail"
        and unique_pos_face == "fail"
        and fail_equal == "hold"
        and fail_univ == "fail"
        and fail_equal != fail_univ
        and all(equal_bit[name] == "hold" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "not-leftover-of-1-axis-or-same-lock-or-live",
        TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != SAME_LOCK_SEEDS
        and TWO_AXIS_SEEDS != LIVE_THREE_AXIS_SEEDS
        and TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and one_transport["C"] == "fail"
        and one_reverse == "fail"
        and one_face == "fail"
        and same_reverse == "fail"
        and same_face == "fail"
        and live_reverse == "fail"
        and live_face == "fail"
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3
        and PAIR2 in seed_map
        and seed_map[PAIR2] == NEG_E2
        and ticks[PAIR2] == 0
        and one_ticks[E3] == 1
        and ticks[E3] == 0,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-Q0-Q1-transport",
        "Q0 = formed-at-τ sites q in B_3(0) with q_1=0" in note
        and "Q1 = formed-at-τ sites q in B_3(0) with q_1=1" in note
        and "|Q0|=27" in note
        and "|Q1|=25" in note
        and "transport((0, -3, 0)) = fail" in note
        and "transport((0, 0, 0)) = hold" in note
        and "transport((0, 0, 1)) = hold" in note
        and "transport((1, -2, -2)) = fail" in note
        and "transport((1, 0, 1)) = hold" in note
        and "transport((1, 1, 1)) = hold" in note
        and "t((0, 0, 0))=0" in note
        and "t((0, 0, 1))=0" in note
        and "t((1, 1, 1))=1" in note
        and "t((0, -3, 0))=5" in note
        and "fail-witness(Q0) = (0, -3, 0)" in note
        and "fail-witness(Q1) = (1, -2, -2)" in note
        and "hold-count(Q0) = 10" in note
        and "fail-count(Q0) = 17" in note
        and "hold-count(Q1) = 10" in note
        and "fail-count(Q1) = 15" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse x=0 plane support of cyclic-frame transport at τ: fail" in note
        and "Face x=1 plane support of cyclic-frame transport at τ: fail" in note
        and "Empty Q0 or Q1 is fail, not UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-6nn-or-zprobe-leftovers",
        "not leftover of nm2cycfrmz cyclic-frame transport" in normalized_note
        and "not leftover of existential neighbor-read" in normalized_note
        and "not leftover of universal 6-NN neighbor-read" in normalized_note
        and "Not a 6-NN forall" in note
        and "not leftover of early-tick plane support" in normalized_note
        and "not leftover of nm2axz axis-cover" in normalized_note
        and "not leftover of nm2ax12z 1-in 2-out split" in normalized_note
        and "second pair is a new seed, not a formed child" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-mixed-7188-fail-fail",
        "not leftover of mixed #7188 fail/fail" in normalized_note
        and "Reverse x=0 plane support of cyclic-frame transport at τ: fail" in note
        and "Face x=1 plane support of cyclic-frame transport at τ: fail" in note,
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
        '    "docs/TWO_AXIS_OPPOSITE_X0_PLANE_SUPPORT_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "frame_triple" in defined_fns
        and "sending_matrix" in defined_fns
        and "is_signed_permutation" in defined_fns
        and "frame_transport" in defined_fns
        and "formed_plane" in defined_fns
        and "plane_support" in defined_fns
        and "first_plane_fail_witness" in defined_fns
        and "universal_neighbor_read" in defined_fns
        and "transport_neighbor_read" in defined_fns
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
    _ = (
        perp_ticks,
        perp_locks,
        perp_seeds,
        zsym_ticks,
        zsym_locks,
        zsym_seeds,
        y0,
        xm1,
        one_q0,
        one_q1,
        same_q0,
        same_q1,
        live_q0,
        live_q1,
        unique_pos,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())

