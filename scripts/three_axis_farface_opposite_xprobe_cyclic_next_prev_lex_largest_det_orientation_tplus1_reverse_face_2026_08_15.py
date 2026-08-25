#!/usr/bin/env python3
"""Cyclic next/prev lex-largest outgoing det orientation at t+1.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is three disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2, (0,0,-1) locks +e_3, (0,1,-1) locks
-e_3. The third pair is a new seed, not a formed child, and sits on the -z
face opposite the z-probes. x-probes as nm2axx. Orient as nm2oricyclz.
Perp-step incoming lock. Unformed => UNDEFINED. Split HOLDs iff cover HOLDs
and |Axis(M)|=1. Split HOLD required. When split HOLDs, m is unique in M.
Let i in {1,2,3} be the axis index of m. e_next = e_{i+1} with 3+1 -> 1.
e_prev = e_{i-1} with 1-1 -> 3. O_next = O intersect {+/- e_next}. O_prev
= O intersect {+/- e_prev}. If either empty, Orient fails, not UNDEFINED.
Order +e < -e. o_next is the lex-largest vector in O_next (hence -e if both
signs). o_prev likewise. Orient is the sign of the integer determinant of
columns (m, o_next, o_prev). If split fails, Orient fails, not UNDEFINED.
Reverse HOLDs iff Orient(A)=Orient(B) both +/-1. Face on C,D. Uniqueness of
O is not required. Occupancy of sites is not used. No larger host.
Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THREE_AXIS_FARFACE_OPPOSITE_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/THREE_AXIS_FARFACE_OPPOSITE_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
AxisSet = frozenset[Point] | str
OrientVal = int | str
SlotVal = Point | str
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
NEAR_A: Point = (2, 0, 0)
NEAR_B: Point = (2, 1, 0)
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
NEAR_THREE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
    (NEAR_A, E3),
    (NEAR_B, NEG_E3),
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
PROBES = {
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
    "Cyclic lex-largest orientation of the 1-in 2-out frame at t+1 on the "
    "four x-probes of the three-axis far-face opposite seed, and reverse/face "
    "from that, are reported. Displayed, not adopted."
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


def negate(lock: Point) -> Point:
    return (-lock[0], -lock[1], -lock[2])


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


def slot_display(value: SlotVal) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if isinstance(value, tuple) and value in LOCK_NAME:
        return LOCK_NAME[value]
    raise TypeError(f"slot is not a lock or fail: {value!r}")


def index_display(value: int | str) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if isinstance(value, int):
        return str(value)
    raise TypeError(f"axis index is not an index or fail: {value!r}")


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


def sign_of_det(det: int) -> OrientVal:
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


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


def axis_index_of(lock: Point) -> int:
    axis = axis_of_letter(lock)
    if axis not in AXIS_INDEX:
        raise ValueError(f"lock is not a six-neighbor step: {lock!r}")
    return AXIS_INDEX[axis]


def cyclic_next_prev(index: int) -> tuple[Point, Point]:
    """e_next = e_{i+1} with 3+1->1; e_prev = e_{i-1} with 1-1->3."""
    if index not in (1, 2, 3):
        raise ValueError(f"axis index is not in {{1,2,3}}: {index!r}")
    next_index = 1 if index == 3 else index + 1
    prev_index = 3 if index == 1 else index - 1
    return AXES[next_index - 1], AXES[prev_index - 1]


def axis_slot(outgoing: Outgoing, axis: Point) -> Incoming:
    """O intersect {+/- axis}. UNDEFINED if O is unformed."""
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    return frozenset(outgoing & {axis, negate(axis)})


def lex_largest_signed(slot: Incoming) -> SlotVal:
    """Lex-largest under +e < -e. Empty is fail. Hence -e if both signs."""
    if slot == UNDEFINED:
        return UNDEFINED
    if not isinstance(slot, frozenset) or not slot:
        return "fail"
    axis = axis_of_letter(next(iter(slot)))
    negative = negate(axis)
    if negative in slot:
        return negative
    if axis in slot:
        return axis
    return "fail"


def lex_smallest_signed(slot: Incoming) -> SlotVal:
    """Lex-smallest under +e < -e. Mutation: +e if both signs. Not this letter."""
    if slot == UNDEFINED:
        return UNDEFINED
    if not isinstance(slot, frozenset) or not slot:
        return "fail"
    axis = axis_of_letter(next(iter(slot)))
    negative = negate(axis)
    if axis in slot:
        return axis
    if negative in slot:
        return negative
    return "fail"


def cyclic_index(incoming: Incoming) -> int | str:
    """Axis index i of unique m. Fail if M is not a singleton."""
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    return axis_index_of(signed_m)


def cyclic_slots(
    incoming: Incoming,
    outgoing: Outgoing,
    *,
    largest: bool = True,
) -> tuple[int | str, SlotVal, SlotVal]:
    """i, o_next, o_prev from unique m and lex choice on cyclic O slots."""
    index = cyclic_index(incoming)
    if index == UNDEFINED:
        return UNDEFINED, UNDEFINED, UNDEFINED
    if index == "fail" or not isinstance(index, int):
        return "fail", "fail", "fail"
    e_next, e_prev = cyclic_next_prev(index)
    picker = lex_largest_signed if largest else lex_smallest_signed
    o_next = picker(axis_slot(outgoing, e_next))
    o_prev = picker(axis_slot(outgoing, e_prev))
    return index, o_next, o_prev


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
        occupied = outgoing & {axis, negate(axis)}
        if len(occupied) != 1:
            return "fail"
        picked.append(next(iter(occupied)))
    return picked[0], picked[1]


def lex_signed_outgoing_plane(outgoing: Outgoing) -> tuple[Point, Point] | str:
    """Lex-smallest signed letter per Axis(O) under +e_i < -e_i. Not cyclic."""
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
        occupied = outgoing & {axis, negate(axis)}
        if not occupied:
            return "fail"
        if axis in occupied:
            picked.append(axis)
        else:
            picked.append(negate(axis))
    return picked[0], picked[1]


def opposite_pair_unit(outgoing: Outgoing) -> Point | str:
    """Positive unit of the smallest-index axis with both e and -e in O."""
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    for axis in AXES:
        if axis in outgoing and negate(axis) in outgoing:
            return axis
    return "fail"


def leftover_axis_unit(signed_m: Point, pair_unit: Point) -> Point | str:
    """Unique Axis not in {axis(m), axis(e_pair)}, oriented as the unit +l."""
    occupied = {axis_of_letter(signed_m), axis_of_letter(pair_unit)}
    leftover = tuple(axis for axis in AXES if axis not in occupied)
    if len(leftover) != 1:
        return "fail"
    return leftover[0]


def leftover_signed(outgoing: Outgoing, leftover_ax: Point) -> Point | str:
    """Unique signed O vector on leftover axis. Fail if |O_l| != 1."""
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    occupied = outgoing & {leftover_ax, negate(leftover_ax)}
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


def det_orient(col1: Point, col2: Point, col3: Point) -> OrientVal:
    return sign_of_det(integer_det_columns(col1, col2, col3))


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
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    plane = outgoing_plane(axis_set(outgoing))
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return det_orient(signed_m, plane[0], plane[1])


def leftover_pair_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: sign of det(m, e_pair, o_l). Not this letter."""
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
    leftover_ax = leftover_axis_unit(signed_m, pair)
    if leftover_ax == "fail" or not isinstance(leftover_ax, tuple):
        return "fail"
    leftover = leftover_signed(outgoing, leftover_ax)
    if leftover == UNDEFINED:
        return UNDEFINED
    if leftover == "fail" or not isinstance(leftover, tuple):
        return "fail"
    return det_orient(signed_m, pair, leftover)


