#!/usr/bin/env python3
"""Forall-orthogonal M vs O at t+1 reverse/face on two-axis opposite x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process and x-probes as nm2axx.
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. The second pair is a new seed, not a formed child of the first
pair. t(q) is the formation tick. tau = t+1. M(q, tau) is the set of
earliest incoming nearest-neighbor steps at q using only records with tick
<= tau. O(q, tau) is the outgoing dual of M: the set of e in
{+/-e_1,+/-e_2,+/-e_3} such that q+e is formed and e is in M(q+e, tau).
Unformed => UNDEFINED. Forall-perp HOLD iff every m in M and o in O have
integer dot m·o=0. Empty or UNDEFINED => UNDEFINED. Exist-perp (some pair
dots to 0) is comparison only. nm2axx cover reverse FAIL face FAIL on these
x-probes (union misses e_2 at A and at D; axes still disjoint). Reverse
HOLD iff forall-perp at A and B. Face on C,D. Uniqueness of locks is not
required. Occupancy n is not used. Named-sign lettering is not used. No
unique P_+. No larger host. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
BALL_SQ = 9
TWO_AXIS_OPPOSITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (YZ, NEG_E2),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
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
NSPAR_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E1, NEG_E1),
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
    "Forall-orthogonal M vs O at t+1 on the four x-probes of the "
    "two-axis opposite seed, and reverse/face from that, are reported. "
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


def dots_display(pairs: tuple[tuple[Point, Point, int], ...]) -> str:
    if not pairs:
        return ""
    parts = [
        f"({LOCK_NAME[a]})·({LOCK_NAME[b]})={value}" for a, b, value in pairs
    ]
    return ", ".join(parts)


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


def integer_dots(left: Incoming, right: Incoming) -> tuple[tuple[Point, Point, int], ...]:
    """All integer dots m·o in NN order. Empty if either side is UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return ()
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("dot sides must be lock sets or UNDEFINED")
    pairs: list[tuple[Point, Point, int]] = []
    for a in NN:
        if a not in left:
            continue
        for b in NN:
            if b not in right:
                continue
            pairs.append((a, b, dot(a, b)))
    return tuple(pairs)


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
    """nm2axx leftover: {e_1,e_2,e_3} minus (Axis(M) union Axis(O))."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    return frozenset(AXES) - (axes_m | axes_o)


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    """nm2axx leftover: HOLD iff Axis(M) and Axis(O) disjoint and union is all three.

    Unformed => UNDEFINED. Empty leftover with overlapping axes fails.
    Empty O fails unless Axis(M) already equals {e_1,e_2,e_3}.
    """
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    if axes_m & axes_o:
        return "fail"
    if (axes_m | axes_o) == frozenset(AXES):
        return "hold"
    return "fail"


def forall_orthogonal(left: Incoming, right: Incoming) -> str:
    """Hold iff every m in left and o in right have integer dot m·o=0."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if dot(a, b) != 0:
                return "fail"
    return "hold"


def forall_perp(left: Incoming, right: Incoming) -> str:
    return forall_orthogonal(left, right)


def exist_perp(left: Incoming, right: Incoming) -> str:
    """Comparison only: hold iff some pair has integer dot 0."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if dot(a, b) == 0:
                return "hold"
    return "fail"


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Exist-opposite leftover: hold iff some lock in left is vector opposite of some in right."""
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


def reverse_report(status_a: str, status_b: str) -> str:
    """Reverse holds iff forall-perp at A and at B."""
    if status_a == UNDEFINED or status_b == UNDEFINED:
        return UNDEFINED
    if status_a == "hold" and status_b == "hold":
        return "hold"
    return "fail"


def face_report(status_c: str, status_d: str) -> str:
    """Face holds iff forall-perp at C and at D."""
    if status_c == UNDEFINED or status_d == UNDEFINED:
        return UNDEFINED
    if status_c == "hold" and status_d == "hold":
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


