#!/usr/bin/env python3
"""Cyclic next/prev lex-largest outgoing determinant orientation at t+1.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin +e_1, (0,1,0) -e_1, (0,0,1) +e_2,
(0,1,1) -e_2. Same process and x-probes as nm2axx. M, O, split as nm2ax12x.
Orient as nm2oricyclz. A 6-NN step is allowed iff it is perpendicular to the
parent lock axis. Newly formed sites lock the incoming step. Seeds keep
their seed letters as a singleton. t(q) is the formation tick. tau = t+1 is
per-probe. Unformed at tau => UNDEFINED. Split HOLD required. When split
HOLDs, m is the unique vector in M. Let i in {1,2,3} be the axis index of
m. e_next = e_{i+1} with 3+1->1. e_prev = e_{i-1} with 1-1->3. O_next =
O intersect {+/-e_next}. O_prev = O intersect {+/-e_prev}. If either empty,
Orient fails, not UNDEFINED. Order +e < -e. o_next is the lex-largest
vector in O_next (hence -e if both signs). o_prev likewise. Orient is the
sign of the integer determinant of columns m, o_next, o_prev. If split
fails, Orient fails, not UNDEFINED. Reverse HOLDs iff Orient(A)=Orient(B)
both +/-1. Face on C,D. Uniqueness of outgoing locks is not required.
Occupancy of sites is not used. A is not a seed. No larger host.
Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
AxisSet = frozenset[Point] | str
OrientVal = int | str
FramePiece = Point | int | str
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
AXIS_INDEX = {E1: 1, E2: 2, E3: 3}
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
    "Cyclic next/prev lex-largest outgoing determinant orientation of the "
    "1-in 2-out frame at t+1 on the four x-probes of the two-axis opposite "
    "seed, and reverse/face from that, are reported. Displayed, not adopted."
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


def lock_display(value: FramePiece) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail":
        return "fail"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, tuple) and value in LOCK_NAME:
        return LOCK_NAME[value]
    raise TypeError(f"frame piece is not a lock, index, or fail: {value!r}")


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


def cyclic_units(index: int) -> tuple[Point, Point]:
    """e_next, e_prev from axis index i with 3+1->1 and 1-1->3."""
    if index not in (1, 2, 3):
        raise ValueError(f"axis index is not in {{1,2,3}}: {index!r}")
    e_next = AXES[index % 3]
    e_prev = AXES[(index - 2) % 3]
    return e_next, e_prev


def signed_on_axis(outgoing: Outgoing, axis: Point) -> frozenset[Point] | str:
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        raise TypeError(f"outgoing is not a lock set: {outgoing!r}")
    return frozenset(outgoing & {axis, negate(axis)})


def lex_largest_on_axis(occupied: frozenset[Point], axis: Point) -> Point | str:
    """Lex-largest under +e < -e. Hence -e if both signs. Empty => fail."""
    if not occupied:
        return "fail"
    negative = negate(axis)
    if negative in occupied:
        return negative
    if axis in occupied:
        return axis
    return "fail"


def lex_smallest_on_axis(occupied: frozenset[Point], axis: Point) -> Point | str:
    """Lex-smallest mutation under +e < -e. Not this letter."""
    if not occupied:
        return "fail"
    if axis in occupied:
        return axis
    negative = negate(axis)
    if negative in occupied:
        return negative
    return "fail"


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
    """Lex-smallest signed letter per Axis(O) under +e_i < -e_i, axis order."""
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
        occupied = frozenset(outgoing & {axis, negate(axis)})
        chosen = lex_smallest_on_axis(occupied, axis)
        if chosen == "fail" or not isinstance(chosen, tuple):
            return "fail"
        picked.append(chosen)
    return picked[0], picked[1]


def sign_of_det(col1: Point, col2: Point, col3: Point) -> OrientVal:
    det = integer_det_columns(col1, col2, col3)
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def cyclic_pieces(
    incoming: Incoming,
    outgoing: Outgoing,
    *,
    largest: bool = True,
) -> tuple[FramePiece, FramePiece, FramePiece, OrientVal]:
    """i, o_next, o_prev, Orient. Split fail or empty side => fail, not UNDEFINED."""
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED
    if split != "hold":
        return "fail", "fail", "fail", "fail"
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail", "fail", "fail", "fail"
    index = axis_index_of(signed_m)
    e_next, e_prev = cyclic_units(index)
    o_next_set = signed_on_axis(outgoing, e_next)
    o_prev_set = signed_on_axis(outgoing, e_prev)
    if o_next_set == UNDEFINED or o_prev_set == UNDEFINED:
        return UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED
    if not isinstance(o_next_set, frozenset) or not isinstance(o_prev_set, frozenset):
        return "fail", "fail", "fail", "fail"
    picker = lex_largest_on_axis if largest else lex_smallest_on_axis
    o_next = picker(o_next_set, e_next)
    o_prev = picker(o_prev_set, e_prev)
    if o_next == "fail" or o_prev == "fail":
        return index, "fail", "fail", "fail"
    if not isinstance(o_next, tuple) or not isinstance(o_prev, tuple):
        return index, "fail", "fail", "fail"
    return index, o_next, o_prev, sign_of_det(signed_m, o_next, o_prev)


def frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Sign of det(m, o_next, o_prev) with cyclic lex-largest outgoing."""
    _index, _o_next, _o_prev, orient = cyclic_pieces(incoming, outgoing)
    return orient


