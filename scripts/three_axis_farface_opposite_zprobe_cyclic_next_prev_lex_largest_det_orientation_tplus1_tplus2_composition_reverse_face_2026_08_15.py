#!/usr/bin/env python3
"""Cyclic lex-largest Orient freeze t+1 versus t+2 reverse/face composition.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is three disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2, (0,0,-1) locks +e_3, (0,1,-1) locks
-e_3. The third pair is a new seed, not a formed child, and sits on the -z
face opposite the z-probes. Same process and z-probes as nm2axz. Perp-step
incoming lock. M, O, split as nm2ax12z. Unformed => UNDEFINED. Orient as
nm2oricyclz at each cut. Split HOLDs iff cover HOLDs and |Axis(M)|=1.
Split HOLD required. When split HOLDs, m is the unique vector in M. Let i
in {1,2,3} be the axis index of m. e_next = e_{i+1} with 3+1->1. e_prev =
e_{i-1} with 1-1->3. O_next = O intersect {+/-e_next}. O_prev = O
intersect {+/-e_prev}. If either empty, Orient fails, not UNDEFINED.
Order +e < -e. o_next is the lex-largest vector in O_next (hence -e if
both signs). o_prev likewise. Orient is the sign of the integer
determinant of columns m, o_next, o_prev. If split fails, Orient fails,
not UNDEFINED. Reverse HOLDs iff Orient(A)=Orient(B) both +/-1 at that
cut. Face on C,D at that cut. Composition HOLDs iff Orient at tau1 equals
Orient at tau2 at A,B,C,D. Uniqueness of O is not required. Occupancy of
sites is not used. No larger host. Displayed, not adopted. Do not attach
L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THREE_AXIS_FARFACE_OPPOSITE_ZPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/THREE_AXIS_FARFACE_OPPOSITE_ZPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
PAIR3: Point = (0, 0, -1)
PAIR3B: Point = (0, 1, -1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
AXES: tuple[Point, ...] = (E1, E2, E3)
AXIS_INDEX = {E1: 1, E2: 2, E3: 3}
INDEX_AXIS = {1: E1, 2: E2, 3: E3}
NEXT_INDEX = {1: 2, 2: 3, 3: 1}
PREV_INDEX = {1: 3, 2: 1, 3: 2}
BALL_SQ = 9
TWO_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
THREE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
    (PAIR3, E3),
    (PAIR3B, NEG_E3),
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
    "Cyclic lex-largest orientation at t+1 versus t+2 on the four z-probes "
    "of the three-axis far-face opposite seed, reverse/face at each cut, "
    "and composition, are reported. Displayed, not adopted."
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


def index_display(value: int | str) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if value not in (1, 2, 3):
        raise TypeError(f"axis index is not 1,2,3 or fail: {value!r}")
    return str(value)


def lock_display(value: Point | str) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if value not in LOCK_NAME:
        raise TypeError(f"lock is not a six-neighbor step: {value!r}")
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
    seeds: tuple[tuple[Point, Point], ...] = THREE_AXIS_SEEDS,
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


def cyclic_axis_index(incoming: Incoming) -> int | str:
    """Axis index i of unique m in {1,2,3}. Fail if m is not unique."""
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    axis = axis_of_letter(signed_m)
    if axis not in AXIS_INDEX:
        return "fail"
    return AXIS_INDEX[axis]


def cyclic_next_prev_units(incoming: Incoming) -> tuple[Point, Point] | str:
    """Unsigned e_next, e_prev of Axis(M). Cyclic 3+1->1 and 1-1->3."""
    index = cyclic_axis_index(incoming)
    if index == UNDEFINED:
        return UNDEFINED
    if index == "fail" or index not in NEXT_INDEX:
        return "fail"
    return INDEX_AXIS[NEXT_INDEX[index]], INDEX_AXIS[PREV_INDEX[index]]


def lex_smallest_on_axis(outgoing: Outgoing, axis: Point) -> Point | str:
    """Lex-smallest signed letter in O intersect {+/-axis}. +e < -e."""
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
    """Lex-largest signed letter in O intersect {+/-axis}. Mutation."""
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


def cyclic_next_prev_plane(
    incoming: Incoming,
    outgoing: Outgoing,
    *,
    largest: bool = False,
) -> tuple[Point, Point] | str:
    """Lex-smallest (or lex-largest) o_next, o_prev on cyclic axes of m."""
    units = cyclic_next_prev_units(incoming)
    if units == UNDEFINED:
        return UNDEFINED
    if units == "fail" or not isinstance(units, tuple):
        return "fail"
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
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
    """Lex-smallest signed letter per Axis(O) under +e_i < -e_i."""
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


def lex_one_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: axis-order lex-one o_j, o_k. Not this cyclic letter."""
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
    """Mutation: sign of det(m, o_next, o_prev) with lex-smallest cyclic slots."""
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
    plane = cyclic_next_prev_plane(incoming, outgoing)
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
    plane = cyclic_next_prev_plane(incoming, outgoing, largest=True)
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
    plane = cyclic_next_prev_plane(incoming, outgoing, largest=True)
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
    """Reverse HOLDs iff Orient(A)=Orient(B) both +/-1."""
    return pair_orient(orient_a, orient_b)