def family_at(
    probes: dict[str, Point],
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[dict[str, Incoming], dict[str, Outgoing], dict[str, str]]:
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    fp: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in ticks:
            m1[name] = UNDEFINED
            o1[name] = UNDEFINED
            fp[name] = UNDEFINED
            continue
        tau = ticks[site] + 1
        m1[name] = incoming_set(site, tau, ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau, ticks, locks, seed_map)
        fp[name] = forall_orthogonal(m1[name], o1[name])
    return m1, o1, fp


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

    print("forall-orthogonal M vs O at t+1 reverse/face on two-axis opposite x-probes")
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
        and add(E3, NEG_E3) == ZERO
        and add(E2, E3) == YZ
        and dot(E1, E2) == 0
        and dot(E1, E1) == 1
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and in_ball(YZ)
        and not in_ball((4, 0, 0)),
    )
    mixed_exist = frozenset({E1, E2})
    mixed_axis = frozenset({E2})
    checks.check(
        "forall-orthogonal-identity",
        forall_orthogonal(UNDEFINED, frozenset({E1})) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), UNDEFINED) == UNDEFINED
        and forall_orthogonal(frozenset(), frozenset({E1})) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), frozenset()) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), frozenset({E1})) == "fail"
        and forall_orthogonal(frozenset({E1}), frozenset({E2})) == "hold"
        and forall_orthogonal(mixed_exist, mixed_axis) == "fail"
        and forall_orthogonal(frozenset({NEG_E3}), frozenset({E1})) == "hold"
        and forall_perp(frozenset({E1}), frozenset({NEG_E1})) == "fail",
    )
    checks.check(
        "exist-perp-comparison-identity",
        exist_perp(UNDEFINED, frozenset({E1})) == UNDEFINED
        and exist_perp(frozenset(), frozenset({E1})) == UNDEFINED
        and exist_perp(frozenset({E1}), frozenset({E1})) == "fail"
        and exist_perp(frozenset({E1}), frozenset({E2})) == "hold"
        and exist_perp(mixed_exist, mixed_axis) == "hold"
        and exist_perp(mixed_exist, mixed_axis)
        != forall_orthogonal(mixed_exist, mixed_axis),
    )
    set_a = frozenset({NEG_E3})
    set_a_o = frozenset({E1})
    set_b = frozenset({E1})
    set_b_o = frozenset({E2, E3, NEG_E3})
    checks.check(
        "cover-is-leftover-identity",
        axis_cover(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_cover(frozenset(), frozenset({E2, E3})) == "fail"
        and axis_cover(set_a, set_a_o) == "fail"
        and axis_cover(set_b, set_b_o) == "hold"
        and leftover_axis(set_a, set_a_o) == frozenset({E2})
        and leftover_axis(set_b, set_b_o) == frozenset()
        and axis_cover(frozenset({E1}), frozenset({E1})) == "fail",
    )

    ticks, locks, seed_map = form()
    one_axis_ticks, one_axis_locks, one_axis_seeds = form(TWO_SITE_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    dots1: dict[str, tuple[tuple[Point, Point, int], ...]] = {}
    forall1: dict[str, str] = {}
    exist1: dict[str, str] = {}
    cover0: dict[str, str] = {}
    cover1: dict[str, str] = {}
    fp0: dict[str, str] = {}
    lx: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        dots1[name] = integer_dots(m1[name], o1[name])
        forall1[name] = forall_orthogonal(m1[name], o1[name])
        exist1[name] = exist_perp(m1[name], o1[name])
        cover0[name] = axis_cover(m0[name], o0[name])
        cover1[name] = axis_cover(m1[name], o1[name])
        fp0[name] = forall_orthogonal(m0[name], o0[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"dots={dots_display(dots1[name])} "
            f"forall-perp={forall1[name]} cover={cover1[name]}"
        )

    reverse_status = reverse_report(forall1["A"], forall1["B"])
    face_status = face_report(forall1["C"], forall1["D"])
    reverse0 = reverse_report(fp0["A"], fp0["B"])
    face0 = face_report(fp0["C"], fp0["D"])
    cover_reverse = reverse_report(cover1["A"], cover1["B"])
    cover_face = face_report(cover1["C"], cover1["D"])
    leftover_m_reverse = existential_opposite(m1["A"], m1["B"])
    leftover_o_reverse = existential_opposite(o1["A"], o1["B"])
    leftover_m_face = existential_opposite(m1["C"], m1["D"])
    leftover_o_face = existential_opposite(o1["C"], o1["D"])
    unique_reverse = reverse_report(
        forall_orthogonal(unique_letter(m1["A"]), unique_letter(o1["A"])),
        forall_orthogonal(unique_letter(m1["B"]), unique_letter(o1["B"])),
    )
    unique_face = face_report(
        forall_orthogonal(unique_letter(m1["C"]), unique_letter(o1["C"])),
        forall_orthogonal(unique_letter(m1["D"]), unique_letter(o1["D"])),
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(f"nm2axx cover reverse={cover_reverse} face={cover_face}")
    print(
        f"leftover exist-opposite M reverse={leftover_m_reverse} "
        f"O reverse={leftover_o_reverse} "
        f"M face={leftover_m_face} O face={leftover_o_face}"
    )
    print(
        "per_element: each integer dot m·o of earliest incoming M and outgoing O"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four M/O pairs, integer dots, forall-perp, reverse/face"
    )
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
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and second_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
        and locks[PROBES["A"]] == {NEG_E3}
        and locks[PROBES["B"]] == {E1}
        and locks[PROBES["C"]] == {E1}
        and locks[PROBES["D"]] == {NEG_E3}
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["C"], 2, ticks, locks, seed_map) == UNDEFINED
        and forall_orthogonal(
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
        "theorem1-M-at-tau",
        m1["A"] == frozenset({NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({NEG_E3})
        and m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E1})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    expected_dots = {
        "A": ((NEG_E3, E1, 0),),
        "B": (
            (E1, E2, 0),
            (E1, E3, 0),
            (E1, NEG_E3, 0),
        ),
        "C": (
            (E1, NEG_E2, 0),
            (E1, E3, 0),
            (E1, NEG_E3, 0),
        ),
        "D": (
            (NEG_E3, E1, 0),
            (NEG_E3, NEG_E1, 0),
        ),
    }
    checks.check(
        "theorem1-dots-and-forall-perp",
        all(dots1[name] == expected_dots[name] for name in ("A", "B", "C", "D"))
        and all(value == 0 for name in ("A", "B", "C", "D") for _a, _b, value in dots1[name])
        and all(forall1[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(exist1[name] == "hold" for name in ("A", "B", "C", "D")),
        str({name: (dots_display(dots1[name]), forall1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and m1["A"] == frozenset({NEG_E3})
        and PROBES["A"] not in seed_map
        and Y_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 3
        and unique_letter(o1["C"]) == UNDEFINED
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 2
        and unique_letter(o1["D"]) == UNDEFINED
        and forall1["B"] == "hold"
        and forall1["C"] == "hold"
        and forall1["D"] == "hold",
    )
    checks.check(
        "theorem1-compare-nm2axx-cover",
        cover1["A"] == "fail"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail"
        and lx["A"] == frozenset({E2})
        and lx["B"] == frozenset()
        and lx["C"] == frozenset()
        and lx["D"] == frozenset({E2})
        and forall1["A"] == "hold"
        and forall1["D"] == "hold",
        str({name: (forall1[name], cover1[name], axis_display(lx[name])) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0),)
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet["D"] == ((2, 1, 0),),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and forall1["A"] == "hold"
        and forall1["B"] == "hold"
        and reverse_status != "fail"
        and reverse_status != UNDEFINED
        and cover_reverse == "fail",
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and forall1["C"] == "hold"
        and forall1["D"] == "hold"
        and face_status != "fail"
        and face_status != UNDEFINED
        and cover_face == "fail",
        face_status,
    )
    checks.check(
        "empty-or-undefined-is-undefined",
        fp0["A"] == UNDEFINED
        and fp0["B"] == UNDEFINED
        and fp0["C"] == UNDEFINED
        and fp0["D"] == "hold"
        and o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E1})
        and reverse0 == UNDEFINED
        and face0 == UNDEFINED
        and cover0["A"] == "fail"
        and cover0["D"] == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-leftover-of-nm2axx-cover",
        cover_reverse == "fail"
        and cover_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and cover1["A"] == "fail"
        and forall1["A"] == "hold"
        and cover1["D"] == "fail"
        and forall1["D"] == "hold"
        and cover_reverse != reverse_status
        and cover_face != face_status,
    )
    checks.check(
        "not-exist-opposite-leftover",
        leftover_m_reverse == "fail"
        and leftover_o_reverse == "fail"
        and leftover_m_face == "fail"
        and leftover_o_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold"
        and forall_orthogonal is not existential_opposite,
    )
    checks.check(
        "exist-perp-is-comparison-only",
        exist1["A"] == "hold"
        and exist1["B"] == "hold"
        and exist1["C"] == "hold"
        and exist1["D"] == "hold"
        and exist_perp(mixed_exist, mixed_axis) == "hold"
        and forall_orthogonal(mixed_exist, mixed_axis) == "fail"
        and reverse_report("hold", "fail") == "fail"
        and reverse_status == "hold",
    )
    checks.check(
        "disjoint-is-not-forall-perp",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and m1["A"].isdisjoint(o1["A"])
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and frozenset({E1}).isdisjoint(frozenset({NEG_E1}))
        and forall1["A"] == "hold",
    )
    checks.check(
        "O-is-not-M",
        o1["A"] != m1["A"]
        and o1["B"] != m1["B"]
        and o1["C"] != m1["C"]
        and o1["D"] != m1["D"]
        and o0["A"] == frozenset()
        and o1["A"] == frozenset({E1}),
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        forall_orthogonal(frozenset(), m1["A"]) == UNDEFINED
        and forall_orthogonal(UNDEFINED, o1["A"]) == UNDEFINED
        and reverse_report(UNDEFINED, "hold") == UNDEFINED
        and face_report("hold", UNDEFINED) == UNDEFINED
        and reverse_report("hold", "fail") == "fail"
        and face_report("fail", "hold") == "fail",
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 1
        and len(m1["D"]) == 1
        and len(o1["B"]) == 3
        and len(o1["C"]) == 3
        and len(o1["D"]) == 2
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_reverse == UNDEFINED
        and unique_face == UNDEFINED
        and forall1["A"] == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
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
        and TWO_AXIS_OPPOSITE_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != PERP_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != NSPAR_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and len({site for site, _lock in TWO_AXIS_OPPOSITE_SEEDS}) == 4,
    )
    checks.check(
        "second-pair-is-new-seed-not-formed-child",
        one_axis_ticks[E3] == 1
        and one_axis_locks[E3] == {E3}
        and one_axis_ticks[YZ] == 1
        and one_axis_locks[YZ] == {E3}
        and one_axis_ticks[PROBES["B"]] == 2
        and one_axis_ticks[PROBES["D"]] == 3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[YZ] == 0
        and locks[YZ] == {NEG_E2}
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["D"]] == 2
        and E3 not in one_axis_seeds
        and YZ not in one_axis_seeds
        and E3 in seed_map
        and YZ in seed_map,
    )
    y_m1, y_o1, y_fp = family_at(Y_PROBES, ticks, locks, seed_map)
    z_m1, z_o1, z_fp = family_at(Z_PROBES, ticks, locks, seed_map)
    y_reverse = reverse_report(y_fp["A"], y_fp["B"])
    y_face = face_report(y_fp["C"], y_fp["D"])
    z_reverse = reverse_report(z_fp["A"], z_fp["B"])
    z_face = face_report(z_fp["C"], z_fp["D"])
    checks.check(
        "not-y-probes-or-z-probes",
        probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and y_m1["A"] != m1["A"]
        and y_m1["A"] == frozenset({NEG_E1})
        and y_reverse == "hold"
        and y_face == "hold"
        and z_m1["A"] != m1["A"]
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O",
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
        and "O(D, τ) = {+e_1, −e_1}" in note,
    )
    checks.check(
        "note-reports-dots-and-forall-perp",
        "(−e_3)·(+e_1)=0" in note
        and "(+e_1)·(+e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0" in note
        and "(+e_1)·(−e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0" in note
        and "(−e_3)·(+e_1)=0, (−e_3)·(−e_1)=0" in note
        and "forall-perp at A: hold" in note
        and "forall-perp at B: hold" in note
        and "forall-perp at C: hold" in note
        and "forall-perp at D: hold" in note
        and "forall-perp(A)=hold" in note
        and "forall-perp(B)=hold" in note
        and "forall-perp(C)=hold" in note
        and "forall-perp(D)=hold" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse: hold" in note
        and "Face: hold" in note
        and "Reverse holds." in note
        and "Face holds." in note
        and "Reverse from forall-perp at τ: hold" in note
        and "Face from forall-perp at τ: hold" in note,
    )
    checks.check(
        "note-compare-nm2axx-cover-fail",
        "nm2axx" in note
        and "union misses e_2" in normalized_note
        and "axes still disjoint" in normalized_note
        and "cover(A) = fail" in note
        and "cover(B) = hold" in note
        and "cover(C) = hold" in note
        and "cover(D) = fail" in note
        and cover_reverse == "fail"
        and cover_face == "fail"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-exist-opposite-leftover",
        "not leftover of exist-opposite" in normalized_note
        or "not exist-opposite leftover" in normalized_note,
    )
    checks.check(
        "note-not-exist-perp-or-cover-or-empty-intersection",
        "not leftover of exist-perp" in normalized_note
        and "not leftover of nm2axx cover" in normalized_note
        and "not leftover of empty intersection" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-uniqueness-not-required",
        "Uniqueness of incoming or outgoing locks is not required."
        in normalized_note
        and "Mixed remains a set." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "Occupancy `n` is not used" in note
        and "forall-perp" in normalized_note,
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
        '    "docs/TWO_AXIS_OPPOSITE_XPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "integer_dots" in defined_fns
        and "forall_orthogonal" in defined_fns
        and "forall_perp" in defined_fns
        and "exist_perp" in defined_fns
        and "axis_cover" in defined_fns
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
        "perp-hold-where-cover-fails",
        reverse_status == "hold"
        and face_status == "hold"
        and cover_reverse == "fail"
        and cover_face == "fail"
        and forall1["A"] == "hold"
        and cover1["A"] == "fail"
        and forall1["D"] == "hold"
        and cover1["D"] == "fail"
        and forall1["C"] == "hold"
        and cover1["C"] == "hold",
    )
    _ = (y_o1, z_o1, z_reverse, z_face)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
