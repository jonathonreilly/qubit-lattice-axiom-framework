#!/usr/bin/env python3
"""Same-k reverse at k=13 under the named ridge-enter hop-cost on B_39(0).

One Dijkstra from the origin on the finite nearest-neighbor graph. The
ridge-enter hop-cost is displayed, not adopted, and is not written into
Admissibility. No cache or governance surface is written.
"""

from __future__ import annotations

import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "RIDGE_ENTER_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/RIDGE_ENTER_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

RADIUS = 39
K = 13
AXIS = (13, 0, 0)
BODY = (13, 13, 13)
FACE = (1, 1, 0)
RIDGE_ENTER_SRC = (2, 1, 0)
RIDGE_ENTER_DST = (2, 1, 1)
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
Site = tuple[int, int, int]


def add(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def support_size(site: Site) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


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
    if support_size(source) == 2 and support_size(dest) == 2:
        nonzero = [abs(coordinate) for coordinate in dest if coordinate != 0]
        if min(nonzero) == 1:
            return 3
    return 1


def rho3_cost(source: Site, dest: Site) -> int:
    if mu_cost(source, dest) == 3:
        return 3
    if support_size(source) == 3 and support_size(dest) == 3:
        absolute = [abs(coordinate) for coordinate in dest]
        if sum(1 for value in absolute if value == 1) == 2:
            return 3
    return 1


def kappa_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if support_size(source) == 2 and support_size(dest) == 3:
        absolute = [abs(coordinate) for coordinate in dest]
        if sum(1 for value in absolute if value == 1) == 2:
            return 3
    return 1


def path_cost(path: list[Site]) -> int:
    return sum(kappa_cost(path[i], path[i + 1]) for i in range(len(path) - 1))


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


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor graph B_39(0) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and one Dijkstra; no fit and "
        "no second graph search"
    )
    print(
        "claim_boundary: same-k reverse at k=13 is displayed, not adopted"
    )

    sites = ball_sites(RADIUS)
    origin = (0, 0, 0)
    counter = DijkstraCounter()
    dist = counter.distances(sites, origin)
    t_axis = dist[AXIS]
    t_body = dist[BODY]
    reverse = 3 * t_axis * t_axis > t_body * t_body

    print(f"t(13,0,0) = {t_axis}")
    print(f"t(13,13,13) = {t_body}")
    print(
        f"same-k comparison: {t_axis}^2 / 169 = {t_axis * t_axis}/169 versus "
        f"{t_body}^2 / 507 = {t_body * t_body}/507; reverse={reverse}"
    )

    axis_witness = (
        [origin, (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0)]
        + [(x, 2, 0) for x in range(3, 14)]
        + [(13, 1, 0), AXIS]
    )
    body_witness = (
        [origin, (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0)]
        + [(x, 2, 0) for x in range(3, 14)]
        + [(13, y, 0) for y in range(3, 14)]
        + [(13, 13, z) for z in range(1, 14)]
    )
    axis_path_cost = path_cost(axis_witness)
    body_path_cost = path_cost(body_witness)

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/RIDGE_ENTER_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "ball-cardinality",
        "B_39(0) is the 82239-site integer set with coordinate-sum at most 39",
        len(sites) == 82239 and origin in sites and AXIS in sites and BODY in sites,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1 and "DijkstraCounter" in self_source,
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
        "hop-support-rise",
        "the displayed k=1 body last hop keeps cost 1",
        kappa_cost((1, 0, 0), FACE) == 1 and kappa_cost(FACE, (1, 1, 1)) == 1,
    )
    checks.check(
        "hop-body-last-untaxed",
        "the 2-to-3 hop into (1,1,1) is not priced by the extra clause",
        kappa_cost(FACE, (1, 1, 1)) == 1
        and rho3_cost(FACE, (1, 1, 1)) == 1
        and sum(1 for value in (1, 1, 1) if abs(value) == 1) == 3,
    )
    checks.check(
        "hop-k13-body-enter-untaxed",
        "the witness 2-to-3 hop into (13,13,1) is not priced by the extra clause",
        kappa_cost((13, 13, 0), (13, 13, 1)) == 1
        and rho3_cost((13, 13, 0), (13, 13, 1)) == 1
        and sum(1 for value in (13, 13, 1) if abs(value) == 1) == 1,
    )
    checks.check(
        "hop-rho3-ridge",
        "a 3-to-3 hop whose dest has exactly two unit coordinates has cost 3",
        kappa_cost((2, 1, 1), (3, 1, 1)) == 3
        and rho3_cost((2, 1, 1), (3, 1, 1)) == 3,
    )
    checks.check(
        "hop-ridge-enter-clause",
        "the named 2-to-3 two-unit dest clause prices (2,1,0) to (2,1,1) at 3",
        kappa_cost(RIDGE_ENTER_SRC, RIDGE_ENTER_DST) == 3
        and rho3_cost(RIDGE_ENTER_SRC, RIDGE_ENTER_DST) == 1
        and RIDGE_ENTER_SRC in sites
        and RIDGE_ENTER_DST in sites,
    )
    in_ball_new = 0
    for site in sites:
        for step in STEPS:
            neighbor = add(site, step)
            if neighbor not in sites:
                continue
            if kappa_cost(site, neighbor) == 3 and rho3_cost(site, neighbor) == 1:
                in_ball_new += 1
    checks.check(
        "ridge-enter-live-on-ball",
        "nearest-neighbor hops inside B_39(0) trigger the extra 2-to-3 clause",
        in_ball_new > 0,
    )
    checks.check(
        "thm1-axis-time",
        "t(13,0,0) equals the computed origin-to-axis arrival time",
        t_axis == axis_path_cost and t_axis > 0,
    )
    checks.check(
        "thm1-body-time",
        "t(13,13,13) equals the computed origin-to-body arrival time",
        t_body == body_path_cost and t_body > 0,
    )
    checks.check(
        "thm2-reverse-holds",
        "t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507 holds on the computed times",
        reverse and 3 * t_axis * t_axis > t_body * t_body,
    )
    checks.check(
        "thm1-note-reports-times",
        "the note reports the computed arrival times",
        f"t(13,0,0) = {t_axis}" in note and f"t(13,13,13) = {t_body}" in note,
    )
    checks.check(
        "thm2-note-reports-comparison",
        "the note reports the integer same-k comparison and does not adopt it",
        f"{3 * t_axis * t_axis} > {t_body * t_body}" in note
        and "Displayed, not adopted" in note,
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
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-tokens",
        "forbidden tokens are absent from the note",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "claim-scope-contract",
        "the required claim_scope is source-visible",
        "Same-k reverse at k=13 under the named ridge-enter hop-cost on B_39(0) is reported. Displayed, not adopted."
        in note,
    )
    checks.check(
        "uniqueness-not-claimed",
        "the note does not claim uniqueness of the named hop-cost",
        "Uniqueness is not claimed" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_39(0) and proposes no axiom edit",
        "B_39(0)" in note
        and "hypothetical_axiom_status: \"no edit\"" in note
        and "one Dijkstra" in note,
    )

    print("per_element: named hop-cost values are 1 or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported only at (13,0,0) and (13,13,13).")
    print("lattice_wide: checked and not executed — the search stays inside B_39(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
