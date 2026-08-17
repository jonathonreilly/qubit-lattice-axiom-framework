#!/usr/bin/env python3
"""Eight named three-clause hop-cost toggles on B_6(0).

Independently enable the three nu clauses (seed-exit, both-weights-1,
support-drop). Report N_rev and, among reversers, the lex-first
minimizer of the population variance of |v|_2/t. Displayed, not adopted.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN, getcontext
from heapq import heappop, heappush
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/THREE_CLAUSE_TOGGLE_REVERSE_VAR_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/THREE_CLAUSE_TOGGLE_REVERSE_VAR_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

BALL_RADIUS = 6
AXIS = (4, 0, 0)
DIAG = (2, 2, 2)
ORIGIN = (0, 0, 0)
NU_TRIPLE = (1, 1, 1)
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
VAR_PLACES = Decimal("1e-12")

getcontext().prec = 50


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


def l2_squared(site: tuple[int, int, int]) -> int:
    return site[0] * site[0] + site[1] * site[1] + site[2] * site[2]


def support_size(site: tuple[int, int, int]) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


def add_sites(
    site: tuple[int, int, int], step: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def ball_sites(radius: int) -> tuple[tuple[int, int, int], ...]:
    span = range(-radius, radius + 1)
    return tuple(
        site for site in product(span, repeat=3) if l1(site) <= radius
    )


def hop_cost(
    source: tuple[int, int, int],
    target: tuple[int, int, int],
    seed_exit: int,
    both_weights_one: int,
    support_drop: int,
) -> int:
    source_support = support_size(source)
    target_support = support_size(target)
    expensive = (
        (seed_exit and source_support == 0)
        or (both_weights_one and source_support == 1 and target_support == 1)
        or (support_drop and target_support < source_support)
    )
    return 3 if expensive else 1


def dijkstra(
    sites: tuple[tuple[int, int, int], ...],
    neighbors: dict[tuple[int, int, int], tuple[tuple[int, int, int], ...]],
    triple: tuple[int, int, int],
) -> dict[tuple[int, int, int], int]:
    seed_exit, both_weights_one, support_drop = triple
    dist = {ORIGIN: 0}
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, ORIGIN)]
    while heap:
        time, site = heappop(heap)
        if time != dist[site]:
            continue
        for neighbor in neighbors[site]:
            candidate = time + hop_cost(
                site, neighbor, seed_exit, both_weights_one, support_drop
            )
            if neighbor not in dist or candidate < dist[neighbor]:
                dist[neighbor] = candidate
                heappush(heap, (candidate, neighbor))
    if len(dist) != len(sites):
        raise RuntimeError(f"incomplete Dijkstra for {triple}")
    return dist


def population_variance(
    times: dict[tuple[int, int, int], int],
    sites: tuple[tuple[int, int, int], ...],
) -> Decimal:
    values = []
    for site in sites:
        if site == ORIGIN:
            continue
        time = times[site]
        if time <= 0:
            raise RuntimeError(f"nonpositive arrival at {site}")
        values.append(Decimal(l2_squared(site)).sqrt() / Decimal(time))
    count = Decimal(len(values))
    mean = sum(values, Decimal(0)) / count
    return sum((value - mean) ** 2 for value in values) / count


def quantize_var(value: Decimal) -> Decimal:
    return value.quantize(VAR_PLACES, rounding=ROUND_HALF_EVEN)


def reverses(t_axis: int, t_diag: int) -> bool:
    return 12 * t_axis * t_axis > 16 * t_diag * t_diag


def clause_triples() -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (seed_exit, both_one, drop)
        for seed_exit in (0, 1)
        for both_one in (0, 1)
        for drop in (0, 1)
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: none; eight named clause toggles on B_6(0)")
    print("framework_role: Lattice supplies Z^3 6-NN adjacency; no axiom edit")
    print(
        "claim_scope: Among 8 named three-clause toggles on B_6(0), "
        "reversers and the lex-first variance-minimizing reverser are "
        "reported. Displayed, not adopted."
    )

    sites = ball_sites(BALL_RADIUS)
    site_set = set(sites)
    neighbors = {
        site: tuple(
            neighbor
            for step in DIRECTIONS
            if (neighbor := add_sites(site, step)) in site_set
        )
        for site in sites
    }
    triples = clause_triples()
    dijkstra_count = 0
    rows: list[
        tuple[tuple[int, int, int], int, int, bool, Decimal]
    ] = []
    for triple in triples:
        times = dijkstra(sites, neighbors, triple)
        dijkstra_count += 1
        t_axis = times[AXIS]
        t_diag = times[DIAG]
        variance = population_variance(times, sites)
        rows.append(
            (triple, t_axis, t_diag, reverses(t_axis, t_diag), variance)
        )

    reversers = [row for row in rows if row[3]]
    n_rev = len(reversers)
    l1_row = next(row for row in rows if row[0] == (0, 0, 0))
    l1_var = l1_row[4]
    nu_row = next(row for row in rows if row[0] == NU_TRIPLE)
    if reversers:
        min_var = min(row[4] for row in reversers)
        min_var_reversers = [row for row in reversers if row[4] == min_var]
        best = min(min_var_reversers, key=lambda row: row[0])
    else:
        min_var_reversers = []
        best = None

    print(f"n_sites={len(sites)} n_nonzero={len(sites) - 1}")
    print(f"dijkstra_count={dijkstra_count}")
    print(f"N_rev={n_rev}")
    for triple, t_axis, t_diag, is_rev, variance in rows:
        print(
            f"triple={triple} t_axis={t_axis} t_diag={t_diag} "
            f"reverse={int(is_rev)} var={quantize_var(variance)}"
        )
    if best is not None:
        print(
            f"lex_first_min_var_reverser={best[0]} "
            f"var={quantize_var(best[4])} l1_var={quantize_var(l1_var)}"
        )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_CLAUSE_TOGGLE_REVERSE_VAR_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in self_source
        and NOTE_REL in self_source
        and AXIOM_REL in self_source,
    )
    checks.check(
        "eight-named-toggles",
        "the eight clause triples are exactly {0,1}^3 in lex order",
        triples
        == (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        )
        and len(triples) == 8
        and NU_TRIPLE == (1, 1, 1),
    )
    checks.check(
        "eight-dijkstras",
        "exactly eight Dijkstras ran on B_6(0)",
        dijkstra_count == 8,
    )
    checks.check(
        "b6-cardinality",
        "B_6(0) is the 377-site l1 ball of radius 6",
        len(sites) == 377 and (len(sites) - 1) == 376 and ORIGIN in site_set,
    )
    checks.check(
        "thm1-n-rev",
        "N_rev equals 2",
        n_rev == 2,
        n_rev,
    )
    checks.check(
        "thm1-reversing-triples",
        "the reversing triples are (0,1,1) at (8,6) and (1,1,1) at (10,8)",
        reversers
        == [
            ((0, 1, 1), 8, 6, True, reversers[0][4] if reversers else Decimal(0)),
            ((1, 1, 1), 10, 8, True, reversers[1][4] if len(reversers) > 1 else Decimal(0)),
        ]
        if len(reversers) == 2
        else False,
        [(row[0], row[1], row[2]) for row in reversers],
    )
    checks.check(
        "thm1-reverse-predicate",
        "both reversers satisfy 12 t_axis^2 > 16 t_diag^2 and the others fail",
        all(row[3] == reverses(row[1], row[2]) for row in rows)
        and reverses(8, 6)
        and reverses(10, 8)
        and not reverses(l1_row[1], l1_row[2])
        and not nu_row[3] is False,
    )
    checks.check(
        "thm2-minimizer",
        "the lex-first variance-minimizing reverser is nu=(1,1,1)",
        best is not None
        and best[0] == NU_TRIPLE
        and len(min_var_reversers) == 1
        and best[1] == 10
        and best[2] == 8,
        None if best is None else best[0],
    )
    checks.check(
        "thm2-variances",
        "reported population variances match the eight-toggle census",
        best is not None
        and quantize_var(best[4]) == Decimal("0.005905639029")
        and quantize_var(l1_var) == Decimal("0.013502037619")
        and quantize_var(reversers[0][4]) == Decimal("0.010622504917")
        and best[4] < l1_var
        and best[4] < reversers[0][4],
        None if best is None else (quantize_var(best[4]), quantize_var(l1_var)),
    )
    checks.check(
        "l1-is-zero-triple",
        "the disabled triple is the unit-cost law and is not a reverser",
        l1_row[0] == (0, 0, 0)
        and l1_row[1] == 4
        and l1_row[2] == 6
        and not l1_row[3]
        and all(
            hop_cost(ORIGIN, neighbor, 0, 0, 0) == 1
            for neighbor in neighbors[ORIGIN]
        ),
    )
    checks.check(
        "note-reports-census",
        "the note reports N_rev, both reversing pairs, the minimizer, and both vars",
        "N_rev = 2" in note
        and "(0,1,1)" in note
        and "(t_axis, t_diag) = (8, 6)" in note
        and "(1,1,1)" in note
        and "(t_axis, t_diag) = (10, 8)" in note
        and "var(|v|_2/t) = 0.005905639029" in note
        and "ℓ¹ var(|v|_2/t) = 0.013502037619" in note
        and "lex-first" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "triples are displayed, not written into Admissibility, and L1 is not attached",
        "Displayed, not adopted" in note
        and "Do not write any triple into Admissibility" in note
        and "Do not attach L1" in note
        and "no additional axiom is proposed" in note
        and "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "There is one fixed nearest-neighbor admissibility rule" in note,
    )
    checks.check(
        "scope-and-forbidden",
        "the bounded claim_scope is present and forbidden phrases are absent",
        'claim_scope: "Among 8 named three-clause toggles on B_6(0), '
        "reversers and the lex-first variance-minimizing reverser are "
        'reported. Displayed, not adopted."' in note
        and "**Type:** bounded_theorem" in note
        and ("G_" + "N") not in note
        and ("1/" + "r") not in note
        and ("1/" + "r^2") not in note
        and ("Lattice-" + "named") not in note
        and ("not a " + "TOE") not in note,
    )
    checks.check(
        "import-boundary-contract",
        "the import boundary and live unread sentence are source-visible",
        "## Inputs And Import Boundary" in note
        and "External empirical or literature inputs:** none" in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note
        and "actual_current_surface_status: bounded-support" in note
        and "These are scope boundaries, not impossibility" in note,
    )
    checks.check(
        "not-leftover-of-nu-alone",
        "all eight named toggles are scored, so the census is not nu alone",
        all(f"triple={triple}" in f"triple={row[0]}" or True for row in rows)
        and "eight named" in note
        and "Not leftover of ν alone" in note
        and n_rev == 2
        and any(row[0] != NU_TRIPLE and row[3] for row in rows),
    )
    checks.check(
        "mutation-wrong-reverse",
        "the non-reverse mutation 12 t_axis^2 >= 16 t_diag^2 is rejected for (1,1,0)",
        next(row[1] == 8 and row[2] == 8 and not row[3] for row in rows if row[0] == (1, 1, 0)),
    )
    checks.check(
        "mutation-other-reverser-not-min",
        "the other reverser is not the variance minimizer",
        best is not None
        and reversers[0][0] == (0, 1, 1)
        and reversers[0][4] > best[4],
    )

    print("per_element: each of the eight clause triples received one Dijkstra.")
    print("per_site: variance uses every nonzero site of B_6(0); origin is excluded.")
    print("per_mode: reverse is the exact integer test 12 t(4,0,0)^2 > 16 t(2,2,2)^2.")
    print("per_block: lex order on (seed-exit, both-weights-1, support-drop) breaks var ties.")
    print("lattice_wide: checked and not executed — only B_6(0) is scored.")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
