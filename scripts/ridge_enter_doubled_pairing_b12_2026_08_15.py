#!/usr/bin/env python3
"""Doubled pairing reverse under the named ridge-enter hop-cost on B_12(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
ridge-enter hop-cost is displayed, not adopted, and is not written into
Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/RIDGE_ENTER_DOUBLED_PAIRING_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/RIDGE_ENTER_DOUBLED_PAIRING_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Doubled-axis versus body-diagonal reverse under the named "
    "ridge-enter hop-cost on B_12(0) is reported for available "
    "k=1..4. Displayed, not adopted."
)

RADIUS = 12
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
RIDGE_ENTER_SRC = (2, 1, 0)
RIDGE_ENTER_DST = (2, 1, 1)
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
Site = tuple[int, int, int]


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


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(self, sites: frozenset[Site], origin: Site) -> dict[Site, int]:
        self.calls += 1
        infinity = 10**9
        dist = {site: infinity for site in sites}
        dist[origin] = 0
        queue: list[tuple[int, Site]] = [(0, origin)]
        while queue:
            cost, site = heapq.heappop(queue)
            if cost != dist[site]:
                continue
            for step in STEPS:
                neighbor = add(site, step)
                if neighbor not in dist:
                    continue
                candidate = cost + kappa_cost(site, neighbor)
                if candidate < dist[neighbor]:
                    dist[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))
        return dist


def add(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def coordinate_sum(site: Site) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def support_size(site: Site) -> int:
    return int(site[0] != 0) + int(site[1] != 0) + int(site[2] != 0)


def least_nonzero_abs(site: Site) -> int | None:
    nonzero = [abs(coordinate) for coordinate in site if coordinate != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_coord_count(site: Site) -> int:
    return (
        int(abs(site[0]) == 1)
        + int(abs(site[1]) == 1)
        + int(abs(site[2]) == 1)
    )


def ball_sites(radius: int) -> frozenset[Site]:
    return frozenset(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


def nu_cost(source: Site, dest: Site) -> int:
    source_support = support_size(source)
    dest_support = support_size(dest)
    if (
        source_support == 0
        or (source_support == 1 and dest_support == 1)
        or dest_support < source_support
    ):
        return 3
    return 1


def mu_cost(source: Site, dest: Site) -> int:
    if nu_cost(source, dest) == 3:
        return 3
    if (
        support_size(source) == 2
        and support_size(dest) == 2
        and least_nonzero_abs(dest) == 1
    ):
        return 3
    return 1


def rho3_cost(source: Site, dest: Site) -> int:
    if mu_cost(source, dest) == 3:
        return 3
    if (
        support_size(source) == 3
        and support_size(dest) == 3
        and unit_coord_count(dest) == 2
    ):
        return 3
    return 1


def kappa_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if (
        support_size(source) == 2
        and support_size(dest) == 3
        and unit_coord_count(dest) == 2
    ):
        return 3
    return 1


def walk_cost(path: tuple[Site, ...]) -> int:
    total = 0
    for source, dest in zip(path, path[1:]):
        total += kappa_cost(source, dest)
    return total


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
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
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor graph B_12(0) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and one Dijkstra; no fit and "
        "no second graph search"
    )
    print("claim_scope: " + CLAIM_SCOPE)
    print("cache_write: false")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(self_source) == AUDIT_INPUT_PATHS,
    )

    sites = ball_sites(RADIUS)
    origin = (0, 0, 0)
    counter = DijkstraCounter()
    dist = counter.distances(sites, origin)
    t_far_axis = dist[(12, 0, 0)]

    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {counter.calls}")
    print(f"t(12,0,0) = {t_far_axis}")

    pairing: list[tuple[int, int, int, bool, str]] = []
    all_in_ball = True
    all_reverse = True
    for k in range(1, 5):
        axis = (2 * k, 0, 0)
        body = (k, k, k)
        in_ball = axis in sites and body in sites
        all_in_ball = all_in_ball and in_ball
        t_axis = dist[axis]
        t_body = dist[body]
        lhs = 3 * t_axis * t_axis
        rhs = 4 * t_body * t_body
        reverse = lhs > rhs
        all_reverse = all_reverse and reverse
        product = f"{lhs} > {rhs}"
        pairing.append((k, t_axis, t_body, reverse, product))
        print(
            f"k {k} t({2 * k},0,0) = {t_axis} t({k},{k},{k}) = {t_body} "
            f"t_axis^2/(4k^2) = {t_axis * t_axis}/{4 * k * k} "
            f"t_body^2/(3k^2) = {t_body * t_body}/{3 * k * k} "
            f"3 t_axis^2 = {lhs} 4 t_body^2 = {rhs} reverse={reverse}"
        )

    in_ball_new = 0
    for site in sites:
        for step in STEPS:
            neighbor = add(site, step)
            if neighbor not in sites:
                continue
            if kappa_cost(site, neighbor) == 3 and rho3_cost(site, neighbor) == 1:
                in_ball_new += 1
    print(f"ridge_enter_live_hops {in_ball_new}")

    checks.check(
        "ball-cardinality",
        "B_12(0) is the 2625-site integer set with coordinate-sum at most 12",
        len(sites) == 2625
        and origin in sites
        and (8, 0, 0) in sites
        and (4, 4, 4) in sites,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1 and "DijkstraCounter" in self_source,
    )
    checks.check(
        "reachable",
        "every site of B_12(0) is reached",
        all(dist[site] < 10**9 for site in sites) and len(dist) == 2625,
    )
    checks.check(
        "pairs-available",
        "both sites of each k=1..4 pair lie in B_12(0)",
        all_in_ball
        and coordinate_sum((8, 0, 0)) == 8
        and coordinate_sum((4, 4, 4)) == 12
        and "no pair is omitted" in note,
    )
    checks.check(
        "hop-origin",
        "the unique origin hop has named cost 3",
        kappa_cost(origin, (1, 0, 0)) == 3 and nu_cost(origin, (1, 0, 0)) == 3,
    )
    checks.check(
        "hop-axis-axis",
        "a same-support axis hop has named cost 3",
        kappa_cost((1, 0, 0), (2, 0, 0)) == 3,
    )
    checks.check(
        "hop-body-last-untaxed",
        "the 2-to-3 hop into (1,1,1) is not priced by the extra clause",
        kappa_cost((1, 1, 0), (1, 1, 1)) == 1
        and rho3_cost((1, 1, 0), (1, 1, 1)) == 1
        and unit_coord_count((1, 1, 1)) == 3,
    )
    checks.check(
        "hop-ridge-enter-clause",
        "the named 2-to-3 two-unit dest clause prices (2,1,0) to (2,1,1) at 3",
        kappa_cost(RIDGE_ENTER_SRC, RIDGE_ENTER_DST) == 3
        and rho3_cost(RIDGE_ENTER_SRC, RIDGE_ENTER_DST) == 1
        and RIDGE_ENTER_SRC in sites
        and RIDGE_ENTER_DST in sites,
    )
    checks.check(
        "ridge-enter-live-on-ball",
        "nearest-neighbor hops inside B_12(0) trigger the extra 2-to-3 clause",
        in_ball_new > 0,
    )
    checks.check(
        "hop-rho3-ridge",
        "a 3-to-3 hop whose dest has exactly two unit coordinates has cost 3",
        kappa_cost((1, 1, 1), (2, 1, 1)) == 3
        and rho3_cost((1, 1, 1), (2, 1, 1)) == 3,
    )
    witness = {
        (2, 0, 0): ((0, 0, 0), (1, 0, 0), (2, 0, 0)),
        (1, 1, 1): ((0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)),
        (4, 0, 0): ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)),
        (2, 2, 2): (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 2),
            (0, 2, 2),
            (1, 2, 2),
            (2, 2, 2),
        ),
        (6, 0, 0): (
            (0, 0, 0),
            (1, 0, 0),
            (2, 0, 0),
            (3, 0, 0),
            (4, 0, 0),
            (5, 0, 0),
            (6, 0, 0),
        ),
        (3, 3, 3): (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 2),
            (0, 2, 2),
            (0, 3, 2),
            (0, 3, 3),
            (1, 3, 3),
            (2, 3, 3),
            (3, 3, 3),
        ),
        (8, 0, 0): (
            (0, 0, 0),
            (0, -1, 0),
            (1, -1, 0),
            (1, -2, 0),
            (2, -2, 0),
            (3, -2, 0),
            (4, -2, 0),
            (5, -2, 0),
            (6, -2, 0),
            (7, -2, 0),
            (8, -2, 0),
            (8, -1, 0),
            (8, 0, 0),
        ),
        (4, 4, 4): (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 2),
            (0, 2, 2),
            (0, 3, 2),
            (0, 4, 2),
            (0, 4, 3),
            (0, 4, 4),
            (1, 4, 4),
            (2, 4, 4),
            (3, 4, 4),
            (4, 4, 4),
        ),
    }
    witness_ok = True
    extra_off_witness = True
    for target, path in witness.items():
        if walk_cost(path) != dist[target]:
            witness_ok = False
        for source, dest in zip(path, path[1:]):
            if kappa_cost(source, dest) == 3 and rho3_cost(source, dest) == 1:
                extra_off_witness = False
    checks.check(
        "thm1-witness-walks",
        "each displayed pairing site has a walk whose cost matches Dijkstra",
        witness_ok and all(dist[target] > 0 for target in witness),
    )
    checks.check(
        "extra-clause-off-pairing-walks",
        "the extra 2-to-3 clause does not fire on the displayed pairing walks",
        extra_off_witness,
    )

    times_in_note = True
    products_in_note = True
    for k, t_axis, t_body, reverse, product in pairing:
        axis_line = f"t({2 * k},0,0) = {t_axis}"
        body_line = f"t({k},{k},{k}) = {t_body}"
        times_in_note = times_in_note and axis_line in note and body_line in note
        products_in_note = products_in_note and product in note
        checks.check(
            f"thm1-k{k}",
            f"t({2 * k},0,0) and t({k},{k},{k}) are computed and reported",
            t_axis > 0 and t_body > 0 and axis_line in note and body_line in note,
        )
        checks.check(
            f"thm2-k{k}",
            f"t({2 * k},0,0)^2/(4k^2) > t({k},{k},{k})^2/(3k^2) is {reverse}",
            reverse and product in note,
        )

    checks.check(
        "thm1-note-reports-times",
        "the note reports all eight computed pairing arrivals",
        times_in_note and f"t(12,0,0) = {t_far_axis}" in note,
    )
    checks.check(
        "thm2-reverse-holds",
        "the doubled-pairing inequality holds at every available k=1..4",
        all_reverse and products_in_note,
    )
    checks.check(
        "thm2-note-reports-comparison",
        "the note reports the integer comparisons and does not adopt them",
        products_in_note and "Displayed, not adopted" in note,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and does not name kappa",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "kappa" not in axiom
        and "κ" not in axiom
        and "Do not write κ into Admissibility." in note,
    )
    checks.check(
        "thm3-no-l1-attachment",
        "the note refuses to attach L1 and does not score a unit hop-cost",
        "Do not attach L1." in note
        and "attach L1" in note
        and "unit hop-cost" not in note.lower(),
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    checks.check(
        "forbidden-tokens",
        "forbidden tokens are absent from the note",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "claim-scope-contract",
        "the required claim_scope is source-visible",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "uniqueness-not-claimed",
        "the note does not claim uniqueness of the named hop-cost",
        "Uniqueness is not claimed" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_12(0) and proposes no axiom edit",
        "B_12(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "one Dijkstra" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "κ(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1 or 3 on nearest-neighbor hops.")
    print(
        "per_site: arrival times are reported at the doubled pairing sites "
        "and at (12,0,0)."
    )
    print("lattice_wide: checked and not executed — the search stays inside B_12(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
