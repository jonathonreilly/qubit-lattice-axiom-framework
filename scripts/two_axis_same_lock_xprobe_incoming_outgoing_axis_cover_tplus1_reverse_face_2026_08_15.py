#!/usr/bin/env python3
"""Axis-cover of M and O at t+1 on four x-probes of the two-axis same-lock seed.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is four sites, two disjoint same-lock pairs: origin locks +e_1, (0,1,0)
locks +e_1, (0,0,1) locks +e_2, (0,1,1) locks +e_2. Same process as nm2sl,
x-probes. Neither pair is opposite. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. t(q) is the formation
tick. tau = t+1. M(q, tau) is the set of earliest incoming nearest-neighbor
steps at q using only records with tick <= tau. Unformed at tau => UNDEFINED.
O(q, tau) is the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3} such
that q+e is formed and e is in M(q+e, tau). Unformed q at tau => UNDEFINED.
Empty O is empty, not UNDEFINED. O is not M. Axis(S) = {e_i | some ±e_i in
S}. Cover HOLD at q iff Axis(M) intersect Axis(O) is empty and Axis(M) union
Axis(O) equals {e_1,e_2,e_3}. Unformed at tau => UNDEFINED. Empty O fails
cover unless Axis(M) already equals {e_1,e_2,e_3}. Reverse HOLD iff cover at
A and at B. Face likewise on C, D. Uniqueness of locks is not required. No
unique P_+. Occupancy of sites is not used. Named-sign lettering is not
used. No larger host. No six-neighbor star. Displayed, not adopted. Do not
attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_INCOMING_OUTGOING_AXIS_COVER_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_INCOMING_OUTGOING_AXIS_COVER_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    ((0, 1, 1), E2),
)
ONE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
TWO_AXIS_OPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    ((0, 1, 1), NEG_E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
XE2_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
)
NSPAR_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E1, NEG_E1),
)
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
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
    "Axis-cover of M and O at t+1 on the four x-probes of the "
    "two-axis same-lock seed, and reverse/face from that, are reported. "
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
    """Lx = {e_1,e_2,e_3} minus (Axis(M) union Axis(O)). Unformed => UNDEFINED."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    return frozenset(AXES) - (axes_m | axes_o)


def leftover_of_one(value: Incoming) -> AxisSet:
    """One-sided leftover contrast: {e_1,e_2,e_3} minus Axis(S). Not this letter."""
    occupied = axis_set(value)
    if occupied == UNDEFINED:
        return UNDEFINED
    if not isinstance(occupied, frozenset):
        raise TypeError("one-sided leftover needs an axis set")
    return frozenset(AXES) - occupied


