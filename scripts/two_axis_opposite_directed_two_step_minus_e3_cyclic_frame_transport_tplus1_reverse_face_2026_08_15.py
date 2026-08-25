#!/usr/bin/env python3
"""Directed 2-step cyclic-frame transport along -e3 at t+1 reverse/face.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Perp-step incoming lock. F, Orient,
directed-edge as nm2frm2sx with step -e_3. Orient as nm2oricyclz
(lex-largest cyclic). Directed-edge HOLD from q to q+e iff q and q+e are
in B_3(0), both formed at tau=t+1, split HOLDs at both, Orient +/-1 at
both, and the 3x3 integer matrix sending columns of F(q) to columns of
F(q+e) is a signed permutation P with det P = Orient(q)Orient(q+e). Else
that edge fails, not UNDEFINED. Directed 2-step along -e_3 HOLDs at q iff
q, q-e_3, q-2e_3 are in B_3(0) and both named directed-edges HOLD. A
vertex outside B_3(0) is fail, not UNDEFINED. Reverse probes: origin and
(0,1,0). Face probes: (0,0,1) and (0,1,1). Reverse HOLDs iff 2-step along
-e_3 HOLDs at both reverse probes. Face HOLDs iff both face probes HOLD.
Not a 4-cycle. Not leftover of +/-e1/+/-e2. Uniqueness is not required.
Occupancy of sites is not used. No larger host. Displayed, not adopted.
Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "A": (0, 0, 0),
    "B": (0, 1, 0),
    "C": (0, 0, 1),
    "D": (0, 1, 1),
}
Z_PROBES = {
    "A": (0, 0, 1),
    "B": (1, 1, 1),
    "C": (0, 0, 2),
    "D": (1, 0, 1),
}
STEP: Point = NEG_E3
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
    "Directed 2-step cyclic-frame transport along −e3 at t+1 on the two-axis "
    "opposite seed, and reverse/face from that, are reported. Displayed, not "
    "adopted."
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


def transport_neighbor_read(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff transport HOLDs at q and some formed 6-NN r has transport HOLD."""
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


