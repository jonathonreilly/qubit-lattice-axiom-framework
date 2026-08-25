#!/usr/bin/env python3
"""Simultaneous M and O freeze t+1 versus t+2 reverse/face on same-lock x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is four sites in two disjoint same-lock pairs: origin and (0,1,0) lock
+e_1; (0,0,1) and (0,1,1) lock +e_2. Neither pair is opposite. Same process
and x-probes as nm2slpx. The second pair is a new seed, not a formed child.
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. t(q) is the formation tick. tau1 = t+1. tau2 = t+2. No global T.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is
the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is
formed and e is in M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is
empty, not UNDEFINED. Simultaneous HOLDs at q, tau iff both M and O are
defined nonempty and M intersect O is empty. UNDEFINED if M or O UNDEFINED.
Else fail. Reverse at a cut HOLDs iff simultaneous at A and at B at that
cut. Face likewise on C, D. Composition holds iff M(tau1)=M(tau2) and
O(tau1)=O(tau2) at A, B, C, and D. Uniqueness is not required. Occupancy of
sites is not used. Named-sign lettering is not used. No unique leftover
letter. No 6-NN star. No larger host. Not leftover of nm2simslx t+1 only.
Not leftover of nm2ot3slx O freeze exist-opposite. Not leftover of nmot2
O at t versus t+1. Not leftover of nmt2 M two-tick. Not leftover of nmout
eventual-O. Not leftover of axis-cover. Displayed, not adopted. Do not
attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_XPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Simultaneous M and O at t+1 versus t+2 on the four "
    "x-probes of the two-axis same-lock seed, reverse/face at each cut, "
    "and composition, are reported. Displayed, not adopted."
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


def named_sign(lock: Point) -> str:
    if lock in (E1, E2, E3):
        return "+"
    return "-"


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


def eventual_outgoing_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Outgoing:
    """nmout leftover: eventual neighbor locks, no t+1 versus t+2 cut."""
    if site not in ticks:
        return UNDEFINED
    outgoing: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        if step in locks[neighbor]:
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
    """nm2slpx leftover: hold iff every integer dot m·o is 0."""
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


def composition_report(
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
    """Hold iff M(tau1)=M(tau2) and O(tau1)=O(tau2) at A, B, C, and D."""
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
    if not all(isinstance(side, frozenset) for side in sides):
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


def leftover_bit_composition(rev1: str, rev2: str, face1: str, face2: str) -> str:
    """Leftover: score composition on reverse/face bits, not on M and O equality."""
    if rev1 != rev2 or face1 != face2:
        return "fail"
    return "hold"


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
    delay: int = 1,
) -> tuple[Point, ...]:
    """Records in B_3(0) that form at t(site)+delay and are 6-NN of site."""
    formation = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] == formation + delay:
            found.append(neighbor)
    return tuple(found)


def sum_of_set(locks: Incoming) -> Point | str:
    if locks == UNDEFINED:
        return UNDEFINED
    if not isinstance(locks, frozenset):
        raise TypeError(f"lock set is not a lock set: {locks!r}")
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
    delay: int = 1,
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = letter(
            incoming_set(
                site, site_ticks[site] + delay, site_ticks, site_locks, site_seeds
            ),
            outgoing_set(
                site, site_ticks[site] + delay, site_ticks, site_locks, site_seeds
            ),
        )
    return out


def probe_sim(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    delay: int = 1,
) -> dict[str, str]:
    return probe_map(probes, site_ticks, site_locks, site_seeds, simultaneous, delay)


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
        "simultaneous M and O freeze t+1 versus t+2 reverse/face "
        "on two-axis same-lock x-probes"
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E2, E3) == PAIR2
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and in_ball(PAIR2)
        and not in_ball((4, 0, 0)),
    )
    set_a = frozenset({NEG_E3})
    set_b = frozenset({E1})
    set_c = frozenset({E1})
    set_d = frozenset({NEG_E3})
    out_a = frozenset({E1})
    out_b = frozenset({E2, E3, NEG_E3})
    out_c = frozenset({NEG_E2, E3, NEG_E3})
    out_d = frozenset({E1})
    grown_a = frozenset({E1, NEG_E1})
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
        "composition-identity",
        composition_report(
            set_a, set_a, out_a, out_a, set_b, set_b, out_b, out_b,
            set_c, set_c, out_c, out_c, set_d, set_d, out_d, out_d,
        )
        == "hold"
        and composition_report(
            set_a, set_a, out_a, grown_a, set_b, set_b, out_b, out_b,
            set_c, set_c, out_c, out_c, set_d, set_d, out_d, out_d,
        )
        == "fail"
        and composition_report(
            UNDEFINED, set_a, out_a, out_a, set_b, set_b, out_b, out_b,
            set_c, set_c, out_c, out_c, set_d, set_d, out_d, out_d,
        )
        == UNDEFINED
        and leftover_bit_composition("hold", "hold", "hold", "hold") == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail",
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
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)

    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    tau2: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    m2: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    o2: dict[str, Outgoing] = {}
    inter1: dict[str, Incoming] = {}
    inter2: dict[str, Incoming] = {}
    sim1: dict[str, str] = {}
    sim2: dict[str, str] = {}
    cover1: dict[str, str] = {}
    cover2: dict[str, str] = {}
    split1: dict[str, str] = {}
    forall1: dict[str, str] = {}
    lx: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_o: dict[str, AxisSet] = {}
    o_eventual: dict[str, Outgoing] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
    new_meet2: dict[str, tuple[Point, ...]] = {}
    one_m1: dict[str, Incoming] = {}
    one_o1: dict[str, Outgoing] = {}
    one_o2: dict[str, Outgoing] = {}
    one_sim1: dict[str, str] = {}
    one_sim2: dict[str, str] = {}
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
        inter1[name] = intersection_set(m1[name], o1[name])
        inter2[name] = intersection_set(m2[name], o2[name])
        sim1[name] = simultaneous(m1[name], o1[name])
        sim2[name] = simultaneous(m2[name], o2[name])
        cover1[name] = axis_cover(m1[name], o1[name])
        cover2[name] = axis_cover(m2[name], o2[name])
        split1[name] = one_two_split(m1[name], o1[name])
        forall1[name] = forall_orthogonal(m1[name], o1[name])
        lx[name] = leftover_axis(m1[name], o1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_o[name] = leftover_of_one(o1[name])
        o_eventual[name] = eventual_outgoing_set(site, ticks, locks)
        new_meet1[name] = new_records_meeting_six_nn(site, ticks, 1)
        new_meet2[name] = new_records_meeting_six_nn(site, ticks, 2)
        one_m1[name] = incoming_set(
            site, one_ticks[site] + 1, one_ticks, one_locks, one_seeds
        )
        one_o1[name] = outgoing_set(
            site, one_ticks[site] + 1, one_ticks, one_locks, one_seeds
        )
        one_o2[name] = outgoing_set(
            site, one_ticks[site] + 2, one_ticks, one_locks, one_seeds
        )
        one_sim1[name] = simultaneous(one_m1[name], one_o1[name])
        one_sim2[name] = simultaneous(
            incoming_set(site, one_ticks[site] + 2, one_ticks, one_locks, one_seeds),
            one_o2[name],
        )
        print(
            f"{name} t={ticks[site]} "
            f"M(tau1)={lockset_display(m1[name])} "
            f"O(tau1)={lockset_display(o1[name])} "
            f"sim1={sim1[name]} "
            f"M(tau2)={lockset_display(m2[name])} "
            f"O(tau2)={lockset_display(o2[name])} "
            f"sim2={sim2[name]}"
        )

    leftover_sim0_a = simultaneous(m0["A"], o0["A"])
    leftover_sim0_b = simultaneous(m0["B"], o0["B"])
    leftover_sim0_c = simultaneous(m0["C"], o0["C"])
    leftover_sim0_d = simultaneous(m0["D"], o0["D"])
    leftover_reverse0 = reverse_report(leftover_sim0_a, leftover_sim0_b)
    leftover_face0 = face_report(leftover_sim0_c, leftover_sim0_d)
    reverse1 = reverse_report(sim1["A"], sim1["B"])
    reverse2 = reverse_report(sim2["A"], sim2["B"])
    face1 = face_report(sim1["C"], sim1["D"])
    face2 = face_report(sim2["C"], sim2["D"])
    composition = composition_report(
        m1["A"], m2["A"], o1["A"], o2["A"],
        m1["B"], m2["B"], o1["B"], o2["B"],
        m1["C"], m2["C"], o1["C"], o2["C"],
        m1["D"], m2["D"], o1["D"], o2["D"],
    )
    leftover_nmot2_composition = composition_report(
        m0["A"], m1["A"], o0["A"], o1["A"],
        m0["B"], m1["B"], o0["B"], o1["B"],
        m0["C"], m1["C"], o0["C"], o1["C"],
        m0["D"], m1["D"], o0["D"], o1["D"],
    )
    leftover_bits = leftover_bit_composition(reverse1, reverse2, face1, face2)
    leftover_reverse = leftover_match(lx["A"], lx["B"])
    leftover_face = leftover_match(lx["C"], lx["D"])
    reverse_m_alone = leftover_match(lx_m["A"], lx_m["B"])
    face_m_alone = leftover_match(lx_m["C"], lx_m["D"])
    reverse_o_alone = leftover_match(lx_o["A"], lx_o["B"])
    face_o_alone = leftover_match(lx_o["C"], lx_o["D"])
    m_exist_reverse1 = existential_opposite(m1["A"], m1["B"])
    m_exist_face1 = existential_opposite(m1["C"], m1["D"])
    o_exist_reverse1 = existential_opposite(o1["A"], o1["B"])
    o_exist_face1 = existential_opposite(o1["C"], o1["D"])
    o_exist_reverse2 = existential_opposite(o2["A"], o2["B"])
    o_exist_face2 = existential_opposite(o2["C"], o2["D"])
    unique_sim_b = simultaneous(unique_letter(m1["B"]), unique_letter(o1["B"]))
    leftover_neighbor_reverse = leftover_match(
        leftover_of_one(
            neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
        ),
        leftover_of_one(
            neighbor_lock_set(PROBES["B"], ticks, locks, ticks[PROBES["B"]])
        ),
    )
    leftover_neighbor_face = leftover_match(
        leftover_of_one(
            neighbor_lock_set(PROBES["C"], ticks, locks, ticks[PROBES["C"]])
        ),
        leftover_of_one(
            neighbor_lock_set(PROBES["D"], ticks, locks, ticks[PROBES["D"]])
        ),
    )
    cover_reverse1 = reverse_report(cover1["A"], cover1["B"])
    cover_face1 = face_report(cover1["C"], cover1["D"])
    cover_reverse2 = reverse_report(cover2["A"], cover2["B"])
    cover_face2 = face_report(cover2["C"], cover2["D"])
    split_reverse = reverse_report(split1["A"], split1["B"])
    split_face = face_report(split1["C"], split1["D"])
    forall_reverse = reverse_report(forall1["A"], forall1["B"])
    forall_face = face_report(forall1["C"], forall1["D"])
    one_reverse1 = reverse_report(one_sim1["A"], one_sim1["B"])
    one_face1 = face_report(one_sim1["C"], one_sim1["D"])
    one_reverse2 = reverse_report(one_sim2["A"], one_sim2["B"])
    one_face2 = face_report(one_sim2["C"], one_sim2["D"])
    opp_sim = probe_sim(PROBES, opp_ticks, opp_locks, opp_seeds)
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
    print(f"reverse tau1={reverse1} tau2={reverse2}")
    print(f"face tau1={face1} tau2={face2}")
    print(f"composition={composition}")
    print(
        "per_element: each signed lock among {±e_1,±e_2,±e_3} in M or in O "
        "at a probe's t+1 or t+2"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four sim reports at two cuts plus reverse/face/composition"
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
    ) and all(ticks.get(add(PAIR2, step)) != 1 for step in (E2, NEG_E2))
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and second_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[E3] == 0
        and ticks[PAIR2] == 0
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
        and outgoing_set(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["C"], 2, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED
        and simultaneous(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
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
        ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau1",
        m1["A"] == set_a
        and m1["B"] == set_b
        and m1["C"] == set_c
        and m1["D"] == set_d,
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau1",
        o1["A"] == out_a
        and o1["B"] == out_b
        and o1["C"] == out_c
        and o1["D"] == out_d,
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-O-at-tau2-freeze",
        m2["A"] == m1["A"]
        and m2["B"] == m1["B"]
        and m2["C"] == m1["C"]
        and m2["D"] == m1["D"]
        and o2["A"] == o1["A"]
        and o2["B"] == o1["B"]
        and o2["C"] == o1["C"]
        and o2["D"] == o1["D"]
        and m1["A"] == m0["A"],
        str({name: lockset_display(o2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-intersection-and-sim-at-both-cuts",
        all(inter1[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(inter2[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(sim1[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(sim2[name] == "hold" for name in ("A", "B", "C", "D")),
        str({name: (sim1[name], sim2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "do-not-score-tau-t",
        all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and leftover_sim0_a == "fail"
        and leftover_sim0_b == "fail"
        and leftover_sim0_c == "fail"
        and leftover_sim0_d == "fail"
        and leftover_reverse0 == "fail"
        and leftover_face0 == "fail"
        and leftover_nmot2_composition == "fail"
        and o0["A"] != o1["A"],
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
        "theorem1-mixed-stays-a-set",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_sim_b == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 3
        and unique_letter(o1["C"]) == UNDEFINED
        and sim1["B"] == "hold"
        and sim1["C"] == "hold"
        and sim2["B"] == "hold",
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and ticks[E1] == 2
        and locks[E1] == {NEG_E3}
        and m1["A"] == frozenset({NEG_E3})
        and PROBES["A"] not in seed_map
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "compare-nm2simz-holding",
        all(opp_z_sim[name] == "hold" for name in ("A", "B", "C", "D"))
        and opp_z_reverse == "hold"
        and opp_z_face == "hold"
        and ticks[PROBES["A"]] == 2
        and m1["A"] == frozenset({NEG_E3})
        and reverse1 == "hold"
        and face1 == "hold"
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS,
    )
    checks.check(
        "compare-nm2slpx-forall-perp",
        all(forall1[name] == "hold" for name in ("A", "B", "C", "D"))
        and forall_reverse == "hold"
        and forall_face == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and simultaneous(frozenset({E1}), frozenset({NEG_E1})) == "hold",
    )
    checks.check(
        "compare-nm2slx-cover-fail",
        cover1["A"] == "fail"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail"
        and cover_reverse1 == "fail"
        and cover_face1 == "fail"
        and cover_reverse2 == "fail"
        and cover_face2 == "fail"
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "compare-1-in-2-out-fail",
        split1["A"] == "fail"
        and split1["B"] == "hold"
        and split1["C"] == "hold"
        and split1["D"] == "fail"
        and split_reverse == "fail"
        and split_face == "fail"
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "compare-1-axis-same-lock-x",
        one_ticks[PROBES["A"]] == 3
        and one_ticks[PROBES["B"]] == 2
        and one_ticks[PROBES["C"]] == 4
        and one_ticks[PROBES["D"]] == 3
        and ticks[PROBES["A"]] == 2
        and one_o1["A"] == frozenset({E1})
        and one_o2["A"] == one_o1["A"]
        and one_reverse1 == "hold"
        and one_face1 == "hold"
        and one_reverse2 == "hold"
        and one_face2 == "hold"
        and m1["A"] != one_m1["A"],
    )
    checks.check(
        "theorem2-reverse-tau1-and-tau2-hold",
        reverse1 == "hold"
        and reverse2 == "hold"
        and sim1["A"] == "hold"
        and sim1["B"] == "hold"
        and sim2["A"] == "hold"
        and sim2["B"] == "hold"
        and reverse1 != UNDEFINED
        and reverse1 != "fail"
        and o_exist_reverse1 == "fail"
        and cover_reverse1 == "fail",
        f"{reverse1}/{reverse2}",
    )
    checks.check(
        "theorem2-face-tau1-and-tau2-hold",
        face1 == "hold"
        and face2 == "hold"
        and sim1["C"] == "hold"
        and sim1["D"] == "hold"
        and sim2["C"] == "hold"
        and sim2["D"] == "hold"
        and face1 != UNDEFINED
        and face1 != "fail"
        and o_exist_face1 == "fail"
        and cover_face1 == "fail",
        f"{face1}/{face2}",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and m2["A"] == m1["A"]
        and o2["A"] == o1["A"]
        and m2["B"] == m1["B"]
        and o2["B"] == o1["B"]
        and m2["C"] == m1["C"]
        and o2["C"] == o1["C"]
        and m2["D"] == m1["D"]
        and o2["D"] == o1["D"]
        and reverse2 == reverse1
        and face2 == face1,
        composition,
    )
    checks.check(
        "not-leftover-empty-fail",
        leftover_reverse == "fail"
        and leftover_face == "fail"
        and lx["A"] == frozenset({E2})
        and lx["B"] == frozenset()
        and lx["C"] == frozenset()
        and lx["D"] == frozenset({E2})
        and reverse1 == "hold"
        and face1 == "hold"
        and leftover_reverse != reverse1
        and leftover_face != face1,
    )
    checks.check(
        "not-leftover-of-M-alone",
        reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and lx_m["A"] == frozenset({E1, E2})
        and lx_m["B"] == frozenset({E2, E3})
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "not-leftover-of-O-alone",
        reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and lx_o["A"] == frozenset({E2, E3})
        and lx_o["B"] == frozenset({E1})
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "not-exist-opposite-of-M-or-O",
        m_exist_reverse1 == "fail"
        and m_exist_face1 == "fail"
        and o_exist_reverse1 == "fail"
        and o_exist_face1 == "fail"
        and o_exist_reverse2 == "fail"
        and o_exist_face2 == "fail"
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E3 in m1["A"]
        and NEG_E3 not in o1["A"]
        and o1["A"] != m1["A"]
        and o1["B"] != m1["B"]
        and o1["C"] != m1["C"]
        and o1["D"] != m1["D"]
        and m1["A"].isdisjoint(o1["A"]),
    )
    y_sim = probe_sim(Y_PROBES, ticks, locks, seed_map)
    z_sim = probe_sim(Z_PROBES, ticks, locks, seed_map)
    y_reverse = reverse_report(y_sim["A"], y_sim["B"])
    y_face = face_report(y_sim["C"], y_sim["D"])
    z_reverse = reverse_report(z_sim["A"], z_sim["B"])
    z_face = face_report(z_sim["C"], z_sim["D"])
    nsopp_sim = probe_sim(PROBES, nsopp_ticks, nsopp_locks, nsopp_seeds)
    perp_sim_map = probe_sim(PROBES, perp_ticks, perp_locks, perp_seeds)
    zsym_sim = probe_sim(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    xsame_sim = probe_sim(PROBES, xsame_ticks, xsame_locks, xsame_seeds)
    checks.check(
        "not-y-probes-or-z-probes",
        FOUR_SITE_SEEDS != X_AXIS_SAME_SEEDS
        and FOUR_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and y_sim["D"] == "hold"
        and y_face == "hold"
        and y_reverse == "hold"
        and z_sim["A"] == "fail"
        and z_reverse == "fail"
        and z_face == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in ysym_ticks.values()) == 3,
    )
    checks.check(
        "not-two-axis-opposite",
        FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
        and FOUR_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and o1["D"] == frozenset({E1})
        and opp_o_d == frozenset({E1, NEG_E1})
        and NEG_E1 not in o1["D"]
        and NEG_E1 in opp_o_d
        and o1["D"] != opp_o_d
        and locks[E2] == {E1}
        and opp_locks[E2] == {NEG_E1}
        and opp_sim["A"] == "hold"
        and reverse1 == "hold"
        and zsym_ticks[E3] == 0
        and zsym_locks[E3] == {NEG_E1},
    )
    checks.check(
        "not-nsopp-or-perp",
        FOUR_SITE_SEEDS != NSOPP_SEEDS
        and FOUR_SITE_SEEDS != PERP_SEEDS
        and nsopp_sim["A"] == "hold"
        and ticks[PROBES["A"]] == 2
        and m1["A"] == frozenset({NEG_E3})
        and reverse_report(perp_sim_map["A"], perp_sim_map["B"]) != reverse1
        and reverse1 == "hold",
    )
    checks.check(
        "not-nnlock-named-sign",
        o1["A"] == frozenset({E1})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E2) == "+"
        and o1["A"] != named_sign(E1)
        and m1["A"] != named_sign(NEG_E3),
    )
    checks.check(
        "outgoing-locks-are-nn-steps",
        all(
            isinstance(o1[name], frozenset) and o1[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        )
        and all(
            isinstance(o2[name], frozenset) and o2[name] <= set(NN)
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 3
        and reverse1 == "hold"
        and face1 == "hold"
        and composition == "hold",
    )
    checks.check(
        "two-axis-same-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {E1}
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[PAIR2] == 0
        and locks[PAIR2] == {E2}
        and add(E1, E1) != ZERO
        and add(E2, E2) != ZERO
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS
        and FOUR_SITE_SEEDS != PERP_SEEDS
        and FOUR_SITE_SEEDS != Y_SYMMETRIC_SEEDS,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    unformed = (0, 0, 3)
    checks.check(
        "empty-O-is-empty-not-undefined",
        outgoing_set(unformed, 0, ticks, locks, seed_map) == UNDEFINED
        and unformed not in ticks
        and isinstance(o0["A"], frozenset)
        and not o0["A"]
        and o0["A"] != UNDEFINED
        and isinstance(o0["B"], frozenset)
        and not o0["B"],
    )
    checks.check(
        "empty-intersection-is-empty-not-undefined",
        all(
            inter1[name] == frozenset() and inter1[name] != UNDEFINED
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "mutation-nmot2opp-tau-t-composition-fail",
        leftover_nmot2_composition == "fail"
        and leftover_reverse0 == "fail"
        and leftover_face0 == "fail"
        and composition == "hold",
    )
    checks.check(
        "mutation-nmoutopp-eventual-O",
        o_eventual["A"] == o1["A"]
        and o_eventual["B"] == o1["B"]
        and o_eventual["C"] == o1["C"]
        and o_eventual["D"] == o1["D"]
        and o_eventual["A"] == o2["A"],
    )
    checks.check(
        "mutation-bit-composition-leftover-is-not-sets",
        leftover_bits == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail"
        and composition == "hold",
    )
    checks.check(
        "mutation-unique-L-outgoing-would-be-undefined",
        unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_sim_b == UNDEFINED
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        sum_of_set(m1["A"]) == NEG_E3
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["B"]) == E2
        and sum_of_set(o1["C"]) == NEG_E2
        and sum_of_set(o1["D"]) == E1
        and o1["B"] != frozenset({E2})
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3,
    )
    checks.check(
        "mutation-neighbor-lock-leftover-differs",
        neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
        != o1["A"]
        and neighbor_lock_set(PROBES["D"], ticks, locks, ticks[PROBES["D"]])
        != o1["D"]
        and leftover_neighbor_reverse == "fail"
        and leftover_neighbor_reverse != reverse1
        and leftover_neighbor_face == "hold",
    )
    checks.check(
        "not-nsopp-leftover-child",
        FOUR_SITE_SEEDS != ONE_AXIS_SEEDS
        and seed_map[E3] == E2
        and seed_map[PAIR2] == E2
        and ticks[E3] == 0
        and ticks[PAIR2] == 0
        and one_ticks[E3] == 1
        and one_ticks[PAIR2] == 1
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in ticks.values()) == 4,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-sets",
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
        and "O(A, τ2) = {+e_1}" in note
        and "O(B, τ2) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ2) = {−e_2, +e_3, −e_3}" in note
        and "O(D, τ2) = {+e_1}" in note
        and "sim(A, τ1) = hold" in note
        and "sim(B, τ1) = hold" in note
        and "sim(C, τ1) = hold" in note
        and "sim(D, τ1) = hold" in note
        and "sim(A, τ2) = hold" in note
        and "sim(B, τ2) = hold" in note
        and "sim(C, τ2) = hold" in note
        and "sim(D, τ2) = hold" in note,
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
        "note-reports-hold-hold-composition-hold",
        "Reverse at τ1: hold" in note
        and "Reverse at τ2: hold" in note
        and "Face at τ1: hold" in note
        and "Face at τ2: hold" in note
        and "Composition of M and O: hold" in note
        and "UNDEFINED" in note,
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
        "not leftover of nm2slx axis-cover" in normalized_note
        and "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover-of-`O` alone" in normalized_note
        and "not leftover of nmsimopp exist-opposite of `M`" in normalized_note,
    )
    checks.check(
        "note-not-nm2simz-or-forall-perp-or-1-in-2-out",
        "not leftover of nm2simz HOLDING" in normalized_note
        and "not leftover of nm2slpx forall-perp" in normalized_note
        and "not leftover of 1-in 2-out" in normalized_note
        and "neither pair is opposite" in normalized_note,
    )
    checks.check(
        "note-not-nm2simslx-or-ot3slx",
        "not leftover of nm2simslx simultaneous at" in normalized_note
        and "not leftover of nm2ot3slx O freeze" in normalized_note
        and "not leftover of two-axis opposite simultaneous freeze"
        in normalized_note,
    )
    checks.check(
        "note-not-nmot2-t-versus-tplus1",
        "not leftover of nmot2" in normalized_note
        and "Do not score τ=t" in note,
    )
    checks.check(
        "note-not-m-two-tick-or-eventual-o",
        "not leftover of nmt2" in normalized_note
        and "not leftover of nmout" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-not-sign-lettering",
        "not named-sign lettering" in normalized_note
        and "lost the axis" in normalized_note,
    )
    checks.check(
        "note-does-not-attach-formation-member",
        "does not attach a formation member from already-recorded six-neighbor locks"
        in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-unique-or-sum-or-star-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "Face holds at τ1 and at τ2." in note
        and "Reverse holds at τ1 and at τ2." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-not-nsopp-leftover-child",
        "not a formed child" in normalized_note
        and "second pair is a new seed" in normalized_note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ1(q)=t(q)+1" in note.replace(" ", "")
        and "τ2(q)=t(q)+2" in note.replace(" ", ""),
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "Occupancy of sites is not used" in note
        and "Occupancy `n` is not used" in note
        and "does not use occupancy" in normalized_note,
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
        all(line in allowed_retained and line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/TWO_AXIS_SAME_LOCK_XPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "composition_report" in defined_fns
        and "form" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
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
        "source-letter-from-simultaneous-freeze",
        "simultaneous" in defined_fns
        and "composition_report" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )
    checks.check(
        "sim-hold-not-leftover-empty-fail",
        reverse1 == "hold"
        and face1 == "hold"
        and leftover_reverse == "fail"
        and leftover_face == "fail"
        and all(sim1[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(sim2[name] == "hold" for name in ("A", "B", "C", "D"))
        and cover_reverse1 == "fail"
        and forall_reverse == "hold"
        and o_exist_reverse1 == "fail"
        and z_reverse == "fail"
        and composition == "hold",
    )
    _ = (
        leftover_neighbor_face,
        leftover_neighbor_reverse,
        ysym_locks,
        ysym_seeds,
        tau0,
        leftover_bits,
        axis_display,
        xsame_sim,
        zsym_sim,
        opp_sim,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
