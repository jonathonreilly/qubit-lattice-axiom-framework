#!/usr/bin/env python3
"""Two-tick own-outgoing-set reverse/face composition on #7213 x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (1,0,0), (-1,0,0)} with locks +e_2, -e_2, and -e_2 (x-symmetric
three-site; same process and x-probes as nmszopx #7213). A 6-NN step is
allowed iff it is perpendicular to the parent lock axis. Newly formed sites
lock the incoming step. Seeds keep their seed letters as a singleton.
M(r, tau) is the set of earliest incoming nearest-neighbor steps at r using
only records with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is
the outgoing dual of M: the set of e in {+/-e_1,+/-e_2,+/-e_3} such that
q+e is formed in B_3(0) and e is in M(q+e, tau). Unformed q at tau =>
UNDEFINED. Empty O is empty, not UNDEFINED. O is not M. Reverse at a cut
uses O(A, .) and O(B, .) at each probe's own t or t+1; face likewise on
C, D. Empty or UNDEFINED => UNDEFINED. Composition HOLD iff the t+1
reverse/face bits equal the t bits. No global T. No 6-NN star. Uniqueness
of outgoing locks is not required. No unique P_+. Occupancy n is not used.
Named-sign lettering is not used. No larger host.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_OUTGOING_SET_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_OUTGOING_SET_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Reverse/face from O at t versus t+1 on the four #7213 "
    "x-probes, and composition, are reported. Displayed, not adopted."
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


def outgoing_display(value: Outgoing) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"outgoing is not a lock set: {value!r}")
    return set_display(value)


def incoming_display(value: Incoming) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"incoming is not a lock set: {value!r}")
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


def eventual_outgoing_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Outgoing:
    """nmoutzx leftover: eventual neighbor locks, no t versus t+1 cut."""
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


def existential_opposite(left: Outgoing, right: Outgoing) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("outgoing sides must be lock sets or UNDEFINED")
    if not left or not right:
        return UNDEFINED
    for a in left:
        for b in right:
            if add(a, b) == ZERO:
                return "hold"
    return "fail"


def reverse_report(set_a: Outgoing, set_b: Outgoing) -> str:
    return existential_opposite(set_a, set_b)


def face_report(set_c: Outgoing, set_d: Outgoing) -> str:
    return existential_opposite(set_c, set_d)


def composition_report(rev0: str, rev1: str, face0: str, face1: str) -> str:
    """HOLD iff t+1 bits equal t bits."""
    if rev0 != rev1 or face0 != face1:
        return "fail"
    return "HOLD"


def unique_letter(value: Outgoing) -> Outgoing:
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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("two-tick own-outgoing-set reverse/face composition on #7213 x-probes")
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
    checks.check("host-is-b3-closed-ball", ORIGIN in host and len(host) == 123)
    checks.check(
        "four-x-probes-in-host",
        probe_sites == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and set(probe_sites) <= host
        and ORIGIN not in probe_sites
        and probe_sites != y_probe_sites,
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
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "existential-opposite-identity",
        existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset(), frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset({E2, NEG_E2}), frozenset({E1})) == "fail"
        and existential_opposite(frozenset({E1}), frozenset({E1})) == "fail"
        and existential_opposite(frozenset({NEG_E2}), frozenset({E2})) == "hold"
        and existential_opposite(
            frozenset({E1, E3, NEG_E3}), frozenset({E1, E3, NEG_E3})
        )
        == "hold"
        and existential_opposite(
            frozenset({E2, NEG_E2, E3, NEG_E3}), frozenset({E2, NEG_E2})
        )
        == "hold",
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
    o_eventual: dict[str, Outgoing] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        o_eventual[name] = eventual_outgoing_set(site, ticks, locks)
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M(tau0)={incoming_display(m0[name])} "
            f"O(tau0)={outgoing_display(o0[name])} "
            f"O(tau1)={outgoing_display(o1[name])} "
            f"new={','.join(site_display(site_n) for site_n in new_meet[name]) or '{}'}"
        )

    reverse0 = reverse_report(o0["A"], o0["B"])
    reverse1 = reverse_report(o1["A"], o1["B"])
    face0 = face_report(o0["C"], o0["D"])
    face1 = face_report(o1["C"], o1["D"])
    composition = composition_report(reverse0, reverse1, face0, face1)
    m_reverse0 = reverse_report(m0["A"], m0["B"])
    m_reverse1 = reverse_report(m1["A"], m1["B"])
    m_face0 = face_report(m0["C"], m0["D"])
    m_face1 = face_report(m1["C"], m1["D"])
    m_composition = composition_report(m_reverse0, m_reverse1, m_face0, m_face1)
    unique_reverse1 = reverse_report(unique_letter(o1["A"]), unique_letter(o1["B"]))
    unique_face1 = face_report(unique_letter(o1["C"]), unique_letter(o1["D"]))
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
    print(f"reverse tau0={reverse0} tau1={reverse1}")
    print(f"face tau0={face0} tau1={face1}")
    print(f"composition={composition}")
    print(
        "per_element: each earliest outgoing nearest-neighbor step at a probe, "
        "read from the record prefix at that probe's t and at t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four outgoing sets at two cuts plus reverse/face/composition bits"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

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
        and outgoing_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and outgoing_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "outgoing-empty-not-undefined",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["A"] != UNDEFINED
        and o0["B"] != UNDEFINED
        and o0["C"] != UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(E1, 0, ticks, locks, seed_map) == frozenset({NEG_E2})
        and incoming_set(E1, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and incoming_set(NEG_E1, 0, ticks, locks, seed_map) == frozenset({NEG_E2})
        and m0["A"] == frozenset({NEG_E2}),
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
        "theorem1-O-at-tau0",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E2}),
        str({name: outgoing_display(o0[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau1",
        o1["A"] == frozenset({E1, E3, NEG_E3})
        and o1["B"] == frozenset({E1, E3, NEG_E3})
        and o1["C"] == frozenset({E2, NEG_E2, E3, NEG_E3})
        and o1["D"] == frozenset({E2, NEG_E2}),
        str({name: outgoing_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-tau1-strictly-larger",
        isinstance(o0["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and isinstance(o0["B"], frozenset)
        and isinstance(o1["B"], frozenset)
        and isinstance(o0["C"], frozenset)
        and isinstance(o1["C"], frozenset)
        and isinstance(o0["D"], frozenset)
        and isinstance(o1["D"], frozenset)
        and o0["A"] < o1["A"]
        and o0["B"] < o1["B"]
        and o0["C"] < o1["C"]
        and o0["D"] < o1["D"],
    )
    checks.check(
        "theorem1-M-two-tick-frozen",
        m0["A"] == frozenset({NEG_E2})
        and m0["B"] == frozenset({E2})
        and m0["C"] == frozenset({E1})
        and m0["D"] == frozenset({NEG_E1, E3, NEG_E3})
        and m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-O-disjoint-from-M",
        all(
            isinstance(o0[name], frozenset)
            and isinstance(o1[name], frozenset)
            and isinstance(m0[name], frozenset)
            and o0[name].isdisjoint(m0[name])
            and o1[name].isdisjoint(m0[name])
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "theorem1-new-records-meet-6nn",
        new_meet["A"] == ((2, 0, 0), (1, 0, 1), (1, 0, -1))
        and new_meet["B"] == ((2, 1, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet["D"] == ((1, 2, 0),),
        str(new_meet),
    )
    checks.check(
        "theorem1-new-neighbors-enter-O",
        all(
            ticks[neighbor] == ticks[PROBES[name]] + 1
            for name in ("A", "B", "C", "D")
            for neighbor in new_meet[name]
        )
        and PROBES["C"] in new_meet["A"]
        and PROBES["D"] in new_meet["B"]
        and E1 in o1["A"]
        and E3 in o1["A"]
        and NEG_E3 in o1["A"]
        and E2 in o1["D"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        isinstance(o1["A"], frozenset)
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED
        and o1["A"] != UNDEFINED
        and isinstance(o1["D"], frozenset)
        and len(o1["D"]) == 2
        and unique_letter(o1["D"]) == UNDEFINED
        and isinstance(o1["C"], frozenset)
        and len(o1["C"]) == 4
        and unique_letter(o1["C"]) == UNDEFINED,
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E1
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and m0["A"] == frozenset({NEG_E2})
        and Y_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-D-tau0-seed-dual",
        o0["D"] == frozenset({NEG_E2})
        and add(PROBES["D"], NEG_E2) == PROBES["A"]
        and m0["A"] == frozenset({NEG_E2}),
    )
    checks.check(
        "theorem2-reverse-tau0-undefined-tau1-hold",
        reverse0 == UNDEFINED
        and reverse1 == "hold"
        and add(E3, NEG_E3) == ZERO
        and E3 in o1["A"]
        and NEG_E3 in o1["B"]
        and reverse0 != "hold"
        and reverse1 != UNDEFINED,
    )
    checks.check(
        "theorem2-face-tau0-undefined-tau1-hold",
        face0 == UNDEFINED
        and face1 == "hold"
        and add(E2, NEG_E2) == ZERO
        and E2 in o1["C"]
        and NEG_E2 in o1["D"]
        and face0 != "hold"
        and face1 != UNDEFINED,
    )
    checks.check(
        "theorem3-composition-fail",
        composition == "fail"
        and reverse1 != reverse0
        and face1 != face0,
    )
    checks.check(
        "mutation-nmt2zx-M-two-tick-hold-hold",
        m_reverse0 == "hold"
        and m_reverse1 == "hold"
        and m_face0 == "hold"
        and m_face1 == "hold"
        and m_composition == "HOLD"
        and composition == "fail",
    )
    checks.check(
        "mutation-nmoutzx-eventual-O-hold-hold",
        o_eventual["A"] == o1["A"]
        and o_eventual["B"] == o1["B"]
        and o_eventual["C"] == o1["C"]
        and o_eventual["D"] == o1["D"]
        and eventual_reverse == "hold"
        and eventual_face == "hold"
        and reverse0 == UNDEFINED
        and face0 == UNDEFINED,
    )
    checks.check(
        "mutation-unique-letter-tau1-undefined",
        unique_reverse1 == UNDEFINED
        and unique_face1 == UNDEFINED
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "mutation-neighbor-lock-leftover-differs",
        leftover_neighbor_reverse == "fail"
        and leftover_neighbor_face == "hold"
        and reverse0 == UNDEFINED
        and reverse1 == "hold"
        and E2 in neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
        and NEG_E2 not in neighbor_lock_set(
            PROBES["A"], ticks, locks, ticks[PROBES["A"]]
        ),
    )
    checks.check(
        "mutation-empty-plus-undefined",
        existential_opposite(frozenset(), o1["B"]) == UNDEFINED
        and reverse0 == UNDEFINED
        and reverse1 == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed-A",
        isinstance(o1["A"], frozenset)
        and isinstance(o1["D"], frozenset)
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["B"]) == E1
        and sum_of_set(o1["C"]) == ZERO
        and sum_of_set(o1["D"]) == ZERO
        and o1["A"] != frozenset({E1})
        and o1["C"] != frozenset()
        and len(o1["A"]) == 3,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m0["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E2 in m0["A"]
        and NEG_E2 not in o1["A"]
        and E2 in m0["B"]
        and E2 not in o1["B"]
        and o1["A"] != m0["A"]
        and o0["A"] != m0["A"],
    )
    checks.check(
        "reverse-hold-7213-not-also-outgoing",
        isinstance(m0["A"], frozenset)
        and isinstance(m0["B"], frozenset)
        and isinstance(o1["A"], frozenset)
        and isinstance(o1["B"], frozenset)
        and NEG_E2 in m0["A"]
        and E2 in m0["B"]
        and NEG_E2 not in o1["A"]
        and E2 not in o1["B"],
    )
    y_o1 = {
        name: outgoing_set(
            Y_PROBES[name],
            ticks[Y_PROBES[name]] + 1,
            ticks,
            locks,
            seed_map,
        )
        for name in ("A", "B", "C", "D")
        if Y_PROBES[name] in ticks
    }
    y_reverse1 = reverse_report(y_o1["A"], y_o1["B"])
    y_face1 = face_report(y_o1["C"], y_o1["D"])
    two_o1 = {
        name: outgoing_set(
            PROBES[name],
            two_ticks[PROBES[name]] + 1,
            two_ticks,
            two_locks,
            two_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in two_ticks
    }
    ysym_o1 = {
        name: outgoing_set(
            PROBES[name],
            ysym_ticks[PROBES[name]] + 1,
            ysym_ticks,
            ysym_locks,
            ysym_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in ysym_ticks
    }
    zsym_o1 = {
        name: outgoing_set(
            PROBES[name],
            zsym_ticks[PROBES[name]] + 1,
            zsym_ticks,
            zsym_locks,
            zsym_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in zsym_ticks
    }
    nstri_o1 = {
        name: outgoing_set(
            PROBES[name],
            nstri_ticks[PROBES[name]] + 1,
            nstri_ticks,
            nstri_locks,
            nstri_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in nstri_ticks
    }
    perp_o1 = {
        name: outgoing_set(
            PROBES[name],
            perp_ticks[PROBES[name]] + 1,
            perp_ticks,
            perp_locks,
            perp_seeds,
        )
        for name in ("A", "B", "C", "D")
        if PROBES[name] in perp_ticks
    }
    ysym_reverse1 = reverse_report(ysym_o1["A"], ysym_o1["B"])
    ysym_face1 = face_report(ysym_o1["C"], ysym_o1["D"])
    zsym_reverse1 = reverse_report(zsym_o1["A"], zsym_o1["B"])
    zsym_face1 = face_report(zsym_o1["C"], zsym_o1["D"])
    checks.check(
        "not-y-probes-or-two-site-or-nstri-or-perp",
        X_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and X_SYMMETRIC_SEEDS != Y_SYMMETRIC_SEEDS
        and X_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and X_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and X_SYMMETRIC_SEEDS != PERP_SEEDS
        and ticks[NEG_E1] == 0
        and two_ticks.get(NEG_E1) != 0
        and probe_sites != y_probe_sites
        and y_o1["A"] != o1["A"]
        and y_reverse1 == "fail"
        and y_face1 == "fail"
        and nstri_o1["B"] != o1["B"]
        and E2 in nstri_o1["B"]
        and E2 not in o1["B"]
        and perp_o1["A"] != o1["A"]
        and E2 in perp_o1["A"]
        and E2 not in o1["A"]
        and two_o1["A"] == o1["A"]
        and ticks[NEG_E1] == 0
        and two_ticks[NEG_E1] == 1
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "not-y-symmetric-or-z-symmetric",
        ysym_o1["A"] != o1["A"]
        and ysym_o1["A"] == frozenset({E1})
        and ysym_reverse1 == "fail"
        and ysym_face1 == "fail"
        and zsym_o1["A"] == frozenset({E1})
        and zsym_reverse1 == "fail"
        and zsym_face1 == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and ticks[PROBES["A"]] == 0
        and ysym_ticks[PROBES["A"]] == 3
        and zsym_ticks[PROBES["A"]] == 3,
    )
    checks.check(
        "uniqueness-not-required",
        isinstance(o1["A"], frozenset)
        and isinstance(o1["D"], frozenset)
        and len(o1["A"]) == 3
        and len(o1["B"]) == 3
        and len(o1["C"]) == 4
        and len(o1["D"]) == 2
        and reverse1 == "hold"
        and face1 == "hold",
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
        and X_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and X_SYMMETRIC_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 3,
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
        and o0["A"] == frozenset()
        and o0["A"] != UNDEFINED
        and existential_opposite(frozenset(), o1["B"]) == UNDEFINED,
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-O-ticks",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "O(A, τ0) = {}" in note
        and "O(B, τ0) = {}" in note
        and "O(C, τ0) = {}" in note
        and "O(D, τ0) = {−e_2}" in note
        and "O(A, τ1) = {+e_1, +e_3, −e_3}" in note
        and "O(B, τ1) = {+e_1, +e_3, −e_3}" in note
        and "O(C, τ1) = {+e_2, −e_2, +e_3, −e_3}" in note
        and "O(D, τ1) = {+e_2, −e_2}" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (2, 0, 0), (1, 0, 1), (1, 0, -1)" in note
        and "new 6-NN of B at t(B)+1: (2, 1, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (1, 2, 0)" in note,
    )
    checks.check(
        "note-reports-undefined-hold-composition-fail",
        "Reverse at τ0: UNDEFINED" in note
        and "Reverse at τ1: hold" in note
        and "Face at τ0: UNDEFINED" in note
        and "Face at τ1: hold" in note
        and "Composition: fail" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-m-two-tick-or-eventual-o",
        "not leftover of nmt2zx `M` two-tick HOLD/HOLD" in normalized_note
        and "not leftover of nmoutzx eventual-`O` hold/hold" in normalized_note
        and "O is not M" in note,
    )
    checks.check(
        "note-not-two-tick-lock-count-clock",
        "not the two-tick lock-count clock composition" in normalized_note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-mixed-7188-fail-fail",
        "not leftover of mixed #7188 fail/fail" in normalized_note
        and "Reverse at τ0: UNDEFINED" in note
        and "Face at τ0: UNDEFINED" in note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ0(q)=t(q)" in note.replace(" ", "")
        and "τ1(q)=t(q)+1" in note.replace(" ", ""),
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in normalized_note
        and "B_3(0)" in note
        and "{n:n·n<=9}" in note.replace(" ", "")
        and "No runner cache is written." in normalized_note,
    )
    checks.check(
        "note-does-not-use-occupancy",
        "does not use occupancy" in normalized_note
        and "own outgoing" in normalized_note,
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
        '    "docs/X_SYMMETRIC_THREE_SITE_XPROBE_OWN_OUTGOING_SET_TWO_TICK_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
