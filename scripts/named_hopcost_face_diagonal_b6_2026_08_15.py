#!/usr/bin/env python3
"""One Dijkstra on B_6(0) for face-diagonal vs axis order under named ρ."""

from __future__ import annotations

from fractions import Fraction
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/NAMED_HOPCOST_FACE_DIAGONAL_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NAMED_HOPCOST_FACE_DIAGONAL_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

SHIFTS: tuple[tuple[int, int, int], ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
RADIUS = 6
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
EIGHT_ORBITS = (
    (0, 1),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
)


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
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1(site: tuple[int, int, int]) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def l2sq(site: tuple[int, int, int]) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def inward_weight(site: tuple[int, int, int]) -> int:
    return sum(1 for coord in site if coord != 0)


def rho(weight_v: int, weight_w: int) -> int:
    if weight_v == weight_w or weight_v == 0:
        return 3
    return 1


def ball(radius: int) -> frozenset[tuple[int, int, int]]:
    sites: set[tuple[int, int, int]] = set()
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                site = (x, y, z)
                if l1(site) <= radius:
                    sites.add(site)
    return frozenset(sites)


def dijkstra_rho(sites: frozenset[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
    inf = 10**9
    dist = {site: inf for site in sites}
    origin = (0, 0, 0)
    dist[origin] = 0
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, origin)]
    while heap:
        cost, site = heappop(heap)
        if cost != dist[site]:
            continue
        weight_v = inward_weight(site)
        x, y, z = site
        for dx, dy, dz in SHIFTS:
            nbr = (x + dx, y + dy, z + dz)
            if nbr not in sites:
                continue
            nxt = cost + rho(weight_v, inward_weight(nbr))
            if nxt < dist[nbr]:
                dist[nbr] = nxt
                heappush(heap, (nxt, nbr))
    return dist


def q_ratio(times: dict[tuple[int, int, int], int], site: tuple[int, int, int]) -> Fraction:
    arrival = times[site]
    return Fraction(arrival * arrival, l2sq(site))


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axioms = AXIOM_PATH.read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: none; ρ is a displayed named hop-cost")
    print(
        "claim_scope: Face-diagonal versus axis arrival order under the named "
        "hop-cost on B_6(0) is reported. Displayed, not adopted."
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and minimal axioms",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball(RADIUS)
    checks.check(
        "ball-cardinality",
        "B_6(0) has 377 sites",
        len(sites) == 377,
        len(sites),
    )

    eight = tuple(rho(a, b) for a, b in EIGHT_ORBITS)
    checks.check(
        "rho-eight-tuple",
        "ρ recovers the eight-tuple (3,1,3,1,1,3,1,1)",
        eight == (3, 1, 3, 1, 1, 3, 1, 1),
        eight,
    )
    checks.check(
        "rho-equal-three",
        "equal inward weight (3,3) has cost 3",
        rho(3, 3) == 3,
    )

    times = dijkstra_rho(sites)
    axis4 = (4, 0, 0)
    axis6 = (6, 0, 0)
    face33 = (3, 3, 0)
    face42 = (4, 2, 0)
    body = (2, 2, 2)
    reported = {
        axis4: 12,
        axis6: 18,
        face33: 16,
        face42: 16,
        body: 14,
    }
    for site, expected in reported.items():
        label = "".join(str(abs(c)) for c in site)
        checks.check(
            f"t-{label}",
            f"t{site}={expected}",
            times[site] == expected,
            times[site],
        )

    pairs = ((axis4, face33), (axis4, face42), (axis6, face33))
    ratios = []
    reverses = []
    for axis, diag in pairs:
        q_axis = q_ratio(times, axis)
        q_diag = q_ratio(times, diag)
        ratios.append((q_axis, q_diag))
        reverses.append(q_diag < q_axis)

    checks.check(
        "pair-400-330",
        "((4,0,0),(3,3,0)) does not reverse: 128/9 > 9",
        ratios[0] == (Fraction(9), Fraction(128, 9)) and not reverses[0],
        ratios[0],
    )
    checks.check(
        "pair-400-420",
        "((4,0,0),(4,2,0)) does not reverse: 64/5 > 9",
        ratios[1] == (Fraction(9), Fraction(64, 5)) and not reverses[1],
        ratios[1],
    )
    checks.check(
        "pair-600-330",
        "((6,0,0),(3,3,0)) does not reverse: 128/9 > 9",
        ratios[2] == (Fraction(9), Fraction(128, 9)) and not reverses[2],
        ratios[2],
    )
    checks.check(
        "no-face-reverse",
        "none of the three face-versus-axis pairs reverses diamond order",
        reverses == [False, False, False],
        reverses,
    )

    required_note = (
        "t(4,0,0)=12",
        "t(6,0,0)=18",
        "t(3,3,0)=16",
        "t(4,2,0)=16",
        "t(2,2,2)=14",
        "128/9 > 9",
        "64/5 > 9",
        "Displayed, not adopted",
        "Do not write `ρ` into Admissibility",
        "Do not attach L1",
        "Face-diagonal versus axis arrival order under the named hop-cost on B_6(0) is reported",
        "**Type:** bounded_theorem",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "hypothetical_axiom_status: no edit",
        "377-site",
        "One Dijkstra",
    )
    checks.check(
        "note-contract",
        "the note reports the times, non-reversals, and bounded scope",
        all(phrase in note for phrase in required_note),
        [phrase for phrase in required_note if phrase not in note],
    )
    checks.check(
        "note-no-forbidden",
        "the note avoids the forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN),
        [phrase for phrase in FORBIDDEN if phrase in note],
    )
    checks.check(
        "axiom-names",
        "the axiom memo names Lattice, Qubit, Admissibility, and Record",
        all(name in axioms for name in ("Lattice", "Qubit", "Admissibility", "Record")),
    )
    checks.check(
        "axis-unit-cost-contrast",
        "unit six-neighbor arrival is |v|_1, so t_unit(3,3,0)=6 is not t_ρ=16",
        l1(face33) == 6 and times[face33] != l1(face33),
        (l1(face33), times[face33]),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
