#!/usr/bin/env python3
"""Simultaneous M and O at t+1 reverse/face on four #7214 x-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (1,0,0)} with locks +e_2 and -e_2 (x-axis opposite ±e_2; same process
and x-probes as nmxe2x #7214). A 6-NN step is allowed iff it is perpendicular
to the parent lock axis. Newly formed sites lock the incoming step. Seeds
keep their seed letters as a singleton. t(q) is formation tick. tau = t+1.
M(q, tau) is the set of earliest incoming NN steps at q using only records
with tick <= tau. Unformed at tau => UNDEFINED. O(q, tau) is the outgoing
dual of M: the set of e in {±e_1,±e_2,±e_3} such that q+e is formed in
B_3(0) and e is in M(q+e, tau). Unformed q at tau => UNDEFINED. Empty O is
empty, not UNDEFINED. Report M, O, and M ∩ O at tau. Reverse/face of M at
tau. Reverse/face of O at tau. Empty or UNDEFINED => UNDEFINED. O is not M.
Uniqueness is not required. Occupancy n is not used. Named-sign lettering
is not used. No unique P_+. No six-neighbor star as the letter. No Dijkstra.
No Gram. No larger host. Displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/X_AXIS_OPPOSITE_E2_XPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/X_AXIS_OPPOSITE_E2_XPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
BALL_SQ = 9
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
)
X_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, NEG_E2),
    (NEG_E1, NEG_E2),
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
SAME_E2_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
)
NSPAR_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E1, NEG_E1),
)
OPPOSITE_E3_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E3),
    (E1, NEG_E3),
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
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Simultaneous M and O at t+1 on the four #7214 x-probes, "
    "intersection, and reverse/face of each are reported. Displayed, not adopted."
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


def intersection_set(left: Incoming, right: Outgoing) -> Incoming:
    """M ∩ O at a cut. UNDEFINED if either side is UNDEFINED. Empty stays empty."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("intersection sides must be lock sets or UNDEFINED")
    return left & right


def eventual_outgoing_set(
    site: Point,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
) -> Outgoing:
    """nmoutx2 leftover: eventual neighbor locks, no t versus t+1 cut."""
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


def existential_opposite(left: Incoming, right: Incoming) -> str:
    """Hold iff some lock in left is the vector opposite of some lock in right."""
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


def reverse_report(set_a: Incoming, set_b: Incoming) -> str:
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    return existential_opposite(set_c, set_d)


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


