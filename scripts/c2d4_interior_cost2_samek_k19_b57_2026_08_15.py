#!/usr/bin/env python3
"""Score same-k reverse at k=19 under i2 on B_57(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/C2D4_INTERIOR_COST2_SAMEK_K19_B57_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/C2D4_INTERIOR_COST2_SAMEK_K19_B57_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=19 under the named c2d4-plus-interior "
    "hop-cost on B_57(0) is reported. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)


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


def coord_sum(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: tuple[int, int, int]) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def nu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1) or sigma_w < sigma_v:
        return 3
    return 1


def mu_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if nu_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        nonzero = [abs(coord) for coord in w if coord != 0]
        if nonzero and min(nonzero) == 1:
            return 3
    return 1


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3:
        if sum(abs(coord) == 1 for coord in w) == 2:
            return 3
    return 1


def c2d4_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if (
            max(abs(coord) for coord in w) > max(abs(coord) for coord in v)
            and max(abs(coord) for coord in v) >= 4
        ):
            return 2
    return 1


def i2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if c2d4_cost(v, w) == 2:
        return 2
    if support_size(v) == 3 and support_size(w) == 3:
        if min(abs(coord) for coord in w) >= 2:
            return 2
    return 1


def path_cost(path: list[tuple[int, int, int]]) -> int:
    return sum(i2_cost(a, b) for a, b in zip(path, path[1:]))


class DijkstraCounter:
    def __init__(self) -> None:
        self.calls = 0

    def distances(
        self, sites: list[tuple[int, int, int]]
    ) -> dict[tuple[int, int, int], int]:
        self.calls += 1
        site_set = set(sites)
        dist: dict[tuple[int, int, int], int] = {(0, 0, 0): 0}
        heap: list[tuple[int, tuple[int, int, int]]] = [(0, (0, 0, 0))]
        seen: set[tuple[int, int, int]] = set()
        while heap:
            d, v = heapq.heappop(heap)
            if v in seen:
                continue
            seen.add(v)
            vx, vy, vz = v
            for dx, dy, dz in NEIGH:
                w = (vx + dx, vy + dy, vz + dz)
                if w not in site_set:
                    continue
                nd = d + i2_cost(v, w)
                if nd < dist.get(w, 10**9):
                    dist[w] = nd
                    heapq.heappush(heap, (nd, w))
        return dist


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print(
        "external_scientific_inputs: none; named hop-cost on the finite "
        "nearest-neighbor graph B_57(0) only"
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
        "claim_boundary: same-k reverse at k=19 is displayed, not adopted"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs are the source note and the current axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
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
        CLAIM_SCOPE in note.replace("\n", " ") and CLAIM_SCOPE in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "i2 is not written into Admissibility",
        "Do not write i2 into Admissibility." in note
        and "Do not write `i2` into Admissibility." in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1." in note and "Do not attach L1." not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note,
    )
    checks.check(
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note]
    checks.check(
        "forbidden-absent",
        "forbidden phrases are absent from the source note",
        forbidden_hits == [],
    )
    checks.check(
        "cache-false",
        "the note records cache_write false",
        "cache_write: false" in note,
    )

    sites = ball(57)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    counter = DijkstraCounter()
    dist = counter.distances(sites)
    t1900 = dist[(19, 0, 0)]
    t191919 = dist[(19, 19, 19)]
    t5700 = dist[(57, 0, 0)]
    t5400 = dist[(54, 0, 0)]
    t320 = dist[(3, 2, 0)]
    t420 = dist[(4, 2, 0)]
    t520 = dist[(5, 2, 0)]
    t221 = dist[(2, 2, 1)]
    t222 = dist[(2, 2, 2)]
    t19191 = dist[(19, 19, 1)]
    reverse = 3 * t1900 * t1900 > t191919 * t191919
    axis_sq = t1900 * t1900
    body_sq = t191919 * t191919
    axis_prod = 3 * axis_sq

    axis_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1)]
    axis_witness.extend((x, 2, 1) for x in range(2, 20))
    axis_witness.extend([(19, 2, 0), (19, 1, 0), (19, 0, 0)])
    body_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1), (2, 2, 1)]
    body_witness.extend((x, 2, 1) for x in range(3, 20))
    body_witness.extend((19, y, 1) for y in range(3, 20))
    body_witness.extend((19, 19, z) for z in range(2, 20))
    c2d4_body_walk = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 2, 0), (2, 2, 0), (2, 2, 1)]
    c2d4_body_walk.extend((2, 2, z) for z in range(2, 20))
    c2d4_body_walk.extend((2, y, 19) for y in range(3, 20))
    c2d4_body_walk.extend((x, 19, 19) for x in range(3, 20))
    interior_fire = ((2, 2, 1), (2, 2, 2))
    interior_grow = ((2, 2, 2), (3, 2, 2))
    interior_skip = ((2, 2, 1), (3, 2, 1))
    skip_hop = ((3, 2, 0), (4, 2, 0))
    fire_hop = ((4, 2, 0), (5, 2, 0))
    unit_out_face = ((1, 1, 0), (2, 1, 0))
    fire_witness = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
        (4, 2, 0),
        (5, 2, 0),
    ]
    interior_witness = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 2, 2),
    ]

    print(f"n_sites {len(sites)}")
    print(f"t(19,0,0) {t1900}")
    print(f"t(19,19,19) {t191919}")
    print(f"t(19,0,0)^2/361 {axis_sq}/361")
    print(f"t(19,19,19)^2/1083 {body_sq}/1083")
    print(f"3 t(19,0,0)^2 {axis_prod}")
    print(f"t(19,19,19)^2 {body_sq}")
    print(f"reverse {reverse}")
    print(f"t(57,0,0) {t5700}")
    print(f"t(54,0,0) {t5400}")
    print(f"t(3,2,0) {t320}")
    print(f"t(4,2,0) {t420}")
    print(f"t(5,2,0) {t520}")
    print(f"t(2,2,1) {t221}")
    print(f"t(2,2,2) {t222}")
    print(f"t(19,19,1) {t19191}")
    print(f"dijkstra_calls {counter.calls}")

    checks.check(
        "theorem-1",
        f"t(19,0,0)={t1900} and t(19,19,19)={t191919} match named witnesses",
        t1900 == path_cost(axis_witness)
        and t191919 == path_cost(body_witness)
        and t1900 > 0
        and t191919 > 0,
    )
    checks.check(
        "reverse-k19",
        "t(19,0,0)^2 / 361 > t(19,19,19)^2 / 1083 is false",
        (not reverse)
        and axis_prod < body_sq
        and f"{axis_prod} < {body_sq}" in note
        and "inequality does not hold" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra from the origin is executed",
        counter.calls == 1 and "DijkstraCounter" in source,
    )
    checks.check(
        "ball-b57",
        "B_57(0) has 253575 sites and 253574 nonzero sites",
        len(sites) == 253575
        and len(nonzero) == 253574
        and all(coord_sum(v) <= 57 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_57(0) is reached",
        len(dist) == 253575,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        f"t(19,0,0) = {t1900}" in note
        and f"t(19,19,19) = {t191919}" in note
        and "`(19,0,0)`" in note
        and "`(19,19,19)`" in note,
    )
    checks.check(
        "note-records-reverse-product",
        "note records the integer reverse comparison",
        f"{axis_prod} < {body_sq}" in note
        and f"{axis_sq}/361" in note
        and f"{body_sq}/1083" in note,
    )
    checks.check(
        "interior-fires",
        "i2 prices interior 3-to-3 dest-min>=2 hops at 2",
        i2_cost(*interior_fire) == 2
        and i2_cost(*interior_grow) == 2
        and c2d4_cost(*interior_fire) == 1
        and c2d4_cost(*interior_grow) == 1
        and rho3_cost(*interior_fire) == 1
        and rho3_cost(*interior_grow) == 1
        and min(abs(c) for c in interior_fire[1]) >= 2
        and min(abs(c) for c in interior_grow[1]) >= 2
        and t221 == 9
        and t222 == 11
        and path_cost(interior_witness) == 11
        and "(2,2,1) → (2,2,2)" in note
        and "(2,2,2) → (3,2,2)" in note
        and "`t(2,2,1) = 9`" in note
        and "`t(2,2,2) = 11`" in note,
    )
    checks.check(
        "interior-skips-hugging",
        "i2 extra skips 3-to-3 hops whose destination min abs is 1",
        i2_cost(*interior_skip) == 1
        and c2d4_cost(*interior_skip) == 1
        and rho3_cost(*interior_skip) == 1
        and min(abs(c) for c in interior_skip[1]) == 1
        and "(2,2,1) → (3,2,1)" in note,
    )
    checks.check(
        "skips-early-out-face",
        "i2 keeps (3,2,0)->(4,2,0) at cost 1",
        i2_cost(*skip_hop) == 1
        and c2d4_cost(*skip_hop) == 1
        and rho3_cost(*skip_hop) == 1
        and t320 == 9
        and t420 == 10
        and "(3,2,0) → (4,2,0)" in note
        and "`t(3,2,0) = 9`" in note
        and "`t(4,2,0) = 10`" in note,
    )
    checks.check(
        "fires-max4-out-face-at-2",
        "i2 keeps (4,2,0)->(5,2,0) at cost 2 from c2d4",
        i2_cost(*fire_hop) == 2
        and c2d4_cost(*fire_hop) == 2
        and rho3_cost(*fire_hop) == 1
        and t520 == path_cost(fire_witness)
        and path_cost(fire_witness) == 12
        and "(4,2,0) → (5,2,0)" in note
        and "`t(5,2,0) = 12`" in note,
    )
    checks.check(
        "unit-out-face-by-mu",
        "unit-out-face (1,1,0)->(2,1,0) is already ρ3=3 by corridor-slide",
        i2_cost(*unit_out_face) == 3
        and rho3_cost(*unit_out_face) == 3
        and mu_cost(*unit_out_face) == 3
        and "(1,1,0) → (2,1,0)" in note,
    )
    checks.check(
        "not-leftover-of-c2d4",
        "interior 3-to-3 dest-min>=2 is i2=2 and c2d4=1",
        i2_cost(*interior_fire) == 2
        and c2d4_cost(*interior_fire) == 1
        and t222 == 11
        and sum(c2d4_cost(a, b) for a, b in zip(c2d4_body_walk, c2d4_body_walk[1:]))
        == 61
        and path_cost(c2d4_body_walk) == 113
        and "cannot price interior 3→3 dest-min≥2" in note
        and "not leftover of `c2d4`" in note,
    )
    checks.check(
        "not-leftover-of-b54",
        "(19,19,19) lies outside B_54(0) and the note says so",
        coord_sum((19, 19, 19)) == 57
        and (19, 19, 19) in dist
        and t5700 == dist[(57, 0, 0)]
        and t5400 == dist[(54, 0, 0)]
        and f"t(57,0,0) = {t5700}" in note
        and f"t(54,0,0) = {t5400}" in note
        and "absent from `B_54(0)`" in note
        and "not leftover of the `B_54(0)` times" in note,
    )
    checks.check(
        "witness-arrivals",
        "named axis and body walks realize the computed arrivals",
        path_cost(axis_witness) == t1900
        and path_cost(body_witness) == t191919
        and axis_witness[-1] == (19, 0, 0)
        and body_witness[-1] == (19, 19, 19)
        and all(coord_sum(v) <= 57 for v in axis_witness)
        and all(coord_sum(v) <= 57 for v in body_witness)
        and t19191 == 43
        and "`t(19,19,1) = 43`" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        i2_cost((0, 0, 0), (1, 0, 0)) == 3
        and i2_cost((1, 0, 0), (2, 0, 0)) == 3
        and i2_cost((1, 0, 0), (1, 1, 0)) == 1
        and i2_cost((1, 1, 0), (1, 1, 1)) == 1
        and i2_cost((1, 1, 0), (1, 0, 0)) == 3
        and i2_cost((1, 1, 1), (2, 1, 1)) == 3,
    )
    checks.check(
        "i2-clauses",
        "seed-exit, axis, drop, corridor-slide, and ridge-slide cost 3; interior dest-min>=2 costs 2; hugging 3-to-3 and small 2-to-3 cost 1",
        i2_cost((0, 0, 0), (1, 0, 0)) == 3
        and i2_cost((1, 0, 0), (2, 0, 0)) == 3
        and i2_cost((1, 1, 0), (1, 0, 0)) == 3
        and i2_cost((1, 1, 0), (2, 1, 0)) == 3
        and i2_cost((1, 1, 1), (2, 1, 1)) == 3
        and i2_cost((4, 2, 0), (5, 2, 0)) == 2
        and i2_cost((2, 2, 2), (3, 2, 2)) == 2
        and i2_cost((2, 2, 1), (2, 2, 2)) == 2
        and i2_cost((19, 19, 1), (19, 19, 2)) == 2
        and i2_cost((2, 2, 1), (3, 2, 1)) == 1
        and i2_cost((1, 0, 0), (1, 1, 0)) == 1
        and i2_cost((1, 1, 0), (1, 1, 1)) == 1
        and i2_cost((3, 2, 0), (4, 2, 0)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "i2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom,
    )

    print("per_element: named hop-cost values are 1, 2, or 3 on nearest-neighbor hops.")
    print("per_site: arrival times are reported at (19,0,0) and (19,19,19).")
    print("lattice_wide: checked and not executed — the search stays inside B_57(0).")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
