#!/usr/bin/env python3
"""Forall-orthogonal M vs O at t+1 reverse/face on four #7208 y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0)} with locks +e_1 and -e_1 (nsopp #7093; same process and
y-probes as nsmopp #7208). A 6-NN step is allowed iff it is perpendicular
to the parent lock axis. Newly formed sites lock the incoming step. Seeds
keep their seed letters as a singleton. M(q, tau) is the set of earliest
incoming nearest-neighbor steps at q using only records with tick <= tau.
O(q, tau) is the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3}
such that q+e is formed and e is in M(q+e, tau). Unformed at tau =>
UNDEFINED. For formed q with both M and O defined and nonempty, forall-perp
holds iff every m in M(q, tau) and o in O(q, tau) have integer dot m·o=0.
Empty or UNDEFINED => UNDEFINED. Exist-perp (some pair dots to 0) is
comparison only. Reverse holds iff forall-perp at A and at B. Face holds
iff forall-perp at C and at D. Not exist-opposite leftover. Uniqueness of
locks is not required. Occupancy n is not used. Named-sign lettering is
not used. No unique P_+. No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OPPOSITE_LOCK_YPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OPPOSITE_LOCK_YPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
BALL_SQ = 9
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
    "Forall-orthogonal M vs O at t+1 on the four #7208 y-probes, "
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
    seeds: tuple[tuple[Point, Point], ...] = TWO_SITE_SEEDS,
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


def dots_display(pairs: tuple[tuple[Point, Point, int], ...]) -> str:
    if not pairs:
        return ""
    parts = [
        f"({LOCK_NAME[a]})·({LOCK_NAME[b]})={value}" for a, b, value in pairs
    ]
    return ", ".join(parts)


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
    """nmsimopp leftover: hold iff some lock in left is vector opposite of some in right."""
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


def opposite_pair(left: Incoming, right: Incoming) -> tuple[Point, Point] | None:
    if left == UNDEFINED or right == UNDEFINED:
        return None
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        return None
    for a in NN:
        if a not in left:
            continue
        for b in NN:
            if b in right and add(a, b) == ZERO:
                return (a, b)
    return None


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

    print("forall-orthogonal M vs O at t+1 reverse/face on #7208 y-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
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
        and add(E3, NEG_E3) == ZERO
        and dot(E1, E2) == 0
        and dot(E1, E1) == 1
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
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
        and forall_orthogonal(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3}))
        == "hold",
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

    ticks, locks, seed_map = form()
    tau1: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    dots1: dict[str, tuple[tuple[Point, Point, int], ...]] = {}
    forall1: dict[str, str] = {}
    exist1: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau1[name] = ticks[site] + 1
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        dots1[name] = integer_dots(m1[name], o1[name])
        forall1[name] = forall_orthogonal(m1[name], o1[name])
        exist1[name] = exist_perp(m1[name], o1[name])
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"O={lockset_display(o1[name])} "
            f"dots={dots_display(dots1[name])} "
            f"forall-perp={forall1[name]}"
        )

    reverse_status = reverse_report(forall1["A"], forall1["B"])
    face_status = face_report(forall1["C"], forall1["D"])
    m_opp_pair = opposite_pair(m1["A"], m1["B"])
    o_opp_pair = opposite_pair(o1["A"], o1["B"])
    leftover_m_reverse = existential_opposite(m1["A"], m1["B"])
    leftover_o_reverse = existential_opposite(o1["A"], o1["B"])
    leftover_m_face = existential_opposite(m1["C"], m1["D"])
    leftover_o_face = existential_opposite(o1["C"], o1["D"])
    print(f"reverse={reverse_status} face={face_status}")
    print(
        f"leftover exist-opposite M reverse={leftover_m_reverse} "
        f"O reverse={leftover_o_reverse}"
    )
    print(
        "per_element: each integer dot m·o of earliest incoming M and outgoing O"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
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
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and forall_orthogonal(
            incoming_set(PROBES["B"], 1, ticks, locks, seed_map),
            outgoing_set(PROBES["B"], 1, ticks, locks, seed_map),
        )
        == UNDEFINED,
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
        "theorem1-M-at-tau",
        m1["A"] == frozenset({NEG_E1})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E2, E3, NEG_E3}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == frozenset({E2, E3, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1}),
        str({name: lockset_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    expected_dots = {
        "A": (
            (NEG_E1, E2, 0),
            (NEG_E1, E3, 0),
            (NEG_E1, NEG_E3, 0),
        ),
        "B": (
            (E1, E2, 0),
            (E1, E3, 0),
            (E1, NEG_E3, 0),
        ),
        "C": (
            (E2, E1, 0),
            (E2, NEG_E1, 0),
            (E2, E3, 0),
            (E2, NEG_E3, 0),
        ),
        "D": (
            (NEG_E2, E1, 0),
            (NEG_E2, NEG_E1, 0),
            (E3, E1, 0),
            (E3, NEG_E1, 0),
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
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and m1["A"] == frozenset({NEG_E1}),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(m1["D"], frozenset)
        and len(m1["D"]) == 3
        and unique_letter(m1["D"]) == UNDEFINED
        and isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED
        and forall1["D"] == "hold"
        and forall1["A"] == "hold",
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse_status == "hold"
        and forall1["A"] == "hold"
        and forall1["B"] == "hold"
        and reverse_status != "fail"
        and reverse_status != UNDEFINED,
        reverse_status,
    )
    checks.check(
        "theorem3-face-hold",
        face_status == "hold"
        and forall1["C"] == "hold"
        and forall1["D"] == "hold"
        and face_status != "fail"
        and face_status != UNDEFINED,
        face_status,
    )
    checks.check(
        "not-exist-opposite-leftover",
        leftover_m_reverse == "hold"
        and leftover_o_reverse == "hold"
        and leftover_m_face == "hold"
        and leftover_o_face == "hold"
        and m_opp_pair == (NEG_E1, E1)
        and o_opp_pair == (E3, NEG_E3)
        and reverse_status == "hold"
        and face_status == "hold"
        and forall_orthogonal is not existential_opposite,
    )
    checks.check(
        "leftover-M-reverse-uses-pm-e1-O-reverse-uses-pm-e3",
        m_opp_pair == (NEG_E1, E1)
        and o_opp_pair == (E3, NEG_E3)
        and add(NEG_E1, E1) == ZERO
        and add(E3, NEG_E3) == ZERO
        and leftover_m_reverse == "hold"
        and leftover_o_reverse == "hold",
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
        and len(m1["D"]) == 3
        and len(o1["A"]) == 3
        and unique_letter(m1["D"]) == UNDEFINED
        and unique_letter(o1["A"]) == UNDEFINED
        and forall1["A"] == "hold"
        and forall1["D"] == "hold",
    )
    checks.check(
        "two-site-opposite-lock-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and TWO_SITE_SEEDS != PERP_SEEDS
        and TWO_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    x_m1 = {
        name: incoming_set(
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
        and x_m1["A"] != m1["A"]
        and reverse_status == "hold",
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "M(A, τ) = {−e_1}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_2}" in note
        and "M(D, τ) = {−e_2, +e_3, −e_3}" in note
        and "O(A, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(B, τ) = {+e_2, +e_3, −e_3}" in note
        and "O(C, τ) = {+e_1, −e_1, +e_3, −e_3}" in note
        and "O(D, τ) = {+e_1, −e_1}" in note,
    )
    checks.check(
        "note-reports-dots-and-forall-perp",
        "(−e_1)·(+e_2)=0, (−e_1)·(+e_3)=0, (−e_1)·(−e_3)=0" in note
        and "(+e_1)·(+e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0" in note
        and "(+e_2)·(+e_1)=0, (+e_2)·(−e_1)=0, (+e_2)·(+e_3)=0, (+e_2)·(−e_3)=0"
        in note
        and "(−e_2)·(+e_1)=0, (−e_2)·(−e_1)=0, (+e_3)·(+e_1)=0, (+e_3)·(−e_1)=0, (−e_3)·(+e_1)=0, (−e_3)·(−e_1)=0"
        in note
        and "forall-perp at A: hold" in note
        and "forall-perp at B: hold" in note
        and "forall-perp at C: hold" in note
        and "forall-perp at D: hold" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse: hold" in note
        and "Face: hold" in note
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
        "note-not-exist-opposite-leftover",
        "not exist-opposite leftover" in normalized_note
        and "M reverse uses ±e_1" in note
        and "O reverse uses ±e_3" in note
        and "Exist-perp" in note,
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
        and "forall-perp" in normalized_note,
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
        '    "docs/OPPOSITE_LOCK_YPROBE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "exist_perp" in defined_fns
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
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
