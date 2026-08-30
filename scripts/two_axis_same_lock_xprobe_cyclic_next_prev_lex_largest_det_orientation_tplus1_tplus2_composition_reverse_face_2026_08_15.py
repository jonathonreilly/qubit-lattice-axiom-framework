#!/usr/bin/env python3
"""Cyclic lex-largest orientation freeze t+1 versus t+2 reverse/face composition.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint same-lock pairs: origin locks +e_1, (0,1,0) locks +e_1,
(0,0,1) locks +e_2, (0,1,1) locks +e_2. Same process and x-probes as nm2slx.
Perp-step incoming lock. M, O, split as nm2sl12. Unformed => UNDEFINED. Split
HOLDs iff cover HOLDs and |Axis(M)|=1. Split HOLD required. When split
HOLDs, m is the unique vector in M. Let i in {1,2,3} be the axis index of
m. e_next = e_{i+1} with 3+1->1. e_prev = e_{i-1} with 1-1->3. O_next =
O intersect {+/-e_next}. O_prev = O intersect {+/-e_prev}. If either is
empty, Orient fails, not UNDEFINED. Order +e < -e. o_next is the
lex-largest vector in O_next (hence -e if both signs). o_prev likewise.
Orient as nm2oricyclz at each cut: the sign of the integer determinant of
columns m, o_next, o_prev. If split fails, Orient fails, not UNDEFINED.
t(q)=formation tick. tau1=t+1, tau2=t+2. No global T. Do not score tau=t.
Reverse/face from Orient at each cut. Reverse HOLDs iff Orient(A)=Orient(B)
both +/-1. Face on C,D. Composition HOLD iff Orient at tau1 equals Orient
at tau2 at A,B,C,D. Uniqueness of O is not required. Occupancy of sites is
not used. A is not a seed. No larger host. Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
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
    "S⁺",
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Cyclic lex-largest orientation at t+1 versus t+2 on the four x-probes of "
    "the two-axis same-lock seed, reverse/face at each cut, and "
    "composition, are reported. Displayed, not adopted."
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

    print("cyclic lex-largest orientation freeze t+1 versus t+2 reverse/face composition on two-axis same-lock x-probes")
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
        and lex_one_orient(frozenset({E2}), frozenset({E1, E3})) == -1
        and frame_orient(frozenset({E2}), frozenset({E1, NEG_E1, E2, E3})) == "fail"
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
        composition_report(-1, -1, -1, -1, 1, 1, 1, 1) == "hold"
        and composition_report(-1, -1, -1, -1, 1, -1, 1, 1) == "fail"
        and composition_report(-1, "fail", -1, -1, 1, 1, 1, 1) == "fail"
        and composition_report("fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail")
        == "hold"
        and composition_report("fail", "fail", -1, -1, 1, 1, 1, 1) == "hold"
        and composition_report(UNDEFINED, -1, -1, -1, 1, 1, 1, 1) == UNDEFINED
        and leftover_bit_composition("hold", "hold", "hold", "hold") == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    xsame_ticks, xsame_locks, xsame_seeds = form(X_AXIS_SAME_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(TWO_SITE_SEEDS)
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
    axis_m1: dict[str, AxisSet] = {}
    axis_o1: dict[str, AxisSet] = {}
    cover1: dict[str, str] = {}
    cover2: dict[str, str] = {}
    split0: dict[str, str] = {}
    split1: dict[str, str] = {}
    split2: dict[str, str] = {}
    two_one: dict[str, str] = {}
    signed_m1: dict[str, Point | str] = {}
    signed_m2: dict[str, Point | str] = {}
    plane1: dict[str, tuple[Point, Point] | str] = {}
    pair1: dict[str, Point | str] = {}
    leftover1: dict[str, Point | str] = {}
    det1: dict[str, int | str] = {}
    det2: dict[str, int | str] = {}
    lex1: dict[str, OrientVal] = {}
    lex2: dict[str, OrientVal] = {}
    leftover_pair1: dict[str, OrientVal] = {}
    leftover_pair2: dict[str, OrientVal] = {}
    unique_signed1: dict[str, OrientVal] = {}
    unique_signed2: dict[str, OrientVal] = {}
    lex_one1: dict[str, OrientVal] = {}
    lex_one2: dict[str, OrientVal] = {}
    pair_present1: dict[str, str] = {}
    pair_present2: dict[str, str] = {}
    unique_plane1: dict[str, tuple[Point, Point] | str] = {}
    cyclic_plane1: dict[str, tuple[Point, Point] | str] = {}
    cyclic_plane2: dict[str, tuple[Point, Point] | str] = {}
    cyclic_small1: dict[str, OrientVal] = {}
    cyclic_small2: dict[str, OrientVal] = {}
    axis_i1: dict[str, int | str] = {}
    axis_i2: dict[str, int | str] = {}
    orient0: dict[str, OrientVal] = {}
    orient1: dict[str, OrientVal] = {}
    orient2: dict[str, OrientVal] = {}
    lx1: dict[str, AxisSet] = {}
    lx_m1: dict[str, AxisSet] = {}
    lx_o1: dict[str, AxisSet] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
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
        axis_m1[name] = axis_set(m1[name])
        axis_o1[name] = axis_set(o1[name])
        cover1[name] = axis_cover(m1[name], o1[name])
        cover2[name] = axis_cover(m2[name], o2[name])
        split0[name] = axis_split(m0[name], o0[name])
        split1[name] = axis_split(m1[name], o1[name])
        split2[name] = axis_split(m2[name], o2[name])
        two_one[name] = two_in_one_out(m1[name], o1[name])
        signed_m1[name] = unique_signed_m(m1[name])
        signed_m2[name] = unique_signed_m(m2[name])
        plane1[name] = outgoing_plane(axis_o1[name])
        unique_plane1[name] = unique_signed_outgoing_plane(o1[name])
        cyclic_plane1[name] = cyclic_signed_outgoing(m1[name], o1[name], largest=True)
        cyclic_plane2[name] = cyclic_signed_outgoing(m2[name], o2[name], largest=True)
        pair1[name] = opposite_pair_unit(o1[name])
        if isinstance(signed_m1[name], tuple):
            axis_i1[name] = axis_index(signed_m1[name])
        else:
            axis_i1[name] = "fail"
        if isinstance(signed_m2[name], tuple):
            axis_i2[name] = axis_index(signed_m2[name])
        else:
            axis_i2[name] = "fail"
        if isinstance(signed_m1[name], tuple) and isinstance(pair1[name], tuple):
            leftover1[name] = leftover_unit(signed_m1[name], pair1[name])
        else:
            leftover1[name] = "fail"
        if split1[name] == "hold" and isinstance(signed_m1[name], tuple) and isinstance(
            cyclic_plane1[name], tuple
        ):
            det1[name] = integer_det_columns(
                signed_m1[name], cyclic_plane1[name][0], cyclic_plane1[name][1]
            )
        else:
            det1[name] = "fail"
        if split2[name] == "hold" and isinstance(signed_m2[name], tuple) and isinstance(
            cyclic_plane2[name], tuple
        ):
            det2[name] = integer_det_columns(
                signed_m2[name], cyclic_plane2[name][0], cyclic_plane2[name][1]
            )
        else:
            det2[name] = "fail"
        pair_present1[name] = has_opposite_pair(o1[name])
        pair_present2[name] = has_opposite_pair(o2[name])
        lex1[name] = lex_frame_orient(m1[name], o1[name])
        lex2[name] = lex_frame_orient(m2[name], o2[name])
        leftover_pair1[name] = leftover_pair_orient(m1[name], o1[name])
        leftover_pair2[name] = leftover_pair_orient(m2[name], o2[name])
        unique_signed1[name] = unique_signed_orient(m1[name], o1[name])
        unique_signed2[name] = unique_signed_orient(m2[name], o2[name])
        lex_one1[name] = lex_one_orient(m1[name], o1[name])
        lex_one2[name] = lex_one_orient(m2[name], o2[name])
        cyclic_small1[name] = cyclic_lex_smallest_orient(m1[name], o1[name])
        cyclic_small2[name] = cyclic_lex_smallest_orient(m2[name], o2[name])
        orient0[name] = frame_orient(m0[name], o0[name])
        orient1[name] = frame_orient(m1[name], o1[name])
        orient2[name] = frame_orient(m2[name], o2[name])
        lx1[name] = leftover_axis(m1[name], o1[name])
        lx_m1[name] = leftover_of_one(m1[name])
        lx_o1[name] = leftover_of_one(o1[name])
        new_meet1[name] = new_records_meeting_six_nn(site, ticks, 1)
        new_meet2[name] = new_records_meeting_six_nn(site, ticks, 2)
        print(
            f"{name} t={ticks[site]} "
            f"M(tau1)={lockset_display(m1[name])} "
            f"O(tau1)={lockset_display(o1[name])} "
            f"Orient(tau1)={orient_display(orient1[name])} "
            f"M(tau2)={lockset_display(m2[name])} "
            f"O(tau2)={lockset_display(o2[name])} "
            f"Orient(tau2)={orient_display(orient2[name])}"
        )

    reverse1 = reverse_report(orient1["A"], orient1["B"])
    reverse2 = reverse_report(orient2["A"], orient2["B"])
    face1 = face_report(orient1["C"], orient1["D"])
    face2 = face_report(orient2["C"], orient2["D"])
    reverse0 = reverse_report(orient0["A"], orient0["B"])
    face0 = face_report(orient0["C"], orient0["D"])
    composition = composition_report(
        orient1["A"], orient2["A"],
        orient1["B"], orient2["B"],
        orient1["C"], orient2["C"],
        orient1["D"], orient2["D"],
    )
    leftover_t_tplus1_composition = composition_report(
        orient0["A"], orient1["A"],
        orient0["B"], orient1["B"],
        orient0["C"], orient1["C"],
        orient0["D"], orient1["D"],
    )
    leftover_bits = leftover_bit_composition(reverse1, reverse2, face1, face2)
    leftover_mo = leftover_mo_composition(
        m1["A"], m2["A"], o1["A"], o2["A"],
        m1["B"], m2["B"], o1["B"], o2["B"],
        m1["C"], m2["C"], o1["C"], o2["C"],
        m1["D"], m2["D"], o1["D"], o2["D"],
    )
    cover_reverse1 = pair_bit(cover1["A"], cover1["B"])
    cover_face1 = pair_bit(cover1["C"], cover1["D"])
    split_reverse1 = pair_bit(split1["A"], split1["B"])
    split_face1 = pair_bit(split1["C"], split1["D"])
    leftover_reverse = leftover_match(lx1["A"], lx1["B"])
    leftover_face = leftover_match(lx1["C"], lx1["D"])
    reverse_m_alone = leftover_match(lx_m1["A"], lx_m1["B"])
    face_m_alone = leftover_match(lx_m1["C"], lx_m1["D"])
    reverse_o_alone = leftover_match(lx_o1["A"], lx_o1["B"])
    face_o_alone = leftover_match(lx_o1["C"], lx_o1["D"])
    m_exist_reverse = existential_opposite(m1["A"], m1["B"])
    m_exist_face = existential_opposite(m1["C"], m1["D"])
    o_exist_reverse = existential_opposite(o1["A"], o1["B"])
    o_exist_face = existential_opposite(o1["C"], o1["D"])
    unsigned_orient1 = {
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
    one_orient_face = face_report(one_orient["C"], one_orient["D"])
    opp_m1, opp_o1 = probe_sides_at(PROBES, opp_ticks, opp_locks, opp_seeds, 1)
    opp_m2, opp_o2 = probe_sides_at(PROBES, opp_ticks, opp_locks, opp_seeds, 2)
    opp_orient1 = {
        name: frame_orient(opp_m1[name], opp_o1[name]) for name in ("A", "B", "C", "D")
    }
    opp_orient2 = {
        name: frame_orient(opp_m2[name], opp_o2[name]) for name in ("A", "B", "C", "D")
    }
    opp_split1 = {name: axis_split(opp_m1[name], opp_o1[name]) for name in ("A", "B", "C", "D")}
    opp_reverse1 = reverse_report(opp_orient1["A"], opp_orient1["B"])
    opp_face1 = face_report(opp_orient1["C"], opp_orient1["D"])
    opp_composition = composition_report(
        opp_orient1["A"], opp_orient2["A"],
        opp_orient1["B"], opp_orient2["B"],
        opp_orient1["C"], opp_orient2["C"],
        opp_orient1["D"], opp_orient2["D"],
    )
    print(f"Orient reverse tau1={reverse1} tau2={reverse2}")
    print(f"Orient face tau1={face1} tau2={face2}")
    print(f"Orient composition={composition}")
    print(
        "per_element: unique signed incoming letter and cyclic next/prev "
        "lex-largest outgoing letters of Axis(M) at a probe's t+1 and t+2"
    )
    print("per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four Orient reports at t+1 and t+2, reverse/face at each cut, composition")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    second_pair_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    ) and all(ticks.get(add(PAIR2, step)) != 1 for step in (E2, NEG_E2))
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and second_pair_parallel_blocked
        and ticks[ORIGIN] == 0
        and ticks[E2] == 0
        and ticks[E3] == 0
        and ticks[PAIR2] == 0
        and locks[ORIGIN] == {E1}
        and locks[E2] == {E1}
        and locks[E3] == {E2}
        and locks[PAIR2] == {E2}
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
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
            incoming_set(PROBES["A"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["A"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["C"], 2, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 2, ticks, locks, seed_map),
        )
        == UNDEFINED
        and frame_orient(
            incoming_set(PROBES["D"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["D"], 1, ticks, locks, seed_map),
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
        "theorem1-M-O-Orient-at-tau1",
        m1["A"] == frozenset({NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({NEG_E3})
        and o1["A"] == frozenset({E1})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E1})
        and split1["A"] == "fail"
        and split1["B"] == "hold"
        and split1["C"] == "hold"
        and split1["D"] == "fail"
        and cover1["A"] == "fail"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail"
        and signed_m1["A"] == NEG_E3
        and signed_m1["B"] == E1
        and signed_m1["C"] == E1
        and signed_m1["D"] == NEG_E3
        and axis_i1["A"] == 3
        and axis_i1["B"] == 1
        and axis_i1["C"] == 1
        and axis_i1["D"] == 3
        and cyclic_plane1["A"] == "fail"
        and cyclic_plane1["B"] == (E2, NEG_E3)
        and cyclic_plane1["C"] == (NEG_E2, NEG_E3)
        and cyclic_plane1["D"] == "fail"
        and unique_plane1["A"] == "fail"
        and unique_plane1["B"] == "fail"
        and unique_plane1["C"] == "fail"
        and unique_plane1["D"] == "fail"
        and det1["A"] == "fail"
        and det1["B"] == -1
        and det1["C"] == 1
        and det1["D"] == "fail"
        and orient1["A"] == "fail"
        and orient1["B"] == -1
        and orient1["C"] == 1
        and orient1["D"] == "fail"
        and plane1["A"] == "fail"
        and pair1["A"] == "fail",
        str({name: orient_display(orient1[name]) for name in ("A", "B", "C", "D")}),
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
        and split2["A"] == "fail"
        and split2["B"] == "hold"
        and split2["C"] == "hold"
        and split2["D"] == "fail"
        and signed_m2["A"] == signed_m1["A"]
        and cyclic_plane2["A"] == cyclic_plane1["A"]
        and cyclic_plane2["B"] == cyclic_plane1["B"]
        and cyclic_plane2["C"] == cyclic_plane1["C"]
        and cyclic_plane2["D"] == cyclic_plane1["D"]
        and det2["A"] == det1["A"]
        and det2["B"] == det1["B"]
        and det2["C"] == det1["C"]
        and det2["D"] == det1["D"]
        and orient2["A"] == "fail"
        and orient2["B"] == -1
        and orient2["C"] == 1
        and orient2["D"] == "fail"
        and orient2["A"] == orient1["A"]
        and orient2["B"] == orient1["B"]
        and orient2["C"] == orient1["C"]
        and orient2["D"] == orient1["D"],
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
        and reverse1 == "fail"
        and face1 == "fail",
    )
    checks.check(
        "theorem1-mixed-O-cyclic-not-unique",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_plane1["B"] == "fail"
        and unique_signed1["B"] == "fail"
        and cyclic_plane1["B"] == (E2, NEG_E3)
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_o_orient_a == "fail"
        and orient1["A"] == "fail"
        and orient1["A"] != UNDEFINED
        and unique_letter(o2["B"]) == UNDEFINED,
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet1["A"] == ((2, 0, 0),)
        and new_meet1["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet1["C"] == ((2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet1["D"] == ((2, 1, 0),)
        and new_meet2["A"] == ()
        and new_meet2["B"] == ()
        and new_meet2["C"] == ()
        and new_meet2["D"] == (),
        str({name: (new_meet1[name], new_meet2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-new-tplus2-neighbor-does-not-enter-O",
        new_meet2["A"] == ()
        and new_meet2["B"] == ()
        and new_meet2["C"] == ()
        and new_meet2["D"] == ()
        and o2["A"] == o1["A"]
        and o2["B"] == o1["B"]
        and o2["C"] == o1["C"]
        and o2["D"] == o1["D"]
        and orient2["A"] == orient1["A"]
        and orient2["D"] == orient1["D"],
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
        "theorem2-reverse-tau1-and-tau2-fail",
        reverse1 == "fail"
        and reverse2 == "fail"
        and orient1["A"] == "fail"
        and orient1["B"] == -1
        and orient2["A"] == "fail"
        and orient2["B"] == -1
        and reverse1 != UNDEFINED
        and reverse2 != "hold"
        and split_reverse1 == "fail"
        and cover_reverse1 == "fail",
    )
    checks.check(
        "theorem2-face-tau1-and-tau2-fail",
        face1 == "fail"
        and face2 == "fail"
        and orient1["C"] == 1
        and orient1["D"] == "fail"
        and orient2["C"] == 1
        and orient2["D"] == "fail"
        and face1 != UNDEFINED
        and face1 != "hold"
        and split_face1 == "fail"
        and cover_face1 == "fail",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and leftover_mo == "hold"
        and leftover_bits == "hold"
        and leftover_t_tplus1_composition == "fail"
        and leftover_t_tplus1_composition != composition
        and orient1["A"] == orient2["A"]
        and orient1["B"] == orient2["B"]
        and orient1["C"] == orient2["C"]
        and orient1["D"] == orient2["D"],
        composition,
    )
    checks.check(
        "cover-and-split-do-not-score-handedness",
        split_reverse1 == "fail"
        and cover_reverse1 == "fail"
        and reverse1 == "fail"
        and split_face1 == "fail"
        and cover_face1 == "fail"
        and face1 == "fail"
        and leftover_pair1["C"] == -1
        and leftover_pair1["D"] == "fail"
        and face_report(leftover_pair1["C"], leftover_pair1["D"]) == "fail"
        and leftover_pair1["C"] != orient1["C"]
        and reverse_report(lex1["A"], lex1["B"]) == "fail"
        and lex1["B"] == 1
        and lex1["B"] != orient1["B"]
        and lex1["C"] == 1
        and lex1["C"] == orient1["C"]
        and reverse2 == "fail"
        and face2 == "fail"
        and leftover_pair2["C"] == leftover_pair1["C"]
        and leftover_pair2["D"] == leftover_pair1["D"],
    )
    checks.check(
        "split-fail-is-orient-fail-not-undefined",
        frame_orient(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold"
        and two_one["A"] == "fail"
        and two_one["D"] == "fail"
        and two_one["C"] == "fail"
        and one_orient["A"] == "fail"
        and one_split["A"] == "fail"
        and one_cover["A"] == "hold"
        and one_orient["C"] == 1
        and one_split["C"] == "hold"
        and one_cover["C"] == "hold"
        and one_orient_face == "fail"
        and one_split_face == "fail"
        and one_cover_face == "hold",
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
        "not-leftover-of-1-axis-cover-reverse-hold",
        one_ticks[PROBES["A"]] == 3
        and one_ticks[PROBES["C"]] == 4
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["C"]] == 3
        and one_cover["A"] == "hold"
        and one_cover["B"] == "hold"
        and pair_bit(one_cover["A"], one_cover["B"]) == "hold"
        and cover_reverse1 == "fail"
        and one_orient["A"] == "fail"
        and one_m1["A"] == frozenset({E2, E3, NEG_E3})
        and one_m1["A"] != m1["A"]
        and reverse1 == "fail"
        and face1 == "fail",
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and leftover_reverse == reverse1
        and leftover_face == face1
        and lx1["A"] == frozenset({E2})
        and lx1["B"] == frozenset()
        and lx1["C"] == frozenset()
        and lx1["D"] == frozenset({E2})
        and leftover_match(lx1["A"], lx1["B"]) == "fail"
        and leftover_match(frozenset(), frozenset()) == "fail"
        and frame_orient(frozenset({E2}), frozenset({E1, E3})) == 1
        and leftover_axis(frozenset({E2}), frozenset({E1, E3})) == frozenset(),
    )
    checks.check(
        "mutation-leftover-of-M-or-O-alone-differs",
        lx_m1["A"] == frozenset({E1, E2})
        and lx_m1["B"] == frozenset({E2, E3})
        and lx_o1["A"] == frozenset({E2, E3})
        and lx_o1["B"] == frozenset({E1})
        and reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and reverse1 == "fail"
        and face1 == "fail"
        and lx_m1["A"] != lx1["A"]
        and lx_o1["A"] != lx1["A"],
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and reverse1 == "fail"
        and face1 == "fail"
        and pair_present1["A"] == "fail"
        and pair_present1["B"] == "hold"
        and pair_present1["C"] == "hold"
        and pair_present1["D"] == "fail"
        and pair_present2["A"] == "fail"
        and pair_bit(pair_present1["C"], pair_present1["D"]) == "fail"
        and leftover_pair1["A"] == "fail"
        and leftover_pair1["B"] == -1
        and leftover_pair1["C"] == -1
        and leftover_pair1["D"] == "fail"
        and leftover_pair1["C"] != orient1["C"]
        and face_report(leftover_pair1["C"], leftover_pair1["D"]) == face1,
    )
    checks.check(
        "mutation-unsigned-incoming-axis-agrees-here",
        unsigned_orient1["A"] == "fail"
        and unsigned_orient1["B"] == -1
        and unsigned_orient1["C"] == 1
        and unsigned_orient1["D"] == "fail"
        and frame_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == -1
        and unsigned_incoming_orient(frozenset({NEG_E2}), frozenset({E1, E3})) == 1
        and frame_orient(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and unsigned_incoming_orient(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and unsigned_orient1["C"] == orient1["C"]
        and unsigned_orient1["D"] == orient1["D"]
        and orient1["A"] == "fail",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == frozenset({NEG_E3})
        and unique_letter(o1["A"]) == frozenset({E1})
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(o1["D"]) == frozenset({E1})
        and unique_o_orient_a == "fail"
        and unique_signed1["A"] == "fail"
        and unique_signed1["B"] == "fail"
        and unique_signed1["C"] == "fail"
        and unique_signed1["D"] == "fail"
        and unique_signed2["B"] == "fail"
        and orient1["A"] == "fail"
        and orient1["D"] == "fail"
        and orient1["B"] == -1
        and orient1["B"] != UNDEFINED
        and unique_letter(o2["B"]) == UNDEFINED,
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["B"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E3
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["B"]) == E2
        and axis_o1["A"] == frozenset({E1})
        and pair1["A"] == "fail"
        and leftover1["A"] == "fail"
        and cyclic_plane1["A"] == "fail"
        and cyclic_plane1["B"] == (E2, NEG_E3)
        and plane1["A"] == "fail"
        and plane1["B"] == (E2, E3),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E3 in m1["A"]
        and E1 in o1["A"]
        and o1["A"] != m1["A"]
        and o2["A"] != m2["A"]
        and o1["B"] != m1["B"],
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
        and PAIR2 not in new_meet1["A"],
    )
    checks.check(
        "compare-nm2oricyclz-opposite-orient",
        opp_orient1["A"] == "fail"
        and opp_orient1["B"] == -1
        and opp_orient1["C"] == 1
        and opp_orient1["D"] == "fail"
        and opp_orient2["A"] == "fail"
        and opp_split1["A"] == "fail"
        and opp_reverse1 == "fail"
        and opp_face1 == "fail"
        and opp_composition == "hold"
        and isinstance(opp_o1["D"], frozenset)
        and NEG_E1 in opp_o1["D"]
        and isinstance(o1["D"], frozenset)
        and NEG_E1 not in o1["D"]
        and o1["D"] == frozenset({E1})
        and opp_o1["D"] == frozenset({E1, NEG_E1})
        and orient1["A"] == "fail"
        and reverse1 == "fail"
        and face1 == "fail"
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
        and opp_o1["D"] != o1["D"],
    )
    y_m1, y_o1 = probe_sides_at(Y_PROBES, ticks, locks, seed_map, 1)
    y_m2, y_o2 = probe_sides_at(Y_PROBES, ticks, locks, seed_map, 2)
    y_split1 = {name: axis_split(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient1 = {name: frame_orient(y_m1[name], y_o1[name]) for name in ("A", "B", "C", "D")}
    y_orient2 = {name: frame_orient(y_m2[name], y_o2[name]) for name in ("A", "B", "C", "D")}
    y_reverse1 = reverse_report(y_orient1["A"], y_orient1["B"])
    y_face1 = face_report(y_orient1["C"], y_orient1["D"])
    z_m1, z_o1 = probe_sides_at(Z_PROBES, ticks, locks, seed_map, 1)
    z_orient1 = {name: frame_orient(z_m1[name], z_o1[name]) for name in ("A", "B", "C", "D")}
    z_reverse1 = reverse_report(z_orient1["A"], z_orient1["B"])
    z_face1 = face_report(z_orient1["C"], z_orient1["D"])
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
        "not-z-probes-or-y-probes-or-z-symmetric-or-perp",
        FOUR_SITE_SEEDS != PERP_SEEDS
        and FOUR_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != z_probe_sites
        and probe_sites != y_probe_sites
        and y_m1["A"] != m1["A"]
        and y_split1["A"] == "hold"
        and y_orient1["A"] == -1
        and y_orient1["B"] == -1
        and y_reverse1 == "hold"
        and lex_frame_orient(y_m1["A"], y_o1["A"]) == 1
        and leftover_pair_orient(y_m1["A"], y_o1["A"]) == "fail"
        and unique_signed_orient(y_m1["A"], y_o1["A"]) == -1
        and y_split1["D"] == "fail"
        and y_orient1["D"] == "fail"
        and y_face1 == "fail"
        and y_orient2["A"] == y_orient1["A"]
        and z_reverse1 == "fail"
        and z_face1 == "hold"
        and z_orient1["A"] == "fail"
        and z_orient1["D"] == 1
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and reverse1 == "fail"
        and face1 == "fail"
        and y_reverse1 != reverse1
        and y_face1 == face1
        and z_face1 != face1,
    )
    checks.check(
        "not-one-axis-or-x-axis-same-or-y-symmetric-seed",
        FOUR_SITE_SEEDS != ONE_AXIS_SEEDS
        and FOUR_SITE_SEEDS != TWO_SITE_SEEDS
        and FOUR_SITE_SEEDS != X_AXIS_SAME_SEEDS
        and FOUR_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
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
        "note-reports-M-O-Orient-at-both-cuts",
        "t(A)=2" in note
        and "t(B)=1" in note
        and "t(C)=3" in note
        and "t(D)=2" in note
        and "M(A, τ1) = {−e_3}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_1}" in note
        and "M(D, τ1) = {−e_3}" in note
        and "O(A, τ1) = {+e_1}" in note
        and "O(B, τ1) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ1) = {−e_2, +e_3, −e_3}" in note
        and "O(D, τ1) = {+e_1}" in note
        and "Orient(A, τ1) = fail" in note
        and "Orient(B, τ1) = −1" in note
        and "Orient(C, τ1) = +1" in note
        and "Orient(D, τ1) = fail" in note
        and "M(A, τ2) = {−e_3}" in note
        and "M(B, τ2) = {+e_1}" in note
        and "M(C, τ2) = {+e_1}" in note
        and "M(D, τ2) = {−e_3}" in note
        and "O(A, τ2) = {+e_1}" in note
        and "O(B, τ2) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ2) = {−e_2, +e_3, −e_3}" in note
        and "O(D, τ2) = {+e_1}" in note
        and "Orient(A, τ2) = fail" in note
        and "Orient(B, τ2) = −1" in note
        and "Orient(C, τ2) = +1" in note
        and "Orient(D, τ2) = fail" in note
        and "o_next(A, τ1) = +e_1" in note
        and "o_prev(A, τ1) = fail" in note
        and "o_next(B, τ1) = +e_2" in note
        and "o_prev(B, τ1) = −e_3" in note
        and "o_next(C, τ1) = −e_2" in note
        and "o_prev(C, τ1) = −e_3" in note
        and "o_next(D, τ1) = +e_1" in note
        and "o_prev(D, τ1) = fail" in note
        and "split(A, τ1) = fail" in note
        and "split(B, τ1) = hold" in note
        and "split(C, τ1) = hold" in note
        and "split(D, τ1) = fail" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note
        and "new 6-NN of A at t(A)+2: none" in note
        and "new 6-NN of B at t(B)+2: none" in note
        and "new 6-NN of C at t(C)+2: none" in note
        and "new 6-NN of D at t(D)+2: none" in note,
    )
    checks.check(
        "note-reports-orient-reverse-face-composition",
        "Reverse oriented frame at τ1: fail" in note
        and "Reverse oriented frame at τ2: fail" in note
        and "Face oriented frame at τ1: fail" in note
        and "Face oriented frame at τ2: fail" in note
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
        and "not leftover of nm2oricyclz" in normalized_note
        and "not leftover of nm2oricyclslx" in normalized_note
        and "not leftover of nm2oricyclt2z" in normalized_note
        and "not leftover of nm2simt2z" in normalized_note
        and "not leftover of nm2chiralz lexicographic" in normalized_note
        and "not leftover of nm2orichz" in normalized_note
        and "not leftover of nm2orionez lex-one" in normalized_note
        and "not leftover of nm2oridetz unique signed" in normalized_note
        and "not leftover of nm2slx" in normalized_note
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
        and "Reverse oriented frame at τ1: fail" in note
        and "Face oriented frame at τ1: fail" in note,
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
        '    "docs/TWO_AXIS_SAME_LOCK_XPROBE_CYCLIC_NEXT_PREV_LEX_LARGEST_DET_ORIENTATION_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "lex_one_orient" in defined_fns
        and "cyclic_lex_smallest_orient" in defined_fns
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
        and ticks[PROBES["A"]] == 2
        and set(ticks) <= host,
    )
    checks.check(
        "orient-cyclic-lex-largest-not-leftover-or-lex-one",
        reverse1 == "fail"
        and face1 == "fail"
        and reverse2 == "fail"
        and face2 == "fail"
        and split_reverse1 == "fail"
        and cover_reverse1 == "fail"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and one_orient_face == "fail"
        and lex1["A"] == "fail"
        and lex1["B"] == 1
        and lex1["C"] == 1
        and lex1["D"] == "fail"
        and lex2["A"] == lex1["A"]
        and reverse_report(lex1["A"], lex1["B"]) == "fail"
        and face_report(lex1["C"], lex1["D"]) == "fail"
        and lex1["B"] != orient1["B"]
        and leftover_pair1["A"] == "fail"
        and leftover_pair1["B"] == -1
        and leftover_pair1["C"] == -1
        and leftover_pair1["D"] == "fail"
        and reverse_report(leftover_pair1["A"], leftover_pair1["B"]) == "fail"
        and face_report(leftover_pair1["C"], leftover_pair1["D"]) == "fail"
        and leftover_pair1["C"] != orient1["C"]
        and cyclic_small1["A"] == "fail"
        and cyclic_small1["B"] == 1
        and cyclic_small1["C"] == -1
        and cyclic_small1["D"] == "fail"
        and cyclic_small2["A"] == cyclic_small1["A"]
        and reverse_report(cyclic_small1["A"], cyclic_small1["B"]) == "fail"
        and face_report(cyclic_small1["C"], cyclic_small1["D"]) == "fail"
        and cyclic_small1["B"] != orient1["B"]
        and cyclic_small1["C"] != orient1["C"]
        and lex_one1["A"] == "fail"
        and lex_one1["B"] == 1
        and lex_one1["C"] == -1
        and lex_one1["D"] == "fail"
        and lex_one2["A"] == lex_one1["A"]
        and reverse_report(lex_one1["A"], lex_one1["B"]) == "fail"
        and face_report(lex_one1["C"], lex_one1["D"]) == "fail"
        and lex_one1["C"] != orient1["C"]
        and unique_signed1["A"] == "fail"
        and unique_signed1["B"] == "fail"
        and unique_signed1["C"] == "fail"
        and unique_signed1["D"] == "fail"
        and reverse_report(unique_signed1["A"], unique_signed1["B"]) == "fail"
        and face_report(unique_signed1["C"], unique_signed1["D"]) == "fail"
        and unique_signed1["C"] != orient1["C"]
        and o_exist_reverse == "fail"
        and o_exist_face == "fail"
        and leftover_mo == "hold"
        and leftover_bits == "hold"
        and opp_composition == "hold"
        and opp_o1["D"] != o1["D"],
    )
    _ = (
        o0,
        unique_o_orient_a,
        one_cover_face,
        one_split_face,
        unsigned_orient1,
        leftover_bits,
        perp_o1,
        axis_i2,
        leftover1,
        lex_one2,
        SAME_LOCK_SEEDS,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
