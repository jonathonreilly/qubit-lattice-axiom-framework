#!/usr/bin/env python3
"""Body and face reverse under the named (0,1,1) hop-cost on B_8(0).

One origin Dijkstra. Seed-exit is cheap; both-weights-one and support-drop
cost 3. The rule is displayed, not adopted. No cache write. No axiom edit.
"""

from __future__ import annotations

from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CLAUSE_011_REVERSE_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_REVERSE_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Body and face reverse under the named (0,1,1) hop-cost on "
    "B_8(0) are reported. Displayed, not adopted."
)
RADIUS = 8
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
IN_BALL_TARGETS = (
    (4, 0, 0),
    (6, 0, 0),
    (8, 0, 0),
    (2, 2, 2),
    (3, 3, 0),
    (4, 4, 0),
)
OUTSIDE_TARGET = (4, 4, 4)
EXPECTED_TIMES = {
    (4, 0, 0): 8,
    (6, 0, 0): 10,
    (8, 0, 0): 14,
    (2, 2, 2): 6,
    (3, 3, 0): 6,
    (4, 4, 0): 8,
}
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


def body_reverse(t_axis: int, t_diag: int) -> bool:
    return 12 * t_axis * t_axis > 16 * t_diag * t_diag


def face_reverse(axis: Point, diag: Point, times: dict[Point, int]) -> bool:
    t_axis = times[axis]
    t_diag = times[diag]
    return t_diag * t_diag * l2sq(axis) < t_axis * t_axis * l2sq(diag)


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
    print("construction: named (0,1,1) hop-cost on B_8(0) with one origin Dijkstra")
    print("negative_scope: displayed, not adopted; not written into Admissibility; L1 not attached")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_REVERSE_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        'AUDIT_INPUT_PATHS = (\n    "docs/CLAUSE_011_REVERSE_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
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

    checks.check("ball-cardinality", "B_8(0) has exactly 833 integer sites", len(BALL) == 833)
    checks.check(
        "targets-inside",
        "the six in-ball scored sites lie in B_8(0) and (4,4,4) does not",
        all(site in BALL for site in IN_BALL_TARGETS)
        and OUTSIDE_TARGET not in BALL
        and l1_norm(OUTSIDE_TARGET) == 12,
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
        all(site in arrivals for site in IN_BALL_TARGETS),
    )

    print("arrival_times:")
    for site in IN_BALL_TARGETS:
        time = arrivals[site]
        print(f"  t{site}={time}  t^2/|v|_2^2={time * time}/{l2sq(site)}")
    print(f"  t{OUTSIDE_TARGET}=absent  |v|_1={l1_norm(OUTSIDE_TARGET)}")

    for site, expected in EXPECTED_TIMES.items():
        token = f"t({site[0]},{site[1]},{site[2]})={expected}"
        checks.check(
            f"time-{site[0]}{site[1]}{site[2]}",
            f"computed {token} is written in the note",
            arrivals[site] == expected and token in note,
            residual=(arrivals[site], token in note),
        )

    t400 = arrivals[(4, 0, 0)]
    t222 = arrivals[(2, 2, 2)]
    t800 = arrivals[(8, 0, 0)]
    t330 = arrivals[(3, 3, 0)]
    t440 = arrivals[(4, 4, 0)]
    t600 = arrivals[(6, 0, 0)]

    print("reverse_bits:")
    print(
        f"  body (4,0,0) vs (2,2,2): {body_reverse(t400, t222)} "
        f"12 t(4,0,0)^2={12 * t400 * t400} 16 t(2,2,2)^2={16 * t222 * t222}"
    )
    print("  body (8,0,0) vs (4,4,4): not a B_8(0) comparison; (4,4,4) is outside the ball")
    print(
        f"  face (4,0,0) vs (3,3,0): {face_reverse((4, 0, 0), (3, 3, 0), arrivals)} "
        f"16 t(3,3,0)^2={16 * t330 * t330} 18 t(4,0,0)^2={18 * t400 * t400}"
    )
    print(
        f"  face (8,0,0) vs (4,4,0): {face_reverse((8, 0, 0), (4, 4, 0), arrivals)} "
        f"64 t(4,4,0)^2={64 * t440 * t440} 32 t(8,0,0)^2={32 * t800 * t800}"
    )

    checks.check(
        "body-400-222",
        "12 t(4,0,0)^2 > 16 t(2,2,2)^2 holds and is written",
        body_reverse(t400, t222)
        and 12 * t400 * t400 == 768
        and 16 * t222 * t222 == 576
        and "12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2" in note,
    )
    checks.check(
        "body-800-444-absent",
        "(4,4,4) is outside B_8(0), so the large body comparison is not scored",
        OUTSIDE_TARGET not in BALL
        and OUTSIDE_TARGET not in arrivals
        and "t(4,4,4) is not a B_8(0) arrival" in note
        and "12 t(8,0,0)^2 > 16 t(4,4,4)^2 is not a B_8(0) comparison" in note,
    )
    checks.check(
        "face-400-330",
        "((4,0,0),(3,3,0)) has smaller t^2/|v|_2^2 on the more-diagonal site",
        face_reverse((4, 0, 0), (3, 3, 0), arrivals)
        and inward_weight((3, 3, 0)) > inward_weight((4, 0, 0))
        and 16 * t330 * t330 == 576
        and 18 * t400 * t400 == 1152
        and "16 t(3,3,0)^2 = 576 < 1152 = 18 t(4,0,0)^2" in note,
    )
    checks.check(
        "face-800-440",
        "((8,0,0),(4,4,0)) has smaller t^2/|v|_2^2 on the more-diagonal site",
        face_reverse((8, 0, 0), (4, 4, 0), arrivals)
        and inward_weight((4, 4, 0)) > inward_weight((8, 0, 0))
        and 64 * t440 * t440 == 4096
        and 32 * t800 * t800 == 6272
        and "64 t(4,4,0)^2 = 4096 < 6272 = 32 t(8,0,0)^2" in note,
    )

    axis_witness = (ORIGIN, (1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 1, 0), (4, 0, 0))
    diag_witness = (ORIGIN, (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2))
    face_witness = (ORIGIN, (1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0), (3, 2, 0), (3, 3, 0))
    far_axis_witness = (
        ORIGIN,
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (3, 1, 0),
        (4, 1, 0),
        (5, 1, 0),
        (6, 1, 0),
        (7, 1, 0),
        (7, 0, 0),
        (8, 0, 0),
    )
    checks.check(
        "witnessing-paths",
        "named in-ball walks realize the four displayed arrivals used in reverse bits",
        path_cost(axis_witness) == t400 == 8
        and path_cost(diag_witness) == t222 == 6
        and path_cost(face_witness) == t330 == 6
        and path_cost(far_axis_witness) == t800 == 14
        and all(site in BALL for site in axis_witness + diag_witness + face_witness + far_axis_witness)
        and "(8,1,0)" in note
        and "outside B_8(0)" in note,
    )

    checks.check(
        "not-b6-leftover",
        "t(6,0,0)=10 on B_8(0) is not the B_6(0) leftover 12",
        t600 == 10
        and t600 != 12
        and "t(6,0,0)=10" in note
        and "not leftover of the B_6(0)" in note,
    )
    checks.check(
        "graph-length-contrast",
        "uniform graph-length does not reverse the in-ball body pair and is not attached",
        l1_norm((4, 0, 0)) == 4
        and l1_norm((2, 2, 2)) == 6
        and l1_norm((4, 0, 0)) < l1_norm((2, 2, 2))
        and not body_reverse(l1_norm((4, 0, 0)), l1_norm((2, 2, 2)))
        and (l1_norm((4, 0, 0)), l1_norm((2, 2, 2))) != (t400, t222),
    )
    expensive_axis_open = hop_cost(ORIGIN, (1, 0, 0), (1, 1, 1))
    checks.check(
        "mutation-seed-exit",
        "charging seed-exit 3 changes the opening hop of the axis witness",
        expensive_axis_open == 3
        and path_cost(axis_witness, (1, 1, 1)) == 10
        and path_cost(axis_witness, (1, 1, 1)) != t400,
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
    forbidden_hits = [phrase for phrase in FORBIDDEN if phrase in note]
    checks.check(
        "forbidden-phrases",
        "forbidden phrases are absent from the source note",
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
    print("per_site: arrivals are read at the six in-ball targets; (4,4,4) is outside B_8(0)")
    print("per_mode: reverse is the exact integer comparison on body and face pairs")
    print("per_block: one Dijkstra on B_8(0) and the named (0,1,1) hop-cost")
    print("lattice_wide: checked and not executed — no Admissibility edit and L1 is not attached")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
