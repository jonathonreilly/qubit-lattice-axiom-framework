#!/usr/bin/env python3
"""Unread-site deletion versus named c2d4 reverse and face bits at k=1 on B_6(0).

Two Dijkstras from the origin: first on the finite nearest-neighbor graph
B_6(0), then on B_6(0) minus the unread witness (2,0,0). Reverse and face
bits are displayed, not adopted. Hop-costs are not written into
Admissibility. L1 is not attached. No cache or governance surface is written.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "UNREAD_SITE_DELETION_VS_C2D4_REVERSE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/UNREAD_SITE_DELETION_VS_C2D4_REVERSE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Same-k reverse and face at k=1 under named c2d4 on B_6(0) "
    "versus B_6(0) minus unread (2,0,0) is compared. Displayed, not adopted."
)

RADIUS = 6
ORIGIN = (0, 0, 0)
AXIS = (1, 0, 0)
BODY = (1, 1, 1)
FACE = (1, 1, 0)
UNREAD = (2, 0, 0)
RECORDED = frozenset({ORIGIN, AXIS, FACE, BODY})
MAX4_OUT_SRC = (4, 2, 0)
MAX4_OUT_DST = (5, 2, 0)
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
Site = tuple[int, int, int]
INFINITY = 10**9


def add(site: Site, step: Site) -> Site:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def support_size(site: Site) -> int:
    return sum(1 for coordinate in site if coordinate != 0)


def unit_coord_count(site: Site) -> int:
    return sum(1 for coordinate in site if abs(coordinate) == 1)


def max_abs(site: Site) -> int:
    return max(abs(coordinate) for coordinate in site)


def min_nonzero_abs(site: Site) -> int | None:
    nonzero = [abs(coordinate) for coordinate in site if coordinate != 0]
    if not nonzero:
        return None
    return min(nonzero)


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
        least = min_nonzero_abs(dest)
        if least == 1:
            return 3
    return 1


def rho3_cost(source: Site, dest: Site) -> int:
    if mu_cost(source, dest) == 3:
        return 3
    if support_size(source) == 3 and support_size(dest) == 3:
        if unit_coord_count(dest) == 2:
            return 3
    return 1


def d4_extra(source: Site, dest: Site) -> bool:
    return (
        support_size(source) == 2
        and support_size(dest) == 2
        and max_abs(dest) > max_abs(source)
        and max_abs(source) >= 4
    )


def c2d4_cost(source: Site, dest: Site) -> int:
    if rho3_cost(source, dest) == 3:
        return 3
    if d4_extra(source, dest):
        return 2
    return 1


def reverse_bit(t_axis: int, t_body: int) -> bool:
    return 3 * t_axis * t_axis > t_body * t_body


def face_bit(t_face_axis: int, t_face: int) -> bool:
    return t_face_axis * t_face_axis > 2 * t_face * t_face


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(self, sites: frozenset[Site], origin: Site) -> dict[Site, int]:
        self.calls += 1
        dist = {site: INFINITY for site in sites}
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
                candidate = cost + c2d4_cost(site, neighbor)
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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print(
        "external_scientific_inputs: none; named c2d4 on B_6(0) versus "
        "B_6(0) minus unread (2,0,0) only"
    )
    print(
        "package_local_integrity_reads: proposed source note and live axiom "
        "memo only; no cache or governance surface is written"
    )
    print(
        "measure_boundary: integer hop-costs and two Dijkstras; no fit and "
        "no leftover larger-ball table"
    )
    print(
        "claim_boundary: same-k reverse and face bits at k=1 are displayed, "
        "not adopted"
    )

    sites = ball_sites(RADIUS)
    sites_punct = frozenset(site for site in sites if site != UNREAD)
    counter = DijkstraCounter()
    dist_full = counter.distances(sites, ORIGIN)
    dist_punct = counter.distances(sites_punct, ORIGIN)

    t_axis = dist_full[AXIS]
    t_body = dist_full[BODY]
    t_unread = dist_full[UNREAD]
    t_face = dist_full[FACE]
    reverse_full = reverse_bit(t_axis, t_body)
    face_full = face_bit(t_unread, t_face)

    punct_unread_absent = UNREAD not in dist_punct
    t_axis_p = dist_punct[AXIS]
    t_body_p = dist_punct[BODY]
    t_face_p = dist_punct[FACE]
    reverse_punct = reverse_bit(t_axis_p, t_body_p)
    face_punct_defined = not punct_unread_absent
    recorded_times_same = all(dist_full[site] == dist_punct[site] for site in RECORDED)
    reverse_moved = reverse_full != reverse_punct
    defined_bit_moved = reverse_moved or (
        face_punct_defined and face_full != face_bit(dist_punct[UNREAD], t_face_p)
    )

    print(f"n_sites_full {len(sites)}")
    print(f"n_sites_punct {len(sites_punct)}")
    print(f"R {sorted(RECORDED)}")
    print(f"unread_witness {UNREAD}")
    print(f"full t(1,0,0) = {t_axis}")
    print(f"full t(1,1,1) = {t_body}")
    print(f"full t(2,0,0) = {t_unread}")
    print(f"full t(1,1,0) = {t_face}")
    print(
        f"full reverse: {t_axis}^2 / 1 = {t_axis * t_axis} versus "
        f"{t_body}^2 / 3 = {t_body * t_body}/3; reverse={reverse_full}"
    )
    print(f"full 3 t(1,0,0)^2 = {3 * t_axis * t_axis}")
    print(f"full t(1,1,1)^2 = {t_body * t_body}")
    print(
        f"full face: {t_unread}^2 / 4 = {t_unread * t_unread}/4 versus "
        f"{t_face}^2 / 2 = {t_face * t_face}/2; face={face_full}"
    )
    print(f"full t(2,0,0)^2 = {t_unread * t_unread}")
    print(f"full 2 t(1,1,0)^2 = {2 * t_face * t_face}")
    print(f"punct t(1,0,0) = {t_axis_p}")
    print(f"punct t(1,1,1) = {t_body_p}")
    print("punct t(2,0,0) absent")
    print(f"punct t(1,1,0) = {t_face_p}")
    print(f"punct reverse={reverse_punct}")
    print("punct face undefined")
    print(f"recorded_times_same {recorded_times_same}")
    print(f"defined_bit_moved {defined_bit_moved}")
    print(f"dijkstra_calls {counter.calls}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/UNREAD_SITE_DELETION_VS_C2D4_REVERSE_B6_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "audit-input-literal",
        "AUDIT_INPUT_PATHS is a static string-literal tuple",
        literal_audit_paths(self_source) == AUDIT_INPUT_PATHS,
    )
    checks.check(
        "ball-cardinality",
        "B_6(0) is the 377-site integer set with coordinate-sum at most 6",
        len(sites) == 377
        and ORIGIN in sites
        and AXIS in sites
        and BODY in sites
        and FACE in sites
        and UNREAD in sites,
    )
    checks.check(
        "punctured-cardinality",
        "B_6(0) minus unread (2,0,0) has 376 sites",
        len(sites_punct) == 376
        and UNREAD not in sites_punct
        and RECORDED <= sites_punct,
    )
    checks.check(
        "recorded-set",
        "R is the four recorded sites and the unread witness is outside R",
        RECORDED == frozenset({ORIGIN, AXIS, FACE, BODY})
        and UNREAD not in RECORDED
        and UNREAD in sites,
    )
    checks.check(
        "two-dijkstras",
        "exactly two Dijkstras from the origin are executed, full ball then ball minus u",
        counter.calls == 2
        and "dist_full = counter.distances(sites, ORIGIN)" in self_source
        and "dist_punct = counter.distances(sites_punct, ORIGIN)" in self_source
        and self_source.index("dist_full = counter.distances(sites, ORIGIN)")
        < self_source.index("dist_punct = counter.distances(sites_punct, ORIGIN)"),
    )
    checks.check(
        "reachable-full",
        "every site of B_6(0) is reached on the full ball",
        all(dist_full[site] < INFINITY for site in sites),
    )
    checks.check(
        "reachable-punct-recorded",
        "every recorded site remains reached on the punctured ball",
        all(dist_punct[site] < INFINITY for site in RECORDED)
        and all(dist_punct[site] < INFINITY for site in sites_punct),
    )
    checks.check(
        "c2d4-clauses",
        "seed-exit and axis cost 3; body and face-support hops cost 1; max>=4 out-face costs 2",
        c2d4_cost(ORIGIN, AXIS) == 3
        and c2d4_cost(AXIS, UNREAD) == 3
        and c2d4_cost(AXIS, FACE) == 1
        and c2d4_cost(FACE, BODY) == 1
        and c2d4_cost(MAX4_OUT_SRC, MAX4_OUT_DST) == 2
        and not d4_extra(AXIS, UNREAD),
    )
    axis_path = c2d4_cost(ORIGIN, AXIS)
    face_path = axis_path + c2d4_cost(AXIS, FACE)
    body_path = face_path + c2d4_cost(FACE, BODY)
    unread_path = axis_path + c2d4_cost(AXIS, UNREAD)
    checks.check(
        "thm1-arrivals",
        "on the full ball the four arrivals are the computed Dijkstra times",
        t_axis == 3
        and t_body == 5
        and t_unread == 6
        and t_face == 4
        and t_axis == axis_path
        and t_body == body_path
        and t_unread == unread_path
        and t_face == face_path,
    )
    checks.check(
        "thm1-reverse-face",
        "on the full ball reverse and face bits at k=1 both hold",
        reverse_full
        and face_full
        and 3 * t_axis * t_axis == 27
        and t_body * t_body == 25
        and t_unread * t_unread == 36
        and 2 * t_face * t_face == 32,
    )
    checks.check(
        "thm2-arrivals-punct",
        "on the punctured ball the recorded arrivals match and t(2,0,0) is absent",
        t_axis_p == 3
        and t_body_p == 5
        and t_face_p == 4
        and punct_unread_absent
        and recorded_times_same,
    )
    checks.check(
        "thm2-bits-if-defined",
        "on the punctured ball reverse remains true and face is undefined",
        reverse_punct
        and not face_punct_defined
        and reverse_punct == reverse_full,
    )
    checks.check(
        "thm3-no-defined-bit-move",
        "no defined reverse or face bit moves after deleting unread u",
        not defined_bit_moved
        and not reverse_moved
        and not face_punct_defined,
    )
    checks.check(
        "thm3-r-unchanged",
        "the recorded set R is unchanged by deleting unread u",
        UNREAD not in RECORDED
        and RECORDED <= sites
        and RECORDED <= sites_punct
        and recorded_times_same,
    )
    checks.check(
        "thm1-note-reports-full",
        "the note reports the full-ball arrivals and both bits",
        "t(1,0,0) = 3" in note
        and "t(1,1,1) = 5" in note
        and "t(2,0,0) = 6" in note
        and "t(1,1,0) = 4" in note
        and "9 > 25/3" in note
        and "27 > 25" in note
        and "36 > 32" in note,
    )
    checks.check(
        "thm2-note-reports-punct",
        "the note reports the punctured arrivals and undefined face bit",
        "t(2,0,0) is absent" in note
        and "The reverse bit does not move" in note
        and "The face bit is undefined" in note,
    )
    checks.check(
        "thm3-note-reports-comparison",
        "the note reports that no defined reverse or face bit moves and R is unchanged",
        "No defined reverse or face bit moves" in note
        and "Record set R is unchanged" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "thm3-not-in-admissibility",
        "the live Admissibility wording is unchanged and hop-costs are not written into it",
        "There is one fixed nearest-neighbor admissibility rule" in axiom
        and "c2d4(v→w)" not in axiom
        and "Do not write hop-costs into Admissibility." in note,
    )
    checks.check(
        "thm3-no-l1-attachment",
        "the note refuses to attach L1",
        "Do not attach L1." in note and "attach L1" in note,
    )
    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-tokens",
        "forbidden tokens are absent from the note",
        all(token not in note for token in forbidden),
    )
    checks.check(
        "claim-scope-contract",
        "the required claim_scope is source-visible",
        CLAIM_SCOPE in note.replace("\n", " ") and CLAIM_SCOPE in note,
    )
    checks.check(
        "uniqueness-not-required",
        "the note does not require uniqueness",
        "Uniqueness is not required" in note and "unique hop-cost" not in note,
    )
    checks.check(
        "scope-boundary",
        "the theorem stays on B_6(0), uses two Dijkstras, and proposes no axiom edit",
        "B_6(0)" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "Two Dijkstras" in note
        and "not leftover of a larger-ball table" in note
        and "B_" + "57" not in note
        and "B_" + "57" not in self_source,
    )
    checks.check(
        "displayed-not-adopted",
        "the comparison is displayed, not adopted",
        "Displayed, not adopted" in note
        and "unread witness" in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "A site with no record cannot be read." in axiom
        and "c2d4(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom,
    )
    checks.check(
        "no-path-dump",
        "the runner stores arrival costs only",
        ("pre" + "decessor") not in self_source.lower()
        and ("path " + "dump") not in self_source.lower()
        and ("path " + "dump") not in note.lower(),
    )
    checks.check(
        "record-unreadability",
        "the note quotes that a site with no record cannot be read",
        "A site with no record cannot be read." in note
        and "A site with no record cannot be read." in axiom,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print(
        "per_site: arrival times are reported at (1,0,0), (1,1,1), (2,0,0), and (1,1,0)."
    )
    print("lattice_wide: checked and not executed — the search stays inside B_6(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
