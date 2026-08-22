#!/usr/bin/env python3
"""Incoming-axis agreement of M at t+1 reverse/face.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is {0, (0,1,0), (0,-1,0)} with locks +e_1, -e_1, and -e_1 (nsyopp #7132;
same process and y-probes as nmsyop #7211). A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q, tau) is the set of
earliest incoming nearest-neighbor steps at q using only records with tick
<= tau. Unformed at tau => UNDEFINED. Axis(M) is the unsigned lattice
directions of signed locks in M. Empty Axis is empty, not UNDEFINED.
Reverse HOLDs iff Axis(M)(A) equals Axis(M)(B) as sets and both nonempty.
Face likewise on C, D. Empty Axis => fail, not UNDEFINED. Uniqueness of
incoming locks is not required. Occupancy of sites is not used. Named-sign
lettering is not used. No larger host. Not leftover of #7211 exist-opposite
of signed M. Not leftover of leftover-of-M alone. Not leftover of leftover
of M and outgoing dual. Not leftover of two-site incoming-axis agreement
as this member.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/Y_SYMMETRIC_THREE_SITE_INCOMING_AXIS_AGREEMENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/Y_SYMMETRIC_THREE_SITE_INCOMING_AXIS_AGREEMENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Incoming-axis agreement of M at t+1 on the four #7211 y-probes, "
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
    """Outgoing dual of M. Contrast only; not this letter."""
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


def leftover_of_one(value: Incoming) -> AxisSet:
    """One-sided leftover contrast: {e_1,e_2,e_3} minus Axis(S). Not this letter."""
    occupied = axis_set(value)
    if occupied == UNDEFINED:
        return UNDEFINED
    if not isinstance(occupied, frozenset):
        raise TypeError("one-sided leftover needs an axis set")
    return frozenset(AXES) - occupied


def leftover_of_union(incoming: Incoming, outgoing: Outgoing) -> AxisSet:
    """Leftover of Axis(M) union Axis(O). Contrast only."""
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if axes_m == UNDEFINED or axes_o == UNDEFINED:
        return UNDEFINED
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    return frozenset(AXES) - (axes_m | axes_o)


def axis_agreement(left: AxisSet, right: AxisSet) -> str:
    """HOLD iff defined, equal, and nonempty. Empty Axis => fail, not UNDEFINED."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise TypeError("axis sides must be axis sets or UNDEFINED")
    if not left or not right:
        return "fail"
    if left == right:
        return "hold"
    return "fail"


def reverse_report(set_a: AxisSet, set_b: AxisSet) -> str:
    """Reverse HOLDs iff Axis(M)(A) equals Axis(M)(B) nonempty."""
    return axis_agreement(set_a, set_b)


def face_report(set_c: AxisSet, set_d: AxisSet) -> str:
    """Face HOLDs iff Axis(M)(C) equals Axis(M)(D) nonempty."""
    return axis_agreement(set_c, set_d)


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


def named_sign(lock: Point) -> str:
    if lock in (E1, E2, E3):
        return "+"
    if lock in (NEG_E1, NEG_E2, NEG_E3):
        return "-"
    raise ValueError(f"lock is not a six-neighbor step: {lock!r}")


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