def face_report(orient_c: OrientVal, orient_d: OrientVal) -> str:
    """Face HOLDs iff Orient(C)=Orient(D) both +/-1."""
    return pair_orient(orient_c, orient_d)


def composition_report(
    left_a: OrientVal,
    right_a: OrientVal,
    left_b: OrientVal,
    right_b: OrientVal,
    left_c: OrientVal,
    right_c: OrientVal,
    left_d: OrientVal,
    right_d: OrientVal,
) -> str:
    """HOLD iff Orient at tau1 equals Orient at tau2 at A, B, C, and D."""
    sides = (left_a, right_a, left_b, right_b, left_c, right_c, left_d, right_d)
    if any(side == UNDEFINED for side in sides):
        return UNDEFINED
    if (
        left_a == right_a
        and left_b == right_b
        and left_c == right_c
        and left_d == right_d
    ):
        return "hold"
    return "fail"


def leftover_bit_composition(rev1: str, rev2: str, face1: str, face2: str) -> str:
    """Leftover: score composition on reverse/face bits, not Orient equality."""
    if any(bit == UNDEFINED for bit in (rev1, rev2, face1, face2)):
        return UNDEFINED
    if rev1 != rev2 or face1 != face2:
        return "fail"
    return "hold"


def leftover_mo_composition(
    m1_a: Incoming,
    m2_a: Incoming,
    o1_a: Outgoing,
    o2_a: Outgoing,
    m1_b: Incoming,
    m2_b: Incoming,
    o1_b: Outgoing,
    o2_b: Outgoing,
    m1_c: Incoming,
    m2_c: Incoming,
    o1_c: Outgoing,
    o2_c: Outgoing,
    m1_d: Incoming,
    m2_d: Incoming,
    o1_d: Outgoing,
    o2_d: Outgoing,
) -> str:
    """Leftover of nm2simt2z: M and O freeze, not Orient equality."""
    sides = (
        m1_a,
        m2_a,
        o1_a,
        o2_a,
        m1_b,
        m2_b,
        o1_b,
        o2_b,
        m1_c,
        m2_c,
        o1_c,
        o2_c,
        m1_d,
        m2_d,
        o1_d,
        o2_d,
    )
    if any(side == UNDEFINED for side in sides):
        return UNDEFINED
    if (
        m1_a == m2_a
        and o1_a == o2_a
        and m1_b == m2_b
        and o1_b == o2_b
        and m1_c == m2_c
        and o1_c == o2_c
        and m1_d == m2_d
        and o1_d == o2_d
    ):
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
    offset: int = 1,
) -> tuple[Point, ...]:
    """Records in B_3(0) that form at t(site)+offset and are 6-NN of site."""
    formation = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] == formation + offset:
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
    plane = cyclic_next_prev_plane(incoming, outgoing, largest=True)
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


