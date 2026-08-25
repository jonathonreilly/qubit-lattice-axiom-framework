#!/usr/bin/env python3
"""Simultaneous M and O freeze t+2 versus t+3 on two-axis z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process and z-probes as nm2axz.
The second pair is a new seed, not a formed child. A 6-NN step is allowed
iff it is perpendicular to the parent lock axis. Newly formed sites lock the
incoming step. Seeds keep their seed letters as a singleton. t(q) is the
formation tick. tau1 = t+2. tau2 = t+3. No global T. Do not score tau=t.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is
the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is
formed and e is in M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is
empty, not UNDEFINED. Simultaneous HOLDs at q, tau iff both M and O are
defined nonempty and M intersect O is empty. UNDEFINED if M or O UNDEFINED.
Else fail. Reverse at a cut HOLDs iff simultaneous at A and at B. Face
likewise on C, D. Composition holds iff M(tau1)=M(tau2) and O(tau1)=O(tau2)
at A, B, C, and D. Uniqueness is not required. Occupancy of sites is not
used. Named-sign lettering is not used. No unique P_+. No 6-NN star. No
Cl(3,0). No Dijkstra. No Gram. No larger host. Not leftover of nm2simt2z
freeze t+1 versus t+2. Not leftover of nm2simz simultaneous at t+1 alone.
Not leftover of nm2ot3z O freeze. Not leftover of nmot2opp O at t versus
t+1. Not leftover of nmt2opp M two-tick. Displayed, not adopted. Do not
attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_ZPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_ZPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
Q_SEED: Point = (0, 1, 1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
AXES: tuple[Point, ...] = (E1, E2, E3)
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
TWO_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (Q_SEED, NEG_E2),
)
ONE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
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
    "S⁺",
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Simultaneous M and O at t+2 versus t+3 on the four "
    "z-probes of the two-axis opposite seed, reverse/face at each cut, and "
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


def named_sign(lock: Point) -> str:
    """Named sign of a lock vector. Contrast only; not the scored predicate."""
    if lock in POSITIVE_LOCKS:
        return "+"
    if lock in NEGATIVE_LOCKS:
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


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


def intersection_set(left: Incoming, right: Outgoing) -> Incoming:
    """M intersect O. Unformed on either side => UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("intersection sides must be lock sets or UNDEFINED")
    return left & right


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


def set_equal_composition(
    left_a: Incoming,
    right_a: Incoming,
    left_b: Incoming,
    right_b: Incoming,
    left_c: Incoming,
    right_c: Incoming,
    left_d: Incoming,
    right_d: Incoming,
) -> str:
    """Hold iff the four pairs of lock sets are equal. UNDEFINED if any side is."""
    sides = (left_a, right_a, left_b, right_b, left_c, right_c, left_d, right_d)
    if any(side == UNDEFINED for side in sides):
        return UNDEFINED
    if not all(isinstance(side, frozenset) for side in sides):
        return UNDEFINED
    if (
        left_a == right_a
        and left_b == right_b
        and left_c == right_c
        and left_d == right_d
    ):
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
    m_part = set_equal_composition(
        m1_a, m2_a, m1_b, m2_b, m1_c, m2_c, m1_d, m2_d
    )
    o_part = set_equal_composition(
        o1_a, o2_a, o1_b, o2_b, o1_c, o2_c, o1_d, o2_d
    )
    if m_part == UNDEFINED or o_part == UNDEFINED:
        return UNDEFINED
    if m_part == "hold" and o_part == "hold":
        return "hold"
    return "fail"


def leftover_bit_composition(rev1: str, rev2: str, face1: str, face2: str) -> str:
    """Leftover: score composition on reverse/face bits, not on M and O equality."""
    if rev1 != rev2 or face1 != face2:
        return "fail"
    return "hold"


def leftover_o_only_composition(
    o1_a: Outgoing,
    o2_a: Outgoing,
    o1_b: Outgoing,
    o2_b: Outgoing,
    o1_c: Outgoing,
    o2_c: Outgoing,
    o1_d: Outgoing,
    o2_d: Outgoing,
) -> str:
    """nm2ot3z leftover: freeze O only, ignore M."""
    return set_equal_composition(o1_a, o2_a, o1_b, o2_b, o1_c, o2_c, o1_d, o2_d)


