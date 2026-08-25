#!/usr/bin/env python3
"""Neighbor-read of 1-in 2-out split at t+1 versus t+2 reverse/face composition.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint same-lock pairs: origin locks +e_1, (0,1,0) locks +e_1,
(0,0,1) locks +e_2, (0,1,1) locks +e_2. Same process and z-probes as nm2slz.
M, O, and split as nm2sl12z. Neighbor-read of split as nm2sreadslz at each
cut. A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. The second pair is a new seed, not a formed child of the first
pair. t(q) is the formation tick. tau1 = t(q)+1. tau2 = t(q)+2. No global T.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is
the outgoing dual of M. Empty O is empty, not UNDEFINED. Axis(S) is the
unsigned lattice directions of signed locks in S. Cover HOLDs iff Axis(M)
intersect Axis(O) is empty and the union equals {e_1,e_2,e_3}. Split HOLDs
iff cover HOLDs and |Axis(M)|=1. 2-in 1-out is fail of this object, not
UNDEFINED. Neighbor-read of split HOLDs at q, tau iff split HOLDs at q and
some formed 6-NN r has split HOLD and Axis(M(r, tau))=Axis(M(q, tau)) and
Axis(O(r, tau))=Axis(O(q, tau)). If split fails at q, neighbor-read fails,
not UNDEFINED. Unformed q => UNDEFINED. Mixed remains a set. Uniqueness is
not required. Reverse HOLDs at a cut iff neighbor-read at A and at B. Face
likewise on C, D. Composition HOLDs iff neighbor-read at tau1 equals
neighbor-read at tau2 at A, B, C, and D. Occupancy of sites is not used.
Named-sign lettering is not used. No larger host. Displayed, not adopted.
Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_NEIGHBOR_READ_ONE_TWO_SPLIT_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_NEIGHBOR_READ_ONE_TWO_SPLIT_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
AxisSet = frozenset[Point] | str
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
    NEG_E1: "\u2212e_1",
    E2: "+e_2",
    NEG_E2: "\u2212e_2",
    E3: "+e_3",
    NEG_E3: "\u2212e_3",
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
    "Neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four "
    "z-probes of the two-axis same-lock seed, reverse/face at each cut, and "
    "composition, are reported. Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"

FormedRow = tuple[Point, Incoming, Outgoing, str, str]


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def neg(step: Point) -> Point:
    return (-step[0], -step[1], -step[2])


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
    """Cover HOLD with |Axis(M)|=2, hence |Axis(O)|=1. Not UNDEFINED."""
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


def matching_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Formed 6-NN r recovering the same 1-in 2-out axis assignment.

    If split fails at site, return the empty tuple (fail, not UNDEFINED).
    Unformed site => UNDEFINED.
    """
    own_m = incoming_set(site, tau, ticks, locks, seed_map)
    own_o = outgoing_set(site, tau, ticks, locks, seed_map)
    split = axis_split(own_m, own_o)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return ()
    axes_m = axis_set(own_m)
    axes_o = axis_set(own_o)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other_m = incoming_set(neighbor, tau, ticks, locks, seed_map)
        other_o = outgoing_set(neighbor, tau, ticks, locks, seed_map)
        if axis_split(other_m, other_o) != "hold":
            continue
        if axis_set(other_m) == axes_m and axis_set(other_o) == axes_o:
            found.append(neighbor)
    return tuple(found)