def probe_sides_at(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    offset: int,
) -> tuple[dict[str, Incoming], dict[str, Outgoing]]:
    incoming: dict[str, Incoming] = {}
    outgoing: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            incoming[name] = UNDEFINED
            outgoing[name] = UNDEFINED
            continue
        tau = site_ticks[site] + offset
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

    print("cyclic lex-largest Orient freeze t+1 versus t+2 reverse/face composition on three-axis far-face opposite z-probes")
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
        integer_det_columns(E2, E1, E3) == -1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(E2, E3, E1) == 1
        and integer_det_columns(E3, E1, E2) == 1
        and integer_det_columns(E3, E1, NEG_E2) == -1
        and integer_det_columns(E1, NEG_E2, E3) == -1
        and integer_det_columns(E2, E3, NEG_E1) == -1
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
        and cyclic_axis_index(frozenset({E2})) == 2
        and cyclic_axis_index(frozenset({E1})) == 1
        and cyclic_axis_index(frozenset({E3})) == 3
        and cyclic_next_prev_units(frozenset({E2})) == (E3, E1)
        and cyclic_next_prev_units(frozenset({E1})) == (E2, E3)
        and cyclic_next_prev_units(frozenset({E3})) == (E1, E2)
        and cyclic_next_prev_plane(frozenset({E2}), frozenset({E1, E3})) == (E3, E1)
        and cyclic_next_prev_plane(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == (E3, E1)
        and cyclic_next_prev_plane(
            frozenset({E2}), frozenset({E1, NEG_E1, E3}), largest=True
        )
        == (E3, NEG_E1)
        and lex_smallest_on_axis(frozenset({E1, NEG_E1}), E1) == E1
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1
        and cyclic_next_prev_plane(frozenset({E2}), frozenset({E1})) == "fail"
        and cyclic_next_prev_plane(frozenset({E2}), frozenset()) == "fail"
        and unique_signed_outgoing_plane(frozenset({E1, NEG_E1, E3})) == "fail"
        and unique_signed_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == "fail"
        and lex_one_orient(frozenset({E2}), frozenset({E1, E3})) == -1
        and lex_largest_cyclic_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == -1
        and cyclic_lex_smallest_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == 1
        and lex_frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == 1
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
    checks.check(
        "composition-identity",
        composition_report(-1, -1, -1, -1, 1, 1, -1, -1) == "hold"
        and composition_report(-1, -1, -1, -1, 1, -1, -1, -1) == "fail"
        and composition_report(-1, "fail", -1, -1, 1, 1, -1, -1) == "fail"
        and composition_report("fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail")
        == "hold"
        and composition_report(UNDEFINED, -1, -1, -1, 1, 1, -1, -1) == UNDEFINED
        and leftover_bit_composition("hold", "hold", "fail", "fail") == "hold"
        and leftover_bit_composition("hold", "hold", "fail", "hold") == "fail",
    )

    ticks, locks, seed_map = form()
    two_ticks, two_locks, two_seeds = form(TWO_AXIS_SEEDS)
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    tau2: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    m2: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    o2: dict[str, Outgoing] = {}
    axis_m: dict[str, AxisSet] = {}
    axis_o: dict[str, AxisSet] = {}
    cover: dict[str, str] = {}
    cover2: dict[str, str] = {}
    split0: dict[str, str] = {}
    split: dict[str, str] = {}
    split2: dict[str, str] = {}
    two_one: dict[str, str] = {}
    signed_m: dict[str, Point | str] = {}
    signed_m2: dict[str, Point | str] = {}
    plane: dict[str, tuple[Point, Point] | str] = {}
    pair: dict[str, Point | str] = {}
    leftover: dict[str, Point | str] = {}
    det: dict[str, int | str] = {}
    det2: dict[str, int | str] = {}
    lex: dict[str, OrientVal] = {}
    lex2: dict[str, OrientVal] = {}
    leftover_pair: dict[str, OrientVal] = {}
    leftover_pair2: dict[str, OrientVal] = {}
    unique_signed: dict[str, OrientVal] = {}
    unique_signed2: dict[str, OrientVal] = {}
    pair_present: dict[str, str] = {}
    pair_present2: dict[str, str] = {}
    unique_plane: dict[str, tuple[Point, Point] | str] = {}
    unique_plane2: dict[str, tuple[Point, Point] | str] = {}
    lex_plane: dict[str, tuple[Point, Point] | str] = {}
    cyclic_plane: dict[str, tuple[Point, Point] | str] = {}
    cyclic_plane2: dict[str, tuple[Point, Point] | str] = {}
    largest_plane: dict[str, tuple[Point, Point] | str] = {}
    index: dict[str, int | str] = {}
    index2: dict[str, int | str] = {}
    lex_one: dict[str, OrientVal] = {}
    lex_one2: dict[str, OrientVal] = {}
    largest: dict[str, OrientVal] = {}
    largest2: dict[str, OrientVal] = {}
    cyclic_small: dict[str, OrientVal] = {}
    cyclic_small2: dict[str, OrientVal] = {}
    orient0: dict[str, OrientVal] = {}
    orient: dict[str, OrientVal] = {}
    orient2: dict[str, OrientVal] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    new_meet2: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        tau2[name] = ticks[site] + 2
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        m2[name] = incoming_set(site, tau2[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        o2[name] = outgoing_set(site, tau2[name], ticks, locks, seed_map)
        axis_m[name] = axis_set(m1[name])
        axis_o[name] = axis_set(o1[name])
        cover[name] = axis_cover(m1[name], o1[name])
        cover2[name] = axis_cover(m2[name], o2[name])
        split0[name] = axis_split(m0[name], o0[name])
        split[name] = axis_split(m1[name], o1[name])
        split2[name] = axis_split(m2[name], o2[name])
        two_one[name] = two_in_one_out(m1[name], o1[name])
        signed_m[name] = unique_signed_m(m1[name])
        signed_m2[name] = unique_signed_m(m2[name])
        index[name] = cyclic_axis_index(m1[name])
        index2[name] = cyclic_axis_index(m2[name])
        plane[name] = outgoing_plane(axis_o[name])
        unique_plane[name] = unique_signed_outgoing_plane(o1[name])
        unique_plane2[name] = unique_signed_outgoing_plane(o2[name])
        lex_plane[name] = lex_signed_outgoing_plane(o1[name])
        cyclic_plane[name] = cyclic_next_prev_plane(m1[name], o1[name], largest=True)
        cyclic_plane2[name] = cyclic_next_prev_plane(m2[name], o2[name], largest=True)
        largest_plane[name] = cyclic_next_prev_plane(m1[name], o1[name], largest=True)
        pair[name] = opposite_pair_unit(o1[name])
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
        if isinstance(signed_m2[name], tuple) and isinstance(cyclic_plane2[name], tuple):
            det2[name] = integer_det_columns(
                signed_m2[name], cyclic_plane2[name][0], cyclic_plane2[name][1]
            )
        else:
            det2[name] = "fail"
        pair_present[name] = has_opposite_pair(o1[name])
        pair_present2[name] = has_opposite_pair(o2[name])
        lex[name] = lex_frame_orient(m1[name], o1[name])
        lex2[name] = lex_frame_orient(m2[name], o2[name])
        lex_one[name] = lex_one_orient(m1[name], o1[name])
        lex_one2[name] = lex_one_orient(m2[name], o2[name])
        leftover_pair[name] = leftover_pair_orient(m1[name], o1[name])
        leftover_pair2[name] = leftover_pair_orient(m2[name], o2[name])
        unique_signed[name] = unique_signed_orient(m1[name], o1[name])
        unique_signed2[name] = unique_signed_orient(m2[name], o2[name])
        largest[name] = lex_largest_cyclic_orient(m1[name], o1[name])
        largest2[name] = lex_largest_cyclic_orient(m2[name], o2[name])
        cyclic_small[name] = cyclic_lex_smallest_orient(m1[name], o1[name])
        cyclic_small2[name] = cyclic_lex_smallest_orient(m2[name], o2[name])
        orient0[name] = frame_orient(m0[name], o0[name])
        orient[name] = frame_orient(m1[name], o1[name])
        orient2[name] = frame_orient(m2[name], o2[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks, 1)
        new_meet2[name] = new_records_meeting_six_nn(site, ticks, 2)
        print(
            f"{name} t={ticks[site]} "
            f"M(tau1)={lockset_display(m1[name])} "
            f"O(tau1)={lockset_display(o1[name])} "
            f"split(tau1)={split[name]} "
            f"i(tau1)={index_display(index[name])} "
            f"o_next(tau1)={lock_display(cyclic_plane[name][0]) if isinstance(cyclic_plane[name], tuple) else cyclic_plane[name]} "
            f"o_prev(tau1)={lock_display(cyclic_plane[name][1]) if isinstance(cyclic_plane[name], tuple) else cyclic_plane[name]} "
            f"det(tau1)={det[name]} "
            f"Orient(tau1)={orient_display(orient[name])} "
            f"M(tau2)={lockset_display(m2[name])} "
            f"O(tau2)={lockset_display(o2[name])} "
            f"Orient(tau2)={orient_display(orient2[name])}"
        )

    reverse = reverse_report(orient["A"], orient["B"])
    reverse2 = reverse_report(orient2["A"], orient2["B"])
    face = face_report(orient["C"], orient["D"])
    face2 = face_report(orient2["C"], orient2["D"])
    reverse0 = reverse_report(orient0["A"], orient0["B"])
    face0 = face_report(orient0["C"], orient0["D"])
    composition = composition_report(
        orient["A"], orient2["A"],
        orient["B"], orient2["B"],
        orient["C"], orient2["C"],
        orient["D"], orient2["D"],
    )
    leftover_t_tplus1_composition = composition_report(
        orient0["A"], orient["A"],
        orient0["B"], orient["B"],
        orient0["C"], orient["C"],
        orient0["D"], orient["D"],
    )
    leftover_bits = leftover_bit_composition(reverse, reverse2, face, face2)
    leftover_mo = leftover_mo_composition(
        m1["A"], m2["A"], o1["A"], o2["A"],
        m1["B"], m2["B"], o1["B"], o2["B"],
        m1["C"], m2["C"], o1["C"], o2["C"],
        m1["D"], m2["D"], o1["D"], o2["D"],
    )
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
    two_m1, two_o1 = probe_sides(PROBES, two_ticks, two_locks, two_seeds)
    two_orient = {
        name: frame_orient(two_m1[name], two_o1[name]) for name in ("A", "B", "C", "D")
    }
    two_reverse = reverse_report(two_orient["A"], two_orient["B"])
    two_face = face_report(two_orient["C"], two_orient["D"])
    one_m1, one_o1 = probe_sides(PROBES, one_ticks, one_locks, one_seeds)
    one_cover = {name: axis_cover(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_split = {name: axis_split(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")}
    one_orient = {
        name: frame_orient(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")
    }
    one_cover_face = pair_bit(one_cover["C"], one_cover["D"])
    one_split_face = pair_bit(one_split["C"], one_split["D"])
    one_orient_face = face_report(one_orient["C"], one_orient["D"])
    print(f"Orient reverse tau1={reverse} tau2={reverse2}")
    print(f"Orient face tau1={face} tau2={face2}")
    print(f"Orient composition={composition}")
    print(f"split reverse={split_reverse} face={split_face}")
    print(f"cover reverse={cover_reverse} face={cover_face}")
    print(
        "per_element: unique signed incoming letter and cyclic next/prev "
        "lex-largest outgoing letters of Axis(M) at a probe's t+1 and t+2"
    )
    print("per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four Orient reports at t+1 and t+2, reverse/face at each cut, composition")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    second_pair_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    ) and all(ticks.get(add(PAIR2, step)) != 1 for step in (E2, NEG_E2))
    third_pair_parallel_blocked = (
        not perpendicular(E3, E3)
        and E3 not in locks.get(add(PAIR3, E3), set())
        and NEG_E3 not in locks.get(add(PAIR3, NEG_E3), set())
        and E3 not in locks.get(add(PAIR3B, E3), set())
        and NEG_E3 not in locks.get(add(PAIR3B, NEG_E3), set())
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and second_pair_parallel_blocked
        and third_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 0
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1
        and ticks[PAIR3] == 0
        and ticks[PAIR3B] == 0
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
        "theorem1-M-O-split-at-tau1",
        m1["A"] == frozenset({E2})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E3})
        and m1["D"] == frozenset({E1})
        and o1["A"] == frozenset({E1, NEG_E1, E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, NEG_E2})
        and o1["D"] == frozenset({NEG_E2, E3, NEG_E3})
        and all(split[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(cover[name] == "hold" for name in ("A", "B", "C", "D")),
        str({name: (lockset_display(m1[name]), split[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Orient-at-tau1",
        signed_m["A"] == E2
        and signed_m["B"] == E1
        and signed_m["C"] == E3
        and signed_m["D"] == E1
        and index["A"] == 2
        and index["B"] == 1
        and index["C"] == 3
        and index["D"] == 1
        and cyclic_plane["A"] == (E3, NEG_E1)
        and cyclic_plane["B"] == (E2, NEG_E3)
        and cyclic_plane["C"] == (NEG_E1, NEG_E2)
        and cyclic_plane["D"] == (NEG_E2, NEG_E3)
        and unique_plane["A"] == "fail"
        and unique_plane["B"] == "fail"
        and unique_plane["C"] == "fail"
        and unique_plane["D"] == "fail"
        and det["A"] == -1
        and det["B"] == -1
        and det["C"] == 1
        and det["D"] == 1
        and orient["A"] == -1
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["D"] == 1
        and plane["A"] == (E1, E3)
        and pair["A"] == E1,
        str({name: orient_display(orient[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-O-Orient-at-tau2",
        m2["A"] == m1["A"]
        and m2["B"] == m1["B"]
        and m2["C"] == m1["C"]
        and m2["D"] == m1["D"]
        and o2["A"] == o1["A"]
        and o2["B"] == o1["B"]
        and o2["C"] == o1["C"]
        and o2["D"] == o1["D"]
        and all(split2[name] == "hold" for name in ("A", "B", "C", "D"))
        and signed_m2["A"] == signed_m["A"]
        and index2["A"] == index["A"]
        and cyclic_plane2["A"] == cyclic_plane["A"]
        and cyclic_plane2["B"] == cyclic_plane["B"]
        and cyclic_plane2["C"] == cyclic_plane["C"]
        and cyclic_plane2["D"] == cyclic_plane["D"]
        and det2["A"] == det["A"]
        and det2["B"] == det["B"]
        and det2["C"] == det["C"]
        and det2["D"] == det["D"]
        and orient2["A"] == -1
        and orient2["B"] == -1
        and orient2["C"] == 1
        and orient2["D"] == 1
        and orient2["A"] == orient["A"]
        and orient2["B"] == orient["B"]
        and orient2["C"] == orient["C"]
        and orient2["D"] == orient["D"],
        str({name: orient_display(orient2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "do-not-score-tau-t",
        all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(orient0[name] == "fail" for name in ("A", "B", "C", "D"))
        and all(split0[name] == "fail" for name in ("A", "B", "C", "D"))
        and reverse0 == "fail"
        and face0 == "fail"
        and leftover_t_tplus1_composition == "fail"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "theorem1-mixed-O-cyclic-not-unique",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(m1["A"]) == frozenset({E2})
        and unique_plane["A"] == "fail"
        and unique_signed["A"] == "fail"
        and cyclic_plane["A"] == (E3, NEG_E1)
        and lex_largest_on_axis(o1["A"], E1) == NEG_E1
        and unique_o_orient_a == UNDEFINED
        and orient["A"] == -1
        and orient["A"] != UNDEFINED,
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(frame_orient(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((1, 0, 1), (-1, 0, 1), (0, 0, 2))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new_meet["D"] == ((1, -1, 1), (1, 0, 2), (1, 0, 0))
        and new_meet2["A"] == ((0, -1, 1),)
        and new_meet2["B"] == ()
        and new_meet2["C"] == ()
        and new_meet2["D"] == (),
        str({name: (new_meet[name], new_meet2[name]) for name in ("A", "B", "C", "D")}),
    )
    child_of_a_tplus2 = (0, -1, 1)
    checks.check(
        "theorem1-new-tplus2-neighbor-does-not-enter-O",
        child_of_a_tplus2 in new_meet2["A"]
        and ticks[child_of_a_tplus2] == ticks[PROBES["A"]] + 2
        and incoming_set(child_of_a_tplus2, tau2["A"], ticks, locks, seed_map)
        == frozenset({E3})
        and NEG_E2 not in o2["A"]
        and o2["A"] == o1["A"]
        and orient2["A"] == orient["A"],
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and m1["A"] == frozenset({E2})
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {NEG_E2},
    )
    checks.check(
        "theorem2-reverse-tau1-and-tau2-hold",
        reverse == "hold"
        and reverse2 == "hold"
        and orient["A"] == -1
        and orient["B"] == -1
        and orient2["A"] == -1
        and orient2["B"] == -1
        and reverse != UNDEFINED
        and reverse2 != "fail"
        and split_reverse == "hold"
        and cover_reverse == "hold",
    )
    checks.check(
        "theorem2-face-tau1-and-tau2-hold",
        face == "hold"
        and face2 == "hold"
        and orient["C"] == 1
        and orient["D"] == 1
        and orient2["C"] == 1
        and orient2["D"] == 1
        and face != UNDEFINED
        and face != "fail"
        and split_face == "hold"
        and cover_face == "hold",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and leftover_mo == "hold"
        and leftover_bits == "hold"
        and leftover_t_tplus1_composition == "fail"
        and leftover_t_tplus1_composition != composition
        and orient["A"] == orient2["A"]
        and orient["B"] == orient2["B"]
        and orient["C"] == orient2["C"]
        and orient["D"] == orient2["D"],
        composition,
    )
    checks.check(
        "cover-and-split-do-not-score-handedness",
        split_reverse == "hold"
        and cover_reverse == "hold"
        and reverse == "hold"
        and split_face == "hold"
        and cover_face == "hold"
        and face == "hold"
        and orient["A"] == -1
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["D"] == 1
        and leftover_pair["A"] == -1
        and leftover_pair["B"] == -1
        and leftover_pair["C"] == 1
        and leftover_pair["D"] == -1
        and reverse_report(leftover_pair["A"], leftover_pair["B"]) == "hold"
        and face_report(leftover_pair["C"], leftover_pair["D"]) == "fail"
        and face_report(leftover_pair["C"], leftover_pair["D"]) != face
        and reverse2 == "hold"
        and face2 == "hold",
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
        "empty-Oi-is-orient-fail-not-undefined",
        cyclic_next_prev_plane(frozenset({E2}), frozenset()) == "fail"
        and cyclic_next_prev_plane(frozenset({E2}), frozenset({E1})) == "fail"
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
        and leftover_reverse != reverse
        and leftover_face != face
        and all(lx[name] == frozenset() for name in ("A", "B", "C", "D"))
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and leftover_axis(frozenset({E2}), frozenset({E1, E3})) == frozenset()
        and leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_reverse != UNDEFINED,
    )
    checks.check(
        "mutation-leftover-of-M-or-O-alone-differs",
        lx_m["A"] == frozenset({E1, E3})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_o["A"] == frozenset({E2})
        and lx_o["B"] == frozenset({E1})
        and reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and reverse == "hold"
        and face == "hold"
        and face_m_alone != face
        and reverse_m_alone != reverse
        and lx_m["A"] != lx["A"],
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "hold"
        and o_exist_face == "fail"
        and reverse == "hold"
        and face == "hold"
        and o_exist_reverse == reverse
        and o_exist_face != face
        and pair_present["A"] == "hold"
        and pair_present["B"] == "hold"
        and pair_present["C"] == "hold"
        and pair_present["D"] == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) == "hold"
        and pair_bit(pair_present["A"], pair_present["B"]) == reverse,
    )
    checks.check(
        "mutation-unsigned-incoming-axis-agrees-here",
        unsigned_orient["A"] == -1
        and unsigned_orient["B"] == -1
        and unsigned_orient["C"] == 1
        and unsigned_orient["D"] == 1
        and frame_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == -1
        and unsigned_incoming_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == 1
        and frame_orient(frozenset({NEG_E2}), o1["A"]) == 1
        and unsigned_incoming_orient(frozenset({NEG_E2}), o1["A"]) == -1
        and orient["A"] == -1,
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
        and unique_letter(o2["A"]) == UNDEFINED
        and orient["A"] == -1
        and orient["D"] == 1
        and orient["A"] != UNDEFINED,
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["A"], frozenset)
        and sum_of_set(m1["A"]) == E2
        and sum_of_set(o1["A"]) == E3
        and axis_o["A"] == frozenset({E1, E3})
        and pair["A"] == E1
        and leftover["A"] == E3
        and leftover["B"] == E2
        and cyclic_plane["A"] == (E3, NEG_E1)
        and cyclic_plane["B"] == (E2, NEG_E3)
        and plane["A"] == (E1, E3),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E2 in m1["A"]
        and E2 not in o1["A"]
        and o1["A"] != m1["A"]
        and o2["A"] != m2["A"],
    )
    checks.check(
        "second-and-third-pair-are-seeds-not-formed-children",
        PAIR2 in seed_map
        and seed_map[PAIR2] == NEG_E2
        and ticks[PAIR2] == 0
        and E3 in seed_map
        and seed_map[E3] == E2
        and ticks[E3] == 0
        and PAIR3 in seed_map
        and seed_map[PAIR3] == E3
        and ticks[PAIR3] == 0
        and PAIR3B in seed_map
        and seed_map[PAIR3B] == NEG_E3
        and ticks[PAIR3B] == 0
        and two_ticks[PAIR3] == 1
        and two_locks[PAIR3] == {NEG_E3}
        and two_ticks[PAIR3B] == 1
        and two_locks[PAIR3B] == {NEG_E3}
        and one_ticks[E3] == 1
        and PAIR2 not in new_meet["A"],
    )
    y_m1, y_o1 = probe_sides_at(Y_PROBES, ticks, locks, seed_map, 1)
    y_m2, y_o2 = probe_sides_at(Y_PROBES, ticks, locks, seed_map, 2)
    y_split = {name: axis_split(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient = {name: frame_orient(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient2 = {name: frame_orient(y_m2[name], y_o2[name]) for name in ("A", "B", "C", "D")}
    y_reverse = reverse_report(y_orient["A"], y_orient["B"])
    y_face = face_report(y_orient["C"], y_orient["D"])
    x_m1, x_o1 = probe_sides_at(X_PROBES, ticks, locks, seed_map, 1)
    x_orient = {name: frame_orient(x_m1[name], x_o1[name]) for name in ("A", "B", "C", "D")}
    x_reverse = reverse_report(x_orient["A"], x_orient["B"])
    x_face = face_report(x_orient["C"], x_orient["D"])
    perp_m1, perp_o1 = probe_sides(PROBES, perp_ticks, perp_locks, perp_seeds)
    same_m_a = incoming_set(
        PROBES["A"], same_ticks[PROBES["A"]] + 1, same_ticks, same_locks, same_seeds
    )
    zsym_m1, _zsym_o1 = probe_sides(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    checks.check(
        "not-x-probes-or-y-probes-or-z-symmetric-or-perp",
        THREE_AXIS_SEEDS != PERP_SEEDS
        and THREE_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and THREE_AXIS_SEEDS != TWO_AXIS_SEEDS
        and probe_sites != x_probe_sites
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
        and y_orient2["A"] == y_orient["A"]
        and x_reverse == "fail"
        and x_face == "fail"
        and X_PROBES["C"] == (2, 0, 0)
        and X_PROBES["C"] != PAIR3
        and X_PROBES["C"] not in seed_map
        and PAIR3 in seed_map
        and x_orient["C"] == 1
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and reverse == "hold"
        and face == "hold"
        and y_reverse != reverse,
    )
    checks.check(
        "not-same-lock-or-one-axis-or-y-symmetric-seed",
        THREE_AXIS_SEEDS != SAME_LOCK_SEEDS
        and THREE_AXIS_SEEDS != TWO_SITE_SEEDS
        and THREE_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and THREE_AXIS_SEEDS != TWO_AXIS_SEEDS
        and same_m_a != m1["A"]
        and sum(time == 0 for time in ticks.values()) == 6
        and sum(time == 0 for time in two_ticks.values()) == 4
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
        and "M(A, τ1) = {+e_2}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_3}" in note
        and "M(D, τ1) = {+e_1}" in note
        and "O(A, τ1) = {+e_1, −e_1, +e_3}" in note
        and "O(B, τ1) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ1) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ1) = {−e_2, +e_3, −e_3}" in note
        and "split(A, τ1) = hold" in note
        and "split(B, τ1) = hold" in note
        and "split(C, τ1) = hold" in note
        and "split(D, τ1) = hold" in note
        and "m(A, τ1) = +e_2" in note
        and "i(A, τ1) = 2" in note
        and "o_next(A, τ1) = +e_3" in note
        and "o_prev(A, τ1) = −e_1" in note
        and "det(A, τ1) = -1" in note
        and "Orient(A, τ1) = −1" in note
        and "m(B, τ1) = +e_1" in note
        and "i(B, τ1) = 1" in note
        and "o_next(B, τ1) = +e_2" in note
        and "o_prev(B, τ1) = −e_3" in note
        and "det(B, τ1) = -1" in note
        and "Orient(B, τ1) = −1" in note
        and "m(C, τ1) = +e_3" in note
        and "i(C, τ1) = 3" in note
        and "o_next(C, τ1) = −e_1" in note
        and "o_prev(C, τ1) = −e_2" in note
        and "det(C, τ1) = 1" in note
        and "Orient(C, τ1) = +1" in note
        and "m(D, τ1) = +e_1" in note
        and "i(D, τ1) = 1" in note
        and "o_next(D, τ1) = −e_2" in note
        and "o_prev(D, τ1) = −e_3" in note
        and "det(D, τ1) = 1" in note
        and "Orient(D, τ1) = +1" in note
        and "M(A, τ2) = {+e_2}" in note
        and "M(B, τ2) = {+e_1}" in note
        and "M(C, τ2) = {+e_3}" in note
        and "M(D, τ2) = {+e_1}" in note
        and "O(A, τ2) = {+e_1, −e_1, +e_3}" in note
        and "O(B, τ2) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ2) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ2) = {−e_2, +e_3, −e_3}" in note
        and "Orient(A, τ2) = −1" in note
        and "Orient(B, τ2) = −1" in note
        and "Orient(C, τ2) = +1" in note
        and "Orient(D, τ2) = +1" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)"
        in note
        and "new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)" in note
        and "new 6-NN of A at t(A)+2: (0, -1, 1)" in note
        and "new 6-NN of B at t(B)+2: none" in note
        and "new 6-NN of C at t(C)+2: none" in note
        and "new 6-NN of D at t(D)+2: none" in note,
    )
    checks.check(
        "note-reports-orient-reverse-face-composition",
        "Reverse oriented frame at τ1: hold" in note
        and "Reverse oriented frame at τ2: hold" in note
        and "Face oriented frame at τ1: hold" in note
        and "Face oriented frame at τ2: hold" in note
        and "Composition of Orient: hold" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-split-or-sim-freeze",
        "Cover and split do not score handedness" in note
        and "not leftover of nm2axz axis-cover" in normalized_note
        and "not leftover of nm2ax12z 1-in 2-out split" in normalized_note
        and "not leftover of nm2chiralz lexicographic" in normalized_note
        and "not leftover of nm2orichz opposite-pair" in normalized_note
        and "not leftover of nm2oridetz unique signed" in normalized_note
        and "not leftover of nm2orionez lex-one" in normalized_note
        and "not leftover of nm2oricyccz" in normalized_note
        and "not leftover of nm2simt2z" in normalized_note
        and "not leftover of cyclic lex-smallest" in normalized_note
        and "O is not M" in note
        and "second pair is a new seed, not a formed child" in normalized_note
        and "third pair is a new seed, not a formed child" in normalized_note,
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
        and "Reverse oriented frame at τ1: hold" in note
        and "Face oriented frame at τ1: hold" in note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "Do not score τ=t" in note
        and "τ1=t+1" in note.replace(" ", "")
        and "τ2=t+2" in note.replace(" ", ""),
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
        '    "docs/THREE_AXIS_FARFACE_OPPOSITE_ZPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "cyclic_next_prev_plane" in defined_fns
        and "lex_smallest_on_axis" in defined_fns
        and "lex_largest_on_axis" in defined_fns
        and "lex_largest_cyclic_orient" in defined_fns
        and "cyclic_lex_smallest_orient" in defined_fns
        and "lex_one_orient" in defined_fns
        and "leftover_pair_orient" in defined_fns
        and "lex_frame_orient" in defined_fns
        and "integer_det_columns" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "composition_report" in defined_fns
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
        "orient-cyclic-lex-largest-not-leftover-or-lex-one",
        reverse == "hold"
        and face == "hold"
        and reverse2 == "hold"
        and face2 == "hold"
        and split_reverse == "hold"
        and cover_reverse == "hold"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and leftover_reverse != reverse
        and leftover_face != face
        and one_orient_face == "fail"
        and two_reverse == "hold"
        and two_face == "hold"
        and two_o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and two_orient["B"] == -1
        and orient["B"] == -1
        and two_ticks[PAIR3] == 1
        and ticks[PAIR3] == 0
        and two_locks[PAIR3] == {NEG_E3}
        and locks[PAIR3] == {E3}
        and lex["A"] == -1
        and lex["B"] == 1
        and lex["C"] == 1
        and lex["D"] == 1
        and lex2["A"] == lex["A"]
        and reverse_report(lex["A"], lex["B"]) == "fail"
        and face_report(lex["C"], lex["D"]) == "hold"
        and lex["B"] != orient["B"]
        and reverse_report(lex["A"], lex["B"]) != reverse
        and lex_one["A"] == -1
        and lex_one["B"] == 1
        and lex_one["C"] == -1
        and lex_one["D"] == -1
        and reverse_report(lex_one["A"], lex_one["B"]) == "fail"
        and face_report(lex_one["C"], lex_one["D"]) == "hold"
        and reverse_report(lex_one["A"], lex_one["B"]) != reverse
        and largest["A"] == -1
        and largest["B"] == -1
        and largest["C"] == 1
        and largest["D"] == 1
        and largest["A"] == orient["A"]
        and largest["C"] == orient["C"]
        and cyclic_small["A"] == 1
        and cyclic_small["B"] == 1
        and cyclic_small["C"] == -1
        and cyclic_small["D"] == -1
        and cyclic_small2["A"] == cyclic_small["A"]
        and reverse_report(cyclic_small["A"], cyclic_small["B"]) == "hold"
        and face_report(cyclic_small["C"], cyclic_small["D"]) == "hold"
        and cyclic_small["A"] != orient["A"]
        and leftover_pair["A"] == -1
        and leftover_pair["B"] == -1
        and leftover_pair["C"] == 1
        and leftover_pair["D"] == -1
        and leftover_pair2["A"] == leftover_pair["A"]
        and leftover_pair["B"] == orient["B"]
        and leftover_pair["D"] != orient["D"]
        and reverse_report(leftover_pair["A"], leftover_pair["B"]) == "hold"
        and face_report(leftover_pair["C"], leftover_pair["D"]) == "fail"
        and unique_signed["A"] == "fail"
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and unique_signed["D"] == "fail"
        and unique_signed2["A"] == unique_signed["A"]
        and reverse_report(unique_signed["A"], unique_signed["B"]) == "fail"
        and face_report(unique_signed["C"], unique_signed["D"]) == "fail"
        and face_report(unique_signed["C"], unique_signed["D"]) != face
        and reverse_report(unique_signed["A"], unique_signed["B"]) != reverse
        and o_exist_reverse == "hold"
        and o_exist_face == "fail"
        and leftover_mo == "hold"
        and leftover_bits == "hold",
    )
    _ = (
        o0,
        unique_o_orient_a,
        one_cover_face,
        one_split_face,
        unsigned_orient,
        perp_o1,
        largest_plane,
        x_o1,
        unique_plane2,
        lex_one2,
        largest2,
        leftover_bits,
        cover2,
        two_m1,
        cyclic_small2,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