def leftover_m_only_composition(
    m1_a: Incoming,
    m2_a: Incoming,
    m1_b: Incoming,
    m2_b: Incoming,
    m1_c: Incoming,
    m2_c: Incoming,
    m1_d: Incoming,
    m2_d: Incoming,
) -> str:
    """nmt2 leftover: freeze M only, ignore O."""
    return set_equal_composition(m1_a, m2_a, m1_b, m2_b, m1_c, m2_c, m1_d, m2_d)


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


def pair_cover(left: str, right: str) -> str:
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
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
    """Z^3 sum leftover of a lock set. Contrast only; not this letter."""
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


def probe_sim(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    delay: int = 1,
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = simultaneous(
            incoming_set(
                site, site_ticks[site] + delay, site_ticks, site_locks, site_seeds
            ),
            outgoing_set(
                site, site_ticks[site] + delay, site_ticks, site_locks, site_seeds
            ),
        )
    return out


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("two-axis opposite z-probe simultaneous M and O freeze t+2 versus t+3")
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
        and probe_sites != y_probe_sites
        and probe_sites != x_probe_sites,
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
        and add(E2, E3) == Q_SEED
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and in_ball(Q_SEED)
        and not in_ball((4, 0, 0)),
    )
    m_a = frozenset({E2})
    m_b = frozenset({E1})
    m_c = frozenset({E3})
    m_d = frozenset({E1})
    out_a = frozenset({E1, NEG_E1, E3})
    out_b = frozenset({E2, E3, NEG_E3})
    out_c = frozenset({E1, NEG_E1, NEG_E2})
    out_d = frozenset({NEG_E2, E3, NEG_E3})
    checks.check(
        "intersection-identity",
        intersection_set(UNDEFINED, frozenset({E1})) == UNDEFINED
        and intersection_set(frozenset({E1}), UNDEFINED) == UNDEFINED
        and intersection_set(frozenset({E1, E2}), frozenset({E2, E3}))
        == frozenset({E2})
        and intersection_set(frozenset({NEG_E1}), frozenset({E2, NEG_E2, E3}))
        == frozenset()
        and intersection_set(frozenset(), frozenset({E1})) == frozenset(),
    )
    checks.check(
        "simultaneous-identity",
        simultaneous(UNDEFINED, frozenset({E1})) == UNDEFINED
        and simultaneous(frozenset({E1}), UNDEFINED) == UNDEFINED
        and simultaneous(frozenset(), frozenset({E2, E3})) == "fail"
        and simultaneous(frozenset({NEG_E1}), frozenset()) == "fail"
        and simultaneous(frozenset({E2}), frozenset({E1, NEG_E1, E3})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({E1, E2})) == "fail"
        and simultaneous(frozenset({NEG_E3}), frozenset({E1, NEG_E1})) == "hold"
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
    grown_a = frozenset({E2, NEG_E3, E1})
    grown_m = frozenset({NEG_E1, E2})
    checks.check(
        "composition-identity",
        composition_report(
            m_a, m_a, out_a, out_a, m_b, m_b, out_b, out_b,
            m_c, m_c, out_c, out_c, m_d, m_d, out_d, out_d,
        )
        == "hold"
        and composition_report(
            m_a, m_a, out_a, grown_a, m_b, m_b, out_b, out_b,
            m_c, m_c, out_c, out_c, m_d, m_d, out_d, out_d,
        )
        == "fail"
        and composition_report(
            m_a, grown_m, out_a, out_a, m_b, m_b, out_b, out_b,
            m_c, m_c, out_c, out_c, m_d, m_d, out_d, out_d,
        )
        == "fail"
        and leftover_o_only_composition(
            out_a, out_a, out_b, out_b, out_c, out_c, out_d, out_d
        )
        == "hold"
        and leftover_o_only_composition(
            out_a, grown_a, out_b, out_b, out_c, out_c, out_d, out_d
        )
        == "fail"
        and leftover_o_only_composition(
            out_a, out_a, out_b, out_b, out_c, out_c, out_d, out_d
        )
        == "hold"
        and leftover_m_only_composition(m_a, grown_m, m_b, m_b, m_c, m_c, m_d, m_d)
        == "fail"
        and leftover_m_only_composition(m_a, m_a, m_b, m_b, m_c, m_c, m_d, m_d)
        == "hold"
        and composition_report(
            UNDEFINED, m_a, out_a, out_a, m_b, m_b, out_b, out_b,
            m_c, m_c, out_c, out_c, m_d, m_d, out_d, out_d,
        )
        == UNDEFINED
        and leftover_bit_composition("hold", "hold", "hold", "hold") == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail",
    )
    checks.check(
        "leftover-o-only-is-not-joint-when-M-moves",
        leftover_o_only_composition(
            out_a, out_a, out_b, out_b, out_c, out_c, out_d, out_d
        )
        == "hold"
        and leftover_m_only_composition(m_a, grown_m, m_b, m_b, m_c, m_c, m_d, m_d)
        == "fail"
        and composition_report(
            m_a, grown_m, out_a, out_a, m_b, m_b, out_b, out_b,
            m_c, m_c, out_c, out_c, m_d, m_d, out_d, out_d,
        )
        == "fail",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)

    tau0: dict[str, int] = {}
    tau_prev: dict[str, int] = {}
    tau1: dict[str, int] = {}
    tau2: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m_prev: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    m2: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o_prev: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    o2: dict[str, Outgoing] = {}
    inter1: dict[str, Incoming] = {}
    inter2: dict[str, Incoming] = {}
    sim0: dict[str, str] = {}
    sim_prev: dict[str, str] = {}
    sim1: dict[str, str] = {}
    sim2: dict[str, str] = {}
    lx1: dict[str, AxisSet] = {}
    lx_m1: dict[str, AxisSet] = {}
    lx_o1: dict[str, AxisSet] = {}
    cover1: dict[str, str] = {}
    cover2: dict[str, str] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
    new_meet2: dict[str, tuple[Point, ...]] = {}
    new_meet3: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau_prev[name] = ticks[site] + 1
        tau1[name] = ticks[site] + 2
        tau2[name] = ticks[site] + 3
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m_prev[name] = incoming_set(site, tau_prev[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        m2[name] = incoming_set(site, tau2[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o_prev[name] = outgoing_set(site, tau_prev[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        o2[name] = outgoing_set(site, tau2[name], ticks, locks, seed_map)
        inter1[name] = intersection_set(m1[name], o1[name])
        inter2[name] = intersection_set(m2[name], o2[name])
        sim0[name] = simultaneous(m0[name], o0[name])
        sim_prev[name] = simultaneous(m_prev[name], o_prev[name])
        sim1[name] = simultaneous(m1[name], o1[name])
        sim2[name] = simultaneous(m2[name], o2[name])
        lx1[name] = leftover_axis(m1[name], o1[name])
        lx_m1[name] = leftover_of_one(m1[name])
        lx_o1[name] = leftover_of_one(o1[name])
        cover1[name] = axis_cover(m1[name], o1[name])
        cover2[name] = axis_cover(m2[name], o2[name])
        new_meet1[name] = new_records_meeting_six_nn(site, ticks, 1)
        new_meet2[name] = new_records_meeting_six_nn(site, ticks, 2)
        new_meet3[name] = new_records_meeting_six_nn(site, ticks, 3)
        print(
            f"{name} t={ticks[site]} "
            f"M(tau1)={lockset_display(m1[name])} "
            f"O(tau1)={lockset_display(o1[name])} "
            f"sim(tau1)={sim1[name]} "
            f"M(tau2)={lockset_display(m2[name])} "
            f"O(tau2)={lockset_display(o2[name])} "
            f"sim(tau2)={sim2[name]}"
        )

    reverse1 = reverse_report(sim1["A"], sim1["B"])
    reverse2 = reverse_report(sim2["A"], sim2["B"])
    face1 = face_report(sim1["C"], sim1["D"])
    face2 = face_report(sim2["C"], sim2["D"])
    leftover_reverse0 = reverse_report(sim0["A"], sim0["B"])
    leftover_face0 = face_report(sim0["C"], sim0["D"])
    leftover_reverse_prev = reverse_report(sim_prev["A"], sim_prev["B"])
    leftover_face_prev = face_report(sim_prev["C"], sim_prev["D"])
    composition = composition_report(
        m1["A"], m2["A"], o1["A"], o2["A"],
        m1["B"], m2["B"], o1["B"], o2["B"],
        m1["C"], m2["C"], o1["C"], o2["C"],
        m1["D"], m2["D"], o1["D"], o2["D"],
    )
    leftover_nmot2opp_composition = composition_report(
        m0["A"], m_prev["A"], o0["A"], o_prev["A"],
        m0["B"], m_prev["B"], o0["B"], o_prev["B"],
        m0["C"], m_prev["C"], o0["C"], o_prev["C"],
        m0["D"], m_prev["D"], o0["D"], o_prev["D"],
    )
    leftover_nm2simt2z_composition = composition_report(
        m_prev["A"], m1["A"], o_prev["A"], o1["A"],
        m_prev["B"], m1["B"], o_prev["B"], o1["B"],
        m_prev["C"], m1["C"], o_prev["C"], o1["C"],
        m_prev["D"], m1["D"], o_prev["D"], o1["D"],
    )
    leftover_o_comp = leftover_o_only_composition(
        o1["A"], o2["A"], o1["B"], o2["B"], o1["C"], o2["C"], o1["D"], o2["D"]
    )
    leftover_m_comp = leftover_m_only_composition(
        m1["A"], m2["A"], m1["B"], m2["B"], m1["C"], m2["C"], m1["D"], m2["D"]
    )
    leftover_bits = leftover_bit_composition(reverse1, reverse2, face1, face2)
    leftover_empty_reverse = leftover_match(lx1["A"], lx1["B"])
    leftover_empty_face = leftover_match(lx1["C"], lx1["D"])
    reverse_m_alone = leftover_match(lx_m1["A"], lx_m1["B"])
    face_m_alone = leftover_match(lx_m1["C"], lx_m1["D"])
    reverse_o_alone = leftover_match(lx_o1["A"], lx_o1["B"])
    face_o_alone = leftover_match(lx_o1["C"], lx_o1["D"])
    m_exist_reverse = existential_opposite(m1["A"], m1["B"])
    m_exist_face = existential_opposite(m1["C"], m1["D"])
    o_exist_reverse = existential_opposite(o1["A"], o1["B"])
    o_exist_face = existential_opposite(o1["C"], o1["D"])
    o_exist_reverse2 = existential_opposite(o2["A"], o2["B"])
    o_exist_face2 = existential_opposite(o2["C"], o2["D"])
    cover_reverse1 = pair_cover(cover1["A"], cover1["B"])
    cover_face1 = pair_cover(cover1["C"], cover1["D"])
    cover_reverse2 = pair_cover(cover2["A"], cover2["B"])
    cover_face2 = pair_cover(cover2["C"], cover2["D"])
    unique_sim_a = simultaneous(unique_letter(m1["A"]), unique_letter(o1["A"]))
    neighbor_a = neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
    neighbor_b = neighbor_lock_set(PROBES["B"], ticks, locks, ticks[PROBES["B"]])
    leftover_neighbor_reverse = leftover_match(
        leftover_of_one(neighbor_a),
        leftover_of_one(neighbor_b),
    )
    print(f"reverse tau1={reverse1} tau2={reverse2}")
    print(f"face tau1={face1} tau2={face2}")
    print(f"composition={composition}")
    print(
        "per_element: each signed lock among {±e_1,±e_2,±e_3} in M or in O "
        "at a probe's t+2 and t+3"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four sim reports at t+2 and t+3, reverse/face at each cut, composition of M and O"
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
    ) and all(ticks.get(add(Q_SEED, step)) != 1 for step in (E2, NEG_E2))
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and second_pair_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[E3] == 0
        and ticks[Q_SEED] == 0
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
        and simultaneous(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and simultaneous(
            incoming_set(PROBES["C"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["C"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and simultaneous(
            incoming_set(PROBES["D"], 0, ticks, locks, seed_map),
            outgoing_set(PROBES["D"], 0, ticks, locks, seed_map),
        )
        == UNDEFINED
        and outgoing_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(Q_SEED, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
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
    checks.check(
        "theorem1-M-at-tau1",
        m1["A"] == m_a
        and m1["B"] == m_b
        and m1["C"] == m_c
        and m1["D"] == m_d,
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
        "theorem1-M-at-tau2",
        m2["A"] == m_a
        and m2["B"] == m_b
        and m2["C"] == m_c
        and m2["D"] == m_d,
        str({name: lockset_display(m2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau2",
        o2["A"] == out_a
        and o2["B"] == out_b
        and o2["C"] == out_c
        and o2["D"] == out_d,
        str({name: lockset_display(o2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-sim-at-tau1-and-tau2",
        all(sim1[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(sim2[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(
            isinstance(m1[name], frozenset)
            and isinstance(o1[name], frozenset)
            and bool(m1[name])
            and bool(o1[name])
            and m1[name].isdisjoint(o1[name])
            and m2[name] == m1[name]
            and o2[name] == o1[name]
            for name in ("A", "B", "C", "D")
        ),
        str(
            {
                name: (sim1[name], sim2[name])
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    checks.check(
        "theorem1-intersection-empty",
        all(
            inter1[name] == frozenset() and inter2[name] == frozenset()
            for name in ("A", "B", "C", "D")
        ),
        str({name: lockset_display(inter1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "do-not-score-tau-t",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset()
        and sim0["A"] == "fail"
        and sim0["B"] == "fail"
        and sim0["C"] == "fail"
        and sim0["D"] == "fail"
        and leftover_reverse0 == "fail"
        and leftover_face0 == "fail"
        and leftover_nmot2opp_composition == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and o0["A"] != o1["A"]
        and o0["D"] != o1["D"],
    )
    checks.check(
        "theorem1-M-and-O-freeze",
        all(m2[name] == m1[name] for name in ("A", "B", "C", "D"))
        and all(o2[name] == o1[name] for name in ("A", "B", "C", "D"))
        and all(m1[name] == m_prev[name] == m0[name] for name in ("A", "B", "C", "D"))
        and all(o1[name] == o_prev[name] for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet2["A"] == ((0, -1, 1),)
        and new_meet2["B"] == ()
        and new_meet2["C"] == ()
        and new_meet2["D"] == ()
        and new_meet3["A"] == ()
        and new_meet3["B"] == ((2, 1, 1),)
        and new_meet3["C"] == ()
        and new_meet3["D"] == ((2, 0, 1),)
        and new_meet1["A"] == ((1, 0, 1), (-1, 0, 1), (0, 0, 2))
        and new_meet1["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet1["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new_meet1["D"] == ((1, -1, 1), (1, 0, 2), (1, 0, 0)),
        str(
            {
                name: (new_meet2[name], new_meet3[name])
                for name in ("A", "B", "C", "D")
            }
        ),
    )
    child_of_a_tplus2 = (0, -1, 1)
    child_of_b_tplus3 = (2, 1, 1)
    child_of_d_tplus3 = (2, 0, 1)
    checks.check(
        "theorem1-new-tplus2-neighbor-does-not-enter-O",
        child_of_a_tplus2 in new_meet2["A"]
        and ticks[child_of_a_tplus2] == ticks[PROBES["A"]] + 2
        and incoming_set(child_of_a_tplus2, tau1["A"], ticks, locks, seed_map)
        == frozenset({E3})
        and NEG_E2 not in o1["A"]
        and o2["A"] == o1["A"],
    )
    checks.check(
        "theorem1-new-tplus3-neighbor-does-not-enter-O",
        child_of_b_tplus3 in new_meet3["B"]
        and child_of_d_tplus3 in new_meet3["D"]
        and ticks[child_of_b_tplus3] == ticks[PROBES["B"]] + 3
        and ticks[child_of_d_tplus3] == ticks[PROBES["D"]] + 3
        and incoming_set(child_of_b_tplus3, tau2["B"], ticks, locks, seed_map)
        == frozenset({NEG_E2, E3, NEG_E3})
        and incoming_set(child_of_d_tplus3, tau2["D"], ticks, locks, seed_map)
        == frozenset({E2, E3, NEG_E3})
        and E1 not in o2["B"]
        and E1 not in o2["D"]
        and E1 not in incoming_set(
            child_of_b_tplus3, tau2["B"], ticks, locks, seed_map
        )
        and E1 not in incoming_set(
            child_of_d_tplus3, tau2["D"], ticks, locks, seed_map
        )
        and o2["B"] == o1["B"]
        and o2["D"] == o1["D"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o2["A"], frozenset)
        and len(o2["A"]) == 3
        and unique_letter(o2["A"]) == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 3
        and unique_letter(o1["C"]) == UNDEFINED
        and sim1["A"] == "hold"
        and sim2["A"] == "hold",
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and m1["A"] == frozenset({E2})
        and ticks[Q_SEED] == 0
        and locks[Q_SEED] == {NEG_E2}
        and Y_PROBES["A"] != PROBES["A"]
        and X_PROBES["A"] != PROBES["A"],
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
        and reverse2 != "fail",
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
        and face1 != "fail"
        and face1 != UNDEFINED,
        f"{face1}/{face2}",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and leftover_m_comp == "hold"
        and leftover_o_comp == "hold"
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
        leftover_empty_reverse == "fail"
        and leftover_empty_face == "fail"
        and lx1["A"] == frozenset()
        and lx1["B"] == frozenset()
        and lx1["C"] == frozenset()
        and lx1["D"] == frozenset()
        and reverse1 == "hold"
        and face1 == "hold"
        and leftover_empty_reverse != reverse1
        and leftover_empty_face != face1,
    )
    checks.check(
        "mutation-leftover-of-M-alone-differs",
        lx_m1["A"] == frozenset({E1, E3})
        and lx_m1["B"] == frozenset({E2, E3})
        and lx_m1["C"] == frozenset({E1, E2})
        and lx_m1["D"] == frozenset({E2, E3})
        and reverse_m_alone == "fail"
        and face_m_alone == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and reverse_m_alone != reverse1
        and face_m_alone != face1,
    )
    checks.check(
        "mutation-leftover-of-O-alone-differs",
        lx_o1["A"] == frozenset({E2})
        and lx_o1["B"] == frozenset({E1})
        and lx_o1["C"] == frozenset({E3})
        and lx_o1["D"] == frozenset({E1})
        and reverse_o_alone == "fail"
        and face_o_alone == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and reverse_o_alone != reverse1
        and face_o_alone != face1,
    )
    checks.check(
        "mutation-exist-opposite-differs",
        m_exist_reverse == "fail"
        and m_exist_face == "fail"
        and o_exist_reverse == "hold"
        and o_exist_face == "fail"
        and o_exist_reverse2 == "hold"
        and o_exist_face2 == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and m_exist_reverse != reverse1
        and m_exist_face != face1
        and o_exist_face != face1,
    )
    y_cover_d = axis_cover(
        incoming_set(
            Y_PROBES["D"],
            ticks[Y_PROBES["D"]] + 2,
            ticks,
            locks,
            seed_map,
        ),
        outgoing_set(
            Y_PROBES["D"],
            ticks[Y_PROBES["D"]] + 2,
            ticks,
            locks,
            seed_map,
        ),
    )
    checks.check(
        "discriminator-sim-hold-vs-leftover-empty-and-exist-opposite",
        reverse1 == "hold"
        and face1 == "hold"
        and reverse2 == "hold"
        and face2 == "hold"
        and cover1["A"] == "hold"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "hold"
        and cover_reverse1 == "hold"
        and cover_face1 == "hold"
        and cover_reverse2 == "hold"
        and cover_face2 == "hold"
        and leftover_empty_reverse == "fail"
        and leftover_empty_face == "fail"
        and leftover_empty_face != face1
        and m_exist_reverse == "fail"
        and o_exist_face == "fail"
        and y_cover_d == "fail",
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-O",
        unique_letter(m1["A"]) == frozenset({E2})
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(m1["D"]) == frozenset({E1})
        and unique_letter(o1["D"]) == UNDEFINED
        and unique_sim_a == UNDEFINED
        and sim1["A"] == "hold"
        and sim2["A"] == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["A"], frozenset)
        and isinstance(m1["A"], frozenset)
        and sum_of_set(m1["A"]) == E2
        and sum_of_set(m1["D"]) == E1
        and sum_of_set(o1["A"]) == E3
        and sum_of_set(o1["C"]) == NEG_E2
        and o1["A"] != frozenset({E3}),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E2 in m1["A"]
        and E2 not in o1["A"]
        and o1["A"] != m1["A"]
        and o1["B"] != m1["B"]
        and o1["C"] != m1["C"]
        and o1["D"] != m1["D"]
        and inter1["A"] == frozenset()
        and m2["A"].isdisjoint(o2["A"]),
    )
    y_sim1 = probe_sim(Y_PROBES, ticks, locks, seed_map, 2)
    y_sim2 = probe_sim(Y_PROBES, ticks, locks, seed_map, 3)
    x_sim1 = probe_sim(X_PROBES, ticks, locks, seed_map, 2)
    perp_sim_map = probe_sim(PROBES, perp_ticks, perp_locks, perp_seeds, 2)
    zsym_sim = probe_sim(PROBES, zsym_ticks, zsym_locks, zsym_seeds, 2)
    one_sim = probe_sim(PROBES, one_ticks, one_locks, one_seeds, 2)
    y_reverse1 = reverse_report(y_sim1["A"], y_sim1["B"])
    y_face1 = face_report(y_sim1["C"], y_sim1["D"])
    y_reverse2 = reverse_report(y_sim2["A"], y_sim2["B"])
    y_face2 = face_report(y_sim2["C"], y_sim2["D"])
    x_reverse1 = reverse_report(x_sim1["A"], x_sim1["B"])
    x_face1 = face_report(x_sim1["C"], x_sim1["D"])
    perp_reverse = reverse_report(perp_sim_map["A"], perp_sim_map["B"])
    checks.check(
        "not-x-probes-or-y-probes-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and ticks[X_PROBES["A"]] == 2
        and x_sim1["A"] == "hold"
        and x_reverse1 == "hold"
        and x_face1 == "hold"
        and ticks[Y_PROBES["A"]] == 0
        and y_sim1["A"] == "hold"
        and y_reverse1 == "hold"
        and y_face1 == "hold"
        and y_reverse2 == "hold"
        and y_face2 == "hold"
        and m1["A"] == frozenset({E2})
        and m1["A"] != frozenset({NEG_E1})
        and perp_sim_map["B"] == "fail"
        and perp_reverse == "fail"
        and perp_reverse != reverse1
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "not-nsopp-leftover-second-pair-is-seed",
        TWO_AXIS_SEEDS != ONE_AXIS_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in one_ticks.values()) == 2
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and one_ticks[E3] == 1
        and one_ticks[Q_SEED] == 1
        and incoming_set(E3, 1, one_ticks, one_locks, one_seeds) == frozenset({E3})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and zsym_ticks[E3] == 0
        and zsym_locks[E3] == {NEG_E1}
        and one_sim["A"] == "hold"
        and zsym_sim["A"] == "hold"
        and sum(time == 0 for time in ysym_ticks.values()) == 3,
    )
    checks.check(
        "not-nnlock-named-sign",
        o1["A"] == frozenset({E1, NEG_E1, E3})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E2) == "+"
        and o1["A"] != named_sign(E2)
        and m1["A"] != named_sign(E2),
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
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 3
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 3
        and reverse1 == "hold"
        and face1 == "hold"
        and composition == "hold",
    )
    checks.check(
        "two-axis-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and ticks[Q_SEED] == 0
        and locks[Q_SEED] == {NEG_E2}
        and add(E1, NEG_E1) == ZERO
        and add(E2, NEG_E2) == ZERO,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    unformed = (0, 3, 0)
    checks.check(
        "empty-O-is-empty-not-undefined",
        outgoing_set(unformed, 0, ticks, locks, seed_map) == UNDEFINED
        and unformed not in ticks
        and isinstance(o0["A"], frozenset)
        and not o0["A"]
        and o0["A"] != UNDEFINED
        and simultaneous(m0["A"], o0["A"]) == "fail",
    )
    checks.check(
        "mutation-nmot2opp-tau-t-composition-fail",
        leftover_nmot2opp_composition == "fail"
        and leftover_reverse0 == "fail"
        and leftover_face0 == "fail"
        and composition == "hold",
    )
    checks.check(
        "not-leftover-nm2simt2z-tplus1-versus-tplus2",
        leftover_nm2simt2z_composition == "hold"
        and leftover_reverse_prev == "hold"
        and leftover_face_prev == "hold"
        and all(sim_prev[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(tau1[name] == ticks[PROBES[name]] + 2 for name in ("A", "B", "C", "D"))
        and all(tau2[name] == ticks[PROBES[name]] + 3 for name in ("A", "B", "C", "D"))
        and composition == "hold"
        and leftover_nmot2opp_composition == "fail",
    )
    checks.check(
        "mutation-bit-composition-leftover-is-not-M-and-O-sets",
        leftover_bits == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail"
        and composition_report(
            m_a, m_a, out_a, grown_a, m_b, m_b, out_b, out_b,
            m_c, m_c, out_c, out_c, m_d, m_d, out_d, out_d,
        )
        == "fail"
        and composition == "hold",
    )
    checks.check(
        "mutation-neighbor-lock-leftover-differs",
        neighbor_a != o1["A"]
        and neighbor_a != m1["A"]
        and neighbor_b != o1["B"]
        and reverse1 == "hold"
        and composition == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O-sim",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=1" in note
        and "M(A, τ1) = {+e_2}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_3}" in note
        and "M(D, τ1) = {+e_1}" in note
        and "O(A, τ1) = {+e_1, −e_1, +e_3}" in note
        and "O(B, τ1) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ1) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ1) = {−e_2, +e_3, −e_3}" in note
        and "M(A, τ2) = {+e_2}" in note
        and "M(B, τ2) = {+e_1}" in note
        and "M(C, τ2) = {+e_3}" in note
        and "M(D, τ2) = {+e_1}" in note
        and "O(A, τ2) = {+e_1, −e_1, +e_3}" in note
        and "O(B, τ2) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ2) = {+e_1, −e_1, −e_2}" in note
        and "O(D, τ2) = {−e_2, +e_3, −e_3}" in note
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
        "new 6-NN of A at t(A)+2: (0, -1, 1)" in note
        and "new 6-NN of B at t(B)+2: none" in note
        and "new 6-NN of C at t(C)+2: none" in note
        and "new 6-NN of D at t(D)+2: none" in note
        and "new 6-NN of A at t(A)+3: none" in note
        and "new 6-NN of B at t(B)+3: (2, 1, 1)" in note
        and "new 6-NN of C at t(C)+3: none" in note
        and "new 6-NN of D at t(D)+3: (2, 0, 1)" in note,
    )
    checks.check(
        "note-reports-reverse-face-composition",
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
        "note-not-o-freeze-alone-or-sim-tplus1-alone",
        "not leftover of nm2ot3z" in normalized_note
        and "not leftover of nm2simz" in normalized_note
        and "not leftover of nm2simt2z" in normalized_note
        and "Composition of M and O: hold" in note,
    )
    checks.check(
        "note-not-nmot2opp-t-versus-tplus1",
        "not leftover of nmot2opp" in normalized_note
        and "Do not score τ=t" in note,
    )
    checks.check(
        "note-not-m-two-tick-or-exist-opposite",
        "not leftover of nmt2opp" in normalized_note
        and "not leftover of nm2axoz timed-O exist-opposite" in normalized_note
        and "O is not M" in note,
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
        and "τ1(q)=t(q)+2" in note.replace(" ", "")
        and "τ2(q)=t(q)+3" in note.replace(" ", ""),
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-nsopp-leftover-child",
        "not a formed child" in normalized_note
        and "second pair is a new seed" in normalized_note,
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
        '    "docs/TWO_AXIS_OPPOSITE_ZPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    checks.check(
        "sim-hold-not-leftover-empty-fail",
        reverse1 == "hold"
        and face1 == "hold"
        and reverse2 == "hold"
        and face2 == "hold"
        and leftover_empty_reverse == "fail"
        and leftover_empty_face == "fail"
        and all(sim1[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(sim2[name] == "hold" for name in ("A", "B", "C", "D"))
        and composition == "hold"
        and lx1["D"] == frozenset(),
    )
    _ = (
        leftover_neighbor_reverse,
        ysym_locks,
        ysym_seeds,
        unique_sim_a,
        axis_display,
        leftover_bits,
        leftover_o_comp,
        leftover_m_comp,
        leftover_nm2simt2z_composition,
        leftover_reverse_prev,
        leftover_face_prev,
        y_face2,
        x_face1,
        tau0,
        tau_prev,
        new_meet1,
        y_cover_d,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
