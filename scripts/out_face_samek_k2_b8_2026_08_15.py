#!/usr/bin/env python3
"""Score same-k reverse at k=2 under ω on B_8(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/OUT_FACE_SAMEK_K2_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OUT_FACE_SAMEK_K2_B8_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=2 under the named out-face hop-cost "
    "on B_8(0) is reported. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
DIJKSTRA_CALLS = 0


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


def l1(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def support_size(v: tuple[int, int, int]) -> int:
    return int(v[0] != 0) + int(v[1] != 0) + int(v[2] != 0)


def least_nonzero_abs(v: tuple[int, int, int]) -> int | None:
    nonzero = [abs(c) for c in v if c != 0]
    if not nonzero:
        return None
    return min(nonzero)


def unit_coord_count(v: tuple[int, int, int]) -> int:
    return int(abs(v[0]) == 1) + int(abs(v[1]) == 1) + int(abs(v[2]) == 1)


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
    if support_size(v) == 2 and support_size(w) == 2 and least_nonzero_abs(w) == 1:
        return 3
    return 1


def rho3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if support_size(v) == 3 and support_size(w) == 3 and unit_coord_count(w) == 2:
        return 3
    return 1


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if (
        support_size(v) == 2
        and support_size(w) == 2
        and max(abs(c) for c in w) > max(abs(c) for c in v)
    ):
        return 3
    return 1


def mid_leave_would_fire(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return (
        support_size(v) == 1
        and support_size(w) == 2
        and max(abs(coord) for coord in w) == 1
        and max(abs(coord) for coord in v) >= 2
    )


def dijkstra_omega(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
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
            nd = d + omega_cost(v, w)
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


def path_cost(
    walk: tuple[tuple[int, int, int], ...],
    cost_fn,
) -> int:
    return sum(cost_fn(a, b) for a, b in zip(walk, walk[1:]))


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
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the rule is displayed, not adopted",
        "Displayed, not adopted" in note or "displayed, not adopted" in note,
    )
    checks.check(
        "not-in-admissibility",
        "ω is not written into Admissibility",
        "Do not write ω into Admissibility" in note
        and "Do not write `ω` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
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

    sites = ball(8)
    site_set = set(sites)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_omega(sites)
    t200 = dist[(2, 0, 0)]
    t222 = dist[(2, 2, 2)]
    t800 = dist[(8, 0, 0)]
    t320 = dist[(3, 2, 0)]
    reverse = 3 * t200 * t200 > t222 * t222
    witness_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (2, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 2, 2),
    )
    witness_out_face = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
    )
    witness_axis_costs = [omega_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])]
    witness_body_costs = [omega_cost(a, b) for a, b in zip(witness_body, witness_body[1:])]
    unit_face_grow = ((1, 1, 0), (2, 1, 0))
    out_face_hop = ((2, 2, 0), (3, 2, 0))
    height2_nongrow = ((1, -2, 0), (2, -2, 0))
    print(f"n_sites {len(sites)}")
    print(f"t(2,0,0) {t200}")
    print(f"t(2,2,2) {t222}")
    print(f"t(2,0,0)^2/4 {t200 * t200}/4")
    print(f"t(2,2,2)^2/12 {t222 * t222}/12")
    print(f"3 t(2,0,0)^2 {3 * t200 * t200}")
    print(f"t(2,2,2)^2 {t222 * t222}")
    print(f"reverse {reverse}")
    print(f"t(8,0,0) {t800}")
    print(f"t(3,2,0) {t320}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_axis_sum {sum(witness_axis_costs)}")
    print(f"witness_body_sum {sum(witness_body_costs)}")
    print(f"omega_out_face {omega_cost(*out_face_hop)}")
    print(f"rho3_out_face {rho3_cost(*out_face_hop)}")
    print(f"witness_out_face_omega {path_cost(witness_out_face, omega_cost)}")
    print(f"witness_out_face_rho3 {path_cost(witness_out_face, rho3_cost)}")

    mid_leave_hits = 0
    for v in sites:
        vx, vy, vz = v
        for dx, dy, dz in NEIGH:
            w = (vx + dx, vy + dy, vz + dz)
            if w in site_set and mid_leave_would_fire(v, w):
                mid_leave_hits += 1

    checks.check(
        "theorem-1",
        f"t(2,0,0)={t200} and t(2,2,2)={t222}",
        t200 == 6
        and t222 == 10
        and t200 == sum(witness_axis_costs)
        and t222 == sum(witness_body_costs),
    )
    checks.check(
        "reverse-k2",
        "t(2,0,0)^2 / 4 > t(2,2,2)^2 / 12",
        reverse
        and 3 * t200 * t200 == 108
        and t222 * t222 == 100
        and "108 > 100" in note
        and "inequality holds" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b8",
        "B_8(0) has 833 sites and 832 nonzero sites",
        len(sites) == 833 and len(nonzero) == 832 and all(l1(v) <= 8 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_8(0) is reached",
        len(dist) == 833,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`(2,0,0)`" in note and "`(2,2,2)`" in note and "`6`" in note and "`10`" in note,
    )
    checks.check(
        "note-records-reverse-product",
        "note records the integer reverse comparison",
        "108 > 100" in note,
    )
    checks.check(
        "out-face-hop",
        "the named out-face hop (1,1,0)->(2,1,0) has ω=3",
        omega_cost(*unit_face_grow) == 3
        and support_size((1, 1, 0)) == 2
        and support_size((2, 1, 0)) == 2
        and max(abs(c) for c in (2, 1, 0)) > max(abs(c) for c in (1, 1, 0))
        and "(1,1,0) → (2,1,0)" in note,
    )
    checks.check(
        "mid-leave-cannot-fire",
        "mid-leave dest-max=1 and source-max>=2 never both hold on 6-NN",
        mid_leave_hits == 0 and "cannot fire" in note,
    )
    checks.check(
        "omega-not-leftover-of-rho3",
        "face-growth (2,2,0)->(3,2,0) is ω=3 and ρ3=1",
        omega_cost(*out_face_hop) == 3
        and rho3_cost(*out_face_hop) == 1
        and mu_cost(*out_face_hop) == 1
        and omega_cost(*height2_nongrow) == 1
        and t320 == 11
        and path_cost(witness_out_face, omega_cost) == 11
        and path_cost(witness_out_face, rho3_cost) == 9
        and "(2,2,0) → (3,2,0)" in note
        and "cannot price out-face" in note
        and "new clause is live" in note,
    )
    checks.check(
        "k2-geodesic-costs",
        "the k=2 body path uses ω costs 3,1,1,3,1,1",
        witness_body_costs == [3, 1, 1, 3, 1, 1]
        and witness_axis_costs == [3, 3]
        and sum(witness_body_costs) == t222
        and sum(witness_axis_costs) == t200,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        omega_cost((0, 0, 0), (1, 0, 0)) == 3
        and omega_cost((1, 0, 0), (2, 0, 0)) == 3
        and omega_cost((1, 0, 0), (1, 1, 0)) == 1
        and omega_cost((1, 1, 0), (1, 1, 1)) == 1
        and omega_cost((1, 1, 0), (1, 0, 0)) == 3
        and omega_cost((1, 1, 1), (2, 1, 1)) == 3
        and omega_cost((2, 2, 1), (2, 2, 2)) == 1
        and omega_cost((2, 2, 0), (3, 2, 0)) == 3
        and t800 == 24,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ω(v→w)" not in axiom,
    )
    checks.check(
        "one-dijkstra-in-note",
        "the theorem stays on B_8(0) and uses one Dijkstra",
        "B_8(0)" in note and "one Dijkstra" in note and "One Dijkstra" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
