#!/usr/bin/env python3
"""Two-seed meeting-set variance of ρ3 versus ℓ¹ on B_12(0)∪B_12((2,0,0)).

Two seed-relative Dijkstras under ρ3. ℓ¹ arrivals are taxicab. No cache write.
No axiom edit.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from heapq import heappop, heappush
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/RIDGE_SLIDE_TWO_SEED_MEET_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/RIDGE_SLIDE_TWO_SEED_MEET_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Two-seed meeting-set arrival-speed variance under the named "
    "ridge-slide hop-cost on B_12(0)∪B_12((2,0,0)) is compared "
    "to ℓ¹. Displayed, not adopted."
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
EQUAL_RHO3 = 313
EQUAL_L1 = 265
MEET_SITE = (1, 0, 0)
T_RHO3 = 3
T_L1 = 1
MEET_CARD = 1
Q_RHO3 = (1, 9)
Q_L1 = (1, 1)
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


def rho3_from_seed(source: Point, target: Point, seed: Point) -> int:
    return rho3_cost(shifted(source, seed), shifted(target, seed))


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
    speeds = [Fraction(l2sq(site, S0)).sqrt() / t0[site] for site in meet]
    mean = sum(speeds, Fraction(0)) / len(meet)
    return sum((speed - mean) ** 2 for speed in speeds) / len(meet)


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
        CLAIM_SCOPE in normalized_note,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ρ3 is not written into Admissibility",
        "Do not write `ρ3` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note and "Uniqueness not required" in note,
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
        and (12, 0, 0) in site_set
        and (12, 0, 0) not in set(ball(S0, 6)) | set(ball(S1, 6))
        and all(l1(v, S0) <= RADIUS or l1(v, S1) <= RADIUS for v in sites),
    )

    t0 = dijkstra(sites, S0, lambda src, dst: rho3_from_seed(src, dst, S0))
    t1 = dijkstra(sites, S1, lambda src, dst: rho3_from_seed(src, dst, S1))
    t0_l1 = {site: l1(site, S0) for site in sites}
    t1_l1 = {site: l1(site, S1) for site in sites}
    equal_rho3 = equal_arrival_set(sites, t0, t1)
    equal_l1 = equal_arrival_set(sites, t0_l1, t1_l1)
    meet_rho3 = meeting_set(sites, t0, t1)
    meet_l1 = meeting_set(sites, t0_l1, t1_l1)
    q_rho3 = second_moment(meet_rho3, t0)
    q_l1 = second_moment(meet_l1, t0_l1)
    var_rho3 = arrival_speed_variance(meet_rho3, t0)
    var_l1 = arrival_speed_variance(meet_l1, t0_l1)
    named = {"l1": var_l1, "rho3": var_rho3}
    lex_first = min(named, key=lambda name: (named[name], name))

    print(f"n_sites {len(sites)}")
    print(f"|E_rho3| {len(equal_rho3)}")
    print(f"meet_rho3 {meet_rho3}")
    print(f"t_rho3 {t0[MEET_SITE]}")
    print(f"|M_rho3| {len(meet_rho3)}")
    print(f"|E_l1| {len(equal_l1)}")
    print(f"meet_l1 {meet_l1}")
    print(f"t_l1 {t0_l1[MEET_SITE]}")
    print(f"|M_l1| {len(meet_l1)}")
    print(f"Q_rho3 {q_rho3[0]}/{q_rho3[1]}")
    print(f"Q_l1 {q_l1[0]}/{q_l1[1]}")
    print(f"var_rho3 {var_rho3}")
    print(f"var_l1 {var_l1}")
    print(f"lex_first_minimizer {lex_first}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "two-dijkstras",
        "exactly two Dijkstras ran and every union site is reached",
        DIJKSTRA_CALLS == 2 and len(t0) == UNION_COUNT and len(t1) == UNION_COUNT,
    )
    checks.check(
        "l1-taxicab",
        "unit hop-cost arrivals equal the taxicab norms from each seed",
        all(t0_l1[site] == l1(site, S0) and t1_l1[site] == l1(site, S1) for site in sites),
    )
    checks.check(
        "meeting-set",
        "lex-first ρ3 meeting site is (1,0,0) at t=3 with |M|=1",
        meet_rho3 == (MEET_SITE,)
        and t0[MEET_SITE] == T_RHO3
        and t1[MEET_SITE] == T_RHO3
        and len(meet_rho3) == MEET_CARD,
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
        "|M|=1 on the B_12 union under ρ3 and under ℓ¹; equal-arrival is 313 versus 265",
        len(meet_rho3) == 1
        and len(meet_l1) == 1
        and len(equal_rho3) == EQUAL_RHO3
        and len(equal_l1) == EQUAL_L1
        and len(equal_rho3) > 1
        and "`313`" in note,
    )
    checks.check(
        "variances",
        "both singleton meeting-set arrival-speed variances are 0",
        q_rho3 == Q_RHO3
        and q_l1 == Q_L1
        and var_rho3 == 0
        and var_l1 == 0
        and "`0`" in note
        and "`1/9`" in note
        and "`1`" in note,
    )
    checks.check(
        "lex-first-minimizer",
        "the lex-first minimizer among the tied scores is ℓ¹",
        lex_first == "l1" and "lex-first minimizer" in note and "`ℓ¹`" in note,
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
        "ρ3 is grown from each seed: exit from (2,0,0) costs 3, not the global 1→2 price",
        rho3_from_seed(S1, (2, 1, 0), S1) == 3
        and rho3_cost(S1, (2, 1, 0)) == 1
        and rho3_from_seed(S0, (1, 0, 0), S0) == 3
        and rho3_from_seed(S1, MEET_SITE, S1) == 3
        and "grown from each seed" in note,
    )
    checks.check(
        "seed-and-ridge-slide-clauses",
        "ν clauses, corridor-slide, and ridge 3→3 cost 3; 1→2, 2→3, and non-ridge 3→3 cost 1",
        rho3_cost((0, 0, 0), (1, 0, 0)) == 3
        and rho3_cost((1, 0, 0), (2, 0, 0)) == 3
        and rho3_cost((1, 0, 0), (1, 1, 0)) == 1
        and rho3_cost((1, 1, 0), (1, 0, 0)) == 3
        and rho3_cost((1, 1, 0), (1, 1, 1)) == 1
        and rho3_cost((1, 1, 0), (2, 1, 0)) == 3
        and rho3_cost((1, 1, 1), (2, 1, 1)) == 3
        and rho3_cost((1, -1, -1), (2, -1, -1)) == 3
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and rho3_cost((2, 2, 2), (3, 2, 2)) == 1,
    )
    checks.check(
        "not-leftover-of-l1",
        "ρ3 meeting time is 3 while ℓ¹ meeting time is 1, so the ρ3 score is not a unit-cost leftover",
        t0[MEET_SITE] == 3
        and t0_l1[MEET_SITE] == 1
        and t0[MEET_SITE] != t0_l1[MEET_SITE]
        and "not a leftover" in note,
    )
    checks.check(
        "not-leftover-of-mu",
        "ρ3 prices the ridge 3→3 hop at 3 while μ prices it at 1, and t(1,2,2)=9",
        rho3_cost((1, 1, 1), (2, 1, 1)) == 3
        and mu_cost((1, 1, 1), (2, 1, 1)) == 1
        and t0[(1, 2, 2)] == 9
        and t1[(1, 2, 2)] == 9
        and "cannot price the ridge slide" in note
        and "`9`" in note,
    )
    checks.check(
        "not-leftover-of-b6",
        "the B_12 union is larger than the B_6 union and the equal-arrival set is 313, but M stayed a singleton",
        (12, 0, 0) in site_set
        and l1((12, 0, 0), S0) == 12
        and len(equal_rho3) == 313
        and len(meet_rho3) == 1
        and "absent from the radius-`6` union" in note
        and "`313`" in note,
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
        and "ρ3(v→w)" not in axiom
        and "μ(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