def leftover_equal(left: AxisSet, right: AxisSet) -> str:
    """Leftover-empty fail: HOLD iff both defined, nonempty, and equal."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("leftover sides must be axis sets or UNDEFINED")
    if not left or not right:
        return "fail"
    return "hold" if left == right else "fail"


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff Axis(M) and Axis(O) are disjoint and their union is {e_1,e_2,e_3}.

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


def forall_perp(left: Incoming, right: Incoming) -> str:
    """Comparison leftover: HOLD iff every m in M and o in O have m·o = 0."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for m in left:
        for o in right:
            if dot(m, o) != 0:
                return "fail"
    return "hold"


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Leftover: HOLD iff some lock in left is the vector opposite of some in right."""
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


def pair_status(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(status_a: str, status_b: str) -> str:
    """Reverse HOLD iff cover at A and at B."""
    return pair_status(status_a, status_b)


def face_report(status_c: str, status_d: str) -> str:
    """Face HOLD iff cover at C and at D."""
    return pair_status(status_c, status_d)


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


def named_sign(lock: Point) -> str:
    if lock in (E1, E2, E3):
        return "+"
    if lock in (NEG_E1, NEG_E2, NEG_E3):
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


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

    print("axis-cover of M and O at t+1 on two-axis same-lock x-probes")
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
        and add(NEG_E2, E2) == ZERO
        and add(E2, NEG_E2) == ZERO
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    set_a = frozenset({NEG_E3})
    set_a_o = frozenset({E1})
    set_b = frozenset({E1})
    set_b_o = frozenset({E2, E3, NEG_E3})
    mixed_nspar_b_m = frozenset({E2, E3})
    mixed_nspar_b_o = frozenset({E1, E2, E3})
    missing_axis = frozenset({E1})
    checks.check(
        "axis-cover-identity",
        axis_cover(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_cover(frozenset({E1}), UNDEFINED) == UNDEFINED
        and axis_cover(frozenset(), frozenset({E1})) == "fail"
        and axis_cover(frozenset({E1}), frozenset()) == "fail"
        and axis_cover(frozenset(), frozenset()) == "fail"
        and axis_cover(set_a, set_a_o) == "fail"
        and axis_cover(set_b, set_b_o) == "hold"
        and axis_cover(mixed_nspar_b_m, mixed_nspar_b_o) == "fail"
        and axis_cover(frozenset({E1}), frozenset({E1})) == "fail"
        and axis_cover(frozenset({E2}), missing_axis) == "fail"
        and leftover_axis(set_a, set_a_o) == frozenset({E2})
        and leftover_axis(set_b, set_b_o) == frozenset()
        and leftover_axis(mixed_nspar_b_m, mixed_nspar_b_o) == frozenset()
        and leftover_axis(frozenset({E2}), missing_axis) == frozenset({E3}),
    )
    checks.check(
        "axis-set-identity",
        axis_set(UNDEFINED) == UNDEFINED
        and axis_set(frozenset()) == frozenset()
        and axis_set(frozenset({NEG_E3})) == frozenset({E3})
        and axis_set(frozenset({E1, NEG_E1, E3})) == frozenset({E1, E3})
        and axis_set(frozenset({E2, NEG_E2})) == frozenset({E2}),
    )
    checks.check(
        "pair-status-identity",
        pair_status(UNDEFINED, "hold") == UNDEFINED
        and pair_status("hold", UNDEFINED) == UNDEFINED
        and pair_status("hold", "hold") == "hold"
        and pair_status("hold", "fail") == "fail"
        and pair_status("fail", "hold") == "fail"
        and pair_status("fail", "fail") == "fail",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(NSOPP_SEEDS)
    xe2_ticks, xe2_locks, xe2_seeds = form(XE2_SEEDS)
    nspar_ticks, nspar_locks, nspar_seeds = form(NSPAR_SEEDS)
    xsame_ticks, xsame_locks, xsame_seeds = form(X_AXIS_SAME_SEEDS)

    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    ax_m: dict[str, AxisSet] = {}
    ax_o: dict[str, AxisSet] = {}
    cover0: dict[str, str] = {}
    cover1: dict[str, str] = {}
    leftover1: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    fp0: dict[str, str] = {}
    fp1: dict[str, str] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        ax_m[name] = axis_set(m1[name])
        ax_o[name] = axis_set(o1[name])
        cover0[name] = axis_cover(m0[name], o0[name])
        cover1[name] = axis_cover(m1[name], o1[name])
        leftover1[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        fp0[name] = forall_perp(m0[name], o0[name])
        fp1[name] = forall_perp(m1[name], o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"Axis(M)={axis_display(ax_m[name])} "
            f"Axis(O)={axis_display(ax_o[name])} "
            f"cover={cover1[name]}"
        )

    reverse_status = reverse_report(cover1["A"], cover1["B"])
    face_status = face_report(cover1["C"], cover1["D"])
    reverse0 = reverse_report(cover0["A"], cover0["B"])
    face0 = face_report(cover0["C"], cover0["D"])
    leftover_reverse = leftover_equal(leftover1["A"], leftover1["B"])
    leftover_face = leftover_equal(leftover1["C"], leftover1["D"])
    reverse_m_alone = leftover_equal(lx_m["A"], lx_m["B"])
    face_m_alone = leftover_equal(lx_m["C"], lx_m["D"])
    reverse_o_alone = leftover_equal(lx_o["A"], lx_o["B"])
    face_o_alone = leftover_equal(lx_o["C"], lx_o["D"])
    fp_reverse = reverse_report(fp1["A"], fp1["B"])
    fp_face = face_report(fp1["C"], fp1["D"])
    m_opp_reverse = existential_opposite(m1["A"], m1["B"])
    m_opp_face = existential_opposite(m1["C"], m1["D"])
    o_opp_reverse = existential_opposite(o1["A"], o1["B"])
    o_opp_face = existential_opposite(o1["C"], o1["D"])
    unique_cover_reverse = reverse_report(
        axis_cover(unique_letter(m1["A"]), unique_letter(o1["A"])),
        axis_cover(unique_letter(m1["B"]), unique_letter(o1["B"])),
    )
    unique_cover_face = face_report(
        axis_cover(unique_letter(m1["C"]), unique_letter(o1["C"])),
        axis_cover(unique_letter(m1["D"]), unique_letter(o1["D"])),
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: each earliest incoming or outgoing nearest-neighbor step "
        "at a probe, read from the record prefix at that probe's t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four incoming sets, four outgoing sets, Axis of each, "
        "cover at each probe, reverse/face from those bits"
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
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["C"], 2, ticks, locks, seed_map) == UNDEFINED
        and axis_cover(
            incoming_set(PROBES["A"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["A"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED,
    )
    checks.check(
        "neither-pair-is-opposite",
        seed_map[ORIGIN] == seed_map[E2] == E1
        and seed_map[E3] == seed_map[(0, 1, 1)] == E2
        and add(seed_map[ORIGIN], seed_map[E2]) != ZERO
        and add(seed_map[E3], seed_map[(0, 1, 1)]) != ZERO
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS,
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
        and m1["D"] == frozenset({NEG_E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E1})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-Axis-M-and-O",
        ax_m["A"] == frozenset({E3})
        and ax_o["A"] == frozenset({E1})
        and ax_m["B"] == frozenset({E1})
        and ax_o["B"] == frozenset({E2, E3})
        and ax_m["C"] == frozenset({E1})
        and ax_o["C"] == frozenset({E2, E3})
        and ax_m["D"] == frozenset({E3})
        and ax_o["D"] == frozenset({E1})
        and leftover1["A"] == frozenset({E2})
        and leftover1["B"] == frozenset()
        and leftover1["C"] == frozenset()
        and leftover1["D"] == frozenset({E2}),
        str(
            {
                name: (axis_display(ax_m[name]), axis_display(ax_o[name]))
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-cover-bits",
        cover1["A"] == "fail"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail",
        str(cover1),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-O-empty-at-t-then-filled",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset()
        and cover0["A"] == "fail"
        and cover0["B"] == "fail"
        and cover0["C"] == "fail"
        and cover0["D"] == "fail"
        and reverse0 == "fail"
        and face0 == "fail"
        and fp0["A"] == UNDEFINED
        and fp0["B"] == UNDEFINED
        and fp0["C"] == UNDEFINED
        and fp0["D"] == UNDEFINED,
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
        "theorem1-mixed-stays-a-set",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 3
        and unique_letter(o1["C"]) == UNDEFINED
        and o1["B"] != UNDEFINED
        and cover1["B"] == "hold",
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and E1 not in seed_map
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and m1["A"] == frozenset({NEG_E3})
        and Y_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse_status == "fail"
        and cover1["A"] == "fail"
        and cover1["B"] == "hold"
        and reverse_status != "hold"
        and reverse_status != UNDEFINED,
        reverse_status,
    )
    checks.check(
        "theorem3-face-fail",
        face_status == "fail"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail"
        and face_status != "hold"
        and face_status != UNDEFINED,
        face_status,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E3 in m1["A"]
        and NEG_E3 not in o1["A"]
        and o1["A"] != m1["A"]
        and m1["A"].isdisjoint(o1["A"])
        and m1["B"].isdisjoint(o1["B"])
        and m1["C"].isdisjoint(o1["C"])
        and m1["D"].isdisjoint(o1["D"]),
    )
    checks.check(
        "mutation-unique-letter-undefined",
        unique_cover_reverse == UNDEFINED
        and unique_cover_face == UNDEFINED
        and reverse_status == "fail"
        and face_status == "fail"
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED,
    )
    checks.check(
        "mutation-leftover-empty-fails",
        leftover1["A"] == frozenset({E2})
        and leftover1["B"] == frozenset()
        and leftover1["C"] == frozenset()
        and leftover1["D"] == frozenset({E2})
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and reverse_status == "fail",
    )
    checks.check(
        "mutation-forall-perp-hold-not-this-predicate",
        fp_reverse == "hold"
        and fp_face == "hold"
        and fp0["A"] == UNDEFINED
        and cover0["A"] == "fail"
        and reverse0 == "fail"
        and reverse_status == "fail"
        and cover1["A"] == "fail"
        and fp1["A"] == "hold",
    )
    checks.check(
        "mutation-exist-opposite-of-M-or-O-not-this-predicate",
        m_opp_reverse == "fail"
        and m_opp_face == "fail"
        and o_opp_reverse == "fail"
        and o_opp_face == "fail"
        and reverse_status == "fail"
        and face_status == "fail"
        and axis_cover(m1["B"], o1["B"]) == "hold"
        and existential_opposite(m1["B"], o1["B"]) == "fail",
    )
    checks.check(
        "not-leftover-of-M-or-O-alone",
        reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and lx_m["A"] == frozenset({E1, E2})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_o["A"] == frozenset({E2, E3})
        and lx_o["B"] == frozenset({E1})
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "mutation-empty-or-undefined",
        axis_cover(frozenset(), o1["A"]) == "fail"
        and axis_cover(m1["A"], frozenset()) == "fail"
        and reverse_report(UNDEFINED, "hold") == UNDEFINED
        and reverse0 == "fail"
        and reverse_status == "fail",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["B"], frozenset)
        and isinstance(o1["D"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E3
        and sum_of_set(m1["B"]) == E1
        and sum_of_set(m1["C"]) == E1
        and sum_of_set(m1["D"]) == NEG_E3
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["D"]) == E1
        and sum_of_set(o1["B"]) == E2
        and o1["B"] != frozenset({E2}),
    )
    checks.check(
        "not-nnlock-named-sign",
        m1["A"] == frozenset({NEG_E3})
        and named_sign(NEG_E3) == "-"
        and named_sign(E1) == "+"
        and m1["B"] == frozenset({E1})
        and m1["A"] != named_sign(NEG_E3)
        and axis_cover(m1["A"], o1["A"]) != named_sign(NEG_E3),
    )

    def probe_cover(
        probe_map: dict[str, Point],
        ticks_map: dict[Point, int],
        locks_map: dict[Point, set[Point]],
        seed_map_local: dict[Point, Point],
    ) -> tuple[dict[str, Incoming], dict[str, Outgoing], dict[str, str]]:
        incoming: dict[str, Incoming] = {}
        outgoing: dict[str, Outgoing] = {}
        status: dict[str, str] = {}
        for name in ("A", "B", "C", "D"):
            site = probe_map[name]
            tau = ticks_map[site] + 1
            incoming[name] = incoming_set(
                site, tau, ticks_map, locks_map, seed_map_local
            )
            outgoing[name] = outgoing_set(
                site, tau, ticks_map, locks_map, seed_map_local
            )
            status[name] = axis_cover(incoming[name], outgoing[name])
        return incoming, outgoing, status

    y_m, y_o, y_cover = probe_cover(Y_PROBES, ticks, locks, seed_map)
    z_m, z_o, z_cover = probe_cover(Z_PROBES, ticks, locks, seed_map)
    one_m, one_o, one_cover = probe_cover(
        PROBES, one_ticks, one_locks, one_seeds
    )
    opp_m, opp_o, opp_cover = probe_cover(
        PROBES, opp_ticks, opp_locks, opp_seeds
    )
    nsopp_m, nsopp_o, nsopp_cover = probe_cover(
        PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds
    )
    xe2_m, xe2_o, xe2_cover = probe_cover(PROBES, xe2_ticks, xe2_locks, xe2_seeds)
    nspar_m, nspar_o, nspar_cover = probe_cover(
        PROBES, nspar_ticks, nspar_locks, nspar_seeds
    )
    xsame_m, xsame_o, xsame_cover = probe_cover(
        PROBES, xsame_ticks, xsame_locks, xsame_seeds
    )
    y_reverse = reverse_report(y_cover["A"], y_cover["B"])
    y_face = face_report(y_cover["C"], y_cover["D"])
    z_reverse = reverse_report(z_cover["A"], z_cover["B"])
    z_face = face_report(z_cover["C"], z_cover["D"])
    one_reverse = reverse_report(one_cover["A"], one_cover["B"])
    one_face = face_report(one_cover["C"], one_cover["D"])
    opp_reverse = reverse_report(opp_cover["A"], opp_cover["B"])
    opp_face = face_report(opp_cover["C"], opp_cover["D"])
    nsopp_reverse = reverse_report(nsopp_cover["A"], nsopp_cover["B"])
    nsopp_face = face_report(nsopp_cover["C"], nsopp_cover["D"])
    nspar_reverse = reverse_report(nspar_cover["A"], nspar_cover["B"])
    checks.check(
        "not-y-or-z-probes-or-opposite-or-1-axis-or-nsopp-or-nspar",
        FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
        and FOUR_SITE_SEEDS != ONE_AXIS_SEEDS
        and FOUR_SITE_SEEDS != NSOPP_SEEDS
        and FOUR_SITE_SEEDS != XE2_SEEDS
        and FOUR_SITE_SEEDS != NSPAR_SEEDS
        and FOUR_SITE_SEEDS != X_AXIS_SAME_SEEDS
        and probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and y_m["A"] != m1["A"]
        and y_o["A"] != o1["A"]
        and z_m["A"] != m1["A"]
        and opp_o["D"] != o1["D"]
        and isinstance(opp_o["D"], frozenset)
        and NEG_E1 in opp_o["D"]
        and isinstance(o1["D"], frozenset)
        and NEG_E1 not in o1["D"]
        and o1["D"] == frozenset({E1})
        and nsopp_m["A"] != m1["A"]
        and xe2_m["A"] != m1["A"]
        and nspar_m["A"] != m1["A"]
        and xsame_m["A"] != m1["A"]
        and y_reverse == "hold"
        and y_face == "fail"
        and z_reverse == "fail"
        and z_face == "hold"
        and opp_reverse == "fail"
        and opp_face == "fail"
        and one_cover["A"] == "hold"
        and one_cover["D"] == "hold"
        and one_reverse == "hold"
        and one_face == "hold"
        and one_ticks[PROBES["A"]] == 3
        and ticks[PROBES["A"]] == 2
        and nsopp_reverse == "hold"
        and nsopp_face == "hold"
        and nspar_cover["B"] == "fail"
        and leftover_axis(nspar_m["B"], nspar_o["B"]) == frozenset()
        and nspar_reverse == "fail"
        and reverse_status == "fail"
        and face_status == "fail"
        and xe2_cover["A"] == "hold"
        and xsame_cover["A"] == "hold",
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(m1["A"], frozenset)
        and len(m1["A"]) == 1
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 1
        and reverse_status == "fail"
        and face_status == "fail",
    )
    checks.check(
        "four-site-two-axis-same-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E1}
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[(0, 1, 1)] == 0
        and locks[(0, 1, 1)] == {E2}
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
        and FOUR_SITE_SEEDS != NSOPP_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O-Axis-cover",
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
        and "O(D, τ) = {+e_1}" in note
        and "Axis(M(A, τ)) = {e_3}" in note
        and "Axis(O(A, τ)) = {e_1}" in note
        and "Axis(M(B, τ)) = {e_1}" in note
        and "Axis(O(B, τ)) = {e_2, e_3}" in note
        and "Axis(M(C, τ)) = {e_1}" in note
        and "Axis(O(C, τ)) = {e_2, e_3}" in note
        and "Axis(M(D, τ)) = {e_3}" in note
        and "Axis(O(D, τ)) = {e_1}" in note
        and "cover(A): fail" in note
        and "cover(B): hold" in note
        and "cover(C): hold" in note
        and "cover(D): fail" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (2, 0, 0)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-fail-fail",
        "Reverse: fail" in note
        and "Face: fail" in note
        and "hold" in note
        and "fail" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "mixed remains a set" in normalized_note,
    )
    checks.check(
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-not-ndot-or-occupancy-inner-product",
        "not an occupancy-kernel inner product" in normalized_note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
        in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-leftover-empty-or-opposite-or-yprobe",
        "not leftover-empty fail" in normalized_note
        and "HOLD iff cover" in note
        and "not leftover of leftover-axis" in normalized_note
        and "not leftover of forall-perp" in normalized_note
        and "not leftover of exist-opposite of M" in normalized_note
        and "not leftover of exist-opposite of O" in normalized_note
        and "not leftover of two-axis opposite" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "own incoming" in normalized_note,
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
        '    "docs/TWO_AXIS_SAME_LOCK_XPROBE_INCOMING_OUTGOING_AXIS_COVER_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "leftover_axis" in defined_fns
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
    _ = (
        y_o,
        z_o,
        one_m,
        one_o,
        opp_m,
        nsopp_o,
        xe2_o,
        nspar_m,
        xsame_o,
        one_reverse,
        one_face,
        opp_cover,
        leftover_reverse,
        leftover_face,
        reverse_m_alone,
        face_m_alone,
        reverse_o_alone,
        face_o_alone,
        unique_cover_reverse,
        unique_cover_face,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