def directed_edge_hold(
    source: Point,
    step: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD from source to source+step as nm2frm2sx. Else fail, not UNDEFINED."""
    target = add(source, step)
    if not in_ball(source) or not in_ball(target):
        return "fail"
    if source not in ticks or target not in ticks:
        return "fail"
    source_in, source_out = site_sides(source, ticks, locks, seed_map)
    target_in, target_out = site_sides(target, ticks, locks, seed_map)
    source_split = axis_split(source_in, source_out)
    target_split = axis_split(target_in, target_out)
    source_orient = frame_orient(source_in, source_out)
    target_orient = frame_orient(target_in, target_out)
    if (
        source_split != "hold"
        or target_split != "hold"
        or source_orient not in (1, -1)
        or target_orient not in (1, -1)
    ):
        return "fail"
    source_frame = frame_triple(source_in, source_out)
    target_frame = frame_triple(target_in, target_out)
    sending = sending_holds(source_frame, target_frame, source_orient, target_orient)
    if sending == UNDEFINED:
        return "fail"
    return sending


def directed_edge_sending(
    source: Point,
    step: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Sending:
    """P sending columns of F(source) to F(source+step). Fail if the edge fails."""
    if directed_edge_hold(source, step, ticks, locks, seed_map) != "hold":
        return "fail"
    source_in, source_out = site_sides(source, ticks, locks, seed_map)
    target = add(source, step)
    target_in, target_out = site_sides(target, ticks, locks, seed_map)
    return sending_matrix(
        frame_triple(source_in, source_out),
        frame_triple(target_in, target_out),
    )


def two_step_hold(
    site: Point,
    step: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff both named directed-edges HOLD and the three vertices lie in B_3(0)."""
    mid = add(site, step)
    end = add(mid, step)
    if not in_ball(site) or not in_ball(mid) or not in_ball(end):
        return "fail"
    first = directed_edge_hold(site, step, ticks, locks, seed_map)
    second = directed_edge_hold(mid, step, ticks, locks, seed_map)
    if first == "hold" and second == "hold":
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
    """Reverse HOLDs iff neighbor-read at A and at B."""
    return pair_bit(left, right)


def neighbor_read_face_report(left: str, right: str) -> str:
    """Face HOLDs iff neighbor-read at C and at D."""
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

    print(
        "directed 2-step cyclic-frame transport along -e3 reverse/face at t+1 "
        "on two-axis opposite seeds"
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
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-seed-probes-in-host",
        probe_sites == (ORIGIN, E2, E3, PAIR2)
        and set(probe_sites) <= host
        and ORIGIN in probe_sites
        and probe_sites != z_probe_sites
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
        and add(ORIGIN, STEP) == NEG_E3
        and add(NEG_E3, STEP) == (0, 0, -2)
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball((0, 0, -2))
        and in_ball((0, 1, -2))
        and not in_ball((4, 0, 0))
        and not in_ball((0, 1, 3)),
    )
    checks.check(
        "det-identity",
        integer_det_columns(E1, NEG_E2, NEG_E3) == 1
        and integer_det_columns(NEG_E1, E2, NEG_E3) == 1
        and integer_det_columns(E2, E3, NEG_E1) == -1
        and integer_det_columns(NEG_E2, E3, NEG_E1) == 1
        and integer_det_columns(NEG_E3, NEG_E1, NEG_E2) == -1
        and integer_det_columns(E1, E2, E3) == 1
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
        and cyclic_units(E1) == (E2, E3)
        and cyclic_units(E2) == (E3, E1)
        and cyclic_units(E3) == (E1, E2)
        and lex_largest_on_axis(frozenset({E1, NEG_E1}), E1) == NEG_E1
        and lex_smallest_on_axis(frozenset({E1, NEG_E1}), E1) == E1
        and cyclic_signed_outgoing(frozenset({E2}), frozenset({E1, NEG_E1, E3}))
        == (E3, NEG_E1)
        and leftover_match(frozenset(), frozenset()) == "fail",
    )
    identity_frame = (E1, NEG_E2, NEG_E3)
    identity_target = (NEG_E3, NEG_E1, NEG_E2)
    identity_sending = sending_matrix(identity_frame, identity_target)
    checks.check(
        "sending-identity",
        frame_triple(frozenset({E1}), frozenset({NEG_E2, NEG_E3}))
        == (E1, NEG_E2, NEG_E3)
        and sending_matrix(UNDEFINED, identity_frame) == UNDEFINED
        and sending_matrix(identity_frame, "fail") == "fail"
        and sending_matrix(identity_frame, identity_frame) == (E1, E2, E3)
        and is_signed_permutation((E1, E2, E3))
        and not is_signed_permutation((E1, E1, E2))
        and sending_holds(identity_frame, identity_frame, 1, 1) == "hold"
        and sending_holds(identity_frame, identity_target, 1, -1) == "hold"
        and integer_det_columns(*identity_sending) == -1
        and is_signed_permutation(identity_sending)
        and not is_nonnegative_permutation(identity_sending)
        and mul_columns(identity_frame, identity_sending) == identity_target,
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(TWO_SITE_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_LOCK_SEEDS)
    live_ticks, live_locks, live_seeds = form(LIVE_THREE_AXIS_SEEDS)

    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    split: dict[str, str] = {}
    orient: dict[str, OrientVal] = {}
    frames: dict[str, FrameVal] = {}
    first_edge: dict[str, str] = {}
    second_edge: dict[str, str] = {}
    first_p: dict[str, Sending] = {}
    second_p: dict[str, Sending] = {}
    two_step: dict[str, str] = {}
    two_step_other: dict[str, dict[str, str]] = {
        name: {} for name in ("plus_e1", "minus_e1", "plus_e2", "minus_e2", "plus_e3")
    }
    other_steps = {
        "plus_e1": E1,
        "minus_e1": NEG_E1,
        "plus_e2": E2,
        "minus_e2": NEG_E2,
        "plus_e3": E3,
    }
    chain: dict[str, tuple[Point, Point, Point]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        mid = add(site, STEP)
        end = add(mid, STEP)
        chain[name] = (site, mid, end)
        incoming, outgoing = site_sides(site, ticks, locks, seed_map)
        m1[name] = incoming
        o1[name] = outgoing
        split[name] = axis_split(incoming, outgoing)
        orient[name] = frame_orient(incoming, outgoing)
        frames[name] = frame_triple(incoming, outgoing)
        first_edge[name] = directed_edge_hold(site, STEP, ticks, locks, seed_map)
        second_edge[name] = directed_edge_hold(mid, STEP, ticks, locks, seed_map)
        first_p[name] = directed_edge_sending(site, STEP, ticks, locks, seed_map)
        second_p[name] = directed_edge_sending(mid, STEP, ticks, locks, seed_map)
        two_step[name] = two_step_hold(site, STEP, ticks, locks, seed_map)
        for label, step in other_steps.items():
            two_step_other[label][name] = two_step_hold(
                site, step, ticks, locks, seed_map
            )
        print(
            f"{name} {site} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"split={split[name]} "
            f"F={frame_display(frames[name])} "
            f"Orient={orient_display(orient[name])} "
            f"edge1={first_edge[name]} P1={matrix_display(first_p[name])} "
            f"edge2={second_edge[name]} P2={matrix_display(second_p[name])} "
            f"two-step={two_step[name]}"
        )

    reverse = pair_bit(two_step["A"], two_step["B"])
    face = pair_bit(two_step["C"], two_step["D"])
    transport = {
        name: frame_transport(PROBES[name], ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    transport_reverse = pair_bit(transport["A"], transport["B"])
    transport_face = pair_bit(transport["C"], transport["D"])
    orient_reverse = pair_bit(
        "hold" if orient["A"] in (1, -1) and orient["A"] == orient["B"] else "fail",
        "hold" if orient["A"] in (1, -1) and orient["A"] == orient["B"] else "fail",
    )
    if orient["A"] in (1, -1) and orient["A"] == orient["B"]:
        orient_reverse = "hold"
    else:
        orient_reverse = "fail" if UNDEFINED not in (orient["A"], orient["B"]) else UNDEFINED
    if orient["C"] in (1, -1) and orient["C"] == orient["D"]:
        orient_face = "hold"
    else:
        orient_face = "fail" if UNDEFINED not in (orient["C"], orient["D"]) else UNDEFINED
    plus_e1_reverse = pair_bit(
        two_step_other["plus_e1"]["A"], two_step_other["plus_e1"]["B"]
    )
    plus_e1_face = pair_bit(
        two_step_other["plus_e1"]["C"], two_step_other["plus_e1"]["D"]
    )
    minus_e1_reverse = pair_bit(
        two_step_other["minus_e1"]["A"], two_step_other["minus_e1"]["B"]
    )
    minus_e1_face = pair_bit(
        two_step_other["minus_e1"]["C"], two_step_other["minus_e1"]["D"]
    )
    plus_e2_reverse = pair_bit(
        two_step_other["plus_e2"]["A"], two_step_other["plus_e2"]["B"]
    )
    plus_e2_face = pair_bit(
        two_step_other["plus_e2"]["C"], two_step_other["plus_e2"]["D"]
    )
    minus_e2_reverse = pair_bit(
        two_step_other["minus_e2"]["A"], two_step_other["minus_e2"]["B"]
    )
    minus_e2_face = pair_bit(
        two_step_other["minus_e2"]["C"], two_step_other["minus_e2"]["D"]
    )
    plus_e3_reverse = pair_bit(
        two_step_other["plus_e3"]["A"], two_step_other["plus_e3"]["B"]
    )
    plus_e3_face = pair_bit(
        two_step_other["plus_e3"]["C"], two_step_other["plus_e3"]["D"]
    )
    print(f"two-step reverse={reverse} face={face}")
    print(f"transport reverse={transport_reverse} face={transport_face}")
    print(
        "per_element: directed 2-step cyclic-frame sending along -e_3 at a seed's t+1"
    )
    print(
        "per_site: scored only at seeds origin,(0,1,0),(0,0,1),(0,1,1) on Euclidean B_3(0)"
    )
    print("per_mode: no spectral or mode calculation is executed on this finite host")
    print("per_block: four 2-step reports, reverse/face from those bits")
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
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 0
        and ticks[PROBES["C"]] == 0
        and ticks[PROBES["D"]] == 0
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "outside-ball-is-fail-not-undefined",
        directed_edge_hold((0, 0, -3), STEP, ticks, locks, seed_map) == "fail"
        and two_step_hold((0, 1, 1), E3, ticks, locks, seed_map) == "fail"
        and not in_ball((0, 1, 3))
        and two_step_hold((0, 1, 1), E3, ticks, locks, seed_map) != UNDEFINED
        and directed_edge_hold((4, 0, 0), STEP, ticks, locks, seed_map) == "fail",
    )
    checks.check(
        "unformed-in-ball-is-fail-not-undefined",
        in_ball((0, 0, 3))
        and (0, 0, 3) not in ticks
        and directed_edge_hold((0, 0, 2), E3, ticks, locks, seed_map) == "fail"
        and two_step_hold((0, 1, 0), E2, ticks, locks, seed_map) == "fail"
        and in_ball((0, 3, 0))
        and (0, 3, 0) not in ticks,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 0
        and ticks[PROBES["C"]] == 0
        and ticks[PROBES["D"]] == 0
        and ticks[chain["A"][1]] == 1
        and ticks[chain["B"][1]] == 1
        and ticks[chain["A"][2]] == 4
        and ticks[chain["B"][2]] == 4,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-F-Orient",
        m1["A"] == frozenset({E1})
        and m1["B"] == frozenset({NEG_E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E2})
        and o1["A"] == frozenset({NEG_E2, NEG_E3})
        and o1["B"] == frozenset({E2, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3})
        and o1["D"] == frozenset({E1, NEG_E1, E3})
        and all(split[name] == "hold" for name in ("A", "B", "C", "D"))
        and frames["A"] == (E1, NEG_E2, NEG_E3)
        and frames["B"] == (NEG_E1, E2, NEG_E3)
        and frames["C"] == (E2, E3, NEG_E1)
        and frames["D"] == (NEG_E2, E3, NEG_E1)
        and orient["A"] == 1
        and orient["B"] == 1
        and orient["C"] == -1
        and orient["D"] == 1,
        str({name: (frame_display(frames[name]), orient_display(orient[name])) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-named-edges-and-two-step",
        first_edge["A"] == "hold"
        and first_edge["B"] == "hold"
        and first_edge["C"] == "hold"
        and first_edge["D"] == "hold"
        and second_edge["A"] == "fail"
        and second_edge["B"] == "fail"
        and second_edge["C"] == "hold"
        and second_edge["D"] == "hold"
        and two_step["A"] == "fail"
        and two_step["B"] == "fail"
        and two_step["C"] == "hold"
        and two_step["D"] == "hold"
        and matrix_display(first_p["A"]) == "[0 -1 0; 0 0 1; 1 0 0]"
        and matrix_display(first_p["B"]) == "[0 1 0; 0 0 1; 1 0 0]"
        and matrix_display(first_p["C"]) == "[0 -1 0; 0 0 -1; -1 0 0]"
        and matrix_display(first_p["D"]) == "[0 -1 0; 0 0 -1; 1 0 0]"
        and matrix_display(second_p["A"]) == "fail"
        and matrix_display(second_p["B"]) == "fail"
        and matrix_display(second_p["C"]) == "[0 -1 0; 0 0 1; 1 0 0]"
        and matrix_display(second_p["D"]) == "[0 1 0; 0 0 1; 1 0 0]"
        and integer_det_columns(*first_p["A"]) == -1
        and integer_det_columns(*first_p["B"]) == 1
        and integer_det_columns(*first_p["C"]) == -1
        and integer_det_columns(*first_p["D"]) == 1
        and integer_det_columns(*first_p["A"]) == orient["A"] * -1
        and integer_det_columns(*first_p["C"]) == orient["C"] * orient["A"]
        and integer_det_columns(*second_p["C"]) == orient["A"] * -1
        and integer_det_columns(*second_p["D"]) == orient["B"] * 1
        and chain["A"] == (ORIGIN, NEG_E3, (0, 0, -2))
        and chain["B"] == (E2, (0, 1, -1), (0, 1, -2))
        and chain["C"] == (E3, ORIGIN, NEG_E3)
        and chain["D"] == (PAIR2, E2, (0, 1, -1))
        and all(in_ball(site) for triple in chain.values() for site in triple),
        str({name: two_step[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem2-reverse-two-step-fail",
        reverse == "fail"
        and two_step["A"] == "fail"
        and two_step["B"] == "fail"
        and reverse != UNDEFINED
        and reverse != "hold"
        and transport_reverse == "hold"
        and transport_reverse != reverse
        and orient_reverse == "hold"
        and orient_reverse != reverse,
    )
    checks.check(
        "theorem3-face-two-step-hold",
        face == "hold"
        and two_step["C"] == "hold"
        and two_step["D"] == "hold"
        and face != UNDEFINED
        and face != "fail"
        and transport_face == "hold",
    )
    checks.check(
        "all-four-chains-stay-in-b3",
        all(in_ball(site) for triple in chain.values() for site in triple)
        and two_step["A"] == "fail"
        and two_step["C"] == "hold",
    )
    checks.check(
        "not-a-4-cycle",
        chain["A"][2] != ORIGIN
        and chain["B"][2] != E2
        and add(add(ORIGIN, STEP), STEP) == (0, 0, -2)
        and {PROBES["A"], PROBES["B"], PROBES["C"], PROBES["D"]}
        == {ORIGIN, E2, E3, PAIR2}
        and "Not a 4-cycle" in note,
    )
    checks.check(
        "not-leftover-of-plus-minus-e1-e2",
        plus_e1_reverse == "fail"
        and plus_e1_face == "fail"
        and minus_e1_reverse == "fail"
        and minus_e1_face == "fail"
        and plus_e2_reverse == "fail"
        and plus_e2_face == "fail"
        and minus_e2_reverse == "fail"
        and minus_e2_face == "fail"
        and reverse == "fail"
        and face == "hold"
        and plus_e1_face != face
        and minus_e1_face != face
        and plus_e2_face != face
        and minus_e2_face != face
        and plus_e3_reverse == "hold"
        and plus_e3_face == "fail"
        and plus_e3_reverse != reverse
        and plus_e3_face != face,
    )
    checks.check(
        "not-leftover-of-existential-6nn-transport",
        all(transport[name] == "hold" for name in ("A", "B", "C", "D"))
        and transport_reverse == "hold"
        and transport_face == "hold"
        and reverse == "fail"
        and face == "hold"
        and transport_reverse != reverse,
    )
    checks.check(
        "split-fail-at-second-reverse-vertex-is-edge-fail",
        axis_split(*site_sides(chain["A"][2], ticks, locks, seed_map)) == "fail"
        and axis_split(*site_sides(chain["B"][2], ticks, locks, seed_map)) == "fail"
        and two_in_one_out(*site_sides(chain["A"][2], ticks, locks, seed_map))
        == "hold"
        and second_edge["A"] == "fail"
        and second_edge["A"] != UNDEFINED
        and frame_triple(*site_sides(chain["A"][2], ticks, locks, seed_map))
        == "fail",
    )
    checks.check(
        "not-same-lock-or-one-axis-or-live-three-axis-seed",
        TWO_AXIS_SEEDS != SAME_LOCK_SEEDS
        and TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != LIVE_THREE_AXIS_SEEDS
        and ticks[PROBES["C"]] == 0
        and one_ticks[PROBES["C"]] == 1
        and same_ticks[PROBES["C"]] == 1
        and m1["C"] == frozenset({E2})
        and site_sides(PROBES["C"], one_ticks, one_locks, one_seeds)[0]
        == frozenset({E3})
        and site_sides(PROBES["C"], same_ticks, same_locks, same_seeds)[0]
        == frozenset({E3})
        and pair_bit(
            two_step_hold(PROBES["C"], STEP, live_ticks, live_locks, live_seeds),
            two_step_hold(PROBES["D"], STEP, live_ticks, live_locks, live_seeds),
        )
        == "fail"
        and face == "hold"
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in live_ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-F-Orient-P-two-step",
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
        and "two-step(A) = fail" in note
        and "two-step(B) = fail" in note
        and "two-step(C) = hold" in note
        and "two-step(D) = hold" in note
        and "P(A → A−e_3) = [0 -1 0; 0 0 1; 1 0 0]" in note
        and "P(B → B−e_3) = [0 1 0; 0 0 1; 1 0 0]" in note
        and "P(C → C−e_3) = [0 -1 0; 0 0 -1; -1 0 0]" in note
        and "P(D → D−e_3) = [0 -1 0; 0 0 -1; 1 0 0]" in note
        and "P(C−e_3 → C−2e_3) = [0 -1 0; 0 0 1; 1 0 0]" in note
        and "P(D−e_3 → D−2e_3) = [0 1 0; 0 0 1; 1 0 0]" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse directed 2-step cyclic-frame transport at τ: fail" in note
        and "Face directed 2-step cyclic-frame transport at τ: hold" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-plus-minus-e1-e2-or-4-cycle",
        "Not a 4-cycle" in note
        and "not leftover of ±e1/±e2" in normalized_note
        and "not leftover of nm2cycfrmz cyclic-frame transport" in normalized_note
        and "O is not M" in note
        and "second pair is a new seed, not a formed child" in normalized_note,
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
        '    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "frame_triple" in defined_fns
        and "sending_matrix" in defined_fns
        and "is_signed_permutation" in defined_fns
        and "directed_edge_hold" in defined_fns
        and "two_step_hold" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns)
        and FORBIDDEN_NOTE_TOKENS == (
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
        ),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    z_two_step = {
        name: two_step_hold(Z_PROBES[name], STEP, ticks, locks, seed_map)
        for name in ("A", "B", "C", "D")
    }
    checks.check(
        "not-z-probes-as-this-letter",
        probe_sites != z_probe_sites
        and z_two_step["A"] == "hold"
        and z_two_step["D"] == "fail"
        and two_step["D"] == "hold"
        and pair_bit(z_two_step["C"], z_two_step["D"]) == "fail"
        and face == "hold"
        and pair_bit(z_two_step["C"], z_two_step["D"]) != face,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