def neighbor_read(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff split HOLDs and a formed 6-NN recovers the same 1+2 axes.

    Unformed => UNDEFINED. Split fail => fail, not UNDEFINED.
    """
    matches = matching_neighbors(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def formed_neighbor_rows(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[FormedRow, ...]:
    """M, O, split, neighbor-read at each eventually-formed 6-NN, same tau."""
    rows: list[FormedRow] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        incoming = incoming_set(neighbor, tau, ticks, locks, seed_map)
        outgoing = outgoing_set(neighbor, tau, ticks, locks, seed_map)
        rows.append(
            (
                neighbor,
                incoming,
                outgoing,
                axis_split(incoming, outgoing),
                neighbor_read(neighbor, tau, ticks, locks, seed_map),
            )
        )
    return tuple(rows)


def matching_incoming_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Leftover contrast: formed 6-NN r with M(r, tau) equal to M(site, tau)."""
    own = incoming_set(site, tau, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if not isinstance(own, frozenset):
        raise TypeError(f"lock set is not a lock set: {own!r}")
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if other == UNDEFINED:
            continue
        if not isinstance(other, frozenset):
            raise TypeError(f"lock set is not a lock set: {other!r}")
        if other == own:
            found.append(neighbor)
    return tuple(found)


def neighbor_read_incoming(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover contrast: neighbor-read of M. Not this letter."""
    matches = matching_incoming_neighbors(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def matching_outgoing_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Leftover contrast: formed 6-NN r with O(r, tau) equal to O(site, tau)."""
    own = outgoing_set(site, tau, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if not isinstance(own, frozenset):
        raise TypeError(f"lock set is not a lock set: {own!r}")
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other = outgoing_set(neighbor, tau, ticks, locks, seed_map)
        if other == UNDEFINED:
            continue
        if not isinstance(other, frozenset):
            raise TypeError(f"lock set is not a lock set: {other!r}")
        if other == own:
            found.append(neighbor)
    return tuple(found)


def neighbor_read_outgoing(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover contrast: neighbor-read of O. Not this letter."""
    matches = matching_outgoing_neighbors(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def signed_pair_matches(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Leftover contrast: split HOLD plus M and O equal as signed sets."""
    own_m = incoming_set(site, tau, ticks, locks, seed_map)
    own_o = outgoing_set(site, tau, ticks, locks, seed_map)
    split = axis_split(own_m, own_o)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return ()
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other_m = incoming_set(neighbor, tau, ticks, locks, seed_map)
        other_o = outgoing_set(neighbor, tau, ticks, locks, seed_map)
        if axis_split(other_m, other_o) != "hold":
            continue
        if other_m == own_m and other_o == own_o:
            found.append(neighbor)
    return tuple(found)


def signed_pair_read(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """Leftover contrast: signed (M, O) recovery. Not this letter."""
    matches = signed_pair_matches(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def pair_read(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either side is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(read_a: str, read_b: str) -> str:
    """Reverse HOLDs iff neighbor-read at A and at B."""
    return pair_read(read_a, read_b)


def face_report(read_c: str, read_d: str) -> str:
    """Face HOLDs iff neighbor-read at C and at D."""
    return pair_read(read_c, read_d)


def composition_report(
    reads1: dict[str, str],
    reads2: dict[str, str],
) -> str:
    """HOLD iff neighbor-read at tau1 equals neighbor-read at tau2 at A,B,C,D."""
    for name in ("A", "B", "C", "D"):
        if reads1[name] == UNDEFINED or reads2[name] == UNDEFINED:
            return UNDEFINED
        if reads1[name] != reads2[name]:
            return "fail"
    return "hold"


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def probe_reads(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    *,
    plus: int = 1,
    reader=neighbor_read,
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = reader(
            site,
            site_ticks[site] + plus,
            site_ticks,
            site_locks,
            site_seeds,
        )
    return out


def match_display(matches: tuple[Point, ...] | str) -> str:
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if not matches:
        return "none"
    return ", ".join(str(site) for site in matches)


def formed_line(
    rows: tuple[FormedRow, ...],
) -> str:
    parts: list[str] = []
    for neighbor, incoming, outgoing, split, read in rows:
        parts.append(
            f"{neighbor} M={lockset_display(incoming)} "
            f"O={lockset_display(outgoing)} split={split} "
            f"neighbor-read={read}"
        )
    return ", ".join(parts)


def new_six_neighbors(
    site: Point,
    ticks: dict[Point, int],
    offset: int,
) -> tuple[Point, ...]:
    formed_tick = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if ticks.get(neighbor) == formed_tick + offset:
            found.append(neighbor)
    return tuple(found)


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
        "neighbor-read of 1-in 2-out split reverse/face composition t+1 versus t+2 "
        "on same-lock z-probes"
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E3, E2) == PAIR2
        and neg(E1) == NEG_E1
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "split-identity",
        axis_split(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_split(frozenset({E1}), UNDEFINED) == UNDEFINED
        and axis_split(frozenset(), frozenset({E2, E3})) == "fail"
        and axis_split(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and axis_split(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1})) == "fail"
        and two_in_one_out(frozenset({E2, E3, NEG_E3}), frozenset({E1, NEG_E1}))
        == "hold",
    )
    checks.check(
        "pair-read-identity",
        pair_read(UNDEFINED, "hold") == UNDEFINED
        and pair_read("hold", UNDEFINED) == UNDEFINED
        and pair_read("hold", "hold") == "hold"
        and pair_read("hold", "fail") == "fail"
        and pair_read("fail", "hold") == "fail"
        and pair_read("fail", "fail") == "fail",
    )
    checks.check(
        "neighbor-read-identity",
        neighbor_read(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and matching_neighbors(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and incoming_set(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and outgoing_set(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and axis_split(UNDEFINED, UNDEFINED) == UNDEFINED,
    )
    checks.check(
        "composition-identity",
        composition_report(
            {"A": UNDEFINED, "B": "hold", "C": "hold", "D": "hold"},
            {"A": "hold", "B": "hold", "C": "hold", "D": "hold"},
        )
        == UNDEFINED
        and composition_report(
            {"A": "hold", "B": "hold", "C": "hold", "D": "fail"},
            {"A": "hold", "B": "hold", "C": "hold", "D": "hold"},
        )
        == "fail"
        and composition_report(
            {"A": "fail", "B": "hold", "C": "hold", "D": "hold"},
            {"A": "fail", "B": "hold", "C": "hold", "D": "hold"},
        )
        == "hold",
    )

    ticks, locks, seed_map = form()
    twosite_ticks, twosite_locks, twosite_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    sl2_ticks, sl2_locks, sl2_seeds = form(SAME_LOCK_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)

    tau1: dict[str, int] = {}
    tau2: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    m2: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    o2: dict[str, Outgoing] = {}
    split1: dict[str, str] = {}
    split2: dict[str, str] = {}
    reads1: dict[str, str] = {}
    reads2: dict[str, str] = {}
    reads_m1: dict[str, str] = {}
    reads_o1: dict[str, str] = {}
    reads_signed1: dict[str, str] = {}
    matches1: dict[str, tuple[Point, ...] | str] = {}
    matches2: dict[str, tuple[Point, ...] | str] = {}
    formed1: dict[str, tuple[FormedRow, ...]] = {}
    formed2: dict[str, tuple[FormedRow, ...]] = {}
    new1: dict[str, tuple[Point, ...]] = {}
    new2: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau1[name] = ticks[site] + 1
        tau2[name] = ticks[site] + 2
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        m2[name] = incoming_set(site, tau2[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        o2[name] = outgoing_set(site, tau2[name], ticks, locks, seed_map)
        split1[name] = axis_split(m1[name], o1[name])
        split2[name] = axis_split(m2[name], o2[name])
        reads1[name] = neighbor_read(site, tau1[name], ticks, locks, seed_map)
        reads2[name] = neighbor_read(site, tau2[name], ticks, locks, seed_map)
        reads_m1[name] = neighbor_read_incoming(
            site, tau1[name], ticks, locks, seed_map
        )
        reads_o1[name] = neighbor_read_outgoing(
            site, tau1[name], ticks, locks, seed_map
        )
        reads_signed1[name] = signed_pair_read(
            site, tau1[name], ticks, locks, seed_map
        )
        matches1[name] = matching_neighbors(
            site, tau1[name], ticks, locks, seed_map
        )
        matches2[name] = matching_neighbors(
            site, tau2[name], ticks, locks, seed_map
        )
        formed1[name] = formed_neighbor_rows(
            site, tau1[name], ticks, locks, seed_map
        )
        formed2[name] = formed_neighbor_rows(
            site, tau2[name], ticks, locks, seed_map
        )
        new1[name] = new_six_neighbors(site, ticks, 1)
        new2[name] = new_six_neighbors(site, ticks, 2)
        print(
            f"{name} t={ticks[site]} "
            f"M1={lockset_display(m1[name])} "
            f"O1={lockset_display(o1[name])} "
            f"split1={split1[name]} "
            f"neighbor-read1={reads1[name]} "
            f"split2={split2[name]} "
            f"neighbor-read2={reads2[name]}"
        )

    reverse1 = reverse_report(reads1["A"], reads1["B"])
    reverse2 = reverse_report(reads2["A"], reads2["B"])
    face1 = face_report(reads1["C"], reads1["D"])
    face2 = face_report(reads2["C"], reads2["D"])
    composition = composition_report(reads1, reads2)
    split_comp = composition_report(split1, split2)
    m_reverse = reverse_report(reads_m1["A"], reads_m1["B"])
    m_face = face_report(reads_m1["C"], reads_m1["D"])
    o_reverse = reverse_report(reads_o1["A"], reads_o1["B"])
    o_face = face_report(reads_o1["C"], reads_o1["D"])
    opp_reads1 = probe_reads(PROBES, opp_ticks, opp_locks, opp_seeds, plus=1)
    opp_reads2 = probe_reads(PROBES, opp_ticks, opp_locks, opp_seeds, plus=2)
    opp_reverse1 = reverse_report(opp_reads1["A"], opp_reads1["B"])
    opp_face1 = face_report(opp_reads1["C"], opp_reads1["D"])
    opp_comp = composition_report(opp_reads1, opp_reads2)
    y_reads1 = probe_reads(Y_PROBES, ticks, locks, seed_map, plus=1)
    y_reads2 = probe_reads(Y_PROBES, ticks, locks, seed_map, plus=2)
    x_reads1 = probe_reads(X_PROBES, ticks, locks, seed_map, plus=1)
    x_reads2 = probe_reads(X_PROBES, ticks, locks, seed_map, plus=2)
    y_reverse = reverse_report(y_reads1["A"], y_reads1["B"])
    y_face = face_report(y_reads1["C"], y_reads1["D"])
    y_comp = composition_report(y_reads1, y_reads2)
    x_reverse = reverse_report(x_reads1["A"], x_reads1["B"])
    x_face = face_report(x_reads1["C"], x_reads1["D"])
    x_comp = composition_report(x_reads1, x_reads2)
    one_reads1 = probe_reads(
        PROBES, twosite_ticks, twosite_locks, twosite_seeds, plus=1
    )
    one_reads2 = probe_reads(
        PROBES, twosite_ticks, twosite_locks, twosite_seeds, plus=2
    )
    one_reverse = reverse_report(one_reads1["A"], one_reads1["B"])
    one_face = face_report(one_reads1["C"], one_reads1["D"])
    one_comp = composition_report(one_reads1, one_reads2)
    perp_reads1 = probe_reads(PROBES, perp_ticks, perp_locks, perp_seeds, plus=1)
    zsym_reads1 = probe_reads(PROBES, zsym_ticks, zsym_locks, zsym_seeds, plus=1)
    sl2_reads1 = probe_reads(PROBES, sl2_ticks, sl2_locks, sl2_seeds, plus=1)
    print(
        f"neighbor-read reverse1={reverse1} reverse2={reverse2} "
        f"face1={face1} face2={face2} composition={composition}"
    )
    print(
        f"M neighbor-read reverse={m_reverse} face={m_face} "
        f"A={reads_m1['A']} B={reads_m1['B']}"
    )
    print(
        f"O neighbor-read reverse={o_reverse} face={o_face} "
        f"A={reads_o1['A']} B={reads_o1['B']}"
    )
    print(
        "per_element: each 1-in 2-out axis assignment of M and O at a probe "
        "and at formed 6-NN, compared as unsigned axes at the probe's t+1 and t+2"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four neighbor-read reports at two cuts, reverse/face at "
        "each cut, composition of the bits"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
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
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["D"], 0, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(PAIR2, 1, ticks, locks, seed_map) == frozenset({E2})
        and m1["A"] == frozenset({E2}),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    empty: Incoming = frozenset()
    checks.check(
        "theorem1-M-O-split-both-cuts",
        m1["A"] == frozenset({E2})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E3})
        and m1["D"] == frozenset({E1})
        and o1["A"] == frozenset({E1, NEG_E1, E2, E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, NEG_E2})
        and o1["D"] == frozenset({NEG_E2, E3, NEG_E3})
        and split1["A"] == "fail"
        and split1["B"] == "hold"
        and split1["C"] == "hold"
        and split1["D"] == "hold"
        and m2["A"] == m1["A"]
        and m2["B"] == m1["B"]
        and m2["C"] == m1["C"]
        and m2["D"] == m1["D"]
        and o2["A"] == o1["A"]
        and o2["B"] == o1["B"]
        and o2["C"] == o1["C"]
        and o2["D"] == o1["D"]
        and split2 == split1,
        str(
            {
                name: (
                    lockset_display(m1[name]),
                    lockset_display(o1[name]),
                    split1[name],
                )
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-neighbor-read-bits-both-cuts",
        reads1["A"] == "fail"
        and reads1["B"] == "hold"
        and reads1["C"] == "hold"
        and reads1["D"] == "hold"
        and reads2["A"] == "fail"
        and reads2["B"] == "hold"
        and reads2["C"] == "hold"
        and reads2["D"] == "hold"
        and matches1["A"] == ()
        and matches1["B"] == ((1, 0, 1),)
        and matches1["C"] == ((0, 1, 2),)
        and matches1["D"] == ((1, 1, 1),)
        and matches2["A"] == matches1["A"]
        and matches2["B"] == matches1["B"]
        and matches2["C"] == matches1["C"]
        and matches2["D"] == matches1["D"],
        str(
            {
                name: (reads1[name], reads2[name], matches1[name])
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-formed-6nn-A-both-cuts",
        formed1["A"]
        == (
            ((1, 0, 1), frozenset({E1}), empty, "fail", "fail"),
            ((-1, 0, 1), frozenset({NEG_E1}), empty, "fail", "fail"),
            (
                (0, 1, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E3}),
                "hold",
                "fail",
            ),
            ((0, -1, 1), UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED),
            ((0, 0, 2), frozenset({E3}), empty, "fail", "fail"),
            (
                (0, 0, 0),
                frozenset({E1}),
                frozenset({NEG_E2, NEG_E3}),
                "hold",
                "hold",
            ),
        )
        and formed2["A"]
        == (
            (
                (1, 0, 1),
                frozenset({E1}),
                frozenset({NEG_E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            (
                (-1, 0, 1),
                frozenset({NEG_E1}),
                frozenset({NEG_E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            (
                (0, 1, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E3}),
                "hold",
                "fail",
            ),
            ((0, -1, 1), frozenset({E3}), frozenset({E2}), "fail", "fail"),
            (
                (0, 0, 2),
                frozenset({E3}),
                frozenset({E1, NEG_E1, NEG_E2}),
                "hold",
                "hold",
            ),
            (
                (0, 0, 0),
                frozenset({E1}),
                frozenset({NEG_E2, NEG_E3}),
                "hold",
                "hold",
            ),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-BCD-tau1",
        formed1["B"]
        == (
            ((2, 1, 1), UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED),
            (
                (0, 1, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E3}),
                "hold",
                "fail",
            ),
            ((1, 2, 1), frozenset({E2}), empty, "fail", "fail"),
            (
                (1, 0, 1),
                frozenset({E1}),
                frozenset({NEG_E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            ((1, 1, 2), frozenset({E1, E3}), empty, "fail", "fail"),
            ((1, 1, 0), frozenset({NEG_E3}), empty, "fail", "fail"),
        )
        and formed1["C"]
        == (
            ((1, 0, 2), frozenset({E1, E3}), empty, "fail", "fail"),
            ((-1, 0, 2), frozenset({NEG_E1, E3}), empty, "fail", "fail"),
            (
                (0, 1, 2),
                frozenset({E3}),
                frozenset({E1, NEG_E1, E2}),
                "hold",
                "hold",
            ),
            ((0, -1, 2), frozenset({NEG_E2}), empty, "fail", "fail"),
            (
                (0, 0, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E2, E3}),
                "fail",
                "fail",
            ),
        )
        and formed1["D"]
        == (
            ((2, 0, 1), UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED),
            (
                (0, 0, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E2, E3}),
                "fail",
                "fail",
            ),
            (
                (1, 1, 1),
                frozenset({E1}),
                frozenset({E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            ((1, -1, 1), frozenset({NEG_E2}), empty, "fail", "fail"),
            ((1, 0, 2), frozenset({E1, E3}), empty, "fail", "fail"),
            ((1, 0, 0), frozenset({NEG_E3}), empty, "fail", "fail"),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-BCD-tau2",
        formed2["B"]
        == (
            ((2, 1, 1), UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED),
            (
                (0, 1, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E3}),
                "hold",
                "fail",
            ),
            (
                (1, 2, 1),
                frozenset({E2}),
                frozenset({E1, E3}),
                "hold",
                "fail",
            ),
            (
                (1, 0, 1),
                frozenset({E1}),
                frozenset({NEG_E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            (
                (1, 1, 2),
                frozenset({E1, E3}),
                frozenset({E1, E2}),
                "fail",
                "fail",
            ),
            ((1, 1, 0), frozenset({NEG_E3}), frozenset({E1}), "fail", "fail"),
        )
        and formed2["C"]
        == (
            (
                (1, 0, 2),
                frozenset({E1, E3}),
                frozenset({E1, NEG_E2}),
                "fail",
                "fail",
            ),
            (
                (-1, 0, 2),
                frozenset({NEG_E1, E3}),
                frozenset({NEG_E1, NEG_E2}),
                "fail",
                "fail",
            ),
            (
                (0, 1, 2),
                frozenset({E3}),
                frozenset({E1, NEG_E1, E2}),
                "hold",
                "hold",
            ),
            (
                (0, -1, 2),
                frozenset({NEG_E2}),
                frozenset({E1, NEG_E1}),
                "fail",
                "fail",
            ),
            (
                (0, 0, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E2, E3}),
                "fail",
                "fail",
            ),
        )
        and formed2["D"]
        == (
            ((2, 0, 1), UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED),
            (
                (0, 0, 1),
                frozenset({E2}),
                frozenset({E1, NEG_E1, E2, E3}),
                "fail",
                "fail",
            ),
            (
                (1, 1, 1),
                frozenset({E1}),
                frozenset({E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            (
                (1, -1, 1),
                frozenset({NEG_E2}),
                frozenset({E1, E3}),
                "hold",
                "fail",
            ),
            (
                (1, 0, 2),
                frozenset({E1, E3}),
                frozenset({E1, NEG_E2}),
                "fail",
                "fail",
            ),
            ((1, 0, 0), frozenset({NEG_E3}), frozenset({E1}), "fail", "fail"),
        ),
    )
    checks.check(
        "theorem1-new-6nn",
        new1["A"] == ((1, 0, 1), (-1, 0, 1), (0, 0, 2))
        and new1["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new1["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new1["D"] == ((1, -1, 1), (1, 0, 2), (1, 0, 0))
        and new2["A"] == ((0, -1, 1),)
        and new2["B"] == ()
        and new2["C"] == ()
        and new2["D"] == (),
    )
    d_at_a_tau = neighbor_read((1, 0, 1), tau1["A"], ticks, locks, seed_map)
    checks.check(
        "theorem1-split-fail-is-fail-not-undefined",
        axis_split(
            incoming_set((1, 0, 1), tau1["A"], ticks, locks, seed_map),
            outgoing_set((1, 0, 1), tau1["A"], ticks, locks, seed_map),
        )
        == "fail"
        and d_at_a_tau == "fail"
        and d_at_a_tau != UNDEFINED
        and reads1["A"] == "fail"
        and reads1["A"] != UNDEFINED
        and split1["A"] == "fail"
        and neighbor_read((0, -1, 1), tau1["A"], ticks, locks, seed_map)
        == UNDEFINED
        and neighbor_read((0, -1, 1), tau2["A"], ticks, locks, seed_map)
        == "fail",
    )
    checks.check(
        "theorem1-axis-match-not-signed-sets",
        m1["A"] == frozenset({E2})
        and incoming_set(PAIR2, tau1["A"], ticks, locks, seed_map)
        == frozenset({E2})
        and axis_split(
            incoming_set(PAIR2, tau1["A"], ticks, locks, seed_map),
            outgoing_set(PAIR2, tau1["A"], ticks, locks, seed_map),
        )
        == "hold"
        and neighbor_read(PAIR2, tau1["A"], ticks, locks, seed_map) == "fail"
        and neighbor_read(PAIR2, tau2["A"], ticks, locks, seed_map) == "fail"
        and o1["B"] != o1["D"]
        and axis_set(o1["B"]) == axis_set(o1["D"])
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(m1["A"]) == frozenset({E2})
        and reads1["A"] == "fail"
        and reads1["B"] == "hold"
        and reads1["D"] == "hold",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and m1["A"] == frozenset({E2})
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {E2}
        and PAIR2 in seed_map
        and seed_map[PAIR2] == E2,
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 4
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 3
        and unique_letter(o1["D"]) == UNDEFINED
        and split1["A"] == "fail"
        and reads1["A"] == "fail"
        and reads1["D"] == "hold",
    )
    checks.check(
        "theorem2-reverse-fail-both-cuts",
        reverse1 == "fail"
        and reverse2 == "fail"
        and reads1["A"] == "fail"
        and reads1["B"] == "hold"
        and reads2["A"] == "fail"
        and reads2["B"] == "hold"
        and reverse1 != UNDEFINED
        and reverse2 != UNDEFINED
        and reverse1 != "hold"
        and reverse2 != "hold",
    )
    checks.check(
        "theorem2-face-hold-both-cuts",
        face1 == "hold"
        and face2 == "hold"
        and reads1["C"] == "hold"
        and reads1["D"] == "hold"
        and reads2["C"] == "hold"
        and reads2["D"] == "hold"
        and face1 != UNDEFINED
        and face2 != UNDEFINED
        and face1 != "fail"
        and face2 != "fail",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and reads1["A"] == reads2["A"]
        and reads1["B"] == reads2["B"]
        and reads1["C"] == reads2["C"]
        and reads1["D"] == reads2["D"]
        and composition != UNDEFINED
        and composition != "fail"
        and split_comp == "hold"
        and reverse1 == reverse2
        and face1 == face2,
    )
    checks.check(
        "mutation-signed-pair-fails",
        reads_signed1["A"] == "fail"
        and reads_signed1["B"] == "fail"
        and reads_signed1["C"] == "fail"
        and reads_signed1["D"] == "fail"
        and reverse1 == "fail"
        and face1 == "hold",
    )
    checks.check(
        "mutation-M-read-differs",
        reads_m1["A"] == "hold"
        and reads_m1["B"] == "hold"
        and reads_m1["C"] == "hold"
        and reads_m1["D"] == "hold"
        and reads1["A"] == "fail"
        and reverse1 == "fail"
        and m_reverse == "hold"
        and m_reverse != reverse1
        and m_face == "hold",
    )
    checks.check(
        "mutation-O-read-differs",
        reads_o1["A"] == "fail"
        and reads_o1["B"] == "fail"
        and reads_o1["C"] == "fail"
        and reads_o1["D"] == "fail"
        and reads1["C"] == "hold"
        and reads1["D"] == "hold"
        and reverse1 == "fail"
        and face1 == "hold"
        and o_face == "fail"
        and o_face != face1,
    )
    checks.check(
        "compare-opposite-z-split-neighbor-read",
        opp_reads1["A"] == "hold"
        and opp_reads1["B"] == "hold"
        and opp_reads1["C"] == "hold"
        and opp_reads1["D"] == "hold"
        and opp_reverse1 == "hold"
        and opp_face1 == "hold"
        and opp_comp == "hold"
        and reverse1 == "fail"
        and opp_reverse1 != reverse1
        and TWO_AXIS_OPP_SEEDS != TWO_AXIS_SEEDS,
    )
    checks.check(
        "compare-1-axis-z-split-neighbor-read",
        twosite_ticks[PROBES["A"]] == 1
        and twosite_ticks[PROBES["C"]] == 4
        and ticks[PROBES["A"]] == 0
        and one_reads1["C"] == "fail"
        and one_reverse == "hold"
        and one_face == "fail"
        and one_comp == "hold"
        and face1 == "hold"
        and one_face != face1,
    )
    checks.check(
        "not-x-probes-or-y-probes-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and y_reads1["C"] == "fail"
        and y_reads1["D"] == "fail"
        and y_reverse == "hold"
        and y_face == "fail"
        and y_comp == "hold"
        and x_reads1["A"] == "fail"
        and x_reads1["D"] == "fail"
        and x_reverse == "fail"
        and x_face == "fail"
        and x_comp == "hold"
        and reverse1 == "fail"
        and face1 == "hold"
        and y_reverse != reverse1
        and y_face != face1
        and x_face != face1,
    )
    checks.check(
        "not-nsopp-leftover-second-pair-is-seed",
        TWO_AXIS_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_AXIS_SEEDS != SAME_LOCK_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in twosite_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and twosite_ticks[E3] == 1
        and twosite_locks[E3] == {E3}
        and one_reverse == "hold"
        and one_face == "fail"
        and reverse1 == "fail"
        and face1 == "hold"
        and zsym_reads1["A"] == "fail"
        and zsym_reads1["C"] == "fail"
        and reverse_report(sl2_reads1["A"], sl2_reads1["B"]) == "hold"
        and face_report(sl2_reads1["C"], sl2_reads1["D"]) == "fail"
        and reverse_report(perp_reads1["A"], perp_reads1["B"]) == "fail"
        and face_report(perp_reads1["C"], perp_reads1["D"]) == "fail"
        and PAIR2 in seed_map
        and PAIR2 not in twosite_seeds
        and twosite_ticks[PAIR2] == 1
        and PAIR2 not in new1["A"],
    )
    checks.check(
        "O-is-not-M",
        o1["A"] != m1["A"] and E2 in m1["A"] and E2 in o1["A"],
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-split-neighbor-read-both-cuts",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=1" in note
        and "M(A, τ1) = {+e_2}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_3}" in note
        and "M(D, τ1) = {+e_1}" in note
        and "O(A, τ1) = {+e_1, \u2212e_1, +e_2, +e_3}" in note
        and "O(B, τ1) = {+e_2, +e_3, \u2212e_3}" in note
        and "O(C, τ1) = {+e_1, \u2212e_1, \u2212e_2}" in note
        and "O(D, τ1) = {\u2212e_2, +e_3, \u2212e_3}" in note
        and "split(A, τ1) = fail" in note
        and "split(B, τ1) = hold" in note
        and "split(C, τ1) = hold" in note
        and "split(D, τ1) = hold" in note
        and "neighbor-read(A, τ1) = fail" in note
        and "neighbor-read(B, τ1) = hold" in note
        and "neighbor-read(C, τ1) = hold" in note
        and "neighbor-read(D, τ1) = hold" in note
        and "neighbor-read(A, τ2) = fail" in note
        and "neighbor-read(B, τ2) = hold" in note
        and "neighbor-read(C, τ2) = hold" in note
        and "neighbor-read(D, τ2) = hold" in note
        and "split(A, τ2) = fail" in note
        and "M(A, τ2) = {+e_2}" in note
        and "O(D, τ2) = {\u2212e_2, +e_3, \u2212e_3}" in note
        and "O(A, τ2) = {+e_1, \u2212e_1, +e_2, +e_3}" in note,
    )
    checks.check(
        "note-reports-formed-neighbors-both-cuts",
        "formed 6-NN of A at τ1: " + formed_line(formed1["A"]) in note
        and "formed 6-NN of B at τ1: " + formed_line(formed1["B"]) in note
        and "formed 6-NN of C at τ1: " + formed_line(formed1["C"]) in note
        and "formed 6-NN of D at τ1: " + formed_line(formed1["D"]) in note
        and "formed 6-NN of A at τ2: " + formed_line(formed2["A"]) in note
        and "formed 6-NN of B at τ2: " + formed_line(formed2["B"]) in note
        and "formed 6-NN of C at τ2: " + formed_line(formed2["C"]) in note
        and "formed 6-NN of D at τ2: " + formed_line(formed2["D"]) in note
        and "matching 6-NN of A at τ1: none" in note
        and "matching 6-NN of B at τ1: (1, 0, 1)" in note
        and "matching 6-NN of C at τ1: (0, 1, 2)" in note
        and "matching 6-NN of D at τ1: (1, 1, 1)" in note
        and "matching 6-NN of A at τ2: none" in note
        and "matching 6-NN of B at τ2: (1, 0, 1)" in note
        and "matching 6-NN of C at τ2: (0, 1, 2)" in note
        and "matching 6-NN of D at τ2: (1, 1, 1)" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)" in note
        and "new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)" in note
        and "new 6-NN of A at t(A)+2: (0, -1, 1)" in note
        and "new 6-NN of B at t(B)+2: none" in note
        and "new 6-NN of C at t(C)+2: none" in note
        and "new 6-NN of D at t(D)+2: none" in note,
    )
    checks.check(
        "note-reports-reverse-face-composition",
        "Reverse neighbor-read at τ1: fail" in note
        and "Reverse neighbor-read at τ2: fail" in note
        and "Face neighbor-read at τ1: hold" in note
        and "Face neighbor-read at τ2: hold" in note
        and "Composition of neighbor-read: hold" in note
        and "Reverse fails at τ1 and at τ2." in note
        and "Face holds at τ1 and at τ2." in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-one-cut-or-M-read-leftover",
        "not leftover of nm2sreadslz one-cut" in normalized_note
        and "not leftover of nm2sl12z 1-in 2-out split without neighbor-read"
        in normalized_note
        and "not leftover of nm2splt2slz split composition" in normalized_note
        and "not leftover of nm2readslz neighbor-read of M" in normalized_note
        and "not leftover of nm2oreadslz neighbor-read of O" in normalized_note
        and "not leftover of signed (M, O) set equality" in normalized_note
        and "not leftover of nm2sreadt2z" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ1(q)=t(q)+1" in note.replace(" ", "")
        and "τ2(q)=t(q)+2" in note.replace(" ", ""),
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "{n:n·n<=9}" in note.replace(" ", "")
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "Occupancy of sites is not used" in note
        and "neighbor-read" in normalized_note,
    )
    checks.check(
        "note-uniqueness-not-required",
        "Uniqueness is not required." in normalized_note
        and "Mixed remains a set." in note,
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
        all(line in allowed_retained for line in allowed_retained)
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_NEIGHBOR_READ_ONE_TWO_SPLIT_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "axis_set" in defined_fns
        and "axis_cover" in defined_fns
        and "axis_split" in defined_fns
        and "neighbor_read" in defined_fns
        and "matching_neighbors" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "composition_report" in defined_fns
        and "formed_neighbor_rows" in defined_fns
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
        "split-neighbor-read-not-leftover-of-M-or-O",
        reverse1 == "fail"
        and face1 == "hold"
        and composition == "hold"
        and reads1["A"] == "fail"
        and reads2["A"] == "fail"
        and reads_m1["A"] == "hold"
        and reads_o1["B"] == "fail"
        and opp_reverse1 == "hold"
        and one_face == "fail",
    )
    _ = (
        match_display,
        x_reads2,
        y_reads2,
        ysym_ticks,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
