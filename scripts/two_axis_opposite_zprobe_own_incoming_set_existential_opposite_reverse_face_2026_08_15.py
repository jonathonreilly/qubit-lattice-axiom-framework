#!/usr/bin/env python3
"""Own incoming set exist-opposite reverse/face on two-axis opposite z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. The second pair is a new seed, not
a formed child of nsopp leftover. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Seeds keep their seed letters as a singleton. M(q, tau) is the set of
earliest incoming nearest-neighbor steps at q using only records with tick
<= tau. Unformed at tau => UNDEFINED. Reverse HOLDs iff some a in M(A, tau)
and some b in M(B, tau) have a+b=(0,0,0). Face likewise on C, D. Empty or
UNDEFINED on either side is UNDEFINED; nonempty with no opposite pair fails.
Same z-probes as nm2axz HOLDING-cover. Compare to 1-axis HOLDING M and to
y-probe signed-M. Uniqueness is not required. Occupancy of sites is not
used. Named-sign lettering is not used. No larger host. Not leftover of
unique-L. Not leftover of axis-cover. Not leftover of timed O.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_ZPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_ZPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
Incoming = frozenset[Point] | str
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
POSITIVE_LOCKS = frozenset({E1, E2, E3})
NEGATIVE_LOCKS = frozenset({NEG_E1, NEG_E2, NEG_E3})
AXES: tuple[Point, ...] = (E1, E2, E3)
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
    "Reverse and face from the own incoming *set* at t+1 on the "
    "four z-probes of the two-axis opposite seed are reported. "
    "Displayed, not adopted."
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


def set_display(locks: Incoming) -> str:
    if locks == UNDEFINED:
        return UNDEFINED
    if not isinstance(locks, frozenset):
        raise TypeError(f"lock set is not a lock set: {locks!r}")
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


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
) -> Incoming:
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


def axis_set(value: Incoming) -> Incoming:
    """Unsigned lattice axes occupied by signed locks. Contrast only."""
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


def axis_cover(incoming: Incoming, outgoing: Incoming) -> str:
    """HOLD iff axes disjoint and union is {e_1,e_2,e_3}. Contrast only."""
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
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
    """Reverse iff some a in M(A, tau) and some b in M(B, tau) have a+b=(0,0,0)."""
    return existential_opposite(set_a, set_b)


def face_report(set_c: Incoming, set_d: Incoming) -> str:
    """Face iff some c in M(C, tau) and some d in M(D, tau) have c+d=(0,0,0)."""
    return existential_opposite(set_c, set_d)


def unique_letter(value: Incoming) -> Incoming:
    """Unique-L leftover: UNDEFINED when mixed. Not this letter."""
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


def probe_incoming(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, Incoming]:
    out: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = incoming_set(
            site, site_ticks[site] + 1, site_ticks, site_locks, site_seeds
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

    print("two-axis opposite seed own incoming set exist-opposite reverse/face at t+1 on z-probes")
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
        and probe_sites != x_probe_sites
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
        and add(E3, E2) == Q_SEED
        and add(E2, E3) == Q_SEED
        and add(E2, E1) != ZERO
        and dot(E1, E2) == 0
        and perpendicular(E1, E2)
        and not perpendicular(E1, E1)
        and in_ball(PROBES["C"])
        and in_ball(Q_SEED)
        and not in_ball((4, 0, 0)),
    )
    set_a = frozenset({E2})
    set_b = frozenset({E1})
    set_c = frozenset({E3})
    set_d = frozenset({E1})
    one_set_c = frozenset({E1, NEG_E1, E2})
    checks.check(
        "existential-opposite-identity",
        existential_opposite(UNDEFINED, frozenset({E1})) == UNDEFINED
        and existential_opposite(frozenset({E1}), UNDEFINED) == UNDEFINED
        and existential_opposite(frozenset(), frozenset({E3})) == UNDEFINED
        and existential_opposite(frozenset({E3}), frozenset()) == UNDEFINED
        and existential_opposite(frozenset(), frozenset()) == UNDEFINED
        and existential_opposite(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and existential_opposite(set_a, set_b) == "fail"
        and existential_opposite(set_c, set_d) == "fail"
        and existential_opposite(one_set_c, set_d) == "hold"
        and existential_opposite(frozenset({NEG_E1}), frozenset({E1})) == "hold",
    )
    checks.check(
        "own-incoming-set-identity",
        unique_letter(frozenset({E2})) == frozenset({E2})
        and unique_letter(frozenset({E2, NEG_E2})) == UNDEFINED
        and unique_letter(one_set_c) == UNDEFINED
        and unique_letter(frozenset()) == UNDEFINED
        and unique_letter(UNDEFINED) == UNDEFINED,
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, ysym_locks, ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    tau0: dict[str, int] = {}
    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    o1: dict[str, Incoming] = {}
    cover: dict[str, str] = {}
    new_meet: dict[str, tuple[Point, ...]] = {}
    one_m1: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0[name] = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0[name], ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        o1[name] = outgoing_set(site, tau1[name], ticks, locks, seed_map)
        cover[name] = axis_cover(m1[name], o1[name])
        new_meet[name] = new_records_meeting_six_nn(site, ticks)
        one_m1[name] = incoming_set(
            site, one_ticks[site] + 1, one_ticks, one_locks, one_seeds
        )
        print(f"{name} t={ticks[site]} M={set_display(m1[name])}")

    reverse = reverse_report(m1["A"], m1["B"])
    face = face_report(m1["C"], m1["D"])
    unique_reverse = reverse_report(unique_letter(m1["A"]), unique_letter(m1["B"]))
    unique_face = face_report(unique_letter(m1["C"]), unique_letter(m1["D"]))
    cover_reverse = pair_cover(cover["A"], cover["B"])
    cover_face = pair_cover(cover["C"], cover["D"])
    o_exist_reverse = existential_opposite(o1["A"], o1["B"])
    o_exist_face = existential_opposite(o1["C"], o1["D"])
    one_reverse = reverse_report(one_m1["A"], one_m1["B"])
    one_face = face_report(one_m1["C"], one_m1["D"])
    neighbor_a = neighbor_lock_set(PROBES["A"], ticks, locks, ticks[PROBES["A"]])
    neighbor_b = neighbor_lock_set(PROBES["B"], ticks, locks, ticks[PROBES["B"]])
    neighbor_reverse = existential_opposite(neighbor_a, neighbor_b)
    y_m1 = probe_incoming(Y_PROBES, ticks, locks, seed_map)
    x_m1 = probe_incoming(X_PROBES, ticks, locks, seed_map)
    y_reverse = reverse_report(y_m1["A"], y_m1["B"])
    y_face = face_report(y_m1["C"], y_m1["D"])
    x_reverse = reverse_report(x_m1["A"], x_m1["B"])
    x_face = face_report(x_m1["C"], x_m1["D"])
    print(f"exist-opposite reverse={reverse} face={face}")
    print(
        f"1-axis HOLDING M reverse={one_reverse} face={one_face} "
        f"t={{{', '.join(str(one_ticks[PROBES[n]]) for n in ('A', 'B', 'C', 'D'))}}}"
    )
    print(f"cover reverse={cover_reverse} face={cover_face}")
    print(f"timed-O reverse={o_exist_reverse} face={o_exist_face}")
    print(
        "per_element: each lock vector in the probe's own incoming set M(q, t+1)"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four incoming sets plus reverse/face as hold, fail, or UNDEFINED"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_a_parallel_blocked = ticks.get(add(E3, NEG_E2)) != 1
    second_pair_parallel_blocked = all(
        ticks.get(add(E3, step)) != 1 for step in (E2, NEG_E2)
    ) and all(ticks.get(add(Q_SEED, step)) != 1 for step in (E2, NEG_E2))
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_a_parallel_blocked
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
        and reverse_report(
            incoming_set(PROBES["B"], 0, ticks, locks, seed_map),
            m1["B"],
        )
        == UNDEFINED
        and incoming_set(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and incoming_set(PROBES["D"], 0, ticks, locks, seed_map) == UNDEFINED
        and face_report(
            incoming_set(PROBES["C"], 0, ticks, locks, seed_map),
            m1["D"],
        )
        == UNDEFINED,
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
        "theorem1-M-at-tau",
        m1["A"] == set_a
        and m1["B"] == set_b
        and m1["C"] == set_c
        and m1["D"] == set_d
        and m1["A"] != UNDEFINED
        and m1["D"] != UNDEFINED
        and len(m1["A"]) == 1
        and len(m1["D"]) == 1,
        str({name: set_display(m1[name]) for name in ("A", "B", "C", "D")}),
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
        new_meet["A"] == ((1, 0, 1), (-1, 0, 1), (0, 0, 2))
        and new_meet["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new_meet["C"] == ((1, 0, 2), (-1, 0, 2), (0, -1, 2))
        and new_meet["D"] == ((1, -1, 1), (1, 0, 2), (1, 0, 0)),
        str(new_meet),
    )
    checks.check(
        "theorem1-mixed-remains-a-set",
        isinstance(m1["A"], frozenset)
        and isinstance(m1["C"], frozenset)
        and unique_letter(m1["C"]) == frozenset({E3})
        and unique_letter(one_m1["C"]) == UNDEFINED
        and isinstance(one_m1["C"], frozenset)
        and len(one_m1["C"]) == 3,
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
        "theorem1-reverse-fail-uses-singleton-M-A",
        reverse == "fail"
        and m1["A"] == set_a
        and isinstance(m1["A"], frozenset)
        and len(m1["A"]) == 1
        and E2 in m1["A"]
        and m1["B"] == set_b
        and add(E2, E1) != ZERO,
    )
    checks.check(
        "theorem1-compare-1-axis-HOLDING-M",
        one_ticks[PROBES["A"]] == 1
        and one_ticks[PROBES["B"]] == 2
        and one_ticks[PROBES["C"]] == 4
        and one_ticks[PROBES["D"]] == 2
        and one_m1["A"] == frozenset({E3})
        and one_m1["B"] == set_b
        and one_m1["C"] == one_set_c
        and one_m1["D"] == set_d
        and one_reverse == "fail"
        and one_face == "hold"
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["C"]] == 1
        and m1["C"] != one_m1["C"]
        and face != one_face,
    )
    checks.check(
        "theorem2-reverse-exist-opposite-fail",
        reverse == "fail"
        and m1["A"] == set_a
        and m1["B"] == set_b
        and add(E2, E1) != ZERO
        and reverse != UNDEFINED
        and reverse != "hold",
    )
    checks.check(
        "theorem3-face-exist-opposite-fail",
        face == "fail"
        and m1["C"] == set_c
        and m1["D"] == set_d
        and add(E3, E1) != ZERO
        and face != UNDEFINED
        and face != "hold",
    )
    checks.check(
        "discriminator-vs-1-axis-HOLDING-M",
        reverse == "fail"
        and face == "fail"
        and one_reverse == "fail"
        and one_face == "hold"
        and face != one_face
        and m1["C"] == frozenset({E3})
        and one_m1["C"] == one_set_c,
    )
    checks.check(
        "not-unique-L-leftover",
        unique_reverse == "fail"
        and unique_face == "fail"
        and reverse == unique_reverse
        and face == unique_face
        and unique_letter(m1["A"]) == frozenset({E2})
        and unique_letter(m1["C"]) == frozenset({E3})
        and unique_letter(one_m1["C"]) == UNDEFINED
        and one_face != unique_face,
    )
    checks.check(
        "not-axis-cover-leftover",
        cover["A"] == "hold"
        and cover["B"] == "hold"
        and cover["C"] == "hold"
        and cover["D"] == "hold"
        and cover_reverse == "hold"
        and cover_face == "hold"
        and reverse != cover_reverse
        and face != cover_face
        and axis_cover(m1["A"], m1["B"]) == "fail",
    )
    checks.check(
        "not-timed-O-exist-opposite",
        o_exist_reverse == "hold"
        and o_exist_face == "fail"
        and reverse == "fail"
        and face == "fail"
        and o_exist_reverse != reverse
        and o1["A"] != m1["A"],
    )
    checks.check(
        "not-six-neighbor-lock-union",
        neighbor_reverse == "fail"
        and reverse == "fail"
        and E1 in neighbor_a
        and NEG_E2 in neighbor_a
        and E1 not in m1["A"]
        and E2 in m1["A"]
        and neighbor_a != m1["A"],
    )
    perp_m1 = probe_incoming(PROBES, perp_ticks, perp_locks, perp_seeds)
    zsym_m1 = probe_incoming(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    ysym_ticks_count0 = sum(time == 0 for time in ysym_ticks.values())
    perp_reverse = reverse_report(perp_m1["A"], perp_m1["B"])
    perp_face = face_report(perp_m1["C"], perp_m1["D"])
    zsym_reverse = reverse_report(zsym_m1["A"], zsym_m1["B"])
    zsym_face = face_report(zsym_m1["C"], zsym_m1["D"])
    checks.check(
        "not-x-probes-or-y-probes-or-perp",
        TWO_AXIS_SEEDS != PERP_SEEDS
        and TWO_AXIS_SEEDS != Z_SYMMETRIC_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and x_m1["A"] != m1["A"]
        and y_m1["A"] != m1["A"]
        and zsym_m1["A"] != m1["A"]
        and perp_m1["A"] != m1["A"]
        and x_reverse == "fail"
        and x_face == "fail"
        and y_reverse == "hold"
        and y_face == "fail"
        and perp_reverse == "fail"
        and perp_face == "hold"
        and zsym_reverse == "hold"
        and zsym_face == "hold"
        and reverse == "fail"
        and face == "fail"
        and y_reverse != reverse
        and perp_face != face
        and zsym_reverse != reverse,
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
        m1["A"] == frozenset({E2})
        and named_sign(E2) == "+"
        and named_sign(E1) == "+"
        and m1["C"] == frozenset({E3})
        and named_sign(E3) == "+"
        and m1["A"] != named_sign(E2)
        and m1["C"] != named_sign(E3),
    )
    checks.check(
        "incoming-locks-are-nn-steps",
        all(isinstance(m1[name], frozenset) and m1[name] <= set(NN) for name in ("A", "B", "C", "D")),
    )
    checks.check(
        "uniqueness-not-required",
        len(m1["A"]) == 1
        and len(m1["B"]) == 1
        and len(m1["C"]) == 1
        and len(m1["D"]) == 1
        and reverse == "fail"
        and face == "fail"
        and unique_letter(one_m1["C"]) == UNDEFINED,
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
        and reverse_report(UNDEFINED, m1["B"]) == UNDEFINED
        and face_report(m1["C"], UNDEFINED) == UNDEFINED,
    )
    checks.check(
        "mutation-no-opposite-pair-fails",
        reverse_report(frozenset({E1}), frozenset({E1, E3})) == "fail"
        and reverse_report(set_a, set_b) == "fail"
        and reverse_report(set_c, set_d) == "fail"
        and reverse == "fail"
        and face == "fail",
    )
    checks.check(
        "mutation-sum-is-not-the-letter",
        isinstance(m1["A"], frozenset)
        and isinstance(m1["D"], frozenset)
        and sum_of_set(m1["A"]) == E2
        and sum_of_set(m1["B"]) == E1
        and sum_of_set(m1["C"]) == E3
        and sum_of_set(m1["D"]) == E1
        and add(E2, E1) != ZERO
        and add(E3, E1) != ZERO
        and reverse == "fail"
        and face == "fail",
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-ticks-and-incoming-sets",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=1" in note
        and "M(A, τ) = {+e_2}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_3}" in note
        and "M(D, τ) = {+e_1}" in note,
    )
    checks.check(
        "note-reports-new-neighbors",
        "new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)" in note
        and "new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)" in note
        and "new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)"
        in note
        and "new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)" in note,
    )
    checks.check(
        "note-reports-exist-opposite-reverse-face",
        "Reverse exist-opposite at τ: fail" in note
        and "Face exist-opposite at τ: fail" in note
        and "Reverse fails." in note
        and "Face fails." in note,
    )
    checks.check(
        "note-compares-1-axis-HOLDING-M",
        "Compare to 1-axis HOLDING M" in note
        and "1-axis face hold" in normalized_note
        and "two-axis seed advances" in normalized_note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
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
        "note-not-unique-or-sum-or-cover-leftover",
        "not a unique lock-vector leftover" in normalized_note
        and "not a sum leftover" in normalized_note
        and "does not sum" in normalized_note
        and "not leftover of unique-L" in normalized_note
        and "not leftover of nm2axz axis-cover" in normalized_note
        and "not leftover of timed `O` exist-opposite" in normalized_note,
    )
    checks.check(
        "note-no-six-neighbor-star-as-letter",
        "six-neighbor star is not the letter" in normalized_note
        and "own incoming set" in normalized_note,
    )
    checks.check(
        "note-not-nsopp-leftover-child",
        "not a formed child" in normalized_note
        and "second pair is a new seed" in normalized_note
        and "not leftover of mixed #7188 fail/fail" in normalized_note,
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
        '    "docs/TWO_AXIS_OPPOSITE_ZPROBE_OWN_INCOMING_SET_EXISTENTIAL_OPPOSITE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "incoming_set" in defined_fns
        and "existential_opposite" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "form" in defined_fns
        and "new_records_meeting_six_nn" in defined_fns
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
    checks.check(
        "exist-opposite-fail-fail-not-cover-hold-hold",
        reverse == "fail"
        and face == "fail"
        and one_reverse == "fail"
        and one_face == "hold"
        and o_exist_reverse == "hold"
        and cover_reverse == "hold"
        and cover_face == "hold"
        and y_reverse == "hold"
        and y_face == "fail",
    )
    _ = (
        neighbor_reverse,
        x_reverse,
        x_face,
        ysym_locks,
        ysym_seeds,
        zsym_m1,
        perp_m1,
        zsym_face,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
