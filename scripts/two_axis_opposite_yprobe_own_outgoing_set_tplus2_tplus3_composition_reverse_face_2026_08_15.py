#!/usr/bin/env python3
"""O freeze t+2 versus t+3 reverse/face composition on two-axis y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process and y-probes as nm2axo.
The second pair is a new seed, not a formed child. A 6-NN step is allowed
iff it is perpendicular to the parent lock axis. Newly formed sites lock the
incoming step. Seeds keep their seed letters as a singleton. t(q) is the
formation tick. tau1 = t+2. tau2 = t+3. No global T. Do not score tau=t.
Do not score tau=t+1 versus t+2 leftover of nm2ot3y. M(r, tau) is the set
of earliest incoming nearest-neighbor steps at r using only records with
tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is the outgoing dual
of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is formed and e is in
M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is empty, not
UNDEFINED. Reverse at a cut HOLDs iff some a in O(A, tau) and some b in
O(B, tau) have a+b=(0,0,0). Face likewise on C, D. Empty or UNDEFINED on
either side is UNDEFINED; nonempty with no opposite pair fails.
Composition holds iff O(tau1)=O(tau2) at A, B, C, and D. Uniqueness is not
required. Occupancy of sites is not used. Named-sign lettering is not used.
No unique P_+. No 6-NN star. No Cl(3,0). No Dijkstra. No Gram. No larger
host. Not leftover of nm2ot3y O at t+1 versus t+2. Not leftover of nmot2opp
O at t versus t+1. Not leftover of nmt2opp M two-tick. Not leftover of
nmoutopp eventual-O. Not leftover of axis-cover. Not leftover of z-probe O
exist-opposite.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_YPROBE_OWN_OUTGOING_SET_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_YPROBE_OWN_OUTGOING_SET_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
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
    "ndot",
)
CLAIM_SCOPE = (
    "O at t+2 versus t+3 on the four y-probes of the two-axis "
    "opposite seed, reverse/face at each cut, and composition, "
    "are reported. Displayed, not adopted."
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


def eventual_outgoing_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Outgoing:
    """nmoutopp leftover: eventual neighbor locks, no t+2 versus t+3 cut."""
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


def unique_letter(value: Incoming) -> Incoming:
    """Unique-L leftover: UNDEFINED when mixed. Not this letter."""
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right.

    UNDEFINED or empty on either side is UNDEFINED. Nonempty with no opposite
    pair fails. Mixed remains a set. Does not sum. Does not require a singleton.
    """
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        return UNDEFINED
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: Incoming, set_b: Incoming) -> str:
    """Reverse iff some a in O(A, tau) and some b in O(B, tau) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Face iff some c in O(C, tau) and some d in O(D, tau) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def composition_report(
    o1_a: Outgoing,
    o2_a: Outgoing,
    o1_b: Outgoing,
    o2_b: Outgoing,
    o1_c: Outgoing,
    o2_c: Outgoing,
    o1_d: Outgoing,
    o2_d: Outgoing,
) -> str:
    """Hold iff O(tau1)=O(tau2) at A, B, C, and D. UNDEFINED if any side is."""
    sides = (o1_a, o2_a, o1_b, o2_b, o1_c, o2_c, o1_d, o2_d)
    if any(side == UNDEFINED for side in sides):
        return UNDEFINED
    if not all(isinstance(side, frozenset) for side in sides):
        return UNDEFINED
    if o1_a == o2_a and o1_b == o2_b and o1_c == o2_c and o1_d == o2_d:
        return "hold"
    return "fail"


def leftover_bit_composition(rev1: str, rev2: str, face1: str, face2: str) -> str:
    """Leftover: score composition on reverse/face bits, not on O-set equality."""
    if rev1 != rev2 or face1 != face2:
        return "fail"
    return "hold"


def axis_set(value: Incoming) -> frozenset[Point] | str:
    """Unsigned axes of a lock set. Contrast only; not this letter."""
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    occupied: set[Point] = set()
    for lock in value:
        occupied.add(axis_of_letter(lock))
    return frozenset(occupied)


def axis_cover(incoming: Incoming, outgoing: Outgoing) -> str:
    """Axis-cover leftover contrast. Not this reverse."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets")
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("two-axis opposite y-probe O freeze t+2 versus t+3 reverse/face composition")
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
    x_probe_sites = tuple(X_PROBES[name] for name in ("A", "B", "C", "D"))
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != z_probe_sites
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
    out_a = frozenset({E2, NEG_E3})
    out_b = frozenset({E2, E3, NEG_E3})
    out_c = frozenset({E1, NEG_E1, E3, NEG_E3})
    out_d = frozenset({E1, NEG_E1})
    set_a = frozenset({NEG_E1})
    set_b = frozenset({E1})
    set_c = frozenset({E2})
    set_d = frozenset({NEG_E3})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset({E1}), UNDEFINED) == UNDEFINED
        and existential_opposite(frozenset(), frozenset({E3})) == UNDEFINED
        and existential_opposite(frozenset({E3}), frozenset()) == UNDEFINED
        and existential_opposite(frozenset(), frozenset()) == UNDEFINED
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(set_a, set_b) == "hold"
        and existential_opposite(set_c, set_d) == "fail"
        and existential_opposite(out_a, out_b) == "hold"
        and existential_opposite(out_c, out_d) == "hold"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold",
    )
    grown_a = frozenset({E2, NEG_E3, E1})
    checks.check(
        "composition-identity",
        composition_report(out_a, out_a, out_b, out_b, out_c, out_c, out_d, out_d)
        == "hold"
        and composition_report(out_a, grown_a, out_b, out_b, out_c, out_c, out_d, out_d)
        == "fail"
        and composition_report(
            UNDEFINED, out_a, out_b, out_b, out_c, out_c, out_d, out_d
        )
        == UNDEFINED
        and composition_report(
            frozenset(), out_a, out_b, out_b, out_c, out_c, out_d, out_d
        )
        == "fail"
        and leftover_bit_composition("hold", "hold", "hold", "hold") == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail",
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
    o_eventual: dict[str, Outgoing] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
    new_meet2: dict[str, tuple[Point, ...]] = {}
    one_o1: dict[str, Outgoing] = {}
    one_o2: dict[str, Outgoing] = {}
    cover1: dict[str, str] = {}
    cover2: dict[str, str] = {}
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
        o_eventual[name] = eventual_outgoing_set(site, ticks, locks)
        new_meet1[name] = new_records_meeting_six_nn(site, ticks, 2)
        new_meet2[name] = new_records_meeting_six_nn(site, ticks, 3)
        one_o1[name] = outgoing_set(
            site, one_ticks[site] + 2, one_ticks, one_locks, one_seeds
        )
        one_o2[name] = outgoing_set(
            site, one_ticks[site] + 3, one_ticks, one_locks, one_seeds
        )
        cover1[name] = axis_cover(m1[name], o1[name])
        cover2[name] = axis_cover(m2[name], o2[name])
        print(
            f"{name} t={ticks[site]} "
            f"O(tau1)={lockset_display(o1[name])} "
            f"O(tau2)={lockset_display(o2[name])}"
        )

    leftover_reverse0 = reverse_report(o0["A"], o0["B"])
    leftover_face0 = face_report(o0["C"], o0["D"])
    leftover_reverse_prev = reverse_report(o_prev["A"], o_prev["B"])
    leftover_face_prev = face_report(o_prev["C"], o_prev["D"])
    reverse1 = reverse_report(o1["A"], o1["B"])
    reverse2 = reverse_report(o2["A"], o2["B"])
    face1 = face_report(o1["C"], o1["D"])
    face2 = face_report(o2["C"], o2["D"])
    composition = composition_report(
        o1["A"], o2["A"], o1["B"], o2["B"], o1["C"], o2["C"], o1["D"], o2["D"]
    )
    leftover_nmot2opp_composition = composition_report(
        o0["A"], o_prev["A"], o0["B"], o_prev["B"], o0["C"], o_prev["C"], o0["D"], o_prev["D"]
    )
    leftover_nm2ot3y_composition = composition_report(
        o_prev["A"], o1["A"], o_prev["B"], o1["B"], o_prev["C"], o1["C"], o_prev["D"], o1["D"]
    )
    leftover_bits = leftover_bit_composition(reverse1, reverse2, face1, face2)
    reverse_m1 = reverse_report(m1["A"], m1["B"])
    reverse_m2 = reverse_report(m2["A"], m2["B"])
    face_m1 = face_report(m1["C"], m1["D"])
    face_m2 = face_report(m2["C"], m2["D"])
    m_composition = composition_report(
        m1["A"], m2["A"], m1["B"], m2["B"], m1["C"], m2["C"], m1["D"], m2["D"]
    )
    cover_reverse1 = pair_cover(cover1["A"], cover1["B"])
    cover_face1 = pair_cover(cover1["C"], cover1["D"])
    cover_reverse2 = pair_cover(cover2["A"], cover2["B"])
    cover_face2 = pair_cover(cover2["C"], cover2["D"])
    unique_out_reverse1 = reverse_report(unique_letter(o1["A"]), unique_letter(o1["B"]))
    unique_out_face1 = face_report(unique_letter(o1["C"]), unique_letter(o1["D"]))
    unique_out_reverse2 = reverse_report(unique_letter(o2["A"]), unique_letter(o2["B"]))
    unique_out_face2 = face_report(unique_letter(o2["C"]), unique_letter(o2["D"]))
    one_reverse1 = reverse_report(one_o1["A"], one_o1["B"])
    one_face1 = face_report(one_o1["C"], one_o1["D"])
    one_reverse2 = reverse_report(one_o2["A"], one_o2["B"])
    one_face2 = face_report(one_o2["C"], one_o2["D"])
    one_composition = composition_report(
        one_o1["A"],
        one_o2["A"],
        one_o1["B"],
        one_o2["B"],
        one_o1["C"],
        one_o2["C"],
        one_o1["D"],
        one_o2["D"],
    )
    leftover_neighbor_reverse = reverse_report(
        neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]]),
        neighbor_lock_set(PROBES["B"], ticks, locks, ticks[PROBES["B"]]),
    )
    leftover_neighbor_face = face_report(
        neighbor_lock_set(PROBES["C"], ticks, locks, ticks[PROBES["C"]]),
        neighbor_lock_set(PROBES["D"], ticks, locks, ticks[PROBES["D"]]),
    )
    eventual_reverse = reverse_report(o_eventual["A"], o_eventual["B"])
    eventual_face = face_report(o_eventual["C"], o_eventual["D"])
    print(f"reverse tau1={reverse1} tau2={reverse2}")
    print(f"face tau1={face1} tau2={face2}")
    print(f"composition={composition}")
    print(
        "per_element: each lock vector in the probe's own outgoing set O(q, tau)"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four outgoing sets at t+2 and t+3 plus reverse/face/composition"
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
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(Q_SEED, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and m1["A"] == frozenset({NEG_E1}),
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
        "theorem1-O-at-tau1",
        o1["A"] == out_a
        and o1["B"] == out_b
        and o1["C"] == out_c
        and o1["D"] == out_d
        and isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and isinstance(o1["B"], frozenset)
        and len(o1["B"]) == 3
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 2,
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau2",
        o2["A"] == out_a
        and o2["B"] == out_b
        and o2["C"] == out_c
        and o2["D"] == out_d
        and isinstance(o2["A"], frozenset)
        and len(o2["A"]) == 2,
        str({name: lockset_display(o2[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-tau2-equals-tau1-freeze",
        all(
            isinstance(o1[name], frozenset)
            and isinstance(o2[name], frozenset)
            and o2[name] == o1[name]
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "do-not-score-tau-t",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E1})
        and leftover_reverse0 == UNDEFINED
        and leftover_face0 == UNDEFINED
        and leftover_nmot2opp_composition == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and o0["A"] != o1["A"]
        and o0["D"] != o1["D"],
    )
    checks.check(
        "not-leftover-nm2ot3y-tplus1-versus-tplus2",
        leftover_nm2ot3y_composition == "hold"
        and leftover_reverse_prev == "hold"
        and leftover_face_prev == "hold"
        and o_prev["A"] == o1["A"]
        and o_prev["B"] == o1["B"]
        and o_prev["C"] == o1["C"]
        and o_prev["D"] == o1["D"]
        and o1["A"] == o2["A"]
        and tau1["A"] == ticks[PROBES["A"]] + 2
        and tau2["A"] == ticks[PROBES["A"]] + 3
        and tau_prev["A"] == ticks[PROBES["A"]] + 1,
    )
    checks.check(
        "theorem1-M-frozen-across-tau1-tau2",
        m1["A"] == set_a
        and m1["B"] == set_b
        and m1["C"] == set_c
        and m1["D"] == set_d
        and m2["A"] == m1["A"]
        and m2["B"] == m1["B"]
        and m2["C"] == m1["C"]
        and m2["D"] == m1["D"]
        and m1["A"] == m0["A"],
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet1["A"] == ((1, 1, 0), (-1, 1, 0))
        and new_meet1["B"] == ()
        and new_meet1["C"] == ()
        and new_meet1["D"] == ()
        and new_meet2["A"] == ()
        and new_meet2["B"] == ((2, 1, 1),)
        and new_meet2["C"] == ()
        and new_meet2["D"] == (),
        str({name: (new_meet1[name], new_meet2[name]) for name in ("A", "B", "C", "D")}),
    )
    child_of_a_tplus2 = (1, 1, 0)
    child_of_a_tplus2_west = (-1, 1, 0)
    checks.check(
        "theorem1-new-tplus2-neighbor-does-not-enter-O",
        child_of_a_tplus2 in new_meet1["A"]
        and child_of_a_tplus2_west in new_meet1["A"]
        and ticks[child_of_a_tplus2] == ticks[PROBES["A"]] + 2
        and ticks[child_of_a_tplus2_west] == ticks[PROBES["A"]] + 2
        and incoming_set(child_of_a_tplus2, tau1["A"], ticks, locks, seed_map)
        == frozenset({NEG_E3})
        and incoming_set(child_of_a_tplus2_west, tau1["A"], ticks, locks, seed_map)
        == frozenset({NEG_E3})
        and E1 not in o1["A"]
        and NEG_E1 not in o1["A"]
        and o2["A"] == o1["A"],
    )
    child_of_b_tplus3 = (2, 1, 1)
    checks.check(
        "theorem1-new-tplus3-neighbor-does-not-enter-O",
        child_of_b_tplus3 in new_meet2["B"]
        and ticks[child_of_b_tplus3] == ticks[PROBES["B"]] + 3
        and incoming_set(child_of_b_tplus3, tau2["B"], ticks, locks, seed_map)
        == frozenset({NEG_E2, E3, NEG_E3})
        and E1 not in o2["B"]
        and E1 not in o1["B"]
        and o2["B"] == o1["B"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and unique_letter(o1["A"]) == UNDEFINED
        and isinstance(o2["A"], frozenset)
        and len(o2["A"]) == 2
        and unique_letter(o2["A"]) == UNDEFINED
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 2
        and unique_letter(o1["D"]) == UNDEFINED,
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and m1["A"] == frozenset({NEG_E1})
        and Z_PROBES["A"] != PROBES["A"]
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-compare-7167-1-axis",
        one_ticks[PROBES["A"]] == 0
        and one_ticks[PROBES["B"]] == 2
        and one_ticks[PROBES["C"]] == 1
        and one_ticks[PROBES["D"]] == 3
        and one_o1["A"] == frozenset({E2, E3, NEG_E3})
        and one_o2["A"] == one_o1["A"]
        and one_composition == "hold"
        and one_reverse1 == "hold"
        and one_face1 == "hold"
        and one_reverse2 == "hold"
        and one_face2 == "hold"
        and o1["A"] != one_o1["A"]
        and E3 not in o1["A"]
        and E3 in one_o1["A"],
    )
    checks.check(
        "theorem2-reverse-tau1-and-tau2-hold",
        reverse1 == "hold"
        and reverse2 == "hold"
        and o1["A"] == out_a
        and o1["B"] == out_b
        and add(NEG_E3, E3) == ZERO
        and NEG_E3 in o1["A"]
        and E3 in o1["B"]
        and reverse1 != UNDEFINED
        and reverse2 != "fail",
        f"{reverse1}/{reverse2}",
    )
    checks.check(
        "theorem2-face-tau1-and-tau2-hold",
        face1 == "hold"
        and face2 == "hold"
        and o1["C"] == out_c
        and o1["D"] == out_d
        and E1 in o1["C"]
        and NEG_E1 in o1["D"]
        and face1 != "fail"
        and face1 != UNDEFINED,
        f"{face1}/{face2}",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and o2["A"] == o1["A"]
        and o2["B"] == o1["B"]
        and o2["C"] == o1["C"]
        and o2["D"] == o1["D"]
        and reverse2 == reverse1
        and face2 == face1,
        composition,
    )
    checks.check(
        "discriminator-O-face-hold-vs-cover-fail",
        reverse1 == "hold"
        and face1 == "hold"
        and cover1["A"] == "hold"
        and cover1["B"] == "hold"
        and cover1["C"] == "hold"
        and cover1["D"] == "fail"
        and cover_reverse1 == "hold"
        and cover_face1 == "fail"
        and cover_reverse2 == "hold"
        and cover_face2 == "fail"
        and cover_face1 != face1,
    )
    checks.check(
        "not-M-exist-opposite-face",
        reverse_m1 == "hold"
        and reverse_m2 == "hold"
        and face_m1 == "fail"
        and face_m2 == "fail"
        and m_composition == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and face1 != face_m1
        and o1["A"] != m1["A"],
    )
    checks.check(
        "not-unique-L-leftover",
        unique_out_reverse1 == UNDEFINED
        and unique_out_face1 == UNDEFINED
        and unique_out_reverse2 == UNDEFINED
        and unique_out_face2 == UNDEFINED
        and reverse1 == "hold"
        and face1 == "hold"
        and reverse1 != unique_out_reverse1,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E1 in m1["A"]
        and NEG_E1 not in o1["A"]
        and o1["A"] != m1["A"]
        and o1["B"] != m1["B"]
        and o1["C"] != m1["C"]
        and o1["D"] != m1["D"]
        and m1["A"].isdisjoint(o1["A"])
        and m2["A"].isdisjoint(o2["A"]),
    )
    y_o1 = {
        name: outgoing_set(
            Z_PROBES[name],
            ticks[Z_PROBES[name]] + 2,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if Z_PROBES[name] in ticks
    }
    y_o2 = {
        name: outgoing_set(
            Z_PROBES[name],
            ticks[Z_PROBES[name]] + 3,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if Z_PROBES[name] in ticks
    }
    x_o1 = {
        name: outgoing_set(
            X_PROBES[name],
            ticks[X_PROBES[name]] + 2,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if X_PROBES[name] in ticks
    }
    perp_o1 = {
        name: outgoing_set(
            PROBES[name],
            perp_ticks[PROBES[name]] + 2,
            perp_ticks,
            perp_locks,
            perp_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in perp_ticks
    }
    zsym_o1 = {
        name: outgoing_set(
            PROBES[name],
            zsym_ticks[PROBES[name]] + 2,
            zsym_ticks,
            zsym_locks,
            zsym_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in zsym_ticks
    }
    y_reverse1 = reverse_report(y_o1["A"], y_o1["B"])
    y_face1 = face_report(y_o1["C"], y_o1["D"])
    y_reverse2 = reverse_report(y_o2["A"], y_o2["B"])
    y_face2 = face_report(y_o2["C"], y_o2["D"])
    x_reverse1 = reverse_report(x_o1["A"], x_o1["B"])
    x_face1 = face_report(x_o1["C"], x_o1["D"])
    zsym_reverse = reverse_report(zsym_o1["A"], zsym_o1["B"])
    zsym_face = face_report(zsym_o1["C"], zsym_o1["D"])
    ysym_ticks_count0 = sum(time == 0 for time in ysym_ticks.values())
    checks.check(
        "not-z-probes-or-x-probes-or-z-symmetric-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != z_probe_sites
        and probe_sites != x_probe_sites
        and y_o1["A"] != o1["A"]
        and x_o1["A"] != o1["A"]
        and zsym_o1["A"] != o1["A"]
        and perp_o1["A"] != o1["A"]
        and y_reverse1 == "hold"
        and y_face1 == "fail"
        and y_reverse2 == "hold"
        and y_face2 == "fail"
        and x_reverse1 == "fail"
        and x_face1 == "fail"
        and y_face1 != face1
        and zsym_reverse == "fail"
        and zsym_reverse != reverse1
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "not-y-symmetric-three-site-seed",
        TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and ysym_ticks_count0 == 3,
    )
    checks.check(
        "not-nsopp-leftover-child",
        TWO_AXIS_SEEDS != ONE_AXIS_SEEDS
        and seed_map[E3] == E2
        and seed_map[Q_SEED] == NEG_E2
        and ticks[E3] == 0
        and ticks[Q_SEED] == 0
        and one_ticks[E3] == 1
        and one_ticks[Q_SEED] == 1
        and sum(time == 0 for time in one_ticks.values()) == 2
        and sum(time == 0 for time in ticks.values()) == 4,
    )
    checks.check(
        "not-nnlock-named-sign",
        o1["A"] == frozenset({E2, NEG_E3})
        and named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E2) == "+"
        and o1["A"] != named_sign(E2)
        and m1["A"] != named_sign(NEG_E1),
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
        and len(o1["A"]) == 2
        and isinstance(o2["A"], frozenset)
        and len(o2["A"]) == 2
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
        and add(E2, NEG_E2) == ZERO
        and TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Y_SYMMETRIC_SEEDS,
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
        and existential_opposite(frozenset(), o1["B"]) == UNDEFINED,
    )
    checks.check(
        "mutation-nmot2opp-tau-t-undefined-composition-fail",
        leftover_reverse0 == UNDEFINED
        and leftover_face0 == UNDEFINED
        and leftover_nmot2opp_composition == "fail"
        and composition == "hold",
    )
    checks.check(
        "mutation-nm2ot3y-tplus1-tplus2-is-prior-freeze-not-this-cut",
        leftover_nm2ot3y_composition == "hold"
        and leftover_reverse_prev == "hold"
        and leftover_face_prev == "hold"
        and composition == "hold"
        and tau1["B"] == ticks[PROBES["B"]] + 2
        and tau2["B"] == ticks[PROBES["B"]] + 3,
    )
    checks.check(
        "mutation-nmt2opp-M-two-tick-hold-fail",
        reverse_m1 == "hold"
        and reverse_m2 == "hold"
        and face_m1 == "fail"
        and face_m2 == "fail"
        and m_composition == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and face1 != face_m1,
    )
    checks.check(
        "mutation-nmoutopp-eventual-O",
        o_eventual["A"] == o1["A"]
        and o_eventual["B"] == o1["B"]
        and o_eventual["C"] == o1["C"]
        and o_eventual["D"] == o1["D"]
        and o_eventual["A"] == o2["A"]
        and eventual_reverse == "hold"
        and eventual_face == "hold"
        and leftover_reverse0 == UNDEFINED,
    )
    checks.check(
        "mutation-bit-composition-leftover-is-not-O-sets",
        leftover_bits == "hold"
        and leftover_bit_composition("hold", "hold", "hold", "fail") == "fail"
        and composition_report(out_a, grown_a, out_b, out_b, out_c, out_c, out_d, out_d)
        == "fail"
        and composition == "hold",
    )
    checks.check(
        "mutation-unique-L-outgoing-would-be-undefined",
        unique_out_face1 == UNDEFINED
        and unique_out_reverse1 == UNDEFINED
        and unique_out_face2 == UNDEFINED
        and unique_out_reverse2 == UNDEFINED
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        sum_of_set(o1["A"]) == add(E2, NEG_E3)
        and sum_of_set(o1["B"]) == E2
        and sum_of_set(o1["C"]) == ZERO
        and sum_of_set(o1["D"]) == ZERO
        and o1["A"] != frozenset({add(E2, NEG_E3)})
        and o1["C"] != frozenset()
        and reverse1 == "hold"
        and isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 2
        and face1 == "hold",
    )
    checks.check(
        "mutation-neighbor-lock-leftover-differs",
        leftover_neighbor_reverse != reverse1
        or leftover_neighbor_face != face1
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        reverse_report(frozenset(), o1["B"]) == UNDEFINED
        and face_report(o1["C"], frozenset()) == UNDEFINED
        and reverse_report(UNDEFINED, o1["B"]) == UNDEFINED
        and face_report(o1["C"], UNDEFINED) == UNDEFINED,
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-outgoing-sets",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=2" in note
        and "O(A, τ1) = {+e_2, −e_3}" in note
        and "O(B, τ1) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ1) = {+e_1, −e_1}" in note
        and "O(A, τ2) = {+e_2, −e_3}" in note
        and "O(B, τ2) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ2) = {+e_1, −e_1}" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+2: (1, 1, 0), (-1, 1, 0)" in note
        and "new 6-NN of B at t(B)+2: none" in note
        and "new 6-NN of C at t(C)+2: none" in note
        and "new 6-NN of D at t(D)+2: none" in note
        and "new 6-NN of A at t(A)+3: none" in note
        and "new 6-NN of B at t(B)+3: (2, 1, 1)" in note
        and "new 6-NN of C at t(C)+3: none" in note
        and "new 6-NN of D at t(D)+3: none" in note,
    )
    checks.check(
        "note-reports-hold-hold-composition-hold",
        "Reverse at τ1: hold" in note
        and "Reverse at τ2: hold" in note
        and "Face at τ1: hold" in note
        and "Face at τ2: hold" in note
        and "Composition of O: hold" in note
        and "UNDEFINED" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-axis-cover-or-M-leftover",
        "not leftover of axis-cover" in normalized_note
        and "not leftover of M exist-opposite" in normalized_note
        and "O is not M" in note
        and "own outgoing set" in normalized_note,
    )
    checks.check(
        "note-not-nmot2opp-t-versus-tplus1",
        "not leftover of nmot2opp" in normalized_note
        and "not leftover of nm2ot3y" in normalized_note
        and "Do not score τ=t" in note,
    )
    checks.check(
        "note-not-m-two-tick-or-eventual-o",
        "not leftover of nmt2opp" in normalized_note
        and "not leftover of nmoutopp" in normalized_note
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
        and "O is not M" in note
        and "own outgoing set" in normalized_note,
    )
    checks.check(
        "note-not-nsopp-leftover-child",
        "not a formed child" in normalized_note
        and "second pair is a new seed" in normalized_note,
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
        '    "docs/TWO_AXIS_OPPOSITE_YPROBE_OWN_OUTGOING_SET_TPLUS2_TPLUS3_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "existential_opposite" in defined_fns
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
        "source-letter-from-own-outgoing-set-freeze",
        "outgoing_set" in defined_fns
        and "composition_report" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )
    _ = (
        x_face1,
        leftover_neighbor_face,
        leftover_neighbor_reverse,
        ysym_locks,
        ysym_seeds,
        tau0,
        leftover_bits,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
