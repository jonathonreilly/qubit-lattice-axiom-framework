#!/usr/bin/env python3
"""Neighbor-read of M at t+1 reverse/face on four two-axis same-lock z-probes.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is four sites in two disjoint same-lock pairs: origin and (0,1,0) lock
+e_1; (0,0,1) and (0,1,1) lock +e_2. Neither pair is opposite. Same process
and z-probes as nm2slz. A 6-NN step is allowed iff it is perpendicular to
the parent lock axis. Newly formed sites lock the incoming step. Seeds keep
their seed letters as a singleton. t(q) is the formation tick. tau = t(q)+1.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. Unformed at tau => UNDEFINED. For formed
neighbor r = q+e, report M(r, tau). Neighbor-read HOLDs at q iff some formed
6-NN r has M(r, tau) defined and equal to M(q, tau) as sets. Unformed q =>
UNDEFINED. Mixed remains a set. Uniqueness is not required. Reverse HOLDs
iff neighbor-read at A and at B. Face likewise on C, D. Occupancy of sites
is not used. Named-sign lettering is not used. No larger host. This is not
leftover of nm2slz axis-cover. This is not leftover of two-axis opposite
z-probe neighbor-read. This is not leftover of R-style recovery of the
incoming step from neighbors. Displayed, not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_NEIGHBOR_READ_INCOMING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_NEIGHBOR_READ_INCOMING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
PAIR2: Point = (0, 1, 1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
BALL_SQ = 9
FOUR_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    (PAIR2, E2),
)
TWO_AXIS_OPP_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (PAIR2, NEG_E2),
)
ONE_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
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
X_AXIS_SAME_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E2),
    (E1, E2),
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
    "Neighbor-read of M at t+1 on the four z-probes of the "
    "two-axis same-lock seed, and reverse/face from that, are reported. "
    "Displayed, not adopted."
)
UNDEFINED = "UNDEFINED"


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def neg(step: Point) -> Point:
    return (-step[0], -step[1], -step[2])


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
    seeds: tuple[tuple[Point, Point], ...] = FOUR_SITE_SEEDS,
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


def matching_neighbors(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[Point, ...] | str:
    """Formed 6-NN r with M(r, tau) defined and equal to M(site, tau)."""
    own = incoming_set(site, tau, ticks, locks, seed_map)
    if own == UNDEFINED:
        return UNDEFINED
    if not isinstance(own, frozenset):
        raise TypeError(f"lock set is not a lock set: {own!r}")
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        other = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if other == UNDEFINED:
            continue
        if not isinstance(other, frozenset):
            raise TypeError(f"lock set is not a lock set: {other!r}")
        if other == own:
            found.append(neighbor)
    return tuple(found)


def neighbor_read(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> str:
    """HOLD iff some formed 6-NN recovers M(q, tau) as a set. Unformed => UNDEFINED."""
    matches = matching_neighbors(site, tau, ticks, locks, seed_map)
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    if matches:
        return "hold"
    return "fail"


def formed_neighbor_incoming(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> tuple[tuple[Point, Incoming], ...]:
    """M(r, tau) at each eventually-formed 6-NN of site, including UNDEFINED."""
    rows: list[tuple[Point, Incoming]] = []
    for step in NN:
        neighbor = add(site, step)
        if neighbor not in ticks:
            continue
        rows.append(
            (neighbor, incoming_set(neighbor, tau, ticks, locks, seed_map))
        )
    return tuple(rows)


def r_style_read(
    site: Point,
    tau: int,
    ticks: dict[Point, int],
    locks: dict[Point, set[Point]],
    seed_map: dict[Point, Point],
) -> Incoming:
    """Leftover contrast: incoming steps recovered as (-e) in M(q+e, tau)."""
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    recovered: set[Point] = set()
    for step in NN:
        neighbor = add(site, step)
        other = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if other == UNDEFINED:
            continue
        if not isinstance(other, frozenset):
            raise TypeError(f"lock set is not a lock set: {other!r}")
        if neg(step) in other:
            recovered.add(step)
    return frozenset(recovered)


def pair_read(left: str, right: str) -> str:
    """HOLD iff both sides HOLD. UNDEFINED if either side is UNDEFINED. Else fail."""
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


def reverse_report(read_a: str, read_b: str) -> str:
    """Reverse HOLDs iff neighbor-read at A and at B."""
    return pair_read(read_a, read_b)


def face_report(read_c: str, read_d: str) -> str:
    """Face HOLDs iff neighbor-read at C and at D."""
    return pair_read(read_c, read_d)


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def probe_reads(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = neighbor_read(
            site,
            site_ticks[site] + 1,
            site_ticks,
            site_locks,
            site_seeds,
        )
    return out


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

    print("neighbor-read of M reverse/face at t+1 on two-axis same-lock z-probes")
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
        "pair-read-identity",
        pair_read(UNDEFINED, "hold") == UNDEFINED
        and pair_read("hold", UNDEFINED) == UNDEFINED
        and pair_read("hold", "hold") == "hold"
        and pair_read("hold", "fail") == "fail"
        and pair_read("fail", "hold") == "fail"
        and pair_read("fail", "fail") == "fail",
    )
    checks.check(
        "neighbor-read-identity",
        neighbor_read(PROBES["B"], -1, {}, {}, {}) == UNDEFINED
        and matching_neighbors(PROBES["B"], -1, {}, {}, {}) == UNDEFINED,
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(TWO_AXIS_OPP_SEEDS)
    twosite_ticks, twosite_locks, twosite_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    xsame_ticks, xsame_locks, xsame_seeds = form(X_AXIS_SAME_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)

    tau1: dict[str, int] = {}
    m0: dict[str, Incoming] = {}
    m1: dict[str, Incoming] = {}
    reads: dict[str, str] = {}
    matches: dict[str, tuple[Point, ...] | str] = {}
    formed_m: dict[str, tuple[tuple[Point, Incoming], ...]] = {}
    r_style: dict[str, Incoming] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau0 = ticks[site]
        tau1[name] = ticks[site] + 1
        m0[name] = incoming_set(site, tau0, ticks, locks, seed_map)
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        reads[name] = neighbor_read(site, tau1[name], ticks, locks, seed_map)
        matches[name] = matching_neighbors(
            site, tau1[name], ticks, locks, seed_map
        )
        formed_m[name] = formed_neighbor_incoming(
            site, tau1[name], ticks, locks, seed_map
        )
        r_style[name] = r_style_read(site, tau1[name], ticks, locks, seed_map)
        print(
            f"{name} t={ticks[site]} "
            f"M={lockset_display(m1[name])} "
            f"neighbor-read={reads[name]}"
        )

    reverse = reverse_report(reads["A"], reads["B"])
    face = face_report(reads["C"], reads["D"])
    opp_reads = probe_reads(PROBES, opp_ticks, opp_locks, opp_seeds)
    opp_reverse = reverse_report(opp_reads["A"], opp_reads["B"])
    opp_face = face_report(opp_reads["C"], opp_reads["D"])
    one_reads = probe_reads(PROBES, one_ticks, one_locks, one_seeds)
    one_reverse = reverse_report(one_reads["A"], one_reads["B"])
    one_face = face_report(one_reads["C"], one_reads["D"])
    print(f"neighbor-read reverse={reverse} face={face}")
    print(
        f"nm2readz opposite z-probe neighbor-read reverse={opp_reverse} "
        f"face={opp_face} A={opp_reads['A']}"
    )
    print(
        f"1-axis same-lock z-probe neighbor-read reverse={one_reverse} "
        f"face={one_face} A={one_reads['A']}"
    )
    print(
        "per_element: each earliest incoming lock set M at a probe and at "
        "formed 6-NN, compared as sets at the probe's t+1"
    )
    print(
        "per_site: scored only at z-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print("per_block: four neighbor-read reports, reverse/face from those bits")
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    seed_a_parallel_blocked = ticks.get(add(E3, NEG_E2)) != 1
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and seed_a_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[E3] == 0
        and ticks[PROBES["A"]] == 0
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 1
        and ticks[PROBES["D"]] == 1
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["C"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["D"], 0, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(PAIR2, 1, ticks, locks, seed_map) == frozenset({E2})
        and FOUR_SITE_SEEDS
        == ((ORIGIN, E1), (E2, E1), (E3, E2), (PAIR2, E2)),
    )
    checks.check(
        "neither-pair-is-opposite",
        seed_map[ORIGIN] == seed_map[E2] == E1
        and seed_map[E3] == seed_map[PAIR2] == E2
        and add(seed_map[ORIGIN], seed_map[E2]) != ZERO
        and add(seed_map[E3], seed_map[PAIR2]) != ZERO
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS,
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
        m1["A"] == frozenset({E2})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E3})
        and m1["D"] == frozenset({E1}),
        str({name: lockset_display(m1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-frozen-from-t",
        m1["A"] == m0["A"]
        and m1["B"] == m0["B"]
        and m1["C"] == m0["C"]
        and m1["D"] == m0["D"],
    )
    checks.check(
        "theorem1-formed-6nn-M-at-A",
        formed_m["A"]
        == (
            ((1, 0, 1), frozenset({E1})),
            ((-1, 0, 1), frozenset({NEG_E1})),
            ((0, 1, 1), frozenset({E2})),
            ((0, -1, 1), UNDEFINED),
            ((0, 0, 2), frozenset({E3})),
            ((0, 0, 0), frozenset({E1})),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-M-at-B",
        formed_m["B"]
        == (
            ((2, 1, 1), UNDEFINED),
            ((0, 1, 1), frozenset({E2})),
            ((1, 2, 1), frozenset({E2})),
            ((1, 0, 1), frozenset({E1})),
            ((1, 1, 2), frozenset({E1, E3})),
            ((1, 1, 0), frozenset({NEG_E3})),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-M-at-C",
        formed_m["C"]
        == (
            ((1, 0, 2), frozenset({E1, E3})),
            ((-1, 0, 2), frozenset({NEG_E1, E3})),
            ((0, 1, 2), frozenset({E3})),
            ((0, -1, 2), frozenset({NEG_E2})),
            ((0, 0, 1), frozenset({E2})),
        ),
    )
    checks.check(
        "theorem1-formed-6nn-M-at-D",
        formed_m["D"]
        == (
            ((2, 0, 1), UNDEFINED),
            ((0, 0, 1), frozenset({E2})),
            ((1, 1, 1), frozenset({E1})),
            ((1, -1, 1), frozenset({NEG_E2})),
            ((1, 0, 2), frozenset({E1, E3})),
            ((1, 0, 0), frozenset({NEG_E3})),
        ),
    )
    checks.check(
        "theorem1-neighbor-read-bits",
        reads["A"] == "hold"
        and reads["B"] == "hold"
        and reads["C"] == "hold"
        and reads["D"] == "hold"
        and matches["A"] == ((0, 1, 1),)
        and matches["B"] == ((1, 0, 1),)
        and matches["C"] == ((0, 1, 2),)
        and matches["D"] == ((1, 1, 1),),
        str({name: (reads[name], matches[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        incoming_set((1, 1, 2), tau1["B"], ticks, locks, seed_map)
        == frozenset({E1, E3})
        and unique_letter(
            incoming_set((1, 1, 2), tau1["B"], ticks, locks, seed_map)
        )
        == UNDEFINED
        and reads["B"] == "hold"
        and incoming_set((1, 0, 2), tau1["C"], ticks, locks, seed_map)
        == frozenset({E1, E3}),
    )
    checks.check(
        "theorem1-A-is-seed",
        PROBES["A"] == E3
        and ticks[E3] == 0
        and E3 in seed_map
        and seed_map[E3] == E2
        and m1["A"] == frozenset({E2})
        and ticks[PAIR2] == 0
        and seed_map[PAIR2] == E2
        and Y_PROBES["A"] != PROBES["A"]
        and X_PROBES["A"] != PROBES["A"],
    )
    checks.check(
        "compare-nm2readz-opposite-neighbor-read",
        opp_reads["A"] == "fail"
        and opp_reads["B"] == "hold"
        and opp_reads["C"] == "hold"
        and opp_reads["D"] == "hold"
        and opp_reverse == "fail"
        and opp_face == "hold"
        and reads["A"] == "hold"
        and reverse == "hold"
        and face == "hold"
        and FOUR_SITE_SEEDS != TWO_AXIS_OPP_SEEDS,
    )
    checks.check(
        "compare-1-axis-same-lock-z-neighbor-read",
        one_reads["A"] == "hold"
        and one_reads["C"] == "fail"
        and one_reverse == "hold"
        and one_face == "fail"
        and one_ticks[PROBES["A"]] == 1
        and ticks[PROBES["A"]] == 0
        and reverse == "hold"
        and face == "hold",
    )
    checks.check(
        "theorem2-reverse-hold",
        reverse == "hold"
        and reads["A"] == "hold"
        and reads["B"] == "hold"
        and reverse != UNDEFINED
        and reverse != "fail",
    )
    checks.check(
        "theorem3-face-hold",
        face == "hold"
        and reads["C"] == "hold"
        and reads["D"] == "hold"
        and face != UNDEFINED
        and face != "fail",
    )
    checks.check(
        "mutation-r-style-differs",
        r_style["A"] == frozenset()
        and r_style["B"] == frozenset()
        and r_style["C"] == frozenset()
        and r_style["D"] == frozenset()
        and r_style["A"] != m1["A"]
        and reads["A"] == "hold"
        and reads["B"] == "hold",
    )
    checks.check(
        "mutation-unique-letter-mixed-neighbor",
        unique_letter(
            incoming_set((1, 1, 2), tau1["B"], ticks, locks, seed_map)
        )
        == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_letter(m1["A"]) == frozenset({E2})
        and reads["A"] == "hold"
        and reads["B"] == "hold",
    )
    y_reads = probe_reads(Y_PROBES, ticks, locks, seed_map)
    x_reads = probe_reads(X_PROBES, ticks, locks, seed_map)
    perp_reads = probe_reads(PROBES, perp_ticks, perp_locks, perp_seeds)
    zsym_reads = probe_reads(PROBES, zsym_ticks, zsym_locks, zsym_seeds)
    twosite_reads = probe_reads(
        PROBES, twosite_ticks, twosite_locks, twosite_seeds
    )
    xsame_reads = probe_reads(PROBES, xsame_ticks, xsame_locks, xsame_seeds)
    y_reverse = reverse_report(y_reads["A"], y_reads["B"])
    y_face = face_report(y_reads["C"], y_reads["D"])
    x_reverse = reverse_report(x_reads["A"], x_reads["B"])
    x_face = face_report(x_reads["C"], x_reads["D"])
    twosite_reverse = reverse_report(twosite_reads["A"], twosite_reads["B"])
    twosite_face = face_report(twosite_reads["C"], twosite_reads["D"])
    checks.check(
        "not-x-probes-or-y-probes-or-perp",
        FOUR_SITE_SEEDS != PERP_SEEDS
        and probe_sites != x_probe_sites
        and probe_sites != y_probe_sites
        and y_reads["A"] == "hold"
        and y_reads["C"] == "fail"
        and y_reverse == "hold"
        and y_face == "fail"
        and x_reverse == "hold"
        and x_face == "hold"
        and x_reads["A"] == "hold"
        and ticks[X_PROBES["A"]] == 2
        and ticks[PROBES["A"]] == 0
        and m1["A"] == frozenset({E2})
        and incoming_set(
            X_PROBES["A"], ticks[X_PROBES["A"]] + 1, ticks, locks, seed_map
        )
        == frozenset({NEG_E3})
        and perp_reads["B"] == "fail"
        and reverse == "hold"
        and face == "hold"
        and y_face != face,
    )
    checks.check(
        "not-nsopp-leftover-second-pair-is-seed",
        FOUR_SITE_SEEDS != TWO_SITE_SEEDS
        and FOUR_SITE_SEEDS != Z_SYMMETRIC_SEEDS
        and FOUR_SITE_SEEDS != X_AXIS_SAME_SEEDS
        and FOUR_SITE_SEEDS != Y_SYMMETRIC_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in twosite_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and twosite_ticks[E3] == 1
        and twosite_locks[E3] == {E3}
        and twosite_reads["A"] == "hold"
        and twosite_reads["C"] == "fail"
        and twosite_reverse == "hold"
        and twosite_face == "fail"
        and reverse == "hold"
        and face == "hold"
        and zsym_reads["A"] == "fail"
        and zsym_reads["C"] == "fail"
        and xsame_reads["C"] == "fail"
        and xsame_reads["A"] == "hold",
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-and-neighbor-read",
        "t(A)=0" in note
        and "t(B)=1" in note
        and "t(C)=1" in note
        and "t(D)=1" in note
        and "M(A, τ) = {+e_2}" in note
        and "M(B, τ) = {+e_1}" in note
        and "M(C, τ) = {+e_3}" in note
        and "M(D, τ) = {+e_1}" in note
        and "neighbor-read(A) = hold" in note
        and "neighbor-read(B) = hold" in note
        and "neighbor-read(C) = hold" in note
        and "neighbor-read(D) = hold" in note,
    )
    checks.check(
        "note-reports-formed-neighbors",
        "formed 6-NN of A at τ: (1, 0, 1)={+e_1}, (-1, 0, 1)={−e_1}, (0, 1, 1)={+e_2}, (0, -1, 1)=UNDEFINED, (0, 0, 2)={+e_3}, (0, 0, 0)={+e_1}"
        in note
        and "formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)={+e_2}, (1, 2, 1)={+e_2}, (1, 0, 1)={+e_1}, (1, 1, 2)={+e_1, +e_3}, (1, 1, 0)={−e_3}"
        in note
        and "formed 6-NN of C at τ: (1, 0, 2)={+e_1, +e_3}, (-1, 0, 2)={−e_1, +e_3}, (0, 1, 2)={+e_3}, (0, -1, 2)={−e_2}, (0, 0, 1)={+e_2}"
        in note
        and "formed 6-NN of D at τ: (2, 0, 1)=UNDEFINED, (0, 0, 1)={+e_2}, (1, 1, 1)={+e_1}, (1, -1, 1)={−e_2}, (1, 0, 2)={+e_1, +e_3}, (1, 0, 0)={−e_3}"
        in note
        and "matching 6-NN of A: (0, 1, 1)" in note
        and "matching 6-NN of B: (1, 0, 1)" in note
        and "matching 6-NN of C: (0, 1, 2)" in note
        and "matching 6-NN of D: (1, 1, 1)" in note,
    )
    checks.check(
        "note-reports-reverse-face",
        "Reverse neighbor-read at τ: hold" in note
        and "Face neighbor-read at τ: hold" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-opposite-or-r-style-leftover",
        "not leftover of nm2slz axis-cover" in normalized_note
        and "not leftover of two-axis opposite z-probe neighbor-read" in normalized_note
        and "not leftover of R-style" in normalized_note
        and "neither pair is opposite" in normalized_note,
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
        '    "docs/TWO_AXIS_SAME_LOCK_ZPROBE_NEIGHBOR_READ_INCOMING_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    defined_fns = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    checks.check(
        "identity-gates-present",
        "incoming_set" in defined_fns
        and "neighbor_read" in defined_fns
        and "matching_neighbors" in defined_fns
        and "reverse_report" in defined_fns
        and "face_report" in defined_fns
        and "formed_neighbor_incoming" in defined_fns
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
    checks.check(
        "neighbor-read-not-cover-or-opposite",
        reverse == "hold"
        and face == "hold"
        and reads["A"] == "hold"
        and reads["B"] == "hold"
        and reads["C"] == "hold"
        and reads["D"] == "hold"
        and opp_reverse == "fail"
        and opp_reads["A"] == "fail",
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