def probe_maps(
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    probes: dict[str, Point],
) -> tuple[dict[str, Incoming], dict[str, Outgoing]]:
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        tau = ticks[site] + 1
        m1[name] = incoming_set(site, tau, ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau, ticks, locks, seed_map)
    return m1, o1


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("simultaneous M and O at t+1 reverse/face on #7214 x-probes")
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
        "existential-opposite-identity",
        existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset({E1}), UNDEFINED) == UNDEFINED
        and existential_opposite(frozenset(), frozenset({E3})) == UNDEFINED
        and existential_opposite(frozenset({E3}), frozenset()) == UNDEFINED
        and existential_opposite(frozenset(), frozenset()) == UNDEFINED
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(set_m_a, set_m_b) == "hold"
        and existential_opposite(set_m_c, set_m_d) == "hold"
        and existential_opposite(set_o_a, set_o_b) == "hold"
        and existential_opposite(set_o_c, set_o_d) == "hold",
    )
    checks.check(
        "intersection-identity",
        intersection_set(UNDEFINED, frozenset({E1})) == UNDEFINED
        and intersection_set(frozenset({E1}), UNDEFINED) == UNDEFINED
        and intersection_set(set_m_a, set_o_a) == frozenset()
        and intersection_set(set_m_d, set_o_d) == frozenset()
        and intersection_set(frozenset({E1}), frozenset({E1, E2})) == frozenset({E1}),
    )

    ticks, locks, seed_map = form()
    xsym_ticks, xsym_locks, xsym_seeds = form(X_SYMMETRIC_SEEDS)
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    nstri_ticks, nstri_locks, nstri_seeds = form(NSTRI_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    same_ticks, same_locks, same_seeds = form(SAME_E2_SEEDS)
    nspar_ticks, nspar_locks, nspar_seeds = form(NSPAR_SEEDS)
    e3_ticks, e3_locks, e3_seeds = form(OPPOSITE_E3_SEEDS)

    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o0: dict[str, Outgoing] = {}
    o1: dict[str, Outgoing] = {}
    inter1: dict[str, Incoming] = {}
    o_eventual: dict[str, Outgoing] = {}
    new_meet1: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o0[name] = outgoing_set(site, tau0[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        inter1[name] = intersection_set(m1[name], o1[name])
        o_eventual[name] = eventual_outgoing_set(site, ticks, locks)
        new_meet1[name] = new_records_meeting_six_nn(site, ticks, 1)
        print(
            f"{name} t={ticks[site]} tau={tau1[name]} "
            f"M={incoming_display(m1[name])} "
            f"O={outgoing_display(o1[name])} "
            f"McapO={incoming_display(inter1[name])}"
        )

    m_reverse = reverse_report(m1["A"], m1["B"])
    m_face = face_report(m1["C"], m1["D"])
    o_reverse = reverse_report(o1["A"], o1["B"])
    o_face = face_report(o1["C"], o1["D"])
    leftover_o_reverse0 = reverse_report(o0["A"], o0["B"])
    leftover_o_face0 = face_report(o0["C"], o0["D"])
    unique_m_reverse = reverse_report(unique_letter(m1["A"]), unique_letter(m1["B"]))
    unique_m_face = face_report(unique_letter(m1["C"]), unique_letter(m1["D"]))
    unique_o_reverse = reverse_report(unique_letter(o1["A"]), unique_letter(o1["B"]))
    unique_o_face = face_report(unique_letter(o1["C"]), unique_letter(o1["D"]))
    leftover_neighbor_reverse = reverse_report(
        neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"]),
        neighbor_lock_set(PROBES["B"], ticks, locks, tau1["B"]),
    )
    leftover_neighbor_face = face_report(
        neighbor_lock_set(PROBES["C"], ticks, locks, tau1["C"]),
        neighbor_lock_set(PROBES["D"], ticks, locks, tau1["D"]),
    )
    eventual_reverse = reverse_report(o_eventual["A"], o_eventual["B"])
    eventual_face = face_report(o_eventual["C"], o_eventual["D"])
    reverse_uses_singleton_m_a = (
        m_reverse == "hold"
        and m1["A"] == set_m_a
        and isinstance(m1["A"], frozenset)
        and len(m1["A"]) == 1
        and NEG_E2 in m1["A"]
        and m1["B"] == set_m_b
        and add(NEG_E2, E2) == ZERO
    )
    print(f"M_reverse={m_reverse} M_face={m_face}")
    print(f"O_reverse={o_reverse} O_face={o_face}")
    print(
        "per_element: each earliest incoming or outgoing NN step at a probe, "
        "read from the record prefix at that probe's t+1"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four M sets, four O sets, four intersections, reverse/face of each"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    xsym_m1, xsym_o1 = probe_maps(xsym_ticks, xsym_locks, xsym_seeds, PROBES)
    ysym_m1, ysym_o1 = probe_maps(ysym_ticks, ysym_locks, ysym_seeds, PROBES)
    zsym_m1, zsym_o1 = probe_maps(zsym_ticks, zsym_locks, zsym_seeds, PROBES)
    nstri_m1, nstri_o1 = probe_maps(nstri_ticks, nstri_locks, nstri_seeds, PROBES)
    perp_m1, perp_o1 = probe_maps(perp_ticks, perp_locks, perp_seeds, PROBES)
    same_m1, _same_o1 = probe_maps(same_ticks, same_locks, same_seeds, PROBES)
    nspar_m1, _nspar_o1 = probe_maps(nspar_ticks, nspar_locks, nspar_seeds, PROBES)
    e3_m1, _e3_o1 = probe_maps(e3_ticks, e3_locks, e3_seeds, PROBES)

    ysym_m_reverse = reverse_report(ysym_m1["A"], ysym_m1["B"])
    ysym_m_face = face_report(ysym_m1["C"], ysym_m1["D"])
    ysym_o_reverse = reverse_report(ysym_o1["A"], ysym_o1["B"])
    ysym_o_face = face_report(ysym_o1["C"], ysym_o1["D"])
    zsym_m_reverse = reverse_report(zsym_m1["A"], zsym_m1["B"])
    zsym_m_face = face_report(zsym_m1["C"], zsym_m1["D"])
    zsym_o_reverse = reverse_report(zsym_o1["A"], zsym_o1["B"])
    zsym_o_face = face_report(zsym_o1["C"], zsym_o1["D"])
    perp_m_reverse = reverse_report(perp_m1["A"], perp_m1["B"])
    perp_m_face = face_report(perp_m1["C"], perp_m1["D"])
    perp_o_reverse = reverse_report(perp_o1["A"], perp_o1["B"])
    perp_o_face = face_report(perp_o1["C"], perp_o1["D"])
    same_m_reverse = reverse_report(same_m1["A"], same_m1["B"])
    same_m_face = face_report(same_m1["C"], same_m1["D"])
    nspar_m_reverse = reverse_report(nspar_m1["A"], nspar_m1["B"])
    e3_m_reverse = reverse_report(e3_m1["A"], e3_m1["B"])
    e3_m_face = face_report(e3_m1["C"], e3_m1["D"])

    y_m1, y_o1 = probe_maps(ticks, locks, seed_map, Y_PROBES)
    z_m1, z_o1 = probe_maps(ticks, locks, seed_map, Z_PROBES)
    y_m_reverse = reverse_report(y_m1["A"], y_m1["B"])
    y_m_face = face_report(y_m1["C"], y_m1["D"])
    y_o_reverse = reverse_report(y_o1["A"], y_o1["B"])
    y_o_face = face_report(y_o1["C"], y_o1["D"])
    z_m_reverse = reverse_report(z_m1["A"], z_m1["B"])
    z_m_face = face_report(z_m1["C"], z_m1["D"])

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E2, NEG_E2)
    )
    seed_partner_parallel_blocked = all(
        ticks.get(add(E1, step)) != 1 for step in (E2, NEG_E2)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_partner_parallel_blocked
        and ticks[NEG_E1] == 1
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
        and incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED,
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
        and incoming_set(E1, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and m1["A"] == frozenset({NEG_E2})
        and NEG_E1 not in seed_map,
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
        m1["A"] == set_m_a
        and m1["B"] == set_m_b
        and m1["C"] == set_m_c
        and m1["D"] == set_m_d
        and m1["A"] != UNDEFINED
        and m1["D"] != UNDEFINED
        and len(m1["A"]) == 1
        and len(m1["D"]) == 3,
        str({name: incoming_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-O-at-tau",
        o1["A"] == set_o_a
        and o1["B"] == set_o_b
        and o1["C"] == set_o_c
        and o1["D"] == set_o_d
        and o1["A"] != UNDEFINED
        and o1["D"] != UNDEFINED
        and len(o1["A"]) == 3
        and len(o1["D"]) == 2,
        str({name: outgoing_display(o1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-intersection-empty",
        all(
            isinstance(inter1[name], frozenset) and inter1[name] == frozenset()
            for name in ("A", "B", "C", "D")
        )
        and all(
            isinstance(m1[name], frozenset)
            and isinstance(o1[name], frozenset)
            and m1[name].isdisjoint(o1[name])
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "theorem1-M-frozen-across-t-and-tplus1",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"]
        and m0["A"] == set_m_a
        and m0["D"] == set_m_d,
    )
    checks.check(
        "theorem1-O-not-frozen-from-t",
        o0["A"] == frozenset()
        and o0["B"] == frozenset()
        and o0["C"] == frozenset()
        and o0["D"] == frozenset({NEG_E2})
        and o1["A"] != o0["A"]
        and o1["B"] != o0["B"]
        and o1["C"] != o0["C"]
        and o1["D"] != o0["D"],
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E1
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and m1["A"] == frozenset({NEG_E2})
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        len(m1["D"]) == 3
        and unique_letter(m1["D"]) == UNDEFINED
        and m1["D"] != UNDEFINED
        and len(o1["A"]) == 3
        and unique_letter(o1["A"]) == UNDEFINED
        and o1["A"] != UNDEFINED
        and len(o1["C"]) == 4
        and unique_letter(o1["D"]) == UNDEFINED,
    )
    checks.check(
        "theorem1-new-records-meet-6nn-at-tplus1",
        new_meet1["A"] == ((2, 0, 0), (1, 0, 1), (1, 0, -1))
        and new_meet1["B"] == ((2, 1, 1), (1, 1, 2), (1, 1, 0))
        and new_meet1["C"] == ((2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new_meet1["D"] == ((1, 2, 0),)
        and PROBES["C"] in new_meet1["A"]
        and PROBES["D"] in new_meet1["B"],
        str(new_meet1),
    )
    checks.check(
        "theorem1-reverse-hold-uses-singleton-M-A",
        reverse_uses_singleton_m_a
        and unique_letter(m1["A"]) == frozenset({NEG_E2})
        and m1["A"] == set_m_a
        and m1["B"] == set_m_b,
        str((m_reverse, incoming_display(m1["A"]))),
    )
    checks.check(
        "theorem2-M-reverse-hold",
        m_reverse == "hold"
        and m1["A"] == set_m_a
        and m1["B"] == set_m_b
        and add(NEG_E2, E2) == ZERO
        and m_reverse != "fail"
        and m_reverse != UNDEFINED,
        m_reverse,
    )
    checks.check(
        "theorem2-M-face-hold",
        m_face == "hold"
        and m1["C"] == set_m_c
        and m1["D"] == set_m_d
        and add(E1, NEG_E1) == ZERO
        and m_face != "fail"
        and m_face != UNDEFINED,
        m_face,
    )
    checks.check(
        "theorem3-O-reverse-hold",
        o_reverse == "hold"
        and o1["A"] == set_o_a
        and o1["B"] == set_o_b
        and add(E3, NEG_E3) == ZERO
        and o_reverse != "fail"
        and o_reverse != UNDEFINED,
        o_reverse,
    )
    checks.check(
        "theorem3-O-face-hold",
        o_face == "hold"
        and o1["C"] == set_o_c
        and o1["D"] == set_o_d
        and add(E2, NEG_E2) == ZERO
        and o_face != "fail"
        and o_face != UNDEFINED,
        o_face,
    )
    checks.check(
        "O-is-not-M",
        isinstance(m1["A"], frozenset)
        and isinstance(o1["A"], frozenset)
        and NEG_E2 in m1["A"]
        and NEG_E2 not in o1["A"]
        and o1["A"] != m1["A"]
        and o0["A"] != m1["A"]
        and E1 in o1["A"]
        and E1 not in m1["A"],
    )
    checks.check(
        "not-unique-letter-leftover",
        unique_m_reverse == "hold"
        and unique_m_face == UNDEFINED
        and unique_o_reverse == UNDEFINED
        and unique_o_face == UNDEFINED
        and m_reverse == "hold"
        and m_face == "hold"
        and o_reverse == "hold"
        and o_face == "hold"
        and m_face != unique_m_face
        and o_reverse != unique_o_reverse,
    )
    checks.check(
        "not-leftover-of-O-at-t",
        leftover_o_reverse0 == UNDEFINED
        and leftover_o_face0 == UNDEFINED
        and o_reverse == "hold"
        and o_face == "hold"
        and leftover_o_reverse0 != o_reverse
        and leftover_o_face0 != o_face,
    )
    checks.check(
        "not-leftover-of-nmxe2x-M-only",
        m0["A"] == m1["A"]
        and m0["B"] == m1["B"]
        and m0["C"] == m1["C"]
        and m0["D"] == m1["D"]
        and reverse_report(m0["A"], m0["B"]) == "hold"
        and face_report(m0["C"], m0["D"]) == "hold"
        and o1["A"] != m1["A"]
        and inter1["A"] == frozenset(),
    )
    checks.check(
        "not-leftover-of-nmot2x2-O-two-tick",
        leftover_o_reverse0 == UNDEFINED
        and leftover_o_face0 == UNDEFINED
        and o_reverse == "hold"
        and o_face == "hold"
        and leftover_o_reverse0 != o_reverse
        and m1["A"] != o1["A"]
        and inter1["A"] == frozenset(),
    )
    checks.check(
        "not-leftover-of-eventual-O-alone",
        o_eventual["A"] == o1["A"]
        and o_eventual["B"] == o1["B"]
        and o_eventual["C"] == o1["C"]
        and o_eventual["D"] == o1["D"]
        and eventual_reverse == "hold"
        and eventual_face == "hold"
        and m1["A"] != o_eventual["A"]
        and inter1["A"] == frozenset(),
    )
    checks.check(
        "not-neighbor-lock-leftover",
        leftover_neighbor_reverse == "hold"
        and leftover_neighbor_face == "hold"
        and isinstance(o1["A"], frozenset)
        and E2 not in o1["A"]
        and E2 in neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"])
        and neighbor_lock_set(PROBES["A"], ticks, locks, tau1["A"]) != o1["A"],
    )
    checks.check(
        "not-reprint-of-nszmenu-7188",
        zsym_m1["A"] != m1["A"]
        and zsym_m1["A"] == frozenset({E2, NEG_E2})
        and zsym_m_reverse == "fail"
        and zsym_m_face == "fail"
        and zsym_o_reverse == "fail"
        and zsym_o_face == "hold"
        and m_reverse == "hold"
        and m_face == "hold"
        and ticks[PROBES["A"]] == 0
        and zsym_ticks[PROBES["A"]] == 3,
    )
    checks.check(
        "not-y-probes-or-three-site-or-nstri-or-perp",
        TWO_SITE_SEEDS != X_SYMMETRIC_SEEDS
        and TWO_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_SITE_SEEDS != NSTRI_SEEDS
        and TWO_SITE_SEEDS != PERP_SEEDS
        and ticks[NEG_E1] == 1
        and xsym_ticks[NEG_E1] == 0
        and sum(time == 0 for time in ticks.values()) == 2
        and sum(time == 0 for time in xsym_ticks.values()) == 3
        and probe_sites != y_probe_sites
        and y_m1["A"] != m1["A"]
        and y_m_reverse == "fail"
        and y_m_face == "fail"
        and y_o_reverse == "fail"
        and y_o_face == "fail"
        and z_m_reverse == "fail"
        and z_m_face == "fail"
        and nstri_m1["B"] != m1["B"]
        and E1 in nstri_m1["B"]
        and E1 not in m1["B"]
        and nstri_o1["D"] != o1["D"]
        and perp_m1["A"] != m1["A"]
        and perp_m_reverse == "fail"
        and perp_m_face == "hold"
        and perp_o_reverse == "hold"
        and perp_o_face == "hold"
        and ysym_m_reverse == "fail"
        and ysym_m_face == "fail"
        and ysym_o_reverse == "fail"
        and ysym_o_face == "fail"
        and m_reverse == "hold"
        and o_reverse == "hold",
    )
    checks.check(
        "not-same-lock-or-nspar-or-opposite-e3",
        TWO_SITE_SEEDS != SAME_E2_SEEDS
        and TWO_SITE_SEEDS != NSPAR_SEEDS
        and TWO_SITE_SEEDS != OPPOSITE_E3_SEEDS
        and same_m_reverse == "fail"
        and same_m_face == "hold"
        and nspar_m_reverse == "fail"
        and e3_m_reverse == "hold"
        and e3_m_face == "fail"
        and m_reverse == "hold"
        and m_face == "hold",
    )
    checks.check(
        "not-nnlock-named-sign",
        m1["A"] == frozenset({NEG_E2})
        and named_sign(NEG_E2) == "-"
        and named_sign(E2) == "+"
        and m1["C"] == frozenset({E1})
        and named_sign(E1) == "+"
        and m1["A"] != named_sign(NEG_E2)
        and o1["A"] != named_sign(E1),
    )
    checks.check(
        "incoming-outgoing-locks-are-nn-steps",
        all(m1[name] <= set(NN) for name in ("A", "B", "C", "D"))
        and all(o1[name] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 1
        and len(m1["B"]) == 1
        and len(m1["C"]) == 1
        and len(m1["D"]) == 3
        and len(o1["A"]) == 3
        and len(o1["D"]) == 2
        and m_reverse == "hold"
        and m_face == "hold"
        and o_reverse == "hold"
        and o_face == "hold",
    )
    checks.check(
        "x-axis-opposite-e2-two-site-seed",
        ticks[ORIGIN] == 0
        and locks[ORIGIN] == {E2}
        and ticks[E1] == 0
        and locks[E1] == {NEG_E2}
        and add(E2, NEG_E2) == ZERO
        and NEG_E1 not in seed_map
        and ticks[NEG_E1] != 0
        and sum(time == 0 for time in ticks.values()) == 2,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check(
        "mutation-empty-or-undefined-is-undefined",
        reverse_report(frozenset(), m1["B"]) == UNDEFINED
        and face_report(m1["C"], frozenset()) == UNDEFINED
        and reverse_report(UNDEFINED, o1["B"]) == UNDEFINED
        and face_report(o1["C"], UNDEFINED) == UNDEFINED
        and leftover_o_reverse0 == UNDEFINED,
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E2})) == "fail"
        and m_reverse == "hold"
        and o_reverse == "hold",
    )
    checks.check(
        "mutation-unique-letter-O-undefined",
        unique_o_reverse == UNDEFINED
        and unique_o_face == UNDEFINED
        and unique_m_face == UNDEFINED
        and m_face == "hold"
        and o_reverse == "hold"
        and o_face == "hold",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        sum_of_set(m1["A"]) == NEG_E2
        and sum_of_set(m1["B"]) == E2
        and sum_of_set(m1["C"]) == E1
        and sum_of_set(m1["D"]) == NEG_E1
        and sum_of_set(o1["A"]) == E1
        and sum_of_set(o1["B"]) == E1
        and sum_of_set(o1["C"]) == ZERO
        and sum_of_set(o1["D"]) == ZERO
        and m1["D"] != frozenset({NEG_E1})
        and o1["A"] != frozenset({E1})
        and len(m1["D"]) == 3
        and len(o1["A"]) == 3,
    )
    checks.check(
        "face-pair-M-not-O-pair",
        add(E1, NEG_E1) == ZERO
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and E1 in m1["C"]
        and NEG_E1 in m1["D"]
        and E2 in o1["C"]
        and NEG_E2 in o1["D"]
        and E2 not in m1["C"]
        and E1 not in o1["C"],
    )

    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-O-intersection",
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
        and "(M ∩ O)(A, τ) = {}" in note
        and "(M ∩ O)(B, τ) = {}" in note
        and "(M ∩ O)(C, τ) = {}" in note
        and "(M ∩ O)(D, τ) = {}" in note,
    )
    checks.check(
        "note-reports-hold-hold-hold-hold",
        "Reverse from M: hold" in note
        and "Face from M: hold" in note
        and "Reverse from O: hold" in note
        and "Face from O: hold" in note
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
        and "O is not M" in note
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
        "note-not-unique-or-sum-or-star-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "not leftover of nmxe2x M-only" in normalized_note
        and "not leftover of O at t" in normalized_note
        and "Reverse from M holds." in note
        and "Face from O holds." in note,
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
        '    "docs/X_AXIS_OPPOSITE_E2_XPROBE_SIMULTANEOUS_INCOMING_OUTGOING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "existential_opposite" in defined_fns
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
