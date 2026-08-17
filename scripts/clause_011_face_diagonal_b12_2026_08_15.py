#!/usr/bin/env python3
"""Face reverse under the named (0,1,1) hop-cost on B_12(0).

One origin Dijkstra. Seed-exit is cheap; both-weights-one and support-drop
cost 3. The rule is displayed, not adopted. No cache write. No axiom edit.
"""

from __future__ import annotations

from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/CLAUSE_011_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Face-diagonal reverse under the named (0,1,1) hop-cost on "
    "B_12(0) is reported. Displayed, not adopted."
)
RADIUS = 12
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
    (8, 0, 0),
    (12, 0, 0),
    (2, 2, 0),
    (4, 4, 0),
    (6, 6, 0),
)
FACE_PAIRS = (
    ((4, 0, 0), (2, 2, 0)),
    ((8, 0, 0), (4, 4, 0)),
    ((12, 0, 0), (6, 6, 0)),
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
    print("construction: named (0,1,1) hop-cost on B_12(0) with one origin Dijkstra")
    print("negative_scope: displayed, not adopted; not written into Admissibility; L1 not attached")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        'AUDIT_INPUT_PATHS = (\n    "docs/CLAUSE_011_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
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

    checks.check("ball-cardinality", "B_12(0) has exactly 2625 integer sites", len(BALL) == 2625)
    checks.check(
        "targets-inside",
        "the six scored sites lie in B_12(0) and (12,1,0) does not",
        all(site in BALL for site in IN_BALL_TARGETS)
        and (12, 1, 0) not in BALL
        and l1_norm((12, 1, 0)) == 13
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
        all(site in arrivals for site in IN_BALL_TARGETS),
    )

    print("arrival_times:")
    for site in IN_BALL_TARGETS:
        time = arrivals[site]
        print(f"  t{site}={time}  t^2/|v|_2^2={time * time}/{l2sq(site)}")

    computed_tokens = {
        site: f"t({site[0]},{site[1]},{site[2]})={arrivals[site]}"
        for site in IN_BALL_TARGETS
    }
    for site in IN_BALL_TARGETS:
        token = computed_tokens[site]
        checks.check(
            f"time-{site[0]}{site[1]}{site[2]}",
            f"computed {token} is written in the note",
            token in note,
            residual=(arrivals[site], token in note),
        )

    t400 = arrivals[(4, 0, 0)]
    t800 = arrivals[(8, 0, 0)]
    t1200 = arrivals[(12, 0, 0)]
    t220 = arrivals[(2, 2, 0)]
    t440 = arrivals[(4, 4, 0)]
    t660 = arrivals[(6, 6, 0)]

    print("reverse_bits:")
    for axis, diag in FACE_PAIRS:
        t_axis = arrivals[axis]
        t_diag = arrivals[diag]
        print(
            f"  face {axis} vs {diag}: {face_reverse(axis, diag, arrivals)} "
            f"{l2sq(axis)} t{diag}^2={l2sq(axis) * t_diag * t_diag} "
            f"{l2sq(diag)} t{axis}^2={l2sq(diag) * t_axis * t_axis}"
        )

    checks.check(
        "face-400-220",
        "((4,0,0),(2,2,0)) has smaller t^2/|v|_2^2 on the more-diagonal site",
        face_reverse((4, 0, 0), (2, 2, 0), arrivals)
        and inward_weight((2, 2, 0)) > inward_weight((4, 0, 0))
        and 16 * t220 * t220 == 256
        and 8 * t400 * t400 == 512
        and "16 t(2,2,0)^2 = 256 < 512 = 8 t(4,0,0)^2" in note,
    )
    checks.check(
        "face-800-440",
        "((8,0,0),(4,4,0)) has smaller t^2/|v|_2^2 on the more-diagonal site",
        face_reverse((8, 0, 0), (4, 4, 0), arrivals)
        and inward_weight((4, 4, 0)) > inward_weight((8, 0, 0))
        and 64 * t440 * t440 == 4096
        and 32 * t800 * t800 == 4608
        and "64 t(4,4,0)^2 = 4096 < 4608 = 32 t(8,0,0)^2" in note,
    )
    checks.check(
        "face-1200-660",
        "((12,0,0),(6,6,0)) has smaller t^2/|v|_2^2 on the more-diagonal site",
        face_reverse((12, 0, 0), (6, 6, 0), arrivals)
        and inward_weight((6, 6, 0)) > inward_weight((12, 0, 0))
        and 144 * t660 * t660 == 20736
        and 72 * t1200 * t1200 == 23328
        and "144 t(6,6,0)^2 = 20736 < 23328 = 72 t(12,0,0)^2" in note,
    )

    axis_witness = (ORIGIN, (1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 1, 0), (4, 0, 0))
    face_witness = (ORIGIN, (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0))
    mid_axis_witness = (
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
        (8, 0, 0),
    )
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
        (8, 1, 0),
        (9, 1, 0),
        (10, 1, 0),
        (11, 1, 0),
        (11, 0, 0),
        (12, 0, 0),
    )
    checks.check(
        "witnessing-paths",
        "named in-ball walks realize the four displayed arrivals used in reverse bits",
        path_cost(axis_witness) == t400
        and path_cost(face_witness) == t220
        and path_cost(mid_axis_witness) == t800
        and path_cost(far_axis_witness) == t1200
        and all(
            site in BALL
            for site in axis_witness + face_witness + mid_axis_witness + far_axis_witness
        )
        and "(12,1,0)" in note
        and "outside B_12(0)" in note,
    )

    checks.check(
        "not-b8-leftover",
        "t(8,0,0)=12 on B_12(0) is not the B_8(0) leftover 14",
        t800 == 12
        and t800 != 14
        and "t(8,0,0)=12" in note
        and "not leftover of the `B_8(0)`" in note,
    )
    checks.check(
        "graph-length-contrast",
        "uniform graph-length does not reverse the three face pairs and is not attached",
        all(not face_reverse(axis, diag, {axis: l1_norm(axis), diag: l1_norm(diag)}) for axis, diag in FACE_PAIRS)
        and (l1_norm((4, 0, 0)), l1_norm((2, 2, 0))) != (t400, t220)
        and "Do not attach L1" in note,
    )
    expensive_axis_open = hop_cost(ORIGIN, (1, 0, 0), (1, 1, 1))
    checks.check(
        "mutation-seed-exit",
        "charging seed-exit 3 changes the opening hop of the axis witness",
        expensive_axis_open == 3
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
    print("per_site: arrivals are read at the six in-ball face and axis targets")
    print("per_mode: reverse is the exact integer comparison on the three face pairs")
    print("per_block: one Dijkstra on B_12(0) and the named (0,1,1) hop-cost")
    print("lattice_wide: checked and not executed — no Admissibility edit and L1 is not attached")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
