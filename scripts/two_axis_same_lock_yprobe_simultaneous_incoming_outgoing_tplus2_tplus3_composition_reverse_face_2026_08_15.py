#!/usr/bin/env python3
"""Simultaneous M and O freeze t+2 versus t+3 on two-axis same-lock y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint same-lock pairs: origin and (0,1,0) lock +e_1; (0,0,1)
and (0,1,1) lock +e_2. Same process and y-probes as nm2slo. A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. Seeds keep their seed letters as a singleton.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is
the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is
formed and e is in M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is
empty, not UNDEFINED. Sim HOLD at q, tau iff M and O defined nonempty and
M intersect O empty. UNDEFINED if M or O UNDEFINED. Else fail. Reverse/face
at a cut from sim at A,B and C,D. Composition HOLD iff M(tau1)=M(tau2) and
O(tau1)=O(tau2) at A,B,C,D. tau1=t+2, tau2=t+3. Do not score tau=t. No
global T. Uniqueness is not required. Occupancy n is not used. Named-sign
lettering is not used. No unique P_+. No larger host. Displayed, not
adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_YPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_YPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_AXIS_SAME_LOCK_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    (PAIR2, E2),
)
ONE_AXIS_SAME_LOCK_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
)
TWO_AXIS_OPPOSITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
NSOPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
)
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
)
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
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
    "y-probes of the two-axis same-lock seed, reverse/face at each "
    "cut, and composition, are reported. Displayed, not adopted."
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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_SAME_LOCK_SEEDS,
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


def composition_report(rev1: str, rev2: str, face1: str, face2: str) -> str:
    """Leftover: HOLD iff t+3 reverse/face bits equal the t+2 bits."""
    if rev1 != rev2 or face1 != face2:
        return "fail"
    return "HOLD"


def composition_from_mo(
    m_first: dict[str, Incoming],
    m_second: dict[str, Incoming],
    o_first: dict[str, Outgoing],
    o_second: dict[str, Outgoing],
) -> str:
    """HOLD iff M(tau1)=M(tau2) and O(tau1)=O(tau2) at A,B,C,D."""
    for name in ("A", "B", "C", "D"):
        if m_first[name] != m_second[name] or o_first[name] != o_second[name]:
            return "fail"
    return "HOLD"


def composition_from_incoming(
    first: dict[str, Incoming],
    second: dict[str, Incoming],
) -> str:
    """Leftover M-only freeze: HOLD iff M(first)=M(second) at A,B,C,D."""
    for name in ("A", "B", "C", "D"):
        if first[name] != second[name]:
            return "fail"
    return "HOLD"


def composition_from_outgoing(
    first: dict[str, Outgoing],
    second: dict[str, Outgoing],
) -> str:
    """Leftover O-only freeze: HOLD iff O(first)=O(second) at A,B,C,D."""
    for name in ("A", "B", "C", "D"):
        if first[name] != second[name]:
            return "fail"
    return "HOLD"


def axis_set(value: Incoming) -> AxisSet:
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
    """Unsigned-axis cover leftover. Not this simultaneous letter."""
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


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Signed exist-opposite leftover. Not this reverse from sim."""
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
    return new_records_meeting_six_nn_at(site, ticks, 1)


