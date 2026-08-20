#!/usr/bin/env python3
"""Two-seed meeting-set variance of c2d4 versus ℓ¹ on B_12(0)∪B_12((2,0,0)).

Two seed-relative Dijkstras under the named cost-2 max≥4 out-face hop-cost.
ℓ¹ arrivals are taxicab. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from heapq import heappop, heappush
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/COST2_MAX4_OUT_FACE_TWO_SEED_MEET_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_MAX4_OUT_FACE_TWO_SEED_MEET_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Two-seed meeting-set arrival-speed variance under the named "
    "cost-2 max≥4 out-face hop-cost on B_12(0)∪B_12((2,0,0)) is reported. "
    "Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
S0 = (0, 0, 0)
S1 = (2, 0, 0)
RADIUS = 12
UNION_COUNT = 3203
BALL_COUNT = 2625
EQUAL_C2D4 = 385
EQUAL_L1 = 265
MEET_SITE = (1, 0, 0)
T_C2D4 = 3
T_L1 = 1
MEET_CARD = 1
Q_C2D4 = (1, 9)
Q_L1 = (1, 1)
AXIS = (1, 0, 0)
FACE = (1, 1, 0)
BODY = (1, 1, 1)
UNIT_OUT = (2, 1, 0)
DF_OUT_SRC = (2, 2, 0)
DF_OUT_DST = (3, 2, 0)
MAX3_OUT_SRC = (3, 2, 0)
MAX3_OUT_DST = (4, 2, 0)
MAX4_OUT_SRC = (4, 2, 0)
MAX4_OUT_DST = (5, 2, 0)
MAX4_LIVE_SRC = (4, 1, 0)
MAX4_LIVE_DST = (5, 1, 0)
DIJKSTRA_CALLS = 0

Point = tuple[int, int, int]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1(point: Point, seed: Point = S0) -> int:
    return abs(point[0] - seed[0]) + abs(point[1] - seed[1]) + abs(point[2] - seed[2])


def l2sq(point: Point, seed: Point = S0) -> int:
    return (point[0] - seed[0]) ** 2 + (point[1] - seed[1]) ** 2 + (point[2] - seed[2]) ** 2


def support_size(point: Point) -> int:
    return int(point[0] != 0) + int(point[1] != 0) + int(point[2] != 0)


def least_nonzero_abs(point: Point) -> int | None:
    nonzero = [abs(coord) for coord in point if coord != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_coord_count(point: Point) -> int:
    return int(abs(point[0]) == 1) + int(abs(point[1]) == 1) + int(abs(point[2]) == 1)


def max_abs(point: Point) -> int:
    return max(abs(coord) for coord in point)


def shifted(point: Point, seed: Point) -> Point:
    return (point[0] - seed[0], point[1] - seed[1], point[2] - seed[2])


def nu_cost(source: Point, target: Point) -> int:
    sigma_v = support_size(source)
    sigma_w = support_size(target)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(source: Point, target: Point) -> int:
    if nu_cost(source, target) == 3:
        return 3
    if support_size(source) == 2 and support_size(target) == 2 and least_nonzero_abs(target) == 1:
        return 3
    return 1


def rho3_cost(source: Point, target: Point) -> int:
    if mu_cost(source, target) == 3:
        return 3
    if support_size(source) == 3 and support_size(target) == 3 and unit_coord_count(target) == 2:
        return 3
    return 1


def omega_extra(source: Point, target: Point) -> bool:
    return (
        support_size(source) == 2
        and support_size(target) == 2
        and max_abs(target) > max_abs(source)
    )


def df_extra(source: Point, target: Point) -> bool:
    return omega_extra(source, target) and max_abs(source) >= 2


def d3_extra(source: Point, target: Point) -> bool:
    return omega_extra(source, target) and max_abs(source) >= 3


def d4_extra(source: Point, target: Point) -> bool:
    return omega_extra(source, target) and max_abs(source) >= 4


def omega_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3 or omega_extra(source, target):
        return 3
    return 1


def d3_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3 or d3_extra(source, target):
        return 3
    return 1


def d4_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3 or d4_extra(source, target):
        return 3
    return 1


def c2d3_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if d3_extra(source, target):
        return 2
    return 1


def c2d4_cost(source: Point, target: Point) -> int:
    if rho3_cost(source, target) == 3:
        return 3
    if d4_extra(source, target):
        return 2
    return 1


def c2d4_from_seed(source: Point, target: Point, seed: Point) -> int:
    return c2d4_cost(shifted(source, seed), shifted(target, seed))


def ball(center: Point, radius: int) -> list[Point]:
    sites: list[Point] = []
    extent = range(-radius, radius + 1)
    cx, cy, cz = center
    for dx, dy, dz in product(extent, repeat=3):
        if abs(dx) + abs(dy) + abs(dz) <= radius:
            sites.append((cx + dx, cy + dy, cz + dz))
    return sites


def union_sites() -> list[Point]:
    return sorted(set(ball(S0, RADIUS)) | set(ball(S1, RADIUS)))


def neighbors(site: Point, site_set: set[Point]) -> list[Point]:
    out: list[Point] = []
    x, y, z = site
    for dx, dy, dz in NEIGH:
        nxt = (x + dx, y + dy, z + dz)
        if nxt in site_set:
            out.append(nxt)
    return out


def dijkstra(sites: list[Point], seed: Point, cost_fn) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    site_set = set(sites)
    dist = {seed: 0}
    heap: list[tuple[int, Point]] = [(0, seed)]
    while heap:
        current, site = heappop(heap)
        if current != dist[site]:
            continue
        for nxt in neighbors(site, site_set):
            trial = current + cost_fn(site, nxt)
            prior = dist.get(nxt)
            if prior is None or trial < prior:
                dist[nxt] = trial
                heappush(heap, (trial, nxt))
    return dist


def equal_arrival_set(
    sites: list[Point],
    t0: dict[Point, int],
    t1: dict[Point, int],
) -> tuple[Point, ...]:
    return tuple(sorted(site for site in sites if t0[site] == t1[site]))


def meeting_set(
    sites: list[Point],
    t0: dict[Point, int],
    t1: dict[Point, int],
) -> tuple[Point, ...]:
    site_set = set(sites)
    found: list[Point] = []
    for site in sites:
        if t0[site] != t1[site]:
            continue
        earlier = False
        for nxt in neighbors(site, site_set):
            if t0[nxt] < t0[site] and t1[nxt] < t1[site]:
                earlier = True
                break
        if not earlier:
            found.append(site)
    return tuple(sorted(found))


def second_moment(meet: tuple[Point, ...], t0: dict[Point, int]) -> tuple[int, int]:
    moment = Fraction(0)
    for site in meet:
        arrival = t0[site]
        moment += Fraction(l2sq(site, S0), arrival * arrival)
    moment /= len(meet)
    return moment.numerator, moment.denominator


def arrival_speed_variance(meet: tuple[Point, ...], t0: dict[Point, int]) -> Fraction:
    if len(meet) <= 1:
        return Fraction(0)
    speeds = [Fraction(l2sq(site, S0), t0[site] * t0[site]) ** Fraction(1, 2) for site in meet]
    mean = sum(speeds) / len(speeds)
    return sum((speed - mean) ** 2 for speed in speeds) / len(speeds)


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
            continue
        if not isinstance(node.value, ast.Tuple):
            return None
        out: list[str] = []
        for elt in node.value.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, str):
                return None
            out.append(elt.value)
        return tuple(out)
    return None


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = " ".join(note.split())
    normalized_axiom = " ".join(axiom.split())

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor union B_12(0)∪B_12((2,0,0)) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and two Dijkstras; no fit and "
        "no third graph search"
    )
    print(
        "claim_boundary: two-seed meeting-set variance is displayed, not adopted"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are the source note and the current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "claim-scope",
        "note claim_scope matches the displayed scoring statement",
        CLAIM_SCOPE in note and CLAIM_SCOPE in normalized_note,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "c2d4 is not written into Admissibility",
        "Do not write c2d4 into Admissibility." in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1." in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note
        and "Uniqueness not required" in note
        and "unique hop-cost" not in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note or token in source]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the note and runner",
        forbidden_hits == [],
    )
    checks.check(
        "cache-false",
        "the note records cache_write false",
        "cache_write: false" in note,
    )

    sites = union_sites()
    site_set = set(sites)
    b0 = ball(S0, RADIUS)
    b1 = ball(S1, RADIUS)
    checks.check(
        "union-cardinality",
        "the executed domain is the 3203-site union B_12(0)∪B_12((2,0,0))",
        len(sites) == UNION_COUNT
        and len(b0) == BALL_COUNT
        and len(b1) == BALL_COUNT
        and S0 in site_set
        and S1 in site_set
        and MEET_SITE in site_set
        and MAX3_OUT_SRC in site_set
        and MAX3_OUT_DST in site_set
        and MAX4_OUT_SRC in site_set
        and MAX4_OUT_DST in site_set
        and (12, 0, 0) in site_set
        and (12, 0, 0) not in set(ball(S0, 6)) | set(ball(S1, 6))
        and all(l1(v, S0) <= RADIUS or l1(v, S1) <= RADIUS for v in sites),
    )

    t0 = dijkstra(sites, S0, lambda src, dst: c2d4_from_seed(src, dst, S0))
    t1 = dijkstra(sites, S1, lambda src, dst: c2d4_from_seed(src, dst, S1))
    t0_l1 = {site: l1(site, S0) for site in sites}
    t1_l1 = {site: l1(site, S1) for site in sites}
    equal_c2d4 = equal_arrival_set(sites, t0, t1)
    equal_l1 = equal_arrival_set(sites, t0_l1, t1_l1)
    meet_c2d4 = meeting_set(sites, t0, t1)
    meet_l1 = meeting_set(sites, t0_l1, t1_l1)
    q_c2d4 = second_moment(meet_c2d4, t0)
    q_l1 = second_moment(meet_l1, t0_l1)
    var_c2d4 = arrival_speed_variance(meet_c2d4, t0)
    var_l1 = arrival_speed_variance(meet_l1, t0_l1)
    t320 = t0[MAX3_OUT_SRC]
    t420 = t0[MAX3_OUT_DST]
    t520 = t0[MAX4_OUT_DST]

    print(f"n_sites {len(sites)}")
    print(f"|E_c2d4| {len(equal_c2d4)}")
    print(f"meet_c2d4 {meet_c2d4}")
    print(f"t_c2d4 {t0[MEET_SITE]}")
    print(f"|M_c2d4| {len(meet_c2d4)}")
    print(f"|E_l1| {len(equal_l1)}")
    print(f"meet_l1 {meet_l1}")
    print(f"t_l1 {t0_l1[MEET_SITE]}")
    print(f"|M_l1| {len(meet_l1)}")
    print(f"t0(3,2,0) {t320}")
    print(f"t0(4,2,0) {t420}")
    print(f"t0(5,2,0) {t520}")
    print(f"Q_c2d4 {q_c2d4[0]}/{q_c2d4[1]}")
    print(f"Q_l1 {q_l1[0]}/{q_l1[1]}")
    print(f"var_c2d4 {var_c2d4}")
    print(f"var_l1 {var_l1}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(
        f"c2d4_unit_out {c2d4_cost(FACE, UNIT_OUT)} "
        f"rho3_unit_out {rho3_cost(FACE, UNIT_OUT)} "
        f"d4_extra_unit_out {int(d4_extra(FACE, UNIT_OUT))} "
        f"d3_extra_unit_out {int(d3_extra(FACE, UNIT_OUT))}"
    )
    print(
        f"c2d4_df_out {c2d4_cost(DF_OUT_SRC, DF_OUT_DST)} "
        f"omega_df_out {omega_cost(DF_OUT_SRC, DF_OUT_DST)} "
        f"d4_extra_df_out {int(d4_extra(DF_OUT_SRC, DF_OUT_DST))} "
        f"df_extra_df_out {int(df_extra(DF_OUT_SRC, DF_OUT_DST))}"
    )
    print(
        f"c2d4_max3_out {c2d4_cost(MAX3_OUT_SRC, MAX3_OUT_DST)} "
        f"c2d3_max3_out {c2d3_cost(MAX3_OUT_SRC, MAX3_OUT_DST)} "
        f"rho3_max3_out {rho3_cost(MAX3_OUT_SRC, MAX3_OUT_DST)} "
        f"d4_extra_max3_out {int(d4_extra(MAX3_OUT_SRC, MAX3_OUT_DST))} "
        f"d3_extra_max3_out {int(d3_extra(MAX3_OUT_SRC, MAX3_OUT_DST))}"
    )
    print(
        f"c2d4_max4_out {c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"d4_max4_out {d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"rho3_max4_out {rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST)} "
        f"d4_extra_max4_out {int(d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST))}"
    )

    checks.check(
        "two-dijkstras",
        "exactly two Dijkstras ran and every union site is reached",
        DIJKSTRA_CALLS == 2 and len(t0) == UNION_COUNT and len(t1) == UNION_COUNT,
    )
    checks.check(
        "l1-taxicab",
        "ℓ¹ arrivals equal the taxicab norms from each seed",
        all(t0_l1[site] == l1(site, S0) and t1_l1[site] == l1(site, S1) for site in sites),
    )
    checks.check(
        "meeting-set",
        "lex-first c2d4 meeting site is (1,0,0) at t=3 with |M|=1",
        meet_c2d4 == (MEET_SITE,)
        and t0[MEET_SITE] == T_C2D4
        and t1[MEET_SITE] == T_C2D4
        and len(meet_c2d4) == MEET_CARD,
    )
    checks.check(
        "l1-meeting-set",
        "lex-first ℓ¹ meeting site is (1,0,0) at t=1 with |M|=1",
        meet_l1 == (MEET_SITE,)
        and t0_l1[MEET_SITE] == T_L1
        and t1_l1[MEET_SITE] == T_L1
        and len(meet_l1) == MEET_CARD,
    )
    checks.check(
        "singleton-meeting",
        "|M|=1 on the B_12 union under c2d4 and under ℓ¹; equal-arrival is 385 versus 265",
        len(meet_c2d4) == 1
        and len(meet_l1) == 1
        and len(equal_c2d4) == EQUAL_C2D4
        and len(equal_l1) == EQUAL_L1
        and len(equal_c2d4) > 1
        and "`385`" in note,
    )
    checks.check(
        "variances",
        "both singleton meeting-set arrival-speed variances are 0",
        q_c2d4 == Q_C2D4
        and q_l1 == Q_L1
        and var_c2d4 == 0
        and var_l1 == 0
        and "`0`" in note
        and "`1/9`" in note
        and "`1`" in note,
    )
    checks.check(
        "note-records-meeting",
        "note records the lex-first site, its t, and |M|",
        "`(1,0,0)`" in note
        and "`3`" in note
        and "`|M|=1`" in note
        and "## Theorem 1" in note
        and "## Theorem 2" in note
        and "## Theorem 3" in note,
    )
    checks.check(
        "seed-relative",
        "c2d4 is grown from each seed: exit from (2,0,0) costs 3, not the global 1→2 price",
        c2d4_from_seed(S1, (2, 1, 0), S1) == 3
        and c2d4_cost(S1, (2, 1, 0)) == 1
        and c2d4_from_seed(S0, AXIS, S0) == 3
        and c2d4_from_seed(S1, MEET_SITE, S1) == 3
        and "grown from each seed" in note,
    )
    checks.check(
        "c2d4-clauses",
        "seed-exit, axis, drop, corridor-slide, and ridge-slide cost 3; max>=4 out-face costs 2; max>=3 out extra is idle; 1-to-2 and small 2-to-3 cost 1",
        c2d4_cost((0, 0, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 0, 0), (2, 0, 0)) == 3
        and c2d4_cost((1, 1, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 1, 0), (2, 1, 0)) == 3
        and c2d4_cost((1, 1, 1), (2, 1, 1)) == 3
        and c2d4_cost((4, 2, 0), (5, 2, 0)) == 2
        and c2d4_cost((4, 1, 0), (5, 1, 0)) == 3
        and c2d4_cost((1, 0, 0), (1, 1, 0)) == 1
        and c2d4_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d4_cost((2, 2, 2), (3, 2, 2)) == 1
        and c2d4_cost((2, 2, 0), (3, 2, 0)) == 1
        and c2d4_cost((3, 2, 0), (4, 2, 0)) == 1
        and not d4_extra((3, 2, 0), (4, 2, 0))
        and not d4_extra((2, 2, 0), (3, 2, 0))
        and not d4_extra((1, 1, 0), (2, 1, 0)),
    )
    checks.check(
        "hop-unit-out-skipped",
        "the extra clause skips (1,1,0) to (2,1,0); rho3 already prices that hop",
        not d4_extra(FACE, UNIT_OUT)
        and omega_extra(FACE, UNIT_OUT)
        and max_abs(FACE) == 1
        and rho3_cost(FACE, UNIT_OUT) == 3
        and c2d4_cost(FACE, UNIT_OUT) == 3
        and FACE in site_set
        and UNIT_OUT in site_set,
    )
    checks.check(
        "hop-df-out-skipped",
        "the named 2-to-2 growing-max clause with source max at least 4 skips (2,2,0) to (3,2,0)",
        not d4_extra(DF_OUT_SRC, DF_OUT_DST)
        and df_extra(DF_OUT_SRC, DF_OUT_DST)
        and omega_cost(DF_OUT_SRC, DF_OUT_DST) == 3
        and rho3_cost(DF_OUT_SRC, DF_OUT_DST) == 1
        and c2d4_cost(DF_OUT_SRC, DF_OUT_DST) == 1
        and max_abs(DF_OUT_SRC) == 2
        and max_abs(DF_OUT_DST) > max_abs(DF_OUT_SRC)
        and DF_OUT_SRC in site_set
        and DF_OUT_DST in site_set,
    )
    checks.check(
        "hop-max3-out-skipped",
        "the named 2-to-2 growing-max clause with source max at least 4 skips (3,2,0) to (4,2,0)",
        not d4_extra(MAX3_OUT_SRC, MAX3_OUT_DST)
        and d3_extra(MAX3_OUT_SRC, MAX3_OUT_DST)
        and rho3_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and c2d4_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and c2d3_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 2
        and max_abs(MAX3_OUT_SRC) == 3
        and max_abs(MAX3_OUT_DST) > max_abs(MAX3_OUT_SRC)
        and MAX3_OUT_SRC in site_set
        and MAX3_OUT_DST in site_set,
    )
    checks.check(
        "hop-max4-out-clause",
        "the named 2-to-2 growing-max clause with source max at least 4 prices (4,2,0) to (5,2,0) at 2",
        d4_extra(MAX4_OUT_SRC, MAX4_OUT_DST)
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 3
        and omega_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 3
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and max_abs(MAX4_OUT_SRC) >= 4
        and max_abs(MAX4_OUT_DST) > max_abs(MAX4_OUT_SRC)
        and MAX4_OUT_SRC in site_set
        and MAX4_OUT_DST in site_set,
    )
    in_union_new = 0
    for site in sites:
        for nxt in neighbors(site, site_set):
            src_s0 = shifted(site, S0)
            dst_s0 = shifted(nxt, S0)
            if (
                d4_extra(src_s0, dst_s0)
                and rho3_cost(src_s0, dst_s0) == 1
                and c2d4_cost(src_s0, dst_s0) == 2
            ):
                in_union_new += 1
    checks.check(
        "max4-out-live-on-union",
        "nearest-neighbor hops inside the union trigger the extra cost-2 clause",
        in_union_new > 0
        and MAX4_OUT_SRC in site_set
        and MAX4_OUT_DST in site_set
        and "cannot price the max≥4 out-face hop" in note,
    )
    checks.check(
        "skipped-max3-arrival",
        "the same Dijkstra records t(3,2,0)=9 and t(4,2,0)=10 matching the skipped extra hop of cost 1",
        t320 == 9
        and t420 == 10
        and t320 + c2d4_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == t420
        and "t(3,2,0) = 9" in note
        and "t(4,2,0) = 10" in note,
    )
    checks.check(
        "live-arrival-uses-cost-2",
        "the same Dijkstra records t(4,2,0)=10 and t(5,2,0)=12 matching the extra hop of cost 2",
        t420 == 10
        and t520 == 12
        and t420 + c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == t520
        and "t(4,2,0) = 10" in note
        and "t(5,2,0) = 12" in note,
    )
    checks.check(
        "corridor-already-taxed",
        "the in-union hop (4,1,0) to (5,1,0) fires the extra clause but corridor-slide already prices it at 3",
        d4_extra(MAX4_LIVE_SRC, MAX4_LIVE_DST)
        and rho3_cost(MAX4_LIVE_SRC, MAX4_LIVE_DST) == 3
        and c2d4_cost(MAX4_LIVE_SRC, MAX4_LIVE_DST) == 3
        and least_nonzero_abs(MAX4_LIVE_DST) == 1
        and MAX4_LIVE_SRC in site_set
        and MAX4_LIVE_DST in site_set,
    )
    checks.check(
        "not-leftover-of-l1",
        "c2d4 meeting time is 3 while ℓ¹ meeting time is 1, so the c2d4 score is not a leftover of ℓ¹",
        t0[MEET_SITE] == 3
        and t0_l1[MEET_SITE] == 1
        and t0[MEET_SITE] != t0_l1[MEET_SITE]
        and "not a leftover" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "rho3 prices the max≥4 out-face hop at 1 while c2d4 prices it at 2",
        c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 1
        and t520 != t420 + rho3_cost(MAX4_OUT_SRC, MAX4_OUT_DST)
        and "cannot price the max≥4 out-face hop" in note,
    )
    checks.check(
        "not-leftover-of-d4-or-omega",
        "d4 and omega price the max≥4 out-face hop at 3, while c2d4 prices it at 2 and skips (3,2,0)->(4,2,0)",
        d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 3
        and omega_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 3
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and omega_cost(DF_OUT_SRC, DF_OUT_DST) == 3
        and c2d4_cost(DF_OUT_SRC, DF_OUT_DST) == 1
        and c2d4_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and t420 + d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) != t520
        and "parent `d4`" in note
        and "skips" in note,
    )
    checks.check(
        "not-leftover-of-c2d3",
        "c2d3 prices the max≥3 out-face hop at 2 while c2d4 prices it at 1",
        c2d3_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 2
        and c2d4_cost(MAX3_OUT_SRC, MAX3_OUT_DST) == 1
        and t320 + c2d3_cost(MAX3_OUT_SRC, MAX3_OUT_DST) != t420
        and "cost-2 max≥3" in note,
    )
    checks.check(
        "not-leftover-of-b6",
        "the B_12 union is larger than the B_6 union and the equal-arrival set is 385, but M stayed a singleton",
        (12, 0, 0) in site_set
        and l1((12, 0, 0), S0) == 12
        and len(equal_c2d4) == 385
        and len(meet_c2d4) == 1
        and "absent from the radius-`6` union" in note
        and "`385`" in note,
    )
    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    checks.check(
        "source-axioms",
        "current Lattice, Admissibility, and Record wording is pinned",
        lattice_sentence in normalized_axiom
        and lattice_sentence in note
        and admissibility_sentence in normalized_axiom
        and admissibility_sentence in normalized_note
        and formation_boundary in normalized_axiom
        and formation_boundary in normalized_note
        and all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "thm3-exact",
        "Theorem 3 uses the required non-adoption sentences",
        "Do not write c2d4 into Admissibility." in note and "Do not attach L1." in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on the B_12 union and proposes no axiom edit",
        "B_12(0)∪B_12((2,0,0))" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "Two Dijkstras" in note,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: meeting-set arrivals are reported only on the computed M.")
    print("lattice_wide: checked and not executed — the search stays inside the union.")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
