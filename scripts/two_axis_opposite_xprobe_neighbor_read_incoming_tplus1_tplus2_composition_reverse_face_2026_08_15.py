#!/usr/bin/env python3
"""Neighbor-read of M at t+1 versus t+2 reverse/face composition.

Finite host: Euclidean ball of radius 3 centered at the origin. Seed at tick
0 is two disjoint opposite pairs: origin locks +e_1, (0,1,0) locks -e_1,
(0,0,1) locks +e_2, (0,1,1) locks -e_2. Same process and x-probes as nm2axpx.
A 6-NN step is allowed iff it is perpendicular to the parent lock axis.
Newly formed sites lock the incoming step. Seeds keep their seed letters as
a singleton. The second pair is a new seed, not a formed child of the first
pair. t(q) is the formation tick. tau1 = t(q)+1. tau2 = t(q)+2. No global T.
M(q, tau) is the set of earliest incoming nearest-neighbor steps at q using
only records with tick <= tau. Unformed at tau => UNDEFINED. Neighbor-read
HOLDs at q, tau iff some formed 6-NN r has M(r, tau) defined and equal to
M(q, tau) as sets. Unformed q => UNDEFINED. Mixed remains a set. Uniqueness
is not required. Reverse HOLDs at a cut iff neighbor-read at A and at B.
Face likewise on C, D. Composition HOLDs iff neighbor-read at tau1 equals
neighbor-read at tau2 at A, B, C, and D. Occupancy n is not used. Named-sign
lettering is not used. No larger host. This is not leftover of nm2readx
one-cut neighbor-read. This is not leftover of nm2axpx forall-perp. This is
not leftover of nm2axx axis-cover. This is not leftover of two-axis
same-lock z-probe neighbor-read. This is not leftover of two-axis same-lock
x-probe neighbor-read. This is not leftover of nm2t2x M freeze. This is not
leftover of R-style recovery of the incoming step from neighbors. Displayed,
not adopted. Do not attach L1.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_NEIGHBOR_READ_INCOMING_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_XPROBE_NEIGHBOR_READ_INCOMING_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
YZ: Point = (0, 1, 1)
NN: tuple[Point, ...] = (
    E1,
    NEG_E1,
    E2,
    NEG_E2,
    E3,
    NEG_E3,
)
BALL_SQ = 9
TWO_AXIS_OPPOSITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (E3, E2),
    (YZ, NEG_E2),
)
FOUR_SITE_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, E1),
    (E3, E2),
    (YZ, E2),
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
Y_SYMMETRIC_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E2, NEG_E1),
    (NEG_E2, NEG_E1),
)
NSPAR_SEEDS: tuple[tuple[Point, Point], ...] = (
    (ORIGIN, E1),
    (E1, NEG_E1),
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
    "S⁺",
    "Cl(3,0)",
    "Runner cache",
    "ndot",
)
CLAIM_SCOPE = (
    "Neighbor-read of M at t+1 versus t+2 on the four x-probes "
    "of the two-axis opposite seed, reverse/face at each cut, and "
    "composition, are reported. Displayed, not adopted."
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


def formed_display(rows: tuple[tuple[Point, Incoming], ...]) -> str:
    return ", ".join(
        f"{neighbor}={lockset_display(incoming)}" for neighbor, incoming in rows
    )


def matching_display(matches: tuple[Point, ...] | str) -> str:
    if matches == UNDEFINED:
        return UNDEFINED
    if not isinstance(matches, tuple):
        raise TypeError(f"matching neighbors are not a tuple: {matches!r}")
    return ", ".join(str(site) for site in matches)


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
    seeds: tuple[tuple[Point, Point], ...] = TWO_AXIS_OPPOSITE_SEEDS,
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
    """Recover incoming as steps e with -e in M(q+e, tau). Different object."""
    own = incoming_set(site, tau, ticks, locks, seed_map)
    if own == UNDEFINED:
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


def composition_report(
    reads1: dict[str, str],
    reads2: dict[str, str],
) -> str:
    """HOLD iff neighbor-read at tau1 equals neighbor-read at tau2 at A,B,C,D."""
    for name in ("A", "B", "C", "D"):
        if reads1[name] == UNDEFINED or reads2[name] == UNDEFINED:
            return UNDEFINED
        if reads1[name] != reads2[name]:
            return "fail"
    return "hold"


def m_freeze_report(
    m1: dict[str, Incoming],
    m2: dict[str, Incoming],
) -> str:
    """Leftover nm2t2x: HOLD iff M(tau1)=M(tau2) at A,B,C,D. Not this letter."""
    for name in ("A", "B", "C", "D"):
        if m1[name] == UNDEFINED or m2[name] == UNDEFINED:
            return UNDEFINED
        if m1[name] != m2[name]:
            return "fail"
    return "hold"


def unique_letter(value: Incoming) -> Incoming:
    if value == UNDEFINED or not isinstance(value, frozenset) or len(value) != 1:
        return UNDEFINED
    return value


def probe_reads(
    probes: dict[str, Point],
    site_ticks: dict[Point, int],
    site_locks: dict[Point, set[Point]],
    site_seeds: dict[Point, Point],
    *,
    plus: int = 1,
) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("A", "B", "C", "D"):
        site = probes[name]
        if site not in site_ticks:
            out[name] = UNDEFINED
            continue
        out[name] = neighbor_read(
            site,
            site_ticks[site] + plus,
            site_ticks,
            site_locks,
            site_seeds,
        )
    return out


def new_six_neighbors(
    site: Point,
    ticks: dict[Point, int],
    offset: int,
) -> tuple[Point, ...]:
    formed_tick = ticks[site]
    found: list[Point] = []
    for step in NN:
        neighbor = add(site, step)
        if ticks.get(neighbor) == formed_tick + offset:
            found.append(neighbor)
    return tuple(found)


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

    print("neighbor-read of M reverse/face composition t+1 versus t+2")
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
        and add(E2, NEG_E2) == ZERO
        and add(E3, NEG_E3) == ZERO
        and add(E3, E2) == YZ
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
    checks.check(
        "composition-identity",
        composition_report(
            {"A": UNDEFINED, "B": "hold", "C": "hold", "D": "hold"},
            {"A": "hold", "B": "hold", "C": "hold", "D": "hold"},
        )
        == UNDEFINED
        and composition_report(
            {"A": "hold", "B": "hold", "C": "hold", "D": "fail"},
            {"A": "hold", "B": "hold", "C": "hold", "D": "hold"},
        )
        == "fail"
        and composition_report(
            {"A": "fail", "B": "hold", "C": "hold", "D": "hold"},
            {"A": "fail", "B": "hold", "C": "hold", "D": "hold"},
        )
        == "hold",
    )

    ticks, locks, seed_map = form()
    one_ticks, one_locks, one_seeds = form(ONE_AXIS_SEEDS)
    sl_ticks, sl_locks, sl_seeds = form(FOUR_SITE_SEEDS)
    twosite_ticks, twosite_locks, twosite_seeds = form(TWO_SITE_SEEDS)
    perp_ticks, perp_locks, perp_seeds = form(PERP_SEEDS)
    zsym_ticks, zsym_locks, zsym_seeds = form(Z_SYMMETRIC_SEEDS)
    ysym_ticks, _ysym_locks, _ysym_seeds = form(Y_SYMMETRIC_SEEDS)
    one_axis_ticks, one_axis_locks, one_axis_seeds = form(TWO_SITE_SEEDS)

    tau1: dict[str, int] = {}
    tau2: dict[str, int] = {}
    m1: dict[str, Incoming] = {}
    m2: dict[str, Incoming] = {}
    reads1: dict[str, str] = {}
    reads2: dict[str, str] = {}
    matches1: dict[str, tuple[Point, ...] | str] = {}
    matches2: dict[str, tuple[Point, ...] | str] = {}
    formed1: dict[str, tuple[tuple[Point, Incoming], ...]] = {}
    formed2: dict[str, tuple[tuple[Point, Incoming], ...]] = {}
    r_style: dict[str, Incoming] = {}
    new1: dict[str, tuple[Point, ...]] = {}
    new2: dict[str, tuple[Point, ...]] = {}
    for name in ("A", "B", "C", "D"):
        site = PROBES[name]
        tau1[name] = ticks[site] + 1
        tau2[name] = ticks[site] + 2
        m1[name] = incoming_set(site, tau1[name], ticks, locks, seed_map)
        m2[name] = incoming_set(site, tau2[name], ticks, locks, seed_map)
        reads1[name] = neighbor_read(site, tau1[name], ticks, locks, seed_map)
        reads2[name] = neighbor_read(site, tau2[name], ticks, locks, seed_map)
        matches1[name] = matching_neighbors(
            site, tau1[name], ticks, locks, seed_map
        )
        matches2[name] = matching_neighbors(
            site, tau2[name], ticks, locks, seed_map
        )
        formed1[name] = formed_neighbor_incoming(
            site, tau1[name], ticks, locks, seed_map
        )
        formed2[name] = formed_neighbor_incoming(
            site, tau2[name], ticks, locks, seed_map
        )
        r_style[name] = r_style_read(site, tau1[name], ticks, locks, seed_map)
        new1[name] = new_six_neighbors(site, ticks, 1)
        new2[name] = new_six_neighbors(site, ticks, 2)
        print(
            f"{name} t={ticks[site]} "
            f"M1={lockset_display(m1[name])} "
            f"M2={lockset_display(m2[name])} "
            f"neighbor-read1={reads1[name]} "
            f"neighbor-read2={reads2[name]}"
        )

    reverse1 = reverse_report(reads1["A"], reads1["B"])
    reverse2 = reverse_report(reads2["A"], reads2["B"])
    face1 = face_report(reads1["C"], reads1["D"])
    face2 = face_report(reads2["C"], reads2["D"])
    composition = composition_report(reads1, reads2)
    m_freeze = m_freeze_report(m1, m2)
    sl_x_reads1 = probe_reads(PROBES, sl_ticks, sl_locks, sl_seeds, plus=1)
    sl_x_reads2 = probe_reads(PROBES, sl_ticks, sl_locks, sl_seeds, plus=2)
    sl_x_reverse1 = reverse_report(sl_x_reads1["A"], sl_x_reads1["B"])
    sl_x_face1 = face_report(sl_x_reads1["C"], sl_x_reads1["D"])
    sl_x_comp = composition_report(sl_x_reads1, sl_x_reads2)
    sl_z_reads1 = probe_reads(Z_PROBES, sl_ticks, sl_locks, sl_seeds, plus=1)
    sl_z_reads2 = probe_reads(Z_PROBES, sl_ticks, sl_locks, sl_seeds, plus=2)
    sl_z_reverse1 = reverse_report(sl_z_reads1["A"], sl_z_reads1["B"])
    sl_z_face1 = face_report(sl_z_reads1["C"], sl_z_reads1["D"])
    sl_z_comp = composition_report(sl_z_reads1, sl_z_reads2)
    opp_z_reads1 = probe_reads(Z_PROBES, ticks, locks, seed_map, plus=1)
    opp_z_reads2 = probe_reads(Z_PROBES, ticks, locks, seed_map, plus=2)
    opp_z_reverse1 = reverse_report(opp_z_reads1["A"], opp_z_reads1["B"])
    opp_z_face1 = face_report(opp_z_reads1["C"], opp_z_reads1["D"])
    opp_z_comp = composition_report(opp_z_reads1, opp_z_reads2)
    print(
        f"neighbor-read reverse1={reverse1} reverse2={reverse2} "
        f"face1={face1} face2={face2} composition={composition}"
    )
    print(
        f"same-lock x-probe neighbor-read reverse={sl_x_reverse1} "
        f"face={sl_x_face1} composition={sl_x_comp}"
    )
    print(
        f"nm2readslx same-lock x-probe neighbor-read A={sl_x_reads1['A']}"
    )
    print(
        f"nm2readslz same-lock z-probe neighbor-read reverse={sl_z_reverse1} "
        f"face={sl_z_face1} composition={sl_z_comp} A={sl_z_reads1['A']}"
    )
    print(
        f"opposite z-probe neighbor-read reverse={opp_z_reverse1} "
        f"face={opp_z_face1} composition={opp_z_comp} A={opp_z_reads1['A']}"
    )
    print(
        "per_element: each earliest incoming lock set M at a probe and at "
        "formed 6-NN, compared as sets at the probe's t+1 and t+2"
    )
    print(
        "per_site: scored only at x-probes A,B,C,D on Euclidean B_3(0); no other sites"
    )
    print(
        "per_mode: no spectral or mode calculation is executed on this finite host"
    )
    print(
        "per_block: four neighbor-read reports at two cuts, reverse/face at "
        "each cut, composition of the bits"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide lettering rule is claimed"
    )

    origin_parallel_blocked = all(
        ticks.get(add(ORIGIN, step)) != 1 for step in (E1, NEG_E1)
    )
    checks.check(
        "perp-step-incoming-lock",
        origin_parallel_blocked
        and ticks[NEG_E2] == 1
        and ticks[NEG_E3] == 1
        and ticks[E3] == 0
        and ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2
        and "s·e_i=0" in note.replace(" ", ""),
    )
    checks.check(
        "undefined-if-unformed",
        incoming_set(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["B"], 0, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["A"], 1, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["C"], 2, ticks, locks, seed_map) == UNDEFINED
        and neighbor_read(PROBES["D"], 1, ticks, locks, seed_map) == UNDEFINED,
    )
    checks.check(
        "incoming-set-seed-singleton",
        incoming_set(ORIGIN, 0, ticks, locks, seed_map) == frozenset({E1})
        and incoming_set(E2, 1, ticks, locks, seed_map) == frozenset({NEG_E1})
        and incoming_set(E3, 1, ticks, locks, seed_map) == frozenset({E2})
        and incoming_set(YZ, 1, ticks, locks, seed_map) == frozenset({NEG_E2})
        and TWO_AXIS_OPPOSITE_SEEDS
        == ((ORIGIN, E1), (E2, NEG_E1), (E3, E2), (YZ, NEG_E2)),
    )
    checks.check(
        "pairs-are-opposite",
        seed_map[ORIGIN] == E1
        and seed_map[E2] == NEG_E1
        and seed_map[E3] == E2
        and seed_map[YZ] == NEG_E2
        and add(seed_map[ORIGIN], seed_map[E2]) == ZERO
        and add(seed_map[E3], seed_map[YZ]) == ZERO
        and TWO_AXIS_OPPOSITE_SEEDS != FOUR_SITE_SEEDS,
    )
    checks.check(
        "theorem1-formation-ticks",
        ticks[PROBES["A"]] == 2
        and ticks[PROBES["B"]] == 1
        and ticks[PROBES["C"]] == 3
        and ticks[PROBES["D"]] == 2,
        str({name: ticks[PROBES[name]] for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-M-at-tau1-and-tau2",
        m1["A"] == frozenset({NEG_E3})
        and m1["B"] == frozenset({E1})
        and m1["C"] == frozenset({E1})
        and m1["D"] == frozenset({NEG_E3})
        and m2["A"] == m1["A"]
        and m2["B"] == m1["B"]
        and m2["C"] == m1["C"]
        and m2["D"] == m1["D"],
        str({name: (lockset_display(m1[name]), lockset_display(m2[name])) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-formed-6nn-M-at-A-both-cuts",
        formed1["A"]
        == (
            ((2, 0, 0), frozenset({E1})),
            ((0, 0, 0), frozenset({E1})),
            ((1, 1, 0), frozenset({NEG_E3})),
            ((1, -1, 0), frozenset({E1})),
            ((1, 0, 1), frozenset({E1})),
            ((1, 0, -1), frozenset({E1})),
        )
        and formed2["A"] == formed1["A"],
    )
    checks.check(
        "theorem1-formed-6nn-M-at-B-both-cuts",
        formed1["B"]
        == (
            ((2, 1, 1), UNDEFINED),
            ((0, 1, 1), frozenset({NEG_E2})),
            ((1, 2, 1), frozenset({E2})),
            ((1, 0, 1), frozenset({E1})),
            ((1, 1, 2), frozenset({E1, E3})),
            ((1, 1, 0), frozenset({NEG_E3})),
        )
        and formed2["B"] == formed1["B"],
    )
    checks.check(
        "theorem1-formed-6nn-M-at-C-both-cuts",
        formed1["C"]
        == (
            ((1, 0, 0), frozenset({NEG_E3})),
            ((2, 1, 0), frozenset({E1})),
            ((2, -1, 0), frozenset({NEG_E2, NEG_E3})),
            ((2, 0, 1), frozenset({E2, E3, NEG_E3})),
            ((2, 0, -1), frozenset({NEG_E3})),
        )
        and formed2["C"] == formed1["C"],
    )
    checks.check(
        "theorem1-formed-6nn-M-at-D-both-cuts",
        formed1["D"]
        == (
            ((2, 1, 0), frozenset({E1})),
            ((0, 1, 0), frozenset({NEG_E1})),
            ((1, 2, 0), frozenset({E1})),
            ((1, 0, 0), frozenset({NEG_E3})),
            ((1, 1, 1), frozenset({E1})),
            ((1, 1, -1), frozenset({E1})),
        )
        and formed2["D"] == formed1["D"],
    )
    checks.check(
        "theorem1-neighbor-read-bits-both-cuts",
        reads1["A"] == "hold"
        and reads1["B"] == "hold"
        and reads1["C"] == "hold"
        and reads1["D"] == "hold"
        and reads2["A"] == "hold"
        and reads2["B"] == "hold"
        and reads2["C"] == "hold"
        and reads2["D"] == "hold"
        and matches1["A"] == ((1, 1, 0),)
        and matches1["B"] == ((1, 0, 1),)
        and matches1["C"] == ((2, 1, 0),)
        and matches1["D"] == ((1, 0, 0),)
        and matches2["A"] == matches1["A"]
        and matches2["B"] == matches1["B"]
        and matches2["C"] == matches1["C"]
        and matches2["D"] == matches1["D"],
        str({name: (reads1[name], reads2[name], matches1[name]) for name in ("A", "B", "C", "D")}),
    )
    checks.check(
        "theorem1-no-new-6nn-at-tplus2",
        new1["A"] == ((2, 0, 0),)
        and new1["B"] == ((1, 2, 1), (1, 1, 2), (1, 1, 0))
        and new1["C"] == ((2, -1, 0), (2, 0, 1), (2, 0, -1))
        and new1["D"] == ((2, 1, 0),)
        and new2["A"] == ()
        and new2["B"] == ()
        and new2["C"] == ()
        and new2["D"] == (),
    )
    checks.check(
        "theorem1-mixed-stays-a-set",
        incoming_set((1, 1, 2), tau1["B"], ticks, locks, seed_map)
        == frozenset({E1, E3})
        and unique_letter(
            incoming_set((1, 1, 2), tau1["B"], ticks, locks, seed_map)
        )
        == UNDEFINED
        and reads1["B"] == "hold"
        and incoming_set((2, -1, 0), tau1["C"], ticks, locks, seed_map)
        == frozenset({NEG_E2, NEG_E3})
        and incoming_set((2, 0, 1), tau1["C"], ticks, locks, seed_map)
        == frozenset({E2, E3, NEG_E3})
        and unique_letter(
            incoming_set((2, 0, 1), tau1["C"], ticks, locks, seed_map)
        )
        == UNDEFINED,
    )
    checks.check(
        "theorem1-A-is-not-seed",
        PROBES["A"] == E1
        and ticks[E1] == 2
        and E1 not in seed_map
        and m1["A"] == frozenset({NEG_E3})
        and Y_PROBES["A"] != PROBES["A"]
        and Z_PROBES["A"] != PROBES["A"],
    )
    sl_b_partner = incoming_set(
        YZ, sl_ticks[PROBES["B"]] + 1, sl_ticks, sl_locks, sl_seeds
    )
    sl_d_partner = incoming_set(
        E2, sl_ticks[PROBES["D"]] + 1, sl_ticks, sl_locks, sl_seeds
    )
    checks.check(
        "compare-same-lock-x-neighbor-read",
        sl_x_reads1["A"] == "hold"
        and sl_x_reads1["B"] == "hold"
        and sl_x_reads1["C"] == "hold"
        and sl_x_reads1["D"] == "hold"
        and sl_x_reverse1 == "hold"
        and sl_x_face1 == "hold"
        and sl_x_comp == "hold"
        and sl_b_partner == frozenset({E2})
        and formed1["B"][1][1] == frozenset({NEG_E2})
        and sl_d_partner == frozenset({E1})
        and formed1["D"][1][1] == frozenset({NEG_E1})
        and FOUR_SITE_SEEDS != TWO_AXIS_OPPOSITE_SEEDS,
    )
    checks.check(
        "compare-nm2readslz-same-lock-z-neighbor-read",
        sl_z_reads1["A"] == "hold"
        and sl_z_reads1["B"] == "hold"
        and sl_z_reads1["C"] == "hold"
        and sl_z_reads1["D"] == "hold"
        and sl_z_reverse1 == "hold"
        and sl_z_face1 == "hold"
        and sl_z_comp == "hold"
        and sl_ticks[Z_PROBES["A"]] == 0
        and ticks[PROBES["A"]] == 2
        and Z_PROBES["A"] in sl_seeds
        and PROBES["A"] not in seed_map
        and incoming_set(
            Z_PROBES["A"], sl_ticks[Z_PROBES["A"]] + 1, sl_ticks, sl_locks, sl_seeds
        )
        == frozenset({E2})
        and m1["A"] == frozenset({NEG_E3}),
    )
    checks.check(
        "compare-opposite-z-neighbor-read",
        opp_z_reads1["A"] == "fail"
        and opp_z_reads1["B"] == "hold"
        and opp_z_reads1["C"] == "hold"
        and opp_z_reads1["D"] == "hold"
        and opp_z_reverse1 == "fail"
        and opp_z_face1 == "hold"
        and opp_z_comp == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and composition == "hold",
    )
    one_reads1 = probe_reads(PROBES, one_ticks, one_locks, one_seeds, plus=1)
    one_reads2 = probe_reads(PROBES, one_ticks, one_locks, one_seeds, plus=2)
    one_reverse = reverse_report(one_reads1["A"], one_reads1["B"])
    one_face = face_report(one_reads1["C"], one_reads1["D"])
    one_comp = composition_report(one_reads1, one_reads2)
    checks.check(
        "compare-1-axis-same-lock-x-neighbor-read",
        one_reads1["A"] == "fail"
        and one_reads1["C"] == "hold"
        and one_reads1["D"] == "fail"
        and one_reverse == "fail"
        and one_face == "fail"
        and one_comp == "hold"
        and one_ticks[PROBES["A"]] == 3
        and ticks[PROBES["A"]] == 2
        and reverse1 == "hold"
        and face1 == "hold",
    )
    checks.check(
        "theorem2-reverse-hold-both-cuts",
        reverse1 == "hold"
        and reverse2 == "hold"
        and reads1["A"] == "hold"
        and reads1["B"] == "hold"
        and reads2["A"] == "hold"
        and reads2["B"] == "hold"
        and reverse1 != UNDEFINED
        and reverse2 != UNDEFINED
        and reverse1 != "fail",
    )
    checks.check(
        "theorem2-face-hold-both-cuts",
        face1 == "hold"
        and face2 == "hold"
        and reads1["C"] == "hold"
        and reads1["D"] == "hold"
        and reads2["C"] == "hold"
        and reads2["D"] == "hold"
        and face1 != UNDEFINED
        and face2 != UNDEFINED
        and face1 != "fail",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and reads1["A"] == reads2["A"]
        and reads1["B"] == reads2["B"]
        and reads1["C"] == reads2["C"]
        and reads1["D"] == reads2["D"]
        and composition != UNDEFINED
        and composition != "fail"
        and m_freeze == "hold"
        and composition == m_freeze
        and opp_z_comp == "hold"
        and opp_z_reverse1 == "fail",
    )
    checks.check(
        "mutation-r-style-differs",
        r_style["A"] == frozenset({NEG_E1})
        and r_style["B"] == frozenset()
        and r_style["C"] == frozenset({E3})
        and r_style["D"] == frozenset()
        and r_style["A"] != m1["A"]
        and r_style["C"] != m1["C"]
        and reads1["A"] == "hold"
        and reads1["C"] == "hold",
    )
    checks.check(
        "mutation-unique-letter-mixed-neighbor",
        unique_letter(
            incoming_set((1, 1, 2), tau1["B"], ticks, locks, seed_map)
        )
        == UNDEFINED
        and unique_letter(m1["B"]) == frozenset({E1})
        and unique_letter(m1["A"]) == frozenset({NEG_E3})
        and reads1["A"] == "hold"
        and reads1["B"] == "hold",
    )
    y_reads1 = probe_reads(Y_PROBES, ticks, locks, seed_map, plus=1)
    y_reads2 = probe_reads(Y_PROBES, ticks, locks, seed_map, plus=2)
    z_reads1 = probe_reads(Z_PROBES, ticks, locks, seed_map, plus=1)
    perp_reads1 = probe_reads(PROBES, perp_ticks, perp_locks, perp_seeds, plus=1)
    zsym_reads1 = probe_reads(PROBES, zsym_ticks, zsym_locks, zsym_seeds, plus=1)
    twosite_reads1 = probe_reads(
        PROBES, twosite_ticks, twosite_locks, twosite_seeds, plus=1
    )
    twosite_reads2 = probe_reads(
        PROBES, twosite_ticks, twosite_locks, twosite_seeds, plus=2
    )
    y_reverse = reverse_report(y_reads1["A"], y_reads1["B"])
    y_face = face_report(y_reads1["C"], y_reads1["D"])
    y_comp = composition_report(y_reads1, y_reads2)
    z_reverse = reverse_report(z_reads1["A"], z_reads1["B"])
    z_face = face_report(z_reads1["C"], z_reads1["D"])
    twosite_reverse = reverse_report(twosite_reads1["A"], twosite_reads1["B"])
    twosite_face = face_report(twosite_reads1["C"], twosite_reads1["D"])
    twosite_comp = composition_report(twosite_reads1, twosite_reads2)
    checks.check(
        "not-y-probes-or-z-probes-or-perp",
        TWO_AXIS_OPPOSITE_SEEDS != PERP_SEEDS
        and probe_sites != y_probe_sites
        and probe_sites != z_probe_sites
        and y_reads1["A"] == "fail"
        and y_reads1["C"] == "fail"
        and y_reverse == "fail"
        and y_face == "fail"
        and y_comp == "hold"
        and z_reverse == "fail"
        and z_face == "hold"
        and ticks[Y_PROBES["A"]] == 0
        and ticks[Z_PROBES["A"]] == 0
        and ticks[PROBES["A"]] == 2
        and m1["A"] == frozenset({NEG_E3})
        and incoming_set(
            Y_PROBES["A"], ticks[Y_PROBES["A"]] + 1, ticks, locks, seed_map
        )
        == frozenset({NEG_E1})
        and perp_reads1["A"] == "fail"
        and perp_reads1["B"] == "fail"
        and reverse1 == "hold"
        and face1 == "hold"
        and y_face != face1,
    )
    checks.check(
        "not-nsopp-leftover-second-pair-is-seed",
        TWO_AXIS_OPPOSITE_SEEDS != TWO_SITE_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != Z_SYMMETRIC_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != Y_SYMMETRIC_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != NSPAR_SEEDS
        and TWO_AXIS_OPPOSITE_SEEDS != FOUR_SITE_SEEDS
        and sum(time == 0 for time in ticks.values()) == 4
        and sum(time == 0 for time in twosite_ticks.values()) == 2
        and sum(time == 0 for time in ysym_ticks.values()) == 3
        and ticks[E3] == 0
        and locks[E3] == {E2}
        and twosite_ticks[E3] == 1
        and twosite_locks[E3] == {E3}
        and twosite_reads1["A"] == "fail"
        and twosite_reads1["C"] == "hold"
        and twosite_reverse == "fail"
        and twosite_face == "fail"
        and twosite_comp == "hold"
        and reverse1 == "hold"
        and face1 == "hold"
        and zsym_reads1["A"] == "fail"
        and zsym_reads1["C"] == "hold"
        and one_axis_ticks[E3] == 1
        and one_axis_locks[E3] == {E3}
        and E3 not in one_axis_seeds
        and E3 in seed_map
        and YZ in seed_map,
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check(
        "no-larger-ball",
        BALL_SQ == 9 and all(dot(site, site) <= 9 for site in ticks),
    )
    checks.check("note-claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "note-reports-M-and-neighbor-read-both-cuts",
        "t(A)=2" in note
        and "t(B)=1" in note
        and "t(C)=3" in note
        and "t(D)=2" in note
        and "M(A, τ1) = {−e_3}" in note
        and "M(B, τ1) = {+e_1}" in note
        and "M(C, τ1) = {+e_1}" in note
        and "M(D, τ1) = {−e_3}" in note
        and "M(A, τ2) = {−e_3}" in note
        and "M(B, τ2) = {+e_1}" in note
        and "M(C, τ2) = {+e_1}" in note
        and "M(D, τ2) = {−e_3}" in note
        and "neighbor-read(A, τ1) = hold" in note
        and "neighbor-read(B, τ1) = hold" in note
        and "neighbor-read(C, τ1) = hold" in note
        and "neighbor-read(D, τ1) = hold" in note
        and "neighbor-read(A, τ2) = hold" in note
        and "neighbor-read(B, τ2) = hold" in note
        and "neighbor-read(C, τ2) = hold" in note
        and "neighbor-read(D, τ2) = hold" in note,
    )
    checks.check(
        "note-reports-formed-neighbors-both-cuts",
        "formed 6-NN of A at τ1: (2, 0, 0)={+e_1}, (0, 0, 0)={+e_1}, (1, 1, 0)={−e_3}, (1, -1, 0)={+e_1}, (1, 0, 1)={+e_1}, (1, 0, -1)={+e_1}"
        in note
        and "formed 6-NN of B at τ1: (2, 1, 1)=UNDEFINED, (0, 1, 1)={−e_2}, (1, 2, 1)={+e_2}, (1, 0, 1)={+e_1}, (1, 1, 2)={+e_1, +e_3}, (1, 1, 0)={−e_3}"
        in note
        and "formed 6-NN of C at τ1: (1, 0, 0)={−e_3}, (2, 1, 0)={+e_1}, (2, -1, 0)={−e_2, −e_3}, (2, 0, 1)={+e_2, +e_3, −e_3}, (2, 0, -1)={−e_3}"
        in note
        and "formed 6-NN of D at τ1: (2, 1, 0)={+e_1}, (0, 1, 0)={−e_1}, (1, 2, 0)={+e_1}, (1, 0, 0)={−e_3}, (1, 1, 1)={+e_1}, (1, 1, -1)={+e_1}"
        in note
        and "formed 6-NN of A at τ2: (2, 0, 0)={+e_1}, (0, 0, 0)={+e_1}, (1, 1, 0)={−e_3}, (1, -1, 0)={+e_1}, (1, 0, 1)={+e_1}, (1, 0, -1)={+e_1}"
        in note
        and "matching 6-NN of A at τ1: (1, 1, 0)" in note
        and "matching 6-NN of B at τ1: (1, 0, 1)" in note
        and "matching 6-NN of C at τ1: (2, 1, 0)" in note
        and "matching 6-NN of D at τ1: (1, 0, 0)" in note
        and "matching 6-NN of A at τ2: (1, 1, 0)" in note
        and "matching 6-NN of B at τ2: (1, 0, 1)" in note
        and "matching 6-NN of C at τ2: (2, 1, 0)" in note
        and "matching 6-NN of D at τ2: (1, 0, 0)" in note,
    )
    checks.check(
        "note-reports-reverse-face-composition",
        "Reverse neighbor-read at τ1: hold" in note
        and "Reverse neighbor-read at τ2: hold" in note
        and "Face neighbor-read at τ1: hold" in note
        and "Face neighbor-read at τ2: hold" in note
        and "Composition of neighbor-read: hold" in note
        and "Reverse holds at τ1 and at τ2." in note
        and "Face holds at τ1 and at τ2." in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in normalized_note.lower()
        and "Do not write into Admissibility." in note
        and "Do not attach L1." in note,
    )
    checks.check(
        "note-not-cover-or-same-lock-or-one-cut-leftover",
        "not leftover of nm2readx one-cut neighbor-read" in normalized_note
        and "not leftover of nm2axpx forall-perp" in normalized_note
        and "not leftover of nm2axx axis-cover" in normalized_note
        and "not leftover of two-axis same-lock z-probe neighbor-read"
        in normalized_note
        and "not leftover of two-axis same-lock x-probe neighbor-read"
        in normalized_note
        and "not leftover of nm2t2x M freeze" in normalized_note
        and "not leftover of R-style" in normalized_note,
    )
    checks.check(
        "note-no-global-T",
        "no global T" in normalized_note
        and "τ1(q)=t(q)+1" in note.replace(" ", "")
        and "τ2(q)=t(q)+2" in note.replace(" ", ""),
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
        and "Occupancy `n` is not used" in note
        and "neighbor-read" in normalized_note,
    )
    checks.check(
        "note-uniqueness-not-required",
        "Uniqueness is not required." in normalized_note
        and "Mixed remains a set." in note,
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
        '    "docs/TWO_AXIS_OPPOSITE_XPROBE_NEIGHBOR_READ_INCOMING_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and "composition_report" in defined_fns
        and "formed_neighbor_incoming" in defined_fns
        and "form" in defined_fns
        and not any("occup" in name for name in defined_fns),
    )
    checks.check(
        "source-formation-is-perp-step-queue",
        "from collections import deque" in source
        and "while queue:" in source
        and "require_perp" in source
        and ticks[PROBES["A"]] == 2
        and set(ticks) <= host,
    )
    checks.check(
        "neighbor-read-not-cover-or-same-lock-z",
        reverse1 == "hold"
        and face1 == "hold"
        and composition == "hold"
        and reads1["A"] == "hold"
        and reads1["B"] == "hold"
        and reads1["C"] == "hold"
        and reads1["D"] == "hold"
        and sl_z_reverse1 == "hold"
        and ticks[PROBES["A"]] != sl_ticks[Z_PROBES["A"]]
        and formed1["B"][1][1] == frozenset({NEG_E2})
        and sl_b_partner == frozenset({E2}),
    )
    _ = (formed_display, matching_display, ysym_ticks)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