def new_records_meeting_six_nn_at(
    site: Point,
    ticks: dict[Point, int],
    offset: int,
) -> tuple[Point, ...]:
    """Records in B_3(0) that form at t(site)+offset and are 6-NN of site."""
    formation = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor in ticks and ticks[neighbor] == formation + offset:
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("simultaneous M and O freeze t+2 versus t+3 on two-axis same-lock y-probes")
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
        "simultaneous-identity",
        simultaneous(UNDEFINED, frozenset({E1})) == UNDEFINED
        and simultaneous(frozenset({E1}), UNDEFINED) == UNDEFINED
        and simultaneous(frozenset(), frozenset({E2, E3})) == "fail"
        and simultaneous(frozenset({NEG_E1}), frozenset()) == "fail"
        and simultaneous(frozenset({NEG_E3}), frozenset({E1})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({E2, E3, NEG_E3})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({NEG_E1})) == "hold"
        and simultaneous(frozenset({E1}), frozenset({E1, E2})) == "fail",
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
        composition_report("hold", "hold", "hold", "hold") == "HOLD"
        and composition_report("fail", "fail", "fail", "fail") == "HOLD"
        and composition_report(UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED) == "HOLD"
        and composition_report(UNDEFINED, "hold", UNDEFINED, "hold") == "fail"
        and composition_report("hold", "hold", "hold", "fail") == "fail",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SAME_LOCK_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPPOSITE_SEEDS)
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    tau0: dict[str, int] = {}
    tau_mid: dict[str, int] = {}
    tau1: dict[str, int] = {}
    tau2: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m_mid: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    m2: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o_mid: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    o2: dict[str, Outgoing] = {}
    inter1: dict[str, Incoming] = {}
    inter2: dict[str, Incoming] = {}
    sim0: dict[str, str] = {}
    sim_mid: dict[str, str] = {}
    sim1: dict[str, str] = {}
    sim2: dict[str, str] = {}
    cover: dict[str, str] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
    new_meet2: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau_mid[name] = ticks[site] + 1
        tau1[name] = ticks[site] + 2
        tau2[name] = ticks[site] + 3
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m_mid[name] = incoming_set(site, tau_mid[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        m2[name] = incoming_set(site, tau2[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o_mid[name] = outgoing_set(site, tau_mid[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        o2[name] = outgoing_set(site, tau2[name], ticks, locks, seed_map)
        inter1[name] = intersection_set(m1[name], o1[name])
        inter2[name] = intersection_set(m2[name], o2[name])
        sim0[name] = simultaneous(m0[name], o0[name])
        sim_mid[name] = simultaneous(m_mid[name], o_mid[name])
        sim1[name] = simultaneous(m1[name], o1[name])
        sim2[name] = simultaneous(m2[name], o2[name])
        cover[name] = axis_cover(m1[name], o1[name])
        new_meet1[name] = new_records_meeting_six_nn_at(site, ticks, 2)
        new_meet2[name] = new_records_meeting_six_nn_at(site, ticks, 3)
        print(
            f"{name} t={ticks[site]} "
            f"M(tau1)={lockset_display(m1[name])} "
            f"O(tau1)={lockset_display(o1[name])} "
            f"M(tau2)={lockset_display(m2[name])} "
            f"O(tau2)={lockset_display(o2[name])} "
            f"sim1={sim1[name]} sim2={sim2[name]}"
        )

    reverse0 = reverse_report(sim0["A"], sim0["B"])
    reverse_mid = reverse_report(sim_mid["A"], sim_mid["B"])
    reverse1 = reverse_report(sim1["A"], sim1["B"])
    reverse2 = reverse_report(sim2["A"], sim2["B"])
    face0 = face_report(sim0["C"], sim0["D"])
    face_mid = face_report(sim_mid["C"], sim_mid["D"])
    face1 = face_report(sim1["C"], sim1["D"])
    face2 = face_report(sim2["C"], sim2["D"])
    bit_composition = composition_report(reverse1, reverse2, face1, face2)
    composition = composition_from_mo(m1, m2, o1, o2)
    leftover_empty_at_t = composition_from_mo(m0, m_mid, o0, o_mid)
    leftover_tplus1_tplus2 = composition_from_mo(m_mid, m1, o_mid, o1)
    leftover_m_only = composition_from_incoming(m1, m2)
    leftover_o_only = composition_from_outgoing(o1, o2)
    leftover_m_from_t = composition_from_incoming(m0, m_mid)
    leftover_o_from_t = composition_from_outgoing(o0, o_mid)
    o_exist_reverse1 = existential_opposite(o1["A"], o1["B"])
    o_exist_face1 = existential_opposite(o1["C"], o1["D"])
    m_exist_reverse1 = existential_opposite(m1["A"], m1["B"])
    m_exist_face1 = existential_opposite(m1["C"], m1["D"])
    cover_reverse = reverse_report(cover["A"], cover["B"])
    cover_face = face_report(cover["C"], cover["D"])
    unique_sim_b1 = simultaneous(unique_letter(m1["B"]), unique_letter(o1["B"]))
    unique_sim_b2 = simultaneous(unique_letter(m2["B"]), unique_letter(o2["B"]))
    print(f"reverse leftover_t={reverse0} leftover_tplus1={reverse_mid} tau1={reverse1} tau2={reverse2}")
    print(f"face leftover_t={face0} leftover_tplus1={face_mid} tau1={face1} tau2={face2}")
    print(
        f"composition={composition} bit_composition={bit_composition} "
        f"leftover_tplus1_tplus2={leftover_tplus1_tplus2}"
    )
    print(
        "per_element: each signed lock among {±e_1,±e_2,±e_3} in M or in O "
        "at a probe's t+2 and at t+3"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four M and O reports at two cuts plus sim/reverse/face/composition"
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
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[E3] == 0
        and ticks[PAIR2] == 0
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
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
        and TWO_AXIS_SAME_LOCK_SEEDS
        == ((ORIGIN, E1), (E2, E1), (E3, E2), (PAIR2, E2)),
    )
    checks.check(
        "neither-pair-is-opposite",
        seed_map[ORIGIN] == seed_map[E2] == E1
        and seed_map[E3] == seed_map[PAIR2] == E2
        and add(seed_map[ORIGIN], seed_map[E2]) != ZERO
        and add(seed_map[E3], seed_map[PAIR2]) != ZERO
        and TWO_AXIS_SAME_LOCK_SEEDS != TWO_AXIS_OPPOSITE_SEEDS,
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
        and TWO_AXIS_SAME_LOCK_SEEDS != ONE_AXIS_SAME_LOCK_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != TWO_AXIS_OPPOSITE_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != NSOPP_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_AXIS_SAME_LOCK_SEEDS != X_AXIS_SAME_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4,
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
        "theorem1-M-at-tau1",
        m1["A"] == frozenset({E1})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau1",
        o1["A"] == frozenset({E2, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau2",
        m2["A"] == frozenset({E1})
        and m2["B"] == frozenset({E1})
        and m2["C"] == frozenset({E2})
        and m2["D"] == frozenset({NEG_E3})
        and all(m2[name] == m1[name] for name in ("A", "B", "C", "D")),
        str({name: lockset_display(m2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau2",
        o2["A"] == frozenset({E2, NEG_E3})
        and o2["B"] == frozenset({E2, E3, NEG_E3})
        and o2["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o2["D"] == frozenset({E1})
        and all(o2[name] == o1[name] for name in ("A", "B", "C", "D")),
        str({name: lockset_display(o2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-sim-hold-at-tau1-and-tau2",
        all(sim1[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(sim2[name] == "hold" for name in ("A", "B", "C", "D"))
        and all(inter1[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(inter2[name] == frozenset() for name in ("A", "B", "C", "D")),
        str({name: (sim1[name], sim2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-new-records-meet-6nn-at-tplus2",
        new_meet1["A"] == ((1, 1, 0), (-1, 1, 0))
        and new_meet1["B"] == ()
        and new_meet1["C"] == ()
        and new_meet1["D"] == ()
        and incoming_set((1, 1, 0), tau1["A"], ticks, locks, seed_map)
        == frozenset({NEG_E3})
        and incoming_set((-1, 1, 0), tau1["A"], ticks, locks, seed_map)
        == frozenset({NEG_E3})
        and E1 not in o1["A"]
        and NEG_E1 not in o1["A"]
        and o1["A"] == o_mid["A"],
        str(new_meet1),
    )
    checks.check(
        "theorem1-new-6nn-at-tplus3-at-B-only",
        new_meet2["A"] == ()
        and new_meet2["B"] == ((2, 1, 1),)
        and new_meet2["C"] == ()
        and new_meet2["D"] == ()
        and incoming_set((2, 1, 1), tau2["B"], ticks, locks, seed_map)
        == frozenset({NEG_E2, E3, NEG_E3})
        and E1 not in o2["B"]
        and o2["B"] == o1["B"],
        str(new_meet2),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_sim_b1 == UNDEFINED
        and unique_sim_b2 == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and unique_letter(o2["A"]) == UNDEFINED,
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and E2 in seed_map
        and seed_map[E2] == E1
        and m1["A"] == frozenset({E1}),
    )
    checks.check(
        "do-not-score-tau-equals-t",
        all(o0[name] == frozenset() for name in ("A", "B", "C", "D"))
        and all(sim0[name] == "fail" for name in ("A", "B", "C", "D"))
        and reverse0 == "fail"
        and face0 == "fail"
        and leftover_empty_at_t == "fail"
        and leftover_m_from_t == "HOLD"
        and leftover_o_from_t == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and composition == "HOLD"
        and leftover_tplus1_tplus2 == "HOLD"
        and reverse_mid == "hold"
        and face_mid == "hold"
        and "Do not score τ=t" in note,
    )
    checks.check(
        "theorem2-reverse-tau1-hold-tau2-hold",
        reverse1 == "hold"
        and reverse2 == "hold"
        and sim1["A"] == "hold"
        and sim1["B"] == "hold"
        and sim2["A"] == "hold"
        and sim2["B"] == "hold"
        and reverse1 != UNDEFINED
        and reverse2 != UNDEFINED,
    )
    checks.check(
        "theorem2-face-tau1-hold-tau2-hold",
        face1 == "hold"
        and face2 == "hold"
        and sim1["C"] == "hold"
        and sim1["D"] == "hold"
        and sim2["C"] == "hold"
        and sim2["D"] == "hold"
        and face1 != UNDEFINED
        and face2 != UNDEFINED,
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "HOLD"
        and bit_composition == "HOLD"
        and leftover_m_only == "HOLD"
        and leftover_o_only == "HOLD"
        and leftover_tplus1_tplus2 == "HOLD"
        and reverse2 == reverse1
        and face2 == face1
        and all(m2[name] == m1[name] for name in ("A", "B", "C", "D"))
        and all(o2[name] == o1[name] for name in ("A", "B", "C", "D"))
        and all(m1[name] == m_mid[name] for name in ("A", "B", "C", "D"))
        and all(o1[name] == o_mid[name] for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "not-leftover-nm2simt2sly-tplus1-tplus2",
        leftover_tplus1_tplus2 == "HOLD"
        and reverse_mid == "hold"
        and face_mid == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and composition == "HOLD"
        and tau1["A"] == ticks[PROBES["A"]] + 2
        and tau2["A"] == ticks[PROBES["A"]] + 3
        and tau_mid["A"] == ticks[PROBES["A"]] + 1,
    )
    checks.check(
        "mutation-empty-at-t-composition-fail",
        reverse0 == "fail"
        and face0 == "fail"
        and leftover_empty_at_t == "fail"
        and leftover_m_from_t == "HOLD"
        and leftover_o_from_t == "fail"
        and leftover_tplus1_tplus2 == "HOLD"
        and composition == "HOLD"
        and o0["A"] == frozenset()
        and o0["A"] != o_mid["A"]
        and o_mid["A"] == o1["A"],
    )
    checks.check(
        "not-exist-opposite-of-M",
        m_exist_reverse1 == "fail"
        and m_exist_face1 == "fail"
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "not-exist-opposite-of-O-alone",
        o_exist_reverse1 == "hold"
        and o_exist_face1 == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and reverse_report(sim1["A"], sim1["B"]) == reverse1,
    )
    checks.check(
        "not-axis-cover-leftover",
        cover["A"] == "hold"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "fail"
        and cover_reverse == "hold"
        and cover_face == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and cover_face != face1,
    )
    checks.check(
        "not-m-two-tick-alone",
        leftover_m_only == "HOLD"
        and leftover_m_from_t == "HOLD"
        and leftover_o_from_t == "fail"
        and leftover_tplus1_tplus2 == "HOLD"
        and composition == "HOLD"
        and leftover_empty_at_t == "fail"
        and m_exist_reverse1 == "fail",
    )
    checks.check(
        "not-o-only-freeze-without-M",
        leftover_o_only == "HOLD"
        and leftover_o_from_t == "fail"
        and leftover_m_from_t == "HOLD"
        and leftover_tplus1_tplus2 == "HOLD"
        and composition == "HOLD"
        and all(m1[name] != o1[name] for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and E1 in m1["A"]
        and E1 not in o1["A"]
        and o1["A"] != m1["A"]
        and o2["A"] != m1["A"]
        and inter1["A"] == frozenset(),
    )
    one_o1 = {
        name: outgoing_set(
            PROBES[name],
            one_ticks[PROBES[name]] + 1,
            one_ticks,
            one_locks,
            one_seeds,
        )
        for name in ("A", "B", "C", "D")
    }
    checks.check(
        "not-one-axis-same-lock-leftover",
        TWO_AXIS_SAME_LOCK_SEEDS != ONE_AXIS_SAME_LOCK_SEEDS
        and ticks[PROBES["B"]] == 1
        and one_ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 2
        and one_ticks[PROBES["D"]] == 3
        and o1["A"] == frozenset({E2, NEG_E3})
        and one_o1["A"] == frozenset({E2, E3, NEG_E3})
        and E3 not in o1["A"],
    )
    opp_o1 = {
        name: outgoing_set(
            PROBES[name],
            opp_ticks[PROBES[name]] + 1,
            opp_ticks,
            opp_locks,
            opp_seeds,
        )
        for name in ("A", "B", "C", "D")
    }
    opp_m1 = {
        name: incoming_set(
            PROBES[name],
            opp_ticks[PROBES[name]] + 1,
            opp_ticks,
            opp_locks,
            opp_seeds,
        )
        for name in ("A", "B", "C", "D")
    }
    checks.check(
        "not-two-axis-opposite",
        TWO_AXIS_SAME_LOCK_SEEDS != TWO_AXIS_OPPOSITE_SEEDS
        and opp_m1["A"] == frozenset({NEG_E1})
        and m1["A"] == frozenset({E1})
        and isinstance(opp_o1["D"], frozenset)
        and NEG_E1 in opp_o1["D"]
        and isinstance(o1["D"], frozenset)
        and NEG_E1 not in o1["D"],
    )
    ysym_o1 = {
        name: outgoing_set(
            PROBES[name],
            ysym_ticks[PROBES[name]] + 1,
            ysym_ticks,
            ysym_locks,
            ysym_seeds,
        )
        for name in ("A", "B", "C", "D")
    }
    checks.check(
        "not-y-symmetric-three-site-seed",
        TWO_AXIS_SAME_LOCK_SEEDS != Y_SYMMETRIC_SEEDS
        and ticks[PROBES["B"]] == 1
        and ysym_ticks[PROBES["B"]] == 2
        and ysym_o1["A"] != o1["A"]
        and E3 in ysym_o1["A"]
        and E3 not in o1["A"],
    )
    checks.check(
        "mutation-unique-letter-undefined",
        unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(o1["C"]) == UNDEFINED
        and unique_sim_b1 == UNDEFINED
        and unique_sim_b2 == UNDEFINED
        and sim1["B"] == "hold"
        and reverse1 == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(o1["A"], frozenset)
        and isinstance(o1["B"], frozenset)
        and sum_of_set(o1["A"]) == add(E2, NEG_E3)
        and sum_of_set(o1["B"]) == E2
        and reverse1 == "hold"
        and add(sum_of_set(o1["A"]), sum_of_set(o1["B"])) != ZERO,
    )
    x_o1 = {
        name: outgoing_set(
            X_PROBES[name],
            ticks[X_PROBES[name]] + 1,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if X_PROBES[name] in ticks
    }
    checks.check(
        "not-x-probes",
        probe_sites != x_probe_sites
        and x_o1["A"] != o1["A"]
        and reverse1 == "hold",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-O-sim-both-cuts",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=2" in note
        and "M(A, τ1) = {+e_1}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_2}" in note
        and "M(D, τ1) = {−e_3}" in note
        and "O(A, τ1) = {+e_2, −e_3}" in note
        and "O(B, τ1) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ1) = {+e_1}" in note
        and "M(A, τ2) = {+e_1}" in note
        and "M(B, τ2) = {+e_1}" in note
        and "M(C, τ2) = {+e_2}" in note
        and "M(D, τ2) = {−e_3}" in note
        and "O(A, τ2) = {+e_2, −e_3}" in note
        and "O(B, τ2) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}" in note
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
        "new 6-NN of A at t(A)+2: (1, 1, 0), (-1, 1, 0)" in note
        and "new 6-NN of B at t(B)+2: {}" in note
        and "new 6-NN of C at t(C)+2: {}" in note
        and "new 6-NN of D at t(D)+2: {}" in note
        and "new 6-NN of A at t(A)+3: {}" in note
        and "new 6-NN of B at t(B)+3: (2, 1, 1)" in note
        and "new 6-NN of C at t(C)+3: {}" in note
        and "new 6-NN of D at t(D)+3: {}" in note,
    )
    checks.check(
        "note-reports-hold-hold-composition-hold",
        "Reverse at τ1: hold" in note
        and "Reverse at τ2: hold" in note
        and "Face at τ1: hold" in note
        and "Face at τ2: hold" in note
        and "Composition: HOLD" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-m-two-tick-or-o-only",
        "not leftover of `M` two-tick" in normalized_note
        and "not leftover of nm2ot3sly O freeze" in normalized_note
        and "not leftover of nm2simsly simultaneous at t+1" in normalized_note
        and "not leftover of nm2simt2sly simultaneous freeze t+1 versus t+2" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-not-empty-at-t",
        "Do not score τ=t" in note
        and "Composition: HOLD" in note
        and "empty `O` at formation tick `t`" in normalized_note,
    )
    checks.check(
        "note-not-axis-cover-or-exist-opposite",
        "not leftover of axis-cover" in normalized_note
        and "cover face fail" in normalized_note
        and "M exist-opposite reverse fail" in normalized_note
        and "not leftover of nm2slo timed-O" in normalized_note,
    )
    checks.check(
        "note-not-one-axis-or-two-axis-opposite",
        "not leftover of the one-axis same-lock seed" in normalized_note
        and "not leftover of the two-axis opposite seed" in normalized_note
        and "O(A)` includes `+e_3`" in note
        and "`O(D)` includes `−e_1`" in note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-mixed-7188-fail-fail",
        "not leftover of mixed #7188 fail/fail" in normalized_note
        and "Reverse at τ1: hold" in note
        and "Face at τ1: hold" in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "Occupancy `n` is not used" in note
        and "does not use occupancy" in normalized_note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ1(q)=t(q)+2" in note.replace(" ", "")
        and "τ2(q)=t(q)+3" in note.replace(" ", ""),
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
        '    "docs/TWO_AXIS_SAME_LOCK_YPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "simultaneous" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "composition_from_mo" in defined_fns
        and "composition_report" in defined_fns
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
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