def unsigned_leftover_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: sign of det(m, e, +l). Unsigned leftover unit. Not this letter."""
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
    leftover = leftover_axis_unit(signed_m, pair)
    if leftover == "fail" or not isinstance(leftover, tuple):
        return "fail"
    return det_orient(signed_m, pair, leftover)


def lex_one_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: lex-one signed O_i in axis order, not cyclic next/prev."""
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
    plane = lex_signed_outgoing_plane(outgoing)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return det_orient(signed_m, plane[0], plane[1])


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
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    plane = unique_signed_outgoing_plane(outgoing)
    if plane == UNDEFINED:
        return UNDEFINED
    if plane == "fail" or not isinstance(plane, tuple):
        return "fail"
    return det_orient(signed_m, plane[0], plane[1])


def lex_smallest_cyclic_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: cyclic next/prev with lex-smallest. Not this letter."""
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
    _index, o_next, o_prev = cyclic_slots(incoming, outgoing, largest=False)
    if o_next == UNDEFINED or o_prev == UNDEFINED:
        return UNDEFINED
    if not isinstance(o_next, tuple) or not isinstance(o_prev, tuple):
        return "fail"
    return det_orient(signed_m, o_next, o_prev)


def frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Sign of det(m, o_next, o_prev) with lex-largest cyclic slots.

    Fail if split fails or a cyclic slot is empty, not UNDEFINED.
    """
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
    _index, o_next, o_prev = cyclic_slots(incoming, outgoing, largest=True)
    if o_next == UNDEFINED or o_prev == UNDEFINED:
        return UNDEFINED
    if not isinstance(o_next, tuple) or not isinstance(o_prev, tuple):
        return "fail"
    return det_orient(signed_m, o_next, o_prev)


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

    print(
        "cyclic next/prev lex-largest det orientation reverse/face at t+1 "
        "on three-axis far-face opposite x-probes"
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
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    y_probe_sites = tuple(Y_PROBES[name] for name in ("A", "B", "C", "D"))
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
        and add(E3, E2) == PAIR2
        and add(PAIR3, E3) == ORIGIN
        and add(PAIR3, E2) == PAIR3B
        and add(NEAR_A, NEG_E1) == PROBES["A"]
        and add(NEAR_B, NEG_E1) == PROBES["D"]
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and perpendicular(E3, E1)
        and in_ball(PROBES["C"])
        and in_ball(PAIR3)
        and in_ball(PAIR3B)
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "cyclic-next-prev-identity",
        cyclic_next_prev(1) == (E2, E3)
        and cyclic_next_prev(2) == (E3, E1)
        and cyclic_next_prev(3) == (E1, E2)
        and axis_index_of(NEG_E1) == 1
        and axis_index_of(E2) == 2
        and axis_index_of(NEG_E3) == 3
        and lex_largest_signed(frozenset({E2, NEG_E2})) == NEG_E2
        and lex_smallest_signed(frozenset({E2, NEG_E2})) == E2
        and lex_largest_signed(frozenset({E2})) == E2
        and lex_largest_signed(frozenset()) == "fail"
        and lex_largest_signed(frozenset({E3, NEG_E3})) == NEG_E3
        and lex_smallest_signed(frozenset({E3, NEG_E3})) == E3,
    )
    checks.check(
        "det-identity",
        integer_det_columns(NEG_E1, NEG_E2, NEG_E3) == -1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(E3, NEG_E1, NEG_E2) == 1
        and integer_det_columns(NEG_E1, E2, NEG_E3) == 1
        and integer_det_columns(E2, E3, E1) == 1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(NEG_E1, E2, E3) == -1
        and integer_det_columns(E1, E1, E2) == 0,
    )
    checks.check(
        "orient-identity",
        frame_orient(UNDEFINED, frozenset({E2, E3})) == UNDEFINED
        and frame_orient(frozenset({E2}), UNDEFINED) == UNDEFINED
        and frame_orient(frozenset(), frozenset({E1, E3})) == "fail"
        and frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "fail"
        and frame_orient(frozenset({NEG_E1}), frozenset({NEG_E2, NEG_E3})) == -1
        and frame_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == -1
        and frame_orient(frozenset({E1}), frozenset({E2, E3})) == 1
        and frame_orient(frozenset({NEG_E1}), frozenset({E2, E3})) == -1
        and frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == 1
        and frame_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3, NEG_E3})) == 1
        and frame_orient(frozenset({NEG_E1}), frozenset({NEG_E1, E2, NEG_E3}))
        == "fail"
        and frame_orient(frozenset({NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and lex_smallest_cyclic_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2}))
        == -1
        and lex_smallest_cyclic_orient(
            frozenset({E2}), frozenset({E1, NEG_E1, E3, NEG_E3})
        )
        == 1
        and lex_one_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == -1
        and lex_one_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3, NEG_E3}))
        == -1
        and leftover_pair_orient(frozenset({NEG_E1}), frozenset({NEG_E2, NEG_E3}))
        == "fail"
        and leftover_pair_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2}))
        == -1
        and unique_signed_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2}))
        == "fail"
        and unique_signed_orient(frozenset({NEG_E1}), frozenset({NEG_E2, NEG_E3}))
        == -1
        and lex_frame_orient(frozenset({E3}), frozenset({E1, NEG_E1, NEG_E2})) == 1
        and lex_frame_orient(frozenset({NEG_E1}), frozenset({NEG_E2, NEG_E3})) == -1,
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
    two_ticks, two_locks, two_seeds = form(TWO_AXIS_SEEDS)
    near_ticks, near_locks, near_seeds = form(NEAR_THREE_AXIS_SEEDS)
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
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
    o_next: dict[str, SlotVal] = {}
    o_prev: dict[str, SlotVal] = {}
    det: dict[str, int | str] = {}
    lex: dict[str, OrientVal] = {}
    lex_small: dict[str, OrientVal] = {}
    lex_one: dict[str, OrientVal] = {}
    leftover: dict[str, OrientVal] = {}
    unique_s: dict[str, OrientVal] = {}
    pair_present: dict[str, str] = {}
    orient: dict[str, OrientVal] = {}
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
        index[name], o_next[name], o_prev[name] = cyclic_slots(m1[name], o1[name])
        if (
            isinstance(signed_m[name], tuple)
            and isinstance(o_next[name], tuple)
            and isinstance(o_prev[name], tuple)
        ):
            det[name] = integer_det_columns(
                signed_m[name], o_next[name], o_prev[name]
            )
        else:
            det[name] = "fail"
        pair_present[name] = has_opposite_pair(o1[name])
        lex[name] = lex_frame_orient(m1[name], o1[name])
        lex_small[name] = lex_smallest_cyclic_orient(m1[name], o1[name])
        lex_one[name] = lex_one_orient(m1[name], o1[name])
        leftover[name] = leftover_pair_orient(m1[name], o1[name])
        unique_s[name] = unique_signed_orient(m1[name], o1[name])
        orient[name] = frame_orient(m1[name], o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"split={split[name]} "
            f"i={index_display(index[name])} "
            f"o_next={slot_display(o_next[name])} "
            f"o_prev={slot_display(o_prev[name])} "
            f"det={det[name]} "
            f"Orient={orient_display(orient[name])}"
        )

    reverse = reverse_report(orient["A"], orient["B"])
    face = face_report(orient["C"], orient["D"])
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
    unique_o_orient_a = frame_orient(unique_letter(m1["A"]), unique_letter(o1["A"]))
    two_m1, two_o1 = probe_sides(PROBES, two_ticks, two_locks, two_seeds)
    two_orient = {
        name: frame_orient(two_m1[name], two_o1[name]) for name in ("A", "B", "C", "D")
    }
    near_m1, near_o1 = probe_sides(PROBES, near_ticks, near_locks, near_seeds)
    near_orient = {
        name: frame_orient(near_m1[name], near_o1[name]) for name in ("A", "B", "C", "D")
    }
    near_orient_reverse = reverse_report(near_orient["A"], near_orient["B"])
    near_orient_face = face_report(near_orient["C"], near_orient["D"])
    two_lex_small = {
        name: lex_smallest_cyclic_orient(two_m1[name], two_o1[name])
        for name in ("A", "B", "C", "D")
    }
    two_orient_reverse = reverse_report(two_orient["A"], two_orient["B"])
    two_orient_face = face_report(two_orient["C"], two_orient["D"])
    one_m1, one_o1 = probe_sides(PROBES, one_ticks, one_locks, one_seeds)
    one_cover = {
        name: axis_cover(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")
    }
    one_split = {
        name: axis_split(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")
    }
    one_orient = {
        name: frame_orient(one_m1[name], one_o1[name]) for name in ("A", "B", "C", "D")
    }
    one_cover_face = pair_bit(one_cover["C"], one_cover["D"])
    one_split_face = pair_bit(one_split["C"], one_split["D"])
    one_orient_face = face_report(one_orient["C"], one_orient["D"])
    one_orient_reverse = reverse_report(one_orient["A"], one_orient["B"])
    print(f"Orient reverse={reverse} face={face}")
    print(f"split reverse={split_reverse} face={split_face}")
    print(f"cover reverse={cover_reverse} face={cover_face}")
    print(
        "per_element: unique signed incoming letter, cyclic next/prev axes of "
        "Axis(M), lex-largest signed O vector on each cyclic slot at a probe's t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four Orient reports, reverse/face from equal +/-1 signs")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_lock_blocks_own_axis = not perpendicular(E1, E1) and not perpendicular(
        E1, NEG_E1
    )
    second_pair_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    ) and all(ticks.get(add(PAIR2, step)) != 1 for step in (E2, NEG_E2))
    third_pair_parallel_blocked = all(
        ticks.get(add(PAIR3, step)) != 1 for step in (E3, NEG_E3)
    ) and all(ticks.get(add(PAIR3B, step)) != 1 for step in (E3, NEG_E3))
    checks.check(
        "perp-step-incoming-lock",
        origin_lock_blocks_own_axis
        and second_pair_parallel_blocked
        and third_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 0
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
        and ticks[PAIR3] == 0
        and ticks[PAIR3B] == 0
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["A"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["A"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["C"], 2, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["A"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["A"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
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
        ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-O-split",
        m1["A"] == frozenset({E3, NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({E3, NEG_E3})
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
        str(
            {
                name: (lockset_display(m1[name]), split[name])
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-Orient",
        signed_m["A"] == "fail"
        and signed_m["B"] == E1
        and signed_m["C"] == E1
        and signed_m["D"] == "fail"
        and index["A"] == "fail"
        and index["B"] == 1
        and index["C"] == 1
        and index["D"] == "fail"
        and o_next["A"] == "fail"
        and o_prev["A"] == "fail"
        and o_next["B"] == E2
        and o_prev["B"] == NEG_E3
        and o_next["C"] == NEG_E2
        and o_prev["C"] == NEG_E3
        and o_next["D"] == "fail"
        and o_prev["D"] == "fail"
        and det["A"] == "fail"
        and det["B"] == -1
        and det["C"] == 1
        and det["D"] == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["D"] == "fail",
        str({name: orient_display(orient[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-mixed-O-lex-largest-slot",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_letter(m1["A"]) == UNDEFINED
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_o_orient_a == UNDEFINED
        and o_prev["B"] == NEG_E3
        and orient["A"] == "fail"
        and unique_s["A"] == "fail"
        and unique_s["B"] == "fail"
        and unique_s["C"] == "fail",
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
        and frame_orient(m0["A"], o0["A"]) == "fail"
        and frame_orient(m0["B"], o0["B"]) == "fail"
        and frame_orient(m0["C"], o0["C"]) == "fail"
        and frame_orient(m0["D"], o0["D"]) == "fail"
        and axis_cover(m0["D"], o0["D"]) == "fail",
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0),)
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet["D"] == ((2, 1, 0),)
        and ticks[PROBES["C"]] == 3
        and PROBES["C"] in new_meet["A"],
        str(new_meet),
    )
    checks.check(
        "theorem1-C-is-formed-child-not-seed",
        PROBES["C"] == NEAR_A
        and PROBES["C"] not in seed_map
        and ticks[PROBES["C"]] == 3
        and locks[PROBES["C"]] == {E1}
        and m1["C"] == frozenset({E1})
        and PROBES["A"] not in seed_map
        and ticks[PROBES["A"]] == 2
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {NEG_E2}
        and ticks[PAIR3] == 0
        and locks[PAIR3] == {E3}
        and ticks[PAIR3B] == 0
        and locks[PAIR3B] == {NEG_E3}
        and PROBES["D"] not in seed_map
        and NEAR_A in near_seeds
        and near_ticks[PROBES["C"]] == 0,
    )
    checks.check(
        "theorem2-reverse-orient-fail",
        reverse == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and reverse != UNDEFINED
        and reverse != "hold"
        and split_reverse == "fail"
        and cover_reverse == "fail",
    )
    checks.check(
        "theorem3-face-orient-fail",
        face == "fail"
        and orient["C"] == 1
        and orient["D"] == "fail"
        and face != UNDEFINED
        and face != "hold"
        and split_face == "fail"
        and cover_face == "fail",
    )
    checks.check(
        "cover-and-split-do-not-score-handedness",
        split_reverse == "fail"
        and cover_reverse == "fail"
        and reverse == "fail"
        and split_face == "fail"
        and cover_face == "fail"
        and face == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and lex["A"] == "fail"
        and lex["B"] == 1
        and reverse_report(lex["A"], lex["B"]) == "fail"
        and lex["B"] != orient["B"],
    )
    checks.check(
        "split-fail-is-orient-fail-not-undefined",
        frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold"
        and two_one["A"] == "fail"
        and two_one["C"] == "fail"
        and two_one["D"] == "fail"
        and one_orient["C"] == 1
        and one_split["C"] == "hold"
        and one_cover["C"] == "hold"
        and one_orient["D"] == "fail"
        and one_split["D"] == "fail"
        and one_cover["D"] == "hold"
        and one_orient_face == "fail"
        and one_split_face == "fail"
        and one_cover_face == "hold"
        and o_prev["D"] == "fail"
        and o_next["D"] == "fail"
        and split["D"] == "fail"
        and cover["D"] == "fail"
        and axis_m["D"] == frozenset({E3})
        and axis_o["D"] == frozenset({E1})
        and det["D"] == "fail"
        and orient["D"] == "fail"
        and orient["D"] != UNDEFINED
        and orient["A"] == "fail"
        and orient["A"] != UNDEFINED,
    )
    checks.check(
        "empty-cyclic-slot-is-orient-fail-not-undefined",
        lex_largest_signed(frozenset()) == "fail"
        and frame_orient(frozenset({NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and cyclic_slots(frozenset({NEG_E3}), frozenset({E1, NEG_E1}))[2] == "fail"
        and leftover_axis(frozenset({NEG_E3}), frozenset({E1, NEG_E1}))
        == frozenset({E2})
        and frame_orient(m1["A"], o1["A"]) == "fail"
        and frame_orient(m1["D"], o1["D"]) == "fail"
        and split["A"] == "fail"
        and split["D"] == "fail"
        and leftover_axis(m1["A"], o1["A"]) == frozenset({E2})
        and leftover_axis(m1["D"], o1["D"]) == frozenset({E2}),
    )
    checks.check(
        "not-leftover-of-1-axis-cover-face-hold",
        one_ticks[PROBES["A"]] == 3
        and one_ticks[PROBES["B"]] == 2
        and one_ticks[PROBES["C"]] == 4
        and one_ticks[PROBES["D"]] == 3
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
        and two_ticks[PROBES["A"]] == 2
        and two_ticks[PROBES["C"]] == 3
        and two_ticks[PROBES["D"]] == 2
        and near_ticks[PROBES["A"]] == 1
        and near_ticks[PROBES["C"]] == 0
        and one_orient["A"] == "fail"
        and one_orient["B"] == -1
        and one_orient_reverse == "fail"
        and one_orient["D"] == "fail"
        and one_orient_face == "fail"
        and one_cover_face == "hold"
        and cover_face == "fail"
        and one_cover_face != cover_face
        and one_m1["D"] != m1["D"]
        and two_m1["A"] != m1["A"]
        and two_m1["A"] == frozenset({NEG_E3})
        and m1["A"] == frozenset({E3, NEG_E3})
        and two_orient_reverse == "fail"
        and reverse == "fail"
        and one_orient["A"] == orient["A"]
        and lex_smallest_cyclic_orient(one_m1["A"], one_o1["A"]) == "fail"
        and lex_small["A"] == "fail"
        and near_orient["A"] == -1
        and near_orient["A"] != orient["A"]
        and near_orient_reverse == "fail"
        and near_orient_face == "fail",
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and lx["A"] == frozenset({E2})
        and lx["B"] == frozenset()
        and lx["C"] == frozenset()
        and lx["D"] == frozenset({E2})
        and leftover_reverse == reverse
        and leftover_face == face
        and reverse == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and leftover_axis(frozenset({E1}), frozenset({E2, E3, NEG_E3}))
        == frozenset()
        and leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_match(frozenset({E2}), frozenset()) == "fail",
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
        and two_orient_reverse == "fail"
        and leftover_match(leftover_of_one(two_m1["A"]), leftover_of_one(two_m1["B"]))
        == "fail"
        and lx_m["C"] == frozenset({E2, E3})
        and lx_m["D"] == frozenset({E1, E2})
        and lx_o["D"] == frozenset({E2, E3})
        and lx_o["C"] == frozenset({E1}),
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
        and pair_bit(pair_present["A"], pair_present["B"]) == "fail"
        and pair_bit(pair_present["C"], pair_present["D"]) == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) != face,
    )
    checks.check(
        "mutation-lex-smallest-cyclic-differs",
        lex_small["A"] == "fail"
        and lex_small["B"] == 1
        and lex_small["C"] == -1
        and lex_small["D"] == "fail"
        and reverse_report(lex_small["A"], lex_small["B"]) == "fail"
        and face_report(lex_small["C"], lex_small["D"]) == "fail"
        and reverse == "fail"
        and lex_small["B"] != orient["B"]
        and lex_small["C"] != orient["C"]
        and two_lex_small["B"] == 1
        and two_orient["B"] == -1
        and reverse_report(two_lex_small["A"], two_lex_small["B"]) == "fail"
        and two_orient_reverse == "fail"
        and two_lex_small["B"] != two_orient["B"]
        and o_prev["B"] == NEG_E3
        and lex_smallest_signed(axis_slot(o1["B"], E3)) == E3
        and lex_largest_signed(axis_slot(o1["B"], E3)) == NEG_E3
        and lex_smallest_signed(axis_slot(two_o1["B"], E3)) == E3
        and lex_largest_signed(axis_slot(two_o1["B"], E3)) == NEG_E3,
    )
    checks.check(
        "mutation-lex-one-and-unsigned-plane-differ",
        lex_one["A"] == "fail"
        and lex_one["B"] == 1
        and lex_one["C"] == -1
        and lex_one["D"] == "fail"
        and reverse_report(lex_one["A"], lex_one["B"]) == "fail"
        and lex["A"] == "fail"
        and lex["B"] == 1
        and lex["C"] == 1
        and lex["D"] == "fail"
        and reverse_report(lex["A"], lex["B"]) == "fail"
        and orient["A"] == "fail"
        and orient["B"] == -1
        and orient["C"] == 1
        and lex_one["B"] != orient["B"]
        and lex_one["C"] != orient["C"]
        and lex["B"] != orient["B"]
        and lex["C"] == orient["C"]
        and lex_small["C"] != orient["C"],
    )
    checks.check(
        "mutation-leftover-signed-and-unsigned-differ",
        leftover["A"] == "fail"
        and leftover["B"] == -1
        and leftover["C"] == 1
        and leftover["D"] == "fail"
        and unsigned_leftover_orient(m1["A"], o1["A"]) == "fail"
        and unsigned_leftover_orient(m1["B"], o1["B"]) == -1
        and unsigned_leftover_orient(m1["C"], o1["C"]) == -1
        and unsigned_leftover_orient(m1["D"], o1["D"]) == "fail"
        and leftover["B"] == orient["B"]
        and leftover["C"] == orient["C"]
        and unsigned_leftover_orient(m1["C"], o1["C"]) != orient["C"]
        and reverse_report(leftover["A"], leftover["B"]) == "fail",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == UNDEFINED
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_o_orient_a == UNDEFINED
        and unique_s["B"] == "fail"
        and unique_s["C"] == "fail"
        and unique_s["C"] != orient["C"]
        and unique_s["A"] == "fail"
        and unique_s["B"] != orient["B"]
        and orient["A"] == "fail"
        and orient["B"] == -1
        and orient["B"] != UNDEFINED,
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["B"], frozenset)
        and sum_of_set(m1["A"]) == ZERO
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["B"]) == E2
        and sum_of_set(o1["C"]) == NEG_E2
        and sum_of_set(o1["D"]) == ZERO
        and axis_o["A"] == frozenset({E1})
        and axis_o["B"] == frozenset({E2, E3})
        and o_next["B"] == E2
        and o_prev["B"] == NEG_E3
        and o_next["C"] == NEG_E2
        and o_prev["C"] == NEG_E3,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E3 in m1["A"]
        and E3 not in o1["A"]
        and E1 in o1["A"]
        and E1 not in m1["A"]
        and o1["A"] != m1["A"],
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
        and one_ticks[E3] == 1
        and two_ticks[PAIR3] == 1
        and two_locks[PAIR3] == {NEG_E3}
        and two_ticks[PAIR3B] == 1
        and two_locks[PAIR3B] == {NEG_E3}
        and PAIR2 not in new_meet["A"]
        and NEAR_B in new_meet["D"]
        and PROBES["C"] not in seed_map,
    )
    z_m1, z_o1 = probe_sides(Z_PROBES, ticks, locks, seed_map)
    z_split = {name: axis_split(z_m1[name], z_o1[name]) for name in ("A", "B", "C", "D")}
    z_orient = {
        name: frame_orient(z_m1[name], z_o1[name]) for name in ("A", "B", "C", "D")
    }
    z_reverse = reverse_report(z_orient["A"], z_orient["B"])
    z_face = face_report(z_orient["C"], z_orient["D"])
    y_m1, y_o1 = probe_sides(Y_PROBES, ticks, locks, seed_map)
    y_orient = {
        name: frame_orient(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")
    }
    y_reverse = reverse_report(y_orient["A"], y_orient["B"])
    y_face = face_report(y_orient["C"], y_orient["D"])
    perp_m1, perp_o1 = probe_sides(PROBES, perp_ticks, perp_locks, perp_seeds)
    same_m_a = incoming_set(
        PROBES["A"], same_ticks[PROBES["A"]] + 1, same_ticks, same_locks, same_seeds
    )
    zsym_m1, _zsym_o1 = probe_sides(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    checks.check(
        "not-y-probes-or-z-probes-or-z-symmetric-or-perp",
        THREE_AXIS_SEEDS != PERP_SEEDS
        and THREE_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and THREE_AXIS_SEEDS != TWO_AXIS_SEEDS
        and probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and z_m1["A"] != m1["A"]
        and z_split["A"] == "hold"
        and z_orient["A"] == -1
        and z_orient["B"] == -1
        and z_orient["C"] == 1
        and z_orient["D"] == 1
        and z_reverse == "hold"
        and z_face == "hold"
        and z_split["D"] == "hold"
        and split["D"] == "fail"
        and y_orient["A"] == 1
        and y_orient["B"] == -1
        and y_orient["C"] == -1
        and y_reverse == "fail"
        and y_face == "fail"
        and ticks[Y_PROBES["A"]] == 0
        and ticks[Y_PROBES["C"]] == 1
        and ticks[Z_PROBES["A"]] == 0
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["C"]] == 3
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and reverse == "fail"
        and face == "fail"
        and z_reverse != reverse
        and z_face != face
        and z_orient["D"] != orient["D"]
        and lex_smallest_cyclic_orient(z_m1["A"], z_o1["A"]) == 1
        and z_orient["A"] != lex_smallest_cyclic_orient(z_m1["A"], z_o1["A"]),
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
        "t(A)=2" in note
        and "t(B)=1" in note
        and "t(C)=3" in note
        and "t(D)=2" in note
        and "M(A, τ) = {+e_3, −e_3}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_1}" in note
        and "M(D, τ) = {+e_3, −e_3}" in note
        and "O(A, τ) = {+e_1}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {−e_2, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_1, −e_1}" in note
        and "split(A) = fail" in note
        and "split(B) = hold" in note
        and "split(C) = hold" in note
        and "split(D) = fail" in note
        and "i(A) = fail" in note
        and "o_next(A) = fail" in note
        and "o_prev(A) = fail" in note
        and "det(A) = fail" in note
        and "Orient(A) = fail" in note
        and "i(B) = 1" in note
        and "o_next(B) = +e_2" in note
        and "o_prev(B) = −e_3" in note
        and "det(B) = -1" in note
        and "Orient(B) = −1" in note
        and "i(C) = 1" in note
        and "o_next(C) = −e_2" in note
        and "o_prev(C) = −e_3" in note
        and "det(C) = 1" in note
        and "Orient(C) = +1" in note
        and "i(D) = fail" in note
        and "o_next(D) = fail" in note
        and "o_prev(D) = fail" in note
        and "det(D) = fail" in note
        and "Orient(D) = fail" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)" in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-orient-reverse-face",
        "Reverse oriented frame at τ: fail" in note
        and "Face oriented frame at τ: fail" in note,
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
        and "not leftover of lexicographic" in normalized_note
        and "not leftover of cyclic lex-smallest" in normalized_note
        and "not leftover of nm2orionex lex-one" in normalized_note
        and "O is not M" in note
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
        and "Reverse oriented frame at τ: fail" in note
        and "Face oriented frame at τ: fail" in note,
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
        all(f"### N{index_n}" in note for index_n in range(1, 9)),
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
        '    "docs/THREE_AXIS_FARFACE_OPPOSITE_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "cyclic_next_prev" in defined_fns
        and "lex_largest_signed" in defined_fns
        and "lex_smallest_cyclic_orient" in defined_fns
        and "integer_det_columns" in defined_fns
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
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["C"]] == 3
        and set(ticks) <= host,
    )
    checks.check(
        "orient-cyclic-lex-largest-not-smallest-or-lex-one",
        reverse == "fail"
        and face == "fail"
        and split_reverse == "fail"
        and cover_reverse == "fail"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and one_orient_face == "fail"
        and two_orient_reverse == "fail"
        and two_ticks[PROBES["A"]] == ticks[PROBES["A"]]
        and two_m1["A"] != m1["A"]
        and near_ticks[PROBES["A"]] != ticks[PROBES["A"]]
        and lex_small["A"] == "fail"
        and lex_small["B"] == 1
        and reverse_report(lex_small["A"], lex_small["B"]) == "fail"
        and lex_one["A"] == "fail"
        and lex_one["B"] == 1
        and lex_one["C"] == -1
        and reverse_report(lex_one["A"], lex_one["B"]) == "fail"
        and lex_one["C"] != orient["C"]
        and lex_small["C"] != orient["C"]
        and lex["A"] == "fail"
        and lex["B"] == 1
        and reverse_report(lex["A"], lex["B"]) == "fail"
        and leftover["A"] == "fail"
        and leftover["C"] == 1
        and orient["A"] == "fail"
        and leftover["C"] == orient["C"]
        and unsigned_leftover_orient(m1["C"], o1["C"]) != orient["C"]
        and z_reverse == "hold"
        and z_face == "hold"
        and z_reverse != reverse
        and y_reverse == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and pair_bit(pair_present["A"], pair_present["B"]) == "fail"
        and pair_bit(pair_present["C"], pair_present["D"]) == "hold"
        and pair_bit(pair_present["C"], pair_present["D"]) != face,
    )
    _ = (
        o0,
        unique_o_orient_a,
        one_cover_face,
        one_split_face,
        two_orient_face,
        perp_o1,
        unique_s,
        near_orient_face,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
