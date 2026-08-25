#!/usr/bin/env python3
"""Neighbor-read of the 1-in 2-out split at t+1 reverse/face on same-lock x.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint same-lock pairs: origin locks +e_1, (0,1,0) locks +e_1,
(0,0,1) locks +e_2, (0,1,1) locks +e_2. Same process and x-probes as nm2slx.
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. t(q) is the formation tick. tau = t(q)+1. M, O, and split are
as nm2sl12. Unformed at tau => UNDEFINED. Neighbor-read of split HOLDs at
q iff split HOLDs at q and some formed 6-NN r has split HOLD and
Axis(M(r, tau)) = Axis(M(q, tau)) and Axis(O(r, tau)) = Axis(O(q, tau)).
If split fails at q, neighbor-read fails, not UNDEFINED. Uniqueness is not
required. Reverse HOLDs iff neighbor-read at A and at B. Face likewise on
C, D. Occupancy of sites is not used. Named-sign lettering is not used.
No larger host. This is not leftover of neighbor-read of M, not leftover of
neighbor-read of O, not leftover of signed (M, O) set equality, not
leftover of nm2sl12 1-in 2-out split without neighbor-read, not leftover
of nm2sreadz, and not leftover of nm2sreadslz. Displayed, not adopted.
Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_NEIGHBOR_READ_ONE_TWO_SPLIT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_NEIGHBOR_READ_ONE_TWO_SPLIT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
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
ONE_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
NNSEED_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
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
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Neighbor-read of the 1-in 2-out split at t+1 on the four x-probes of the "
    "two-axis same-lock seed, and reverse/face from that, are reported. "
    "Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_SAME_SEEDS,
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
    """HOLD iff cover HOLD and |Axis(M)|=1 (hence |Axis(O)|=2).

    2-in 1-out (cover HOLD with |Axis(M)|=2) is fail of this object, not
    UNDEFINED.
    """
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
) -> tuple[tuple[Point, Incoming, Outgoing, str, str], ...]:
    """M, O, split, neighbor-read at each eventually-formed 6-NN, same tau."""
    rows: list[tuple[Point, Incoming, Outgoing, str, str]] = []
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


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def probe_reads(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = neighbor_read(
            site,
            site_ticks[site] + 1,
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
    rows: tuple[tuple[Point, Incoming, Outgoing, str, str], ...],
) -> str:
    parts: list[str] = []
    for neighbor, incoming, outgoing, split, read in rows:
        parts.append(
            f"{neighbor} M={lockset_display(incoming)} "
            f"O={lockset_display(outgoing)} split={split} "
            f"neighbor-read={read}"
        )
    return ", ".join(parts)


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

    print("neighbor-read of 1-in 2-out split reverse/face at t+1 on same-lock x-probes")
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E2, E3) == PAIR2
        and neg(E1) == NEG_E1
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
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
        and axis_split(UNDEFINED, UNDEFINED) == UNDEFINED
        and axis_split(frozenset({E1}), frozenset({E2, NEG_E3})) == "hold"
        and axis_split(frozenset({E1, E2}), frozenset({E3})) == "fail"
        and axis_split(frozenset({E1}), frozenset({E2})) == "fail",
    )

    ticks, locks, seed_map = form()
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SAME_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(NSOPP_SEEDS)
    nnseed_ticks, nnseed_locks, nnseed_seeds = form(NNSEED_SEEDS)

    tau1: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    split: dict[str, str] = {}
    reads: dict[str, str] = {}
    reads_m: dict[str, str] = {}
    reads_o: dict[str, str] = {}
    reads_signed: dict[str, str] = {}
    matches: dict[str, tuple[Point, ...] | str] = {}
    formed: dict[str, tuple[tuple[Point, Incoming, Outgoing, str, str], ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau1[name] = ticks[site] + 1
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        split[name] = axis_split(m1[name], o1[name])
        reads[name] = neighbor_read(site, tau1[name], ticks, locks, seed_map)
        reads_m[name] = neighbor_read_incoming(
            site, tau1[name], ticks, locks, seed_map
        )
        reads_o[name] = neighbor_read_outgoing(
            site, tau1[name], ticks, locks, seed_map
        )
        reads_signed[name] = signed_pair_read(
            site, tau1[name], ticks, locks, seed_map
        )
        matches[name] = matching_neighbors(
            site, tau1[name], ticks, locks, seed_map
        )
        formed[name] = formed_neighbor_rows(
            site, tau1[name], ticks, locks, seed_map
        )
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"Axis(M)={axis_display(axis_set(m1[name]))} "
            f"Axis(O)={axis_display(axis_set(o1[name]))} "
            f"split={split[name]} "
            f"neighbor-read={reads[name]}"
        )

    reverse = reverse_report(reads["A"], reads["B"])
    face = face_report(reads["C"], reads["D"])
    print(f"neighbor-read reverse={reverse} face={face}")
    print(
        "per_element: each 1-in 2-out axis assignment of M and O at a probe "
        "and at formed 6-NN, compared as unsigned axes at the probe's t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four neighbor-read reports, reverse/face from those bits")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )


    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[ORIGIN] == 0
        and ticks[E2] == 0
        and ticks[E3] == 0
        and ticks[PAIR2] == 0
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["C"], 2, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED,
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
        "theorem1-M-O-at-tau",
        m1["A"] == frozenset({NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({NEG_E3})
        and o1["A"] == frozenset({E1})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E1}),
        str(
            {
                name: (lockset_display(m1[name]), lockset_display(o1[name]))
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    empty: Incoming = frozenset()
    checks.check(
        "theorem1-axis-split",
        axis_set(m1["A"]) == frozenset({E3})
        and axis_set(o1["A"]) == frozenset({E1})
        and axis_set(m1["B"]) == frozenset({E1})
        and axis_set(o1["B"]) == frozenset({E2, E3})
        and axis_set(m1["C"]) == frozenset({E1})
        and axis_set(o1["C"]) == frozenset({E2, E3})
        and axis_set(m1["D"]) == frozenset({E3})
        and axis_set(o1["D"]) == frozenset({E1})
        and split["A"] == "fail"
        and split["B"] == "hold"
        and split["C"] == "hold"
        and split["D"] == "fail"
        and split["A"] != UNDEFINED
        and split["D"] != UNDEFINED,
    )
    checks.check(
        "theorem1-formed-6nn-A",
        formed["A"]
        == (
            ((2, 0, 0), frozenset({E1}), empty, "fail", "fail"),
            (
                (0, 0, 0),
                frozenset({E1}),
                frozenset({NEG_E2, NEG_E3}),
                "hold",
                "hold",
            ),
            ((1, 1, 0), frozenset({NEG_E3}), frozenset({E1}), "fail", "fail"),
            (
                (1, -1, 0),
                frozenset({E1}),
                frozenset({NEG_E2, NEG_E3}),
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
                (1, 0, -1),
                frozenset({E1}),
                frozenset({NEG_E2, NEG_E3}),
                "hold",
                "hold",
            ),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-B",
        formed["B"]
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
        ),
    )
    checks.check(
        "theorem1-formed-6nn-C",
        formed["C"]
        == (
            ((1, 0, 0), frozenset({NEG_E3}), frozenset({E1}), "fail", "fail"),
            (
                (2, 1, 0),
                frozenset({E1}),
                frozenset({E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            ((2, -1, 0), frozenset({NEG_E2, NEG_E3}), empty, "fail", "fail"),
            ((2, 0, 1), frozenset({E2, E3, NEG_E3}), empty, "fail", "fail"),
            ((2, 0, -1), frozenset({NEG_E3}), empty, "fail", "fail"),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-D",
        formed["D"]
        == (
            ((2, 1, 0), frozenset({E1}), empty, "fail", "fail"),
            (
                (0, 1, 0),
                frozenset({E1}),
                frozenset({E2, NEG_E3}),
                "hold",
                "hold",
            ),
            ((1, 2, 0), frozenset({E1}), frozenset({NEG_E3}), "fail", "fail"),
            ((1, 0, 0), frozenset({NEG_E3}), frozenset({E1}), "fail", "fail"),
            (
                (1, 1, 1),
                frozenset({E1}),
                frozenset({E2, E3, NEG_E3}),
                "hold",
                "hold",
            ),
            (
                (1, 1, -1),
                frozenset({E1}),
                frozenset({E2, NEG_E3}),
                "hold",
                "hold",
            ),
        ),
    )
    checks.check(
        "theorem1-neighbor-read-bits",
        reads["A"] == "fail"
        and reads["B"] == "hold"
        and reads["C"] == "hold"
        and reads["D"] == "fail"
        and matches["A"] == ()
        and matches["B"] == ((1, 0, 1),)
        and matches["C"] == ((2, 1, 0),)
        and matches["D"] == (),
        str({name: (reads[name], matches[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-split-fail-is-fail-not-undefined",
        split["A"] == "fail"
        and reads["A"] == "fail"
        and reads["A"] != UNDEFINED
        and split["D"] == "fail"
        and reads["D"] == "fail"
        and reads["D"] != UNDEFINED
        and neighbor_read(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read((3, 0, 0), tau1["C"], ticks, locks, seed_map)
        == UNDEFINED
        and in_ball((3, 0, 0))
        and (3, 0, 0) not in ticks,
    )
    checks.check(
        "theorem1-split-hold-without-neighbor-is-fail-not-undefined",
        split["C"] == "hold"
        and reads["C"] == "hold"
        and axis_split(
            incoming_set((1, -1, 0), tau1["A"], ticks, locks, seed_map),
            outgoing_set((1, -1, 0), tau1["A"], ticks, locks, seed_map),
        )
        == "hold"
        and neighbor_read((1, -1, 0), tau1["A"], ticks, locks, seed_map)
        == "fail"
        and neighbor_read((1, -1, 0), tau1["A"], ticks, locks, seed_map)
        != UNDEFINED
        and axis_split(
            incoming_set((0, 1, 1), tau1["B"], ticks, locks, seed_map),
            outgoing_set((0, 1, 1), tau1["B"], ticks, locks, seed_map),
        )
        == "hold"
        and neighbor_read((0, 1, 1), tau1["B"], ticks, locks, seed_map)
        == "fail",
    )
    checks.check(
        "theorem1-axis-match-not-signed-sets",
        m1["B"] == frozenset({E1})
        and incoming_set((1, 0, 1), tau1["B"], ticks, locks, seed_map)
        == frozenset({E1})
        and o1["B"] != outgoing_set((1, 0, 1), tau1["B"], ticks, locks, seed_map)
        and axis_set(o1["B"])
        == axis_set(outgoing_set((1, 0, 1), tau1["B"], ticks, locks, seed_map))
        and o1["C"] != outgoing_set((2, 1, 0), tau1["C"], ticks, locks, seed_map)
        and axis_set(o1["C"])
        == axis_set(outgoing_set((2, 1, 0), tau1["C"], ticks, locks, seed_map))
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(m1["A"]) == frozenset({NEG_E3})
        and unique_letter(o1["A"]) == frozenset({E1})
        and reads["B"] == "hold"
        and reads["C"] == "hold"
        and reads_signed["B"] == "fail"
        and reads_signed["C"] == "fail",
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and m1["A"] == frozenset({NEG_E3})
        and ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse == "fail"
        and reads["A"] == "fail"
        and reads["B"] == "hold"
        and reverse != UNDEFINED
        and reverse != "hold",
        reverse,
    )
    checks.check(
        "theorem3-face-fail",
        face == "fail"
        and reads["C"] == "hold"
        and reads["D"] == "fail"
        and face != UNDEFINED
        and face != "hold"
        and split["C"] == "hold",
        face,
    )
    checks.check(
        "mutation-signed-pair-fails",
        reads_signed["A"] == "fail"
        and reads_signed["B"] == "fail"
        and reads_signed["C"] == "fail"
        and reads_signed["D"] == "fail"
        and reverse == "fail"
        and face == "fail",
    )
    checks.check(
        "mutation-M-read-differs",
        reads_m["A"] == "hold"
        and reads_m["B"] == "hold"
        and reads_m["C"] == "hold"
        and reads_m["D"] == "hold"
        and reads["A"] == "fail"
        and reads["D"] == "fail"
        and reverse_report(reads_m["A"], reads_m["B"]) == "hold"
        and face_report(reads_m["C"], reads_m["D"]) == "hold"
        and reverse == "fail"
        and face == "fail",
    )
    checks.check(
        "mutation-O-read-differs",
        reads_o["A"] == "hold"
        and reads_o["B"] == "fail"
        and reads_o["C"] == "fail"
        and reads_o["D"] == "hold"
        and reads["B"] == "hold"
        and reads["C"] == "hold"
        and reverse_report(reads_o["A"], reads_o["B"]) == "fail"
        and face_report(reads_o["C"], reads_o["D"]) == "fail"
        and reverse == "fail"
        and face == "fail",
    )
    y_reads = probe_reads(Y_PROBES, ticks, locks, seed_map)
    z_reads = probe_reads(Z_PROBES, ticks, locks, seed_map)
    opp_reads = probe_reads(PROBES, opp_ticks, opp_locks, opp_seeds)
    one_reads = probe_reads(PROBES, one_ticks, one_locks, one_seeds)
    nsopp_reads = probe_reads(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    nnseed_reads = probe_reads(
        PROBES, nnseed_ticks, nnseed_locks, nnseed_seeds
    )
    y_reverse = reverse_report(y_reads["A"], y_reads["B"])
    y_face = face_report(y_reads["C"], y_reads["D"])
    z_reverse = reverse_report(z_reads["A"], z_reads["B"])
    z_face = face_report(z_reads["C"], z_reads["D"])
    opp_reverse = reverse_report(opp_reads["A"], opp_reads["B"])
    opp_face = face_report(opp_reads["C"], opp_reads["D"])
    one_reverse = reverse_report(one_reads["A"], one_reads["B"])
    one_face = face_report(one_reads["C"], one_reads["D"])
    nnseed_reverse = reverse_report(nnseed_reads["A"], nnseed_reads["B"])
    nnseed_face = face_report(nnseed_reads["C"], nnseed_reads["D"])
    checks.check(
        "not-y-probes-or-z-probes-or-nnseed",
        probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and y_reads["A"] == "hold"
        and y_reads["B"] == "hold"
        and y_reverse == "hold"
        and y_face == "fail"
        and z_reads["A"] == "fail"
        and z_reads["C"] == "hold"
        and z_reads["D"] == "hold"
        and z_reverse == "fail"
        and z_face == "hold"
        and nnseed_reads["A"] == "fail"
        and nnseed_reads["B"] == "fail"
        and nnseed_reads["C"] == "fail"
        and nnseed_reads["D"] == "fail"
        and nnseed_reverse == "fail"
        and nnseed_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and y_reverse != reverse
        and z_face != face
        and nnseed_reads["B"] != reads["B"]
        and nnseed_reads["C"] != reads["C"],
    )
    opp_m_a = incoming_set(
        PROBES["A"], opp_ticks[PROBES["A"]] + 1, opp_ticks, opp_locks, opp_seeds
    )
    opp_o_d = outgoing_set(
        PROBES["D"], opp_ticks[PROBES["D"]] + 1, opp_ticks, opp_locks, opp_seeds
    )
    checks.check(
        "not-opposite-or-one-axis-or-nsopp",
        TWO_AXIS_SAME_SEEDS != TWO_AXIS_OPP_SEEDS
        and TWO_AXIS_SAME_SEEDS != ONE_AXIS_SAME_SEEDS
        and TWO_AXIS_SAME_SEEDS != NSOPP_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and ticks[PROBES["A"]] == 2
        and one_ticks[PROBES["A"]] == 3
        and ticks[PROBES["B"]] == 1
        and one_ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 3
        and one_ticks[PROBES["C"]] == 4
        and ticks[PROBES["D"]] == 2
        and one_ticks[PROBES["D"]] == 3
        and m1["A"] == frozenset({NEG_E3})
        and opp_m_a == frozenset({NEG_E3})
        and o1["D"] == frozenset({E1})
        and opp_o_d == frozenset({E1, NEG_E1})
        and incoming_set(
            PROBES["A"],
            nsopp_ticks[PROBES["A"]] + 1,
            nsopp_ticks,
            nsopp_locks,
            nsopp_seeds,
        )
        == frozenset({E2, E3, NEG_E3})
        and opp_reverse == "fail"
        and opp_face == "fail"
        and one_reverse == "fail"
        and one_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and nsopp_reads["A"] == "fail"
        and nsopp_ticks[PROBES["A"]] == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-split-nread",
        "t(A)=2" in note
        and "t(B)=1" in note
        and "t(C)=3" in note
        and "t(D)=2" in note
        and "M(A, τ) = {\u2212e_3}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_1}" in note
        and "M(D, τ) = {\u2212e_3}" in note
        and "O(A, τ) = {+e_1}" in note
        and "O(B, τ) = {+e_2, +e_3, \u2212e_3}" in note
        and "O(C, τ) = {\u2212e_2, +e_3, \u2212e_3}" in note
        and "O(D, τ) = {+e_1}" in note
        and "Axis(M)(A, τ) = {e_3}" in note
        and "Axis(O)(A, τ) = {e_1}" in note
        and "Axis(M)(B, τ) = {e_1}" in note
        and "Axis(O)(B, τ) = {e_2, e_3}" in note
        and "Axis(M)(C, τ) = {e_1}" in note
        and "Axis(O)(C, τ) = {e_2, e_3}" in note
        and "Axis(M)(D, τ) = {e_3}" in note
        and "Axis(O)(D, τ) = {e_1}" in note
        and "split(A) = fail" in note
        and "split(B) = hold" in note
        and "split(C) = hold" in note
        and "split(D) = fail" in note
        and "neighbor-read(A) = fail" in note
        and "neighbor-read(B) = hold" in note
        and "neighbor-read(C) = hold" in note
        and "neighbor-read(D) = fail" in note,
    )
    checks.check(
        "note-reports-formed-neighbors",
        "formed 6-NN of A at τ: " + formed_line(formed["A"]) in note
        and "formed 6-NN of B at τ: " + formed_line(formed["B"]) in note
        and "formed 6-NN of C at τ: " + formed_line(formed["C"]) in note
        and "formed 6-NN of D at τ: " + formed_line(formed["D"]) in note
        and "matching 6-NN of A: none" in note
        and "matching 6-NN of B: (1, 0, 1)" in note
        and "matching 6-NN of C: (2, 1, 0)" in note
        and "matching 6-NN of D: none" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse neighbor-read at τ: fail" in note
        and "Face neighbor-read at τ: fail" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-m-or-o-or-signed-leftover",
        "not leftover of nm2readslx neighbor-read of M" in normalized_note
        and "not leftover of nm2oreadslx neighbor-read of O" in normalized_note
        and "not leftover of signed (M, O) set equality" in normalized_note
        and "not leftover of nm2sl12 1-in 2-out split without neighbor-read"
        in normalized_note
        and "not leftover of nm2sreadz" in normalized_note
        and "not leftover of nm2sreadslz" in normalized_note,
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
        all(line in allowed_retained for line in allowed_retained)
        and all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/TWO_AXIS_SAME_LOCK_XPROBE_NEIGHBOR_READ_ONE_TWO_SPLIT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "axis_split" in defined_fns
        and "neighbor_read" in defined_fns
        and "matching_neighbors" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "formed_neighbor_rows" in defined_fns
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
        "neighbor-read-not-m-or-o-read",
        reverse == "fail"
        and face == "fail"
        and reads["A"] == "fail"
        and reads["B"] == "hold"
        and reads["C"] == "hold"
        and reads["D"] == "fail"
        and split["C"] == "hold"
        and reads_m["A"] == "hold"
        and reads_o["B"] == "fail"
        and reads_signed["A"] == "fail",
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
