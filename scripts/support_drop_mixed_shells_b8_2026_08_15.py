#!/usr/bin/env python3
"""Mixed t=const shells of the named support-drop hop-cost on B_8(0).

One Dijkstra on the six-neighbor graph of the closed ℓ¹ ball of radius 8.
Names each mixed arrival and the number of distinct |v|_2^2 in that shell.
The named cost is displayed, not adopted. No cache is written and
Admissibility is not edited. L1 is not attached.
"""

from __future__ import annotations

from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_MIXED_SHELLS_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_MIXED_SHELLS_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

RADIUS = 8
NEIGHBORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
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


def radius2(site: tuple[int, int, int]) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def support_weight(site: tuple[int, int, int]) -> int:
    return sum(coord != 0 for coord in site)


def support_drop_cost(
    source: tuple[int, int, int],
    target: tuple[int, int, int],
) -> int:
    source_weight = support_weight(source)
    target_weight = support_weight(target)
    if source_weight == 0 or (source_weight == 1 and target_weight == 1) or target_weight < source_weight:
        return 3
    return 1


def ball_sites(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                if abs(x) + abs(y) + abs(z) <= radius:
                    sites.append((x, y, z))
    return sites


def dijkstra_times(
    sites: list[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
    allowed = set(sites)
    infinity = 10**9
    arrival = {site: infinity for site in sites}
    origin = (0, 0, 0)
    arrival[origin] = 0
    queue: list[tuple[int, tuple[int, int, int]]] = [(0, origin)]
    while queue:
        time, site = heappop(queue)
        if time != arrival[site]:
            continue
        for step in NEIGHBORS:
            neighbor = (site[0] + step[0], site[1] + step[1], site[2] + step[2])
            if neighbor not in allowed:
                continue
            candidate = time + support_drop_cost(site, neighbor)
            if candidate < arrival[neighbor]:
                arrival[neighbor] = candidate
                heappush(queue, (candidate, neighbor))
    return arrival


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("dijkstra_count: 1")
    print(
        "external_scientific_inputs: none; the named support-drop hop-cost is a "
        "declared displayed rule on B_8(0)"
    )
    print(
        "claim_scope: Mixed t=const shells under the named support-drop "
        "hop-cost on B_8(0) are named. Displayed, not adopted."
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites(RADIUS)
    checks.check(
        "ball-cardinality",
        "B_8(0) is the closed ℓ¹ ball of radius 8 and has 833 sites",
        len(sites) == 833,
        residual=len(sites),
    )

    arrival = dijkstra_times(sites)
    checks.check(
        "one-dijkstra-complete",
        "the single Dijkstra reaches every site of B_8(0)",
        all(arrival[site] < 10**9 for site in sites),
    )
    checks.check(
        "origin-time-zero",
        "t(0,0,0) = 0 and the origin is excluded from the mixed-shell census",
        arrival[(0, 0, 0)] == 0,
    )

    shells: dict[int, set[int]] = defaultdict(set)
    shell_count: dict[int, int] = defaultdict(int)
    for site in sites:
        if site == (0, 0, 0):
            continue
        shells[arrival[site]].add(radius2(site))
        shell_count[arrival[site]] += 1

    all_times = sorted(shells)
    mixed_times = [time for time in all_times if len(shells[time]) > 1]
    single_times = [time for time in all_times if len(shells[time]) == 1]
    mixed_rows = [
        (time, shell_count[time], len(shells[time]), tuple(sorted(shells[time])))
        for time in mixed_times
    ]

    print(f"arrival_values={all_times}")
    print(f"n_arrival_values={len(all_times)}")
    print(f"single_radius_t={single_times}")
    print(f"mixed_t={mixed_times}")
    for time, n_sites, n_radii, radii in mixed_rows:
        print(f"mixed t={time} sites={n_sites} n_|v|_2^2={n_radii} radii={list(radii)}")
    if 8 in shells:
        print(
            f"reverse_critical_t=8 sites={shell_count[8]} "
            f"n_|v|_2^2={len(shells[8])} mixed={len(shells[8]) > 1}"
        )

    checks.check(
        "twelve-arrival-values",
        "B_8(0)\\{0} carries exactly twelve distinct arrival values",
        all_times == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16],
        residual=all_times,
    )
    checks.check(
        "six-of-twelve-mixed",
        "exactly six of those twelve arrival values mix Euclidean radii",
        mixed_times == [5, 6, 7, 8, 9, 10] and len(single_times) == 6,
        residual=mixed_times,
    )

    expected_mixed = {
        5: (32, 2, (3, 5)),
        6: (66, 4, (4, 6, 8, 10)),
        7: (96, 4, (9, 11, 13, 17)),
        8: (140, 5, (12, 14, 18, 20, 26)),
        9: (198, 8, (9, 17, 19, 21, 25, 27, 29, 37)),
        10: (258, 10, (16, 22, 24, 26, 30, 32, 34, 38, 40, 50)),
    }
    computed_map = {time: (n_sites, n_radii, radii) for time, n_sites, n_radii, radii in mixed_rows}
    checks.check(
        "named-mixed-shells",
        "each mixed t is named with its site count and distinct |v|_2^2 count",
        computed_map == expected_mixed,
        residual=computed_map,
    )
    for time, (n_sites, n_radii, radii) in expected_mixed.items():
        checks.check(
            f"mixed-t{time}",
            f"t={time} has {n_sites} sites and {n_radii} distinct |v|_2^2 {list(radii)}",
            computed_map.get(time) == (n_sites, n_radii, radii),
            residual=computed_map.get(time),
        )

    checks.check(
        "t8-present-and-mixed",
        "the reverse-critical t=8 shell is present and mixes five Euclidean radii",
        8 in mixed_times and computed_map[8] == (140, 5, (12, 14, 18, 20, 26)),
        residual=computed_map.get(8),
    )
    checks.check(
        "t8-contains-body-diagonal",
        "t(2,2,2)=8, so the reverse-critical body-diagonal type sits in the mixed t=8 shell",
        arrival[(2, 2, 2)] == 8 and radius2((2, 2, 2)) == 12,
        residual=arrival[(2, 2, 2)],
    )
    checks.check(
        "not-leftover-mixed-bit",
        "the census is the six named mixed arrivals with radii counts, not a leftover six-mix bit",
        sum(row[1] for row in mixed_rows) == 32 + 66 + 96 + 140 + 198 + 258
        and {row[0] for row in mixed_rows} == set(expected_mixed)
        and all(row[2] > 1 for row in mixed_rows),
    )

    seed_exit = support_drop_cost((0, 0, 0), (1, 0, 0)) == 3
    axis_skeleton = support_drop_cost((1, 0, 0), (2, 0, 0)) == 3
    drop_clause = support_drop_cost((1, 1, 0), (1, 0, 0)) == 3
    cheap_raise = support_drop_cost((1, 1, 0), (1, 1, 1)) == 1
    checks.check(
        "named-cost-clauses",
        "ν is 3 on seed-exit, both-weights-1, and support-drop, else 1",
        seed_exit and axis_skeleton and drop_clause and cheap_raise,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-tokens",
        "the note avoids the forbidden tokens",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "displayed-not-adopted",
        "the mixed shells are displayed, not adopted",
        "Displayed, not adopted" in note and "not adopted" in note,
    )
    checks.check(
        "nu-not-admissibility",
        "the note refuses to write ν into Admissibility, and the axiom memo is untouched by this claim",
        "Do not write" in note
        and "Admissibility" in note
        and "named support-drop hop-cost" in note
        and "ν" not in axiom
        and "support-drop" not in axiom,
    )
    checks.check(
        "l1-not-attached",
        "L1 is not attached as a hop-cost, comparator, or leftover",
        "Do not attach L1" in note
        and "not attached" in note
        and "var(|v|_2/t)" not in note
        and "var_ℓ" not in note,
    )
    checks.check(
        "claim-scope-text",
        "the note states the declared mixed-shell claim_scope",
        "Mixed t=const shells under the named support-drop hop-cost on B_8(0) are named."
        in note,
    )
    checks.check(
        "note-names-mixed-arrivals",
        "the note names each mixed t with its distinct-radius count and site count",
        all(
            f"t={time}" in note and str(n_sites) in note and str(n_radii) in note
            for time, (n_sites, n_radii, _radii) in expected_mixed.items()
        )
        and "{3, 5}" in note
        and "{4, 6, 8, 10}" in note
        and "{9, 11, 13, 17}" in note
        and "{12, 14, 18, 20, 26}" in note
        and "{9, 17, 19, 21, 25, 27, 29, 37}" in note
        and "{16, 22, 24, 26, 30, 32, 34, 38, 40, 50}" in note,
    )
    checks.check(
        "note-records-t8-mixed",
        "the note displays the reverse-critical t=8 shell as mixed, not adopted",
        "t=8" in note
        and "140" in note
        and "five" in note
        and "Displayed, not adopted" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
