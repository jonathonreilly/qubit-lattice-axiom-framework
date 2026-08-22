#!/usr/bin/env python3
"""Forall-orthogonal M versus O at t+1 reverse/face on four #7211 y-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (0,-1,0)} with locks +e_1, -e_1, and -e_1 (nsyopp #7132;
same process and y-probes as nmsyop #7211). A 6-NN step is allowed iff it
is perpendicular to the parent lock axis. Newly formed sites lock the
incoming step. Seeds keep their seed letters as a singleton.
t(q) is the formation tick. tau = t+1. M(q, tau) is the set of earliest
incoming nearest-neighbor steps at q using only records with tick <= tau.
O(q, tau) is the outgoing dual of M: the set of e in {±e_1,±e_2,±e_3}
such that q+e is formed in B_3(0) and e is in M(q+e, tau). Unformed at tau
=> UNDEFINED. Forall-perp HOLD iff every m in M(q, tau) and every o in
O(q, tau) have m·o=0. Empty or UNDEFINED => UNDEFINED. Reverse HOLD iff
forall-perp at A and at B. Face likewise on C, D. Uniqueness is not
required. Unique L is not the object. Occupancy n is not used. Named-sign
lettering is not used. No unique P_+. No 6-NN star. No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_SYMMETRIC_THREE_SITE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_SYMMETRIC_THREE_SITE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
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
NSTRI_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
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
    "Forall-orthogonal M vs O at t+1 on the four #7211 y-probes, "
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


def site_display(site: Point) -> str:
    return f"({site[0]}, {site[1]}, {site[2]})"


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
    seeds: tuple[tuple[Point, Point], ...] = Y_SYMMETRIC_SEEDS,
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


def forall_orthogonal(incoming: Incoming, outgoing: Outgoing) -> str:
    """HOLD iff every m in M and every o in O have m·o=0.

    Empty or UNDEFINED on either side is UNDEFINED. Nonempty with a
    nonzero pair fails. Mixed stays a set. Does not require a singleton.
    """
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    if not incoming or not outgoing:
        return UNDEFINED
    for m in incoming:
        for o in outgoing:
            if dot(m, o) != 0:
                return "fail"
    return "hold"


def pair_and(left: str, right: str) -> str:
    """HOLD iff both sides hold. Fail dominates. Else UNDEFINED."""
    if left == "fail" or right == "fail":
        return "fail"
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(status_a: str, status_b: str) -> str:
    """Reverse HOLD iff forall-perp at A and at B."""
    return pair_and(status_a, status_b)


def face_report(status_c: str, status_d: str) -> str:
    """Face HOLD iff forall-perp at C and at D."""
    return pair_and(status_c, status_d)


def dots_display(incoming: Incoming, outgoing: Outgoing) -> str:
    """NN-ordered list of m·o, or UNDEFINED when the pair cannot be scored."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    if not incoming or not outgoing:
        return UNDEFINED
    values: list[str] = []
    for m in NN:
        if m not in incoming:
            continue
        for o in NN:
            if o not in outgoing:
                continue
            values.append(str(dot(m, o)))
    return ",".join(values)


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Leftover comparator: some pair sums to zero. Not this predicate."""
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
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        suffix = f" {detail}" if detail else ""
        print(f"{'PASS' if result else 'FAIL'}: {label}{suffix}")

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

    print("forall-orthogonal M vs O at t+1 reverse/face on #7211 y-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-y-probes-in-host",
        probe_sites == ((0, 1, 0), (1, 1, 1), (0, 2, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and PROBES != X_PROBES
        and ORIGIN not in probe_sites,
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
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "forall-orthogonal-identity",
        forall_orthogonal(UNDEFINED, frozenset({E2})) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), UNDEFINED) == UNDEFINED
        and forall_orthogonal(frozenset(), frozenset({E2})) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), frozenset()) == UNDEFINED
        and forall_orthogonal(frozenset({E1}), frozenset({E1})) == "fail"
        and forall_orthogonal(frozenset({E1}), frozenset({E1, E2})) == "fail"
        and forall_orthogonal(frozenset({E1}), frozenset({E2, E3})) == "hold"
        and forall_orthogonal(frozenset({NEG_E1, E2}), frozenset({E3})) == "hold"
        and forall_orthogonal(frozenset({E2, E3}), frozenset({E2})) == "fail",
    )
    checks.check(
        "pair-and-identity",
        reverse_report("hold", "hold") == "hold"
        and reverse_report("hold", "fail") == "fail"
        and reverse_report("fail", UNDEFINED) == "fail"
        and reverse_report(UNDEFINED, "hold") == UNDEFINED
        and reverse_report(UNDEFINED, UNDEFINED) == UNDEFINED
        and face_report("hold", "hold") == "hold"
        and face_report("hold", UNDEFINED) == UNDEFINED
        and face_report("fail", "hold") == "fail",
    )
    checks.check(
        "existential-opposite-is-leftover",
        existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E2, E3, NEG_E3}))
        == "fail"
        and existential_opposite(frozenset(), frozenset({E1})) == UNDEFINED,
    )

    ticks, locks, seed_map = form()
    tau1: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    perp: dict[str, str] = {}
    dots: dict[str, str] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau1[name] = ticks[site] + 1
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        perp[name] = forall_orthogonal(m1[name], o1[name])
        dots[name] = dots_display(m1[name], o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} tau={tau1[name]} "
            f"M={incoming_display(m1[name])} "
            f"O={outgoing_display(o1[name])} "
            f"dots={dots[name]} forall-perp={perp[name]} "
            f"new={','.join(site_display(site_n) for site_n in new_meet[name]) or '{}'}"
        )

    reverse = reverse_report(perp["A"], perp["B"])
    face = face_report(perp["C"], perp["D"])
    unique_perp = {
        name: forall_orthogonal(unique_letter(m1[name]), unique_letter(o1[name]))
        for name in ("A", "B", "C", "D")
    }
    unique_reverse = reverse_report(unique_perp["A"], unique_perp["B"])
    unique_face = face_report(unique_perp["C"], unique_perp["D"])
    exist_mo = {
        name: existential_opposite(m1[name], o1[name])
        for name in ("A", "B", "C", "D")
    }
    exist_m_reverse = existential_opposite(m1["A"], m1["B"])
    exist_o_reverse = existential_opposite(o1["A"], o1["B"])
    exist_m_face = existential_opposite(m1["C"], m1["D"])
    exist_o_face = existential_opposite(o1["C"], o1["D"])
    leftover_neighbor_reverse = reverse_report(
        forall_orthogonal(
            neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"]),
            o1["A"],
        ),
        forall_orthogonal(
            neighbor_lock_set(PROBES["B"], ticks, locks, tau1["B"]),
            o1["B"],
        ),
    )
    tau0_o_a = outgoing_set(PROBES["A"], ticks[PROBES["A"]], ticks, locks, seed_map)
    tau0_perp_a = forall_orthogonal(
        incoming_set(PROBES["A"], ticks[PROBES["A"]], ticks, locks, seed_map),
        tau0_o_a,
    )
    print(f"reverse={reverse}")
    print(f"face={face}")
    print(
        "per_element: each pair (m,o) with m in M(q,t+1) and o in O(q,t+1) "
        "at a scored y-probe"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four (M,O) pairs at t+1 plus forall-perp and reverse/face bits"
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
    y_mirror_parallel_blocked = all(
        ticks.get(add(NEG_E2, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and y_mirror_parallel_blocked
        and ticks[NEG_E2] == 0
        and ticks[E3] == 1
        and ticks[NEG_E3] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "incoming-set-undefined-if-unformed",
        incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "outgoing-set-undefined-if-unformed",
        outgoing_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "y-symmetric-three-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E1}
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and ticks[NEG_E2] == 0
        and locks[NEG_E2] == {NEG_E1}
        and Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and Y_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 3,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and tau1["A"] == 1
        and tau1["B"] == 3
        and tau1["C"] == 2
        and tau1["D"] == 4,
    )
    checks.check(
        "theorem1-M-at-tplus1",
        m1["A"] == frozenset({NEG_E1})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E2})
        and m1["D"] == frozenset({NEG_E2, E3, NEG_E3}),
        str({name: incoming_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tplus1",
        o1["A"] == frozenset({E2, E3, NEG_E3})
        and o1["B"] == frozenset({E2, E3, NEG_E3})
        and o1["C"] == frozenset({E1, NEG_E1, E3, NEG_E3})
        and o1["D"] == frozenset({E1, NEG_E1}),
        str({name: outgoing_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-dots-all-zero",
        dots["A"] == "0,0,0"
        and dots["B"] == "0,0,0"
        and dots["C"] == "0,0,0,0"
        and dots["D"] == "0,0,0,0,0,0"
        and all(
            isinstance(m1[name], frozenset)
            and isinstance(o1[name], frozenset)
            and all(dot(m, o) == 0 for m in m1[name] for o in o1[name])
            for name in ("A", "B", "C", "D")
        ),
        str(dots),
    )
    checks.check(
        "theorem1-forall-perp-hold-at-four-probes",
        perp["A"] == "hold"
        and perp["B"] == "hold"
        and perp["C"] == "hold"
        and perp["D"] == "hold",
        str(perp),
    )
    checks.check(
        "theorem1-O-disjoint-from-M",
        all(
            isinstance(m1[name], frozenset)
            and isinstance(o1[name], frozenset)
            and m1[name].isdisjoint(o1[name])
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((0, 2, 0), (0, 1, 1), (0, 1, -1))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1))
        and new_meet["D"] == ((2, 1, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse == "hold" and perp["A"] == "hold" and perp["B"] == "hold",
    )
    checks.check(
        "theorem3-face-hold",
        face == "hold" and perp["C"] == "hold" and perp["D"] == "hold",
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(m1["D"], frozenset)
        and isinstance(o1["A"], frozenset)
        and len(m1["A"]) == 1
        and len(m1["B"]) == 1
        and len(m1["C"]) == 1
        and len(m1["D"]) == 3
        and len(o1["A"]) == 3
        and len(o1["B"]) == 3
        and len(o1["C"]) == 4
        and len(o1["D"]) == 2
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-unique-letter-undefined",
        unique_letter(o1["A"]) == UNDEFINED
        and unique_letter(o1["B"]) == UNDEFINED
        and unique_letter(m1["D"]) == UNDEFINED
        and unique_perp["A"] == UNDEFINED
        and unique_reverse == UNDEFINED
        and unique_face == UNDEFINED
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-exist-opposite-M-vs-O-fails",
        exist_mo["A"] == "fail"
        and exist_mo["B"] == "fail"
        and exist_mo["C"] == "fail"
        and exist_mo["D"] == "fail"
        and perp["A"] == "hold"
        and reverse == "hold",
    )
    checks.check(
        "mutation-exist-opposite-same-kind-leftover",
        exist_m_reverse == "hold"
        and exist_m_face == "hold"
        and exist_o_reverse == "hold"
        and exist_o_face == "hold"
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "mutation-empty-O-at-t-is-undefined-perp",
        tau0_o_a == frozenset()
        and tau0_o_a != UNDEFINED
        and tau0_perp_a == UNDEFINED
        and perp["A"] == "hold",
    )
    checks.check(
        "mutation-neighbor-lock-leftover",
        leftover_neighbor_reverse == "fail"
        and reverse == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(m1["D"], frozenset)
        and isinstance(o1["A"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E1
        and sum_of_set(o1["A"]) == E2
        and sum_of_set(m1["D"]) == NEG_E2
        and m1["D"] != frozenset({NEG_E2})
        and o1["A"] != frozenset({E2})
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "M-is-not-O",
        m1["A"] != o1["A"]
        and m1["B"] != o1["B"]
        and m1["C"] != o1["C"]
        and m1["D"] != o1["D"],
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O-dots-perp",
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
        and "O(D, τ) = {+e_1, −e_1}" in note
        and "dots(A) = 0,0,0" in note
        and "dots(B) = 0,0,0" in note
        and "dots(C) = 0,0,0,0" in note
        and "dots(D) = 0,0,0,0,0,0" in note
        and "forall-perp at A: hold" in note
        and "forall-perp at B: hold" in note
        and "forall-perp at C: hold" in note
        and "forall-perp at D: hold" in note,
    )
    checks.check(
        "note-reports-reverse-hold-face-hold",
        "Reverse: hold" in note and "Face: hold" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-exist-opposite-or-unique-letter-leftover",
        "not leftover of existential opposite of `M` versus `O`" in normalized_note
        and "not leftover of unique own-incoming or own-outgoing letters"
        in normalized_note
        and "Mixed remains a set" in note,
    )
    checks.check(
        "note-not-same-kind-exist-opposite",
        "not leftover of existential opposite inside `M` or inside `O`"
        in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "Occupancy `n` is not used" in note
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
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/Y_SYMMETRIC_THREE_SITE_INCOMING_OUTGOING_FORALL_ORTHOGONAL_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "dots_display" in defined_fns
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