def snapshot(
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
    probes: dict[str, Point],
) -> tuple[dict[str, Incoming], dict[str, AxisSet]]:
    incoming: dict[str, Incoming] = {}
    axes: dict[str, AxisSet] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        tau = ticks[site] + 1
        incoming[name] = incoming_set(site, tau, ticks, locks, seed_map)
        axes[name] = axis_set(incoming[name])
    return incoming, axes


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

    print("incoming-axis agreement of M reverse/face at t+1")
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and not in_ball((4, 0, 0)),
    )
    checks.check(
        "axis-identity",
        axis_set(UNDEFINED) == UNDEFINED
        and axis_set(frozenset({NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E1, NEG_E1})) == frozenset({E1})
        and axis_set(frozenset({E2, E3, NEG_E3})) == frozenset({E2, E3})
        and axis_set(frozenset()) == frozenset(),
    )
    checks.check(
        "axis-agreement-identity",
        axis_agreement(UNDEFINED, frozenset({E1})) == UNDEFINED
        and axis_agreement(frozenset({E1}), UNDEFINED) == UNDEFINED
        and axis_agreement(frozenset(), frozenset()) == "fail"
        and axis_agreement(frozenset(), frozenset({E1})) == "fail"
        and axis_agreement(frozenset({E1}), frozenset()) == "fail"
        and axis_agreement(frozenset({E1}), frozenset({E1})) == "hold"
        and axis_agreement(frozenset({E1}), frozenset({E2})) == "fail"
        and axis_agreement(frozenset({E2}), frozenset({E2, E3})) == "fail"
        and axis_agreement(frozenset({E2, E3}), frozenset({E2, E3})) == "hold",
    )

    ticks, locks, seed_map = form()
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    twosite_ticks, twosite_locks, twosite_seeds = form(TWO_SITE_SEEDS)
    nstri_ticks, nstri_locks, nstri_seeds = form(NSTRI_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o1: dict[str, Outgoing] = {}
    axis_m: dict[str, AxisSet] = {}
    lx_m: dict[str, AxisSet] = {}
    lx_union: dict[str, AxisSet] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        axis_m[name] = axis_set(m1[name])
        lx_m[name] = leftover_of_one(m1[name])
        lx_union[name] = leftover_of_union(m1[name], o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"Axis(M)={axis_display(axis_m[name])}"
        )

    reverse = reverse_report(axis_m["A"], axis_m["B"])
    face = face_report(axis_m["C"], axis_m["D"])
    reverse_m_alone = reverse_report(lx_m["A"], lx_m["B"])
    face_m_alone = face_report(lx_m["C"], lx_m["D"])
    reverse_union = reverse_report(lx_union["A"], lx_union["B"])
    face_union = face_report(lx_union["C"], lx_union["D"])
    m_exist_reverse = existential_opposite(m1["A"], m1["B"])
    m_exist_face = existential_opposite(m1["C"], m1["D"])
    unique_reverse = reverse_report(
        axis_set(unique_letter(m1["A"])),
        axis_set(unique_letter(m1["B"])),
    )
    unique_face = face_report(
        axis_set(unique_letter(m1["C"])),
        axis_set(unique_letter(m1["D"])),
    )
    print(f"incoming-axis reverse={reverse} face={face}")
    print(
        "per_element: each unsigned occupied lattice axis among {e_1,e_2,e_3} "
        "of M at a probe's t+1"
    )
    print(
        "per_site: scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four Axis(M) sets, reverse/face from incoming-axis agreement")
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
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 2
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 3
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 1, ticks, locks, seed_map) == UNDEFINED
        and axis_set(incoming_set(PROBES["B"], 1, ticks, locks, seed_map)) == UNDEFINED
        and incoming_set(PROBES["D"], 2, ticks, locks, seed_map) == UNDEFINED
        and reverse_report(UNDEFINED, frozenset({E1})) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and incoming_set(NEG_E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and m1["A"] == frozenset({NEG_E1}),
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
        "theorem1-Axis-M",
        axis_m["A"] == frozenset({E1})
        and axis_m["B"] == frozenset({E1})
        and axis_m["C"] == frozenset({E2})
        and axis_m["D"] == frozenset({E2, E3}),
        str({name: axis_display(axis_m[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
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
        "theorem1-mixed-stays-a-set",
        isinstance(m1["D"], frozenset)
        and len(m1["D"]) == 3
        and unique_letter(m1["D"]) == UNDEFINED
        and axis_m["D"] == frozenset({E2, E3})
        and axis_m["D"] != UNDEFINED
        and E3 in axis_m["D"],
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E2
        and ticks[E2] == 0
        and locks[E2] == {NEG_E1}
        and m1["A"] == frozenset({NEG_E1})
        and axis_m["A"] == frozenset({E1}),
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse == "hold"
        and axis_m["A"] == frozenset({E1})
        and axis_m["B"] == frozenset({E1})
        and reverse != "fail"
        and reverse != UNDEFINED,
        reverse,
    )
    checks.check(
        "theorem3-face-fail",
        face == "fail"
        and axis_m["C"] == frozenset({E2})
        and axis_m["D"] == frozenset({E2, E3})
        and face != "hold"
        and face != UNDEFINED,
        face,
    )
    checks.check(
        "mutation-leftover-of-M-alone-differs",
        lx_m["A"] == frozenset({E2, E3})
        and lx_m["B"] == frozenset({E2, E3})
        and lx_m["C"] == frozenset({E1, E3})
        and lx_m["D"] == frozenset({E1})
        and reverse_m_alone == "hold"
        and face_m_alone == "fail"
        and lx_m["A"] != axis_m["A"]
        and lx_m["C"] != axis_m["C"],
    )
    checks.check(
        "mutation-leftover-of-union-differs",
        lx_union["A"] == frozenset()
        and lx_union["B"] == frozenset()
        and lx_union["C"] == frozenset()
        and lx_union["D"] == frozenset()
        and reverse_union == "fail"
        and face_union == "fail"
        and reverse == "hold"
        and face == "fail",
    )
    checks.check(
        "mutation-exist-opposite-HOLD-differs",
        m_exist_reverse == "hold"
        and m_exist_face == "hold"
        and reverse == "hold"
        and face == "fail"
        and face != m_exist_face,
    )
    checks.check(
        "mutation-unique-letter-undefined-at-mixed-D",
        unique_letter(m1["A"]) == frozenset({NEG_E1})
        and unique_letter(m1["D"]) == UNDEFINED
        and unique_reverse == "hold"
        and unique_face == UNDEFINED
        and face == "fail"
        and face != unique_face,
    )
    checks.check(
        "mutation-empty-plus-undefined",
        axis_agreement(frozenset(), frozenset({E1})) == "fail"
        and axis_agreement(UNDEFINED, frozenset({E1})) == UNDEFINED
        and reverse == "hold"
        and face == "fail",
    )
    checks.check(
        "mutation-sum-cancels-mixed",
        isinstance(m1["D"], frozenset)
        and sum_of_set(m1["A"]) == NEG_E1
        and sum_of_set(m1["D"]) == NEG_E2
        and axis_m["D"] != frozenset({E2})
        and axis_m["D"] == frozenset({E2, E3}),
    )
    checks.check(
        "not-nnlock-named-sign",
        named_sign(NEG_E1) == "-"
        and named_sign(E1) == "+"
        and named_sign(E2) == "+"
        and axis_m["A"] != named_sign(NEG_E1)
        and axis_m["C"] != named_sign(E2),
    )
    twosite_m1, twosite_axis = snapshot(
        twosite_ticks, twosite_locks, twosite_seeds, PROBES
    )
    nstri_m1, nstri_axis = snapshot(nstri_ticks, nstri_locks, nstri_seeds, PROBES)
    x_m1, x_axis = snapshot(ticks, locks, seed_map, X_PROBES)
    perp_m1, perp_axis = snapshot(perp_ticks, perp_locks, perp_seeds, PROBES)
    zsym_m1, zsym_axis = snapshot(zsym_ticks, zsym_locks, zsym_seeds, PROBES)
    x_reverse = reverse_report(x_axis["A"], x_axis["B"])
    x_face = face_report(x_axis["C"], x_axis["D"])
    checks.check(
        "not-x-probes-or-z-symmetric-or-perp",
        Y_SYMMETRIC_SEEDS != PERP_SEEDS
        and Y_SYMMETRIC_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and x_m1["A"] != m1["A"]
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and x_axis["A"] != axis_m["A"]
        and reverse == "hold"
        and face == "fail",
    )
    checks.check(
        "y-symmetric-three-site-seed",
        Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and Y_SYMMETRIC_SEEDS != NSTRI_SEEDS
        and sum(time == 0 for time in ticks.values()) == 3
        and sum(time == 0 for time in twosite_ticks.values()) == 2
        and ticks[NEG_E2] == 0
        and twosite_ticks[NEG_E2] == 1
        and locks[ORIGIN] == {E1}
        and locks[E2] == {NEG_E1}
        and locks[NEG_E2] == {NEG_E1},
    )
    checks.check(
        "not-two-site-axis-as-this-member",
        Y_SYMMETRIC_SEEDS != TWO_SITE_SEEDS
        and twosite_m1["A"] == m1["A"]
        and twosite_axis["A"] == axis_m["A"]
        and twosite_axis["D"] == axis_m["D"]
        and ticks[NEG_E2] != twosite_ticks[NEG_E2]
        and nstri_m1["B"] != m1["B"]
        and E2 in nstri_m1["B"],
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 1
        and len(m1["B"]) == 1
        and len(m1["C"]) == 1
        and len(m1["D"]) == 3
        and reverse == "hold"
        and face == "fail",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-M-Axis",
        "t(A)=0" in note
        and "t(B)=2" in note
        and "t(C)=1" in note
        and "t(D)=3" in note
        and "M(A, τ) = {−e_1}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_2}" in note
        and "M(D, τ) = {−e_2, +e_3, −e_3}" in note
        and "Axis(M)(A, τ) = {e_1}" in note
        and "Axis(M)(B, τ) = {e_1}" in note
        and "Axis(M)(C, τ) = {e_2}" in note
        and "Axis(M)(D, τ) = {e_2, e_3}" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)"
        in note
        and "new 6-NN of D at t(D)+1: (2, 1, 0)" in note,
    )
    checks.check(
        "note-reports-hold-fail",
        "Reverse incoming-axis at τ: hold" in note
        and "Face incoming-axis at τ: fail" in note
        and "Reverse holds." in note
        and "Face fails." in note,
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
        and "Occupancy of sites is not used." in note,
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
        "note-not-exist-opposite-or-leftover-M",
        "not leftover of #7211 exist-opposite of signed" in normalized_note
        and "not leftover of leftover-of-`M` alone" in normalized_note
        and "not leftover of leftover of `M` and outgoing dual" in normalized_note
        and "Face fails." in note
        and "Reverse holds." in note,
    )
    checks.check(
        "note-not-two-site-member",
        "not leftover of two-site incoming-axis agreement #7167 as this member"
        in normalized_note
        and "y-mirror is tick 0" in normalized_note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "does not use a six-neighbor star" in normalized_note
        and "A six-neighbor star is not the letter." in note,
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
        '    "docs/Y_SYMMETRIC_THREE_SITE_INCOMING_AXIS_AGREEMENT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "identity-gates-present",
        "def incoming_set(" in source
        and "def axis_set(" in source
        and "def axis_agreement(" in source
        and "def reverse_report(" in source
        and "def face_report(" in source
        and "def form(" in source,
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 0
        and set(ticks) <= host,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "source-letter-from-incoming-axis-agreement",
        "incoming_set" in defined_fns
        and "axis_set" in defined_fns
        and "axis_agreement" in defined_fns
        and "unique_vector_letter" not in defined_fns
        and "sum_letter" not in defined_fns
        and not any("occup" in name for name in defined_fns)
        and "inner_product" not in defined_fns,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
