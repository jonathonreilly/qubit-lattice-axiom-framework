#!/usr/bin/env python3
"""Simultaneous M and O at t+1 reverse/face on two-axis same-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is four sites in two disjoint same-lock pairs: origin and (0,1,0) lock
+e_1; (0,0,1) and (0,1,1) lock +e_2. Neither pair is opposite. Same process
and y-probes as the two-axis same-lock y-probe timed-O display. A 6-NN
step is allowed iff it is perpendicular to the parent lock axis. Newly
formed sites lock the incoming step. Seeds keep their seed letters as a
singleton. M(q, tau) is the set of earliest incoming nearest-neighbor steps
at q using only records with tick <= tau. Unformed at tau => UNDEFINED.
O(q, tau) is the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3} such
that q+e is formed and e is in M(q+e, tau). Unformed q at tau => UNDEFINED.
Empty O is empty, not UNDEFINED. Intersection is M intersect O; unformed =>
UNDEFINED. Empty intersection is empty, not UNDEFINED. Simultaneous HOLDs
at q iff both M and O are defined nonempty and M intersect O is empty.
UNDEFINED if M or O UNDEFINED. Else fail. Reverse HOLDs iff simultaneous
at A and at B. Face likewise on C, D. Compare to nm2simy HOLDING and
nm2slo timed-O HOLDING. Uniqueness is not required. Occupancy of
sites is not used. Named-sign lettering is not used. No larger host. Not
leftover of M alone or of O alone. Not leftover-empty fail. Not unsigned
axis-cover. Not 1-in 2-out split. Not exist-opposite of signed locks.
Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_YPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_YPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
FOUR_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    (PAIR2, E2),
)
ONE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
TWO_AXIS_OPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
)
Z_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E3, NEG_E1),
    (NEG_E3, NEG_E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E2),
)
PROBES = {
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
    "Simultaneous M and O at t+1 on the four y-probes of the "
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


def intersection_set(left: Incoming, right: Outgoing) -> Incoming:
    """M intersect O. Unformed on either side => UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("intersection sides must be lock sets or UNDEFINED")
    return left & right


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
    """One-sided leftover contrast: {e_1,e_2,e_3} minus Axis(S). Not this letter."""
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
    """Unsigned-axis cover contrast. Not this simultaneous letter."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    if not incoming or not outgoing:
        return "fail"
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


def one_two_split(incoming: Incoming, outgoing: Outgoing) -> str:
    """1-in 2-out contrast: cover HOLD and |Axis(M)|=1. Not this letter."""
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    axes_m = axis_set(incoming)
    if axes_m == UNDEFINED or not isinstance(axes_m, frozenset):
        return UNDEFINED
    if len(axes_m) != 1:
        return "fail"
    return "hold"


def forall_orthogonal(left: Incoming, right: Incoming) -> str:
    """nm2slp leftover: hold iff every integer dot m·o is 0."""
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


def simultaneous(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff both defined nonempty and signed-letter intersection empty."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    if not incoming or not outgoing:
        return "fail"
    if incoming & outgoing:
        return "fail"
    return "hold"


def pair_sim(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either side is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(sim_a: str, sim_b: str) -> str:
    """Reverse HOLDs iff simultaneous at A and simultaneous at B."""
    return pair_sim(sim_a, sim_b)


def face_report(sim_c: str, sim_d: str) -> str:
    """Face HOLDs iff simultaneous at C and simultaneous at D."""
    return pair_sim(sim_c, sim_d)


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


def neighbor_lock_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    tau: int,
) -> frozenset[Point]:
    """Leftover contrast: locks of 6-NN formed by tau, site excluded."""
    collected: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks or ticks[neighbor] > tau:
            continue
        collected.update(locks[neighbor])
    return frozenset(collected)


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


def probe_map(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    letter,
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = letter(
            incoming_set(
                site, site_ticks[site] + 1, site_ticks, site_locks, site_seeds
            ),
            outgoing_set(
                site, site_ticks[site] + 1, site_ticks, site_locks, site_seeds
            ),
        )
    return out


def probe_sim(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    return probe_map(probes, site_ticks, site_locks, site_seeds, simultaneous)


def probe_cover(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    return probe_map(probes, site_ticks, site_locks, site_seeds, axis_cover)


def probe_split(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    return probe_map(probes, site_ticks, site_locks, site_seeds, one_two_split)


def probe_forall(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    return probe_map(probes, site_ticks, site_locks, site_seeds, forall_orthogonal)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("simultaneous M and O reverse/face at t+1 on two-axis same-lock y-probes")
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
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    z_probe_sites = tuple(Z_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != x_probe_sites
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E3, E2) == PAIR2
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "intersection-identity",
        intersection_set(UNDEFINED, frozenset({E1})) == UNDEFINED
        and intersection_set(frozenset({E1}), UNDEFINED) == UNDEFINED
        and intersection_set(frozenset({E1, E2}), frozenset({E2, E3}))
        == frozenset({E2})
        and intersection_set(frozenset({NEG_E3}), frozenset({E1})) == frozenset()
        and intersection_set(frozenset(), frozenset({E1})) == frozenset(),
    )
    checks.check(
        "simultaneous-identity",
        simultaneous(UNDEFINED, frozenset({E1})) == UNDEFINED
        and simultaneous(frozenset({E1}), UNDEFINED) == UNDEFINED
        and simultaneous(frozenset(), frozenset({E2, E3})) == "fail"
        and simultaneous(frozenset({NEG_E1}), frozenset()) == "fail"
        and simultaneous(frozenset({NEG_E3}), frozenset({E1})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({NEG_E1})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({E1, E2})) == "fail"
        and simultaneous(frozenset({E1, E3}), frozenset({E1, E2, E3})) == "fail",
    )
    checks.check(
        "pair-sim-identity",
        pair_sim(UNDEFINED, "hold") == UNDEFINED
        and pair_sim("hold", UNDEFINED) == UNDEFINED
        and pair_sim("hold", "hold") == "hold"
        and pair_sim("hold", "fail") == "fail"
        and pair_sim("fail", "hold") == "fail"
        and pair_sim("fail", "fail") == "fail",
    )
    checks.check(
        "leftover-empty-fail-contrast",
        leftover_match(frozenset(), frozenset()) == "fail"
        and leftover_match(UNDEFINED, frozenset({E1})) == UNDEFINED
        and leftover_axis(frozenset({NEG_E3}), frozenset({E1})) == frozenset({E2})
        and leftover_axis(frozenset({E1}), frozenset({E2, E3, NEG_E3}))
        == frozenset(),
    )
    checks.check(
        "one-two-split-identity",
        one_two_split(UNDEFINED, frozenset({E1})) == UNDEFINED
        and one_two_split(frozenset({E1}), UNDEFINED) == UNDEFINED
        and one_two_split(frozenset({NEG_E3}), frozenset({E1})) == "fail"
        and one_two_split(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and one_two_split(frozenset({E1, E2}), frozenset({E3})) == "fail",
    )
    checks.check(
        "forall-perp-is-not-simultaneous",
        forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and simultaneous(frozenset({E1}), frozenset({NEG_E1})) == "hold"
        and forall_orthogonal(frozenset({NEG_E3}), frozenset({E1})) == "hold"
        and simultaneous(frozenset({NEG_E3}), frozenset({E1})) == "hold",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)
    nsopp_ticks, nsopp_locks, nsopp_seeds = form(NSOPP_SEEDS)
    xsame_ticks, xsame_locks, xsame_seeds = form(X_AXIS_SAME_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    inter1: dict[str, Incoming] = {}
    sim: dict[str, str] = {}
    cover: dict[str, str] = {}
    split: dict[str, str] = {}
    forall1: dict[str, str] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        inter1[name] = intersection_set(m1[name], o1[name])
        sim[name] = simultaneous(m1[name], o1[name])
        cover[name] = axis_cover(m1[name], o1[name])
        split[name] = one_two_split(m1[name], o1[name])
        forall1[name] = forall_orthogonal(m1[name], o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"M∩O={lockset_display(inter1[name])} "
            f"sim={sim[name]}"
        )

    reverse = reverse_report(sim["A"], sim["B"])
    face = face_report(sim["C"], sim["D"])
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
    unique_sim_b = simultaneous(unique_letter(m1["B"]), unique_letter(o1["B"]))
    leftover_neighbor_reverse = leftover_match(
        leftover_of_one(
            neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
        ),
        leftover_of_one(
            neighbor_lock_set(PROBES["B"], ticks, locks, ticks[PROBES["B"]])
        ),
    )
    cover_reverse = reverse_report(cover["A"], cover["B"])
    cover_face = face_report(cover["C"], cover["D"])
    split_reverse = reverse_report(split["A"], split["B"])
    split_face = face_report(split["C"], split["D"])
    forall_reverse = reverse_report(forall1["A"], forall1["B"])
    forall_face = face_report(forall1["C"], forall1["D"])
    one_sim = probe_sim(PROBES, one_ticks, one_locks, one_seeds)
    one_reverse = reverse_report(one_sim["A"], one_sim["B"])
    one_face = face_report(one_sim["C"], one_sim["D"])
    one_cover = probe_cover(PROBES, one_ticks, one_locks, one_seeds)
    opp_sim = probe_sim(PROBES, opp_ticks, opp_locks, opp_seeds)
    opp_reverse = reverse_report(opp_sim["A"], opp_sim["B"])
    opp_face = face_report(opp_sim["C"], opp_sim["D"])
    opp_z_sim = probe_sim(Z_PROBES, opp_ticks, opp_locks, opp_seeds)
    opp_z_reverse = reverse_report(opp_z_sim["A"], opp_z_sim["B"])
    opp_z_face = face_report(opp_z_sim["C"], opp_z_sim["D"])
    opp_o_d = outgoing_set(
        PROBES["D"],
        opp_ticks[PROBES["D"]] + 1,
        opp_ticks,
        opp_locks,
        opp_seeds,
    )
    opp_o_d_t = outgoing_set(
        PROBES["D"],
        opp_ticks[PROBES["D"]],
        opp_ticks,
        opp_locks,
        opp_seeds,
    )
    print(f"sim reverse={reverse} face={face}")
    print(f"leftover-empty reverse={leftover_reverse} face={leftover_face}")
    print(f"nm2sl cover reverse={cover_reverse} face={cover_face}")
    print(f"nm2slp forall-perp reverse={forall_reverse} face={forall_face}")
    print(
        f"nm2simy opposite y-probe sim reverse={opp_reverse} face={opp_face} "
        f"A={opp_sim['A']}"
    )
    print(
        f"nm2simz opposite z-probe sim reverse={opp_z_reverse} face={opp_z_face} "
        f"A={opp_z_sim['A']}"
    )
    print(
        "per_element: each signed lock among {±e_1,±e_2,±e_3} in M or in O "
        "at a probe's t+1"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four sim reports, reverse/face from sim HOLD")
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
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2
        and locks[PROBES["A"]] == {E1}
        and locks[PROBES["B"]] == {E1}
        and locks[PROBES["C"]] == {E2}
        and locks[PROBES["D"]] == {NEG_E3}
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and simultaneous(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and simultaneous(
            incoming_set(PROBES["C"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED,
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
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau",
        m1["A"] == frozenset({E1})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E2, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-intersection-at-tau",
        inter1["A"] == frozenset()
        and inter1["B"] == frozenset()
        and inter1["C"] == frozenset()
        and inter1["D"] == frozenset()
        and all(
            isinstance(m1[name], frozenset)
            and isinstance(o1[name], frozenset)
            and m1[name].isdisjoint(o1[name])
            for name in ("A", "B", "C", "D")
        ),
        str({name: lockset_display(inter1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-sim-hold",
        all(sim[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(
            isinstance(m1[name], frozenset)
            and isinstance(o1[name], frozenset)
            and bool(m1[name])
            and bool(o1[name])
            and m1[name].isdisjoint(o1[name])
            for name in ("A", "B", "C", "D")
        ),
        str({name: sim[name] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-O-empty-at-t-nonempty-at-tplus1",
        all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(
            simultaneous(m0[name], o0[name]) == "fail" for name in ("A", "B", "C", "D")
        )
        and all(sim[name] == "hold" for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((0, 2, 0), (0, 1, -1))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1))
        and new_meet["D"] == ((2, 1, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_sim_b == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and unique_letter(o1["C"]) == UNDEFINED
        and sim["A"] == "hold"
        and sim["B"] == "hold"
        and sim["C"] == "hold",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {E1}
        and m1["A"] == frozenset({E1})
        and PROBES["A"] in seed_map
        and seed_map[E2] == E1
        and X_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "compare-nm2simz-holding",
        all(opp_z_sim[name] == "hold" for name in ("A", "B", "C", "D"))
        and opp_z_reverse == "hold"
        and opp_z_face == "hold"
        and ticks[PROBES["A"]] == 0
        and m1["A"] == frozenset({E1})
        and reverse == "hold"
        and face == "hold"
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS,
    )
    checks.check(
        "compare-nm2slp-forall-perp",
        all(forall1[name] == "hold" for name in ("A", "B", "C", "D"))
        and forall_reverse == "hold"
        and forall_face == "hold"
        and reverse == "hold"
        and face == "hold"
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and simultaneous(frozenset({E1}), frozenset({NEG_E1})) == "hold",
    )
    checks.check(
        "compare-nm2sl-cover",
        cover["A"] == "hold"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "fail"
        and cover_reverse == "hold"
        and cover_face == "fail"
        and lx["A"] == frozenset()
        and lx["D"] == frozenset({E2})
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "compare-1-in-2-out",
        split["A"] == "hold"
        and split["B"] == "hold"
        and split["C"] == "hold"
        and split["D"] == "fail"
        and split_reverse == "hold"
        and split_face == "fail"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "compare-1-axis-same-lock-y",
        one_ticks[PROBES["A"]] == 0
        and one_ticks[PROBES["B"]] == 2
        and one_ticks[PROBES["C"]] == 1
        and one_ticks[PROBES["D"]] == 3
        and ticks[PROBES["A"]] == 0
        and cover["A"] == "hold"
        and cover["D"] == "fail"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "theorem2-reverse-sim-hold",
        reverse == "hold"
        and sim["A"] == "hold"
        and sim["B"] == "hold"
        and reverse != UNDEFINED
        and reverse != "fail"
        and cover_reverse == "hold",
    )
    checks.check(
        "theorem3-face-sim-hold",
        face == "hold"
        and sim["C"] == "hold"
        and sim["D"] == "hold"
        and face != UNDEFINED
        and face != "fail"
        and cover_face == "fail",
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and lx["A"] == frozenset()
        and lx["B"] == frozenset()
        and lx["C"] == frozenset()
        and lx["D"] == frozenset({E2})
        and reverse == "hold"
        and face == "hold"
        and leftover_reverse != reverse
        and leftover_face != face,
    )
    checks.check(
        "not-leftover-of-M-alone",
        reverse_m_alone == "hold"
        and face_m_alone == "fail"
        and lx_m["A"] == frozenset({E2, E3})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_m["C"] == frozenset({E1, E3})
        and lx_m["D"] == frozenset({E1, E2})
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "not-leftover-of-O-alone",
        reverse_o_alone == "hold"
        and face_o_alone == "fail"
        and lx_o["A"] == frozenset({E1})
        and lx_o["B"] == frozenset({E1})
        and lx_o["C"] == frozenset({E2})
        and lx_o["D"] == frozenset({E2, E3})
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "not-exist-opposite-of-M",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "not-exist-opposite-of-O",
        o_exist_reverse == "hold"
        and o_exist_face == "hold"
        and reverse == "hold"
        and face == "hold"
        and o_exist_reverse == reverse
        and cover_face == "fail",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == frozenset({E1})
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_letter(o1["D"]) == frozenset({E1})
        and unique_sim_b == UNDEFINED
        and sim["B"] == "hold"
        and reverse == "hold",
    )
    checks.check(
        "mutation-empty-plus-undefined",
        simultaneous(frozenset(), frozenset({E2, E3})) == "fail"
        and simultaneous(UNDEFINED, frozenset({E1})) == UNDEFINED
        and reverse == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["B"], frozenset)
        and isinstance(m1["B"], frozenset)
        and sum_of_set(m1["A"]) == E1
        and sum_of_set(o1["A"]) == add(E2, NEG_E3)
        and sum_of_set(o1["B"]) == E2
        and o1["B"] != frozenset({E2}),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E1 in m1["A"]
        and E1 not in o1["A"]
        and o1["A"] != m1["A"]
        and inter1["A"] == frozenset(),
    )
    x_sim = probe_sim(X_PROBES, ticks, locks, seed_map)
    z_sim = probe_sim(Z_PROBES, ticks, locks, seed_map)
    x_cover = probe_cover(X_PROBES, ticks, locks, seed_map)
    z_cover = probe_cover(Z_PROBES, ticks, locks, seed_map)
    x_split = probe_split(X_PROBES, ticks, locks, seed_map)
    xsame_sim = probe_sim(PROBES, xsame_ticks, xsame_locks, xsame_seeds)
    perp_sim_map = probe_sim(PROBES, perp_ticks, perp_locks, perp_seeds)
    zsym_sim = probe_sim(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    x_reverse = reverse_report(x_sim["A"], x_sim["B"])
    x_face = face_report(x_sim["C"], x_sim["D"])
    z_reverse = reverse_report(z_sim["A"], z_sim["B"])
    z_face = face_report(z_sim["C"], z_sim["D"])
    nsopp_sim = probe_sim(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    checks.check(
        "not-x-probes-or-z-probes-or-x-axis-same",
        FOUR_SITE_SEEDS != X_AXIS_SAME_SEEDS
        and FOUR_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != z_probe_sites
        and x_sim["D"] == "hold"
        and x_cover["D"] == "fail"
        and x_split["D"] == "fail"
        and x_face == "hold"
        and x_reverse == "hold"
        and z_sim["A"] == "fail"
        and z_reverse == "fail"
        and z_face == "hold"
        and reverse == "hold"
        and face == "hold"
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in ysym_ticks.values()) == 3,
    )
    checks.check(
        "mutation-axis-cover-is-not-this-letter",
        cover["A"] == "hold"
        and cover["D"] == "fail"
        and cover_reverse == "hold"
        and cover_face == "fail"
        and x_cover["D"] == "fail"
        and x_sim["D"] == "hold"
        and reverse == "hold"
        and face == "hold"
        and simultaneous(frozenset({NEG_E3}), frozenset({E1, NEG_E1})) == "hold"
        and axis_cover(frozenset({NEG_E3}), frozenset({E1, NEG_E1})) == "fail",
    )
    checks.check(
        "not-two-axis-opposite",
        FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
        and FOUR_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and o1["D"] == frozenset({E1})
        and opp_o_d == frozenset({E1, NEG_E1})
        and o0["D"] == frozenset()
        and opp_o_d_t == frozenset({NEG_E1})
        and locks[E2] == {E1}
        and opp_locks[E2] == {NEG_E1}
        and locks[PAIR2] == {E2}
        and opp_locks[PAIR2] == {NEG_E2}
        and opp_sim["A"] == "hold"
        and reverse == "hold"
        and zsym_ticks[E3] == 0
        and zsym_locks[E3] == {NEG_E1},
    )
    checks.check(
        "not-nsopp-or-perp",
        FOUR_SITE_SEEDS != NSOPP_SEEDS
        and FOUR_SITE_SEEDS != PERP_SEEDS
        and nsopp_sim["A"] == "hold"
        and ticks[PROBES["A"]] == 0
        and m1["A"] == frozenset({E1})
        and reverse_report(perp_sim_map["A"], perp_sim_map["B"]) != reverse
        and reverse == "hold",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "empty-intersection-is-empty-not-undefined",
        all(
            inter1[name] == frozenset() and inter1[name] != UNDEFINED
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(o1["A"], frozenset)
        and isinstance(o1["B"], frozenset)
        and isinstance(o1["C"], frozenset)
        and isinstance(o1["D"], frozenset)
        and len(o1["A"]) == 2
        and len(o1["B"]) == 3
        and len(o1["C"]) == 4
        and len(o1["D"]) == 1
        and reverse == "hold"
        and face == "hold",
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-intersection-sim",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=2" in note
        and "M(A, τ) = {+e_1}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_2}" in note
        and "M(D, τ) = {−e_3}" in note
        and "O(A, τ) = {+e_2, −e_3}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_1}" in note
        and "M(A, τ) ∩ O(A, τ) = {}" in note
        and "M(B, τ) ∩ O(B, τ) = {}" in note
        and "M(C, τ) ∩ O(C, τ) = {}" in note
        and "M(D, τ) ∩ O(D, τ) = {}" in note
        and "sim(A) = hold" in note
        and "sim(B) = hold" in note
        and "sim(C) = hold" in note
        and "sim(D) = hold" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-sim-reverse-face",
        "Reverse simultaneous at τ: hold" in note
        and "Face simultaneous at τ: hold" in note
        and "Reverse holds." in note
        and "Face holds." in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-leftover-empty-fail",
        "not leftover-empty fail" in normalized_note
        and "HOLD iff simultaneous" in note
        and "O is not M" in note,
    )
    checks.check(
        "note-not-axis-cover-or-exist-opposite-leftover",
        "not leftover of nm2sl axis-cover" in normalized_note
        and "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover-of-`O` alone" in normalized_note
        and "not leftover of nmsimopp exist-opposite of `M`" in normalized_note,
    )
    checks.check(
        "note-not-nm2simz-or-forall-perp-or-1-in-2-out",
        "not leftover of nm2simy HOLDING" in normalized_note
        and "not leftover of nm2slo timed-O" in normalized_note
        and "not leftover of nm2slp forall-perp" in normalized_note
        and "not leftover of 1-in 2-out" in normalized_note
        and "neither pair is opposite" in normalized_note
        and "Reverse simultaneous at τ: hold" in note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-mixed-7188-fail-fail",
        "not leftover of mixed #7188 fail/fail" in normalized_note
        and "Reverse simultaneous at τ: hold" in note
        and "Face simultaneous at τ: hold" in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "Occupancy of sites is not used" in note
        and "Occupancy `n` is not used" in note
        and "does not use occupancy" in normalized_note,
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
        '    "docs/TWO_AXIS_SAME_LOCK_YPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "intersection_set" in defined_fns
        and "simultaneous" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
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
        "sim-hold-not-leftover-empty-fail",
        reverse == "hold"
        and face == "hold"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and all(sim[name] == "hold" for name in ("A", "B", "C", "D"))
        and cover_reverse == "hold"
        and cover_face == "fail"
        and forall_reverse == "hold"
        and opp_sim["A"] == "hold"
        and opp_z_sim["A"] == "hold"
        and z_reverse == "fail",
    )
    _ = (
        leftover_neighbor_reverse,
        unique_sim_b,
        axis_display,
        z_cover,
        xsame_sim,
        one_reverse,
        one_face,
        zsym_sim,
        incoming_set(E3, 1, zsym_ticks, zsym_locks, zsym_seeds),
        opp_reverse,
        opp_face,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
