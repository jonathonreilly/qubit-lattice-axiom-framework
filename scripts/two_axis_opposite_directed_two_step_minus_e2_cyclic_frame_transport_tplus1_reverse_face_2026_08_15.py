#!/usr/bin/env python3
"""Directed 2-step cyclic-frame transport along -e2 at t+1 reverse/face.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Perp-step incoming lock. F, Orient,
directed-edge as nm2frm2sx with step -e_2. Unformed interior is fail for a
named directed edge, not UNDEFINED. A vertex outside B_3(0) is fail, not
UNDEFINED. Directed-edge HOLD from q to q-e_2 iff both sites are in B_3(0),
both formed at tau=t+1, split HOLDs at both, Orient +/-1 at both, and the
unique 3x3 integer matrix sending columns of F(q) to columns of F(q-e_2)
is a signed permutation P with det P = Orient(q)Orient(q-e_2). Directed
2-step along -e_2 HOLDs at q iff q, q-e_2, q-2e_2 are in B_3(0) and both
named directed edges HOLD. Reverse probes: origin and (0,1,0). Face probes:
(0,0,1) and (0,1,1). Reverse HOLD iff 2-step HOLDs at both reverse probes.
Face HOLD iff both face probes HOLD. Not a 4-cycle. Not leftover of 10 to
+e_1. Uniqueness is not required. Occupancy of sites is not used. No larger
host. Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E2_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E2_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Directed 2-step cyclic-frame transport along −e2 at t+1 on the two-axis "
    "opposite seed, and reverse/face from that, are reported. Displayed, not "
    "adopted."
)
STEP: Point = NEG_E2
SEED_PROBES = {
    "A": ORIGIN,
    "B": E2,
    "C": E3,
    "D": PAIR2,
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


def directed_edge(
    source: Point,
    target: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[str, Sending]:
    """Directed-edge HOLD along a named step. Else fail, not UNDEFINED."""
    if not in_ball(source) or not in_ball(target):
        return "fail", "fail"
    if source not in ticks or target not in ticks:
        return "fail", "fail"
    split_q, orient_q, frame_q = site_frame_state(source, ticks, locks, seed_map)
    split_r, orient_r, frame_r = site_frame_state(target, ticks, locks, seed_map)
    sending = sending_matrix(frame_q, frame_r)
    if (
        split_q == "hold"
        and split_r == "hold"
        and orient_q in (1, -1)
        and orient_r in (1, -1)
        and sending_holds(frame_q, frame_r, orient_q, orient_r) == "hold"
        and isinstance(sending, tuple)
    ):
        return "hold", sending
    return "fail", "fail"


def chain_of(site: Point, step: Point = STEP) -> tuple[Point, Point, Point]:
    mid = add(site, step)
    end = add(mid, step)
    return site, mid, end


def two_step_hold(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    step: Point = STEP,
) -> str:
    """HOLD iff both named directed edges HOLD and the three vertices are in B_3(0)."""
    start, mid, end = chain_of(site, step)
    if not in_ball(start) or not in_ball(mid) or not in_ball(end):
        return "fail"
    first, _p1 = directed_edge(start, mid, ticks, locks, seed_map)
    second, _p2 = directed_edge(mid, end, ticks, locks, seed_map)
    if first == "hold" and second == "hold":
        return "hold"
    return "fail"


def two_step_reverse_report(left: str, right: str) -> str:
    """Reverse HOLDs iff 2-step along -e_2 HOLDs at both reverse probes."""
    return pair_bit(left, right)


def two_step_face_report(left: str, right: str) -> str:
    """Face HOLDs iff 2-step along -e_2 HOLDs at both face probes."""
    return pair_bit(left, right)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("directed 2-step cyclic-frame transport along -e2 reverse/face at t+1 on two-axis opposite seed")
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
    seed_sites = tuple(SEED_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-seeds-in-host",
        seed_sites == (ORIGIN, E2, E3, PAIR2)
        and set(seed_sites) <= host
        and STEP == NEG_E2
        and add(ORIGIN, STEP) == NEG_E2
        and add(E2, STEP) == ORIGIN,
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
        and in_ball((0, -2, 1))
        and not in_ball((4, 0, 0)),
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
        and sending_holds(identity_frame, identity_frame, -1, -1) == "hold"
        and sending_holds(identity_frame, identity_target, -1, 1) == "hold"
        and integer_det_columns(*identity_sending) == -1
        and is_signed_permutation(identity_sending)
        and not is_nonnegative_permutation(identity_sending)
        and mul_columns(identity_frame, identity_sending) == identity_target,
    )

    ticks, locks, seed_map = form()
    plus_e1_bits = {
        name: two_step_hold(SEED_PROBES[name], ticks, locks, seed_map, step=E1)
        for name in ("A", "B", "C", "D")
    }

    t0: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    split: dict[str, str] = {}
    orient: dict[str, OrientVal] = {}
    frames: dict[str, FrameVal] = {}
    chain: dict[str, tuple[Point, Point, Point]] = {}
    edge1: dict[str, str] = {}
    edge2: dict[str, str] = {}
    p1: dict[str, Sending] = {}
    p2: dict[str, Sending] = {}
    two_step: dict[str, str] = {}
    mid_split: dict[str, str] = {}
    end_split: dict[str, str] = {}
    mid_orient: dict[str, OrientVal] = {}
    end_orient: dict[str, OrientVal] = {}
    mid_frame: dict[str, FrameVal] = {}
    end_frame: dict[str, FrameVal] = {}
    for name in ("A", "B", "C", "D"):
        site = SEED_PROBES[name]
        t0[name] = ticks[site]
        incoming, outgoing = site_sides(site, ticks, locks, seed_map)
        m1[name] = incoming
        o1[name] = outgoing
        split[name], orient[name], frames[name] = site_frame_state(
            site, ticks, locks, seed_map
        )
        start, mid, end = chain_of(site)
        chain[name] = (start, mid, end)
        mid_split[name], mid_orient[name], mid_frame[name] = site_frame_state(
            mid, ticks, locks, seed_map
        )
        end_split[name], end_orient[name], end_frame[name] = site_frame_state(
            end, ticks, locks, seed_map
        )
        edge1[name], p1[name] = directed_edge(start, mid, ticks, locks, seed_map)
        edge2[name], p2[name] = directed_edge(mid, end, ticks, locks, seed_map)
        two_step[name] = two_step_hold(site, ticks, locks, seed_map)
        print(
            f"{name} q={start} t={ticks[site]} "
            f"F={frame_display(frames[name])} "
            f"Orient={orient_display(orient[name])} "
            f"mid={mid} end={end} "
            f"edge1={edge1[name]} P1={matrix_display(p1[name])} "
            f"edge2={edge2[name]} P2={matrix_display(p2[name])} "
            f"two_step={two_step[name]}"
        )

    reverse = two_step_reverse_report(two_step["A"], two_step["B"])
    face = two_step_face_report(two_step["C"], two_step["D"])
    plus_e1_reverse = two_step_reverse_report(plus_e1_bits["A"], plus_e1_bits["B"])
    plus_e1_face = two_step_face_report(plus_e1_bits["C"], plus_e1_bits["D"])
    print(f"two_step reverse={reverse} face={face}")
    print(f"plus_e1 reverse={plus_e1_reverse} face={plus_e1_face}")
    print(
        "per_element: directed 2-step of F=(m,o_next,o_prev) along -e_2 "
        "with signed-permutation P on each named edge at t+1"
    )
    print("per_site: scored at the four seeds of the two-axis opposite seed on Euclidean B_3(0)")
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four 2-step reports, reverse/face from 2-step at paired seeds")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and ticks[SEED_PROBES["A"]] == 0
        and ticks[SEED_PROBES["B"]] == 0
        and ticks[SEED_PROBES["C"]] == 0
        and ticks[SEED_PROBES["D"]] == 0
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "outside-host-is-fail-not-undefined",
        directed_edge((4, 0, 0), (4, -1, 0), ticks, locks, seed_map) == ("fail", "fail")
        and two_step_hold((0, -3, 0), ticks, locks, seed_map) == "fail"
        and site_frame_state((4, 0, 0), ticks, locks, seed_map) == ("fail", "fail", "fail"),
    )
    checks.check(
        "theorem1-formation-ticks",
        t0["A"] == 0
        and t0["B"] == 0
        and t0["C"] == 0
        and t0["D"] == 0
        and ticks[chain["A"][1]] == 1
        and ticks[chain["A"][2]] == 4
        and ticks[chain["C"][1]] == 2
        and ticks[chain["C"][2]] == 3,
        str({name: t0[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-F-Orient",
        frames["A"] == (E1, NEG_E2, NEG_E3)
        and frames["B"] == (NEG_E1, E2, NEG_E3)
        and frames["C"] == (E2, E3, NEG_E1)
        and frames["D"] == (NEG_E2, E3, NEG_E1)
        and orient["A"] == 1
        and orient["B"] == 1
        and orient["C"] == -1
        and orient["D"] == 1
        and split["A"] == "hold"
        and split["B"] == "hold"
        and split["C"] == "hold"
        and split["D"] == "hold"
        and m1["A"] == frozenset({E1})
        and m1["B"] == frozenset({NEG_E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E2}),
        str({name: (frame_display(frames[name]), orient_display(orient[name])) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-named-edges-and-P",
        chain["A"] == (ORIGIN, NEG_E2, (0, -2, 0))
        and chain["B"] == (E2, ORIGIN, NEG_E2)
        and chain["C"] == (E3, (0, -1, 1), (0, -2, 1))
        and chain["D"] == (PAIR2, E3, (0, -1, 1))
        and all(in_ball(site) for name in ("A", "B", "C", "D") for site in chain[name])
        and edge1["A"] == "hold"
        and edge2["A"] == "fail"
        and edge1["B"] == "hold"
        and edge2["B"] == "hold"
        and edge1["C"] == "fail"
        and edge2["C"] == "fail"
        and edge1["D"] == "hold"
        and edge2["D"] == "fail"
        and p1["A"] == ((0, 1, 0), (0, 0, 1), (-1, 0, 0))
        and p2["A"] == "fail"
        and p1["B"] == ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
        and p2["B"] == ((0, 1, 0), (0, 0, 1), (-1, 0, 0))
        and p1["C"] == "fail"
        and p2["C"] == "fail"
        and p1["D"] == ((-1, 0, 0), (0, 1, 0), (0, 0, 1))
        and p2["D"] == "fail"
        and integer_det_columns(*p1["A"]) == -1
        and integer_det_columns(*p1["B"]) == 1
        and integer_det_columns(*p2["B"]) == -1
        and integer_det_columns(*p1["D"]) == -1
        and mid_split["A"] == "hold"
        and end_split["A"] == "fail"
        and mid_split["C"] == "fail"
        and end_split["D"] == "fail",
        str({name: (edge1[name], edge2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-two-step-bits",
        two_step["A"] == "fail"
        and two_step["B"] == "hold"
        and two_step["C"] == "fail"
        and two_step["D"] == "fail"
        and two_step["B"] != plus_e1_bits["B"]
        and all(plus_e1_bits[name] == "fail" for name in ("A", "B", "C", "D")),
        str(two_step),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse == "fail"
        and two_step["A"] == "fail"
        and two_step["B"] == "hold"
        and reverse != UNDEFINED
        and reverse != "hold",
    )
    checks.check(
        "theorem3-face-fail",
        face == "fail"
        and two_step["C"] == "fail"
        and two_step["D"] == "fail"
        and face != UNDEFINED
        and face != "hold",
    )
    checks.check(
        "not-a-4-cycle",
        chain["A"][2] != SEED_PROBES["A"]
        and chain["B"][2] != SEED_PROBES["B"]
        and chain["C"][2] != SEED_PROBES["C"]
        and chain["D"][2] != SEED_PROBES["D"]
        and STEP == NEG_E2
        and add(add(STEP, STEP), STEP) != ZERO,
    )
    checks.check(
        "not-leftover-of-plus-e1",
        plus_e1_bits["B"] == "fail"
        and two_step["B"] == "hold"
        and plus_e1_reverse == "fail"
        and plus_e1_face == "fail"
        and plus_e1_bits["B"] != two_step["B"],
    )
    checks.check(
        "second-pair-is-seed-not-formed-child",
        PAIR2 in seed_map
        and seed_map[PAIR2] == NEG_E2
        and ticks[PAIR2] == 0
        and E3 in seed_map
        and seed_map[E3] == E2
        and ticks[E3] == 0,
    )
    checks.check(
        "note-reports-ticks-frames-edges",
        "t(A)=0" in note
        and "t(B)=0" in note
        and "t(C)=0" in note
        and "t(D)=0" in note
        and "F(A) = (+e_1, −e_2, −e_3)" in note
        and "F(B) = (−e_1, +e_2, −e_3)" in note
        and "F(C) = (+e_2, +e_3, −e_1)" in note
        and "F(D) = (−e_2, +e_3, −e_1)" in note
        and "Orient(A) = +1" in note
        and "Orient(B) = +1" in note
        and "Orient(C) = −1" in note
        and "Orient(D) = +1" in note
        and "P(A→mid) = [0 0 -1; 1 0 0; 0 1 0]" in note
        and "P(B→mid) = [-1 0 0; 0 -1 0; 0 0 1]" in note
        and "P(B→end) = [0 0 -1; 1 0 0; 0 1 0]" in note
        and "P(D→mid) = [-1 0 0; 0 1 0; 0 0 1]" in note
        and "two_step(A) = fail" in note
        and "two_step(B) = hold" in note
        and "two_step(C) = fail" in note
        and "two_step(D) = fail" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse directed 2-step along −e_2 at τ: fail" in note
        and "Face directed 2-step along −e_2 at τ: fail" in note
        and "Not a 4-cycle." in note
        and "not leftover of 10" in normalized_note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
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
        '    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E2_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "directed_edge" in defined_fns
        and "two_step_hold" in defined_fns
        and "two_step_reverse_report" in defined_fns
        and "two_step_face_report" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[SEED_PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    _ = (plus_e1_reverse, plus_e1_face, mid_orient, end_orient, mid_frame, end_frame)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
