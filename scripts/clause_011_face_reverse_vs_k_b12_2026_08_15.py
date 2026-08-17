#!/usr/bin/env python3
"""Face reverse versus integer scale k under the named (0,1,1) hop-cost on B_12(0).

One origin Dijkstra. Seed-exit is cheap; both-weights-one and support-drop
cost 3. The rule is displayed, not adopted. No cache write. No axiom edit.
"""

from __future__ import annotations

from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CLAUSE_011_FACE_REVERSE_VS_K_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_FACE_REVERSE_VS_K_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Face-diagonal reverse versus integer scale k under the named "
    "(0,1,1) hop-cost on B_12(0) is reported for k=1..6. "
    "Displayed, not adopted."
)
RADIUS = 12
SCALES = (1, 2, 3, 4, 5, 6)
ORIGIN = (0, 0, 0)
CLAUSE_011 = (0, 1, 1)
SHIFTS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
DIJKSTRA_CALLS = 0


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


Point = tuple[int, int, int]


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1_norm(site: Point) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def l2sq(site: Point) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def inward_weight(site: Point) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


def ball_sites(radius: int = RADIUS) -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


BALL = ball_sites()


def neighbors(site: Point) -> tuple[Point, ...]:
    return tuple(dest for shift in SHIFTS if (dest := add(site, shift)) in BALL)


def hop_clauses(src: Point, dest: Point) -> tuple[bool, bool, bool]:
    source_weight = inward_weight(src)
    dest_weight = inward_weight(dest)
    seed_exit = source_weight == 0
    both_weights_one = source_weight == 1 and dest_weight == 1
    support_drop = dest_weight < source_weight
    return seed_exit, both_weights_one, support_drop


