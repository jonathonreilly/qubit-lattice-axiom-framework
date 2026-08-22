#!/usr/bin/env python3
"""Forall-orthogonal M vs O at t+1 reverse/face on four #7213 x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (1,0,0), (-1,0,0)} with locks +e_2, -e_2, and -e_2 (nmszopx #7213).
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. t(q) is formation tick. tau = t+1. M(q, tau) is the set of
earliest incoming NN steps at q using only records with tick <= tau.
Unformed at tau => UNDEFINED. O(q, tau) is the outgoing dual of M: the set
of e in {±e_1,±e_2,±e_3} such that q+e is formed in B_3(0) and e is in
M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is empty, not
UNDEFINED. Forall-perp HOLD iff every m in M(q, tau) and o in O(q, tau)
have integer dot m·o=0. Empty or UNDEFINED => UNDEFINED. Reverse HOLD iff
forall-perp at A and at B. Face HOLD iff forall-perp at C and at D.
Exist-perp and exist-opposite are leftover comparators. Uniqueness is not
required. Occupancy n is not used. Named-sign lettering is not used. No
unique P_+. No six-neighbor star as the letter. No Dijkstra. No Gram. No
larger host. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
Outgoing = frozenset[Point] | str
DotPairs = tuple[tuple[Point, Point, int], ...] | str
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
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
X_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
    (NEG_E1, NEG_E2),
)
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
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
NSTRI_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
    (E2, E1),
)
PERP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E1),
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
    "Forall-orthogonal M vs O at t+1 on the four #7213 x-probes, "
    "and reverse/face from that, are reported. Displayed, not adopted."
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


def set_display(locks: frozenset[Point]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def incoming_display(value: Incoming) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"incoming is not a lock set: {value!r}")
    return set_display(value)


def outgoing_display(value: Outgoing) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"outgoing is not a lock set: {value!r}")
    return set_display(value)


def pair_dots(left: Incoming, right: Outgoing) -> DotPairs:
    """Integer dots m·o for every pair from M against O. UNDEFINED if either is."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("sides must be lock sets or UNDEFINED")
    return tuple(
        (a, b, dot(a, b))
        for a in NN
        if a in left
        for b in NN
        if b in right
    )


def dots_display(pairs: DotPairs) -> str:
    if pairs == UNDEFINED:
        return UNDEFINED
    if not pairs:
        return "{}"
    parts = [
        f"{LOCK_NAME[a]}·{LOCK_NAME[b]}={value}" for a, b, value in pairs
    ]
    return "{" + ", ".join(parts) + "}"


def forall_orthogonal(left: Incoming, right: Outgoing) -> str:
    """HOLD iff every m in M and o in O have m·o=0. Empty or UNDEFINED => UNDEFINED."""
    pairs = pair_dots(left, right)
    if pairs == UNDEFINED:
        return UNDEFINED
    if not pairs:
        return UNDEFINED
    return "hold" if all(value == 0 for _a, _b, value in pairs) else "fail"


def exist_orthogonal(left: Incoming, right: Outgoing) -> str:
    """Leftover: HOLD iff some pair dots to 0. Empty or UNDEFINED => UNDEFINED."""
    pairs = pair_dots(left, right)
    if pairs == UNDEFINED:
        return UNDEFINED
    if not pairs:
        return UNDEFINED
    return "hold" if any(value == 0 for _a, _b, value in pairs) else "fail"


def both_hold(left_bit: str, right_bit: str) -> str:
    """Reverse/face from two forall-perp bits. UNDEFINED if either side is."""
    if left_bit == UNDEFINED or right_bit == UNDEFINED:
        return UNDEFINED
    return "hold" if left_bit == "hold" and right_bit == "hold" else "fail"


def reverse_report(
    m_a: Incoming, o_a: Outgoing, m_b: Incoming, o_b: Outgoing
) -> str:
    """Reverse HOLD iff forall-perp at A and at B."""
    return both_hold(forall_orthogonal(m_a, o_a), forall_orthogonal(m_b, o_b))