def lex_smallest_cyclic_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: cyclic next/prev with lex-smallest, not lex-largest."""
    _index, _o_next, _o_prev, orient = cyclic_pieces(
        incoming, outgoing, largest=False
    )
    return orient


def lex_one_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: lex-smallest Axis(O) pair in axis order e1<e2<e3."""
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
    return sign_of_det(signed_m, plane[0], plane[1])


def unsigned_cyclic_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: unsigned +e_next,+e_prev instead of lex-largest signed."""
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
    e_next, e_prev = cyclic_units(axis_index_of(signed_m))
    o_next_set = signed_on_axis(outgoing, e_next)
    o_prev_set = signed_on_axis(outgoing, e_prev)
    if not isinstance(o_next_set, frozenset) or not isinstance(o_prev_set, frozenset):
        return "fail"
    if not o_next_set or not o_prev_set:
        return "fail"
    return sign_of_det(signed_m, e_next, e_prev)


def unique_signed_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: unique |O_i|=1 signed plane in axis order."""
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
    return sign_of_det(signed_m, plane[0], plane[1])


def lex_frame_orient(incoming: Incoming, outgoing: Outgoing) -> OrientVal:
    """Mutation: lexicographic unsigned o1,o2 in axis order."""
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
    return sign_of_det(signed_m, plane[0], plane[1])


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

    print("cyclic next/prev lex-largest det orientation reverse/face at t+1 on two-axis x-probes")
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
        and add(E2, E3) == YZ
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "cyclic-units-identity",
        cyclic_units(1) == (E2, E3)
        and cyclic_units(2) == (E3, E1)
        and cyclic_units(3) == (E1, E2)
        and axis_index_of(NEG_E3) == 3
        and axis_index_of(E1) == 1,
    )
    checks.check(
        "det-identity",
        integer_det_columns(E1, E2, NEG_E3) == -1
        and integer_det_columns(E1, NEG_E2, NEG_E3) == 1
        and integer_det_columns(E1, E2, E3) == 1
        and integer_det_columns(E1, NEG_E2, E3) == -1
        and integer_det_columns(E2, E3, NEG_E1) == -1
        and integer_det_columns(E1, E1, E2) == 0,
    )
    checks.check(
        "orient-identity",
        frame_orient(UNDEFINED, frozenset({E2, E3})) == UNDEFINED
        and frame_orient(frozenset({E1}), UNDEFINED) == UNDEFINED
        and frame_orient(frozenset(), frozenset({E2, E3})) == "fail"
        and frame_orient(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and frame_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == -1
        and frame_orient(frozenset({E1}), frozenset({NEG_E2, E3, NEG_E3})) == 1
        and frame_orient(frozenset({E1}), frozenset({E2, E3})) == 1
        and frame_orient(frozenset({E1}), frozenset({E2, NEG_E2, E3})) == -1
        and frame_orient(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == -1
        and frame_orient(frozenset({E1, NEG_E1}), frozenset({E2, E3})) == "fail"
        and lex_smallest_cyclic_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3}))
        == 1
        and lex_one_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == 1
        and lex_frame_orient(frozenset({E1}), frozenset({NEG_E2, E3, NEG_E3})) == 1
        and unique_signed_orient(frozenset({E1}), frozenset({E2, E3, NEG_E3}))
        == "fail"
        and leftover_axis(frozenset({NEG_E3}), frozenset({E1})) == frozenset({E2})
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
    split: dict[str, str] = {}
    signed_m: dict[str, Point | str] = {}
    index: dict[str, FramePiece] = {}
    o_next: dict[str, FramePiece] = {}
    o_prev: dict[str, FramePiece] = {}
    det: dict[str, int | str] = {}
    orient: dict[str, OrientVal] = {}
    lex_small: dict[str, OrientVal] = {}
    lex_one: dict[str, OrientVal] = {}
    unsigned_cyc: dict[str, OrientVal] = {}
    unique_signed: dict[str, OrientVal] = {}
    unsigned_lex: dict[str, OrientVal] = {}
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
        signed_m[name] = unique_signed_m(m1[name])
        index[name], o_next[name], o_prev[name], orient[name] = cyclic_pieces(
            m1[name], o1[name]
        )
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
        lex_small[name] = lex_smallest_cyclic_orient(m1[name], o1[name])
        lex_one[name] = lex_one_orient(m1[name], o1[name])
        unsigned_cyc[name] = unsigned_cyclic_orient(m1[name], o1[name])
        unique_signed[name] = unique_signed_orient(m1[name], o1[name])
        unsigned_lex[name] = lex_frame_orient(m1[name], o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"split={split[name]} "
            f"i={lock_display(index[name])} "
            f"o_next={lock_display(o_next[name])} "
            f"o_prev={lock_display(o_prev[name])} "
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
    unique_o_orient_b = frame_orient(unique_letter(m1["B"]), unique_letter(o1["B"]))
    print(f"Orient reverse={reverse} face={face}")
    print(f"split reverse={split_reverse} face={split_face}")
    print(f"cover reverse={cover_reverse} face={cover_face}")
    print(
        "per_element: unique signed incoming letter and cyclic next/prev "
        "lex-largest outgoing letters at a probe's t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four Orient reports, reverse/face from equal +/-1 signs")
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
        and frame_orient(
            incoming_set(PROBES["A"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["A"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["D"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["D"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["C"], 2, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 2, ticks, locks, seed_map),
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
        "theorem1-i-onext-oprev-Orient",
        index["A"] == "fail"
        and o_next["A"] == "fail"
        and o_prev["A"] == "fail"
        and orient["A"] == "fail"
        and index["B"] == 1
        and o_next["B"] == E2
        and o_prev["B"] == NEG_E3
        and det["B"] == -1
        and orient["B"] == -1
        and index["C"] == 1
        and o_next["C"] == NEG_E2
        and o_prev["C"] == NEG_E3
        and det["C"] == 1
        and orient["C"] == 1
        and index["D"] == "fail"
        and o_next["D"] == "fail"
        and o_prev["D"] == "fail"
        and orient["D"] == "fail"
        and signed_m["B"] == E1
        and signed_m["C"] == E1,
        str({name: orient_display(orient[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-mixed-O-lex-largest-not-unique",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_signed["B"] == "fail"
        and unique_o_orient_b == UNDEFINED
        and orient["B"] == -1
        and orient["B"] != UNDEFINED
        and lex_small["B"] == 1
        and lex_one["B"] == 1
        and lex_small["B"] != orient["B"],
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
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and PROBES["A"] not in seed_map
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and Y_PROBES["A"] in seed_map
        and Z_PROBES["A"] in seed_map,
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
        reverse,
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
        face,
    )
    checks.check(
        "cover-and-split-do-not-score-handedness",
        split["B"] == "hold"
        and split["C"] == "hold"
        and orient["B"] == -1
        and orient["C"] == 1
        and orient["B"] != orient["C"]
        and reverse == "fail"
        and face == "fail"
        and reverse == split_reverse
        and face == split_face,
    )
    checks.check(
        "split-fail-is-orient-fail-not-undefined",
        frame_orient(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and axis_split(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "fail"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "fail"
        and frame_orient(frozenset({E1, NEG_E1}), frozenset({E2, E3})) == "fail"
        and axis_split(frozenset({E1, NEG_E1}), frozenset({E2, E3})) == "hold"
        and orient["A"] == "fail"
        and orient["D"] == "fail"
        and orient["A"] != UNDEFINED,
    )
    checks.check(
        "empty-Onext-or-Oprev-is-orient-fail-not-undefined",
        frame_orient(frozenset({E1}), frozenset()) == "fail"
        and frame_orient(frozenset({E1}), frozenset({E2})) == "fail"
        and frame_orient(frozenset({E1}), frozenset({E3})) == "fail"
        and frame_orient(frozenset({E1}), frozenset({E2, E3})) == 1,
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
        and frame_orient(frozenset({E1}), frozenset({E2, E3})) == 1
        and leftover_axis(frozenset({E1}), frozenset({E2, E3})) == frozenset(),
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
        and face_o_alone == "fail",
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and reverse == "fail"
        and face == "fail",
    )
    checks.check(
        "mutation-lex-smallest-or-lex-one-differs-at-B",
        lex_small["A"] == "fail"
        and lex_small["B"] == 1
        and lex_small["C"] == -1
        and lex_small["D"] == "fail"
        and lex_one["B"] == 1
        and lex_one["C"] == -1
        and unsigned_lex["B"] == 1
        and unsigned_lex["C"] == 1
        and unsigned_cyc["B"] == 1
        and unsigned_cyc["C"] == 1
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and orient["B"] == -1
        and orient["C"] == 1
        and lex_small["B"] != orient["B"]
        and lex_one["B"] != orient["B"]
        and unsigned_cyc["B"] != orient["B"]
        and unique_signed["C"] != orient["C"],
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["B"]) == frozenset({E1})
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_o_orient_b == UNDEFINED
        and orient["B"] == -1
        and split["B"] == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["D"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E3
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
        and o1["B"] != m1["B"],
    )

    y_m1, y_o1 = probe_sides(Y_PROBES, ticks, locks, seed_map)
    y_split = {name: axis_split(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient = {name: frame_orient(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_reverse = reverse_report(y_orient["A"], y_orient["B"])
    y_face = face_report(y_orient["C"], y_orient["D"])
    z_m1, z_o1 = probe_sides(Z_PROBES, ticks, locks, seed_map)
    z_split = {name: axis_split(z_m1[name], z_o1[name]) for name in ("A", "B", "C", "D")}
    z_orient = {name: frame_orient(z_m1[name], z_o1[name]) for name in ("A", "B", "C", "D")}
    z_reverse = reverse_report(z_orient["A"], z_orient["B"])
    z_face = face_report(z_orient["C"], z_orient["D"])
    nsopp_m1, nsopp_o1 = probe_sides(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    nsopp_cover = {
        name: axis_cover(nsopp_m1[name], nsopp_o1[name]) for name in ("A", "B", "C", "D")
    }
    nsopp_orient = {
        name: frame_orient(nsopp_m1[name], nsopp_o1[name]) for name in ("A", "B", "C", "D")
    }
    nsopp_cover_reverse = pair_bit(nsopp_cover["A"], nsopp_cover["B"])
    nsopp_reverse = reverse_report(nsopp_orient["A"], nsopp_orient["B"])
    same_d_o = outgoing_set(
        PROBES["D"],
        same_ticks[PROBES["D"]] + 1,
        same_ticks,
        same_locks,
        same_seeds,
    )
    nn_m1, nn_o1 = probe_sides(PROBES, nnseed_ticks, nnseed_locks, nnseed_seeds)
    nnseed_orient = {
        name: frame_orient(nn_m1[name], nn_o1[name]) for name in ("A", "B", "C", "D")
    }
    e2_orient_b = frame_orient(
        incoming_set(
            PROBES["B"], e2_ticks[PROBES["B"]] + 1, e2_ticks, e2_locks, e2_seeds
        ),
        outgoing_set(
            PROBES["B"], e2_ticks[PROBES["B"]] + 1, e2_ticks, e2_locks, e2_seeds
        ),
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
        and y_split["A"] == "hold"
        and y_split["B"] == "hold"
        and y_orient["A"] == 1
        and y_orient["B"] == -1
        and y_reverse == "fail"
        and y_face == "fail"
        and pair_bit(y_split["A"], y_split["B"]) == "hold"
        and y_reverse != pair_bit(y_split["A"], y_split["B"])
        and z_split["A"] == "hold"
        and z_orient["A"] == -1
        and z_orient["B"] == -1
        and z_orient["C"] == 1
        and z_orient["D"] == 1
        and z_reverse == "hold"
        and z_face == "hold"
        and reverse == "fail"
        and face == "fail"
        and z_reverse != reverse
        and z_face != face,
        str((y_orient, y_reverse, z_orient, z_reverse, z_face)),
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
        and nsopp_orient["A"] == "fail"
        and nsopp_cover_reverse == "hold"
        and nsopp_reverse == "fail"
        and cover["A"] == "fail"
        and reverse == "fail"
        and cover_reverse != nsopp_cover_reverse
        and nsopp_m1["A"] == frozenset({E2, E3, NEG_E3})
        and m1["A"] == frozenset({NEG_E3}),
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
        and o1["D"] != same_d_o,
    )
    checks.check(
        "not-nnseed-or-y-axis-e2-or-same-e1",
        TWO_AXIS_OPPOSITE_SEEDS != NNSEED_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != Y_AXIS_E2_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != SAME_E1_SEEDS
        and nnseed_orient["A"] == "fail"
        and nnseed_orient["B"] == "fail"
        and e2_orient_b == "fail"
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
        "note-reports-M-O-split-i-onext-oprev-Orient",
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
        and "i(A) = fail" in note
        and "o_next(A) = fail" in note
        and "o_prev(A) = fail" in note
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
        "note-not-cover-or-split-or-lex-one",
        "Cover and split do not score handedness" in note
        and "not leftover of nm2axx axis-cover" in normalized_note
        and "not leftover of nm2ax12x 1-in 2-out split" in normalized_note
        and "not leftover of nm2oricyclz z-probe cyclic" in normalized_note
        and "not leftover of lex-one axis-order" in normalized_note
        and "not leftover of lex-smallest cyclic" in normalized_note
        and "O is not M" in note
        and "A is not a seed" in note,
    )
    checks.check(
        "note-not-one-sided-or-leftover-empty",
        "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover-of-`O` alone" in normalized_note
        and "not leftover-empty fail" in normalized_note
        and "not leftover of y-probe cyclic" in normalized_note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
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
        '    "docs/TWO_AXIS_OPPOSITE_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "cyclic_pieces" in defined_fns
        and "lex_largest_on_axis" in defined_fns
        and "lex_smallest_cyclic_orient" in defined_fns
        and "lex_one_orient" in defined_fns
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
        and set(ticks) <= host,
    )
    checks.check(
        "orient-cyclic-lex-largest-not-lex-one",
        reverse == "fail"
        and face == "fail"
        and split_reverse == "fail"
        and cover_reverse == "fail"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and z_reverse == "hold"
        and z_face == "hold"
        and lex_small["B"] == 1
        and orient["B"] == -1
        and lex_one["B"] == 1
        and unique_signed["B"] == "fail"
        and unique_signed["C"] == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail",
    )
    _ = (
        o0,
        unique_o_orient_b,
        unsigned_cyc,
        unsigned_lex,
        same_e1_ticks,
        same_e1_locks,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