def hop_cost(src: Point, dest: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> int:
    seed_exit, both_weights_one, support_drop = hop_clauses(src, dest)
    seed_bit, axis_bit, drop_bit = clauses
    if (seed_bit and seed_exit) or (axis_bit and both_weights_one) or (drop_bit and support_drop):
        return 3
    return 1


def dijkstra_from(source: Point, clauses: tuple[int, int, int] = CLAUSE_011) -> dict[Point, int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
    dist = {source: 0}
    heap: list[tuple[int, Point]] = [(0, source)]
    while heap:
        cost, site = heappop(heap)
        if cost != dist[site]:
            continue
        for dest in neighbors(site):
            candidate = cost + hop_cost(site, dest, clauses)
            if dest not in dist or candidate < dist[dest]:
                dist[dest] = candidate
                heappush(heap, (candidate, dest))
    return dist


def path_cost(path: tuple[Point, ...], clauses: tuple[int, int, int] = CLAUSE_011) -> int:
    return sum(hop_cost(path[index], path[index + 1], clauses) for index in range(len(path) - 1))


def axis_site(k: int) -> Point:
    return (2 * k, 0, 0)


def face_site(k: int) -> Point:
    return (k, k, 0)


def is_reverse(times: dict[Point, int], k: int) -> bool:
    axis = axis_site(k)
    face = face_site(k)
    return times[axis] * times[axis] * l2sq(face) > times[face] * times[face] * l2sq(axis)


def main() -> int:
    checks = Checks()
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    axiom = (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("dijkstra_count_budget: 1")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print("external_scientific_inputs: current Lattice and Admissibility wording; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: named (0,1,1) hop-cost on B_12(0) with one origin Dijkstra")
    print("negative_scope: displayed, not adopted; not written into Admissibility; L1 not attached")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_FACE_REVERSE_VS_K_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and NOTE_REL in source
        and AXIOM_REL in source,
    )
    checks.check(
        "audit-input-literals",
        "AUDIT_INPUT_PATHS is a static two-string literal in this runner",
        'AUDIT_INPUT_PATHS = (\n    "docs/CLAUSE_011_FACE_REVERSE_VS_K_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_fixed = "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check(
        "source-admissibility",
        "current one-fixed-rule wording is pinned",
        admissibility_fixed in normalized_axiom
        and admissibility_sentence in normalized_axiom
        and admissibility_sentence in note,
    )
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    targets = tuple(axis_site(k) for k in SCALES) + tuple(face_site(k) for k in SCALES)
    checks.check("ball-cardinality", "B_12(0) has exactly 2625 integer sites", len(BALL) == 2625)
    checks.check(
        "targets-inside",
        "the twelve scored sites lie in B_12(0) and (12,1,0) does not",
        all(site in BALL for site in targets)
        and (12, 1, 0) not in BALL
        and l1_norm((12, 1, 0)) == 13
        and (10, 1, 0) in BALL
        and (8, 1, 0) in BALL,
    )
    checks.check(
        "clause-identity",
        "seed-exit is cheap and axis-one and support-drop cost 3",
        hop_cost(ORIGIN, (1, 0, 0)) == 1
        and hop_cost((1, 0, 0), (2, 0, 0)) == 3
        and hop_cost((1, 1, 0), (1, 0, 0)) == 3
        and hop_cost((1, 0, 0), (1, 1, 0)) == 1,
    )

    arrivals = dijkstra_from(ORIGIN)
    checks.check("one-dijkstra", "exactly one Dijkstra computation is used", DIJKSTRA_CALLS == 1)
    checks.check(
        "finite-times",
        "every in-ball target is reached by a finite path",
        all(site in arrivals for site in targets),
    )

    print("arrival_times:")
    for k in SCALES:
        for site in (axis_site(k), face_site(k)):
            time = arrivals[site]
            print(f"  t{site}={time}  t^2/|v|_2^2={time * time}/{l2sq(site)}")

    expected_times = {
        (2, 0, 0): 4,
        (4, 0, 0): 8,
        (6, 0, 0): 10,
        (8, 0, 0): 12,
        (10, 0, 0): 14,
        (12, 0, 0): 18,
        (1, 1, 0): 2,
        (2, 2, 0): 4,
        (3, 3, 0): 6,
        (4, 4, 0): 8,
        (5, 5, 0): 10,
        (6, 6, 0): 12,
    }
    for site, expected in expected_times.items():
        token = f"t({site[0]},{site[1]},{site[2]})={expected}"
        checks.check(
            f"time-{site[0]}{site[1]}{site[2]}",
            f"computed {token} is written in the note",
            token in note and arrivals[site] == expected,
            residual=arrivals[site],
        )

    expected_bits = {
        1: True,
        2: True,
        3: True,
        4: True,
        5: False,
        6: True,
    }
    comparison_tokens = {
        1: "4 t(1,1,0)^2 = 16 < 32 = 2 t(2,0,0)^2",
        2: "16 t(2,2,0)^2 = 256 < 512 = 8 t(4,0,0)^2",
        3: "36 t(3,3,0)^2 = 1296 < 1800 = 18 t(6,0,0)^2",
        4: "64 t(4,4,0)^2 = 4096 < 4608 = 32 t(8,0,0)^2",
        5: "100 t(5,5,0)^2 = 10000 > 9800 = 50 t(10,0,0)^2",
        6: "144 t(6,6,0)^2 = 20736 < 23328 = 72 t(12,0,0)^2",
    }
    print("reverse_bits:")
    bits: list[bool] = []
    for k in SCALES:
        axis = axis_site(k)
        face = face_site(k)
        bit = is_reverse(arrivals, k)
        bits.append(bit)
        ta, tb = arrivals[axis], arrivals[face]
        print(
            f"  k={k} {axis} vs {face}: reverse={bit} "
            f"({tb * tb}*{l2sq(axis)}={tb * tb * l2sq(axis)} vs "
            f"{ta * ta}*{l2sq(face)}={ta * ta * l2sq(face)})"
        )
        dens_ok = ta * ta * (2 * k * k) > tb * tb * (4 * k * k)
        checks.check(
            f"reverse-k{k}",
            f"k={k} reverse bit is {expected_bits[k]} and the comparison is written",
            bit is expected_bits[k]
            and dens_ok is expected_bits[k]
            and comparison_tokens[k] in note
            and inward_weight(face) > inward_weight(axis),
        )

    axis_k1 = (ORIGIN, (1, 0, 0), (2, 0, 0))
    face_k1 = (ORIGIN, (1, 0, 0), (1, 1, 0))
    axis_k2 = (ORIGIN, (1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 1, 0), (4, 0, 0))
    face_k2 = (ORIGIN, (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0))
    axis_k5 = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (6, 1, 0),
        (7, 1, 0),
        (8, 1, 0),
        (9, 1, 0),
        (10, 1, 0),
        (10, 0, 0),
    )
    face_k5 = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (5, 2, 0),
        (5, 3, 0),
        (5, 4, 0),
        (5, 5, 0),
    )
    axis_k6 = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (6, 1, 0),
        (7, 1, 0),
        (8, 1, 0),
        (9, 1, 0),
        (10, 1, 0),
        (11, 1, 0),
        (11, 0, 0),
        (12, 0, 0),
    )
    checks.check(
        "witnessing-paths",
        "named in-ball walks realize the arrivals used in the k=1,2,5,6 reverse bits",
        path_cost(axis_k1) == arrivals[(2, 0, 0)]
        and path_cost(face_k1) == arrivals[(1, 1, 0)]
        and path_cost(axis_k2) == arrivals[(4, 0, 0)]
        and path_cost(face_k2) == arrivals[(2, 2, 0)]
        and path_cost(axis_k5) == arrivals[(10, 0, 0)]
        and path_cost(face_k5) == arrivals[(5, 5, 0)]
        and path_cost(axis_k6) == arrivals[(12, 0, 0)]
        and all(
            site in BALL
            for site in axis_k1 + face_k1 + axis_k2 + face_k2 + axis_k5 + face_k5 + axis_k6
        )
        and "(12,1,0)" in note
        and "outside B_12(0)" in note,
    )

    checks.check(
        "bit-not-constant",
        "the reverse bit is not the same for every k=1..6",
        bits == [True, True, True, True, False, True]
        and "not the same for every" in note
        and "does not stay reversed at $k=5$" in note,
    )
    checks.check(
        "keeps-k4-fails-k5",
        "k=4 remains reverse and k=5 fails reverse",
        bits[3] is True
        and bits[4] is False
        and "holds at $k=4$" in note
        and "fails at $k=5$" in note,
    )
    checks.check(
        "not-even-k-leftover",
        "the k=1..6 census is not leftover of the three even-k face pairs",
        "not leftover of those three pairs" in note
        and "independent Dijkstra" in note
        and arrivals[(1, 1, 0)] == 2
        and arrivals[(3, 3, 0)] == 6
        and arrivals[(5, 5, 0)] == 10
        and arrivals[(10, 0, 0)] == 14
        and l1_norm((12, 0, 0)) == 12
        and l1_norm((6, 6, 0)) == 12,
    )
    checks.check(
        "graph-length-contrast",
        "uniform graph-length does not reverse the six face pairs and is not attached",
        all(
            not is_reverse({axis_site(k): l1_norm(axis_site(k)), face_site(k): l1_norm(face_site(k))}, k)
            for k in SCALES
        )
        and (l1_norm((4, 0, 0)), l1_norm((2, 2, 0))) != (arrivals[(4, 0, 0)], arrivals[(2, 2, 0)])
        and "Do not attach L1" in note,
    )
    expensive_axis_open = hop_cost(ORIGIN, (1, 0, 0), (1, 1, 1))
    checks.check(
        "mutation-seed-exit",
        "charging seed-exit 3 changes the opening hop of the axis witness",
        expensive_axis_open == 3
        and path_cost(axis_k2, (1, 1, 1)) != arrivals[(4, 0, 0)],
    )

    allowed_retained = ("audit_required_before_effective_retained: true", "bare_retained_allowed: false")
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        'hypothetical_axiom_status: "no edit"',
        "Displayed, not adopted",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "not written into Admissibility",
        "Do not attach L1",
        "Uniqueness is not claimed",
    )
    checks.check(
        "note-contract",
        "machine fields, exhibition wording, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{index}" in note for index in range(1, 9))
        and not any(phrase in note for phrase in FORBIDDEN)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
        residual=[phrase for phrase in required if phrase not in note],
    )
    checks.check(
        "claim-scope",
        "front matter keeps the dispatch claim_scope",
        CLAIM_SCOPE in note,
    )
    checks.check(
        "not-in-admissibility",
        "(0,1,1) is not written into Admissibility",
        "Do not write (0,1,1) into Admissibility" in note
        and "not written into Admissibility" in note
        and "There is one fixed nearest-neighbor admissibility rule" in axiom,
    )
    forbidden_hits = [phrase for phrase in FORBIDDEN if phrase in note or phrase in source.split("FORBIDDEN =", 1)[0]]
    checks.check(
        "forbidden-phrases",
        "forbidden phrases are absent from the note and from runner prose",
        forbidden_hits == [],
        residual=forbidden_hits,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only",
        "### Admissibility / Local Constraint" in axiom
        and "(0,1,1)" not in axiom,
    )

    print("per_element: inward-weight clauses and hop-costs are evaluated on named directed nearest-neighbor edges")
    print("per_site: arrivals are read at the twelve in-ball face and axis targets")
    print("per_mode: reverse is the exact integer comparison versus integer scale k")
    print("per_block: one Dijkstra on B_12(0) and the named (0,1,1) hop-cost")
    print("lattice_wide: checked and not executed — no Admissibility edit and L1 is not attached")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