def face_report(
    m_c: Incoming, o_c: Outgoing, m_d: Incoming, o_d: Outgoing
) -> str:
    """Face HOLD iff forall-perp at C and at D."""
    return both_hold(forall_orthogonal(m_c, o_c), forall_orthogonal(m_d, o_d))


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
    seeds: tuple[tuple[Point, Point], ...] = X_SYMMETRIC_SEEDS,
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
    """M ∩ O leftover. UNDEFINED if either side is UNDEFINED. Empty stays empty."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("intersection sides must be lock sets or UNDEFINED")
    return left & right


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("forall-orthogonal M vs O at t+1 reverse/face on #7213 x-probes")
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
        and add(E1, E1) != ZERO
        and dot(E1, E2) == 0
        and dot(E1, E1) == 1
        and dot(E1, NEG_E1) == -1
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    set_m_a = frozenset({NEG_E2})
    set_m_b = frozenset({E2})
    set_m_c = frozenset({E1})
    set_m_d = frozenset({NEG_E1, E3, NEG_E3})
    set_o_a = frozenset({E1, E3, NEG_E3})
    set_o_b = frozenset({E1, E3, NEG_E3})
    set_o_c = frozenset({E2, NEG_E2, E3, NEG_E3})
    set_o_d = frozenset({E2, NEG_E2})
    checks.check(
        "forall-orthogonal-identity",
        forall_orthogonal(UNDEFINED, frozenset({E1})) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), UNDEFINED) == UNDEFINED
        and forall_orthogonal(frozenset(), frozenset({E3})) == UNDEFINED
        and forall_orthogonal(frozenset({E3}), frozenset()) == UNDEFINED
        and forall_orthogonal(frozenset(), frozenset()) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), frozenset({E1})) == "fail"
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and forall_orthogonal(frozenset({E1}), frozenset({E2})) == "hold"
        and forall_orthogonal(set_m_a, set_o_a) == "hold"
        and forall_orthogonal(set_m_b, set_o_b) == "hold"
        and forall_orthogonal(set_m_c, set_o_c) == "hold"
        and forall_orthogonal(set_m_d, set_o_d) == "hold"
        and forall_orthogonal(frozenset({E1, E2}), frozenset({E1, E3})) == "fail",
    )
    checks.check(
        "exist-orthogonal-is-weaker",
        exist_orthogonal(frozenset({E1, E2}), frozenset({E1, E3})) == "hold"
        and forall_orthogonal(frozenset({E1, E2}), frozenset({E1, E3})) == "fail"
        and exist_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and exist_orthogonal(set_m_a, set_o_a) == "hold",
    )
    checks.check(
        "empty-intersection-is-not-forall",
        intersection_set(frozenset({E1}), frozenset({NEG_E1})) == frozenset()
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and intersection_set(set_m_a, set_o_a) == frozenset()
        and forall_orthogonal(set_m_a, set_o_a) == "hold",
    )

    ticks, locks, seed_map = form()
    two_ticks, two_locks, two_seeds = form(TWO_SITE_SEEDS)
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    nstri_ticks, nstri_locks, nstri_seeds = form(NSTRI_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)

    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    bits1: dict[str, str] = {}
    exist1: dict[str, str] = {}
    inter1: dict[str, Incoming] = {}
    dots1: dict[str, DotPairs] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        bits1[name] = forall_orthogonal(m1[name], o1[name])
        exist1[name] = exist_orthogonal(m1[name], o1[name])
        inter1[name] = intersection_set(m1[name], o1[name])
        dots1[name] = pair_dots(m1[name], o1[name])
        new_meet1[name] = new_records_meeting_six_nn(site, ticks, 1)
        print(
            f"{name} t={ticks[site]} tau={tau1[name]} "
            f"M={incoming_display(m1[name])} "
            f"O={outgoing_display(o1[name])} "
            f"dots={dots_display(dots1[name])} "
            f"forall={bits1[name]}"
        )

    reverse_status = reverse_report(m1["A"], o1["A"], m1["B"], o1["B"])
    face_status = face_report(m1["C"], o1["C"], m1["D"], o1["D"])
    leftover_o_reverse0 = reverse_report(m0["A"], o0["A"], m0["B"], o0["B"])
    leftover_o_face0 = face_report(m0["C"], o0["C"], m0["D"], o0["D"])
    m_exist_opp_reverse = existential_opposite(m1["A"], m1["B"])
    m_exist_opp_face = existential_opposite(m1["C"], m1["D"])
    o_exist_opp_reverse = existential_opposite(o1["A"], o1["B"])
    o_exist_opp_face = existential_opposite(o1["C"], o1["D"])
    unique_reverse = reverse_report(
        unique_letter(m1["A"]),
        unique_letter(o1["A"]),
        unique_letter(m1["B"]),
        unique_letter(o1["B"]),
    )
    unique_face = face_report(
        unique_letter(m1["C"]),
        unique_letter(o1["C"]),
        unique_letter(m1["D"]),
        unique_letter(o1["D"]),
    )
    neighbor_reverse = reverse_report(
        neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"]),
        o1["A"],
        neighbor_lock_set(PROBES["B"], ticks, locks, tau1["B"]),
        o1["B"],
    )
    print(f"reverse={reverse_status} face={face_status}")
    print(
        "per_element: each pair (m,o) from M(q,t+1) against O(q,t+1) at a probe"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four M sets, four O sets, integer dots, forall-perp, reverse/face"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    def probe_cut(
        ticks_map: dict[Point, int],
        locks_map: dict[Point, set[Point]],
        seeds_map: dict[Point, Point],
        probes: dict[str, Point] = PROBES,
    ) -> tuple[dict[str, Incoming], dict[str, Outgoing], dict[str, str]]:
        incoming: dict[str, Incoming] = {}
        outgoing: dict[str, Outgoing] = {}
        bits: dict[str, str] = {}
        for name in ("A", "B", "C", "D"):
            site = probes[name]
            incoming[name] = incoming_set(
                site, ticks_map[site] + 1, ticks_map, locks_map, seeds_map
            )
            outgoing[name] = outgoing_set(
                site, ticks_map[site] + 1, ticks_map, locks_map, seeds_map
            )
            bits[name] = forall_orthogonal(incoming[name], outgoing[name])
        return incoming, outgoing, bits

    nstri_m1, nstri_o1, nstri_bits = probe_cut(
        nstri_ticks, nstri_locks, nstri_seeds
    )
    perp_m1, perp_o1, perp_bits = probe_cut(perp_ticks, perp_locks, perp_seeds)
    zsym_m1, zsym_o1, zsym_bits = probe_cut(
        zsym_ticks, zsym_locks, zsym_seeds
    )
    ysym_m1, ysym_o1, ysym_bits = probe_cut(
        ysym_ticks, ysym_locks, ysym_seeds
    )
    two_m1, two_o1, two_bits = probe_cut(two_ticks, two_locks, two_seeds)
    y_m1, y_o1, y_bits = probe_cut(ticks, locks, seed_map, Y_PROBES)

    nstri_reverse = reverse_report(
        nstri_m1["A"], nstri_o1["A"], nstri_m1["B"], nstri_o1["B"]
    )
    nstri_face = face_report(
        nstri_m1["C"], nstri_o1["C"], nstri_m1["D"], nstri_o1["D"]
    )
    nstri_exist_opp_reverse = existential_opposite(nstri_m1["A"], nstri_m1["B"])
    nstri_exist_opp_face = existential_opposite(nstri_m1["C"], nstri_m1["D"])
    nstri_exist_perp_b = exist_orthogonal(nstri_m1["B"], nstri_o1["B"])
    perp_reverse = reverse_report(
        perp_m1["A"], perp_o1["A"], perp_m1["B"], perp_o1["B"]
    )
    perp_face = face_report(
        perp_m1["C"], perp_o1["C"], perp_m1["D"], perp_o1["D"]
    )
    zsym_reverse = reverse_report(
        zsym_m1["A"], zsym_o1["A"], zsym_m1["B"], zsym_o1["B"]
    )
    zsym_m_exist_opp_reverse = existential_opposite(zsym_m1["A"], zsym_m1["B"])
    y_reverse = reverse_report(y_m1["A"], y_o1["A"], y_m1["B"], y_o1["B"])
    y_face = face_report(y_m1["C"], y_o1["C"], y_m1["D"], y_o1["D"])

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E2, NEG_E2)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E1, step)) != 1 for step in (E2, NEG_E2)
    )
    x_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E1, step)) != 1 for step in (E2, NEG_E2)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and x_mirror_parallel_blocked
        and ticks[NEG_E1] == 0
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "outgoing-set-undefined-if-unformed",
        outgoing_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and forall_orthogonal(
            incoming_set(PROBES["B"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED,
    )
    checks.check(
        "outgoing-empty-not-undefined",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["A"] != UNDEFINED
        and forall_orthogonal(m0["A"], o0["A"]) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(E1, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and m1["A"] == frozenset({NEG_E2}),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-O-at-tau",
        m1["A"] == set_m_a
        and m1["B"] == set_m_b
        and m1["C"] == set_m_c
        and m1["D"] == set_m_d
        and o1["A"] == set_o_a
        and o1["B"] == set_o_b
        and o1["C"] == set_o_c
        and o1["D"] == set_o_d
        and m1["D"] != UNDEFINED
        and len(m1["D"]) == 3
        and len(o1["A"]) == 3,
        str({name: incoming_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-dots-all-zero",
        all(
            isinstance(dots1[name], tuple)
            and dots1[name]
            and all(value == 0 for _a, _b, value in dots1[name])
            for name in ("A", "B", "C", "D")
        )
        and len(dots1["A"]) == 3
        and len(dots1["B"]) == 3
        and len(dots1["C"]) == 4
        and len(dots1["D"]) == 6,
        str({name: dots_display(dots1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-forall-perp-hold-at-each-probe",
        bits1["A"] == "hold"
        and bits1["B"] == "hold"
        and bits1["C"] == "hold"
        and bits1["D"] == "hold"
        and exist1["A"] == "hold"
        and exist1["B"] == "hold"
        and exist1["C"] == "hold"
        and exist1["D"] == "hold",
        str(bits1),
    )
    checks.check(
        "theorem1-M-frozen-O-not-frozen",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E2})
        and o1["A"] != o0["A"]
        and o1["D"] != o0["D"],
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E1
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and m1["A"] == frozenset({NEG_E2})
        and Y_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(m1["D"]) == 3
        and unique_letter(m1["D"]) == UNDEFINED
        and m1["D"] != UNDEFINED
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED,
    )
    checks.check(
        "theorem1-new-records-meet-6nn-at-tplus1",
        new_meet1["A"] == ((2, 0, 0), (1, 0, 1), (1, 0, -1))
        and new_meet1["B"] == ((2, 1, 1), (1, 1, 2), (1, 1, 0))
        and new_meet1["C"] == ((2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet1["D"] == ((1, 2, 0),),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and bits1["A"] == "hold"
        and bits1["B"] == "hold"
        and reverse_status != "fail"
        and reverse_status != UNDEFINED,
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and bits1["C"] == "hold"
        and bits1["D"] == "hold"
        and face_status != "fail"
        and face_status != UNDEFINED,
        face_status,
    )
    checks.check(
        "not-exist-opposite-leftover",
        m_exist_opp_reverse == "hold"
        and m_exist_opp_face == "hold"
        and o_exist_opp_reverse == "hold"
        and o_exist_opp_face == "hold"
        and reverse_status == "hold"
        and face_status == "hold"
        and nstri_exist_opp_reverse == "hold"
        and nstri_exist_opp_face == "hold"
        and nstri_reverse == "fail"
        and nstri_face == "fail"
        and reverse_status != nstri_reverse,
    )
    checks.check(
        "not-exist-perp-leftover",
        exist1["A"] == "hold"
        and nstri_exist_perp_b == "hold"
        and nstri_bits["B"] == "fail"
        and exist_orthogonal(nstri_m1["D"], nstri_o1["D"]) == "hold"
        and nstri_bits["D"] == "fail"
        and reverse_status == "hold"
        and nstri_reverse == "fail",
    )
    checks.check(
        "not-leftover-of-O-at-t",
        leftover_o_reverse0 == UNDEFINED
        and leftover_o_face0 == UNDEFINED
        and reverse_status == "hold"
        and face_status == "hold"
        and leftover_o_reverse0 != reverse_status,
    )
    checks.check(
        "not-unique-letter-leftover",
        unique_reverse == UNDEFINED
        and unique_face == UNDEFINED
        and reverse_status == "hold"
        and face_status == "hold"
        and unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(m1["D"]) == UNDEFINED,
    )
    checks.check(
        "not-empty-intersection-leftover",
        all(inter1[name] == frozenset() for name in ("A", "B", "C", "D"))
        and reverse_status == "hold"
        and intersection_set(nstri_m1["B"], nstri_o1["B"]) != frozenset()
        and nstri_bits["B"] == "fail"
        and intersection_set(frozenset({E1}), frozenset({NEG_E1})) == frozenset()
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail",
    )
    checks.check(
        "not-neighbor-lock-leftover",
        E2 in neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"])
        and E2 not in o1["A"]
        and neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"]) != o1["A"]
        and neighbor_reverse == "fail"
        and reverse_status == "hold",
    )
    checks.check(
        "not-nstri-or-perp-or-zmenu-or-y-probes",
        X_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and X_SYMMETRIC_SEEDS != PERP_SEEDS
        and X_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and X_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and nstri_bits["B"] == "fail"
        and nstri_bits["D"] == "fail"
        and nstri_reverse == "fail"
        and nstri_face == "fail"
        and perp_bits["B"] == "fail"
        and perp_reverse == "fail"
        and perp_face == "hold"
        and zsym_m1["A"] == frozenset({E2, NEG_E2})
        and zsym_m_exist_opp_reverse == "fail"
        and zsym_reverse == "hold"
        and zsym_bits["A"] == "hold"
        and y_m1["A"] != m1["A"]
        and probe_sites != y_probe_sites
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "not-nnlock-named-sign",
        named_sign(NEG_E2) == "-"
        and named_sign(E2) == "+"
        and named_sign(E1) == "+"
        and m1["A"] != named_sign(NEG_E2)
        and bits1["A"] != named_sign(NEG_E2),
    )
    checks.check(
        "incoming-outgoing-locks-are-nn-steps",
        all(m1[name] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(o1[name] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["D"]) == 3
        and len(o1["A"]) == 3
        and len(o1["C"]) == 4
        and bits1["D"] == "hold"
        and bits1["A"] == "hold"
        and reverse_status == "hold"
        and face_status == "hold",
    )
    checks.check(
        "x-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E2}
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and ticks[NEG_E1] == 0
        and locks[NEG_E1] == {NEG_E2}
        and add(E2, NEG_E2) == ZERO
        and sum(time == 0 for time in ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        forall_orthogonal(frozenset(), o1["B"]) == UNDEFINED
        and forall_orthogonal(m1["C"], frozenset()) == UNDEFINED
        and reverse_report(UNDEFINED, o1["A"], m1["B"], o1["B"]) == UNDEFINED
        and leftover_o_reverse0 == UNDEFINED,
    )
    checks.check(
        "mutation-parallel-pair-fails",
        forall_orthogonal(frozenset({E1}), frozenset({E1})) == "fail"
        and forall_orthogonal(frozenset({E1}), frozenset({NEG_E1})) == "fail"
        and bits1["A"] == "hold"
        and reverse_status == "hold",
    )
    checks.check(
        "mutation-sum-is-not-forall",
        sum_of_set(m1["A"]) == NEG_E2
        and sum_of_set(o1["A"]) == E1
        and dot(sum_of_set(m1["A"]), sum_of_set(o1["A"])) == 0
        and sum_of_set(m1["D"]) == NEG_E1
        and sum_of_set(o1["D"]) == ZERO
        and m1["D"] != frozenset({NEG_E1})
        and len(m1["D"]) == 3
        and bits1["D"] == "hold",
    )
    checks.check(
        "two-site-same-x-probes-is-not-the-seed",
        X_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and two_m1["A"] == m1["A"]
        and two_bits["A"] == "hold"
        and ticks[NEG_E1] == 0
        and two_ticks.get(NEG_E1) != 0
        and ysym_bits["A"] == "hold"
        and y_reverse == "hold"
        and y_face == "hold",
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O-dots-forall",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "M(A, τ) = {−e_2}" in note
        and "M(B, τ) = {+e_2}" in note
        and "M(C, τ) = {+e_1}" in note
        and "M(D, τ) = {−e_1, +e_3, −e_3}" in note
        and "O(A, τ) = {+e_1, +e_3, −e_3}" in note
        and "O(B, τ) = {+e_1, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_2, −e_2, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_2, −e_2}" in note
        and "forall-perp(A) = hold" in note
        and "forall-perp(B) = hold" in note
        and "forall-perp(C) = hold" in note
        and "forall-perp(D) = hold" in note,
    )
    checks.check(
        "note-reports-reverse-face-hold",
        "Reverse: hold" in note
        and "Face: hold" in note
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
        and "mixed stays a set" in normalized_note,
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
        "note-not-unique-or-sum-or-exist-opp-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "not leftover of exist-opposite" in normalized_note
        and "not leftover of exist-perp" in normalized_note
        and "not leftover of O at t" in normalized_note
        and "Reverse holds." in note
        and "Face holds." in note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "own incoming set" in normalized_note
        and "outgoing dual" in normalized_note,
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
        '    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "forall_orthogonal" in defined_fns
        and "pair_dots" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "form" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
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
